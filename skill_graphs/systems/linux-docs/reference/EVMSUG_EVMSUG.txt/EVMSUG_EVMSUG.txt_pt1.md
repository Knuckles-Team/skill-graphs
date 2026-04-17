```
EVMS User Guide

Christine Lorenz

IBM

Joy Goodreau

IBM

Kylie Smith

IBM

Copyright � 2004 IBM

September 16, 2004


Special Notices

The following terms are registered trademarks of International Business
Machines corporation in the United States and/or other countries: AIX, OS/2,
System/390. A full list of U.S. trademarks owned by IBM may be found at
[http://www.ibm.com/legal/copytrade.shtml] http://www.ibm.com/legal/
copytrade.shtml.

Intel is a trademark or registered trademark of Intel Corporation in the
United States, other countries, or both.

Windows is a trademark of Microsoft Corporation in the United States, other
countries, or both.

Linux is a trademark of Linus Torvalds.

UNIX is a registered trademark of The Open Group in the United States and
other countries.

Other company, product, and service names may be trademarks or service marks
of others.

This document is provided "AS IS," with no express or implied warranties. Use
the information in this document at your own risk.


License Information

This document may be reproduced or distributed in any form without prior
permission provided the copyright notice is retained on all copies. Modified
versions of this document may be freely distributed provided that they are
clearly identified as such, and this copyright is included intact.
-----------------------------------------------------------------------------

Table of Contents
Preface
1. What is EVMS?
    1.1. Why choose EVMS?
    1.2. The EVMS user interfaces
    1.3. EVMS terminology
    1.4. What makes EVMS so flexible?
    1.5. Plug-in layer definitions


2. Using the EVMS interfaces
    2.1. EVMS GUI
    2.2. EVMS Ncurses interface
    2.3. EVMS Command Line Interpreter


3. The EVMS log file and error data collection
    3.1. About the EVMS log file
    3.2. Log file logging levels
    3.3. Specifying the logging levels


4. Viewing compatibility volumes after migrating
    4.1. Using the EVMS GUI
    4.2. Using Ncurses
    4.3. Using the CLI


5. Obtaining interface display details
    5.1. Using the EVMS GUI
    5.2. Using Ncurses
    5.3. Using the CLI


6. Adding and removing a segment manager
    6.1. When to add a segment manager
    6.2. Types of segment managers
    6.3. Adding a segment manager to an existing disk
    6.4. Adding a segment manager to a new disk
    6.5. Example: add a segment manager
    6.6. Removing a segment manager
    6.7. Example: remove a segment manager


7. Creating segments
    7.1. When to create a segment
    7.2. Example: create a segment


8. Creating a container
    8.1. When to create a container
    8.2. Example: create a container


9. Creating regions
    9.1. When to create regions
    9.2. Example: create a region


10. Creating drive links
    10.1. What is drive linking?
    10.2. How drive linking is implemented
    10.3. Creating a drive link
    10.4. Example: create a drive link
    10.5. Expanding a drive link
    10.6. Shrinking a drive link
    10.7. Deleting a drive link


11. Creating snapshots
    11.1. What is a snapshot?
    11.2. Creating snapshot objects
    11.3. Example: create a snapshot
    11.4. Reinitializing a snapshot
    11.5. Expanding a snapshot
    11.6. Deleting a snapshot
    11.7. Rolling back a snapshot


12. Creating volumes
    12.1. When to create a volume
    12.2. Example: create an EVMS native volume
    12.3. Example: create a compatibility volume


13. FSIMs and file system operations
    13.1. The FSIMs supported by EVMS
    13.2. Example: add a file system to a volume
    13.3. Example: check a file system


14. Clustering operations
    14.1. Rules and restrictions for creating cluster containers
    14.2. Example: create a private cluster container
    14.3. Example: create a shared cluster container
    14.4. Example: convert a private container to a shared container
    14.5. Example: convert a shared container to a private container
    14.6. Example: deport a private or shared container
    14.7. Deleting a cluster container
    14.8. Failover and Failback of a private container on Linux-HA
    14.9. Remote configuration management
    14.10. Forcing a cluster container to be active


15. Converting volumes
    15.1. When to convert volumes
    15.2. Example: convert compatibility volumes to EVMS volumes
    15.3. Example: convert EVMS volumes to compatibility volumes


16. Expanding and shrinking volumes
    16.1. Why expand and shrink volumes?
    16.2. Example: shrink a volume
    16.3. Example: expand a volume


17. Adding features to an existing volume
    17.1. Why add features to a volume?
    17.2. Example: add drive linking to an existing volume


18. Selectively activating volumes and objects
    18.1. Initial activation using /etc/evms.conf
    18.2. Activating and deactivating volumes and objects


19. Mounting and unmounting volumes from within EVMS
    19.1. Mounting a volume
    19.2. Unmounting a volume
    19.3. The SWAPFS file system


20. Plug-in operations tasks
    20.1. What are plug-in tasks?
    20.2. Example: complete a plug-in operations task


21. Deleting objects
    21.1. How to delete objects: delete and delete recursive
    21.2. Example: perform a delete recursive operation


22. Replacing objects
    22.1. What is object-replace?
    22.2. Replacing a drive-link child object


23. Moving segment storage objects
    23.1. What is segment moving?
    23.2. Why move a segment?
    23.3. Which segment manager plug-ins implement the move function?
    23.4. Example: move a DOS segment


A. The DOS plug-in
    A.1. How the DOS plug-in is implemented
    A.2. Assigning the DOS plug-in
    A.3. Creating DOS partitions
    A.4. Expanding DOS partitions
    A.5. Shrinking DOS partitions
    A.6. Deleting partitions


B. The MD region manager
    B.1. Characteristics of Linux RAID levels
    B.2. Creating an MD region
    B.3. Active and spare objects
    B.4. Faulty objects
    B.5. Resizing MD regions
    B.6. Replacing objects


C. The LVM plug-in
    C.1. How LVM is implemented
    C.2. Container operations
    C.3. Region operations


D. The LVM2 plug-in
    D.1. Container operations
    D.2. Region operations


E. The CSM plug-in
    E.1. Assigning the CSM plug-in
    E.2. Unassigning the CSM plug-in
    E.3. Deleting a CSM container


F. JFS file system interface module
    F.1. Creating JFS file systems
    F.2. Checking JFS file systems
    F.3. Removing JFS file systems
    F.4. Expanding JFS file systems
    F.5. Shrinking JFS file systems


G. XFS file system interface module
    G.1. Creating XFS file systems
    G.2. Checking XFS file systems
    G.3. Removing XFS file systems
    G.4. Expanding XFS file systems
    G.5. Shrinking XFS file systems


H. ReiserFS file system interface module
    H.1. Creating ReiserFS file systems
    H.2. Checking ReiserFS file systems
    H.3. Removing ReiserFS file systems
    H.4. Expanding ReiserFS file systems
    H.5. Shrinking ReiserFS file systems


I. Ext-2/3 file system interface module
    I.1. Creating Ext-2/3 file systems
    I.2. Checking Ext-2/3 file systems
    I.3. Removing Ext-2/3 file systems
    I.4. Expanding and shrinking Ext-2/3 file systems


J. OpenGFS file system interface module
    J.1. Creating OpenGFS file systems
    J.2. Checking OpenGFS file systems
    J.3. Removing OpenGFS file systems
    J.4. Expanding and shrinking OpenGFS file systems


K. NTFS file system interface module
    K.1. Creating NTFS file systems
    K.2. Fixing NTFS file systems
    K.3. Cloning NTFS file systems
    K.4. Removing NTFS file systems
    K.5. Expanding and shrinking NTFS file systems



List of Tables
1. Organization of the EVMS User Guide
1-1. EVMS user interfaces
2-1. Accelerator keys in the Main Window
2-2. Accelerator keys in the views
2-3. Accelerator keys in the selection window
2-4. Accelerator keys in the configuration options window
2-5. Widget navigation keys in the configuration options window
3-1. EVMS logging levels
16-1. FSIM support for expand and shrink operations

List of Figures
4-1. GUI start-up window
4-2. Ncurses start-up window
4-3. CLI volume query results

List of Examples
6-1. Add the DOS Segment Manager
6-2. Remove the DOS Segment Manager
7-1. Create a 100MB segment
8-1. Create "Sample Container"
9-1. Create "Sample Region"
10-1. Create a drive link
11-1. Create a snapshot of a volume
12-1. Create an EVMS native volume
12-2. Create a compatibility volume
13-1. Add a JFS File System to a Volume
13-2. Check a JFS File System
14-1. Create a private cluster container
14-2. Create a shared cluster container
14-3. Convert a private container to shared
14-4. Convert a shared container to private
14-5. Deport a cluster container
15-1. Convert a compatibility volume
15-2. Convert an EVMS volume
16-1. Shrink a volume
16-2. Expand a volume
17-1. Add drive linking to an existing volume
20-1. Add a spare disk to a compatibility volume made from an MDRaid5 region
21-1. Destroy a volume and the region and container below it

-----------------------------------------------------------------------------
Preface

This guide tells how to configure and manage Enterprise Volume Management
System (EVMS). EVMS is a storage management program that provides a single
framework for managing and administering your system's storage.

This guide is intended for Linux system administrators and users who are
responsible for setting up and maintaining EVMS.

For additional information about EVMS or to ask questions specific to your
distribution, refer to the EVMS mailing lists. You can view the list archives
or subscribe to the lists from the EVMS Project web site.

The following table shows how this guide is organized:


Table 1. Organization of the EVMS User Guide
+------------------+-------------------------------------------+
|Chapter or        |Contents                                   |
|appendix title    |                                           |
+------------------+-------------------------------------------+
|1. What is EVMS?  |Discusses general EVMS concepts and terms. |
+------------------+-------------------------------------------+
|2. Using the EVMS |Describes the three EVMS user interfaces   |
|interfaces        |and how to use them.                       |
+------------------+-------------------------------------------+
|3. The EVMS log   |Discusses the EVMS information and error   |
|file and error    |log file and explains how to change the    |
|data collection   |logging level.                             |
+------------------+-------------------------------------------+
|4. Viewing        |Tells how to view existing files that have |
|compatibility     |been migrated to EVMS.                     |
|volumes after     |                                           |
|migrating         |                                           |
+------------------+-------------------------------------------+
|5. Obtaining      |Tells how to view detailed information     |
|interface display |about EVMS objects.                        |
|details           |                                           |
+------------------+-------------------------------------------+
|6. Adding and     |Discusses segments and explains how to add |
|removing a segment|and remove a segment manager.              |
|manager           |                                           |
+------------------+-------------------------------------------+
|7. Creating       |Explains when and how to create segments.  |
|segments          |                                           |
+------------------+-------------------------------------------+
|8. Creating       |Discusses containers and explains when and |
|containers        |how to create them.                        |
+------------------+-------------------------------------------+
|9. Creating       |Discusses regions and explains when and how|
|regions           |to create them.                            |
+------------------+-------------------------------------------+
|10. Creating drive|Discusses the drive linking feature and    |
|links             |tells how to create a drive link.          |
+------------------+-------------------------------------------+
|11. Creating      |Discusses snapshotting and tells how to    |
|snapshots         |create a snapshot.                         |
+------------------+-------------------------------------------+
|12. Creating      |Explains when and how to create volumes.   |
|volumes           |                                           |
+------------------+-------------------------------------------+
|13. FSIMs and file|Discusses the standard FSIMs shipped with  |
|system operations |EVMS and provides examples of adding file  |
|                  |systems and coordinating file checks with  |
|                  |the FSIMs.                                 |
+------------------+-------------------------------------------+
|14. Clustering    |Describes EVMS clustering and how to create|
|operations        |private and shared containers.             |
+------------------+-------------------------------------------+
|15. Converting    |Explains how to convert EVMS native volumes|
|volumes           |to compatibility volumes and compatibility |
|                  |volumes to EVMS native volumes.            |
+------------------+-------------------------------------------+
|16. Expanding and |Tells how to expand and shrink EVMS volumes|
|shrinking volumes |with the various EVMS user interfaces.     |
+------------------+-------------------------------------------+
|17. Adding        |Tells how to add additional features, such |
|features to an    |as drive linking, to an existing volume.   |
|existing volume   |                                           |
+------------------+-------------------------------------------+
|18. Selectively   |Explains how to selectively activate and   |
|activating volumes|deactivate volumes and options.              |
|and objects       |                                           |
+------------------+-------------------------------------------+
|19. Mounting and  |Tells how to have EVMS mount and unmount   |
|unmounting volumes|volumes so you do not have to open a       |
|from within EVMS. |separate terminal session.                 |
+------------------+-------------------------------------------+
|20. Plug-in       |Discusses the plug-in tasks that are       |
|operations tasks  |available within the context of a          |
|                  |particular plug-in.                        |
+------------------+-------------------------------------------+
|21. Deleting      |Tells how to safely delete EVMS objects.   |
|objects           |                                           |
+------------------+-------------------------------------------+
|22. Replacing     |Tells how to change the configuration of a |
|objects           |volume or storage object.                  |
+------------------+-------------------------------------------+
|23. Moving segment|Discusses how to use the move function for |
|storage objects   |moving segments.                           |
+------------------+-------------------------------------------+
|A. The DOS plug-in|Provides details about the DOS plug-in,    |
|                  |which is a segment manager plug-in.        |
+------------------+-------------------------------------------+
|B. The MD region  |Explains the Multiple Disks (MD) support in|
|manager           |Linux that is a software implementation of |
|                  |RAID.                                      |
+------------------+-------------------------------------------+
|C. The LVM plug-in|Tells how the LVM plug-in is implemented   |
|                  |and how to perform container operations.   |
+------------------+-------------------------------------------+
|D. The LVM2       |Tells how the LVM2 plug-in is implemented  |
|plug-in           |and how to perform container operations on |
|                  |LVM2 containers.                           |
+------------------+-------------------------------------------+
|E. The CSM plug-in|Explains how the Cluster Segment Manager   |
|                  |(CSM) plug-in is implemented and how to    |
|                  |perform CSM operations.                    |
+------------------+-------------------------------------------+
|F. JFS file system|Provides information about the JFS FSIM.   |
|interface module  |                                           |
+------------------+-------------------------------------------+
|G. XFS file system|Provides information about the XFS FSIM.   |
|interface module  |                                           |
+------------------+-------------------------------------------+
|H. ReiserFS file  |Provides information about the ReiserFS    |
|system interface  |FSIM.                                      |
|module            |                                           |
+------------------+-------------------------------------------+
|I. Ext-2/3 file   |Provides information about the Ext-2/3     |
|system interface  |FSIM.                                      |
|module            |                                           |
+------------------+-------------------------------------------+
|J. OpenGFS file   |Provides information about the OpenGFS     |
|system interface  |FSIM.                                      |
|module            |                                           |
+------------------+-------------------------------------------+
|K. NTFS file      |Provides information about the NTFS FSIM.  |
|system interface  |                                           |
|module            |                                           |
+------------------+-------------------------------------------+
-----------------------------------------------------------------------------

Chapter 1. What is EVMS?

EVMS brings a new model of volume management to Linux�. EVMS integrates all
aspects of volume management, such as disk partitioning, Linux logical volume
manager (LVM) and multi-disk (MD) management, and file system operations into
a single cohesive package. With EVMS, various volume management technologies
are accessible through one interface, and new technologies can be added as
plug-ins as they are developed.
-----------------------------------------------------------------------------

1.1. Why choose EVMS?

EVMS lets you manage storage space in a way that is more intuitive and
flexible than many other Linux volume management systems. Practical tasks,
such as migrating disks or adding new disks to your Linux system, become more
manageable with EVMS because EVMS can recognize and read from different
volume types and file systems. EVMS provides additional safety controls by
not allowing commands that are unsafe. These controls help maintain the
integrity of the data stored on the system.

You can use EVMS to create and manage data storage. With EVMS, you can use
multiple volume management technologies under one framework while ensuring
your system still interacts correctly with stored data. With EVMS, you are
can use drive linking, shrink and expand volumes, create snapshots of your
volumes, and set up RAID (redundant array of independent devices) features
for your system. You can also use many types of file systems and manipulate
these storage pieces in ways that best meet the needs of your particular work
environment.

EVMS also provides the capability to manage data on storage that is
physically shared by nodes in a cluster. This shared storage allows data to
be highly available from different nodes in the cluster.
-----------------------------------------------------------------------------

1.2. The EVMS user interfaces

There are currently three user interfaces available for EVMS: graphical
(GUI), text mode (Ncurses), and the Command Line Interpreter (CLI).
Additionally, you can use the EVMS Application Programming Interface to
implement your own customized user interface.

Table 1-1 tells more about each of the EVMS user interfaces.


Table 1-1. EVMS user interfaces
+------------+------------------+------------+------------------------------+
|User        |Typical user      |Types of use|Function                      |
|interface   |                  |            |                              |
+------------+------------------+------------+------------------------------+
|GUI         |All               |All uses    |Allows you to choose from     |
|            |                  |except      |available options only,       |
|            |                  |automation  |instead of having to sort     |
|            |                  |            |through all the options,      |
|            |                  |            |including ones that are not   |
|            |                  |            |available at that point in the|
|            |                  |            |process.                      |
+------------+------------------+------------+------------------------------+
|Ncurses     |Users who don't   |All uses    |Allows you to choose from     |
|            |have GTK libraries|except      |available options only,       |
|            |or X Window       |automation  |instead of having to sort     |
|            |Systems on their  |            |through all the options,      |
|            |machines          |            |including ones that are not   |
|            |                  |            |available at that point in the|
|            |                  |            |process.                      |
+------------+------------------+------------+------------------------------+
|Command Line|Expert            |All uses    |Allows easy automation of     |
|            |                  |            |tasks                         |
+------------+------------------+------------+------------------------------+
-----------------------------------------------------------------------------

1.3. EVMS terminology

To avoid confusion with other terms that describe volume management in
general, EVMS uses a specific set of terms. These terms are listed, from most
fundamental to most comprehensive, as follows:

Logical disk
    Representation of anything EVMS can access as a physical disk. In EVMS,
    physical disks are logical disks.

Sector
    The lowest level of addressability on a block device. This definition is
    in keeping with the standard meaning found in other management systems.

Disk segment
    An ordered set of physically contiguous sectors residing on the same
    storage object. The general analogy for a segment is to a traditional
    disk partition, such as DOS or OS/2 �

Storage region
    An ordered set of logically contiguous sectors that are not necessarily
    physically contiguous.

Storage object
    Any persistent memory structure in EVMS that can be used to build objects
    or create a volume. Storage object is a generic term for disks, segments,
    regions, and feature objects.

Storage container
    A collection of storage objects. A storage container consumes one set of
    storage objects and produces new storage objects. One common subset of
    storage containers is volume groups, such as AIX� or LVM.

    Storage containers can be either of type private or cluster.

Cluster storage container
    Specialized storage containers that consume only disk objects that are
    physically accessible from all nodes of a cluster.

    Private storage container
        A collection of disks that are physically accessible from all nodes
        of a cluster, managed as a single pool of storage, and owned and
        accessed by a single node of the cluster at any given time.

    Shared storage container
        A collection of disks that are physically accessible from all nodes
        of a cluster, managed as a single pool of storage, and owned and
        accessed by all nodes of the cluster simultaneously.

    Deported storage container
        A shared cluster container that is not owned by any node of the
        cluster.



Feature object
    A storage object that contains an EVMS native feature.

    An EVMS Native Feature is a function of volume management designed and
    implemented by EVMS. These features are not intended to be backward
    compatible with other volume management technologies.

Logical volume
    A volume that consumes a storage object and exports something mountable.
    There are two varieties of logical volumes: EVMS Volumes and
    Compatibility volumes.

    EVMS Volumes contain EVMS native metadata and can support all EVMS
    features. /dev/evms/my_volume would be an example of an EVMS Volume.

    Compatibility volumes do not contain any EVMS native metadata.
    Compatibility volumes are backward compatible to their particular scheme,
    but they cannot support EVMS features. /dev/evms/md/md0 would be an
    example of a compatibility volume.


-----------------------------------------------------------------------------
1.4. What makes EVMS so flexible?

There are numerous drivers in the Linux kernel, such as Device Mapper and MD
(software RAID), that implement volume management schemes. EVMS is built on
top of these drivers to provide one framework for combining and accessing the
capabilities.
