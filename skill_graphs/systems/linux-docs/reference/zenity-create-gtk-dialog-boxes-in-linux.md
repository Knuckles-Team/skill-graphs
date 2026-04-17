[Skip to content](https://www.tecmint.com/install-opennms-network-monitoring-in-centos-rhel/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-opennms-network-monitoring-in-centos-rhel/)
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
  * [Pro Courses](https://www.tecmint.com/install-opennms-network-monitoring-in-centos-rhel/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-opennms-network-monitoring-in-centos-rhel/)
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
  * [Pro Courses](https://www.tecmint.com/install-opennms-network-monitoring-in-centos-rhel/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-opennms-network-monitoring-in-centos-rhel/)
# Install OpenNMS Network Monitoring Tool in CentOS/RHEL 7
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: June 24, 2019 Read Time: 5 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [Leave a comment](https://www.tecmint.com/install-opennms-network-monitoring-in-centos-rhel/#respond)
**OpenNMS** (or **OpenNMS Horizon**) is a free and open source, scalable, extensible, highly configurable and cross-platform network monitoring and network management platform built using Java. It’s an enterprise-grade network service management platform currently being used for managing telecom and enterprise networks around the world.
**Read Also** : [Install OpenNMS Network Monitoring in Debian and Ubuntu](https://www.tecmint.com/install-opennms-in-debian-and-ubuntu/)
#### OpenNMS Features:
  * Supports service assurance.
  * It supports device and application monitoring.
  * It’s built on an event-driven architecture.
  * Supports the collection of performance metrics from industry standard agents via SNMP, JMX, WMI, NRPE, NSClient++ and XMP simply through configuration.
  * Allows for easy integration to extend service polling and performance data collection frameworks.
  * Supports topology discovery based on SNMP information from industry standards such as LLDP, CDP and Bridge-MIB discovery.
  * A provisioning system to discover your network and applications through manual, detected, or ReST API driven interfaces.


#### OpenNMS Requirements
  1. **Operating System** : [Red Hat Enterprise Linux 7](https://www.tecmint.com/red-hat-enterprise-linux-7-3-installation-guide/) or [CentOS 7](https://www.tecmint.com/centos-7-5-installation-guide/).
  2. **Minimal Hardware** : 2 CPU, 2 GB RAM, 20 GB disk


In this article, we will explain how to install and setup the latest **OpenNMS Horizon** network service monitoring software in **RHEL** and **CentOS 7.x** releases.
### Step1: Installing Java and Setting JAVA_HOME
The first step is to install **Java** and its environment on your system, as **OpenNMS Horizon** requires at least **Java 8** or higher version. We will install the latest **OpenJDK Java 11** version using the following [yum command](https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/).
```
# yum install java-11-openjdk

```

Once the Java installed, you can verify the version of Java on your system using the following command.
```
# java -version

```
![Check Java Version in Linux](https://www.tecmint.com/wp-content/uploads/2019/05/check-java-version.png)Check Java Version in Linux
Now set the **Java** environment variable for all users on boot time, by adding the following line in **/etc/profile** file.
```
export JAVA_HOME=/usr/lib/jvm/java-11

```

### Step 2: Install OpenNMS Horizon
To install **OpenNMS Horizon** , add the yum repository and the import GPG key.
```
# yum -y install https://yum.opennms.org/repofiles/opennms-repo-stable-rhel7.noarch.rpm
# rpm --import https://yum.opennms.org/OPENNMS-GPG-KEY

```

Then install the **opennms** meta package together with all built-in dependencies such as **jicmp6 and jicmp** , **opennms-core** , **opennms-webapp-jetty** , **postgresql** and **postgresql-libs**.
```
# yum -y install opennms

```

Once **opennms** meta packages are installed, you can verify them in the `/opt/opennms` using the following commands.
```
# cd /opt/opennms
# tree -L 1
.
└── opennms
   ├── bin
   ├── contrib
   ├── data
   ├── deploy
   ├── etc
   ├── jetty-webapps
   ├── lib
   ├── logs -> /var/log/opennms
   ├── share -> /var/opennms
   └── system

```

### Step 3: Initialize and Setup PostgreSQL
Now you need to **Initialize** the **PostgreSQL** database.
```
# postgresql-setup initdb

```

Next, start the **PostgreSQL** service for now and enable it to auto-start at system boot time, and check its status.
```
# systemctl start postgresql
# systemctl enable postgresql
# systemctl status postgresql

```
![Verify Postgres Status](https://www.tecmint.com/wp-content/uploads/2019/05/start-enable-and-view-postgres-status.png)Verify Postgres Status
Now create access to **PostgreSQL** by switching to the **postgres** user account, then access the postgres shell and create an **opennms** database user with a password and create an opennms database which is owned by the user opennms as follows.
```
# su - postgres
$ createuser -P opennms
$ createdb -O opennms opennms

```
![Create OpenNMS Database User](https://www.tecmint.com/wp-content/uploads/2019/05/create-opennms-db-user.png)Create OpenNMS Database User
Set a password for **Postgres** super user.
```
$ psql -c "ALTER USER postgres WITH PASSWORD 'admin123';"
$ exit

```
![Set Password for Postgres User](https://www.tecmint.com/wp-content/uploads/2019/05/change-postgres-admin-user-passwd.png)Set Password for Postgres User
Next, you need to modify the access policy for PostgreSQL in the `/var/lib/pgsql/data/pg_hba.conf` configuration file.
```
# vi /var/lib/pgsql/data/pg_hba.conf

```

Find the following lines and change the authentication method to `md5` to allow **OpenNMS Horizon** accessing the database over the local network with a [MD5 hashed password](https://www.tecmint.com/check-verify-md5sum-packages-files-in-linux/).
```
host    all             all             127.0.0.1/32            md5
host    all             all             ::1/128                 md5

```
![Set Access Policy for PostgreSQL](https://www.tecmint.com/wp-content/uploads/2019/05/change-postgres-db-access.png)Set Access Policy for PostgreSQL
Apply configuration changes for PostgreSQL.
```
# systemctl reload postgresql

```

Next, you need to configure database access in **OpenNMS Horizon**. Open the **/opt/opennms/etc/opennms-datasources.xml** configuration file to set credentials to access the PostgreSQL database you created above.
```
# vim /opt/opennms/etc/opennms-datasources.xml

```

Then set credentials to access the PostgreSQL database.
```
<jdbc-data-source name="opennms"
                    database-name="opennms"
                    class-name="org.postgresql.Driver"
                    url="jdbc:postgresql://localhost:5432/opennms"
                    user-name="**opennms**"
                    password="**your-passwd-here**" />

<jdbc-data-source name="opennms-admin"
                    database-name="template1"
                    class-name="org.postgresql.Driver"
                    url="jdbc:postgresql://localhost:5432/template1"
                    user-name="postgres"
                    password="**your-db-admin-pass-here**" />

```
![Set Credentials Access in PostgreSQL](https://www.tecmint.com/wp-content/uploads/2019/05/set-credentials-for-postgres-access.png) Set Credentials Access in PostgreSQL
### Step 4: Initialize and start OpenNMS Horizon
At this point, you need to integrate the default version of **Java** with **OpenNMS Horizon**. Run the following command to detect the **Java environment** and persist in the **/opt/opennms/etc/java.conf** configuration file.
```
# /opt/opennms/bin/runjava -s

```
![Integrate Java with OpenNMS](https://www.tecmint.com/wp-content/uploads/2019/05/integrate-java-with-opennms.png)Integrate Java with OpenNMS
Next, run the **OpenNMS Installer** which will initialize the database and detect system libraries persisted in **/opt/opennms/etc/libraries.properties**.
```
# /opt/opennms/bin/install -dis

```
![Run OpenNMS Installer](https://www.tecmint.com/wp-content/uploads/2019/05/run-opennms-installer.png)Run OpenNMS Installer
Then start **OpenNMS** horizon service via systemd for the mean time, enable it to auto-start at system boot and check its status.
```
# systemctl start opennms
# systemctl enable opennms
# systemctl status opennms

```
![Verify OpenNMS Status](https://www.tecmint.com/wp-content/uploads/2019/05/start-enable-and-check-opennms-status.png)Verify OpenNMS Status
If you have a firewall running on your system, there is one critical thing you need to do, before you can access the **OpenNMS Web Console**. Allow access to the OpenNMS web console from remote computers via the interface port**8980** in your firewall.
```
# firewall-cmd --permanent --add-port=8980/tcp
# firewall-cmd --reload

```

### Step 5: Access OpenNMS Web Console and Login
Next, open your browser and type any of the following URL to access the web console.
```
http://SERVER_IP:8980/opennms
OR
http://FDQN-OF-YOUR-SERVER:8980/opennms

```

Once the login interface appears, the default login username is **admin** and the password is **admin**.
![OpenNMS Web Console Login](https://www.tecmint.com/wp-content/uploads/2019/05/opennms-web-console-login-interface.png)OpenNMS Web Console Login
After login, you will land in the default admin dashboard. To ensure secure access to your OpenNMS web app, you need to change the default admin password. Go to the main navigation menu on “**admin → Change Password** , then under **User Account Self-Service** , click **Change Password** “.
Enter the old, set a new password and confirm it, then Click “**Submit** “. Afterwards, logout and login with your new password to use a more secure session.
![OpenNMS Default Admin Dashboard](https://www.tecmint.com/wp-content/uploads/2019/05/opennms-default-admin-dashboard.png)OpenNMS Default Admin Dashboard
**Read Also** : [How to Add Hosts in OpenNMS Monitoring Server](https://www.tecmint.com/add-hosts-in-opennms-monitoring/)
Last but not least, you need to learn the few steps to setup, configure, and maintain an **OpenNMS Horizon** via the web console using
**Read Also** : [20 Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)
**OpenNMS** is a free and fully open source enterprise-grade network service management platform. It is scalable, extensible and highly configurable. In this article, we have explained how to install **OpenNMS** in **CentOS** and **RHEL 7**. Do you have any questions or comments to share, use the feedback form below.
Tags [linux network monitoring](https://www.tecmint.com/tag/linux-network-monitoring/), [linux server monitoring](https://www.tecmint.com/tag/linux-server-monitoring/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Count Word Occurrences in a Text File](https://www.tecmint.com/count-word-occurrences-in-linux-text-file/)
Next article:
[How to Create Local HTTP Yum/DNF Repository on RHEL 8](https://www.tecmint.com/create-local-http-yum-dnf-repository-on-rhel-8/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-opennms-network-monitoring-in-centos-rhel/#respond)** or
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
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-opennms-network-monitoring-in-centos-rhel/#respond)
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
[How to Use Conspy to View and Control Remote Linux Virtual Consoles in Real Time](https://www.tecmint.com/use-conspy-to-view-and-control-remote-linux-virtual-consoles/)
[Linux Uptime Command With Usage Examples](https://www.tecmint.com/linux-uptime-command-examples/)
[Todo.txt – Manages Your Todo Tasks from Linux Terminal](https://www.tecmint.com/manage-todo-tasks-from-linux-terminal/)
[11 Lesser Known Useful Linux Commands](https://www.tecmint.com/lesser-known-linux-commands/)
[10 7zip (File Archive) Command Examples in Linux](https://www.tecmint.com/7zip-command-examples-in-linux/)
[13 CLI Tools Every Developer Should Master in 2025](https://www.tecmint.com/linux-cli-tools-for-developers/)
## Linux Server Monitoring Tools
[ngxtop – Monitor Nginx Log Files in Real Time in Linux](https://www.tecmint.com/ngxtop-monitor-nginx-log-files-in-real-time-in-linux/)
[How to Install Tripwire IDS (Intrusion Detection System) on Linux](https://www.tecmint.com/install-tripwire-ids-intrusion-detection-system-on-linux/)
[bmon – A Powerful Network Bandwidth Monitoring and Debugging Tool for Linux](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/)
[Amplify – NGINX Monitoring Made Easy](https://www.tecmint.com/amplify-nginx-monitoring-tool/)
[TCPflow – Analyze and Debug Network Traffic in Linux](https://www.tecmint.com/tcpflow-analyze-debug-network-traffic-in-linux/)
[systemd-analyze – Find System Boot-up Performance Statistics in Linux](https://www.tecmint.com/systemd-analyze-monitor-linux-bootup-performance/)
## Learn Linux Tricks & Tips
[How to Optimize and Compress JPEG or PNG Images in Linux Commandline](https://www.tecmint.com/optimize-and-compress-jpeg-or-png-batch-images-linux-commandline/)
[12 Ways to Find User Account Info and Login Details in Linux](https://www.tecmint.com/check-user-in-linux/)
[How to Check Which Apache Modules are Enabled/Loaded in Linux](https://www.tecmint.com/check-apache-modules-enabled/)
[How to Identify Working Directories Using Shell Characters and Variables](https://www.tecmint.com/identify-working-directories-in-linux/)
[How to Find MySQL, PHP and Apache Configuration Files](https://www.tecmint.com/find-mysql-php-apache-configuration-files/)
[How to Christmassify Your Linux Terminal and Shell](https://www.tecmint.com/christmassify-linux-terminal-and-shell/)
## Best Linux Tools
[7 Best Audio and Video Players for Gnome Desktop](https://www.tecmint.com/best-video-players-for-gnome-desktop/)
[9 Best Microsoft Excel Alternatives for Linux](https://www.tecmint.com/microsoft-excel-alternatives-for-linux/)
[10 Best PDF Document Viewers for Linux Systems](https://www.tecmint.com/linux-pdf-viewers-and-readers-tools/)
[10 Best Clipboard Managers for Linux](https://www.tecmint.com/best-clipboard-managers-for-linux/)
[8 Best Open-Source Disk Cloning & Backup Tools for Linux (2024)](https://www.tecmint.com/linux-disk-cloning-tools/)
[4 Best Tools for Creating Fillable PDF Forms on Linux](https://www.tecmint.com/create-pdf-forms-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-opennms-network-monitoring-in-centos-rhel/ "Scroll back to top")
Search for:
