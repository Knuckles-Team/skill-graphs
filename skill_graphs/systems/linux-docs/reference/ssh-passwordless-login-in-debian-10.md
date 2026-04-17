[Skip to content](https://www.tecmint.com/ssh-passwordless-login-in-debian-10/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/ssh-passwordless-login-in-debian-10/ "Linux Online Courses")
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


[](https://www.tecmint.com/ssh-passwordless-login-in-debian-10/)
**SSH** (**Secure Shell**) is a popular and widely used tool for remote login and file transfers over insecure networks, that uses encryption to secure the connection between a client and a server.
**Read Also** : [How to Setup Two Factor Authentication for SSH on Linux](https://www.tecmint.com/two-factor-authentication-for-ssh-on-fedora/)
Whereas it is possible to use SSH with an ordinary user ID and password as credentials, it is more and recommended to use key-based authentication (or public key authentication) to authenticate hosts to each other and this is referred to as SSH password-less login.
#### Requirements:
  1. [Install a Debian 10 (Buster) Minimal Server](https://www.tecmint.com/install-debian-10-minimal-server/)


To easily understand this, I will be using two servers:
  * 192.168.56.100 – (tecmint) – A **CentOS 7** server from which I will be connecting to **Debian 10**.
  * 192.168.56.108 – (tecmint) – My **Debian 10** system with password-less login.


In this article, we will show you how to install **OpenSSH** server setup SSH password-less login on **Debian 10** Linux distribution.
### Installing OpenSSH Server on Debian 10
Before you can configure SSH password-less login on your **Debian 10** system, you need to install and configure the OpenSSH server package on the system using the following commands.
```
$ sudo apt-get update
$ sudo apt-get install openssh-server

```

Next, start the **sshd** service for now, then check if it is up and running using the [systemctl command](https://www.tecmint.com/manage-services-using-systemd-and-systemctl-in-linux/) as follows.
```
$ sudo systemctl start sshd
$ sudo systemctl status sshd

```

Then enable the **sshd** service to automatically start at system boot, every time the system is rebooted as follows.
```
$ sudo systemctl start sshd

```

Verify the **sshd** service, which by default listens on port **22** using the **ss command** as shown. If you want you can change SSH Port as shown: [How to Change SSH Port in Linux](https://www.tecmint.com/change-ssh-port-in-linux/).
```
$ sudo ss -tlpn

```
![Check SSH Port in Debian](https://www.tecmint.com/wp-content/uploads/2019/07/check-sshd-port.png)Check SSH Port in Debian
### Setting Up SSH Key on CentOS 7 (192.168.56.100)
First, you need to create an SSH key pair (public key and private key) on the **CentOS 7** system from where you will be connecting to your **Debian 10** server by using the **ssh-keygen** utility as follows.
```
$ ssh-keygen

```

Then enter a meaningful name for the file or leave the default one (this should be the full path as shown in the screenshot, otherwise the files will be created in the current directory). When asked for a passphrase, simply press **“enter”** and leave the password empty. The key files are usually stored in the `~/.ssh` directory by default.
![Generate SSH Key Pair](https://www.tecmint.com/wp-content/uploads/2019/07/generate-ssh-key-pair.png)Generate SSH Key Pair
### Copying the Public Key to Debian 10 Server (192.168.56.108)
After creating the key pair, you need to copy the public key to the **Debian 10** server. You can use the **ssh-copy-id** utility as shown (you will be asked a password for the specified user on the server).
```
$ ssh-copy-id -i ~/.ssh/debian10 tecmint@192.168.56.108

```
![Copy SSH Key to Debian 10](https://www.tecmint.com/wp-content/uploads/2019/07/copy-key-to-debian-10-server.png)Copy SSH Key to Debian 10
The above command logs into the **Debian 10** server, and copies keys to the server, and configures them to grant access by adding them to the authorized_keys file.
### Testing SSH Passwordless Login from 192.168.20.100
Now that the key has been copied to the **Debian 10** server, you need to test if SSH password-less login works by running the following SSH command. The login should now complete without asking for a password, but if you created a passphrase, you need to enter it before access is granted.
```
$ ssh -i ~/.ssh/debian10 tecmint@192.168.56.108

```
![Check SSH Passwordless Login to Debian 10](https://www.tecmint.com/wp-content/uploads/2019/07/Check-Passwordless-ssh-login.png)Check SSH Passwordless Login to Debian 10
In this guide, we have shown you how to install **OpenSSH** server with SSH password-less Login or key-based authentication (or public key authentication) in **Debian 10**. If you want to ask any question related to this topic or share any ideas, use the feedback form below.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install Redis on Ubuntu](https://www.tecmint.com/install-redis-on-ubuntu/)
Next article:
[How to Setup Free SSL Certificate for Apache on Debian 10](https://www.tecmint.com/setup-free-ssl-certificate-for-apache-on-debian-10/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/ssh-passwordless-login-in-debian-10/#respond)** or
## Related Posts
[![Fix “404 Not Found” Errors in Debian apt Update](https://www.tecmint.com/wp-content/uploads/2025/11/fix-apt-get-404-errors-debian.webp)](https://www.tecmint.com/fix-apt-get-404-errors-debian/ "How to Fix “404 Not Found” Errors in Debian During apt-get upgrade")
[![manage software in Debian using dpkg, apt, aptitude, Synaptic, and tasksel](https://www.tecmint.com/wp-content/uploads/2014/08/debian-dpkg-apt-aptitude-synaptic-tasksel.webp)](https://www.tecmint.com/debian-dpkg-apt-aptitude-synaptic-tasksel/ "How to Use dpkg, apt, aptitude, synaptic, and tasksel in Debian")
[![ufw setup ubuntu](https://www.tecmint.com/wp-content/uploads/2013/12/ufw-setup-ubuntu.webp)](https://www.tecmint.com/install-ufw-on-ubuntu-debian/ "UFW Firewall: How to Install, Configure, and Use It on Ubuntu/Debian")
[![Install ProtonVPN on Debian](https://www.tecmint.com/wp-content/uploads/2025/02/Install-ProtonVPN-on-Debian.webp)](https://www.tecmint.com/install-protonvpn-debian/ "How to Set Up ProtonVPN on Debian 12")
[![Installing Nvidia Drivers on Debian](https://www.tecmint.com/wp-content/uploads/2025/02/Installing-Nvidia-Drivers-on-Debian.webp)](https://www.tecmint.com/install-nvidia-drivers-debian/ "Installing Nvidia Graphics Drivers on Debian 12")
[![Auto Mount USB Drive in Linux](https://www.tecmint.com/wp-content/uploads/2025/01/auto-mount-usb-drive-linux.png)](https://www.tecmint.com/mount-usb-drive-on-linux-startup/ "How to Mount a USB Drive Every Time Linux Boots Up")
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/ssh-passwordless-login-in-debian-10/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/ssh-passwordless-login-in-debian-10/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=4304786844614014&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
