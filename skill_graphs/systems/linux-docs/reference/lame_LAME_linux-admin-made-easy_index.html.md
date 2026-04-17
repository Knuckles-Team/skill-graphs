# Linux Administration Made Easy
### by Steve Frampton, <frampton@LinuxNinja.com>
The "Linux Administration Made Easy" (LAME) guide attempts to describe day-to-day administration and maintenance issues commonly faced by Linux system administrators. Part of the Linux Documentation Project.
* * *

**Table of Contents**


1. [Preface](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/preface.html)


1.1. [Acknowledgements](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/acknowledgements.html)


1.2. [Copyright Information and Legal Disclaimers](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/copyright-and-disclaimer.html)


1.3. [A Plea for Help](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/help-plea.html)


2. [Introduction](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/introduction.html)


2.1. [Scope](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/scope.html)


2.2. [Choosing a Linux Distribution](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/choosing-linux.html)


3. [Linux Overview](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/linux-overview.html)


3.1. [What is Linux?](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/what-is-linux.html)


3.2. [Breaking the Myths](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/linux-myths.html)


3.3. [One User's Perspective](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/user-perspective.html)


4. [Installation and Hardware Configuration](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/install-config.html)


4.1. [Creating an Installation Diskette](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/install-diskette.html)


4.2. [Booting Linux Installation Program](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/booting-install.html)


4.3. [Partitioning Hard Drive(s)](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/install-partitioning.html)


4.4. [Setting up Swap Space](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/install-swap.html)


4.5. [Choosing Partitions to Format](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/install-format.html)


4.6. [Choosing Desired Packages to Install](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/install-packages.html)


4.7. [Hardware Configuration](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/install-configuration.html)


4.8. [Booting with LILO](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/install-lilo.html)


4.8.1. [Multi-boot with Other Operating Systems](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/install-lilo.html#INSTALL-LILO-MULTI)


4.9. [Downloading and Installing Red Hat Updates](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/update-redhat.html)


5. [Configuring the X Window System](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/xwindows-configuration.html)


5.1. [Getting the X Window System Working with X-Configurator](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/xwindows-xconfigurator.html)


5.2. [Using the X Desktop Manager](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/xwindows-xdm.html)


5.3. [Improving Font Appearance Under X](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/xwindows-fonts.html)


5.4. [Choosing a Window Manager for X](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/xwindows-winmgr.html)


5.5. [GNOME Installation and Configuration](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/using-gnome.html)


5.6. [KDE Installation and Configuration](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/using-kde.html)


6. [General System Administration Issues](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/administrative-issues.html)


6.1. [Root Account](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/root-account.html)


6.2. [Creating User Accounts](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/creating-user-accounts.html)


6.3. [Changing User Passwords](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/changing-user-passwords.html)


6.4. [Disabling User Accounts](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/disabling-user-accounts.html)


6.5. [Removing User Accounts](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/removing-user-accounts.html)


6.6. [Linux Password & Shadow File Formats](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/shadow-file-formats.html)


6.7. [System Shutdown and Restart](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/system-shutdown-and-restart.html)


7. [Custom Configuration and Administration Issues](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/custom-config.html)


7.1. [Web Server and HTTP Caching Proxy Administration](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/web-server-administration.html)


7.2. [Domain Name Server (DNS) Configuration and Administration](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/domain-name-server.html)


7.3. [Internet User Authentication with TACACS](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/internet-user-authentication.html)


7.4. [Windows-style File and Print Services with Samba](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/samba-file-and-print.html)


7.5. [Macintosh-style File and Print Services with Netatalk](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/netatalk-file-and-print.html)


7.6. [Network File System (NFS) Services](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/nfs-services.html)


7.7. [Configuration from A-Z with Linuxconf](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/linuxconf.html)


8. [Backup and Restore Procedures](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/backup-and-restore.html)


8.1. [Server Backup Procedures](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/server-backup.html)


8.1.1. [Backing up with ``tar'':](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/server-backup.html#TAR-BACKUP)


8.1.2. [Backing up with ``KDat'':](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/server-backup.html#KDAT-BACKUP)


8.2. [Server Restore Procedures](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/server-restore.html)


8.2.1. [Restoring with ``tar'':](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/server-restore.html#TAR-RESTORE)


8.2.2. [Restoring with ``KDat'':](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/server-restore.html#KDAT-RESTORE)


8.3. [Cisco Router Configuration Backups](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/router-configuration.html)


9. [Various & Sundry Administrative Tasks](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/various-and-sundry.html)


9.1. [Checking Storage Space](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/checking-storage-space.html)


9.2. [Managing Processes](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/managing-processes.html)


9.3. [Starting and Stopping Processes](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/redhat-processes.html)


9.4. [Automating Tasks with Cron and Crontab files](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/using-cron.html)


10. [Upgrading Linux and Other Applications](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/upgrading-linux.html)


10.1. [Using the Red Hat Package Manager (RPM)](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/using-rpm.html)


10.2. [Installing or Upgrading Without RPM](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/using-tarballs.html)


10.3. [Strategies for Keeping an Up-to-date System](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/keeping-up-to-date.html)


10.4. [Linux Kernel Upgrades](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/linux-kernel-upgrades.html)


10.5. [Upgrading a Red Hat Stock Kernel](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/kernel-upgrade.html)


10.6. [Building a Custom Kernel](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/kernel-custom.html)


10.7. [Moving to the Linux 2.2.x Kernels](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/linux-2.2.x.html)


10.8. [Configuring the Apache Web Server](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/apache-config.html)


10.9. [Configuring the Squid HTTP Caching Proxy Daemon](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/squid-upgrades.html)


10.10. [Configuring the Sendmail E-mail Daemon](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/sendmail-upgrades.html)


11. [Enterprise Computing with Linux](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/enterprise-computing.html)


11.1. [Performance Tuning](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/performance-tuning.html)


11.2. [High Availability with RAID](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/hardware-raid.html)


11.3. [Server Migration and Scalability Issues](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/server-migration.html)


12. [Strategies for Keeping a Secure Server](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/security.html)


13. [Help! Trouble in Paradise!](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/trouble-in-paradise.html)


13.1. [Getting Linux Installed on new, Unsupported Hardware](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/unsupported-tips.html)


13.2. [File System Corruption after Power Outage or System Crash](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/crash-repair.html)


13.3. [Where to Turn for Help](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/where-to-turn.html)


13.4. [Pointers to Additional Documentation](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/additional-docs.html)

* * *
|  | [Next](https://tldp.org/LDP/lame/LAME/linux-admin-made-easy/preface.html)
---|---|---
|  | Preface
