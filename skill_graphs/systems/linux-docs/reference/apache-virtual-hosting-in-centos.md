[Skip to content](https://www.tecmint.com/install-zabbix-on-debian-10/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-zabbix-on-debian-10/)
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
  * [Pro Courses](https://www.tecmint.com/install-zabbix-on-debian-10/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-zabbix-on-debian-10/)
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
  * [Pro Courses](https://www.tecmint.com/install-zabbix-on-debian-10/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-zabbix-on-debian-10/)
# How to Install Zabbix Monitoring Tool on Debian 11/10
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: October 27, 2021 Read Time: 6 minsCategories [Debian](https://www.tecmint.com/category/debian/), [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [Zabbix](https://www.tecmint.com/category/zabbix/) [16 Comments](https://www.tecmint.com/install-zabbix-on-debian-10/#comments)
**Zabbix** is a free, open-source, popular, and feature-rich IT infrastructure monitoring software developed using PHP language. It is used to monitor networks, servers, applications, services as well as cloud resources. It also supports the monitoring of storage devices, databases, virtual machines, telephony, IT security resources, and much more.
**[ You might also like:[How to Install Zabbix on RHEL 8](https://www.tecmint.com/install-zabbix-on-rhel-8/ "How to Install Zabbix on RHEL 8") ]**
For developers, **Zabbix** ships with an **API** that provides access to almost all functions available in Zabbix. It supports easy two-way integration with any software. You can also use the API to integrate Zabbix functions into third-party software.
#### Requirements
  * [How to Install Debian 11 (Bullseye) Minimal Server](https://www.tecmint.com/install-debian-11-minimal-server/ "How to Install Debian 11 \(Bullseye\) Minimal Server")
  * [How to Install a Debian 10 (Buster) Minimal Server](https://www.tecmint.com/install-debian-10-minimal-server/ "How to Install a Debian 10 \(Buster\) Minimal Server")


This tutorial shows how to install and configure the latest release of **Zabbix** open-source monitoring tool on **Debian 11** and **Debian 10** with **MySQL** database to keep data, **PHP,** and **Apache Web Server** as the main web interface.
### Step 1: Installing Apache Web Server and PHP Packages
**1.** To install **Zabbix** , first, you need to install **Apache** and **PHP** along with some required PHP modules as follows.
```
# apt install apache2 php php-mysql php-mysqlnd php-ldap php-bcmath php-mbstring php-gd php-pdo php-xml libapache2-mod-php

```

**2.** In the installation process, the installer triggers the **systemd** to automatically start **Apache** service, and it also enables it to automatically start at system boot. You can check if it is up and running using the [systemctl command](https://www.tecmint.com/manage-services-using-systemd-and-systemctl-in-linux/).
```
# systemctl status apache2

```
![Check Apache Status in Debian](https://www.tecmint.com/wp-content/uploads/2019/09/Check-Apache-Status-in-Debian.png)Check Apache Status in Debian
The following are some useful [systemctl commands](https://www.tecmint.com/manage-apache-web-server-in-linux/) for managing the **Apache** services under **systemd**.
```
# systemctl start apache2
# systemctl stop apache2
# systemctl restart apache2

```

### Step 2: Install MariaDB Server and Client
**3.** To store data, **Zabbix** requires a database management system. It supports **MySQL** by default but for this guide, we will install **MariaDB** as a drop-in replacement for **MySQL**.
```
# apt install mariadb-server mariadb-client

```

**4.** When the installation is complete, the **MariaDB** service is auto-started and enabled to automatically start at system startup. To check if it is up and running, use the following command.
```
# systemctl status mariadb

```
![Check MariaDB Status in Debian](https://www.tecmint.com/wp-content/uploads/2019/09/check-mariadb-service-status.png)Check MariaDB Status in Debian
**5.** Next, you need to secure your **MariaDB** server database installation. The installed package ships with a script that you need to run and follow the security recommendations.
```
# mysql_secure_installation

```

It will ask you to determine actions to remove anonymous users, disable root login remotely, remove test database and access to it, and apply all changes.
![Secure MariaDB in Debian 10](https://www.tecmint.com/wp-content/uploads/2019/08/Secure-MariaDB-in-Debian-10.png)Secure MariaDB in Debian 10
**6.** Once the database server is secured, you need to create a database for Zabbix. First, log in to the database to gain access to the MariaDB shell as follows.
```
# mysql -u root -p

```

**7.** Then issues the following SQL commands to create the required database (do not forget to set a secure password).
```
**MariaDB [(none)]>** create database zabbix character set utf8 collate utf8_bin;
**MariaDB [(none)]>** grant all privileges on zabbix.* to zabbix@localhost identified by 'admin@monit1';
**MariaDB [(none)]>** quit;

```

### Step 3: Installing and Configuring Zabbix Server
**8.** To install **Zabbix** , you need to enable the **Zabbix Official Repository** which contains the Zabbix packages, as follows.
```
# wget --no-check-certificate https://repo.zabbix.com/zabbix/5.4/debian/pool/main/z/zabbix-release/zabbix-release_5.4-1+debian11_all.deb
# dpkg -i zabbix-release_5.4-1+debian11_all.deb
# apt update

```

**9.** Now install the Zabbix server, web frontend, agent packages using the following command.
```
# apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent

```

**10.** If the package installation is successful, next, import the initial schema and data into the Zabbix database which you created in the previous step.
```
# zcat /usr/share/doc/zabbix-sql-scripts/mysql/create.sql.gz | mysql -uzabbix -p zabbix

```

**11.** Next, configure the Zabbix server daemon to use the database you created for it by editing the file **/etc/zabbix/zabbix_server.conf**.
```
# vim /etc/zabbix/zabbix_server.conf

```

Look for the following configuration options and update their values to reflect your database settings. Note that you need to uncomment any option(s) that are commented out and set their correct values.
```
DBHost=localhost
DBName=zabbix
DBUser=zabbix
DBPassword=admin@monit1

```
![Configure Zabbix Database Settings](https://www.tecmint.com/wp-content/uploads/2019/08/configure-zabbix-database-settings.png)Configure Zabbix Database Settings
Then save the new changes in the file and exit it.
**12.** You should also set up PHP to work correctly with the Zabbix frontend by defining your timezone in the **/etc/zabbix/apache.conf** file.
```
# vim /etc/zabbix/apache.conf

```

Find the configuration section for your PHP version, for example, **PHP 7.x**. Then uncomment the following line (by removing the `“#”` character at the start) to enable timezone for your server as shown in the screenshot.
```
php_value date.timezone Africa/Kampala

```
![Configure PHP Timezone](https://www.tecmint.com/wp-content/uploads/2019/09/configure-php-timezone-for-zabbix-frontend.png)Configure PHP Timezone
Save the changes and close the file.
**13.** Now restart the Apache server to apply recent changes.
```
# systemctl restart apache2

```

**14.** With all the perfect environment setup, you can now start the Zabbix server and agent processes, enabling them to auto-start at system boot as shown.
```
# systemctl start zabbix-server zabbix-agent
# systemctl enable zabbix-server zabbix-agent

```
![Start Zabbix Server and Agent](https://www.tecmint.com/wp-content/uploads/2019/09/start-and-enable-zabbix-server-and-zabbix-agent-services.png)Start Zabbix Server and Agent
**15.** Then make sure to check the status of the Zabbix server using the following command.
```
# systemctl status zabbix-server

```
![Check Zabbix Status](https://www.tecmint.com/wp-content/uploads/2019/09/check-zabbix-server-service-status.png)Check Zabbix Status
**16.** Also, ensure that the Zabbix agent process is up and running by checking its status as shown. Remember the agent you have started is running on and monitoring the local host. If you want to monitor remote servers, install and configure agents on them (refer to related articles at the end of the guide).
```
# systemctl status zabbix-agent

```
![Check Zabbix Agent Status](https://www.tecmint.com/wp-content/uploads/2019/09/check-zabbix-agent-service-status.png)Check Zabbix Agent Status
**17.** Before you can access the Zabbix web frontend as shown in the next section if you have the [UFW firewall service running](https://www.tecmint.com/setup-ufw-firewall-on-ubuntu-and-debian/), you need to open port **80(HTTP)** and **443(HTTPS)** to allow traffic to the Apache server.
```
# ufw allow 80/tcp
# ufw allow 443/tcp
# ufw reload

```

### Step 4: Installing and Configuring Zabbix Web Frontend Interface
**18.** Before you can start using the Zabbix web frontend for monitoring, you need to configure and set it up via a web installer. To access the installer, open a web browser and point it to the following URL.
```
http://SERVER_FQDM/zabbix
OR
http://SERVER_IP/zabbix

```

**19.** Once you click go, or press **Enter** , you will land on the Welcome page as shown in the following screenshot. Click **Next** step to start the setup process.
![Zabbix Web Installer](https://www.tecmint.com/wp-content/uploads/2021/10/Zabbix-Web-Installer.png)Zabbix Web Installer
**20.** The installer will then check the pre-requisites as shown in the screenshot, if all required PHP modules and configuration options are OK (scroll down to view more requirements), click Next step to proceed.
![Zabbix Checks Pre-requisites](https://www.tecmint.com/wp-content/uploads/2021/10/Zabbix-Checks-pre-requisites.png)Zabbix Checks Pre-requisites
**21.** Next, enter the database connection settings for the Zabbix frontend to link to the database. Choose the database type (which should be MySQL), provide the database host, database port, database name, and database user, and the user’s password as shown in the screenshot.
![Zabbix Database Settings](https://www.tecmint.com/wp-content/uploads/2021/10/Zabbix-Database-Settings.png)Zabbix Database Settings
**22.** Next, enter the Zabbix server details (hostname or host IP address and port number of the hosting server). Optionally, set a name for the installation.
![Zabbix- Server Details](https://www.tecmint.com/wp-content/uploads/2021/10/Zabbix-Server-Details.png)Zabbix- Server Details
**23.** Now the installer should show you the pre-installation summary page. If all is fine, click Next step to complete the setup.
![Zabbix Pre-installation Summary](https://www.tecmint.com/wp-content/uploads/2021/10/Zabbix-Pre-installation-Summary.png)Zabbix Pre-installation Summary
**24.** Now click Finish, and you should be re-directed to the login page as shown in the next screenshot.
![Zabbix Installation Complete](https://www.tecmint.com/wp-content/uploads/2021/10/Zabbix-Installation-Complete.png)Zabbix Installation Complete
**25.** To login, enter the username **Admin** and password **zabbix**.
![Zabbix Login](https://www.tecmint.com/wp-content/uploads/2021/10/Zabbix-Login.png)Zabbix Login
**26.** Once you have logged on, you will see the Monitoring section Dashboard. The Global view will display a sample of System information, problems by severity, problems, local time, and more, as shown in the screenshot.
![Zabbix Dashboard](https://www.tecmint.com/wp-content/uploads/2021/10/Zabbix-Dashboard.png)Zabbix Dashboard
**27.** As an important step, you need to change the default administrator account password. To do that, go to **Administration** ==> **Users**.
From the list of users, under **Alias** , click on **Admin** to open the user’s details. In the user details page, look for the **Password** field and click Change password. Then set a secure password and confirm it. And click **Update** to save the password.
![Change Zabbix Admin Password](https://www.tecmint.com/wp-content/uploads/2021/10/Zabbix-Admin-Password-Change.png)Change Zabbix Admin Password
You might also like to read the following related Zabbix articles.
  * [How to Configure ‘Zabbix Monitoring’ to Send Email Alerts to Gmail Account](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/)
  * [How to Install and Configure Zabbix Agents on Remote Linux Systems](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/)
  * [How to Install Zabbix Agent and Add Windows Host to Zabbix Monitoring](https://www.tecmint.com/install-zabbix-agent-and-add-windows-host-to-zabbix-monioring/)


That’s all! In this article, we’ve learned how to the latest version of Zabbix monitoring software on your **Debian 11/10** server. You can find more information in the
Tags [Debian Tips](https://www.tecmint.com/tag/debian-tips/), [linux server monitoring](https://www.tecmint.com/tag/linux-server-monitoring/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Beautify Dynamic HTML5 Web App Using Online Tools](https://www.tecmint.com/beautify-website-using-fontawesome-and-tools/)
Next article:
[How to Create File-Sharing with ONLYOFFICE Docs and Seafile](https://www.tecmint.com/create-file-sharing-onlyoffice-docs-seafile/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-zabbix-on-debian-10/#respond)** or
## Related Posts
[![Fix “404 Not Found” Errors in Debian apt Update](https://www.tecmint.com/wp-content/uploads/2025/11/fix-apt-get-404-errors-debian.webp)](https://www.tecmint.com/fix-apt-get-404-errors-debian/ "How to Fix “404 Not Found” Errors in Debian During apt-get upgrade")
[How to Fix “404 Not Found” Errors in Debian During apt-get upgrade](https://www.tecmint.com/fix-apt-get-404-errors-debian/)
[![manage software in Debian using dpkg, apt, aptitude, Synaptic, and tasksel](https://www.tecmint.com/wp-content/uploads/2014/08/debian-dpkg-apt-aptitude-synaptic-tasksel.webp)](https://www.tecmint.com/debian-dpkg-apt-aptitude-synaptic-tasksel/ "How to Use dpkg, apt, aptitude, synaptic, and tasksel in Debian")
[How to Use dpkg, apt, aptitude, synaptic, and tasksel in Debian](https://www.tecmint.com/debian-dpkg-apt-aptitude-synaptic-tasksel/)
[![ufw setup ubuntu](https://www.tecmint.com/wp-content/uploads/2013/12/ufw-setup-ubuntu.webp)](https://www.tecmint.com/install-ufw-on-ubuntu-debian/ "UFW Firewall: How to Install, Configure, and Use It on Ubuntu/Debian")
[UFW Firewall: How to Install, Configure, and Use It on Ubuntu/Debian](https://www.tecmint.com/install-ufw-on-ubuntu-debian/)
[![Install ProtonVPN on Debian](https://www.tecmint.com/wp-content/uploads/2025/02/Install-ProtonVPN-on-Debian.webp)](https://www.tecmint.com/install-protonvpn-debian/ "How to Set Up ProtonVPN on Debian 12")
[How to Set Up ProtonVPN on Debian 12](https://www.tecmint.com/install-protonvpn-debian/)
[![Installing Nvidia Drivers on Debian](https://www.tecmint.com/wp-content/uploads/2025/02/Installing-Nvidia-Drivers-on-Debian.webp)](https://www.tecmint.com/install-nvidia-drivers-debian/ "Installing Nvidia Graphics Drivers on Debian 12")
[Installing Nvidia Graphics Drivers on Debian 12](https://www.tecmint.com/install-nvidia-drivers-debian/)
[![Auto Mount USB Drive in Linux](https://www.tecmint.com/wp-content/uploads/2025/01/auto-mount-usb-drive-linux.png)](https://www.tecmint.com/mount-usb-drive-on-linux-startup/ "How to Mount a USB Drive Every Time Linux Boots Up")
[How to Mount a USB Drive Every Time Linux Boots Up](https://www.tecmint.com/mount-usb-drive-on-linux-startup/)
### 16 Comments
[Leave a Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/8aae3a678cfe99883aeb5d9a3138de538b7ec4198af8527c4538c5a5bedfbb13?s=50&d=blank&r=g)
panos
[ December 17, 2021 at 12:53 am  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1679541)
Hello,
Can’t install zabbix-apache-conf and zabbix-sql-scripts.
What am I doing wrong?
Thank you
Panos
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1679541)
  2. ![](https://secure.gravatar.com/avatar/cbedbb4b3e1bdee8ae7c5cca69f0474848b6790a71bd19c013e248c1efb8382f?s=50&d=blank&r=g)
Samuel Melton
[ June 23, 2021 at 2:01 am  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1526220)
Can you explain step 7: “(do not forget to set a secure password).”?
Am I supposed to set a secure password for the database or for a “zabbix@localhost” user? I’m not at all familiar with this CLI so I’m not sure what’s happening here.
What’s the syntax for setting this password?
Thanks
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1526220)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 23, 2021 at 11:55 am  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1526657)
@Samuel,
Replace the `admin@monit1` with your own secure password this is what I mean in step 7.
```
MariaDB [(none)]> grant all privileges on zabbix.* to zabbix@localhost identified by 'admin@monit1';

```
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1526657)
  3. ![](https://secure.gravatar.com/avatar/3550d0e2964966566d59d4d6d404004c6bd0c0a2112251245657717c80d9db82?s=50&d=blank&r=g)
student
[ May 5, 2021 at 2:57 am  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1485731)
Hi, thank you a lot for sharing this…
I have one problem I’m trying to start Zabbix-server it’s not starting i did all the steps and when it comes to starting the Zabbix server it’s not working any suggestions?
Please thank you in advance…
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1485731)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 5, 2021 at 10:16 am  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1485851)
@Student,
Could you share what error you getting while starting the Zabbix server?
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1485851)
       * ![](https://secure.gravatar.com/avatar/3550d0e2964966566d59d4d6d404004c6bd0c0a2112251245657717c80d9db82?s=50&d=blank&r=g)
student
[ May 5, 2021 at 3:38 pm  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1485953)
Hi, I don’t get any error it just doesn’t start, the problem is only in starting the server ( apache2 and zabbix-agent they are active ).
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1485953)
  4. ![](https://secure.gravatar.com/avatar/ffd2fd817d8ea774b0c8d0819bb02803b7d91cce10a1dda2b0b2170ce1bcf03d?s=50&d=blank&r=g)
clement
[ October 27, 2020 at 9:37 pm  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1381750)
Thanks a lot. On step 15 you should replace “**start** ” by “**status** ” in the command line.
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1381750)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 28, 2020 at 11:00 am  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1382076)
@Clement,
Thanks for updating us, I have corrected the command as suggested…
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1382076)
  5. ![](https://secure.gravatar.com/avatar/b529752e4fb11fc6c41d5a24086e537321cc4d3ffb065344e1edbf6c6d49b47c?s=50&d=blank&r=g)
M Innes
[ May 20, 2020 at 3:52 pm  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1334531)
There is a bug in the MariaDB on Debian 10 which means the database import does not work;
ERROR 1118 (42000) at line 1278: Row size too large (> 8126). Changing some columns to TEXT or BLOB may help. In the current row format, the BLOB prefix of 0 bytes is stored inline.
After some research i found this worked in my.cnf
```
innodb_strict_mode = 0
innodb_log_buffer_size = 32M

```

Remove innodb_strict_mode = 0 after import.
If import already failed you will need to drop and recreate DB
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1334531)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ May 21, 2020 at 12:12 pm  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1334629)
@M
Many thanks for sharing this.
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1334629)
     * ![](https://secure.gravatar.com/avatar/2afb029eec828c5a13a65b256989c1b576b9e3afef35b2bf3971dc0287f66102?s=50&d=blank&r=g)
Daniel
[ July 28, 2020 at 4:36 pm  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1348387)
Thank you so much!
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1348387)
  6. ![](https://secure.gravatar.com/avatar/3de2594a279b8bc1ce2ed6062ffa4634d9616aae6986c87087f8993695f5e445?s=50&d=blank&r=g)
marc
[ April 25, 2020 at 12:35 am  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1329583)
```
# zcat /usr/share/doc/zabbix-server-mysql/create.sql.gz | mysql -u zabbix -p zabbix

```

ERROR 1045 (28000): Access denied for user ‘zabbix’@’localhost’ (using password: YES)
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1329583)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ April 27, 2020 at 12:06 pm  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1330393)
@marc
Try to use the password you created for the zabbix database user in step 7, instead of zabbix.
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1330393)
     * ![](https://secure.gravatar.com/avatar/8ec856904933b6f84b2d042330261171195e3e3585cafb9492ea15b4ee02efe7?s=50&d=blank&r=g)
Eder Pardeiro
[ January 18, 2021 at 6:59 am  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1417407)
Same error here…
ERROR 1045 (28000): Access denied for user ‘zabbix’@’localhost’ (using password: YES)
I’m using the same password in step 7, but not work…
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1417407)
       * ![](https://secure.gravatar.com/avatar/8ec856904933b6f84b2d042330261171195e3e3585cafb9492ea15b4ee02efe7?s=50&d=blank&r=g)
Eder Pardeiro
[ January 18, 2021 at 7:15 am  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1417412)
Now it’s work, but the error below appears:
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1417412)
         * ![](https://secure.gravatar.com/avatar/8ec856904933b6f84b2d042330261171195e3e3585cafb9492ea15b4ee02efe7?s=50&d=blank&r=g)
Eder Pardeiro
[ January 18, 2021 at 7:15 am  ](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1417413)
ERROR 1118 (42000) at line 1284: Row size too large (> 8126). Changing some columns to TEXT or BLOB may help. In the current row format, the BLOB prefix of 0 bytes is stored inline.
[Reply](https://www.tecmint.com/install-zabbix-on-debian-10/#comment-1417413)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-zabbix-on-debian-10/#respond)
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
[How to Watch TCP and UDP Ports in Real-time](https://www.tecmint.com/watch-tcp-and-udp-ports-in-linux/)
[Assign Read/Write Access to a User on Specific Directory in Linux](https://www.tecmint.com/give-read-write-access-to-directory-in-linux/)
[4 Useful Tools to Monitor CPU and GPU Temperature in Ubuntu](https://www.tecmint.com/monitor-cpu-and-gpu-temperature-in-ubuntu/)
[35 Practical Examples of Linux Find Command](https://www.tecmint.com/35-practical-examples-of-linux-find-command/)
[How to Add Text to Existing Files in Linux](https://www.tecmint.com/append-lines-to-file-linux/)
[How to Use ‘lsof’ Command to Check Open Files in Linux](https://www.tecmint.com/10-lsof-command-examples-in-linux/)
## Linux Server Monitoring Tools
[CBM – Shows Network Bandwidth in Ubuntu](https://www.tecmint.com/cbm-shows-network-bandwidth-traffic-in-ubuntu/)
[How to Monitor Ubuntu Performance Using Netdata](https://www.tecmint.com/monitor-ubuntu-performance-using-netdata/)
[How to Monitor Website and Application with Uptime Kuma](https://www.tecmint.com/uptime-kuma-linux-website-monitoring-tool/)
[How To Install and Connect an Agent to Pandora FMS Server](https://www.tecmint.com/install-and-connect-an-agent-to-pandora-fms-server/)
[Suricata – A Intrusion Detection, Prevention, and Security Tool](https://www.tecmint.com/suricata-intrusion-detection-prevention-linux/)
[How to Monitor Linux Server Security with Osquery](https://www.tecmint.com/monitor-linux-server-security-with-osquery/)
## Learn Linux Tricks & Tips
[Learn How to Set Your $PATH Variables Permanently in Linux](https://www.tecmint.com/set-path-variable-linux-permanently/)
[How to Create Multiple User Accounts in Linux](https://www.tecmint.com/create-multiple-user-accounts-in-linux/)
[How to Create a Shared Directory for All Users in Linux](https://www.tecmint.com/create-a-shared-directory-in-linux/)
[4 Ways to Batch Convert Your PNG to JPG and Vice-Versa](https://www.tecmint.com/linux-image-conversion-tools/)
[How to Delete HUGE (100-200GB) Files in Linux](https://www.tecmint.com/delete-huge-files-in-linux/)
[10 Useful Sudoers Configurations for Setting ‘sudo’ in Linux](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/)
## Best Linux Tools
[15 Best Kali Linux Web Penetration Testing Tools](https://www.tecmint.com/kali-linux-web-penetration-testing-tools/)
[Top 5 Open-Source Productivity Tools for Linux](https://www.tecmint.com/open-source-productivity-tools-linux/)
[8 Best PowerPoint Alternatives for Linux](https://www.tecmint.com/powerpoint-alternatives-for-linux/)
[Top 5 Open Source Collaboration Platforms for Linux in 2024](https://www.tecmint.com/open-source-collaboration-platforms-linux/)
[32 Best File Managers and Explorers [GUI + CLI] for Linux in 2024](https://www.tecmint.com/linux-file-managers/)
[6 Best Command-Line FTP Clients for Linux Users](https://www.tecmint.com/command-line-ftp-clients-for-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-zabbix-on-debian-10/ "Scroll back to top")
Search for:
