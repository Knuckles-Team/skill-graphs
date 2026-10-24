   very similar to rebooting and instructing the kernel to mount the LFS
   partition as the root partition. The system does not actually reboot,
   but instead chroot's because creating a bootable system requires
   additional work which is not necessary just yet. The major advantage
   is that "chrooting" allows the builder to continue using the host
   while LFS is being built. While waiting for package compilation to
   complete, a user can switch to a different virtual console (VC) or X
   desktop and continue using the computer as normal.

   To finish the installation, the LFS-Bootscripts are set up in
   [167]Chapter 7, and the kernel and boot loader are set up in
   [168]Chapter 8. [169]Chapter 9 contains information on furthering the
   LFS experience beyond this book. After the steps in this book have
   been implemented, the computer will be ready to reboot into the new
   LFS system.

   This is the process in a nutshell. Detailed information on each step
   is discussed in the following chapters and package descriptions. Items
   that may seem complicated will be clarified, and everything will fall
   into place as the reader embarks on the LFS adventure.

1.2. Changelog

   This is version 6.1.1 of the Linux From Scratch book, dated November
   30, 2005. If this book is more than six months old, a newer and better
   version is probably already available. To find out, please check one
   of the mirrors via [170]http://www.linuxfromscratch.org/.

   Below is a list of changes made since the previous release of the
   book. First a summary, then a detailed log.
     * Upgraded to:
          + Perl 5.8.7
          + Zlib 1.2.3
     * Added:
          + binutils-2.15.94.0.2.2-gcc4-1.patch
          + bzip2-1.0.3-install_docs-1.patch
          + bzip2-1.0.3-bzgrep_security-1.patch
          + glibc-2.3.4-rtld_search_dirs-1.patch
          + glibc-2.3.4-tls_assert-1.patch
          + texinfo-4.8-tempfile_fix-1.patch
          + util-linux-2.12q-umount_fix-1.patch
          + vim-6.3-security_fix-2.patch
     * Removed:
          + zlib-1.2.2-security_fix-1.patch;
     * November 30, 2005 [matt]: LFS-6.1.1 release.
     * November 24, 2005 [matt]: LFS-6.1.1-pre2 release.
     * November 24, 2005 [matt]: Fix an issue with Glibc that prevents
       some programs (including OpenOffice.org) from running.
     * November 23, 2005 [gerard]: Corrected reference to 'man page' to
       'HTML documentation' in chapter 6/sec
     * November 18, 2005 [manuel]: Fixed the unpack of the
       module-init-tools-testsuite package.
     * November 18, 2005 [manuel]: PDF fixes.
     * November 17, 2005 [matt]: LFS-6.1.1-pre1 release.
     * November 12, 2005 [matt]: Improve the heuristic for determining a
       locale that is supported by both Glibc and packages outside LFS
       (bug 1642). Many thanks to Alexander Patrakov for highlighting the
       numerous issues and for reviewing the various suggested fixes.
     * November 12, 2005 [matt]: Omit running Bzip2's testsuite as a
       separate step, as make runs it automatically (bug 1652).
     * November 7, 2005 [matt]: Stop Udev from killing udevd processes on
       the host system (fixes bug 1651). Thanks to Alexander Patrakov for
       the report and the fix.
     * November 5, 2005 [matt]: Add a note to the toolchain sanity check
       in chapter 5 to explain that if TCL fails to build, it's an
       indication of a broken toolchain (bug 1581).
     * November 4, 2005 [matt]: Correct the instructions for running
       Module-Init-Tools' testsuite (fixes bug 1597). Thanks to Greg
       Schafer, Tushar Teredesai and to Randy McMurchy for providing the
       patch.
     * October 29, 2005 [manuel]: PDF fixes.
     * October 23, 2005 [manuel]: Added Bash documentation installation.
       Added notes about libiconv and Cracklib. Fixed the installation of
       Sed documentation. Replaced a patch for IPRoute2 by a sed command.
     * October 19, 2005 [manuel]: Updated the acknowledgements to current
       trunk version. Ported some redaction changes in preface and
       chapter01 pages. Moved chapter02 to part II. Added -v switches.
       Ported several typos and redaction fixes from trunk.
     * October 19, 2005 [manuel]: Updated the stylesheets, Makefile and
       related files to current trunk versions.
     * October 15, 2005 [matt]: Use an updated version of the Udev rules
       file (fixes bug 1639).
     * October 15, 2005 [matt]: Add a cdrom group as required by the Udev
       rules file
     * October 14th, 2005 [ken]: Added a patch to allow binutils to be
       built from a host running gcc-4, updated glibc instructions for
       the rtld patch, updated space/time for perl and zlib.
     * October 14th, 2005 [matt]: Added a patch to fix a security
       vulnerability in util-linux.
     * October 14th, 2005 [matt]: Added the updated vim security patch.
     * October 14th, 2005 [jhuntwork]: Added the bzip2 security and
       install docs patches.
     * October 14th, 2005 [jhuntwork]: Added the tempfile patch for
       texinfo.
     * October 14th, 2005 [ken]: Update packages and patches in the
       changelog to only reflect changes since 6.1. Update zlib.
     * October 13th, 2005 [ken]: Fix known errors in lists of installed
       files and bump the perl version.

1.3. Resources

1.3.1. FAQ

   If during the building of the LFS system you encounter any errors,
   have any questions, or think there is a typo in the book, please start
   by consulting the Frequently Asked Questions (FAQ) that is located at
   [171]http://www.linuxfromscratch.org/faq/.

1.3.2. Mailing Lists

   The linuxfromscratch.org server hosts a number of mailing lists used
   for the development of the LFS project. These lists include the main
   development and support lists, among others. If the FAQ does not solve
   the problem you are having, the next step would be to search the
   mailing lists at [172]http://www.linuxfromscratch.org/search.html.

   For information on the different lists, how to subscribe, archive
   locations, and additional information, visit
   [173]http://www.linuxfromscratch.org/mail.html.

1.3.3. News Server

   The mailing lists hosted at linuxfromscratch.org are also accessible
   via the Network News Transfer Protocol (NNTP) server. All messages
   posted to a mailing list are copied to the corresponding newsgroup,
   and vice versa.

   The news server is located at news.linuxfromscratch.org.

1.3.4. IRC

   Several members of the LFS community offer assistance on our community
   Internet Relay Chat (IRC) network. Before using this support, please
   make sure that your question is not already answered in the LFS FAQ or
   the mailing list archives. You can find the IRC network at
   irc.linuxfromscratch.org. The support channel is named #LFS-support.

1.3.5. References

   For additional information on the packages, useful tips are available
   in the LFS Package Reference page located at
   [174]http://www.linuxfromscratch.org/~matthew/LFS-references.html.

1.3.6. Mirror Sites

   The LFS project has a number of world-wide mirrors to make accessing
   the website and downloading the required packages more convenient.
   Please visit the LFS website at
   [175]http://www.linuxfromscratch.org/mirrors.html for a list of
   current mirrors.

1.3.7. Contact Information

   Please direct all your questions and comments to one of the LFS
   mailing lists (see above).

1.4. Help

   If an issue or a question is encountered while working through this
   book, check the FAQ page at
   [176]http://www.linuxfromscratch.org/faq/#generalfaq. Questions are
   often already answered there. If your question is not answered on this
   page, try to find the source of the problem. The following hint will
   give you some guidance for troubleshooting:
   [177]http://www.linuxfromscratch.org/hints/downloads/files/errors.txt.

   If you cannot find your problem listed in the FAQ, search the mailing
   lists at [178]http://www.linuxfromscratch.org/search.html.

   We also have a wonderful LFS community that is willing to offer
   assistance through the mailing lists and IRC (see the
   [179]Section 1.3, "Resources" section of this book). However, we get
   several support questions everyday and many of them can be easily
   answered by going to the FAQ and by searching the mailing lists first.
   So for us to offer the best assistance possible, you need to do some
   research on your own first. That allows us to focus on the more
   unusual support needs. If your searches do not produce a solution,
   please include all relevant information (mentioned below) in your
   request for help.

1.4.1. Things to Mention

   Apart from a brief explanation of the problem being experienced, the
   essential things to include in any request for help are:
     * The version of the book being used (in this case 6.1.1)
     * The host distribution and version being used to create LFS
     * The package or section the problem was encountered in
     * The exact error message or symptom being received
     * Note whether you have deviated from the book at all

Note

   Deviating from this book does not mean that we will not help you.
   After all, LFS is about personal preference. Being upfront about any
   changes to the established procedure helps us evaluate and determine
   possible causes of your problem.

1.4.2. Configure Script Problems

   If something goes wrong while running the configure script, review the
   config.log file. This file may contain errors encountered during
   configure which were not printed to the screen. Include the relevant
   lines if you need to ask for help.

1.4.3. Compilation Problems

   Both the screen output and the contents of various files are useful in
   determining the cause of compilation problems. The screen output from
   the configure script and the make run can be helpful. It is not
   necessary to include the entire output, but do include enough of the
   relevant information. Below is an example of the type of information
   to include from the screen output from make:
gcc -DALIASPATH=\"/mnt/lfs/usr/share/locale:.\"
-DLOCALEDIR=\"/mnt/lfs/usr/share/locale\"
-DLIBDIR=\"/mnt/lfs/usr/lib\"
-DINCLUDEDIR=\"/mnt/lfs/usr/include\" -DHAVE_CONFIG_H -I. -I.
-g -O2 -c getopt1.c
gcc -g -O2 -static -o make ar.o arscan.o commands.o dir.o
expand.o file.o function.o getopt.o implicit.o job.o main.o
misc.o read.o remake.o rule.o signame.o variable.o vpath.o
default.o remote-stub.o version.o opt1.o
-lutil job.o: In function `load_too_high':
/lfs/tmp/make-3.79.1/job.c:1565: undefined reference
to `getloadavg'
collect2: ld returned 1 exit status
make[2]: *** [make] Error 1
make[2]: Leaving directory `/lfs/tmp/make-3.79.1'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/lfs/tmp/make-3.79.1'
make: *** [all-recursive-am] Error 2

   In this case, many people would just include the bottom section:
make [2]: *** [make] Error 1

   This is not enough information to properly diagnose the problem
   because it only notes that something went wrong, not what went wrong.
   The entire section, as in the example above, is what should be saved
   because it includes the command that was executed and the associated
   error message(s).

   An excellent article about asking for help on the Internet is
   available online at
   [180]http://catb.org/~esr/faqs/smart-questions.html. Read and follow
   the hints in this document to increase the likelihood of getting the
   help you need.

Part II. Preparing for the Build

Table of Contents

     * 2. Preparing a New Partition
          + [181]Introduction
          + [182]Creating a New Partition
          + [183]Creating a File System on the Partition
          + [184]Mounting the New Partition
     * 3. Packages and Patches
          + [185]Introduction
          + [186]All Packages
          + [187]Needed Patches
     * 4. Final Preparations
          + [188]About $LFS
          + [189]Creating the $LFS/tools Directory
          + [190]Adding the LFS User
          + [191]Setting Up the Environment
          + [192]About SBUs
          + [193]About the Test Suites
     * 5. Constructing a Temporary System
          + [194]Introduction
          + [195]Toolchain Technical Notes
          + [196]Binutils-2.15.94.0.2.2 - Pass 1
          + [197]GCC-3.4.3 - Pass 1
          + [198]Linux-Libc-Headers-2.6.11.2
          + [199]Glibc-2.3.4
          + [200]Adjusting the Toolchain
          + [201]Tcl-8.4.9
          + [202]Expect-5.43.0
          + [203]DejaGNU-1.4.4
          + [204]GCC-3.4.3 - Pass 2
          + [205]Binutils-2.15.94.0.2.2 - Pass 2
          + [206]Gawk-3.1.4
          + [207]Coreutils-5.2.1
          + [208]Bzip2-1.0.3
          + [209]Gzip-1.3.5
          + [210]Diffutils-2.8.1
          + [211]Findutils-4.2.23
          + [212]Make-3.80
          + [213]Grep-2.5.1a
          + [214]Sed-4.1.4
          + [215]Gettext-0.14.3
          + [216]Ncurses-5.4
          + [217]Patch-2.5.4
          + [218]Tar-1.15.1
          + [219]Texinfo-4.8
          + [220]Bash-3.0
          + [221]M4-1.4.3
          + [222]Bison-2.0
          + [223]Flex-2.5.31
          + [224]Util-linux-2.12q
          + [225]Perl-5.8.7
          + [226]Stripping

Chapter 2. Preparing a New Partition

2.1. Introduction

   In this chapter, the partition which will host the LFS system is
   prepared. We will create the partition itself, create a file system on
   it, and mount it.

2.2. Creating a New Partition

   Like most other operating systems, LFS is usually installed on a
   dedicated partition. The recommended approach to building an LFS
   system is to use an available empty partition or, if you have enough
   unpartitioned space, to create one. However, an LFS system (in fact
   even multiple LFS systems) may also be installed on a partition
   already occupied by another operating system and the different systems
   will co-exist peacefully. The document
   [227]http://www.linuxfromscratch.org/hints/downloads/files/lfs_next_to
   _existing_systems.txt explains how to implement this, whereas this
   book discusses the method of using a fresh partition for the
   installation.

   A minimal system requires a partition of around 1.3 gigabytes (GB).
   This is enough to store all the source tarballs and compile the
   packages. However, if the LFS system is intended to be the primary
   Linux system, additional software will probably be installed which
   will require additional space (2-3 GB). The LFS system itself will not
   take up this much room. A large portion of this requirement is to
   provide sufficient free temporary storage. Compiling packages can
   require a lot of disk space which will be reclaimed after the package
   is installed.

   Because there is not always enough Random Access Memory (RAM)
   available for compilation processes, it is a good idea to use a small
   disk partition as swap space. This is used by the kernel to store
   seldom-used data and leave more memory available for active processes.
   The swap partition for an LFS system can be the same as the one used
   by the host system, in which case it is not necessary to create
   another one.

   Start a disk partitioning program such as cfdisk or fdisk with a
   command line option naming the hard disk on which the new partition
   will be created--for example /dev/had for the primary Integrated Drive
   Electronics (IDE) disk. Create a Linux native partition and a swap
   partition, if needed. Please refer to cfdisk(8) or fdisk(8) if you do
   not yet know how to use the programs.

   Remember the designation of the new partition (e.g., hda5). This book
   will refer to this as the LFS partition. Also remember the designation
   of the swap partition. These names will be needed later for the
   /etc/fstab file.

2.3. Creating a File System on the Partition

   Now that a blank partition has been set up, the file system can be
   created. The most widely-used system in the Linux world is the second
   extended file system (ext2), but with newer high-capacity hard disks,
   journaling file systems are becoming increasingly popular. We will
   create an ext2 file system. Build instructions for other file systems
   can be found at
   [228]http://www.linuxfromscratch.org/blfs/view/svn/postlfs/filesystems
   .html.

   To create an ext2 file system on the LFS partition, run the following:
mke2fs -v /dev/[xxx]

   Replace [xxx] with the name of the LFS partition (hda5 in our previous
   example).

Note

   Some host distributions use custom features in their filesystem
   creation tools (e2fsprogs). This can cause problems when booting into
   your new LFS in Chapter 9, as those features will not be supported by
   the LFS-installed e2fsprogs; you will get an error similar to
   "unsupported filesystem features, upgrade your e2fsprogs". To check if
   your host system uses custom enhancements, run the following command:
debugfs -R feature /dev/[xxx]

   If the output contains features other than: dir_index; filetype;
   large_file; resize_inode or sparse_super then your host system may
   have custom enhancements. In that case, to avoid later problems, you
   should compile the stock e2fsprogs package and use the resulting
   binaries to re-create the filesystem on your LFS partition:
cd /tmp
tar -xjvf /path/to/sources/e2fsprogs-1.37.tar.bz2
cd e2fsprogs-1.37
mkdir -v build
cd build
../configure
make #note that we intentionally don't 'make install' here!
./misc/mke2fs -v /dev/[xxx]
cd /tmp
rm -rfv e2fsprogs-1.37

   If a swap partition was created, it will need to be initialized for
   use by issuing the command below. If you are using an existing swap
   partition, there is no need to format it.
mkswap -v /dev/[yyy]

   Replace [yyy] with the name of the swap partition.

2.4. Mounting the New Partition

   Now that a file system has been created, the partition needs to be
   made accessible. In order to do this, the partition needs to be
   mounted at a chosen mount point. For the purposes of this book, it is
   assumed that the file system is mounted under /mnt/lfs, but the
   directory choice is up to you.

   Choose a mount point and assign it to the LFS environment variable by
   running:
export LFS=/mnt/lfs

   Next, create the mount point and mount the LFS file system by running:
mkdir -pv $LFS
mount -v /dev/[xxx] $LFS

   Replace [xxx] with the designation of the LFS partition.

   If using multiple partitions for LFS (e.g., one for / and another for
   /usr), mount them using:
mkdir -pv $LFS
mount -v /dev/[xxx] $LFS
mkdir -v $LFS/usr
mount -v /dev/[yyy] $LFS/usr

   Replace [xxx] and [yyy] with the appropriate partition names.

   Ensure that this new partition is not mounted with permissions that
   are too restrictive (such as the nosuid, nodev, or noatime options).
   Run the mount command without any parameters to see what options are
   set for the mounted LFS partition. If nosuid, nodev, and/or noatime
   are set, the partition will need to be remounted.

   Now that there is an established place to work, it is time to download
   the packages.

Chapter 3. Packages and Patches

3.1. Introduction

   This chapter includes a list of packages that need to be downloaded
   for building a basic Linux system. The listed version numbers
   correspond to versions of the software that are known to work, and
   this book is based on their use. We highly recommend not using newer
   versions because the build commands for one version may not work with
   a newer version. The newest package versions may also have problems
   that require work-arounds. These work-arounds will be developed and
   stabilized in the development version of the book.

   Download locations may not always be accessible. If a download
   location has changed since this book was published, Google
   ([229]http://www.google.com/) provides a useful search engine for most
   packages. If this search is unsuccessful, try one of the alternative
   means of downloading discussed at
   [230]http://www.linuxfromscratch.org/lfs/packages.html.

   Downloaded packages and patches will need to be stored somewhere that
   is conveniently available throughout the entire build. A working
   directory is also required to unpack the sources and build them.
   $LFS/sources can be used both as the place to store the tarballs and
   patches and as a working directory. By using this directory, the
   required elements will be located on the LFS partition and will be
   available during all stages of the building process.

   To create this directory, execute, as user root, the following command
   before starting the download session:
mkdir -v $LFS/sources

   Make this directory writable and sticky. "Sticky" means that even if
   multiple users have write permission on a directory, only the owner of
   a file can delete the file within a sticky directory. The following
   command will enable the write and sticky modes:
chmod -v a+wt $LFS/sources

3.2. All Packages

   Download or otherwise obtain the following packages:

   Autoconf (2.59) - 908 kilobytes (KB):
          [231]http://ftp.gnu.org/gnu/autoconf/

   Automake (1.9.5) - 748 KB:
          [232]http://ftp.gnu.org/gnu/automake/

   Bash (3.0) - 1,824 KB:
          [233]http://ftp.gnu.org/gnu/bash/

   Bash Documentation (3.0) - 1,994 KB:
          [234]http://ftp.gnu.org/gnu/bash/

   Binutils (2.15.94.0.2.2) - 11,056 KB:
          [235]http://www.kernel.org/pub/linux/devel/binutils/

   Bison (2.0) - 916 KB:
          [236]http://ftp.gnu.org/gnu/bison/

   Bzip2 (1.0.3) - 596 KB:
          [237]http://www.bzip.org/

   Coreutils (5.2.1) - 4,184 KB:
          [238]http://ftp.gnu.org/gnu/coreutils/

   DejaGNU (1.4.4) - 852 KB:
          [239]http://ftp.gnu.org/gnu/dejagnu/

   Diffutils (2.8.1) - 648 KB:
          [240]http://ftp.gnu.org/gnu/diffutils/

   E2fsprogs (1.37) - 3,100 KB:
          [241]http://prdownloads.sourceforge.net/e2fsprogs/

   Expect (5.43.0) - 416 KB:
          [242]http://expect.nist.gov/src/

   File (4.13) - 324 KB:
          [243]ftp://ftp.gw.com/mirrors/pub/unix/file/

Note

          File (4.13) may no longer be available at the listed location.
          The site administrators of the master download location
          occasionally remove older versions when new ones are released.
          An alternative download location that may have the correct
          version available can also be found at:
          [244]http://www.linuxfromscratch.org/lfs/download.html#ftp.

   Findutils (4.2.23) - 784 KB:
          [245]http://ftp.gnu.org/gnu/findutils/

   Flex (2.5.31) - 672 KB:
          [246]http://prdownloads.sourceforge.net/lex/

   Gawk (3.1.4) - 1,696 KB:
          [247]http://ftp.gnu.org/gnu/gawk/

   GCC (3.4.3) - 26,816 KB:
          [248]http://ftp.gnu.org/gnu/gcc/

   Gettext (0.14.3) - 4,568 KB:
          [249]http://ftp.gnu.org/gnu/gettext/

   Glibc (2.3.4) - 12,924 KB:
          [250]http://ftp.gnu.org/gnu/glibc/

   Glibc-Linuxthreads (2.3.4) - 236 KB:
          [251]http://ftp.gnu.org/gnu/glibc/

   Grep (2.5.1a) - 520 KB:
          [252]http://ftp.gnu.org/gnu/grep/

   Groff (1.19.1) - 2,096 KB:
          [253]http://ftp.gnu.org/gnu/groff/

   GRUB (0.96) - 768 KB:
          [254]ftp://alpha.gnu.org/gnu/grub/

   Gzip (1.3.5) - 284 KB:
          [255]ftp://alpha.gnu.org/gnu/gzip/

   Hotplug (2004_09_23) - 40 KB:
          [256]http://www.kernel.org/pub/linux/utils/kernel/hotplug/

   Iana-Etc (1.04) - 176 KB:
          [257]http://www.sethwklein.net/projects/iana-etc/downloads/

   Inetutils (1.4.2) - 752 KB:
          [258]http://ftp.gnu.org/gnu/inetutils/

   IPRoute2 (2.6.11-050330) - 276 KB:
          [259]http://developer.osdl.org/dev/iproute2/download/

   Kbd (1.12) - 624 KB:
          [260]http://www.kernel.org/pub/linux/utils/kbd/

   Less (382) - 216 KB:
          [261]http://ftp.gnu.org/gnu/less/

   LFS-Bootscripts (3.2.1) - 32 KB:
          [262]http://downloads.linuxfromscratch.org/

   Libtool (1.5.14) - 1,604 KB:
          [263]http://ftp.gnu.org/gnu/libtool/

   Linux (2.6.11.12) - 35,792 KB:
          [264]http://www.kernel.org/pub/linux/kernel/v2.6/

   Linux-Libc-Headers (2.6.11.2) - 2,476 KB:
          [265]http://ep09.pld-linux.org/~mmazur/linux-libc-headers/

   M4 (1.4.3) - 304 KB:
          [266]http://ftp.gnu.org/gnu/m4/

   Make (3.80) - 904 KB:
          [267]http://ftp.gnu.org/gnu/make/

   Man (1.5p) - 208 KB:
          [268]http://www.kernel.org/pub/linux/utils/man/

   Man-pages (2.01) - 1,640 KB:
          [269]http://www.kernel.org/pub/linux/docs/manpages/

   Mktemp (1.5) - 68 KB:
          [270]ftp://ftp.mktemp.org/pub/mktemp/

   Module-Init-Tools (3.1) - 128 KB:
          [271]http://www.kernel.org/pub/linux/utils/kernel/module-init-t
          ools/

   Module-Init-Tools-Testsuite (3.1) - 34 KB:
          [272]http://www.kernel.org/pub/linux/utils/kernel/module-init-t
          ools/

   Ncurses (5.4) - 1,556 KB:
          [273]ftp://invisible-island.net/ncurses/

   Patch (2.5.4) - 156 KB:
          [274]http://ftp.gnu.org/gnu/patch/

   Perl (5.8.7) - 9,628 KB:
          [275]http://ftp.funet.fi/pub/CPAN/src/

   Procps (3.2.5) - 224 KB:
          [276]http://procps.sourceforge.net/

   Psmisc (21.6) - 188 KB:
          [277]http://prdownloads.sourceforge.net/psmisc/

   Readline (5.0) - 1,456 KB:
          [278]http://ftp.gnu.org/gnu/readline/

   Sed (4.1.4) - 632 KB:
          [279]http://ftp.gnu.org/gnu/sed/
