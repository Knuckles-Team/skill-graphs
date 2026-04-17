[Skip to content](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/)
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
  * [Pro Courses](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/ "Linux Online Courses")
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


[](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/)
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
  * [Pro Courses](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/ "Linux Online Courses")
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


[](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/)
# How to Setup Rsyslog Client to Send Logs to Rsyslog Server in CentOS 7
[Matei Cezar](https://www.tecmint.com/author/cezarmatei/ "View all posts by Matei Cezar")Last Updated: September 12, 2017 Read Time: 5 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [10 Comments](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comments)
[Log management](https://www.tecmint.com/best-linux-log-monitoring-and-management-tools/) is one of the most critical component in a network infrastructure. Logs messages are constantly generated by numerous system software, such as utilities, applications, daemons, services related to network, kernel, physical devices and so on.
Log files proves to be useful in case of [troubleshooting Linux system issues](https://www.tecmint.com/audit-network-performance-security-and-troubleshooting-in-linux/), monitor the system and review a system security strength and problems.
**Rsyslog** is an Open Source logging program, which is the most popular logging mechanism in a huge number of Linux distributions. It’s also the default logging service in **CentOS 7** or **RHEL 7**.
**Rsyslog** daemon in CentOS can be configured to run as a server in order collect log messages from multiple network devices. These devices act as clients and are configured to transmit their logs to a rsyslog server.
However, the **Rsyslog** service can be also configured and started in client mode. This setup instructs the rsyslog daemon to forward log messages to a remote Rsyslog server using the TCP or UDP transport protocols. Rsyslog service can also be configured to run as a client and as a server in the same time.
In this tutorial we’ll describe how to setup a **CentOS/RHEL 7** Rsyslog daemon to send log messages to a remote Rsyslog server. This setup ensures that your machine disk space can be preserved for storing other data.
The place where almost all log files are written by default in **CentOS** is the `/var` system path. It’s also advisable to always create a separate partition for `/var` directory, which can be dynamically grown, in order to not exhaust the `/(root)` partition.
An **Rsyslog** client always sends the log messages in plain text, if not specified otherwise. You should not setup an Rsyslog client to transmit log messages over Internet or networks that are not under your complete control.
#### Requirements
  1. [CentOS 7.3 Installation Procedure](https://www.tecmint.com/centos-7-3-installation-guide/)
  2. [RHEL 7.3 Installation Procedure](https://www.tecmint.com/red-hat-enterprise-linux-7-3-installation-guide/)
  3. [Configure a Rsyslog Server in CentOS/RHEL 7](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/)


### Step 1: Verify Rsyslog Installation
**1.** By default, the Rsyslog daemon is already installed and running in a CentOS 7 system. In order to verify if rsyslog service is present in the system, issue the following commands.
```
# rpm -q | grep rsyslog
# rsyslogd -v

```
![Check Rsyslog Installation](https://www.tecmint.com/wp-content/uploads/2017/09/Check-Rsyslog-Installation.png)Check Rsyslog Installation
**2.** If the Rsyslog package is not installed in CentOS, execute the below command to install the service.
```
# yum install rsyslog

```

### Step 2: Configure Rsyslog Service as Client
**3.** In order to enforce the Rsyslog daemon installed on a **CentOS 7** system to act as a log client and route all of locally generated log messages to a remote Rsyslog server, modify the rsyslog configuration file as follows:
First open the main configuration file for editing.
```
# vi /etc/rsyslog.conf

```

Then, append the below line at the end of the file as illustrated in the below excerpt.
```
*. *  @192.168.10.254:514

```

On the above line makes sure you replace the IP address of the FQDN of the remote rsyslog server accordingly. The above line instructs the Rsyslog daemon to send all log messages, regardless of the facility or severity, to the host with the **IP 192.168.10.254** via **514/UDP** port.
![Configure Rsyslog Client](https://www.tecmint.com/wp-content/uploads/2017/09/Configure-Rsyslog-Client.png)Configure Rsyslog Client
**4.** If the remote log server is configured to listen only on TCP connections or you want to use a reliable transport network protocol, such as TCP, add another `@` character in front of the remote host as shown in the below example:
```
*. *  @@logs.domain.lan:514

```

The Linux rsyslog also allows has some special characters, such as `=` or `!`, which can be prefixed to priority levels to indicate “**this priority only** ” for equal sign and “**not this priority or higher than this** ”.
Some samples of Rsyslog priority level qualifiers in CentOS 7:
  * **kern.info** = kernel logs with info priority and higher.
  * **kern.=info** = only kernel messages with info priority.
  * **kern.info;kern.!err** = only kernel messages with info, notice, and warning priorities.
  * **kern.debug;kern.!=warning** = all kernel priorities except warning.
  * **kern.*** = all kernel priorities messages.
  * **kern.none** = don’t log any related kernel facility messages regardless of the priority.


For instance, assuming you want to send only a specific facility messages to a remote log server, such as all related mail messages regardless of the priority level, add the below line to rsyslog configuration file:
```
mail.* @192.168.10.254:514

```

**5.** Finally, in order to apply the new configuration, Rsyslog service needs to be restarted in order for the daemon to pick-up the changes, by running the below command:
```
# systemctl restart rsyslog.service

```

**6.** If for some reasons Rsyslog daemon is not enabled during the boot time, issue the below command to enable the service system-wide:
```
# systemctl enable rsyslog.service

```

### Step 3: Send Apache and Nginx Logs to a Remote Log Server
**7.** Apache HTTP server can be configured to send logs messages to a remote syslog server by adding the following line to its main configuration file as illustrated in the below example.
```
# vi /etc/httpd/conf/httpd.conf

```

On Apache main conf file add the below line.
```
CustomLog "| /bin/sh -c '/usr/bin/tee -a /var/log/httpd/httpd-access.log | /usr/bin/logger -thttpd -plocal1.notice'" combined

```

The line will enforce the HTTP daemon to write the log messages internally to the filesystem log file, but also process the messages further through a pipe to logger utility, which will send them to a distant syslog server, by marking them as coming from the local1 facility.
**8.** If you want to also direct **Apache** error log messages to a remote syslog server, add a new rule as the one presented in the above example, but make sure to replace the name of the httpd log file and the log file severity level to match error priority, as shown in the following sample:
```
ErrorLog "|/bin/sh -c '/usr/bin/tee -a /var/log/httpd/httpd-error.log | /usr/bin/logger -thttpd -plocal1.err'"

```

**9.** Once you’ve added the above lines, you need to restart Apache daemon to apply changes, by issuing the following command:
```
# systemctl restart httpd.service

```

**10.** As of version **1.7.1** , Nginx web server has built-in capabilities in order to directly log its messages to a remote syslog server, by adding the following lines of code to an nginx configuration file.
```
error_log syslog:server=192.168.1.10:514,facility=local7,tag=nginx,severity=error;
access_log syslog:server=192.168.10.254:514,facility=local7,tag=nginx,severity=info main;

```

For an **IPv6** server, use the following syntax format to enclose the IPv6 address.
```
access_log syslog:server=[7101:dc7::9]:514,facility=local7,tag=nginx,severity=info;

```

**11.** On the remote Rsyslog server you need to make the following change to rsyslog configuration file, in order to receive the logs send by Apache web server.
```
local1.* @Apache_IP_address:514

```

That’s all! You have successfully configured **Rsyslog** daemon to run in client mode and, also, you’ve instructed **Apache HTTP** server or **Nginx** to forward its log messages to a remote syslog server.
In case you system crashes, you should be able to investigate the problem by inspecting the log files content which are stored on the remote syslog server.
Tags [rsyslog](https://www.tecmint.com/tag/rsyslog/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[30 Useful ‘ps Command’ Examples for Linux Process Monitoring](https://www.tecmint.com/ps-command-examples-for-linux-process-monitoring/)
Next article:
[Learn Python Programming With This 8-Course BONUS Bundle](https://www.tecmint.com/learn-python-3-programming-online-courses/)
![Photo of author](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=100&d=blank&r=g)
Matei Cezar
I'am a computer addicted guy, a fan of open source and linux based system software, have about 4 years experience with Linux distributions desktop, servers and bash scripting.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#respond)** or
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
### 10 Comments
[Leave a Reply](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/03443b5a73bd22880cfb98c4e5160501367d31f98ab4747460060bac9b8e539e?s=50&d=blank&r=g)
vikri
[ November 26, 2020 at 9:44 am  ](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-1394747)
I got this error.
logger: unknown priority name: notice
any clue?
[Reply](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-1394747)
  2. ![](https://secure.gravatar.com/avatar/cfd85480646cee6cba1d5bddf95a5b302da1debd61ca67bc6f029b202388ebe4?s=50&d=blank&r=g)
eagle33
[ April 17, 2020 at 12:43 pm  ](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-1328161)
How to forward different path in the log to different ports in rsyslog server?
e.g **/var/log/message** to **514** and **/var/log/auth** to **1080**.
[Reply](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-1328161)
  3. ![](https://secure.gravatar.com/avatar/580a88f1b3684639d72eb03983ccd6b8891340015d7d768af1a969bba25325a1?s=50&d=blank&r=g)
Vương Quốc Mạnh
[ October 3, 2019 at 10:18 am  ](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-1260318)
Hello, can you tell me how to send an apache access log to ryslog server?
[Reply](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-1260318)
  4. ![](https://secure.gravatar.com/avatar/710b71977675b0fbd3544c0af0927ab7ec0689b7f5c73097ef3e4509b27610ae?s=50&d=blank&r=g)
SHUBHAM AGARWAL
[ May 27, 2018 at 1:37 pm  ](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-997405)
Please refer 11th point, You mentioned that on remote * **syslog server** * we need to make changes. But I think these changes are to be done on syslog client end (not on server end). By this client specifies that what logs to be sent to syslog server and on what port.
[Reply](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-997405)
     * ![](https://secure.gravatar.com/avatar/7bcb145c75d31b26efcf0115b433fb38ac79084b41ac5b2f28e086c9b04ed51c?s=50&d=blank&r=g)
gilroy toledano
[ November 21, 2018 at 12:32 pm  ](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-1062877)
totally agree with this
[Reply](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-1062877)
  5. ![](https://secure.gravatar.com/avatar/42f6e4fcf06b8307fe86303181be93feda9047f062116df6e7b34efde7fa1e10?s=50&d=blank&r=g)
Carlso mondree
[ February 12, 2018 at 9:32 pm  ](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-968590)
not working in Centos 7.4
[Reply](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-968590)
  6. ![](https://secure.gravatar.com/avatar/39048f273daf1e2d75731d82946af8fe9b92218559ce2a497decf3220ce908c9?s=50&d=blank&r=g)
Otis Gospodnetic
[ February 3, 2018 at 1:03 am  ](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-965825)
Rsyslog has been around for a really long time and lots of how-tos are old, so it’s good to see something fresh, Matei!
[Reply](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-965825)
  7. ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ September 14, 2017 at 12:23 pm  ](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-913271)
The point 5 code lines should look like this:
**
$template RemoteLogs,”/var/log/%HOSTNAME%/%PROGRAMNAME%.log”
*.* ?RemoteLogs
&~
**
and the next template:
$template FromIp,”/var/log/%FROMHOST-IP%.log”
*.* ?FromIp
&~
[Reply](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-913271)
  8. ![](https://secure.gravatar.com/avatar/a54fb3aa2cabf76bf01aeb7891a2ccf41bc083cbfa3723983ae643fbf34a3cd6?s=50&d=blank&r=g)
Jurgen Rastapopoulos
[ September 13, 2017 at 6:37 pm  ](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-913035)
Great! I may have spotted one typo though. At step 2, point 4, your first example of redirection is : `*. *` @192.168.10.254:514 Should there really be a space between the dot and the second star?
[Reply](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-913035)
     * ![](https://secure.gravatar.com/avatar/7dcb0cd247aa94896e665c337696a7be18d387a78d6d55b4854b7ff7d5925042?s=50&d=blank&r=g)
Amit
[ August 13, 2020 at 9:27 pm  ](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-1352821)
Nope. you are correct. Extra space should be deleted.
[Reply](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#comment-1352821)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/#respond)
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
[Tips to Create ISO from CD, Watch User Activity and Check Memory Usages of Browser](https://www.tecmint.com/creating-cdrom-iso-image-watch-user-activity-in-linux/)
[5 Command Line Tools to Find Files Quickly in Linux](https://www.tecmint.com/find-files-quickly-in-linux-terminal/)
[fdupes – A Command Line Tool to Find and Delete Duplicate Files in Linux](https://www.tecmint.com/fdupes-find-and-delete-duplicate-files-in-linux/)
[10 fdisk Commands to Manage Linux Disk Partitions](https://www.tecmint.com/fdisk-commands-to-manage-linux-disk-partitions/)
[How to Install Zip and Unzip in Linux](https://www.tecmint.com/install-zip-and-unzip-in-linux/)
[How to Copy File Permissions and Ownership to Another File in Linux](https://www.tecmint.com/copy-file-permissions-and-ownership-to-another-file-in-linux/)
## Linux Server Monitoring Tools
[4 Tools to Manage EXT2, EXT3 and EXT4 Health in Linux](https://www.tecmint.com/manage-ext2-ext3-and-ext4-health-in-linux/)
[Icinga: A Next Generation Open Source ‘Linux Server Monitoring’ Tool for RHEL/CentOS 7.0](https://www.tecmint.com/install-icinga-in-centos-7/)
[How to Create a Centralized Log Server with Rsyslog in CentOS/RHEL 7](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/)
[Duf – A Better Linux Disk Monitoring Utility](https://www.tecmint.com/duf-linux-disk-monitoring-utility/)
[Trickle – Control Network Traffic Bandwidth Of Applications in a Linux](https://www.tecmint.com/limit-linux-network-bandwidth-usage-with-trickle/)
[whowatch – Monitor Linux Users and Processes in Real Time](https://www.tecmint.com/whowatch-monitor-linux-users-and-processes-in-real-time/)
## Learn Linux Tricks & Tips
[Tips to Create ISO from CD, Watch User Activity and Check Memory Usages of Browser](https://www.tecmint.com/creating-cdrom-iso-image-watch-user-activity-in-linux/)
[5 Useful Ways to Do Arithmetic in Linux Terminal](https://www.tecmint.com/arithmetic-in-linux-terminal/)
[Learn Why ‘less’ is Faster Than ‘more’ Command for Effective File Navigation](https://www.tecmint.com/linux-more-command-and-less-command-examples/)
[How to Configure Custom SSH Connections to Simplify Remote Access](https://www.tecmint.com/configure-custom-ssh-connection-in-linux/)
[How to Increase Number of Open Files Limit in Linux](https://www.tecmint.com/increase-set-open-file-limits-in-linux/)
[How to Increase Disk Inode Number in Linux](https://www.tecmint.com/increase-disk-inode-number-in-linux/)
## Best Linux Tools
[5 Open Source Log Monitoring and Management Tools for Linux](https://www.tecmint.com/best-linux-log-monitoring-and-management-tools/)
[5 Best Reference Management Software for Linux in 2024](https://www.tecmint.com/reference-management-software/)
[Top 4 Google Docs Alternatives for Linux in 2024](https://www.tecmint.com/google-docs-alternatives/)
[5 Best Microsoft Word Alternatives for Linux in 2024](https://www.tecmint.com/microsoft-word-alternatives-linux/)
[18 Best NodeJS Frameworks for App Development in 2023](https://www.tecmint.com/best-nodejs-frameworks-for-developers/)
[Top 5 Open Source Collaboration Platforms for Linux in 2024](https://www.tecmint.com/open-source-collaboration-platforms-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/ "Scroll back to top")
Search for:
