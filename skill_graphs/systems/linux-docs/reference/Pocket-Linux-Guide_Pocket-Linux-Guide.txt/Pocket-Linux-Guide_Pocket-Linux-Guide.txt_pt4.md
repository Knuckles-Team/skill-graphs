large number of results. From reading the From-Powerup-To-BASH-Prompt-HOWTO
however, we know that most Linux systems use a System V style init daemon.
Narrowing the search with the additional key phrase of "System V" gives much
better results. The sysvinit package contains init, shutdown, halt and reboot
which is everything we need. The version listed in the LSM entry looks to be
pretty old, but there is a primary-site URL that will probably lead to the
latest version.
-----------------------------------------------------------------------------

6.2.3. Checking dependencies

The manpage for init mentions a FIFO called /dev/initctl that is required for
init to communicate with other programs in the sysvinit package. We will have
to create this file for init to function properly.
-----------------------------------------------------------------------------

6.2.4. Designing a simple GRUB configuration file.

Using a GRUB configuration file is slightly more complex than specifying the
bootloader commands manually. There are directives for features like menus,
default selections and timeouts that need to be specified in the
configuration file as well as the familiar kernel loading command. The info
page for GRUB gives much of the necessary information. We may also be able to
use the GRUB configuration file on the development system as a template.
However, there is some inconsistency between vendors as to the name and
location of the file. Regardless of what the path is on the development
system it should be /boot/grub/menu.lst on the Pocket Linux System.
-----------------------------------------------------------------------------

6.2.5. Outlining start-up scripts

Many of the popular GNU/Linux distributions use System V style init scripts.
Since we are using a "sysvinit" daemon it makes sense to use System V style
scripts as well. The following documents all touch upon the System V style
init scripts in some way and will serve as references when building the
scripts for this project:

��*�The Debian Policy Manual -- available online at [http://www.debian.org/
    doc/debian-policy] http://www.debian.org/doc/debian-policy.

��*�The Linux Standard Base specification -- downloadable in many formats
    from [http://www.linuxbase.org/spec/index.shtml] http://www.linuxbase.org
    /spec/index.shtml.

��*�Essential System Administration, 3rd Edition by Aeleen Frisch --
    available at libraries, bookstores or directly from O'Reilly Publishing
    at [http://www.oreilly.com/] http://www.oreilly.com/.


After glancing at one or two of the above references we should have a pretty
good idea of how the System V style system initialization process works. We
should also know what it takes to create System V style init scripts for the
Pocket Linux project. Below is a brief list of what needs to be done:

��*�Create an inittab file to call an rc script with a numerical argument
    giving the runlevel.

��*�Write an rc script that uses the runlevel argument to execute the
    appropriate "K" and "S" scripts.

��*�Modify the previously built local_fs script to take start and stop
    arguments.

��*�Create new scripts for shutdown and reboot.

��*�Set up /etc/rcN.d directories and links to scripts in /etc/init.d.


As always, the BASH(1) manpage and the Advanced BASH Scripting Guide are very
helpful for writing and understanding shell scripts.
-----------------------------------------------------------------------------

6.3. Construction

There is a lot of typing to do in this section because of all of the start-up
scripts that need to be created. Using a mouse to copy the text from this
guide and paste it into a text editor can be a great time saving tool.
-----------------------------------------------------------------------------

6.3.1. Create a GRUB configuration file

Insert and mount the floppy labeled "boot disk".
bash# mount /dev/fd0 /mnt
bash# cd /mnt/boot/grub

Use your favorite text editor to create the following file and save it as /
mnt/boot/grub/menu.lst:
default 0
timeout 3
title Pocket Linux Boot Disk
kernel (fd0)/boot/vmlinuz root=/dev/fd0 load_ramdisk=1 prompt_ramdisk=1
-----------------------------------------------------------------------------

6.3.2. Install sysvinit utilities

Download the latest sysvinit source from [ftp://ftp.cistron.nl/pub/people/
miquels/software/] ftp://ftp.cistron.nl/pub/people/miquels/software/

bash# cd /usr/src/sysvinit-2.85/src
bash# make CC="gcc -mcpu=i386"
bash# cp halt init shutdown ~/staging/sbin
bash# ln -s halt ~/staging/sbin/reboot
bash# ln -s init ~/staging/sbin/telinit
bash# mknod ~/staging/dev/initctl p

Note In the interest of speed we are skipping the steps for checking
     libraries and stripping binaries. The library requirements for sysvinit
     are very basic and the Makefile is configured to automatically strip the
     binaries.
-----------------------------------------------------------------------------

6.3.3. Create /etc/inittab file

Use a text editor to create the following file and save it as ~/staging/etc/
inittab

# /etc/inittab - init daemon configuration file
#
# Default runlevel
id:1:initdefault:
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
# end of /etc/inittab
-----------------------------------------------------------------------------

6.3.4. Create /etc/init.d/rc script

Use a text editor to create the following file and save it as ~/staging/etc/
init.d/rc

#!/bin/sh
#
# /etc/init.d/rc - runlevel change script
#
PATH=/sbin:/bin
SCRIPT_DIR="/etc/rc$1.d"
#
# Check that the rcN.d directory really exists.
if [ -d $SCRIPT_DIR ]; then
#
# Execute the kill scripts first.
  for SCRIPT in $SCRIPT_DIR/K*; do
    if [ -x $SCRIPT ]; then
      $SCRIPT stop;
    fi;
  done;
#
# Do the Start scripts last.
  for SCRIPT in $SCRIPT_DIR/S*; do
    if [ -x $SCRIPT ]; then
      $SCRIPT start;
    fi;
  done;
fi
#
# end of /etc/init.d/rc

Make the file executable.

bash# chmod +x ~/staging/etc/init.d/rc
-----------------------------------------------------------------------------

6.3.5. Modify /etc/init.d/local_fs script

A case statement is added to allow the script to either mount or unmount
local filesystems depending on the command-line argument given. The original
script is contained inside the "start" portion of the case statement. The
"stop" portion is new.

#!/bin/sh
#
# local_fs - check and mount local filesystems
#
PATH=/sbin:/bin ; export PATH

case $1 in

start)
  echo "Checking local filesystem integrity."
  fsck -ATCp
  if [ $? -gt 1 ]; then
    echo "Filesystem errors still exist!  Manual intervention required."
    /bin/sh
  else
    echo "Remounting / as read-write."
    mount -n -o remount,rw /
    echo -n > /etc/mtab
    mount -f -o remount,rw /
    echo "Mounting local filesystems."
    mount -a -t nonfs,smbfs
  fi
;;

stop)
  echo "Unmounting local filesystems."
  umount -a -r
;;

*)
  echo "usage: $0 start|stop";
;;

esac
#
# end of local_fs
-----------------------------------------------------------------------------

6.3.6. Create a hostname script

Use a text editor to create the following script and save it as ~/staging/etc
/init.d/hostname

#!/bin/sh
#
# hostname - set the system name to the name stored in /etc/hostname
#
PATH=/sbin:/bin ; export PATH

echo "Setting hostname."
if [ -f /etc/hostname ]; then
  hostname $(cat /etc/hostname)
else
  hostname gnu-linux
fi
#
# end of hostname
-----------------------------------------------------------------------------

6.3.7. Create halt & reboot scripts

Use a text editor to create ~/staging/etc/init.d/halt as shown below.

#!/bin/sh
#
# halt - halt the system
#
PATH=/sbin:/bin ; export PATH

echo "Initiating system halt."
halt
#
# end of /etc/init.d/halt

Create the following script and save it as ~/staging/etc/init.d/reboot

#!/bin/sh
#
# reboot - reboot the system
#
PATH=/sbin:/bin ; export PATH

echo "Initiating system reboot."
reboot
#
# end of /etc/init.d/reboot

Flag all script files as executable.

bash# chmod +x ~/staging/etc/init.d/*
-----------------------------------------------------------------------------

6.3.8. Create rcN.d directories and links

bash# cd ~/staging/etc
bash# mkdir rc0.d rc1.d rc2.d rc3.d rc4.d rc5.d rc6.d rcS.d
bash# cd ~/staging/etc/rcS.d
bash# ln -s ../init.d/local_fs S20local_fs
bash# ln -s ../init.d/hostname S30hostname
bash# cd ~/staging/etc/rc0.d
bash# ln -s ../init.d/local_fs K10local_fs
bash# ln -s ../init.d/halt K90halt
bash# cd ~/staging/etc/rc6.d
bash# ln -s ../init.d/local_fs K10local_fs
bash# ln -s ../init.d/reboot K90reboot
-----------------------------------------------------------------------------

6.3.9. Create the root disk image

bash# cd /
bash# dd if=/dev/zero of=/dev/ram7 bs=1k count=4096
bash# mke2fs -m0 /dev/ram7 4096
bash# mount /dev/ram7 /mnt
bash# cp -dpR ~/staging/* /mnt
bash# umount /dev/ram7
bash# dd if=/dev/ram7 of=~/phase5-image bs=1k
bash# gzip -9 ~/phase5-image
-----------------------------------------------------------------------------

6.3.10. Copy the image to diskette

Insert the diskette labeled "root disk" into drive fd0.

bash# dd if=~/phase5-image.gz of=/dev/fd0 bs=1k
-----------------------------------------------------------------------------

6.4. Implementation

6.4.1. System Startup

Boot the PC using the floppy labeled "boot disk". Place the recently created
root disk in fd0 when prompted. The output should resemble the example below:

GNU GRUB version 0.95

Uncompressing Linux... Ok, booting kernel.
..
.. [various kernel messages]
..
VFS: Insert root floppy to be loaded into RAM disk and press ENTER
RAMDISK: Compressed image found at block 0
VFS: Mounted root (ext2 filesystem) readonly.
Freeing unused kernel memory: 178k freed
Checking local filesystem integrity.
/dev/ram0: clean 105/1024 files 2842/4096 blocks
Remounting / as read-write.
Mounting local filesystems.
Setting the hostname.
INIT: Entering runlevel: 1
# _
-----------------------------------------------------------------------------

6.4.2. Verify success of startup scripts

Use the mount command to check that local filesystems are mounted as
read-write. The output should look like the example below.

bash# mount
/dev/root on / type ext2 (rw)
proc on /proc type proc (rw)

Check the hostname.

bash# uname -n
gnu-linux
-----------------------------------------------------------------------------

6.4.3. System shutdown

Bring the system down gracefully with the shutdown command.

bash# shutdown -h now

We should see the following output from init and the shutdown scripts:

INIT: Switching to runlevel: 0
INIT: Sending processes the TERM signal
Terminated
INIT: Sending processes the KILL signal
Unmounting local filesystems.
Initiating system halt.
System halted.
-----------------------------------------------------------------------------

Chapter 7. Enabling Multiple Users

7.1. Analysis

Up to now the system has been operating in single-user mode. There is no
login process and anyone who boots the system goes straight into a shell with
root privileges. Obviously, this is not the normal operating mode for most
GNU/Linux distributions. Most systems feature multi-user capability where
many users can access the system simultaneously with different privilege
levels. These multi-user systems also support virtual consoles so that the
keyboard and video display can be multiplexed between several terminal
sessions. So in this phase we would like to add the following enhancements to
the system:

��*�Enable multi-user capability.

��*�Create multiple, virtual consoles.


-----------------------------------------------------------------------------
7.2. Design

7.2.1. The login process

The From-Powerup-To-BASH-Prompt-HOWTO does a good job of outlining the steps
in the login process. Basically it works like this.

 1. The init daemon starts a getty process on the terminal.

 2. The getty program displays the contents of /etc/issue and prompts for a
    user name.

 3. When the user name is entered, control is handed off to the login
    program.

 4. The login program asks for a password and verifies the credentials using
    /etc/passwd, /etc/group and possibly /etc/shadow.

 5. If everything is okay the user's shell is started.


-----------------------------------------------------------------------------
7.2.2. Obtaining source code

The getty and login programs were already installed as part of the util-linux
package so there is no need to download any new source code.
-----------------------------------------------------------------------------

7.2.3. Creating support files

7.2.3.1. Device nodes

Details about virtual console device files can be found in the Linux kernel
source code file called devices.txt in the Documentation directory. We will
need to create tty1 through tty6 for each of the virtual consoles as well as
tty0 and tty to represent the current virtual console.
-----------------------------------------------------------------------------

7.2.3.2. /etc/issue

The /etc/issue file is pretty easy to construct. It can contain any text we
want displayed on the screen prior to the login prompt. It could be something
friendly like "Welcome to Pocket Linux", something menacing like "Authorized
users only!" or something informational like "Connected to tty1 at 9600bps".
The agetty(8) manpage explains how to display information like tty line and
baud rate using escape codes.
-----------------------------------------------------------------------------

7.2.3.3. /etc/passwd

The format of /etc/passwd can be obtained by reading the passwd(5) manpage.
We can easily create a user account by adding a line like "root::0:0:
superuser:/root:/bin/sh" to the file.

Maintaining passwords will be somewhat challenging because of the system
being loaded into ramdisk. Any changes to /etc/passwd will be lost when the
system is shutdown. So to make things easy, we will create all users with
null passwords.
-----------------------------------------------------------------------------

7.2.3.4. /etc/group

The structure of /etc/group is available from the group(5) manpage. A line of
"root::0:root" would define a group called "root" with no password, a group
id of zero and the user root assigned to it as the only member.
-----------------------------------------------------------------------------

7.2.3.5. Conventions

User and group names and id's are generally not chosen at random. Most Linux
systems have very similar looking /etc/passwd and /etc/group files.
Definitions for commonly used user id and group id assignments may be found
in one of several places:

��*�The /etc/passwd and /etc/group files on any popular GNU/Linux
    distribution.

��*�The Debian Policy Manual -- available online at [http://www.debian.org/
    doc/debian-policy] http://www.debian.org/doc/debian-policy.

��*�The Linux Standard Base specification -- downloadable in many formats
    from [http://www.linuxbase.org/spec/index.shtml] http://www.linuxbase.org
    /spec/index.shtml.

��*�Essential System Administration, 3rd Edition by Aeleen Frisch --
    available at libraries, bookstores or directly from O'Reilly Publishing
    at [http://www.oreilly.com/] http://www.oreilly.com/.


-----------------------------------------------------------------------------
