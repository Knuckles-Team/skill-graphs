[Skip to content](https://www.tecmint.com/install-zabbix-on-rhel-8/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-zabbix-on-rhel-8/)
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
  * [Pro Courses](https://www.tecmint.com/install-zabbix-on-rhel-8/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-zabbix-on-rhel-8/)
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
  * [Pro Courses](https://www.tecmint.com/install-zabbix-on-rhel-8/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-zabbix-on-rhel-8/)
# How to Install Zabbix on RHEL 8
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: August 27, 2019 Read Time: 6 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [RedHat](https://www.tecmint.com/category/redhat/), [Zabbix](https://www.tecmint.com/category/zabbix/) [1 Comment](https://www.tecmint.com/install-zabbix-on-rhel-8/#comments)
**Zabbix** is a free, open-source, enterprise-grade, fully-featured, flexible, extensible and distributed monitoring software, which is used to monitor an entire IT infrastructure, services, applications, and server resources. Zabbix is one of the most popular open-source monitoring solutions on the globe, that monitors various parameters of a computer network and the health and integrity of servers.
It is widely used for features such as a flexible notification mechanism that allows users to configure e-mail based alerts for virtually any event; this allows for fast reaction to server problems. It also features an excellent reporting and data visualization tool based on the stored data.
Importantly, all reports and statistics collected by Zabbix, plus configuration parameters, are accessed through a web-based frontend. This means you can monitor your systems from any location.
#### Requirements
Before we start, make sure that the following requirements have been satisfied:
  1. [RHEL 8 with Minimal Installation](https://www.tecmint.com/installation-of-rhel-8/)
  2. [RHEL 8 with RedHat Subscription Enabled](https://www.tecmint.com/enable-rhel-subscription-in-rhel-8/)
  3. [RHEL 8 with Static IP Address](https://www.tecmint.com/set-static-ip-address-in-rhel-8/)


This tutorial will focus on how to install latest version of **Zabbix 4.2** Server on **RHEL 8** with **MySQL/MariaDB** database to store data, **PHP** and **Apache Web Server** as the mainly web interface.
### Step 1: Installing Apache and PHP Packages
**1.** To begin with, you need to [enable the EPEL 8 repository](https://www.tecmint.com/install-epel-repo-on-rhel-8/) which contains some of the dependencies for **Zabbix**. Then install the Apache web server which is provided by the **HTTPD** package, **PHP** interpreter, **PHP-FPM** (**PHP FastCGI Process Manager**) and other required modules as follows.
```
# dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
# dnf install httpd php php-fpm php-mysqlnd php-ldap php-bcmath php-mbstring php-gd php-pdo php-xml

```

**2.** When the installation is complete, start the **HTTPD** and **PHP-FPM** services for now, then enable it to automatically start at system startup (after every reboot) and check if it is up and running as follows.
```
# systemctl start httpd
# systemctl enable httpd
# systemctl status httpd

# systemctl start php-fpm
# systemctl enable php-fpm
# systemctl status php-fpm

```

### Step 2: Install MariaDB Database and Library
Zabbix uses a **MySQL** database to store its data. However, on **RHEL 8** , **MariaDB** database is supported by default, as a drop-in replacement for **MySQL**.
**3.** To install **MariaDB** server, client and library packages use the following command.
```
# dnf install mariadb mariadb-server mariadb-devel

```

**4.** Next, start the **MariaDB** service for now, then enable it to automatically start at system startup and make sure that it is up and running by checking its status as shown.
```
# systemctl start mariadb
# systemctl enable mariadb
# systemctl status mariadb

```

**5.** Once the **MariaDB** database server is up and running, you need to secure it by running the `mysql_secure_installation` script, which helps you to implement some useful security recommendations such as removing anonymous users, disabling root login remotely, removing test database and access to it, and applying all changes.
```
# mysql_secure_installation

```

Then you will be prompted to determine which actions to perform as shown in the following screenshot.
![Secure MariaDB Server in RHEL 8](https://www.tecmint.com/wp-content/uploads/2019/01/Secure-MariaDB-Server-in-RHEL-8.png)Secure MariaDB Server in RHEL 8
**6.** Now log in to the database to gain access to the **MariaDB** shell to create a database for **Zabbix** as shown.
```
# mysql -uroot -p
**MariaDB [(none)]>** create database zabbix character set utf8 collate utf8_bin;
**MariaDB [(none)]>** grant all privileges on zabbix.* to zabbix@localhost identified by 'password';
**MariaDB [(none)]>** quit;

```

### Step 3: Installing and Configuring Zabbix Packages
**7.** Once everything installed, now its time to install the latest version of Zabbix packages from the **Zabbix Official Repository** as shown.
```
# rpm -Uvh https://repo.zabbix.com/zabbix/4.2/rhel/8/x86_64/zabbix-release-4.2-2.el8.noarch.rpm
# dnf clean all

```

**8.** Then install the Zabbix server, web frontend, agent packages with the following command.
```
# dnf -y install zabbix-server-mysql zabbix-web-mysql zabbix-agent

```

**9.** When the installation finishes, you need to import the initial schema and data into the Zabbix database which you created in the previous step (note that you will be prompted to enter the Zabbix database user’s password).
```
# zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -u zabbix -p zabbix

```

**10.** Now configure the Zabbix server daemon to use the database you created for it by editing the file **/etc/zabbix/zabbix_server.conf**.
```
# vim /etc/zabbix/zabbix_server.conf

```

Search and update the values of the following configuration options to reflect your database settings (uncomment options that are commented out and set their correct values) as follows.
```
DBHost=localhost
DBName=zabbix
DBUser=zabbix
DBPassword=database-passwod-here

```
![Configure Zabbix Database Settings](https://www.tecmint.com/wp-content/uploads/2019/08/configure-zabbix-database-settings.png)Configure Zabbix Database Settings
Save the changes in the file and close it.
**11.** Next, configure **PHP** for the **Zabbix** frontend by edtting the file **/etc/php-fpm.d/zabbix.conf** using your favorite text-based editor.
```
# vim /etc/php-fpm.d/zabbix.conf

```

Look for the following line and uncomment it (by removing the `“;”` character at the start of the line) to set the right timezone for your server.
```
php_value date.timezone Africa/Kampala

```

**12.** At this point you need to restart the **HTTPD** and **PHP-FPM** services to effect the recent changes before starting the Zabbix service.
```
# systemctl restart httpd php-fpm

```

**13.** Then start the **Zabbix** server and agent processes and enable them to auto-start at system boot as follows. Note that this agent is used on the localhost. To monitor remote servers, you need to install agents on them and configure the server to query them.
```
# systemctl start zabbix-server zabbix-agent
# systemctl enable zabbix-server zabbix-agent

```

Besides, check if the Zabbix server is up and running fine using the following command.
```
# systemctl status zabbix-server

```
![Check Zabbix Server Status](https://www.tecmint.com/wp-content/uploads/2019/08/check-zabbix-server-status.png)Check Zabbix Server Status
Also, ensure that the agent process is up and running.
```
# systemctl status zabbix-agent

```
![Check Zabbix Agent Status](https://www.tecmint.com/wp-content/uploads/2019/08/check-zabbix-agent-status.png)Check Zabbix Agent Status
### Step 4: Installing and Configuring Zabbix Web Frontend
**14.** With the Zabbix server up and running, open a web browser and point it to the following URL to access the web frontend installer.
```
http://SERVER_FQDM/zabbix
OR
http://SERVER_IP/zabbix

```

After pressing enter, you will be re-directed to the Welcome page as shown in the following screenshot. Click **Next** step to proceed.
![Zabbix Welcome Page](https://www.tecmint.com/wp-content/uploads/2019/08/zabbix-frontend-installer-welcome-page.png)Zabbix Welcome Page
**15.** Next, the installer will check of pre-requisites. If everything is **OK** (scroll down to view more requirements), click **Next** step to proceed.
![Check Zabbix Pre-requisites](https://www.tecmint.com/wp-content/uploads/2019/08/check-pre-requisites.png)Check Zabbix Pre-requisites
**16.** Then configure Zabbix database connection (note it is the database you created in Step 2 above). Select the database type, enter the database host, database port, database name and database user and the user’s password.
![Zabbix Database Settings](https://www.tecmint.com/wp-content/uploads/2019/08/configure-db-connection.png)Zabbix Database Settings
**17.** Next, provide the Zabbix server details (the hostname or host IP address and port number of the Zabbix server). You can also set a name for the installation which is optional. Click Next step to view the pre-installation summary.
![Zabbix Server Details](https://www.tecmint.com/wp-content/uploads/2019/08/provide-server-details.png)Zabbix Server Details
**18.** From the pre-installation summary page, click **Next** step to create the frontend configuration file, based on the information displayed.
![Zabbix Pre-Installation Summary](https://www.tecmint.com/wp-content/uploads/2019/08/pre-installation-summary.png)Zabbix Pre-Installation Summary
**19.** To complete the configuration and installation of the Zabbix frontend interface, click **Finish** and the installer will then re-direct you to the login page as shown in the next screenshot.
![Zabbix Frontend Installed](https://www.tecmint.com/wp-content/uploads/2019/08/zabbix-frontend-installed.png)Zabbix Frontend Installed
**20.** At the login page, use the username **Admin** and password `zabbix` to log in as shown in the following screenshot.
![Zabbix Frontend Login](https://www.tecmint.com/wp-content/uploads/2019/08/zabbix-web-frontend-login-page.png)Zabbix Frontend Login
**21.** After a successful log on, you will land at the Zabbix web frontend’s Monitoring Dashboard’s Global view which shows a sample of System information, local time and more.
![Zabbix Dashboard](https://www.tecmint.com/wp-content/uploads/2019/08/TecMint-Zabbix-Test-Dashboard.png)Zabbix Dashboard
**22.** Last but not least, secure the Zabbix super administrator account by changing the default password. Go to **Administration** , then **Users**. In the list of users, under **Alias** , click on **Admin** to open the user’s details for editing.
Under the user details, look for the **Password** field and click **Change password** , enter a secure password and confirm it. Then click on **Update** to save the admin account new password.
![Change Zabbix Admin Password](https://www.tecmint.com/wp-content/uploads/2019/08/update-web-frontend-admin-password.png)Change Zabbix Admin Password
**Congratulations!** You have successfully installed the latest version of Zabbix monitoring software on your **RHEL 8** server. If you have any queries, reach us via the feedback form below and for more information, see the
Tags [RHEL 8](https://www.tecmint.com/tag/rhel-8/), [RHEL Tips](https://www.tecmint.com/tag/rhel-tips/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install Free SSL Certificate for Nginx on Debian 10](https://www.tecmint.com/install-free-ssl-certificate-for-nginx-on-debian-10/)
Next article:
[How to Install PgAdmin 4 Debian 10](https://www.tecmint.com/install-pgadmin-debian-10/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-zabbix-on-rhel-8/#respond)** or
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
### 1 Comment
[Leave a Reply](https://www.tecmint.com/install-zabbix-on-rhel-8/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/dfc07d137d48ae767179c482f68666d4cc439a996f03f0ac69918afef0b49172?s=50&d=blank&r=g)
themetman
[ July 3, 2021 at 2:16 pm  ](https://www.tecmint.com/install-zabbix-on-rhel-8/#comment-1535831)
Step 3 Section 8 is incorrect. You have forgotten to install two items which are critical!
In particular the two modules **zabbix-apache-conf** and **zabbix-sql-scripts**.
So the next step will NOT work because there is no **create.sql.gz** file to upload to the database.
[Reply](https://www.tecmint.com/install-zabbix-on-rhel-8/#comment-1535831)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-zabbix-on-rhel-8/#respond)
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
[How to Start, Stop, and Restart Services in Linux](https://www.tecmint.com/systemd-service-commands/)
[How to Compress and Decompress a .bz2 File in Linux](https://www.tecmint.com/linux-compress-decompress-bz2-files-using-bzip2/)
[MultiCD – Create a MultiBoot Linux Live USB](https://www.tecmint.com/multicd-create-multiboot-linux-usb/)
[How to Switch (su) to Another User Account without Password](https://www.tecmint.com/switch-user-account-without-password/)
[Mhddfs – Combine Several Smaller Partition into One Large Virtual Storage](https://www.tecmint.com/combine-partitions-into-one-in-linux-using-mhddfs/)
[4 Ways to Batch Convert Your PNG to JPG and Vice-Versa](https://www.tecmint.com/linux-image-conversion-tools/)
## Linux Server Monitoring Tools
[Hegemon – A Modular System Monitoring Tool for Linux](https://www.tecmint.com/hegemon-system-monitoring-tool-for-linux/)
[4 Ways to Watch or Monitor Log Files in Real Time](https://www.tecmint.com/watch-or-monitor-linux-log-files-in-real-time/)
[How to Monitor Docker Containers with Zabbix Monitoring Tool](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/)
[How to Install Icinga2 Monitoring Tool on OpenSUSE](https://www.tecmint.com/install-icinga2-monitoring-opensuse/)
[Arpwatch – Monitor Ethernet Activity {IP and Mac Address} in Linux](https://www.tecmint.com/monitor-ethernet-activity-in-linux/)
[24 Best Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)
## Learn Linux Tricks & Tips
[How to Force User to Change Password at Next Login in Linux](https://www.tecmint.com/force-user-to-change-password-next-login-in-linux/)
[Easily Correct a Typo of Previous Command Using Carat (^) Symbol](https://www.tecmint.com/fix-correct-mistakes-typos-previous-command-in-linux/)
[How to Add or Remove Linux User From Group](https://www.tecmint.com/add-or-remove-user-from-group-in-linux/)
[Ternimal – Show Animated Lifeform in Your Linux Terminal](https://www.tecmint.com/ternimal-show-animated-lifeform-in-linux-terminal/)
[How to Switch (su) to Another User Account without Password](https://www.tecmint.com/switch-user-account-without-password/)
[5 Ways to Empty or Delete a Large File Content in Linux](https://www.tecmint.com/empty-delete-file-content-linux/)
## Best Linux Tools
[10 Best PuTTY Alternatives for SSH Remote Connection](https://www.tecmint.com/putty-alternatives/)
[4 Best QR Code Generator Tools for Linux](https://www.tecmint.com/qr-code-generator-for-linux/)
[Top 5 Open Source Collaboration Platforms for Linux in 2024](https://www.tecmint.com/open-source-collaboration-platforms-linux/)
[6 Best Linux Apps for Downloading Movie Subtitles](https://www.tecmint.com/best-linux-movie-subtitles-player-software/)
[16 Best Tools to Access Remote Linux Desktop](https://www.tecmint.com/best-remote-linux-desktop-sharing-software/)
[10 Best Flowchart and Diagramming Software for Linux](https://www.tecmint.com/best-flowchart-and-diagramming-software-for-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-zabbix-on-rhel-8/ "Scroll back to top")
Search for:
