
GNU Bourne-Again SHell From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sh-utils**

The GNU shell utilities are a set of useful system utilities that are often used in shell scripts. The sh-utils package includes basename (to remove the path prefix from a specified pathname), chroot (to change the root directory), date (to print/set the system time anddate), dirname (to remove the last level or the filename from a givenpath), echo (to print a line of text), env (to display/modify theenvironment), expr (to evaluate expressions), factor (to print primefactors), false (to return an unsuccessful exit status), groups (toprint the groups a specified user is a member of), id (to print the real/effective uid/gid), logname (to print the current login name),nice (to modify a scheduling priority), nohup (to allow a command to continue running after logging out), pathchk (to check a file name's portability), printenv (to print environment variables), printf (to format and print data), pwd (to print the current directory), seq (to print numeric sequences), sleep (to suspend execution for a specified time), stty (to print/change terminal settings), su (to become another user or the superuser), tee (to send output to multiple files), test(to evaluate an expression), true (to return a successful exit status), tty (to print the terminal name), uname (to print system information), users (to print current users' names), who (to print a list of the users who are currently logged in), whoami (to print the effective user id), and yes (to print a string indefinitely). From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SHA**

Secure Hash Algorithm (cryptography, NIST) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SHA**

Super High Aperture [LCD] (LCD) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SHA-1 (United States Government Secure Hash Algorithm, FIPS 180-1, ANSI 9.30-2, ISO/IEC 10118-3)**

SHA-1 is a popular hash algorithm. It converts an input file or message into a "unique" 160-bit fingerprint. This fingerprint is believed to be "unique"; while it is theoretically possible that two inputs could hash to the same fingerprint, it is nearly statistically impossible. Contrast: SHA-1 is currently (year 2001) considered to be the strongest hash function available. It has a larger size (160-bits vs. 128-bits) and has underground thorough scrutiny without discovery of weaknesses (such as MD5). On the other hand, it is one of the slower hash algorithms. History: SHA-1 is a slight variation of SHA. It adds a one-bit shift at one stage in order to overcome a theoretical weakness. SHA was based upon MD4, enhanced to overcome known weaknesses and increase the length to 160-bits. See also: integrity From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shadow-utils**

The shadow-utils package includes the necessary programs for converting UNIX password files to the shadow password format, plus programs for managing user and group accounts. The pwconv command converts passwords to the shadow password format. The pwunconv command unconverts shadow passwords and generates an npasswd file (a standard UNIX password file). The pwck command checks the integrity of password and shadow files. The lastlog command prints out the last login times for all users. The useradd, userdel and usermod commands are used for managing user accounts. The groupadd, groupdel andgroupmod commands are used for managing group accounts. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shadowconfig**

toggle shadow passwords on and off From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shadowed passwords (/etc/shadow)**

UNIX was designed around the concept of making the encrypted form of passwords readable by everyone. These passwords were stored in the /etc/passwd file, along with the full account information. It was thought to be secure because the passwords were stored in an encrypted format within this file. However, this is not secure in practice because users tend to choose easily guessable passwords. A program called crack was developed that would guess dictionary words (/usr/dict) and then attempt to brute force the passwords. On an average UNIX system, 90% of all passwords could be cracked with a few days worth of computing time. In order to solve this problem, a "shadow" password file was developed. The encrypted passwords are removed from the normal /etc/passwd and placed in a special file (usually /etc/shadow) that is only readable by root. The remaining account information is left in the original password file for backwards compatibility. Example: The following is a table of typical locations for the shadowed passwords: AIX 3 /etc/security/passwd or /tcb/auth/files// A/UX 3.0s /tcb/files/auth/?/ BSD4.3-Reno /etc/master.passwd ConvexOS 10 /etc/shadpw ConvexOS 11 /etc/shadow DG/UX /etc/tcb/aa/user/ EP/IX /etc/shadow HP-UX /.secure/etc/passwd IRIX 5 /etc/shadow Linux /etc/shadow OSF/1 /etc/passwd[.dir|.pag] SCO Unix #.2.x /tcb/auth/files// SunOS4.1+c2 /etc/security/passwd.adjunct SunOS 5.0 /etc/shadow System V Release 4.0 /etc/shadow System V Release 4.2 /etc/security/* database Ultrix 4 /etc/auth.dir or /etc/auth.pag UNICOS /etc/udb Key point: In the old days, most remote attacks against UNIX were directed at the /etc/passwd file. For example, the most common form of the phf would be to grab the password file. As password shadowing becomes more common, such attacks are increasingly being pointed at the shadow password file instead. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shapecfg**

The Shapecfg program configures and adjusts traffic shaper bandwidth limiters. Traffic shaping is setting parameters or limits on bandwidth consumption, to which network traffic should conform. To use Shapecfg,you must have also installed the kernel which supports the shaper module (kernel versions 2.0.36 or later and late 2.1.x kernels). From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shaper**

Traffic Shaper for Linux The traffic shaper for Linux configures and adjusts traffic shaper bandwidth limiters. Traffic shaping means setting parameters or limits to which network traffic should conform - that is, setting limitations on bandwidth consumption. See README.shaper for more details. An init script which sets up traffic shaping using class-based queueing is also provided. This can be used to build smart bandwidth shapers which know about TCP/IP. See README.cbq for more details. The kernel support needed to use either of these facilities is described in README.Debian. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shaperd**

A user-mode traffic shaper for tcp-ip networks. Shaperd is a user-mode program that can shape traffic passing through a Linux box. As it runs as a normal daemon, some kind of packet-forwarding mechanism is needed. This can be done with the BSD divert sockets patch for Linux 2.2, or with netfilter's built-in libipq under Linux 2.4. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shapetools**

Configuration and Release management using AtFS. ShapeTools is a collection of programs to support software configuration management in an UNIX environment. It consists of a set of version and attribute control commands, and a configuration interpreter and build tool ("shape"). The toolkit is integrated on top of the Attributed File System (AtFS). ShapeTools is designed to live meaningfully together with any other UNIX tool operating on regular files. This distribution also contains a prototype for a comprehensive change control and release management system designed to manage the evolution of system releases in multi programmer software development efforts. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shar**

create shell archives From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sharchive**

/shar'ki:v/ n. [Unix and Usenet; from /bin/sh archive] A flattened representation of a set of one or more files, with the unique property that it can be unflattened (the original files restored) by feeding it through a standard Unix shell; thus, a sharchive can be distributed to anyone running Unix, and no special unpacking software is required. Sharchives are also intriguing in that they are typically created by shell scripts; the script that produces sharchives is thus a script which produces self-unpacking scripts, which may themselves contain scripts. (The downsides of sharchives are that they are an ideal venue for Trojan horse attacks and that, for recipients not running Unix, no simple un-sharchiving program is possible; sharchives can and do make use of arbitrarily-powerful shell features.) Sharchives are also commonly referred to as `shar files' after the name of the most common program for generating them. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shared library**

A library where the linker leaves a note in the output that says "when this is run, it will first have to load this library". Shared libraries tend to make for smaller executables than static library. On Linux they have names like libname.so.x.y.z From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shared media**

Networks like Ethernet whereby multiple computers connect to the same wire. Key point: In such systems, any computer on the wire can eavesdrop on its neighbors. Contrast: Most corporations are replacing their shared media nets with switched connections. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shared memory**

memory which can be access by more than one process in a multitasking operating system with memory protection From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Shared memory pixmaps**

They are 2 dimensional arrays of pixels in a format specified by the X server, where the pixmap data is stored in the shared memory segment. See MIT-SHM. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shared secret**

The idea that many people share the same password or key. Shared secrets are widely use because they are easy: there is simply one password to give out. On the other hand, the more widely secrets are shared, the more likely it will become compromised. In fact, many people believe that even sharing a secret among two people is extremely risky, where the proper solution is using public keys to distribute a randomly generated key only valid for the particular message. Example: DVD movies are encrypted with a randomly generated key. This key is then is then encrypted multiple times with hundreds of different keys. Every DVD player vendor owns one of these keys and imbeds it in their device, thus allows that player to decrypt the movie. (Presumably, if one of the keys is compromised, future movies can be generated without the offending key, causing players based upon that key to become obsolete). However, there is no good way to protect these keys, even though they are in hardware. In late 1999, students in Europe where able to break one of these keys (the Xing software DVD player), and from there they were able to break the majority of the other keys. (These keys only used 40-bit encryption, so breaking one key in the software player allowed a known-plaintext attack). From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ShareTheNet**

ShareTheNet lets you share your low cost Internet connection across your network. Using ShareTheNet, all of the computers on your network can do their own work on the Internet as though they have their own connection. ShareTheNet allows just about any network software to use the Internet and its ultra-secure. Distribution development is not all that active. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shareware**

/sheir'weir/ n. A kind of freeware (sense 1) for which the author requests some payment, usually in the accompanying documentation files or in an announcement made by the software itself. Such payment may or may not buy additional support or functionality. See also careware, charityware, crippleware, FRS, guiltware, postcardware, and -ware; compare payware. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Shareware**

A form of commercial software, where it is offered as "try before you buy". If the customer continues to use the product after a short trial period, they are required to pay a specified, usually nominal, fee. (Also, see Open Source and Public Domain.) From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sharutils**

shar, unshar, uuencode, uudecode `shar' makes so-called shell archives out of many files, preparing them for transmission by electronic mail services. `unshar' helps unpacking shell archives after reception. Other related utility programs help with other tasks. `uuencode' prepares a file for transmission over an electronic channel which ignores or otherwise mangles the eight bit (high order bit) of bytes. `uudecode' does the converse transformation. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**sharutils**

The sharutils package contains the GNU shar utilities, a set of tools for encoding and decoding packages of files (in binary or text format) in a special plain text format called shell archives (shar). This format can be sent through email (which can be problematic for regular binary files). The shar utility supports a wide range of capabilities (compressing, uuencoding, splitting long files for multi-part mailings, providing checksums), which make it very flexible at creating shar files. After the files have been sent, the unshartool scans mail messages looking for shar files. Unshar automatically strips off mail headers and introductory text and then unpacks the sharfiles. Install sharutils if you send binary files through email very often. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SHED**

Segmented Hypergraphics EDitor (MS, Windows, ADT) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shell**

A command interpreter that allows a user to run executable code. Shells also store and configure additional information about a user's executable paths, environment variables, and usability options. From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Shell**

A text-mode window containing a command line interface to the operating system. From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shell**

a utility program that enables the user to interact with the UNIX operating system. Commands entered by the user are passed by the shell to the operating system which carries them out. The results are then passed back by the shell and displayed on the user's display. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Shell**

One of several command line interfaces available on Unix machines, some common shells include Bourne shell, ksh, and tcsh. From KADOWKEV <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shell**

The default command-line interface on UNIX systems. Key point: This is similar to the "Command Prompt" or incorrectly named "DOS Prompt" on Windows systems. Key point: Many systems pass filenames along with commands directly to the shell. Hackers can exploit this by sending special shell characters (like the pipe | character) as part of filenames in order to execute their own commands. This is an example of an input validation exploit. Examples of this are web-servers, PERL scripts, and CGI scripts. Key point: The most popular shell among hackers is probably "bash", the shell from GNU that ships with Linux. (Culture: The original shell on UNIX is known as the "Bourne Shell", named for its creator. The acronym "bash" means "Bourne Again SHell", reflecting that fact that it is a rewrite of that shell). Key point: Retrieving someone's .bash_history file is a common attack against UNIX machines. Several embedded systems have shipped such that the file http://raq.robertgraham.com/~root/.bash_history could be retrieved via the web. Key point: The holy grail of UNIX hacking is to somehow obtain (or re-obtain) a root shell. In other words, the hacker wants to get a command-line on the victim system in order to carry out any task. For this reason, buffer overflow exploits often contain what is called "shell code". When the victim process is running with root privileges, the buffer-overflow will cause that process to begin running a shell. For example, an exploit might send a long password containing the shell code to an FTP server, converting the TCP connection to the FTP server into a full command-prompt from which any program can be launched. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shell**

[orig. Multics n. techspeak, widely propagated via Unix] 1. [techspeak] The command interpreter used to pass commands to an operating system; so called because it is the part of the operating system that interfaces with the outside world. 2. More generally, any interface program that mediates access to a special resource or server for convenience, efficiency, or security reasons; for this meaning, the usage is usually `a shell around' whatever. This sort of program is also called a `wrapper'. 3. A skeleton program, created by hand or by another program (like, say, a parser generator), which provides the necessary incantations to set up some task and the control flow to drive it (the term driver is sometimes used synonymously). The user is meant to fill in whatever code is needed to get real work done. This usage is common in the AI and Microsoft Windows worlds, and confuses Unix hackers. Historical note: Apparently, the original Multics shell (sense 1) was so called because it was a shell (sense 3); it ran user programs not by starting up separate processes, but by dynamically linking the programs into its own code, calling them as subroutines, and then dynamically de-linking them on return. The VMS command interpreter still does something very like this. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shell out**

vi. [Unix] To spawn an interactive subshell from within a program (e.g., a mailer or editor). "Bang foo runs foo in a subshell, while bang alone shells out." From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shell prompt**

a character at the start of the command line which indicates that the shell is ready to receive your commands. The character is usually a '%' (percent sign) or a $ (dollar sign). It may be different on your system. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shell prompt**

An application that offers interactive console or terminal access to a computer system. From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Shell Prompt**

The user input area of a shell. Whereas in a DOS shell the command prompt is designated by a Greater Than (>) symbol, in Linux it is usually a Percent (%) symbol, Dollar sign ($) or other special character, depending on the shell used. (Also, see Command Prompt.) From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shell script**

A program written to be interpreted by the shell of an operating system such as Linux. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Shell Script**

A script designed to be run automatically when a shell is started. From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Shell Scripting**

Shell Scripting and hence computer programming is merely the idea of getting a number of commands to be executed, that in combination do some unique powerful function. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shellcode**

When a hackers successfully exploit vulnerabilities like buffer overflows, they will typically open a shell at the end of the exploit. With a command-line shell, the hacker will then be able to carry out any task they desire. However, opening shells within buffer overflow exploits can be difficult. Therefore, hackers often maintain libraries of "shellcode": code fragments for various operating systems that can be pasted into buffer overflow exploits. Key point: One of the difficulties in writing shellcode is that need to pass through filters. For example, when exploiting a bug in an SMTP server, you may find that the server strips the high-order bit from all bytes (i.e. will pass text but not binary). Therefore, all bytes between 0x00-07F will pass through, but not 0x80-0xFF. Alternately, a big limitation is systems that won't pass nul characters (0x00) because they terminate strings in functions like strcpy(). Therefore, when a hacker picks shellcode to append to their script, they must be fully aware of the limitations of the system they are dealing with. Key point: When creating new shellcode, create a C program that calls something like "system("/bin/sh");" or "execve("/bin/sh",0,0);" and grab the assembly output. At that point, pare it down to what you need. This requires extensive knowledge of assembly, needless to say. Key point: Sometimes you won't be able to grab a shell, so you have to create the exploit script to run a command. Typical choices of commands would be those that change passwords, add accounts, or in some fashion open up some other hole on the system. Key point: The vast majority of buffer overflow attacks will execute /bin/sh. Therefore, by simply removing this program (or replacing it with something that double-checks what's being done), you can protect yourself against many 0-day exploits. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shellutils**

The GNU shell programming utilities. The utilities: basename chroot date dirname echo env expr factor false groups hostid id logname nice nohup pathchk pinky printenv printf pwd seq sleep stty tee test true tty uname users who whoami yes. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**SHF**

Super-High Frequency From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shhmsg**

library for displaying messages - runtime This is Sverre H. Huseby's library for displaying messages in terminal based programs. It can treat the verbosity level and prepend the program name if necessary. This package contains what you need to run programs that use this library. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shhopt**

Command line option parser - runtime This is Sverre H. Huseby's library for parsing command line options. Both traditional one-character options and GNU-style --long-options are supported. This library does a little more than standard getopt. This package contains what you need to run programs that use this library. upstream webpage: http://shh.thathost.com/ From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shift left (or right) logical**

[from any of various machines' instruction sets] 1. vi. To move oneself to the left (right). To move out of the way. 2. imper. "Get out of that (my) seat! You can shift to that empty one to the left (right)." Often used without the `logical', or as `left shift' instead of `shift left'. Sometimes heard as LSH /lish/, from the PDP-10 instruction set. See Programmer's Cheer. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shoop**

The SHell Object Oriented Programming library Every language under the sun these days is Object Oriented. In an effort to make POSIX shell more buzzword compliant, and to show that it's really not a big deal for a language to lack built-in OO support, we have added object orientation to plain old shell script. Specifically, we have implemented classless OO with introspection, finalization, serialization, and multiple inheritance. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shoop-modules**

A collection of shoop modules This package includes various modules for shoop, such as introspect, prettyprint, serialize, and some others. It is a good idea to have these at hand! From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**shorewall**

Shoreline Firewall (Shorewall) The Shoreline Firewall (Shorewall) is an iptables based firewall that can be used on a dedicated firewall system, a multi-function masquerade gateway/server or on a standalone Linux system. Shorewall supports these features: * Customizable using configuration files. * Supports status monitoring with an audible alarm when an "interesting" packet is detected. * Include a fallback script that backs out the installation of the most recent version of Shoreline Firewall and an uninstall script for completely uninstalling the firewall. * Static NAT is supported. * Proxy ARP is supported. * Provides DMZ functionality. * Support for IPSEC, GRE and IPIP Tunnels. * Limited support for Traffic Control/Shaping From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
