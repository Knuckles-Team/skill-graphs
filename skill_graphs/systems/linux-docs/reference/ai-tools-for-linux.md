[Skip to content](https://www.tecmint.com/install-icinga-in-centos-7/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-icinga-in-centos-7/)
Menu
Menu
  * [Learn Linux](https://www.tecmint.com/free-online-linux-learning-guide-for-beginners/ "Start Learning Linux")
  * [Linux Distros](https://www.tecmint.com/best-linux-distributions/ "Linux Distributions")
    * [Linux Distros for Beginners](https://www.tecmint.com/best-linux-distributions-for-beginners/)
    * [Linux Distros for Experts](https://www.tecmint.com/linux-distro-for-power-users/ "Widely Used Distros")
    * [New Linux Distros](https://www.tecmint.com/new-linux-distributions/)
    * [Linux Server Distros](https://www.tecmint.com/10-best-linux-server-distributions/)
    * [Secure Linux Distros](https://www.tecmint.com/best-security-centric-linux-distributions/)
    * [CentOS Alternatives](https://www.tecmint.com/centos-alternative-distributions/ "CentOS Alternative Distros")
    * [RedHat Distributions](https://www.tecmint.com/redhat-based-linux-distributions/ "RedHat Based Distros")
    * [Debian Distributions](https://www.tecmint.com/debian-based-linux-distributions/ "Debian Based Distros")
    * [Ubuntu Distributions](https://www.tecmint.com/ubuntu-based-linux-distributions/ "Ubuntu Based Distros")
    * [Arch Linux Distros](https://www.tecmint.com/arch-based-linux-distributions/ "Arch Linux Based Distros")
    * [Rolling Linux Distros](https://www.tecmint.com/best-rolling-release-linux-distributions/)
    * [KDE Linux Distros](https://www.tecmint.com/best-linux-distributions-for-kde-plasma/ "KDE Based Distros")
    * [Linux Distros for Old PC](https://www.tecmint.com/linux-distributions-for-old-computers/ "Linux Distros for Older Computers")
    * [Linux Distros for Kids](https://www.tecmint.com/best-linux-distributions-for-kids/)
    * [Linux Distributions for Students](https://www.tecmint.com/linux-distros-students/)
    * [Linux Distros for Windows](https://www.tecmint.com/best-alternative-linux-distributions-for-windows-users/)
  * [Commands](https://www.tecmint.com/category/linux-commands/ "Linux Commands")
    * [A – Z Linux Commands](https://www.tecmint.com/linux-commands-cheat-sheet/)
    * [100+ Linux Commands](https://www.tecmint.com/essential-linux-commands/ "Essential Linux Commands")
  * [Tools](https://www.tecmint.com/category/top-tools/ "Best Linux Software")
  * [Pro Courses](https://www.tecmint.com/install-icinga-in-centos-7/ "Linux Online Courses")
    * [Bash Scripting](https://pro.tecmint.com/learn-bash-scripting/ "Bash Scripting for Beginners")
    * [Learn Linux](https://pro.tecmint.com/learn-linux/ "Master Linux in 7 Days")
    * [AI for Linux](https://pro.tecmint.com/ai-for-linux/ "AI for Linux Course")
    * [RHCSA Certification](https://pro.tecmint.com/rhcsa-certification-course/ "RHCSA Certification Course")
    * [RHCE Certification](https://pro.tecmint.com/rhce-certification-course/ "RHCE Certification Course")
    * [LFCS Certification](https://pro.tecmint.com/lfcs-certification-course/ "LFCS Certification Course")
  *     * [RHCSA Exam](https://www.tecmint.com/rhcsa-exam-reviewing-essential-commands-system-documentation/ "RHCSA Certification eBook")
    * [RHCE Exam](https://www.tecmint.com/how-to-setup-and-configure-static-network-routing-in-rhel/ "RHCE Certification eBook")
    * [LFCS Exam](https://www.tecmint.com/sed-command-to-create-edit-and-manipulate-files-in-linux/ "LFCS Certification eBook")
    * [LFCE Exam](https://www.tecmint.com/installing-network-services-and-configuring-services-at-system-boot/ "LFCE Certification eBook")
    * [LFCA Exam](https://www.tecmint.com/understanding-linux-operating-system/ "LFCA Certification eBook")
    * [Ansible Exam](https://www.tecmint.com/understand-core-components-of-ansible/ "Ansible Certification eBook")
  * [About](https://www.tecmint.com/who-we-are/)
    * [Contact](https://www.tecmint.com/contact-us/ "Contact Us")
    * [Hiring](https://www.tecmint.com/hiring/ "Write for Us")
    * [Newsletter](https://www.tecmint.com/subscribe-to-blog/ "Linux Weekly Newsletter")
    * [Testimonials](https://www.tecmint.com/testimonials/)
    * [Donate](https://www.tecmint.com/donate-to-tecmint/ "Support TecMint")
    * [Advertise](https://www.tecmint.com/advertise/ "TecMint Sponsorship Opportunities")
    * [Submit Article Request](https://www.tecmint.com/submit-article-request/)
    * [Suggest an Update](https://www.tecmint.com/suggest-an-update/)


[](https://www.tecmint.com/install-icinga-in-centos-7/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
Menu
  * [Learn Linux](https://www.tecmint.com/free-online-linux-learning-guide-for-beginners/ "Start Learning Linux")
  * [Linux Distros](https://www.tecmint.com/best-linux-distributions/ "Linux Distributions")
    * [Linux Distros for Beginners](https://www.tecmint.com/best-linux-distributions-for-beginners/)
    * [Linux Distros for Experts](https://www.tecmint.com/linux-distro-for-power-users/ "Widely Used Distros")
    * [New Linux Distros](https://www.tecmint.com/new-linux-distributions/)
    * [Linux Server Distros](https://www.tecmint.com/10-best-linux-server-distributions/)
    * [Secure Linux Distros](https://www.tecmint.com/best-security-centric-linux-distributions/)
    * [CentOS Alternatives](https://www.tecmint.com/centos-alternative-distributions/ "CentOS Alternative Distros")
    * [RedHat Distributions](https://www.tecmint.com/redhat-based-linux-distributions/ "RedHat Based Distros")
    * [Debian Distributions](https://www.tecmint.com/debian-based-linux-distributions/ "Debian Based Distros")
    * [Ubuntu Distributions](https://www.tecmint.com/ubuntu-based-linux-distributions/ "Ubuntu Based Distros")
    * [Arch Linux Distros](https://www.tecmint.com/arch-based-linux-distributions/ "Arch Linux Based Distros")
    * [Rolling Linux Distros](https://www.tecmint.com/best-rolling-release-linux-distributions/)
    * [KDE Linux Distros](https://www.tecmint.com/best-linux-distributions-for-kde-plasma/ "KDE Based Distros")
    * [Linux Distros for Old PC](https://www.tecmint.com/linux-distributions-for-old-computers/ "Linux Distros for Older Computers")
    * [Linux Distros for Kids](https://www.tecmint.com/best-linux-distributions-for-kids/)
    * [Linux Distributions for Students](https://www.tecmint.com/linux-distros-students/)
    * [Linux Distros for Windows](https://www.tecmint.com/best-alternative-linux-distributions-for-windows-users/)
  * [Commands](https://www.tecmint.com/category/linux-commands/ "Linux Commands")
    * [A – Z Linux Commands](https://www.tecmint.com/linux-commands-cheat-sheet/)
    * [100+ Linux Commands](https://www.tecmint.com/essential-linux-commands/ "Essential Linux Commands")
  * [Tools](https://www.tecmint.com/category/top-tools/ "Best Linux Software")
  * [Pro Courses](https://www.tecmint.com/install-icinga-in-centos-7/ "Linux Online Courses")
    * [Bash Scripting](https://pro.tecmint.com/learn-bash-scripting/ "Bash Scripting for Beginners")
    * [Learn Linux](https://pro.tecmint.com/learn-linux/ "Master Linux in 7 Days")
    * [AI for Linux](https://pro.tecmint.com/ai-for-linux/ "AI for Linux Course")
    * [RHCSA Certification](https://pro.tecmint.com/rhcsa-certification-course/ "RHCSA Certification Course")
    * [RHCE Certification](https://pro.tecmint.com/rhce-certification-course/ "RHCE Certification Course")
    * [LFCS Certification](https://pro.tecmint.com/lfcs-certification-course/ "LFCS Certification Course")
  *     * [RHCSA Exam](https://www.tecmint.com/rhcsa-exam-reviewing-essential-commands-system-documentation/ "RHCSA Certification eBook")
    * [RHCE Exam](https://www.tecmint.com/how-to-setup-and-configure-static-network-routing-in-rhel/ "RHCE Certification eBook")
    * [LFCS Exam](https://www.tecmint.com/sed-command-to-create-edit-and-manipulate-files-in-linux/ "LFCS Certification eBook")
    * [LFCE Exam](https://www.tecmint.com/installing-network-services-and-configuring-services-at-system-boot/ "LFCE Certification eBook")
    * [LFCA Exam](https://www.tecmint.com/understanding-linux-operating-system/ "LFCA Certification eBook")
    * [Ansible Exam](https://www.tecmint.com/understand-core-components-of-ansible/ "Ansible Certification eBook")
  * [About](https://www.tecmint.com/who-we-are/)
    * [Contact](https://www.tecmint.com/contact-us/ "Contact Us")
    * [Hiring](https://www.tecmint.com/hiring/ "Write for Us")
    * [Newsletter](https://www.tecmint.com/subscribe-to-blog/ "Linux Weekly Newsletter")
    * [Testimonials](https://www.tecmint.com/testimonials/)
    * [Donate](https://www.tecmint.com/donate-to-tecmint/ "Support TecMint")
    * [Advertise](https://www.tecmint.com/advertise/ "TecMint Sponsorship Opportunities")
    * [Submit Article Request](https://www.tecmint.com/submit-article-request/)
    * [Suggest an Update](https://www.tecmint.com/suggest-an-update/)


[](https://www.tecmint.com/install-icinga-in-centos-7/)
# Icinga: A Next Generation Open Source ‘Linux Server Monitoring’ Tool for RHEL/CentOS 7.0
[Matei Cezar](https://www.tecmint.com/author/cezarmatei/ "View all posts by Matei Cezar")Last Updated: April 23, 2016 Read Time: 5 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [19 Comments](https://www.tecmint.com/install-icinga-in-centos-7/#comments)
**Icinga** is a modern open source monitoring tool that originated from a **Nagios** fork, and now has two parallel branches, **Icinga 1** and **Icinga 2**. What this tool does is, not to different from Nagios due to the fact that it still uses Nagios plugins and add-ons and even configuration files to check and monitor network services and hosts, but some differences can be spotted on web interfaces, especially on new web interface, reporting capability and easy add-ons development.
![Install Icinga Monitoring Tool in CentOS](https://www.tecmint.com/wp-content/uploads/2014/08/Install-Icinga-Monitoring-Tool-in-CentOS.png)Install Icinga Monitoring Tool in CentOS/RHEL 7.0
This topic will concentrate on a basic installation of **Icinga 1** Monitoring Tool from binaries on **CentOS** or **RHEL 7** , using **RepoForge** (previously known as RPMforge) repositories for CentOS 6, with the classical web interface held by Apache Webserver and the use of Nagios Plugins that will be installed on your system.
**Read Also** : [Install Nagios Monitoring Tool in RHEL/CentOS](https://www.tecmint.com/install-nagios-in-linux/)
#### Requirements
A basic **LAMP** installation on RHEL/CentOS 7.0 without MySQL and PhpMyAdmin, but with these PHP modules: **php-cli**
**php-pear** **php-xmlrpc** **php-xsl** **php-pdo** **php-soap** **php-gd**.
  1. [Installing Basic LAMP in RHEL/CentOS 7.0](https://www.tecmint.com/install-lamp-in-centos-7/)


### Step 1: Installing Icinga Monitoring Tool
**1.** Before proceeding with Icinga installation from binaries add **RepoForge** repositories on your system by issuing the following command, depending on your machine.
##### For 86-64-bit
```
# rpm -Uvh http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
```

##### For 32-bit
```
# rpm -Uvh http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.i686.rpm
```
![Install RepoForge in CentOS](https://www.tecmint.com/wp-content/uploads/2014/08/Install-RepoForge-in-CentOS-620x133.png)Install RepoForge Repository
**2.** After RepoForge repositories had been added on your system, start with Icinga basic installation without the web interface yet, by running the following command.
```
# yum install icinga icinga-doc
```
![Install Icinga in CentOS](https://www.tecmint.com/wp-content/uploads/2014/08/Install-Icinga-in-CentOS-620x300.png)Install Icinga Monitoring Tool
**3.** The next step is to try to install Icinga web interface provided by **icinga-gui** package. It seems that for the moment this package has some unresolved issues with CentOS/RHEL 7, and will generate some transaction check errors, but you can feel free to try to install the package, maybe meanwhile the problem was resolved.
Still, if you get the same errors on your machine as the pictures below shows you, use the following approach as further described, to be able to install Icinga web interface.
```
# yum install icinga-gui
```
![Install Icinga Gui in CentOS](https://www.tecmint.com/wp-content/uploads/2014/08/Install-Icinga-Gui-620x318.png)Install Icinga Gui ![Icinga Gui Conflict Error](https://www.tecmint.com/wp-content/uploads/2014/08/Icinga-Gui-Conflict-Error-620x311.png)Icinga Gui Conflict Error
**4.** The procedure to install **icinga-gui** package which provides the web interface is the following. First download the binary package form RepoForge website using **wget** command.
##### For 86-64-bit
```
# wget http://pkgs.repoforge.org/icinga/icinga-gui-1.8.4-4.el6.rf.x86_64.rpm
```

##### For 32-bit
```
# wget http://pkgs.repoforge.org/icinga/icinga-gui-1.8.4-4.el6.rf.i686.rpm
```
![Install Icinga RPM Package](https://www.tecmint.com/wp-content/uploads/2014/08/install-Icinga-Gui-rpm-620x300.png)Install Icinga RPM Package
**5.** After wget finishes downloading the package, create a directory named **icinga-gui** (you can choose other name if you want), move **icinga-gui** RPM binary to that folder, enter the folder and extract RPM package contents by issuing the next series of commands.
```
# mkdir icinga-gui
# mv icinga-gui-* icinga-gui
# cd icinga-gui
# rpm2cpio icinga-gui-* | cpio -idmv
```
![Copy Icinga GUI Packages](https://www.tecmint.com/wp-content/uploads/2014/08/Copy-Icinga-Gui-RPM-620x301.png)Copy Icinga GUI Packages
**6.** Now that you have the extracted **icinga-gui** package, use **ls** command to visualize folder content – it should result three new directories – **etc** , **usr** and **var**. Start by executing a recursive copying of all three resulted directories on your system root file system layout.
```
# cp -r etc/* /etc/
# cp -r usr/* /usr/
# cp -r var/* /var/
```
![Copy Directories Recursively in Linux](https://www.tecmint.com/wp-content/uploads/2014/08/Copy-Directories-Recursively-620x166.png)Copy Directories Recursively
### Step 2: Modify Icinga Apache Configuration file and System Permissions
**7.** As presented on this article introduction, your system needs to have Apache HTTP server and PHP installed in order to be able to run Icinga Web Interface.
After you finished the above steps, a new configuration file should be now present on Apache **conf.d** path named **icinga.conf**. In order to be able to access Icinga from a remote location from browser, open this configuration file and replace all its content with the following configurations.
```
# nano /etc/httpd/conf.d/icinga.conf
```

Make sure you replace all file content with the following.
```
ScriptAlias /icinga/cgi-bin "/usr/lib64/icinga/cgi"

<Directory "/usr/lib64/icinga/cgi">
#  SSLRequireSSL
   Options ExecCGI
   AllowOverride None
   AuthName "Icinga Access"
   AuthType Basic
   AuthUserFile /etc/icinga/passwd

   <IfModule mod_authz_core.c>
      # Apache 2.4
      <RequireAll>
         Require all granted
         # Require local
         Require valid-user
      </RequireAll>
   </IfModule>

   <IfModule !mod_authz_core.c>
      # Apache 2.2
      Order allow,deny
      Allow from all
      #  Order deny,allow
      #  Deny from all
      #  Allow from 127.0.0.1
      Require valid-user
    </IfModule>
 </Directory>

Alias /icinga "/usr/share/icinga/"

<Directory "/usr/share/icinga/">

#  SSLRequireSSL
   Options None
   AllowOverride All
   AuthName "Icinga Access"
   AuthType Basic
   AuthUserFile /etc/icinga/passwd

   <IfModule mod_authz_core.c>
      # Apache 2.4
      <RequireAll>
         Require all granted
         # Require local
         Require valid-user
      </RequireAll>
   </IfModule>

   <IfModule !mod_authz_core.c>
      # Apache 2.2
      Order allow,deny
      Allow from all
      #  Order deny,allow
      #  Deny from all
      #  Allow from 127.0.0.1
      Require valid-user
   </IfModule>
</Directory>
```

**8.** After you have edited Icinga httpd configuration file, add Apache system user to Icinga system group and use the following system permissions on next system paths.
```
# usermod -aG icinga apache
# chown -R icinga:icinga /var/spool/icinga/*
# chgrp -R icinga /etc/icinga/*
# chgrp -R icinga /usr/lib64/icinga/*
# chgrp -R icinga /usr/share/icinga/*
```

**9.** Before starting Icinga system process and Apache server, make sure you also disable **SELinux** security mechanism by running **setenforce 0** command and make the changes permanent by editing **/etc/selinux/config** file, changing SELINUX context from **enforcing** to **disabled**.
```
# nano /etc/selinux/config
```

Modify SELINUX directive to look like this.
```
SELINUX=disabled
```
![Disable SELinux in CentOS](https://www.tecmint.com/wp-content/uploads/2014/08/Disable-SELinux-620x246.png)Disable SELinux
You can also use **getenforce** command to view SELinux status.
**10.** As the last step before starting Icinga process and web interface, as a security measure you can now modify Icinga Admin password by running the following command, and then start both processes.
```
# htpasswd -cm /etc/icinga/passwd icingaadmin
# systemctl start icinga
# systemctl start httpd
```
![Create Icinga Admin Password](https://www.tecmint.com/wp-content/uploads/2014/08/Create-IcingaAdmin-Password-620x156.png)Create Icinga Admin Password ![Start Icinga Service](https://www.tecmint.com/wp-content/uploads/2014/08/Start-Icinga-Service-620x286.png)Start Icinga Service
### Step 3: Install Nagios Plugins and Access Icinga Web Interface
**11.** In order to start monitoring public external services on hosts with Icinga, such as HTTP, IMAP, POP3, SSH, DNS, ICMP ping and many others services accessible from internet or LAN you need to install **Nagios Plugins** package provided by **EPEL** Repositories.
```
# rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-6.noarch.rpm
# yum install yum install nagios-plugins nagios-plugins-all
```
![Install Epel Repo in CentOS](https://www.tecmint.com/wp-content/uploads/2014/08/Install-Epel-Repository-620x119.png)Install Epel Repository ![Install NRPE Plugin in CentOS](https://www.tecmint.com/wp-content/uploads/2014/08/Install-Nagios-Plugin-620x291.png)Install Nagios Plugin
**12.** To login on Icinga Web Interface, open a browser and point it to the URL **http://system_IP/icinga/**. Use **icingaadmin** as username and the password that you changed earlier and you can now see your localhost system status.
![Icinga Admin Login](https://www.tecmint.com/wp-content/uploads/2014/08/Icinga-Admin-Login-620x323.png)Icinga Admin Login ![Icinga Monitoring Dashboard](https://www.tecmint.com/wp-content/uploads/2014/08/Icinga-Dashboard-620x308.png)Icinga Monitoring Dashboard
That’s all! Now you have Icinga basic with the classical web interface – nagios like – installed and running on your system. Using Nagios Plugins you can now start adding new hosts and external services to check and monitor by editing Icinga configuration files located on **/etc/icinga/** path. If you need to monitor internal services on remote hosts then you must install an agent on remote hosts like NRPE, NSClient++, SNMP to gather data and send it to Icinga main process.
**Read Also**
  1. [Install NRPE Plugin and Monitor Remote Linux Hosts](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/)
  2. [Install NSClient++ Agent and Monitor Remote Windows Hosts](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/)


Tags [icinga](https://www.tecmint.com/tag/icinga/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[The Story Behind Acquisition of ‘MySQL’ by Sun Microsystem and the Rise of ‘MariaDB’](https://www.tecmint.com/the-story-behind-acquisition-of-mysql-and-the-rise-of-mariadb/)
Next article:
[How to Extend/Reduce LVM’s (Logical Volume Management) in Linux – Part II](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/)
![Photo of author](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=100&d=blank&r=g)
Matei Cezar
I'am a computer addicted guy, a fan of open source and linux based system software, have about 4 years experience with Linux distributions desktop, servers and bash scripting.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-icinga-in-centos-7/#respond)** or
## Related Posts
[![Linux Disk I/O Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2015/04/Linux-Disk-IO-Monitoring-Tools.png)](https://www.tecmint.com/monitor-linux-disk-io-performance/ "7 Best Tools to Monitor and Debug Disk I/O Performance in Linux")
[7 Best Tools to Monitor and Debug Disk I/O Performance in Linux](https://www.tecmint.com/monitor-linux-disk-io-performance/)
[![Disk Usage Monitoring Script in Linux](https://www.tecmint.com/wp-content/uploads/2014/01/linux-disk-usage-monitoring-shell-script.webp)](https://www.tecmint.com/monitor-disk-usage-bash-script/ "A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%")
[A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%](https://www.tecmint.com/monitor-disk-usage-bash-script/)
[![Linux Performance Monitoring with Command-Line Tools](https://www.tecmint.com/wp-content/uploads/2023/08/command-line-monitoring-tools-linux.webp)](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/ "24 Best Command Line Tools to Monitor Linux Performance")
[24 Best Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)
[![atop: System and process monitor for Linux](https://www.tecmint.com/wp-content/uploads/2025/06/atop-System-and-process-monitor-for-Linux.webp)](https://www.tecmint.com/atop-linux-performance-monitoring/ "How to Install ‘atop’ to Monitor Real-Time System Performance")
[How to Install ‘atop’ to Monitor Real-Time System Performance](https://www.tecmint.com/atop-linux-performance-monitoring/)
[![Bash Script to Monitor Linux Health Daily](https://www.tecmint.com/wp-content/uploads/2025/06/bash-script-automate-system-health-checks.webp)](https://www.tecmint.com/bash-script-automate-system-health-checks/ "How to Automate Daily Linux Health Checks with a Bash Script + Cron")
[How to Automate Daily Linux Health Checks with a Bash Script + Cron](https://www.tecmint.com/bash-script-automate-system-health-checks/)
[![Network Bandwidth Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2013/07/network-bandwidth-monitoring-tools.webp)](https://www.tecmint.com/network-bandwidth-monitoring-tools/ "5 Modern VnStat PHP Replacements for Bandwidth Monitoring")
[5 Modern VnStat PHP Replacements for Bandwidth Monitoring](https://www.tecmint.com/network-bandwidth-monitoring-tools/)
### 19 Comments
[Leave a Reply](https://www.tecmint.com/install-icinga-in-centos-7/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/bb7d31aba39ad9541d307c7754cb2a0710ca3ac42f0b0692aaca7d38229aeb03?s=50&d=blank&r=g)
keshav Kumar
[ April 18, 2017 at 11:13 am  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-884430)
Hi Team,
I am getting the below error message while installing the rpm forge packages. Could you please assist me on this.
`
 # rpm -Uvh http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
 Retrieving http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm
 curl: (7) Failed to connect to pkgs.repoforge.org port 80: Connection timed out
 error: skipping http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el6.rf.x86_64.rpm - transfer failed
 `
Thanks
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-884430)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ April 19, 2017 at 12:31 am  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-884518)
Unfortunately, repoforge is currently unmaintained and outdated by its maintainers and seems to be decommissioned very soon. Try to use EPEL repositories project instead.
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-884518)
  2. ![](https://secure.gravatar.com/avatar/e5a4a932bc9dad97a58bdcbac27098740132bb1fc5c095f861d61fee347a0eec?s=50&d=blank&r=g)
Neha Joshua
[ September 29, 2016 at 5:26 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-821893)
I have been currently using SeaLion (
Key Features
Jump back in time
Custom metrics
Custom commands
Real time Monitoring
View Raw outputs
Receive alerts
FREE 14-Day Trial. TRY Sealion- Server monitoring in just 2 steps!!
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-821893)
  3. ![](https://secure.gravatar.com/avatar/0640c9da25c373aac29c6da3cc08f434163b27331e287515451f69d34d7d99d7?s=50&d=blank&r=g)
Somia
[ January 19, 2015 at 9:59 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-457090)
Hello,
I’m installing Icinga in CentOS7, and I arrived to the step 11, but the following link (the link you publish) rpm -Uvh
When I execute the command, it returns an error saying:
The requested URL returned error: 404 Not Found
Please Help
Thank’s in advance
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-457090)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 20, 2015 at 11:25 am  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-457623)
@Somia,
Thanks, we’ve added working link now, could you please check and confirm..
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-457623)
       * ![](https://secure.gravatar.com/avatar/0640c9da25c373aac29c6da3cc08f434163b27331e287515451f69d34d7d99d7?s=50&d=blank&r=g)
Somia
[ February 2, 2015 at 4:26 am  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-470881)
I’m sorry but the team decided to uninstall it. They said that it is not secure to have it in the server and it is not answering our request which is to monitor the logs (if there is any attacks) [we’re students and we made a web site which should be secure and is attacked by other students]
any solution you suggest please?
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-470881)
     * ![](https://secure.gravatar.com/avatar/5e8c31388aac2da53fa71f34e7a26c5921b3176222c49143537372993db60236?s=50&d=blank&r=g)
Dizzo
[ July 1, 2016 at 9:45 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-796726)
Try

worked for me.
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-796726)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ July 2, 2016 at 7:32 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-796954)
The epel release download link pagages change often. In order to stay up to date with the latest release links visit the following links to download the rpm packages:

[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-796954)
  4. ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ September 19, 2014 at 2:00 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-278022)
@sarfaraz: To monitor client machines internal services you must install Nagios NRPE. Client external services can be monitored directly from Icinga server.
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-278022)
  5. ![](https://secure.gravatar.com/avatar/ae37f5fbcfce4861ace357f7dfde20dfc0ebfa070b772ab06bd2005d9c3cbd48?s=50&d=blank&r=g)
909
[ August 12, 2014 at 6:10 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-237945)
At step 10, you forgot to add the user in the first cmd line:
# htpasswd -cm /etc/icinga/passwd icingaadmin
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-237945)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 13, 2014 at 5:53 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-238725)
Corrected in the write-up and thanks for informing..
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-238725)
  6. ![](https://secure.gravatar.com/avatar/ebcf7bc534ff0e63c758ec13fa595a817b1a9b80f0a8ce903512fa057cd1b296?s=50&d=blank&r=g)
Samtjin
[ August 11, 2014 at 11:14 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-237306)
never ever disable SElinux
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-237306)
  7. ![](https://secure.gravatar.com/avatar/cb821678493485242e4374000234719d2a83b2d26bb12616fee3513da8e252ff?s=50&d=blank&r=g)
Alex
[ August 11, 2014 at 11:10 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-237302)
Hi, icinga 1 vs icinga2?, which is the best?
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-237302)
  8. ![](https://secure.gravatar.com/avatar/bffc88b6705c97b9c9692deae34a6cd09f52cfccbf94aba4bc69efb690eea35a?s=50&d=blank&r=g)
sarfaraz
[ August 11, 2014 at 9:30 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-237250)
It does not require any client side installation? How to configure client machine ?
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-237250)
  9. ![](https://secure.gravatar.com/avatar/bffc88b6705c97b9c9692deae34a6cd09f52cfccbf94aba4bc69efb690eea35a?s=50&d=blank&r=g)
sarfaraz
[ August 11, 2014 at 9:29 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-237249)
It does not require any client side installation
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-237249)
  10. ![](https://secure.gravatar.com/avatar/095d9978a2b2f42f3a8099fa3ad57ee47954e95f48a8fb2bc34e7af62d3ab0d1?s=50&d=blank&r=g)
Ariel
[ August 11, 2014 at 8:02 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-237200)
Please, please, please, don’t teach bad sysadmin examples ;-) SELinux is there for a reason, i’m tired of seeing people disabling it as soon as it interferes with their expectations. Please teach how to correctly configure it!
Also copying files to /etc, /usr and /var bypassing the package manager is a very bad habit. Please install those files in /usr/local or /opt instead!!
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-237200)
  11. ![](https://secure.gravatar.com/avatar/25c9ee90256bdb52ee32e3d4c4e0c8ff9cea79cdc5cada3a4d3c42cd04ea1b08?s=50&d=blank&r=g)
Numenori
[ August 11, 2014 at 10:16 am  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-236915)
Our Icinga for 3338 network hosts (right now, our network grow every day) works well enough on Debian server, but we modified it a little when compiled from sources. And don’t forget about something like NConf and SQL – it’s very useful.
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-236915)
  12. ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ August 7, 2014 at 7:41 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-234325)
For RHEL/CentOS 6 will work surely, just add repoforge repositories and you can install from binaries.
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-234325)
  13. ![](https://secure.gravatar.com/avatar/505b4926ba5b27c30223414715c688b0d7e522342e4f22466316b86a462702bf?s=50&d=blank&r=g)
Omipenguin
[ August 6, 2014 at 7:56 pm  ](https://www.tecmint.com/install-icinga-in-centos-7/#comment-233382)
Will it work for Redhat 5 and 6 ???
[Reply](https://www.tecmint.com/install-icinga-in-centos-7/#comment-233382)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-icinga-in-centos-7/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
## Upgrade Your Linux Learning with Pro.Tecmint
**If you find TecMint helpful** , consider supporting us by subscribing to [**Pro.Tecmint.com**](https://pro.tecmint.com) – our premium platform with exclusive guides, ad-free experience, early access to tutorials, and much more.

Your support helps us keep creating quality Linux content for everyone.
[ Get Lifetime Access ](https://pro.tecmint.com)
## Linux Commands and Tools
[20 Netstat Commands for Linux Network Management](https://www.tecmint.com/20-netstat-commands-for-linux-network-management/)
[Goto – Quickly Navigate to Aliased Directories with Auto-Completion Support](https://www.tecmint.com/goto-navigate-aliased-directories-with-auto-completion/)
[Ways to Use ‘find’ Command to Search Directories More Efficiently](https://www.tecmint.com/find-directory-in-linux/)
[How to Install and Use Chrony in Linux](https://www.tecmint.com/install-chrony-in-centos-ubuntu-linux/)
[Terminalizer – Record Your Linux Terminal and Generate Animated GIF](https://www.tecmint.com/terminalizer-record-your-linux-terminal-in-gif/)
[How to Free Up Space in Linux When Root (/) Partition Is Full](https://www.tecmint.com/fix-full-root-partition-linux/)
## Linux Server Monitoring Tools
[Arpwatch – Monitor Ethernet Activity {IP and Mac Address} in Linux](https://www.tecmint.com/monitor-ethernet-activity-in-linux/)
[linux-dash: Monitors “Linux Server Performance” Remotely Using Web Browser](https://www.tecmint.com/monitors-linux-server-performance-remotely-using-web-browser/)
[5 Modern VnStat PHP Replacements for Bandwidth Monitoring](https://www.tecmint.com/network-bandwidth-monitoring-tools/)
[Observium: A Complete Network Management and Monitoring System for RHEL/CentOS](https://www.tecmint.com/install-observium-in-centos/)
[A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%](https://www.tecmint.com/monitor-disk-usage-bash-script/)
[Configure Collectd as a Central Monitoring Server for Clients](https://www.tecmint.com/configure-collectd-as-central-monitoring-server-for-clients/)
## Learn Linux Tricks & Tips
[How to Find Difference Between Two Directories Using Diff and Meld Tools](https://www.tecmint.com/compare-find-difference-between-two-directories-in-linux/)
[How to Backup or Clone Linux Partitions Using ‘cat’ Command](https://www.tecmint.com/backup-or-clone-linux-partitions-using-cat-command/)
[How to Manage User Password Expiration and Aging in Linux](https://www.tecmint.com/manage-user-password-expiration-and-aging-in-linux/)
[How to Auto Execute Commands/Scripts During Reboot or Startup](https://www.tecmint.com/auto-execute-linux-scripts-during-reboot-or-startup/)
[8 Parted Commands to Manage Disk Partitions in Linux](https://www.tecmint.com/parted-command-create-linux-partitions/)
[How to Block or Disable Normal User Logins in Linux](https://www.tecmint.com/block-or-disable-normal-user-logins-in-linux/)
## Best Linux Tools
[12 Best Media Server Software for Linux in 2024](https://www.tecmint.com/best-media-server-software-for-linux/)
[How to Install Microsoft Teams, Slack, and Discord on Linux Desktop](https://www.tecmint.com/install-microsoft-teams-slack-discord-linux/)
[Top 3 Open Source Virtual Data Room (VDR) for Linux](https://www.tecmint.com/open-source-virtual-data-room-for-linux/)
[5 Best Command Line HTTP Clients for Linux](https://www.tecmint.com/command-line-http-clients-for-linux/)
[Top 6 Partition Managers (CLI + GUI) for Linux](https://www.tecmint.com/linux-partition-managers/)
[10 Top Open Source Artificial Intelligence Tools for Linux](https://www.tecmint.com/open-source-artificial-intelligence-tools-softwares-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-icinga-in-centos-7/ "Scroll back to top")
Search for:
