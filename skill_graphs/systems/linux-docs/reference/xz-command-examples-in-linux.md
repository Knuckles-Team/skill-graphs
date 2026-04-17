[Skip to content](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/)
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
  * [Pro Courses](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/ "Linux Online Courses")
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


[](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/)
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
  * [Pro Courses](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/ "Linux Online Courses")
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


[](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/)
# How to Monitor Apache Performance using Netdata on CentOS 7
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: June 22, 2018 Read Time: 3 minsCategories [Apache](https://www.tecmint.com/category/web-servers/apache/), [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [3 Comments](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/#comments)
[Netdata](https://www.tecmint.com/netdata-real-time-linux-performance-network-monitoring-tool/) is a free open source, simple yet powerful, and effective real-time system performance monitoring tool for Linux, FreeBSD and MacOS. It supports various plugins for monitoring general server status, applications, web services such as **Apache** or **Nginx HTTP** server and so much more.
**Read Also** : [How to Monitor Nginx Performance Using Netdata on CentOS 7](https://www.tecmint.com/monitor-nginx-performance-using-netdata-on-centos-7/)
In this article, we will explain how to monitor **Apache HTTP** server performance using **Netdata** performance monitoring tool on a **CentOS 7** or **RHEL 7** distribution. At the end of this article, you will be able to watch visualizations of requests, bandwidth, workers, and other Apache server metrics.
#### Requirements:
  1. A [CentOS 7 Server](https://www.tecmint.com/centos-7-3-installation-guide/) or [RHEL 7 Server](https://www.tecmint.com/red-hat-enterprise-linux-7-3-installation-guide/) with Minimal Install.
  2. [Apache HTTP server installation](https://www.tecmint.com/install-apache-on-centos-7/) with [mod_status module enabled](https://www.tecmint.com/check-apache-modules-enabled/).


### Step 1: Install Apache on CentOS 7
**1.** First start by installing **Apache HTTP** server from the default software repositories using the [YUM package manager](https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/).
```
# yum install httpd

```

**2.** After you have installed **Apache** web server, start it for the first time, check if it is up and running, and enable it to start automatically at system boot using following commands.
```
# systemctl start httpd
# systemctl enable httpd
# systemctl status httpd

```

**3.** If you are running a firewall for example [firewalld](https://www.tecmint.com/configure-firewalld-in-centos-7/), you need to open the ports **80** and **443** to allow web traffic to **Apache** via **HTTP** and **HTTPS** respectively, using the commands below.
```
# firewall-cmd --zone=public --permanent --add-port=80/tcp
# firewall-cmd --zone=public --permanent --add-port=443/tcp
# firewall-cmd --reload

```

### Step 2: Enable Mod_Status Module in Apache
**4.** In this step, you need to enable and configure **mod_status** module in **Apache** , this is required by **Netdata** for gathering server status information and statistics.
Open the file **/etc/httpd/conf.modules.d/00-base.conf** file using your favorite editor.
```
# vim /etc/httpd/conf.modules.d/00-base.conf

```

And ensure that the line below is uncommented to enable **mod_status** module, as shown in the screenshot.
![Enable Mod_Status Module in Apache](https://www.tecmint.com/wp-content/uploads/2018/06/Enable-mod_status-Module-in-Apache.png)Enable Mod_Status Module in Apache
**5.** Once you’ve enabled **mod_status** , next you need to create a `server-status.conf` configuration file for the Apache server status page.
```
# vim /etc/httpd/conf.d/server-status.conf

```

Add the following configuration inside the file.
```
<Location "/server-status">
    SetHandler server-status
    #Require host localhost           #uncomment to only allow requests from localhost
</Location>

```

Save the file and close. Then restart the Apache HTTPD service.
```
# systemctl restart httpd

```

**6.** Next, you need to verify that the Apache server status and statistics page is working well by using a [command-line web browser](https://www.tecmint.com/command-line-web-browsers/) such as **lynx** as shown.
```
# yum install lynx
# lynx http://localhost/server-status

```
![Check Apache Server Status](https://www.tecmint.com/wp-content/uploads/2018/06/Check-Apache-Server-Status.png)Check Apache Server Status
### Step 3: Install Netdata on CentOS 7
**7.** Fortunately, there is a kickstarter shell script for painlessly installing **netdata** from its github repository. This one-liner script downloads a second script which checks your Linux distribution and installs the required system packages for building netdata, then downloads the latest netdata source tree; builds and installs it on your server.
You can start the kickstarter script as shown, the **all** flag allows for installing required packages for all netdata plugins including the ones for Apache HTTP server.
```
# bash <(curl -Ss https://my-netdata.io/kickstart.sh) all

```

Note that if your not administering your system as **root** , you will be prompted to enter your user password for [sudo command](https://www.tecmint.com/su-vs-sudo-and-how-to-configure-sudo-in-linux/), and you will also be asked to confirm a number of functions by pressing **[Enter]**.
![Install Netdata on CentOS 7](https://www.tecmint.com/wp-content/uploads/2018/06/Install-Netdata-on-CentOS-7.png)Install Netdata on CentOS 7
**8.** Once the script has completed building and installing netdata, it will automatically start the **netdata** service via **systemd** service manager and enables it to start at system boot.
![Netdata Installation Summary](https://www.tecmint.com/wp-content/uploads/2018/06/Netdata-Installation-Summary.png)Netdata Installation Summary
By default, **netdata** listens on port **19999** , you will access the web UI using this port. So, open port **19999** in the firewall to access the netdata web UI.
```
# firewall-cmd --permanent --add-port=19999/tcp
# firewall-cmd --reload

```

### Step 4: Configure Netdata to Monitor Apache Performance
**9.** The netdata configuration for Apache plugin is **/etc/netdata/python.d/apache.conf** , this file is written in **YaML** format, you can open it using your favorite editor.
```
# vim /etc/netdata/python.d/apache.conf

```

The default configuration is just enough to get you started with monitoring your Apache HTTP server.
![Netdata Configuration for Apache](https://www.tecmint.com/wp-content/uploads/2018/06/netdata-config-for-apache-plugin.png)Netdata Configuration for Apache
However, if you have read the documentation, and made any changes to it, restart the **netdata** service to effect the changes.
```
# systemctl restart netdata

```

### Step 5: Monitor Apache Performance Using Netdata
**10.** Next, open a web browser and use the following URL to access the netdata web UI.
```
http://domain_name:19999
OR
http://SERVER_IP:19999

```

From the netdata dashboard, search for “**Apache local** ” on the right hand side list of plugins, and click on it to start monitoring your Apache server. You will be able to watch visualizations of requests, bandwidth, workers, and other server statistics, as shown in the following screenshot.
![Monitor Apache Performance Using Netdata](https://www.tecmint.com/wp-content/uploads/2018/06/Monitor-Apache-Performance-using-netdata.png)Monitor Apache Performance Using Netdata
**Netdata Github repository** :
That’s all! In this article, we’ve explained how to monitor **Apache** performance using **Netdata** on **CentOS 7**. If you have any questions or additional thoughts to share, please reach us via the comment form below.
Tags [Netdata Monitoring Tool](https://www.tecmint.com/tag/netdata-monitoring-tool/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[4 Ways to Check CentOS or RHEL Version](https://www.tecmint.com/check-centos-version/)
Next article:
[zstd – A Fast Data Compression Algorithm Used By Facebook](https://www.tecmint.com/zstd-fast-data-compression-algorithm-used-by-facebook/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/#respond)** or
## Related Posts
[![Timeout HTTP Requests in Linux](https://www.tecmint.com/wp-content/uploads/2025/01/Timeout-HTTP-Requests-in-Linux.png)](https://www.tecmint.com/timeout-http-requests/ "How to Timeout HTTP Requests in Linux")
[How to Timeout HTTP Requests in Linux](https://www.tecmint.com/timeout-http-requests/)
[![Create Apache Virtual Host in RHEL](https://www.tecmint.com/wp-content/uploads/2014/07/Create-Apache-Virtual-Host-in-RHEL.webp)](https://www.tecmint.com/apache-virtual-hosting-in-centos/ "How to Setup Apache Virtual Hosts in RHEL 9")
[How to Setup Apache Virtual Hosts in RHEL 9](https://www.tecmint.com/apache-virtual-hosting-in-centos/)
[![Monitor Apache Server Status](https://www.tecmint.com/wp-content/uploads/2014/01/Monitor-Apache-Server-Status.webp)](https://www.tecmint.com/monitor-apache-web-server-load-and-page-statistics/ "How to Monitor Apache Load with mod_status in Linux")
[How to Monitor Apache Load with mod_status in Linux](https://www.tecmint.com/monitor-apache-web-server-load-and-page-statistics/)
[![Apache htaccess Tips](https://www.tecmint.com/wp-content/uploads/2015/01/Apache-htaccess-Tips.webp)](https://www.tecmint.com/apache-htaccess-tricks/ "36 Useful Apache ‘.htaccess’ Tricks for Security and Performance")
[36 Useful Apache ‘.htaccess’ Tricks for Security and Performance](https://www.tecmint.com/apache-htaccess-tricks/)
[![Allow or Deny Access to Websites in Apache](https://www.tecmint.com/wp-content/uploads/2024/10/block-website-in-Apache.png)](https://www.tecmint.com/allow-deny-access-website-apache/ "How to Allow or Deny Access to Websites in Apache")
[How to Allow or Deny Access to Websites in Apache](https://www.tecmint.com/allow-deny-access-website-apache/)
[![Enable mod_rewrite in .htaccess File](https://www.tecmint.com/wp-content/uploads/2024/10/Enable-mod_rewrite-in-htaccess-File.png)](https://www.tecmint.com/enable-mod_rewrite-in-htaccess/ "How to Enable mod_rewrite in .htaccess File")
[How to Enable mod_rewrite in .htaccess File](https://www.tecmint.com/enable-mod_rewrite-in-htaccess/)
### 3 Comments
[Leave a Reply](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/58d942a35f01941137aec17cfa7db84d65cbadd8ad2fccff1c3cc2d735b089cd?s=50&d=blank&r=g)
Alexey
[ June 25, 2018 at 8:22 pm  ](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/#comment-1006491)
Thank you for article!
I would appreciate your help if you describe how to install Netdata+ Apache on Debian.
[Reply](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/#comment-1006491)
  2. ![](https://secure.gravatar.com/avatar/307a36a08c1c3eee64af4b9e842b3175f7d604e11a5ae340076f12c77396b5b6?s=50&d=blank&r=g)
Stephen
[ June 19, 2018 at 5:09 pm  ](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/#comment-1005277)
Nice guide man!
Would you be interested in updating this guide at some point where this is placed behind apache/nginx? preferably with https and authentication ^^
[Reply](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/#comment-1005277)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ June 20, 2018 at 12:34 pm  ](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/#comment-1005423)
@Stephen
Okay, great probably behind Nginx, because it is a high-performance and more efficient reverse proxy server, to me and easy to configure with HTTPS and basic authentication. Thanks for the feedback.
[Reply](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/#comment-1005423)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/#respond)
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
[How to Christmassify Your Linux Terminal and Shell](https://www.tecmint.com/christmassify-linux-terminal-and-shell/)
[How to Backup or Clone Linux Partitions Using ‘cat’ Command](https://www.tecmint.com/backup-or-clone-linux-partitions-using-cat-command/)
[How to View Colored Man Pages in Linux](https://www.tecmint.com/view-colored-man-pages-in-linux/)
[11 Cron Command Examples in Linux [Schedule Cron Jobs]](https://www.tecmint.com/11-cron-scheduling-task-examples-in-linux/)
[Linux Performance Monitoring with Vmstat and Iostat Commands](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/)
[fdupes – A Command Line Tool to Find and Delete Duplicate Files in Linux](https://www.tecmint.com/fdupes-find-and-delete-duplicate-files-in-linux/)
## Linux Server Monitoring Tools
[A Shell Script to Monitor Network, Diske, Uptime, Load, and RAM in Linux](https://www.tecmint.com/linux-server-health-monitoring-script/)
[Cockpit – A Powerful Tool to Monitor and Administer Multiple Linux Servers via Browser](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/)
[httpstat – A Curl Statistics Tool to Check Website Performance](https://www.tecmint.com/httpstat-curl-statistics-tool-check-website-performance/)
[TCPflow – Analyze and Debug Network Traffic in Linux](https://www.tecmint.com/tcpflow-analyze-debug-network-traffic-in-linux/)
[Linux Performance Monitoring with Vmstat and Iostat Commands](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/)
[How to Monitor Remote Linux Systems with Glances](https://www.tecmint.com/glances-monitor-remote-linux-systems/)
## Learn Linux Tricks & Tips
[How to Find a Specific String or Word in Files and Directories](https://www.tecmint.com/find-a-specific-string-or-word-in-files-and-directories/)
[6 Best CLI Tools to Search Plain-Text Data Using Regular Expressions](https://www.tecmint.com/command-line-tools-to-search-strings-or-patterns-in-files/)
[How to Disable SELinux Temporarily or Permanently](https://www.tecmint.com/disable-selinux-in-centos-rhel-fedora/)
[How to Monitor Progress of (Copy/Backup/Compress) Data using ‘pv’ Command](https://www.tecmint.com/monitor-copy-backup-tar-progress-in-linux-using-pv-command/)
[How to Copy a File to Multiple Directories in Linux](https://www.tecmint.com/copy-file-to-multiple-directories-in-linux/)
[How to Keep Remote SSH Processes Alive Even When Disconnected](https://www.tecmint.com/keep-remote-ssh-sessions-running-after-disconnection/)
## Best Linux Tools
[13 Best Photo Editing Software for Linux in 2024](https://www.tecmint.com/best-image-photo-editors-for-linux/)
[10 Best Tools to Install on Fresh Linux Mint Installation](https://www.tecmint.com/linux-mint-tools/)
[Top Cross-Platform Apps for Linux, Windows, and Mac in 2025](https://www.tecmint.com/cross-platform-apps/)
[5 Most Frequently Used Open Source Shells for Linux](https://www.tecmint.com/different-types-of-linux-shells/)
[Top 5 Open Source Collaboration Platforms for Linux in 2024](https://www.tecmint.com/open-source-collaboration-platforms-linux/)
[8 Best HTML & CSS Code Editors for Linux](https://www.tecmint.com/html-css-editors-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/ "Scroll back to top")
Search for:
