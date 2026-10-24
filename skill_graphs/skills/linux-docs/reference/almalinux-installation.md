[Skip to content](https://www.tecmint.com/install-nagios-on-rhel-8/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-nagios-on-rhel-8/)
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
  * [Pro Courses](https://www.tecmint.com/install-nagios-on-rhel-8/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-nagios-on-rhel-8/)
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
  * [Pro Courses](https://www.tecmint.com/install-nagios-on-rhel-8/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-nagios-on-rhel-8/)
# How to Install Nagios Monitoring Tool on RHEL 8
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: July 1, 2019 Read Time: 3 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [RedHat](https://www.tecmint.com/category/redhat/) [Leave a comment](https://www.tecmint.com/install-nagios-on-rhel-8/#respond)
**Nagios Core** is an open source IT infrastructure monitoring and alerting platform built using **PHP**. It is used for monitoring mission-critical IT infrastructure components such as network infrastructure, servers, network protocols, system metrics, applications, and services.
In addition, **Nagios Core** supports alerting (when critical infrastructure components fail and recover), via email, SMS, or custom script, and reporting of the historical record of events, outages, notifications, and alert response for later analysis.
Importantly, **Nagios Core** ships with multiple API’s that provide integration with existing or third-party applications as well as community-developed add-ons.
This article will walk you through the process of installing **Nagios Core 4.4.3** and **Nagios Plugins** 2.2.1 in **RHEL 8** Linux distribution.
#### Requirements:
  1. [RHEL 8 with Minimal Installation](https://www.tecmint.com/installation-of-rhel-8/)
  2. [RHEL 8 with RedHat Subscription Enabled](https://www.tecmint.com/enable-rhel-subscription-in-rhel-8/)
  3. [RHEL 8 with Static IP Address](https://www.tecmint.com/set-static-ip-address-in-rhel-8/)


### Step 1: Install Required Dependencies
**1.** To install **Nagios Core** package from sources, you need to install following dependencies including Apache HTTP server and PHP using the default [dnf package manager](https://www.tecmint.com/dnf-commands-for-fedora-rpm-package-management/).
```
# dnf install -y gcc glibc glibc-common perl httpd php wget gd gd-devel

```

**2.** Next, start the **HTTPD** service for now, enable it to automatically start at system boot and check its status using the [systemctl commands](https://www.tecmint.com/manage-apache-web-server-in-linux/).
```
# systemctl start httpd
# systemctl enable httpd
# systemctl start httpd

```

### Step 2: Downloading, Compiling and Installing Nagios Core
**3.** Now download the **Nagios Core** source package using [wget command](https://www.tecmint.com/10-wget-command-examples-in-linux/), extract it and move into the extracted directory as shown.
```
# wget -O nagioscore.tar.gz https://github.com/NagiosEnterprises/nagioscore/archive/nagios-4.4.3.tar.gz
# tar xzf nagioscore.tar.gz
# cd nagioscore-nagios-4.4.3/

```

**4.** Next, run the following commands to configure the source package and build it.
```
# ./configure
# make all

```

**5.** After that create the Nagios User and Group, and add the Apache user to the Nagios Group as follows.
```
# make install-groups-users
# usermod -a -G nagios apache

```

**6.** Now install the binary files, CGIs, and HTML files with using the following commands.
```
# make install
# make install-daemoninit

```

**7.** Next, run the following commands to install and configure the external command file, a sample configuration file and the **Apache-Nagios** configuration file.
```
# make install-commandmode		#installs and configures the external command file
# make install-config			#installs the *SAMPLE* configuration files.
# make install-webconf		        #installs the Apache web server configuration files.

```

**8.** In this step, you need to secure the **Nagios Core** web console using [HTTP basic authentication](https://www.tecmint.com/password-protect-apache-web-directories-using-htaccess/). So, you’ll need to create an Apache user account to be able to log into Nagios – this account will act as the Nagios Administrator account.
```
# htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin

```

### Step 3: Installing Nagio Plugins in RHEL 8
**9.** Next, you need to install necessary Nagios plugins. But before you download and install the Nagios plugins, you need to install the required packages for compiling and building the plugin package.
```
# dnf install -y gcc glibc glibc-common make gettext automake autoconf wget openssl-devel net-snmp net-snmp-utils

```

**10.** Then download and extract the latest version of the **Nagios Plugins** using the following commands.
```
# wget --no-check-certificate -O nagios-plugins.tar.gz https://github.com/nagios-plugins/nagios-plugins/archive/release-2.2.1.tar.gz
# tar zxf nagios-plugins.tar.gz

```

**11.** Move into the extracted directory, compile, build and install the Nagios Plugins install the Nagios Plugins as follows.
```
# cd nagios-plugins-release-2.2.1/
# ./tools/setup
# ./configure
# make
# make install

```

**12.** At this point, you have set up the Nagios Core service and configured it to work with the Apache HTTP server. Now you need to restart the HTTPD service. Also, start and enable the Nagios service and check if it is up and running as follows.
```
# systemctl restart httpd.service
# systemctl start nagios.service
# systemctl start nagios.service
# systemctl start nagios.service

```
![Start Nagios Service](https://www.tecmint.com/wp-content/uploads/2019/07/start-enable-and-view-nagios-status.png)Start Nagios Service
**13.** If you have firewall running, you need to open port **80** in the firewall.
```
# firewall-cmd --permanent --zone=public --add-port=80/tcp
# firewall-cmd --reload

```

14. Next disable **SELinux** which is in **enforcing mode** by default or you can set it in **permissive mode**.
```
# sed -i 's/SELINUX=.*/SELINUX=disabled/g' /etc/selinux/config
# setenforce 0

```

### Step 4: Accessing Nagios Web Console in RHEL 8
**15.** In this final step, you can now access the Nagios web console. Open your web browser and point it to Nagios Core web directory, for example (replace the IP address or FDQN with your own values).
```
http://192.168.56.100/nagios
OR
http://tecmint.lan/nagios

```

You will be prompted to enter a **username** and **password** to access the web interface. Provide the credentials you created in point 8 (i.e username is **nagiosadmin** and the password).
![Nagios Login](https://www.tecmint.com/wp-content/uploads/2019/07/access-nagios-web-console-login.png)Nagios Login
After a successful login, you will be presented with the Nagios interface as shown in the following screenshot.
![Nagios Web Console](https://www.tecmint.com/wp-content/uploads/2019/07/Nagios-web-console.png)Nagios Web Console
Congratulations! You have successfully installed **Nagios Core** on your **RHEL 8** server. If you have any questions, use the feedback form below to reach us.
**Read Also** :
  1. [How to Add Linux Host to Nagios Monitoring Server](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/)
  2. [How to Add Windows Host to Nagios Monitoring Server](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/)


Tags [nagios monitoring](https://www.tecmint.com/tag/nagios-monitoring/), [RHEL 8](https://www.tecmint.com/tag/rhel-8/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Fix “No route to host” SSH Error in Linux](https://www.tecmint.com/fix-no-route-to-host-ssh-error-in-linux/)
Next article:
[How to Install VNC Server on RHEL 8](https://www.tecmint.com/install-vnc-server-on-rhel-8/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-nagios-on-rhel-8/#respond)** or
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
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-nagios-on-rhel-8/#respond)
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
[Linux rmdir Command Examples for Beginners](https://www.tecmint.com/rmdir-command-examples/)
[20 mysqladmin Commands for MYSQL/MariaDB Database Administration](https://www.tecmint.com/mysqladmin-commands-for-database-administration-in-linux/)
[Let Sudo Insult You When You Enter Incorrect Password](https://www.tecmint.com/sudo-insult-when-enter-wrong-password/)
[How to Run a Linux Command Without Saving It in History](https://www.tecmint.com/run-linux-command-without-saving-in-history/)
[5 ‘stat’ Command Examples for Linux Newbies](https://www.tecmint.com/linux-stat-command-examples/)
[Woof – Easily Exchange Files Over a Local Network in Linux](https://www.tecmint.com/share-files-over-a-local-network-in-linux/)
## Linux Server Monitoring Tools
[BCC – Tracing Tools for Linux IO, Networking, Monitoring, and More](https://www.tecmint.com/bcc-best-linux-performance-monitoring-tools/)
[How to Create a Centralized Log Server with Rsyslog in CentOS/RHEL 7](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/)
[6 Useful Tools to Monitor MongoDB Performance](https://www.tecmint.com/monitor-mongodb-performance/)
[5 Modern VnStat PHP Replacements for Bandwidth Monitoring](https://www.tecmint.com/network-bandwidth-monitoring-tools/)
[How to Setup Central Logging Server with Rsyslog in Linux](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/)
[How to Monitor Node.js Applications Using PM2 Web Dashboard](https://www.tecmint.com/monitor-node-js-applications-using-pm2/)
## Learn Linux Tricks & Tips
[12 Useful Commands For Filtering Text for Effective File Operations in Linux](https://www.tecmint.com/linux-file-operations-commands/)
[Learn The Basics of How Linux I/O (Input/Output) Redirection Works](https://www.tecmint.com/linux-io-input-output-redirection-operators/)
[How to Find Out List of All Open Ports in Linux](https://www.tecmint.com/find-open-ports-in-linux/)
[12 Ways to Find User Account Info and Login Details in Linux](https://www.tecmint.com/check-user-in-linux/)
[5 Ways to Empty or Delete a Large File Content in Linux](https://www.tecmint.com/empty-delete-file-content-linux/)
[How to Set and Unset Local, User and System Wide Environment Variables in Linux](https://www.tecmint.com/set-unset-environment-variables-in-linux/)
## Best Linux Tools
[Top 5 Open-Source OCR Tools for Linux in 2025](https://www.tecmint.com/best-linux-ocr-tools/)
[6 Best Whiteboard Applications for Your Linux Systems](https://www.tecmint.com/linux-whiteboard-applications/)
[8 Best IRC Clients for Linux in 2024](https://www.tecmint.com/best-irc-clients-for-linux/)
[10 Best API Gateways and Management Tools in 2024](https://www.tecmint.com/open-source-api-gateways-and-management-tools/)
[5 Must-Try AI Tools for Linux Users in 2026](https://www.tecmint.com/ai-tools-for-linux/)
[6 Best Command-Line FTP Clients for Linux Users](https://www.tecmint.com/command-line-ftp-clients-for-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-nagios-on-rhel-8/ "Scroll back to top")
Search for:
