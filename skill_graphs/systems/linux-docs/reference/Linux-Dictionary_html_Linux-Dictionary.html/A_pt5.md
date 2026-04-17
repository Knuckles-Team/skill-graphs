
**ALTS**

Association for Local Telecommunications Services (org., USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ALU**

Arithmetic and Logic Unit (CPU) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AM**

Active Matrix (LCD) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AM**

Amplitude Modulation From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AM**

Asynchronous Mode From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**am-utils**

The 4.4BSD automounter. Amd is an automounter--it mounts file systems "on demand" when they are first referenced and unmounts them after a period of inactivity. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMA**

Automatic Message Accounting From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMACS**

AMA Collection System (AMA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**amanda-client**

Advanced Maryland Automatic Network Disk Archiver (Client) Amanda is a backup system designed to archive many computers on a network to a single large-capacity tape drive. This package is suitable for large amounts of data to backup. For smaller solutions take a look at afbackup, tob, taper, ... Features: * will back up multiple machines in parallel to a holding disk, blasting finished dumps one by one to tape as fast as we can write files to tape. For example, a ~2 Gb 8mm tape on a ~240K/s interface to a host with a large holding disk can be filled by Amanda in under 4 hours. * built on top of standard backup software: Unix dump/restore, and later GNU Tar and others. * does simple tape management: will not overwrite the wrong tape. * supports tape changers via a generic interface. Easily customizable to any type of tape carousel, robot, or stacker that can be controlled via the unix command line. * for a restore, tells you what tapes you need, and finds the proper backup image on the tape for you. * recovers gracefully from errors, including down or hung machines. * reports results, including all errors in detail, in email to operators. * will dynamically adjust backup schedule to keep within constraints: no more juggling by hand when adding disks and computers to network. * includes a pre-run checker program, that conducts sanity checks on both the tape server host and all the client hosts (in parallel), and will send an e-mail report of any problems that could cause the backups to fail. * can compress dumps before sending or after sending over the net, with either compress or gzip. * can optionally synchronize with external backups, for those large timesharing computers where you want to do full dumps when the system is down in single-user mode (since BSD dump is not reliable on active filesystems): Amanda will still do your daily dumps. * lots of other options; Amanda is very configurable. THIS PACKAGE RELIES ON A RUNNING AMANDA SERVER IN YOUR NETWORK. For a quick start read the README.client.debian in /usr/share/doc/amanda-client. Explanation of suggested programs: - awk and gnuplot are needed for plotting statistics of backups From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**amanda-common**

Advanced Maryland Automatic Network Disk Archiver (Libs) This package contains libraries required by the amanda client and server packages. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**amanda-server**

Advanced Maryland Automatic Network Disk Archiver (Server) Amanda is a backup system designed to archive many computers on a network to a single large-capacity tape drive. This package is suitable for large amounts of data to backup. For smaller solutions take a look at afbackup, tob, taper, ... Features: * will back up multiple machines in parallel to a holding disk, blasting finished dumps one by one to tape as fast as we can write files to tape. For example, a ~2 Gb 8mm tape on a ~240K/s interface to a host with a large holding disk can be filled by Amanda in under 4 hours. * built on top of standard backup software: Unix dump/restore, and later GNU Tar and others. * does simple tape management: will not overwrite the wrong tape. * supports tape changers via a generic interface. Easily customizable to any type of tape carousel, robot, or stacker that can be controlled via the unix command line. * for a restore, tells you what tapes you need, and finds the proper backup image on the tape for you. * recovers gracefully from errors, including down or hung machines. * reports results, including all errors in detail, in email to operators. * will dynamically adjust backup schedule to keep within constraints: no more juggling by hand when adding disks and computers to network. * includes a pre-run checker program, that conducts sanity checks on both the tape server host and all the client hosts (in parallel), and will send an e-mail report of any problems that could cause the backups to fail. * can compress dumps before sending or after sending over the net, with either compress or gzip. * can optionally synchronize with external backups, for those large timesharing computers where you want to do full dumps when the system is down in single-user mode (since BSD dump is not reliable on active filesystems): Amanda will still do your daily dumps. * lots of other options; Amanda is very configurable. For a quick start read the README.server.debian in /usr/share/doc/amanda. Explanation of suggested programs: - perl is needed for some non essential server utilities - awk and gnuplot are needed for plotting statistics of backups - to backup the tape server, you need to install the client too - /usr/bin/Mail from mailx is used by amcheck to mail info about which tape is needed next, etc From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMAP**

As Much As Possible (DFUe, Usenet, IRC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**amap**

Networt protocol probing tool Amap allows you to probe IP ports for running protocols, ignoring the port number. It does this by sending probe packets to the port and analyzing the responses. This will allow you to find services running on non-standard ports. Having nmap installed is suggested, since amap cannot scan for open ports (but there is an option to import nmap's output). From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMARC**

AMA Recording Center (AMA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMASE**

AMA Standard Entry (AMA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMAT**

AMA Transmitter (AMA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**amateurs**

GTK+ based window manager AMATEURS is a GTK+ based Window Manager. It has some interesting features like: * It is written with GTK * You can make "window group" and manipulate windows which belong to the group together. * You can edit the title bar strings. * Configuration file has an XML syntax (implementation is not so stable nor complete, though). * You can apply the GTK+ theme to the window manager. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMATPS**

AMA TeleProcessing System (AMA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**amavis-postfix**

Interface between MTA and virus scanner. AMaViS is a script that interfaces a mail transport agent (MTA) with one or more virus scanners. AMaViS supports MTAs are exim, qmail, postfix, and sendmail, although this version has been built with only postfix support. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**amaya**

Graphical HTML Editor from w3.org Amaya is a WYSIWYG HTML Editor, based on the thot toolkit developed at INRIA. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMCD**

Active Matrix Color Display (AMD, LCD) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMCD**

Activity Monitoring Completion Detection From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMD**

Active Matrix Display (LCD) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMD**

Advanced MicroDevices [inc.] (manufacturer) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AME**

Advanced Metal Evaporated [tape] (Seagate, Streamer) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AME**

Advanced Modeling Extension (AutoCAD) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ame**

hosts. These tools will provide you with the IP addresses for given host names, as well as other information about registered domains and network addresses.You should install bind-utils if you need to get information from DNS nameservers. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMEL**

Active Matrix Electro Luminescent (AMD, LCD) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**American Standard Code for Information Interchange (ASCII)**

Alphanumeric characters are represented by numbers ranging from 0 to 127 and are translated into a 7-bit binary code. ASCII allows for easy transfer of text-only files between different kinds of computers. From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMH**

Automated Material Handling From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMHS**

Automated Message Handling System (MHS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMI**

Alternate Mark Inversion (ISDN, T1) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMI**

American Megatrends Incorporation (manufacturer) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ami**

An X input method server for Korean text input Ami is an X input method server for Korean text input. Hangul or Hanja Korean text can be input with Ami, which responds the requests from XIM compliant applications. In this package, Ami has been built as a standalone version and a WindowMaker dock. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMI**

ATM Management Interface (ForeRunner) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMIA**

American Medical Informatics Association (org., USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMIA**

Australian Medical Informatics Association (org., Australia) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMIC**

Apple Memory-mapped I/O Controller (Apple) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMIGADE**

Amiga Digital Environment (Amiga), "AmigaDE" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMIGOS**

Advanced Mobile Integration in General Operating Systems From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMIS**

Audio Message Interface Standard From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AML**

ACPI Machine Language (ACPI, ASL, BIOS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMLCD**

Active Matrix Liquid Crystal Display (AMD, LCD) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMMA**

Advanced Memory Management Architecture From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMME**

Automated Multi-Media Exchange From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMNET**

Allgemeines Mailbox NETzwerk (BBS, network) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMOK**

A Modular Operating Kernel (OS, Cray) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**amor**

a KDE creature for your desktop AMOR stands for Amusing Misuse Of Resources. It provides several different characters who prance around your X screen doing tricks and giving you tips. This package is part of the official KDE toys module. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMOS**

Alpha Microsystems Operating System (OS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMPE**

Automated Message Processing Exchange From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**amphetamine**

jump'n run game that offers some unique visual effects Amphetamine is an exciting Jump'n run game that offers some unique visual effects like colored lighting, fogging and coronas. You must fight eleven evil monsters with your magic weapons. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**amplifier**

Any type of system on the network that can be used to amplify (increase) the the size of traffic is known as an amplifier. Example: The classic example is the smurf amplifier. An attacker spoofs the address of a victim and sends directed broadcasts to the amplifier, which then sends hundreds of replies back to the victim. Thus, it only costs the attacker a single packet to send many packets to the victim. Example: A more subtle attack is the use of DNS. The DNS response packet can be much larger than the request. This allows an attacker to flood the victim with large packets at the cost of small packets. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMPS**

Advanced Mobile Phone Service (mobile-systems, Motorola) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMR**

Audio MODEM Riser [slot] (Intel) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMS**

Advanced Monitor System (OS, DEC, PDP 9, PDP 15) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMS**

American Mathematical Society (org., USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMS**

Andrew Mail / Message System (Unix) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMS**

Asymmetric Multiprocessing System From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMS**

AUTODIN Mail Server (AUTODIN, mil., USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMSDOS**

AMStrad Disk Operating System (Amstrad, OS), "AMS-DOS" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**amstex**

structured text formatting and typesetting From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMT**

Active Matrix Technology (AMD, LDC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMT**

Apple Media Toolkit (Apple) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMTF**

Average Modulation Transfer Function From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMTFT**

Active Matrix Thin Film Transistor (AMD, LCD, TFT) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMTPE**

Apple Media Tool Programming Environment (Apple), "AMT PE" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AMWG**

Architecture Methodology Working Group (org., DISA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AN**

Access Node From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AN**

Alternating Network From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**an**

Very fast anagram generator. Generates anagrams for a phrase supplied by the user, the words used in the anagram are taken from a specified dictionary which should contain one word per line (default:/usr/share/dict/words). Appears to be up to 10 times faster than wordplay, especially for longer phrases. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**anacron**

a cron-like program that doesn't go by time Anacron (like `anac(h)ronistic') is a periodic command scheduler. It executes commands at intervals specified in days. Unlike cron, it does not assume that the system is running continuously. It can therefore be used to control the execution of daily, weekly and monthly jobs (or anything with a period of n days), on systems that don't run 24 hours a day. When installed and configured properly, Anacron will make sure that the commands are run at the specified intervals as closely as machine-uptime permits. This package is pre-configured to execute the daily jobs of the Debian system. You should install this program if your system isn't powered on 24 hours a day to make sure the maintenance jobs of other Debian packages are executed each day. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**anacron**

Anacron (like `anac(h)ronistic') is a periodic command scheduler. It executes commands at intervals specified in days. Unlike cron, it does not assume that the system is running continuously. It can therefore be used to control the execution of daily, weekly, and monthly jobs (or anything with a period of n days), on systems that do not run 24 hours a day. When installed and configured properly, Anacron will make sure that the commands are run at the specifiedintervals as closely as machine-uptime permits. This package is pre-configured to execute the daily jobs of the RedHat Linux system. You should install this program if your system is not powered on 24 hours a day to make sure the maintenance jobs ofother Red Hat Linux packages are executed periodically. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**analog**

analyzes logfiles from web servers Analog is a fast logfile processor that generates usage statistic reports for your web server. Features: * It's fast. Very fast. It can process millions of lines per minute. * It's very scalable. * It's very flexible. The default output will be satisfactory for most people, but there are hundreds of options producing 32 different reports for those who want to do things differently. * It can output in many different languages, and 4 output formats. * It produces attractive output that complies with the HTML spec (and so can be read on any browser). * It can read logfiles in almost any format. * It can be run at the command line or from a web form interface. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**anarchism**

An exhaustive exploration of Anarchist theory and practice. The Anarchist FAQ is an excellent source of information regarding Anarchist (libertarian socialist) theory and practice. It covers all major topics, from the basics of Anarchism to very specific discussions of politics, social organization, and economics. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANBU**

ANlagenBUchhaltung From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANCS**

AT&T Netware Connect Services (AT&T, Netware) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**and**

Auto Nice Daemon The auto nice daemon activates itself in certain intervals and renices jobs according to their priority and CPU usage. Jobs owned by root are left alone. Jobs are never increased in their priority. The renice intervals can be adjusted as well as the default nice level and the activation intervals. A priority database stores user/group/job tuples along with their renice values for three CPU usage time ranges. Negative nice levels are interpreted as signals to be sent to a process, triggered by CPU usage; this way, Netscapes going berserk can be killed automatically. The strategy for searching the priority database can be configured. AND also provides network-wide configuration files with host-specific sections, as well as wildcard/regexp support for commands in the priority database. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**AND**

Architecture Neutral Distribution Format (OSF) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANFSCD**

And Now For Something Completely Different (slang, Usenet, IRC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**angle brackets**

n. Either of the characters < (ASCII 0111100) and > (ASCII 0111110) (ASCII less-than or greater-than signs). Typographers in the Real World use angle brackets which are either taller and slimmer (the ISO `Bra' and `Ket' characters), or significantly smaller (single or double guillemets) than the less-than and greater-than signs. See broket, ASCII. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANHR**

Access Node Hub Router (AN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANI**

Automatic Number Identification From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**animals**

Traditional AI animal guessing engine using a binary tree DB You think of an animal, and this package tries to guess it... when it's wrong, you teach it about your animal. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**anjuta**

A GNOME development IDE, for C/C++. Anjuta is a GNOME development IDE and can be used to create either GNOME/Gtk+ applications with glade or glade-gnome or can be used for creating generic applications. It is designed for use with C/C++ and therefore features an easy to use debugger and compilation environment. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANMA**

Apple Network Managers Association (org., Apple) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANMP**

Advanced ??? Network Management Protocol From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANN**

Artificial Neural Networks (NN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**anonymous FTP**

A means of transferring and obtaining files that are available for public download from FTP sites. The publicly available files are usually kept in a directory called /pub/. See File Transfer Protocol (FTP). From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**anonymous FTP**

A method of file transfer that allows you to log in to an FTP server as a guest. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**anonymous FTP**

Access to FTP servers with an account name of "anonymous" or "ftp" (or sometimes "guest"). When you access FTP URLs with your web browser, it will automatically use anonymous FTP. This means that conceptually, anonymous FTP provides access similar to standard HTTP. However, there is a slight difference. Anonymous FTP servers are frequently misconfigured to allow for anonymous write access to the same directories as read access. Hackers regularly scan the Internet looking for anonymous FTP servers that they can use as drop-off spots for porn and warez. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANR**

Access Node Router From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANS**

Advanced Network & Services Inc. (IBM, MCI. Merit, NFSnet) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANS**

American National Standard (ANSI, ISO, USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANSA**

Advanced Networked Systems Architecture (ISA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANSI**

American National Standard Institute (org., USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANSI (American National Standards Institute)**

A standards body made up of industry representatives. For infosec purposes, the two interesting areas are the X9 standards for financial/banking, and the X12 standards for EDI (also governing health-care transactions). Contrast: ANSI is the American representative to the ISO. ANSI is made up of industry, whereas NIST specifies standards only for use within government. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ANSI /an'see/**

1. n. [techspeak] The American National Standards Institute. ANSI, along with the International Organization for Standards (ISO), standardized the C programming language (see K&R, Classic C), and promulgates many other important software standards. 2. n. [techspeak] A terminal may be said to be `ANSI' if it meets the ANSI X3.64 standard for terminal control. Unfortunately, this standard was both over-complicated and too permissive. It has been retired and replaced by the ECMA-48 standard, which shares both flaws. 3. n. [BBS jargon] The set of screen-painting codes that most MS-DOS and Amiga computers accept. This comes from the ANSI.SYS device driver that must be loaded on an MS-DOS computer to view such codes. Unfortunately, neither DOS ANSI nor the BBS ANSIs derived from it exactly match the ANSI X3.64 terminal standard. For example, the ESC-[1m code turns on the bold highlight on large machines, but in IBM PC/MS-DOS ANSI, it turns on `intense' (bright) colors. Also, in BBS-land, the term `ANSI' is often used to imply that a particular computer uses or can emulate the IBM high-half character set from MS-DOS. Particular use depends on context. Occasionally, the vanilla ASCII character set is used with the color codes, but on BBSs, ANSI and `IBM characters' tend to go together. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
