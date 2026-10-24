
**metacharacter (shell metacharacters)**

A metacharacter is one that represents some other concept rather than itself. For example, in entering in filenames, the metacharacter '*' doesn't represent an asterisk, but instead tells the system to match on any character. For example, looking for the filename "*.txt" will look for all files ending in the real characters ".txt". On UNIX, the most important characters are "shell" metacharacters. The reason they are important is because the shell is often used by one program to spawn another. This means that input provided to the parent program will be passed to the shell, then to the child program. If a hacker can craft special input using metacharacters, the hacker may be able to cause that shell to do something unexpected. E-mail address: A classic example is a webpage containing a FORM that asks for a user's e-mail address. The software (such as a CGI script) will often just invoke the 'mail' program using the shell. By inserting shell metacharacters into the field for the email address, a hacker may be able to execute some other program on the web server. Example: Some UNIX shell metacharacters are: [] () {} ~ # $ ^ & * \ | ; <> ? ` ' | (pipe) The pipe metacharacter links two command-line programs together, causing the output from the first program to become the input into the second program. Hackers don't care about redirecting input/output, but they will use the pipe simply as a way of confusing the shell into executing a second program. When a hacker attempts to break into a webserver, one of the first things they will do is to look for all the forms on the website and provide input containing pipe characters to see if they can force the system to execute commands. ; (semicolon) Similar to the pipe metacharacter in its ability to run multiple programs at once. However, the semicolon simply launches the programs without redirecting input/output. ` (back-quote, back-tick) The backwards quote metacharacter is similar to the pipe in that it can take the output from one command and pass it another. In this case, the output of the second program is provided as command-line input into the first. $ (dollar sign) The dollar sign prefixes a variable name. Thus, the string $FOO represents the value of the variable named "FOO" rather than the letters 'F', 'O', 'O'. In particular, you'll commonly see $IFS in attacks, where the IFS variable indicates the character used to separate lines in the shell. && and || These are logical operations used in shell programming. They look at the "result" of a program and "conditionally" execute other programs. A hacker doesn't care about this intended use, but can instead use these as yet another way to execute additional commands. See also: taint, CGI From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**metacity**

A lightweight GTK2 based Window Manager. Metacity is a small (<6K lines of code) window manager, using gtk2 to do everything. As HP says, metacity is a "Boring window manager for the adult in you. Many window managers are like Marshmallow Froot Loops; Metacity is like Cheerios." From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Metafont**

a graphics programming language (like postscript) that has applications wider than just fonts. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**METAL**

Machine Evaluation and Translation Language (Siemens) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**metamail**

An implementation of MIME. Metamail is an implementation of MIME (Multi-purpose Internet Mail Extensions), a proposed standard for multimedia electronic mail on the Internet. Metamail is configurable and extensible via the "mailcap" mechanism described in an informational RFC that is a companion to the MIME document. Metamail can be used to turn virtually any mail reader program into a multimedia mail reader. For information about how to change mail readers so that they can use Metamail, please read the file `/usr/share/doc/metamail/mailers.txt.gz'. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**metamail**

Metamail is a system for handling multimedia mail, using the mailcapfile. Metamail reads the mailcap file, which tells Metamail what helper program to call in order to handle a particular type of non-text mail. Note that metamail can also add multimedia support to certain non-mail programs. Metamail should be installed if you need to add multimedia support to mail programs and some other programs, using the mailcap file. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Metcalfe's Law**

A philosophical point of view: "The power of the network increases exponentially by the number of computers connected to it. Therefore, the every computer added to the network both uses it as a resource while adding resources in a spiral of increasing value and choice." -- Dr. Bob M. Metcalfe, inventor of Ethernet, co-founder of 3Com, editor-in-chief of InfoWorld. The idea is that the power of the Internet is not simply all the websites that you can access (linear), but the power represented by everyone else also on the Internet (exponential). For example, organizations like http://www.distributed.net/ cannot only harness lots of machines in order to tackle large problems (linear), but they also can exploit the word-of-mouth on the Internet to sign up (exponential). Similarly, consider the growth in sites like http://www.slashdot.org/ that start out as hobbyist sites, but eventually blossom into large money making ventures, tossing pre-Internet-age business philosophies on their ear. Key point: Hacker attacks grow exponentially because more and more hackers are getting online (especially from 3rd world countries) and more and more resources (businesses) are getting online. Key point: The amount of computing resources a hacker can tap into from his/her computer desktop is more than the combined might of all governments and militaries. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**METDST**

Middle European Time Daylight Saving Time [+0200] (TZ, MET, MEZ) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mew**

Messaging in the Emacs World Mew is an interface to integrate - Email - MIME (Multipurpose Internet Mail Extensions) - PGP (Pretty Good Privacy) and to make it easy to view and compose them. Thread, POP biff, POP folder, and icon-based interface are supported. More information is available at http://www.Mew.org/. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mew-bin**

The external commands for Mew Mew has thrown away IM and is being implemented purely by Elisp with these external commands: - The mewencode utility encode/decode MIME objects. - The mewls utility extracts necessary fields from messages stored in folders. - The incm utility incorporates new mails from the mbox or the maildir to Mew's inbox folder. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MEZ**

MittelEuropaeische [sommer] Zeit [+0200] (TZ) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mf**

Metafont, a language for font and logo design From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MF**

Multi Frequency From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFAST**

Mwave Folded Array Signal Transform [DSP] (IBM, DSP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFC**

Microsoft Foundation Classes From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFC**

Music Feature Card (IBM, Yamaha, MIDI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFENET**

Magnetic Fusion Energy NETwork From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFG**

Mit Freundlichen Gruessen [= best wishes] From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFG**

Multi-Function Gateway From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFI**

MainFrame Interactive (IBM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFII**

Multi-Functional [keyboard] II (IBM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFIP**

Multi-Function Interoperability Processor From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFKS**

MultiFunktionales KonferenzSystem From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFLOPS**

Million FLoating-point Operations Per Second (CPU) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFM**

Modified Frequency Modulation From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mformat**

add an MSDOS filesystem to a low-level formatted floppy disk TQ From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFP**

MultiFunction Product From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mfpic**

Define Tex/LaTeX commands to draw using metafont/metapost MFpic defines a command group \mfpic...\endmfpic (optionally in LaTeX an environment mfpic) and drawing commands to be used inside this group. When TeX (or LaTeX) is run on a file containing those commands, a Metafont or MetaPost source file is created. When that file is correctly processed by Metafont (or MetaPost), and LaTeX or TeX is run again, the result is a figure in the TeX document in the location of the environment. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFS**

Macintosh File System (Apple) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFS**

Message Format Service (IBM, IMS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFS**

Mobile File Sync (IBM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFS**

MOSIX File System (MOSIX, DFSA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFT**

Master File Table (NTFS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFT**

Multiprogramming with a Fixed number of Tasks (IBM, OS, OS/MFT, OS/MVT) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mft**

translate Metafont code to TeX code for prettyprinting From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MFV**

MehrFrequenzwahlVerfahren From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mfw**

Metafont, a language for font and logo design From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MGA**

Matrox Graphics Adapter (Matrox) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MGA**

Monochrome Graphics Adapter From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mgapdesk**

X configuration tool for Matrox video card. Configuration tool for Xfree86 version 4.x to set up your X-server to support single and dual monitors. Support for Matrox Millennium G200, G400 and G450 cards. For best operation you should download the Matrox HAL library from the Matrox homepage. But this tool works without it even if it complains because the xserver can not use all config options. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mgdiff**

xdiff clone mgdiff is modeled after xdiff and provides a nice graphical interface for comparing the contents of two text files. rmgdiff recurses down two directories collating difference information and invoking mgdiff whenever two text files differ. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mgetty**

Smart Modem getty replacement Mgetty is a versatile program to handle all aspects of a modem under Unix. This package includes basic modem data capabilities. Install mgetty-fax to get the additional functionality for fax. Install mgetty-voice to get the functionality to operate voice modems. Mgetty is also configurable to select programs other than login for special connections (eg: uucico, fido or other programs) depending on the login userid. It also supports caller-id if the modem and phone line supply it, and can deny connections based on originating telephone number. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MGI**

Multi-Function Interpreter From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mgm**

A highly configurable, very gaudy system load meter MGM is the Moaning Goat Meter, a system load monitor along the lines of procmeter3 but much prettier (and with a much higher resource usage). It's written in Perl/Tk, uses a nice antialiased Helvetica font, is configurable with X resource, and can have a larger memory footprint than Emacs. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MGM**

Memory Grant Manager (Informix, DB) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mgp**

MagicPoint- an X11 based presentation tool MagicPoint is an X11 based presentation tool. It is designed to make simple presentations easy while to make complicated presentations possible. Its presentation file (whose suffix is typically .mgp) is just text so that you can create presentation files quickly with your favorite editor (e.g. Emacs). From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mgt**

a game record display/editor for the oriental game of go Mgt allows the user to examine Go game tree files in the SmartGo format. Mgt also has basic Go game tree editing capabilities and may be used to create or edit game tree files. Mailgo is a utility which manages E-mail Go games using mgt as the Go board editor. It is included in the mgt package. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MH**

Mobile Host (MHP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MH**

Modified Huffman (Fax) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mh-book**

MH & nmh: Email for Users & Programmers online book This is the book written by Jerry Peek and published by O'Reilly & Associates, Inc. This book covers MH, nmh, and several interfaces to MH including xmh, exmh and mh-e. This package is a recent snapshot of http://www.ics.uci.edu/~mh/book/ From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mh-e**

the GNU Emacs front end for MH and nmh mail user agents. This is likely a more recent version of mh-e than the one packaged with the flavor of Emacs you use. It also includes latest version of Info format documentation as well as contributed files that are not distributed with GNU Emacs: mh-alias.el - MH mail alias expansion and substitution. mh-frame.el - Open mh-e in a separate frame. The mh-e web page is http://mh-e.sourceforge.net/ From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mhc**

Message Harmonized Calendaring system MHC is designed to help those who receive most appointments via email. Using MHC, you can easily import schedule articles from emails. MHC has following features: + Simple data structure allows you to manipulate stored data in many ways. + Appointments can be made to repeat in flexible ways. + powerful but simple expression of appointments. + Multiple User Interface such as commandline/emacs/GUI/Web. MHC currently has following interfaces: + Elisp package cooperative with Mew, Wanderlust or Gnus (popular MUA in the Emacs world) (emacs/mhc.el) MHC stores schedule articles in the same form of MH; you can manipulate these messages not only by above tools but also by many other MUAs, editors, UNIX commandline tools or your own scripts. For more information, you can find at http://www.quickhack.net/mhc/ From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MHDL**

MIMIC Hardware Description Language From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MHEG**

Multimedia and Hypermedia information coding Expert Group (JTC1, ISO) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mhonarc**

Mail to HTML converter _MHonArc_ is a Perl program for converting e-mail messages as specified in RFC 822 and RFC 1521 (_MIME_) to HTML. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MHP**

Multimedia Home Platform (ETSI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MHP**

[columbia] Mobile Host Protocol From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MHPCC**

Maui High Performance Computing Center (org., USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MHS**

Message Handling System (GOSIP, X.400, Novell, SPX, IPX) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MHTML**

Messaging HyperText Markup Language (HTML) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MHTML**

MIME [e-mail encapsulation of aggregate documents, such as] HTML (MIME, HTML, RFC 2110) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MI**

Management Interface From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIA**

Missing In Action (DFUe, Usenet, IRC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIAW**

Movie In A Window From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIB**

Management Information Base (OSI, SNMP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIC**

Media Interface Connector (FDDI, PMD) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIC**

Memory in Cassette (Seagate, EEPROM, Streamer, AIT) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIC**

Message Integrity Check / Code From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIC**

Multiple Interface Connection (Kyocera) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MICA**

MODEM ISDN Channel Integration (Telebit, MODEM, ISDN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MICE**

Modular Integrated Communications Environment From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mico**

A fully compliant CORBA implementation, executables The acronym MICO expands to MICO Is CORBA. The intention of this project is to provide a freely available and fully compliant implementation of the CORBA standard. MICO has become quite popular as an OpenSource project and is widely used for different purposes. As a major milestone, MICO has been branded as CORBA compliant by the OpenGroup. Executables From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MICO**

MICO Is CORBA (ORB, CORBA, Uni Frankfurt) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**micq**

text based ICQ client with many features mICQ is a small, yet powerful console based ICQ client. It supports password changing, auto-away, creation of new accounts, and other features that makes it a very complete yet simple client. It now has complete support for the new v8 protocol. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**microcode.ctl**

Intel IA32 CPU Microcode Utility The microcode_ctl utility is a companion to the IA32 microcode driver written by Tigran Aivazian <tigran@veritas.com>. The utility has two uses: a) it decodes and sends new microcode to the kernel driver to be uploaded to Intel IA32 family processors. (Pentium Pro, PII, Celeron, PIII, Xeon, Pentium 4 etc.) b) it signals the kernel driver to release any buffers it may hold The microcode update is volatile and needs to be uploaded on each system boot i.e. it doesn't re-flash your CPU permanently, reboot and it reverts back to the old microcode. The ideal place to load microcode is in BIOS, but most vendors never update it! To enable microcode update, I need some kernel support, thus I need the linux kernel 2.2.18 or later, or 2.4.0 or later. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**microkernel**

An approach to operating systems design which puts emphasis on small modules which implement the basic features of the system kernel and can be flexibly configured. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MID**

Message IDentifier (ATM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**midentd**

identd replacement with masquerading support. An identd replacement with masquerading support. With your average identd on a masquerading firewall, if an ident request comes in for a masqueraded connection, it will return 'ERROR : NO-USER' or something along those lines. This may be quite irritating at times, with, for example, IRC servers that won't let you in if they don't get a valid ident reply. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIDI**

Musical Instruments Digital Interface (MIDI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIDL**

Microsoft Interface Definition Language (NT) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Midori**

Midori Linux, from Transmeta, is an Open Source project for delivering system software on small devices. It includes a build system, a Linux kernel with memory- and storage-conserving features, and system-level support for normal Linux software on platforms which might otherwise require custom "embedded" applications. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIDP**

Mobile Information Device Profile (J2ME) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIDPEG**

Mobile Information Device Profile Expert Group (Sun, AOL, Motorola, NEC, Nokia, Palm, Samsung, Sharp, ...) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIF**

Module Interconnection Facility (Proteus) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mifluz**

A full text inverted indexer The purpose of mifluz is to provide a C++ library to build and query a full text inverted index. It is dynamically updatable, scalable (up to 1Tb indexes), uses a controlled amount of memory, shares index files and memory cache among processes or threads and compresses index files to 50% of the raw data. The structure of the index is configurable at runtime and allows inclusion of relevance ranking information. The query functions do not require to load all the occurrences of a searched term. They consume very few resources and many searches can be run in parallel. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MIG**

Mach Interface Generator (Mach) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mig-i386-gnu**

The GNU distribution of the Mach 3.0 interface generator `MiG'. You need this tool to compile the gnumach and hurd distributions, and to compile GNU libc for the Hurd. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**migemo**

Japanese incremental search with Romaji on Emacsen migemo is a tool that supports Japanese incremental search with Romaji. It release you from heavy tasks of Kana Kanji conversion in order to search. This is Emacsen interface, that is wrapper for isearch. http://migemo.namazu.org/ From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**migemo-perl**

Japanese incremental search with Romaji on Emacsen migemo is a tool that supports Japanese incremental search with Romaji. It release you from heavy tasks of Kana Kanji conversion in order to search. This is Emacsen interface, that is wrapper for isearch. http://migemo.namazu.org/ This is obsolete version of migemo. Newer version is written in ruby. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**migrationtools**

Migration scripts for LDAP The MigrationTools are a set of Perl scripts for migrating users, groups, aliases, hosts, netgroups, networks, protocols, RPCs, and services from existing nameservices (flat files, NIS, and NetInfo) to LDAP. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MII**

Media Independent Interface From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mii-diag**

A little tool to manipulate network cards Examines and sets the MII registers of network cards. This is a general program. You can find specialized programs for several network cards in the nictools-pci and nictools-nopci packages. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mii-tool**

view, manipulate media-independent interface status From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
