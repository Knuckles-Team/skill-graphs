      po::powerokwait:/etc/init.d/powerfail stop
      # /sbin/getty invocations for the runlevels.
      #
      # The "id" field MUST be the same as the last
      # characters of the device (after "tty").
      #
      # Format:
      # <id>:<runlevels>:<action>:<process>
      #
      # Note that on most Debian systems tty7 is used by the X Window System,
      # so if you want to add more getty's go ahead but skip tty7 if you run X.
      #
      1:2345:respawn:/sbin/getty 38400 tty1 2:23:respawn:/sbin/getty 38400 tty2
      3:23:respawn:/sbin/getty 38400 tty3 4:23:respawn:/sbin/getty 38400 tty4
      5:23:respawn:/sbin/getty 38400 tty5 6:23:respawn:/sbin/getty 38400 tty6
      # Example how to put a getty on a serial line (for a terminal)
      #
      #T0:23:respawn:/sbin/getty -L ttyS0 9600 vt100
      #T1:23:respawn:/sbin/getty -L ttyS1 9600 vt100
      # Example how to put a getty on a modem line.
      #
      #T3:23:respawn:/sbin/mgetty -x0 -s 57600 ttyS3

      Undocumented features

      The letters A-C can be used to spawn a daemon listed in /etc/inittab. For
      example, assuming you want to start getty on a port to receive a call, but
      only after receiving a voice call first (and not all the time). Furthermore,
      you want to be able to receive a data or a fax call and that when you get
      the voice message you'll know which you want. You insert two new lines
      in /etc/inittab, each with its own ID, and each with a runlevel such as A
      for data and B for fax. When you know which you need, you simply spawn the
      appropriate daemon by calling 'telinit A' or 'telinit B'.
      The appropriate getty is put on the line until the first call is received.
      When the caller terminates the connection, the getty drops because, by
      definition, on demand will not respawn. The other two letters, S and Q, are
      special. S brings you system to maintenance mode and is the same as changing
      state to runlevel 1. The Q is used to tell init to reread inittab. The
      /etc/inittab file can be changed as often as required, but will only be read
      under certain circumstances: -One of its processes dies (do you need to
      respawn another?) -On a powerful signal from a power daemon (or a command
      line) -When told to change state by telinit The Q argument tells init to
      reread the /etc/inittab file. Even though it is called the System V runlevel
      system runlevels 7-9 are legitimate runlevels that can be used if necessary.
      The administrator must remember to alter the inittab file though and also to
      create the required rc?.d files.

/etc/inputrc
    Global inputrc for libreadline. Readline is a function that gets a line
    from a user and automatically edits it.

/etc/isapnp.conf
    Configuration file for ISA based cards. This standard is virtually
    redundant in new systems. The 'isapnptools' suite of ISA Plug-And-Play
    configuration utilities is used to configure such devices. These programs
    are suitable for all systems, whether or not they include a PnP BIOS. In
    fact, PnP BIOS adds some complications because it may already activate
    some cards so that the drivers can find them, and these tools can
    unconfigure them, or change their settings causing all sorts of nasty
    effects.

/etc/isdn
    ISDN configuration files.

/etc/issue
    Output by getty before the login prompt. Usually contains a short
    description or welcoming message to the system. The contents are up to
    the system administrator. Debian GNU/\s 3.0 \n \l

/etc/issue.net
    Presents the welcome screen to users who login remotely to your machine
    (whereas /etc/issue determines what a local user sees on login). Debian
    GNU/%s 3.0 %h

/etc/kde
    KDE initialization scripts and KDM configuration.

/etc/kde/kdm
    Location for the K Desktop Manager files. kdm manages a collection of X
    servers, which may be on the local host or remote machines. It provides
    services similar to those provided by init, getty, and login on
    character-based terminals: prompting for login name and password,
    authenticating the user, and running a session. kdm supports XDMCP (X
    Display Manager Control Protocol) and can also be used to run a chooser
    process which presents the user with a menu of possible hosts that offer
    XDMCP display management.

/etc/kderc
    System wide KDE initialization script. Commands here executed every time
    the KDE environment is loaded. It's a link to /etc/kde2/system.kdeglobals


          [Directories]
          dir_config=/etc/kde2
          dir_html=/usr/share/doc/kde/HTML
          dir_cgi=/usr/lib/cgi-bin
          dir_apps=/usr/share/applnk
          dir_mime=/usr/share/mimelnk
          dir_services=/usr/share/services
          dir_servicetypes=/usr/share/servicetypes
          [General]
          TerminalApplication=x-terminal-emulator




/etc/ld.so.conf, /etc/ld.so.cache



        /etc/ld.so.conf is a file containing a list of colon, space, tab,
        newline, or comma separated directories in which to search for
        libraries. /etc/ld.so.cache containing an ordered list of libraries
        found in the directories specified in /etc/ld.so.conf. This file is
        not in human readable format, and is not intended to be edited.


        'ldconfig' creates the necessary links and cache (for use by the
        run-time linker, ld.so) to the most recent shared libraries found in
        the directories specified on the command line, in the file /etc/
        ld.so.conf, and in the trusted directories (/usr/lib and /lib).
        'ldconfig' checks the header and file names of the libraries it
        encounters when determining which versions should have their links
        updated. ldconfig ignores symbolic links when scanning for libraries.


        'ldconfig' will attempt to deduce the type of ELF libs (ie. libc5 or
        libc6/glibc) based on what C libs if any the library was linked
        against, therefore when making dynamic libraries, it is wise to
        explicitly link against libc (use -lc).


        Some existing libs do not contain enough information to allow the
        deduction of their type, therefore the /etc/ld.so.conf file format
        allows the specification of an expected type. This is only used for
        those ELF libs which we can not work out. The format is like this
        "dirname=TYPE", where type can be libc4, libc5 or libc6. (This syntax
        also works on the command line). Spaces are not allowed. Also see the
        -p option.


        Directory names containing an = are no longer legal unless they also
        have an expected type specifier.


        'ldconfig' should normally be run by the super-user as it may require
        write permission on some root owned directories and files. It is
        normally run automatically at bootup or manually whenever new shared
        libraries are installed.



/usr/X11R6/lib
    X libraries.

/usr/local/lib
    Local libraries.

/etc/lilo.conf
    Configuration file for the Linux boot loader 'lilo'. 'lilo' is the
    original OS loader and can load Linux and others. The 'lilo' package
    normally contains lilo (the installer) and boot-record-images to install
    Linux, OS/2, DOS and generic Boot Sectors of other Oses. You can use Lilo
    to manage your Master Boot Record (with a simple text screen, text menu
    or colorful splash graphics) or call 'lilo' from other boot-loaders to
    jump-start the Linux kernel.


          Prompt #Prompt user to select
          OS choice at boot timeout=300  # Amount of time to wait before default OS
                                         # started (in ms)
          default=Debian4 #Default OS to be loaded
          vga=normal #VGA mode
          boot=/dev/had #location of MBR
          map=/boot/map #location of kernel
          install=/boot/boot-bmp.b #File to be installed as boot sector
          bitmap=/boot/debian.bmp #LILO boot image
          bmp-table=30p,100p,1,10 #Colours
          selectable bmp-colors=13,,0,1,,0 #Colours chosen
          lba32 #Required on most new systems to overcome
                #1024 cylinder problem
          image=/vmlinuz #name of kernel
          image label=Debian #a label
          read-only #file system to be mounted read only
          root=/dev/hda6 #location of root filesystem

          image=/boot/bzImage
          label=Debian4
          read-only
          root=/dev/hda6

          image=/mnt/redhat/boot/vmlinuz
          label=Redhat
          initrd=/mnt/redhat/boot/initrd-2.4.18-14.img
          read-only
          root=/dev/hda5
          vga=788
          append=" hdc=ide-scsi hdd=ide-scsi"

          image=/mnt/mandrake/boot/vmlinuz
          label="Mandrake"
          root=/dev/hda7
          initrd=/mnt/mandrake/boot/initrd.img
          append="devfs=mount hdc=ide-scsi
          acpi=off quiet"
          vga=788
          read-only

          other=/dev/hda2
          table=/dev/had
          loader=/boot/chain.b
          label=FBSD
          other=/dev/hda1
          label=Windows
          table=/dev/had

          other=/dev/fd0
          label=floppy unsafe




/etc/local.gen
    This file lists locales that you wish to have built. You can find a list
    of valid supported locales at /usr/share/i18n/SUPPORTED. Other
    combinations are possible, but may not be well tested. If you change this
    file, you need to re-run locale-gen.

/etc/locale.alias
    Locale name alias data base.

/etc/login.defs
    Configuration control definitions for the login package. An inordinate
    number of attributes can be altered via this single file such as the
    location of mail, delay in seconds after a failed login, enabling display
    of fail log information, display of unknown username login failures,
    shell environment variables, etc....

/etc/logrotate.conf
    The logrotate utility is designed to simplify the administration of log
    files on a system which generates a lot of log files. Logrotate allows
    for the automatic rotation compression, removal and mailing of log files.
    Logrotate can be set to handle a log file daily, weekly, monthly or when
    the log file gets to a certain size. Normally, logrotate runs as a daily
    cron job.

      # see "man logrotate" for details
      # rotate log files weekly
      weekly

      # keep 4 weeks worth of backlogs
      rotate 4

      # create new (empty) log files after rotating old ones
      create

      # uncomment this if you want your log files compressed
      #compress

      # packages drop log rotation information into this directory
      include /etc/logrotate.d

      # no packages own wtmp, or btmp -- we'll rotate them here
      /var/log/wtmp {
          monthly
          create 0664 root utmp
          rotate 1
      }

      /var/log/btmp {
          missingok
          monthly
          create 0664 root utmp
          rotate 1
      }

      # system-specific logs may be configured here

/etc/ltrace.conf
    Configuration file for ltrace (Library Call Tracer). It tracks runtime
    library calls in dynamically linked programs. 'ltrace' is a debugging
    program which runs a specified command until it exits. While the command
    is executing, ltrace intercepts and records the dynamic library calls
    which are called by the executed process and the signals received by that
    process. It can also intercept and print the system calls executed by the
    program. The program to be traced need not be recompiled for this, so you
    can use it on binaries for which you don't have the source handy. You
    should install ltrace if you need a sysadmin tool for tracking the
    execution of processes.

/etc/magic
    Magic local data and configuration file for the file(1) command. Contains
    the descriptions of various file formats based on which file guesses the
    type of the file. Insert here your local magic data. Format is described
    in magic(5).

/etc/mail.rc
    Initialization file for 'mail'. 'mail' is an intelligent mail processing
    system which has a command syntax reminiscent of ed with lines replaced
    by messages. It's basically a command line version of Microsoft Outlook.

/etc/mailcap
    'metamail' capabilities file. The mailcap file is read by the metamail
    program to determine how to display non-text at the local site. The
    syntax of a mailcap file is quite simple, at least compared to termcap
    files. Any line that starts with "#" is a comment. Blank lines are
    ignored. Otherwise, each line defines a single mailcap entry for a single
    content type. Long lines may be continued by ending them with a backslash
    character, \. Each individual mailcap entry consists of a content-type
    specification, a command to execute, and (possibly) a set of optional
    "flag" values.

/etc/mailcap.order
    The mailcap ordering specifications. The order of entries in the /etc/
    mailcap file can be altered by editing the /etc/mailcap.order file. Each
    line of that file specifies a package and an optional mime type. Mailcap
    entries that match will be placed in the order of this file. Entries that
    don't match will be placed later.

/etc/mailname
    Mail server hostname. Normally the same as the hostname.

/etc/menu, /etc/menu-methods
    The menu package was inspired by the install-fvwm2-menu program from the
    old fvwm2 package. However, menu tries to provide a more general
    interface for menu building. With the update-menus command from this
    package, no package needs to be modified for every X window manager
    again, and it provides a unified interface for both text-and X-oriented
    programs.

    When a package that wants to add something to the menu tree gets
    installed, it will run update-menus in its postinstall script.
    Update-menus then reads in all menu files in /etc/menu/ /usr/lib/menu and
    /usr/lib/menu/default, and stores the menu entries of all installed
    packages in memory. Once that has been done, it will run the menu-methods
    in /etc/menu-methods/*, and pipe the information about the menu entries
    to the menu-methods on stdout, so that the menu-methods can read this.
    Each Window Manager or other program that wants to have the debian menu
    tree, will supply a menu-method script in /etc/menu-methods/. This
    menu-method then knows how to generate the startup-file for that window
    manager. To facilitate this task for the window-manager maintainers, menu
    provides a install-menu program. This program can generate the startup
    files for just about every window manager.

/etc/mgetty+sendfax
    Configuration files for use of mgetty as the interface on the serial
    port. The mgetty routine special routine has special features for
    handling things such as dial up connections and fax connections.

/etc/mime.types
    MIME-TYPES and the extensions that represent them. This file is part of
    the "mime-support" package. Note: Compression schemes like "gzip",
    "bzip", and "compress" are not actually "mime-types". They are
    "encodings" and hence must _not_ have entries in this file to map their
    extensions. The "mime-type" of an encoded file refers to the type of data
    that has been encoded, not the type of the encoding.

/etc/minicom
    'minicom' configuration files. 'minicom' is a communication program which
    somewhat resembles the shareware program TELIX but is free with source
    code and runs under most unices. Features include dialling directory with
    auto-redial, support for UUCP-style lock files on serial devices, a
    separate script language interpreter, capture to file, multiple users
    with individual configurations, and more.

/etc/modules
    List of modules to be loaded at startup.

      # /etc/modules: kernel modules to load at boot time.
      #
      # This file should contain the names of kernel modules that are
      # to be loaded at boot time, one per line. Comments begin with
      # a "#", and everything on the line after them are ignored.
      unix
      af_packet
      via-rhine
      cmpci
      ne2k-pci
      nvidia


/etc/modules.conf
      ### This file is automatically generated by update-modules"
      #
      # Please do not edit this file directly. If you want to change or add
      # anything please take a look at the files in /etc/modutils and read
      # the manpage for update-modules.
      #
      ### update-modules: start processing /etc/modutils/0keep
      # DO NOT MODIFY THIS FILE!
      # This file is not marked as conffile to make sure if you upgrade modutils
      # it will be restored in case some modifications have been made.
      #
      # The keep command is necessary to prevent insmod and friends from ignoring
      # the builtin defaults of a path-statement is encountered. Until all other
      # packages use the new `add path'-statement this keep-statement is essential
      # to keep your system working
      keep

      ### update-modules: end processing /etc/modutils/0keep

      ### update-modules: start processing /etc/modutils/actions
      # Special actions that are needed for some modules

      # The BTTV module does not load the tuner module automatically,
      # so do that in here
      post-install bttv insmod tuner
      post-remove bttv rmmod tuner


      ### update-modules: end processing /etc/modutils/actions
