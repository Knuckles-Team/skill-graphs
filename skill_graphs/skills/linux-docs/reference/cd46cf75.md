umount.

It should of course be unmount, but the n mysteriously disappeared in the
70s, and hasn't been seen since. Please return it to Bell Labs, NJ, if you
find it.

umount takes one argument: either the device file or the mount point. For
example, to unmount the directories of the previous example, one could use
the commands
  $ umount /dev/hda2
  $ umount /usr
  $


See the man page for further instructions on how to use the command. It is
imperative that you always unmount a mounted floppy. Don't just pop the
floppy out of the drive! Because of disk caching, the data is not necessarily
written to the floppy until you unmount it, so removing the floppy from the
drive too early might cause the contents to become garbled. If you only read
from the floppy, this is not very likely, but if you write, even
accidentally, the result may be catastrophic.

Mounting and unmounting requires super user privileges, i.e., only root can
do it. The reason for this is that if any user can mount a floppy on any
directory, then it is rather easy to create a floppy with, say, a Trojan
horse disguised as /bin/sh, or any other often used program. However, it is
often necessary to allow users to use floppies, and there are several ways to
do this:

��*�Give the users the root password. This is obviously bad security, but is
    the easiest solution. It works well if there is no need for security
    anyway, which is the case on many non-networked, personal systems.

��*�Use a program such as sudo to allow users to use mount. This is still bad
    security, but doesn't directly give super user privileges to everyone.
    [1]

��*�Make the users use mtools, a package for manipulating MS-DOS filesystems,
    without mounting them. This works well if MS-DOS floppies are all that is
    needed, but is rather awkward otherwise.

��*�List the floppy devices and their allowable mount points together with
    the suitable options in /etc/fstab.


The last alternative can be implemented by adding a line like the following
to the /etc/fstab file:

  /dev/fd0 /floppy
  msdos user,noauto 0 0


The columns are: device file to mount, directory to mount on, filesystem
type, options, backup frequency (used by dump), and fsck pass number (to
specify the order in which filesystems should be checked upon boot; 0 means
no check).

The noauto option stops this mount to be done automatically when the system
is started (i.e., it stops mount -a from mounting it). The user option allows
any user to mount the filesystem, and, because of security reasons, disallows
execution of programs (normal or setuid) and interpretation of device files
from the mounted filesystem. After this, any user can mount a floppy with an
msdos filesystem with the following command:



  $ mount /floppy
  $


The floppy can (and needs to, of course) be unmounted with the corresponding
umount command.

If you want to provide access to several types of floppies, you need to give
several mount points. The settings can be different for each mount point. For
example, to give access to both MS-DOS and ext2 floppies, you could have the
following to lines in /etc/fstab:

  /dev/fd0 /dosfloppy msdos user,noauto 0 0 /dev/fd0
  /ext2floppy ext2 user,noauto 0 0


For MS-DOS filesystems (not just floppies), you probably want to restrict
access to it by using the uid, gid, and umask filesystem options, described
in detail on the mount manual page. If you aren't careful, mounting an MS-DOS
filesystem gives everyone at least read access to the files in it, which is
not a good idea.
-----------------------------------------------------------------------------

1.13. /opt

  This directory is reserved for all the software and add-on packages that
are not part of the default installation. For example, StarOffice, Kylix,
Netscape Communicator and WordPerfect packages are normally found here. To
comply with the FSSTND, all third party applications should be installed in
this directory. Any package to be installed here must locate its static files
(ie. extra fonts, clipart, database files) must locate its static files in a
separate /opt/'package' or /opt/'provider' directory tree (similar to the way
in which Windows will install new software to its own directory tree C:\
Windows\Program Files\"Program Name"), where 'package' is a name that
describes the software package and 'provider' is the provider's LANANA
registered name.

  Although most distributions neglect to create the directories /opt/bin, /
opt/doc, /opt/include, /opt/info, /opt/lib, and /opt/man they are reserved
for local system administrator use. Packages may provide "front-end" files
intended to be placed in (by linking or copying) these reserved directories
by the system administrator, but must function normally in the absence of
these reserved directories. Programs to be invoked by users are located in
the directory /opt/'package'/bin. If the package includes UNIX manual pages,
they are located in /opt/'package'/man and the same substructure as /usr/
share/man must be used. Package files that are variable must be installed in
/var/opt. Host-specific configuration files are installed in /etc/opt.

  Under no circumstances are other package files to exist outside the /opt, /
var/opt, and /etc/opt hierarchies except for those package files that must
reside in specific locations within the filesystem tree in order to function
properly. For example, device lock files in /var/lock and devices in /dev.
Distributions may install software in /opt, but must not modify or delete
software installed by the local system administrator without the assent of
the local system administrator.

  The use of /opt for add-on software is a well-established practice in the
UNIX community. The System V Application Binary Interface [AT&T 1990], based
on the System V Interface Definition (Third Edition) and the Intel Binary
Compatibility Standard v. 2 (iBCS2) provides for an /opt structure very
similar to the one defined here.

  Generally, all data required to support a package on a system must be
present within /opt/'package', including files intended to be copied into /
etc/opt/'package' and /var/opt/'package' as well as reserved directories in /
opt. The minor restrictions on distributions using /opt are necessary because
conflicts are possible between distribution installed and locally installed
software, especially in the case of fixed pathnames found in some binary
software.

  The structure of the directories below /opt/'provider' is left up to the
packager of the software, though it is recommended that packages are
installed in /opt/'provider'/'package' and follow a similar structure to the
guidelines for /opt/package. A valid reason for diverging from this structure
is for support packages which may have files installed in /opt/ 'provider'/
lib or /opt/'provider'/bin.
-----------------------------------------------------------------------------

1.14. /proc

/proc is very special in that it is also a virtual filesystem. It's sometimes
referred to as a process information pseudo-file system. It doesn't contain
'real' files but runtime system information (e.g. system memory, devices
mounted, hardware configuration, etc). For this reason it can be regarded as
a control and information centre for the kernel. In fact, quite a lot of
system utilities are simply calls to files in this directory. For example,
'lsmod' is the same as 'cat /proc/modules' while 'lspci' is a synonym for
'cat /proc/pci'. By altering files located in this directory you can even
read/change kernel parameters (sysctl) while the system is running.

The most distinctive thing about files in this directory is the fact that all
of them have a file size of 0, with the exception of kcore, mtrr and self. A
directory listing looks similar to the following:

total 525256
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 1
dr-xr-xr-x    3 daemon   root            0 Jan 19 15:00 109
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 170
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 173
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 178
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 2
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 3
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 4
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 421
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 425
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 433
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 439
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 444
dr-xr-xr-x    3 daemon   daemon          0 Jan 19 15:00 446
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 449
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 453
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 456
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 458
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 462
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 463
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 464
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 465
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 466
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 467
dr-xr-xr-x    3 gdm      gdm             0 Jan 19 15:00 472
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 483
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 5
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 6
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 7
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 8
-r--r--r--    1 root     root            0 Jan 19 15:00 apm
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 bus
-r--r--r--    1 root     root            0 Jan 19 15:00 cmdline
-r--r--r--    1 root     root            0 Jan 19 15:00 cpuinfo
-r--r--r--    1 root     root            0 Jan 19 15:00 devices
-r--r--r--    1 root     root            0 Jan 19 15:00 dma
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 driver
-r--r--r--    1 root     root            0 Jan 19 15:00 execdomains
-r--r--r--    1 root     root            0 Jan 19 15:00 fb
-r--r--r--    1 root     root            0 Jan 19 15:00 filesystems
dr-xr-xr-x    2 root     root            0 Jan 19 15:00 fs
dr-xr-xr-x    4 root     root            0 Jan 19 15:00 ide
-r--r--r--    1 root     root            0 Jan 19 15:00 interrupts
-r--r--r--    1 root     root            0 Jan 19 15:00 iomem
-r--r--r--    1 root     root            0 Jan 19 15:00 ioports
dr-xr-xr-x   18 root     root            0 Jan 19 15:00 irq
-r--------    1 root     root     536809472 Jan 19 15:00 kcore
-r--------    1 root     root            0 Jan 19 14:58 kmsg
-r--r--r--    1 root     root            0 Jan 19 15:00 ksyms
-r--r--r--    1 root     root            0 Jan 19 15:00 loadavg
-r--r--r--    1 root     root            0 Jan 19 15:00 locks
-r--r--r--    1 root     root            0 Jan 19 15:00 mdstat
-r--r--r--    1 root     root            0 Jan 19 15:00 meminfo
-r--r--r--    1 root     root            0 Jan 19 15:00 misc
-r--r--r--    1 root     root            0 Jan 19 15:00 modules
-r--r--r--    1 root     root            0 Jan 19 15:00 mounts
-rw-r--r--    1 root     root          137 Jan 19 14:59 mtrr
dr-xr-xr-x    3 root     root            0 Jan 19 15:00 net
dr-xr-xr-x    2 root     root            0 Jan 19 15:00 nv
-r--r--r--    1 root     root            0 Jan 19 15:00 partitions
-r--r--r--    1 root     root            0 Jan 19 15:00 pci
dr-xr-xr-x    4 root     root            0 Jan 19 15:00 scsi
lrwxrwxrwx    1 root     root           64 Jan 19 14:58 self -> 483
-rw-r--r--    1 root     root            0 Jan 19 15:00 slabinfo
-r--r--r--    1 root     root            0 Jan 19 15:00 stat
-r--r--r--    1 root     root            0 Jan 19 15:00 swaps
dr-xr-xr-x   10 root     root            0 Jan 19 15:00 sys
dr-xr-xr-x    2 root     root            0 Jan 19 15:00 sysvipc
dr-xr-xr-x    4 root     root            0 Jan 19 15:00 tty
-r--r--r--    1 root     root            0 Jan 19 15:00 uptime
-r--r--r--    1 root     root            0 Jan 19 15:00 version

Each of the numbered directories corresponds to an actual process ID. Looking
at the process table, you can match processes with the associated process ID.
For example, the process table might indicate the following for the secure
shell server:

# ps ax | grep sshd
439 ? S 0:00 /usr/sbin/sshd

Details of this process can be obtained by looking at the associated files in
the directory for this process, /proc/460. You might wonder how you can see
details of a process that has a file size of 0. It makes more sense if you
think of it as a window into the kernel. The file doesn't actually contain
any data; it just acts as a pointer to where the actual process information
resides. For example, a listing of the files in the /proc/460 directory looks
similar to the following:

total 0
-r--r--r--    1 root     root            0 Jan 19 15:02 cmdline
lrwxrwxrwx    1 root     root            0 Jan 19 15:02 cwd -> /
-r--------    1 root     root            0 Jan 19 15:02 environ
lrwxrwxrwx    1 root     root            0 Jan 19 15:02 exe -> /usr/sbin/sshd
dr-x------    2 root     root            0 Jan 19 15:02 fd
-r--r--r--    1 root     root            0 Jan 19 15:02 maps
-rw-------    1 root     root            0 Jan 19 15:02 mem
lrwxrwxrwx    1 root     root            0 Jan 19 15:02 root -> /
-r--r--r--    1 root     root            0 Jan 19 15:02 stat
-r--r--r--    1 root     root            0 Jan 19 15:02 statm
-r--r--r--    1 root     root            0 Jan 19 15:02 status

The purpose and contents of each of these files is explained below:

/proc/PID/cmdline
    Command line arguments.

/proc/PID/cpu
    Current and last cpu in which it was executed.

/proc/PID/cwd
    Link to the current working directory.

/proc/PID/environ
    Values of environment variables.

/proc/PID/exe
    Link to the executable of this process.

/proc/PID/fd
    Directory, which contains all file descriptors.

/proc/PID/maps
    Memory maps to executables and library files.

/proc/PID/mem
    Memory held by this process.

/proc/PID/root
    Link to the root directory of this process.

/proc/PID/stat
    Process status.

/proc/PID/statm
    Process memory status information.

/proc/PID/status
    Process status in human readable form.


Should you wish to know more, the man page for proc describes each of the
files associated with a running process ID in far greater detail.

Even though files appear to be of size 0, examining their contents reveals
otherwise:

# cat status

Name: sshd
State: S (sleeping)
Tgid: 439
Pid: 439
PPid: 1
TracerPid: 0
Uid: 0 0 0 0
Gid: 0 0 0 0
FDSize: 32
Groups:
VmSize:     2788 kB
VmLck:        0 kB
VmRSS:     1280 kB
VmData:      252 kB
VmStk:       16 kB
VmExe:      268 kB
VmLib:     2132 kB
SigPnd: 0000000000000000
SigBlk: 0000000000000000
SigIgn: 8000000000001000
SigCgt: 0000000000014005
CapInh: 0000000000000000
CapPrm: 00000000fffffeff
CapEff: 00000000fffffeff

The files in the /proc directory act very similar to the process ID
subdirectory files. For example, examining the contents of the /proc/
interrupts file displays something like the following:

# cat interrupts

           CPU0
  0:      32657          XT-PIC  timer
  1:       1063          XT-PIC  keyboard
  2:          0          XT-PIC  cascade
  8:          3          XT-PIC  rtc
  9:          0          XT-PIC  cmpci
 11:        332          XT-PIC  nvidia
 14:       5289          XT-PIC  ide0
 15:         13          XT-PIC  ide1
NMI:          0
ERR:          0

Each of the numbers down the left-hand column represents the interrupt that
is in use. Examining the contents of the file dynamically gathers the
associated data and displays it to the screen. Most of the /proc file system
is read-only; however, some files allow kernel variable to be changed. This
provides a mechanism to actually tune the kernel without recompiling and
rebooting.

The procinfo utility summarizes /proc file system information into a display
similar to the following:

# /usr/bin/procinfo

Linux 2.4.18 (root@DEB) (gcc 2.95.4 20011002 ) #2 1CPU [DEB.(none)]

Memory:      Total        Used        Free      Shared     Buffers      Cached
Mem:        513908      107404      406504           0        2832       82180
Swap:       265032           0      265032

Bootup: Sun Jan 19 14:58:27 2003    Load average: 0.29 0.13 0.05 1/30 566

user  :       0:00:10.26   2.3%  page in :    74545  disk 1:     6459r     796w
nice  :       0:00:00.00   0.0%  page out:     9416  disk 2:       19r       0w
system:       0:00:19.55   4.5%  swap in :        1
idle  :       0:06:48.30  93.2%  swap out:        0
uptime:       0:07:18.11         context :    22059

irq  0:     43811 timer                 irq  9:         0 cmpci
irq  1:      1427 keyboard              irq 11:       332 nvidia
irq  2:         0 cascade [4]           irq 12:         2
irq  6:         2                       irq 14:      7251 ide0
irq  8:         3 rtc                   irq 15:        83 ide1

/proc/apm
      Advanced power management info.

/proc/bus
    Directory containing bus specific information.

/proc/cmdline
    Kernel command line.

/proc/cpuinfo
      Information about the processor, such as its type, make, model, and
    performance.

/proc/devices
      List of device drivers configured into the currently running kernel
    (block and character).

/proc/dma
    Shows which DMA channels are being used at the moment.

/proc/driver
    Various drivers grouped here, currently rtc

/proc/execdomains
    Execdomains, related to security.

/proc/fb
    Frame Buffer devices.

/proc/filesystems
    Filesystems configured/supported into/by the kernel.

/proc/fs
    File system parameters, currently nfs/exports.

/proc/ide
    This subdirectory contains information about all IDE devices of which the
    kernel is aware. There is one subdirectory for each IDE controller, the
    file drivers and a link for each IDE device, pointing to the device
    directory in the controller-specific subtree. The file drivers contains
    general information about the drivers used for the IDE devices. More
    detailed information can be found in the controller-specific
    subdirectories. These are named ide0, ide1 and so on. Each of these
    directories contains the files shown here:

    /proc/ide/ide?/channel
        IDE channel (0 or 1)

    /proc/ide/ide?/config
          Configuration (only for PCI/IDE bridge)

    /proc/ide/ide?/mate
        Mate name (onchip partnered controller)

    /proc/ide/ide?/model
        Type/Chipset of IDE controller


          Each device connected to a controller has a separate subdirectory
        in the controllers directory. The following files listed are
        contained in these directories:

    /proc/ide/ide?/model/cache
        The cache.

    /proc/ide/ide?/model/capacity
          Capacity of the medium (in 512Byte blocks)

    /proc/ide/ide?/model/driver
          driver and version

    /proc/ide/ide?/model/geometry
          physical and logical geometry

    /proc/ide/ide?/model/identify
          device identify block

    /proc/ide/ide?/model/media
        media type

    /proc/ide/ide?/model/model
          device identifier

    /proc/ide/ide?/model/settings
          device setup

    /proc/ide/ide?/model/smart_thresholds
          IDE disk management thresholds

    /proc/ide/ide?/model/smart_values
          IDE disk management values



/proc/interrupts
    Shows which interrupts are in use, and how many of each there have been.


        You can, for example, check which interrupts are currently in use and
        what they are used for by looking in the file /proc/interrupts:


        # cat /proc/interrupts



          CPU0 0: 8728810
          XT-PIC timer 1: 895
          XT-PIC keyboard 2:
