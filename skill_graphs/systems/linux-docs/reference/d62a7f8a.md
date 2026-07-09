unmounted. This operation involves erasing the superblock from the volume so
the file system will not be recognized in the future. There are no options
available for removing file systems.
-----------------------------------------------------------------------------

F.4. Expanding JFS file systems

 A JFS file system is automatically expanded when its volume is expanded.
However, JFS only allows the volume to be expanded if it is mounted, because
JFS performs all of its expansions online. In addition, JFS only allows
expansions if version 1.0.21 or later of the JFS utilities are installed.
-----------------------------------------------------------------------------

F.5. Shrinking JFS file systems

 At this time, JFS does not support shrinking its file systems. Hence,
volumes with JFS file systems cannot be shrunk.
-----------------------------------------------------------------------------

Appendix G. XFS file system interface module

 The XFS FSIM lets EVMS users create and manage XFS file systems from within
the EVMS interfaces. In order to use the XFS FSIM, version 2.0.0 or later of
the XFS utilities must be installed on your system. The latest version of XFS
can be found at [http://oss.sgi.com/projects/xfs/] http://oss.sgi.com/
projects/xfs/.
-----------------------------------------------------------------------------

G.1. Creating XFS file systems

 XFS file systems can be created with mkfs on any EVMS or compatibility
volume that does not already have a file system. The following options are
available for creating XFS file systems:

vollabel
    Specify a volume label for the file system. The default is none.

journalvol
    Specify the volume to use for an external journal. The default is none.

logsize
     Specify the inline log size (in MB). This option is only available if
    the journalvol option is not set. The default is 4 MB; the allowed range
    is 2 to 256 MB.


-----------------------------------------------------------------------------
G.2. Checking XFS file systems

 The following options are available for checking XFS file systems with fsck:

readonly
    Check the file system is in read-only mode. Report but do not fix errors.
    The default is false.

verbose
    Display details and debugging information during the check. The default
    is false.


-----------------------------------------------------------------------------
G.3. Removing XFS file systems

 An XFS file system can be removed from its volume if the file system is
unmounted. This operation involves erasing the superblock from the volume so
the file system will not be recognized in the future. There are no options
available for removing file systems.
-----------------------------------------------------------------------------

G.4. Expanding XFS file systems

 An XFS file system is automatically expanded when its volume is expanded.
However, XFS only allows the volume to be expanded if it is mounted, because
XFS performs all of its expansions online.
-----------------------------------------------------------------------------

G.5. Shrinking XFS file systems

 At this time, XFS does not support shrinking its file systems. Hence,
volumes with XFS file systems cannot be shrunk.
-----------------------------------------------------------------------------

Appendix H. ReiserFS file system interface module

 The ReiserFS FSIM lets EVMS users create and manage ReiserFS file systems
from within the EVMS interfaces. In order to use the ReiserFS FSIM, version
3.x.0 or later of the ReiserFS utilities must be installed on your system. In
order to get full functionality from the ReiserFS FSIM, use version 3.x.1b or
later. The latest version of ReiserFS can be found at [http://www.namesys.com
/] http://www.namesys.com/.
-----------------------------------------------------------------------------

H.1. Creating ReiserFS file systems

 ReiserFS file systems can be created with mkfs on any EVMS or compatibility
volume that does not already have a file system. The following option is
available for creating ReiserFS file systems:

vollabel
    Specify a volume label for the file system. The default is none.


-----------------------------------------------------------------------------
H.2. Checking ReiserFS file systems

 The following option is available for checking XFS file systems with fsck:

mode
    There are three possible modes for checking a ReiserFS file system: Check
    Read-Only, Fix, and Rebuild Tree."


-----------------------------------------------------------------------------
H.3. Removing ReiserFS file systems

 A ReiserFS file system can be removed from its volume if the file system is
unmounted. This operation involves erasing the superblock from the volume so
the file system will not be recognized in the future. There are no options
available for removing file systems.
-----------------------------------------------------------------------------

H.4. Expanding ReiserFS file systems

 A ReiserFS file system is automatically expanded when its volume is
expanded. ReiserFS file systems can be expanded if the volume is mounted or
unmounted.
-----------------------------------------------------------------------------

H.5. Shrinking ReiserFS file systems

 A ReiserFS file system is automatically shrunk if the volume is shrunk.
ReiserFS file systems can only be shrunk if the volume is unmounted.
-----------------------------------------------------------------------------

Appendix I. Ext-2/3 file system interface module

 The Ext-2/3 FSIM lets EVMS users create and manage Ext2 and Ext3 file
systems from within the EVMS interfaces. In order to use the Ext-2/3 FSIM,
the e2fsprogs package must be installed on your system. The e2fsprogs package
can be found at [http://e2fsprogs.sourceforge.net/] http://
e2fsprogs.sourceforge.net/.
-----------------------------------------------------------------------------

I.1. Creating Ext-2/3 file systems

 Ext-2/3 file systems can be created with mkfs on any EVMS or compatibility
volume that does not already have a file system. The following options are
available for creating Ext-2/3 file systems:

badblocks
    Perform a read-only check for bad blocks on the volume before creating
    the file system. The default is false.

badblocks_rw
    Perform a read/write check for bad blocks on the volume before creating
    the file system. The default is false.

vollabel
    Specify a volume label for the file system. The default is none.

journal
    Create a journal for use with the Ext2 file system. The default is true.


-----------------------------------------------------------------------------
I.2. Checking Ext-2/3 file systems

 The following options are available for checking Ext-2/3 file systems with
fsck:

force
    Force a complete file system check, even if the file system is already
    marked clean. The default is false.

readonly
    Check the file system is in read-only mode. Report but do not fix errors.
    If the file system is mounted, this option is automatically selected. The
    default is false.

badblocks
    Check for bad blocks on the volume and mark them as busy. The default is
    false.

badblocks_rw
    Perform a read-write check for bad blocks on the volume and mark them as
    busy. The default is false.


-----------------------------------------------------------------------------
I.3. Removing Ext-2/3 file systems

 An Ext-2/3 file system can be removed from its volume if the file system is
unmounted. This operation involves erasing the superblock from the volume so
the file system will not be recognized in the future. There are no options
available for removing file systems.
-----------------------------------------------------------------------------

I.4. Expanding and shrinking Ext-2/3 file systems

 An Ext-2/3 file system is automatically expanded or shrunk when its volume
is expanded or shrunk. However, Ext-2/3 only allows these operations if the
volume is unmounted, because online expansion and shrinkage is not yet
supported.
-----------------------------------------------------------------------------

Appendix J. OpenGFS file system interface module

 The OpenGFS FSIM lets EVMS users create and manage OpenGFS file systems from
within the EVMS interfaces. In order to use the OpenGFS FSIM, the OpenGFS
utilities must be installed on your system. Go to [http://sourceforge.net/
projects/opengfs] http://sourceforge.net/projects/opengfs for the OpenGFS
project.
-----------------------------------------------------------------------------

J.1. Creating OpenGFS file systems

 OpenGFS file systems can be created with mkfs on any EVMS or compatibility
volume that does not already have a file system and that is produced from a
shared cluster container. The following options are available for creating
OpenGFS file systems:

blocksize
    Set the file system block size. The block size is in bytes. The block
    size must be a power of 2 between 512 and 65536, inclusive. The default
    block size is 4096 bytes.

journals
    The names of the journal volumes, one for each node.

protocol
    Specify the name of the locking protocol to use. The choices are "memexp"
    and "opendlm."

lockdev
    Specify the shared volume to be used to contain the locking metadata.


 The OpenGFS FSIM only takes care of file system operations. It does not take
care of OpenGFS cluster and node configuration. Before the volumes can be
mounted, you must configure the cluster and node separately after you have
made the file system and saved the changes.
-----------------------------------------------------------------------------

J.2. Checking OpenGFS file systems

 The OpenGFS utility for checking the file system has no additional options.
-----------------------------------------------------------------------------

J.3. Removing OpenGFS file systems

 An OpenGFS file system can be removed from its volume if the file system is
unmounted. This operation involves erasing the superblock from the volume,
erasing the log headers for the journal volumes, and erasing the control
block on the cluster configuration volume associated with the file system
volume so that the file system will not be recognized in the future. There
are no options available for removing file systems.
-----------------------------------------------------------------------------

J.4. Expanding and shrinking OpenGFS file systems

 OpenGFS only allows a volume to be expanded. OpenGFS only allows a volume to
expanded when the volume is mounted. An OpenGFS file system is automatically
expanded when its volume is expanded.
-----------------------------------------------------------------------------

Appendix K. NTFS file system interface module

 The NTFS FSIM lets EVMS users create and manage Windows� NT� file systems
from within the EVMS interfaces.
-----------------------------------------------------------------------------

K.1. Creating NTFS file systems

 NTFS file systems can be created with mkfs on any EVMS or compatibility
volume that is at least 1 MB in size and that does not already have a file
system. The following options are available for creating NTFS file systems:

label
     Specify a volume label for the file system. The default is none.

cluster-size
    Specify the size of clusters in bytes. Valid cluster size values are
    powers of two, with at least 256, and at most 65536 bytes per cluster. If
    omitted, mkntfs cluster-size is determined by the volume size. The value
    is determined as follows:
    Volume size     Default cluster

    0-512 MB        512 bytes
    512 MB-1 GB     1024 bytes
    1 GB-2 GB       2048 bytes
    2 GB+           4096 bytes

mft-zone-mult
    Set the MFT zone multiplier, which determines the size of the MFT zone to
    use on the volume. The MFT zone is the area at the beginning of the
    volume reserved for the master file table (MFT), which stores the on disk
    inodes (MFT records). Note that small files are stored entirely within
    the node. Thus, if you expect to use the volume for storing large numbers
    of very small files, it is useful to set the zone multiplier to a higher
    value. Note that the MFT zone is resized on the fly as required during
    operation of the NTFS driver, but choosing a good value will reduce
    fragmentation. Valid values are 12.5 (the default), 25, 37.5, and 50.

compress
    Enable compression on the volume.

quick
    Perform quick format. This skips both zeroing of the volume and bad
    sector checking.


-----------------------------------------------------------------------------
K.2. Fixing NTFS file systems

 The NTFS FSIM can run the ntfsfix utility on an NTFS file system.

 ntfsfix fixes NTFS partitions altered in any manner with the Linux NTFS
driver. ntfsfix is not a Linux version of chkdsk. ntfsfix only tries to leave
the NTFS partition in a not-so-inconsistent state after the NTFS driver has
written to it.

 Running ntfsfix after mounting an NTFS volume read-write is recommended for
reducing the chance of severe data loss when Windows NT or Windows 2000 tries
to remount the affected volume.

 In order to use ntfsfix, you must unmount the NTFS volume. After running
ntfsfix, you can safely reboot into Windows NT or Windows 2000. Please note
that ntfsfix is not an fsck-like tool. ntfsfix is not guaranteed to fix all
the alterations provoked by the NTFS driver.

 The following option is available for running ntfsfix on an NTFS file
system:

force
     Force ntfsfix to write changes even if it detects that the file system
    is dirty. The default is false.


-----------------------------------------------------------------------------
K.3. Cloning NTFS file systems

 The NTFS FSIM can run the ntfsclone utility to copy an NTFS file system from
one volume to another. ntfsclone is faster than dd because it only copies the
files and the file system data instead of the entire contents of the volume.

 The following options are available for running ntfsclone on an NTFS file
system:

target
    The volume onto which the file system should be cloned.

force
     Force ntfsclone to copy the file system even if it detects that the
    volume is dirty. The default is false.


-----------------------------------------------------------------------------
K.4. Removing NTFS file systems

 An NTFS file system can be removed from its volume if the file system is
unmounted. This operation involves erasing the superblock from the volume so
the file system will not be recognized in the future. There are no options
available for removing file systems.
-----------------------------------------------------------------------------

K.5. Expanding and shrinking NTFS file systems

 An NTFS file system is automatically expanded or shrunk when its volume is
expanded for shrunk. However, NTFS only allows these operations if the volume
is unmounted.

```
