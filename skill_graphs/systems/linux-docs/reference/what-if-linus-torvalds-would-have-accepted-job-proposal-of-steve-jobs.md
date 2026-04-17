[Skip to content](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/)
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
  * [Pro Courses](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/ "Linux Online Courses")
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


[](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/)
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
  * [Pro Courses](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/ "Linux Online Courses")
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


[](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/)
# How to Create a Centralized Log Server with Rsyslog in CentOS/RHEL 7
[Matei Cezar](https://www.tecmint.com/author/cezarmatei/ "View all posts by Matei Cezar")Last Updated: November 7, 2018 Read Time: 7 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [25 Comments](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comments)
In order for system administrator to identify or troubleshoot a problem on a **CentOS 7** or **RHEL 7** server system, it must know and view the events that happened on the system in a specific period of time from log files stored in the system in the **/var/log** directory.
The syslog server on a Linux machine can act a central monitoring point over a network where all servers, network devices, routers, switches and most of their internal services that generate logs, whether related to specific internal issue or just informative messages can send their logs.
On a **CentOS/RHEL 7** system, **Rsyslog** daemon is the main log server preinstalled, followed by **Systemd Journal Daemon** (**journald**).
**Rsyslog** server in build as a client/server architecture service and can achieve both roles simultaneous. It can run as a server and collect all logs transmitted by other devices in the network or it can run as a client by sending all internal system events logged to a remote endpoint syslog server.
When rsyslog is configured as a client, the logs can be stored locally in files on the local filesystem or can be send remotely rather than write them in files stored on the machine or write events log files locally and send them to a remote syslog server at the same time.
Syslog server operates any log message using the following scheme:
```
type (facility).priority (severity)  destination(where to send the log)

```

**A.** The **facility** or type data is represented by the internal system processes that generates the messages. In Linux internal processes (facilities) that generate logs are standardized as follows:
  * **auth** = messages generated by authentication processes (login).
  * **cron** = messages generated by scheduled processes (crontab).
  * **daemon** = messages generated by daemons (internal services).
  * **kernel** = messages generated by the Linux Kernel itself.
  * **mail** = messages generated by a mail server.
  * **syslog** = messages generated by the rsyslog daemon itself.
  * **lpr** = messages generated by local printers or a print server.
  * **local0 – local7** = custom messages defined by an administrator (local7 is usually assigned for Cisco or Windows).


**B.** The **priority (severity)** levels are standardized also. Each priority is assigned with a standard abbreviation and a number as described below. The 7th priority is the higher level of all.
  * **emerg** = Emergency – 0
  * **alert** = Alerts – 1
  * **err** = Errors – 3
  * **warn** = Warnings – 4
  * **notice** = Notification – 5
  * **info** = Information – 6
  * **debug** = Debugging – 7


Special Rsyslog keywords:
  * ***** = all facilities or priorities
  * **none** = the facilities have no given priorities Eg: **mail.none**


**C.** The third part for the syslog schema is represented by the **destination** directive. Rsyslog daemon can send log messages to be written in a file on the local filesystem (mostly in a file in **/var/log/** directory) or to be piped to another local process or to be send to a local user console (to stdout), or send the message to a remote syslog server via TCP/UDP protocol, or even discard the message to **/dev/null**.
In order to Configure **CentOS/RHEL 7** as a central Log Server, first we need to check and ensure that the **/var** partition where all log file are recorded is large enough (a few GB minimum) in order to be able to store all the log files that will be sent by other devices. It’s a good decision to use a separate drive (LVM, RAID) to mount the **/var/log/** directory.
#### Requirements
  1. [CentOS 7.3 Installation Procedure](https://www.tecmint.com/centos-7-3-installation-guide/)
  2. [RHEL 7.3 Installation Procedure](https://www.tecmint.com/red-hat-enterprise-linux-7-3-installation-guide/)


### How to Configure Rsyslog in CentOS/RHEL 7 Server
**1.** By default, **Rsyslog** service is automatically installed and should be running in **CentOS/RHEL 7**. In order to check if the daemon is started in the system, issue the following command with root privileges.
```
# systemctl status rsyslog.service

```
![Check Rsyslog Service](https://www.tecmint.com/wp-content/uploads/2017/09/Check-Rsyslog-Service.png)Check Rsyslog Service
If the service is not running by default, execute the below command in order to start rsyslog daemon.
```
# systemctl start rsyslog.service

```

**2.** If the rsyslog package is not installed on the system that you intend to use as a centralized logging server, issue the following command to install the rsyslog package.
```
# yum install rsyslog

```

**3.** The first step that we need to do on the system in order to configure rsyslog daemon as a centralized log server, so it can receive log messages for external clients, is to open and edit, using your favorite text editor, the main configuration file from **/etc/rsyslog.conf** , as presented in the below excerpt.
```
# vi /etc/rsyslog.conf

```

In the rsyslog main configuration file, search and uncomment the following lines (remove the hashtag `#` sign at the line beginning) in order to provide UDP transport reception to Rsyslog server via **514** port. UDP is the standard protocol used for log transmission by Rsyslog.
```
$ModLoad imudp
$UDPServerRun 514

```
![Configure Rsyslog Server](https://www.tecmint.com/wp-content/uploads/2017/09/Configure-Rsyslog-Server.png)Configure Rsyslog Server
**4.** UDP protocol does not have the TCP overhead, which make it faster for transmitting data than TCP protocol. On the other hand, UDP protocol does not assure reliability of transmitted data.
However, if you need to use TCP protocol for log reception you must search and uncomment the following lines from **/etc/rsyslog.conf** file in order to configure Rsyslog daemon to bind and listen a TCP socket on 514 port. TCP and UDP listening sockets for reception can be configured on a Rsyslog server simultaneously.
```
$ModLoad imtcp
$InputTCPServerRun 514

```

**5.** On the next step, don’t close the file yet, create a new template that will be used for receiving remote messages. This template will instruct the local Rsyslog server where to save the received messages send by syslog network clients. The template must be added before the beginning of the **GLOBAL DIRECTIVES** block as illustrated in the below excerpt.
```
$template RemoteLogs,"/var/log/%HOSTNAME%/%PROGRAMNAME%.log" 
. ?RemoteLogs & ~

```
![Create Rsyslog Template](https://www.tecmint.com/wp-content/uploads/2017/09/Create-Rsyslog-Template.jpg)Create Rsyslog Template
The above **$template RemoteLogs** directive instructs Rsyslog daemon to collect and write all of the received log messages to distinct files, based on the client machine name and remote client facility (application) that generated the messages based on the defined properties presents in the template configuration: **%HOSTNAME%** and **%PROGRAMNAME%**.
All these log files will be written to local filesystem to a dedicated file named after client machine’s hostname and stored in /var/log/ directory.
The **& ~** redirect rule instructs the local Rsyslog server to stop processing the received log message further and discard the messages (not write them to internal log files).
The **RemoteLogs** name is an arbitrary name given to this template directive. You can use whatever name you can find best suited for your template.
In order to write all received messages from clients in a single log file named after the IP Address of the remote client, without filtering the facility that generated the message, use the below excerpt.
```
$template FromIp,"/var/log/%FROMHOST-IP%.log" 
. ?FromIp & ~

```

Another example of a template where all messages with auth facility flag will be logged to a template named “**TmplAuth** “.
```
$template TmplAuth, "/var/log/%HOSTNAME%/%PROGRAMNAME%.log"
authpriv.*   ?TmplAuth

```

Below is an excerpt form a template definition from Rsyslog 7 server:
```
template(name="TmplMsg" type="string"
         string="/var/log/remote/msg/%HOSTNAME%/%PROGRAMNAME:::secpath-replace%.log"
        )

```

The above template excerpt can also be written as:
```
template(name="TmplMsg" type="list") {
    constant(value="/var/log/remote/msg/")
    property(name="hostname")
    constant(value="/")
    property(name="programname" SecurePath="replace")
    constant(value=".log")
    }

```

To write complex Rsyslog templates, read the Rsyslog configuration file manual by issuing **man rsyslog.conf** command or consult
**6.** After you’ve edited the Rsyslog configuration file with your own settings as explained above, restart the Rsyslog daemon in order to apply changes by issuing the following command:
```
# service rsyslog restart

```

**7.** By now, Rsyslog server should be configured to act a centralized log server and record messages from syslog clients. To verify Rsyslog network sockets, run [netstat command](https://www.tecmint.com/20-netstat-commands-for-linux-network-management/) with root privileges and use grep to filter rsyslog string.
```
# netstat -tulpn | grep rsyslog

```
![Verify Rsyslog Network Socket](https://www.tecmint.com/wp-content/uploads/2017/09/Verify-Rsyslog-Network-Socket.png)Verify Rsyslog Network Socket
**8.** If you have SELinux enabled in **CentOS/RHEL 7** , issue the following command to configure SELinux to allow rsyslog traffic depending on network socket type.
```
# semanage -a -t syslogd_port_t -p udp 514
# semanage -a -t syslogd_port_t -p tcp 514

```

**9.** If the firewall is enabled and active, run the below command in order to add the necessary rules for opening rsyslog ports in Firewalld.
```
# firewall-cmd --permanent --add-port=514/tcp
# firewall-cmd --permanent --add-port=514/udp
# firewall-cmd –reload

```

That’s all! Rsyslog is now configured in server mode and can centralize logs from remote clients. In next article, we will see how to [configure Rsyslog client on CentOS/RHEL 7 server](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/).
Using Rsyslog server as a central monitoring point for remote log messages you can inspect log files and observe the clients health status or debug client’s issues more easily when systems crash or are under some kind of attack.
Tags [Linux Log Management](https://www.tecmint.com/tag/linux-log-management/), [rsyslog](https://www.tecmint.com/tag/rsyslog/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[eBook – Install WordPress with Apache + Let’s Encrypt + W3 Total Cache + CloudFlare + Postfix on CentOS 7](https://www.tecmint.com/setup-wordpress-apache-letsencrypt-w3cache-cloudflare-book/)
Next article:
[Sysdig – A Powerful System Monitoring and Troubleshooting Tool for Linux](https://www.tecmint.com/sysdig-system-monitoring-and-troubleshooting-tool-for-linux/)
![Photo of author](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=100&d=blank&r=g)
Matei Cezar
I'am a computer addicted guy, a fan of open source and linux based system software, have about 4 years experience with Linux distributions desktop, servers and bash scripting.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#respond)** or
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
### 25 Comments
[Leave a Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/ab9dd3d0f0c581220fab2f37242cc48db2b36e3f4a3591b7f332e2653ad2f5d9?s=50&d=blank&r=g)
Reader
[ July 9, 2022 at 11:35 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1842438)
This article falls flat because it lacks any test procedure. How can the administrator run some command-line program to generate a Syslog message and show that it was received by rsyslogd? What can go wrong, and how does one diagnose the problem?
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1842438)
     * ![](https://secure.gravatar.com/avatar/973adfd0162a35740d7e68156390a9c94c70b93014a524a57a3ab8f75c868dbb?s=50&d=blank&r=g)
Rob
[ July 11, 2022 at 12:36 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1843559)
You could test that it works by configuring a device on your network to send its logs to the newly configured Syslog server. Lots of things can go wrong, misconfiguration, firewall, a bug in the software, bad routing between the sending and receiving devices, corrupted packet, etc. and any trouble-shooting would be based on the problem being presented. I think that much information would be best suited for a separate article.
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1843559)
  2. ![](https://secure.gravatar.com/avatar/56d02cecf9040d66b3baa902f44ca640c5463768f17797ca2bf96bc5325d8896?s=50&d=blank&r=g)
robert a
[ June 23, 2021 at 3:19 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1526889)
Is there a difference in the configuration file between ipv6 and ipv4?
It only works for me in Ipv4.
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1526889)
  3. ![](https://secure.gravatar.com/avatar/f708fae6b03fdbd209884c070a67a58c21846456603e9d18143f20c446550069?s=50&d=blank&r=g)
Asim Khan
[ January 16, 2020 at 10:02 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1312186)
Very useful article, short and simple to understand.
thanks!!
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1312186)
  4. ![](https://secure.gravatar.com/avatar/c4a2aa35f1cf53863c8c107b3eab3531973d5e668fd57c240a33125f6530f2b6?s=50&d=blank&r=g)
Gator Nation
[ October 3, 2019 at 12:20 am  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1259999)
Has anyone created a logging server on CentOS 8 yet? The rsyslog.conf file is very different. Thanks
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1259999)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 3, 2019 at 11:26 am  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1260348)
@Gator,
The same instructions provided here for CentOS 7, works with CentOS 8 as well. Give a try and see, if you face any issues do ask your query here.
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1260348)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 3, 2019 at 2:09 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1260404)
@Gator,
As per your request, I have created an article on setting up Centralized Log Server with Rsyslog in CentOS/RHEL 8 – <https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-8/>
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1260404)
  5. ![](https://secure.gravatar.com/avatar/b6cd26bd5e1cf219bf0204fbfcaee55f12cfb2b81cd3b30566a527084014dd3c?s=50&d=blank&r=g)
faran mustafa
[ February 8, 2019 at 12:42 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1099873)
how to creat a folder in syslog where all log are come
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1099873)
  6. ![](https://secure.gravatar.com/avatar/f4dee70bcc582aee3cbe8a5ceb4ef581b1ed0eafa231380c67886f2d436989c0?s=50&d=blank&r=g)
Brian Weslowski
[ December 20, 2018 at 7:21 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1084586)
In step 8, your **semanage** command is incorrect as of RHEL/CentOS 7.4. The correct command is: **semanage port -a -t syslog_port_t -p udp 514**. You are missing the first “port” option.
Also, if you are using a basic install of RHEL/CentOS, you need to install **semanage** with: **yum install policycoreutils-python**.
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1084586)
  7. ![](https://secure.gravatar.com/avatar/7db484efa720bc697ee0a3edbd702aa44ef1177c0e75c647001266ac2aa44835?s=50&d=blank&r=g)
Red Cricket
[ December 13, 2018 at 12:41 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1082856)
If I set up rsyslog server how can I set it up so that only certain clients can send log messages to it?
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1082856)
     * ![](https://secure.gravatar.com/avatar/7b133da096f6c757e395bafc01fcfb1b894b363b2d345b5ac8857a3b971ef0eb?s=50&d=blank&r=g)
c
[ December 1, 2020 at 3:28 am  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1396768)
Setup a firewall to allow only the addresses or address range to send logging messages on that port.
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1396768)
  8. ![](https://secure.gravatar.com/avatar/954aa928fae4fddb0260801099215baf34a1c28b124b9c1f36fb483b458354f3?s=50&d=blank&r=g)
SDB
[ December 7, 2018 at 11:32 am  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1081259)
I have added below in my **/etc/rsyslog.conf** :
```
$template RemoteLogs,"/var/log/rsyslog/%HOSTNAME%/%PROGRAMNAME%.log"
*.* ?RemoteLogs &

```

But after restarting rsyslog service status is showing below error :
invalid character in selector line – ‘;template’ expected [v8.24.0-34.el7]
error during parsing file **/etc/rsyslog.conf** , on or before line 23: errors occu…2207 ]
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1081259)
  9. ![](https://secure.gravatar.com/avatar/954aa928fae4fddb0260801099215baf34a1c28b124b9c1f36fb483b458354f3?s=50&d=blank&r=g)
SDB
[ December 5, 2018 at 6:04 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1079676)
Great tutorial thanks.
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1079676)
  10. ![](https://secure.gravatar.com/avatar/7bcb145c75d31b26efcf0115b433fb38ac79084b41ac5b2f28e086c9b04ed51c?s=50&d=blank&r=g)
Gilroy
[ November 21, 2018 at 12:15 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1062867)
awesome blog
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1062867)
  11. ![](https://secure.gravatar.com/avatar/ddf69a0cfcd56bd3c950feffb9ed3425f515650eaa93d555363d644f28eecea7?s=50&d=blank&r=g)
Rob Ramsey
[ November 1, 2018 at 7:04 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1054832)
You referenced TCP twice in your firewall statement. One of those should be UDP.
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1054832)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 7, 2018 at 10:30 am  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1056607)
@Rob,
Thanks for pointing out that error, corrected in the writeup..
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1056607)
  12. ![](https://secure.gravatar.com/avatar/8ba45bf6eb09c17df37dd321d5dce66eb332bd4813e2488cf342fd1dc1c3786c?s=50&d=blank&r=g)
david
[ July 28, 2018 at 12:47 am  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1018968)
rsyslog syntax has changed somewhat since this article was written. The `"~"` character has been deprecated in favor of STOP.
The rsyslog developers also recommend a statement like the one below on the client to forward records.
```
*.* action (type="omfwd" target="192.0.2.2" port="514" protocol="tcp"
                   action.resumeRetryCount="100"
                   queue.type="linedList" queue.size="10000)

```

The problem is inertial, and many of the deprecated methods are listed on websites. There doesn’t appear to be a single good website with the new methods listed.
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-1018968)
  13. ![](https://secure.gravatar.com/avatar/8c0a30398a426376f41f212460d08a088029d182273fb3dd3b7afd1c5d63d648?s=50&d=blank&r=g)
Huan
[ March 13, 2018 at 10:02 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-975813)
It seems in **v8.33.1** there are some changes:
```
$template RemoteLogs,"/logs/%HOSTNAME%/%PROGRAMNAME%.log"
*.* ?RemoteLogs
&stop

```

When I restart Syslog server I got:
Shutting down system logger: [ OK ]
Starting system logger: rsyslogd: error during config processing: STOP is followed by unreachable statements! [v8.33.1 try
[ OK ]
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-975813)
  14. ![](https://secure.gravatar.com/avatar/d4c19054e328ee2e06a4699fc76d153bd4ce8a6e1739cb8a3afd5224512b0201?s=50&d=blank&r=g)
soph
[ February 12, 2018 at 5:42 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-968557)
Hi, I tried your directives but they just caused an error. Any ideas?
```
# /usr/lib/rsyslog/rsyslogd -N 1

```

rsyslogd: version 8.4.2, config validation run (level 1), master config /etc/rsyslog.conf
rsyslogd: invalid character in selector line – ‘;template’ expected
rsyslogd: error during parsing file /etc/rsyslog.conf, on or before line 13: errors occurred in file ‘/etc/rsyslog.conf’ around line 13 [try
/etc/rsyslod.conf
$ModLoad imsolaris # for Solaris kernel logging
$ModLoad imtcp
$InputTCPServerRun 514
$ModLoad imudp.so # provides UDP syslog reception
$UDPServerRun 514 # start a UDP syslog server at standard port 514
$UDPServerAddress * # listen to all IP addresses
$template RemoteLogs,”/var/log/%HOSTNAME%/%PROGRAMNAME%.log”
. ?RemoteLogs & ~
$WorkDirectory /var/spool/rsyslog # where to place spool files
$template FromIp,”/var/log/%FROMHOST-IP%.log”
. ?FromIp & ~
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-968557)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ February 16, 2018 at 1:55 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-970375)
The last two lines of rsyslog should be as shown in the below excerpt:
```
$template RemoteLogs,”/var/log/%HOSTNAME%/%PROGRAMNAME%.log”
*.* ?RemoteLogs
&~

```
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-970375)
       * ![](https://secure.gravatar.com/avatar/d4c19054e328ee2e06a4699fc76d153bd4ce8a6e1739cb8a3afd5224512b0201?s=50&d=blank&r=g)
soph
[ February 16, 2018 at 2:49 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-970392)
Thanks for reply..
Changed to read:
&stop
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-970392)
  15. ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ September 14, 2017 at 1:27 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-913297)
The point 5 code lines should should have the following content:
**
$template RemoteLogs,”/var/log/%HOSTNAME%/%PROGRAMNAME%.log”
*.* ?RemoteLogs
&~
**
and the next template:
$template FromIp,”/var/log/%FROMHOST-IP%.log”
*.* ?FromIp
&~
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-913297)
  16. ![](https://secure.gravatar.com/avatar/51205fdfb7777a8d177eeea7d8b28d267df99f4d275ba06fb04f2d87a2d2f681?s=50&d=blank&r=g)
IWO
[ September 5, 2017 at 1:54 am  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-910909)
Hello Matei:
```
# mkdir /var/log/rsyslog
# cp -p /etc/rsyslog.conf	/etc/rsyslog.conf.original
# vi /etc/rsyslog.conf

```
```
$template RemoteLogs,"/var/log/rsyslog/%HOSTNAME%/%PROGRAMNAME%.log"
. ?RemoteLogs & ~

```

netstat’s deprecation <– in Centos 7 from minimal Install
Apparently in CentOS 7 netstat, which is part of the package net-tools has been officially deprecated, so you should be using ss (part of the package iproute2), going forward.
```
# yum provides /usr/sbin/ss		OR		# yum whatprovides /usr/sbin/ss
Complementos cargados:fastestmirror
Loading mirror speeds from cached hostfile
iproute-3.10.0-74.el7.x86_64 : Advanced IP routing and network device configuration tools
Repositorio        : @base
Resultado obtenido desde:
Nombre del archivo    : /usr/sbin/ss

```
```
# ss -tulpn | grep rsyslog
udp    UNCONN     0      0   *:514     *:*    users:(("rsyslogd",pid=10339,fd=3))
udp    UNCONN     0      0   :::514    :::*   users:(("rsyslogd",pid=10339,fd=4))
tcp    LISTEN     0      25  *:514    *:*    users:(("rsyslogd",pid=10339,fd=5))
tcp    LISTEN     0      25  :::514    :::*   users:(("rsyslogd",pid=10339,fd=6))

```
```
# getenforce
Enforcing

# semanage -a -t syslogd_port_t -p udp 514	   <-- ERROR
# semanage port -a -t syslogd_port_t -p udp 514	   <-- Sintaxis OK
bash: semanage: no se encontró la orden		   <-- in Centos 7

```
```
# yum -y install policycoreutils-python
# yum whatprovides /usr/sbin/semanage
Complementos cargados:fastestmirror
Loading mirror speeds from cached hostfile
policycoreutils-python-2.5-11.el7_3.x86_64 : SELinux policy core
python utilities
Repositorio        : @updates
Resultado obtenido desde:
Nombre del archivo    : /usr/sbin/semanage

```
```
# semanage port	-a -t syslogd_port_t -p udp 514
ValueError: El puerto udp/514 ya está definido		<-- Is it OK?

# semanage port -a -t syslogd_port_t -p tcp 514
ValueError: El puerto tcp/514 ya está definido		<-- Is it OK?

# semanage port -l| grep syslog			<-- Is it OK?
syslog_tls_port_t              tcp      6514
syslog_tls_port_t              udp      6514
syslogd_port_t                 tcp      601
syslogd_port_t                 udp      514, 601

# firewall-cmd --get-default-zone
public						<-- Is it OK?
# firewall-cmd --permanent --add-port=514/tcp
# firewall-cmd --permanent --add-port=514/udp
# firewall-cmd --reload

# firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: ens33
  sources:
  services: dhcpv6-client ssh
  ports: 514/tcp 514/udp	<-- Is it OK?
  protocols:
  masquerade: no
  forward-ports:
  sourceports:
  icmp-blocks:
  rich rules:

```

Bye
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-910909)
  17. ![](https://secure.gravatar.com/avatar/f3cafb2e335278fd9ca9155ed471a19d348f01b8d3987b1262f9a3f60344ea35?s=50&d=blank&r=g)
Mauro Formigoni Junior
[ September 4, 2017 at 6:49 pm  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-910786)
There is a little typo on Step 1, probably resulted of copy-paste.
The command to start rsyslog is # systemctl START rsyslog.service instead of STATUS.
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-910786)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ September 5, 2017 at 11:20 am  ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-911101)
@Mauro,
Thanks for pointing out that typo, yes it should be START, corrected in the article..:)
[Reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#comment-911101)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/#respond)
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
[How to Identify Your Linux System: Desktop or Laptop](https://www.tecmint.com/identify-linux-system-desktop-or-laptop/)
[fdupes – A Command Line Tool to Find and Delete Duplicate Files in Linux](https://www.tecmint.com/fdupes-find-and-delete-duplicate-files-in-linux/)
[How to Create a Password Protected ZIP File in Linux](https://www.tecmint.com/create-password-protected-zip-file-in-linux/)
[How to Convert From RPM to DEB and DEB to RPM Package Using Alien](https://www.tecmint.com/convert-from-rpm-to-deb-and-deb-to-rpm-package-using-alien/)
[6 Useful Tools to Troubleshoot DNS Name Resolution Problems](https://www.tecmint.com/troubleshoot-dns-in-linux/)
[How to Use diff3 Command for File Merging in Linux](https://www.tecmint.com/diff3-command-in-linux/)
## Linux Server Monitoring Tools
[How to Monitor Linux Server and Process Metrics from Browser](https://www.tecmint.com/monitor-linux-server-in-realtime/)
[How to Configure Zabbix to Send Email Alerts to Gmail Account – Part 2](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/)
[Cpustat – Monitors CPU Utilization by Running Processes in Linux](https://www.tecmint.com/cpustat-monitors-cpu-utilization-by-processes-in-linux/)
[Arpwatch – Monitor Ethernet Activity {IP and Mac Address} in Linux](https://www.tecmint.com/monitor-ethernet-activity-in-linux/)
[How to Install Nagios 4 in Ubuntu and Debian](https://www.tecmint.com/install-nagios-core-in-ubuntu-and-debian/)
[10 Strace Commands for Troubleshooting and Debugging Linux Processes](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/)
## Learn Linux Tricks & Tips
[Learn Difference Between “su” and “su -” Commands in Linux](https://www.tecmint.com/difference-between-su-and-su-commands-in-linux/)
[Ways to Use ‘find’ Command to Search Directories More Efficiently](https://www.tecmint.com/find-directory-in-linux/)
[How to Add a New Disk to an Existing Linux Server](https://www.tecmint.com/add-new-disk-to-an-existing-linux/)
[How to Repair and Defragment Linux System Partitions and Directories](https://www.tecmint.com/defragment-linux-system-partitions-and-directories/)
[How to Set or Change System Hostname in Linux](https://www.tecmint.com/set-hostname-permanently-in-linux/)
[How to Customize Bash Colors and Content in Linux Terminal Prompt](https://www.tecmint.com/customize-bash-colors-terminal-prompt-linux/)
## Best Linux Tools
[11 Best GUI Tools for Linux System Administrators in 2024](https://www.tecmint.com/gui-tools-for-linux-system-administrators/)
[7 Best Tools to Monitor and Debug Disk I/O Performance in Linux](https://www.tecmint.com/monitor-linux-disk-io-performance/)
[4 Best QR Code Generator Tools for Linux](https://www.tecmint.com/qr-code-generator-for-linux/)
[10 Tools to Monitor Linux Disk Partitions and Usage in Linux](https://www.tecmint.com/linux-tools-to-monitor-disk-partition-usage/)
[6 Best Whiteboard Applications for Your Linux Systems](https://www.tecmint.com/linux-whiteboard-applications/)
[20 Useful Security Features and Tools for Linux Admins](https://www.tecmint.com/security-features-tools-linux-admins/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/ "Scroll back to top")
Search for:
