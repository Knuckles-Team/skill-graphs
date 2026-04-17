[Skip to content](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/)
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
  * [Pro Courses](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/)
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
  * [Pro Courses](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/)
# How to Setup Central Logging Server with Rsyslog in Linux
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: October 26, 2018 Read Time: 6 minsCategories [CentOS](https://www.tecmint.com/category/linux-distros/centos/), [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [Ubuntu](https://www.tecmint.com/category/linux-distros/ubuntu/) [18 Comments](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comments)
**Logs** are a critical component of any software or operating system. Logs usually record user’s actions, system events, network activity and so much more, depending on what they are intended for. One of the most widely used logging systems on Linux systems is **rsyslog**.
**Rsyslog** is a powerful, secure and high-performance log processing system which accepts data from different types of source (systems/applications) and outputs it into multiple formats.
It has evolved from a regular **syslog** daemon to a fully-featured, enterprise level logging system. It is designed in a client/server model, therefore it can be configured as a client and/or as a central logging server for other servers, network devices, and remote applications.
#### Testing Environment
For the purpose of this guide, we will use the following hosts:
  * **Server** : 192.168.241.140
  * **Client** : 172.31.21.58


### How to Install and Configure Rsyslog Server
Most Linux distributions come with the **rsyslog** package preinstalled. In case it’s not installed, you can install it using your Linux package manager tool as shown.
```
$ sudo yum update && yum install rsyslog 	#CentOS 7
$ sudo apt update && apt install rsyslog	#Ubuntu 16.04, 18.04

```

Once **rsyslog** installed, you need to start the service for now, enable it to auto-start at boot and check it’s status with the [systemctl command](https://www.tecmint.com/manage-services-using-systemd-and-systemctl-in-linux/).
```
$ sudo systemctl start rsyslog
$ sudo systemctl enable rsyslog
$ sudo systemctl status rsyslog

```

The main rsyslog configuration file is located at **/etc/rsyslog.conf** , which loads modules, defines the global directives, contains rules for processing log messages and it also includes all config files in **/etc/rsyslog.d/** for various applications/services.
```
$ sudo vim /etc/rsyslog.conf

```

By default, **rsyslog** uses the **imjournal** and **imusock** modules for importing structured log messages from **systemd journal** and for accepting syslog messages from applications running on the local system via Unix sockets, respectively.
![Rsyslog Modules for Logging](https://www.tecmint.com/wp-content/uploads/2018/10/rsyslog-modules-for-logging.png)Rsyslog Modules for Logging
To configure rsyslog as a network/central logging server, you need to set the protocol (either **UDP** or **TCP** or both) it will use for remote syslog reception as well as the port it listens on.
If you want to use a **UDP** connection, which is faster but unreliable, search and uncomment the lines below (replace **514** with the port you want it to listen on, this should match the port address that the clients send messages to, we will look at this more when configuring a rsyslog client).
```
$ModLoad imudp
$UDPServerRun 514

```

To use **TCP** connection (which is slower but more reliable), search and uncomment the lines below.
```
$ModLoad imtcp
$InputTCPServerRun 514

```

In this case, we want to use both UDP and TCP connections at the same time.
![Configure Rsyslog Logging Server](https://www.tecmint.com/wp-content/uploads/2018/10/Configure-Rsyslog-Logging-Server.png)Configure Rsyslog Logging Server
Next, you need to define the **ruleset** for processing remote logs in the following format.
```
facility.severity_level	destination (where to store log)

```

Where:
  * **facility** : is type of process/application generating message, they include auth, cron, daemon, kernel, local0..local7. Using `*` means all facilities.
  * **severity_level** : is type of log message: emerg-0, alert-1, crit-2, err-3, warn-4, notice-5, info-6, debug-7. Using `*` means all severity levels and none implies no severity level.
  * **destination** : is either local file or remote rsyslog server (defined in the form IP:port).


We will use the following **ruleset** for collecting logs from remote hosts, using the **RemoteLogs** template. Note that these rules must come before any rules for processing local messages, as shown in the screenshot.
```
$template RemoteLogs,"/var/log/%HOSTNAME%/%PROGRAMNAME%.log"
*.* ?RemoteLogs
& ~

```
![Define Ruleset for Rsyslog-Logging](https://www.tecmint.com/wp-content/uploads/2018/10/Define-Ruleset-for-Rsyslog-Logging.png)Define Ruleset for Rsyslog-Logging
Looking at the above **ruleset** , the first rule is **“$template RemoteLogs,”/var/log/%HOSTNAME%/%PROGRAMNAME%.log””**.
The directive **$template** tells rsyslog daemon to gather and write all of the received remote messages to distinct logs under **/var/log** , based on the **hostname** (client machine name) and remote client facility (program/application) that generated the messages as defined by the settings present in the template **RemoteLogs**.
The second line **“*.* ?RemoteLogs”** means record messages from all facilities at all severity levels using the **RemoteLogs** template configuration.
The final line **“ & ~”** instructs rsyslog to stop processing the messages once it is written to a file. If you don’t include **“ & ~”**, messages will instead be be written to the local files.
There are many other templates that you can use, for more information, see the rsyslog configuration man page (**man rsyslog.conf**) or refer to the
That’s it with configuring the rsyslog server. Save and close the configuration file. To apply the recent changes, restart rsyslog daemon with the following command.
```
$ sudo systemctl restart rsyslog

```

Now verify the rsyslog network sockets. Use the **ss command** (or [netstat](https://www.tecmint.com/20-netstat-commands-for-linux-network-management/) with the same flags) command and pipe the output to [grep to filter](https://www.tecmint.com/12-practical-examples-of-linux-grep-command/) out rsyslogd connections.
```
$ sudo ss -tulnp | grep "rsyslog"

```
![Check Rsyslog Network Status](https://www.tecmint.com/wp-content/uploads/2018/10/Check-rsyslog-Status.png)Check Rsyslog Network Status
Next, on **CentOS 7** , if you have **SELinux** enabled, run the following commands to allow rsyslog traffic based on the network socket type.
```
$ sudo semanage -a -t syslogd_port_t -p udp 514
$ sudo semanage -a -t syslogd_port_t -p tcp 514

```

If the system has firewall enabled, you need to open port **514** to allow both **UDP/TCP** connections to the rsyslog server, by running.
```
**------------- On CentOS -------------**
$ sudo firewall-cmd --permanent --add-port=514/udp
$ sudo firewall-cmd --permanent --add-port=514/tcp
$ sudo firewall-cmd --reload

**------------- On Ubuntu -------------**
$ sudo ufw allow 514/udp
$ sudo ufw allow 514/tcp
$ sudo ufw reload

```

### How to Configure Rsyslog Client to Send Logs to Rsyslog Server
Now on the client system, check if the rsyslog service is running or not with the following command.
```
$ sudo systemctl status rsyslog

```

If it’s not installed, install it and start the service as shown earlier on.
```
$ sudo yum update && yum install rsyslog 	#CentOS 7
$ sudo apt update && apt install rsyslog	#Ubuntu 16.04, 18.04
$ sudo systemctl start rsyslog
$ sudo systemctl enable rsyslog
$ sudo systemctl status rsyslog

```

Once the rsyslog service is up and running, open the main configuration file where you will perform changes to the default configuration.
```
$ sudo vim /etc/rsyslog.conf

```

To force the rsyslog daemon to act as a log client and forward all locally generated log messages to the remote rsyslog server, add this forwarding rule, at the end of the file as shown in the following screenshot.
```
*. *  @@192.168.100.10:514

```
![Configure Rsyslog Client](https://www.tecmint.com/wp-content/uploads/2018/10/Configure-Rsyslog-Client.png)Configure Rsyslog Client
The above rule will send messages from all facilities and at all severity levels. To send messages from a specific facility for example **auth** , use the following rule.
```
auth. *  @@192.168.100.10:514

```

Save the changes and close the configuration file. To apply the above settings, restart the rsyslog daemon.
```
$ sudo systemctl restart rsyslog

```

### How to Monitor Remote Logging on the Rsyslog Server
The final step is to verify if the rsyslog is actually receiving and logging messages from the client, under **/var/log** , in the form **hostname/programname.log**.
Run a [ls command](https://www.tecmint.com/tag/linux-ls-command/) to long listing of the parent logs directory and check if there is a directory called **ip-172.31.21.58** (or whatever your client machine’s hostname is).
```

$ ls -l /var/log/

```
![Check Rsyslog Client Logging](https://www.tecmint.com/wp-content/uploads/2018/10/Check-Rsyslog-Client-Logging.png)Check Rsyslog Client Logging
If the directory exists, check the log files inside it, by running.
```
$ sudo ls -l /var/log/ip-172-31-21-58/

```
![Check Rsyslog Client Logs](https://www.tecmint.com/wp-content/uploads/2018/10/Check-Rsyslog-Client-Logs.png)Check Rsyslog Client Logs
##### Summary
**Rsyslog** is a high-performance log processing system, designed in a client/server architecture. We hope you are able to install and configure **Rsyslog** as a central/network logging server and as a client as demonstrated in this guide.
You may also want to refer to relevant rsyslog manual pages for more help. Feel free to give us any feedback or ask questions.
Tags [Linux Log Management](https://www.tecmint.com/tag/linux-log-management/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[WonderShaper – A Tool to Limit Network Bandwidth in Linux](https://www.tecmint.com/wondershaper-limit-network-bandwidth-in-linux/)
Next article:
[10 tr Command Examples in Linux](https://www.tecmint.com/tr-command-examples-in-linux/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#respond)** or
## Related Posts
[![CentOS Stream for Development](https://www.tecmint.com/wp-content/uploads/2013/03/CentOS-Stream-for-Development.webp)](https://www.tecmint.com/centos-stream-for-developers/ "CentOS Stream: The Perfect Distribution for Development Projects")
[CentOS Stream: The Perfect Distribution for Development Projects](https://www.tecmint.com/centos-stream-for-developers/)
[![Manage Layered Local Storage with Stratis](https://www.tecmint.com/wp-content/uploads/2024/10/Manage-Layered-Local-Storage-with-Stratis.webp)](https://www.tecmint.com/install-stratis-to-manage-layered-local-storage-on-rhel/ "How to Install Stratis to Manage Layered Local Storage on RHEL 9/8")
[How to Install Stratis to Manage Layered Local Storage on RHEL 9/8](https://www.tecmint.com/install-stratis-to-manage-layered-local-storage-on-rhel/)
[![Linux Disable Unwanted Services](https://www.tecmint.com/wp-content/uploads/2014/09/Linux-Disable-Unwanted-Services.png)](https://www.tecmint.com/disable-unwanted-services-linux/ "How to Disable and Remove Unnecessary Services on Linux")
[How to Disable and Remove Unnecessary Services on Linux](https://www.tecmint.com/disable-unwanted-services-linux/)
[![Install Memcached on RHEL](https://www.tecmint.com/wp-content/uploads/2019/03/Install-Memcached-on-RHEL.png)](https://www.tecmint.com/install-memcached-linux/ "Improve Website Performance – Install Memcached on RHEL 9")
[Improve Website Performance – Install Memcached on RHEL 9](https://www.tecmint.com/install-memcached-linux/)
[![Migrate CentOS to Rocky Linux](https://www.tecmint.com/wp-content/uploads/2013/01/Migrate-CentOS-to-Rocky-Linux.png)](https://www.tecmint.com/migrate-centos-to-rocky-linux/ "How to Migrate CentOS 7 to Rocky Linux 9")
[How to Migrate CentOS 7 to Rocky Linux 9](https://www.tecmint.com/migrate-centos-to-rocky-linux/)
[![How to Reset Root Password](https://www.tecmint.com/wp-content/uploads/2012/11/Reset-Root-Password.jpg)](https://www.tecmint.com/reset-forgotten-root-password-in-rhel-centos-and-fedora/ "How to Reset Forgotten Root Password in RHEL Systems")
[How to Reset Forgotten Root Password in RHEL Systems](https://www.tecmint.com/reset-forgotten-root-password-in-rhel-centos-and-fedora/)
### 18 Comments
[Leave a Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/6ab4595359dd89de5124faad0ee7980227ef87d00662a5c26ce9873e8b357d25?s=50&d=blank&r=g)
Bhuvan
[ March 10, 2022 at 3:06 am  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1736194)
Did you get any solution for this situation? Am facing the same issue.
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1736194)
  2. ![](https://secure.gravatar.com/avatar/fa8546e78462046e0bb57900003899cc68c03d725fe883c7f6cfa4b625d90bcf?s=50&d=blank&r=g)
Antonio
[ July 4, 2021 at 1:37 pm  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1537012)
Hi Everyone,
I would like to share with the community about a critical instruction ‘**rsyslog** ‘ which is mandatory in order to make work exporting to **CentOS 7/RHEL 8** as a logs server with mariadb-mysql database.
Very useful in uses with “**Adiscon LogAnalyzer WebApp** “. You just need to add to the “**/etc/rsyslog.conf** ” file as follows gère :
```
$ModLoad ommysql
$ActionOmmysqlServerPort 1234
*.* :ommysql:database-server,database-name,database-userid,database-password

```

Hoping to help others…
Best regards,
Antonio
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1537012)
  3. ![](https://secure.gravatar.com/avatar/e1ba1a11281c705cccf2066765a3a1db93851bb6578dd499ce32274b6f743714?s=50&d=blank&r=g)
Dachshund Digital
[ May 17, 2021 at 11:52 pm  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1492195)
The ‘stop’ is still wrong, it generates configuration error unless the given stop is the LAST line in the rsyslog configuration chain. I as chain, because **/etc/rsyslog.d** context is injected before any defined rules in the actual **/etc/rsyslog.conf** file.
A typical **rsyslog.conf** local file will have additional local rules defined. What happens right now, with ‘& stop’ replacing ‘& ~’ as I said the configuration error reported. If the stop directive is removed, then you get some local files populated as expected, and others directed to a directory that holds local information.
This can and will be confusing to support personnel. You need to add a test of the hostname and if the hostname IS NOT the local system name then and only then the template (rule) is leveraged. Doing this should leave local file content alone as is often defined in the actual rsyslog.conf file.
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1492195)
  4. ![](https://secure.gravatar.com/avatar/2abcf08edf90fdb47d967e430d84ff4163132d76a859b792024da8f57cd1ce51?s=50&d=blank&r=g)
Steffen
[ June 12, 2020 at 12:02 am  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1337226)
This article is outdated and confusing. The `"~"` syntax is deprecated. The documentation says to replace it with “**stop** ” but then everything after “**stop** ” will be completely ignored.
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1337226)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ June 12, 2020 at 11:42 am  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1337266)
@Steffen
Thanks for the useful info, we will update the article soon.
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1337266)
       * ![](https://secure.gravatar.com/avatar/2abcf08edf90fdb47d967e430d84ff4163132d76a859b792024da8f57cd1ce51?s=50&d=blank&r=g)
Steffen
[ June 12, 2020 at 7:14 pm  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1337295)
What you need to do now is something like
```
if $fromhost-ip == '192.168.1.1' then {
  /var/log/router.log
 stop
}

```

which stops this very rule but not the rest of your config file.
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1337295)
         * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ June 16, 2020 at 10:22 am  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1337573)
@Steffen
Many thanks, ones again for sharing this. We are truly grateful.
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1337573)
         * ![](https://secure.gravatar.com/avatar/ef0c57c1f2adfc70d9f67db82826738416c866dc6f88d0b5d763b799d6921ed9?s=50&d=blank&r=g)
Edongkido
[ May 4, 2021 at 12:20 am  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1485298)
Thank you! this saves me a lot of time!
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1485298)
  5. ![](https://secure.gravatar.com/avatar/da054dac85891c5bb290d349eb3e162efa01cd38819450795350857fb913c074?s=50&d=blank&r=g)
Randeep Singh
[ September 6, 2019 at 8:54 pm  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1238391)
Does rsyslog configuration support failover? for example does it work on primary secondary model?
If yes how I can defined in .conf file.
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1238391)
  6. ![](https://secure.gravatar.com/avatar/817158e6d4c80cebcae7f92e101c351f700be6e9718c99f1eff0d174e684d8b7?s=50&d=blank&r=g)
DHARANI BABU
[ August 30, 2019 at 12:10 am  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1234083)
Hi Team,
I need to send non-standard logs to remote server via rsyslog. can you please share me steps ,
For Example, if i need to send a **/var/opt/httpd/httpd.logs** to my remote host via rsyslog . Please share me steps to my email ID ?
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1234083)
  7. ![](https://secure.gravatar.com/avatar/962190a99d5f342f792b3c4d0d358b2ac9f558f494cc7c34f38fabe04d6f3719?s=50&d=blank&r=g)
linuxman1
[ July 24, 2019 at 9:24 am  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1209920)
Thanks, worked on Centos 7 servers very well.
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1209920)
  8. ![](https://secure.gravatar.com/avatar/c4470f9b88a3d82cd049fc72cbbd0d3992a90a6b108eb854e376ba19c514eaf9?s=50&d=blank&r=g)
PC
[ July 16, 2019 at 8:11 pm  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1204943)
This works for remote logs coming in. However, this seems to prevent the local logs on the rsyslog server from being stored. How would you modify this so that the local logs for the rsyslog server itself are stored in the same directory structure as all the other logs from remote servers?
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1204943)
  9. ![](https://secure.gravatar.com/avatar/99eb6e54a238cb357f862ce167080b43f08f4f74a00c97eb35c0ea1cf651d0d7?s=50&d=blank&r=g)
Sitha
[ May 18, 2019 at 9:19 am  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1153841)
What are the different between rsyslog on Centos7 and Ubuntu? I really hard to identify it.
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1153841)
  10. ![](https://secure.gravatar.com/avatar/02878f682f2635ed3be17569eb90d8330db8c7212d11d10a904615985f9ab796?s=50&d=blank&r=g)
Sebastien
[ November 12, 2018 at 10:30 am  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1058223)
Hi,
Thank you for this article.
A little modification in lines of forward configurations, you have a space character between characters `.` and `*`:
```
*. *  @@192.168.100.10:514 => *.*  @@192.168.100.10:514

```
```
auth. *  @@192.168.100.10:514 => auth.*  @@192.168.100.10:514

```

Bye
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1058223)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ November 13, 2018 at 12:42 am  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1058492)
@Sebastien
Using ***** means all facilities, using **auth** means only send auth logs.
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1058492)
       * ![](https://secure.gravatar.com/avatar/02878f682f2635ed3be17569eb90d8330db8c7212d11d10a904615985f9ab796?s=50&d=blank&r=g)
Sebastien
[ May 20, 2019 at 1:47 pm  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1154834)
Hi,
I have just a little comment because in your article you write a space character `"*. *"`…
Regards
Sebastien
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1154834)
  11. ![](https://secure.gravatar.com/avatar/8be37805c0edfc20f57041d1be694934f1822f111c84a0b99e376dba72787a7a?s=50&d=blank&r=g)
Robert Meyer
[ October 30, 2018 at 1:22 am  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1053854)
Why did you choose to ignore the whole block of information above your single line forwarding rule? This client rule will hang if the syslog server isn’t answering.
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1053854)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ October 31, 2018 at 11:23 am  ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1054363)
@Robert
Okay, this is a great concern. We will update the article to include this point. Thanks for the feedback.
[Reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#comment-1054363)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/#respond)
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
[How to Kill a Process in Linux from Command Line](https://www.tecmint.com/how-to-kill-a-process-in-linux/)
[7 Best Tools to Compare Text Files in Linux](https://www.tecmint.com/compare-files-linux/)
[How to Block or Disable Normal User Logins in Linux](https://www.tecmint.com/block-or-disable-normal-user-logins-in-linux/)
[whowatch – Monitor Linux Users and Processes in Real Time](https://www.tecmint.com/whowatch-monitor-linux-users-and-processes-in-real-time/)
[How to Control Systemd Services on Remote Linux Server](https://www.tecmint.com/control-systemd-services-on-remote-linux-server/)
[How to Append Text to End of File in Linux](https://www.tecmint.com/append-text-to-end-of-file-in-linux/)
## Linux Server Monitoring Tools
[Sysmon – A Graphical System Activity Monitor for Linux](https://www.tecmint.com/sysmon-linux-activity-monitor/)
[Smem – Reports Memory Consumption Per-Process and Per-User in Linux](https://www.tecmint.com/smem-linux-memory-usage-per-process-per-user/)
[btop: A Modern and Resourceful System Monitor](https://www.tecmint.com/btop-system-monitoring-tool-for-linux/)
[Understand Linux Load Averages and Monitor Performance of Linux](https://www.tecmint.com/understand-linux-load-averages-and-monitor-performance/)
[7 Best Tools to Monitor and Debug Disk I/O Performance in Linux](https://www.tecmint.com/monitor-linux-disk-io-performance/)
[Monit – A Open Source Tool for Managing and Monitoring Linux System](https://www.tecmint.com/monit-linux-services-monitoring/)
## Learn Linux Tricks & Tips
[Learn Difference Between “su” and “su -” Commands in Linux](https://www.tecmint.com/difference-between-su-and-su-commands-in-linux/)
[2 Ways to Create an ISO from a Bootable USB in Linux](https://www.tecmint.com/create-an-iso-from-a-bootable-usb-in-linux/)
[How to Create a Virtual HardDisk Volume Using a File in Linux](https://www.tecmint.com/create-virtual-harddisk-volume-in-linux/)
[How to Check Timezone in Linux](https://www.tecmint.com/check-linux-timezone/)
[How to Enable, Disable and Install Yum Plug-ins](https://www.tecmint.com/enable-disable-and-install-yum-plug-ins/)
[How to Clear BASH Command Line History in Linux](https://www.tecmint.com/clear-command-line-history-in-linux/)
## Best Linux Tools
[13 Most Used Microsoft Office Alternatives for Linux](https://www.tecmint.com/microsoft-office-alternatives-for-linux/)
[4 Best Tools for Creating Fillable PDF Forms on Linux](https://www.tecmint.com/create-pdf-forms-linux/)
[5 Best Command Line HTTP Clients for Linux](https://www.tecmint.com/command-line-http-clients-for-linux/)
[10 Most Popular Download Managers for Linux in 2023](https://www.tecmint.com/download-managers-for-linux/)
[8 Best Mail Transfer Agents (MTA’s) for Linux](https://www.tecmint.com/best-mail-transfer-agents-mta-for-linux/)
[How to Open and Edit Apple iWork Files on Linux](https://www.tecmint.com/open-and-edit-apple-iwork-files-on-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/ "Scroll back to top")
Search for:
