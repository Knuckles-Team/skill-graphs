[Skip to content](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/)
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
  * [Pro Courses](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/)
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
  * [Pro Courses](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/)
# Pyinotify – Monitor Filesystem Changes in Real-Time in Linux
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: April 15, 2017 Read Time: 2 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [7 Comments](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comments)
**Pyinotify** is a simple yet useful Python module for [monitoring filesystems changes](https://www.tecmint.com/fswatch-monitors-files-and-directory-changes-modifications-in-linux/) in real-time in Linux.
As a System administrator, you can use it to monitor changes happening to a directory of interest such as web directory or application data storage directory and beyond.
**Suggested Read:** [fswatch – Monitors Files and Directory Changes or Modifications in Linux](https://www.tecmint.com/fswatch-monitors-files-and-directory-changes-modifications-in-linux/)
It depends on **inotify** (a Linux kernel feature incorporated in kernel 2.6.13), which is an event-driven notifier, its notifications are exported from kernel space to user space via three system calls.
The purpose of **pyinotiy** is to bind the three system calls, and support an implementation on top of them providing a common and abstract means to manipulate those functionalities.
In this article, we will show you how to install and use pyinotify in Linux to monitor filesystem changes or modifications in real-time.
#### Dependencies
In order to use **pyinotify** , your system must be running:
  1. Linux kernel 2.6.13 or higher
  2. Python 2.4 or higher


### How to Install Pyinotify in Linux
First start by checking the kernel and Python versions installed on your system as follows:
```
# uname -r
# python -V

```

Once dependencies are met, we will use pip to install **pynotify**. In most Linux distributions, **Pip** is already installed if you’re using **Python 2 >=2.7.9** or **Python 3 >=3.4** binaries downloaded from python.org, otherwise, install it as follows:
```
# yum install python-pip      [On CentOS based Distros]
# apt-get install python-pip  [On Debian based Distros]
# dnf install python-pip      [On Fedora 22+]

```

Now, install pyinotify like so:
```
# pip install pyinotify

```

It will install available version from the default repository, if you are looking to have a latest stable version of **pyinotify** , consider cloning it’s git repository as shown.
```
# git clone https://github.com/seb-m/pyinotify.git
# cd pyinotify/
# ls
# python setup.py install

```

### How to Use pyinotify in Linux
In the example below, I am monitoring any changes to the user tecmint’s home (**/home/tecmint**) directory as root user (logged in via ssh) as shown in the screenshot:
```
# python -m pyinotify -v /home/tecmint

```
![Monitor Directory Changes](https://www.tecmint.com/wp-content/uploads/2017/03/Monitor-Directory-File-Changes.png)Monitor Directory Changes
Next, we will keep a watch for any changes to the web directory (**/var/www/html/tecmint.com**):
```
# python -m pyinotify -v /var/www/html/tecmint.com

```

To exit the program, simply hit `[Ctrl+C]`.
**Note** : When you run **pyinotify** without specifying any directory to monitor, the `/tmp` directory is considered by default.
Find more about Pyinotify on Github:
That’s all for now! In this article, we showed you how to install and use pyinotify, a useful Python module for monitoring filesystems changes in Linux.
Have you come across any similar Python modules or related [Linux tools/utilities](https://tecmint.com/tag/commandline-tools)? Let us know in the comments, perhaps you can as well ask any question in relation to this article.
Tags [commandline tools](https://www.tecmint.com/tag/commandline-tools/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[FreeFileSync – Compare and Synchronize Files in Ubuntu](https://www.tecmint.com/freefilesync-compare-synchronize-files-in-ubuntu/)
Next article:
[pyDash – A Web Based Linux Performance Monitoring Tool](https://www.tecmint.com/pydash-a-web-based-linux-performance-monitoring-tool/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#respond)** or
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
### 7 Comments
[Leave a Reply](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/3c94ba0a7c18a5d59f75db96cc32e14a54b8b3c25363230a08cebc5b712dd8e0?s=50&d=blank&r=g)
Zinx
[ January 27, 2021 at 10:21 pm  ](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-1423520)
I’m not interested in just printing out when a file is added to a directory, what I’m looking for is the ability to execute specific python code when that happens. This looks like a half-baked demo, not a useful library function for implementing some action that should occur when new files land. Consequently, this seems pretty pointless.
[Reply](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-1423520)
  2. ![](https://secure.gravatar.com/avatar/13b40e0bb05bb055235396da946021e63da5f2e5fe798ed20908bab83cb99a05?s=50&d=blank&r=g)
santosh
[ November 23, 2018 at 3:25 pm  ](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-1064713)
Can we also check who changed file and what does he/she changed in that and send a mail to recipients? If yes please share how can we achieve that. Many Thanks!!!
[Reply](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-1064713)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ November 27, 2018 at 11:32 pm  ](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-1069163)
@santosh
The easiest way to achieve that is to use a version control system such as Git. It helps you track changes in a file; showing you exactly who changed what file and what he/she changed in it. Git is commonly used for software projects but it can track changes in any file in a computer.
For more information, check out: <https://www.tecmint.com/use-git-version-control-system-in-linux/>
[Reply](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-1069163)
  3. ![](https://secure.gravatar.com/avatar/671525167ba4878e6a412c5bf37b24c8d96a93dbd091ef0ae8afd9c87d938ce7?s=50&d=blank&r=g)
jorge
[ September 30, 2017 at 12:27 pm  ](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-916790)
When you run pyinotify without specifying any directory to monitor, the /tmp directory is considered by default.
[Reply](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-916790)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ October 4, 2017 at 10:36 am  ](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-918370)
@jorge
Oh, useful tip here. Many thanks for sharing this.
[Reply](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-918370)
  4. ![](https://secure.gravatar.com/avatar/011ef82f3453306f860d3a76dc86e2cbd4dadc226d631a04497c13eb23feaa01?s=50&d=blank&r=g)
Sushma
[ April 9, 2017 at 6:07 am  ](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-882250)
I did commands all in the above but I didn’t get this command.
```
# python -m pyinotify -v /home/tecmint,com

```

i get this error:
`
 [2017-04-08 17:24:37,360 pyinotify DEBUG] Start monitoring ['/home/tecmint'], (press c^c to halt pyinotify)
 [2017-04-08 17:24:37,360 pyinotify ERROR] add_watch: cannot watch /home/tecmint WD=-1, Errno=No such file or directory (ENOENT)
 ^[[A
 ^C[2017-04-08 17:24:44,532 pyinotify DEBUG] Pyinotify stops monitoring.
 `
can you help me t0 resolve this issue?
Thank you.
[Reply](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-882250)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ April 15, 2017 at 2:01 pm  ](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-883816)
@Sushma
Use a directory that is present on your machine, **/home/tecmint** is a test directory on our local system. You’ll probably run a command like so:
**# python -m pyinotify -v /path/to/your/directory**
[Reply](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#comment-883816)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/#respond)
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
[Cricket-CLI – Watch Live Cricket Scores in Linux Terminal](https://www.tecmint.com/watch-live-cricket-scores-in-linux-terminal/)
[Display Command Output or File Contents in Column Format](https://www.tecmint.com/display-command-output-or-file-contents-in-column-format/)
[How to Add Text to Existing Files in Linux](https://www.tecmint.com/append-lines-to-file-linux/)
[How to Set Static IP Address and Configure Network in Linux](https://www.tecmint.com/set-add-static-ip-address-in-linux/)
[20 Practical Examples of RPM Commands in Linux](https://www.tecmint.com/20-practical-examples-of-rpm-commands-in-linux/)
[How to Control Systemd Services on Remote Linux Server](https://www.tecmint.com/control-systemd-services-on-remote-linux-server/)
## Linux Server Monitoring Tools
[Netdata – A Real-Time Performance Monitoring Tool for Linux Systems](https://www.tecmint.com/netdata-real-time-linux-performance-network-monitoring-tool/)
[4 Useful Tools to Monitor CPU and GPU Temperature in Ubuntu](https://www.tecmint.com/monitor-cpu-and-gpu-temperature-in-ubuntu/)
[nload – Monitor Linux Network Bandwidth Usage in Real Time](https://www.tecmint.com/nload-monitor-linux-network-traffic-bandwidth-usage/)
[Petiti – An Open Source Log Analysis Tool for Linux SysAdmins](https://www.tecmint.com/petiti-log-analysis-tool-for-linux-sysadmins/)
[How to Add Hosts in OpenNMS Monitoring Server](https://www.tecmint.com/add-hosts-in-opennms-monitoring/)
[Dool – All-in-One Linux Server Performance Monitoring Tool](https://www.tecmint.com/dool-monitor-linux-server-performance-process-memory-network/)
## Learn Linux Tricks & Tips
[How to Delete Root Mails (Mailbox) File in Linux](https://www.tecmint.com/delete-root-mails-mailbox-file-in-linux/)
[How to Repair and Defragment Linux System Partitions and Directories](https://www.tecmint.com/defragment-linux-system-partitions-and-directories/)
[10 Interesting Linux Command Line Tricks and Tips Worth Knowing](https://www.tecmint.com/linux-command-line-tricks-and-tips-worth-knowing/)
[How to Find Linux Server Geographic Location in Terminal](https://www.tecmint.com/find-linux-server-geographic-location/)
[How to Upload or Download Files/Directories Using sFTP in Linux](https://www.tecmint.com/sftp-upload-download-directory-in-linux/)
[How to Find Recent or Today’s Modified Files in Linux](https://www.tecmint.com/find-recent-modified-files-in-linux/)
## Best Linux Tools
[15 Best Kali Linux Web Penetration Testing Tools](https://www.tecmint.com/kali-linux-web-penetration-testing-tools/)
[11 Best IP Address Management Tools for Linux Network](https://www.tecmint.com/ip-address-management-tools-for-linux/)
[11 Best Free and Low-Cost SSL Certificate Authorities](https://www.tecmint.com/best-ssl-certificate-authorities/)
[10 Best File Comparison and Difference (Diff) Tools for Linux](https://www.tecmint.com/best-linux-file-diff-tools-comparison/)
[10 Tools to Make Bootable USB Drive from ISO in 2026](https://www.tecmint.com/linux-bootable-usb-creators/)
[5 Best Open-Source Project Management Tools for Linux in 2024](https://www.tecmint.com/linux-project-management-tools/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/ "Scroll back to top")
Search for:
