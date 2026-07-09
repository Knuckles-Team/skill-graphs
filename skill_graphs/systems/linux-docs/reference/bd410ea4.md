See [Section D.2.5](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#renamereg2) for more information about the effects of renaming the regions.
* * *
#  D.2. Region operations
##  D.2.1. Creating LVM2 regions
You create LVM2 regions from the freespace in LVM2 containers. If there is at least one extent of freespace in the container, you can create a new region.
The following options are available for creating LVM2 regions:

name

The name of the new region.

size

The size of the new region. This size must be a multiple of the container's extent-size. If it isn't, the size will be rounded down as appropriate. By default, all of the available freespace in the container will be used for the new region.

stripes

If the container consumes two or more objects, and each object has unallocated extents, then the new region can be striped across multiple objects. This is similar to RAID-0 striping and achieves an increased amount of I/O throughput. This option specifies how many objects the new region should be striped across. By default, new regions are not striped, and this value is set to 1.

stripe_size

The granularity of striping. The default value is 64 KB. Use this option only if the stripes option is greater than 1.

pvs

A list of names of the objects the new region should map to. By default, this list is empty, which means all available objects will be used to allocate space to the new region.
* * *
##  D.2.2. Expanding LVM2 regions
You can expand an existing LVM region if there are any unused extents in the container. The following options are available for expanding LVM regions.

size

The amount of space to add to the region. This is a delta-size, not the new absolute size of the region. As with creating new regions, this size must be a multiple of the container's extent-size, and will be rounded down if necessary.

stripes

The number of objects to stripe this new portion of the region across. This value can be different than the number of stripes in the existing region. For example, if the region was created originally with three stripes, but now only two objects are available, then the new portion of the region could be striped across just those two objects. The number of stripes for the last mapping in the region will be used as the default.

stripe_size

The granularity of striping. As with the number of stripes, this value can be different than the stripe-size for the existing region. By default, the stripe-size of the last mapping in the region is used.

pvs

A list of names of the objects the region should be expanded onto. By default, this list is empty, which means all available objects will be used to allocate additional space for the region.
* * *
##  D.2.3. Shrinking LVM2 regions
You can shrink an existing LVM region by removing extents from the end of the region. Regions must have at least one extent, so regions cannot be shrunk to zero.
The following options are available when shrinking LVM regions. Because regions are always shrunk by removing space from the end of the region, a list of objects cannot be specified in this command.

size

The amount of space to remove from the region. This is a delta-size, not the new absolute size of the region. As with creating and expanding regions, this size must be a multiple of the container's extent-size, and will be rounded down if necessary.
* * *
##  D.2.4. Deleting LVM2 regions
You can delete an existing LVM region as long as it is not currently a compatibility volume, an EVMS volume, or consumed by another EVMS plug-in. No options are available for deleting LVM regions.
* * *
##  D.2.5. Renaming LVM2 regions
You can rename an existing LVM2 region. In the EVMS GUI and text-mode UIs, this is done using the **modify properties** command, which is available through the "Actions" menu or the context-sensitive pop-up menus. In the EVMS CLI, this is done using the **set** command.
If the renamed LVM2 region has a compatibility volume on it, then the name of that compatibility volume will also change. In order for this to work correctly, that volume must be unmounted before the name is changed. Also, be sure to update your `/etc/fstab` file if the volume is listed, or the volume won't be mounted properly the next time the system boots.
If the renamed LVM2 region has an EVMS volume or another storage object built on it, then the region's name change will be transparent to the upper layers. In this case, the rename can be done while the volume is mounted.
* * *
#  Appendix E. The CSM plug-in
The Cluster Segment Manager (CSM) is the EVMS plug-in that identifies and manages cluster storage. The CSM protects disk storage objects by writing metadata at the start and end of the disk, which prevents other plug-ins from attempting to use the disk. Other plug-ins can look at the disk, but they cannot see their own metadata signatures and cannot consume the disk. The protection that CSM provides allows the CSM to discover cluster storage and present it in an appropriate fashion to the system.
All cluster storage disk objects must be placed in containers that have the following attributes:
  * cluster ID that identifies the cluster management software
  * node ID that identifies the owner of the disk objects
  * storage type: private, shared, or deported


The CSM plug-in reads metadata and constructs containers that consume the disk object. Each disk provides a usable area, mapped as an EVMS data segment, but only if the disk is accessible to the node viewing the storage.
The CSM plug-in performs these operations:
  * examines disk objects
  * creates containers
  * uses the containers to consume disk objects
  * produces data segment objects if the disk is accessible to the node


* * *
#  E.1. Assigning the CSM plug-in
Assigning a segment manager to a disk means that you want the plug-in to manage partitions on the disk. In order to do this, the plug-in needs to create and maintain appropriate metadata. The CSM creates the follow three segments on the disk:
  * primary metadata segment
  * usable area data segment
  * secondary metadata segment


The CSM collects the information it needs to perform the assign operation with the following options:

NodeId

Choose only from a list of configured node IDs that have been provided to the CSM by clustering software. The default selection is the node from which you are running the EVMS user interface.

Container Name

The name for the container. You need to keep this name unique across the cluster to prevent name-in-conflict errors should the container fail over to another node that has a container with the same name.

Storage Type

Can be either: share, private, or deported.
Note that you would typically assign the CSM to a disk when you want to add a disk to an existing CSM container. If you are creating a new container, you have a choice of using either: Actions->Create->Container or Actions->Add->Segment Manager.
If the container doesn't exist, it will be created for the disk. If the container already exists, the disk will be added to it.
* * *
#  E.2. Unassigning the CSM plug-in
Unassigning a CSM plug-in results in the CSM removing its metadata from the specified disk storage object. The result is that the disk has no segments mapped and appears as a raw disk object. The disk is removed from the container that consumed it and the data segment is removed as well.
* * *
#  E.3. Deleting a CSM container
An existing CSM container cannot be deleted if it is producing any data segments, because other EVMS plug-ins might be building higher-level objects on the CSM objects. To delete a CSM container, first remove disk objects from the container. When the last disk is removed, the container is also removed.
* * *
#  Appendix F. JFS file system interface module
The JFS FSIM lets EVMS users create and manage JFS file systems from within the EVMS interfaces. In order to use the JFS FSIM, version 1.0.9 or later of the JFS utilities must be installed on your system. The latest version of JFS can be found at
* * *
#  F.1. Creating JFS file systems
JFS file systems can be created with **mkfs** on any EVMS or compatibility volume (at least 16 MB in size) that does not already have a file system. The following options are available for creating JFS file systems:

badblocks

Perform a read-only check for bad blocks on the volume before creating the file system. The default is false.

caseinsensitive

Mark the file system as case-insensitive (for OS/2 compatibility). The default is false.

vollabel

Specify a volume label for the file system. The default is none.

journalvol

Specify the volume to use for an external journal. This option is only available with version 1.0.20 or later of the JFS utilities. The default is none.

logsize

Specify the inline log size (in MB). This option is only available if the journalvol option is not set. The default is 0.4% of the size of the volume up to 32 MB.
* * *
#  F.2. Checking JFS file systems
The following options are available for checking JFS file systems with **fsck** :

force

Force a complete file system check, even if the file system is already marked clean. The default is false.

readonly

Check the file system is in read-only mode. Report but do not fix errors. If the file system is mounted, this option is automatically selected. The default is false.

omitlog

Omit replaying the transaction log. This option should only be specified if the log is corrupt. The default is false.

verbose

Display details and debugging information during the check. The default is false.

version

Display the version of `fsck.jfs` and exit without checking the file system. The default is false.
* * *
#  F.3. Removing JFS file systems
A JFS file system can be removed from its volume if the file system is unmounted. This operation involves erasing the superblock from the volume so the file system will not be recognized in the future. There are no options available for removing file systems.
* * *
#  F.4. Expanding JFS file systems
A JFS file system is automatically expanded when its volume is expanded. However, JFS only allows the volume to be expanded if it is mounted, because JFS performs all of its expansions online. In addition, JFS only allows expansions if version 1.0.21 or later of the JFS utilities are installed.
* * *
#  F.5. Shrinking JFS file systems
At this time, JFS does not support shrinking its file systems. Hence, volumes with JFS file systems cannot be shrunk.
* * *
#  Appendix G. XFS file system interface module
The XFS FSIM lets EVMS users create and manage XFS file systems from within the EVMS interfaces. In order to use the XFS FSIM, version 2.0.0 or later of the XFS utilities must be installed on your system. The latest version of XFS can be found at
* * *
#  G.1. Creating XFS file systems
XFS file systems can be created with **mkfs** on any EVMS or compatibility volume that does not already have a file system. The following options are available for creating XFS file systems:

vollabel

Specify a volume label for the file system. The default is none.

journalvol

Specify the volume to use for an external journal. The default is none.

logsize

Specify the inline log size (in MB). This option is only available if the journalvol option is not set. The default is 4 MB; the allowed range is 2 to 256 MB.
* * *
#  G.2. Checking XFS file systems
The following options are available for checking XFS file systems with **fsck** :

readonly

Check the file system is in read-only mode. Report but do not fix errors. The default is false.

verbose

Display details and debugging information during the check. The default is false.
* * *
#  G.3. Removing XFS file systems
An XFS file system can be removed from its volume if the file system is unmounted. This operation involves erasing the superblock from the volume so the file system will not be recognized in the future. There are no options available for removing file systems.
* * *
#  G.4. Expanding XFS file systems
An XFS file system is automatically expanded when its volume is expanded. However, XFS only allows the volume to be expanded if it is mounted, because XFS performs all of its expansions online.
* * *
#  G.5. Shrinking XFS file systems
At this time, XFS does not support shrinking its file systems. Hence, volumes with XFS file systems cannot be shrunk.
* * *
#  Appendix H. ReiserFS file system interface module
The ReiserFS FSIM lets EVMS users create and manage ReiserFS file systems from within the EVMS interfaces. In order to use the ReiserFS FSIM, version 3.x.0 or later of the ReiserFS utilities must be installed on your system. In order to get full functionality from the ReiserFS FSIM, use version 3.x.1b or later. The latest version of ReiserFS can be found at
* * *
#  H.1. Creating ReiserFS file systems
ReiserFS file systems can be created with **mkfs** on any EVMS or compatibility volume that does not already have a file system. The following option is available for creating ReiserFS file systems:

vollabel

Specify a volume label for the file system. The default is none.
* * *
#  H.2. Checking ReiserFS file systems
The following option is available for checking XFS file systems with **fsck** :

mode

There are three possible modes for checking a ReiserFS file system: Check Read-Only, Fix, and Rebuild Tree."
* * *
#  H.3. Removing ReiserFS file systems
A ReiserFS file system can be removed from its volume if the file system is unmounted. This operation involves erasing the superblock from the volume so the file system will not be recognized in the future. There are no options available for removing file systems.
* * *
#  H.4. Expanding ReiserFS file systems
A ReiserFS file system is automatically expanded when its volume is expanded. ReiserFS file systems can be expanded if the volume is mounted or unmounted.
* * *
#  H.5. Shrinking ReiserFS file systems
A ReiserFS file system is automatically shrunk if the volume is shrunk. ReiserFS file systems can only be shrunk if the volume is unmounted.
* * *
#  Appendix I. Ext-2/3 file system interface module
The Ext-2/3 FSIM lets EVMS users create and manage Ext2 and Ext3 file systems from within the EVMS interfaces. In order to use the Ext-2/3 FSIM, the e2fsprogs package must be installed on your system. The e2fsprogs package can be found at
* * *
#  I.1. Creating Ext-2/3 file systems
Ext-2/3 file systems can be created with **mkfs** on any EVMS or compatibility volume that does not already have a file system. The following options are available for creating Ext-2/3 file systems:

badblocks

Perform a read-only check for bad blocks on the volume before creating the file system. The default is false.

badblocks_rw

Perform a read/write check for bad blocks on the volume before creating the file system. The default is false.

vollabel

Specify a volume label for the file system. The default is none.

journal

Create a journal for use with the Ext2 file system. The default is true.
* * *
#  I.2. Checking Ext-2/3 file systems
The following options are available for checking Ext-2/3 file systems with **fsck** :

force

Force a complete file system check, even if the file system is already marked clean. The default is false.

readonly

Check the file system is in read-only mode. Report but do not fix errors. If the file system is mounted, this option is automatically selected. The default is false.

badblocks

Check for bad blocks on the volume and mark them as busy. The default is false.

badblocks_rw

Perform a read-write check for bad blocks on the volume and mark them as busy. The default is false.
* * *
#  I.3. Removing Ext-2/3 file systems
An Ext-2/3 file system can be removed from its volume if the file system is unmounted. This operation involves erasing the superblock from the volume so the file system will not be recognized in the future. There are no options available for removing file systems.
* * *
#  I.4. Expanding and shrinking Ext-2/3 file systems
An Ext-2/3 file system is automatically expanded or shrunk when its volume is expanded or shrunk. However, Ext-2/3 only allows these operations if the volume is unmounted, because online expansion and shrinkage is not yet supported.
* * *
#  Appendix J. OpenGFS file system interface module
The OpenGFS FSIM lets EVMS users create and manage OpenGFS file systems from within the EVMS interfaces. In order to use the OpenGFS FSIM, the OpenGFS utilities must be installed on your system. Go to
* * *
#  J.1. Creating OpenGFS file systems
OpenGFS file systems can be created with **mkfs** on any EVMS or compatibility volume that does not already have a file system and that is produced from a shared cluster container. The following options are available for creating OpenGFS file systems:

blocksize

Set the file system block size. The block size is in bytes. The block size must be a power of 2 between 512 and 65536, inclusive. The default block size is 4096 bytes.

journals

The names of the journal volumes, one for each node.

protocol

Specify the name of the locking protocol to use. The choices are "memexp" and "opendlm."

lockdev

Specify the shared volume to be used to contain the locking metadata.
The OpenGFS FSIM only takes care of file system operations. It does not take care of OpenGFS cluster and node configuration. Before the volumes can be mounted, you must configure the cluster and node separately after you have made the file system and saved the changes.
* * *
#  J.2. Checking OpenGFS file systems
The OpenGFS utility for checking the file system has no additional options.
* * *
#  J.3. Removing OpenGFS file systems
An OpenGFS file system can be removed from its volume if the file system is unmounted. This operation involves erasing the superblock from the volume, erasing the log headers for the journal volumes, and erasing the control block on the cluster configuration volume associated with the file system volume so that the file system will not be recognized in the future. There are no options available for removing file systems.
* * *
#  J.4. Expanding and shrinking OpenGFS file systems
OpenGFS only allows a volume to be expanded. OpenGFS only allows a volume to expanded when the volume is mounted. An OpenGFS file system is automatically expanded when its volume is expanded.
* * *
#  Appendix K. NTFS file system interface module
The NTFS FSIM lets EVMS users create and manage Windows� NT� file systems from within the EVMS interfaces.
* * *
#  K.1. Creating NTFS file systems
NTFS file systems can be created with **mkfs** on any EVMS or compatibility volume that is at least 1 MB in size and that does not already have a file system. The following options are available for creating NTFS file systems:

label

Specify a volume label for the file system. The default is none.

cluster-size

Specify the size of clusters in bytes. Valid cluster size values are powers of two, with at least 256, and at most 65536 bytes per cluster. If omitted, mkntfs cluster-size is determined by the volume size. The value is determined as follows:
```

Volume size	Default cluster

0-512 MB	512 bytes
512 MB-1 GB	1024 bytes
1 GB-2 GB	2048 bytes
2 GB+		4096 bytes

```

---

mft-zone-mult

Set the MFT zone multiplier, which determines the size of the MFT zone to use on the volume. The MFT zone is the area at the beginning of the volume reserved for the master file table (MFT), which stores the on disk inodes (MFT records). Note that small files are stored entirely within the node. Thus, if you expect to use the volume for storing large numbers of very small files, it is useful to set the zone multiplier to a higher value. Note that the MFT zone is resized on the fly as required during operation of the NTFS driver, but choosing a good value will reduce fragmentation. Valid values are 12.5 (the default), 25, 37.5, and 50.

compress

Enable compression on the volume.

quick

Perform quick format. This skips both zeroing of the volume and bad sector checking.
* * *
#  K.2. Fixing NTFS file systems
The NTFS FSIM can run the **ntfsfix** utility on an NTFS file system.
**ntfsfix** fixes NTFS partitions altered in any manner with the Linux NTFS driver. **ntfsfix** is not a Linux version of **chkdsk**. **ntfsfix** only tries to leave the NTFS partition in a not-so-inconsistent state after the NTFS driver has written to it.
Running **ntfsfix** after mounting an NTFS volume read-write is recommended for reducing the chance of severe data loss when Windows NT or Windows 2000 tries to remount the affected volume.
In order to use **ntfsfix** , you must unmount the NTFS volume. After running **ntfsfix** , you can safely reboot into Windows NT or Windows 2000. Please note that **ntfsfix** is not an **fsck** -like tool. **ntfsfix** is not guaranteed to fix all the alterations provoked by the NTFS driver.
The following option is available for running **ntfsfix** on an NTFS file system:

force

Force **ntfsfix** to write changes even if it detects that the file system is dirty. The default is false.
* * *
#  K.3. Cloning NTFS file systems
The NTFS FSIM can run the **ntfsclone** utility to copy an NTFS file system from one volume to another. **ntfsclone** is faster than **dd** because it only copies the files and the file system data instead of the entire contents of the volume.
The following options are available for running **ntfsclone** on an NTFS file system:

target

The volume onto which the file system should be cloned.

force

Force **ntfsclone** to copy the file system even if it detects that the volume is dirty. The default is false.
* * *
#  K.4. Removing NTFS file systems
An NTFS file system can be removed from its volume if the file system is unmounted. This operation involves erasing the superblock from the volume so the file system will not be recognized in the future. There are no options available for removing file systems.
* * *
#  K.5. Expanding and shrinking NTFS file systems
An NTFS file system is automatically expanded or shrunk when its volume is expanded for shrunk. However, NTFS only allows these operations if the volume is unmounted.
