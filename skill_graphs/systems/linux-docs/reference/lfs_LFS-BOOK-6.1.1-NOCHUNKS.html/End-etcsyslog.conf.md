# End /etc/syslog.conf`
EOF`
```

###  6.55.3. Contents of Sysklogd
**Installed programs:** klogd and syslogd
###  Short Descriptions
**klogd** |  A system daemon for intercepting and logging kernel messages
---|---
**syslogd** |  Logs the messages that system programs offer for logging. Every logged message contains at least a date stamp and a hostname, and normally the program's name too, but that depends on how trusting the logging daemon is told to be
##  6.56. Sysvinit-2.86
The Sysvinit package contains programs for controlling the startup, running, and shutdown of the system.
**Approximate build time:** 0.1 SBU
**Required disk space:** 1012 KB
**Installation depends on:** Binutils, Coreutils, GCC, Glibc, and Make
###  6.56.1. Installation of Sysvinit
When run-levels are changed (for example, when halting the system), **init** sends termination signals to those processes that **init** itself started and that should not be running in the new run-level. While doing this, **init** outputs messages like “Sending processes the TERM signal” which seem to imply that it is sending these signals to all currently running processes. To avoid this misinterpretation, modify the source so that these messages read like “Sending processes started by init the TERM signal” instead:
```
`sed -i 's@Sending processes@& started by init@g' \
    src/init.c`
```

Compile the package:
```
`make -C src`
```

Install the package:
```
`make -C src install`
```

###  6.56.2. Configuring Sysvinit
Create a new file `/etc/inittab` by running the following:
```
`cat > /etc/inittab << "EOF"
`# Begin /etc/inittab

id:3:initdefault:

si::sysinit:/etc/rc.d/init.d/rc sysinit

l0:0:wait:/etc/rc.d/init.d/rc 0
l1:S1:wait:/etc/rc.d/init.d/rc 1
l2:2:wait:/etc/rc.d/init.d/rc 2
l3:3:wait:/etc/rc.d/init.d/rc 3
l4:4:wait:/etc/rc.d/init.d/rc 4
l5:5:wait:/etc/rc.d/init.d/rc 5
l6:6:wait:/etc/rc.d/init.d/rc 6

ca:12345:ctrlaltdel:/sbin/shutdown -t1 -a -r now

su:S016:once:/sbin/sulogin

1:2345:respawn:/sbin/agetty -I '\033(K' tty1 9600
2:2345:respawn:/sbin/agetty -I '\033(K' tty2 9600
3:2345:respawn:/sbin/agetty -I '\033(K' tty3 9600
4:2345:respawn:/sbin/agetty -I '\033(K' tty4 9600
5:2345:respawn:/sbin/agetty -I '\033(K' tty5 9600
6:2345:respawn:/sbin/agetty -I '\033(K' tty6 9600
