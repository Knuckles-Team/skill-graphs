# ls -l /dev/hd*
```

brw-rw----    1 root     disk       3,   0 Mar 15  2002 /dev/had
brw-rw----    1 root     disk       3,   1 Mar 15  2002 /dev/hda1
brw-rw----    1 root     disk       3,  10 Mar 15  2002 /dev/hda10
brw-rw----    1 root     disk       3,  11 Mar 15  2002 /dev/hda11
brw-rw----    1 root     disk       3,  12 Mar 15  2002 /dev/hda12
brw-rw----    1 root     disk       3,  13 Mar 15  2002 /dev/hda13
brw-rw----    1 root     disk       3,  14 Mar 15  2002 /dev/hda14
brw-rw----    1 root     disk       3,  15 Mar 15  2002 /dev/hda15
brw-rw----    1 root     disk       3,  16 Mar 15  2002 /dev/hda16
brw-rw----    1 root     disk       3,  17 Mar 15  2002 /dev/hda17
brw-rw----    1 root     disk       3,  18 Mar 15  2002 /dev/hda18
brw-rw----    1 root     disk       3,  19 Mar 15  2002 /dev/hda19
brw-rw----    1 root     disk       3,   2 Mar 15  2002 /dev/hda2
brw-rw----    1 root     disk       3,  20 Mar 15  2002 /dev/hda20
brw-rw----    1 root     disk       3,   3 Mar 15  2002 /dev/hda3
brw-rw----    1 root     disk       3,   4 Mar 15  2002 /dev/hda4
brw-rw----    1 root     disk       3,   5 Mar 15  2002 /dev/hda5
brw-rw----    1 root     disk       3,   6 Mar 15  2002 /dev/hda6
brw-rw----    1 root     disk       3,   7 Mar 15  2002 /dev/hda7
brw-rw----    1 root     disk       3,   8 Mar 15  2002 /dev/hda8
brw-rw----    1 root     disk       3,   9 Mar 15  2002 /dev/hda9
brw-rw----    1 root     disk       3,  64 Mar 15  2002 /dev/hdb
brw-rw----    1 root     disk       3,  65 Mar 15  2002 /dev/hdb1
brw-rw----    1 root     disk       3,  74 Mar 15  2002 /dev/hdb10
brw-rw----    1 root     disk       3,  75 Mar 15  2002 /dev/hdb11
brw-rw----    1 root     disk       3,  76 Mar 15  2002 /dev/hdb12
brw-rw----    1 root     disk       3,  77 Mar 15  2002 /dev/hdb13
brw-rw----    1 root     disk       3,  78 Mar 15  2002 /dev/hdb14
brw-rw----    1 root     disk       3,  79 Mar 15  2002 /dev/hdb15
brw-rw----    1 root     disk       3,  80 Mar 15  2002 /dev/hdb16
brw-rw----    1 root     disk       3,  81 Mar 15  2002 /dev/hdb17
brw-rw----    1 root     disk       3,  82 Mar 15  2002 /dev/hdb18
brw-rw----    1 root     disk       3,  83 Mar 15  2002 /dev/hdb19
brw-rw----    1 root     disk       3,  66 Mar 15  2002 /dev/hdb2
brw-rw----    1 root     disk       3,  84 Mar 15  2002 /dev/hdb20
brw-rw----    1 root     disk       3,  67 Mar 15  2002 /dev/hdb3
brw-rw----    1 root     disk       3,  68 Mar 15  2002 /dev/hdb4
brw-rw----    1 root     disk       3,  69 Mar 15  2002 /dev/hdb5
brw-rw----    1 root     disk       3,  70 Mar 15  2002 /dev/hdb6
brw-rw----    1 root     disk       3,  71 Mar 15  2002 /dev/hdb7
brw-rw----    1 root     disk       3,  72 Mar 15  2002 /dev/hdb8
brw-rw----    1 root     disk       3,  73 Mar 15  2002 /dev/hdb9
brw-rw----    1 root     disk      22,   0 Mar 15  2002 /dev/hdc
brw-rw----    1 root     disk      22,  64 Mar 15  2002 /dev/hdd

```

---
The major number for both had and hdb devices is 3. Of course, the minor number changes for each specific partition. The definition of each major number category can be examined by looking at the contents of the /usr/src/linux/include/linux/major.h file. The devices.txt also documents major and minor numbers. It is located in the /usr/src/linux/Documentation directory. This file defines the major numbers. Almost all files devices are created by default at the install time. However, you can always create a device using the mknod command or the MAKEDEV script which is located in the /dev directory itself. Devices can be created with this utility by supplying the device to be created, the device type (block or character) and the major and minor numbers. For example, let's say you have accidentally deleted /dev/ttyS0 (COM1 under Windows), it can be recreated using the following command
