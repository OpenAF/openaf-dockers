```yaml
╭ [0] ╭ Target         : openaf/ojobrt:latest (alpine 3.24.4) 
│     ├ Class          : os-pkgs 
│     ├ Type           : alpine 
│     ├ Packages        
│     ╰ Vulnerabilities ╭ [0]  ╭ VulnerabilityID : CVE-2026-107496 
│                       │      ├ PkgID           : libcrypto3@3.5.9-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.9-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.4 
│                       │      │                  ╰ UID : 3de134b31d66634f 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-107496 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:6c7131e5126518bed68b4ce5411cd838de8cd35cb07ffc60be6e6
│                       │      │                   2983ca22e59 
│                       │      ├ Title           : openssl: openssl: Denial of Service via crafted EC
│                       │      │                   certificate in CMS encryption 
│                       │      ├ Description     : Issue summary: Encrypting a CMS message to an EC certificate
│                       │      │                    whose group order
│                       │      │                   is 1 may cause CMS_encrypt() or CMS_encrypt_ex() to loop
│                       │      │                   indefinitely.
│                       │      │                   
│                       │      │                   Impact summary: An attacker able to supply the recipient
│                       │      │                   certificate to an
│                       │      │                   application performing CMS encryption can cause that
│                       │      │                   application to loop
│                       │      │                   indefinitely, consuming CPU and resulting in Denial of
│                       │      │                   Service.
│                       │      │                   CWE: CWE-835: Loop with Unreachable Exit Condition
│                       │      │                   ('Infinite Loop')
│                       │      │                   Description: CMS_encrypt() and CMS_encrypt_ex() encrypt a
│                       │      │                   message to one or
│                       │      │                   more recipient certificates and, for an EC recipient,
│                       │      │                   generate an ephemeral
│                       │      │                   key in the recipient's group. If the certificate declares a
│                       │      │                   group order of 1,
│                       │      │                   random scalar generation can only produce zero. The key
│                       │      │                   generation routine
│                       │      │                   then retries without limit while waiting for a nonzero
│                       │      │                   private scalar, so the
│                       │      │                   call never returns.
│                       │      │                   The OpenSSL TLS and QUIC implementations do not use this
│                       │      │                   path. An application
│                       │      │                   is exposed only if it calls CMS_encrypt() or
│                       │      │                   CMS_encrypt_ex() with a recipient
│                       │      │                   certificate whose EC parameters are attacker-controlled.
│                       │      │                   Certificates with
│                       │      │                   normal EC group orders do not trigger the loop.
│                       │      │                   OpenSSL 4.0 and later reject unknown explicit EC groups in
│                       │      │                   default builds.
│                       │      │                   These versions are affected only when configured with the
│                       │      │                   enable-ec_explicit_curves option.
│                       │      │                   The result is a hang that consumes a CPU core until the
│                       │      │                   process is
│                       │      │                   interrupted, a Denial of Service. The severity is Low
│                       │      │                   because the attacker
│                       │      │                   must supply the recipient certificate and the application
│                       │      │                   must choose to
│                       │      │                   encrypt to it; ordinary CMS encryption to trusted recipients
│                       │      │                    is unaffected.
│                       │      │                   The fix makes EC key generation fail when the group has no
│                       │      │                   valid nonzero
│                       │      │                   private scalar, instead of retrying indefinitely.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules in 4.1, 4.0, 3.5 and 3.0 are not affected.
│                       │      │                   The FIPS provider
│                       │      │                   does not support arbitrary explicit EC domain parameters, so
│                       │      │                    an order-1 group
│                       │      │                   is rejected during key import before the vulnerable key
│                       │      │                   generation path is
│                       │      │                   reached. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-835
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-107496       
│                       │      │                  https://github.com/openssl/openssl/commit/36e15b618decdff1b11
│                       │      │                  6eead6747718e6e729ad2                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a0051cfe699bf5a047b
│                       │      │                  c1c4faef65f80f7987366                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a8531368ddb1f86d2a2
│                       │      │                  782a8b693926bb67b59e7                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-107496             
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-107496             
│                       │      ├ PublishedDate   : 2026-11-10T19:18:02.583Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T19:17:24.6Z 
│                       ├ [1]  ╭ VulnerabilityID : CVE-2026-95691 
│                       │      ├ PkgID           : libcrypto3@3.5.9-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.9-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.4 
│                       │      │                  ╰ UID : 3de134b31d66634f 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-95691 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:f8d736043371604d07cc994f2d737c1a27398235f6eb164faf462
│                       │      │                   1ef22ac9a57 
│                       │      ├ Title           : openssl: openssl: Denial of Service via overlapping QUIC
│                       │      │                   CRYPTO frame processing 
│                       │      ├ Description     : Issue summary: A retransmitted QUIC CRYPTO frame can release
│                       │      │                    packet storage
│                       │      │                   while the TLS record layer retains a direct pointer into
│                       │      │                   that storage causing
│                       │      │                   use after free.
│                       │      │                   
│                       │      │                   Impact summary: A malicious QUIC server can cause a
│                       │      │                   heap-use-after-free read
│                       │      │                   in the OpenSSL QUIC client. The server can also identify one
│                       │      │                    allocator-adjacent
│                       │      │                   byte through the client's protected Handshake response.
│                       │      │                   CWE: CWE-416: Use After Free
│                       │      │                   Description: During CRYPTO stream processing, a pointer into
│                       │      │                    the first frame's
│                       │      │                   memory on the stream is lent to the TLS handshake
│                       │      │                   processing. The memory
│                       │      │                   must remain stable until it is processed and released.
│                       │      │                   However the processing
│                       │      │                   of retransmitted CRYPTO frames could release the memory if
│                       │      │                   the retransmitted
│                       │      │                   frame fully overlapped the existing frame. This then causes
│                       │      │                   use-after-free read
│                       │      │                   when the TLS handshake processing continues.
│                       │      │                   The use-after-free read can lead to a Denial-of-Service of
│                       │      │                   the client
│                       │      │                   application or a minor leak of information about the heap
│                       │      │                   memory contents
│                       │      │                   that might be overwritten with other data, subsequently
│                       │      │                   allocated by
│                       │      │                   the application, to the peer.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS module is not affected as the QUIC implementation
│                       │      │                   is outside of
│                       │      │                   the OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-416
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.4 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-95691        
│                       │      │                  https://github.com/openssl/openssl/commit/dd90ceb99a3c2ddba33
│                       │      │                  6bb4a00be9ebabd84c2a1                                        
│                       │      │                  https://github.com/openssl/openssl/commit/ec9d4de9d03989b29db
│                       │      │                  5a3d7efdb4c285deaf386                                        
│                       │      │                  https://github.com/openssl/openssl/commit/f6244675833e097c242
│                       │      │                  9a40d1b206d95385bd42f                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-95691              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-95691              
│                       │      ├ PublishedDate   : 2026-11-10T19:21:39.377Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T20:19:19.43Z 
│                       ├ [2]  ╭ VulnerabilityID : CVE-2026-95692 
│                       │      ├ PkgID           : libcrypto3@3.5.9-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.9-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.4 
│                       │      │                  ╰ UID : 3de134b31d66634f 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-95692 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:73383452f6e1a1edb6f0c2f2c360c3a5f3f25c476319b985b3a9b
│                       │      │                   cd1211d4657 
│                       │      ├ Title           : openssl: OpenSSL: Denial of Service via out-of-bounds read
│                       │      │                   in AES-GCM-SIV 
│                       │      ├ Description     : Issue summary: Setting an AES-GCM-SIV IV shorter than the
│                       │      │                   expected nonce
│                       │      │                   length via EVP_CipherInit_ex() may trigger a heap
│                       │      │                   out-of-bounds read.
│                       │      │                   Supplying a longer IV is silently truncated instead of
│                       │      │                   rejected.
│                       │      │                   
│                       │      │                   Impact summary: An application passing a caller-supplied IV
│                       │      │                   of the wrong
│                       │      │                   length may crash or read beyond its buffer. Because trailing
│                       │      │                    IV bytes are
│                       │      │                   ignored, an attacker who knows one message and tag may forge
│                       │      │                    messages under a
│                       │      │                   different IV.
│                       │      │                   CWE: CWE-125: Out-of-bounds Read
│                       │      │                   Description: AES-GCM-SIV copies the caller-supplied IV or
│                       │      │                   nonce into its
│                       │      │                   internal state using a copy whose length is taken from the
│                       │      │                   expected nonce size
│                       │      │                   rather than from the length the caller actually provided.
│                       │      │                   When the caller
│                       │      │                   passes a shorter IV, the copy reads past the end of the
│                       │      │                   caller's buffer;
│                       │      │                   AddressSanitizer confirms a heap out-of-bounds read reached
│                       │      │                   through
│                       │      │                   EVP_CipherInit_ex() into ossl_aes_gcm_siv_init(). When the
│                       │      │                   caller passes a
│                       │      │                   longer IV, the implementation silently discards the trailing
│                       │      │                    bytes instead of
│                       │      │                   rejecting the length.
│                       │      │                   The truncation breaks the binding between the IV and the
│                       │      │                   computed
│                       │      │                   authentication tag. An attacker who has observed a message
│                       │      │                   and its tag under
│                       │      │                   one IV can produce a message and tag that verify under a
│                       │      │                   different IV whose
│                       │      │                   first bytes match, since the surplus bytes never influence
│                       │      │                   the computation.
│                       │      │                   The message itself is unchanged, so this is a failure of IV
│                       │      │                   commitment rather
│                       │      │                   than a classic existential forgery.
│                       │      │                   Only applications that call EVP_CipherInit_ex() (or the
│                       │      │                   equivalent provider
│                       │      │                   cipher initialization) with an IV length other than the
│                       │      │                   standard 12 bytes for
│                       │      │                   AES-GCM-SIV are affected. The severity is limited because
│                       │      │                   the out-of-bounds
│                       │      │                   read is small and attacker-controlled only in length, and
│                       │      │                   the forgery requires
│                       │      │                   an unusual IV length choice by the application.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules are not affected by this issue, as
│                       │      │                   AES-GCM-SIV is not an
│                       │      │                   approved algorithm. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-95692        
│                       │      │                  https://github.com/openssl/openssl/commit/257a3427aa0ef8d9dd2
│                       │      │                  ef5b3e2d1c021a221b116                                        
│                       │      │                  https://github.com/openssl/openssl/commit/510872388f5d145cf87
│                       │      │                  0868b3d288a23822cb776                                        
│                       │      │                  https://github.com/openssl/openssl/commit/70a47ac78b6f3be1b22
│                       │      │                  fb1551bd0bfcff4f29613                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-95692              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-95692              
│                       │      ├ PublishedDate   : 2026-11-10T19:21:39.53Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T19:17:54.88Z 
│                       ├ [3]  ╭ VulnerabilityID : CVE-2026-88822 
│                       │      ├ PkgID           : libcrypto3@3.5.9-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.9-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.4 
│                       │      │                  ╰ UID : 3de134b31d66634f 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-88822 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:b06eef27854dc0ec9a6126094b0a36650adcdb83b22430d9917e7
│                       │      │                   4161541a998 
│                       │      ├ Title           : openssl: openssl: Information disclosure via uninitialized
│                       │      │                   memory in QUIC peer detection 
│                       │      ├ Description     : Issue summary: QUIC, when performing automated peer
│                       │      │                   detection, may allow
│                       │      │                   uninitialized stack data to leak into the received address
│                       │      │                   which is then used
│                       │      │                   as the destination for outgoing packets.
│                       │      │                   
│                       │      │                   Impact summary: Applications using QUIC's automated peer
│                       │      │                   detection mechanism
│                       │      │                   may receive an invalid address, leading to connection loss
│                       │      │                   and disclosure of
│                       │      │                   uninitialized stack data to an attacker observing the
│                       │      │                   outgoing network traffic.
│                       │      │                   CWE: CWE-457 (Use of Uninitialized Variable)
│                       │      │                   Description: The OpenSSL QUIC stack contains a feature in
│                       │      │                   which, when using an
│                       │      │                   already connected socket, it will auto-detect the peer
│                       │      │                   address during the SSL
│                       │      │                   handshake.  This feature uses the getpeername() function,
│                       │      │                   passing a buffer of
│                       │      │                   sufficient length to hold any supported address family, but
│                       │      │                   passes a buffer
│                       │      │                   length that is only sized such that larger addresses, such
│                       │      │                   as IPv6, cannot be
│                       │      │                   retrieved. The getpeername() function however, still returns
│                       │      │                    the full address
│                       │      │                   length, which is accepted as the valid input buffer length,
│                       │      │                   leading to the
│                       │      │                   address buffer containing uninitialized stack data instead
│                       │      │                   of the actual peer
│                       │      │                   address. The invalid peer address is then used as
│                       │      │                   destination for the outgoing
│                       │      │                   packets which leads to a connectivity breakage and a leakage
│                       │      │                    of the
│                       │      │                   uninitialized stack data to passive network observers.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules in 4.0, 3.6, 3.5, 3.4, and 3.0 are not
│                       │      │                   affected by this CVE as
│                       │      │                   the affected protocol is not implemented in the FIPS
│                       │      │                   module. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-457
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-88822        
│                       │      │                  https://github.com/openssl/openssl/commit/1a73dc590cbad62d6f0
│                       │      │                  329ea4779eadaa8d8fd75                                        
│                       │      │                  https://github.com/openssl/openssl/commit/7b4f5344aa0401e7b77
│                       │      │                  7640050b5257ed2a70e88                                        
│                       │      │                  https://github.com/openssl/openssl/commit/911eee8eb7550b95a20
│                       │      │                  6f1ad8cbdb986098982f3                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-88822              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-88822              
│                       │      ├ PublishedDate   : 2026-11-10T19:21:34.623Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T20:19:17.693Z 
│                       ├ [4]  ╭ VulnerabilityID : CVE-2026-88823 
│                       │      ├ PkgID           : libcrypto3@3.5.9-r0 
│                       │      ├ PkgName         : libcrypto3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libcrypto3@3.5.9-r0?arch=x86_64&distro
│                       │      │                  │       =3.24.4 
│                       │      │                  ╰ UID : 3de134b31d66634f 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-88823 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:434729d4ca8b90e146a348bdbf001d1141280b8a4f71f85661272
│                       │      │                   3b95b24dc76 
│                       │      ├ Title           : openssl: OpenSSL: Message authentication bypass via
│                       │      │                   zero-length AAD update 
│                       │      ├ Description     : Issue summary: The AES-GCM-SIV implementation treats a
│                       │      │                   zero-length Additional
│                       │      │                   Authenticated Data (AAD) update as a reset of all the AAD
│                       │      │                   supplied so far,
│                       │      │                   instead of leaving the AAD unchanged. An application that
│                       │      │                   supplies its AAD in
│                       │      │                   several fragments, one of which is empty, therefore produces
│                       │      │                    or verifies
│                       │      │                   messages whose authentication tag does not cover the AAD
│                       │      │                   supplied before
│                       │      │                   the empty fragment.
│                       │      │                   
│                       │      │                   Impact summary: Data an application intended to authenticate
│                       │      │                    alongside a
│                       │      │                   message is silently left unauthenticated. An attacker can
│                       │      │                   forge the AAD of such
│                       │      │                   a message.
│                       │      │                   CWE: CWE-325: Missing Cryptographic Step
│                       │      │                   Description: An application passing AAD in multiple chunks
│                       │      │                   of which some have
│                       │      │                   zero length will have the previous AAD chunks effectively
│                       │      │                   unauthenticated. Also,
│                       │      │                   on context re-initialisation, the AAD was not reset, which
│                       │      │                   meant that any AAD
│                       │      │                   accumulated from the previous context usage were also
│                       │      │                   included in the AAD of the
│                       │      │                   new message.
│                       │      │                   The fix makes a zero-length AAD update a no-op and clears
│                       │      │                   any accumulated AAD
│                       │      │                   whenever the context is re-initialised with a key or a
│                       │      │                   nonce.
│                       │      │                   A re-initialisation that only changes parameters keeps the
│                       │      │                   AAD.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules are not affected, as AES-GCM-SIV is not a
│                       │      │                   FIPS approved
│                       │      │                   algorithm and is implemented only in the default provider,
│                       │      │                   outside the
│                       │      │                   OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-325
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-88823        
│                       │      │                  https://github.com/openssl/openssl/commit/159e1de0c448d7b9f09
│                       │      │                  ad768c8e141def4aa1eb4                                        
│                       │      │                  https://github.com/openssl/openssl/commit/2f5fc833ff9b5bfe00b
│                       │      │                  32f8b5c74f73c5773c682                                        
│                       │      │                  https://github.com/openssl/openssl/commit/6747b1a278816dd7db4
│                       │      │                  6438040a70b0b5e5e0a90                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-88823              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-88823              
│                       │      ├ PublishedDate   : 2026-11-10T19:21:34.847Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T20:19:17.89Z 
│                       ├ [5]  ╭ VulnerabilityID : CVE-2026-107496 
│                       │      ├ PkgID           : libssl3@3.5.9-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.9-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.4 
│                       │      │                  ╰ UID : c5a60e84169f3215 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-107496 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:a2a2ea9eb838d15a040078785faeacf2ae505c1dff0a14084cc0d
│                       │      │                   4e457c7bf53 
│                       │      ├ Title           : openssl: openssl: Denial of Service via crafted EC
│                       │      │                   certificate in CMS encryption 
│                       │      ├ Description     : Issue summary: Encrypting a CMS message to an EC certificate
│                       │      │                    whose group order
│                       │      │                   is 1 may cause CMS_encrypt() or CMS_encrypt_ex() to loop
│                       │      │                   indefinitely.
│                       │      │                   
│                       │      │                   Impact summary: An attacker able to supply the recipient
│                       │      │                   certificate to an
│                       │      │                   application performing CMS encryption can cause that
│                       │      │                   application to loop
│                       │      │                   indefinitely, consuming CPU and resulting in Denial of
│                       │      │                   Service.
│                       │      │                   CWE: CWE-835: Loop with Unreachable Exit Condition
│                       │      │                   ('Infinite Loop')
│                       │      │                   Description: CMS_encrypt() and CMS_encrypt_ex() encrypt a
│                       │      │                   message to one or
│                       │      │                   more recipient certificates and, for an EC recipient,
│                       │      │                   generate an ephemeral
│                       │      │                   key in the recipient's group. If the certificate declares a
│                       │      │                   group order of 1,
│                       │      │                   random scalar generation can only produce zero. The key
│                       │      │                   generation routine
│                       │      │                   then retries without limit while waiting for a nonzero
│                       │      │                   private scalar, so the
│                       │      │                   call never returns.
│                       │      │                   The OpenSSL TLS and QUIC implementations do not use this
│                       │      │                   path. An application
│                       │      │                   is exposed only if it calls CMS_encrypt() or
│                       │      │                   CMS_encrypt_ex() with a recipient
│                       │      │                   certificate whose EC parameters are attacker-controlled.
│                       │      │                   Certificates with
│                       │      │                   normal EC group orders do not trigger the loop.
│                       │      │                   OpenSSL 4.0 and later reject unknown explicit EC groups in
│                       │      │                   default builds.
│                       │      │                   These versions are affected only when configured with the
│                       │      │                   enable-ec_explicit_curves option.
│                       │      │                   The result is a hang that consumes a CPU core until the
│                       │      │                   process is
│                       │      │                   interrupted, a Denial of Service. The severity is Low
│                       │      │                   because the attacker
│                       │      │                   must supply the recipient certificate and the application
│                       │      │                   must choose to
│                       │      │                   encrypt to it; ordinary CMS encryption to trusted recipients
│                       │      │                    is unaffected.
│                       │      │                   The fix makes EC key generation fail when the group has no
│                       │      │                   valid nonzero
│                       │      │                   private scalar, instead of retrying indefinitely.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules in 4.1, 4.0, 3.5 and 3.0 are not affected.
│                       │      │                   The FIPS provider
│                       │      │                   does not support arbitrary explicit EC domain parameters, so
│                       │      │                    an order-1 group
│                       │      │                   is rejected during key import before the vulnerable key
│                       │      │                   generation path is
│                       │      │                   reached. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-835
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-107496       
│                       │      │                  https://github.com/openssl/openssl/commit/36e15b618decdff1b11
│                       │      │                  6eead6747718e6e729ad2                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a0051cfe699bf5a047b
│                       │      │                  c1c4faef65f80f7987366                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a8531368ddb1f86d2a2
│                       │      │                  782a8b693926bb67b59e7                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-107496             
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-107496             
│                       │      ├ PublishedDate   : 2026-11-10T19:18:02.583Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T19:17:24.6Z 
│                       ├ [6]  ╭ VulnerabilityID : CVE-2026-95691 
│                       │      ├ PkgID           : libssl3@3.5.9-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.9-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.4 
│                       │      │                  ╰ UID : c5a60e84169f3215 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-95691 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:971ccc1b56e2cfb8507fcc827efe7dd508743ffbdbfd6944da024
│                       │      │                   1b7888f89cc 
│                       │      ├ Title           : openssl: openssl: Denial of Service via overlapping QUIC
│                       │      │                   CRYPTO frame processing 
│                       │      ├ Description     : Issue summary: A retransmitted QUIC CRYPTO frame can release
│                       │      │                    packet storage
│                       │      │                   while the TLS record layer retains a direct pointer into
│                       │      │                   that storage causing
│                       │      │                   use after free.
│                       │      │                   
│                       │      │                   Impact summary: A malicious QUIC server can cause a
│                       │      │                   heap-use-after-free read
│                       │      │                   in the OpenSSL QUIC client. The server can also identify one
│                       │      │                    allocator-adjacent
│                       │      │                   byte through the client's protected Handshake response.
│                       │      │                   CWE: CWE-416: Use After Free
│                       │      │                   Description: During CRYPTO stream processing, a pointer into
│                       │      │                    the first frame's
│                       │      │                   memory on the stream is lent to the TLS handshake
│                       │      │                   processing. The memory
│                       │      │                   must remain stable until it is processed and released.
│                       │      │                   However the processing
│                       │      │                   of retransmitted CRYPTO frames could release the memory if
│                       │      │                   the retransmitted
│                       │      │                   frame fully overlapped the existing frame. This then causes
│                       │      │                   use-after-free read
│                       │      │                   when the TLS handshake processing continues.
│                       │      │                   The use-after-free read can lead to a Denial-of-Service of
│                       │      │                   the client
│                       │      │                   application or a minor leak of information about the heap
│                       │      │                   memory contents
│                       │      │                   that might be overwritten with other data, subsequently
│                       │      │                   allocated by
│                       │      │                   the application, to the peer.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS module is not affected as the QUIC implementation
│                       │      │                   is outside of
│                       │      │                   the OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-416
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.4 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-95691        
│                       │      │                  https://github.com/openssl/openssl/commit/dd90ceb99a3c2ddba33
│                       │      │                  6bb4a00be9ebabd84c2a1                                        
│                       │      │                  https://github.com/openssl/openssl/commit/ec9d4de9d03989b29db
│                       │      │                  5a3d7efdb4c285deaf386                                        
│                       │      │                  https://github.com/openssl/openssl/commit/f6244675833e097c242
│                       │      │                  9a40d1b206d95385bd42f                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-95691              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-95691              
│                       │      ├ PublishedDate   : 2026-11-10T19:21:39.377Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T20:19:19.43Z 
│                       ├ [7]  ╭ VulnerabilityID : CVE-2026-95692 
│                       │      ├ PkgID           : libssl3@3.5.9-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.9-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.4 
│                       │      │                  ╰ UID : c5a60e84169f3215 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-95692 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:da3838754085e95e04fbfe696b26094d4ae855b5a41be5480d490
│                       │      │                   45af1ae38af 
│                       │      ├ Title           : openssl: OpenSSL: Denial of Service via out-of-bounds read
│                       │      │                   in AES-GCM-SIV 
│                       │      ├ Description     : Issue summary: Setting an AES-GCM-SIV IV shorter than the
│                       │      │                   expected nonce
│                       │      │                   length via EVP_CipherInit_ex() may trigger a heap
│                       │      │                   out-of-bounds read.
│                       │      │                   Supplying a longer IV is silently truncated instead of
│                       │      │                   rejected.
│                       │      │                   
│                       │      │                   Impact summary: An application passing a caller-supplied IV
│                       │      │                   of the wrong
│                       │      │                   length may crash or read beyond its buffer. Because trailing
│                       │      │                    IV bytes are
│                       │      │                   ignored, an attacker who knows one message and tag may forge
│                       │      │                    messages under a
│                       │      │                   different IV.
│                       │      │                   CWE: CWE-125: Out-of-bounds Read
│                       │      │                   Description: AES-GCM-SIV copies the caller-supplied IV or
│                       │      │                   nonce into its
│                       │      │                   internal state using a copy whose length is taken from the
│                       │      │                   expected nonce size
│                       │      │                   rather than from the length the caller actually provided.
│                       │      │                   When the caller
│                       │      │                   passes a shorter IV, the copy reads past the end of the
│                       │      │                   caller's buffer;
│                       │      │                   AddressSanitizer confirms a heap out-of-bounds read reached
│                       │      │                   through
│                       │      │                   EVP_CipherInit_ex() into ossl_aes_gcm_siv_init(). When the
│                       │      │                   caller passes a
│                       │      │                   longer IV, the implementation silently discards the trailing
│                       │      │                    bytes instead of
│                       │      │                   rejecting the length.
│                       │      │                   The truncation breaks the binding between the IV and the
│                       │      │                   computed
│                       │      │                   authentication tag. An attacker who has observed a message
│                       │      │                   and its tag under
│                       │      │                   one IV can produce a message and tag that verify under a
│                       │      │                   different IV whose
│                       │      │                   first bytes match, since the surplus bytes never influence
│                       │      │                   the computation.
│                       │      │                   The message itself is unchanged, so this is a failure of IV
│                       │      │                   commitment rather
│                       │      │                   than a classic existential forgery.
│                       │      │                   Only applications that call EVP_CipherInit_ex() (or the
│                       │      │                   equivalent provider
│                       │      │                   cipher initialization) with an IV length other than the
│                       │      │                   standard 12 bytes for
│                       │      │                   AES-GCM-SIV are affected. The severity is limited because
│                       │      │                   the out-of-bounds
│                       │      │                   read is small and attacker-controlled only in length, and
│                       │      │                   the forgery requires
│                       │      │                   an unusual IV length choice by the application.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules are not affected by this issue, as
│                       │      │                   AES-GCM-SIV is not an
│                       │      │                   approved algorithm. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-95692        
│                       │      │                  https://github.com/openssl/openssl/commit/257a3427aa0ef8d9dd2
│                       │      │                  ef5b3e2d1c021a221b116                                        
│                       │      │                  https://github.com/openssl/openssl/commit/510872388f5d145cf87
│                       │      │                  0868b3d288a23822cb776                                        
│                       │      │                  https://github.com/openssl/openssl/commit/70a47ac78b6f3be1b22
│                       │      │                  fb1551bd0bfcff4f29613                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-95692              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-95692              
│                       │      ├ PublishedDate   : 2026-11-10T19:21:39.53Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T19:17:54.88Z 
│                       ├ [8]  ╭ VulnerabilityID : CVE-2026-88822 
│                       │      ├ PkgID           : libssl3@3.5.9-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.9-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.4 
│                       │      │                  ╰ UID : c5a60e84169f3215 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-88822 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:6da10c20168e63b45e55e91a9eebdebc07410d50b41776b8b7448
│                       │      │                   e1cebe25970 
│                       │      ├ Title           : openssl: openssl: Information disclosure via uninitialized
│                       │      │                   memory in QUIC peer detection 
│                       │      ├ Description     : Issue summary: QUIC, when performing automated peer
│                       │      │                   detection, may allow
│                       │      │                   uninitialized stack data to leak into the received address
│                       │      │                   which is then used
│                       │      │                   as the destination for outgoing packets.
│                       │      │                   
│                       │      │                   Impact summary: Applications using QUIC's automated peer
│                       │      │                   detection mechanism
│                       │      │                   may receive an invalid address, leading to connection loss
│                       │      │                   and disclosure of
│                       │      │                   uninitialized stack data to an attacker observing the
│                       │      │                   outgoing network traffic.
│                       │      │                   CWE: CWE-457 (Use of Uninitialized Variable)
│                       │      │                   Description: The OpenSSL QUIC stack contains a feature in
│                       │      │                   which, when using an
│                       │      │                   already connected socket, it will auto-detect the peer
│                       │      │                   address during the SSL
│                       │      │                   handshake.  This feature uses the getpeername() function,
│                       │      │                   passing a buffer of
│                       │      │                   sufficient length to hold any supported address family, but
│                       │      │                   passes a buffer
│                       │      │                   length that is only sized such that larger addresses, such
│                       │      │                   as IPv6, cannot be
│                       │      │                   retrieved. The getpeername() function however, still returns
│                       │      │                    the full address
│                       │      │                   length, which is accepted as the valid input buffer length,
│                       │      │                   leading to the
│                       │      │                   address buffer containing uninitialized stack data instead
│                       │      │                   of the actual peer
│                       │      │                   address. The invalid peer address is then used as
│                       │      │                   destination for the outgoing
│                       │      │                   packets which leads to a connectivity breakage and a leakage
│                       │      │                    of the
│                       │      │                   uninitialized stack data to passive network observers.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules in 4.0, 3.6, 3.5, 3.4, and 3.0 are not
│                       │      │                   affected by this CVE as
│                       │      │                   the affected protocol is not implemented in the FIPS
│                       │      │                   module. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-457
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-88822        
│                       │      │                  https://github.com/openssl/openssl/commit/1a73dc590cbad62d6f0
│                       │      │                  329ea4779eadaa8d8fd75                                        
│                       │      │                  https://github.com/openssl/openssl/commit/7b4f5344aa0401e7b77
│                       │      │                  7640050b5257ed2a70e88                                        
│                       │      │                  https://github.com/openssl/openssl/commit/911eee8eb7550b95a20
│                       │      │                  6f1ad8cbdb986098982f3                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-88822              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-88822              
│                       │      ├ PublishedDate   : 2026-11-10T19:21:34.623Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T20:19:17.693Z 
│                       ├ [9]  ╭ VulnerabilityID : CVE-2026-88823 
│                       │      ├ PkgID           : libssl3@3.5.9-r0 
│                       │      ├ PkgName         : libssl3 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/libssl3@3.5.9-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.4 
│                       │      │                  ╰ UID : c5a60e84169f3215 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-88823 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:16f88da2fce09116a297b811bb25942af88abe74294cf9e284a0a
│                       │      │                   e7284a0c9df 
│                       │      ├ Title           : openssl: OpenSSL: Message authentication bypass via
│                       │      │                   zero-length AAD update 
│                       │      ├ Description     : Issue summary: The AES-GCM-SIV implementation treats a
│                       │      │                   zero-length Additional
│                       │      │                   Authenticated Data (AAD) update as a reset of all the AAD
│                       │      │                   supplied so far,
│                       │      │                   instead of leaving the AAD unchanged. An application that
│                       │      │                   supplies its AAD in
│                       │      │                   several fragments, one of which is empty, therefore produces
│                       │      │                    or verifies
│                       │      │                   messages whose authentication tag does not cover the AAD
│                       │      │                   supplied before
│                       │      │                   the empty fragment.
│                       │      │                   
│                       │      │                   Impact summary: Data an application intended to authenticate
│                       │      │                    alongside a
│                       │      │                   message is silently left unauthenticated. An attacker can
│                       │      │                   forge the AAD of such
│                       │      │                   a message.
│                       │      │                   CWE: CWE-325: Missing Cryptographic Step
│                       │      │                   Description: An application passing AAD in multiple chunks
│                       │      │                   of which some have
│                       │      │                   zero length will have the previous AAD chunks effectively
│                       │      │                   unauthenticated. Also,
│                       │      │                   on context re-initialisation, the AAD was not reset, which
│                       │      │                   meant that any AAD
│                       │      │                   accumulated from the previous context usage were also
│                       │      │                   included in the AAD of the
│                       │      │                   new message.
│                       │      │                   The fix makes a zero-length AAD update a no-op and clears
│                       │      │                   any accumulated AAD
│                       │      │                   whenever the context is re-initialised with a key or a
│                       │      │                   nonce.
│                       │      │                   A re-initialisation that only changes parameters keeps the
│                       │      │                   AAD.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules are not affected, as AES-GCM-SIV is not a
│                       │      │                   FIPS approved
│                       │      │                   algorithm and is implemented only in the default provider,
│                       │      │                   outside the
│                       │      │                   OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-325
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-88823        
│                       │      │                  https://github.com/openssl/openssl/commit/159e1de0c448d7b9f09
│                       │      │                  ad768c8e141def4aa1eb4                                        
│                       │      │                  https://github.com/openssl/openssl/commit/2f5fc833ff9b5bfe00b
│                       │      │                  32f8b5c74f73c5773c682                                        
│                       │      │                  https://github.com/openssl/openssl/commit/6747b1a278816dd7db4
│                       │      │                  6438040a70b0b5e5e0a90                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-88823              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-88823              
│                       │      ├ PublishedDate   : 2026-11-10T19:21:34.847Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T20:19:17.89Z 
│                       ├ [10] ╭ VulnerabilityID : CVE-2026-107496 
│                       │      ├ PkgID           : openssl@3.5.9-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.9-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.4 
│                       │      │                  ╰ UID : 5da5422ed30cee1 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-107496 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:6efcd3c7f6e062cb8dc198d10c93db36faf12142a370c36d7fb9b
│                       │      │                   999d824758d 
│                       │      ├ Title           : openssl: openssl: Denial of Service via crafted EC
│                       │      │                   certificate in CMS encryption 
│                       │      ├ Description     : Issue summary: Encrypting a CMS message to an EC certificate
│                       │      │                    whose group order
│                       │      │                   is 1 may cause CMS_encrypt() or CMS_encrypt_ex() to loop
│                       │      │                   indefinitely.
│                       │      │                   
│                       │      │                   Impact summary: An attacker able to supply the recipient
│                       │      │                   certificate to an
│                       │      │                   application performing CMS encryption can cause that
│                       │      │                   application to loop
│                       │      │                   indefinitely, consuming CPU and resulting in Denial of
│                       │      │                   Service.
│                       │      │                   CWE: CWE-835: Loop with Unreachable Exit Condition
│                       │      │                   ('Infinite Loop')
│                       │      │                   Description: CMS_encrypt() and CMS_encrypt_ex() encrypt a
│                       │      │                   message to one or
│                       │      │                   more recipient certificates and, for an EC recipient,
│                       │      │                   generate an ephemeral
│                       │      │                   key in the recipient's group. If the certificate declares a
│                       │      │                   group order of 1,
│                       │      │                   random scalar generation can only produce zero. The key
│                       │      │                   generation routine
│                       │      │                   then retries without limit while waiting for a nonzero
│                       │      │                   private scalar, so the
│                       │      │                   call never returns.
│                       │      │                   The OpenSSL TLS and QUIC implementations do not use this
│                       │      │                   path. An application
│                       │      │                   is exposed only if it calls CMS_encrypt() or
│                       │      │                   CMS_encrypt_ex() with a recipient
│                       │      │                   certificate whose EC parameters are attacker-controlled.
│                       │      │                   Certificates with
│                       │      │                   normal EC group orders do not trigger the loop.
│                       │      │                   OpenSSL 4.0 and later reject unknown explicit EC groups in
│                       │      │                   default builds.
│                       │      │                   These versions are affected only when configured with the
│                       │      │                   enable-ec_explicit_curves option.
│                       │      │                   The result is a hang that consumes a CPU core until the
│                       │      │                   process is
│                       │      │                   interrupted, a Denial of Service. The severity is Low
│                       │      │                   because the attacker
│                       │      │                   must supply the recipient certificate and the application
│                       │      │                   must choose to
│                       │      │                   encrypt to it; ordinary CMS encryption to trusted recipients
│                       │      │                    is unaffected.
│                       │      │                   The fix makes EC key generation fail when the group has no
│                       │      │                   valid nonzero
│                       │      │                   private scalar, instead of retrying indefinitely.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules in 4.1, 4.0, 3.5 and 3.0 are not affected.
│                       │      │                   The FIPS provider
│                       │      │                   does not support arbitrary explicit EC domain parameters, so
│                       │      │                    an order-1 group
│                       │      │                   is rejected during key import before the vulnerable key
│                       │      │                   generation path is
│                       │      │                   reached. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-835
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N
│                       │      │                           │           /A:H 
│                       │      │                           ╰ V3Score : 5.9 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-107496       
│                       │      │                  https://github.com/openssl/openssl/commit/36e15b618decdff1b11
│                       │      │                  6eead6747718e6e729ad2                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a0051cfe699bf5a047b
│                       │      │                  c1c4faef65f80f7987366                                        
│                       │      │                  https://github.com/openssl/openssl/commit/a8531368ddb1f86d2a2
│                       │      │                  782a8b693926bb67b59e7                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-107496             
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-107496             
│                       │      ├ PublishedDate   : 2026-11-10T19:18:02.583Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T19:17:24.6Z 
│                       ├ [11] ╭ VulnerabilityID : CVE-2026-95691 
│                       │      ├ PkgID           : openssl@3.5.9-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.9-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.4 
│                       │      │                  ╰ UID : 5da5422ed30cee1 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-95691 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:e433ee069f51cfd7dbe47b9d86aec1087c14f79dbb58d2427cc52
│                       │      │                   e343a219192 
│                       │      ├ Title           : openssl: openssl: Denial of Service via overlapping QUIC
│                       │      │                   CRYPTO frame processing 
│                       │      ├ Description     : Issue summary: A retransmitted QUIC CRYPTO frame can release
│                       │      │                    packet storage
│                       │      │                   while the TLS record layer retains a direct pointer into
│                       │      │                   that storage causing
│                       │      │                   use after free.
│                       │      │                   
│                       │      │                   Impact summary: A malicious QUIC server can cause a
│                       │      │                   heap-use-after-free read
│                       │      │                   in the OpenSSL QUIC client. The server can also identify one
│                       │      │                    allocator-adjacent
│                       │      │                   byte through the client's protected Handshake response.
│                       │      │                   CWE: CWE-416: Use After Free
│                       │      │                   Description: During CRYPTO stream processing, a pointer into
│                       │      │                    the first frame's
│                       │      │                   memory on the stream is lent to the TLS handshake
│                       │      │                   processing. The memory
│                       │      │                   must remain stable until it is processed and released.
│                       │      │                   However the processing
│                       │      │                   of retransmitted CRYPTO frames could release the memory if
│                       │      │                   the retransmitted
│                       │      │                   frame fully overlapped the existing frame. This then causes
│                       │      │                   use-after-free read
│                       │      │                   when the TLS handshake processing continues.
│                       │      │                   The use-after-free read can lead to a Denial-of-Service of
│                       │      │                   the client
│                       │      │                   application or a minor leak of information about the heap
│                       │      │                   memory contents
│                       │      │                   that might be overwritten with other data, subsequently
│                       │      │                   allocated by
│                       │      │                   the application, to the peer.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS module is not affected as the QUIC implementation
│                       │      │                   is outside of
│                       │      │                   the OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-416
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 5.4 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-95691        
│                       │      │                  https://github.com/openssl/openssl/commit/dd90ceb99a3c2ddba33
│                       │      │                  6bb4a00be9ebabd84c2a1                                        
│                       │      │                  https://github.com/openssl/openssl/commit/ec9d4de9d03989b29db
│                       │      │                  5a3d7efdb4c285deaf386                                        
│                       │      │                  https://github.com/openssl/openssl/commit/f6244675833e097c242
│                       │      │                  9a40d1b206d95385bd42f                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-95691              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-95691              
│                       │      ├ PublishedDate   : 2026-11-10T19:21:39.377Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T20:19:19.43Z 
│                       ├ [12] ╭ VulnerabilityID : CVE-2026-95692 
│                       │      ├ PkgID           : openssl@3.5.9-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.9-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.4 
│                       │      │                  ╰ UID : 5da5422ed30cee1 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-95692 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:041315d36ceaa7ff039b6ba7e592a8a814c54914c754499af5a1b
│                       │      │                   8c44ae5f8f3 
│                       │      ├ Title           : openssl: OpenSSL: Denial of Service via out-of-bounds read
│                       │      │                   in AES-GCM-SIV 
│                       │      ├ Description     : Issue summary: Setting an AES-GCM-SIV IV shorter than the
│                       │      │                   expected nonce
│                       │      │                   length via EVP_CipherInit_ex() may trigger a heap
│                       │      │                   out-of-bounds read.
│                       │      │                   Supplying a longer IV is silently truncated instead of
│                       │      │                   rejected.
│                       │      │                   
│                       │      │                   Impact summary: An application passing a caller-supplied IV
│                       │      │                   of the wrong
│                       │      │                   length may crash or read beyond its buffer. Because trailing
│                       │      │                    IV bytes are
│                       │      │                   ignored, an attacker who knows one message and tag may forge
│                       │      │                    messages under a
│                       │      │                   different IV.
│                       │      │                   CWE: CWE-125: Out-of-bounds Read
│                       │      │                   Description: AES-GCM-SIV copies the caller-supplied IV or
│                       │      │                   nonce into its
│                       │      │                   internal state using a copy whose length is taken from the
│                       │      │                   expected nonce size
│                       │      │                   rather than from the length the caller actually provided.
│                       │      │                   When the caller
│                       │      │                   passes a shorter IV, the copy reads past the end of the
│                       │      │                   caller's buffer;
│                       │      │                   AddressSanitizer confirms a heap out-of-bounds read reached
│                       │      │                   through
│                       │      │                   EVP_CipherInit_ex() into ossl_aes_gcm_siv_init(). When the
│                       │      │                   caller passes a
│                       │      │                   longer IV, the implementation silently discards the trailing
│                       │      │                    bytes instead of
│                       │      │                   rejecting the length.
│                       │      │                   The truncation breaks the binding between the IV and the
│                       │      │                   computed
│                       │      │                   authentication tag. An attacker who has observed a message
│                       │      │                   and its tag under
│                       │      │                   one IV can produce a message and tag that verify under a
│                       │      │                   different IV whose
│                       │      │                   first bytes match, since the surplus bytes never influence
│                       │      │                   the computation.
│                       │      │                   The message itself is unchanged, so this is a failure of IV
│                       │      │                   commitment rather
│                       │      │                   than a classic existential forgery.
│                       │      │                   Only applications that call EVP_CipherInit_ex() (or the
│                       │      │                   equivalent provider
│                       │      │                   cipher initialization) with an IV length other than the
│                       │      │                   standard 12 bytes for
│                       │      │                   AES-GCM-SIV are affected. The severity is limited because
│                       │      │                   the out-of-bounds
│                       │      │                   read is small and attacker-controlled only in length, and
│                       │      │                   the forgery requires
│                       │      │                   an unusual IV length choice by the application.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules are not affected by this issue, as
│                       │      │                   AES-GCM-SIV is not an
│                       │      │                   approved algorithm. 
│                       │      ├ Severity        : MEDIUM 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-125
│                       │      ├ VendorSeverity   ╭ redhat: 2 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:L 
│                       │      │                           ╰ V3Score : 4.8 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-95692        
│                       │      │                  https://github.com/openssl/openssl/commit/257a3427aa0ef8d9dd2
│                       │      │                  ef5b3e2d1c021a221b116                                        
│                       │      │                  https://github.com/openssl/openssl/commit/510872388f5d145cf87
│                       │      │                  0868b3d288a23822cb776                                        
│                       │      │                  https://github.com/openssl/openssl/commit/70a47ac78b6f3be1b22
│                       │      │                  fb1551bd0bfcff4f29613                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-95692              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-95692              
│                       │      ├ PublishedDate   : 2026-11-10T19:21:39.53Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T19:17:54.88Z 
│                       ├ [13] ╭ VulnerabilityID : CVE-2026-88822 
│                       │      ├ PkgID           : openssl@3.5.9-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.9-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.4 
│                       │      │                  ╰ UID : 5da5422ed30cee1 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-88822 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:8caa61d862f8a55d1c13bb41667466793b36851784fe9ee5822fb
│                       │      │                   d1cc0096e11 
│                       │      ├ Title           : openssl: openssl: Information disclosure via uninitialized
│                       │      │                   memory in QUIC peer detection 
│                       │      ├ Description     : Issue summary: QUIC, when performing automated peer
│                       │      │                   detection, may allow
│                       │      │                   uninitialized stack data to leak into the received address
│                       │      │                   which is then used
│                       │      │                   as the destination for outgoing packets.
│                       │      │                   
│                       │      │                   Impact summary: Applications using QUIC's automated peer
│                       │      │                   detection mechanism
│                       │      │                   may receive an invalid address, leading to connection loss
│                       │      │                   and disclosure of
│                       │      │                   uninitialized stack data to an attacker observing the
│                       │      │                   outgoing network traffic.
│                       │      │                   CWE: CWE-457 (Use of Uninitialized Variable)
│                       │      │                   Description: The OpenSSL QUIC stack contains a feature in
│                       │      │                   which, when using an
│                       │      │                   already connected socket, it will auto-detect the peer
│                       │      │                   address during the SSL
│                       │      │                   handshake.  This feature uses the getpeername() function,
│                       │      │                   passing a buffer of
│                       │      │                   sufficient length to hold any supported address family, but
│                       │      │                   passes a buffer
│                       │      │                   length that is only sized such that larger addresses, such
│                       │      │                   as IPv6, cannot be
│                       │      │                   retrieved. The getpeername() function however, still returns
│                       │      │                    the full address
│                       │      │                   length, which is accepted as the valid input buffer length,
│                       │      │                   leading to the
│                       │      │                   address buffer containing uninitialized stack data instead
│                       │      │                   of the actual peer
│                       │      │                   address. The invalid peer address is then used as
│                       │      │                   destination for the outgoing
│                       │      │                   packets which leads to a connectivity breakage and a leakage
│                       │      │                    of the
│                       │      │                   uninitialized stack data to passive network observers.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules in 4.0, 3.6, 3.5, 3.4, and 3.0 are not
│                       │      │                   affected by this CVE as
│                       │      │                   the affected protocol is not implemented in the FIPS
│                       │      │                   module. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-457
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-88822        
│                       │      │                  https://github.com/openssl/openssl/commit/1a73dc590cbad62d6f0
│                       │      │                  329ea4779eadaa8d8fd75                                        
│                       │      │                  https://github.com/openssl/openssl/commit/7b4f5344aa0401e7b77
│                       │      │                  7640050b5257ed2a70e88                                        
│                       │      │                  https://github.com/openssl/openssl/commit/911eee8eb7550b95a20
│                       │      │                  6f1ad8cbdb986098982f3                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-88822              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-88822              
│                       │      ├ PublishedDate   : 2026-11-10T19:21:34.623Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T20:19:17.693Z 
│                       ├ [14] ╭ VulnerabilityID : CVE-2026-88823 
│                       │      ├ PkgID           : openssl@3.5.9-r0 
│                       │      ├ PkgName         : openssl 
│                       │      ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/openssl@3.5.9-r0?arch=x86_64&distro=3.
│                       │      │                  │       24.4 
│                       │      │                  ╰ UID : 5da5422ed30cee1 
│                       │      ├ InstalledVersion: 3.5.9-r0 
│                       │      ├ FixedVersion    : 3.5.9-r1 
│                       │      ├ Status          : fixed 
│                       │      ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                       │      │                  │         14e79699173d1fa49d21 
│                       │      │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                       │      │                            eac12f4c91ad3083627d 
│                       │      ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-88823 
│                       │      ├ DataSource       ╭ ID  : alpine 
│                       │      │                  ├ Name: Alpine Secdb 
│                       │      │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                       │      ├ Fingerprint     : sha256:d294204fee07f7b0f8dcb39bdd0d83d8c4220dc6158701999b1a0
│                       │      │                   d1374609d83 
│                       │      ├ Title           : openssl: OpenSSL: Message authentication bypass via
│                       │      │                   zero-length AAD update 
│                       │      ├ Description     : Issue summary: The AES-GCM-SIV implementation treats a
│                       │      │                   zero-length Additional
│                       │      │                   Authenticated Data (AAD) update as a reset of all the AAD
│                       │      │                   supplied so far,
│                       │      │                   instead of leaving the AAD unchanged. An application that
│                       │      │                   supplies its AAD in
│                       │      │                   several fragments, one of which is empty, therefore produces
│                       │      │                    or verifies
│                       │      │                   messages whose authentication tag does not cover the AAD
│                       │      │                   supplied before
│                       │      │                   the empty fragment.
│                       │      │                   
│                       │      │                   Impact summary: Data an application intended to authenticate
│                       │      │                    alongside a
│                       │      │                   message is silently left unauthenticated. An attacker can
│                       │      │                   forge the AAD of such
│                       │      │                   a message.
│                       │      │                   CWE: CWE-325: Missing Cryptographic Step
│                       │      │                   Description: An application passing AAD in multiple chunks
│                       │      │                   of which some have
│                       │      │                   zero length will have the previous AAD chunks effectively
│                       │      │                   unauthenticated. Also,
│                       │      │                   on context re-initialisation, the AAD was not reset, which
│                       │      │                   meant that any AAD
│                       │      │                   accumulated from the previous context usage were also
│                       │      │                   included in the AAD of the
│                       │      │                   new message.
│                       │      │                   The fix makes a zero-length AAD update a no-op and clears
│                       │      │                   any accumulated AAD
│                       │      │                   whenever the context is re-initialised with a key or a
│                       │      │                   nonce.
│                       │      │                   A re-initialisation that only changes parameters keeps the
│                       │      │                   AAD.
│                       │      │                   FIPS impact: no
│                       │      │                   The FIPS modules are not affected, as AES-GCM-SIV is not a
│                       │      │                   FIPS approved
│                       │      │                   algorithm and is implemented only in the default provider,
│                       │      │                   outside the
│                       │      │                   OpenSSL FIPS module boundary. 
│                       │      ├ Severity        : LOW 
│                       │      ├ CweIDs                  
│                       │      │                  ───────
│                       │      │                  CWE-325
│                       │      ├ VendorSeverity   ╭ redhat: 1 
│                       │      │                  ╰ ubuntu: 2 
│                       │      ├ CVSS             ─ redhat ╭ V3Vector: CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:L
│                       │      │                           │           /A:N 
│                       │      │                           ╰ V3Score : 3.7 
│                       │      ├ References                                                                    
│                       │      │                  ─────────────────────────────────────────────────────────────
│                       │      │                  https://access.redhat.com/security/cve/CVE-2026-88823        
│                       │      │                  https://github.com/openssl/openssl/commit/159e1de0c448d7b9f09
│                       │      │                  ad768c8e141def4aa1eb4                                        
│                       │      │                  https://github.com/openssl/openssl/commit/2f5fc833ff9b5bfe00b
│                       │      │                  32f8b5c74f73c5773c682                                        
│                       │      │                  https://github.com/openssl/openssl/commit/6747b1a278816dd7db4
│                       │      │                  6438040a70b0b5e5e0a90                                        
│                       │      │                  https://nvd.nist.gov/vuln/detail/CVE-2026-88823              
│                       │      │                                                                               
│                       │      │                  https://openssl-library.org/news/secadv/20261110.txt         
│                       │      │                                                                               
│                       │      │                  https://www.cve.org/CVERecord?id=CVE-2026-88823              
│                       │      ├ PublishedDate   : 2026-11-10T19:21:34.847Z 
│                       │      ╰ LastModifiedDate: 2026-11-16T20:19:17.89Z 
│                       ╰ [15] ╭ VulnerabilityID : CVE-2026-4738 
│                              ├ PkgID           : zlib@1.3.2-r1 
│                              ├ PkgName         : zlib 
│                              ├ PkgIdentifier    ╭ PURL: pkg:apk/alpine/zlib@1.3.2-r1?arch=x86_64&distro=3.24.4 
│                              │                  ╰ UID : 926381dc853769fb 
│                              ├ InstalledVersion: 1.3.2-r1 
│                              ├ FixedVersion    : 1.4-r0 
│                              ├ Status          : fixed 
│                              ├ Layer            ╭ Digest: sha256:0f3459bbf5b7373cfd5ce62bc19eba236db59070dc9b
│                              │                  │         14e79699173d1fa49d21 
│                              │                  ╰ DiffID: sha256:e9dd49b25f348bd8e13aa2844ffebbcee8d27b88536f
│                              │                            eac12f4c91ad3083627d 
│                              ├ PrimaryURL      : https://avd.aquasec.com/nvd/cve-2026-4738 
│                              ├ DataSource       ╭ ID  : alpine 
│                              │                  ├ Name: Alpine Secdb 
│                              │                  ╰ URL : https://secdb.alpinelinux.org/ 
│                              ├ Fingerprint     : sha256:ddb6ec3dd6cdff7d71b436a344b89491b585a9dd8af7fbc6e50e9
│                              │                   b072eb40a09 
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
