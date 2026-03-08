cp -Rv lib/* /tools/lib/perl5/5.8.7

   Details on this package are located in [376]Section 6.33.2, "Contents
   of Perl."

5.33. Stripping

   The steps in this section are optional, but if the LFS partition is
   rather small, it is beneficial to learn that unnecessary items can be
   removed. The executables and libraries built so far contain about 130
   MB of unneeded debugging symbols. Remove those symbols with:
strip --strip-debug /tools/lib/*
strip --strip-unneeded /tools/{,s}bin/*

   The last of the above commands will skip some twenty files, reporting
   that it does not recognize their file format. Most of these are
   scripts instead of binaries.

   Take care not to use --strip-unneeded on the libraries. The static
   ones would be destroyed and the toolchain packages would need to be
   built all over again.

   To save another 30 MB, remove the documentation:
rm -rf /tools/{info,man}

   There will now be at least 850 MB of free space on the LFS file system
   that can be used to build and install Glibc in the next phase. If you
   can build and install Glibc, you can build and install the rest too.

Part III. Building the LFS System

Table of Contents

     * 6. Installing Basic System Software
          + [377]Introduction
          + [378]Mounting Virtual Kernel File Systems
          + [379]Entering the Chroot Environment
          + [380]Changing Ownership
          + [381]Creating Directories
          + [382]Creating Essential Symlinks
          + [383]Creating the passwd, group, and log Files
          + [384]Populating /dev
          + [385]Linux-Libc-Headers-2.6.11.2
          + [386]Man-pages-2.01
          + [387]Glibc-2.3.4
          + [388]Re-adjusting the Toolchain
          + [389]Binutils-2.15.94.0.2.2
          + [390]GCC-3.4.3
          + [391]Coreutils-5.2.1
          + [392]Zlib-1.2.3
          + [393]Mktemp-1.5
          + [394]Iana-Etc-1.04
          + [395]Findutils-4.2.23
          + [396]Gawk-3.1.4
          + [397]Ncurses-5.4
          + [398]Readline-5.0
          + [399]Vim-6.3
          + [400]M4-1.4.3
          + [401]Bison-2.0
          + [402]Less-382
          + [403]Groff-1.19.1
          + [404]Sed-4.1.4
          + [405]Flex-2.5.31
          + [406]Gettext-0.14.3
          + [407]Inetutils-1.4.2
          + [408]IPRoute2-2.6.11-050330
          + [409]Perl-5.8.7
          + [410]Texinfo-4.8
          + [411]Autoconf-2.59
          + [412]Automake-1.9.5
          + [413]Bash-3.0
          + [414]File-4.13
          + [415]Libtool-1.5.14
          + [416]Bzip2-1.0.3
          + [417]Diffutils-2.8.1
          + [418]Kbd-1.12
          + [419]E2fsprogs-1.37
          + [420]Grep-2.5.1a
          + [421]GRUB-0.96
          + [422]Gzip-1.3.5
          + [423]Hotplug-2004_09_23
          + [424]Man-1.5p
          + [425]Make-3.80
          + [426]Module-Init-Tools-3.1
          + [427]Patch-2.5.4
          + [428]Procps-3.2.5
          + [429]Psmisc-21.6
          + [430]Shadow-4.0.9
          + [431]Sysklogd-1.4.1
          + [432]Sysvinit-2.86
          + [433]Tar-1.15.1
          + [434]Udev-056
          + [435]Util-linux-2.12q
          + [436]About Debugging Symbols
          + [437]Stripping Again
          + [438]Cleaning Up
     * 7. Setting Up System Bootscripts
          + [439]Introduction
          + [440]LFS-Bootscripts-3.2.1
          + [441]How Do These Bootscripts Work?
          + [442]Device and Module Handling on an LFS System
          + [443]Configuring the setclock Script
          + [444]Configuring the Linux Console
          + [445]Configuring the sysklogd script
          + [446]Creating the /etc/inputrc File
          + [447]The Bash Shell Startup Files
          + [448]Configuring the localnet Script
          + [449]Creating the /etc/hosts File
          + [450]Configuring the network Script
     * 8. Making the LFS System Bootable
          + [451]Introduction
          + [452]Creating the /etc/fstab File
          + [453]Linux-2.6.11.12
          + [454]Making the LFS System Bootable
     * 9. The End
          + [455]The End
          + [456]Get Counted
          + [457]Rebooting the System
          + [458]What Now?

Chapter 6. Installing Basic System Software

6.1. Introduction

   In this chapter, we enter the building site and start constructing the
   LFS system in earnest. That is, we chroot into the temporary mini
   Linux system, make a few final preparations, and then begin installing
   the packages.

   The installation of this software is straightforward. Although in many
   cases the installation instructions could be made shorter and more
   generic, we have opted to provide the full instructions for every
   package to minimize the possibilities for mistakes. The key to
   learning what makes a Linux system work is to know what each package
   is used for and why the user (or the system) needs it. For every
   installed package, a summary of its contents is given, followed by
   concise descriptions of each program and library the package
   installed.

   If using the compiler optimizations provided in this chapter, please
   review the optimization hint at
   [459]http://www.linuxfromscratch.org/hints/downloads/files/optimizatio
   n.txt. Compiler optimizations can make a program run slightly faster,
   but they may also cause compilation difficulties and problems when
   running the program. If a package refuses to compile when using
   optimization, try to compile it without optimization and see if that
   fixes the problem. Even if the package does compile when using
   optimization, there is the risk it may have been compiled incorrectly
   because of the complex interactions between the code and build tools.
   The small potential gains achieved in using compiler optimizations are
   often outweighed by the risks. First-time builders of LFS are
   encouraged to build without custom optimizations. The subsequent
   system will still run very fast and be stable at the same time.

   The order that packages are installed in this chapter needs to be
   strictly followed to ensure that no program accidentally acquires a
   path referring to /tools hard-wired into it. For the same reason, do
   not compile packages in parallel. Compiling in parallel may save time
   (especially on dual-CPU machines), but it could result in a program
   containing a hard-wired path to /tools, which will cause the program
   to stop working when that directory is removed.

   Before the installation instructions, each installation page provides
   information about the package, including a concise description of what
   it contains, approximately how long it will take to build, how much
   disk space is required during this building process, and any other
   packages needed to successfully build the package. Following the
   installation instructions, there is a list of programs and libraries
   (along with brief descriptions of these) that the package installs.

   To keep track of which package installs particular files, a package
   manager can be used. For a general overview of different styles of
   package managers, please refer to
   [460]http://www.linuxfromscratch.org/blfs/view/svn/introduction/import
   ant.html. For a package management method specifically geared towards
   LFS, we recommend
   [461]http://www.linuxfromscratch.org/hints/downloads/files/more_contro
   l_and_pkg_man.txt.

Note

   The remainder of this book is to be performed while logged in as user
   root and no longer as user lfs. Also, double check that $LFS is set.

6.2. Mounting Virtual Kernel File Systems

   Various file systems exported by the kernel are used to communicate to
   and from the kernel itself. These file systems are virtual in that no
   disk space is used for them. The content of the file systems resides
   in memory.

   Begin by creating directories onto which the file systems will be
   mounted:
mkdir -pv $LFS/{proc,sys}

   Now mount the file systems:
mount -vt proc proc $LFS/proc
mount -vt sysfs sysfs $LFS/sys

   Remember that if for any reason you stop working on the LFS system and
   start again later, it is important to check that these file systems
   are mounted again before entering the chroot environment.

   Additional file systems will soon be mounted from within the chroot
   environment. To keep the host up to date, perform a "fake mount" for
   each of these now:
mount -vft tmpfs tmpfs $LFS/dev
mount -vft tmpfs tmpfs $LFS/dev/shm
mount -vft devpts -o gid=4,mode=620 devpts $LFS/dev/pts

6.3. Entering the Chroot Environment

   It is time to enter the chroot environment to begin building and
   installing the final LFS system. As user root, run the following
   command to enter the realm that is, at the moment, populated with only
   the temporary tools:
chroot "$LFS" /tools/bin/env -i \
    HOME=/root TERM="$TERM" PS1='\u:\w\$ ' \
    PATH=/bin:/usr/bin:/sbin:/usr/sbin:/tools/bin \
    /tools/bin/bash --login +h

   The -i option given to the env command will clear all variables of the
   chroot environment. After that, only the HOME, TERM, PS1, and PATH
   variables are set again. The TERM=$TERM construct will set the TERM
   variable inside chroot to the same value as outside chroot. This
   variable is needed for programs like vim and less to operate properly.
   If other variables are needed, such as CFLAGS or CXXFLAGS, this is a
   good place to set them again.

   From this point on, there is no need to use the LFS variable anymore,
   because all work will be restricted to the LFS file system. This is
   because the Bash shell is told that $LFS is now the root (/)
   directory.

   Notice that /tools/bin comes last in the PATH. This means that a
   temporary tool will no longer be used once its final version is
   installed. This occurs when the shell does not "remember" the
   locations of executed binaries--for this reason, hashing is switched
   off by passing the +h option to bash.

   It is important that all the commands throughout the remainder of this
   chapter and the following chapters are run from within the chroot
   environment. If you leave this environment for any reason (rebooting
   for example), remember to first mount the proc and devpts file systems
   (discussed in the previous section) and enter chroot again before
   continuing with the installations.

   Note that the bash prompt will say I have no name! This is normal
   because the /etc/passwd file has not been created yet.

6.4. Changing Ownership

   Currently, the /tools directory is owned by the user lfs, a user that
   exists only on the host system. Although the /tools directory can be
   deleted once the LFS system has been finished, it can be retained to
   build additional LFS systems. If the /tools directory is kept as is,
   the files are owned by a user ID without a corresponding account. This
   is dangerous because a user account created later could get this same
   user ID and would own the /tools directory and all the files therein,
   thus exposing these files to possible malicious manipulation.

   To avoid this issue, add the lfs user to the new LFS system later when
   creating the /etc/passwd file, taking care to assign it the same user
   and group IDs as on the host system. Alternatively, assign the
   contents of the /tools directory to user root by running the following
   command:
chown -R 0:0 /tools

   The command uses 0:0 instead of root:root, because chown is unable to
   resolve the name "root" until the password file has been created. This
   book assumes you ran this chown command.

6.5. Creating Directories

   It is time to create some structure in the LFS file system. Create a
   standard directory tree by issuing the following commands:
install -dv /{bin,boot,dev,etc/opt,home,lib,mnt}
install -dv /{sbin,srv,usr/local,var,opt}
install -dv /root -m 0750
install -dv /tmp /var/tmp -m 1777
install -dv /media/{floppy,cdrom}
install -dv /usr/{bin,include,lib,sbin,share,src}
ln -sv share/{man,doc,info} /usr
install -dv /usr/share/{doc,info,locale,man}
install -dv /usr/share/{misc,terminfo,zoneinfo}
install -dv /usr/share/man/man{1,2,3,4,5,6,7,8}
install -dv /usr/local/{bin,etc,include,lib,sbin,share,src}
ln -sv share/{man,doc,info} /usr/local
install -dv /usr/local/share/{doc,info,locale,man}
install -dv /usr/local/share/{misc,terminfo,zoneinfo}
install -dv /usr/local/share/man/man{1,2,3,4,5,6,7,8}
install -dv /var/{lock,log,mail,run,spool}
install -dv /var/{opt,cache,lib/{misc,locate},local}
install -dv /opt/{bin,doc,include,info}
install -dv /opt/{lib,man/man{1,2,3,4,5,6,7,8}}

   Directories are, by default, created with permission mode 755, but
   this is not desirable for all directories. In the commands above, two
   changes are made--one to the home directory of user root, and another
   to the directories for temporary files.

   The first mode change ensures that not just anybody can enter the
   /root directory--the same as a normal user would do with his or her
   home directory. The second mode change makes sure that any user can
   write to the /tmp and /var/tmp directories, but cannot remove another
   user's files from them. The latter is prohibited by the so-called
   "sticky bit," the highest bit (1) in the 1777 bit mask.

6.5.1. FHS Compliance Note

   The directory tree is based on the Filesystem Hierarchy Standard (FHS)
   (available at [462]http://www.pathname.com/fhs/). In addition to the
   tree created above, this standard stipulates the existence of
   /usr/local/games and /usr/share/games. The FHS is not precise as to
   the structure of the /usr/local/share subdirectory, so we create only
   the directories that are needed. However, feel free to create these
   directories if you prefer to conform more strictly to the FHS.

6.6. Creating Essential Symlinks

   Some programs use hard-wired paths to programs which do not exist yet.
   In order to satisfy these programs, create a number of symbolic links
   which will be replaced by real files throughout the course of this
   chapter after the software has been installed.
ln -sv /tools/bin/{bash,cat,pwd,stty} /bin
ln -sv /tools/bin/perl /usr/bin
ln -sv /tools/lib/libgcc_s.so{,.1} /usr/lib
ln -sv bash /bin/sh

6.7. Creating the passwd, group, and log Files

   In order for user root to be able to login and for the name "root" to
   be recognized, there must be relevant entries in the /etc/passwd and
   /etc/group files.

   Create the /etc/passwd file by running the following command:
cat > /etc/passwd << "EOF"
root:x:0:0:root:/root:/bin/bash
EOF

   The actual password for root (the "x" used here is just a placeholder)
   will be set later.

   Create the /etc/group file by running the following command:
cat > /etc/group << "EOF"
root:x:0:
bin:x:1:
sys:x:2:
kmem:x:3:
tty:x:4:
tape:x:5:
daemon:x:6:
floppy:x:7:
disk:x:8:
lp:x:9:
dialout:x:10:
audio:x:11:
video:x:12:
utmp:x:13:
usb:x:14:
cdrom:x:15:
EOF

   The created groups are not part of any standard--they are groups
   decided on in part by the requirements of the Udev configuration in
   this chapter, and in part by common convention employed by a number of
   existing Linux distributions. The Linux Standard Base (LSB, available
   at [463]http://www.linuxbase.org) recommends only that, besides the
   group "root" with a Group ID (GID) of 0, a group "bin" with a GID of 1
   be present. All other group names and GIDs can be chosen freely by the
   system administrator since well-written programs do not depend on GID
   numbers, but rather use the group's name.

   To remove the "I have no name!" prompt, start a new shell. Since a
   full Glibc was installed in [464]Chapter 5 and the /etc/passwd and
   /etc/group files have been created, user name and group name
   resolution will now work.
exec /tools/bin/bash --login +h

   Note the use of the +h directive. This tells bash not to use its
   internal path hashing. Without this directive, bash would remember the
   paths to binaries it has executed. To ensure the use of the newly
   compiled binaries as soon as they are installed, the +h directive will
   be used for the duration of this chapter.

   The login, agetty, and init programs (and others) use a number of log
   files to record information such as who was logged into the system and
   when. However, these programs will not write to the log files if they
   do not already exist. Initialize the log files and give them proper
   permissions:
touch /var/run/utmp /var/log/{btmp,lastlog,wtmp}
chgrp -v utmp /var/run/utmp /var/log/lastlog
chmod -v 664 /var/run/utmp /var/log/lastlog

   The /var/run/utmp file records the users that are currently logged in.
   The /var/log/wtmp file records all logins and logouts. The
   /var/log/lastlog file records when each user last logged in. The
   /var/log/btmp file records the bad login attempts.

6.8. Populating /dev

6.8.1. Creating Initial Device Nodes

   When the kernel boots the system, it requires the presence of a few
   device nodes, in particular the console and null devices. The device
   nodes will be created on the hard disk so that they are available
   before udev has been started, and additionally when Linux is started
   in single user mode (hence the restrictive permissions on console).
   Create the devices by running the following commands:
mknod -m 600 /dev/console c 5 1
mknod -m 666 /dev/null c 1 3

6.8.2. Mounting tmpfs and Populating /dev

   The recommended method of populating the /dev directory with devices
   is to mount a virtual filesystem (such as tmpfs) on the /dev
   directory, and allow the devices to be created dynamically on that
   virtual filesystem as they are detected or accessed. This is generally
   done during the boot process. Since this new system has not been
   booted, it is necessary to do what the LFS-Bootscripts package would
   otherwise do by mounting /dev:
mount -nvt tmpfs none /dev

   The Udev package is what actually creates the devices in the /dev
   directory. Since it will not be installed until later on in the
   process, manually create the minimal set of device nodes needed to
   complete the building of this system:
mknod -m 622 /dev/console c 5 1
mknod -m 666 /dev/null c 1 3
mknod -m 666 /dev/zero c 1 5
mknod -m 666 /dev/ptmx c 5 2
mknod -m 666 /dev/tty c 5 0
mknod -m 444 /dev/random c 1 8
mknod -m 444 /dev/urandom c 1 9
chown -v root:tty /dev/{console,ptmx,tty}

   There are some symlinks and directories required by LFS that are
   created during system startup by the LFS-Bootscripts package. Since
   this is a chroot environment and not a booted environment, those
   symlinks and directories need to be created here:
ln -sv /proc/self/fd /dev/fd
ln -sv /proc/self/fd/0 /dev/stdin
ln -sv /proc/self/fd/1 /dev/stdout
ln -sv /proc/self/fd/2 /dev/stderr
ln -sv /proc/kcore /dev/core
mkdir -v /dev/pts
mkdir -v /dev/shm

   Finally, mount the proper virtual (kernel) file systems on the
   newly-created directories:
mount -vt devpts -o gid=4,mode=620 none /dev/pts
mount -vt tmpfs none /dev/shm

   The mount commands executed above may result in the following warning
   message:
can't open /etc/fstab: No such file or directory.

   This file--/etc/fstab--has not been created yet but is also not
   required for the file systems to be properly mounted. As such, the
   warning can be safely ignored.

6.9. Linux-Libc-Headers-2.6.11.2

   The Linux-Libc-Headers package contains the "sanitized" kernel
   headers.
   Approximate build time: 0.1 SBU
   Required disk space: 26.9 MB
   Installation depends on: Coreutils

6.9.1. Installation of Linux-Libc-Headers

   For years it has been common practice to use "raw" kernel headers
   (straight from a kernel tarball) in /usr/include, but over the last
   few years, the kernel developers have taken a strong stance that this
   should not be done. This gave birth to the Linux-Libc-Headers Project,
   which was designed to maintain an API stable version of the Linux
   headers.

   Install the header files:
cp -Rv include/asm-i386 /usr/include/asm
cp -Rv include/linux /usr/include

   Ensure that all the headers are owned by root:
chown -Rv root:root /usr/include/{asm,linux}

   Make sure the users can read the headers:
find /usr/include/{asm,linux} -type d -exec chmod -v 755 {} \;
find /usr/include/{asm,linux} -type f -exec chmod -v 644 {} \;

6.9.2. Contents of Linux-Libc-Headers

   Installed headers: /usr/include/{asm,linux}/*.h

Short Descriptions

   /usr/include/{asm,linux}/*.h

   The Linux API headers

6.10. Man-pages-2.01

   The Man-pages package contains over 1,200 man pages.
   Approximate build time: 0.1 SBU
   Required disk space: 25.8 MB
   Installation depends on: Bash, Coreutils, and Make

6.10.1. Installation of Man-pages

   Install Man-pages by running:
make install

6.10.2. Contents of Man-pages

   Installed files: various man pages

Short Descriptions

   man pages

   Describe the C and C++ functions, important device files, and
   significant configuration files

6.11. Glibc-2.3.4

   The Glibc package contains the main C library. This library provides
   the basic routines for allocating memory, searching directories,
   opening and closing files, reading and writing files, string handling,
   pattern matching, arithmetic, and so on.
   Approximate build time: 12.3 SBU
   Required disk space: 476 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, Gawk,
   GCC, Gettext, Grep, Make, Perl, Sed, and Texinfo

6.11.1. Installation of Glibc

Note

   Some packages outside of LFS suggest installing GNU libiconv in order
   to translate data from one encoding to another. The project's home
   page ([465]http://www.gnu.org/software/libiconv/) says "This library
   provides an iconv() implementation, for use on systems which don't
   have one, or whose implementation cannot convert from/to Unicode. "
   Glibc provides an iconv() implementation and can convert from/to
   Unicode, therefore libiconv is not required on an LFS system.

   This package is known to have issues when its default optimization
   flags (including the -march and -mcpu options) are changed. If any
   environment variables that override default optimizations have been
   defined, such as CFLAGS and CXXFLAGS, unset them when building Glibc.

   The Glibc build system is self-contained and will install perfectly,
   even though the compiler specs file and linker are still pointing at
   /tools. The specs and linker cannot be adjusted before the Glibc
   install because the Glibc autoconf tests would give false results and
   defeat the goal of achieving a clean build.

   The linuxthreads tarball contains the man pages for the threading
   libraries installed by Glibc. Unpack the tarball from within the Glibc
   source directory:
tar -xjvf ../glibc-linuxthreads-2.3.4.tar.bz2

   In certain rare circumstances, Glibc can segfault when no standard
   search directories exist. The following patch prevents this:
patch -Np1 -i ../glibc-2.3.4-rtld_search_dirs-1.patch

   Glibc has two tests which fail when the running kernel is 2.6.11.x The
   problem has been determined to be with the tests themselves, not with
   the libc nor the kernel. This patch fixes the problem:
patch -Np1 -i ../glibc-2.3.4-fix_test-1.patch

   Apply the following patch to fix a bug in Glibc that can prevent some
   programs (including OpenOffice.org) from running:
patch -Np1 -i ../glibc-2.3.4-tls_assert-1.patch

   The Glibc documentation recommends building Glibc outside of the
   source directory in a dedicated build directory:
mkdir -v ../glibc-build
cd ../glibc-build

   Prepare Glibc for compilation:
../glibc-2.3.4/configure --prefix=/usr \
    --disable-profile --enable-add-ons \
    --enable-kernel=2.6.0 --libexecdir=/usr/lib/glibc

   The meaning of the new configure options:

   --libexecdir=/usr/lib/glibc
          This changes the location of the pt_chown program from its
          default of /usr/libexec to /usr/lib/glibc.

   Compile the package:
make

Important

   In this section, the test suite for Glibc is considered critical. Do
   not skip it under any circumstance.

   Test the results:
make -k check >glibc-check-log 2>&1
grep Error glibc-check-log

   The Glibc test suite is highly dependent on certain functions of the
   host system, in particular the kernel. In general, the Glibc test
   suite is always expected to pass. However, in certain circumstances,
   some failures are unavoidable. This is a list of the most common
   issues:
     * The math tests sometimes fail when running on systems where the
       CPU is not a relatively new genuine Intel or authentic AMD.
       Certain optimization settings are also known to be a factor here.
     * The gettext test sometimes fails due to host system issues. The
       exact reasons are not yet clear.
     * If you have mounted the LFS partition with the noatime option, the
       atime test will fail. As mentioned in [466]Section 2.4, "Mounting
       the New Partition", do not use the noatime option while building
       LFS.
     * When running on older and slower hardware, some tests can fail
       because of test timeouts being exceeded.

   Though it is a harmless message, the install stage of Glibc will
   complain about the absence of /etc/ld.so.conf. Prevent this warning
   with:
touch /etc/ld.so.conf

   Install the package:
make install

   The locales that can make the system respond in a different language
   were not installed by the above command. Install this with:
make localedata/install-locales
