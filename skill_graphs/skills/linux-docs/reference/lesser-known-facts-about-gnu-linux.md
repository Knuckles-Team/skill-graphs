[Skip to content](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/)
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
  * [Pro Courses](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/)
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
  * [Pro Courses](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/)
# How to Install and Configure Zabbix Agents on Remote Linux – Part 3
[Matei Cezar](https://www.tecmint.com/author/cezarmatei/ "View all posts by Matei Cezar")Last Updated: October 29, 2021 Read Time: 5 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [Zabbix](https://www.tecmint.com/category/zabbix/) [12 Comments](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comments)
Continuing the **Zabbix series** , this tutorial will guide you on how you can install and configure Zabbix agents on **Linux** ([Debian-based systems](https://www.tecmint.com/debian-based-linux-distributions/ "Best Debian-based Linux Distributions") and [RHEL-based distros](https://www.tecmint.com/redhat-based-linux-distributions/ "The Best RedHat-based Linux Distributions")) in order to actively monitor local resources on remote systems.
The main job of Zabbix agents consists in gathering local information from the targets where they run and sending the data to a central Zabbix server to be further processed and analyzed.
#### Requirements
Install and Configure **Zabbix** on **Debian/Ubuntu** and **RHEL** /**CentOS** /**Fedora** and **Rocky Linux** /**AlmaLinux**.
  * [How to Install Zabbix on RHEL/CentOS and Debian/Ubuntu – Part 1](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/ "Install Zabbix in Linux")
  * [How to Configure Zabbix to Send Email Alerts to Gmail Account – Part 2](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/ "Configure Zabbix to Send Email Alerts to Gmail Account – Part 2")


### Step 1: Install Zabbix Agents in Linux Systems
**1.** Depending on the Linux distribution you are running, go to the **[wget](https://www.tecmint.com/10-wget-command-examples-in-linux/ "Linux Wget Command Examples")** or **[curl](https://www.tecmint.com/linux-curl-command-examples/ "Linux Curl Command Examples")** and install it on your machine using the distribution-specific package manager – [Yum](https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/), [Rpm](https://www.tecmint.com/20-practical-examples-of-rpm-commands-in-linux/) or [Dpkg](https://www.tecmint.com/dpkg-command-examples/).
For **Debian/Ubuntu** systems (including latest releases) use the following steps to download and install Zabbix Agent:
#### Install Zabbix Agent in Debian
```
----------------- **On Debian 11** -----------------
$ wget https://repo.zabbix.com/zabbix/5.4/debian/pool/main/z/zabbix/zabbix-agent2_5.4.6-1+debian11_amd64.deb
$ sudo dpkg -i zabbix-agent2_5.4.6-1+debian11_amd64.deb

----------------- **On Debian 10** -----------------
$ wget https://repo.zabbix.com/zabbix/5.4/debian/pool/main/z/zabbix/zabbix-agent2_5.4.6-1+debian10_amd64.deb
$ sudo dpkg -i zabbix-agent2_5.4.6-1+debian10_amd64.deb

```

#### Install Zabbix Agent in Ubuntu
```
----------------- **On Ubuntu 20.04** -----------------
$ wget https://repo.zabbix.com/zabbix/5.4/ubuntu/pool/main/z/zabbix/zabbix-agent_5.4.7-1+ubuntu20.04_amd64.deb
$ sudo dpkg -i zabbix-agent_5.4.7-1+ubuntu20.04_amd64.deb

----------------- **On Ubuntu 18.04** -----------------
$ wget https://repo.zabbix.com/zabbix/5.4/ubuntu/pool/main/z/zabbix/zabbix-agent_5.4.7-1+ubuntu18.04_amd64.deb
$ sudo dpkg -i zabbix-agent_5.4.7-1+ubuntu18.04_amd64.deb

```

#### Install Zabbix On RHEL-based Systems
For **RHEL** alike systems, download the **.rpm** packaged for the distribution-specific release number, using the same page as above, and install it using rpm package manager.
In order to automatically manage missing dependency issues and install the agent using one-shot use the **yum** command followed by the binary package download link, as in the example below used for installing the agent on CentOS 8:
```
----------------- **On RHEL 8** -----------------
# rpm -Uvh https://repo.zabbix.com/zabbix/5.4/rhel/8/x86_64/zabbix-agent-5.4.6-1.el8.x86_64.rpm

----------------- **On RHEL 7** -----------------
# rpm -Uvh https://repo.zabbix.com/zabbix/5.4/rhel/7/x86_64/zabbix-agent-5.4.6-1.el7.x86_64.rpm

```

### Step 2: Configure and Test Zabbix Agent in Linux
**2.** The next logical step after installing the packages on the system is to open the **Zabbix** agent configuration file located in **/etc/zabbix/** system path on both major distributions and instruct the program to send all the collected information to the Zabbix server in order to be analyzed and processed.
Therefore, open the **zabbix_agentd.conf** file with your favorite text editor, find the below lines (use the screenshots as a guide), uncomment them and make the following changes:
```
# nano /etc/zabbix/zabbix_agentd.conf

```

add Zabbix server IP address and hostname as shown below.
Configure Zabbix Agent – zabbix_agentd.conf
```
Server=IP of Zabbix Server
ServerActive=IP of Zabbix Server
Hostname=use the FQDN of the node where the agent runs

```
![Add Zabbix Server IP Address](https://www.tecmint.com/wp-content/uploads/2015/10/Add-Zabbix-Server-IP-Address-620x108.png)Add Zabbix Server IP Address ![Add Zabbix Server Active IP Address](https://www.tecmint.com/wp-content/uploads/2015/10/Add-Zabbix-Server-Active-IP-Address-620x141.png)Add Zabbix Server Active IP Address ![Add Zabbix Agent Hostname](https://www.tecmint.com/wp-content/uploads/2015/10/Add-Zabbix-Agent-Hostname-620x136.png)Add Zabbix Agent Hostname
**3.** Once you’ve finished editing the Zabbix agent configuration file with the required values, restart the daemon using the following command, then use the [netstat command](https://www.tecmint.com/20-netstat-commands-for-linux-network-management/) to verify if the daemon has been started and operates on the specific port – **10050/tcp** :
```
$ sudo systemctl restart zabbix-agent
$ sudo netstat -tulpn|grep zabbix

```

For older distributions use the service command to manage Zabbix agent daemon:
```
$ sudo service zabbix-agent restart
$ sudo netstat -tulpn|grep zabbix

```
![Start Zabbix Agent](https://www.tecmint.com/wp-content/uploads/2015/10/Start-Zabbix-Agent-620x266.png)Start Zabbix Agent
**4.** If your system is behind a firewall then you need to open **10050/tcp** port on the system in order to reach through the Zabbix server.
For **Debian** based systems, including **Ubuntu** , you can use the [ufw tool](https://www.tecmint.com/how-to-install-and-configure-ufw-firewall/) to open the port and on **RHEL-based,** you can use [Firewalld utility](https://www.tecmint.com/firewalld-rules-for-centos-7/) to manage the firewall rules as the below examples:
```
$ sudo ufw allow 10050/tcp  [On **Debian** based systems]

```
```
$ sudo firewall-cmd --add-port=10050/tcp --permanent  [On **RHEL** based systems]

```

For older distributions such as **RHEL/CentOS 6** or unmanaged firewalls through specific utilities use the powerful **iptables** command to open ports:
```
# iptables -A INPUT -p tcp -m tcp --dport 10050 -j ACCEPT

```

5. Finally, in order to test if you can reach Zabbix Agent from Zabbix Server, use **Telnet** command from Zabbix server machine to the IP addresses of the machines that run the agents, as illustrated below (don’t worry about the thrown error from agents):
```
# telnet zabbix_agent_IP 10050

```
![Check Zabbix Agent Connection](https://www.tecmint.com/wp-content/uploads/2015/10/Check-Zabbix-Agent-Connection-620x176.jpg)Check Zabbix Agent Connection
### Step 3: Add Zabbix Agent Monitored Host to Zabbix Server
**6.** On the next step it’s time to move to the Zabbix server web console and start adding the hosts which run zabbix agent in order to be monitored by the server.
Go to **Configuration** -> **Hosts** -> **Create Host** -> **Host** tab and fill the **Hostname** field with the FQDN of the monitored Zabbix agent machine, use the same value as above for the Visible name field.
Next, add this host to a group of monitored servers and use the IP Address of the monitored machine at the Agent interfaces field – alternatively you can also use DNS resolution if it’s the case. Use the below screenshots as a guide.
![Add Linux Host to Zabbix Monitoring](https://www.tecmint.com/wp-content/uploads/2015/10/Add-Linux-Host-to-Zabbix-Monitoring1-620x236.jpg)Add Linux Host to Zabbix Monitoring ![Add Linux Host to Zabbix Host Group](https://www.tecmint.com/wp-content/uploads/2015/10/Add-Linux-Host-to-Zabbix-Host-Group-620x391.jpg)Add Linux Host to Zabbix Host Group
**7.** Next, move to the **Templates** tab and hit **Select**. A new window with templates should open. Choose **Template OS Linux** then scroll down and hit on Select button to add it and automatically close the window.
![Add Zabbix Linux OS Template](https://www.tecmint.com/wp-content/uploads/2015/10/Add-Linux-host-Template-620x276.jpg)Add Zabbix Linux OS Template ![Select Linux OS Template](https://www.tecmint.com/wp-content/uploads/2015/10/Select-Linux-OS-Template-620x395.jpg)Select Linux OS Template
**8.** Once the template appears to **Link the new template** box, hit on **Add** text to link it to Zabbix server, then hit on the lower **Add** button to finish the process and completely add the monitored host. The visible name of the monitored host should now appear hosts window.
![Link New Linux OS Template](https://www.tecmint.com/wp-content/uploads/2015/10/Link-New-Linux-OS-Template-620x289.jpg)Link New Linux OS Template ![Add Linux OS Template](https://www.tecmint.com/wp-content/uploads/2015/10/Add-Linux-OS-Template-620x276.jpg)Add Linux OS Template ![Added Linux Host to Zabbix](https://www.tecmint.com/wp-content/uploads/2015/10/Added-Linux-Host-to-Zabbix-620x297.png)Added Linux Host to Zabbix
That’s all! Just assure that the host **Status** is set to **Enabled** and wait a few minutes in order for the Zabbix server to contact the agent, process the received data, and inform or eventually alert you if something goes bad on the monitored target.
Tags [linux monitoring](https://www.tecmint.com/tag/linux-monitoring/), [zabbix](https://www.tecmint.com/tag/zabbix/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Configure Zabbix to Send Email Alerts to Gmail Account – Part 2](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/)
Next article:
[How to Install Zabbix Agent and Add Windows Host to Zabbix Monitoring – Part 4](https://www.tecmint.com/install-zabbix-agent-and-add-windows-host-to-zabbix-monioring/)
![Photo of author](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=100&d=blank&r=g)
Matei Cezar
I'am a computer addicted guy, a fan of open source and linux based system software, have about 4 years experience with Linux distributions desktop, servers and bash scripting.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#respond)** or
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
### 12 Comments
[Leave a Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/dc8cfe64ce935633d06c485db2476400216c9c4fde02539f0b23134df4c581d6?s=50&d=blank&r=g)
Pedro
[ October 5, 2022 at 9:50 am  ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-1891730)
Best tutorial page of **zabbix** , everything is working fine, you are the best! I hope you could do the same with cacti, it is a little bit more stressful.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-1891730)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 5, 2022 at 9:56 am  ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-1891733)
@Pedro,
Here is the Cacti guide – [How to Install Cacti on Rocky Linux and AlmaLinux](https://www.tecmint.com/install-cacti-on-rocky-linux-almalinux/ "How to Install Cacti on Rocky Linux and AlmaLinux")
[Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-1891733)
  2. ![](https://secure.gravatar.com/avatar/93d5bea0752e44ddfe96dec8701ac4b0e9f71c5c8b93fb34863ad89e3ed8116e?s=50&d=blank&r=g)
adrian
[ December 1, 2021 at 9:50 pm  ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-1667049)
Hello, very good tutorial, I would like you to help me, I would like to be able to monitor the VMs within WMWARE ESXI. Thank you
[Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-1667049)
  3. ![](https://secure.gravatar.com/avatar/25198e8b2d27cd67a2eac9e84b88a812703ff5906145756d4da072043cb39a14?s=50&d=blank&r=g)
Sergio
[ November 18, 2021 at 11:57 pm  ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-1653390)
Hi,
Just one question…
For Debian, the package is **zabbix-agent2_*.deb** (with the 2), but for Ubuntu and CentOS/RH is zabbix-agent_*.(deb or rpm).
Even the config file is **/etc/zabbix/zabbix_agent.conf** with zabbix-agent_*.(deb or rpm), but for Debian is **zabbix-agent2.conf**.
Is that OK??
[Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-1653390)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 19, 2021 at 10:57 am  ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-1653947)
@Sergio,
Yes, it is okay…
Zabbix agent 2 is a new version of Zabbix agent and may be used in place of the Zabbix agent in Debian’s latest versions…
[Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-1653947)
  4. ![](https://secure.gravatar.com/avatar/5813636920ed873a099b943ec1c50c71a63162b82707121a84b654ad6ebfd20a?s=50&d=blank&r=g)
Norberto Valverde Llanos
[ September 21, 2019 at 3:23 am  ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-1249500)
Hello
Any guide to install and configure the Zabbix agent on Unix Sun Solaris?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-1249500)
  5. ![](https://secure.gravatar.com/avatar/653f809ae336bfd751b02e0fbf38b067d8ae3b7ade0960b87f998f8fe3a6ad15?s=50&d=blank&r=g)
arvin karimi
[ December 16, 2017 at 4:44 pm  ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-949948)
thanks ,it was very useful.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-949948)
  6. ![](https://secure.gravatar.com/avatar/318cf329b4f6969c7064679c934d9862846aba5e2a1509815616fd0cf1f59470?s=50&d=blank&r=g)
Jaz
[ March 2, 2017 at 5:02 pm  ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-872279)
How to install zabbix agent on multiple Ubuntu systems connected in lan from a single admin terminal. I need a shell script to do this. Any suggestions?
Thanks in advance
[Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-872279)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ March 3, 2017 at 6:53 pm  ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-872571)
Use an automation program , such as Ansible, Puppet for that. You can use bash, perl or python for that matter also. Nobody will write a script for you. Learn and do it yourshelf. Nobody knows what your requirements are (what distros, IPs, hosts etc)
[Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-872571)
  7. ![](https://secure.gravatar.com/avatar/514204d781baddc790d0fd0958249f91befb782fa701798c77730ef18b1f7732?s=50&d=blank&r=g)
subramanyam
[ March 18, 2016 at 8:49 am  ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-761384)
please can any one add tutorial on how to change alerts of disk usage percentage (average, critical, warning and etc)
[Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-761384)
  8. ![](https://secure.gravatar.com/avatar/f10837ac50a3cc72a69c4e95068e3094ca65db28b250ac47f5041bb5184b32b5?s=50&d=blank&r=g)
Ambarish
[ February 18, 2016 at 5:56 pm  ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-752660)
Thanks for the detailed how-to.
Now that Zabbix 3 is released, do you have plans to write and upgrade guide on this?

[Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-752660)
  9. ![](https://secure.gravatar.com/avatar/cdde08bd018900e6784a5b1ffa6e0b51829f8cf8b7ee817a59db230b9fb78d36?s=50&d=blank&r=g)
Klein
[ October 9, 2015 at 8:06 pm  ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-682732)
Eu só recomendaria não instalar o pacote no CentOS diretamente do RPM do jeito que você fez, o correto seria criar um repositório (eu acho que o zabbix tem um).
Ou usar o epel (
E toda vez que executar yum update, se houver um pacote mais recente no epel, ele já atualiza.
**Translated to English**
I would recommend not only install the package on CentOS RPM directly the way you did, correct would be to create a repository ( I think the zabbix have one) .
Or use the EPEL (
And each time you run yum update if there is a newer package in EPEL , it has updated .
[Reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#comment-682732)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/#respond)
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
[Learn Difference Between “su” and “su -” Commands in Linux](https://www.tecmint.com/difference-between-su-and-su-commands-in-linux/)
[How to Download Files to Specific Directory Using Wget](https://www.tecmint.com/wget-download-file-to-specific-directory/)
[How Linux Services and Daemons Work (and How to Control Them)](https://www.tecmint.com/linux-services-and-daemons/)
[How to Lock a File for Renaming/Deleting in Linux](https://www.tecmint.com/prevent-file-deletion-linux/)
[How to Fix “passwd: Authentication token manipulation error” in Linux](https://www.tecmint.com/fix-passwd-authentication-token-manipulation-error-in-linux/)
[How to Copy File Permissions and Ownership to Another File in Linux](https://www.tecmint.com/copy-file-permissions-and-ownership-to-another-file-in-linux/)
## Linux Server Monitoring Tools
[How to Add Windows Host to Nagios Monitoring Server](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/)
[ngrep – A Network Packet Analyzer for Linux](https://www.tecmint.com/ngrep-network-packet-analyzer-for-linux/)
[How to Monitor Nginx Performance Using Netdata on CentOS 7](https://www.tecmint.com/monitor-nginx-performance-using-netdata-on-centos-7/)
[How to Boost Linux Server Internet Speed with TCP BBR](https://www.tecmint.com/increase-linux-server-internet-speed-with-tcp-bbr/)
[Sysstat – All-in-One System Performance and Usage Activity Monitoring Tool For Linux](https://www.tecmint.com/install-sysstat-in-linux/)
[Icinga: A Next Generation Open Source ‘Linux Server Monitoring’ Tool for RHEL/CentOS 7.0](https://www.tecmint.com/install-icinga-in-centos-7/)
## Learn Linux Tricks & Tips
[How to Use ‘at’ Command to Schedule a Task on Given or Later Time in Linux](https://www.tecmint.com/linux-cron-alternative-at-command-to-schedule-tasks/)
[How to Find Number of Files in a Directory and Subdirectories](https://www.tecmint.com/find-number-of-files-in-directory-subdirectories-linux/)
[How to Delete HUGE (100-200GB) Files in Linux](https://www.tecmint.com/delete-huge-files-in-linux/)
[Progress – Show Percentage of Copied Data for (cp, mv, dd, tar) Commands](https://www.tecmint.com/show-progress-linux-commands/)
[Lolcat – Display Text in Rainbow Colors in Linux Terminal](https://www.tecmint.com/lolcat-color-output-linux-terminal/)
[10 Useful Sudoers Configurations for Setting ‘sudo’ in Linux](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/)
## Best Linux Tools
[Top 7 Apps to Install for Your Nextcloud Instance](https://www.tecmint.com/nextcloud-apps/)
[10 Best Linux File and Disk Encryption Tools (2024)](https://www.tecmint.com/file-and-disk-encryption-tools-for-linux/)
[10 Best PuTTY Alternatives for SSH Remote Connection](https://www.tecmint.com/putty-alternatives/)
[Universal Package Managers for Linux: Snap, Flatpak, and AppImage](https://www.tecmint.com/cross-distribution-package-managers-for-linux/)
[25 Outstanding Backup Utilities for Linux Systems in 2024](https://www.tecmint.com/linux-system-backup-tools/)
[19 Best Open Source WYSIWYG HTML Editors in 2023](https://www.tecmint.com/wysiwyg-html-editors/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/ "Scroll back to top")
Search for:
