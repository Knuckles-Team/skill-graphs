#  5.8. Formatting
_Formatting_ is the process of writing marks on the magnetic media that are used to mark tracks and sectors. Before a disk is formatted, its magnetic surface is a complete mess of magnetic signals. When it is formatted, some order is brought into the chaos by essentially drawing lines where the tracks go, and where they are divided into sectors. The actual details are not quite exactly like this, but that is irrelevant. What is important is that a disk cannot be used unless it has been formatted.
The terminology is a bit confusing here: in MS-DOS and MS Windows, the word formatting is used to cover also the process of creating a filesystem (which will be discussed below). There, the two processes are often combined, especially for floppies. When the distinction needs to be made, the real formatting is called _low-level formatting_ , while making the filesystem is called _high-level formatting_ . In UNIX circles, the two are called formatting and making a filesystem, so that's what is used in this book as well.
For IDE and some SCSI disks the formatting is actually done at the factory and doesn't need to be repeated; hence most people rarely need to worry about it. In fact, formatting a hard disk can cause it to work less well, for example because a disk might need to be formatted in some very special way to allow automatic bad sector replacement to work.
Disks that need to be or can be formatted often require a special program anyway, because the interface to the formatting logic inside the drive is different from drive to drive. The formatting program is often either on the controller BIOS, or is supplied as an MS-DOS program; neither of these can easily be used from within Linux.
During formatting one might encounter bad spots on the disk, called _bad blocks_ or _bad sectors_. These are sometimes handled by the drive itself, but even then, if more of them develop, something needs to be done to avoid using those parts of the disk. The logic to do this is built into the filesystem; how to add the information into the filesystem is described below. Alternatively, one might create a small partition that covers just the bad part of the disk; this approach might be a good idea if the bad spot is very large, since filesystems can sometimes have trouble with very large bad areas.
Floppies are formatted with **fdformat** . The floppy device file to use is given as the parameter. For example, the following command would format a high density, 3.5 inch floppy in the first floppy drive:
```
	`$` `**fdformat /dev/fd0H1440**`
	`Double-sided, 80 tracks, 18 sec/track. Total capacity
	1440 kB.`
	`Formatting ... done`
	`Verifying ... done`
	`$`

```

---
Note that if you want to use an autodetecting device (e.g.,` /dev/fd0`), you _must_ set the parameters of the device with **setfdprm** first. To achieve the same effect as above, one would have to do the following: ```
	`$` `**setfdprm /dev/fd0 1440/1440**`
	`$` `**fdformat /dev/fd0**`
	`Double-sided, 80 tracks, 18 sec/track. Total capacity
	1440 KB.`
	`Formatting ... done`
	`Verifying ... done`
	`$`

```

---
It is usually more convenient to choose the correct device file that matches the type of the floppy. Note that it is unwise to format floppies to contain more information than what they are designed for.
**fdformat** also validate the floppy, i.e., check it for bad blocks. It will try a bad block several times (you can usually hear this, the drive noise changes dramatically). If the floppy is only marginally bad (due to dirt on the read/write head, some errors are false signals), **fdformat** won't complain, but a real error will abort the validation process. The kernel will print log messages for each I/O error it finds; these will go to the console or, if **syslog** is being used, to the file `/var/log/messages`. **fdformat** itself won't tell where the error is (one usually doesn't care, floppies are cheap enough that a bad one is automatically thrown away).
```
	`$` `**fdformat /dev/fd0H1440**`
	`Double-sided, 80 tracks, 18 sec/track. Total capacity
	1440 KB.`
	`Formatting ... done`
	`Verifying ... read: Unknown error`
	`$`

```

---
The**badblocks** command can be used to search any disk or partition for bad blocks (including a floppy). It does not format the disk, so it can be used to check even existing filesystems. The example below checks a 3.5 inch floppy with two bad blocks. ```
	`$` `**badblocks /dev/fd0H1440 1440**`
	`718`
	`719`
	`$`

```

---
**badblocks** outputs the block numbers of the bad blocks it finds. Most filesystems can avoid such bad blocks. They maintain a list of known bad blocks, which is initialized when the filesystem is made, and can be modified later. The initial search for bad blocks can be done by the **mkfs** command (which initializes the filesystem), but later checks should be done with **badblocks** and the new blocks should be added with **fsck**. We'll describe **mkfs** and **fsck** later.
Many modern disks automatically notice bad blocks, and attempt to fix them by using a special, reserved good block instead. This is invisible to the operating system. This feature should be documented in the disk's manual, if you're curious if it is happening. Even such disks can fail, if the number of bad blocks grows too large, although chances are that by then the disk will be so rotten as to be unusable.
* * *
