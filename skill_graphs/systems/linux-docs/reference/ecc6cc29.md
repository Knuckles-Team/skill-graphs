particular logging level, the Engine collects messages for that level and all
the levels below it.

The following table lists the allowable log levels and the information they
provide:

Table 3-1. EVMS logging levels
+------------------------------------+-------------------------------------+
|Level name                          |Description                          |
+------------------------------------+-------------------------------------+
|Critical                            |The health of the system or the      |
|                                    |Engine is in jeopardy; for example,  |
|                                    |an operation has failed because there|
|                                    |is not enough memory.                |
+------------------------------------+-------------------------------------+
|Serious                             |An operation did not succeed.        |
+------------------------------------+-------------------------------------+
|Error                               |The user has caused an error. The    |
|                                    |error messages are provided to help  |
|                                    |the user correct the problem.        |
+------------------------------------+-------------------------------------+
|Warning                             |An error has occurred that the system|
|                                    |might or might not be able to work   |
|                                    |around.                              |
+------------------------------------+-------------------------------------+
|Default                             |An error has occurred that the system|
|                                    |has already worked around.           |
+------------------------------------+-------------------------------------+
|Details                             |Detailed information about the       |
|                                    |system.                              |
+------------------------------------+-------------------------------------+
|Entry_Exit                          |Traces the entries and exits of      |
|                                    |functions.                           |
+------------------------------------+-------------------------------------+
|Debug                               |Information that helps the user debug|
|                                    |a problem.                           |
+------------------------------------+-------------------------------------+
|Extra                               |More information that helps the user |
|                                    |debug a problem than the "Debug"     |
|                                    |level provides.                      |
+------------------------------------+-------------------------------------+
|Everything                          |Verbose output.                      |
+------------------------------------+-------------------------------------+
-----------------------------------------------------------------------------

3.3. Specifying the logging levels

By default, when any of the EVMS interfaces is opened, the Engine logs the
Default level of messages into the /var/log/evmsEngine.log file. However, if
your system is having problems and you want to see more of what is happening,
you can change the logging level to be higher; if you want fewer logging
messages, you can change the logging level to be lower. To change the logging
level, specify the -d parameter and the log level on the interface open call.
The following examples show how to open the various interfaces with the
highest logging level (everything):
GUI:            evmsgui -d everything
Ncurses:        evmsn -d everything
CLI:            evms -d everything

Note NOTE
�    If you use the EVMS mailing list for help with a problem, providing to
     us the log file that is created when you open one of the interfaces (as
     shown in the previous commands) makes it easier for us to help you.

The EVMS GUI lets you change the logging level during an Engine session. To
do so, follow these steps:

 1. Select Settings->Log Level->Engine.

 2. Click the Level you want.


The CLI command, probe, opens and closes the Engine, which causes a new log
to start. The log that existed before the probe command was issued is renamed
/var/log/evmsEngine.1.log and the new log is named /var/log/evmsEngine.log.

 If you will be frequently using a different log level than the default, you
can specify the default logging level in /etc/evms.conf rather than having to
use the -d option when starting the user interface. The "debug_level" option
in the "engine" section sets the default logging level for when the Engine is
opened. Using the -d option during the command invocation overrides the
setting in /etc/evms.conf.
-----------------------------------------------------------------------------

Chapter 4. Viewing compatibility volumes after migrating

Migrating to EVMS allows you to have the flexibility of EVMS without losing
the integrity of your existing data. EVMS discovers existing volume
management volumes as compatibility volumes. After you have installed EVMS,
you can view your existing volumes with the interface of your choice.
-----------------------------------------------------------------------------

4.1. Using the EVMS GUI

If you are using the EVMS GUI as your preferred interface, you can view your
migrated volumes by typing evmsgui at the command prompt. The following
window opens, listing your migrated volumes.


Figure 4-1. GUI start-up window

[gui_active]
-----------------------------------------------------------------------------

4.2. Using Ncurses

If you are using the Ncurses interface, you can view your migrated volumes by
typing evmsn at the command prompt. The following window opens, listing your
migrated volumes.


Figure 4-2. Ncurses start-up window

[ncurses_active]
-----------------------------------------------------------------------------

4.3. Using the CLI

If you are using the Command Line Interpreter (CLI) interface, you can view
your migrated volumes by following these steps:

 1. Start the Command Line Interpreter by typing evms at the command line.

 2. Query the volumes by typing the following at the EVMS prompt:
    query:volumes

    Your migrated volumes are displayed as results of the query.


Figure 4-3. CLI volume query results

[cli_active]
-----------------------------------------------------------------------------

Chapter 5. Obtaining interface display details

The EVMS interfaces let you view more detailed information about an EVMS
object than what is readily available from the main views of the EVMS user
interfaces. The type and extent of additional information available is
dependent on the interface you use. For example, the EVMS GUI provides more
in-depth information than does the CLI.

The following sections show how to find detailed information on the region
lvm/Sample Container/Sample Region, which is part of volume /dev/evms/Sample
Volume (created in section 10.2).
-----------------------------------------------------------------------------

5.1. Using the EVMS GUI

With the EVMS GUI, it is only possible to display additional details on an
object through the Context Sensitive Menus, as shown in the following steps:

 1. Looking at the volumes view, click the "+" next to volume /dev/evms/
    Sample Volume. Alternatively, look at the regions view.

 2. Right click lvm/Sample Container/Sample Region.

 3. Point at Display Details... and click. A new window opens with additional
    information about the selected region.

 4. Click More by the Logical Extents box. Another window opens that displays
    the mappings of logical extents to physical extents.


-----------------------------------------------------------------------------
5.2. Using Ncurses

Follow these steps to display additional details on an object with Ncurses:

 1. Press Tab to reach the Storage Regions view.

 2. Scroll down using the down arrow until lvm/Sample Container/Sample Region
    is highlighted.

 3. Press Enter.

 4. In the context menu, scroll down using the down arrow to highlight
    "Display Details..."

 5. Press Enter to activate the menu item.

 6. In the Detailed Information dialog, use the down arrow to highlight the
    "Logical Extents" item and then use spacebar to open another window that
    displays the mappings of logical extents to physical extents.


-----------------------------------------------------------------------------
5.3. Using the CLI

Use the query command (abbreviated q) with filters to display details about
EVMS objects. There are two filters that are especially helpful for
navigating within the command line: list options (abbreviated lo) and
extended info (abbreviated ei).

The list options command tells you what can currently be done and what
options you can specify. To use this command, first build a traditional query
command starting with the command name query, followed by a colon (:), and
then the type of object you want to query (for example, volumes, objects,
plug-ins). Then, you can use filters to narrow the search to only the area
you are interested in. For example, to determine the acceptable actions at
the current time on lvm/Sample Container/Sample Region, enter the following
command:
query: regions, region="lvm/Sample Container/Sample Region", list options

The extended info filter is the equivalent of Display Details in the EVMS GUI
and Ncurses interfaces. The command takes the following form: query, followed
by a colon (:), the filter (extended info), a comma (,), and the object you
want more information about. The command returns a list containing the field
names, titles, descriptions and values for each field defined for the object.
For example, to obtain details on lvm/Sample Container/Sample Region, enter
the following command:
query: extended info, "lvm/Sample Container/Sample Region"

Many of the field names that are returned by the extended info filter can be
expanded further by specifying the field name or names at the end of the
command, separated by commas. For example, if you wanted additional
information about logical extents, the query would look like the following:
query: extended info, "lvm/Sample Container/Sample Region", Extents
-----------------------------------------------------------------------------

Chapter 6. Adding and removing a segment manager

This chapter discusses when to use a segment manager, what the different
types of segment managers are, how to add a segment manager to a disk, and
how to remove a segment manager.
-----------------------------------------------------------------------------

6.1. When to add a segment manager

Adding a segment manager to a disk allows the disk to be subdivided into
smaller storage objects called disk segments. The add command causes a
segment manager to create appropriate metadata and expose freespace that the
segment manager finds on the disk. You need to add segment managers when you
have a new disk or when you are switching from one partitioning scheme to
another.

EVMS displays disk segments as the following types:

��*�Data: a set of contiguous sectors that has been allocated from a disk and
    can be used to construct a volume or object.

��*�Freespace: a set of contiguous sectors that are unallocated or not in
    use. Freespace can be used to create a segment.

��*�Metadata: a set of contiguous sectors that contain information needed by
    the segment manager.


-----------------------------------------------------------------------------
6.2. Types of segment managers

There are seven types of segment managers in EVMS: DOS, GPT, S/390, Cluster,
BSD, MAC, and BBR.
-----------------------------------------------------------------------------

6.2.1. DOS Segment Manager

The most commonly used segment manager is the DOS Segment Manager. This
plug-in provides support for traditional DOS disk partitioning. The DOS
Segment Manager also recognizes and supports the following variations of the
DOS partitioning scheme:

��*�OS/2: an OS/2 disk has additional metadata sectors that contain
    information needed to reconstruct disk segments.

��*�Embedded partitions: support for BSD, SolarisX86, and UnixWare is
    sometimes found embedded in primary DOS partitions. The DOS Segment
    Manager recognizes and supports these slices as disk segments.


-----------------------------------------------------------------------------
6.2.2. GUID Partitioning Table (GPT) Segment Manager

The GUID Partitioning Table (GPT) Segment Manager handles the new GPT
partitioning scheme on IA-64 machines. The Intel Extensible Firmware
Interface Specification requires that firmware be able to discover partitions
and produce logical devices that correspond to disk partitions. The
partitioning scheme described in the specification is called GPT due to the
extensive use of Globally Unique Identifier (GUID) tagging. GUID is a 128 bit
long identifier, also referred to as a Universally Unique Identifier (UUID).
As described in the Intel Wired For Management Baseline Specification, a GUID
is a combination of time and space fields that produce an identifier that is
unique across an entire UUID space. These identifiers are used extensively on
GPT partitioned disks for tagging entire disks and individual partitions. GPT
partitioned disks serve several functions, such as:

��*�keeping a primary and backup copy of metadata

��*�replacing msdos partition nesting by allowing many partitions

��*�using 64 bit logical block addressing

��*�tagging partitions and disks with GUID descriptors


The GPT Segment Manager scales better to large disks. It provides more
redundancy with added reliability and uses unique names. However, the GPT
Segment Manager is not compatible with DOS, OS/2, or Windows�.
-----------------------------------------------------------------------------

6.2.3. S/390 Segment Manager

The S/390 Segment Manager is used exclusively on System/390 mainframes. The S
/390 Segment Manager has the ability to recognize various disk layouts found
on an S/390 machine, and provide disk segment support for this architecture.
The two most common disk layouts are Linux Disk Layout (LDL) and Common Disk
Layout (CDL).

The principle difference between LDL and CDL is that an LDL disk cannot be
further subdivided. An LDL disk will produce a single metadata disk segment
and a single data disk segment. There is no freespace on an LDL disk, and you
cannot delete or re-size the data segment. A CDL disk can be subdivided into
multiple data disk segments because it contains metadata that is missing from
an LDL disk, specifically the Volume Table of Contents (vtoc) information.

The S/390 Segment Manager is the only segment manager plug-in capable of
understanding the unique S/390 disk layouts. The S/390 Segment Manager cannot
be added or removed from a disk.
-----------------------------------------------------------------------------

6.2.4. Cluster segment manager

The cluster segment manager (CSM) supports high availability clusters. When
the CSM is added to a shared storage disk, it writes metadata on the disk
that:

��*�provides a unique disk ID (guid)

��*�names the EVMS container the disk will reside within

��*�specifies the cluster node (nodeid) that owns the disk

��*�specifies the cluster (clusterid)


This metadata allows the CSM to build containers for supporting failover
situations. It does so by constructing an EVMS container object that consumes
all shared disks discovered by the CSM and belonging to the same container.
These shared storage disks are consumed by the container and a single data
segment is produced by the container for each consumed disk. A failover of
the EVMS resource is accomplished by simply reassigning the CSM container to
the standby cluster node and having that node re-run its discovery process.

Adding disks to CSM containers implies that only disk storage objects are
acceptable to the CSM. This is an important aspect of the CSM. Other segment
managers can be embedded within storage objects and used to further subdivide
them. However, the CSM cannot add any other kind of storage object to a CSM
container because the container is meant to be a disk group and the entire
disk group is reassigned during a failover. So, the CSM only accepts disks
when constructing containers. This is important to remember when adding the
CSM to a disk. If you choose Add and the CSM does not appear in the list of
selectable plug-ins when you know you have a disk, you should look at the
Volume list and see if the disk has already been listed as a compatibility
volume. If you simply delete the volume, the disk will become an available
object and the CSM will then appear in the list of plug-ins because it now
has an available disk that it can add to a container.
-----------------------------------------------------------------------------

6.2.5. BSD segment manager

BSD refers to the Berkeley Software Distribution UNIX� operating system. The
EVMS BSD segment manager is responsible for recognizing and producing EVMS
segment storage objects that map BSD partitions. A BSD disk may have a slice
table in the very first sector on the disk for compatibility purposes with
other operating systems. For example, a DOS slice table might be found in the
usual MBR sector. The BSD disk would then be found within a disk slice that
is located using the compatibility slice table. However, BSD has no need for
the slice table and can fully dedicate the disk to itself by placing the disk
label in the very first sector. This is called a "fully dedicated disk"
because BSD uses the entire disk and does not provide a compatibility slice
table. The BSD segment manager recognizes such "fully dedicated disks" and
provides mappings for the BSD partitions.
-----------------------------------------------------------------------------

6.2.6. MAC segment manager

Apple-partitioned disks use a disk label that is recognized by the MAC
segment manager. The MAC segment manager recognizes the disk label during
discovery and creates EVMS segments to map the MacOS disk partitions.
-----------------------------------------------------------------------------

6.2.7. BBR segment manager

The bad block replacement (BBR) segment manager enhances the reliability of a
disk by remapping bad storage blocks. When BBR is added to a disk, it writes
metadata on the disk that:

��*�reserves replacement blocks

��*�maps bad blocks to reserved blocks


Bad blocks occur when an I/O error is detected for a write operation. When
this happens, I/O normally fails and the failure code is returned to the
calling program code. BBR detects failed write operations and remaps the I/O
to a reserved block on the disk. Afterward, BBR restarts the I/O using the
reserve block.

Every block of storage has an address, called a logical block address, or
LBA. When BBR is added to a disk, it provides two critical functions: remap
and recovery. When an I/O operation is sent to disk, BBR inspects the LBA in
the I/O command to see if the LBA has been remapped to a reserve block due to
some earlier I/O error. If BBR finds a mapping between the LBA and a reserve
block, it updates the I/O command with the LBA of the reserve block before
sending it on to the disk. Recovery occurs when BBR detects an I/O error and
remaps the bad block to a reserve block. The new LBA mapping is saved in BBR
metadata so that subsequent I/O to the LBA can be remapped.
-----------------------------------------------------------------------------

6.3. Adding a segment manager to an existing disk

When you add a segment manager to a disk, the segment manager needs to change
the basic layout of the disk. This change means that some sectors are
reserved for metadata and the remaining sectors are made available for
creating data disk segments. Metadata sectors are written to disk to save
information needed by the segment manager; previous information found on the
disk is lost. Before adding a segment manager to an existing disk, you must
remove any existing volume management structures, including any previous
segment manager.
-----------------------------------------------------------------------------

6.4. Adding a segment manager to a new disk

When a new disk is added to a system, the disk usually contains no data and
has not been partitioned. If this is the case, the disk shows up in EVMS as a
compatibility volume because EVMS cannot tell if the disk is being used as a
volume. To add a segment manager to the disk so that it can be subdivided
into smaller disk segment objects, tell EVMS that the disk is not a
compatibility volume by deleting the volume information.

If the new disk was moved from another system, chances are good that the disk
already contains metadata. If the disk does contain metadata, the disk shows
up in EVMS with storage objects that were produced from the existing
metadata. Deleting these objects will allow you to add a different segment
manager to the disk, and you lose any old data.
-----------------------------------------------------------------------------

6.5. Example: add a segment manager

This section shows how to add a segment manager with EVMS.

EVMS initially displays the physical disks it sees as volumes. Assume that
you have added a new disk to the system that EVMS sees as sde. This disk
contains no data and has not been subdivided (no partitions). EVMS assumes
that this disk is a compatibility volume known as /dev/evms/sde.



    Example 6-1. Add the DOS Segment Manager

    Add the DOS Segment Manager to disk sde.

Note NOTE
�    In the following example, the DOS Segment Manager creates two segments
     on the disk: a metadata segment known as sde_mbr, and a segment to
     represent the available space on the drive, sde_freespace1. This
     freespace segment (sde_freespace1) can be divided into other segments
     because it represents space on the drive that is not in use.
-----------------------------------------------------------------------------

6.5.1. Using the EVMS GUI

To add the DOS Segment Manager to sde, first remove the volume, /dev/evms/
sde:

 1. Select Actions->Delete->Volume.

 2. Select /dev/evms/sde.

 3. Click Delete.


Alternatively, you can remove the volume through the GUI context sensitive
menu:

 1. From the Volumes tab, right click /dev/evms/sde.

 2. Click Delete.


After the volume is removed, add the DOS Segment Manager:

 1. Select Actions->Add->Segment Manager to Storage Object.

 2. Select DOS Segment Manager.

 3. Click Next.

 4. Select sde

 5. Click Add


-----------------------------------------------------------------------------
6.5.2. Using Ncurses

To add the DOS Segment Manager to sde, first remove the volume /dev/evms/sde:

 1. Select Actions->Delete->Segment Manager to Storage Object.

 2. Select /dev/evms/sde.

 3. Activate Delete.


Alternatively, you can remove the volume through the context sensitive menu:

 1. From the Logical Volumes view, press Enter on /dev/evms/sde.

 2. Activate Delete.


After the volume is removed, add the DOS Segment Manager:

 1. Select Actions->Add->Segment Manager to Storage Object

 2. Select DOS Segment Manager.

 3. Activate Next.

 4. Select sde.

 5. Activate Add.


-----------------------------------------------------------------------------
6.5.3. Using the CLI

To add the DOS Segment Manager to sde, first tell EVMS that this disk is not
a volume and is available for use:
Delete:/dev/evms/sde

Next, add the DOS Segment Manager to sde by typing the following:
Add:DosSegMgr={},sde
-----------------------------------------------------------------------------

6.6. Removing a segment manager

When a segment manager is removed from a disk, the disk can be reused by
other plug-ins. The remove command causes the segment manager to remove its
partition or slice table from the disk, leaving the raw disk storage object
that then becomes an available EVMS storage object. As an available storage
object, the disk is free to be used by any plug-in when storage objects are
created or expanded. You can also add any of the segment managers to the
available disk storage object to subdivide the disk into segments.

Most segment manager plug-ins check to determine if any of the segments are
still in use by other plug-ins or are still part of volumes. If a segment
manager determines that there are no disks from which it can safely remove
itself, it will not be listed when you use the remove command. In this case,
you should delete the volume or storage object that is consuming segments
from the disk you want to reuse.
-----------------------------------------------------------------------------

6.7. Example: remove a segment manager
