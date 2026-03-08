[Skip to content](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/)
**rdesktop** is an open source software that enables you to connect and manage your remote Windows desktop from your Linux computer using **RDP – Remote Desktop Protocol**. In other words, while you are sitting in front of your Linux system at home or office, and access your Windows desktop as if you’re sitting in front of the Windows machine.
**Read Also** : [11 Best Tools to Access Remote Linux Desktop](https://www.tecmint.com/best-remote-linux-desktop-sharing-software/)
In this article, we will explain how to install **rdesktop** in Linux system to access the remote desktop of **Windows** computer using the **Hostname** and **IP Address**.
#### Windows Settings
To enable **rdesktop** to connect to any given Windows machine, you need to make few following changes on the Windows box itself.
  1. Enable **RDP** port no. **3389** in **Firewall**.
  2. Enable remote desktop under **Windows Operating System**.
  3. Require at least one **user** with a **password**.


Once you make all of the above Windows configuration settings, you can now move further to install **rdesktop** on your Linux system to access your Windows desktop.
### Install rdesktop (Remote Desktop) in Linux
It is always preferable to use a default package manager such as [yum](https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/), [dnf](https://www.tecmint.com/dnf-commands-for-fedora-rpm-package-management/) or [apt](https://www.tecmint.com/apt-advanced-package-command-examples-in-ubuntu/) to install software to handle dependencies automatically during installation.
```
# yum install rdesktop   [On CentOS/RHEL 7]
# dnf install rdesktop   [On CentOS/RHEL 8 and Fedora]
# apt install rdesktop   [On Debian/Ubuntu]

```

If **rdesktop** is not available to install from the default repositories, you can download the tarball from Github [wget command](https://www.tecmint.com/10-wget-command-examples-in-linux/) to download and install it as shown.
```
# wget https://github.com/rdesktop/rdesktop/releases/download/v1.8.6/rdesktop-1.8.6.tar.gz
# tar xvzf rdesktop-1.8.6.tar.gz
# cd rdesktop-1.8.6/
# ./configure --disable-credssp --disable-smartcard
# make
# make install

```

### Connecting to Windows Desktop Using Hostname
To connect **Windows** host from **Linux** desktop type following command using **-u** parameter as **username** (**narad**) and (**ft2**) as the **hostname** of my **Windows** host. To resolve hostname make an entry at **/etc/hosts** file if you don’t have **DNS Server** in your environment.
```
**# rdesktop -u narad ft2**
```
![rdesktop using hostname](https://www.tecmint.com/wp-content/uploads/2012/09/rdesk-04.png) Use rdesktop using hostname
### Connecting to Windows Desktop Using IP Address
To connect **Windows** host from **Linux** machine, use **username** as (**narad**) and **IP Address** as (**192.168.50.5**) of my windows host, the command would be as.
```
**# rdesktop -u narad 192.168.50.5**
```
![rdesktop using IP Address](https://www.tecmint.com/wp-content/uploads/2012/09/rdesk-05.png) Use rdesktop using IP Address
Please execute **man rdesktop** in command prompt If you would like to know more about it or visit
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install Node.js in RHEL 8](https://www.tecmint.com/install-node-js-in-rhel-8/)
Next article:
[4 Process Managers for Node.js Applications in Linux](https://www.tecmint.com/process-managers-for-node-js-applications-in-linux/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#respond)** or
## Related Posts
[![LocalSend Share Files Between Linux and Windows](https://www.tecmint.com/wp-content/uploads/2016/09/localsend-share-files-between-linux-and-windows.webp)](https://www.tecmint.com/localsend-share-files-linux-windows/ "LocalSend – Local Network File Sharing Between Linux, Windows and Mac")
[![Why the Modern World Runs on Linux](https://www.tecmint.com/wp-content/uploads/2014/02/Why-Modern-World-Runs-on-Linux.webp)](https://www.tecmint.com/why-the-world-runs-on-linux/ "Why Linux Powers Everything From Your Coffee Machine to Mars Rovers")
[![introduction to makefiles gnu make in Linux](https://www.tecmint.com/wp-content/uploads/2014/03/introduction-to-makefiles-gnu-make.webp)](https://www.tecmint.com/introduction-to-makefiles-gnu-make/ "A Brief Introduction to Makefiles and GNU Make for Beginners")
[![mkcert: Make Locally-Trusted Development Certificates on Linux](https://www.tecmint.com/wp-content/uploads/2025/07/mkcert-Create-Trusted-SSL-Certificates-for-Local-Development.webp)](https://www.tecmint.com/mkcert-create-ssl-certs-for-local-development/ "mkcert: Make Locally-Trusted Development Certificates on Linux")
[![Fix Kernel Panic in Linux](https://www.tecmint.com/wp-content/uploads/2013/12/Fix-Kernel-Panic-in-Linux.webp)](https://www.tecmint.com/fix-kernel-panic-linux/ "How to Trigger and Fix a Linux Kernel Panic")
[![LogKey - Monitor Keyboard Keystrokes in Linux](https://www.tecmint.com/wp-content/uploads/2014/01/LogKeys-Monitor-Keyboard-Keystrokes-in-Linux.webp)](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/ "LogKeys: Monitor Keyboard Keystrokes in Linux")
### 20 Comments
[Leave a Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#reply-title)
  1. On my Red Hat 8.2, I had first to run:
```
# dnf install libX11-devel libXcursor-devel libtasn1-devel nettle-devel gnutls-devel

```

And then it worked with:
```
# ./configure --disable-credssp --disable-smartcard

```
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-1357208)
     * We have **Debian** only with the **SSH** package installed and **RDESKTOP** in the call center with 16 machines logging into the Windows Server 2016 TS. However, if an employee goes out to have a coffee and the computer is without activity, he drops the rdesktop and returns to the home screen. Debian is ready with login and password. How do I never go into standby?
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-1705426)
  2. How I redirect printer from Windows to Ubuntu with the help of rdesktop?
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-1296948)
  3. I have installed the rdesktop successfully, but the Rdesktop application not working…
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-1283635)
     * @Harish,
Any error you getting while starting rdesktop? could you share?
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-1284085)
  4. How to install rdesktop offline (without internet) mode or downloaded package.
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-993662)
     * @Thiruvengadam,
Run the following commands to install rdesktop offline on any Linux distribution.
```
# wget https://github.com/rdesktop/rdesktop/releases/download/v1.8.3/rdesktop-1.8.3.tar.gz
# tar -xvf rdesktop-1.8.3.tar.gz
# cd rdesktop*
# ./configure
# make
# make install

```
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-993666)
  5. I installed rdesktop, but I noticed that day by day he keeps flashing the screen, has updated video drive and nothing …. anyone have any tips?
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-884474)
  6. In a GUI environment.
yum -y install rdesktop
yum -y install tsclient
The tsclient is a frontend that makes it easy to use rdesktop (and vncviewer). You should now see “Teminal Server Client” in the Internet tab in GUI.
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-751366)
  7. Its very useful
Thanks
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-738002)
  8. can we use it for linux-linux sharing………????????
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-536262)
     * @Kiran,
Yes, you can use this tool to share your Linux desktop too..
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-536273)
  9. let help me I am not configure mail server in Linux5.1
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-337160)
  10. Hi, am unable to install rdesktop package in rhel 6 terminal.it says
Unable to read consumer identity
No package rdesktop available. what to do ?
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-272635)
  11. great tutorial man… but i’d most like to use free nx in installing RDP on my centos server. it more fast and great work..
thanks for tutorial…
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-266493)
  12. Thank you!!
I was able to connect to a windows machine. If I go to full screen then I was unable to get back. Screen remain full in the windows machine. I tried restarting the remote windows machine, then the current(linux) machine screen frozen at the shutdown screen of the remote windows machine.
Question is,
how do I get back to the physical Linux machine from the remote full screen windows machine?
Thank you.
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-156840)
     * Use key combination ctrl+enter key to come back from fullscreen.
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-772047)
  13. -When I type rdesktop -u hourhour hour; it appears ” Error: getaddrinfo: Name or Sevice not Know.
-When I type rdesktop -u hourhour 192.168.0.10; it appears ” Error: Unable to connect.” .
Thank you for your reply.
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-128537)
  14. I’m amazed, I have to admit. Seldom do I come across a blog that’s both equally
educative and amusing, and let me tell you, you have hit the nail on
the head. The issue is something that not enough people are
speaking intelligently about. Now i’m very happy I found this in my search for something relating to this.
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-31822)
  15. Hy,
I have installed rdesktop+grdesktop,
congratulations for your work. Can you help me?
How i can delete ip adress in General/Logon Settings/Computer: ………….
Thanks you very much
[Reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#comment-25706)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/rdesktop-connect-windows-desktop-from-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
