
5.11.1. Re-installation of GCC

   This package is known to have issues when its default optimization
   flags (including the -march and -mcpu options) are changed. If any
   environment variables that override default optimizations have been
   defined, such as CFLAGS and CXXFLAGS, unset them when building GCC.

   The tools required to test GCC and Binutils--Tcl, Expect and
   DejaGNU--are installed now. GCC and Binutils can now be rebuilt,
   linking them against the new Glibc and testing them properly (if
   running the test suites in this chapter). Please note that these test
   suites are highly dependent on properly functioning PTYs which are
   provided by the host. PTYs are most commonly implemented via the
   devpts file system. Check to see if the host system is set up
   correctly in this regard by performing a quick test:
expect -c "spawn ls"

   The response might be:
The system has no more ptys.
Ask your system administrator to create more.

   If the above message is received, the host does not have its PTYs set
   up properly. In this case, there is no point in running the test
   suites for GCC and Binutils until this issue is resolved. Please
   consult the LFS FAQ at
   [350]http://www.linuxfromscratch.org//lfs/faq.html#no-ptys for more
   information on how to get PTYs working.

   First correct a known problem and make an essential adjustment:
patch -Np1 -i ../gcc-3.4.3-no_fixincludes-1.patch
patch -Np1 -i ../gcc-3.4.3-specs-2.patch

   The first patch disables the GCC fixincludes script. This was briefly
   mentioned earlier, but a more in-depth explanation of the fixincludes
   process is warranted here. Under normal circumstances, the GCC
   fixincludes script scans the system for header files that need to be
   fixed. It might find that some Glibc header files on the host system
   need to be fixed, and will fix them and put them in the GCC private
   include directory. In [351]Chapter 6, after the newer Glibc has been
   installed, this private include directory will be searched before the
   system include directory. This may result in GCC finding the fixed
   headers from the host system, which most likely will not match the
   Glibc version used for the LFS system.

   The second patch changes GCC's default location of the dynamic linker
   (typically ld-linux.so.2). It also removes /usr/include from GCC's
   include search path. Patching now rather than adjusting the specs file
   after installation ensures that the new dynamic linker is used during
   the actual build of GCC. That is, all of the final (and temporary)
   binaries created during the build will link against the new Glibc.

Important

   The above patches are critical in ensuring a successful overall build.
   Do not forget to apply them.

   Create a separate build directory again:
mkdir -v ../gcc-build
cd ../gcc-build

   Before starting to build GCC, remember to unset any environment
   variables that override the default optimization flags.

   Now prepare GCC for compilation:
../gcc-3.4.3/configure --prefix=/tools \
    --libexecdir=/tools/lib --with-local-prefix=/tools \
    --enable-clocale=gnu --enable-shared \
    --enable-threads=posix --enable-__cxa_atexit \
    --enable-languages=c,c++ --disable-libstdcxx-pch

   The meaning of the new configure options:

   --enable-clocale=gnu
          This option ensures the correct locale model is selected for
          the C++ libraries under all circumstances. If the configure
          script finds the de_DE locale installed, it will select the
          correct gnu locale model. However, if the de_DE locale is not
          installed, there is the risk of building Application Binary
          Interface (ABI)-incompatible C++ libraries because the
          incorrect generic locale model may be selected.

   --enable-threads=posix
          This enables C++ exception handling for multi-threaded code.

   --enable-__cxa_atexit
          This option allows use of __cxa_atexit, rather than atexit, to
          register C++ destructors for local statistics and global objects.
          This option is essential for fully standards-compliant handling
          of destructors. It also affects the C++ ABI, and therefore
          results in C++ shared libraries and C++ programs that are
          interoperable with other Linux distributions.

   --enable-languages=c,c++
          This option ensures that both the C and C++ compilers are
          built.

   --disable-libstdcxx-pch
          Do not build the pre-compiled header (PCH) for libstdc++. It
          takes up a lot of space, and we have no use for it.

   Compile the package:
make

   There is no need to use the bootstrap target now because the compiler
   being used to compile this GCC was built from the exact same version
   of the GCC sources used earlier.

   Compilation is now complete. As previously mentioned, running the test
   suites for the temporary tools compiled in this chapter is not
   mandatory. To run the GCC test suite anyway, use the following
   command:
make -k check

   The -k flag is used to make the test suite run through to completion
   and not stop at the first failure. The GCC test suite is very
   comprehensive and is almost guaranteed to generate a few failures. To
   receive a summary of the test suite results, run:
../gcc-3.4.3/contrib/test_summary

   For only the summaries, pipe the output through grep -A7 Summ.

   Results can be compared with those located at
   [352]http://www.linuxfromscratch.org/lfs/build-logs/6.1.1/.

   A few unexpected failures cannot always be avoided. The GCC developers
   are usually aware of these issues, but have not resolved them yet.
   Unless the test results are vastly different from those at the above
   URL, it is safe to continue.

   Install the package:
make install

Note

   At this point it is strongly recommended to repeat the sanity check we
   performed earlier in this chapter. Refer back to [353]Section 5.7,
   "Adjusting the Toolchain," and repeat the test compilation. If the
   result is wrong, the most likely reason is that the GCC Specs patch
   was not properly applied.

   Details on this package are located in [354]Section 6.14.2, "Contents
   of GCC."

5.12. Binutils-2.15.94.0.2.2 - Pass 2

   The Binutils package contains a linker, an assembler, and other tools
   for handling object files.
   Approximate build time: 1.5 SBU
   Required disk space: 114 MB
   Installation depends on: Bash, Bison, Coreutils, Diffutils, Flex, GCC,
   Gettext, Glibc, Grep, M4, Make, Perl, Sed, and Texinfo

5.12.1. Re-installation of Binutils

   This package is known to have issues when its default optimization
   flags (including the -march and -mcpu options) are changed. If any
   environment variables that override default optimizations have been
   defined, such as CFLAGS and CXXFLAGS, unset them when building
   Binutils.

   Create a separate build directory again:
mkdir -v ../binutils-build
cd ../binutils-build

   Prepare Binutils for compilation:
../binutils-2.15.94.0.2.2/configure --prefix=/tools \
    --disable-nls --enable-shared --with-lib-path=/tools/lib

   The meaning of the new configure options:

   --with-lib-path=/tools/lib
          This tells the configure script to specify the library search
          path during the compilation of Binutils, resulting in
          /tools/lib being passed to the linker. This prevents the linker
          from searching through library directories on the host.

   Compile the package:
make

   Compilation is now complete. As discussed earlier, running the test
   suite is not mandatory for the temporary tools here in this chapter.
   To run the Binutils test suite anyway, issue the following command:
make check

   Install the package:
make install

   Now prepare the linker for the "Re-adjusting" phase in the next
   chapter:
make -C ld clean
make -C ld LIB_PATH=/usr/lib:/lib

Warning

   Do not remove the Binutils source and build directories yet. These
   directories will be needed again in the next chapter in their current
   state.

   Details on this package are located in [355]Section 6.13.2, "Contents
   of Binutils."

5.13. Gawk-3.1.4

   The Gawk package contains programs for manipulating text files.
   Approximate build time: 0.2 SBU
   Required disk space: 16.4 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, and Sed

5.13.1. Installation of Gawk

   Prepare Gawk for compilation:
./configure --prefix=/tools

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

   Details on this package are located in [356]Section 6.20.2, "Contents
   of Gawk."

5.14. Coreutils-5.2.1

   The Coreutils package contains utilities for showing and setting the
   basic system characteristics.
   Approximate build time: 0.9 SBU
   Required disk space: 53.3 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, Perl, and Sed

5.14.1. Installation of Coreutils

   Prepare Coreutils for compilation:
DEFAULT_POSIX2_VERSION=199209 ./configure --prefix=/tools

   This package has an issue when compiled against versions of Glibc
   later than 2.3.2. Some of the Coreutils utilities (such as head, tail,
   and sort) will reject their traditional syntax, a syntax that has been
   in use for approximately 30 years. This old syntax is so pervasive
   that compatibility should be preserved until the many places where it
   is used can be updated. Backwards compatibility is achieved by setting
   the DEFAULT_POSIX2_VERSION environment variable to "199209" in the
   above command. If you do not want Coreutils to be backwards compatible
   with the traditional syntax, then omit setting the
   DEFAULT_POSIX2_VERSION environment variable. It is important to
   remember that doing so will have consequences, including the need to
   patch the many packages that still use the old syntax. Therefore, it
   is recommended that the instructions be followed exactly as given
   above.

   Compile the package:
make

   To test the results, issue: make RUN_EXPENSIVE_TESTS=yes check. The
   RUN_EXPENSIVE_TESTS=yes parameter tells the test suite to run several
   additional tests that are considered relatively expensive (in terms of
   CPU power and memory usage) on some platforms, but generally are not a
   problem on Linux.

   Install the package:
make install

   Details on this package are located in [357]Section 6.15.2, "Contents
   of Coreutils."

5.15. Bzip2-1.0.3

   The Bzip2 package contains programs for compressing and decompressing
   files. Compressing text files with bzip2 yields a much better
   compression percentage than with the traditional gzip.
   Approximate build time: 0.1 SBU
   Required disk space: 3.5 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, and Make

5.15.1. Installation of Bzip2

   The Bzip2 package does not contain a configure script. Compile and
   test it with:
make

   Install the package:
make PREFIX=/tools install

   Details on this package are located in [358]Section 6.40.2, "Contents
   of Bzip2."

5.16. Gzip-1.3.5

   The Gzip package contains programs for compressing and decompressing
   files.
   Approximate build time: 0.1 SBU
   Required disk space: 2.2 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, Grep, Make, and Sed

5.16.1. Installation of Gzip

   Prepare Gzip for compilation:
./configure --prefix=/tools

   Compile the package:
make

   This package does not come with a test suite.

   Install the package:
make install

   Details on this package are located in [359]Section 6.46.2, "Contents
   of Gzip."

5.17. Diffutils-2.8.1

   The Diffutils package contains programs that show the differences
   between files or directories.
   Approximate build time: 0.1 SBU
   Required disk space: 5.6 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, and Sed

5.17.1. Installation of Diffutils

   Prepare Diffutils for compilation:
./configure --prefix=/tools

   Compile the package:
make

   This package does not come with a test suite.

   Install the package:
make install

   Details on this package are located in [360]Section 6.41.2, "Contents
   of Diffutils."

5.18. Findutils-4.2.23

   The Findutils package contains programs to find files. These programs
   are provided to recursively search through a directory tree and to
   create, maintain, and search a database (often faster than the
   recursive find, but unreliable if the database has not been recently
   updated).
   Approximate build time: 0.2 SBU
   Required disk space: 8.9 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make and Sed

5.18.1. Installation of Findutils

   Prepare Findutils for compilation:
./configure --prefix=/tools

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

   Details on this package are located in [361]Section 6.19.2, "Contents
   of Findutils."

5.19. Make-3.80

   The Make package contains a program for compiling packages.
   Approximate build time: 0.2 SBU
   Required disk space: 7.1 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, and Sed

5.19.1. Installation of Make

   Prepare Make for compilation:
./configure --prefix=/tools

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

   Details on this package are located in [362]Section 6.49.2, "Contents
   of Make."

5.20. Grep-2.5.1a

   The Grep package contains programs for searching through files.
   Approximate build time: 0.1 SBU
   Required disk space: 4.5 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Make, Sed, and Texinfo

5.20.1. Installation of Grep

   Prepare Grep for compilation:
./configure --prefix=/tools \
    --disable-perl-regexp

   The meaning of the configure options:

   --disable-perl-regexp
          This ensures that the grep program does not get linked against
          a Perl Compatible Regular Expression (PCRE) library that may be
          present on the host but will not be available once we enter the
          chroot environment.

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

   Details on this package are located in [363]Section 6.44.2, "Contents
   of Grep."

5.21. Sed-4.1.4

   The Sed package contains a stream editor.
   Approximate build time: 0.2 SBU
   Required disk space: 8.4 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, and Texinfo

5.21.1. Installation of Sed

   Prepare Sed for compilation:
./configure --prefix=/tools

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

   Details on this package are located in [364]Section 6.28.2, "Contents
   of Sed."

5.22. Gettext-0.14.3

   The Gettext package contains utilities for internationalization and
   localization. These allow programs to be compiled with NLS (Native
   Language Support), enabling them to output messages in the user's
   native language.
   Approximate build time: 0.5 SBU
   Required disk space: 63.0 MB
   Installation depends on: Bash, Binutils, Bison, Coreutils, Diffutils,
   Gawk, GCC, Glibc, Grep, Make, and Sed

5.22.1. Installation of Gettext

   Prepare Gettext for compilation:
./configure --prefix=/tools --disable-libasprintf \
    --without-csharp

   The meaning of the configure options:

   --disable-libasprintf
          This flag tells Gettext not to build the asprintf library.
          Because nothing in this chapter or the next requires this
          library and Gettext gets rebuilt later, exclude it to save time
          and space.

   --without-csharp
          This ensures that Gettext does not build support for the C#
          compiler which may be present on the host but will not be
          available once we enter the chroot environment.

   Compile the package:
make

   To test the results, issue: make check. This takes quite some time,
   around 7 SBUs. The Gettext test suite is known to experience failures
   under certain host conditions, for example when it finds a Java
   compiler on the host. An experimental patch to disable Java is
   available from the LFS Patches project at
   [365]http://www.linuxfromscratch.org/patches/.

   Install the package:
make install

   Details on this package are located in [366]Section 6.30.2, "Contents
   of Gettext."

5.23. Ncurses-5.4

   The Ncurses package contains libraries for terminal-independent
   handling of character screens.
   Approximate build time: 0.7 SBU
   Required disk space: 27.5 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, Gawk,
   GCC, Glibc, Grep, Make, and Sed

5.23.1. Installation of Ncurses

   Prepare Ncurses for compilation:
./configure --prefix=/tools --with-shared \
    --without-debug --without-ada --enable-overwrite

   The meaning of the configure options:

   --without-ada
          This ensures that Ncurses does not build support for the Ada
          compiler which may be present on the host but will not be
          available once we enter the chroot environment.

   --enable-overwrite
          This tells Ncurses to install its header files into
          /tools/include, instead of /tools/include/ncurses, to ensure
          that other packages can find the Ncurses headers successfully.

   Compile the package:
make

   This package does not come with a test suite.

   Install the package:
make install

   Details on this package are located in [367]Section 6.21.2, "Contents
   of Ncurses."

5.24. Patch-2.5.4

   The Patch package contains a program for modifying or creating files
   by applying a "patch" file typically created by the diff program.
   Approximate build time: 0.1 SBU
   Required disk space: 1.5 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, Grep, Make, and Sed

5.24.1. Installation of Patch

   Prepare Patch for compilation:
CPPFLAGS=-D_GNU_SOURCE ./configure --prefix=/tools

   The preprocessor flag -D_GNU_SOURCE is only needed on the PowerPC
   platform. It can be left out on other architectures.

   Compile the package:
make

   This package does not come with a test suite.

   Install the package:
make install

   Details on this package are located in [368]Section 6.51.2, "Contents
   of Patch."

5.25. Tar-1.15.1

   The Tar package contains an archiving program.
   Approximate build time: 0.2 SBU
   Required disk space: 12.7 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, and Sed

5.25.1. Installation of Tar

   Prepare Tar for compilation:
./configure --prefix=/tools

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

   Details on this package are located in [369]Section 6.57.2, "Contents
   of Tar."

5.26. Texinfo-4.8

   The Texinfo package contains programs for reading, writing, and
   converting info pages.
   Approximate build time: 0.2 SBU
   Required disk space: 14.7 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, Ncurses, and Sed

5.26.1. Installation of Texinfo

   Prepare Texinfo for compilation:
./configure --prefix=/tools

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

   Details on this package are located in [370]Section 6.34.2, "Contents
   of Texinfo."

5.27. Bash-3.0

   The Bash package contains the Bourne-Again SHell.
   Approximate build time: 1.2 SBU
   Required disk space: 20.7 MB
   Installation depends on: Binutils, Coreutils, Diffutils, Gawk, GCC,
   Glibc, Grep, Make, Ncurses, and Sed.

5.27.1. Installation of Bash

   Bash has a problem when compiled against newer versions of Glibc,
   causing it to hang inappropriately. This patch fixes the problem:
patch -Np1 -i ../bash-3.0-avoid_WCONTINUED-1.patch

   Prepare Bash for compilation:
./configure --prefix=/tools --without-bash-malloc

   The meaning of the configure options:

   --without-bash-malloc
          This options turns off the use of Bash's memory allocation
          (malloc) function which is known to cause segmentation faults.
          By turning this option off, Bash will use the malloc functions
          from Glibc which are more stable.

   Compile the package:
make

   To test the results, issue: make tests.

   Install the package:
make install

   Make a link for the programs that use sh for a shell:
ln -vs bash /tools/bin/sh

   Details on this package are located in [371]Section 6.37.2, "Contents
   of Bash."

5.28. M4-1.4.3

   The M4 package contains a macro processor.
   Approximate build time: 0.1 SBU
   Required disk space: 2.8 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, Perl, and Sed

5.28.1. Installation of M4

   Prepare M4 for compilation:
./configure --prefix=/tools

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

   Details on this package are located in [372]Section 6.24.2, "Contents
   of M4."

5.29. Bison-2.0

   The Bison package contains a parser generator.
   Approximate build time: 0.6 SBU
   Required disk space: 10.0 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, M4, Make, and Sed

5.29.1. Installation of Bison

   Prepare Bison for compilation:
./configure --prefix=/tools

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

   Details on this package are located in [373]Section 6.25.2, "Contents
   of Bison."

5.30. Flex-2.5.31

   The Flex package contains a utility for generating programs that
   recognize patterns in text.
   Approximate build time: 0.6 SBU
   Required disk space: 22.5 MB
   Installation depends on: Bash, Binutils, Bison, Coreutils, Diffutils,
   GCC, Gettext, Glibc, Grep, M4, Make, and Sed

5.30.1. Installation of Flex

   Flex contains several known bugs. These can be fixed with the
   following patch:
patch -Np1 -i ../flex-2.5.31-debian_fixes-3.patch

   The GNU autotools will detect that the Flex source code has been
   modified by the previous patch and tries to update the man page
   accordingly. This does not work on many systems, and the default page
   is fine, so make sure it does not get regenerated:
touch doc/flex.1

   Now prepare Flex for compilation:
./configure --prefix=/tools

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

   Details on this package are located in [374]Section 6.29.2, "Contents
   of Flex."

5.31. Util-linux-2.12q

   The Util-linux package contains miscellaneous utility programs. Among
   them are utilities for handling file systems, consoles, partitions,
   and messages.
   Approximate build time: 0.2 SBU
   Required disk space: 8.9 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, Ncurses, Sed, and Zlib

5.31.1. Installation of Util-linux

   Util-linux does not use the freshly installed headers and libraries
   from the /tools directory by default. This is fixed by altering the
   configure script:
sed -i 's@/usr/include@/tools/include@g' configure

   Prepare Util-linux for compilation:
./configure

   Compile some support routines:
make -C lib

   Only a few of the utilities contained in this package need to be
   built:
make -C mount mount umount
make -C text-utils more

   This package does not come with a test suite.

   Copy these programs to the temporary tools directory:
cp mount/{,u}mount text-utils/more /tools/bin

   Details on this package are located in [375]Section 6.59.3, "Contents
   of Util-linux."

5.32. Perl-5.8.7

   The Perl package contains the Practical Extraction and Report
   Language.
   Approximate build time: 0.8 SBU
   Required disk space: 81.6 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, Gawk,
   GCC, Glibc, Grep, Make, and Sed

5.32.1. Installation of Perl

   First adapt some hard-wired paths to the C library by applying the
   following patch:
patch -Np1 -i ../perl-5.8.7-libc-1.patch

   Prepare Perl for compilation (make sure to get the 'IO Fcntl POSIX'
   part of the command correct--they are all letters):
./configure.gnu --prefix=/tools -Dstatic_ext='IO Fcntl POSIX'

   The meaning of the configure options:

   -Dstatic_ext='IO Fcntl POSIX'
          This tells Perl to build the minimum set of static extensions
          needed for installing and testing the Coreutils package in the
          next chapter.

   Only a few of the utilities contained in this package need to be
   built:
make perl utilities

   Although Perl comes with a test suite, it is not recommended to run it
   at this point. Only part of Perl was built and running make test now
   will cause the rest of Perl to be built as well, which is unnecessary
   at this point. The test suite can be run in the next chapter if
   desired.

   Install these tools and their libraries:
cp -v perl pod/pod2man /tools/bin
mkdir -pv /tools/lib/perl5/5.8.7
