snapshot, given sufficient activity on the original. In this situation, the
snapshot is deactivated and additional I/O to the snapshot fails.

Base the size of the snapshot object on the amount of activity that is likely
to take place on the original during the lifetime of the snapshot. The more
changes that occur on the original and the longer the snapshot is expected to
remain active, the larger the snapshot object should be. Clearly, determining
this calculation is not simple and requires trial and error to determine the
correct snapshot object size to use for a particular situation. The goal is
to create a snapshot object large enough to prevent the snapshot from being
deactivated if it fills up, yet small enough to not waste disk space. If the
snapshot object is the same size as the original volume, or a little larger,
to account for the snapshot mapping tables, the snapshot is never
deactivated.

After you've created the snapshot object and saved the changes, the snapshot
will be activated (as long as the snapshot child object is already active).
This is a change from snapshots in EVMS 2.3.x and earlier, where the snapshot
would not be activated until the object was made into an EVMS volume. If you
wish to have an inactive snapshot, please add the name of the snapshot object
to the "activate.exclude" line in the EVMS configuration file (see section
about selective-activation for more details). If at any point you decide to
deactivate a snapshot object while the original volume is still active, the
snapshot will be reset. The next time that the snapshot object is activated,
it will reflect the state of the original volume at that point in time, just
as if the snapshot had just been created.

In order to mount the snapshot, the snapshot object must still be made into
an EVMS volume. The name of this volume can be the same as or different than
the name of the snapshot object.
-----------------------------------------------------------------------------

11.3. Example: create a snapshot

This section shows how to create a snapshot with EVMS:



    Example 11-1. Create a snapshot of a volume

    Create a new snapshot of /dev/evms/vol on lvm/Sample Container/Sample
    Region, and call it "snap."

-----------------------------------------------------------------------------
11.3.1. Using the EVMS GUI

To create the snapshot using the GUI, follow these steps:

 1. Select Actions->Create->Feature Object to see a list of EVMS feature
    objects.

 2. Select Snapshot Feature.

 3. Click Next.

 4. Select lvm/Sample Container/Sample Region.

 5. Click Next.

 6. Select /dev/evms/vol from the list in the "Volume to be Snapshotted"
    field.

 7. Type snap in the "Snapshot Object Name" field.

 8. Click Create.


Alternatively, you can perform some of the steps to create a snapshot with
the GUI context sensitive menu:

 1. From the Available Objects tab, right click lvm/Sample Container/Sample
    Region.

 2. Click Create Feature Object...

 3. Continue creating the snapshot beginning with step 2 of the GUI
    instructions. You can skip steps 4 and 5 of the GUI instructions.


-----------------------------------------------------------------------------
11.3.2. Using Ncurses

To create the snapshot, follow these steps:

 1. Select Actions->Create->Feature Object to see a list of EVMS feature
    objects.

 2. Select Snapshot Feature.

 3. Activate Next.

 4. Select lvm/Sample Container/Sample Region.

 5. Activate Next.

 6. Press spacebar to edit the "Volume to be Snapshotted" field.

 7. Highlight /dev/evms/vol and press spacebar to select.

 8. Activate OK.

 9. Highlight "Snapshot Object Name" and press spacebar to edit.

10. Type snap at the "::" prompt. Press Enter.

11. Activate Create.


Alternatively, you can perform some of the steps to create a snapshot with
the context sensitive menu:

 1. From the Available Objects view, press Enter on lvm/Sample Container/
    Sample Region.

 2. Activate the Create Feature Object menu item.

 3. Continue creating the snapshot beginning with step 6 of the Ncurses
    instructions.


-----------------------------------------------------------------------------
11.3.3. Using the CLI

Use the create command to create a snapshot through the CLI. You pass the
"Object" keyword to the create command, followed by the plug-in and its
options, and finally the objects.

To determine the options for the plug-in you are going to use, issue the
following command:
query: plugins, plugin=Snapshot, list options

Now construct the create command, as follows:
create: object, Snapshot={original=/dev/evms/vol, snapshot=snap},
"lvm/Sample Container/Sample Region"
-----------------------------------------------------------------------------

11.4. Reinitializing a snapshot

Snapshots can be reinitialized. Reinitializing causes all of the saved data
to be erased and starts the snapshot from the current point in time. A
reinitialized snapshot has the same original, chunk size, and writeable flags
as the original snapshot.

To reinitialize a snapshot, use the Reset command on the snapshot object (not
the snapshot volume). This command reinitializes the snapshot without
requiring you to manually deactivate and reactivate the volume. The snapshot
must be active but unmounted for it to be reinitialized.

This section continues the example from the previous section, where a
snapshot object and volume were created. The snapshot object is called "snap"
and the volume is called "/dev/evms/snap."
-----------------------------------------------------------------------------

11.4.1. Using the EVMS GUI or Ncurses

To reinitialize a snapshot, follow these steps:

 1. Select Actions->Other->Storage Object Tasks

 2. Select the volume "snap."

 3. Click or activate Next.

 4. Select Reset.

 5. Click or activate Next.

 6. Click or activate Reset on the action panel.

 7. Click or activate Reset on the warning panel.


Alternatively, you can perform these same steps with the context sensitive
menus:

 1. From the Feature Objects panel, right click (or press Enter on) the
    object snap.

 2. Click or activate Reset on the popup menu.

 3. Click or activate Reset on the action panel.

 4. Click or activate Reset on the warning panel.


-----------------------------------------------------------------------------
11.4.2. Using the CLI

Follow these steps to reinitialize a snapshot with the CLI:

 1. Issue the following command to the CLI:
    task:reset,snap

 2. Press Enter to select "Reset" (the default choice) at the warning
    message.


-----------------------------------------------------------------------------
11.5. Expanding a snapshot

 As mentioned in Section 11.2, as data is copied from the original volume to
the snapshot, the space available for the snapshot might fill up, causing the
snapshot to be invalidated. This situation might cause your data backup to
end prematurely, as the snapshot volume begins returning I/O errors after it
is invalidated.

 To solve this problem, EVMS now has the ability to expand the storage space
for a snapshot object while the snapshot volume is active and mounted. This
feature allows you to initially create a small snapshot object and expand the
object as necessary as the space begins to fill up.

 In order to expand the snapshot object, the underlying object must be
expandable. Continuing the example from the previous sections, the object
"snap" is built on the LVM region lvm/Sample Container/Sample Region. When we
refer to expanding the "snap" object, the region lvm/Sample Container/Sample
Region is the object that actually gets expanded, and the object "snap"
simply makes use of the new space on that region. Thus, to have expandable
snapshots, you will usually want to build your snapshot objects on top of LVM
regions that have extra freespace available in their LVM container. DriveLink
objects and some disk segments also work in certain situations.

 One notable quirk about expanding snapshots is that the snapshot object and
volume do not actually appear to expand after the operation is complete.
Because the snapshot volume is supposed to be a frozen image of the original
volume, the snapshot volume always has the same size as the original, even if
the snapshot has been expanded. However, you can verify that the snapshot
object is using the additional space by displaying the details for the
snapshot object and comparing the percent-full field before and after the
expand operation.
-----------------------------------------------------------------------------

11.5.1. Using the EVMS GUI or Ncurses

To create the snapshot using the GUI or Ncurses, follow these steps:

 1. Select Actions->Expand->Volume to see a list of EVMS feature objects.

 2. Select the volume /dev/evms/snap.

 3. Click or activate Next.

 4. Select lvm/Sample Container/Sample Region. This object is the object that
    will actually be expanded.

 5. Click or activate Next.

 6. Select the options for expanding the LVM region, including the amount of
    extra space to add to the region.

 7. Click or activate Expand.


Alternatively, you can perform the same steps using the context sensitive
menus.

 1. From the Volumes panel, right click (or press Enter on) /dev/evms/snap.

 2. Select Expand from the popup menu.

 3. Click or activate Next.

 4. Select the region lvm/Sample Container/Sample Region. This is the object
    that will actually be expanded.

 5. Click or activate Next.

 6. Select the options for expanding the LVM region, including the amount of
    extra space to add to the region.

 7. Click or activate Expand.


-----------------------------------------------------------------------------
11.5.2. Using the CLI

The CLI expands volumes by targeting the object to be expanded. The CLI
automatically handles expanding the volume and other objects above the volume
in the volume stock. As with a regular expand operation, the options are
determined by the plug-in that owns the object being expanded.

Issue the following command to determine the expand options for the region
lvm/Sample Container/Sample Region:
query:region,region="lvm/Sample Container/Sample Region",lo

The option to use for expanding this region is called "add_size." Issue the
following command to expand the snapshot by 100 MB:
expand:"lvm/Sample Container/Sample Region", add_size=100MB
-----------------------------------------------------------------------------

11.6. Deleting a snapshot

When a snapshot is no longer needed, you can remove it by deleting the EVMS
volume from the snapshot object, and then deleting the snapshot object.
Because the snapshot saved the initial state of the original volume (and not
the changed state), the original is always up-to-date and does not need any
modifications when a snapshot is deleted.

No options are available for deleting snapshots.
-----------------------------------------------------------------------------

11.7. Rolling back a snapshot

Situations can arise where a user wants to restore the original volume to the
saved state of the snapshot. This action is called a rollback. One such
scenario is if the data on the original is lost or corrupted. Snapshot
rollback acts as a quick backup and restore mechanism, and allows the user to
avoid a more lengthy restore operation from tapes or other archives.

Another situation where rollback can be particularly useful is when you are
testing new software. Before you install a new software package, create a
writeable snapshot of the target volume. You can then install the software to
the snapshot volume, instead of to the original, and then test and verify the
new software on the snapshot. If the testing is successful, you can then roll
back the snapshot to the original and effectively install the software on the
regular system. If there is a problem during the testing, you can simply
delete the snapshot without harming the original volume.

You can perform a rollback when the following conditions are met:

��*� Both the snapshot and the original volumes are unmounted and otherwise
    not in use.

��*� There is only a single snapshot of an original.

     If an original has multiple snapshots, all but the desired snapshot must
    be deleted before rollback can take place.


No options are available for rolling back snapshots.
-----------------------------------------------------------------------------

11.7.1. Using the EVMS GUI or Ncurses

Follow these steps to roll back a snapshot with the EVMS GUI or Ncurses:

 1. Select Actions->Other->Storage Object Tasks+.+ +

 2. Select the object "snap."

 3. Click or activate Next.

 4. Select Rollback
    .
 5. Click or activate Next.

 6. Click or activate Rollback on the action panel.

 7. Click or activate Rollback on the warning panel.


Alternatively, you can perform these same steps with the context-sensitive
menus:

 1. From the Feature Objects panel, right click (or press Enter on) the
    object "snap."

 2. Click or activate Rollback on the popup menu.

 3. Click or activate Rollback on the action panel.

 4. Click or activate Rollback on the warning panel.


-----------------------------------------------------------------------------
11.7.2. Using the CLI

Follow these steps to roll back a snapshot with the CLI:

 1. Issue the following command to the CLI:
    task:rollback,snap

 2. Press Enter to select "Rollback" (the default choice) at the warning
    message.


-----------------------------------------------------------------------------
Chapter 12. Creating volumes

This chapter discusses when and how to create volumes.
-----------------------------------------------------------------------------

12.1. When to create a volume

EVMS treats volumes and storage objects separately. A storage object does not
automatically become a volume; it must be made into a volume.

Volumes are created from storage objects. Volumes are either EVMS native
volumes or compatibility volumes. Compatibility volumes are intended to be
compatible with a volume manager other than EVMS, such as the Linux LVM, MD,
OS/2 or AIX. Compatibility volumes might have restrictions on what EVMS can
do with them. EVMS native volumes have no such restrictions, but they can be
used only by an EVMS equipped system. Volumes are mountable and can contain
file systems.

EVMS native volumes contain EVMS-specific information to identify the volume
name. After this volume information is applied, the volume is no longer fully
backward compatible with existing volume types.

Instead of adding EVMS metadata to an existing object, you can tell EVMS to
make an object directly available as a volume. This type of volume is known
as a compatibility volume. Using this method, the final product is fully
backward-compatible with the desired system.
-----------------------------------------------------------------------------

12.2. Example: create an EVMS native volume

This section provides a detailed explanation of how to create an EVMS native
volume with EVMS by providing instructions to help you complete the following
task.



    Example 12-1. Create an EVMS native volume

    Create an EVMS native volume called "Sample Volume" from the region, /lvm
    /Sample Container/Region, you created in Chapter 9.

-----------------------------------------------------------------------------
12.2.1. Using the EVMS GUI

Follow these instructions to create an EVMS volume:

 1. Select Actions->Create->EVMS Volume.

 2. Choose lvm/Sample Container/Sample Region.

 3. Type Sample Volume in the name field.

 4. Click Create.


Alternatively, you can perform some of the steps to create an EVMS volume
from the GUI context sensitive menu:

 1. From the Available Options tab, right click lvm/Sample Container/Sample
    Region.

 2. Click Create EVMS Volume...

 3. Continue beginning with step 3 of the GUI instructions.


-----------------------------------------------------------------------------
12.2.2. Using Ncurses

To create a volume, follow these steps:

 1. Select Actions->Create->EVMS Volume.

 2. Enter Sample Volume at the "name" prompt. Press Enter.

 3. Activate Create.


Alternatively, you can perform some of the steps to create an EVMS volume
from the context sensitive menu:

 1. From the Available Objects view, press Enter on lvm/Sample Container/
    Sample Region.

 2. Activate the Create EVMS Volume menu item.

 3. Continue beginning with step 3 of the Ncurses instructions.


-----------------------------------------------------------------------------
12.2.3. Using the CLI

To create a volume, use the Create command. The arguments the Create command
accepts vary depending on what is being created. In the case of the example,
the first argument is the key word volume that specifies what is being
created. The second argument is the object being made into a volume, in this
case lvm/Sample Container/Sample Region. The third argument is type specific
for an EVMS volume, Name=, followed by what you want to call the volume, in
this case Sample Volume. The following command creates the volume from the
example.
Create: Volume, "lvm/Sample Container/Sample Region", Name="Sample Volume"
-----------------------------------------------------------------------------

12.3. Example: create a compatibility volume

This section provides a detailed explanation of how to create a compatibility
volume with EVMS by providing instructions to help you complete the following
task.



    Example 12-2. Create a compatibility volume

    Create a compatibility volume called "Sample Volume" from the region, /
    lvm/Sample Container/Region, you created in Chapter 9.

-----------------------------------------------------------------------------
12.3.1. Using the GUI

To create a compatibility volume, follow these steps:

 1. Select Actions->Create->Compatibility Volume.

 2. Choose the region lvm/Sample Container/Sample Region from the list.

 3. Click the Create button.

 4. Click the Volume tab in the GUI to see a volume named /dev/evms/lvm/
    Sample Container/Sample Region. This volume is your compatibility volume.


Alternatively, you can perform some of the steps to create a compatibility
volume from the GUI context sensitive menu:

 1. From the Available Objects tab, right click lvm/Sample Container/Sample
    Region.

 2. Click Create Compatibility Volume...

 3. Continue beginning with step 3 of the GUI instructions.


-----------------------------------------------------------------------------
12.3.2. Using Ncurses

To create a compatibility volume, follow these steps:

 1. Select Actions->Create->Compatibility Volume.

 2. Choose the region lvm/Sample Container/Storage Region from the list..

 3. Activate Create.


Alternatively, you can perform some of the steps to create a compatibility
volume from the context sensitive menu:

 1. From the Available Objects view, press Enter on lvm/Sample Container/
    Sample Region.

 2. Activate the Create Compatibility Volume menu item.

 3. Continue beginning with step 3 of the Ncurses instructions.


-----------------------------------------------------------------------------
12.3.3. Using the CLI

To create a volume, use the Create command. The arguments the Create command
accepts vary depending on what is being created. In the case of the example,
the first argument is the key word volume that specifies what is being
created. The second argument is the object being made into a volume, in this
case lvm/Sample Container/Sample Region. The third argument, compatibility,
indicates that this is a compatibility volume and should be named as such.
Create:Volume,"lvm/Sample Container/Sample Region",compatibility
-----------------------------------------------------------------------------

Chapter 13. FSIMs and file system operations

This chapter discusses the seven File System Interface Modules (FSIMs)
shipped with EVMS, and then provides examples of adding file systems and
coordinating file system checks with the FSIMs.
-----------------------------------------------------------------------------

13.1. The FSIMs supported by EVMS

EVMS currently ships with seven FSIMs. These file system modules allow EVMS
to interact with file system utilities such as mkfs and fsck. Additionally,
the FSIMs ensure that EVMS safely performs operations, such as expanding and
shrinking file systems, by coordinating these actions with the file system.

You can invoke operations such as mkfs and fsck through the various EVMS user
interfaces. Any actions you initiate through an FSIM are not saved to disk
until the changes are saved in the user interface. Later in this chapter we
provide examples of creating a new file system and coordinating file system
checks through the EVMS GUI, Ncurses, and command-line interfaces.

The FSIMs supported by EVMS are:

��*�JFS

��*�XFS

��*�ReiserFS

��*�Ext2/3

��*�SWAPFS

��*�OpenGFS

��*�NTFS


-----------------------------------------------------------------------------
13.1.1. JFS

 The JFS module supports the IBM journaling file system (JFS). Current
support includes mkfs, unmkfs, fsck, and online file system expansion. You
must have at least version 1.0.9 of the JFS utilities for your system to work
with this EVMS FSIM. You can download the latest utilities from the [http://
oss.software.ibm.com/jfs] JFS for Linux site.

 For more information on the JFS FSIM, refer to Appendix F.
-----------------------------------------------------------------------------

13.1.2. XFS

 The XFS FSIM supports the XFS file system from SGI. Command support includes
mkfs, unmkfs, fsck, and online expansion. Use version 1.2 or higher, which
you can download from [ftp://oss.sgi.com/projects/xfs/download] the SGI open
source FTP directory.

 For more information on the XFS FSIM, refer to Appendix G.
-----------------------------------------------------------------------------

13.1.3. ReiserFS

 The ReiserFS module supports the ReiserFS journaling file system. This
module supports mkfs, unmkfs, fsck, online and offline expansion and offline
shrinkage. You need version 3.x.1a or higher of the ReiserFS utilities for
use with the EVMS FSIM modules. You can download the ReiserFS utilities from
The Naming System Venture (Namesys) Web site.

 For more information on the ReiserFS FSIM, refer to Appendix H.
-----------------------------------------------------------------------------

13.1.4. Ext2/3

 The EXT2/EXT3 FSIM supports both the ext2 and ext3 file system formats. The
FSIM supports mkfs, unmkfs, fsck, and offline shrinkage and expansion.

 For more information on the Ext2/3 FSIM, refer to Appendix I.
-----------------------------------------------------------------------------

13.1.5. SWAPFS

 The SWAPFS FSIM supports Linux swap devices. The FSIM lets you create and
delete swap devices, and supports mkfs, unmkfs, shrinkage and expansion.
Currently, you are responsible for issuing the swapon and swapoff commands
either in the startup scripts or manually. You can resize swap device with
the SWAPFS FSIM as long as the device is not in use.
-----------------------------------------------------------------------------

13.1.6. OpenGFS

 The OpenGFS module supports the OpenGFS clustered journaling file system.
This module supports mkfs, unmkfs, fsck, and online expansion. You need the
OpenGFS utilities for use with the EVMS FSIM module. You can download the
OpenGFS utilities from the [http://sourceforge.net/projects/opengfs] OpenGFS
project on SourceForge.

 For more information on the OpenGFS FSIM, refer to Appendix J.
-----------------------------------------------------------------------------

13.1.7. NTFS

 The NTFS FSIM supports the NTFS file system format. The FSIM supports mkfs,
unmkfs, and offline shrinkage and expansion. It also has support for running
the ntfsfix and netfsclone from the ntfsprogs utilities. You can download the
ntfsprogs utilities from the [http://linux-ntfs.sourceforge.net/] Linux NTFS
project web site.

 For more information on the NTFS FSIM, refer to Appendix K.
-----------------------------------------------------------------------------

13.2. Example: add a file system to a volume

After you have made an EVMS or compatibility volume, add a file system to the
volume before mounting it. You can add a file system to a volume through the
EVMS interface of your choice.



    Example 13-1. Add a JFS File System to a Volume

    This example creates a new JFS file system, named jfs_vol, on volume /dev
    /evms/my_vol.

-----------------------------------------------------------------------------
13.2.1. Using the EVMS GUI

Follow these steps to create a JFS file system with the EVMS GUI:

 1. Select Actions->File Systems->Make.

 2. Select JFS File System Interface Module.

 3. Click Next.

 4. Select /dev/evms/my_vol.

 5. Click Next.

 6. Type jfs_vol in the "Volume Label" field. Customize any other options you
