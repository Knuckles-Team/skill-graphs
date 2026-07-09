
   This file contains all the events that hotplug has called since bootup

6.48. Man-1.5p

   The Man package contains programs for finding and viewing man pages.
   Approximate build time: 0.1 SBU
   Required disk space: 2.9 MB
   Installation depends on: Bash, Binutils, Coreutils, Gawk, GCC, Glibc,
   Grep, Make, and Sed

6.48.1. Installation of Man

   Two adjustments need to be made to the sources of Man.

   The first is a sed substitution to add the -R switch to the PAGER
   variable so that escape sequences are properly handled by Less:
sed -i 's@-is@&R@g' configure

   The second is also a sed substitution to comment out the "MANPATH
   /usr/man" line in the man.conf file to prevent redundant results when
   using programs such as whatis:
sed -i 's@MANPATH./usr/man@#&@g' src/man.conf.in

   Prepare Man for compilation:
./configure -confdir=/etc

   The meaning of the configure options:

   -confdir=/etc
          This tells the man program to look for the man.conf
          configuration file in the /etc directory.

   Compile the package:
make

   Install the package:
make install

Note

   If you will be working on a terminal that does not support text
   attributes such as color and bold, you can disable Select Graphic
   Rendition (SGR) escape sequences by editing the man.conf file and
   adding the -c option to the NROFF variable. If you use multiple
   terminal types for one computer it may be better to selectively add
   the GROFF_NO_SGR environment variable for the terminals that do not
   support SGR.

   If the character set of the locale uses 8-bit characters, search for
   the line beginning with "NROFF" in /etc/man.conf, and verify that it
   matches the following:
              NROFF  /usr/bin/nroff -Tlatin1 -mandoc

   Note that "latin1" should be used even if it is not the character set
   of the locale. The reason is that, according to the specification,
   groff has no means of typesetting characters outside International
   Organization for Standards (ISO) 8859-1 without some strange escape
   codes. When formatting man pages, groff thinks that they are in the
   ISO 8859-1 encoding and this -Tlatin1 switch tells groff to use the
   same encoding for output. Since groff does no recoding of input
   characters, the formatted result is really in the same encoding as
   input, and therefore it is usable as the input for a pager.

   This does not solve the problem of a non-working man2dvi program for
   localized man pages in non-ISO 8859-1 locales. Also, it does not work
   with multibyte character sets. The first problem does not currently
   have a solution. The second issue is not of concern because the LFS
   installation does not support multibyte character sets.

   Additional information with regards to the compression of man and info
   pages can be found in the BLFS book at
   [479]http://www.linuxfromscratch.org/blfs/view/cvs/postlfs/compressdoc
   .html.

6.48.2. Contents of Man

   Installed programs: apropos, makewhatis, man, man2dvi, man2html, and
   whatis

Short Descriptions

   apropos

   Searches the whatis database and displays the short descriptions of
   system commands that contain a given string
   makewhatis

   Builds the whatis database; it reads all the man pages in the MANPATH
   and writes the name and a short description in the whatis database for
   each page
   man

   Formats and displays the requested on-line man page
   man2dvi

   Converts a man page into dvi format
   man2html

   Converts a man page into HTML
   whatis

   Searches the whatis database and displays the short descriptions of
   system commands that contain the given keyword as a separate word

6.49. Make-3.80

   The Make package contains a program for compiling packages.
   Approximate build time: 0.2 SBU
   Required disk space: 7.1 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, and Sed

6.49.1. Installation of Make

   Prepare Make for compilation:
./configure --prefix=/usr

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

6.49.2. Contents of Make

   Installed program: make

Short Descriptions

   make

   Automatically determines which pieces of a package need to be
   (re)compiled and then issues the relevant commands

6.50. Module-Init-Tools-3.1

   The Module-Init-Tools package contains programs for handling kernel
   modules in Linux kernels greater than or equal to version 2.5.47.
   Approximate build time: 0.1 SBU
   Required disk space: 4.9 MB
   Installation depends on: Bash, Binutils, Bison, Coreutils, Diffutils,
   Flex, GCC, Glibc, Grep, M4, Make, and Sed

6.50.1. Installation of Module-Init-Tools

   Module-Init-Tools attempts to rewrite its modprobe.conf man page
   during the build process. This is unnecessary and also relies on
   docbook2man -- which is not installed in LFS. Run the following
   command to avoid this:
touch modprobe.conf.5

   If you wish to run the test suite for Module-Init-Tools, you will need
   to download the separate testsuite tarball. Issue the following
   commands to perform the tests (note that the make distclean command is
   required to clean up the source tree, as the source gets recompiled as
   part of the testing process):
tar -xvf ../module-init-tools-testsuite-3.1.tar.bz2 --strip-path=1 &&
./configure &&
make check &&
make distclean

   Prepare Module-Init-Tools for compilation:
./configure --prefix="" --enable-zlib

   The meaning of the configure options:

   --enable-zlib
          This allows the Module-Init-Tools package to handle compressed
          kernel modules.

   Compile the package:
make

   Install the package:
make install

6.50.2. Contents of Module-Init-Tools

   Installed programs: depmod, insmod, insmod.static, lsmod (link to
   insmod), modinfo, modprobe (link to insmod), and rmmod (link to
   insmod)

Short Descriptions

   depmod

   Creates a dependency file based on the symbols it finds in the
   existing set of modules; this dependency file is used by modprobe to
   automatically load the required modules
   insmod

   Installs a loadable module in the running kernel
   insmod.static

   A statically compiled version of insmod
   lsmod

   Lists currently loaded modules
   modinfo

   Examines an object file associated with a kernel module and displays
   any information that it can glean
   modprobe

   Uses a dependency file, created by depmod, to automatically load
   relevant modules
   rmmod

   Unloads modules from the running kernel

6.51. Patch-2.5.4

   The Patch package contains a program for modifying or creating files
   by applying a "patch" file typically created by the diff program.
   Approximate build time: 0.1 SBU
   Required disk space: 1.5 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Glibc, Grep, Make, and Sed

6.51.1. Installation of Patch

   Prepare Patch for compilation. The preprocessor flag -D_GNU_SOURCE is
   only needed on the PowerPC platform. It can be left it out on other
   architectures:
CPPFLAGS=-D_GNU_SOURCE ./configure --prefix=/usr

   Compile the package:
make

   This package does not come with a test suite.

   Install the package:
make install

6.51.2. Contents of Patch

   Installed program: patch

Short Descriptions

   patch

   Modifies files according to a patch file. A patch file is normally a
   difference listing created with the diff program. By applying these
   differences to the original files, patch creates the patched versions.

6.52. Procps-3.2.5

   The Procps package contains programs for monitoring processes.
   Approximate build time: 0.1 SBU
   Required disk space: 2.3 MB
   Installation depends on: Bash, Binutils, Coreutils, GCC, Glibc, Make,
   and Ncurses

6.52.1. Installation of Procps

   Compile the package:
make

   Install the package:
make install

6.52.2. Contents of Procps

   Installed programs: free, kill, pgrep, pkill, pmap, ps, skill, snice,
   sysctl, tload, top, uptime, vmstat, w, and watch
   Installed library: libproc.so

Short Descriptions

   free

   Reports the amount of free and used memory (both physical and swap
   memory) in the system
   kill

   Sends signals to processes
   pgrep

   Looks up processes based on their name and other attributes
   pkill

   Signals processes based on their name and other attributes
   pmap

   Reports the memory map of the given process
   ps

   Lists the current running processes
   skill

   Sends signals to processes matching the given criteria
   snice

   Changes the scheduling priority of processes matching the given
   criteria
   sysctl

   Modifies kernel parameters at run time
   tload

   Prints a graph of the current system load average
   top

   Displays a list of the most CPU intensive processes; it provides an
   ongoing look at processor activity in real time
   uptime

   Reports how long the system has been running, how many users are
   logged on, and the system load averages
   vmstat

   Reports virtual memory statistics, giving information about processes,
   memory, paging, block Input/Output (IO), traps, and CPU activity
   w

   Shows which users are currently logged on, where, and since when
   watch

   Runs a given command repeatedly, displaying the first screen-full of
   its output; this allows a user to watch the output change over time
   libproc

   Contains the functions used by most programs in this package

6.53. Psmisc-21.6

   The Psmisc package contains programs for displaying information about
   running processes.
   Approximate build time: 0.1 SBU
   Required disk space: 1.7 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, Ncurses, and Sed

6.53.1. Installation of Psmisc

   Prepare Psmisc for compilation:
./configure --prefix=/usr --exec-prefix=""

   The meaning of the configure options:

   --exec-prefix=""
          This ensures that the Psmisc binaries will install into /bin
          instead of /usr/bin. This is the correct location according to
          the FHS, because some of the Psmisc binaries are used by the
          LFS-Bootscripts package.

   Compile the package:
make

   Install the package:
make install

   There is no reason for the pstree and pstree.x11 programs to reside in
   /bin. Therefore, move them to /usr/bin:
mv -v /bin/pstree* /usr/bin

   By default, Psmisc's pidof program is not installed. This usually is
   not a problem because it is installed later in the Sysvinit package,
   which provides a better pidof program. If Sysvinit will not be used
   for a particular system, complete the installation of Psmisc by
   creating the following symlink:
ln -sv killall /bin/pidof

6.53.2. Contents of Psmisc

   Installed programs: fuser, killall, pstree, and pstree.x11 (link to
   pstree)

Short Descriptions

   fuser

   Reports the Process IDs (PIDs) of processes that use the given files
   or file systems
   killall

   Kills processes by name; it sends a signal to all processes running
   any of the given commands
   pstree

   Displays running processes as a tree
   pstree.x11

   Same as pstree, except that it waits for confirmation before exiting

6.54. Shadow-4.0.9

   The Shadow package contains programs for handling passwords in a
   secure way.
   Approximate build time: 0.4 SBU
   Required disk space: 13.7 MB
   Installation depends on: Bash, Binutils, Bison, Coreutils, Diffutils,
   GCC, Gettext, Glibc, Grep, Make, and Sed

6.54.1. Installation of Shadow

Note

   If you would like to enforce the use of strong passwords, refer to
   [480]http://www.linuxfromscratch.org/blfs/view/svn/postlfs/cracklib.ht
   ml for installing Cracklib prior to building Shadow. Then add
   --with-libcrack to the configure command below.

   Prepare Shadow for compilation:
./configure --libdir=/lib --enable-shared

   Disable the installation of the groups program and its man page, as
   Coreutils provides a better version:
sed -i 's/groups$(EXEEXT) //' src/Makefile
sed -i '/groups/d' man/Makefile

   Compile the package:
make

   Install the package:
make install

   Shadow uses two files to configure authentication settings for the
   system. Install these two configuration files:
cp -v etc/{limits,login.access} /etc

   Instead of using the default crypt method, use the more secure MD5
   method of password encryption, which also allows passwords longer than
   8 characters. It is also necessary to change the obsolete
   /var/spool/mail location for user mailboxes that Shadow uses by
   default to the /var/mail location used currently. Both of these can be
   accomplished by changing the relevant configuration file while copying
   it to its destination:

Note

   If you built Shadow with Cracklib support, insert the following into
   the sed given below:
-e 's@DICTPATH.*@DICTPATH\t/lib/cracklib/pw_dict@'

sed -e's@#MD5_CRYPT_ENAB.no@MD5_CRYPT_ENAB yes@' \
    -e 's@/var/spool/mail@/var/mail@' \
    etc/login.defs.linux > /etc/login.defs

   Move a misplaced program to its proper location:
mv -v /usr/bin/passwd /bin

   Move Shadow's libraries to more appropriate locations:
mv -v /lib/libshadow.*a /usr/lib
rm -v /lib/libshadow.so
ln -sfv ../../lib/libshadow.so.0 /usr/lib/libshadow.so

   The -D option of the useradd program requires the /etc/default
   directory for it to work properly:
mkdir -v /etc/default

6.54.2. Configuring Shadow

   This package contains utilities to add, modify, and delete users and
   groups; set and change their passwords; and perform other
   administrative tasks. For a full explanation of what password
   shadowing means, see the doc/HOWTO file within the unpacked source
   tree. If using Shadow support, keep in mind that programs which need
   to verify passwords (display managers, FTP programs, pop3 daemons,
   etc.) must be Shadow-compliant. That is, they need to be able to work
   with shadowed passwords.

   To enable shadowed passwords, run the following command:
pwconv

   To enable shadowed group passwords, run:
grpconv

   Under normal circumstances, passwords will not have been created yet.
   However, if returning to this section later to enable shadowing, reset
   any current user passwords with the passwd command or any group
   passwords with the gpasswd command.

6.54.3. Setting the root password

   Choose a password for user root and set it by running:
passwd root

6.54.4. Contents of Shadow

   Installed programs: chage, chfn, chpasswd, chsh, expiry, faillog,
   gpasswd, groupadd, groupdel, groupmod, grpck, grpconv, grpunconv,
   lastlog, login, logoutd, mkpasswd, newgrp, newusers, passwd, pwck,
   pwconv, pwunconv, sg (link to newgrp), useradd, userdel, usermod, vigr
   (link to vipw), and vipw
   Installed libraries: libshadow.[a,so]

Short Descriptions

   chage

   Used to change the maximum number of days between obligatory password
   changes
   chfn

   Used to change a user's full name and other information
   chpasswd

   Used to update the passwords of an entire series of user accounts
   chsh

   Used to change a user's default login shell
   expiry

   Checks and enforces the current password expiration policy
   faillog

   Is used to examine the log of login failures, to set a maximum number
   of failures before an account is blocked, or to reset the failure
   count
   gpasswd

   Is used to add and delete members and administrators to groups
   groupadd

   Creates a group with the given name
   groupdel

   Deletes the group with the given name
   groupmod

   Is used to modify the given group's name or GID
   grpck

   Verifies the integrity of the group files /etc/group and /etc/gshadow
   grpconv

   Creates or updates the shadow group file from the normal group file
   grpunconv

   Updates /etc/group from /etc/gshadow and then deletes the latter
   lastlog

   Reports the most recent login of all users or of a given user
   login

   Is used by the system to let users sign on
   logoutd

   Is a daemon used to enforce restrictions on log-on time and ports
   mkpasswd

   Generates random passwords
   newgrp

   Is used to change the current GID during a login session
   newusers

   Is used to create or update an entire series of user accounts
   passwd

   Is used to change the password for a user or group account
   pwck

   Verifies the integrity of the password files /etc/passwd and
   /etc/shadow
   pwconv

   Creates or updates the shadow password file from the normal password
   file
   pwunconv

   Updates /etc/passwd from /etc/shadow and then deletes the latter
   sg

   Executes a given command while the user's GID is set to that of the
   given group
   su

   Runs a shell with substitute user and group IDs
   useradd

   Creates a new user with the given name, or updates the default
   new-user information
   userdel

   Deletes the given user account
   usermod

   Is used to modify the given user's login name, User Identification
   (UID), shell, initial group, home directory, etc.
   vigr

   Edits the /etc/group or /etc/gshadow files
   vipw

   Edits the /etc/passwd or /etc/shadow files
   libshadow

   Contains functions used by most programs in this package

6.55. Sysklogd-1.4.1

   The Sysklogd package contains programs for logging system messages,
   such as those given by the kernel when unusual things happen.
   Approximate build time: 0.1 SBU
   Required disk space: 704 KB
   Installation depends on: Binutils, Coreutils, GCC, Glibc, Make

6.55.1. Installation of Sysklogd

   The following patch fixes various issues, including a problem building
   Sysklogd with Linux 2.6 series kernels
patch -Np1 -i ../sysklogd-1.4.1-fixes-1.patch

   Compile the package:
make

   Install the package:
make install

6.55.2. Configuring Sysklogd

   Create a new /etc/syslog.conf file by running the following:
cat > /etc/syslog.conf << "EOF"
# Begin /etc/syslog.conf

auth,authpriv.* -/var/log/auth.log
*.*;auth,authpriv.none -/var/log/sys.log
daemon.* -/var/log/daemon.log
kern.* -/var/log/kern.log
mail.* -/var/log/mail.log
user.* -/var/log/user.log
*.emerg *

# log the bootscript output:
local2.* -/var/log/boot.log

# End /etc/syslog.conf
EOF

6.55.3. Contents of Sysklogd

   Installed programs: klogd and syslogd

Short Descriptions

   klogd

   A system daemon for intercepting and logging kernel messages
   syslogd

   Logs the messages that system programs offer for logging. Every logged
   message contains at least a date stamp and a hostname, and normally
   the program's name too, but that depends on how trusting the logging
   daemon is told to be

6.56. Sysvinit-2.86

   The Sysvinit package contains programs for controlling the startup,
   running, and shutdown of the system.
   Approximate build time: 0.1 SBU
   Required disk space: 1012 KB
   Installation depends on: Binutils, Coreutils, GCC, Glibc, and Make

6.56.1. Installation of Sysvinit

   When run-levels are changed (for example, when halting the system),
   init sends termination signals to those processes that init itself
   started and that should not be running in the new run-level. While
   doing this, init outputs messages like "Sending processes the TERM
   signal" which seem to imply that it is sending these signals to all
   currently running processes. To avoid this misinterpretation, modify
   the source so that these messages read like "Sending processes started
   by init the TERM signal" instead:
sed -i 's@Sending processes@& started by init@g' \
    src/init.c

   Compile the package:
make -C src

   Install the package:
make -C src install

6.56.2. Configuring Sysvinit

   Create a new file /etc/inittab by running the following:
cat > /etc/inittab << "EOF"
# Begin /etc/inittab

id:3:initdefault:

si::sysinit:/etc/rc.d/init.d/rc sysinit

l0:0:wait:/etc/rc.d/init.d/rc 0
l1:S1:wait:/etc/rc.d/init.d/rc 1
l2:2:wait:/etc/rc.d/init.d/rc 2
l3:3:wait:/etc/rc.d/init.d/rc 3
l4:4:wait:/etc/rc.d/init.d/rc 4
l5:5:wait:/etc/rc.d/init.d/rc 5
l6:6:wait:/etc/rc.d/init.d/rc 6

ca:12345:ctrlaltdel:/sbin/shutdown -t1 -a -r now

su:S016:once:/sbin/sulogin

1:2345:respawn:/sbin/agetty -I '\033(K' tty1 9600
2:2345:respawn:/sbin/agetty -I '\033(K' tty2 9600
3:2345:respawn:/sbin/agetty -I '\033(K' tty3 9600
4:2345:respawn:/sbin/agetty -I '\033(K' tty4 9600
5:2345:respawn:/sbin/agetty -I '\033(K' tty5 9600
6:2345:respawn:/sbin/agetty -I '\033(K' tty6 9600

# End /etc/inittab
EOF

   The -I '\033(K' option tells agetty to send this escape sequence to
   the terminal before doing anything else. This escape sequence switches
   the console character set to a user-defined one, which can be modified
   by running the setfont program. The console initscript from the
   LFS-Bootscripts package calls the setfont program during system
   startup. Sending this escape sequence is necessary for people who use
   non-ISO 8859-1 screen fonts, but it does not affect native English
   speakers.

6.56.3. Contents of Sysvinit

   Installed programs: halt, init, killall5, last, lastb (link to last),
   mesg, pidof (link to killall5), poweroff (link to halt), reboot (link
   to halt), runlevel, shutdown, sulogin, telinit (link to init),
   utmpdump, and wall

Short Descriptions

   halt

   Normally invokes shutdown with the -h option, except when already in
   run-level 0, then it tells the kernel to halt the system; it notes in
   the file /var/log/wtmp that the system is being brought down
   init

   The first process to be started when the kernel has initialized the
   hardware which takes over the boot process and starts all the processes
   it is instructed to
   killall5

   Sends a signal to all processes, except the processes in its own
   session so it will not kill the shell running the script that called
   it
   last

   Shows which users last logged in (and out), searching back through the
   /var/log/wtmp file; it also shows system boots, shutdowns, and
   run-level changes
   lastb

   Shows the failed login attempts, as logged in /var/log/btmp
   mesg

   Controls whether other users can send messages to the current user's
   terminal
   mountpoint

   Checks if the directory is a mountpoint
   pidof

   Reports the PIDs of the given programs
   poweroff

   Tells the kernel to halt the system and switch off the computer (see
   halt)
   reboot

   Tells the kernel to reboot the system (see halt)
   runlevel

   Reports the previous and the current run-level, as noted in the last
   run-level record in /var/run/utmp
   shutdown

   Brings the system down in a secure way, signaling all processes and
   notifying all logged-in users
   sulogin

   Allows root to log in; it is normally invoked by init when the system
   goes into single user mode
   telinit

   Tells init which run-level to change to
   utmpdump

   Displays the content of the given login file in a more user-friendly
   format
   wall

   Writes a message to all logged-in users

6.57. Tar-1.15.1

   The Tar package contains an archiving program.
   Approximate build time: 0.2 SBU
   Required disk space: 12.7 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, and Sed

6.57.1. Installation of Tar

   Tar has a bug when the -S option is used with files larger than 4 GB.
   The following patch properly fixes this issue:
patch -Np1 -i ../tar-1.15.1-sparse_fix-1.patch

   Prepare Tar for compilation:
./configure --prefix=/usr --bindir=/bin --libexecdir=/usr/sbin

   Compile the package:
make

   To test the results, issue: make check.

   Install the package:
make install

6.57.2. Contents of Tar

   Installed programs: rmt and tar

Short Descriptions

   rmt

   Remotely manipulates a magnetic tape drive through an interprocess
   communication connection
   tar

   Creates, extracts files from, and lists the contents of archives, also
   known as tarballs

6.58. Udev-056

   The Udev package contains programs for dynamic creation of device
   nodes.
   Approximate build time: 0.1 SBU
   Required disk space: 6.7 MB
   Installation depends on: Coreutils and Make

6.58.1. Installation of Udev

   Compile the package:
make udevdir=/dev

   udevdir=/dev
          This tells udev in which directory devices nodes are to be
          created.

   To test the results, issue: make test.

   Install the package:
make DESTDIR=/ udevdir=/dev install

   The meaning of the make option:

   DESTDIR=/
          This prevents the Udev build process from killing any udevd
          processes that may be running on the host system.

   Udev's configuration is far from ideal by default, so install the
   configuration files here:
cp -v ../udev-config-4.rules /etc/udev/rules.d/25-lfs.rules

   Run the udevstart program to create our full complement of device
   nodes.
/sbin/udevstart

6.58.2. Contents of Udev

   Installed programs: udev, udevd, udevsend, udevstart, udevinfo, and
   udevtest
   Installed directory: /etc/udev

Short Descriptions

   udev

   Creates device nodes in /dev or renames network interfaces (not in
   LFS) in response to hotplug events
   udevd

   A daemon that reorders hotplug events before submitting them to udev,
   thus avoiding various race conditions
   udevsend

   Delivers hotplug events to udevd
   udevstart

   Creates device nodes in /dev that correspond to drivers compiled
   directly into the kernel; it performs that task by simulating hotplug
