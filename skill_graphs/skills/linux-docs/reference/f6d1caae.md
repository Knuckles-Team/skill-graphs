#  5.4. Implementation
##  5.4.1. System startup
Start the system using the following procedure:
  * Boot the PC using the floppy labeled "boot disk".
  * At the `grub>` prompt, type the usual kernel and boot commands, but without the `_rw_` parameter this time. In other words, type `**kernel (fd0)/boot/vmlinuz init=/bin/sh root=/dev/fd0 load_ramdisk=1 prompt_ramdisk=1**` , press **Enter** then type `**boot**` and press **Enter**.
  * Put in the recently created root disk when prompted.


The output should resemble the example below:
```
GNU GRUB version 0.95

grub> kernel (fd0)/boot/vmlinuz init=/bin/sh root=/dev/fd0 load_ramdisk=1 prompt_ramdisk=1
   [Linux-bzImage, setup=0xc00, size=0xce29b]

grub> boot

Linux version 2.4.26
..
.. [various kernel messages]
..
VFS: Insert root floppy disk to be loaded into RAM disk and press ENTER
RAMDISK: Compressed image found at block 0
VFS: Mounted root (ext2 filesystem) readonly.
Freeing unused kernel memory: 178k freed
# _
```

---
* * *
##  5.4.2. Test the local_fs script
Run the script by typing the following commands at the shell prompt:
```
`bash#` PATH=/sbin:/bin:/etc/init.d ; export PATH
`bash#` cat /etc/mtab
`bash#` local_fs
`bash#` cat /etc/mtab
`bash#` df
```

---
If everything is working properly, then the screen output should look something like the example below.
```
`bash#` PATH=/sbin:/bin:/etc/init.d ; export PATH
`bash#` cat /etc/mtab
`bash#` local_fs
/dev/ram0: clean 74/1024 files 3178/4096 blocks
Remounting / as read-write.
Mounting local filesystems.
`bash#` cat /etc/mtab
/dev/ram0 / ext2 rw 0 0
proc /proc proc rw 0 0
`bash#` df
Filesystem      1k-blocks       Used Available Use% Mounted on
/dev/ram0       3963            3045 918        77% /

```

---
* * *
##  5.4.3. Create and mount additional filesystems
Procure a blank floppy disk and label it as "home". Remove the root disk floppy and insert the "home" diskette. Type the following commands:
```
`bash#` mkfs -t ext2 /dev/fd0
`bash#` fsck /dev/fd0
`bash#` mount /dev/fd0 /home
`bash#` mkdir /home/floyd
`bash#` cd /home/floyd
`bash#` echo "Goodbye cruel world." > goodbye.txt
`bash#` cat goodbye.txt
```

---
* * *
##  5.4.4. System shutdown
```
`bash#` cd /
`bash#` umount /home
```

---
Remove the diskette from fd0 and restart the system using **CTRL** -**ALT** -**DELETE**.
* * *
