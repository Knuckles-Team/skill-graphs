```
Linux Filesystem Hierarchy

Version 0.65

Binh Nguyen


<linuxfilesystem(at)yahoo(dot)com(dot)au>

2004-07-30


 This document outlines the set of requirements and guidelines for file and
directory placement under the Linux operating system according to those of
the FSSTND v2.3 final (January 29, 2004) and also its actual implementation
on an arbitrary system. It is meant to be accessible to all members of the
Linux community, be distribution independent and is intended to discuss the
impact of the FSSTND and how it has managed to increase the efficiency of
support interoperability of applications, system administration tools,
development tools, and scripts as well as greater uniformity of documentation
for these systems.

Copyright 2003 Binh Nguyen

Trademarks are owned by their owners.

Permission is granted to copy, distribute and/or modify this document under
the terms of the GNU Free Documentation License, Version 1.2; with no
Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU Free
Documentation License".

-----------------------------------------------------------------------------
Table of Contents
Source and pre-formatted versions available
1. Linux Filesystem Hierarchy
    1.1. Foreward
    1.2. The Root Directory
    1.3. /bin
    1.4. /boot
    1.5. /dev
    1.6. /etc
    1.7. /home
    1.8. /initrd
    1.9. /lib
    1.10. /lost+found
    1.11. /media
    1.12. /mnt
    1.13. /opt
    1.14. /proc
    1.15. /root
    1.16. /sbin
    1.17. /usr
    1.18. /var
    1.19. /srv
    1.20. /tmp


Glossary
A. UNIX System V Signals
B. Sources
C. About the Author
D. Contributors
E. Disclaimer
F. Donations
G. Feedback
H. GNU Free Documentation License
    H.1. PREAMBLE
    H.2. APPLICABILITY AND DEFINITIONS
    H.3. VERBATIM COPYING
    H.4. COPYING IN QUANTITY
    H.5. MODIFICATIONS
    H.6. COMBINING DOCUMENTS
    H.7. COLLECTIONS OF DOCUMENTS
    H.8. AGGREGATION WITH INDEPENDENT WORKS
    H.9. TRANSLATION
    H.10. TERMINATION
    H.11. FUTURE REVISIONS OF THIS LICENSE
    H.12. ADDENDUM: How to use this License for your documents



-----------------------------------------------------------------------------
Source and pre-formatted versions available

The source code and other machine readable formats of this book can be found
on the Internet at the Linux Documentation Project home page [http://
www.tldp.org] http://www.tldp.org The latest version of this document can be
found at [http://cvsview.tldp.org/index.cgi/LDP/guide/docbook/
Linux-Filesystem-Hierarchy/]  http://cvsview.tldp.org/index.cgi/LDP/guide/
docbook/Linux-Filesystem-Hierarchy/
-----------------------------------------------------------------------------

Chapter 1. Linux Filesystem Hierarchy

1.1. Foreward

When migrating from another operating system such as Microsoft Windows to
another; one thing that will profoundly affect the end user greatly will be
the differences between the filesystems.

What are filesystems?

A filesystem is the methods and data structures that an operating system uses
to keep track of files on a disk or partition; that is, the way the files are
organized on the disk. The word is also used to refer to a partition or disk
that is used to store the files or the type of the filesystem. Thus, one
might say I have two filesystems meaning one has two partitions on which one
stores files, or that one is using the extended filesystem, meaning the type
of the filesystem.

The difference between a disk or partition and the filesystem it contains is
important. A few programs (including, reasonably enough, programs that create
filesystems) operate directly on the raw sectors of a disk or partition; if
there is an existing file system there it will be destroyed or seriously
corrupted. Most programs operate on a filesystem, and therefore won't work on
a partition that doesn't contain one (or that contains one of the wrong
type).

 Before a partition or disk can be used as a filesystem, it needs to be
initialized, and the bookkeeping data structures need to be written to the
disk. This process is called making a filesystem.

Most UNIX filesystem types have a similar general structure, although the
exact details vary quite a bit. The central concepts are superblock, inode,
data block, directory block, and indirection block. The superblock contains
information about the filesystem as a whole, such as its size (the exact
information here depends on the filesystem). An inode contains all
information about a file, except its name. The name is stored in the
directory, together with the number of the inode. A directory entry consists
of a filename and the number of the inode which represents the file. The
inode contains the numbers of several data blocks, which are used to store
the data in the file. There is space only for a few data block numbers in the
inode, however, and if more are needed, more space for pointers to the data
blocks is allocated dynamically. These dynamically allocated blocks are
indirect blocks; the name indicates that in order to find the data block, one
has to find its number in the indirect block first.

 Like UNIX, Linux chooses to have a single hierarchical directory structure.
Everything starts from the root directory, represented by /, and then expands
into sub-directories instead of having so-called 'drives'. In the Windows
environment, one may put one's files almost anywhere: on C drive, D drive, E
drive etc. Such a file system is called a hierarchical structure and is
managed by the programs themselves (program directories), not by the
operating system. On the other hand, Linux sorts directories descending from
the root directory / according to their importance to the boot process.

 If you're wondering why Linux uses the frontslash / instead of the backslash
\ as in Windows it's because it's simply following the UNIX tradition. Linux,
like Unix also chooses to be case sensitive. What this means is that the
case, whether in capitals or not, of the characters becomes very important.
So this is not the same as THIS. This feature accounts for a fairly large
proportion of problems for new users especially during file transfer
operations whether it may be via removable disk media such as floppy disk or
over the wire by way of FTP.

 The filesystem order is specific to the function of a file and not to its
program context (the majority of Linux filesystems are 'Second Extended File
Systems', short 'EXT2' (aka 'ext2fs' or 'extfs2') or are themselves subsets
of this filesystem such as ext3 and Reiserfs). It is within this filesystem
that the operating system determines into which directories programs store
their files.

 If you install a program in Windows, it usually stores most of its files in
its own directory structure. A help file for instance may be in C:\Program
Files\[program name]\ or in C:\Program Files\[program-name]\help or in C:\
Program Files\[program -name]\humpty\dumpty\doo. In Linux, programs put their
documentation into /usr/share/doc/[program-name], man(ual) pages into /usr/
share/man/man[1-9] and info pages into /usr/share/info. They are merged into
and with the system hierarchy.

 As all Linux users know, unless you mount a partition or a device, the
system does not know of the existence of that partition or device. This might
not appear to be the easiest way to provide access to your partitions or
devices, however it offers the advantage of far greater flexibility when
compared to other operating systems. This kind of layout, known as the
unified filesystem, does offer several advantages over the approach that
Windows uses. Let's take the example of the /usr directory. This
sub-directory of the root directory contains most of the system executables.
With the Linux filesystem, you can choose to mount it off another partition
or even off another machine over the network using an innumerable set of
protocols such as NFS (Sun), Coda (CMU) or AFS (IBM). The underlying system
will not and need not know the difference. The presence of the /usr directory
is completely transparent. It appears to be a local directory that is part of
the local directory structure.

Compliance requires that:
 +---------+-----------------+-------------+
 |         | shareable       | unshareable |
 +---------+-----------------+-------------+
 |static   | /usr            | /etc        |
 |         | /opt            | /boot       |
 +---------+-----------------+-------------+
 |variable | /var/mail       | /var/run    |
 |         | /var/spool/news | /var/lock   |
 +---------+-----------------+-------------+

 "Shareable" files are defined as those that can be stored on one host and
 used on others. "Unshareable" files are those that are not shareable. For
 example, the files in user home directories are shareable whereas device
 lock files are not. "Static" files include binaries, libraries,
 documentation files and other files that do not change without system
 administrator intervention. "Variable" files are defined as files that
 are not static.


 Another reason for this unified filesystem is that Linux caches a lot of
disk accesses using system memory while it is running to accelerate these
processes. It is therefore vitally important that these buffers are flushed
(get their content written to disk), before the system closes down. Otherwise
files are left in an undetermined state which is of course a very bad thing.
Flushing is achieved by 'unmounting' the partitions during proper system
shutdown. In other words, don't switch your system off while it's running!
You may get away with it quite often, since the Linux file system is very
robust, but you may also wreak havoc upon important files. Just hit
ctrl-alt-del or use the proper commands (e.g. shutdown, poweroff, init 0).
This will shut down the system in a decent way which will thus, guarantee the
integrity of your files.

 Many of us in the Linux community have come to take for granted the
existence of excellent books and documents about Linux, an example being
those produced by the Linux Documentation Project. We are used to having
various packages taken from different sources such as Linux FTP sites and
distribution CD-ROMs integrate together smoothly. We have come to accept that
we all know where critical files like mount can be found on any machine
running Linux. We also take for granted CD-ROM based distributions that can
be run directly from the CD and which consume only a small amount of physical
hard disk or a RAM disk for some variable files like /etc/passwd, etc. This
has not always been the case.

 During the adolescent years of Linux during the early to mid-90s each
distributor had his own favorite scheme for locating files in the directory
hierarchy. Unfortunately, this caused many problems. The Linux File System
Structure is a document, which was created to help end this anarchy. Often
the group, which creates this document or the document itself, is referred to
as the FSSTND. This is short for file system standard". This document has
helped to standardize the layout of file systems on Linux systems everywhere.
Since the original release of the standard, most distributors have adopted it
in whole or in part, much to the benefit of all Linux users.

Since the first draft of the standard, the FSSTND project has been
coordinated by Daniel Quinlan and development of this standard has been
through consensus by a group of developers and Linux enthusiasts. The FSSTND
group set out to accomplish a number of specific goals. The first goal was to
solve a number of problems that existed with the current distributions at the
time. Back then, it was not possible to have a shareable /usr partition,
there was no clear distinction between /bin and /usr/bin, it was not possible
to set up a diskless workstation, and there was just general confusion about
what files went where. The second goal was to ensure the continuation of some
reasonable compatibility with the de-facto standards already in use in Linux
and other UNIX-like operating systems. Finally, the standard had to gain
widespread approval by the developers, distributors, and users within the
Linux community. Without such support, the standard would be pointless,
becoming just another way of laying out the file system.

Fortunately, the FSSTND has succeeded though there are also some goals that
the FSSTND project did not set out to achieve. The FSSTND does not try to
emulate the scheme of any specific commercial UNIX operating system (e.g.
SunOS, AIX, etc.) Furthermore, for many of the files covered by the FSSTND,
the standard does not dictate whether the files should be present, merely
where the files should be if they are present. Finally, for most files, the
FSSTND does not attempt to dictate the format of the contents of the files.
(There are some specific exceptions when several different packages may need
to know the file formats to work together properly. For example, lock files
that contain the process ID of the process holding the lock.) The overall
objective was to establish the location where common files could be found, if
they existed on a particular machine. The FSSTND project began in early
August 1993. Since then, there have been a number of public revisions of this
document. The latest, v2.3 was released on January 29, 2004.

If you're asking "What's the purpose of all this? Well, the answer depends on
who you are. If you are a Linux user, and you don't administrate your own
system then the FSSTND ensures that you will be able to find programs where
you'd expect them to be if you've already had experience on another Linux
machine. It also ensures that any documentation you may have makes sense.
Furthermore, if you've already had some experience with Unix before, then the
FSSTND shouldn't be too different from what you're currently using, with a
few exceptions. Perhaps the most important thing is that the development of a
standard brings Linux to a level of maturity authors and commercial
application developers feel they can support.

If you administer your own machine then you gain all the benefits of the
FSSTND mentioned above. You may also feel more secure in the ability of
others to provide support for you, should you have a problem. Furthermore,
periodic upgrades to your system are theoretically easier. Since there is an
agreed-upon standard for the locations of files, package maintainers can
provide instructions for upgrading that will not leave extra, older files
lying around your system inhabiting valuable disk space. The FSSTND also
means that there is more support from those providing source code packages
for you to compile and install yourself. The provider knows, for example,
where the executable for sed is to be found on a Linux machine and can use
that in his installation scripts or Makefiles.

If you run a large network, the FSSTND may ease many of your NFS headaches,
since it specifically addresses the problems which formerly made shared
implementations of /usr impractical. If you are a distributor, then you will
be affected most by the Linux FSSTND. You may have to do a little extra work
to make sure that your distribution is FSSTND-compliant, but your users (and
hence your business) will gain by it. If your system is compliant, third
party add-on packages (and possibly your own) will integrate smoothly with
your system. Your users will, of course, gain all the benefits listed above,
and many of your support headaches will be eased. You will benefit from all
the discussion and thought that has been put into the FSSTND and avoid many
of the pitfalls involved in designing a filesystem structure yourself. If you
adhere to the FSSTND, you will also be able to take advantage of various
features that the FSSTND was designed around. For example, the FSSTND makes
"live" CD-ROMs containing everything except some of the files in the / and /
var directories possible. If you write documentation for Linux, the FSSTND
makes it much easier to do so, which makes sense to the Linux community. You
no longer need to worry about the specific location of lock files on one
distribution versus another, nor are you forced to write documentation that
is only useful to the users of a specific distribution. The FSSTND is at
least partly responsible for the recent explosion of Linux books being
published.

If you are a developer, the existence of the FSSTND greatly eases the
possibility for potential problems. You can know where important system
binaries are found, so you can use them from inside your programs or your
shell scripts. Supporting users is also greatly eased, since you don't have
to worry about things like the location of these binaries when resolving
support issues. If you are the developer of a program that needs to integrate
with the rest of the system, the FSSTND ensures that you can be certain of
the steps to meet this end. For example, applications such as kermit, which
access the serial ports, need to know they can achieve exclusive access to
the TTY device. The FSSTND specifies a common method of doing this so that
all compliant applications can work together. That way you can concentrate on
making more great software for Linux instead of worrying about how to detect
and deal with the differences in flavors of Linux. The widespread acceptance
of the FSSTND by the Linux community has been crucial to the success of both
the standard and operating system. Nearly every modern distribution conforms
to the Linux FSSTND. If your implementation isn't at least partially FSSTND
compliant, then it is probably either very old or you built it yourself. The
FSSTND itself contains a list of some of the distributions that aim to
conform to the FSSTND. However, there are some distributions that are known
to cut some corners in their implementation of FSSTND.

By no means does this mean that the standard itself is complete. There are
still unresolved issues such as the organization of architecture-independent
scripts and data files /usr/share. Up until now, the i386 has been the
primary platform for Linux, so the need for standardization of such files was
non-existent.

The rapid progress in porting Linux to other architectures (MC680x0, Alpha,
MIPS, PowerPC) suggests that this issue will soon need to be dealt with.
Another issue that is under some discussion is the creation of an /opt
directory as in SVR4. The goal for such a directory would be to provide a
location for large commercial or third party packages to install themselves
without worrying about the requirements made by FSSTND for the other
directory hierarchies. The FSSTND provides the Linux community with an
excellent reference document and has proven to be an important factor in the
maturation of Linux. As Linux continues to evolve, so will the FSSTND.

Now, that we have seen how things should be, let's take a look at the real
world. As you will see, the implementation of this concept on Linux isn't
perfect and since Linux has always attracted individualists who tend to be
fairly opinionated, it has been a bone of contention among users for instance
which directories certain files should be put into. With the arrival of
different distributions, anarchy has once again descended upon us. Some
distributions put mount directories for external media into the / directory,
others into /mnt. Red Hat based distributions feature the /etc/sysconfig
sub-hierarchy for configuration files concerning input and network devices.
Other distributions do not have this directory at all and put the appropriate
files elsewhere or even use completely different mechanisms to do the same
thing. Some distributions put KDE into /opt/, others into /usr.

But even within a given file system hierarchy, there are inconsistencies. For
example, even though this was never the intention of the XFree86 group,
XFree86 does indeed have its own directory hierarchy.

These problems don't manifest themselves as long as you compile programs
yourself. You can adapt configure scripts or Makefiles to your system's
configuration or to your preference. It's a different story if you install
pre-compiled packages like RPMs though. Often these are not adaptable from
one file system hierarchy to another. What's worse: some RPMs might even
create their own hierarchy. If you, say, install a KDE RPM from the SuSE
Linux distribution on your Mandrake system, the binary will be put into /opt/
kde2/bin. And thus it won't work, because Mandrake expects it to be in /usr/
bin. There are of course ways to circumvent this problem but the current
situation is clearly untenable. Thus, all the leading Linux distributors have
joined the Linux Standard Base project, which is attempting to create a
common standard for Linux distributions. This isn't easy, since changing the
file system hierarchy means a lot of work for distributors so every
distributor tries to push a standard which will allow them to keep as much of
their own hierarchy as possible. The LSB will also encompass the proposals
made by the Filesystem Hierarchy Standard project (FHS, former FSSTND).
-----------------------------------------------------------------------------

1.2. The Root Directory

  To comply with the FSSTND the following directories, or symbolic links to
directories, are required in /.


       /bin       Essential command binaries
       /boot      Static files of the boot loader
       /dev       Device files
       /etc       Host-specific system configuration
       /lib       Essential shared libraries and kernel modules
       /media     Mount point for removable media
       /mnt       Mount point for mounting a filesystem temporarily
       /opt       Add-on application software packages
       /sbin      Essential system binaries
       /srv       Data for services provided by this system
       /tmp       Temporary files
       /usr       Secondary hierarchy
       /var       Variable data


The following directories, or symbolic links to directories, must be in /, if
the corresponding subsystem is installed:


     / -- the root directory
     /home User home directories (optional)
     /lib<qual> Alternate format essential shared libraries
                      (optional)
     /root Home directory for the root user (optional)


  Each directory listed above is described in detail in separate subsections
further on in this document.

  The reference system will be based upon Debian 3.0r0 (Woody), 2.4.18 kernel
configured to a Redhat kernel-2.4.18-i686.config file.



Hardware


    ��+�Intel Celeron 766 Processor

    ��+�MSI MS-6309 V.2.0 Mainboard

    ��+�512MB PQI PC133 SDRAM

    ��+�16x Lite-On LTD-165H DVD-ROM

    ��+�40x24x10 Sony CRX175A1 CD-RW

    ��+�NVIDIA RIVA 32MB TNT2 M64

    ��+�D-Link DFE-530TX 10/100 NIC

    ��+�Realtek RTL8029(AS) 10 NIC

    ��+�Lucent Mars2 Linmodem

    ��+�C-Media CMI8738 PCI Audio Device

    ��+�Miro DC-30 VIVO

    ��+�Aopen KF-45A Miditower Case

    ��+�Acer Accufeel Keyboard

    ��+�Genius Netscroll+ Mouse

    ��+�Compaq MV500 Presario Monitor


Software


    ��+�Windows XP on /dev/hda1

    ��+�FreeBSD 4.2 on /dev/hda2

    ��+�Redhat 8.0 on /dev/hda5

    ��+�Debian 3.0r0 on /dev/hda6

    ��+�Mandrake 9.1 on /dev/hda7

    ��+�Swap partition on /dev/hda8



  As we all know Linux file system starts with /, the root directory. All
other directories are 'children' of this directory. The partition which the
root file system resides on is mounted first during boot and the system will
not boot if it doesn't find it. On our reference system, the root directory
contains the following sub-directories:

  bin/ dev/ home/ lost+found/ proc/ sbin/ usr/ cdrom/ opt/ vmlinuz boot/ etc/
lib/ mnt/ root/ tmp/ var/ dvd/ floppy/ initrd/ /tftpboot

  In days past it was also the home directory of 'root' but now he has been
given his own directory for reasons that will be explained further on in this
document.
-----------------------------------------------------------------------------
