   include search path. These items highlight an important aspect of the
   Glibc package--it is very self-sufficient in terms of its build
   machinery and generally does not rely on toolchain defaults.

   After the Glibc installation, make some adjustments to ensure that
   searching and linking take place only within the /tools prefix.
   Install an adjusted ld, which has a hard-wired search path limited to
   /tools/lib. Then amend gcc's specs file to point to the new dynamic
   linker in /tools/lib. This last step is vital to the whole process. As
   mentioned above, a hard-wired path to a dynamic linker is embedded
   into every Executable and Link Format (ELF)-shared executable. This
   can be inspected by running: readelf -l <name of binary> | grep
   interpreter. Amending gcc's specs file ensures that every program
   compiled from here through the end of this chapter will use the new
   dynamic linker in /tools/lib.

   The need to use the new dynamic linker is also the reason why the
   Specs patch is applied for the second pass of GCC. Failure to do so
   will result in the GCC programs themselves having the name of the
   dynamic linker from the host system's /lib directory embedded into
   them, which would defeat the goal of getting away from the host.

   During the second pass of Binutils, we are able to utilize the
   --with-lib-path configure switch to control ld's library search path.
   From this point onwards, the core toolchain is self-contained and
   self-hosted. The remainder of the [336]Chapter 5 packages all build
   against the new Glibc in /tools.

   Upon entering the chroot environment in [337]Chapter 6, the first
   major package to be installed is Glibc, due to its self-sufficient
   nature mentioned above. Once this Glibc is installed into /usr,
   perform a quick changeover of the toolchain defaults, then proceed in
   building the rest of the target LFS system.

5.3. Binutils-2.15.94.0.2.2 - Pass 1

   The Binutils package contains a linker, an assembler, and other tools
   for handling object files.
   Approximate build time: 1.0 SBU
   Required disk space: 179 MB
   Installation depends on: Bash, Bison, Coreutils, Diffutils, Flex, GCC,
   Gettext, Glibc, Grep, M4, Make, Perl, Sed, and Texinfo

5.3.1. Installation of Binutils

   It is important that Binutils be the first package compiled because
   both Glibc and GCC perform various tests on the available linker and
   assembler to determine which of their own features to enable.

   This package is known to have issues when its default optimization
   flags (including the -march and -mcpu options) are changed. If any
   environment variables that override default optimizations have been
   defined, such as CFLAGS and CXXFLAGS, unset them when building
   Binutils.

   If you are building from a host running Gcc-4 or later, it is
   necessary to patch the first build of this version of Binutils so that
   it can be compiled by the host system.
patch -Np1 -i ../binutils-2.15.94.0.2.2-gcc4-1.patch

   The Binutils documentation recommends building Binutils outside of the
   source directory in a dedicated build directory:
mkdir -v ../binutils-build
cd ../binutils-build

Note

   In order for the SBU values listed in the rest of the book to be of
   any use, measure the time it takes to build this package from the
   configuration, up to and including the first install. To achieve this
   easily, wrap the three commands in a time command like this: time {
   ./configure ... && make && make install; }.

   Now prepare Binutils for compilation:
../binutils-2.15.94.0.2.2/configure --prefix=/tools --disable-nls

   The meaning of the configure options:

   --prefix=/tools
          This tells the configure script to prepare to install the
          Binutils programs in the /tools directory.

   --disable-nls
          This disables internationalization as i18n is not needed for
          the temporary tools.

   Continue with compiling the package:
make

   Compilation is now complete. Ordinarily we would now run the test
   suite, but at this early stage the test suite framework (Tcl, Expect,
   and DejaGNU) is not yet in place. The benefits of running the tests at
   this point are minimal since the programs from this first pass will
   soon be replaced by those from the second.

   Install the package:
make install

   Next, prepare the linker for the "Adjusting" phase later on:
make -C ld clean
make -C ld LIB_PATH=/tools/lib

   The meaning of the make parameters:

   -C ld clean
          This tells the make program to remove all compiled files in the
          ld subdirectory.

   -C ld LIB_PATH=/tools/lib
          This option rebuilds everything in the ld subdirectory.
          Specifying the LIB_PATH Makefile variable on the command line
          allows us to override the default value and point it to the
          temporary tools location. The value of this variable specifies
          the linker's default library search path. This preparation is
          used later in the chapter.

Warning

   Do not remove the Binutils build and source directories yet. These
   will be needed again in their current state later in this chapter.

   Details on this package are located in [338]Section 6.13.2, "Contents
   of Binutils."

5.4. GCC-3.4.3 - Pass 1

   The GCC package contains the GNU compiler collection, which includes
   the C and C++ compilers.
   Approximate build time: 4.4 SBU
   Required disk space: 219 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils,
   Findutils, Gawk, Gettext, Glibc, Grep, Make, Perl, Sed, and Texinfo

5.4.1. Installation of GCC

   This package is known to have issues when its default optimization
   flags (including the -march and -mcpu options) are changed. If any
   environment variables that override default optimizations have been
   defined, such as CFLAGS and CXXFLAGS, unset them when building GCC.

   The GCC documentation recommends building GCC outside of the source
   directory in a dedicated build directory:
mkdir -v ../gcc-build
cd ../gcc-build

   Prepare GCC for compilation:
../gcc-3.4.3/configure --prefix=/tools \
    --libexecdir=/tools/lib --with-local-prefix=/tools \
    --disable-nls --enable-shared --enable-languages=c

   The meaning of the configure options:

   --with-local-prefix=/tools
          The purpose of this switch is to remove /usr/local/include from
          gcc's include search path. This is not absolutely essential,
          however, it helps to minimize the influence of the host system.

   --enable-shared
          This switch allows the building of libgcc_s.so.1 and
          libgcc_eh.a. Having libgcc_eh.a available ensures that the
          configure script for Glibc (the next package we compile)
          produces the proper results.

   --enable-languages=c
          This option ensures that only the C compiler is built.

   Continue with compiling the package:
make bootstrap

   The meaning of the make parameters:

   bootstrap
          This target does not just compile GCC, but compiles it several
          times. It uses the programs compiled in a first round to
          compile itself a second time, and then again a third time. It
          then compares these second and third compiles to make sure it
          can reproduce itself flawlessly. This also implies that it was
          compiled correctly.

   Compilation is now complete. At this point, the test suite would
   normally be run, but, as mentioned before, the test suite framework is
   not in place yet. The benefits of running the tests at this point are
   minimal since the programs from this first pass will soon be replaced.

   Install the package:
make install

   As a finishing touch, create a symlink. Many programs and scripts run
   cc instead of gcc, which is used to keep programs generic and
   therefore usable on all kinds of UNIX systems where the GNU C compiler
   is not always installed. Running cc leaves the system administrator
   free to decide which C compiler to install.
ln -vs gcc /tools/bin/cc

   Details on this package are located in [339]Section 6.14.2, "Contents
   of GCC."

5.5. Linux-Libc-Headers-2.6.11.2

   The Linux-Libc-Headers package contains the "sanitized" kernel
   headers.
   Approximate build time: 0.1 SBU
   Required disk space: 26.9 MB
   Installation depends on: Coreutils

5.5.1. Installation of Linux-Libc-Headers

   For years it has been common practice to use "raw" kernel headers
   (straight from a kernel tarball) in /usr/include, but over the last
   few years, the kernel developers have taken a strong stance that this
   should not be done. This gave birth to the Linux-Libc-Headers Project,
   which was designed to maintain an Application Programming Interface
   (API) stable version of the Linux headers.

   Install the header files:
cp -Rv include/asm-i386 /tools/include/asm
cp -Rv include/linux /tools/include

   If your architecture is not i386 (compatible), adjust the first
   command accordingly.

   Details on this package are located in [340]Section 6.9.2, "Contents
   of Linux-Libc-Headers."

5.6. Glibc-2.3.4

   The Glibc package contains the main C library. This library provides
   the basic routines for allocating memory, searching directories,
   opening and closing files, reading and writing files, string handling,
   pattern matching, arithmetic, and so on.
   Approximate build time: 11.8 SBU
   Required disk space: 454 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, Gawk,
   GCC, Gettext, Grep, Make, Perl, Sed, and Texinfo

5.6.1. Installation of Glibc

   This package is known to have issues when its default optimization
   flags (including the -march and -mcpu options) are changed. If any
   environment variables that override default optimizations have been
   defined, such as CFLAGS and CXXFLAGS, unset them when building Glibc.

   It should be noted that compiling Glibc in any way other than the
   method suggested in this book puts the stability of the system at
   risk.

   Glibc has two tests which fail when the running kernel is 2.6.11 or
   later. The problem has been determined to be with the tests
   themselves, not with the C library or the kernel. If you plan to run
   the testsuite apply this patch:
patch -Np1 -i ../glibc-2.3.4-fix_test-1.patch

   The Glibc documentation recommends building Glibc outside of the
   source directory in a dedicated build directory:
mkdir -v ../glibc-build
cd ../glibc-build

   Next, prepare Glibc for compilation:
../glibc-2.3.4/configure --prefix=/tools \
    --disable-profile --enable-add-ons \
    --enable-kernel=2.6.0 --with-binutils=/tools/bin \
    --without-gd --with-headers=/tools/include \
    --without-selinux

   The meaning of the configure options:

   --disable-profile
          This builds the libraries without profiling information. Omit
          this option if profiling on the temporary tools is necessary.

   --enable-add-ons
          This tells Glibc to use the NPTL add-on as its threading
          library.

   --enable-kernel=2.6.0
          This tells Glibc to compile the library with support for 2.6.x
          Linux kernels.

   --with-binutils=/tools/bin
          While not required, this switch ensures that there are no
          errors pertaining to which Binutils programs get used during
          the Glibc build.

   --without-gd
          This prevents the build of the memusagestat program, which
          insists on linking against the host's libraries (libgd, libpng,
          libz, etc.).

   --with-headers=/tools/include
          This tells Glibc to compile itself against the headers recently
          installed to the tools directory, so that it knows exactly what
          features the kernel has and can optimize itself accordingly.

   --without-selinux
          When building from hosts that include SELinux functionality
          (e.g. Fedora Core 3), Glibc will build with support for
          SELinux. As the LFS tools environment does not contain support
          for SELinux, a Glibc compiled with such support will fail to
          operate correctly.

   During this stage the following warning might appear:

configure: WARNING:
*** These auxiliary programs are missing or
*** incompatible versions: msgfmt
*** some features will be disabled.
*** Check the INSTALL file for required versions.

   The missing or incompatible msgfmt program is generally harmless, but
   it can sometimes cause issues when running the test suite. This msgfmt
   program is part of the Gettext package which the host distribution
   should provide. If msgfmt is present but deemed incompatible, upgrade
   the host system's Gettext package or continue without it and see if
   the test suite runs without problems regardless.

   Compile the package:
make

   Compilation is now complete. As mentioned earlier, running the test
   suites for the temporary tools installed in this chapter is not
   mandatory. To run the Glibc test suite (if desired), the following
   command will do so:
make check

   For a discussion of test failures that are of particular importance,
   please see [341]Section 6.11, "Glibc-2.3.4."

   In this chapter, some tests can be adversely affected by existing
   tools or environmental issues on the host system. Glibc test suite
   failures in this chapter are typically not worrisome. The Glibc
   installed in [342]Chapter 6 is the one that will ultimately end up
   being used, so that is the one that needs to pass most tests (even in
   [343]Chapter 6, some failures could still occur, for example, with the
   math tests).

   When experiencing a failure, make a note of it, then continue by
   reissuing the make check command. The test suite should pick up where
   it left off and continue. This stop-start sequence can be circumvented
   by issuing a make -k check command. If using this option, be sure to
   log the output so that the log file can be examined for failures
   later.

   The install stage of Glibc will issue a harmless warning at the end
   about the absence of /tools/etc/ld.so.conf. Prevent this warning with:
mkdir -v /tools/etc
touch /tools/etc/ld.so.conf

   Install the package:
make install

   Different countries and cultures have varying conventions for how to
   communicate. These conventions range from the format for representing
   dates and times to more complex issues, such as the language spoken.
   The "internationalization" of GNU programs works by locale.

Note

   If the test suites are not being run in this chapter (as per the
   recommendation), there is no need to install the locales now. The
   appropriate locales will be installed in the next chapter.

   To install the Glibc locales anyway, use the following command:
make localedata/install-locales

   To save time, an alternative to running the previous command (which
   generates and installs every locale Glibc is aware of) is to install
   only those locales that are wanted and needed. This can be achieved by
   using the localedef command. Information on this command is located in
   the INSTALL file in the Glibc source. However, there are a number of
   locales that are essential in order for the tests of future packages
   to pass, in particular, the libstdc++ tests from GCC. The following
   instructions, instead of the install-locales target used above, will
   install the minimum set of locales necessary for the tests to run
   successfully:
mkdir -pv /tools/lib/locale
localedef -i de_DE -f ISO-8859-1 de_DE
localedef -i de_DE@euro -f ISO-8859-15 de_DE@euro
localedef -i en_HK -f ISO-8859-1 en_HK
localedef -i en_PH -f ISO-8859-1 en_PH
localedef -i en_US -f ISO-8859-1 en_US
localedef -i es_MX -f ISO-8859-1 es_MX
localedef -i fa_IR -f UTF-8 fa_IR
localedef -i fr_FR -f ISO-8859-1 fr_FR
localedef -i fr_FR@euro -f ISO-8859-15 fr_FR@euro
localedef -i it_IT -f ISO-8859-1 it_IT
localedef -i ja_JP -f EUC-JP ja_JP

   Details on this package are located in [344]Section 6.11.4, "Contents
   of Glibc."

5.7. Adjusting the Toolchain

   Now that the temporary C libraries have been installed, all tools
   compiled in the rest of this chapter should be linked against these
   libraries. In order to accomplish this, the linker and the compiler's
   specs file need to be adjusted.

   The linker, adjusted at the end of the first pass of Binutils, is
   installed by running the following command from within the
   binutils-build directory:
make -C ld install

   From this point onwards, everything will link only against the
   libraries in /tools/lib.

Note

   If the earlier warning to retain the Binutils source and build
   directories from the first pass was missed, ignore the above command.
   This results in a small chance that the subsequent testing programs
   will link against libraries on the host. This is not ideal, but it is
   not a major problem. The situation is corrected when the second pass
   of Binutils is installed later.

   Now that the adjusted linker is installed, the Binutils build and
   source directories should be removed.

   The next task is to amend the GCC specs file so that it points to the
   new dynamic linker. A simple sed script will accomplish this:
SPECFILE=`gcc --print-file specs` &&
sed 's@ /lib/ld-linux.so.2@ /tools/lib/ld-linux.so.2@g' \
    $SPECFILE > tempspecfile &&
mv -f tempspecfile $SPECFILE &&
unset SPECFILE

   It is recommended that the above command be copy-and-pasted in order
   to ensure accuracy. Alternatively, the specs file can be edited by
   hand. This is done by replacing every occurrence of
   "/lib/ld-linux.so.2" with "/tools/lib/ld-linux.so.2"

   Be sure to visually inspect the specs file in order to verify the
   intended changes have been made.

Important

   If working on a platform where the name of the dynamic linker is
   something other than ld-linux.so.2, replace "ld-linux.so.2" with the
   name of the platform's dynamic linker in the above commands. Refer
   back to [345]Section 5.2, "Toolchain Technical Notes," if necessary.

   There is a possibility that some include files from the host system
   have found their way into GCC's private include dir. This can happen
   as a result of GCC's "fixincludes" process, which runs as part of the
   GCC build. This is explained in more detail later in this chapter. Run
   the following command to eliminate this possibility:
rm -vf /tools/lib/gcc/*/*/include/{pthread.h,bits/sigthread.h}

Caution

   At this point, it is imperative to stop and ensure that the basic
   functions (compiling and linking) of the new toolchain are working as
   expected. To perform a sanity check, run the following commands:
echo 'main(){}' > dummy.c
cc dummy.c
readelf -l a.out | grep ': /tools'

   If everything is working correctly, there should be no errors, and the
   output of the last command will be of the form:
[Requesting program interpreter:
    /tools/lib/ld-linux.so.2]

   Note that /tools/lib appears as the prefix of the dynamic linker.

   If the output is not shown as above or there was no output at all,
   then something is wrong. Investigate and retrace the steps to find out
   where the problem is and correct it. This issue must be resolved
   before continuing on. First, perform the sanity check again, using gcc
   instead of cc. If this works, then the /tools/bin/cc symlink is
   missing. Revisit [346]Section 5.4, "GCC-3.4.3 - Pass 1," and install
   the symlink. Next, ensure that the PATH is correct. This can be
   checked by running echo $PATH and verifying that /tools/bin is at the
   head of the list. If the PATH is wrong it could mean that you are not
   logged in as user lfs or that something went wrong back in
   [347]Section 4.4, "Setting Up the Environment." Another option is that
   something may have gone wrong with the specs file amendment above. In
   this case, redo the specs file amendment, being careful to
   copy-and-paste the commands.

   Once all is well, clean up the test files:
rm -v dummy.c a.out

   Building TCL in the next section will serve as an additional check
   that the toolchain has been built properly. If TCL fails to build, it
   is an indication that something has gone wrong with the Binutils, GCC,
   or Glibc installation, but not with TCL itself.

5.8. Tcl-8.4.9

   The Tcl package contains the Tool Command Language.
   Approximate build time: 0.9 SBU
   Required disk space: 23.3 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, Grep, Make, and Sed

5.8.1. Installation of Tcl

   This package and the next two (Expect and DejaGNU) are installed to
   support running the test suites for GCC and Binutils. Installing three
   packages for testing purposes may seem excessive, but it is very
   reassuring, if not essential, to know that the most important tools
   are working properly. Even if the test suites are not run in this
   chapter (they are not mandatory), these packages are required to run
   the test suites in [348]Chapter 6.

   Prepare Tcl for compilation:
cd unix
./configure --prefix=/tools

   Build the package:
make

   To test the results, issue: TZ=UTC make test. The Tcl test suite is
   known to experience failures under certain host conditions that are
   not fully understood. Therefore, test suite failures here are not
   surprising, and are not considered critical. The TZ=UTC parameter sets
   the time zone to Coordinated Universal Time (UTC), also known as
   Greenwich Mean Time (GMT), but only for the duration of the test suite
   run. This ensures that the clock tests are exercised correctly.
   Details on the TZ environment variable are provided in [349]Chapter 7.

   Install the package:
make install

Warning

   Do not remove the tcl8.4.9 source directory yet, as the next package
   will need its internal headers.

   Set a variable containing the full path of the current directory. The
   next package, Expect, will use this variable to find Tcl's headers.
cd ..
export TCLPATH=`pwd`

   Now make a necessary symbolic link:
ln -sv tclsh8.4 /tools/bin/tclsh

5.8.2. Contents of Tcl

   Installed programs: tclsh (link to tclsh8.4) and tclsh8.4
   Installed library: libtcl8.4.so

Short Descriptions

   tclsh8.4

   The Tcl command shell
   tclsh

   A link to tclsh8.4
   libtcl8.4.so

   The Tcl library

5.9. Expect-5.43.0

   The Expect package contains a program for carrying out scripted
   dialogues with other interactive programs.
   Approximate build time: 0.1 SBU
   Required disk space: 4.0 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, Grep, Make, Sed, and Tcl

5.9.1. Installation of Expect

   First, fix a bug that can result in false failures during the GCC test
   suite run:
patch -Np1 -i ../expect-5.43.0-spawn-1.patch

   Now prepare Expect for compilation:
./configure --prefix=/tools --with-tcl=/tools/lib \
   --with-tclinclude=$TCLPATH --with-x=no

   The meaning of the configure options:

   --with-tcl=/tools/lib
          This ensures that the configure script finds the Tcl
          installation in the temporary tools location instead of
          possibly locating an existing one on the host system.

   --with-tclinclude=$TCLPATH
          This explicitly tells Expect where to find Tcl's source
          directory and internal headers. Using this option avoids
          conditions where configure fails because it cannot
          automatically discover the location of the Tcl source
          directory.

   --with-x=no
          This tells the configure script not to search for Tk (the Tcl
          GUI component) or the X Window System libraries, both of which
          may reside on the host system but will not exist in the
          temporary environment.

   Build the package:
make

   To test the results, issue: make test. Note that the Expect test suite
   is known to experience failures under certain host conditions that are
   not within our control. Therefore, test suite failures here are not
   surprising and are not considered critical.

   Install the package:
make SCRIPTS="" install

   The meaning of the make parameter:

   SCRIPTS=""
          This prevents installation of the supplementary expect scripts,
          which are not needed.

   Now remove the TCLPATH variable:
unset TCLPATH

   The source directories of both Tcl and Expect can now be removed.

5.9.2. Contents of Expect

   Installed program: expect
   Installed library: libexpect-5.43.a

Short Descriptions

   expect

   Communicates with other interactive programs according to a script
   libexpect-5.43.a

   Contains functions that allow Expect to be used as a Tcl extension or
   to be used directly from C or C++ (without Tcl)

5.10. DejaGNU-1.4.4

   The DejaGNU package contains a framework for testing other programs.
   Approximate build time: 0.1 SBU
   Required disk space: 6.1 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, Grep, Make, and Sed

5.10.1. Installation of DejaGNU

   Prepare DejaGNU for compilation:
./configure --prefix=/tools

   Build and install the package:
make install

5.10.2. Contents of DejaGNU

   Installed program: runtest

Short Descriptions

   runtest

   A wrapper script that locates the proper expect shell and then runs
   DejaGNU

5.11. GCC-3.4.3 - Pass 2

   Approximate build time: 11.0 SBU
   Required disk space: 292 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils,
   Findutils, Gawk, Gettext, Glibc, Grep, Make, Perl, Sed, and Texinfo
