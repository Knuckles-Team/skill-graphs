[Skip to content](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/ "Linux Online Courses")
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


[](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/)
**zzUpdate** is a free, open-source, simple, fully configurable, and easy-to-use command line utility to upgrade an **Ubuntu** system via an [apt package management](https://www.tecmint.com/apt-command-in-linux/) system.
It is a complete config file-driven shell script that allows you to upgrade your **Ubuntu** desktop or server hands-off and unwatched for almost the entire process.
It will upgrade your **Ubuntu** system to the next available release in case of a normal release. For **Ubuntu LTS** (**Long Term Support**) releases, it tries to search for the next **LTS** version only and not the latest Ubuntu version available.
In this article, we will explain how to install and run the **zzupdate** tool to upgrade an **Ubuntu** system to the latest available version from the command line.
## How to Install zzUpdate Tool in Ubuntu
First, make sure that your system has the [git program installed](https://www.tecmint.com/git-basics/ "Learn the Basics of Git"), otherwise, install it using the following command.
```
sudo apt install git

```

Now install **zzupdate** on your **Ubuntu** system by cloning the latest version from its GitHub repository.
```
git clone https://github.com/TurboLabIt/zzupdate.git
cd zzupdate
sudo chmod +x zzupdate.sh

```

Next, create a configuration file named **zzupdate.cfg** to customize the upgrade process or you can start with the example configuration provided in the repository.
```
sudo cp zzupdate.default.conf zzupdate.conf
sudo nano zzupdate.conf

```

Adjust the following default configuration variables (a value of `1` means **yes** and `0` means **no**) you will find in this file.
![zzUpdate Configuration](https://www.tecmint.com/wp-content/uploads/2018/06/zzUpdate-Configuration-1.png)zzUpdate Configuration
Before upgrading your Ubuntu system, you can check your current Ubuntu release using the following [cat command](https://www.tecmint.com/cat-command-linux/ "Cat Command in Linux").
```
cat /etc/os-release

```
![Check Ubuntu Release Version](https://www.tecmint.com/wp-content/uploads/2018/06/Check-Ubuntu-Release-Version-1.png)Check the Ubuntu Release Version
When you have configured **zzupdate** to work the way you wish, simply run it to fully upgrade your Ubuntu system with root user privileges. It will inform you of any actions performed.
```
sudo ./zzupdate.sh

```

Once you have launched it, **zzupdate** will self-update via **git** , update available package information (asks you to disable third-party repositories), upgrade any packages where necessary, and check for a new Ubuntu release.
If there is a new release, it will download the upgrade packages and install them, when the system upgrade is complete, it will prompt you to restart your system.
![Fully Upgrade Ubuntu](https://www.tecmint.com/wp-content/uploads/2018/06/Fully-Upgrade-Ubuntu.png)Fully Upgrade Ubuntu
Once the upgrade is finished, you can verify your **Ubuntu** release to ensure that the upgrade was successful.
```
lsb_release -a
OR
cat /etc/os-release

```

The output will include information about your Ubuntu operating system, kernel, uptime, and more.
![Verify Ubuntu Release Version](https://www.tecmint.com/wp-content/uploads/2024/06/Verify-Ubuntu-Release-Version.png)Verify Ubuntu Release Version
## Troubleshooting
If you encounter issues during the upgrade process, here are some common troubleshooting steps:
**1.** Before running **zzUpdate** , ensure your system is fully up-to-date:
```
sudo apt-get update
sudo apt-get upgrade

```

**2.** If **zzUpdate** encounters an error, check the log file (**/var/log/zzupdate.log**) for detailed information about what went wrong.
```
sudo nano /var/log/zzupdate.log

```

**3.** If there are broken dependencies, you can try to fix them with the following command:
```
sudo apt-get install -f

```

**4.** In some cases, manual intervention may be required. If the script fails, you can manually perform the distribution upgrade:
```
sudo do-release-upgrade

```

##### Conclusion
In this guide, we have explained how to install and use **zzupdate** to upgrade an Ubuntu system from the command line. You can ask any questions via the feedback form below.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install Apache Pinot in Linux](https://www.tecmint.com/install-apache-pinot-in-linux/)
Next article:
[Improve Website Performance – Install Memcached on RHEL 9](https://www.tecmint.com/install-memcached-linux/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/#respond)** or
## Related Posts
[![Best Ubuntu Apps for Beginners](https://www.tecmint.com/wp-content/uploads/2025/05/ubuntu-apps-for-beginners.webp)](https://www.tecmint.com/ubuntu-apps-for-beginners/ "17 Must-Have Tools for Ubuntu Users in 2026")
[![Run Local AI in ONLYOFFICE on Ubuntu Using Ollama](https://www.tecmint.com/wp-content/uploads/2026/01/Run-Local-AI-in-ONLYOFFICE-on-Ubuntu-Using-Ollama.webp)](https://www.tecmint.com/ubuntu-ai-document-editing-onlyoffice-ollama/ "How to Enable AI Document Editing on Ubuntu with ONLYOFFICE and Ollama")
[![Install LAMP Stack on Ubuntu](https://www.tecmint.com/wp-content/uploads/2016/10/Install-LAMP-Stack-on-Ubuntu-24.04.webp)](https://www.tecmint.com/install-lamp-stack-ubuntu/ "How to Install LAMP Stack with PHP 8.3 and MariaDB 11 on Ubuntu 24.04")
[![Install aaPanel Hosting Control Panel in Ubuntu](https://www.tecmint.com/wp-content/uploads/2025/11/Install-aaPanel-Control-Panel-on-Ubuntu.webp)](https://www.tecmint.com/install-aapanel-hosting-control-panel-in-ubuntu/ "How to Install aaPanel Hosting Control Panel in Ubuntu 24.04")
[![Install WireGuard on Ubuntu](https://www.tecmint.com/wp-content/uploads/2025/11/Install-WireGuard-on-Ubuntu.webp)](https://www.tecmint.com/setup-wireguard-vpn-server-web-ui-ubuntu/ "How to Setup WireGuard VPN Server with WireGuard-UI on Ubuntu")
[![Install PostgreSQL on Ubuntu](https://www.tecmint.com/wp-content/uploads/2025/10/Install-PostgreSQL-on-Ubuntu.webp)](https://www.tecmint.com/install-postgresql-on-ubuntu/ "How to Install and Use PostgreSQL 18 on Ubuntu 24.04 LTS")
### 8 Comments
[Leave a Reply](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/#reply-title)
  1. If **zzupdate** is an automatic way of upgrading **Ubuntu** with many steps described in your article, and `do-release-upgrade` is manual according to your writing, I think you got it wrong. `do-release-upgrade` automatically performs all the steps to upgrade Ubuntu; you’ll only have to confirm twice with a `'y'` (yes) or so along the process.
Anyway, **Ubuntu** will not upgrade the **LTS** version until the first point release (**24.04.1**) is out, in order to clear most bugs found meanwhile. **Ubuntu 24.04.1** will be released next August.
[Reply](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/#comment-2185220)
     * @Martins,
Thanks for the clarification! You’re right, `do-release-upgrade` automates the process and only needs a couple of confirmations.
Also, good point about Ubuntu LTS versions waiting for the first point release like 24.04.1.
[Reply](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/#comment-2185677)
  2. Will it work on **Debian OS** as **Debian** also uses the **APT** package manager?
[Reply](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/#comment-2182575)
     * @Mani,
Yes, the **zzupdate** tool should work on **Debian** as well since it uses the **APT** package manager, but I haven’t tested it yet.
[Reply](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/#comment-2183606)
  3. Thanks, but NO. I’ll stick with **apt** and **Synaptic**. No need to introduce another layer to the software update process.
[Reply](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/#comment-2182053)
     * @Dragonmouth,
Thank you for your feedback. I understand your preference for sticking with familiar tools like **apt** and **Synaptic**.
While **zzUpdate** offers a streamlined way to fully upgrade Ubuntu to the latest release, it’s entirely optional and meant to provide an alternative for those who find it convenient.
[Reply](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/#comment-2182273)
  4. I was trying to install **zzUpdate** in my Ubuntu 15.04 version OS. To do so, while installing ‘curl’ I get the following massage:
**E: package curl has no installation candidate**
Any solution?
[Reply](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/#comment-1252116)
     * @Sumit,
Try to change the mirror server to main server.
Open **System settings > Software & Updates > Ubuntu Software >** and make sure to select all sources (main, universe, restricted, and multiverse) and select download from the Main server.
Now try again `sudo apt-get update && sudo apt-get install curl`
[Reply](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/#comment-1253305)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/zzupdate-upgrade-ubuntu-to-newer-version/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=4598205190194808&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
