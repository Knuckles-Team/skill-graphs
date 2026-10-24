```

Linux From Scratch

Version 6.1.1

Gerard Beekmans

   Copyright � 1999-2005 Gerard Beekmans

   Copyright (c) 1999-2005, Gerard Beekmans

   All rights reserved.

   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are
   met:
     * Redistributions in any form must retain the above copyright
       notice, this list of conditions and the following disclaimer
     * Neither the name of "Linux From Scratch" nor the names of its
       contributors may be used to endorse or promote products derived
       from this material without specific prior written permission
     * Any material derived from Linux From Scratch must contain a
       reference to the "Linux From Scratch" project

   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR
   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
   PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
   LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
     _________________________________________________________________

Table of Contents

     * Preface
          + [1]Foreword
          + [2]Audience
          + [3]Prerequisites
          + [4]Host System Requirements
          + [5]Typography
          + [6]Structure
          + [7]Errata
     * I. Introduction
          + 1. Introduction
               o [8]How to Build an LFS System
               o [9]Changelog
               o [10]Resources
               o [11]Help
     * II. Preparing for the Build
          + 2. Preparing a New Partition
               o [12]Introduction
               o [13]Creating a New Partition
               o [14]Creating a File System on the Partition
               o [15]Mounting the New Partition
          + 3. Packages and Patches
               o [16]Introduction
               o [17]All Packages
               o [18]Needed Patches
          + 4. Final Preparations
               o [19]About $LFS
               o [20]Creating the $LFS/tools Directory
               o [21]Adding the LFS User
               o [22]Setting Up the Environment
               o [23]About SBUs
               o [24]About the Test Suites
          + 5. Constructing a Temporary System
               o [25]Introduction
               o [26]Toolchain Technical Notes
               o [27]Binutils-2.15.94.0.2.2 - Pass 1
               o [28]GCC-3.4.3 - Pass 1
               o [29]Linux-Libc-Headers-2.6.11.2
               o [30]Glibc-2.3.4
               o [31]Adjusting the Toolchain
               o [32]Tcl-8.4.9
               o [33]Expect-5.43.0
               o [34]DejaGNU-1.4.4
               o [35]GCC-3.4.3 - Pass 2
               o [36]Binutils-2.15.94.0.2.2 - Pass 2
               o [37]Gawk-3.1.4
               o [38]Coreutils-5.2.1
               o [39]Bzip2-1.0.3
               o [40]Gzip-1.3.5
               o [41]Diffutils-2.8.1
               o [42]Findutils-4.2.23
               o [43]Make-3.80
               o [44]Grep-2.5.1a
               o [45]Sed-4.1.4
               o [46]Gettext-0.14.3
               o [47]Ncurses-5.4
               o [48]Patch-2.5.4
               o [49]Tar-1.15.1
               o [50]Texinfo-4.8
               o [51]Bash-3.0
               o [52]M4-1.4.3
               o [53]Bison-2.0
               o [54]Flex-2.5.31
               o [55]Util-linux-2.12q
               o [56]Perl-5.8.7
               o [57]Stripping
     * III. Building the LFS System
          + 6. Installing Basic System Software
               o [58]Introduction
               o [59]Mounting Virtual Kernel File Systems
               o [60]Entering the Chroot Environment
               o [61]Changing Ownership
               o [62]Creating Directories
               o [63]Creating Essential Symlinks
               o [64]Creating the passwd, group, and log Files
               o [65]Populating /dev
               o [66]Linux-Libc-Headers-2.6.11.2
               o [67]Man-pages-2.01
               o [68]Glibc-2.3.4
               o [69]Re-adjusting the Toolchain
               o [70]Binutils-2.15.94.0.2.2
               o [71]GCC-3.4.3
               o [72]Coreutils-5.2.1
               o [73]Zlib-1.2.3
               o [74]Mktemp-1.5
               o [75]Iana-Etc-1.04
               o [76]Findutils-4.2.23
               o [77]Gawk-3.1.4
               o [78]Ncurses-5.4
               o [79]Readline-5.0
               o [80]Vim-6.3
               o [81]M4-1.4.3
               o [82]Bison-2.0
               o [83]Less-382
               o [84]Groff-1.19.1
               o [85]Sed-4.1.4
               o [86]Flex-2.5.31
               o [87]Gettext-0.14.3
               o [88]Inetutils-1.4.2
               o [89]IPRoute2-2.6.11-050330
               o [90]Perl-5.8.7
               o [91]Texinfo-4.8
               o [92]Autoconf-2.59
               o [93]Automake-1.9.5
               o [94]Bash-3.0
               o [95]File-4.13
               o [96]Libtool-1.5.14
               o [97]Bzip2-1.0.3
               o [98]Diffutils-2.8.1
               o [99]Kbd-1.12
               o [100]E2fsprogs-1.37
               o [101]Grep-2.5.1a
               o [102]GRUB-0.96
               o [103]Gzip-1.3.5
               o [104]Hotplug-2004_09_23
               o [105]Man-1.5p
               o [106]Make-3.80
               o [107]Module-Init-Tools-3.1
               o [108]Patch-2.5.4
               o [109]Procps-3.2.5
               o [110]Psmisc-21.6
               o [111]Shadow-4.0.9
               o [112]Sysklogd-1.4.1
               o [113]Sysvinit-2.86
               o [114]Tar-1.15.1
               o [115]Udev-056
               o [116]Util-linux-2.12q
               o [117]About Debugging Symbols
               o [118]Stripping Again
               o [119]Cleaning Up
          + 7. Setting Up System Bootscripts
               o [120]Introduction
               o [121]LFS-Bootscripts-3.2.1
               o [122]How Do These Bootscripts Work?
               o [123]Device and Module Handling on an LFS System
               o [124]Configuring the setclock Script
               o [125]Configuring the Linux Console
               o [126]Configuring the sysklogd script
               o [127]Creating the /etc/inputrc File
               o [128]The Bash Shell Startup Files
               o [129]Configuring the localnet Script
               o [130]Creating the /etc/hosts File
               o [131]Configuring the network Script
          + 8. Making the LFS System Bootable
               o [132]Introduction
               o [133]Creating the /etc/fstab File
               o [134]Linux-2.6.11.12
               o [135]Making the LFS System Bootable
          + 9. The End
               o [136]The End
               o [137]Get Counted
               o [138]Rebooting the System
               o [139]What Now?
     * IV. Appendices
          + [140]A. Acronyms and Terms
          + [141]B. Acknowledgments
     * [142]Index

Preface

1. Foreword

   My adventures in Linux began in 1998 when I downloaded and installed
   my first distribution. After working with it for a while, I discovered
   issues I definitely would have liked to see improved upon. For
   example, I didn't like the arrangement of the bootscripts or the way
   programs were configured by default. I tried a number of alternative
   distributions to address these issues, yet each had its pros and cons.
   Finally, I realized that if I wanted full satisfaction from my Linux
   system, I would have to build my own from scratch.

   What does this mean? I resolved not to use pre-compiled packages of
   any kind, nor CD-ROMs or boot disks that would install basic
   utilities. I would use my current Linux system to develop my own
   customized system. This "perfect" Linux system would then have the
   strengths of various systems without their associated weaknesses. In
   the beginning, the idea was rather daunting, but I remained committed
   to the idea that a system could be built that would conform to my
   needs and desires rather than to a standard that just did not fit what
   I was looking for.

   After sorting through issues such as circular dependencies and
   compile-time errors, I created a custom-built Linux system that was
   fully operational and suitable to individual needs. This process also
   allowed me to create compact and streamlined Linux systems which are
   faster and take up less space than traditional operating systems. I
   called this system a Linux From Scratch system, or an LFS system for
   short.

   As I shared my goals and experiences with other members of the Linux
   community, it became apparent that there was sustained interest in the
   ideas set forth in my Linux adventures. Such custom-built LFS systems
   serve not only to meet user specifications and requirements, but also
   serve as an ideal learning opportunity for programmers and system
   administrators to enhance their Linux skills. Out of this broadened
   interest, the Linux From Scratch Project was born.

   This Linux From Scratch book provides readers with the background and
   instruction to design and build custom Linux systems. This book
   highlights the Linux from Scratch project and the benefits of using
   this system. Users can dictate all aspects of their system, including
   directory layout, script setup, and security. The resulting system
   will be compiled completely from the source code, and the user will be
   able to specify where, why, and how programs are installed. This book
   allows readers to fully customize Linux systems to their own needs and
   allows users more control over their system.

   I hope you will have a great time working on your own LFS system, and
   enjoy the numerous benefits of having a system that is truly your own.

   --
   Gerard Beekmans
   gerard AT linuxfromscratch D0T org

2. Audience

   There are many reasons why somebody would want to read this book. The
   principal reason is to install a Linux system from the source code. A
   question many people raise is, "why go through all the hassle of
   manually building a Linux system from scratch when you can just
   download and install an existing one?" That is a good question and is
   the impetus for this section of the book.

   One important reason for LFS's existence is to help people learn how a
   Linux system works from the inside out. Building an LFS system helps
   demonstrate what makes Linux tick, and how things work together and
   depend on each other. One of the best things that this learning
   experience provides is the ability to customize Linux to your own
   tastes and needs.

   A key benefit of LFS is that it allows users to have more control over
   the system without relying on someone else's Linux implementation.
   With LFS, you are in the driver's seat and dictate every aspect of the
   system, such as the directory layout and bootscript setup. You also
   dictate where, why, and how programs are installed.

   Another benefit of LFS is the ability to create a very compact Linux
   system. When installing a regular distribution, one is often forced to
   include several programs which are probably never used. These programs
   waste disk space, or worse, CPU cycles. It is not difficult to build
   an LFS system of less than 100 megabytes (MB), which is substantially
   smaller than the majority of existing installations. Does this still
   sound like a lot of space? A few of us have been working on creating a
   very small embedded LFS system. We successfully built a system that
   was specialized to run the Apache web server with approximately 8MB of
   disk space used. Further stripping could bring this down to 5 MB or
   less. Try that with a regular distribution! This is only one of the
   many benefits of designing your own Linux implementation.

   We could compare Linux distributions to a hamburger purchased at a
   fast-food restaurant--you have no idea what might be in what you are
   eating. LFS, on the other hand, does not give you a hamburger. Rather,
   LFS provides the recipe to make the exact hamburger desired. This
   allows users to review the recipe, omit unwanted ingredients, and add
   your own ingredients to enhance the flavor of the burger. When you are
   satisfied with the recipe, move on to preparing it. It can be made to
   exact specifications--broil it, bake it, deep-fry it, or barbecue it.

   Another analogy that we can use is that of comparing LFS with a
   finished house. LFS provides the skeletal plan of a house, but it is
   up to you to build it. LFS maintains the freedom to adjust plans
   throughout the process, customizing it to the user's needs and
   preferences.

   An additional advantage of a custom built Linux system is security. By
   compiling the entire system from source code, you are empowered to
   audit everything and apply all the security patches desired. It is no
   longer necessary to wait for somebody else to compile binary packages
   that fix a security hole. Unless you examine the patch and implement
   it yourself, you have no guarantee that the new binary package was
   built correctly and adequately fixes the problem.

   The goal of Linux From Scratch is to build a complete and usable
   foundation-level system. Readers who do not wish to build their own
   Linux system from scratch may not benefit from the information in this
   book. If you only want to know what happens while the computer boots,
   we recommend the "From Power Up To Bash Prompt" HOWTO located at
   [143]http://axiom.anu.edu.au/~okeefe/p2b/ or on The Linux
   Documentation Project's (TLDP) website at
   [144]http://www.tldp.org/HOWTO/From-PowerUp-To-Bash-Prompt-HOWTO.html.
   The HOWTO builds a system which is similar to that of this book, but
   it focuses strictly on creating a system capable of booting to a BASH
   prompt. Consider your objective. If you wish to build a Linux system
   while learning along the way, then this book is your best choice.

   There are too many good reasons to build your own LFS system to list
   them all here. This section is only the tip of the iceberg. As you
   continue in your LFS experience, you will find the power that
   information and knowledge truly bring.

3. Prerequisites

   Building an LFS system is not a simple task. It requires a certain
   level of existing knowledge of Unix system administration in order to
   resolve problems, and correctly execute the commands listed. In
   particular, as an absolute minimum, the reader should already have the
   ability to use the command line (shell) to copy or move files and
   directories, list directory and file contents, and change the current
   directory. It is also expected that the reader has a reasonable
   knowledge of using and installing Linux software.

   Because the LFS book assumes at least this basic level of skill, the
   various LFS support forums are unlikely to be able to provide you with
   much assistance; you will find that your questions regarding such
   basic knowledge will likely go unanswered, or you will simply be
   referred to the LFS essential pre-reading list.

   Before building an LFS system, we recommend reading the following
   HOWTOs:
     * Software-Building-HOWTO
       [145]http://www.tldp.org/HOWTO/Software-Building-HOWTO.html
       This is a comprehensive guide to building and installing "generic"
       Unix software distributions under Linux.
     * The Linux Users' Guide
       [146]http://www.linuxhq.com/guides/LUG/guide.html
       This guide covers the usage of assorted Linux software.
     * The Essential Pre-Reading Hint
       [147]http://www.linuxfromscratch.org/hints/downloads/files/essenti
       al_prereading.txt
       This is an LFS Hint written specifically for users new to Linux.
       It includes a list of links to excellent sources of information on
       a wide range of topics. Anyone attempting to install LFS should
       have an understanding of many of the topics in this hint.

4. Host System Requirements

   The host must be running at least a 2.6.2 kernel compiled with GCC-3.0
   or higher. There are two main reasons for this requirement. First, the
   Native POSIX Threading Library (NPTL) test suite will segfault if the
   host's kernel has not been compiled with GCC-3.0 or a later version.
   Second, the 2.6.2 or later version of the kernel is required for the
   use of Udev. Udev creates devices dynamically by reading from the
   sysfs file system. However, support for this filesystem has only
   recently been implemented in most of the kernel drivers. We must be
   sure that all critical system devices get created properly.

   In order to determine whether the host kernel meets the requirements
   outlined above, run the following command:
cat /proc/version

   This will produce output similar to:
Linux version 2.6.2 (user@host) (gcc version 3.4.0) #1
    Tue Apr 20 21:22:18 GMT 2004

   If the results of the above command do not state that the host kernel
   is either 2.6.2 (or later), or that it was not compiled using a
   GCC-3.0 (or later) compiler, one will need to be installed. There are
   two methods you can take to solve this. First, see if your Linux
   vendor provides a 2.6.2 (or later) kernel package. If so, you may wish
   to install it. If your vendor doesn't offer a 2.6.2 (or later) kernel
   package, or you would prefer not to install it, then you can compile a
   2.6 kernel yourself. Instructions for compiling the kernel and
   configuring the boot loader (assuming the host uses GRUB) are located
   in [148]Chapter 8. This second option can also be seen as a gauge of
   your current Linux skills. If this second requirement is too steep,
   then the LFS book will not likely be much use to you at this time.

5. Typography

   To make things easier to follow, there are a few typographical
   conventions used throughout this book. This section contains some
   examples of the typographical format found throughout Linux From
   Scratch.
./configure --prefix=/usr

   This form of text is designed to be typed exactly as seen unless
   otherwise noted in the surrounding text. It is also used in the
   explanation sections to identify which of the commands is being
   referenced.
install-info: unknown option '--dir-file=/mnt/lfs/usr/info/dir'

   This form of text (fixed-width text) shows screen output, probably as
   the result of commands issued. This format is also used to show
   filenames, such as /etc/ld.so.conf.

   Emphasis

   This form of text is used for several purposes in the book. Its main
   purpose is to emphasize important points or items.

   [149]http://www.linuxfromscratch.org/

   This format is used for hyperlinks both within the LFS community and
   to external pages. It includes HOWTOs, download locations, and
   websites.
cat > $LFS/etc/group << "EOF"
root:x:0:
bin:x:1:
......
EOF

   This format is used when creating configuration files. The first
   command tells the system to create the file $LFS/etc/group from
   whatever is typed on the following lines until the sequence end of
   file (EOF) is encountered. Therefore, this entire section is generally
   typed as seen.

   [REPLACED TEXT]

   This format is used to encapsulate text that is not to be typed as
   seen or copied-and-pasted.

   passwd(5)

   This format is used to refer to a specific manual page (hereinafter
   referred to simply as a "man" page). The number inside parentheses
   indicates a specific section inside of man. For example, passwd has
   two man pages. Per LFS installation instructions, those two man pages
   will be located at /usr/share/man/man1/passwd.1 and
   /usr/share/man/man5/passwd.5. Both man pages have different
   information in them. When the book uses passwd(5) it is specifically
   referring to /usr/share/man/man5/passwd.5. man passwd will print the
   first man page it finds that matches "passwd", which will be
   /usr/share/man/man1/passwd.1. For this example, you will need to run
   man 5 passwd in order to read the specific page being referred to. It
   should be noted that most man pages do not have duplicate page names
   in different sections. Therefore, man [program name] is generally
   sufficient.

6. Structure

   This book is divided into the following parts.

6.1. Part I - Introduction

   Part I explains a few important notes on how to proceed with the LFS
   installation. This section also provides meta-information about the
   book.

6.2. Part II - Preparing for the Build

   Part II describes how to prepare for the building process--making a
   partition, downloading the packages, and compiling temporary tools.

6.3. Part III - Building the LFS System

   Part III guides the reader through the building of the LFS
   system--compiling and installing all the packages one by one, setting
   up the boot scripts, and installing the kernel. The resulting Linux
   system is the foundation on which other software can be built to
   expand the system as desired. At the end of this book, there is an
   easy to use reference listing all of the programs, libraries, and
   important files that have been installed.

7. Errata

   The software used to create an LFS system is constantly being updated
   and enhanced. Security warnings and bug fixes may become available
   after the LFS book has been released. To check whether the package
   versions or instructions in this release of LFS need any modifications
   to accommodate security vulnerabilities or other bug fixes, please
   visit [150]http://www.linuxfromscratch.org/lfs/errata/6.1.1/ before
   proceeding with your build. You should note any changes shown and
   apply them to the relevant section of the book as you progress with
   building the LFS system.

Part I. Introduction

Table of Contents

     * 1. Introduction
          + [151]How to Build an LFS System
          + [152]Changelog
          + [153]Resources
          + [154]Help

Chapter 1. Introduction

1.1. How to Build an LFS System

   The LFS system will be built by using a previously installed Linux
   distribution (such as Debian, Mandrake, Red Hat, or SuSE). This
   existing Linux system (the host) will be used as a starting point to
   provide necessary programs, including a compiler, linker, and shell,
   to build the new system. Select the "development" option during the
   distribution installation to be able to access these tools.

   As an alternative to installing an entire separate distribution onto
   your machine, you may wish to use the Linux From Scratch LiveCD. The
   CD works well as a host system, providing all the tools you need to
   successfully follow the instructions in this book. Additionally, it
   contains all the source packages, patches and a copy of this book. So
   once you have the CD, no network connection or additional downloads
   are necessary. For more information about the LFS LiveCD or to
   download a copy, visit [155]http://www.linuxfromscratch.org/livecd/.

   [156]Chapter 2 of this book describes how to create a new Linux native
   partition and file system, the place where the new LFS system will be
   compiled and installed. [157]Chapter 3 explains which packages and
   patches need to be downloaded to build an LFS system and how to store
   them on the new file system. [158]Chapter 4 discusses the setup for an
   appropriate working environment. Please read [159]Chapter 4 carefully
   as it explains several important issues the developer should be aware
   of before beginning to work through [160]Chapter 5 and beyond.

   [161]Chapter 5 explains the installation of a number of packages that
   will form the basic development suite (or toolchain) which is used to
   build the actual system in [162]Chapter 6. Some of these packages are
   needed to resolve circular dependencies--for example, to compile a
   compiler, you need a compiler.

   [163]Chapter 5 also shows the user how to build a first pass of the
   toolchain, including Binutils and GCC (first pass basically means
   these two core packages will be re-installed a second time). The next
   step is to build Glibc, the C library. Glibc will be compiled by the
   toolchain programs built in the first pass. Then, a second pass of the
   toolchain will be built. This time, the toolchain will be dynamically
   linked against the newly built Glibc. The remaining [164]Chapter 5
   packages are built using this second pass toolchain. When this is
   done, the LFS installation process will no longer depend on the host
   distribution, with the exception of the running kernel.

   This effort to isolate the new system from the host distribution may
   seem excessive, but a full technical explanation is provided in
   [165]Section 5.2, "Toolchain Technical Notes".

   In [166]Chapter 6, the full LFS system is built. The chroot (change
   root) program is used to enter a virtual environment and start a new
   shell whose root directory will be set to the LFS partition. This is
