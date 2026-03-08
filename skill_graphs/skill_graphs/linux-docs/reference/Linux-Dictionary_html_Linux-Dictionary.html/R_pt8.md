
Time-series data storage and display system (tcl) RRD is the Acronym for Round Robin Database. RRD is a system to store and display time-series data (i.e. network bandwidth, machine-room temperature, server load average). It stores the data in a very compact way that will not expand over time, and it presents useful graphs by processing the data to enforce a certain data density. It can be used either via simple wrapper scripts (from shell or Perl) or via frontends that poll network devices and put friendly user interface on it. This package contains a tcl interface to RRDs. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RRIP**

Rock Ridge Interchange Protocol (CD, Unix) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rrlogind**

Login daemon for the Road Runner Cable Modem Service Login daemon for the Road Runner Cable Modem Service. You need a dhcp client as well. This program takes care of the authentication piece for the Road Runner Cable Modem Service. These areas include, but are not limited to: North Eastern Ohio, Columbus Ohio, Austin Texas, Hawaii, Tampa Bay Fla, and Charlotte NC. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RRZE**

Regionales RechenZentrum Erlangen (org.) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RRZN**

Regionales RechenZentrum fuer Niedersachsen (org.) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RS**

Recommended Standard From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RS**

Registry Service (DCE) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSA**

Random Scheduling Algorithm [protocol] From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSA**

Reference System Architecture From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSA**

Reusable Software Assets From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSA**

Rivest, Shamir and Adleman (cryptography, RSA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSA**

RSA is the name of the most prevalent public/private key algorithm. It is also the name of the company (RSA Security) that originally held the patent rights to this system. It was invented in 1977 by Ron Rivest, Adi Shamir, and Leonard Adleman. Details: In order to generate the keys: First, some random data is generated. Most of the successful attacks against RSA implementations have been against this step. Two large primes are randomly chosen. This can be a time consuming step as the computer randomly generates numbers and tests to see if they are prime. These two numbers are traditionally called p and q. The two numbers are multiplied together, n = pq. We will be publishing n as part of the public-key. The security of RSA lies in the fact that it is computationally too difficult to factor n back into p and q. (However, somebody may in the future discover a way to easily factor large numbers, in which case all of today's cryptography will be rendered useless in one fell swoop). A number e is chosen, where e is less than n and "relatively prime" (no common factors) to (p-1)(q-1). The public-key will consist of the pair (n,e). A number d is chosen, where (ed-1) is divisible by (p-1)(q-1). The private-key consists of the pair (n,d). Usually, the original prime numbers p and q are discarded after this step. The numbers n, e, and d are of interest because they serve as fields within digital certificates. Details: In order to encrypt/decrypt something using RSA, the following algorithm is used. Start with the original message called m. Note that in reality, we've already encrypted the real message with a randomly generated symmetric key, and we really are just encrypting this key to send along with the encrypted message. Public-key cryptography is generally used for key-exchange because it is too slow for general-purpose encryption. Therefore, m is really just a small 128-bit key rather than the entire message. Create the ciphertext c using the equation c = me mod n, where (n,e) are the public-key. Send the ciphertext message c. Upon reception, use the equation m = cd mod n, where (n,d) is the private-key and m is the decrypted message. (Again, this is usually just the symmetric key that we will use to decrypt the actual message). Point: RSA forms the basis for X.509 certificates in web servers and browsers. Key point: RSA Security charges a hefty license to use the RSA algorithm. However, the patent expires in September of the year 2000. At that time, the number of products using the RSA algorithm are likely to explode. Key point: An alternative to RSA is the "Diffie-Hellman" algorithm. This is used in many cases, but it is hampered by the fact that many products that could use it (like Netscape and Microsoft browsers) do not; for interoperability you often need to use RSA over DH. History: When exporting RSA was illegal, a popular form of disobedience would be to wear T-shirts with the algorithm or us it as part of your .sig. #!/bin/perl -sp0777i<X+d*lMLa^*lN%0]dsXx++lMlN/dsM0<j]dsj $/=unpack('H*',$_);$_=`echo 16dio\U$k"SK$/SM$n\EsN0p[lN*1lK[d2%Sa2/d0$^Ixp"|dc`;s/\W//g;$_=pack('H*',/((..)*)$/) Applications: PGP, SSL, SET, DNSSEC, SSH See also: DSA From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSAC**

Recreational Software Advisory Council (org.) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSAP**

Remote Service Access Point (SAP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSAREF**

RSA Reference Implementation. This was a fairly open implementation of the RSA algorithm that has been embedded into many problems. This is not the source code that RSA sells to vendors, but an open-source version that has been embedded within freeware/open-source products (like ssh). A patent-license is still required when using this code in commercial products, though. Key point: RSAREF has been supported by RSA (the company) for a long time, and a number of security holes have been found in this implementation. RSA wants people to use the BSAFE development kit instead. In late 1999 in particular, a bug was found that allows ssh to be hacked. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSAT**

Reliability and System Architecture Testing From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSCS**

Remote Source Control System From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSCS**

Remote Spooling Communications Subsystem (IBM, VM, NJE) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSDP**

Root System Description Pointer (ACPI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSDT**

Root System Description Table (ACPI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSE**

Removable Storage Elements From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSE**

Research and Systems Engineering From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSF**

Remote Support Facility From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSF**

ReStart active File (IBM, VM/ESA, CP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSFD**

Retrieve Subsequent File Descriptor (IBM, VM/ESA, CP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSFDNPR**

Retrieve Subsequent File Descriptor Not Previously Retrieved (IBM, VM/ESA, CP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rsh**

OpenSSH SSH client (remote login program) From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSH**

Remote SHell (Unix, BSD, Shell) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSH**

Restricted SHell (Unix, Shell) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rsh**

The rsh package contains a set of programs which allow users to run commands on remote machines, login to other machines, and copy files between machines (respectively, rsh, rlogin, and rcp). All three ofthese commands use rhosts style authentication. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rsh-client**

rsh clients. This package contains rsh, rcp and rlogin. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rsh-server**

rsh servers. This package contains rexecd, rlogind and rshd. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rsh-server**

The rsh-server package contains a set of programs which allow users to run commands on remote machines, login to other machines, and copy files between machines (respectively, rsh, rlogin, and rcp). All three of these commands use rhosts style authentication. This package contains the servers needed for all of these services. It also contains a server for rexec, an alternate method of executing remote commands. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSI**

Repetitive Strain Injury From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSIS**

Relocatable Screen Interface Specification From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSLM**

Remote Subscriber Line Module From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSM**

Remote Switching Module From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rsmtp**

Mail Transfer Agent From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSN**

Real Soon Now (slang) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSP**

Reality Signal Processor (Nintendo) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSPC**

Reed Solomon Product Code (SDD), "RS-PC" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rspfd**

Radio Shortest Path Daemon RSPF is a routing protocol for hamradio wireless links. This package provides a daemon with the latest version of the protocol. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSSCP**

Remote System Services Control Point (SSCP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rstart**

a sample implementation of a Remote Start client From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rstartd**

a sample implementation of a Remote Start rsh helper From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rstartd**

a sample implementation of a Remote Start rsh helper From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rstat-client**

A client for rstatd. This package contains rup(1) and rsysinfo(1), clients for rstatd. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rstatd**

Display uptime information for remote machines. This allows other machines on your local network to get information about your computer - especially uptime. This will allow you to use the rup(1) command. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSTS**

Resource Sharing Time Sharing (DEC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSTSE**

Resource System Time Sharing/Enhanced (DEC), "RSTS/E" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSU**

Remote Software Update (IBDM, OS/2, ...) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSU**

Remote Switching Unit From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSVP**

Resource reSerVation Protocol (IP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSX**

Realistic Sound eXperience (Intel, audio) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSX11**

Resource Sharing eXecutive - 11 (DEC, OS, PDP 11), "RSX-11" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RSX3D**

Realistic Sound eXperience - 3D (Intel, audio, VRML), "RSX-3D" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rsync**

fast remote file copy program (like rcp) rsync is a program that allows files to be copied to and from remote machines in much the same way as rcp. It has many more options than rcp, and uses the rsync remote-update protocol to greatly speed up file transfers when the destination file already exists. The rsync remote-update protocol allows rsync to transfer just the differences between two sets of files across the network link. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rsync**

Rsync uses a quick and reliable algorithm to very quickly bring remote and host files into sync. Rsync is fast because it just sends the differences in the files over the network (instead of sending the complete files). Rsync is often used as a very powerful mirroring process or just as a more capable replacement for the rcp command. A technical report which describes the rsync algorithmis included in this package. Install rsync if you need a powerful mirroring program. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RT**

Register Transfer From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RT**

Remote Terminal From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RT**

Research and Technology, "R&T" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RT**

Routing Type From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTA**

Rapid Thermal Annealling (IC, MOSFET) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTA**

Real-Time Accelerator From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTAM**

Remote Teleprocessing Access Method From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTB**

Read Tape Binary From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTBM**

Real Time Bit Mapping From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTC**

Real Time Clock From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTC**

Real-Time Command From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTCP**

Real Time Control Protocol (RTP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTCS**

Real Time Computer System From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTCU**

Real Time Control Unit From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTD**

Real Time Display From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTDAT**

RealTime Deformation And Tessellation [engine] (3D, Shiny), "RT-DAT" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTDHS**

Real Time Data Handling System From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTE**

Real Time Execution From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTE**

Real Time Executive (OS, HP, HP 2000) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTE**

Remote Terminal Emulation From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTE**

Run Time Environment From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTE6VM**

Real Time Executive - 6 / Virtual Memory (OS, HP, RTE, HP 1000), "RTE-6/VM" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTEX**

Real Time EXecutive (OS, Interdata) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTF**

Rich Text Format From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTF (Rich Text Format)**

A text formatting standard developed by Microseft Corporation that allows a wordprocrssing program to create a file encoded with all the document's formatting instructions, but without using any special hidden codes. An RTF-encoded document can be transmitted over telecommunications links or read by another RTF-compatible word processing program, without loss of the formatting. From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rtf2latex**

Convert RTF files to LaTeX rtf2latex converts Microsoft RTF (Rich Text Format) files to LaTeX source files. If imagemagick is installed, rtf2latex tries to use it to convert embedded images from the RTF source file. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rtf2rtf**

programs to postprocess the raw RTF generated by the mapping files From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTFF**

Read The F****** FAQ (slang, Usenet) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTFM**

Read The Flaming / F****** Manual (slang, Usenet, IRC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTG**

Real Time Gambling From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTG**

Real Time Geometry (manufacturer) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTG**

Routing Table Generator From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTI**

ReTurn from Interrupt From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTL**

Real Time Language From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTL**

Register Transfer Language (GCC) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTL**

Resistor-Transistor Logic From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTL**

RunTime Library From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTLinux**

FSMLabs makes RTLinux, providing hard real-time solutions. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTM**

Registered Transfer Module From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTM**

Release To Manufacture / Market From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTM**

Remote Test Module From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTMOS**

Real Time Multiprogramming Operating System (OS, GE) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTMP**

Routing Table Maintenance Protocol (AppleTalk) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTMS**

Real Time Multiprogramming System (???) (OS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTOS**

Real Time Operating System (OS, Interdata, Prime, ...) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTOS16**

Real Time Operating System - 16 (OS, Digico), "RTOS-16" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTOS360**

Real Time Operating System /360 (IBM, OS, S/360), "RTOS/360" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTOSUH**

Real Time Operating System - Universitaet Hannover (OS), "RTOS-UH" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTP**

Real Time Protocol (Internet, RFC 1889/1890, RTCP) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTS**

Real Time System From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTS**

Reliable Transfer Service (OSI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTS**

Request To Send (MODEM, RS-232) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTS**

Residual Time Stamp From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTSE**

Reliable Transfer Service Element (OSI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTSM**

RealTime System Manager From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTSP**

Real Time Streaming Protocol (TV, WWW, UDP, TCP/IP, RDP, Multicast) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTT**

Round-Trip Time From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTTI**

Run-Time Type Identification (ANSI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTTM**

Round-Trip Time Measurements (TCP, satellite) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTTS**

Real Time Task Scheduler (OS, August Systems) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTTY**

Radio Tele TYpe From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTU**

Real Time Unix (Unix) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTUX**

Real Time UniX (OS, Emerge Systems) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTV**

Real Time Video From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTVBR**

RealTime Variable Bit Rate (VBR, ATM), "rt-VBR" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTX**

Real Time eXecutive (OS) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RTX16**

Real Time eXecutive - 16 (OS, Honeywell, ...), "RTX-16" From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RU.nix**

RU.nix is devoted to running Linux on the PlayStation and on MIPS. Some of the site is in English, but to get real information you will need to read the Russian pages. Last entry dated January 22, 2003. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RUA**

Remote User Agent From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RUAC**

Remote User Access Centers From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rubibtex**

make a bibliography for (La)TeX using Russian letters as item names From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**ruby**

An interpreter of object-oriented scripting language Ruby Ruby is the interpreted scripting language for quick and easy object-oriented programming. It has many features to process text files and to do system management tasks (as in perl). It is simple, straight-forward, and extensible. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rubybook**

the "Programming Ruby" book This book is a tutorial nd reference for the Ruby programming language. Use Ruby, and you'll write better code, be more productive, and enjoy programming more. The book is a guide to working with the object-oriented programming language, teaching the basics, plus how to write large programs, how to extend Ruby using C code, and much more. This is the HTML version of the "Programming Ruby" book by David Thomas and Andrew Hunt, published by Addison-Wesley and graciously licensed under the Open Publication Licence. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rubymagick**

Ruby interface for ImageMagick Ruby interface for ImageMagick. (beta release) From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rubyunit**

Simple testing framework for Ruby RubyUnit is a simple Testing Framework for Ruby. You can get the information about Testing Framework on next web site: <URL:http://www.xprogramming.com/> From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**RUI**

Reality User Interface From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rumakeindex**

process a LaTeX index using Russian Cyrillic characters From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rumba-manifold-demo**

Sample programs that use RUMBA brain imaging main library Sample programs that use RUMBA brain imaging main library Main library From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rumba-utils**

RUMBA brain imaging utility programs RUMBA brain imaging system utility programs From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**rumbaview**

RUMBA project brain imaging viewer RUMBA project brain imaging viewer From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**run**

Watch programs and restart them if they die Run allows you to run a program, and ensure that you have only one of that program running simultaneously. i.e. we would like to run some program, but not if its already running. We also may need to restart the program if it dies. Run accomplishes these tasks giving all the functionality that would otherwise require tedious shell scripting to accomplish. PLEASE NOTICE that upstream considers this package "a broken program" and advises on his home page not to use run unless one is prepared to debug. However, run seems to be working reasonably well, but be warned. Remove the Conflicts: line from control file if you want to build on potato From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>
