-----------------------------------------------------------------------------

18.2.2.1. Using the EVMS GUI

To deactivate a volume or object with the GUI, follow these steps:

 1. Select Actions->Activation->Deactivate...

 2. Select the volume(s) and object(s) you want to deactivate.

 3.  Click Deactivate.

 4. Click Save to save the changes and activate the volume(s) and object(s).


-----------------------------------------------------------------------------
18.2.2.2. Using the EVMS GUI context-sensitive menu

To deactivate a volume or object with the GUI context-sensitive menu, follow
these steps:

 1.  Right click the volume or object you want to deactivate.

 2.  Click "Deactivate."

 3.  Click Deactivate.

 4. Click Save to save the changes and activate the volume(s) and object(s).


-----------------------------------------------------------------------------
18.2.2.3. Using Ncurses

To deactivate a volume or object with Ncurses, follow these steps:

 1. Select Actions->Activation->Deactivate...

 2. Select the volume(s) and object(s) you want to deactivate.

 3.  Select Deactivate.

 4. Select Actions->Save to save the changes and deactivate the volume(s) and
    object(s).


-----------------------------------------------------------------------------
18.2.2.4. Using the Ncurses context-sensitive menu

To deactivate a volume or object with the Ncurses context-sensitive menu,
follow these steps:

 1.  Highlight the volume or object you want to deactivate and press Enter.

 2.  Select "Deactivate."

 3.  Select Deactivate.

 4. Select Actions->Save to save the changes and deactivate the volume(s) and
    object(s).


-----------------------------------------------------------------------------
18.2.2.5. Using the CLI

To deactivate a volume or object with the CLI, issue the following command to
the CLI (where "name" is the name of the volume or object you want to
deactivate):
Deactivate:name
-----------------------------------------------------------------------------

18.2.3. Activation and deactivation dependencies

 In order for a volume or object to be active, all of its children must be
active. When you activate a volume or object, EVMS will activate all the
objects that the volume or object comprises.

 Similarly, in order for an object to be inactive, all of its parents cannot
be activate. When you deactivate an object, EVMS will deactivate all of the
objects and volumes that are built from that object.
-----------------------------------------------------------------------------

18.2.3.1. Dependencies during initial activation

 As discussed in Section 18.1, when EVMS starts, it builds an initial list of
volumes and objects whose names match the "include" entry in the activation
section of /etc/evms.conf. Because those volumes and objects cannot be active
unless the objects they comprise are active, EVMS then adds to the list all
the objects that are comprised by the volumes and objects that were found in
the initial match.

 EVMS then removes from the list the volumes and objects whose names match
the "exclude" entry in the activation section of /etc/evms.conf. Because any
volumes or objects that are built from the excluded ones cannot be active,
EVMS removes them from the list as well.

 The enforcement of the dependencies can result in behavior that is not
immediately apparent. Let's say, for example, that segment hda7 is made into
volume /dev/evms/home. and the activation section in /etc/evms.conf looks
like this:
activate {
        include = [*]
        exclude = [had*]
}

 When EVMS builds the list of volumes and objects to activate, everything is
included. EVMS next removes all objects whose names start with "had." hda7
will be removed from the list. Next, because volume /dev/evms/home is built
from hda7, it will also be removed from the list and will not be activated.
So, although volume /dev/evms/home is not explicitly in the exclude list, it
is not activated because it depends on an object that will not be activated.
-----------------------------------------------------------------------------

18.2.3.2. Dependencies for compatibility volumes

 Compatibility volumes are made directly from the volume's object. That is,
the device node for the volume points directly to the device for the volume's
object. Because a compatibility volume is inseparable from its object, a
compatibility volume itself cannot be deactivated. To deactivate a
compatibility volume you must deactivate the volume's object.

 Similarly, if a compatibility volume and its object are not active and you
activate the volume's object, the compatibility volume will be active as
well.
-----------------------------------------------------------------------------

Chapter 19. Mounting and unmounting volumes from within EVMS

 Some volume operations, such as expanding and shrinking, may require that
the volume be mounted or unmounted before you can perform the operation. EVMS
lets you mount and unmount volumes from within EVMS without having to go to a
separate terminal session.

 EVMS performs the mount and unmount operations immediately. It does not wait
until the changes are saved.
-----------------------------------------------------------------------------

19.1. Mounting a volume

This section tells how to mount a volume through the various EVMS user
interfaces.
-----------------------------------------------------------------------------

19.1.1. Using the EVMS GUI

Follow these steps to mount a volume with the EVMS GUI:

 1. Select Actions->File System->Mount.

 2. Select the volume you want to mount.

 3. In the Mount Point box, enter the directory on which you want to mount
    the volume.

 4. Click Options if you want to enter additional options for the mount.

 5. Click Mount.


Alternatively, you can mount a volume from the EVMS GUI context sensitive
menu:

 1. Right click the volume you want to mount.

 2. Click Mount...

 3. In the Mount Point box, enter the directory on which you want to mount
    the volume.

 4.   Click Options if you want to enter additional options for the mount.

 5.   Click Mount.


-----------------------------------------------------------------------------
19.1.2. Using Ncurses

Follow these steps to mount a volume with Ncurses:

 1. Select Actions->File System->Mount....

 2. Select the volume you want to mount.

 3. At the Mount Point prompt, enter the directory on which you want to mount
    the volume and press Enter.

 4. Select Mount Options if you want to enter additional options for the
    mount.

 5. Select Mount.


Alternatively, you can mount a volume with the Ncurses context-sensitive
menu:

 1. Highlight the volume you want to mount and press Enter.

 2. Select Mount File System.

 3. At the Mount Point prompt, enter the directory on which you want to mount
    the volume and press Enter.

 4.  Select Mount Options if you want to enter additional options for the
    mount.

 5.  Select Mount.


-----------------------------------------------------------------------------
19.1.3. Using the CLI

To mount a volume with the CLI, use the following command:
mount:<volume>, <mount point>, [ <mount options> ]

<volume> is the name of the volume to be mounted.

<mount point> is the name of the directory on which to mount the volume.

<mount options> is a string of options to be passed to the <command>mount</
command> command.
-----------------------------------------------------------------------------

19.2. Unmounting a volume

This section tells how to unmount a volume through the various EVMS user
interfaces.
-----------------------------------------------------------------------------

19.2.1. Using the EVMS GUI

Follow these steps to unmount a volume with the EVMS GUI:

 1. Select Actions->File System->Unmount.

 2. Select the volume you want to unmount.

 3. Click Unmount.


Alternatively, you can unmount a volume from the EVMS GUI context sensitive
menu:

 1. Right click the volume you want to unmount.

 2. Click Unmount...

 3.   Click Unmount.


-----------------------------------------------------------------------------
19.2.2. Using Ncurses

Follow these steps to unmount a volume with Ncurses:

 1. Select Actions->File System->Unmount....

 2. Select the volume you want to unmount.

 3. Select Unmount.


Alternatively, you can unmount a volume with the Ncurses context-sensitive
menu:

 1. Highlight the volume you want to unmount and press Enter.

 2. Select Unmount File System.....

 3.  Select Unmount.


-----------------------------------------------------------------------------
19.2.3. Using the CLI

To unmount a volume with the CLI, use the following command:
unmount:<volume>

<volume> is the name of the volume to be unmounted.
-----------------------------------------------------------------------------

19.3. The SWAPFS file system

A volume with the SWAPFS file system is not mounted or unmounted. Rather,
swapping is turned on for the volume using the sbin/swapon command and turned
off using the <command>sbin/swapoff</command>. EVMS lets you turn swapping on
or off for a volume from within EVMS without having to go to a separate
terminal session.

As with mounting and unmounting, EVMS performs the swapon and swapoff
operations immediately. It does not wait until the changes are saved.
-----------------------------------------------------------------------------

19.3.1. Turning swap on

This section tells how to turn swap on using the various EVMS user
interfaces.
-----------------------------------------------------------------------------

19.3.1.1. Using the EVMS GUI

Follow these steps to turn swap on with the EVMS GUI:

 1. Select Actions->Other->Volume tasks....

 2. Select the volume you want to turn on swapping and click Next.

 3. Select "Swap on" and click Next.

 4. Select the priority for the swap. If you select "High" you will get an
    additional prompt for the priority level. The priority level must be a
    number in the range of 0 to 32767. The default is 0.

 5. Click Swap on.


Alternatively, you can turn swap on from the EVMS GUI context-sensitive menu:

 1. Right click the volume with the SWAPFS you want to turn on.

 2. Click Swap on...

 3. Select the priority for the swap. If you select "High" you will get an
    additional prompt for the priority level. The priority level must be a
    number in the range of 0 to 32767. The default is 0.

 4.   Click Swap on.


-----------------------------------------------------------------------------
19.3.1.2. Using Ncurses

Follow these steps to turn swap on with Ncurses:

 1. Select Actions->Other->Volume tasks....

 2. Select the volume on which you want to turn on swapping and select Next.

 3. Select "Swap on" and select Next.

 4. Select the priority for the swap. If you select "High" you will get an
    additional prompt for the priority level. The priority level must be a
    number in the range of 0 to 32767. The default is 0.

 5. Select "Swap on."


Alternatively, you can turn swap on with the Ncurses context-sensitive menu:

 1. Highlight the volume with the SWAPFS you want to turn on.

 2. Select "Swap on...."

 3.  Select the priority for the swap. If you select "High" you will get an
    additional prompt for the priority level. The priority level must be a
    number in the range of 0 to 32767. The default is 0.

 4. Select "Swap on."


-----------------------------------------------------------------------------
19.3.1.3. Using the CLI

To turn swap on with the CLI, use the following command:
Task: swapon, <volume>[, priority=low | , priority=high [level=0..32767]]

<volume> is the name of the volume with SWAPFS you want to turn on.
-----------------------------------------------------------------------------

19.3.2. Turning swap off

This section tells how to turn swap off using the various EVMS user
interfaces.
-----------------------------------------------------------------------------

19.3.2.1. Using the EVMS GUI

Follow these steps to turn swap off with the EVMS GUI:

 1. Select Actions->Other->Volume tasks....

 2. Select the volume you want to turn off swapping and click Next.

 3. Select "Swap off" and click Next.

 4. Click Swap off.


Alternatively, you can turn swap off from the EVMS GUI context-sensitive
menu:

 1. Right click the volume with the SWAPFS you want to turn off.

 2. Click Swap off...

 3.   Click Swap off.


-----------------------------------------------------------------------------
19.3.2.2. Using Ncurses

Follow these steps to turn swap off with Ncurses:

 1. Select Actions->Other->Volume tasks....

 2. Select the volume on which you want to turn off swapping and select Next.

 3. Select "Swap off" and select Next.

 4. Select "Swap off."


Alternatively, you can turn swap on with the Ncurses context-sensitive menu:

 1. Highlight the volume with the SWAPFS you want to turn off.

 2. Select "Swap off...."

 3. Select "Swap off."


-----------------------------------------------------------------------------
19.3.2.3. Using the CLI

To turn swap on with the CLI, use the following command:
Task: swapoff, <volume>

<volume> is the name of the volume with SWAPFS you want to turn off.
-----------------------------------------------------------------------------

Chapter 20. Plug-in operations tasks

This chapter discusses plug-in operations tasks and shows how to complete a
plug-in task with the EVMS GUI, Ncurses, and CLI interfaces.
-----------------------------------------------------------------------------

20.1. What are plug-in tasks?

Plug-in tasks are functions that are available only within the context of a
particular plug-in. These functions are not common to all plug-ins. For
example, tasks to add spare disks to a RAID array make sense only in the
context of the MD plug-in, and tasks to reset a snapshot make sense only in
the context of the Snapshot plug-in.
-----------------------------------------------------------------------------

20.2. Example: complete a plug-in operations task

This section shows how to complete a plug-in operations task with the EVMS
GUI, Ncurses, and CLI interfaces.



    Example 20-1. Add a spare disk to a compatibility volume made from an
    MDRaid5 region

    This example adds disk sde as a spare disk onto volume /dev/evms/md/md0,
    which is a compatibility volume that was created from an MDRaid5 region.

-----------------------------------------------------------------------------
20.2.1. Using the EVMS GUI

Follow these steps to add sde to /dev/evms/md/md0 with the EVMS GUI:

 1. Select Other->Storage Object Tasks...

 2. Select md/md0.

 3. Click Next.

 4. Select Add spare object.

 5. Click Next.

 6. Select sde.

 7. Click Add.

 8. The operation is completed when you save.


Alternatively, you could use context-sensitive menus to complete the task, as
follows:

 1. View the region md/md0. You can view the region either by clicking on the
    small plus sign beside the volume name (/dev/evms/md/md0) on the volumes
    tab, or by selecting the regions tab.

 2. Right click the region (md/md0). A list of acceptable Actions and
    Navigational shortcuts displays. The last items on the list are the tasks
    that are acceptable at this time.

 3. Point to Add spare object and left click.

 4. Select sde.

 5. Click Add.


-----------------------------------------------------------------------------
20.2.2. Using Ncurses

Follow these steps to add sde to /dev/evms/md/md0 with Ncurses:

 1. Select Other->Storage Object Tasks

 2. Select md/md0.

 3. Activate Next.

 4. Select Add spare object.

 5. Activate Next.

 6. Select sde.

 7. Activate Add.


Alternatively, you can use the context sensitive menu to complete the task:

 1. From the Regions view, press Enter on md/md0.

 2. Activate the Add spare object menu item.

 3. Select sde.

 4. Activate Add.


-----------------------------------------------------------------------------
20.2.3. Using the CLI

With the EVMS CLI, all plug-in tasks must be accomplished with the task
command. Follow these steps to add sde to /dev/evms/md/md0 with the CLI:

 1. The following query command with the list options filter to determines
    the acceptable tasks for a particular object and the name-value pairs it
    supports. The command returns information about which plug-in tasks are
    available at the current time and provides the information necessary for
    you to complete the command.
    query: objects, object=md/md0, list options

 2. The command takes the name of the task (returned from the previous
    query), the object to operate on (in this case, md/md0), any required
    options (none in this case) and, if necessary, another object to be
    manipulated (in our example, sde, which is the spare disk we want to
    add):
    task: addspare, md/md0, sde
    The command is completed upon saving.


-----------------------------------------------------------------------------
Chapter 21. Deleting objects

This chapter tells how to delete EVMS objects through the delete and delete
recursive operations.
-----------------------------------------------------------------------------

21.1. How to delete objects: delete and delete recursive

There are two ways in EVMS that you can destroy objects that you no longer
want: Delete and Delete Recursive. The Delete option destroys only the
specific object you specify. The Delete Recursive option destroys the object
you specify and its underlying objects, down to the container, if one exists,
or else down to the disk. In order for a volume to be deleted, it must not be
mounted. EVMS verifies that the volume you are attempting to delete is not
mounted and does not perform the deletion if the volume is mounted.
-----------------------------------------------------------------------------

21.2. Example: perform a delete recursive operation

The following example shows how to destroy a volume and the objects below it
with the EVMS GUI, Ncurses, and CLI interfaces.



    Example 21-1. Destroy a volume and the region and container below it

    This example uses the delete recursive operation to destroy volume /dev/
    evms/Sample Volume and the region and container below it. Volume /dev/
    evms/Sample Volume is the volume that was created in earlier. Although we
    could also use the delete option on each of the objects, the delete
    recursive option takes fewer steps. Note that because we intend to delete
    the container as well as the volume, the operation needs to be performed
    in two steps: one to delete the volume and its contents, and one to
    delete the container and its contents.

-----------------------------------------------------------------------------
21.2.1. Using the EVMS GUI

Follow these steps to delete the volume and the container with the EVMS GUI:

 1. Select Actions->Delete->Volume.

 2. Select volume /dev/evms/Sample Volume from the list.

 3. Click Recursive Delete. This step deletes the volume and the region lvm/
    Sample Container/Sample Region. If you want to keep the underlying pieces
    or want to delete each piece separately, you would click Delete instead
    of Delete Recursive.

 4. Assuming you chose Delete Recursive (if not, delete the region before
    continuing with these steps), select Actions->Delete->Container.

 5. Select container lvm/Sample Container from the list.

 6. Click Recursive Delete to destroy the container and anything under it.
    Alternatively, click Delete to destroy only the container (if you built
    the container on disks as in the example, either command has the same
    effect).


Alternatively, you can perform some of the volume deletion steps with the GUI
context sensitive menu:

 1. From the Volumes tab, right click /dev/evms/Sample Volume.

 2. Click Delete...

 3. Continue with the operation beginning with step 3 of the GUI
    instructions.


-----------------------------------------------------------------------------
21.2.2. Using Ncurses

Follow these steps to delete the volume and the container with Ncurses:

 1. Select Actions->Delete->Volume.

 2. Select volume /dev/evms/Sample Volume from the list.

 3. Activate Delete Volume Recursively. This step deletes the volume and the
    region lvm/Sample Container/Sample Region. If you want to keep the
    underlying pieces or want to delete each piece separately, activate
    Delete instead of Delete Recursive.

 4. Assuming you chose Delete Volume Recursively (if not, delete the region
    before continuing with these steps), select Actions->Delete->Container.

 5. Select container lvm/Sample Container from the list.

 6. Click Recursive Delete to destroy the container and everything under it.
    Alternatively, activate Delete to delete only the container (if you built
    the container on disks as in the example, either command has the same
    effect).

 7. Press Enter.


Alternatively, you can perform some of the volume deletion steps with the
context sensitive menu:

 1. From the Volumes view, press Enter on /dev/evms/Sample Volume.

 2. Activate Delete.

 3. Continue with the operation beginning with step 3 of the Ncurses
    instructions.


-----------------------------------------------------------------------------
21.2.3. Using the CLI

Use the delete and delete recursive commands to destroy EVMS objects. Specify
the command name followed by a colon, and then specify the volume, object, or
container name. For example:

 1. Enter this command to perform the delete recursive operation:
    delete recursive: "/dev/evms/Sample Volume"

    This step deletes the volume and the region /lvm/Sample Container/Sample
    Region. If you wanted to keep the underlying pieces or wanted to delete
    each piece separately, use the delete command, as follows:
    delete: "/dev/evms/Sample Volume"

 2. Assuming you chose Delete Volume Recursively (if not, delete the region
    before continuing with these steps) enter the following to destroy the
    container and everything under it:
    delete recursive: "lvm/Sample Container"

    To destroy only the container, enter the following:
    delete: "lvm/Sample Container"


-----------------------------------------------------------------------------
Chapter 22. Replacing objects

This chapter discusses how to replace objects.
-----------------------------------------------------------------------------

22.1. What is object-replace?

Occasionally, you might wish to change the configuration of a volume or
storage object. For instance, you might wish to replace one of the disks in a
drive-link or RAID-0 object with a newer, faster disk. As another example,
you might have an EVMS volume created from a simple disk segment, and want to
switch that segment for a RAID-1 region to provide extra data redundancy.
Object-replace accomplishes such tasks.

 Object-replace gives you the ability to swap one object for another object.
The new object is added while the original object is still in place. The data
is then copied from the original object to the new object. When this is
complete, the original object is removed. This process can be performed while
the volume is mounted and in use.
-----------------------------------------------------------------------------

22.2. Replacing a drive-link child object

For this example, we will start with a drive-link object named link1, which
is composed of two disk segments named sda1 and sdb1. The goal is to replace
sdb1 with another segment named sdc1.

Note Note
�    The drive-linking plug-in allows the target object (sdc1 in this
     example) to be the same size or larger than the source object. If the
     target is larger, the extra space will be unused. Other plug-ins have
     different restrictions and might require that both objects be the same
     size.
-----------------------------------------------------------------------------

22.2.1. Using the EVMS GUI or Ncurses

Follow these steps to replace sdb1 with sdc1:

 1. Select Actions->Replace.

 2. In the "Replace Source Object" panel select sdb1.

 3. Activate Next.

 4. In the "Select Replace Target Object" panel, select sdc1.

 5. Activate Replace.


Alternatively, you can perform these same steps with the context sensitive
menus:

 1. From the "Disk Segments" panel, right click (or Press Enter on) the
    object sdb1.
