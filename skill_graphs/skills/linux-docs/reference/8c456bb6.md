#  Preface
This guide tells how to configure and manage Enterprise Volume Management System (EVMS). EVMS is a storage management program that provides a single framework for managing and administering your system's storage.
This guide is intended for Linux system administrators and users who are responsible for setting up and maintaining EVMS.
For additional information about EVMS or to ask questions specific to your distribution, refer to the EVMS mailing lists. You can view the list archives or subscribe to the lists from the
The following table shows how this guide is organized:
**Table 1. Organization of the EVMS User Guide**
Chapter or appendix title | Contents
---|---
1. What is EVMS? | Discusses general EVMS concepts and terms.
2. Using the EVMS interfaces | Describes the three EVMS user interfaces and how to use them.
3. The EVMS log file and error data collection | Discusses the EVMS information and error log file and explains how to change the logging level.
4. Viewing compatibility volumes after migrating | Tells how to view existing files that have been migrated to EVMS.
5. Obtaining interface display details | Tells how to view detailed information about EVMS objects.
6. Adding and removing a segment manager | Discusses segments and explains how to add and remove a segment manager.
7. Creating segments | Explains when and how to create segments.
8. Creating containers | Discusses containers and explains when and how to create them.
9. Creating regions | Discusses regions and explains when and how to create them.
10. Creating drive links | Discusses the drive linking feature and tells how to create a drive link.
11. Creating snapshots | Discusses snapshotting and tells how to create a snapshot.
12. Creating volumes | Explains when and how to create volumes.
13. FSIMs and file system operations | Discusses the standard FSIMs shipped with EVMS and provides examples of adding file systems and coordinating file checks with the FSIMs.
14. Clustering operations | Describes EVMS clustering and how to create private and shared containers.
15. Converting volumes | Explains how to convert EVMS native volumes to compatibility volumes and compatibility volumes to EVMS native volumes.
16. Expanding and shrinking volumes | Tells how to expand and shrink EVMS volumes with the various EVMS user interfaces.
17. Adding features to an existing volume | Tells how to add additional features, such as drive linking, to an existing volume.
18. Selectively activating volumes and objects | Explains how to selectively activate and deactivate volumes and options.
19. Mounting and unmounting volumes from within EVMS. | Tells how to have EVMS mount and unmount volumes so you do not have to open a separate terminal session.
20. Plug-in operations tasks | Discusses the plug-in tasks that are available within the context of a particular plug-in.
21. Deleting objects | Tells how to safely delete EVMS objects.
22. Replacing objects | Tells how to change the configuration of a volume or storage object.
23. Moving segment storage objects | Discusses how to use the move function for moving segments.
A. The DOS plug-in | Provides details about the DOS plug-in, which is a segment manager plug-in.
B. The MD region manager | Explains the Multiple Disks (MD) support in Linux that is a software implementation of RAID.
C. The LVM plug-in | Tells how the LVM plug-in is implemented and how to perform container operations.
D. The LVM2 plug-in | Tells how the LVM2 plug-in is implemented and how to perform container operations on LVM2 containers.
E. The CSM plug-in | Explains how the Cluster Segment Manager (CSM) plug-in is implemented and how to perform CSM operations.
F. JFS file system interface module | Provides information about the JFS FSIM.
G. XFS file system interface module | Provides information about the XFS FSIM.
H. ReiserFS file system interface module | Provides information about the ReiserFS FSIM.
I. Ext-2/3 file system interface module | Provides information about the Ext-2/3 FSIM.
J. OpenGFS file system interface module | Provides information about the OpenGFS FSIM.
K. NTFS file system interface module | Provides information about the NTFS FSIM.
* * *
