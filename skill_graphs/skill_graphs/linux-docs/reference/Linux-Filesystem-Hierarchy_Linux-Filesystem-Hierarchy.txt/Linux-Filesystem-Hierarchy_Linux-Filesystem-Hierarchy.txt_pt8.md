          vc/2
          vc/3
          vc/4
          vc/5
          vc/6
          vc/7
          vc/8
          vc/9
          vc/10
          vc/11
          vc/12




/etc/sensors.conf
    Configuration file for libsensors. A set of libraries designed to
    ascertain current hardware states via motherboard sensor chips. Useful
    statistics such as core voltages, CPU temperature can be determined
    through third party utilities that make user of these libraries such as
    'gkrellm'. If you do not wish to install these packages you may also
    utilise the /proc filesystem real-time nature.

/etc/sudoers
    Sudoers file. This file must be edited with the 'visudo' command as root.
    The sudo command allows an authenticated user to execute an authorized
    command as root. Both the effective UID and GID are set to 0 (you are
    basically root). It determines which users are authorized and which
    commands they are authorized to use. Configuration of this command is via
    this file.

/etc/shadow
    Shadow password file on systems with shadow password software installed
    (PAMs). Shadow passwords move the encrypted password from /etc/passwd
    into /etc/shadow; the latter is not readable by anyone except root. This
    makes it more difficult to crack passwords.

/etc/shadow-
    Old /etc/shadow file.

/etc/sysctl.conf
    Configuration file for setting system variables, most notably kernel
    parameters. 'sysctl' is a means of configuring certain aspects of the
    kernel at run-time, and the /proc/sys/ directory is there so that you
    don't even need special tools to do it!

/etc/security
    Essential to security. This subdirectory allows administrators to impose
    quota limits, access limits and also to configure PAM environments.

/etc/serial.conf
    Serial port configuration. Changeable parameters include speed, baud
    rate, port, irq and type.

/etc/services
    A definition of the networks, services and the associated port for each
    protocol that are available on this system. For example, web services
    (http) are assigned to port 80 by default. # /etc/services: # $Id:
    etc.xml,v 1.10 2004/02/03 21:42:57 binh Exp $ # # Network services,
    Internet style # # Note that it is presently the policy of IANA to assign
    a single # well-known port number for both TCP and UDP; hence, most
    entries # here have two entries even if the protocol doesn't support UDP
    # operations. Updated from RFC 1700, ``Assigned Numbers'' (October #
    1994). Not all ports are included, only the more common ones. echo 7/tcp
    echo 7/udp discard 9/tcp sink null discard 9/udp sink null systat 11/tcp
    users daytime 13/tcp daytime 13/udp netstat 15/tcp qotd 17/tcp quote msp
    18/tcp # message send protocol msp 18/udp # message send protocol chargen
    19/tcp ttytst source chargen 19/udp ttytst source ftp-data 20/tcp ftp 21/
    tcp fsp 21/udp fspd ssh 22/tcp # SSH Remote Login Protocol ssh 22/udp #
    SSH Remote Login Protocol telnet 23/tcp # 24 - private smtp 25/tcp mail #
    26 - unassigned time 37/tcp timserver time 37/udp timserver rlp 39/udp
    resource # resource location nameserver 42/tcp name # IEN 116 whois 43/
    tcp nicname re-mail-ck 50/tcp # Remote Mail Checking Protocol re-mail-ck
    50/udp # Remote Mail Checking Protocol domain 53/tcp nameserver #
    name-domain server domain 53/udp nameserver netbios-ns 137/tcp # NETBIOS
    Name Service netbios-ns 137/udp netbios-dgm 138/tcp # NETBIOS Datagram
    Service netbios-dgm 138/udp netbios-ssn 139/tcp # NETBIOS session service
    netbios-ssn 139/udp x11 6000/tcp x11-0 # X windows system x11 6000/udp
    x11-0 # X windows system

/etc/shells
    Lists trusted shells. The chsh command allows users to change their login
    shell only to shells listed in this file. ftpd, the server process that
    provides FTP services for a machine, will check that the user's shell is
    listed in /etc/shells and will not let people log in unless the shell is
    listed there. There are also some display managers that will passively or
    actively (dependent upon on distribution and display manager being used)
    refuse a user access to the system unless their shell is one of those
    listed here.


          # /etc/shells: valid login shells
          /bin/ash
          /bin/bash
          /bin/csh
          /bin/sh
          /usr/bin/es
          /usr/bin/ksh
          /bin/ksh
          /usr/bin/rc
          /usr/bin/tcsh
          /bin/tcsh
          /usr/bin/zsh
          /bin/sash
          /bin/zsh
          /usr/bin/esh




/etc/skel/
    The default files for each new user are stored in this directory. Each
    time a new user is added, these skeleton files are copied into their home
    directory. An average system would have: .alias, .bash_profile, .bashrc
    and .cshrc files. Other files are left up to the system administrator.

/etc/sysconfig/
    This directory contains configuration files and subdirectories for the
    setup of system configuration specifics and for the boot process, like
    'clock', which sets the timezone, or 'keyboard' which controls the
    keyboard map. The contents may vary drastically depending on which
    distribution and what utilities you have installed. For example, on a
    Redhat or Mandrake based system it is possible to alter an endless array
    of attributes from the default desktop to whether DMA should be enabled
    for your IDE devices. On our Debian reference system though this folder
    is almost expedient containing only two files hwconf and soundcard which
    are both configured by the Redhat utilities hwconf and sndconfig
    respectively.

/etc/slip
    Configuration files for the setup and operation of SLIP (serial line IP)
    interface. Generally unused nowadays. This protocol has been superseded
    by the faster and more efficient PPP protocol.

/etc/screenrc
    This is the system wide screenrc. You can use this file to change the
    default behavior of screen system wide or copy it to ~/.screenrc and use
    it as a starting point for your own settings. Commands in this file are
    used to set options, bind screen functions to keys, redefine terminal
    capabilities, and to automatically establish one or more windows at the
    beginning of your screen session. This is not a comprehensive list of
    options, look at the screen manual for details on everything that you can
    put in this file.

/etc/scrollkeeper.conf
    A free electronic cataloging system for documentation. It stores metadata
    specified by the http://www.ibiblio.org/osrt/omf/ (Open Source Metadata
    Framework) as well as certain metadata extracted directly from documents
    (such as the table of contents). It provides various functionality
    pertaining to this metadata to help browsers, such as sorting the
    registered documents or searching the metadata for documents which
    satisfy a set of criteria.

/etc/ssh
    'ssh' configuration files. 'ssh' is a secure rlogin/rsh/rcp replacement
    (OpenSSH). This is the portable version of OpenSSH, a free implementation
    of the Secure Shell protocol as specified by the IETF secsh working
    group. 'ssh' (Secure Shell) is a program for logging into a remote
    machine and for executing commands on a remote machine. It provides
    secure encrypted communications between two untrusted hosts over an
    insecure network. X11 connections and arbitrary TCP/IP ports can also be
    forwarded over the secure channel. It is intended as a replacement for
    rlogin, rsh and rcp, and can be used to provide applications with a
    secure communication channel. It should be noted that in some countries,
    particularly Iraq, and Pakistan, it may be illegal to use any encryption
    at all without a special permit.

/etc/syslog.conf
    Lists where log files should go, what messages are written to them and
    the level of verbosity. It is also now possible to filter based on
    message content, message integrity, message encryption (near future),
    portability and better network forwarding.

/etc/termcap
    The terminal capability database. Describes the "escape sequences" by
    which various terminals can be controlled. Programs are written so that
    instead of directly outputting an escape sequence that only works on a
    particular brand of terminal, they look up the correct sequence to do
    whatever it is they want to do in /etc/termcap. As a result most programs
    work with most kinds of terminals.

/etc/timezone
    local timezone.

/etc/updatedb.conf
    Sets environment variables that are used by updatedb which therefore
    configures the database for 'locate', a utility that locates a pattern in
    a database of filenames and returns the filenames that match.

      # This file sets environment variables which are used by updatedb

      # filesystems which are pruned from updatedb database
      PRUNEFS="NFS nfs afs proc smbfs autofs auto iso9660 ncpfs coda devpts ftpfs"
      export PRUNEFS
      # paths which are pruned from updatedb database
      PRUNEPATHS="/tmp /usr/tmp /var/tmp /afs /amd /alex /var/spool"
      export PRUNEPATHS
      # netpaths which are added
      NETPATHS=""
      export NETPATHS


/etc/vga
    The configuration file for the svgalib is stored in this directory.
    svgalib provides graphics capabilities to programs running on the system
    console, without going through the X Window System. It uses direct access
    to the video hardware to provide low-level access to the standard VGA and
    SVGA graphics modes. It only works with some video hardware; so use with
    caution.

/etc/vim
    Contains configuration files for both vim and its X based counterpart
    gvim. A wide range of options can be accessed though these two files such
    as automatic indentation, syntax highlighting, etc....

/etc/xinetd.d/
    The original 'inetd' daemon has now been superseded by the much improved
    'xinetd'. 'inetd' should be run at boot time by /etc/init.d/inetd (or /
    etc/rc.local on some systems). It then listens for connections on certain
    Internet sockets. When a connection is found on one of its sockets, it
    decides what service the socket corresponds to, and invokes a program to
    service the request. After the program is finished, it continues to
    listen on the socket (except in some cases). Essentially, inetd allows
    running one daemon to invoke several others, reducing load on the system.
    Services controlled via xinetd put their configuration files here.

/etc/zlogin
    System-wide .zlogin file for zsh(1). This file is sourced only for login
    shells. It should contain commands that should be executed only in login
    shells. It should be used to set the terminal type and run a series of
    external commands (fortune, msgs, from, etc.)

/etc/zlogout
    Commands to be executed upon user exit from the zsh. Its control is
    system-wide but the .zlogout file for zsh(1) does override it in terms of
    importance.

/etc/zprofile
    System-wide .zprofile file for zsh(1). This file is sourced only for
    login shells (i.e. Shells invoked with "-" as the first character of argv
    [0], and shells invoked with the -l flag.)

/etc/zshenv
    System-wide .zshenv file for zsh(1). This file is sourced on all
    invocations of the shell. If the -f flag is present or if the NO_RCS
    option is set within this file, all other initialization files are
    skipped. This file should contain commands to set the command search
    path, plus other important environment variables. This file should not
    contain commands that produce output or assume the shell is attached to a
    tty.

/etc/zshrc
    System-wide .zshrc file for zsh(1). This file is sourced only for
    interactive shells. It should contain commands to set up aliases,
    functions, options, key bindings, etc.


Compliance with the FSSTND requires that the following directories, or
symbolic links to directories are required in /etc:

  opt       Configuration for /opt
  X11       Configuration for the X Window system (optional)
  sgml      Configuration for SGML (optional)
  xml       Configuration for XML (optional)

  The following directories, or symbolic links to directories must be in /etc,
  if the corresponding subsystem is installed:

  opt       Configuration for /opt

  The following files, or symbolic links to files, must be in /etc if the
  corresponding subsystem is installed (it is recommended that files be
  stored in subdirectories of /etc/ rather than directly in /etc:

  csh.login   Systemwide initialization file for C shell logins (optional)
  exports     NFS filesystem access control list (optional)
  fstab       Static information about filesystems (optional)
  ftpusers    FTP daemon user access control list (optional)
  gateways    File which lists gateways for routed (optional)
  gettydefs   Speed and terminal settings used by getty (optional)
  group       User group file (optional)
  host.conf   Resolver configuration file (optional)
  hosts       Static information about host names (optional)
  hosts.allow Host access file for TCP wrappers (optional)
  hosts.deny  Host access file for TCP wrappers (optional)
  hosts.equiv List of trusted hosts for rlogin, rsh, rcp (optional)
  hosts.lpd   List of trusted hosts for lpd (optional)
  inetd.conf  Configuration file for inetd (optional)
  inittab     Configuration file for init (optional)
  issue       Pre-login message and identification file (optional)
  ld.so.conf  List of extra directories to search for shared libraries
              (optional)
  motd        Post-login message of the day file (optional)
  mtab        Dynamic information about filesystems (optional)
  mtools.conf Configuration file for mtools (optional)
  networks    Static information about network names (optional)
  passwd      The password file (optional)
  printcap    The lpd printer capability database (optional)
  profile     Systemwide initialization file for sh shell logins (optional)
  protocols   IP protocol listing (optional)
  resolv.conf Resolver configuration file (optional)
  rpc         RPC protocol listing (optional)
  securetty   TTY access control for root login (optional)
  services    Port names for network services (optional)
  shells      Pathnames of valid login shells (optional)
  syslog.conf Configuration file for syslogd (optional)

  mtab does not fit the static nature of /etc: it is excepted for historical
  reasons. On some Linux systems, this may be a symbolic link to /proc/mounts,
  in which case this exception is not required.

  /etc/opt : Configuration files for /opt
  Host-specific configuration files for add-on application software packages
  must be installed within the directory /etc/opt/&60;subdir&62;, where
  &60;subdir&62; is the name of the subtree in /opt where the static data
  from that package is stored.

  No structure is imposed on the internal arrangement of /etc/opt/&60;subdir&62;.
  If a configuration file must reside in a different location in order for the
  package or system to function properly, it may be placed in a location other
  than /etc/opt/&60;subdir&62;.

  The rationale behind this subtree is best explained by referring to the
  rationale for /opt.

  /etc/X11 : Configuration for the X Window System (optional)
  /etc/X11 is the location for all X11 host-specific configuration. This
  directory is necessary to allow local control if /usr is mounted read only.

  The following files, or symbolic links to files, must be in /etc/X11 if the
  corresponding subsystem is installed:

  Xconfig    The configuration file for early versions of XFree86 (optional)
  XF86Config The configuration file for XFree86 versions 3 and 4 (optional)
  Xmodmap    Global X11 keyboard modification file (optional)

  Subdirectories of /etc/X11 may include those for xdm and for any other
  programs (some window managers, for example) that need them.

  /etc/X11/xdm holds the configuration files for xdm. These are most of the
  files previously found in /usr/lib/X11/xdm. Some local variable data for
  xdm is stored in /var/lib/xdm.

  It is recommended that window managers with only one configuration file
  which is a default .*wmrc file must name it system.*wmrc (unless there is
  a widely-accepted alternative name) and not use a subdirectory. Any window
  manager subdirectories must be identically named to the actual window
  manager binary.

  /etc/sgml : Configuration files for SGML (optional)
  Generic configuration files defining high-level parameters of the SGML
  systems are installed here. Files with names *.conf indicate generic
  configuration files. File with names *.cat are the DTD-specific centralized
  catalogs, containing references to all other catalogs needed to use the
  given DTD. The super catalog file catalog references all the centralized
  catalogs.

  /etc/xml : Configuration files for XML (optional)
  Generic configuration files defining high-level parameters of the XML
  systems are installed here. Files with names *.conf indicate generic
  configuration files. The super catalog file catalog references all the
  centralized catalogs.

-----------------------------------------------------------------------------

1.7. /home

Linux is a multi-user environment so each user is also assigned a specific
directory that is accessible only to them and the system administrator. These
are the user home directories, which can be found under '/home/$USER' (~/).
It is your playground: everything is at your command, you can write files,
delete them, install programs, etc.... Your home directory contains your
personal configuration files, the so-called dot files (their name is preceded
by a dot). Personal configuration files are usually 'hidden', if you want to
see them, you either have to turn on the appropriate option in your file
manager or run ls with the -a switch. If there is a conflict between personal
and system wide configuration files, the settings in the personal file will
prevail.

Dotfiles most likely to be altered by the end user are probably your
.xsession and .bashrc files. The configuration files for X and Bash
respectively. They allow you to be able to change the window manager to be
startup upon login and also aliases, user-specified commands and environment
variables respectively. Almost always when a user is created their dotfiles
will be taken from the /etc/skel directory where system administrators place
a sample file that user's can modify to their hearts content.

/home can get quite large and can be used for storing downloads, compiling,
installing and running programs, your mail, your collection of image or sound
files etc.

The FSSTND states that:

  /home is a fairly standard concept, but it is clearly a site-specific
  filesystem.

  Different people prefer to place user accounts in a variety of places.
  This section describes only a suggested placement for user home
  directories; nevertheless we recommend that all FHS-compliant
  distributions use this as the default location for home directories.
  On small systems, each user's directory is typically one of the many
  subdirectories of /home such as /home/smith, /home/torvalds,
  /home/operator, etc. On large systems (especially when the /home
  directories are shared amongst many hosts using NFS) it is useful
  to subdivide user home directories. Subdivision may be accomplished by
  using subdirectories such as /home/staff, /home/guests, /home/students,
  etc.
