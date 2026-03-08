[Skip to content](https://www.tecmint.com/yum-thirdparty-repositories-for-centos-rhel/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/yum-thirdparty-repositories-for-centos-rhel/ "Linux Online Courses")
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


[](https://www.tecmint.com/yum-thirdparty-repositories-for-centos-rhel/)
[YUM (Yellowdog Updater Modified)](https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/) is an open-source, widely used command-line and graphical-based package management tool for [RPM (RedHat Package Manager)](https://www.tecmint.com/20-practical-examples-of-rpm-commands-in-linux/) based Linux systems, including, but not limited to, **Red Hat Enterprise Linux** (**RHEL**), **CentOS** , **Scientific Linux** (**SL**), **Oracle Linux** (**OL**), **Rocky Linux** and **AlmaLinux** , which is used to install, update, remove or search software packages on a system.
The [DNF command](https://www.tecmint.com/dnf-commands-for-fedora-rpm-package-management/ "DNF Command Examples") (Dandified yum) is the next-generation version of the traditional YUM package manager for [RedHat-based systems](https://www.tecmint.com/redhat-based-linux-distributions/ "The Best RedHat-based Linux Distributions").
To install software packages that are not included in the default **base** and **update** repositories, as well as **additional** repositories, you need to install and enable other third-party repositories on your system.
In this article, we will review the top **8** **YUM/DNF** repositories for RHEL-based distributions, which are frequently recommended by the Linux community.
**Warning** : You should always remember the repositories listed below are not provided nor supported by **RHEL** ; they may or may not be up to date or behave the way you expect them to – use them at your own risk.
### 1. EPEL Repository
**EPEL** (**Extra Packages for Enterprise Linux**) is a free and open-source, popular, community-based repository project aimed at providing high-quality packages that have been developed, tested, and improved in **Fedora** and made available for **RHEL** , **CentOS** , **Scientific Linux,** and similar Linux distributions. Most of the other repositories listed in this article are dependent on **EPEL**.
To enable the **EPEL** repository on your system, use the following commands.
```
# yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm  [on RHEL 8]
# yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm  [on RHEL 7]
# yum install https://archives.fedoraproject.org/pub/archive/epel/6/x86_64/epel-release-6-8.noarch.rpm  [on RHEL 6]

```

### 2. REMI Repository
**REMI** is a widely used third-party repository that provides the latest versions of the **PHP** stack, and some other related software, to users of **Fedora** and **Enterprise Linux** (**EL**) distributions such as RHEL, CentOS, Oracle, Scientific Linux, and more.
Before you can enable **Remi** , you need to enable the **EPEL** repository first, as follows:
```
**-------- On RHEL 8 --------**
# yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
# yum install https://rpms.remirepo.net/enterprise/remi-release-8.rpm

**-------- On RHEL 7 --------**
# yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
# yum install https://rpms.remirepo.net/enterprise/remi-release-7.rpm

**-------- On RHEL 6 --------**
# yum install https://archives.fedoraproject.org/pub/archive/epel/6/x86_64/epel-release-6-8.noarch.rpm
# yum install https://rpms.remirepo.net/enterprise/remi-release-6.rpm

```

### 3. RPMFusion Repository
**RPMFusion** is a third-party repository that offers some free and non-free add-on software for **Fedora** and **Enterprise Linux** distros including RHEL and CentOS. You need to enable the **EPEL** repo before you enable **RPM Fusion**.
```
**-------- On RHEL 8 --------**
# yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
# yum localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm
# yum localinstall --nogpgcheck https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm

**-------- On RHEL 7 --------**
# yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
# yum localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
# yum localinstall --nogpgcheck https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm

**-------- On RHEL 6 --------**
# yum install https://archives.fedoraproject.org/pub/archive/epel/6/x86_64/epel-release-6-8.noarch.rpm
# yum localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-6.noarch.rpm
# yum localinstall --nogpgcheck https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-6.noarch.rpm

```

### 4. ELRepo Repository
**ELRepo** (**Community Enterprise Linux Repository**) is an **RPM** repository intended to provide hardware-related packages such as filesystem drivers, graphics drivers, network drivers, sound drivers, webcam, and video drivers, to improve your experience with Enterprise Linux.
To enable ELRepo on your system, use the following commands.
```
**-------- On RHEL 8 --------**
# rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
# rpm -Uvh https://www.elrepo.org/elrepo-release-8.el8.elrepo.noarch.rpm

**-------- On RHEL 7 --------**
# rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
# rpm -Uvh https://www.elrepo.org/elrepo-release-7.el7.elrepo.noarch.rpm

**-------- On RHEL 6 --------**
# rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
# rpm -Uvh https://www.elrepo.org/elrepo-release-6-8.el6.elrepo.noarch.rpm

```

### 5. NUX-dextop Repository
**NUX-dextop** is an **RPM** repository for desktop and multimedia software packages for EL. It contains a lot of graphical software and command-line interface (CLI) based programs including [Remmina remote desktop sharing tool](https://www.tecmint.com/remmina-remote-desktop-sharing-and-ssh-client/), [VLC media player](https://www.tecmint.com/install-vlc-media-player-in-rhel-centos-fedora/), and many others.
You also need to enable the **EPEL** repo before you enable **nux-dextop**.
```
**-------- On RHEL 8 --------**
# yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
# yum install http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm

**-------- On RHEL 7 --------**
# yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
# yum install http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm

**-------- On RHEL 6 --------**
# yum install https://archives.fedoraproject.org/pub/archive/epel/6/x86_64/epel-release-6-8.noarch.rpm
# yum install http://li.nux.ro/download/nux/dextop/el6/x86_64/nux-dextop-release-0-2.el6.nux.noarch.rpm

```

### 6. GhettoForge Repository
**GhettoForge** project focuses on providing packages for Enterprise Linux releases **6** and **7** that are not present in the base EL package sets nor in other third-party repositories.
You can enable **GhettoForge** on your system using the following commands.
```
**-------- On RHEL 8 --------**
# yum install http://mirror.ghettoforge.org/distributions/gf/gf-release-latest.gf.el8.noarch.rpm

**-------- On RHEL 7 --------**
# yum install http://mirror.ghettoforge.org/distributions/gf/gf-release-latest.gf.el7.noarch.rpm

**-------- On RHEL 6 --------**
# yum install http://mirror.ghettoforge.org/distributions/gf/gf-release-latest.gf.el6.noarch.rpm

```

### 7. Psychotic Ninja Repository
**Psychotic Ninja** aims to provide high-quality packages that do not exist in the base EL package sets nor in other third-party repositories, for Enterprise Linux releases 6 and 7.
To enable the **Psychotic Ninja** repository, first, you need to import the GPG key and then install it.
```
# rpm --import http://wiki.psychotic.ninja/RPM-GPG-KEY-psychotic
# rpm -ivh http://packages.psychotic.ninja/6/base/i386/RPMS/psychotic-release-1.0.0-1.el6.psychotic.noarch.rpm

```

Note that this unified psychotic-release package works across all releases and architectures, including the 64-bit version of CentOS/RHEL 7.
### 8. IUS Community Repository
Last on the list is, **IUS** (**Inline with Upstream Stable**) is a new third-party, community-supported repo that provides high-quality RPM packages for the latest upstream versions of PHP, Python, MySQL, and Red Hat Enterprise Linux (RHEL), and CentOS.
Just like many of the repos we have looked at, **IUS** also depends on **EPEL**.
```
**-------- On RHEL 7 --------**
# yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
# yum install https://repo.ius.io/ius-release-el7.rpm

```

That’s all! In this article, we reviewed the top **8 YUM/DNF** third-party repositories for RHEL-based Linux, which are frequently recommended by the Linux community. If you know of any other repository that provides high-quality software packages and deserves to be included here, let us know via the comment form below.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Zorin OS Core 16.1 – A Ultimate Linux Desktop for Windows and macOS Users](https://www.tecmint.com/zorin-os-installation-guide-and-review/)
Next article:
[Installation and Review of Q4OS Linux [Lightweight Distro]](https://www.tecmint.com/q4os-linux/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/yum-thirdparty-repositories-for-centos-rhel/#respond)** or
## Related Posts
[![CentOS Stream for Development](https://www.tecmint.com/wp-content/uploads/2013/03/CentOS-Stream-for-Development.webp)](https://www.tecmint.com/centos-stream-for-developers/ "CentOS Stream: The Perfect Distribution for Development Projects")
[![Manage Layered Local Storage with Stratis](https://www.tecmint.com/wp-content/uploads/2024/10/Manage-Layered-Local-Storage-with-Stratis.webp)](https://www.tecmint.com/install-stratis-to-manage-layered-local-storage-on-rhel/ "How to Install Stratis to Manage Layered Local Storage on RHEL 9/8")
[![Linux Disable Unwanted Services](https://www.tecmint.com/wp-content/uploads/2014/09/Linux-Disable-Unwanted-Services.png)](https://www.tecmint.com/disable-unwanted-services-linux/ "How to Disable and Remove Unnecessary Services on Linux")
[![Install Memcached on RHEL](https://www.tecmint.com/wp-content/uploads/2019/03/Install-Memcached-on-RHEL.png)](https://www.tecmint.com/install-memcached-linux/ "Improve Website Performance – Install Memcached on RHEL 9")
[![Migrate CentOS to Rocky Linux](https://www.tecmint.com/wp-content/uploads/2013/01/Migrate-CentOS-to-Rocky-Linux.png)](https://www.tecmint.com/migrate-centos-to-rocky-linux/ "How to Migrate CentOS 7 to Rocky Linux 9")
[![How to Reset Root Password](https://www.tecmint.com/wp-content/uploads/2012/11/Reset-Root-Password.jpg)](https://www.tecmint.com/reset-forgotten-root-password-in-rhel-centos-and-fedora/ "How to Reset Forgotten Root Password in RHEL Systems")
### 2 Comments
[Leave a Reply](https://www.tecmint.com/yum-thirdparty-repositories-for-centos-rhel/#reply-title)
  1. what are the repo file contents
[Reply](https://www.tecmint.com/yum-thirdparty-repositories-for-centos-rhel/#comment-1224026)
     * @rmaniacnyc
You can check the repo file content under the /etc/yum.repos.d/ directory.
[Reply](https://www.tecmint.com/yum-thirdparty-repositories-for-centos-rhel/#comment-1227982)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/yum-thirdparty-repositories-for-centos-rhel/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/yum-thirdparty-repositories-for-centos-rhel/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=7867807779493595&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
