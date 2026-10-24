[Skip to content](https://www.tecmint.com/add-hosts-in-opennms-monitoring/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/add-hosts-in-opennms-monitoring/)
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
  * [Pro Courses](https://www.tecmint.com/add-hosts-in-opennms-monitoring/ "Linux Online Courses")
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


[](https://www.tecmint.com/add-hosts-in-opennms-monitoring/)
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
  * [Pro Courses](https://www.tecmint.com/add-hosts-in-opennms-monitoring/ "Linux Online Courses")
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


[](https://www.tecmint.com/add-hosts-in-opennms-monitoring/)
# How to Add Hosts in OpenNMS Monitoring Server
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: June 24, 2019 Read Time: 1 minCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [Leave a comment](https://www.tecmint.com/add-hosts-in-opennms-monitoring/#respond)
In our first part of this article, we have described in detail on how to install and configure the latest **OpenNMS** network monitoring platform on **CentOS/RHEL** as well as on **Ubuntu/Debian** server. In this article, we will show you how to add hosts/server nodes to **OpenNMS**.
We hope you already having **OpenNMS** installed and running properly. If not, please use the following guides to install it on your system.
  1. [Install OpenNMS Network Monitoring Tool in CentOS/RHEL 7](https://www.tecmint.com/install-opennms-network-monitoring-in-centos-rhel/)
  2. [Install OpenNMS Network Monitoring in Debian and Ubuntu](https://www.tecmint.com/install-opennms-in-debian-and-ubuntu/)


### Adding Hosts in OpenNMS
**1.** Log into your **OpenNMS** web console, go to the main navigation menu, click “**admin → Quick Add Node** ”. Then create a “**Provisioning Requisition** ”: a requisition tells OpenNMS what to monitor and it consists of nodes. In this case, our requisition is called **Group 1**.
![Add Requisition in OpenNMS](https://www.tecmint.com/wp-content/uploads/2019/06/add-requisition.png)Add Requisition in OpenNMS
**2.** Now set the basic attributes of the new node. Select the **Requisition** , add the node IP address and set a node label. In addition, also add a **Surveillance Category Memberships** by clicking on **Add Category** , then select the category from the drop-down menu.
![Add Node Attributes](https://www.tecmint.com/wp-content/uploads/2019/06/add-node-attributes.png)Add Node Attributes
The other sections are optional but you can set their values appropriately. To save the changes, scroll down to the end and click **Provision**.
![Node Added to OpenNMS](https://www.tecmint.com/wp-content/uploads/2019/06/node-added-successfully.png)Node Added to OpenNMS
**3.** Now if you go back to **home** , the under **Status Overview** , you should be able to see one node added. And under **Availability Over the Past 24 Hours** section, **OpenNMS** tries to discover different categories of services (such as Web Servers, Email Servers, DNS and DHCP Servers, Database Servers, and more) on the just added node. It shows the total number of services under each category and the number of outages, and the corresponding percentage of **Availability**.
The left panel also shows some useful information concerning Pending situations, Nodes with Pending Problems, Nodes with Outages and more. Importantly, the right panel shows Notifications and allows you to search Resource Groups, KSC Reports and Nodes via the Quick Search.
![OpenNMS Status Overview](https://www.tecmint.com/wp-content/uploads/2019/06/opennms-status-overview.png)OpenNMS Status Overview
You can go on and add more nodes to monitor by following the above procedure. To view all nodes added, go to the main navigation menu, click **Info → Nodes**.
![View OpenNMS Nodes](https://www.tecmint.com/wp-content/uploads/2019/06/view-all-nodes.png)View OpenNMS Nodes
**4.** To analyze a single node, click on it from the above interface. For example **cserver3**.
![Analyze a Single Node](https://www.tecmint.com/wp-content/uploads/2019/06/analyze-a-single-node.png)Analyze a Single Node
For more information, see the
Tags [linux network monitoring](https://www.tecmint.com/tag/linux-network-monitoring/), [linux server monitoring](https://www.tecmint.com/tag/linux-server-monitoring/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Setting Up Bind As a Private DNS Server on RHEL 8](https://www.tecmint.com/install-bind-private-dns-server-on-rhel-8/)
Next article:
[8 Partx Command Usage Examples in Linux](https://www.tecmint.com/partx-command-in-linux-with-examples/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/add-hosts-in-opennms-monitoring/#respond)** or
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
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/add-hosts-in-opennms-monitoring/#respond)
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
[How to Disable ‘su’ Access for Sudo Users](https://www.tecmint.com/disable-su-access-sudo-users/)
[Zaloha.sh – A Simple Local Directory Synchronizer Script for Linux](https://www.tecmint.com/local-directory-synchronizer-for-linux/)
[How to Show Asterisks While Typing Sudo Password in Linux](https://www.tecmint.com/show-asterisks-sudo-password-in-linux/)
[sysget – A Front-end for Every Package Manager in Linux](https://www.tecmint.com/sysget-front-end-package-manager-in-linux/)
[Transfer.sh – Easy File Sharing from Linux Commandline](https://www.tecmint.com/file-sharing-from-linux-commandline/)
[6 Useful Tools to Remember Linux Commands Forever](https://www.tecmint.com/remember-linux-commands/)
## Linux Server Monitoring Tools
[How to Monitor Performance Of CentOS 8/7 Server Using Netdata](https://www.tecmint.com/monitor-centos-server-performance/)
[6 Useful Tools to Monitor MongoDB Performance](https://www.tecmint.com/monitor-mongodb-performance/)
[Suricata – A Intrusion Detection, Prevention, and Security Tool](https://www.tecmint.com/suricata-intrusion-detection-prevention-linux/)
[Netdata – A Real-Time Performance Monitoring Tool for Linux Systems](https://www.tecmint.com/netdata-real-time-linux-performance-network-monitoring-tool/)
[Will ‘Htop’ Replace Default ‘Top’ Monitoring Tool in Linux?](https://www.tecmint.com/htop-vs-top-in-linux/)
[How to Monitor Website and Application with Uptime Kuma](https://www.tecmint.com/uptime-kuma-linux-website-monitoring-tool/)
## Learn Linux Tricks & Tips
[How to Create Multiple User Accounts in Linux](https://www.tecmint.com/create-multiple-user-accounts-in-linux/)
[5 Useful Ways to Do Arithmetic in Linux Terminal](https://www.tecmint.com/arithmetic-in-linux-terminal/)
[Learn Why ‘less’ is Faster Than ‘more’ Command for Effective File Navigation](https://www.tecmint.com/linux-more-command-and-less-command-examples/)
[4 Ways to Send Email Attachment from Linux Command Line](https://www.tecmint.com/send-email-attachment-from-linux-commandline/)
[How to Compress and Decompress a .bz2 File in Linux](https://www.tecmint.com/linux-compress-decompress-bz2-files-using-bzip2/)
[Rename All Files and Directory Names to Lowercase in Linux](https://www.tecmint.com/rename-all-files-and-directory-names-to-lowercase-in-linux/)
## Best Linux Tools
[5 Best Reference Management Software for Linux in 2024](https://www.tecmint.com/reference-management-software/)
[Top 3 Open Source Virtual Data Room (VDR) for Linux](https://www.tecmint.com/open-source-virtual-data-room-for-linux/)
[8 Best RDP (Remote Desktop) Clients for Linux in 2024](https://www.tecmint.com/best-linux-rdp-remote-desktop-clients/)
[17 Best KDE Multimedia Applications for Linux](https://www.tecmint.com/kde-multimedia-applications/)
[11 Best Screen Recorders For Linux in 2024](https://www.tecmint.com/best-linux-screen-recorders-for-desktop-screen-recording/)
[5 Best Open-Source eLearning Platforms for Linux in 2024](https://www.tecmint.com/open-source-elearning-platforms-for-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/add-hosts-in-opennms-monitoring/ "Scroll back to top")
Search for:
