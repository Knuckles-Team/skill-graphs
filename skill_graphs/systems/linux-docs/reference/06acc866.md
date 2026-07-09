
**mikmod**

MikMod is a MOD music file player. MikMod uses the OSS /dev/dsp driver including all recent kernels for output, and will also write .wavfiles. Supported file formats include MOD, STM, S3M, MTM, XM, ULT, andIT. The player uses ncurses for console output. It supports transparent loading from gzip/pkzip/zoo archives and the loading and saving of playlists. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mikmod**

Portable tracked music player Mikmod is a very portable tracked music player which supports a wide variety of module formats including compressed sample Impulse Tracker modules. It also supports many archive formats, as well as on the fly decompression. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIL**

Matrox Imaging Library From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Miller, Cliff**

president and CEO of TurboLinux, a popular Linux distribution. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Miller, David**

responsible for the TCP/IP coding in the Linux kernel, David Miller is also responsible for UltraPenguin (a project to port Linux to Sparc CPUs), kernel fixes and developments such as fuzzy hashing. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MILNET**

MILitary NETwork (USA, mil., network) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MILOS**

Maschinelle Indizierung auf Linguistischer Grundlage fuer OPAC Systeme (OPAC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MILSTAR**

Military Strategic TActical Relay (mil., USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MILSTD**

Military STandarD (mil., USA), "MIL-STD" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIMD**

Multiple Instruction [stream], Multiple Data [stream] (CPU) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIME**

(Multipurpose Internet Mail Extensions) The protocol for attaching non-text files to email messages (graphics, spreadsheets, formatted text documents, sound files, Quicktime, multimedia files, etc.) MIME is utilised by some email packages & is universally used by Web Servers to identify the files they are sending to Web Clients. From Faculty-of-Education <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIME**

Multipurpose Internet Mail Extensions (RFC 2045/2046/2047/2048/2049, IETF) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIME (Multipurpose Internet Mail Extensions)**

Originally a standard for defining the types of files attached to standard Internet mail messages. The MIME standard has come to be used in many situations where one cmputer programs needs to communicate with another program about what kind of file is being sent. For example, HTML files have a MIME-type of text/html, JPEG files are image/jpeg, etc. From Matisse <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIME encapsulation**

Most graphical mail readers have the ability to attach files to mail messages and read these attachments. The way they do this is not with uuencode but in a special format known as MIME encapsulation. MIME (Multipurpose Internet Mail Extensions) is a way of representing multiple files inside a single mail message. The way binary data is handled is similar to uuencode, but in a format known as base64. Each MIME attachment to a mail message has a particular type, known as the MIME type. MIME types merely classify the attached file as an image, an audio clip, a formatted document, or some other type of data. The MIME type is a text tag with the format <major>/<minor>. The major part is called the major MIME type and the minor part is called the minor MIME type. Available major types match all the kinds of files that you would expect to exist. They are usually one of application, audio, image, message, text, or video. The application type means a file format specific to a particular utility. The minor MIME types run into the hundreds. A long list of MIME types can be found in /etc/mime.types. If needed, some useful command-line utilities in the same vein as uuencode can create and extract MIME messages. These are mpack, munpack, and mmencode (or mimencode). From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mime-codecs**

Fast Quoted-Printable and BASE64 MIME transport codecs At its most basic MIME is a set of transfer encodings used to ensure error free transport, and a set of content types. VM understands the two standard MIME transport encodings, Quoted-Printable and BASE64, and will decode messages that use them as necessary. VM has Emacs-Lisp based Quoted-Printable and BASE64 encoders and decoders, but you can have VM use external programs to perform these tasks and the process will almost certainly be faster. This package provides external executables for Quoted-Printable and BASE64 encoders and decoders. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mime-construct**

construct/send MIME messages from the command line mime-construct constructs and (by default) mails MIME messages. It is entirely driven from the command line, it is designed to be used by other programs, or people who act like programs. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mime-support**

MIME files 'mime.types' & 'mailcap', and support programs As these files can be used by all MIME compliant programs, they have been moved into their own package that others can depend upon. Other packages add themselves as viewers/editors/composers/etc by using the provided "update-mime" program. In addition, the commands "see", "edit", "compose", and "print" will display, alter, create, and print (respectively) any file using a program determined from the entries in the mime.types and mailcap files. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mimedecode**

Decodes transfer encoded text type mime messages. This program performs the decoding of transfer encoded text type mime messages. The message in its entirety is read from stdin. The decoded message is written to stdout; hence, this program behaves as a filter which may be placed wherever convenient. It is assumed that the message has reached its point of final delivery and at that point 8-bit text types can be handled natively. Hence, the need for transfer-encodings is not present any more. Only some cases are handled: - encoded header fields are decoded from QP or B encoding. - The charset is assumed to be iso-8859-1 - part or subparts of content-type text only are decoded - all other content-types are passed transparently. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mimefilter**

Strips some unwanted MIME parts out of a MIME message. This program may be useful as a filter on a mailing list. It strips every unwanted MIME part from a MIME compliant message, warning by email the original author about this, and outputs a MIME compliant cleaned message, to be further processed by a mailing list software. You may find it useful if you don't want certain attachments on your mailing lists, or if you want to allow just the text part from multipart/alternative messages, and so on. You can easily fine tune the list of allowed MIME types to suit your particular needs, using normal Perl regexps. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIMOLA**

Machine Independent MicrOprogramming LAnguage (HDL) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIN**

Multistage Interconnection Networks From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MINC**

Multilingual Internet Names Consortium (org., Internet, DOMAIN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mindi**

Creates boot/root disks based on your system Mindi is a script that creates boot/root disks based on your system. It uses your kernel, modules, tools and libraries. It is use for the Mondo disaster recovery scripts and tools to create the boot CD/disks. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Mindi Linux**

Mindi builds boot/root disk images using your existing kernel, modules, tools and libraries. Version 0.71_20021109 was released November 10, 2002. Version 0.85 was released May 21, 2003. A 'special purpose/mini' distribution. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mindterm**

java ssh client that can be used as a web applet Mindterm is a ssh client written in java that can be used as a web applet. This package installs it so it will be available on your web site; users can then ssh into the system from most web browsers that have java support. Warning: By its very nature, installing this package and making it available on your web server constitutes exporting cryptographic software. If you're in a country that does not look kindly on this act, use caution. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mindy**

A Dylan interpreter. Mindy is a Dylan bytecode interpreter, originally written as part of CMU's Gwydion Dylan project. It compiles faster than d2c and includes much better debugging tools. Unfortunately, Mindy makes no attempt to run fast. Documentation for Mindy can be found in the main gwydion-dylan package, or on the web at <http://www.gwydiondylan.org/>. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**minfo**

print the parameters of a MSDOS filesystem TQ From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mingetty**

The mingetty program is a lightweight, minimalist getty program foruse only on virtual consoles. Mingetty is not suitable for serial lines (you should use the mgetty program instead for that purpose). From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mingw32**

Minimalist GNU win32 (cross) compiler A Linux hosted, win32 target, cross compiler for C/C++ Freedom through obsolescence. Those who still really need to can now build windows executables from the comfort of Debian. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mingw32-runtime**

Minimalist GNU win32 (cross) compiler runtime This package contains the target runtime files for a Linux hosted, win32 target, C/C++ cross compiler. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**minicom**

Clone of the MS-DOS "Telix" communications program. Minicom is a menu driven communications program. It emulates ANSI and VT102 terminals. It has a dialing directory and auto zmodem download. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**minicom**

friendly serial communication program From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**minicom**

Minicom is a simple text-based modem control and terminal emulation program somewhat similar to MSDOS Telix. Minicom includes a dialing directory, full ANSI and VT100 emulation, an (external) scripting language, and other features. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**minilinux**

MiniLinux is for Hams (Ham Radio). There do not appear to be recent updates, the latest is v2.2.15b 8.V.2000. Distribution development is not all that active. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**minimalist**

a MINImalist MAiling LIST manager Minimalist is a MINImalist MAiling LIST manager. It is fast, extremely easy to setup and support. Minimalist has these features: - subscribing/unsubscribing users by request - several levels of security - additional services such as information about list, archiving lists, information about users of list and so on - support for read-only/closed/mandatory lists - support for Blacklist - logging activity Minimalist has also a notion of 'trusted users'. They have full rights to subscribe/unsubscribe other users; get any information related to lists and users. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MINISTREL**

Models for INformatIon STorage and REtrievaL (OA, BIS, ESPRIT) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mini_commander_applet**

Mini-Commander Applet for the GNOME panel. From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**minpack1**

nonlinear equations and nonlinear least squares shared library Minpack includes software for solving nonlinear equations and nonlinear least squares problems. Five algorithmic paths each include a core subroutine and an easy-to-use driver. The algorithms proceed either from an analytic specification of the Jacobian matrix or directly from the problem functions. The paths include facilities for systems of equations with a banded Jacobian matrix, for least squares problems with a large amount of data, and for checking the consistency of the Jacobian matrix with the functions. This package provides the shared library. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MINT**

Mint is Not TOS (Atari), "MiNT" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MINT**

Multimedia-kommunikation aif Integrierten Netzen und Terminals From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MINX**

Multimedia Information Network eXchange From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIO**

Memory Input/Output (Motorola) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIO**

Modular Input/Output [architecture] (HP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIP**

Multimission Interactive Picture From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIP**

Multum In Parvo (3D, SAT) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIPS**

Microprocessor without Interlocked Piped Stages From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIPS**

Million Instructions Per Second (CPU) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIR**

Maximum Information Rate From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIR**

Micro-Instruction Register (IC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Miracle Linux**

Miracle Linux is a high reliability, scalability and availability server OS for the enterprise market, according to MIRACLE LINUX CORPORATION, the developer of the distribution. MIRACLE LINUX CORPORATION was originally founded by Oracle Corporation Japan. (Currently Oracle Japan owns about 60% of MIRACLE LINUX.) They offer not only "MIRACLE LINUX with Oracle," but also "MIRACLE LINUX for Samba" and "MIRACLE LINUX for PostgreSQL." Japanese distribution From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mird1**

Mird database library (runtime files) Mird is a database library, for operating on simple disk-based databases. This package contains files necessary for runing applications that use Mird database From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Mirror**

Generally speaking, "to mirror" is to maintain an exact copy of something. Probably the most common use of the term on the Internet refers to "mirror sites" which are web sites, or FTP sites that maintain copies of material originated at another location, usually in order to provide more widespread access to the resource. For example, one site might create a library of software, and 5 other sites might maintain mirrors of that library. From Matisse <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mirror**

Keeps FTP archives up-to-date Mirror uses the FTP protocol to locally duplicate remote host files and directories selected with Perl regular expressions. By default transfers only files missing locally or whose remote sizes or time-stamps have changed. Can reduce directory download using compressed listings in ls-lR.gz files or further using compressed differences of daily listings in ls-lR.patch.gz files. Amongst many flexible options it can gzip and split files. Tracks large distant FTP archives accurately with low download volume. Simpler programs like "mirrordir" use less memory and may copy directory trees faster between local machines. From mirror.tar.gz 2.9 in Perl by Lee McLoughlin. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mirrordir**

duplicate a directory by making a minimal set of changes mirrordir forces the mirror directory to be an exact replica of the control directory tree in every possible detail suitable for purposes of timed backup. Files whose modification times or sizes differ are copied. File permissions, ownerships, modification times, access times, and sticky bits are duplicated. Devices, pipes, and symbolic and hard links are duplicated. Files or directories that exist in the mirror directory that don't exist in the control directory are deleted. It naturally descends into subdirectories to all their depths. mirrordir tries to be as efficient as possible by making the minimal set of changes necessary to mirror the directory. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mirrordir**

Easy to use ftp mirroring package - simply usemirrordir ftp://some.where.com/dir /some/local/dir From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mirrormagic**

Shoot around obstacles to collect energy using your beam. A game like "Deflektor" (C 64) or "Mindbender" (Amiga). The goal is to work out how to get around obstacles to shoot energy containers with your beam, enabling the path to the next level to be opened. Included are many levels known from the games "Deflektor" and "Mindbender". Some features: - stereo sound effects and music - music module support for SDL version (Unix/Win32) - fullscreen support for SDL version (Unix/Win32) - complete source code included under GNU GPL From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIS**

Management Information System From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIS**

Mega Iterations per Second From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**miscfiles**

Dictionaries and other interesting files. These files are not crucial to system administration or operation, but which have come to be common on various systems over the years. They originated from various sources and are freely redistributable (see the copyright file for more information). These files include those of general interest (English `connectives', Webster's Second International English wordlist, traditional stone and flower for each month, Precedence table for operators in the C language, description of the ISO Latin-1 character set, two-letter codes for languages, from ISO 639, International country telephone codes, geographic coordinates of many major cities, Some common abbreviations used in electronic communication, GNU tasks and mailing lists, country and currency abbreviations, rfc-index, etc.). There also is information specific to the United States (List of three letter codes for some major airports, North American (+1) telephone area codes, postal codes for US and Mexican states and Canadian provinces, the Constitution of the United States of America, the Declaration of Independence of the Thirteen Colonies). From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**miscutils**

obsolete utilities package miscutils is an obsolete package and may be removed safely. miscutils was replaced by the following packages: getty, login, util-linux, update, fdutils, debianutils, passwd. Since fdutils is not required, it must be installed separately. After this version miscutils is installed, it is safe and desirable to purge miscutils. If miscutils is purged while it still has conffiles, then important conffiles may be lost. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MISD**

Multiple Instruction [stream], Single Data [stream] (CPU) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MISS**

Mecklenburg Internet Service System (ISP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MISSI**

Multilevel Information System Security Initiative (org.) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mission critical**

Describes a system that is absolutely necessary. It comes from NASA where mission critical elements were those items that had to work otherwise the billion dollar space mission would blow up. Key point: A big problem with corporations is that they do not spend enough time hardening mission critical applications, or spend too much effort on non-mission critical elements. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MISX**

Metered Services Information eXchange (Internet) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIT**

Management Information Tree From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIT**

Massachusetts Institute of Technology (org., USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mit-scheme**

The MIT Scheme development environment MIT Scheme is an implementation of the Scheme programming language, providing an interpreter, compiler, source-code debugger, integrated Emacs-like editor, and a large runtime library. MIT Scheme is best suited to programming large applications with a rapid development cycle. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIT-SHM**

A MIT shared-memory Ximage \ref {X extension}. It provides both shared memory XImages and shared memory pixmaps based on the SYSV shared memory primitives. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mixal**

A MIX emulator and MIXAL interpreter Mixal is an implementation of the imaginary computer called MIX and its assembly language MIXAL, which were invented by Donald E. Knuth in the 1960's for use in his monumental and yet unfinished book series "The Art of Computer Programming". All actual programs and all programming exercises in the series are written in MIXAL. This package contains a modified version of Darius Bacon's Mixal implementation. It takes a MIXAL source file, translates it to MIX machine code and then executes the resulting program, all in a single run. The result of the assembler step cannot be extracted to a file. Similarly, one cannot take a precompiled MIX program and try to execute it in this emulator - only MIXAL source is accepted. The MIX emulator does not support floating-point operations nor the tape devices described in Knuth's book. This is not fatal, however, and most of the programs and exercise answers in Knuth's book can be run in this MIXAL implementation. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mixer.app**

Another mixer application designed for WindowMaker There's nothing in the program that makes it *require* WindowMaker, except maybe the look. Mixer.app is a mixer utility for Linux systems. Requires /dev/mixer to work. Provides three customizable controls on a tiny 64x64 app. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mixer_applet**

Mixer Applet for the GNOME panel. From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIZI Linux**

MIZI Linux is a Korean distribution. Version 2.0 was released October 19, 2001. MIZI the company also provides Linu, which can be found in the Embedded section of this list. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MJ**

Modular Jack From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mkboot**

makes a bootdisk From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mkbootdisk**

The mkbootdisk program creates a standalone boot floppy disk for booting the running system. The created boot disk will look for the root filesystem on the device mentioned in /etc/fstab and includes an initial ramdisk image which will load any necessary SCSI modules for the system. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MkCDrec**

mkCDrec makes a bootable disaster recovery image (CDrec.iso), including backups of the Linux system to the same CD-ROM (or CD-RW) if space permits, or to a multi-volume CD-ROM set. Otherwise, the backups can be stored on another local disk, NFS disk or (remote) tape. After a disaster (disk crash or system intrusion) the system can be booted from the CD-ROM and one can restore the complete system as it was (at the time mkCDrec was run). From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
