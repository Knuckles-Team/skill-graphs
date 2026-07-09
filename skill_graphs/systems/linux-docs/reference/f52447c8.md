
**setfdprm**

sets user-provided floppy disk parameters TQ From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setiathome**

SETI@Home Client (install package) SETI@home is a scientific experiment that harnesses the power of hundreds of thousands of Internet-connected computers in the Search for Extraterrestrial Intelligence (SETI). You can participate by running a free program that downloads and analyzes radio telescope data. There's a small but captivating possibility that your computer will detect the faint murmur of a civilization beyond Earth. SETI@Home is only distributed in binary form and the correct unix tar ball for your architecture has to be downloaded from http://setiathome.ssl.berkeley.edu/unix.html and placed in $TMPDIR (or /tmp if $TMPDIR is not defined). This installer package will automagically wget (if wget is installed) the right tarball and install the program, if the target debian linux architecture is one of the following: x86, alpha, sparc, powerpc or hppa. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setkeycodes**

load kernel scancode-to-keycode mapping table entries From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SETL**

SEt Theory Language (New York Uni.), "SetL" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setleds**

set the keyboard leds From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setmetamode**

define the keyboard meta key handling From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setmixer**

a command mode mixer. Got bored resetting soundcard manually after every reboot? Here is a small utility which can help you to avoid that. The whole source is setmixer.c. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SETP**

Secure Electronic Transactions Process From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SETP**

Stream Environment Transport Protocol From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setpci**

configure PCI devices From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setserial**

Controls configuration of serial ports. Set and/or report the configuration information associated with a serial port. This information includes what I/O port and which IRQ a particular serial port is using. This version has a completely new approach to configuration, so if you have a setup other than the standard ttyS0 and 1, you will have to get your hands dirty. By default, only COM1-4 are configured by the kernel, using IRQ 3 and 4. If you have other serial ports (such as an AST Fourport card), or if you have mapped the IRQs differently (perhaps COM3 and 4 to other IRQs to allow concurrent access with COM1 and 2) then you must have this package. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setserial**

get/set Linux serial port information From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setsid**

creates a session and sets the process group ID From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setsid**

run a program in a new session From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setterm**

set terminal attributes From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setuid**

sets the effective user ID of the current process. If the effective userid of the caller is root, the real and saved user ID's are also set. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setuid (SUID)**

UNIX programs that can be run by a user, but which have root privileges. Key point: In theory, setuid programs can only be installed by root, and they are considered as part of the operating system, because they inherently bypass security checks and must verify security themselves. A typical example is the passwd command, which a user runs in order to change his/her password. It must be setuid, because it changes files only root has access to, but yet it must be runnable by users. Key point: In practice, setuid programs often have bugs that can be exploited by logged in users. Key point: As part of hardening a system, the administrator should scour the system and remove all unnecessary setuid programs. Linux find / -type f -perm +6000 -exec ls -l {} \; Solaris find / -type f \\( -perm -4000 -o -perm -2000 \\) -exec ls -l {} \; In order to remove the suid bit, you can use the command chmod -s filename. Removing the suid bit will disable a lot of programs. Two programs that really need to have this bit turned on are /usr/bin/passwd, which users run to change their passwords, and /bin/su, which elevates a normal user to super user (when given the correct password). Key point: Some programs are really setguid which only changes the group context rather than the user context. Key point: Windows doesn't have the concept of setuid. Instead, RPC is used whereby client programs (run by users) contact server programs to carry out the desired task. For example, in order to change the password, the client program asks the SAM to do it on behalf of the user. Thus, whereas UNIX requires a myriad of client programs to verify credentials and be written securely, Windows only requires a few server programs to do the same. Key point: A common way to backdoor a system is to place a SUID program in the /tmp directory. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setuptool**

Setuptool is a user-friendly text mode menu utility which allows youto access all of the text mode configuration programs included in the Red Hat Linux operating system. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**setxkbmap**

set the keyboard using the X Keyboard Extension From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SEU**

Software-Entwicklungs-Umgebung (CASE) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SEU**

Source Entry Utility (IBM, ADT) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sex**

Simple editor for X The Simple editor for X (SeX) is a relatively small, simple, not too slow editor for X. It has no text mode user interface. It doesn't have very many features. The primary attraction is the mouse language, which is almost identical to xterm's, but clicking the middle mouse button inside a selection cuts it instead of pasting it. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**seyon**

Full-featured native X11 communications program. Seyon is a complete full-featured modem communications package for the X Window System. Some of its features are: - dialing directory - terminal emulation (DEC VT02, Tektronix 4014 and ANSI) - script language - Zmodem From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SF**

Service Feature (IN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SF**

Sign Flag (assembler) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SF**

Standard Form From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SF**

Switching Fabric From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFBI**

Shared Frame Buffer Interconnect From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sfconvert**

convert between various audio formats From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFD**

Simple Formattable Document (CCITT, MHS, X.420) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFD**

Start Frame Delimiter (ethernet) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFD**

Symbolic File Directory From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sfdisk**

Partition table manipulator for Linux From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFF**

Small Form Factor [committee] (org.) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sfftw2**

Library for computing Fast Fourier Transforms This library computes Fast Fourier Transforms (FFT) in one or more dimensions. It is extremely fast. This package contains the shared library version of the fftw libraries in single precision. To get the static library and the header files you need to install sfftw-dev. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sfinfo**

display information about audio files From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sfio**

Sfio is a library for managing I/O streams. It provides functionality similar to that of Stdio, the ANSI C Standard I/O library, but via a distinct interface that is more powerful, robust and efficient. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sfio1999**

Enhanced library for managing I/O streams. Sfio is a portable library for managing I/O streams. It provides similar functionality to the ANSI C Standard I/O functions known collectively as Stdio. However, it has a distinct interface and is generally faster and more robust than most Stdio implementations. Sfio also introduces a number of new features and concepts beyond Stdio stream I/O processing. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sfio2000**

Enhanced library for managing I/O streams. Sfio is a portable library for managing I/O streams. It provides similar functionality to the ANSI C Standard I/O functions known collectively as Stdio. However, it has a distinct interface and is generally faster and more robust than most Stdio implementations. Sfio also introduces a number of new features and concepts beyond Stdio stream I/O processing. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFMJI**

Sorry For My Jumping In (slang, Usenet, IRC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sformat**

SCSI disk format and repair tool Sformat will let you low-level format and repair bad blocks on SCSI disks. It can help you get data off a failing disk and often resurrect an apparently-broken drive. Users of SunOS will recognise the features from Sun's format command. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFP**

System File Protection (MS, WIndows) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFPRNSB**

Select a File for Processing and Read Next Spool Buffer (IBM, VM/ESA, CP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFPS**

Secure Fast Packet Switching (Cabletron) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFQL**

Structured Full-text Query Language From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sfront**

MPEG 4 Structured Audio files decoder. Sfront compiles MPEG 4 Structured Audio (MP4-SA) bitstreams into efficient C programs that generate audio when executed. It supports real-time, low-latency audio input/output and MIDI input from soundcards. MP4-SA is a standard for normative algorithmic sound, that combines an audio signal processing language (SAOL) with score languages (SASL, and the legacy MIDI File Format). From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sfs**

Self-Certifying File System common files SFS is a secure, global file system with completely decentralized control. It takes NFS shares exported from localhost and transports them securely to other hosts; NFS services do not need to be exposed to network. SFS features key management and authorization separated from filesystem with key revocation separated from key distribution. SFS requires solid NFSv3 support; Linux kernel version 2.2.18, 2.4.0 or greater is required (earlier versions need patching). SFS home page is at http://www.fs.net From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFS**

Shared File System (IBM. CMS, VM/ESA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFS**

Stepless Frequency Selection From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFS**

Suomen Standardisoimisliitto [Standards Association of Finland] (org., Finland) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFT**

System Fault Tolerance (Novell) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFT**

System File Table (DOS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFTP**

Screened Foiled Twisted Pair [cable] (UTP, TP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sftp**

Secure file transfer program From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFTP**

Simple File Transfer Protocol (RFC 913) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SFUG**

Security Features User's Guide From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sg**

Execute command as different group ID From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SG**

Signal Ground (MODEM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sg-utils**

Utilities for working with generic SCSI devices. This package includes a number of utilities to manipulate the linux "sg" (version 2) device driver, and to a lesser extent, the version 1 driver found in the 2.0.x kernels. The version 2 driver is only found in 2.2.x linux kernels; if you are using 2.4, please install the sg3-utils package instead. The package includes: * isosize - gives the number of bytes in an iso9660 filesystem * scsi_inquiry - same as sg_inq, only uses SCSI_IOCTL_SEND_COMMAND * sg_dd - a variant of 'dd' that works with the sg interface * sg_debug - prints debug info for all open sg file descriptors * sg_inq - a utility for poking around with the SCSI INQUIRY command * sg_map - shows the mapping between SCSI devices and sg devices * sg_rbuf - tests SCSI bus speed * sg_readcap - prints the output of a READ CAPACITY command * sg_runt_ex - an example program to test the sg driver version * sg_scan - displays the SCSI bus on stdout * sg_start - spins up (or down) disks * sg_test_rwbuf - tests the SCSI host adapter * sg_turs - execute a TEST UNIT READY command on the given device * sg_whoami - displays information about the given sg device * sginfo - a re-porting of the 'scsiinfo' program to use sg devices * sgp_dd - like sg_dd, only multithreaded It also includes sg_simple1 and sg_simple2, which demonstrate calls to the SCSI INQUIRY and TEST UNIT READY commands. They only differ in their error processing: sg_simple1 uses sg_err.[hc] for error processing while sg_simple2 does its own more primitive checks. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGA**

Shared Global Array (DEC, VMS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgb**

The Stanford GraphBase: combinatorial data and algorithms. A highly portable collection of programs and data for researchers who study combinatorial algorithms and data structures. The programs are intended to be interesting in themselves as examples of literate programming. Thus, the Stanford GraphBase can also be regarded as a collection of approximately 30 essays for programmers to enjoy reading, whether or not they are doing algorithmic research. The programs are written in CWEB, a combination of TeX and C that is easy to use by anyone who knows those languages and easy to read by anyone familiar with the rudiments of C. This package contains only the libraries and the demonstration programs; for the readable source code, which forms the documentation as well, see the sgb-doc package. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGC**

SCSI Graphic Commands (SAM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGI**

Silicon Graphics Incorporated (manufacturer, SGI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGID**

Set Group ID: a file attribute which allows a program to run with specific group privileges no matter who executes it. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGID (set group ID)**

The SGID permission causes a script to run with its group set to the group of the script, rather than the group of the user who started it. It is normally considered extremely bad practice to run a program in this way as it can pose many security problems. Later versions of the Linux kernel will even prohibit the running of shell scripts that have this attribute set. <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGM**

SeGmentation Message From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGML**

Standard Generalized Markup Language (ISO 8879, JTC1, RFC 1874, SGML) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgml**

The ISO standardization organization has normalized a set of characters symbolic names ("character entities") used by SGML documents of many types. There are character entities for latin languages, math symbols, greek, cyrillic, etc. This package also includes very basic utilities to allow SGML catalogs manipulation. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgml-data**

common SGML DTDs and entities This package includes Document Type Definitions for HTML Level 0, 1, 2, 3, 3.2, and 4.0, DTDs representing the capabilities for popular browsers, SGML and XML declarations, and popular XML DTDs. Also included are ISO standard entities (SGML and XML), HTML standard entities, and other generally useful sets of entities. Access to these data files is facilitated by the inclusion of an SGML catalog file which defines a default SGML declaration and a default DTD for documents whose DOCTYPE is 'html', and which links system identifiers to public identifiers for other SGML DTDs and entity sets. No setup is required by the user, due to the Debian SGML/XML common layer (see the sgml-base package) From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgml2html**

create HTML output from a LinuxDoc DTD SGML source file From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgml2info**

create GNU info output from a LinuxDoc DTD SGML source file From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgml2latex**

create LaTeX, DVI, PostScript or PDF output from a LinuxDoc DTD SGML source file From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgml2lyx**

create LyX output from a LinuxDoc DTD SGML source file From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgml2rtf**

create RTF output from a LinuxDoc DTD SGML source file From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgml2txt**

create plain text output from a LinuxDoc DTD SGML source file From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgml2x**

Generic formatter for SGML documents using DSSSL stylesheets sgml2x allows to easily format a SGML document using DSSSL stylesheets, and provides the following features: * Multiple possible stylesheets per document class * Easy integration of new stylesheets by adding a simple new definition file in a configuration directory * The caller can specify a PATH-like list of configuration directories, defaulting to a system-wide, a per-user, and a per-project configuration directories * Automatic selection of a default stylesheet to be used From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgml2xml**

convert SGML to XML From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGMLB**

Standard Generalized Markup Language - Binary version (SGML), "SGML-B" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgmlcheck**

check the syntax of an LinuxDoc DTD sgml source file From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgmldiff**

Find differences in the markup of two SGML files From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgmlnorm**

normalize SGML documents From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgmlpre**

handle SGML conditionalization for SGML-tools From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgmlsasp**

translate output of sgmls using ASP replacement files From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgmlspl**

a simple post-processor for nsgmls From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgmlspl**

SGMLS-based example Perl script for processing SGML parser output This is an example of a Perl script to post-process SGML parser output using the SGMLS Perl modules. To make sensible use of this package you will need to install a suitable SGML parser as well. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgmltexi**

SGML typesetting system able to create Texinfo documents. Sgmltexi is a DTD with tools to get Texinfo. The idea is to have another way to write Texinfo documents, intended to be a little bit easier. Sgmltexi manages Texinfo nodes automatically, generating an Info menu at the Top node, and other menus if required. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgmltools**

process sgml files. From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgmltools-2**

Replaced by sgmltools-lite (dummy package for upgrade) sgmltools-2 is now obsoleted and replaced by sgmltools-lite. This is dummy package for automatic migration. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgmltools-lite**

convert DocBook SGML source into HTML using DSSSL A text-formatting package based on SGML (Standard Generalized Markup Language), which allows you to produce TeX/DVI/PS/PDF, HTML, RTF, and plain ASCII (currently via w3m by default) from a single source with other recommended and suggested packages; due to the flexible nature of SGML, many other target formats are possible. This tool can not handle DocBook XML yet. For DocBook SGML only. HTML can be generated without any other Debian text processing package, but for the other formats the appropriate packages have to be installed. You need to install lynx or w3m for ASCII text output (w3m is the default txt backend). Also jadetex is required for PS and PDF, and linuxdoc-tools for ld2db conversion. This system is tailored for writing technical software documentation, an example of which are the Linux HOWTO documents. However, there is nothing Linux-specific about this package; it can be used for many other types of documentation on many other systems. It should be useful for all kinds of printed and online documentation. The package was formerly called linuxdoc-sgml because it originates from the Linux Documentation Project (LDP). The name has been changed into sgmltools to make it clearer that there is no Linux-specific stuff included in this package. This is the latest version of the sgmltools series and the successor of sgmltools v2. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgmlwhich**

outputs system SGML catalog path From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGMP**

Simple Gateway Monitoring Protocol (RFC 1028) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGRAM**

Synchronous Graphics Random Access Memory (DRAM, RAM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sgrep**

a tool to search a file for structured pattern Sgrep (structured grep) is a tool for searching text files and filtering text streams for structured criteria. Sgrep implements a query language based on so called region expressions. Like grep, sgrep can be used for any kind of text files. However it is most useful for text files containing some kind of structured text. A file containing structured text could be defined as a file, which obeys some syntax. Examples of structured text files are SGML, HTML, C, Tex and mail files. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGSN**

Serving GPRS Support Node (GPRS, mobile-systems) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGT**

Surrounding Gate Transistor (IC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SGTSI**

Semi-Graphical Tree Structure Interface From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sh**
