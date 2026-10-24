
**symbol-table**

The part of an object table that gives the value of each symbol (usually as a section name and an offset) is called the symbol table. Executables may also have a symbol table, with this one giving the final values of the symbols. Debuggers use the symbol table to present addresses to the user in a symbolic, rather than a numeric form. It is possible to strip the symbol table from executables resulting in a smaller sized executable but this prevents meaningful debugging. From 252 <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Symbolic link**

An alias or shortcut to a program or file. From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**symbolic-link or soft-link**

A special filetype, which is a small pointer, file allowing multiple names for the same file. Unlilke hard links, symbolic links can be made for directories and can be made across filesystems. Commands that access the file being pointed to are said to follow the symbolic link. Commands that access the link itself do not follow the symbolic link. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**symlink (symbolic link)**

On UNIX, a symbolic link is where a file in one directory acts as a pointer to a file in another directory. For example, you could create a link so that all accesses to the file /tmp/foo really act upon the file /etc/passwd. This feature can often be exploited. While a non-root user does not have permission to write to administrative files like /etc/passwd, they can certainly create links to them in the /tmp directory or their local directory. SUID can then be exploited whereby they believe they are acting upon a user file, which which are instead acting upon the original administrative file. This is the leading way that local users can escalate their privileges on a system. Example: finger A user could link their .plan file to any other file on the system. A finger daemon running with root privileges would then follow the link to that file and read it upon execution of a finger lookup. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**symlinks**

scan/change symbolic links Symlinks scans directories for symbolic links and lists them on stdout. Each link is prefixed with a classification of relative, absolute, dangling, messy, lengthy or other_fs. Symlinks can also convert absolute links (within the same filesystem) to relative links and can delete messy and dangling links. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**symlinks**

The symlinks utility performs maintenance on symbolic links. Symlinks checks for symlink problems, including dangling symlinks which point to nonexistent files. Symlinks can also automatically convert absolute symlinks to relative symlinks. Install the symlinks package if you need a program for maintaining symlinks on your system. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SYMM**

SYnchronized MultiMedia working group (WAI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**symmetric**

In encryption, the word symmetric means those cases where the same key both encrypts and decrypts. This has been historically the "normal" encryption, but new public-key cryptography is changing things. Analogy: In your house, the same keys are used to lock and unlock your door. Examples: Some symmetric encryption ciphers are: DES The forerunner to most of today's popular symmetric ciphers. RC2, RC4, and RC5 Popular ciphers by RSA used in today's browsers for secure connections to websites. IDEA A cipher made popular by the fact that it was used in PGP. Blowfish A well-regarded cipher with free source code, no license required, unpatented, and royalty-free. As such, it is an extremely popular symmetric encryption algorithm. http://www.counterpane.com/blowfish.html TwoFish A new cipher with many of the same restrictions as Blowfish (i.e. none). It is even more efficient, and destined to become very popular. http://www.counterpane.com/twofish.html From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**symmetric multi-processing (SMP)**

Method of computing which uses two or more processors managed by one operating system, often sharing the same memory and having equal access to input/output devices. Application programs may run on any or all processors in a system. From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sympa**

Modern mailing list manager Sympa is a scalable and highly customizable modern mailing list manager which can cope with big lists (200,000 subscribers). It can can handle a lots of useful features : - Moderation - Digest mode - Authentication (for subscription process) - Archive management - Multi-language support (us, fr, de, as, it, fi and Chinese locales) - Expiration process - Virtual domains (virtual robots) - Accesses to LDAP directories - Using a RDBMS for storing subscriber information (it supports both MySQL and PostgreSQL). - S/MIME encryption and HTTPS authentication Sympa provides a scripting language for extending the behaviour of commands, and a complete (user and admin) Web interface called WWSympa. SYMPA means 'Systhme de Multi-Postage Automatique' (French) or 'Automatic Mailing System' (English). It is written in Perl and uses some modules (mailtools, md5, msgcat, db). WWSympa is provided in a separate package named `wwsympa'. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SYN**

The first packet sent across a TCP connection is known as a "SYN" or "synchronize" packet. For example, when you contact http://www.robertgraham.com, the first packet your systems out will be a SYN packet to the HTTP port 80 on www.robertgraham.com. Your browser is telling the web server that it wants to connect. Key point: Most packet-filtering firewalls work by blocking the SYN packets. This stops connections from being initiated. You can still scan behind these firewalls using ACK or FIN packets, but you will not be able to connect to any of those machines. See also: SYN flood, three-way-handshake, TCP From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SYN flood**

A SYN flood is a type of DoS attack. A SYN packet notifies a server of a new connection. The server then allocates some memory in order to handle the incoming connection, sends back an acknowledgement, then waits for the client to complete the connection and start sending data. By spoofing large numbers of SYN requests, an attacker can fill up memory on the server, which will sit their waiting for more data that never will arrive. Once memory has filled up, the server will be unable to accept connections from legitimate clients. This effectively disables the server. Key point: SYN floods exploit a flaw in the core of the TCP/IP technology itself. There is no complete defense against this attack. There are, however, partial defenses. Servers can be configured to reserve more memory and decrease the amount of time they wait for connections to complete. Likewise, routers and firewalls can filter out some of the spoofed SYN packets. Finally, there are techniques (such as "SYN cookies") that can play tricks with the protocol in order to help distinguish good SYNs from bad ones. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**synaesthesia**

A program for representing sounds visually This is a program for representing sounds visually (from a CD, line input, or through a pipe). It goes beyond the usual oscilloscope style program by combining a FFT and stereo positioning information to give a two dimensional display. X and svgalib versions are included in this package. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**synaptic**

GUI-frontend for APT Synaptic (previously known as raptor) is a graphical package management program for Debian. It provides the same features as the apt-get command line utility with a GUI front-end based on WINGs and can handle RPMs as well. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sync**

/sink/ n., vi. (var. `synch') 1. To synchronize, to bring into synchronization. 2. [techspeak] To force all pending I/O to the disk; see flush, sense 2. 3. More generally, to force a number of competing processes or agents to a state that would be `safe' if the system were to crash; thus, to checkpoint (in the database-theory sense). From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sync**

commit buffer cache to disk. From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sync**

flush filesystem buffers From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sync**

To force all pending I/O to the disk. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Sync**

To force all pending input/output to the disk drive. From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syncbbdb**

BBDB to PalmOS Pilot Manager conduit Transfer address records between a PalmOS device like a Palm Pilot or a Visor, using a perl BBDB to PalmOS Pilot Manager conduit. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SYSAD**

SYStem ADministrator, "SysAd" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysadmin**

/sis'ad-min/ n. Common contraction of `system admin'; see admin. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysadmin-guide**

The Linux System Administrators' Guide The Linux System Administrators' Guide from the Linux Documentation Project. Aimed at novice system administrators. This package presents the guide in HTML format, you can produce other formats by getting the source package. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysctl**

configure kernel parameters at runtime From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysctl**

read/write system parameters From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SYSEX**

SYStem EXecutive (OS, IBM, S/360) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysklogd**

System Logging Daemon This package implements the system log daemon, which is an enhanced version of the standard Berkeley utility program. It is responsible for providing logging of messages received from programs and facilities on the local host as well as from remote hosts. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysklogd**

The sysklogd package contains two system utilities (syslogd and klogd) which provide support for system logging. Syslogd and klogd run as daemons (background processes) and log system messages to different places, like sendmail logs, security logs, error logs, etc. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syslinux**

bootloader for Linux using MS-DOS floppies From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syslinux**

Bootloader for Linux/i386 using MS-DOS floppies SYSLINUX is a boot loader for the Linux/i386 operating system which operates off an MS-DOS/Windows FAT filesystem. It is intended to simplify first-time installation of Linux, and for creation of rescue and other special-purpose boot disks. SYSLINUX is probably not suitable as a general purpose boot loader. However, SYSLINUX has shown itself to be quite useful in a number of special-purpose applications. You will need support for `msdos' filesystem in order to use this program From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syslinux**

SYSLINUX is a boot loader for the Linux operating system which canoperate off MS-DOS floppies. It is intended to simplify first-time installation of Linux, rescue disks, and provide other uses for boot floppies. A SYSLINUX floppy can be manipulated using standard MS-DOS(or any other OS that can access an MS-DOS filesystem) tools (once it has been created), and requires only an approximately 7K DOS program or approximately 13K Linux program to create it in the first place. It also includes PXELINUX, a program to boot off a network server using a boot PROM compatible with the Intel PXE (Pre-Execution Environment) specification. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syslinux**

SYSLINUX is a boot loader for the Linux operating system which operates off an MS-DOS/Windows FAT filesystem. It is intended to simplify first-time installation of Linux, and for creation of rescue-and other special-purpose boot disks. This version include a patched SYSLINUX for handling VESA graphic mode. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syslinux2ansi**

converts a syslinux-format screen to pc-ansi From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syslog**

On UNIX, syslog is the standard logging facility. Programs call the syslog() function, and their messages end up somewhere in the /var/log directory. The syslog facility can also be configured to forward alerts from one UNIX machine to another (using un-authenticated UDP datagrams to port 514). Key point: When analyzing a machine that was broken into, you may find interesting information in the syslog logs. In particular, buffer-overflow attempts have distinctive messages, such as messages claiming an unknown command where the command is a string of binary characters. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syslog**

The UNIX System Logger. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Syslog**

The UNIX/Linux System Logger, where all system messages or errors are stored. From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syslog-facility**

Setup and remove LOCALx facility for sysklogd From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syslog-ng**

Next generation logging daemon Syslog-ng tries to fill the gaps original syslogd's were lacking: * powerful configurability * filtering based on message content * message integrity, message encryption (near future) * portability * better network forwarding From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syslog-summary**

Summarize the contents of a syslog log file. This program summarizes the contents of a log file written by syslog, by displaying each unique (except for the time) line once, and also the number of times such a line occurs in the input. The lines are displayed in the order they occur in the input. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syslogd-listfiles**

list system logfiles From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**syslogout**

Modularized system wide shell logout mechanism Simple centralized configuration mechanism for flexible maintenance of the shell specific parts for logout from a Debian Linux system. It has been designed to work with bash. Other shells have not been taken in consideration for this version. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysnews**

display system news The news command keeps you informed of news concerning the system. Each news item is contained in a separate file in the /var/lib/sysnews directory. Anyone having write permission to this directory can create a news file. NOTE: This command has nothing to do with USENET news. It's more like an enhanced motd. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysop**

/sis'op/ n. [esp. in the BBS world] The operator (and usually the owner) of a bulletin-board system. A common neophyte mistake on FidoNet is to address a message to `sysop' in an international echo, thus sending it to hundreds of sysops around the world. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SYSOP**

SYStem OPerator (BBS), "SysOp" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Sysop (System Operator)**

Anyone responsible for the physical operations of a computer system or network resource. For example, a System Administrator decides how often backups and maintenance should be performed and the System Operator performs those tasks. From Matisse <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysprofile**

Modularized system wide shell configuration mechanism Simple centralized configuration mechanism for flexible maintenance of the shell specific parts for login to a Debian Linux system. It has been designed to work with bash. Other shells have not been taken in consideration for this version. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysstat**

sar, iostat and mpstat - system performance tools for Linux The sysstat package contains the sar, mpstat and iostat commands for Linux. The sar command collects and reports system activity information. The iostat command reports CPU utilization and I/O statistics for disks. The mpstat command reports global and per-processor statistics. The statistics reported by sar concern I/O transfer rates, paging activity, process-related activities, interrupts, network activity, memory and swap space utilization, CPU utilization, kernel activities and TTY statistics, among others. Both UP and SMP machines are fully supported. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**system**

n. 1. The supervisor program or OS on a computer. 2. The entire computer system, including input/output devices, the supervisor program or OS, and possibly other software. 3. Any large-scale program. 4. Any method or algorithm. 5. `System hacker': one who hacks the system (in senses 1 and 2 only; for sense 3 one mentions the particular program: e.g., `LISP hacker') From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**system call**

The mechanism used by an application program to request service from the operating system. System calls often use a special machine code instruction which causes the processor to change mode (e.g. to "supervisor mode" or "protected mode"). From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**system-call**

The services provided by the kernel to application programs, and the way in which they are invoked. See section 2 of the manual pages. <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**System-Down::Rescue**

System-Down::Rescue is a free downloadable live distribution. It is designed to recover damaged file-systems, copying the data around other physical discs or networks, or burning them on a CD-ROM, using cdrecord. It features a working hardware detection system. Initial version 1.0.0pre4 was released June 9, 2003. A 'special purpose/mini' distribution. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**system-program**

Programs that implement high level functionality of an operating system, i.e., things that aren't directly dependent on the hardware. May sometimes require special privileges to run (e.g., for delivering electronic mail), but often just commonly thought of as part of the system (e.g., a compiler). <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**systemconfigurator**

Unified Configuration API for Linux Installation Provides an API for various installation and configuration processes that are otherwise inconsistent between the many Linux distributions, and the many architectures they run on. For example, you can configure the bootloader on a system in a general way - you don't need to know anything about the particular boot loader on the system. You can update the network settings of a system, without knowing the distribution or the format of its network configuration files. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**systemimager**

SystemImager utilities for golden clients SystemImager is a set of utilities for installing GNU/Linux images to clients machines over the network. Images are stored in flat files on the server, making updates easy. rsync is used for transfers, making updates efficient. This package contains utilities for updating a client's image from the server, and preparing a client for having it's image fetched by the server. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**systune**

Kernel tuning through the /proc filesystem. This program writes kernel parameters, previously saved in a configuration file, to the /proc filesystem. This enables kernel performance to be adjusted without recompiling the kernel. systune can be alternative to sysctl(8). It is also started after the most daemons and other init.d scripts, so it can be used as "second stage" sysctl. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysutils**

Miscellaneous small system utilities. This is a package incorporating various small utilities which are: procinfo - Displays system information from /proc (v17), memtest - Test system memory for errors (v2.93.1), bogomips - Shows the current bogomips rating without rebooting (v1.2), tofromdos - Converts DOS <-> Unix text files (v1.4). From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysvbanner**

System-V banner clone Displays a `banner' text the same way as the System V banner does: horizontally. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sysvinit**

System-V like init. Init is the first program to run after your system is booted, and continues to run as process number 1 until your system halts. Init's job is to start other programs that are essential to the operation of your system. All processes are descended from init. For more information, see the manual page init(8). From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SysVinit**

The SysVinit package contains a group of processes that control the very basic functions of your system. SysVinit includes the init program, the first program started by the Linux kernel when the system boots. Init then controls the startup, running and shutdown of all other programs. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
