     node on which the cluster container resides is the only active node in
     the cluster. Otherwise, the data in volumes on shared and private
     containers on the node can get corrupted.

 1.  Enabling maintenance mode in the /etc/evms.conf file. The option to
    modify in the /etc/evms.conf file is the following:
    # cluster segment manager section
    csm {
    #       admin_mode=yes  # values are: yes or no
                                    # The default is no. Set this key to
                                    # yes when you wish to force the CSM
                                    # to discover objects from all cluster
                                    # containers, allowing you to perform
                                    # configuration and maintenance.  Setting
                                    # admin_mode to yes will cause the CSM
                                    # to ignore container ownership, which
                                    # will allow you to configure storage
                                    # in a maintenance mode.



 2.  Running evms_activate on the node.


-----------------------------------------------------------------------------
Chapter 15. Converting volumes

This chapter discusses converting compatibility volumes to EVMS volumes and
converting EVMS volumes to compatibility volumes. For a discussion of the
differences between compatibility and EVMS volumes, see Chapter 12.
-----------------------------------------------------------------------------

15.1. When to convert volumes

There are several different scenarios that might help you determine what type
of volumes you need. For example, if you wanted persistent names or to make
full use of EVMS features, such as Drive Linking or Snapshotting, you would
convert your compatibility volumes to EVMS volumes. In another situation, you
might decide that a volume needs to be read by a system that understands the
underlying volume management scheme. In this case, you would convert your
EVMS volume to a compatibility volume.

A volume can only be converted when it is offline. This means the volume must
be unmounted and otherwise not in use. The volume must be unmounted because
the conversion operation changes both the name and the device number of the
volume. Once the volume is converted, you can remount it using its new name.
-----------------------------------------------------------------------------

15.2. Example: convert compatibility volumes to EVMS volumes

A compatibility volume can be converted to an EVMS volume in the following
situations:

��*�The compatibility volume has no file system (FSIM) on it.

��*�The compatibility volume has a file system, but the file system can be
    shrunk (if necessary) to make room for the EVMS metadata.


This section provides a detailed explanation of how to convert compatibility
volumes to EVMS volumes and provides instructions to help you complete the
following task.



    Example 15-1. Convert a compatibility volume

    You have a compatibility volume /dev/evms/hda3 that you want to make into
    an EVMS volume named my_vol.

-----------------------------------------------------------------------------
15.2.1. Using the EVMS GUI

Follow these steps to convert a compatibility volume with the EVMS GUI:

 1. Choose Action->Convert ->Compatibility Volume to EVMS.

 2. Select /dev/evms/hda3 from the list of available volumes.

 3. Type my_vol in the name field.

 4. Click the Convert button to convert the volume.


Alternatively, you can perform some of the steps to convert the volume from
the GUI context sensitive menu:

 1. From the Volumes tab, right click on /dev/evms/hda3.

 2. Click Convert to EVMS Volume...

 3. Continue to convert the volume beginning with step 3 of the GUI
    instructions.


-----------------------------------------------------------------------------
15.2.2. Using Ncurses

Follow these instructions to convert a compatibility volume to an EVMS volume
with the Ncurses interface:

 1. Choose Actions->Convert->Compatibility Volume to EVMS Volume

 2. Select /dev/evms/hda3 from the list of available volumes.

 3. Type my_vol when prompted for the name. Press Enter.

 4. Activate Convert.


Alternatively, you can perform some of the steps to convert the volume from
the context sensitive menu:

 1. From the Volumes view, press Enter on /dev/evms/hda3.

 2. Activate the Convert to EVMS Volume menu item.

 3. Continue to convert the volume beginning with step 3 of the Ncurses
    instructions.


-----------------------------------------------------------------------------
15.2.3. Using the CLI

To convert a volume, use the Convert command. The Convert command takes the
name of a volume as its first argument, and then name= for what you want to
name the new volume as the second argument. To complete the example and
convert a volume, type the following command at the EVMS: prompt:
convert: /dev/evms/hda3, Name=my_vol
-----------------------------------------------------------------------------

15.3. Example: convert EVMS volumes to compatibility volumes

An EVMS volume can be converted to a compatibility volume only if the volume
does not have EVMS features on it. This section provides a detailed
explanation of how to convert EVMS volumes to compatibility volumes by
providing instructions to help you complete the following task.



    Example 15-2. Convert an EVMS volume

    You have an EVMS volume, /dev/evms/my_vol, that you want to make a
    compatibility volume.

-----------------------------------------------------------------------------
15.3.1. Using the EVMS GUI

Follow these instructions to convert an EVMS volume to a compatibility volume
with the EVMS GUI:

 1. Choose Action->Convert ->EVMS Volume to Compatibility Volume.

 2. Select /dev/evms/my_vol from the list of available volumes.

 3. Click the Convert button to convert the volume.


Alternatively, you can perform some of the steps to convert the volume
through the GUI context sensitive menu:

 1. From the Volumes tab, right click /dev/evms/my_vol.

 2. Click Convert to Compatibility Volume...

 3. Continue converting the volume beginning with step 3 of the GUI
    instructions.


-----------------------------------------------------------------------------
15.3.2. Using Ncurses

Follow these instructions to convert an EVMS volume to a compatibility volume
with the Ncurses interface:

 1. Choose Actions->Convert->EVMS Volume to Compatibility Volume

 2. Select /dev/evms/my_vol from the list of available volumes.

 3. Activate Convert.


Alternatively, you can perform some of the steps to convert the volume
through the context sensitive menu:

 1. From the Volumes view, press Enter on /dev/evms/my_vol.

 2. Activate the Convert to Compatibility Volume menu item.

 3. Continue to convert the volume beginning with step 3 of the Ncurses
    instructions.


-----------------------------------------------------------------------------
15.3.3. Using the CLI

To convert a volume use the Convert command. The Convert command takes the
name of a volume as its first argument, and the keyword compatibility to
indicate a change to a compatibility volume as the second argument. To
complete the example and convert a volume, type the following command at the
EVMS: prompt:
convert: /dev/evms/my_vol, compatibility
-----------------------------------------------------------------------------

Chapter 16. Expanding and shrinking volumes

This chapter tells how to expand and shrink EVMS volumes with the EVMS GUI,
Ncurses, and CLI interfaces. Note that you can also expand and shrink
compatibility volumes and EVMS objects.
-----------------------------------------------------------------------------

16.1. Why expand and shrink volumes?

Expanding and shrinking volumes are common volume operations on most systems.
For example, it might be necessary to shrink a particular volume to create
free space for another volume to expand into or to create a new volume.

EVMS simplifies the process for expanding and shrinking volumes, and protects
the integrity of your data, by coordinating expand and shrink operations with
the volume's file system. For example, when shrinking a volume, EVMS first
shrinks the underlying file system appropriately to protect the data. When
expanding a volume, EVMS expands the file system automatically when new space
becomes available.

Not all file system interface modules (FSIM) types supported by EVMS allow
shrink and expand operations, and some only perform the operations when the
file system is mounted ("online"). The following table details the shrink and
expand options available for each type of FSIM.

Table 16-1. FSIM support for expand and shrink operations
+-----------------+-----------------+------------------+
|FSIM type        |Shrinks          |Expands           |
+-----------------+-----------------+------------------+
|JFS              |No               |Online only       |
+-----------------+-----------------+------------------+
|XFS              |No               |Online only       |
+-----------------+-----------------+------------------+
|ReiserFS         |Offline only     |Offline and online|
+-----------------+-----------------+------------------+
|ext2/3           |Offline only     |Offline only      |
+-----------------+-----------------+------------------+
|SWAPFS           |Offline only     |Offline only      |
+-----------------+-----------------+------------------+
|OpenGFS          |No               |Online only       |
+-----------------+-----------------+------------------+
|NTFS             |Offline only     |Offline only      |
+-----------------+-----------------+------------------+

You can perform all of the supported shrink and expand operations with each
of the EVMS user interfaces.
-----------------------------------------------------------------------------

16.2. Example: shrink a volume

This section tells how to shrink a compatibility volume by 500 MB.



    Example 16-1. Shrink a volume

    Shrink the volume /dev/evms/lvm/Sample Container/Sample Region, which is
    the compatibility volume that was created in the chapter entitled
    "Creating Volumes," by 500 MB.

-----------------------------------------------------------------------------
16.2.1. Using the EVMS GUI

Follow these steps to shrink the volume with the EVMS GUI:

 1. Select Actions->Shrink->Volume...

 2. Select /dev/evms/lvm/Sample Container/Sample Region from the list of
    volumes.

 3. Click Next.

 4. Select /lvm/Sample Container/Sample Region from the list of volumes.

 5. Click Next.

 6. Enter 500MB in the "Shrink by Size" field.

 7. Click Shrink.


Alternatively, you can perform some of the steps to shrink the volume with
the GUI context sensitive menu:

 1. From the Volumes tab, right click /dev/evms/lvm/Sample Container/Sample
    Region

 2. Click Shrink...

 3. Continue the operation beginning with step 3 of the GUI instructions.


-----------------------------------------------------------------------------
16.2.2. Using Ncurses

Follow these steps to shrink a volume with Ncurses:

 1. Select Actions->Shrink->Volume.

 2. Select /dev/evms/lvm/Sample Container/Sample Region from the list of
    volumes.

 3. Activate Next.

 4. Select lvm/Sample Container/Sample Region from the shrink point selection
    list.

 5. Activate Next.

 6. Scroll down using the down arrow until Shrink by Size is highlighted.

 7. Press spacebar.

 8. Press Enter.

 9. At the "::" prompt enter 500MB.

10. Press Enter.

11. Activate Shrink.


 Alternatively, you can perform some of the steps to shrink the volume with
the context sensitive menu:

 1. From the Volumes view, press Enter on /dev/evms/lvm/Sample Container/
    Sample Region.

 2. Activate the Shrink menu item.

 3. Continue the operation beginning with step 3 of the Ncurses instructions.


-----------------------------------------------------------------------------
16.2.3. Using the CLI

The shrink command takes a shrink point followed by an optional name value
pair or an optional shrink object. To find the shrink point, use the query
command with the shrink points filter on the object or volume you plan to
shrink. For example:
query: shrink points, "/dev/evms/lvm/Sample Container/Sample Region"

Use a list options filter on the object of the shrink point to determine the
name-value pair to use, as follows:
query: objects, object="lvm/Sample Container/Sample Region", list options

With the option information that is returned, you can construct the command,
as follows:
shrink: "lvm/Sample Container/Sample Region", remove_size=500MB
-----------------------------------------------------------------------------

16.3. Example: expand a volume

This section tells how to expand a volume a compatibility volume by 500 MB.



    Example 16-2. Expand a volume

    Expand the volume /dev/evms/lvm/Sample Container/Sample Region, which is
    the compatibility volume that was created in the chapter entitled
    "Creating Volumes," by 500 MB.

-----------------------------------------------------------------------------
16.3.1. Using the EVMS GUI

Follow these steps to expand the volume with the EVMS GUI:

 1. Select Actions->Expand->Volume...

 2. Select /dev/evms/lvm/Sample Container/Sample Region from the list of
    volumes.

 3. Click Next.

 4. Select lvm/Sample Container/Sample Region from the list as the expand
    point.

 5. Click Next.

 6. Enter 500MB in the "Additional Size" field.

 7. Click Expand.


Alternatively, you can perform some of the steps to expand the volume with
the GUI context sensitive menu:

 1. From the Volumes tab, right click /dev/evms/lvm/Sample Container/Sample
    Region.

 2. Click Expand...

 3. Continue the operation to expand the volume beginning with step 3 of the
    GUI instructions.


-----------------------------------------------------------------------------
16.3.2. Using Ncurses

Follow these steps to expand a volume with Ncurses:

 1. Select Actions->Expand->Volume.

 2. Select /dev/evms/lvm/Sample Container/Sample Region from the list of
    volumes.

 3. Activate Next.

 4. Select lvm/Sample Container/Sample Region from the list of expand points.

 5. Activate Next.

 6. Press spacebar on the Additional Size field.

 7. At the "::" prompt enter 500MB.

 8. Press Enter.

 9. Activate Expand.


Alternatively, you can perform some of the steps to shrink the volume with
the context sensitive menu:

 1. From the Volumes view, press Enter on /dev/evms/lvm/Sample Container/
    Sample Region.

 2. Activate the Expand menu item.

 3. Continue the operation beginning with step 3 of the Ncurses instructions.


-----------------------------------------------------------------------------
16.3.3. Using the CLI

The expand command takes an expand point followed by an optional name value
pair and an expandable object. To find the expand point, use the query
command with the Expand Points filter on the object or volume you plan to
expand. For example:
query: expand points, "/dev/evms/lvm/Sample Container/Sample Region"

Use a list options filter on the object of the expand point to determine the
name-value pair to use, as follows:
query: objects, object="lvm/Sample Container/Sample Region", list options

The free space in your container is the container name plus /Freespace.

With the option information that is returned, you can construct the command,
as follows:
expand: "lvm/Sample Container/Sample Region", add_size=500MB,
"lvm/Sample Container/Freespace"
-----------------------------------------------------------------------------

Chapter 17. Adding features to an existing volume

This chapter tells how to add additional EVMS features to an already existing
EVMS volume.
-----------------------------------------------------------------------------

17.1. Why add features to a volume?

EVMS lets you add features such as drive linking to a volume that already
exists. By adding features, you avoid having to potentially destroy the
volume and recreate it from scratch. For example, take the scenario of a
volume that contains important data but is almost full. If you wanted to add
more data to that volume but no free space existed on the disk immediately
after the segment, you could add a drive link to the volume. The drive link
concatenates another object to the end of the volume and continues
seamlessly.
-----------------------------------------------------------------------------

17.2. Example: add drive linking to an existing volume

The following example shows how to add drive linking to a volume with the
EVMS GUI, Ncurses, and CLI interfaces.



    Example 17-1. Add drive linking to an existing volume

    The following sections show how to add a drive link to volume /dev/evms/
    vol and call the drive link "DL."

    Note NOTE
    �    Drive linking can be done only on EVMS volumes; therefore, /dev/evms
         /vol must be converted to an EVMS volume if it is not already.

-----------------------------------------------------------------------------
17.2.1. Using the EVMS GUI

Follow these steps to add a drive link to the volume with the EVMS GUI:

 1. Select Actions->Add->Feature to Volume.

 2. Select /dev/evms/vol

 3. Click Next.

 4. Select Drive Linking Feature.

 5. Click Next.

 6. Type DL in the Name Field.

 7. Click Add.


Alternatively, you can perform some of the steps to add a drive link with the
GUI context sensitive menu:

 1. From the Volumes tab, right click /dev/evms/vol.

 2. Click Add feature...

 3. Continue adding the drive link beginning with step 3 of the GUI
    instructions.


-----------------------------------------------------------------------------
17.2.2. Using Ncurses

Follow these steps to add a drive link to a volume with Ncurses:

 1. Select Actions->Add->Feature to Volume.

 2. Select /dev/evms/vol.

 3. Activate Next.

 4. Select Drive Linking Feature.

 5. Activate Next.

 6. Press Spacebar to edit the Name field.

 7. At the "::" prompt enter DL.

 8. Press Enter.

 9. Activate Add.


Alternatively, you can perform some of the steps to add a drive link with the
context sensitive menu:

 1. From the Volumes view, press Enter on /dev/evms/vol.

 2. Activate the Add feature menu item.

 3. Continue adding the drive link beginning with step 3 of the Ncurses
    instructions.


-----------------------------------------------------------------------------
17.2.3. Using the CLI

Use the add feature to add a feature to an existing volume. Specify the
command name followed by a colon, followed by any options and the volume to
operate on. To determine the options for a given feature, use the following
query:
query: plugins, plugin=DriveLink, list options

 The option names and descriptions are listed to help you construct your
command. For our example, the command would look like the following:
add feature: DriveLink={ Name="DL }, /dev/evms/vol
-----------------------------------------------------------------------------

Chapter 18. Selectively activating volumes and objects

This chapter discusses selective activation and deactivation of EVMS volumes
and objects.
-----------------------------------------------------------------------------

18.1. Initial activation using /etc/evms.conf

 There is a section in the EVMS configuration file, /etc/etc/evms.conf, named
"activate." This section has two entries: "include" and "exclude." The
"include" entry lists the volumes and objects that should be activated. The
"exclude" entry lists the volumes and objects that should not be activated.

 Names in either of the entries can be specified using "*", "?", and "[...]"
notation. For example, the following entry will activate all the volumes:
include = [/dev/evms/*]

 The next entry specifies that objects sda5 and sda7 not be activated:
exclude = [ sda[57] ]

When EVMS is started, it first reads the include entry and builds a list of
the volumes and objects that it should activate. It then reads the exclude
entry and removes from the list any names found in the exclude list. For
example, an activation section that activates all of the volumes except /dev/
evms/temp looks like this:
activate {
        include = [/dev/evms/*]
        exclude = [/dev/evms/temp]
}

 If /etc/evms.conf does not contain an activate section, the default behavior
is to activate everything. This behavior is consistent with versions of EVMS
prior to 2.4.

 Initial activation via /etc/evms.conf does not deactivate any volumes or
objects. It only determines which ones should be active.
-----------------------------------------------------------------------------

18.2. Activating and deactivating volumes and objects

 The EVMS user interfaces offer the ability to activate or deactivate a
particular volume or object. The volume or object will be activated or
deactivated when the changes are saved.
-----------------------------------------------------------------------------

18.2.1. Activation

 You can activate inactive volumes and objects using the various EVMS user
interfaces.

Note Note
�    EVMS does not currently update the EVMS configuration file (/etc/
     evms.conf) when volumes and objects are activated. If you activate a
     volume or object that is not initially activated and do not make the
     corresponding change in /etc/evms.conf, the volume or object will not be
     activated the next time the system is booted and you run evms_activate
     or one of the user interfaces.
-----------------------------------------------------------------------------

18.2.1.1. Using the EVMS GUI

To activate volumes or objects with the GUI, follow these steps:

 1. Select Actions->Activation->Activate...

 2. Select the volume(s) and object(s) you want to activate.

 3.  Click Activate.

 4. Click Save to save the changes and activate the volume(s) and object(s).


-----------------------------------------------------------------------------
18.2.1.2. Using the EVMS GUI context-sensitive menu

To activate with the GUI context-sensitive menu, follow these steps:

 1.  Right click the volume or object you want to activate.

 2.  Click "Activate."

 3.  Click Activate.

 4. Click Save to save the changes and activate the volume(s) and object(s).


-----------------------------------------------------------------------------
18.2.1.3. Using Ncurses

To activate a volume or object with Ncurses, follow these steps:

 1. Select Actions->Activation->Activate...

 2. Select the volume(s) and object(s) you want to activate.

 3.  Select Activate.

 4. Select Actions->Save to save the changes and activate the volume(s) and
    object(s).


-----------------------------------------------------------------------------
18.2.1.4. Using the Ncurses context-sensitive menu

To enable activation on a volume or object with the Ncurses context-sensitive
menu, follow these steps:

 1.  Highlight the volume or object you want to activate and press Enter.

 2.  Select "Activate."

 3.  Select Activate.

 4. Select Actions->Save to save the changes and activate the volume(s) and
    object(s).


-----------------------------------------------------------------------------
18.2.1.5. Using the CLI

To activate a volume or object with the CLI, issue the following command to
the CLI (where "name" is the name of the volume or object you want to
activate):
Activate:name
-----------------------------------------------------------------------------

18.2.2. Deactivation

 You can deactivate active volumes and objects using the various EVMS user
interfaces.

Note Note
�    EVMS does not currently update the EVMS configuration file (/etc/
     evms.conf) when a volume or object is deactivated. If you deactivate a
     volume or object that is initially activated and do not make the
     corresponding change in /etc/evms.conf, then the volume or object will
     be activated the next time you run evms_activate or one of the user
     interfaces.
