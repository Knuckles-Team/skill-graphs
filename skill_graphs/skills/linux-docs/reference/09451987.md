      ### update-modules: start processing /etc/modutils/aliases
      # Aliases to tell insmod/modprobe which modules to use

      # Uncomment the network protocols you don't want loaded:
      # alias net-pf-1 off          # Unix
      # alias net-pf-2 off          # IPv4
      # alias net-pf-3 off          # Amateur Radio AX.25
      # alias net-pf-4 off          # IPX
      # alias net-pf-5 off          # DDP / appletalk
      # alias net-pf-6 off          # Amateur Radio NET/ROM
      # alias net-pf-9 off          # X.25
      # alias net-pf-10 off         # IPv6
      # alias net-pf-11 off         # ROSE / Amateur Radio X.25 PLP
      # alias net-pf-19 off         # Acorn Econet

      alias char-major-10-175       agpgart
      alias char-major-10-200       tun
      alias char-major-81   bttv
      alias char-major-108  ppp_generic
      alias /dev/ppp                ppp_generic
      alias tty-ldisc-3     ppp_async
      alias tty-ldisc-14    ppp_synctty
      alias ppp-compress-21 bsd_comp
      alias ppp-compress-24 ppp_deflate
      alias ppp-compress-26 ppp_deflate

      # Crypto modules (see http://www.kerneli.org/)
      alias loop-xfer-gen-0 loop_gen
      alias loop-xfer-3     loop_fish2
      alias loop-xfer-gen-10        loop_gen
      alias cipher-2                des
      alias cipher-3                fish2
      alias cipher-4                blowfish
      alias cipher-6                idea
      alias cipher-7                serp6f
      alias cipher-8                mars6
      alias cipher-11               rc62
      alias cipher-15               dfc2
      alias cipher-16               rijndael
      alias cipher-17               rc5


      ### update-modules: end processing /etc/modutils/aliases

      ### update-modules: start processing /etc/modutils/ltmodem-2.4.18
      # lt_drivers: autoloading and insertion parameter usage
      alias char-major-62 lt_serial
      alias /dev/tts/LT0  lt_serial
      alias /dev/modem lt_serial
      # options lt_modem vendor_id=0x115d device_id=0x0420 Forced=3,0x130,0x2f8
      # section for lt_drivers ends

      ### update-modules: end processing /etc/modutils/ltmodem-2.4.18

      ### update-modules: start processing /etc/modutils/paths
      # This file contains a list of paths that modprobe should scan,
      # beside the once that are compiled into the modutils tools
      # themselves.


      ### update-modules: end processing /etc/modutils/paths

      ### update-modules: start processing /etc/modutils/ppp
      alias /dev/ppp          ppp_generic
      alias char-major-108    ppp_generic
      alias tty-ldisc-3       ppp_async
      alias tty-ldisc-14      ppp_synctty
      alias ppp-compress-21   bsd_comp
      alias ppp-compress-24   ppp_deflate
      alias ppp-compress-26   ppp_deflate

      ### update-modules: end processing /etc/modutils/ppp

      ### update-modules: start processing /etc/modutils/setserial
      #
      # This is what I wanted to do, but logger is in /usr/bin, which isn't
      # loaded when the module is first loaded into the kernel at boot time!
      #
      #post-install serial /etc/init.d/setserial start |
      #logger -p daemon.info -t "setserial-module reload"
      #pre-remove serial /etc/init.d/setserial stop |
      #logger -p daemon.info -t "setserial-module uload"
      #
      alias /dev/tts          serial
      alias /dev/tts/0        serial
      alias /dev/tts/1        serial
      alias /dev/tts/2        serial
      alias /dev/tts/3        serial
      post-install serial /etc/init.d/setserial modload > /dev/null 2> /dev/null
      pre-remove serial /etc/init.d/setserial modsave  > /dev/null 2> /dev/null

      ### update-modules: end processing /etc/modutils/setserial

      ### update-modules: start processing /etc/modutils/arch/i386
      alias parport_lowlevel parport_pc
      alias char-major-10-144 nvram
      alias binfmt-0064 binfmt_aout
      alias char-major-10-135 rtc

      ### update-modules: end processing /etc/modutils/arch/i386


/etc/modutils
    These utilities are intended to make a Linux modular kernel manageable
    for all users, administrators and distribution maintainers.

/etc/mtools
    Debian default mtools configuration file. The mtools series of commands
    work with MS-DOS files and directories on floppy disks. This allows you
    to use Linux with MS-DOS formatted diskettes on DOS and Windows systems.

/etc/manpath.conf
    This file is used by the man_db package to configure the man and cat
    paths. It is also used to provide a manpath for those without one by
    examining their PATH environment variable. For details see the manpath(5)
    man page.

/etc/mediaprm
    Was formally named /etc/fdprm. See /etc/fdprm for further details.

/etc/motd
    The message of the day, automatically output after a successful login.
    Contents are up to the system administrator. Often used for getting
    information to every user, such as warnings about planned downtimes.
    Linux debian.localdomain.com 2.4.18 #1 Sat Mar 15 00:17:39 EST 2003 i686
    unknown Most of the programs included with the Debian GNU/Linux system
    are freely redistributable; the exact distribution terms for each program
    are described in the individual files in /usr/share/doc/*/copyright
    Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
    permitted by applicable law.

/etc/mtab
    List of currently mounted filesystems. Initially set up by the bootup
    scripts, and updated automatically by the mount command. Used when a list
    of mounted filesystems is needed, e.g., by the df command. This file is
    sometimes a symbolic link to /proc/mounts.

/etc/networks
    List of networks that the system is currently located on. For example,
    192.168.0.0.

/etc/nsswitch.conf
    System Database/Name Service Switch configuration file.

/etc/oss.conf
    OSS (Open Sound System) configuration file.

/etc/pam.d/
    This directory is the home of the configuration files for PAMs, Pluggable
    Authentication Modules.

/etc/postfix/
    Holds your postfix configuration files. Postfix is now the MTA of choice
    among Linux distributions. It is sendmail-compatible, offers improved
    speed over sendmail, ease of administration and security. It was
    originally developed by IBM and was called the IBM Secure Mailer and is
    used in many large commercial networks. It is now the de-facto standard.

/etc/ppp/
    The place where your dial-up configuration files are placed. More than
    likely to be created by the text menu based pppconfig or other GUI based
    ppp configuration utilities such as kppp or gnome-ppp.

/etc/pam.conf
    Most programs use a file under the /etc/pam.d/ directory to setup their
    PAM service modules. This file is and can be used, but is not
    recommended.

/etc/paper.config
    Paper size configuration file.

/etc/papersize
    Default papersize.

/etc/passwd
    This is the 'old' password file, It is kept for compatibility and
    contains the user database, with fields giving the username, real name,
    home directory, encrypted password, and other information about each
    user. The format is documented in the passwd man(ual) page.

    root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/bin/sh
    bin:x:2:2:bin:/bin:/bin/sh sys:x:3:3:sys:/dev:/bin/sh
    sync:x:4:100:sync:/bin:/bin/sync games:x:5:100:games:/usr/games:/bin/sh
    man:x:6:100:man:/var/cache/man:/bin/sh lp:x:7:7:lp:/var/spool/lpd:/bin/sh
    mail:x:8:8:mail:/var/mail:/bin/sh news:x:9:9:news:/var/spool/news:/bin/sh
    uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh proxy:x:13:13:proxy:/bin:/bin/sh
    postgres:x:31:32:postgres:/var/lib/postgres:/bin/sh
    www-data:x:33:33:www-data:/var/www:/bin/sh
    backup:x:34:34:backup:/var/backups:/bin/sh
    operator:x:37:37:Operator:/var:/bin/sh
    list:x:38:38:SmartList:/var/list:/bin/sh irc:x:39:39:ircd:/var:/bin/sh
    gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
    nobody:x:65534:65534:nobody:/home:/bin/sh
    binh:x:1000:1000:,,,:/home/binh:/bin/bash
    identd:x:100:65534::/var/run/identd:/bin/false
    sshd:x:101:65534::/var/run/sshd:/bin/false gdm:x:102:101:Gnome Display
    Manager:/var/lib/gdm:/bin/false
    telnetd:x:103:103::/usr/lib/telnetd:/bin/false
    dummy:x:1001:1001:,,,:/home/dummy:/bin/bash

/etc/passwd-
    Old /etc/passwd file.

/etc/printcap
    Printer configuration (capabilities) file. The definition of all system
    printers, whether local or remote, is stored in this file. Its layout is
    similar to that of /etc/termcap but it uses a different syntax.

/etc/profile
    Files and commands to be executed at login or startup time by the Bourne
    or C shells. These allow the system administrator to set global defaults
    for all users.

/etc/profile.d
    Shells scripts to be executed upon login to the Bourne or C shells. These
    scripts are normally called from the /etc/profile file.

/etc/protocols
    Protocols definitions file. It describes the various DARPA Internet
    protocols that are available from the TCP/IP subsystem. It should be
    consulted instead of using the numbers in the ARPA include files or
    resorting to guesstimation. This file should be left untouched since
    changes could result in incorrect IP packages.

/etc/pcmcia
    Configuration files for PCMCIA devices. Generally only useful to laptop
    users.

/etc/reportbug.conf
    Configuration file for reportbug. Reportbug is primarily designed to
    report bugs in the Debian distribution. By default it creates an e-mail
    to the Debian bug tracking system at mit@bugs.debian.org with information
    about the bug. Using the -bts option you can report bugs to other servers
    also using ddebbugs such as KDE.org. It is similar to bug but has far
    greater capabilities while still maintaining simplicity.

/etc/rc.boot or /etc/rc?.d
    These directories contain all the files necessary to control system
    services and configure runlevels. A skeleton file is provided in /etc/
    init.d/skeleton

/etc/rcS.d
    The scripts in this directory are executed once when booting the system,
    even when booting directly into single user mode. The files are all
    symbolic links, the real files are located in /etc/init.d/. For a more
    general discussion of this technique, see /etc/init.d/README.

/etc/resolv.conf
    Configuration of how DNS is to occur is defined in this file. It tells
    the name resolver libraries where they need to go to find information not
    found in the /etc/hosts file. This always has at least one nameserver
    line, but preferably three. The resolver uses each in turn. More than the
    first three can be included but anything beyond the first three will be
    ignored. Two lines that appear in the /etc/resolv.conf file are domain
    and search. Both of these are mutually exclusive options, and where both
    show up, the last one wins. Other entries beyond the three discussed here
    are listed in the man pages but aren't often used.

/etc/rmt
    This is not a mistake. This shell script (/etc/rmt) has been provided for
    compatibility with other Unix-like systems, some of which have utilities
    that expect to find (and execute) rmt in the /etc directory on remote
    systems.

/etc/rpc
    The rpc file contains user readable names that can be used in place of
    rpc program numbers. Each line has the following information: -name of
    server for the rpc program -rpc program number -aliases Items are
    separated by any number of blanks and/or tab characters. A ``#''
    indicates the beginning of a comment; characters up to the end of the
    line are not interpreted by routines which search the file.

      # /etc/rpc:
      # $Id: etc.xml,v 1.10 2004/02/03 21:42:57 binh Exp $
      #
      # rpc 88/08/01 4.0 RPCSRC; from 1.12   88/02/07 SMI

      portmapper    100000  portmap sunrpc
      rstatd                100001  rstat rstat_svc rup perfmeter
      rusersd               100002  rusers
      nfs           100003  nfsprog
      ypserv                100004  ypprog
      mountd                100005  mount showmount
      ypbind                100007
      walld         100008  rwall shutdown
      yppasswdd     100009  yppasswd
      etherstatd    100010  etherstat
      rquotad               100011  rquotaprog quota rquota
      sprayd                100012  spray
      3270_mapper   100013
      rje_mapper    100014
      selection_svc 100015  selnsvc
      database_svc  100016
      rexd          100017  rex
      alis          100018
      sched         100019
      llockmgr      100020
      nlockmgr      100021
      x25.inr               100022
      statmon               100023
      status                100024
      bootparam     100026
      ypupdated     100028  ypupdate
      keyserv               100029  keyserver
      tfsd          100037
      nsed          100038
      nsemntd               100039
      pcnfsd                150001
      amd           300019  amq
      sgi_fam               391002
      ugidd         545580417
      bwnfsd          788585389


/etc/samba
    Samba configuration files. A 'LanManager' like file and printer server
    for Unix. The Samba software suite is a collection of programs that
    implements the SMB protocol for unix systems, allowing you to serve files
    and printers to Windows, NT, OS/2 and DOS clients. This protocol is
    sometimes also referred to as the LanManager or NetBIOS protocol.

/etc/sane.d
    Sane configuration files. SANE stands for "Scanner Access Now Easy" and
    is an application programming interface (API) that provides standardized
    access to any raster image scanner hardware (flatbed scanner, hand-held
    scanner, video- and still-cameras, frame-grabbers, etc.). The SANE API is
    public domain and its discussion and development is open to everybody.
    The current source code is written for UNIX (including GNU/Linux) and is
    available under the GNU General Public License (the SANE API is available
    to proprietary applications and backends as well, however).

    SANE is a universal scanner interface. The value of such a universal
    interface is that it allows writing just one driver per image acquisition
    device rather than one driver for each device and application. So, if you
    have three applications and four devices, traditionally you'd have had to
    write 12 different programs. With SANE, this number is reduced to seven:
    the three applications plus the four drivers. Of course, the savings get
    even bigger as more and more drivers and/or applications are added.

    Not only does SANE reduce development time and code duplication, it also
    raises the level at which applications can work. As such, it will enable
    applications that were previously unheard of in the UNIX world. While
    SANE is primarily targeted at a UNIX environment, the standard has been
    carefully designed to make it possible to implement the API on virtually
    any hardware or operating system.

    While SANE is an acronym for ``Scanner Access Now Easy'' the hope is of
    course that SANE is indeed sane in the sense that it will allow easy
    implementation of the API while accommodating all features required by
    today's scanner hardware and applications. Specifically, SANE should be
    broad enough to accommodate devices such as scanners, digital still and
    video cameras, as well as virtual devices like image file filters.

    If you're familiar with TWAIN, you may wonder why there is a need for
    SANE. Simply put, TWAIN does not separate the user-interface from the
    driver of a device. This, unfortunately, makes it difficult, if not
    impossible, to provide network transparent access to image acquisition
    devices (which is useful if you have a LAN full of machines, but scanners
    connected to only one or two machines; it's obviously also useful for
    remote-controlled cameras and such). It also means that any particular
    TWAIN driver is pretty much married to a particular GUI API (be it Win32
    or the Mac API). In contrast, SANE cleanly separates device controls from
    their representation in a user-interface. As a result, SANE has no
    difficulty supporting command-line driven interfaces or
    network-transparent scanning. For these reasons, it is unlikely that
    there will ever be a SANE backend that can talk to a TWAIN driver. The
    converse is no problem though: it would be pretty straight forward to
    access SANE devices through a TWAIN source. In summary, if TWAIN had been
    just a little better designed, there would have been no reason for SANE
    to exist, but things being the way they are, TWAIN simply isn't SANE.

/etc/securetty
    Identifies secure terminals, i.e., the terminals from which root is
    allowed to log in. Typically only the virtual consoles are listed, so
    that it becomes impossible (or at least harder) to gain superuser
    privileges by breaking into a system over a modem or a network.



          # /etc/securetty: list of terminals on which root is allowed to login.
          # See securetty(5) and login(1).
          console

          # Standard consoles
          tty1
          tty2
          tty3
          tty4
          tty5
          tty6
          tty7
          tty8
          tty9
          tty10
          tty11
          tty12

          # Same as above, but these only occur with devfs devices
          vc/1
