[Skip to content](https://www.tecmint.com/create-sftp-user-linux/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/create-sftp-user-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/create-sftp-user-linux/)
To create an **SFTP** user in Linux, you can follow a systematic approach that ensures the user has restricted access while being able to [transfer files securely](https://www.tecmint.com/scp-commands-examples/ "scp to Transfer Files Securely").
This guide will provide detailed steps to set up an **SFTP** -only user on a Linux system, focusing on **Ubuntu** as a primary example, but the principles apply broadly to [other Linux distributions](https://www.tecmint.com/top-most-popular-linux-distributions/ "Popular Linux Distributions") as well.
## Overview of SFTP
**SFTP** (**SSH File Transfer Protocol**) is a secure version of the **File Transfer Protocol** (**FTP**) that uses **SSH** (**Secure Shell**) to encrypt the data transferred over the network, which is commonly used for securely transferring files between a client and a server.
## Creating a New SFTP User
First, you need to create a new **sftp** user account, which will be used to log in and transfer files using **SFTP**.
```
sudo adduser sftpuser

```
![Create sFTP User in Ubuntu](https://www.tecmint.com/wp-content/uploads/2024/07/Create-sFTP-User-in-Ubuntu.png)Create sFTP User in Ubuntu
## Creating a Directory for SFTP
Next, you need to create a directory where the **SFTP** user can upload and download files, this directory will be their home directory for **SFTP** purposes.
```
sudo mkdir -p /home/sftpuser/uploads

```

To ensure security, set the correct permissions for the directories. The user should only have access to their own directory and not be able to navigate to other parts of the system.
```
sudo chown root:root /home/sftpuser
sudo chmod 755 /home/sftpuser

```

Then, change the ownership of the uploads directory:
```
sudo chown sftpuser:sftpuser /home/sftpuser/uploads

```
![Create sFTP User Directory](https://www.tecmint.com/wp-content/uploads/2024/07/Create-sFTP-User-Directory.png)Create sFTP User Directory
## Configure SSH for SFTP
You need to edit the SSH server configuration file to configure SSH to allow SFTP for the new user.
```
sudo nano /etc/ssh/sshd_config

```

Add the following lines at the end of the file to configure SFTP access:
```
Match User sftpuser
    ChrootDirectory /home/sftpuser
    ForceCommand internal-sftp
    AllowTcpForwarding no
    X11Forwarding no

```
![Configure SSH for SFTP](https://www.tecmint.com/wp-content/uploads/2024/07/Configure-SSH-for-SFTP.png)Configure SSH for SFTP
Here’s what each line does:
  * **Match User sftpuser** applies these settings only to the sftpuser.
  * **ChrootDirectory /home/sftpuser** restricts the user’s access to **/home/sftpuser**.
  * **ForceCommand internal-sftp** forces the user to use **SFTP** only, disallowing **SSH** shell access.
  * **AllowTcpForwarding no** and **X11Forwarding no** are additional security measures to prevent the user from using other **SSH** features.


After saving your changes, restart the SSH service to apply the changes.
```
sudo systemctl restart ssh

```

## Testing the SFTP User
You can now test the connection to the **SFTP** server using an SFTP client or command line to connect to your server.
```
sftp sftpuser@your_server_ip

```

Once connected, you can use [SFTP commands](https://www.tecmint.com/sftp-command-examples/ "sFTP Command Examples") to navigate and manage files in the uploads directory.
For example, use the [ls command](https://www.tecmint.com/ls-command-in-linux/ "ls - List Files in Linux") to list files and put to upload files.
```
sftp> ls
sftp> cd uploads
sftp> get remotefile.txt
sftp> put lists.txt

```
![sFTP File Upload](https://www.tecmint.com/wp-content/uploads/2024/07/sFTP-File-Upload.png)sFTP File Upload
##### Conclusion
Creating an SFTP user in Linux is a straightforward process that enhances security and file management capabilities. By following these steps, you can set up a dedicated user for SFTP access, ensuring that your file transfers are secure and restricted to the appropriate directories.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[10 Lesser Known Linux Commands – Part 2](https://www.tecmint.com/10-lesser-known-linux-commands-part-2/)
Next article:
[How to Install TrueNAS (Network-Attached Storage) – Part 1](https://www.tecmint.com/installation-of-truenas/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/create-sftp-user-linux/#respond)** or
## Related Posts
[![Install Proftp in Ubuntu and Debian](https://www.tecmint.com/wp-content/uploads/2014/09/Install-Proftp-in-Ubuntu-and-Debian.png)](https://www.tecmint.com/install-proftpd-in-ubuntu-and-debian/ "How to Create a Secure FTP Server with ProFTPD on Ubuntu/Debian")
[![Linux Commandline FTP Clients](https://www.tecmint.com/wp-content/uploads/2019/05/Commandline-FTP-Clients-for-Linux.png)](https://www.tecmint.com/command-line-ftp-clients-for-linux/ "6 Best Command-Line FTP Clients for Linux Users")
[![Install Anonymous FTP in Fedora](https://www.tecmint.com/wp-content/uploads/2020/01/Install-Anonymous-FTP-in-Fedora.png)](https://www.tecmint.com/setup-anonymous-ftp-download-server-in-fedora/ "How to Setup an Anonymous FTP Download Server in Fedora")
[![Install Secure FTP Using SSL on RHEL 8](https://www.tecmint.com/wp-content/uploads/2019/06/Install-Secure-FTP-Using-SSL-on-RHEL-8.png)](https://www.tecmint.com/setup-secure-ftp-file-transfer-using-ssl-tls-in-rhel-8/ "Setup Secure FTP File Transfer Using SSL/TLS in RHEL 8")
[![Change FTP Port in Linux](https://www.tecmint.com/wp-content/uploads/2018/01/Change-FTP-Port-in-Linux.png)](https://www.tecmint.com/change-ftp-port-in-linux/ "How to Change FTP Port in Linux")
[![How to Upload or Download Directory using sFTP](https://www.tecmint.com/wp-content/uploads/2017/02/sFTP-Directory-Upload-Download-in-Linux.png)](https://www.tecmint.com/sftp-upload-download-directory-in-linux/ "How to Upload or Download Files/Directories Using sFTP in Linux")
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/create-sftp-user-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/create-sftp-user-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=412596274698107&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
