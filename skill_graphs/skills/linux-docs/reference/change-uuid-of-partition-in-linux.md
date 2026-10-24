[Skip to content](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/)
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
  * [Pro Courses](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/)
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
  * [Pro Courses](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/)
# Install Munin (Network Monitoring) in RHEL, CentOS and Fedora
[Ravi Saive](https://www.tecmint.com/author/admin/ "View all posts by Ravi Saive")Last Updated: June 30, 2017 Read Time: 5 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [19 Comments](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comments)
**Munin** (**Network Monitoring Tool**) is an open source web based network monitoring application written in **Perl** that shows network usage of servers and services in graphical form using **RRDtool**. With the help of Munin you can monitor the performance of your systems, networks, SANS’s and applications.
It has a **master/node** architecture where master connects to each node regularly and pulls the data from them. It then uses RRDtool to log and generate updated graphs.
**Suggested Read:** [20 Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)
In this article, we will walk through you the steps in setting up **Munin** ( **Network Monitoring Tool** ) with **Munin Node** in **RHEL** , **CentOS** and **Fedora** systems using following environment.
```
**Munin Server** - hostname: **munin.tecmint.com** and IP Address: **192.168.103**
**Munin Client** - hostname: **munin-node.tecmint.com** and IP Address: **192.168.15**

```

### Installing Munin in RHEL, CentOS & Fedora
Installing **Munin** is very simple, just follow my below step-by-step commands to install it on your server.
#### Step 1: Install EPEL Repository
**Munin** can be installed by using **Fedora** ‘s **EPEL** repository under **RHEL 7.x/6.x/5.x** and **CentOS 7.x/6.x/5.x**.
Just, run the following commands as root user to install and enable **Epel** repository using **wget**.
##### RHEL/CentOS 7
```
------------------ **RHEL/CentOS 7 - 64-Bit** ------------------
# wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-9.noarch.rpm
# rpm -ivh epel-release-7-9.noarch.rpm

```

##### RHEL/CentOS 6
```
------------------ **RHEL/CentOS 6 - 32-Bit** ------------------
# wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
# rpm -ivh epel-release-6-8.noarch.rpm

------------------ **RHEL/CentOS 6 - 64-Bit** ------------------
# http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
# rpm -ivh epel-release-6-8.noarch.rpm

```

##### RHEL/CentOS 5
```
------------------ **RHEL/CentOS 5 - 32-Bit** ------------------
# wget http://download.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm
# rpm -ivh epel-release-5-4.noarch.rpm

------------------ **RHEL/CentOS 5 - 64-Bit** ------------------
# wget http://download.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm
# rpm -ivh epel-release-5-4.noarch.rpm

```

**Note** : Fedora users don’t need to install **EPEL** repository, because **munin** is included in Fedora and can be installed using **yum** or **dnf** package manager.
**Suggested Read:** [20 Yum Commands to Manage Linux Package Management](https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/)
**Suggested Read:** [27 Dnf Commands to Manage Fedora Package Management](https://www.tecmint.com/dnf-commands-for-fedora-rpm-package-management/)
Next, do a system update to make sure that the **EPEL** package database is loaded before we going to install **Munin**.
```
------------------ **On RHEL and CentOS Only** ------------------
# yum -y update

```

#### Step 2: Install Apache Web Server
**Munin** needs a working web server such as **Apache** or **Nginx** to display its statistics files. We will install **Apache** web server to serve Munin graphs here.
```
------------------ **On RHEL, CentOS and Fedora** ------------------
# yum install httpd

------------------ **On Fedora 22+ Releases** ------------------
# dnf install httpd

```

Once Apache installed, start and enable the service to automatically start at system boot time.
```
------------------ **On RHEL, CentOS and Fedora** ------------------
# service httpd start
# chkconfig --level 35 httpd on

------------------ **On RHEL/CentOS 7 and Fedora 22+** ------------------
# systemctl enable httpd
# systemctl start httpd

```

#### Step 3: Install Munin and Munin-Node
Now its time to install the **Munin** and **Munin-Node** as shown.
```
------------------ **On RHEL, CentOS and Fedora** ------------------
# yum -y install munin munin-node

------------------ **On Fedora 22+ Releases** ------------------
# dnf -y install munin munin-node

```

By default the above installation creates following directories.
  1. **/etc/munin/munin.conf** : Munin master configuration file.
  2. **/etc/cron.d/munin** : Munin cron file.
  3. **/etc/httpd/conf.d/munin.conf** : Munin Apache configuration file.
  4. **/var/log/munin** : Munin log directory.
  5. **/var/www/html/munin** : Munin web directory.
  6. **/etc/munin/munin-node.conf** : Munin Node master configuration file.
  7. **/etc/munin/plugins.conf** : Munin plugins configuration file.


#### Step 3: Configure Munin and Password Protect Munin
This is step is optional and only applicable if you want to use `munin.tecmint.com` instead `localhost` in HTML output as shown:
Open `/etc/munin/munin.conf` configuration file and make the changes as suggested and don’t forget to replace `munin.tecmint.com` with your server name.
```
# a simple host tree
[**munin.tecmint.com**]
    address 127.0.0.1
    use_node_name yes
[...]

```

Next password protect Munin statistics with **username** and **password** using Apache basic auth module as shown:
```
# htpasswd /etc/munin/munin-htpasswd admin

```
![Munin Password Protect](https://www.tecmint.com/wp-content/uploads/2012/07/Munin-Password-Protect.png)Munin Password Protect
Next restart Munin and enable it to start at boot time automatically.
```
------------------ **On RHEL, CentOS and Fedora** ------------------
# service munin-node start
# chkconfig --level 35 munin-node on

------------------ **On RHEL/CentOS 7 and Fedora 22+** ------------------
# systemctl enable munin-node
# systemctl start munin-node

```

#### Step 4: Accessing Munin Web Interface
Wait for **30** minutes so that **Munin** can generate graphs and displayed it. To see first output of graphs, open your browser and navigate to `http://munin.tecmint.com/munin` and enter login credentials.
If it didn’t prompt for **username** and **password** , open `/etc/httpd/conf.d/munin.conf` and change the username from `Munin` to `admin` and restart Apache.
```
AuthUserFile /etc/munin/munin-htpasswd
AuthName "**admin**"
AuthType Basic
require valid-user

```
![Munin Linux Monitoring Overview](https://www.tecmint.com/wp-content/uploads/2012/07/Munin-Linux-Monitoring-Graphs.png) Munin Linux Monitoring Overview
#### Step 5: Add Linux Client to Munin Server
Login into Linux client machine and install only `munin-node` package as shown:
```
# yum install munin-node
# dnf install munin-node      [On **Fedora 22+** versions]
# apt-get install munin-node  [On **Debian** based systems]

```

Now open `/etc/munin/munin-node.conf` configuration file and add the munin server IP address to enable data fetching from the client.
```
# vi /etc/munin/munin-node.conf

```

Add the IP address of Munin sever in the following format as shown:
```
# A list of addresses that are allowed to connect.

allow ^127\.0\.0\.1$
allow ^::1$
**allow ^192\.168\.0\.103$**

```

Finally, restart the munin client:
```
------------------ **On RHEL, CentOS and Fedora** ------------------
# service munin-node start
# chkconfig --level 35 munin-node on

------------------ **On RHEL/CentOS 7 and Fedora 22+** ------------------
# systemctl enable munin-node
# systemctl start munin-node

```

#### Step 6: Configure Munin Server to Connect Client Node
Open `/etc/munin/munin.conf` configuration file and add the following new section of remote Linux client node with the server name and IP address as shown:
```
# a simple host tree
[**munin.tecmint.com**]
    address 127.0.0.1
    use_node_name yes

[**munin-node.tecmint.com**]
    address 192.168.0.15
    use_node_name yes

```

Next, restart munin server and navigate to the `http://munin.tecmint.com/munin` page to see the new client node graphs in action.
![Munin Client Node](https://www.tecmint.com/wp-content/uploads/2016/08/Munin-Client-Node-Graphs.png)Munin Client Node
For more information and usage please visit at
Tags [linux monitoring](https://www.tecmint.com/tag/linux-monitoring/), [Munin Network Monitoring](https://www.tecmint.com/tag/munin-network-monitoring/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Debian GNU/Linux Birthday : A 23 Years of Journey and Still Counting…](https://www.tecmint.com/happy-birthday-to-debian-gnu-linux/)
Next article:
[How to Clone or Backup Linux Disk Using Clonezilla](https://www.tecmint.com/linux-centos-ubuntu-disk-cloning-backup-using-clonezilla/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#respond)** or
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
### 19 Comments
[Leave a Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/70bf657b5f83c09edd44c4abf170bfe407802c35e7e8d7bf87ff207ef224c251?s=50&d=blank&r=g)
Henry
[ June 15, 2018 at 3:50 am  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-1004610)
I cannot see my munin node on the munin server web…
I Added the host name and IP address of one of my nodes to the Munin Server in the vi **munin.conf** editor and I cannot see my munin node on the munin server web. and yes I also, added the munin server IP address to the node in the **/etc/munin/munin-nod.conf**.
Any suggestions on how to see the node on the munin server web.
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-1004610)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 15, 2018 at 11:30 am  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-1004650)
@Henry,
Have you added the IP address of Munin sever in the **/etc/munin/munin-node.conf** file with the following format as shown:
```
allow ^192\.168\.0\.103$

```

And Also have you configured Munin server to connect to client in **/etc/munin/munin.conf** file in the correct format.
```
[munin-node.tecmint.com]
    address 192.168.0.15
    use_node_name yes

```

Please check these two configurations again..
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-1004650)
  2. ![](https://secure.gravatar.com/avatar/14413cc0371a28cff6ec91461378cdaf5cb9bd3d12cf847251a507b034ba8fcb?s=50&d=blank&r=g)
Alex
[ June 30, 2017 at 1:42 am  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-897677)
wget
it should be “epel-release-7-9.noarch.rpm”
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-897677)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 30, 2017 at 4:37 pm  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-897799)
@Alex,
Thanks for notifying about new epel version, corrected the link in the article.
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-897799)
  3. ![](https://secure.gravatar.com/avatar/c89b3d73f0e0f07205a026c3ac258b868e8a0d298cc6cd630c39febb530ca874?s=50&d=blank&r=g)
vi
[ April 17, 2017 at 2:53 pm  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-884275)
Hi,
I install Munin and munin node as your post. On Munin web, I can browse the munin master info, but client. I got below error for munin client
Process Backgrounded
2017/04/17-15:30:10 Munin::Node::Server (type Net::Server::Fork) starting! pid(1622)
Resolved [*]:4949 to [::]:4949, IPv6
Not including resolved host [0.0.0.0] IPv4 because it will be handled by [::] IPv6
Binding to TCP port 4949 on host :: with IPv6
Setting gid to “0 0”
2017/04/17-15:30:13 [1622] Error output from if_virbr0:
2017/04/17-15:30:13 [1622] /etc/munin/plugins/if_virbr0: line 94: [: : integer expression expected
2017/04/17-15:30:14 [1622] Error output from if_virbr0-nic:
2017/04/17-15:30:14 [1622] /etc/munin/plugins/if_virbr0-nic: line 94: [: : integer expression expected
so I cannot see my munin node on munin server web
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-884275)
  4. ![](https://secure.gravatar.com/avatar/3be5802b8599e28d47ba4dd3e06dca2c5b64f30afc52a8a6cd598166ca843ccf?s=50&d=blank&r=g)
Vijay Kadadi
[ January 10, 2017 at 8:42 pm  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-858525)
Hello Ravi,
On my Centos 7 vm , munin URL works with https instead of http.
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-858525)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 11, 2017 at 11:19 am  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-858683)
@Vijay,
May you have SSL module install and enabled, but it should work both way http and https..
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-858683)
  5. ![](https://secure.gravatar.com/avatar/8761f8810c7042333aa9985dc2e8cd3b572a1ac8b8c8dedf637c44ee60ec8c92?s=50&d=blank&r=g)
Rana
[ November 30, 2016 at 3:55 pm  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-843172)
Hi, I want to install it in my zimbra mailserver (centos 6.8), is it possible….
thanks..
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-843172)
  6. ![](https://secure.gravatar.com/avatar/0240b800471e79b05e04203b27149d0322331edfc65eb54410de3a9a3a9e01e2?s=50&d=blank&r=g)
Parthasarathi Dash
[ September 21, 2016 at 2:47 am  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-819656)
Hi,
I want a user not to access all the munin graphs except few. how can i do that. can you please help me on this
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-819656)
  7. ![](https://secure.gravatar.com/avatar/de4b36f913868d676ea28b1c94967e72a4e42b562551f873f478c0ad4f9d4238?s=50&d=blank&r=g)
Shalini
[ April 17, 2015 at 8:16 am  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-544287)
Also provide complete,i dont think so only above steps could give munin inetrface
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-544287)
  8. ![](https://secure.gravatar.com/avatar/de4b36f913868d676ea28b1c94967e72a4e42b562551f873f478c0ad4f9d4238?s=50&d=blank&r=g)
hema
[ April 17, 2015 at 8:14 am  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-544285)
No info regarding port opening 4949…
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-544285)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 17, 2015 at 11:12 am  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-544392)
@Hema,
We’re sorry for that..we will update the article….
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-544392)
  9. ![](https://secure.gravatar.com/avatar/efce17fc3b13d2c84ce9b7a6895d6e3a795de6e30d48522da5d13c4c59f0af24?s=50&d=blank&r=g)
Mr.Right
[ February 3, 2015 at 1:23 pm  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-472587)
Hey guys !!!!
I have installed MUNIN on rhel 6 ,
But in webpage am getting only index .
No graphs etc…..
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-472587)
  10. ![](https://secure.gravatar.com/avatar/d2c6307167b3c22278a70b502fd91a229fba1665d196dd5b6bfc3d5ec4eda210?s=50&d=blank&r=g)
sudarshan
[ November 27, 2013 at 3:45 am  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-76009)
could you please explain the problem why my server unable to resolve the host address.
i am a great follower of techmint
thanks in advance
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-76009)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 27, 2013 at 4:15 am  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-76017)
add hostname in /etc/hosts file and check.
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-76017)
  11. ![](https://secure.gravatar.com/avatar/d2c6307167b3c22278a70b502fd91a229fba1665d196dd5b6bfc3d5ec4eda210?s=50&d=blank&r=g)
sudarshan
[ November 27, 2013 at 3:42 am  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-76008)
[root@server ~]# wget
–2013-11-26 21:43:32–
Resolving download.fedoraproject.org… failed: Temporary failure in name resolution.
wget: unable to resolve host address `download.fedoraproject.org’
[root@server ~]#
[root@server ~]#
I am Getting above error while giving the first command as mentioned in procedure
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-76008)
  12. ![](https://secure.gravatar.com/avatar/a19418686a4c7e1ffb95e61193dca88315f03af5ee61fe775b458b87c97442dd?s=50&d=blank&r=g)
Minu
[ November 25, 2013 at 10:49 pm  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-75453)
After the installation using the above steps password authentication enabled. you can configure Authentication details using the following command.
—
htpasswd -c /etc/munin/munin-htpasswd Munin
Enter the correct password
—
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-75453)
  13. ![](https://secure.gravatar.com/avatar/a334a06820e2f7ac0bd29a1af85d2fb857de1859164484d849ebe604f478ee53?s=50&d=blank&r=g)
Elavarasan
[ August 17, 2013 at 10:59 pm  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-34234)
Hi,
I have installed Munin in our server successfully but when i browse in browser it’s asking username and password, so what is the default username and password for munin
Thanks,
Ela
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-34234)
     * ![](https://secure.gravatar.com/avatar/830e887f6747f7994d44041bb95cf09e795637eb7af7f59274cdfa37c56f8b12?s=50&d=blank&r=g)
JF
[ November 16, 2013 at 12:42 am  ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-70912)
Hi Ela,
That’s per file /etc/httpd/conf.d/munin.conf that such authentication is required.
You can easily disable it my modifying this conf file. Do not hesitate to look at Apache Http doc to get help on the conf file contents.
[Reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#comment-70912)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/#respond)
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
[The Power of Linux “History Command” in Bash Shell](https://www.tecmint.com/history-command-examples/)
[How to Find a Specific String or Word in Files and Directories](https://www.tecmint.com/find-a-specific-string-or-word-in-files-and-directories/)
[Transfer.sh – Easy File Sharing from Linux Commandline](https://www.tecmint.com/file-sharing-from-linux-commandline/)
[7 Best Tools to Compare Text Files in Linux](https://www.tecmint.com/compare-files-linux/)
[How to Run a Command Multiple Times in Linux](https://www.tecmint.com/run-linux-command-multiple-times/)
[Browsh – A Modern Text Browser That Play Videos and Everything](https://www.tecmint.com/browsh-text-web-browser-for-linux/)
## Linux Server Monitoring Tools
[Monitorix – A Linux System and Network Monitoring Tool](https://www.tecmint.com/monitorix-linux-network-monitoring-tool/)
[How To Install Elasticsearch, Logstash, and Kibana (ELK Stack) on RHEL](https://www.tecmint.com/install-elasticsearch-logstash-and-kibana-elk-stack-on-centos-rhel-7/)
[iftop – A Real Time Linux Network Bandwidth Monitoring Tool](https://www.tecmint.com/iftop-linux-network-bandwidth-monitoring-tool/)
[Cpustat – Monitors CPU Utilization by Running Processes in Linux](https://www.tecmint.com/cpustat-monitors-cpu-utilization-by-processes-in-linux/)
[Icinga: A Next Generation Open Source ‘Linux Server Monitoring’ Tool for RHEL/CentOS 7.0](https://www.tecmint.com/install-icinga-in-centos-7/)
[How to Monitor System Usage, Outages and Troubleshoot Linux Servers – Part 9](https://www.tecmint.com/linux-system-monitoring-troubleshooting-tools/)
## Learn Linux Tricks & Tips
[How to Find Difference Between Two Directories Using Diff and Meld Tools](https://www.tecmint.com/compare-find-difference-between-two-directories-in-linux/)
[Learn The Basics of How Linux I/O (Input/Output) Redirection Works](https://www.tecmint.com/linux-io-input-output-redirection-operators/)
[4 Useful Tips on mkdir, tar and kill Commands in Linux](https://www.tecmint.com/mkdir-tar-and-kill-commands-in-linux/)
[How to Find MySQL, PHP and Apache Configuration Files](https://www.tecmint.com/find-mysql-php-apache-configuration-files/)
[How to Download and Extract Tar Files with One Command](https://www.tecmint.com/download-and-extract-tar-files-with-one-command/)
[How to Create Multiple User Accounts in Linux](https://www.tecmint.com/create-multiple-user-accounts-in-linux/)
## Best Linux Tools
[6 Best Linux Boot Loaders](https://www.tecmint.com/best-linux-boot-loaders/)
[8 Best HTML & CSS Code Editors for Linux](https://www.tecmint.com/html-css-editors-linux/)
[Universal Package Managers for Linux: Snap, Flatpak, and AppImage](https://www.tecmint.com/cross-distribution-package-managers-for-linux/)
[11 Best Self-Hosted Alternatives to Google Photos](https://www.tecmint.com/google-photos-alternatives/)
[6 Most Notable Open Source Centralized Log Management Tools](https://www.tecmint.com/open-source-centralized-linux-log-management-tools/)
[11 Best IP Address Management Tools for Linux Network](https://www.tecmint.com/ip-address-management-tools-for-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-munin-network-monitoring-in-rhel-centos-fedora/ "Scroll back to top")
Search for:
