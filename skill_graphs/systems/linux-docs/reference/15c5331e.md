## Version 0.9
###  Lars Wirzenius
`<`

###  Joanna Oja
`<`

###  Stephen Stafford
`<`

###  Alex Weeks
`<`

An introduction to system administration of a Linux system for novices.
Copyright 1993--1998 Lars Wirzenius.
Copyright 1998--2001 Joanna Oja.
Copyright 2001--2003 Stephen Stafford.
Copyright 2003--2004 Stephen Stafford & Alex Weeks.
Copyright 2004--Present Alex Weeks.
Trademarks are owned by their owners.
Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the license is included in the section entitled "GNU Free Documentation License".
* * *

**Table of Contents**


[About This Book](https://tldp.org/LDP/sag/html/sag.html#PREFACE)


1. [Acknowledgments](https://tldp.org/LDP/sag/html/sag.html#ACKNOWLEDGEMENTS)


2. [Revision History](https://tldp.org/LDP/sag/html/sag.html#REVISION-HIST)


3. [Source and pre-formatted versions available](https://tldp.org/LDP/sag/html/sag.html#AVAILABLE-VERSIONS)


4. [Typographical Conventions](https://tldp.org/LDP/sag/html/sag.html#TYPO-CONVENTIONS)


1. [Introduction](https://tldp.org/LDP/sag/html/sag.html#INTRO)


1.1. [Linux or GNU/Linux, that is the question.](https://tldp.org/LDP/sag/html/sag.html#GNU-OR-NOT)


1.2. [Trademarks](https://tldp.org/LDP/sag/html/sag.html#AEN186)


2. [Overview of a Linux System](https://tldp.org/LDP/sag/html/sag.html#OVERVIEW)


2.1. [Various parts of an operating system](https://tldp.org/LDP/sag/html/sag.html#VARIOUS-PARTS)


2.2. [Important parts of the kernel](https://tldp.org/LDP/sag/html/sag.html#KERNEL-PARTS)


2.3. [Major services in a UNIX system](https://tldp.org/LDP/sag/html/sag.html#MAJOR-SERVICES)


3. [Overview of the Directory Tree](https://tldp.org/LDP/sag/html/sag.html#DIR-TREE-OVERVIEW)


3.1. [Background](https://tldp.org/LDP/sag/html/sag.html#FS-BACKGROUND)


3.2. [The root filesystem](https://tldp.org/LDP/sag/html/sag.html#ROOT-FS)


3.3. [The `/etc` directory](https://tldp.org/LDP/sag/html/sag.html#ETC-FS)


3.4. [The `/dev` directory](https://tldp.org/LDP/sag/html/sag.html#DEV-FS)


3.5. [The `/usr` filesystem.](https://tldp.org/LDP/sag/html/sag.html#USR-FS)


3.6. [The `/var` filesystem](https://tldp.org/LDP/sag/html/sag.html#VAR-FS)


3.7. [The `/proc` filesystem](https://tldp.org/LDP/sag/html/sag.html#PROC-FS)


4. [Hardware, Devices, and Tools](https://tldp.org/LDP/sag/html/sag.html#DEVICE-LIST)


4.1. [Hardware Utilities](https://tldp.org/LDP/sag/html/sag.html#HWUTILS)


4.2. [Kernel Modules](https://tldp.org/LDP/sag/html/sag.html#AEN1926)


5. [Using Disks and Other Storage Media](https://tldp.org/LDP/sag/html/sag.html#DISK-USAGE)


5.1. [Two kinds of devices](https://tldp.org/LDP/sag/html/sag.html#BLOCK-CHAR-DEV)


5.2. [Hard disks](https://tldp.org/LDP/sag/html/sag.html#HARD-DISK)


5.3. [Storage Area Networks - Draft](https://tldp.org/LDP/sag/html/sag.html#SAN)


5.4. [Network Attached Storage - Draft](https://tldp.org/LDP/sag/html/sag.html#NET-ATTACHED)


5.5. [Floppies](https://tldp.org/LDP/sag/html/sag.html#FLOPPIES)


5.6. [CD-ROMs](https://tldp.org/LDP/sag/html/sag.html#CDROM)


5.7. [Tapes](https://tldp.org/LDP/sag/html/sag.html#TAPES)


5.8. [Formatting](https://tldp.org/LDP/sag/html/sag.html#FORMATTING)


5.9. [Partitions](https://tldp.org/LDP/sag/html/sag.html#PARTITIONS)


5.10. [Filesystems](https://tldp.org/LDP/sag/html/sag.html#FILESYSTEMS)


5.11. [Disks without filesystems](https://tldp.org/LDP/sag/html/sag.html#DISK-NO-FS)


5.12. [Allocating disk space](https://tldp.org/LDP/sag/html/sag.html#ALLOC-DISK)


6. [Memory Management](https://tldp.org/LDP/sag/html/sag.html#MEMORY-MANAGEMENT)


6.1. [What is virtual memory?](https://tldp.org/LDP/sag/html/sag.html#VM-INTRO)


6.2. [Creating a swap space](https://tldp.org/LDP/sag/html/sag.html#SWAP-SPACE)


6.3. [Using a swap space](https://tldp.org/LDP/sag/html/sag.html#USING-SWAP)


6.4. [Sharing swap spaces with other operating systems](https://tldp.org/LDP/sag/html/sag.html#SHARING-SWAP)


6.5. [Allocating swap space](https://tldp.org/LDP/sag/html/sag.html#SWAP-ALLOCATION)


6.6. [The buffer cache](https://tldp.org/LDP/sag/html/sag.html#BUFFER-CACHE)


7. [System Monitoring](https://tldp.org/LDP/sag/html/sag.html#SYSTEM-MONITORING)


7.1. [System Resources](https://tldp.org/LDP/sag/html/sag.html#SYSTEM-RESOURCES)


7.2. [Filesystem Usage](https://tldp.org/LDP/sag/html/sag.html#FS-USAGE)


7.3. [Monitoring Users](https://tldp.org/LDP/sag/html/sag.html#MONITORING-USERS)


8. [Boots And Shutdowns](https://tldp.org/LDP/sag/html/sag.html#BOOTS-AND-SHUTDOWNS)


8.1. [An overview of boots and shutdowns](https://tldp.org/LDP/sag/html/sag.html#BOOT-OVERVIEW)


8.2. [The boot process in closer look](https://tldp.org/LDP/sag/html/sag.html#BOOT-PROCESS)


8.3. [More about shutdowns](https://tldp.org/LDP/sag/html/sag.html#SHUTDOWN)


8.4. [Rebooting](https://tldp.org/LDP/sag/html/sag.html#REBOOTING)


8.5. [Single user mode](https://tldp.org/LDP/sag/html/sag.html#SINGLE-USER)


8.6. [Emergency boot floppies](https://tldp.org/LDP/sag/html/sag.html#EMERG-BOOT-FLOPPY)


9. [**init**](https://tldp.org/LDP/sag/html/sag.html#INIT-INTRO)


9.1. [**init** comes first](https://tldp.org/LDP/sag/html/sag.html#INIT-PROCESS)


9.2. [Configuring **init** to start **getty** : the `/etc/inittab` file](https://tldp.org/LDP/sag/html/sag.html#CONFIG-INIT)


9.3. [Run levels](https://tldp.org/LDP/sag/html/sag.html#RUN-LEVELS-INTRO)


9.4. [Special configuration in `/etc/inittab`](https://tldp.org/LDP/sag/html/sag.html#INITTAB)


9.5. [Booting in single user mode](https://tldp.org/LDP/sag/html/sag.html#BOOT-SINGLE-USER)


10. [Logging In And Out](https://tldp.org/LDP/sag/html/sag.html#LOG-IN-AND-OUT)


10.1. [Logins via terminals](https://tldp.org/LDP/sag/html/sag.html#LOGIN-VIA-TERMINAL)


10.2. [Logins via the network](https://tldp.org/LDP/sag/html/sag.html#LOGIN-VIA-NETWORK)


10.3. [What **login** does](https://tldp.org/LDP/sag/html/sag.html#WHAT-LOGIN-DOES)


10.4. [X and xdm](https://tldp.org/LDP/sag/html/sag.html#X-XDM)


10.5. [Access control](https://tldp.org/LDP/sag/html/sag.html#ACCESS-CONTROL)


10.6. [Shell startup](https://tldp.org/LDP/sag/html/sag.html#SHELL-STARTUP)


11. [Managing user accounts](https://tldp.org/LDP/sag/html/sag.html#MANAGING-USERS)


11.1. [What's an account?](https://tldp.org/LDP/sag/html/sag.html#ACCOUNT)


11.2. [Creating a user](https://tldp.org/LDP/sag/html/sag.html#ADDUSER)


11.3. [Changing user properties](https://tldp.org/LDP/sag/html/sag.html#USER-PROPERTIES)


11.4. [Removing a user](https://tldp.org/LDP/sag/html/sag.html#DELUSER)


11.5. [Disabling a user temporarily](https://tldp.org/LDP/sag/html/sag.html#DISABLE-USER)


12. [Backups](https://tldp.org/LDP/sag/html/sag.html#BACKUPS-INTRO)


12.1. [On the importance of being backed up](https://tldp.org/LDP/sag/html/sag.html#BACKUPS)


12.2. [Selecting the backup medium](https://tldp.org/LDP/sag/html/sag.html#BACKUP-MEDIA)


12.3. [Selecting the backup tool](https://tldp.org/LDP/sag/html/sag.html#BACKUP-TOOLS)


12.4. [Simple backups](https://tldp.org/LDP/sag/html/sag.html#SIMPLE-BACKUPS)


12.5. [Multilevel backups](https://tldp.org/LDP/sag/html/sag.html#MULTI-LEVEL-BACKUPS)


12.6. [What to back up](https://tldp.org/LDP/sag/html/sag.html#WHAT-TO-BACKUP)


12.7. [Compressed backups](https://tldp.org/LDP/sag/html/sag.html#COMPRESSED-BACKUPS)


13. [Task Automation --To Be Added](https://tldp.org/LDP/sag/html/sag.html#TASK-AUTOMATION)


14. [Keeping Time](https://tldp.org/LDP/sag/html/sag.html#KEEPING-TIME)


14.1. [The concept of localtime](https://tldp.org/LDP/sag/html/sag.html#LOCALTIME)


14.2. [The hardware and software clocks](https://tldp.org/LDP/sag/html/sag.html#HW-SW-CLOCKS)


14.3. [Showing and setting time](https://tldp.org/LDP/sag/html/sag.html#SHOWING-SETTING-TIME)


14.4. [When the clock is wrong](https://tldp.org/LDP/sag/html/sag.html#CLOCK-WRONG)


14.5. [NTP - Network Time Protocol](https://tldp.org/LDP/sag/html/sag.html#NTP)


14.6. [Basic NTP configuration](https://tldp.org/LDP/sag/html/sag.html#BASIC-NTP-CONFIG)


14.7. [NTP Toolkit](https://tldp.org/LDP/sag/html/sag.html#NTP-TOOLKIT)


14.8. [Some known NTP servers](https://tldp.org/LDP/sag/html/sag.html#NTP-SERVERS)


14.9. [NTP Links](https://tldp.org/LDP/sag/html/sag.html#NTP-LINKS)


15. [System Logs --To Be Added](https://tldp.org/LDP/sag/html/sag.html#SYSTEM-LOGS)


16. [System Updates --To Be Added](https://tldp.org/LDP/sag/html/sag.html#SYSTEM-UPDATES)


17. [The Linux Kernel Source](https://tldp.org/LDP/sag/html/sag.html#KERNEL)


18. [Finding Help](https://tldp.org/LDP/sag/html/sag.html#FINDING-HELP)


18.1. [Newsgroups and Mailing Lists](https://tldp.org/LDP/sag/html/sag.html#NEWSGROUPS-MAILLING-LISTS)


18.2. [IRC](https://tldp.org/LDP/sag/html/sag.html#IRC)


A. [GNU Free Documentation License](https://tldp.org/LDP/sag/html/sag.html#GFDL1.2)


A.1. [PREAMBLE](https://tldp.org/LDP/sag/html/sag.html#GFDL-0)


A.2. [APPLICABILITY AND DEFINITIONS](https://tldp.org/LDP/sag/html/sag.html#GFDL-1)


A.3. [VERBATIM COPYING](https://tldp.org/LDP/sag/html/sag.html#GFDL-2)


A.4. [COPYING IN QUANTITY](https://tldp.org/LDP/sag/html/sag.html#GFDL-3)


A.5. [MODIFICATIONS](https://tldp.org/LDP/sag/html/sag.html#GFDL-4)


A.6. [COMBINING DOCUMENTS](https://tldp.org/LDP/sag/html/sag.html#GFDL-5)


A.7. [COLLECTIONS OF DOCUMENTS](https://tldp.org/LDP/sag/html/sag.html#GFDL-6)


A.8. [AGGREGATION WITH INDEPENDENT WORKS](https://tldp.org/LDP/sag/html/sag.html#GFDL-7)


A.9. [TRANSLATION](https://tldp.org/LDP/sag/html/sag.html#GFDL-8)


A.10. [TERMINATION](https://tldp.org/LDP/sag/html/sag.html#GFDL-9)


A.11. [FUTURE REVISIONS OF THIS LICENSE](https://tldp.org/LDP/sag/html/sag.html#GFDL-10)


A.12. [ADDENDUM: How to use this License for your documents](https://tldp.org/LDP/sag/html/sag.html#GFDL-ADDENDUM)


[Glossary (DRAFT, but not for long hopefully)](https://tldp.org/LDP/sag/html/sag.html#GLOSSARY)


[Index-Draft](https://tldp.org/LDP/sag/html/sag.html#BOOKINDEX)


**List of Tables**


5-1. [Comparing Filesystem Features](https://tldp.org/LDP/sag/html/sag.html#AEN2790)


5-2. [Sizes](https://tldp.org/LDP/sag/html/sag.html#AEN2949)


5-3. [My Partitions](https://tldp.org/LDP/sag/html/sag.html#AEN3270)


9-1. [Run level numbers](https://tldp.org/LDP/sag/html/sag.html#RUN-LEVELS-TABLE)


12-1. [Efficient backup scheme using many backup levels](https://tldp.org/LDP/sag/html/sag.html#EFFICIENT-BACKUP-LEVELS)


**List of Figures**


2-1. [Some of the more important parts of the Linux kernel](https://tldp.org/LDP/sag/html/sag.html#KERNELOVERVIEW)


3-1. [Parts of a Unix directory tree. Dashed lines indicate partition limits.](https://tldp.org/LDP/sag/html/sag.html#FSTREE)


5-1. [A schematic picture of a hard disk.](https://tldp.org/LDP/sag/html/sag.html#HD-SCHEMATIC)


5-2. [A sample hard disk partitioning.](https://tldp.org/LDP/sag/html/sag.html#HARD-DISK-LAYOUT)


5-3. [Three separate filesystems.](https://tldp.org/LDP/sag/html/sag.html#HD-MOUNT-ROOT)


5-4. [`/home` and `/usr` have been mounted.](https://tldp.org/LDP/sag/html/sag.html#HD-MOUNT-ALL)


10-1. [Logins via terminals: the interaction of **init** , **getty** , **login** , and the shell.](https://tldp.org/LDP/sag/html/sag.html#TERMINAL-LOGINS-TABLE)


12-1. [A sample multilevel backup schedule.](https://tldp.org/LDP/sag/html/sag.html#BACKUP-HISTORY-TIMELINE)

* * *
