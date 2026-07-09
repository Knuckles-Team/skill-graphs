
B.2.1. RAID-0 options

 RAID-0 has the following option:

chunksize
     This option represents the granularity of the striped data. In other
    words, the amount of data that is written to one child object before
    moving to the next object. The range of valid values is 4 KB to 4096 KB,
    and must be a power of 2. If the option is not specified, the default
    chunk size of 32 KB will be used.


-----------------------------------------------------------------------------
B.2.2. RAID-1 options

 RAID-1 has the following option:

sparedisk
     This option is the name of another object to use as a "hot-spare." This
    object cannot be one of the objects selected in the initial
    object-selection list. If no object is selected for this option, then the
    new region will simply not initially have a spare. More information about
    spare objects is in the following sections.


-----------------------------------------------------------------------------
B.2.3. RAID-4/5 options

 RAID-4/5 have the following options:

chunksize
     This is the same as the chunksize option for RAID-0.

sparedisk
     This is the same as the sparedisk option for RAID-1.

level
     Choose between RAID4 and RAID5. The default value for this option is
    RAID5.

algorithm
     If the RAID-5 level is chosen, this option allows choosing the desired
    parity algorithm. Valid choices are "Left Symmetric" (which is the
    default), "Right Symmetric," "Left Asymmetric, and "Right Asymmetric." If
    the RAID-4 level is chosen, this option is not available.


-----------------------------------------------------------------------------
B.3. Active and spare objects

 An active object in a RAID region is one that is actively used by the region
and contains data or parity information. When creating a new RAID region, all
the objects selected from the main available-objects panel will be active
objects. Linear-RAID and RAID-0 regions only have active objects, and if any
of those active objects fail, the region is unavailable.

 On the other hand, the redundant RAID levels (1 and 4/5) can have spare
objects in addition to their active objects. A spare is an object that is
assigned to the region, but does not contain any live data or parity. Its
primary purpose is to act as a "hot standby" in case one of the active
objects fails.

 In the event of a failure of one of the child objects, the MD kernel driver
removes the failed object from the region. Because these RAID levels provide
redundancy (either in the form of mirrored data or parity information), the
whole region can continue providing normal access to the data. However,
because one of the active objects is missing, the region is now "degraded."

 If a region becomes degraded and a spare object has been assigned to that
region, the kernel driver will automatically activate that spare object. This
means the spare object is turned into an active object. However, this newly
active object does not have any data or parity information, so the kernel
driver must "sync" the data to this object. For RAID-1, this means copying
all the data from one of the current active objects to this new active
object. For RAID-4/5, this means using the data and parity information from
the current active objects to fill in the missing data and parity on the new
active object. While the sync process is taking place, the region remains in
the degraded state. Only when the sync is complete does the region return to
the full "clean" state.

 You can follow the progress of the sync process by examining the /proc/
mdstat file. You can also control the speed of the sync process using the
files /proc/sys/dev/raid/speed_limit_min and /proc/sys/dev/raid/
speed_limit_max. To speed up the process, echo a larger number into the
speed_limit_min file.
-----------------------------------------------------------------------------

B.3.1. Adding spare objects

 As discussed above, a spare object can be assigned to a RAID-1 or RAID-4/5
region when the region is created. In addition, a spare object can also be
added to an already existing RAID region. The effect of this operation is the
same as if the object were assigned when the region was created.

 If the RAID region is clean and operating normally, the kernel driver will
add the new object as a regular spare, and it will act as a hot-standby for
future failures. If the RAID region is currently degraded, the kernel driver
will immediately activate the new spare object and begin syncing the data and
parity information.

 For both RAID-1 and RAID-4/5 regions, use the "addspare" plug-in function to
add a new spare object to the region. The only argument is the name of the
desired object, and only one spare object can be added at a time. For RAID-1
regions, the new spare object must be at least as big as the region, and for
RAID-4/5 regions, the new spare object must be at least as big as the
smallest active object.

 Spare objects can be added while the RAID region is active and in use.
-----------------------------------------------------------------------------

B.3.2. Removing spare objects

 If a RAID-1 or RAID-4/5 region is clean and operating normally, and that
region has a spare object, the spare object can be removed from the region if
you need to use that object for another purpose.

 For both RAID-1 and RAID-4/5 regions, use the "remspare" plug-in function to
remove a spare object from the region. The only argument is the name of the
desired object, and only one spare object can be removed at a time. After the
spare is removed, that object will show up in the Available-Objects list in
the EVMS user interfaces.

 Spare objects can be removed while the RAID region is active and in use.
-----------------------------------------------------------------------------

B.3.3. Adding active objects to RAID-1

 In RAID-1 regions, every active object has a full copy of the data for the
region. This means it is easy to simply add a new active object, sync the
data to this new object, and thus increase the "width" of the mirror. For
instance, if you have a 2-way RAID-1 region, you can add a new active object,
which will increase the region to a 3-way mirror, which increases the amount
of redundancy offered by the region.

 The first process of adding a new active object can be done in one of two
ways. First, the "addactive" plug-in function adds any available object in
EVMS to the region as a new active object. The new object must be at least as
big as the size of the RAID-1 region. Second, if the RAID-1 region has a
spare object, that object can be converted to an active member of the region
using the "activatespare" plug-in function.
-----------------------------------------------------------------------------

B.4. Faulty objects

 As discussed in the previous section, if one of the active objects in a
RAID-1 or RAID-4/5 region has a problem, that object will be kicked out and
the region will become degraded. A problem can occur with active objects in a
variety of ways. For instance, a disk can crash, a disk can be pulled out of
the system, a drive cable can be removed, or one or more I/Os can cause
errors. Any of these will result in the object being kicked out and the RAID
region becoming degraded.

 If a disk has completely stopped working or has been removed from the
machine, EVMS obviously will no longer recognize that disk, and it will not
show up as part of the RAID region when running the EVMS user interfaces.
However, if the disk is still available in the machine, EVMS will likely be
able to recognize that the disk is assigned to the RAID region, but has been
removed from any active service by the kernel. This type of disk is referred
to as a faulty object.
-----------------------------------------------------------------------------

B.4.1. Removing faulty objects

 Faulty objects are no longer usable by the RAID region, and should be
removed. You can remove faulty objects with the "remfaulty" plug-in function
for both RAID-1 and RAID-4/5. This operation is very similar to removing
spare objects. After the object is removed, it will appear in the
Available-Objects list in the EVMS user interfaces.

 Faulty objects can be removed while the RAID region is active and in use.
-----------------------------------------------------------------------------

B.4.2. Fixing temporarily failed objects

 Sometimes a disk can have a temporary problem that causes the disk to be
marked faulty and the RAID region to become degraded. For instance, a drive
cable can come loose, causing the MD kernel driver to think the disk has
disappeared. However, if the cable is plugged back in, the disk should be
available for normal use. However, the MD kernel driver and the EVMS MD
plug-in will continue to indicate that the disk is a faulty object because
the disk might have missed some writes to the RAID region and would therefore
be out of sync with the rest of the disks in the region.

 In order to correct this situation, the faulty object should be removed from
the RAID region (as discussed in the previous section). The object will then
show up as an Available-Object. Next, that object should be added back to the
RAID region as a spare (as discussed in Section B.3.1. When the changes are
saved, the MD kernel driver will activate the spare and sync the data and
parity. When the sync is complete, the RAID region will be operating in its
original, normal configuration.

 This procedure can be accomplished while the RAID region is active and in
use.
-----------------------------------------------------------------------------

B.4.3. Marking objects faulty

 EVMS provides the ability to manually mark a child of a RAID-1 or RAID-4/5
region as faulty. This has the same effect as if the object had some problem
or caused I/O errors. The object will be kicked out from active service in
the region, and will then show up as a faulty object in EVMS. It can then be
removed from the region as discussed in the previous sections.

 There are a variety of reasons why you might want to manually mark an object
faulty. One example would be to test failure scenarios to learn how Linux and
EVMS deal with the hardware failures. Another example would be that you want
to replace one of the current active objects with a different object. To do
this, you would add the new object as a spare, then mark the current object
faulty (causing the new object to be activated and the data to be resynced),
and finally remove the faulty object.

 EVMS allows you to mark an object faulty in a RAID-1 region if there are
more than one active objects in the region. EVMS allows you to mark an object
faulty in a RAID-4/5 region if the region has a spare object.

 Use the "markfaulty" plug-in function for both RAID-1 and RAID-4/5. This
command can be used while the RAID region is active and in use.
-----------------------------------------------------------------------------

B.5. Resizing MD regions

 RAID regions can be resized in order to expand or shrink the available data
space in the region. Each RAID level has different characteristics, and thus
each RAID level has different requirements for when and how they can expand
or shrink.

 See Chapter 16 for general information about resizing EVMS volumes and
objects.
-----------------------------------------------------------------------------

B.5.1. Linear

 A Linear-RAID region can be expanded in two ways. First, if the last child
object in the Linear-RAID region is expandable, then that object can be
expanded, and the RAID region can expand into that new space. Second, one or
more new objects can be added to the end of the region.

 Likewise, a Linear-RAID region can be shrunk in two ways. If the last child
object in the region is shrinkable, then that object can be shrunk, and the
RAID region will shrink by the same amount. Also, one or more objects can be
removed from the end of the RAID region (but the first object in the region
cannot be removed).

 Linear-RAID regions can be resized while they are active and in use.
-----------------------------------------------------------------------------

B.5.2. RAID-0

 You can expand a RAID-0 region by adding one new object to the region. You
can shrink a RAID-0 region by removing up to N-1 of the current child objects
in a region with N objects.

 Because RAID-0 regions stripe across the child objects, when a RAID-0 region
is resized, the data must be "re-striped" to account for the new number of
objects. This means the MD plug-in will move each chunk of data from its
location in the current region to the appropriate location in the expanded
region. Be forewarned, the re-striping process can take a long time. At this
time, there is no mechanism for speeding up or slowing down the re-striping
process. The EVMS GUI and text-mode user interface will indicate the progress
of the re-striping. Please do not attempt to interrupt the re-striping before
it is complete, because the data in the RAID-0 region will likely become
corrupted.

 RAID-0 regions must be deactivated before they are resized in order to
prevent data corruption while the data is being re-striped.

 IMPORTANT: Please have a suitable backup available before attempting a
RAID-0 resize. If the re-striping process is interrupted before it completes
(for example, the EVMS process gets killed, the machine crashes, or a child
object in the RAID region starts returning I/O errors), then the state of
that region cannot be ensured in all situations.

 EVMS will attempt to recover following a problem during a RAID-0 resize. The
MD plug-in does keep track of the progress of the resize in the MD metadata.
Each time a data chunk is moved, the MD metadata is updated to reflect which
chunk is currently being processed. If EVMS or the machine crashes during a
resize, the next time you run EVMS the MD plug-in will try to restore the
state of that region based on the latest metadata information. If an expand
was taking place, the region will be "rolled back" to its state before the
expand. If a shrink was taking place, the shrink will continue from the point
it stopped. However, this recovery is not always enough to ensure that the
entire volume stack is in the correct state. If the RAID-0 region is made
directly into a volume, then it will likely be restored to the correct state.
On the other hand, if the RAID region is a consumed-object in an LVM
container, or a child-object of another RAID region, then the metadata for
those plug-ins might not always be in the correct state and might be at the
wrong location on the RAID region. Thus, the containers, objects, and volumes
built on top of the RAID-0 region might not reflect the correct size and
might not even be discovered.
-----------------------------------------------------------------------------

B.5.3. RAID-1

 A RAID-1 region can be resized if all of the child objects can be
simultaneously resized by the same amount.

 RAID-1 regions cannot be resized by adding additional objects. This type of
operation is referred to as "adding active objects," and is discussed in
Section B.3.3.

 RAID-1 regions must be deactivated before they are resized.
-----------------------------------------------------------------------------

B.5.4. RAID-4/5

Resizing a RAID-4/5 region follows the same rules and restrictions for
resizing a RAID-0 region. Expand a RAID-4/5 region by adding one new object
to the region. Shrink a RAID-4/5 region by removing up to N-1 of the current
child objects in a region with N objects.

See Section B.5.2 for information about how to perform this function.

 Like RAID-0, RAID-4/5 regions must be deactivated before they are resized.
-----------------------------------------------------------------------------

B.6. Replacing objects

The MD plug-in allows the child objects of a RAID region to be replaced with
other available objects. This is accomplished using the general EVMS replace
function. Please see Chapter 22 for more detailed information about how to
perform this function.

For all RAID levels, the replacement object must be at least as big as the
child object being replaced. If the replacement object is bigger than the
child object being replaced, the extra space on the replacement object will
be unused. In order to perform a replace operation, any volumes that comprise
the RAID region must be unmounted.

This capability is most useful for Linear-RAID and RAID-0 regions. It is also
allowed with RAID-1 and RAID-4/5, but those two RAID levels offer the ability
to mark objects faulty, which accomplishes the same end result. Because that
process can be done while the region is in use, it is generally preferable to
object-replace, which must be done with the region deactivated.
-----------------------------------------------------------------------------

Appendix C. The LVM plug-in

The LVM plug-in combines storage objects into groups called containers. From
these containers, new storage objects can be created, with a variety of
mappings to the consumed objects. Containers allow the storage capacity of
several objects to be combined, allow additional storage to be added in the
future, and allow for easy resizing of the produced objects.
-----------------------------------------------------------------------------

C.1. How LVM is implemented

The Linux LVM plug-in is compatible with volumes and volume groups from the
original Linux LVM tools from Sistina Software. The original LVM is based on
the concept of volume groups. A volume group (VG) is a grouping of physical
volumes (PVs), which are usually disks or disk partitions. The volume group
is not directly usable as storage space; instead, it represents a pool of
available storage. You create logical volumes (LVs) to use this storage. The
storage space of the LV can map to one or more of the group's PVs.

The Linux LVM concepts are represented by similar concepts in the EVMS LVM
plug-in. A volume group is called a container, and the logical volumes that
are produced are called regions. The physical volumes can be disks, segments,
or other regions. Just as in the original LVM, regions can map to the
consumed objects in a variety of ways.
-----------------------------------------------------------------------------

C.2. Container operations

C.2.1. Creating LVM containers

Containers are created with an initial set of objects. In the LVM plug-in,
the objects can be disks, segments, or regions. LVM has two options for
creating containers. The value of these options cannot be changed after the
container has been created. The options are:

name
    The name of the new container.

pe_size
    The physical extent (PE) size, which is the granularity with which
    regions can be created. The default is 16 MB. Each region must have a
    whole number of extents. Also, each region can have only up to 65534
    extents. Thus, the PE size for the container limits the maximum size of a
    region in that container. With the default PE size, an LVM region can be,
    at most 1 TB. In addition, each object consumed by the container must be
    big enough to hold at least five extents. Thus, the PE size cannot be
    arbitrarily large. Choose wisely.


-----------------------------------------------------------------------------
C.2.2. Adding objects to LVM containers

You can add objects to existing LVM containers in order to increase the pool
of storage that is available for creating regions. A single container can
consume up to 256 objects. Because the name and PE size of the containers are
set when the container is created, no options are available when you add new
objects to a container. Each object must be large enough to hold five
physical extents. If an object is not large enough to satisfy this
requirement, the LVM plug-in will not allow the object to be added to the
container.
-----------------------------------------------------------------------------

C.2.3. Removing objects from LVM containers

You can remove a consumed object from its container as long as no regions are
mapped to that object. The LVM plug-in does not allow objects that are in use
to be removed their their container. If an object must be removed, you can
delete or shrink regions, or move extents, in order to free the object from
use.

No options are available for removing objects from LVM containers.
-----------------------------------------------------------------------------

C.2.4. Expanding consumed objects in LVM containers

In addition to adding new objects to an LVM container, you can also expand
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

C.2.5. Shrinking consumed objects in LVM containers

 In addition to removing existing objects from an LVM container, you can also
reduce the size of a container by shrinking one of the existing consumed
objects (PVs). This is only allowed if the consumed object has physical
extents (PEs) at the end of the object that are not allocated to any LVM
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

C.2.6. Deleting LVM containers

You can delete a container as long as the container does not have any
produced regions. The LVM plug-in does not allow containers to be deleted if
they have any regions. No options are available for deleting LVM containers.
-----------------------------------------------------------------------------

C.2.7. Renaming LVM containers

You can rename an existing LVM container. When renaming an LVM container, all
of the regions produced from that container will automatically have their
names changed as well, because the region names include the container name.
In the EVMS GUI and text-mode UIs, this is done using the modify properties
command, which is available through the "Actions" menu or the
context-sensitive pop-up menus. In the EVMS CLI, this is done using the set
command.

See Section C.3.6 for more information about the effects of renaming the
regions.
-----------------------------------------------------------------------------

C.3. Region operations

C.3.1. Creating LVM regions

You create LVM regions from the freespace in LVM containers. If there is at
least one extent of freespace in the container, you can create a new region.

The following options are available for creating LVM regions:

name
    The name of the new region.

extents
    The number of extents to allocate to the new region. A new region must
    have at least one extent and no more than the total available free
    extents in the container, or 65534 (whichever is smaller). If you use the
    extents option, the appropriate value for the size option is
    automatically calculated. By default, a new region uses all available
    extents in the container.

size
    The size of the new region. This size must be a multiple of the
    container's PE size. If you use the size option, the appropriate value
    for the extents options is automatically calculated. By default, a new
    region uses all available freespace in the container.

stripes
    If the container consumes two or more objects, and each object has
    unallocated extents, then the new region can be striped across multiple
    objects. This is similar to RAID-0 striping and achieves an increased
