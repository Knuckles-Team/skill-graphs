   to [http://repair4laptop.org/] repair, disassemble, upgrade or mod
   laptops or notebooks, [http://repair4pda.org/] dissect, repair and
   upgrade broken PDAs and HandHelds, as well as
   [http://repair4mobilephone.org/] take apart, repair and upgrade
   mobile (cell) phones, [http://repair4player.org/] open, repair and
   upgrade mobile audio and video players and
   [http://repair4printer.org/] repair and upgrade printers.
     ________________________________________________________________

Appendix D. Survey about Micro Linuxes

   Because of their small or non-existent footprint, micro-Linuxes are
   especially suited to run on laptops - particularly if you use a
   company-provided laptop running Microsoft-Windows9x/NT. Or for
   installation purposes using another non Linux machine. There are
   several micro Linux distributions out there that boot from one or two
   floppies or CD/DVD.

   Also a [http://tldp.org/HOWTO/Bootdisk-HOWTO/index.html]
   BootDisk-HOWTO is available. Thanks to Matthew D. Franz maintainer of
   [http://www.trinux.org/] Trinux for this tips and collecting most of
   the following URLs. Search also for "mini distribution" at
   [http://freshmeat.net/] FreshMeat.

    1. [http://www.knopper.net/knoppix/index-en.html] Knoppix by Klaus
       Knopper is a bootable CD with a collection of GNU/Linux software,
       automatic hardware detection, and support for many graphics
       cards, sound cards, SCSI and USB devices and other peripherals.
       KNOPPIX can be used as a Linux demo, educational CD, rescue
       system, or adapted and used as a platform for commercial software
       product demos. It is not necessary to install anything on a hard
       disk. Due to on-the-fly decompression, the CD can have up to 2 GB
       of executable software installed on it. A kix (Knoppix mini CD)
       is now available in the contrib directory.
    2. [http://sunsite.auc.dk/mulinux/] MuLinux by Michele Andreoli.
    3. [http://www.toms.net/~toehser/rb/] tomsrbt "The most Linux on one
       floppy. (distribution or panic disk)." by Tom Oehser.
    4. Trinux [http://www.trinux.org/] Trinux "A Linux Security Toolkit"
       by Matthew D. Franz.
    5. [http://www.psychosis.com/linux-router/] LRP "Linux Router
       Project"
    6. [http://home.sol.no/~okolaas/hal91.html] hal91
       [http://chris.silmor.de/hal91/] hal91 is a very small Linux
       distribution that fits on one floppy disk. You need at least a
       386 machine (FPU not necessary) with 8 mb ram to run HAL91. The
       entire system runs in ram, so you can remove the floppy after
       booting. The kernel supports IDE hard disks and ATAPI cdrom
       drives. Supported filesystems are ext2, iso9660 and vfat,
       optional encryption using AES is possible. Limited support for
       ethernet cards (NE2000 only) is also included. Support for scsi
       adapters, parallel zip drive and other ethernet cards is possible
       by loading kernel modules from an optional package.
    7. [http://www.zelow.no/floppyfw/] floppyfw by Thomas Lundquist.
    8. [http://www.kiarchive.ru/pub/linux/mini-linux/] minilinux:
       Minimal linux package. UMSDOS filesystem (no repartition), TCP/IP
       and SLIP/PPP, X Windows including Xmosaic. Support Soundblaster,
       mouse, modem, SCSI.
    9. [http://sunsite.bilkent.edu.tr/pub/linux/monkey/docs/english.htm]
       Monkey Linux is a minimal Linux ELF distribution in 7.5MB archive
       (5 diskettes) designed to be used within MSDOS and to allow the
       user to experiment with Linux anywhere he/she wants.
   10. [http://web.archive.org/web/*/http://www.wu-wien.ac.at/usr/h93/h9
       301726/dlx.html] DLX by Erich Boehm is a full featured linux
       system running on Intel PC's. The special thing is that DLX comes
       with only one 3,5" floppydisk. DLX boots with a kernel >= 1.3.89
       and starts a ramdisk image. In addition to that DLX also has a
       writeable ext2 filesystem of about 130 kb on the same disk to
       easily store configuration scripts (survives booting, is not on
       the ramdisk !). Further is DLX fully prepared for the
       paralell-port ZIP-Drive which allows you to mount 100 mb disks.
       You can even put large programs like perl5 on the disk because a
       special directory on the ZIP-disk is mounted as /usr/local/*!
   11. [http://metalab.unc.edu/pub/Linux/kernel/images/] C-RAMDISK
       creates a bootable X Windows system that fits on two 1.44 MB
       floppies. The kernel (2.0.26) includes networking (PPP and dialin
       script, NE2000, 3C509) and the driver for the parallel port ZIP
       drive as modules. The file system contains pppd, rlogin, tar and
       ncftp and a small X Windows system. Requires a Linux system (with
       2.0.0 kernel or above) to create the 2 floppies. The cramdisk
       floppy set will boot to "xdm" on a 486/pentium with 16MB RAM. For
       networking, the IP addresses and/or ppp dialin sequence need to
       be set. A method for modifying the floppy image is included.
   12. [http://pocket-linux.coven.vmh.net/] pocket-linux
   13. [http://www.linuxlots.com/~fawcett/yard/] YARD
   14. [http://linux.apostols.org/guru/wen/] ODL
   15. [http://www.superant.com/smalllinux/] SmallLinux by Steven
       Gibson. Three disk micro-distribution of Linux and utilities.
       Based on kernel 1.2.11. Root disk is ext2 format and has fdisk
       and mkfs.ext2 so that a harddisk install can be done. Useful to
       boot up on old machines with less than 4MB of RAM.
   16. [ftp://ftp.blueznet.com/pub/colorg] cLIeNUX by Rick Hohensee
       client-use-oriented Linux distribution
   17. [http://metalab.unc.edu/pub/Linux/kernel] linux-lite by Paul
       Gortmaker for very small systems with less than 2MB RAM and 10MB
       harddisk space (1.x.x kernel)
   18. See also the packages at
       [http://metalab.unc.edu/pub/Linux/system/recovery/!INDEX.html]
       MetaLab formerly known as SunSite and the
       [http://tldp.org/HOWTO/Bootdisk-HOWTO/index.html] Boot-Disk-HOWTO
       .
   19. You may also consider some of the boot floppies provided by
       various distributions falling into this category, e.g. the
       boot/rescue floppy of Debian/GNU Linux.
   20. If you like to build your own flavour of a boot floppy you may do
       so manually, as described in the
       [http://tldp.org/HOWTO/Bootdisk-HOWTO/index.html] Boot-Disk-HOWTO
       or using some helper tools, for instance mkrboot (provided at
       least as a Debian/GNU Linux package) or pcinitrd, which is part
       of the PCMCIA-CS package by David Hinds.
   21. Also you might try to build your Linux system on a ZIP drive.
       This is described in the [http://tldp.org/HOWTO/ZIP-Install.html]
       ZIP-Install-HOWTO .
     ________________________________________________________________

Appendix E. Dealing with Limited Resources or Tuning the System

E.1. Related Documentation

    1. [http://www.tldp.org/HOWTO/LBX.html] LBX-HOWTO
    2. [http://tldp.org/HOWTO/Small-Memory/] Small-Memory-HOWTO
    3. [http://www-128.ibm.com/developerworks/linux/library/l-lwl1/]
       Lightweight Linux, Part 1: Hardware is only as old as the
       software it runs: a modern operating system and up-to-date
       applications return an older system to productivity. This article
       provides best practices and step-by-step guidance on how to build
       a working Linux system on older hardware or on modern hardware
       with limited memory and storage.
     ________________________________________________________________

E.2. Introduction

   As mentioned in the introduction laptops sometimes have less
   resources if you compare them to desktops. To deal with limited
   space, memory, CPU speed and battery power, I have written this
   chapter.
     ________________________________________________________________

E.3. Small Space

E.3.1. Introduction

   There are different types of techniques to gain more disk space, such
   as sharing of space, freeing unused or redundant space, filesystem
   tuning and compression. Note: some of these techniques use memory
   instead of disk space. As you will see, there are many small steps
   necessary to free some space.
     ________________________________________________________________

E.3.2. Techniques

    1. Stripping: Though many distributions come with stripped binaries
       today it is useful to check this. For details see man strip. To
       find every unstripped file you can use the file command or more
       convenient the tool findstrip. Attention: don't strip libraries,
       sometimes the wrong symbols are removed due to a bad programming
       technique. Or use the --strip-unneeded option.
    2. Perforation: zum(1) reads a file list on stdin and attempts to
       perforate these files. Perforation means, that series of null
       bytes are replaced by lseek, thus giving the file system a chance
       of not allocating real disk space for those bytes. Example: find
       . -type f | xargs zum
    3. Remove Odd Files and Duplicates: Check your system for core
       files, emacs recovery files <#FILE#> vi recovery files
       <FILE>.swp, RPM recovery files <FILE>.rpmorig and patch recovery
       files. Find duplicates, you may try finddup. Choose a system to
       name your backup, temporary and test files, e.g. with a signature
       at the end.
    4. Clean Temporary Files: , e.g. /tmp, there is even a tool
       tmpwatch.
    5. Shorten the Log Files: usually the files in /var/log. You may use
       logrotate to achieve this task.
    6. Remove Files: Remove files which are not "necessary" under all
       circumstances such as man pages, documentation /usr/doc and
       sources e.g. /usr/src .
    7. Unnecessary Libraries: You may use the binstats package to find
       unused libraries (Thanks to Tom Ed White).
    8. Filesystem: Choose a filesystem which treats disk space
       economically e.g. rsfs. Tune your filesystem e.g. tune2fs. Choose
       an appropriate partition and block size.
    9. Reduce Kernel Size: Either by using only the necessary kernel
       features and/or making a compressed kernel image bzImage.
   10. Compression: I didn't check this but as far as I know you may
       compress your filesystem with gzip and decompress it on the fly.
       Alternatively you may choose to compress only certain files. You
       can even execute compressed files with zexec
   11. Compressed Filesystems: - For e2fs filesystems there is a
       compression version available [http://e2compr.sourceforge.net/]
       e2compr.
       - [http://cmp.felk.cvut.cz/~pisa/dmsdos/] DMSDOS which enables
       your machine to access Windows95 compressed drives (drivespace,
       doublestacker). If you don't need DOS/Windows95 compatibility,
       i.e. if you want to compress Linux-only data, this is really
       discouraged by the author of the program.
   12. Partition Sharing: You may share swap-space (see
       [http://tldp.org/HOWTO/Swap-Space.html] Swap-Space-HOWTO) or data
       partitions between different OS (see mount). For mounting MS-DOS
       Windows95 compressed drives (doublespace, drivespace) you may use
       dmsdos
       [http://metalab.unc.edu/pub/Linux/system/filesystems/dosfs/]
       dosfs/ .
   13. Libraries: Take another (older) library, for instance libc5 ,
       this library seems to be smaller than libc6 also known as glibc2
       .
   14. Kernel: If your needs are fitted with an older kernel version,
       you can save some space.
   15. GUI: Avoid as much Graphical User Interface (GUI) as possible.
   16. Tiny Distributions: There are some distributions available which
       fit from one 3.5" floppy to 10MB disk space and fit for small
       memories, too. See Appendix A Appendix D and below.
   17. External Storage Devices (Hard Disks, ZIP Drives, NFS, SAMBA):
       Since many notebooks may be limited in their expandability, using
       the parallel port is an attractive option. There are external
       hard disks and ZIP Drives available. Usually they are also
       connectable via PCMCIA. Another way is using the resources of
       another machine through NFS or SAMBA etc.
   18. Purging of uneeded locales: localepurge for Debian is just a
       simple script to recover disk space wasted for unneeded locale
       files and localized man pages. Depending on your installation, it
       is possible to save some 200, 300, or even more megabytes of disk
       space usually dedicated for locales you'll probably never have
       any usage for.
     ________________________________________________________________

E.4. Hard Disk Speed

   Use the tool hdparm to set up better harddisk performance. Though I
   have seen laptop disk enabled with striping, I can't see a reason to
   do so, because in my humble opinion also known as RAID0 striping
   needs at least two different disks to increase performance. Before
   using hdparm check the BIOS settings for harddisk parameters like DMA
   or ATA4 or 32bit transfer. The bad thing is that if something is
   disabled there - it can not be enabled with hdparm!

   See UNIX and LINUX Computing Journal:
   [http://www.diverge.org/ulcj/199910tfsp.shtml] Tunable Filesystem
   Parameters in /proc How to increase, decrease and reconfigure
   filesystem behavior from within /proc.
     ________________________________________________________________

E.5. Small Memory

E.5.1. Related Documentation

    1. [http://tldp.org/HOWTO/Small-Memory/index.html]
       Small-Memory-HOWTO
    2. [http://tldp.org/HOWTO/Module-HOWTO/] Module-HOWTO
    3. [http://tldp.org/HOWTO/Kerneld/] Kerneld-HOWTO
     ________________________________________________________________

E.5.2. Techniques

   Check the memory usage with free and top.

   [http://www.complang.tuwien.ac.at/ulrich/mergemem/] Mergemem Project
   . Many programs contain memory areas of the same content that remain
   undetected by the operating system. Typically, these areas contain
   data that have been generated on startup and remain unchanged for
   longer periods. With mergemem such areas are detected and shared. The
   sharing is performed on the operating system level and is invisible
   to the user level programs. mergemem is particularly useful if you
   run many instances of interpreters and emulators (like Java or
   Prolog) that keep their code in private data areas. But also other
   programs can take advantage albeit to a lesser degree.

   You may also reduce the kernel size as much as possible by removing
   any feature which is not necessary for your needs and by modularizing
   the kernel as much as possible.

   Also you may shutdown every service or daemon which is not needed,
   e.g. lpd, mountd, nfsd and close some virtual consoles. Please see
   [http://tldp.org/HOWTO/Small-Memory/] Small-Memory-HOWTO for details.

   And of course use swap space, when possible.

   If possible you use the resources of another machine, for instance
   with X11, VNC or even telnet. For more information on Virtual Network
   Computing (VNC), see [http://www.realvnc.com/] VNC.
     ________________________________________________________________

E.6. Low CPU Speed

   You may want to overdrive the CPU speed but this can damage your
   hardware and I don't have experience with it. For some examples look
   at [http://www.silverace.com/libretto/] Adorable Toshiba Libretto -
   Overclocking.
     ________________________________________________________________

E.7. Power Saving Techniques

    1. If you don't need infrared support, disable it in the BIOS or
       shutdown the IrDA� device driver. There are also some IrDA�
       features of the kernel which are useful for saving power.
    2. PCMCIA services consume much power, so shut them down if you
       don't need them.
    3. I'm not sure to which extend the backlight consumes power.

       Warning

   As far as I know this device can only bear a limited number of uptime
   circles. So avoid using screensavers, which turn off the backlight.
       If you want do it anyhow, you may use xset +dpms and xset dpms 0
       0 300 This turns the screen off after 5 minutes of inactivity.
       Works only if the display is DPMS capable.
    4. For some examples to build batteries with increased uptime up to
       8 hours look at [http://repair4laptop.org/notebook_battery.html]
       Repair4Laptop: Battery .
    5. For information about APM look at the chapter APM above.
    6. The "noatime" option when mouting filesystems tells the kernel to
       not update the access time information of the file. This
       information, although sometimes useful, is not used by most
       people. Therefore, you can safely disable it, then preventing
       disk access each time you cat a file. Here is an example of a
       /etc/fstab with this power-saving option: /dev/hda7 /var ext2
       defaults,noatime 0 2
    7. [http://sourceforge.net/projects/hdparm/] hdparm hdparm is a
       Linux disk utility that lets you set spin-down timeouts and other
       disk parameters.
    8. [http://www.complang.tuwien.ac.at/ulrich/linux/tips.html] Mobile
       Update Daemon This is a drop-in replacement for the standard
       update daemon, mobile-update minimizes disk spin ups and reduces
       disk uptime. It flushes buffers only when other disk activity is
       present. To ensure a consistent file system call sync manually.
       Otherwise files may be lost on power failure. mobile-update does
       not use APM. So it works also on older systems.
    9. [http://noflushd.sourceforge.net/] noflushd : noflushd monitors
       disk activity and spins down disks that have been idle for more
       than <timeout> seconds. It requires a kernel >=2.2.11 . Useful in
       combination with hdparm and mount with noatime option to bring
       down disk activity.
       Here are some comments and thoughts by Nat Makarevitch about a
       possible approach which may reduce the disk activity under Linux
       (sparing energy, especially with noflushd) the file
       Documentation/filesystems/proc.txt of the Linux sourcetree
       documents some useful features, esp. in the /proc/sys/vm section.
       Under Linux 2.2 I used:

echo "100 5000 8 256 500 60000 60000 1884 2" > /proc/sys/vm/bdflush

       especially under Linux 2.4 which uses its spare time to
       'pre-save' the less-used memory pages into the swap, increasing
       the disk activity I tried to figure the more adequate parameters
       (Linux 2.4.9, 192 MB RAM, Toshiba 3480 laptop) beware: some of
       those parameters may be dangerous or useless (I have not gathered
       serious data about the practical efficiency). moreover do not
       forget that delaying disk writes of data is intrinsically
       dangerous

echo 99 512 32 512 0 300000 60 0 0 > /proc/sys/vm/bdflush
# is '60' the max value for age_super?
echo 1 1 96 > /proc/sys/vm/buffermem
echo 512 128 32 > /proc/sys/vm/kswapd
echo 1 10 96 > /proc/sys/vm/pagecache

   10. The [http://www.buzzard.me.uk/toshiba/index.html] Toshiba Linux
       Utilities are a set of Linux utilities for controlling the fan,
       supervisor passwords, and hot key functions of Toshiba Pentium
       notebooks. There is a KDE package Klibreta, too.
   11. At Kenneth E. Harker's page there is a recommendation for LCDproc
       [http://lcdproc.omnipotent.net/] LCDProc . "LCDproc is a small
       piece of software that will enable your Linux box to display live
       system information on a 20x4 line backlit LCD display. This
       program shows, among other things, battery status on notebooks."
       I tried this package and found that it connects only to the
       external [http://www.matrixorbital.com/] Matrix-Orbital LCD 20x4
       display , which is a LCD display connected to a serial port. I
       can't see any use for a laptop yet, but you might use it to build
       a wearable.
   12. The [http://sourceforge.net/projects/diald/] Diald Dial Daemon
       provides on demand Internet connectivity using the SLIP or PPP
       protocols. Diald can automatically dial in to a remote host when
       needed or bring down dial-up connections that are inactive.
   13. [http://www.kde.org] KDE provides KAPM, Kbatmon and Kcmlaptop.
       Written by Paul Campbell kcmlaptop is a set of KDE control panels
       that implements laptop computer support functions, it includes a
       dockable battery status monitor for laptops - in short a little
       icon in the KDE status bar that shows how much battery time you
       have left. It also will warn you when power is getting low and
       allows you to configure power saving options. Similar packages
       you may find at the GNOME project [http://www.gnome.org/] GNOME .
       See the software maps at both sites.
   14. Please see the [http://tldp.org/HOWTO/Battery-Powered/]
       Battery-Powered-HOWTO for further information.

   Some more words about disks spin down with noflushd or hdparm
   utilities. The objective is to reduce hard disk usage to minimum,
   because on most laptops it is the primary source of noise and energy
   consumption. The "noflushd" daemon is a replacement of "update" which
   makes buffer updates on disk only when some other data is being read
   from the disk (the behavior of "update" is to flush buffers every 5
   seconds, and it usually generates constant disk activity, so that the
   disk never becomes idle). "noflushd" also sets the disk spindown time
   and automatically calls "sync" before spindown. The syntax is
   something like "noflushd -n 5 /dev/had". Using "noflushd" may cause
   loss of data if some files were edited while the disk was parked and
   not sync'ed, e.g. if the power was suddenly lost.

   The hdparm utility can set the sleep time too, and also tune the IDE
   disk parameters for better performance. Make sure that the kernel IDE
   parameter "Use DMA by default when available" (section "Block
   devices") is enabled.

   However, it is not enough to enable noflushd or IDE disk sleep time
   to make the disk effectively silent, because the system in most
   default installations is running many cron jobs, writes to log files,
   uses swap and so on. This activity is not always desirable,
   especially if the computer is standalone (not on network) and is used
   mostly by one user. Here are some recommendations.

   First, the cron daemon and friends (anacron, atd, logrotate, sendmail
   / exim / ...) could be removed from the system if the services they
   run (such as, cleaning /tmp directories and logs, checking email
   etc.) are not needed.

   Secondly, the syslogd configuration file /etc/syslog.conf should be
   modified to reduce the number of log files and messages logged, and
   also to have "-" signs before every file name (which means that the
   system will not have to sync the disk every time a message is
   logged).

   Also, it is advisable to add "mark:none;" to the "syslog" strings, so
   that the "strich strich strich MARK strich strich strich" messages do
   not get written to the log files every half an hour. Typical Linux
   installations today have too many log files for the home user.

   Finally, the disk may not go to sleep when a lot of swap space is in
   use. Type "free" and see how much swap is being used and how much
   free RAM is available. If you think there is enough free RAM to work
   without swap, or if there is a lot of swap used AND also a lot of
   free RAM, consider freeing the swap space ("su; swapoff -a; swapon
   -a") or switching the swap space off altogether ("su; swapoff -a").
   Working without swap should be fine on systems with 64MB or more of
   RAM. (Working without swap will reduce the available memory, of
   course, and some software crashes without warning when it runs out of
   memory. But, adding swap will not prevent the crash resulting from
   some runaway memory consumuing software, it will only delay it, and
   it will make the system swap a lot before it happens.)

   With these changes in the system, one could get the laptop to work
   for extended periods of time with its hard disk switched off.

   The kernel can be configured with "Yes" to "APM Support" and "Enable
   console blanking using APM" (section "General setup"). Then the LCD
   screen lamp will shut off in console mode (so not just the screen
   goes black, but also the lamp). In X mode, the same effect can be
   obtained with "xset +dpms" (enable DPMS function) and "xset s blank"
   (enable screen blanking). One can add these commands to the X window
   session or window manager initialization scripts.

   The computer's BIOS energy savings options (hard disk sleep time,
   video blanking time and so on) are probably not useful and in some
   cases may even cause crashes. Therefore they could be disabled in the
   laptop's BIOS.
     ________________________________________________________________

E.8. Kernel

E.8.1. Related Documentation

     * [http://tldp.org/HOWTO/Kernel-HOWTO/] Kernel-HOWTO
     * [http://tldp.org/HOWTO/BootPrompt-HOWTO.html] BootPrompt-HOWTO

   Many kernel features are related to laptops. For instance APM, IrDA�,
   PCMCIA and some options for certain laptops, e.g. IBM(TM) ThinkPads.
   In some distributions they are not included by default. And the
   kernel is usually bigger than necessary. So it's seems a good idea to
