        age out old hosts.

    aarp-resolve-time
          The amount of time we will spend trying to resolve an Appletalk
        address.

    aarp-retransmit-limit
          The number of times we will retransmit a query before giving up.

    aarp-tick-time
          Controls the rate at which expires are checked.

    /proc/net/appletalk
        Holds the list of active Appletalk sockets on a machine. The fields
        indicate the DDP type, the local address (in network:node format) the
        remote address, the size of the transmit pending queue, the size of
        the received queue (bytes waiting for applications to read) the state
        and the uid owning the socket.

    /proc/net/atalk_iface
        lists all the interfaces configured for appletalk. It shows the name
        of the interface, its Appletalk address, the network range on that
        address (or network number for phase 1 networks), and the status of
        the interface.

    /proc/net/atalk_route
        lists each known network route. It lists the target (network) that
        the route leads to, the router (may be directly connected), the route
        flags, and the device the route is using.



IPX



        The IPX protocol has no tunable values in proc/sys/net, it does,
        however, provide proc/net/ipx. This lists each IPX socket giving the
        local and remote addresses in Novell format (that is network:node:
        port). In accordance with the strange Novell tradition, everything
        but the port is in hex. Not_Connected is displayed for sockets that
        are not tied to a specific remote address. The Tx and Rx queue sizes
        indicate the number of bytes pending for transmission and reception.
        The state indicates the state the socket is in and the uid is the
        owning uid of the socket.

    ipx_interface
        Lists all IPX interfaces. For each interface it gives the network
        number, the node number, and indicates if the network is the primary
        network. It also indicates which device it is bound to (or Internal
        for internal networks) and the Frame Type if appropriate. Linux
        supports 802.3, 802.2, 802.2 SNAP and DIX (Blue Book) ethernet
        framing for IPX.

    ipx_route
        Table holding a list of IPX routes. For each route it gives the
        destination network, the router node (or Directly) and the network
        address of the router (or Connected) for internal networks.



/proc/sysvipc
    Info of SysVIPC Resources (msg, sem, shm) (2.4)

/proc/tty
    Information about the available and actually used tty's can be found in
    the directory /proc/tty. You'll find entries for drivers and line
    disciplines in this directory.

/proc/tty/drivers
      list of drivers and their usage.

/proc/tty/ldiscs
    registered line disciplines.

/proc/tty/driver/serial
      usage statistic and status of single tty lines.


        To see which tty's are currently in use, you can simply look into the
        file /proc/tty/drivers:


          # cat /proc/tty/drivers
          serial               /dev/cua        5  64-127 serial:callout
          serial               /dev/ttyS       4  64-127 serial
          pty_slave            /dev/pts      143   0-255 pty:slave
          pty_master           /dev/ptm      135   0-255 pty:master
          pty_slave            /dev/pts      142   0-255 pty:slave
          pty_master           /dev/ptm      134   0-255 pty:master
          pty_slave            /dev/pts      141   0-255 pty:slave
          pty_master           /dev/ptm      133   0-255 pty:master
          pty_slave            /dev/pts      140   0-255 pty:slave
          pty_master           /dev/ptm      132   0-255 pty:master
          pty_slave            /dev/pts      139   0-255 pty:slave
          pty_master           /dev/ptm      131   0-255 pty:master
          pty_slave            /dev/pts      138   0-255 pty:slave
          pty_master           /dev/ptm      130   0-255 pty:master
          pty_slave            /dev/pts      137   0-255 pty:slave
          pty_master           /dev/ptm      129   0-255 pty:master
          pty_slave            /dev/pts      136   0-255 pty:slave
          pty_master           /dev/ptm      128   0-255 pty:master
          pty_slave            /dev/ttyp       3   0-255 pty:slave
          pty_master           /dev/pty        2   0-255 pty:master
          /dev/vc/0            /dev/vc/0       4       0 system:vtmaster
          /dev/ptmx            /dev/ptmx       5       2 system
          /dev/console         /dev/console    5       1 system:console
          /dev/tty             /dev/tty        5       0 system:/dev/tty
          unknown              /dev/vc/%d      4    1-63 console



        Note that while the above files tend to be easily readable text
        files, they can sometimes be formatted in a way that is not easily
        digestible. There are many commands that do little more than read the
        above files and format them for easier understanding. For example,
        the free program reads /proc/meminfo and converts the amounts given
        in bytes to kilobytes (and adds a little more information, as well).



/proc/uptime
    The time the system has been up.

/proc/version
      The kernel version.

/proc/video
    BTTV info of video resources.


-----------------------------------------------------------------------------
1.15. /root

  This is the home directory of the System Administrator, 'root'. This may be
somewhat confusing ('root on root') but in former days, '/' was root's home
directory (hence the name of the Administrator account). To keep things
tidier, 'root' got his own home directory. Why not in '/home'? Because '/
home' is often located on a different partition or even on another system and
would thus be inaccessible to 'root' when - for some reason - only '/' is
mounted.

  The FSSTND merely states that this is the recommended location for the home
directory of 'root'. It is left up to the end user to determine the home
directory of 'root'. However, the FSSTND also says that:



  If the home directory of the root account is not stored on the root
  partition it will be necessary to make certain it will default to
  / if it can not be located.

  We recommend against using the root account for tasks that can be
  performed as an unprivileged user, and that it be used solely for
  system administration. For this reason, we recommend that subdirectories
  for mail and other applications not appear in the root account's home
  directory, and that mail for administration roles such as root, postmaster,
  and webmaster be forwarded to an appropriate user.

-----------------------------------------------------------------------------

1.16. /sbin

  Linux discriminates between 'normal' executables and those used for system
maintenance and/or administrative tasks. The latter reside either here or -
the less important ones - in /usr/sbin. Locally installed system
administration programs should be placed into /usr/local/sbin.

  Programs executed after /usr is known to be mounted (when there are no
problems) are generally placed into /usr/sbin. This directory contains
binaries that are essential to the working of the system. These include
system administration as well as maintenance and hardware configuration
programs. You may find lilo, fdisk, init, ifconfig, etc.... here.

  Another directory that contains system binaries is /usr/sbin. This
directory contains other binaries of use to the system administrator. This is
where you will find the network daemons for your system along with other
binaries that (generally) only the system administrator has access to, but
which are not required for system maintenance and repair. Normally, these
directories are never part of normal user's $PATHs, only of roots (PATH is an
environment variable that controls the sequence of locations that the system
will attempt to look in for commands).

  The FSSTND states that:



  /sbin should contain only binaries essential for booting, restoring,
  recovering, and/or repairing the system in addition to the binaries
  in /bin.


  A particular eccentricity of the Linux filesystem hierarchy is that
originally /sbin binaries were kept in /etc.


  Deciding what things go into "sbin" directories is simple: if a normal
  (not a system administrator) user will ever run it directly, then it
  must be placed in one of the "bin" directories. Ordinary users should
  not have to place any of the sbin directories in their path.

  For example, files such as chfn which users only occasionally use must
  still be placed in /usr/bin. ping, although it is absolutely necessary
  for root (network recovery and diagnosis) is often used by users and
  must live in /bin for that reason.

  We recommend that users have read and execute permission for everything
  in /sbin except, perhaps, certain setuid and setgid programs. The
  division between /bin and /sbin was not created for security reasons or
  to prevent users from seeing the operating system, but to provide a
  good partition between binaries that everyone uses and ones that are
  primarily used for administration tasks. There is no inherent security
  advantage in making /sbin off-limits for users.


  FSSTND compliance requires that the following commands, or symbolic links
to commands, are required in /sbin.


       shutdown Command to bring the system down.


  The following files, or symbolic links to files, must be in /sbin if the
corresponding subsystem is installed:


       fastboot   Reboot the system without checking the disks (optional)
       fasthalt   Stop the system without checking the disks (optional)
       fdisk      Partition table manipulator (optional)
       fsck       File system check and repair utility (optional)
       fsck.*     File system check and repair utility for a specific filesystem (optional)
       getty      The getty program (optional)
       halt       Command to stop the system (optional)
       ifconfig   Configure a network interface (optional)
       init       Initial process (optional)
       mkfs       Command to build a filesystem (optional)
       mkfs.*     Command to build a specific filesystem (optional)
       mkswap     Command to set up a swap area (optional)
       reboot     Command to reboot the system (optional)
       route      IP routing table utility (optional)
       swapon     Enable paging and swapping (optional)
       swapoff    Disable paging and swapping (optional)
       update     Daemon to periodically flush filesystem buffers (optional)

-----------------------------------------------------------------------------

1.17. /usr

 /usr usually contains by far the largest share of data on a system. Hence,
this is one of the most important directories in the system as it contains
all the user binaries, their documentation, libraries, header files, etc....
X and its supporting libraries can be found here. User programs like telnet,
ftp, etc.... are also placed here. In the original Unix implementations, /usr
was where the home directories of the users were placed (that is to say, /usr
/someone was then the directory now known as /home/someone). In current
Unices, /usr is where user-land programs and data (as opposed to 'system
land' programs and data) are. The name hasn't changed, but it's meaning has
narrowed and lengthened from "everything user related" to "user usable
programs and data". As such, some people may now refer to this directory as
meaning 'User System Resources' and not 'user' as was originally intended.


/usr is shareable, read-only data. That means that /usr should
be shareable between various FHS-compliant hosts and must not be written to.
Any information that is host-specific or varies with time is stored elsewhere.

Large software packages must not use a direct subdirectory under the /usr
hierarchy.

/usr/X11R6



         Another large subdirectory structure begins here, containing
        libraries, executables, docs, fonts and much more concerning the X
        Window System. Its inclusion here is somewhat inconsistent and so is
        the difference between '/usr' and '/usr/X11R6' directories. One would
        assume that programs that run on X only have their files in the '/usr
        /X11R6' hierarchy, while the others use '/usr'. Regrettably, it isn't
        so. KDE and GNOME put their files in the '/usr' hierarchy, whereas
        the window manager Window Maker uses '/usr/X11R6'. Documentation
        files for X11R6 are not in '/usr/X11R6/doc', but primarily in '/usr/
        X11R6/lib/X11/doc'. This mess is due to the fact that in contrast to
        other operating systems, the graphical desktop isn't an integral part
        of the system. Linux is still primarily used on servers, where
        graphical systems don't make sense.


         This hierarchy is reserved for the X Window System, version 11
        release 6, and related files. To simplify matters and make XFree86
        more compatible with the X Window System on other systems, the
        following symbolic links must be present if /usr/X11R6 exists:


          /usr/bin/X11 -> /usr/X11R6/bin
          /usr/lib/X11 -> /usr/X11R6/lib/X11
          /usr/include/X11 -> /usr/X11R6/include/X11


         In general, software must not be installed or managed via the above
        symbolic links. They are intended for utilization by users only. The
        difficulty is related to the release version of the X Window System -
        in transitional periods, it is impossible to know what release of X11
        is in use.



/usr/X11R6/bin
     XFree86 system binaries. These are necessary for the initialisation,
    configuration and running of the X windowing system. X, xf86config,
    xauth, xmodmap and even xpenguin are located here.

/usr/X11R6/include
     XFree86 system header files. There are required for the compilation of
    some applications that utilise the X toolkit.

/usr/X11R6/lib
     XFree86 system libraries.

/usr/X11R6/lib/modules
     XFree86 system modules. These are the modules that X loads upon startup.
    Without these modules video4linux, DRI and GLX extensions and drivers for
    certain input devices would cease to function.

/usr/X11R6/lib/X11/fonts
     XFree86 system fonts. Fonts that are utilised by 'xfs' (the X Font
    Server) and programs of that ilk.

/usr/bin
     This directory contains the vast majority of binaries on your system.
    Executables in this directory vary widely. For instance vi, gcc,
    gnome-session and mozilla and are all found here.

/usr/doc
     The central documentation directory. Documentation is actually located
    in /usr/share/doc and linked from here.

/usr/etc
     Theoretically, that's another directory for configuration files.
    Virtually unused now.

/usr/games
     Once upon a time, this directory contained network games files. Rarely
    used now.

/usr/include
     The directory for 'header files', needed for compiling user space source
    code.

/usr/include/'package-name'
     Application specific header files.

/usr/info
     This directory used to contain the files for the info documentation
    system. Now they are in '/usr/share/info'.

/usr/lib
     This directory contains program libraries. Libraries are collections of
    frequently used program routines.

/usr/local
     The original idea behind '/usr/local' was to have a separate ('local') '
    /usr' directory on every machine besides '/usr', which might be just
    mounted read-only from somewhere else. It copies the structure of '/usr'.
    These days, '/usr/local' is widely regarded as a good place in which to
    keep self-compiled or third-party programs. The /usr/local hierarchy is
    for use by the system administrator when installing software locally. It
    needs to be safe from being overwritten when the system software is
    updated. It may be used for programs and data that are shareable amongst
    a group of hosts, but not found in /usr. Locally installed software must
    be placed within /usr/local rather than /usr unless it is being installed
    to replace or upgrade software in /usr.

/usr/man
     It once held the man pages. It has been moved to /usr/share/man.

/usr/sbin
     This directory contains programs for administering a system, meant to be
    run by 'root'. Like '/sbin', it's not part of a user's $PATH. Examples of
    included binaries here are chroot, useradd, in.tftpd and pppconfig.

/usr/share
     This directory contains 'shareable', architecture-independent files
    (docs, icons, fonts etc). Note, however, that '/usr/share' is generally
    not intended to be shared by different operating systems or by different
    releases of the same operating system. Any program or package which
    contains or requires data that doesn't need to be modified should store
    that data in '/usr/share' (or '/usr/local/share', if installed locally).
    It is recommended that a subdirectory be used in /usr/share for this
    purpose."

/usr/share/doc
     Location of package specific documentation files. These directories
    often contain useful information that might not be in the man pages. They
    may also contain templates and configuration files for certain utilities
    making configuration that much easier.

/usr/share/info
     Location of 'info' pages. This style of documentation seems to be
    largely ignored now. Manual pages are in far greater favour.

/usr/share/man
     Manual pages. They are organised into 8 sections, which are explained
    below.



        man1: User programs
        Manual pages that describe publicly accessible commands are contained
        in this chapter. Most program documentation that a user will need to
        use is located here.

        man2: System calls
        This section describes all of the system calls (requests for the kernel
        to perform operations).

        man3: Library functions and subroutines
        Section 3 describes program library routines that are not direct calls
        to kernel services. This and chapter 2 are only really of interest to
        programmers.

        man4: Special files
        Section 4 describes the special files, related driver functions, and
        networking support available in the system. Typically, this includes
        the device files found in /dev and the kernel interface to networking
        protocol support.

        man5: File formats
        The formats for many data files are documented in the section 5. This
        includes various include files, program output files, and system files.

        man6: Games
        This chapter documents games, demos, and generally trivial programs.
        Different people have various notions about how essential this is.

        man7: Miscellaneous Manual pages that are difficult to classify are
        designated as being section 7. The troff and other text processing
        macro packages are found here.

        man8: System administration Programs used by system administrators
        for system operation and maintenance are documented here. Some of
        these programs are also occasionally useful for normal users.



/usr/src
     The 'linux' sub-directory holds the Linux kernel sources, header-files
    and documentation.

/usr/src/RPM
     RPM provides a substructure for building RPMs from SRPMs. Organisation
    of this branch is fairly logical with packages being organised according
    to a package's architecture.

/usr/src/RPM/BUILD
     A temporary store for RPM binary files that are being built from source
    code.

/usr/src/RPM/RPMS/athlon, /usr/src/RPM/RPMS/i386, /usr/src/RPM/RPMS/i486, /
    usr/src/RPM/RPMS/i586, /usr/src/RPM/RPMS/i686, /usr/src/RPM/RPMS/noarch
     These directories contain architecture dependent RPM source files.

/usr/src/RPM/SOURCES
     This directory contains the source TAR files, patches, and icon files
    for software to be packaged.

/usr/src/RPM/SPECS
     RPM SPEC files. A SPEC file is a file that contains information as well
    as scripts that are necessary to build a package.

/usr/src/RPM/SRPMS
     Contains the source RPM files which result from a build.

/usr/src/linux
    Contains the source code for the Linux kernel.

/usr/src/linux/.config
     The last kernel source configuration. This file is normally created
    through the 'make config', 'make menuconfig' or 'make xconfig' steps
    during kernel compilation.

/usr/src/linux/.depend, /usr/src/linux/.hdepend
     'make dep' checks the dependencies of the selections you made when you
    created your .config file. It ensures that the required files can be
    found and it builds a list that is to be used during compilation. Should
    this process be successful these two files are created.

/usr/src/linux/COPYING
     GNU License

/usr/src/linux/CREDITS
     A partial credits-file of people that have contributed to the Linux
    project. It is sorted by name and formatted to allow easy grepping and
    beautification by scripts. The fields are: name (N), email (E),
    web-address (W), PGP key ID and fingerprint (P), description (D), and
    snail-mail address (S).

/usr/src/linux/MAINTAINERS
     List of maintainers and details on how to submit kernel changes.

/usr/src/linux/Makefile
     Contains data necessary for compilation of a working kernel. It allows
    developers and end-users to compile a kernel with a few simple steps (ie.
    make dep, make clean, make bzImage, make modules, make modules_install)
