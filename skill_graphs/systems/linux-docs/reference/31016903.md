configurable, however, and it might be better to allow for some delay before
the reboot on a multiuser machine. Systems that are physically accessible to
anyone might even be configured to do nothing when ctrl-alt-del is pressed.
-----------------------------------------------------------------------------

8.5. Single user mode

The shutdown command can also be used to bring the system down to single user
mode, in which no one can log in, but root can use the console. This is
useful for system administration tasks that can't be done while the system is
running normally.
-----------------------------------------------------------------------------

8.6. Emergency boot floppies

It is not always possible to boot a computer from the hard disk. For example,
if you make a mistake in configuring LILO, you might make your system
unbootable. For these situations, you need an alternative way of booting that
will always work (as long as the hardware works). For typical PCs, this means
booting from the floppy drive.

Most Linux distributions allow one to create an emergency boot floppy during
installation. It is a good idea to do this. However, some such boot disks
contain only the kernel, and assume you will be using the programs on the
distribution's installation disks to fix whatever problem you have. Sometimes
those programs aren't enough; for example, you might have to restore some
files from backups made with software not on the installation disks.

Thus, it might be necessary to create a custom root floppy as well. The
Bootdisk HOWTO by Graham Chapman contains instructions for doing this. You
can find this HOWTO at [http://www.tldp.org/HOWTO/Bootdisk-HOWTO/index.html]
http://www.tldp.org/HOWTO/Bootdisk-HOWTO/index.html. You must, of course,
remember to keep your emergency boot and root floppies up to date.

You can't use the floppy drive you use to mount the root floppy for anything
else. This can be inconvenient if you only have one floppy drive. However, if
you have enough memory, you can configure your boot floppy to load the root
disk to a ramdisk (the boot floppy's kernel needs to be specially configured
for this). Once the root floppy has been loaded into the ramdisk, the floppy
drive is free to mount other disks.
-----------------------------------------------------------------------------

Chapter 9. init

    "Uuno on numero yksi" (Slogan for a series of Finnish movies.)

This chapter describes the init process, which is the first user level
process started by the kernel. init has many important duties, such as
starting getty (so that users can log in), implementing run levels, and
taking care of orphaned processes. This chapter explains how init is
configured and how you can make use of the different run levels.
-----------------------------------------------------------------------------

9.1. init comes first

init is one of those programs that are absolutely essential to the operation
of a Linux system, but that you still can mostly ignore. A good Linux
distribution will come with a configuration for init that will work for most
systems, and on these systems there is nothing you need to do about init.
Usually, you only need to worry about init if you hook up serial terminals,
dial-in (not dial-out) modems, or if you want to change the default run
level.

When the kernel has started itself (has been loaded into memory, has started
running, and has initialized all device drivers and data structures and
such), it finishes its own part of the boot process by starting a user level
program, init. Thus, init is always the first process (its process number is
always 1).

The kernel looks for init in a few locations that have been historically used
for it, but the proper location for it (on a Linux system) is /sbin/init. If
the kernel can't find init, it tries to run /bin/sh, and if that also fails,
the startup of the system fails.

When init starts, it finishes the boot process by doing a number of
administrative tasks, such as checking filesystems, cleaning up /tmp,
starting various services, and starting a getty for each terminal and virtual
console where users should be able to log in (see Chapter 10).

After the system is properly up, init restarts getty for each terminal after
a user has logged out (so that the next user can log in). init also adopts
orphan processes: when a process starts a child process and dies before its
child, the child immediately becomes a child of init. This is important for
various technical reasons, but it is good to know it, since it makes it
easier to understand process lists and process tree graphs. There are a few
variants of init available. Most Linux distributions use sysvinit (written by
Miquel van Smoorenburg), which is based on the System V init design. The BSD
versions of Unix have a different init. The primary difference is run levels:
System V has them, BSD does not (at least traditionally). This difference is
not essential. We'll look at sysvinit only.
-----------------------------------------------------------------------------

9.2. Configuring init to start getty: the /etc/inittab file

When it starts up, init reads the /etc/inittab configuration file. While the
system is running, it will re-read it, if sent the HUP signal (kill -HUP 1);
this feature makes it unnecessary to boot the system to make changes to the
init configuration take effect.

The /etc/inittab file is a bit complicated. We'll start with the simple case
of configuring getty lines. Lines in /etc/inittab consist of four
colon-delimited fields:
+---------------------------------------------------------------------------+
|id:runlevels:action:process                                                |
+---------------------------------------------------------------------------+
The fields are described below. In addition, /etc/inittab can contain empty
lines, and lines that begin with a number sign (`#'); these are both ignored.

id
    This identifies the line in the file. For getty lines, it specifies the
    terminal it runs on (the characters after /dev/tty in the device file
    name). For other lines, it doesn't matter (except for length
    restrictions), but it should be unique.

runlevels
    The run levels the line should be considered for. The run levels are
    given as single digits, without delimiters. (Run levels are described in
    the next section.)

action
    What action should be taken by the line, e.g., respawn to run the command
    in the next field again, when it exits, or once to run it just once.

process
    The command to run.


To start a getty on the first virtual terminal (/dev/tty1), in all the normal
multi-user run levels (2-5), one would write the following line:
+---------------------------------------------------------------------------+
|1:2345:respawn:/sbin/getty 9600 tty1                                       |
+---------------------------------------------------------------------------+
The first field says that this is the line for /dev/tty1. The second field
says that it applies to run levels 2, 3, 4, and 5. The third field means that
the command should be run again, after it exits (so that one can log in, log
out, and then log in again). The last field is the command that runs getty on
the first virtual terminal.

Different versions of getty are run differently. Consult your manual page,
and make sure it is the correct manual page.

If you wanted to add terminals or dial-in modem lines to a system, you'd add
more lines to /etc/inittab, one for each terminal or dial-in line. For more
details, see the manual pages init, inittab, and getty.

If a command fails when it starts, and init is configured to restart it, it
will use a lot of system resources: init starts it, it fails, init starts it,
it fails, init starts it, it fails, and so on, ad infinitum. To prevent this,
init will keep track of how often it restarts a command, and if the frequency
grows to high, it will delay for five minutes before restarting again.
-----------------------------------------------------------------------------

9.3. Run levels

A run level is a state of init and the whole system that defines what system
services are operating. Run levels are identified by numbers. Some system
administrators use run levels to define which subsystems are working, e.g.,
whether X is running, whether the network is operational, and so on. Others
have all subsystems always running or start and stop them individually,
without changing run levels, since run levels are too coarse for controlling
their systems. You need to decide for yourself, but it might be easiest to
follow the way your Linux distribution does things.

The following table defines how most Linux Distributions define the different
run levels. However, run-levels 2 through 5 can be modified to suit your own
tastes.


Table 9-1. Run level numbers
+-+----------------------------------------------------------------------+
|0|Halt the system.                                                      |
+-+----------------------------------------------------------------------+
|1|Single-user mode (for special administration).                        |
+-+----------------------------------------------------------------------+
|2|Local Multiuser with Networking but without network service (like NFS)|
+-+----------------------------------------------------------------------+
|3|Full Multiuser with Networking                                        |
+-+----------------------------------------------------------------------+
|4|Not Used                                                              |
+-+----------------------------------------------------------------------+
|5|Full Multiuser with Networking and X Windows(GUI)                     |
+-+----------------------------------------------------------------------+
|6|Reboot.                                                               |
+-+----------------------------------------------------------------------+

Services that get started at a certain runtime are determined by the contents
of the various rcN.d directories. Most distributions locate these directories
either at /etc/init.d/rcN.d or /etc/rcN.d. (Replace the N with the run-level
number.)

In each run-level you will find a series of if links pointing to start-up
scripts located in /etc/init.d. The names of these links all start as either
K or S, followed by a number. If the name of the link starts with an S, then
that indicates the service will be started when you go into that run level.
If the name of the link starts with a K, the service will be killed (if
running).

The number following the K or S indicates the order the scripts will be run.
Here is a sample of what an /etc/init.d/rc3.d may look like.
+---------------------------------------------------------------------------+
|# ls -l /etc/init.d/rc3.d                                                  |
|lrwxrwxrwx  1 root root 10 2004-11-29 22:09 K12nfsboot -> ../nfsboot       |
|lrwxrwxrwx  1 root root  6 2005-03-29 13:42 K15xdm -> ../xdm               |
|lrwxrwxrwx  1 root root  9 2004-11-29 22:08 S01pcmcia -> ../pcmcia         |
|lrwxrwxrwx  1 root root  9 2004-11-29 22:06 S01random -> ../random         |
|lrwxrwxrwx  1 root root 11 2005-03-01 11:56 S02firewall -> ../firewall     |
|lrwxrwxrwx  1 root root 10 2004-11-29 22:34 S05network -> ../network       |
|lrwxrwxrwx  1 root root  9 2004-11-29 22:07 S06syslog -> ../syslog         |
|lrwxrwxrwx  1 root root 10 2004-11-29 22:09 S08portmap -> ../portmap       |
|lrwxrwxrwx  1 root root  9 2004-11-29 22:07 S08resmgr -> ../resmgr         |
|lrwxrwxrwx  1 root root  6 2004-11-29 22:09 S10nfs -> ../nfs               |
|lrwxrwxrwx  1 root root 12 2004-11-29 22:40 S12alsasound -> ../alsasound   |
|lrwxrwxrwx  1 root root  8 2004-11-29 22:09 S12fbset -> ../fbset           |
|lrwxrwxrwx  1 root root  7 2004-11-29 22:10 S12sshd -> ../sshd             |
|lrwxrwxrwx  1 root root  8 2005-02-01 09:24 S12xntpd -> ../xntpd           |
|lrwxrwxrwx  1 root root  7 2004-12-02 20:34 S13cups -> ../cups             |
|lrwxrwxrwx  1 root root  6 2004-11-29 22:09 S13kbd -> ../kbd               |
|lrwxrwxrwx  1 root root 13 2004-11-29 22:10 S13powersaved -> ../powersaved |
|lrwxrwxrwx  1 root root  9 2004-11-29 22:09 S14hwscan -> ../hwscan         |
|lrwxrwxrwx  1 root root  7 2004-11-29 22:10 S14nscd -> ../nscd             |
|lrwxrwxrwx  1 root root 10 2004-11-29 22:10 S14postfix -> ../postfix       |
|lrwxrwxrwx  1 root root  6 2005-02-04 13:27 S14smb -> ../smb               |
|lrwxrwxrwx  1 root root  7 2004-11-29 22:10 S15cron -> ../cron             |
|lrwxrwxrwx  1 root root  8 2004-12-22 20:35 S15smbfs -> ../smbfs           |
+---------------------------------------------------------------------------+

How run levels start are configured in /etc/inittab by lines like the
following:
+---------------------------------------------------------------------------+
|l2:2:wait:/etc/init.d/rc 2                                                 |
+---------------------------------------------------------------------------+
The first field is an arbitrary label, the second one means that this applies
for run level 2. The third field means that init should run the command in
the fourth field once, when the run level is entered, and that init should
wait for it to complete. The /etc/init.d/rc command runs whatever commands
are necessary to start and stop services to enter run level 2.

The command in the fourth field does all the hard work of setting up a run
level. It starts services that aren't already running, and stops services
that shouldn't be running in the new run level any more. Exactly what the
command is, and how run levels are configured, depends on the Linux
distribution.

When init starts, it looks for a line in /etc/inittab that specifies the
default run level:
+---------------------------------------------------------------------------+
|id:2:initdefault:                                                          |
+---------------------------------------------------------------------------+
You can ask init to go to a non-default run level at startup by giving the
kernel a command line argument of single or emergency. Kernel command line
arguments can be given via LILO, for example. This allows you to choose the
single user mode (run level 1).

While the system is running, the telinit command can change the run level.
When the run level is changed, init runs the relevant command from /etc/
inittab.
-----------------------------------------------------------------------------

9.4. Special configuration in /etc/inittab

The /etc/inittab has some special features that allow init to react to
special circumstances. These special features are marked by special keywords
in the third field. Some examples:

powerwait
    Allows init to shut the system down, when the power fails. This assumes
    the use of a UPS, and software that watches the UPS and informs init that
    the power is off.

ctrlaltdel
    Allows init to reboot the system, when the user presses ctrl-alt-del on
    the console keyboard. Note that the system administrator can configure
    the reaction to ctrl-alt-del to be something else instead, e.g., to be
    ignored, if the system is in a public location. (Or to start nethack.)

sysinit
    Command to be run when the system is booted. This command usually cleans
    up /tmp, for example.


The list above is not exhaustive. See your inittab manual page for all
possibilities, and for details on how to use the above ones.
-----------------------------------------------------------------------------

9.5. Booting in single user mode

An important run level is single user mode (run level 1), in which only the
system administrator is using the machine and as few system services,
including logins, as possible are running. Single user mode is necessary for
a few administrative tasks, such as running fsck on a /usr partition, since
this requires that the partition be unmounted, and that can't happen, unless
just about all system services are killed.

A running system can be taken to single user mode by using telinit to request
run level 1. At bootup, it can be entered by giving the word single or
emergency on the kernel command line: the kernel gives the command line to
init as well, and init understands from that word that it shouldn't use the
default run level. (The kernel command line is entered in a way that depends
on how you boot the system.)

Booting into single user mode is sometimes necessary so that one can run fsck
by hand, before anything mounts or otherwise touches a broken /usr partition
(any activity on a broken filesystem is likely to break it more, so fsck
should be run as soon as possible).

The bootup scripts init runs will automatically enter single user mode, if
the automatic fsck at bootup fails. This is an attempt to prevent the system
from using a filesystem that is so broken that fsck can't fix it
automatically. Such breakage is relatively rare, and usually involves a
broken hard disk or an experimental kernel release, but it's good to be
prepared.

As a security measure, a properly configured system will ask for the root
password before starting the shell in single user mode. Otherwise, it would
be simple to just enter a suitable line to LILO to get in as root. (This will
break if /etc/passwd has been broken by filesystem problems, of course, and
in that case you'd better have a boot floppy handy.)
-----------------------------------------------------------------------------

Chapter 10. Logging In And Out

    "I don't care to belong to a club that accepts people like me as a
    member." (Groucho Marx)

This section describes what happens when a user logs in or out. The various
interactions of background processes, log files, configuration files, and so
on are described in some detail.
-----------------------------------------------------------------------------

10.1. Logins via terminals

Section 2.3.2 shows how logins happen via terminals. First, init makes sure
there is a getty program for the terminal connection (or console). getty
listens at the terminal and waits for the user to notify that he is ready to
login in (this usually means that the user must type something). When it
notices a user, getty outputs a welcome message (stored in /etc/issue), and
prompts for the username, and finally runs the login program. login gets the
username as a parameter, and prompts the user for the password. If these
match, login starts the shell configured for the user; else it just exits and
terminates the process (perhaps after giving the user another chance at
entering the username and password). init notices that the process
terminated, and starts a new getty for the terminal.


Figure 10-1. Logins via terminals: the interaction of init, getty, login, and
the shell.

[logins-via-terminals]

Note that the only new process is the one created by init (using the fork
system call); getty and login only replace the program running in the process
(using the exec system call).

A separate program, for noticing the user, is needed for serial lines, since
it can be (and traditionally was) complicated to notice when a terminal
becomes active. getty also adapts to the speed and other settings of the
connection, which is important especially for dial-in connections, where
these parameters may change from call to call.

There are several versions of getty and init in use, all with their good and
bad points. It is a good idea to learn about the versions on your system, and
also about the other versions (you could use the Linux Software Map to search
them). If you don't have dial-ins, you probably don't have to worry about
getty, but init is still important.
-----------------------------------------------------------------------------

10.2. Logins via the network

Two computers in the same network are usually linked via a single physical
cable. When they communicate over the network, the programs in each computer
that take part in the communication are linked via a virtual connection, a
sort of imaginary cable. As far as the programs at either end of the virtual
connection are concerned, they have a monopoly on their own cable. However,
since the cable is not real, only imaginary, the operating systems of both
computers can have several virtual connections share the same physical cable.
This way, using just a single cable, several programs can communicate without
having to know of or care about the other communications. It is even possible
to have several computers use the same cable; the virtual connections exist
between two computers, and the other computers ignore those connections that
they don't take part in.

That's a complicated and over-abstracted description of the reality. It
might, however, be good enough to understand the important reason why network
logins are somewhat different from normal logins. The virtual connections are
established when there are two programs on different computers that wish to
communicate. Since it is in principle possible to login from any computer in
a network to any other computer, there is a huge number of potential virtual
communications. Because of this, it is not practical to start a getty for
each potential login.

There is a single process inetd (corresponding to getty) that handles all
network logins. When it notices an incoming network login (i.e., it notices
that it gets a new virtual connection to some other computer), it starts a
new process to handle that single login. The original process remains and
continues to listen for new logins.

To make things a bit more complicated, there is more than one communication
protocol for network logins. The two most important ones are telnet and
rlogin. In addition to logins, there are many other virtual connections that
may be made (for FTP, Gopher, HTTP, and other network services). It would be
ineffective to have a separate process listening for a particular type of
connection, so instead there is only one listener that can recognize the type
of the connection and can start the correct type of program to provide the
service. This single listener is called inetd; see the Linux Network
Administrators' Guide for more information.
-----------------------------------------------------------------------------

10.3. What login does

The login program takes care of authenticating the user (making sure that the
username and password match), and of setting up an initial environment for
the user by setting permissions for the serial line and starting the shell.

Part of the initial setup is outputting the contents of the file /etc/motd
(short for message of the day) and checking for electronic mail. These can be
disabled by creating a file called .hushlogin in the user's home directory.

If the file /etc/nologin exists, logins are disabled. That file is typically
created by shutdown and relatives. login checks for this file, and will
refuse to accept a login if it exists. If it does exist, login outputs its
contents to the terminal before it quits.

login logs all failed login attempts in a system log file (via syslog). It
also logs all logins by root. Both of these can be useful when tracking down
intruders.

Currently logged in people are listed in /var/run/utmp. This file is valid
only until the system is next rebooted or shut down; it is cleared when the
system is booted. It lists each user and the terminal (or network connection)
he is using, along with some other useful information. The who, w, and other
similar commands look in utmp to see who are logged in.

All successful logins are recorded into /var/log/wtmp. This file will grow
without limit, so it must be cleaned regularly, for example by having a
weekly cron job to clear it. The last command browses wtmp.

Both utmp and wtmp are in a binary format (see the utmp manual page); it is
unfortunately not convenient to examine them without special programs.
-----------------------------------------------------------------------------

10.4. X and xdm

XXX X implements logins via xdm; also: xterm -ls

TO BE ADDED
-----------------------------------------------------------------------------

10.5. Access control

The user database is traditionally contained in the /etc/passwd file. Some
systems use shadow passwords, and have moved the passwords to /etc/shadow.
Sites with many computers that share the accounts use NIS or some other
method to store the user database; they might also automatically copy the
database from one central location to all other computers.

The user database contains not only the passwords, but also some additional
information about the users, such as their real names, home directories, and
login shells. This other information needs to be public, so that anyone can
read it. Therefore the password is stored encrypted. This does have the
drawback that anyone with access to the encrypted password can use various
cryptographic methods to guess it, without trying to actually log into the
computer. Shadow passwords try to avoid this by moving the password into
another file, which only root can read (the password is still stored
encrypted). However, installing shadow passwords later onto a system that did
not support them can be difficult.

With or without passwords, it is important to make sure that all passwords in
a system are good, i.e., not easily guessed. The crack program can be used to
crack passwords; any password it can find is by definition not a good one.
