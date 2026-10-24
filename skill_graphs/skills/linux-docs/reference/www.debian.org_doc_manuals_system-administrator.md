* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-index.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-intro.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-overview.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-files.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch4.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-directories.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-filesystems.html) ] [ [7](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-booting.html) ] [ [8](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-users.html) ] [ [9](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-sessions.html) ] [ [10](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-printing.html) ] [ [11](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-accounting.html) ] [ [12](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-backup.html) ] [ [13](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-X.html) ] [ [14](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-security.html) ] [ [15](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-config.html) ] [ [16](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html) ] [ [17](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-localisation.html) ] [ [18](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-index.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-intro.html) ]
* * *
#  Debian GNU/Linux System Administrator's Manual (Obsolete Documentation)

* * *
##  Abstract
The Debian GNU/Linux System Administrator's Manual covers all system administration aspects of a Debian GNU/Linux system.
* * *
##  Copyright Notice
  * Copyright © 1997 Ardo van Rangelrooij


  * Copyright © 1998 Oliver Elphick


  * Copyright © 1998 Tapio Lehtonen


This manual is free software; you may redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version.
This is distributed in the hope that it will be useful, but _without any warranty_ ; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License with your Debian GNU/Linux system, in /usr/doc/copyright/GPL, or with the `debiandoc-sgml` source package as the file COPYING. If not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
* * *
##  Contents
  * [1 Introduction](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-intro.html)
    * [1.1 About this manual](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-intro.html#s1.1)
    * [1.2 Where to find newer versions](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-intro.html#s1.2)
    * [1.3 Comments](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-intro.html#s1.3)
  * [2 Overview of a Debian GNU/Linux System](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-overview.html)
    * [2.1 The main components of a system](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-overview.html#s2.1)
  * [3 Files and Devices](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-files.html)
    * [3.1 Files](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-files.html#s3.1)
    * [3.2 Devices](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-files.html#s3.2)
  * [4 Programs and processes](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch4.html)
    * [4.1 Programs](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch4.html#s4.1)
    * [4.2 Processes](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch4.html#s4.2)
    * [4.3 The /proc filesystem](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch4.html#s4.3)
    * [4.4 Tools for handling programs and processes](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch4.html#s4.4)
  * [5 Directory Structure](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-directories.html)
    * [5.1 Directories](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-directories.html#s5.1)
    * [5.2 Permissions](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-directories.html#s5.2)
    * [5.3 Links](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-directories.html#s5.3)
    * [5.4 ACL - Access Control Lists](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-directories.html#s5.4)
    * [5.5 Tools for managing directories](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-directories.html#s5.5)
  * [6 Filesystems and Storage Media](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-filesystems.html)
    * [6.1 Storage devices and media](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-filesystems.html#s6.1)
    * [6.2 Types of filesystem](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-filesystems.html#s6.2)
    * [6.3 Quotas](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-filesystems.html#s6.3)
    * [6.4 Tools for managing filesystems](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-filesystems.html#s6.4)
  * [7 Boot and Shutdown](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-booting.html)
    * [7.1 Boot loaders](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-booting.html#s7.1)
  * [8 Managing User Accounts](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-users.html)
    * [8.1 Concepts](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-users.html#s8.1)
    * [8.2 Common tasks](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-users.html#s8.2)
    * [8.3 Tools reference](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-users.html#s8.3)
    * [8.4 Files reference](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-users.html#s8.4)
  * [9 Logging In and Out](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-sessions.html)
    * [9.1 Starting a session - logging in](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-sessions.html#s9.1)
  * [10 Printing](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-printing.html)
    * [10.1 Print devices](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-printing.html#s10.1)
    * [10.2 Spooler](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-printing.html#s10.2)
  * [11 Accounting](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-accounting.html)
    * [11.1 Concepts](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-accounting.html#s11.1)
  * [12 Backup and Restore](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-backup.html)
    * [12.1 Why backup?](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-backup.html#s12.1)
    * [12.2 What to backup?](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-backup.html#s12.2)
    * [12.3 Backup devices and media](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-backup.html#s12.3)
    * [12.4 Backup methods and software](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-backup.html#s12.4)
    * [12.5 Types of backup](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-backup.html#s12.5)
  * [13 X Windows](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-X.html)
    * [13.1 Overview of X](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-X.html#s13.1)
  * [14 Security](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-security.html)
    * [14.1 Threats](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-security.html#s14.1)
  * [15 System Configuration](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-config.html)
    * [15.1 ???](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-config.html#s15.1)
  * [16 Time](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html)
    * [16.1 Setting time, time zones and Daylight Saving](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html#s16.1)
    * [16.2 Setting and showing hardware clock](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html#s16.2)
    * [16.3 Multiboot with operating systems not understanding timezone](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html#s-multiboot-with)
    * [16.4 Syncing time, rdate and NTP](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html#s-syncing-time)
    * [16.5 Setting up an NTP server](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html#s16.5)
    * [16.6 Radio clocks](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html#s-radio-clocks)
    * [16.7 Timestamps](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html#s16.7)
    * [16.8 Time in cron](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html#s16.8)
  * [17 Localisation](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-localisation.html)
    * [17.1 Environment variables](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-localisation.html#s17.1)
  * [18 Index](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-index.html)


* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-index.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-intro.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-overview.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-files.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch4.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-directories.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-filesystems.html) ] [ [7](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-booting.html) ] [ [8](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-users.html) ] [ [9](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-sessions.html) ] [ [10](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-printing.html) ] [ [11](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-accounting.html) ] [ [12](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-backup.html) ] [ [13](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-X.html) ] [ [14](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-security.html) ] [ [15](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-config.html) ] [ [16](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html) ] [ [17](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-localisation.html) ] [ [18](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-index.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/system-administrator/ch-sysadmin-intro.html) ]
* * *
Debian GNU/Linux System Administrator's Manual (Obsolete Documentation)
This manual is OBSOLETE and DEPRECATED since 2006, 29 December 2009. Instead see http://www.de.debian.org/doc/user-manuals#quick-reference.

Ardo van Rangelrooij
Tapio Lehtonen
Oliver Elphick - Previous maintainer


* * *
