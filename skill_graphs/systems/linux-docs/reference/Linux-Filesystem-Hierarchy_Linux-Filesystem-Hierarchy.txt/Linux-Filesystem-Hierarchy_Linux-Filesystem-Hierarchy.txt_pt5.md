      nasd: 192.168.0.


/etc/hosts.deny
    part of the tcp-wrappers system to control access to your machine's
    services. It lists hosts that are not allowed to access the system.

      # Example: ALL: some.host.name, .some.domain
      # ALL EXCEPT in.fingerd: other.host.name, .other.domain
      #
      # If you're going to protect the portmapper use the name "portmap"
      # for the daemon name. Remember that you can only use the keyword
      # "ALL" and IP addresses (NOT host or domain names) for the
      # portmapper. See portmap(8) and /usr/doc/portmap/portmapper.txt.gz
      # for further information.
      #
      # The PARANOID wildcard matches any host whose name does not match
      # its address. You may wish to enable this to ensure any programs
      # that don't validate looked up hostnames still leave understandable
      # logs. In past versions of Debian this has been the default.
      # ALL: PARANOID


/etc/httpd
    Apache configuration files. Apache is a versatile, high-performance HTTP
    server. The most popular server in the world, Apache features a modular
    design and supports dynamic selection of extension modules at runtime.
    Its strong points are its range of possible customization, dynamic
    adjustment of the number of server processes, and a whole range of
    available modules including many authentication mechanisms, server-parsed
    HTML, server-side includes, access control, CERN httpd metafiles
    emulation, proxy caching, etc. Apache also supports multiple virtual
    homing.

/etc/identd.conf
    TCP/IP IDENT protocol server. It implements the TCP/IP proposed standard
    IDENT user identification protocol (RFC 1413). identd operates by looking
    up specific TCP/IP connections and returning the username of the process
    owning the connection. It can also return other information besides the
    username.

      # /etc/identd.conf - an example configuration file


      #-- The syslog facility for error messages
      # syslog:facility = daemon


      #-- User and group (from passwd database) to run as
      server:user = nobody

      #-- Override the group id
      # server:group = kmem

      #-- What port to listen on when started as a daemon or from /etc/inittab
      # server:port = 113

      #-- The socket backlog limit
      # server:backlog = 256

      #-- Where to write the file containing our process id
      # server:pid-file = "/var/run/identd/identd.pid"

      #-- Maximum number of concurrent requests allowed (0 = unlimited)
      # server:max-requests = 0

      #-- Enable some protocol extensions like "VERSION" or "QUIT"
      protocol:extensions = enabled

      #-- Allow multiple queries per connection
      protocol:multiquery = enabled

      #-- Timeout in seconds since connection or last query. Zero = disable
      # protocol:timeout = 120

      #-- Maximum number of threads doing kernel lookups
      # kernel:threads = 8

      #-- Maximum number of queued kernel lookup requests
      # kernel:buffers = 32

      #-- Maximum number of time to retry a kernel lookup in case of failure
      # kernel:attempts = 5



      #-- Disable username lookups (only return uid numbers)
      # result:uid-only = no

      #-- Enable the ".noident" file
      # result:noident = enabled

      #-- Charset token to return in replies
      # result:charset = "US-ASCII"

      #-- Opsys token to return in replies
      # result:opsys = "UNIX"

      #-- Log all request replies to syslog (none == don't)
      # result:syslog-level = none


      #-- Enable encryption (only available if linked with a DES library)
      # result:encrypt = no

      #-- Path to the DES key file (only available if linked with a DES library)
      # encrypt:key-file = "/usr/local/etc/identd.key"


      #-- Include a machine local configuration file
      # include = /etc/identd.conf


/etc/inetd.conf
    Configuration of services that are started by the INETD TCP/IP super
    server. 'inetd' is now deprecated. 'xinetd' has taken its place. See /etc
    /xinet.conf for further details.

      # /etc/inetd.conf:  see inetd(8) for further information.
      #
      # Internet server configuration database
      #
      #
      # Lines starting with "#:LABEL:" or "#<off>#" should not
      # be changed unless you know what you are doing!
      #
      # If you want to disable an entry so it isn't touched during
      # package updates just comment it out with a single '#' character.
      #
      # Packages should modify this file by using update-inetd(8)
      #
      # <service_name> <sock_type> <proto>
      # <flags> <user> <server_path>
      # <args>
      #
      #:INTERNAL: Internal services
      #echo stream  tcp nowait root internal
      #echo dgram   udp wait root internal
      #chargen stream tcp   nowait root internal
      #chargen dgram udp    wait root internal
      discard stream tcp nowait root internal
      discard dgram udp wait root internal
      daytime stream tcp nowait root internal
      #daytime dgram udp wait root internal
      time stream tcp nowait root internal
      #time dgram udp wait root internal

      #:STANDARD: These are standard services.
      ftp stream tcp nowait root /usr/sbin/tcpd /usr/sbin/in.ftpd
      telnet stream tcp nowait telnetd.telnetd /usr/sbin/tcpd
                                               /usr/sbin/in.telnetd

      #:MAIL: Mail, news and uucp services.
      smtp stream tcp nowait mail /usr/sbin/exim exim -bs
      imap2  stream  tcp nowait root /usr/sbin/tcpd /usr/sbin/imapd
      imap3  stream  tcp nowait root /usr/sbin/tcpd /usr/sbin/imapd

      #:INFO: Info services
      ident stream tcp wait identd /usr/sbin/identd identd
      finger stream tcp nowait nobody /usr/sbin/tcpd
                                      /usr/sbin/in.fingerd

      #:BOOT: Tftp service is provided primarily for booting.
      #Most sites run this only on machines acting as "boot servers."
      tftp dgram udp wait nobody /usr/sbin/tcpd
                                 /usr/sbin/in.tftpd -s /tftpboot


/etc/init.d
    Order of scripts run in /etc/rc?.d
    ==================================

    0. Overview.

       All scripts executed by the init system are located in /etc/init.d.
       The directories /etc/rc?.d (? = S, 0 .. 6) contain relative links to
       those scripts. These links are named S<2-digit-number><
       original-name> or K<2-digit-number><original-name>.

       If a scripts has the ".sh" suffix it is a bourne shell script and
       MAY be handled in an optimized manner. The behaviour of executing the
       script in an optimized way will not differ in any way from it being
       forked and executed in the regular way.

       The following runlevels are defined:

       N       System bootup (NONE).
       S       Single user mode (not to be switched to directly)
       0       halt
       1       single user mode
       2 .. 5  multi user mode
       6       reboot

    1. Boot.

       When the systems boots, the /etc/init.d/rcS script is executed. It
       in turn executes all the S* scripts in /etc/rcS.d in alphabetical
       (and thus numerical) order. The first argument passed to the
       executed scripts is "start". The runlevel at this point is
       "N" (none).

       Only things that need to be run once to get the system in a consistent
       state are to be run. The rcS.d directory is NOT meant to replace rc.local.
       One should not start daemons in this runlevel unless absolutely
       necessary. Eg, NFS might need the portmapper, so it is OK to start it
       early in the boot process. But this is not the time to start the
       squid proxy server.

    2. Going multiuser.

       After the rcS.d scripts have been executed, init switches to the
       default runlevel as specified in /etc/inittab, usually "2".

       Init then executes the /etc/init.d/rc script which takes care of
       starting the services in /etc/rc2.d.

       Because the previous runlevel is "N" (none) the /etc/rc2.d/KXXxxxx
       scripts will NOT be executed - there is nothing to stop yet,
       the system is busy coming up.

       If for example there is a service that wants to run in runlevel 4
       and ONLY in that level, it will place a KXXxxxx script in
       /etc/rc{2,3,5}.d to stop the service when switching out of runlevel 4.
       We do not need to run that script at this point.

       The /etc.rc2.d/SXXxxxx scripts will be executed in alphabetical
       order, with the first argument set to "start".

    3. Switching runlevels.

       When one switches from (for example) runlevel 2 to runlevel 3,
       /etc/init.d/rc will first execute in alphabetical order all K
       scripts for runlevel 3 (/etc/rc3.d/KXXxxxx) with as first argument
       "stop" and then all S scripts for runlevel 3 (/etc/rc3.d/SXXxxxx)
       with as first argument "start".

       As an optimization, a check is made for each "service" to see if
       it was already running in the previous runlevel. If it was, and there
       is no K (stop) script present for it in the new runlevel, there is
       no need to start it a second time so that will not be done.

       On the other hand, if there was a K script present, it is assumed the
       service was stopped on purpose first and so needs to be restarted.

       We MIGHT make the same optimization for stop scripts as well-
       if no S script was present in the previous runlevel, we can assume
       that service was not running and we don't need to stop it either.
       In that case we can remove the "coming from level N" special case
       mentioned above in 2). But right now that has not been implemented.

    4. Single user mode.

       Switching to single user mode is done by switching to runlevel 1.
       That will cause all services to be stopped (assuming they all have
       a K script in /etc/rc1.d). The runlevel 1 scripts will then switch
       to runlevel "S" which has no scripts - all it does is spawn
       a shell directly on /dev/console for maintenance.

    5. Halt/reboot

       Going to runlevel 0 or 6 will cause the system to be halted or rebooted,
       respectively. For example, if we go to runlevel 6 (reboot) first
       all /etc/rc6.d/KXXxxxx scripts will be executed alphabetically with
       "stop" as the first argument.

       Then the /etc/rc6.d/SXXxxxx scripts will be executed alphabetically
       with "stop" as the first argument as well. The reason is that there
       is nothing to start any more at this point - all scripts that are
       run are meant to bring the system down.

       In the future, the /etc/rc6.d/SXXxxxx scripts MIGHT be moved to
       /etc/rc6.d/K1XXxxxx for clarity.

/etc/inittab
    Boot-time system configuration/initialization script. Tells init how to
    handle runlevels. It sets the default runlevel. This is run first except
    when booting in emergency (-b) mode. It also enables a user to startup a
    getty session on an external device such as the serial ports. To add
    terminals or dial-in modem lines to a system, just add more lines to /etc
    /inittab, one for each terminal or dial-in line. For more details, see
    the manual pages init, inittab, and getty. If a command fails when it
    starts, and init is configured to restart it, it will use a lot of system
    resources: init starts it, it fails, init starts it, it fails, and so on.
    To prevent this, init will keep track of how often it restarts a command,
    and if the frequency grows to high, it will delay for five minutes before
    restarting again. /etc/inittab also has some special features that allow
    init to react to special circumstances. powerwait Allows init to shut the
    system down, when the power fails. This assumes the use of a UPS, and
    software that watches the UPS and informs init that the power is off.
    ctrlaltdel Allows init to reboot the system, when the user presses
    ctrl-alt-del on the console keyboard. Note that the system administrator
    can configure the reaction to ctrl-alt-del to be something else instead,
    e.g., to be ignored, if the system is in a public location. sysinit
    Command to be run when the system is booted. This command usually cleans
    up /tmp, for example. The list above is not exhaustive. See your inittab
    manual page for all possibilities, and for details on how to use the ones
    above. To set (or reset) initial terminal colours. The following shell
    script should work for VGA consoles: for n in 1 2 4 5 6 7 8; do setterm
    -fore yellow -bold on -back blue -store > /dev/tty$n done Substitute your
    favorite colors, and use /dev/ttyS$n for serial terminals. To make sure
    they are reset when people log out (if they've been changed) replace the
    references to getty (or mingetty or uugetty or whatever) in /etc/inittab
    with references to /sbin/mygetty. #!/bin/sh setterm -fore yellow -bold on
    -back blue -store > $1 exec /sbin/mingetty $@ An example /etc/inittab is
    provided below.

      # /etc/inittab: init(8) configuration.
      # $Id: etc.xml,v 1.10 2004/02/03 21:42:57 binh Exp $
      # The default runlevel. id:2:initdefault:
      # Boot-time system configuration/initialization script.
      # This is run first except when booting in emergency (-b) mode.
      si::sysinit:/etc/init.d/rcS
      # What to do in single-user mode.
      ~~:S:wait:/sbin/sulogin
      # /etc/init.d executes the S and K scripts upon change
      # of runlevel.
      #
      # Runlevel 0 is halt.
      # Runlevel 1 is single-user.
      # Runlevels 2-5 are multi-user.
      # Runlevel 6 is reboot.
      l0:0:wait:/etc/init.d/rc 0 l1:1:wait:/etc/init.d/rc 1
      l2:2:wait:/etc/init.d/rc 2 l3:3:wait:/etc/init.d/rc 3
      l4:4:wait:/etc/init.d/rc 4 l5:5:wait:/etc/init.d/rc 5
      l6:6:wait:/etc/init.d/rc 6
      # Normally not reached, but fallthrough in case of emergency.
      z6:6:respawn:/sbin/sulogin
      # What to do when CTRL-ALT-DEL is pressed.
      ca:12345:ctrlaltdel:/sbin/shutdown -t1 -a -r now
      # Action on special keypress (ALT-UpArrow).
      #kb::kbrequest:/bin/echo "Keyboard Request
      #--edit /etc/inittab to let this work."
      # What to do when the power fails/returns.
      pf::powerwait:/etc/init.d/powerfail start
      pn::powerfailnow:/etc/init.d/powerfail now
