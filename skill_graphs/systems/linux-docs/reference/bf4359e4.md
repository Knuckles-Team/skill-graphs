#  P

**P-code (Pseudo-code) Language**

A type of Interpreted language. P-code languages are something of a hybrid, falling between compiled languages and interpreted languages in the way they execute. Like an interpreted language, P-code programming is converted to a binary form automatically when it is run, rather than having to be compiled. However, unlike a compiled language the executable binary file is stored in pseudo-code, not machine language. In addition, unlike an Interpreted language, the program does not have to be converted to binary each time it is run. After it is converted to P-code the first time, the pseudo-code version is used for each additional execution. P-code languages (and thus their programs) tend to be slower than compiled languages and programs but faster than interpreted languages, and they generally have authorization to some low-level operating system functions but not direct hardware access. They do not require sometimes-expensive compilers, are often included along with operating systems, and some p-code languages are easier to program than compiled languages. Examples of Pcode languages are Java, Python and REXX/Object REXX. From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**P-code language**

They are like compiled languages in that the source is translated to a compact binary form which is what you actually execute, but that form is not machine code. Instead it's pseudocode (or p-code), which is usually a lot simpler but more powerful than a real machine language. When you run the program, you interpret the p-code. Important p-code languages include Python and Java. See Compiled language and Interpreted language. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**p10cfgd**

Remote configuration daemon for Gracilis Packeten. The 'p10cfgd' daemon provides support for the 'rmtcfg' command in the Gracilis Packeten amateur radio network packet switch. With this daemon, and appropriate entries in the non-volatile configuration memory of a Packeten, it is possible to have the switch load commands and information at boot time. Further, this daemon appends a command which sets the date and time in the clock on the Packeten. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**p2c**

Pascal to C translator P2c is a tool for translating Pascal programs into C. The input consists of a set of source files in any of the following Pascal dialects: HP Pascal, Turbo/UCSD Pascal, DEC VAX Pascal, Oregon Software Pascal/2, Macintosh Programmer's Workshop Pascal, Sun/Berkeley Pascal, Texas Instruments Pascal, Apollo Domain Pascal. Modula-2 syntax is also supported. Output is a set of .c and .h files that comprise an equivalent program in any of several dialects of C. Output code may be kept machine and dialect-independent, or it may be targeted to a specific machine and compiler. Most reasonable Pascal programs are converted into fully functional C which will compile and run with no further modifications, although p2c sometimes chooses to generate readable code at the expense of absolute generality. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**P2CC2P**

PCI to CPU / CPU tp PCI [concurrency] (BIOS, PC, PCI, CPU), "P2C/C2P" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**P2P**

Peer to Peer [net] From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**p3nfs**

Mount Psion series 3[ac], 5 drives. The package lets you mount psion drives on your Debian box over a serial cable. You can access all the files from the psion with the usual commands like tar, cp, vi & co. Works with Psion series 3[ac], 5 machines. Haven't tested on a Sienna yet. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**P3P**

Platform for Privacy Preferences (WWW) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**p4fftwgel2**

Library for computing Fast Fourier Transforms on Intel P4 This library computes Fast Fourier Transforms (FFT) in one or more dimensions. It is extremely fast. This package contains the documentation and the shared version of the libraries. To get the static library and the header files you need to install p4fftwgel-dev. This library uses the same interface as fftw so should be a drop-in replacement, but is currently limited to single precision only. The code is tuned for Intel P4 processors and can be as much as three times as fast as vanilla fftw. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PA**

Precision Architecture (HP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PA-RISC Linux**

On December 11, 2001 the PA-RISC Linux development community announced version 0.9.3, the latest version of Linux for computers using Hewlett Packard's PA-RISC processor. This release is the latest in a series representing several years of work by developers in the Free Software community including developers from The Debian Project, Hewlett Packard, ESIEE, and Linuxcare. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PABX**

Private Automatic Branch eXchange From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pac**

printer/plotter accounting information From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAC**

Privilege Attribute Certificate (DCE) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PACE**

Priority Access Control Enabled (3Com, ethernet) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PACER**

Public Access to Court Electronic Records From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**package**

A file containing software written in a particular format to enables easy installation, upgrade, and removal. From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**package**

register package user via mailagent From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**packet**

All data sent across the Internet is broken up into packets, sent individually across the network, and reassembled back into the original data at the other end. Analogy: Imagine looking at an automobile freeway during rush hour from an airplane. The freeway looks like a flowing river, but each individual car (packet) is really independent from all the others. While it looks like the cars on the freeway are going in the same direction, each car really has its own source and destination separate from the others around it. This is how Internet core routes look. Analogy: Now consider that a bunch of coworkers leave the office and go to a party. Each gets in his/her own car and drives to the party. Each person may take a slightly route, but they all end up together at the party. This demonstrates how data is broken up into individual packets, sent across the Internet (potentially following different routes), then reassembled back again at the destination. Key point: Conceptually, networking occurs at abstract layers well above the concept of packets. Users type in a URL, and the file is downloaded. By dealing with the raw packets themselves, hackers are frequently able to subvert communications in ways not detectable at these higher layers. Contrast: The term "packet switched network (PSN)" is used to describe the Internet, whereas the term "circuit switched network (CSN)" is used to contrast it with the traditional phone system. The key difference is that in the phone system, the route between two people is setup at the start, and each bit in the stream follows that route. On the Internet, each packet finds its own route through the system, so during a conversation, the packets can follow different paths, and indeed arrive out-of-order. Another key difference is latency. The phone system forwards each bit one at a time, so as soon as one arrives, it doesn't have to wait before forwarding it on. On the Internet, bits are bunched together before transmission. Each hop must wait and receive all the bits before forwarding any of them on. Each hop therefore adds a significant amount of delay. Gamers know this as the "ping" time. Key point: There are other technologies that use packets, not just the Internet. Before the Internet came along, X.25 networks were a popular form of packet-based communication (and indeed, X.25 formed the basis for many links on the nascent Internet). From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Packet**

The fundamental unit of communication on the Internet. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**packet filter**

In firewalls, packet filters are the technology most often used to control traffic. Every packet contains the following fields: source IP address (example: 192.0.2.156) destination IP address transport type (example: TCP=6, UDP=17, ICMP=1) source port (example: HTTP=80, DNS=53, FTP=21) destination port flags (example: SYN) This data is compared against "rules" within the firewall. A typical set of rules might be: BLOCK destination=192.0.2.x TCP flag=SYNALLOW destination=192.0.2.123 TCP destport=80 ALLOW destination=192.0.2.124 TCP destport=25 If our private network is 192.0.2.x, then the first rule above blocks all incoming TCP connections (though outbound connections would still be allowed). The following rules override the first, allowing access to the web-server at port 80 and access to the e-mail server at port 25. Key point: The basic stance of a company firewall is: blocks all UDP traffic except for DNS blocks all incoming TCP connections but allows all outgoing ones allows incoming connections to public HTTP, FTP, SMTP, and DNS servers located in a "DMZ". blocks all ICMP traffic except for those packets needed for path MTU discovery. This allow most access to the Internet for end-users and allows the Internet to access the public servers. It blocks everything else. Contrast: The word "dynamic packet filter" was coined to contrast with the normal "static filter" rules in a firewall described above. Dynamic rules are needed because: Ports are a poor way of identifying protocols (and getting poorer) Whereas most communication uses only outbound connections, some (like FTP) use multiple connections in both directions. In the case of FTP, the client creates an outbound connection to the server, then the server creates separate inbound connections in order to transfer files to the client. Static firewall rules would block this incoming connection, dynamic rules monitor the state and temporarily change the static rules just to allow that connection. An example of a "dynamic" rule is to solve the FTP problem is: Block all incoming connections, but if the user has established a connection to port 21 on a server, then allowing incoming TCP connection from the server port 20 to ports higher than 1024 on the client. Another type of "dynamic" rule is one where the firewall does protocol analysis at layers higher than TCP. To contrast with the example above, the firewall might analyze the FTP connection looking for the PORT command. (The "PORT" command is the FTP protocol whereby the client tells the server which port is has opened to receive a file on). Checkpoint calls this protocol analysis "stateful packet inspection" in their firewall. Other vendors do similar stuff, but call it different names. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Packet filtering**

The action a device takes to selectively control the flow of data to and from a network. Packet filters allow or block packets, usually while routing them from one network to another (most often from the Internet to an internal network, and vice-versa). To accomplish packet filtering, you set up rules that specify what types of packets (those to or from a particular IP address or port) are to be allowed and what types are to be blocked. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Packet Switching**

The method used to move data around on the Internet. In packet switching,all the data coming out of a machine is broken up into chunks, each chunk has the address of where it came from and where it is going. This enables chunks of data from many different sources to co-mingle on the same lines, and be sorted and directed along different routes by special machines along the way. This way many people can use the same lines at the same time. You might think of several caravans of trucks all using the same road system. to carry materials. From Matisse <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pacman**

Chase Monsters in a Labyrinth You are Pacman, and you are supposed to eat all the small dots to get to the next level. You are also supposed to keep away from the ghosts, if they take you, you lose one life, unless you have eaten a large dot, then you can, for a limited amount of time, chase and eat the ghosts. There is also bonus available, for a limited amount of time. An X gives just points, but a little pacman gives an extra life. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PACS**

Public-Access Computing Systems From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAD**

Packet Assembling Disassembling (CCITT, X.3, X.28, X.29, PSDN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**padding**

Padding is the process of adding unused data to the end of a message in order to make it conform to a certain length. For example, block-ciphers often work on blocks that are 64-bits (8-bytes) long. Therefore, if you have a message that is 77-bytes long, you will need to "pad" it with an extra 3-bytes to make it an even 80-bytes in size (10-blocks). Key point: Padding is a regular feature of all crypto algorithms, including hashing and encryption. Some algorithms have been broken due to poor choices for padding. Most importantly, however, the size of the message can often reveal details about its contents. For example, let's assume a protocol whereby somebody accepts something with a simple message of "yes", but when it declines, it says "no" along with a reason why it was rejected. Therefore, even though the messages are encrypted, the "yes" will be a short message but the "no" will be a long message. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PADS**

Programmer's Advanced Debugging System From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pager**

opposite of more From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAL**

Privileged Architecture Library (DEC, Alpha) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAL**

Programmable Array Logic From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**palbart**

An enhanced version of the PAL PDP8 assembler PALBART is an enhanced version of the pdp8 PAL assembler. This is a PDP8 cross assembler. Its useful for the users of SIMH or any other PDP8 emulator. The original source code is available at: http://www.cs.uiowa.edu/~jones/pdp8/index.html To quote that web page, "This enhancement was written by Gary Messenbrink to support BART's fleet of PDP-8 systems." From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PALCD**

Plasma Addressable Liquid Crystal Display (LCD) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**palo**

Linux boot loader for parisc/hppa This package contains the parisc boot loader itself, plus palo which is the boot media management tool as lilo is for i386. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAM**

Paging Area Memory From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pam**

PAM (Pluggable Authentication Modules) is a system security tool which allows system administrators to set authentication policy without having to recompile programs which do authentication. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAM**

Pluggable Authentication Module (Linux, LISA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAM**

Pluggable Authentication Modules. A suite of shared libraries that determine how a user will be authenticated. For example, conventionally UNIX users authenticate themselves by supplying a password at the password prompt after they have typed their name at the login prompt. In many circumstances, such as internal access to workstations, this simple form of authentication is considered sufficient. In other cases, more information is warranted. If a user wants to log in to an internal system from an external source, like the Internet, more or alternative information may be required, perhaps a one-time password. PAM provides this type of capability and much more. Most important, PAM modules allow you to configure your environment with the necessary level of security. From Linux System Security <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAM**

Primary Access Method (BS2000) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAM**

Programmable Attribute Maps (DRAM, PCI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAM**

Pulse Amplification Modulation From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAM**

see pluggable authentication modules (PAM). From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAM (Pluggable Authentication Modules)**

A replaceable user authentication module for system security, which allows programs to be written without knowing which authentication scheme will be used. This allows a module to be replaced later with a different module without requiring rewriting the software. From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAML**

Publicly Accessible Mailing Lists (Internet, BBS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pam_krb5**

The pam_krb5 module is a Pluggable Authentication Module (PAM) thatcan be used with Linux-PAM and Kerberos 5. The pam_krb5 module supports password checking, ticket creation, optional TGT verification and conversion to Kerberos IV tickets. The pam_krb5afs module, for AFStokens, is also included in this package. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pam_smb**

The pam_smb module can be used to authenticate users using an external SMB server. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pan**

A Newsreader uses GTK, looks like Forte Agent. Pan is a newsreader, loosely based on Agent and Gravity, which attempts to be pleasant to use for new and advanced users alike. It has all the typical features found in newsreaders and also supports offline newsreading, sophisticated filtering, multiple connections, and a number of extra features for power users and alt.binaries fans. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAN**

Personal Account Number From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pan**

This is PAN, a powerful and user-friendly USENET newsreader for GNOME. The latest info and versions of Pan can always be found at http://pan.rebelbase.com/. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PANDORA**

Preserving and Accessing Networked Documentary Resources of Australia From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**panel**

The Gnome panel From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Panel**

The name for the Linux equivalent of the Windows Taskbar. From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pango**

A library to handle unicode strings as well as complex bidirectional or context dependent shaped strings. It is the next step on Gtk+ internationalization. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pango**

Pango is a system for layout and rendering of internationalized text. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PANIX**

Public Access internet/uNIX [system] (Unix, Internet, network) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**panorama**

A framework for 3D graphics production Panorama will include modeling, rendering, post-processing, animating, etc. Functionally, it is structured as an API, composed by two dynamic libraries, and several plugins, that you can optionally load in runtime. A simple console mode front-end for this API is included in the package, that can load a scene description in one of the supported scene languages and then outputs a single image file in any of the supported graphic formats. Its main features are: - Plugin architecture. Most elements in the system are plugin's. This means components are loaded as needed, and can be substituted, added, etc without recompiling anything. This will let third parties distribute their plugins outside the main distribution. - Object oriented scene description language, with classes, inheritance, etc. It's easy to use, and has a simple syntax. - Scene language is a plugin itself, so any other scene language can be used instead. - Several rendering methods are possible without any other change in input scene file. Currently supported methods are raytracing and zbuffer, but other methods are being tested and will be incorporated in the future. - A postprocessing system lets you apply filters to the whole image after it has been generated by renderer. - Similarly, there are object filters, that you can apply to an object in the rendering process. This means a new class of effects (e.g. a cartoon-like object in a photorealistic scene). - Materials have a BSDF (Bidirectional Scattering Distribution Function) that encapsulates its properties with respect to the light. Now, only Lambertian and Phong BSDF's are implemented, but more sophisticated ones will follow, like Schlick's, Ward's, etc. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pantomime1**

Objective-C library for mail handling (development files) Pantomime provides a set of Objective-C classes that model a mail system. Pantomime can be seen as a JavaMail 1.2 clone written in Objective-C. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAP**

Password Authentication Protocol (RFC 1334) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAP**

Password Authentication Protocol: The usual method of user authentication used on the internet: sending a username and password to a server where they are compared with a table of authorized users. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAP**

Printer Access Protocol (AppleTalk) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAP**

ProgrammAblaufPlan (DIN 66001) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAP (Password authentication Protocol)**

Authentication mechinisms used after logging in using PPP. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**paperconf**

print paper configuration information From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**paperconfig**

configure the system default paper size From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAPI**

PC voice API (API, PC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**par**

Paragraph reformatter Greatly enhanced fmt type program by Adam M. Costello. Can be used within vi or other editor to automatically reformat text in a variety of ways. Perfect for use with email & usenet messages as it correctly handles multiple levels of quoting characters. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAR**

Positive Acknowledgement with Retransmission [protocols] From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PAR**

Project Authorization Request (IEEE) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**paragui-themes**

Standard themes for the widget set library ParaGUI is a cross-platform high-level application framework and GUI (graphical user interface) library. ParaGUI's is completely based on the Simple DirectMedia Layer. This package contains standard themes files for the paragui library. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**parallel line Internet protocol (PLIP)**

A protocol that allows TCP/IP communication over a computer's parallel port using a specially designed cables. From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
