
   Installed programs: addftinfo, afmtodit, eqn, eqn2graph, geqn (link to
   eqn), grn, grodvi, groff, groffer, grog, grolbp, grolj4, grops,
   grotty, gtbl (link to tbl), hpftodit, indxbib, lkbib, lookbib, mmroff,
   neqn, nroff, pfbtops, pic, pic2graph, post-grohtml, pre-grohtml,
   refer, soelim, tbl, tfmtodit, troff, and zsoelim (link to soelim)

Short Descriptions

   addftinfo

   Reads a troff font file and adds some additional font-metric
   information that is used by the groff system
   afmtodit

   Creates a font file for use with groff and grops
   eqn

   Compiles descriptions of equations embedded within troff input files
   into commands that are understood by troff
   eqn2graph

   Converts a troff EQN (equation) into a cropped image
   geqn

   A link to eqn
   grn

   A groff preprocessor for gremlin files
   grodvi

   A driver for groff that produces TeX dvi format
   groff

   A front-end to the groff document formatting system; normally, it runs
   the troff program and a post-processor appropriate for the selected
   device
   groffer

   Displays groff files and man pages on X and tty terminals
   grog

   Reads files and guesses which of the groff options -e, -man, -me, -mm,
   -ms, -p, -s, and -t are required for printing files, and reports the
   groff command including those options
   grolbp

   Is a groff driver for Canon CAPSL printers (LBP-4 and LBP-8 series
   laser printers)
   grolj4

   Is a driver for groff that produces output in PCL5 format suitable for
   an HP LaserJet 4 printer
   grops

   Translates the output of GNU troff to PostScript
   grotty

   Translates the output of GNU troff into a form suitable for
   typewriter-like devices
   gtbl

   A link to tbl
   hpftodit

   Creates a font file for use with groff -Tlj4 from an HP-tagged font
   metric file
   indxbib

   Creates an inverted index for the bibliographic databases with a
   specified file for use with refer, lookbib, and lkbib
   lkbib

   Searches bibliographic databases for references that contain specified
   keys and reports any references found
   lookbib

   Prints a prompt on the standard error (unless the standard input is
   not a terminal), reads a line containing a set of keywords from the
   standard input, searches the bibliographic databases in a specified
   file for references containing those keywords, prints any references
   found on the standard output, and repeats this process until the end
   of input
   mmroff

   A simple preprocessor for groff
   neqn

   Formats equations for American Standard Code for Information
   Interchange (ASCII) output
   nroff

   A script that emulates the nroff command using groff
   pfbtops

   Translates a PostScript font in .pfb format to ASCII
   pic

   Compiles descriptions of pictures embedded within troff or TeX input
   files into commands understood by TeX or troff
   pic2graph

   Converts a PIC diagram into a cropped image
   post-grohtml

   Translates the output of GNU troff to HTML
   pre-grohtml

   Translates the output of GNU troff to HTML
   refer

   Copies the contents of a file to the standard output, except that
   lines between .[ and .] are interpreted as citations, and lines
   between .R1 and .R2 are interpreted as commands for how citations are
   to be processed
   soelim

   Reads files and replaces lines of the form .so file by the contents of
   the mentioned file
   tbl

   Compiles descriptions of tables embedded within troff input files into
   commands that are understood by troff
   tfmtodit

   Creates a font file for use with groff -Tdvi
   troff

   Is highly compatible with Unix troff; it should usually be invoked
   using the groff command, which will also run preprocessors and
   post-processors in the appropriate order and with the appropriate
   options
   zsoelim

   A link to soelim

6.28. Sed-4.1.4

   The Sed package contains a stream editor.
   Approximate build time: 0.2 SBU
   Required disk space: 8.4 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, and Texinfo

6.28.1. Installation of Sed

   By default, Sed installs its HTML documentation in /usr/share/doc.
   Alter this to /usr/share/doc/sed-4.1.4 by applying the following sed:
sed -i 's@/doc@&/sed-4.1.4@' doc/Makefile.in

   Prepare Sed for compilation:
./configure --prefix=/usr --bindir=/bin

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

6.28.2. Contents of Sed

   Installed program: sed

Short Descriptions

   sed

   Filters and transforms text files in a single pass

6.29. Flex-2.5.31

   The Flex package contains a utility for generating programs that
   recognize patterns in text.
   Approximate build time: 0.1 SBU
   Required disk space: 22.5 MB
   Installation depends on: Bash, Binutils, Bison, Coreutils, Diffutils,
   GCC, Gettext, Glibc, Grep, M4, Make, and Sed

6.29.1. Installation of Flex

   Flex contains several known bugs. Fix these with the following patch:
patch -Np1 -i ../flex-2.5.31-debian_fixes-3.patch

   The GNU autotools detects that the Flex source code has been modified
   by the previous patch and tries to update the man page accordingly.
   This does not work correctly on many systems, and the default page is
   fine, so make sure it does not get regenerated:
touch doc/flex.1

   Prepare Flex for compilation:
./configure --prefix=/usr

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

   There are some packages that expect to find the lex library in
   /usr/lib. Create a symlink to account for this:
ln -sv libfl.a /usr/lib/libl.a

   A few programs do not know about flex yet and try to run its
   predecessor, lex. To support those programs, create a wrapper script
   named lex that calls flex in lex emulation mode:
cat > /usr/bin/lex << "EOF"
#!/bin/sh
# Begin /usr/bin/lex

exec /usr/bin/flex -l "$@"

# End /usr/bin/lex
EOF
chmod -v 755 /usr/bin/lex

6.29.2. Contents of Flex

   Installed programs: flex and lex
   Installed library: libfl.a

Short Descriptions

   flex

   A tool for generating programs that recognize patterns in text; it
   allows for the versatility to specify the rules for pattern-finding,
   eradicating the need to develop a specialized program
   lex

   A script that runs flex in lex emulation mode
   libfl.a

   The flex library

6.30. Gettext-0.14.3

   The Gettext package contains utilities for internationalization and
   localization. These allow programs to be compiled with NLS (Native
   Language Support), enabling them to output messages in the user's
   native language.
   Approximate build time: 1.2 SBU
   Required disk space: 65.1 MB
   Installation depends on: Bash, Binutils, Bison, Coreutils, Diffutils,
   Gawk, GCC, Glibc, Grep, Make, and Sed

6.30.1. Installation of Gettext

   Prepare Gettext for compilation:
./configure --prefix=/usr

   Compile the package:
make

   To test the results, issue: make check. This takes a very long time,
   around 7 SBUs.

   Install the package:
make install

6.30.2. Contents of Gettext

   Installed programs: autopoint, config.charset, config.rpath, envsubst,
   gettext, gettextize, hostname, msgattrib, msgcat, msgcmp, msgcomm,
   msgconv, msgen, msgexec, msgfilter, msgfmt, msggrep, msginit,
   msgmerge, msgunfmt, msguniq, ngettext, and xgettext
   Installed libraries: libasprintf.[a,so], libgettextlib.so,
   libgettextpo.[a,so], and libgettextsrc.so

Short Descriptions

   autopoint

   Copies standard Gettext infrastructure files into a source package
   config.charset

   Outputs a system-dependent table of character encoding aliases
   config.rpath

   Outputs a system-dependent set of variables, describing how to set the
   runtime search path of shared libraries in an executable
   envsubst

   Substitutes environment variables in shell format strings
   gettext

   Translates a natural language message into the user's language by
   looking up the translation in a message catalog
   gettextize

   Copies all standard Gettext files into the given top-level directory
   of a package to begin internationalizing it
   hostname

   Displays a network hostname in various forms
   msgattrib

   Filters the messages of a translation catalog according to their
   attributes and manipulates the attributes
   msgcat

   Concatenates and merges the given .po files
   msgcmp

   Compares two .po files to check that both contain the same set of
   msgid strings
   msgcomm

   Finds the messages that are common to to the given .po files
   msgconv

   Converts a translation catalog to a different character encoding
   msgen

   Creates an English translation catalog
   msgexec

   Applies a command to all translations of a translation catalog
   msgfilter

   Applies a filter to all translations of a translation catalog
   msgfmt

   Generates a binary message catalog from a translation catalog
   msggrep

   Extracts all messages of a translation catalog that match a given
   pattern or belong to some given source files
   msginit

   Creates a new .po file, initializing the meta information with values
   from the user's environment
   msgmerge

   Combines two raw translations into a single file
   msgunfmt

   Decompiles a binary message catalog into raw translation text
   msguniq

   Unifies duplicate translations in a translation catalog
   ngettext

   Displays native language translations of a textual message whose
   grammatical form depends on a number
   xgettext

   Extracts the translatable message lines from the given source files to
   make the first translation template
   libasprintf

   defines the autosprintf class, which makes C formatted output routines
   usable in C++ programs, for use with the <string> strings and the
   <iostream> streams
   libgettextlib

   a private library containing common routines used by the various
   Gettext programs; these are not intended for general use
   libgettextpo

   Used to write specialized programs that process .po files; this
   library is used when the standard applications shipped with Gettext
   (such as msgcomm, msgcmp, msgattrib, and msgen) will not suffice
   libgettextsrc

   A private library containing common routines used by the various
   Gettext programs; these are not intended for general use

6.31. Inetutils-1.4.2

   The Inetutils package contains programs for basic networking.
   Approximate build time: 0.2 SBU
   Required disk space: 8.7 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, Grep, Make, Ncurses, and Sed

6.31.1. Installation of Inetutils

   Inetutils has issues with the Linux 2.6 kernel series. Fix these
   issues by applying the following patch:
patch -Np1 -i ../inetutils-1.4.2-kernel_headers-1.patch

   All programs that come with Inetutils will not be installed. However,
   the Inetutils build system will insist on installing all the man pages
   anyway. The following patch will correct this situation:
patch -Np1 -i ../inetutils-1.4.2-no_server_man_pages-1.patch

   Prepare Inetutils for compilation:
./configure --prefix=/usr --libexecdir=/usr/sbin \
    --sysconfdir=/etc --localstatedir=/var \
    --disable-logger --disable-syslogd \
    --disable-whois --disable-servers

   The meaning of the configure options:

   --disable-logger
          This option prevents Inetutils from installing the logger
          program, which is used by scripts to pass messages to the
          System Log Daemon. Do not install it because Util-linux
          installs a better version later.

   --disable-syslogd
          This option prevents Inetutils from installing the System Log
          Daemon, which is installed with the Sysklogd package.

   --disable-whois
          This option disables the building of the Inetutils whois
          client, which is out of date. Instructions for a better whois
          client are in the BLFS book.

   --disable-servers
          This disables the installation of the various network servers
          included as part of the Inetutils package. These servers are
          deemed not appropriate in a basic LFS system. Some are insecure
          by nature and are only considered safe on trusted networks.
          More information can be found at
          [476]http://www.linuxfromscratch.org/blfs/view/svn/basicnet/ine
          tutils.html. Note that better replacements are available for
          many of these servers.

   Compile the package:
make

   Install the package:
make install

   Move the ping program to its FHS-compliant place:
mv -v /usr/bin/ping /bin

6.31.2. Contents of Inetutils

   Installed programs: ftp, ping, rcp, rlogin, rsh, talk, telnet, and
   tftp

Short Descriptions

   ftp

   Is the file transfer protocol program
   ping

   Sends echo-request packets and reports how long the replies take
   rcp

   Performs remote file copy
   rlogin

   Performs remote login
   rsh

   Runs a remote shell
   talk

   Is used to chat with another user
   telnet

   An interface to the TELNET protocol
   tftp

   A trivial file transfer program

6.32. IPRoute2-2.6.11-050330

   The IPRoute2 package contains programs for basic and advanced
   IPV4-based networking.
   Approximate build time: 0.1 SBU
   Required disk space: 4.3 MB
   Installation depends on: GCC, Glibc, Make, Linux-Headers, and Sed

6.32.1. Installation of IPRoute2

   The arpd binary included in this package is dependent on Berkeley DB.
   Because arpd is not a very common requirement on a base Linux system,
   remove the dependency on Berkeley DB by applying the sed command
   below. If the arpd binary is needed, instructions for compiling
   Berkeley DB can be found in the BLFS Book at
   [477]http://www.linuxfromscratch.org/blfs/view/svn/server/databases.ht
   ml#db.
sed -i '/^TARGETS/s@arpd@@g' misc/Makefile

   Prepare IPRoute2 for compilation:
./configure

   Compile the package:
make SBINDIR=/sbin

   The meaning of the make option:

   SBINDIR=/sbin
          This ensures that the IPRoute2 binaries will install into
          /sbin. This is the correct location according to the FHS,
          because some of the IPRoute2 binaries are used by the
          LFS-Bootscripts package.

   Install the package:
make SBINDIR=/sbin install

6.32.2. Contents of IPRoute2

   Installed programs: ctstat (link to lnstat), ifcfg, ifstat, ip,
   lnstat, nstat, routef, routel, rtacct, rtmon, rtpr, rtstat (link to
   lnstat), ss, and tc.

Short Descriptions

   ctstat

   Connection status utility
   ifcfg

   A shell script wrapper for the ip command
   ifstat

   Shows the interface statistics, including the amount of transmitted
   and received packets by interface
   ip

   The main executable. It has several different functions:

   ip link [device] allows users to look at the state of devices and to
   make changes

   ip addr allows users to look at addresses and their properties, add
   new addresses, and delete old ones

   ip neighbor allows users to look at neighbor bindings and their
   properties, add new neighbor entries, and delete old ones

   ip rule allows users to look at the routing policies and change them

   ip route allows users to look at the routing table and change routing
   table rules

   ip tunnel allows users to look at the IP tunnels and their properties,
   and change them

   ip maddr allows users to look at the multicast addresses and their
   properties, and change them

   ip mroute allows users to set, change, or delete the multicast routing

   ip monitor allows users to continuously monitor the state of devices,
   addresses and routes
   lnstat

   Provides Linux network statistics. It is a generalized and more
   feature-complete replacement for the old rtstat program
   nstat

   Shows network statistics
   routef

   A component of ip route. This is for flushing the routing tables
   routel

   A component of ip route. This is for listing the routing tables
   rtacct

   Displays the contents of /proc/net/rt_acct
   rtmon

   Route monitoring utility
   rtpr

   Converts the output of ip -o back into a readable form
   rtstat

   Route status utility
   ss

   Similar to the netstat command; shows active connections
   tc

   Traffic Controlling Executable; this is for Quality Of Service (QOS)
   and Class Of Service (COS) implementations

   tc qdisc allows users to setup the queueing discipline

   tc class allows users to setup classes based on the queuing discipline
   scheduling

   tc estimator allows users to estimate the network flow into a network

   tc filter allows users to setup the QOS/COS packet filtering

   tc policy allows users to setup the QOS/COS policies

6.33. Perl-5.8.7

   The Perl package contains the Practical Extraction and Report
   Language.
   Approximate build time: 4.1 SBU
   Required disk space: 140 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, Gawk,
   GCC, Glibc, Grep, Make, and Sed

6.33.1. Installation of Perl

   To have full control over the way Perl is set up, run the interactive
   Configure script and hand-pick the way this package is built. If the
   defaults it auto-detects are suitable, prepare Perl for compilation
   with:
./configure.gnu --prefix=/usr -Dpager="/bin/less -isR"

   The meaning of the configure options:

   -Dpager="/bin/less -isR"
          This corrects an error in the way that perldoc invokes the less
          program.

   Compile the package:
make

   To run the test suite, first create a basic /etc/hosts file which is
   needed by a couple of the tests to resolve the network name localhost:
echo "127.0.0.1 localhost $(hostname)" > /etc/hosts

   Now run the tests, if desired:
make test

   Install the package:
make install

6.33.2. Contents of Perl

   Installed programs: a2p, c2ph, dprofpp, enc2xs, find2perl, h2ph, h2xs,
   libnetcfg, perl, perl5.8.7 (link to perl), perlbug, perlcc, perldoc,
   perlivp, piconv, pl2pm, pod2html, pod2latex, pod2man, pod2text,
   pod2usage, podchecker, podselect, psed (link to s2p), pstruct (link to
   c2ph), s2p, splain, and xsubpp
   Installed libraries: Several hundred which cannot all be listed here

Short Descriptions

   a2p

   Translates awk to Perl
   c2ph

   Dumps C structures as generated from cc -g -S
   dprofpp

   Displays Perl profile data
   en2cxs

   Builds a Perl extension for the Encode module from either Unicode
   Character Mappings or Tcl Encoding Files
   find2perl

   Translates find commands to Perl
   h2ph

   Converts .h C header files to .ph Perl header files
   h2xs

   Converts .h C header files to Perl extensions
   libnetcfg

   Can be used to configure the libnet
   perl

   Combines some of the best features of C, sed, awk and sh into a single
   swiss-army language
   perl5.8.7

   A hard link to perl
   perlbug

   Used to generate bug reports about Perl, or the modules that come with
   it, and mail them
   perlcc

   Generates executables from Perl programs
   perldoc

   Displays a piece of documentation in pod format that is embedded in
   the Perl installation tree or in a Perl script
   perlivp

   The Perl Installation Verification Procedure; it can be used to verify
   that Perl and its libraries have been installed correctly
   piconv

   A Perl version of the character encoding converter iconv
   pl2pm

   A rough tool for converting Perl4 .pl files to Perl5 .pm modules
   pod2html

   Converts files from pod format to HTML format
   pod2latex

   Converts files from pod format to LaTeX format
   pod2man

   Converts pod data to formatted *roff input
   pod2text

   Converts pod data to formatted ASCII text
   pod2usage

   Prints usage messages from embedded pod docs in files
   podchecker

   Checks the syntax of pod format documentation files
   podselect

   Displays selected sections of pod documentation
   psed

   A Perl version of the stream editor sed
   pstruct

   Dumps C structures as generated from cc -g -S stabs
   s2p

   Translates sed scripts to Perl
   splain

   Is used to force verbose warning diagnostics in Perl
   xsubpp

   Converts Perl XS code into C code

6.34. Texinfo-4.8

   The Texinfo package contains programs for reading, writing, and
   converting info pages.
   Approximate build time: 0.2 SBU
   Required disk space: 14.7 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, Ncurses, and Sed

6.34.1. Installation of Texinfo

   Texinfo allows local users to overwrite arbitrary files via a symlink
   attack on temporary files. Apply the following patch to fix this:
patch -Np1 -i ../texinfo-4.8-tempfile_fix-1.patch

   Prepare Texinfo for compilation:
./configure --prefix=/usr

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

   Optionally, install the components belonging in a TeX installation:
make TEXMF=/usr/share/texmf install-tex

   The meaning of the make parameter:

   TEXMF=/usr/share/texmf
          The TEXMF makefile variable holds the location of the root of
          the TeX tree if, for example, a TeX package will be installed
          later.

   The Info documentation system uses a plain text file to hold its list
   of menu entries. The file is located at /usr/share/info/dir.
   Unfortunately, due to occasional problems in the Makefiles of various
   packages, it can sometimes get out of sync with the info pages
   installed on the system. If the /usr/share/info/dir file ever needs to
   be recreated, the following optional commands will accomplish the
   task:
cd /usr/share/info
rm dir
for f in *
do install-info $f dir 2>/dev/null
done

6.34.2. Contents of Texinfo

   Installed programs: info, infokey, install-info, makeinfo, texi2dvi,
   texi2pdf, and texindex

Short Descriptions

   info

   Used to read info pages which are similar to man pages, but often go
   much deeper than just explaining all the available command line
   options. For example, compare man bison and info bison.
   infokey

   Compiles a source file containing Info customizations into a binary
   format
   install-info

   Used to install info pages; it updates entries in the info index file
   makeinfo

   Translates the given Texinfo source documents into info pages, plain
   text, or HTML
   texi2dvi

   Used to format the given Texinfo document into a device-independent
   file that can be printed
   texi2pdf

   Used to format the given Texinfo document into a Portable Document
   Format (PDF) file
   texindex

   Used to sort Texinfo index files

6.35. Autoconf-2.59

   The Autoconf package contains programs for producing shell scripts
   that can automatically configure source code.
   Approximate build time: 0.5 SBU
   Required disk space: 8.5 MB
   Installation depends on: Bash, Coreutils, Diffutils, Grep, M4, Make,
   Perl, and Sed

6.35.1. Installation of Autoconf

   Prepare Autoconf for compilation:
./configure --prefix=/usr

   Compile the package:
make

   To test the results, issue: make check. This takes a long time, about
   2 SBUs.

   Install the package:
make install

6.35.2. Contents of Autoconf

   Installed programs: autoconf, autoheader, autom4te, autoreconf,
   autoscan, autoupdate, and ifnames

Short Descriptions

   autoconf

   Produces shell scripts that automatically configure software source
   code packages to adapt to many kinds of Unix-like systems. The
   configuration scripts it produces are independent--running them does
   not require the autoconf program.
   autoheader

   A tool for creating template files of C #define statements for
   configure to use
   autom4te

   A wrapper for the M4 macro processor
   autoreconf

   Automatically runs autoconf, autoheader, aclocal, automake,
   gettextize, and libtoolize in the correct order to save time when
   changes are made to autoconf and automake template files
   autoscan

   Helps to create a configure.in file for a software package; it
   examines the source files in a directory tree, searching them for
   common portability issues, and creates a configure.scan file that
   serves as as a preliminary configure.in file for the package
   autoupdate

   Modifies a configure.in file that still calls autoconf macros by their
   old names to use the current macro names
   ifnames

   Helps when writing configure.in files for a software package; it
   prints the identifiers that the package uses in C preprocessor
   conditionals. If a package has already been set up to have some
   portability, this program can help determine what configure needs to
   check for. It can also fill in gaps in a configure.in file generated
   by autoscan

6.36. Automake-1.9.5

   The Automake package contains programs for generating Makefiles for
   use with Autoconf.
   Approximate build time: 0.2 SBU
   Required disk space: 8.8 MB
   Installation depends on: Autoconf, Bash, Coreutils, Diffutils, Grep,
   M4, Make, Perl, and Sed

6.36.1. Installation of Automake

   Prepare Automake for compilation:
./configure --prefix=/usr

   Compile the package:
make

   To test the results, issue: make check. This takes a long time, about
   5 SBUs.

   Install the package:
make install
