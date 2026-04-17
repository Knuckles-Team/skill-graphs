#  M

**m-tx**

A simple music-from-text language for use with MusiXTeX M-Tx is a music-from-text language designed to look as much as possible like printed music. Here is some typical input code: ------------------------------------------------------------------------ Title: Net soos ek is Composer: Charlotte Elliott Style: SATB Sharps: 2 Meter: 3/4 PMX: w190m Space: 9 @+5 b4 b b | b2d | a4 a a | a2d | d4 e- f | g2 e4 | d2d of |] L: Net soos ek is, net soos ek is, O Lam van God, ek kom. d4s g f | e2d | e4 f e | d2d | d4 dr d | d2 c4 | d2d |] @^+5 rp | b4 e d | c2d | a4 d c | ( b2d | b2 ) g4 | f2d |] LT: Net soos ek is, O Lam van God, ek kom. a4 a a | g2d | g4 g g | f2d | b4- g+ f | e2 a4- | d2d ofd |] L: Net soos ek is, net soos ek is, O Lam van God, ek kom. ------------------------------------------------------------------------ To run M-Tx, you also need MusiXTeX, musixlyr and PMX, all available as Debian packages. Author: Dirk Laurie <dirk@calvyn.puk.ac.za> From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**m2c**

Modula-2 translator (compiler) m2c is a Modula-2 translator. The translator supports Modula-2 versions described in 3rd and 4th editions of famous Wirth's book _Programming_in_Modula-2_. (Note: This is not current Modula-2 ISO standard.) High portability of the translator is achieved by intermediate translation into C. The translator is aimed to be used on Unixes of different flavours. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**m4**

A GNU implementation of the traditional UNIX macro processor. M4 is useful for writing text files which can be logically parsed, and is used by many programs as part of their build process. M4 has built-in functions for including files, running shell commands, doing arithmetic, etc. The autoconf program needs m4 for generating configure scripts, but not for running configure scripts. Install m4 if you need a macro processor. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**m4**

a macro processing language GNU `m4' is an implementation of the traditional UNIX macro processor. It is mostly SVR4 compatible, although it has some extensions (for example, handling more than 9 positional parameters to macros). `m4' also has builtin functions for including files, running shell commands, doing arithmetic, etc. Autoconf needs GNU `m4' for generating `configure' scripts, but not for running them. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**m68k-vme-tftplilo**

Linux kernel TFTP boot loader for m68k VME processor boards. Tftplilo is a highly configurable kernel and ramdisk network boot loader for BVM and Motorola m68k VME processor boards. It provides a mechanism for one or more diskless machines to interactively select a kernel boot configuration from a set of configurations defined in a single text configuration file that is transferred from the host tftp server. Each defined configuration specifies things such as Linux kernel and initial ramdisk file names which are then also transferred from the host tftp server. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MAC**

Mandatory Access Control (MLS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MAC**

Media Access Control (ISO, OSI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MAC**

Membership Advisory Committee (ICANN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MAC**

Message Authentication Code (SSL, SRT, cryptography) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MAC (Message Authentication Code)**

A specific type of message digest where the secret key is included as part of the fingerprint. Whereas a normal digest consists of a hash(data), the MAC consists of a hash(key + data). Contrast: The most common form is actually HMAC (hash MAC) that uses the algorithm hash(key + hash(key + data)). From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MAC address**

Every piece of Ethernet hardware has a unique number assigned to it called it's MAC address. Remember that Ethernet is used locally to connect you to the Internet, and you share the local network with many other people. The MAC address is used by your local Internet router in order to direct your traffic to you rather than somebody else in your local area. Key point: The MAC address is 6-bytes long, and must be unique. In order to guarantee uniqueness, equipment vendors are assigned a unique 3-byte prefix, and they then assign their own 3-byte suffix. Thus, the first 3-bytes of a MAC address identifies what kind of hardware you have (3Com, Cisco, Intel, etc.). Key point: The uniqueness property of MAC addresses has interesting implications. It was an important clue in tracking down David Smith (the Melissa author). From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MACH**

Multilayer ACtuator Head From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Machine language**

The native binary language recognised and executed by a computer's central procsessing unit (CPU). Machine language, a low-level language symbolised by 0s and 1s, is extremely difficult to use and read. See assembly language and high-level programming language. From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MACID**

Media Access Control IDentifier, "MAC-ID" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MACOS**

MACintosh Operating System (Apple, OS), "MacOS" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**macro**

/mak'roh/ n. [techspeak] A name (possibly followed by a formal arg list) that is equated to a text or symbolic expression to which it is to be expanded (possibly with the substitution of actual arguments) by a macro expander. This definition can be found in any technical dictionary; what those won't tell you is how the hackish connotations of the term have changed over time. The term `macro' originated in early assemblers, which encouraged the use of macros as a structuring and information-hiding device. During the early 1970s, macro assemblers became ubiquitous, and sometimes quite as powerful and expensive as HLLs, only to fall from favor as improving compiler technology marginalized assembler programming (see languages of choice). Nowadays the term is most often used in connection with the C preprocessor, LISP, or one of several special-purpose languages built around a macro-expansion facility (such as TeX or Unix's [nt]roff suite). Indeed, the meaning has drifted enough that the collective `macros' is now sometimes used for code in any special-purpose application control language (whether or not the language is actually translated by text expansion), and for macro-like entities such as the `keyboard macros' supported in some text editors (and PC TSR or Macintosh INIT/CDEV keyboard enhancers). From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**macro**

A command that incorporates a set of other commands. You custom design a command, called a macro, from existing commands. Both the vi editor and the nroff and troff formatters use macros. The mm macro package described in this book is an example of a large collection of nroff and troff macros. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Macro**

A program consisting of recorded keystrokes and an application's command language that, when run within the application, executes the keystrokes and commands to accomplish a task. Macros can automate tedious and often-repeated tasks (such as saving and backing up a file to a floppy) or create special menus to speed data entry. Some programs provide a macro-recording mode in which the program records your keystrokes and then saves the recording as a macro. Others provide a built-in macro editor, where you type and edit macro commands directly to create IF/THEN/ELSE statements and DO/WHILE loops. From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Macro**

A set of instructions stored in an executable form. Macros may be application specific (such as a spreadsheet or word processing macro that performs specific steps within that program) or general-purpose (for example, a keyboard macro that types in a user ID when Ctrl-U is pressed on the keyboard). From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**macro- pref.**

Large. Opposite of micro-. In the mainstream and among other technical cultures (for example, medical people) this competes with the prefix mega-, but hackers tend to restrict the latter to quantification. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MACS**

Manufacturing Application Control System (SNI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MACS**

MODEM Access Control System (MODEM, DES, cryptography), "M.A.C.S." From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**macutils**

Set of tools to deal with specially encoded Macintosh files macutils is a package that contains a number of utilities that deal with Macintosh files on a Unix system. This is useful for converting BinHex-encoded files to the smaller MacBinary format before transferring them to a Mac. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MAD**

Memory Address Driver strength (BIOS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MAD**

Message Address Directory From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**madbomber**

A Kaboom! clone "Mad Bomber" is a clone of Activision's classic Atari 2600 console game, "Kaboom!," by Larry Kaplan, with spruced-up graphics and sound effects, and music. The Mad Bomber is loose in the city and he's dropping bombs everywhere! It's your job to catch them before they hit the ground and explode. Luckily, you have a set of trusty buckets to extinguish the bombs with. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MADCAP**

Multicast Address Dynamic Client Allocation Protocol (RFC 2730, Multicast) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MADE**

Multimedia Application Development Environment (CWI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Madeinlinux**

An Italian Linux Distribution. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MADK**

Microsoft Activex Development Kit (ActiveX, MS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**madoka**

IRC personal proxy, stationing, logger and bot program (pirc). madoka can work as IRC personal proxy server, stationing on the IRC net with logging. and some bot plugins included. madoka is IPv6 compliant with Socket6.pm which is in libsocket6-perl. But Documents are available only Japanese. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**madplay**

MPEG audio player in fixed point MAD is an MPEG audio decoder. It currently only supports the MPEG 1 standard, but fully implements all three audio layers (Layer I, Layer II, and Layer III, the latter often colloquially known as MP3.). There is also full support for ID3 tags. All work is done in fixed point, so it even works on machines without a FPU. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MADT**

Multiple APIC Description Table (ACPI, APIC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MAE**

Macintosh Application Environment (Apple, Sun, HPUX) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Maelstrom**

Maelstrom is a space combat game, originally ported from the Macintosh platform. Brave pilots get to dodge asteroids and fight off other ships at the same time. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mag**

computes fontsizes and magsteps From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**magic number**

In source code, some non-obvious constant whose value is significant to the operation of a program and that is inserted inconspicuously in-line (hardcoded), rather than expanded in by a symbol set by a commented #define. Magic numbers in this sense are bad style. 2. A number that encodes critical information used in an algorithm in some opaque way. 3. pecial data located at the beginning of a binary data file to indicate its type to a utility. Under Unix, the system and various applications programs (especially the linker) distinguish between types of executable file by looking for a magic number. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**magic number**

n. [Unix/C; common] 1. In source code, some non-obvious constant whose value is significant to the operation of a program and that is inserted inconspicuously in-line (hardcoded), rather than expanded in by a symbol set by a commented #define. Magic numbers in this sense are bad style. 2. A number that encodes critical information used in an algorithm in some opaque way. The classic examples of these are the numbers used in hash or CRC functions, or the coefficients in a linear congruential generator for pseudo-random numbers. This sense actually predates and was ancestral to the more commonsense 1. 3. Special data located at the beginning of a binary data file to indicate its type to a utility. Under Unix, the system and various applications programs (especially the linker) distinguish between types of executable file by looking for a magic number. Once upon a time, these magic numbers were PDP-11 branch instructions that skipped over header data to the start of executable code; 0407, for example, was octal for `branch 16 bytes relative'. Many other kinds of files now have magic numbers somewhere; some magic numbers are, in fact, strings, like the !<arch> at the beginning of a Unix archive file or the %! leading PostScript files. Nowadays only a wizard knows the spells to create magic numbers. How do you choose a fresh magic number of your own? Simple -- you pick one at random. See? It's magic! The magic number, on the other hand, is 7+/-2. See "The magical number seven, plus or minus two: some limits on our capacity for processing information" by George Miller, in the "Psychological Review" 63:81-97 (1956). This classic paper established the number of distinct items (such as numeric digits) that humans can hold in short-term memory. Among other things, this strongly influenced the interface design of the phone system. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**magic2mime**

determine file type From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**magicdev**

Magicdev is a daemon that runs within the GNOME environment and detects when a CD is removed or inserted. Magicdev handles running autorun programs on the CD, updating the File Manager, and playing audio CDs. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**magicfilter**

automatic printer filter. Magicfilter is a customizable, extensible automatic printer filter. It uses its own magic database (` la file(1)) to decide how to print out a given print job. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**MagicPoint**

MagicPoint is an X11 based presentation tool. MagicPoint's presentation files (typically .mgp files) are plain text so you can create presentation files quickly with your favorite editor. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**magnus**

Computational group theory software with GUI The MAGNUS computational group theory package is an innovative symbolic algebra package providing facilities for doing calculations in and about infinite groups. Almost all symbolic algebra systems are oriented toward finite computations that are guaranteed to produce answers, given enough time and resources. By contrast, MAGNUS is concerned with experiments and computations on infinite groups which in some cases are known to terminate, while in others are known to be generally recursively unsolvable. MAGNUS features an intuitive graphical user interface, facilities for running different algorithms on the same problem in parallel, generation of approximations for working on otherwise infeasible problems, genetic algorithms and a plug-in package manager. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**magpie**

Debian reference librarian This program acts as a "reference librarian" for the apt(8) and dpkg(8) database, and how that information compares to the actual system. Each package is fully described on an individual page. Three additional package lists are provided: "required by," "recommended by" and "suggested by," as is a link to the Debian bug tracking system. If the package is installed, the page also shows the conffiles and any files in the package which don't match the manifest (if enabled). All package lists provide the "summary" description and the version of the package, if installed. A synopsis of all packages (the 'description' field) is available, grouped by section or priority or keyword. A synopsis of all installed packages is also provided. Additional indexes include package name, maintainer, source package, package size, installed size and md5sum. Magpie also has experimental XML support, but no XSL stylesheets have been defined yet. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mah-jong**

The original Mah-Jong game This is a set of programs to play the original Mah-Jong game: one server, one client for a human player and one client for a programmed player. Hence the game can be played by 1 to 4 human players. You should keep in mind that the original Mah-Jong game has nothing to do with the well-known solitaire game. (It only uses the same set of tiles.) If you like the game, please consider making a donation to the (upstream) author. Read /usr/share/doc/mah-jong/README.Debian for details. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Mail**

Electronic Mail is a means of exchanging private text messages through the Internet and other networks. Common Unix mail readers include Elm, Pine, and MUSH. It is also possible to read mail across a SLIP connection with a client program connected to a popmail server. From KADOWKEV <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mail**

send and receive mail From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mail-audit-tools**

Programs derived from the Mail::Audit package Small programs designed to enhance the Mail::Audit package. These include proc2ma, to convert procmail rc files to mail filters using Mail::Audit, and popread, to act as a replacement for fetchmail. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mail-files**

GNU sharutils From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mailagent**

an automatic mail-processing tool From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mailagent**

An automatic mail-processing tool Mailagent allows you to process your mail automatically. This has far more functionality than procmail, and is easier to configure (providing, of course, that you grok perl). As a mail processing tool, this slices, it dices, it ... Given a set of lex-like rules, you are able to file mails to specific folders (plain Unix-style folders and also MMDF and MH ones), forward messages to a third person, pipe a message to a command or even post the message to a newsgroup. It is also possible to process messages containing some commands. You may also set up a vacation program, which will automatically answer your mail while you are not there, but more flexibly than the Unix command of the same name. You only need to supply a message to be sent and the frequency at which this will occur. Some simple macro substitutions allow you to reuse some parts of the mail header into your vacation message, for a more personalized reply. You may also set up a generic mail server, without the hassle of the lower-level concerns like error recovery, logging or command parsing. The mailagent is not usually invoked manually but is rather called via the filter program, which is in turn invoked by sendmail. That means you must have sendmail/smail on your system to use this. You also must have perl to run the mailagent scripts. It is possible to extend the mailagent filtering commands by implementing them in perl and then having them automagically loaded when used. Please note that on Debian systems, mailagent can not lock /var/spool/mail directory mailboxes, and thus one must put a catch all rule saving all mail in ones home directory. This is because Debian MDA policy requires them to be setgid mail, and making anything as extensible as mailagent setgid anything negates any benefit of having group permission protection. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Mailbox**

In electronix mail, the storage space that has been set aside to store an individual's electronic mail messages. From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mailcap**

The mailcap file is used by the metamail program. Metamail reads the mailcap file to determine how it should display non-text or multimedia material. Basically, mailcap associates a particular type of file with a particular program that a mail agent or other program can call in order to handle the file. Mailcap should be installed to allow certain programs to be able to handle non-text files. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mailcheck**

Check multiple mailboxes/maildirs for mail Mailcheck is a simple, configurable tool that allows multiple mailboxes to be checked for the existence of new mail messages. It supports both mbox and maildir-style mailboxes, for compatibility with most mail transport agents. It also supports remote POP3 and IMAP mailboxes. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mailcrypt**

An Emacs interface to the GNU Privacy Guard. Mailcrypt is an Emacs lisp package that provides a simple but powerful interface to cryptographic functions for mail and news. With Mailcrypt, encryption becomes a seamlessly integrated part of your mail and news handling environment. Mailcrypt can automatically fetch public keys to encode, decode, and verify messages, and can be configured to automate mailing through anonymous remailers. Although Mailcrypt may be used to process data in arbitrary Emacs buffers, it is most useful in conjunction with other Emacs packages for handling mail and news. Mailcrypt has specialized support for Rmail, VM, MH-E, and Gnus. Currently XEmacs ships with its own Mailcrypt, so this package should only be used with GNU/Emacs. (I.e., you don't need to install this package if your site uses only XEmacs.) From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**maildir-bulletin**

Deliver bulletins directly to the users' Maildir. Deliver bulletins directly to the Maildir mail storage of users. Designed to be run from the /etc/aliases file with command-line parameters for which groups to send mail to. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**maildist**

mailagent's commands From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**maildrop**

mail delivery agent with filtering abilities maildrop is a replacement for your local mail delivery agent. maildrop reads a mail message from standard input, then delivers the message to your mailbox. maildrop knows how to deliver mail to mbox-style mailboxes, and maildirs (a mail storing format introduced by Qmail). maildrop can optionally read instructions from a file on how to filter incoming mail, and, based upon the instructions, deliver mail to alternate mailboxes, or forward it to somewhere else, like procmail. Unlike procmail, maildrop uses a structured filtering language that's a bit easier on the eyes. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**mailfilter**

A program that filters your incoming e-mail to help remove spam. Mailfilter is very flexible utility for UNIX (-like) operating systems to get rid of unwanted e-mail messages, before having to go through the trouble of downloading them to the local computer. It offers support for one or many POP3 accounts and is especially useful for dialup connections via modem, ISDN, etc. Install Mailfilter if you'd like to remove spam from your POP3 mail accounts. With Mailfilter you can define your own filters (rules) to determine which e-mails should be delivered and which are considered waste. Rules are Regular Expressions, so you can make use of familiar options from other mail delivery programs such as e.g. procmail. If you do not get your mail from a POP3-Server you don't need Mailfilter. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
