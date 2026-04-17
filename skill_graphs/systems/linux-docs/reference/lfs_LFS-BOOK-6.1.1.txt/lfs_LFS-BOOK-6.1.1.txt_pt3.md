
   Shadow (4.0.9) - 1,084 KB:
          [280]ftp://ftp.pld.org.pl/software/shadow/

Note

          Shadow (4.0.9) may no longer be available at the listed
          location. The site administrators of the master download
          location occasionally remove older versions when new ones are
          released. An alternative download location that may have the
          correct version available cat also be found at:
          [281]http://www.linuxfromscratch.org/lfs/download.html#ftp.

   Sysklogd (1.4.1) - 72 KB:
          [282]http://www.infodrom.org/projects/sysklogd/download/

   Sysvinit (2.86) - 88 KB:
          [283]ftp://ftp.cistron.nl/pub/people/miquels/sysvinit/

   Tar (1.15.1) - 1,580 KB:
          [284]http://ftp.gnu.org/gnu/tar/

   Tcl (8.4.9) - 2,748 KB:
          [285]http://prdownloads.sourceforge.net/tcl/

   Texinfo (4.8) - 1,492 KB:
          [286]http://ftp.gnu.org/gnu/texinfo/

   Udev (056) - 476 KB:
          [287]http://www.kernel.org/pub/linux/utils/kernel/hotplug/

   Udev Rules Configuration - 5 KB:
          [288]http://downloads.linuxfromscratch.org/udev-config-4.rules

   Util-linux (2.12q) - 1,344 KB:
          [289]http://www.kernel.org/pub/linux/utils/util-linux/

   Vim (6.3) - 3,620 KB:
          [290]ftp://ftp.vim.org/pub/vim/unix/

   Vim (6.3) language files (optional) - 540 KB:
          [291]ftp://ftp.vim.org/pub/vim/extra/

   Zlib (1.2.3) - 415 KB:
          [292]http://www.zlib.net/

   Total size of these packages: 146 MB

3.3. Needed Patches

   In addition to the packages, several patches are also required. These
   patches correct any mistakes in the packages that should be fixed by
   the maintainer. The patches also make small modifications to make the
   packages easier to work with. The following patches will be needed to
   build an LFS system:

   Bash Avoid Wcontinued Patch - 1 KB:
          [293]http://www.linuxfromscratch.org/patches/lfs/6.1.1/bash-3.0
          -avoid_WCONTINUED-1.patch

   Bash Various Fixes - 23 KB:
          [294]http://www.linuxfromscratch.org/patches/lfs/6.1.1/bash-3.0
          -fixes-3.patch

   Binutils Build From Host Running Gcc4 Patch - 2 KB:
          [295]http://www.linuxfromscratch.org/patches/lfs/6.1.1/binutils
          -2.15.94.0.2.2-gcc4-1.patch

   Bzip2 Documentation Patch - 1 KB:
          [296]http://www.linuxfromscratch.org/patches/lfs/6.1.1/bzip2-1.
          0.3-install_docs-1.patch

   Bzip2 Bzgrep Security Fixes Patch - 1 KB:
          [297]http://www.linuxfromscratch.org/patches/lfs/6.1.1/bzip2-1.
          0.3-bzgrep_security-1.patch

   Coreutils Suppress Uptime, Kill, Su Patch - 15 KB:
          [298]http://www.linuxfromscratch.org/patches/lfs/6.1.1/coreutils
          s-5.2.1-suppress_uptime_kill_su-1.patch

   Coreutils Uname Patch - 4 KB:
          [299]http://www.linuxfromscratch.org/patches/lfs/6.1.1/coreutils
          s-5.2.1-uname-2.patch

   Expect Spawn Patch - 7 KB:
          [300]http://www.linuxfromscratch.org/patches/lfs/6.1.1/expect-5
          .43.0-spawn-1.patch

   Flex Brokenness Patch - 156 KB:
          [301]http://www.linuxfromscratch.org/patches/lfs/6.1.1/flex-2.5
          .31-debian_fixes-3.patch

   GCC Linkonce Patch - 12 KB:
          [302]http://www.linuxfromscratch.org/patches/lfs/6.1.1/gcc-3.4.
          3-linkonce-1.patch

   GCC No-Fixincludes Patch - 1 KB:
          [303]http://www.linuxfromscratch.org/patches/lfs/6.1.1/gcc-3.4.
          3-no_fixincludes-1.patch

   GCC Specs Patch - 14 KB:
          [304]http://www.linuxfromscratch.org/patches/lfs/6.1.1/gcc-3.4.
          3-specs-2.patch

   Glibc Rtld Search Dirs Patch - 1 KB:
          [305]http://www.linuxfromscratch.org/patches/lfs/6.1.1/glibc-2.
          3.4-rtld_search_dirs-1.patch

   Glibc Fix Testsuite Patch - 1 KB:
          [306]http://www.linuxfromscratch.org/patches/lfs/6.1.1/glibc-2.
          3.4-fix_test-1.patch

   Glibc TLS Assertion Patch - 6 KB:
          [307]http://www.linuxfromscratch.org/patches/lfs/6.1.1/glibc-2.
          3.4-tls_assert-1.patch

   Gzip Security Patch - 2 KB:
          [308]http://www.linuxfromscratch.org/patches/lfs/6.1.1/gzip-1.3
          .5-security_fixes-1.patch

   Inetutils Kernel Headers Patch - 1 KB:
          [309]http://www.linuxfromscratch.org/patches/lfs/6.1.1/inetutil
          s-1.4.2-kernel_headers-1.patch

   Inetutils No-Server-Man-Pages Patch - 4 KB:
          [310]http://www.linuxfromscratch.org/patches/lfs/6.1.1/inetutil
          s-1.4.2-no_server_man_pages-1.patch

   Mktemp Tempfile Patch - 3 KB:
          [311]http://www.linuxfromscratch.org/patches/lfs/6.1.1/mktemp-1
          .5-add_tempfile-2.patch

   Perl Libc Patch - 1 KB:
          [312]http://www.linuxfromscratch.org/patches/lfs/6.1.1/perl-5.8
          .7-libc-1.patch

   Readline Fixes Patch - 7 KB:
          [313]http://www.linuxfromscratch.org/patches/lfs/6.1.1/readline
          -5.0-fixes-1.patch

   Sysklogd Fixes Patch - 27 KB:
          [314]http://www.linuxfromscratch.org/patches/lfs/6.1.1/sysklogd
          -1.4.1-fixes-1.patch

   Tar Sparse Fix Patch - 1 KB:
          [315]http://www.linuxfromscratch.org/patches/lfs/6.1.1/tar-1.15
          .1-sparse_fix-1.patch

   Texinfo Tempfile Fix Patch - 2 KB:
          [316]http://www.linuxfromscratch.org/patches/lfs/6.1.1/texinfo-
          4.8-tempfile_fix-1.patch

   Util-linux Cramfs Patch - 3 KB:
          [317]http://www.linuxfromscratch.org/patches/lfs/6.1.1/util-lin
          ux-2.12q-cramfs-1.patch

   Util-linux Umount Patch - 1 KB:
          [318]http://www.linuxfromscratch.org/patches/lfs/6.1.1/util-lin
          ux-2.12q-umount_fix-1.patch

   Vim Security Patch - 8 KB:
          [319]http://www.linuxfromscratch.org/patches/lfs/6.1.1/vim-6.3-
          security_fix-2.patch

   In addition to the above required patches, there exist a number of
   optional patches created by the LFS community. These optional patches
   solve minor problems or enable functionality that is not enabled by
   default. Feel free to peruse the patches database located at
   [320]http://www.linuxfromscratch.org/patches/ and acquire any
   additional patches to suit the system needs.

Chapter 4. Final Preparations

4.1. About $LFS

   Throughout this book, the environment variable LFS will be used
   several times. It is paramount that this variable is always defined.
   It should be set to the mount point chosen for the LFS partition.
   Check that the LFS variable is set up properly with:
echo $LFS

   Make sure the output shows the path to the LFS partition's mount
   point, which is /mnt/lfs if the provided example was followed. If the
   output is incorrect, the variable can be set with:
export LFS=/mnt/lfs

   Having this variable set is beneficial in that commands such as mkdir
   $LFS/tools can be typed literally. The shell will automatically
   replace "$LFS" with "/mnt/lfs" (or whatever the variable was set to)
   when it processes the command line.

   Do not forget to check that $LFS is set whenever you leave and reenter
   the current working environment (as when doing a "su" to root or
   another user).

4.2. Creating the $LFS/tools Directory

   All programs compiled in [321]Chapter 5 will be installed under
   $LFS/tools to keep them separate from the programs compiled in
   [322]Chapter 6. The programs compiled here are temporary tools and
   will not be a part of the final LFS system. By keeping these programs
   in a separate directory, they can easily be discarded later after
   their use. This also prevents these programs from ending up in the
   host production directories (easy to do by accident in [323]Chapter
   5).

   Create the required directory by running the following as root:
mkdir -v $LFS/tools

   The next step is to create a /tools symlink on the host system. This
   will point to the newly-created directory on the LFS partition. Run
   this command as root as well:
ln -sv $LFS/tools /

Note

   The above command is correct. The ln command has a few syntactic
   variations, so be sure to check info coreutils ln and ln(1) before
   reporting what you may think is an error.

   The created symlink enables the toolchain to be compiled so that it
   always refers to /tools, meaning that the compiler, assembler, and
   linker will work both in this chapter (when we are still using some
   tools from the host) and in the next (when we are "chrooted" to the
   LFS partition).

4.3. Adding the LFS User

   When logged in as user root, making a single mistake can damage or
   destroy a system. Therefore, we recommend building the packages in
   this chapter as an unprivileged user. You could use your own user
   name, but to make it easier to set up a clean working environment,
   create a new user called lfs as a member of a new group (also named
   lfs) and use this user during the installation process. As root, issue
   the following commands to add the new user:
groupadd lfs
useradd -s /bin/bash -g lfs -m -k /dev/null lfs

   The meaning of the command line options:

   -s /bin/bash
          This makes bash the default shell for user lfs.

   -g lfs
          This option adds user lfs to group lfs.

   -m
          This creates a home directory for lfs.

   -k /dev/null
          This parameter prevents possible copying of files from a
          skeleton directory (default is /etc/skel) by changing the input
          location to the special null device.

   lfs
          This is the actual name for the created group and user.

   To log in as lfs (as opposed to switching to user lfs when logged in
   as root, which does not require the lfs user to have a password), give
   lfs a password:
passwd lfs

   Grant lfs full access to $LFS/tools by making lfs the directory owner:
chown -v lfs $LFS/tools

   If a separate working directory was created as suggested, give user
   lfs ownership of this directory:
chown -v lfs $LFS/sources

   Next, login as user lfs. This can be done via a virtual console,
   through a display manager, or with the following substitute user
   command:
su - lfs

   The "-" instructs su to start a login shell as opposed to a non-login
   shell. The difference between these two types of shells can be found
   in detail in bash(1) and info bash.

4.4. Setting Up the Environment

   Set up a good working environment by creating two new startup files
   for the bash shell. While logged in as user lfs, issue the following
   command to create a new .bash_profile:
cat > ~/.bash_profile << "EOF"
exec env -i HOME=$HOME TERM=$TERM PS1='\u:\w\$ ' /bin/bash
EOF

   When logged on as user lfs, the initial shell is usually a login shell
   which reads the /etc/profile of the host (probably containing some
   settings and environment variables) and then .bash_profile. The exec
   env -i.../bin/bash command in the .bash_profile file replaces the
   running shell with a new one with a completely empty environment,
   except for the HOME, TERM, and PS1 variables. This ensures that no
   unwanted and potentially hazardous environment variables from the host
   system leak into the build environment. The technique used here
   achieves the goal of ensuring a clean environment.

   The new instance of the shell is a non-login shell, which does not
   read the /etc/profile or .bash_profile files, but rather reads the
   .bashrc file instead. Create the .bashrc file now:
cat > ~/.bashrc << "EOF"
set +h
umask 022
LFS=/mnt/lfs
LC_ALL=POSIX
PATH=/tools/bin:/bin:/usr/bin
export LFS LC_ALL PATH
EOF

   The set +h command turns off bash's hash function. Hashing is
   ordinarily a useful feature--bash uses a hash table to remember the
   full path of executable files to avoid searching the PATH time and
   again to find the same executable. However, the new tools should be
   used as soon as they are installed. By switching off the hash
   function, the shell will always search the PATH when a program is to
   be run. As such, the shell will find the newly compiled tools in
   $LFS/tools as soon as they are available without remembering a
   previous version of the same program in a different location.

   Setting the user file-creation mask (umask) to 022 ensures that newly
   created files and directories are only writable by their owner, but
   are readable and executable by anyone (assuming default modes are used
   by the open(2) system call, new files will end up with permission mode
   644 and directories with mode 755).

   The LFS variable should be set to the chosen mount point.

   The LC_ALL variable controls the localization of certain programs,
   making their messages follow the conventions of a specified country.
   If the host system uses a version of Glibc older than 2.2.4, having
   LC_ALL set to something other than "POSIX" or "C" (during this
   chapter) may cause issues if you exit the chroot environment and wish
   to return later. Setting LC_ALL to "POSIX" or "C" (the two are
   equivalent) ensures that everything will work as expected in the
   chroot environment.

   By putting /tools/bin ahead of the standard PATH, all the programs
   installed in [324]Chapter 5 are picked up by the shell immediately
   after their installation. This, combined with turning off hashing,
   limits the risk that old programs are used from the host when the same
   programs are available in the chapter 5 environment.

   Finally, to have the environment fully prepared for building the
   temporary tools, source the just-created user profile:
source ~/.bash_profile

4.5. About SBUs

   Many people would like to know beforehand approximately how long it
   takes to compile and install each package. Because Linux From Scratch
   can be built on many different systems, it is impossible to provide
   accurate time estimates. The biggest package (Glibc) will take
   approximately 20 minutes on the fastest systems, but could take up to
   three days on slower systems! Instead of providing actual times, the
   Standard Build Unit (SBU) measure will be used instead.

   The SBU measure works as follows. The first package to be compiled
   from this book is Binutils in [325]Chapter 5. The time it takes to
   compile this package is what will be referred to as the Standard Build
   Unit or SBU. All other compile times will be expressed relative to
   this time.

   For example, consider a package whose compilation time is 4.5 SBUs.
   This means that if a system took 10 minutes to compile and install the
   first pass of Binutils, it will take approximately 45 minutes to build
   this example package. Fortunately, most build times are shorter than
   the one for Binutils.

   In general, SBUs are not entirely accurate because they depend on many
   factors, including the host system's version of GCC. Note that on
   Symmetric Multi-Processor (SMP)-based machines, SBUs are even less
   accurate. They are provided here to give an estimate of how long it
   might take to install a package, but the numbers can vary by as much
   as dozens of minutes in some cases.

   To view actual timings for a number of specific machines, we recommend
   The LinuxFromScratch SBU Home Page at
   [326]http://www.linuxfromscratch.org/~bdubbs/.

4.6. About the Test Suites

   Most packages provide a test suite. Running the test suite for a newly
   built package is a good idea because it can provide a "sanity check"
   indicating that everything compiled correctly. A test suite that
   passes its set of checks usually proves that the package is
   functioning as the developer intended. It does not, however, guarantee
   that the package is totally bug free.

   Some test suites are more important than others. For example, the test
   suites for the core toolchain packages--GCC, Binutils, and Glibc--are
   of the utmost importance due to their central role in a properly
   functioning system. The test suites for GCC and Glibc can take a very
   long time to complete, especially on slower hardware, but are strongly
   recommended.

Note

   Experience has shown that there is little to be gained from running
   the test suites in [327]Chapter 5. There can be no escaping the fact
   that the host system always exerts some influence on the tests in that
   chapter, often causing inexplicable failures. Because the tools built
   in [328]Chapter 5 are temporary and eventually discarded, we do not
   recommend running the test suites in [329]Chapter 5 for the average
   reader. The instructions for running those test suites are provided
   for the benefit of testers and developers, but they are strictly
   optional.

   A common issue with running the test suites for Binutils and GCC is
   running out of pseudo terminals (PTYs). This can result in a high
   number of failing tests. This may happen for several reasons, but the
   most likely cause is that the host system does not have the devpts
   file system set up correctly. This issue is discussed in greater
   detail in [330]Chapter 5.

   Sometimes package test suites will fail, but for reasons which the
   developers are aware of and have deemed non-critical. Consult the logs
   located at [331]http://www.linuxfromscratch.org/lfs/build-logs/6.1.1/
   to verify whether or not these failures are expected. This site is
   valid for all tests throughout this book.

Chapter 5. Constructing a Temporary System

5.1. Introduction

   This chapter shows how to compile and install a minimal Linux system.
   This system will contain just enough tools to start constructing the
   final LFS system in [332]Chapter 6 and allow a working environment
   with more user convenience than a minimum environment would.

   There are two steps in building this minimal system. The first step is
   to build a new and host-independent toolchain (compiler, assembler,
   linker, libraries, and a few useful utilities). The second step uses
   this toolchain to build the other essential tools.

   The files compiled in this chapter will be installed under the
   $LFS/tools directory to keep them separate from the files installed in
   the next chapter and the host production directories. Since the
   packages compiled here are temporary, we do not want them to pollute
   the soon-to-be LFS system.

Important

   Before issuing the build instructions for a package, the package
   should be unpacked as user lfs, and a cd into the created directory
   should be performed. The build instructions assume that the bash shell
   is in use.

   Several of the packages are patched before compilation, but only when
   the patch is needed to circumvent a problem. A patch is often needed
   in both this and the next chapter, but sometimes in only one or the
   other. Therefore, do not be concerned if instructions for a downloaded
   patch seem to be missing. Warning messages about offset or fuzz may
   also be encountered when applying a patch. Do not worry about these
   warnings, as the patch was still successfully applied.

   During the compilation of most packages, there will be several
   warnings that scroll by on the screen. These are normal and can safely
   be ignored. These warnings are as they appear--warnings about
   deprecated, but not invalid, use of the C or C++ syntax. C standards
   change fairly often, and some packages still use the older standard.
   This is not a problem, but does prompt the warning.

Important

   After installing each package, delete its source and build
   directories, unless specifically instructed otherwise. Deleting the
   sources prevents mis-configuration when the same package is
   reinstalled later. Only three of the packages need to retain the
   source and build directories in order for their contents to be used by
   later commands. Pay special attention to these reminders.

   Check one last time that the LFS environment variable is set up
   properly:
echo $LFS

   Make sure the output shows the path to the LFS partition's mount
   point, which is /mnt/lfs, using our example.

5.2. Toolchain Technical Notes

   This section explains some of the rationale and technical details
   behind the overall build method. It is not essential to immediately
   understand everything in this section. Most of this information will
   be clearer after performing an actual build. This section can be
   referred back to at any time during the process.

   The overall goal of [333]Chapter 5 is to provide a temporary
   environment that can be chrooted into and from which can be produced a
   clean, trouble-free build of the target LFS system in [334]Chapter 6.
   Along the way, we separate the new system from the host system as much
   as possible, and in doing so, build a self-contained and self-hosted
   toolchain. It should be noted that the build process has been designed
   to minimize the risks for new readers and provide maximum educational
   value at the same time.

Important

   Before continuing, be aware of the name of the working platform, often
   referred to as the target triplet. Many times, the target triplet will
   probably be i686-pc-linux-gnu. A simple way to determine the name of
   the target triplet is to run the config.guess script that comes with
   the source for many packages. Unpack the Binutils sources and run the
   script: ./config.guess and note the output.

   Also be aware of the name of the platform's dynamic linker, often
   referred to as the dynamic loader (not to be confused with the
   standard linker ld that is part of Binutils). The dynamic linker
   provided by Glibc finds and loads the shared libraries needed by a
   program, prepares the program to run, and then runs it. The name of
   the dynamic linker will usually be ld-linux.so.2. On platforms that
   are less prevalent, the name might be ld.so.1, and newer 64 bit
   platforms might be named something else entirely. The name of the
   platform's dynamic linker can be determined by looking in the /lib
   directory on the host system. A sure-fire way to determine the name is
   to inspect a random binary from the host system by running: readelf -l
   <name of binary> | grep interpreter and noting the output. The
   authoritative reference covering all platforms is in the
   shlib-versions file in the root of the Glibc source tree.

   Some key technical points of how the [335]Chapter 5 build method
   works:
     * The process is similar in principle to cross-compiling, whereby
       tools installed in the same prefix work in cooperation, and thus
       utilize a little GNU "magic"
     * Careful manipulation of the standard linker's library search path
       ensures programs are linked only against chosen libraries
     * Careful manipulation of gcc's specs file tells the compiler which
       target dynamic linker will be used

   Binutils is installed first because the configure runs of both GCC and
   Glibc perform various feature tests on the assembler and linker to
   determine which software features to enable or disable. This is more
   important than one might first realize. An incorrectly configured GCC
   or Glibc can result in a subtly broken toolchain, where the impact of
   such breakage might not show up until near the end of the build of an
   entire distribution. A test suite failure will usually highlight this
   error before too much additional work is performed.

   Binutils installs its assembler and linker in two locations,
   /tools/bin and /tools/$TARGET_TRIPLET/bin. The tools in one location
   are hard linked to the other. An important facet of the linker is its
   library search order. Detailed information can be obtained from ld by
   passing it the --verbose flag. For example, an ld --verbose | grep
   SEARCH will illustrate the current search paths and their order. It
   shows which files are linked by ld by compiling a dummy program and
   passing the --verbose switch to the linker. For example, gcc dummy.c
   -Wl,--verbose 2>&1 | grep succeeded will show all the files
   successfully opened during the linking.

   The next package installed is GCC. An example of what can be seen
   during its run of configure is:
checking what assembler to use...
        /tools/i686-pc-linux-gnu/bin/as
checking what linker to use... /tools/i686-pc-linux-gnu/bin/ld

   This is important for the reasons mentioned above. It also
   demonstrates that GCC's configure script does not search the PATH
   directories to find which tools to use. However, during the actual
   operation of gcc itself, the same search paths are not necessarily
   used. To find out which standard linker gcc will use, run: gcc
   -print-prog-name=ld.

   Detailed information can be obtained from gcc by passing it the -v
   command line option while compiling a dummy program. For example, gcc
   -v dummy.c will show detailed information about the preprocessor,
   compilation, and assembly stages, including gcc's included search
   paths and their order.

   The next package installed is Glibc. The most important considerations
   for building Glibc are the compiler, binary tools, and kernel headers.
   The compiler is generally not an issue since Glibc will always use the
   gcc found in a PATH directory. The binary tools and kernel headers can
   be a bit more complicated. Therefore, take no risks and use the
   available configure switches to enforce the correct selections. After
   the run of configure, check the contents of the config.make file in
   the glibc-build directory for all important details. Note the use of
   CC="gcc -B/tools/bin/" to control which binary tools are used and the
   use of the -nostdinc and -isystem flags to control the compiler's
