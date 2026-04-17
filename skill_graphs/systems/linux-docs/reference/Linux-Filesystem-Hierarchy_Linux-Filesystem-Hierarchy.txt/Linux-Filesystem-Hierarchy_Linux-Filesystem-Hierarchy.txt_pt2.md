
1.3. /bin

 Unlike /sbin, the bin directory contains several useful commands that are of
use to both the system administrator as well as non-privileged users. It
usually contains the shells like bash, csh, etc.... and commonly used
commands like cp, mv, rm, cat, ls. For this reason and in contrast to /usr/
bin, the binaries in this directory are considered to be essential. The
reason for this is that it contains essential system programs that must be
available even if only the partition containing / is mounted. This situation
may arise should you need to repair other partitions but have no access to
shared directories (ie. you are in single user mode and hence have no network
access). It also contains programs which boot scripts may depend on.

 Compliance to the FSSTND means that there are no subdirectories in /bin and
that the following commands, or symbolic links to commands, are located
there.


cat      Utility to concatenate files to standard output
chgrp    Utility to change file group ownership
chmod    Utility to change file access permissions
chown    Utility to change file owner and group
cp       Utility to copy files and directories
date     Utility to print or set the system data and time
dd       Utility to convert and copy a file
df       Utility to report filesystem disk space usage
dmesg    Utility to print or control the kernel message buffer
echo     Utility to display a line of text
false    Utility to do nothing, unsuccessfully
hostname Utility to show or set the system's host name
kill     Utility to send signals to processes
ln       Utility to make links between files
login    Utility to begin a session on the system
ls       Utility to list directory contents
mkdir    Utility to make directories
mknod    Utility to make block or character special files
more     Utility to page through text
mount    Utility to mount a filesystem
mv       Utility to move/rename files
ps       Utility to report process status
pwd      Utility to print name of current working directory
rm       Utility to remove files or directories
rmdir    Utility to remove empty directories
sed      The `sed' stream editor
sh       The Bourne command shell
stty     Utility to change and print terminal line settings
su       Utility to change user ID
sync     Utility to flush filesystem buffers
true     Utility to do nothing, successfully
umount   Utility to unmount file systems
uname    Utility to print system information

If /bin/sh is not a true Bourne shell, it must be a hard or symbolic link to
the real shell command.

The rationale behind this is because sh and bash mightn't necessarily behave
in the same manner. The use of a symbolic link also allows users to easily
see that /bin/sh is not a true Bourne shell.

The [ and test commands must be placed together in either /bin or /usr/bin.

The requirement for the [ and test commands to be included as binaries
(even if implemented internally by the shell) is shared with the POSIX.2
standard.

The following programs, or symbolic links to programs, must be in /bin if the
corresponding subsystem is installed:

csh     The C shell (optional)
ed      The `ed' editor (optional)
tar     The tar archiving utility (optional)
cpio    The cpio archiving utility (optional)
gzip    The GNU compression utility (optional)
gunzip  The GNU uncompression utility (optional)
zcat    The GNU uncompression utility (optional)
netstat The network statistics utility (optional)
ping    The ICMP network test utility (optional)

If the gunzip and zcat programs exist, they must be symbolic or hard links to
gzip. /bin/csh may be a symbolic link to /bin/tcsh or /usr/bin/tcsh.

The tar, gzip and cpio commands have been added to make restoration of a
system possible (provided that / is intact).

Conversely, if no restoration from the root partition is ever expected,
then these binaries might be omitted (e.g., a ROM chip root, mounting /usr
through NFS). If restoration of a system is planned through the network,
then ftp or tftp (along with everything necessary to get an ftp connection)
must be available on the root partition.
-----------------------------------------------------------------------------

1.4. /boot

This directory contains everything required for the boot process except for
configuration files not needed at boot time (the most notable of those being
those that belong to the GRUB boot-loader) and the map installer. Thus, the /
boot directory stores data that is used before the kernel begins executing
user-mode programs. This may include redundant (back-up) master boot records,
sector/system map files, the kernel and other important boot files and data
that is not directly edited by hand. Programs necessary to arrange for the
boot loader to be able to boot a file are placed in /sbin. Configuration
files for boot loaders are placed in /etc. The system kernel is located in
either / or /boot (or as under Debian in /boot but is actually a symbolically
linked at / in accordance with the FSSTND).

/boot/boot.0300
    Backup master boot record.

/boot/boot.b
    This is installed as the basic boot sector. In the case of most modern
    distributions it is actually a symbolic link to one of four files /boot/
    boot-bmp.b, /boot/boot-menu.b, /boot/boot-text.b, /boot/boot-compat.b
    which allow a user to change the boot-up schema so that it utilises a
    splash screen, a simple menu, a text based interface or a minimal boot
    loader to ensure compatibility respectively. In each case re-installation
    of lilo is necessary in order to complete the changes. To change the
    actual 'boot-logo' you can either use utilities such as fblogo or the
    more refined bootsplash.

/boot/chain.b
    Used to boot non-Linux operating systems.

/boot/config-kernel-version
    Installed kernel configuration. This file is most useful when compiling
    kernels on other systems or device modules. Below is a small sample of
    what the contents of the file looks like.

            CONFIG_X86=y
            CONFIG_MICROCODE=m
            CONFIG_X86_MSR=m
            CONFIG_MATH_EMULATION=y
            CONFIG_MTRR=y
            CONFIG_MODULES=y
            CONFIG_MODVERSIONS=y
            CONFIG_SCSI_DEBUG=m
            CONFIG_I2O=m
            CONFIG_ARCNET_ETH=y
            CONFIG_FMV18X=m
            CONFIG_HPLAN_PLUS=m
            CONFIG_ETH16I=m
            CONFIG_NE2000=m
            CONFIG_HISAX_HFC_PCI=y
            CONFIG_ISDN_DRV_AVMB1_C4=m
            CONFIG_USB_RIO500=m
            CONFIG_QUOTA=y
            CONFIG_AUTOFS_FS=m
            CONFIG_ADFS_FS=m
            CONFIG_AFFS_FS=m
            CONFIG_HFS_FS=m
            CONFIG_FAT_FS=y
            CONFIG_MSDOS_FS=y
            CONFIG_UMSDOS_FS=m
            CONFIG_FBCON_VGA=m
            CONFIG_FONT_8x8=y
            CONFIG_FONT_8x16=y
            CONFIG_SOUND=m
            CONFIG_SOUND_CMPCI=m
            CONFIG_AEDSP16=m


    As you can see, it's rather simplistic. The line begins with the
    configuration option and whether it's configured as part of the kernel,
    as a module or not at all. Lines beginning with a # symbol are comments
    and are not interpreted during processing.

/boot/os2_d.b
    Used to boot to the 0S/2 operating system.

/boot/map
    Contains the location of the kernel.

/boot/vmlinuz, /boot/vmlinuz-kernel-version
    Normally the kernel or symbolic link to the kernel.

/boot/grub
    This subdirectory contains the GRUB configuration files including boot-up
    images and sounds. GRUB is the GNU GRand Unified Bootloader, a project
    which intends to solve all bootup problems once and for all. One of the
    most interesting features, is that you don't have to install a new
    partition or kernel, you can change all parameters at boot time via the
    GRUB Console, since it knows about the filesystems.

/boot/grub/device.map
    Maps devices in /dev to those used by grub. For example, (/dev/fd0) is
    represented by /dev/fd0 and (hd0, 4) is referenced by /dev/hda5.

/boot/grub/grub.conf, /boot/grub/menu.lst
    Grub configuration file.

/boot/grub/messages
    Grub boot-up welcome message.

/boot/grub/splash.xpm.gz
    Grub boot-up background image.


-----------------------------------------------------------------------------
1.5. /dev

/dev is the location of special or device files. It is a very interesting
directory that highlights one important aspect of the Linux filesystem -
everything is a file or a directory. Look through this directory and you
should hopefully see hda1, hda2 etc.... which represent the various
partitions on the first master drive of the system. /dev/cdrom and /dev/fd0
represent your CD-ROM drive and your floppy drive. This may seem strange but
it will make sense if you compare the characteristics of files to that of
your hardware. Both can be read from and written to. Take /dev/dsp, for
instance. This file represents your speaker device. Any data written to this
file will be re-directed to your speaker. If you try 'cat /boot/vmlinuz > /
dev/dsp' (on a properly configured system) you should hear some sound on the
speaker. That's the sound of your kernel! A file sent to /dev/lp0 gets
printed. Sending data to and reading from /dev/ttyS0 will allow you to
communicate with a device attached there - for instance, your modem.

The majority of devices are either block or character devices; however other
types of devices exist and can be created. In general, 'block devices' are
devices that store or hold data, 'character devices' can be thought of as
devices that transmit or transfer data. For example, diskette drives, hard
drives and CD-ROM drives are all block devices while serial ports, mice and
parallel printer ports are all character devices. There is a naming scheme of
sorts but in the vast majority of cases these are completely illogical.


total 724
lrwxrwxrwx    1 root     root           13 Sep 28 18:06 MAKEDEV -> /sbin/MAKEDEV
crw-rw----    1 root     audio     14,  14 Oct  7 16:26 admmidi0
crw-rw----    1 root     audio     14,  30 Oct  7 16:26 admmidi1
lrwxrwxrwx    1 root     root           11 Oct  7 16:26 amidi -> /dev/amidi0
crw-rw----    1 root     audio     14,  13 Oct  7 16:26 amidi0
crw-rw----    1 root     audio     14,  29 Oct  7 16:26 amidi1
crw-rw----    1 root     audio     14,  11 Oct  7 16:26 amixer0
crw-rw----    1 root     audio     14,  27 Oct  7 16:26 amixer1
drwxr-xr-x    2 root     root         4096 Sep 28 18:05 ataraid
lrwxrwxrwx    1 root     root           11 Oct  7 16:26 audio -> /dev/audio0
crw-rw----    1 root     audio     14,   4 Oct  7 16:26 audio0
crw-rw----    1 root     audio     14,  20 Oct  7 16:26 audio1
crw-rw----    1 root     audio     14,   7 Mar 15  2002 audioctl
lrwxrwxrwx    1 root     root            9 Oct 14 22:51 cdrom -> /dev/scd1
lrwxrwxrwx    1 root     root            9 Oct 14 22:52 cdrom1 -> /dev/scd0
crw-------    1 root     tty        5,   1 Jan 19 20:47 console
lrwxrwxrwx    1 root     root           11 Sep 28 18:06 core -> /proc/kcore
crw-rw----    1 root     audio     14,  10 Oct  7 16:26 dmfm0
crw-rw----    1 root     audio     14,  26 Oct  7 16:26 dmfm1
crw-rw----    1 root     audio     14,   9 Oct  7 16:26 dmmidi0
crw-rw----    1 root     audio     14,  25 Oct  7 16:26 dmmidi1
lrwxrwxrwx    1 root     root            9 Oct  7 16:26 dsp -> /dev/dsp0
crw-rw----    1 root     audio     14,   3 Oct  7 16:26 dsp0
crw-rw----    1 root     audio     14,  19 Oct  7 16:26 dsp1
crw--w----    1 root     video     29,   0 Mar 15  2002 fb0
crw--w----    1 root     video     29,   1 Mar 15  2002 fb0autodetect
crw--w----    1 root     video     29,   0 Mar 15  2002 fb0current
crw--w----    1 root     video     29,  32 Mar 15  2002 fb1
crw--w----    1 root     video     29,  33 Mar 15  2002 fb1autodetect
crw--w----    1 root     video     29,  32 Mar 15  2002 fb1current
lrwxrwxrwx    1 root     root           13 Sep 28 18:05 fd -> /proc/self/fd
brw-rw----    1 root     floppy     2,   0 Mar 15  2002 fd0
brw-rw----    1 root     floppy     2,   1 Mar 15  2002 fd1
crw--w--w-    1 root     root       1,   7 Sep 28 18:06 full
brw-rw----    1 root     disk       3,   0 Mar 15  2002 had
brw-rw----    1 root     disk       3,  64 Mar 15  2002 hdb
brw-rw----    1 root     disk      22,   0 Mar 15  2002 hdc
brw-rw----    1 root     disk      22,  64 Mar 15  2002 hdd
drwxr-xr-x    2 root     root        12288 Sep 28 18:05 ida
prw-------    1 root     root            0 Jan 19 20:46 initctl
brw-rw----    1 root     disk       1, 250 Mar 15  2002 initrd
drwxr-xr-x    2 root     root         4096 Sep 28 18:05 input
crw-rw----    1 root     dialout   45, 128 Mar 15  2002 ippp0
crw-rw----    1 root     dialout   45,   0 Mar 15  2002 isdn0
crw-rw----    1 root     dialout   45,  64 Mar 15  2002 isdnctrl0
crw-rw----    1 root     dialout   45, 255 Mar 15  2002 isdninfo
crw-------    1 root     root      10,   4 Mar 15  2002 jbm
crw-r-----    1 root     kmem       1,   2 Sep 28 18:06 kmem
brw-rw----    1 root     cdrom     24,   0 Mar 15  2002 lmscd
crw-------    1 root     root      10,   0 Mar 15  2002 logibm
brw-rw----    1 root     disk       7,   0 Sep 28 18:06 loop0
brw-rw----    1 root     disk       7,   1 Sep 28 18:06 loop1
crw-rw----    1 root     lp         6,   0 Mar 15  2002 lp0
crw-rw----    1 root     lp         6,   1 Mar 15  2002 lp1
crw-rw----    1 root     lp         6,   2 Mar 15  2002 lp2
crw-r-----    1 root     kmem       1,   1 Sep 28 18:06 mem
lrwxrwxrwx    1 root     root           10 Oct  7 16:26 midi -> /dev/midi0
crw-rw----    1 root     audio     14,   2 Oct  7 16:26 midi0
crw-rw----    1 root     audio     14,  18 Oct  7 16:26 midi1
lrwxrwxrwx    1 root     root           11 Oct  7 16:26 mixer -> /dev/mixer0
crw-rw-rw-    1 root     root      14,   0 Nov 11 16:22 mixer0
crw-rw----    1 root     audio     14,  16 Oct  7 16:26 mixer1
lrwxrwxrwx    1 root     root           11 Oct  7 06:50 modem -> /dev/ttyLT0
crw-rw----    1 root     audio     31,   0 Mar 15  2002 mpu401data
crw-rw----    1 root     audio     31,   1 Mar 15  2002 mpu401stat
crw-rw----    1 root     audio     14,   8 Oct  7 16:26 music
crw-rw-rw-    1 root     root       1,   3 Sep 28 18:06 null
crw-rw-rw-    1 root     root     195,   0 Jan  6 03:03 nvidia0
crw-rw-rw-    1 root     root     195,   1 Jan  6 03:03 nvidia1
crw-rw-rw-    1 root     root     195, 255 Jan  6 03:03 nvidiactl
crw-rw----    1 root     lp         6,   0 Mar 15  2002 par0
crw-rw----    1 root     lp         6,   1 Mar 15  2002 par1
crw-rw----    1 root     lp         6,   2 Mar 15  2002 par2
-rw-r--r--    1 root     root       665509 Oct  7 16:41 pcm
crw-r-----    1 root     kmem       1,   4 Sep 28 18:06 port
crw-rw----    1 root     dip      108,   0 Sep 28 18:07 ppp
crw-------    1 root     root      10,   1 Mar 15  2002 psaux
crw-rw-rw-    1 root     root       1,   8 Sep 28 18:06 random
crw-rw----    1 root     root      10, 135 Mar 15  2002 rtc
brw-rw----    1 root     cdrom     11,   0 Mar 15  2002 scd0
brw-rw----    1 root     cdrom     11,   1 Mar 15  2002 scd1
brw-rw----    1 root     disk       8,   0 Mar 15  2002 sda
brw-rw----    1 root     disk       8,   1 Mar 15  2002 sda1
brw-rw----    1 root     disk       8,   2 Mar 15  2002 sda2
brw-rw----    1 root     disk       8,   3 Mar 15  2002 sda3
brw-rw----    1 root     disk       8,   4 Mar 15  2002 sda4
brw-rw----    1 root     disk       8,  16 Mar 15  2002 sdb
brw-rw----    1 root     disk       8,  17 Mar 15  2002 sdb1
brw-rw----    1 root     disk       8,  18 Mar 15  2002 sdb2
brw-rw----    1 root     disk       8,  19 Mar 15  2002 sdb3
brw-rw----    1 root     disk       8,  20 Mar 15  2002 sdb4
crw-rw----    1 root     audio     14,   1 Oct  7 16:26 sequencer
lrwxrwxrwx    1 root     root           10 Oct  7 16:26 sequencer2 -> /dev/music
lrwxrwxrwx    1 root     root            4 Sep 28 18:05 stderr -> fd/2
lrwxrwxrwx    1 root     root            4 Sep 28 18:05 stdin -> fd/0
lrwxrwxrwx    1 root     root            4 Sep 28 18:05 stdout -> fd/1
crw-rw-rw-    1 root     tty        5,   0 Sep 28 18:06 tty
crw-------    1 root     root       4,   0 Sep 28 18:06 tty0
crw-------    1 root     root       4,   1 Jan 19 14:59 tty1
crw-rw----    1 root     dialout   62,  64 Oct  7 06:50 ttyLT0
crw-rw----    1 root     dialout    4,  64 Mar 15  2002 ttyS0
crw-rw----    1 root     dialout    4,  65 Mar 15  2002 ttyS1
crw-rw----    1 root     dialout    4,  66 Mar 15  2002 ttyS2
crw-rw----    1 root     dialout    4,  67 Mar 15  2002 ttyS3
crw-rw----    1 root     dialout  188,   0 Mar 15  2002 ttyUSB0
crw-rw----    1 root     dialout  188,   1 Mar 15  2002 ttyUSB1
cr--r--r--    1 root     root       1,   9 Jan 19 20:46 urandom
drwxr-xr-x    2 root     root         4096 Sep 28 18:05 usb
prw-r-----    1 root     adm             0 Jan 19 14:58 xconsole
crw-rw-rw-    1 root     root       1,   5 Sep 28 18:06 zero

Some common device files as well as their equivalent counterparts under
Windows that you may wish to remember are:

/dev/ttyS0 (First communications port, COM1)
     First serial port (mice, modems).

/dev/psaux (PS/2)
     PS/2 mouse connection (mice, keyboards).

/dev/lp0 (First printer port, LPT1)
     First parallel port (printers, scanners, etc).

/dev/dsp (First audio device)
     The name DSP comes from the term digital signal processor, a specialized
    processor chip optimized for digital signal analysis. Sound cards may use
    a dedicated DSP chip, or may implement the functions with a number of
    discrete devices. Other terms that may be used for this device are
    digitized voice and PCM.

/dev/usb (USB Devices)
     This subdirectory contains most of the USB device nodes. Device name
    allocations are fairly simplistic so no elaboration is be necessary.

/dev/sda (C:\, SCSI device)
     First SCSI device (HDD, Memory Sticks, external mass storage devices
    such as CD-ROM drives on laptops, etc).

/dev/scd (D:\, SCSI CD-ROM device)
     First SCSI CD-ROM device.

/dev/js0 (Standard gameport joystick)
     First joystick device.


Devices are defined by type, such as 'block' or 'character', and 'major' and
'minor' number. The major number is used to categorize a device and the minor
number is used to identify a specific device type. For example, all IDE
device connected to the primary controller have a major number of 3. Master
and slave devices, as well as individual partitions are further defined by
the use of minor numbers. These are the two numbers precede the date in the
following display:

# ls -l /dev/hd*


brw-rw----    1 root     disk       3,   0 Mar 15  2002 /dev/had
brw-rw----    1 root     disk       3,   1 Mar 15  2002 /dev/hda1
brw-rw----    1 root     disk       3,  10 Mar 15  2002 /dev/hda10
brw-rw----    1 root     disk       3,  11 Mar 15  2002 /dev/hda11
brw-rw----    1 root     disk       3,  12 Mar 15  2002 /dev/hda12
brw-rw----    1 root     disk       3,  13 Mar 15  2002 /dev/hda13
brw-rw----    1 root     disk       3,  14 Mar 15  2002 /dev/hda14
brw-rw----    1 root     disk       3,  15 Mar 15  2002 /dev/hda15
brw-rw----    1 root     disk       3,  16 Mar 15  2002 /dev/hda16
brw-rw----    1 root     disk       3,  17 Mar 15  2002 /dev/hda17
brw-rw----    1 root     disk       3,  18 Mar 15  2002 /dev/hda18
brw-rw----    1 root     disk       3,  19 Mar 15  2002 /dev/hda19
brw-rw----    1 root     disk       3,   2 Mar 15  2002 /dev/hda2
