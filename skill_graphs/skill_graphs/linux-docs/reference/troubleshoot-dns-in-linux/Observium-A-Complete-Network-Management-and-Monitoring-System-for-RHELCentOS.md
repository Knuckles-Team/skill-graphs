# Observium: A Complete Network Management and Monitoring System for RHEL/CentOS
[Ravi Saive](https://www.tecmint.com/author/admin/ "View all posts by Ravi Saive")Last Updated: January 7, 2015 Read Time: 6 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [43 Comments](https://www.tecmint.com/install-observium-in-centos/#comments)
**Observium** is a PHP/MySQL driven Network Observation and Monitoring application, that supports a wide range of operating systems/hardware platforms including, Linux, Windows, FreeBSD, Cisco, HP, Dell, NetApp and many more. It seeks to present a robust and simple web interface to monitor health and performance of your network.
![Install Observium in CentOS](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-620x405.jpeg)Install Observium in CentOS/RHEL
Observium gathers data from devices with the help of SNMP and display those data in graphical pattern via a web interface. It makes hefty use of the RRDtool package. It has a number of thin core design goals, which includes collecting as much historical information about devices, being totally auto-discovered with slight or no manual interruption, and having a very simple yet powerful interface.
##### Observium Demo
Please have a quick online demo of the Observium deployed by the developer at the following location.
This article will guide you on how to install **Observium** on **RHEL** , **CentOS** and **Scientific Linux** , the supported version is **EL** (**Enterprise Linux)** **6.x**. Currently, Observium unsupported for **EL** release **4** and **5** respectively. So, please don’t use following instructions on these releases.
### Step 1: Adding RPM Forge and EPEL Repositories
**RPMForge** and **EPEL** is a repository that provides many add-on rpm software packages for RHEL, CentOS and Scientific Linux. Let’s install and enable these two community based repositories using the following serious of commands.
##### On i386 Systems
```
# yum install wget
# wget http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el5.rf.i386.rpm
# wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
# wget http://apt.sw.be/RPM-GPG-KEY.dag.txt
# rpm --import RPM-GPG-KEY.dag.txt
# rpm -Uvh rpmforge-release-0.5.3-1.el5.rf.i386.rpm
# rpm -Uvh epel-release-6-8.noarch.rpm
```

##### On x86_64 Systems
```
# yum install wget
# wget http://packages.sw.be/rpmforge-release/rpmforge-release-0.5.2-2.el6.rf.rpm
# wget http://epel.mirror.net.in/epel/6/x86_64/epel-release-6-8.noarch.rpm
# wget http://apt.sw.be/RPM-GPG-KEY.dag.txt
# rpm --import RPM-GPG-KEY.dag.txt
# rpm -Uvh rpmforge-release-0.5.2-2.el6.rf.rpm
# rpm -Uvh epel-release-6-8.noarch.rpm
```
![Install RPMForge Repository](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-01-620x429.jpeg)Install RPMForge Repository ![Install EPEL Repository](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-02-620x410.jpeg)Install EPEL Repository ![Installing Repositories](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-03-620x430.jpeg)Installing Repositories
### Step 2: Install Needed Software Packages
Now let’s install the required software packages needed for Observium.
```
# yum install httpd php php-mysql php-gd php-snmp vixie-cron php-mcrypt \
php-pear net-snmp net-snmp-utils graphviz subversion mysql-server mysql rrdtool \
fping ImageMagick jwhois nmap ipmitool php-pear.noarch MySQL-python
```
![Install Needed Packages](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-04-620x412.jpeg)Install Needed Packages
If you wish to monitor virtual machines, please install ‘**libvirt** ‘ package.
```
# yum install libvirt
```

### Step 3: Downloading Observium
For your information, Observium has two following editions
  1. **Community/Open Source Edition** : This edition is freely available for download with less features and few security fixes.
  2. **Subscription Edition** : This edition is comes with additional features, rapid feature/fixes, hardware support and easy to use SVN-based release mechanism.


Firstly navigate to the **/opt** directly, here we will going to install Observium as default. If you wish to install somewhere else, please modify commands and configuration accordingly. We strongly suggest you to first deploy under **/opt** directory. Once you verify that everything works perfectly, you can install at your desired location.
If you have a active Observium subscription, you can use **SVN** repositories to download most recent version. A valid subscription account only valid for a single installation and two testing or development installations with daily security patches, new features and bug fixes.
To download most recent stable and current version of Observium, you need to have a **svn** package installed on the system, in order to pull the files from the SVN repository.
```
# yum install svn
```

##### Development Version
```
# svn co http://svn.observium.org/svn/observium/trunk observium
```

##### Stable Version
```
# svn co http://svn.observium.org/svn/observium/branches/stable observium
```

We don’t have a valid subscription, So we we are going to try out Observium using the Community/Open Source Edition. Download the latest ‘observium-community-latest.tar.gz’ stable version and unpack it as shown.
```
# cd /opt
# wget http://www.observium.org/observium-community-latest.tar.gz
# tar zxvf observium-community-latest.tar.gz
```
![Download Observium Community Edition](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-05-620x410.jpeg)Download Observium Community Edition
### Step 4: Creating Observium MySQL Database
This is a clean installation of MySQL. So, we are going to set a new root password with the help of following command.
```
# service mysqld start
# /usr/bin/mysqladmin -u root password 'yourmysqlpassword'
```

Now login into mysql shell and create the new Observium database.
```
# mysql -u root -p

mysql> CREATE DATABASE observium;
mysql> GRANT ALL PRIVILEGES ON observium.* TO 'observium'@'localhost' IDENTIFIED BY 'dbpassword';
```

### Step 5: Configure Observium
Configuring SELinux to work with Observium is beyond the scope of this article, so we disabled SELinux. If you are familiar with SELinux rules, then you can configure it, but no guarantee that the Observium work with active SELinux. So, better disable it permanently. To do, open ‘**/etc/sysconfig/selinux** ‘ file and change the option from ‘**permissive** ‘ to ‘**disabled** ‘.
```
# vi /etc/sysconfig/selinux
```
```
SELINUX=disabled
```

Copy the default configuration file ‘**config.php.default** ‘ to ‘**config.php** ‘ and modify the settings as shown.
```
# /opt/observium
# cp config.php.default config.php
```

Now open **‘config.php** ‘ file and enter MySQL details such as database name, username and password.
```
# vi config.php
```
```
// Database config
$config['db_host'] = '**localhost**';
$config['db_user'] = '**observium**';
$config['db_pass'] = '**dbpassword**';
$config['db_name'] = '**observium**';
```

Then add an entry for **fping** binary location to **config.php**. In RHEL distribution the location is different.
```
$config['fping'] = "**/usr/sbin/fping**";
```
![Enter MySQL Settings](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-06-620x414.jpeg) Enter MySQL Settings
Next, run the following command to setup the MySQL database and insert the database default file schema.
```
# php includes/update/update.php
```
![Insert Observium Database Schema](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-07-620x412.jpeg)Insert Observium Database Schema
### Step 6: Configure Apache for Observium
Now create a ‘**rrd** ‘ directory under ‘**/opt/observium** ‘ directory for storing RRD’s.
```
# /opt/observium
# mkdir rrd
```

Next, grant Apache ownership to ‘**rrd** ‘ directory to write and store RRD’s under this directory.
```
# chown apache:apache rrd
```

Create a Apache Virtual Host directive for Obervium in ‘**/etc/httpd/conf/httpd.conf** ‘ file.
```
# vi /etc/httpd/conf/httpd.conf
```

Add the following Virtual Host directive at the bottom of the file and enable Virtualhost section as shown in the screenshot below.
```
<VirtualHost *:80>
  DocumentRoot /opt/observium/html/
  ServerName  observium.domain.com
  CustomLog /opt/observium/logs/access_log combined
  ErrorLog /opt/observium/logs/error_log
  <Directory "/opt/observium/html/">
  AllowOverride All
  Options FollowSymLinks MultiViews
  </Directory>
  </VirtualHost>
```
![Create Observium Virtual Host](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-08-620x412.jpeg)Create Observium Virtual Host
To maintain observium logs, create a ‘**logs** ‘ directory for Apache under ‘**/op/observium** ‘ and apply Apache ownership to write logs.
```
# mkdir /opt/observium/logs
# chown apache:apache /opt/observium/logs
```

After all settings, restart Apache service.
```
# service httpd restart
```

### Step 7: Create Observium Admin User
Add a first user, give level of **10** for admin. Make sure to replace username and password with your choice.
```
# cd /opt/observium
# ./adduser.php tecmint tecmint123 10

User tecmint added successfully.
```

Next add a New Device and run following commands to populate the data for new device.
```
# ./add_device.php <hostname> <community> v2c
# ./discovery.php -h all
# ./poller.php -h all
```
![Populate Observium Data](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-09-620x412.jpeg)Populate Observium Data
Next set a cron jobs, create a new file ‘**/etc/cron.d/observium** ‘ and add the following contents.
```
33  */6   * * *   root    /opt/observium/discovery.php -h all >> /dev/null 2>&1
*/5 *      * * *   root    /opt/observium/discovery.php -h new >> /dev/null 2>&1
*/5 *      * * *   root    /opt/observium/poller-wrapper.py 1 >> /dev/null 2>&1
```

Reload cron process to take new entries.
```
# /etc/init.d/cron reload
```

The final step is to add httpd and mysqld services system-wide, to automatically start after system boot.
```
# chkconfig mysqld on
# chkconfig httpd on
```

Finally, open your favourite browser and point to **http://Your-Ip-Address**.
![Observium Login Screen](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-10-620x399.jpeg)Observium Login Screen ![Observium Dashboard](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-11-620x360.jpeg)Observium Dashboard
#### Observium Screenshot Tour
Following are the screen grabs of last mid-2013, taken from the Observium website. For up-to-date view, please check live demo.
![Complete System Information](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-12-529x450.png)Complete System Information ![Load Average Graphs](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-13-529x450.png)Load Average Graphs ![Historical Usage Overview](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-14-529x450.png)Historical Usage Overview ![CPU Frequency Monitoring](https://www.tecmint.com/wp-content/uploads/2014/07/Observium-15-529x450.png)CPU Frequency Monitoring
### Conclusion
Observium doesn’t mean to completely remove other monitoring tools such as [Nagios](https://www.tecmint.com/install-nagios-in-linux/) or [Cacti](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-6-3-5-8-and-fedora-17-12/), but rather to addition them with terrific understanding of certain devices. For this reason, its important to deploy Observium with Naigos or other monitoring systems to provide alerting and Cacti to produce customized graphing of your network devices.
**Reference Links** :
Tags [linux monitoring](https://www.tecmint.com/tag/linux-monitoring/), [observium](https://www.tecmint.com/tag/observium/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Installing Seafile (Secure Cloud Storage) with MySQL Database in RHEL/CentOS/SL 7.x/6.x](https://www.tecmint.com/install-seafile-in-linux/)
Next article:
[Installation of “Red Hat Enterprise Linux (RHEL) 7.0” with Screenshots](https://www.tecmint.com/redhat-enterprise-linux-7-installation/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-observium-in-centos/#respond)** or
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
### 43 Comments
[Leave a Reply](https://www.tecmint.com/install-observium-in-centos/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/852cbe733942fff27eda2d9bf6b3d5e384d47c83be72b82000e7779fe1b1076f?s=50&d=blank&r=g)
Mixkino
[ August 13, 2018 at 6:36 am  ](https://www.tecmint.com/install-observium-in-centos/#comment-1023225)
Observium improves your network’s reliability by providing you with the information to pro-actively respond to a greater number of potential issues before they become service impacting.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-1023225)
  2. ![](https://secure.gravatar.com/avatar/a4260578df0fdcb6507d777f0da715dab6311430766a24c46899c512c7fa4e45?s=50&d=blank&r=g)
Prateek
[ August 15, 2017 at 6:57 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-906655)
I am getting difficulties while adding centos 7 as a agent..
can you please add adding agent link into same tutorial
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-906655)
  3. ![](https://secure.gravatar.com/avatar/0f79077127dc690e6728489fc648032203ae9e587db59d85b67773606cb56623?s=50&d=blank&r=g)
GinFace
[ March 6, 2017 at 12:09 am  ](https://www.tecmint.com/install-observium-in-centos/#comment-873056)
Just to say Observium is very good however there is a premium for support.
There was a fork a while ago called LibreNMS which seems to be better and gives you a little more.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-873056)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 6, 2017 at 11:48 am  ](https://www.tecmint.com/install-observium-in-centos/#comment-873222)
@GinFace,
Yes Observium is very good monitoring tool for Linux, but I never heard of premium support, I thought its completely open source and free to use…Never heard of LibreNMS, is it active?
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-873222)
       * ![](https://secure.gravatar.com/avatar/0f79077127dc690e6728489fc648032203ae9e587db59d85b67773606cb56623?s=50&d=blank&r=g)
GinFaced
[ March 6, 2017 at 3:57 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-873289)
Yes quite active [
Observium has two versions a Community version and a Professional version. The Professional version has more perks and support & services options. I have to say though, the Tecmint walk through is excellent.
Thanks
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-873289)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 7, 2017 at 12:40 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-873640)
@GinFaced,
Thanks for the update, LibreNMS seems to be a good monitoring tool for Linux, let me give a try and see how it works, also if possible I will create a detailed guide on the same..
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-873640)
  4. ![](https://secure.gravatar.com/avatar/a0614161f25c044eb24bd7008b70f9e1b84737738e2a037e23fdc40edf4db653?s=50&d=blank&r=g)
zain
[ January 3, 2017 at 1:35 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-857279)
Email settings in Observium:
How to configure the email settings in Observium so i am able to receive alert emails. Any one please provide steps for Observium community edition email alert configuration file( config.php).
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-857279)
  5. ![](https://secure.gravatar.com/avatar/31b5b7345f31feeddc35543836f24732b2c60a2f243a88cb02cf04004fb7fd92?s=50&d=blank&r=g)
Ravinder
[ October 12, 2016 at 6:21 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-828134)
hello,
I am getting the following error, please advise
Resolving packages.sw.be (packages.sw.be)… 78.46.17.228
Connecting to packages.sw.be (packages.sw.be)|78.46.17.228|:80… failed: Connection timed out.
Retrying.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-828134)
  6. ![](https://secure.gravatar.com/avatar/4cb2318b34739f68a7cd65aebba704ac903e8de69d81563c4f623514f430bedb?s=50&d=blank&r=g)
James Otto
[ March 29, 2016 at 10:05 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-767105)
when I execute the following command
$ sudo service mysqld start
I get the following error
Redirecting to /bin/systemctl start mysqld.service
Failed to issue method call: Unit mysqld.service failed to load: No such file or directory.
Any ideas what file is missing? I am using Centos7
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-767105)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 30, 2016 at 11:21 am  ](https://www.tecmint.com/install-observium-in-centos/#comment-767348)
@James,
Have you installed MySQL or MariaDB on the system before starting up the database? after reading your error, it seems there isn’t any mysql installed on the system, better first install database and then try to start it. I think you’re using CentOS 7, so install MariaDB using following command.
```
# yum install mariadb mariadb-server

```
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-767348)
  7. ![](https://secure.gravatar.com/avatar/e8c472e0df3fd44bd8e2b00055a47183d743cc1d2f7bd9bf8db4a11301352f13?s=50&d=blank&r=g)
Jaco Toledo
[ January 10, 2016 at 2:04 am  ](https://www.tecmint.com/install-observium-in-centos/#comment-736514)
Observium is great, not as advanced as Cacti or Nagios but nonetheless a powerful tool to analyze traffic and possible errors i installed it on ubuntu and it runs great here.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-736514)
  8. ![](https://secure.gravatar.com/avatar/28dad0c9864bb36449c6e462023c33e53b57d06056c114eba4218701de850a99?s=50&d=blank&r=g)
John
[ August 27, 2015 at 8:20 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-652191)
Why would this NMS not replace something like Cacti? I’ve found it to be a good replacement for Cacti.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-652191)
  9. ![](https://secure.gravatar.com/avatar/dd1faa7751d345260daf0f9a476b3da998626f6577870278957f13a32f7f708e?s=50&d=blank&r=g)
Tonmoy
[ July 18, 2015 at 1:00 am  ](https://www.tecmint.com/install-observium-in-centos/#comment-626014)
Please upload a video on Youtube on how to install Observium in Cent-OS 6 (VMware workstation 10).
I have followed the total process. But when I write
Please suggest.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-626014)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 18, 2015 at 10:49 am  ](https://www.tecmint.com/install-observium-in-centos/#comment-626263)
@Tonmoy,
It could be incomplete installation, try to follow instructions carefully, it will work 100%
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-626263)
  10. ![](https://secure.gravatar.com/avatar/71ba1287dc3b6212b18b2013f16d6bb904ce4a883fd03ed6a83a5494deb162b8?s=50&d=blank&r=g)
MissSB
[ March 5, 2015 at 12:05 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-498921)
Hi guys,
I followed the documentation on setting up rsyslog, got a couple of firewalls and routers sending logs to the Observium server (/var/log/syslog) but nothing is replicated on the webconsole. I’m running it on Ubuntu Server 12.04.
.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-498921)
  11. ![](https://secure.gravatar.com/avatar/012e5969eba7c41bf2e8247a483e1a4c0408eb40fa9fcf33e6f008ec2b52a84c?s=50&d=blank&r=g)
Christos Papakostas
[ December 23, 2014 at 2:33 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-429710)
I have installed observium on Ubuntu 14.04 LTS. I want to monitor a VM Windows 7 instance. I added device on /etc/hosts, enabled snmp service on Windows 7 and after trying adding the device, the following errors appear on observium,
root@observium:/opt/observium# ./add_device.php Christos-PC public
Observium CE 0.14.11.6000
Add Device(s)
Try to add christos-pc:
Trying v2c community public …
No reply on community public using v2c.
Could not reach christos-pc with given SNMP parameters using v2c.
Trying v1 community public …
No reply on community public using v1.
Could not reach christos-pc with given SNMP parameters using v1.
Devices skipped: 1.
USAGE:
add_device.php [community] [v1|v2c] [port] [udp|udp6|tcp|tcp6]
add_device.php [any|nanp|anp|ap] [v3] [user] [password] [enckey] [md5|sha] [aes|des] [port] [udp|udp6|tcp|tcp6]
add_device.php
EXAMPLE:
SNMPv1/2c: add_device.php [community] [v1|v2c] [port] [udp|udp6|tcp|tcp6]
SNMPv3 : Defaults : add_device.php any v3 [user] [port] [udp|udp6|tcp|tcp6]
No Auth, No Priv : add_device.php nanp v3 [user] [port] [udp|udp6|tcp|tcp6]
Auth, No Priv : add_device.php anp v3 [md5|sha] [port] [udp|udp6|tcp|tcp6]
Auth, Priv : add_device.php ap v3 [md5|sha] [aes|des] [port] [udp|udp6|tcp|tcp6]
FILE : add_device.php
ADD FROM FILE:
To add multiple devices, create a file in which each line contains one device with or without options.
Format for device options, the same as specified in USAGE.
Should I configure snmp parameters(v1 or v2c) on Windows 7 snmp service or the problem is something else I don’t really realize?
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-429710)
  12. ![](https://secure.gravatar.com/avatar/23eca3ba40b322386ad943ee47a7d9aee877bf6633f3cdc827852761f8406f8f?s=50&d=blank&r=g)
Mike
[ December 4, 2014 at 11:19 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-393307)
new instance of Observium running on Unbuntu 14.04. i add devices to /etc/hosts and save, go to the GUI and ad Device but it never finishes polling.
Thanks,
Mike
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-393307)
  13. ![](https://secure.gravatar.com/avatar/dd1faa7751d345260daf0f9a476b3da998626f6577870278957f13a32f7f708e?s=50&d=blank&r=g)
Mr.X
[ September 20, 2014 at 8:01 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-279692)
Dear Ravi,
Many thanks for your excellent presentation. I’m trying to install observium in my CentOS 6. But could not make it. I was trying to install it in VMWare 10. Everything goes just fine but when I try to login through the browser, it doesn’t work.
Can you give me any link of a video where the process is shown step-by-step.
Waiting eagerly for your reply.
Thanks in advance.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-279692)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ September 22, 2014 at 6:13 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-286756)
Did you get any error message on the browser while accessing it?
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-286756)
       * ![](https://secure.gravatar.com/avatar/ca52d19762533372f2437b8cafabe1086cd40c75e91c9b96e620de90b04c299d?s=50&d=blank&r=g)
Ravi
[ October 13, 2014 at 7:27 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-331904)
Hi
Can you provide me steps how to add host in obsermin to monitor windows server
Thanks
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-331904)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 14, 2014 at 4:38 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-333310)
Surely, in our upcoming article, we will try to cover the integration of hosts to Observium panel.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-333310)
  14. ![](https://secure.gravatar.com/avatar/2fef9d3ef1b0be86185e807d7e041b011822d9098453bb479cf6a4c195790b14?s=50&d=blank&r=g)
Ion
[ July 16, 2014 at 7:21 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-215869)
I had a problem starting httpd until I rebooted, pretty sure SELinux was the culprit; I did a quick search but to disable it do you really have to reboot? If not it might be a good idea to include a line in this howto…
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-215869)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 17, 2014 at 11:14 am  ](https://www.tecmint.com/install-observium-in-centos/#comment-216294)
Yes, you need a reboot after disabling SELinux.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-216294)
       * ![](https://secure.gravatar.com/avatar/d8968ea41abd969c286209897178f92f4adf149a435dc34899f1f726ef5c9484?s=50&d=blank&r=g)
sriram
[ July 21, 2014 at 5:16 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-219727)
im very new to admin in linux environment.. My LAN having one unmanagable router and unmanagable switch.. IP Range 192.168.0.0/24… i using centos 6.5 for configure observium. but i couldn’t make it.. i tried with DNS server configuration also but the name dose’t get resolve please help me to build my infra….. :-(
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-219727)
  15. ![](https://secure.gravatar.com/avatar/52ee551933e22d52844509d5b7d65d545913c2a62e427f71d9c585608406b035?s=50&d=blank&r=g)
sriram
[ July 8, 2014 at 6:48 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-209890)
No devices found
Please try adjusting your search parameters.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-209890)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 10, 2014 at 4:01 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-211573)
It seems your device is not reachable.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-211573)
  16. ![](https://secure.gravatar.com/avatar/52ee551933e22d52844509d5b7d65d545913c2a62e427f71d9c585608406b035?s=50&d=blank&r=g)
sriram
[ July 8, 2014 at 6:47 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-209889)
This is error i have facing …
[root@galaxy observium]# ./add_device.php sriram.galaxy.local sriram v2c
Observium v0.14.4.5229
Add Device(s)
Try to add sriram.galaxy.local:
Could not resolve sriram.galaxy.local.
Devices skipped: 1.
USAGE:
add_device.php [community] [v1|v2c] [port] [udp|udp6|tcp|tcp6]
add_device.php [any|nanp|anp|ap] [v3] [user] [password] [enckey] [md5|sha] [aes|des] [port] [udp|udp6|tcp|tcp6]
add_device.php
EXAMPLE:
SNMPv1/2c: add_device.php [community] [v1|v2c] [port] [udp|udp6|tcp|tcp6]
SNMPv3 : Defaults : add_device.php any v3 [user] [port] [udp|udp6|tcp|tcp6]
No Auth, No Priv : add_device.php nanp v3 [user] [port] [udp|udp6|tcp|tcp6]
Auth, No Priv : add_device.php anp v3 [md5|sha] [port] [udp|udp6|tcp|tcp6]
Auth, Priv : add_device.php ap v3 [md5|sha] [aes|des] [port] [udp|udp6|tcp|tcp6]
FILE : add_device.php
ADD FROM FILE:
To add multiple devices, create a file in which each line contains one device with or without options.
Format for device options, the same as specified in USAGE.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-209889)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 10, 2014 at 4:02 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-211574)
Again, the errors indicates that your remote host name is not resolved by the Observium server.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-211574)
  17. ![](https://secure.gravatar.com/avatar/52ee551933e22d52844509d5b7d65d545913c2a62e427f71d9c585608406b035?s=50&d=blank&r=g)
sriram
[ July 8, 2014 at 6:41 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-209885)
hi im very new to observium.. i have some doubts on if observium can manage with only manageable switches like cisco.. because i couldn’t find any host in my network.. im using 192.168.1.0 range of IP. i dont have manageable switch.. i confiugred observium i can logoin.. how to find other hosts in my network..
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-209885)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 10, 2014 at 4:02 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-211576)
You need to add them manually to Observium server and run the commands to update the polling data.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-211576)
  18. ![](https://secure.gravatar.com/avatar/921398407e145ce0f88f4bbd19f4a9694a58f0b39e17bdf495c23c0ad01aac81?s=50&d=blank&r=g)
emjay
[ July 4, 2014 at 9:55 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-207232)
I followed this tut to the “T” and everything works great except that I can’t access the server from a remote computer on the same LAN using the IP address of the server. While on the server
Any ideas?
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-207232)
     * ![](https://secure.gravatar.com/avatar/921398407e145ce0f88f4bbd19f4a9694a58f0b39e17bdf495c23c0ad01aac81?s=50&d=blank&r=g)
emjay
[ July 4, 2014 at 10:44 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-207258)
never mind, I forgot to modify iptables.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-207258)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 7, 2014 at 4:08 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-208970)
Please open the port 80 on the firewall to allow other client to access.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-208970)
  19. ![](https://secure.gravatar.com/avatar/fed065bbbaf6a66d426ec2d290befcc942b531721becba6efb3f5538b620e584?s=50&d=blank&r=g)
srikanth
[ July 4, 2014 at 4:52 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-207087)
can u give me ur mail id i will send u the screen shots and docs
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-207087)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 7, 2014 at 4:18 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-208982)
Please use our contact link to get in touch.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-208982)
  20. ![](https://secure.gravatar.com/avatar/fed065bbbaf6a66d426ec2d290befcc942b531721becba6efb3f5538b620e584?s=50&d=blank&r=g)
nani
[ July 4, 2014 at 2:17 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-207016)
Hi Ravi
i successfully added remote hosts to observium ,but memory,storage graphs shows error drawing graph and i added oneday back still shoeing this error msg
Device not yet polled
This device has not yet been successfully polled. System information and statistics will not be populated and graphs will not draw.
Please wait 5-10 minutes for graphs to draw correctly.
Device not yet discovered
This device has not yet been successfully discovered. System information and statistics will not be populated and graphs will not draw.
This device should be automatically discovered within 10 minutes.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-207016)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 4, 2014 at 3:51 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-207058)
Yeah that’s great you’ve successfully added remote host to Observium, it would be great if you could share the docs for adding remote hosts so others can benefit from your instructions. Can you share the screeshot for the same, so it will helpful me to trace the problem.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-207058)
  21. ![](https://secure.gravatar.com/avatar/fed065bbbaf6a66d426ec2d290befcc942b531721becba6efb3f5538b620e584?s=50&d=blank&r=g)
srikanth
[ July 3, 2014 at 6:21 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-206407)
Thanks for ur help added remote host :)
,,,
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-206407)
  22. ![](https://secure.gravatar.com/avatar/fed065bbbaf6a66d426ec2d290befcc942b531721becba6efb3f5538b620e584?s=50&d=blank&r=g)
srikanth
[ July 3, 2014 at 3:26 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-206328)
Hi Ravi Thanks For the reply
i hv installed needed step:2 packages on remote machine and yum install libvirt
but still getting same problem and iam working on vmplayer centos 6.5 machine with etherner br0 device
[root@observium ~]# tail -f /var/log/messages
Jul 3 03:12:55 observium kernel: br0: port 1(eth0) entering forwarding state
Jul 3 03:12:57 observium polkitd[2255]: started daemon version 0.96 using authority implementat ion `local’ version `0.96′
Jul 3 03:12:58 observium rtkit-daemon[2264]: Sucessfully made thread 2262 of process 2262 (/usr /bin/pulseaudio) owned by ’42’ high priority at nice level -11.
Jul 3 03:12:58 observium pulseaudio[2262]: alsa-util.c: Disabling timer-based scheduling becaus e running inside a VM.
Jul 3 03:12:58 observium rtkit-daemon[2264]: Sucessfully made thread 2270 of process 2262 (/usr /bin/pulseaudio) owned by ’42’ RT at priority 5.
Jul 3 03:12:58 observium pulseaudio[2262]: alsa-util.c: Disabling timer-based scheduling becaus e running inside a VM.
Jul 3 03:12:58 observium rtkit-daemon[2264]: Sucessfully made thread 2271 of process 2262 (/usr /bin/pulseaudio) owned by ’42’ RT at priority 5.
Jul 3 03:12:58 observium pulseaudio[2262]: alsa-source.c: ALSA woke us up to read new data from the device, but there was actually nothing to read!
Jul 3 03:12:58 observium pulseaudio[2262]: alsa-source.c: Most likely this is a bug in the ALSA driver ‘snd_ens1371’. Please report this issue to the ALSA developers.
Jul 3 03:12:58 observium pulseaudio[2262]: alsa-source.c: We were woken up with POLLIN set — h owever a subsequent snd_pcm_avail() returned 0 or another value < min_avail.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-206328)
  23. ![](https://secure.gravatar.com/avatar/fed065bbbaf6a66d426ec2d290befcc942b531721becba6efb3f5538b620e584?s=50&d=blank&r=g)
srikanth
[ July 3, 2014 at 11:38 am  ](https://www.tecmint.com/install-observium-in-centos/#comment-206203)
hi ravi
when i try to add hostname am getting this issue pls help me
[root@Test observium]# ./add_device.php test.centos.com public v2c
Observium v0.14.4.5229
Add Device(s)
Try to add test.centos.com:
Trying v2c community public …
No reply on community public using v2c.
Could not reach test.centos.com with given SNMP community using v2c.
Devices skipped: 1.
logs?
[root@Test ~]# tail -f /var/log/messages
Jul 2 05:28:59 Test snmpd[4200]: net-snmp: 2 error(s) in config file(s)
Jul 2 05:28:59 Test snmpd[4203]: NET-SNMP version 5.5
Jul 2 05:29:56 Test snmpd[4203]: Received TERM or STOP signal… shutting down …
Jul 2 05:29:56 Test snmpd[4223]: /etc/snmp/snmpd.conf: line 93: Error: bad secu rity level (noauthnopriv, authnopriv, authpriv)
Jul 2 05:29:56 Test snmpd[4223]: /etc/snmp/snmpd.conf: line 94: Error: bad secu rity level (noauthnopriv, authnopriv, authpriv)
Jul 2 05:29:56 Test snmpd[4223]: net-snmp: 2 error(s) in config file(s)
Jul 2 05:29:56 Test snmpd[4226]: NET-SNMP version 5.5
Jul 2 06:47:45 Test snmpd[4226]: Received TERM or STOP signal… shutting down …
Jul 2 06:47:45 Test snmpd[4690]: NET-SNMP version 5.5
Jul 2 22:05:36 Test kernel: hrtimer: interrupt took 11093372 ns
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-206203)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 3, 2014 at 1:15 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-206256)
You must have SNMP tools installed on remote host and make sure remote and observium server can talk each other.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-206256)
  24. ![](https://secure.gravatar.com/avatar/426269011ab6eef547c6bcb55aa86822bb311c02f3cc99cfa4e64d7cfb6edce5?s=50&d=blank&r=g)
Andrew Meyer
[ July 2, 2014 at 2:40 am  ](https://www.tecmint.com/install-observium-in-centos/#comment-205119)
when I do the php updates command I get this:
[root@monitoring observium]# !30
php includes/update/update.php
— Updating database/file schema
000 -> 001 … (db) done.
001 -> 002 … (db) done.
002 -> 003 … (db) done.
003 -> 004 … (db) done.
004 -> 005 … (db) done.
005 -> 006 … (db) done (6 errors).
006 -> 007 … (db) done (1 errors).
007 -> 008 … (db) done (1 errors).
008 -> 009 … (db) done (9 errors).
009 -> 010 … (db) done (1 errors).
010 -> 011 … (db) done (1 errors).
011 -> 012 … (db) done (1 errors).
012 -> 013 … (db) done (1 errors).
013 -> 014 … (db) done (2 errors).
014 -> 015 … (db) done (2 errors).
015 -> 016 … (db) done (5 errors).
016 -> 017 … (db) done (1 errors).
017 -> 018 … (db) done (3 errors).
018 -> 019 … (db) done (1 errors).
019 -> 020 … (db) done (6 errors).
020 -> 021 … (db) done (3 errors).
021 -> 022 … (db) done (1 errors).
022 -> 023 … (db) done (5 errors).
023 -> 024 … (db) done (2 errors).
024 -> 025 … (db) done (11 errors).
025 -> 026 … (db) done (1 errors).
026 -> 027 … (db) done (2 errors).
027 -> 028 … (db) done (22 errors).
028 -> 029 … (db) done (1 errors).
029 -> 030 … (db) done (2 errors).
030 -> 031 … (db) done (1 errors).
031 -> 032 … (db) done (2 errors).
032 -> 033 … (db) done.
033 -> 034 … (db) done (2 errors).
034 -> 035 … (db) done (1 errors).
035 -> 036 … (db) done (1 errors).
036 -> 037 … (db) done (2 errors).
037 -> 038 … (db) done (2 errors).
038 -> 039 … (db) done (1 errors).
039 -> 040 … (db) done (1 errors).
040 -> 041 … (db) done (2 errors).
041 -> 042 … (db) done (5 errors).
042 -> 043 … (db) done (9 errors).
043 -> 044 … (db) done (2 errors).
044 -> 045 … (db) done (4 errors).
045 -> 046 … (db) done.
Where are the logs for this…mysql is on a different IP.
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-205119)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 2, 2014 at 2:14 pm  ](https://www.tecmint.com/install-observium-in-centos/#comment-205488)
It’s fine to have such SQL errors in the SQL revisions up to 006. No need to worry about much, just continue installation…
[Reply](https://www.tecmint.com/install-observium-in-centos/#comment-205488)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-observium-in-centos/#respond)
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
[Pydf – An Alternative “df” Command to Check Disk Usage in Different Colours](https://www.tecmint.com/pydf-command-to-check-disk-usage/)
[How to List Running Services in Linux (systemctl Examples)](https://www.tecmint.com/list-all-running-services-under-systemd-in-linux/)
[procinfo – Shows System Statistics from /proc Filesystem](https://www.tecmint.com/procinfo-shows-proc-system-information/)
[8 Linux Nslookup Commands to Troubleshoot DNS (Domain Name Server)](https://www.tecmint.com/8-linux-nslookup-commands-to-troubleshoot-dns-domain-name-server/)
[How to Install and Run Multiple glibc Libraries in Linux](https://www.tecmint.com/install-multiple-glibc-libraries-linux/)
[How to Check How Long a Process Has Been Running in Linux](https://www.tecmint.com/check-running-process-time-in-linux/)
## Linux Server Monitoring Tools
[Glances – An Advanced Real Time System Monitoring Tool for Linux](https://www.tecmint.com/glances-linux-monitoring/)
[Collectl: An Advanced All-in-One Performance Monitoring Tool for Linux](https://www.tecmint.com/collectl-linux-performance-reporting-monitoring/)
[How to Monitor Website and Application with Uptime Kuma](https://www.tecmint.com/uptime-kuma-linux-website-monitoring-tool/)
[How to Install Nagios Monitoring in RHEL, Rocky, and AlmaLinux](https://www.tecmint.com/install-nagios-in-linux/)
[How to Monitor Linux Server Security with Osquery](https://www.tecmint.com/monitor-linux-server-security-with-osquery/)
[20 Best Linux Bandwidth Monitoring Tools for Network Analysis](https://www.tecmint.com/linux-network-bandwidth-monitoring-tools/)
## Learn Linux Tricks & Tips
[How to Set Static IP Address and Configure Network in Linux](https://www.tecmint.com/set-add-static-ip-address-in-linux/)
[Ways to Use ‘find’ Command to Search Directories More Efficiently](https://www.tecmint.com/find-directory-in-linux/)
[How to Search and Remove Directories Recursively on Linux](https://www.tecmint.com/find-remove-directory-in-linux/)
[How to Copy a File to Multiple Directories in Linux](https://www.tecmint.com/copy-file-to-multiple-directories-in-linux/)
[How to Send a Message to Logged Users in Linux Terminal](https://www.tecmint.com/send-a-message-to-logged-users-in-linux-terminal/)
[Ternimal – Show Animated Lifeform in Your Linux Terminal](https://www.tecmint.com/ternimal-show-animated-lifeform-in-linux-terminal/)
## Best Linux Tools
[5 Best Open Source Internet Radio Player for Linux](https://www.tecmint.com/internet-radio-player-linux/)
[10 Best PDF Document Viewers for Linux Systems](https://www.tecmint.com/linux-pdf-viewers-and-readers-tools/)
[10 Most Popular Download Managers for Linux in 2023](https://www.tecmint.com/download-managers-for-linux/)
[Top 6 Telegram Bots to Boost Your Productivity in 2025](https://www.tecmint.com/best-telegram-bots/)
[7 Best Email Clients for Linux Systems](https://www.tecmint.com/best-email-clients-linux/)
[21 Best Slack Alternatives for Team Chat [Free & Paid]](https://www.tecmint.com/slack-alternatives/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-observium-in-centos/ "Scroll back to top")
Search for:
