```
Pocket Linux Guide

David Horton


<dhorton<AT>NOSPAM.member.fsf.org>
Revision History
Revision 3.1            2005-04-09             Revised by: DH
Minor clarifications and spelling corrections.
Revision 3.0            2004-11-02             Revised by: DH
Changed bootloader to GRUB rather than LILO. Updated versions on all source
code packages. Made minor clarifications to some shell commands and scripts.
Revision 2.1            2004-02-18             Revised by: DH
Corrected typos. Changed resource site hosting to SourceForge. Added appendix
B to include the GNU Free Documentation License as part of this document.
Revision 2.0            2003-11-08             Revised by: DH
Updated to use GNU coreutils in place of fileutils, sh-utils and textutils.
Updated version numbers on many source code packages. Introduced Freshmeat as
a resource for finding source code. Changed /etc/mtab to a real file rather
than using a symlink to /proc/mounts. Corrected local_fs script errors.
Updated email address.
Revision 1.2            2003-05-31             Revised by: DH
Corrected errors in "strip -o library" commands.
Revision 1.1            2003-05-21             Revised by: DH
Bug fixes, typo corrections and improved XML markup.
Revision 1.0            2003-02-17             Revised by: DH
Initial Release, reviewed by LDP.


The Pocket Linux Guide is for anyone interested in learning the techniques of
building a GNU/Linux system from source code. The guide is structured as a
project that builds a small diskette-based GNU/Linux system called Pocket
Linux. Each chapter explores a small piece of the overall system explaining
how it works, why it is needed and how to build it. After completing the
Pocket Linux project, readers should possess an enhanced knowledge of what
makes GNU/Linux systems work as well as the confidence to explore larger,
more complex source-code-only projects.

-----------------------------------------------------------------------------
Table of Contents
Legal Information
    1. Copyright and License
    2. Disclaimer


Introduction
    1. About Pocket Linux
    2. Prerequisite Skills
    3. Project Format
    4. Help & Support
    5. Feedback


1. Project Initiation
    1.1. A Brief History of GNU/Linux
    1.2. The Goal of Pocket Linux
    1.3. Working Within The Constraints


2. A Simple Prototype
    2.1. Analysis
    2.2. Design
    2.3. Construction
    2.4. Implementation


3. Saving Space
    3.1. Analysis
    3.2. Design
    3.3. Construction
    3.4. Implementation


4. Some Basic Utilities
    4.1. Analysis
    4.2. Design
    4.3. Construction
    4.4. Implementation


5. Checking and Mounting Disks
    5.1. Analysis
    5.2. Design
    5.3. Construction
    5.4. Implementation


6. Automating Startup & Shutdown
    6.1. Analysis
    6.2. Design
    6.3. Construction
    6.4. Implementation


7. Enabling Multiple Users
    7.1. Analysis
    7.2. Design
    7.3. Construction
    7.4. Implementation


8. Filling in the Gaps
    8.1. Analysis
    8.2. Design
    8.3. Construction
    8.4. Implementation


9. Project Wrap Up
    9.1. Celebrating Accomplishments
    9.2. Planning Next Steps


A. Hosting Applications
    A.1. Analysis
    A.2. Design
    A.3. Construction
    A.4. Implementation


B. GNU Free Documentation License
    B.1. PREAMBLE
    B.2. APPLICABILITY AND DEFINITIONS
    B.3. VERBATIM COPYING
    B.4. COPYING IN QUANTITY
    B.5. MODIFICATIONS
    B.6. COMBINING DOCUMENTS
    B.7. COLLECTIONS OF DOCUMENTS
    B.8. AGGREGATION WITH INDEPENDENT WORKS
    B.9. TRANSLATION
    B.10. TERMINATION
    B.11. FUTURE REVISIONS OF THIS LICENSE
    B.12. ADDENDUM: How to use this License for your documents



-----------------------------------------------------------------------------
Legal Information

1. Copyright and License

This document, Pocket Linux Guide, is copyright (c) 2003 - 2005 by David
Horton. Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.2 or any
later version published by the Free Software Foundation; with no Invariant
Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of
the license is available at the end of this document.

Linux is a registered trademark of Linus Torvalds.
-----------------------------------------------------------------------------

2. Disclaimer

This documentation is provided as-is with no warranty of any kind, either
expressed or implied, including, but not limited to, the implied warranties
of merchantability and fitness for a particular purpose. Use the concepts,
examples and information at your own risk. The author(s) do not take any
responsibility for damages that may arise from the use of this document.

All copyrights are held by their respective owners, unless specifically noted
otherwise. Use of a term in this document should not be regarded as affecting
the validity of any trademark or service mark. Naming of particular products
or brands should not be seen as endorsements.
-----------------------------------------------------------------------------

Introduction

1. About Pocket Linux

The Pocket Linux Guide demonstrates how to build a small console-based GNU/
Linux system using only source code and a couple of diskettes. It is intended
for Linux users who would like to gain a deeper understanding about how their
system works beneath the shroud of distribution specific features and tools.
-----------------------------------------------------------------------------

2. Prerequisite Skills

This guide is intended for intermediate to advanced Linux users. It is not
intentionally obscure, but certain assumptions about the readers skill level
are made. Success with this guide depends in part on being able to perform
the following tasks:

��*�Use basic shell commands

��*�Reference man and info pages

��*�Build a custom Linux kernel

��*�Compile source code using make and related tools


-----------------------------------------------------------------------------
3. Project Format

The Pocket Linux Guide takes a hands-on approach to learning. The guide is
written with each chapter building a piece of an overall project. Chapters
are further broken into sections of Analysis, Design, Construction and
Implementation. This format is derived from Rapid Application Development
(RAD) methodology. Without going into detail about design methodologies, the
sections may be summed up as follows.

��*�The Analysis section gives a high-level overview of what is to be
    accomplished in each chapter. It will introduce the tasks that need to be
    completed and why they are important to the overall system.

��*�The Design section defines the source code packages, files and
    configuration necessary to address the requirements set forth in the
    Analysis section. Much of the theory of why certain system files exist
    and what their purpose is can be found here.

��*�The Construction section is where all the hands-on action takes place.
    This section goes into detail about building source code and configuring
    the system files.

��*�The Implementation section will test the proper operation of the project
    at the end of each chapter. Often there are a few shell commands to
    perform and samples of expected screen outputs are given.


Readers interested in learning more about RAD may want to consult a textbook
covering systems analysis and design or visit the following University of
California, Davis website on the subject: [http://sysdev.ucdavis.edu/WEBADM/
document/rad-stages.htm] http://sysdev.ucdavis.edu/WEBADM/document/
rad-stages.htm.
-----------------------------------------------------------------------------

4. Help & Support

Readers are encouraged to visit the Pocket Linux Resource Site at [http://
pocket-linux.sourceforge.net] http://pocket-linux.sourceforge.net/. The
resource site is home to:

��*�Information about the Pocket Linux mailing list.

��*�A web-based troubleshooting forum where readers can ask questions and
    give tips to others.

��*�A collection of diskette images for various chapters.

��*�Additional projects that may be of interest to Pocket Linux Guide
    readers.


-----------------------------------------------------------------------------
5. Feedback

For technical questions about Pocket Linux please use the mailing list or the
troubleshooting forum on the [http://pocket-linux.sourceforge.net] resource
site. General comments and suggestions may be sent to the mailing list or
emailed to the author directly.
-----------------------------------------------------------------------------

Chapter 1. Project Initiation

1.1. A Brief History of GNU/Linux

In the early 90's GNU/Linux systems consisted of little more than a
beta-quality Linux kernel and a small collection of software ported from the
GNU project. It was a true hacker's operating system. There were no CD-ROM's
or GUI installation tools; everything had to be compiled and configured by
the end user. Being a Linux Expert meant knowing your system inside and out.

Toward the middle of the decade several GNU/Linux distributions began
appearing. One of the first was [http://www.slackware.org] Slackware in 1993
and since then there have been many others. Even though there are many
"flavors" of Linux today, the main purpose of the distribution remains the
same. The distribution automates many of the tasks involved in GNU/Linux
installation and configuration taking the burden off of the system
administrator. Being a Linux Expert now means knowing which button to click
in the GUI administration tool.

Recently there has been a yearn for a return to the "good old days" of Linux
when men were men, sysadmins were hardcore geeks and everything was compiled
from source code. A notable indication of this movement was the publication
of the Linux-From-Scratch-HOWTO version 1.0 by Gerard Beekmans in 1999. Being
a Linux Expert once again means knowing how to do it yourself.

For more historical information, see Ragib Hasan's "History of Linux" at
[http://netfiles.uiuc.edu/rhasan/linux] http://netfiles.uiuc.edu/rhasan/linux
-----------------------------------------------------------------------------

1.2. The Goal of Pocket Linux

The purpose of Pocket Linux is to support and encourage people who wish to
explore Linux by building a GNU/Linux system from nothing but source code.
Pocket Linux is not intended to be a full featured system, but rather to give
the reader a taste of what is involved in building an operating system from
source code. After completing the Pocket Linux system the reader should have
enough knowledge to confidently build almost any project using only source
code. Given this direction we can put a few constraints on the project.

��*�The main focus should be learning. The project should not just describe
    how to do something, it should also describe why it should be done.

��*�The required time commitment should be minimal and manageable.

��*�The project should not require any investment in additional hardware or
    reconfiguration of existing hardware to set up a lab environment.

��*�Readers should not need to know any programming languages in order to
    complete the project.

��*�To remain true to the spirit of GNU/Linux, all software used in the
    project should be covered under the GNU/GPL or another, similarly
    liberal, open-source license.


-----------------------------------------------------------------------------
1.3. Working Within The Constraints

The Pocket Linux project gets its name from the fact that the bulk of the
project fits onto two diskettes making it possible to carry the entire,
working system around in one's pocket. This has the advantage of not
requiring any additional hardware since any PC can be booted from the
diskettes without disrupting any OS that exists on the hard drive. Using
diskettes also partially addresses the aspect of time commitment, because the
project size and complexity is necessarily limited by the 1.44 Megabyte size
of the installation media.

To further reduce the time commitment, the Pocket Linux project is divided
into several phases, each one chapter in length. Each phase builds only a
small piece of the overall project, but at the same time the conclusion of
each chapter results in a self-contained, working system. This step-by-step
approach should allow readers to pace themselves and not feel the need to
rush to see results.

Chapters are further subdivided into four sections. The first two sections,
analysis and design, focus on the theory of what is to be accomplished in
each phase and why. The last two sections, construction and implementation,
detail the steps needed to do the actual building. Advanced readers, who may
be familiar with the theories laid out in a particular chapter are encouraged
to gloss over the analysis and design sections in the interest of time. The
separation of theory from hands-on exercises should allow readers of all
skill levels to complete the project without feeling either completely lost
or mired in too much detail.

Finally, the Pocket Linux project will strive to use GNU/GPL software when
possible and other open-source licensed software when there is no GNU/GPL
alternative. Also, Pocket Linux will never require any programming more
complex than a BASH shell script.
-----------------------------------------------------------------------------

Chapter 2. A Simple Prototype

2.1. Analysis

Since this is the first phase of the project it will be kept very simple. The
goal here is not to create the ultimate GNU/Linux system on the first try.
Instead, we will be building a very minimal, working system to be used as a
building block in subsequent phases of the project. Keeping this in mind, we
can list a few goals for phase one.

��*�Keep it simple to avoid stressing out.

��*�Build something that works for instant gratification.

��*�Make something that it is useful in later phases of the project.


-----------------------------------------------------------------------------
2.2. Design

2.2.1. Simplification

Take a moment to skim through the Bootdisk-HOWTO or the
From-PowerUp-to-BASH-Prompt-HOWTO. These HOWTO documents can be found online
at [http://www.tldp.org/docs.html#howto] http://www.tldp.org/docs.html#howto.
Both documents offer an excellent view of what it takes to get a GNU/Linux
system up and running. There is also a lot of information to digest. Remember
that one of our goals is, "keep it simple to avoid stressing out," so we want
to ignore everything but the absolutely critical pieces of a boot / root
diskset.

Basically it boils down to the following required items:

��*�A boot loader

��*�The Linux kernel

��*�A shell

��*�Some /dev files


We don't even need an init daemon. The kernel can be told to run the shell
directly by passing it an option through the boot loader.

For easy construction we will build a two-disk boot / root set rather than
trying to get everything onto a single diskette. The boot loader and kernel
will go on the boot disk and the shell will reside on the root disk.
-----------------------------------------------------------------------------

2.2.2. Boot Disk

For the boot disk we simply need to install the GRUB bootloader and a Linux
kernel. We will need to use a kernel that does not require modules for the
hardware we need to access. Mainly, it should have compiled-in support for
the floppy drive, ram disk, second extended filesystem, proc filesystem, ELF
binaries, and a text-based console. If such a kernel is not available, it
will need to be built from source code. Kwan Lowe's Kernel Rebuild Guide is a
good reference for this task, however we can ignore the sections that deal
with modules and the initial ramdisk.
-----------------------------------------------------------------------------

2.2.3. Root Disk

For the root disk we will need a floppy that has been prepared with a
filesystem. We will also need a BASH shell that is statically-linked so we
can avoid the additional complexities of shared libraries. The configure
program in the BASH source code recognizes the --enable-static-link option
for this feature. We will also be using the --enable-minimal-config option to
keep the BASH binary down to a manageable size. Additional requirements for
the root disk are a /dev directory and a device file for the console. The
console device is required for BASH to be able to communicate with the
keyboard and video display.
-----------------------------------------------------------------------------

2.2.4. CPU Compatibility

There is one other, less obvious requirement to keep in mind and that is CPU
compatibility. Each generation of CPU features a more complex architecture
than its predecessor. Late generation chips have additional registers and
instructions when compared to an older 486 or 386. So a kernel optimized for
a new, fast 6x86 machine will not run on an older box. (See the README file
in the Linux kernel source code for details.) A BASH shell built for a 6x86
will probably not run on an older processor either. To avoid this problem, we
can choose the 386 as a lowest common denominator CPU and build all the code
for that architecture.
-----------------------------------------------------------------------------

2.3. Construction

In this section, we will be building the actual boot disk and root disk
floppies. Lines preceded by bash# indicate a shell command and lines starting
with grub> indicate a command typed within the grub shell.
-----------------------------------------------------------------------------

2.3.1. Prepare the boot disk media

Insert a blank diskette labeled "boot disk".

Note It may be necessary to erase the "blank" diskette if it comes factory
     pre-formatted for another, non-Linux operating system. This can be done
     using the command dd if=/dev/zero of=/dev/fd0 bs=1k count=1440

bash# mke2fs -m0 /dev/fd0
bash# mount /dev/fd0 /mnt
-----------------------------------------------------------------------------

2.3.2. Build the GRUB bootloader

Get the GRUB source code from [ftp://alpha.gnu.org/gnu/grub/] ftp://
alpha.gnu.org/gnu/grub/ and unpack it into the /usr/src directory.

Configure and build the GRUB source code for an i386 processor by using the
following commands:
bash# cd /usr/src/grub-0.95
bash# export CC="gcc -mcpu=i386"
bash# ./configure --host=i386-pc-linux-gnu --without-curses
bash# make
-----------------------------------------------------------------------------

2.3.3. Copy the bootloader files to diskette

Normally, after compiling source code, one would use the command make install
to copy the finished files to their proper destinations in the filesystem.
However, using make install does not work well with small media like the
floppy disks we are using. The problem is that there are many files in a
package besides the actual binaries that get the job done. For example, there
are often man or info pages that provide documentation. These extra files can
take up more space than we can spare on the diskette. We can work around this
limitation by copying essential files manually rather than using make install
.

For GRUB to boot we will need to copy the stage1 and stage2 bootloader files
to the /boot/grub directory on the boot floppy.
bash# mkdir -p /mnt/boot/grub
bash# cp /usr/src/grub-0.95/stage1/stage1 /mnt/boot/grub
bash# cp /usr/src/grub-0.95/stage2/stage2 /mnt/boot/grub
-----------------------------------------------------------------------------

2.3.4. Finish bootloader installation

Once the bootloader's files are copied to the boot disk we can enter the grub
shell to finish the installation.
bash# /usr/src/grub-0.95/grub/grub
grub> root (fd0)
grub> setup (fd0)
grub> quit
-----------------------------------------------------------------------------

2.3.5. Build the Linux kernel

The steps for building the kernel were tested using Linux kernel version
2.4.26 and should work any 2.4.x or 2.6.x kernel. The latest version of the
kernel source code may be downloaded from [http://www.kernel.org/] http://
www.kernel.org/ or one of its mirrors.

Note The instructions below are very brief and are intended for someone who
     has previous experience building custom kernels. A more detailed
     explanation of the kernel building process can be found in the Kernel
     Rebuild Guide by Kwan Lowe.

bash# cd /usr/src/linux
bash# make menuconfig

Be sure to configure support for the following:

��*�386 processor

��*�Console on virtual terminal (2.4.x kernels only)

��*�ELF binaries

��*�Floppy disk

��*�proc filesystem

��*�RAM disk with a default size of 4096K

��*�Second extended (ext2) filesystem

��*�VGA console


bash# make dep
bash# make clean
bash# make bzImage
-----------------------------------------------------------------------------

2.3.6. Copy the kernel to diskette

bash# cp /usr/src/linux/arch/i386/boot/bzImage /mnt/boot/vmlinuz
-----------------------------------------------------------------------------

2.3.7. Unmount the boot disk

bash# cd /
bash# umount /mnt
-----------------------------------------------------------------------------

2.3.8. Prepare the root disk media

Insert a blank diskette labeled "root disk".

bash# mke2fs -m0 /dev/fd0
bash# mount /dev/fd0 /mnt
-----------------------------------------------------------------------------

2.3.9. Build BASH

Get the bash-3.0 source code package from [ftp://ftp.gnu.org/gnu/bash/] ftp:/
/ftp.gnu.org/gnu/bash/ and untar it into the /usr/src directory.

Build BASH for an i386 CPU with the following commands:

bash# cd /usr/src/bash-3.0
bash# export CC="gcc -mcpu=i386"
bash# ./configure --enable-static-link \
  --enable-minimal-config --host=i386-pc-linux-gnu
bash# make
bash# strip bash
-----------------------------------------------------------------------------

2.3.10. Copy BASH to the root disk

bash# mkdir /mnt/bin
bash# cp bash /mnt/bin/bash
bash# ln -s bash /mnt/bin/sh
-----------------------------------------------------------------------------

2.3.11. Create device files that BASH needs

bash# mkdir /mnt/dev
bash# mknod /mnt/dev/console c 5 1
-----------------------------------------------------------------------------

2.3.12. Unmount the root disk

bash# cd /
bash# umount /mnt
-----------------------------------------------------------------------------

2.4. Implementation

2.4.1. System startup

Follow these steps to boot the system:

��*�Restart the PC with the boot disk in the floppy drive.

��*�When the grub> prompt appears, type kernel (fd0)/boot/vmlinuz init=/bin/
    sh root=/dev/fd0 load_ramdisk=1 prompt_ramdisk=1 and press Enter.

��*�After the kernel loads, type boot and press Enter.

��*�Insert the root disk when prompted.


If all goes well the screen should look something like the example shown
below.

GNU GRUB version 0.95
