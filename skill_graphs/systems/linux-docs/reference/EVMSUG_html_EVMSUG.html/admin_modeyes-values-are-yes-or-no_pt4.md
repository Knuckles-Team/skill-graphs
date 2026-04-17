Because RAID-0 regions stripe across the child objects, when a RAID-0 region is resized, the data must be "re-striped" to account for the new number of objects. This means the MD plug-in will move each chunk of data from its location in the current region to the appropriate location in the expanded region. Be forewarned, the re-striping process can take a long time. At this time, there is no mechanism for speeding up or slowing down the re-striping process. The EVMS GUI and text-mode user interface will indicate the progress of the re-striping. Please do not attempt to interrupt the re-striping before it is complete, because the data in the RAID-0 region will likely become corrupted.
RAID-0 regions must be deactivated before they are resized in order to prevent data corruption while the data is being re-striped.
IMPORTANT: Please have a suitable backup available before attempting a RAID-0 resize. If the re-striping process is interrupted before it completes (for example, the EVMS process gets killed, the machine crashes, or a child object in the RAID region starts returning I/O errors), then the state of that region cannot be ensured in all situations.
EVMS will attempt to recover following a problem during a RAID-0 resize. The MD plug-in does keep track of the progress of the resize in the MD metadata. Each time a data chunk is moved, the MD metadata is updated to reflect which chunk is currently being processed. If EVMS or the machine crashes during a resize, the next time you run EVMS the MD plug-in will try to restore the state of that region based on the latest metadata information. If an expand was taking place, the region will be "rolled back" to its state before the expand. If a shrink was taking place, the shrink will continue from the point it stopped. However, this recovery is not always enough to ensure that the entire volume stack is in the correct state. If the RAID-0 region is made directly into a volume, then it will likely be restored to the correct state. On the other hand, if the RAID region is a consumed-object in an LVM container, or a child-object of another RAID region, then the metadata for those plug-ins might not always be in the correct state and might be at the wrong location on the RAID region. Thus, the containers, objects, and volumes built on top of the RAID-0 region might not reflect the correct size and might not even be discovered.
* * *
##  B.5.3. RAID-1
A RAID-1 region can be resized if all of the child objects can be simultaneously resized by the same amount.
RAID-1 regions cannot be resized by adding additional objects. This type of operation is referred to as "adding active objects," and is discussed in [Section B.3.3](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#addactobjsr1).
RAID-1 regions must be deactivated before they are resized.
* * *
##  B.5.4. RAID-4/5
Resizing a RAID-4/5 region follows the same rules and restrictions for resizing a RAID-0 region. Expand a RAID-4/5 region by adding one new object to the region. Shrink a RAID-4/5 region by removing up to N-1 of the current child objects in a region with N objects.
See [Section B.5.2](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#resizeraid0) for information about how to perform this function.
Like RAID-0, RAID-4/5 regions must be deactivated before they are resized.
* * *
#  B.6. Replacing objects
The MD plug-in allows the child objects of a RAID region to be replaced with other available objects. This is accomplished using the general EVMS replace function. Please see [Chapter 22](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmsreplaceobjects) for more detailed information about how to perform this function.
For all RAID levels, the replacement object must be at least as big as the child object being replaced. If the replacement object is bigger than the child object being replaced, the extra space on the replacement object will be unused. In order to perform a replace operation, any volumes that comprise the RAID region must be unmounted.
This capability is most useful for Linear-RAID and RAID-0 regions. It is also allowed with RAID-1 and RAID-4/5, but those two RAID levels offer the ability to mark objects faulty, which accomplishes the same end result. Because that process can be done while the region is in use, it is generally preferable to object-replace, which must be done with the region deactivated.
* * *
#  Appendix C. The LVM plug-in
The LVM plug-in combines storage objects into groups called containers. From these containers, new storage objects can be created, with a variety of mappings to the consumed objects. Containers allow the storage capacity of several objects to be combined, allow additional storage to be added in the future, and allow for easy resizing of the produced objects.
* * *
#  C.1. How LVM is implemented
The Linux LVM plug-in is compatible with volumes and volume groups from the original Linux LVM tools from Sistina Software. The original LVM is based on the concept of volume groups. A volume group (VG) is a grouping of physical volumes (PVs), which are usually disks or disk partitions. The volume group is not directly usable as storage space; instead, it represents a pool of available storage. You create logical volumes (LVs) to use this storage. The storage space of the LV can map to one or more of the group's PVs.
The Linux LVM concepts are represented by similar concepts in the EVMS LVM plug-in. A volume group is called a container, and the logical volumes that are produced are called regions. The physical volumes can be disks, segments, or other regions. Just as in the original LVM, regions can map to the consumed objects in a variety of ways.
* * *
#  C.2. Container operations
##  C.2.1. Creating LVM containers
Containers are created with an initial set of objects. In the LVM plug-in, the objects can be disks, segments, or regions. LVM has two options for creating containers. The value of these options cannot be changed after the container has been created. The options are:

name

The name of the new container.

pe_size

The physical extent (PE) size, which is the granularity with which regions can be created. The default is 16 MB. Each region must have a whole number of extents. Also, each region can have only up to 65534 extents. Thus, the PE size for the container limits the maximum size of a region in that container. With the default PE size, an LVM region can be, at most 1 TB. In addition, each object consumed by the container must be big enough to hold at least five extents. Thus, the PE size cannot be arbitrarily large. Choose wisely.
* * *
##  C.2.2. Adding objects to LVM containers
You can add objects to existing LVM containers in order to increase the pool of storage that is available for creating regions. A single container can consume up to 256 objects. Because the name and PE size of the containers are set when the container is created, no options are available when you add new objects to a container. Each object must be large enough to hold five physical extents. If an object is not large enough to satisfy this requirement, the LVM plug-in will not allow the object to be added to the container.
* * *
##  C.2.3. Removing objects from LVM containers
You can remove a consumed object from its container as long as no regions are mapped to that object. The LVM plug-in does not allow objects that are in use to be removed their their container. If an object must be removed, you can delete or shrink regions, or move extents, in order to free the object from use.
No options are available for removing objects from LVM containers.
* * *
##  C.2.4. Expanding consumed objects in LVM containers
In addition to adding new objects to an LVM container, you can also expand the space in a container by expanding one of the existing consumed objects (PVs). For example, if a PV is a disk-segment with freespace immediately following it on the disk, you can expand that segment, which will increase the amount of freespace in the container. Likewise, if a PV is a RAID-0 or RAID-5 region, you can expand that region by adding additional objects, which in turn increases the freespace in the container.
When using the GUI or text-mode UIs, PV-expand is performed by expanding the container. If any of the existing PVs are expandable, they will appear in the expand-points list. Choose the PV to expand, and then the options for expanding that object. After the PV has expanded, the container's freespace will reflect the additional space available on that PV.
When using the CLI, PV-expand is performed by expanding the appropriate object directly. The CLI and the EVMS engine will route the necessary commands so the container is expanded at the same time.
The options for expanding a PV are dependent on the plug-in that owns that PV object. Please see the appropriate plug-in's appendix for more details on options for that object.
* * *
##  C.2.5. Shrinking consumed objects in LVM containers
In addition to removing existing objects from an LVM container, you can also reduce the size of a container by shrinking one of the existing consumed objects (PVs). This is only allowed if the consumed object has physical extents (PEs) at the end of the object that are not allocated to any LVM regions. In this case, LVM2 will allow the object to shrink by the number of unused PEs at the end of that object.
For example, if a PV is a desk-segment, you can shrink that segment, which will decrease the amount of freespace in the container. Likewise, if a PV is a RAID-0 or RAID-5 region, you can shrink that region by removing one of the objects, which in turn decreases the freespace in the container.
When using the GUI or text-mode UIs, PV-shrink is performed by shrinking the container. If any of the existing PVs are shrinkable, they will appear in the shrink-points list. Choose the PV to shrink, and then the options for shrinking that object. After the PV has shrunk, the container's freespace will reflect the reduced space available on that PV.
When using the CLI, PV-shrink is performed by shrinking the appropriate object directly. The CLI and the EVMS engine will route the necessary commands so the container is shrunk at the same time.
The options for shrinking a PV are dependent on the plug-in that owns that PV object. Please see the appropriate plug-in's appendix for more details on options for that object.
* * *
##  C.2.6. Deleting LVM containers
You can delete a container as long as the container does not have any produced regions. The LVM plug-in does not allow containers to be deleted if they have any regions. No options are available for deleting LVM containers.
* * *
##  C.2.7. Renaming LVM containers
You can rename an existing LVM container. When renaming an LVM container, all of the regions produced from that container will automatically have their names changed as well, because the region names include the container name. In the EVMS GUI and text-mode UIs, this is done using the **modify properties** command, which is available through the "Actions" menu or the context-sensitive pop-up menus. In the EVMS CLI, this is done using the **set** command.
See [Section C.3.6](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#renamereg) for more information about the effects of renaming the regions.
* * *
#  C.3. Region operations
##  C.3.1. Creating LVM regions
You create LVM regions from the freespace in LVM containers. If there is at least one extent of freespace in the container, you can create a new region.
The following options are available for creating LVM regions:

name

The name of the new region.

extents

The number of extents to allocate to the new region. A new region must have at least one extent and no more than the total available free extents in the container, or 65534 (whichever is smaller). If you use the `extents` option, the appropriate value for the size option is automatically calculated. By default, a new region uses all available extents in the container.

size

The size of the new region. This size must be a multiple of the container's PE size. If you use the `size` option, the appropriate value for the extents options is automatically calculated. By default, a new region uses all available freespace in the container.

stripes

If the container consumes two or more objects, and each object has unallocated extents, then the new region can be striped across multiple objects. This is similar to RAID-0 striping and achieves an increased amount of I/O throughput across multiple objects. This option specifies how many objects the new region should be striped across. By default, new regions are not striped, and this value is set to 1.

stripe_size

The granularity of striping. The default value is 16 KB. Use this option only if the `stripes` option is greater than 1.

contiguous

This option specifies that the new region must be allocated on a single object, and that the extents on that object must be physically contiguous. By default, this is set to false, which allows regions to span objects. This option cannot be used if the `stripes` option is greater than 1.

pv_names

A list of names of the objects the new region should map to. By default, this list is empty, which means all available objects will be used to allocate space to the new region.
* * *
##  C.3.2. Expanding LVM regions
You can expand an existing LVM region if there are unused extents in the container. If a region is striped, you can expand it only by using free space on the objects it is striped across. If a region was created with the contiguous option, you can only expand it if there is physically contiguous space following the currently allocated space.
The following options are available for expanding LVM regions:

add_extents

The number of extents to add to the region. If you specify this option, the appropriate value for the add_size option is automatically calculated. By default, the region will expand to use all free extents in the container.

add_size

The amount of space to add to the region. If you specify this option, the appropriate value for the add_extents option is automatically calculated. By default, the region will expand to use all freespace in the container.

pv_names

A list of names of the objects to allocate the additional space from. By default, this list is empty, which means all available objects will be used to allocate new space to the region.
* * *
##  C.3.3. Shrinking LVM regions
You can shrink an existing LVM region by removing extents from the end of the region. Regions must have at least one extent, so regions cannot be shrunk to zero.
The following options are available when shrinking LVM regions. Because regions are always shrunk by removing space from the end of the region, a list of objects cannot be specified in this command.

remove_extents

The number of extents to remove from the region. If you specify this option, the appropriate value for the `remove_size` option is automatically calculated. By default, one extent is removed from the region.

remove_size

The amount of space to shrink the region by. If you specify this option, the appropriate value for the `remove_extents` option is automatically calculated.
* * *
##  C.3.4. Deleting LVM regions
You can delete an existing LVM region as long as it is not currently a compatibility volume, an EVMS volume, or consumed by another EVMS plug-in. No options are available for deleting LVM regions.
* * *
##  C.3.5. Moving LVM regions
The LVM plug-in lets you change the logical-to-physical mapping for an LVM region and move the necessary data in the process. This capability is most useful if a PV needs to be removed from a container. There are currently two LVM plug-in functions for moving regions: **move_pv** and **move_extent**.
* * *
###  C.3.5.1. move_pv
When a PV needs to be removed from a container, all PEs on that PV that are allocated to regions must be moved to other PVs. The **move_pv** command lets you move PEs to other PVs. **move_pv** is targeted at the LVM container and the desired PV is used as the selected object. The following options are available:

target_pvs

By default, all remaining PVs in the container are used to find available extents to move the PEs. You can specify a subset of the PVs with this option.

maintain_stripes

When the target PV contains striped regions, there are three choices for handling moving extents that belong to those regions:

no

Don't bother to maintain true striping. This choice allows extents to be moved to PVs that the region already uses for other stripes. This means that the performance will not be as optimal as it is with true striping, but allows the most flexibility in performing the move operation. This choice is the default for the **maintain_stripes** option.

loose

Ensure that moved extents do not end up on any PVs that the striped region already uses. However, this does not ensure that all moved extents end up on the same PV. For example, a region with three stripes may end up mapping to four or more PVs.

strict

Ensure that all moved extents end up on the same PV, thus ensuring true striping with the same number of PVs that the striped region originally used. This is the most restricted choice, and may prevent the **move_pv** operation from proceeding (depending on the particular configuration of the container).
If the target PV has no striped regions, the **maintain_stripes** option is ignored.
* * *
###  C.3.5.2. move_extent
In addition to moving all the extents from one PV, the LVM plug-in provides the ability to move single extents. This allows a fine-grain tuning of the allocation of extents. This command is targeted at the region owning the extent to move. There are three required options for the **move_extent** command:

le

The number of the logical extent to move. LE numbers start at 0.

pv

The target object to move the extent to.

pe

The target physical extent on the target object. PE numbers also start at 0.
To determine the source LE and target PE, it is often helpful to view the extended information about the region and container in question. The following are command-line options that can be used to gather this information:
To view the map of LEs in the region, enter this command:
```
query:ei,<region_name>,Extents
```

---
To view the list of PVs in the container, enter this command:
```
query:ei,<container_name>,Current_PVs
```

---
To view the current PE map for the desired target PV, enter this command:
```
query:ei,<container_name>,PEMapPV#
```

---
# is the number of the target PV in the container.
This information is also easily obtainable in the GUI and Text-Mode UIs by using the "Display Details" item in the context-popup menus for the desired region and container.
* * *
##  C.3.6. Renaming LVM regions
You can rename an existing LVM region. In the EVMS GUI and text-mode UIs, this is done using the **modify properties** command, which is available through the "Actions" menu or the context-sensitive pop-up menus. In the EVMS CLI, this is done using the **set** command.
If the renamed LVM region has a compatibility volume on it, then the name of that compatibility volume will also change. In order for this to work correctly, that volume must be unmounted before the name is changed. Also, be sure to update your `/etc/fstab` file if the volume is listed, or the volume won't be mounted properly the next time the system boots.
If the renamed LVM region has an EVMS volume or another storage object built on it, then the region's name change will be transparent to the upper layers. In this case, the rename can be done while the volume is mounted.
* * *
#  Appendix D. The LVM2 plug-in
The LVM2 plug-in provides compatibility with the new volume format introduced by the LVM2 tools from Red Hat (previously Sistina). This plug-in is very similar in functionality to the LVM plug-in. The primary difference is the new, improved metadata format. LVM2 is still based on the concept of volume groups (VGs), which are constructed from physical volumes (PVs) and produce logical volumes (LVs).
Just like the LVM plug-in, the LVM2 plug-in represents volume groups as EVMS containers and represents logical volumes as EVMS regions. LVM2 containers combine storage objects (disks, segments, or other regions) to create a pool of freespace. Regions are then created from this freespace, with a variety of mappings to the consumed objects.
* * *
#  D.1. Container operations
##  D.1.1. Creating LVM2 containers
Containers are created with an initial set of objects. These objects can be disks, segments, or regions. There are two options available when creating an LVM2 container:

name

The name of the new container.

extent_size

The physical-extent (PE) size, which is the granularity with which regions can be created. The default is 32 MB. Unlike the LVM1 plug-in, there is no limitation to the number of extents that can be allocated to an LVM2 region.
* * *
##  D.1.2. Adding objects to LVM2 containers
You can add objects to existing LVM containers in order to increase the pool of storage that is available for creating regions. Because the name and extent-size are set when the container is created, no options are available when you add new objects to a container. Each object must be large enough to hold at least one physical extent. If an object is not large enough to satisfy this requirement, the LVM2 plug-in will not allow the object to be added to the container.
* * *
##  D.1.3. Removing objects from LVM2 containers
You can remove a consumed object from its container as long as no regions are mapped to that object. The LVM2 plug-in does not allow objects that are in use to be removed from their container. If an object must be removed, you can delete or shrink regions, or move extents, in order to free the object from use.
No options are available for removing objects from LVM containers.
* * *
##  D.1.4. Expanding consumed objects in LVM2 containers
In addition to adding new objects to an LVM2 container, you can also expand the space in a container by expanding one of the existing consumed objects (PVs). For example, if a PV is a disk-segment with freespace immediately following it on the disk, you can expand that segment, which will increase the amount of freespace in the container. Likewise, if a PV is a RAID-0 or RAID-5 region, you can expand that region by adding additional objects, which in turn increases the freespace in the container.
When using the GUI or text-mode UIs, PV-expand is performed by expanding the container. If any of the existing PVs are expandable, they will appear in the expand-points list. Choose the PV to expand, and then the options for expanding that object. After the PV has expanded, the container's freespace will reflect the additional space available on that PV.
When using the CLI, PV-expand is performed by expanding the appropriate object directly. The CLI and the EVMS engine will route the necessary commands so the container is expanded at the same time.
The options for expanding a PV are dependent on the plug-in that owns that PV object. Please see the appropriate plug-in's appendix for more details on options for that object.
* * *
##  D.1.5. Shrinking consumed objects in LVM2 containers
In addition to removing existing objects from an LVM2 container, you can also reduce the size of a container by shrinking one of the existing consumed objects (PVs). This is only allowed if the consumed object has physical extents (PEs) at the end of the object that are not allocated to any LVM2 regions. In this case, LVM2 will allow the object to shrink by the number of unused PEs at the end of that object.
For example, if a PV is a desk-segment, you can shrink that segment, which will decrease the amount of freespace in the container. Likewise, if a PV is a RAID-0 or RAID-5 region, you can shrink that region by removing one of the objects, which in turn decreases the freespace in the container.
When using the GUI or text-mode UIs, PV-shrink is performed by shrinking the container. If any of the existing PVs are shrinkable, they will appear in the shrink-points list. Choose the PV to shrink, and then the options for shrinking that object. After the PV has shrunk, the container's freespace will reflect the reduced space available on that PV.
When using the CLI, PV-shrink is performed by shrinking the appropriate object directly. The CLI and the EVMS engine will route the necessary commands so the container is shrunk at the same time.
The options for shrinking a PV are dependent on the plug-in that owns that PV object. Please see the appropriate plug-in's appendix for more details on options for that object.
* * *
##  D.1.6. Deleting LVM2 containers
You can delete a container as long as the container does not have any produced regions. The LVM2 plug-in does not allow containers to be deleted if they have any regions. No options are available for deleting LVM2 containers.
* * *
##  D.1.7. Renaming LVM2 containers
You can rename an existing LVM2 container. When renaming an LVM2 container, all of the regions produced from that container will automatically have their names changed as well, because the region names include the container name. In the EVMS GUI and text-mode UIs, this is done using the **modify properties** command, which is available through the "Actions" menu or the context-sensitive pop-up menus. In the EVMS CLI, this is done using the **set** command.
