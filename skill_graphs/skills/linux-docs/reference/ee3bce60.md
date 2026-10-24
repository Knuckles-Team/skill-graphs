    reduce this limit.

��*�A maximal time between checks. e2fsck can also enforce a maximal time
    between two checks, even if the clean flag is set, and the filesystem
    hasn't been mounted very often. This can be disabled, however.

��*�Number of blocks reserved for root. Ext2 reserves some blocks for root so
    that if the filesystem fills up, it is still possible to do system
    administration without having to delete anything. The reserved amount is
    by default 5 percent, which on most disks isn't enough to be wasteful.
    However, for floppies there is no point in reserving any blocks.


See the tune2fs manual page for more information.

dumpe2fs shows information about an ext2 or ext3 filesystem, mostly from the
superblock. Below is a sample output. Some of the information in the output
is technical and requires understanding of how the filesystem works, but much
of it is readily understandable even for lay-admins.
+---------------------------------------------------------------------------+
|# dumpe2fs                                                                 |
|dumpe2fs 1.32 (09-Nov-2002)                                                |
|Filesystem volume name:   /                                                |
|Last mounted on:          not available                                    |
|Filesystem UUID:          51603f82-68f3-4ae7-a755-b777ff9dc739             |
|Filesystem magic number:  0xEF53                                           |
|Filesystem revision #:    1 (dynamic)                                      |
|Filesystem features:      has_journal filetype needs_recovery sparse_super |
|Default mount options:    (none)                                           |
|Filesystem state:         clean                                            |
|Errors behavior:          Continue                                         |
|Filesystem OS type:       Linux                                            |
|Inode count:              3482976                                          |
|Block count:              6960153                                          |
|Reserved block count:     348007                                           |
|Free blocks:              3873525                                          |
|Free inodes:              3136573                                          |
|First block:              0                                                |
|Block size:               4096                                             |
|Fragment size:            4096                                             |
|Blocks per group:         32768                                            |
|Fragments per group:      32768                                            |
|Inodes per group:         16352                                            |
|Inode blocks per group:   511                                              |
|Filesystem created:       Tue Aug 26 08:11:55 2003                         |
|Last mount time:          Mon Dec 22 08:23:12 2003                         |
|Last write time:          Mon Dec 22 08:23:12 2003                         |
|Mount count:              3                                                |
|Maximum mount count:      -1                                               |
|Last checked:             Mon Nov  3 11:27:38 2003                         |
|Check interval:           0 (none)                                         |
|Reserved blocks uid:      0 (user root)                                    |
|Reserved blocks gid:      0 (group root)                                   |
|First inode:              11                                               |
|Inode size:               128                                              |
|Journal UUID:             none                                             |
|Journal inode:            8                                                |
|Journal device:           0x0000                                           |
|First orphan inode:       655612                                           |
|                                                                           |
|                                                                           |
|Group 0: (Blocks 0-32767)                                                  |
|  Primary superblock at 0, Group descriptors at 1-2                        |
|  Block bitmap at 3 (+3), Inode bitmap at 4 (+4)                           |
|  Block bitmap at 3 (+3), Inode bitmap at 4 (+4)                           |
|  Inode table at 5-515 (+5)                                                |
|  3734 free blocks, 16338 free inodes, 2 directories                       |
+---------------------------------------------------------------------------+

debugfs is a filesystem debugger. It allows direct access to the filesystem
data structures stored on disk and can thus be used to repair a disk that is
so broken that fsck can't fix it automatically. It has also been known to be
used to recover deleted files. However, debugfs very much requires that you
understand what you're doing; a failure to understand can destroy all your
data.

dump and restore can be used to back up an ext2 filesystem. They are ext2
specific versions of the traditional UNIX backup tools. See Section 12.1 for
more information on backups.
-----------------------------------------------------------------------------

5.11. Disks without filesystems

Not all disks or partitions are used as filesystems. A swap partition, for
example, will not have a filesystem on it. Many floppies are used in a
tape-drive emulating fashion, so that a tar (tape archive) or other file is
written directly on the raw disk, without a filesystem. Linux boot floppies
don't contain a filesystem, only the raw kernel.

Avoiding a filesystem has the advantage of making more of the disk usable,
since a filesystem always has some bookkeeping overhead. It also makes the
disks more easily compatible with other systems: for example, the tar file
format is the same on all systems, while filesystems are different on most
systems. You will quickly get used to disks without filesystems if you need
them. Bootable Linux floppies also do not necessarily have a filesystem,
although they may.

One reason to use raw disks is to make image copies of them. For instance, if
the disk contains a partially damaged filesystem, it is a good idea to make
an exact copy of it before trying to fix it, since then you can start again
if your fixing breaks things even more. One way to do this is to use dd:
+---------------------------------------------------------------------------+
|        $ dd if=/dev/fd0H1440                                              |
|        of=floppy-image                                                    |
|        2880+0 records in                                                  |
|        2880+0 records out                                                 |
|        $ dd if=floppy-image                                               |
|        of=/dev/fd0H1440                                                   |
|        2880+0 records in                                                  |
|        2880+0 records out                                                 |
|        $                                                                  |
|                                                                           |
+---------------------------------------------------------------------------+
The first dd makes an exact image of the floppy to the file floppy-image, the
second one writes the image to the floppy. (The user has presumably switched
the floppy before the second command. Otherwise the command pair is of
doubtful usefulness.)
-----------------------------------------------------------------------------

5.12. Allocating disk space

5.12.1. Partitioning schemes

When it comes to partitioning your machine, there is no universally correct
way to do it. There are many factors that must be taken into account
depending on the purpose of the machine.

For a simple workstation with limited disk space, such as a laptop, you may
have as few a 3 partitions. A partition for /, /boot, and swap. However, for
most users this is not a recommended solution.



The traditional way is to have a (relatively) small root filesystem, and
separate partitions for filesystems such as /usr and /home>. Creating a
separate root filesystem if the root filesystem is small and not heavily
used, it is less likely to become corrupt when the system crashes, and
therefore make it easier to recover a crashed system. The reason is to
prevent having the root filesystem get filled and cause a system crash.

When creating your partitioning scheme, there are some things you need to
remember. You cannot create separate partitions for the following
directories: /bin, /etc, /dev, /initrd, /lib, and /sbin. The contents of
these directories are required at bootup and must always be part of the /
partition.

It is also recommended that you create separate partitions for /var and /tmp.
This is because both directories typically have data that is constantly
changing. Not creating separate partitions for these filesystems puts you at
risk of having log file fill up our / partition.

An example of a server partition is:
+---------------------------------------------------------------------------+
|Filesystem            Size  Used Avail Use% Mounted on                     |
|/dev/hda2             9.7G  1.3G  8.0G  14% /                              |
|/dev/hda1             128M   44M   82M  34% /boot                          |
|/dev/hda3             4.9G  4.0G  670M  86% /usr                           |
|/dev/hda5             4.9G  2.1G  2.5G  46% /var                           |
|/dev/hda7              31G   24G  5.6G  81% /home                          |
|/dev/hda8             4.9G  2.0G  670M  43% /opt                           |
|                                                                           |
+---------------------------------------------------------------------------+

The problem with having many partitions is that it splits the total amount of
free disk space into many small pieces. One way to avoid this problem is to
use to create Logical Volumes.
-----------------------------------------------------------------------------

5.12.2. Logical Volume Manager (LVM)

Using LVM allows administrators the flexibility to create logical disks that
can be expanded dynamically as more disk space is required.

This is done first by creating partitions with as an 0x8e Linux LVM partition
type. Then the Physical Partitions are added to a Volume Group and broken up
into chunks, or Physical Extents Volume Group. These extends can then be
grouped into Logical Volumes. These Logical Volumes then can be formatted
just like a physical partition. The big difference is that they can be
expanded by adding more extents to them.

Right now, a full discussion of LVM is beyond the scope of this guide.
However, and excellent resource for learning more about LVM can be found at
[http://www.tldp.org/HOWTO/LVM-HOWTO.html] http://www.tldp.org/HOWTO/
LVM-HOWTO.html.
-----------------------------------------------------------------------------

5.12.3. Space requirements

The Linux distribution you install will give some indication of how much disk
space you need for various configurations. Programs installed separately may
also do the same. This will help you plan your disk space usage, but you
should prepare for the future and reserve some extra space for things you
will notice later that you need.

The amount you need for user files depends on what your users wish to do.
Most people seem to need as much space for their files as possible, but the
amount they will live happily with varies a lot. Some people do only light
text processing and will survive nicely with a few megabytes, others do heavy
image processing and will need gigabytes.

By the way, when comparing file sizes given in kilobytes or megabytes and
disk space given in megabytes, it can be important to know that the two units
can be different. Some disk manufacturers like to pretend that a kilobyte is
1000 bytes and a megabyte is 1000 kilobytes, while all the rest of the
computing world uses 1024 for both factors. Therefore, a 345 MB hard disk is
really a 330 MB hard disk.

Swap space allocation is discussed in Section 6.5.
-----------------------------------------------------------------------------

5.12.4. Examples of hard disk allocation

I used to have a 10 GB hard disk. Now I am using a 30 GB hard disk. I'll
explain how and why I partitioned those disks.

First, I created a /boot partition at 128 MG. This is larger than I will
need, and big enough to give me space if I need it. I created a separate /
boot partition to ensure that this filesystem will never get filled up, and
therefore will be bootable. Then I created a 5 GB /var partition. Since the /
var filesystem is where log files and email is stored I wanted to isolate it
from my root partition. (I have had log files grow overnight and fill my root
filesystem in the past.) Next, I created a 15 GB /home partition. This is
handy in the event of a system crash. If I ever have to re-install Linux from
scratch, I can tell the installation program to not format this partition,
and instead remount it without the data being lost. Finally since I had 512
MG of RAM I created a 1024 MG (or 1 GB) swap partition. This left me with
roughly a 9 GB root filesystem. I using my old 10 GB hard drive, I created an
8 GB /usr partition and left 2 GB unused. This is in case I need more space in
the future.

In the end, my partition tables looked like this:


Table 5-3. My Partitions
+-----+------------------+
|9 GB |root filesystem   |
+-----+------------------+
|1 GB |swap partition    |
+-----+------------------+
|5 GB |/var filesystem   |
+-----+------------------+
|15 GB|/home filesystem  |
+-----+------------------+
|8 GB |/usr filesystem   |
+-----+------------------+
|2 GB |scratch partition |
+-----+------------------+
-----------------------------------------------------------------------------

5.12.5. Adding more disk space for Linux

Adding more disk space for Linux is easy, at least after the hardware has
been properly installed (the hardware installation is outside the scope of
this book). You format it if necessary, then create the partitions and
filesystem as described above, and add the proper lines to /etc/fstab so that
it is mounted automatically.
-----------------------------------------------------------------------------

5.12.6. Tips for saving disk space

The best tip for saving disk space is to avoid installing unnecessary
programs. Most Linux distributions have an option to install only part of the
packages they contain, and by analyzing your needs you might notice that you
don't need most of them. This will help save a lot of disk space, since many
programs are quite large. Even if you do need a particular package or
program, you might not need all of it. For example, some on-line
documentation might be unnecessary, as might some of the Elisp files for GNU
Emacs, some of the fonts for X11, or some of the libraries for programming.

If you cannot uninstall packages, you might look into compression.
Compression programs such as gzip or zip will compress (and uncompress)
individual files or groups of files. The gzexe system will compress and
uncompress programs invisibly to the user (unused programs are compressed,
then uncompressed as they are used). The experimental DouBle system will
compress all files in a filesystem, invisibly to the programs that use them.
(If you are familiar with products such as Stacker for MS-DOS or DriveSpace
for Windows, the principle is the same.)

Another way to save space is to take special care when formatting you
partitions. Most modern filesystems will allow you to specify the block size.
The block size is chunk size that the filesystem will use to read and write
data. Larger block sizes will help disk I/O performance when using large
files, such as databases. This happens because the disk can read or write
data for a longer period of time before having to search for the next block.
The
-----------------------------------------------------------------------------

Chapter 6. Memory Management

    "Minnet, jag har tappat mitt minne, �r jag svensk eller finne, kommer
    inte ih�g..." (Bosse �sterberg)

    A Swedish drinking song, (rough) translation: ``Memory, I have lost my
    memory. Am I Swedish or Finnish? I can't remember''

This section describes the Linux memory management features, i.e., virtual
memory and the disk buffer cache. The purpose and workings and the things the
system administrator needs to take into consideration are described.
-----------------------------------------------------------------------------

6.1. What is virtual memory?

Linux supports virtual memory, that is, using a disk as an extension of RAM
so that the effective size of usable memory grows correspondingly. The kernel
will write the contents of a currently unused block of memory to the hard
disk so that the memory can be used for another purpose. When the original
contents are needed again, they are read back into memory. This is all made
completely transparent to the user; programs running under Linux only see the
larger amount of memory available and don't notice that parts of them reside
on the disk from time to time. Of course, reading and writing the hard disk
is slower (on the order of a thousand times slower) than using real memory,
so the programs don't run as fast. The part of the hard disk that is used as
virtual memory is called the swap space.

Linux can use either a normal file in the filesystem or a separate partition
for swap space. A swap partition is faster, but it is easier to change the
size of a swap file (there's no need to repartition the whole hard disk, and
possibly install everything from scratch). When you know how much swap space
you need, you should go for a swap partition, but if you are uncertain, you
can use a swap file first, use the system for a while so that you can get a
feel for how much swap you need, and then make a swap partition when you're
confident about its size.

You should also know that Linux allows one to use several swap partitions and
/or swap files at the same time. This means that if you only occasionally
need an unusual amount of swap space, you can set up an extra swap file at
such times, instead of keeping the whole amount allocated all the time.

A note on operating system terminology: computer science usually
distinguishes between swapping (writing the whole process out to swap space)
and paging (writing only fixed size parts, usually a few kilobytes, at a
time). Paging is usually more efficient, and that's what Linux does, but
traditional Linux terminology talks about swapping anyway.
-----------------------------------------------------------------------------

6.2. Creating a swap space

A swap file is an ordinary file; it is in no way special to the kernel. The
only thing that matters to the kernel is that it has no holes, and that it is
prepared for use with mkswap. It must reside on a local disk, however; it
can't reside in a filesystem that has been mounted over NFS due to
implementation reasons.

The bit about holes is important. The swap file reserves the disk space so
that the kernel can quickly swap out a page without having to go through all
the things that are necessary when allocating a disk sector to a file. The
kernel merely uses any sectors that have already been allocated to the file.
Because a hole in a file means that there are no disk sectors allocated (for
that place in the file), it is not good for the kernel to try to use them.

One good way to create the swap file without holes is through the following
command:
+---------------------------------------------------------------------------+
|        $ dd if=/dev/zero of=/extra-swap bs=1024                           |
|        count=1024                                                         |
|        1024+0 records in                                                  |
|        1024+0 records out                                                 |
|        $                                                                  |
|                                                                           |
+---------------------------------------------------------------------------+
where /extra-swap is the name of the swap file and the size of is given after
the count=. It is best for the size to be a multiple of 4, because the kernel
writes out memory pages, which are 4 kilobytes in size. If the size is not a
multiple of 4, the last couple of kilobytes may be unused.

A swap partition is also not special in any way. You create it just like any
other partition; the only difference is that it is used as a raw partition,
that is, it will not contain any filesystem at all. It is a good idea to mark
swap partitions as type 82 (Linux swap); this will the make partition
listings clearer, even though it is not strictly necessary to the kernel.

After you have created a swap file or a swap partition, you need to write a
signature to its beginning; this contains some administrative information and
is used by the kernel. The command to do this is mkswap, used like this:
+---------------------------------------------------------------------------+
|        $ mkswap /extra-swap 1024                                          |
|        Setting up swapspace, size = 1044480                               |
|        bytes                                                              |
|        $                                                                  |
|                                                                           |
+---------------------------------------------------------------------------+
Note that the swap space is still not in use yet: it exists, but the kernel
does not use it to provide virtual memory.

You should be very careful when using mkswap, since it does not check that
the file or partition isn't used for anything else. You can easily overwrite
important files and partitions with mkswap! Fortunately, you should only need
to use mkswap when you install your system.

The Linux memory manager limits the size of each swap space to 2 GB. You can,
however, use up to 8 swap spaces simultaneously, for a total of 16GB.
-----------------------------------------------------------------------------

6.3. Using a swap space

An initialized swap space is taken into use with swapon. This command tells
the kernel that the swap space can be used. The path to the swap space is
given as the argument, so to start swapping on a temporary swap file one
might use the following command.
+---------------------------------------------------------------------------+
|$ swapon /extra-swap                                                       |
|$                                                                          |
+---------------------------------------------------------------------------+
Swap spaces can be used automatically by listing them in the /etc/fstab file.
+---------------------------------------------------------------------------+
|/dev/hda8        none        swap        sw     0     0                    |
|/swapfile        none        swap        sw     0     0                    |
+---------------------------------------------------------------------------+
The startup scripts will run the command swapon -a, which will start swapping
on all the swap spaces listed in /etc/fstab. Therefore, the swapon command is
usually used only when extra swap is needed.

You can monitor the use of swap spaces with free. It will tell the total
amount of swap space used.
+---------------------------------------------------------------------------+
|$ free                                                                     |
|             total       used       free     shared                        |
| buffers                                                                   |
|Mem:         15152      14896        256      12404       2528             |
|-/+ buffers:            12368       2784                                   |
|Swap:        32452       6684      25768                                   |
|$                                                                          |
+---------------------------------------------------------------------------+
The first line of output (Mem:) shows the physical memory. The total column
does not show the physical memory used by the kernel, which is usually about
a megabyte. The used column shows the amount of memory used (the second line
does not count buffers). The free column shows completely unused memory. The
shared column shows the amount of memory shared by several processes; the
more, the merrier. The buffers column shows the current size of the disk
buffer cache.

That last line (Swap:) shows similar information for the swap spaces. If this
line is all zeroes, your swap space is not activated.

The same information is available via top, or using the proc filesystem in
file /proc/meminfo. It is currently difficult to get information on the use
of a specific swap space.

A swap space can be removed from use with swapoff. It is usually not
necessary to do it, except for temporary swap spaces. Any pages in use in the
swap space are swapped in first; if there is not sufficient physical memory
