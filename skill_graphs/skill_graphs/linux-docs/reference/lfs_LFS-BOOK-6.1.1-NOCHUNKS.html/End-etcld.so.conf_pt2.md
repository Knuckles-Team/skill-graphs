**test** |  Compares values and checks file types
**touch** |  Changes file timestamps, setting the access and modification times of the given files to the current time; files that do not exist are created with zero length
**tr** |  Translates, squeezes, and deletes the given characters from standard input
**true** |  Does nothing, successfully; it always exits with a status code indicating success
**tsort** |  Performs a topological sort; it writes a completely ordered list according to the partial ordering in a given file
**tty** |  Reports the file name of the terminal connected to standard input
**uname** |  Reports system information
**unexpand** |  Converts spaces to tabs
**uniq** |  Discards all but one of successive identical lines
**unlink** |  Removes the given file
**users** |  Reports the names of the users currently logged on
**vdir** |  Is the same as **ls -l**
**wc** |  Reports the number of lines, words, and bytes for each given file, as well as a total line when more than one file is given
**who** |  Reports who is logged on
**whoami** |  Reports the user name associated with the current effective user ID
**yes** |  Repeatedly outputs “y” or a given string until killed
##  6.16. Zlib-1.2.3
The Zlib package contains compression and decompression routines used by some programs.
**Approximate build time:** 0.1 SBU
**Required disk space:** 3.1 MB
**Installation depends on:** Binutils, Coreutils, GCC, Glibc, Make, and Sed
###  6.16.1. Installation of Zlib
###  Note
Zlib is known to build its shared library incorrectly if `CFLAGS` is specified in the environment. If using a specified `CFLAGS` variable, be sure to add the _`-fPIC`_ directive to the `CFLAGS` variable for the duration of the configure command below, then remove it afterwards.
Prepare Zlib for compilation:
```
`./configure --prefix=/usr --shared --libdir=/lib`
```

Compile the package:
```
`make`
```

To test the results, issue: **`make check`**.
Install the shared library:
```
`make install`
```

The previous command installed a `.so` file in `/lib`. We will remove it and relink it into `/usr/lib`:
```
`rm -v /lib/libz.so
ln -sfv ../../lib/libz.so.1.2.3 /usr/lib/libz.so`
```

Build the static library:
```
`make clean
./configure --prefix=/usr
make`
```

To test the results again, issue: **`make check`**.
Install the static library:
```
`make install`
```

Fix the permissions on the static library:
```
`chmod -v 644 /usr/lib/libz.a`
```

###  6.16.2. Contents of Zlib
**Installed libraries:** libz.[a,so]
###  Short Descriptions
`libz` |  Contains compression and decompression functions used by some programs
---|---
##  6.17. Mktemp-1.5
The Mktemp package contains programs used to create secure temporary files in shell scripts.
**Approximate build time:** 0.1 SBU
**Required disk space:** 436 KB
**Installation depends on:** Coreutils, Make, and Patch
###  6.17.1. Installation of Mktemp
Many scripts still use the deprecated **tempfile** program, which has functionality similar to **mktemp**. Patch Mktemp to include a **tempfile** wrapper:
```
`patch -Np1 -i ../mktemp-1.5-add_tempfile-2.patch`
```

Prepare Mktemp for compilation:
```
`./configure --prefix=/usr --with-libc`
```

The meaning of the configure options:

_`--with-libc`_

This causes the **mktemp** program to use the _mkstemp_ and _mkdtemp_ functions from the system C library.
Compile the package:
```
`make`
```

Install the package:
```
`make install
make install-tempfile`
```

###  6.17.2. Contents of Mktemp
**Installed programs:** mktemp and tempfile
###  Short Descriptions
**mktemp** |  Creates temporary files in a secure manner; it is used in scripts
---|---
**tempfile** |  Creates temporary files in a less secure manner than **mktemp** ; it is installed for backwards-compatibility
##  6.18. Iana-Etc-1.04
The Iana-Etc package provides data for network services and protocols.
**Approximate build time:** 0.1 SBU
**Required disk space:** 1.9 MB
**Installation depends on:** Make
###  6.18.1. Installation of Iana-Etc
The following command converts the raw data provided by IANA into the correct formats for the `/etc/protocols` and `/etc/services` data files:
```
`make`
```

Install the package:
```
`make install`
```

###  6.18.2. Contents of Iana-Etc
**Installed files:** /etc/protocols and /etc/services
###  Short Descriptions
`/etc/protocols` |  Describes the various DARPA Internet protocols that are available from the TCP/IP subsystem
---|---
`/etc/services` |  Provides a mapping between friendly textual names for internet services, and their underlying assigned port numbers and protocol types
##  6.19. Findutils-4.2.23
The Findutils package contains programs to find files. These programs are provided to recursively search through a directory tree and to create, maintain, and search a database (often faster than the recursive find, but unreliable if the database has not been recently updated).
**Approximate build time:** 0.1 SBU
**Required disk space:** 9.4 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Gettext, Glibc, Grep, Make and Sed
###  6.19.1. Installation of Findutils
Prepare Findutils for compilation:
```
`./configure --prefix=/usr --libexecdir=/usr/lib/locate \
    --localstatedir=/var/lib/locate`
```

The meaning of the configure options:

_`--localstatedir`_

This option changes the location of the **locate** database to be in `/var/lib/locate`, which is FHS-compliant.
Compile the package:
```
`make`
```

To test the results, issue: **`make check`**.
Install the package:
```
`make install`
```

###  6.19.2. Contents of Findutils
**Installed programs:** bigram, code, find, frcode, locate, updatedb, and xargs
###  Short Descriptions
**bigram** |  Was formerly used to produce **locate** databases
---|---
**code** |  Was formerly used to produce **locate** databases; it is the ancestor of **frcode**.
**find** |  Searches given directory trees for files matching the specified criteria
**frcode** |  Is called by **updatedb** to compress the list of file names; it uses front-compression, reducing the database size by a factor of four to five.
**locate** |  Searches through a database of file names and reports the names that contain a given string or match a given pattern
**updatedb** |  Updates the **locate** database; it scans the entire file system (including other file systems that are currently mounted, unless told not to) and puts every file name it finds into the database
**xargs** |  Can be used to apply a given command to a list of files
##  6.20. Gawk-3.1.4
The Gawk package contains programs for manipulating text files.
**Approximate build time:** 0.2 SBU
**Required disk space:** 16.4 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Gettext, Glibc, Grep, Make, and Sed
###  6.20.1. Installation of Gawk
Prepare Gawk for compilation:
```
`./configure --prefix=/usr --libexecdir=/usr/lib`
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

###  6.20.2. Contents of Gawk
**Installed programs:** awk (link to gawk), gawk, gawk-3.1.4, grcat, igawk, pgawk, pgawk-3.1.4, and pwcat
###  Short Descriptions
**awk** |  A link to **gawk**
---|---
**gawk** |  A program for manipulating text files; it is the GNU implementation of **awk**
**gawk-3.1.4** |  A hard link to **gawk**
**grcat** |  Dumps the group database `/etc/group`
**igawk** |  Gives **gawk** the ability to include files
**pgawk** |  The profiling version of **gawk**
**pgawk-3.1.4** |  Hard link to **pgawk**
**pwcat** |  Dumps the password database `/etc/passwd`
##  6.21. Ncurses-5.4
The Ncurses package contains libraries for terminal-independent handling of character screens.
**Approximate build time:** 0.6 SBU
**Required disk space:** 18.6 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, Gawk, GCC, Glibc, Grep, Make, and Sed
###  6.21.1. Installation of Ncurses
Prepare Ncurses for compilation:
```
`./configure --prefix=/usr --with-shared --without-debug`
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

Give the Ncurses libraries execute permissions:
```
`chmod -v 755 /usr/lib/*.5.4`
```

Fix a library that should not be executable:
```
`chmod -v 644 /usr/lib/libncurses++.a`
```

Move the libraries to the `/lib` directory, where they are expected to reside:
```
`mv -v /usr/lib/libncurses.so.5* /lib`
```

Because the libraries have been moved, a few symlinks point to non-existent files. Recreate those symlinks:
```
`ln -sfv ../../lib/libncurses.so.5 /usr/lib/libncurses.so
ln -sfv libncurses.so /usr/lib/libcurses.so`
```

###  6.21.2. Contents of Ncurses
**Installed programs:** captoinfo (link to tic), clear, infocmp, infotocap (link to tic), reset (link to tset), tack, tic, toe, tput, and tset
**Installed libraries:** libcurses.[a,so] (link to libncurses.[a,so]), libform.[a,so], libmenu.[a,so], libncurses++.a, libncurses.[a,so], and libpanel.[a,so]
###  Short Descriptions
**captoinfo** |  Converts a termcap description into a terminfo description
---|---
**clear** |  Clears the screen, if possible
**infocmp** |  Compares or prints out terminfo descriptions
**infotocap** |  Converts a terminfo description into a termcap description
**reset** |  Reinitializes a terminal to its default values
**tack** |  The terminfo action checker; it is mainly used to test the accuracy of an entry in the terminfo database
**tic** |  The terminfo entry-description compiler that translates a terminfo file from source format into the binary format needed for the ncurses library routines. A terminfo file contains information on the capabilities of a certain terminal
**toe** |  Lists all available terminal types, giving the primary name and description for each
**tput** |  Makes the values of terminal-dependent capabilities available to the shell; it can also be used to reset or initialize a terminal or report its long name
**tset** |  Can be used to initialize terminals
`libcurses` |  A link to `libncurses`
`libncurses` |  Contains functions to display text in many complex ways on a terminal screen; a good example of the use of these functions is the menu displayed during the kernel's **make menuconfig**
`libform` |  Contains functions to implement forms
`libmenu` |  Contains functions to implement menus
`libpanel` |  Contains functions to implement panels
##  6.22. Readline-5.0
The Readline package is a set of libraries that offers command-line editing and history capabilities.
**Approximate build time:** 0.11 SBU
**Required disk space:** 9.1 MB
**Installation depends on:** Binutils, Coreutils, Diffutils, Gawk, GCC, Glibc, Grep, Make, Ncurses, and Sed
###  6.22.1. Installation of Readline
The following patch includes a fix for a problem where Readline sometimes only shows 33 characters on a line and then wraps to the next line. It also includes other fixes recommended by the Readline author.
```
`patch -Np1 -i ../readline-5.0-fixes-1.patch`
```

Prepare Readline for compilation:
```
`./configure --prefix=/usr --libdir=/lib`
```

Compile the package:
```
`make SHLIB_XLDFLAGS=-lncurses`
```

The meaning of the make option:

_`SHLIB_XLDFLAGS=-lncurses`_

This option forces Readline to link against the `libncurses` library.
Install the package:
```
`make install`
```

Give Readline's dynamic libraries more appropriate permissions:
```
`chmod -v 755 /lib/lib{readline,history}.so*`
```

Now move the static libraries to a more appropriate location:
```
`mv -v /lib/lib{readline,history}.a /usr/lib`
```

Next, remove the `.so` files in `/lib` and relink them into `/usr/lib`.
```
`rm -v /lib/lib{readline,history}.so
ln -sfv ../../lib/libreadline.so.5 /usr/lib/libreadline.so
ln -sfv ../../lib/libhistory.so.5 /usr/lib/libhistory.so`
```

###  6.22.2. Contents of Readline
**Installed libraries:** libhistory.[a,so], and libreadline.[a,so]
###  Short Descriptions
`libhistory` |  Provides a consistent user interface for recalling lines of history
---|---
`libreadline` |  Aids in the consistency of user interface across discrete programs that need to provide a command line interface
##  6.23. Vim-6.3
The Vim package contains a powerful text editor.
**Approximate build time:** 0.4 SBU
**Required disk space:** 38.0 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Glibc, Grep, Make, Ncurses, and Sed
###  Alternatives to Vim
If you prefer another editor—such as Emacs, Joe, or Nano—please refer to
###  6.23.1. Installation of Vim
First, unpack both `vim-6.3.tar.bz2` and (optionally) `vim-6.3-lang.tar.gz` archives into the same directory. Then, change the default location of the `vimrc` configuration file to `/etc`:
```
`echo '#define SYS_VIMRC_FILE "/etc/vimrc"' >> src/feature.h`
```

Vim has two known security vulnerabilities that have already been addressed upstream. The following patch fixes the problems:
```
`patch -Np1 -i ../vim-6.3-security_fix-2.patch`
```

Now prepare Vim for compilation:
```
`./configure --prefix=/usr --enable-multibyte`
```

The meaning of the configure options:

_`--enable-multibyte`_

This optional but highly recommended switch enables support for editing files in multibyte character encodings. This is needed if using a locale with a multibyte character set. This switch is also helpful to be able to edit text files initially created in Linux distributions like Fedora Core that use UTF-8 as a default character set.
Compile the package:
```
`make`
```

To test the results, issue: **`make test`**. However, this test suite outputs a lot of binary data to the screen, which can cause issues with the settings of the current terminal. This can be resolved by redirecting the output to a log file.
Install the package:
```
`make install`
```

Many users are used to using **vi** instead of **vim**. To allow execution of **vim** when users habitually enter **vi** , create a symlink:
```
`ln -sv vim /usr/bin/vi`
```

If an X Window System is going to be installed on the LFS system, it may be necessary to recompile Vim after installing X. Vim comes with a GUI version of the editor that requires X and some additional libraries to be installed. For more information on this process, refer to the Vim documentation and the Vim installation page in the BLFS book at
###  6.23.2. Configuring Vim
By default, **vim** runs in vi-incompatible mode. This may be new to users who have used other editors in the past. The “nocompatible” setting is included below to highlight the fact that a new behavior is being used. It also reminds those who would change to “compatible” mode that it should be the first setting in the configuration file. This is necessary because it changes other settings, and overrides must come after this setting. Create a default **vim** configuration file by running the following:
```
`cat > /etc/vimrc << "EOF"
`" Begin /etc/vimrc

set nocompatible
set backspace=2
syntax on
if (&term == "iterm") || (&term == "putty")
  set background=dark
endif

" End /etc/vimrc`
EOF`
```

The _`set nocompatible`_ makes **vim** behave in a more useful way (the default) than the vi-compatible manner. Remove the “no” to keep the old **vi** behavior. The _`set backspace=2`_ allows backspacing over line breaks, autoindents, and the start of insert. The _`syntax on`_ enables vim's syntax highlighting. Finally, the _if_ statement with the _`set background=dark`_ corrects **vim** 's guess about the background color of some terminal emulators. This gives the highlighting a better color scheme for use on the black background of these programs.
Documentation for other available options can be obtained by running the following command:
```
`vim -c ':options'`
```

###  6.23.3. Contents of Vim
**Installed programs:** efm_filter.pl, efm_perl.pl, ex (link to vim), less.sh, mve.awk, pltags.pl, ref, rview (link to vim), rvim (link to vim), shtags.pl, tcltags, vi (link to vim), view (link to vim), vim, vim132, vim2html.pl, vimdiff (link to vim), vimm, vimspell.sh, vimtutor, and xxd
###  Short Descriptions
**efm_filter.pl** |  A filter for creating an error file that can be read by **vim**
---|---
**efm_perl.pl** |  Reformats the error messages of the Perl interpreter for use with the “quickfix” mode of **vim**
**ex** |  Starts **vim** in ex mode
**less.sh** |  A script that starts **vim** with less.vim
**mve.awk** |  Processes **vim** errors
**pltags.pl** |  Creates a tags file for Perl code for use by **vim**
**ref** |  Checks the spelling of arguments
**rview** |  Is a restricted version of **view** ; no shell commands can be started and **view** cannot be suspended
**rvim** |  Is a restricted version of **vim** ; no shell commands can be started and **vim** cannot be suspended
**shtags.pl** |  Generates a tags file for Perl scripts
**tcltags** |  Generates a tags file for TCL code
**view** |  Starts **vim** in read-only mode
**vi** |  Is the editor
**vim** |  Is the editor
**vim132** |  Starts **vim** with the terminal in 132-column mode
**vim2html.pl** |  Converts Vim documentation to HypterText Markup Language (HTML)
**vimdiff** |  Edits two or three versions of a file with **vim** and show differences
**vimm** |  Enables the DEC locator input model on a remote terminal
**vimspell.sh** |  Spell checks a file and generates the syntax statements necessary to highlight in **vim**. This script requires the old Unix **spell** command, which is provided neither in LFS nor in BLFS
**vimtutor** |  Teaches the basic keys and commands of **vim**
**xxd** |  Creates a hex dump of the given file; it can also do the reverse, so it can be used for binary patching
##  6.24. M4-1.4.3
The M4 package contains a macro processor.
**Approximate build time:** 0.1 SBU
**Required disk space:** 2.8 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Gettext, Glibc, Grep, Make, Perl, and Sed
###  6.24.1. Installation of M4
Prepare M4 for compilation:
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

###  6.24.2. Contents of M4
**Installed program:** m4
###  Short Descriptions
**m4** |  copies the given files while expanding the macros that they contain. These macros are either built-in or user-defined and can take any number of arguments. Besides performing macro expansion, **m4** has built-in functions for including named files, running Unix commands, performing integer arithmetic, manipulating text, recursion, etc. The **m4** program can be used either as a front-end to a compiler or as a macro processor in its own right.
---|---
##  6.25. Bison-2.0
The Bison package contains a parser generator.
**Approximate build time:** 0.6 SBU
**Required disk space:** 9.9 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Gettext, Glibc, Grep, M4, Make, and Sed
###  6.25.1. Installation of Bison
Prepare Bison for compilation:
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

###  6.25.2. Contents of Bison
**Installed programs:** bison and yacc
**Installed library:** liby.a
###  Short Descriptions
**bison** |  Generates, from a series of rules, a program for analyzing the structure of text files; Bison is a replacement for Yacc (Yet Another Compiler Compiler)
---|---
**yacc** |  A wrapper for **bison** , meant for programs that still call **yacc** instead of **bison** ; it calls **bison** with the _`-y`_ option
`liby.a` |  The Yacc library containing implementations of Yacc-compatible _yyerror_ and _main_ functions; this library is normally not very useful, but POSIX requires it
##  6.26. Less-382
The Less package contains a text file viewer.
**Approximate build time:** 0.1 SBU
**Required disk space:** 2.3 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Glibc, Grep, Make, Ncurses, and Sed
###  6.26.1. Installation of Less
Prepare Less for compilation:
```
`./configure --prefix=/usr --bindir=/bin --sysconfdir=/etc`
```

The meaning of the configure options:

_`--sysconfdir=/etc`_

This option tells the programs created by the package to look in `/etc` for the configuration files.
Compile the package:
```
`make`
```

Install the package:
```
`make install`
```

###  6.26.2. Contents of Less
**Installed programs:** less, lessecho, and lesskey
###  Short Descriptions
**less** |  A file viewer or pager; it displays the contents of the given file, letting the user scroll, find strings, and jump to marks
---|---
**lessecho** |  Needed to expand meta-characters, such as _*_ and _?_ , in filenames on Unix systems
**lesskey** |  Used to specify the key bindings for **less**
##  6.27. Groff-1.19.1
The Groff package contains programs for processing and formatting text.
**Approximate build time:** 0.5 SBU
**Required disk space:** 38.7 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, Gawk, GCC, Glibc, Grep, Make, and Sed
###  6.27.1. Installation of Groff
Groff expects the environment variable `PAGE` to contain the default paper size. For users in the United States, _`PAGE=letter`_ is appropriate. Elsewhere, _`PAGE=A4`_ may be more suitable.
Prepare Groff for compilation:
```
`PAGE=_`[paper_size]`_ ./configure --prefix=/usr`
```

Compile the package:
```
`make`
```

Install the package:
```
`make install`
```

Some documentation programs, such as **xman** , will not work properly without the following symlinks:
```
`ln -sv soelim /usr/bin/zsoelim
ln -sv eqn /usr/bin/geqn
ln -sv tbl /usr/bin/gtbl`
```

###  6.27.2. Contents of Groff
**Installed programs:** addftinfo, afmtodit, eqn, eqn2graph, geqn (link to eqn), grn, grodvi, groff, groffer, grog, grolbp, grolj4, grops, grotty, gtbl (link to tbl), hpftodit, indxbib, lkbib, lookbib, mmroff, neqn, nroff, pfbtops, pic, pic2graph, post-grohtml, pre-grohtml, refer, soelim, tbl, tfmtodit, troff, and zsoelim (link to soelim)
###  Short Descriptions
**addftinfo** |  Reads a troff font file and adds some additional font-metric information that is used by the **groff** system
---|---
**afmtodit** |  Creates a font file for use with **groff** and **grops**
**eqn** |  Compiles descriptions of equations embedded within troff input files into commands that are understood by **troff**
**eqn2graph** |  Converts a troff EQN (equation) into a cropped image
**geqn** |  A link to **eqn**
**grn** |  A **groff** preprocessor for gremlin files
**grodvi** |  A driver for **groff** that produces TeX dvi format
**groff** |  A front-end to the groff document formatting system; normally, it runs the **troff** program and a post-processor appropriate for the selected device
**groffer** |  Displays groff files and man pages on X and tty terminals
**grog** |  Reads files and guesses which of the **groff** options _`-e`_ , _`-man`_ , _`-me`_ , _`-mm`_ , _`-ms`_ , _`-p`_ , _`-s`_ , and _`-t`_ are required for printing files, and reports the **groff** command including those options
**grolbp** |  Is a **groff** driver for Canon CAPSL printers (LBP-4 and LBP-8 series laser printers)
**grolj4** |  Is a driver for **groff** that produces output in PCL5 format suitable for an HP LaserJet 4 printer
**grops** |  Translates the output of GNU **troff** to PostScript
**grotty** |  Translates the output of GNU **troff** into a form suitable for typewriter-like devices
**gtbl** |  A link to **tbl**
**hpftodit** |  Creates a font file for use with **groff -Tlj4** from an HP-tagged font metric file
**indxbib** |  Creates an inverted index for the bibliographic databases with a specified file for use with **refer** , **lookbib** , and **lkbib**
**lkbib** |  Searches bibliographic databases for references that contain specified keys and reports any references found
**lookbib** |  Prints a prompt on the standard error (unless the standard input is not a terminal), reads a line containing a set of keywords from the standard input, searches the bibliographic databases in a specified file for references containing those keywords, prints any references found on the standard output, and repeats this process until the end of input
**mmroff** |  A simple preprocessor for **groff**
**neqn** |  Formats equations for American Standard Code for Information Interchange (ASCII) output
**nroff** |  A script that emulates the **nroff** command using **groff**
**pfbtops** |  Translates a PostScript font in `.pfb` format to ASCII
**pic** |  Compiles descriptions of pictures embedded within troff or TeX input files into commands understood by TeX or **troff**
**pic2graph** |  Converts a PIC diagram into a cropped image
**post-grohtml** |  Translates the output of GNU **troff** to HTML
**pre-grohtml** |  Translates the output of GNU **troff** to HTML
**refer** |  Copies the contents of a file to the standard output, except that lines between _.[_ and _.]_ are interpreted as citations, and lines between _.R1_ and _.R2_ are interpreted as commands for how citations are to be processed
