# The first entry is for LFS.
title LFS 6.1.1
root (hd0,3)
kernel /boot/lfskernel-2.6.11.12 root=/dev/hda4`
EOF`
```

Add an entry for the host distribution if desired. It might look like this:
```
`cat >> /boot/grub/menu.lst << "EOF"
`title Red Hat
root (hd0,2)
kernel /boot/kernel-2.6.5 root=/dev/hda3
initrd /boot/initrd-2.6.5`
EOF`
```

If dual-booting Windows, the following entry will allow booting it:
```
`cat >> /boot/grub/menu.lst << "EOF"
`title Windows
rootnoverify (hd0,0)
chainloader +1`
EOF`
```

If **info grub** does not provide all necessary material, additional information regarding GRUB is located on its website at:
The FHS stipulates that GRUB's `menu.lst` file should be symlinked to `/etc/grub/menu.lst`. To satisfy this requirement, issue the following command:
```
`mkdir -v /etc/grub &&
ln -sv /boot/grub/menu.lst /etc/grub`
```

##  Chapter 9. The End
##  9.1. The End
Well done! The new LFS system is installed! We wish you much success with your shiny new custom-built Linux system.
It may be a good idea to create an `/etc/lfs-release` file. By having this file, it is very easy for you (and for us if you need to ask for help at some point) to find out which LFS version is installed on the system. Create this file by running:
```
`echo 6.1.1 > /etc/lfs-release`
```

##  9.2. Get Counted
Now that you have finished the book, do you want to be counted as an LFS user? Head over to
Let's reboot into LFS now.
##  9.3. Rebooting the System
Now that all of the software has been installed, it is time to reboot your computer. However, you should be aware of a few things. The system you have created in this book is quite minimal, and most likely will not have the functionality you would need to be able to continue forward. By installing a few extra packages from the BLFS book while still in our current chroot environment, you can leave yourself in a much better position to continue on once you reboot into your new LFS installation. Installing a text mode web browser, such as Lynx, you can easily view the BLFS book in one virtual terminal, while building packages in another. The GPM package will also allow you to perform copy/paste actions in your virtual terminals. Lastly, if you are in a situation where static IP configuration does not meet your networking requirements, installing packages such as Dhcpcd or PPP at this point might also be useful.
Now that we have said that, lets move on to booting our shiny new LFS installation for the first time! First exit from the chroot environment:
```
`logout`
```

Then unmount the virtual files systems:
```
`umount -v $LFS/dev/pts
umount -v $LFS/dev/shm
umount -v $LFS/dev
umount -v $LFS/proc
umount -v $LFS/sys`
```

Unmount the LFS file system itself:
```
`umount -v $LFS`
```

If multiple partitions were created, unmount the other partitions before unmounting the main one, like this:
```
`umount -v $LFS/usr
umount -v $LFS/home
umount -v $LFS`
```

Now, reboot the system with:
```
`shutdown -r now`
```

Assuming the GRUB boot loader was set up as outlined earlier, the menu is set to boot _LFS 6.1.1_ automatically.
When the reboot is complete, the LFS system is ready for use and more software may be added to suit your needs.
##  9.4. What Now?
Thank you for reading this LFS book. We hope that you have found this book helpful and have learned more about the system creation process.
Now that the LFS system is installed, you may be wondering “What next?” To answer that question, we have compiled a list of resources for you.
  * Maintenance
Bugs and security notices are reported regularly for all software. Since an LFS system is compiled from source, it is up to you to keep abreast of such reports. There are several online resources that track such reports, some of which are shown below:
    * Freshmeat.net (
Freshmeat can notify you (via email) of new versions of packages installed on your system.
    * CERT has a mailing list that publishes security alerts concerning various operating systems and applications. Subscription information is available at
    * Bugtraq
Bugtraq is a full-disclosure computer security mailing list. It publishes newly discovered security issues, and occasionally potential fixes for them. Subscription information is available at
  * Beyond Linux From Scratch
The Beyond Linux From Scratch book covers installation procedures for a wide range of software beyond the scope of the LFS Book. The BLFS project is located at
  * LFS Hints
The LFS Hints are a collection of educational documents submitted by volunteers in the LFS community. The hints are available at
  * Mailing lists
There are several LFS mailing lists you may subscribe to if you are in need of help, want to stay current with the latest developments, want to contribute to the project, and more. See [Chapter 1 - Mailing Lists](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-scatter-maillists) for more information.
  * The Linux Documentation Project
The goal of The Linux Documentation Project (TLDP) is to collaborate on all of the issues of Linux documentation. The TLDP features a large collection of HOWTOs, guides, and man pages. It is located at [_http://www.tldp.org/_](http://www.tldp.org/).


#  Part IV. Appendices
###  Table of Contents
  * [A. Acronyms and Terms](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#appendixa)
  * [B. Acknowledgments](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#appendixb)


##  Appendix A. Acronyms and Terms
**ABI** |  Application Binary Interface
---|---
**ALFS** |  Automated Linux From Scratch
**ALSA** |  Advanced Linux Sound Architecture
**API** |  Application Programming Interface
**ASCII** |  American Standard Code for Information Interchange
**BIOS** |  Basic Input/Output System
**BLFS** |  Beyond Linux From Scratch
**BSD** |  Berkeley Software Distribution
**chroot** |  change root
**CMOS** |  Complementary Metal Oxide Semiconductor
**COS** |  Class Of Service
**CPU** |  Central Processing Unit
**CRC** |  Cyclic Redundancy Check
**CVS** |  Concurrent Versions System
**DHCP** |  Dynamic Host Configuration Protocol
**DNS** |  Domain Name Service
**EGA** |  Enhanced Graphics Adapter
**ELF** |  Executable and Linkable Format
**EOF** |  End of File
**EQN** |  equation
**EVMS** |  Enterprise Volume Management System
**ext2** |  second extended file system
**FAQ** |  Frequently Asked Questions
**FHS** |  Filesystem Hierarchy Standard
**FIFO** |  First-In, First Out
**FQDN** |  Fully Qualified Domain Name
**FTP** |  File Transfer Protocol
**GB** |  Gibabytes
**GCC** |  GNU Compiler Collection
**GID** |  Group Identifier
**GMT** |  Greenwich Mean Time
**GPG** |  GNU Privacy Guard
**HTML** |  Hypertext Markup Language
**IDE** |  Integrated Drive Electronics
**IEEE** |  Institute of Electrical and Electronic Engineers
**IO** |  Input/Output
**IP** |  Internet Protocol
**IPC** |  Inter-Process Communication
**IRC** |  Internet Relay Chat
**ISO** |  International Organization for Standardization
**ISP** |  Internet Service Provider
**KB** |  Kilobytes
**LED** |  Light Emitting Diode
**LFS** |  Linux From Scratch
**LSB** |  Linux Standards Base
**MB** |  Megabytes
**MBR** |  Master Boot Record
**MD5** |  Message Digest 5
**NIC** |  Network Interface Card
**NLS** |  Native Language Support
**NNTP** |  Network News Transport Protocol
**NPTL** |  Native POSIX Threading Library
**OSS** |  Open Sound System
**PCH** |  Pre-Compiled Headers
**PCRE** |  Perl Compatible Regular Expression
**PID** |  Process Identifier
**PLFS** |  Pure Linux From Scratch
**PTY** |  pseudo terminal
**QA** |  Quality Assurance
**QOS** |  Quality Of Service
**RAM** |  Random Access Memory
**RPC** |  Remote Procedure Call
**RTC** |  Real Time Clock
**SBU** |  Standard Build Unit
**SCO** |  The Santa Cruz Operation
**SGR** |  Select Graphic Rendition
**SHA1** |  Secure-Hash Algorithm 1
**SMP** |  Symmetric Multi-Processor
**TLDP** |  The Linux Documentation Project
**TFTP** |  Trivial File Transfer Protocol
**TLS** |  Thread-Local Storage
**UID** |  User Identifier
**umask** |  user file-creation mask
**USB** |  Universal Serial Bus
**UTC** |  Coordinated Universal Time
**UUID** |  Universally Unique Identifier
**VC** |  Virtual Console
**VGA** |  Video Graphics Array
**VT** |  Virtual Terminal
##  Appendix B. Acknowledgments
We would like to thank the following people and organizations for their contributions to the Linux From Scratch Project.
  * Countless other people on the various LFS and BLFS mailing lists who helped make this book possible by giving their suggestions, testing the book, and submitting bug reports, instructions, and their experiences with installing various packages.


##  Translators
##  Mirror Maintainers
###  North American Mirrors
###  South American Mirrors
###  European Mirrors
###  Asian Mirrors
###  Australian Mirrors
##  Former Project Team Members
  * Timothy Bauscher
  * Robert Briggs
  * Ian Chilton
  * Alex Groenewoud – LFS Technical Writer
  * Marc Heerdink
  * Mark Hymers
  * Seth W. Klein – FAQ maintainer
  * Simon Perreault
  * Jesse Tie-Ten-Quee – LFS Technical Writer


##  A very special thank you to our donators
  * Mark Stone for donating Belgarath, the linuxfromscratch.org server


#  Index
##  Packages
  * **Autoconf:** [Autoconf-2.59](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-autoconf)
  * **Automake:** [Automake-1.9.5](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-automake)
  * **Bash:** [Bash-3.0](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bash)
    * **tools:** [Bash-3.0](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-bash)
  * **Binutils:** [Binutils-2.15.94.0.2.2](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-binutils)
    * **tools, pass 1:** [Binutils-2.15.94.0.2.2 - Pass 1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-binutils-pass1)
    * **tools, pass 2:** [Binutils-2.15.94.0.2.2 - Pass 2](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-binutils-pass2)
  * **Bison:** [Bison-2.0](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bison)
    * **tools:** [Bison-2.0](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-bison)
  * **Bootscripts:** [LFS-Bootscripts-3.2.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-scripts-bootscripts)
    * **usage:** [How Do These Bootscripts Work?](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-scripts-usage)
  * **Bzip2:** [Bzip2-1.0.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bzip2)
    * **tools:** [Bzip2-1.0.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-bzip2)
  * **Coreutils:** [Coreutils-5.2.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-coreutils)
    * **tools:** [Coreutils-5.2.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-coreutils)
  * **DejaGNU:** [DejaGNU-1.4.4](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-dejagnu)
  * **Diffutils:** [Diffutils-2.8.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-diffutils)
    * **tools:** [Diffutils-2.8.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-diffutils)
  * **E2fsprogs:** [E2fsprogs-1.37](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-e2fsprogs)
  * **Expect:** [Expect-5.43.0](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-expect)
  * **File:** [File-4.13](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-file)
  * **Findutils:** [Findutils-4.2.23](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-findutils)
    * **tools:** [Findutils-4.2.23](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-findutils)
  * **Flex:** [Flex-2.5.31](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-flex)
    * **tools:** [Flex-2.5.31](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-flex)
  * **Gawk:** [Gawk-3.1.4](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-gawk)
    * **tools:** [Gawk-3.1.4](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-gawk)
  * **GCC:** [GCC-3.4.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-gcc)
    * **tools, pass 1:** [GCC-3.4.3 - Pass 1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-gcc-pass1)
    * **tools, pass 2:** [GCC-3.4.3 - Pass 2](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-gcc-pass2)
  * **Gettext:** [Gettext-0.14.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-gettext)
    * **tools:** [Gettext-0.14.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-gettext)
  * **Glibc:** [Glibc-2.3.4](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-glibc)
    * **tools:** [Glibc-2.3.4](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-glibc)
  * **Grep:** [Grep-2.5.1a](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-grep)
    * **tools:** [Grep-2.5.1a](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-grep)
  * **Groff:** [Groff-1.19.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-groff)
  * **GRUB:** [GRUB-0.96](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-grub)
    * **configuring:** [Making the LFS System Bootable](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-bootable-grub)
  * **Gzip:** [Gzip-1.3.5](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-gzip)
    * **tools:** [Gzip-1.3.5](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-gzip)
  * **Hotplug:** [Hotplug-2004_09_23](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-hotplug)
  * **Iana-Etc:** [Iana-Etc-1.04](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-iana-etc)
  * **Inetutils:** [Inetutils-1.4.2](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-inetutils)
  * **IPRoute2:** [IPRoute2-2.6.11-050330](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-iproute2)
  * **Kbd:** [Kbd-1.12](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-kbd)
  * **Less:** [Less-382](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-less)
  * **Libtool:** [Libtool-1.5.14](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-libtool)
  * **Linux:** [Linux-2.6.11.12](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-bootable-kernel)
  * **Linux-Libc-Headers:** [Linux-Libc-Headers-2.6.11.2](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-linux-libc-headers)
    * **tools, headers:** [Linux-Libc-Headers-2.6.11.2](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-linux-libc-headers)
  * **M4:** [M4-1.4.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-m4)
    * **tools:** [M4-1.4.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-m4)
  * **Make:** [Make-3.80](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-make)
    * **tools:** [Make-3.80](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-make)
  * **Man:** [Man-1.5p](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-man)
  * **Man-pages:** [Man-pages-2.01](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-man-pages)
  * **Mktemp:** [Mktemp-1.5](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-mktemp)
  * **Module-Init-Tools:** [Module-Init-Tools-3.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-module-init-tools)
  * **Ncurses:** [Ncurses-5.4](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-ncurses)
    * **tools:** [Ncurses-5.4](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-ncurses)
  * **Patch:** [Patch-2.5.4](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-patch)
    * **tools:** [Patch-2.5.4](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-patch)
  * **Perl:** [Perl-5.8.7](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-perl)
    * **tools:** [Perl-5.8.7](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-perl)
  * **Procps:** [Procps-3.2.5](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-procps)
  * **Psmisc:** [Psmisc-21.6](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-psmisc)
  * **Readline:** [Readline-5.0](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-readline)
  * **Sed:** [Sed-4.1.4](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-sed)
    * **tools:** [Sed-4.1.4](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-sed)
  * **Shadow:** [Shadow-4.0.9](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-shadow)
    * **configuring:** [Configuring Shadow](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#conf-shadow)
  * **Sysklogd:** [Sysklogd-1.4.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-sysklogd)
    * **configuring:** [Configuring Sysklogd](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#conf-sysklogd)
  * **Sysvinit:** [Sysvinit-2.86](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-sysvinit)
    * **configuring:** [Configuring Sysvinit](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#conf-sysvinit)
  * **Tar:** [Tar-1.15.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-tar)
    * **tools:** [Tar-1.15.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-tar)
  * **Tcl:** [Tcl-8.4.9](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-tcl)
  * **Texinfo:** [Texinfo-4.8](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-texinfo)
    * **tools:** [Texinfo-4.8](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-texinfo)
  * **Udev:** [Udev-056](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-udev)
    * **usage:** [Device and Module Handling on an LFS System](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-scripts-udev)
  * **Util-linux:** [Util-linux-2.12q](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-util-linux)
    * **tools:** [Util-linux-2.12q](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-tools-util-linux)
  * **Vim:** [Vim-6.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-vim)
  * **Zlib:** [Zlib-1.2.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-zlib)


##  Programs
  * **a2p:** [Perl-5.8.7](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-perl) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#a2p)
  * **acinstall:** [Automake-1.9.5](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-automake) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#acinstall)
  * **aclocal:** [Automake-1.9.5](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-automake) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#aclocal)
  * **aclocal-1.9.5:** [Automake-1.9.5](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-automake) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#aclocal-version)
  * **addftinfo:** [Groff-1.19.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-groff) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#addftinfo)
  * **addr2line:** [Binutils-2.15.94.0.2.2](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-binutils) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#addr2line)
  * **afmtodit:** [Groff-1.19.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-groff) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#afmtodit)
  * **agetty:** [Util-linux-2.12q](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-util-linux) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#agetty)
  * **apropos:** [Man-1.5p](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-man) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#apropos)
  * **ar:** [Binutils-2.15.94.0.2.2](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-binutils) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ar)
  * **arch:** [Util-linux-2.12q](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-util-linux) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#arch)
  * **as:** [Binutils-2.15.94.0.2.2](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-binutils) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#as)
  * **autoconf:** [Autoconf-2.59](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-autoconf) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#autoconf)
  * **autoheader:** [Autoconf-2.59](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-autoconf) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#autoheader)
  * **autom4te:** [Autoconf-2.59](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-autoconf) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#autom4te)
  * **automake:** [Automake-1.9.5](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-automake) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#automake)
  * **automake-1.9.5:** [Automake-1.9.5](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-automake) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#automake-version)
  * **autopoint:** [Gettext-0.14.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-gettext) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#autopoint)
  * **autoreconf:** [Autoconf-2.59](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-autoconf) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#autoreconf)
  * **autoscan:** [Autoconf-2.59](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-autoconf) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#autoscan)
  * **autoupdate:** [Autoconf-2.59](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-autoconf) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#autoupdate)
  * **awk:** [Gawk-3.1.4](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-gawk) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#awk)
  * **badblocks:** [E2fsprogs-1.37](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-e2fsprogs) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#badblocks)
  * **basename:** [Coreutils-5.2.1](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-coreutils) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#basename)
  * **bash:** [Bash-3.0](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bash) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#bash)
  * **bashbug:** [Bash-3.0](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bash) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#bashbug)
  * **bigram:** [Findutils-4.2.23](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-findutils) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#bigram)
  * **bison:** [Bison-2.0](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bison) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#bison)
  * **blkid:** [E2fsprogs-1.37](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-e2fsprogs) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#blkid)
  * **blockdev:** [Util-linux-2.12q](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-util-linux) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#blockdev)
  * **bunzip2:** [Bzip2-1.0.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bzip2) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#bunzip2)
  * **bzcat:** [Bzip2-1.0.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bzip2) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#bzcat)
  * **bzcmp:** [Bzip2-1.0.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bzip2) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#bzcmp)
  * **bzdiff:** [Bzip2-1.0.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bzip2) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#bzdiff)
  * **bzegrep:** [Bzip2-1.0.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bzip2) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#bzegrep)
  * **bzfgrep:** [Bzip2-1.0.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bzip2) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#bzfgrep)
  * **bzgrep:** [Bzip2-1.0.3](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-system-bzip2) -- [description](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#bzgrep)
