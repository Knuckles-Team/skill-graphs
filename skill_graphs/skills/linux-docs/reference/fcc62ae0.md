there can be additional ones as well, for example, to run X on the console.

Linux allows for up to 10 runlevels, 0-9, but usually only some of these are
defined by default. Runlevel 0 is defined as ``system halt''. Runlevel 1 is
defined as ``single user mode''. Runlevel 3 is defined as "multi user"
because it is the runlevel that the system boot into under normal day to day
conditions. Runlevel 5 is typically the same as 3 except that a GUI gets
started also. Runlevel 6 is defined as ``system reboot''. Other runlevels are
dependent on how your particular distribution has defined them, and they vary
significantly between distributions. Looking at the contents of /etc/inittab
usually will give some hint what the predefined runlevels are and what they
have been defined as.

In normal operation, init makes sure getty is working (to allow users to log
in) and to adopt orphan processes (processes whose parent has died; in UNIX
all processes must be in a single tree, so orphans must be adopted).

When the system is shut down, it is init that is in charge of killing all
other processes, unmounting all filesystems and stopping the processor, along
with anything else it has been configured to do.
-----------------------------------------------------------------------------

2.3.2. Logins from terminals

Logins from terminals (via serial lines) and the console (when not running X)
are provided by the getty program. init starts a separate instance of getty
for each terminal upon which logins are to be allowed. getty reads the
username and runs the loginprogram, which reads the password. If the username
and password are correct, login runs the shell. When the shell terminates,
i.e., the user logs out, or when login terminated because the username and
password didn't match, init notices this and starts a new instance of getty.
The kernel has no notion of logins, this is all handled by the system
programs.
-----------------------------------------------------------------------------

2.3.3. Syslog

The kernel and many system programs produce error, warning, and other
messages. It is often important that these messages can be viewed later, even
much later, so they should be written to a file. The program doing this is
syslog . It can be configured to sort the messages to different files
according to writer or degree of importance. For example, kernel messages are
often directed to a separate file from the others, since kernel messages are
often more important and need to be read regularly to spot problems.

Chapter 15 will provide more on this.
-----------------------------------------------------------------------------

2.3.4. Periodic command execution: cron and at

Both users and system administrators often need to run commands periodically.
For example, the system administrator might want to run a command to clean
the directories with temporary files (/tmp and /var/tmp) from old files, to
keep the disks from filling up, since not all programs clean up after
themselves correctly.

The cron service is set up to do this. Each user can have a crontab file,
where she lists the commands she wishes to execute and the times they should
be executed. The cron daemon takes care of starting the commands when
specified.

The at service is similar to cron, but it is once only: the command is
executed at the given time, but it is not repeated.

We will go more into this later. See the manual pages cron(1), crontab(1),
crontab(5), at(1) and atd(8) for more in depth information.

Chapter 13 will cover this.
-----------------------------------------------------------------------------

2.3.5. Graphical user interface

  UNIX and Linux don't incorporate the user interface into the kernel;
instead, they let it be implemented by user level programs. This applies for
both text mode and graphical environments.

This arrangement makes the system more flexible, but has the disadvantage
that it is simple to implement a different user interface for each program,
making the system harder to learn.

The graphical environment primarily used with Linux is called the X Window
System (X for short). X also does not implement a user interface; it only
implements a window system, i.e., tools with which a graphical user interface
can be implemented. Some popular window managers are: fvwm , icewm , blackbox
, and windowmaker . There are also two popular desktop managers, KDE and
Gnome.
-----------------------------------------------------------------------------

2.3.6. Networking

Networking is the act of connecting two or more computers so that they can
communicate with each other. The actual methods of connecting and
communicating are slightly complicated, but the end result is very useful.

UNIX operating systems have many networking features. Most basic services
(filesystems, printing, backups, etc) can be done over the network. This can
make system administration easier, since it allows centralized
administration, while still reaping in the benefits of microcomputing and
distributed computing, such as lower costs and better fault tolerance.

However, this book merely glances at networking; see the Linux Network
Administrators' Guide [http://www.tldp.org/LDP/nag2/index.html] http://
www.tldp.org/LDP/nag2/index.html for more information, including a basic
description of how networks operate.
-----------------------------------------------------------------------------

2.3.7. Network logins

Network logins work a little differently than normal logins. For each person
logging in via the network there is a separate virtual network connection,
and there can be any number of these depending on the available bandwidth. It
is therefore not possible to run a separate getty for each possible virtual
connection. There are also several different ways to log in via a network,
telnet and ssh being the major ones in TCP/IP networks.

These days many Linux system administrators consider telnet and rlogin to be
insecure and prefer ssh, the ``secure shell'', which encrypts traffic going
over the network, thereby making it far less likely that the malicious can
``sniff'' your connection and gain sensitive data like usernames and
passwords. It is highly recommended you use ssh rather than telnet or rlogin.

Network logins have, instead of a herd of gettys, a single daemon per way of
logging in (telnet and ssh have separate daemons) that listens for all
incoming login attempts. When it notices one, it starts a new instance of
itself to handle that single attempt; the original instance continues to
listen for other attempts. The new instance works similarly to getty.
-----------------------------------------------------------------------------

2.3.8. Network file systems

One of the more useful things that can be done with networking services is
sharing files via a network file system. Depending on your network this could
be done over the Network File System (NFS), or over the Common Internet File
System (CIFS). NFS is typically a 'UNIX' based service. In Linux, NFS is
supported by the kernel. CIFS however is not. In Linux, CIFS is supported by
Samba [http://www.samba.org] http://www.samba.org.

With a network file system any file operations done by a program on one
machine are sent over the network to another computer. This fools the program
to think that all the files on the other computer are actually on the
computer the program is running on. This makes information sharing extremely
simple, since it requires no modifications to programs.

This will be covered in more detail in Section 5.4.
-----------------------------------------------------------------------------

2.3.9. Mail

Electronic mail is the most popularly used method for communicating via
computer. An electronic letter is stored in a file using a special format,
and special mail programs are used to send and read the letters.

Each user has an incoming mailbox (a file in the special format), where all
new mail is stored. When someone sends mail, the mail program locates the
receiver's mailbox and appends the letter to the mailbox file. If the
receiver's mailbox is in another machine, the letter is sent to the other
machine, which delivers it to the mailbox as it best sees fit.

The mail system consists of many programs. The delivery of mail to local or
remote mailboxes is done by one program (the mail transfer agent (MTA) ,
e.g., sendmail or postfix ), while the programs users use are many and varied
(mail user agent (MUA) , e.g., pine , or evolution . The mailboxes are
usually stored in /var/spool/mail until the user's MUA retrieves them.

For more information on setting up and running mail services you can read the
Mail Administrator HOWTO at [http://www.tldp.org/HOWTO/
Mail-Administrator-HOWTO.html] http://www.tldp.org/HOWTO/
Mail-Administrator-HOWTO.html, or visit the sendmail or postfix's website.
[http://www.sendmail.org/] http://www.sendmail.org/, or http://
www.postfix.org/ .
-----------------------------------------------------------------------------

2.3.10. Printing

Only one person can use a printer at one time, but it is uneconomical not to
share printers between users. The printer is therefore managed by software
that implements a print queue: all print jobs are put into a queue and
whenever the printer is done with one job, the next one is sent to it
automatically. This relieves the users from organizing the print queue and
fighting over control of the printer. Instead, they form a new queue at the
printer, waiting for their printouts, since no one ever seems to be able to
get the queue software to know exactly when anyone's printout is really
finished. This is a great boost to intra-office social relations.

The print queue software also spools the printouts on disk, i.e., the text is
kept in a file while the job is in the queue. This allows an application
program to spit out the print jobs quickly to the print queue software; the
application does not have to wait until the job is actually printed to
continue. This is really convenient, since it allows one to print out one
version, and not have to wait for it to be printed before one can make a
completely revised new version.

You can refer to the Printing-HOWTO located at [http://www.tldp.org/HOWTO/
Printing-HOWTO/index.html] http://www.tldp.org/HOWTO/Printing-HOWTO/
index.html for more help in setting up printers.
-----------------------------------------------------------------------------

2.3.11. The filesystem layout

The filesystem is divided into many parts; usually along the lines of a root
filesystem with /bin , /lib , /etc , /dev , and a few others; a /usr
filesystem with programs and unchanging data; /var filesystem with changing
data (such as log files); and a /home for everyone's personal files.
Depending on the hardware configuration and the decisions of the system
administrator, the division can be different; it can even be all in one
filesystem.

Chapter 3 describes the filesystem layout in some little detail; the
Filesystem Hierarchy Standard . covers it in somewhat more detail. This can
be found on the web at: [http://www.pathname.com/fhs/] http://
www.pathname.com/fhs/
-----------------------------------------------------------------------------

Chapter 3. Overview of the Directory Tree

    " Two days later, there was Pooh, sitting on his branch, dangling his
    legs, and there, beside him, were four pots of honey..." (A.A. Milne)

This chapter describes the important parts of a standard Linux directory
tree, based on the Filesystem Hierarchy Standard . It outlines the normal way
of breaking the directory tree into separate filesystems with different
purposes and gives the motivation behind this particular split. Not all Linux
distributions follow this standard slavishly, but it is generic enough to
give you an overview.
-----------------------------------------------------------------------------

3.1. Background

This chapter is loosely based on the Filesystems Hierarchy Standard (FHS).
version 2.1, which attempts to set a standard for how the directory tree in a
Linux system is organized. Such a standard has the advantage that it will be
easier to write or port software for Linux, and to administer Linux machines,
since everything should be in standardized places. There is no authority
behind the standard that forces anyone to comply with it, but it has gained
the support of many Linux distributions. It is not a good idea to break with
the FHS without very compelling reasons. The FHS attempts to follow Unix
tradition and current trends, making Linux systems familiar to those with
experience with other Unix systems, and vice versa.

This chapter is not as detailed as the FHS. A system administrator should
also read the full FHS for a complete understanding.

This chapter does not explain all files in detail. The intention is not to
describe every file, but to give an overview of the system from a filesystem
point of view. Further information on each file is available elsewhere in
this manual or in the Linux manual pages.

The full directory tree is intended to be breakable into smaller parts, each
capable of being on its own disk or partition, to accommodate to disk size
limits and to ease backup and other system administration tasks. The major
parts are the root (/ ), /usr , /var , and /home filesystems (see Figure 3-1
). Each part has a different purpose. The directory tree has been designed so
that it works well in a network of Linux machines which may share some parts
of the filesystems over a read-only device (e.g., a CD-ROM), or over the
network with NFS.


Figure 3-1. Parts of a Unix directory tree. Dashed lines indicate partition
limits.

[fstree]

The roles of the different parts of the directory tree are described below.

��*�The root filesystem is specific for each machine (it is generally stored
    on a local disk, although it could be a ramdisk or network drive as well)
    and contains the files that are necessary for booting the system up, and
    to bring it up to such a state that the other filesystems may be mounted.
    The contents of the root filesystem will therefore be sufficient for the
    single user state. It will also contain tools for fixing a broken system,
    and for recovering lost files from backups.

��*�The /usr filesystem contains all commands, libraries, manual pages, and
    other unchanging files needed during normal operation. No files in /usr
    should be specific for any given machine, nor should they be modified
    during normal use. This allows the files to be shared over the network,
    which can be cost-effective since it saves disk space (there can easily
    be hundreds of megabytes, increasingly multiple gigabytes in /usr). It
    can make administration easier (only the master /usr needs to be changed
    when updating an application, not each machine separately) to have /usr
    network mounted. Even if the filesystem is on a local disk, it could be
    mounted read-only, to lessen the chance of filesystem corruption during a
    crash.

��*�The /var filesystem contains files that change, such as spool directories
    (for mail, news, printers, etc), log files, formatted manual pages, and
    temporary files. Traditionally everything in /var has been somewhere
    below /usr , but that made it impossible to mount /usr read-only.


��*�The /home filesystem contains the users' home directories, i.e., all the
    real data on the system. Separating home directories to their own
    directory tree or filesystem makes backups easier; the other parts often
    do not have to be backed up, or at least not as often as they seldom
    change. A big /home might have to be broken across several filesystems,
    which requires adding an extra naming level below /home, for example /
    home/students and /home/staff.


Although the different parts have been called filesystems above, there is no
requirement that they actually be on separate filesystems. They could easily
be kept in a single one if the system is a small single-user system and the
user wants to keep things simple. The directory tree might also be divided
into filesystems differently, depending on how large the disks are, and how
space is allocated for various purposes. The important part, though, is that
all the standard names work; even if, say, /var and /usr are actually on the
same partition, the names /usr/lib/libc.a and /var/log/messages must work,
for example by moving files below /var into /usr/var, and making /var a
symlink to /usr/var.

The Unix filesystem structure groups files according to purpose, i.e., all
commands are in one place, all data files in another, documentation in a
third, and so on. An alternative would be to group files files according to
the program they belong to, i.e., all Emacs files would be in one directory,
all TeX in another, and so on. The problem with the latter approach is that
it makes it difficult to share files (the program directory often contains
both static and sharable and changing and non-sharable files), and sometimes
to even find the files (e.g., manual pages in a huge number of places, and
making the manual page programs find all of them is a maintenance nightmare).
-----------------------------------------------------------------------------

3.2. The root filesystem

The root filesystem should generally be small, since it contains very
critical files and a small, infrequently modified filesystem has a better
chance of not getting corrupted. A corrupted root filesystem will generally
mean that the system becomes unbootable except with special measures (e.g.,
from a floppy), so you don't want to risk it.

The root directory generally doesn't contain any files, except perhaps on
older systems where the standard boot image for the system, usually called /
vmlinuz was kept there. (Most distributions have moved those files the the /
boot directory. Otherwise, all files are kept in subdirectories under the
root filesystem:

/bin
    Commands needed during bootup that might be used by normal users
    (probably after bootup).

/sbin
    Like /bin, but the commands are not intended for normal users, although
    they may use them if necessary and allowed. /sbin is not usually in the
    default path of normal users, but will be in root's default path.

/etc
    Configuration files specific to the machine.

/root
    The home directory for user root. This is usually not accessible to other
    users on the system

/lib
    Shared libraries needed by the programs on the root filesystem.

/lib/modules
    Loadable kernel modules, especially those that are needed to boot the
    system when recovering from disasters (e.g., network and filesystem
    drivers).

/dev
    Device files. These are special files that help the user interface with
    the various devices on the system.

/tmp
    Temporary files. As the name suggests, programs running often store
    temporary files in here.

/boot
    Files used by the bootstrap loader, e.g., LILO or GRUB. Kernel images are
    often kept here instead of in the root directory. If there are many
    kernel images, the directory can easily grow rather big, and it might be
    better to keep it in a separate filesystem. Another reason would be to
    make sure the kernel images are within the first 1024 cylinders of an IDE
    disk. This 1024 cylinder limit is no longer true in most cases. With
    modern BIOSes and later versions of LILO (the LInux LOader) the 1024
    cylinder limit can be passed with logical block addressing (LBA). See the
    lilo manual page for more details.

/mnt
    Mount point for temporary mounts by the system administrator. Programs
    aren't supposed to mount on /mnt automatically. /mnt might be divided
    into subdirectories (e.g., /mnt/dosa might be the floppy drive using an
    MS-DOS filesystem, and /mnt/exta might be the same with an ext2
    filesystem).

/proc, /usr, /var, /home
    Mount points for the other filesystems. Although /proc does not reside on
    any disk in reality it is still mentioned here. See the section about /
    proc later in the chapter.


-----------------------------------------------------------------------------
3.3. The /etc directory

The /etc maintains a lot of files. Some of them are described below. For
others, you should determine which program they belong to and read the manual
page for that program. Many networking configuration files are in /etc as
well, and are described in the Networking Administrators' Guide.

/etc/rc or /etc/rc.d or /etc/rc?.d
    Scripts or directories of scripts to run at startup or when changing the
    run level. See Section 2.3.1 for further information.

/etc/passwd
    The user database, with fields giving the username, real name, home
    directory, and other information about each user. The format is
    documented in the passwd manual page.

/etc/shadow
    /etc/shadow is an encrypted file the holds user passwords.

/etc/fdprm
    Floppy disk parameter table. Describes what different floppy disk formats
    look like. Used by setfdprm . See the setfdprm manual page for more
    information.

/etc/fstab
    Lists the filesystems mounted automatically at startup by the mount -a
    command (in /etc/rc or equivalent startup file). Under Linux, also
    contains information about swap areas used automatically by swapon -a .
    See Section 5.10.7 and the mount manual page for more information. Also
    fstab usually has its own manual page in section 5.

/etc/group
    Similar to /etc/passwd, but describes groups instead of users. See the
    group manual page in section 5 for more information.

/etc/inittab
    Configuration file for init.

/etc/issue
    Output by getty before the login prompt. Usually contains a short
    description or welcoming message to the system. The contents are up to
    the system administrator.

/etc/magic
    The configuration file for file. Contains the descriptions of various
    file formats based on which file guesses the type of the file. See the
    magic and file manual pages for more information.

/etc/motd
    The message of the day, automatically output after a successful login.
    Contents are up to the system administrator. Often used for getting
    information to every user, such as warnings about planned downtimes.

/etc/mtab
    List of currently mounted filesystems. Initially set up by the bootup
    scripts, and updated automatically by the mount command. Used when a list
    of mounted filesystems is needed, e.g., by the df command.

/etc/login.defs
    Configuration file for the login command. The login.defs file usually has
    a manual page in section 5.

/etc/printcap
    Like /etc/termcap /etc/printcap , but intended for printers. However it
    uses different syntax. The printcap has a manual page in section 5.

/etc/profile, /etc/bash.rc, /etc/csh.cshrc
    Files executed at login or startup time by the Bourne, BASH , or C
    shells. These allow the system administrator to set global defaults for
    all users. Users can also create individual copies of these in their home
    directory to personalize their environment. See the manual pages for the
    respective shells.

/etc/securetty
    Identifies secure terminals, i.e., the terminals from which root is
    allowed to log in. Typically only the virtual consoles are listed, so
    that it becomes impossible (or at least harder) to gain superuser
    privileges by breaking into a system over a modem or a network. Do not
    allow root logins over a network. Prefer to log in as an unprivileged
    user and use su or sudo to gain root privileges.

/etc/shells
    Lists trusted shells. The chsh command allows users to change their login
    shell only to shells listed in this file. ftpd, is the server process
    that provides FTP services for a machine, will check that the user's
    shell is listed in /etc/shells and will not let people log in unless the
    shell is listed there.

/etc/termcap
    The terminal capability database. Describes by what ``escape sequences''
    various terminals can be controlled. Programs are written so that instead
    of directly outputting an escape sequence that only works on a particular
    brand of terminal, they look up the correct sequence to do whatever it is
    they want to do in /etc/termcap. As a result most programs work with most
    kinds of terminals. See the termcap, curs_termcap, and terminfo manual
    pages for more information.


-----------------------------------------------------------------------------
3.4. The /dev directory

The /dev directory contains the special device files for all the devices. The
device files are created during installation, and later with the /dev/MAKEDEV
script. The /dev/MAKEDEV.local is a script written by the system
administrator that creates local-only device files or links (i.e. those that
are not part of the standard MAKEDEV, such as device files for some
non-standard device driver).

This list which follows is by no means exhaustive or as detailed as it could
be. Many of these device files will need support compiled into your kernel
for the hardware. Read the kernel documentation to find details of any
particular device.

If you think there are other devices which should be included here but aren't
then let me know. I will try to include them in the next revision.

/dev/dsp
    Digital Signal Processor. Basically this forms the interface between
