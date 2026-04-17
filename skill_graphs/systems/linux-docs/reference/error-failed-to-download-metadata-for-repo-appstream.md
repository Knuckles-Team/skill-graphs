[Skip to content](https://www.tecmint.com/error-failed-to-download-metadata-for-repo-appstream/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/error-failed-to-download-metadata-for-repo-appstream/ "Linux Online Courses")
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


[](https://www.tecmint.com/error-failed-to-download-metadata-for-repo-appstream/)
If you, for one reason or the other, are still actively using **CentOS 8** , you might probably have encountered the following error when trying to update your system or simply install a package.
“**Error: Failed to download metadata for repo ‘appstream’: Cannot prepare internal mirrorlist: No URLs in mirrorlist** ”
For example, in the screenshot that follows, I was trying to install the **fio** package and run into it.
![Error: Failed to Download Metadata for Repo 'AppStream'](https://www.tecmint.com/wp-content/uploads/2022/08/Error-Failed-to-Download-Metadata-for-Repo-AppStream.png)Error: Failed to Download Metadata for Repo ‘AppStream’
#### What is the Cause of This Error?
You may well be aware that **CentOS Linux 8** died a premature death, it reached the End Of Life (EOL) on December 31st, 2021, thus it no longer receives development resources from the official CentOS project.
This means that after Dec 31st, 2021, to update your CentOS installation, you are required to change the mirrors to
### Fix Error: Failed to Download Metadata for Repo ‘AppStream’
To fix the above error, open your terminal or login via ssh, and run the following commands to change the repo URL to point to **vault.centos.org** , from the official CentOS repos.
Here we use the **sed** command to edit the required directives or parameters in the repo configuration files:
```
# sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
# sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

```

Alternatively, you can also point to the Cloudflare-based vault repository, by running the following commands:
```
# sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-Linux-*
# sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.epel.cloud|g' /etc/yum.repos.d/CentOS-Linux-*

```

Now you should be able to update **CentOS** or install packages without any error:
![Install Packages in CentOS 8](https://www.tecmint.com/wp-content/uploads/2022/08/Install-Packages-in-CentOS-8.png)Install Packages in CentOS 8
If you wish to migrate from **CentOS 8** to **Rock Linux 8** or **AlamLinux 8** , check these guides:
  * [How to Migrate from CentOS 8 to Rocky Linux 8](https://www.tecmint.com/migrate-centos-8-to-rocky-linux/ "Migrate from CentOS 8 to Rocky Linux 8")
  * [How to Migrate from CentOS 8 to AlmaLinux 8.5](https://www.tecmint.com/migrate-centos-8-to-almalinux/ "Migrate from CentOS 8 to AlmaLinux 8.5")


That’s all! We hope that this guide helped you fix the above-aforementioned error. Use the comment form below to share feedback with us, you can ask questions as well.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install Latest LAMP Stack in RHEL-based Distributions](https://www.tecmint.com/install-lamp-in-rhel-based-distributions/)
Next article:
[How to Install LMDE 5 “Elsie” Cinnamon Edition](https://www.tecmint.com/install-linux-mint-debian-edition/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/error-failed-to-download-metadata-for-repo-appstream/#respond)** or
## Related Posts
[![CentOS Stream for Development](https://www.tecmint.com/wp-content/uploads/2013/03/CentOS-Stream-for-Development.webp)](https://www.tecmint.com/centos-stream-for-developers/ "CentOS Stream: The Perfect Distribution for Development Projects")
[![Manage Layered Local Storage with Stratis](https://www.tecmint.com/wp-content/uploads/2024/10/Manage-Layered-Local-Storage-with-Stratis.webp)](https://www.tecmint.com/install-stratis-to-manage-layered-local-storage-on-rhel/ "How to Install Stratis to Manage Layered Local Storage on RHEL 9/8")
[![Linux Disable Unwanted Services](https://www.tecmint.com/wp-content/uploads/2014/09/Linux-Disable-Unwanted-Services.png)](https://www.tecmint.com/disable-unwanted-services-linux/ "How to Disable and Remove Unnecessary Services on Linux")
[![Install Memcached on RHEL](https://www.tecmint.com/wp-content/uploads/2019/03/Install-Memcached-on-RHEL.png)](https://www.tecmint.com/install-memcached-linux/ "Improve Website Performance – Install Memcached on RHEL 9")
[![Migrate CentOS to Rocky Linux](https://www.tecmint.com/wp-content/uploads/2013/01/Migrate-CentOS-to-Rocky-Linux.png)](https://www.tecmint.com/migrate-centos-to-rocky-linux/ "How to Migrate CentOS 7 to Rocky Linux 9")
[![How to Reset Root Password](https://www.tecmint.com/wp-content/uploads/2012/11/Reset-Root-Password.jpg)](https://www.tecmint.com/reset-forgotten-root-password-in-rhel-centos-and-fedora/ "How to Reset Forgotten Root Password in RHEL Systems")
### 3 Comments
[Leave a Reply](https://www.tecmint.com/error-failed-to-download-metadata-for-repo-appstream/#reply-title)
  1. Great! Following your steps worked for me as well.
Thank you for the clear instructions on fixing the ‘**Failed to Download Metadata for Repo ‘AppStream’** ‘ error.
[Reply](https://www.tecmint.com/error-failed-to-download-metadata-for-repo-appstream/#comment-2183702)
  2. It works, thanks for trick
[Reply](https://www.tecmint.com/error-failed-to-download-metadata-for-repo-appstream/#comment-2182002)
  3. This is used for CentOS Linux, but in the case of centos appstream use the following trick
Go to **/etc/yum.repos.d**.
Add in CentOS-Stream-AppStream.repo
baseurl=http://mirror.centos.org/centos/8-stream/AppStream/x86_64/os/
Add in CentOS-Stream-BaseOS.repo
baseurl=http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/
Add in CentOS-Stream-Extras.repo
baseurl=http://mirror.centos.org/centos/8-stream/extras/x86_64/os/
CentOS-Stream-Extras-common.repo
baseurl=https://vault.centos.org/centos/8-stream/extras/Source/extras-common/
[Reply](https://www.tecmint.com/error-failed-to-download-metadata-for-repo-appstream/#comment-1883815)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/error-failed-to-download-metadata-for-repo-appstream/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/error-failed-to-download-metadata-for-repo-appstream/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=4196664062862657&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
