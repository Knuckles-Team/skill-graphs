
6.36.2. Contents of Automake

   Installed programs: acinstall, aclocal, aclocal-1.9.5, automake,
   automake-1.9.5, compile, config.guess, config.sub, depcomp,
   elisp-comp, install-sh, mdate-sh, missing, mkinstalldirs, py-compile,
   symlink-tree, and ylwrap

Short Descriptions

   acinstall

   A script that installs aclocal-style M4 files
   aclocal

   Generates aclocal.m4 files based on the contents of configure.in files
   aclocal-1.9.5

   A hard link to aclocal
   automake

   A tool for automatically generating Makefile.in files from Makefile.am
   files. To create all the Makefile.in files for a package, run this
   program in the top-level directory. By scanning the configure.in file,
   it automatically finds each appropriate Makefile.am file and generates
   the corresponding Makefile.in file
   automake-1.9.5

   A hard link to automake
   compile

   A wrapper for compilers
   config.guess

   A script that attempts to guess the canonical triplet for the given
   build, host, or target architecture
   config.sub

   A configuration validation subroutine script
   depcomp

   A script for compiling a program so that dependency information is
   generated in addition to the desired output
   elisp-comp

   Byte-compiles Emacs Lisp code
   install-sh

   A script that installs a program, script, or data file
   mdate-sh

   A script that prints the modification time of a file or directory
   missing

   A script acting as a common stub for missing GNU programs during an
   installation
   mkinstalldirs

   A script that creates a directory tree
   py-compile

   Compiles a Python program
   symlink-tree

   A script to create a symlink tree of a directory tree
   ylwrap

   A wrapper for lex and yacc

6.37. Bash-3.0

   The Bash package contains the Bourne-Again SHell.
   Approximate build time: 1.2 SBU
   Required disk space: 20.6 MB
   Installation depends on: Binutils, Coreutils, Diffutils, Gawk, GCC,
   Glibc, Grep, Make, Ncurses, and Sed.

6.37.1. Installation of Bash

   If you downloaded the Bash documentation tarball and wish to install
   HTML documentation, issue the following commands:
tar -xvf ../bash-doc-3.0.tar.gz &&
sed -i "s|htmldir = @htmldir@|htmldir = /usr/share/doc/bash-3.0|" \
    Makefile.in

   The following patch fixes various issues, including a problem where
   Bash will sometimes only show 33 characters on a line, then wrap to
   the next:
patch -Np1 -i ../bash-3.0-fixes-3.patch

   Bash also has issues when compiled against newer versions of Glibc.
   The following patch resolves this problem:
patch -Np1 -i ../bash-3.0-avoid_WCONTINUED-1.patch

   Prepare Bash for compilation:
./configure --prefix=/usr --bindir=/bin \
    --without-bash-malloc --with-installed-readline

   The meaning of the configure options:

   --with-installed-readline
          This option tells Bash to use the readline library that is
          already installed on the system rather than using its own
          readline version.

   Compile the package:
make

   To test the results, issue: make tests.

   Install the package:
make install

   Run the newly compiled bash program (replacing the one that is
   currently being executed):
exec /bin/bash --login +h

Note

   The parameters used make the bash process an interactive login shell
   and continue to disable hashing so that new programs are found as they
   become available.

6.37.2. Contents of Bash

   Installed programs: bash, bashbug, and sh (link to bash)

Short Descriptions

   bash

   A widely-used command interpreter; it performs many types of
   expansions and substitutions on a given command line before executing
   it, thus making this interpreter a powerful tool
   bashbug

   A shell script to help the user compose and mail standard formatted
   bug reports concerning bash
   sh

   A symlink to the bash program; when invoked as sh, bash tries to mimic
   the startup behavior of historical versions of sh as closely as
   possible, while conforming to the POSIX standard as well

6.38. File-4.13

   The File package contains a utility for determining the type of a
   given file or files.
   Approximate build time: 0.1 SBU
   Required disk space: 6.2 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, Grep, Make, Sed, and Zlib

6.38.1. Installation of File

   Prepare File for compilation:
./configure --prefix=/usr

   Compile the package:
make

   Install the package:
make install

6.38.2. Contents of File

   Installed programs: file
   Installed library: libmagic.[a,so]

Short Descriptions

   file

   Tries to classify each given file; it does this by performing several
   tests--file system tests, magic number tests, and language tests
   libmagic

   Contains routines for magic number recognition, used by the file
   program

6.39. Libtool-1.5.14

   The Libtool package contains the GNU generic library support script.
   It wraps the complexity of using shared libraries in a consistent,
   portable interface.
   Approximate build time: 1.5 SBU
   Required disk space: 19.7 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, Grep, Make, and Sed

6.39.1. Installation of Libtool

   Prepare Libtool for compilation:
./configure --prefix=/usr

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

6.39.2. Contents of Libtool

   Installed programs: libtool and libtoolize
   Installed libraries: libltdl.[a,so]

Short Descriptions

   libtool

   Provides generalized library-building support services
   libtoolize

   Provides a standard way to add libtool support to a package
   libltdl

   Hides the various difficulties of dlopening libraries

6.40. Bzip2-1.0.3

   The Bzip2 package contains programs for compressing and decompressing
   files. Compressing text files with bzip2 yields a much better
   compression percentage than with the traditional gzip.
   Approximate build time: 0.1 SBU
   Required disk space: 3.9 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, and Make

6.40.1. Installation of Bzip2

   Apply a patch to install the documentation for this package:
patch -Np1 -i ../bzip2-1.0.3-install_docs-1.patch

   The bzgrep command does not escape '|' and '&' in filenames passed to
   it. This allows arbitrary commands to be executed with the privileges
   of the user running bzgrep. Apply the following to address this:
patch -Np1 -i ../bzip2-1.0.3-bzgrep_security-1.patch

   Prepare Bzip2 for compilation with:
make -f Makefile-libbz2_so
make clean

   The -f flag will cause Bzip2 to be built using a different Makefile
   file, in this case the Makefile-libbz2_so file, which creates a
   dynamic libbz2.so library and links the Bzip2 utilities against it.

   Compile and test the package:
make

   If reinstalling Bzip2, perform rm -vf /usr/bin/bz* first, otherwise
   the following make install will fail.

   Install the programs:
make install

   Install the shared bzip2 binary into the /bin directory, make some
   necessary symbolic links, and clean up:
cp -v bzip2-shared /bin/bzip2
cp -av libbz2.so* /lib
ln -sv ../../lib/libbz2.so.1.0 /usr/lib/libbz2.so
rm -v /usr/bin/{bunzip2,bzcat,bzip2}
ln -sv bzip2 /bin/bunzip2
ln -sv bzip2 /bin/bzcat

6.40.2. Contents of Bzip2

   Installed programs: bunzip2 (link to bzip2), bzcat (link to bzip2),
   bzcmp, bzdiff, bzegrep, bzfgrep, bzgrep, bzip2, bzip2recover, bzless,
   and bzmore
   Installed libraries: libbz2.[a,so]

Short Descriptions

   bunzip2

   Decompresses bzipped files
   bzcat

   Decompresses to standard output
   bzcmp

   Runs cmp on bzipped files
   bzdiff

   Runs diff on bzipped files
   bzgrep

   Runs grep on bzipped files
   bzegrep

   Runs egrep on bzipped files
   bzfgrep

   Runs fgrep on bzipped files
   bzip2

   Compresses files using the Burrows-Wheeler block sorting text
   compression algorithm with Huffman coding; the compression rate is
   better than that achieved by more conventional compressors using
   "Lempel-Ziv" algorithms, like gzip
   bzip2recover

   Tries to recover data from damaged bzipped files
   bzless

   Runs less on bzipped files
   bzmore

   Runs more on bzipped files
   libbz2*

   The library implementing lossless, block-sorting data compression,
   using the Burrows-Wheeler algorithm

6.41. Diffutils-2.8.1

   The Diffutils package contains programs that show the differences
   between files or directories.
   Approximate build time: 0.1 SBU
   Required disk space: 5.6 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, and Sed

6.41.1. Installation of Diffutils

   Prepare Diffutils for compilation:
./configure --prefix=/usr

   Compile the package:
make

   This package does not come with a test suite.

   Install the package:
make install

6.41.2. Contents of Diffutils

   Installed programs: cmp, diff, diff3, and sdiff

Short Descriptions

   cmp

   Compares two files and reports whether or in which bytes they differ
   diff

   Compares two files or directories and reports which lines in the files
   differ
   diff3

   Compares three files line by line
   sdiff

   Merges two files and interactively outputs the results

6.42. Kbd-1.12

   The Kbd package contains key-table files and keyboard utilities.
   Approximate build time: 0.1 SBU
   Required disk space: 11.8 MB
   Installation depends on: Bash, Binutils, Bison, Coreutils, Diffutils,
   Flex, GCC, Gettext, Glibc, Grep, Gzip, M4, Make, and Sed

6.42.1. Installation of Kbd

   Prepare Kbd for compilation:
./configure

   Compile the package:
make

   Install the package:
make install

6.42.2. Contents of Kbd

   Installed programs: chvt, deallocvt, dumpkeys, fgconsole, getkeycodes,
   getunimap, kbd_mode, kbdrate, loadkeys, loadunimap, mapscrn, openvt,
   psfaddtable (link to psfxtable), psfgettable (link to psfxtable),
   psfstriptable (link to psfxtable), psfxtable, resizecons, setfont,
   setkeycodes, setleds, setlogcons, setmetamode, setvesablank,
   showconsolefont, showkey, unicode_start, and unicode_stop

Short Descriptions

   chvt

   Changes the foreground virtual terminal
   deallocvt

   Deallocates unused virtual terminals
   dumpkeys

   Dumps the keyboard translation tables
   fgconsole

   Prints the number of the active virtual terminal
   getkeycodes

   Prints the kernel scancode-to-keycode mapping table
   getunimap

   Prints the currently used unicode-to-font mapping table
   kbd_mode

   Reports or sets the keyboard mode
   kbdrate

   Sets the keyboard repeat and delay rates
   loadkeys

   Loads the keyboard translation tables
   loadunimap

   Loads the kernel unicode-to-font mapping table
   mapscrn

   An obsolete program that used to load a user-defined output character
   mapping table into the console driver; this is now done by setfont
   openvt

   Starts a program on a new virtual terminal (VT)
   psfaddtable

   A link to psfxtable
   psfgettable

   A link to psfxtable
   psfstriptable

   A link to psfxtable
   psfxtable

   Handle Unicode character tables for console fonts
   resizecons

   Changes the kernel idea of the console size
   setfont

   Changes the Enhanced Graphic Adapter (EGA) and Video Graphics Array
   (VGA) fonts on the console
   setkeycodes

   Loads kernel scancode-to-keycode mapping table entries; this is useful
   if there are unusual keys on the keyboard
   setleds

   Sets the keyboard flags and Light Emitting Diodes (LEDs)
   setlogcons

   Sends kernel messages to the console
   setmetamode

   Defines the keyboard meta-key handling
   setvesablank

   Lets the user adjust the built-in hardware screensaver (a blank
   screen)
   showconsolefont

   Shows the current EGA/VGA console screen font
   showkey

   Reports the scancodes, keycodes, and ASCII codes of the keys pressed
   on the keyboard
   unicode_start

   Puts the keyboard and console in UNICODE mode. Never use it on LFS,
   because applications are not configured to support UNICODE.
   unicode_stop

   Reverts keyboard and console from UNICODE mode

6.43. E2fsprogs-1.37

   The E2fsprogs package contains the utilities for handling the ext2
   file system. It also supports the ext3 journaling file system.
   Approximate build time: 0.6 SBU
   Required disk space: 40.0 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, Gawk,
   GCC, Gettext, Glibc, Grep, Make, Sed, and Texinfo

6.43.1. Installation of E2fsprogs

   Fix a compilation error in E2fsprogs' testsuite:
sed -i -e 's/-DTEST/$(ALL_CFLAGS) &/' lib/e2p/Makefile.in

   It is recommended that E2fsprogs be built in a subdirectory of the
   source tree:
mkdir -v build
cd build

   Prepare E2fsprogs for compilation:
../configure --prefix=/usr --with-root-prefix="" \
    --enable-elf-shlibs --disable-evms

   The meaning of the configure options:

   --with-root-prefix=""
          Certain programs (such as the e2fsck program) are considered
          essential programs. When, for example, /usr is not mounted,
          these programs still need to be available. They belong in
          directories like /lib and /sbin. If this option is not passed
          to E2fsprogs' configure, the programs are installed into the
          /usr directory.

   --enable-elf-shlibs
          This creates the shared libraries which some programs in this
          package use.

   --disable-evms
          This disables the building of the Enterprise Volume Management
          System (EVMS) plugin. This plugin is not up-to-date with the
          latest EVMS internal interfaces and EVMS is not installed as
          part of a base LFS system, so the plugin is not required. See
          the EVMS website at [478]http://evms.sourceforge.net/ for more
          information regarding EVMS.

   Compile the package:
make

   To test the results, issue: make check.

   Install the binaries and documentation:
make install

   Install the shared libraries:
make install-libs

6.43.2. Contents of E2fsprogs

   Installed programs: badblocks, blkid, chattr, compile_et, debugfs,
   dumpe2fs, e2fsck, e2image, e2label, findfs, fsck, fsck.ext2,
   fsck.ext3, logsave, lsattr, mk_cmds, mke2fs, mkfs.ext2, mkfs.ext3,
   mklost+found, resize2fs, tune2fs, and uuidgen.
   Installed libraries: libblkid.[a,so], libcom_err.[a,so],
   libe2p.[a,so], libext2fs.[a,so], libss.[a,so], and libuuid.[a,so]

Short Descriptions

   badblocks

   Searches a device (usually a disk partition) for bad blocks
   blkid

   A command line utility to locate and print block device attributes
   chattr

   Changes the attributes of files on an ext2 file system; it also
   changes ext3 file systems, the journaling version of ext2 file systems
   compile_et

   An error table compiler; it converts a table of error-code names and
   messages into a C source file suitable for use with the com_err
   library
   debugfs

   A file system debugger; it can be used to examine and change the state
   of an ext2 file system
   dumpe2fs

   Prints the super block and blocks group information for the file
   system present on a given device
   e2fsck

   Is used to check, and optionally repair ext2 file systems and ext3
   file systems
   e2image

   Is used to save critical ext2 file system data to a file
   e2label

   Displays or changes the file system label on the ext2 file system
   present on a given device
   findfs

   Finds a file system by label or Universally Unique Identifier (UUID)
   fsck

   Is used to check, and optionally repair, file systems
   fsck.ext2

   By default checks ext2 file systems
   fsck.ext3

   By default checks ext3 file systems
   logsave

   Saves the output of a command in a log file
   lsattr

   Lists the attributes of files on a second extended file system
   mk_cmds

   Converts a table of command names and help messages into a C source
   file suitable for use with the libss subsystem library
   mke2fs

   Creates an ext2 or ext3 file system on the given device
   mkfs.ext2

   By default creates ext2 file systems
   mkfs.ext3

   By default creates ext3 file systems
   mklost+found

   Used to create a lost+found directory on an ext2 file system; it
   pre-allocates disk blocks to this directory to lighten the task of
   e2fsck
   resize2fs

   Can be used to enlarge or shrink an ext2 file system
   tune2fs

   Adjusts tunable file system parameters on an ext2 file system
   uuidgen

   Creates new UUIDs. Each new UUID can reasonably be considered unique
   among all UUIDs created, on the local system and on other systems, in
   the past and in the future
   libblkid

   Contains routines for device identification and token extraction
   libcom_err

   The common error display routine
   libe2p

   Used by dumpe2fs, chattr, and lsattr
   libext2fs

   Contains routines to enable user-level programs to manipulate an ext2
   file system
   libss

   Used by debugfs
   libuuid

   Contains routines for generating unique identifiers for objects that
   may be accessible beyond the local system

6.44. Grep-2.5.1a

   The Grep package contains programs for searching through files.
   Approximate build time: 0.1 SBU
   Required disk space: 4.5 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Make, Sed, and Texinfo

6.44.1. Installation of Grep

   Prepare Grep for compilation:
./configure --prefix=/usr --bindir=/bin

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

6.44.2. Contents of Grep

   Installed programs: egrep (link to grep), fgrep (link to grep), and
   grep

Short Descriptions

   egrep

   Prints lines matching an extended regular expression
   fgrep

   Prints lines matching a list of fixed strings
   grep

   Prints lines matching a basic regular expression

6.45. GRUB-0.96

   The GRUB package contains the GRand Unified Bootloader.
   Approximate build time: 0.2 SBU
   Required disk space: 10.0 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, Grep, Make, Ncurses, and Sed

6.45.1. Installation of GRUB

   This package is known to have issues when its default optimization
   flags (including the -march and -mcpu options) are changed. If any
   environment variables that override default optimizations have been
   defined, such as CFLAGS and CXXFLAGS, unset them when building GRUB.

   Prepare GRUB for compilation:
./configure --prefix=/usr

   Compile the package:
make

   To test the results, issue: make check.

   Note that the test results will always show the error "ufs2_stage1_5
   is too big." This is due to a compiler issue, but can be ignored
   unless you plan to boot from an UFS partition. The partitions are
   normally only used by Sun workstations.

   Install the package:
make install
mkdir -v /boot/grub
cp -v /usr/lib/grub/i386-pc/stage{1,2} /boot/grub

   Replace i386-pc with whatever directory is appropriate for the
   hardware in use.

   The i386-pc directory contains a number of *stage1_5 files, different
   ones for different file systems. Review the files available and copy
   the appropriate ones to the /boot/grub directory. Most users will copy
   the e2fs_stage1_5 and/or reiserfs_stage1_5 files.

6.45.2. Contents of GRUB

   Installed programs: grub, grub-install, grub-md5-crypt, grub-terminfo,
   and mbchk

Short Descriptions

   grub

   The Grand Unified Bootloader's command shell
   grub-install

   Installs GRUB on the given device
   grub-md5-crypt

   Encrypts a password in MD5 format
   grub-terminfo

   Generates a terminfo command from a terminfo name; it can be employed
   if an unknown terminal is being used
   mbchk

   Checks the format of a multi-boot kernel

6.46. Gzip-1.3.5

   The Gzip package contains programs for compressing and decompressing
   files.
   Approximate build time: 0.1 SBU
   Required disk space: 2.2 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, Grep, Make, and Sed

6.46.1. Installation of Gzip

   Gzip has 2 known security vulnerabilities. The following patch
   addresses both of them:
patch -Np1 -i ../gzip-1.3.5-security_fixes-1.patch

   Prepare Gzip for compilation:
./configure --prefix=/usr

   The gzexe script has the location of the gzip binary hard-wired into
   it. Because the location of the binary is changed later, the following
   command ensures that the new location gets placed into the script:
sed -i 's@"BINDIR"@/bin@g' gzexe.in

   Compile the package:
make

   Install the package:
make install

   Move the gzip program to the /bin directory and create some commonly
   used symlinks to it:
mv -v /usr/bin/gzip /bin
rm -v /usr/bin/{gunzip,zcat}
ln -sv gzip /bin/gunzip
ln -sv gzip /bin/zcat
ln -sv gzip /bin/compress
ln -sv gunzip /bin/uncompress

6.46.2. Contents of Gzip

   Installed programs: compress (link to gzip), gunzip (link to gzip),
   gzexe, gzip, uncompress (link to gunzip), zcat (link to gzip), zcmp,
   zdiff, zegrep, zfgrep, zforce, zgrep, zless, zmore, and znew

Short Descriptions

   compress

   Compresses and decompresses files
   gunzip

   Decompresses gzipped files
   gzexe

   Creates self-decompressing executable files
   gzip

   Compresses the given files using Lempel-Ziv (LZ77) coding
   uncompress

   Decompresses compressed files
   zcat

   Decompresses the given gzipped files to standard output
   zcmp

   Runs cmp on gzipped files
   zdiff

   Runs diff on gzipped files
   zegrep

   Runs egrep on gzipped files
   zfgrep

   Runs fgrep on gzipped files
   zforce

   Forces a .gz extension on all given files that are gzipped files, so
   that gzip will not compress them again; this can be useful when file
   names were truncated during a file transfer
   zgrep

   Runs grep on gzipped files
   zless

   Runs less on gzipped files
   zmore

   Runs more on gzipped files
   znew

   Re-compresses files from compress format to gzip format--.Z to .gz

6.47. Hotplug-2004_09_23

   The Hotplug package contains scripts that react upon hotplug events
   generated by the kernel. Such events correspond to every change in the
   kernel state visible in the sysfs filesystem, e.g., the addition and
   removal of hardware. This package also detects existing hardware
   during boot and inserts the relevant modules into the running kernel.
   Approximate build time: 0.01 SBU
   Required disk space: 460 KB
   Installation depends on: Bash, Coreutils, Find, Gawk, and Make

6.47.1. Installation of Hotplug

   Install the Hotplug package:
make install

   Copy a file that the "install" target omits.
cp -v etc/hotplug/pnp.distmap /etc/hotplug

   Remove the init script that Hotplug installs since we are going to be
   using the script included in the LFS-Bootscripts package:
rm -rfv /etc/init.d

   Network device hotplugging is not yet supported by the LFS-Bootscripts
   package. For that reason, remove the network hotplug agent:
rm -fv /etc/hotplug/net.agent

   Create a directory for storing firmware that can be loaded by hotplug:
mkdir -v /lib/firmware

6.47.2. Contents of Hotplug

   Installed program: hotplug
   Installed scripts: /etc/hotplug/*.rc, /etc/hotplug/*.agent
   Installed files: /etc/hotplug/hotplug.functions,
   /etc/hotplug/blacklist, /etc/hotplug/{pci,usb},
   /etc/hotplug/usb.usermap, /etc/hotplug.d, and /var/log/hotplug/events

Short Descriptions

   hotplug

   This script is called by default by the Linux kernel when something
   changes in its internal state (e.g., a new device is added or an
   existing device is removed)
   /etc/hotplug/*.rc

   These scripts are used for cold plugging, i.e., detecting and acting
   upon hardware already present during system startup. They are called
   by the hotplug initscript included in the LFS-Bootscripts package. The
   *.rc scripts try to recover hotplug events that were lost during
   system boot because, for example, the root filesystem was not mounted
   by the kernel
   /etc/hotplug/*.agent

   These scripts are called by hotplug in response to different types of
   hotplug events generated by the kernel. Their action is to insert
   corresponding kernel modules and call any user-provided scripts
   /etc/hotplug/blacklist

   This file contains the list of modules that should never be inserted
   into the kernel by the Hotplug scripts
   /etc/hotplug/hotplug.functions

   This file contains common functions used by other scripts in the
   Hotplug package
   /etc/hotplug/{pci,usb}

   These directories contain user-written handlers for hotplug events
   /etc/hotplug/usb.usermap

   This file contains rules that determine which user-defined handlers to
   call for each USB device, based on its vendor ID and other attributes
   /etc/hotplug.d

   This directory contains programs (or symlinks to them) that are
   interested in receiving hotplug events. For example, Udev puts its
   symlink here during installation
   /lib/firmware

   This directory contains the firmware for devices that need to have
   their firmware loaded before use
   /var/log/hotplug/events
