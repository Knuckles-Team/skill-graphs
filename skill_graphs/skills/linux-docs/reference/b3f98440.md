
 2. Choose Replace on the popup menu.

 3. In the "Select Replace Target Object" panel, select sdc1.

 4. Activate Replace.


When you save changes, EVMS begins to copy the data from sdb1 to sdc1. The
status bar at the bottom of the UI will reflect the percent-complete of the
copy operation. The UI must remain open until the copy is finished. At that
time, the object sdb1 will be moved to the "Available Objects" panel.
-----------------------------------------------------------------------------

22.2.2. Using the CLI

Use the Replace to replace objects with the CLI:
Replace:source_object_name, target_object_name

 "source_object_name" is the name of the object you wish to replace with
"target_object_name." In the following example, sdb1 is replaced with sdc1.
Replace:sdb1,sdc1
-----------------------------------------------------------------------------

Chapter 23. Moving segment storage objects

This chapter discusses how and why to move segments.
-----------------------------------------------------------------------------

23.1. What is segment moving?

A segment move is when a data segment is relocated to another location on the
underlying storage object. The new location of the segment cannot overlap
with the current segment location.
-----------------------------------------------------------------------------

23.2. Why move a segment?

 Segments are moved for a variety of reasons. The most compelling among them
is to make better use of disk freespace. Disk freespace is an unused
contiguous extent of sectors on a disk that has been identified by EVMS as a
freespace segment. A data segment can only be expanded by adding sectors to
the end of the segment, moving the end of the data segment up into the
freespace that immediately follows the data segment. However, what if there
is no freespace following the data segment? A segment or segments could be be
moved around to put freespace after the segment that is to be expanded. For
example:

��*�The segment following the segment to be expanded can be moved elsewhere
    on the disk, thus freeing up space after the segment that is to be
    expanded.

��*�The segment to be expanded can be moved into freespace where there is
    more room for the segment to be expanded.

��*�The segment can be moved into freespace that precedes the segment so that
    after the move the data segment can be expanded into the freespace
    created by the move.


-----------------------------------------------------------------------------
23.3. Which segment manager plug-ins implement the move function?

The following segment manager plug-ins support the move function:

��*� DOS

��*� s390

��*� GPT


-----------------------------------------------------------------------------
23.4. Example: move a DOS segment

This section shows how to move a DOS segment:

Note Note
�    In the following example, the DOS segment manager has a single primary
     partition on disk sda that is located at the very end of the disk. We
     want to move it to the front of the drive because we want to expand the
     segment but there is currently no freespace following the segment.
-----------------------------------------------------------------------------

23.4.1. Using the EVMS GUI context sensitive menu

To move the DOS segment through the GUI context sensitive menu, follow these
steps:

 1. From the Segments tab, right click sda1.

 2. Click Move.

 3. Select sda_freespace1.

 4. Click Move.


-----------------------------------------------------------------------------
23.4.2. Using Ncurses

To move the DOS segment, follow these steps:

 1. Use Tab to select the Disk Segments view.

 2. Scroll down with the down arrow and select sda1.

 3. Press Enter.

 4. Scroll down with the down arrow and select Move by pressing Enter.

 5. Use the spacebar to select sda_freespace1.

 6. Use Tab to select Move and press Enter.


-----------------------------------------------------------------------------
23.4.3. Using the CLI

Use the task command to move a DOS segment with the CLI.
task:Move,sda1,sda_freespace1
-----------------------------------------------------------------------------

Appendix A. The DOS plug-in

The DOS plug-in is the most commonly used EVMS segment manager plug-in. The
DOS plug-in supports DOS disk partitioning as well as:

��*�OS/2 partitions that require extra metadata sectors.

��*�Embedded partition tables: SolarisX86, BSD, and UnixWare.


The DOS plug-in reads metadata and constructs segment storage objects that
provide mappings to disk partitions.
-----------------------------------------------------------------------------

A.1. How the DOS plug-in is implemented

The DOS plug-in provides compatibility with DOS partition tables. The plug-in
produces EVMS segment storage objects that map primary partitions described
by the MBR partition table and logical partitions described by EBR partition
tables.

DOS partitions have names that are constructed from two pieces of
information:

��*�The device they are found on.

��*�The partition table entry that provided the information.


Take, for example, partition name hda1, which describes a partition that is
found on device had in the MBR partition table. DOS partition tables can hold
four entries. Partition numbers 1-4 refer to MBR partition records.
Therefore, our example is telling us that partition hda1 is described by the
very first partition record entry in the MBR partition table. Logical
partitions, however, are different than primary partitions. EBR partition
tables are scattered across a disk but are linked together in a chain that is
first located using an extended partition record found in the MBR partition
table. Each EBR partition table contains a partition record that describes a
logical partition on the disk. The name of the logical partition reflects its
position in the EBR chain. Because the MBR partition table reserves numerical
names 1-4, the very first logical partition is always named 5. The next
logical partition, found by following the EBR chain, is called 6, and so
forth. So, the partition hda5 is a logical partition that is described by a
partition record in the very first EBR partition table.

While discovering DOS partitions, the DOS plug-in also looks for OS/2 DLAT
metadata to further determine if the disk is an OS/2 disk. An OS/2 disk has
additional metadata and the metadata is validated during recovery. This
information is important for the DOS plug-in to know because an OS/2 disk
must maintain additional partition information. (This is why the DOS plug-in
asks, when being assigned to a disk, if the disk is a Linux disk or an OS/2
disk.) The DOS plug-in needs to know how much information must be kept on the
disk and what kind of questions it should ask the user when obtaining the
information.

 An OS/2 disk can contain compatibility volumes as well as logical volumes. A
compatibility volume is a single partition with an assigned drive letter that
can be mounted. An OS/2 logical volume is a drive link of 1 or more
partitions that have software bad-block relocation at the partition level.

 Embedded partitions, like those found on a SolarisX86 disk or a BSD
compatibility disk, are found within a primary partition. Therefore, the DOS
plug-in inspects primary partitions that it has just discovered to further
determine if any embedded partitions exist. Primary partitions that hold
embedded partition tables have partition type fields that indicate this. For
example, a primary partition of type 0xA9 probably has a BSD partition table
that subdivides the primary partition into BSD partitions. The DOS plug-in
looks for a BSD disk label and BSD data partitions in the primary partition.
If the DOS plug-in finds a BSD disk label, it exports the BSD partitions.
Because this primary partition is actually just a container that holds the
BSD partitions, and not a data partition itself, it is not exported by the
DOS plug-in. Embedded partitions are named after the primary partition they
were discovered within. As an example, hda3.1 is the name of the first
embedded partition found within primary partition hda3.
-----------------------------------------------------------------------------

A.2. Assigning the DOS plug-in

 Assigning a segment manager to a disk means that you want the plug-in to
manage partitions on the disk. In order to assign a segment manager to a
disk, the plug-in needs to create and maintain the appropriate metadata,
which is accomplished through the "disk type" option. When you specify the
"disk type" option and choose Linux or OS/2, the plug-in knows what sort of
metadata it needs to keep and what sort of questions it should ask when
creating partitions.

 An additional OS/2 option is the "disk name" option, by which you can
provide a name for the disk that will be saved in OS/2 metadata and that will
be persistent across reboots.
-----------------------------------------------------------------------------

A.3. Creating DOS partitions

 There are two basic DOS partition types:

 1. A primary partition, which is described by a partition record in the MBR
    partition table.

 2. A logical partition, which is described by a partition record in the EBR
    partition table.


Every partition table has room for four partition records; however, there are
a few rules that impose limits on this.

 An MBR partition table can hold four primary partition records unless you
also have logical partitions. In this case, one partition record is used to
describe an extended partition and the start of the EBR chain that in turn
describes logical partitions.

 Because all logical partitions must reside in the extended partition, you
cannot allocate room for a primary partition within the extended partition
and you cannot allocate room for a logical partition outside or adjacent to
this area.

 Lastly, an EBR partition table performs two functions:

 1. It describes a logical partition and therefore uses a partition record
    for this purpose.

 2. It uses a partition record to locate the next EBR partition table.


 EBR partition tables use at most two entries.

 When creating a DOS partition, the options you are presented with depend on
the kind of disk you are working with. However, both OS/2 disks and Linux
disks require that you choose a freespace segment on the disk within which to
create the new data segment. The create options are:

size
    The size of the partition you are creating. Any adjustments that are
    needed for alignment are performed by the DOS plug-in and the resulting
    size might differ slightly from the value you enter.

offset
    Lets you skip sectors and start the new partition within the freespace
    area by specifying a sector offset.

type
    Lets you enter a partition type or choose from a list of partition types;
    for example, native Linux.

primary
    Lets you choose between creating a primary or logical partition. Due to
    the rules outlined above, you might or might not have a choice. The DOS
    plug-in can determine if a primary or logical partition can be created in
    the freespace area you chose and disable this choice.

bootable
    Lets you enable the sys_ind flag field in a primary partition and disable
    it when creating a logical partition. The sys_ind flag field identifies
    the active primary partition for booting.


 Additional OS/2 options are the following:

partition name
     An OS/2 partition can have a name, like Fred or Part1.

volume name
     OS/2 partitions belong to volumes, either compatibility or logical, and
    volumes have names. However, because the DOS plug-in is not a logical
    volume manager, it cannot actually create OS/2 logical volumes.

drive letter
    You can specify the drive letter for an OS/2 partition, but it is not a
    required field. Valid drive letters are: C,D...Z.


-----------------------------------------------------------------------------
A.4. Expanding DOS partitions

 A partition is a physically contiguous run of sectors on a disk. You can
expand a partition by adding unallocated sectors to the initial run of
sectors on the disk. Because the partition must remain physically contiguous,
a partition can only be expanded by growing into an unused area on the disk.
These unused areas are exposed by the DOS plug-in as freespace segments.
Therefore, a data segment is only expandable if a freespace segment
immediately follows it. Lastly, because a DOS partition must end on a
cylinder boundary, DOS segments are expanded in cylinder size increments.
This means that if the DOS segment you want to expand is followed by a
freespace segment, you might be unable to expand the DOS segment if the
freespace segment is less than a cylinder in size.

 There is one expand option, as follows:

size
     This is the amount by which you want to expand the data segment. The
    amount must be a multiple of the disk's cylinder size.


-----------------------------------------------------------------------------
A.5. Shrinking DOS partitions

 A partition is shrunk when sectors are removed from the end of the
partition. Because a partition must end on a cylinder boundary, a partition
is shrunk by removing cylinder amounts from the end of the segment.

 There is one shrink option, as follows:

size
    The amount by which you want to reduce the size of the segment. Because a
    segment ends on a cylinder boundary, this value must be some multiple of
    the disk's cylinder size.


-----------------------------------------------------------------------------
A.6. Deleting partitions

You can delete an existing DOS data segment as long as it is not currently a
compatibility volume, an EVMS volume, or consumed by another EVMS plug-in. No
options are available for deleting partitions.
-----------------------------------------------------------------------------

Appendix B. The MD region manager

 The Multi-Disk (MD) driver in the Linux kernel and the MD plug-in in EVMS
provide a software implementation of RAID (Redundant Array of Inexpensive
Disks). The basic idea of software RAID is to combine multiple hard disks
into an array of disks in order to improve capacity, performance, and
reliability.

 The RAID standard defines a wide variety of methods for combining disks into
a RAID array. In Linux, MD implements a subset of the full RAID standard,
including RAID-0, RAID-1, RAID-4, and RAID-5. In addition, MD also supports
additional combinations called Linear-RAID and Multipath.

 In addition to this appendix, more information about RAID and the Linux MD
driver can be found in the Software RAID HOWTO at [http://www.tldp.org/HOWTO/
Software-RAID-HOWTO.html] www.tldp.org/HOWTO/Software-RAID-HOWTO.html.
-----------------------------------------------------------------------------

B.1. Characteristics of Linux RAID levels

 All RAID levels are used to combine multiple devices into a single MD array.
The MD plug-in is a region-manager, so EVMS refers to MD arrays as "regions."
MD can create these regions using disks, segments or other regions. This
means that it's possible to create RAID regions using other RAID regions, and
thus combine multiple RAID levels within a single volume stack.

 The following subsections describe the characteristics of each Linux RAID
level. Within EVMS, these levels can be thought of as sub-modules of the MD
plug-in.
-----------------------------------------------------------------------------

B.1.1. Linear mode

 Linear-RAID regions combine objects by appending them to each other. Writing
(or reading) linearly to the MD region starts by writing to the first child
object. When that object is full, writes continue on the second child object,
and so on until the final child object is full. Child objects of a
Linear-RAID region do not have to be the same size.

 Advantage:

��*� Linear-RAID provides a simple method for building very large regions
    using several small objects.


 Disadvantages:

��*� Linear-RAID is not "true" RAID, in the sense that there is no data
    redundancy. If one disk crashes, the RAID region will be unavailable, and
    will result in a loss of some or all data on that region.

��*� Linear-RAID provides little or no performance benefit. The objects are
    combined in a simple, linear fashion that doesn't allow for much (if any)
    I/O in parallel to multiple child objects. The performance of a
    Linear-RAID will generally be equivalent to the performance of a single
    disk.


-----------------------------------------------------------------------------
B.1.2. RAID-0

 RAID-0 is usually referred to as "striping." This means that data in a
RAID-0 region is evenly distributed and interleaved on all the child objects.
For example, when writing 16 KB of data to a RAID-0 region with three child
objects and a chunk-size of 4 KB, the data would be written as follows:

��*� 4 KB to object 0

��*� 4 KB to object 1

��*� 4 KB to object 2

��*� 4 KB to object 0


 Advantages:

��*� Like Linear-RAID, RAID-0 provides a simple method for building very
    large regions using several small objects.

��*� In general, RAID-0 provides I/O performance improvements, because it can
    break large I/O requests up and submit them in parallel across several
    disks.


 Disadvantage:

��*� Also like Linear-RAID, RAID-0 is not "true" RAID, in the sense that
    there is no data redundancy (hence the name RAID "zero"). If one disk
    crashes, the RAID region will be unavailable, and will likely result in a
    loss of all data on that region.


-----------------------------------------------------------------------------
B.1.3. RAID-1

 RAID-1 is usually referred to as "mirroring." Each child object in a RAID-1
region contains an identical copy of the data in the region. A write to a
RAID-1 region results in that data being written simultaneously to all child
objects. A read from a RAID-1 region can result in reading the data from any
one of the child objects. Child objects of a RAID-1 region do not have to be
the same size, but the size of the region will be equal to the size of the
smallest child object.

 Advantages:

��*� RAID-1 provides complete data redundancy. In a RAID-1 region made from N
    child objects, up to N-1 of those objects can crash and the region will
    still be operational, and can retrieve data from the remaining objects.

��*� RAID-1 can provide improved performance on I/O-reads. Because all child
    objects contain a full copy of the data, multiple read requests can be
    load-balanced among all the objects.


Disadvantages:

��*� RAID-1 can cause a decrease in performance on I/O-writes. Because each
    child object must have a full copy of the data, each write to the region
    must be duplicated and sent to each object. A write request cannot be
    completed until all duplicated writes to the child objects are complete.

��*� A RAID-1 region with N disks costs N times as much as a single disk, but
    only provides the storage space of a single disk.


-----------------------------------------------------------------------------
B.1.4. RAID-4/5

 RAID-4/5 is often referred to as "striping with parity." Like RAID-0, the
data in a RAID-4/5 region is striped, or interleaved, across all the child
objects. However, in RAID-4/5, parity information is also calculated and
recorded for each stripe of data in order to provide redundancy in case one
of the objects is lost. In the event of a disk crash, the data from that disk
can be recovered based on the data on the remaining disks and the parity
information.

 In RAID-4 regions, a single child object is used to store the parity
information for each data stripe. However, this can cause an I/O bottleneck
on this one object, because the parity information must be updated for each I
/O-write to the region.

 In RAID-5 regions, the parity is spread evenly across all the child objects
in the region, thus eliminating the parity bottleneck in RAID-4. RAID-5
provides four different algorithms for how the parity is distributed. In
fact, RAID-4 is often thought of as a special case of RAID-5 with a parity
algorithm that simply uses one object instead of all objects. This is the
viewpoint that Linux and EVMS use. Therefore, the RAID-4/5 level is often
just referred to as RAID-5, with RAID-4 simply being one of the five
available parity algorithms.

Advantages and disadvantages

��*� Like RAID-1, RAID-4/5 provides redundancy in the event of a hardware
    failure. However, unlike RAID-1, RAID-4/5 can only survive the loss of a
    single object. This is because only one object's worth of parity is
    recorded. If more than one object is lost, there isn't enough parity
    information to recover the lost data.

��*� RAID-4/5 provides redundancy more cost effectively than RAID-1. A RAID-4
    /5 region with N disks provides N-1 times the storage space of a single
    disk. The redundancy comes at the cost of only a single disk in the
    region.

��*� Like RAID-0, RAID-4/5 can generally provide an I/O performance
    improvement, because large I/O requests can be broken up and submitted in
    parallel to the multiple child objects. However, on I/O-writes the
    performance improvement will be less than that of RAID-0, because the
    parity information must be calculated and rewritten each time a write
    request is serviced. In addition, in order to provide any performance
    improvement on I/O-writes, an in-memory cache must be maintained for
    recently accessed stripes so the parity information can be quickly
    recalculated. If a write request is received for a stripe of data that
    isn't in the cache, the data chunks for the stripe must first be read
    from disk in order to calculate the parity. If such cache-misses occur
    too often, the I/O-write performance could potentially be worse than even
    a Linear-RAID region.


-----------------------------------------------------------------------------
B.1.5. Multipath

 A multipath region consists of one or more objects, just like the other RAID
levels. However, in multipath, the child objects actually represent multiple
physical paths to the same physical disk. Such setups are often found on
systems with fiber-attached storage devices or SANs.

 Multipath is not actually part of the RAID standard, but was added to the
Linux MD driver because it provides a convenient place to create "virtual"
devices that consist of multiple underlying devices.

 The previous RAID levels can all be created using a wide variety of storage
devices, including generic, locally attached disks (for example, IDE and
SCSI). However, Multipath can only be used if the hardware actually contains
multiple physical paths to the storage device, and such hardware is usually
available on high-end systems with fiber-or network-attached storage.
Therefore, if you don't know whether you should be using the Multipath
module, chances are you don't need to use it.

 Like RAID-1 and RAID-4/5, Multipath provides redundancy against hardware
failures. However, unlike these other RAID levels, Multipath protects against
failures in the paths to the device, and not failures in the device itself.
If one of the paths is lost (for example, a network adapter breaks or a
fiber-optic cable is removed), I/O will be redirected to the remaining paths.

 Like RAID-0 and RAID-4/5, Multipath can provide I/O performance improvements
by load balancing I/O requests across the various paths.
-----------------------------------------------------------------------------

B.2. Creating an MD region

 The procedure for creating a new MD region is very similar for all the
different RAID levels. When using the EVMS GUI or Ncurses, first choose the
ActionsCreate Region menu item. A list of region-managers will open, and each
RAID level will appear as a separate plug-in in this list. Select the plug-in
representing the desired RAID level. The next panel will list the objects
available for creating a new RAID region. Select the desired objects to build
the new region. If the selected RAID level does not support any additional
options, then there are no more steps, and the region will be created. If the
selected RAID level has extra creation options, the next panel will list
those options. After selecting the options, the region will be created.

 When using the CLI, use the following command to create a new region:
create:region,<plugin>={<option_name>=<value>[,<option_name>=<value>]*},
   <object_name>[,<object_name>]*

 For <plugin>, the available plug-in names are "MDLinearRegMgr,"
"MDRaid0RegMgr," "MDRaid1RegMgr," "MDRaid5RegMgr," and "MD Multipath." The
available options are listed in the following sections. If no options are
available or desired, simply leave the space blank between the curly braces.

 The Linear-RAID and Multipath levels provide no extra options for creation.
The remaining RAID levels provide the options listed below.
-----------------------------------------------------------------------------
