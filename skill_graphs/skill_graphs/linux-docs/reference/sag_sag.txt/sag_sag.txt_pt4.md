makes the installation programs simpler, and makes it easier to add new
hardware (there is no need to find out the correct parameters for and create
the device files for the new device).
-----------------------------------------------------------------------------

5.2. Hard disks

This subsection introduces terminology related to hard disks. If you already
know the terms and concepts, you can skip this subsection.

See Figure 5-1 for a schematic picture of the important parts in a hard disk.
A hard disk consists of one or more circular aluminum platters\ , of which
either or both surfaces are coated with a magnetic substance used for
recording the data. For each surface, there is a read-write head that
examines or alters the recorded data. The platters rotate on a common axis;
typical rotation speed is 5400 or 7200 rotations per minute, although
high-performance hard disks have higher speeds and older disks may have lower
speeds. The heads move along the radius of the platters; this movement
combined with the rotation of the platters allows the head to access all
parts of the surfaces.

The processor (CPU) and the actual disk communicate through a disk controller
. This relieves the rest of the computer from knowing how to use the drive,
since the controllers for different types of disks can be made to use the
same interface towards the rest of the computer. Therefore, the computer can
say just ``hey disk, give me what I want'', instead of a long and complex
series of electric signals to move the head to the proper location and
waiting for the correct position to come under the head and doing all the
other unpleasant stuff necessary. (In reality, the interface to the
controller is still complex, but much less so than it would otherwise be.)
The controller may also do other things, such as caching, or automatic bad
sector replacement.

The above is usually all one needs to understand about the hardware. There
are also other things, such as the motor that rotates the platters and moves
the heads, and the electronics that control the operation of the mechanical
parts, but they are mostly not relevant for understanding the working
principles of a hard disk.

The surfaces are usually divided into concentric rings, called tracks, and
these in turn are divided into sectors. This division is used to specify
locations on the hard disk and to allocate disk space to files. To find a
given place on the hard disk, one might say ``surface 3, track 5, sector 7''.
Usually the number of sectors is the same for all tracks, but some hard disks
put more sectors in outer tracks (all sectors are of the same physical size,
so more of them fit in the longer outer tracks). Typically, a sector will
hold 512 bytes of data. The disk itself can't handle smaller amounts of data
than one sector.


Figure 5-1. A schematic picture of a hard disk.

[hd-schematic]

Each surface is divided into tracks (and sectors) in the same way. This means
that when the head for one surface is on a track, the heads for the other
surfaces are also on the corresponding tracks. All the corresponding tracks
taken together are called a cylinder. It takes time to move the heads from
one track (cylinder) to another, so by placing the data that is often
accessed together (say, a file) so that it is within one cylinder, it is not
necessary to move the heads to read all of it. This improves performance. It
is not always possible to place files like this; files that are stored in
several places on the disk are called fragmented.

The number of surfaces (or heads, which is the same thing), cylinders, and
sectors vary a lot; the specification of the number of each is called the
geometry of a hard disk. The geometry is usually stored in a special,
battery-powered memory location called the CMOS RAM , from where the
operating system can fetch it during bootup or driver initialization.

Unfortunately, the BIOS has a design limitation, which makes it impossible to
specify a track number that is larger than 1024 in the CMOS RAM, which is too
little for a large hard disk. To overcome this, the hard disk controller lies
about the geometry, and translates the addresses given by the computer into
something that fits reality. For example, a hard disk might have 8 heads,
2048 tracks, and 35 sectors per track. Its controller could lie to the
computer and claim that it has 16 heads, 1024 tracks, and 35 sectors per
track, thus not exceeding the limit on tracks, and translates the address
that the computer gives it by halving the head number, and doubling the track
number. The mathematics can be more complicated in reality, because the
numbers are not as nice as here (but again, the details are not relevant for
understanding the principle). This translation distorts the operating
system's view of how the disk is organized, thus making it impractical to use
the all-data-on-one-cylinder trick to boost performance.

The translation is only a problem for IDE disks. SCSI disks use a sequential
sector number (i.e., the controller translates a sequential sector number to
a head, cylinder, and sector triplet), and a completely different method for
the CPU to talk with the controller, so they are insulated from the problem.
Note, however, that the computer might not know the real geometry of an SCSI
disk either.

Since Linux often will not know the real geometry of a disk, its filesystems
don't even try to keep files within a single cylinder. Instead, it tries to
assign sequentially numbered sectors to files, which almost always gives
similar performance. The issue is further complicated by on-controller
caches, and automatic prefetches done by the controller.

Each hard disk is represented by a separate device file. There can (usually)
be only two or four IDE hard disks. These are known as /dev/had, /dev/hdb, /
dev/hdc, and /dev/hdd, respectively. SCSI hard disks are known as /dev/sda, /
dev/sdb, and so on. Similar naming conventions exist for other hard disk
types; see Chapter 4 for more information. Note that the device files for the
hard disks give access to the entire disk, with no regard to partitions
(which will be discussed below), and it's easy to mess up the partitions or
the data in them if you aren't careful. The disks' device files are usually
used only to get access to the master boot record (which will also be
discussed below).
-----------------------------------------------------------------------------

5.3. Storage Area Networks - Draft

A SAN is a dedicated storage network that provides block level access to
LUNs. A LUN, or logical unit number, is a virtual disk provided by the SAN.
The system administrator the same access and rights to the LUN as if it were
a disk directly attached to it. The administrator can partition, and format
the disk in any means he or she chooses.

Two networking protocols commonly used in a SAN are fibre channel and iSCSI .
A fibre channel network is very fast and is not burdened by the other network
traffic in a company's LAN. However, it's very expensive. Fibre channel cards
cost around $1000.00 USD each. They also require special fibre channel
switches.

iSCSI is a newer technology that sends SCSI commands over a TCP/IP network.
While this method may not be as fast as a Fibre Channel network, it does save
money by using less expensive network hardware.

More To Be Added
-----------------------------------------------------------------------------

5.4. Network Attached Storage - Draft

A NAS uses your companies existing Ethernet network to allow access to shared
disks. This is filesystem level access. The system administrator does not
have the ability to partition or format the disks since they are potentially
shared by multiple computers. This technology is commonly used to provide
multiple workstations access to the same data.

Similar to a SAN, a NAS need to make use of a protocol to allow access to
it's disks. With a NAS this is either CIFS/Samba , or NFS.

Traditionally CIFS was used with Microsoft Windows networks, and NFS was used
with UNIX & Linux networks. However, with Samba, Linux machines can also make
use of CIFS shares.

Does this mean that your Windows 2003 server or your Linux box are NAS
servers because they provide access to shared drives over your network? Yes,
they are. You could also purchase a NAS device from a number of
manufacturers. These devices are specifically designed to provide high speed
access to data.

More To Be Added
-----------------------------------------------------------------------------

5.4.1. NFS

TO BE ADDED
-----------------------------------------------------------------------------

5.4.2. CIFS

TO BE ADDED
-----------------------------------------------------------------------------

5.5. Floppies

A floppy disk consists of a flexible membrane covered on one or both sides
with similar magnetic substance as a hard disk. The floppy disk itself
doesn't have a read-write head, that is included in the drive. A floppy
corresponds to one platter in a hard disk, but is removable and one drive can
be used to access different floppies, and the same floppy can be read by many
drives, whereas the hard disk is one indivisible unit.

Like a hard disk, a floppy is divided into tracks and sectors (and the two
corresponding tracks on either side of a floppy form a cylinder), but there
are many fewer of them than on a hard disk.

A floppy drive can usually use several different types of disks; for example,
a 3.5 inch drive can use both 720 KB and 1.44 MB disks. Since the drive has
to operate a bit differently and the operating system must know how big the
disk is, there are many device files for floppy drives, one per combination
of drive and disk type. Therefore, /dev/fd0H1440 is the first floppy drive
(fd0), which must be a 3.5 inch drive, using a 3.5 inch, high density disk
(H) of size 1440 KB (1440), i.e., a normal 3.5 inch HD floppy.

The names for floppy drives are complex, however, and Linux therefore has a
special floppy device type that automatically detects the type of the disk in
the drive. It works by trying to read the first sector of a newly inserted
floppy using different floppy types until it finds the correct one. This
naturally requires that the floppy is formatted first. The automatic devices
are called /dev/fd0, /dev/fd1, and so on.

The parameters the automatic device uses to access a disk can also be set
using the program setfdprm . This can be useful if you need to use disks that
do not follow any usual floppy sizes, e.g., if they have an unusual number of
sectors, or if the autodetecting for some reason fails and the proper device
file is missing.

Linux can handle many nonstandard floppy disk formats in addition to all the
standard ones. Some of these require using special formatting programs. We'll
skip these disk types for now, but in the mean time you can examine the /etc/
fdprm file. It specifies the settings that setfdprm recognizes.

The operating system must know when a disk has been changed in a floppy
drive, for example, in order to avoid using cached data from the previous
disk. Unfortunately, the signal line that is used for this is sometimes
broken, and worse, this won't always be noticeable when using the drive from
within MS-DOS. If you are experiencing weird problems using floppies, this
might be the reason. The only way to correct it is to repair the floppy
drive.
-----------------------------------------------------------------------------

5.6. CD-ROMs

A CD-ROM drive uses an optically read, plastic coated disk. The information
is recorded on the surface of the disk in small `holes' aligned along a
spiral from the center to the edge. The drive directs a laser beam along the
spiral to read the disk. When the laser hits a hole, the laser is reflected
in one way; when it hits smooth surface, it is reflected in another way. This
makes it easy to code bits, and therefore information. The rest is easy, mere
mechanics.

CD-ROM drives are slow compared to hard disks. Whereas a typical hard disk
will have an average seek time less than 15 milliseconds, a fast CD-ROM drive
can use tenths of a second for seeks. The actual data transfer rate is fairly
high at hundreds of kilobytes per second. The slowness means that CD-ROM
drives are not as pleasant to use as hard disks (some Linux distributions
provide `live' filesystems on CD-ROMs, making it unnecessary to copy the
files to the hard disk, making installation easier and saving a lot of hard
disk space), although it is still possible. For installing new software,
CD-ROMs are very good, since maximum speed is not essential during
installation.

There are several ways to arrange data on a CD-ROM. The most popular one is
specified by the international standard ISO 9660 . This standard specifies a
very minimal filesystem, which is even more crude than the one MS-DOS uses.
On the other hand, it is so minimal that every operating system should be
able to map it to its native system.

For normal UNIX use, the ISO 9660 filesystem is not usable, so an extension
to the standard has been developed, called the Rock Ridge extension. Rock
Ridge allows longer filenames, symbolic links, and a lot of other goodies,
making a CD-ROM look more or less like any contemporary UNIX filesystem. Even
better, a Rock Ridge filesystem is still a valid ISO 9660 filesystem, making
it usable by non-UNIX systems as well. Linux supports both ISO 9660 and the
Rock Ridge extensions; the extensions are recognized and used automatically.

The filesystem is only half the battle, however. Most CD-ROMs contain data
that requires a special program to access, and most of these programs do not
run under Linux (except, possibly, under dosemu, the Linux MS-DOS emulator,
or wine, the Windows emulator.

Ironically perhaps, wine actually stands for ``Wine Is Not an Emulator''.
Wine, more strictly, is an API (Application Program Interface) replacement.
Please see the wine documentation at [http://www.winehq.com] http://
www.winehq.com for more information.

There is also VMWare, a commercial product, which emulates an entire x86
machine in software. See the VMWare website, [http://www.vmware.com] http://
www.vmware.com for more information.

A CD-ROM drive is accessed via the corresponding device file. There are
several ways to connect a CD-ROM drive to the computer: via SCSI, via a sound
card, or via EIDE. The hardware hacking needed to do this is outside the
scope of this book, but the type of connection decides the device file.
-----------------------------------------------------------------------------

5.7. Tapes

A tape drive uses a tape, similar to cassettes used for music. A tape is
serial in nature, which means that in order to get to any given part of it,
you first have to go through all the parts in between. A disk can be accessed
randomly, i.e., you can jump directly to any place on the disk. The serial
access of tapes makes them slow.

On the other hand, tapes are relatively cheap to make, since they do not need
to be fast. They can also easily be made quite long, and can therefore
contain a large amount of data. This makes tapes very suitable for things
like archiving and backups, which do not require large speeds, but benefit
from low costs and large storage capacities.
-----------------------------------------------------------------------------

5.8. Formatting

Formatting is the process of writing marks on the magnetic media that are
used to mark tracks and sectors. Before a disk is formatted, its magnetic
surface is a complete mess of magnetic signals. When it is formatted, some
order is brought into the chaos by essentially drawing lines where the tracks
go, and where they are divided into sectors. The actual details are not quite
exactly like this, but that is irrelevant. What is important is that a disk
cannot be used unless it has been formatted.

The terminology is a bit confusing here: in MS-DOS and MS Windows, the word
formatting is used to cover also the process of creating a filesystem (which
will be discussed below). There, the two processes are often combined,
especially for floppies. When the distinction needs to be made, the real
formatting is called low-level formatting, while making the filesystem is
called high-level formatting . In UNIX circles, the two are called formatting
and making a filesystem, so that's what is used in this book as well.

For IDE and some SCSI disks the formatting is actually done at the factory
and doesn't need to be repeated; hence most people rarely need to worry about
it. In fact, formatting a hard disk can cause it to work less well, for
example because a disk might need to be formatted in some very special way to
allow automatic bad sector replacement to work.

Disks that need to be or can be formatted often require a special program
anyway, because the interface to the formatting logic inside the drive is
different from drive to drive. The formatting program is often either on the
controller BIOS, or is supplied as an MS-DOS program; neither of these can
easily be used from within Linux.

During formatting one might encounter bad spots on the disk, called bad
blocks or bad sectors. These are sometimes handled by the drive itself, but
even then, if more of them develop, something needs to be done to avoid using
those parts of the disk. The logic to do this is built into the filesystem;
how to add the information into the filesystem is described below.
Alternatively, one might create a small partition that covers just the bad
part of the disk; this approach might be a good idea if the bad spot is very
large, since filesystems can sometimes have trouble with very large bad
areas.

Floppies are formatted with fdformat . The floppy device file to use is given
as the parameter. For example, the following command would format a high
density, 3.5 inch floppy in the first floppy drive:
+---------------------------------------------------------------------------+
|        $ fdformat /dev/fd0H1440                                           |
|        Double-sided, 80 tracks, 18 sec/track. Total capacity              |
|        1440 kB.                                                           |
|        Formatting ... done                                                |
|        Verifying ... done                                                 |
|        $                                                                  |
|                                                                           |
+---------------------------------------------------------------------------+
Note that if you want to use an autodetecting device (e.g., /dev/fd0), you
must set the parameters of the device with setfdprm first. To achieve the
same effect as above, one would have to do the following:
+---------------------------------------------------------------------------+
|        $ setfdprm /dev/fd0 1440/1440                                      |
|        $ fdformat /dev/fd0                                                |
|        Double-sided, 80 tracks, 18 sec/track. Total capacity              |
|        1440 KB.                                                           |
|        Formatting ... done                                                |
|        Verifying ... done                                                 |
|        $                                                                  |
|                                                                           |
+---------------------------------------------------------------------------+
It is usually more convenient to choose the correct device file that matches
the type of the floppy. Note that it is unwise to format floppies to contain
more information than what they are designed for.

fdformatalso validate the floppy, i.e., check it for bad blocks. It will try
a bad block several times (you can usually hear this, the drive noise changes
dramatically). If the floppy is only marginally bad (due to dirt on the read/
write head, some errors are false signals), fdformat won't complain, but a
real error will abort the validation process. The kernel will print log
messages for each I/O error it finds; these will go to the console or, if
syslog is being used, to the file /var/log/messages. fdformat itself won't
tell where the error is (one usually doesn't care, floppies are cheap enough
that a bad one is automatically thrown away).
+---------------------------------------------------------------------------+
|        $ fdformat /dev/fd0H1440                                           |
|        Double-sided, 80 tracks, 18 sec/track. Total capacity              |
|        1440 KB.                                                           |
|        Formatting ... done                                                |
|        Verifying ... read: Unknown error                                  |
|        $                                                                  |
|                                                                           |
+---------------------------------------------------------------------------+
The badblocks command can be used to search any disk or partition for bad
blocks (including a floppy). It does not format the disk, so it can be used
to check even existing filesystems. The example below checks a 3.5 inch
floppy with two bad blocks.
+---------------------------------------------------------------------------+
|        $ badblocks /dev/fd0H1440 1440                                     |
|        718                                                                |
|        719                                                                |
|        $                                                                  |
|                                                                           |
+---------------------------------------------------------------------------+
badblocks outputs the block numbers of the bad blocks it finds. Most
filesystems can avoid such bad blocks. They maintain a list of known bad
blocks, which is initialized when the filesystem is made, and can be modified
later. The initial search for bad blocks can be done by the mkfs command
(which initializes the filesystem), but later checks should be done with
badblocks and the new blocks should be added with fsck. We'll describe mkfs
and fsck later.

Many modern disks automatically notice bad blocks, and attempt to fix them by
using a special, reserved good block instead. This is invisible to the
operating system. This feature should be documented in the disk's manual, if
you're curious if it is happening. Even such disks can fail, if the number of
bad blocks grows too large, although chances are that by then the disk will
be so rotten as to be unusable.
-----------------------------------------------------------------------------

5.9. Partitions

A hard disk can be divided into several partitions. Each partition functions
as if it were a separate hard disk. The idea is that if you have one hard
disk, and want to have, say, two operating systems on it, you can divide the
disk into two partitions. Each operating system uses its partition as it
wishes and doesn't touch the other ones. This way the two operating systems
can co-exist peacefully on the same hard disk. Without partitions one would
have to buy a hard disk for each operating system.

Floppies are not usually partitioned. There is no technical reason against
this, but since they're so small, partitions would be useful only very
rarely. CD-ROMs are usually also not partitioned, since it's easier to use
them as one big disk, and there is seldom a need to have several operating
systems on one.
-----------------------------------------------------------------------------

5.9.1. The MBR, boot sectors and partition table

The information about how a hard disk has been partitioned is stored in its
first sector (that is, the first sector of the first track on the first disk
surface). The first sector is the master boot record (MBR) of the disk; this
is the sector that the BIOS reads in and starts when the machine is first
booted. The master boot record contains a small program that reads the
partition table, checks which partition is active (that is, marked bootable),
and reads the first sector of that partition, the partition's boot sector
(the MBR is also a boot sector, but it has a special status and therefore a
special name). This boot sector contains another small program that reads the
first part of the operating system stored on that partition (assuming it is
bootable), and then starts it.

The partitioning scheme is not built into the hardware, or even into the
BIOS. It is only a convention that many operating systems follow. Not all
operating systems do follow it, but they are the exceptions. Some operating
systems support partitions, but they occupy one partition on the hard disk,
and use their internal partitioning method within that partition. The latter
type exists peacefully with other operating systems (including Linux), and
does not require any special measures, but an operating system that doesn't
support partitions cannot co-exist on the same disk with any other operating
system.

As a safety precaution, it is a good idea to write down the partition table
on a piece of paper, so that if it ever corrupts you don't have to lose all
your files. (A bad partition table can be fixed with fdisk). The relevant
information is given by the fdisk -l command:
+---------------------------------------------------------------------------+
