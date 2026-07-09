brw-rw----    1 root     disk       3,  20 Mar 15  2002 /dev/hda20
brw-rw----    1 root     disk       3,   3 Mar 15  2002 /dev/hda3
brw-rw----    1 root     disk       3,   4 Mar 15  2002 /dev/hda4
brw-rw----    1 root     disk       3,   5 Mar 15  2002 /dev/hda5
brw-rw----    1 root     disk       3,   6 Mar 15  2002 /dev/hda6
brw-rw----    1 root     disk       3,   7 Mar 15  2002 /dev/hda7
brw-rw----    1 root     disk       3,   8 Mar 15  2002 /dev/hda8
brw-rw----    1 root     disk       3,   9 Mar 15  2002 /dev/hda9
brw-rw----    1 root     disk       3,  64 Mar 15  2002 /dev/hdb
brw-rw----    1 root     disk       3,  65 Mar 15  2002 /dev/hdb1
brw-rw----    1 root     disk       3,  74 Mar 15  2002 /dev/hdb10
brw-rw----    1 root     disk       3,  75 Mar 15  2002 /dev/hdb11
brw-rw----    1 root     disk       3,  76 Mar 15  2002 /dev/hdb12
brw-rw----    1 root     disk       3,  77 Mar 15  2002 /dev/hdb13
brw-rw----    1 root     disk       3,  78 Mar 15  2002 /dev/hdb14
brw-rw----    1 root     disk       3,  79 Mar 15  2002 /dev/hdb15
brw-rw----    1 root     disk       3,  80 Mar 15  2002 /dev/hdb16
brw-rw----    1 root     disk       3,  81 Mar 15  2002 /dev/hdb17
brw-rw----    1 root     disk       3,  82 Mar 15  2002 /dev/hdb18
brw-rw----    1 root     disk       3,  83 Mar 15  2002 /dev/hdb19
brw-rw----    1 root     disk       3,  66 Mar 15  2002 /dev/hdb2
brw-rw----    1 root     disk       3,  84 Mar 15  2002 /dev/hdb20
brw-rw----    1 root     disk       3,  67 Mar 15  2002 /dev/hdb3
brw-rw----    1 root     disk       3,  68 Mar 15  2002 /dev/hdb4
brw-rw----    1 root     disk       3,  69 Mar 15  2002 /dev/hdb5
brw-rw----    1 root     disk       3,  70 Mar 15  2002 /dev/hdb6
brw-rw----    1 root     disk       3,  71 Mar 15  2002 /dev/hdb7
brw-rw----    1 root     disk       3,  72 Mar 15  2002 /dev/hdb8
brw-rw----    1 root     disk       3,  73 Mar 15  2002 /dev/hdb9
brw-rw----    1 root     disk      22,   0 Mar 15  2002 /dev/hdc
brw-rw----    1 root     disk      22,  64 Mar 15  2002 /dev/hdd

The major number for both had and hdb devices is 3. Of course, the minor
number changes for each specific partition. The definition of each major
number category can be examined by looking at the contents of the /usr/src/
linux/include/linux/major.h file. The devices.txt also documents major and
minor numbers. It is located in the /usr/src/linux/Documentation directory.
This file defines the major numbers. Almost all files devices are created by
default at the install time. However, you can always create a device using
the mknod command or the MAKEDEV script which is located in the /dev
directory itself. Devices can be created with this utility by supplying the
device to be created, the device type (block or character) and the major and
minor numbers. For example, let's say you have accidentally deleted /dev/
ttyS0 (COM1 under Windows), it can be recreated using the following command

# mknod ttyS0 c 4 64

For those of us who are rather lazy you can simply run the MAKEDEV script as
such

# MAKEDEV *

which will create all devices known.

If is possible that /dev may also contain a MAKEDEV.local for the creation of
any local device files.

In general and as required by the FSSTND, MAKEDEV will have provisions for
creating any device that may be found on the system, not just those that a
particular implementation installs.

For those of you who are wondering why Linux is using such a primitive system
to reference devices its because we haven't been able to devise a
sufficiently sophisticated mechanism which provides enough advantages over
the current system in order to achieve widespread adoption.

To date (as of kernel version 2.4), the best attempt has been made by Richard
Gooch of the CSIRO. It's called devfsd and has been a part of the kernel for
a number of years now. It has been sanctioned by the kernel developers and
Linus himself and details of its implementation can be found at /usr/src/
linux/Documentation/filesystems/devfs/README. Below is an excerpt from this
document.

Devfs is an alternative to "real" character and block special devices on your
root filesystem. Kernel device drivers can register devices by name rather
than major and minor numbers. These devices will appear in devfs
automatically, with whatever default ownership and protection the driver
specified. A daemon (devfsd) can be used to override these defaults. Devfs
has been in the kernel since 2.3.46.

NOTE that devfs is entirely optional. If you prefer the old disc-based device
nodes, then simply leave CONFIG_DEVFS_FS=n (the default). In this case,
nothing will change. ALSO NOTE that if you do enable devfs, the defaults are
such that full compatibility is maintained with the old devices names.

There are two aspects to devfs: one is the underlying device namespace, which
is a namespace just like any mounted filesystem. The other aspect is the
filesystem code which provides a view of the device namespace. The reason I
make a distinction is because devfs can be mounted many times, with each
mount showing the same device namespace. Changes made are global to all
mounted devfs filesystems. Also, because the devfs namespace exists without
any devfs mounts, you can easily mount the root filesystem by referring to an
entry in the devfs namespace.

The cost of devfs is a small increase in kernel code size and memory usage.
About 7 pages of code (some of that in __init sections) and 72 bytes for each
entry in the namespace. A modest system has only a couple of hundred device
entries, so this costs a few more pages. Compare this with the suggestion to
put /dev on a ramdisc.

On a typical machine, the cost is under 0.2 percent. On a modest system with
64 MBytes of RAM, the cost is under 0.1 percent. The accusations of
"bloatware" levelled at devfs are not justified.

As of kernel version 2.6, devfs has been marked obsolete and has now been
replaced by udev. A system very similar (at least from a the end user's point
of view) to devfs but which works entirely in userspace. An overview of udev
can be found at [http://www.kroah.com/linux/talks/ols_2003_udev_paper/
Reprint-Kroah-Hartman-OLS2003.pdf] http://www.kroah.com/linux/talks/
ols_2003_udev_paper/Reprint-Kroah-Hartman-OLS2003.pdf
-----------------------------------------------------------------------------

1.6. /etc

This is the nerve center of your system, it contains all system related
configuration files in here or in its sub-directories. A "configuration file"
is defined as a local file used to control the operation of a program; it
must be static and cannot be an executable binary. For this reason, it's a
good idea to backup this directory regularly. It will definitely save you a
lot of re-configuration later if you re-install or lose your current
installation. Normally, no binaries should be or are located here.

/etc/X11/
    This directory tree contains all the configuration files for the X Window
    System. Users should note that many of the files located in this
    directory are actually symbolic links to the /usr/X11R6 directory tree.
    Thus, the presence of these files in these locations can not be certain.

/etc/X11/XF86Config, /etc/X11/XF86Config-4
    The 'X' configuration file. Most modern distributions possess hardware
    autodetection systems that enable automatic creation of a valid file.
    Should autodetection fail a configuration file can also be created
    manually provided that you have sufficient knowledge about your system.
    It would be considered prudent not to attempt to type out a file from
    beginning to end. Rather, use common configuration utilities such as
    xf86config, XF86Setup and xf86cfg to create a workable template. Then,
    using suitable documentation commence optimization through intuition and/
    or trial and error. Options that can be configured via this file include
    X modules to be loaded on startup, keyboard, mouse, monitor and graphic
    chipset type. Often, commercial distributions will include their own X
    configuration utilities such as XDrake on Mandrake and also
    Xconfiguration on Redhat. Below is a sample X configuration file from the
    reference system

    ### BEGIN DEBCONF SECTION
    # XF86Config-4 (XFree86 server configuration file) generated by dexconf, the
    # Debian X Configuration tool, using values from the debconf database.
    #
    # Edit this file with caution, and see the XF86Config-4 manual page.
    # (Type "man XF86Config-4" at the shell prompt.)
    #
    # If you want your changes to this file preserved by dexconf, only
    # make changes
    # before the "### BEGIN DEBCONF SECTION" line above, and/or after the
    # "### END DEBCONF SECTION" line below.
    #
    # To change things within the debconf section, run the command:
    #   dpkg-reconfigure xserver-xfree86
    # as root.  Also see "How do I add custom sections to a dexconf-
    # generated
    # XF86Config or XF86Config-4 file?" in /usr/share/doc/xfree86-
    # common/FAQ.gz.

    Section "Files"
            FontPath        "unix/:7100"
    # local font server
            # if the local font server has problems,
    # we can fall back on these
            FontPath        "/usr/lib/X11/fonts/misc"
            FontPath        "/usr/lib/X11/fonts/cyrillic"
            FontPath        "/usr/lib/X11/fonts/100dpi/:unscaled"
            FontPath        "/usr/lib/X11/fonts/75dpi/:unscaled"
            FontPath        "/usr/lib/X11/fonts/Type1"
            FontPath        "/usr/lib/X11/fonts/Speedo"
            FontPath        "/usr/lib/X11/fonts/100dpi"
            FontPath        "/usr/lib/X11/fonts/75dpi"
    EndSection

    Section "Module"
            Load        "GLcore"
            Load        "bitmap"
            Load        "dbe"
            Load        "ddc"
            Load        "dri"
            Load        "extmod"
            Load        "freetype"
            Load        "glx"
            Load        "int10"
            Load        "pex5"
            Load        "record"
            Load        "speedo"
            Load        "type1"
            Load        "vbe"
            Load        "xie"
    EndSection

    Section "InputDevice"
            Identifier        "Generic Keyboard"
            Driver                "keyboard"
            Option                "CoreKeyboard"
            Option                "XkbRules"        "xfree86"
            Option                "XkbModel"        "pc104"
            Option                "XkbLayout"        "us"
    EndSection

    Section "InputDevice"
            Identifier        "Configured Mouse"
            Driver                "mouse"
            Option                "CorePointer"
            Option                "Device"                "/dev/psaux"
            Option                "Protocol"                "NetMousePS/2"
            Option                "Emulate3Buttons"        "true"
            Option                "ZAxisMapping"                "4 5"
    EndSection

    Section "InputDevice"
            Identifier        "Generic Mouse"
            Driver                "mouse"
            Option                "SendCoreEvents"        "true"
            Option                "Device"                "/dev/input/mice"
            Option                "Protocol"                "ImPS/2"
            Option                "Emulate3Buttons"        "true"
            Option                "ZAxisMapping"                "4 5"
    EndSection

    Section "Device"
            Identifier        "Generic Video Card"
            Driver                "nv"
    #        Option                "UseFBDev"                "true"
            Option                "UseFBDev"                "false"
    EndSection

    Section "Monitor"
            Identifier        "Generic Monitor"
            HorizSync        30-38
            VertRefresh        43-95
            Option                "DPMS"
    EndSection

    Section "Screen"
            Identifier        "Default Screen"
            Device                "Generic Video Card"
            Monitor                "Generic Monitor"
            DefaultDepth        16
            SubSection "Display"
                    Depth                1
                    Modes                "800x600" "640x480"
            EndSubSection
            SubSection "Display"
                    Depth                4
                    Modes                "800x600" "640x480"
            EndSubSection
            SubSection "Display"
                    Depth                8
                    Modes                "800x600" "640x480"
            EndSubSection
            SubSection "Display"
                    Depth                15
                    Modes                "800x600" "640x480"
            EndSubSection
            SubSection "Display"
                    Depth                16
                    Modes                "800x600" "640x480"
            EndSubSection
            SubSection "Display"
                    Depth                24
                    Modes                "800x600" "640x480"
            EndSubSection
    EndSection

    Section "ServerLayout"
            Identifier        "Default Layout"
            Screen                "Default Screen"
            InputDevice        "Generic Keyboard"
            InputDevice        "Configured Mouse"
            InputDevice        "Generic Mouse"
    EndSection

    Section "DRI"
            Mode        0666
    EndSection

    ### END DEBCONF SECTION

    As you can see, the layout of the file is quite simple and tends to be
    quite standard across most distributions. At the top are the locations of
    the various font files for X (note - X will not start if you do not
    specify a valid font), next is the "Modules" section. It details what
    modules are to be loaded upon startup. The most well known extensions are
    probably GLX (required for 3D rendering of graphics and games) and
    Xinerama which allows users to expand their desktop over several
    monitors. Next are the various "Device" sections which describe the type
    of hardware you have. Improper configuration of these subsections can
    lead to heartache and trauma with seemingly misplaced keys, bewitched
    mice and also constant flashing as X attempts to restart in a sometimes
    never ending loop. In most cases when all else fails the vesa driver
    seems to be able to initialise most modern video cards. In the "Screen"
    section it is possible to alter the default startup resolution and depth.
    Quite often it is possible to alter these attributes on the fly by using
    the alt-ctrl-+ or alt-ctrl- set of keystrokes. Lastly are the
    "ServerLayout" and "DRI" sections. Users will almost never touch the
    "DRI" section and only those who wish to utilise the Xinerama extensions
    of X will require having to change any of the ServerLayout options.

/etc/X11/Xmodmap
    In general your default keyboard mapping comes from your X server setup.
    If this setup is insufficient and you are unwilling to go through the
    process of reconfiguration and/or you are not the superuser you'll need
    to use the xmodmap program. This is the utility's global configuration
    file.

/etc/X11/xkb/
    The various symbols, types, geometries of keymaps that the X server
    supports can be found in this directory tree.

/etc/X11/lbxproxy/
    Low Bandwidth X (LBX) proxy server configuration files. Applications that
    would like to take advantage of the Low Bandwidth extension to X (LBX)
    must make their connections to an lbxproxy. These applications need know
    nothing about LBX, they simply connect to the lbxproxy as if it were a
    regular X server. The lbxproxy accepts client connections, multiplexes
    them over a single connection to the X server, and performs various
    optimizations on the X protocol to make it faster over low bandwidth and/
    or high latency connections. It should be noted that such compression
    will not increase the pace of rendering all that much. Its primary
    purpose is to reduce network load and thus increase overall network
    latency. A competing project called DXPC (Differential X Protocol
    Compression) has been found to be more efficient at this task. Studies
    have shown though that in almost all cases ssh tunneling of X will
    produce far better results than through any of these specialised pieces
    of software.

/etc/X11/proxymngr/
    X proxy services manager initialisation files. proxymngr is responsible
    for resolving requests from xfindproxy (in the xbase-clients package) and
    other similar clients, starting new proxies when appropriate, and keeping
    track of all the available proxy services.

/etc/X11/xdm/
    X display manager configuration files. xdm manages a collection of X
    servers, which may be on the local host or remote machines. It provides
    services similar to those provided by init, getty, and login on
    character-based terminals: prompting for login name and password,
    authenticating the user, and running a session. xdm supports XDMCP (X
    Display Manager Control Protocol) and can also be used to run a chooser
    process which presents the user with a menu of possible hosts that offer
    XDMCP display management. If the xutils package is installed, xdm can use
    the sessreg utility to register login sessions to the system utmp file;
    this, however, is not necessary for xdm to function.

/etc/X11/xdm/xdm-config
    This is the master 'xdm' configuration file. It determines where all
    other 'xdm' configuration files will be located. It is almost certain to
    be left undisturbed.

/etc/X11/gdm/
    GNOME Display Manager configuration files. gdm provides the equivalent of
    a "login:" prompt for X displays- it pops up a login window and starts an
    X session. It provides all the functionality of xdm, including XDMCP
    support for managing remote displays. The greeting window is written
    using the GNOME libraries and hence looks like a GNOME application- even
    to the extent of supporting themes! By default, the greeter is run as an
    unprivileged user for security.

/etc/X11/gdm/gdm.conf
    This is the primary configuration file for GDM. Through it, users can
    specify whether they would like their system to automatically login as a
    certain user, background startup image and also if they would like to run
    their machine as somewhat of a terminal server by using the XDMCP
    protocol.

/etc/X11/fonts
    Home of xfs fonts.

/etc/X11/fs/
    X font server configuration files. xfs is a daemon that listens on a
    network port and serves X fonts to X servers (and thus to X clients). All
    X servers have the ability to serve locally installed fonts for
    themselves, but xfs makes it possible to offload that job from the X
    server, and/or have a central repository of fonts on a networked machine
    running xfs so that all the machines running X servers on a network do
    not require their own set of fonts. xfs may also be invoked by users to,
