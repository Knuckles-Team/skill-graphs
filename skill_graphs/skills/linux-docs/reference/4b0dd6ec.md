   events presumably dropped by the kernel before invocation of this
   program (e.g., because the root filesystem has not been mounted) and
   submitting such synthetic hotplug events to udev
   udevinfo

   Allows users to query the udev database for information on any device
   currently present on the system; it also provides a way to query any
   device in the sysfs tree to help create udev rules
   udevtest

   Simulates a udev run for the given device, and prints out the name of
   the node the real udev would have created or (not in LFS) the name of
   the renamed network interface
   /etc/udev

   Contains udev configuration files, device permissions, and rules for
   device naming

6.59. Util-linux-2.12q

   The Util-linux package contains miscellaneous utility programs. Among
   them are utilities for handling file systems, consoles, partitions,
   and messages.
   Approximate build time: 0.2 SBU
   Required disk space: 11.6 MB
   Installation depends on: Bash, Binutils, Coreutils, Diffutils, GCC,
   Gettext, Glibc, Grep, Make, Ncurses, Sed, and Zlib

6.59.1. FHS compliance notes

   The FHS recommends using the /var/lib/hwclock directory instead of the
   usual /etc directory as the location for the adjtime file. To make the
   hwclock program FHS-compliant, run the following:
sed -i 's@etc/adjtime@var/lib/hwclock/adjtime@g' \
    hwclock/hwclock.c
mkdir -p /var/lib/hwclock

6.59.2. Installation of Util-linux

   Util-linux fails to compile against newer versions of
   Linux-Libc-Headers. The following patch properly fixes this issue:
patch -Np1 -i ../util-linux-2.12q-cramfs-1.patch

   Util-linux has a security vulnerability that could allow a user to
   remount a volume without the nosuid option. The following patch fixes
   this issue:
patch -Np1 -i ../util-linux-2.12q-umount_fix-1.patch

   Prepare Util-linux for compilation:
./configure

   Compile the package:
make HAVE_KILL=yes HAVE_SLN=yes

   The meaning of the make parameters:

   HAVE_KILL=yes
          This prevents the kill program (already installed by Procps)
          from being built and installed again.

   HAVE_SLN=yes
          This prevents the sln program (a statically linked version of
          ln already installed by Glibc) from being built and installed
          again.

   This package does not come with a test suite.

   Install the package and move the logger binary to /bin as it is needed
   by the LFS-Bootscripts package:
make HAVE_KILL=yes HAVE_SLN=yes install
mv /usr/bin/logger /bin

6.59.3. Contents of Util-linux

   Installed programs: agetty, arch, blockdev, cal, cfdisk, chkdupexe,
   col, colcrt, colrm, column, ctrlaltdel, cytune, ddate, dmesg, elvtune,
   fdformat, fdisk, fsck.cramfs, fsck.minix, getopt, hexdump, hwclock,
   ipcrm, ipcs, isosize, line, logger, look, losetup, mcookie, mkfs,
   mkfs.bfs, mkfs.cramfs, mkfs.minix, mkswap, more, mount, namei, pg,
   pivot_root, ramsize (link to rdev), raw, rdev, readprofile, rename,
   renice, rev, rootflags (link to rdev), script, setfdprm, setsid,
   setterm, sfdisk, swapdev, swapoff (link to swapon), swapon, tunelp,
   ul, umount, vidmode (link to rdev), whereis, and write

Short Descriptions

   agetty

   Opens a tty port, prompts for a login name, and then invokes the login
   program
   arch

   Reports the machine's architecture
   blockdev

   Allows users to call block device ioctls from the command line
   cal

   Displays a simple calendar
   cfdisk

   Manipulates the partition table of the given device
   chkdupexe

   Finds duplicate executables
   col

   Filters out reverse line feeds
   colcrt

   Filters nroff output for terminals that lack some capabilities, such
   as overstriking and half-lines
   colrm

   Filters out the given columns
   column

   Formats a given file into multiple columns
   ctrlaltdel

   Sets the function of the Ctrl+Alt+Del key combination to a hard or a
   soft reset
   cytune

   Tunes the parameters of the serial line drivers for Cyclades cards
   ddate

   Gives the Discordian date or converts the given Gregorian date to a
   Discordian one
   dmesg

   Dumps the kernel boot messages
   elvtune

   Tunes the performance and interactivity of a block device
   fdformat

   Low-level formats a floppy disk
   fdisk

   Manipulates the partition table of the given device
   fsck.cramfs

   Performs a consistency check on the Cramfs file system on the given
   device
   fsck.minix

   Performs a consistency check on the Minix file system on the given
   device
   getopt

   Parses options in the given command line
   hexdump

   Dumps the given file in hexadecimal or in another given format
   hwclock

   Reads or sets the system's hardware clock, also called the Real-Time
   Clock (RTC) or Basic Input-Output System (BIOS) clock
   ipcrm

   Removes the given Inter-Process Communication (IPC) resource
   ipcs

   Provides IPC status information
   isosize

   Reports the size of an iso9660 file system
   line

   Copies a single line
   logger

   Enters the given message into the system log
   look

   Displays lines that begin with the given string
   losetup

   Sets up and controls loop devices
   mcookie

   Generates magic cookies (128-bit random hexadecimal numbers) for xauth
   mkfs

   Builds a file system on a device (usually a hard disk partition)
   mkfs.bfs

   Creates a Santa Cruz Operations (SCO) bfs file system
   mkfs.cramfs

   Creates a cramfs file system
   mkfs.minix

   Creates a Minix file system
   mkswap

   Initializes the given device or file to be used as a swap area
   more

   A filter for paging through text one screen at a time
   mount

   Attaches the file system on the given device to a specified directory
   in the file-system tree
   namei

   Shows the symbolic links in the given pathnames
   pg

   Displays a text file one screen full at a time
   pivot_root

   Makes the given file system the new root file system of the current
   process
   ramsize

   Sets the size of the RAM disk in a bootable image
   raw

   Used to bind a Linux raw character device to a block device
   rdev

   Queries and sets the root device, among other things, in a bootable
   image
   readprofile

   Reads kernel profiling information
   rename

   Renames the given files, replacing a given string with another
   renice

   Alters the priority of running processes
   rev

   Reverses the lines of a given file
   rootflags

   Sets the rootflags in a bootable image
   script

   Makes a typescript of a terminal session
   setfdprm

   Sets user-provided floppy disk parameters
   setsid

   Runs the given program in a new session
   setterm

   Sets terminal attributes
   sfdisk

   A disk partition table manipulator
   swapdev

   Sets the swap device in a bootable image
   swapoff

   Disables devices and files for paging and swapping
   swapon

   Enables devices and files for paging and swapping and lists the
   devices and files currently in use
   tunelp

   Tunes the parameters of the line printer
   ul

   A filter for translating underscores into escape sequences indicating
   underlining for the terminal in use
   umount

   Disconnects a file system from the system's file tree
   vidmode

   Sets the video mode in a bootable image
   whereis

   Reports the location of the binary, source, and man page for the given
   command
   write

   Sends a message to the given user if that user has not disabled
   receipt of such messages

6.60. About Debugging Symbols

   Most programs and libraries are, by default, compiled with debugging
   symbols included (with gcc's -g option). This means that when
   debugging a program or library that was compiled with debugging
   information included, the debugger can provide not only memory
   addresses, but also the names of the routines and variables.

   However, the inclusion of these debugging symbols enlarges a program
   or library significantly. The following is an example of the amount of
   space these symbols occupy:
     * a bash binary with debugging symbols: 1200 KB
     * a bash binary without debugging symbols: 480 KB
     * Glibc and GCC files (/lib and /usr/lib) with debugging symbols: 87
       MB
     * Glibc and GCC files without debugging symbols: 16 MB

   Sizes may vary depending on which compiler and C library were used,
   but when comparing programs with and without debugging symbols, the
   difference will usually be a factor between two and five.

   Because most users will never use a debugger on their system software,
   a lot of disk space can be regained by removing these symbols. The
   next section shows how to strip all debugging symbols from the
   programs and libraries. Additional information on system optimization
   can be found at
   [481]http://www.linuxfromscratch.org/hints/downloads/files/optimizatio
   n.txt.

6.61. Stripping Again

   If the intended user is not a programmer and does not plan to do any
   debugging on the system software, the system size can be decreased by
   about 200 MB by removing the debugging symbols from binaries and
   libraries. This causes no inconvenience other than not being able to
   debug the software fully anymore.

   Most people who use the command mentioned below do not experience any
   difficulties. However, it is easy to make a typo and render the new
   system unusable, so before running the strip command, it is a good
   idea to make a backup of the current situation.

   Before performing the stripping, take special care to ensure that none
   of the binaries that are about to be stripped are running. If unsure
   whether the user entered chroot with the command given in
   [482]Section 6.3, "Entering the Chroot Environment," first exit from
   chroot:
logout

   Then reenter it with:
chroot $LFS /tools/bin/env -i \
    HOME=/root TERM=$TERM PS1='\u:\w\$ ' \
    PATH=/bin:/usr/bin:/sbin:/usr/sbin \
    /tools/bin/bash --login

   Now the binaries and libraries can be safely stripped:
/tools/bin/find /{,usr/}{bin,lib,sbin} -type f \
   -exec /tools/bin/strip --strip-debug '{}' ';'

   A large number of files will be reported as having their file format
   not recognized. These warnings can be safely ignored. These warnings
   indicate that those files are scripts instead of binaries.

   If disk space is very tight, the --strip-all option can be used on the
   binaries in /{,usr/}{bin,sbin} to gain several more megabytes. Do not
   use this option on libraries--they will be destroyed.

6.62. Cleaning Up

   From now on, when reentering the chroot environment after exiting, use
   the following modified chroot command:
chroot "$LFS" /usr/bin/env -i \
    HOME=/root TERM="$TERM" PS1='\u:\w\$ ' \
    PATH=/bin:/usr/bin:/sbin:/usr/sbin \
    /bin/bash --login

   The reason for this is that the programs in /tools are no longer
   needed. Since they are no longer needed you can delete the /tools
   directory if so desired or tar it up and keep it to build another
   final system.

Note

   Removing /tools will also remove the temporary copies of Tcl, Expect,
   and DejaGNU which were used for running the toolchain tests. If you
   need these programs later on, they will need to be recompiled and
   re-installed. The BLFS book has instructions for this (see
   [483]http://www.linuxfromscratch.org/blfs/).

Chapter 7. Setting Up System Bootscripts

7.1. Introduction

   This chapter details how to install and configure the LFS-Bootscripts
   package. Most of these scripts will work without modification, but a
   few require additional configuration files because they deal with
   hardware-dependent information.

   System-V style init scripts are employed in this book because they are
   widely used. For additional options, a hint detailing the BSD style
   init setup is available at
   [484]http://www.linuxfromscratch.org/hints/downloads/files/bsd-init.tx
   t. Searching the LFS mailing lists for "depinit" will also offer
   additional choices.

   If using an alternative style of init scripts, skip this chapter and
   move on to [485]Chapter 8.

7.2. LFS-Bootscripts-3.2.1

   The LFS-Bootscripts package contains a set of scripts to start/stop
   the LFS system at bootup/shutdown.
   Approximate build time: 0.1 SBU
   Required disk space: 0.3 MB
   Installation depends on: Bash and Coreutils

7.2.1. Installation of LFS-Bootscripts

   Install the package:
make install

7.2.2. Contents of LFS-Bootscripts

   Installed scripts: checkfs, cleanfs, console, functions, halt,
   hotplug, ifdown, ifup, localnet, mountfs, mountkernfs, network, rc,
   reboot, sendsignals, setclock, static, swap, sysklogd, template, and
   udev

Short Descriptions

   checkfs

   Checks the integrity of the file systems before they are mounted (with
   the exception of journal and network based file systems)
   cleanfs

   Removes files that should not be preserved between reboots, such as
   those in /var/run/ and /var/lock/; it re-creates /var/run/utmp and
   removes the possibly present /etc/nologin, /fastboot, and /forcefsck
   files
   console

   Loads the correct keymap table for the desired keyboard layout; it
   also sets the screen font
   functions

   Contains common functions, such as error and status checking, that are
   used by several bootscripts
   halt

   Halts the system
   hotplug

   Loads modules for system devices
   ifdown

   Assists the network script with stopping network devices
   ifup

   Assists the network script with starting network devices
   localnet

   Sets up the system's hostname and local loopback device
   mountfs

   Mounts all file systems, except ones that are marked noauto or are
   network based
   mountkernfs

   Mounts virtual kernel file systems, such as proc
   network

   Sets up network interfaces, such as network cards, and sets up the
   default gateway (where applicable)
   rc

   The master run-level control script; it is responsible for running all
   the other bootscripts one-by-one, in a sequence determined by the name
   of the symbolic links being processed
   reboot

   Reboots the system
   sendsignals

   Makes sure every process is terminated before the system reboots or
   halts
   setclock

   Resets the kernel clock to local time in case the hardware clock is
   not set to UTC time
   static

   Provides the functionality needed to assign a static Internet Protocol
   (IP) address to a network interface
   swap

   Enables and disables swap files and partitions
   sysklogd

   Starts and stops the system and kernel log daemons
   template

   A template to create custom bootscripts for other daemons
   udev

   Prepares the /dev directory and starts Udev

7.3. How Do These Bootscripts Work?

   Linux uses a special booting facility named SysVinit that is based on
   a concept of run-levels. It can be quite different from one system to
   another, so it cannot be assumed that because things worked in one
   particular Linux distribution, they should work the same in LFS too.
   LFS has its own way of doing things, but it respects generally
   accepted standards.

   SysVinit (which will be referred to as "init" from now on) works using
   a run-levels scheme. There are seven (numbered 0 to 6) run-levels
   (actually, there are more run-levels, but they are for special cases
   and are generally not used. See init(8) for more details), and each
   one of those corresponds to the actions the computer is supposed to
   perform when it starts up. The default run-level is 3. Here are the
   descriptions of the different run-levels as they are implemented:

   0: halt the computer
   1: single-user mode
   2: multi-user mode without networking
   3: multi-user mode with networking
   4: reserved for customization, otherwise does the same as 3
   5: same as 4, it is usually used for GUI login (like X's
   xdm or KDE's  kdm)
   6: reboot the computer

   The command used to change run-levels is init [runlevel], where
   [runlevel] is the target run-level. For example, to reboot the
   computer, a user could issue the init 6 command, which is an alias for
   the reboot command. Likewise, init 0 is an alias for the halt command.

   There are a number of directories under /etc/rc.d that look like rc?.d
   (where ? is the number of the run-level) and rcsysinit.d, all
   containing a number of symbolic links. Some begin with a K, the others
   begin with an S, and all of them have two numbers following the
   initial letter. The K means to stop (kill) a service and the S means
   to start a service. The numbers determine the order in which the
   scripts are run, from 00 to 99--the lower the number the earlier it
   gets executed. When init switches to another run-level, the
   appropriate services are either started or stopped, depending on the
   runlevel chosen.

   The real scripts are in /etc/rc.d/init.d. They do the actual work, and
   the symlinks all point to them. Killing links and starting links point
   to the same script in /etc/rc.d/init.d. This is because the scripts
   can be called with different parameters like start, stop, restart,
   reload, and status. When a K link is encountered, the appropriate
   script is run with the stop argument. When an S link is encountered,
   the appropriate script is run with the start argument.

   There is one exception to this explanation. Links that start with an S
   in the rc0.d and rc6.d directories will not cause anything to be
   started. They will be called with the parameter stop to stop
   something. The logic behind this is that when a user is going to
   reboot or halt the system, nothing needs to be started. The system
   only needs to be stopped.

   These are descriptions of what the arguments make the scripts do:

   start
          The service is started.

   stop
          The service is stopped.

   restart
          The service is stopped and then started again.

   reload
          The configuration of the service is updated. This is used after
          the configuration file of a service was modified, when the
          service does not need to be restarted.

   status
          Tells if the service is running and with which PIDs.

   Feel free to modify the way the boot process works (after all, it is
   your own LFS system). The files given here are an example of how it
   can be done.

7.4. Device and Module Handling on an LFS System

   In [486]Chapter 6, we installed the Udev package. Before we go into
   the details regarding how this works, a brief history of previous
   methods of handling devices is in order.

   Linux systems in general traditionally use a static device creation
   method, whereby a great many device nodes are created under /dev
   (sometimes literally thousands of nodes), regardless of whether the
   corresponding hardware devices actually exist. This is typically done
   via a MAKEDEV script, which contains a number of calls to the mknod
   program with the relevant major and minor device numbers for every
   possible device that might exist in the world. Using the Udev method,
   only those devices which are detected by the kernel get device nodes
   created for them. Because these device nodes will be created each time
   the system boots, they will be stored on a tmpfs file system (a
   virtual file system that resides entirely in system memory). Device
   nodes do not require much space, so the memory that is used is
   negligible.

7.4.1. History

   In February 2000, a new filesystem called devfs was merged into the
   2.3.46 kernel and was made available during the 2.4 series of stable
   kernels. Although it was present in the kernel source itself, this
   method of creating devices dynamically never received overwhelming
   support from the core kernel developers.

   The main problem with the approach adopted by devfs was the way it
   handled device detection, creation, and naming. The latter issue, that
   of device node naming, was perhaps the most critical. It is generally
   accepted that if device names are allowed to be configurable, then the
   device naming policy should be up to a system administrator, not
   imposed on them by any particular developer(s). The devfs file system
   also suffers from race conditions that are inherent in its design and
   cannot be fixed without a substantial revision to the kernel. It has
   also been marked as deprecated due to a lack of recent maintenance.

   With the development of the unstable 2.5 kernel tree, later released
   as the 2.6 series of stable kernels, a new virtual filesystem called
   sysfs came to be. The job of sysfs is to export a view of the system's
   hardrware configuration to userspace processes. With this
   userspace-visible representation, the possibility of seeing a
   userspace replacement for devfs became much more realistic.

7.4.2. Udev Implementation

   The sysfs filesystem was mentioned briefly above. One may wonder how
   sysfs knows about the devices present on a system and what device
   numbers should be used for them. Drivers that have been compiled into
   the kernel directly register their objects with sysfs as they are
   detected by the kernel. For drivers compiled as modules, this
   registration will happen when the module is loaded. Once the sysfs
   filesystem is mounted (on /sys), data which the built-in drivers
   registered with sysfs are available to userspace processes and to udev
   for device node creation.

   The S10udev initscript takes care of creating these device nodes when
   Linux is booted. This script starts by registering /sbin/udevsend as a
   hotplug event handler. Hotplug events (discussed below) are not
   usually generated during this stage, but udev is registered just in
   case they do occur. The udevstart program then walks through the /sys
   filesystem and creates devices under /dev that match the descriptions.
   For example, /sys/class/tty/vcs/dev contains the string "7:0" This
   string is used by udevstart to create /dev/vcs with major number 7 and
   minor 0. The names and permissions of the nodes created under the /dev
   directory are configured according to the rules specified in the files
   within the /etc/udev/rules.d/ directory. These are numbered in a
   similar fashion to the LFS-Bootscripts package. If udev can't find a
   rule for the device it is creating, it will default permissions to 660
   and ownership to root:root.

   Once the above stage is complete, all devices that were already
   present and have compiled-in drivers will be available for use. This
   leads us to the devices that have modular drivers.

   Earlier, we mentioned the concept of a "hotplug event handler." When a
   new device connection is detected by the kernel, the kernel will
   generate a hotplug event and look at the file /proc/sys/kernel/hotplug
   to determine the userspace program that handles the device's
   connection. The udev bootscript registered udevsend as this handler.
   When these hotplug events are generated, the kernel will tell udev to
   check the /sys filesystem for the information pertaining to this new
   device and create the /dev entry for it.

   This brings us to one problem that exists with udev, and likewise with
   devfs before it. It is commonly referred to as the "chicken and egg"
   problem. Most Linux distributions handle loading modules via entries
   in /etc/modules.conf. Access to a device node causes the appropriate
   kernel module to load. With udev, this method will not work because
   the device node does not exist until the module is loaded. To solve
   this, the S05modules bootscript was added to the LFS-Bootscripts
   package, along with the /etc/sysconfig/modules file. By adding module
   names to the modules file, these modules will be loaded when the
   computer starts up. This allows udev to detect the devices and create
   the appropriate device nodes.

   Note that on slower machines or for drivers that create a lot of
   device nodes, the process of creating devices may take a few seconds
   to complete. This means that some device nodes may not be immediately
   accessible.

7.4.3. Handling Hotpluggable/Dynamic Devices

   When you plug in a device, such as a Universal Serial Bus (USB) MP3
   player, the kernel recognizes that the device is now connected and
   generates a hotplug event. If the driver is already loaded (either
   because it was compiled into the kernel or because it was loaded via
   the S05modules bootscript), udev will be called upon to create the
   relevant device node(s) according to the sysfs data available in /sys.

   If the driver for the just plugged in device is available as a module
   but currently unloaded, the Hotplug package will load the appropriate
   module and make this device available by creating the device node(s)
   for it.

7.4.4. Problems with Creating Devices

   There are a few known problems when it comes to automatically creating
   device nodes:

   1) A kernel driver may not export its data to sysfs.

   This is most common with third party drivers from outside the kernel
   tree. Udev will be unable to automatically create device nodes for
   such drivers. Use the /etc/sysconfig/createfiles configuration file to
   manually create the devices. Consult the devices.txt file inside the
