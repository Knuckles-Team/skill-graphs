[Skip to content](https://www.tecmint.com/xubuntu-installation-guide/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/xubuntu-installation-guide/ "Linux Online Courses")
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


[](https://www.tecmint.com/xubuntu-installation-guide/)
**Xubuntu** is a popular [lightweight Linux distribution](https://www.tecmint.com/lightweight-linux-desktop-environments/ "Lightweight Linux Desktop Environments") that is based on **Ubuntu**. It ships with an Xfce desktop environment which is light, stable, and highly configurable.
Being a lightweight distribution, **Xubuntu** is a perfect choice for users who are running modern PCs with low RAM and CPU resources. It also works quite well on older hardware.
**Xubuntu 20.04** is an **LTS** release that is based on **Ubuntu 20.04** , codenamed **Focal Fossa**. It was released in April 2020 and will be supported up to April 2023.
In this guide, we will walk you through the installation of the **Xubuntu 20.04** Desktop.
#### Prerequisites
Before getting started out, ensure your system meets the following minimum requirements:
  * 1.5 GHz dual-core Intel or AMD processor with at least 1 GB RAM (2 GB is Recommended).
  * 9 GB of free hard disk space (20 GB is recommended).


#### Download Xubuntu 20.04 ISO Image
Additionally, you need an **ISO** image of **Xubuntu 20.04**. You can download it from the Official Xubuntu download page. You also need a **16GB** USB drive which will be used as a bootable installation medium.
### Installation of Xubuntu 20.04 Desktop
The first step is to create a bootable USB drive for installing **Xubuntu** using the downloaded **Xubuntu ISO** image. There are a couple of ways of doing this.
#### Create a Xubuntu USB Bootable Image
You can use the [UNetBootin tool or the dd command](https://www.tecmint.com/install-linux-from-usb-device/ "Create a Bootable USB Drive"). If you have downloaded the ISO from a Windows machine, you can use the
![Create Xubuntu USB Bootable Image](https://www.tecmint.com/wp-content/uploads/2013/04/Create-Xubuntu-USB-Bootable-Image.png)Create Xubuntu USB Bootable Image
#### Begin the Xubuntu Installation
Now plug in the bootable USB drive into your **PC** and reboot it. Just to be sure that your PC boots from the USB drive, head over to the **BIOS** settings, and set the boot order with your USB drive at the very top of the boot priority. Then save the changes and exit.
On startup, you will see a **Xubuntu** log splash on the screen. The installer will perform some filesystem integrity checks. This can take a while, so just be patient.
![Xubuntu Booting](https://www.tecmint.com/wp-content/uploads/2013/04/Xubuntu-Booting.png)Xubuntu Booting
Shortly after, the Graphical installer will pop up and present you with two options. To try out Xubuntu without installing, click on ‘**Try Xubuntu** ’. Since our goal is to install Xubuntu, click on the ‘**Install Xubuntu** ’ option.
![Install Xubuntu Desktop](https://www.tecmint.com/wp-content/uploads/2013/04/Install-Xubuntu-Desktop.png)Install Xubuntu Desktop
#### Select Keyboard Layout
Next, choose your preferred keyboard layout and click ‘**Continue** ’.
![Xubuntu Keyboard Layout](https://www.tecmint.com/wp-content/uploads/2013/04/Xubuntu-Keyboard-Layout.png)Xubuntu Keyboard Layout
#### Install Xubuntu Updates
In the next step, you are provided with the option of downloading updates and other third-party software packages for graphics, WiFi, and other media formats. In my case, I selected both options and pressed ‘**Continue** ’.
![Install Xubuntu Updates](https://www.tecmint.com/wp-content/uploads/2013/04/Install-Xubuntu-Updates.png)Install Xubuntu Updates
#### Create Xubuntu Disk Partitions
The installer provides two options for Installing Xubuntu. The first option – **Erase disk and install Xubuntu** – wipes out your entire disk along with any files and programs. It also automatically partitions your disk and is recommended for those who are unfamiliar with the manual partitioning of a hard drive.
The second option allows you to manually partition your hard drive. You can explicitly specify which partitions you want to create on your hard disk.
For this guide, we will click on ‘**Something Else** ’ so that we can manually define the partitions to be created.
![Xubuntu Installation Type](https://www.tecmint.com/wp-content/uploads/2013/04/Xubuntu-Installation-Type.png)Xubuntu Installation Type
In the next step, your drive will be highlighted as `/dev/sda` (for **SATA** hard drives) or `/dev/had` (for the old IDE hard drives). You need to create a partition table for the drive before proceeding further.
We have a **27.5 GB** hard drive and we will partition it as follows:
```
/boot		- 	1024 MB
swap		-	4096 MB
/ ( root )	-	The  remaining disk space ( 22320 MB )

```

To proceed, click on the ‘**New Partition Table** ’ button.
![Create New Partition Table](https://www.tecmint.com/wp-content/uploads/2013/04/Create-New-Partition-Table.png)Create New Partition Table
On the pop-up dialogue click on ‘**Continue** ’.
![Confirm New Partition Table](https://www.tecmint.com/wp-content/uploads/2013/04/Confirm-New-Partition-Table.png)Confirm New Partition Table
A free space will be created equivalent to the size of your hard drive. To begin partitioning, click on the plus sign `(+)` button directly below.
![Create New Partition](https://www.tecmint.com/wp-content/uploads/2013/04/Create-New-Partition.png)Create New Partition
We will start off with the **boot** partition. Specify the size in MB and mount point as `/boot`. Then click ‘**OK** ’.
![Create Boot Partition](https://www.tecmint.com/wp-content/uploads/2013/04/Create-Boot-Partition.png)Create Boot Partition
This takes you back to the partition table and as you can see, our boot partition has been created.
![Confirm Boot Partition](https://www.tecmint.com/wp-content/uploads/2013/04/Confirm-Boot-Partition.png)Confirm Boot Partition
Next up, we will create the **swap** area. So, once again, click on the remaining free space entry and click on the plus sign `(+)` and fill in the swap details as indicated. Take note that you should click on the **“Use as** ” label and select **swap** area then click ‘**OK** ’.
![Create Swap Partition](https://www.tecmint.com/wp-content/uploads/2013/04/Create-Swap-Partition.png)Create Swap Partition
The remaining space will be reserved for the root partition `(/)`. Repeat the drill and create the root partition.
![Create Root Partition](https://www.tecmint.com/wp-content/uploads/2013/04/Create-Root-Partition.png)Create Root Partition
Here is our partition table with all the partitions. To proceed with the installation of Xubuntu, click ‘**Install Now** ’.
![Summary of Partition Table](https://www.tecmint.com/wp-content/uploads/2013/04/Xubuntu-Partition-Table.png)Summary of Partition Table
Click ‘**Continue** ’ on the pop-up dialogue to write changes to the disk and proceed with the installation.
![Confirm Partition Changes](https://www.tecmint.com/wp-content/uploads/2013/04/Confirm-Partition-Changes.png)Confirm Partition Changes
In the next step, specify your geographical location. If you are connected to the internet, the installer will automatically detect your region.
![Choose Geographical Region](https://www.tecmint.com/wp-content/uploads/2013/04/Choose-Geographical-Region.png)Choose Geographical Region
#### Create a Regular User
Next, create a login user by filling in your user details such as your PC’s name, username, and password and click on ‘**Continue** ’.
![Create User Account](https://www.tecmint.com/wp-content/uploads/2013/04/Create-User-Account.png)Create User Account
#### Installing Xubuntu System
The installer will begin by copying all the files required by Xubuntu. It will then install and configure all the software packages from the installation media.
This can take a while. It took around 30 min in my case.
![Installing Xubuntu System](https://www.tecmint.com/wp-content/uploads/2013/04/Installing-Xubuntu-System.png)Installing Xubuntu System
Once the installation is complete, click on the ‘**Restart Now** ’ button to restart the system.
![Xubuntu Installation Completes](https://www.tecmint.com/wp-content/uploads/2013/04/Xubuntu-Installation-Completes.png)Xubuntu Installation Completes
Remove the bootable USB drive and press **ENTER**.
![Remove Xubuntu Media](https://www.tecmint.com/wp-content/uploads/2013/04/Remove-Xubuntu-Media.png)Remove Xubuntu Media
Once the system reboots, a login GUI will be displayed whereupon you will be required to provide your password to access the desktop.
![Xubuntu User Login](https://www.tecmint.com/wp-content/uploads/2013/04/Xubuntu-User-Login.png)Xubuntu User Login
Once logged in, you will be ushered to the **Xfce** desktop environment. From here you can explore your new system and try out a couple of tweaks to enhance the look and feel and performance.
![Xubuntu Desktop](https://www.tecmint.com/wp-content/uploads/2013/04/Xubuntu-Desktop.png)Xubuntu Desktop
This sums up this instructional guide. We have successfully walked you through the installation of **Xubuntu 20.04**.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Manage Zentyal PDC (Primary Domain Controller) from Windows System – Part 2](https://www.tecmint.com/manage-zentyal-pdc-from-windows/)
Next article:
[How to Create Organizational Units (OU) and Enable GPO (Group Policy) in Zentyal – Part 3](https://www.tecmint.com/creating-organizational-units-and-enableing-group-policy-in-zentyal/)
![Photo of author](https://secure.gravatar.com/avatar/3b060d6a6c8d6305817bda1435529b27f2d4f900a7998bd703a17094636601a9?s=100&d=blank&r=g)
James Kiarie
This is James, a certified Linux administrator and a tech enthusiast who loves keeping in touch with emerging trends in the tech world. When I'm not running commands on the terminal, I'm taking listening to some cool music. taking a casual stroll or watching a nice movie.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/xubuntu-installation-guide/#respond)** or
## Related Posts
Sorry, no posts were found.
### 5 Comments
[Leave a Reply](https://www.tecmint.com/xubuntu-installation-guide/#reply-title)
  1. I created a USB boot drive with the ISO. When I boot my laptop with the USB drive I do not get the same splash and Welcome screens that you show here. I get a DOS-looking screen with 4 or so options.
The top two options are Try xUbuntu and Install xUbuntu. I’ve tried both options and they both give me a black screen with a blinking cursor in the upper left corner. I left them like that for a day and nothing happened. I tried to install it from DVD too and get the same results.
[Reply](https://www.tecmint.com/xubuntu-installation-guide/#comment-1965122)
  2. I don’t install pinguy builder to create an iso file when installing some applications on Xubuntu 20.04. Please help me. Thanks!
[Reply](https://www.tecmint.com/xubuntu-installation-guide/#comment-1733561)
  3. Since **Xubuntu 18.04** there is no need for a swap partition anymore if your main partition is ext4. Swap just uses a swap file on your main partition.
Greetings
[Reply](https://www.tecmint.com/xubuntu-installation-guide/#comment-1713996)
  4. Thank you for this article with its visual walk-through. It’s useful to see what’s involved BEFORE I take the plunge with the product.
[Reply](https://www.tecmint.com/xubuntu-installation-guide/#comment-1672471)
     * Thank you for your feedback BobbieCB. We wish you an eventful time as you get started out.
[Reply](https://www.tecmint.com/xubuntu-installation-guide/#comment-1672718)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/xubuntu-installation-guide/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/xubuntu-installation-guide/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=835204628800108&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
