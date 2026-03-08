[Skip to content](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/)
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
  * [Pro Courses](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/ "Linux Online Courses")
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


[](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/)
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
  * [Pro Courses](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/ "Linux Online Courses")
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


[](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/)
# Monitor Server Resources with Collectd-web and Apache CGI in Linux
[Matei Cezar](https://www.tecmint.com/author/cezarmatei/ "View all posts by Matei Cezar")Last Updated: June 30, 2015 Read Time: 4 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [3 Comments](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/#comments)
This tutorial will discuss how you can install and run **Collectd-web** interface, which is a front-end web monitoring tool for **Collectd** daemon, in conjunction with **Apache CGI** interface in order to produce graphical html outputs in order to monitor Linux boxes.
![Monitor Linux Server Resources](https://www.tecmint.com/wp-content/uploads/2015/06/Monitor-Linux-Server-Resources-Using-Collectd-web.png)Monitor Linux Server Resources
At the end of the article we will, also, present how you can protect Collectd-web interface using **.hpasswd** Apache Authentication mechanism.
#### Requirements
The requirement of this article is, you must have **Collectd** and **Collectd-Web** installed on your Linux system. To install these packages, you must follow Steps **#1** and **#2** from the previous article of this series at:
  1. [Install Collectd and Collectd-Web in Linux](https://www.tecmint.com/install-collectd-and-collectd-web-to-monitor-server-resources-in-linux/)


Only Follow following two steps from the above link:
```
Step 1: **Install Collectd Service**
Step 2: **Install Collectd-Web and Dependencies**

```

Once these two required things completed successfully, you can continue further instructions in this article to configure **Collectd-web** with **Apache CGI**.
### Step 1: Installing Apache Web Server
**1.** Assuming that you already have installed Apache web server on your system, if not you can install using following command according to your Linux distribution.
```
# apt-get install apache2	[On **Debian** based Systems]
# yum install httpd		[On **RedHat** based Systems]

```

**2.** After Apache installed, change the directory to your default web server document root (which is located under **/var/www/html/** or **/var/www** system path and clone the **Collectd-web Github** project by issuing the below commands:
```
# cd /var/www/html
# git clone https://github.com/httpdss/collectd-web.git

```

Also, make the following **Collectd-web** script executable by issuing the following command:
```
# chmod +x /var/www/html/collectd-web/cgi-bin/graphdefs.cgi

```

### Step 2: Enable Apache CGI (.cgi scripts) for Default Host
**3.** In order for Apache to run the CGI scripts located under the default host HTML Collectd-web cgi-bin directory, you need to explicitly enable Apache CGI interface for Bash scripts (with **.cgi** extension) by altering the **sites-available** default host and adding the below statements block.
#### On Debian Systems
First open Apache default host configuration file for editing with **nano** editor:
```
# nano /etc/apache2/sites-available/000-default.conf

```

While the file is opened for editing add the following directive block below the **Document Root** directive as illustrated on the below image:
```
<Directory /var/www/html/collectd-web/cgi-bin>
                Options Indexes ExecCGI
                AllowOverride All
                AddHandler cgi-script .cgi
                Require all granted
</Directory>

```
![Enable CGI in Debian](https://www.tecmint.com/wp-content/uploads/2015/06/Enable-CGI-in-Debian-620x362.png)Enable CGI in Debian
After you’re done editing the file, close it with **CTRL + o** and exit nano editor **(CTRL+x)** , then enable Apache CGI module and restart the server in order to apply all the changes made so far by issuing the below commands:
```
# a2enmod cgi cgid
# service apache2 restart
OR
# systemctl restart apache2.service     [For **systemd init** scripts]

```
![Enable Apache CGI](https://www.tecmint.com/wp-content/uploads/2015/06/Enable-Apache-CGI-620x193.png) Enable Apache CGI
#### On RedHat Systems
**4.** To enable Apache CGI interface for CentOS/RHEL, open **httpd.conf** Apache configuration file and add the following lines at the bottom of the file:
```
# nano /etc/httpd/conf/httpd.conf

```

Add following excerpt to **httpd.conf** file.
```
ScriptAlias /cgi-bin/ “/var/www/html/collectd-web/cgi-bin"
Options FollowSymLinks ExecCGI
AddHandler cgi-script .cgi .pl

```

In order to apply changes, restart **httpd** daemon by issuing the following command:
```
# service httpd restart
OR
# systemctl restart httpd        [For **systemd init** scripts]

```

### Step 3: Browse Collectd-web Interface
**5.** In order to visit **Collectd-web** interface and visualize statistics about your machine collected so far, open a browser and navigate to your machine **IP Address/collectd-web/** URI location using the HTTP protocol.
```
http://192.168.1.211/collect-web/

```
![Collectd-Web Dashboard](https://www.tecmint.com/wp-content/uploads/2015/06/Collectd-Web-Dashboard-620x392.png)Collectd-Web Dashboard
### Step 4: Password Protect Collectd-web URL using Apache Authentication
**6.** In case you want to limit access to **Collectd-web** interface by protecting it using Apache Authentication mechanism (**.htpasswd**), which requires visitors to enter a username and a password in order to access a web resource.
To do so, you need to install **apache2-utils** package and create a set of credentials for local authentication. To achieve this goal, first issue the following command to install **apache2-utils** package:
```
# apt-get install apache2-utils	        [On **Debian** based Systems]
# yum install httpd-tools		[On **RedHat** based Systems]

```

**7.** Next, generate a username and a password which will be stored on a hidden local **.htpass** file located under Apache default host **Collectd-web** path by issuing the below command:
```
# htpasswd -c /var/www/html/collectd-web/.htpass  your_username

```

Try to protect this file by assigning the following permissions:
```
# chmod 700 /var/www/html/collectd-web/.htpass
# chown www-data /var/www/html/collectd-web/.htpass

```

**8.** On the next step, after you have generated **.htpass** file, open Apache default host for editing and instruct the server to use **htpasswd** basic server-side authentication by adding the following directive block as illustrated on the below screenshot:
```
<Directory /var/www/html/collectd-web >
                AuthType Basic
                AuthName "Collectd Restricted Page"
                AuthBasicProvider file
                AuthUserFile /var/www/html/collectd-web/.htpass
                Require valid-user
</Directory>

```
![Apache Password Protect Directory](https://www.tecmint.com/wp-content/uploads/2015/06/Apache-Password-Protect-Directory-620x443.png)Apache Password Protect Directory
**9.** The last step in order to reflect changes is to restart **Apache** server by issuing the below command and visit the **Coollectd-web** URL page as described above.
A pop-up should appear on the web page requesting for your authentication credentials. Use the username and password created earlier to access Collectd web interface.
```
# service apache2 restart		[On **Debian** based Systems]
# service httpd restart			[On **RedHat** based Systems]

OR
---------------- For **systemd init** scripts ----------------
# systemctl restart apache2.service
# systemctl restart http.service

```
![Apache Password Authentication](https://www.tecmint.com/wp-content/uploads/2015/06/Apache-Password-Authentication-620x274.png) Apache Password Authentication ![Collectd-Web Panel](https://www.tecmint.com/wp-content/uploads/2015/06/Collectd-Web-Panel-620x390.png)Collectd-Web Panel
Tags [collectd](https://www.tecmint.com/tag/collectd/), [collectd-web](https://www.tecmint.com/tag/collectd-web/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[4 Useful Tips on mkdir, tar and kill Commands in Linux](https://www.tecmint.com/mkdir-tar-and-kill-commands-in-linux/)
Next article:
[Atom – A Hackable Text and Source Code Editor for Linux](https://www.tecmint.com/atom-text-and-source-code-editor-for-linux/)
![Photo of author](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=100&d=blank&r=g)
Matei Cezar
I'am a computer addicted guy, a fan of open source and linux based system software, have about 4 years experience with Linux distributions desktop, servers and bash scripting.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/#respond)** or
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
### 3 Comments
[Leave a Reply](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/752c4c7db5f9ffad15c034378ce1f2b438e39bcf5d30f680ea370400e408138c?s=50&d=blank&r=g)
Naseath Saly
[ February 3, 2016 at 1:31 pm  ](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/#comment-747431)
Your problem look like you don’t have a correct PHP version to support the app.
Another issue could cause by your php mode does not enable yet. to enable php mode you should use this command:
```
$ sudo a2enmod php5

```
[Reply](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/#comment-747431)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 3, 2016 at 2:16 pm  ](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/#comment-747447)
@Naseath,
Thanks a ton for helping our fellow readers, keep it up and stay connected to TecMint and looking forward for your support in future..
[Reply](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/#comment-747447)
  2. ![](https://secure.gravatar.com/avatar/8d64389050523d2e47641a2c6db1a60af038392824bc55580071390befa48d8d?s=50&d=blank&r=g)
Mallikharjun
[ November 26, 2015 at 7:04 pm  ](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/#comment-714223)
Hi,
Configured the Collectd-web for Apache2.4.7 but when i open the url as: <http:///collectd-web/> instead of graphical page displaying the html source and <http:///collectd-web/index.html> the ui is scattered around the browser nothing is displaying..
iam using the following broswers
Firefox version 42.0
chrome Version 46.0.2490.86 m
explorer version 9.0.8112
kindly do the needfull.
[Reply](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/#comment-714223)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/#respond)
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
[The Ultimate Guide to Handling Filenames with Special Characters in Linux](https://www.tecmint.com/special-character-filenames-linux/)
[How to Install YTP-DL to Download Songs from YouTube Videos](https://www.tecmint.com/install-youtube-dl-command-line-video-download-tool/)
[LFCA: Learn Basic Network Troubleshooting Tips – Part 12](https://www.tecmint.com/basic-network-troubleshooting-tips/)
[How to Compress Files Faster with Pigz Tool in Linux](https://www.tecmint.com/compress-files-faster-in-linux/)
[4 Ways to Disable Root Account in Linux](https://www.tecmint.com/disable-root-login-in-linux/)
[How to Convert Files to UTF-8 Encoding in Linux](https://www.tecmint.com/convert-files-to-utf-8-encoding-in-linux/)
## Linux Server Monitoring Tools
[btop: A Modern and Resourceful System Monitor](https://www.tecmint.com/btop-system-monitoring-tool-for-linux/)
[5 Tools to Scan a Linux Server for Malware and Rootkits](https://www.tecmint.com/scan-linux-for-malware-and-rootkits/)
[Inxi – A Powerful Feature-Rich Commandline System Information Tool for Linux](https://www.tecmint.com/inxi-command-to-find-linux-system-information/)
[How to Install Cacti with Cacti-Spine in Debian and Ubuntu](https://www.tecmint.com/install-cacti-with-cacti-spine-in-debian-and-ubuntu/)
[How to Install htop on CentOS 8](https://www.tecmint.com/install-htop-on-centos-8/)
[How to Add Hosts in OpenNMS Monitoring Server](https://www.tecmint.com/add-hosts-in-opennms-monitoring/)
## Learn Linux Tricks & Tips
[How to Change UUID of Partition in Linux Filesystem](https://www.tecmint.com/change-uuid-of-partition-in-linux/)
[Ternimal – Show Animated Lifeform in Your Linux Terminal](https://www.tecmint.com/ternimal-show-animated-lifeform-in-linux-terminal/)
[Useful Commands to Create Commandline Chat Server and Remove Unwanted Packages in Linux](https://www.tecmint.com/linux-commandline-chat-server-and-remove-unwanted-packages/)
[3 Ways to List All Installed Packages in RHEL, CentOS and Fedora](https://www.tecmint.com/list-installed-packages-in-rhel-centos-fedora/)
[How to Optimize and Compress JPEG or PNG Images in Linux Commandline](https://www.tecmint.com/optimize-and-compress-jpeg-or-png-batch-images-linux-commandline/)
[Fd – The Best Alternative to ‘Find’ Command for Quick File Searching](https://www.tecmint.com/fd-alternative-to-find-command/)
## Best Linux Tools
[My Favorite Command Line Editors for Linux – What’s Your Editor?](https://www.tecmint.com/linux-command-line-editors/)
[13 Most Used Microsoft Office Alternatives for Linux](https://www.tecmint.com/microsoft-office-alternatives-for-linux/)
[11 Best PDF Editors to Edit PDF Documents in Linux](https://www.tecmint.com/pdf-editors-linux/)
[11 Best GUI Tools for Linux System Administrators in 2024](https://www.tecmint.com/gui-tools-for-linux-system-administrators/)
[5 Best Reference Management Software for Linux in 2024](https://www.tecmint.com/reference-management-software/)
[13 Best Photo Editing Software for Linux in 2024](https://www.tecmint.com/best-image-photo-editors-for-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/ "Scroll back to top")
Search for:
