#  The Linux System Administrator's Guide
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
[Legal Notice](https://tldp.org/LDP/sag/html/LEGAL-NOTICE.html)
* * *

**Table of Contents**


[About This Book](https://tldp.org/LDP/sag/html/preface.html)


1. [Acknowledgments](https://tldp.org/LDP/sag/html/acknowledgements.html)


2. [Revision History](https://tldp.org/LDP/sag/html/revision-hist.html)


3. [Source and pre-formatted versions available](https://tldp.org/LDP/sag/html/available-versions.html)


4. [Typographical Conventions](https://tldp.org/LDP/sag/html/typo-conventions.html)


1. [Introduction](https://tldp.org/LDP/sag/html/intro.html)


1.1. [Linux or GNU/Linux, that is the question.](https://tldp.org/LDP/sag/html/gnu-or-not.html)


1.2. [Trademarks](https://tldp.org/LDP/sag/html/x186.html)


2. [Overview of a Linux System](https://tldp.org/LDP/sag/html/overview.html)


2.1. [Various parts of an operating system](https://tldp.org/LDP/sag/html/various-parts.html)


2.2. [Important parts of the kernel](https://tldp.org/LDP/sag/html/kernel-parts.html)


2.3. [Major services in a UNIX system](https://tldp.org/LDP/sag/html/major-services.html)


3. [Overview of the Directory Tree](https://tldp.org/LDP/sag/html/dir-tree-overview.html)


3.1. [Background](https://tldp.org/LDP/sag/html/fs-background.html)


3.2. [The root filesystem](https://tldp.org/LDP/sag/html/root-fs.html)


3.3. [The `/etc` directory](https://tldp.org/LDP/sag/html/etc-fs.html)


3.4. [The `/dev` directory](https://tldp.org/LDP/sag/html/dev-fs.html)


3.5. [The `/usr` filesystem.](https://tldp.org/LDP/sag/html/usr-fs.html)


3.6. [The `/var` filesystem](https://tldp.org/LDP/sag/html/var-fs.html)


3.7. [The `/proc` filesystem](https://tldp.org/LDP/sag/html/proc-fs.html)


4. [Hardware, Devices, and Tools](https://tldp.org/LDP/sag/html/device-list.html)


4.1. [Hardware Utilities](https://tldp.org/LDP/sag/html/hwutils.html)


4.2. [Kernel Modules](https://tldp.org/LDP/sag/html/x1926.html)


5. [Using Disks and Other Storage Media](https://tldp.org/LDP/sag/html/disk-usage.html)


5.1. [Two kinds of devices](https://tldp.org/LDP/sag/html/block-char-dev.html)


5.2. [Hard disks](https://tldp.org/LDP/sag/html/hard-disk.html)


5.3. [Storage Area Networks - Draft](https://tldp.org/LDP/sag/html/san.html)


5.4. [Network Attached Storage - Draft](https://tldp.org/LDP/sag/html/net-attached.html)


5.5. [Floppies](https://tldp.org/LDP/sag/html/floppies.html)


5.6. [CD-ROMs](https://tldp.org/LDP/sag/html/cdrom.html)


5.7. [Tapes](https://tldp.org/LDP/sag/html/tapes.html)


5.8. [Formatting](https://tldp.org/LDP/sag/html/formatting.html)


5.9. [Partitions](https://tldp.org/LDP/sag/html/partitions.html)


5.10. [Filesystems](https://tldp.org/LDP/sag/html/filesystems.html)


5.11. [Disks without filesystems](https://tldp.org/LDP/sag/html/disk-no-fs.html)


5.12. [Allocating disk space](https://tldp.org/LDP/sag/html/alloc-disk.html)


6. [Memory Management](https://tldp.org/LDP/sag/html/memory-management.html)


6.1. [What is virtual memory?](https://tldp.org/LDP/sag/html/vm-intro.html)


6.2. [Creating a swap space](https://tldp.org/LDP/sag/html/swap-space.html)


6.3. [Using a swap space](https://tldp.org/LDP/sag/html/using-swap.html)


6.4. [Sharing swap spaces with other operating systems](https://tldp.org/LDP/sag/html/sharing-swap.html)


6.5. [Allocating swap space](https://tldp.org/LDP/sag/html/swap-allocation.html)


6.6. [The buffer cache](https://tldp.org/LDP/sag/html/buffer-cache.html)


7. [System Monitoring](https://tldp.org/LDP/sag/html/system-monitoring.html)


7.1. [System Resources](https://tldp.org/LDP/sag/html/system-resources.html)


7.2. [Filesystem Usage](https://tldp.org/LDP/sag/html/fs-usage.html)


7.3. [Monitoring Users](https://tldp.org/LDP/sag/html/monitoring-users.html)


8. [Boots And Shutdowns](https://tldp.org/LDP/sag/html/boots-and-shutdowns.html)


8.1. [An overview of boots and shutdowns](https://tldp.org/LDP/sag/html/boot-overview.html)


8.2. [The boot process in closer look](https://tldp.org/LDP/sag/html/boot-process.html)


8.3. [More about shutdowns](https://tldp.org/LDP/sag/html/shutdown.html)


8.4. [Rebooting](https://tldp.org/LDP/sag/html/rebooting.html)


8.5. [Single user mode](https://tldp.org/LDP/sag/html/single-user.html)


8.6. [Emergency boot floppies](https://tldp.org/LDP/sag/html/emerg-boot-floppy.html)


9. [**init**](https://tldp.org/LDP/sag/html/init-intro.html)


9.1. [**init** comes first](https://tldp.org/LDP/sag/html/init-process.html)


9.2. [Configuring **init** to start **getty** : the `/etc/inittab` file](https://tldp.org/LDP/sag/html/config-init.html)


9.3. [Run levels](https://tldp.org/LDP/sag/html/run-levels-intro.html)


9.4. [Special configuration in `/etc/inittab`](https://tldp.org/LDP/sag/html/inittab.html)


9.5. [Booting in single user mode](https://tldp.org/LDP/sag/html/boot-single-user.html)


10. [Logging In And Out](https://tldp.org/LDP/sag/html/log-in-and-out.html)


10.1. [Logins via terminals](https://tldp.org/LDP/sag/html/login-via-terminal.html)


10.2. [Logins via the network](https://tldp.org/LDP/sag/html/login-via-network.html)


10.3. [What **login** does](https://tldp.org/LDP/sag/html/what-login-does.html)


10.4. [X and xdm](https://tldp.org/LDP/sag/html/x-xdm.html)


10.5. [Access control](https://tldp.org/LDP/sag/html/access-control.html)


10.6. [Shell startup](https://tldp.org/LDP/sag/html/shell-startup.html)


11. [Managing user accounts](https://tldp.org/LDP/sag/html/managing-users.html)


11.1. [What's an account?](https://tldp.org/LDP/sag/html/account.html)


11.2. [Creating a user](https://tldp.org/LDP/sag/html/adduser.html)


11.3. [Changing user properties](https://tldp.org/LDP/sag/html/user-properties.html)


11.4. [Removing a user](https://tldp.org/LDP/sag/html/deluser.html)


11.5. [Disabling a user temporarily](https://tldp.org/LDP/sag/html/disable-user.html)


12. [Backups](https://tldp.org/LDP/sag/html/backups-intro.html)


12.1. [On the importance of being backed up](https://tldp.org/LDP/sag/html/backups.html)


12.2. [Selecting the backup medium](https://tldp.org/LDP/sag/html/backup-media.html)


12.3. [Selecting the backup tool](https://tldp.org/LDP/sag/html/backup-tools.html)


12.4. [Simple backups](https://tldp.org/LDP/sag/html/simple-backups.html)


12.5. [Multilevel backups](https://tldp.org/LDP/sag/html/multi-level-backups.html)


12.6. [What to back up](https://tldp.org/LDP/sag/html/what-to-backup.html)


12.7. [Compressed backups](https://tldp.org/LDP/sag/html/compressed-backups.html)


13. [Task Automation --To Be Added](https://tldp.org/LDP/sag/html/task-automation.html)


14. [Keeping Time](https://tldp.org/LDP/sag/html/keeping-time.html)


14.1. [The concept of localtime](https://tldp.org/LDP/sag/html/localtime.html)


14.2. [The hardware and software clocks](https://tldp.org/LDP/sag/html/hw-sw-clocks.html)


14.3. [Showing and setting time](https://tldp.org/LDP/sag/html/showing-setting-time.html)


14.4. [When the clock is wrong](https://tldp.org/LDP/sag/html/clock-wrong.html)


14.5. [NTP - Network Time Protocol](https://tldp.org/LDP/sag/html/ntp.html)


14.6. [Basic NTP configuration](https://tldp.org/LDP/sag/html/basic-ntp-config.html)


14.7. [NTP Toolkit](https://tldp.org/LDP/sag/html/ntp-toolkit.html)


14.8. [Some known NTP servers](https://tldp.org/LDP/sag/html/ntp-servers.html)


14.9. [NTP Links](https://tldp.org/LDP/sag/html/ntp-links.html)


15. [System Logs --To Be Added](https://tldp.org/LDP/sag/html/system-logs.html)


16. [System Updates --To Be Added](https://tldp.org/LDP/sag/html/system-updates.html)


17. [The Linux Kernel Source](https://tldp.org/LDP/sag/html/kernel.html)


18. [Finding Help](https://tldp.org/LDP/sag/html/finding-help.html)


18.1. [Newsgroups and Mailing Lists](https://tldp.org/LDP/sag/html/newsgroups-mailling-lists.html)


18.2. [IRC](https://tldp.org/LDP/sag/html/irc.html)


A. [GNU Free Documentation License](https://tldp.org/LDP/sag/html/gfdl1.2.html)


A.1. [PREAMBLE](https://tldp.org/LDP/sag/html/gfdl-0.html)


A.2. [APPLICABILITY AND DEFINITIONS](https://tldp.org/LDP/sag/html/gfdl-1.html)


A.3. [VERBATIM COPYING](https://tldp.org/LDP/sag/html/gfdl-2.html)


A.4. [COPYING IN QUANTITY](https://tldp.org/LDP/sag/html/gfdl-3.html)


A.5. [MODIFICATIONS](https://tldp.org/LDP/sag/html/gfdl-4.html)


A.6. [COMBINING DOCUMENTS](https://tldp.org/LDP/sag/html/gfdl-5.html)


A.7. [COLLECTIONS OF DOCUMENTS](https://tldp.org/LDP/sag/html/gfdl-6.html)


A.8. [AGGREGATION WITH INDEPENDENT WORKS](https://tldp.org/LDP/sag/html/gfdl-7.html)


A.9. [TRANSLATION](https://tldp.org/LDP/sag/html/gfdl-8.html)


A.10. [TERMINATION](https://tldp.org/LDP/sag/html/gfdl-9.html)


A.11. [FUTURE REVISIONS OF THIS LICENSE](https://tldp.org/LDP/sag/html/gfdl-10.html)


A.12. [ADDENDUM: How to use this License for your documents](https://tldp.org/LDP/sag/html/gfdl-addendum.html)


[Glossary (DRAFT, but not for long hopefully)](https://tldp.org/LDP/sag/html/glossary.html)


[Index-Draft](https://tldp.org/LDP/sag/html/bookindex.html)


**List of Tables**


5-1. [Comparing Filesystem Features](https://tldp.org/LDP/sag/html/filesystems.html#AEN2790)


5-2. [Sizes](https://tldp.org/LDP/sag/html/filesystems.html#AEN2949)


5-3. [My Partitions](https://tldp.org/LDP/sag/html/alloc-disk.html#AEN3270)


9-1. [Run level numbers](https://tldp.org/LDP/sag/html/run-levels-intro.html#RUN-LEVELS-TABLE)


12-1. [Efficient backup scheme using many backup levels](https://tldp.org/LDP/sag/html/multi-level-backups.html#EFFICIENT-BACKUP-LEVELS)


**List of Figures**


2-1. [Some of the more important parts of the Linux kernel](https://tldp.org/LDP/sag/html/kernel-parts.html#KERNELOVERVIEW)


3-1. [Parts of a Unix directory tree. Dashed lines indicate partition limits.](https://tldp.org/LDP/sag/html/fs-background.html#FSTREE)


5-1. [A schematic picture of a hard disk.](https://tldp.org/LDP/sag/html/hard-disk.html#HD-SCHEMATIC)


5-2. [A sample hard disk partitioning.](https://tldp.org/LDP/sag/html/partitions.html#HARD-DISK-LAYOUT)


5-3. [Three separate filesystems.](https://tldp.org/LDP/sag/html/filesystems.html#HD-MOUNT-ROOT)


5-4. [`/home` and `/usr` have been mounted.](https://tldp.org/LDP/sag/html/filesystems.html#HD-MOUNT-ALL)


10-1. [Logins via terminals: the interaction of **init** , **getty** , **login** , and the shell.](https://tldp.org/LDP/sag/html/login-via-terminal.html#TERMINAL-LOGINS-TABLE)


12-1. [A sample multilevel backup schedule.](https://tldp.org/LDP/sag/html/multi-level-backups.html#BACKUP-HISTORY-TIMELINE)

* * *
|  | [Next](https://tldp.org/LDP/sag/html/preface.html)
---|---|---
|  | About This Book
