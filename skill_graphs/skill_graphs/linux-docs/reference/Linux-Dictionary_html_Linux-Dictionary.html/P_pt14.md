
**PTP**

Picture Transfer Protocol (PIMA 15740) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PTR**

Paper Tape Reader From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PTSS**

People's Time Sharing System (OS; CDC 6600) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PTT**

Postes, Telegraphe et Telephone (org., Switzerland) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PTTP**

Point-to-PoinT Tunneling Protocol From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PTW**

Primary Translation Word From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ptx**

produce a permuted index of file contents From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PTY**

Pseudo-Terminal driver From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PU**

Physical Unit (NAU) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PU**

Power Unit From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PU**

Processing Unit From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUA**

Profiling User Agent From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUB**

Physical Unit Block From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Public Domain**

Software that is available to be used and modified by anyone, for any purpose, and may even be incorporated for distribution in commercial software. Public domain software is not copyrighted, and no rights are retained by the author. (Also, see Open Source and Shareware.) From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**public key**

A shared data file that is distributed to any interested recipient for the secure transmission of data. Used in conjunction with a private key to decrypt data. From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Public Key Encryption**

A method of data encryption that involves two separate keys: a public key and a private key. Data encrypted with the public key can be decrypted only with the private key and vice versa. Typically, the public key is published and can be used to encrypt data sent to the holder of the private key, and the private key is used to sign data. From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**public-key (private-key, asymmetric cryptography)**

Public-key cryptography uses two mathematically related keys, where a message encrypted by one key can only be decrypted by the other key. This is in stark contrast to traditional cryptography (now known as symmetric cryptography) where the same key was used for both encryption and decryption. The reason this is so important is because one of the two keys can be made public, hence the name "public-key cryptography". When this technique was discovered, it solved the biggest problem in cryptography at that time. In traditional symmetric cryptography, both the sender and receiver of a message had to agree upon the same key. Imagine your country has spies out in the field. If a spy gets captured, then the adversary could steal that key and decrypt messages. With asymmetric keys, however, the enemy can only steal the key the spy is using to encrypt messages, but cannot use that key to decrypt anything. The enemy may be able to forge messages, but the system wouldn't otherwise be compromised. Furthermore, the key could be extremely public: you could simply broadcast your public-key on the open airwaves for your spies to use. This is indeed what happens with SSL, the protocol you use to connect to e-commerce sites and pay for stuff with credit-cards. The public-key of the server is given out to everybody who connects to the site. However, each user encrypts his data using the public-key, which means nobody else can decrypt it without the secret private-key known only to the owners of the website. Example: Some uses of public-key encryption are: e-mail encryption Allows anybody to send an encrypted message to you that only you can read. The two most popular ways of doing this are PGP and S/MIME. digital signatures You can encrypt something with your private-key that can be decrypted by everyone (using your public-key). Therefore, if you encrypt a message, it proves it came from you, because only you know the private-key. Thus, you can digitally "sign" documents. President Clinton signed the "Electronic Signatures in Global and National Commerce Act" into law using a digital signature in this manner (using a smart-card with the password "Buddy"). Point: The public and private keys are mathematically related. In order to create them, you start with some randomly generated prime numbers. You then run these through some mathematical operations in order to generate the two keys. You publish one of the keys (making it "public") and you keep the other one private. Since the keys are rather large (hundreds of bytes), you generally store them in an encrypted file. Whenever you need to decrypt a message, you type in a password to decrypt the private-key, then use the private-key to decrypt the message. Key point: Protecting the "private key" from theft/disclosure is the most important thing any company can do. There is exist private keys whose value lie in the range of hundreds of millions if not billions of dollars (such as the key Verisign uses to sign certificates). The private key is usually protected with strong encryption based upon a strong password. In paranoid cases, parts of the password are given to different people, so that more than one person must be present in order to recover the private key for use (note: redundancy is also used, if the key is XYZ, then Alice knows XY, Bob knows YZ, and Charlene knows XZ, meaning that any two can unlock the private key). The paranoid things you see in movies about high-security installations apply: background checks on employees with access to the private key physical security consisting of photo IDs, searches, and strict entry/exit controls the two-person rule biometrics (retina/palm/finger/handwriting) additions to normal authentication physical keys Private-keys are frequently stored on separate objects. The most common is the floppy disk, which can be inserted into a server when booted, but removed to a safety deposit box. Other examples include crypto-cards. (Note: when you get a certificates from a CA, they usually require that the private-key never be stored on a computer). Servers that must use private keys must employ heavy countermeasures: intrusion detection systems firewalls (both packet filtering as well as more complex ones) frequent vulnerability assessments and auditing limited people who have access to the server full use of the security features of the server (i.e. turn on logging, enforce strong passwords, etc.) Example: Some public-key algorithms are: Diffie-Hellman The original one, though only designed for key-exchange. RSA The most popular algorithm. ElGamal Extends Diffie-Hellman algorithms to support the same features as RSA, such as encryption and digital-signatures. DSA Government standard for digital-signatures based upon ElGamal. Elliptic Curves Based upon a different mathematical problem from number theory and algebraic geometry. It results in smaller keys and faster operation, but is not as well analyzed as other systems. Other There are other systems based upon different hard-to-solve mathematical problems. Antonym: Sometimes the word "secret-key" is used as an antonym to "public-key" in order to highlight the fact that it is a shared-secret. Also, "symmetric" encryption is the antonym to "asymmetric". From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**public-key encryption**

An encryption scheme, introduced by Diffie and Hellman in 1976, where each person gets a pair of keys, called the public key and the private key. Each person's public key is published while the private key is kept secret. Messages are encrypted using the intended recipient's public key and can only be decrypted using his private key. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUC**

Peripheral Unit Controller From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUC**

Public Utilities Commission From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUCP**

Physical Unit Control Point (IBM, SNA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**puf**

Parallel URL fetcher puf is a download tool for UNIX-like systems. You may use it to download single files or to mirror entire servers. It is similar to GNU wget (and has a partly compatible command line), but has the ability to do many downloads in parallel. This is very interesting, if you have a high-bandwidth internet connection. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUFFT**

Purdue University Fast FORTRAN compiler (FORTRAN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUID**

Physical Unit IDentifier (IBM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUK**

Personal / PIN Unblocking Key (PIN) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUMA**

Power User's Macintosh Association (org., Apple) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUMA**

Processor Upgradable Modular Architecture From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUMA**

Programmable Universal Micro Accelerator From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pump**

Simple DHCP/BOOTP client. This is the DHCP/BOOTP client written by RedHat. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUMS**

Physical Unit Management Services From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUP**

PARC Universal packet Protocol From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pup**

Printer Utility Program This is a GUI utility for maintaining your printer under Linux. For uni-directional mode it supports the Lexmark Optra Color 40 and 45, Lexmark Optra E310, HP 2100M, HP 4000, and HP LJ4 Plus. For bi-directional mode it supports any PJL printer (or partially, depending on the printer). From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**purity**

Automated purity testing software. For many years now, the purity test, (in various forms) has been widely available on the net. This package provides an automated way of taking the test. Purity tests are an amusing way to see how much of a nerd or a hacker you are. More tests are available in the purity-off package. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**purity-off**

Sex related purity tests This package installs the sex related purity tests not included in the purity package. If you are offended by sex or by unusual sexual activities please do not install this package. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PURL**

Persistent Uniform Resource Locator (URL, WWW) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PUT**

Program Update Tape From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PV**

Physical Volume (LVM, HDD) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PVA**

Packetized Video Audio From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PVC**

Permanent Virtual Circuit (SVC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PVC**

Permanent Virtual Circuit / Channel / Connection (ATM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PVCC**

Permanent Virtual Channel Connection (ATM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PVCS**

Polytron Version Control System From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PVD**

Primary Volume Descriptor (CD, IS 9660) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PVITL**

Program-Variation-In-The-Large (SCM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PVITS**

Program-Variation-In-The-Small (SCM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PVM**

Parallel Virtual Machine (SMP, Cluster) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pvm**

Parallel Virtual Machine - binaries and shared libraries Console and communication daemon binaries for the Parallel Virtual Machine. Should be sufficient to utilize a node in a dynamically linked PVM program such as pvmpov. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PVN**

Private Virtual Network From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PVP**

Packet Video Protocol From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PVPC**

Permanent Virtual Path Connection (ATM) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PWB**

Printer Wire Board From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PWB**

Programmers Work Bench (MS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pwck**

verify integrity of password files From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pwconv**

convert to and from shadow passwords and groups. From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pwd**

print name of current/working directory From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PWD**

Print Working Directory (Unix) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pwdb-conf**

Configuration package for the libpwdb, the password database library. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pwgen**

Automatic Password generation pwgen generates random, meaningless but pronounceable passwords. These passwords contain either only lowercase letters, or upper and lower case mixed, or digits thrown in. Uppercase letters and digits are placed in a way that eases remembering their position when memorizing only the word. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pwm**

Lightweight window manager with frames PWM is a rather lightweight window manager for X11. It has the unique feature that multiple client windows can be attached to the same frame. This feature helps keeping windows, especially the numerous xterms, organized. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PWM**

Pulse Width Modulation (DVD) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PWN**

Peacenet World News From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PWSCS**

Programmable WorkStation Communication Services From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pwunconv**

convert to and from shadow passwords and groups. From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PWV**

Pulse-Wave Velocity From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PXE**

Preboot eXecution Environment (Intel) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pxe**

The pxe package contains the PXE (Preboot eXecution Environment) server and code needed for Linux to boot from a boot disk image on aLinux PXE server. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PXES Linux Thin Client**

PXES will convert any complaint hardware into a versatile thin client capable of accessing any Microsoft Terminal Server through RDP protocol. (Future versions will include XDM, VNC and other protocols). This thin client boots from the network. Version 0.4 was released March 27, 2002. Version 0.5-final was released September 3, 2002. Version 0.5.1-41 was released May 15, 2003. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pxfonts**

Palatino-likes fonts for TeX The PX fonts consist of: 1. virtual text roman fonts using Adobe Palatino (or URWPalladioL) with some modified and additional text symbols in the OT1, T1, and TS1 encoding 2. virtual text sans serif fonts using Adobe Helvetica (or URW NimbusSanL) with additional text symbols in OT1, T1, TS1, and LY1 encodings (Provided in the TX fonts distribution) 3. monospaced typewriter fonts in OT1, T1, TS1, and LY1 encodings (Provided in the TX fonts distribution) 4. math alphabets using Adobe Palatino (or URWPalladioL) with modified metrics 5. math fonts of all symbols corresponding to those of Computer Modern math fonts (CMSY, CMMI, CMEX, and Greek letters of CMR) 6. math fonts of all symbols corresponding to those of AMS fonts (MSAM and MSBM) 7. additional math fonts of various symbols From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**PY**

Person Years From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pybliographer**

A tool for manipulating bibliographic databases. It currently supports BibTeX, Medline, Ovid and Refer files. It is useful for viewing, editing and searching, but also to convert bibliographic databases into HTML pages for example. Home Page: http://canvas.gnome.org:65348/pybliographer/ From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pychecker**

Finds common bugs in python source code PyChecker is a tool for finding common bugs in python source code. It finds problems that are typically caught by a compiler for less dynamic languages, like C and C++. Because of the dynamic nature of python, some warnings may be incorrect; however, spurious warnings should be fairly infrequent. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pyching**

A Python program to cast and interpret I Ching hexagrams pyChing is a program that allows you to 'consult' the I Ching. The I Ching is an ancient Chinese book of wisdom, which, apart from being read as a book, has also traditionally been consulted as an oracle. pyChing allows you to perform an I Ching 'reading' using the coin oracle, and then look up a brief interpretation from the I Ching. pyChing is completely written in Python, a cross platform, object oriented, programming language, using the Tkinter interface to the Tk GUI toolkit. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pycmail**

mail sorter written in python mail sorter similar to procmail, written in python, using python syntax for mail delivery From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pydb**

An enhanced Python command-line debugger Pydb is a command-line debugger for Python. It is based on the standard Python debugger pdb, but has a number of added features. Particularly, it is suitable for use with DDD, a graphical debugger front end. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pydf**

colourised df(1)-clone pydf is all-singing, all-dancing, fully colourised df(1)-clone written in python. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pydict**

an English/Chinese Dictionary written with python/gtk This is an English/Chinese Dictionary written by Daniel Gau with python/gtk. The word base was originally from xdict, and was converted and modified by Daniel Gau and bv1al. This program can be run in both console mode and X Window GUI mode. Author: Daniel Gau <plateau@pagic.net> Maintainer: Shang-Feng Yang <sfyang@users.sourceforge.net> Home Page: http://www.linux.org.tw/~plateau/linux_notes/ http://sourceforge.net/projects/pydict/ From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pyftpd**

ftp daemon with advanced features multithreaded ftp daemon written in python, featuring advanced permission scheme, upload/download speed throttling, GUI configuration, internal database of users and more. Does not need to run as root. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pyg**

Python Mail <-> News Gateway Python Gateway Script from news to mail and vice versa. It is intended to be a full SMTP/NNTP rfc compliant gateway with whitelist manager. You will probably have to install a mail-transport-agent and/or news-transport-system package to manage SMTP/NNTP traffic. MTA is needed for mail2news service, since mail have to be processed on a box where pyg is installed. You can use a remote smtpserver for news2mail. News system is useful but not needed, since you can send articles to a remote SMTP server (ie: moderated NG) where is installed pyg, otherwise you will need it. It refers to rfc 822 (mail) and 850 (news). From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pygame**

SDL bindings for games development in Python A multimedia development kit for Python. Pygame provides modules for you to access the video display, play sounds, track time, read the mouse and joystick, control the CD player, render true type fonts and more. It does this using mainly the cross-platform SDL library, a lightweight wrapper to OS-specific APIs. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Pygmy**

Pygmy Linux is small distribution of the Linux operating system, based on Slackware 7.1. PL use UMSDOS filesystem, it allows an user to install a fully functional operating system, that co-exists peacefully with DOS/Win9x on the same partition. PL is Internet ready, it supports connection via modem and network card. It is a console minilinux, so there are no X windows, Netscape or etc. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pygtk2**

PyGTK is an extension module for python that gives you access to the GTK+widget set. Just about anything you can write in C with GTK+ you can write in python with PyGTK (within reason), but with all the benefits of python. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pygtk2-libglade**

This module contains a wrapper for the libglade library. Libglade allows a program to construct its user interface from an XML description, which allows the programmer to keep the UI and program logic separate. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pyne**

A Python-GTK powered GUI mail-/newsreader Pyne is a graphical (GTK+) offline news- and mailreader written in Python. Multiple POP3, SMTP, IMAP and NNTP boxes are supported. Features include threading of newsgroups, optional expiry of news and mail, filters, attachment support, etc. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pyOpenSSL**

High-level wrapper around a subset of the OpenSSL library, includes* SSL. Connection objects, wrapping the methods of Python's portable sockets* Callbacks written in Python* Extensive error-handling mechanism, mirroring OpenSSL's error codes... and much more ;) From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pyrite-publisher**

Convert html and text documents to palm DOC format Pyrite Publisher can convert a variety of input formats into several different variations on the palm doc format. This package requires python 2.1. This new version includes experimental support for a gui interface; see /usr/share/doc/pyrite-publisher/README.GUI for details. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pysol**

X11 solitaire game written in Python PySol is an X11 solitaire game with a number of nice features, including hints, autoplay, unlimited undo, player statistics, demo mode, selectable card set and background graphics, and integrated help. It currently plays over one hundred different games and variants, and has a plug-in architecture which makes adding more easy. Install python-cardsets for a wide variety of cardsets. Install pysol-sound-server and pysol-sounds to get support for sound effects and background music. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pysol-cardsets**

Additional card graphics for Pysol This package contains several additional sets of card graphics for the X11 solitaire game PySol. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pysol-sound-server**

Sound server for PySol When installed along with the pysol-sounds package, allows PySol to play sounds and background music. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**pysol-sounds**

Sounds and background music for use with PySol When this package is installed along with pysol-sound-server, PySol can play sounds and background music. It is mostly useless without the server. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
