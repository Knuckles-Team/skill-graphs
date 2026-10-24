[Skip to content](https://www.tecmint.com/install-htop-on-centos-8/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/install-htop-on-centos-8/)
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
  * [Pro Courses](https://www.tecmint.com/install-htop-on-centos-8/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-htop-on-centos-8/)
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
  * [Pro Courses](https://www.tecmint.com/install-htop-on-centos-8/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-htop-on-centos-8/)
# How to Install htop on CentOS 8
[James Kiarie](https://www.tecmint.com/author/james2030kiarie/ "View all posts by James Kiarie")Last Updated: November 15, 2019 Read Time: 1 minCategories [CentOS](https://www.tecmint.com/category/linux-distros/centos/), [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [2 Comments](https://www.tecmint.com/install-htop-on-centos-8/#comments)
If you are looking to monitor your system interactively, then the **htop command** should be one of your best options. An improvement of its predecessor [top command](https://www.tecmint.com/12-top-command-examples-in-linux/), **htop** is an interactive process viewer and system monitor that displays resource-usage metrics in color and allows you to easily keep tabs on your system’s performance.
It displays information about CPU & RAM utilization, tasks being carried out, load average and uptime. Additionally, **htop** displays a [list of all the running processes](https://www.tecmint.com/list-all-running-services-under-systemd-in-linux/) and can also display these [processes in a tree-like format](https://www.tecmint.com/linux-tree-command-examples/).
#### Advantages of htop over top include
  1. Colored output resource usage statistics.
  2. The ability to end or [kill processes](https://www.tecmint.com/find-and-kill-running-processes-pid-in-linux/) without typing their PIDs.
  3. Htop allows mouse usage, unlike top which doesn’t support it.
  4. Better performance than top command.


Let’s now jump in and see how to install this handy feature.
### Install htop on CentOS 8
By default, **htop** comes pre-installed on **CentOS8**. However, if by any chance the tool is missing on your system, installation is an easy 3 step process.
**1.** The first step in the installation of the Htop tool is to enable the EPEL repository. To do so, run:
```
# dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

```

After the installation of the EPEL repository, update the system.
```
# dnf update

```

**2.** To install **htop** tool, simply run the command:
```
# dnf install htop

```
![Install htop in CentOS 8](https://www.tecmint.com/wp-content/uploads/2019/11/Install-htop-in-CentOs-8.png)Install htop in CentOS 8
After the installation is complete, you can find more information about **htop** by running the command.
```
# dnf info htop

```
![Get htop Info](https://www.tecmint.com/wp-content/uploads/2019/11/htop-info.png)Get htop Info
**3.** To launch **htop** , simply run the command.
```
# htop

```
![htop - interactive system-monitor process-viewer and process-manager](https://www.tecmint.com/wp-content/uploads/2019/11/htop-command.png)htop – interactive system-monitor process-viewer and process-manager
Additionally, you can pass some arguments to the command. For example, to list the processes of a user. let’s say **tecmint** run the command.
```
# htop -u tecmint

```
![htop List User Processes](https://www.tecmint.com/wp-content/uploads/2019/11/htop-List-User-Processes.png)htop List User Processes
To get help with the command usage, simply run.
```
# htop --help

```
![Get htop Help](https://www.tecmint.com/wp-content/uploads/2019/11/Get-htop-Help.png)Get htop Help
Alternatively, you can view the man pages by running:
```
# man htop

```

##### Conclusion
In this article, you learned how to install **htop** on **CentOS 8** and how to use the command to retrieve system statistics.
Tags [CentOS Tips](https://www.tecmint.com/tag/centos-tips/), [linux server monitoring](https://www.tecmint.com/tag/linux-server-monitoring/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Set Up Automatic Updates for CentOS 8](https://www.tecmint.com/setup-automatic-updates-for-centos-8/)
Next article:
[How to Disable NetworkManager in CentOS/RHEL 8](https://www.tecmint.com/disable-networkmanager-in-centos/)
![Photo of author](https://secure.gravatar.com/avatar/3b060d6a6c8d6305817bda1435529b27f2d4f900a7998bd703a17094636601a9?s=100&d=blank&r=g)
James Kiarie
This is James, a certified Linux administrator and a tech enthusiast who loves keeping in touch with emerging trends in the tech world. When I'm not running commands on the terminal, I'm taking listening to some cool music. taking a casual stroll or watching a nice movie.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-htop-on-centos-8/#respond)** or
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
### 2 Comments
[Leave a Reply](https://www.tecmint.com/install-htop-on-centos-8/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/e781bf8d6bf5a32269203c9484f3c11aa32708e32539ba7f2dc0778d54dc22bf?s=50&d=blank&r=g)
Rob
[ May 1, 2020 at 11:02 pm  ](https://www.tecmint.com/install-htop-on-centos-8/#comment-1331248)
epel-release is part of centos8.
simply perform
```
# dnf install epel-release

```
[Reply](https://www.tecmint.com/install-htop-on-centos-8/#comment-1331248)
     * ![](https://secure.gravatar.com/avatar/3b060d6a6c8d6305817bda1435529b27f2d4f900a7998bd703a17094636601a9?s=50&d=blank&r=g)
James Kiarie
[ May 4, 2020 at 1:52 pm  ](https://www.tecmint.com/install-htop-on-centos-8/#comment-1331685)
Hey Rob. You’re very correct. I’ve just tried on an instance of CentOS 8.
[Reply](https://www.tecmint.com/install-htop-on-centos-8/#comment-1331685)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-htop-on-centos-8/#respond)
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
[How to Block USB Storage Devices in Linux Servers](https://www.tecmint.com/block-usb-storage-devices-in-linux/)
[Level Up Linux: 20 Must-Know Commands for Newbies](https://www.tecmint.com/useful-linux-commands-for-newbies/)
[10 Most Dangerous Commands – You Should Never Execute on Linux](https://www.tecmint.com/dangerous-linux-commands/)
[How to Find Out List of All Open Ports in Linux](https://www.tecmint.com/find-open-ports-in-linux/)
[How to Use the Linux column Command to Format Text into Tables](https://www.tecmint.com/linux-column-command/)
[How to Temporarily Set a Static IP Address on a Linux System](https://www.tecmint.com/temporary-static-ip-linux/)
## Linux Server Monitoring Tools
[Perf- A Performance Monitoring and Analysis Tool for Linux](https://www.tecmint.com/perf-performance-monitoring-and-analysis-tool-for-linux/)
[Install OpenNMS Network Monitoring Tool in CentOS/RHEL 7](https://www.tecmint.com/install-opennms-network-monitoring-in-centos-rhel/)
[15 Useful Performance and Network Monitoring Tools for Linux](https://www.tecmint.com/linux-performance-monitoring-tools/)
[Understand Linux Load Averages and Monitor Performance of Linux](https://www.tecmint.com/understand-linux-load-averages-and-monitor-performance/)
[How to Add Hosts in OpenNMS Monitoring Server](https://www.tecmint.com/add-hosts-in-opennms-monitoring/)
[How to Install Icinga2 Monitoring Tool on Ubuntu 20.04/22.04](https://www.tecmint.com/install-icinga-monitoring-ubuntu/)
## Learn Linux Tricks & Tips
[3 Ways to Extract and Copy Files from ISO Image in Linux](https://www.tecmint.com/extract-files-from-iso-files-linux/)
[How to Manage User Password Expiration and Aging in Linux](https://www.tecmint.com/manage-user-password-expiration-and-aging-in-linux/)
[How to Find and Sort Files Based on Modification Date and Time in Linux](https://www.tecmint.com/find-and-sort-files-modification-date-and-time-in-linux/)
[Fd – The Best Alternative to ‘Find’ Command for Quick File Searching](https://www.tecmint.com/fd-alternative-to-find-command/)
[4 Ways to Generate a Strong Pre-Shared Key (PSK) in Linux](https://www.tecmint.com/generate-pre-shared-key-in-linux/)
[How to Search and Remove Directories Recursively on Linux](https://www.tecmint.com/find-remove-directory-in-linux/)
## Best Linux Tools
[5 Best Open Source Internet Radio Player for Linux](https://www.tecmint.com/internet-radio-player-linux/)
[5 CLI Tools for Downloading Files and Browsing Internet in Terminal](https://www.tecmint.com/linux-command-line-tools-for-downloading-files/)
[8 Best Open-Source Disk Cloning & Backup Tools for Linux (2024)](https://www.tecmint.com/linux-disk-cloning-tools/)
[16 Best Tools to Access Remote Linux Desktop](https://www.tecmint.com/best-remote-linux-desktop-sharing-software/)
[10 Best Open Source Forum Software for Linux in 2024](https://www.tecmint.com/best-open-source-forum-software-for-linux/)
[8 Best SSH Clients for Linux in 2024](https://www.tecmint.com/ssh-clients-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-htop-on-centos-8/ "Scroll back to top")
Search for:
