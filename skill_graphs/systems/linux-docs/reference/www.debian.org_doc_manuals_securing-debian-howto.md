* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-apache-env.en.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch2.en.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-automatic-harden.en.html) ] [ [7](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch7.en.html) ] [ [8](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.en.html) ] [ [9](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch9.en.html) ] [ [10](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch10.en.html) ] [ [11](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-after-compromise.en.html) ] [ [12](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch12.en.html) ] [ [A](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-harden-step.en.html) ] [ [B](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-checklist.en.html) ] [ [C](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-snort-box.en.html) ] [ [D](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-bridge-fw.en.html) ] [ [E](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-bind-chuser.en.html) ] [ [F](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-fw-security-update.en.html) ] [ [G](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-ssh-env.en.html) ] [ [H](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-apache-env.en.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html) ]
* * *
#  Securing Debian Manual

* * *
##  Abstract
This document describes security in the Debian project and in the Debian operating system. Starting with the process of securing and hardening the default Debian GNU/Linux distribution installation, it also covers some of the common tasks to set up a secure network environment using Debian GNU/Linux, gives additional information on the security tools available and talks about how security is enforced in Debian by the security and audit team.
* * *
##  Copyright Notice
Copyright © 2002-2007 Javier Fern�ndez-Sanguino Pe�a
Copyright © 2001 Alexander Reelsen, Javier Fern�ndez-Sanguino Pe�a
Copyright © 2000 Alexander Reelsen
Some sections are copyright © their respective authors, for details please refer to [Credits and thanks!, Section 1.7](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html#s-credits).
Permission is granted to copy, distribute and/or modify this document under the terms of the
Permission is granted to make and distribute verbatim copies of this document provided the copyright notice and this permission notice are preserved on all copies.
Permission is granted to copy and distribute modified versions of this document under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one.
Permission is granted to copy and distribute translations of this document into another language, under the above conditions for modified versions, except that this permission notice may be included in translations approved by the Free Software Foundation instead of in the original English.
* * *
##  Contents
  * [1 Introduction](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html)
    * [1.1 Authors](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html#s-authors)
    * [1.2 Where to get the manual (and available formats)](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html#s1.2)
    * [1.3 Organizational notes/feedback](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html#s1.3)
    * [1.4 Prior knowledge](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html#s1.4)
    * [1.5 Things that need to be written (FIXME/TODO)](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html#s1.5)
    * [1.6 Changelog/History](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html#s-changelog)
    * [1.7 Credits and thanks!](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html#s-credits)
  * [2 Before you begin](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch2.en.html)
    * [2.1 What do you want this system for?](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch2.en.html#s2.1)
    * [2.2 Be aware of general security problems](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch2.en.html#s-references)
    * [2.3 How does Debian handle security?](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch2.en.html#s2.3)
  * [3 Before and during the installation](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html)
    * [3.1 Choose a BIOS password](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html#s-bios-passwd)
    * [3.2 Partitioning the system](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html#s3.2)
    * [3.3 Do not plug to the Internet until ready](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html#s3.3)
    * [3.4 Set a root password](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html#s3.4)
    * [3.5 Activate shadow passwords and MD5 passwords](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html#s3.5)
    * [3.6 Run the minimum number of services required](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html#s3.6)
    * [3.7 Install the minimum amount of software required](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html#s3.7)
    * [3.8 Read the Debian security mailing lists](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html#s3.8)
  * [4 After installation](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html)
    * [4.1 Subscribe to the Debian Security Announce mailing list](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-debian-sec-announce)
    * [4.2 Execute a security update](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-security-update)
    * [4.3 Change the BIOS (again)](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-bios-boot)
    * [4.4 Set a LILO or GRUB password](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-lilo-passwd)
    * [4.5 Disable root prompt on the initramfs](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-kernel-initramfs-prompt)
    * [4.6 Remove root prompt on the kernel](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-kernel-root-prompt)
    * [4.7 Restricting console login access](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-restrict-console-login)
    * [4.8 Restricting system reboots through the console](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-restrict-reboots)
    * [4.9 Mounting partitions the right way](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s4.9)
    * [4.10 Providing secure user access](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s4.10)
    * [4.11 Using tcpwrappers](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-tcpwrappers)
    * [4.12 The importance of logs and alerts](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-log-alerts)
    * [4.13 Adding kernel patches](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-kernel-patches)
    * [4.14 Protecting against buffer overflows](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s4.14)
    * [4.15 Secure file transfers](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s4.15)
    * [4.16 File system limits and control](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s4.16)
    * [4.17 Securing network access](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-network-secure)
    * [4.18 Taking a snapshot of the system](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s-snapshot)
    * [4.19 Other recommendations](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html#s4.19)
  * [5 Securing services running on your system](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html)
    * [5.1 Securing ssh](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s5.1)
    * [5.2 Securing Squid](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s5.2)
    * [5.3 Securing FTP](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s-ftp-secure)
    * [5.4 Securing access to the X Window System](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s5.4)
    * [5.5 Securing printing access (the lpd and lprng issue)](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s5.5)
    * [5.6 Securing the mail service](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s5.6)
    * [5.7 Securing BIND](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s-sec-bind)
    * [5.8 Securing Apache](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s5.8)
    * [5.9 Securing finger](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s5.9)
    * [5.10 General chroot and suid paranoia](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s-chroot)
    * [5.11 General cleartext password paranoia](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s5.11)
    * [5.12 Disabling NIS](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s5.12)
    * [5.13 Securing RPC services](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s-rpc)
    * [5.14 Adding firewall capabilities](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html#s-firewall-setup)
  * [6 Automatic hardening of Debian systems](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-automatic-harden.en.html)
    * [6.1 Harden](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-automatic-harden.en.html#s6.1)
    * [6.2 Bastille Linux](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-automatic-harden.en.html#s6.2)
  * [7 Debian Security Infrastructure](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch7.en.html)
    * [7.1 The Debian Security Team](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch7.en.html#s-debian-sec-team)
    * [7.2 Debian Security Advisories](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch7.en.html#s-dsa)
    * [7.3 Security Tracker](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch7.en.html#s7.3)
    * [7.4 Debian Security Build Infrastructure](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch7.en.html#s7.4)
    * [7.5 Package signing in Debian](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch7.en.html#s-deb-pack-sign)
  * [8 Security tools in Debian](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.en.html)
    * [8.1 Remote vulnerability assessment tools](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.en.html#s-vuln-asses)
    * [8.2 Network scanner tools](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.en.html#s8.2)
    * [8.3 Internal audits](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.en.html#s8.3)
    * [8.4 Auditing source code](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.en.html#s8.4)
    * [8.5 Virtual Private Networks](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.en.html#s-vpn)
    * [8.6 Public Key Infrastructure (PKI)](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.en.html#s8.6)
    * [8.7 SSL Infrastructure](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.en.html#s8.7)
    * [8.8 Antivirus tools](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.en.html#s8.8)
    * [8.9 GPG agent](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.en.html#s-gpg-agent)
  * [9 Developer's Best Practices for OS Security](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch9.en.html)
    * [9.1 Best practices for security review and design](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch9.en.html#s-bpp-devel-design)
    * [9.2 Creating users and groups for software daemons](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch9.en.html#s-bpp-lower-privs)
  * [10 Before the compromise](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch10.en.html)
    * [10.1 Keep your system secure](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch10.en.html#s-keep-secure)
    * [10.2 Do periodic integrity checks](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch10.en.html#s-periodic-integrity)
    * [10.3 Set up Intrusion Detection](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch10.en.html#s-intrusion-detect)
    * [10.4 Avoiding root-kits](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch10.en.html#s10.4)
    * [10.5 Genius/Paranoia Ideas — what you could do](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch10.en.html#s10.5)
  * [11 After the compromise (incident response)](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-after-compromise.en.html)
    * [11.1 General behavior](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-after-compromise.en.html#s11.1)
    * [11.2 Backing up the system](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-after-compromise.en.html#s11.2)
    * [11.3 Contact your local CERT](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-after-compromise.en.html#s11.3)
    * [11.4 Forensic analysis](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-after-compromise.en.html#s11.4)
  * [12 Frequently asked Questions (FAQ)](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch12.en.html)
    * [12.1 Security in the Debian operating system](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch12.en.html#s12.1)
    * [12.2 My system is vulnerable! (Are you sure?)](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch12.en.html#s-vulnerable-system)
    * [12.3 Questions regarding the Debian security team](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch12.en.html#s-debian-sec-team-faq)
  * [A The hardening process step by step](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-harden-step.en.html)
  * [B Configuration checklist](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-checklist.en.html)
  * [C Setting up a stand-alone IDS](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-snort-box.en.html)
  * [D Setting up a bridge firewall](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-bridge-fw.en.html)
    * [D.1 A bridge providing NAT and firewall capabilities](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-bridge-fw.en.html#sD.1)
    * [D.2 A bridge providing firewall capabilities](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-bridge-fw.en.html#sD.2)
    * [D.3 Basic IPtables rules](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-bridge-fw.en.html#sD.3)
  * [E Sample script to change the default Bind installation.](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-bind-chuser.en.html)
  * [F Security update protected by a firewall](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-fw-security-update.en.html)
  * [G `Chroot` environment for `SSH`](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-ssh-env.en.html)
    * [G.1 Chrooting the ssh users](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-ssh-env.en.html#sG.1)
    * [G.2 Chrooting the ssh server](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-ssh-env.en.html#sG.2)
  * [H `Chroot` environment for `Apache`](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-apache-env.en.html)
    * [H.1 Introduction](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-apache-env.en.html#sH.1)
    * [H.2 Installing the server](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-apache-env.en.html#sH.2)
    * [H.3 See also](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-apache-env.en.html#sH.3)


* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-apache-env.en.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch2.en.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch3.en.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch4.en.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-services.en.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-automatic-harden.en.html) ] [ [7](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch7.en.html) ] [ [8](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-sec-tools.en.html) ] [ [9](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch9.en.html) ] [ [10](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch10.en.html) ] [ [11](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch-after-compromise.en.html) ] [ [12](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch12.en.html) ] [ [A](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-harden-step.en.html) ] [ [B](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-checklist.en.html) ] [ [C](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-snort-box.en.html) ] [ [D](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-bridge-fw.en.html) ] [ [E](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-bind-chuser.en.html) ] [ [F](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-fw-security-update.en.html) ] [ [G](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-ssh-env.en.html) ] [ [H](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ap-chroot-apache-env.en.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html) ]
* * *
Securing Debian Manual
Version: 3.13, Sun, 08 Apr 2012 02:48:09 +0000

Javier Fernández-Sanguino Peña
[Authors, Section 1.1](https://tldp.org/LDP/www.debian.org/doc/manuals/securing-debian-howto/ch1.en.html#s-authors)


* * *
