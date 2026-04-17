    amount of I/O throughput across multiple objects. This option specifies
    how many objects the new region should be striped across. By default, new
    regions are not striped, and this value is set to 1.

stripe_size
    The granularity of striping. The default value is 16 KB. Use this option
    only if the stripes option is greater than 1.

contiguous
    This option specifies that the new region must be allocated on a single
    object, and that the extents on that object must be physically
    contiguous. By default, this is set to false, which allows regions to
    span objects. This option cannot be used if the stripes option is greater
    than 1.

pv_names
    A list of names of the objects the new region should map to. By default,
    this list is empty, which means all available objects will be used to
    allocate space to the new region.


-----------------------------------------------------------------------------
C.3.2. Expanding LVM regions

You can expand an existing LVM region if there are unused extents in the
container. If a region is striped, you can expand it only by using free space
on the objects it is striped across. If a region was created with the
contiguous option, you can only expand it if there is physically contiguous
space following the currently allocated space.

The following options are available for expanding LVM regions:

add_extents
    The number of extents to add to the region. If you specify this option,
    the appropriate value for the add_size option is automatically
    calculated. By default, the region will expand to use all free extents in
    the container.

add_size
    The amount of space to add to the region. If you specify this option, the
    appropriate value for the add_extents option is automatically calculated.
    By default, the region will expand to use all freespace in the container.

pv_names
    A list of names of the objects to allocate the additional space from. By
    default, this list is empty, which means all available objects will be
    used to allocate new space to the region.


-----------------------------------------------------------------------------
C.3.3. Shrinking LVM regions

You can shrink an existing LVM region by removing extents from the end of the
region. Regions must have at least one extent, so regions cannot be shrunk to
zero.

The following options are available when shrinking LVM regions. Because
regions are always shrunk by removing space from the end of the region, a
list of objects cannot be specified in this command.

remove_extents
    The number of extents to remove from the region. If you specify this
    option, the appropriate value for the remove_size option is automatically
    calculated. By default, one extent is removed from the region.

remove_size
    The amount of space to shrink the region by. If you specify this option,
    the appropriate value for the remove_extents option is automatically
    calculated.


-----------------------------------------------------------------------------
C.3.4. Deleting LVM regions

You can delete an existing LVM region as long as it is not currently a
compatibility volume, an EVMS volume, or consumed by another EVMS plug-in. No
options are available for deleting LVM regions.
-----------------------------------------------------------------------------

C.3.5. Moving LVM regions

The LVM plug-in lets you change the logical-to-physical mapping for an LVM
region and move the necessary data in the process. This capability is most
useful if a PV needs to be removed from a container. There are currently two
LVM plug-in functions for moving regions: move_pv and move_extent.
-----------------------------------------------------------------------------

C.3.5.1. move_pv

When a PV needs to be removed from a container, all PEs on that PV that are
allocated to regions must be moved to other PVs. The move_pv command lets you
move PEs to other PVs. move_pv is targeted at the LVM container and the
desired PV is used as the selected object. The following options are
available:

target_pvs
    By default, all remaining PVs in the container are used to find available
    extents to move the PEs. You can specify a subset of the PVs with this
    option.

maintain_stripes
    When the target PV contains striped regions, there are three choices for
    handling moving extents that belong to those regions:

    no
        Don't bother to maintain true striping. This choice allows extents to
        be moved to PVs that the region already uses for other stripes. This
        means that the performance will not be as optimal as it is with true
        striping, but allows the most flexibility in performing the move
        operation. This choice is the default for the maintain_stripes
        option.

    loose
        Ensure that moved extents do not end up on any PVs that the striped
        region already uses. However, this does not ensure that all moved
        extents end up on the same PV. For example, a region with three
        stripes may end up mapping to four or more PVs.

    strict
        Ensure that all moved extents end up on the same PV, thus ensuring
        true striping with the same number of PVs that the striped region
        originally used. This is the most restricted choice, and may prevent
        the move_pv operation from proceeding (depending on the particular
        configuration of the container).


    If the target PV has no striped regions, the maintain_stripes option is
    ignored.


-----------------------------------------------------------------------------
C.3.5.2. move_extent

In addition to moving all the extents from one PV, the LVM plug-in provides
the ability to move single extents. This allows a fine-grain tuning of the
allocation of extents. This command is targeted at the region owning the
extent to move. There are three required options for the move_extent command:

le
    The number of the logical extent to move. LE numbers start at 0.

pv
    The target object to move the extent to.

pe
    The target physical extent on the target object. PE numbers also start at
    0.


To determine the source LE and target PE, it is often helpful to view the
extended information about the region and container in question. The
following are command-line options that can be used to gather this
information:

To view the map of LEs in the region, enter this command:
query:ei,<region_name>,Extents

To view the list of PVs in the container, enter this command:
query:ei,<container_name>,Current_PVs

To view the current PE map for the desired target PV, enter this command:
query:ei,<container_name>,PEMapPV#

# is the number of the target PV in the container.

This information is also easily obtainable in the GUI and Text-Mode UIs by
using the "Display Details" item in the context-popup menus for the desired
region and container.
-----------------------------------------------------------------------------

C.3.6. Renaming LVM regions

You can rename an existing LVM region. In the EVMS GUI and text-mode UIs,
this is done using the modify properties command, which is available through
the "Actions" menu or the context-sensitive pop-up menus. In the EVMS CLI,
this is done using the set command.

If the renamed LVM region has a compatibility volume on it, then the name of
that compatibility volume will also change. In order for this to work
correctly, that volume must be unmounted before the name is changed. Also, be
sure to update your /etc/fstab file if the volume is listed, or the volume
won't be mounted properly the next time the system boots.

If the renamed LVM region has an EVMS volume or another storage object built
on it, then the region's name change will be transparent to the upper layers.
In this case, the rename can be done while the volume is mounted.
-----------------------------------------------------------------------------

Appendix D. The LVM2 plug-in

The LVM2 plug-in provides compatibility with the new volume format introduced
by the LVM2 tools from Red Hat (previously Sistina). This plug-in is very
similar in functionality to the LVM plug-in. The primary difference is the
new, improved metadata format. LVM2 is still based on the concept of volume
groups (VGs), which are constructed from physical volumes (PVs) and produce
logical volumes (LVs).

Just like the LVM plug-in, the LVM2 plug-in represents volume groups as EVMS
containers and represents logical volumes as EVMS regions. LVM2 containers
combine storage objects (disks, segments, or other regions) to create a pool
of freespace. Regions are then created from this freespace, with a variety of
mappings to the consumed objects.
-----------------------------------------------------------------------------

D.1. Container operations

D.1.1. Creating LVM2 containers

Containers are created with an initial set of objects. These objects can be
disks, segments, or regions. There are two options available when creating an
LVM2 container:

name
    The name of the new container.

extent_size
    The physical-extent (PE) size, which is the granularity with which
    regions can be created. The default is 32 MB. Unlike the LVM1 plug-in,
    there is no limitation to the number of extents that can be allocated to
    an LVM2 region.


-----------------------------------------------------------------------------
D.1.2. Adding objects to LVM2 containers

You can add objects to existing LVM containers in order to increase the pool
of storage that is available for creating regions. Because the name and
extent-size are set when the container is created, no options are available
when you add new objects to a container. Each object must be large enough to
hold at least one physical extent. If an object is not large enough to
satisfy this requirement, the LVM2 plug-in will not allow the object to be
added to the container.
-----------------------------------------------------------------------------

D.1.3. Removing objects from LVM2 containers

You can remove a consumed object from its container as long as no regions are
mapped to that object. The LVM2 plug-in does not allow objects that are in
use to be removed from their container. If an object must be removed, you can
delete or shrink regions, or move extents, in order to free the object from
use.

No options are available for removing objects from LVM containers.
-----------------------------------------------------------------------------

D.1.4. Expanding consumed objects in LVM2 containers

In addition to adding new objects to an LVM2 container, you can also expand
the space in a container by expanding one of the existing consumed objects
(PVs). For example, if a PV is a disk-segment with freespace immediately
following it on the disk, you can expand that segment, which will increase
the amount of freespace in the container. Likewise, if a PV is a RAID-0 or
RAID-5 region, you can expand that region by adding additional objects, which
in turn increases the freespace in the container.

When using the GUI or text-mode UIs, PV-expand is performed by expanding the
container. If any of the existing PVs are expandable, they will appear in the
expand-points list. Choose the PV to expand, and then the options for
expanding that object. After the PV has expanded, the container's freespace
will reflect the additional space available on that PV.

When using the CLI, PV-expand is performed by expanding the appropriate
object directly. The CLI and the EVMS engine will route the necessary
commands so the container is expanded at the same time.

The options for expanding a PV are dependent on the plug-in that owns that PV
object. Please see the appropriate plug-in's appendix for more details on
options for that object.
-----------------------------------------------------------------------------

D.1.5. Shrinking consumed objects in LVM2 containers

 In addition to removing existing objects from an LVM2 container, you can
also reduce the size of a container by shrinking one of the existing consumed
objects (PVs). This is only allowed if the consumed object has physical
extents (PEs) at the end of the object that are not allocated to any LVM2
regions. In this case, LVM2 will allow the object to shrink by the number of
unused PEs at the end of that object.

 For example, if a PV is a desk-segment, you can shrink that segment, which
will decrease the amount of freespace in the container. Likewise, if a PV is
a RAID-0 or RAID-5 region, you can shrink that region by removing one of the
objects, which in turn decreases the freespace in the container.

 When using the GUI or text-mode UIs, PV-shrink is performed by shrinking the
container. If any of the existing PVs are shrinkable, they will appear in the
shrink-points list. Choose the PV to shrink, and then the options for
shrinking that object. After the PV has shrunk, the container's freespace
will reflect the reduced space available on that PV.

 When using the CLI, PV-shrink is performed by shrinking the appropriate
object directly. The CLI and the EVMS engine will route the necessary
commands so the container is shrunk at the same time.

 The options for shrinking a PV are dependent on the plug-in that owns that
PV object. Please see the appropriate plug-in's appendix for more details on
options for that object.
-----------------------------------------------------------------------------

D.1.6. Deleting LVM2 containers

You can delete a container as long as the container does not have any
produced regions. The LVM2 plug-in does not allow containers to be deleted if
they have any regions. No options are available for deleting LVM2 containers.
-----------------------------------------------------------------------------

D.1.7. Renaming LVM2 containers

You can rename an existing LVM2 container. When renaming an LVM2 container,
all of the regions produced from that container will automatically have their
names changed as well, because the region names include the container name.
In the EVMS GUI and text-mode UIs, this is done using the modify properties
command, which is available through the "Actions" menu or the
context-sensitive pop-up menus. In the EVMS CLI, this is done using the set
command.

See Section D.2.5 for more information about the effects of renaming the
regions.
-----------------------------------------------------------------------------

D.2. Region operations

D.2.1. Creating LVM2 regions

You create LVM2 regions from the freespace in LVM2 containers. If there is at
least one extent of freespace in the container, you can create a new region.

The following options are available for creating LVM2 regions:

name
    The name of the new region.

size
    The size of the new region. This size must be a multiple of the
    container's extent-size. If it isn't, the size will be rounded down as
    appropriate. By default, all of the available freespace in the container
    will be used for the new region.

stripes
    If the container consumes two or more objects, and each object has
    unallocated extents, then the new region can be striped across multiple
    objects. This is similar to RAID-0 striping and achieves an increased
    amount of I/O throughput. This option specifies how many objects the new
    region should be striped across. By default, new regions are not striped,
    and this value is set to 1.

stripe_size
    The granularity of striping. The default value is 64 KB. Use this option
    only if the stripes option is greater than 1.

pvs
    A list of names of the objects the new region should map to. By default,
    this list is empty, which means all available objects will be used to
    allocate space to the new region.


-----------------------------------------------------------------------------
D.2.2. Expanding LVM2 regions

You can expand an existing LVM region if there are any unused extents in the
container. The following options are available for expanding LVM regions.

size
    The amount of space to add to the region. This is a delta-size, not the
    new absolute size of the region. As with creating new regions, this size
    must be a multiple of the container's extent-size, and will be rounded
    down if necessary.

stripes
    The number of objects to stripe this new portion of the region across.
    This value can be different than the number of stripes in the existing
    region. For example, if the region was created originally with three
    stripes, but now only two objects are available, then the new portion of
    the region could be striped across just those two objects. The number of
    stripes for the last mapping in the region will be used as the default.

stripe_size
    The granularity of striping. As with the number of stripes, this value
    can be different than the stripe-size for the existing region. By
    default, the stripe-size of the last mapping in the region is used.

pvs
    A list of names of the objects the region should be expanded onto. By
    default, this list is empty, which means all available objects will be
    used to allocate additional space for the region.


-----------------------------------------------------------------------------
D.2.3. Shrinking LVM2 regions

You can shrink an existing LVM region by removing extents from the end of the
region. Regions must have at least one extent, so regions cannot be shrunk to
zero.

The following options are available when shrinking LVM regions. Because
regions are always shrunk by removing space from the end of the region, a
list of objects cannot be specified in this command.

size
    The amount of space to remove from the region. This is a delta-size, not
    the new absolute size of the region. As with creating and expanding
    regions, this size must be a multiple of the container's extent-size, and
    will be rounded down if necessary.


-----------------------------------------------------------------------------
D.2.4. Deleting LVM2 regions

You can delete an existing LVM region as long as it is not currently a
compatibility volume, an EVMS volume, or consumed by another EVMS plug-in. No
options are available for deleting LVM regions.
-----------------------------------------------------------------------------

D.2.5. Renaming LVM2 regions

You can rename an existing LVM2 region. In the EVMS GUI and text-mode UIs,
this is done using the modify properties command, which is available through
the "Actions" menu or the context-sensitive pop-up menus. In the EVMS CLI,
this is done using the set command.

If the renamed LVM2 region has a compatibility volume on it, then the name of
that compatibility volume will also change. In order for this to work
correctly, that volume must be unmounted before the name is changed. Also, be
sure to update your /etc/fstab file if the volume is listed, or the volume
won't be mounted properly the next time the system boots.

If the renamed LVM2 region has an EVMS volume or another storage object built
on it, then the region's name change will be transparent to the upper layers.
In this case, the rename can be done while the volume is mounted.
-----------------------------------------------------------------------------

Appendix E. The CSM plug-in

The Cluster Segment Manager (CSM) is the EVMS plug-in that identifies and
manages cluster storage. The CSM protects disk storage objects by writing
metadata at the start and end of the disk, which prevents other plug-ins from
attempting to use the disk. Other plug-ins can look at the disk, but they
cannot see their own metadata signatures and cannot consume the disk. The
protection that CSM provides allows the CSM to discover cluster storage and
present it in an appropriate fashion to the system.

All cluster storage disk objects must be placed in containers that have the
following attributes:

��*�cluster ID that identifies the cluster management software

��*�node ID that identifies the owner of the disk objects

��*�storage type: private, shared, or deported


 The CSM plug-in reads metadata and constructs containers that consume the
disk object. Each disk provides a usable area, mapped as an EVMS data
segment, but only if the disk is accessible to the node viewing the storage.

The CSM plug-in performs these operations:

��*� examines disk objects

��*� creates containers

��*� uses the containers to consume disk objects

��*� produces data segment objects if the disk is accessible to the node


-----------------------------------------------------------------------------
E.1. Assigning the CSM plug-in

Assigning a segment manager to a disk means that you want the plug-in to
manage partitions on the disk. In order to do this, the plug-in needs to
create and maintain appropriate metadata. The CSM creates the follow three
segments on the disk:

��*�primary metadata segment

��*�usable area data segment

��*�secondary metadata segment


The CSM collects the information it needs to perform the assign operation
with the following options:

NodeId
    Choose only from a list of configured node IDs that have been provided to
    the CSM by clustering software. The default selection is the node from
    which you are running the EVMS user interface.

Container Name
    The name for the container. You need to keep this name unique across the
    cluster to prevent name-in-conflict errors should the container fail over
    to another node that has a container with the same name.

Storage Type
    Can be either: share, private, or deported.


Note that you would typically assign the CSM to a disk when you want to add a
disk to an existing CSM container. If you are creating a new container, you
have a choice of using either: Actions->Create->Container or Actions->Add->
Segment Manager.

If the container doesn't exist, it will be created for the disk. If the
container already exists, the disk will be added to it.
-----------------------------------------------------------------------------

E.2. Unassigning the CSM plug-in

Unassigning a CSM plug-in results in the CSM removing its metadata from the
specified disk storage object. The result is that the disk has no segments
mapped and appears as a raw disk object. The disk is removed from the
container that consumed it and the data segment is removed as well.
-----------------------------------------------------------------------------

E.3. Deleting a CSM container

An existing CSM container cannot be deleted if it is producing any data
segments, because other EVMS plug-ins might be building higher-level objects
on the CSM objects. To delete a CSM container, first remove disk objects from
the container. When the last disk is removed, the container is also removed.
-----------------------------------------------------------------------------

Appendix F. JFS file system interface module

 The JFS FSIM lets EVMS users create and manage JFS file systems from within
the EVMS interfaces. In order to use the JFS FSIM, version 1.0.9 or later of
the JFS utilities must be installed on your system. The latest version of JFS
can be found at [http://oss.software.ibm.com/jfs/] http://
oss.software.ibm.com/jfs/.
-----------------------------------------------------------------------------

F.1. Creating JFS file systems

 JFS file systems can be created with mkfs on any EVMS or compatibility
volume (at least 16 MB in size) that does not already have a file system. The
following options are available for creating JFS file systems:

badblocks
    Perform a read-only check for bad blocks on the volume before creating
    the file system. The default is false.

caseinsensitive
    Mark the file system as case-insensitive (for OS/2 compatibility). The
    default is false.

vollabel
    Specify a volume label for the file system. The default is none.

journalvol
    Specify the volume to use for an external journal. This option is only
    available with version 1.0.20 or later of the JFS utilities. The default
    is none.

logsize
     Specify the inline log size (in MB). This option is only available if
    the journalvol option is not set. The default is 0.4% of the size of the
    volume up to 32 MB.


-----------------------------------------------------------------------------
F.2. Checking JFS file systems

 The following options are available for checking JFS file systems with fsck:

force
    Force a complete file system check, even if the file system is already
    marked clean. The default is false.

readonly
    Check the file system is in read-only mode. Report but do not fix errors.
    If the file system is mounted, this option is automatically selected. The
    default is false.

omitlog
    Omit replaying the transaction log. This option should only be specified
    if the log is corrupt. The default is false.

verbose
    Display details and debugging information during the check. The default
    is false.

version
    Display the version of fsck.jfs and exit without checking the file
    system. The default is false.


-----------------------------------------------------------------------------
F.3. Removing JFS file systems

 A JFS file system can be removed from its volume if the file system is
