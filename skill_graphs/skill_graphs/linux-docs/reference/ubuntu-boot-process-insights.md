[Skip to content](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/)
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
  * [Pro Courses](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/)
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
  * [Pro Courses](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/)
# How to Install and Configure ‘Collectd’ and ‘Collectd-Web’ to Monitor Server Resources in Linux
[Matei Cezar](https://www.tecmint.com/author/cezarmatei/ "View all posts by Matei Cezar")Last Updated: June 30, 2015 Read Time: 8 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [17 Comments](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comments)
**Collectd-web** is a web front-end monitoring tool based on RRDtool (**R** ound-**R** obin **D** atabase **Tool)** , which interprets and graphical outputs the data collected by the **Collectd** service on Linux systems.
**Collectd** service comes by default with a huge collection of available plug-ins into its default configuration file, some of them being, by default, already activated once you have installed the software package.
**Collectd-web CGI** scripts which interprets and generates the graphical html page statistics can be simply executed by the **Apache CGI** gateway with minimal of configurations required on Apache web server side.
However, the graphical web interface with the generated statistics can, also, be executed by the standalone web server offered by **Python CGIHTTPServer** script that comes pre-installed with the main **Git** repository.
This tutorial will cover the installation process of **Collectd** service and **Collectd-web** interface on **RHEL/CentOS/Fedora** and **Ubuntu/Debian** based systems with the minimal configurations needed to be done in order to run the services and to enable a **Collectd** service plug-in.
Please go through the following articles of **collectd** series.
**Part 1** : **Install and Configure ‘Collectd’ and ‘Collectd-Web’ to Monitor Linux Resources**
**Part 2** : [Monitor Linux Resources with Collectd-web and Apache CGI](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/)
**Part 3** : [Configure Collectd as a Central Monitoring Server for Clients](https://www.tecmint.com/configure-collectd-as-central-monitoring-server-for-clients/)
### Step 1: – Install Collectd Service
**1.** Basically, the **Collectd** daemon task is to gather and store data statistics on the system that it runs on. The **Collectd** package can be downloaded and installed from the default Debian based distribution repositories by issuing the following command:
##### On Ubuntu/Debian
```
# apt-get install collectd			[On **Debian** based Systems]

```
![Install Collectd on Ubuntu](https://www.tecmint.com/wp-content/uploads/2015/04/Install-Collectd-on-Ubuntu-568x450.png) Install Collectd on Debian/Ubuntu
##### On RHEL/CentOS 6.x/5.x
On older **RedHat** based systems like **CentOS/Fedora** , you first need to [enable epel repository](https://www.tecmint.com/how-to-enable-epel-repository-for-rhel-centos-6-5/ "Enable EPEL Repository ") under your system, then you can able to install **collectd** package from the epel repository.
```
# yum install collectd

```

##### On RHEL/CentOS 7.x
On latest version of RHEL/CentOS 7.x, you can install and enable epel repository from default yum repos as shown below.
```
# yum install epel-release
# yum install collectd

```
![Install Collectd on CentOS](https://www.tecmint.com/wp-content/uploads/2015/04/Install-Collectd-on-CentOS-620x344.png)Install Collectd on CentOS/RHEL/Fedora
**Note:** For Fedora users, no need to enable any third party repositories, simple yum to get the collectd package from default yum repositories.
**2.** Once the package is installed on your system, run the below command in order to start the service.
```
# service collectd start			[On **Debian** based Systems]
# service collectd start                        [On **RHEL/CentOS 6.x/5.x** Systems]
# systemctl start collectd.service              [On **RHEL/CentOS 7.x** Systems]

```

### Step 2: Install Collectd-Web and Dependencies
**3.** Before starting to import the **Collectd-web** Git repository, first you need to assure that **Git** software package and the following required dependencies are installed on your machine:
```
----------------- On **Debian / Ubuntu** systems -----------------
# apt-get install git
# apt-get install librrds-perl libjson-perl libhtml-parser-perl

```
![Install Git on Ubuntu](https://www.tecmint.com/wp-content/uploads/2015/04/Install-Git-on-Ubuntu-620x242.png) Install Git on Debian/Ubuntu ```
----------------- On **RedHat/CentOS/Fedora** based systems -----------------
# yum install git
# yum install rrdtool rrdtool-devel rrdtool-perl perl-HTML-Parser perl-JSON

```
![Install Git on CentOS](https://www.tecmint.com/wp-content/uploads/2015/04/Install-Git-on-CentOS-620x344.png) Install Git and Dependencies
### Step 3: Import Collectd-Web Git Repository and Modify Standalone Python Server
**4.** On the next step choose and change the directory to a system path from the Linux tree hierarchy where you want to import the Git project (you can use `/usr/local/` path), then run the following command to clone **Collectd-web** git repository:
```
# cd /usr/local/
# git clone https://github.com/httpdss/collectd-web.git

```
![Git Clone Collectd-Web](https://www.tecmint.com/wp-content/uploads/2015/04/Clone-Collectd-Web-620x344.png)Git Clone Collectd-Web
**5.** Once the Git repository is imported into your system, go ahead and enter the **collectd-web** directory and list its contents in order to identify the Python server script (`runserver.py`), which will be modified on the next step. Also, add execution permissions to the following CGI script: `graphdefs.cgi`.
```
# cd collectd-web/
# ls
# chmod +x cgi-bin/graphdefs.cgi

```
![Set Execute Permission](https://www.tecmint.com/wp-content/uploads/2015/04/Set-Execute-Permission-620x344.png)Set Execute Permission
**6.** **Collectd-web** standalone Python server script is configured by default to run and bind only on **loopback address (127.0.0.1)**.
In order to access **Collectd-web** interface from a remote browser, you need to edit the `runserver.py` script and change the **127.0.1.1 IP** Address to **0.0.0.0** , in order to bind on all network interfaces IP Addresses.
If you want to bind only on a specific interface, then use that interface IP Address (not advised to use this option in case your network interface Address is dynamically allocated by a DHCP server). Use the below screenshot as an excerpt on how the final `runserver.py` script should look like:
```
# nano runserver.py

```
![Configure Collect-web](https://www.tecmint.com/wp-content/uploads/2015/04/Configure-Collect-web-620x361.png)Configure Collect-web
If you want to use another network port than **8888** , modify the PORT variable value.
### Step 4: Run Python CGI Standalone Server and Browse Collectd-web Interface
**7.** After you have modified the standalone Python server script IP Address binding, go ahead and start the server in background by issuing the following command:
```
# ./runserver.py &

```

Optional, as an alternate method you can call the Python interpreter to start the server:
```
# python runserver.py &

```
![Start Collect-Web Server](https://www.tecmint.com/wp-content/uploads/2015/04/Start-Collect-Web-620x344.png)Start Collect-Web Server
Pages: 1 [2](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/2/)
Tags [collectd](https://www.tecmint.com/tag/collectd/), [collectd-web](https://www.tecmint.com/tag/collectd-web/), [linux monitoring](https://www.tecmint.com/tag/linux-monitoring/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[30 Things to Do After Minimal RHEL/CentOS 7 Installation](https://www.tecmint.com/things-to-do-after-minimal-rhel-centos-7-installation/)
Next article:
[15 Things to Do After Installing Ubuntu 15.04 Desktop](https://www.tecmint.com/things-to-do-after-installing-ubuntu-15-04-desktop/)
![Photo of author](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=100&d=blank&r=g)
Matei Cezar
I'am a computer addicted guy, a fan of open source and linux based system software, have about 4 years experience with Linux distributions desktop, servers and bash scripting.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#respond)** or
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
### 17 Comments
[Leave a Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/8c59b9a32ed8390614993a58cac354e27bc5ad1367c36a2f3ad3d2fe880e23d8?s=50&d=blank&r=g)
Mohsin Feroz
[ February 6, 2020 at 5:28 am  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-1315065)
Can anyone draft the `runserver.py` file to support python3? The current file is not working.
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-1315065)
  2. ![](https://secure.gravatar.com/avatar/925f17f37126222f77cd9c721b8092b24714707dbb1a701ddab2199aeb088ec2?s=50&d=blank&r=g)
DineshVNV
[ June 21, 2018 at 8:31 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-1005705)
Hi
I have installed collectd and the service is up and running. I have configured the ip address in the python script and the UI is accessible, but when i enable the plugin in **/etc/collectd.conf** i am not able to see anything in the web console.
Kindly help to solve my issue.
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-1005705)
  3. ![](https://secure.gravatar.com/avatar/ba85cfac4586666d0df8e9d193662b559bd20aecb0fc453b750a44d7eb3d6950?s=50&d=blank&r=g)
Joerg
[ May 8, 2018 at 2:22 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-990409)
Great article but I have a problem already at step 8. It produces a web-page without any graphics and the button “**server.example.lan** ” is missing.
Thank you so much
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-990409)
     * ![](https://secure.gravatar.com/avatar/13db16d88abb8f3b5948eda4c2c287be625929be974c2e9c2a81b6c7289b5bc0?s=50&d=blank&r=g)
Matt
[ June 21, 2018 at 8:52 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-1005707)
Hi, I also have this problem, have you found a solution?
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-1005707)
  4. ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ March 16, 2017 at 12:49 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-875979)
@adji: Check if the configuration file look ok by running the following command: collectd -t
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-875979)
  5. ![](https://secure.gravatar.com/avatar/cee17573c9c86e2102756a35c6ecd13f7c338ef10804ec2aa497008626dc3f0a?s=50&d=blank&r=g)
kumar
[ August 29, 2016 at 3:31 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-810720)
This post is bit out dated for CentOS 7.2 yum install collectd does not seem to create folder /etc/collectd/collectd.conf.d or /etc/collectd. collectd.conf file is installed in /etc/collectd.conf. How do i get collectd-web to work with collectd. the version it is installing is collectd.x86_64 0:5.5.2-1.el7
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-810720)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 29, 2016 at 4:45 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-810738)
@Kumar
Thanks for pointing out those configuration files of Collectd, let me check the instructions on latest CentOS 7.2 and will update the article with new supported instructions..
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-810738)
       * ![](https://secure.gravatar.com/avatar/cee17573c9c86e2102756a35c6ecd13f7c338ef10804ec2aa497008626dc3f0a?s=50&d=blank&r=g)
kumar
[ September 6, 2016 at 8:42 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-813618)
Thanks for looking into this. Is there any ETA when you would be able to updated this doc. Looking forward for the latest document.
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-813618)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ September 7, 2016 at 10:55 am  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-813822)
@Kumar,
Sorry for delay, but I think by this weekend will update this article with new latest instructions..
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-813822)
  6. ![](https://secure.gravatar.com/avatar/392c9d1596efe48b365754b60f0ececaca3035209fbc91ea9ec697a6e565faa4?s=50&d=blank&r=g)
Gabonvikar
[ June 22, 2016 at 12:43 am  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-793535)
I want to point out that this is by no means a complete instructional when dealing with Centos 6.7
There were several steps required in order to make this work, such as:
Un-commenting out the rrdtool plugin line in collectd.conf.
Adding the rrdtool plugin definition in collectd.conf
Creating a configuration file: collection.conf in /etc/collectd for collectd-web to get rrdfile location details from.
Installing the collectd-rrdtool package
After I had gone though and did all of these things, collectd started loading information in to my collectd-web interface, but not before. I hope this helps someone who is stuck.
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-793535)
  7. ![](https://secure.gravatar.com/avatar/65f3a4e39bb6ace1446d411d6a84330a631f1a21033ef3547c265986de255714?s=50&d=blank&r=g)
Jagpac
[ January 30, 2016 at 10:38 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-746098)
Thank you. This is a great article and I now have everything set up. However, does anybody know how to protect the web interface with a password ? I just don’t like the idea that anybody can connect on the interface and see the data.
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-746098)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ February 1, 2016 at 5:50 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-746762)
htpasswd –c /path/to/collectd_directory/.htpasswd your_user
Open Apache config file and add the following statements:
AuthType basic
AuthName “What ever message you want”
AuthBasicProvider file
AuthUserFile /path/to/collectd_directory/.htpasswd
Require user your_user
Then a2enmod auth_basic and restart apache daemon.
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-746762)
       * ![](https://secure.gravatar.com/avatar/65f3a4e39bb6ace1446d411d6a84330a631f1a21033ef3547c265986de255714?s=50&d=blank&r=g)
Jagpac
[ February 7, 2016 at 11:24 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-748921)
Thank you for your answer. However, I don’t think this solution is appropriate here because we’re not using Apache for the web interface (we are using a python module).
I found a solution by modifying the runserver.py file using the information on this page :
I simply put the content of the class AuthHandler in the class Handler of the runserver.py file and added a few more lines here and there (to use the key and import the stuff needed) and it works !
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-748921)
  8. ![](https://secure.gravatar.com/avatar/74bfe85ffba8e041759ae77b6b6fa203005a83843a6e8a3a971da527f4e652b6?s=50&d=blank&r=g)
Cooky
[ November 17, 2015 at 4:13 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-707541)
Thank you so much! You saved my day, ur post is great for beginners like me! Could follow every step :)
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-707541)
  9. ![](https://secure.gravatar.com/avatar/15edbe265446c4e15fa5133184d8b97c47492ecd6e3ba98c1df4421bbfafa17d?s=50&d=blank&r=g)
G
[ October 14, 2015 at 12:20 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-685835)
Wow this is a great article. I didn’t have to go off your steps once which is rare in my experience.
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-685835)
  10. ![](https://secure.gravatar.com/avatar/505b4926ba5b27c30223414715c688b0d7e522342e4f22466316b86a462702bf?s=50&d=blank&r=g)
omipenguin
[ April 24, 2015 at 4:39 pm  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-550910)
Great post as usual. But i prefer Munin Server-Client. Can anyone is tecmint please make a tutorial on SAN. I know no one own SAN at home. But it will be helpful if someone make a demo on
1: Discovering HBA and what is WWN and how to know
2: Discovering LUN
3: And multipathing
Because this is one critical thing and Information on this subject is just scattered and there is no sequence like what thing should be done first and then and then and then ……
Please please make a tut on it or if not possible then please give us theoretical tutorial with commands ……. Thanks and Bless you
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-550910)
  11. ![](https://secure.gravatar.com/avatar/5ed0ea670d7b942644f03005638cfa26654ec6813bbabccff758eb1d928ecb89?s=50&d=blank&r=g)
konrad
[ April 24, 2015 at 2:49 am  ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-550405)
Hi,
Great article. Could You write manual ex: svn+trac oraz gitolite with migrate actual svn/trac/git arch ?
[Reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#comment-550405)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/#respond)
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
[20 Basic ‘ls’ Command Examples in Linux](https://www.tecmint.com/ls-command-in-linux/)
[Fish – A Smart and User-Friendly Interactive Shell for Linux](https://www.tecmint.com/fish-a-smart-and-user-friendly-interactive-shell-for-linux/)
[How to Search DuckDuckGo from the Linux Terminal](https://www.tecmint.com/search-duckduckgo-from-linux-terminal/)
[DSH (Distributed Shell) – Run Commands on Multiple Linux Servers](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/)
[How to Execute MySQL Queries via Linux Terminal](https://www.tecmint.com/run-mysql-queries-linux-command-line/)
[How to Run or Repeat a Linux Command Every X Seconds Forever](https://www.tecmint.com/run-repeat-linux-command-every-x-seconds/)
## Linux Server Monitoring Tools
[4 Ways to Watch or Monitor Log Files in Real Time](https://www.tecmint.com/watch-or-monitor-linux-log-files-in-real-time/)
[How to Do Security Auditing of Linux System Using Lynis Tool](https://www.tecmint.com/linux-security-auditing-and-scanning-with-lynis-tool/)
[How to Install Cacti on Rocky Linux and AlmaLinux](https://www.tecmint.com/install-cacti-on-rocky-linux-almalinux/)
[24 Best Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)
[LibreNMS – A Fully Featured Network Monitoring Tool for Linux](https://www.tecmint.com/install-librenms-monitoring-on-ubuntu-centos/)
[How To Install and Connect an Agent to Pandora FMS Server](https://www.tecmint.com/install-and-connect-an-agent-to-pandora-fms-server/)
## Learn Linux Tricks & Tips
[Progress – Show Percentage of Copied Data for (cp, mv, dd, tar) Commands](https://www.tecmint.com/show-progress-linux-commands/)
[Learn Difference Between “su” and “su -” Commands in Linux](https://www.tecmint.com/difference-between-su-and-su-commands-in-linux/)
[4 Useful Tips on mkdir, tar and kill Commands in Linux](https://www.tecmint.com/mkdir-tar-and-kill-commands-in-linux/)
[5 Command Line Tools to Find Files Quickly in Linux](https://www.tecmint.com/find-files-quickly-in-linux-terminal/)
[How to Auto Execute Commands/Scripts During Reboot or Startup](https://www.tecmint.com/auto-execute-linux-scripts-during-reboot-or-startup/)
[Add Rainbow Colors to Linux Command Output in Slow Motion](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/)
## Best Linux Tools
[3 Best Document Collaboration Platforms for Linux in 2024](https://www.tecmint.com/document-collaboration-platforms-linux/)
[21 Best Slack Alternatives for Team Chat [Free & Paid]](https://www.tecmint.com/slack-alternatives/)
[8 Best SSH Clients for Linux in 2024](https://www.tecmint.com/ssh-clients-linux/)
[Top 5 Open-Source Enterprise Software for Linux in 2024](https://www.tecmint.com/open-source-enterprise-software-linux/)
[5 Best Microsoft Word Alternatives for Linux in 2024](https://www.tecmint.com/microsoft-word-alternatives-linux/)
[11 Best GUI Tools for Linux System Administrators in 2024](https://www.tecmint.com/gui-tools-for-linux-system-administrators/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/ "Scroll back to top")
Search for:
