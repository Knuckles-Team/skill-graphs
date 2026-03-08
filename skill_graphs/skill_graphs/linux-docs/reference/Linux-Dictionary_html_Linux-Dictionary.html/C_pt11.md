
**cron**

management of regular background processing cron is a background process (`daemon') that runs programs at regular intervals (for example, every minute, day, week or month); which processes are run and at what times are specified in the `crontab'. Users may also install crontabs so that processes are run on their behalf, though this feature can be disabled or restricted to particular users. Output from the commands is usually mailed to the system administrator (or to the user in question); you should probably install a mail system as well so that you can receive these messages. This cron package is configured by default to do various standard system maintenance tasks, such as ensuring that logfiles do not grow endlessly and overflow the disk. The lockfile-progs package is only a "Suggests" because of the poor way that dselect handles "Recommends", but I do strongly suggest that you install it; it prevents /etc/cron.daily/standard from running multiple times if something gets jammed. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**cron**

On UNIX, the cron daemon automated background tasks (such as backups or rotating the logs). It is really the simplest of programs; it reads instructions from a file and executes the appropriate programs at the scheduled time. Key point: When the machine is compromised, intruders will often put backdoor jobs into the crontab. When the victim tries to clean up his/her machine, the jobs in the crontab will run giving the intruder control again. This sort of thing happened in the famous attack against the New York Times; they kept cleaning up the machine, but cron kept giving control back to the intruder. Typically, these jobs would run during the we hours of the morning when nobody is looking. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**cron-apt**

Automatic update of packages using apt This package contains a tool that is run by a cron job at regular intervals. By default it just updates the package list and download new packages without installing. You can instruct it to run anything that you can do with apt-get. It also sends mail (configurable) to the system administrator on errors. Observe that this tool is a security risk, so you should not set it to do more than necessary (automatic upgrade of all packages is NOT recommended). From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**cronolog**

Logfile rotator for web servers A simple program that reads log messages from its input and writes them to a set of output files, the names of which are constructed using template and the current date and time. The template uses the same format specifiers as the Unix date command (which are the same as the standard C strftime library function). It intended to be used in conjunction with a Web server, such as Apache, to split the access log into daily or monthly logs: TransferLog "|/usr/sbin/cronolog /var/log/apache/%Y/access.%Y.%m.%d.log" A cronosplit script is also included, to convert existing traditionally-rotated logs into this rotation format. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**cronosii**

fast, light-weight and functional GNOME e-mail client Cronos II is a powerful GNOME e-mail client. It has been designed to be fast, light, user-friendly, yet strong. Its strength resides in the extended configuration, that the user can manage dynamically without touching any code at all. The friendly aspect resides in the intuitive interface and in the simplicity of the environment and in the full compatibility with the GNOME Project. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**crontab**

A short name for file /var/lib/crontab, which contains a list of Linux commands to be performed at specific times. A system administrator can use crontab as an automatic timer to trigger the initiation of important jobs. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**crontabs**

The crontabs package contains root crontab files. Crontab is theprogram used to install, uninstall or list the tables used to drive thecron daemon. The cron daemon checks the crontab files to see when particular commands are scheduled to be executed. If commands are scheduled, it executes them. Crontabs handles a basic system function, so it should be installed on your system. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**crossfire-client**

Base Client Side of the game Crossfire. Crossfire is "a multiplayer graphical arcade and adventure game made for the X environment. It has certain flavours from other games, especially Gauntlet (TM) and Nethack/Moria. Any number of players can move around in their own window, finding and using items and battle monsters. They can choose to cooperate or compete in the same 'world'." This program can operate stand alone if you have access to a remote server. Playing with sounds will require rplay, also. This package contains no binaries From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**crossfire-server**

Server for Crossfire Games This is the server program for the crossfire client Crossfire is a multiplayer graphical arcade and adventure game made for the X environment. It has certain flavours from other games, especially Gauntlet (TM) and Nethack/Moria. Any number of players can move around in their own window, finding and using items and battle monsters. They can choose to cooperate or compete in the same "world". From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CRP**

Candidate Rendezvous Point (PIM, RP, Multicast), "C-RP" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CRP**

Common Reference Platform (PowerPC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CRPC**

Center for Research on Parallel Computation (STC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CRS**

Cell Relay Service (UNI, ATM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CRT**

Cathode Ray Tube From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CRT**

Computer Technology Research [corporation] (provider) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CRTC**

Cathode Ray Tube Controller (EGA, VGA, MCGA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**cruft**

Find any cruft built up on your system cruft is a program to look over your system for anything that shouldn't be there, but is; or for anything that should be there, but isn't. It bases most of its results on dpkg's database, as well as a list of `extra files' that can appear during the lifetime of various packages. cruft is still in pre-release; your assistance in improving its accuracy and performance is appreciated. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CRUX**

CRUX is a lightweight, i686-optimized Linux distribution targeted at experienced Linux users. The primary focus of this distribution is "keep it simple", which is reflected in a simple tar.gz-based package system, BSD-style initscripts, and a relatively small collection of trimmed packages. The secondary focus is utilization of new Linux features and recent tools and libraries. Version 1.1 was released March 24, 2003. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**crypt++el**

Emacs-Lisp Code for handling compressed and encrypted files Code for handling all sorts of compressed and encrypted files like: .gz, .tar.gz, .Z, .zip, PGP etc. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**cryptcat**

TCP/IP swiss army knife extended with twofish encryption Cryptcat is a simple Unix utility which reads and writes data across network connections, using TCP or UDP protocol while encrypting the data being transmitted. It is designed to be a reliable "back-end" tool that can be used directly or easily driven by other programs and scripts. At the same time, it is a feature-rich network debugging and exploration tool, since it can create almost any kind of connection you would need and has several interesting built-in capabilities. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Cryptography**

The study of codes, cryptography refers to the making and breaking of algorithms to conceal or otherwise encrypt information. One of the most popular internet encryption schemes is PGP. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**crystalspace**

Multiplatform 3D Game Development Kit Crystal Space is a free 3D game toolkit. It can be used for a variety of 3D visualization tasks. Many people will probably be interested in using Crystal Space as the basis of a 3D game, for which it is well suited. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CS**

Carrier Selection From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CS**

Chip Select (IC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CS**

Client/Server, "C/S" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CS**

Code Segment [register] (CPU, Intel, assembler) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CS**

Coding Scheme (GPRS, mobile-systems) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CS**

Computer Science From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CS**

Controlled Slip [error event] (DS1/E1) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CS**

Convergence Sublayer (ATM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CS1**

Capability Set 1 (IN), "CS-1" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CS2**

Capability Set 2 (IN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSA**

Callpath Service Architecture (IBM, CTI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSA**

Client Service Agent From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSA**

Configuration Status Accounting From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSAPI**

Common Speller Application Program Interface (API) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSC**

Computer Sciences Corporation (provider) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSCC**

Concurrent SuperComputing Consortium (org.) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSCD**

Caldera Systems Curriculum Developers (Caldera) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**cscope**

Interactively examine a C program source cscope is an interactive, screen-oriented tool that allows the user to browse through C source files for specified elements of code. Open-Sourced by: The Santa Cruz Operation, Inc. (SCO) Maintainer: Petr Sorfa <petr@users.sourceforge.net> Home Page: http://cscope.sourceforge.net/ From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSCSI**

Canadian Society for the Computational Studies of Intelligence (org., Canada, AI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSCW**

Computer Supported Cooperative Work From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSD**

Control flow Specification Diagram (CASE) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSD**

Corrective Service Diskettes (IBM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSD**

Customer Specific Dictionaries From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSDC**

Circuit Switched Digital Capability From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSDC**

Code Segment Descriptor Cache [register] (CS, Intel, CPU) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSE**

Client-Server Environment From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSEIA**

[conference on] Computer Support for Environmental Impact Assessment (IFIP, conference) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSEL**

Cable SELect (EIDE, HD) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSELT**

Centro Studi E Laboratori Telecomunicazioni [s.p.a.] (org., Italy) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSEM**

Centre Suisse d'Electronique et de Microtecnique (org., Switzerland) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSES**

C-bit Severely Errored Seconds (DS3/E3) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSG**

Constructive Solid Geometry (CAD, CAM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSH**

C SHell (Unix, BSD, Shell) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSH**

Complementary Software House (DEC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**csh**

Shell with C-like syntax, standard login shell on BSD systems. The C shell was originally written at UCB to overcome limitations in the Bourne shell. Its flexibility and comfort (at that time) quickly made it the shell of choice until more advanced shells like ksh, bash, zsh or tcsh appeared. Most of the latter incorporate features original to csh. This package is based on current OpenBSD sources. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSI**

CompuServe Incorporated (ISP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSI**

Convergence Sublayer Indication (ATM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSIC**

Customer Specific Integrated Circuit (IC, RL) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSID**

Caller Station IDentification (Fax) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSIDS**

Central command/Southern command Integrated Data System (mil., USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSII**

Center for Systems Interoperability and Integration (org., ???) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSIRO**

Commonwealth Scientific and Industrial Research Organization (org., UK) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSIS**

Central Schengen Information System (SIS, Europe, Strasbourg) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSKI**

Ceska Spolecnost pro Kybernetiku a Informatiku (org., Tschechien) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSL**

Callable Services Library (IBM, VM/ESA, CMS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSL**

Computer SoLutions [software gmbh] (Haendler) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSLIP**

Compressed [headers] Serial Line Internet Protocol (SLIP, IP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSMA**

Carrier Sense Multiple Access From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSMACA**

Carrier Sense Multiple Access with Collision Avoidance, "CSMA/CA" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSMACD**

Carrier Sense Multiple Access with Collision Detection (IEEE 802.3, ethernet, CSMA/CD), "CSMA/CD" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**csmash**

CannonSmash, a table tennis simulation game CannonSmash is a funny 3D table tennis game. It takes a while to get your hand at ease with the mouse+keyboard manipulations. But once you're used to the technique, you can feel like playing a real game. It is playable against the computer or through a network. Since csmash relies on OpenGL-compatible rendering, it is best experienced with a 3D accelerator card, although software rendering in wireframe mode should be sustainable. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSMS**

C Specific Media Support (NEST, MLID, Novell) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSMUX**

Circuit Switching MUltipleXer (FDDI), "CS-MUX" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSN**

Card Select Number (PNP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSNET**

Computer + Science NETwork (USA, network, BITNET) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSP**

Centro Supercacolo Piemonte (org., Italy, HPC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSP**

Chip Scale Package (IC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSP**

Communicating Sequential Processes From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSP**

Cross System Product (IBM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSPDN**

Circuit Switched Public Data Network (IN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSPDU**

Convergence Sublayer Protocol Data Unit (ATM, PDU), "CS PDU" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**csplit**

split a file into sections determined by context lines From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSPP**

Computer Systems Policy Project [group] (org., USA. manufacturer) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSR**

Cell misSequenced Ratio (ATM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSR**

Cell Switch Router (Toshiba) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSRAM**

Clock Synchronous Random Access Memory (RAM, IC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSS**

Cascading Style Sheets (HTML, WWW, JavaScript) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSS**

Cascading Style Sheets: A simple mechanism for adding style (e.g. fonts, colors, spacing) to Web documents. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSS**

Computer Sub System From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSS**

Content Scrambling System (DVD, Matsushita, IBM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSS**

Controlled Slip Seconds (DS1/E1) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSS**

Customer Switching System From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSS (Cascading Style Sheet)**

A standard for specifying the appearance of text and other elements. CSS was developed for use with HTML in Web pages but is also used in other situations, notably in applications built using XPFE. CSS is typically used to provide a single "library" of styles that are used over and over throughout a large number of related documents, as in a web site. A CSS file might specify that all numbered lists are to appear in italics. By changing that single specification the look of a large number of documents can be easily changed. From Matisse <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**cssc**

Clone of the Unix SCCS revision-control system. SCCS is a de-facto standard shipped with most commercial Unices, and is the pre-file revision-control system under many project-wide revision-control systems. This software is under development and not all features are implemented at this time. GNU-based systems use RCS instead of SCCS. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CST**

Central Standard Time [-0600] (TZ, CDT, USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSTA**

Computer Supported Telecommunications Applications (ECMA, CTI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSTB**

Computer Science and Technology Board (org., NRC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSTC**

Computer Security Technology Center (org., CIAC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSTO**

Computing Systems Technology Office (org., ARPA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**cstocs**

Recoding utility and Czech sorter. This is a utility which allows you to re-encode files between various encodings and sort Czech data. Some main features: - Written in Perl, providing appropriate Perl modules. - Supported encodings: ASCII, ISO-8859-1, ISO-8859-2, Microsoft cp1250 and cp1252, Mac, MacCE, PC Latin 2, Koi8-CS and TeX Cork (T1). - You can create your own encoding definition files and use them for recoding to any other defined encoding. - Single to single or single to many chars recodings are supported. - Sophisticated sorting algorithm for Czech. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSTR**

Centre for Speech Technology Research From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**cstr**

print out string literals in C source code From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSTS**

Computer Supported Telecommunications Standard From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSU**

Channel Service Unit (ATM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSU/DSU (Customer Service Unit/Digital Service Unit)**

Sometimes called a digital modem. It does not modulate or demodulate, but converts a computer's uni-polar digital signal to a bi-polar digital signal for transmission over ISDN lines. From Glossary of Distance Education and Internet Terminology <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSUNET**

California State University NETwork (network, USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CSV**

Comma Separated Values From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CT**

Chipcard Terminal (ICC, CT) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CT**

Chips & Technologies (manufacturer), "C&T" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CT**

[magazin fuer] Computer Technique, "c't" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ctags**

The ctags program generate an index (or "tag") file for C, C++, Eiffel,Fortran, and Java language objects found in files. This tag file allows these items to be quickly and easily located by a text editor or other utility. A "tag" signifies a language object for which an index entry is available (or, alternatively, the index entry created for that object). Alternatively, ctags can generate a cross reference file which lists, inhuman readable form, information about the various source objects found in a set of language files. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CTAN**

Comprehensive Tex Archive Network (TeX, FTP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CTAPI**

Chipcard Terminal Application Program Interface (ICC, CT, API), "CT-API" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CTB**

Communication ToolBox (Apple) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CTCA**

Channel To Channel Adapter (IBM, System/370) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CTCP**

An acronym for Client-To-Client-Protocol, see IRC. From KADOWKEV <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CTCP**

Client To Client Protocol (IRC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CTCPEC**

Canadian Trusted Computer Product Evaluation Criteria (Canada) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CTD**

Cell Transfer Delay (UNI, ATM, QOS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CTE**

Compliance Test and Evaluation, "CT & E" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**CTERM**

Command TERMinal (DEC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**cthumb**

A program to generate themable Web picture albums cthumb allows you to create themable web picture albums, i.e. collections of digital pictures, with small thumbnails of your pictures and with captions. In addition, it optionally allows you to have several views of the collection of pictures. An album is composed of a series of pages, each composed of a collection of pictures. For each page (and each picture), you can have several annotations per picture. cthumb will generate several versions of the page, for each annotation type. You can customize almost everything in the way the albums look on the screen, from the size of the thumbnails to the background and foreground colors, the border colors, whether you want film-strips, etc. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
