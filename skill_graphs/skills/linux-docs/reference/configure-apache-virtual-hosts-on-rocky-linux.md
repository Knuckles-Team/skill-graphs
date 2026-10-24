[Skip to content](https://www.tecmint.com/configure-apache-virtual-hosts-on-rocky-linux/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/configure-apache-virtual-hosts-on-rocky-linux/)
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
  * [Pro Courses](https://www.tecmint.com/configure-apache-virtual-hosts-on-rocky-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/configure-apache-virtual-hosts-on-rocky-linux/)
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
  * [Pro Courses](https://www.tecmint.com/configure-apache-virtual-hosts-on-rocky-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/configure-apache-virtual-hosts-on-rocky-linux/)
# How to Configure Apache Virtual Hosts on Rocky Linux
[James Kiarie](https://www.tecmint.com/author/james2030kiarie/ "View all posts by James Kiarie")Last Updated: August 6, 2021 Read Time: 2 minsCategories [Apache](https://www.tecmint.com/category/web-servers/apache/), [Rocky Linux](https://www.tecmint.com/category/rocky-linux/) [Leave a comment](https://www.tecmint.com/configure-apache-virtual-hosts-on-rocky-linux/#respond)
This is an optional step intended only for those who wish to host multiple sites on the same server. So far, our [LAMP setup](https://www.tecmint.com/install-lamp-on-rocky-linux/ "How to Install LAMP Stack on Rocky Linux 8") can only host one site. If you wish to host multiple sites, then you need to set up or configure virtual host files. Apache virtual host files encapsulate the configurations of multiple websites.
For this section, we will create an Apache virtual host file to demonstrate how you can go about setting your virtual hosts in **Rocky Linux**.
#### Requirements
  * For this to be successful, you need to have a **Fully Qualified Domain Name** pointing to the public IP address of your server in your DNS hosting control panel.
  * An [instance of Rocky Linux 8](https://www.tecmint.com/install-rocky-linux/ "Install Rocky Linux 8") with [LAMP stack installed](https://www.tecmint.com/install-lamp-on-rocky-linux/ "How to Install LAMP Stack on Rocky Linux 8").


**Note** : In our setup, we are using the domain name `tecmint.info` which is pointed to the public IP of our virtual server. Be sure to use your own domain name in all the instances where our domain name appears.
### Creating an Apache Virtual Directory Structure
The first step is to create a directory that will accommodate the website or domain’s files. This will be the **DocumentRoot** which will be in the **/var/www/** path. Therefore run the following command.
```
$ sudo mkdir -p /var/www/tecmint.info/html

```

Next, we will create a simple **index.html** file which we shall use to test our virtual host file.
```
$ sudo vim /var/www/tecmint.info/html/index.html

```

Insert the following HTML lines.
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Welcome to tecmint.info!</title>
  </head>
  <body>
    <h1>Success! The tecmint.info virtual host is active and running!</h1>
  </body>
</html>

```

Save the HTML file and exit.
Then assign the permissions to the currently logged-in user to allow them to edit the webroot directories without permission hiccups.
```
$ sudo chown -R $USER:$USER /var/www/tecmint.info/html

```

### Creating an Apache Virtual Host File
At this point, we will create a separate virtual host file for our domain. By default, **Rocky Linux 8** , just like **CentOS 8** , loads all its configurations from the **/etc/httpd/conf.d** directory.
So, proceed and create a separate virtual host file.
```
$ sudo vim /etc/httpd/conf.d/tecmint.info.conf

```

Paste the content below to define the virtual host.
```
<VirtualHost *:80>
    ServerName **www.tecmint.info**
    ServerAlias **tecmint.info**
    DocumentRoot /var/www/**tecmint.info**/html

    <Directory /var/www/**tecmint.info**/html>
        Options -Indexes +FollowSymLinks
        AllowOverride All
    </Directory>

    ErrorLog /var/log/httpd/**tecmint.info**-error.log
    CustomLog /var/log/httpd/**tecmint.info**-access.log combined
</VirtualHost>

```

Save the changes and exit the virtual host file.
To check whether all the configurations are sound, execute the command:
```
$ sudo apachectl configtest

```
![Check Apache Configuration in Rocky Linux](https://www.tecmint.com/wp-content/uploads/2021/08/Check-Apache-Configuration-in-Rocky-Linux.png)Check Apache Configuration in Rocky Linux
Next, restart Apache to effect the changes made.
```
$ sudo systemctl restart httpd

```

Then launch your web browser and browse your domain as follows:
```
http://tecmint.info

```

This should display the sample HTML page we configured in step 1 of this section. This is ironclad proof that our virtual host setup is working!
![Check Apache Virtual Host Domain](https://www.tecmint.com/wp-content/uploads/2021/08/Check-Apache-Virtual-Host-Domain.png)Check Apache Virtual Host Domain
If you have multiple domain names, repeat the same steps to set up virtual host files for each domain or website.
##### Conclusion
And there you have it. We have successfully configured virtual host files to host several websites or domains in **Rocky Linux 8** with the **LAMP** stack. You can proceed to host your web applications or [secure your Apache with an SSL Certificate](https://www.tecmint.com/secure-apache-with-ssl-in-rocky-linux/ "Secure Apache with Let’s Encrypt Certificate on Rocky Linux") using free Let’s Encrypt.
Tags [Apache Tips](https://www.tecmint.com/tag/apache-tips/), [LAMP Guides](https://www.tecmint.com/tag/lamp-guides/), [Rocky Linux Tips](https://www.tecmint.com/tag/rocky-linux-tips/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install Java 16 in Rocky Linux and AlmaLinux](https://www.tecmint.com/install-java-in-rocky-linux/)
Next article:
[How to Install MongoDB on Rocky Linux and AlmaLinux](https://www.tecmint.com/install-mongodb-on-rocky-linux-and-almalinux/)
![Photo of author](https://secure.gravatar.com/avatar/3b060d6a6c8d6305817bda1435529b27f2d4f900a7998bd703a17094636601a9?s=100&d=blank&r=g)
James Kiarie
This is James, a certified Linux administrator and a tech enthusiast who loves keeping in touch with emerging trends in the tech world. When I'm not running commands on the terminal, I'm taking listening to some cool music. taking a casual stroll or watching a nice movie.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/configure-apache-virtual-hosts-on-rocky-linux/#respond)** or
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
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/configure-apache-virtual-hosts-on-rocky-linux/#respond)
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
[12 Useful Commands For Filtering Text for Effective File Operations in Linux](https://www.tecmint.com/linux-file-operations-commands/)
[How To Create A File In Linux: Echo, Touch, Tee and Cat Commands](https://www.tecmint.com/create-file-linux/)
[How to Fix “Command ‘pip3’ not found” Error in Linux](https://www.tecmint.com/pip-command-not-found/)
[10 Must-Know sFTP Commands for Linux File Transfers](https://www.tecmint.com/sftp-command-examples/)
[How To Run a Cron Job Every 30 Seconds in Linux](https://www.tecmint.com/run-cronjob-every-x-seconds/)
[PhotoRec – Recover Deleted or Lost Files in Linux](https://www.tecmint.com/photorec-recover-deleted-lost-files-in-linux/)
## Linux Server Monitoring Tools
[How to Install Icinga2 Monitoring Tool on Ubuntu 20.04/22.04](https://www.tecmint.com/install-icinga-monitoring-ubuntu/)
[Monitor Server Logs in Real-Time with “Log.io” Tool on RHEL/CentOS 7/6](https://www.tecmint.com/linux-server-log-monitoring-with-log-io/)
[Collectl: An Advanced All-in-One Performance Monitoring Tool for Linux](https://www.tecmint.com/collectl-linux-performance-reporting-monitoring/)
[How to Install Nagios Monitoring in RHEL, Rocky, and AlmaLinux](https://www.tecmint.com/install-nagios-in-linux/)
[How to Create a Centralized Log Server with Rsyslog in CentOS/RHEL 7](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/)
[Darkstat – A Web Based Linux Network Traffic Analyzer](https://www.tecmint.com/darkstat-web-based-linux-network-traffic-analyzer/)
## Learn Linux Tricks & Tips
[How to Boot into Single User Mode in CentOS/RHEL 7](https://www.tecmint.com/boot-into-single-user-mode-in-centos-7/)
[How to Restore Deleted /tmp Directory in Linux](https://www.tecmint.com/restore-deleted-tmp-directory-in-linux/)
[How to Change Default Apache ‘DocumentRoot’ Directory in Linux](https://www.tecmint.com/change-root-directory-of-apache-web-server/)
[How to Switch (su) to Another User Account without Password](https://www.tecmint.com/switch-user-account-without-password/)
[How to Compress and Decompress a .bz2 File in Linux](https://www.tecmint.com/linux-compress-decompress-bz2-files-using-bzip2/)
[Lolcat – Display Text in Rainbow Colors in Linux Terminal](https://www.tecmint.com/lolcat-color-output-linux-terminal/)
## Best Linux Tools
[5 Best Open Source Internet Radio Player for Linux](https://www.tecmint.com/internet-radio-player-linux/)
[Top 4 Google Docs Alternatives for Linux in 2024](https://www.tecmint.com/google-docs-alternatives/)
[32 Most Used Firefox Add-ons to Improve Productivity in Linux](https://www.tecmint.com/firefox-add-ons-productivity/)
[4 Best Tools for Creating Fillable PDF Forms on Linux](https://www.tecmint.com/create-pdf-forms-linux/)
[3 Best Cloud-Based Music Apps for Linux](https://www.tecmint.com/cloud-music-player/)
[32 Best File Managers and Explorers [GUI + CLI] for Linux in 2024](https://www.tecmint.com/linux-file-managers/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/configure-apache-virtual-hosts-on-rocky-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
