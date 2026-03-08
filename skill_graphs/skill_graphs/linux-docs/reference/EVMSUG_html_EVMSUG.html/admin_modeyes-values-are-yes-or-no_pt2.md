  2. Select the volume you want to mount.
  3. In the Mount Point box, enter the directory on which you want to mount the volume.
  4. Click Options if you want to enter additional options for the mount.
  5. Click Mount.


Alternatively, you can mount a volume from the EVMS GUI context sensitive menu:
  1. Right click the volume you want to mount.
  2. Click Mount...
  3. In the Mount Point box, enter the directory on which you want to mount the volume.
  4. Click Options if you want to enter additional options for the mount.
  5. Click Mount.


* * *
##  19.1.2. Using Ncurses
Follow these steps to mount a volume with Ncurses:
  1. Select Actions->File System->Mount....
  2. Select the volume you want to mount.
  3. At the Mount Point prompt, enter the directory on which you want to mount the volume and press **Enter**.
  4. Select Mount Options if you want to enter additional options for the mount.
  5. Select Mount.


Alternatively, you can mount a volume with the Ncurses context-sensitive menu:
  1. Highlight the volume you want to mount and press **Enter**.
  2. Select Mount File System.
  3. At the Mount Point prompt, enter the directory on which you want to mount the volume and press **Enter**.
  4. Select Mount Options if you want to enter additional options for the mount.
  5. Select Mount.


* * *
##  19.1.3. Using the CLI
To mount a volume with the CLI, use the following command:
```
mount:<volume>, <mount point>, [ <mount options> ]
```

---
<volume> is the name of the volume to be mounted.
<mount point> is the name of the directory on which to mount the volume.
<mount options> is a string of options to be passed to the <command>mount</command> command.
* * *
#  19.2. Unmounting a volume
This section tells how to unmount a volume through the various EVMS user interfaces.
* * *
##  19.2.1. Using the EVMS GUI
Follow these steps to unmount a volume with the EVMS GUI:
  1. Select Actions->File System->Unmount.
  2. Select the volume you want to unmount.
  3. Click Unmount.


Alternatively, you can unmount a volume from the EVMS GUI context sensitive menu:
  1. Right click the volume you want to unmount.
  2. Click Unmount...
  3. Click Unmount.


* * *
##  19.2.2. Using Ncurses
Follow these steps to unmount a volume with Ncurses:
  1. Select Actions->File System->Unmount....
  2. Select the volume you want to unmount.
  3. Select Unmount.


Alternatively, you can unmount a volume with the Ncurses context-sensitive menu:
  1. Highlight the volume you want to unmount and press **Enter**.
  2. Select Unmount File System.....
  3. Select Unmount.


* * *
##  19.2.3. Using the CLI
To unmount a volume with the CLI, use the following command:
```
unmount:<volume>
```

---
<volume> is the name of the volume to be unmounted.
* * *
#  19.3. The SWAPFS file system
A volume with the SWAPFS file system is not mounted or unmounted. Rather, swapping is turned on for the volume using the **sbin/swapon** command and turned off using the <command>sbin/swapoff</command>. EVMS lets you turn swapping on or off for a volume from within EVMS without having to go to a separate terminal session.
As with mounting and unmounting, EVMS performs the swapon and swapoff operations immediately. It does not wait until the changes are saved.
* * *
##  19.3.1. Turning swap on
This section tells how to turn swap on using the various EVMS user interfaces.
* * *
###  19.3.1.1. Using the EVMS GUI
Follow these steps to turn swap on with the EVMS GUI:
  1. Select Actions->Other->Volume tasks....
  2. Select the volume you want to turn on swapping and click Next.
  3. Select "Swap on" and click Next.
  4. Select the priority for the swap. If you select "High" you will get an additional prompt for the priority level. The priority level must be a number in the range of 0 to 32767. The default is 0.
  5. Click Swap on.


Alternatively, you can turn swap on from the EVMS GUI context-sensitive menu:
  1. Right click the volume with the SWAPFS you want to turn on.
  2. Click Swap on...
  3. Select the priority for the swap. If you select "High" you will get an additional prompt for the priority level. The priority level must be a number in the range of 0 to 32767. The default is 0.
  4. Click Swap on.


* * *
###  19.3.1.2. Using Ncurses
Follow these steps to turn swap on with Ncurses:
  1. Select Actions->Other->Volume tasks....
  2. Select the volume on which you want to turn on swapping and select Next.
  3. Select "Swap on" and select Next.
  4. Select the priority for the swap. If you select "High" you will get an additional prompt for the priority level. The priority level must be a number in the range of 0 to 32767. The default is 0.
  5. Select "Swap on."


Alternatively, you can turn swap on with the Ncurses context-sensitive menu:
  1. Highlight the volume with the SWAPFS you want to turn on.
  2. Select "Swap on...."
  3. Select the priority for the swap. If you select "High" you will get an additional prompt for the priority level. The priority level must be a number in the range of 0 to 32767. The default is 0.
  4. Select "Swap on."


* * *
###  19.3.1.3. Using the CLI
To turn swap on with the CLI, use the following command:
```

Task: swapon, <volume>[, priority=low | , priority=high [level=0..32767]]

```

---
<volume> is the name of the volume with SWAPFS you want to turn on.
* * *
##  19.3.2. Turning swap off
This section tells how to turn swap off using the various EVMS user interfaces.
* * *
###  19.3.2.1. Using the EVMS GUI
Follow these steps to turn swap off with the EVMS GUI:
  1. Select Actions->Other->Volume tasks....
  2. Select the volume you want to turn off swapping and click Next.
  3. Select "Swap off" and click Next.
  4. Click Swap off.


Alternatively, you can turn swap off from the EVMS GUI context-sensitive menu:
  1. Right click the volume with the SWAPFS you want to turn off.
  2. Click Swap off...
  3. Click Swap off.


* * *
###  19.3.2.2. Using Ncurses
Follow these steps to turn swap off with Ncurses:
  1. Select Actions->Other->Volume tasks....
  2. Select the volume on which you want to turn off swapping and select Next.
  3. Select "Swap off" and select Next.
  4. Select "Swap off."


Alternatively, you can turn swap on with the Ncurses context-sensitive menu:
  1. Highlight the volume with the SWAPFS you want to turn off.
  2. Select "Swap off...."
  3. Select "Swap off."


* * *
###  19.3.2.3. Using the CLI
To turn swap on with the CLI, use the following command:
```

Task: swapoff, <volume>

```

---
<volume> is the name of the volume with SWAPFS you want to turn off.
* * *
#  Chapter 20. Plug-in operations tasks
This chapter discusses plug-in operations tasks and shows how to complete a plug-in task with the EVMS GUI, Ncurses, and CLI interfaces.
* * *
#  20.1. What are plug-in tasks?
Plug-in tasks are functions that are available only within the context of a particular plug-in. These functions are not common to all plug-ins. For example, tasks to add spare disks to a RAID array make sense only in the context of the MD plug-in, and tasks to reset a snapshot make sense only in the context of the Snapshot plug-in.
* * *
#  20.2. Example: complete a plug-in operations task
This section shows how to complete a plug-in operations task with the EVMS GUI, Ncurses, and CLI interfaces.
> **Example 20-1. Add a spare disk to a compatibility volume made from an MDRaid5 region**
> This example adds disk `sde` as a spare disk onto volume `/dev/evms/md/md0`, which is a compatibility volume that was created from an MDRaid5 region.
* * *
##  20.2.1. Using the EVMS GUI
Follow these steps to add `sde` to `/dev/evms/md/md0` with the EVMS GUI:
  1. Select Other->Storage Object Tasks...
  2. Select md/md0.
  3. Click Next.
  4. Select Add spare object.
  5. Click Next.
  6. Select sde.
  7. Click Add.
  8. The operation is completed when you save.


Alternatively, you could use context-sensitive menus to complete the task, as follows:
  1. View the region `md/md0`. You can view the region either by clicking on the small plus sign beside the volume name (`/dev/evms/md/md0`) on the volumes tab, or by selecting the regions tab.
  2. Right click the region (`md/md0`). A list of acceptable Actions and Navigational shortcuts displays. The last items on the list are the tasks that are acceptable at this time.
  3. Point to Add spare object and left click.
  4. Select sde.
  5. Click Add.


* * *
##  20.2.2. Using Ncurses
Follow these steps to add `sde` to `/dev/evms/md/md0` with Ncurses:
  1. Select Other->Storage Object Tasks
  2. Select md/md0.
  3. Activate Next.
  4. Select Add spare object.
  5. Activate Next.
  6. Select sde.
  7. Activate Add.


Alternatively, you can use the context sensitive menu to complete the task:
  1. From the Regions view, press **Enter** on md/md0.
  2. Activate the Add spare object menu item.
  3. Select sde.
  4. Activate Add.


* * *
##  20.2.3. Using the CLI
With the EVMS CLI, all plug-in tasks must be accomplished with the **task** command. Follow these steps to add `sde` to `/dev/evms/md/md0` with the CLI:
  1. The following query command with the list options filter to determines the acceptable tasks for a particular object and the name-value pairs it supports. The command returns information about which plug-in tasks are available at the current time and provides the information necessary for you to complete the command.
```
query: objects, object=md/md0, list options
```

---
  2. The command takes the name of the task (returned from the previous query), the object to operate on (in this case, md/md0), any required options (none in this case) and, if necessary, another object to be manipulated (in our example, `sde`, which is the spare disk we want to add):
```
task: addspare, md/md0, sde
```

---
The command is completed upon saving.


* * *
#  Chapter 21. Deleting objects
This chapter tells how to delete EVMS objects through the delete and delete recursive operations.
* * *
#  21.1. How to delete objects: delete and delete recursive
There are two ways in EVMS that you can destroy objects that you no longer want: Delete and Delete Recursive. The Delete option destroys only the specific object you specify. The Delete Recursive option destroys the object you specify and its underlying objects, down to the container, if one exists, or else down to the disk. In order for a volume to be deleted, it must not be mounted. EVMS verifies that the volume you are attempting to delete is not mounted and does not perform the deletion if the volume is mounted.
* * *
#  21.2. Example: perform a delete recursive operation
The following example shows how to destroy a volume and the objects below it with the EVMS GUI, Ncurses, and CLI interfaces.
> **Example 21-1. Destroy a volume and the region and container below it**
> This example uses the delete recursive operation to destroy volume `/dev/evms/Sample Volume` and the region and container below it. Volume `/dev/evms/Sample Volume` is the volume that was created in earlier. Although we could also use the delete option on each of the objects, the delete recursive option takes fewer steps. Note that because we intend to delete the container as well as the volume, the operation needs to be performed in two steps: one to delete the volume and its contents, and one to delete the container and its contents.
* * *
##  21.2.1. Using the EVMS GUI
Follow these steps to delete the volume and the container with the EVMS GUI:
  1. Select Actions->Delete->Volume.
  2. Select volume /dev/evms/Sample Volume from the list.
  3. Click Recursive Delete. This step deletes the volume and the region `lvm/Sample Container/Sample Region`. If you want to keep the underlying pieces or want to delete each piece separately, you would click Delete instead of Delete Recursive.
  4. Assuming you chose Delete Recursive (if not, delete the region before continuing with these steps), select Actions->Delete->Container.
  5. Select container lvm/Sample Container from the list.
  6. Click Recursive Delete to destroy the container and anything under it. Alternatively, click Delete to destroy only the container (if you built the container on disks as in the example, either command has the same effect).


Alternatively, you can perform some of the volume deletion steps with the GUI context sensitive menu:
  1. From the Volumes tab, right click `/dev/evms/Sample Volume`.
  2. Click Delete...
  3. Continue with the operation beginning with step 3 of the GUI instructions.


* * *
##  21.2.2. Using Ncurses
Follow these steps to delete the volume and the container with Ncurses:
  1. Select Actions->Delete->Volume.
  2. Select volume /dev/evms/Sample Volume from the list.
  3. Activate Delete Volume Recursively. This step deletes the volume and the region `lvm/Sample Container/Sample Region`. If you want to keep the underlying pieces or want to delete each piece separately, activate Delete instead of Delete Recursive.
  4. Assuming you chose Delete Volume Recursively (if not, delete the region before continuing with these steps), select Actions->Delete->Container.
  5. Select container lvm/Sample Container from the list.
  6. Click Recursive Delete to destroy the container and everything under it. Alternatively, activate Delete to delete only the container (if you built the container on disks as in the example, either command has the same effect).
  7. Press **Enter**.


Alternatively, you can perform some of the volume deletion steps with the context sensitive menu:
  1. From the Volumes view, press **Enter** on /dev/evms/Sample Volume.
  2. Activate Delete.
  3. Continue with the operation beginning with step 3 of the Ncurses instructions.


* * *
##  21.2.3. Using the CLI
Use the **delete** and **delete recursive** commands to destroy EVMS objects. Specify the command name followed by a colon, and then specify the volume, object, or container name. For example:
  1. Enter this command to perform the delete recursive operation:
```
delete recursive: "/dev/evms/Sample Volume"
```

---
This step deletes the volume and the region `/lvm/Sample Container/Sample Region`. If you wanted to keep the underlying pieces or wanted to delete each piece separately, use the **delete** command, as follows:
```
delete: "/dev/evms/Sample Volume"
```

---
  2. Assuming you chose Delete Volume Recursively (if not, delete the region before continuing with these steps) enter the following to destroy the container and everything under it:
```
delete recursive: "lvm/Sample Container"
```

---
To destroy only the container, enter the following:
```
delete: "lvm/Sample Container"
```

---


* * *
#  Chapter 22. Replacing objects
This chapter discusses how to replace objects.
* * *
#  22.1. What is object-replace?
Occasionally, you might wish to change the configuration of a volume or storage object. For instance, you might wish to replace one of the disks in a drive-link or RAID-0 object with a newer, faster disk. As another example, you might have an EVMS volume created from a simple disk segment, and want to switch that segment for a RAID-1 region to provide extra data redundancy. Object-replace accomplishes such tasks.
Object-replace gives you the ability to swap one object for another object. The new object is added while the original object is still in place. The data is then copied from the original object to the new object. When this is complete, the original object is removed. This process can be performed while the volume is mounted and in use.
* * *
#  22.2. Replacing a drive-link child object
For this example, we will start with a drive-link object named `link1`, which is composed of two disk segments named sda1 and sdb1. The goal is to replace sdb1 with another segment named sdc1.
![Note](https://tldp.org/LDP/EVMSUG/images/note.gif) | **Note**
---|---
| The drive-linking plug-in allows the target object (sdc1 in this example) to be the same size or larger than the source object. If the target is larger, the extra space will be unused. Other plug-ins have different restrictions and might require that both objects be the same size.
* * *
##  22.2.1. Using the EVMS GUI or Ncurses
Follow these steps to replace sdb1 with sdc1:
  1. Select Actions->Replace.
  2. In the "Replace Source Object" panel select sdb1.
  3. Activate Next.
  4. In the "Select Replace Target Object" panel, select sdc1.
  5. Activate Replace.


Alternatively, you can perform these same steps with the context sensitive menus:
  1. From the "Disk Segments" panel, right click (or Press **Enter** on) the object sdb1.
  2. Choose Replace on the popup menu.
  3. In the "Select Replace Target Object" panel, select sdc1.
  4. Activate Replace.


When you save changes, EVMS begins to copy the data from sdb1 to sdc1. The status bar at the bottom of the UI will reflect the percent-complete of the copy operation. The UI must remain open until the copy is finished. At that time, the object sdb1 will be moved to the "Available Objects" panel.
* * *
##  22.2.2. Using the CLI
Use the **Replace** to replace objects with the CLI:
```

Replace:source_object_name, target_object_name

```

---
"source_object_name" is the name of the object you wish to replace with "target_object_name." In the following example, sdb1 is replaced with sdc1.
```

Replace:sdb1,sdc1

```

---
* * *
#  Chapter 23. Moving segment storage objects
This chapter discusses how and why to move segments.
* * *
#  23.1. What is segment moving?
A segment move is when a data segment is relocated to another location on the underlying storage object. The new location of the segment cannot overlap with the current segment location.
* * *
#  23.2. Why move a segment?
Segments are moved for a variety of reasons. The most compelling among them is to make better use of disk freespace. Disk freespace is an unused contiguous extent of sectors on a disk that has been identified by EVMS as a freespace segment. A data segment can only be expanded by adding sectors to the end of the segment, moving the end of the data segment up into the freespace that immediately follows the data segment. However, what if there is no freespace following the data segment? A segment or segments could be be moved around to put freespace after the segment that is to be expanded. For example:
  * The segment following the segment to be expanded can be moved elsewhere on the disk, thus freeing up space after the segment that is to be expanded.
  * The segment to be expanded can be moved into freespace where there is more room for the segment to be expanded.
  * The segment can be moved into freespace that precedes the segment so that after the move the data segment can be expanded into the freespace created by the move.


* * *
#  23.3. Which segment manager plug-ins implement the move function?
The following segment manager plug-ins support the move function:
  * DOS
  * s390
  * GPT


* * *
#  23.4. Example: move a DOS segment
This section shows how to move a DOS segment:
![Note](https://tldp.org/LDP/EVMSUG/images/note.gif) | **Note**
---|---
|  In the following example, the DOS segment manager has a single primary partition on disk sda that is located at the very end of the disk. We want to move it to the front of the drive because we want to expand the segment but there is currently no freespace following the segment.
* * *
##  23.4.1. Using the EVMS GUI context sensitive menu
To move the DOS segment through the GUI context sensitive menu, follow these steps:
  1. From the Segments tab, right click `sda1`.
  2. Click Move.
  3. Select `sda_freespace1`.
  4. Click Move.


* * *
##  23.4.2. Using Ncurses
To move the DOS segment, follow these steps:
  1. Use **Tab** to select the Disk Segments view.
  2. Scroll down with the down arrow and select `sda1`.
  3. Press **Enter**.
  4. Scroll down with the down arrow and select Move by pressing **Enter**.
  5. Use the spacebar to select `sda_freespace1`.
  6. Use **Tab** to select Move and press **Enter**.


* * *
##  23.4.3. Using the CLI
Use the **task** command to move a DOS segment with the CLI.
```
task:Move,sda1,sda_freespace1
```

---
* * *
#  Appendix A. The DOS plug-in
The DOS plug-in is the most commonly used EVMS segment manager plug-in. The DOS plug-in supports DOS disk partitioning as well as:
  * OS/2 partitions that require extra metadata sectors.
  * Embedded partition tables: SolarisX86, BSD, and UnixWare.


The DOS plug-in reads metadata and constructs segment storage objects that provide mappings to disk partitions.
* * *
#  A.1. How the DOS plug-in is implemented
The DOS plug-in provides compatibility with DOS partition tables. The plug-in produces EVMS segment storage objects that map primary partitions described by the MBR partition table and logical partitions described by EBR partition tables.
DOS partitions have names that are constructed from two pieces of information:
  * The device they are found on.
  * The partition table entry that provided the information.


Take, for example, partition name `hda1`, which describes a partition that is found on device `had` in the MBR partition table. DOS partition tables can hold four entries. Partition numbers 1-4 refer to MBR partition records. Therefore, our example is telling us that partition `hda1` is described by the very first partition record entry in the MBR partition table. Logical partitions, however, are different than primary partitions. EBR partition tables are scattered across a disk but are linked together in a chain that is first located using an extended partition record found in the MBR partition table. Each EBR partition table contains a partition record that describes a logical partition on the disk. The name of the logical partition reflects its position in the EBR chain. Because the MBR partition table reserves numerical names 1-4, the very first logical partition is always named 5. The next logical partition, found by following the EBR chain, is called 6, and so forth. So, the partition `hda5` is a logical partition that is described by a partition record in the very first EBR partition table.
While discovering DOS partitions, the DOS plug-in also looks for OS/2 DLAT metadata to further determine if the disk is an OS/2 disk. An OS/2 disk has additional metadata and the metadata is validated during recovery. This information is important for the DOS plug-in to know because an OS/2 disk must maintain additional partition information. (This is why the DOS plug-in asks, when being assigned to a disk, if the disk is a Linux disk or an OS/2 disk.) The DOS plug-in needs to know how much information must be kept on the disk and what kind of questions it should ask the user when obtaining the information.
An OS/2 disk can contain compatibility volumes as well as logical volumes. A compatibility volume is a single partition with an assigned drive letter that can be mounted. An OS/2 logical volume is a drive link of 1 or more partitions that have software bad-block relocation at the partition level.
Embedded partitions, like those found on a SolarisX86 disk or a BSD compatibility disk, are found within a primary partition. Therefore, the DOS plug-in inspects primary partitions that it has just discovered to further determine if any embedded partitions exist. Primary partitions that hold embedded partition tables have partition type fields that indicate this. For example, a primary partition of type 0xA9 probably has a BSD partition table that subdivides the primary partition into BSD partitions. The DOS plug-in looks for a BSD disk label and BSD data partitions in the primary partition. If the DOS plug-in finds a BSD disk label, it exports the BSD partitions. Because this primary partition is actually just a container that holds the BSD partitions, and not a data partition itself, it is not exported by the DOS plug-in. Embedded partitions are named after the primary partition they were discovered within. As an example, `hda3.1` is the name of the first embedded partition found within primary partition `hda3`.
* * *
#  A.2. Assigning the DOS plug-in
Assigning a segment manager to a disk means that you want the plug-in to manage partitions on the disk. In order to assign a segment manager to a disk, the plug-in needs to create and maintain the appropriate metadata, which is accomplished through the "disk type" option. When you specify the "disk type" option and choose Linux or OS/2, the plug-in knows what sort of metadata it needs to keep and what sort of questions it should ask when creating partitions.
An additional OS/2 option is the "disk name" option, by which you can provide a name for the disk that will be saved in OS/2 metadata and that will be persistent across reboots.
* * *
#  A.3. Creating DOS partitions
There are two basic DOS partition types:
  1. A primary partition, which is described by a partition record in the MBR partition table.
  2. A logical partition, which is described by a partition record in the EBR partition table.


Every partition table has room for four partition records; however, there are a few rules that impose limits on this.
An MBR partition table can hold four primary partition records unless you also have logical partitions. In this case, one partition record is used to describe an extended partition and the start of the EBR chain that in turn describes logical partitions.
Because all logical partitions must reside in the extended partition, you cannot allocate room for a primary partition within the extended partition and you cannot allocate room for a logical partition outside or adjacent to this area.
