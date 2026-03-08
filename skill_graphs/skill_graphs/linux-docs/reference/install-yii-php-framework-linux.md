[Skip to content](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/)
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
  * [Pro Courses](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/)
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
  * [Pro Courses](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/)
# Install Glances, InfluxDB and Grafana to Monitor CentOS 7
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: August 29, 2018 Read Time: 5 minsCategories [CentOS](https://www.tecmint.com/category/linux-distros/centos/), [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [16 Comments](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comments)
[Glances](https://www.tecmint.com/glances-an-advanced-real-time-system-monitoring-tool-for-linux/) is a free open source, modern, cross-platform, real-time [top](https://www.tecmint.com/12-top-command-examples-in-linux/) and [htop-like](https://www.tecmint.com/install-htop-linux-process-monitoring-for-rhel-centos-fedora/) monitoring tool with advanced features. It can run in different modes: as a standalone, in client/server mode and [in web server mode](https://www.tecmint.com/glances-monitor-remote-linux-in-web-server-mode/).
**InfluxDB** is an open source and scalable time series database for metrics, events, and real-time analytics.
[Grafana](https://www.tecmint.com/install-grafana-analytics-in-centos-ubuntu-debian/) is an open source, feature rich, powerful, elegant and highly-extensible, cross-platform tool for monitoring and metric analytics, with beautiful and customizable dashboards. It is a de facto software for data analytics.
In this article, we will explain how to install and configure **Glances** , **InfluxDB** and **Grafana** to monitor performance of a **CentOS 7** server.
### Step 1: Install Glances in CentOS 7
**1.** First start by installing latest stable version of **glances** (**v2.11.1**) using [PIP](https://www.tecmint.com/install-pip-in-linux/). If you don’t have **pip** , install it as follows, including **Python-headers** required for installing **psutil**.
```
# yum install python-pip python-devel

```

**2.** Once you have **PIP** and the **Python-headers** , run the following command to install the latest stable version of **glances** and verify the version.
```
# pip install glances
# glances -V

**Glances v2.11.1 with psutil v5.4.7**

```

Alternatively, if you already have **glances** installed, you can upgrade it to the latest version using following command.
```
# pip install --upgrade glances

```

**3.** Now you need to start glances via **systemd** so that it runs as a service. Create a new unit by creating a file called **glances.service** in **/etc/systemd/system/**.
```
# vim /etc/systemd/system/glances.service

```

Copy and paste the following configuration in the file **glances.service**. The `--config` specifies the config file, `--export-influxdb` option tells glances to export stats to an InfluxDB server and the `--disable-ip` option disables the IP module.
```
[Unit]
Description=Glances
After=network.target influxd.service

[Service]
ExecStart=/usr/bin/glances --config /home/admin/.config/glances/glances.conf --quiet --export-influxdb --disable-ip
Restart=on-failure
RestartSec=30s
TimeoutSec=30s

[Install]
WantedBy=multi-user.target

```

Save the file and close it.
**4.** Then reload systemd manager configuration, start the glances service, view its status, and enable it to auto-start at boot time.
```
# systemctl daemon-reload
# systemctl start glances.service
# systemctl status glances.service
# systemctl enable glances.service

```

**5.** Next, you need to download the glances configuration file provided by the developer using [wget command](https://www.tecmint.com/10-wget-command-examples-in-linux/) as shown.
```
# mkdir ~/.config/glances/
# wget https://raw.githubusercontent.com/nicolargo/glances/master/conf/glances.conf -P ~/.config/glances/

```

**6.** In order to export **Glances** stats to an **InfluxDB** database, you need the **Python InfluxdDB** lib, which you can install it using pip command.
```
# sudo pip install influxdb

```

### Step 2: Install InfluxDB in CentOS 7
**7.** Next, you need to add the InfluxDB Yum repository to install latest vesrion of **InfluxDB** package as shown.
```
# cat <<EOF | sudo tee /etc/yum.repos.d/influxdb.repo
[influxdb]
name = InfluxDB Repository - RHEL \$releasever
baseurl = https://repos.influxdata.com/rhel/\$releasever/\$basearch/stable
enabled = 1
gpgcheck = 1
gpgkey = https://repos.influxdata.com/influxdb.key
EOF

```

**8.** After adding the repository to the YUM configuration, install the **InfluxDB** package by running.
```
# yum install influxdb

```

**9.** Next, start the **InfluxDB** service via systemd, confirm that it is running by viewing its status and enable it to auto-start at system boot.
```
# systemctl start influxdb
# systemctl status influxdb
# systemctl enable influxdb

```

**10.** By default, InfluxDB uses TCP port **8086** for client-server communication over InfluxDB’s HTTP API, you need to open this port in your firewall using the firewall-cmd.
```
# firewall-cmd --add-port=8086/tcp --permanent
# firewall-cmd --reload

```

**11.** Next, you need to create a database in **InfluxDB** for storing data from **glances**. The **influx** command which is included in the InfluxDB packages is the simplest way to interact with the database. So execute **influx** to start the CLI and automatically connect to the local InfluxDB instance.
```
# influx

```

Run the following commands to create a database called **glances** and view available databases.
```
Connected to http://localhost:8086 version 1.6.2
InfluxDB shell version: 1.6.2
> **CREATE DATABASE glances**
> **SHOW DATABASES**
name: databases
name
----
_internal
glances
>

```

To exit the **InfluxQL** shell, type **exit** and hit **Enter**.
### Step 3: Install Grafana in CentOS 7
**12.** Now, install **Grafana** from its official YUM repository, start by adding the following configuration to **/etc/yum.repos.d/grafana.repo** repository file.
```
[grafana]
name=grafana
baseurl=https://packagecloud.io/grafana/stable/el/7/$basearch
repo_gpgcheck=1
enabled=1
gpgcheck=1
gpgkey=https://packagecloud.io/gpg.key https://grafanarel.s3.amazonaws.com/RPM-GPG-KEY-grafana
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt

```

**13.** After adding the repository to the YUM configuration, install the **Grafana** package by running.
```
# yum install grafana

```

**14.** Once you have installed **Grafana** , reload systemd manager configuration, start the grafana server, check if the service is up and running by viewing its status and enable it to auto-start at boot time.
```
# systemctl daemon-reload
# systemctl start grafana-server
# systemctl status grafana-server
# systemctl enable grafana-server

```

**15.** Next, open port **3000** which **Grafana** server listens on, in your firewall using the firewall-cmd.
```
# firewall-cmd --add-port=3000/tcp --permanent
# firewall-cmd --reload

```

### Step 4: Monitor CentOS 7 Server Metrics Via Grafana
**16.** At this point, you can use the following URL to access **Grafana** web interface, which will redirect to the login page, use the default credentials to login.
```
URL: **http://SERVER_IP:3000**
Username: **admin**
Password: **admin**

```

You will be asked to create a new password, once you have done that, you will be redirected to the home dashboard, as shown in the screenshot below.
![Grafana Admin Login](https://www.tecmint.com/wp-content/uploads/2018/08/Grafana-Login.png)Grafana Admin Login ![Grafana Set Admin Password](https://www.tecmint.com/wp-content/uploads/2018/08/Grafana-Set-Admin-Password.png)Grafana Set Admin Password ![Grafana Dashboard](https://www.tecmint.com/wp-content/uploads/2018/08/Grafana-Dashboard.png)Grafana Dashboard
**17.** Next, click on **Create your first data source** , which should be an InfluxDB database. Under **Settings** , enter a suitable name e.g **Glances Import** , then use the following values for the other two important variables (**HTTP URL** and **InfluxDB Database**) as shown in the screenshot.
```
HTTP URL: **http://localhost:8086**
InfluxDB Details - Database: **glances**

```

Then click on **Save & Test** to connect to the data source. You should receive a feedback indicating “**Data source is working** ”.
![Create Data Source](https://www.tecmint.com/wp-content/uploads/2018/08/Create-Data-Source.png)Create Data Source
**18.** Now you need to import the **Glances** dashboard. Click on the plus `(+)` and go to **Import** as shown in the screenshot.
![Import Glances](https://www.tecmint.com/wp-content/uploads/2018/08/Import-Glances.png)Import Glances
17. You will need either the **Glances Dashboard URL** or ID or upload its `.JSON` file which you can find from **Grafana.com**. In this case, we will use the **Glances Dashboard** created by the developer of Glances, its URL is **https://grafana.com/dashboards/2387** or ID is **2387**.
![Import Glances Dashboard](https://www.tecmint.com/wp-content/uploads/2018/08/Import-Glances-Dashboard.png)Import Glances Dashboard
**18.** Once the Grafana dashboard has been loaded, under options, find glances and choose an InluxDB data source (**Glances Import**) which you created earlier on, then click on **Import** as shown in the following screenshot.
![Import Glances Settings](https://www.tecmint.com/wp-content/uploads/2018/08/Import-Glances-Settings.png)Import Glances Settings
**19.** After successfully importing the **Glances** dashboard, you should be able to watch graphs showing metrics from your server as provided by glances via influxdb.
![Monitor CentOS Using Grafana](https://www.tecmint.com/wp-content/uploads/2018/08/Monitor-CentOS-Using-Grafana.png)Monitor CentOS Using Grafana
That’s all for now! In this article, we have explained how to monitor CentOS 7 server with Glances, InfluxDB and Grafana. If you have any queries, or information to share, use the comment form below to do so.
Tags [CentOS Server Monitoring](https://www.tecmint.com/tag/centos-server-monitoring/), [CentOS Tips](https://www.tecmint.com/tag/centos-tips/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Setup Local HTTP Yum Repository on CentOS 7](https://www.tecmint.com/setup-local-http-yum-repository-on-centos-7/)
Next article:
[How to Install Mod_GeoIP for Apache in RHEL and CentOS](https://www.tecmint.com/install-mod_geoip-for-apache-in-centos/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#respond)** or
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
### 16 Comments
[Leave a Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/825c1a06a244c934cc27fcc542d7ae4d530b1d7435da59a1e02f720ab6d78575?s=50&d=blank&r=g)
Adrian
[ September 7, 2020 at 6:19 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1361319)
```
[root@mail ~]# systemctl status glances

```

##### Sample Output
```
● glances.service - Glances
   Loaded: loaded (/etc/systemd/system/glances.service; enabled; vendor preset: disabled)
   Active: activating (auto-restart) (Result: exit-code) since Mon 2020-09-07 14:40:36 CEST; 16s ago
  Process: 3347 ExecStart=/usr/bin/glances --config /home/adrian/.config/glances/glances.conf --quiet --export-influxdb --disable-plugin ip (code=exited, status=2)
 Main PID: 3347 (code=exited, status=2)

Sep 07 14:40:36 mail.sysyadmin.info.pl systemd[1]: glances.service: main process exited, code=exited, status=2/INVALIDARGUMENT
Sep 07 14:40:36 mail.sysyadmin.info.pl systemd[1]: Unit glances.service entered failed state.
Sep 07 14:40:36 mail.sysyadmin.info.pl systemd[1]: glances.service failed.

glances: error: unrecognized arguments: --export-influxdb
Sep  7 14:44:39 mail systemd[1]: glances.service: main process exited, code=exited, status=2/INVALIDARGUMENT
Sep  7 14:44:39 mail systemd[1]: Unit glances.service entered failed state.
Sep  7 14:44:39 mail systemd[1]: glances.service failed.
Sep  7 14:44:48 mail systemd[1]: Reloading.
Sep  7 14:44:55 mail systemd[1]: Stopped Glances.
Sep  7 14:45:01 mail systemd[1]: Started Glances.
Sep  7 14:45:03 mail glances[3458]: Traceback (most recent call last):
Sep  7 14:45:03 mail glances[3458]: File "/usr/bin/glances", line 9, in
Sep  7 14:45:03 mail glances[3458]: load_entry_point('Glances==3.1.5', 'console_scripts', 'glances')()
Sep  7 14:45:03 mail glances[3458]: File "/usr/lib/python2.7/site-packages/glances/__init__.py", line 143, in main
Sep  7 14:45:03 mail glances[3458]: start(config=config, args=args)
Sep  7 14:45:03 mail glances[3458]: File "/usr/lib/python2.7/site-packages/glances/__init__.py", line 108, in start
Sep  7 14:45:03 mail glances[3458]: mode = GlancesMode(config=config, args=args)
Sep  7 14:45:03 mail glances[3458]: File "/usr/lib/python2.7/site-packages/glances/standalone.py", line 51, in __init__
Sep  7 14:45:03 mail glances[3458]: self.stats = GlancesStats(config=config, args=args)
Sep  7 14:45:03 mail glances[3458]: File "/usr/lib/python2.7/site-packages/glances/stats.py", line 48, in __init__
Sep  7 14:45:03 mail glances[3458]: self.load_modules(self.args)
Sep  7 14:45:03 mail glances[3458]: File "/usr/lib/python2.7/site-packages/glances/stats.py", line 103, in load_modules
Sep  7 14:45:03 mail glances[3458]: self.load_exports(args=args)
Sep  7 14:45:03 mail glances[3458]: File "/usr/lib/python2.7/site-packages/glances/stats.py", line 178, in load_exports
Sep  7 14:45:03 mail glances[3458]: export_module = __import__(self._exports_all[export_name])
Sep  7 14:45:03 mail glances[3458]: File "/usr/lib/python2.7/site-packages/glances/exports/glances_influxdb.py", line 27, in
Sep  7 14:45:03 mail glances[3458]: from influxdb import InfluxDBClient
Sep  7 14:45:03 mail glances[3458]: ImportError: No module named influxdb
Sep  7 14:45:05 mail systemd[1]: glances.service: main process exited, code=exited, status=1/FAILURE
Sep  7 14:45:05 mail systemd[1]: Unit glances.service entered failed state.
Sep  7 14:45:05 mail systemd[1]: glances.service failed.
Sep  7 14:45:05 mail dbus[498]: [system] Activating service name='org.fedoraproject.Setroubleshootd' (using servicehelper)
Sep  7 14:45:07 mail dbus[498]: [system] Successfully activated service 'org.fedoraproject.Setroubleshootd'
Sep  7 14:45:10 mail setroubleshoot: SELinux is preventing /usr/bin/python2.7
from read access on the file disable_ipv6. For complete SELinux messages run: sealert -l 66e1e5bf-322d-4bd9-911e
-c580274a0951

```

Seems I need to play with SELinux using my article from my own website LOL.
```
cat /etc/systemd/system/glances.service
[Unit]
Description=Glances
After=network.target influxd.service

[Service]
ExecStart=/usr/bin/glances --config /home/adrian/.config/glances/glances.conf --quiet --export-influxdb --disable-plugin ip
Restart=on-failure
RestartSec=30s
TimeoutSec=30s

[Install]
WantedBy=multi-user.target

```
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1361319)
     * ![](https://secure.gravatar.com/avatar/825c1a06a244c934cc27fcc542d7ae4d530b1d7435da59a1e02f720ab6d78575?s=50&d=blank&r=g)
Adrian
[ September 7, 2020 at 6:24 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1361321)
Additionally, log from /tmp/glances-root.log
```
2020-09-07 14:49:16,798 -- INFO -- Start Glances 3.1.5
2020-09-07 14:49:16,800 -- INFO -- CPython 2.7.5 and psutil 5.6.7 detected
2020-09-07 14:49:32,041 -- INFO -- Start Glances 3.1.5
2020-09-07 14:49:32,044 -- INFO -- CPython 2.7.5 and psutil 5.6.7 detected
2020-09-07 14:49:32,051 -- INFO -- Search glances.conf file in /home/adrian/.config/glances/glances.conf
2020-09-07 14:49:32,059 -- INFO -- Read configuration file '/home/adrian/.config/glances/glances.conf'
2020-09-07 14:49:32,072 -- INFO -- Start GlancesStandalone mode
2020-09-07 14:49:32,303 -- WARNING -- Error loading Docker Python Lib. Docker plugin is disabled (No module named docker)
2020-09-07 14:49:32,304 -- ERROR -- docker plugin - Can not connect to Docker (global name 'docker' is not defined)
2020-09-07 14:49:32,305 -- ERROR -- Scandir not found. Please use Python 3.5+ or install the scandir lib
2020-09-07 14:49:32,306 -- WARNING -- Missing Python Lib (No module named py3nvml.py3nvml), Nvidia GPU plugin is disabled
2020-09-07 14:49:32,309 -- WARNING -- Missing Python Lib (No module named netifaces), IP plugin is disabled
2020-09-07 14:49:32,345 -- WARNING -- Sparklines module not found (No module named sparklines)
2020-09-07 14:49:32,346 -- WARNING -- UTF-8 is mandatory for sparklines (encode() argument 1 must be string, not None)
2020-09-07 14:49:32,346 -- WARNING -- Missing Python Lib (No module named cpuinfo), Quicklook plugin will not display CPU info
2020-09-07 14:49:32,347 -- WARNING -- Missing Python Lib (No module named pymdstat), Raid plugin is disabled
2020-09-07 14:49:32,354 -- WARNING -- Missing Python Lib (No module named pySMART), HDD Smart plugin is disabled
2020-09-07 14:49:32,357 -- WARNING -- Missing Python Lib (No module named wifi.scan), Wifi plugin is disabled

```
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1361321)
  2. ![](https://secure.gravatar.com/avatar/825c1a06a244c934cc27fcc542d7ae4d530b1d7435da59a1e02f720ab6d78575?s=50&d=blank&r=g)
Adrian
[ September 7, 2020 at 6:12 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1361318)
Can you review the post? Still have issues with the glances. Even after reading all comments and changing the entry in service for glances.
None of the solutions works.
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1361318)
  3. ![](https://secure.gravatar.com/avatar/825c1a06a244c934cc27fcc542d7ae4d530b1d7435da59a1e02f720ab6d78575?s=50&d=blank&r=g)
Adrian
[ September 7, 2020 at 5:32 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1361309)
Proper grafana repo:
```
[grafana]
name=grafana
baseurl=https://packages.grafana.com/oss/rpm
repo_gpgcheck=1
enabled=1
gpgcheck=1
gpgkey=https://packages.grafana.com/gpg.key
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt

```
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1361309)
  4. ![](https://secure.gravatar.com/avatar/3ac01eb74c54873225a5ac968fa6feb99f2be39e76e25d0e974895abfa2355f3?s=50&d=blank&r=g)
Sean Chiarot
[ September 20, 2019 at 10:16 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1249243)
Hmmm, I followed this but all I see is ‘No Data points’
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1249243)
  5. ![](https://secure.gravatar.com/avatar/772a89cfe31c8675bc955a28a3f665013faf35f17bc2e643e5bd7fff6f26c243?s=50&d=blank&r=g)
Marcos
[ January 8, 2019 at 6:05 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1092424)
Nice article.
For Glances v 3 they have change the syntax, the command it’s now:
`ExecStart=/usr/bin/glances --config /home/admin/.config/glances/glances.conf --quiet --export influxdb --disable-plugin ip`
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1092424)
  6. ![](https://secure.gravatar.com/avatar/17ae501f5395fa4b1f85e3347f3a82a52348748575b261c1d8c79c8070cee507?s=50&d=blank&r=g)
paulflammes
[ October 23, 2018 at 1:23 am  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1051834)
Why use 3 programs and a complicated flow of data instead of using netdata? Thanks in advance
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1051834)
  7. ![](https://secure.gravatar.com/avatar/35c72fdb03140216818ec51d8e57275249aea468ec089354070acc59f7fe7f01?s=50&d=blank&r=g)
Jakob
[ September 30, 2018 at 4:34 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1041798)
Thank you very much! I used it (with modifications) on Ubuntu 16.04.5: It works generally very well!
But some data series aren’t displayed! To example disk I/O and the network RX/TX …
Have somebody an idea how to fix this?
Thank you!
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1041798)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ October 1, 2018 at 11:59 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1042198)
@Jakob
You can contact the developer of glances for a possible solution:
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1042198)
       * ![](https://secure.gravatar.com/avatar/35c72fdb03140216818ec51d8e57275249aea468ec089354070acc59f7fe7f01?s=50&d=blank&r=g)
Jakob
[ October 3, 2018 at 4:14 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1042829)
I had found the error: A typical “**greenhorn** ” mistake: I haven’t adjusted the InfluxDB query.
Now all is going pretty well, thank you very much for the article!
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1042829)
         * ![](https://secure.gravatar.com/avatar/1b42053a4c4e0539fe5a762408ab2e4fe312b64fa7b25c0fd14f53b0dc7260de?s=50&d=blank&r=g)
Rainbow Dashie
[ October 16, 2018 at 6:55 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1049096)
What did you use as your query? I can’t seem to find any references what query to use.
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1049096)
  8. ![](https://secure.gravatar.com/avatar/c8a7342710f20c7b6adb1699de5303a47e6ffb6cf1b92c624022178fe45711b2?s=50&d=blank&r=g)
Max
[ August 28, 2018 at 9:54 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1028842)
Process: 3043 ExecStart=/usr/bin/glances –config /home/admin/.config/glances/glances.conf –quiet –export-influxdb – -disable-ip (code=exited, status=2)
Main PID: 3043 (code=exited, status=2)
Aug 28 16:22:25 testmachine systemd[1]: Unit glances.service entered failed state.
Aug 28 16:22:25 testmachine systemd[1]: glances.service failed.
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1028842)
     * ![](https://secure.gravatar.com/avatar/307a36a08c1c3eee64af4b9e842b3175f7d604e11a5ae340076f12c77396b5b6?s=50&d=blank&r=g)
Stephen
[ August 29, 2018 at 12:13 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1029111)
Ye there’s a typo in there I had this as well.
There’s a space between the 2 dashes at disable-ip and the config location assumes you are user ‘**admin** ‘.
Just remove the dashes and fix the username.
`
 ExecStart=/usr/bin/glances --config /home/YourUsername/.config/glances/glances.conf --quiet --export-influxdb  --disable-ip
 `
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1029111)
       * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 29, 2018 at 12:19 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1029115)
@Stephen,
Thanks for pointing out that typo, we’ve corrected the command in the article..
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1029115)
  9. ![](https://secure.gravatar.com/avatar/307a36a08c1c3eee64af4b9e842b3175f7d604e11a5ae340076f12c77396b5b6?s=50&d=blank&r=g)
Stephen
[ August 28, 2018 at 4:18 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1028718)
Very interesting!
Going to give this a go on debian.
Thanks for the write-up :)
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1028718)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ August 29, 2018 at 12:30 pm  ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1029119)
@Stephen
Welcome, many thanks for the feedback.
[Reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#comment-1029119)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/#respond)
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
[How to Determine and Fix Boot Issues in Linux](https://www.tecmint.com/find-and-fix-linux-boot-issues/)
[Set Date and Time for Each Command You Execute in Bash History](https://www.tecmint.com/display-linux-command-history-with-date-and-time/)
[How to Find a Process Name Using PID Number in Linux](https://www.tecmint.com/find-process-name-pid-number-linux/)
[How to Get Total Inodes of Root Partition](https://www.tecmint.com/check-inodes-in-linux/)
[4 Ways to Find Server Public IP Address in Linux Terminal](https://www.tecmint.com/find-linux-server-public-ip-address/)
[How to Reconfigure Installed Package in Ubuntu and Debian](https://www.tecmint.com/dpkg-reconfigure-installed-package-in-ubuntu-debian/)
## Linux Server Monitoring Tools
[Icinga: A Next Generation Open Source ‘Linux Server Monitoring’ Tool for RHEL/CentOS 7.0](https://www.tecmint.com/install-icinga-in-centos-7/)
[How to Add Windows Host to Nagios Monitoring Server](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/)
[Duf – A Better Linux Disk Monitoring Utility](https://www.tecmint.com/duf-linux-disk-monitoring-utility/)
[rtop – An Interactive Tool to Monitor Remote Linux Server Over SSH](https://www.tecmint.com/rtop-monitor-remote-linux-server-over-ssh/)
[Configure Collectd as a Central Monitoring Server for Clients](https://www.tecmint.com/configure-collectd-as-central-monitoring-server-for-clients/)
[Htop – An Interactive Process Viewer for Linux](https://www.tecmint.com/htop-linux-process-monitoring/)
## Learn Linux Tricks & Tips
[How to Send a Message to Logged Users in Linux Terminal](https://www.tecmint.com/send-a-message-to-logged-users-in-linux-terminal/)
[How to Clear BASH Command Line History in Linux](https://www.tecmint.com/clear-command-line-history-in-linux/)
[How to Copy File Permissions and Ownership to Another File in Linux](https://www.tecmint.com/copy-file-permissions-and-ownership-to-another-file-in-linux/)
[10 Useful Sudoers Configurations for Setting ‘sudo’ in Linux](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/)
[How to Configure Custom SSH Connections to Simplify Remote Access](https://www.tecmint.com/configure-custom-ssh-connection-in-linux/)
[How to View Colored Man Pages in Linux](https://www.tecmint.com/view-colored-man-pages-in-linux/)
## Best Linux Tools
[Universal Package Managers for Linux: Snap, Flatpak, and AppImage](https://www.tecmint.com/cross-distribution-package-managers-for-linux/)
[6 Best Linux Boot Loaders](https://www.tecmint.com/best-linux-boot-loaders/)
[My Favorite Command Line Editors for Linux – What’s Your Editor?](https://www.tecmint.com/linux-command-line-editors/)
[5 Online Tools for Generating and Testing Cron Jobs for Linux](https://www.tecmint.com/online-cron-job-generator-and-tester-for-linux/)
[Top 6 Linux Apps You Should Install This Week (Sept 15-21)](https://www.tecmint.com/linux-apps-to-try-this-week-september-15-21/)
[18 Best NodeJS Frameworks for App Development in 2023](https://www.tecmint.com/best-nodejs-frameworks-for-developers/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-glances-influxdb-grafana-to-monitor-centos-7/ "Scroll back to top")
Search for:
