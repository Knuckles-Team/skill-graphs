#  EVMS User Guide
###  Christine Lorenz
IBM

###  Joy Goodreau
IBM

###  Kylie Smith
IBM

[Copyright](https://tldp.org/LDP/EVMSUG/html/ln24.html) © 2004 IBM
September 16, 2004

* * *

**Table of Contents**


[Preface](https://tldp.org/LDP/EVMSUG/html/userguidepref.html)


1. [What is EVMS?](https://tldp.org/LDP/EVMSUG/html/intro.html)


1.1. [Why choose EVMS?](https://tldp.org/LDP/EVMSUG/html/cando.html)


1.2. [The EVMS user interfaces](https://tldp.org/LDP/EVMSUG/html/uis.html)


1.3. [EVMS terminology](https://tldp.org/LDP/EVMSUG/html/terminology.html)


1.4. [What makes EVMS so flexible?](https://tldp.org/LDP/EVMSUG/html/x262.html)


1.5. [Plug-in layer definitions](https://tldp.org/LDP/EVMSUG/html/layerdef.html)


2. [Using the EVMS interfaces](https://tldp.org/LDP/EVMSUG/html/evmscmuse.html)


2.1. [EVMS GUI](https://tldp.org/LDP/EVMSUG/html/gui.html)


2.2. [EVMS Ncurses interface](https://tldp.org/LDP/EVMSUG/html/ncurses.html)


2.3. [EVMS Command Line Interpreter](https://tldp.org/LDP/EVMSUG/html/commandline.html)


3. [The EVMS log file and error data collection](https://tldp.org/LDP/EVMSUG/html/debuglevels.html)


3.1. [About the EVMS log file](https://tldp.org/LDP/EVMSUG/html/fsimsupp.html)


3.2. [Log file logging levels](https://tldp.org/LDP/EVMSUG/html/loglevels.html)


3.3. [Specifying the logging levels](https://tldp.org/LDP/EVMSUG/html/specifylevels.html)


4. [Viewing compatibility volumes after migrating](https://tldp.org/LDP/EVMSUG/html/evmsmigrate.html)


4.1. [Using the EVMS GUI](https://tldp.org/LDP/EVMSUG/html/guimigrate.html)


4.2. [Using Ncurses](https://tldp.org/LDP/EVMSUG/html/ncurmigrate.html)


4.3. [Using the CLI](https://tldp.org/LDP/EVMSUG/html/climigrate.html)


5. [Obtaining interface display details](https://tldp.org/LDP/EVMSUG/html/displaydetails.html)


5.1. [Using the EVMS GUI](https://tldp.org/LDP/EVMSUG/html/displaygui.html)


5.2. [Using Ncurses](https://tldp.org/LDP/EVMSUG/html/displaydatancurses.html)


5.3. [Using the CLI](https://tldp.org/LDP/EVMSUG/html/x812.html)


6. [Adding and removing a segment manager](https://tldp.org/LDP/EVMSUG/html/evmsassignseg.html)


6.1. [When to add a segment manager](https://tldp.org/LDP/EVMSUG/html/whenassign.html)


6.2. [Types of segment managers](https://tldp.org/LDP/EVMSUG/html/smtypes.html)


6.3. [Adding a segment manager to an existing disk](https://tldp.org/LDP/EVMSUG/html/assignsegex.html)


6.4. [Adding a segment manager to a new disk](https://tldp.org/LDP/EVMSUG/html/assignsegnew.html)


6.5. [Example: add a segment manager](https://tldp.org/LDP/EVMSUG/html/assignex.html)


6.6. [Removing a segment manager](https://tldp.org/LDP/EVMSUG/html/removeseg.html)


6.7. [Example: remove a segment manager](https://tldp.org/LDP/EVMSUG/html/rmvex.html)


7. [Creating segments](https://tldp.org/LDP/EVMSUG/html/evmscreateseg.html)


7.1. [When to create a segment](https://tldp.org/LDP/EVMSUG/html/whyseg.html)


7.2. [Example: create a segment](https://tldp.org/LDP/EVMSUG/html/crsegex.html)


8. [Creating a container](https://tldp.org/LDP/EVMSUG/html/evmscreatecont.html)


8.1. [When to create a container](https://tldp.org/LDP/EVMSUG/html/whencont.html)


8.2. [Example: create a container](https://tldp.org/LDP/EVMSUG/html/context.html)


9. [Creating regions](https://tldp.org/LDP/EVMSUG/html/evmscreatereg.html)


9.1. [When to create regions](https://tldp.org/LDP/EVMSUG/html/x1320.html)


9.2. [Example: create a region](https://tldp.org/LDP/EVMSUG/html/crregex.html)


10. [Creating drive links](https://tldp.org/LDP/EVMSUG/html/evmscreatedrivelinking.html)


10.1. [What is drive linking?](https://tldp.org/LDP/EVMSUG/html/whatisdrivelinking.html)


10.2. [How drive linking is implemented](https://tldp.org/LDP/EVMSUG/html/howimp.html)


10.3. [Creating a drive link](https://tldp.org/LDP/EVMSUG/html/x1453.html)


10.4. [Example: create a drive link](https://tldp.org/LDP/EVMSUG/html/drivelinkex.html)


10.5. [Expanding a drive link](https://tldp.org/LDP/EVMSUG/html/expandpartitions.html)


10.6. [Shrinking a drive link](https://tldp.org/LDP/EVMSUG/html/shrinkdrivelink.html)


10.7. [Deleting a drive link](https://tldp.org/LDP/EVMSUG/html/deletedrivelink.html)


11. [Creating snapshots](https://tldp.org/LDP/EVMSUG/html/evmscreatesnap.html)


11.1. [What is a snapshot?](https://tldp.org/LDP/EVMSUG/html/whatissnapshotting.html)


11.2. [Creating snapshot objects](https://tldp.org/LDP/EVMSUG/html/createactivsnap.html)


11.3. [Example: create a snapshot](https://tldp.org/LDP/EVMSUG/html/snapshotex.html)


11.4. [Reinitializing a snapshot](https://tldp.org/LDP/EVMSUG/html/x1717.html)


11.5. [Expanding a snapshot](https://tldp.org/LDP/EVMSUG/html/x1775.html)


11.6. [Deleting a snapshot](https://tldp.org/LDP/EVMSUG/html/x1843.html)


11.7. [Rolling back a snapshot](https://tldp.org/LDP/EVMSUG/html/x1847.html)


12. [Creating volumes](https://tldp.org/LDP/EVMSUG/html/evmscreatevol.html)


12.1. [When to create a volume](https://tldp.org/LDP/EVMSUG/html/x1913.html)


12.2. [Example: create an EVMS native volume](https://tldp.org/LDP/EVMSUG/html/crvolexcomp.html)


12.3. [Example: create a compatibility volume](https://tldp.org/LDP/EVMSUG/html/crvolexevms.html)


13. [FSIMs and file system operations](https://tldp.org/LDP/EVMSUG/html/evmsfsimops.html)


13.1. [The FSIMs supported by EVMS](https://tldp.org/LDP/EVMSUG/html/fsimsuppevms.html)


13.2. [Example: add a file system to a volume](https://tldp.org/LDP/EVMSUG/html/fsimmkfs.html)


13.3. [Example: check a file system](https://tldp.org/LDP/EVMSUG/html/fsimmkfsaex.html)


14. [Clustering operations](https://tldp.org/LDP/EVMSUG/html/clusterops.html)


14.1. [Rules and restrictions for creating cluster containers](https://tldp.org/LDP/EVMSUG/html/x2372.html)


14.2. [Example: create a private cluster container](https://tldp.org/LDP/EVMSUG/html/x2382.html)


14.3. [Example: create a shared cluster container](https://tldp.org/LDP/EVMSUG/html/x2496.html)


14.4. [Example: convert a private container to a shared container](https://tldp.org/LDP/EVMSUG/html/x2604.html)


14.5. [Example: convert a shared container to a private container](https://tldp.org/LDP/EVMSUG/html/x2688.html)


14.6. [Example: deport a private or shared container](https://tldp.org/LDP/EVMSUG/html/x2773.html)


14.7. [Deleting a cluster container](https://tldp.org/LDP/EVMSUG/html/x2849.html)


14.8. [Failover and Failback of a private container on Linux-HA](https://tldp.org/LDP/EVMSUG/html/x2853.html)


14.9. [Remote configuration management](https://tldp.org/LDP/EVMSUG/html/x2896.html)


14.10. [Forcing a cluster container to be active](https://tldp.org/LDP/EVMSUG/html/x2946.html)


15. [Converting volumes](https://tldp.org/LDP/EVMSUG/html/evmsconvert.html)


15.1. [When to convert volumes](https://tldp.org/LDP/EVMSUG/html/x2974.html)


15.2. [Example: convert compatibility volumes to EVMS volumes](https://tldp.org/LDP/EVMSUG/html/comptoevms.html)


15.3. [Example: convert EVMS volumes to compatibility volumes](https://tldp.org/LDP/EVMSUG/html/evmstocomp.html)


16. [Expanding and shrinking volumes](https://tldp.org/LDP/EVMSUG/html/expandshrink.html)


16.1. [Why expand and shrink volumes?](https://tldp.org/LDP/EVMSUG/html/whyexpandshrink.html)


16.2. [Example: shrink a volume](https://tldp.org/LDP/EVMSUG/html/exshrink.html)


16.3. [Example: expand a volume](https://tldp.org/LDP/EVMSUG/html/mkfs.html)


17. [Adding features to an existing volume](https://tldp.org/LDP/EVMSUG/html/addfeatures.html)


17.1. [Why add features to a volume?](https://tldp.org/LDP/EVMSUG/html/whyadd.html)


17.2. [Example: add drive linking to an existing volume](https://tldp.org/LDP/EVMSUG/html/exaddfeature.html)


18. [Selectively activating volumes and objects](https://tldp.org/LDP/EVMSUG/html/selectact.html)


18.1. [Initial activation using /etc/evms.conf](https://tldp.org/LDP/EVMSUG/html/initialactivation.html)


18.2. [Activating and deactivating volumes and objects](https://tldp.org/LDP/EVMSUG/html/x3528.html)


19. [Mounting and unmounting volumes from within EVMS](https://tldp.org/LDP/EVMSUG/html/mountunmount.html)


19.1. [Mounting a volume](https://tldp.org/LDP/EVMSUG/html/mntvol.html)


19.2. [Unmounting a volume](https://tldp.org/LDP/EVMSUG/html/x3804.html)


19.3. [The SWAPFS file system](https://tldp.org/LDP/EVMSUG/html/x3863.html)


20. [Plug-in operations tasks](https://tldp.org/LDP/EVMSUG/html/plugintasks.html)


20.1. [What are plug-in tasks?](https://tldp.org/LDP/EVMSUG/html/aboutplugintasks.html)


20.2. [Example: complete a plug-in operations task](https://tldp.org/LDP/EVMSUG/html/pluginexample.html)


21. [Deleting objects](https://tldp.org/LDP/EVMSUG/html/deleterecurs.html)


21.1. [How to delete objects: delete and delete recursive](https://tldp.org/LDP/EVMSUG/html/howtodel.html)


21.2. [Example: perform a delete recursive operation](https://tldp.org/LDP/EVMSUG/html/examdelrecur.html)


22. [Replacing objects](https://tldp.org/LDP/EVMSUG/html/evmsreplaceobjects.html)


22.1. [What is object-replace?](https://tldp.org/LDP/EVMSUG/html/whatisobjectreplace.html)


22.2. [Replacing a drive-link child object](https://tldp.org/LDP/EVMSUG/html/replacedlchildobj.html)


23. [Moving segment storage objects](https://tldp.org/LDP/EVMSUG/html/segstorobjs.html)


23.1. [What is segment moving?](https://tldp.org/LDP/EVMSUG/html/segmovewhatis.html)


23.2. [Why move a segment?](https://tldp.org/LDP/EVMSUG/html/whymove.html)


23.3. [Which segment manager plug-ins implement the move function?](https://tldp.org/LDP/EVMSUG/html/x4331.html)


23.4. [Example: move a DOS segment](https://tldp.org/LDP/EVMSUG/html/movesegex.html)


A. [The DOS plug-in](https://tldp.org/LDP/EVMSUG/html/appxdos.html)


A.1. [How the DOS plug-in is implemented](https://tldp.org/LDP/EVMSUG/html/doshow.html)


A.2. [Assigning the DOS plug-in](https://tldp.org/LDP/EVMSUG/html/assigndos.html)


A.3. [Creating DOS partitions](https://tldp.org/LDP/EVMSUG/html/creatingdos.html)


A.4. [Expanding DOS partitions](https://tldp.org/LDP/EVMSUG/html/expanddos.html)


A.5. [Shrinking DOS partitions](https://tldp.org/LDP/EVMSUG/html/shrinkdos.html)


A.6. [Deleting partitions](https://tldp.org/LDP/EVMSUG/html/deletedos.html)


B. [The MD region manager](https://tldp.org/LDP/EVMSUG/html/appxmdreg.html)


B.1. [Characteristics of Linux RAID levels](https://tldp.org/LDP/EVMSUG/html/characraidlvls.html)


B.2. [Creating an MD region](https://tldp.org/LDP/EVMSUG/html/createmdreg.html)


B.3. [Active and spare objects](https://tldp.org/LDP/EVMSUG/html/activepsareobjs.html)


B.4. [Faulty objects](https://tldp.org/LDP/EVMSUG/html/faultobjs.html)


B.5. [Resizing MD regions](https://tldp.org/LDP/EVMSUG/html/resizemdreg.html)


B.6. [Replacing objects](https://tldp.org/LDP/EVMSUG/html/replaceobjs.html)


C. [The LVM plug-in](https://tldp.org/LDP/EVMSUG/html/appxlvm.html)


C.1. [How LVM is implemented](https://tldp.org/LDP/EVMSUG/html/lvmimp.html)


C.2. [Container operations](https://tldp.org/LDP/EVMSUG/html/containerops.html)


C.3. [Region operations](https://tldp.org/LDP/EVMSUG/html/x4759.html)


D. [The LVM2 plug-in](https://tldp.org/LDP/EVMSUG/html/appxlvm2.html)


D.1. [Container operations](https://tldp.org/LDP/EVMSUG/html/contops.html)


D.2. [Region operations](https://tldp.org/LDP/EVMSUG/html/regionops.html)


E. [The CSM plug-in](https://tldp.org/LDP/EVMSUG/html/appxcsm.html)


E.1. [Assigning the CSM plug-in](https://tldp.org/LDP/EVMSUG/html/csmassn.html)


E.2. [Unassigning the CSM plug-in](https://tldp.org/LDP/EVMSUG/html/unassigncsm.html)


E.3. [Deleting a CSM container](https://tldp.org/LDP/EVMSUG/html/x5078.html)


F. [JFS file system interface module](https://tldp.org/LDP/EVMSUG/html/jfsfsim.html)


F.1. [Creating JFS file systems](https://tldp.org/LDP/EVMSUG/html/createjfsfsim.html)


F.2. [Checking JFS file systems](https://tldp.org/LDP/EVMSUG/html/checkjfsfsim.html)


F.3. [Removing JFS file systems](https://tldp.org/LDP/EVMSUG/html/removejfsfsim.html)


F.4. [Expanding JFS file systems](https://tldp.org/LDP/EVMSUG/html/expandjfsfsim.html)


F.5. [Shrinking JFS file systems](https://tldp.org/LDP/EVMSUG/html/shrinkjfsfsim.html)


G. [XFS file system interface module](https://tldp.org/LDP/EVMSUG/html/xfsfsim.html)


G.1. [Creating XFS file systems](https://tldp.org/LDP/EVMSUG/html/createxfsfsim.html)


G.2. [Checking XFS file systems](https://tldp.org/LDP/EVMSUG/html/checkxfsfsim.html)


G.3. [Removing XFS file systems](https://tldp.org/LDP/EVMSUG/html/removexfsfsim.html)


G.4. [Expanding XFS file systems](https://tldp.org/LDP/EVMSUG/html/expandxfsfsim.html)


G.5. [Shrinking XFS file systems](https://tldp.org/LDP/EVMSUG/html/shrinkxfsfsim.html)


H. [ReiserFS file system interface module](https://tldp.org/LDP/EVMSUG/html/reiserfsim.html)


H.1. [Creating ReiserFS file systems](https://tldp.org/LDP/EVMSUG/html/createreiserfsim.html)


H.2. [Checking ReiserFS file systems](https://tldp.org/LDP/EVMSUG/html/checkreiserfsim.html)


H.3. [Removing ReiserFS file systems](https://tldp.org/LDP/EVMSUG/html/removexreiserfsim.html)


H.4. [Expanding ReiserFS file systems](https://tldp.org/LDP/EVMSUG/html/expandreiserfsfsim.html)


H.5. [Shrinking ReiserFS file systems](https://tldp.org/LDP/EVMSUG/html/shrinkreiserfsim.html)


I. [Ext-2/3 file system interface module](https://tldp.org/LDP/EVMSUG/html/ext23fsim.html)


I.1. [Creating Ext-2/3 file systems](https://tldp.org/LDP/EVMSUG/html/createext23fsim.html)


I.2. [Checking Ext-2/3 file systems](https://tldp.org/LDP/EVMSUG/html/checkext23fsim.html)


I.3. [Removing Ext-2/3 file systems](https://tldp.org/LDP/EVMSUG/html/removeext23fsim.html)


I.4. [Expanding and shrinking Ext-2/3 file systems](https://tldp.org/LDP/EVMSUG/html/expandshrinkext23fsim.html)


J. [OpenGFS file system interface module](https://tldp.org/LDP/EVMSUG/html/gfsfsim.html)


J.1. [Creating OpenGFS file systems](https://tldp.org/LDP/EVMSUG/html/createopengfsfsim.html)


J.2. [Checking OpenGFS file systems](https://tldp.org/LDP/EVMSUG/html/checkopengfsfsim.html)


J.3. [Removing OpenGFS file systems](https://tldp.org/LDP/EVMSUG/html/removeopengfsfsim.html)


J.4. [Expanding and shrinking OpenGFS file systems](https://tldp.org/LDP/EVMSUG/html/expandshrinkopengfsfsim.html)


K. [NTFS file system interface module](https://tldp.org/LDP/EVMSUG/html/ntfsfsim.html)


K.1. [Creating NTFS file systems](https://tldp.org/LDP/EVMSUG/html/createntfsfsim.html)


K.2. [Fixing NTFS file systems](https://tldp.org/LDP/EVMSUG/html/fixntfsfsim.html)


K.3. [Cloning NTFS file systems](https://tldp.org/LDP/EVMSUG/html/clonentfsfsim.html)


K.4. [Removing NTFS file systems](https://tldp.org/LDP/EVMSUG/html/removentfsfsim.html)


K.5. [Expanding and shrinking NTFS file systems](https://tldp.org/LDP/EVMSUG/html/expandshrinkntfsfsim.html)


**List of Tables**


1. [Organization of the EVMS User Guide](https://tldp.org/LDP/EVMSUG/html/userguidepref.html#bookorg)


1-1. [EVMS user interfaces](https://tldp.org/LDP/EVMSUG/html/uis.html#userinterf)


2-1. [Accelerator keys in the Main Window](https://tldp.org/LDP/EVMSUG/html/gui.html#AEN370)


2-2. [Accelerator keys in the views](https://tldp.org/LDP/EVMSUG/html/gui.html#AEN384)


2-3. [Accelerator keys in the selection window](https://tldp.org/LDP/EVMSUG/html/gui.html#AEN430)


2-4. [Accelerator keys in the configuration options window](https://tldp.org/LDP/EVMSUG/html/gui.html#AEN454)


2-5. [Widget navigation keys in the configuration options window](https://tldp.org/LDP/EVMSUG/html/gui.html#AEN476)


3-1. [EVMS logging levels](https://tldp.org/LDP/EVMSUG/html/loglevels.html#AEN645)


16-1. [FSIM support for expand and shrink operations](https://tldp.org/LDP/EVMSUG/html/whyexpandshrink.html#AEN3141)


**List of Figures**


4-1. [GUI start-up window](https://tldp.org/LDP/EVMSUG/html/guimigrate.html#AEN726)


4-2. [Ncurses start-up window](https://tldp.org/LDP/EVMSUG/html/ncurmigrate.html#AEN737)


4-3. [CLI volume query results](https://tldp.org/LDP/EVMSUG/html/climigrate.html#AEN756)


**List of Examples**


6-1. [Add the DOS Segment Manager](https://tldp.org/LDP/EVMSUG/html/assignex.html#AEN929)


6-2. [Remove the DOS Segment Manager](https://tldp.org/LDP/EVMSUG/html/rmvex.html#AEN1049)


7-1. [Create a 100MB segment](https://tldp.org/LDP/EVMSUG/html/crsegex.html#AEN1122)


8-1. [Create "Sample Container"](https://tldp.org/LDP/EVMSUG/html/context.html#AEN1231)


9-1. [Create "Sample Region"](https://tldp.org/LDP/EVMSUG/html/crregex.html#AEN1327)


10-1. [Create a drive link](https://tldp.org/LDP/EVMSUG/html/drivelinkex.html#AEN1461)


11-1. [Create a snapshot of a volume](https://tldp.org/LDP/EVMSUG/html/snapshotex.html#AEN1607)


12-1. [Create an EVMS native volume](https://tldp.org/LDP/EVMSUG/html/crvolexcomp.html#AEN1923)


12-2. [Create a compatibility volume](https://tldp.org/LDP/EVMSUG/html/crvolexevms.html#AEN2001)


13-1. [Add a JFS File System to a Volume](https://tldp.org/LDP/EVMSUG/html/fsimmkfs.html#AEN2167)


13-2. [Check a JFS File System](https://tldp.org/LDP/EVMSUG/html/fsimmkfsaex.html#AEN2277)


14-1. [Create a private cluster container](https://tldp.org/LDP/EVMSUG/html/x2382.html#AEN2386)


14-2. [Create a shared cluster container](https://tldp.org/LDP/EVMSUG/html/x2496.html#AEN2500)


14-3. [Convert a private container to shared](https://tldp.org/LDP/EVMSUG/html/x2604.html#AEN2608)


14-4. [Convert a shared container to private](https://tldp.org/LDP/EVMSUG/html/x2688.html#AEN2692)


14-5. [Deport a cluster container](https://tldp.org/LDP/EVMSUG/html/x2773.html#AEN2777)


15-1. [Convert a compatibility volume](https://tldp.org/LDP/EVMSUG/html/comptoevms.html#AEN2988)


15-2. [Convert an EVMS volume](https://tldp.org/LDP/EVMSUG/html/evmstocomp.html#AEN3066)


16-1. [Shrink a volume](https://tldp.org/LDP/EVMSUG/html/exshrink.html#AEN3186)


16-2. [Expand a volume](https://tldp.org/LDP/EVMSUG/html/mkfs.html#AEN3297)


17-1. [Add drive linking to an existing volume](https://tldp.org/LDP/EVMSUG/html/exaddfeature.html#AEN3410)


20-1. [Add a spare disk to a compatibility volume made from an MDRaid5 region](https://tldp.org/LDP/EVMSUG/html/pluginexample.html#AEN4012)


21-1. [Destroy a volume and the region and container below it](https://tldp.org/LDP/EVMSUG/html/examdelrecur.html#AEN4143)

* * *
|  | [Next](https://tldp.org/LDP/EVMSUG/html/userguidepref.html)
---|---|---
|  | Preface
