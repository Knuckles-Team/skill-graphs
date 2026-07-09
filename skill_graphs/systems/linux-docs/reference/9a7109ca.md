```
The Linux System Administrator's Guide

Version 0.9

Lars Wirzenius

����������������<Email address removed by request>
����������������

Joanna Oja

����������������<Current email address unknown>
����������������

Stephen Stafford

����������������<stephen@clothcat.demon.co.uk.NOSPAM>
����������������

Alex Weeks

����������������<draxeman@gmail.com.NOSPAM>
����������������


An introduction to system administration of a Linux system for novices.

Copyright 1993--1998 Lars Wirzenius.

Copyright 1998--2001 Joanna Oja.

Copyright 2001--2003 Stephen Stafford.

Copyright 2003--2004 Stephen Stafford & Alex Weeks.

Copyright 2004--Present Alex Weeks.

Trademarks are owned by their owners.

Permission is granted to copy, distribute and/or modify this document under
the terms of the GNU Free Documentation License, Version 1.2 or any later
version published by the Free Software Foundation; with no Invariant
Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the
license is included in the section entitled "GNU Free Documentation License".

-----------------------------------------------------------------------------
Table of Contents
About This Book
    1. Acknowledgments
    2. Revision History
    3. Source and pre-formatted versions available
    4. Typographical Conventions


1. Introduction
    1.1. Linux or GNU/Linux, that is the question.
    1.2. Trademarks


2. Overview of a Linux System
    2.1. Various parts of an operating system
    2.2. Important parts of the kernel
    2.3. Major services in a UNIX system


3. Overview of the Directory Tree
    3.1. Background
    3.2. The root filesystem
    3.3. The /etc directory
    3.4. The /dev directory
    3.5. The /usr filesystem.
    3.6. The /var filesystem
    3.7. The /proc filesystem


4. Hardware, Devices, and Tools
    4.1. Hardware Utilities
    4.2. Kernel Modules


5. Using Disks and Other Storage Media
    5.1. Two kinds of devices
    5.2. Hard disks
    5.3. Storage Area Networks - Draft
    5.4. Network Attached Storage - Draft
    5.5. Floppies
    5.6. CD-ROMs
    5.7. Tapes
    5.8. Formatting
    5.9. Partitions
    5.10. Filesystems
    5.11. Disks without filesystems
    5.12. Allocating disk space


6. Memory Management
    6.1. What is virtual memory?
    6.2. Creating a swap space
    6.3. Using a swap space
    6.4. Sharing swap spaces with other operating systems
    6.5. Allocating swap space
    6.6. The buffer cache


7. System Monitoring
    7.1. System Resources
    7.2. Filesystem Usage
    7.3. Monitoring Users


8. Boots And Shutdowns
    8.1. An overview of boots and shutdowns
    8.2. The boot process in closer look
    8.3. More about shutdowns
    8.4. Rebooting
    8.5. Single user mode
    8.6. Emergency boot floppies


9. init
    9.1. init comes first
    9.2. Configuring init to start getty: the /etc/inittab file
    9.3. Run levels
    9.4. Special configuration in /etc/inittab
    9.5. Booting in single user mode


10. Logging In And Out
    10.1. Logins via terminals
    10.2. Logins via the network
    10.3. What login does
    10.4. X and xdm
    10.5. Access control
    10.6. Shell startup


11. Managing user accounts
    11.1. What's an account?
    11.2. Creating a user
    11.3. Changing user properties
    11.4. Removing a user
    11.5. Disabling a user temporarily


12. Backups
    12.1. On the importance of being backed up
    12.2. Selecting the backup medium
    12.3. Selecting the backup tool
    12.4. Simple backups
    12.5. Multilevel backups
    12.6. What to back up
    12.7. Compressed backups


13. Task Automation --To Be Added
14. Keeping Time
    14.1. The concept of localtime
    14.2. The hardware and software clocks
    14.3. Showing and setting time
    14.4. When the clock is wrong
    14.5. NTP - Network Time Protocol
    14.6. Basic NTP configuration
    14.7. NTP Toolkit
    14.8. Some known NTP servers
    14.9. NTP Links


15. System Logs --To Be Added
16. System Updates --To Be Added
17. The Linux Kernel Source
18. Finding Help
    18.1. Newsgroups and Mailing Lists
    18.2. IRC


A. GNU Free Documentation License
    A.1. PREAMBLE
    A.2. APPLICABILITY AND DEFINITIONS
    A.3. VERBATIM COPYING
    A.4. COPYING IN QUANTITY
    A.5. MODIFICATIONS
    A.6. COMBINING DOCUMENTS
    A.7. COLLECTIONS OF DOCUMENTS
    A.8. AGGREGATION WITH INDEPENDENT WORKS
    A.9. TRANSLATION
    A.10. TERMINATION
    A.11. FUTURE REVISIONS OF THIS LICENSE
    A.12. ADDENDUM: How to use this License for your documents


Glossary (DRAFT, but not for long hopefully)
Index-Draft

List of Tables
5-1. Comparing Filesystem Features
5-2. Sizes
5-3. My Partitions
9-1. Run level numbers
12-1. Efficient backup scheme using many backup levels

List of Figures
2-1. Some of the more important parts of the Linux kernel
3-1. Parts of a Unix directory tree. Dashed lines indicate partition limits.
5-1. A schematic picture of a hard disk.
5-2. A sample hard disk partitioning.
5-3. Three separate filesystems.
5-4. /home and /usr have been mounted.
10-1. Logins via terminals: the interaction of init, getty, login, and the
    shell.
12-1. A sample multilevel backup schedule.

-----------------------------------------------------------------------------
About This Book

    "Only two things are infinite, the universe and human stupidity, and I'm
    not sure about the former." Albert Einstein

-----------------------------------------------------------------------------
1. Acknowledgments

1.1. Joanna's acknowledgments

Many people have helped me with this book, directly or indirectly. I would
like to especially thank Matt Welsh for inspiration and LDP leadership, Andy
Oram for getting me to work again with much-valued feedback, Olaf Kirch for
showing me that it can be done, and Adam Richter at Yggdrasil and others for
showing me that other people can find it interesting as well.

Stephen Tweedie, H. Peter Anvin, Remy Card, Theodore Ts'o, and Stephen
Tweedie have let me borrow their work (and thus make the book look thicker
and much more impressive): a comparison between the xia and ext2 filesystems,
the device list and a description of the ext2 filesystem. These aren't part
of the book any more. I am most grateful for this, and very apologetic for
the earlier versions that sometimes lacked proper attribution.

In addition, I would like to thank Mark Komarinski for sending his material
in 1993 and the many system administration columns in Linux Journal. They are
quite informative and inspirational.

Many useful comments have been sent by a large number of people. My miniature
black hole of an archive doesn't let me find all their names, but some of
them are, in alphabetical order: Paul Caprioli, Ales Cepek, Marie-France
Declerfayt, Dave Dobson, Olaf Flebbe, Helmut Geyer, Larry Greenfield and his
father, Stephen Harris, Jyrki Havia, Jim Haynes, York Lam, Timothy Andrew
Lister, Jim Lynch, Michael J. Micek, Jacob Navia, Dan Poirier, Daniel
Quinlan, Jouni K Sepp�nen, Philippe Steindl, G.B. Stotte. My apologies to
anyone I have forgotten.
-----------------------------------------------------------------------------

1.2. Stephen's acknowledgments

I would like to thank Lars and Joanna for their hard work on the guide.

In a guide like this one there are likely to be at least some minor
inaccuracies. And there are almost certainly going to be sections that become
out of date from time to time. If you notice any of this then please let me
know by sending me an email to: <bagpuss@debian.org.NOSPAM>. I will take
virtually any form of input (diffs, just plain text, html, whatever), I am in
no way above allowing others to help me maintain such a large text as this :)

Many thanks to Helen Topping Shaw for getting the red pen out and making the
text far better than it would otherwise have been. Also thanks are due just
for being wonderful.
-----------------------------------------------------------------------------

1.3. Alex's Acknowledgments

I would like to thank Lars, Joanna, and Stephen for all the great work that
they have done on this document over the years. I only hope that my
contribution will be worthy of continuing the work they started.

Like the previous maintainers, I openly welcome any comments, suggestions,
complains, corrections, or any other form of feedback you may have. This
document can only benefit from the suggestions of those who use it.

There have been many people who have helped me on my journey through the
"Windows-Free" world, the person I feel I need to thank the most is my first
true UN*X mentor, Mike Velasco. Back in a time before SCO became a "dirty
word", Mike helped me on the path of tar's, cpio's, and many, many man pages.
Thanks Mike! You are the 'Sofa King'.

-----------------------------------------------------------------------------
2. Revision History

Revision History
Revision 0.7            2001-12-03             Revised by: SS
Revision 0.8            2003-11-18             Revised by: AW

 1. Added a section on NTP
 2. Cleaned some SGML
 3. Added ext3 to the filesystem section

Revision 0.9                                   Revised by: AW

 1. Cleaned some SGML code, changed doctype to lds.dsl, and added id tags
 2. Updated section on filesystem types, and Filesystem comparison
 3. Updated partition type section
 4. Updated section on creating partitions
 5. Wrote section on Logical Volume Manager (LVM)
 6. Updated section on space allocation
 7. Added chapter on System Monitoring
 8. Added more command line utilities
 9. Verified Device list
10. Modified email address for Authors
11. Added references to more in-depth documents where applicable
12. Added notes on upcoming sections
13. Indexed chapters 1 - 4, & part of 5
14. Updated Misc Information throughout the book

-----------------------------------------------------------------------------

3. Source and pre-formatted versions available

The source code and other machine readable formats of this book can be found
on the Internet via anonymous FTP at the Linux Documentation Project home
page [http://www.tldp.org/] http://www.tldp.org/, or at the home page of this
book at [http://www.draxeman.com/sag.html] http://www.draxeman/sag.html. This
book is available in at least it's SGML source, as well as, HTML and PDF
formats. Other formats may be available.
-----------------------------------------------------------------------------

4. Typographical Conventions

Throughout this book, I have tried to use uniform typographical conventions.
Hopefully they aid readability. If you can suggest any improvements please
contact me.

Filenames are expressed as: /usr/share/doc/foo.

Command names are expressed as: fsck

Email addresses are expressed as: <user@domain.com>

URLs are expressed as: [http://www.tldp.org] http://www.tldp.org

I will add to this section as things come up whilst editing. If you notice
anything that should be added then please let me know.
-----------------------------------------------------------------------------

Chapter 1. Introduction

    "In the beginning, the file was without form, and void; and emptiness was
    upon the face of the bits. And the Fingers of the Author moved upon the
    face of the keyboard. And the Author said, Let there be words, and there
    were words."

The Linux System Administrator's Guide, describes the system administration
aspects of using Linux. It is intended for people who know next to nothing
about system administration (those saying ``what is it?''), but who have
already mastered at least the basics of normal usage. This manual doesn't
tell you how to install Linux; that is described in the Installation and
Getting Started document. See below for more information about Linux manuals.

System administration covers all the things that you have to do to keep a
computer system in usable order. It includes things like backing up files
(and restoring them if necessary), installing new programs, creating accounts
for users (and deleting them when no longer needed), making certain that the
filesystem is not corrupted, and so on. If a computer were, say, a house,
system administration would be called maintenance, and would include
cleaning, fixing broken windows, and other such things.

The structure of this manual is such that many of the chapters should be
usable independently, so if you need information about backups, for example,
you can read just that chapter. However, this manual is first and foremost a
tutorial and can be read sequentially or as a whole.

This manual is not intended to be used completely independently. Plenty of
the rest of the Linux documentation is also important for system
administrators. After all, a system administrator is just a user with special
privileges and duties. Very useful resources are the manual pages, which
should always be consulted when you are not familiar with a command. If you
do not know which command you need, then the apropos command can be used.
Consult its manual page for more details.

While this manual is targeted at Linux, a general principle has been that it
should be useful with other UNIX based operating systems as well.
Unfortunately, since there is so much variance between different versions of
UNIX in general, and in system administration in particular, there is little
hope to cover all variants. Even covering all possibilities for Linux is
difficult, due to the nature of its development.

There is no one official Linux distribution, so different people have
different setups and many people have a setup they have built up themselves.
This book is not targeted at any one distribution. Distributions can and do
vary considerably. When possible, differences have been noted and
alternatives given. For a list of distributions and some of their differences
see [http://en.wikipedia.org/wiki/Comparison_of_Linux_distributions] http://
en.wikipedia.org/wiki/Comparison_of_Linux_distributions.

In trying to describe how things work, rather than just listing ``five easy
steps'' for each task, there is much information here that is not necessary
for everyone, but those parts are marked as such and can be skipped if you
use a preconfigured system. Reading everything will, naturally, increase your
understanding of the system and should make using and administering it more
productive.

Understanding is the key to success with Linux. This book could just provide
recipes, but what would you do when confronted by a problem this book had no
recipe for? If the book can provide understanding, then recipes are not
required. The answers will be self evident.

Like all other Linux related development, the work to write this manual was
done on a volunteer basis: I did it because I thought it might be fun and
because I felt it should be done. However, like all volunteer work, there is
a limit to how much time, knowledge and experience people have. This means
that the manual is not necessarily as good as it would be if a wizard had
been paid handsomely to write it and had spent millennia to perfect it. Be
warned.

One particular point where corners have been cut is that many things that are
already well documented in other freely available manuals are not always
covered here. This applies especially to program specific documentation, such
as all the details of using mkfs. Only the purpose of the program and as much
of its usage as is necessary for the purposes of this manual is described.
For further information, consult these other manuals. Usually, all of the
referred to documentation is part of the full Linux documentation set.
-----------------------------------------------------------------------------

1.1. Linux or GNU/Linux, that is the question.

Many people feel that Linux should really be called GNU/Linux. This is
because Linux is only the kernel, not the applications that run on it. Most
of the basic command line utilities were written by the Free Software
Foundation while developing their GNU operating system. Among those utilities
are some of the most basic commands like cp, mv lsof, and dd.

In a nutshell, what happened was, the FSF started developing GNU by writing
things like compilers, C libraries, and basic command line utilities before
the kernel. Linus Torvalds, started Linux by writing the Linux kernel first
and using applications written for GNU.

I do not feel that this is the proper forum to debate what name people should
use when referring to Linux. I mention it here, because I feel it is
important to understand the relationship between GNU and Linux, and to also
explain why some Linux is sometimes referred to as GNU/Linux. The document
will be simply referring to it as Linux.

GNU's side of the issue is discussed on their website:

The relationship - [http://www.gnu.org/gnu/linux-and-gnu.html] http://
www.gnu.org/gnu/linux-and-gnu.html

Why Linux should be GNU/Linux - [http://www.gnu.org/gnu/why-gnu-linux.html]
http://www.gnu.org/gnu/why-gnu-linux.html

GNU/Linux FAQ's - [http://www.gnu.org/gnu/gnu-linux-faq.html] http://
www.gnu.org/gnu/gnu-linux-faq.html

Here are some Alternate views:

[http://librenix.com/?inode=2312] http://librenix.com/?inode=2312

[http://www.topology.org/linux/lingl.html] http://www.topology.org/linux/
lingl.html

[http://atulchitnis.net/writings/gnulinux.php] http://atulchitnis.net/
writings/gnulinux.php
-----------------------------------------------------------------------------

1.2. Trademarks

Microsoft, Windows, Windows NT, Windows 2000, and Windows XP are trademarks
and/or registered trademarks of Microsoft Corporation.

Red Hat is a trademark of Red Hat, Inc., in the United States and other
countries.

SuSE is a trademark of Novell.

Linux is a registered trademark of Linus Torvalds.

UNIX is a registered trademark in the United States and other countries,
licensed exclusively through X/Open Company Ltd.

GNU is a registered trademark of the Free Software Foundation.

Other product names mentioned herein may be trademarks and/or registered
trademarks of their respective companies.
-----------------------------------------------------------------------------

Chapter 2. Overview of a Linux System

    "God saw everything that he had made, and saw that it was very good. " --
    Bible King James Version. Genesis 1:31

This chapter gives an overview of a Linux system. First, the major services
provided by the operating system are described. Then, the programs that
implement these services are described with a considerable lack of detail.
The purpose of this chapter is to give an understanding of the system as a
whole, so that each part is described in detail elsewhere.
-----------------------------------------------------------------------------

2.1. Various parts of an operating system

UNIX and 'UNIX-like' operating systems (such as Linux) consist of a kernel
and some system programs. There are also some application programs for doing
work. The kernel is the heart of the operating system. In fact, it is often
mistakenly considered to be the operating system itself, but it is not. An
operating system provides provides many more services than a plain kernel.

It keeps track of files on the disk, starts programs and runs them
concurrently, assigns memory and other resources to various processes,
receives packets from and sends packets to the network, and so on. The kernel
does very little by itself, but it provides tools with which all services can
be built. It also prevents anyone from accessing the hardware directly,
forcing everyone to use the tools it provides. This way the kernel provides
some protection for users from each other. The tools provided by the kernel
are used via system calls. See manual page section 2 for more information on
these.

The system programs use the tools provided by the kernel to implement the
various services required from an operating system. System programs, and all
other programs, run `on top of the kernel', in what is called the user mode.
The difference between system and application programs is one of intent:
applications are intended for getting useful things done (or for playing, if
it happens to be a game), whereas system programs are needed to get the
system working. A word processor is an application; mount is a system
program. The difference is often somewhat blurry, however, and is important
only to compulsive categorizers.

An operating system can also contain compilers and their corresponding
libraries (GCC and the C library in particular under Linux), although not all
programming languages need be part of the operating system. Documentation,
and sometimes even games, can also be part of it. Traditionally, the
operating system has been defined by the contents of the installation tape or
disks; with Linux it is not as clear since it is spread all over the FTP
sites of the world.
-----------------------------------------------------------------------------

2.2. Important parts of the kernel

The Linux kernel consists of several important parts: process management,
memory management, hardware device drivers, filesystem drivers, network
management, and various other bits and pieces. Figure 2-1 shows some of them.


Figure 2-1. Some of the more important parts of the Linux kernel

[overview-kernel]

Probably the most important parts of the kernel (nothing else works without
them) are memory management and process management. Memory management takes
care of assigning memory areas and swap space areas to processes, parts of
the kernel, and for the buffer cache. Process management creates processes,
and implements multitasking by switching the active process on the processor.

At the lowest level, the kernel contains a hardware device driver for each
kind of hardware it supports. Since the world is full of different kinds of
hardware, the number of hardware device drivers is large. There are often
many otherwise similar pieces of hardware that differ in how they are
controlled by software. The similarities make it possible to have general
classes of drivers that support similar operations; each member of the class
has the same interface to the rest of the kernel but differs in what it needs
to do to implement them. For example, all disk drivers look alike to the rest
of the kernel, i.e., they all have operations like `initialize the drive',
`read sector N', and `write sector N'.

Some software services provided by the kernel itself have similar properties,
and can therefore be abstracted into classes. For example, the various
network protocols have been abstracted into one programming interface, the
BSD socket library. Another example is the virtual filesystem (VFS) layer
that abstracts the filesystem operations away from their implementation. Each
filesystem type provides an implementation of each filesystem operation. When
some entity tries to use a filesystem, the request goes via the VFS, which
routes the request to the proper filesystem driver.

A more in-depth discussion of kernel internals can be found at [http://
www.tldp.org/LDP/lki/index.html] http://www.tldp.org/LDP/lki/index.html. This
document was written for the 2.4 kernel. When I find one for the 2.6 kernel,
I will list it here.
-----------------------------------------------------------------------------

2.3. Major services in a UNIX system

This section describes some of the more important UNIX services, but without
much detail. They are described more thoroughly in later chapters.
-----------------------------------------------------------------------------

2.3.1. init

The single most important service in a UNIX system is provided by init init
is started as the first process of every UNIX system, as the last thing the
kernel does when it boots. When init starts, it continues the boot process by
doing various startup chores (checking and mounting filesystems, starting
daemons, etc).

The exact list of things that init does depends on which flavor it is; there
are several to choose from. init usually provides the concept of single user
mode, in which no one can log in and root uses a shell at the console; the
usual mode is called multiuser mode. Some flavors generalize this as run
levels; single and multiuser modes are considered to be two run levels, and
