    tracks, sectors , and cylinders. It is also sometimes (incorrectly) a
    term used to signify the action of writing a filesystem to a disk
    (especially in the MS Windows/MS DOS world).

fragmented
    When a file is not written to a disk in contiguous blocks. If there is
    not enough free space to write a full file to a disk in one continuous
    stream of blocks then the file gets split up between two or more parts of
    the disk surface. This is known as fragmenting and can make the time for
    loading a file longer as the disk has to seek for the rest of the file.

full backup
    Taking a copy of the whole filesystem to a backup media (eg tape, floppy,
    or CD).

geometry
    How many cylinders, sectors per cylinder and heads a disk drive has.

high level formatting
    An incorrect term for writing a filesystem to a disk. Often used in the
    MS Windows and MS DOS world.

incremental backups
    A backup of what has changed in a filesystem since the last full backup.
    Incremental backups if used sensibly as part of a backup regime, can save
    a lot of time and effort in maintaining a backup of data.

inode
    A data structure holding information about files in a Unix file system.
    There is an inode for each file and a file is uniquely identified by the
    file system on which it resides and its inode number on that system. Each
    inode contains the following information: the device where the inode
    resides, locking information, mode and type of file, the number of links
    to the file, the owner's user and group ids, the number of bytes in the
    file, access and modification times, the time the inode itself was last
    modified and the addresses of the file's blocks on disk. A Unix directory
    is an association between file leafnames and inode numbers. A file's
    inode number can be found using the "-i" switch to ls.

iSCSI
    A network storage protocol that enables the sending of SCSI commands over
    a TCP/IP network. Primarily used in Storage Area Networks.

kernel
    Part of an operating system that implements the interaction with hardware
    and the sharing of resources. See also system program.

local time
    The official time in a local region (adjusted for location around the
    Earth); established by law or custom.

logical partition
    A partition inside an extended partition, which is ``logical'' in that it
    does not exist in reality, but only inside the logical structure of the
    software.

logical volume manager (LVM)
    A collection of programs that allow larger physical disks to be
    reassembled into "logical" disks that can be shrunk or expanded as data
    needs change.

low level formatting
    Synonymous with formatting and used in the MS DOS world so differentiate
    from creating a filesystem which is also known as formatting sometimes.

mail transfer agent
    (MTA) The program responsible for delivering e-mail messages. Upon
    receiving a message from a mail user agent or another MTA it stores it
    temporarily locally and analyzes the recipients and either delivers it
    (local addressee) or forwards it to another MTA. In either case it may
    edit and/or add to the message headers. A widely used MTA for Unix is
    sendmail.

mail user agent
    (MUA) The program that allows the user to compose and read electronic
    mail messages. The MUA provides the interface between the user and the
    mail transfer agent . Outgoing mail is eventually handed over to an MTA
    for delivery while the incoming messages are picked up from where the MTA
    left it (although MUAs running on single-user machines may pick up mail
    using POP). Examples of MUAs are pine, elm and mutt.

master boot record
    (MBR) The first logical sector on a disk, this is (usually) where the
    BIOS looks to load a small program that will boot the computer.

network file system
    (NFS) A protocol developed by Sun Microsystems, and defined in RFC 1094
    (FIND URL), which allows a computer to access files over a network as if
    they were on its local disks.

operating system
    Software that shares a computer system's resources (processor, memory,
    disk space, network bandwidth, and so on) between users and the
    application programs they run. Controls access to the system to provide
    security. See also kernel, system program, application program.

partition
    A logical section of a disk. Each partition normally has its own file
    system. Unix tends to treat partitions as though they were separate
    physical entities.

password file
    A file that holds usernames and information about their accounts like
    their password. On Unix systems this file is usually /etc/passwd. On most
    modern Linux systems the /etc/passwd file does not actually hold password
    data. That tends to be held in a different file /etc/shadow for security
    reasons. See manual pages passwd(5) and shadow(5) for more information.

physical extents
    A term used to describe a the chunks a physical volume is broken down
    into when using the Logical Volume Manager.

physical volume
    A term used an actual disk partition, usually in reference to the logical
    volume manager.

platters
    A physical disk inside a hard drive. Usually a hard drive is made up of
    multiple physical disks stacked up on top of each other. One individual
    disk is known as a platter .

power on self test
    (POST) A series of diagnostic tests which are run when a computer is
    powered on. Typically this might include testing the memory, testing that
    the hardware configuration is the same as the last saved configuration,
    checking that any floppy drives, or hard drives which are known about by
    the BIOS are installed and working.

print queue
    A file (or set of files) which the print daemon uses so that applications
    which wish to use the printer do not have to wait until the print job
    they have sent is finished before they can continue. It also allows
    multiple users to share a printer.

read-write head
    A tiny electromagnetic coil and metal pole used to write and read
    magnetic patterns on a disk. These coils move laterally against the
    rotary motion on the platters.

root filesystem
    The parent of all the other filesystems mounted in a Unix filesystem
    tree. Mounted as / it might have other filesystems mounted on it (/usr
    for example). If the root filesystem cannot be mounted then the kernel
    will panic and the system will not be able to continue booting

run level
    Linux has up to 10 runlevels (0-9) available (of which usually only the
    first 7 are defined). Each runlevel may start a different set of
    services, giving multiple different configurations in the same system.
    Runlevel 0 is defined as ``system halt'', runlevel 1 is defined as
    ``single user mode'', and runlevel 6 is defined as ``reboot system''. The
    remaining runlevels can, theoretically, be defined by the system
    administrator in any way. However most distributions provide some other
    predefined runlevels. For example, runlevel 2 might be defined as
    ``multi-user console'', and runlevel 5 as ``multi-user X-Window system''.
    These definitions vary considerably from distribution to distribution, so
    please check the documentation for your own distribution.

sectors
    The minimum track length that can be allocated to store data. This is
    usually (but not always) 512 bytes.

shadow passwords
    Because the password file on Unix systems often needs to be world
    readable it usually does not actually contain the encrypted passwords for
    users' accounts. Instead a shadow file is employed (which is not world
    readable) which holds the encrypted passwords for users' accounts.

single user mode
    Usually runlevel 1. A runlevel where logins are not allowed except by the
    root account. Used either for system repairs (if the filesystem is
    partially damaged it may still be possible to boot into runlevel 1 and
    repair it), or for moving filesystems around between partitions. These
    are just two examples. Any task that requires a system where only one
    person can write to a disk at a time is a candidate for requiring
    runlevel 1.

spool
    To send a file (or other data) to a queue. Generally used in conjunction
    with printers, but might also be used for other things (mail for
    example). The term is reported to be an acronym for ``Simultaneous
    Peripheral Operation On-Line'', but according to the Jargon File it may
    have been a backronym (something made up later for effect).

system call
    The services provided by the kernel to application programs, and the way
    in which they are invoked. See section 2 of the manual pages.

swap space
    Space on a disk in which the system can write portions of memory to.
    Usually this is a dedicated partition, but it may also be a swapfile.

system program
    Programs that implement high level functionality of an operating system,
    i.e., things that aren't directly dependent on the hardware. May
    sometimes require special privileges to run (e.g., for delivering
    electronic mail), but often just commonly thought of as part of the
    system (e.g., a compiler). See also application program, kernel,
    operating system.

time drift
    This is a term for a computers inaccuracy at keeping track of time. All
    computers have some rate of error when keeping time. With newer computers
    this rate of error is extremely small.

track
    The part of a disk platter which passes under one read-write head while
    the head is stationary but the disk is spinning. Each track is divided
    into sectors, and a vertical collection of tracks is a cylinder

volume group
    A collection of physical volumes broken down into physical extents, and
    available for use in logical partitions.


-----------------------------------------------------------------------------
Index-Draft

A

at , Periodic command execution: cron and at

-----------------------------------------------------------------------------
B

BIOS, The root filesystem, Hard disks, Partitioning a hard disk
booting
    vmlinuz, The root filesystem





-----------------------------------------------------------------------------
C

CMOS, Hard disks
commands
    badblocks, Formatting


    cfdisk, Partitioning a hard disk


    chsh, The /etc directory


    depmod, depmod


    df, The /etc directory


    fdformat, Formatting


    fdisk, The MBR, boot sectors and partition table, Partition types,
        Partitioning a hard disk


    file, The /etc directory


    fips, Partitioning a hard disk


    free, The /proc filesystem


    fsck, Formatting


    ftpd, The /etc directory


    getty, init, The /etc directory


    gzexe, Tips for saving disk space


    gzip, Tips for saving disk space


    hdparm, The hdparm command


    init, init


    insmod, insmod


    login, The /etc directory, The /var filesystem


    losetup, The /dev directory


    lpr, Two kinds of devices


    ls, Two kinds of devices


    lsdev, The lsdev command


    lsmod, lsmod


    lspci, The lspci command


    lsraid, The lsraid command


    lsusb, The lsusb command


    MAKEDEV, The /dev directory, The MAKEDEV Script, The mknod command


    man, The /var filesystem


    mkfs, Formatting


    mknod, The mknod command


    modprobe, modprobe


    mount, The /etc directory, The /dev directory


    parted, Partitioning a hard disk


    rmmod, rmmod


    setfdparm, Floppies


    setfdprm, The /etc directory, Formatting


    su, The /etc directory


    sudo, The /etc directory


    swapon, The /etc directory


    syslog, The /var filesystem, Formatting


    zip, Tips for saving disk space




Common Internet File System (CIFS), Network file systems, Network Attached
    Storage - Draft, CIFS
cron, Periodic command execution: cron and at
    crontab , Periodic command execution: cron and at





-----------------------------------------------------------------------------
D

devices
    block, Two kinds of devices


    character, Two kinds of devices




disks, Using Disks and Other Storage Media
    bad blocks, Formatting


    bad sectors, Formatting


    boot sectors, The MBR, boot sectors and partition table


    changing partition size, Partitioning a hard disk


    components, Hard disks


    cylinders, Hard disks


    extended partition, Extended and logical partitions, Device files and
        partitions


    filesystem, What are filesystems?
        data block, What are filesystems?
        directory block, What are filesystems?
        indirection block, What are filesystems?
        inode, What are filesystems?
        superblock, What are filesystems?


    formatting, Formatting
        high-level, Formatting
        low-level, Formatting


    geometry, Hard disks


    IDE, Partitioning a hard disk


    Logical Block Addressing (LBA), Partitioning a hard disk


    MBR, The MBR, boot sectors and partition table


    partition table, The MBR, boot sectors and partition table


    partition type, Partition types


    partitions, Partitions


    saving space, Tips for saving disk space


    sectors, Hard disks


    tracks, Hard disks





-----------------------------------------------------------------------------
E

email, Mail

-----------------------------------------------------------------------------
F

fibre channel, Storage Area Networks - Draft
filesystem, The filesystem layout, The /usr filesystem.
    / (root), Background, The root filesystem


    /bin, The filesystem layout, The root filesystem


    /boot, The root filesystem


    /dev, The filesystem layout, The root filesystem, The /dev directory, Two
        kinds of devices
        /dev/dsp, The /dev directory
        /dev/fb0, The /dev directory
        /dev/fd0, The /dev directory, Floppies, Formatting
        /dev/fd1, Floppies
        /dev/had, The /dev directory, Hard disks
        /dev/hdb, The /dev directory, Hard disks
        /dev/hdc, The /dev directory, Hard disks
        /dev/hdc9, The /dev directory
        /dev/hdd, The /dev directory, Hard disks
        /dev/ht0, The /dev directory
        /dev/js0, The /dev directory
        /dev/loop0, The /dev directory
        /dev/lp0, The /dev directory
        /dev/md0, The /dev directory
        /dev/mixer, The /dev directory
        /dev/null, The /dev directory
        /dev/parport0, The /dev directory
        /dev/pcd0, The /dev directory
        /dev/pda, The /dev directory
        /dev/pdb, The /dev directory
        /dev/pdc, The /dev directory
        /dev/pdd, The /dev directory
        /dev/psaux, The /dev directory
        /dev/pt0, The /dev directory
        /dev/pt1, The /dev directory
        /dev/random, The /dev directory
        /dev/sda, The /dev directory, Two kinds of devices, Hard disks
        /dev/sdb, The /dev directory, Hard disks
        /dev/sdd, The /dev directory
        /dev/ttyS0, The /dev directory, The MAKEDEV Script, The mknod command
        /dev/urandom, The /dev directory
        /dev/zero, The /dev directory


    /etc, The filesystem layout, The root filesystem, The /etc directory
        /etc/bash.rc, The /etc directory
        /etc/csh.cshrc, The /etc directory
        /etc/fdprm, The /etc directory, Floppies
        /etc/fstab, The /etc directory
        /etc/group, The /etc directory
        /etc/inittab, The /etc directory
        /etc/issue, The /etc directory
        /etc/login.defs, The /etc directory
        /etc/magic, The /etc directory
        /etc/motd, The /etc directory
        /etc/mtab, The /etc directory
        /etc/passwd, The /etc directory
        /etc/printcap, The /etc directory
        /etc/profile, The /etc directory
        /etc/rc.d, The /etc directory
        /etc/securetty, The /etc directory
        /etc/shadow, The /etc directory
        /etc/shells, The /etc directory
        /etc/termcap, The /etc directory


    /home, The filesystem layout, Background, The root filesystem


    /lib, The filesystem layout, The root filesystem


    /lib/modules, The root filesystem


    /mnt, The root filesystem


    /proc, The root filesystem, The /proc filesystem, Filesystems galore
        /proc/1, The /proc filesystem
        /proc/cpuinfo, The /proc filesystem
        /proc/devices, The /proc filesystem
        /proc/dma, The /proc filesystem
        /proc/filesystems, The /proc filesystem
        /proc/interrupts, The /proc filesystem
        /proc/ioports, The /proc filesystem
        /proc/kcore, The /proc filesystem, Filesystems galore
        /proc/kmsg, The /proc filesystem
        /proc/ksyms, The /proc filesystem
        /proc/loadavg, The /proc filesystem
        /proc/meminfo, The /proc filesystem
        /proc/modules, The /proc filesystem
        /proc/net, The /proc filesystem
        /proc/self, The /proc filesystem
        /proc/stat, The /proc filesystem
        /proc/uptime, The /proc filesystem
        /proc/version, The /proc filesystem


    /root, The root filesystem


    /sbin, The root filesystem


    /tmp, The root filesystem, The /var filesystem


    /usr, The filesystem layout, Background, The root filesystem
        /usr/bin, The /usr filesystem.
        /usr/include, The /usr filesystem.
        /usr/lib, The /usr filesystem.
        /usr/local, The /usr filesystem., The /var filesystem
        /usr/sbin, The /usr filesystem.
        /usr/share/doc, The /usr filesystem.
        /usr/share/info, The /usr filesystem.
        /usr/share/man, The /usr filesystem.
        /usr/share/man/cat, The /var filesystem
        /usr/share/man/man, The /var filesystem
        /usr/X11R6, The /usr filesystem.


    /var, The filesystem layout, Background, The root filesystem, The /var
        filesystem
        /var/cache/man, The /var filesystem
        /var/games, The /var filesystem
        /var/lib, The /var filesystem
        /var/local, The /var filesystem
        /var/lock, The /var filesystem
        /var/log, The /var filesystem
        /var/log/messages, The /var filesystem
        /var/log/wtmp, The /var filesystem
        /var/mail, The /var filesystem
        /var/run, The /var filesystem
        /var/spool, The /var filesystem
        /var/spool/mail, The /var filesystem
        /var/spool/news, The /var filesystem
        /var/tmp, The /var filesystem
        /var/utmp, The /var filesystem




Filesystem Hierarchy Standard (FHS) , The filesystem layout, Overview of the
    Directory Tree, Background
filesystem types
    ext, Filesystems galore


    ext2, Filesystems galore, Filesystem comparison


    ext3, Filesystems galore, Filesystem comparison


    fat16, Filesystem comparison


    fat32, Filesystem comparison


    hfs+, Filesystem comparison


    hpfs, Filesystems galore, Filesystem comparison


    iso9660, Filesystems galore


    jfs, Filesystems galore, Filesystem comparison


    minix, Filesystems galore


    msdos, Filesystems galore


    nfs, Filesystems galore


    ntfs, Filesystems galore, Filesystem comparison


    reiserfs, Filesystems galore, Filesystem comparison


    smbfs, Filesystems galore


    sysv, Filesystems galore


    ufs2, Filesystem comparison


    umsdos, Filesystems galore


    vfat, Filesystems galore


    vxfs, Filesystem comparison


    xfs, Filesystems galore


    xia, Filesystems galore


    zfs, Filesystem comparison




filesystems
    /etc
        /etc/fstab, Adding more disk space for Linux




Free Software Foundation, Linux or GNU/Linux, that is the question.

-----------------------------------------------------------------------------
G

getty, Logins from terminals, Network logins
GNOME, Graphical user interface
GRUB , The root filesystem
GUI, init, Graphical user interface
    blackbox, Graphical user interface


    fvwm, Graphical user interface


    icewm, Graphical user interface


    windowmaker , Graphical user interface


    X Windows, Graphical user interface





-----------------------------------------------------------------------------
H

hardware
    CD-ROM, CD-ROMs


    Central Processing Unit (CPU), Hard disks


    disk controller, Hard disks


    fibre channel, Storage Area Networks - Draft


    floppy disk, Floppies


    tape drive, Tapes





-----------------------------------------------------------------------------
I

init, init, Logins from terminals
inittab, init
iSCSI, Storage Area Networks - Draft
ISO 9660, CD-ROMs
    Rock Ridge extensions, CD-ROMs





-----------------------------------------------------------------------------
K

KDE, Graphical user interface
kernel
    devices, Hardware, Devices, and Tools


    documentation
        devices.txt, The mknod command


    driver, Important parts of the kernel


    memory management, Important parts of the kernel


    modules, Kernel Modules
        depmod, depmod
        insmod, insmod
        lsmod, lsmod
        modprobe, modprobe
        rmmod, rmmod


    NFS, Network file systems


    overview, Various parts of an operating system, Important parts of the
        kernel


    process management, Important parts of the kernel


    virtual filesystem (VFS), Important parts of the kernel





-----------------------------------------------------------------------------
L

LILO, The root filesystem, Partitioning a hard disk
Linux
    Distributions, Introduction


    GNU , Linux or GNU/Linux, that is the question.




logging in, Network logins
login, Logins from terminals
logs
    /var/log/messages, The /var filesystem, Formatting


    /var/log/wtmp, The /var filesystem





-----------------------------------------------------------------------------
M

mail transfer agent (MTA) , Mail
    postfix, Mail


    sendmail, Mail




mail user agent, Mail
    evolution, Mail


    pine, Mail





-----------------------------------------------------------------------------
N

Network Attached Storage (NAS), Network Attached Storage - Draft
Network File System (NFS), Network file systems, Background, Network Attached
    Storage - Draft, NFS
networking, Networking
    Network Admin Guide (NAG), Networking





-----------------------------------------------------------------------------
O

Open Sound System (OSS), The /dev directory

-----------------------------------------------------------------------------
P

partition types
    AIX, Partition types


    FAT16, Partition types


    FAT32, Partition types


    FreeBSD, Partition types


    HPFS, Partition types


    Linux, Partition types


    Linux LVM, Partition types


    Linux Swap, Partition types


    Minix, Partition types


    NetBSD, Partition types


    NTFS, Partition types




printing, Printing
    queue, Printing


    spools, Printing





-----------------------------------------------------------------------------
R

runlevels, init
    0 - shutdown, init


    1 - single user , init


    1 - single-user, init


    3 - multi-user, init


    5 - multi-user with GUI , init


    6 - reboot, init


    inittab, init





-----------------------------------------------------------------------------
