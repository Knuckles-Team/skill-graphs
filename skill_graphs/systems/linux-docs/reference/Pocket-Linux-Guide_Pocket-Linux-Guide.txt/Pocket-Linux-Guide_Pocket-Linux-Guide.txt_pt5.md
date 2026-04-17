7.2.4. Dependencies

Running ldd on the login program from util-linux will reveal that it is
linked to the libraries libcrypt.so.1, libc.so.6 and ld-linux.so.2. In
addition to these libraries there is another, unseen dependency on
libnss_files.so.2 and the configuration file /etc/nsswitch.conf.

The name service switch library libnss_files.so.2 and nsswitch.conf are
required for libc.so.6, and consequently the login program, to access the /
etc/passwd file. Without libnss and its configuration file, all logins will
mysteriously fail. More information about glibc's use of the name service
switch libraries can be found at [http://www.gnu.org/software/libc/manual/
html_node/Name-Service-Switch.html] http://www.gnu.org/software/libc/manual/
html_node/Name-Service-Switch.html.
-----------------------------------------------------------------------------

7.2.5. Assigning ownership and permissions

Previously, with the single user system, there was no need to worry about
permissions when installing directories, files and device nodes. The shell
was effectively operating as root, so everything was accessible. Things
become more complex with the addition of multiple user capability. Now we
need to make sure that every user has access to what they need and at the
same time gets blocked from what they do not need.

A good guideline for assigning ownership and permissions would be to give the
minimum level of access required. Take the /bin directory as an example. The
Filesystem Hierarchy (FHS) document says, "/bin contains commands that may be
used by both the system administrator and by users". From that statement we
can infer that /bin should have read and execute permission for everyone. On
the other hand, the /boot directory contains files for the boot loader.
Chances are good that regular users will not need to access anything in the /
boot directory. So the minimum level of access would be read permission for
the root user and other administrators who are members of the root group.
Normal users would have no permissions assigned on the /boot directory.

Most of the time we can assign similar permissions to all the commands in a
directory, but there are some programs that prove to be exceptions to the
rule. The su command is a good example. Other commands in the /bin directory
have a minimum requirement of read and execute, but the su command needs to
be setuid root in order to run correctly. Since it is a setuid binary, it
might not be a good idea to allow just anyone to run it. Ownership of 0:0
(root user, root group) and permissions of rwsr-x--- (octal 4750) would be a
good fit for su.

The same logic can be applied to other directories and files in the root
filesystem using the following steps:

 1. Assign ownership to the root user and root group.

 2. Set the most restrictive permissions possible.

 3. Adjust ownership and permissions on an "as needed" basis.


-----------------------------------------------------------------------------
7.3. Construction

7.3.1. Verify presence of getty and login

bash# ls ~/staging/sbin/getty
bash# ls ~/staging/bin/login
-----------------------------------------------------------------------------

7.3.2. Modify inittab for multi-user mode

Modify ~/staging/etc/inittab by changing the default runlevel and adding
getty entries as shown below.

# /etc/inittab - init daemon configuration file
#
# Default runlevel
id:2:initdefault:
#
# System initialization
si:S:sysinit:/etc/init.d/rc S
#
# Runlevel scripts
r0:0:wait:/etc/init.d/rc 0
r1:1:respawn:/bin/sh
r2:2:wait:/etc/init.d/rc 2
r3:3:wait:/etc/init.d/rc 3
r4:4:wait:/etc/init.d/rc 4
r5:5:wait:/etc/init.d/rc 5
r6:6:wait:/etc/init.d/rc 6
#
# Spawn virtual terminals
1:235:respawn:/sbin/getty 38400 tty1 linux
2:235:respawn:/sbin/getty 38400 tty2 linux
3:235:respawn:/sbin/getty 38400 tty3 linux
4:235:respawn:/sbin/getty 38400 tty4 linux
5:235:respawn:/sbin/getty 38400 tty5 linux
6:2345:respawn:/sbin/getty 38400 tty6 linux
#
# end of /etc/inittab
-----------------------------------------------------------------------------

7.3.3. Create tty devices

bash# cd ~/staging/dev
bash# mknod ~/staging/dev/tty0 c 4 0
bash# mknod ~/staging/dev/tty1 c 4 1
bash# mknod ~/staging/dev/tty2 c 4 2
bash# mknod ~/staging/dev/tty3 c 4 3
bash# mknod ~/staging/dev/tty4 c 4 4
bash# mknod ~/staging/dev/tty5 c 4 5
bash# mknod ~/staging/dev/tty6 c 4 6
bash# mknod ~/staging/dev/tty c 5 0
-----------------------------------------------------------------------------

7.3.4. Create support files in /etc

7.3.4.1. /etc/issue

Create the file ~/staging/etc/issue using the example below or design a
customized message.

Connected to \l at \b bps.

Be sure that "\l" is a lowercase letter L and not the number one.
-----------------------------------------------------------------------------

7.3.4.2. /etc/passwd

Use a text editor to create a minimal passwd file conforming to the Linux
Standards Base (LSB) document. Save the file as ~/staging/etc/passwd

root::0:0:Super User:/root:/bin/sh
bin:x:1:1:Legacy UID:/bin:/bin/false
daemon:x:2:2:Legacy UID:/sbin:/bin/false
-----------------------------------------------------------------------------

7.3.4.3. /etc/group

Use a text editor to create an LSB conforming group file and save it as ~/
staging/etc/group

root::0:root
bin:x:1:root,bin,daemon
daemon:x:2:root,bin,daemon
-----------------------------------------------------------------------------

7.3.4.4. /etc/nsswitch.conf

Create the following file and save it as ~/staging/etc/nsswitch.conf

passwd: files
group:  files
-----------------------------------------------------------------------------

7.3.5. Copy required libraries

bash# cp /lib/libnss_files.so.2 ~/staging/lib
bash# strip --strip-unneeded ~/staging/lib/*
-----------------------------------------------------------------------------

7.3.6. Set directory and file permissions

Set minimal privileges on all files and directories under ~/staging.
Everything is owned by the root user and the root group. Permissions are
read-write for the owner and read-only for the group. Exceptions to the
blanket permissions are handled case by case.

bash# cd ~/staging
bash# chown -R 0:0 ~/staging/*
bash# chmod -R 640 ~/staging/*

Set execute permission on all directories. (Note the capital "X")

bash# chmod -R +X ~/staging/*

Files in /bin are read and execute for all, but su is an exception.

bash# chmod 755 ~/staging/bin/*
bash# chmod 4750 ~/staging/bin/su

Files in /dev have various permissions. Disk devices should be accessible to
administrators only. Other files like /dev/null should have full privileges
granted to everyone.

bash# chmod 660 ~/staging/dev/fd0 dev/ram0
bash# chmod 666 ~/staging/dev/null
bash# chmod 622 ~/staging/dev/console
bash# chmod 600 ~/staging/dev/initctl
bash# chmod 622 ~/staging/dev/tty
bash# chmod 622 ~/staging/dev/tty?

The passwd and group files must be world readable.

bash# chmod 644 ~/staging/etc/passwd
bash# chmod 644 ~/staging/etc/group

The scripts in /etc/init.d are read and execute for administrators.

bash# chmod 750 ~/staging/etc/init.d/*

Libraries need read and execute permissions for everyone.

bash# chmod 755 ~/staging/lib/*

Only root should have access to the /root directory.

bash# chmod 700 ~/staging/root

Make files in /sbin read and execute for administrators.

bash# chmod 750 ~/staging/sbin/*

Temp should be read-write for all with the sticky bit set.

bash# chmod 1777 ~/staging/tmp
-----------------------------------------------------------------------------

7.3.7. Create the root disk image

bash# cd /
bash# dd if=/dev/zero of=/dev/ram7 bs=1k count=4096
bash# mke2fs -m0 /dev/ram7 4096
bash# mount /dev/ram7 /mnt
bash# cp -dpR ~/staging/* /mnt
bash# umount /dev/ram7
bash# dd if=/dev/ram7 of=~/phase6-image bs=1k count=4096
bash# gzip -9 ~/phase6-image
-----------------------------------------------------------------------------

7.3.8. Copy the image to diskette

Insert the diskette labeled "root disk" into drive fd0.

bash# dd if=~/phase6-image.gz of=/dev/fd0 bs=1k
-----------------------------------------------------------------------------

7.4. Implementation

7.4.1. System Startup

If everything goes well, the virtual console display should look similar to
the following example:

Connected to tty1 at 38400 bps.
gnu-linux login:
-----------------------------------------------------------------------------

7.4.2. Add a new user to the system

Log in as root.

Create a new, unprivileged user and new group by appending a line to the /etc
/passwd and /etc/group files, respectively. Be sure to use a double
greater-than (>>) to avoid accidentally overwriting the files.

bash# echo "floyd::501:500:User:/home/floyd:/bin/sh" >>/etc/passwd
bash# echo "users::500:" >>/etc/group
bash# mkdir /home/floyd
bash# chown floyd.users /home/floyd
bash# chmod 700 /home/floyd
-----------------------------------------------------------------------------

7.4.3. Test the new user's ability to use the system

Switch to virtual terminal tty2 by pressing ALT+F2.

Log in as floyd.

Try the following commands and verify that they work.

bash$ pwd
bash$ ls -l /
bash$ cat /etc/passwd

Try the following commands and verify that they do not work.

bash$ ls /root
bash$ /sbin/shutdown -h now
bash$ su -
-----------------------------------------------------------------------------

7.4.4. System shutdown

Switch back to tty1 where root is logged in.

bash# shutdown -h now
-----------------------------------------------------------------------------

Chapter 8. Filling in the Gaps

8.1. Analysis

The root disk has come a long way since its humble beginnings as a
statically-linked shell. It now shares many features with the popular,
ready-made distributions. For example it has:

��*�Several common utilities like cat, ls and so on.

��*�Startup scripts that automatically check and mount filesystems.

��*�Graceful shutdown capability.

��*�Support for multiple users and virtual terminals.


As a final test, we can put the root disk up against the Filesystem Hierarchy
Standard (FHS) requirements for the root filesystem. (We will ignore anything
in the /usr hierarchy because of space constraints.) Compared to FHS
requirement, the only files missing are a few commands in the /bin directory.
Specifically, the root disk lacks the following commands:

��*�more

��*�ps

��*�sed


In addition to the required commands, it might be nice to include the "ed"
editor listed as an option by the FHS. It is not as robust as vi or emacs,
but it works and it should fit onto the tiny root filesystem.

So in order to finish up this phase of the project, we need to accomplish the
following goals:

��*�Add the more, ps and sed commands.

��*�Install the optional ed editor.


-----------------------------------------------------------------------------
8.2. Design

8.2.1. more

There is a more command that comes with util-linux, but it will not work for
this project. The reason is because of library dependencies and space
constraints. The util-linux supplied more needs either the libncurses or
libtermcap to work and there just is not enough space on the root disk floppy
to fit everything in. So, in order to have a more command we will have to get
creative.

The more command is used to display a file page by page. It's a little like
having a cat command that pauses every twenty-five lines. The basic logic is
outlined below.

��*�Read one line of the file.

��*�Display the line on the screen.

��*�If 25 lines have been displayed, pause.

��*�Loop and do it again.


Of course there are some details left out like what to do if the screen
dimensions are not what we anticipated, but overall it is a fair
representation of what more does. Given this simple program logic, it should
not be hard to put together a short shell script that emulates the basic
functionality of more. The BASH(1) manpage and Adv-BASH-Scripting-Guide will
serve as references.
-----------------------------------------------------------------------------

8.2.2. More device files

The more script will need access to device files that are not on the root
disk yet. Specifically more needs to have stdin, stdout and stderr, but while
we are at it we should check for any other missing /dev files. The Linux
Standard Base requires null, zero and tty to be present in the /dev
directory. Files for null and tty already exist from previous phases of the
project, but we still need /dev/zero. We can refer to devices.txt in the
Linux source code Documentation directory for major and minor numbers.
-----------------------------------------------------------------------------

8.2.3. ps, sed & ed

These three packages can be found by using the Internet resources we have
used before plus one new site. The "sed" and "ed" packages can be found at
the same place we found BASH, on the [ftp://ftp.gnu.org] GNU FTP server. The
procps package shows up in an Ibiblio LSM search, but it is an old version.
In order to find the latest version we can go to the Freshmeat website at
[http://freshmeat.net] http://freshmeat.net and search for "procps" in
projects.

Both "sed" and "ed" packages feature GNU's familiar configure script and are
therefore very easy to build. There is no configure script for "procps" but
this does not make things too difficult. We can just read the package's
README file to find out about how to set various configuration options. We
can use one of these options to avoid the complexity of using and installing
libproc. Setting SHARED=0 makes libproc an integrated part of ps rather than
a separate, shared library.
-----------------------------------------------------------------------------

8.3. Construction

8.3.1. Write a "more" script

Create the following script with a text editor and save it as ~/staging/bin/
more.sh

#!/bin/sh
#
# more.sh - emulates the basic functions of the "more" binary without
#           requiring ncurses or termcap libraries.
#
# Assume input is coming from STDIN unless a valid file is given as
# a command-line argument.
if [ -f $1 ]; then
  INPUT="$1"
else
  INPUT="/dev/stdin"
fi
#
# Set IFS to newline only. See BASH(1) manpage for details on IFS.
IFS=$'\n'
#
# If terminal dimensions are not already set as shell variables, take
# a guess of 80x25.
if [ "$COLUMNS" = "" ]; then
  let COLUMNS=80;
fi
if [ "$LINES" = "" ]; then
  let LINES=25;
fi
#
# Initialize line counter variable
let LINE_COUNTER=$LINES
#
# Read the input file one line at a time and display on STDOUT until
# the page fills up. Display "Press <Enter>" message on STDERR and wait
# for keypress from STDERR.  Continue until the end of the input file.
# Any input line greater than $COLUMNS characters in length is wrapped
# and counts as multiple lines.
#
while read -n $COLUMNS LINE_BUFFER; do
  echo "$LINE_BUFFER"
  let LINE_COUNTER=$LINE_COUNTER-1
  if [ $LINE_COUNTER -le 1 ]; then
    echo "Press <ENTER> for next page or <CTRL>+C to quit.">/dev/stderr
    read</dev/stderr
    let LINE_COUNTER=$LINES
  fi
done<$INPUT
#
# end of more.sh

Create a symbolic link for more

bash# ln -s more.sh ~/staging/bin/more
-----------------------------------------------------------------------------

8.3.2. Create additional device files

bash# ln -s /proc/self/fd ~/staging/dev/fd
bash# ln -s fd/0 ~/staging/dev/stdin
bash# ln -s fd/1 ~/staging/dev/stdout
bash# ln -s fd/2 ~/staging/dev/stderr
bash# mknod -m644 ~/staging/dev/zero c 1 5
-----------------------------------------------------------------------------

8.3.3. Install ps

Get the latest procps source package from [http://procps.sourceforge.net/]
http://procps.sourceforge.net/

bash# cd /usr/src/procps-3.2.3
bash# make SHARED=0 CC="gcc -mcpu=i386"
bash# cd ps
bash# cp ps ~/staging/bin
-----------------------------------------------------------------------------

8.3.4. Install sed

Download GNU's sed from [ftp://ftp.gnu.org/gnu/sed/] ftp://ftp.gnu.org/gnu/
sed/

bash# cd /usr/src/sed-4.1.2
bash# export CC="gcc -mcpu=i386"
bash# ./configure --host=i386-pc-linux-gnu
bash# make
bash# cd sed
bash# cp sed ~/staging/bin
-----------------------------------------------------------------------------

8.3.5. Install ed

The ed package also comes from GNU at [ftp://ftp.gnu.org/gnu/ed/] ftp://
ftp.gnu.org/gnu/ed/

bash# cd /usr/src/ed-0.2
bash# ./configure --host=i386-pc-linux-gnu
bash# make
bash# cp ed ~/staging/bin
-----------------------------------------------------------------------------

8.3.6. Strip binaries to save space

bash# strip ~/staging/bin/*
-----------------------------------------------------------------------------

8.3.7. Ensure proper permissions

bash# chown 0:0 ~/staging/bin/*
bash# chmod -R 755 ~/staging/bin
bash# chmod 4750 ~/staging/bin/su
-----------------------------------------------------------------------------

8.3.8. Create the root disk image

bash# cd /
bash# dd if=/dev/zero of=/dev/ram7 bs=1k count=4096
bash# mke2fs -m0 /dev/ram7 4096
bash# mount /dev/ram7 /mnt
bash# cp -dpR ~/staging/* /mnt
bash# umount /dev/ram7
bash# dd if=/dev/ram7 of=~/phase7-image bs=1k
bash# gzip -9 ~/phase7-image
-----------------------------------------------------------------------------

8.3.9. Copy the image to diskette

Insert the diskette labeled "root disk" into drive fd0.

bash# dd if=~/phase7-image.gz of=/dev/fd0 bs=1k
