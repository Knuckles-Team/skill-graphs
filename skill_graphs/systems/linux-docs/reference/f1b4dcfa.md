# How to Install Zabbix on RHEL/CentOS and Debian/Ubuntu – Part 1
[Matei Cezar](https://www.tecmint.com/author/cezarmatei/ "View all posts by Matei Cezar")Last Updated: October 28, 2021 Read Time: 8 minsCategories [CentOS](https://www.tecmint.com/category/linux-distros/centos/), [Debian](https://www.tecmint.com/category/debian/), [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [RedHat](https://www.tecmint.com/category/redhat/), [Ubuntu](https://www.tecmint.com/category/linux-distros/ubuntu/), [Zabbix](https://www.tecmint.com/category/zabbix/) [93 Comments](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comments)
**Zabbix** is an Open Source, high-level enterprise software designed to monitor and keep track of networks, servers, and applications in real-time. Build in a server-client model, Zabbix can collect different types of data that are used to create historical graphics and output performance or load trends of the monitored targets.
The server has the ability to check standard networking services (**HTTP** , **FTP** , **SMTP** , **IMAP,** etc) without the need to install extra software on the monitored hosts.
However, in order to gather data and create statistics about local services or other specific system resources that run on remote instances, such as CPU, disks, internal system process, RAM, etc, you need to install and configure a Zabbix agent.
Following are the 4-article series about the **Zabbix Monitoring** application:
**Part 1** : **Install Zabbix on Debian/Ubuntu and RHEL/CentOS/Fedora/Rocky Linux/AlmaLinux**
**Part 2** : [How to Configure ‘Zabbix Monitoring’ to Send Email Alerts to Gmail Account](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/)
**Part 3** : [How to Install and Configure Zabbix Agents on Remote Linux Systems](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/)
**Part 4** : [How to Install Zabbix Agent and Add Windows Host to Zabbix Monitoring](https://www.tecmint.com/install-zabbix-agent-and-add-windows-host-to-zabbix-monioring/)
This tutorial will focus on how to install the latest version of the **Zabbix Server** on **Debian/Ubuntu** and **RHEL** /**CentOS** /**Fedora** /**Rocky Linux** /**AlmaLinux** with **MySQL/MariaDB** backend database to store collected data, **PHP** and **Apache Web Server** as the mainly web interface.
**Important:** The given Zabbix instructions also work on all [Debian derivatives](https://www.tecmint.com/debian-based-linux-distributions/ "Best Debian-based Linux Distributions") and [RedHat-based distros](https://www.tecmint.com/redhat-based-linux-distributions/ "The Best RedHat-based Linux Distributions") like **RHEL** /**CentOS** /**Fedora** and **Rocky Linux** /**AlmaLinux**.
### Step 1: Install Apache Web Server and PHP
**1.** First, update the software packages and then install **Apache Web Server** alongside **PHP** and its extensions in order to provide the web-backed functionality for Zabbix Server by issuing the following command.
```
**--------------- On Debian/Ubuntu ---------------**
$ sudo apt update && sudo apt upgrade
$ sudo apt install apache2 php php-mysql php-mysqlnd php-ldap php-bcmath php-mbstring php-gd php-pdo php-xml libapache2-mod-php

**--------------- On RHEL-based Distros ---------------**
# yum update && yum upgrade
# yum -y install epel-release
# yum install httpd php php-mysqlnd php-ldap php-bcmath php-mbstring php-gd php-xml

```

**2.** Next, you need to tune the PHP interpreter and adjust some values in order to run Zabbix Server. So, open Apache `php.ini` configuration file for editing by issuing the following command:
```
$ sudo nano /etc/php/7.X/apache2/php.ini 	[On **Debian/Ubuntu**]
# vi /etc/php.ini				[On **RHEL/CentOS/**]

```

Now, search with **CTRL+C** and replace the following PHP values as it follows:
```
post_max_size = 16M
upload_max_filesize = 2M
max_execution_time 300
max_input_time = 300
memory_limit 128M
session.auto_start = 0
mbstring.func_overload = 0
date.timezone = Europe/Bucharest

```

Replace the **date.timezone** variable according to your server’s geographical location. A list of PHP-supported Timezones can be found here
**3.** After updating the PHP configuration file, restart Apache daemon to reflect changes by issuing the following command.
```
$ sudo systemctl restart apache2.service	 [On **Debian/Ubuntu**]
# systemctl restart httpd.service		 [On **RHEL/CentOS**]

```

### Step 2: Install MariaDB Database and Library
**4.** On the next step install the MariaDB database and MySQL development library from binary packages. As MariaDB installs on your system you will be asked to set a password for the database root user during installation (Only on **Debian**). Choose a strong password, repeat it and wait for the installation to finish.
```
$ sudo apt-get install mariadb-server mariadb-client libmysqld-dev	 [On **Debian/Ubuntu**]
# yum install mariadb-server mariadb-client mariadb-devel	         [On **RHEL/CentOS**]

```
![Set MySQL root Password](https://www.tecmint.com/wp-content/uploads/2015/07/Set-MySQL-root-Password-620x191.png) Set MySQL root Password
**5.** When the installation of **Mariadb** finishes, start and secure the database by issuing **mysql_secure_installation** command with system root privileges ( answer with **yes** for removing anonymous users, disable root login remotely, remove test database and access to it and apply all changes).
```
$ sudo systemctl start mariadb
$ sudo mysql_secure_installation
OR
# systemctl start mariadb
# mysql_secure_installation

```

Use the below screenshot as a guide.
![Secure MySQL Installation](https://www.tecmint.com/wp-content/uploads/2015/07/Secure-MySQL-Installation.png)
**6.** The next requirement for Zabbix is setting up an RDBMS database. Log in to your LAMP stack database component (MySQL or MariaDB) and create a Zabbix database and the credentials required to manage the database, by issuing the following commands.
Make sure you replace the database name, user, and password to match your own settings.
```
# mysql -u root -p
**MariaDB [(none)]>** create database zabbixdb character set utf8 collate utf8_bin;
**MariaDB [(none)]>** grant all privileges on zabbixdb.* to 'zabbixuser'@'localhost' identified by 'password1';
**MariaDB [(none)]>** flush privileges;
**MariaDB [(none)]>** exit

```

### Step 3: Install Zabbix Server
**7.** Now, start to install the Zabbix server and Zabbix PHP frontend application by adding the official Zabbix repositories to your system package manager by issuing the following commands with root privileges.
#### Install Zabbix on Debian
```
**--------------- On Debian 11 ---------------**
$ sudo wget https://repo.zabbix.com/zabbix/5.4/debian/pool/main/z/zabbix-release/zabbix-release_5.4-1+debian11_all.deb
$ sudo dpkg -i zabbix-release_5.4-1+debian11_all.deb
$ sudo apt update
$ sudo apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent

**--------------- On Debian 10 ---------------**
$ sudo wget https://repo.zabbix.com/zabbix/5.4/debian/pool/main/z/zabbix-release/zabbix-release_5.4-1+debian10_all.deb
$ sudo dpkg -i zabbix-release_5.4-1+debian10_all.deb
$ sudo apt update
$ sudo apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent

```

#### Install Zabbix on Ubuntu
```
**--------------- On Ubuntu 20.04 ---------------**
$ sudo wget https://repo.zabbix.com/zabbix/5.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.4-1+ubuntu20.04_all.deb
$ sudo dpkg -i zabbix-release_5.4-1+ubuntu20.04_all.deb
$ sudo apt update
$ sudo apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent

**--------------- On Ubuntu 18.04 ---------------**
$ sudo wget https://repo.zabbix.com/zabbix/5.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.4-1+ubuntu18.04_all.deb
$ sudo dpkg -i zabbix-release_5.4-1+ubuntu18.04_all.deb
$ sudo apt update
$ sudo apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent

```

#### Install Zabbix on RHEL-based Distros
```
**--------------- On RHEL/CentOS 8 ---------------**
# rpm -Uvh https://repo.zabbix.com/zabbix/5.4/rhel/8/x86_64/zabbix-release-5.4-1.el8.noarch.rpm
# dnf clean all
# dnf install zabbix-server-mysql zabbix-web-mysql zabbix-apache-conf zabbix-sql-scripts zabbix-agent

**--------------- On RHEL/CentOS 7 ---------------**
# rpm -Uvh https://repo.zabbix.com/zabbix/5.4/rhel/7/x86_64/zabbix-release-5.4-1.el7.noarch.rpm
# dnf clean all
# dnf install zabbix-server-mysql zabbix-web-mysql zabbix-apache-conf zabbix-sql-scripts zabbix-agent

```

If you want to download and compile an older version, please visit Zabbix official
**8.** On the next step, restart the Apache HTTP server in order to apply the Zabbix configuration file installed for Apache.
```
$ sudo systemctl restart apache2   [On **Debian/Ubuntu**]
# systemctl restart httpd     [On **RHEL/CentOS**]
# setenforce 0                [Disable SELinux on **RHEL/CentOS**]

```

### Step 4: Configure Zabbix Server and Agent
**9.** Before configuring the server, first, import Zabbix’s initial database schema to the MySQL database. Import the schema against the database created for the Zabbix application, by issuing the below command.
```
$ sudo zcat /usr/share/doc/zabbix-sql-scripts/mysql/create.sql.gz | mysql -u zabbixuser zabbixdb -p
OR
# zcat /usr/share/doc/zabbix-sql-scripts/mysql/create.sql.gz | mysql -u zabbixuser zabbixdb -p

```

**10.** On the next step, set up the Zabbix server by opening the main configuration file for editing with the following command.
```
$ sudo nano /etc/zabbix/zabbix_server.conf
OR
# nano /etc/zabbix/zabbix_server.conf

```

In **zabbix_server.conf** file search and modify the following lines as presented in the below excerpt. Update the variables to reflect your own database settings.
```
DBHost=localhost
DBName=zabbixdb
DBUser=zabbixuser
DBPassword=password1

```

**11.** Finally, save and close the Zabbix server configuration file by pressing **Ctrl+o** and **Ctrl+x** file and restarting the Zabbix daemon to apply changes by issuing the below command.
```
# systemctl restart zabbix-server.service

```

**12.** Next, configure the Zabbix Agent configuration file by updating the following lines. First, open the file for editing.
```
# nano /etc/zabbix/zabbix_agentd.conf

```

Zabbix agent configuration file excerpt:
```
Server=127.0.0.1
ListenPort=10050

```

**13.** Save and close the Zabbix agent configuration file and restart Zabbix Agent to reflect changes by issuing the following command.
```
# systemctl restart zabbix-agent.service

```

### Step 5: Install and Configure Zabbix Frontend Interface
**15.** Now it’s time to install the **Zabbix Server Frontend** web interface. In order to accomplish this step open a browser and navigate to your server IP Address using **HTTP** or **HTTPS** protocol and the welcome screen should appear. Hit the **Next** button to move forward.
```
http://192.168.1.151/zabbix/setup.php
OR
https://192.168.1.151/zabbix/setup.php

```

On the first welcome screen, just hit the **Next** step button to move to the new step of the installation process.
![Zabbix Web Installer](https://www.tecmint.com/wp-content/uploads/2015/07/Zabbix-Web-Installer.png)Zabbix Web Installer
**16.** After a series of checks, if all pre-requires values are satisfied, hit the **Next** button to proceed further.
![Zabbix Checks Pre-requisites](https://www.tecmint.com/wp-content/uploads/2015/07/Zabbix-Checks-pre-requisites.png)Zabbix Checks Pre-requisites
**17.** On the next step provide the settings for the MySQL database, hit the **Test connection** button to test MySQL connectivity, and move to the step by pressing the **Next** button.
![Zabbix Database Settings](https://www.tecmint.com/wp-content/uploads/2015/07/Zabbix-Database-Settings.png)Zabbix Database Settings
**18.** Next, supply the **Host** (or **IP Address**) and the **Port** of the Zabbix server (use the host localhost and the port **10051** because Zabbix server is configured to run on the same host as the Zabbix frontend web interface in this tutorial) and a Name for Zabbix frontend installation. When you’re done hit **Next** to continue.
![Zabbix Server Details](https://www.tecmint.com/wp-content/uploads/2015/07/Zabbix-Server-Details-1.png)Zabbix Server Details
**19.** Next, check all the configurations parameters.
![Zabbix Pre Installation Summary](https://www.tecmint.com/wp-content/uploads/2015/07/Zabbix-Pre-installation-Summary.png)Zabbix Pre Installation Summary
**20.** After the installation process completes, a congratulations message will appear in your browser. Hit on the **Finish** button to exit the Zabbix frontend installer.
![Zabbix Installation Complete](https://www.tecmint.com/wp-content/uploads/2015/07/Zabbix-Installation-Complete.png)Zabbix Installation Complete
**21.** Finally, navigate to your server IP address or domain name by appending **/zabbix** URL address and log in to the Zabbix web admin panel with the default credentials presented below.
```
https://your_domain.tld/zabbix/
Username: Admin
Password: zabbix

```
![Zabbix Login](https://www.tecmint.com/wp-content/uploads/2015/07/Zabbix-Login-1.png)Zabbix Login
**22.** After you’ve logged in to the Zabbix admin panel, you can start to configure Zabbix and add new network resources to be monitored by the Zabbix server.
![Zabbix Dashboard](https://www.tecmint.com/wp-content/uploads/2015/07/Zabbix-Dashboard-2.png)Zabbix Dashboard
**23.** To change the Zabbix frontend admin account password, navigate to **Administration - > Users –> User** and hit on the **Change password** button and add your new password, as illustrated in the below screenshot. Finally, hit on the bottom **Update** button in order to save the admin account’s new password.
![Zabbix Admin Password Change](https://www.tecmint.com/wp-content/uploads/2015/07/Zabbix-Admin-Password-Change.png)Zabbix Admin Password Change
That’ll! The next series concerning the Zabbix monitoring system will discuss how to set up the server further using the web interface and how to install and configure Zabbix agents on different Linux distributions or even Windows systems.
Tags [zabbix](https://www.tecmint.com/tag/zabbix/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Create File-Sharing with ONLYOFFICE Docs and Seafile](https://www.tecmint.com/create-file-sharing-onlyoffice-docs-seafile/)
Next article:
[How to Configure Zabbix to Send Email Alerts to Gmail Account – Part 2](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/)
![Photo of author](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=100&d=blank&r=g)
Matei Cezar
I'am a computer addicted guy, a fan of open source and linux based system software, have about 4 years experience with Linux distributions desktop, servers and bash scripting.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#respond)** or
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
### 93 Comments
[Leave a Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/d0d2de2cdc1879757bfe68ebaa724c2ac70eae2e49467deea7451524d0df33bc?s=50&d=blank&r=g)
weidashuai
[ November 1, 2023 at 12:40 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-2097239)
After completing all the steps, I logged into the Zabbix service website and was prompted that the Zabbix server was not running, and the information displayed may not be current.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-2097239)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 2, 2023 at 9:07 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-2097571)
@Weidashuai,
First, ensure that the Zabbix server service is running. If not, you can start the service using the following command:
```
sudo systemctl start zabbix-server

```

After starting the Zabbix server, monitor the server’s logs to check for any issues or error messages that might provide more information about the problem.
```
sudo journalctl -xe -u zabbix-server

```

Look for any error messages that might point to the cause of the Zabbix server not running.
Next, you need to check that the Zabbix web interface is properly configured to communicate with the Zabbix server in the configuration settings, including the Zabbix server hostname and port.
```
sudo nano /etc/zabbix/zabbix_server.conf
OR
sudo vi /etc/zabbix/zabbix_server.conf

```

After making any necessary configuration changes, restart the Zabbix server to apply the changes:
```
sudo systemctl restart zabbix-server

```

Finally, make sure that your firewall not blocking Zabbix server communication. Adjust your firewall rules or SELinux policies if needed.
Then, log in again to the Zabbix web interface.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-2097571)
  2. ![](https://secure.gravatar.com/avatar/229bbbac61875956d5a9073aee5941451ab6391c46d5265cde2bf198e1aecc7e?s=50&d=blank&r=g)
Desh Deepak pal
[ December 10, 2022 at 5:14 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1927449)
Dear Sir,
I am stuck in installing **Zabbix** to my centos 7. I tried multiple times so it shows a conflict.
​Kindly find below the Details
I checked all the packages by:
