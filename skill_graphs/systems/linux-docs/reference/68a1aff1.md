..
.. [various kernel messages]
..
VFS: Insert root floppy disk to be loaded into RAM disk and press ENTER
RAMDISK: Compressed image found at block 0
VFS: Mounted root (ext2 filesystem) read-write.
Freeing unused kernel memory: 178k freed
# _
-----------------------------------------------------------------------------

4.4.2. Testing new commands

Now that the system is up and running, try using some of the new commands.

bash# uname -a
bash# ls /etc
bash# echo "PocketLinux" > /etc/hostname
bash# hostname $(cat /etc/hostname)
bash# uname -n
bash# mkdir /home/stuff
bash# cd /home/stuff

If everything goes well the commands like cat, ls and hostname should work
now. Even mkdir should work since the root filesystem is mounted read-write.
Of course since we are using a ramdisk, any changes will be lost once the PC
is reset.
-----------------------------------------------------------------------------

4.4.3. System shutdown

Remove the diskette from fd0 and restart the system using CTRL-ALT-DELETE.
-----------------------------------------------------------------------------

Chapter 5. Checking and Mounting Disks

5.1. Analysis

In the previous chapter we added many new commands by installing coreutils
and as a result the root disk has a lot more functionality. But there are
still a few things lacking. One thing that really stands out is that there
was no way to mount disks. In order to get a read-write root filesystem we
had to resort to passing the rw kernel parameter at the grub> prompt. This is
fine for an emergency situation, but a normal system boot process should do
things differently.

Most GNU/Linux distributions take several steps to mount filesystems.
Watching the boot process or digging into the startup scripts on one of the
popular Linux distributions reveals the following sequence of events:

 1. The kernel automatically mounts the root filesystem as read-only.

 2. All local filesystems are checked for errors.

 3. If filesystems are clean, root is remounted as read-write.

 4. The rest of the local filesystems are mounted.

 5. Network filesystems are mounted.


So far our Pocket Linux system can do step one and that is it. If we want to
have a professional looking boot / root diskset we will have to do better
than one out of five. In this phase of the project we will work on steps two
and three. Steps four and five can wait. Since this is a diskette-based
system, there really are no other filesystems to mount besides root.

Taking into account all of the above information, the goals for this phase
are defined as follows:

��*�A way to check filesystem integrity.

��*�The ability to mount filesystems.

��*�A script to automate checking and mounting of local filesystems.


-----------------------------------------------------------------------------
5.2. Design

5.2.1. Determining necessary utilities.

We can use the Filesystem Hierarchy Standard (FHS) document to help find the
names of utilities we need and where they reside in the directory structure.
The FHS /sbin directory lists fsck and something called fsck.* for checking
filesystems. Since we are using a Second Extended (ext2) filesystem the fsck.
* becomes fsck.ext2 for our purposes. Mounting filesystems is done using the
commands mount and umount in the /bin directory. However, the name of a
script to automatically mount local filesystems cannot be found. On most
systems this type of script is in the /etc directory, but while FHS does list
requirements for /etc, it does not currently make recommendations for startup
scripts. Several GNU/Linux distributions use /etc/init.d as the place to hold
startup scripts so we will put our filesystem mounting script there.
-----------------------------------------------------------------------------

5.2.2. Finding source code

In the previous chapter we used manpages to help us find source code. In this
chapter we will use a tool called the Linux Software Map (LSM). LSM is a
database of GNU/Linux software that tracks such things as package name,
author, names of binaries that make up the package and download sites. Using
an LSM search engine we can locate packages using command names as keywords.

If we search Ibiblio's Linux Software Map (LSM) at [http://www.ibiblio.org/
pub/Linux/] http://www.ibiblio.org/pub/Linux/ for the keyword "fsck" we get a
large number of matches. Since we are using a Second Extended filesystem,
called ext2 for short, we can refine the search using "ext2" as a keyword.
Supplying both keywords to the LSM search engine comes up with a package
called e2fsprogs. Looking at the LSM entry for e2fsprogs we find out that
this package contains the utilities e2fsck, mke2fs, dumpe2fs, fsck and more.
We also find out that the LSM entry for e2fsprogs has not been updated for a
while. There is almost certainly a newer version out there somewhere. Another
good Internet resource for source code is SourceForge at [http://
sourceforge.net/] http://sourceforge.net/. Using the keyword "e2fsprogs" in
the SourceForge search engine results in a much newer version of e2fsprogs.

Finding fsck was quite an adventure, but now we can move on to finding mount
and umount. A search on LSM comes up with a number of matches, but most of
them point to various versions of a package called util-linux. All we have to
do is scroll through and pick the most recent release. The LSM entry for
util-linux lists a lot of utilities besides just mount and umount. We should
definitely scan through the list to see if any of the other util-linux
commands show up in the FHS requirements for /bin and /sbin.

Below is a list of packages we have gathered so far and the utilities that
match up with FHS.

��*�e2fsprogs -- fsck, fsck.ext2 (e2fsck), mkfs.ext2 (mke2fs)

��*�util-linux -- dmesg, getty (agetty), kill, login, mount, swapon, umount


-----------------------------------------------------------------------------
5.2.3. Automating fsck and mount

Now that we have fsck and mount commands we need to come up with a shell
script to automate checking and mounting the local filesystems. An easy way
to do this would be to write a short, two line script that calls fsck and
then mount. But, what if the filesystems are not clean? The system should
definitely not try to mount a corrupted filesystem. Therefore we need to
devise a way of determining the status of the filesystems before mounting
them. The manpage for fsck gives some insight into how this can be
accomplished using return codes. Basically, if fsck returns a code of zero or
one it means the filesystem is okay and a return code of two or greater means
some kind of manual intervention is needed. A simple if-then statement could
evaluate the fsck return code to determine whether or not the filesystem
should be mounted. For help on writing shell scripts we can turn to the BASH
(1) manpage and the Advanced-BASH-Scripting-Guide. Both references are freely
available from the Linux Documentation Project web site at [http://
www.tldp.org/] http://www.tldp.org/.
-----------------------------------------------------------------------------

5.2.4. File dependencies

The last thing to do is to figure out if any other files besides the binaries
are needed. We learned about using ldd to check for library dependencies in
the last phase of the project and we will use it to check the utilities in
this phase too. There are also some other files that fsck and mount will need
and the fsck(8) and mount(8) manpages give some insight into what those files
are. There is /etc/fstab that lists devices and their mount points, /etc/mtab
that keeps track of what is mounted, and a number of /dev files that
represent the various disks. We will need to include all of these to have
everything work right.
-----------------------------------------------------------------------------

5.2.4.1. /etc/fstab

The /etc/fstab file is just a simple text file that can be created with any
editor. We will need an entry for the root filesystem and for the proc
filesystem. Information about the format of this file can be found in the
fstab(5) manpage or by looking at the /etc/fstab file on any of the popular
GNU/Linux distributions.
-----------------------------------------------------------------------------

5.2.4.2. /etc/mtab

The /etc/mtab file presents a unique challenge, because it does not contain
static information like fstab. The mtab file tracks mounted filesystems and
therefore its contents change from time to time. We are particularly
interested in the state of mtab when the system first starts up, before any
filesystems are mounted. At this point /etc/mtab should be empty so we will
need to configure a startup script to create an empty /etc/mtab before any
filesystems are mounted. But it is not possible to create any files in the /
etc directory because / is read-only at startup. This creates a paradox. We
cannot create an empty mtab, because the / filesystem is not mounted as
writable and we should not mount any filesystems until we have created an
empty mtab. In order to sidestep this problem we need to do the following:

 1. Remount / as read-write, but use the -n option so that mount does not
    attempt to write an entry to /etc/mtab which is read-only at this point.

 2. Create an empty /etc/mtab file now that the filesystem is writable.

 3. Remount / as read-write again, this time using the -f option so that an
    entry is written into /etc/mtab, but / is not actually mounted a second
    time.


-----------------------------------------------------------------------------
5.2.4.3. Device files

The only thing left to do is to create device files. We will need /dev/ram0,
because that is where the root filesystem is located. We also need /dev/fd0
to mount other floppy disks and /dev/null for use by some of the system
commands.
-----------------------------------------------------------------------------

5.3. Construction

5.3.1. Install utilities from e2fsprogs

Download the e2fsprogs source code package from [http://sourceforge.net/
projects/e2fsprogs/] http://sourceforge.net/projects/e2fsprogs/

bash# cd /usr/src/e2fsprogs-1.35
bash# export CC="gcc -mcpu=i386"
bash# ./configure --host=i386-pc-linux-gnu
bash# make
bash# cd e2fsck
bash# cp e2fsck.shared ~/staging/sbin/e2fsck
bash# ln -s e2fsck ~/staging/sbin/fsck.ext2
bash# cd ../misc
bash# cp fsck mke2fs ~/staging/sbin
bash# ln -s mke2fs ~/staging/sbin/mkfs.ext2
-----------------------------------------------------------------------------

5.3.2. Install utilities from util-linux

Get the latest util-linux source from [ftp://ftp.win.tue.nl/pub/linux-local/
utils/util-linux/] ftp://ftp.win.tue.nl/pub/linux-local/utils/util-linux/

bash# cd /usr/src/util-linux-2.12h

Use a text editor to make the following changes to MCONFIG:

��*�Change "CPU=$(shell uname -m)" to "CPU=i386"

��*�Change "HAVE_SHADOW=yes" to "HAVE_SHADOW=no"


bash# ./configure
bash# make
bash# cp disk-utils/mkfs ~/staging/sbin
bash# cp fdisk/fdisk ~/staging/sbin
bash# cp login-utils/agetty ~/staging/sbin
bash# ln -s agetty ~/staging/sbin/getty
bash# cp login-utils/login ~/staging/bin
bash# cp misc-utils/kill ~/staging/bin
bash# cp mount/mount ~/staging/bin
bash# cp mount/umount ~/staging/bin
bash# cp mount/swapon ~/staging/sbin
bash# cp sys-utils/dmesg ~/staging/bin
-----------------------------------------------------------------------------

5.3.3. Check library requirements

bash# ldd ~/staging/bin/* | more
bash# ldd ~/staging/sbin/* | more
bash# ls ~/staging/lib

All of the dependencies revealed by the ldd command are for libraries already
present in the staging area so there is no need to copy anything new.
-----------------------------------------------------------------------------

5.3.4. Strip binaries to save space

bash# strip ~/staging/bin/*
bash# strip ~/staging/sbin/*
-----------------------------------------------------------------------------

5.3.5. Create additional device files

bash# mknod ~/staging/dev/ram0 b 1 0
bash# mknod ~/staging/dev/fd0 b 2 0
bash# mknod ~/staging/dev/null c 1 3
-----------------------------------------------------------------------------

5.3.6. Create the fstab and mtab files

bash# cd ~/staging/etc

Use an editor like vi, emacs or pico to create the following file and save it
as ~/staging/etc/fstab.

proc        /proc   proc   defaults   0   0
/dev/ram0   /       ext2   defaults   1   1

Create an empty mtab file.
bash# echo -n >mtab
-----------------------------------------------------------------------------

5.3.7. Write a script to check and mount local filesystems

Use an editor to create the following shell script and save it as ~/staging/
etc/init.d/local_fs:

#!/bin/sh
#
# local_fs - check and mount local filesystems
#
PATH=/sbin:/bin ; export PATH

fsck -ATCp
if [ $? -gt 1 ]; then
  echo "Filesystem errors still exist!  Manual intervention required."
  /bin/sh
else
  echo "Remounting / as read-write."
  mount -n -o remount,rw /
  echo -n >/etc/mtab
  mount -f -o remount,rw /
  echo "Mounting local filesystems."
  mount -a -t nonfs,nosmbfs
fi
#
# end of local_fs

Set execute permissions on the script.
bash# chmod +x local_fs
-----------------------------------------------------------------------------

5.3.8. Create a compressed root disk image

bash# cd /
bash# dd if=/dev/zero of=/dev/ram7 bs=1k count=4096
bash# mke2fs -m0 /dev/ram7 4096
bash# mount /dev/ram7 /mnt
bash# cp -dpR ~/staging/* /mnt
bash# umount /dev/ram7
bash# dd if=/dev/ram7 of=~/phase4-image bs=1k count=4096
bash# gzip -9 ~/phase4-image
-----------------------------------------------------------------------------

5.3.9. Write the root disk image to floppy

Insert the diskette labeled "root disk" into drive fd0.

bash# dd if=~/phase4-image.gz of=/dev/fd0 bs=1k
-----------------------------------------------------------------------------

5.4. Implementation

5.4.1. System startup

Start the system using the following procedure:

��*�Boot the PC using the floppy labeled "boot disk".

��*�At the grub> prompt, type the usual kernel and boot commands, but without
    the rw parameter this time. In other words, type kernel (fd0)/boot/
    vmlinuz init=/bin/sh root=/dev/fd0 load_ramdisk=1 prompt_ramdisk=1, press
    Enter then type boot and press Enter.

��*�Put in the recently created root disk when prompted.


The output should resemble the example below:
GNU GRUB version 0.95

grub> kernel (fd0)/boot/vmlinuz init=/bin/sh root=/dev/fd0 load_ramdisk=1 prompt_ramdisk=1
   [Linux-bzImage, setup=0xc00, size=0xce29b]

grub> boot

Linux version 2.4.26
..
.. [various kernel messages]
..
VFS: Insert root floppy disk to be loaded into RAM disk and press ENTER
RAMDISK: Compressed image found at block 0
VFS: Mounted root (ext2 filesystem) readonly.
Freeing unused kernel memory: 178k freed
# _
-----------------------------------------------------------------------------

5.4.2. Test the local_fs script

Run the script by typing the following commands at the shell prompt:

bash# PATH=/sbin:/bin:/etc/init.d ; export PATH
bash# cat /etc/mtab
bash# local_fs
bash# cat /etc/mtab
bash# df

If everything is working properly, then the screen output should look
something like the example below.

bash# PATH=/sbin:/bin:/etc/init.d ; export PATH
bash# cat /etc/mtab
bash# local_fs
/dev/ram0: clean 74/1024 files 3178/4096 blocks
Remounting / as read-write.
Mounting local filesystems.
bash# cat /etc/mtab
/dev/ram0 / ext2 rw 0 0
proc /proc proc rw 0 0
bash# df
Filesystem      1k-blocks       Used Available Use% Mounted on
/dev/ram0       3963            3045 918        77% /
-----------------------------------------------------------------------------

5.4.3. Create and mount additional filesystems

Procure a blank floppy disk and label it as "home". Remove the root disk
floppy and insert the "home" diskette. Type the following commands:

bash# mkfs -t ext2 /dev/fd0
bash# fsck /dev/fd0
bash# mount /dev/fd0 /home
bash# mkdir /home/floyd
bash# cd /home/floyd
bash# echo "Goodbye cruel world." > goodbye.txt
bash# cat goodbye.txt
-----------------------------------------------------------------------------

5.4.4. System shutdown

bash# cd /
bash# umount /home

Remove the diskette from fd0 and restart the system using CTRL-ALT-DELETE.
-----------------------------------------------------------------------------

Chapter 6. Automating Startup & Shutdown

6.1. Analysis

The root disk from the last chapter is looking pretty good. It has about
seventy percent of the commands that the Filesystem Hierarchy Standard (FHS)
document requires for the root filesystem. Plus it has commands for checking
and mounting filesystems. But even with all of this the root disk is far from
perfect. The list below outlines three things that could use some improvement
if the Pocket Linux system is to stand up next to the more professional
looking distributions.

 1. The system currently requires the kernel parameters to be typed at the
    grub> prompt in order to start properly. On any other GNU/Linux system
    this is only done in an emergency situation when the system is corrupted.

 2. Checking and mounting the root filesystem has to be done manually by
    running a script at a shell prompt. On most modern operating systems this
    function is handled automatically as part of the system start-up process.

 3. Using CTRL-ALT-DELETE for system shutdown is not very graceful.
    Filesystems should be unmounted and cached information should be flushed
    prior to shutdown. Again, this is something that most operating systems
    handle automatically.


Taking the above list into consideration, the goals for this phase are
defined as follows:

��*�Kernel loads without manual intervention.

��*�Automated system start-up sequence.

��*�Graceful shutdown capability.


-----------------------------------------------------------------------------
6.2. Design

6.2.1. Determining necessary utilities

Loading the kernel without manually typing parameters is easy to do if we
read the grub info page. According to the section entitled "configuration"
all of the commands used for booting can be put in a file called menu.lst and
placed in the /boot/grub directory.

Note Be sure to type the menu.lst filename correctly with a lowercase L after
     the dot and not a number one.

To automate system start-up we will need an init daemon. We know this because
the Bootdisk-HOWTO and From-Powerup-To-BASH-Prompt-HOWTO both make mention of
init as the first program to start after the kernel loads. The latter HOWTO
also goes into some detail about the /etc/inittab file and the organization
of startup scripts. This could be helpful since FHS, the blueprint we have
used so far, makes no recommendation for init scripts.

We will also need to find the shutdown command to fulfill the second goal of
graceful shutdown capability.
-----------------------------------------------------------------------------

6.2.2. Obtaining source code

Searching the Linux Software Map on Ibiblio for the keyword "init" gives a
