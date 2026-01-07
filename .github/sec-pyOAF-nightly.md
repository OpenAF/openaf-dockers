````yaml
╭ [0] ╭ Target  : openaf/pyoaf:nightly (alpine 3.23.2) 
│     ├ Class   : os-pkgs 
│     ├ Type    : alpine 
│     ╰ Packages ╭ [0]  ╭ ID            : alpine-baselayout@3.7.1-r8 
│                │      ├ Name          : alpine-baselayout 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/alpine-baselayout@3.7.1-r8?arch=x86_64&distro=3
│                │      │                │       .23.2 
│                │      │                ╰ UID : 3b8c61777e21ddf4 
│                │      ├ Version       : 3.7.1-r8 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : alpine-baselayout 
│                │      ├ SrcVersion    : 3.7.1-r8 
│                │      ├ Licenses       ─ [0]: GPL-2.0-only 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: alpine-baselayout-data@3.7.1-r8 
│                │      │                ╰ [1]: busybox-binsh@1.37.0-r30 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:9a137c3c8e738bcabac13326c9fc5472fa58aaf4 
│                │      ╰ InstalledFiles ╭ [0] : etc/motd 
│                │                       ├ [1] : etc/crontabs/root 
│                │                       ├ [2] : etc/modprobe.d/aliases.conf 
│                │                       ├ [3] : etc/modprobe.d/blacklist.conf 
│                │                       ├ [4] : etc/modprobe.d/i386.conf 
│                │                       ├ [5] : etc/profile.d/20locale.sh 
│                │                       ├ [6] : etc/profile.d/README 
│                │                       ├ [7] : etc/profile.d/color_prompt.sh.disabled 
│                │                       ├ [8] : usr/lib/sysctl.d/00-alpine.conf 
│                │                       ├ [9] : var/lock 
│                │                       ├ [10]: var/run 
│                │                       ├ [11]: var/spool/mail 
│                │                       ╰ [12]: var/spool/cron/crontabs 
│                ├ [1]  ╭ ID            : alpine-baselayout-data@3.7.1-r8 
│                │      ├ Name          : alpine-baselayout-data 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/alpine-baselayout-data@3.7.1-r8?arch=x86_64&dis
│                │      │                │       tro=3.23.2 
│                │      │                ╰ UID : aaf48747bbe2abe1 
│                │      ├ Version       : 3.7.1-r8 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : alpine-baselayout 
│                │      ├ SrcVersion    : 3.7.1-r8 
│                │      ├ Licenses       ─ [0]: GPL-2.0-only 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:9a60b0edb4559ab279cf004b7e685cfd78dd0c15 
│                │      ╰ InstalledFiles ╭ [0] : etc/fstab 
│                │                       ├ [1] : etc/group 
│                │                       ├ [2] : etc/hostname 
│                │                       ├ [3] : etc/hosts 
│                │                       ├ [4] : etc/inittab 
│                │                       ├ [5] : etc/modules 
│                │                       ├ [6] : etc/mtab 
│                │                       ├ [7] : etc/nsswitch.conf 
│                │                       ├ [8] : etc/passwd 
│                │                       ├ [9] : etc/profile 
│                │                       ├ [10]: etc/protocols 
│                │                       ├ [11]: etc/services 
│                │                       ├ [12]: etc/shadow 
│                │                       ├ [13]: etc/shells 
│                │                       ╰ [14]: etc/sysctl.conf 
│                ├ [2]  ╭ ID            : alpine-keys@2.6-r0 
│                │      ├ Name          : alpine-keys 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/alpine-keys@2.6-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : a40d710a5174ffeb 
│                │      ├ Version       : 2.6-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : alpine-keys 
│                │      ├ SrcVersion    : 2.6-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:5c45a821cd6b84d543bbd7ff12a7de1855c5cd13 
│                │      ╰ InstalledFiles ╭ [0] : etc/apk/keys/alpine-devel@lists.alpinelinux.org-4a6a0840.rsa.pub 
│                │                       ├ [1] : etc/apk/keys/alpine-devel@lists.alpinelinux.org-5261cecb.rsa.pub 
│                │                       ├ [2] : etc/apk/keys/alpine-devel@lists.alpinelinux.org-6165ee59.rsa.pub 
│                │                       ├ [3] : usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-4a6a0840
│                │                       │       .rsa.pub 
│                │                       ├ [4] : usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-5243ef4b
│                │                       │       .rsa.pub 
│                │                       ├ [5] : usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-524d27bb
│                │                       │       .rsa.pub 
│                │                       ├ [6] : usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-5261cecb
│                │                       │       .rsa.pub 
│                │                       ├ [7] : usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-58199dcc
│                │                       │       .rsa.pub 
│                │                       ├ [8] : usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-58cbb476
│                │                       │       .rsa.pub 
│                │                       ├ [9] : usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-58e4f17d
│                │                       │       .rsa.pub 
│                │                       ├ [10]: usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-5e69ca50
│                │                       │       .rsa.pub 
│                │                       ├ [11]: usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-60ac2099
│                │                       │       .rsa.pub 
│                │                       ├ [12]: usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-6165ee59
│                │                       │       .rsa.pub 
│                │                       ├ [13]: usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-61666e3f
│                │                       │       .rsa.pub 
│                │                       ├ [14]: usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-616a9724
│                │                       │       .rsa.pub 
│                │                       ├ [15]: usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-616abc23
│                │                       │       .rsa.pub 
│                │                       ├ [16]: usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-616ac3bc
│                │                       │       .rsa.pub 
│                │                       ├ [17]: usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-616adfeb
│                │                       │       .rsa.pub 
│                │                       ├ [18]: usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-616ae350
│                │                       │       .rsa.pub 
│                │                       ├ [19]: usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-616db30d
│                │                       │       .rsa.pub 
│                │                       ├ [20]: usr/share/apk/keys/alpine-devel@lists.alpinelinux.org-66ba20fe
│                │                       │       .rsa.pub 
│                │                       ├ [21]: usr/share/apk/keys/aarch64/alpine-devel@lists.alpinelinux.org-
│                │                       │       58199dcc.rsa.pub 
│                │                       ├ [22]: usr/share/apk/keys/aarch64/alpine-devel@lists.alpinelinux.org-
│                │                       │       616ae350.rsa.pub 
│                │                       ├ [23]: usr/share/apk/keys/armhf/alpine-devel@lists.alpinelinux.org-52
│                │                       │       4d27bb.rsa.pub 
│                │                       ├ [24]: usr/share/apk/keys/armhf/alpine-devel@lists.alpinelinux.org-61
│                │                       │       6a9724.rsa.pub 
│                │                       ├ [25]: usr/share/apk/keys/armv7/alpine-devel@lists.alpinelinux.org-52
│                │                       │       4d27bb.rsa.pub 
│                │                       ├ [26]: usr/share/apk/keys/armv7/alpine-devel@lists.alpinelinux.org-61
│                │                       │       6adfeb.rsa.pub 
│                │                       ├ [27]: usr/share/apk/keys/loongarch64/alpine-devel@lists.alpinelinux.
│                │                       │       org-66ba20fe.rsa.pub 
│                │                       ├ [28]: usr/share/apk/keys/mips64/alpine-devel@lists.alpinelinux.org-5
│                │                       │       e69ca50.rsa.pub 
│                │                       ├ [29]: usr/share/apk/keys/ppc64le/alpine-devel@lists.alpinelinux.org-
│                │                       │       58cbb476.rsa.pub 
│                │                       ├ [30]: usr/share/apk/keys/ppc64le/alpine-devel@lists.alpinelinux.org-
│                │                       │       616abc23.rsa.pub 
│                │                       ├ [31]: usr/share/apk/keys/riscv64/alpine-devel@lists.alpinelinux.org-
│                │                       │       60ac2099.rsa.pub 
│                │                       ├ [32]: usr/share/apk/keys/riscv64/alpine-devel@lists.alpinelinux.org-
│                │                       │       616db30d.rsa.pub 
│                │                       ├ [33]: usr/share/apk/keys/s390x/alpine-devel@lists.alpinelinux.org-58
│                │                       │       e4f17d.rsa.pub 
│                │                       ├ [34]: usr/share/apk/keys/s390x/alpine-devel@lists.alpinelinux.org-61
│                │                       │       6ac3bc.rsa.pub 
│                │                       ├ [35]: usr/share/apk/keys/x86/alpine-devel@lists.alpinelinux.org-4a6a
│                │                       │       0840.rsa.pub 
│                │                       ├ [36]: usr/share/apk/keys/x86/alpine-devel@lists.alpinelinux.org-5243
│                │                       │       ef4b.rsa.pub 
│                │                       ├ [37]: usr/share/apk/keys/x86/alpine-devel@lists.alpinelinux.org-6166
│                │                       │       6e3f.rsa.pub 
│                │                       ├ [38]: usr/share/apk/keys/x86_64/alpine-devel@lists.alpinelinux.org-4
│                │                       │       a6a0840.rsa.pub 
│                │                       ├ [39]: usr/share/apk/keys/x86_64/alpine-devel@lists.alpinelinux.org-5
│                │                       │       261cecb.rsa.pub 
│                │                       ╰ [40]: usr/share/apk/keys/x86_64/alpine-devel@lists.alpinelinux.org-6
│                │                               165ee59.rsa.pub 
│                ├ [3]  ╭ ID            : alpine-release@3.23.2-r0 
│                │      ├ Name          : alpine-release 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/alpine-release@3.23.2-r0?arch=x86_64&distro=3.2
│                │      │                │       3.2 
│                │      │                ╰ UID : 57c1aff3fc070b0b 
│                │      ├ Version       : 3.23.2-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : alpine-base 
│                │      ├ SrcVersion    : 3.23.2-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: alpine-keys@2.6-r0 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:91714ffd6e07934d455777f7d6e3fe87878f7778 
│                │      ╰ InstalledFiles ╭ [0]: etc/alpine-release 
│                │                       ├ [1]: etc/issue 
│                │                       ├ [2]: etc/os-release 
│                │                       ├ [3]: etc/secfixes.d/alpine 
│                │                       ╰ [4]: usr/lib/os-release 
│                ├ [4]  ╭ ID            : alsa-lib@1.2.14-r2 
│                │      ├ Name          : alsa-lib 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/alsa-lib@1.2.14-r2?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 32eab98abe9de9d5 
│                │      ├ Version       : 1.2.14-r2 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : alsa-lib 
│                │      ├ SrcVersion    : 1.2.14-r2 
│                │      ├ Licenses       ─ [0]: LGPL-2.1-or-later 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:dfb787005e07d66c2db231863d54ab01c2cfb350 
│                │      ╰ InstalledFiles ╭ [0] : usr/bin/aserver 
│                │                       ├ [1] : usr/lib/libasound.so.2 
│                │                       ├ [2] : usr/lib/libasound.so.2.0.0 
│                │                       ├ [3] : usr/lib/libatopology.so.2 
│                │                       ├ [4] : usr/lib/libatopology.so.2.0.0 
│                │                       ├ [5] : usr/share/alsa/alsa.conf 
│                │                       ├ [6] : usr/share/alsa/cards/AACI.conf 
│                │                       ├ [7] : usr/share/alsa/cards/ATIIXP-MODEM.conf 
│                │                       ├ [8] : usr/share/alsa/cards/ATIIXP-SPDMA.conf 
│                │                       ├ [9] : usr/share/alsa/cards/ATIIXP.conf 
│                │                       ├ [10]: usr/share/alsa/cards/AU8810.conf 
│                │                       ├ [11]: usr/share/alsa/cards/AU8820.conf 
│                │                       ├ [12]: usr/share/alsa/cards/AU8830.conf 
│                │                       ├ [13]: usr/share/alsa/cards/Audigy.conf 
│                │                       ├ [14]: usr/share/alsa/cards/Audigy2.conf 
│                │                       ├ [15]: usr/share/alsa/cards/Aureon51.conf 
│                │                       ├ [16]: usr/share/alsa/cards/Aureon71.conf 
│                │                       ├ [17]: usr/share/alsa/cards/CA0106.conf 
│                │                       ├ [18]: usr/share/alsa/cards/CMI8338-SWIEC.conf 
│                │                       ├ [19]: usr/share/alsa/cards/CMI8338.conf 
│                │                       ├ [20]: usr/share/alsa/cards/CMI8738-MC6.conf 
│                │                       ├ [21]: usr/share/alsa/cards/CMI8738-MC8.conf 
│                │                       ├ [22]: usr/share/alsa/cards/CMI8788.conf 
│                │                       ├ [23]: usr/share/alsa/cards/CS46xx.conf 
│                │                       ├ [24]: usr/share/alsa/cards/EMU10K1.conf 
│                │                       ├ [25]: usr/share/alsa/cards/EMU10K1X.conf 
│                │                       ├ [26]: usr/share/alsa/cards/ENS1370.conf 
│                │                       ├ [27]: usr/share/alsa/cards/ENS1371.conf 
│                │                       ├ [28]: usr/share/alsa/cards/ES1968.conf 
│                │                       ├ [29]: usr/share/alsa/cards/Echo_Echo3G.conf 
│                │                       ├ [30]: usr/share/alsa/cards/FM801.conf 
│                │                       ├ [31]: usr/share/alsa/cards/FWSpeakers.conf 
│                │                       ├ [32]: usr/share/alsa/cards/FireWave.conf 
│                │                       ├ [33]: usr/share/alsa/cards/GUS.conf 
│                │                       ├ [34]: usr/share/alsa/cards/HDA-Intel.conf 
│                │                       ├ [35]: usr/share/alsa/cards/HdmiLpeAudio.conf 
│                │                       ├ [36]: usr/share/alsa/cards/ICE1712.conf 
│                │                       ├ [37]: usr/share/alsa/cards/ICE1724.conf 
│                │                       ├ [38]: usr/share/alsa/cards/ICH-MODEM.conf 
│                │                       ├ [39]: usr/share/alsa/cards/ICH.conf 
│                │                       ├ [40]: usr/share/alsa/cards/ICH4.conf 
│                │                       ├ [41]: usr/share/alsa/cards/Loopback.conf 
│                │                       ├ [42]: usr/share/alsa/cards/Maestro3.conf 
│                │                       ├ [43]: usr/share/alsa/cards/NFORCE.conf 
│                │                       ├ [44]: usr/share/alsa/cards/PC-Speaker.conf 
│                │                       ├ [45]: usr/share/alsa/cards/PMac.conf 
│                │                       ├ [46]: usr/share/alsa/cards/PMacToonie.conf 
│                │                       ├ [47]: usr/share/alsa/cards/PS3.conf 
│                │                       ├ [48]: usr/share/alsa/cards/RME9636.conf 
│                │                       ├ [49]: usr/share/alsa/cards/RME9652.conf 
│                │                       ├ [50]: usr/share/alsa/cards/SB-XFi.conf 
│                │                       ├ [51]: usr/share/alsa/cards/SI7018.conf 
│                │                       ├ [52]: usr/share/alsa/cards/TRID4DWAVENX.conf 
│                │                       ├ [53]: usr/share/alsa/cards/USB-Audio.conf 
│                │                       ├ [54]: usr/share/alsa/cards/VIA686A.conf 
│                │                       ├ [55]: usr/share/alsa/cards/VIA8233.conf 
│                │                       ├ [56]: usr/share/alsa/cards/VIA8233A.conf 
│                │                       ├ [57]: usr/share/alsa/cards/VIA8237.conf 
│                │                       ├ [58]: usr/share/alsa/cards/VX222.conf 
│                │                       ├ [59]: usr/share/alsa/cards/VXPocket.conf 
│                │                       ├ [60]: usr/share/alsa/cards/VXPocket440.conf 
│                │                       ├ [61]: usr/share/alsa/cards/YMF744.conf 
│                │                       ├ [62]: usr/share/alsa/cards/aliases.conf 
│                │                       ├ [63]: usr/share/alsa/cards/pistachio-card.conf 
│                │                       ├ [64]: usr/share/alsa/cards/vc4-hdmi.conf 
│                │                       ├ [65]: usr/share/alsa/ctl/default.conf 
│                │                       ├ [66]: usr/share/alsa/pcm/center_lfe.conf 
│                │                       ├ [67]: usr/share/alsa/pcm/default.conf 
│                │                       ├ [68]: usr/share/alsa/pcm/dmix.conf 
│                │                       ├ [69]: usr/share/alsa/pcm/dpl.conf 
│                │                       ├ [70]: usr/share/alsa/pcm/dsnoop.conf 
│                │                       ├ [71]: usr/share/alsa/pcm/front.conf 
│                │                       ├ [72]: usr/share/alsa/pcm/hdmi.conf 
│                │                       ├ [73]: usr/share/alsa/pcm/iec958.conf 
│                │                       ├ [74]: usr/share/alsa/pcm/modem.conf 
│                │                       ├ [75]: usr/share/alsa/pcm/rear.conf 
│                │                       ├ [76]: usr/share/alsa/pcm/side.conf 
│                │                       ├ [77]: usr/share/alsa/pcm/surround21.conf 
│                │                       ├ [78]: usr/share/alsa/pcm/surround40.conf 
│                │                       ├ [79]: usr/share/alsa/pcm/surround41.conf 
│                │                       ├ [80]: usr/share/alsa/pcm/surround50.conf 
│                │                       ├ [81]: usr/share/alsa/pcm/surround51.conf 
│                │                       ╰ [82]: usr/share/alsa/pcm/surround71.conf 
│                ├ [5]  ╭ ID            : apk-tools@3.0.3-r1 
│                │      ├ Name          : apk-tools 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/apk-tools@3.0.3-r1?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : ba6de1c379629b84 
│                │      ├ Version       : 3.0.3-r1 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : apk-tools 
│                │      ├ SrcVersion    : 3.0.3-r1 
│                │      ├ Licenses       ─ [0]: GPL-2.0-only 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: ca-certificates-bundle@20251003-r0 
│                │      │                ├ [1]: libapk@3.0.3-r1 
│                │      │                ├ [2]: libcrypto3@3.5.4-r0 
│                │      │                ├ [3]: musl@1.2.5-r21 
│                │      │                ╰ [4]: zlib@1.3.1-r2 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:b2f877e6c9fb945c185cf36ed546064b8b374245 
│                │      ╰ InstalledFiles ─ [0]: sbin/apk 
│                ├ [6]  ╭ ID            : brotli-libs@1.2.0-r0 
│                │      ├ Name          : brotli-libs 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/brotli-libs@1.2.0-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : b299b9e27780dd4f 
│                │      ├ Version       : 1.2.0-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : brotli 
│                │      ├ SrcVersion    : 1.2.0-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : prspkt <prspkt@protonmail.com> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:0814694602f35d2741e916fdcb4c9a1e0ec50b42 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libbrotlicommon.so.1 
│                │                       ├ [1]: usr/lib/libbrotlicommon.so.1.2.0 
│                │                       ├ [2]: usr/lib/libbrotlidec.so.1 
│                │                       ├ [3]: usr/lib/libbrotlidec.so.1.2.0 
│                │                       ├ [4]: usr/lib/libbrotlienc.so.1 
│                │                       ╰ [5]: usr/lib/libbrotlienc.so.1.2.0 
│                ├ [7]  ╭ ID            : busybox@1.37.0-r30 
│                │      ├ Name          : busybox 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/busybox@1.37.0-r30?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : f28a1cfcf00f0dab 
│                │      ├ Version       : 1.37.0-r30 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : busybox 
│                │      ├ SrcVersion    : 1.37.0-r30 
│                │      ├ Licenses       ─ [0]: GPL-2.0-only 
│                │      ├ Maintainer    : Sören Tempel <soeren+alpine@soeren-tempel.net> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:f1347801bb96b1aa40d17f82237c3f4ff02a4725 
│                │      ╰ InstalledFiles ╭ [0]: bin/busybox 
│                │                       ├ [1]: etc/securetty 
│                │                       ├ [2]: etc/busybox-paths.d/busybox 
│                │                       ├ [3]: etc/logrotate.d/acpid 
│                │                       ├ [4]: etc/network/if-up.d/dad 
│                │                       ├ [5]: etc/udhcpc/udhcpc.conf 
│                │                       ╰ [6]: usr/share/udhcpc/default.script 
│                ├ [8]  ╭ ID            : busybox-binsh@1.37.0-r30 
│                │      ├ Name          : busybox-binsh 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/busybox-binsh@1.37.0-r30?arch=x86_64&distro=3.2
│                │      │                │       3.2 
│                │      │                ╰ UID : f655486c35e2f7d2 
│                │      ├ Version       : 1.37.0-r30 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : busybox 
│                │      ├ SrcVersion    : 1.37.0-r30 
│                │      ├ Licenses       ─ [0]: GPL-2.0-only 
│                │      ├ Maintainer    : Sören Tempel <soeren+alpine@soeren-tempel.net> 
│                │      ├ DependsOn      ─ [0]: busybox@1.37.0-r30 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:188d2d0110afa58e8a3e3e5fd424b2d996df7a09 
│                │      ╰ InstalledFiles ─ [0]: bin/sh 
│                ├ [9]  ╭ ID            : c-ares@1.34.6-r0 
│                │      ├ Name          : c-ares 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/c-ares@1.34.6-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 7c7a6bf6ae3bc6e8 
│                │      ├ Version       : 1.34.6-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : c-ares 
│                │      ├ SrcVersion    : 1.34.6-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Carlo Landmeter <clandmeter@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:e3bb3ff47a277ff9409b8c4bb825099cfe2bcbe2 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libcares.so.2 
│                │                       ╰ [1]: usr/lib/libcares.so.2.19.5 
│                ├ [10] ╭ ID            : ca-certificates@20251003-r0 
│                │      ├ Name          : ca-certificates 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/ca-certificates@20251003-r0?arch=x86_64&distro=
│                │      │                │       3.23.2 
│                │      │                ╰ UID : 5410ad956d60f968 
│                │      ├ Version       : 20251003-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : ca-certificates 
│                │      ├ SrcVersion    : 20251003-r0 
│                │      ├ Licenses       ╭ [0]: MPL-2.0 
│                │      │                ╰ [1]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: busybox-binsh@1.37.0-r30 
│                │      │                ├ [1]: libcrypto3@3.5.4-r0 
│                │      │                ╰ [2]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:3b10fd335b2af819c4fd3562900e76fd6ea304c5 
│                │      ╰ InstalledFiles ╭ [0]  : etc/ca-certificates.conf 
│                │                       ├ [1]  : etc/apk/protected_paths.d/ca-certificates.list 
│                │                       ├ [2]  : etc/ca-certificates/update.d/certhash 
│                │                       ├ [3]  : usr/bin/c_rehash 
│                │                       ├ [4]  : usr/sbin/update-ca-certificates 
│                │                       ├ [5]  : usr/share/ca-certificates/mozilla/ACCVRAIZ1.crt 
│                │                       ├ [6]  : usr/share/ca-certificates/mozilla/AC_RAIZ_FNMT-RCM.crt 
│                │                       ├ [7]  : usr/share/ca-certificates/mozilla/AC_RAIZ_FNMT-RCM_SERVIDORES
│                │                       │        _SEGUROS.crt 
│                │                       ├ [8]  : usr/share/ca-certificates/mozilla/ANF_Secure_Server_Root_CA.crt 
│                │                       ├ [9]  : usr/share/ca-certificates/mozilla/Actalis_Authentication_Root
│                │                       │        _CA.crt 
│                │                       ├ [10] : usr/share/ca-certificates/mozilla/AffirmTrust_Commercial.crt 
│                │                       ├ [11] : usr/share/ca-certificates/mozilla/AffirmTrust_Networking.crt 
│                │                       ├ [12] : usr/share/ca-certificates/mozilla/AffirmTrust_Premium.crt 
│                │                       ├ [13] : usr/share/ca-certificates/mozilla/AffirmTrust_Premium_ECC.crt 
│                │                       ├ [14] : usr/share/ca-certificates/mozilla/Amazon_Root_CA_1.crt 
│                │                       ├ [15] : usr/share/ca-certificates/mozilla/Amazon_Root_CA_2.crt 
│                │                       ├ [16] : usr/share/ca-certificates/mozilla/Amazon_Root_CA_3.crt 
│                │                       ├ [17] : usr/share/ca-certificates/mozilla/Amazon_Root_CA_4.crt 
│                │                       ├ [18] : usr/share/ca-certificates/mozilla/Atos_TrustedRoot_2011.crt 
│                │                       ├ [19] : usr/share/ca-certificates/mozilla/Atos_TrustedRoot_Root_CA_EC
│                │                       │        C_TLS_2021.crt 
│                │                       ├ [20] : usr/share/ca-certificates/mozilla/Atos_TrustedRoot_Root_CA_RS
│                │                       │        A_TLS_2021.crt 
│                │                       ├ [21] : usr/share/ca-certificates/mozilla/Autoridad_de_Certificacion_
│                │                       │        Firmaprofesional_CIF_A62634068.crt 
│                │                       ├ [22] : usr/share/ca-certificates/mozilla/BJCA_Global_Root_CA1.crt 
│                │                       ├ [23] : usr/share/ca-certificates/mozilla/BJCA_Global_Root_CA2.crt 
│                │                       ├ [24] : usr/share/ca-certificates/mozilla/Buypass_Class_2_Root_CA.crt 
│                │                       ├ [25] : usr/share/ca-certificates/mozilla/Buypass_Class_3_Root_CA.crt 
│                │                       ├ [26] : usr/share/ca-certificates/mozilla/CA_Disig_Root_R2.crt 
│                │                       ├ [27] : usr/share/ca-certificates/mozilla/CFCA_EV_ROOT.crt 
│                │                       ├ [28] : usr/share/ca-certificates/mozilla/COMODO_Certification_Author
│                │                       │        ity.crt 
│                │                       ├ [29] : usr/share/ca-certificates/mozilla/COMODO_ECC_Certification_Au
│                │                       │        thority.crt 
│                │                       ├ [30] : usr/share/ca-certificates/mozilla/COMODO_RSA_Certification_Au
│                │                       │        thority.crt 
│                │                       ├ [31] : usr/share/ca-certificates/mozilla/Certainly_Root_E1.crt 
│                │                       ├ [32] : usr/share/ca-certificates/mozilla/Certainly_Root_R1.crt 
│                │                       ├ [33] : usr/share/ca-certificates/mozilla/Certigna.crt 
│                │                       ├ [34] : usr/share/ca-certificates/mozilla/Certigna_Root_CA.crt 
│                │                       ├ [35] : usr/share/ca-certificates/mozilla/Certum_EC-384_CA.crt 
│                │                       ├ [36] : usr/share/ca-certificates/mozilla/Certum_Trusted_Network_CA.crt 
│                │                       ├ [37] : usr/share/ca-certificates/mozilla/Certum_Trusted_Network_CA_2
│                │                       │        .crt 
│                │                       ├ [38] : usr/share/ca-certificates/mozilla/Certum_Trusted_Root_CA.crt 
│                │                       ├ [39] : usr/share/ca-certificates/mozilla/CommScope_Public_Trust_ECC_
│                │                       │        Root-01.crt 
│                │                       ├ [40] : usr/share/ca-certificates/mozilla/CommScope_Public_Trust_ECC_
│                │                       │        Root-02.crt 
│                │                       ├ [41] : usr/share/ca-certificates/mozilla/CommScope_Public_Trust_RSA_
│                │                       │        Root-01.crt 
│                │                       ├ [42] : usr/share/ca-certificates/mozilla/CommScope_Public_Trust_RSA_
│                │                       │        Root-02.crt 
│                │                       ├ [43] : usr/share/ca-certificates/mozilla/D-TRUST_BR_Root_CA_1_2020.crt 
│                │                       ├ [44] : usr/share/ca-certificates/mozilla/D-TRUST_BR_Root_CA_2_2023.crt 
│                │                       ├ [45] : usr/share/ca-certificates/mozilla/D-TRUST_EV_Root_CA_1_2020.crt 
│                │                       ├ [46] : usr/share/ca-certificates/mozilla/D-TRUST_EV_Root_CA_2_2023.crt 
│                │                       ├ [47] : usr/share/ca-certificates/mozilla/D-TRUST_Root_Class_3_CA_2_2
│                │                       │        009.crt 
│                │                       ├ [48] : usr/share/ca-certificates/mozilla/D-TRUST_Root_Class_3_CA_2_E
│                │                       │        V_2009.crt 
│                │                       ├ [49] : usr/share/ca-certificates/mozilla/DigiCert_Assured_ID_Root_CA
│                │                       │        .crt 
│                │                       ├ [50] : usr/share/ca-certificates/mozilla/DigiCert_Assured_ID_Root_G2
│                │                       │        .crt 
│                │                       ├ [51] : usr/share/ca-certificates/mozilla/DigiCert_Assured_ID_Root_G3
│                │                       │        .crt 
│                │                       ├ [52] : usr/share/ca-certificates/mozilla/DigiCert_Global_Root_CA.crt 
│                │                       ├ [53] : usr/share/ca-certificates/mozilla/DigiCert_Global_Root_G2.crt 
│                │                       ├ [54] : usr/share/ca-certificates/mozilla/DigiCert_Global_Root_G3.crt 
│                │                       ├ [55] : usr/share/ca-certificates/mozilla/DigiCert_High_Assurance_EV_
│                │                       │        Root_CA.crt 
│                │                       ├ [56] : usr/share/ca-certificates/mozilla/DigiCert_TLS_ECC_P384_Root_
│                │                       │        G5.crt 
│                │                       ├ [57] : usr/share/ca-certificates/mozilla/DigiCert_TLS_RSA4096_Root_G
│                │                       │        5.crt 
│                │                       ├ [58] : usr/share/ca-certificates/mozilla/DigiCert_Trusted_Root_G4.crt 
│                │                       ├ [59] : usr/share/ca-certificates/mozilla/Entrust_Root_Certification_
│                │                       │        Authority.crt 
│                │                       ├ [60] : usr/share/ca-certificates/mozilla/Entrust_Root_Certification_
│                │                       │        Authority_-_EC1.crt 
│                │                       ├ [61] : usr/share/ca-certificates/mozilla/Entrust_Root_Certification_
│                │                       │        Authority_-_G2.crt 
│                │                       ├ [62] : usr/share/ca-certificates/mozilla/FIRMAPROFESIONAL_CA_ROOT-A_
│                │                       │        WEB.crt 
│                │                       ├ [63] : usr/share/ca-certificates/mozilla/GDCA_TrustAUTH_R5_ROOT.crt 
│                │                       ├ [64] : usr/share/ca-certificates/mozilla/GLOBALTRUST_2020.crt 
│                │                       ├ [65] : usr/share/ca-certificates/mozilla/GTS_Root_R1.crt 
│                │                       ├ [66] : usr/share/ca-certificates/mozilla/GTS_Root_R2.crt 
│                │                       ├ [67] : usr/share/ca-certificates/mozilla/GTS_Root_R3.crt 
│                │                       ├ [68] : usr/share/ca-certificates/mozilla/GTS_Root_R4.crt 
│                │                       ├ [69] : usr/share/ca-certificates/mozilla/GlobalSign_ECC_Root_CA_-_R4
│                │                       │        .crt 
│                │                       ├ [70] : usr/share/ca-certificates/mozilla/GlobalSign_ECC_Root_CA_-_R5
│                │                       │        .crt 
│                │                       ├ [71] : usr/share/ca-certificates/mozilla/GlobalSign_Root_CA_-_R3.crt 
│                │                       ├ [72] : usr/share/ca-certificates/mozilla/GlobalSign_Root_CA_-_R6.crt 
│                │                       ├ [73] : usr/share/ca-certificates/mozilla/GlobalSign_Root_E46.crt 
│                │                       ├ [74] : usr/share/ca-certificates/mozilla/GlobalSign_Root_R46.crt 
│                │                       ├ [75] : usr/share/ca-certificates/mozilla/Go_Daddy_Root_Certificate_A
│                │                       │        uthority_-_G2.crt 
│                │                       ├ [76] : usr/share/ca-certificates/mozilla/HARICA_TLS_ECC_Root_CA_2021
│                │                       │        .crt 
│                │                       ├ [77] : usr/share/ca-certificates/mozilla/HARICA_TLS_RSA_Root_CA_2021
│                │                       │        .crt 
│                │                       ├ [78] : usr/share/ca-certificates/mozilla/Hellenic_Academic_and_Resea
│                │                       │        rch_Institutions_ECC_RootCA_2015.crt 
│                │                       ├ [79] : usr/share/ca-certificates/mozilla/Hellenic_Academic_and_Resea
│                │                       │        rch_Institutions_RootCA_2015.crt 
│                │                       ├ [80] : usr/share/ca-certificates/mozilla/HiPKI_Root_CA_-_G1.crt 
│                │                       ├ [81] : usr/share/ca-certificates/mozilla/Hongkong_Post_Root_CA_3.crt 
│                │                       ├ [82] : usr/share/ca-certificates/mozilla/ISRG_Root_X1.crt 
│                │                       ├ [83] : usr/share/ca-certificates/mozilla/ISRG_Root_X2.crt 
│                │                       ├ [84] : usr/share/ca-certificates/mozilla/IdenTrust_Commercial_Root_C
│                │                       │        A_1.crt 
│                │                       ├ [85] : usr/share/ca-certificates/mozilla/IdenTrust_Public_Sector_Roo
│                │                       │        t_CA_1.crt 
│                │                       ├ [86] : usr/share/ca-certificates/mozilla/Izenpe.com.crt 
│                │                       ├ [87] : usr/share/ca-certificates/mozilla/Microsec_e-Szigno_Root_CA_2
│                │                       │        009.crt 
│                │                       ├ [88] : usr/share/ca-certificates/mozilla/Microsoft_ECC_Root_Certific
│                │                       │        ate_Authority_2017.crt 
│                │                       ├ [89] : usr/share/ca-certificates/mozilla/Microsoft_RSA_Root_Certific
│                │                       │        ate_Authority_2017.crt 
│                │                       ├ [90] : usr/share/ca-certificates/mozilla/NAVER_Global_Root_Certifica
│                │                       │        tion_Authority.crt 
│                │                       ├ [91] : usr/share/ca-certificates/mozilla/NetLock_Arany_=Class_Gold=_
│                │                       │        Főtanúsítvány.crt 
│                │                       ├ [92] : usr/share/ca-certificates/mozilla/OISTE_Server_Root_ECC_G1.crt 
│                │                       ├ [93] : usr/share/ca-certificates/mozilla/OISTE_Server_Root_RSA_G1.crt 
│                │                       ├ [94] : usr/share/ca-certificates/mozilla/OISTE_WISeKey_Global_Root_G
│                │                       │        B_CA.crt 
│                │                       ├ [95] : usr/share/ca-certificates/mozilla/OISTE_WISeKey_Global_Root_G
│                │                       │        C_CA.crt 
│                │                       ├ [96] : usr/share/ca-certificates/mozilla/QuoVadis_Root_CA_1_G3.crt 
│                │                       ├ [97] : usr/share/ca-certificates/mozilla/QuoVadis_Root_CA_2.crt 
│                │                       ├ [98] : usr/share/ca-certificates/mozilla/QuoVadis_Root_CA_2_G3.crt 
│                │                       ├ [99] : usr/share/ca-certificates/mozilla/QuoVadis_Root_CA_3.crt 
│                │                       ├ [100]: usr/share/ca-certificates/mozilla/QuoVadis_Root_CA_3_G3.crt 
│                │                       ├ [101]: usr/share/ca-certificates/mozilla/SSL.com_EV_Root_Certificati
│                │                       │        on_Authority_ECC.crt 
│                │                       ├ [102]: usr/share/ca-certificates/mozilla/SSL.com_EV_Root_Certificati
│                │                       │        on_Authority_RSA_R2.crt 
│                │                       ├ [103]: usr/share/ca-certificates/mozilla/SSL.com_Root_Certification_
│                │                       │        Authority_ECC.crt 
│                │                       ├ [104]: usr/share/ca-certificates/mozilla/SSL.com_Root_Certification_
│                │                       │        Authority_RSA.crt 
│                │                       ├ [105]: usr/share/ca-certificates/mozilla/SSL.com_TLS_ECC_Root_CA_202
│                │                       │        2.crt 
│                │                       ├ [106]: usr/share/ca-certificates/mozilla/SSL.com_TLS_RSA_Root_CA_202
│                │                       │        2.crt 
│                │                       ├ [107]: usr/share/ca-certificates/mozilla/SZAFIR_ROOT_CA2.crt 
│                │                       ├ [108]: usr/share/ca-certificates/mozilla/Sectigo_Public_Server_Authe
│                │                       │        ntication_Root_E46.crt 
│                │                       ├ [109]: usr/share/ca-certificates/mozilla/Sectigo_Public_Server_Authe
│                │                       │        ntication_Root_R46.crt 
│                │                       ├ [110]: usr/share/ca-certificates/mozilla/SecureSign_Root_CA12.crt 
│                │                       ├ [111]: usr/share/ca-certificates/mozilla/SecureSign_Root_CA14.crt 
│                │                       ├ [112]: usr/share/ca-certificates/mozilla/SecureSign_Root_CA15.crt 
│                │                       ├ [113]: usr/share/ca-certificates/mozilla/SecureTrust_CA.crt 
│                │                       ├ [114]: usr/share/ca-certificates/mozilla/Secure_Global_CA.crt 
│                │                       ├ [115]: usr/share/ca-certificates/mozilla/Security_Communication_ECC_
│                │                       │        RootCA1.crt 
│                │                       ├ [116]: usr/share/ca-certificates/mozilla/Security_Communication_Root
│                │                       │        CA2.crt 
│                │                       ├ [117]: usr/share/ca-certificates/mozilla/Starfield_Root_Certificate_
│                │                       │        Authority_-_G2.crt 
│                │                       ├ [118]: usr/share/ca-certificates/mozilla/Starfield_Services_Root_Cer
│                │                       │        tificate_Authority_-_G2.crt 
│                │                       ├ [119]: usr/share/ca-certificates/mozilla/SwissSign_Gold_CA_-_G2.crt 
│                │                       ├ [120]: usr/share/ca-certificates/mozilla/SwissSign_RSA_TLS_Root_CA_2
│                │                       │        022_-_1.crt 
│                │                       ├ [121]: usr/share/ca-certificates/mozilla/T-TeleSec_GlobalRoot_Class_
│                │                       │        2.crt 
│                │                       ├ [122]: usr/share/ca-certificates/mozilla/T-TeleSec_GlobalRoot_Class_
│                │                       │        3.crt 
│                │                       ├ [123]: usr/share/ca-certificates/mozilla/TUBITAK_Kamu_SM_SSL_Kok_Ser
│                │                       │        tifikasi_-_Surum_1.crt 
│                │                       ├ [124]: usr/share/ca-certificates/mozilla/TWCA_CYBER_Root_CA.crt 
│                │                       ├ [125]: usr/share/ca-certificates/mozilla/TWCA_Global_Root_CA.crt 
│                │                       ├ [126]: usr/share/ca-certificates/mozilla/TWCA_Root_Certification_Aut
│                │                       │        hority.crt 
│                │                       ├ [127]: usr/share/ca-certificates/mozilla/Telekom_Security_TLS_ECC_Ro
│                │                       │        ot_2020.crt 
│                │                       ├ [128]: usr/share/ca-certificates/mozilla/Telekom_Security_TLS_RSA_Ro
│                │                       │        ot_2023.crt 
│                │                       ├ [129]: usr/share/ca-certificates/mozilla/TeliaSonera_Root_CA_v1.crt 
│                │                       ├ [130]: usr/share/ca-certificates/mozilla/Telia_Root_CA_v2.crt 
│                │                       ├ [131]: usr/share/ca-certificates/mozilla/TrustAsia_Global_Root_CA_G3
│                │                       │        .crt 
│                │                       ├ [132]: usr/share/ca-certificates/mozilla/TrustAsia_Global_Root_CA_G4
│                │                       │        .crt 
│                │                       ├ [133]: usr/share/ca-certificates/mozilla/TrustAsia_TLS_ECC_Root_CA.crt 
│                │                       ├ [134]: usr/share/ca-certificates/mozilla/TrustAsia_TLS_RSA_Root_CA.crt 
│                │                       ├ [135]: usr/share/ca-certificates/mozilla/Trustwave_Global_Certificat
│                │                       │        ion_Authority.crt 
│                │                       ├ [136]: usr/share/ca-certificates/mozilla/Trustwave_Global_ECC_P256_C
│                │                       │        ertification_Authority.crt 
│                │                       ├ [137]: usr/share/ca-certificates/mozilla/Trustwave_Global_ECC_P384_C
│                │                       │        ertification_Authority.crt 
│                │                       ├ [138]: usr/share/ca-certificates/mozilla/TunTrust_Root_CA.crt 
│                │                       ├ [139]: usr/share/ca-certificates/mozilla/UCA_Extended_Validation_Roo
│                │                       │        t.crt 
│                │                       ├ [140]: usr/share/ca-certificates/mozilla/UCA_Global_G2_Root.crt 
│                │                       ├ [141]: usr/share/ca-certificates/mozilla/USERTrust_ECC_Certification
│                │                       │        _Authority.crt 
│                │                       ├ [142]: usr/share/ca-certificates/mozilla/USERTrust_RSA_Certification
│                │                       │        _Authority.crt 
│                │                       ├ [143]: usr/share/ca-certificates/mozilla/certSIGN_ROOT_CA.crt 
│                │                       ├ [144]: usr/share/ca-certificates/mozilla/certSIGN_Root_CA_G2.crt 
│                │                       ├ [145]: usr/share/ca-certificates/mozilla/e-Szigno_Root_CA_2017.crt 
│                │                       ├ [146]: usr/share/ca-certificates/mozilla/ePKI_Root_Certification_Aut
│                │                       │        hority.crt 
│                │                       ├ [147]: usr/share/ca-certificates/mozilla/emSign_ECC_Root_CA_-_C3.crt 
│                │                       ├ [148]: usr/share/ca-certificates/mozilla/emSign_ECC_Root_CA_-_G3.crt 
│                │                       ├ [149]: usr/share/ca-certificates/mozilla/emSign_Root_CA_-_C1.crt 
│                │                       ├ [150]: usr/share/ca-certificates/mozilla/emSign_Root_CA_-_G1.crt 
│                │                       ├ [151]: usr/share/ca-certificates/mozilla/vTrus_ECC_Root_CA.crt 
│                │                       ╰ [152]: usr/share/ca-certificates/mozilla/vTrus_Root_CA.crt 
│                ├ [11] ╭ ID            : ca-certificates-bundle@20251003-r0 
│                │      ├ Name          : ca-certificates-bundle 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/ca-certificates-bundle@20251003-r0?arch=x86_64&
│                │      │                │       distro=3.23.2 
│                │      │                ╰ UID : 601aed1e41b824a1 
│                │      ├ Version       : 20251003-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : ca-certificates 
│                │      ├ SrcVersion    : 20251003-r0 
│                │      ├ Licenses       ╭ [0]: MPL-2.0 
│                │      │                ╰ [1]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:63ebe72ba79f548b6cdc8a9894e16a90d80f42b0 
│                │      ╰ InstalledFiles ╭ [0]: etc/ssl/cert.pem 
│                │                       ├ [1]: etc/ssl/certs/ca-certificates.crt 
│                │                       ├ [2]: etc/ssl1.1/cert.pem 
│                │                       ╰ [3]: etc/ssl1.1/certs 
│                ├ [12] ╭ ID            : curl@8.17.0-r1 
│                │      ├ Name          : curl 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/curl@8.17.0-r1?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 88ffdbbc87036140 
│                │      ├ Version       : 8.17.0-r1 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : curl 
│                │      ├ SrcVersion    : 8.17.0-r1 
│                │      ├ Licenses       ─ [0]: curl 
│                │      ├ Maintainer    : Achill Gilgenast <achill@achill.org> 
│                │      ├ DependsOn      ╭ [0]: libcurl@8.17.0-r1 
│                │      │                ├ [1]: musl@1.2.5-r21 
│                │      │                ╰ [2]: zlib@1.3.1-r2 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:c467d4938a8ffc55afe3b1a6223787e0ecd60036 
│                │      ╰ InstalledFiles ╭ [0]: usr/bin/curl 
│                │                       ╰ [1]: usr/bin/wcurl 
│                ├ [13] ╭ ID            : freetype@2.14.1-r0 
│                │      ├ Name          : freetype 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/freetype@2.14.1-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : ec7aa3ca99070542 
│                │      ├ Version       : 2.14.1-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : freetype 
│                │      ├ SrcVersion    : 2.14.1-r0 
│                │      ├ Licenses       ╭ [0]: FTL 
│                │      │                ╰ [1]: GPL-2.0-or-later 
│                │      ├ Maintainer    : Carlo Landmeter <clandmeter@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: brotli-libs@1.2.0-r0 
│                │      │                ├ [1]: libbz2@1.0.8-r6 
│                │      │                ├ [2]: libpng@1.6.53-r0 
│                │      │                ├ [3]: musl@1.2.5-r21 
│                │      │                ╰ [4]: zlib@1.3.1-r2 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:e227f29a00edd7ed5b1e62a050da6532183e60be 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libfreetype.so.6 
│                │                       ╰ [1]: usr/lib/libfreetype.so.6.20.4 
│                ├ [14] ╭ ID            : gdbm@1.26-r0 
│                │      ├ Name          : gdbm 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/gdbm@1.26-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 2b2e855bec41243b 
│                │      ├ Version       : 1.26-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : gdbm 
│                │      ├ SrcVersion    : 1.26-r0 
│                │      ├ Licenses       ─ [0]: GPL-3.0-or-later 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:015081387c654fbfd7d9e000cb35ee31b3158567 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libgdbm.so.6 
│                │                       ├ [1]: usr/lib/libgdbm.so.6.0.0 
│                │                       ├ [2]: usr/lib/libgdbm_compat.so.4 
│                │                       ╰ [3]: usr/lib/libgdbm_compat.so.4.0.0 
│                ├ [15] ╭ ID            : giflib@5.2.2-r1 
│                │      ├ Name          : giflib 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/giflib@5.2.2-r1?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 59bf3ff686548507 
│                │      ├ Version       : 5.2.2-r1 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : giflib 
│                │      ├ SrcVersion    : 5.2.2-r1 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:18c5a46dd282cbd6aba1f8246985d992a160e9b5 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libgif.so.7 
│                │                       ╰ [1]: usr/lib/libgif.so.7.2.0 
│                ├ [16] ╭ ID            : java-cacerts@1.1-r0 
│                │      ├ Name          : java-cacerts 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/java-cacerts@1.1-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 50cf94070f158d78 
│                │      ├ Version       : 1.1-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : java-cacerts 
│                │      ├ SrcVersion    : 1.1-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: busybox-binsh@1.37.0-r30 
│                │      │                ├ [1]: ca-certificates@20251003-r0 
│                │      │                ├ [2]: p11-kit-trust@0.25.5-r2 
│                │      │                ╰ [3]: p11-kit@0.25.5-r2 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:dd6d704f5e91ed26d9c026eac28bcd716f49a753 
│                │      ╰ InstalledFiles ─ [0]: etc/ca-certificates/update.d/java-cacerts 
│                ├ [17] ╭ ID            : java-common@1.0-r1 
│                │      ├ Name          : java-common 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/java-common@1.0-r1?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 5ca066732893798e 
│                │      ├ Version       : 1.0-r1 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : java-common 
│                │      ├ SrcVersion    : 1.0-r1 
│                │      ├ Licenses       ─ [0]: GPL-2.0-or-later 
│                │      ├ Maintainer    : Timo Teras <timo.teras@iki.fi> 
│                │      ├ DependsOn      ─ [0]: busybox-binsh@1.37.0-r30 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:52205baa8687d26c879a55110a0a258d4dbfe8a6 
│                │      ╰ InstalledFiles ─ [0]: usr/bin/java 
│                ├ [18] ╭ ID            : lcms2@2.17-r0 
│                │      ├ Name          : lcms2 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/lcms2@2.17-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 7862ee3458766f09 
│                │      ├ Version       : 2.17-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : lcms2 
│                │      ├ SrcVersion    : 2.17-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:4b9df8b110088ab37a048d0be4bae4d06ce0747f 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/liblcms2.so.2 
│                │                       ╰ [1]: usr/lib/liblcms2.so.2.0.17 
│                ├ [19] ╭ ID            : libapk@3.0.3-r1 
│                │      ├ Name          : libapk 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libapk@3.0.3-r1?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : d2ec8433b3b9b1de 
│                │      ├ Version       : 3.0.3-r1 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : apk-tools 
│                │      ├ SrcVersion    : 3.0.3-r1 
│                │      ├ Licenses       ─ [0]: GPL-2.0-only 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libcrypto3@3.5.4-r0 
│                │      │                ├ [1]: libssl3@3.5.4-r0 
│                │      │                ├ [2]: musl@1.2.5-r21 
│                │      │                ╰ [3]: zlib@1.3.1-r2 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:17d0c18e379eb411aaa3e07392343a2dd6e098cc 
│                │      ╰ InstalledFiles ─ [0]: usr/lib/libapk.so.3.0.0 
│                ├ [20] ╭ ID            : libbsd@0.12.2-r0 
│                │      ├ Name          : libbsd 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libbsd@0.12.2-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 25f2a887b0a92f53 
│                │      ├ Version       : 0.12.2-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libbsd 
│                │      ├ SrcVersion    : 0.12.2-r0 
│                │      ├ Licenses       ─ [0]: BSD-3-Clause 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libmd@1.1.0-r0 
│                │      │                ╰ [1]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:33970b157edad359d05a2c3e6f3460e725549c8b 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libbsd.so.0 
│                │                       ╰ [1]: usr/lib/libbsd.so.0.12.2 
│                ├ [21] ╭ ID            : libbz2@1.0.8-r6 
│                │      ├ Name          : libbz2 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libbz2@1.0.8-r6?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : fb616a0731666455 
│                │      ├ Version       : 1.0.8-r6 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : bzip2 
│                │      ├ SrcVersion    : 1.0.8-r6 
│                │      ├ Licenses       ─ [0]: bzip-2-1.0.6 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:864d363da11ee24c7920e0d052d2da7f8429251e 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libbz2.so.1 
│                │                       ╰ [1]: usr/lib/libbz2.so.1.0.8 
│                ├ [22] ╭ ID            : libcrypto3@3.5.4-r0 
│                │      ├ Name          : libcrypto3 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.4-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 62215c30ccf85b6f 
│                │      ├ Version       : 3.5.4-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : openssl 
│                │      ├ SrcVersion    : 3.5.4-r0 
│                │      ├ Licenses       ─ [0]: Apache-2.0 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:adcd00253f51f9cd8f76189d94a5953da688365b 
│                │      ╰ InstalledFiles ╭ [0]: etc/ssl/ct_log_list.cnf 
│                │                       ├ [1]: etc/ssl/ct_log_list.cnf.dist 
│                │                       ├ [2]: etc/ssl/openssl.cnf 
│                │                       ├ [3]: etc/ssl/openssl.cnf.dist 
│                │                       ├ [4]: usr/lib/libcrypto.so.3 
│                │                       ├ [5]: usr/lib/engines-3/afalg.so 
│                │                       ├ [6]: usr/lib/engines-3/capi.so 
│                │                       ├ [7]: usr/lib/engines-3/loader_attic.so 
│                │                       ├ [8]: usr/lib/engines-3/padlock.so 
│                │                       ╰ [9]: usr/lib/ossl-modules/legacy.so 
│                ├ [23] ╭ ID            : libcurl@8.17.0-r1 
│                │      ├ Name          : libcurl 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libcurl@8.17.0-r1?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 5f058cd923236541 
│                │      ├ Version       : 8.17.0-r1 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : curl 
│                │      ├ SrcVersion    : 8.17.0-r1 
│                │      ├ Licenses       ─ [0]: curl 
│                │      ├ Maintainer    : Achill Gilgenast <achill@achill.org> 
│                │      ├ DependsOn      ╭ [0] : brotli-libs@1.2.0-r0 
│                │      │                ├ [1] : c-ares@1.34.6-r0 
│                │      │                ├ [2] : ca-certificates-bundle@20251003-r0 
│                │      │                ├ [3] : libcrypto3@3.5.4-r0 
│                │      │                ├ [4] : libidn2@2.3.8-r0 
│                │      │                ├ [5] : libpsl@0.21.5-r3 
│                │      │                ├ [6] : libssl3@3.5.4-r0 
│                │      │                ├ [7] : musl@1.2.5-r21 
│                │      │                ├ [8] : nghttp2-libs@1.68.0-r0 
│                │      │                ├ [9] : nghttp3@1.13.1-r0 
│                │      │                ├ [10]: zlib@1.3.1-r2 
│                │      │                ╰ [11]: zstd-libs@1.5.7-r2 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:4018e686de80aa87659e95c1e62a3539c1d2542f 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libcurl.so.4 
│                │                       ╰ [1]: usr/lib/libcurl.so.4.8.0 
│                ├ [24] ╭ ID            : libexpat@2.7.3-r0 
│                │      ├ Name          : libexpat 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libexpat@2.7.3-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : e9f9b31d29660cc3 
│                │      ├ Version       : 2.7.3-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : expat 
│                │      ├ SrcVersion    : 2.7.3-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Carlo Landmeter <clandmeter@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:cf92f86fbd3ac20b3317689ef17fc3e8b7ba52f6 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libexpat.so.1 
│                │                       ╰ [1]: usr/lib/libexpat.so.1.11.1 
│                ├ [25] ╭ ID            : libffi@3.5.2-r0 
│                │      ├ Name          : libffi 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libffi@3.5.2-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : c72f7679d8deb59c 
│                │      ├ Version       : 3.5.2-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libffi 
│                │      ├ SrcVersion    : 3.5.2-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:fa51bf028f40768bfe1c7ef494b1fe3f8590c19f 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libffi.so.8 
│                │                       ╰ [1]: usr/lib/libffi.so.8.2.0 
│                ├ [26] ╭ ID            : libgcc@15.2.0-r2 
│                │      ├ Name          : libgcc 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libgcc@15.2.0-r2?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 706498a3cf65ea27 
│                │      ├ Version       : 15.2.0-r2 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : gcc 
│                │      ├ SrcVersion    : 15.2.0-r2 
│                │      ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│                │      │                ╰ [1]: LGPL-2.1-or-later 
│                │      ├ Maintainer    : Ariadne Conill <ariadne@dereferenced.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:57fccbe9eebf23f2c4f38ee2a24f8b0bdd508ff7 
│                │      ╰ InstalledFiles ─ [0]: usr/lib/libgcc_s.so.1 
│                ├ [27] ╭ ID            : libidn2@2.3.8-r0 
│                │      ├ Name          : libidn2 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libidn2@2.3.8-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 4ced466399e71e2d 
│                │      ├ Version       : 2.3.8-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libidn2 
│                │      ├ SrcVersion    : 2.3.8-r0 
│                │      ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│                │      │                ╰ [1]: LGPL-3.0-or-later 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libunistring@1.4.1-r0 
│                │      │                ╰ [1]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:b8c5bfa365da5c360a01230db4d71e65af94af3d 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libidn2.so.0 
│                │                       ╰ [1]: usr/lib/libidn2.so.0.4.0 
│                ├ [28] ╭ ID            : libjpeg-turbo@3.1.2-r0 
│                │      ├ Name          : libjpeg-turbo 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libjpeg-turbo@3.1.2-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : c07f4388a4c0bc44 
│                │      ├ Version       : 3.1.2-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libjpeg-turbo 
│                │      ├ SrcVersion    : 3.1.2-r0 
│                │      ├ Licenses       ╭ [0]: BSD-3-Clause 
│                │      │                ├ [1]: IJG 
│                │      │                ╰ [2]: Zlib 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:aa025fb7ecf9bd65ef2afe47e3740639521e09ce 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libjpeg.so.8 
│                │                       ╰ [1]: usr/lib/libjpeg.so.8.3.2 
│                ├ [29] ╭ ID            : libmd@1.1.0-r0 
│                │      ├ Name          : libmd 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libmd@1.1.0-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 52b26e1bbfba437a 
│                │      ├ Version       : 1.1.0-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libmd 
│                │      ├ SrcVersion    : 1.1.0-r0 
│                │      ├ Licenses       ╭ [0]: BSD-3-Clause 
│                │      │                ├ [1]: BSD-2-Clause 
│                │      │                ├ [2]: ISC 
│                │      │                ├ [3]: Beerware 
│                │      │                ├ [4]: Public 
│                │      │                ╰ [5]: Domain 
│                │      ├ Maintainer    : omni <omni+alpine@hack.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:ce7c57bd1f6628da8ba0d3f2ac18f6d8c93c0346 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libmd.so.0 
│                │                       ╰ [1]: usr/lib/libmd.so.0.1.0 
│                ├ [30] ╭ ID            : libncursesw@6.5_p20251123-r0 
│                │      ├ Name          : libncursesw 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libncursesw@6.5_p20251123-r0?arch=x86_64&distro
│                │      │                │       =3.23.2 
│                │      │                ╰ UID : a35409bd0514dd78 
│                │      ├ Version       : 6.5_p20251123-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : ncurses 
│                │      ├ SrcVersion    : 6.5_p20251123-r0 
│                │      ├ Licenses       ─ [0]: X-11 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: musl@1.2.5-r21 
│                │      │                ╰ [1]: ncurses-terminfo-base@6.5_p20251123-r0 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:649d3041c52b80620fb50a98f5979d25ebbe1523 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libncursesw.so.6 
│                │                       ╰ [1]: usr/lib/libncursesw.so.6.5 
│                ├ [31] ╭ ID            : libpanelw@6.5_p20251123-r0 
│                │      ├ Name          : libpanelw 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libpanelw@6.5_p20251123-r0?arch=x86_64&distro=3
│                │      │                │       .23.2 
│                │      │                ╰ UID : 7a9ed0343f0b1310 
│                │      ├ Version       : 6.5_p20251123-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : ncurses 
│                │      ├ SrcVersion    : 6.5_p20251123-r0 
│                │      ├ Licenses       ─ [0]: X-11 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libncursesw@6.5_p20251123-r0 
│                │      │                ├ [1]: musl@1.2.5-r21 
│                │      │                ╰ [2]: ncurses-terminfo-base@6.5_p20251123-r0 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:ff98388ab154b09e32c313d45d389ec611e5f4b5 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libpanelw.so.6 
│                │                       ╰ [1]: usr/lib/libpanelw.so.6.5 
│                ├ [32] ╭ ID            : libpng@1.6.53-r0 
│                │      ├ Name          : libpng 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libpng@1.6.53-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : cb73e61ec749ca01 
│                │      ├ Version       : 1.6.53-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libpng 
│                │      ├ SrcVersion    : 1.6.53-r0 
│                │      ├ Licenses       ─ [0]: Libpng 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: musl@1.2.5-r21 
│                │      │                ╰ [1]: zlib@1.3.1-r2 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:bf233e45a996ce2ff4da18ec31de3b911fcfe087 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libpng16.so.16 
│                │                       ╰ [1]: usr/lib/libpng16.so.16.53.0 
│                ├ [33] ╭ ID            : libpsl@0.21.5-r3 
│                │      ├ Name          : libpsl 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libpsl@0.21.5-r3?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : f89bcb8f8b2c3fd1 
│                │      ├ Version       : 0.21.5-r3 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libpsl 
│                │      ├ SrcVersion    : 0.21.5-r3 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libidn2@2.3.8-r0 
│                │      │                ├ [1]: libunistring@1.4.1-r0 
│                │      │                ╰ [2]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:b663c00f920a93be49c825555aa1a212e4287393 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libpsl.so.5 
│                │                       ╰ [1]: usr/lib/libpsl.so.5.3.5 
│                ├ [34] ╭ ID            : libssl3@3.5.4-r0 
│                │      ├ Name          : libssl3 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libssl3@3.5.4-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : b48853cdc61496a3 
│                │      ├ Version       : 3.5.4-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : openssl 
│                │      ├ SrcVersion    : 3.5.4-r0 
│                │      ├ Licenses       ─ [0]: Apache-2.0 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libcrypto3@3.5.4-r0 
│                │      │                ╰ [1]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:e328b24da910b652aadc87242828d43db30bad67 
│                │      ╰ InstalledFiles ─ [0]: usr/lib/libssl.so.3 
│                ├ [35] ╭ ID            : libstdc++@15.2.0-r2 
│                │      ├ Name          : libstdc++ 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libstdc%2B%2B@15.2.0-r2?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : bdcd54151e7c7725 
│                │      ├ Version       : 15.2.0-r2 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : gcc 
│                │      ├ SrcVersion    : 15.2.0-r2 
│                │      ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│                │      │                ╰ [1]: LGPL-2.1-or-later 
│                │      ├ Maintainer    : Ariadne Conill <ariadne@dereferenced.org> 
│                │      ├ DependsOn      ╭ [0]: libgcc@15.2.0-r2 
│                │      │                ╰ [1]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:528d77417a16706468af852f2859ad00f176e266 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libstdc++.so.6 
│                │                       ╰ [1]: usr/lib/libstdc++.so.6.0.34 
│                ├ [36] ╭ ID            : libtasn1@4.20.0-r0 
│                │      ├ Name          : libtasn1 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libtasn1@4.20.0-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : e85d6de4c4cb9425 
│                │      ├ Version       : 4.20.0-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libtasn1 
│                │      ├ SrcVersion    : 4.20.0-r0 
│                │      ├ Licenses       ─ [0]: LGPL-2.1-or-later 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:9136bfc0b214e8914f439b72250339a38feaf2c2 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libtasn1.so.6 
│                │                       ╰ [1]: usr/lib/libtasn1.so.6.6.4 
│                ├ [37] ╭ ID            : libunistring@1.4.1-r0 
│                │      ├ Name          : libunistring 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libunistring@1.4.1-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 7200a20237fda131 
│                │      ├ Version       : 1.4.1-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libunistring 
│                │      ├ SrcVersion    : 1.4.1-r0 
│                │      ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│                │      │                ╰ [1]: LGPL-3.0-or-later 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:6e56562bde456bee5971787d3d95c34e84ced797 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libunistring.so.5 
│                │                       ╰ [1]: usr/lib/libunistring.so.5.2.1 
│                ├ [38] ╭ ID            : libx11@1.8.12-r1 
│                │      ├ Name          : libx11 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libx11@1.8.12-r1?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : ad0c9251b6202dc3 
│                │      ├ Version       : 1.8.12-r1 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libx11 
│                │      ├ SrcVersion    : 1.8.12-r1 
│                │      ├ Licenses       ─ [0]: X-11 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libxcb@1.17.0-r1 
│                │      │                ╰ [1]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:689b36ec47d6c9abb9cbd0c7067ba4636568dbd5 
│                │      ╰ InstalledFiles ╭ [0]  : usr/lib/libX11-xcb.so.1 
│                │                       ├ [1]  : usr/lib/libX11-xcb.so.1.0.0 
│                │                       ├ [2]  : usr/lib/libX11.so.6 
│                │                       ├ [3]  : usr/lib/libX11.so.6.4.0 
│                │                       ├ [4]  : usr/share/X11/XErrorDB 
│                │                       ├ [5]  : usr/share/X11/Xcms.txt 
│                │                       ├ [6]  : usr/share/X11/locale/compose.dir 
│                │                       ├ [7]  : usr/share/X11/locale/locale.alias 
│                │                       ├ [8]  : usr/share/X11/locale/locale.dir 
│                │                       ├ [9]  : usr/share/X11/locale/C/Compose 
│                │                       ├ [10] : usr/share/X11/locale/C/XI18N_OBJS 
│                │                       ├ [11] : usr/share/X11/locale/C/XLC_LOCALE 
│                │                       ├ [12] : usr/share/X11/locale/am_ET.UTF-8/Compose 
│                │                       ├ [13] : usr/share/X11/locale/am_ET.UTF-8/XI18N_OBJS 
│                │                       ├ [14] : usr/share/X11/locale/am_ET.UTF-8/XLC_LOCALE 
│                │                       ├ [15] : usr/share/X11/locale/armscii-8/Compose 
│                │                       ├ [16] : usr/share/X11/locale/armscii-8/XI18N_OBJS 
│                │                       ├ [17] : usr/share/X11/locale/armscii-8/XLC_LOCALE 
│                │                       ├ [18] : usr/share/X11/locale/cs_CZ.UTF-8/Compose 
│                │                       ├ [19] : usr/share/X11/locale/cs_CZ.UTF-8/XI18N_OBJS 
│                │                       ├ [20] : usr/share/X11/locale/cs_CZ.UTF-8/XLC_LOCALE 
│                │                       ├ [21] : usr/share/X11/locale/el_GR.UTF-8/Compose 
│                │                       ├ [22] : usr/share/X11/locale/el_GR.UTF-8/XI18N_OBJS 
│                │                       ├ [23] : usr/share/X11/locale/el_GR.UTF-8/XLC_LOCALE 
│                │                       ├ [24] : usr/share/X11/locale/en_US.UTF-8/Compose 
│                │                       ├ [25] : usr/share/X11/locale/en_US.UTF-8/XI18N_OBJS 
│                │                       ├ [26] : usr/share/X11/locale/en_US.UTF-8/XLC_LOCALE 
│                │                       ├ [27] : usr/share/X11/locale/fi_FI.UTF-8/Compose 
│                │                       ├ [28] : usr/share/X11/locale/fi_FI.UTF-8/XI18N_OBJS 
│                │                       ├ [29] : usr/share/X11/locale/fi_FI.UTF-8/XLC_LOCALE 
│                │                       ├ [30] : usr/share/X11/locale/georgian-academy/Compose 
│                │                       ├ [31] : usr/share/X11/locale/georgian-academy/XI18N_OBJS 
│                │                       ├ [32] : usr/share/X11/locale/georgian-academy/XLC_LOCALE 
│                │                       ├ [33] : usr/share/X11/locale/georgian-ps/Compose 
│                │                       ├ [34] : usr/share/X11/locale/georgian-ps/XI18N_OBJS 
│                │                       ├ [35] : usr/share/X11/locale/georgian-ps/XLC_LOCALE 
│                │                       ├ [36] : usr/share/X11/locale/ibm-cp1133/Compose 
│                │                       ├ [37] : usr/share/X11/locale/ibm-cp1133/XI18N_OBJS 
│                │                       ├ [38] : usr/share/X11/locale/ibm-cp1133/XLC_LOCALE 
│                │                       ├ [39] : usr/share/X11/locale/iscii-dev/Compose 
│                │                       ├ [40] : usr/share/X11/locale/iscii-dev/XI18N_OBJS 
│                │                       ├ [41] : usr/share/X11/locale/iscii-dev/XLC_LOCALE 
│                │                       ├ [42] : usr/share/X11/locale/isiri-3342/Compose 
│                │                       ├ [43] : usr/share/X11/locale/isiri-3342/XI18N_OBJS 
│                │                       ├ [44] : usr/share/X11/locale/isiri-3342/XLC_LOCALE 
│                │                       ├ [45] : usr/share/X11/locale/iso8859-1/Compose 
│                │                       ├ [46] : usr/share/X11/locale/iso8859-1/XI18N_OBJS 
│                │                       ├ [47] : usr/share/X11/locale/iso8859-1/XLC_LOCALE 
│                │                       ├ [48] : usr/share/X11/locale/iso8859-10/Compose 
│                │                       ├ [49] : usr/share/X11/locale/iso8859-10/XI18N_OBJS 
│                │                       ├ [50] : usr/share/X11/locale/iso8859-10/XLC_LOCALE 
│                │                       ├ [51] : usr/share/X11/locale/iso8859-11/Compose 
│                │                       ├ [52] : usr/share/X11/locale/iso8859-11/XI18N_OBJS 
│                │                       ├ [53] : usr/share/X11/locale/iso8859-11/XLC_LOCALE 
│                │                       ├ [54] : usr/share/X11/locale/iso8859-13/Compose 
│                │                       ├ [55] : usr/share/X11/locale/iso8859-13/XI18N_OBJS 
│                │                       ├ [56] : usr/share/X11/locale/iso8859-13/XLC_LOCALE 
│                │                       ├ [57] : usr/share/X11/locale/iso8859-14/Compose 
│                │                       ├ [58] : usr/share/X11/locale/iso8859-14/XI18N_OBJS 
│                │                       ├ [59] : usr/share/X11/locale/iso8859-14/XLC_LOCALE 
│                │                       ├ [60] : usr/share/X11/locale/iso8859-15/Compose 
│                │                       ├ [61] : usr/share/X11/locale/iso8859-15/XI18N_OBJS 
│                │                       ├ [62] : usr/share/X11/locale/iso8859-15/XLC_LOCALE 
│                │                       ├ [63] : usr/share/X11/locale/iso8859-2/Compose 
│                │                       ├ [64] : usr/share/X11/locale/iso8859-2/XI18N_OBJS 
│                │                       ├ [65] : usr/share/X11/locale/iso8859-2/XLC_LOCALE 
│                │                       ├ [66] : usr/share/X11/locale/iso8859-3/Compose 
│                │                       ├ [67] : usr/share/X11/locale/iso8859-3/XI18N_OBJS 
│                │                       ├ [68] : usr/share/X11/locale/iso8859-3/XLC_LOCALE 
│                │                       ├ [69] : usr/share/X11/locale/iso8859-4/Compose 
│                │                       ├ [70] : usr/share/X11/locale/iso8859-4/XI18N_OBJS 
│                │                       ├ [71] : usr/share/X11/locale/iso8859-4/XLC_LOCALE 
│                │                       ├ [72] : usr/share/X11/locale/iso8859-5/Compose 
│                │                       ├ [73] : usr/share/X11/locale/iso8859-5/XI18N_OBJS 
│                │                       ├ [74] : usr/share/X11/locale/iso8859-5/XLC_LOCALE 
│                │                       ├ [75] : usr/share/X11/locale/iso8859-6/Compose 
│                │                       ├ [76] : usr/share/X11/locale/iso8859-6/XI18N_OBJS 
│                │                       ├ [77] : usr/share/X11/locale/iso8859-6/XLC_LOCALE 
│                │                       ├ [78] : usr/share/X11/locale/iso8859-7/Compose 
│                │                       ├ [79] : usr/share/X11/locale/iso8859-7/XI18N_OBJS 
│                │                       ├ [80] : usr/share/X11/locale/iso8859-7/XLC_LOCALE 
│                │                       ├ [81] : usr/share/X11/locale/iso8859-8/Compose 
│                │                       ├ [82] : usr/share/X11/locale/iso8859-8/XI18N_OBJS 
│                │                       ├ [83] : usr/share/X11/locale/iso8859-8/XLC_LOCALE 
│                │                       ├ [84] : usr/share/X11/locale/iso8859-9/Compose 
│                │                       ├ [85] : usr/share/X11/locale/iso8859-9/XI18N_OBJS 
│                │                       ├ [86] : usr/share/X11/locale/iso8859-9/XLC_LOCALE 
│                │                       ├ [87] : usr/share/X11/locale/iso8859-9e/Compose 
│                │                       ├ [88] : usr/share/X11/locale/iso8859-9e/XI18N_OBJS 
│                │                       ├ [89] : usr/share/X11/locale/iso8859-9e/XLC_LOCALE 
│                │                       ├ [90] : usr/share/X11/locale/ja/Compose 
│                │                       ├ [91] : usr/share/X11/locale/ja/XI18N_OBJS 
│                │                       ├ [92] : usr/share/X11/locale/ja/XLC_LOCALE 
│                │                       ├ [93] : usr/share/X11/locale/ja.JIS/Compose 
│                │                       ├ [94] : usr/share/X11/locale/ja.JIS/XI18N_OBJS 
│                │                       ├ [95] : usr/share/X11/locale/ja.JIS/XLC_LOCALE 
│                │                       ├ [96] : usr/share/X11/locale/ja.SJIS/Compose 
│                │                       ├ [97] : usr/share/X11/locale/ja.SJIS/XI18N_OBJS 
│                │                       ├ [98] : usr/share/X11/locale/ja.SJIS/XLC_LOCALE 
│                │                       ├ [99] : usr/share/X11/locale/ja_JP.UTF-8/Compose 
│                │                       ├ [100]: usr/share/X11/locale/ja_JP.UTF-8/XI18N_OBJS 
│                │                       ├ [101]: usr/share/X11/locale/ja_JP.UTF-8/XLC_LOCALE 
│                │                       ├ [102]: usr/share/X11/locale/km_KH.UTF-8/Compose 
│                │                       ├ [103]: usr/share/X11/locale/km_KH.UTF-8/XI18N_OBJS 
│                │                       ├ [104]: usr/share/X11/locale/km_KH.UTF-8/XLC_LOCALE 
│                │                       ├ [105]: usr/share/X11/locale/ko/Compose 
│                │                       ├ [106]: usr/share/X11/locale/ko/XI18N_OBJS 
│                │                       ├ [107]: usr/share/X11/locale/ko/XLC_LOCALE 
│                │                       ├ [108]: usr/share/X11/locale/ko_KR.UTF-8/Compose 
│                │                       ├ [109]: usr/share/X11/locale/ko_KR.UTF-8/XI18N_OBJS 
│                │                       ├ [110]: usr/share/X11/locale/ko_KR.UTF-8/XLC_LOCALE 
│                │                       ├ [111]: usr/share/X11/locale/koi8-c/Compose 
│                │                       ├ [112]: usr/share/X11/locale/koi8-c/XI18N_OBJS 
│                │                       ├ [113]: usr/share/X11/locale/koi8-c/XLC_LOCALE 
│                │                       ├ [114]: usr/share/X11/locale/koi8-r/Compose 
│                │                       ├ [115]: usr/share/X11/locale/koi8-r/XI18N_OBJS 
│                │                       ├ [116]: usr/share/X11/locale/koi8-r/XLC_LOCALE 
│                │                       ├ [117]: usr/share/X11/locale/koi8-u/Compose 
│                │                       ├ [118]: usr/share/X11/locale/koi8-u/XI18N_OBJS 
│                │                       ├ [119]: usr/share/X11/locale/koi8-u/XLC_LOCALE 
│                │                       ├ [120]: usr/share/X11/locale/microsoft-cp1251/Compose 
│                │                       ├ [121]: usr/share/X11/locale/microsoft-cp1251/XI18N_OBJS 
│                │                       ├ [122]: usr/share/X11/locale/microsoft-cp1251/XLC_LOCALE 
│                │                       ├ [123]: usr/share/X11/locale/microsoft-cp1255/Compose 
│                │                       ├ [124]: usr/share/X11/locale/microsoft-cp1255/XI18N_OBJS 
│                │                       ├ [125]: usr/share/X11/locale/microsoft-cp1255/XLC_LOCALE 
│                │                       ├ [126]: usr/share/X11/locale/microsoft-cp1256/Compose 
│                │                       ├ [127]: usr/share/X11/locale/microsoft-cp1256/XI18N_OBJS 
│                │                       ├ [128]: usr/share/X11/locale/microsoft-cp1256/XLC_LOCALE 
│                │                       ├ [129]: usr/share/X11/locale/mulelao-1/Compose 
│                │                       ├ [130]: usr/share/X11/locale/mulelao-1/XI18N_OBJS 
│                │                       ├ [131]: usr/share/X11/locale/mulelao-1/XLC_LOCALE 
│                │                       ├ [132]: usr/share/X11/locale/nokhchi-1/Compose 
│                │                       ├ [133]: usr/share/X11/locale/nokhchi-1/XI18N_OBJS 
│                │                       ├ [134]: usr/share/X11/locale/nokhchi-1/XLC_LOCALE 
│                │                       ├ [135]: usr/share/X11/locale/pt_BR.UTF-8/Compose 
│                │                       ├ [136]: usr/share/X11/locale/pt_BR.UTF-8/XI18N_OBJS 
│                │                       ├ [137]: usr/share/X11/locale/pt_BR.UTF-8/XLC_LOCALE 
│                │                       ├ [138]: usr/share/X11/locale/pt_PT.UTF-8/Compose 
│                │                       ├ [139]: usr/share/X11/locale/pt_PT.UTF-8/XI18N_OBJS 
│                │                       ├ [140]: usr/share/X11/locale/pt_PT.UTF-8/XLC_LOCALE 
│                │                       ├ [141]: usr/share/X11/locale/ru_RU.UTF-8/Compose 
│                │                       ├ [142]: usr/share/X11/locale/ru_RU.UTF-8/XI18N_OBJS 
│                │                       ├ [143]: usr/share/X11/locale/ru_RU.UTF-8/XLC_LOCALE 
│                │                       ├ [144]: usr/share/X11/locale/sr_RS.UTF-8/Compose 
│                │                       ├ [145]: usr/share/X11/locale/sr_RS.UTF-8/XI18N_OBJS 
│                │                       ├ [146]: usr/share/X11/locale/sr_RS.UTF-8/XLC_LOCALE 
│                │                       ├ [147]: usr/share/X11/locale/tatar-cyr/Compose 
│                │                       ├ [148]: usr/share/X11/locale/tatar-cyr/XI18N_OBJS 
│                │                       ├ [149]: usr/share/X11/locale/tatar-cyr/XLC_LOCALE 
│                │                       ├ [150]: usr/share/X11/locale/th_TH/Compose 
│                │                       ├ [151]: usr/share/X11/locale/th_TH/XI18N_OBJS 
│                │                       ├ [152]: usr/share/X11/locale/th_TH/XLC_LOCALE 
│                │                       ├ [153]: usr/share/X11/locale/th_TH.UTF-8/Compose 
│                │                       ├ [154]: usr/share/X11/locale/th_TH.UTF-8/XI18N_OBJS 
│                │                       ├ [155]: usr/share/X11/locale/th_TH.UTF-8/XLC_LOCALE 
│                │                       ├ [156]: usr/share/X11/locale/tscii-0/Compose 
│                │                       ├ [157]: usr/share/X11/locale/tscii-0/XI18N_OBJS 
│                │                       ├ [158]: usr/share/X11/locale/tscii-0/XLC_LOCALE 
│                │                       ├ [159]: usr/share/X11/locale/vi_VN.tcvn/Compose 
│                │                       ├ [160]: usr/share/X11/locale/vi_VN.tcvn/XI18N_OBJS 
│                │                       ├ [161]: usr/share/X11/locale/vi_VN.tcvn/XLC_LOCALE 
│                │                       ├ [162]: usr/share/X11/locale/vi_VN.viscii/Compose 
│                │                       ├ [163]: usr/share/X11/locale/vi_VN.viscii/XI18N_OBJS 
│                │                       ├ [164]: usr/share/X11/locale/vi_VN.viscii/XLC_LOCALE 
│                │                       ├ [165]: usr/share/X11/locale/zh_CN/Compose 
│                │                       ├ [166]: usr/share/X11/locale/zh_CN/XI18N_OBJS 
│                │                       ├ [167]: usr/share/X11/locale/zh_CN/XLC_LOCALE 
│                │                       ├ [168]: usr/share/X11/locale/zh_CN.UTF-8/Compose 
│                │                       ├ [169]: usr/share/X11/locale/zh_CN.UTF-8/XI18N_OBJS 
│                │                       ├ [170]: usr/share/X11/locale/zh_CN.UTF-8/XLC_LOCALE 
│                │                       ├ [171]: usr/share/X11/locale/zh_CN.gb18030/Compose 
│                │                       ├ [172]: usr/share/X11/locale/zh_CN.gb18030/XI18N_OBJS 
│                │                       ├ [173]: usr/share/X11/locale/zh_CN.gb18030/XLC_LOCALE 
│                │                       ├ [174]: usr/share/X11/locale/zh_CN.gbk/Compose 
│                │                       ├ [175]: usr/share/X11/locale/zh_CN.gbk/XI18N_OBJS 
│                │                       ├ [176]: usr/share/X11/locale/zh_CN.gbk/XLC_LOCALE 
│                │                       ├ [177]: usr/share/X11/locale/zh_HK.UTF-8/Compose 
│                │                       ├ [178]: usr/share/X11/locale/zh_HK.UTF-8/XI18N_OBJS 
│                │                       ├ [179]: usr/share/X11/locale/zh_HK.UTF-8/XLC_LOCALE 
│                │                       ├ [180]: usr/share/X11/locale/zh_HK.big5/Compose 
│                │                       ├ [181]: usr/share/X11/locale/zh_HK.big5/XI18N_OBJS 
│                │                       ├ [182]: usr/share/X11/locale/zh_HK.big5/XLC_LOCALE 
│                │                       ├ [183]: usr/share/X11/locale/zh_HK.big5hkscs/Compose 
│                │                       ├ [184]: usr/share/X11/locale/zh_HK.big5hkscs/XI18N_OBJS 
│                │                       ├ [185]: usr/share/X11/locale/zh_HK.big5hkscs/XLC_LOCALE 
│                │                       ├ [186]: usr/share/X11/locale/zh_TW/Compose 
│                │                       ├ [187]: usr/share/X11/locale/zh_TW/XI18N_OBJS 
│                │                       ├ [188]: usr/share/X11/locale/zh_TW/XLC_LOCALE 
│                │                       ├ [189]: usr/share/X11/locale/zh_TW.UTF-8/Compose 
│                │                       ├ [190]: usr/share/X11/locale/zh_TW.UTF-8/XI18N_OBJS 
│                │                       ├ [191]: usr/share/X11/locale/zh_TW.UTF-8/XLC_LOCALE 
│                │                       ├ [192]: usr/share/X11/locale/zh_TW.big5/Compose 
│                │                       ├ [193]: usr/share/X11/locale/zh_TW.big5/XI18N_OBJS 
│                │                       ╰ [194]: usr/share/X11/locale/zh_TW.big5/XLC_LOCALE 
│                ├ [39] ╭ ID            : libxau@1.0.12-r0 
│                │      ├ Name          : libxau 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libxau@1.0.12-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 37aeecde4cde19c7 
│                │      ├ Version       : 1.0.12-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libxau 
│                │      ├ SrcVersion    : 1.0.12-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:89d2bc9daae3cb0e2ae095db6866357b7653f341 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libXau.so.6 
│                │                       ╰ [1]: usr/lib/libXau.so.6.0.0 
│                ├ [40] ╭ ID            : libxcb@1.17.0-r1 
│                │      ├ Name          : libxcb 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libxcb@1.17.0-r1?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 9fd7d10725d96cfc 
│                │      ├ Version       : 1.17.0-r1 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libxcb 
│                │      ├ SrcVersion    : 1.17.0-r1 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libxau@1.0.12-r0 
│                │      │                ├ [1]: libxdmcp@1.1.5-r1 
│                │      │                ╰ [2]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:61b06f883e8f8d2d8ee360e4dac04ac037fcca13 
│                │      ╰ InstalledFiles ╭ [0] : usr/lib/libxcb-composite.so.0 
│                │                       ├ [1] : usr/lib/libxcb-composite.so.0.0.0 
│                │                       ├ [2] : usr/lib/libxcb-damage.so.0 
│                │                       ├ [3] : usr/lib/libxcb-damage.so.0.0.0 
│                │                       ├ [4] : usr/lib/libxcb-dbe.so.0 
│                │                       ├ [5] : usr/lib/libxcb-dbe.so.0.0.0 
│                │                       ├ [6] : usr/lib/libxcb-dpms.so.0 
│                │                       ├ [7] : usr/lib/libxcb-dpms.so.0.0.0 
│                │                       ├ [8] : usr/lib/libxcb-dri2.so.0 
│                │                       ├ [9] : usr/lib/libxcb-dri2.so.0.0.0 
│                │                       ├ [10]: usr/lib/libxcb-dri3.so.0 
│                │                       ├ [11]: usr/lib/libxcb-dri3.so.0.1.0 
│                │                       ├ [12]: usr/lib/libxcb-glx.so.0 
│                │                       ├ [13]: usr/lib/libxcb-glx.so.0.0.0 
│                │                       ├ [14]: usr/lib/libxcb-present.so.0 
│                │                       ├ [15]: usr/lib/libxcb-present.so.0.0.0 
│                │                       ├ [16]: usr/lib/libxcb-randr.so.0 
│                │                       ├ [17]: usr/lib/libxcb-randr.so.0.1.0 
│                │                       ├ [18]: usr/lib/libxcb-record.so.0 
│                │                       ├ [19]: usr/lib/libxcb-record.so.0.0.0 
│                │                       ├ [20]: usr/lib/libxcb-render.so.0 
│                │                       ├ [21]: usr/lib/libxcb-render.so.0.0.0 
│                │                       ├ [22]: usr/lib/libxcb-res.so.0 
│                │                       ├ [23]: usr/lib/libxcb-res.so.0.0.0 
│                │                       ├ [24]: usr/lib/libxcb-screensaver.so.0 
│                │                       ├ [25]: usr/lib/libxcb-screensaver.so.0.0.0 
│                │                       ├ [26]: usr/lib/libxcb-shape.so.0 
│                │                       ├ [27]: usr/lib/libxcb-shape.so.0.0.0 
│                │                       ├ [28]: usr/lib/libxcb-shm.so.0 
│                │                       ├ [29]: usr/lib/libxcb-shm.so.0.0.0 
│                │                       ├ [30]: usr/lib/libxcb-sync.so.1 
│                │                       ├ [31]: usr/lib/libxcb-sync.so.1.0.0 
│                │                       ├ [32]: usr/lib/libxcb-xf86dri.so.0 
│                │                       ├ [33]: usr/lib/libxcb-xf86dri.so.0.0.0 
│                │                       ├ [34]: usr/lib/libxcb-xfixes.so.0 
│                │                       ├ [35]: usr/lib/libxcb-xfixes.so.0.0.0 
│                │                       ├ [36]: usr/lib/libxcb-xinerama.so.0 
│                │                       ├ [37]: usr/lib/libxcb-xinerama.so.0.0.0 
│                │                       ├ [38]: usr/lib/libxcb-xinput.so.0 
│                │                       ├ [39]: usr/lib/libxcb-xinput.so.0.1.0 
│                │                       ├ [40]: usr/lib/libxcb-xkb.so.1 
│                │                       ├ [41]: usr/lib/libxcb-xkb.so.1.0.0 
│                │                       ├ [42]: usr/lib/libxcb-xtest.so.0 
│                │                       ├ [43]: usr/lib/libxcb-xtest.so.0.0.0 
│                │                       ├ [44]: usr/lib/libxcb-xv.so.0 
│                │                       ├ [45]: usr/lib/libxcb-xv.so.0.0.0 
│                │                       ├ [46]: usr/lib/libxcb-xvmc.so.0 
│                │                       ├ [47]: usr/lib/libxcb-xvmc.so.0.0.0 
│                │                       ├ [48]: usr/lib/libxcb.so.1 
│                │                       ╰ [49]: usr/lib/libxcb.so.1.1.0 
│                ├ [41] ╭ ID            : libxdmcp@1.1.5-r1 
│                │      ├ Name          : libxdmcp 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libxdmcp@1.1.5-r1?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 466169ccb3517c34 
│                │      ├ Version       : 1.1.5-r1 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libxdmcp 
│                │      ├ SrcVersion    : 1.1.5-r1 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libbsd@0.12.2-r0 
│                │      │                ╰ [1]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:99a24c0fa12282b5ef89a6e732a8d494b7696d9d 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libXdmcp.so.6 
│                │                       ╰ [1]: usr/lib/libXdmcp.so.6.0.0 
│                ├ [42] ╭ ID            : libxext@1.3.6-r2 
│                │      ├ Name          : libxext 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libxext@1.3.6-r2?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 4c346f98711496dd 
│                │      ├ Version       : 1.3.6-r2 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libxext 
│                │      ├ SrcVersion    : 1.3.6-r2 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libx11@1.8.12-r1 
│                │      │                ╰ [1]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:92fb4f12c2170403d6a48c7485ecaee40c84bee2 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libXext.so.6 
│                │                       ╰ [1]: usr/lib/libXext.so.6.4.0 
│                ├ [43] ╭ ID            : libxi@1.8.2-r0 
│                │      ├ Name          : libxi 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libxi@1.8.2-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : ccc00cee81bd9473 
│                │      ├ Version       : 1.8.2-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libxi 
│                │      ├ SrcVersion    : 1.8.2-r0 
│                │      ├ Licenses       ╭ [0]: MIT 
│                │      │                ╰ [1]: X-11 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libx11@1.8.12-r1 
│                │      │                ├ [1]: libxext@1.3.6-r2 
│                │      │                ╰ [2]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:78ea3cdf1dfa3c07aa965866bb9e64be2254fc5e 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libXi.so.6 
│                │                       ╰ [1]: usr/lib/libXi.so.6.1.0 
│                ├ [44] ╭ ID            : libxrender@0.9.12-r0 
│                │      ├ Name          : libxrender 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libxrender@0.9.12-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : a017f228f1bb6c12 
│                │      ├ Version       : 0.9.12-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libxrender 
│                │      ├ SrcVersion    : 0.9.12-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libx11@1.8.12-r1 
│                │      │                ╰ [1]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:16accdec4598ad42a3201234aab60e44d607f1b0 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libXrender.so.1 
│                │                       ╰ [1]: usr/lib/libXrender.so.1.3.0 
│                ├ [45] ╭ ID            : libxtst@1.2.5-r0 
│                │      ├ Name          : libxtst 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/libxtst@1.2.5-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 5666308ca4446107 
│                │      ├ Version       : 1.2.5-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : libxtst 
│                │      ├ SrcVersion    : 1.2.5-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libx11@1.8.12-r1 
│                │      │                ├ [1]: libxext@1.3.6-r2 
│                │      │                ╰ [2]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:6c021814b3a61c34ad3d6c83b916c68159e8316f 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libXtst.so.6 
│                │                       ╰ [1]: usr/lib/libXtst.so.6.1.0 
│                ├ [46] ╭ ID            : mpdecimal@4.0.1-r0 
│                │      ├ Name          : mpdecimal 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/mpdecimal@4.0.1-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 91403780e814bc8c 
│                │      ├ Version       : 4.0.1-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : mpdecimal 
│                │      ├ SrcVersion    : 4.0.1-r0 
│                │      ├ Licenses       ─ [0]: BSD-2-Clause 
│                │      ├ Maintainer    : Stefan Stutz <stutz@pm.me> 
│                │      ├ DependsOn      ╭ [0]: libgcc@15.2.0-r2 
│                │      │                ├ [1]: libstdc++@15.2.0-r2 
│                │      │                ╰ [2]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:8ded4ff4c401cd7fb672d973289752b11bae56bf 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libmpdec++.so.4 
│                │                       ├ [1]: usr/lib/libmpdec++.so.4.0.1 
│                │                       ├ [2]: usr/lib/libmpdec.so.4 
│                │                       ╰ [3]: usr/lib/libmpdec.so.4.0.1 
│                ├ [47] ╭ ID            : musl@1.2.5-r21 
│                │      ├ Name          : musl 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/musl@1.2.5-r21?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : b403e8328a352729 
│                │      ├ Version       : 1.2.5-r21 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : musl 
│                │      ├ SrcVersion    : 1.2.5-r21 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:d05a75ec13e1a7a8bab56ce7cd3dc79bd727e698 
│                │      ╰ InstalledFiles ╭ [0]: lib/ld-musl-x86_64.so.1 
│                │                       ╰ [1]: lib/libc.musl-x86_64.so.1 
│                ├ [48] ╭ ID            : musl-utils@1.2.5-r21 
│                │      ├ Name          : musl-utils 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/musl-utils@1.2.5-r21?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 603bb96b0fa7ce27 
│                │      ├ Version       : 1.2.5-r21 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : musl 
│                │      ├ SrcVersion    : 1.2.5-r21 
│                │      ├ Licenses       ╭ [0]: MIT 
│                │      │                ├ [1]: BSD-2-Clause 
│                │      │                ╰ [2]: GPL-2.0-or-later 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: musl@1.2.5-r21 
│                │      │                ╰ [1]: scanelf@1.3.8-r2 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:daa79528d2cf877f6d656207a818d43c8dea9a30 
│                │      ╰ InstalledFiles ╭ [0]: sbin/ldconfig 
│                │                       ├ [1]: usr/bin/getconf 
│                │                       ├ [2]: usr/bin/getent 
│                │                       ├ [3]: usr/bin/iconv 
│                │                       ╰ [4]: usr/bin/ldd 
│                ├ [49] ╭ ID            : ncurses-terminfo-base@6.5_p20251123-r0 
│                │      ├ Name          : ncurses-terminfo-base 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/ncurses-terminfo-base@6.5_p20251123-r0?arch=x86
│                │      │                │       _64&distro=3.23.2 
│                │      │                ╰ UID : b39472a9551d7178 
│                │      ├ Version       : 6.5_p20251123-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : ncurses 
│                │      ├ SrcVersion    : 6.5_p20251123-r0 
│                │      ├ Licenses       ─ [0]: X-11 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:57bd1d8124ec957eefea2314bdf45b0ed1068cee 
│                │      ╰ InstalledFiles ╭ [0] : etc/terminfo/a/alacritty 
│                │                       ├ [1] : etc/terminfo/a/ansi 
│                │                       ├ [2] : etc/terminfo/d/dumb 
│                │                       ├ [3] : etc/terminfo/g/gnome 
│                │                       ├ [4] : etc/terminfo/g/gnome-256color 
│                │                       ├ [5] : etc/terminfo/k/konsole 
│                │                       ├ [6] : etc/terminfo/k/konsole-256color 
│                │                       ├ [7] : etc/terminfo/k/konsole-linux 
│                │                       ├ [8] : etc/terminfo/l/linux 
│                │                       ├ [9] : etc/terminfo/p/putty 
│                │                       ├ [10]: etc/terminfo/p/putty-256color 
│                │                       ├ [11]: etc/terminfo/r/rxvt 
│                │                       ├ [12]: etc/terminfo/r/rxvt-256color 
│                │                       ├ [13]: etc/terminfo/s/screen 
│                │                       ├ [14]: etc/terminfo/s/screen-256color 
│                │                       ├ [15]: etc/terminfo/s/st-0.6 
│                │                       ├ [16]: etc/terminfo/s/st-0.7 
│                │                       ├ [17]: etc/terminfo/s/st-0.8 
│                │                       ├ [18]: etc/terminfo/s/st-0.8.5 
│                │                       ├ [19]: etc/terminfo/s/st-16color 
│                │                       ├ [20]: etc/terminfo/s/st-256color 
│                │                       ├ [21]: etc/terminfo/s/st-direct 
│                │                       ├ [22]: etc/terminfo/s/sun 
│                │                       ├ [23]: etc/terminfo/t/terminator 
│                │                       ├ [24]: etc/terminfo/t/terminology 
│                │                       ├ [25]: etc/terminfo/t/terminology-0.6.1 
│                │                       ├ [26]: etc/terminfo/t/terminology-1.0.0 
│                │                       ├ [27]: etc/terminfo/t/terminology-1.8.1 
│                │                       ├ [28]: etc/terminfo/t/tmux 
│                │                       ├ [29]: etc/terminfo/t/tmux-256color 
│                │                       ├ [30]: etc/terminfo/v/vt100 
│                │                       ├ [31]: etc/terminfo/v/vt102 
│                │                       ├ [32]: etc/terminfo/v/vt200 
│                │                       ├ [33]: etc/terminfo/v/vt220 
│                │                       ├ [34]: etc/terminfo/v/vt52 
│                │                       ├ [35]: etc/terminfo/v/vte 
│                │                       ├ [36]: etc/terminfo/v/vte-256color 
│                │                       ├ [37]: etc/terminfo/x/xterm 
│                │                       ├ [38]: etc/terminfo/x/xterm-256color 
│                │                       ├ [39]: etc/terminfo/x/xterm-color 
│                │                       ╰ [40]: etc/terminfo/x/xterm-xfree86 
│                ├ [50] ╭ ID            : nghttp2-libs@1.68.0-r0 
│                │      ├ Name          : nghttp2-libs 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/nghttp2-libs@1.68.0-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : dca2be8e80b615ee 
│                │      ├ Version       : 1.68.0-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : nghttp2 
│                │      ├ SrcVersion    : 1.68.0-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Francesco Colista <fcolista@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:584b6a1b0aed58a3f543bfd77729b0d8a8b1745b 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libnghttp2.so.14 
│                │                       ╰ [1]: usr/lib/libnghttp2.so.14.29.2 
│                ├ [51] ╭ ID            : nghttp3@1.13.1-r0 
│                │      ├ Name          : nghttp3 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/nghttp3@1.13.1-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 47a1d1cccc4a6c6 
│                │      ├ Version       : 1.13.1-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : nghttp3 
│                │      ├ SrcVersion    : 1.13.1-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Jakub Jirutka <jakub@jirutka.cz> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:e48fcb3e81f7e46a42e3926d8513c83b7798774b 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libnghttp3.so.9 
│                │                       ╰ [1]: usr/lib/libnghttp3.so.9.5.1 
│                ├ [52] ╭ ID            : openjdk21-jre@21.0.9_p10-r0 
│                │      ├ Name          : openjdk21-jre 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/openjdk21-jre@21.0.9_p10-r0?arch=x86_64&distro=
│                │      │                │       3.23.2 
│                │      │                ╰ UID : 205951353b88a425 
│                │      ├ Version       : 21.0.9_p10-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : openjdk21 
│                │      ├ SrcVersion    : 21.0.9_p10-r0 
│                │      ├ Licenses       ─ [0]: GPL-2.0-with-classpath-exception 
│                │      ├ Maintainer    : Simon Frankenberger <simon-alpine@fraho.eu> 
│                │      ├ DependsOn      ╭ [0] : alsa-lib@1.2.14-r2 
│                │      │                ├ [1] : freetype@2.14.1-r0 
│                │      │                ├ [2] : giflib@5.2.2-r1 
│                │      │                ├ [3] : lcms2@2.17-r0 
│                │      │                ├ [4] : libjpeg-turbo@3.1.2-r0 
│                │      │                ├ [5] : libpng@1.6.53-r0 
│                │      │                ├ [6] : libx11@1.8.12-r1 
│                │      │                ├ [7] : libxext@1.3.6-r2 
│                │      │                ├ [8] : libxi@1.8.2-r0 
│                │      │                ├ [9] : libxrender@0.9.12-r0 
│                │      │                ├ [10]: libxtst@1.2.5-r0 
│                │      │                ├ [11]: musl@1.2.5-r21 
│                │      │                ╰ [12]: openjdk21-jre-headless@21.0.9_p10-r0 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:328af842b01e787bfeb37bd8c345d6d08f0feddb 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/jvm/java-21-openjdk/lib/libawt_xawt.so 
│                │                       ├ [1]: usr/lib/jvm/java-21-openjdk/lib/libfontmanager.so 
│                │                       ├ [2]: usr/lib/jvm/java-21-openjdk/lib/libjavajpeg.so 
│                │                       ├ [3]: usr/lib/jvm/java-21-openjdk/lib/libjawt.so 
│                │                       ├ [4]: usr/lib/jvm/java-21-openjdk/lib/libjsound.so 
│                │                       ├ [5]: usr/lib/jvm/java-21-openjdk/lib/liblcms.so 
│                │                       ╰ [6]: usr/lib/jvm/java-21-openjdk/lib/libsplashscreen.so 
│                ├ [53] ╭ ID            : openjdk21-jre-headless@21.0.9_p10-r0 
│                │      ├ Name          : openjdk21-jre-headless 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/openjdk21-jre-headless@21.0.9_p10-r0?arch=x86_6
│                │      │                │       4&distro=3.23.2 
│                │      │                ╰ UID : 251c82a3ee5dd21f 
│                │      ├ Version       : 21.0.9_p10-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : openjdk21 
│                │      ├ SrcVersion    : 21.0.9_p10-r0 
│                │      ├ Licenses       ─ [0]: GPL-2.0-with-classpath-exception 
│                │      ├ Maintainer    : Simon Frankenberger <simon-alpine@fraho.eu> 
│                │      ├ DependsOn      ╭ [0]: java-cacerts@1.1-r0 
│                │      │                ├ [1]: java-common@1.0-r1 
│                │      │                ├ [2]: musl@1.2.5-r21 
│                │      │                ╰ [3]: zlib@1.3.1-r2 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:cc17d54ecb7c46da305d1f71ba727969a65a9419 
│                │      ╰ InstalledFiles ╭ [0]  : usr/lib/jvm/java-21-openjdk/ASSEMBLY_EXCEPTION 
│                │                       ├ [1]  : usr/lib/jvm/java-21-openjdk/LICENSE 
│                │                       ├ [2]  : usr/lib/jvm/java-21-openjdk/README.md 
│                │                       ├ [3]  : usr/lib/jvm/java-21-openjdk/jre 
│                │                       ├ [4]  : usr/lib/jvm/java-21-openjdk/release 
│                │                       ├ [5]  : usr/lib/jvm/java-21-openjdk/bin/java 
│                │                       ├ [6]  : usr/lib/jvm/java-21-openjdk/bin/jfr 
│                │                       ├ [7]  : usr/lib/jvm/java-21-openjdk/bin/jrunscript 
│                │                       ├ [8]  : usr/lib/jvm/java-21-openjdk/bin/jwebserver 
│                │                       ├ [9]  : usr/lib/jvm/java-21-openjdk/bin/keytool 
│                │                       ├ [10] : usr/lib/jvm/java-21-openjdk/bin/rmiregistry 
│                │                       ├ [11] : usr/lib/jvm/java-21-openjdk/conf/jaxp.properties 
│                │                       ├ [12] : usr/lib/jvm/java-21-openjdk/conf/logging.properties 
│                │                       ├ [13] : usr/lib/jvm/java-21-openjdk/conf/net.properties 
│                │                       ├ [14] : usr/lib/jvm/java-21-openjdk/conf/sound.properties 
│                │                       ├ [15] : usr/lib/jvm/java-21-openjdk/conf/management/jmxremote.access 
│                │                       ├ [16] : usr/lib/jvm/java-21-openjdk/conf/management/jmxremote.passwor
│                │                       │        d.template 
│                │                       ├ [17] : usr/lib/jvm/java-21-openjdk/conf/management/management.proper
│                │                       │        ties 
│                │                       ├ [18] : usr/lib/jvm/java-21-openjdk/conf/sdp/sdp.conf.template 
│                │                       ├ [19] : usr/lib/jvm/java-21-openjdk/conf/security/java.policy 
│                │                       ├ [20] : usr/lib/jvm/java-21-openjdk/conf/security/java.security 
│                │                       ├ [21] : usr/lib/jvm/java-21-openjdk/conf/security/policy/README.txt 
│                │                       ├ [22] : usr/lib/jvm/java-21-openjdk/conf/security/policy/limited/defa
│                │                       │        ult_US_export.policy 
│                │                       ├ [23] : usr/lib/jvm/java-21-openjdk/conf/security/policy/limited/defa
│                │                       │        ult_local.policy 
│                │                       ├ [24] : usr/lib/jvm/java-21-openjdk/conf/security/policy/limited/exem
│                │                       │        pt_local.policy 
│                │                       ├ [25] : usr/lib/jvm/java-21-openjdk/conf/security/policy/unlimited/de
│                │                       │        fault_US_export.policy 
│                │                       ├ [26] : usr/lib/jvm/java-21-openjdk/conf/security/policy/unlimited/de
│                │                       │        fault_local.policy 
│                │                       ├ [27] : usr/lib/jvm/java-21-openjdk/legal/java.base/ADDITIONAL_LICENS
│                │                       │        E_INFO 
│                │                       ├ [28] : usr/lib/jvm/java-21-openjdk/legal/java.base/ASSEMBLY_EXCEPTION 
│                │                       ├ [29] : usr/lib/jvm/java-21-openjdk/legal/java.base/LICENSE 
│                │                       ├ [30] : usr/lib/jvm/java-21-openjdk/legal/java.base/aes.md 
│                │                       ├ [31] : usr/lib/jvm/java-21-openjdk/legal/java.base/asm.md 
│                │                       ├ [32] : usr/lib/jvm/java-21-openjdk/legal/java.base/c-libutl.md 
│                │                       ├ [33] : usr/lib/jvm/java-21-openjdk/legal/java.base/cldr.md 
│                │                       ├ [34] : usr/lib/jvm/java-21-openjdk/legal/java.base/icu.md 
│                │                       ├ [35] : usr/lib/jvm/java-21-openjdk/legal/java.base/public_suffix.md 
│                │                       ├ [36] : usr/lib/jvm/java-21-openjdk/legal/java.base/siphash.md 
│                │                       ├ [37] : usr/lib/jvm/java-21-openjdk/legal/java.base/unicode.md 
│                │                       ├ [38] : usr/lib/jvm/java-21-openjdk/legal/java.compiler/ADDITIONAL_LI
│                │                       │        CENSE_INFO 
│                │                       ├ [39] : usr/lib/jvm/java-21-openjdk/legal/java.compiler/ASSEMBLY_EXCE
│                │                       │        PTION 
│                │                       ├ [40] : usr/lib/jvm/java-21-openjdk/legal/java.compiler/LICENSE 
│                │                       ├ [41] : usr/lib/jvm/java-21-openjdk/legal/java.datatransfer/ADDITIONA
│                │                       │        L_LICENSE_INFO 
│                │                       ├ [42] : usr/lib/jvm/java-21-openjdk/legal/java.datatransfer/ASSEMBLY_
│                │                       │        EXCEPTION 
│                │                       ├ [43] : usr/lib/jvm/java-21-openjdk/legal/java.datatransfer/LICENSE 
│                │                       ├ [44] : usr/lib/jvm/java-21-openjdk/legal/java.desktop/ADDITIONAL_LIC
│                │                       │        ENSE_INFO 
│                │                       ├ [45] : usr/lib/jvm/java-21-openjdk/legal/java.desktop/ASSEMBLY_EXCEP
│                │                       │        TION 
│                │                       ├ [46] : usr/lib/jvm/java-21-openjdk/legal/java.desktop/LICENSE 
│                │                       ├ [47] : usr/lib/jvm/java-21-openjdk/legal/java.desktop/colorimaging.md 
│                │                       ├ [48] : usr/lib/jvm/java-21-openjdk/legal/java.desktop/harfbuzz.md 
│                │                       ├ [49] : usr/lib/jvm/java-21-openjdk/legal/java.desktop/mesa3d.md 
│                │                       ├ [50] : usr/lib/jvm/java-21-openjdk/legal/java.desktop/pipewire.md 
│                │                       ├ [51] : usr/lib/jvm/java-21-openjdk/legal/java.desktop/xwd.md 
│                │                       ├ [52] : usr/lib/jvm/java-21-openjdk/legal/java.instrument/ADDITIONAL_
│                │                       │        LICENSE_INFO 
│                │                       ├ [53] : usr/lib/jvm/java-21-openjdk/legal/java.instrument/ASSEMBLY_EX
│                │                       │        CEPTION 
│                │                       ├ [54] : usr/lib/jvm/java-21-openjdk/legal/java.instrument/LICENSE 
│                │                       ├ [55] : usr/lib/jvm/java-21-openjdk/legal/java.logging/ADDITIONAL_LIC
│                │                       │        ENSE_INFO 
│                │                       ├ [56] : usr/lib/jvm/java-21-openjdk/legal/java.logging/ASSEMBLY_EXCEP
│                │                       │        TION 
│                │                       ├ [57] : usr/lib/jvm/java-21-openjdk/legal/java.logging/LICENSE 
│                │                       ├ [58] : usr/lib/jvm/java-21-openjdk/legal/java.management/ADDITIONAL_
│                │                       │        LICENSE_INFO 
│                │                       ├ [59] : usr/lib/jvm/java-21-openjdk/legal/java.management/ASSEMBLY_EX
│                │                       │        CEPTION 
│                │                       ├ [60] : usr/lib/jvm/java-21-openjdk/legal/java.management/LICENSE 
│                │                       ├ [61] : usr/lib/jvm/java-21-openjdk/legal/java.management.rmi/ADDITIO
│                │                       │        NAL_LICENSE_INFO 
│                │                       ├ [62] : usr/lib/jvm/java-21-openjdk/legal/java.management.rmi/ASSEMBL
│                │                       │        Y_EXCEPTION 
│                │                       ├ [63] : usr/lib/jvm/java-21-openjdk/legal/java.management.rmi/LICENSE 
│                │                       ├ [64] : usr/lib/jvm/java-21-openjdk/legal/java.naming/ADDITIONAL_LICE
│                │                       │        NSE_INFO 
│                │                       ├ [65] : usr/lib/jvm/java-21-openjdk/legal/java.naming/ASSEMBLY_EXCEPT
│                │                       │        ION 
│                │                       ├ [66] : usr/lib/jvm/java-21-openjdk/legal/java.naming/LICENSE 
│                │                       ├ [67] : usr/lib/jvm/java-21-openjdk/legal/java.net.http/ADDITIONAL_LI
│                │                       │        CENSE_INFO 
│                │                       ├ [68] : usr/lib/jvm/java-21-openjdk/legal/java.net.http/ASSEMBLY_EXCE
│                │                       │        PTION 
│                │                       ├ [69] : usr/lib/jvm/java-21-openjdk/legal/java.net.http/LICENSE 
│                │                       ├ [70] : usr/lib/jvm/java-21-openjdk/legal/java.prefs/ADDITIONAL_LICEN
│                │                       │        SE_INFO 
│                │                       ├ [71] : usr/lib/jvm/java-21-openjdk/legal/java.prefs/ASSEMBLY_EXCEPTION 
│                │                       ├ [72] : usr/lib/jvm/java-21-openjdk/legal/java.prefs/LICENSE 
│                │                       ├ [73] : usr/lib/jvm/java-21-openjdk/legal/java.rmi/ADDITIONAL_LICENSE
│                │                       │        _INFO 
│                │                       ├ [74] : usr/lib/jvm/java-21-openjdk/legal/java.rmi/ASSEMBLY_EXCEPTION 
│                │                       ├ [75] : usr/lib/jvm/java-21-openjdk/legal/java.rmi/LICENSE 
│                │                       ├ [76] : usr/lib/jvm/java-21-openjdk/legal/java.scripting/ADDITIONAL_L
│                │                       │        ICENSE_INFO 
│                │                       ├ [77] : usr/lib/jvm/java-21-openjdk/legal/java.scripting/ASSEMBLY_EXC
│                │                       │        EPTION 
│                │                       ├ [78] : usr/lib/jvm/java-21-openjdk/legal/java.scripting/LICENSE 
│                │                       ├ [79] : usr/lib/jvm/java-21-openjdk/legal/java.se/ADDITIONAL_LICENSE_
│                │                       │        INFO 
│                │                       ├ [80] : usr/lib/jvm/java-21-openjdk/legal/java.se/ASSEMBLY_EXCEPTION 
│                │                       ├ [81] : usr/lib/jvm/java-21-openjdk/legal/java.se/LICENSE 
│                │                       ├ [82] : usr/lib/jvm/java-21-openjdk/legal/java.security.jgss/ADDITION
│                │                       │        AL_LICENSE_INFO 
│                │                       ├ [83] : usr/lib/jvm/java-21-openjdk/legal/java.security.jgss/ASSEMBLY
│                │                       │        _EXCEPTION 
│                │                       ├ [84] : usr/lib/jvm/java-21-openjdk/legal/java.security.jgss/LICENSE 
│                │                       ├ [85] : usr/lib/jvm/java-21-openjdk/legal/java.security.sasl/ADDITION
│                │                       │        AL_LICENSE_INFO 
│                │                       ├ [86] : usr/lib/jvm/java-21-openjdk/legal/java.security.sasl/ASSEMBLY
│                │                       │        _EXCEPTION 
│                │                       ├ [87] : usr/lib/jvm/java-21-openjdk/legal/java.security.sasl/LICENSE 
│                │                       ├ [88] : usr/lib/jvm/java-21-openjdk/legal/java.smartcardio/ADDITIONAL
│                │                       │        _LICENSE_INFO 
│                │                       ├ [89] : usr/lib/jvm/java-21-openjdk/legal/java.smartcardio/ASSEMBLY_E
│                │                       │        XCEPTION 
│                │                       ├ [90] : usr/lib/jvm/java-21-openjdk/legal/java.smartcardio/LICENSE 
│                │                       ├ [91] : usr/lib/jvm/java-21-openjdk/legal/java.smartcardio/pcsclite.md 
│                │                       ├ [92] : usr/lib/jvm/java-21-openjdk/legal/java.sql/ADDITIONAL_LICENSE
│                │                       │        _INFO 
│                │                       ├ [93] : usr/lib/jvm/java-21-openjdk/legal/java.sql/ASSEMBLY_EXCEPTION 
│                │                       ├ [94] : usr/lib/jvm/java-21-openjdk/legal/java.sql/LICENSE 
│                │                       ├ [95] : usr/lib/jvm/java-21-openjdk/legal/java.sql.rowset/ADDITIONAL_
│                │                       │        LICENSE_INFO 
│                │                       ├ [96] : usr/lib/jvm/java-21-openjdk/legal/java.sql.rowset/ASSEMBLY_EX
│                │                       │        CEPTION 
│                │                       ├ [97] : usr/lib/jvm/java-21-openjdk/legal/java.sql.rowset/LICENSE 
│                │                       ├ [98] : usr/lib/jvm/java-21-openjdk/legal/java.transaction.xa/ADDITIO
│                │                       │        NAL_LICENSE_INFO 
│                │                       ├ [99] : usr/lib/jvm/java-21-openjdk/legal/java.transaction.xa/ASSEMBL
│                │                       │        Y_EXCEPTION 
│                │                       ├ [100]: usr/lib/jvm/java-21-openjdk/legal/java.transaction.xa/LICENSE 
│                │                       ├ [101]: usr/lib/jvm/java-21-openjdk/legal/java.xml/ADDITIONAL_LICENSE
│                │                       │        _INFO 
│                │                       ├ [102]: usr/lib/jvm/java-21-openjdk/legal/java.xml/ASSEMBLY_EXCEPTION 
│                │                       ├ [103]: usr/lib/jvm/java-21-openjdk/legal/java.xml/LICENSE 
│                │                       ├ [104]: usr/lib/jvm/java-21-openjdk/legal/java.xml/bcel.md 
│                │                       ├ [105]: usr/lib/jvm/java-21-openjdk/legal/java.xml/dom.md 
│                │                       ├ [106]: usr/lib/jvm/java-21-openjdk/legal/java.xml/jcup.md 
│                │                       ├ [107]: usr/lib/jvm/java-21-openjdk/legal/java.xml/xalan.md 
│                │                       ├ [108]: usr/lib/jvm/java-21-openjdk/legal/java.xml/xerces.md 
│                │                       ├ [109]: usr/lib/jvm/java-21-openjdk/legal/java.xml.crypto/ADDITIONAL_
│                │                       │        LICENSE_INFO 
│                │                       ├ [110]: usr/lib/jvm/java-21-openjdk/legal/java.xml.crypto/ASSEMBLY_EX
│                │                       │        CEPTION 
│                │                       ├ [111]: usr/lib/jvm/java-21-openjdk/legal/java.xml.crypto/LICENSE 
│                │                       ├ [112]: usr/lib/jvm/java-21-openjdk/legal/java.xml.crypto/santuario.md 
│                │                       ├ [113]: usr/lib/jvm/java-21-openjdk/legal/jdk.accessibility/ADDITIONA
│                │                       │        L_LICENSE_INFO 
│                │                       ├ [114]: usr/lib/jvm/java-21-openjdk/legal/jdk.accessibility/ASSEMBLY_
│                │                       │        EXCEPTION 
│                │                       ├ [115]: usr/lib/jvm/java-21-openjdk/legal/jdk.accessibility/LICENSE 
│                │                       ├ [116]: usr/lib/jvm/java-21-openjdk/legal/jdk.attach/ADDITIONAL_LICEN
│                │                       │        SE_INFO 
│                │                       ├ [117]: usr/lib/jvm/java-21-openjdk/legal/jdk.attach/ASSEMBLY_EXCEPTION 
│                │                       ├ [118]: usr/lib/jvm/java-21-openjdk/legal/jdk.attach/LICENSE 
│                │                       ├ [119]: usr/lib/jvm/java-21-openjdk/legal/jdk.charsets/ADDITIONAL_LIC
│                │                       │        ENSE_INFO 
│                │                       ├ [120]: usr/lib/jvm/java-21-openjdk/legal/jdk.charsets/ASSEMBLY_EXCEP
│                │                       │        TION 
│                │                       ├ [121]: usr/lib/jvm/java-21-openjdk/legal/jdk.charsets/LICENSE 
│                │                       ├ [122]: usr/lib/jvm/java-21-openjdk/legal/jdk.compiler/ADDITIONAL_LIC
│                │                       │        ENSE_INFO 
│                │                       ├ [123]: usr/lib/jvm/java-21-openjdk/legal/jdk.compiler/ASSEMBLY_EXCEP
│                │                       │        TION 
│                │                       ├ [124]: usr/lib/jvm/java-21-openjdk/legal/jdk.compiler/LICENSE 
│                │                       ├ [125]: usr/lib/jvm/java-21-openjdk/legal/jdk.crypto.cryptoki/ADDITIO
│                │                       │        NAL_LICENSE_INFO 
│                │                       ├ [126]: usr/lib/jvm/java-21-openjdk/legal/jdk.crypto.cryptoki/ASSEMBL
│                │                       │        Y_EXCEPTION 
│                │                       ├ [127]: usr/lib/jvm/java-21-openjdk/legal/jdk.crypto.cryptoki/LICENSE 
│                │                       ├ [128]: usr/lib/jvm/java-21-openjdk/legal/jdk.crypto.cryptoki/pkcs11c
│                │                       │        ryptotoken.md 
│                │                       ├ [129]: usr/lib/jvm/java-21-openjdk/legal/jdk.crypto.cryptoki/pkcs11w
│                │                       │        rapper.md 
│                │                       ├ [130]: usr/lib/jvm/java-21-openjdk/legal/jdk.crypto.ec/ADDITIONAL_LI
│                │                       │        CENSE_INFO 
│                │                       ├ [131]: usr/lib/jvm/java-21-openjdk/legal/jdk.crypto.ec/ASSEMBLY_EXCE
│                │                       │        PTION 
│                │                       ├ [132]: usr/lib/jvm/java-21-openjdk/legal/jdk.crypto.ec/LICENSE 
│                │                       ├ [133]: usr/lib/jvm/java-21-openjdk/legal/jdk.dynalink/ADDITIONAL_LIC
│                │                       │        ENSE_INFO 
│                │                       ├ [134]: usr/lib/jvm/java-21-openjdk/legal/jdk.dynalink/ASSEMBLY_EXCEP
│                │                       │        TION 
│                │                       ├ [135]: usr/lib/jvm/java-21-openjdk/legal/jdk.dynalink/LICENSE 
│                │                       ├ [136]: usr/lib/jvm/java-21-openjdk/legal/jdk.dynalink/dynalink.md 
│                │                       ├ [137]: usr/lib/jvm/java-21-openjdk/legal/jdk.editpad/ADDITIONAL_LICE
│                │                       │        NSE_INFO 
│                │                       ├ [138]: usr/lib/jvm/java-21-openjdk/legal/jdk.editpad/ASSEMBLY_EXCEPT
│                │                       │        ION 
│                │                       ├ [139]: usr/lib/jvm/java-21-openjdk/legal/jdk.editpad/LICENSE 
│                │                       ├ [140]: usr/lib/jvm/java-21-openjdk/legal/jdk.hotspot.agent/ADDITIONA
│                │                       │        L_LICENSE_INFO 
│                │                       ├ [141]: usr/lib/jvm/java-21-openjdk/legal/jdk.hotspot.agent/ASSEMBLY_
│                │                       │        EXCEPTION 
│                │                       ├ [142]: usr/lib/jvm/java-21-openjdk/legal/jdk.hotspot.agent/LICENSE 
│                │                       ├ [143]: usr/lib/jvm/java-21-openjdk/legal/jdk.httpserver/ADDITIONAL_L
│                │                       │        ICENSE_INFO 
│                │                       ├ [144]: usr/lib/jvm/java-21-openjdk/legal/jdk.httpserver/ASSEMBLY_EXC
│                │                       │        EPTION 
│                │                       ├ [145]: usr/lib/jvm/java-21-openjdk/legal/jdk.httpserver/LICENSE 
│                │                       ├ [146]: usr/lib/jvm/java-21-openjdk/legal/jdk.incubator.vector/ADDITI
│                │                       │        ONAL_LICENSE_INFO 
│                │                       ├ [147]: usr/lib/jvm/java-21-openjdk/legal/jdk.incubator.vector/ASSEMB
│                │                       │        LY_EXCEPTION 
│                │                       ├ [148]: usr/lib/jvm/java-21-openjdk/legal/jdk.incubator.vector/LICENSE 
│                │                       ├ [149]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.ed/ADDITIONAL_
│                │                       │        LICENSE_INFO 
│                │                       ├ [150]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.ed/ASSEMBLY_EX
│                │                       │        CEPTION 
│                │                       ├ [151]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.ed/LICENSE 
│                │                       ├ [152]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.jvmstat/ADDITI
│                │                       │        ONAL_LICENSE_INFO 
│                │                       ├ [153]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.jvmstat/ASSEMB
│                │                       │        LY_EXCEPTION 
│                │                       ├ [154]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.jvmstat/LICENSE 
│                │                       ├ [155]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.le/ADDITIONAL_
│                │                       │        LICENSE_INFO 
│                │                       ├ [156]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.le/ASSEMBLY_EX
│                │                       │        CEPTION 
│                │                       ├ [157]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.le/LICENSE 
│                │                       ├ [158]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.le/jline.md 
│                │                       ├ [159]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.opt/ADDITIONAL
│                │                       │        _LICENSE_INFO 
│                │                       ├ [160]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.opt/ASSEMBLY_E
│                │                       │        XCEPTION 
│                │                       ├ [161]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.opt/LICENSE 
│                │                       ├ [162]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.opt/jopt-simpl
│                │                       │        e.md 
│                │                       ├ [163]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.vm.ci/ADDITION
│                │                       │        AL_LICENSE_INFO 
│                │                       ├ [164]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.vm.ci/ASSEMBLY
│                │                       │        _EXCEPTION 
│                │                       ├ [165]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.vm.ci/LICENSE 
│                │                       ├ [166]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.vm.compiler/AD
│                │                       │        DITIONAL_LICENSE_INFO 
│                │                       ├ [167]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.vm.compiler/AS
│                │                       │        SEMBLY_EXCEPTION 
│                │                       ├ [168]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.vm.compiler/LI
│                │                       │        CENSE 
│                │                       ├ [169]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.vm.compiler.ma
│                │                       │        nagement/ADDITIONAL_LICENSE_INFO 
│                │                       ├ [170]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.vm.compiler.ma
│                │                       │        nagement/ASSEMBLY_EXCEPTION 
│                │                       ├ [171]: usr/lib/jvm/java-21-openjdk/legal/jdk.internal.vm.compiler.ma
│                │                       │        nagement/LICENSE 
│                │                       ├ [172]: usr/lib/jvm/java-21-openjdk/legal/jdk.jartool/ADDITIONAL_LICE
│                │                       │        NSE_INFO 
│                │                       ├ [173]: usr/lib/jvm/java-21-openjdk/legal/jdk.jartool/ASSEMBLY_EXCEPT
│                │                       │        ION 
│                │                       ├ [174]: usr/lib/jvm/java-21-openjdk/legal/jdk.jartool/LICENSE 
│                │                       ├ [175]: usr/lib/jvm/java-21-openjdk/legal/jdk.javadoc/ADDITIONAL_LICE
│                │                       │        NSE_INFO 
│                │                       ├ [176]: usr/lib/jvm/java-21-openjdk/legal/jdk.javadoc/ASSEMBLY_EXCEPT
│                │                       │        ION 
│                │                       ├ [177]: usr/lib/jvm/java-21-openjdk/legal/jdk.javadoc/LICENSE 
│                │                       ├ [178]: usr/lib/jvm/java-21-openjdk/legal/jdk.javadoc/jquery.md 
│                │                       ├ [179]: usr/lib/jvm/java-21-openjdk/legal/jdk.javadoc/jqueryUI.md 
│                │                       ├ [180]: usr/lib/jvm/java-21-openjdk/legal/jdk.jcmd/ADDITIONAL_LICENSE
│                │                       │        _INFO 
│                │                       ├ [181]: usr/lib/jvm/java-21-openjdk/legal/jdk.jcmd/ASSEMBLY_EXCEPTION 
│                │                       ├ [182]: usr/lib/jvm/java-21-openjdk/legal/jdk.jcmd/LICENSE 
│                │                       ├ [183]: usr/lib/jvm/java-21-openjdk/legal/jdk.jconsole/ADDITIONAL_LIC
│                │                       │        ENSE_INFO 
│                │                       ├ [184]: usr/lib/jvm/java-21-openjdk/legal/jdk.jconsole/ASSEMBLY_EXCEP
│                │                       │        TION 
│                │                       ├ [185]: usr/lib/jvm/java-21-openjdk/legal/jdk.jconsole/LICENSE 
│                │                       ├ [186]: usr/lib/jvm/java-21-openjdk/legal/jdk.jdeps/ADDITIONAL_LICENS
│                │                       │        E_INFO 
│                │                       ├ [187]: usr/lib/jvm/java-21-openjdk/legal/jdk.jdeps/ASSEMBLY_EXCEPTION 
│                │                       ├ [188]: usr/lib/jvm/java-21-openjdk/legal/jdk.jdeps/LICENSE 
│                │                       ├ [189]: usr/lib/jvm/java-21-openjdk/legal/jdk.jdi/ADDITIONAL_LICENSE_
│                │                       │        INFO 
│                │                       ├ [190]: usr/lib/jvm/java-21-openjdk/legal/jdk.jdi/ASSEMBLY_EXCEPTION 
│                │                       ├ [191]: usr/lib/jvm/java-21-openjdk/legal/jdk.jdi/LICENSE 
│                │                       ├ [192]: usr/lib/jvm/java-21-openjdk/legal/jdk.jdwp.agent/ADDITIONAL_L
│                │                       │        ICENSE_INFO 
│                │                       ├ [193]: usr/lib/jvm/java-21-openjdk/legal/jdk.jdwp.agent/ASSEMBLY_EXC
│                │                       │        EPTION 
│                │                       ├ [194]: usr/lib/jvm/java-21-openjdk/legal/jdk.jdwp.agent/LICENSE 
│                │                       ├ [195]: usr/lib/jvm/java-21-openjdk/legal/jdk.jfr/ADDITIONAL_LICENSE_
│                │                       │        INFO 
│                │                       ├ [196]: usr/lib/jvm/java-21-openjdk/legal/jdk.jfr/ASSEMBLY_EXCEPTION 
│                │                       ├ [197]: usr/lib/jvm/java-21-openjdk/legal/jdk.jfr/LICENSE 
│                │                       ├ [198]: usr/lib/jvm/java-21-openjdk/legal/jdk.jlink/ADDITIONAL_LICENS
│                │                       │        E_INFO 
│                │                       ├ [199]: usr/lib/jvm/java-21-openjdk/legal/jdk.jlink/ASSEMBLY_EXCEPTION 
│                │                       ├ [200]: usr/lib/jvm/java-21-openjdk/legal/jdk.jlink/LICENSE 
│                │                       ├ [201]: usr/lib/jvm/java-21-openjdk/legal/jdk.jpackage/ADDITIONAL_LIC
│                │                       │        ENSE_INFO 
│                │                       ├ [202]: usr/lib/jvm/java-21-openjdk/legal/jdk.jpackage/ASSEMBLY_EXCEP
│                │                       │        TION 
│                │                       ├ [203]: usr/lib/jvm/java-21-openjdk/legal/jdk.jpackage/LICENSE 
│                │                       ├ [204]: usr/lib/jvm/java-21-openjdk/legal/jdk.jshell/ADDITIONAL_LICEN
│                │                       │        SE_INFO 
│                │                       ├ [205]: usr/lib/jvm/java-21-openjdk/legal/jdk.jshell/ASSEMBLY_EXCEPTION 
│                │                       ├ [206]: usr/lib/jvm/java-21-openjdk/legal/jdk.jshell/LICENSE 
│                │                       ├ [207]: usr/lib/jvm/java-21-openjdk/legal/jdk.jsobject/ADDITIONAL_LIC
│                │                       │        ENSE_INFO 
│                │                       ├ [208]: usr/lib/jvm/java-21-openjdk/legal/jdk.jsobject/ASSEMBLY_EXCEP
│                │                       │        TION 
│                │                       ├ [209]: usr/lib/jvm/java-21-openjdk/legal/jdk.jsobject/LICENSE 
│                │                       ├ [210]: usr/lib/jvm/java-21-openjdk/legal/jdk.jstatd/ADDITIONAL_LICEN
│                │                       │        SE_INFO 
│                │                       ├ [211]: usr/lib/jvm/java-21-openjdk/legal/jdk.jstatd/ASSEMBLY_EXCEPTION 
│                │                       ├ [212]: usr/lib/jvm/java-21-openjdk/legal/jdk.jstatd/LICENSE 
│                │                       ├ [213]: usr/lib/jvm/java-21-openjdk/legal/jdk.localedata/ADDITIONAL_L
│                │                       │        ICENSE_INFO 
│                │                       ├ [214]: usr/lib/jvm/java-21-openjdk/legal/jdk.localedata/ASSEMBLY_EXC
│                │                       │        EPTION 
│                │                       ├ [215]: usr/lib/jvm/java-21-openjdk/legal/jdk.localedata/LICENSE 
│                │                       ├ [216]: usr/lib/jvm/java-21-openjdk/legal/jdk.localedata/cldr.md 
│                │                       ├ [217]: usr/lib/jvm/java-21-openjdk/legal/jdk.localedata/thaidict.md 
│                │                       ├ [218]: usr/lib/jvm/java-21-openjdk/legal/jdk.management/ADDITIONAL_L
│                │                       │        ICENSE_INFO 
│                │                       ├ [219]: usr/lib/jvm/java-21-openjdk/legal/jdk.management/ASSEMBLY_EXC
│                │                       │        EPTION 
│                │                       ├ [220]: usr/lib/jvm/java-21-openjdk/legal/jdk.management/LICENSE 
│                │                       ├ [221]: usr/lib/jvm/java-21-openjdk/legal/jdk.management.agent/ADDITI
│                │                       │        ONAL_LICENSE_INFO 
│                │                       ├ [222]: usr/lib/jvm/java-21-openjdk/legal/jdk.management.agent/ASSEMB
│                │                       │        LY_EXCEPTION 
│                │                       ├ [223]: usr/lib/jvm/java-21-openjdk/legal/jdk.management.agent/LICENSE 
│                │                       ├ [224]: usr/lib/jvm/java-21-openjdk/legal/jdk.management.jfr/ADDITION
│                │                       │        AL_LICENSE_INFO 
│                │                       ├ [225]: usr/lib/jvm/java-21-openjdk/legal/jdk.management.jfr/ASSEMBLY
│                │                       │        _EXCEPTION 
│                │                       ├ [226]: usr/lib/jvm/java-21-openjdk/legal/jdk.management.jfr/LICENSE 
│                │                       ├ [227]: usr/lib/jvm/java-21-openjdk/legal/jdk.naming.dns/ADDITIONAL_L
│                │                       │        ICENSE_INFO 
│                │                       ├ [228]: usr/lib/jvm/java-21-openjdk/legal/jdk.naming.dns/ASSEMBLY_EXC
│                │                       │        EPTION 
│                │                       ├ [229]: usr/lib/jvm/java-21-openjdk/legal/jdk.naming.dns/LICENSE 
│                │                       ├ [230]: usr/lib/jvm/java-21-openjdk/legal/jdk.naming.rmi/ADDITIONAL_L
│                │                       │        ICENSE_INFO 
│                │                       ├ [231]: usr/lib/jvm/java-21-openjdk/legal/jdk.naming.rmi/ASSEMBLY_EXC
│                │                       │        EPTION 
│                │                       ├ [232]: usr/lib/jvm/java-21-openjdk/legal/jdk.naming.rmi/LICENSE 
│                │                       ├ [233]: usr/lib/jvm/java-21-openjdk/legal/jdk.net/ADDITIONAL_LICENSE_
│                │                       │        INFO 
│                │                       ├ [234]: usr/lib/jvm/java-21-openjdk/legal/jdk.net/ASSEMBLY_EXCEPTION 
│                │                       ├ [235]: usr/lib/jvm/java-21-openjdk/legal/jdk.net/LICENSE 
│                │                       ├ [236]: usr/lib/jvm/java-21-openjdk/legal/jdk.nio.mapmode/ADDITIONAL_
│                │                       │        LICENSE_INFO 
│                │                       ├ [237]: usr/lib/jvm/java-21-openjdk/legal/jdk.nio.mapmode/ASSEMBLY_EX
│                │                       │        CEPTION 
│                │                       ├ [238]: usr/lib/jvm/java-21-openjdk/legal/jdk.nio.mapmode/LICENSE 
│                │                       ├ [239]: usr/lib/jvm/java-21-openjdk/legal/jdk.random/ADDITIONAL_LICEN
│                │                       │        SE_INFO 
│                │                       ├ [240]: usr/lib/jvm/java-21-openjdk/legal/jdk.random/ASSEMBLY_EXCEPTION 
│                │                       ├ [241]: usr/lib/jvm/java-21-openjdk/legal/jdk.random/LICENSE 
│                │                       ├ [242]: usr/lib/jvm/java-21-openjdk/legal/jdk.sctp/ADDITIONAL_LICENSE
│                │                       │        _INFO 
│                │                       ├ [243]: usr/lib/jvm/java-21-openjdk/legal/jdk.sctp/ASSEMBLY_EXCEPTION 
│                │                       ├ [244]: usr/lib/jvm/java-21-openjdk/legal/jdk.sctp/LICENSE 
│                │                       ├ [245]: usr/lib/jvm/java-21-openjdk/legal/jdk.security.auth/ADDITIONA
│                │                       │        L_LICENSE_INFO 
│                │                       ├ [246]: usr/lib/jvm/java-21-openjdk/legal/jdk.security.auth/ASSEMBLY_
│                │                       │        EXCEPTION 
│                │                       ├ [247]: usr/lib/jvm/java-21-openjdk/legal/jdk.security.auth/LICENSE 
│                │                       ├ [248]: usr/lib/jvm/java-21-openjdk/legal/jdk.security.jgss/ADDITIONA
│                │                       │        L_LICENSE_INFO 
│                │                       ├ [249]: usr/lib/jvm/java-21-openjdk/legal/jdk.security.jgss/ASSEMBLY_
│                │                       │        EXCEPTION 
│                │                       ├ [250]: usr/lib/jvm/java-21-openjdk/legal/jdk.security.jgss/LICENSE 
│                │                       ├ [251]: usr/lib/jvm/java-21-openjdk/legal/jdk.unsupported/ADDITIONAL_
│                │                       │        LICENSE_INFO 
│                │                       ├ [252]: usr/lib/jvm/java-21-openjdk/legal/jdk.unsupported/ASSEMBLY_EX
│                │                       │        CEPTION 
│                │                       ├ [253]: usr/lib/jvm/java-21-openjdk/legal/jdk.unsupported/LICENSE 
│                │                       ├ [254]: usr/lib/jvm/java-21-openjdk/legal/jdk.unsupported.desktop/ADD
│                │                       │        ITIONAL_LICENSE_INFO 
│                │                       ├ [255]: usr/lib/jvm/java-21-openjdk/legal/jdk.unsupported.desktop/ASS
│                │                       │        EMBLY_EXCEPTION 
│                │                       ├ [256]: usr/lib/jvm/java-21-openjdk/legal/jdk.unsupported.desktop/LIC
│                │                       │        ENSE 
│                │                       ├ [257]: usr/lib/jvm/java-21-openjdk/legal/jdk.xml.dom/ADDITIONAL_LICE
│                │                       │        NSE_INFO 
│                │                       ├ [258]: usr/lib/jvm/java-21-openjdk/legal/jdk.xml.dom/ASSEMBLY_EXCEPT
│                │                       │        ION 
│                │                       ├ [259]: usr/lib/jvm/java-21-openjdk/legal/jdk.xml.dom/LICENSE 
│                │                       ├ [260]: usr/lib/jvm/java-21-openjdk/legal/jdk.zipfs/ADDITIONAL_LICENS
│                │                       │        E_INFO 
│                │                       ├ [261]: usr/lib/jvm/java-21-openjdk/legal/jdk.zipfs/ASSEMBLY_EXCEPTION 
│                │                       ├ [262]: usr/lib/jvm/java-21-openjdk/legal/jdk.zipfs/LICENSE 
│                │                       ├ [263]: usr/lib/jvm/java-21-openjdk/lib/classlist 
│                │                       ├ [264]: usr/lib/jvm/java-21-openjdk/lib/jexec 
│                │                       ├ [265]: usr/lib/jvm/java-21-openjdk/lib/jrt-fs.jar 
│                │                       ├ [266]: usr/lib/jvm/java-21-openjdk/lib/jspawnhelper 
│                │                       ├ [267]: usr/lib/jvm/java-21-openjdk/lib/jvm.cfg 
│                │                       ├ [268]: usr/lib/jvm/java-21-openjdk/lib/libattach.so 
│                │                       ├ [269]: usr/lib/jvm/java-21-openjdk/lib/libawt.so 
│                │                       ├ [270]: usr/lib/jvm/java-21-openjdk/lib/libawt_headless.so 
│                │                       ├ [271]: usr/lib/jvm/java-21-openjdk/lib/libdt_socket.so 
│                │                       ├ [272]: usr/lib/jvm/java-21-openjdk/lib/libextnet.so 
│                │                       ├ [273]: usr/lib/jvm/java-21-openjdk/lib/libinstrument.so 
│                │                       ├ [274]: usr/lib/jvm/java-21-openjdk/lib/libj2gss.so 
│                │                       ├ [275]: usr/lib/jvm/java-21-openjdk/lib/libj2pcsc.so 
│                │                       ├ [276]: usr/lib/jvm/java-21-openjdk/lib/libj2pkcs11.so 
│                │                       ├ [277]: usr/lib/jvm/java-21-openjdk/lib/libjaas.so 
│                │                       ├ [278]: usr/lib/jvm/java-21-openjdk/lib/libjava.so 
│                │                       ├ [279]: usr/lib/jvm/java-21-openjdk/lib/libjdwp.so 
│                │                       ├ [280]: usr/lib/jvm/java-21-openjdk/lib/libjimage.so 
│                │                       ├ [281]: usr/lib/jvm/java-21-openjdk/lib/libjli.so 
│                │                       ├ [282]: usr/lib/jvm/java-21-openjdk/lib/libjsig.so 
│                │                       ├ [283]: usr/lib/jvm/java-21-openjdk/lib/libjsvml.so 
│                │                       ├ [284]: usr/lib/jvm/java-21-openjdk/lib/lible.so 
│                │                       ├ [285]: usr/lib/jvm/java-21-openjdk/lib/libmanagement.so 
│                │                       ├ [286]: usr/lib/jvm/java-21-openjdk/lib/libmanagement_agent.so 
│                │                       ├ [287]: usr/lib/jvm/java-21-openjdk/lib/libmanagement_ext.so 
│                │                       ├ [288]: usr/lib/jvm/java-21-openjdk/lib/libmlib_image.so 
│                │                       ├ [289]: usr/lib/jvm/java-21-openjdk/lib/libnet.so 
│                │                       ├ [290]: usr/lib/jvm/java-21-openjdk/lib/libnio.so 
│                │                       ├ [291]: usr/lib/jvm/java-21-openjdk/lib/libprefs.so 
│                │                       ├ [292]: usr/lib/jvm/java-21-openjdk/lib/librmi.so 
│                │                       ├ [293]: usr/lib/jvm/java-21-openjdk/lib/libsaproc.so 
│                │                       ├ [294]: usr/lib/jvm/java-21-openjdk/lib/libsctp.so 
│                │                       ├ [295]: usr/lib/jvm/java-21-openjdk/lib/libsyslookup.so 
│                │                       ├ [296]: usr/lib/jvm/java-21-openjdk/lib/libverify.so 
│                │                       ├ [297]: usr/lib/jvm/java-21-openjdk/lib/libzip.so 
│                │                       ├ [298]: usr/lib/jvm/java-21-openjdk/lib/modules 
│                │                       ├ [299]: usr/lib/jvm/java-21-openjdk/lib/psfont.properties.ja 
│                │                       ├ [300]: usr/lib/jvm/java-21-openjdk/lib/psfontj2d.properties 
│                │                       ├ [301]: usr/lib/jvm/java-21-openjdk/lib/tzdb.dat 
│                │                       ├ [302]: usr/lib/jvm/java-21-openjdk/lib/jfr/default.jfc 
│                │                       ├ [303]: usr/lib/jvm/java-21-openjdk/lib/jfr/profile.jfc 
│                │                       ├ [304]: usr/lib/jvm/java-21-openjdk/lib/security/blocked.certs 
│                │                       ├ [305]: usr/lib/jvm/java-21-openjdk/lib/security/cacerts 
│                │                       ├ [306]: usr/lib/jvm/java-21-openjdk/lib/security/default.policy 
│                │                       ├ [307]: usr/lib/jvm/java-21-openjdk/lib/security/public_suffix_list.dat 
│                │                       ├ [308]: usr/lib/jvm/java-21-openjdk/lib/server/classes.jsa 
│                │                       ├ [309]: usr/lib/jvm/java-21-openjdk/lib/server/classes_nocoops.jsa 
│                │                       ├ [310]: usr/lib/jvm/java-21-openjdk/lib/server/libjsig.so 
│                │                       ╰ [311]: usr/lib/jvm/java-21-openjdk/lib/server/libjvm.so 
│                ├ [54] ╭ ID            : openssl@3.5.4-r0 
│                │      ├ Name          : openssl 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/openssl@3.5.4-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : a1cd04a89fc287e3 
│                │      ├ Version       : 3.5.4-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : openssl 
│                │      ├ SrcVersion    : 3.5.4-r0 
│                │      ├ Licenses       ─ [0]: Apache-2.0 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0]: libcrypto3@3.5.4-r0 
│                │      │                ├ [1]: libssl3@3.5.4-r0 
│                │      │                ╰ [2]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:c2a94fa9b033f8a1066e3545cbe6b4e86e54e9b8 
│                │      ╰ InstalledFiles ─ [0]: usr/bin/openssl 
│                ├ [55] ╭ ID            : p11-kit@0.25.5-r2 
│                │      ├ Name          : p11-kit 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/p11-kit@0.25.5-r2?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : b0d6e48300259c9f 
│                │      ├ Version       : 0.25.5-r2 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : p11-kit 
│                │      ├ SrcVersion    : 0.25.5-r2 
│                │      ├ Licenses       ─ [0]: BSD-3-Clause 
│                │      ├ Maintainer    : Patrycja Rosa <alpine@ptrcnull.me> 
│                │      ├ DependsOn      ╭ [0]: libffi@3.5.2-r0 
│                │      │                ├ [1]: libtasn1@4.20.0-r0 
│                │      │                ╰ [2]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:b03c9c498fc8b875d694659827c39e791b0dce51 
│                │      ╰ InstalledFiles ╭ [0]: etc/pkcs11/pkcs11.conf.example 
│                │                       ├ [1]: usr/bin/p11-kit 
│                │                       ├ [2]: usr/lib/libp11-kit.so.0 
│                │                       ├ [3]: usr/lib/libp11-kit.so.0.4.1 
│                │                       ├ [4]: usr/libexec/p11-kit/p11-kit-remote 
│                │                       ╰ [5]: usr/libexec/p11-kit/trust-extract-compat 
│                ├ [56] ╭ ID            : p11-kit-trust@0.25.5-r2 
│                │      ├ Name          : p11-kit-trust 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/p11-kit-trust@0.25.5-r2?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : cdbfa4b26a87980f 
│                │      ├ Version       : 0.25.5-r2 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : p11-kit 
│                │      ├ SrcVersion    : 0.25.5-r2 
│                │      ├ Licenses       ─ [0]: BSD-3-Clause 
│                │      ├ Maintainer    : Patrycja Rosa <alpine@ptrcnull.me> 
│                │      ├ DependsOn      ╭ [0]: libtasn1@4.20.0-r0 
│                │      │                ├ [1]: musl@1.2.5-r21 
│                │      │                ╰ [2]: p11-kit@0.25.5-r2 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:566b28378ea154f29cc0c26050403949573a7cd1 
│                │      ╰ InstalledFiles ╭ [0]: usr/bin/trust 
│                │                       ├ [1]: usr/lib/pkcs11/p11-kit-trust.so 
│                │                       ╰ [2]: usr/share/p11-kit/modules/p11-kit-trust.module 
│                ├ [57] ╭ ID            : py3-packaging@25.0-r0 
│                │      ├ Name          : py3-packaging 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/py3-packaging@25.0-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 34c3dcafdb92e3d6 
│                │      ├ Version       : 25.0-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : py3-packaging 
│                │      ├ SrcVersion    : 25.0-r0 
│                │      ├ Licenses       ╭ [0]: Apache-2.0 
│                │      │                ╰ [1]: BSD-2-Clause 
│                │      ├ Maintainer    : Peter Shkenev <santurysim@gmail.com> 
│                │      ├ DependsOn      ╭ [0]: py3-parsing@3.2.3-r0 
│                │      │                ╰ [1]: python3@3.12.12-r0 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:e09cd5f2c2613d8be8704d833ee8e1b73ed6ca33 
│                │      ╰ InstalledFiles ╭ [0] : usr/lib/python3.12/site-packages/packaging/__init__.py 
│                │                       ├ [1] : usr/lib/python3.12/site-packages/packaging/_elffile.py 
│                │                       ├ [2] : usr/lib/python3.12/site-packages/packaging/_manylinux.py 
│                │                       ├ [3] : usr/lib/python3.12/site-packages/packaging/_musllinux.py 
│                │                       ├ [4] : usr/lib/python3.12/site-packages/packaging/_parser.py 
│                │                       ├ [5] : usr/lib/python3.12/site-packages/packaging/_structures.py 
│                │                       ├ [6] : usr/lib/python3.12/site-packages/packaging/_tokenizer.py 
│                │                       ├ [7] : usr/lib/python3.12/site-packages/packaging/markers.py 
│                │                       ├ [8] : usr/lib/python3.12/site-packages/packaging/metadata.py 
│                │                       ├ [9] : usr/lib/python3.12/site-packages/packaging/py.typed 
│                │                       ├ [10]: usr/lib/python3.12/site-packages/packaging/requirements.py 
│                │                       ├ [11]: usr/lib/python3.12/site-packages/packaging/specifiers.py 
│                │                       ├ [12]: usr/lib/python3.12/site-packages/packaging/tags.py 
│                │                       ├ [13]: usr/lib/python3.12/site-packages/packaging/utils.py 
│                │                       ├ [14]: usr/lib/python3.12/site-packages/packaging/version.py 
│                │                       ├ [15]: usr/lib/python3.12/site-packages/packaging-25.0.dist-info/META
│                │                       │       DATA 
│                │                       ├ [16]: usr/lib/python3.12/site-packages/packaging-25.0.dist-info/RECORD 
│                │                       ├ [17]: usr/lib/python3.12/site-packages/packaging-25.0.dist-info/WHEEL 
│                │                       ├ [18]: usr/lib/python3.12/site-packages/packaging-25.0.dist-info/lice
│                │                       │       nses/LICENSE 
│                │                       ├ [19]: usr/lib/python3.12/site-packages/packaging-25.0.dist-info/lice
│                │                       │       nses/LICENSE.APACHE 
│                │                       ├ [20]: usr/lib/python3.12/site-packages/packaging-25.0.dist-info/lice
│                │                       │       nses/LICENSE.BSD 
│                │                       ├ [21]: usr/lib/python3.12/site-packages/packaging/licenses/__init__.py 
│                │                       ╰ [22]: usr/lib/python3.12/site-packages/packaging/licenses/_spdx.py 
│                ├ [58] ╭ ID            : py3-packaging-pyc@25.0-r0 
│                │      ├ Name          : py3-packaging-pyc 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/py3-packaging-pyc@25.0-r0?arch=x86_64&distro=3.
│                │      │                │       23.2 
│                │      │                ╰ UID : 1da8bdaae4360b85 
│                │      ├ Version       : 25.0-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : py3-packaging 
│                │      ├ SrcVersion    : 25.0-r0 
│                │      ├ Licenses       ╭ [0]: Apache-2.0 
│                │      │                ╰ [1]: BSD-2-Clause 
│                │      ├ Maintainer    : Peter Shkenev <santurysim@gmail.com> 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:0175e03c745fcd319d5a73622b5f94d698749ee4 
│                │      ╰ InstalledFiles ╭ [0] : usr/lib/python3.12/site-packages/packaging/__pycache__/__init_
│                │                       │       _.cpython-312.pyc 
│                │                       ├ [1] : usr/lib/python3.12/site-packages/packaging/__pycache__/_elffil
│                │                       │       e.cpython-312.pyc 
│                │                       ├ [2] : usr/lib/python3.12/site-packages/packaging/__pycache__/_manyli
│                │                       │       nux.cpython-312.pyc 
│                │                       ├ [3] : usr/lib/python3.12/site-packages/packaging/__pycache__/_muslli
│                │                       │       nux.cpython-312.pyc 
│                │                       ├ [4] : usr/lib/python3.12/site-packages/packaging/__pycache__/_parser
│                │                       │       .cpython-312.pyc 
│                │                       ├ [5] : usr/lib/python3.12/site-packages/packaging/__pycache__/_struct
│                │                       │       ures.cpython-312.pyc 
│                │                       ├ [6] : usr/lib/python3.12/site-packages/packaging/__pycache__/_tokeni
│                │                       │       zer.cpython-312.pyc 
│                │                       ├ [7] : usr/lib/python3.12/site-packages/packaging/__pycache__/markers
│                │                       │       .cpython-312.pyc 
│                │                       ├ [8] : usr/lib/python3.12/site-packages/packaging/__pycache__/metadat
│                │                       │       a.cpython-312.pyc 
│                │                       ├ [9] : usr/lib/python3.12/site-packages/packaging/__pycache__/require
│                │                       │       ments.cpython-312.pyc 
│                │                       ├ [10]: usr/lib/python3.12/site-packages/packaging/__pycache__/specifi
│                │                       │       ers.cpython-312.pyc 
│                │                       ├ [11]: usr/lib/python3.12/site-packages/packaging/__pycache__/tags.cp
│                │                       │       ython-312.pyc 
│                │                       ├ [12]: usr/lib/python3.12/site-packages/packaging/__pycache__/utils.c
│                │                       │       python-312.pyc 
│                │                       ├ [13]: usr/lib/python3.12/site-packages/packaging/__pycache__/version
│                │                       │       .cpython-312.pyc 
│                │                       ├ [14]: usr/lib/python3.12/site-packages/packaging/licenses/__pycache_
│                │                       │       _/__init__.cpython-312.pyc 
│                │                       ╰ [15]: usr/lib/python3.12/site-packages/packaging/licenses/__pycache_
│                │                               _/_spdx.cpython-312.pyc 
│                ├ [59] ╭ ID            : py3-parsing@3.2.3-r0 
│                │      ├ Name          : py3-parsing 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/py3-parsing@3.2.3-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 6a5922fc39d98107 
│                │      ├ Version       : 3.2.3-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : py3-parsing 
│                │      ├ SrcVersion    : 3.2.3-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: python3@3.12.12-r0 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:4629e466d7ba4ed095bc0bdb3c6bad75b9b36cf6 
│                │      ╰ InstalledFiles ╭ [0] : usr/lib/python3.12/site-packages/pyparsing/__init__.py 
│                │                       ├ [1] : usr/lib/python3.12/site-packages/pyparsing/actions.py 
│                │                       ├ [2] : usr/lib/python3.12/site-packages/pyparsing/common.py 
│                │                       ├ [3] : usr/lib/python3.12/site-packages/pyparsing/core.py 
│                │                       ├ [4] : usr/lib/python3.12/site-packages/pyparsing/exceptions.py 
│                │                       ├ [5] : usr/lib/python3.12/site-packages/pyparsing/helpers.py 
│                │                       ├ [6] : usr/lib/python3.12/site-packages/pyparsing/py.typed 
│                │                       ├ [7] : usr/lib/python3.12/site-packages/pyparsing/results.py 
│                │                       ├ [8] : usr/lib/python3.12/site-packages/pyparsing/testing.py 
│                │                       ├ [9] : usr/lib/python3.12/site-packages/pyparsing/unicode.py 
│                │                       ├ [10]: usr/lib/python3.12/site-packages/pyparsing/util.py 
│                │                       ├ [11]: usr/lib/python3.12/site-packages/pyparsing-3.2.3.dist-info/MET
│                │                       │       ADATA 
│                │                       ├ [12]: usr/lib/python3.12/site-packages/pyparsing-3.2.3.dist-info/REC
│                │                       │       ORD 
│                │                       ├ [13]: usr/lib/python3.12/site-packages/pyparsing-3.2.3.dist-info/WHEEL 
│                │                       ├ [14]: usr/lib/python3.12/site-packages/pyparsing-3.2.3.dist-info/lic
│                │                       │       enses/LICENSE 
│                │                       ├ [15]: usr/lib/python3.12/site-packages/pyparsing/diagram/__init__.py 
│                │                       ├ [16]: usr/lib/python3.12/site-packages/pyparsing/tools/__init__.py 
│                │                       ╰ [17]: usr/lib/python3.12/site-packages/pyparsing/tools/cvt_pyparsing
│                │                               _pep8_names.py 
│                ├ [60] ╭ ID            : py3-parsing-pyc@3.2.3-r0 
│                │      ├ Name          : py3-parsing-pyc 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/py3-parsing-pyc@3.2.3-r0?arch=x86_64&distro=3.2
│                │      │                │       3.2 
│                │      │                ╰ UID : d0a70f926c79e309 
│                │      ├ Version       : 3.2.3-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : py3-parsing 
│                │      ├ SrcVersion    : 3.2.3-r0 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:d687c1f6ce81a3709f4989d4d5baa451cf4cdb9b 
│                │      ╰ InstalledFiles ╭ [0] : usr/lib/python3.12/site-packages/pyparsing/__pycache__/__init_
│                │                       │       _.cpython-312.pyc 
│                │                       ├ [1] : usr/lib/python3.12/site-packages/pyparsing/__pycache__/actions
│                │                       │       .cpython-312.pyc 
│                │                       ├ [2] : usr/lib/python3.12/site-packages/pyparsing/__pycache__/common.
│                │                       │       cpython-312.pyc 
│                │                       ├ [3] : usr/lib/python3.12/site-packages/pyparsing/__pycache__/core.cp
│                │                       │       ython-312.pyc 
│                │                       ├ [4] : usr/lib/python3.12/site-packages/pyparsing/__pycache__/excepti
│                │                       │       ons.cpython-312.pyc 
│                │                       ├ [5] : usr/lib/python3.12/site-packages/pyparsing/__pycache__/helpers
│                │                       │       .cpython-312.pyc 
│                │                       ├ [6] : usr/lib/python3.12/site-packages/pyparsing/__pycache__/results
│                │                       │       .cpython-312.pyc 
│                │                       ├ [7] : usr/lib/python3.12/site-packages/pyparsing/__pycache__/testing
│                │                       │       .cpython-312.pyc 
│                │                       ├ [8] : usr/lib/python3.12/site-packages/pyparsing/__pycache__/unicode
│                │                       │       .cpython-312.pyc 
│                │                       ├ [9] : usr/lib/python3.12/site-packages/pyparsing/__pycache__/util.cp
│                │                       │       ython-312.pyc 
│                │                       ├ [10]: usr/lib/python3.12/site-packages/pyparsing/diagram/__pycache__
│                │                       │       /__init__.cpython-312.pyc 
│                │                       ├ [11]: usr/lib/python3.12/site-packages/pyparsing/tools/__pycache__/_
│                │                       │       _init__.cpython-312.pyc 
│                │                       ╰ [12]: usr/lib/python3.12/site-packages/pyparsing/tools/__pycache__/c
│                │                               vt_pyparsing_pep8_names.cpython-312.pyc 
│                ├ [61] ╭ ID            : py3-pip@25.1.1-r1 
│                │      ├ Name          : py3-pip 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/py3-pip@25.1.1-r1?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 91f6c6f092f4fc6f 
│                │      ├ Version       : 25.1.1-r1 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : py3-pip 
│                │      ├ SrcVersion    : 25.1.1-r1 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Achill Gilgenast <achill@achill.org> 
│                │      ├ DependsOn      ╭ [0]: py3-setuptools@80.9.0-r2 
│                │      │                ╰ [1]: python3@3.12.12-r0 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:c87fcc35bf409170cf455c4105b8b0cd44bf417c 
│                │      ╰ InstalledFiles ╭ [0]  : usr/bin/pip 
│                │                       ├ [1]  : usr/bin/pip3 
│                │                       ├ [2]  : usr/lib/python3.12/site-packages/pip/__init__.py 
│                │                       ├ [3]  : usr/lib/python3.12/site-packages/pip/__main__.py 
│                │                       ├ [4]  : usr/lib/python3.12/site-packages/pip/__pip-runner__.py 
│                │                       ├ [5]  : usr/lib/python3.12/site-packages/pip/py.typed 
│                │                       ├ [6]  : usr/lib/python3.12/site-packages/pip-25.1.1.dist-info/METADATA 
│                │                       ├ [7]  : usr/lib/python3.12/site-packages/pip-25.1.1.dist-info/RECORD 
│                │                       ├ [8]  : usr/lib/python3.12/site-packages/pip-25.1.1.dist-info/WHEEL 
│                │                       ├ [9]  : usr/lib/python3.12/site-packages/pip-25.1.1.dist-info/entry_p
│                │                       │        oints.txt 
│                │                       ├ [10] : usr/lib/python3.12/site-packages/pip-25.1.1.dist-info/top_lev
│                │                       │        el.txt 
│                │                       ├ [11] : usr/lib/python3.12/site-packages/pip-25.1.1.dist-info/license
│                │                       │        s/AUTHORS.txt 
│                │                       ├ [12] : usr/lib/python3.12/site-packages/pip-25.1.1.dist-info/license
│                │                       │        s/LICENSE.txt 
│                │                       ├ [13] : usr/lib/python3.12/site-packages/pip/_internal/__init__.py 
│                │                       ├ [14] : usr/lib/python3.12/site-packages/pip/_internal/build_env.py 
│                │                       ├ [15] : usr/lib/python3.12/site-packages/pip/_internal/cache.py 
│                │                       ├ [16] : usr/lib/python3.12/site-packages/pip/_internal/configuration.py 
│                │                       ├ [17] : usr/lib/python3.12/site-packages/pip/_internal/exceptions.py 
│                │                       ├ [18] : usr/lib/python3.12/site-packages/pip/_internal/main.py 
│                │                       ├ [19] : usr/lib/python3.12/site-packages/pip/_internal/pyproject.py 
│                │                       ├ [20] : usr/lib/python3.12/site-packages/pip/_internal/self_outdated_
│                │                       │        check.py 
│                │                       ├ [21] : usr/lib/python3.12/site-packages/pip/_internal/wheel_builder.py 
│                │                       ├ [22] : usr/lib/python3.12/site-packages/pip/_internal/cli/__init__.py 
│                │                       ├ [23] : usr/lib/python3.12/site-packages/pip/_internal/cli/autocomple
│                │                       │        tion.py 
│                │                       ├ [24] : usr/lib/python3.12/site-packages/pip/_internal/cli/base_comma
│                │                       │        nd.py 
│                │                       ├ [25] : usr/lib/python3.12/site-packages/pip/_internal/cli/cmdoptions
│                │                       │        .py 
│                │                       ├ [26] : usr/lib/python3.12/site-packages/pip/_internal/cli/command_co
│                │                       │        ntext.py 
│                │                       ├ [27] : usr/lib/python3.12/site-packages/pip/_internal/cli/index_comm
│                │                       │        and.py 
│                │                       ├ [28] : usr/lib/python3.12/site-packages/pip/_internal/cli/main.py 
│                │                       ├ [29] : usr/lib/python3.12/site-packages/pip/_internal/cli/main_parse
│                │                       │        r.py 
│                │                       ├ [30] : usr/lib/python3.12/site-packages/pip/_internal/cli/parser.py 
│                │                       ├ [31] : usr/lib/python3.12/site-packages/pip/_internal/cli/progress_b
│                │                       │        ars.py 
│                │                       ├ [32] : usr/lib/python3.12/site-packages/pip/_internal/cli/req_comman
│                │                       │        d.py 
│                │                       ├ [33] : usr/lib/python3.12/site-packages/pip/_internal/cli/spinners.py 
│                │                       ├ [34] : usr/lib/python3.12/site-packages/pip/_internal/cli/status_cod
│                │                       │        es.py 
│                │                       ├ [35] : usr/lib/python3.12/site-packages/pip/_internal/commands/__ini
│                │                       │        t__.py 
│                │                       ├ [36] : usr/lib/python3.12/site-packages/pip/_internal/commands/cache
│                │                       │        .py 
│                │                       ├ [37] : usr/lib/python3.12/site-packages/pip/_internal/commands/check
│                │                       │        .py 
│                │                       ├ [38] : usr/lib/python3.12/site-packages/pip/_internal/commands/compl
│                │                       │        etion.py 
│                │                       ├ [39] : usr/lib/python3.12/site-packages/pip/_internal/commands/confi
│                │                       │        guration.py 
│                │                       ├ [40] : usr/lib/python3.12/site-packages/pip/_internal/commands/debug
│                │                       │        .py 
│                │                       ├ [41] : usr/lib/python3.12/site-packages/pip/_internal/commands/downl
│                │                       │        oad.py 
│                │                       ├ [42] : usr/lib/python3.12/site-packages/pip/_internal/commands/freez
│                │                       │        e.py 
│                │                       ├ [43] : usr/lib/python3.12/site-packages/pip/_internal/commands/hash.py 
│                │                       ├ [44] : usr/lib/python3.12/site-packages/pip/_internal/commands/help.py 
│                │                       ├ [45] : usr/lib/python3.12/site-packages/pip/_internal/commands/index
│                │                       │        .py 
│                │                       ├ [46] : usr/lib/python3.12/site-packages/pip/_internal/commands/inspe
│                │                       │        ct.py 
│                │                       ├ [47] : usr/lib/python3.12/site-packages/pip/_internal/commands/insta
│                │                       │        ll.py 
│                │                       ├ [48] : usr/lib/python3.12/site-packages/pip/_internal/commands/list.py 
│                │                       ├ [49] : usr/lib/python3.12/site-packages/pip/_internal/commands/lock.py 
│                │                       ├ [50] : usr/lib/python3.12/site-packages/pip/_internal/commands/searc
│                │                       │        h.py 
│                │                       ├ [51] : usr/lib/python3.12/site-packages/pip/_internal/commands/show.py 
│                │                       ├ [52] : usr/lib/python3.12/site-packages/pip/_internal/commands/unins
│                │                       │        tall.py 
│                │                       ├ [53] : usr/lib/python3.12/site-packages/pip/_internal/commands/wheel
│                │                       │        .py 
│                │                       ├ [54] : usr/lib/python3.12/site-packages/pip/_internal/distributions/
│                │                       │        __init__.py 
│                │                       ├ [55] : usr/lib/python3.12/site-packages/pip/_internal/distributions/
│                │                       │        base.py 
│                │                       ├ [56] : usr/lib/python3.12/site-packages/pip/_internal/distributions/
│                │                       │        installed.py 
│                │                       ├ [57] : usr/lib/python3.12/site-packages/pip/_internal/distributions/
│                │                       │        sdist.py 
│                │                       ├ [58] : usr/lib/python3.12/site-packages/pip/_internal/distributions/
│                │                       │        wheel.py 
│                │                       ├ [59] : usr/lib/python3.12/site-packages/pip/_internal/index/__init__
│                │                       │        .py 
│                │                       ├ [60] : usr/lib/python3.12/site-packages/pip/_internal/index/collecto
│                │                       │        r.py 
│                │                       ├ [61] : usr/lib/python3.12/site-packages/pip/_internal/index/package_
│                │                       │        finder.py 
│                │                       ├ [62] : usr/lib/python3.12/site-packages/pip/_internal/index/sources.py 
│                │                       ├ [63] : usr/lib/python3.12/site-packages/pip/_internal/locations/__in
│                │                       │        it__.py 
│                │                       ├ [64] : usr/lib/python3.12/site-packages/pip/_internal/locations/_dis
│                │                       │        tutils.py 
│                │                       ├ [65] : usr/lib/python3.12/site-packages/pip/_internal/locations/_sys
│                │                       │        config.py 
│                │                       ├ [66] : usr/lib/python3.12/site-packages/pip/_internal/locations/base
│                │                       │        .py 
│                │                       ├ [67] : usr/lib/python3.12/site-packages/pip/_internal/metadata/__ini
│                │                       │        t__.py 
│                │                       ├ [68] : usr/lib/python3.12/site-packages/pip/_internal/metadata/_json
│                │                       │        .py 
│                │                       ├ [69] : usr/lib/python3.12/site-packages/pip/_internal/metadata/base.py 
│                │                       ├ [70] : usr/lib/python3.12/site-packages/pip/_internal/metadata/pkg_r
│                │                       │        esources.py 
│                │                       ├ [71] : usr/lib/python3.12/site-packages/pip/_internal/metadata/impor
│                │                       │        tlib/__init__.py 
│                │                       ├ [72] : usr/lib/python3.12/site-packages/pip/_internal/metadata/impor
│                │                       │        tlib/_compat.py 
│                │                       ├ [73] : usr/lib/python3.12/site-packages/pip/_internal/metadata/impor
│                │                       │        tlib/_dists.py 
│                │                       ├ [74] : usr/lib/python3.12/site-packages/pip/_internal/metadata/impor
│                │                       │        tlib/_envs.py 
│                │                       ├ [75] : usr/lib/python3.12/site-packages/pip/_internal/models/__init_
│                │                       │        _.py 
│                │                       ├ [76] : usr/lib/python3.12/site-packages/pip/_internal/models/candida
│                │                       │        te.py 
│                │                       ├ [77] : usr/lib/python3.12/site-packages/pip/_internal/models/direct_
│                │                       │        url.py 
│                │                       ├ [78] : usr/lib/python3.12/site-packages/pip/_internal/models/format_
│                │                       │        control.py 
│                │                       ├ [79] : usr/lib/python3.12/site-packages/pip/_internal/models/index.py 
│                │                       ├ [80] : usr/lib/python3.12/site-packages/pip/_internal/models/install
│                │                       │        ation_report.py 
│                │                       ├ [81] : usr/lib/python3.12/site-packages/pip/_internal/models/link.py 
│                │                       ├ [82] : usr/lib/python3.12/site-packages/pip/_internal/models/pylock.py 
│                │                       ├ [83] : usr/lib/python3.12/site-packages/pip/_internal/models/scheme.py 
│                │                       ├ [84] : usr/lib/python3.12/site-packages/pip/_internal/models/search_
│                │                       │        scope.py 
│                │                       ├ [85] : usr/lib/python3.12/site-packages/pip/_internal/models/selecti
│                │                       │        on_prefs.py 
│                │                       ├ [86] : usr/lib/python3.12/site-packages/pip/_internal/models/target_
│                │                       │        python.py 
│                │                       ├ [87] : usr/lib/python3.12/site-packages/pip/_internal/models/wheel.py 
│                │                       ├ [88] : usr/lib/python3.12/site-packages/pip/_internal/network/__init
│                │                       │        __.py 
│                │                       ├ [89] : usr/lib/python3.12/site-packages/pip/_internal/network/auth.py 
│                │                       ├ [90] : usr/lib/python3.12/site-packages/pip/_internal/network/cache.py 
│                │                       ├ [91] : usr/lib/python3.12/site-packages/pip/_internal/network/downlo
│                │                       │        ad.py 
│                │                       ├ [92] : usr/lib/python3.12/site-packages/pip/_internal/network/lazy_w
│                │                       │        heel.py 
│                │                       ├ [93] : usr/lib/python3.12/site-packages/pip/_internal/network/sessio
│                │                       │        n.py 
│                │                       ├ [94] : usr/lib/python3.12/site-packages/pip/_internal/network/utils.py 
│                │                       ├ [95] : usr/lib/python3.12/site-packages/pip/_internal/network/xmlrpc
│                │                       │        .py 
│                │                       ├ [96] : usr/lib/python3.12/site-packages/pip/_internal/operations/__i
│                │                       │        nit__.py 
│                │                       ├ [97] : usr/lib/python3.12/site-packages/pip/_internal/operations/che
│                │                       │        ck.py 
│                │                       ├ [98] : usr/lib/python3.12/site-packages/pip/_internal/operations/fre
│                │                       │        eze.py 
│                │                       ├ [99] : usr/lib/python3.12/site-packages/pip/_internal/operations/pre
│                │                       │        pare.py 
│                │                       ├ [100]: usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/__init__.py 
│                │                       ├ [101]: usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/build_tracker.py 
│                │                       ├ [102]: usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/metadata.py 
│                │                       ├ [103]: usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/metadata_editable.py 
│                │                       ├ [104]: usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/metadata_legacy.py 
│                │                       ├ [105]: usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/wheel.py 
│                │                       ├ [106]: usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/wheel_editable.py 
│                │                       ├ [107]: usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/wheel_legacy.py 
│                │                       ├ [108]: usr/lib/python3.12/site-packages/pip/_internal/operations/ins
│                │                       │        tall/__init__.py 
│                │                       ├ [109]: usr/lib/python3.12/site-packages/pip/_internal/operations/ins
│                │                       │        tall/editable_legacy.py 
│                │                       ├ [110]: usr/lib/python3.12/site-packages/pip/_internal/operations/ins
│                │                       │        tall/wheel.py 
│                │                       ├ [111]: usr/lib/python3.12/site-packages/pip/_internal/req/__init__.py 
│                │                       ├ [112]: usr/lib/python3.12/site-packages/pip/_internal/req/constructo
│                │                       │        rs.py 
│                │                       ├ [113]: usr/lib/python3.12/site-packages/pip/_internal/req/req_depend
│                │                       │        ency_group.py 
│                │                       ├ [114]: usr/lib/python3.12/site-packages/pip/_internal/req/req_file.py 
│                │                       ├ [115]: usr/lib/python3.12/site-packages/pip/_internal/req/req_instal
│                │                       │        l.py 
│                │                       ├ [116]: usr/lib/python3.12/site-packages/pip/_internal/req/req_set.py 
│                │                       ├ [117]: usr/lib/python3.12/site-packages/pip/_internal/req/req_uninst
│                │                       │        all.py 
│                │                       ├ [118]: usr/lib/python3.12/site-packages/pip/_internal/resolution/__i
│                │                       │        nit__.py 
│                │                       ├ [119]: usr/lib/python3.12/site-packages/pip/_internal/resolution/bas
│                │                       │        e.py 
│                │                       ├ [120]: usr/lib/python3.12/site-packages/pip/_internal/resolution/leg
│                │                       │        acy/__init__.py 
│                │                       ├ [121]: usr/lib/python3.12/site-packages/pip/_internal/resolution/leg
│                │                       │        acy/resolver.py 
│                │                       ├ [122]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/__init__.py 
│                │                       ├ [123]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/base.py 
│                │                       ├ [124]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/candidates.py 
│                │                       ├ [125]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/factory.py 
│                │                       ├ [126]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/found_candidates.py 
│                │                       ├ [127]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/provider.py 
│                │                       ├ [128]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/reporter.py 
│                │                       ├ [129]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/requirements.py 
│                │                       ├ [130]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/resolver.py 
│                │                       ├ [131]: usr/lib/python3.12/site-packages/pip/_internal/utils/__init__
│                │                       │        .py 
│                │                       ├ [132]: usr/lib/python3.12/site-packages/pip/_internal/utils/_jaraco_
│                │                       │        text.py 
│                │                       ├ [133]: usr/lib/python3.12/site-packages/pip/_internal/utils/_log.py 
│                │                       ├ [134]: usr/lib/python3.12/site-packages/pip/_internal/utils/appdirs.py 
│                │                       ├ [135]: usr/lib/python3.12/site-packages/pip/_internal/utils/compat.py 
│                │                       ├ [136]: usr/lib/python3.12/site-packages/pip/_internal/utils/compatib
│                │                       │        ility_tags.py 
│                │                       ├ [137]: usr/lib/python3.12/site-packages/pip/_internal/utils/datetime
│                │                       │        .py 
│                │                       ├ [138]: usr/lib/python3.12/site-packages/pip/_internal/utils/deprecat
│                │                       │        ion.py 
│                │                       ├ [139]: usr/lib/python3.12/site-packages/pip/_internal/utils/direct_u
│                │                       │        rl_helpers.py 
│                │                       ├ [140]: usr/lib/python3.12/site-packages/pip/_internal/utils/egg_link
│                │                       │        .py 
│                │                       ├ [141]: usr/lib/python3.12/site-packages/pip/_internal/utils/entrypoi
│                │                       │        nts.py 
│                │                       ├ [142]: usr/lib/python3.12/site-packages/pip/_internal/utils/filesyst
│                │                       │        em.py 
│                │                       ├ [143]: usr/lib/python3.12/site-packages/pip/_internal/utils/filetype
│                │                       │        s.py 
│                │                       ├ [144]: usr/lib/python3.12/site-packages/pip/_internal/utils/glibc.py 
│                │                       ├ [145]: usr/lib/python3.12/site-packages/pip/_internal/utils/hashes.py 
│                │                       ├ [146]: usr/lib/python3.12/site-packages/pip/_internal/utils/logging.py 
│                │                       ├ [147]: usr/lib/python3.12/site-packages/pip/_internal/utils/misc.py 
│                │                       ├ [148]: usr/lib/python3.12/site-packages/pip/_internal/utils/packagin
│                │                       │        g.py 
│                │                       ├ [149]: usr/lib/python3.12/site-packages/pip/_internal/utils/retry.py 
│                │                       ├ [150]: usr/lib/python3.12/site-packages/pip/_internal/utils/setuptoo
│                │                       │        ls_build.py 
│                │                       ├ [151]: usr/lib/python3.12/site-packages/pip/_internal/utils/subproce
│                │                       │        ss.py 
│                │                       ├ [152]: usr/lib/python3.12/site-packages/pip/_internal/utils/temp_dir
│                │                       │        .py 
│                │                       ├ [153]: usr/lib/python3.12/site-packages/pip/_internal/utils/unpackin
│                │                       │        g.py 
│                │                       ├ [154]: usr/lib/python3.12/site-packages/pip/_internal/utils/urls.py 
│                │                       ├ [155]: usr/lib/python3.12/site-packages/pip/_internal/utils/virtuale
│                │                       │        nv.py 
│                │                       ├ [156]: usr/lib/python3.12/site-packages/pip/_internal/utils/wheel.py 
│                │                       ├ [157]: usr/lib/python3.12/site-packages/pip/_internal/vcs/__init__.py 
│                │                       ├ [158]: usr/lib/python3.12/site-packages/pip/_internal/vcs/bazaar.py 
│                │                       ├ [159]: usr/lib/python3.12/site-packages/pip/_internal/vcs/git.py 
│                │                       ├ [160]: usr/lib/python3.12/site-packages/pip/_internal/vcs/mercurial.py 
│                │                       ├ [161]: usr/lib/python3.12/site-packages/pip/_internal/vcs/subversion
│                │                       │        .py 
│                │                       ├ [162]: usr/lib/python3.12/site-packages/pip/_internal/vcs/versioncon
│                │                       │        trol.py 
│                │                       ├ [163]: usr/lib/python3.12/site-packages/pip/_vendor/__init__.py 
│                │                       ├ [164]: usr/lib/python3.12/site-packages/pip/_vendor/distlib.pyi 
│                │                       ├ [165]: usr/lib/python3.12/site-packages/pip/_vendor/msgpack.pyi 
│                │                       ├ [166]: usr/lib/python3.12/site-packages/pip/_vendor/pkg_resources.pyi 
│                │                       ├ [167]: usr/lib/python3.12/site-packages/pip/_vendor/pygments.pyi 
│                │                       ├ [168]: usr/lib/python3.12/site-packages/pip/_vendor/requests.pyi 
│                │                       ├ [169]: usr/lib/python3.12/site-packages/pip/_vendor/typing_extension
│                │                       │        s.py 
│                │                       ├ [170]: usr/lib/python3.12/site-packages/pip/_vendor/typing_extension
│                │                       │        s.pyi 
│                │                       ├ [171]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3.pyi 
│                │                       ├ [172]: usr/lib/python3.12/site-packages/pip/_vendor/vendor.txt 
│                │                       ├ [173]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/__i
│                │                       │        nit__.py 
│                │                       ├ [174]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/_cm
│                │                       │        d.py 
│                │                       ├ [175]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/ada
│                │                       │        pter.py 
│                │                       ├ [176]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/cac
│                │                       │        he.py 
│                │                       ├ [177]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/con
│                │                       │        troller.py 
│                │                       ├ [178]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/fil
│                │                       │        ewrapper.py 
│                │                       ├ [179]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/heu
│                │                       │        ristics.py 
│                │                       ├ [180]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/py.
│                │                       │        typed 
│                │                       ├ [181]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/ser
│                │                       │        ialize.py 
│                │                       ├ [182]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/wra
│                │                       │        pper.py 
│                │                       ├ [183]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/cac
│                │                       │        hes/__init__.py 
│                │                       ├ [184]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/cac
│                │                       │        hes/file_cache.py 
│                │                       ├ [185]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/cac
│                │                       │        hes/redis_cache.py 
│                │                       ├ [186]: usr/lib/python3.12/site-packages/pip/_vendor/certifi/__init__
│                │                       │        .py 
│                │                       ├ [187]: usr/lib/python3.12/site-packages/pip/_vendor/certifi/__main__
│                │                       │        .py 
│                │                       ├ [188]: usr/lib/python3.12/site-packages/pip/_vendor/certifi/cacert.pem 
│                │                       ├ [189]: usr/lib/python3.12/site-packages/pip/_vendor/certifi/core.py 
│                │                       ├ [190]: usr/lib/python3.12/site-packages/pip/_vendor/certifi/py.typed 
│                │                       ├ [191]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/__init__.py 
│                │                       ├ [192]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/__main__.py 
│                │                       ├ [193]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/_implementation.py 
│                │                       ├ [194]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/_lint_dependency_groups.py 
│                │                       ├ [195]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/_pip_wrapper.py 
│                │                       ├ [196]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/_toml_compat.py 
│                │                       ├ [197]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/py.typed 
│                │                       ├ [198]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__init__
│                │                       │        .py 
│                │                       ├ [199]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/compat.py 
│                │                       ├ [200]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/database
│                │                       │        .py 
│                │                       ├ [201]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/index.py 
│                │                       ├ [202]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/locators
│                │                       │        .py 
│                │                       ├ [203]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/manifest
│                │                       │        .py 
│                │                       ├ [204]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/markers.py 
│                │                       ├ [205]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/metadata
│                │                       │        .py 
│                │                       ├ [206]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/resource
│                │                       │        s.py 
│                │                       ├ [207]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/scripts.py 
│                │                       ├ [208]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/t32.exe 
│                │                       ├ [209]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/t64-arm.
│                │                       │        exe 
│                │                       ├ [210]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/t64.exe 
│                │                       ├ [211]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/util.py 
│                │                       ├ [212]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/version.py 
│                │                       ├ [213]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/w32.exe 
│                │                       ├ [214]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/w64-arm.
│                │                       │        exe 
│                │                       ├ [215]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/w64.exe 
│                │                       ├ [216]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/wheel.py 
│                │                       ├ [217]: usr/lib/python3.12/site-packages/pip/_vendor/distro/__init__.py 
│                │                       ├ [218]: usr/lib/python3.12/site-packages/pip/_vendor/distro/__main__.py 
│                │                       ├ [219]: usr/lib/python3.12/site-packages/pip/_vendor/distro/distro.py 
│                │                       ├ [220]: usr/lib/python3.12/site-packages/pip/_vendor/distro/py.typed 
│                │                       ├ [221]: usr/lib/python3.12/site-packages/pip/_vendor/idna/__init__.py 
│                │                       ├ [222]: usr/lib/python3.12/site-packages/pip/_vendor/idna/codec.py 
│                │                       ├ [223]: usr/lib/python3.12/site-packages/pip/_vendor/idna/compat.py 
│                │                       ├ [224]: usr/lib/python3.12/site-packages/pip/_vendor/idna/core.py 
│                │                       ├ [225]: usr/lib/python3.12/site-packages/pip/_vendor/idna/idnadata.py 
│                │                       ├ [226]: usr/lib/python3.12/site-packages/pip/_vendor/idna/intranges.py 
│                │                       ├ [227]: usr/lib/python3.12/site-packages/pip/_vendor/idna/package_dat
│                │                       │        a.py 
│                │                       ├ [228]: usr/lib/python3.12/site-packages/pip/_vendor/idna/py.typed 
│                │                       ├ [229]: usr/lib/python3.12/site-packages/pip/_vendor/idna/uts46data.py 
│                │                       ├ [230]: usr/lib/python3.12/site-packages/pip/_vendor/msgpack/__init__
│                │                       │        .py 
│                │                       ├ [231]: usr/lib/python3.12/site-packages/pip/_vendor/msgpack/exceptio
│                │                       │        ns.py 
│                │                       ├ [232]: usr/lib/python3.12/site-packages/pip/_vendor/msgpack/ext.py 
│                │                       ├ [233]: usr/lib/python3.12/site-packages/pip/_vendor/msgpack/fallback
│                │                       │        .py 
│                │                       ├ [234]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__init
│                │                       │        __.py 
│                │                       ├ [235]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/_elffi
│                │                       │        le.py 
│                │                       ├ [236]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/_manyl
│                │                       │        inux.py 
│                │                       ├ [237]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/_musll
│                │                       │        inux.py 
│                │                       ├ [238]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/_parse
│                │                       │        r.py 
│                │                       ├ [239]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/_struc
│                │                       │        tures.py 
│                │                       ├ [240]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/_token
│                │                       │        izer.py 
│                │                       ├ [241]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/marker
│                │                       │        s.py 
│                │                       ├ [242]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/metada
│                │                       │        ta.py 
│                │                       ├ [243]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/py.typed 
│                │                       ├ [244]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/requir
│                │                       │        ements.py 
│                │                       ├ [245]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/specif
│                │                       │        iers.py 
│                │                       ├ [246]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/tags.py 
│                │                       ├ [247]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/utils.py 
│                │                       ├ [248]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/versio
│                │                       │        n.py 
│                │                       ├ [249]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/licens
│                │                       │        es/__init__.py 
│                │                       ├ [250]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/licens
│                │                       │        es/_spdx.py 
│                │                       ├ [251]: usr/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__
│                │                       │        init__.py 
│                │                       ├ [252]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/__i
│                │                       │        nit__.py 
│                │                       ├ [253]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/__m
│                │                       │        ain__.py 
│                │                       ├ [254]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/and
│                │                       │        roid.py 
│                │                       ├ [255]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/api
│                │                       │        .py 
│                │                       ├ [256]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/mac
│                │                       │        os.py 
│                │                       ├ [257]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/py.
│                │                       │        typed 
│                │                       ├ [258]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/uni
│                │                       │        x.py 
│                │                       ├ [259]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/ver
│                │                       │        sion.py 
│                │                       ├ [260]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/win
│                │                       │        dows.py 
│                │                       ├ [261]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__init_
│                │                       │        _.py 
│                │                       ├ [262]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__main_
│                │                       │        _.py 
│                │                       ├ [263]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/console
│                │                       │        .py 
│                │                       ├ [264]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/filter.py 
│                │                       ├ [265]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/formatt
│                │                       │        er.py 
│                │                       ├ [266]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/lexer.py 
│                │                       ├ [267]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/modelin
│                │                       │        e.py 
│                │                       ├ [268]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/plugin.py 
│                │                       ├ [269]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/regexop
│                │                       │        t.py 
│                │                       ├ [270]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/scanner
│                │                       │        .py 
│                │                       ├ [271]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/sphinxe
│                │                       │        xt.py 
│                │                       ├ [272]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/style.py 
│                │                       ├ [273]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/token.py 
│                │                       ├ [274]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/unistri
│                │                       │        ng.py 
│                │                       ├ [275]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/util.py 
│                │                       ├ [276]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/filters
│                │                       │        /__init__.py 
│                │                       ├ [277]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/formatt
│                │                       │        ers/__init__.py 
│                │                       ├ [278]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/formatt
│                │                       │        ers/_mapping.py 
│                │                       ├ [279]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/lexers/
│                │                       │        __init__.py 
│                │                       ├ [280]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/lexers/
│                │                       │        _mapping.py 
│                │                       ├ [281]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/lexers/
│                │                       │        python.py 
│                │                       ├ [282]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/styles/
│                │                       │        __init__.py 
│                │                       ├ [283]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/styles/
│                │                       │        _mapping.py 
│                │                       ├ [284]: usr/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/
│                │                       │        __init__.py 
│                │                       ├ [285]: usr/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/
│                │                       │        _impl.py 
│                │                       ├ [286]: usr/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/
│                │                       │        py.typed 
│                │                       ├ [287]: usr/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/
│                │                       │        _in_process/__init__.py 
│                │                       ├ [288]: usr/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/
│                │                       │        _in_process/_in_process.py 
│                │                       ├ [289]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__init_
│                │                       │        _.py 
│                │                       ├ [290]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__versi
│                │                       │        on__.py 
│                │                       ├ [291]: usr/lib/python3.12/site-packages/pip/_vendor/requests/_intern
│                │                       │        al_utils.py 
│                │                       ├ [292]: usr/lib/python3.12/site-packages/pip/_vendor/requests/adapter
│                │                       │        s.py 
│                │                       ├ [293]: usr/lib/python3.12/site-packages/pip/_vendor/requests/api.py 
│                │                       ├ [294]: usr/lib/python3.12/site-packages/pip/_vendor/requests/auth.py 
│                │                       ├ [295]: usr/lib/python3.12/site-packages/pip/_vendor/requests/certs.py 
│                │                       ├ [296]: usr/lib/python3.12/site-packages/pip/_vendor/requests/compat.py 
│                │                       ├ [297]: usr/lib/python3.12/site-packages/pip/_vendor/requests/cookies
│                │                       │        .py 
│                │                       ├ [298]: usr/lib/python3.12/site-packages/pip/_vendor/requests/excepti
│                │                       │        ons.py 
│                │                       ├ [299]: usr/lib/python3.12/site-packages/pip/_vendor/requests/help.py 
│                │                       ├ [300]: usr/lib/python3.12/site-packages/pip/_vendor/requests/hooks.py 
│                │                       ├ [301]: usr/lib/python3.12/site-packages/pip/_vendor/requests/models.py 
│                │                       ├ [302]: usr/lib/python3.12/site-packages/pip/_vendor/requests/package
│                │                       │        s.py 
│                │                       ├ [303]: usr/lib/python3.12/site-packages/pip/_vendor/requests/session
│                │                       │        s.py 
│                │                       ├ [304]: usr/lib/python3.12/site-packages/pip/_vendor/requests/status_
│                │                       │        codes.py 
│                │                       ├ [305]: usr/lib/python3.12/site-packages/pip/_vendor/requests/structu
│                │                       │        res.py 
│                │                       ├ [306]: usr/lib/python3.12/site-packages/pip/_vendor/requests/utils.py 
│                │                       ├ [307]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/__ini
│                │                       │        t__.py 
│                │                       ├ [308]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/provi
│                │                       │        ders.py 
│                │                       ├ [309]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/py.ty
│                │                       │        ped 
│                │                       ├ [310]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/repor
│                │                       │        ters.py 
│                │                       ├ [311]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/struc
│                │                       │        ts.py 
│                │                       ├ [312]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/resol
│                │                       │        vers/__init__.py 
│                │                       ├ [313]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/resol
│                │                       │        vers/abstract.py 
│                │                       ├ [314]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/resol
│                │                       │        vers/criterion.py 
│                │                       ├ [315]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/resol
│                │                       │        vers/exceptions.py 
│                │                       ├ [316]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/resol
│                │                       │        vers/resolution.py 
│                │                       ├ [317]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__init__.py 
│                │                       ├ [318]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__main__.py 
│                │                       ├ [319]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_cell_width
│                │                       │        s.py 
│                │                       ├ [320]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_emoji_code
│                │                       │        s.py 
│                │                       ├ [321]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_emoji_repl
│                │                       │        ace.py 
│                │                       ├ [322]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_export_for
│                │                       │        mat.py 
│                │                       ├ [323]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_extension.py 
│                │                       ├ [324]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_fileno.py 
│                │                       ├ [325]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_inspect.py 
│                │                       ├ [326]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_log_render
│                │                       │        .py 
│                │                       ├ [327]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_loop.py 
│                │                       ├ [328]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_null_file.py 
│                │                       ├ [329]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_palettes.py 
│                │                       ├ [330]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_pick.py 
│                │                       ├ [331]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_ratio.py 
│                │                       ├ [332]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_spinners.py 
│                │                       ├ [333]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_stack.py 
│                │                       ├ [334]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_timer.py 
│                │                       ├ [335]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_win32_cons
│                │                       │        ole.py 
│                │                       ├ [336]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_windows.py 
│                │                       ├ [337]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_windows_re
│                │                       │        nderer.py 
│                │                       ├ [338]: usr/lib/python3.12/site-packages/pip/_vendor/rich/_wrap.py 
│                │                       ├ [339]: usr/lib/python3.12/site-packages/pip/_vendor/rich/abc.py 
│                │                       ├ [340]: usr/lib/python3.12/site-packages/pip/_vendor/rich/align.py 
│                │                       ├ [341]: usr/lib/python3.12/site-packages/pip/_vendor/rich/ansi.py 
│                │                       ├ [342]: usr/lib/python3.12/site-packages/pip/_vendor/rich/bar.py 
│                │                       ├ [343]: usr/lib/python3.12/site-packages/pip/_vendor/rich/box.py 
│                │                       ├ [344]: usr/lib/python3.12/site-packages/pip/_vendor/rich/cells.py 
│                │                       ├ [345]: usr/lib/python3.12/site-packages/pip/_vendor/rich/color.py 
│                │                       ├ [346]: usr/lib/python3.12/site-packages/pip/_vendor/rich/color_tripl
│                │                       │        et.py 
│                │                       ├ [347]: usr/lib/python3.12/site-packages/pip/_vendor/rich/columns.py 
│                │                       ├ [348]: usr/lib/python3.12/site-packages/pip/_vendor/rich/console.py 
│                │                       ├ [349]: usr/lib/python3.12/site-packages/pip/_vendor/rich/constrain.py 
│                │                       ├ [350]: usr/lib/python3.12/site-packages/pip/_vendor/rich/containers.py 
│                │                       ├ [351]: usr/lib/python3.12/site-packages/pip/_vendor/rich/control.py 
│                │                       ├ [352]: usr/lib/python3.12/site-packages/pip/_vendor/rich/default_sty
│                │                       │        les.py 
│                │                       ├ [353]: usr/lib/python3.12/site-packages/pip/_vendor/rich/diagnose.py 
│                │                       ├ [354]: usr/lib/python3.12/site-packages/pip/_vendor/rich/emoji.py 
│                │                       ├ [355]: usr/lib/python3.12/site-packages/pip/_vendor/rich/errors.py 
│                │                       ├ [356]: usr/lib/python3.12/site-packages/pip/_vendor/rich/file_proxy.py 
│                │                       ├ [357]: usr/lib/python3.12/site-packages/pip/_vendor/rich/filesize.py 
│                │                       ├ [358]: usr/lib/python3.12/site-packages/pip/_vendor/rich/highlighter
│                │                       │        .py 
│                │                       ├ [359]: usr/lib/python3.12/site-packages/pip/_vendor/rich/json.py 
│                │                       ├ [360]: usr/lib/python3.12/site-packages/pip/_vendor/rich/jupyter.py 
│                │                       ├ [361]: usr/lib/python3.12/site-packages/pip/_vendor/rich/layout.py 
│                │                       ├ [362]: usr/lib/python3.12/site-packages/pip/_vendor/rich/live.py 
│                │                       ├ [363]: usr/lib/python3.12/site-packages/pip/_vendor/rich/live_render
│                │                       │        .py 
│                │                       ├ [364]: usr/lib/python3.12/site-packages/pip/_vendor/rich/logging.py 
│                │                       ├ [365]: usr/lib/python3.12/site-packages/pip/_vendor/rich/markup.py 
│                │                       ├ [366]: usr/lib/python3.12/site-packages/pip/_vendor/rich/measure.py 
│                │                       ├ [367]: usr/lib/python3.12/site-packages/pip/_vendor/rich/padding.py 
│                │                       ├ [368]: usr/lib/python3.12/site-packages/pip/_vendor/rich/pager.py 
│                │                       ├ [369]: usr/lib/python3.12/site-packages/pip/_vendor/rich/palette.py 
│                │                       ├ [370]: usr/lib/python3.12/site-packages/pip/_vendor/rich/panel.py 
│                │                       ├ [371]: usr/lib/python3.12/site-packages/pip/_vendor/rich/pretty.py 
│                │                       ├ [372]: usr/lib/python3.12/site-packages/pip/_vendor/rich/progress.py 
│                │                       ├ [373]: usr/lib/python3.12/site-packages/pip/_vendor/rich/progress_ba
│                │                       │        r.py 
│                │                       ├ [374]: usr/lib/python3.12/site-packages/pip/_vendor/rich/prompt.py 
│                │                       ├ [375]: usr/lib/python3.12/site-packages/pip/_vendor/rich/protocol.py 
│                │                       ├ [376]: usr/lib/python3.12/site-packages/pip/_vendor/rich/py.typed 
│                │                       ├ [377]: usr/lib/python3.12/site-packages/pip/_vendor/rich/region.py 
│                │                       ├ [378]: usr/lib/python3.12/site-packages/pip/_vendor/rich/repr.py 
│                │                       ├ [379]: usr/lib/python3.12/site-packages/pip/_vendor/rich/rule.py 
│                │                       ├ [380]: usr/lib/python3.12/site-packages/pip/_vendor/rich/scope.py 
│                │                       ├ [381]: usr/lib/python3.12/site-packages/pip/_vendor/rich/screen.py 
│                │                       ├ [382]: usr/lib/python3.12/site-packages/pip/_vendor/rich/segment.py 
│                │                       ├ [383]: usr/lib/python3.12/site-packages/pip/_vendor/rich/spinner.py 
│                │                       ├ [384]: usr/lib/python3.12/site-packages/pip/_vendor/rich/status.py 
│                │                       ├ [385]: usr/lib/python3.12/site-packages/pip/_vendor/rich/style.py 
│                │                       ├ [386]: usr/lib/python3.12/site-packages/pip/_vendor/rich/styled.py 
│                │                       ├ [387]: usr/lib/python3.12/site-packages/pip/_vendor/rich/syntax.py 
│                │                       ├ [388]: usr/lib/python3.12/site-packages/pip/_vendor/rich/table.py 
│                │                       ├ [389]: usr/lib/python3.12/site-packages/pip/_vendor/rich/terminal_th
│                │                       │        eme.py 
│                │                       ├ [390]: usr/lib/python3.12/site-packages/pip/_vendor/rich/text.py 
│                │                       ├ [391]: usr/lib/python3.12/site-packages/pip/_vendor/rich/theme.py 
│                │                       ├ [392]: usr/lib/python3.12/site-packages/pip/_vendor/rich/themes.py 
│                │                       ├ [393]: usr/lib/python3.12/site-packages/pip/_vendor/rich/traceback.py 
│                │                       ├ [394]: usr/lib/python3.12/site-packages/pip/_vendor/rich/tree.py 
│                │                       ├ [395]: usr/lib/python3.12/site-packages/pip/_vendor/tomli/__init__.py 
│                │                       ├ [396]: usr/lib/python3.12/site-packages/pip/_vendor/tomli/_parser.py 
│                │                       ├ [397]: usr/lib/python3.12/site-packages/pip/_vendor/tomli/_re.py 
│                │                       ├ [398]: usr/lib/python3.12/site-packages/pip/_vendor/tomli/_types.py 
│                │                       ├ [399]: usr/lib/python3.12/site-packages/pip/_vendor/tomli/py.typed 
│                │                       ├ [400]: usr/lib/python3.12/site-packages/pip/_vendor/tomli_w/__init__
│                │                       │        .py 
│                │                       ├ [401]: usr/lib/python3.12/site-packages/pip/_vendor/tomli_w/_writer.py 
│                │                       ├ [402]: usr/lib/python3.12/site-packages/pip/_vendor/tomli_w/py.typed 
│                │                       ├ [403]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/__ini
│                │                       │        t__.py 
│                │                       ├ [404]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/_api.py 
│                │                       ├ [405]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/_maco
│                │                       │        s.py 
│                │                       ├ [406]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/_open
│                │                       │        ssl.py 
│                │                       ├ [407]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/_ssl_
│                │                       │        constants.py 
│                │                       ├ [408]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/_wind
│                │                       │        ows.py 
│                │                       ├ [409]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/py.ty
│                │                       │        ped 
│                │                       ├ [410]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/__init__
│                │                       │        .py 
│                │                       ├ [411]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/_collect
│                │                       │        ions.py 
│                │                       ├ [412]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/_version
│                │                       │        .py 
│                │                       ├ [413]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/connecti
│                │                       │        on.py 
│                │                       ├ [414]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/connecti
│                │                       │        onpool.py 
│                │                       ├ [415]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/exceptio
│                │                       │        ns.py 
│                │                       ├ [416]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/fields.py 
│                │                       ├ [417]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/filepost
│                │                       │        .py 
│                │                       ├ [418]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/poolmana
│                │                       │        ger.py 
│                │                       ├ [419]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/request.py 
│                │                       ├ [420]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/response
│                │                       │        .py 
│                │                       ├ [421]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        __init__.py 
│                │                       ├ [422]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        _appengine_environ.py 
│                │                       ├ [423]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        appengine.py 
│                │                       ├ [424]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        ntlmpool.py 
│                │                       ├ [425]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        pyopenssl.py 
│                │                       ├ [426]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        securetransport.py 
│                │                       ├ [427]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        socks.py 
│                │                       ├ [428]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        _securetransport/__init__.py 
│                │                       ├ [429]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        _securetransport/bindings.py 
│                │                       ├ [430]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        _securetransport/low_level.py 
│                │                       ├ [431]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/packages
│                │                       │        /__init__.py 
│                │                       ├ [432]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/packages
│                │                       │        /six.py 
│                │                       ├ [433]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/packages
│                │                       │        /backports/__init__.py 
│                │                       ├ [434]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/packages
│                │                       │        /backports/makefile.py 
│                │                       ├ [435]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/packages
│                │                       │        /backports/weakref_finalize.py 
│                │                       ├ [436]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__i
│                │                       │        nit__.py 
│                │                       ├ [437]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/con
│                │                       │        nection.py 
│                │                       ├ [438]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/pro
│                │                       │        xy.py 
│                │                       ├ [439]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/que
│                │                       │        ue.py 
│                │                       ├ [440]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/req
│                │                       │        uest.py 
│                │                       ├ [441]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/res
│                │                       │        ponse.py 
│                │                       ├ [442]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/ret
│                │                       │        ry.py 
│                │                       ├ [443]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/ssl
│                │                       │        _.py 
│                │                       ├ [444]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/ssl
│                │                       │        _match_hostname.py 
│                │                       ├ [445]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/ssl
│                │                       │        transport.py 
│                │                       ├ [446]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/tim
│                │                       │        eout.py 
│                │                       ├ [447]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/url
│                │                       │        .py 
│                │                       ╰ [448]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/wai
│                │                                t.py 
│                ├ [62] ╭ ID            : py3-pip-pyc@25.1.1-r1 
│                │      ├ Name          : py3-pip-pyc 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/py3-pip-pyc@25.1.1-r1?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 111ee7a5a0ef5f49 
│                │      ├ Version       : 25.1.1-r1 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : py3-pip 
│                │      ├ SrcVersion    : 25.1.1-r1 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Achill Gilgenast <achill@achill.org> 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:5e28e07b305888b038bbd7d47862d3ca1a3f50c7 
│                │      ╰ InstalledFiles ╭ [0]  : usr/lib/python3.12/site-packages/pip/__pycache__/__init__.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [1]  : usr/lib/python3.12/site-packages/pip/__pycache__/__main__.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [2]  : usr/lib/python3.12/site-packages/pip/__pycache__/__pip-runner
│                │                       │        __.cpython-312.pyc 
│                │                       ├ [3]  : usr/lib/python3.12/site-packages/pip/_internal/__pycache__/__
│                │                       │        init__.cpython-312.pyc 
│                │                       ├ [4]  : usr/lib/python3.12/site-packages/pip/_internal/__pycache__/bu
│                │                       │        ild_env.cpython-312.pyc 
│                │                       ├ [5]  : usr/lib/python3.12/site-packages/pip/_internal/__pycache__/ca
│                │                       │        che.cpython-312.pyc 
│                │                       ├ [6]  : usr/lib/python3.12/site-packages/pip/_internal/__pycache__/co
│                │                       │        nfiguration.cpython-312.pyc 
│                │                       ├ [7]  : usr/lib/python3.12/site-packages/pip/_internal/__pycache__/ex
│                │                       │        ceptions.cpython-312.pyc 
│                │                       ├ [8]  : usr/lib/python3.12/site-packages/pip/_internal/__pycache__/ma
│                │                       │        in.cpython-312.pyc 
│                │                       ├ [9]  : usr/lib/python3.12/site-packages/pip/_internal/__pycache__/py
│                │                       │        project.cpython-312.pyc 
│                │                       ├ [10] : usr/lib/python3.12/site-packages/pip/_internal/__pycache__/se
│                │                       │        lf_outdated_check.cpython-312.pyc 
│                │                       ├ [11] : usr/lib/python3.12/site-packages/pip/_internal/__pycache__/wh
│                │                       │        eel_builder.cpython-312.pyc 
│                │                       ├ [12] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/__init__.cpython-312.pyc 
│                │                       ├ [13] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/autocompletion.cpython-312.pyc 
│                │                       ├ [14] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/base_command.cpython-312.pyc 
│                │                       ├ [15] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/cmdoptions.cpython-312.pyc 
│                │                       ├ [16] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/command_context.cpython-312.pyc 
│                │                       ├ [17] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/index_command.cpython-312.pyc 
│                │                       ├ [18] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/main.cpython-312.pyc 
│                │                       ├ [19] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/main_parser.cpython-312.pyc 
│                │                       ├ [20] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/parser.cpython-312.pyc 
│                │                       ├ [21] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/progress_bars.cpython-312.pyc 
│                │                       ├ [22] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/req_command.cpython-312.pyc 
│                │                       ├ [23] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/spinners.cpython-312.pyc 
│                │                       ├ [24] : usr/lib/python3.12/site-packages/pip/_internal/cli/__pycache_
│                │                       │        _/status_codes.cpython-312.pyc 
│                │                       ├ [25] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/__init__.cpython-312.pyc 
│                │                       ├ [26] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/cache.cpython-312.pyc 
│                │                       ├ [27] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/check.cpython-312.pyc 
│                │                       ├ [28] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/completion.cpython-312.pyc 
│                │                       ├ [29] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/configuration.cpython-312.pyc 
│                │                       ├ [30] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/debug.cpython-312.pyc 
│                │                       ├ [31] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/download.cpython-312.pyc 
│                │                       ├ [32] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/freeze.cpython-312.pyc 
│                │                       ├ [33] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/hash.cpython-312.pyc 
│                │                       ├ [34] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/help.cpython-312.pyc 
│                │                       ├ [35] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/index.cpython-312.pyc 
│                │                       ├ [36] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/inspect.cpython-312.pyc 
│                │                       ├ [37] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/install.cpython-312.pyc 
│                │                       ├ [38] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/list.cpython-312.pyc 
│                │                       ├ [39] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/lock.cpython-312.pyc 
│                │                       ├ [40] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/search.cpython-312.pyc 
│                │                       ├ [41] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/show.cpython-312.pyc 
│                │                       ├ [42] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/uninstall.cpython-312.pyc 
│                │                       ├ [43] : usr/lib/python3.12/site-packages/pip/_internal/commands/__pyc
│                │                       │        ache__/wheel.cpython-312.pyc 
│                │                       ├ [44] : usr/lib/python3.12/site-packages/pip/_internal/distributions/
│                │                       │        __pycache__/__init__.cpython-312.pyc 
│                │                       ├ [45] : usr/lib/python3.12/site-packages/pip/_internal/distributions/
│                │                       │        __pycache__/base.cpython-312.pyc 
│                │                       ├ [46] : usr/lib/python3.12/site-packages/pip/_internal/distributions/
│                │                       │        __pycache__/installed.cpython-312.pyc 
│                │                       ├ [47] : usr/lib/python3.12/site-packages/pip/_internal/distributions/
│                │                       │        __pycache__/sdist.cpython-312.pyc 
│                │                       ├ [48] : usr/lib/python3.12/site-packages/pip/_internal/distributions/
│                │                       │        __pycache__/wheel.cpython-312.pyc 
│                │                       ├ [49] : usr/lib/python3.12/site-packages/pip/_internal/index/__pycach
│                │                       │        e__/__init__.cpython-312.pyc 
│                │                       ├ [50] : usr/lib/python3.12/site-packages/pip/_internal/index/__pycach
│                │                       │        e__/collector.cpython-312.pyc 
│                │                       ├ [51] : usr/lib/python3.12/site-packages/pip/_internal/index/__pycach
│                │                       │        e__/package_finder.cpython-312.pyc 
│                │                       ├ [52] : usr/lib/python3.12/site-packages/pip/_internal/index/__pycach
│                │                       │        e__/sources.cpython-312.pyc 
│                │                       ├ [53] : usr/lib/python3.12/site-packages/pip/_internal/locations/__py
│                │                       │        cache__/__init__.cpython-312.pyc 
│                │                       ├ [54] : usr/lib/python3.12/site-packages/pip/_internal/locations/__py
│                │                       │        cache__/_distutils.cpython-312.pyc 
│                │                       ├ [55] : usr/lib/python3.12/site-packages/pip/_internal/locations/__py
│                │                       │        cache__/_sysconfig.cpython-312.pyc 
│                │                       ├ [56] : usr/lib/python3.12/site-packages/pip/_internal/locations/__py
│                │                       │        cache__/base.cpython-312.pyc 
│                │                       ├ [57] : usr/lib/python3.12/site-packages/pip/_internal/metadata/__pyc
│                │                       │        ache__/__init__.cpython-312.pyc 
│                │                       ├ [58] : usr/lib/python3.12/site-packages/pip/_internal/metadata/__pyc
│                │                       │        ache__/_json.cpython-312.pyc 
│                │                       ├ [59] : usr/lib/python3.12/site-packages/pip/_internal/metadata/__pyc
│                │                       │        ache__/base.cpython-312.pyc 
│                │                       ├ [60] : usr/lib/python3.12/site-packages/pip/_internal/metadata/__pyc
│                │                       │        ache__/pkg_resources.cpython-312.pyc 
│                │                       ├ [61] : usr/lib/python3.12/site-packages/pip/_internal/metadata/impor
│                │                       │        tlib/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [62] : usr/lib/python3.12/site-packages/pip/_internal/metadata/impor
│                │                       │        tlib/__pycache__/_compat.cpython-312.pyc 
│                │                       ├ [63] : usr/lib/python3.12/site-packages/pip/_internal/metadata/impor
│                │                       │        tlib/__pycache__/_dists.cpython-312.pyc 
│                │                       ├ [64] : usr/lib/python3.12/site-packages/pip/_internal/metadata/impor
│                │                       │        tlib/__pycache__/_envs.cpython-312.pyc 
│                │                       ├ [65] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/__init__.cpython-312.pyc 
│                │                       ├ [66] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/candidate.cpython-312.pyc 
│                │                       ├ [67] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/direct_url.cpython-312.pyc 
│                │                       ├ [68] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/format_control.cpython-312.pyc 
│                │                       ├ [69] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/index.cpython-312.pyc 
│                │                       ├ [70] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/installation_report.cpython-312.pyc 
│                │                       ├ [71] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/link.cpython-312.pyc 
│                │                       ├ [72] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/pylock.cpython-312.pyc 
│                │                       ├ [73] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/scheme.cpython-312.pyc 
│                │                       ├ [74] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/search_scope.cpython-312.pyc 
│                │                       ├ [75] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/selection_prefs.cpython-312.pyc 
│                │                       ├ [76] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/target_python.cpython-312.pyc 
│                │                       ├ [77] : usr/lib/python3.12/site-packages/pip/_internal/models/__pycac
│                │                       │        he__/wheel.cpython-312.pyc 
│                │                       ├ [78] : usr/lib/python3.12/site-packages/pip/_internal/network/__pyca
│                │                       │        che__/__init__.cpython-312.pyc 
│                │                       ├ [79] : usr/lib/python3.12/site-packages/pip/_internal/network/__pyca
│                │                       │        che__/auth.cpython-312.pyc 
│                │                       ├ [80] : usr/lib/python3.12/site-packages/pip/_internal/network/__pyca
│                │                       │        che__/cache.cpython-312.pyc 
│                │                       ├ [81] : usr/lib/python3.12/site-packages/pip/_internal/network/__pyca
│                │                       │        che__/download.cpython-312.pyc 
│                │                       ├ [82] : usr/lib/python3.12/site-packages/pip/_internal/network/__pyca
│                │                       │        che__/lazy_wheel.cpython-312.pyc 
│                │                       ├ [83] : usr/lib/python3.12/site-packages/pip/_internal/network/__pyca
│                │                       │        che__/session.cpython-312.pyc 
│                │                       ├ [84] : usr/lib/python3.12/site-packages/pip/_internal/network/__pyca
│                │                       │        che__/utils.cpython-312.pyc 
│                │                       ├ [85] : usr/lib/python3.12/site-packages/pip/_internal/network/__pyca
│                │                       │        che__/xmlrpc.cpython-312.pyc 
│                │                       ├ [86] : usr/lib/python3.12/site-packages/pip/_internal/operations/__p
│                │                       │        ycache__/__init__.cpython-312.pyc 
│                │                       ├ [87] : usr/lib/python3.12/site-packages/pip/_internal/operations/__p
│                │                       │        ycache__/check.cpython-312.pyc 
│                │                       ├ [88] : usr/lib/python3.12/site-packages/pip/_internal/operations/__p
│                │                       │        ycache__/freeze.cpython-312.pyc 
│                │                       ├ [89] : usr/lib/python3.12/site-packages/pip/_internal/operations/__p
│                │                       │        ycache__/prepare.cpython-312.pyc 
│                │                       ├ [90] : usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [91] : usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/__pycache__/build_tracker.cpython-312.pyc 
│                │                       ├ [92] : usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/__pycache__/metadata.cpython-312.pyc 
│                │                       ├ [93] : usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/__pycache__/metadata_editable.cpython-312.pyc 
│                │                       ├ [94] : usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/__pycache__/metadata_legacy.cpython-312.pyc 
│                │                       ├ [95] : usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/__pycache__/wheel.cpython-312.pyc 
│                │                       ├ [96] : usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/__pycache__/wheel_editable.cpython-312.pyc 
│                │                       ├ [97] : usr/lib/python3.12/site-packages/pip/_internal/operations/bui
│                │                       │        ld/__pycache__/wheel_legacy.cpython-312.pyc 
│                │                       ├ [98] : usr/lib/python3.12/site-packages/pip/_internal/operations/ins
│                │                       │        tall/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [99] : usr/lib/python3.12/site-packages/pip/_internal/operations/ins
│                │                       │        tall/__pycache__/editable_legacy.cpython-312.pyc 
│                │                       ├ [100]: usr/lib/python3.12/site-packages/pip/_internal/operations/ins
│                │                       │        tall/__pycache__/wheel.cpython-312.pyc 
│                │                       ├ [101]: usr/lib/python3.12/site-packages/pip/_internal/req/__pycache_
│                │                       │        _/__init__.cpython-312.pyc 
│                │                       ├ [102]: usr/lib/python3.12/site-packages/pip/_internal/req/__pycache_
│                │                       │        _/constructors.cpython-312.pyc 
│                │                       ├ [103]: usr/lib/python3.12/site-packages/pip/_internal/req/__pycache_
│                │                       │        _/req_dependency_group.cpython-312.pyc 
│                │                       ├ [104]: usr/lib/python3.12/site-packages/pip/_internal/req/__pycache_
│                │                       │        _/req_file.cpython-312.pyc 
│                │                       ├ [105]: usr/lib/python3.12/site-packages/pip/_internal/req/__pycache_
│                │                       │        _/req_install.cpython-312.pyc 
│                │                       ├ [106]: usr/lib/python3.12/site-packages/pip/_internal/req/__pycache_
│                │                       │        _/req_set.cpython-312.pyc 
│                │                       ├ [107]: usr/lib/python3.12/site-packages/pip/_internal/req/__pycache_
│                │                       │        _/req_uninstall.cpython-312.pyc 
│                │                       ├ [108]: usr/lib/python3.12/site-packages/pip/_internal/resolution/__p
│                │                       │        ycache__/__init__.cpython-312.pyc 
│                │                       ├ [109]: usr/lib/python3.12/site-packages/pip/_internal/resolution/__p
│                │                       │        ycache__/base.cpython-312.pyc 
│                │                       ├ [110]: usr/lib/python3.12/site-packages/pip/_internal/resolution/leg
│                │                       │        acy/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [111]: usr/lib/python3.12/site-packages/pip/_internal/resolution/leg
│                │                       │        acy/__pycache__/resolver.cpython-312.pyc 
│                │                       ├ [112]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [113]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/__pycache__/base.cpython-312.pyc 
│                │                       ├ [114]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/__pycache__/candidates.cpython-312.pyc 
│                │                       ├ [115]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/__pycache__/factory.cpython-312.pyc 
│                │                       ├ [116]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/__pycache__/found_candidates.cpython-312.pyc 
│                │                       ├ [117]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/__pycache__/provider.cpython-312.pyc 
│                │                       ├ [118]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/__pycache__/reporter.cpython-312.pyc 
│                │                       ├ [119]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/__pycache__/requirements.cpython-312.pyc 
│                │                       ├ [120]: usr/lib/python3.12/site-packages/pip/_internal/resolution/res
│                │                       │        olvelib/__pycache__/resolver.cpython-312.pyc 
│                │                       ├ [121]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/__init__.cpython-312.pyc 
│                │                       ├ [122]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/_jaraco_text.cpython-312.pyc 
│                │                       ├ [123]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/_log.cpython-312.pyc 
│                │                       ├ [124]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/appdirs.cpython-312.pyc 
│                │                       ├ [125]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/compat.cpython-312.pyc 
│                │                       ├ [126]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/compatibility_tags.cpython-312.pyc 
│                │                       ├ [127]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/datetime.cpython-312.pyc 
│                │                       ├ [128]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/deprecation.cpython-312.pyc 
│                │                       ├ [129]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/direct_url_helpers.cpython-312.pyc 
│                │                       ├ [130]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/egg_link.cpython-312.pyc 
│                │                       ├ [131]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/entrypoints.cpython-312.pyc 
│                │                       ├ [132]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/filesystem.cpython-312.pyc 
│                │                       ├ [133]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/filetypes.cpython-312.pyc 
│                │                       ├ [134]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/glibc.cpython-312.pyc 
│                │                       ├ [135]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/hashes.cpython-312.pyc 
│                │                       ├ [136]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/logging.cpython-312.pyc 
│                │                       ├ [137]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/misc.cpython-312.pyc 
│                │                       ├ [138]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/packaging.cpython-312.pyc 
│                │                       ├ [139]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/retry.cpython-312.pyc 
│                │                       ├ [140]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/setuptools_build.cpython-312.pyc 
│                │                       ├ [141]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/subprocess.cpython-312.pyc 
│                │                       ├ [142]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/temp_dir.cpython-312.pyc 
│                │                       ├ [143]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/unpacking.cpython-312.pyc 
│                │                       ├ [144]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/urls.cpython-312.pyc 
│                │                       ├ [145]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/virtualenv.cpython-312.pyc 
│                │                       ├ [146]: usr/lib/python3.12/site-packages/pip/_internal/utils/__pycach
│                │                       │        e__/wheel.cpython-312.pyc 
│                │                       ├ [147]: usr/lib/python3.12/site-packages/pip/_internal/vcs/__pycache_
│                │                       │        _/__init__.cpython-312.pyc 
│                │                       ├ [148]: usr/lib/python3.12/site-packages/pip/_internal/vcs/__pycache_
│                │                       │        _/bazaar.cpython-312.pyc 
│                │                       ├ [149]: usr/lib/python3.12/site-packages/pip/_internal/vcs/__pycache_
│                │                       │        _/git.cpython-312.pyc 
│                │                       ├ [150]: usr/lib/python3.12/site-packages/pip/_internal/vcs/__pycache_
│                │                       │        _/mercurial.cpython-312.pyc 
│                │                       ├ [151]: usr/lib/python3.12/site-packages/pip/_internal/vcs/__pycache_
│                │                       │        _/subversion.cpython-312.pyc 
│                │                       ├ [152]: usr/lib/python3.12/site-packages/pip/_internal/vcs/__pycache_
│                │                       │        _/versioncontrol.cpython-312.pyc 
│                │                       ├ [153]: usr/lib/python3.12/site-packages/pip/_vendor/__pycache__/__in
│                │                       │        it__.cpython-312.pyc 
│                │                       ├ [154]: usr/lib/python3.12/site-packages/pip/_vendor/__pycache__/typi
│                │                       │        ng_extensions.cpython-312.pyc 
│                │                       ├ [155]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/__p
│                │                       │        ycache__/__init__.cpython-312.pyc 
│                │                       ├ [156]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/__p
│                │                       │        ycache__/_cmd.cpython-312.pyc 
│                │                       ├ [157]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/__p
│                │                       │        ycache__/adapter.cpython-312.pyc 
│                │                       ├ [158]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/__p
│                │                       │        ycache__/cache.cpython-312.pyc 
│                │                       ├ [159]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/__p
│                │                       │        ycache__/controller.cpython-312.pyc 
│                │                       ├ [160]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/__p
│                │                       │        ycache__/filewrapper.cpython-312.pyc 
│                │                       ├ [161]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/__p
│                │                       │        ycache__/heuristics.cpython-312.pyc 
│                │                       ├ [162]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/__p
│                │                       │        ycache__/serialize.cpython-312.pyc 
│                │                       ├ [163]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/__p
│                │                       │        ycache__/wrapper.cpython-312.pyc 
│                │                       ├ [164]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/cac
│                │                       │        hes/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [165]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/cac
│                │                       │        hes/__pycache__/file_cache.cpython-312.pyc 
│                │                       ├ [166]: usr/lib/python3.12/site-packages/pip/_vendor/cachecontrol/cac
│                │                       │        hes/__pycache__/redis_cache.cpython-312.pyc 
│                │                       ├ [167]: usr/lib/python3.12/site-packages/pip/_vendor/certifi/__pycach
│                │                       │        e__/__init__.cpython-312.pyc 
│                │                       ├ [168]: usr/lib/python3.12/site-packages/pip/_vendor/certifi/__pycach
│                │                       │        e__/__main__.cpython-312.pyc 
│                │                       ├ [169]: usr/lib/python3.12/site-packages/pip/_vendor/certifi/__pycach
│                │                       │        e__/core.cpython-312.pyc 
│                │                       ├ [170]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [171]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/__pycache__/__main__.cpython-312.pyc 
│                │                       ├ [172]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/__pycache__/_implementation.cpython-312.pyc 
│                │                       ├ [173]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/__pycache__/_lint_dependency_groups.cpython-312.pyc 
│                │                       ├ [174]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/__pycache__/_pip_wrapper.cpython-312.pyc 
│                │                       ├ [175]: usr/lib/python3.12/site-packages/pip/_vendor/dependency_group
│                │                       │        s/__pycache__/_toml_compat.cpython-312.pyc 
│                │                       ├ [176]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/__init__.cpython-312.pyc 
│                │                       ├ [177]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/compat.cpython-312.pyc 
│                │                       ├ [178]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/database.cpython-312.pyc 
│                │                       ├ [179]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/index.cpython-312.pyc 
│                │                       ├ [180]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/locators.cpython-312.pyc 
│                │                       ├ [181]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/manifest.cpython-312.pyc 
│                │                       ├ [182]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/markers.cpython-312.pyc 
│                │                       ├ [183]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/metadata.cpython-312.pyc 
│                │                       ├ [184]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/resources.cpython-312.pyc 
│                │                       ├ [185]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/scripts.cpython-312.pyc 
│                │                       ├ [186]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/util.cpython-312.pyc 
│                │                       ├ [187]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/version.cpython-312.pyc 
│                │                       ├ [188]: usr/lib/python3.12/site-packages/pip/_vendor/distlib/__pycach
│                │                       │        e__/wheel.cpython-312.pyc 
│                │                       ├ [189]: usr/lib/python3.12/site-packages/pip/_vendor/distro/__pycache
│                │                       │        __/__init__.cpython-312.pyc 
│                │                       ├ [190]: usr/lib/python3.12/site-packages/pip/_vendor/distro/__pycache
│                │                       │        __/__main__.cpython-312.pyc 
│                │                       ├ [191]: usr/lib/python3.12/site-packages/pip/_vendor/distro/__pycache
│                │                       │        __/distro.cpython-312.pyc 
│                │                       ├ [192]: usr/lib/python3.12/site-packages/pip/_vendor/idna/__pycache__
│                │                       │        /__init__.cpython-312.pyc 
│                │                       ├ [193]: usr/lib/python3.12/site-packages/pip/_vendor/idna/__pycache__
│                │                       │        /codec.cpython-312.pyc 
│                │                       ├ [194]: usr/lib/python3.12/site-packages/pip/_vendor/idna/__pycache__
│                │                       │        /compat.cpython-312.pyc 
│                │                       ├ [195]: usr/lib/python3.12/site-packages/pip/_vendor/idna/__pycache__
│                │                       │        /core.cpython-312.pyc 
│                │                       ├ [196]: usr/lib/python3.12/site-packages/pip/_vendor/idna/__pycache__
│                │                       │        /idnadata.cpython-312.pyc 
│                │                       ├ [197]: usr/lib/python3.12/site-packages/pip/_vendor/idna/__pycache__
│                │                       │        /intranges.cpython-312.pyc 
│                │                       ├ [198]: usr/lib/python3.12/site-packages/pip/_vendor/idna/__pycache__
│                │                       │        /package_data.cpython-312.pyc 
│                │                       ├ [199]: usr/lib/python3.12/site-packages/pip/_vendor/idna/__pycache__
│                │                       │        /uts46data.cpython-312.pyc 
│                │                       ├ [200]: usr/lib/python3.12/site-packages/pip/_vendor/msgpack/__pycach
│                │                       │        e__/__init__.cpython-312.pyc 
│                │                       ├ [201]: usr/lib/python3.12/site-packages/pip/_vendor/msgpack/__pycach
│                │                       │        e__/exceptions.cpython-312.pyc 
│                │                       ├ [202]: usr/lib/python3.12/site-packages/pip/_vendor/msgpack/__pycach
│                │                       │        e__/ext.cpython-312.pyc 
│                │                       ├ [203]: usr/lib/python3.12/site-packages/pip/_vendor/msgpack/__pycach
│                │                       │        e__/fallback.cpython-312.pyc 
│                │                       ├ [204]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/__init__.cpython-312.pyc 
│                │                       ├ [205]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/_elffile.cpython-312.pyc 
│                │                       ├ [206]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/_manylinux.cpython-312.pyc 
│                │                       ├ [207]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/_musllinux.cpython-312.pyc 
│                │                       ├ [208]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/_parser.cpython-312.pyc 
│                │                       ├ [209]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/_structures.cpython-312.pyc 
│                │                       ├ [210]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/_tokenizer.cpython-312.pyc 
│                │                       ├ [211]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/markers.cpython-312.pyc 
│                │                       ├ [212]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/metadata.cpython-312.pyc 
│                │                       ├ [213]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/requirements.cpython-312.pyc 
│                │                       ├ [214]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/specifiers.cpython-312.pyc 
│                │                       ├ [215]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/tags.cpython-312.pyc 
│                │                       ├ [216]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/utils.cpython-312.pyc 
│                │                       ├ [217]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/__pyca
│                │                       │        che__/version.cpython-312.pyc 
│                │                       ├ [218]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/licens
│                │                       │        es/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [219]: usr/lib/python3.12/site-packages/pip/_vendor/packaging/licens
│                │                       │        es/__pycache__/_spdx.cpython-312.pyc 
│                │                       ├ [220]: usr/lib/python3.12/site-packages/pip/_vendor/pkg_resources/__
│                │                       │        pycache__/__init__.cpython-312.pyc 
│                │                       ├ [221]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/__p
│                │                       │        ycache__/__init__.cpython-312.pyc 
│                │                       ├ [222]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/__p
│                │                       │        ycache__/__main__.cpython-312.pyc 
│                │                       ├ [223]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/__p
│                │                       │        ycache__/android.cpython-312.pyc 
│                │                       ├ [224]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/__p
│                │                       │        ycache__/api.cpython-312.pyc 
│                │                       ├ [225]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/__p
│                │                       │        ycache__/macos.cpython-312.pyc 
│                │                       ├ [226]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/__p
│                │                       │        ycache__/unix.cpython-312.pyc 
│                │                       ├ [227]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/__p
│                │                       │        ycache__/version.cpython-312.pyc 
│                │                       ├ [228]: usr/lib/python3.12/site-packages/pip/_vendor/platformdirs/__p
│                │                       │        ycache__/windows.cpython-312.pyc 
│                │                       ├ [229]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/__init__.cpython-312.pyc 
│                │                       ├ [230]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/__main__.cpython-312.pyc 
│                │                       ├ [231]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/console.cpython-312.pyc 
│                │                       ├ [232]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/filter.cpython-312.pyc 
│                │                       ├ [233]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/formatter.cpython-312.pyc 
│                │                       ├ [234]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/lexer.cpython-312.pyc 
│                │                       ├ [235]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/modeline.cpython-312.pyc 
│                │                       ├ [236]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/plugin.cpython-312.pyc 
│                │                       ├ [237]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/regexopt.cpython-312.pyc 
│                │                       ├ [238]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/scanner.cpython-312.pyc 
│                │                       ├ [239]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/sphinxext.cpython-312.pyc 
│                │                       ├ [240]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/style.cpython-312.pyc 
│                │                       ├ [241]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/token.cpython-312.pyc 
│                │                       ├ [242]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/unistring.cpython-312.pyc 
│                │                       ├ [243]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/__pycac
│                │                       │        he__/util.cpython-312.pyc 
│                │                       ├ [244]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/filters
│                │                       │        /__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [245]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/formatt
│                │                       │        ers/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [246]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/formatt
│                │                       │        ers/__pycache__/_mapping.cpython-312.pyc 
│                │                       ├ [247]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/lexers/
│                │                       │        __pycache__/__init__.cpython-312.pyc 
│                │                       ├ [248]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/lexers/
│                │                       │        __pycache__/_mapping.cpython-312.pyc 
│                │                       ├ [249]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/lexers/
│                │                       │        __pycache__/python.cpython-312.pyc 
│                │                       ├ [250]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/styles/
│                │                       │        __pycache__/__init__.cpython-312.pyc 
│                │                       ├ [251]: usr/lib/python3.12/site-packages/pip/_vendor/pygments/styles/
│                │                       │        __pycache__/_mapping.cpython-312.pyc 
│                │                       ├ [252]: usr/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/
│                │                       │        __pycache__/__init__.cpython-312.pyc 
│                │                       ├ [253]: usr/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/
│                │                       │        __pycache__/_impl.cpython-312.pyc 
│                │                       ├ [254]: usr/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/
│                │                       │        _in_process/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [255]: usr/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/
│                │                       │        _in_process/__pycache__/_in_process.cpython-312.pyc 
│                │                       ├ [256]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/__init__.cpython-312.pyc 
│                │                       ├ [257]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/__version__.cpython-312.pyc 
│                │                       ├ [258]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/_internal_utils.cpython-312.pyc 
│                │                       ├ [259]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/adapters.cpython-312.pyc 
│                │                       ├ [260]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/api.cpython-312.pyc 
│                │                       ├ [261]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/auth.cpython-312.pyc 
│                │                       ├ [262]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/certs.cpython-312.pyc 
│                │                       ├ [263]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/compat.cpython-312.pyc 
│                │                       ├ [264]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/cookies.cpython-312.pyc 
│                │                       ├ [265]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/exceptions.cpython-312.pyc 
│                │                       ├ [266]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/help.cpython-312.pyc 
│                │                       ├ [267]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/hooks.cpython-312.pyc 
│                │                       ├ [268]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/models.cpython-312.pyc 
│                │                       ├ [269]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/packages.cpython-312.pyc 
│                │                       ├ [270]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/sessions.cpython-312.pyc 
│                │                       ├ [271]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/status_codes.cpython-312.pyc 
│                │                       ├ [272]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/structures.cpython-312.pyc 
│                │                       ├ [273]: usr/lib/python3.12/site-packages/pip/_vendor/requests/__pycac
│                │                       │        he__/utils.cpython-312.pyc 
│                │                       ├ [274]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/__pyc
│                │                       │        ache__/__init__.cpython-312.pyc 
│                │                       ├ [275]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/__pyc
│                │                       │        ache__/providers.cpython-312.pyc 
│                │                       ├ [276]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/__pyc
│                │                       │        ache__/reporters.cpython-312.pyc 
│                │                       ├ [277]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/__pyc
│                │                       │        ache__/structs.cpython-312.pyc 
│                │                       ├ [278]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/resol
│                │                       │        vers/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [279]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/resol
│                │                       │        vers/__pycache__/abstract.cpython-312.pyc 
│                │                       ├ [280]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/resol
│                │                       │        vers/__pycache__/criterion.cpython-312.pyc 
│                │                       ├ [281]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/resol
│                │                       │        vers/__pycache__/exceptions.cpython-312.pyc 
│                │                       ├ [282]: usr/lib/python3.12/site-packages/pip/_vendor/resolvelib/resol
│                │                       │        vers/__pycache__/resolution.cpython-312.pyc 
│                │                       ├ [283]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /__init__.cpython-312.pyc 
│                │                       ├ [284]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /__main__.cpython-312.pyc 
│                │                       ├ [285]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_cell_widths.cpython-312.pyc 
│                │                       ├ [286]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_emoji_codes.cpython-312.pyc 
│                │                       ├ [287]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_emoji_replace.cpython-312.pyc 
│                │                       ├ [288]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_export_format.cpython-312.pyc 
│                │                       ├ [289]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_extension.cpython-312.pyc 
│                │                       ├ [290]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_fileno.cpython-312.pyc 
│                │                       ├ [291]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_inspect.cpython-312.pyc 
│                │                       ├ [292]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_log_render.cpython-312.pyc 
│                │                       ├ [293]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_loop.cpython-312.pyc 
│                │                       ├ [294]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_null_file.cpython-312.pyc 
│                │                       ├ [295]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_palettes.cpython-312.pyc 
│                │                       ├ [296]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_pick.cpython-312.pyc 
│                │                       ├ [297]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_ratio.cpython-312.pyc 
│                │                       ├ [298]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_spinners.cpython-312.pyc 
│                │                       ├ [299]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_stack.cpython-312.pyc 
│                │                       ├ [300]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_timer.cpython-312.pyc 
│                │                       ├ [301]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_win32_console.cpython-312.pyc 
│                │                       ├ [302]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_windows.cpython-312.pyc 
│                │                       ├ [303]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_windows_renderer.cpython-312.pyc 
│                │                       ├ [304]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /_wrap.cpython-312.pyc 
│                │                       ├ [305]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /abc.cpython-312.pyc 
│                │                       ├ [306]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /align.cpython-312.pyc 
│                │                       ├ [307]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /ansi.cpython-312.pyc 
│                │                       ├ [308]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /bar.cpython-312.pyc 
│                │                       ├ [309]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /box.cpython-312.pyc 
│                │                       ├ [310]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /cells.cpython-312.pyc 
│                │                       ├ [311]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /color.cpython-312.pyc 
│                │                       ├ [312]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /color_triplet.cpython-312.pyc 
│                │                       ├ [313]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /columns.cpython-312.pyc 
│                │                       ├ [314]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /console.cpython-312.pyc 
│                │                       ├ [315]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /constrain.cpython-312.pyc 
│                │                       ├ [316]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /containers.cpython-312.pyc 
│                │                       ├ [317]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /control.cpython-312.pyc 
│                │                       ├ [318]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /default_styles.cpython-312.pyc 
│                │                       ├ [319]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /diagnose.cpython-312.pyc 
│                │                       ├ [320]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /emoji.cpython-312.pyc 
│                │                       ├ [321]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /errors.cpython-312.pyc 
│                │                       ├ [322]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /file_proxy.cpython-312.pyc 
│                │                       ├ [323]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /filesize.cpython-312.pyc 
│                │                       ├ [324]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /highlighter.cpython-312.pyc 
│                │                       ├ [325]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /json.cpython-312.pyc 
│                │                       ├ [326]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /jupyter.cpython-312.pyc 
│                │                       ├ [327]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /layout.cpython-312.pyc 
│                │                       ├ [328]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /live.cpython-312.pyc 
│                │                       ├ [329]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /live_render.cpython-312.pyc 
│                │                       ├ [330]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /logging.cpython-312.pyc 
│                │                       ├ [331]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /markup.cpython-312.pyc 
│                │                       ├ [332]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /measure.cpython-312.pyc 
│                │                       ├ [333]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /padding.cpython-312.pyc 
│                │                       ├ [334]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /pager.cpython-312.pyc 
│                │                       ├ [335]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /palette.cpython-312.pyc 
│                │                       ├ [336]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /panel.cpython-312.pyc 
│                │                       ├ [337]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /pretty.cpython-312.pyc 
│                │                       ├ [338]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /progress.cpython-312.pyc 
│                │                       ├ [339]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /progress_bar.cpython-312.pyc 
│                │                       ├ [340]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /prompt.cpython-312.pyc 
│                │                       ├ [341]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /protocol.cpython-312.pyc 
│                │                       ├ [342]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /region.cpython-312.pyc 
│                │                       ├ [343]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /repr.cpython-312.pyc 
│                │                       ├ [344]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /rule.cpython-312.pyc 
│                │                       ├ [345]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /scope.cpython-312.pyc 
│                │                       ├ [346]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /screen.cpython-312.pyc 
│                │                       ├ [347]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /segment.cpython-312.pyc 
│                │                       ├ [348]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /spinner.cpython-312.pyc 
│                │                       ├ [349]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /status.cpython-312.pyc 
│                │                       ├ [350]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /style.cpython-312.pyc 
│                │                       ├ [351]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /styled.cpython-312.pyc 
│                │                       ├ [352]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /syntax.cpython-312.pyc 
│                │                       ├ [353]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /table.cpython-312.pyc 
│                │                       ├ [354]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /terminal_theme.cpython-312.pyc 
│                │                       ├ [355]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /text.cpython-312.pyc 
│                │                       ├ [356]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /theme.cpython-312.pyc 
│                │                       ├ [357]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /themes.cpython-312.pyc 
│                │                       ├ [358]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /traceback.cpython-312.pyc 
│                │                       ├ [359]: usr/lib/python3.12/site-packages/pip/_vendor/rich/__pycache__
│                │                       │        /tree.cpython-312.pyc 
│                │                       ├ [360]: usr/lib/python3.12/site-packages/pip/_vendor/tomli/__pycache_
│                │                       │        _/__init__.cpython-312.pyc 
│                │                       ├ [361]: usr/lib/python3.12/site-packages/pip/_vendor/tomli/__pycache_
│                │                       │        _/_parser.cpython-312.pyc 
│                │                       ├ [362]: usr/lib/python3.12/site-packages/pip/_vendor/tomli/__pycache_
│                │                       │        _/_re.cpython-312.pyc 
│                │                       ├ [363]: usr/lib/python3.12/site-packages/pip/_vendor/tomli/__pycache_
│                │                       │        _/_types.cpython-312.pyc 
│                │                       ├ [364]: usr/lib/python3.12/site-packages/pip/_vendor/tomli_w/__pycach
│                │                       │        e__/__init__.cpython-312.pyc 
│                │                       ├ [365]: usr/lib/python3.12/site-packages/pip/_vendor/tomli_w/__pycach
│                │                       │        e__/_writer.cpython-312.pyc 
│                │                       ├ [366]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/__pyc
│                │                       │        ache__/__init__.cpython-312.pyc 
│                │                       ├ [367]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/__pyc
│                │                       │        ache__/_api.cpython-312.pyc 
│                │                       ├ [368]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/__pyc
│                │                       │        ache__/_macos.cpython-312.pyc 
│                │                       ├ [369]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/__pyc
│                │                       │        ache__/_openssl.cpython-312.pyc 
│                │                       ├ [370]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/__pyc
│                │                       │        ache__/_ssl_constants.cpython-312.pyc 
│                │                       ├ [371]: usr/lib/python3.12/site-packages/pip/_vendor/truststore/__pyc
│                │                       │        ache__/_windows.cpython-312.pyc 
│                │                       ├ [372]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/__pycach
│                │                       │        e__/__init__.cpython-312.pyc 
│                │                       ├ [373]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/__pycach
│                │                       │        e__/_collections.cpython-312.pyc 
│                │                       ├ [374]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/__pycach
│                │                       │        e__/_version.cpython-312.pyc 
│                │                       ├ [375]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/__pycach
│                │                       │        e__/connection.cpython-312.pyc 
│                │                       ├ [376]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/__pycach
│                │                       │        e__/connectionpool.cpython-312.pyc 
│                │                       ├ [377]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/__pycach
│                │                       │        e__/exceptions.cpython-312.pyc 
│                │                       ├ [378]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/__pycach
│                │                       │        e__/fields.cpython-312.pyc 
│                │                       ├ [379]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/__pycach
│                │                       │        e__/filepost.cpython-312.pyc 
│                │                       ├ [380]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/__pycach
│                │                       │        e__/poolmanager.cpython-312.pyc 
│                │                       ├ [381]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/__pycach
│                │                       │        e__/request.cpython-312.pyc 
│                │                       ├ [382]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/__pycach
│                │                       │        e__/response.cpython-312.pyc 
│                │                       ├ [383]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        __pycache__/__init__.cpython-312.pyc 
│                │                       ├ [384]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        __pycache__/_appengine_environ.cpython-312.pyc 
│                │                       ├ [385]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        __pycache__/appengine.cpython-312.pyc 
│                │                       ├ [386]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        __pycache__/ntlmpool.cpython-312.pyc 
│                │                       ├ [387]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        __pycache__/pyopenssl.cpython-312.pyc 
│                │                       ├ [388]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        __pycache__/securetransport.cpython-312.pyc 
│                │                       ├ [389]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        __pycache__/socks.cpython-312.pyc 
│                │                       ├ [390]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        _securetransport/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [391]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        _securetransport/__pycache__/bindings.cpython-312.pyc 
│                │                       ├ [392]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/contrib/
│                │                       │        _securetransport/__pycache__/low_level.cpython-312.pyc 
│                │                       ├ [393]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/packages
│                │                       │        /__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [394]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/packages
│                │                       │        /__pycache__/six.cpython-312.pyc 
│                │                       ├ [395]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/packages
│                │                       │        /backports/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [396]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/packages
│                │                       │        /backports/__pycache__/makefile.cpython-312.pyc 
│                │                       ├ [397]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/packages
│                │                       │        /backports/__pycache__/weakref_finalize.cpython-312.pyc 
│                │                       ├ [398]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                       │        ycache__/__init__.cpython-312.pyc 
│                │                       ├ [399]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                       │        ycache__/connection.cpython-312.pyc 
│                │                       ├ [400]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                       │        ycache__/proxy.cpython-312.pyc 
│                │                       ├ [401]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                       │        ycache__/queue.cpython-312.pyc 
│                │                       ├ [402]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                       │        ycache__/request.cpython-312.pyc 
│                │                       ├ [403]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                       │        ycache__/response.cpython-312.pyc 
│                │                       ├ [404]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                       │        ycache__/retry.cpython-312.pyc 
│                │                       ├ [405]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                       │        ycache__/ssl_.cpython-312.pyc 
│                │                       ├ [406]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                       │        ycache__/ssl_match_hostname.cpython-312.pyc 
│                │                       ├ [407]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                       │        ycache__/ssltransport.cpython-312.pyc 
│                │                       ├ [408]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                       │        ycache__/timeout.cpython-312.pyc 
│                │                       ├ [409]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                       │        ycache__/url.cpython-312.pyc 
│                │                       ╰ [410]: usr/lib/python3.12/site-packages/pip/_vendor/urllib3/util/__p
│                │                                ycache__/wait.cpython-312.pyc 
│                ├ [63] ╭ ID            : py3-setuptools@80.9.0-r2 
│                │      ├ Name          : py3-setuptools 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/py3-setuptools@80.9.0-r2?arch=x86_64&distro=3.2
│                │      │                │       3.2 
│                │      │                ╰ UID : 832d1f7cd2bd2bb7 
│                │      ├ Version       : 80.9.0-r2 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : py3-setuptools 
│                │      ├ SrcVersion    : 80.9.0-r2 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Achill Gilgenast <achill@achill.org> 
│                │      ├ DependsOn      ╭ [0]: py3-packaging@25.0-r0 
│                │      │                ╰ [1]: python3@3.12.12-r0 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:56cb361a5115365733ca168b41a9dd2e8200c98f 
│                │      ╰ InstalledFiles ╭ [0]  : usr/lib/python3.12/site-packages/distutils-precedence.pth 
│                │                       ├ [1]  : usr/lib/python3.12/site-packages/_distutils_hack/__init__.py 
│                │                       ├ [2]  : usr/lib/python3.12/site-packages/_distutils_hack/override.py 
│                │                       ├ [3]  : usr/lib/python3.12/site-packages/pkg_resources/__init__.py 
│                │                       ├ [4]  : usr/lib/python3.12/site-packages/pkg_resources/api_tests.txt 
│                │                       ├ [5]  : usr/lib/python3.12/site-packages/pkg_resources/py.typed 
│                │                       ├ [6]  : usr/lib/python3.12/site-packages/pkg_resources/tests/__init__
│                │                       │        .py 
│                │                       ├ [7]  : usr/lib/python3.12/site-packages/pkg_resources/tests/test_fin
│                │                       │        d_distributions.py 
│                │                       ├ [8]  : usr/lib/python3.12/site-packages/pkg_resources/tests/test_int
│                │                       │        egration_zope_interface.py 
│                │                       ├ [9]  : usr/lib/python3.12/site-packages/pkg_resources/tests/test_mar
│                │                       │        kers.py 
│                │                       ├ [10] : usr/lib/python3.12/site-packages/pkg_resources/tests/test_pkg
│                │                       │        _resources.py 
│                │                       ├ [11] : usr/lib/python3.12/site-packages/pkg_resources/tests/test_res
│                │                       │        ources.py 
│                │                       ├ [12] : usr/lib/python3.12/site-packages/pkg_resources/tests/test_wor
│                │                       │        king_set.py 
│                │                       ├ [13] : usr/lib/python3.12/site-packages/pkg_resources/tests/data/my-
│                │                       │        test-package-source/setup.cfg 
│                │                       ├ [14] : usr/lib/python3.12/site-packages/pkg_resources/tests/data/my-
│                │                       │        test-package-source/setup.py 
│                │                       ├ [15] : usr/lib/python3.12/site-packages/pkg_resources/tests/data/my-
│                │                       │        test-package-zip/my-test-package.zip 
│                │                       ├ [16] : usr/lib/python3.12/site-packages/pkg_resources/tests/data/my-
│                │                       │        test-package_unpacked-egg/my_test_package-1.0-py3.7.egg/EGG-I
│                │                       │        NFO/PKG-INFO 
│                │                       ├ [17] : usr/lib/python3.12/site-packages/pkg_resources/tests/data/my-
│                │                       │        test-package_unpacked-egg/my_test_package-1.0-py3.7.egg/EGG-I
│                │                       │        NFO/SOURCES.txt 
│                │                       ├ [18] : usr/lib/python3.12/site-packages/pkg_resources/tests/data/my-
│                │                       │        test-package_unpacked-egg/my_test_package-1.0-py3.7.egg/EGG-I
│                │                       │        NFO/dependency_links.txt 
│                │                       ├ [19] : usr/lib/python3.12/site-packages/pkg_resources/tests/data/my-
│                │                       │        test-package_unpacked-egg/my_test_package-1.0-py3.7.egg/EGG-I
│                │                       │        NFO/top_level.txt 
│                │                       ├ [20] : usr/lib/python3.12/site-packages/pkg_resources/tests/data/my-
│                │                       │        test-package_unpacked-egg/my_test_package-1.0-py3.7.egg/EGG-I
│                │                       │        NFO/zip-safe 
│                │                       ├ [21] : usr/lib/python3.12/site-packages/pkg_resources/tests/data/my-
│                │                       │        test-package_zipped-egg/my_test_package-1.0-py3.7.egg 
│                │                       ├ [22] : usr/lib/python3.12/site-packages/setuptools/__init__.py 
│                │                       ├ [23] : usr/lib/python3.12/site-packages/setuptools/_core_metadata.py 
│                │                       ├ [24] : usr/lib/python3.12/site-packages/setuptools/_discovery.py 
│                │                       ├ [25] : usr/lib/python3.12/site-packages/setuptools/_entry_points.py 
│                │                       ├ [26] : usr/lib/python3.12/site-packages/setuptools/_imp.py 
│                │                       ├ [27] : usr/lib/python3.12/site-packages/setuptools/_importlib.py 
│                │                       ├ [28] : usr/lib/python3.12/site-packages/setuptools/_itertools.py 
│                │                       ├ [29] : usr/lib/python3.12/site-packages/setuptools/_normalization.py 
│                │                       ├ [30] : usr/lib/python3.12/site-packages/setuptools/_path.py 
│                │                       ├ [31] : usr/lib/python3.12/site-packages/setuptools/_reqs.py 
│                │                       ├ [32] : usr/lib/python3.12/site-packages/setuptools/_scripts.py 
│                │                       ├ [33] : usr/lib/python3.12/site-packages/setuptools/_shutil.py 
│                │                       ├ [34] : usr/lib/python3.12/site-packages/setuptools/_static.py 
│                │                       ├ [35] : usr/lib/python3.12/site-packages/setuptools/archive_util.py 
│                │                       ├ [36] : usr/lib/python3.12/site-packages/setuptools/build_meta.py 
│                │                       ├ [37] : usr/lib/python3.12/site-packages/setuptools/depends.py 
│                │                       ├ [38] : usr/lib/python3.12/site-packages/setuptools/discovery.py 
│                │                       ├ [39] : usr/lib/python3.12/site-packages/setuptools/dist.py 
│                │                       ├ [40] : usr/lib/python3.12/site-packages/setuptools/errors.py 
│                │                       ├ [41] : usr/lib/python3.12/site-packages/setuptools/extension.py 
│                │                       ├ [42] : usr/lib/python3.12/site-packages/setuptools/glob.py 
│                │                       ├ [43] : usr/lib/python3.12/site-packages/setuptools/installer.py 
│                │                       ├ [44] : usr/lib/python3.12/site-packages/setuptools/launch.py 
│                │                       ├ [45] : usr/lib/python3.12/site-packages/setuptools/logging.py 
│                │                       ├ [46] : usr/lib/python3.12/site-packages/setuptools/modified.py 
│                │                       ├ [47] : usr/lib/python3.12/site-packages/setuptools/monkey.py 
│                │                       ├ [48] : usr/lib/python3.12/site-packages/setuptools/msvc.py 
│                │                       ├ [49] : usr/lib/python3.12/site-packages/setuptools/namespaces.py 
│                │                       ├ [50] : usr/lib/python3.12/site-packages/setuptools/script (dev).tmpl 
│                │                       ├ [51] : usr/lib/python3.12/site-packages/setuptools/script.tmpl 
│                │                       ├ [52] : usr/lib/python3.12/site-packages/setuptools/unicode_utils.py 
│                │                       ├ [53] : usr/lib/python3.12/site-packages/setuptools/version.py 
│                │                       ├ [54] : usr/lib/python3.12/site-packages/setuptools/warnings.py 
│                │                       ├ [55] : usr/lib/python3.12/site-packages/setuptools/wheel.py 
│                │                       ├ [56] : usr/lib/python3.12/site-packages/setuptools/windows_support.py 
│                │                       ├ [57] : usr/lib/python3.12/site-packages/setuptools-80.9.0.dist-info/
│                │                       │        METADATA 
│                │                       ├ [58] : usr/lib/python3.12/site-packages/setuptools-80.9.0.dist-info/
│                │                       │        RECORD 
│                │                       ├ [59] : usr/lib/python3.12/site-packages/setuptools-80.9.0.dist-info/
│                │                       │        WHEEL 
│                │                       ├ [60] : usr/lib/python3.12/site-packages/setuptools-80.9.0.dist-info/
│                │                       │        entry_points.txt 
│                │                       ├ [61] : usr/lib/python3.12/site-packages/setuptools-80.9.0.dist-info/
│                │                       │        licenses/LICENSE 
│                │                       ├ [62] : usr/lib/python3.12/site-packages/setuptools/_distutils/__init
│                │                       │        __.py 
│                │                       ├ [63] : usr/lib/python3.12/site-packages/setuptools/_distutils/_log.py 
│                │                       ├ [64] : usr/lib/python3.12/site-packages/setuptools/_distutils/_macos
│                │                       │        _compat.py 
│                │                       ├ [65] : usr/lib/python3.12/site-packages/setuptools/_distutils/_modif
│                │                       │        ied.py 
│                │                       ├ [66] : usr/lib/python3.12/site-packages/setuptools/_distutils/_msvcc
│                │                       │        ompiler.py 
│                │                       ├ [67] : usr/lib/python3.12/site-packages/setuptools/_distutils/archiv
│                │                       │        e_util.py 
│                │                       ├ [68] : usr/lib/python3.12/site-packages/setuptools/_distutils/ccompi
│                │                       │        ler.py 
│                │                       ├ [69] : usr/lib/python3.12/site-packages/setuptools/_distutils/cmd.py 
│                │                       ├ [70] : usr/lib/python3.12/site-packages/setuptools/_distutils/core.py 
│                │                       ├ [71] : usr/lib/python3.12/site-packages/setuptools/_distutils/cygwin
│                │                       │        ccompiler.py 
│                │                       ├ [72] : usr/lib/python3.12/site-packages/setuptools/_distutils/debug.py 
│                │                       ├ [73] : usr/lib/python3.12/site-packages/setuptools/_distutils/dep_ut
│                │                       │        il.py 
│                │                       ├ [74] : usr/lib/python3.12/site-packages/setuptools/_distutils/dir_ut
│                │                       │        il.py 
│                │                       ├ [75] : usr/lib/python3.12/site-packages/setuptools/_distutils/dist.py 
│                │                       ├ [76] : usr/lib/python3.12/site-packages/setuptools/_distutils/errors
│                │                       │        .py 
│                │                       ├ [77] : usr/lib/python3.12/site-packages/setuptools/_distutils/extens
│                │                       │        ion.py 
│                │                       ├ [78] : usr/lib/python3.12/site-packages/setuptools/_distutils/fancy_
│                │                       │        getopt.py 
│                │                       ├ [79] : usr/lib/python3.12/site-packages/setuptools/_distutils/file_u
│                │                       │        til.py 
│                │                       ├ [80] : usr/lib/python3.12/site-packages/setuptools/_distutils/fileli
│                │                       │        st.py 
│                │                       ├ [81] : usr/lib/python3.12/site-packages/setuptools/_distutils/log.py 
│                │                       ├ [82] : usr/lib/python3.12/site-packages/setuptools/_distutils/spawn.py 
│                │                       ├ [83] : usr/lib/python3.12/site-packages/setuptools/_distutils/syscon
│                │                       │        fig.py 
│                │                       ├ [84] : usr/lib/python3.12/site-packages/setuptools/_distutils/text_f
│                │                       │        ile.py 
│                │                       ├ [85] : usr/lib/python3.12/site-packages/setuptools/_distutils/unixcc
│                │                       │        ompiler.py 
│                │                       ├ [86] : usr/lib/python3.12/site-packages/setuptools/_distutils/util.py 
│                │                       ├ [87] : usr/lib/python3.12/site-packages/setuptools/_distutils/versio
│                │                       │        n.py 
│                │                       ├ [88] : usr/lib/python3.12/site-packages/setuptools/_distutils/versio
│                │                       │        npredicate.py 
│                │                       ├ [89] : usr/lib/python3.12/site-packages/setuptools/_distutils/zoscco
│                │                       │        mpiler.py 
│                │                       ├ [90] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__init__.py 
│                │                       ├ [91] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/_framework_compat.py 
│                │                       ├ [92] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/bdist.py 
│                │                       ├ [93] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/bdist_dumb.py 
│                │                       ├ [94] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/bdist_rpm.py 
│                │                       ├ [95] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/build.py 
│                │                       ├ [96] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/build_clib.py 
│                │                       ├ [97] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/build_ext.py 
│                │                       ├ [98] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/build_py.py 
│                │                       ├ [99] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/build_scripts.py 
│                │                       ├ [100]: usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/check.py 
│                │                       ├ [101]: usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/clean.py 
│                │                       ├ [102]: usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/config.py 
│                │                       ├ [103]: usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/install.py 
│                │                       ├ [104]: usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/install_data.py 
│                │                       ├ [105]: usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/install_egg_info.py 
│                │                       ├ [106]: usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/install_headers.py 
│                │                       ├ [107]: usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/install_lib.py 
│                │                       ├ [108]: usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/install_scripts.py 
│                │                       ├ [109]: usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/sdist.py 
│                │                       ├ [110]: usr/lib/python3.12/site-packages/setuptools/_distutils/compat
│                │                       │        /__init__.py 
│                │                       ├ [111]: usr/lib/python3.12/site-packages/setuptools/_distutils/compat
│                │                       │        /numpy.py 
│                │                       ├ [112]: usr/lib/python3.12/site-packages/setuptools/_distutils/compat
│                │                       │        /py39.py 
│                │                       ├ [113]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/base.py 
│                │                       ├ [114]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/cygwin.py 
│                │                       ├ [115]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/errors.py 
│                │                       ├ [116]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/msvc.py 
│                │                       ├ [117]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/unix.py 
│                │                       ├ [118]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/zos.py 
│                │                       ├ [119]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/tests/test_base.py 
│                │                       ├ [120]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/tests/test_cygwin.py 
│                │                       ├ [121]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/tests/test_mingw.py 
│                │                       ├ [122]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/tests/test_msvc.py 
│                │                       ├ [123]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/tests/test_unix.py 
│                │                       ├ [124]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __init__.py 
│                │                       ├ [125]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        support.py 
│                │                       ├ [126]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_archive_util.py 
│                │                       ├ [127]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_bdist.py 
│                │                       ├ [128]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_bdist_dumb.py 
│                │                       ├ [129]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_bdist_rpm.py 
│                │                       ├ [130]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_build.py 
│                │                       ├ [131]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_build_clib.py 
│                │                       ├ [132]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_build_ext.py 
│                │                       ├ [133]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_build_py.py 
│                │                       ├ [134]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_build_scripts.py 
│                │                       ├ [135]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_check.py 
│                │                       ├ [136]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_clean.py 
│                │                       ├ [137]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_cmd.py 
│                │                       ├ [138]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_config_cmd.py 
│                │                       ├ [139]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_core.py 
│                │                       ├ [140]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_dir_util.py 
│                │                       ├ [141]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_dist.py 
│                │                       ├ [142]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_extension.py 
│                │                       ├ [143]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_file_util.py 
│                │                       ├ [144]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_filelist.py 
│                │                       ├ [145]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_install.py 
│                │                       ├ [146]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_install_data.py 
│                │                       ├ [147]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_install_headers.py 
│                │                       ├ [148]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_install_lib.py 
│                │                       ├ [149]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_install_scripts.py 
│                │                       ├ [150]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_log.py 
│                │                       ├ [151]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_modified.py 
│                │                       ├ [152]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_sdist.py 
│                │                       ├ [153]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_spawn.py 
│                │                       ├ [154]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_sysconfig.py 
│                │                       ├ [155]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_text_file.py 
│                │                       ├ [156]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_util.py 
│                │                       ├ [157]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_version.py 
│                │                       ├ [158]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        test_versionpredicate.py 
│                │                       ├ [159]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        unix_compat.py 
│                │                       ├ [160]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        compat/__init__.py 
│                │                       ├ [161]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        compat/py39.py 
│                │                       ├ [162]: usr/lib/python3.12/site-packages/setuptools/_vendor/typing_ex
│                │                       │        tensions.py 
│                │                       ├ [163]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd/__init__.py 
│                │                       ├ [164]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd/autoasync.py 
│                │                       ├ [165]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd/autocommand.py 
│                │                       ├ [166]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd/automain.py 
│                │                       ├ [167]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd/autoparse.py 
│                │                       ├ [168]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd/errors.py 
│                │                       ├ [169]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd-2.2.2.dist-info/INSTALLER 
│                │                       ├ [170]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd-2.2.2.dist-info/LICENSE 
│                │                       ├ [171]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd-2.2.2.dist-info/METADATA 
│                │                       ├ [172]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd-2.2.2.dist-info/RECORD 
│                │                       ├ [173]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd-2.2.2.dist-info/WHEEL 
│                │                       ├ [174]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd-2.2.2.dist-info/top_level.txt 
│                │                       ├ [175]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        /__init__.py 
│                │                       ├ [176]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        .tarfile-1.2.0.dist-info/INSTALLER 
│                │                       ├ [177]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        .tarfile-1.2.0.dist-info/LICENSE 
│                │                       ├ [178]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        .tarfile-1.2.0.dist-info/METADATA 
│                │                       ├ [179]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        .tarfile-1.2.0.dist-info/RECORD 
│                │                       ├ [180]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        .tarfile-1.2.0.dist-info/REQUESTED 
│                │                       ├ [181]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        .tarfile-1.2.0.dist-info/WHEEL 
│                │                       ├ [182]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        .tarfile-1.2.0.dist-info/top_level.txt 
│                │                       ├ [183]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        /tarfile/__init__.py 
│                │                       ├ [184]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        /tarfile/__main__.py 
│                │                       ├ [185]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        /tarfile/compat/__init__.py 
│                │                       ├ [186]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        /tarfile/compat/py38.py 
│                │                       ├ [187]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/__init__.py 
│                │                       ├ [188]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/_adapters.py 
│                │                       ├ [189]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/_collections.py 
│                │                       ├ [190]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/_compat.py 
│                │                       ├ [191]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/_functools.py 
│                │                       ├ [192]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/_itertools.py 
│                │                       ├ [193]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/_meta.py 
│                │                       ├ [194]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/_text.py 
│                │                       ├ [195]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/diagnose.py 
│                │                       ├ [196]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/py.typed 
│                │                       ├ [197]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata-8.0.0.dist-info/INSTALLER 
│                │                       ├ [198]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata-8.0.0.dist-info/LICENSE 
│                │                       ├ [199]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata-8.0.0.dist-info/METADATA 
│                │                       ├ [200]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata-8.0.0.dist-info/RECORD 
│                │                       ├ [201]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata-8.0.0.dist-info/REQUESTED 
│                │                       ├ [202]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata-8.0.0.dist-info/WHEEL 
│                │                       ├ [203]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata-8.0.0.dist-info/top_level.txt 
│                │                       ├ [204]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/compat/__init__.py 
│                │                       ├ [205]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/compat/py311.py 
│                │                       ├ [206]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/compat/py39.py 
│                │                       ├ [207]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect/_
│                │                       │        _init__.py 
│                │                       ├ [208]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect/p
│                │                       │        y.typed 
│                │                       ├ [209]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect-7
│                │                       │        .3.1.dist-info/INSTALLER 
│                │                       ├ [210]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect-7
│                │                       │        .3.1.dist-info/LICENSE 
│                │                       ├ [211]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect-7
│                │                       │        .3.1.dist-info/METADATA 
│                │                       ├ [212]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect-7
│                │                       │        .3.1.dist-info/RECORD 
│                │                       ├ [213]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect-7
│                │                       │        .3.1.dist-info/WHEEL 
│                │                       ├ [214]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect-7
│                │                       │        .3.1.dist-info/top_level.txt 
│                │                       ├ [215]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect/c
│                │                       │        ompat/__init__.py 
│                │                       ├ [216]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect/c
│                │                       │        ompat/py38.py 
│                │                       ├ [217]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/co
│                │                       │        ntext.py 
│                │                       ├ [218]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        llections-5.1.0.dist-info/INSTALLER 
│                │                       ├ [219]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        llections-5.1.0.dist-info/LICENSE 
│                │                       ├ [220]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        llections-5.1.0.dist-info/METADATA 
│                │                       ├ [221]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        llections-5.1.0.dist-info/RECORD 
│                │                       ├ [222]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        llections-5.1.0.dist-info/REQUESTED 
│                │                       ├ [223]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        llections-5.1.0.dist-info/WHEEL 
│                │                       ├ [224]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        llections-5.1.0.dist-info/top_level.txt 
│                │                       ├ [225]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        ntext-5.3.0.dist-info/INSTALLER 
│                │                       ├ [226]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        ntext-5.3.0.dist-info/LICENSE 
│                │                       ├ [227]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        ntext-5.3.0.dist-info/METADATA 
│                │                       ├ [228]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        ntext-5.3.0.dist-info/RECORD 
│                │                       ├ [229]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        ntext-5.3.0.dist-info/WHEEL 
│                │                       ├ [230]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.co
│                │                       │        ntext-5.3.0.dist-info/top_level.txt 
│                │                       ├ [231]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.fu
│                │                       │        nctools-4.0.1.dist-info/INSTALLER 
│                │                       ├ [232]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.fu
│                │                       │        nctools-4.0.1.dist-info/LICENSE 
│                │                       ├ [233]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.fu
│                │                       │        nctools-4.0.1.dist-info/METADATA 
│                │                       ├ [234]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.fu
│                │                       │        nctools-4.0.1.dist-info/RECORD 
│                │                       ├ [235]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.fu
│                │                       │        nctools-4.0.1.dist-info/WHEEL 
│                │                       ├ [236]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.fu
│                │                       │        nctools-4.0.1.dist-info/top_level.txt 
│                │                       ├ [237]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.te
│                │                       │        xt-3.12.1.dist-info/INSTALLER 
│                │                       ├ [238]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.te
│                │                       │        xt-3.12.1.dist-info/LICENSE 
│                │                       ├ [239]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.te
│                │                       │        xt-3.12.1.dist-info/METADATA 
│                │                       ├ [240]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.te
│                │                       │        xt-3.12.1.dist-info/RECORD 
│                │                       ├ [241]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.te
│                │                       │        xt-3.12.1.dist-info/REQUESTED 
│                │                       ├ [242]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.te
│                │                       │        xt-3.12.1.dist-info/WHEEL 
│                │                       ├ [243]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco.te
│                │                       │        xt-3.12.1.dist-info/top_level.txt 
│                │                       ├ [244]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/co
│                │                       │        llections/__init__.py 
│                │                       ├ [245]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/co
│                │                       │        llections/py.typed 
│                │                       ├ [246]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/fu
│                │                       │        nctools/__init__.py 
│                │                       ├ [247]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/fu
│                │                       │        nctools/__init__.pyi 
│                │                       ├ [248]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/fu
│                │                       │        nctools/py.typed 
│                │                       ├ [249]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/Lorem ipsum.txt 
│                │                       ├ [250]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/__init__.py 
│                │                       ├ [251]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/layouts.py 
│                │                       ├ [252]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/show-newlines.py 
│                │                       ├ [253]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/strip-prefix.py 
│                │                       ├ [254]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/to-dvorak.py 
│                │                       ├ [255]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/to-qwerty.py 
│                │                       ├ [256]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools/__init__.py 
│                │                       ├ [257]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools/__init__.pyi 
│                │                       ├ [258]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools/more.py 
│                │                       ├ [259]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools/more.pyi 
│                │                       ├ [260]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools/py.typed 
│                │                       ├ [261]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools/recipes.py 
│                │                       ├ [262]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools/recipes.pyi 
│                │                       ├ [263]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools-10.3.0.dist-info/INSTALLER 
│                │                       ├ [264]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools-10.3.0.dist-info/LICENSE 
│                │                       ├ [265]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools-10.3.0.dist-info/METADATA 
│                │                       ├ [266]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools-10.3.0.dist-info/RECORD 
│                │                       ├ [267]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools-10.3.0.dist-info/REQUESTED 
│                │                       ├ [268]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools-10.3.0.dist-info/WHEEL 
│                │                       ├ [269]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__init__.py 
│                │                       ├ [270]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /_elffile.py 
│                │                       ├ [271]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /_manylinux.py 
│                │                       ├ [272]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /_musllinux.py 
│                │                       ├ [273]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /_parser.py 
│                │                       ├ [274]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /_structures.py 
│                │                       ├ [275]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /_tokenizer.py 
│                │                       ├ [276]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /markers.py 
│                │                       ├ [277]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /metadata.py 
│                │                       ├ [278]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /py.typed 
│                │                       ├ [279]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /requirements.py 
│                │                       ├ [280]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /specifiers.py 
│                │                       ├ [281]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /tags.py 
│                │                       ├ [282]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /utils.py 
│                │                       ├ [283]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /version.py 
│                │                       ├ [284]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        -24.2.dist-info/INSTALLER 
│                │                       ├ [285]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        -24.2.dist-info/LICENSE 
│                │                       ├ [286]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        -24.2.dist-info/LICENSE.APACHE 
│                │                       ├ [287]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        -24.2.dist-info/LICENSE.BSD 
│                │                       ├ [288]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        -24.2.dist-info/METADATA 
│                │                       ├ [289]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        -24.2.dist-info/RECORD 
│                │                       ├ [290]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        -24.2.dist-info/REQUESTED 
│                │                       ├ [291]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        -24.2.dist-info/WHEEL 
│                │                       ├ [292]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /licenses/__init__.py 
│                │                       ├ [293]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /licenses/_spdx.py 
│                │                       ├ [294]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/__init__.py 
│                │                       ├ [295]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/__main__.py 
│                │                       ├ [296]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/android.py 
│                │                       ├ [297]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/api.py 
│                │                       ├ [298]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/macos.py 
│                │                       ├ [299]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/py.typed 
│                │                       ├ [300]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/unix.py 
│                │                       ├ [301]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/version.py 
│                │                       ├ [302]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/windows.py 
│                │                       ├ [303]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs-4.2.2.dist-info/INSTALLER 
│                │                       ├ [304]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs-4.2.2.dist-info/METADATA 
│                │                       ├ [305]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs-4.2.2.dist-info/RECORD 
│                │                       ├ [306]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs-4.2.2.dist-info/REQUESTED 
│                │                       ├ [307]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs-4.2.2.dist-info/WHEEL 
│                │                       ├ [308]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs-4.2.2.dist-info/licenses/LICENSE 
│                │                       ├ [309]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli/__i
│                │                       │        nit__.py 
│                │                       ├ [310]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli/_pa
│                │                       │        rser.py 
│                │                       ├ [311]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli/_re
│                │                       │        .py 
│                │                       ├ [312]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli/_ty
│                │                       │        pes.py 
│                │                       ├ [313]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli/py.
│                │                       │        typed 
│                │                       ├ [314]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli-2.0
│                │                       │        .1.dist-info/INSTALLER 
│                │                       ├ [315]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli-2.0
│                │                       │        .1.dist-info/LICENSE 
│                │                       ├ [316]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli-2.0
│                │                       │        .1.dist-info/METADATA 
│                │                       ├ [317]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli-2.0
│                │                       │        .1.dist-info/RECORD 
│                │                       ├ [318]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli-2.0
│                │                       │        .1.dist-info/REQUESTED 
│                │                       ├ [319]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli-2.0
│                │                       │        .1.dist-info/WHEEL 
│                │                       ├ [320]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__init__.py 
│                │                       ├ [321]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /_checkers.py 
│                │                       ├ [322]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /_config.py 
│                │                       ├ [323]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /_decorators.py 
│                │                       ├ [324]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /_exceptions.py 
│                │                       ├ [325]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /_functions.py 
│                │                       ├ [326]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /_importhook.py 
│                │                       ├ [327]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /_memo.py 
│                │                       ├ [328]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /_pytest_plugin.py 
│                │                       ├ [329]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /_suppression.py 
│                │                       ├ [330]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /_transformer.py 
│                │                       ├ [331]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /_union_transformer.py 
│                │                       ├ [332]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /_utils.py 
│                │                       ├ [333]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /py.typed 
│                │                       ├ [334]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        -4.3.0.dist-info/INSTALLER 
│                │                       ├ [335]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        -4.3.0.dist-info/LICENSE 
│                │                       ├ [336]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        -4.3.0.dist-info/METADATA 
│                │                       ├ [337]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        -4.3.0.dist-info/RECORD 
│                │                       ├ [338]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        -4.3.0.dist-info/WHEEL 
│                │                       ├ [339]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        -4.3.0.dist-info/entry_points.txt 
│                │                       ├ [340]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        -4.3.0.dist-info/top_level.txt 
│                │                       ├ [341]: usr/lib/python3.12/site-packages/setuptools/_vendor/typing_ex
│                │                       │        tensions-4.12.2.dist-info/INSTALLER 
│                │                       ├ [342]: usr/lib/python3.12/site-packages/setuptools/_vendor/typing_ex
│                │                       │        tensions-4.12.2.dist-info/LICENSE 
│                │                       ├ [343]: usr/lib/python3.12/site-packages/setuptools/_vendor/typing_ex
│                │                       │        tensions-4.12.2.dist-info/METADATA 
│                │                       ├ [344]: usr/lib/python3.12/site-packages/setuptools/_vendor/typing_ex
│                │                       │        tensions-4.12.2.dist-info/RECORD 
│                │                       ├ [345]: usr/lib/python3.12/site-packages/setuptools/_vendor/typing_ex
│                │                       │        tensions-4.12.2.dist-info/WHEEL 
│                │                       ├ [346]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/__i
│                │                       │        nit__.py 
│                │                       ├ [347]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/__m
│                │                       │        ain__.py 
│                │                       ├ [348]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/_bd
│                │                       │        ist_wheel.py 
│                │                       ├ [349]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/_se
│                │                       │        tuptools_logging.py 
│                │                       ├ [350]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/bdi
│                │                       │        st_wheel.py 
│                │                       ├ [351]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/mac
│                │                       │        osx_libfile.py 
│                │                       ├ [352]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/met
│                │                       │        adata.py 
│                │                       ├ [353]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/uti
│                │                       │        l.py 
│                │                       ├ [354]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/whe
│                │                       │        elfile.py 
│                │                       ├ [355]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel-0.4
│                │                       │        5.1.dist-info/INSTALLER 
│                │                       ├ [356]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel-0.4
│                │                       │        5.1.dist-info/LICENSE.txt 
│                │                       ├ [357]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel-0.4
│                │                       │        5.1.dist-info/METADATA 
│                │                       ├ [358]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel-0.4
│                │                       │        5.1.dist-info/RECORD 
│                │                       ├ [359]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel-0.4
│                │                       │        5.1.dist-info/REQUESTED 
│                │                       ├ [360]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel-0.4
│                │                       │        5.1.dist-info/WHEEL 
│                │                       ├ [361]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel-0.4
│                │                       │        5.1.dist-info/entry_points.txt 
│                │                       ├ [362]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/cli
│                │                       │        /__init__.py 
│                │                       ├ [363]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/cli
│                │                       │        /convert.py 
│                │                       ├ [364]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/cli
│                │                       │        /pack.py 
│                │                       ├ [365]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/cli
│                │                       │        /tags.py 
│                │                       ├ [366]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/cli
│                │                       │        /unpack.py 
│                │                       ├ [367]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/__init__.py 
│                │                       ├ [368]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/vendor.txt 
│                │                       ├ [369]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/LICENSE 
│                │                       ├ [370]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/LICENSE.APACHE 
│                │                       ├ [371]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/LICENSE.BSD 
│                │                       ├ [372]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__init__.py 
│                │                       ├ [373]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/_elffile.py 
│                │                       ├ [374]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/_manylinux.py 
│                │                       ├ [375]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/_musllinux.py 
│                │                       ├ [376]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/_parser.py 
│                │                       ├ [377]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/_structures.py 
│                │                       ├ [378]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/_tokenizer.py 
│                │                       ├ [379]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/markers.py 
│                │                       ├ [380]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/requirements.py 
│                │                       ├ [381]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/specifiers.py 
│                │                       ├ [382]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/tags.py 
│                │                       ├ [383]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/utils.py 
│                │                       ├ [384]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/version.py 
│                │                       ├ [385]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp/__in
│                │                       │        it__.py 
│                │                       ├ [386]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp/glob
│                │                       │        .py 
│                │                       ├ [387]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp-3.19
│                │                       │        .2.dist-info/INSTALLER 
│                │                       ├ [388]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp-3.19
│                │                       │        .2.dist-info/LICENSE 
│                │                       ├ [389]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp-3.19
│                │                       │        .2.dist-info/METADATA 
│                │                       ├ [390]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp-3.19
│                │                       │        .2.dist-info/RECORD 
│                │                       ├ [391]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp-3.19
│                │                       │        .2.dist-info/REQUESTED 
│                │                       ├ [392]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp-3.19
│                │                       │        .2.dist-info/WHEEL 
│                │                       ├ [393]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp-3.19
│                │                       │        .2.dist-info/top_level.txt 
│                │                       ├ [394]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp/comp
│                │                       │        at/__init__.py 
│                │                       ├ [395]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp/comp
│                │                       │        at/py310.py 
│                │                       ├ [396]: usr/lib/python3.12/site-packages/setuptools/command/__init__.py 
│                │                       ├ [397]: usr/lib/python3.12/site-packages/setuptools/command/_requires
│                │                       │        txt.py 
│                │                       ├ [398]: usr/lib/python3.12/site-packages/setuptools/command/alias.py 
│                │                       ├ [399]: usr/lib/python3.12/site-packages/setuptools/command/bdist_egg
│                │                       │        .py 
│                │                       ├ [400]: usr/lib/python3.12/site-packages/setuptools/command/bdist_rpm
│                │                       │        .py 
│                │                       ├ [401]: usr/lib/python3.12/site-packages/setuptools/command/bdist_whe
│                │                       │        el.py 
│                │                       ├ [402]: usr/lib/python3.12/site-packages/setuptools/command/build.py 
│                │                       ├ [403]: usr/lib/python3.12/site-packages/setuptools/command/build_cli
│                │                       │        b.py 
│                │                       ├ [404]: usr/lib/python3.12/site-packages/setuptools/command/build_ext
│                │                       │        .py 
│                │                       ├ [405]: usr/lib/python3.12/site-packages/setuptools/command/build_py.py 
│                │                       ├ [406]: usr/lib/python3.12/site-packages/setuptools/command/develop.py 
│                │                       ├ [407]: usr/lib/python3.12/site-packages/setuptools/command/dist_info
│                │                       │        .py 
│                │                       ├ [408]: usr/lib/python3.12/site-packages/setuptools/command/easy_inst
│                │                       │        all.py 
│                │                       ├ [409]: usr/lib/python3.12/site-packages/setuptools/command/editable_
│                │                       │        wheel.py 
│                │                       ├ [410]: usr/lib/python3.12/site-packages/setuptools/command/egg_info.py 
│                │                       ├ [411]: usr/lib/python3.12/site-packages/setuptools/command/install.py 
│                │                       ├ [412]: usr/lib/python3.12/site-packages/setuptools/command/install_e
│                │                       │        gg_info.py 
│                │                       ├ [413]: usr/lib/python3.12/site-packages/setuptools/command/install_l
│                │                       │        ib.py 
│                │                       ├ [414]: usr/lib/python3.12/site-packages/setuptools/command/install_s
│                │                       │        cripts.py 
│                │                       ├ [415]: usr/lib/python3.12/site-packages/setuptools/command/launcher
│                │                       │        manifest.xml 
│                │                       ├ [416]: usr/lib/python3.12/site-packages/setuptools/command/rotate.py 
│                │                       ├ [417]: usr/lib/python3.12/site-packages/setuptools/command/saveopts.py 
│                │                       ├ [418]: usr/lib/python3.12/site-packages/setuptools/command/sdist.py 
│                │                       ├ [419]: usr/lib/python3.12/site-packages/setuptools/command/setopt.py 
│                │                       ├ [420]: usr/lib/python3.12/site-packages/setuptools/command/test.py 
│                │                       ├ [421]: usr/lib/python3.12/site-packages/setuptools/compat/__init__.py 
│                │                       ├ [422]: usr/lib/python3.12/site-packages/setuptools/compat/py310.py 
│                │                       ├ [423]: usr/lib/python3.12/site-packages/setuptools/compat/py311.py 
│                │                       ├ [424]: usr/lib/python3.12/site-packages/setuptools/compat/py312.py 
│                │                       ├ [425]: usr/lib/python3.12/site-packages/setuptools/compat/py39.py 
│                │                       ├ [426]: usr/lib/python3.12/site-packages/setuptools/config/NOTICE 
│                │                       ├ [427]: usr/lib/python3.12/site-packages/setuptools/config/__init__.py 
│                │                       ├ [428]: usr/lib/python3.12/site-packages/setuptools/config/_apply_pyp
│                │                       │        rojecttoml.py 
│                │                       ├ [429]: usr/lib/python3.12/site-packages/setuptools/config/distutils.
│                │                       │        schema.json 
│                │                       ├ [430]: usr/lib/python3.12/site-packages/setuptools/config/expand.py 
│                │                       ├ [431]: usr/lib/python3.12/site-packages/setuptools/config/pyprojectt
│                │                       │        oml.py 
│                │                       ├ [432]: usr/lib/python3.12/site-packages/setuptools/config/setupcfg.py 
│                │                       ├ [433]: usr/lib/python3.12/site-packages/setuptools/config/setuptools
│                │                       │        .schema.json 
│                │                       ├ [434]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/NOTICE 
│                │                       ├ [435]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/__init__.py 
│                │                       ├ [436]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/error_reporting.py 
│                │                       ├ [437]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/extra_validations.py 
│                │                       ├ [438]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/fastjsonschema_exceptions.py 
│                │                       ├ [439]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/fastjsonschema_validations.py 
│                │                       ├ [440]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/formats.py 
│                │                       ├ [441]: usr/lib/python3.12/site-packages/setuptools/tests/__init__.py 
│                │                       ├ [442]: usr/lib/python3.12/site-packages/setuptools/tests/contexts.py 
│                │                       ├ [443]: usr/lib/python3.12/site-packages/setuptools/tests/environment
│                │                       │        .py 
│                │                       ├ [444]: usr/lib/python3.12/site-packages/setuptools/tests/fixtures.py 
│                │                       ├ [445]: usr/lib/python3.12/site-packages/setuptools/tests/mod_with_co
│                │                       │        nstant.py 
│                │                       ├ [446]: usr/lib/python3.12/site-packages/setuptools/tests/namespaces.py 
│                │                       ├ [447]: usr/lib/python3.12/site-packages/setuptools/tests/script-with
│                │                       │        -bom.py 
│                │                       ├ [448]: usr/lib/python3.12/site-packages/setuptools/tests/test_archiv
│                │                       │        e_util.py 
│                │                       ├ [449]: usr/lib/python3.12/site-packages/setuptools/tests/test_bdist_
│                │                       │        deprecations.py 
│                │                       ├ [450]: usr/lib/python3.12/site-packages/setuptools/tests/test_bdist_
│                │                       │        egg.py 
│                │                       ├ [451]: usr/lib/python3.12/site-packages/setuptools/tests/test_bdist_
│                │                       │        wheel.py 
│                │                       ├ [452]: usr/lib/python3.12/site-packages/setuptools/tests/test_build.py 
│                │                       ├ [453]: usr/lib/python3.12/site-packages/setuptools/tests/test_build_
│                │                       │        clib.py 
│                │                       ├ [454]: usr/lib/python3.12/site-packages/setuptools/tests/test_build_
│                │                       │        ext.py 
│                │                       ├ [455]: usr/lib/python3.12/site-packages/setuptools/tests/test_build_
│                │                       │        meta.py 
│                │                       ├ [456]: usr/lib/python3.12/site-packages/setuptools/tests/test_build_
│                │                       │        py.py 
│                │                       ├ [457]: usr/lib/python3.12/site-packages/setuptools/tests/test_config
│                │                       │        _discovery.py 
│                │                       ├ [458]: usr/lib/python3.12/site-packages/setuptools/tests/test_core_m
│                │                       │        etadata.py 
│                │                       ├ [459]: usr/lib/python3.12/site-packages/setuptools/tests/test_depend
│                │                       │        s.py 
│                │                       ├ [460]: usr/lib/python3.12/site-packages/setuptools/tests/test_develo
│                │                       │        p.py 
│                │                       ├ [461]: usr/lib/python3.12/site-packages/setuptools/tests/test_dist.py 
│                │                       ├ [462]: usr/lib/python3.12/site-packages/setuptools/tests/test_dist_i
│                │                       │        nfo.py 
│                │                       ├ [463]: usr/lib/python3.12/site-packages/setuptools/tests/test_distut
│                │                       │        ils_adoption.py 
│                │                       ├ [464]: usr/lib/python3.12/site-packages/setuptools/tests/test_editab
│                │                       │        le_install.py 
│                │                       ├ [465]: usr/lib/python3.12/site-packages/setuptools/tests/test_egg_in
│                │                       │        fo.py 
│                │                       ├ [466]: usr/lib/python3.12/site-packages/setuptools/tests/test_extern
│                │                       │        .py 
│                │                       ├ [467]: usr/lib/python3.12/site-packages/setuptools/tests/test_find_p
│                │                       │        ackages.py 
│                │                       ├ [468]: usr/lib/python3.12/site-packages/setuptools/tests/test_find_p
│                │                       │        y_modules.py 
│                │                       ├ [469]: usr/lib/python3.12/site-packages/setuptools/tests/test_glob.py 
│                │                       ├ [470]: usr/lib/python3.12/site-packages/setuptools/tests/test_instal
│                │                       │        l_scripts.py 
│                │                       ├ [471]: usr/lib/python3.12/site-packages/setuptools/tests/test_loggin
│                │                       │        g.py 
│                │                       ├ [472]: usr/lib/python3.12/site-packages/setuptools/tests/test_manife
│                │                       │        st.py 
│                │                       ├ [473]: usr/lib/python3.12/site-packages/setuptools/tests/test_namesp
│                │                       │        aces.py 
│                │                       ├ [474]: usr/lib/python3.12/site-packages/setuptools/tests/test_script
│                │                       │        s.py 
│                │                       ├ [475]: usr/lib/python3.12/site-packages/setuptools/tests/test_sdist.py 
│                │                       ├ [476]: usr/lib/python3.12/site-packages/setuptools/tests/test_setopt
│                │                       │        .py 
│                │                       ├ [477]: usr/lib/python3.12/site-packages/setuptools/tests/test_setupt
│                │                       │        ools.py 
│                │                       ├ [478]: usr/lib/python3.12/site-packages/setuptools/tests/test_shutil
│                │                       │        _wrapper.py 
│                │                       ├ [479]: usr/lib/python3.12/site-packages/setuptools/tests/test_unicod
│                │                       │        e_utils.py 
│                │                       ├ [480]: usr/lib/python3.12/site-packages/setuptools/tests/test_virtua
│                │                       │        lenv.py 
│                │                       ├ [481]: usr/lib/python3.12/site-packages/setuptools/tests/test_warnin
│                │                       │        gs.py 
│                │                       ├ [482]: usr/lib/python3.12/site-packages/setuptools/tests/test_wheel.py 
│                │                       ├ [483]: usr/lib/python3.12/site-packages/setuptools/tests/test_window
│                │                       │        s_wrappers.py 
│                │                       ├ [484]: usr/lib/python3.12/site-packages/setuptools/tests/text.py 
│                │                       ├ [485]: usr/lib/python3.12/site-packages/setuptools/tests/textwrap.py 
│                │                       ├ [486]: usr/lib/python3.12/site-packages/setuptools/tests/compat/__in
│                │                       │        it__.py 
│                │                       ├ [487]: usr/lib/python3.12/site-packages/setuptools/tests/compat/py39
│                │                       │        .py 
│                │                       ├ [488]: usr/lib/python3.12/site-packages/setuptools/tests/config/__in
│                │                       │        it__.py 
│                │                       ├ [489]: usr/lib/python3.12/site-packages/setuptools/tests/config/setu
│                │                       │        pcfg_examples.txt 
│                │                       ├ [490]: usr/lib/python3.12/site-packages/setuptools/tests/config/test
│                │                       │        _apply_pyprojecttoml.py 
│                │                       ├ [491]: usr/lib/python3.12/site-packages/setuptools/tests/config/test
│                │                       │        _expand.py 
│                │                       ├ [492]: usr/lib/python3.12/site-packages/setuptools/tests/config/test
│                │                       │        _pyprojecttoml.py 
│                │                       ├ [493]: usr/lib/python3.12/site-packages/setuptools/tests/config/test
│                │                       │        _pyprojecttoml_dynamic_deps.py 
│                │                       ├ [494]: usr/lib/python3.12/site-packages/setuptools/tests/config/test
│                │                       │        _setupcfg.py 
│                │                       ├ [495]: usr/lib/python3.12/site-packages/setuptools/tests/config/down
│                │                       │        loads/__init__.py 
│                │                       ├ [496]: usr/lib/python3.12/site-packages/setuptools/tests/config/down
│                │                       │        loads/preload.py 
│                │                       ├ [497]: usr/lib/python3.12/site-packages/setuptools/tests/indexes/tes
│                │                       │        t_links_priority/external.html 
│                │                       ├ [498]: usr/lib/python3.12/site-packages/setuptools/tests/indexes/tes
│                │                       │        t_links_priority/simple/foobar/index.html 
│                │                       ├ [499]: usr/lib/python3.12/site-packages/setuptools/tests/integration
│                │                       │        /__init__.py 
│                │                       ├ [500]: usr/lib/python3.12/site-packages/setuptools/tests/integration
│                │                       │        /helpers.py 
│                │                       ├ [501]: usr/lib/python3.12/site-packages/setuptools/tests/integration
│                │                       │        /test_pbr.py 
│                │                       ╰ [502]: usr/lib/python3.12/site-packages/setuptools/tests/integration
│                │                                /test_pip_install_sdist.py 
│                ├ [64] ╭ ID            : py3-setuptools-pyc@80.9.0-r2 
│                │      ├ Name          : py3-setuptools-pyc 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/py3-setuptools-pyc@80.9.0-r2?arch=x86_64&distro
│                │      │                │       =3.23.2 
│                │      │                ╰ UID : a4e313db87a12dd3 
│                │      ├ Version       : 80.9.0-r2 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : py3-setuptools 
│                │      ├ SrcVersion    : 80.9.0-r2 
│                │      ├ Licenses       ─ [0]: MIT 
│                │      ├ Maintainer    : Achill Gilgenast <achill@achill.org> 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:3a598640236f6e8ec99f670f4a5cb4cb4bfdd233 
│                │      ╰ InstalledFiles ╭ [0]  : usr/lib/python3.12/site-packages/_distutils_hack/__pycache__/
│                │                       │        __init__.cpython-312.pyc 
│                │                       ├ [1]  : usr/lib/python3.12/site-packages/_distutils_hack/__pycache__/
│                │                       │        override.cpython-312.pyc 
│                │                       ├ [2]  : usr/lib/python3.12/site-packages/pkg_resources/__pycache__/__
│                │                       │        init__.cpython-312.pyc 
│                │                       ├ [3]  : usr/lib/python3.12/site-packages/pkg_resources/tests/__pycach
│                │                       │        e__/__init__.cpython-312.pyc 
│                │                       ├ [4]  : usr/lib/python3.12/site-packages/pkg_resources/tests/__pycach
│                │                       │        e__/test_find_distributions.cpython-312.pyc 
│                │                       ├ [5]  : usr/lib/python3.12/site-packages/pkg_resources/tests/__pycach
│                │                       │        e__/test_integration_zope_interface.cpython-312.pyc 
│                │                       ├ [6]  : usr/lib/python3.12/site-packages/pkg_resources/tests/__pycach
│                │                       │        e__/test_markers.cpython-312.pyc 
│                │                       ├ [7]  : usr/lib/python3.12/site-packages/pkg_resources/tests/__pycach
│                │                       │        e__/test_pkg_resources.cpython-312.pyc 
│                │                       ├ [8]  : usr/lib/python3.12/site-packages/pkg_resources/tests/__pycach
│                │                       │        e__/test_resources.cpython-312.pyc 
│                │                       ├ [9]  : usr/lib/python3.12/site-packages/pkg_resources/tests/__pycach
│                │                       │        e__/test_working_set.cpython-312.pyc 
│                │                       ├ [10] : usr/lib/python3.12/site-packages/pkg_resources/tests/data/my-
│                │                       │        test-package-source/__pycache__/setup.cpython-312.pyc 
│                │                       ├ [11] : usr/lib/python3.12/site-packages/setuptools/__pycache__/__ini
│                │                       │        t__.cpython-312.pyc 
│                │                       ├ [12] : usr/lib/python3.12/site-packages/setuptools/__pycache__/_core
│                │                       │        _metadata.cpython-312.pyc 
│                │                       ├ [13] : usr/lib/python3.12/site-packages/setuptools/__pycache__/_disc
│                │                       │        overy.cpython-312.pyc 
│                │                       ├ [14] : usr/lib/python3.12/site-packages/setuptools/__pycache__/_entr
│                │                       │        y_points.cpython-312.pyc 
│                │                       ├ [15] : usr/lib/python3.12/site-packages/setuptools/__pycache__/_imp.
│                │                       │        cpython-312.pyc 
│                │                       ├ [16] : usr/lib/python3.12/site-packages/setuptools/__pycache__/_impo
│                │                       │        rtlib.cpython-312.pyc 
│                │                       ├ [17] : usr/lib/python3.12/site-packages/setuptools/__pycache__/_iter
│                │                       │        tools.cpython-312.pyc 
│                │                       ├ [18] : usr/lib/python3.12/site-packages/setuptools/__pycache__/_norm
│                │                       │        alization.cpython-312.pyc 
│                │                       ├ [19] : usr/lib/python3.12/site-packages/setuptools/__pycache__/_path
│                │                       │        .cpython-312.pyc 
│                │                       ├ [20] : usr/lib/python3.12/site-packages/setuptools/__pycache__/_reqs
│                │                       │        .cpython-312.pyc 
│                │                       ├ [21] : usr/lib/python3.12/site-packages/setuptools/__pycache__/_scri
│                │                       │        pts.cpython-312.pyc 
│                │                       ├ [22] : usr/lib/python3.12/site-packages/setuptools/__pycache__/_shut
│                │                       │        il.cpython-312.pyc 
│                │                       ├ [23] : usr/lib/python3.12/site-packages/setuptools/__pycache__/_stat
│                │                       │        ic.cpython-312.pyc 
│                │                       ├ [24] : usr/lib/python3.12/site-packages/setuptools/__pycache__/archi
│                │                       │        ve_util.cpython-312.pyc 
│                │                       ├ [25] : usr/lib/python3.12/site-packages/setuptools/__pycache__/build
│                │                       │        _meta.cpython-312.pyc 
│                │                       ├ [26] : usr/lib/python3.12/site-packages/setuptools/__pycache__/depen
│                │                       │        ds.cpython-312.pyc 
│                │                       ├ [27] : usr/lib/python3.12/site-packages/setuptools/__pycache__/disco
│                │                       │        very.cpython-312.pyc 
│                │                       ├ [28] : usr/lib/python3.12/site-packages/setuptools/__pycache__/dist.
│                │                       │        cpython-312.pyc 
│                │                       ├ [29] : usr/lib/python3.12/site-packages/setuptools/__pycache__/error
│                │                       │        s.cpython-312.pyc 
│                │                       ├ [30] : usr/lib/python3.12/site-packages/setuptools/__pycache__/exten
│                │                       │        sion.cpython-312.pyc 
│                │                       ├ [31] : usr/lib/python3.12/site-packages/setuptools/__pycache__/glob.
│                │                       │        cpython-312.pyc 
│                │                       ├ [32] : usr/lib/python3.12/site-packages/setuptools/__pycache__/insta
│                │                       │        ller.cpython-312.pyc 
│                │                       ├ [33] : usr/lib/python3.12/site-packages/setuptools/__pycache__/launc
│                │                       │        h.cpython-312.pyc 
│                │                       ├ [34] : usr/lib/python3.12/site-packages/setuptools/__pycache__/loggi
│                │                       │        ng.cpython-312.pyc 
│                │                       ├ [35] : usr/lib/python3.12/site-packages/setuptools/__pycache__/modif
│                │                       │        ied.cpython-312.pyc 
│                │                       ├ [36] : usr/lib/python3.12/site-packages/setuptools/__pycache__/monke
│                │                       │        y.cpython-312.pyc 
│                │                       ├ [37] : usr/lib/python3.12/site-packages/setuptools/__pycache__/msvc.
│                │                       │        cpython-312.pyc 
│                │                       ├ [38] : usr/lib/python3.12/site-packages/setuptools/__pycache__/names
│                │                       │        paces.cpython-312.pyc 
│                │                       ├ [39] : usr/lib/python3.12/site-packages/setuptools/__pycache__/unico
│                │                       │        de_utils.cpython-312.pyc 
│                │                       ├ [40] : usr/lib/python3.12/site-packages/setuptools/__pycache__/versi
│                │                       │        on.cpython-312.pyc 
│                │                       ├ [41] : usr/lib/python3.12/site-packages/setuptools/__pycache__/warni
│                │                       │        ngs.cpython-312.pyc 
│                │                       ├ [42] : usr/lib/python3.12/site-packages/setuptools/__pycache__/wheel
│                │                       │        .cpython-312.pyc 
│                │                       ├ [43] : usr/lib/python3.12/site-packages/setuptools/__pycache__/windo
│                │                       │        ws_support.cpython-312.pyc 
│                │                       ├ [44] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/__init__.cpython-312.pyc 
│                │                       ├ [45] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/_log.cpython-312.pyc 
│                │                       ├ [46] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/_macos_compat.cpython-312.pyc 
│                │                       ├ [47] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/_modified.cpython-312.pyc 
│                │                       ├ [48] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/_msvccompiler.cpython-312.pyc 
│                │                       ├ [49] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/archive_util.cpython-312.pyc 
│                │                       ├ [50] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/ccompiler.cpython-312.pyc 
│                │                       ├ [51] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/cmd.cpython-312.pyc 
│                │                       ├ [52] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/core.cpython-312.pyc 
│                │                       ├ [53] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/cygwinccompiler.cpython-312.pyc 
│                │                       ├ [54] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/debug.cpython-312.pyc 
│                │                       ├ [55] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/dep_util.cpython-312.pyc 
│                │                       ├ [56] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/dir_util.cpython-312.pyc 
│                │                       ├ [57] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/dist.cpython-312.pyc 
│                │                       ├ [58] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/errors.cpython-312.pyc 
│                │                       ├ [59] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/extension.cpython-312.pyc 
│                │                       ├ [60] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/fancy_getopt.cpython-312.pyc 
│                │                       ├ [61] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/file_util.cpython-312.pyc 
│                │                       ├ [62] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/filelist.cpython-312.pyc 
│                │                       ├ [63] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/log.cpython-312.pyc 
│                │                       ├ [64] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/spawn.cpython-312.pyc 
│                │                       ├ [65] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/sysconfig.cpython-312.pyc 
│                │                       ├ [66] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/text_file.cpython-312.pyc 
│                │                       ├ [67] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/unixccompiler.cpython-312.pyc 
│                │                       ├ [68] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/util.cpython-312.pyc 
│                │                       ├ [69] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/version.cpython-312.pyc 
│                │                       ├ [70] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/versionpredicate.cpython-312.pyc 
│                │                       ├ [71] : usr/lib/python3.12/site-packages/setuptools/_distutils/__pyca
│                │                       │        che__/zosccompiler.cpython-312.pyc 
│                │                       ├ [72] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [73] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/_framework_compat.cpython-312.pyc 
│                │                       ├ [74] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/bdist.cpython-312.pyc 
│                │                       ├ [75] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/bdist_dumb.cpython-312.pyc 
│                │                       ├ [76] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/bdist_rpm.cpython-312.pyc 
│                │                       ├ [77] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/build.cpython-312.pyc 
│                │                       ├ [78] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/build_clib.cpython-312.pyc 
│                │                       ├ [79] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/build_ext.cpython-312.pyc 
│                │                       ├ [80] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/build_py.cpython-312.pyc 
│                │                       ├ [81] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/build_scripts.cpython-312.pyc 
│                │                       ├ [82] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/check.cpython-312.pyc 
│                │                       ├ [83] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/clean.cpython-312.pyc 
│                │                       ├ [84] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/config.cpython-312.pyc 
│                │                       ├ [85] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/install.cpython-312.pyc 
│                │                       ├ [86] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/install_data.cpython-312.pyc 
│                │                       ├ [87] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/install_egg_info.cpython-312.pyc 
│                │                       ├ [88] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/install_headers.cpython-312.pyc 
│                │                       ├ [89] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/install_lib.cpython-312.pyc 
│                │                       ├ [90] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/install_scripts.cpython-312.pyc 
│                │                       ├ [91] : usr/lib/python3.12/site-packages/setuptools/_distutils/comman
│                │                       │        d/__pycache__/sdist.cpython-312.pyc 
│                │                       ├ [92] : usr/lib/python3.12/site-packages/setuptools/_distutils/compat
│                │                       │        /__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [93] : usr/lib/python3.12/site-packages/setuptools/_distutils/compat
│                │                       │        /__pycache__/numpy.cpython-312.pyc 
│                │                       ├ [94] : usr/lib/python3.12/site-packages/setuptools/_distutils/compat
│                │                       │        /__pycache__/py39.cpython-312.pyc 
│                │                       ├ [95] : usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/__pycache__/base.cpython-312.pyc 
│                │                       ├ [96] : usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/__pycache__/cygwin.cpython-312.pyc 
│                │                       ├ [97] : usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/__pycache__/errors.cpython-312.pyc 
│                │                       ├ [98] : usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/__pycache__/msvc.cpython-312.pyc 
│                │                       ├ [99] : usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/__pycache__/unix.cpython-312.pyc 
│                │                       ├ [100]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/__pycache__/zos.cpython-312.pyc 
│                │                       ├ [101]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/tests/__pycache__/test_base.cpython-312.pyc 
│                │                       ├ [102]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/tests/__pycache__/test_cygwin.cpython-312.pyc 
│                │                       ├ [103]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/tests/__pycache__/test_mingw.cpython-312.pyc 
│                │                       ├ [104]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/tests/__pycache__/test_msvc.cpython-312.pyc 
│                │                       ├ [105]: usr/lib/python3.12/site-packages/setuptools/_distutils/compil
│                │                       │        ers/C/tests/__pycache__/test_unix.cpython-312.pyc 
│                │                       ├ [106]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/__init__.cpython-312.pyc 
│                │                       ├ [107]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/support.cpython-312.pyc 
│                │                       ├ [108]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_archive_util.cpython-312.pyc 
│                │                       ├ [109]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_bdist.cpython-312.pyc 
│                │                       ├ [110]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_bdist_dumb.cpython-312.pyc 
│                │                       ├ [111]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_bdist_rpm.cpython-312.pyc 
│                │                       ├ [112]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_build.cpython-312.pyc 
│                │                       ├ [113]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_build_clib.cpython-312.pyc 
│                │                       ├ [114]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_build_ext.cpython-312.pyc 
│                │                       ├ [115]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_build_py.cpython-312.pyc 
│                │                       ├ [116]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_build_scripts.cpython-312.pyc 
│                │                       ├ [117]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_check.cpython-312.pyc 
│                │                       ├ [118]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_clean.cpython-312.pyc 
│                │                       ├ [119]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_cmd.cpython-312.pyc 
│                │                       ├ [120]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_config_cmd.cpython-312.pyc 
│                │                       ├ [121]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_core.cpython-312.pyc 
│                │                       ├ [122]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_dir_util.cpython-312.pyc 
│                │                       ├ [123]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_dist.cpython-312.pyc 
│                │                       ├ [124]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_extension.cpython-312.pyc 
│                │                       ├ [125]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_file_util.cpython-312.pyc 
│                │                       ├ [126]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_filelist.cpython-312.pyc 
│                │                       ├ [127]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_install.cpython-312.pyc 
│                │                       ├ [128]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_install_data.cpython-312.pyc 
│                │                       ├ [129]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_install_headers.cpython-312.pyc 
│                │                       ├ [130]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_install_lib.cpython-312.pyc 
│                │                       ├ [131]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_install_scripts.cpython-312.pyc 
│                │                       ├ [132]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_log.cpython-312.pyc 
│                │                       ├ [133]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_modified.cpython-312.pyc 
│                │                       ├ [134]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_sdist.cpython-312.pyc 
│                │                       ├ [135]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_spawn.cpython-312.pyc 
│                │                       ├ [136]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_sysconfig.cpython-312.pyc 
│                │                       ├ [137]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_text_file.cpython-312.pyc 
│                │                       ├ [138]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_util.cpython-312.pyc 
│                │                       ├ [139]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_version.cpython-312.pyc 
│                │                       ├ [140]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/test_versionpredicate.cpython-312.pyc 
│                │                       ├ [141]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        __pycache__/unix_compat.cpython-312.pyc 
│                │                       ├ [142]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        compat/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [143]: usr/lib/python3.12/site-packages/setuptools/_distutils/tests/
│                │                       │        compat/__pycache__/py39.cpython-312.pyc 
│                │                       ├ [144]: usr/lib/python3.12/site-packages/setuptools/_vendor/__pycache
│                │                       │        __/typing_extensions.cpython-312.pyc 
│                │                       ├ [145]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [146]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd/__pycache__/autoasync.cpython-312.pyc 
│                │                       ├ [147]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd/__pycache__/autocommand.cpython-312.pyc 
│                │                       ├ [148]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd/__pycache__/automain.cpython-312.pyc 
│                │                       ├ [149]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd/__pycache__/autoparse.cpython-312.pyc 
│                │                       ├ [150]: usr/lib/python3.12/site-packages/setuptools/_vendor/autocomma
│                │                       │        nd/__pycache__/errors.cpython-312.pyc 
│                │                       ├ [151]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        /__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [152]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        /tarfile/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [153]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        /tarfile/__pycache__/__main__.cpython-312.pyc 
│                │                       ├ [154]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        /tarfile/compat/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [155]: usr/lib/python3.12/site-packages/setuptools/_vendor/backports
│                │                       │        /tarfile/compat/__pycache__/py38.cpython-312.pyc 
│                │                       ├ [156]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [157]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/__pycache__/_adapters.cpython-312.pyc 
│                │                       ├ [158]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/__pycache__/_collections.cpython-312.pyc 
│                │                       ├ [159]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/__pycache__/_compat.cpython-312.pyc 
│                │                       ├ [160]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/__pycache__/_functools.cpython-312.pyc 
│                │                       ├ [161]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/__pycache__/_itertools.cpython-312.pyc 
│                │                       ├ [162]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/__pycache__/_meta.cpython-312.pyc 
│                │                       ├ [163]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/__pycache__/_text.cpython-312.pyc 
│                │                       ├ [164]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/__pycache__/diagnose.cpython-312.pyc 
│                │                       ├ [165]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/compat/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [166]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/compat/__pycache__/py311.cpython-312.pyc 
│                │                       ├ [167]: usr/lib/python3.12/site-packages/setuptools/_vendor/importlib
│                │                       │        _metadata/compat/__pycache__/py39.cpython-312.pyc 
│                │                       ├ [168]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect/_
│                │                       │        _pycache__/__init__.cpython-312.pyc 
│                │                       ├ [169]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect/c
│                │                       │        ompat/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [170]: usr/lib/python3.12/site-packages/setuptools/_vendor/inflect/c
│                │                       │        ompat/__pycache__/py38.cpython-312.pyc 
│                │                       ├ [171]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/__
│                │                       │        pycache__/context.cpython-312.pyc 
│                │                       ├ [172]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/co
│                │                       │        llections/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [173]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/fu
│                │                       │        nctools/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [174]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [175]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/__pycache__/layouts.cpython-312.pyc 
│                │                       ├ [176]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/__pycache__/show-newlines.cpython-312.pyc 
│                │                       ├ [177]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/__pycache__/strip-prefix.cpython-312.pyc 
│                │                       ├ [178]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/__pycache__/to-dvorak.cpython-312.pyc 
│                │                       ├ [179]: usr/lib/python3.12/site-packages/setuptools/_vendor/jaraco/te
│                │                       │        xt/__pycache__/to-qwerty.cpython-312.pyc 
│                │                       ├ [180]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [181]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools/__pycache__/more.cpython-312.pyc 
│                │                       ├ [182]: usr/lib/python3.12/site-packages/setuptools/_vendor/more_iter
│                │                       │        tools/__pycache__/recipes.cpython-312.pyc 
│                │                       ├ [183]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [184]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/_elffile.cpython-312.pyc 
│                │                       ├ [185]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/_manylinux.cpython-312.pyc 
│                │                       ├ [186]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/_musllinux.cpython-312.pyc 
│                │                       ├ [187]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/_parser.cpython-312.pyc 
│                │                       ├ [188]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/_structures.cpython-312.pyc 
│                │                       ├ [189]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/_tokenizer.cpython-312.pyc 
│                │                       ├ [190]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/markers.cpython-312.pyc 
│                │                       ├ [191]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/metadata.cpython-312.pyc 
│                │                       ├ [192]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/requirements.cpython-312.pyc 
│                │                       ├ [193]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/specifiers.cpython-312.pyc 
│                │                       ├ [194]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/tags.cpython-312.pyc 
│                │                       ├ [195]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/utils.cpython-312.pyc 
│                │                       ├ [196]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /__pycache__/version.cpython-312.pyc 
│                │                       ├ [197]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /licenses/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [198]: usr/lib/python3.12/site-packages/setuptools/_vendor/packaging
│                │                       │        /licenses/__pycache__/_spdx.cpython-312.pyc 
│                │                       ├ [199]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [200]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/__pycache__/__main__.cpython-312.pyc 
│                │                       ├ [201]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/__pycache__/android.cpython-312.pyc 
│                │                       ├ [202]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/__pycache__/api.cpython-312.pyc 
│                │                       ├ [203]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/__pycache__/macos.cpython-312.pyc 
│                │                       ├ [204]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/__pycache__/unix.cpython-312.pyc 
│                │                       ├ [205]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/__pycache__/version.cpython-312.pyc 
│                │                       ├ [206]: usr/lib/python3.12/site-packages/setuptools/_vendor/platformd
│                │                       │        irs/__pycache__/windows.cpython-312.pyc 
│                │                       ├ [207]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli/__p
│                │                       │        ycache__/__init__.cpython-312.pyc 
│                │                       ├ [208]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli/__p
│                │                       │        ycache__/_parser.cpython-312.pyc 
│                │                       ├ [209]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli/__p
│                │                       │        ycache__/_re.cpython-312.pyc 
│                │                       ├ [210]: usr/lib/python3.12/site-packages/setuptools/_vendor/tomli/__p
│                │                       │        ycache__/_types.cpython-312.pyc 
│                │                       ├ [211]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [212]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/_checkers.cpython-312.pyc 
│                │                       ├ [213]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/_config.cpython-312.pyc 
│                │                       ├ [214]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/_decorators.cpython-312.pyc 
│                │                       ├ [215]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/_exceptions.cpython-312.pyc 
│                │                       ├ [216]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/_functions.cpython-312.pyc 
│                │                       ├ [217]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/_importhook.cpython-312.pyc 
│                │                       ├ [218]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/_memo.cpython-312.pyc 
│                │                       ├ [219]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/_pytest_plugin.cpython-312.pyc 
│                │                       ├ [220]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/_suppression.cpython-312.pyc 
│                │                       ├ [221]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/_transformer.cpython-312.pyc 
│                │                       ├ [222]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/_union_transformer.cpython-312.pyc 
│                │                       ├ [223]: usr/lib/python3.12/site-packages/setuptools/_vendor/typeguard
│                │                       │        /__pycache__/_utils.cpython-312.pyc 
│                │                       ├ [224]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/__p
│                │                       │        ycache__/__init__.cpython-312.pyc 
│                │                       ├ [225]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/__p
│                │                       │        ycache__/__main__.cpython-312.pyc 
│                │                       ├ [226]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/__p
│                │                       │        ycache__/_bdist_wheel.cpython-312.pyc 
│                │                       ├ [227]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/__p
│                │                       │        ycache__/_setuptools_logging.cpython-312.pyc 
│                │                       ├ [228]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/__p
│                │                       │        ycache__/bdist_wheel.cpython-312.pyc 
│                │                       ├ [229]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/__p
│                │                       │        ycache__/macosx_libfile.cpython-312.pyc 
│                │                       ├ [230]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/__p
│                │                       │        ycache__/metadata.cpython-312.pyc 
│                │                       ├ [231]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/__p
│                │                       │        ycache__/util.cpython-312.pyc 
│                │                       ├ [232]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/__p
│                │                       │        ycache__/wheelfile.cpython-312.pyc 
│                │                       ├ [233]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/cli
│                │                       │        /__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [234]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/cli
│                │                       │        /__pycache__/convert.cpython-312.pyc 
│                │                       ├ [235]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/cli
│                │                       │        /__pycache__/pack.cpython-312.pyc 
│                │                       ├ [236]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/cli
│                │                       │        /__pycache__/tags.cpython-312.pyc 
│                │                       ├ [237]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/cli
│                │                       │        /__pycache__/unpack.cpython-312.pyc 
│                │                       ├ [238]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [239]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [240]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/_elffile.cpython-312.pyc 
│                │                       ├ [241]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/_manylinux.cpython-312.pyc 
│                │                       ├ [242]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/_musllinux.cpython-312.pyc 
│                │                       ├ [243]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/_parser.cpython-312.pyc 
│                │                       ├ [244]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/_structures.cpython-312.pyc 
│                │                       ├ [245]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/_tokenizer.cpython-312.pyc 
│                │                       ├ [246]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/markers.cpython-312.pyc 
│                │                       ├ [247]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/requirements.cpython-312.pyc 
│                │                       ├ [248]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/specifiers.cpython-312.pyc 
│                │                       ├ [249]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/tags.cpython-312.pyc 
│                │                       ├ [250]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/utils.cpython-312.pyc 
│                │                       ├ [251]: usr/lib/python3.12/site-packages/setuptools/_vendor/wheel/ven
│                │                       │        dored/packaging/__pycache__/version.cpython-312.pyc 
│                │                       ├ [252]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp/__py
│                │                       │        cache__/__init__.cpython-312.pyc 
│                │                       ├ [253]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp/__py
│                │                       │        cache__/glob.cpython-312.pyc 
│                │                       ├ [254]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp/comp
│                │                       │        at/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [255]: usr/lib/python3.12/site-packages/setuptools/_vendor/zipp/comp
│                │                       │        at/__pycache__/py310.cpython-312.pyc 
│                │                       ├ [256]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/__init__.cpython-312.pyc 
│                │                       ├ [257]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/_requirestxt.cpython-312.pyc 
│                │                       ├ [258]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/alias.cpython-312.pyc 
│                │                       ├ [259]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/bdist_egg.cpython-312.pyc 
│                │                       ├ [260]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/bdist_rpm.cpython-312.pyc 
│                │                       ├ [261]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/bdist_wheel.cpython-312.pyc 
│                │                       ├ [262]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/build.cpython-312.pyc 
│                │                       ├ [263]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/build_clib.cpython-312.pyc 
│                │                       ├ [264]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/build_ext.cpython-312.pyc 
│                │                       ├ [265]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/build_py.cpython-312.pyc 
│                │                       ├ [266]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/develop.cpython-312.pyc 
│                │                       ├ [267]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/dist_info.cpython-312.pyc 
│                │                       ├ [268]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/easy_install.cpython-312.pyc 
│                │                       ├ [269]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/editable_wheel.cpython-312.pyc 
│                │                       ├ [270]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/egg_info.cpython-312.pyc 
│                │                       ├ [271]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/install.cpython-312.pyc 
│                │                       ├ [272]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/install_egg_info.cpython-312.pyc 
│                │                       ├ [273]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/install_lib.cpython-312.pyc 
│                │                       ├ [274]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/install_scripts.cpython-312.pyc 
│                │                       ├ [275]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/rotate.cpython-312.pyc 
│                │                       ├ [276]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/saveopts.cpython-312.pyc 
│                │                       ├ [277]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/sdist.cpython-312.pyc 
│                │                       ├ [278]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/setopt.cpython-312.pyc 
│                │                       ├ [279]: usr/lib/python3.12/site-packages/setuptools/command/__pycache
│                │                       │        __/test.cpython-312.pyc 
│                │                       ├ [280]: usr/lib/python3.12/site-packages/setuptools/compat/__pycache_
│                │                       │        _/__init__.cpython-312.pyc 
│                │                       ├ [281]: usr/lib/python3.12/site-packages/setuptools/compat/__pycache_
│                │                       │        _/py310.cpython-312.pyc 
│                │                       ├ [282]: usr/lib/python3.12/site-packages/setuptools/compat/__pycache_
│                │                       │        _/py311.cpython-312.pyc 
│                │                       ├ [283]: usr/lib/python3.12/site-packages/setuptools/compat/__pycache_
│                │                       │        _/py312.cpython-312.pyc 
│                │                       ├ [284]: usr/lib/python3.12/site-packages/setuptools/compat/__pycache_
│                │                       │        _/py39.cpython-312.pyc 
│                │                       ├ [285]: usr/lib/python3.12/site-packages/setuptools/config/__pycache_
│                │                       │        _/__init__.cpython-312.pyc 
│                │                       ├ [286]: usr/lib/python3.12/site-packages/setuptools/config/__pycache_
│                │                       │        _/_apply_pyprojecttoml.cpython-312.pyc 
│                │                       ├ [287]: usr/lib/python3.12/site-packages/setuptools/config/__pycache_
│                │                       │        _/expand.cpython-312.pyc 
│                │                       ├ [288]: usr/lib/python3.12/site-packages/setuptools/config/__pycache_
│                │                       │        _/pyprojecttoml.cpython-312.pyc 
│                │                       ├ [289]: usr/lib/python3.12/site-packages/setuptools/config/__pycache_
│                │                       │        _/setupcfg.cpython-312.pyc 
│                │                       ├ [290]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [291]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/__pycache__/error_reporting.cpython-312.pyc 
│                │                       ├ [292]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/__pycache__/extra_validations.cpython-312.pyc 
│                │                       ├ [293]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/__pycache__/fastjsonschema_exceptions.cpython-312.p
│                │                       │        yc 
│                │                       ├ [294]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/__pycache__/fastjsonschema_validations.cpython-312.
│                │                       │        pyc 
│                │                       ├ [295]: usr/lib/python3.12/site-packages/setuptools/config/_validate_
│                │                       │        pyproject/__pycache__/formats.cpython-312.pyc 
│                │                       ├ [296]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /__init__.cpython-312.pyc 
│                │                       ├ [297]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /contexts.cpython-312.pyc 
│                │                       ├ [298]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /environment.cpython-312.pyc 
│                │                       ├ [299]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /fixtures.cpython-312.pyc 
│                │                       ├ [300]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /mod_with_constant.cpython-312.pyc 
│                │                       ├ [301]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /namespaces.cpython-312.pyc 
│                │                       ├ [302]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /script-with-bom.cpython-312.pyc 
│                │                       ├ [303]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_archive_util.cpython-312.pyc 
│                │                       ├ [304]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_bdist_deprecations.cpython-312.pyc 
│                │                       ├ [305]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_bdist_egg.cpython-312.pyc 
│                │                       ├ [306]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_bdist_wheel.cpython-312.pyc 
│                │                       ├ [307]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_build.cpython-312.pyc 
│                │                       ├ [308]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_build_clib.cpython-312.pyc 
│                │                       ├ [309]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_build_ext.cpython-312.pyc 
│                │                       ├ [310]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_build_meta.cpython-312.pyc 
│                │                       ├ [311]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_build_py.cpython-312.pyc 
│                │                       ├ [312]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_config_discovery.cpython-312.pyc 
│                │                       ├ [313]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_core_metadata.cpython-312.pyc 
│                │                       ├ [314]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_depends.cpython-312.pyc 
│                │                       ├ [315]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_develop.cpython-312.pyc 
│                │                       ├ [316]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_dist.cpython-312.pyc 
│                │                       ├ [317]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_dist_info.cpython-312.pyc 
│                │                       ├ [318]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_distutils_adoption.cpython-312.pyc 
│                │                       ├ [319]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_editable_install.cpython-312.pyc 
│                │                       ├ [320]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_egg_info.cpython-312.pyc 
│                │                       ├ [321]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_extern.cpython-312.pyc 
│                │                       ├ [322]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_find_packages.cpython-312.pyc 
│                │                       ├ [323]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_find_py_modules.cpython-312.pyc 
│                │                       ├ [324]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_glob.cpython-312.pyc 
│                │                       ├ [325]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_install_scripts.cpython-312.pyc 
│                │                       ├ [326]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_logging.cpython-312.pyc 
│                │                       ├ [327]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_manifest.cpython-312.pyc 
│                │                       ├ [328]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_namespaces.cpython-312.pyc 
│                │                       ├ [329]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_scripts.cpython-312.pyc 
│                │                       ├ [330]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_sdist.cpython-312.pyc 
│                │                       ├ [331]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_setopt.cpython-312.pyc 
│                │                       ├ [332]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_setuptools.cpython-312.pyc 
│                │                       ├ [333]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_shutil_wrapper.cpython-312.pyc 
│                │                       ├ [334]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_unicode_utils.cpython-312.pyc 
│                │                       ├ [335]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_virtualenv.cpython-312.pyc 
│                │                       ├ [336]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_warnings.cpython-312.pyc 
│                │                       ├ [337]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_wheel.cpython-312.pyc 
│                │                       ├ [338]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /test_windows_wrappers.cpython-312.pyc 
│                │                       ├ [339]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /text.cpython-312.pyc 
│                │                       ├ [340]: usr/lib/python3.12/site-packages/setuptools/tests/__pycache__
│                │                       │        /textwrap.cpython-312.pyc 
│                │                       ├ [341]: usr/lib/python3.12/site-packages/setuptools/tests/compat/__py
│                │                       │        cache__/__init__.cpython-312.pyc 
│                │                       ├ [342]: usr/lib/python3.12/site-packages/setuptools/tests/compat/__py
│                │                       │        cache__/py39.cpython-312.pyc 
│                │                       ├ [343]: usr/lib/python3.12/site-packages/setuptools/tests/config/__py
│                │                       │        cache__/__init__.cpython-312.pyc 
│                │                       ├ [344]: usr/lib/python3.12/site-packages/setuptools/tests/config/__py
│                │                       │        cache__/test_apply_pyprojecttoml.cpython-312.pyc 
│                │                       ├ [345]: usr/lib/python3.12/site-packages/setuptools/tests/config/__py
│                │                       │        cache__/test_expand.cpython-312.pyc 
│                │                       ├ [346]: usr/lib/python3.12/site-packages/setuptools/tests/config/__py
│                │                       │        cache__/test_pyprojecttoml.cpython-312.pyc 
│                │                       ├ [347]: usr/lib/python3.12/site-packages/setuptools/tests/config/__py
│                │                       │        cache__/test_pyprojecttoml_dynamic_deps.cpython-312.pyc 
│                │                       ├ [348]: usr/lib/python3.12/site-packages/setuptools/tests/config/__py
│                │                       │        cache__/test_setupcfg.cpython-312.pyc 
│                │                       ├ [349]: usr/lib/python3.12/site-packages/setuptools/tests/config/down
│                │                       │        loads/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [350]: usr/lib/python3.12/site-packages/setuptools/tests/config/down
│                │                       │        loads/__pycache__/preload.cpython-312.pyc 
│                │                       ├ [351]: usr/lib/python3.12/site-packages/setuptools/tests/integration
│                │                       │        /__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [352]: usr/lib/python3.12/site-packages/setuptools/tests/integration
│                │                       │        /__pycache__/helpers.cpython-312.pyc 
│                │                       ├ [353]: usr/lib/python3.12/site-packages/setuptools/tests/integration
│                │                       │        /__pycache__/test_pbr.cpython-312.pyc 
│                │                       ╰ [354]: usr/lib/python3.12/site-packages/setuptools/tests/integration
│                │                                /__pycache__/test_pip_install_sdist.cpython-312.pyc 
│                ├ [65] ╭ ID        : pyc@3.12.12-r0 
│                │      ├ Name      : pyc 
│                │      ├ Identifier ╭ PURL: pkg:apk/alpine/pyc@3.12.12-r0?arch=x86_64&distro=3.23.2 
│                │      │            ╰ UID : c065b5883abaf3cf 
│                │      ├ Version   : 3.12.12-r0 
│                │      ├ Arch      : x86_64 
│                │      ├ SrcName   : python3 
│                │      ├ SrcVersion: 3.12.12-r0 
│                │      ├ Licenses   ─ [0]: PSF-2.0 
│                │      ├ Maintainer: Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ Layer      ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335fa38
│                │      │            │         6e9e106 
│                │      │            ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cbad77
│                │      │                      07d9fbb 
│                │      ╰ Digest    : sha1:27188be1b985948860232f6887dcbd88f4c64381 
│                ├ [66] ╭ ID            : python3@3.12.12-r0 
│                │      ├ Name          : python3 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/python3@3.12.12-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : bce4904556c176df 
│                │      ├ Version       : 3.12.12-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : python3 
│                │      ├ SrcVersion    : 3.12.12-r0 
│                │      ├ Licenses       ─ [0]: PSF-2.0 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ╭ [0] : gdbm@1.26-r0 
│                │      │                ├ [1] : libbz2@1.0.8-r6 
│                │      │                ├ [2] : libcrypto3@3.5.4-r0 
│                │      │                ├ [3] : libexpat@2.7.3-r0 
│                │      │                ├ [4] : libffi@3.5.2-r0 
│                │      │                ├ [5] : libncursesw@6.5_p20251123-r0 
│                │      │                ├ [6] : libpanelw@6.5_p20251123-r0 
│                │      │                ├ [7] : libssl3@3.5.4-r0 
│                │      │                ├ [8] : mpdecimal@4.0.1-r0 
│                │      │                ├ [9] : musl@1.2.5-r21 
│                │      │                ├ [10]: readline@8.3.1-r0 
│                │      │                ├ [11]: sqlite-libs@3.51.1-r0 
│                │      │                ├ [12]: xz-libs@5.8.1-r0 
│                │      │                ╰ [13]: zlib@1.3.1-r2 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:314f6b1ea5d7da1aa23121ee7dc29bc4c565ac9b 
│                │      ╰ InstalledFiles ╭ [0]  : usr/bin/2to3 
│                │                       ├ [1]  : usr/bin/2to3-3.12 
│                │                       ├ [2]  : usr/bin/pydoc3 
│                │                       ├ [3]  : usr/bin/pydoc3.12 
│                │                       ├ [4]  : usr/bin/python 
│                │                       ├ [5]  : usr/bin/python3 
│                │                       ├ [6]  : usr/bin/python3.12 
│                │                       ├ [7]  : usr/include/python3.12/pyconfig.h 
│                │                       ├ [8]  : usr/lib/libpython3.12.so.1.0 
│                │                       ├ [9]  : usr/lib/libpython3.so 
│                │                       ├ [10] : usr/lib/python3.12/EXTERNALLY-MANAGED 
│                │                       ├ [11] : usr/lib/python3.12/LICENSE.txt 
│                │                       ├ [12] : usr/lib/python3.12/__future__.py 
│                │                       ├ [13] : usr/lib/python3.12/__hello__.py 
│                │                       ├ [14] : usr/lib/python3.12/_aix_support.py 
│                │                       ├ [15] : usr/lib/python3.12/_collections_abc.py 
│                │                       ├ [16] : usr/lib/python3.12/_compat_pickle.py 
│                │                       ├ [17] : usr/lib/python3.12/_compression.py 
│                │                       ├ [18] : usr/lib/python3.12/_markupbase.py 
│                │                       ├ [19] : usr/lib/python3.12/_osx_support.py 
│                │                       ├ [20] : usr/lib/python3.12/_py_abc.py 
│                │                       ├ [21] : usr/lib/python3.12/_pydatetime.py 
│                │                       ├ [22] : usr/lib/python3.12/_pydecimal.py 
│                │                       ├ [23] : usr/lib/python3.12/_pyio.py 
│                │                       ├ [24] : usr/lib/python3.12/_pylong.py 
│                │                       ├ [25] : usr/lib/python3.12/_sitebuiltins.py 
│                │                       ├ [26] : usr/lib/python3.12/_strptime.py 
│                │                       ├ [27] : usr/lib/python3.12/_sysconfigdata__linux_x86_64-linux-musl.py 
│                │                       ├ [28] : usr/lib/python3.12/_threading_local.py 
│                │                       ├ [29] : usr/lib/python3.12/_weakrefset.py 
│                │                       ├ [30] : usr/lib/python3.12/abc.py 
│                │                       ├ [31] : usr/lib/python3.12/aifc.py 
│                │                       ├ [32] : usr/lib/python3.12/antigravity.py 
│                │                       ├ [33] : usr/lib/python3.12/argparse.py 
│                │                       ├ [34] : usr/lib/python3.12/ast.py 
│                │                       ├ [35] : usr/lib/python3.12/base64.py 
│                │                       ├ [36] : usr/lib/python3.12/bdb.py 
│                │                       ├ [37] : usr/lib/python3.12/bisect.py 
│                │                       ├ [38] : usr/lib/python3.12/bz2.py 
│                │                       ├ [39] : usr/lib/python3.12/cProfile.py 
│                │                       ├ [40] : usr/lib/python3.12/calendar.py 
│                │                       ├ [41] : usr/lib/python3.12/cgi.py 
│                │                       ├ [42] : usr/lib/python3.12/cgitb.py 
│                │                       ├ [43] : usr/lib/python3.12/chunk.py 
│                │                       ├ [44] : usr/lib/python3.12/cmd.py 
│                │                       ├ [45] : usr/lib/python3.12/code.py 
│                │                       ├ [46] : usr/lib/python3.12/codecs.py 
│                │                       ├ [47] : usr/lib/python3.12/codeop.py 
│                │                       ├ [48] : usr/lib/python3.12/colorsys.py 
│                │                       ├ [49] : usr/lib/python3.12/compileall.py 
│                │                       ├ [50] : usr/lib/python3.12/configparser.py 
│                │                       ├ [51] : usr/lib/python3.12/contextlib.py 
│                │                       ├ [52] : usr/lib/python3.12/contextvars.py 
│                │                       ├ [53] : usr/lib/python3.12/copy.py 
│                │                       ├ [54] : usr/lib/python3.12/copyreg.py 
│                │                       ├ [55] : usr/lib/python3.12/crypt.py 
│                │                       ├ [56] : usr/lib/python3.12/csv.py 
│                │                       ├ [57] : usr/lib/python3.12/dataclasses.py 
│                │                       ├ [58] : usr/lib/python3.12/datetime.py 
│                │                       ├ [59] : usr/lib/python3.12/decimal.py 
│                │                       ├ [60] : usr/lib/python3.12/difflib.py 
│                │                       ├ [61] : usr/lib/python3.12/dis.py 
│                │                       ├ [62] : usr/lib/python3.12/doctest.py 
│                │                       ├ [63] : usr/lib/python3.12/enum.py 
│                │                       ├ [64] : usr/lib/python3.12/filecmp.py 
│                │                       ├ [65] : usr/lib/python3.12/fileinput.py 
│                │                       ├ [66] : usr/lib/python3.12/fnmatch.py 
│                │                       ├ [67] : usr/lib/python3.12/fractions.py 
│                │                       ├ [68] : usr/lib/python3.12/ftplib.py 
│                │                       ├ [69] : usr/lib/python3.12/functools.py 
│                │                       ├ [70] : usr/lib/python3.12/genericpath.py 
│                │                       ├ [71] : usr/lib/python3.12/getopt.py 
│                │                       ├ [72] : usr/lib/python3.12/getpass.py 
│                │                       ├ [73] : usr/lib/python3.12/gettext.py 
│                │                       ├ [74] : usr/lib/python3.12/glob.py 
│                │                       ├ [75] : usr/lib/python3.12/graphlib.py 
│                │                       ├ [76] : usr/lib/python3.12/gzip.py 
│                │                       ├ [77] : usr/lib/python3.12/hashlib.py 
│                │                       ├ [78] : usr/lib/python3.12/heapq.py 
│                │                       ├ [79] : usr/lib/python3.12/hmac.py 
│                │                       ├ [80] : usr/lib/python3.12/imaplib.py 
│                │                       ├ [81] : usr/lib/python3.12/imghdr.py 
│                │                       ├ [82] : usr/lib/python3.12/inspect.py 
│                │                       ├ [83] : usr/lib/python3.12/io.py 
│                │                       ├ [84] : usr/lib/python3.12/ipaddress.py 
│                │                       ├ [85] : usr/lib/python3.12/keyword.py 
│                │                       ├ [86] : usr/lib/python3.12/linecache.py 
│                │                       ├ [87] : usr/lib/python3.12/locale.py 
│                │                       ├ [88] : usr/lib/python3.12/lzma.py 
│                │                       ├ [89] : usr/lib/python3.12/mailbox.py 
│                │                       ├ [90] : usr/lib/python3.12/mailcap.py 
│                │                       ├ [91] : usr/lib/python3.12/mimetypes.py 
│                │                       ├ [92] : usr/lib/python3.12/modulefinder.py 
│                │                       ├ [93] : usr/lib/python3.12/netrc.py 
│                │                       ├ [94] : usr/lib/python3.12/nntplib.py 
│                │                       ├ [95] : usr/lib/python3.12/ntpath.py 
│                │                       ├ [96] : usr/lib/python3.12/nturl2path.py 
│                │                       ├ [97] : usr/lib/python3.12/numbers.py 
│                │                       ├ [98] : usr/lib/python3.12/opcode.py 
│                │                       ├ [99] : usr/lib/python3.12/operator.py 
│                │                       ├ [100]: usr/lib/python3.12/optparse.py 
│                │                       ├ [101]: usr/lib/python3.12/os.py 
│                │                       ├ [102]: usr/lib/python3.12/pathlib.py 
│                │                       ├ [103]: usr/lib/python3.12/pdb.py 
│                │                       ├ [104]: usr/lib/python3.12/pickle.py 
│                │                       ├ [105]: usr/lib/python3.12/pickletools.py 
│                │                       ├ [106]: usr/lib/python3.12/pipes.py 
│                │                       ├ [107]: usr/lib/python3.12/pkgutil.py 
│                │                       ├ [108]: usr/lib/python3.12/platform.py 
│                │                       ├ [109]: usr/lib/python3.12/plistlib.py 
│                │                       ├ [110]: usr/lib/python3.12/poplib.py 
│                │                       ├ [111]: usr/lib/python3.12/posixpath.py 
│                │                       ├ [112]: usr/lib/python3.12/pprint.py 
│                │                       ├ [113]: usr/lib/python3.12/profile.py 
│                │                       ├ [114]: usr/lib/python3.12/pstats.py 
│                │                       ├ [115]: usr/lib/python3.12/pty.py 
│                │                       ├ [116]: usr/lib/python3.12/py_compile.py 
│                │                       ├ [117]: usr/lib/python3.12/pyclbr.py 
│                │                       ├ [118]: usr/lib/python3.12/pydoc.py 
│                │                       ├ [119]: usr/lib/python3.12/queue.py 
│                │                       ├ [120]: usr/lib/python3.12/quopri.py 
│                │                       ├ [121]: usr/lib/python3.12/random.py 
│                │                       ├ [122]: usr/lib/python3.12/reprlib.py 
│                │                       ├ [123]: usr/lib/python3.12/rlcompleter.py 
│                │                       ├ [124]: usr/lib/python3.12/runpy.py 
│                │                       ├ [125]: usr/lib/python3.12/sched.py 
│                │                       ├ [126]: usr/lib/python3.12/secrets.py 
│                │                       ├ [127]: usr/lib/python3.12/selectors.py 
│                │                       ├ [128]: usr/lib/python3.12/shelve.py 
│                │                       ├ [129]: usr/lib/python3.12/shlex.py 
│                │                       ├ [130]: usr/lib/python3.12/shutil.py 
│                │                       ├ [131]: usr/lib/python3.12/signal.py 
│                │                       ├ [132]: usr/lib/python3.12/site.py 
│                │                       ├ [133]: usr/lib/python3.12/smtplib.py 
│                │                       ├ [134]: usr/lib/python3.12/sndhdr.py 
│                │                       ├ [135]: usr/lib/python3.12/socket.py 
│                │                       ├ [136]: usr/lib/python3.12/socketserver.py 
│                │                       ├ [137]: usr/lib/python3.12/sre_compile.py 
│                │                       ├ [138]: usr/lib/python3.12/sre_constants.py 
│                │                       ├ [139]: usr/lib/python3.12/sre_parse.py 
│                │                       ├ [140]: usr/lib/python3.12/ssl.py 
│                │                       ├ [141]: usr/lib/python3.12/stat.py 
│                │                       ├ [142]: usr/lib/python3.12/statistics.py 
│                │                       ├ [143]: usr/lib/python3.12/string.py 
│                │                       ├ [144]: usr/lib/python3.12/stringprep.py 
│                │                       ├ [145]: usr/lib/python3.12/struct.py 
│                │                       ├ [146]: usr/lib/python3.12/subprocess.py 
│                │                       ├ [147]: usr/lib/python3.12/sunau.py 
│                │                       ├ [148]: usr/lib/python3.12/symtable.py 
│                │                       ├ [149]: usr/lib/python3.12/sysconfig.py 
│                │                       ├ [150]: usr/lib/python3.12/tabnanny.py 
│                │                       ├ [151]: usr/lib/python3.12/tarfile.py 
│                │                       ├ [152]: usr/lib/python3.12/telnetlib.py 
│                │                       ├ [153]: usr/lib/python3.12/tempfile.py 
│                │                       ├ [154]: usr/lib/python3.12/textwrap.py 
│                │                       ├ [155]: usr/lib/python3.12/this.py 
│                │                       ├ [156]: usr/lib/python3.12/threading.py 
│                │                       ├ [157]: usr/lib/python3.12/timeit.py 
│                │                       ├ [158]: usr/lib/python3.12/token.py 
│                │                       ├ [159]: usr/lib/python3.12/tokenize.py 
│                │                       ├ [160]: usr/lib/python3.12/trace.py 
│                │                       ├ [161]: usr/lib/python3.12/traceback.py 
│                │                       ├ [162]: usr/lib/python3.12/tracemalloc.py 
│                │                       ├ [163]: usr/lib/python3.12/tty.py 
│                │                       ├ [164]: usr/lib/python3.12/turtle.py 
│                │                       ├ [165]: usr/lib/python3.12/types.py 
│                │                       ├ [166]: usr/lib/python3.12/typing.py 
│                │                       ├ [167]: usr/lib/python3.12/uu.py 
│                │                       ├ [168]: usr/lib/python3.12/uuid.py 
│                │                       ├ [169]: usr/lib/python3.12/warnings.py 
│                │                       ├ [170]: usr/lib/python3.12/wave.py 
│                │                       ├ [171]: usr/lib/python3.12/weakref.py 
│                │                       ├ [172]: usr/lib/python3.12/webbrowser.py 
│                │                       ├ [173]: usr/lib/python3.12/xdrlib.py 
│                │                       ├ [174]: usr/lib/python3.12/zipapp.py 
│                │                       ├ [175]: usr/lib/python3.12/zipimport.py 
│                │                       ├ [176]: usr/lib/python3.12/__phello__/__init__.py 
│                │                       ├ [177]: usr/lib/python3.12/__phello__/spam.py 
│                │                       ├ [178]: usr/lib/python3.12/asyncio/__init__.py 
│                │                       ├ [179]: usr/lib/python3.12/asyncio/__main__.py 
│                │                       ├ [180]: usr/lib/python3.12/asyncio/base_events.py 
│                │                       ├ [181]: usr/lib/python3.12/asyncio/base_futures.py 
│                │                       ├ [182]: usr/lib/python3.12/asyncio/base_subprocess.py 
│                │                       ├ [183]: usr/lib/python3.12/asyncio/base_tasks.py 
│                │                       ├ [184]: usr/lib/python3.12/asyncio/constants.py 
│                │                       ├ [185]: usr/lib/python3.12/asyncio/coroutines.py 
│                │                       ├ [186]: usr/lib/python3.12/asyncio/events.py 
│                │                       ├ [187]: usr/lib/python3.12/asyncio/exceptions.py 
│                │                       ├ [188]: usr/lib/python3.12/asyncio/format_helpers.py 
│                │                       ├ [189]: usr/lib/python3.12/asyncio/futures.py 
│                │                       ├ [190]: usr/lib/python3.12/asyncio/locks.py 
│                │                       ├ [191]: usr/lib/python3.12/asyncio/log.py 
│                │                       ├ [192]: usr/lib/python3.12/asyncio/mixins.py 
│                │                       ├ [193]: usr/lib/python3.12/asyncio/proactor_events.py 
│                │                       ├ [194]: usr/lib/python3.12/asyncio/protocols.py 
│                │                       ├ [195]: usr/lib/python3.12/asyncio/queues.py 
│                │                       ├ [196]: usr/lib/python3.12/asyncio/runners.py 
│                │                       ├ [197]: usr/lib/python3.12/asyncio/selector_events.py 
│                │                       ├ [198]: usr/lib/python3.12/asyncio/sslproto.py 
│                │                       ├ [199]: usr/lib/python3.12/asyncio/staggered.py 
│                │                       ├ [200]: usr/lib/python3.12/asyncio/streams.py 
│                │                       ├ [201]: usr/lib/python3.12/asyncio/subprocess.py 
│                │                       ├ [202]: usr/lib/python3.12/asyncio/taskgroups.py 
│                │                       ├ [203]: usr/lib/python3.12/asyncio/tasks.py 
│                │                       ├ [204]: usr/lib/python3.12/asyncio/threads.py 
│                │                       ├ [205]: usr/lib/python3.12/asyncio/timeouts.py 
│                │                       ├ [206]: usr/lib/python3.12/asyncio/transports.py 
│                │                       ├ [207]: usr/lib/python3.12/asyncio/trsock.py 
│                │                       ├ [208]: usr/lib/python3.12/asyncio/unix_events.py 
│                │                       ├ [209]: usr/lib/python3.12/asyncio/windows_events.py 
│                │                       ├ [210]: usr/lib/python3.12/asyncio/windows_utils.py 
│                │                       ├ [211]: usr/lib/python3.12/collections/__init__.py 
│                │                       ├ [212]: usr/lib/python3.12/collections/abc.py 
│                │                       ├ [213]: usr/lib/python3.12/concurrent/__init__.py 
│                │                       ├ [214]: usr/lib/python3.12/concurrent/futures/__init__.py 
│                │                       ├ [215]: usr/lib/python3.12/concurrent/futures/_base.py 
│                │                       ├ [216]: usr/lib/python3.12/concurrent/futures/process.py 
│                │                       ├ [217]: usr/lib/python3.12/concurrent/futures/thread.py 
│                │                       ├ [218]: usr/lib/python3.12/config-3.12-x86_64-linux-musl/Makefile 
│                │                       ├ [219]: usr/lib/python3.12/config-3.12-x86_64-linux-musl/Setup 
│                │                       ├ [220]: usr/lib/python3.12/config-3.12-x86_64-linux-musl/Setup.bootst
│                │                       │        rap 
│                │                       ├ [221]: usr/lib/python3.12/config-3.12-x86_64-linux-musl/Setup.local 
│                │                       ├ [222]: usr/lib/python3.12/config-3.12-x86_64-linux-musl/Setup.stdlib 
│                │                       ├ [223]: usr/lib/python3.12/config-3.12-x86_64-linux-musl/config.c.in 
│                │                       ├ [224]: usr/lib/python3.12/config-3.12-x86_64-linux-musl/install-sh 
│                │                       ├ [225]: usr/lib/python3.12/config-3.12-x86_64-linux-musl/makesetup 
│                │                       ├ [226]: usr/lib/python3.12/config-3.12-x86_64-linux-musl/python-confi
│                │                       │        g.py 
│                │                       ├ [227]: usr/lib/python3.12/ctypes/__init__.py 
│                │                       ├ [228]: usr/lib/python3.12/ctypes/_aix.py 
│                │                       ├ [229]: usr/lib/python3.12/ctypes/_endian.py 
│                │                       ├ [230]: usr/lib/python3.12/ctypes/util.py 
│                │                       ├ [231]: usr/lib/python3.12/ctypes/wintypes.py 
│                │                       ├ [232]: usr/lib/python3.12/ctypes/macholib/README.ctypes 
│                │                       ├ [233]: usr/lib/python3.12/ctypes/macholib/__init__.py 
│                │                       ├ [234]: usr/lib/python3.12/ctypes/macholib/dyld.py 
│                │                       ├ [235]: usr/lib/python3.12/ctypes/macholib/dylib.py 
│                │                       ├ [236]: usr/lib/python3.12/ctypes/macholib/fetch_macholib 
│                │                       ├ [237]: usr/lib/python3.12/ctypes/macholib/fetch_macholib.bat 
│                │                       ├ [238]: usr/lib/python3.12/ctypes/macholib/framework.py 
│                │                       ├ [239]: usr/lib/python3.12/curses/__init__.py 
│                │                       ├ [240]: usr/lib/python3.12/curses/ascii.py 
│                │                       ├ [241]: usr/lib/python3.12/curses/has_key.py 
│                │                       ├ [242]: usr/lib/python3.12/curses/panel.py 
│                │                       ├ [243]: usr/lib/python3.12/curses/textpad.py 
│                │                       ├ [244]: usr/lib/python3.12/dbm/__init__.py 
│                │                       ├ [245]: usr/lib/python3.12/dbm/dumb.py 
│                │                       ├ [246]: usr/lib/python3.12/dbm/gnu.py 
│                │                       ├ [247]: usr/lib/python3.12/dbm/ndbm.py 
│                │                       ├ [248]: usr/lib/python3.12/email/__init__.py 
│                │                       ├ [249]: usr/lib/python3.12/email/_encoded_words.py 
│                │                       ├ [250]: usr/lib/python3.12/email/_header_value_parser.py 
│                │                       ├ [251]: usr/lib/python3.12/email/_parseaddr.py 
│                │                       ├ [252]: usr/lib/python3.12/email/_policybase.py 
│                │                       ├ [253]: usr/lib/python3.12/email/architecture.rst 
│                │                       ├ [254]: usr/lib/python3.12/email/base64mime.py 
│                │                       ├ [255]: usr/lib/python3.12/email/charset.py 
│                │                       ├ [256]: usr/lib/python3.12/email/contentmanager.py 
│                │                       ├ [257]: usr/lib/python3.12/email/encoders.py 
│                │                       ├ [258]: usr/lib/python3.12/email/errors.py 
│                │                       ├ [259]: usr/lib/python3.12/email/feedparser.py 
│                │                       ├ [260]: usr/lib/python3.12/email/generator.py 
│                │                       ├ [261]: usr/lib/python3.12/email/header.py 
│                │                       ├ [262]: usr/lib/python3.12/email/headerregistry.py 
│                │                       ├ [263]: usr/lib/python3.12/email/iterators.py 
│                │                       ├ [264]: usr/lib/python3.12/email/message.py 
│                │                       ├ [265]: usr/lib/python3.12/email/parser.py 
│                │                       ├ [266]: usr/lib/python3.12/email/policy.py 
│                │                       ├ [267]: usr/lib/python3.12/email/quoprimime.py 
│                │                       ├ [268]: usr/lib/python3.12/email/utils.py 
│                │                       ├ [269]: usr/lib/python3.12/email/mime/__init__.py 
│                │                       ├ [270]: usr/lib/python3.12/email/mime/application.py 
│                │                       ├ [271]: usr/lib/python3.12/email/mime/audio.py 
│                │                       ├ [272]: usr/lib/python3.12/email/mime/base.py 
│                │                       ├ [273]: usr/lib/python3.12/email/mime/image.py 
│                │                       ├ [274]: usr/lib/python3.12/email/mime/message.py 
│                │                       ├ [275]: usr/lib/python3.12/email/mime/multipart.py 
│                │                       ├ [276]: usr/lib/python3.12/email/mime/nonmultipart.py 
│                │                       ├ [277]: usr/lib/python3.12/email/mime/text.py 
│                │                       ├ [278]: usr/lib/python3.12/encodings/__init__.py 
│                │                       ├ [279]: usr/lib/python3.12/encodings/aliases.py 
│                │                       ├ [280]: usr/lib/python3.12/encodings/ascii.py 
│                │                       ├ [281]: usr/lib/python3.12/encodings/base64_codec.py 
│                │                       ├ [282]: usr/lib/python3.12/encodings/big5.py 
│                │                       ├ [283]: usr/lib/python3.12/encodings/big5hkscs.py 
│                │                       ├ [284]: usr/lib/python3.12/encodings/bz2_codec.py 
│                │                       ├ [285]: usr/lib/python3.12/encodings/charmap.py 
│                │                       ├ [286]: usr/lib/python3.12/encodings/cp037.py 
│                │                       ├ [287]: usr/lib/python3.12/encodings/cp1006.py 
│                │                       ├ [288]: usr/lib/python3.12/encodings/cp1026.py 
│                │                       ├ [289]: usr/lib/python3.12/encodings/cp1125.py 
│                │                       ├ [290]: usr/lib/python3.12/encodings/cp1140.py 
│                │                       ├ [291]: usr/lib/python3.12/encodings/cp1250.py 
│                │                       ├ [292]: usr/lib/python3.12/encodings/cp1251.py 
│                │                       ├ [293]: usr/lib/python3.12/encodings/cp1252.py 
│                │                       ├ [294]: usr/lib/python3.12/encodings/cp1253.py 
│                │                       ├ [295]: usr/lib/python3.12/encodings/cp1254.py 
│                │                       ├ [296]: usr/lib/python3.12/encodings/cp1255.py 
│                │                       ├ [297]: usr/lib/python3.12/encodings/cp1256.py 
│                │                       ├ [298]: usr/lib/python3.12/encodings/cp1257.py 
│                │                       ├ [299]: usr/lib/python3.12/encodings/cp1258.py 
│                │                       ├ [300]: usr/lib/python3.12/encodings/cp273.py 
│                │                       ├ [301]: usr/lib/python3.12/encodings/cp424.py 
│                │                       ├ [302]: usr/lib/python3.12/encodings/cp437.py 
│                │                       ├ [303]: usr/lib/python3.12/encodings/cp500.py 
│                │                       ├ [304]: usr/lib/python3.12/encodings/cp720.py 
│                │                       ├ [305]: usr/lib/python3.12/encodings/cp737.py 
│                │                       ├ [306]: usr/lib/python3.12/encodings/cp775.py 
│                │                       ├ [307]: usr/lib/python3.12/encodings/cp850.py 
│                │                       ├ [308]: usr/lib/python3.12/encodings/cp852.py 
│                │                       ├ [309]: usr/lib/python3.12/encodings/cp855.py 
│                │                       ├ [310]: usr/lib/python3.12/encodings/cp856.py 
│                │                       ├ [311]: usr/lib/python3.12/encodings/cp857.py 
│                │                       ├ [312]: usr/lib/python3.12/encodings/cp858.py 
│                │                       ├ [313]: usr/lib/python3.12/encodings/cp860.py 
│                │                       ├ [314]: usr/lib/python3.12/encodings/cp861.py 
│                │                       ├ [315]: usr/lib/python3.12/encodings/cp862.py 
│                │                       ├ [316]: usr/lib/python3.12/encodings/cp863.py 
│                │                       ├ [317]: usr/lib/python3.12/encodings/cp864.py 
│                │                       ├ [318]: usr/lib/python3.12/encodings/cp865.py 
│                │                       ├ [319]: usr/lib/python3.12/encodings/cp866.py 
│                │                       ├ [320]: usr/lib/python3.12/encodings/cp869.py 
│                │                       ├ [321]: usr/lib/python3.12/encodings/cp874.py 
│                │                       ├ [322]: usr/lib/python3.12/encodings/cp875.py 
│                │                       ├ [323]: usr/lib/python3.12/encodings/cp932.py 
│                │                       ├ [324]: usr/lib/python3.12/encodings/cp949.py 
│                │                       ├ [325]: usr/lib/python3.12/encodings/cp950.py 
│                │                       ├ [326]: usr/lib/python3.12/encodings/euc_jis_2004.py 
│                │                       ├ [327]: usr/lib/python3.12/encodings/euc_jisx0213.py 
│                │                       ├ [328]: usr/lib/python3.12/encodings/euc_jp.py 
│                │                       ├ [329]: usr/lib/python3.12/encodings/euc_kr.py 
│                │                       ├ [330]: usr/lib/python3.12/encodings/gb18030.py 
│                │                       ├ [331]: usr/lib/python3.12/encodings/gb2312.py 
│                │                       ├ [332]: usr/lib/python3.12/encodings/gbk.py 
│                │                       ├ [333]: usr/lib/python3.12/encodings/hex_codec.py 
│                │                       ├ [334]: usr/lib/python3.12/encodings/hp_roman8.py 
│                │                       ├ [335]: usr/lib/python3.12/encodings/hz.py 
│                │                       ├ [336]: usr/lib/python3.12/encodings/idna.py 
│                │                       ├ [337]: usr/lib/python3.12/encodings/iso2022_jp.py 
│                │                       ├ [338]: usr/lib/python3.12/encodings/iso2022_jp_1.py 
│                │                       ├ [339]: usr/lib/python3.12/encodings/iso2022_jp_2.py 
│                │                       ├ [340]: usr/lib/python3.12/encodings/iso2022_jp_2004.py 
│                │                       ├ [341]: usr/lib/python3.12/encodings/iso2022_jp_3.py 
│                │                       ├ [342]: usr/lib/python3.12/encodings/iso2022_jp_ext.py 
│                │                       ├ [343]: usr/lib/python3.12/encodings/iso2022_kr.py 
│                │                       ├ [344]: usr/lib/python3.12/encodings/iso8859_1.py 
│                │                       ├ [345]: usr/lib/python3.12/encodings/iso8859_10.py 
│                │                       ├ [346]: usr/lib/python3.12/encodings/iso8859_11.py 
│                │                       ├ [347]: usr/lib/python3.12/encodings/iso8859_13.py 
│                │                       ├ [348]: usr/lib/python3.12/encodings/iso8859_14.py 
│                │                       ├ [349]: usr/lib/python3.12/encodings/iso8859_15.py 
│                │                       ├ [350]: usr/lib/python3.12/encodings/iso8859_16.py 
│                │                       ├ [351]: usr/lib/python3.12/encodings/iso8859_2.py 
│                │                       ├ [352]: usr/lib/python3.12/encodings/iso8859_3.py 
│                │                       ├ [353]: usr/lib/python3.12/encodings/iso8859_4.py 
│                │                       ├ [354]: usr/lib/python3.12/encodings/iso8859_5.py 
│                │                       ├ [355]: usr/lib/python3.12/encodings/iso8859_6.py 
│                │                       ├ [356]: usr/lib/python3.12/encodings/iso8859_7.py 
│                │                       ├ [357]: usr/lib/python3.12/encodings/iso8859_8.py 
│                │                       ├ [358]: usr/lib/python3.12/encodings/iso8859_9.py 
│                │                       ├ [359]: usr/lib/python3.12/encodings/johab.py 
│                │                       ├ [360]: usr/lib/python3.12/encodings/koi8_r.py 
│                │                       ├ [361]: usr/lib/python3.12/encodings/koi8_t.py 
│                │                       ├ [362]: usr/lib/python3.12/encodings/koi8_u.py 
│                │                       ├ [363]: usr/lib/python3.12/encodings/kz1048.py 
│                │                       ├ [364]: usr/lib/python3.12/encodings/latin_1.py 
│                │                       ├ [365]: usr/lib/python3.12/encodings/mac_arabic.py 
│                │                       ├ [366]: usr/lib/python3.12/encodings/mac_croatian.py 
│                │                       ├ [367]: usr/lib/python3.12/encodings/mac_cyrillic.py 
│                │                       ├ [368]: usr/lib/python3.12/encodings/mac_farsi.py 
│                │                       ├ [369]: usr/lib/python3.12/encodings/mac_greek.py 
│                │                       ├ [370]: usr/lib/python3.12/encodings/mac_iceland.py 
│                │                       ├ [371]: usr/lib/python3.12/encodings/mac_latin2.py 
│                │                       ├ [372]: usr/lib/python3.12/encodings/mac_roman.py 
│                │                       ├ [373]: usr/lib/python3.12/encodings/mac_romanian.py 
│                │                       ├ [374]: usr/lib/python3.12/encodings/mac_turkish.py 
│                │                       ├ [375]: usr/lib/python3.12/encodings/mbcs.py 
│                │                       ├ [376]: usr/lib/python3.12/encodings/oem.py 
│                │                       ├ [377]: usr/lib/python3.12/encodings/palmos.py 
│                │                       ├ [378]: usr/lib/python3.12/encodings/ptcp154.py 
│                │                       ├ [379]: usr/lib/python3.12/encodings/punycode.py 
│                │                       ├ [380]: usr/lib/python3.12/encodings/quopri_codec.py 
│                │                       ├ [381]: usr/lib/python3.12/encodings/raw_unicode_escape.py 
│                │                       ├ [382]: usr/lib/python3.12/encodings/rot_13.py 
│                │                       ├ [383]: usr/lib/python3.12/encodings/shift_jis.py 
│                │                       ├ [384]: usr/lib/python3.12/encodings/shift_jis_2004.py 
│                │                       ├ [385]: usr/lib/python3.12/encodings/shift_jisx0213.py 
│                │                       ├ [386]: usr/lib/python3.12/encodings/tis_620.py 
│                │                       ├ [387]: usr/lib/python3.12/encodings/undefined.py 
│                │                       ├ [388]: usr/lib/python3.12/encodings/unicode_escape.py 
│                │                       ├ [389]: usr/lib/python3.12/encodings/utf_16.py 
│                │                       ├ [390]: usr/lib/python3.12/encodings/utf_16_be.py 
│                │                       ├ [391]: usr/lib/python3.12/encodings/utf_16_le.py 
│                │                       ├ [392]: usr/lib/python3.12/encodings/utf_32.py 
│                │                       ├ [393]: usr/lib/python3.12/encodings/utf_32_be.py 
│                │                       ├ [394]: usr/lib/python3.12/encodings/utf_32_le.py 
│                │                       ├ [395]: usr/lib/python3.12/encodings/utf_7.py 
│                │                       ├ [396]: usr/lib/python3.12/encodings/utf_8.py 
│                │                       ├ [397]: usr/lib/python3.12/encodings/utf_8_sig.py 
│                │                       ├ [398]: usr/lib/python3.12/encodings/uu_codec.py 
│                │                       ├ [399]: usr/lib/python3.12/encodings/zlib_codec.py 
│                │                       ├ [400]: usr/lib/python3.12/ensurepip/__init__.py 
│                │                       ├ [401]: usr/lib/python3.12/ensurepip/__main__.py 
│                │                       ├ [402]: usr/lib/python3.12/ensurepip/_uninstall.py 
│                │                       ├ [403]: usr/lib/python3.12/ensurepip/_bundled/pip-25.0.1-py3-none-any
│                │                       │        .whl 
│                │                       ├ [404]: usr/lib/python3.12/html/__init__.py 
│                │                       ├ [405]: usr/lib/python3.12/html/entities.py 
│                │                       ├ [406]: usr/lib/python3.12/html/parser.py 
│                │                       ├ [407]: usr/lib/python3.12/http/__init__.py 
│                │                       ├ [408]: usr/lib/python3.12/http/client.py 
│                │                       ├ [409]: usr/lib/python3.12/http/cookiejar.py 
│                │                       ├ [410]: usr/lib/python3.12/http/cookies.py 
│                │                       ├ [411]: usr/lib/python3.12/http/server.py 
│                │                       ├ [412]: usr/lib/python3.12/importlib/__init__.py 
│                │                       ├ [413]: usr/lib/python3.12/importlib/_abc.py 
│                │                       ├ [414]: usr/lib/python3.12/importlib/_bootstrap.py 
│                │                       ├ [415]: usr/lib/python3.12/importlib/_bootstrap_external.py 
│                │                       ├ [416]: usr/lib/python3.12/importlib/abc.py 
│                │                       ├ [417]: usr/lib/python3.12/importlib/machinery.py 
│                │                       ├ [418]: usr/lib/python3.12/importlib/readers.py 
│                │                       ├ [419]: usr/lib/python3.12/importlib/simple.py 
│                │                       ├ [420]: usr/lib/python3.12/importlib/util.py 
│                │                       ├ [421]: usr/lib/python3.12/importlib/metadata/__init__.py 
│                │                       ├ [422]: usr/lib/python3.12/importlib/metadata/_adapters.py 
│                │                       ├ [423]: usr/lib/python3.12/importlib/metadata/_collections.py 
│                │                       ├ [424]: usr/lib/python3.12/importlib/metadata/_functools.py 
│                │                       ├ [425]: usr/lib/python3.12/importlib/metadata/_itertools.py 
│                │                       ├ [426]: usr/lib/python3.12/importlib/metadata/_meta.py 
│                │                       ├ [427]: usr/lib/python3.12/importlib/metadata/_text.py 
│                │                       ├ [428]: usr/lib/python3.12/importlib/resources/__init__.py 
│                │                       ├ [429]: usr/lib/python3.12/importlib/resources/_adapters.py 
│                │                       ├ [430]: usr/lib/python3.12/importlib/resources/_common.py 
│                │                       ├ [431]: usr/lib/python3.12/importlib/resources/_itertools.py 
│                │                       ├ [432]: usr/lib/python3.12/importlib/resources/_legacy.py 
│                │                       ├ [433]: usr/lib/python3.12/importlib/resources/abc.py 
│                │                       ├ [434]: usr/lib/python3.12/importlib/resources/readers.py 
│                │                       ├ [435]: usr/lib/python3.12/importlib/resources/simple.py 
│                │                       ├ [436]: usr/lib/python3.12/json/__init__.py 
│                │                       ├ [437]: usr/lib/python3.12/json/decoder.py 
│                │                       ├ [438]: usr/lib/python3.12/json/encoder.py 
│                │                       ├ [439]: usr/lib/python3.12/json/scanner.py 
│                │                       ├ [440]: usr/lib/python3.12/json/tool.py 
│                │                       ├ [441]: usr/lib/python3.12/lib-dynload/_asyncio.cpython-312-x86_64-li
│                │                       │        nux-musl.so 
│                │                       ├ [442]: usr/lib/python3.12/lib-dynload/_bisect.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [443]: usr/lib/python3.12/lib-dynload/_blake2.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [444]: usr/lib/python3.12/lib-dynload/_bz2.cpython-312-x86_64-linux-
│                │                       │        musl.so 
│                │                       ├ [445]: usr/lib/python3.12/lib-dynload/_codecs_cn.cpython-312-x86_64-
│                │                       │        linux-musl.so 
│                │                       ├ [446]: usr/lib/python3.12/lib-dynload/_codecs_hk.cpython-312-x86_64-
│                │                       │        linux-musl.so 
│                │                       ├ [447]: usr/lib/python3.12/lib-dynload/_codecs_iso2022.cpython-312-x8
│                │                       │        6_64-linux-musl.so 
│                │                       ├ [448]: usr/lib/python3.12/lib-dynload/_codecs_jp.cpython-312-x86_64-
│                │                       │        linux-musl.so 
│                │                       ├ [449]: usr/lib/python3.12/lib-dynload/_codecs_kr.cpython-312-x86_64-
│                │                       │        linux-musl.so 
│                │                       ├ [450]: usr/lib/python3.12/lib-dynload/_codecs_tw.cpython-312-x86_64-
│                │                       │        linux-musl.so 
│                │                       ├ [451]: usr/lib/python3.12/lib-dynload/_contextvars.cpython-312-x86_6
│                │                       │        4-linux-musl.so 
│                │                       ├ [452]: usr/lib/python3.12/lib-dynload/_crypt.cpython-312-x86_64-linu
│                │                       │        x-musl.so 
│                │                       ├ [453]: usr/lib/python3.12/lib-dynload/_csv.cpython-312-x86_64-linux-
│                │                       │        musl.so 
│                │                       ├ [454]: usr/lib/python3.12/lib-dynload/_ctypes.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [455]: usr/lib/python3.12/lib-dynload/_ctypes_test.cpython-312-x86_6
│                │                       │        4-linux-musl.so 
│                │                       ├ [456]: usr/lib/python3.12/lib-dynload/_curses.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [457]: usr/lib/python3.12/lib-dynload/_curses_panel.cpython-312-x86_
│                │                       │        64-linux-musl.so 
│                │                       ├ [458]: usr/lib/python3.12/lib-dynload/_datetime.cpython-312-x86_64-l
│                │                       │        inux-musl.so 
│                │                       ├ [459]: usr/lib/python3.12/lib-dynload/_dbm.cpython-312-x86_64-linux-
│                │                       │        musl.so 
│                │                       ├ [460]: usr/lib/python3.12/lib-dynload/_decimal.cpython-312-x86_64-li
│                │                       │        nux-musl.so 
│                │                       ├ [461]: usr/lib/python3.12/lib-dynload/_elementtree.cpython-312-x86_6
│                │                       │        4-linux-musl.so 
│                │                       ├ [462]: usr/lib/python3.12/lib-dynload/_hashlib.cpython-312-x86_64-li
│                │                       │        nux-musl.so 
│                │                       ├ [463]: usr/lib/python3.12/lib-dynload/_heapq.cpython-312-x86_64-linu
│                │                       │        x-musl.so 
│                │                       ├ [464]: usr/lib/python3.12/lib-dynload/_json.cpython-312-x86_64-linux
│                │                       │        -musl.so 
│                │                       ├ [465]: usr/lib/python3.12/lib-dynload/_lsprof.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [466]: usr/lib/python3.12/lib-dynload/_lzma.cpython-312-x86_64-linux
│                │                       │        -musl.so 
│                │                       ├ [467]: usr/lib/python3.12/lib-dynload/_md5.cpython-312-x86_64-linux-
│                │                       │        musl.so 
│                │                       ├ [468]: usr/lib/python3.12/lib-dynload/_multibytecodec.cpython-312-x8
│                │                       │        6_64-linux-musl.so 
│                │                       ├ [469]: usr/lib/python3.12/lib-dynload/_multiprocessing.cpython-312-x
│                │                       │        86_64-linux-musl.so 
│                │                       ├ [470]: usr/lib/python3.12/lib-dynload/_opcode.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [471]: usr/lib/python3.12/lib-dynload/_pickle.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [472]: usr/lib/python3.12/lib-dynload/_posixshmem.cpython-312-x86_64
│                │                       │        -linux-musl.so 
│                │                       ├ [473]: usr/lib/python3.12/lib-dynload/_posixsubprocess.cpython-312-x
│                │                       │        86_64-linux-musl.so 
│                │                       ├ [474]: usr/lib/python3.12/lib-dynload/_queue.cpython-312-x86_64-linu
│                │                       │        x-musl.so 
│                │                       ├ [475]: usr/lib/python3.12/lib-dynload/_random.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [476]: usr/lib/python3.12/lib-dynload/_sha1.cpython-312-x86_64-linux
│                │                       │        -musl.so 
│                │                       ├ [477]: usr/lib/python3.12/lib-dynload/_sha2.cpython-312-x86_64-linux
│                │                       │        -musl.so 
│                │                       ├ [478]: usr/lib/python3.12/lib-dynload/_sha3.cpython-312-x86_64-linux
│                │                       │        -musl.so 
│                │                       ├ [479]: usr/lib/python3.12/lib-dynload/_socket.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [480]: usr/lib/python3.12/lib-dynload/_sqlite3.cpython-312-x86_64-li
│                │                       │        nux-musl.so 
│                │                       ├ [481]: usr/lib/python3.12/lib-dynload/_ssl.cpython-312-x86_64-linux-
│                │                       │        musl.so 
│                │                       ├ [482]: usr/lib/python3.12/lib-dynload/_statistics.cpython-312-x86_64
│                │                       │        -linux-musl.so 
│                │                       ├ [483]: usr/lib/python3.12/lib-dynload/_struct.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [484]: usr/lib/python3.12/lib-dynload/_testbuffer.cpython-312-x86_64
│                │                       │        -linux-musl.so 
│                │                       ├ [485]: usr/lib/python3.12/lib-dynload/_testcapi.cpython-312-x86_64-l
│                │                       │        inux-musl.so 
│                │                       ├ [486]: usr/lib/python3.12/lib-dynload/_testclinic.cpython-312-x86_64
│                │                       │        -linux-musl.so 
│                │                       ├ [487]: usr/lib/python3.12/lib-dynload/_testimportmultiple.cpython-31
│                │                       │        2-x86_64-linux-musl.so 
│                │                       ├ [488]: usr/lib/python3.12/lib-dynload/_testinternalcapi.cpython-312-
│                │                       │        x86_64-linux-musl.so 
│                │                       ├ [489]: usr/lib/python3.12/lib-dynload/_testmultiphase.cpython-312-x8
│                │                       │        6_64-linux-musl.so 
│                │                       ├ [490]: usr/lib/python3.12/lib-dynload/_testsinglephase.cpython-312-x
│                │                       │        86_64-linux-musl.so 
│                │                       ├ [491]: usr/lib/python3.12/lib-dynload/_xxinterpchannels.cpython-312-
│                │                       │        x86_64-linux-musl.so 
│                │                       ├ [492]: usr/lib/python3.12/lib-dynload/_xxsubinterpreters.cpython-312
│                │                       │        -x86_64-linux-musl.so 
│                │                       ├ [493]: usr/lib/python3.12/lib-dynload/_xxtestfuzz.cpython-312-x86_64
│                │                       │        -linux-musl.so 
│                │                       ├ [494]: usr/lib/python3.12/lib-dynload/_zoneinfo.cpython-312-x86_64-l
│                │                       │        inux-musl.so 
│                │                       ├ [495]: usr/lib/python3.12/lib-dynload/array.cpython-312-x86_64-linux
│                │                       │        -musl.so 
│                │                       ├ [496]: usr/lib/python3.12/lib-dynload/audioop.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [497]: usr/lib/python3.12/lib-dynload/binascii.cpython-312-x86_64-li
│                │                       │        nux-musl.so 
│                │                       ├ [498]: usr/lib/python3.12/lib-dynload/cmath.cpython-312-x86_64-linux
│                │                       │        -musl.so 
│                │                       ├ [499]: usr/lib/python3.12/lib-dynload/fcntl.cpython-312-x86_64-linux
│                │                       │        -musl.so 
│                │                       ├ [500]: usr/lib/python3.12/lib-dynload/grp.cpython-312-x86_64-linux-m
│                │                       │        usl.so 
│                │                       ├ [501]: usr/lib/python3.12/lib-dynload/math.cpython-312-x86_64-linux-
│                │                       │        musl.so 
│                │                       ├ [502]: usr/lib/python3.12/lib-dynload/mmap.cpython-312-x86_64-linux-
│                │                       │        musl.so 
│                │                       ├ [503]: usr/lib/python3.12/lib-dynload/ossaudiodev.cpython-312-x86_64
│                │                       │        -linux-musl.so 
│                │                       ├ [504]: usr/lib/python3.12/lib-dynload/pyexpat.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [505]: usr/lib/python3.12/lib-dynload/readline.cpython-312-x86_64-li
│                │                       │        nux-musl.so 
│                │                       ├ [506]: usr/lib/python3.12/lib-dynload/resource.cpython-312-x86_64-li
│                │                       │        nux-musl.so 
│                │                       ├ [507]: usr/lib/python3.12/lib-dynload/select.cpython-312-x86_64-linu
│                │                       │        x-musl.so 
│                │                       ├ [508]: usr/lib/python3.12/lib-dynload/spwd.cpython-312-x86_64-linux-
│                │                       │        musl.so 
│                │                       ├ [509]: usr/lib/python3.12/lib-dynload/syslog.cpython-312-x86_64-linu
│                │                       │        x-musl.so 
│                │                       ├ [510]: usr/lib/python3.12/lib-dynload/termios.cpython-312-x86_64-lin
│                │                       │        ux-musl.so 
│                │                       ├ [511]: usr/lib/python3.12/lib-dynload/unicodedata.cpython-312-x86_64
│                │                       │        -linux-musl.so 
│                │                       ├ [512]: usr/lib/python3.12/lib-dynload/xxlimited.cpython-312-x86_64-l
│                │                       │        inux-musl.so 
│                │                       ├ [513]: usr/lib/python3.12/lib-dynload/xxlimited_35.cpython-312-x86_6
│                │                       │        4-linux-musl.so 
│                │                       ├ [514]: usr/lib/python3.12/lib-dynload/xxsubtype.cpython-312-x86_64-l
│                │                       │        inux-musl.so 
│                │                       ├ [515]: usr/lib/python3.12/lib-dynload/zlib.cpython-312-x86_64-linux-
│                │                       │        musl.so 
│                │                       ├ [516]: usr/lib/python3.12/lib2to3/Grammar.txt 
│                │                       ├ [517]: usr/lib/python3.12/lib2to3/Grammar3.12.12.final.0.pickle 
│                │                       ├ [518]: usr/lib/python3.12/lib2to3/PatternGrammar.txt 
│                │                       ├ [519]: usr/lib/python3.12/lib2to3/PatternGrammar3.12.12.final.0.pickle 
│                │                       ├ [520]: usr/lib/python3.12/lib2to3/__init__.py 
│                │                       ├ [521]: usr/lib/python3.12/lib2to3/__main__.py 
│                │                       ├ [522]: usr/lib/python3.12/lib2to3/btm_matcher.py 
│                │                       ├ [523]: usr/lib/python3.12/lib2to3/btm_utils.py 
│                │                       ├ [524]: usr/lib/python3.12/lib2to3/fixer_base.py 
│                │                       ├ [525]: usr/lib/python3.12/lib2to3/fixer_util.py 
│                │                       ├ [526]: usr/lib/python3.12/lib2to3/main.py 
│                │                       ├ [527]: usr/lib/python3.12/lib2to3/patcomp.py 
│                │                       ├ [528]: usr/lib/python3.12/lib2to3/pygram.py 
│                │                       ├ [529]: usr/lib/python3.12/lib2to3/pytree.py 
│                │                       ├ [530]: usr/lib/python3.12/lib2to3/refactor.py 
│                │                       ├ [531]: usr/lib/python3.12/lib2to3/fixes/__init__.py 
│                │                       ├ [532]: usr/lib/python3.12/lib2to3/fixes/fix_apply.py 
│                │                       ├ [533]: usr/lib/python3.12/lib2to3/fixes/fix_asserts.py 
│                │                       ├ [534]: usr/lib/python3.12/lib2to3/fixes/fix_basestring.py 
│                │                       ├ [535]: usr/lib/python3.12/lib2to3/fixes/fix_buffer.py 
│                │                       ├ [536]: usr/lib/python3.12/lib2to3/fixes/fix_dict.py 
│                │                       ├ [537]: usr/lib/python3.12/lib2to3/fixes/fix_except.py 
│                │                       ├ [538]: usr/lib/python3.12/lib2to3/fixes/fix_exec.py 
│                │                       ├ [539]: usr/lib/python3.12/lib2to3/fixes/fix_execfile.py 
│                │                       ├ [540]: usr/lib/python3.12/lib2to3/fixes/fix_exitfunc.py 
│                │                       ├ [541]: usr/lib/python3.12/lib2to3/fixes/fix_filter.py 
│                │                       ├ [542]: usr/lib/python3.12/lib2to3/fixes/fix_funcattrs.py 
│                │                       ├ [543]: usr/lib/python3.12/lib2to3/fixes/fix_future.py 
│                │                       ├ [544]: usr/lib/python3.12/lib2to3/fixes/fix_getcwdu.py 
│                │                       ├ [545]: usr/lib/python3.12/lib2to3/fixes/fix_has_key.py 
│                │                       ├ [546]: usr/lib/python3.12/lib2to3/fixes/fix_idioms.py 
│                │                       ├ [547]: usr/lib/python3.12/lib2to3/fixes/fix_import.py 
│                │                       ├ [548]: usr/lib/python3.12/lib2to3/fixes/fix_imports.py 
│                │                       ├ [549]: usr/lib/python3.12/lib2to3/fixes/fix_imports2.py 
│                │                       ├ [550]: usr/lib/python3.12/lib2to3/fixes/fix_input.py 
│                │                       ├ [551]: usr/lib/python3.12/lib2to3/fixes/fix_intern.py 
│                │                       ├ [552]: usr/lib/python3.12/lib2to3/fixes/fix_isinstance.py 
│                │                       ├ [553]: usr/lib/python3.12/lib2to3/fixes/fix_itertools.py 
│                │                       ├ [554]: usr/lib/python3.12/lib2to3/fixes/fix_itertools_imports.py 
│                │                       ├ [555]: usr/lib/python3.12/lib2to3/fixes/fix_long.py 
│                │                       ├ [556]: usr/lib/python3.12/lib2to3/fixes/fix_map.py 
│                │                       ├ [557]: usr/lib/python3.12/lib2to3/fixes/fix_metaclass.py 
│                │                       ├ [558]: usr/lib/python3.12/lib2to3/fixes/fix_methodattrs.py 
│                │                       ├ [559]: usr/lib/python3.12/lib2to3/fixes/fix_ne.py 
│                │                       ├ [560]: usr/lib/python3.12/lib2to3/fixes/fix_next.py 
│                │                       ├ [561]: usr/lib/python3.12/lib2to3/fixes/fix_nonzero.py 
│                │                       ├ [562]: usr/lib/python3.12/lib2to3/fixes/fix_numliterals.py 
│                │                       ├ [563]: usr/lib/python3.12/lib2to3/fixes/fix_operator.py 
│                │                       ├ [564]: usr/lib/python3.12/lib2to3/fixes/fix_paren.py 
│                │                       ├ [565]: usr/lib/python3.12/lib2to3/fixes/fix_print.py 
│                │                       ├ [566]: usr/lib/python3.12/lib2to3/fixes/fix_raise.py 
│                │                       ├ [567]: usr/lib/python3.12/lib2to3/fixes/fix_raw_input.py 
│                │                       ├ [568]: usr/lib/python3.12/lib2to3/fixes/fix_reduce.py 
│                │                       ├ [569]: usr/lib/python3.12/lib2to3/fixes/fix_reload.py 
│                │                       ├ [570]: usr/lib/python3.12/lib2to3/fixes/fix_renames.py 
│                │                       ├ [571]: usr/lib/python3.12/lib2to3/fixes/fix_repr.py 
│                │                       ├ [572]: usr/lib/python3.12/lib2to3/fixes/fix_set_literal.py 
│                │                       ├ [573]: usr/lib/python3.12/lib2to3/fixes/fix_standarderror.py 
│                │                       ├ [574]: usr/lib/python3.12/lib2to3/fixes/fix_sys_exc.py 
│                │                       ├ [575]: usr/lib/python3.12/lib2to3/fixes/fix_throw.py 
│                │                       ├ [576]: usr/lib/python3.12/lib2to3/fixes/fix_tuple_params.py 
│                │                       ├ [577]: usr/lib/python3.12/lib2to3/fixes/fix_types.py 
│                │                       ├ [578]: usr/lib/python3.12/lib2to3/fixes/fix_unicode.py 
│                │                       ├ [579]: usr/lib/python3.12/lib2to3/fixes/fix_urllib.py 
│                │                       ├ [580]: usr/lib/python3.12/lib2to3/fixes/fix_ws_comma.py 
│                │                       ├ [581]: usr/lib/python3.12/lib2to3/fixes/fix_xrange.py 
│                │                       ├ [582]: usr/lib/python3.12/lib2to3/fixes/fix_xreadlines.py 
│                │                       ├ [583]: usr/lib/python3.12/lib2to3/fixes/fix_zip.py 
│                │                       ├ [584]: usr/lib/python3.12/lib2to3/pgen2/__init__.py 
│                │                       ├ [585]: usr/lib/python3.12/lib2to3/pgen2/conv.py 
│                │                       ├ [586]: usr/lib/python3.12/lib2to3/pgen2/driver.py 
│                │                       ├ [587]: usr/lib/python3.12/lib2to3/pgen2/grammar.py 
│                │                       ├ [588]: usr/lib/python3.12/lib2to3/pgen2/literals.py 
│                │                       ├ [589]: usr/lib/python3.12/lib2to3/pgen2/parse.py 
│                │                       ├ [590]: usr/lib/python3.12/lib2to3/pgen2/pgen.py 
│                │                       ├ [591]: usr/lib/python3.12/lib2to3/pgen2/token.py 
│                │                       ├ [592]: usr/lib/python3.12/lib2to3/pgen2/tokenize.py 
│                │                       ├ [593]: usr/lib/python3.12/logging/__init__.py 
│                │                       ├ [594]: usr/lib/python3.12/logging/config.py 
│                │                       ├ [595]: usr/lib/python3.12/logging/handlers.py 
│                │                       ├ [596]: usr/lib/python3.12/multiprocessing/__init__.py 
│                │                       ├ [597]: usr/lib/python3.12/multiprocessing/connection.py 
│                │                       ├ [598]: usr/lib/python3.12/multiprocessing/context.py 
│                │                       ├ [599]: usr/lib/python3.12/multiprocessing/forkserver.py 
│                │                       ├ [600]: usr/lib/python3.12/multiprocessing/heap.py 
│                │                       ├ [601]: usr/lib/python3.12/multiprocessing/managers.py 
│                │                       ├ [602]: usr/lib/python3.12/multiprocessing/pool.py 
│                │                       ├ [603]: usr/lib/python3.12/multiprocessing/popen_fork.py 
│                │                       ├ [604]: usr/lib/python3.12/multiprocessing/popen_forkserver.py 
│                │                       ├ [605]: usr/lib/python3.12/multiprocessing/popen_spawn_posix.py 
│                │                       ├ [606]: usr/lib/python3.12/multiprocessing/popen_spawn_win32.py 
│                │                       ├ [607]: usr/lib/python3.12/multiprocessing/process.py 
│                │                       ├ [608]: usr/lib/python3.12/multiprocessing/queues.py 
│                │                       ├ [609]: usr/lib/python3.12/multiprocessing/reduction.py 
│                │                       ├ [610]: usr/lib/python3.12/multiprocessing/resource_sharer.py 
│                │                       ├ [611]: usr/lib/python3.12/multiprocessing/resource_tracker.py 
│                │                       ├ [612]: usr/lib/python3.12/multiprocessing/shared_memory.py 
│                │                       ├ [613]: usr/lib/python3.12/multiprocessing/sharedctypes.py 
│                │                       ├ [614]: usr/lib/python3.12/multiprocessing/spawn.py 
│                │                       ├ [615]: usr/lib/python3.12/multiprocessing/synchronize.py 
│                │                       ├ [616]: usr/lib/python3.12/multiprocessing/util.py 
│                │                       ├ [617]: usr/lib/python3.12/multiprocessing/dummy/__init__.py 
│                │                       ├ [618]: usr/lib/python3.12/multiprocessing/dummy/connection.py 
│                │                       ├ [619]: usr/lib/python3.12/pydoc_data/__init__.py 
│                │                       ├ [620]: usr/lib/python3.12/pydoc_data/_pydoc.css 
│                │                       ├ [621]: usr/lib/python3.12/pydoc_data/topics.py 
│                │                       ├ [622]: usr/lib/python3.12/re/__init__.py 
│                │                       ├ [623]: usr/lib/python3.12/re/_casefix.py 
│                │                       ├ [624]: usr/lib/python3.12/re/_compiler.py 
│                │                       ├ [625]: usr/lib/python3.12/re/_constants.py 
│                │                       ├ [626]: usr/lib/python3.12/re/_parser.py 
│                │                       ├ [627]: usr/lib/python3.12/site-packages/README.txt 
│                │                       ├ [628]: usr/lib/python3.12/sqlite3/__init__.py 
│                │                       ├ [629]: usr/lib/python3.12/sqlite3/__main__.py 
│                │                       ├ [630]: usr/lib/python3.12/sqlite3/dbapi2.py 
│                │                       ├ [631]: usr/lib/python3.12/sqlite3/dump.py 
│                │                       ├ [632]: usr/lib/python3.12/tomllib/__init__.py 
│                │                       ├ [633]: usr/lib/python3.12/tomllib/_parser.py 
│                │                       ├ [634]: usr/lib/python3.12/tomllib/_re.py 
│                │                       ├ [635]: usr/lib/python3.12/tomllib/_types.py 
│                │                       ├ [636]: usr/lib/python3.12/turtledemo/__init__.py 
│                │                       ├ [637]: usr/lib/python3.12/turtledemo/__main__.py 
│                │                       ├ [638]: usr/lib/python3.12/turtledemo/bytedesign.py 
│                │                       ├ [639]: usr/lib/python3.12/turtledemo/chaos.py 
│                │                       ├ [640]: usr/lib/python3.12/turtledemo/clock.py 
│                │                       ├ [641]: usr/lib/python3.12/turtledemo/colormixer.py 
│                │                       ├ [642]: usr/lib/python3.12/turtledemo/forest.py 
│                │                       ├ [643]: usr/lib/python3.12/turtledemo/fractalcurves.py 
│                │                       ├ [644]: usr/lib/python3.12/turtledemo/lindenmayer.py 
│                │                       ├ [645]: usr/lib/python3.12/turtledemo/minimal_hanoi.py 
│                │                       ├ [646]: usr/lib/python3.12/turtledemo/nim.py 
│                │                       ├ [647]: usr/lib/python3.12/turtledemo/paint.py 
│                │                       ├ [648]: usr/lib/python3.12/turtledemo/peace.py 
│                │                       ├ [649]: usr/lib/python3.12/turtledemo/penrose.py 
│                │                       ├ [650]: usr/lib/python3.12/turtledemo/planet_and_moon.py 
│                │                       ├ [651]: usr/lib/python3.12/turtledemo/rosette.py 
│                │                       ├ [652]: usr/lib/python3.12/turtledemo/round_dance.py 
│                │                       ├ [653]: usr/lib/python3.12/turtledemo/sorting_animate.py 
│                │                       ├ [654]: usr/lib/python3.12/turtledemo/tree.py 
│                │                       ├ [655]: usr/lib/python3.12/turtledemo/turtle.cfg 
│                │                       ├ [656]: usr/lib/python3.12/turtledemo/two_canvases.py 
│                │                       ├ [657]: usr/lib/python3.12/turtledemo/yinyang.py 
│                │                       ├ [658]: usr/lib/python3.12/unittest/__init__.py 
│                │                       ├ [659]: usr/lib/python3.12/unittest/__main__.py 
│                │                       ├ [660]: usr/lib/python3.12/unittest/_log.py 
│                │                       ├ [661]: usr/lib/python3.12/unittest/async_case.py 
│                │                       ├ [662]: usr/lib/python3.12/unittest/case.py 
│                │                       ├ [663]: usr/lib/python3.12/unittest/loader.py 
│                │                       ├ [664]: usr/lib/python3.12/unittest/main.py 
│                │                       ├ [665]: usr/lib/python3.12/unittest/mock.py 
│                │                       ├ [666]: usr/lib/python3.12/unittest/result.py 
│                │                       ├ [667]: usr/lib/python3.12/unittest/runner.py 
│                │                       ├ [668]: usr/lib/python3.12/unittest/signals.py 
│                │                       ├ [669]: usr/lib/python3.12/unittest/suite.py 
│                │                       ├ [670]: usr/lib/python3.12/unittest/util.py 
│                │                       ├ [671]: usr/lib/python3.12/urllib/__init__.py 
│                │                       ├ [672]: usr/lib/python3.12/urllib/error.py 
│                │                       ├ [673]: usr/lib/python3.12/urllib/parse.py 
│                │                       ├ [674]: usr/lib/python3.12/urllib/request.py 
│                │                       ├ [675]: usr/lib/python3.12/urllib/response.py 
│                │                       ├ [676]: usr/lib/python3.12/urllib/robotparser.py 
│                │                       ├ [677]: usr/lib/python3.12/venv/__init__.py 
│                │                       ├ [678]: usr/lib/python3.12/venv/__main__.py 
│                │                       ├ [679]: usr/lib/python3.12/venv/scripts/common/Activate.ps1 
│                │                       ├ [680]: usr/lib/python3.12/venv/scripts/common/activate 
│                │                       ├ [681]: usr/lib/python3.12/venv/scripts/posix/activate.csh 
│                │                       ├ [682]: usr/lib/python3.12/venv/scripts/posix/activate.fish 
│                │                       ├ [683]: usr/lib/python3.12/wsgiref/__init__.py 
│                │                       ├ [684]: usr/lib/python3.12/wsgiref/handlers.py 
│                │                       ├ [685]: usr/lib/python3.12/wsgiref/headers.py 
│                │                       ├ [686]: usr/lib/python3.12/wsgiref/simple_server.py 
│                │                       ├ [687]: usr/lib/python3.12/wsgiref/types.py 
│                │                       ├ [688]: usr/lib/python3.12/wsgiref/util.py 
│                │                       ├ [689]: usr/lib/python3.12/wsgiref/validate.py 
│                │                       ├ [690]: usr/lib/python3.12/xml/__init__.py 
│                │                       ├ [691]: usr/lib/python3.12/xml/dom/NodeFilter.py 
│                │                       ├ [692]: usr/lib/python3.12/xml/dom/__init__.py 
│                │                       ├ [693]: usr/lib/python3.12/xml/dom/domreg.py 
│                │                       ├ [694]: usr/lib/python3.12/xml/dom/expatbuilder.py 
│                │                       ├ [695]: usr/lib/python3.12/xml/dom/minicompat.py 
│                │                       ├ [696]: usr/lib/python3.12/xml/dom/minidom.py 
│                │                       ├ [697]: usr/lib/python3.12/xml/dom/pulldom.py 
│                │                       ├ [698]: usr/lib/python3.12/xml/dom/xmlbuilder.py 
│                │                       ├ [699]: usr/lib/python3.12/xml/etree/ElementInclude.py 
│                │                       ├ [700]: usr/lib/python3.12/xml/etree/ElementPath.py 
│                │                       ├ [701]: usr/lib/python3.12/xml/etree/ElementTree.py 
│                │                       ├ [702]: usr/lib/python3.12/xml/etree/__init__.py 
│                │                       ├ [703]: usr/lib/python3.12/xml/etree/cElementTree.py 
│                │                       ├ [704]: usr/lib/python3.12/xml/parsers/__init__.py 
│                │                       ├ [705]: usr/lib/python3.12/xml/parsers/expat.py 
│                │                       ├ [706]: usr/lib/python3.12/xml/sax/__init__.py 
│                │                       ├ [707]: usr/lib/python3.12/xml/sax/_exceptions.py 
│                │                       ├ [708]: usr/lib/python3.12/xml/sax/expatreader.py 
│                │                       ├ [709]: usr/lib/python3.12/xml/sax/handler.py 
│                │                       ├ [710]: usr/lib/python3.12/xml/sax/saxutils.py 
│                │                       ├ [711]: usr/lib/python3.12/xml/sax/xmlreader.py 
│                │                       ├ [712]: usr/lib/python3.12/xmlrpc/__init__.py 
│                │                       ├ [713]: usr/lib/python3.12/xmlrpc/client.py 
│                │                       ├ [714]: usr/lib/python3.12/xmlrpc/server.py 
│                │                       ├ [715]: usr/lib/python3.12/zipfile/__init__.py 
│                │                       ├ [716]: usr/lib/python3.12/zipfile/__main__.py 
│                │                       ├ [717]: usr/lib/python3.12/zipfile/_path/__init__.py 
│                │                       ├ [718]: usr/lib/python3.12/zipfile/_path/glob.py 
│                │                       ├ [719]: usr/lib/python3.12/zoneinfo/__init__.py 
│                │                       ├ [720]: usr/lib/python3.12/zoneinfo/_common.py 
│                │                       ├ [721]: usr/lib/python3.12/zoneinfo/_tzpath.py 
│                │                       ╰ [722]: usr/lib/python3.12/zoneinfo/_zoneinfo.py 
│                ├ [67] ╭ ID        : python3-pyc@3.12.12-r0 
│                │      ├ Name      : python3-pyc 
│                │      ├ Identifier ╭ PURL: pkg:apk/alpine/python3-pyc@3.12.12-r0?arch=x86_64&distro=3.23.2 
│                │      │            ╰ UID : be2d287e5bd0b15e 
│                │      ├ Version   : 3.12.12-r0 
│                │      ├ Arch      : x86_64 
│                │      ├ SrcName   : python3 
│                │      ├ SrcVersion: 3.12.12-r0 
│                │      ├ Licenses   ─ [0]: PSF-2.0 
│                │      ├ Maintainer: Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn  ╭ [0]: pyc@3.12.12-r0 
│                │      │            ╰ [1]: python3-pycache-pyc0@3.12.12-r0 
│                │      ├ Layer      ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335fa38
│                │      │            │         6e9e106 
│                │      │            ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cbad77
│                │      │                      07d9fbb 
│                │      ╰ Digest    : sha1:1590b1800379a72b1fd6d11a734cd0b8c9472c78 
│                ├ [68] ╭ ID            : python3-pycache-pyc0@3.12.12-r0 
│                │      ├ Name          : python3-pycache-pyc0 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/python3-pycache-pyc0@3.12.12-r0?arch=x86_64&dis
│                │      │                │       tro=3.23.2 
│                │      │                ╰ UID : 6a0858a4baf76401 
│                │      ├ Version       : 3.12.12-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : python3 
│                │      ├ SrcVersion    : 3.12.12-r0 
│                │      ├ Licenses       ─ [0]: PSF-2.0 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: libssl3@3.5.4-r0 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:cb693ca60fe985e6c5b0ebaecd8f5201e2195c2c 
│                │      ╰ InstalledFiles ╭ [0]  : usr/lib/python3.12/__phello__/__pycache__/__init__.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [1]  : usr/lib/python3.12/__phello__/__pycache__/spam.cpython-312.pyc 
│                │                       ├ [2]  : usr/lib/python3.12/__pycache__/__future__.cpython-312.pyc 
│                │                       ├ [3]  : usr/lib/python3.12/__pycache__/__hello__.cpython-312.pyc 
│                │                       ├ [4]  : usr/lib/python3.12/__pycache__/_aix_support.cpython-312.pyc 
│                │                       ├ [5]  : usr/lib/python3.12/__pycache__/_collections_abc.cpython-312.pyc 
│                │                       ├ [6]  : usr/lib/python3.12/__pycache__/_compat_pickle.cpython-312.pyc 
│                │                       ├ [7]  : usr/lib/python3.12/__pycache__/_compression.cpython-312.pyc 
│                │                       ├ [8]  : usr/lib/python3.12/__pycache__/_markupbase.cpython-312.pyc 
│                │                       ├ [9]  : usr/lib/python3.12/__pycache__/_osx_support.cpython-312.pyc 
│                │                       ├ [10] : usr/lib/python3.12/__pycache__/_py_abc.cpython-312.pyc 
│                │                       ├ [11] : usr/lib/python3.12/__pycache__/_pydatetime.cpython-312.pyc 
│                │                       ├ [12] : usr/lib/python3.12/__pycache__/_pydecimal.cpython-312.pyc 
│                │                       ├ [13] : usr/lib/python3.12/__pycache__/_pyio.cpython-312.pyc 
│                │                       ├ [14] : usr/lib/python3.12/__pycache__/_pylong.cpython-312.pyc 
│                │                       ├ [15] : usr/lib/python3.12/__pycache__/_sitebuiltins.cpython-312.pyc 
│                │                       ├ [16] : usr/lib/python3.12/__pycache__/_strptime.cpython-312.pyc 
│                │                       ├ [17] : usr/lib/python3.12/__pycache__/_sysconfigdata__linux_x86_64-l
│                │                       │        inux-musl.cpython-312.pyc 
│                │                       ├ [18] : usr/lib/python3.12/__pycache__/_threading_local.cpython-312.pyc 
│                │                       ├ [19] : usr/lib/python3.12/__pycache__/_weakrefset.cpython-312.pyc 
│                │                       ├ [20] : usr/lib/python3.12/__pycache__/abc.cpython-312.pyc 
│                │                       ├ [21] : usr/lib/python3.12/__pycache__/aifc.cpython-312.pyc 
│                │                       ├ [22] : usr/lib/python3.12/__pycache__/antigravity.cpython-312.pyc 
│                │                       ├ [23] : usr/lib/python3.12/__pycache__/argparse.cpython-312.pyc 
│                │                       ├ [24] : usr/lib/python3.12/__pycache__/ast.cpython-312.pyc 
│                │                       ├ [25] : usr/lib/python3.12/__pycache__/base64.cpython-312.pyc 
│                │                       ├ [26] : usr/lib/python3.12/__pycache__/bdb.cpython-312.pyc 
│                │                       ├ [27] : usr/lib/python3.12/__pycache__/bisect.cpython-312.pyc 
│                │                       ├ [28] : usr/lib/python3.12/__pycache__/bz2.cpython-312.pyc 
│                │                       ├ [29] : usr/lib/python3.12/__pycache__/cProfile.cpython-312.pyc 
│                │                       ├ [30] : usr/lib/python3.12/__pycache__/calendar.cpython-312.pyc 
│                │                       ├ [31] : usr/lib/python3.12/__pycache__/cgi.cpython-312.pyc 
│                │                       ├ [32] : usr/lib/python3.12/__pycache__/cgitb.cpython-312.pyc 
│                │                       ├ [33] : usr/lib/python3.12/__pycache__/chunk.cpython-312.pyc 
│                │                       ├ [34] : usr/lib/python3.12/__pycache__/cmd.cpython-312.pyc 
│                │                       ├ [35] : usr/lib/python3.12/__pycache__/code.cpython-312.pyc 
│                │                       ├ [36] : usr/lib/python3.12/__pycache__/codecs.cpython-312.pyc 
│                │                       ├ [37] : usr/lib/python3.12/__pycache__/codeop.cpython-312.pyc 
│                │                       ├ [38] : usr/lib/python3.12/__pycache__/colorsys.cpython-312.pyc 
│                │                       ├ [39] : usr/lib/python3.12/__pycache__/compileall.cpython-312.pyc 
│                │                       ├ [40] : usr/lib/python3.12/__pycache__/configparser.cpython-312.pyc 
│                │                       ├ [41] : usr/lib/python3.12/__pycache__/contextlib.cpython-312.pyc 
│                │                       ├ [42] : usr/lib/python3.12/__pycache__/contextvars.cpython-312.pyc 
│                │                       ├ [43] : usr/lib/python3.12/__pycache__/copy.cpython-312.pyc 
│                │                       ├ [44] : usr/lib/python3.12/__pycache__/copyreg.cpython-312.pyc 
│                │                       ├ [45] : usr/lib/python3.12/__pycache__/crypt.cpython-312.pyc 
│                │                       ├ [46] : usr/lib/python3.12/__pycache__/csv.cpython-312.pyc 
│                │                       ├ [47] : usr/lib/python3.12/__pycache__/dataclasses.cpython-312.pyc 
│                │                       ├ [48] : usr/lib/python3.12/__pycache__/datetime.cpython-312.pyc 
│                │                       ├ [49] : usr/lib/python3.12/__pycache__/decimal.cpython-312.pyc 
│                │                       ├ [50] : usr/lib/python3.12/__pycache__/difflib.cpython-312.pyc 
│                │                       ├ [51] : usr/lib/python3.12/__pycache__/dis.cpython-312.pyc 
│                │                       ├ [52] : usr/lib/python3.12/__pycache__/doctest.cpython-312.pyc 
│                │                       ├ [53] : usr/lib/python3.12/__pycache__/enum.cpython-312.pyc 
│                │                       ├ [54] : usr/lib/python3.12/__pycache__/filecmp.cpython-312.pyc 
│                │                       ├ [55] : usr/lib/python3.12/__pycache__/fileinput.cpython-312.pyc 
│                │                       ├ [56] : usr/lib/python3.12/__pycache__/fnmatch.cpython-312.pyc 
│                │                       ├ [57] : usr/lib/python3.12/__pycache__/fractions.cpython-312.pyc 
│                │                       ├ [58] : usr/lib/python3.12/__pycache__/ftplib.cpython-312.pyc 
│                │                       ├ [59] : usr/lib/python3.12/__pycache__/functools.cpython-312.pyc 
│                │                       ├ [60] : usr/lib/python3.12/__pycache__/genericpath.cpython-312.pyc 
│                │                       ├ [61] : usr/lib/python3.12/__pycache__/getopt.cpython-312.pyc 
│                │                       ├ [62] : usr/lib/python3.12/__pycache__/getpass.cpython-312.pyc 
│                │                       ├ [63] : usr/lib/python3.12/__pycache__/gettext.cpython-312.pyc 
│                │                       ├ [64] : usr/lib/python3.12/__pycache__/glob.cpython-312.pyc 
│                │                       ├ [65] : usr/lib/python3.12/__pycache__/graphlib.cpython-312.pyc 
│                │                       ├ [66] : usr/lib/python3.12/__pycache__/gzip.cpython-312.pyc 
│                │                       ├ [67] : usr/lib/python3.12/__pycache__/hashlib.cpython-312.pyc 
│                │                       ├ [68] : usr/lib/python3.12/__pycache__/heapq.cpython-312.pyc 
│                │                       ├ [69] : usr/lib/python3.12/__pycache__/hmac.cpython-312.pyc 
│                │                       ├ [70] : usr/lib/python3.12/__pycache__/imaplib.cpython-312.pyc 
│                │                       ├ [71] : usr/lib/python3.12/__pycache__/imghdr.cpython-312.pyc 
│                │                       ├ [72] : usr/lib/python3.12/__pycache__/inspect.cpython-312.pyc 
│                │                       ├ [73] : usr/lib/python3.12/__pycache__/io.cpython-312.pyc 
│                │                       ├ [74] : usr/lib/python3.12/__pycache__/ipaddress.cpython-312.pyc 
│                │                       ├ [75] : usr/lib/python3.12/__pycache__/keyword.cpython-312.pyc 
│                │                       ├ [76] : usr/lib/python3.12/__pycache__/linecache.cpython-312.pyc 
│                │                       ├ [77] : usr/lib/python3.12/__pycache__/locale.cpython-312.pyc 
│                │                       ├ [78] : usr/lib/python3.12/__pycache__/lzma.cpython-312.pyc 
│                │                       ├ [79] : usr/lib/python3.12/__pycache__/mailbox.cpython-312.pyc 
│                │                       ├ [80] : usr/lib/python3.12/__pycache__/mailcap.cpython-312.pyc 
│                │                       ├ [81] : usr/lib/python3.12/__pycache__/mimetypes.cpython-312.pyc 
│                │                       ├ [82] : usr/lib/python3.12/__pycache__/modulefinder.cpython-312.pyc 
│                │                       ├ [83] : usr/lib/python3.12/__pycache__/netrc.cpython-312.pyc 
│                │                       ├ [84] : usr/lib/python3.12/__pycache__/nntplib.cpython-312.pyc 
│                │                       ├ [85] : usr/lib/python3.12/__pycache__/ntpath.cpython-312.pyc 
│                │                       ├ [86] : usr/lib/python3.12/__pycache__/nturl2path.cpython-312.pyc 
│                │                       ├ [87] : usr/lib/python3.12/__pycache__/numbers.cpython-312.pyc 
│                │                       ├ [88] : usr/lib/python3.12/__pycache__/opcode.cpython-312.pyc 
│                │                       ├ [89] : usr/lib/python3.12/__pycache__/operator.cpython-312.pyc 
│                │                       ├ [90] : usr/lib/python3.12/__pycache__/optparse.cpython-312.pyc 
│                │                       ├ [91] : usr/lib/python3.12/__pycache__/os.cpython-312.pyc 
│                │                       ├ [92] : usr/lib/python3.12/__pycache__/pathlib.cpython-312.pyc 
│                │                       ├ [93] : usr/lib/python3.12/__pycache__/pdb.cpython-312.pyc 
│                │                       ├ [94] : usr/lib/python3.12/__pycache__/pickle.cpython-312.pyc 
│                │                       ├ [95] : usr/lib/python3.12/__pycache__/pickletools.cpython-312.pyc 
│                │                       ├ [96] : usr/lib/python3.12/__pycache__/pipes.cpython-312.pyc 
│                │                       ├ [97] : usr/lib/python3.12/__pycache__/pkgutil.cpython-312.pyc 
│                │                       ├ [98] : usr/lib/python3.12/__pycache__/platform.cpython-312.pyc 
│                │                       ├ [99] : usr/lib/python3.12/__pycache__/plistlib.cpython-312.pyc 
│                │                       ├ [100]: usr/lib/python3.12/__pycache__/poplib.cpython-312.pyc 
│                │                       ├ [101]: usr/lib/python3.12/__pycache__/posixpath.cpython-312.pyc 
│                │                       ├ [102]: usr/lib/python3.12/__pycache__/pprint.cpython-312.pyc 
│                │                       ├ [103]: usr/lib/python3.12/__pycache__/profile.cpython-312.pyc 
│                │                       ├ [104]: usr/lib/python3.12/__pycache__/pstats.cpython-312.pyc 
│                │                       ├ [105]: usr/lib/python3.12/__pycache__/pty.cpython-312.pyc 
│                │                       ├ [106]: usr/lib/python3.12/__pycache__/py_compile.cpython-312.pyc 
│                │                       ├ [107]: usr/lib/python3.12/__pycache__/pyclbr.cpython-312.pyc 
│                │                       ├ [108]: usr/lib/python3.12/__pycache__/pydoc.cpython-312.pyc 
│                │                       ├ [109]: usr/lib/python3.12/__pycache__/queue.cpython-312.pyc 
│                │                       ├ [110]: usr/lib/python3.12/__pycache__/quopri.cpython-312.pyc 
│                │                       ├ [111]: usr/lib/python3.12/__pycache__/random.cpython-312.pyc 
│                │                       ├ [112]: usr/lib/python3.12/__pycache__/reprlib.cpython-312.pyc 
│                │                       ├ [113]: usr/lib/python3.12/__pycache__/rlcompleter.cpython-312.pyc 
│                │                       ├ [114]: usr/lib/python3.12/__pycache__/runpy.cpython-312.pyc 
│                │                       ├ [115]: usr/lib/python3.12/__pycache__/sched.cpython-312.pyc 
│                │                       ├ [116]: usr/lib/python3.12/__pycache__/secrets.cpython-312.pyc 
│                │                       ├ [117]: usr/lib/python3.12/__pycache__/selectors.cpython-312.pyc 
│                │                       ├ [118]: usr/lib/python3.12/__pycache__/shelve.cpython-312.pyc 
│                │                       ├ [119]: usr/lib/python3.12/__pycache__/shlex.cpython-312.pyc 
│                │                       ├ [120]: usr/lib/python3.12/__pycache__/shutil.cpython-312.pyc 
│                │                       ├ [121]: usr/lib/python3.12/__pycache__/signal.cpython-312.pyc 
│                │                       ├ [122]: usr/lib/python3.12/__pycache__/site.cpython-312.pyc 
│                │                       ├ [123]: usr/lib/python3.12/__pycache__/smtplib.cpython-312.pyc 
│                │                       ├ [124]: usr/lib/python3.12/__pycache__/sndhdr.cpython-312.pyc 
│                │                       ├ [125]: usr/lib/python3.12/__pycache__/socket.cpython-312.pyc 
│                │                       ├ [126]: usr/lib/python3.12/__pycache__/socketserver.cpython-312.pyc 
│                │                       ├ [127]: usr/lib/python3.12/__pycache__/sre_compile.cpython-312.pyc 
│                │                       ├ [128]: usr/lib/python3.12/__pycache__/sre_constants.cpython-312.pyc 
│                │                       ├ [129]: usr/lib/python3.12/__pycache__/sre_parse.cpython-312.pyc 
│                │                       ├ [130]: usr/lib/python3.12/__pycache__/ssl.cpython-312.pyc 
│                │                       ├ [131]: usr/lib/python3.12/__pycache__/stat.cpython-312.pyc 
│                │                       ├ [132]: usr/lib/python3.12/__pycache__/statistics.cpython-312.pyc 
│                │                       ├ [133]: usr/lib/python3.12/__pycache__/string.cpython-312.pyc 
│                │                       ├ [134]: usr/lib/python3.12/__pycache__/stringprep.cpython-312.pyc 
│                │                       ├ [135]: usr/lib/python3.12/__pycache__/struct.cpython-312.pyc 
│                │                       ├ [136]: usr/lib/python3.12/__pycache__/subprocess.cpython-312.pyc 
│                │                       ├ [137]: usr/lib/python3.12/__pycache__/sunau.cpython-312.pyc 
│                │                       ├ [138]: usr/lib/python3.12/__pycache__/symtable.cpython-312.pyc 
│                │                       ├ [139]: usr/lib/python3.12/__pycache__/sysconfig.cpython-312.pyc 
│                │                       ├ [140]: usr/lib/python3.12/__pycache__/tabnanny.cpython-312.pyc 
│                │                       ├ [141]: usr/lib/python3.12/__pycache__/tarfile.cpython-312.pyc 
│                │                       ├ [142]: usr/lib/python3.12/__pycache__/telnetlib.cpython-312.pyc 
│                │                       ├ [143]: usr/lib/python3.12/__pycache__/tempfile.cpython-312.pyc 
│                │                       ├ [144]: usr/lib/python3.12/__pycache__/textwrap.cpython-312.pyc 
│                │                       ├ [145]: usr/lib/python3.12/__pycache__/this.cpython-312.pyc 
│                │                       ├ [146]: usr/lib/python3.12/__pycache__/threading.cpython-312.pyc 
│                │                       ├ [147]: usr/lib/python3.12/__pycache__/timeit.cpython-312.pyc 
│                │                       ├ [148]: usr/lib/python3.12/__pycache__/token.cpython-312.pyc 
│                │                       ├ [149]: usr/lib/python3.12/__pycache__/tokenize.cpython-312.pyc 
│                │                       ├ [150]: usr/lib/python3.12/__pycache__/trace.cpython-312.pyc 
│                │                       ├ [151]: usr/lib/python3.12/__pycache__/traceback.cpython-312.pyc 
│                │                       ├ [152]: usr/lib/python3.12/__pycache__/tracemalloc.cpython-312.pyc 
│                │                       ├ [153]: usr/lib/python3.12/__pycache__/tty.cpython-312.pyc 
│                │                       ├ [154]: usr/lib/python3.12/__pycache__/turtle.cpython-312.pyc 
│                │                       ├ [155]: usr/lib/python3.12/__pycache__/types.cpython-312.pyc 
│                │                       ├ [156]: usr/lib/python3.12/__pycache__/typing.cpython-312.pyc 
│                │                       ├ [157]: usr/lib/python3.12/__pycache__/uu.cpython-312.pyc 
│                │                       ├ [158]: usr/lib/python3.12/__pycache__/uuid.cpython-312.pyc 
│                │                       ├ [159]: usr/lib/python3.12/__pycache__/warnings.cpython-312.pyc 
│                │                       ├ [160]: usr/lib/python3.12/__pycache__/wave.cpython-312.pyc 
│                │                       ├ [161]: usr/lib/python3.12/__pycache__/weakref.cpython-312.pyc 
│                │                       ├ [162]: usr/lib/python3.12/__pycache__/webbrowser.cpython-312.pyc 
│                │                       ├ [163]: usr/lib/python3.12/__pycache__/xdrlib.cpython-312.pyc 
│                │                       ├ [164]: usr/lib/python3.12/__pycache__/zipapp.cpython-312.pyc 
│                │                       ├ [165]: usr/lib/python3.12/__pycache__/zipimport.cpython-312.pyc 
│                │                       ├ [166]: usr/lib/python3.12/asyncio/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [167]: usr/lib/python3.12/asyncio/__pycache__/__main__.cpython-312.pyc 
│                │                       ├ [168]: usr/lib/python3.12/asyncio/__pycache__/base_events.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [169]: usr/lib/python3.12/asyncio/__pycache__/base_futures.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [170]: usr/lib/python3.12/asyncio/__pycache__/base_subprocess.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [171]: usr/lib/python3.12/asyncio/__pycache__/base_tasks.cpython-312
│                │                       │        .pyc 
│                │                       ├ [172]: usr/lib/python3.12/asyncio/__pycache__/constants.cpython-312.
│                │                       │        pyc 
│                │                       ├ [173]: usr/lib/python3.12/asyncio/__pycache__/coroutines.cpython-312
│                │                       │        .pyc 
│                │                       ├ [174]: usr/lib/python3.12/asyncio/__pycache__/events.cpython-312.pyc 
│                │                       ├ [175]: usr/lib/python3.12/asyncio/__pycache__/exceptions.cpython-312
│                │                       │        .pyc 
│                │                       ├ [176]: usr/lib/python3.12/asyncio/__pycache__/format_helpers.cpython
│                │                       │        -312.pyc 
│                │                       ├ [177]: usr/lib/python3.12/asyncio/__pycache__/futures.cpython-312.pyc 
│                │                       ├ [178]: usr/lib/python3.12/asyncio/__pycache__/locks.cpython-312.pyc 
│                │                       ├ [179]: usr/lib/python3.12/asyncio/__pycache__/log.cpython-312.pyc 
│                │                       ├ [180]: usr/lib/python3.12/asyncio/__pycache__/mixins.cpython-312.pyc 
│                │                       ├ [181]: usr/lib/python3.12/asyncio/__pycache__/proactor_events.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [182]: usr/lib/python3.12/asyncio/__pycache__/protocols.cpython-312.
│                │                       │        pyc 
│                │                       ├ [183]: usr/lib/python3.12/asyncio/__pycache__/queues.cpython-312.pyc 
│                │                       ├ [184]: usr/lib/python3.12/asyncio/__pycache__/runners.cpython-312.pyc 
│                │                       ├ [185]: usr/lib/python3.12/asyncio/__pycache__/selector_events.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [186]: usr/lib/python3.12/asyncio/__pycache__/sslproto.cpython-312.pyc 
│                │                       ├ [187]: usr/lib/python3.12/asyncio/__pycache__/staggered.cpython-312.
│                │                       │        pyc 
│                │                       ├ [188]: usr/lib/python3.12/asyncio/__pycache__/streams.cpython-312.pyc 
│                │                       ├ [189]: usr/lib/python3.12/asyncio/__pycache__/subprocess.cpython-312
│                │                       │        .pyc 
│                │                       ├ [190]: usr/lib/python3.12/asyncio/__pycache__/taskgroups.cpython-312
│                │                       │        .pyc 
│                │                       ├ [191]: usr/lib/python3.12/asyncio/__pycache__/tasks.cpython-312.pyc 
│                │                       ├ [192]: usr/lib/python3.12/asyncio/__pycache__/threads.cpython-312.pyc 
│                │                       ├ [193]: usr/lib/python3.12/asyncio/__pycache__/timeouts.cpython-312.pyc 
│                │                       ├ [194]: usr/lib/python3.12/asyncio/__pycache__/transports.cpython-312
│                │                       │        .pyc 
│                │                       ├ [195]: usr/lib/python3.12/asyncio/__pycache__/trsock.cpython-312.pyc 
│                │                       ├ [196]: usr/lib/python3.12/asyncio/__pycache__/unix_events.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [197]: usr/lib/python3.12/asyncio/__pycache__/windows_events.cpython
│                │                       │        -312.pyc 
│                │                       ├ [198]: usr/lib/python3.12/asyncio/__pycache__/windows_utils.cpython-
│                │                       │        312.pyc 
│                │                       ├ [199]: usr/lib/python3.12/collections/__pycache__/__init__.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [200]: usr/lib/python3.12/collections/__pycache__/abc.cpython-312.pyc 
│                │                       ├ [201]: usr/lib/python3.12/concurrent/__pycache__/__init__.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [202]: usr/lib/python3.12/concurrent/futures/__pycache__/__init__.cp
│                │                       │        ython-312.pyc 
│                │                       ├ [203]: usr/lib/python3.12/concurrent/futures/__pycache__/_base.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [204]: usr/lib/python3.12/concurrent/futures/__pycache__/process.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [205]: usr/lib/python3.12/concurrent/futures/__pycache__/thread.cpyt
│                │                       │        hon-312.pyc 
│                │                       ├ [206]: usr/lib/python3.12/ctypes/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [207]: usr/lib/python3.12/ctypes/__pycache__/_aix.cpython-312.pyc 
│                │                       ├ [208]: usr/lib/python3.12/ctypes/__pycache__/_endian.cpython-312.pyc 
│                │                       ├ [209]: usr/lib/python3.12/ctypes/__pycache__/util.cpython-312.pyc 
│                │                       ├ [210]: usr/lib/python3.12/ctypes/__pycache__/wintypes.cpython-312.pyc 
│                │                       ├ [211]: usr/lib/python3.12/ctypes/macholib/__pycache__/__init__.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [212]: usr/lib/python3.12/ctypes/macholib/__pycache__/dyld.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [213]: usr/lib/python3.12/ctypes/macholib/__pycache__/dylib.cpython-
│                │                       │        312.pyc 
│                │                       ├ [214]: usr/lib/python3.12/ctypes/macholib/__pycache__/framework.cpyt
│                │                       │        hon-312.pyc 
│                │                       ├ [215]: usr/lib/python3.12/curses/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [216]: usr/lib/python3.12/curses/__pycache__/ascii.cpython-312.pyc 
│                │                       ├ [217]: usr/lib/python3.12/curses/__pycache__/has_key.cpython-312.pyc 
│                │                       ├ [218]: usr/lib/python3.12/curses/__pycache__/panel.cpython-312.pyc 
│                │                       ├ [219]: usr/lib/python3.12/curses/__pycache__/textpad.cpython-312.pyc 
│                │                       ├ [220]: usr/lib/python3.12/dbm/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [221]: usr/lib/python3.12/dbm/__pycache__/dumb.cpython-312.pyc 
│                │                       ├ [222]: usr/lib/python3.12/dbm/__pycache__/gnu.cpython-312.pyc 
│                │                       ├ [223]: usr/lib/python3.12/dbm/__pycache__/ndbm.cpython-312.pyc 
│                │                       ├ [224]: usr/lib/python3.12/email/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [225]: usr/lib/python3.12/email/__pycache__/_encoded_words.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [226]: usr/lib/python3.12/email/__pycache__/_header_value_parser.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [227]: usr/lib/python3.12/email/__pycache__/_parseaddr.cpython-312.pyc 
│                │                       ├ [228]: usr/lib/python3.12/email/__pycache__/_policybase.cpython-312.
│                │                       │        pyc 
│                │                       ├ [229]: usr/lib/python3.12/email/__pycache__/base64mime.cpython-312.pyc 
│                │                       ├ [230]: usr/lib/python3.12/email/__pycache__/charset.cpython-312.pyc 
│                │                       ├ [231]: usr/lib/python3.12/email/__pycache__/contentmanager.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [232]: usr/lib/python3.12/email/__pycache__/encoders.cpython-312.pyc 
│                │                       ├ [233]: usr/lib/python3.12/email/__pycache__/errors.cpython-312.pyc 
│                │                       ├ [234]: usr/lib/python3.12/email/__pycache__/feedparser.cpython-312.pyc 
│                │                       ├ [235]: usr/lib/python3.12/email/__pycache__/generator.cpython-312.pyc 
│                │                       ├ [236]: usr/lib/python3.12/email/__pycache__/header.cpython-312.pyc 
│                │                       ├ [237]: usr/lib/python3.12/email/__pycache__/headerregistry.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [238]: usr/lib/python3.12/email/__pycache__/iterators.cpython-312.pyc 
│                │                       ├ [239]: usr/lib/python3.12/email/__pycache__/message.cpython-312.pyc 
│                │                       ├ [240]: usr/lib/python3.12/email/__pycache__/parser.cpython-312.pyc 
│                │                       ├ [241]: usr/lib/python3.12/email/__pycache__/policy.cpython-312.pyc 
│                │                       ├ [242]: usr/lib/python3.12/email/__pycache__/quoprimime.cpython-312.pyc 
│                │                       ├ [243]: usr/lib/python3.12/email/__pycache__/utils.cpython-312.pyc 
│                │                       ├ [244]: usr/lib/python3.12/email/mime/__pycache__/__init__.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [245]: usr/lib/python3.12/email/mime/__pycache__/application.cpython
│                │                       │        -312.pyc 
│                │                       ├ [246]: usr/lib/python3.12/email/mime/__pycache__/audio.cpython-312.pyc 
│                │                       ├ [247]: usr/lib/python3.12/email/mime/__pycache__/base.cpython-312.pyc 
│                │                       ├ [248]: usr/lib/python3.12/email/mime/__pycache__/image.cpython-312.pyc 
│                │                       ├ [249]: usr/lib/python3.12/email/mime/__pycache__/message.cpython-312
│                │                       │        .pyc 
│                │                       ├ [250]: usr/lib/python3.12/email/mime/__pycache__/multipart.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [251]: usr/lib/python3.12/email/mime/__pycache__/nonmultipart.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [252]: usr/lib/python3.12/email/mime/__pycache__/text.cpython-312.pyc 
│                │                       ├ [253]: usr/lib/python3.12/encodings/__pycache__/__init__.cpython-312
│                │                       │        .pyc 
│                │                       ├ [254]: usr/lib/python3.12/encodings/__pycache__/aliases.cpython-312.
│                │                       │        pyc 
│                │                       ├ [255]: usr/lib/python3.12/encodings/__pycache__/ascii.cpython-312.pyc 
│                │                       ├ [256]: usr/lib/python3.12/encodings/__pycache__/base64_codec.cpython
│                │                       │        -312.pyc 
│                │                       ├ [257]: usr/lib/python3.12/encodings/__pycache__/big5.cpython-312.pyc 
│                │                       ├ [258]: usr/lib/python3.12/encodings/__pycache__/big5hkscs.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [259]: usr/lib/python3.12/encodings/__pycache__/bz2_codec.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [260]: usr/lib/python3.12/encodings/__pycache__/charmap.cpython-312.
│                │                       │        pyc 
│                │                       ├ [261]: usr/lib/python3.12/encodings/__pycache__/cp037.cpython-312.pyc 
│                │                       ├ [262]: usr/lib/python3.12/encodings/__pycache__/cp1006.cpython-312.pyc 
│                │                       ├ [263]: usr/lib/python3.12/encodings/__pycache__/cp1026.cpython-312.pyc 
│                │                       ├ [264]: usr/lib/python3.12/encodings/__pycache__/cp1125.cpython-312.pyc 
│                │                       ├ [265]: usr/lib/python3.12/encodings/__pycache__/cp1140.cpython-312.pyc 
│                │                       ├ [266]: usr/lib/python3.12/encodings/__pycache__/cp1250.cpython-312.pyc 
│                │                       ├ [267]: usr/lib/python3.12/encodings/__pycache__/cp1251.cpython-312.pyc 
│                │                       ├ [268]: usr/lib/python3.12/encodings/__pycache__/cp1252.cpython-312.pyc 
│                │                       ├ [269]: usr/lib/python3.12/encodings/__pycache__/cp1253.cpython-312.pyc 
│                │                       ├ [270]: usr/lib/python3.12/encodings/__pycache__/cp1254.cpython-312.pyc 
│                │                       ├ [271]: usr/lib/python3.12/encodings/__pycache__/cp1255.cpython-312.pyc 
│                │                       ├ [272]: usr/lib/python3.12/encodings/__pycache__/cp1256.cpython-312.pyc 
│                │                       ├ [273]: usr/lib/python3.12/encodings/__pycache__/cp1257.cpython-312.pyc 
│                │                       ├ [274]: usr/lib/python3.12/encodings/__pycache__/cp1258.cpython-312.pyc 
│                │                       ├ [275]: usr/lib/python3.12/encodings/__pycache__/cp273.cpython-312.pyc 
│                │                       ├ [276]: usr/lib/python3.12/encodings/__pycache__/cp424.cpython-312.pyc 
│                │                       ├ [277]: usr/lib/python3.12/encodings/__pycache__/cp437.cpython-312.pyc 
│                │                       ├ [278]: usr/lib/python3.12/encodings/__pycache__/cp500.cpython-312.pyc 
│                │                       ├ [279]: usr/lib/python3.12/encodings/__pycache__/cp720.cpython-312.pyc 
│                │                       ├ [280]: usr/lib/python3.12/encodings/__pycache__/cp737.cpython-312.pyc 
│                │                       ├ [281]: usr/lib/python3.12/encodings/__pycache__/cp775.cpython-312.pyc 
│                │                       ├ [282]: usr/lib/python3.12/encodings/__pycache__/cp850.cpython-312.pyc 
│                │                       ├ [283]: usr/lib/python3.12/encodings/__pycache__/cp852.cpython-312.pyc 
│                │                       ├ [284]: usr/lib/python3.12/encodings/__pycache__/cp855.cpython-312.pyc 
│                │                       ├ [285]: usr/lib/python3.12/encodings/__pycache__/cp856.cpython-312.pyc 
│                │                       ├ [286]: usr/lib/python3.12/encodings/__pycache__/cp857.cpython-312.pyc 
│                │                       ├ [287]: usr/lib/python3.12/encodings/__pycache__/cp858.cpython-312.pyc 
│                │                       ├ [288]: usr/lib/python3.12/encodings/__pycache__/cp860.cpython-312.pyc 
│                │                       ├ [289]: usr/lib/python3.12/encodings/__pycache__/cp861.cpython-312.pyc 
│                │                       ├ [290]: usr/lib/python3.12/encodings/__pycache__/cp862.cpython-312.pyc 
│                │                       ├ [291]: usr/lib/python3.12/encodings/__pycache__/cp863.cpython-312.pyc 
│                │                       ├ [292]: usr/lib/python3.12/encodings/__pycache__/cp864.cpython-312.pyc 
│                │                       ├ [293]: usr/lib/python3.12/encodings/__pycache__/cp865.cpython-312.pyc 
│                │                       ├ [294]: usr/lib/python3.12/encodings/__pycache__/cp866.cpython-312.pyc 
│                │                       ├ [295]: usr/lib/python3.12/encodings/__pycache__/cp869.cpython-312.pyc 
│                │                       ├ [296]: usr/lib/python3.12/encodings/__pycache__/cp874.cpython-312.pyc 
│                │                       ├ [297]: usr/lib/python3.12/encodings/__pycache__/cp875.cpython-312.pyc 
│                │                       ├ [298]: usr/lib/python3.12/encodings/__pycache__/cp932.cpython-312.pyc 
│                │                       ├ [299]: usr/lib/python3.12/encodings/__pycache__/cp949.cpython-312.pyc 
│                │                       ├ [300]: usr/lib/python3.12/encodings/__pycache__/cp950.cpython-312.pyc 
│                │                       ├ [301]: usr/lib/python3.12/encodings/__pycache__/euc_jis_2004.cpython
│                │                       │        -312.pyc 
│                │                       ├ [302]: usr/lib/python3.12/encodings/__pycache__/euc_jisx0213.cpython
│                │                       │        -312.pyc 
│                │                       ├ [303]: usr/lib/python3.12/encodings/__pycache__/euc_jp.cpython-312.pyc 
│                │                       ├ [304]: usr/lib/python3.12/encodings/__pycache__/euc_kr.cpython-312.pyc 
│                │                       ├ [305]: usr/lib/python3.12/encodings/__pycache__/gb18030.cpython-312.
│                │                       │        pyc 
│                │                       ├ [306]: usr/lib/python3.12/encodings/__pycache__/gb2312.cpython-312.pyc 
│                │                       ├ [307]: usr/lib/python3.12/encodings/__pycache__/gbk.cpython-312.pyc 
│                │                       ├ [308]: usr/lib/python3.12/encodings/__pycache__/hex_codec.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [309]: usr/lib/python3.12/encodings/__pycache__/hp_roman8.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [310]: usr/lib/python3.12/encodings/__pycache__/hz.cpython-312.pyc 
│                │                       ├ [311]: usr/lib/python3.12/encodings/__pycache__/idna.cpython-312.pyc 
│                │                       ├ [312]: usr/lib/python3.12/encodings/__pycache__/iso2022_jp.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [313]: usr/lib/python3.12/encodings/__pycache__/iso2022_jp_1.cpython
│                │                       │        -312.pyc 
│                │                       ├ [314]: usr/lib/python3.12/encodings/__pycache__/iso2022_jp_2.cpython
│                │                       │        -312.pyc 
│                │                       ├ [315]: usr/lib/python3.12/encodings/__pycache__/iso2022_jp_2004.cpyt
│                │                       │        hon-312.pyc 
│                │                       ├ [316]: usr/lib/python3.12/encodings/__pycache__/iso2022_jp_3.cpython
│                │                       │        -312.pyc 
│                │                       ├ [317]: usr/lib/python3.12/encodings/__pycache__/iso2022_jp_ext.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [318]: usr/lib/python3.12/encodings/__pycache__/iso2022_kr.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [319]: usr/lib/python3.12/encodings/__pycache__/iso8859_1.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [320]: usr/lib/python3.12/encodings/__pycache__/iso8859_10.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [321]: usr/lib/python3.12/encodings/__pycache__/iso8859_11.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [322]: usr/lib/python3.12/encodings/__pycache__/iso8859_13.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [323]: usr/lib/python3.12/encodings/__pycache__/iso8859_14.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [324]: usr/lib/python3.12/encodings/__pycache__/iso8859_15.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [325]: usr/lib/python3.12/encodings/__pycache__/iso8859_16.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [326]: usr/lib/python3.12/encodings/__pycache__/iso8859_2.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [327]: usr/lib/python3.12/encodings/__pycache__/iso8859_3.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [328]: usr/lib/python3.12/encodings/__pycache__/iso8859_4.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [329]: usr/lib/python3.12/encodings/__pycache__/iso8859_5.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [330]: usr/lib/python3.12/encodings/__pycache__/iso8859_6.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [331]: usr/lib/python3.12/encodings/__pycache__/iso8859_7.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [332]: usr/lib/python3.12/encodings/__pycache__/iso8859_8.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [333]: usr/lib/python3.12/encodings/__pycache__/iso8859_9.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [334]: usr/lib/python3.12/encodings/__pycache__/johab.cpython-312.pyc 
│                │                       ├ [335]: usr/lib/python3.12/encodings/__pycache__/koi8_r.cpython-312.pyc 
│                │                       ├ [336]: usr/lib/python3.12/encodings/__pycache__/koi8_t.cpython-312.pyc 
│                │                       ├ [337]: usr/lib/python3.12/encodings/__pycache__/koi8_u.cpython-312.pyc 
│                │                       ├ [338]: usr/lib/python3.12/encodings/__pycache__/kz1048.cpython-312.pyc 
│                │                       ├ [339]: usr/lib/python3.12/encodings/__pycache__/latin_1.cpython-312.
│                │                       │        pyc 
│                │                       ├ [340]: usr/lib/python3.12/encodings/__pycache__/mac_arabic.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [341]: usr/lib/python3.12/encodings/__pycache__/mac_croatian.cpython
│                │                       │        -312.pyc 
│                │                       ├ [342]: usr/lib/python3.12/encodings/__pycache__/mac_cyrillic.cpython
│                │                       │        -312.pyc 
│                │                       ├ [343]: usr/lib/python3.12/encodings/__pycache__/mac_farsi.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [344]: usr/lib/python3.12/encodings/__pycache__/mac_greek.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [345]: usr/lib/python3.12/encodings/__pycache__/mac_iceland.cpython-
│                │                       │        312.pyc 
│                │                       ├ [346]: usr/lib/python3.12/encodings/__pycache__/mac_latin2.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [347]: usr/lib/python3.12/encodings/__pycache__/mac_roman.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [348]: usr/lib/python3.12/encodings/__pycache__/mac_romanian.cpython
│                │                       │        -312.pyc 
│                │                       ├ [349]: usr/lib/python3.12/encodings/__pycache__/mac_turkish.cpython-
│                │                       │        312.pyc 
│                │                       ├ [350]: usr/lib/python3.12/encodings/__pycache__/mbcs.cpython-312.pyc 
│                │                       ├ [351]: usr/lib/python3.12/encodings/__pycache__/oem.cpython-312.pyc 
│                │                       ├ [352]: usr/lib/python3.12/encodings/__pycache__/palmos.cpython-312.pyc 
│                │                       ├ [353]: usr/lib/python3.12/encodings/__pycache__/ptcp154.cpython-312.
│                │                       │        pyc 
│                │                       ├ [354]: usr/lib/python3.12/encodings/__pycache__/punycode.cpython-312
│                │                       │        .pyc 
│                │                       ├ [355]: usr/lib/python3.12/encodings/__pycache__/quopri_codec.cpython
│                │                       │        -312.pyc 
│                │                       ├ [356]: usr/lib/python3.12/encodings/__pycache__/raw_unicode_escape.c
│                │                       │        python-312.pyc 
│                │                       ├ [357]: usr/lib/python3.12/encodings/__pycache__/rot_13.cpython-312.pyc 
│                │                       ├ [358]: usr/lib/python3.12/encodings/__pycache__/shift_jis.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [359]: usr/lib/python3.12/encodings/__pycache__/shift_jis_2004.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [360]: usr/lib/python3.12/encodings/__pycache__/shift_jisx0213.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [361]: usr/lib/python3.12/encodings/__pycache__/tis_620.cpython-312.
│                │                       │        pyc 
│                │                       ├ [362]: usr/lib/python3.12/encodings/__pycache__/undefined.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [363]: usr/lib/python3.12/encodings/__pycache__/unicode_escape.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [364]: usr/lib/python3.12/encodings/__pycache__/utf_16.cpython-312.pyc 
│                │                       ├ [365]: usr/lib/python3.12/encodings/__pycache__/utf_16_be.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [366]: usr/lib/python3.12/encodings/__pycache__/utf_16_le.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [367]: usr/lib/python3.12/encodings/__pycache__/utf_32.cpython-312.pyc 
│                │                       ├ [368]: usr/lib/python3.12/encodings/__pycache__/utf_32_be.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [369]: usr/lib/python3.12/encodings/__pycache__/utf_32_le.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [370]: usr/lib/python3.12/encodings/__pycache__/utf_7.cpython-312.pyc 
│                │                       ├ [371]: usr/lib/python3.12/encodings/__pycache__/utf_8.cpython-312.pyc 
│                │                       ├ [372]: usr/lib/python3.12/encodings/__pycache__/utf_8_sig.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [373]: usr/lib/python3.12/encodings/__pycache__/uu_codec.cpython-312
│                │                       │        .pyc 
│                │                       ├ [374]: usr/lib/python3.12/encodings/__pycache__/zlib_codec.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [375]: usr/lib/python3.12/ensurepip/__pycache__/__init__.cpython-312
│                │                       │        .pyc 
│                │                       ├ [376]: usr/lib/python3.12/ensurepip/__pycache__/__main__.cpython-312
│                │                       │        .pyc 
│                │                       ├ [377]: usr/lib/python3.12/ensurepip/__pycache__/_uninstall.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [378]: usr/lib/python3.12/html/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [379]: usr/lib/python3.12/html/__pycache__/entities.cpython-312.pyc 
│                │                       ├ [380]: usr/lib/python3.12/html/__pycache__/parser.cpython-312.pyc 
│                │                       ├ [381]: usr/lib/python3.12/http/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [382]: usr/lib/python3.12/http/__pycache__/client.cpython-312.pyc 
│                │                       ├ [383]: usr/lib/python3.12/http/__pycache__/cookiejar.cpython-312.pyc 
│                │                       ├ [384]: usr/lib/python3.12/http/__pycache__/cookies.cpython-312.pyc 
│                │                       ├ [385]: usr/lib/python3.12/http/__pycache__/server.cpython-312.pyc 
│                │                       ├ [386]: usr/lib/python3.12/importlib/__pycache__/__init__.cpython-312
│                │                       │        .pyc 
│                │                       ├ [387]: usr/lib/python3.12/importlib/__pycache__/_abc.cpython-312.pyc 
│                │                       ├ [388]: usr/lib/python3.12/importlib/__pycache__/_bootstrap.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [389]: usr/lib/python3.12/importlib/__pycache__/_bootstrap_external.
│                │                       │        cpython-312.pyc 
│                │                       ├ [390]: usr/lib/python3.12/importlib/__pycache__/abc.cpython-312.pyc 
│                │                       ├ [391]: usr/lib/python3.12/importlib/__pycache__/machinery.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [392]: usr/lib/python3.12/importlib/__pycache__/readers.cpython-312.
│                │                       │        pyc 
│                │                       ├ [393]: usr/lib/python3.12/importlib/__pycache__/simple.cpython-312.pyc 
│                │                       ├ [394]: usr/lib/python3.12/importlib/__pycache__/util.cpython-312.pyc 
│                │                       ├ [395]: usr/lib/python3.12/importlib/metadata/__pycache__/__init__.cp
│                │                       │        ython-312.pyc 
│                │                       ├ [396]: usr/lib/python3.12/importlib/metadata/__pycache__/_adapters.c
│                │                       │        python-312.pyc 
│                │                       ├ [397]: usr/lib/python3.12/importlib/metadata/__pycache__/_collection
│                │                       │        s.cpython-312.pyc 
│                │                       ├ [398]: usr/lib/python3.12/importlib/metadata/__pycache__/_functools.
│                │                       │        cpython-312.pyc 
│                │                       ├ [399]: usr/lib/python3.12/importlib/metadata/__pycache__/_itertools.
│                │                       │        cpython-312.pyc 
│                │                       ├ [400]: usr/lib/python3.12/importlib/metadata/__pycache__/_meta.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [401]: usr/lib/python3.12/importlib/metadata/__pycache__/_text.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [402]: usr/lib/python3.12/importlib/resources/__pycache__/__init__.c
│                │                       │        python-312.pyc 
│                │                       ├ [403]: usr/lib/python3.12/importlib/resources/__pycache__/_adapters.
│                │                       │        cpython-312.pyc 
│                │                       ├ [404]: usr/lib/python3.12/importlib/resources/__pycache__/_common.cp
│                │                       │        ython-312.pyc 
│                │                       ├ [405]: usr/lib/python3.12/importlib/resources/__pycache__/_itertools
│                │                       │        .cpython-312.pyc 
│                │                       ├ [406]: usr/lib/python3.12/importlib/resources/__pycache__/_legacy.cp
│                │                       │        ython-312.pyc 
│                │                       ├ [407]: usr/lib/python3.12/importlib/resources/__pycache__/abc.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [408]: usr/lib/python3.12/importlib/resources/__pycache__/readers.cp
│                │                       │        ython-312.pyc 
│                │                       ├ [409]: usr/lib/python3.12/importlib/resources/__pycache__/simple.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [410]: usr/lib/python3.12/json/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [411]: usr/lib/python3.12/json/__pycache__/decoder.cpython-312.pyc 
│                │                       ├ [412]: usr/lib/python3.12/json/__pycache__/encoder.cpython-312.pyc 
│                │                       ├ [413]: usr/lib/python3.12/json/__pycache__/scanner.cpython-312.pyc 
│                │                       ├ [414]: usr/lib/python3.12/json/__pycache__/tool.cpython-312.pyc 
│                │                       ├ [415]: usr/lib/python3.12/lib2to3/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [416]: usr/lib/python3.12/lib2to3/__pycache__/__main__.cpython-312.pyc 
│                │                       ├ [417]: usr/lib/python3.12/lib2to3/__pycache__/btm_matcher.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [418]: usr/lib/python3.12/lib2to3/__pycache__/btm_utils.cpython-312.
│                │                       │        pyc 
│                │                       ├ [419]: usr/lib/python3.12/lib2to3/__pycache__/fixer_base.cpython-312
│                │                       │        .pyc 
│                │                       ├ [420]: usr/lib/python3.12/lib2to3/__pycache__/fixer_util.cpython-312
│                │                       │        .pyc 
│                │                       ├ [421]: usr/lib/python3.12/lib2to3/__pycache__/main.cpython-312.pyc 
│                │                       ├ [422]: usr/lib/python3.12/lib2to3/__pycache__/patcomp.cpython-312.pyc 
│                │                       ├ [423]: usr/lib/python3.12/lib2to3/__pycache__/pygram.cpython-312.pyc 
│                │                       ├ [424]: usr/lib/python3.12/lib2to3/__pycache__/pytree.cpython-312.pyc 
│                │                       ├ [425]: usr/lib/python3.12/lib2to3/__pycache__/refactor.cpython-312.pyc 
│                │                       ├ [426]: usr/lib/python3.12/lib2to3/fixes/__pycache__/__init__.cpython
│                │                       │        -312.pyc 
│                │                       ├ [427]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_apply.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [428]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_asserts.cpyt
│                │                       │        hon-312.pyc 
│                │                       ├ [429]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_basestring.c
│                │                       │        python-312.pyc 
│                │                       ├ [430]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_buffer.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [431]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_dict.cpython
│                │                       │        -312.pyc 
│                │                       ├ [432]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_except.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [433]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_exec.cpython
│                │                       │        -312.pyc 
│                │                       ├ [434]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_execfile.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [435]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_exitfunc.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [436]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_filter.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [437]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_funcattrs.cp
│                │                       │        ython-312.pyc 
│                │                       ├ [438]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_future.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [439]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_getcwdu.cpyt
│                │                       │        hon-312.pyc 
│                │                       ├ [440]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_has_key.cpyt
│                │                       │        hon-312.pyc 
│                │                       ├ [441]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_idioms.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [442]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_import.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [443]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_imports.cpyt
│                │                       │        hon-312.pyc 
│                │                       ├ [444]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_imports2.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [445]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_input.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [446]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_intern.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [447]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_isinstance.c
│                │                       │        python-312.pyc 
│                │                       ├ [448]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_itertools.cp
│                │                       │        ython-312.pyc 
│                │                       ├ [449]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_itertools_im
│                │                       │        ports.cpython-312.pyc 
│                │                       ├ [450]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_long.cpython
│                │                       │        -312.pyc 
│                │                       ├ [451]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_map.cpython-
│                │                       │        312.pyc 
│                │                       ├ [452]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_metaclass.cp
│                │                       │        ython-312.pyc 
│                │                       ├ [453]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_methodattrs.
│                │                       │        cpython-312.pyc 
│                │                       ├ [454]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_ne.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [455]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_next.cpython
│                │                       │        -312.pyc 
│                │                       ├ [456]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_nonzero.cpyt
│                │                       │        hon-312.pyc 
│                │                       ├ [457]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_numliterals.
│                │                       │        cpython-312.pyc 
│                │                       ├ [458]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_operator.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [459]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_paren.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [460]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_print.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [461]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_raise.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [462]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_raw_input.cp
│                │                       │        ython-312.pyc 
│                │                       ├ [463]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_reduce.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [464]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_reload.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [465]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_renames.cpyt
│                │                       │        hon-312.pyc 
│                │                       ├ [466]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_repr.cpython
│                │                       │        -312.pyc 
│                │                       ├ [467]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_set_literal.
│                │                       │        cpython-312.pyc 
│                │                       ├ [468]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_standarderro
│                │                       │        r.cpython-312.pyc 
│                │                       ├ [469]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_sys_exc.cpyt
│                │                       │        hon-312.pyc 
│                │                       ├ [470]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_throw.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [471]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_tuple_params
│                │                       │        .cpython-312.pyc 
│                │                       ├ [472]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_types.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [473]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_unicode.cpyt
│                │                       │        hon-312.pyc 
│                │                       ├ [474]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_urllib.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [475]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_ws_comma.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [476]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_xrange.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [477]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_xreadlines.c
│                │                       │        python-312.pyc 
│                │                       ├ [478]: usr/lib/python3.12/lib2to3/fixes/__pycache__/fix_zip.cpython-
│                │                       │        312.pyc 
│                │                       ├ [479]: usr/lib/python3.12/lib2to3/pgen2/__pycache__/__init__.cpython
│                │                       │        -312.pyc 
│                │                       ├ [480]: usr/lib/python3.12/lib2to3/pgen2/__pycache__/conv.cpython-312
│                │                       │        .pyc 
│                │                       ├ [481]: usr/lib/python3.12/lib2to3/pgen2/__pycache__/driver.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [482]: usr/lib/python3.12/lib2to3/pgen2/__pycache__/grammar.cpython-
│                │                       │        312.pyc 
│                │                       ├ [483]: usr/lib/python3.12/lib2to3/pgen2/__pycache__/literals.cpython
│                │                       │        -312.pyc 
│                │                       ├ [484]: usr/lib/python3.12/lib2to3/pgen2/__pycache__/parse.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [485]: usr/lib/python3.12/lib2to3/pgen2/__pycache__/pgen.cpython-312
│                │                       │        .pyc 
│                │                       ├ [486]: usr/lib/python3.12/lib2to3/pgen2/__pycache__/token.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [487]: usr/lib/python3.12/lib2to3/pgen2/__pycache__/tokenize.cpython
│                │                       │        -312.pyc 
│                │                       ├ [488]: usr/lib/python3.12/logging/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [489]: usr/lib/python3.12/logging/__pycache__/config.cpython-312.pyc 
│                │                       ├ [490]: usr/lib/python3.12/logging/__pycache__/handlers.cpython-312.pyc 
│                │                       ├ [491]: usr/lib/python3.12/multiprocessing/__pycache__/__init__.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [492]: usr/lib/python3.12/multiprocessing/__pycache__/connection.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [493]: usr/lib/python3.12/multiprocessing/__pycache__/context.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [494]: usr/lib/python3.12/multiprocessing/__pycache__/forkserver.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [495]: usr/lib/python3.12/multiprocessing/__pycache__/heap.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [496]: usr/lib/python3.12/multiprocessing/__pycache__/managers.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [497]: usr/lib/python3.12/multiprocessing/__pycache__/pool.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [498]: usr/lib/python3.12/multiprocessing/__pycache__/popen_fork.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [499]: usr/lib/python3.12/multiprocessing/__pycache__/popen_forkserv
│                │                       │        er.cpython-312.pyc 
│                │                       ├ [500]: usr/lib/python3.12/multiprocessing/__pycache__/popen_spawn_po
│                │                       │        six.cpython-312.pyc 
│                │                       ├ [501]: usr/lib/python3.12/multiprocessing/__pycache__/popen_spawn_wi
│                │                       │        n32.cpython-312.pyc 
│                │                       ├ [502]: usr/lib/python3.12/multiprocessing/__pycache__/process.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [503]: usr/lib/python3.12/multiprocessing/__pycache__/queues.cpython
│                │                       │        -312.pyc 
│                │                       ├ [504]: usr/lib/python3.12/multiprocessing/__pycache__/reduction.cpyt
│                │                       │        hon-312.pyc 
│                │                       ├ [505]: usr/lib/python3.12/multiprocessing/__pycache__/resource_share
│                │                       │        r.cpython-312.pyc 
│                │                       ├ [506]: usr/lib/python3.12/multiprocessing/__pycache__/resource_track
│                │                       │        er.cpython-312.pyc 
│                │                       ├ [507]: usr/lib/python3.12/multiprocessing/__pycache__/shared_memory.
│                │                       │        cpython-312.pyc 
│                │                       ├ [508]: usr/lib/python3.12/multiprocessing/__pycache__/sharedctypes.c
│                │                       │        python-312.pyc 
│                │                       ├ [509]: usr/lib/python3.12/multiprocessing/__pycache__/spawn.cpython-
│                │                       │        312.pyc 
│                │                       ├ [510]: usr/lib/python3.12/multiprocessing/__pycache__/synchronize.cp
│                │                       │        ython-312.pyc 
│                │                       ├ [511]: usr/lib/python3.12/multiprocessing/__pycache__/util.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [512]: usr/lib/python3.12/multiprocessing/dummy/__pycache__/__init__
│                │                       │        .cpython-312.pyc 
│                │                       ├ [513]: usr/lib/python3.12/multiprocessing/dummy/__pycache__/connecti
│                │                       │        on.cpython-312.pyc 
│                │                       ├ [514]: usr/lib/python3.12/pydoc_data/__pycache__/__init__.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [515]: usr/lib/python3.12/pydoc_data/__pycache__/topics.cpython-312.
│                │                       │        pyc 
│                │                       ├ [516]: usr/lib/python3.12/re/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [517]: usr/lib/python3.12/re/__pycache__/_casefix.cpython-312.pyc 
│                │                       ├ [518]: usr/lib/python3.12/re/__pycache__/_compiler.cpython-312.pyc 
│                │                       ├ [519]: usr/lib/python3.12/re/__pycache__/_constants.cpython-312.pyc 
│                │                       ├ [520]: usr/lib/python3.12/re/__pycache__/_parser.cpython-312.pyc 
│                │                       ├ [521]: usr/lib/python3.12/sqlite3/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [522]: usr/lib/python3.12/sqlite3/__pycache__/__main__.cpython-312.pyc 
│                │                       ├ [523]: usr/lib/python3.12/sqlite3/__pycache__/dbapi2.cpython-312.pyc 
│                │                       ├ [524]: usr/lib/python3.12/sqlite3/__pycache__/dump.cpython-312.pyc 
│                │                       ├ [525]: usr/lib/python3.12/tomllib/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [526]: usr/lib/python3.12/tomllib/__pycache__/_parser.cpython-312.pyc 
│                │                       ├ [527]: usr/lib/python3.12/tomllib/__pycache__/_re.cpython-312.pyc 
│                │                       ├ [528]: usr/lib/python3.12/tomllib/__pycache__/_types.cpython-312.pyc 
│                │                       ├ [529]: usr/lib/python3.12/turtledemo/__pycache__/__init__.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [530]: usr/lib/python3.12/turtledemo/__pycache__/__main__.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [531]: usr/lib/python3.12/turtledemo/__pycache__/bytedesign.cpython-
│                │                       │        312.pyc 
│                │                       ├ [532]: usr/lib/python3.12/turtledemo/__pycache__/chaos.cpython-312.pyc 
│                │                       ├ [533]: usr/lib/python3.12/turtledemo/__pycache__/clock.cpython-312.pyc 
│                │                       ├ [534]: usr/lib/python3.12/turtledemo/__pycache__/colormixer.cpython-
│                │                       │        312.pyc 
│                │                       ├ [535]: usr/lib/python3.12/turtledemo/__pycache__/forest.cpython-312.
│                │                       │        pyc 
│                │                       ├ [536]: usr/lib/python3.12/turtledemo/__pycache__/fractalcurves.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [537]: usr/lib/python3.12/turtledemo/__pycache__/lindenmayer.cpython
│                │                       │        -312.pyc 
│                │                       ├ [538]: usr/lib/python3.12/turtledemo/__pycache__/minimal_hanoi.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [539]: usr/lib/python3.12/turtledemo/__pycache__/nim.cpython-312.pyc 
│                │                       ├ [540]: usr/lib/python3.12/turtledemo/__pycache__/paint.cpython-312.pyc 
│                │                       ├ [541]: usr/lib/python3.12/turtledemo/__pycache__/peace.cpython-312.pyc 
│                │                       ├ [542]: usr/lib/python3.12/turtledemo/__pycache__/penrose.cpython-312
│                │                       │        .pyc 
│                │                       ├ [543]: usr/lib/python3.12/turtledemo/__pycache__/planet_and_moon.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [544]: usr/lib/python3.12/turtledemo/__pycache__/rosette.cpython-312
│                │                       │        .pyc 
│                │                       ├ [545]: usr/lib/python3.12/turtledemo/__pycache__/round_dance.cpython
│                │                       │        -312.pyc 
│                │                       ├ [546]: usr/lib/python3.12/turtledemo/__pycache__/sorting_animate.cpy
│                │                       │        thon-312.pyc 
│                │                       ├ [547]: usr/lib/python3.12/turtledemo/__pycache__/tree.cpython-312.pyc 
│                │                       ├ [548]: usr/lib/python3.12/turtledemo/__pycache__/two_canvases.cpytho
│                │                       │        n-312.pyc 
│                │                       ├ [549]: usr/lib/python3.12/turtledemo/__pycache__/yinyang.cpython-312
│                │                       │        .pyc 
│                │                       ├ [550]: usr/lib/python3.12/unittest/__pycache__/__init__.cpython-312.
│                │                       │        pyc 
│                │                       ├ [551]: usr/lib/python3.12/unittest/__pycache__/__main__.cpython-312.
│                │                       │        pyc 
│                │                       ├ [552]: usr/lib/python3.12/unittest/__pycache__/_log.cpython-312.pyc 
│                │                       ├ [553]: usr/lib/python3.12/unittest/__pycache__/async_case.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [554]: usr/lib/python3.12/unittest/__pycache__/case.cpython-312.pyc 
│                │                       ├ [555]: usr/lib/python3.12/unittest/__pycache__/loader.cpython-312.pyc 
│                │                       ├ [556]: usr/lib/python3.12/unittest/__pycache__/main.cpython-312.pyc 
│                │                       ├ [557]: usr/lib/python3.12/unittest/__pycache__/mock.cpython-312.pyc 
│                │                       ├ [558]: usr/lib/python3.12/unittest/__pycache__/result.cpython-312.pyc 
│                │                       ├ [559]: usr/lib/python3.12/unittest/__pycache__/runner.cpython-312.pyc 
│                │                       ├ [560]: usr/lib/python3.12/unittest/__pycache__/signals.cpython-312.pyc 
│                │                       ├ [561]: usr/lib/python3.12/unittest/__pycache__/suite.cpython-312.pyc 
│                │                       ├ [562]: usr/lib/python3.12/unittest/__pycache__/util.cpython-312.pyc 
│                │                       ├ [563]: usr/lib/python3.12/urllib/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [564]: usr/lib/python3.12/urllib/__pycache__/error.cpython-312.pyc 
│                │                       ├ [565]: usr/lib/python3.12/urllib/__pycache__/parse.cpython-312.pyc 
│                │                       ├ [566]: usr/lib/python3.12/urllib/__pycache__/request.cpython-312.pyc 
│                │                       ├ [567]: usr/lib/python3.12/urllib/__pycache__/response.cpython-312.pyc 
│                │                       ├ [568]: usr/lib/python3.12/urllib/__pycache__/robotparser.cpython-312
│                │                       │        .pyc 
│                │                       ├ [569]: usr/lib/python3.12/venv/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [570]: usr/lib/python3.12/venv/__pycache__/__main__.cpython-312.pyc 
│                │                       ├ [571]: usr/lib/python3.12/wsgiref/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [572]: usr/lib/python3.12/wsgiref/__pycache__/handlers.cpython-312.pyc 
│                │                       ├ [573]: usr/lib/python3.12/wsgiref/__pycache__/headers.cpython-312.pyc 
│                │                       ├ [574]: usr/lib/python3.12/wsgiref/__pycache__/simple_server.cpython-
│                │                       │        312.pyc 
│                │                       ├ [575]: usr/lib/python3.12/wsgiref/__pycache__/types.cpython-312.pyc 
│                │                       ├ [576]: usr/lib/python3.12/wsgiref/__pycache__/util.cpython-312.pyc 
│                │                       ├ [577]: usr/lib/python3.12/wsgiref/__pycache__/validate.cpython-312.pyc 
│                │                       ├ [578]: usr/lib/python3.12/xml/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [579]: usr/lib/python3.12/xml/dom/__pycache__/NodeFilter.cpython-312
│                │                       │        .pyc 
│                │                       ├ [580]: usr/lib/python3.12/xml/dom/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [581]: usr/lib/python3.12/xml/dom/__pycache__/domreg.cpython-312.pyc 
│                │                       ├ [582]: usr/lib/python3.12/xml/dom/__pycache__/expatbuilder.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [583]: usr/lib/python3.12/xml/dom/__pycache__/minicompat.cpython-312
│                │                       │        .pyc 
│                │                       ├ [584]: usr/lib/python3.12/xml/dom/__pycache__/minidom.cpython-312.pyc 
│                │                       ├ [585]: usr/lib/python3.12/xml/dom/__pycache__/pulldom.cpython-312.pyc 
│                │                       ├ [586]: usr/lib/python3.12/xml/dom/__pycache__/xmlbuilder.cpython-312
│                │                       │        .pyc 
│                │                       ├ [587]: usr/lib/python3.12/xml/etree/__pycache__/ElementInclude.cpyth
│                │                       │        on-312.pyc 
│                │                       ├ [588]: usr/lib/python3.12/xml/etree/__pycache__/ElementPath.cpython-
│                │                       │        312.pyc 
│                │                       ├ [589]: usr/lib/python3.12/xml/etree/__pycache__/ElementTree.cpython-
│                │                       │        312.pyc 
│                │                       ├ [590]: usr/lib/python3.12/xml/etree/__pycache__/__init__.cpython-312
│                │                       │        .pyc 
│                │                       ├ [591]: usr/lib/python3.12/xml/etree/__pycache__/cElementTree.cpython
│                │                       │        -312.pyc 
│                │                       ├ [592]: usr/lib/python3.12/xml/parsers/__pycache__/__init__.cpython-3
│                │                       │        12.pyc 
│                │                       ├ [593]: usr/lib/python3.12/xml/parsers/__pycache__/expat.cpython-312.
│                │                       │        pyc 
│                │                       ├ [594]: usr/lib/python3.12/xml/sax/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [595]: usr/lib/python3.12/xml/sax/__pycache__/_exceptions.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [596]: usr/lib/python3.12/xml/sax/__pycache__/expatreader.cpython-31
│                │                       │        2.pyc 
│                │                       ├ [597]: usr/lib/python3.12/xml/sax/__pycache__/handler.cpython-312.pyc 
│                │                       ├ [598]: usr/lib/python3.12/xml/sax/__pycache__/saxutils.cpython-312.pyc 
│                │                       ├ [599]: usr/lib/python3.12/xml/sax/__pycache__/xmlreader.cpython-312.
│                │                       │        pyc 
│                │                       ├ [600]: usr/lib/python3.12/xmlrpc/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [601]: usr/lib/python3.12/xmlrpc/__pycache__/client.cpython-312.pyc 
│                │                       ├ [602]: usr/lib/python3.12/xmlrpc/__pycache__/server.cpython-312.pyc 
│                │                       ├ [603]: usr/lib/python3.12/zipfile/__pycache__/__init__.cpython-312.pyc 
│                │                       ├ [604]: usr/lib/python3.12/zipfile/__pycache__/__main__.cpython-312.pyc 
│                │                       ├ [605]: usr/lib/python3.12/zipfile/_path/__pycache__/__init__.cpython
│                │                       │        -312.pyc 
│                │                       ├ [606]: usr/lib/python3.12/zipfile/_path/__pycache__/glob.cpython-312
│                │                       │        .pyc 
│                │                       ├ [607]: usr/lib/python3.12/zoneinfo/__pycache__/__init__.cpython-312.
│                │                       │        pyc 
│                │                       ├ [608]: usr/lib/python3.12/zoneinfo/__pycache__/_common.cpython-312.pyc 
│                │                       ├ [609]: usr/lib/python3.12/zoneinfo/__pycache__/_tzpath.cpython-312.pyc 
│                │                       ╰ [610]: usr/lib/python3.12/zoneinfo/__pycache__/_zoneinfo.cpython-312
│                │                                .pyc 
│                ├ [69] ╭ ID            : readline@8.3.1-r0 
│                │      ├ Name          : readline 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/readline@8.3.1-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 4280e2fd4a1d9dfe 
│                │      ├ Version       : 8.3.1-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : readline 
│                │      ├ SrcVersion    : 8.3.1-r0 
│                │      ├ Licenses       ─ [0]: GPL-3.0-or-later 
│                │      ├ Maintainer    : Celeste <cielesti@protonmail.com> 
│                │      ├ DependsOn      ╭ [0]: libncursesw@6.5_p20251123-r0 
│                │      │                ╰ [1]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:8aeb81b3a477f922b9b6a533381114c63dd928fe 
│                │      ╰ InstalledFiles ╭ [0]: etc/inputrc 
│                │                       ├ [1]: usr/lib/libreadline.so.8 
│                │                       ╰ [2]: usr/lib/libreadline.so.8.3 
│                ├ [70] ╭ ID            : scanelf@1.3.8-r2 
│                │      ├ Name          : scanelf 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/scanelf@1.3.8-r2?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 40949233d54f5297 
│                │      ├ Version       : 1.3.8-r2 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : pax-utils 
│                │      ├ SrcVersion    : 1.3.8-r2 
│                │      ├ Licenses       ─ [0]: GPL-2.0-only 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:6ea36dd44ef9f6364f0cdfabe09ea15d2fdbe229 
│                │      ╰ InstalledFiles ─ [0]: usr/bin/scanelf 
│                ├ [71] ╭ ID            : sqlite-libs@3.51.1-r0 
│                │      ├ Name          : sqlite-libs 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/sqlite-libs@3.51.1-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : e5e30bb7ff9aaca9 
│                │      ├ Version       : 3.51.1-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : sqlite 
│                │      ├ SrcVersion    : 3.51.1-r0 
│                │      ├ Licenses       ─ [0]: blessing 
│                │      ├ Maintainer    : Celeste <cielesti@protonmail.com> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:9bfc54f88e4ed995b47fa4828f5bac6416f1c2db 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libsqlite3.so.0 
│                │                       ╰ [1]: usr/lib/libsqlite3.so.3.51.1 
│                ├ [72] ╭ ID            : ssl_client@1.37.0-r30 
│                │      ├ Name          : ssl_client 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/ssl_client@1.37.0-r30?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : fd27e09d6ac385bf 
│                │      ├ Version       : 1.37.0-r30 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : busybox 
│                │      ├ SrcVersion    : 1.37.0-r30 
│                │      ├ Licenses       ─ [0]: GPL-2.0-only 
│                │      ├ Maintainer    : Sören Tempel <soeren+alpine@soeren-tempel.net> 
│                │      ├ DependsOn      ╭ [0]: libcrypto3@3.5.4-r0 
│                │      │                ├ [1]: libssl3@3.5.4-r0 
│                │      │                ╰ [2]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:5b6ec0939cfc9be47d9677a3152c547cc18b5edd 
│                │      ╰ InstalledFiles ─ [0]: usr/bin/ssl_client 
│                ├ [73] ╭ ID            : sudo@1.9.17_p2-r0 
│                │      ├ Name          : sudo 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/sudo@1.9.17_p2-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 35f8e6a2b9015b57 
│                │      ├ Version       : 1.9.17_p2-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : sudo 
│                │      ├ SrcVersion    : 1.9.17_p2-r0 
│                │      ├ Licenses       ╭ [0]: custom 
│                │      │                ╰ [1]: ISC 
│                │      ├ Maintainer    : Celeste <cielesti@protonmail.com> 
│                │      ├ DependsOn      ╭ [0]: musl@1.2.5-r21 
│                │      │                ╰ [1]: zlib@1.3.1-r2 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:130531eafa71df74c196ee9c1fbdaedc1b92a1cd 
│                │      ╰ InstalledFiles ╭ [0] : etc/sudo.conf 
│                │                       ├ [1] : etc/sudo_logsrvd.conf 
│                │                       ├ [2] : etc/sudoers 
│                │                       ├ [3] : usr/bin/cvtsudoers 
│                │                       ├ [4] : usr/bin/sudo 
│                │                       ├ [5] : usr/bin/sudoedit 
│                │                       ├ [6] : usr/bin/sudoreplay 
│                │                       ├ [7] : usr/lib/sudo/audit_json.so 
│                │                       ├ [8] : usr/lib/sudo/group_file.so 
│                │                       ├ [9] : usr/lib/sudo/libsudo_util.so 
│                │                       ├ [10]: usr/lib/sudo/libsudo_util.so.0 
│                │                       ├ [11]: usr/lib/sudo/libsudo_util.so.0.0.0 
│                │                       ├ [12]: usr/lib/sudo/sudo_intercept.so 
│                │                       ├ [13]: usr/lib/sudo/sudo_noexec.so 
│                │                       ├ [14]: usr/lib/sudo/sudoers.so 
│                │                       ├ [15]: usr/lib/sudo/system_group.so 
│                │                       ├ [16]: usr/sbin/sudo_logsrvd 
│                │                       ├ [17]: usr/sbin/sudo_sendlog 
│                │                       ╰ [18]: usr/sbin/visudo 
│                ├ [74] ╭ ID            : xz-libs@5.8.1-r0 
│                │      ├ Name          : xz-libs 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/xz-libs@5.8.1-r0?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : b4b5ed40dad1522a 
│                │      ├ Version       : 5.8.1-r0 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : xz 
│                │      ├ SrcVersion    : 5.8.1-r0 
│                │      ├ Licenses       ╭ [0]: GPL-2.0-or-later 
│                │      │                ├ [1]: 0BSD 
│                │      │                ├ [2]: Public-Domain 
│                │      │                ╰ [3]: LGPL-2.1-or-later 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:e97ef71707f929b48a64e00b1ba7f424e916968387e7144c80335
│                │      │                │         fa386e9e106 
│                │      │                ╰ DiffID: sha256:506144398cbef0ec27b6777f129268e0509d49db73927b77b55cb
│                │      │                          ad7707d9fbb 
│                │      ├ Digest        : sha1:657557db3bbd8752475a7ad1e06da45416191c95 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/liblzma.so.5 
│                │                       ╰ [1]: usr/lib/liblzma.so.5.8.1 
│                ├ [75] ╭ ID            : zlib@1.3.1-r2 
│                │      ├ Name          : zlib 
│                │      ├ Identifier     ╭ PURL: pkg:apk/alpine/zlib@1.3.1-r2?arch=x86_64&distro=3.23.2 
│                │      │                ╰ UID : 4fcd0ec5030a15a0 
│                │      ├ Version       : 1.3.1-r2 
│                │      ├ Arch          : x86_64 
│                │      ├ SrcName       : zlib 
│                │      ├ SrcVersion    : 1.3.1-r2 
│                │      ├ Licenses       ─ [0]: Zlib 
│                │      ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                │      ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                │      ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                │      │                │         ffbb346f872 
│                │      │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                │      │                          6c60b969984 
│                │      ├ Digest        : sha1:3e8e8e76dfefb4efd27658ada6d792e66ba2775e 
│                │      ╰ InstalledFiles ╭ [0]: usr/lib/libz.so.1 
│                │                       ╰ [1]: usr/lib/libz.so.1.3.1 
│                ╰ [76] ╭ ID            : zstd-libs@1.5.7-r2 
│                       ├ Name          : zstd-libs 
│                       ├ Identifier     ╭ PURL: pkg:apk/alpine/zstd-libs@1.5.7-r2?arch=x86_64&distro=3.23.2 
│                       │                ╰ UID : 42a1f51d30fcfa27 
│                       ├ Version       : 1.5.7-r2 
│                       ├ Arch          : x86_64 
│                       ├ SrcName       : zstd 
│                       ├ SrcVersion    : 1.5.7-r2 
│                       ├ Licenses       ╭ [0]: BSD-3-Clause 
│                       │                ╰ [1]: GPL-2.0-or-later 
│                       ├ Maintainer    : Natanael Copa <ncopa@alpinelinux.org> 
│                       ├ DependsOn      ─ [0]: musl@1.2.5-r21 
│                       ├ Layer          ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359d
│                       │                │         ffbb346f872 
│                       │                ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf185918983
│                       │                          6c60b969984 
│                       ├ Digest        : sha1:d507b8ac3c4335a40405ac20e49bac9d43642be6 
│                       ╰ InstalledFiles ╭ [0]: usr/lib/libzstd.so.1 
│                                        ╰ [1]: usr/lib/libzstd.so.1.5.7 
╰ [1] ╭ Target  : Java 
      ├ Class   : lang-pkgs 
      ├ Type    : jar 
      ╰ Packages ╭ [0]  ╭ Name      : com.fasterxml.jackson.core:jackson-annotations 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.20 
                 │      │            ╰ UID : 8c51c23e51c8ef16 
                 │      ├ Version   : 2.20 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [1]  ╭ Name      : com.fasterxml.jackson.core:jackson-core 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-core@2.20.1 
                 │      │            ╰ UID : 9822b3547f110bc6 
                 │      ├ Version   : 2.20.1 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [2]  ╭ Name      : com.fasterxml.jackson.core:jackson-databind 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.20.1 
                 │      │            ╰ UID : 4f8c9a471ff43465 
                 │      ├ Version   : 2.20.1 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [3]  ╭ Name      : com.fasterxml.jackson.dataformat:jackson-dataformat-toml 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.fasterxml.jackson.dataformat/jackson-dataformat-toml
                 │      │            │       @2.19.2 
                 │      │            ╰ UID : f187132d4296b98 
                 │      ├ Version   : 2.19.2 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [4]  ╭ Name      : com.github.mwiede:jsch 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.github.mwiede/jsch@2.27.7 
                 │      │            ╰ UID : 168f2be2e6ac4be5 
                 │      ├ Version   : 2.27.7 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [5]  ╭ Name      : com.github.vertical-blank:sql-formatter 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.github.vertical-blank/sql-formatter@2.0.5 
                 │      │            ╰ UID : 4aa6d74fa002054a 
                 │      ├ Version   : 2.0.5 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [6]  ╭ Name      : com.google.code.gson:gson 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.google.code.gson/gson@2.13.2 
                 │      │            ╰ UID : a60cbe5d2898b6fd 
                 │      ├ Version   : 2.13.2 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [7]  ╭ Name      : com.googlecode.juniversalchardet:juniversalchardet 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.googlecode.juniversalchardet/juniversalchardet@1.0.3 
                 │      │            ╰ UID : 59979d47f792d6c8 
                 │      ├ Version   : 1.0.3 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [8]  ╭ Name      : com.jcraft:jsch.agentproxy.connector-factory 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.connector-factory@0.0.9 
                 │      │            ╰ UID : c33f344564a099d2 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [9]  ╭ Name      : com.jcraft:jsch.agentproxy.core 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.core@0.0.9 
                 │      │            ╰ UID : 4be7fe5e595d9eb2 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [10] ╭ Name      : com.jcraft:jsch.agentproxy.jsch 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.jsch@0.0.9 
                 │      │            ╰ UID : 2c09ba989715b29 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [11] ╭ Name      : com.jcraft:jsch.agentproxy.pageant 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.pageant@0.0.9 
                 │      │            ╰ UID : 8affbecb98c67dc0 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [12] ╭ Name      : com.jcraft:jsch.agentproxy.sshagent 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.sshagent@0.0.9 
                 │      │            ╰ UID : 77f3ddb6f8158192 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [13] ╭ Name      : com.jcraft:jsch.agentproxy.svnkit-trilead-ssh2 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.svnkit-trilead-ssh2@0.0.9 
                 │      │            ╰ UID : dfc6f6319fc95cbe 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [14] ╭ Name      : com.jcraft:jsch.agentproxy.usocket-jna 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.usocket-jna@0.0.9 
                 │      │            ╰ UID : 80b49070dfd3f3a7 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [15] ╭ Name      : com.jcraft:jsch.agentproxy.usocket-nc 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.jcraft/jsch.agentproxy.usocket-nc@0.0.9 
                 │      │            ╰ UID : 8ce583c9bcf3a507 
                 │      ├ Version   : 0.0.9 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [16] ╭ Name      : com.sun.activation:javax.activation 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.sun.activation/javax.activation@1.2.0 
                 │      │            ╰ UID : 885b1754dac6edf 
                 │      ├ Version   : 1.2.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [17] ╭ Name      : com.sun.mail:javax.mail 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.sun.mail/javax.mail@1.6.2 
                 │      │            ╰ UID : eb67ca13361cdf7e 
                 │      ├ Version   : 1.6.2 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [18] ╭ Name      : com.warrenstrange:googleauth 
                 │      ├ Identifier ╭ PURL: pkg:maven/com.warrenstrange/googleauth@1.5.0 
                 │      │            ╰ UID : abdfc1ca334283c7 
                 │      ├ Version   : 1.5.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [19] ╭ Name      : commons-cli:commons-cli 
                 │      ├ Identifier ╭ PURL: pkg:maven/commons-cli/commons-cli@1.11.0 
                 │      │            ╰ UID : 7c850f7741b728f1 
                 │      ├ Version   : 1.11.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [20] ╭ Name      : commons-codec:commons-codec 
                 │      ├ Identifier ╭ PURL: pkg:maven/commons-codec/commons-codec@1.20.0 
                 │      │            ╰ UID : 36f72796c80a5f04 
                 │      ├ Version   : 1.20.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [21] ╭ Name      : commons-io:commons-io 
                 │      ├ Identifier ╭ PURL: pkg:maven/commons-io/commons-io@2.21.0 
                 │      │            ╰ UID : 4812ba05106027a5 
                 │      ├ Version   : 2.21.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [22] ╭ Name      : commons-logging:commons-logging 
                 │      ├ Identifier ╭ PURL: pkg:maven/commons-logging/commons-logging@1.3.5 
                 │      │            ╰ UID : 78410c5141b86fa 
                 │      ├ Version   : 1.3.5 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [23] ╭ Name      : commons-net:commons-net 
                 │      ├ Identifier ╭ PURL: pkg:maven/commons-net/commons-net@3.12.0 
                 │      │            ╰ UID : 1dfaef0fb0ac5d0b 
                 │      ├ Version   : 3.12.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [24] ╭ Name      : de.vandermeer:asciilist-j7 
                 │      ├ Identifier ╭ PURL: pkg:maven/de.vandermeer/asciilist-j7@1.0.0 
                 │      │            ╰ UID : d4e586b2e07acda4 
                 │      ├ Version   : 1.0.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [25] ╭ Name      : de.vandermeer:asciitable-j7 
                 │      ├ Identifier ╭ PURL: pkg:maven/de.vandermeer/asciitable-j7@1.0.1 
                 │      │            ╰ UID : 272a590ba643367f 
                 │      ├ Version   : 1.0.1 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [26] ╭ Name      : dnsjava:dnsjava 
                 │      ├ Identifier ╭ PURL: pkg:maven/dnsjava/dnsjava@3.6.3 
                 │      │            ╰ UID : 4b5e6e63b1733dfa 
                 │      ├ Version   : 3.6.3 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [27] ╭ Name      : io.jsonwebtoken:jjwt-api 
                 │      ├ Identifier ╭ PURL: pkg:maven/io.jsonwebtoken/jjwt-api@0.13.0 
                 │      │            ╰ UID : cdc3bc0a8b47e911 
                 │      ├ Version   : 0.13.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [28] ╭ Name      : io.jsonwebtoken:jjwt-gson 
                 │      ├ Identifier ╭ PURL: pkg:maven/io.jsonwebtoken/jjwt-gson@0.13.0 
                 │      │            ╰ UID : 9fc30d362e446fcd 
                 │      ├ Version   : 0.13.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [29] ╭ Name      : io.jsonwebtoken:jjwt-impl 
                 │      ├ Identifier ╭ PURL: pkg:maven/io.jsonwebtoken/jjwt-impl@0.13.0 
                 │      │            ╰ UID : d42e28c78bfe4cd6 
                 │      ├ Version   : 0.13.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [30] ╭ Name      : io.sigpipe:jbsdiff 
                 │      ├ Identifier ╭ PURL: pkg:maven/io.sigpipe/jbsdiff@1.0 
                 │      │            ╰ UID : 3ad9c9a90222e030 
                 │      ├ Version   : 1.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [31] ╭ Name      : jakarta.activation:jakarta.activation-api 
                 │      ├ Identifier ╭ PURL: pkg:maven/jakarta.activation/jakarta.activation-api@1.2.2 
                 │      │            ╰ UID : 84baa18824622446 
                 │      ├ Version   : 1.2.2 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [32] ╭ Name      : javax.xml.bind:jaxb-api 
                 │      ├ Identifier ╭ PURL: pkg:maven/javax.xml.bind/jaxb-api@2.3.1 
                 │      │            ╰ UID : 68f09018f4453b95 
                 │      ├ Version   : 2.3.1 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [33] ╭ Name      : jline:jline 
                 │      ├ Identifier ╭ PURL: pkg:maven/jline/jline@2.14.6 
                 │      │            ╰ UID : 6930774a112e73bc 
                 │      ├ Version   : 2.14.6 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [34] ╭ Name      : org.apache.commons:commons-collections4 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.apache.commons/commons-collections4@4.5.0 
                 │      │            ╰ UID : b6f26728bc972346 
                 │      ├ Version   : 4.5.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [35] ╭ Name      : org.apache.commons:commons-compress 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.apache.commons/commons-compress@1.28.0 
                 │      │            ╰ UID : 645d61b3c78fd14e 
                 │      ├ Version   : 1.28.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [36] ╭ Name      : org.apache.commons:commons-csv 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.apache.commons/commons-csv@1.14.1 
                 │      │            ╰ UID : fd28379ee7ee9be4 
                 │      ├ Version   : 1.14.1 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [37] ╭ Name      : org.apache.commons:commons-email 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.apache.commons/commons-email@1.6.0 
                 │      │            ╰ UID : 1cdb7e2822178209 
                 │      ├ Version   : 1.6.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [38] ╭ Name      : org.apache.commons:commons-lang3 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.apache.commons/commons-lang3@3.20.0 
                 │      │            ╰ UID : 2e779afc3ea0251d 
                 │      ├ Version   : 3.20.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [39] ╭ Name      : org.apache.commons:commons-math3 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.apache.commons/commons-math3@3.6.1 
                 │      │            ╰ UID : 3992f1c5b6195e89 
                 │      ├ Version   : 3.6.1 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [40] ╭ Name      : org.eclipse.jetty.compression:jetty-compression-common 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty.compression/jetty-compression-common@1
                 │      │            │       2.1.5 
                 │      │            ╰ UID : d53e331f6a4de8ef 
                 │      ├ Version   : 12.1.5 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [41] ╭ Name      : org.eclipse.jetty.websocket:jetty-websocket-core-client 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty.websocket/jetty-websocket-core-client@
                 │      │            │       12.1.5 
                 │      │            ╰ UID : 7f48c08d79907813 
                 │      ├ Version   : 12.1.5 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [42] ╭ Name      : org.eclipse.jetty.websocket:jetty-websocket-core-common 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty.websocket/jetty-websocket-core-common@
                 │      │            │       12.1.5 
                 │      │            ╰ UID : 445a6d49434632dc 
                 │      ├ Version   : 12.1.5 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [43] ╭ Name      : org.eclipse.jetty.websocket:jetty-websocket-jetty-api 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty.websocket/jetty-websocket-jetty-api@12
                 │      │            │       .1.5 
                 │      │            ╰ UID : 2e708493e974b081 
                 │      ├ Version   : 12.1.5 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [44] ╭ Name      : org.eclipse.jetty.websocket:jetty-websocket-jetty-client 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty.websocket/jetty-websocket-jetty-client
                 │      │            │       @12.1.5 
                 │      │            ╰ UID : a4a8588127d3eff3 
                 │      ├ Version   : 12.1.5 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [45] ╭ Name      : org.eclipse.jetty.websocket:jetty-websocket-jetty-common 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty.websocket/jetty-websocket-jetty-common
                 │      │            │       @12.1.5 
                 │      │            ╰ UID : dbb38700df63b71a 
                 │      ├ Version   : 12.1.5 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [46] ╭ Name      : org.eclipse.jetty:jetty-client 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty/jetty-client@12.1.3 
                 │      │            ╰ UID : 6f2abd14ed552ef5 
                 │      ├ Version   : 12.1.3 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [47] ╭ Name      : org.eclipse.jetty:jetty-http 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty/jetty-http@12.1.4 
                 │      │            ╰ UID : 2714f45b932050d8 
                 │      ├ Version   : 12.1.4 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [48] ╭ Name      : org.eclipse.jetty:jetty-io 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty/jetty-io@12.1.5 
                 │      │            ╰ UID : 5f17a12c3044db69 
                 │      ├ Version   : 12.1.5 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [49] ╭ Name      : org.eclipse.jetty:jetty-util 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.eclipse.jetty/jetty-util@12.1.5 
                 │      │            ╰ UID : ef57f7f7d56c669b 
                 │      ├ Version   : 12.1.5 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [50] ╭ Name      : org.fusesource.hawtjni:hawtjni-runtime 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.hawtjni/hawtjni-runtime@1.17 
                 │      │            ╰ UID : 368c86360d5d2d6e 
                 │      ├ Version   : 1.17 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [51] ╭ Name      : org.fusesource.jansi:jansi 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi@1.18 
                 │      │            ╰ UID : 28003612621d63f7 
                 │      ├ Version   : 1.18 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [52] ╭ Name      : org.fusesource.jansi:jansi-freebsd32 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-freebsd32@1.8 
                 │      │            ╰ UID : 75689643540ac0cc 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [53] ╭ Name      : org.fusesource.jansi:jansi-freebsd64 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-freebsd64@1.8 
                 │      │            ╰ UID : cdf9cdca8706e16f 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [54] ╭ Name      : org.fusesource.jansi:jansi-linux32 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-linux32@1.8 
                 │      │            ╰ UID : 3d49c0eb4793e1f4 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [55] ╭ Name      : org.fusesource.jansi:jansi-linux64 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-linux64@1.8 
                 │      │            ╰ UID : 8b11f3d47b9658b2 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [56] ╭ Name      : org.fusesource.jansi:jansi-native 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-native@1.8 
                 │      │            ╰ UID : c89c538fba388aa2 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [57] ╭ Name      : org.fusesource.jansi:jansi-osx 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-osx@1.8 
                 │      │            ╰ UID : b0bc0de50b8059ad 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [58] ╭ Name      : org.fusesource.jansi:jansi-windows32 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-windows32@1.8 
                 │      │            ╰ UID : 7c1a51c801be878e 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [59] ╭ Name      : org.fusesource.jansi:jansi-windows64 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.fusesource.jansi/jansi-windows64@1.8 
                 │      │            ╰ UID : 6c10b179e44aabcb 
                 │      ├ Version   : 1.8 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [60] ╭ Name      : org.semver4j:semver4j 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.semver4j/semver4j@6.0.0 
                 │      │            ╰ UID : b4987f502c5eba1f 
                 │      ├ Version   : 6.0.0 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [61] ╭ Name      : org.slf4j:slf4j-api 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.slf4j/slf4j-api@2.0.17 
                 │      │            ╰ UID : 669ca5d81bb821ff 
                 │      ├ Version   : 2.0.17 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [62] ╭ Name      : org.slf4j:slf4j-nop 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.slf4j/slf4j-nop@2.0.17 
                 │      │            ╰ UID : 5e42b1280e39632b 
                 │      ├ Version   : 2.0.17 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ├ [63] ╭ Name      : org.snmp4j:snmp4j 
                 │      ├ Identifier ╭ PURL: pkg:maven/org.snmp4j/snmp4j@3.9.6 
                 │      │            ╰ UID : 9cf3d6b9898ef004 
                 │      ├ Version   : 3.9.6 
                 │      ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                 │      │            │         346f872 
                 │      │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                 │      │                      b969984 
                 │      ╰ FilePath  : openaf/openaf.jar 
                 ╰ [64] ╭ Name      : org.snmp4j:snmp4j-agent 
                        ├ Identifier ╭ PURL: pkg:maven/org.snmp4j/snmp4j-agent@3.8.3 
                        │            ╰ UID : c2172330bf41add 
                        ├ Version   : 3.8.3 
                        ├ Layer      ╭ Digest: sha256:bcd8674e48afe69947158bf5c00fe3a9353f76d24c4598774359dffbb
                        │            │         346f872 
                        │            ╰ DiffID: sha256:48cf1b854a9082ff2f4c628ea73f3bdbc99983e769cf1859189836c60
                        │                      b969984 
                        ╰ FilePath  : openaf/openaf.jar 
````
