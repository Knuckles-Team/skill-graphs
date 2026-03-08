The Bzip2 package contains programs for compressing and decompressing files. Compressing text files with **bzip2** yields a much better compression percentage than with the traditional **gzip**.
**Approximate build time:** 0.1 SBU
**Required disk space:** 3.9 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Glibc, and Make
###  6.40.1. Installation of Bzip2
Apply a patch to install the documentation for this package:
```
`patch -Np1 -i ../bzip2-1.0.3-install_docs-1.patch`
```

The **bzgrep** command does not escape '|' and '&' in filenames passed to it. This allows arbitrary commands to be executed with the privileges of the user running **bzgrep**. Apply the following to address this:
```
`patch -Np1 -i ../bzip2-1.0.3-bzgrep_security-1.patch`
```

Prepare Bzip2 for compilation with:
```
`make -f Makefile-libbz2_so
make clean`
```

The _`-f`_ flag will cause Bzip2 to be built using a different `Makefile` file, in this case the `Makefile-libbz2_so` file, which creates a dynamic `libbz2.so` library and links the Bzip2 utilities against it.
Compile and test the package:
```
`make`
```

If reinstalling Bzip2, perform **`rm -vf /usr/bin/bz*`** first, otherwise the following **make install** will fail.
Install the programs:
```
`make install`
```

Install the shared **bzip2** binary into the `/bin` directory, make some necessary symbolic links, and clean up:
```
`cp -v bzip2-shared /bin/bzip2
cp -av libbz2.so* /lib
ln -sv ../../lib/libbz2.so.1.0 /usr/lib/libbz2.so
rm -v /usr/bin/{bunzip2,bzcat,bzip2}
ln -sv bzip2 /bin/bunzip2
ln -sv bzip2 /bin/bzcat`
```

###  6.40.2. Contents of Bzip2
**Installed programs:** bunzip2 (link to bzip2), bzcat (link to bzip2), bzcmp, bzdiff, bzegrep, bzfgrep, bzgrep, bzip2, bzip2recover, bzless, and bzmore
**Installed libraries:** libbz2.[a,so]
###  Short Descriptions
**bunzip2** |  Decompresses bzipped files
---|---
**bzcat** |  Decompresses to standard output
**bzcmp** |  Runs **cmp** on bzipped files
**bzdiff** |  Runs **diff** on bzipped files
**bzgrep** |  Runs **grep** on bzipped files
**bzegrep** |  Runs **egrep** on bzipped files
**bzfgrep** |  Runs **fgrep** on bzipped files
**bzip2** |  Compresses files using the Burrows-Wheeler block sorting text compression algorithm with Huffman coding; the compression rate is better than that achieved by more conventional compressors using “Lempel-Ziv” algorithms, like **gzip**
**bzip2recover** |  Tries to recover data from damaged bzipped files
**bzless** |  Runs **less** on bzipped files
**bzmore** |  Runs **more** on bzipped files
`libbz2*` |  The library implementing lossless, block-sorting data compression, using the Burrows-Wheeler algorithm
##  6.41. Diffutils-2.8.1
The Diffutils package contains programs that show the differences between files or directories.
**Approximate build time:** 0.1 SBU
**Required disk space:** 5.6 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Gettext, Glibc, Grep, Make, and Sed
###  6.41.1. Installation of Diffutils
Prepare Diffutils for compilation:
```
`./configure --prefix=/usr`
```

Compile the package:
```
`make`
```

This package does not come with a test suite.
Install the package:
```
`make install`
```

###  6.41.2. Contents of Diffutils
**Installed programs:** cmp, diff, diff3, and sdiff
###  Short Descriptions
**cmp** |  Compares two files and reports whether or in which bytes they differ
---|---
**diff** |  Compares two files or directories and reports which lines in the files differ
**diff3** |  Compares three files line by line
**sdiff** |  Merges two files and interactively outputs the results
##  6.42. Kbd-1.12
The Kbd package contains key-table files and keyboard utilities.
**Approximate build time:** 0.1 SBU
**Required disk space:** 11.8 MB
**Installation depends on:** Bash, Binutils, Bison, Coreutils, Diffutils, Flex, GCC, Gettext, Glibc, Grep, Gzip, M4, Make, and Sed
###  6.42.1. Installation of Kbd
Prepare Kbd for compilation:
```
`./configure`
```

Compile the package:
```
`make`
```

Install the package:
```
`make install`
```

###  6.42.2. Contents of Kbd
**Installed programs:** chvt, deallocvt, dumpkeys, fgconsole, getkeycodes, getunimap, kbd_mode, kbdrate, loadkeys, loadunimap, mapscrn, openvt, psfaddtable (link to psfxtable), psfgettable (link to psfxtable), psfstriptable (link to psfxtable), psfxtable, resizecons, setfont, setkeycodes, setleds, setlogcons, setmetamode, setvesablank, showconsolefont, showkey, unicode_start, and unicode_stop
###  Short Descriptions
**chvt** |  Changes the foreground virtual terminal
---|---
**deallocvt** |  Deallocates unused virtual terminals
**dumpkeys** |  Dumps the keyboard translation tables
**fgconsole** |  Prints the number of the active virtual terminal
**getkeycodes** |  Prints the kernel scancode-to-keycode mapping table
**getunimap** |  Prints the currently used unicode-to-font mapping table
**kbd_mode** |  Reports or sets the keyboard mode
**kbdrate** |  Sets the keyboard repeat and delay rates
**loadkeys** |  Loads the keyboard translation tables
**loadunimap** |  Loads the kernel unicode-to-font mapping table
**mapscrn** |  An obsolete program that used to load a user-defined output character mapping table into the console driver; this is now done by **setfont**
**openvt** |  Starts a program on a new virtual terminal (VT)
**psfaddtable** |  A link to **psfxtable**
**psfgettable** |  A link to **psfxtable**
**psfstriptable** |  A link to **psfxtable**
**psfxtable** |  Handle Unicode character tables for console fonts
**resizecons** |  Changes the kernel idea of the console size
**setfont** |  Changes the Enhanced Graphic Adapter (EGA) and Video Graphics Array (VGA) fonts on the console
**setkeycodes** |  Loads kernel scancode-to-keycode mapping table entries; this is useful if there are unusual keys on the keyboard
**setleds** |  Sets the keyboard flags and Light Emitting Diodes (LEDs)
**setlogcons** |  Sends kernel messages to the console
**setmetamode** |  Defines the keyboard meta-key handling
**setvesablank** |  Lets the user adjust the built-in hardware screensaver (a blank screen)
**showconsolefont** |  Shows the current EGA/VGA console screen font
**showkey** |  Reports the scancodes, keycodes, and ASCII codes of the keys pressed on the keyboard
**unicode_start** |  Puts the keyboard and console in UNICODE mode. Never use it on LFS, because applications are not configured to support UNICODE.
**unicode_stop** |  Reverts keyboard and console from UNICODE mode
##  6.43. E2fsprogs-1.37
The E2fsprogs package contains the utilities for handling the `ext2` file system. It also supports the `ext3` journaling file system.
**Approximate build time:** 0.6 SBU
**Required disk space:** 40.0 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, Gawk, GCC, Gettext, Glibc, Grep, Make, Sed, and Texinfo
###  6.43.1. Installation of E2fsprogs
Fix a compilation error in E2fsprogs' testsuite:
```
`sed -i -e 's/-DTEST/$(ALL_CFLAGS) &/' lib/e2p/Makefile.in`
```

It is recommended that E2fsprogs be built in a subdirectory of the source tree:
```
`mkdir -v build
cd build`
```

Prepare E2fsprogs for compilation:
```
`../configure --prefix=/usr --with-root-prefix="" \
    --enable-elf-shlibs --disable-evms`
```

The meaning of the configure options:

_`--with-root-prefix=""`_

Certain programs (such as the **e2fsck** program) are considered essential programs. When, for example, `/usr` is not mounted, these programs still need to be available. They belong in directories like `/lib` and `/sbin`. If this option is not passed to E2fsprogs' configure, the programs are installed into the `/usr` directory.

_`--enable-elf-shlibs`_

This creates the shared libraries which some programs in this package use.

_`--disable-evms`_

This disables the building of the Enterprise Volume Management System (EVMS) plugin. This plugin is not up-to-date with the latest EVMS internal interfaces and EVMS is not installed as part of a base LFS system, so the plugin is not required. See the EVMS website at
Compile the package:
```
`make`
```

To test the results, issue: **`make check`**.
Install the binaries and documentation:
```
`make install`
```

Install the shared libraries:
```
`make install-libs`
```

###  6.43.2. Contents of E2fsprogs
**Installed programs:** badblocks, blkid, chattr, compile_et, debugfs, dumpe2fs, e2fsck, e2image, e2label, findfs, fsck, fsck.ext2, fsck.ext3, logsave, lsattr, mk_cmds, mke2fs, mkfs.ext2, mkfs.ext3, mklost+found, resize2fs, tune2fs, and uuidgen.
**Installed libraries:** libblkid.[a,so], libcom_err.[a,so], libe2p.[a,so], libext2fs.[a,so], libss.[a,so], and libuuid.[a,so]
###  Short Descriptions
**badblocks** |  Searches a device (usually a disk partition) for bad blocks
---|---
**blkid** |  A command line utility to locate and print block device attributes
**chattr** |  Changes the attributes of files on an `ext2` file system; it also changes `ext3` file systems, the journaling version of `ext2` file systems
**compile_et** |  An error table compiler; it converts a table of error-code names and messages into a C source file suitable for use with the `com_err` library
**debugfs** |  A file system debugger; it can be used to examine and change the state of an `ext2` file system
**dumpe2fs** |  Prints the super block and blocks group information for the file system present on a given device
**e2fsck** |  Is used to check, and optionally repair `ext2` file systems and `ext3` file systems
**e2image** |  Is used to save critical `ext2` file system data to a file
**e2label** |  Displays or changes the file system label on the `ext2` file system present on a given device
**findfs** |  Finds a file system by label or Universally Unique Identifier (UUID)
**fsck** |  Is used to check, and optionally repair, file systems
**fsck.ext2** |  By default checks `ext2` file systems
**fsck.ext3** |  By default checks `ext3` file systems
**logsave** |  Saves the output of a command in a log file
**lsattr** |  Lists the attributes of files on a second extended file system
**mk_cmds** |  Converts a table of command names and help messages into a C source file suitable for use with the `libss` subsystem library
**mke2fs** |  Creates an ext2 or ext3 file system on the given device
**mkfs.ext2** |  By default creates `ext2` file systems
**mkfs.ext3** |  By default creates `ext3` file systems
**mklost+found** |  Used to create a `lost+found` directory on an `ext2` file system; it pre-allocates disk blocks to this directory to lighten the task of **e2fsck**
**resize2fs** |  Can be used to enlarge or shrink an `ext2` file system
**tune2fs** |  Adjusts tunable file system parameters on an `ext2` file system
**uuidgen** |  Creates new UUIDs. Each new UUID can reasonably be considered unique among all UUIDs created, on the local system and on other systems, in the past and in the future
`libblkid` |  Contains routines for device identification and token extraction
`libcom_err` |  The common error display routine
`libe2p` |  Used by **dumpe2fs** , **chattr** , and **lsattr**
`libext2fs` |  Contains routines to enable user-level programs to manipulate an `ext2` file system
`libss` |  Used by **debugfs**
`libuuid` |  Contains routines for generating unique identifiers for objects that may be accessible beyond the local system
##  6.44. Grep-2.5.1a
The Grep package contains programs for searching through files.
**Approximate build time:** 0.1 SBU
**Required disk space:** 4.5 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Gettext, Glibc, Make, Sed, and Texinfo
###  6.44.1. Installation of Grep
Prepare Grep for compilation:
```
`./configure --prefix=/usr --bindir=/bin`
```

Compile the package:
```
`make`
```

To test the results, issue: **`make check`**.
Install the package:
```
`make install`
```

###  6.44.2. Contents of Grep
**Installed programs:** egrep (link to grep), fgrep (link to grep), and grep
###  Short Descriptions
**egrep** |  Prints lines matching an extended regular expression
---|---
**fgrep** |  Prints lines matching a list of fixed strings
**grep** |  Prints lines matching a basic regular expression
##  6.45. GRUB-0.96
The GRUB package contains the GRand Unified Bootloader.
**Approximate build time:** 0.2 SBU
**Required disk space:** 10.0 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Glibc, Grep, Make, Ncurses, and Sed
###  6.45.1. Installation of GRUB
This package is known to have issues when its default optimization flags (including the _`-march`_ and _`-mcpu`_ options) are changed. If any environment variables that override default optimizations have been defined, such as `CFLAGS` and `CXXFLAGS`, unset them when building GRUB.
Prepare GRUB for compilation:
```
`./configure --prefix=/usr`
```

Compile the package:
```
`make`
```

To test the results, issue: **`make check`**.
Note that the test results will always show the error “ufs2_stage1_5 is too big.” This is due to a compiler issue, but can be ignored unless you plan to boot from an UFS partition. The partitions are normally only used by Sun workstations.
Install the package:
```
`make install
mkdir -v /boot/grub
cp -v /usr/lib/grub/i386-pc/stage{1,2} /boot/grub`
```

Replace `i386-pc` with whatever directory is appropriate for the hardware in use.
The `i386-pc` directory contains a number of `*stage1_5` files, different ones for different file systems. Review the files available and copy the appropriate ones to the `/boot/grub` directory. Most users will copy the `e2fs_stage1_5` and/or `reiserfs_stage1_5` files.
###  6.45.2. Contents of GRUB
**Installed programs:** grub, grub-install, grub-md5-crypt, grub-terminfo, and mbchk
###  Short Descriptions
**grub** |  The Grand Unified Bootloader's command shell
---|---
**grub-install** |  Installs GRUB on the given device
**grub-md5-crypt** |  Encrypts a password in MD5 format
**grub-terminfo** |  Generates a terminfo command from a terminfo name; it can be employed if an unknown terminal is being used
**mbchk** |  Checks the format of a multi-boot kernel
##  6.46. Gzip-1.3.5
The Gzip package contains programs for compressing and decompressing files.
**Approximate build time:** 0.1 SBU
**Required disk space:** 2.2 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Glibc, Grep, Make, and Sed
###  6.46.1. Installation of Gzip
Gzip has 2 known security vulnerabilities. The following patch addresses both of them:
```
`patch -Np1 -i ../gzip-1.3.5-security_fixes-1.patch`
```

Prepare Gzip for compilation:
```
`./configure --prefix=/usr`
```

The **gzexe** script has the location of the **gzip** binary hard-wired into it. Because the location of the binary is changed later, the following command ensures that the new location gets placed into the script:
```
`sed -i 's@"BINDIR"@/bin@g' gzexe.in`
```

Compile the package:
```
`make`
```

Install the package:
```
`make install`
```

Move the **gzip** program to the `/bin` directory and create some commonly used symlinks to it:
```
`mv -v /usr/bin/gzip /bin
rm -v /usr/bin/{gunzip,zcat}
ln -sv gzip /bin/gunzip
ln -sv gzip /bin/zcat
ln -sv gzip /bin/compress
ln -sv gunzip /bin/uncompress`
```

###  6.46.2. Contents of Gzip
**Installed programs:** compress (link to gzip), gunzip (link to gzip), gzexe, gzip, uncompress (link to gunzip), zcat (link to gzip), zcmp, zdiff, zegrep, zfgrep, zforce, zgrep, zless, zmore, and znew
###  Short Descriptions
**compress** |  Compresses and decompresses files
---|---
**gunzip** |  Decompresses gzipped files
**gzexe** |  Creates self-decompressing executable files
**gzip** |  Compresses the given files using Lempel-Ziv (LZ77) coding
**uncompress** |  Decompresses compressed files
**zcat** |  Decompresses the given gzipped files to standard output
**zcmp** |  Runs **cmp** on gzipped files
**zdiff** |  Runs **diff** on gzipped files
**zegrep** |  Runs **egrep** on gzipped files
**zfgrep** |  Runs **fgrep** on gzipped files
**zforce** |  Forces a `.gz` extension on all given files that are gzipped files, so that **gzip** will not compress them again; this can be useful when file names were truncated during a file transfer
**zgrep** |  Runs **grep** on gzipped files
**zless** |  Runs **less** on gzipped files
**zmore** |  Runs **more** on gzipped files
**znew** |  Re-compresses files from **compress** format to **gzip** format—`.Z` to `.gz`
##  6.47. Hotplug-2004_09_23
The Hotplug package contains scripts that react upon hotplug events generated by the kernel. Such events correspond to every change in the kernel state visible in the `sysfs` filesystem, e.g., the addition and removal of hardware. This package also detects existing hardware during boot and inserts the relevant modules into the running kernel.
**Approximate build time:** 0.01 SBU
**Required disk space:** 460 KB
**Installation depends on:** Bash, Coreutils, Find, Gawk, and Make
###  6.47.1. Installation of Hotplug
Install the Hotplug package:
```
`make install`
```

Copy a file that the “install” target omits.
```
`cp -v etc/hotplug/pnp.distmap /etc/hotplug`
```

Remove the init script that Hotplug installs since we are going to be using the script included in the LFS-Bootscripts package:
```
`rm -rfv /etc/init.d`
```

Network device hotplugging is not yet supported by the LFS-Bootscripts package. For that reason, remove the network hotplug agent:
```
`rm -fv /etc/hotplug/net.agent`
```

Create a directory for storing firmware that can be loaded by **hotplug** :
```
`mkdir -v /lib/firmware`
```

###  6.47.2. Contents of Hotplug
**Installed program:** hotplug
**Installed scripts:** /etc/hotplug/*.rc, /etc/hotplug/*.agent
**Installed files:** /etc/hotplug/hotplug.functions, /etc/hotplug/blacklist, /etc/hotplug/{pci,usb}, /etc/hotplug/usb.usermap, /etc/hotplug.d, and /var/log/hotplug/events
###  Short Descriptions
**hotplug** |  This script is called by default by the Linux kernel when something changes in its internal state (e.g., a new device is added or an existing device is removed)
---|---
**/etc/hotplug/*.rc** |  These scripts are used for cold plugging, i.e., detecting and acting upon hardware already present during system startup. They are called by the `hotplug` initscript included in the LFS-Bootscripts package. The ***.rc** scripts try to recover hotplug events that were lost during system boot because, for example, the root filesystem was not mounted by the kernel
**/etc/hotplug/*.agent** |  These scripts are called by **hotplug** in response to different types of hotplug events generated by the kernel. Their action is to insert corresponding kernel modules and call any user-provided scripts
`/etc/hotplug/blacklist` |  This file contains the list of modules that should never be inserted into the kernel by the Hotplug scripts
`/etc/hotplug/hotplug.functions` |  This file contains common functions used by other scripts in the Hotplug package
`/etc/hotplug/{pci,usb}` |  These directories contain user-written handlers for hotplug events
`/etc/hotplug/usb.usermap` |  This file contains rules that determine which user-defined handlers to call for each USB device, based on its vendor ID and other attributes
`/etc/hotplug.d` |  This directory contains programs (or symlinks to them) that are interested in receiving hotplug events. For example, Udev puts its symlink here during installation
`/lib/firmware` |  This directory contains the firmware for devices that need to have their firmware loaded before use
`/var/log/hotplug/events` |  This file contains all the events that **hotplug** has called since bootup
##  6.48. Man-1.5p
The Man package contains programs for finding and viewing man pages.
**Approximate build time:** 0.1 SBU
**Required disk space:** 2.9 MB
**Installation depends on:** Bash, Binutils, Coreutils, Gawk, GCC, Glibc, Grep, Make, and Sed
###  6.48.1. Installation of Man
Two adjustments need to be made to the sources of Man.
The first is a **sed** substitution to add the _`-R`_ switch to the `PAGER` variable so that escape sequences are properly handled by Less:
```
`sed -i 's@-is@&R@g' configure`
```

The second is also a **sed** substitution to comment out the “MANPATH /usr/man” line in the `man.conf` file to prevent redundant results when using programs such as **whatis** :
```
`sed -i 's@MANPATH./usr/man@#&@g' src/man.conf.in`
```

Prepare Man for compilation:
```
`./configure -confdir=/etc`
```

The meaning of the configure options:

_`-confdir=/etc`_

This tells the **man** program to look for the `man.conf` configuration file in the `/etc` directory.
Compile the package:
```
`make`
```

Install the package:
```
`make install`
```

###  Note
If you will be working on a terminal that does not support text attributes such as color and bold, you can disable Select Graphic Rendition (SGR) escape sequences by editing the `man.conf` file and adding the _`-c`_ option to the `NROFF` variable. If you use multiple terminal types for one computer it may be better to selectively add the `GROFF_NO_SGR` environment variable for the terminals that do not support SGR.
If the character set of the locale uses 8-bit characters, search for the line beginning with “NROFF” in `/etc/man.conf`, and verify that it matches the following:
```
              NROFF  /usr/bin/nroff -Tlatin1 -mandoc
```

Note that “latin1” should be used even if it is not the character set of the locale. The reason is that, according to the specification, **groff** has no means of typesetting characters outside International Organization for Standards (ISO) 8859-1 without some strange escape codes. When formatting man pages, **groff** thinks that they are in the ISO 8859-1 encoding and this _`-Tlatin1`_ switch tells **groff** to use the same encoding for output. Since **groff** does no recoding of input characters, the formatted result is really in the same encoding as input, and therefore it is usable as the input for a pager.
This does not solve the problem of a non-working **man2dvi** program for localized man pages in non-ISO 8859-1 locales. Also, it does not work with multibyte character sets. The first problem does not currently have a solution. The second issue is not of concern because the LFS installation does not support multibyte character sets.
Additional information with regards to the compression of man and info pages can be found in the BLFS book at
###  6.48.2. Contents of Man
**Installed programs:** apropos, makewhatis, man, man2dvi, man2html, and whatis
###  Short Descriptions
**apropos** |  Searches the **whatis** database and displays the short descriptions of system commands that contain a given string
---|---
**makewhatis** |  Builds the **whatis** database; it reads all the man pages in the `MANPATH` and writes the name and a short description in the **whatis** database for each page
**man** |  Formats and displays the requested on-line man page
**man2dvi** |  Converts a man page into dvi format
**man2html** |  Converts a man page into HTML
**whatis** |  Searches the **whatis** database and displays the short descriptions of system commands that contain the given keyword as a separate word
##  6.49. Make-3.80
The Make package contains a program for compiling packages.
**Approximate build time:** 0.2 SBU
**Required disk space:** 7.1 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Gettext, Glibc, Grep, and Sed
###  6.49.1. Installation of Make
Prepare Make for compilation:
```
`./configure --prefix=/usr`
```

Compile the package:
```
`make`
```

To test the results, issue: **`make check`**.
Install the package:
```
`make install`
```

###  6.49.2. Contents of Make
**Installed program:** make
###  Short Descriptions
**make** |  Automatically determines which pieces of a package need to be (re)compiled and then issues the relevant commands
---|---
##  6.50. Module-Init-Tools-3.1
The Module-Init-Tools package contains programs for handling kernel modules in Linux kernels greater than or equal to version 2.5.47.
**Approximate build time:** 0.1 SBU
**Required disk space:** 4.9 MB
**Installation depends on:** Bash, Binutils, Bison, Coreutils, Diffutils, Flex, GCC, Glibc, Grep, M4, Make, and Sed
###  6.50.1. Installation of Module-Init-Tools
Module-Init-Tools attempts to rewrite its `modprobe.conf` man page during the build process. This is unnecessary and also relies on **docbook2man** — which is not installed in LFS. Run the following command to avoid this:
```
`touch modprobe.conf.5`
```

If you wish to run the test suite for Module-Init-Tools, you will need to download the separate testsuite tarball. Issue the following commands to perform the tests (note that the **make distclean** command is required to clean up the source tree, as the source gets recompiled as part of the testing process):
```
`tar -xvf ../module-init-tools-testsuite-3.1.tar.bz2 --strip-path=1 &&
./configure &&
make check &&
make distclean`
```

Prepare Module-Init-Tools for compilation:
```
`./configure --prefix="" --enable-zlib`
```

The meaning of the configure options:
