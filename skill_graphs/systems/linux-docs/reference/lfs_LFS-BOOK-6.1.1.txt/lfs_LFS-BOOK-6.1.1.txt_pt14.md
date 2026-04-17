   documented. The problem is that Udev will create a device node only if
   Hotplug or a user-written script inserts the corresponding module into
   the kernel, and not all modules are detectable by Hotplug. Note that
   statements like the one below in the /etc/modprobe.conf file do not
   work with Udev:
alias char-major-XXX some-module

   Because of the complications with Hotplug, Udev, and modules, we
   strongly recommend starting with a completely non-modular kernel
   configuration, especially if this is the first time using Udev.

   Install the modules, if the kernel configuration uses them:
make modules_install

   After kernel compilation is complete, additional steps are required to
   complete the installation. Some files need to be copied to the /boot
   directory.

   The path to the kernel image may vary depending on the platform being
   used. The following command assumes an x86 architecture:
cp -v arch/i386/boot/bzImage /boot/lfskernel-2.6.11.12

   System.map is a symbol file for the kernel. It maps the function entry
   points of every function in the kernel API, as well as the addresses
   of the kernel data structures for the running kernel. Issue the
   following command to install the map file:
cp -v System.map /boot/System.map-2.6.11.12

   The kernel configuration file .config produced by the make menuconfig
   step above contains all the configuration selections for the kernel
   that was just compiled. It is a good idea to keep this file for future
   reference:
cp -v .config /boot/config-2.6.11.12

   It is important to note that the files in the kernel source directory
   are not owned by root. Whenever a package is unpacked as user root
   (like we did inside chroot), the files have the user and group IDs of
   whatever they were on the packager's computer. This is usually not a
   problem for any other package to be installed because the source tree
   is removed after the installation. However, the Linux source tree is
   often retained for a long time. Because of this, there is a chance
   that whatever user ID the packager used will be assigned to somebody
   on the machine. That person would then have write access to the kernel
   source.

   If the kernel source tree is going to be retained, run chown -R 0:0 on
   the linux-2.6.11.12 directory to ensure all files are owned by user
   root.

Warning

   Some kernel documentation recommends creating a symlink from
   /usr/src/linux pointing to the kernel source directory. This is
   specific to kernels prior to the 2.6 series and must not be created on
   an LFS system as it can cause problems for packages you may wish to
   build once your base LFS system is complete.

   Also, the headers in the system's include directory should always be
   the ones against which Glibc was compiled, that is, the ones from the
   Linux-Libc-Headers package, and therefore, should never be replaced by
   the kernel headers.

8.3.2. Contents of Linux

   Installed files: config-2.6.11.12, lfskernel-2.6.11.12, and
   System.map-2.6.11.12

Short Descriptions

   config-2.6.11.12

   Contains all the configuration selections for the kernel
   lfskernel-2.6.11.12

   The engine of the Linux system. When turning on the computer, the
   kernel is the first part of the operating system that gets loaded. It
   detects and initializes all components of the computer's hardware,
   then makes these components available as a tree of files to the
   software and turns a single CPU into a multitasking machine capable of
   running scores of programs seemingly at the same time
   System.map-2.6.11.12

   A list of addresses and symbols; it maps the entry points and
   addresses of all the functions and data structures in the kernel

8.4. Making the LFS System Bootable

   Your shiny new LFS system is almost complete. One of the last things
   to do is to ensure that the system can be properly booted. The
   instructions below apply only to computers of IA-32 architecture,
   meaning mainstream PCs. Information on "boot loading" for other
   architectures should be available in the usual resource-specific
   locations for those architectures.

   Boot loading can be a complex area, so a few cautionary words are in
   order. Be familiar with the current boot loader and any other
   operating systems present on the hard drive(s) that need to be
   bootable. Make sure that an emergency boot disk is ready to "rescue"
   the computer if the computer becomes unusable (un-bootable).

   Earlier, we compiled and installed the GRUB boot loader software in
   preparation for this step. The procedure involves writing some special
   GRUB files to specific locations on the hard drive. We highly
   recommend creating a GRUB boot floppy diskette as a backup. Insert a
   blank floppy diskette and run the following commands:
dd if=/boot/grub/stage1 of=/dev/fd0 bs=512 count=1
dd if=/boot/grub/stage2 of=/dev/fd0 bs=512 seek=1

   Remove the diskette and store it somewhere safe. Now, run the grub
   shell:
grub

   GRUB uses its own naming structure for drives and partitions in the
   form of (hdn,m), where n is the hard drive number and m is the
   partition number, both starting from zero. For example, partition hda1
   is (hd0,0) to GRUB and hdb3 is (hd1,2). In contrast to Linux, GRUB
   does not consider CD-ROM drives to be hard drives. For example, if
   using a CD on hdb and a second hard drive on hdc, that second hard
   drive would still be (hd1).

   Using the above information, determine the appropriate designator for
   the root partition (or boot partition, if a separate one is used). For
   the following example, it is assumed that the root (or separate boot)
   partition is hda4.

   Tell GRUB where to search for its stage{1,2} files. The Tab key can be
   used everywhere to make GRUB show the alternatives:
root (hd0,3)

Warning

   The following command will overwrite the current boot loader. Do not
   run the command if this is not desired, for example, if using a third
   party boot manager to manage the Master Boot Record (MBR). In this
   scenario, it would make more sense to install GRUB into the "boot
   sector" of the LFS partition. In this case, this next command would
   become setup (hd0,3).

   Tell GRUB to install itself into the MBR of had:
setup (hd0)

   If all went well, GRUB will have reported finding its files in
   /boot/grub. That's all there is to it. Quit the grub shell:
quit

   Create a "menu list" file defining GRUB's boot menu:
cat > /boot/grub/menu.lst << "EOF"
# Begin /boot/grub/menu.lst

# By default boot the first menu entry.
default 0

# Allow 30 seconds before booting the default.
timeout 30

# Use prettier colors.
color green/black light-green/black

# The first entry is for LFS.
title LFS 6.1.1
root (hd0,3)
kernel /boot/lfskernel-2.6.11.12 root=/dev/hda4
EOF

   Add an entry for the host distribution if desired. It might look like
   this:
cat >> /boot/grub/menu.lst << "EOF"
title Red Hat
root (hd0,2)
kernel /boot/kernel-2.6.5 root=/dev/hda3
initrd /boot/initrd-2.6.5
EOF

   If dual-booting Windows, the following entry will allow booting it:
cat >> /boot/grub/menu.lst << "EOF"
title Windows
rootnoverify (hd0,0)
chainloader +1
EOF

   If info grub does not provide all necessary material, additional
   information regarding GRUB is located on its website at:
   [495]http://www.gnu.org/software/grub/.

   The FHS stipulates that GRUB's menu.lst file should be symlinked to
   /etc/grub/menu.lst. To satisfy this requirement, issue the following
   command:
mkdir -v /etc/grub &&
ln -sv /boot/grub/menu.lst /etc/grub

Chapter 9. The End

9.1. The End

   Well done! The new LFS system is installed! We wish you much success
   with your shiny new custom-built Linux system.

   It may be a good idea to create an /etc/lfs-release file. By having
   this file, it is very easy for you (and for us if you need to ask for
   help at some point) to find out which LFS version is installed on the
   system. Create this file by running:
echo 6.1.1 > /etc/lfs-release

9.2. Get Counted

   Now that you have finished the book, do you want to be counted as an
   LFS user? Head over to
   [496]http://www.linuxfromscratch.org/cgi-bin/lfscounter.cgi and
   register as an LFS user by entering your name and the first LFS
   version you have used.

   Let's reboot into LFS now.

9.3. Rebooting the System

   Now that all of the software has been installed, it is time to reboot
   your computer. However, you should be aware of a few things. The
   system you have created in this book is quite minimal, and most likely
   will not have the functionality you would need to be able to continue
   forward. By installing a few extra packages from the BLFS book while
   still in our current chroot environment, you can leave yourself in a
   much better position to continue on once you reboot into your new LFS
   installation. Installing a text mode web browser, such as Lynx, you
   can easily view the BLFS book in one virtual terminal, while building
   packages in another. The GPM package will also allow you to perform
   copy/paste actions in your virtual terminals. Lastly, if you are in a
   situation where static IP configuration does not meet your networking
   requirements, installing packages such as Dhcpcd or PPP at this point
   might also be useful.

   Now that we have said that, lets move on to booting our shiny new LFS
   installation for the first time! First exit from the chroot
   environment:
logout

   Then unmount the virtual files systems:
umount -v $LFS/dev/pts
umount -v $LFS/dev/shm
umount -v $LFS/dev
umount -v $LFS/proc
umount -v $LFS/sys

   Unmount the LFS file system itself:
umount -v $LFS

   If multiple partitions were created, unmount the other partitions
   before unmounting the main one, like this:
umount -v $LFS/usr
umount -v $LFS/home
umount -v $LFS

   Now, reboot the system with:
shutdown -r now

   Assuming the GRUB boot loader was set up as outlined earlier, the menu
   is set to boot LFS 6.1.1 automatically.

   When the reboot is complete, the LFS system is ready for use and more
   software may be added to suit your needs.

9.4. What Now?

   Thank you for reading this LFS book. We hope that you have found this
   book helpful and have learned more about the system creation process.

   Now that the LFS system is installed, you may be wondering "What
   next?" To answer that question, we have compiled a list of resources
   for you.
     * Maintenance
       Bugs and security notices are reported regularly for all software.
       Since an LFS system is compiled from source, it is up to you to
       keep abreast of such reports. There are several online resources
       that track such reports, some of which are shown below:
          + Freshmeat.net ([497]http://freshmeat.net/)
            Freshmeat can notify you (via email) of new versions of
            packages installed on your system.
          + [498]CERT (Computer Emergency Response Team)
            CERT has a mailing list that publishes security alerts
            concerning various operating systems and applications.
            Subscription information is available at
            [499]http://www.us-cert.gov/cas/signup.html.
          + Bugtraq
            Bugtraq is a full-disclosure computer security mailing list.
            It publishes newly discovered security issues, and
            occasionally potential fixes for them. Subscription
            information is available at
            [500]http://www.securityfocus.com/archive.
     * Beyond Linux From Scratch
       The Beyond Linux From Scratch book covers installation procedures
       for a wide range of software beyond the scope of the LFS Book. The
       BLFS project is located at
       [501]http://www.linuxfromscratch.org/blfs/.
     * LFS Hints
       The LFS Hints are a collection of educational documents submitted
       by volunteers in the LFS community. The hints are available at
       [502]http://www.linuxfromscratch.org/hints/list.html.
     * Mailing lists
       There are several LFS mailing lists you may subscribe to if you
       are in need of help, want to stay current with the latest
       developments, want to contribute to the project, and more. See
       [503]Chapter 1 - Mailing Lists for more information.
     * The Linux Documentation Project
       The goal of The Linux Documentation Project (TLDP) is to
       collaborate on all of the issues of Linux documentation. The TLDP
       features a large collection of HOWTOs, guides, and man pages. It
       is located at [504]http://www.tldp.org/.

Part IV. Appendices

Table of Contents

     * [505]A. Acronyms and Terms
     * [506]B. Acknowledgments

Appendix A. Acronyms and Terms

   ABI

   Application Binary Interface
   ALFS

   Automated Linux From Scratch
   ALSA

   Advanced Linux Sound Architecture
   API

   Application Programming Interface
   ASCII

   American Standard Code for Information Interchange
   BIOS

   Basic Input/Output System
   BLFS

   Beyond Linux From Scratch
   BSD

   Berkeley Software Distribution
   chroot

   change root
   CMOS

   Complementary Metal Oxide Semiconductor
   COS

   Class Of Service
   CPU

   Central Processing Unit
   CRC

   Cyclic Redundancy Check
   CVS

   Concurrent Versions System
   DHCP

   Dynamic Host Configuration Protocol
   DNS

   Domain Name Service
   EGA

   Enhanced Graphics Adapter
   ELF

   Executable and Linkable Format
   EOF

   End of File
   EQN

   equation
   EVMS

   Enterprise Volume Management System
   ext2

   second extended file system
   FAQ

   Frequently Asked Questions
   FHS

   Filesystem Hierarchy Standard
   FIFO

   First-In, First Out
   FQDN

   Fully Qualified Domain Name
   FTP

   File Transfer Protocol
   GB

   Gibabytes
   GCC

   GNU Compiler Collection
   GID

   Group Identifier
   GMT

   Greenwich Mean Time
   GPG

   GNU Privacy Guard
   HTML

   Hypertext Markup Language
   IDE

   Integrated Drive Electronics
   IEEE

   Institute of Electrical and Electronic Engineers
   IO

   Input/Output
   IP

   Internet Protocol
   IPC

   Inter-Process Communication
   IRC

   Internet Relay Chat
   ISO

   International Organization for Standardization
   ISP

   Internet Service Provider
   KB

   Kilobytes
   LED

   Light Emitting Diode
   LFS

   Linux From Scratch
   LSB

   Linux Standards Base
   MB

   Megabytes
   MBR

   Master Boot Record
   MD5

   Message Digest 5
   NIC

   Network Interface Card
   NLS

   Native Language Support
   NNTP

   Network News Transport Protocol
   NPTL

   Native POSIX Threading Library
   OSS

   Open Sound System
   PCH

   Pre-Compiled Headers
   PCRE

   Perl Compatible Regular Expression
   PID

   Process Identifier
   PLFS

   Pure Linux From Scratch
   PTY

   pseudo terminal
   QA

   Quality Assurance
   QOS

   Quality Of Service
   RAM

   Random Access Memory
   RPC

   Remote Procedure Call
   RTC

   Real Time Clock
   SBU

   Standard Build Unit
   SCO

   The Santa Cruz Operation
   SGR

   Select Graphic Rendition
   SHA1

   Secure-Hash Algorithm 1
   SMP

   Symmetric Multi-Processor
   TLDP

   The Linux Documentation Project
   TFTP

   Trivial File Transfer Protocol
   TLS

   Thread-Local Storage
   UID

   User Identifier
   umask

   user file-creation mask
   USB

   Universal Serial Bus
   UTC

   Coordinated Universal Time
   UUID

   Universally Unique Identifier
   VC

   Virtual Console
   VGA

   Video Graphics Array
   VT

   Virtual Terminal

Appendix B. Acknowledgments

   We would like to thank the following people and organizations for
   their contributions to the Linux From Scratch Project.
     * [507]Gerard Beekmans <gerard AT linuxfromscratch D0T org> - LFS
       Creator, LFS Project Leader
     * [508]Matthew Burgess <matthew AT linuxfromscratch D0T org> - LFS
       Project Leader, LFS Technical Writer/Editor, LFS Release Manager
     * [509]Archaic <archaic AT linuxfromscratch D0T org> - LFS Technical
       Writer/Editor, HLFS Project Leader, BLFS Editor, Hints and Patches
       Project Maintainer
     * [510]Nathan Coulson <nathan AT linuxfromscratch D0T org> -
       LFS-Bootscripts Maintainer
     * [511]Bruce Dubbs <bdubbs AT linuxfromscratch D0T org> - BLFS
       Project Leader
     * [512]Manuel Canales Esparcia <manuel AT linuxfromscratch D0T org>
       - LFS/BLFS/HLFS XML and XSL Maintainer
     * [513]Jim Gifford <jim AT linuxfromscratch D0T org> - LFS Technical
       Writer, Patches Project Leader
     * [514]Jeremy Huntwork <jhuntwork AT linuxfromscratch D0T org> - LFS
       Technical Writer, LFS LiveCD Maintainer, ALFS Project Leader
     * [515]Anderson Lizardo <lizardo AT linuxfromscratch D0T org> -
       Website Backend-Scripts Maintainer
     * [516]Ryan Oliver <ryan AT linuxfromscratch D0T org> - LFS
       Toolchain Maintainer
     * [517]James Robertson <jwrober AT linuxfromscratch D0T org> -
       Bugzilla Maintainer
     * [518]Tushar Teredesai <tushar AT linuxfromscratch D0T org> - BLFS
       Book Editor, Hints and Patches Project Leader
     * Countless other people on the various LFS and BLFS mailing lists
       who helped make this book possible by giving their suggestions,
       testing the book, and submitting bug reports, instructions, and
       their experiences with installing various packages.

Translators

     * [519]Manuel Canales Esparcia <macana AT lfs-es D0T com> - Spanish
       LFS translation project
     * [520]Johan Lenglet <johan AT linuxfromscratch D0T org> - French
       LFS translation project
     * [521]Anderson Lizardo <lizardo AT linuxfromscratch D0T org> -
       Portuguese LFS translation project
     * [522]Thomas Reitelbach <tr AT erdfunkstelle D0T de> - German LFS
       translation project

Mirror Maintainers

North American Mirrors

     * [523]Scott Kveton <scott AT osuosl D0T org> - lfs.oregonstate.edu
       mirror
     * [524]Mikhail Pastukhov <miha AT xuy D0T biz> - lfs.130th.net
       mirror
     * [525]William Astle <lost AT l-w D0T net> - ca.linuxfromscratch.org
       mirror
     * [526]Jeremy Polen <jpolen AT rackspace D0T com> -
       us2.linuxfromscratch.org mirror
     * [527]Tim Jackson <tim AT idge D0T net> - linuxfromscratch.idge.net
       mirror
     * [528]Jeremy Utley <jeremy AT linux-phreak D0T net> -
       lfs.linux-phreak.net mirror

South American Mirrors

     * [529]Andres Meggiotto <sysop AT mesi D0T com D0T ar> -
       lfs.mesi.com.ar mirror
     * [530]Manuel Canales Esparcia <manuel AT linuxfromscratch D0T org>
       - lfsmirror.lfs-es.info mirror
     * [531]Eduardo B. Fonseca <ebf AT aedsolucoes D0T com D0T br> -
       br.linuxfromscratch.org mirror

European Mirrors

     * [532]Barna Koczka <barna AT siker D0T hu> -
       hu.linuxfromscratch.org mirror
     * [533]UK Mirror Service - linuxfromscratch.mirror.ac.uk mirror
     * [534]Martin Voss <Martin D0T Voss AT ada D0T de> -
       lfs.linux-matrix.net mirror
     * [535]Guido Passet <guido AT primerelay D0T net> -
       nl.linuxfromscratch.org mirror
     * [536]Bastiaan Jacques <baafie AT planet D0T nl> -
       lfs.pagefault.net mirror
     * [537]Roel Neefs <lfs-mirror AT linuxfromscratch D0T rave D0T org>
       - linuxfromscratch.rave.org mirror
     * [538]Justin Knierim <justin AT jrknierim D0T de> -
       www.lfs-matrix.de mirror
     * [539]Stephan Brendel <stevie AT stevie20 D0T de> -
       lfs.netservice-neuss.de mirror
     * [540]Antonin Sprinzl <Antonin D0T Sprinzl AT tuwien D0T ac D0T at>
       - at.linuxfromscratch.org mirror
     * [541]Fredrik Danerklint <fredan-lfs AT fredan D0T org> -
       se.linuxfromscratch.org mirror
     * [542]Parisian sysadmins <archive AT doc D0T cs D0T univ-paris8 D0T
       fr> - www2.fr.linuxfromscratch.org mirror
     * [543]Alexander Velin <velin AT zadnik D0T org> -
       bg.linuxfromscratch.org mirror
     * [544]Dirk Webster <dirk AT securewebservices D0T co D0T uk> -
       lfs.securewebservices.co.uk mirror
     * [545]Thomas Skyt <thomas AT sofagang D0T dk> -
       dk.linuxfromscratch.org mirror
     * [546]Simon Nicoll <sime AT dot-sime D0T com> -
       uk.linuxfromscratch.org mirror

Asian Mirrors

     * [547]Pui Yong <pyng AT spam D0T averse D0T net> -
       sg.linuxfromscratch.org mirror
     * [548]Stuart Harris <stuart AT althalus D0T me D0T uk> -
       lfs.mirror.intermedia.com.sg mirror

Australian Mirrors

     * [549]Jason Andrade <jason AT dstc D0T edu D0T au> -
       au.linuxfromscratch.org mirror

Former Project Team Members

     * [550]Christine Barczak <theladyskye AT linuxfromscratch D0T org> -
       LFS Book Editor
     * Timothy Bauscher
     * Robert Briggs
     * Ian Chilton
     * [551]Jeroen Coumans <jeroen AT linuxfromscratch D0T org> - Website
       Developer, FAQ Maintainer
     * Alex Groenewoud - LFS Technical Writer
     * Marc Heerdink
     * Mark Hymers
     * Seth W. Klein - FAQ maintainer
     * [552]Nicholas Leippe <nicholas AT linuxfromscratch D0T org> - Wiki
       Maintainer
     * Simon Perreault
     * [553]Scot Mc Pherson <scot AT linuxfromscratch D0T org> - LFS NNTP
       Gateway Maintainer
     * [554]Alexander Patrakov <semzx AT newmail D0T ru> - LFS Technical
       Writer
     * [555]Greg Schafer <gschafer AT zip D0T com D0T au> - LFS Technical
       Writer
     * Jesse Tie-Ten-Quee - LFS Technical Writer
     * [556]Jeremy Utley <jeremy AT linuxfromscratch D0T org> - LFS
       Technical Writer, Bugzilla Maintainer, LFS-Bootscripts Maintainer
     * [557]Zack Winkles <zwinkles AT gmail D0T com> - LFS Technical
       Writer

A very special thank you to our donators

     * [558]Dean Benson <dean AT vipersoft D0T co D0T uk> for several
       monetary contributions
     * [559]Hagen Herrschaft <hrx AT hrxnet D0T de> for donating a 2.2
       GHz P4 system, now running under the name of Lorien
     * [560]VA Software who, on behalf of [561]Linux.com, donated a VA
       Linux 420 (former StartX SP2) workstation
     * Mark Stone for donating Belgarath, the linuxfromscratch.org server

Index

Packages

     * Autoconf: [562]Autoconf-2.59
     * Automake: [563]Automake-1.9.5
     * Bash: [564]Bash-3.0
          + tools: [565]Bash-3.0
     * Binutils: [566]Binutils-2.15.94.0.2.2
          + tools, pass 1: [567]Binutils-2.15.94.0.2.2 - Pass 1
          + tools, pass 2: [568]Binutils-2.15.94.0.2.2 - Pass 2
     * Bison: [569]Bison-2.0
          + tools: [570]Bison-2.0
     * Bootscripts: [571]LFS-Bootscripts-3.2.1
          + usage: [572]How Do These Bootscripts Work?
     * Bzip2: [573]Bzip2-1.0.3
          + tools: [574]Bzip2-1.0.3
     * Coreutils: [575]Coreutils-5.2.1
          + tools: [576]Coreutils-5.2.1
     * DejaGNU: [577]DejaGNU-1.4.4
     * Diffutils: [578]Diffutils-2.8.1
          + tools: [579]Diffutils-2.8.1
     * E2fsprogs: [580]E2fsprogs-1.37
     * Expect: [581]Expect-5.43.0
     * File: [582]File-4.13
     * Findutils: [583]Findutils-4.2.23
          + tools: [584]Findutils-4.2.23
     * Flex: [585]Flex-2.5.31
          + tools: [586]Flex-2.5.31
     * Gawk: [587]Gawk-3.1.4
          + tools: [588]Gawk-3.1.4
     * GCC: [589]GCC-3.4.3
          + tools, pass 1: [590]GCC-3.4.3 - Pass 1
          + tools, pass 2: [591]GCC-3.4.3 - Pass 2
     * Gettext: [592]Gettext-0.14.3
          + tools: [593]Gettext-0.14.3
     * Glibc: [594]Glibc-2.3.4
          + tools: [595]Glibc-2.3.4
     * Grep: [596]Grep-2.5.1a
          + tools: [597]Grep-2.5.1a
     * Groff: [598]Groff-1.19.1
     * GRUB: [599]GRUB-0.96
          + configuring: [600]Making the LFS System Bootable
     * Gzip: [601]Gzip-1.3.5
          + tools: [602]Gzip-1.3.5
     * Hotplug: [603]Hotplug-2004_09_23
     * Iana-Etc: [604]Iana-Etc-1.04
     * Inetutils: [605]Inetutils-1.4.2
     * IPRoute2: [606]IPRoute2-2.6.11-050330
     * Kbd: [607]Kbd-1.12
     * Less: [608]Less-382
     * Libtool: [609]Libtool-1.5.14
     * Linux: [610]Linux-2.6.11.12
     * Linux-Libc-Headers: [611]Linux-Libc-Headers-2.6.11.2
          + tools, headers: [612]Linux-Libc-Headers-2.6.11.2
     * M4: [613]M4-1.4.3
          + tools: [614]M4-1.4.3
     * Make: [615]Make-3.80
          + tools: [616]Make-3.80
     * Man: [617]Man-1.5p
     * Man-pages: [618]Man-pages-2.01
     * Mktemp: [619]Mktemp-1.5
     * Module-Init-Tools: [620]Module-Init-Tools-3.1
     * Ncurses: [621]Ncurses-5.4
          + tools: [622]Ncurses-5.4
     * Patch: [623]Patch-2.5.4
          + tools: [624]Patch-2.5.4
     * Perl: [625]Perl-5.8.7
          + tools: [626]Perl-5.8.7
     * Procps: [627]Procps-3.2.5
     * Psmisc: [628]Psmisc-21.6
     * Readline: [629]Readline-5.0
     * Sed: [630]Sed-4.1.4
          + tools: [631]Sed-4.1.4
     * Shadow: [632]Shadow-4.0.9
          + configuring: [633]Configuring Shadow
     * Sysklogd: [634]Sysklogd-1.4.1
          + configuring: [635]Configuring Sysklogd
     * Sysvinit: [636]Sysvinit-2.86
          + configuring: [637]Configuring Sysvinit
     * Tar: [638]Tar-1.15.1
          + tools: [639]Tar-1.15.1
     * Tcl: [640]Tcl-8.4.9
     * Texinfo: [641]Texinfo-4.8
          + tools: [642]Texinfo-4.8
     * Udev: [643]Udev-056
          + usage: [644]Device and Module Handling on an LFS System
     * Util-linux: [645]Util-linux-2.12q
          + tools: [646]Util-linux-2.12q
     * Vim: [647]Vim-6.3
