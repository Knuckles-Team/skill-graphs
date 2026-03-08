#  B

**B8ZS**

Binary 8 Zero Suppression [encoding] (ISDN, T1) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**babygimp**

An icon editor in Perl-Tk Babygimp is an icon editor in Perl-Tk. It can edit and save files in .xpm format. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**back door**

A hole in the security of a system deliberately left in place by designers or maintainers. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**back door**

n. [common] A hole in the security of a system deliberately left in place by designers or maintainers. The motivation for such holes is not always sinister; some operating systems, for example, come out of the box with privileged accounts intended for use by field service technicians or the vendor's maintenance programmers. Syn. trap door; may also be called a `wormhole'. See also iron box, cracker, worm, logic bomb. Historically, back doors have often lurked in systems longer than anyone expected or planned, and a few have become widely known. Ken Thompson's 1983 Turing Award lecture to the ACM admitted the existence of a back door in early Unix versions that may have qualified as the most fiendishly clever security hack of all time. In this scheme, the C compiler contained code that would recognize when the `login' command was being recompiled and insert some code recognizing a password chosen by Thompson, giving him entry to the system whether or not an account had been created for him. Normally such a back door could be removed by removing it from the source code for the compiler and recompiling the compiler. But to recompile the compiler, you have to use the compiler -- so Thompson also arranged that the compiler would recognize when it was compiling a version of itself, and insert into the recompiled compiler the code to insert into the recompiled `login' the code to allow Thompson entry -- and, of course, the code to recognize itself and do the whole thing again the next time around! And having done this once, he was then able to recompile the compiler from the original sources; the hack perpetuated itself invisibly, leaving the back door in place and active but with no trace in the sources. The talk that suggested this truly moby hack was published as "Reflections on Trusting Trust", "Communications of the ACM 27", 8 (August 1984), pp. 761-763 (text available at http://www.acm.org/classics). Ken Thompson has since confirmed that this hack was implemented and that the Trojan Horse code did appear in the login binary of a Unix Support group machine. Ken says the crocked compiler was never distributed. Your editor has heard two separate reports that suggest that the crocked login did make it out of Bell Labs, notably to BBN, and that it enabled at least one late-night login across the network by someone using the login name `kt'. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**back up**

to make a copy of important data onto a different storage medium. Backing up to tape is essential system maintenance. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Backbone**

A high-speed line or series of connections that forms a major pathway within a network. The term is relative as a backbone in a small network will likely be much smaller than many non-backbone lines in a large network. From Matisse <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Background**

In computers that can do more than one task at a time, the environment in which tasks (such as printing a document or downloading a file) are carried out while the user works with an application in the foreground. In computers that lack multitasking capabilities, background tasks are carried out during brief pauses in the execution of the system's primary (foreground) tasks. From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**background**

n.,adj.,vt. [common] To do a task `in background' is to do it whenever foreground matters are not claiming your undivided attention, and `to background' something means to relegate it to a lower priority. "For now, we'll just print a list of nodes and links; I'm working on the graph-printing problem in background." Note that this implies ongoing activity but at a reduced level or in spare time, in contrast to mainstream `back burner' (which connotes benign neglect until some future resumption of activity). Some people prefer to use the term for processing that they have queued up for their unconscious minds (a tack that one can often fruitfully take upon encountering an obstacle in creative work). Compare amp off, slopsucker. Technically, a task running in background is detached from the terminal where it was started (and often running at a lower priority); oppose foreground. Nowadays this term is primarily associated with Unix, but it appears to have been first used in this sense on OS/360. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**background**

Processing that a system performs without requiring interaction with the user. In Linux, append an ampersand (&) to the command line to request background processing. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**background process**

A process that runs without interacting with a terminal. Because each user in a Linux system is allowed to have a number of background processes running simultaneously, Linux is called a multitasking system. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Background Process**

A program that is running without user input. A number of background processes can be running on a multitasking operating system, such as UNIX/Linux, while the user is interacting with the foreground process (for example, data entry). Some background processes daemons, for example never require user input. Others are merely in the background temporarily while the user is busy with the program presently running in the foreground. From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**backreference**

n. 1. In a regular expression or pattern match, the text which was matched within grouping parentheses 2. The part of the pattern which refers back to the matched text. 3. By extension, anything which refers back to something which has been seen or discussed before. "When you said `she' just now, who were you backreferencing?" From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**backslash**

A character (\\) that is used in shell statements to quote another character (that is, to remove its special meaning to the shell). For example, if you want to use a dollar sign as a dollar sign, rather than as a symbol for end of line, enter \$. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**backup**

A copy of a file (or a group of files) that is stored off-line in the event that a computer system fails, losing or damaging the original file or files. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**backup**

To periodically archive data on a system to mitigate risk of permanent data loss in the event of system or component malfunction or destruction. From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**backward combatability**

/bak'w*rd k*m-bat'*-bil'*-tee/ n. [CMU, Tektronix: from `backward compatibility'] A property of hardware or software revisions in which previous protocols, formats, layouts, etc. are irrevocably discarded in favor of `new and improved' protocols, formats, and layouts, leaving the previous ones not merely deprecated but actively defeated. (Too often, the old and new versions cannot definitively be distinguished, such that lingering instances of the previous ones yield crashes or other infelicitous effects, as opposed to a simple "version mismatch" message.) A backwards compatible change, on the other hand, allows old versions to coexist without crashes or error messages, but too many major changes incorporating elaborate backwards compatibility processing can lead to extreme software bloat. See also flag day. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**backwards compatible**

The quality of software to be able to work properly with older versions of the software that may be installed on a machine or communicating with another machine with a lower version of the software. From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BACP**

Bandwidth Allocation Control Protocol (BAP, RFC 2125) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAD**

Broken As Designed (slang) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Bad Penguin Linux**

An Italian distribution, currently at version 0.99.5. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**badblocks**

search a device for bad blocks From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BADW**

Bayerische Akademie Der Wissenschaften (org.) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAGEL**

Bay Area GNU Enthusiasts League (GNU, org., user group) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAI**

Basic Access Interface (ISDN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**balsa**

GNOME email client Balsa is a e-mail reader. This client is part of the GNOME desktop environment. It supports local mailboxes, POP3 and IMAP. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BALUN**

BALanced-UNbalanced [adapter] (cable), "Balun" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAM**

Bidirectional Associative Memory (neural nets) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAM**

Block-Availability-Map From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAM**

Bundesanstalt fuer Materialpruefung (org., Berlin, Germany) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Bambi Linux**

A Red Hat based wireless distribution. A 'wireless' distribution. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Bandwidth**

How much stuff you can send through a connection. Usually measured in bits-per-second. A full page of English text is about 16,000 bits. A fast modem can move about 57,000 bits in one second. Full-motion full-screen video would require roughly 10,000,000 bits-per-second, depending on compression. From Matisse <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**bang**

1. n. Common spoken name for ! (ASCII 0100001), especially when used in pronouncing a bang path in spoken hackish. In elder days this was considered a CMUish usage, with MIT and Stanford hackers preferring excl or shriek; but the spread of Unix has carried `bang' with it (esp. via the term bang path) and it is now certainly the most common spoken name for !. Note that it is used exclusively for non-emphatic written !; one would not say "Congratulations bang" (except possibly for humorous purposes), but if one wanted to specify the exact characters `foo!' one would speak "Eff oh oh bang". See shriek, ASCII. 2. interj. An exclamation signifying roughly "I have achieved enlightenment!", or "The dynamite has cleared out my brain!" Often used to acknowledge that one has perpetrated a thinko immediately after one has been called on it. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**bang**

Denoted by the ! character. The C shell command !!, which repeats the last command, for example, is pronounced "Bang!Bang!". From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Bang path**

A series of names that specifies a path between two nodes. It is sometimes used for email or BITNET as well as in the Linux uucp program. The path consists of machine or domain names separated by ! (bang). From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**bang path**

n. [now historical] An old-style UUCP electronic-mail address specifying hops to get from some assumed-reachable location to the addressee, so called because each hop is signified by a bang sign. Thus, for example, the path ...!bigsite!foovax!barbox!me directs people to route their mail to machine bigsite (presumably a well-known location accessible to everybody) and from there through the machine foovax to the account of user me on barbox. In the bad old days of not so long ago, before autorouting mailers became commonplace, people often published compound bang addresses using the { } convention (see glob) to give paths from several big machines, in the hopes that one's correspondent might be able to get mail to one of them reliably (example: ...!{seismo, ut-sally, ihnp4}!rice!beta!gamma!me). Bang paths of 8 to 10 hops were not uncommon in 1981. Late-night dial-up UUCP links would cause week-long transmission times. Bang paths were often selected by both transmission time and reliability, as messages would often get lost. See Internet address, the network, and sitename. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**banner**

Many text-based protocols will issue text banners when you connect to the service. These can usually be used to fingerprint the os or service. Key point: Many banners reveal the exact version of the product. Over time, exploits are found for specific versions of products. Therefore, the intruder can simply lookup the version numbers in a list to find which exploit will work on the system. In the examples below, the version numbers that reveal the service has known exploitable weaknesses are highlighted. Example: The example below is a RedHat Linux box with most the default service enabled. The examples below show only the text-based services that show banners upon connection (in some cases, a little bit of input was provided in order to trigger the banners). Note that this is an older version of Linux; exploits exist for most these services that would allow a hacker to break into this box (most are buffer-overflow exploits). Best practices: It is often recommend (and required in some government areas) to display a banner warning off unauthorized users. It makes the legal case stronger if you can show that the attacker saw a banner that indicated that they were unauthorized. Best practices: All version information should be suppressed in the banners. See the product documentation for more information on this. An example on Solaris is to edit the configuration file /etc/default/telnetd and added the line: BANNER="" This will remove the Solaris login banner, making it more difficult for an intruder to determine the type of operating system. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**banner page**

A way to separate printing jobs which often indicates the owner of the file that has been printed. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BanShee Linux/R**

BanShee Linux/R is a two-floppy rescue system using uClibc and Busybox to make sure that the system is as small as possible. Initial version 0.5 was released September 18, 2002. Version 0.61 was released October 27, 2002. A floppy-based distribution. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAP**

[PPP] Bandwidth Allocation Protocol (PPP, RFC 2125, BACP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAPC**

[PPP] Bandwidth Allocation Control Protocol (PPP, BAP, RFC 2125) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAPCO**

Business Application Performance COrporation (org., Compaq, Dell, HP, IBM, MS, Lotus, Intel, ...), "BAPCo" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAPI**

Business Application Programmer's Interface (SAP, R/3, API) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAPT**

BundesAmt fuer Post und Telefon (org.) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**bar**

/bar/ n. 1. [very common] The second metasyntactic variable, after foo and before baz. "Suppose we have two functions: FOO and BAR. FOO calls BAR...." 2. Often appended to foo to produce foobar. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAR**

Base Address Register (IC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**barcode**

Creates barcodes in .ps format GNU barcode can create printouts for the conventional product packaging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, code 39 code 128 (b and c), and interleaved 2 of 5 . Output is generated as either Postscript or Encapsulated Postscript. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**barrendero**

Deletes messages on the spool dir depending on their age. Barrendero is intended to limit the disk space wasted at the spool directory. It deletes mail messages depending on their age, and has the ability to send warnings and reports to the users, to make full and partial backups, and to have different allowed ages on a per-user basis. Warning and report messages are customizable and can be translated easily in order to make this package useful in any environment. This way of handling mail as an advantage over the traditional 'quota' system: quotas make the end user loose NEW mail, barrendero deletes OLD mail, so the new mail is always available. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BARRNET**

Bay Area Regional Research NETwork (network), "BARRNet" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BART**

Basic Application RunTime (OS/2, IBM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BARWAN**

Bay Area Research Wireless Access Network (network, USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BAS**

Basic Activity Subset From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**basename**

Parse pathname components From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**basename**

strip directory and suffix from filenames From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**basename**

the name of a file minus any extension that may be included in the full name. For example, if the full name of the source file for a C program is combine.c, its basename is combine. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**bash**

Bash is a GNU project sh-compatible shell or command language interpreter. Bash (Bourne Again shell) incorporates useful features from the Korn shell (ksh) and the C shell (csh). Most sh scripts can be run by bash without modification. Bash offers several improvements over sh, including command line editing, unlimited size command history, job control, shell functions and aliases, indexed arrays of unlimited size and integer arithmetic in any base from two to 64. Bash is ultimately intended to conform to the IEEE POSIX P1003.2/ISO 9945.2 Shell andTools standard.Bash is the default shell for Mandrake Linux. You should installbash because of its popularity and power. You'll probably end up using it. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BASH**

Bourne-Again SHell (Unix, Shell) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Bash**

Descended from the Bourne Shell, Bash is a GNU product, the "Bourne Again SHell." It's the standard command line interface on most Linux machines. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BASH**

The Bourne Again Shell and is based on the Bourne shell, sh, the original command interpreter. <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**bash**

The default command interpreter, or shell, for Red Hat Linux. bash features several enhancements to sh, such as built-in file management commands and support for completion of commands and paths using the the [Tab] key. From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**bash**

The GNU Bourne Again SHell Bash is an sh-compatible command language interpreter that executes commands read from the standard input or from a file. Bash also incorporates useful features from the Korn and C shells (ksh and csh). Bash is ultimately intended to be a conformant implementation of the IEEE POSIX Shell and Tools specification (IEEE Working Group 1003.2). From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Bash (Bourne Again SHell)**

An enhanced version of the Bourne Shell. (Also, see Korn Shell.) From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**bashbug**

report a bug in bash From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BASIC**

/bay'-sic/ n. A programming language, originally designed for Dartmouth's experimental timesharing system in the early 1960s, which for many years was the leading cause of brain damage in proto-hackers. Edsger W. Dijkstra observed in "Selected Writings on Computing: A Personal Perspective" that "It is practically impossible to teach good programming style to students that have had prior exposure to BASIC: as potential programmers they are mentally mutilated beyond hope of regeneration." This is another case (like Pascal) of the cascading lossage that happens when a language deliberately designed as an educational toy gets taken too seriously. A novice can write short BASIC programs (on the order of 10-20 lines) very easily; writing anything longer (a) is very painful, and (b) encourages bad habits that will make it harder to use more powerful languages well. This wouldn't be so bad if historical accidents hadn't made BASIC so common on low-end micros in the 1980s. As it is, it probably ruined tens of thousands of potential wizards. [1995: Some languages called `BASIC' aren't quite this nasty any more, having acquired Pascal- and C-like procedures and control structures and shed their line numbers. --ESR] Note: the name is commonly parsed as Beginner's All-purpose Symbolic Instruction Code, but this is a backronym. BASIC was originally named Basic, simply because it was a simple and basic programming language. Because most programming language names were in fact acronyms, BASIC was often capitalized just out of habit or to be silly. No acronym for BASIC originally existed or was intended (as one can verify by reading texts through the early 1970s). Later, around the mid-1970s, people began to make up backronyms for BASIC because they weren't sure. Beginner's All-purpose Symbolic Instruction Code is the one that caught on. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BASIC**

Beginner's All-purpose Symbolic Instruction Code From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BASIC**

Beginners All purpose Symbolic Instruction Code: a non-structured language that is often considered the easiest to start programming. It was developed as an interactive, mainframe timesharing language that received fame with home computers in the 1980s. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Basic Input Output System (BIOS)**

A set of instructions stored on a ROM CHIP that handles input-output functions and system component management (such as power configuration and interrupt request settings). From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BasicLinux**

BasicLinux is a mini-version of Linux that boots from hard drive, floppy, or CDROM, and runs in a 4meg ramdisk. It's based on Slackware 3.5 and contains a fully-featured shell, an easy-to-use editor, and a variety of useful utilities. It can dial an ISP, browse the web, send/receive mail, or act as a router/firewall. Version 1.7 was released May 12, 2002. Version 2.0 was released February 22, 2003, now based on Slackware 7.1. A small disk distribution. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**basilix**

A PHP (both PHP3 and PHP4) and IMAP based webmail application powered with MySQL database server. It has a nice user-friendly interface and its HTML files are easy to be changed/edited. 0.7.6 includes WAP-Support. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**BASIN**

Bundesweites Alternatives Studentisches InformationsNetzwerk (WWW, org.) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**bastille**

Security hardening tool Bastille Linux is a security hardening program for several Linux distributions. If run in the preferred Interactive mode, it can teach you a good deal about Security while personalizing your system security state. If run in the quicker Automated mode, it can quickly tighten your machine, once a default profile is selected. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
