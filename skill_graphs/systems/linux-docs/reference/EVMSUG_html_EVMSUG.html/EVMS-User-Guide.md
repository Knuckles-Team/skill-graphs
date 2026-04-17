#  EVMS User Guide
###  Christine Lorenz
IBM

###  Joy Goodreau
IBM

###  Kylie Smith
IBM

Copyright © 2004 IBM
September 16, 2004

**Special Notices**
The following terms are registered trademarks of International Business Machines corporation in the United States and/or other countries: AIX, OS/2, System/390. A full list of U.S. trademarks owned by IBM may be found at
Intel is a trademark or registered trademark of Intel Corporation in the United States, other countries, or both.
Windows is a trademark of Microsoft Corporation in the United States, other countries, or both.
Linux is a trademark of Linus Torvalds.
UNIX is a registered trademark of The Open Group in the United States and other countries.
Other company, product, and service names may be trademarks or service marks of others.
This document is provided "AS IS," with no express or implied warranties. Use the information in this document at your own risk.
**License Information**
This document may be reproduced or distributed in any form without prior permission provided the copyright notice is retained on all copies. Modified versions of this document may be freely distributed provided that they are clearly identified as such, and this copyright is included intact.
* * *

**Table of Contents**


[Preface](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#userguidepref)


1. [What is EVMS?](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#intro)


1.1. [Why choose EVMS?](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#cando)


1.2. [The EVMS user interfaces](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#uis)


1.3. [EVMS terminology](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#terminology)


1.4. [What makes EVMS so flexible?](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN262)


1.5. [Plug-in layer definitions](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#LAYERDEF)


2. [Using the EVMS interfaces](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmscmuse)


2.1. [EVMS GUI](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#GUI)


2.2. [EVMS Ncurses interface](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#NCURSES)


2.3. [EVMS Command Line Interpreter](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#COMMANDLINE)


3. [The EVMS log file and error data collection](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#debuglevels)


3.1. [About the EVMS log file](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#FSIMsupp)


3.2. [Log file logging levels](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#loglevels)


3.3. [Specifying the logging levels](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#specifylevels)


4. [Viewing compatibility volumes after migrating](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmsmigrate)


4.1. [Using the EVMS GUI](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#guimigrate)


4.2. [Using Ncurses](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#ncurmigrate)


4.3. [Using the CLI](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#climigrate)


5. [Obtaining interface display details](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#displaydetails)


5.1. [Using the EVMS GUI](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#displaygui)


5.2. [Using Ncurses](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#displaydatancurses)


5.3. [Using the CLI](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN812)


6. [Adding and removing a segment manager](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmsassignseg)


6.1. [When to add a segment manager](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#whenassign)


6.2. [Types of segment managers](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#smtypes)


6.3. [Adding a segment manager to an existing disk](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#assignsegex)


6.4. [Adding a segment manager to a new disk](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#assignsegnew)


6.5. [Example: add a segment manager](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#assignex)


6.6. [Removing a segment manager](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#removeseg)


6.7. [Example: remove a segment manager](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#rmvex)


7. [Creating segments](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmscreateseg)


7.1. [When to create a segment](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#whyseg)


7.2. [Example: create a segment](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#crsegex)


8. [Creating a container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmscreatecont)


8.1. [When to create a container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#whencont)


8.2. [Example: create a container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#context)


9. [Creating regions](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmscreatereg)


9.1. [When to create regions](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1320)


9.2. [Example: create a region](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#crregex)


10. [Creating drive links](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmscreatedrivelinking)


10.1. [What is drive linking?](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#whatisdrivelinking)


10.2. [How drive linking is implemented](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#howimp)


10.3. [Creating a drive link](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1453)


10.4. [Example: create a drive link](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#drivelinkex)


10.5. [Expanding a drive link](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#expandpartitions)


10.6. [Shrinking a drive link](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#shrinkdrivelink)


10.7. [Deleting a drive link](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#deletedrivelink)


11. [Creating snapshots](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmscreatesnap)


11.1. [What is a snapshot?](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#whatissnapshotting)


11.2. [Creating snapshot objects](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#createactivsnap)


11.3. [Example: create a snapshot](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#snapshotex)


11.4. [Reinitializing a snapshot](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1717)


11.5. [Expanding a snapshot](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1775)


11.6. [Deleting a snapshot](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1843)


11.7. [Rolling back a snapshot](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1847)


12. [Creating volumes](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmscreatevol)


12.1. [When to create a volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1913)


12.2. [Example: create an EVMS native volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#crvolexcomp)


12.3. [Example: create a compatibility volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#crvolexevms)


13. [FSIMs and file system operations](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmsfsimops)


13.1. [The FSIMs supported by EVMS](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#FSIMsuppevms)


13.2. [Example: add a file system to a volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#fsimmkfs)


13.3. [Example: check a file system](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#fsimmkfsaex)


14. [Clustering operations](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#clusterops)


14.1. [Rules and restrictions for creating cluster containers](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2372)


14.2. [Example: create a private cluster container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2382)


14.3. [Example: create a shared cluster container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2496)


14.4. [Example: convert a private container to a shared container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2604)


14.5. [Example: convert a shared container to a private container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2688)


14.6. [Example: deport a private or shared container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2773)


14.7. [Deleting a cluster container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2849)


14.8. [Failover and Failback of a private container on Linux-HA](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2853)


14.9. [Remote configuration management](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2896)


14.10. [Forcing a cluster container to be active](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2946)


15. [Converting volumes](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmsconvert)


15.1. [When to convert volumes](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2974)


15.2. [Example: convert compatibility volumes to EVMS volumes](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#comptoevms)


15.3. [Example: convert EVMS volumes to compatibility volumes](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmstocomp)


16. [Expanding and shrinking volumes](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#expandshrink)


16.1. [Why expand and shrink volumes?](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#whyexpandshrink)


16.2. [Example: shrink a volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#exshrink)


16.3. [Example: expand a volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#mkfs)


17. [Adding features to an existing volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#addfeatures)


17.1. [Why add features to a volume?](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#whyadd)


17.2. [Example: add drive linking to an existing volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#exaddfeature)


18. [Selectively activating volumes and objects](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#selectact)


18.1. [Initial activation using /etc/evms.conf](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#initialactivation)


18.2. [Activating and deactivating volumes and objects](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN3528)


19. [Mounting and unmounting volumes from within EVMS](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#mountunmount)


19.1. [Mounting a volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#mntvol)


19.2. [Unmounting a volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN3804)


19.3. [The SWAPFS file system](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN3863)


20. [Plug-in operations tasks](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#plugintasks)


20.1. [What are plug-in tasks?](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#aboutplugintasks)


20.2. [Example: complete a plug-in operations task](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#pluginexample)


21. [Deleting objects](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#deleterecurs)


21.1. [How to delete objects: delete and delete recursive](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#howtodel)


21.2. [Example: perform a delete recursive operation](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#examdelrecur)


22. [Replacing objects](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#evmsreplaceobjects)


22.1. [What is object-replace?](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#whatisobjectreplace)


22.2. [Replacing a drive-link child object](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#replacedlchildobj)


23. [Moving segment storage objects](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#segstorobjs)


23.1. [What is segment moving?](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#segmovewhatis)


23.2. [Why move a segment?](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#whymove)


23.3. [Which segment manager plug-ins implement the move function?](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN4331)


23.4. [Example: move a DOS segment](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#movesegex)


A. [The DOS plug-in](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#appxdos)


A.1. [How the DOS plug-in is implemented](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#DOShow)


A.2. [Assigning the DOS plug-in](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#assignDOS)


A.3. [Creating DOS partitions](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#creatingDOS)


A.4. [Expanding DOS partitions](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#expandDOS)


A.5. [Shrinking DOS partitions](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#shrinkDOS)


A.6. [Deleting partitions](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#deleteDOS)


B. [The MD region manager](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#appxmdreg)


B.1. [Characteristics of Linux RAID levels](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#characraidlvls)


B.2. [Creating an MD region](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#createmdreg)


B.3. [Active and spare objects](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#activepsareobjs)


B.4. [Faulty objects](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#faultobjs)


B.5. [Resizing MD regions](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#resizemdreg)


B.6. [Replacing objects](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#replaceobjs)


C. [The LVM plug-in](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#appxlvm)


C.1. [How LVM is implemented](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#lvmimp)


C.2. [Container operations](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#containerops)


C.3. [Region operations](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN4759)


D. [The LVM2 plug-in](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#appxlvm2)


D.1. [Container operations](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#contops)


D.2. [Region operations](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#regionops)


E. [The CSM plug-in](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#appxcsm)


E.1. [Assigning the CSM plug-in](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#csmassn)


E.2. [Unassigning the CSM plug-in](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#unassignCSM)


E.3. [Deleting a CSM container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN5078)


F. [JFS file system interface module](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#jfsfsim)


F.1. [Creating JFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#createjfsfsim)


F.2. [Checking JFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#checkjfsfsim)


F.3. [Removing JFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#removejfsfsim)


F.4. [Expanding JFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#expandjfsfsim)


F.5. [Shrinking JFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#shrinkjfsfsim)


G. [XFS file system interface module](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#xfsfsim)


G.1. [Creating XFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#createxfsfsim)


G.2. [Checking XFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#checkxfsfsim)


G.3. [Removing XFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#removexfsfsim)


G.4. [Expanding XFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#expandxfsfsim)


G.5. [Shrinking XFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#shrinkxfsfsim)


H. [ReiserFS file system interface module](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#reiserfsim)


H.1. [Creating ReiserFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#createreiserfsim)


H.2. [Checking ReiserFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#checkreiserfsim)


H.3. [Removing ReiserFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#removexreiserfsim)


H.4. [Expanding ReiserFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#expandreiserFSfsim)


H.5. [Shrinking ReiserFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#shrinkreiserfsim)


I. [Ext-2/3 file system interface module](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#ext23fsim)


I.1. [Creating Ext-2/3 file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#createext23fsim)


I.2. [Checking Ext-2/3 file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#checkext23fsim)


I.3. [Removing Ext-2/3 file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#removeext23fsim)


I.4. [Expanding and shrinking Ext-2/3 file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#expandshrinkext23fsim)


J. [OpenGFS file system interface module](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#gfsfsim)


J.1. [Creating OpenGFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#createopengfsfsim)


J.2. [Checking OpenGFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#checkopengfsfsim)


J.3. [Removing OpenGFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#removeopengfsfsim)


J.4. [Expanding and shrinking OpenGFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#expandshrinkopengfsfsim)


K. [NTFS file system interface module](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#ntfsfsim)


K.1. [Creating NTFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#createntfsfsim)


K.2. [Fixing NTFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#fixntfsfsim)


K.3. [Cloning NTFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#clonentfsfsim)


K.4. [Removing NTFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#removentfsfsim)


K.5. [Expanding and shrinking NTFS file systems](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#expandshrinkntfsfsim)


**List of Tables**


1. [Organization of the EVMS User Guide](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#bookorg)


1-1. [EVMS user interfaces](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#userinterf)


2-1. [Accelerator keys in the Main Window](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN370)


2-2. [Accelerator keys in the views](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN384)


2-3. [Accelerator keys in the selection window](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN430)


2-4. [Accelerator keys in the configuration options window](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN454)


2-5. [Widget navigation keys in the configuration options window](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN476)


3-1. [EVMS logging levels](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN645)


16-1. [FSIM support for expand and shrink operations](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN3141)


**List of Figures**


4-1. [GUI start-up window](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN726)


4-2. [Ncurses start-up window](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN737)


4-3. [CLI volume query results](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN756)


**List of Examples**


6-1. [Add the DOS Segment Manager](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN929)


6-2. [Remove the DOS Segment Manager](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1049)


7-1. [Create a 100MB segment](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1122)


8-1. [Create "Sample Container"](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1231)


9-1. [Create "Sample Region"](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1327)


10-1. [Create a drive link](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1461)


11-1. [Create a snapshot of a volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1607)


12-1. [Create an EVMS native volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN1923)


12-2. [Create a compatibility volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2001)


13-1. [Add a JFS File System to a Volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2167)


13-2. [Check a JFS File System](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2277)


14-1. [Create a private cluster container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2386)


14-2. [Create a shared cluster container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2500)


14-3. [Convert a private container to shared](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2608)


14-4. [Convert a shared container to private](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2692)


14-5. [Deport a cluster container](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2777)


15-1. [Convert a compatibility volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN2988)


15-2. [Convert an EVMS volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN3066)


16-1. [Shrink a volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN3186)


16-2. [Expand a volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN3297)


17-1. [Add drive linking to an existing volume](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN3410)


20-1. [Add a spare disk to a compatibility volume made from an MDRaid5 region](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN4012)


21-1. [Destroy a volume and the region and container below it](https://tldp.org/LDP/EVMSUG/html/EVMSUG.html#AEN4143)

* * *
