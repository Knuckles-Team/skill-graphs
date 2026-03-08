    software which produces sound and your soundcard. It is a character
    device on major node 14 and minor 3.

/dev/fd0
    The first floppy drive. If you are lucky enough to have several drives
    then they will be numbered sequentially. It is a character device on
    major node 2 and minor 0.

/dev/fb0
    The first framebuffer device. A framebuffer is an abstraction layer
    between software and graphics hardware. This means that applications do
    not need to know about what kind of hardware you have but merely how to
    communicate with the framebuffer driver's API (Application Programming
    Interface) which is well defined and standardized. The framebuffer is a
    character device and is on major node 29 and minor 0.

/dev/had
    /dev/had is the master IDE drive on the primary IDE controller. /dev/hdb
    the slave drive on the primary controller. /dev/hdc , and /dev/hdd are
    the master and slave devices on the secondary controller respectively.
    Each disk is divided into partitions. Partitions 1-4 are primary
    partitions and partitions 5 and above are logical partitions inside
    extended partitions. Therefore the device file which references each
    partition is made up of several parts. For example /dev/hdc9 references
    partition 9 (a logical partition inside an extended partition type) on
    the master IDE drive on the secondary IDE controller. The major and minor
    node numbers are somewhat complex. For the first IDE controller all
    partitions are block devices on major node 3. The master drive had is at
    minor 0 and the slave drive hdb is at minor 64. For each partition inside
    the drive add the partition number to the minor minor node number for the
    drive. For example /dev/hdb5 is major 3, minor 69 (64 + 5 = 69). Drives
    on the secondary interface are handled the same way, but with major node
    22.

/dev/ht0
    The first IDE tape drive. Subsequent drives are numbered ht1 etc. They
    are character devices on major node 37 and start at minor node 0 for ht0
    1 for ht1 etc.

/dev/js0
    The first analogue joystick. Subsequent joysticks are numbered js1, js2
    etc. Digital joysticks are called djs0, djs1 and so on. They are
    character devices on major node 15. The analogue joysticks start at minor
    node 0 and go up to 127 (more than enough for even the most fanatic
    gamer). Digital joysticks start at minor node 128.

/dev/lp0
    The first parallel printer device. Subsequent printers are numbered lp1,
    lp2 etc. They are character devices on major mode 6 and minor nodes
    starting at 0 and numbered sequentially.

/dev/loop0
    The first loopback device. Loopback devices are used for mounting
    filesystems which are not located on other block devices such as disks.
    For example if you wish to mount an iso9660 CD ROM image without burning
    it to CD then you need to use a loopback device to do so. This is usually
    transparent to the user and is handled by the mount command. Refer to the
    manual pages for mount and losetup. The loopback devices are block
    devices on major node 7 and with minor nodes starting at 0 and numbered
    sequentially.

/dev/md0
    First metadisk group. Metadisks are related to RAID (Redundant Array of
    Independent Disks) devices. Please refer to the most current RAID HOWTO
    at the LDP for more details. This can be found at [http://www.tldp.org/
    HOWTO/Software-RAID-HOWTO.html] http://www.tldp.org/HOWTO/
    Software-RAID-HOWTO.html. Metadisk devices are block devices on major
    node 9 with minor nodes starting at 0 and numbered sequentially.

/dev/mixer
    This is part of the OSS (Open Sound System) driver. Refer to the OSS
    documentation at [http://www.opensound.com] http://www.opensound.com for
    more details. It is a character device on major node 14, minor node 0.

/dev/null
    The bit bucket. A black hole where you can send data for it never to be
    seen again. Anything sent to /dev/null will disappear. This can be useful
    if, for example, you wish to run a command but not have any feedback
    appear on the terminal. It is a character device on major node 1 and
    minor node 3.

/dev/psaux
    The PS/2 mouse port. This is a character device on major node 10, minor
    node 1.

/dev/pda
    Parallel port IDE disks. These are named similarly to disks on the
    internal IDE controllers (/dev/hd*). They are block devices on major node
    45. Minor nodes need slightly more explanation here. The first device is
    /dev/pda and it is on minor node 0. Partitions on this device are found
    by adding the partition number to the minor number for the device. Each
    device is limited to 15 partitions each rather than 63 (the limit for
    internal IDE disks). /dev/pdb minor nodes start at 16, /dev/pdc at 32 and
    /dev/pdd at 48. So for example the minor node number for /dev/pdc6 would
    be 38 (32 + 6 = 38). This scheme limits you to 4 parallel disks of 15
    partitions each.

/dev/pcd0
    Parallel port CD ROM drives. These are numbered from 0 onwards. All are
    block devices on major node 46. /dev/pcd0 is on minor node 0 with
    subsequent drives being on minor nodes 1, 2, 3 etc.

/dev/pt0
    Parallel port tape devices. Tapes do not have partitions so these are
    just numbered sequentially. They are character devices on major node 96.
    The minor node numbers start from 0 for /dev/pt0, 1 for /dev/pt1, and so
    on.

/dev/parport0
    The raw parallel ports. Most devices which are attached to parallel ports
    have their own drivers. This is a device to access the port directly. It
    is a character device on major node 99 with minor node 0. Subsequent
    devices after the first are numbered sequentially incrementing the minor
    node.

/dev/random or /dev/urandom
    These are kernel random number generators. /dev/random is a
    non-deterministic generator which means that the value of the next number
    cannot be guessed from the preceding ones. It uses the entropy of the
    system hardware to generate numbers. When it has no more entropy to use
    then it must wait until it has collected more before it will allow any
    more numbers to be read from it. /dev/urandom works similarly. Initially
    it also uses the entropy of the system hardware, but when there is no
    more entropy to use it will continue to return numbers using a pseudo
    random number generating formula. This is considered to be less secure
    for vital purposes such as cryptographic key pair generation. If security
    is your overriding concern then use /dev/random, if speed is more
    important then /dev/urandom works fine. They are character devices on
    major node 1 with minor nodes 8 for /dev/random and 9 for /dev/urandom.

/dev/sda
    The first SCSI drive on the first SCSI bus. The following drives are
    named similar to IDE drives. /dev/sdb is the second SCSI drive, /dev/sdc
    is the third SCSI drive, and so forth.

/dev/ttyS0
    The first serial port. Many times this it the port used to connect an
    external modem to your system.

/dev/zero
    This is a simple way of getting many 0s. Every time you read from this
    device it will return 0. This can be useful sometimes, for example when
    you want a file of fixed length but don't really care what it contains.
    It is a character device on major node 1 and minor node 5.


-----------------------------------------------------------------------------
3.5. The /usr filesystem.

The /usr filesystem is often large, since all programs are installed there.
All files in /usr usually come from a Linux distribution; locally installed
programs and other stuff goes below /usr/local. This makes it possible to
update the system from a new version of the distribution, or even a
completely new distribution, without having to install all programs again.
Some of the subdirectories of /usr are listed below (some of the less
important directories have been dropped; see the FSSTND for more
information).

/usr/X11R6.
    The X Window System, all files. To simplify the development and
    installation of X, the X files have not been integrated into the rest of
    the system. There is a directory tree below /usr/X11R6 similar to that
    below /usr itself.

/usr/bin.
    Almost all user commands. Some commands are in /bin or in /usr/local/bin.

/usr/sbin
    System administration commands that are not needed on the root
    filesystem, e.g., most server programs.

/usr/share/man, /usr/share/info, /usr/share/doc
    Manual pages, GNU Info documents, and miscellaneous other documentation
    files, respectively.

/usr/include
    Header files for the C programming language. This should actually be
    below /usr/lib for consistency, but the tradition is overwhelmingly in
    support for this name.

/usr/lib
    Unchanging data files for programs and subsystems, including some
    site-wide configuration files. The name lib comes from library;
    originally libraries of programming subroutines were stored in /usr/lib.

/usr/local
    The place for locally installed software and other files. Distributions
    may not install anything in here. It is reserved solely for the use of
    the local administrator. This way he can be absolutely certain that no
    updates or upgrades to his distribution will overwrite any extra software
    he has installed locally.


-----------------------------------------------------------------------------
3.6. The /var filesystem

The /var contains data that is changed when the system is running normally.
It is specific for each system, i.e., not shared over the network with other
computers.

/var/cache/man
    A cache for man pages that are formatted on demand. The source for manual
    pages is usually stored in /usr/share/man/man?/ (where ? is the manual
    section. See the manual page for man in section 7); some manual pages
    might come with a pre-formatted version, which might be stored in /usr/
    share/man/cat* . Other manual pages need to be formatted when they are
    first viewed; the formatted version is then stored in /var/cache/man so
    that the next person to view the same page won't have to wait for it to
    be formatted.

/var/games
    Any variable data belonging to games in /usr should be placed here. This
    is in case /usr is mounted read only.

/var/lib
    Files that change while the system is running normally.

/var/local
    Variable data for programs that are installed in /usr/local (i.e.,
    programs that have been installed by the system administrator). Note that
    even locally installed programs should use the other /var directories if
    they are appropriate, e.g., /var/lock.

/var/lock
    Lock files. Many programs follow a convention to create a lock file in /
    var/lock to indicate that they are using a particular device or file.
    Other programs will notice the lock file and won't attempt to use the
    device or file.

/var/log
    Log files from various programs, especially login(/var/log/wtmp, which
    logs all logins and logouts into the system) and syslog(/var/log/
    messages, where all kernel and system program message are usually
    stored). Files in /var/log can often grow indefinitely, and may require
    cleaning at regular intervals.

/var/mail
    This is the FHS approved location for user mailbox files. Depending on
    how far your distribution has gone towards FHS compliance, these files
    may still be held in /var/spool/mail.

/var/run
    Files that contain information about the system that is valid until the
    system is next booted. For example, /var/run/utmp contains information
    about people currently logged in.

/var/spool
    Directories for news, printer queues, and other queued work. Each
    different spool has its own subdirectory below /var/spool, e.g., the news
    spool is in /var/spool/news . Note that some installations which are not
    fully compliant with the latest version of the FHS may have user
    mailboxes under /var/spool/mail.

/var/tmp
    Temporary files that are large or that need to exist for a longer time
    than what is allowed for /tmp . (Although the system administrator might
    not allow very old files in /var/tmp either.)


-----------------------------------------------------------------------------
3.7. The /proc filesystem

The /proc filesystem contains a illusionary filesystem. It does not exist on
a disk. Instead, the kernel creates it in memory. It is used to provide
information about the system (originally about processes, hence the name).
Some of the more important files and directories are explained below. The /
proc filesystem is described in more detail in the proc manual page.

/proc/1
    A directory with information about process number 1. Each process has a
    directory below /proc with the name being its process identification
    number.

/proc/cpuinfo
    Information about the processor, such as its type, make, model, and
    performance.

/proc/devices
    List of device drivers configured into the currently running kernel.

/proc/dma
    Shows which DMA channels are being used at the moment.

/proc/filesystems
    Filesystems configured into the kernel.

/proc/interrupts
    Shows which interrupts are in use, and how many of each there have been.

/proc/ioports
    Which I/O ports are in use at the moment.

/proc/kcore
    An image of the physical memory of the system. This is exactly the same
    size as your physical memory, but does not really take up that much
    memory; it is generated on the fly as programs access it. (Remember:
    unless you copy it elsewhere, nothing under /proc takes up any disk space
    at all.)

/proc/kmsg
    Messages output by the kernel. These are also routed to syslog.

/proc/ksyms
    Symbol table for the kernel.

/proc/loadavg
    The `load average' of the system; three meaningless indicators of how
    much work the system has to do at the moment.

/proc/meminfo
    Information about memory usage, both physical and swap.

/proc/modules
    Which kernel modules are loaded at the moment.

/proc/net
    Status information about network protocols.

/proc/self
    A symbolic link to the process directory of the program that is looking
    at /proc. When two processes look at /proc, they get different links.
    This is mainly a convenience to make it easier for programs to get at
    their process directory.

/proc/stat
    Various statistics about the system, such as the number of page faults
    since the system was booted.

/proc/uptime
    The time the system has been up.

/proc/version
    The kernel version.


Note that while the above files tend to be easily readable text files, they
can sometimes be formatted in a way that is not easily digestible. There are
many commands that do little more than read the above files and format them
for easier understanding. For example, the freeprogram reads /proc/meminfo
converts the amounts given in bytes to kilobytes (and adds a little more
information, as well).
-----------------------------------------------------------------------------

Chapter 4. Hardware, Devices, and Tools

    "Knowledge speaks, but wisdom listens." Jimi Hendrix

This chapter gives an overview of what a device file is, and how to create
one. The canonical list of device files is /usr/src/linux/Documentation/
devices.txt if you have the Linux kernel source code installed on your
system. The devices listed here are correct as of kernel version 2.6.8.
-----------------------------------------------------------------------------

4.1. Hardware Utilities

4.1.1. The MAKEDEV Script

Most device files will already be created and will be there ready to use
after you install your Linux system. If by some chance you need to create one
which is not provided then you should first try to use the MAKEDEV script.
This script is usually located in /dev/MAKEDEV but might also have a copy (or
a symbolic link) in /sbin/MAKEDEV. If it turns out not to be in your path
then you will need to specify the path to it explicitly.

In general the command is used as:
+---------------------------------------------------------------------------+
|        # /dev/MAKEDEV -v ttyS0                                            |
|        create ttyS0   c 4 64 root:dialout 0660                            |
|                                                                           |
+---------------------------------------------------------------------------+
This will create the device file /dev/ttyS0 with major node 4 and minor node
64 as a character device with access permissions 0660 with owner root and
group dialout.

ttyS0 is a serial port. The major and minor node numbers are numbers
understood by the kernel. The kernel refers to hardware devices as numbers,
this would be very difficult for us to remember, so we use filenames. Access
permissions of 0660 means read and write permission for the owner (root in
this case) and read and write permission for members of the group (dialout in
this case) with no access for anyone else.
-----------------------------------------------------------------------------

4.1.2. The mknod command

MAKEDEV is the preferred way of creating device files which are not present.
However sometimes the MAKEDEV script will not know about the device file you
wish to create. This is where the mknod command comes in. In order to use
mknod you need to know the major and minor node numbers for the device you
wish to create. The devices.txt file in the kernel source documentation is
the canonical source of this information.

To take an example, let us suppose that our version of the MAKEDEV script
does not know how to create the /dev/ttyS0 device file. We need to use mknod
to create it. We know from looking at the devices.txt that it should be a
character device with major number 4 and minor number 64. So we now know all
we need to create the file.
+-------------------------------------------------------------------------------+
|        # mknod /dev/ttyS0 c 4 64                                              |
|        # chown root.dialout /dev/ttyS0                                        |
|        # chmod 0644 /dev/ttyS0                                                |
|        # ls -l /dev/ttyS0                                                     |
|                crw-rw----   1 root dialout    4,   64 Oct 23 18:23 /dev/ttyS0 |
|                                                                               |
|                                                                               |
+-------------------------------------------------------------------------------+
As you can see, many more steps are required to create the file. In this
example you can see the process required however. It is unlikely in the
extreme that the ttyS0 file would not be provided by the MAKEDEV script, but
it suffices to illustrate the point.
-----------------------------------------------------------------------------

4.1.3. The lspci command

lspci

TO BE ADDED
-----------------------------------------------------------------------------

4.1.4. The lsdev command

lsdev

TO BE ADDED
-----------------------------------------------------------------------------

4.1.5. The lsusb command

lsusb

TO BE ADDED
-----------------------------------------------------------------------------

4.1.6. The lsraid command

lsraid

TO BE ADDED
-----------------------------------------------------------------------------

4.1.7. The hdparm command

hdparm

TO BE ADDED
-----------------------------------------------------------------------------

4.1.8. More Hardware Resources

More information on what hardware resources the kernel is using can be found
in the /proc directory. Refer to Section 3.7 in chapter 3.
-----------------------------------------------------------------------------

4.2. Kernel Modules

This section will discuss kernel modules.

TO BE ADDED
-----------------------------------------------------------------------------

4.2.1. lsmod

lsmod

TO BE ADDED
-----------------------------------------------------------------------------

4.2.2. insmod

insmod

TO BE ADDED
-----------------------------------------------------------------------------

4.2.3. depmod

depmod

TO BE ADDED
-----------------------------------------------------------------------------

4.2.4. rmmod

rmmod

TO BE ADDED
-----------------------------------------------------------------------------

4.2.5. modprobe

modprobe

TO BE ADDED
-----------------------------------------------------------------------------

Chapter 5. Using Disks and Other Storage Media

    "On a clear disk you can seek forever. "

When you install or upgrade your system, you need to do a fair amount of work
on your disks. You have to make filesystems on your disks so that files can
be stored on them and reserve space for the different parts of your system.

This chapter explains all these initial activities. Usually, once you get
your system set up, you won't have to go through the work again, except for
using floppies. You'll need to come back to this chapter if you add a new
disk or want to fine-tune your disk usage.



The basic tasks in administering disks are:

��*�Format your disk. This does various things to prepare it for use, such as
    checking for bad sectors. (Formatting is nowadays not necessary for most
    hard disks.)

��*�Partition a hard disk, if you want to use it for several activities that
    aren't supposed to interfere with one another. One reason for
    partitioning is to store different operating systems on the same disk.
    Another reason is to keep user files separate from system files, which
    simplifies back-ups and helps protect the system files from corruption.

��*�Make a filesystem (of a suitable type) on each disk or partition. The
    disk means nothing to Linux until you make a filesystem; then files can
    be created and accessed on it.

��*�Mount different filesystems to form a single tree structure, either
    automatically, or manually as needed. (Manually mounted filesystems
    usually need to be unmounted manually as well.)


Chapter 6 contains information about virtual memory and disk caching, of
which you also need to be aware when using disks.
-----------------------------------------------------------------------------

5.1. Two kinds of devices

UNIX, and therefore Linux, recognizes two different kinds of device:
random-access block devices (such as disks), and character devices (such as
tapes and serial lines) , some of which may be serial, and some
random-access. Each supported device is represented in the filesystem as a
device file. When you read or write a device file, the data comes from or
goes to the device it represents. This way no special programs (and no
special application programming methodology, such as catching interrupts or
polling a serial port) are necessary to access devices; for example, to send
a file to the printer, one could just say
+---------------------------------------------------------------------------+
|$ cat filename > /dev/lp1                                                  |
|$                                                                          |
+---------------------------------------------------------------------------+
and the contents of the file are printed (the file must, of course, be in a
form that the printer understands). However, since it is not a good idea to
have several people cat their files to the printer at the same time, one
usually uses a special program to send the files to be printed (usually lpr
). This program makes sure that only one file is being printed at a time, and
will automatically send files to the printer as soon as it finishes with the
previous file. Something similar is needed for most devices. In fact, one
seldom needs to worry about device files at all.

Since devices show up as files in the filesystem (in the /dev directory), it
is easy to see just what device files exist, using ls or another suitable
command. In the output of ls -l, the first column contains the type of the
file and its permissions. For example, inspecting a serial device might give
+-----------------------------------------------------------------------------------+
|        $ ls -l /dev/ttyS0                                                         |
|                crw-rw-r--    1 root     dialout    4,  64 Aug 19 18:56 /dev/ttyS0 |
|                                                                                   |
|        $                                                                          |
|                                                                                   |
+-----------------------------------------------------------------------------------+
The first character in the first column, i.e., `c' in crw-rw-rw- above, tells
an informed user the type of the file, in this case a character device. For
ordinary files, the first character is `-', for directories it is `d', and
for block devices `b'; see the ls man page for further information.

Note that usually all device files exist even though the device itself might
be not be installed. So just because you have a file /dev/sda, it doesn't
mean that you really do have an SCSI hard disk. Having all the device files
