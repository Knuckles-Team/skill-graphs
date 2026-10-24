#  Chapter 9. Controlling the system
The controlling the system chapter details commands that you may wish to use to interact with devices on your system and then details how to control processes and services/daemons.

eject

eject simply tells a device to open (eject) the drive. Useful for cdrom/DVD drives.
For example the command below would eject the cdrom-drive (if your cdrom is linked to /dev/cdrom):
```
eject /dev/cdrom
```

---
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **This won't work unless**
---|---
|  This will only work if the user has permission to mount the partition. Please see the tip in [Section 9.1](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#MOUNTING-AND-UNMOUNTING) for more information.
* * *
