[Skip to content](https://www.tecmint.com/install-librenms-debian/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-librenms-debian/)
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
  * [Pro Courses](https://www.tecmint.com/install-librenms-debian/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-librenms-debian/)
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
  * [Pro Courses](https://www.tecmint.com/install-librenms-debian/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-librenms-debian/)
# How to Install LibreNMS Monitoring Tool on Debian 11/10
[James Kiarie](https://www.tecmint.com/author/james2030kiarie/ "View all posts by James Kiarie")Last Updated: April 18, 2022 Read Time: 8 minsCategories [Debian](https://www.tecmint.com/category/debian/), [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [2 Comments](https://www.tecmint.com/install-librenms-debian/#comments)
**LibreNMS** is an open-source and fully-featured [networking monitoring tool](https://www.tecmint.com/linux-network-bandwidth-monitoring-tools/ "Bandwidth Monitoring Tools in Linux") that provides a wide range of monitoring features and capabilities for your network devices.
Key features include:
  * Automatic discovery of your entire network using ARP, SNMP, BGP, OSPF, LLDP, and FDP protocols.
  * An alerting system that is highly customizable and can be tweaked to send alerts via email, Slack, and other channels.
  * A simple, and easily customizable dashboard.
  * A fully-extensive API for managing and graphing data from your monitoring server.
  * Extensive device support – Supports a wide range of hardware vendors such as Cisco, Juniper, HP, and many more.
  * Automatic updates and bug fixes.
  * Multi-Factor authentication.
  * Native support for Android and iOS Apps.
  * and many more.


In this guide, we will install the **LibreNMS** monitoring tool on **Debian 11/10**.
### Step 1: Install Nginx, MariaDB and PHP
To start off, refresh the repositories and install the prerequisite packages as follows:
```
$ sudo apt update
$ sudo apt install software-properties-common wget apt-transport-https

```

The next step is to install **Nginx** and additional packages such as curl, git, SNMP, and python packages which will be required by the LibreNMS monitoring tool.
So, run the command:
```
$ sudo apt install nginx-full curl acl fping graphviz composer git imagemagick mtr-tiny nmap python3-pip python3-memcache python3-mysqldb python3-dotenv python3-pymysql rrdtool snmp snmpd whois python3-redis python3-systemd python3-setuptools python3-systemd

```

Next, install the **MariaDB** database server, **PHP** , and additional PHP extensions which are needed by the **LibreNMS** monitoring tool.
```
$ sudo apt install mariadb-server php php-fpm php-cli php-xml php-common php-gd php-json php-snmp php-pdo php-mysql php-zip php-curl php-mbstring php-pear php-bcmath

```

Once installed, be sure to enable **Nginx** , **php-fpm** , **MariaDB** , and **SNMP** services as shown.
```
$ sudo systemctl enable --now nginx
$ sudo systemctl enable --now php7.4-fpm
$ sudo systemctl enable --now mariadb
$ sudo systemctl enable --now snmpd.service

```

### Step 2: Configure TimeZone for PHP
The next step requires us to configure or set the PHP timezone. This is done in the **php.ini** file which is the default PHP configuration file.
Access the **php.ini** configuration files in the following paths using your favorite editor.
```
$ sudo nano /etc/php/7.4/fpm/php.ini
$ sudo nano /etc/php/7.4/cli/php.ini

```

Navigate to the **date.timezone** parameter and set it to your timezone. To get a comprehensive list of all the supported Timezone, head over to the
In this example, we are setting the timezone to **UTC**.
```
date.timezone = UTC

```

Then save the changes and exit the files.
### Step 3: Create a Database for LibreNMS
In this step, we will create a database for **LibreNMS** installation. But first, let us secure the database secure by running the following script:
```
$ sudo mysql_secure_installation

```

Follow the detailed prompts that will guide you on how to create the MariaDB root password, remove anonymous users and test the database and finally disallow remote root login.
Next, log into MariaDB:
```
$ sudo mysql -u root -p

```

Then run the following commands to create a database and database user and assign all privileges to the database user.
```
CREATE DATABASE librenms_db CHARACTER SET utf8 COLLATE utf8_unicode_ci;
CREATE USER 'librenms_user'@'localhost' IDENTIFIED BY 'P@ssword321';
GRANT ALL PRIVILEGES ON librenms_db.* TO 'librenms_user'@'localhost';

```

Then save the changes and exit the MariaDB prompt.
```
FLUSH PRIVILEGES;
EXIT;

```
![Create LibreNMS Database](https://www.tecmint.com/wp-content/uploads/2022/04/Create-LibreNMS-Database.png)Create LibreNMS Database
Some database fine-tuning is needed. So open the MariaDB configuration file shown:
```
$ sudo vim /etc/mysql/mariadb.conf.d/50-server.cnf

```

Then paste the following lines of code in the ‘**mysqld** ’ section.
```
innodb_file_per_table=1
lower_case_table_names=0

```

Save the changes and exit the file. To apply the changes, restart the database server.
```
$ sudo systemctl restart mariadb

```

### Step 4: Add LibreNMS User
You also need to create a new **LibreNMS** user. This is the user that **LibreNMS** will be running under. In this example, we are creating a user called **librenms** with the following attributes.
```
$ sudo useradd librenms -d /opt/librenms -M -r -s /bin/bash
$ sudo usermod -aG librenms www-data

```

  * The `-d` option sets the home directory for the librenms user to the **/opt/librenms** directory.
  * The `-r` option configures the librenms user as the system user.
  * The `-M` option skips creating a home directory for the user since it has already been defined using the `-d` option.
  * The `-s` option specifies the type of shell, in this case, bash.


### Step 5: Clone LibreNMS Git Repository
Shifting gears, we are now going to clone the **LibreNMS** git repository to begin setting it up.
Run the following commands to clone the Git repository
```
$ cd /opt
$ sudo git clone https://github.com/librenms/librenms.git

```

Then switch back to the home directory.
```
$ cd  ~

```

Next, we need to assign directory ownership and permissions to the **Librenms** home directory. To achieve this, run the following commands:
```
$ sudo chown -R librenms:librenms /opt/librenms
$ sudo chmod 771 /opt/librenms

```

Additionally, modify the access control lists for the Librenms home directory using the **setfacl** command. This grants the Librenms group permission to read and write on the subdirectories in the home directory.
```
$ sudo setfacl -d -m g::rwx /opt/librenms/rrd /opt/librenms/logs /opt/librenms/bootstrap/cache/ /opt/librenms/storage/
$ sudo setfacl -R -m g::rwx /opt/librenms/rrd /opt/librenms/logs /opt/librenms/bootstrap/cache/ /opt/librenms/storage/

```

### Step 6: Install PHP Dependencies
Some dependencies are required by PHP during the setup of the LibreNMS monitoring tool. To do this, you need to be logged in as the **librenmsuser**.
```
$ sudo su - librenms

```

Next, install all the PHP dependencies as follows.
```
$ ./scripts/composer_wrapper.php install --no-dev

```
![Install Librenms Dependencies](https://www.tecmint.com/wp-content/uploads/2022/04/Install-librenms-dependencies.png)Install Librenms Dependencies
Once the installation of the dependencies is complete, exit the librenms user.
```
$ exit

```

### Step 7: Configure PHP-FPM for LibreNMS Installation
Moving on, we need to make a few changes to **PHP-FPM** in order to support **LibreNMS**.
To accomplish this. Copy the ‘**www.conf** ‘ file which is the default pool configuration file to the ‘**librenms.conf** ‘ file as follows.
```
$ sudo cp /etc/php/7.4/fpm/pool.d/www.conf /etc/php/7.4/fpm/pool.d/librenms.conf

```

Next, edit the ‘**librenms.conf** ‘ file.
```
$ sudo nano /etc/php/7.4/fpm/pool.d/librenms.conf

```

Change the user and group parameters to librenms as shown
```
user = librenms
group = librenms

```

Next, modify the listen attribute to **/run/php-fpm-librenms.sock** as follows.
```
listen = /run/php-fpm-librenms.sock

```

Save the changes and exit the configuration. Be sure to restart the PHP-FPM service to apply the changes.
```
$ sudo systemctl restart php7.4-fpm

```

### Step 8: Configure the SNMP Daemon
The SNMP protocol is a TCP/IP protocol that collects and organizes metrics or information from managed devices across a network.
Most monitoring tools such as Cacti leverage the SNMP service to collect information from remote hosts. And so does LibreNMS.
To configure the SNMP service, go ahead and copy the **snmpd.conf.example** file to the **/etc/snmp/snmpd.conf** file.
```
$ sudo cp /opt/librenms/snmpd.conf.example /etc/snmp/snmpd.conf

```

Next, edit the **snmpd.conf** file.
```
$ sudo vim /etc/snmp/snmpd.conf

```

Locate the **RANDOMSTRINGGOESHERE** string.
```
com2sec readonly  default         RANDOMSTRINGGOESHERE

```

Change it to librenms.
```
com2sec readonly  default		  librenms

```

Save the changes and exit.
Next, download the distro file, which is a file that automatically detects the OS of the managed nodes and distinguishes its distribution.
```
$ sudo curl -o /usr/bin/distro https://raw.githubusercontent.com/librenms/librenms-agent/master/snmp/distro

```

Make it executable and restart the SNMP service.
```
$ sudo chmod +x /usr/bin/distro
$ sudo systemctl restart snmpd

```

### Step 9: Configure Nginx for LibreNMS
With **Nginx** as our preferred web server, we need to go an extra step and configure it in order to server LibreNMS.
First, we will create an Nginx server block as shown.
```
$ sudo nano /etc/nginx/sites-available/librenms

```

Paste the following lines of codes. For the **server_name** attribute, provide your server’s registered domain name or IP address.
```
server {
  listen      80;
  server_name **23.92.30.144**;
  root        /opt/librenms/html;
  index       index.php;
 charset utf-8;
  gzip on;
  gzip_types text/css application/javascript text/javascript application/x-javascript image/svg+xml text/plain text/xsd text/xsl text/xml image/x-icon;
  location / {
   try_files $uri $uri/ /index.php?$query_string;
  }
  location /api/v0 {
   try_files $uri $uri/ /api_v0.php?$query_string;
  }
  location ~ .php {
   include fastcgi.conf;
   fastcgi_split_path_info ^(.+.php)(/.+)$;
   fastcgi_pass unix:**/var/run/php/php-fpm.sock**;
  }
  location ~ /.ht {
   deny all;
  }
 }

```

Save the changes and exit the configuration file. Next, enable the Nginx server block by creating a symbolic link as shown.
```
$ sudo ln -s /etc/nginx/sites-available/librenms /etc/nginx/sites-enabled/

```

Then restart Nginx to apply the changes made to the configuration.
```
$ sudo systemctl restart nginx

```

Additionally, you can confirm that all the Nginx settings are okay by running the command:
```
$ sudo nginx -t

```
![Configure Nginx for LibreNMS](https://www.tecmint.com/wp-content/uploads/2022/04/Configure-Nginx-for-LibreNMS.png)Configure Nginx for LibreNMS
### Step 10: Copy the Logrotate and Cron Configuration
By default, **LibreNMS** stores its logs in the **/opt/librenms/logs** directory. Over time, this can easily fill up and present space problems. To prevent this, rotation of old log files is recommended.
Therefore copy the logrotate file in the LibreNMS directory to the **/etc/logrotate.d/** directory.
```
$ sudo cp /opt/librenms/misc/librenms.logrotate /etc/logrotate.d/librenms

```

Equally important, copy the cron job file as follows to allow automatic polling & discovery of new devices
```
$ sudo cp /opt/librenms/librenms.nonroot.cron /etc/cron.d/librenms

```

### Step 11: Complete the Setup of LibreNMS from a Browser
To complete the setup from a browser, head over to the following URL:
```
http://server-ip

```

This takes you to the pre-installation checklist shown. If all look good, click on the ‘**database** ’ icon to the right.
![LibreNMS Pre-Install Checks](https://www.tecmint.com/wp-content/uploads/2022/04/LibreNMS-Pre-Install-Checks.png)LibreNMS Pre-Install Checks
Be sure to fill in all the database details and click ‘**Check Credentials** ’.
![LibreNMS Database Settings](https://www.tecmint.com/wp-content/uploads/2022/04/LibreNMS-Database-Settings.png)LibreNMS Database Settings
Once the database details have been validated, click on ‘**Build Database** ’.
![LibreNMS Build Database](https://www.tecmint.com/wp-content/uploads/2022/04/LibreNMS-Build-Database.png)LibreNMS Build Database
When you get past this step, click the next icon to create an **Admin** user. Provide the username, password, and the email of the Admin user and click ‘Add user’.
![LibreNMS Admin User](https://www.tecmint.com/wp-content/uploads/2022/04/LibreNMS-Admin-User.png)LibreNMS Admin User
Finally, click on the last button to finish the installation.
![LibreNMS Installation](https://www.tecmint.com/wp-content/uploads/2022/04/LibreNMS-Installation.png)LibreNMS Installation
You will bump into this error informing you that the installer ‘**Failed to write file: /opt/librenms/.env** ’.
But don’t worry. Simply manually update the **/opt/librenms/.env** file afresh with the database details provided. These details will vary in your case.
![Failed to write file: /opt/librenms/.env](https://www.tecmint.com/wp-content/uploads/2022/04/Failed-to-write-file-librenms.png)Failed to write file: /opt/librenms/.env
So, access the file.
```
$ sudo nano /opt/librenms/.env

```

Delete all the content in the file and paste the details provided above into the file and save the changes.
Next head back and click the ‘**Retry** ’ button. This takes you to the LibreNMS login page. Provide the login credentials and click ‘Login’.
![LibreNMS Login](https://www.tecmint.com/wp-content/uploads/2022/04/LibreNMS-Login.png)LibreNMS Login
Once logged in you will get such a dashboard. From here, you can begin adding your hosts and monitor various metrics.
![LibreNMS Dashboard](https://www.tecmint.com/wp-content/uploads/2022/04/LibreNMS-Dashboard.png)LibreNMS Dashboard
And that’s it. In this guide, we have walked you through the installation of the **LibreNMS** monitoring tool on **Debian 11/10**.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Installation and Review of Linux Mint 20.3 XFCE](https://www.tecmint.com/linux-mint-xfce-installation/)
Next article:
[Puppy Linux – A Collection of Multiple Linux Distributions](https://www.tecmint.com/puppy-linux/)
![Photo of author](https://secure.gravatar.com/avatar/3b060d6a6c8d6305817bda1435529b27f2d4f900a7998bd703a17094636601a9?s=100&d=blank&r=g)
James Kiarie
This is James, a certified Linux administrator and a tech enthusiast who loves keeping in touch with emerging trends in the tech world. When I'm not running commands on the terminal, I'm taking listening to some cool music. taking a casual stroll or watching a nice movie.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-librenms-debian/#respond)** or
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
### 2 Comments
[Leave a Reply](https://www.tecmint.com/install-librenms-debian/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/576c9b8fa7072750a034310b1b4b534e20bf331084d84b66b9c29e379d79d4c0?s=50&d=blank&r=g)
chili
[ April 12, 2023 at 12:00 am  ](https://www.tecmint.com/install-librenms-debian/#comment-1995131)
In step 7 this line is inaccurate:
```
listen = /run/php-fpm-librenms.sock

```

I don’t see a **php-fpm-librenms.sock** file anywhere.
Trying to get this installed has truly been a challenge. Every website on how to do this has fatal flaws in their directions that make it so it doesn’t work. It’s like people don’t even check their work. How about starting with a fresh system and following your own instructions?
[Reply](https://www.tecmint.com/install-librenms-debian/#comment-1995131)
  2. ![](https://secure.gravatar.com/avatar/44ca88228a345eb33204ae3766dd8859f6834943aa5e78f308acd09aec4cc9c0?s=50&d=blank&r=g)
Ben Spradling
[ July 29, 2022 at 3:00 am  ](https://www.tecmint.com/install-librenms-debian/#comment-1852544)
Following your instructions, I was able to get it to start up and log in. One major problem. I have in my network a Linux web server, Ubuntu 18.04 with Apache2 running.
All my sites work until I start up librenms. Get an error when trying to access one of my sites. The site can’t be found. I shut down the librenms server and everything comes back up.
Librenms is running on Virtual Box Space. Ubuntu 20.04 LTS Focal.
I have tried about 10 different other sites’ installation instructions, but none of them worked.
Any suggestion or troubling shooting tips would be appreciated.
[Reply](https://www.tecmint.com/install-librenms-debian/#comment-1852544)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-librenms-debian/#respond)
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
[How to Compress Files Faster with Pigz Tool in Linux](https://www.tecmint.com/compress-files-faster-in-linux/)
[How to Clear RAM Cache, Buffers, and Swap in Linux Without Reboot](https://www.tecmint.com/clear-ram-memory-cache-buffer-and-swap-space-on-linux/)
[How to Search DuckDuckGo from the Linux Terminal](https://www.tecmint.com/search-duckduckgo-from-linux-terminal/)
[15 Useful ‘dpkg’ Commands for Debian and Ubuntu Users [With Examples]](https://www.tecmint.com/dpkg-command-examples/)
[Ncdu – A Powerful NCurses-Based Disk Usage Analyzer for Linux](https://www.tecmint.com/ncdu-a-ncurses-based-disk-usage-analyzer-and-tracker/)
[4 Ways to Disable or Lock Package Updates in Yum and DNF](https://www.tecmint.com/disable-package-updates-in-yum-and-dnf/)
## Linux Server Monitoring Tools
[How to Install Icinga2 Monitoring Tool on OpenSUSE](https://www.tecmint.com/install-icinga2-monitoring-opensuse/)
[How to Install Cacti (Network Monitoring) Tool on RHEL Systems](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/)
[Watchman – A File and Directory Watching Tool for Changes](https://www.tecmint.com/watchman-monitor-file-changes-in-linux/)
[Duf – A Better Linux Disk Monitoring Utility](https://www.tecmint.com/duf-linux-disk-monitoring-utility/)
[Nethogs – Monitor Linux Network Traffic Usage Per Process](https://www.tecmint.com/nethogs-monitor-per-process-network-bandwidth-usage-in-real-time/)
[Collectl: An Advanced All-in-One Performance Monitoring Tool for Linux](https://www.tecmint.com/collectl-linux-performance-reporting-monitoring/)
## Learn Linux Tricks & Tips
[How to Customize Bash Colors and Content in Linux Terminal Prompt](https://www.tecmint.com/customize-bash-colors-terminal-prompt-linux/)
[Set Date and Time for Each Command You Execute in Bash History](https://www.tecmint.com/display-linux-command-history-with-date-and-time/)
[2 Ways to Re-run Last Executed Commands in Linux](https://www.tecmint.com/run-last-executed-commands-in-linux/)
[10 Useful Sudoers Configurations for Setting ‘sudo’ in Linux](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/)
[Learn How to Set Your $PATH Variables Permanently in Linux](https://www.tecmint.com/set-path-variable-linux-permanently/)
[How to List Files Installed From a RPM or DEB Package in Linux](https://www.tecmint.com/list-files-installed-from-rpm-deb-package-in-linux/)
## Best Linux Tools
[12 Best Java IDE’s for Linux Developers](https://www.tecmint.com/best-java-ides/)
[Top 5 Open Source Collaboration Platforms for Linux in 2024](https://www.tecmint.com/open-source-collaboration-platforms-linux/)
[6 Best Linux Boot Loaders](https://www.tecmint.com/best-linux-boot-loaders/)
[Top 7 Apps to Install for Your Nextcloud Instance](https://www.tecmint.com/nextcloud-apps/)
[5 Best Platforms for Hosting Your Web Projects in 2024](https://www.tecmint.com/best-web-software-hosting-platforms/)
[17 Best KDE Multimedia Applications for Linux](https://www.tecmint.com/kde-multimedia-applications/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-librenms-debian/ "Scroll back to top")
Search for:
