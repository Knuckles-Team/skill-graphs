[Skip to content](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/)
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
  * [Pro Courses](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/)
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
  * [Pro Courses](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/)
# How to Setup and Manage Log Rotation Using Logrotate in Linux
[Gabriel Cánepa](https://www.tecmint.com/author/gacanepa/ "View all posts by Gabriel Cánepa")Last Updated: October 21, 2020 Read Time: 6 minsCategories [CentOS](https://www.tecmint.com/category/linux-distros/centos/), [Debian](https://www.tecmint.com/category/debian/), [Fedora](https://www.tecmint.com/category/linux-distros/fedora/), [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [RedHat](https://www.tecmint.com/category/redhat/), [Ubuntu](https://www.tecmint.com/category/linux-distros/ubuntu/) [11 Comments](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comments)
One of the most interesting (and perhaps one of the most important as well) directories in a Linux system is `/var/log`. According to the [Filesystem Hierarchy Standard](https://www.tecmint.com/linux-directory-structure-and-important-files-paths-explained/), the activity of most services running in the system are written to a file inside this directory or one of its subdirectories.
Such files are known as **logs** and are the key to examining how the system is operating (and how it has behaved in the past). **Logs** are also the first source of information where administrators and engineers look while troubleshooting.
If we look at the contents of `/var/log` on a **CentOS/RHEL/Fedora** and **Debian/Ubuntu** (for variety) we will see the following log files and subdirectories.
Please note that the result may be somewhat different in your case depending on the services running on your system(s) and the time they have been running.
#### In RHEL/CentOS and Fedora
```
# ls /var/log

```
![Log Files and Directories under CentOS 7](https://www.tecmint.com/wp-content/uploads/2016/08/Logs-under-CentOS-7.png)Log Files and Directories under CentOS 7
#### In Debian and Ubuntu
```
# ls /var/log

```
![Log Files and Directories in Debian 8](https://www.tecmint.com/wp-content/uploads/2016/08/Log-Files-in-Debian.png)Log Files and Directories in Debian 8
In both cases, we can observe that some of the log names end as expected in **“log”** , while others are either renamed using a date (for example, **maillog-20160822** on **CentOS**) or compressed (consider **auth.log.2.gz** and **mysql.log.1.gz** on **Debian**).
This is not a default behavior [based on the chosen distribution](https://www.tecmint.com/best-linux-distributions-for-beginners/ "Best Linux Distributions for Beginners") but can be changed at will using directives in the configuration files, as we will see in this article.
If logs were kept forever, they would eventually end up filling the filesystem where **/var/log** resides. In order to prevent that, the system administrator can use a nice utility called **logrotate** to clean up the logs on a periodic basis.
In a few words, **logrotate** will rename or compress the main log when a condition is met (more about that in a minute) so that the next event is recorded on an empty file.
In addition, it will remove **“old”** log files and will keep the most recent ones. Of course, we get to decide what **“old”** means and how often we want logrotate to clean up the logs for us.
### Installing Logrotate in Linux
To install **logrotate** , just use your package manager:
```
---------- **On Debian and Ubuntu** ----------
# aptitude update && aptitude install logrotate

---------- **On CentOS, RHEL and Fedora** ----------
# yum update && yum install logrotate

```

It is worth and well to note that the configuration file (`/etc/logrotate.conf`) may indicate that other, more specific settings may be placed on individual `.conf` files inside **/etc/logrotate.d**.
**Suggested Read** : [Manage System Logs (Configure, Rotate, and Import Into Database) Using Logrotate](https://www.tecmint.com/manage-linux-system-logs-using-rsyslogd-and-logrotate/ "Manage System Logs in Linux")
This will be the case if and only if the following line exists and is not commented out:
```
include /etc/logrotate.d

```

We will stick with this approach, as it will help us to keep things in order, and use the **Debia** n box for the following examples.
### Configure Logrotate in Linux
Being a very versatile tool, logrotate provides plenty of directives to help us configure when and how the logs will be rotated, and what should happen right afterward.
Let’s insert the following contents in **/etc/logrotate.d/apache2.conf** (note that most likely you will have to create that file) and examine each line to indicate its purpose:
apache2.conf
```
/var/log/apache2/* {
    weekly
    rotate 3
    size 10M
    compress
    delaycompress
}

```

The first line indicates that the directives inside the block apply to all logs inside **/var/log/apache2** :
  * **weekly** means that the tool will attempt to rotate the logs on a weekly basis. Other possible values are daily and monthly.
  * **rotate 3** indicates that only 3 rotated logs should be kept. Thus, the oldest file will be removed on the fourth subsequent run.
  * **size=10M** sets the minimum size for the rotation to take place to 10M. In other words, each log will not be rotated until it reaches 10MB.
  * **compress** and **delaycompress** are used to tell that all rotated logs, with the exception of the most recent one, should be compressed.


Let’s execute a dry-run to see what logrotate would do if it was actually executed now. Use the `-d` option followed by the configuration file (you can actually run logrotate by omitting this option):
```
# logrotate -d /etc/logrotate.d/apache2.conf

```

The results are shown below:
![Rotate Apache Logs with Logrotate](https://www.tecmint.com/wp-content/uploads/2016/08/Rotate-Apache-Logs-with-Logrotate.png)Rotate Apache Logs with Logrotate
Instead of compressing the logs, we could rename them after the **date** when they were rotated. To do that, we will use the `dateext` directive. If our date format is other than the default **yyyymmdd** , we can specify it using **dateformat**.
**Suggested Read** : [Install ‘atop’ to Monitor Logging Activity of Linux System Processes](https://www.tecmint.com/how-to-install-atop-to-monitor-logging-activity-of-linux-system-processes/ "Analyzing Linux server performance with atop")
Note that we can even prevent the rotation from happening if the log is empty with **notifempty**. In addition, let’s tell logrotate to mail the rotated log to the system administrator (**gabriel@mydomain.com** in this case) for his / her reference (this will require a [mail server to be set up](https://www.tecmint.com/setup-postfix-mail-server-and-dovecot-with-mariadb-in-centos/), which is out of the scope of this article).
If you want to get emails about logrotate, you can setup Postfix mail server as shown here: [Install Postfix Mail Server](https://www.tecmint.com/setup-postfix-mail-server-and-dovecot-with-mariadb-in-centos/)
This time we will use **/etc/logrotate.d/squid.conf** to only rotate **/var/log/squid/access.log** :
squid.conf
```
/var/log/squid/access.log {
    monthly
    create 0644 root root
    rotate 5
    size=1M
    dateext
    dateformat -%d%m%Y
    notifempty
    mail gabriel@mydomain.com
}

```

As we can see in the image below, this log did not need to be rotated. However, when the size condition is met **(size=1M**), the rotated log will be renamed **access.log-25082020** (if the log was rotated on **August 25, 2020**) and the main log (**access.log**) will be re-created with access permissions set to **0644** and with **root** as owner and group owner.
Finally, when the number of logs finally reaches **6** , the oldest log will be mailed to **gabriel@mydomain.com**.
![Rotate Squid Logs with Logrotate](https://www.tecmint.com/wp-content/uploads/2016/08/Rotate-Squid-Logs-with-Logrotate.png)Rotate Squid Logs with Logrotate
Now let’s suppose you want to run a custom command when the rotation takes place. To do that, place the line with such command between the postrotate and endscript directives.
For example, let’s suppose we want to send an email to root when any of the logs inside **/var/log/myservice** gets rotated. Let’s add the lines in red to **/etc/logrotate.d/squid.conf** :
squid.conf
```
/var/log/myservice/* {
	monthly
	create 0644 root root
	rotate 5
	size=1M
    	**postrotate
   		echo "A rotation just took place." | mail root
    	endscript**
}

```

Last, but not least, it is important to note that options present in `/etc/logrotate.d/*.conf` override those in the main configuration file in case of conflicts.
### Logrotate and Cron
By default, the installation of logrotate creates a crontab file inside **/etc/cron.daily** named **logrotate**. As it is the case with the other crontab files inside this directory, it will be executed daily starting at **6:25 am** if anacron is not installed.
**Suggested Read** : [11 Cron Scheduling Task Examples in Linux](https://www.tecmint.com/11-cron-scheduling-task-examples-in-linux/ "Set Cron in Linux")
Otherwise, the execution will begin around **7:35 am**. To verify, watch for the line containing **cron.daily** in either **/etc/crontab** or **/etc/anacrontab**.
### Summary
In a system that generates several logs, the administration of such files can be greatly simplified using logrotate. As we have explained in this article, it will automatically rotate, compress, remove, and mail logs on a periodic basis or when the file reaches a given size.
Just make sure it is set to run as a cron job and logrotate will make things much easier for you. For more details, refer to the man page.
Do you have any questions or suggestions about this article? Feel free to let us know using the comment form below.
Tags [CentOS Tips](https://www.tecmint.com/tag/centos-tips/), [Debian Tips](https://www.tecmint.com/tag/debian-tips/), [Linux Log Monitoring](https://www.tecmint.com/tag/linux-log-monitoring/), [Logrotate in Linux](https://www.tecmint.com/tag/logrotate-in-linux/), [RHEL Tips](https://www.tecmint.com/tag/rhel-tips/), [Ubuntu Tips](https://www.tecmint.com/tag/ubuntu-tips/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[GoAccess (A Real-Time Apache and Nginx) Web Server Log Analyzer](https://www.tecmint.com/goaccess-a-real-time-apache-and-nginx-web-server-log-analyzer/)
Next article:
[How to Install Shutter Screenshot Tool in Ubuntu 20.04](https://www.tecmint.com/install-shutter-in-ubuntu/)
![Photo of author](https://secure.gravatar.com/avatar/27b3ea2a3fb1de4ed1c8694a1465c099a86586d8b833a0d852a26d76d750df9f?s=100&d=blank&r=g)
Gabriel Cánepa
Gabriel Cánepa is a GNU/Linux sysadmin and web developer from Villa Mercedes, San Luis, Argentina. He works for a worldwide leading consumer product company and takes great pleasure in using FOSS tools to increase productivity in all areas of his daily work.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#respond)** or
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
### 11 Comments
[Leave a Reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/c96cf913507067592df4343f381c313697d1732aba36f6b399bf70d403f1cc17?s=50&d=blank&r=g)
Blake
[ May 31, 2021 at 8:36 pm  ](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-1513764)
Thanks, worked well for me! I just wanted to point out in this line from the article:
`/var/log/apache2/* {`
..if you just use an asterisk `*` it seems like logrotate will rotate any files, even previously rotated files. To correct this, I had to use `*.log`.
[Reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-1513764)
  2. ![](https://secure.gravatar.com/avatar/55c103410b2166db04b15e4b049a44c8c69386512c6bfc2e249004185b3c7d1f?s=50&d=blank&r=g)
Sarjit Singh
[ February 26, 2019 at 11:15 am  ](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-1104919)
How can I setup logrotate to rotate the logs hourly?
There is no option and minimum frequency is daily.
[Reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-1104919)
  3. ![](https://secure.gravatar.com/avatar/cc9b6c9d7e475394497968066616d5ae14083889ee0ad6a1e8644e4d04fd6a00?s=50&d=blank&r=g)
Siva
[ October 16, 2018 at 5:05 pm  ](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-1049070)
Hi log rotate is not working, please help me.
```
/opt/var/foo.log {
    copytruncate
    daily
    dateext
    rotate 3
    compress
    missingok
    size 10M
}

```

It is appending data on same file, now the file size reached 6GB how can I fix it
[Reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-1049070)
  4. ![](https://secure.gravatar.com/avatar/d53050c6531bb7d1c01acddf0e503bad1bc8c1ae88d1f191e738fe8c718052a3?s=50&d=blank&r=g)
Kumar P
[ September 21, 2018 at 10:52 am  ](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-1038100)
Hello Gabriel A. Cánepa,
Are we allowed to add our own log path of apache2 here ? with new file on /etc/logrotate.d/mylog with my own log path ?
[Reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-1038100)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ September 21, 2018 at 12:00 pm  ](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-1038113)
@Kumar
Yes, you can add your own apache website log path in this file..
[Reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-1038113)
  5. ![](https://secure.gravatar.com/avatar/2f2282038308f8157d14b1f0f5df6e627be7f2550e57cae2e75a50389774a75e?s=50&d=blank&r=g)
youtube to mp3
[ May 2, 2018 at 1:09 am  ](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-988467)
So i wasn’t sure, if i already have logrotate and it seems like it takes care of logs in **/var/log/** folder, all of them seem to be numbered, dated, and stuff, so i am assuming it’s on and working, but what about manually specified folders, for example, all of my websites have their logs in their special folders, and not in **/var/log/**. How do i go about this? will simple directive on holding those logs in **/var/log** take care of log-rotation as well? i mean, if i set my website to keep its log in **/var/log** , do i need to worry about rotation, or will everything in that folder auto-rotate if logrotate is installed?
a bit confusing, but basically trying to go the way of least resistance… =)
[Reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-988467)
  6. ![](https://secure.gravatar.com/avatar/4bd66109759bfcac402c2099b8fd37a8b9c4eb3d711aa25c162da8ff49259b10?s=50&d=blank&r=g)
K Sinclair
[ June 29, 2017 at 8:16 pm  ](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-897657)
Hi, I am new to Linux and recently built a **syslog** server but the log file is not rotating. I have the entry below for the **logrotate.conf** file and the error I get when I try to force it to run using:
```
# logrotate -vdf /etc/logrotate.conf

```

Can you tell me what I need to change for the rotate to run properly.
```
/var/log/Firewalls/firewall.log {

daily
rotate 30
dateyesterday
missingok
compress
postrotate
systemctl restart rsyslog
endscript
}

```

(It’s world writable or writable by group which is not “**root** ”) Set “**su** ” directive in config file to tell logrotate which user/group should be used for rotation.
[Reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-897657)
  7. ![](https://secure.gravatar.com/avatar/dd16e7f1f07a30b29e537e636387ff8b9e0aa842654a254a19e4ec36ba9f0c93?s=50&d=blank&r=g)
fatboy92
[ September 14, 2016 at 8:06 pm  ](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-817249)
Hi all,
What about cases where the outdoor is never close. I had that case, it meant that the file ran full, i.e. the file system ran full, the file however showed only a small.size. A real problem when you don’t know. The file system says it’s full, but the sum of all file sizes is much smaller than the file system.
Regards
[Reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-817249)
  8. ![](https://secure.gravatar.com/avatar/fa31aaf1276ddbf91d4a87567e5bf95a956dfec16a512d49fd211148c88a25d6?s=50&d=blank&r=g)
Ravikumar
[ August 25, 2016 at 12:35 pm  ](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-809515)
How to rotate logs manually. If I want to rotate the log files now, what to do?
[Reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-809515)
     * ![](https://secure.gravatar.com/avatar/27b3ea2a3fb1de4ed1c8694a1465c099a86586d8b833a0d852a26d76d750df9f?s=50&d=blank&r=g)
Gabriel A. Cánepa
[ August 25, 2016 at 5:58 pm  ](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-809576)
@Ravikumar,
As explained in this very article, you can rotate the logs by using the same command as in the dry-run – just omit the **-d** option. Assuming you want to process the /var/log/squid/access.log file, do:
**logrotate /etc/logrotate.d/squid.conf**
Best,
Gabriel
[Reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-809576)
     * ![](https://secure.gravatar.com/avatar/bc7ea883c3b9ae034f5bae5e38b86e91cf584eca716ba50818efa921253788c3?s=50&d=blank&r=g)
gasmyr
[ August 25, 2016 at 7:46 pm  ](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-809592)
logrotate -f myConfig_file, have a look in man page of logrotate(man logrotate)
[Reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#comment-809592)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/#respond)
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
[How to Find Out File Types in Linux](https://www.tecmint.com/find-file-types-in-linux/)
[Lolcat – Display Text in Rainbow Colors in Linux Terminal](https://www.tecmint.com/lolcat-color-output-linux-terminal/)
[How to Change UUID of Partition in Linux Filesystem](https://www.tecmint.com/change-uuid-of-partition-in-linux/)
[4 Ways to Find Out Which Process Listening on a Particular Port](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/)
[10 Practical Examples Using Wildcards to Match Filenames in Linux](https://www.tecmint.com/use-wildcards-to-match-filenames-in-linux/)
[15 Must-Know FFmpeg Commands for Video, Audio & Image Conversion](https://www.tecmint.com/ffmpeg-commands-for-video-audio-and-image-conversion-in-linux/)
## Linux Server Monitoring Tools
[How to Set Priority of a Running Process in Linux](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/)
[3 Methods to Check Apache Server Status and Uptime in Linux](https://www.tecmint.com/check-apache-httpd-status-and-uptime-in-linux/)
[How to Monitor Website and Application with Uptime Kuma](https://www.tecmint.com/uptime-kuma-linux-website-monitoring-tool/)
[How to Use Nmap Script Engine (NSE) Scripts in Linux](https://www.tecmint.com/use-nmap-script-engine-nse-scripts-in-linux/)
[10 Strace Commands for Troubleshooting and Debugging Linux Processes](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/)
[Perf- A Performance Monitoring and Analysis Tool for Linux](https://www.tecmint.com/perf-performance-monitoring-and-analysis-tool-for-linux/)
## Learn Linux Tricks & Tips
[8 Parted Commands to Manage Disk Partitions in Linux](https://www.tecmint.com/parted-command-create-linux-partitions/)
[How to Check Remote Ports are Reachable Using ‘nc’ Command](https://www.tecmint.com/check-remote-port-in-linux/)
[How to Change Default Apache ‘DocumentRoot’ Directory in Linux](https://www.tecmint.com/change-root-directory-of-apache-web-server/)
[Rename All Files and Directory Names to Lowercase in Linux](https://www.tecmint.com/rename-all-files-and-directory-names-to-lowercase-in-linux/)
[How to Find Linux Server Geographic Location in Terminal](https://www.tecmint.com/find-linux-server-geographic-location/)
[4 Ways to Find Server Public IP Address in Linux Terminal](https://www.tecmint.com/find-linux-server-public-ip-address/)
## Best Linux Tools
[3 Essential Linux Disk Scanning Tools (GUI and Terminal Based)](https://www.tecmint.com/linux-disk-scanning-tools/)
[Top 5 Open Source Collaboration Platforms for Linux in 2024](https://www.tecmint.com/open-source-collaboration-platforms-linux/)
[25 Outstanding Backup Utilities for Linux Systems in 2024](https://www.tecmint.com/linux-system-backup-tools/)
[18 Best NodeJS Frameworks for App Development in 2023](https://www.tecmint.com/best-nodejs-frameworks-for-developers/)
[10 Tools to Make Bootable USB Drive from ISO in 2026](https://www.tecmint.com/linux-bootable-usb-creators/)
[17 Best KDE Multimedia Applications for Linux](https://www.tecmint.com/kde-multimedia-applications/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/ "Scroll back to top")
Search for:
