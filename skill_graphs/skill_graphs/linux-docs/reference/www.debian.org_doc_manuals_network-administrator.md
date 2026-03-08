* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-index.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-intro.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-overview.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-tcpip.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-uucp.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-ppp.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-nfs.html) ] [ [7](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-nis.html) ] [ [8](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-bind.html) ] [ [9](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-router.html) ] [ [10](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-mail.html) ] [ [11](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-news.html) ] [ [12](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-ftp.html) ] [ [13](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-www.html) ] [ [14](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-security.html) ] [ [15](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-firewall.html) ] [ [16](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-kernel.html) ] [ [17](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-index.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-intro.html) ]
* * *
#  Debian GNU/Linux Network Administrator's Manual (Obsolete Documentation)

* * *
##  Abstract
The Debian GNU/Linux Network Administrator's Manual covers all network administration aspects of a Debian GNU/Linux system.
* * *
##  Copyright Notice
  * Copyright © 1997 Ardo van Rangelrooij


  * Copyright © 1998-2000 Ivan E. Moore II


  * Copyright © 1998 Duncon C. Thomson


This manual is free software; you may redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version.
This is distributed in the hope that it will be useful, but _without any warranty_ ; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License with your Debian GNU/Linux system, in /usr/share/common-licenses/GPL, or with the `debiandoc-sgml` source package as the file COPYING. If not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
* * *
##  Contents
  * [1 Introduction](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-intro.html)
    * [1.1 About this manual](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-intro.html#s1.1)
    * [1.2 Where to find newer versions](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-intro.html#s1.2)
    * [1.3 How this manual came about](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-intro.html#s1.3)
  * [2 Overview of a Debian GNU/Linux System](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-overview.html)
  * [3 TCP/IP](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-tcpip.html)
    * [3.1 Intro](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-tcpip.html#s3.1)
    * [3.2 IP Addresses](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-tcpip.html#s3.2)
    * [3.3 IP Interface Configuration](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-tcpip.html#s3.3)
    * [3.4 Basic IP Routing](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-tcpip.html#s3.4)
    * [3.5 Domain Name Service (DNS)](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-tcpip.html#s3.5)
    * [3.6 ICMP and IP Troubleshooting](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-tcpip.html#s3.6)
    * [3.7 TCP and UDP](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-tcpip.html#s3.7)
    * [3.8 Servers, Daemons and the Superserver](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-tcpip.html#s3.8)
  * [4 UUCP](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-uucp.html)
  * [5 PPP, SLIP, PLIP](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-ppp.html)
  * [6 NFS](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-nfs.html)
  * [7 NIS](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-nis.html)
  * [8 DNS/BIND](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-bind.html)
    * [8.1 Obtaining the necessary files](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-bind.html#s-bindnecessary)
    * [8.2 Configuring BIND](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-bind.html#s-bindconfig)
    * [8.3 Advanced Configuration](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-bind.html#s-bindadvance)
    * [8.4 Setting up a Primary DNS Server](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-bind.html#s-bindprimary)
    * [8.5 Setting up a Secondary DNS Server](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-bind.html#s-bindsecondary)
    * [8.6 Testing](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-bind.html#s-bindtest)
    * [8.7 Obtaining Help With BIND](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-bind.html#s-bindhelp)
  * [9 Router](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-router.html)
  * [10 Mail](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-mail.html)
    * [10.1 Post Office Protocol (POP3) software](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-mail.html#s10.1)
    * [10.2 Interactive Mail Access Protocol (IMAP) software](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-mail.html#s10.2)
    * [10.3 Simple Mail Transfer Protocol (SMTP) software](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-mail.html#s10.3)
    * [10.4 Other mail processing tools](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-mail.html#s10.4)
    * [10.5 Mailing lists handling software](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-mail.html#s10.5)
  * [11 News](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-news.html)
  * [12 FTP](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-ftp.html)
  * [13 WWW](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-www.html)
    * [13.1 Choosing a Web Server that's best for you](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-www.html#s13.1)
    * [13.2 Setting up your Web Server](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-www.html#s13.2)
    * [13.3 Web Proxies](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-www.html#s13.3)
    * [13.4 Tools and Other Programs](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-www.html#s13.4)
    * [13.5 Finding Help](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-www.html#s13.5)
  * [14 Security](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-security.html)
    * [14.1 Before you begin](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-security.html#s14.1)
    * [14.2 Security from a Network standpoint](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-security.html#s14.2)
    * [14.3 Security from a User standpoint](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-security.html#s14.3)
    * [14.4 Security Tools](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-security.html#s14.4)
    * [14.5 Things you can do](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-security.html#s14.5)
    * [14.6 Finding Help](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-security.html#s14.6)
  * [15 Firewall](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-firewall.html)
    * [15.1 Background information](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-firewall.html#s15.1)
    * [15.2 ipfwadm](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-firewall.html#s15.2)
    * [15.3 IP Masquerading (NAT)](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-firewall.html#s15.3)
    * [15.4 Using Proxy's](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-firewall.html#s15.4)
    * [15.5 Finding Help](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-firewall.html#s15.5)
  * [16 Kernel Configuration](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-kernel.html)
  * [17 Index](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-index.html)


* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-index.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-intro.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-overview.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-tcpip.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-uucp.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-ppp.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-nfs.html) ] [ [7](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-nis.html) ] [ [8](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-bind.html) ] [ [9](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-router.html) ] [ [10](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-mail.html) ] [ [11](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-news.html) ] [ [12](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-ftp.html) ] [ [13](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-www.html) ] [ [14](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-security.html) ] [ [15](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-firewall.html) ] [ [16](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-kernel.html) ] [ [17](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-index.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/network-administrator/ch-intro.html) ]
* * *
Debian GNU/Linux Network Administrator's Manual (Obsolete Documentation)
This manual is OBSOLETE and DEPRECATED since 2000, Instead see http://www.debian.org/doc/user-manuals#quick-reference

Ardo van Rangelrooij
Oliver Elphick
Ivan E. Moore II
Duncan C. Thomson


* * *
