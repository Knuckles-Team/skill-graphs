[Skip to content](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/)
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
  * [Pro Courses](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/ "Linux Online Courses")
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


[](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/)
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
  * [Pro Courses](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/ "Linux Online Courses")
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


[](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/)
# DSH (Distributed Shell) – Run Commands on Multiple Linux Servers
[Rob Krul](https://www.tecmint.com/author/kaoxkrul/ "View all posts by Rob Krul")Last Updated: January 19, 2024 Read Time: 3 minsCategories [Linux Commands](https://www.tecmint.com/category/linux-commands/) [30 Comments](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comments)
**Systems Administrators** are well aware of the importance of being able to [monitor and administer numerous machines](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/ "Monitor Linux Performance") in a short amount of time, preferably with minimal physical movement. Whether it’s a small cloud environment or a large server cluster, the ability to centrally manage computers is essential.
To partly accomplish this, I am going to show you how to use a nifty little tool called **DSH** (dancer’s shell/distributed shell) that allows a user to run commands across multiple machines.
**You might also like:**
  * [Pssh – Execute Commands on Multiple Remote Linux Servers](https://www.tecmint.com/execute-commands-on-multiple-linux-servers-using-pssh/ "Pssh – Execute Commands on Multiple Linux Servers")
  * [How to Run a Command Multiple Times in Linux](https://www.tecmint.com/run-linux-command-multiple-times/ "Run a Command Multiple Times in Linux")
  * [4 Useful Tools to Run Commands on Multiple Linux Servers](https://www.tecmint.com/run-commands-on-multiple-linux-servers/ "Run Commands on Multiple Linux Servers")


## What is DSH?
**DSH** is short for ‘**Distributed Shell** ‘ or ‘**Dancer’s Shell** ‘, which is a freely available tool on [most major distributions](https://www.tecmint.com/top-most-popular-linux-distributions/ "Popular Linux Distributions") of Linux but can be easily built from a source if your distribution does not include it in its package repository.
## Install DSH (Distributed Shell) in Linux
We are going to assume a **Debian** / **Ubuntu** environment for the scope of this tutorial. If you are using another distribution, please substitute the appropriate commands for your package manager.
On [Debian-based distributions](https://www.tecmint.com/debian-based-linux-distributions/ "Debian-based Linux Distributions"), you can install **DSH** using the following [apt command](https://www.tecmint.com/apt-command-in-linux/ "Debian apt Command") in the terminal.
```
sudo apt install dsh

```

On [RHEL-based distributions](https://www.tecmint.com/redhat-based-linux-distributions/ "RedHat-based Linux Distributions"), you need to compile it from source tar balls, but before doing so, make sure to compile and install the ‘**libdshconfig** ‘ library.
```
wget http://www.netfort.gr.jp/~dancer/software/downloads/libdshconfig-0.20.10.cvs.1.tar.gz
tar xfz libdshconfig*.tar.gz
cd libdshconfig-*
./configure ; make
sudo make install

```

Then compile **dsh** and install.
```
wget https://www.netfort.gr.jp/~dancer/software/downloads/dsh-0.22.0.tar.gz
tar xfz dsh-0.22.0.tar.gz
cd dsh-*
./configure ; make
sudo make install

```

## How to Use DSH in Linux
The main configuration file “**/etc/dsh/dsh.conf”** (For **Debian**) and “**/usr/local/etc/dsh.conf** ” (for **Red Hat)** is pretty straightforward, but since **rsh** is an unencrypted protocol, we are going to use [SSH](https://www.tecmint.com/install-openssh-server-in-linux/ "Install SSH In Linux") as the remote shell.
Using the [text editor](https://www.tecmint.com/linux-command-line-editors/ "Command Line Editors for Linux") of your choice, find this line:
```
remoteshell =rsh

```

and change it to:
```
remoteshell =ssh

```

There are other options you can pass in here if you choose, and there are plenty of them to find on the dsh man page. For now, we are going to accept the defaults and have a look at the next file, **/etc/dsh/machines.list** (for **Debian**).
For **Red Hat-based** systems you need to create a file called “**machines.list** ” in the “**/usr/local/etc/** ” directory.
The syntax here is pretty easy. All you have to do is enter in a machine’s credentials (**Hostname** , **IP Address** , or **FQDN**) one per line.
**Note** : When accessing more than one machine simultaneously, it would behoove you to set up [key-based password-less SSH](https://www.tecmint.com/ssh-passwordless-login-using-ssh-keygen-in-5-easy-steps/) on all of your machines. Not only does this provide ease of access, but security-wise, it hardens your machine as well.
My “**/etc/dsh/machines.list** ” or “**/usr/local/etc/machines.list** ” file says:
```
172.16.25.125
172.16.25.126

```

Once you have entered the credentials of the machines you wish to access, let’s run a simple command like [uptime](https://www.tecmint.com/linux-uptime-command-examples/ "Linux Uptime Command") to all of the machines.
```
dsh -aM -c uptime

```

**Sample Output** :
```
**172.16.25.125**: 05:11:58 up 40 days, 51 min, 0 users, load average: 0.00, 0.01, 0.05
**172.16.25.126**: 05:11:47 up 13 days, 38 min, 0 users, load average: 0.00, 0.01, 0.05
```

## So, What Does the ‘dsh’ Command Do?
Pretty simple. First, we ran **dsh** and passed the “`-a`” option to it, which says to send the “**uptime** ” command to “**ALL** ” of the machines listed in “**/etc/dsh/machines.list** “.
Next, we specified the “`-M`” option, which says to return the “**machine name** ” (specified in “**/etc/dsh/machines.list** “) along with the output of the **uptime** command. (Very useful for sorting when running a command on a number of machines).
The “`-c`” option stands for “**command to be executed** ” in this case, “**uptime** “.
**DSH** can also be configured with groups of machines in the “**/etc/dsh/groups/** ” file, where is a file with a list of machines in the same format as the “**/etc/dsh/machines.list** ” file. When running **dsh** on a group, specify the **groupname** after the “`-g`” option.
For **Red Hat-based** systems you need to create a folder called “**groups** ” in the “**/usr/local/etc/** ” directory. In that “**groups** ” directory you create a file called “**cluster** “.
For example, run the “`w`” command on all machines listed in the “**cluster** ” group file “**/etc/dsh/groups/cluster** ” or “**/usr/local/etc/groups/cluster** “.
```
dsh -M -g cluster -c w

```

**DSH** provides much more flexibility, and this tutorial only scratches the surface. Aside from executing commands, **DSH** can be used to transfer files, install software, add routes, and much more.
To a **Systems Administrator** tasked with the responsibility of a large network, it is invaluable.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install and Compile Kernel in Debian](https://www.tecmint.com/kernel-compilation-in-debian-linux/)
Next article:
[How to Create Clones and Templates of Virtual Machines in Proxmox](https://www.tecmint.com/proxmox-clones-templates/)
![Photo of author](https://secure.gravatar.com/avatar/342e75ba54affd90050d5b946d0214854cd516ded35ae3f88b2d05d649b270f2?s=100&d=blank&r=g)
Rob Krul
Rob is an avid user of Linux and Open Source Software, with over 15 years experience in the tech geek universe. Aside from experimenting with the many flavors of Linux, he enjoys working with BSDs, Solaris, and OS X. He currently works as an Independent IT Contractor.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[How to Use Rsync Command: 16 Examples for Linux File Sync](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/)
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[15 Useful “ifconfig” Commands to Configure Network Interface in Linux](https://www.tecmint.com/ifconfig-command-examples/)
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[How to Find Most Used Disk Space Directories and Files in Linux](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/)
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[4 Ways to Find Out Which Process Listening on a Particular Port](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/)
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[How to Find Command Location and Description in Linux](https://www.tecmint.com/find-linux-command-description-and-location/)
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
[How to Use the Linux column Command to Format Text into Tables](https://www.tecmint.com/linux-column-command/)
### 30 Comments
[Leave a Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/48a543e80a896c2dc691331477536064b88c83927658a85e7c2bb03dd7037015?s=50&d=blank&r=g)
n2o
[ September 20, 2016 at 9:21 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-819564)
The -c command does not mean “command to be executed”. According to the manual, it means “concurrent shell”.
–concurrent-shell | -c
Executes shell concurrently.
See
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-819564)
  2. ![](https://secure.gravatar.com/avatar/aa9e2dcc9e469a059e2e81a61ae94f210edf4f34d3a8a8b39676bd4a0a5d1c17?s=50&d=blank&r=g)
nakul
[ May 4, 2016 at 3:47 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-776108)
If you have 1000 servers, It will ask 1000 times to put yes/no to known hosts and for first time to add ssh-key again it will ask 1000 times for password, then what is the use of this???
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-776108)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 4, 2016 at 11:06 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-776263)
@Nakul,
Then you should go for [Pscp tool](https://www.tecmint.com/copy-files-to-multiple-linux-servers/) to achieve the same
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-776263)
     * ![](https://secure.gravatar.com/avatar/1bd4f1567be18450969450d3af2ffae6645a7022df0e341b04b2a5fb0c404f1b?s=50&d=blank&r=g)
Andrew DeFaria
[ July 14, 2016 at 5:42 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-799074)
Well if you set config for ssh to auto accept new known_hosts and establish pre-shared ssh keys then there’s no prompting at all!
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-799074)
     * ![](https://secure.gravatar.com/avatar/3e3c4b47dff8d948aa8e780fb7b0e11fa7c80a24e97269416e407a54961f1a49?s=50&d=blank&r=g)
kai keliikuli
[ December 23, 2016 at 2:23 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-851956)
echo “StrictHostKeyChecking no” >> ~/.ssh/config
and then connect to your thousand servers.
They’ll end up in known hosts
and then remove that line from ~/.ssh/config
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-851956)
     * ![](https://secure.gravatar.com/avatar/2e3461d73ed0fd8598c5a3a7fb45fc4fcc2f63df933f781cd24719a0ca3671e0?s=50&d=blank&r=g)
matish
[ August 9, 2019 at 4:08 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-1221209)
you can use “**StrictHostKeyChecking=no** ” in your **/etc/ssh/sshd.config** and restart the sshd and run the dsh command.
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-1221209)
  3. ![](https://secure.gravatar.com/avatar/289c99f2bada3cab551b410b4113b1af38169d3d1127f7a41256a8c8fbcf5096?s=50&d=blank&r=g)
Aurelien
[ May 2, 2016 at 2:49 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-775638)
dsh is the ancestor, pdsh improved it and is much better, and clustershell is now a better pdsh. Available in EPEL (CentOS , Fedora) and Debian and ubuntu
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-775638)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 2, 2016 at 11:48 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-775693)
@Aurelien,
Thanks for informing us about clustershell, we will definitely test run right away and write a detailed article on this, till then stay tuned..
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-775693)
  4. ![](https://secure.gravatar.com/avatar/ea5f34ca326c00e992815e5c34104204b0b3bead372195de9eadbcb05880f786?s=50&d=blank&r=g)
Marin Todorov
[ April 28, 2016 at 10:10 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-774809)
For those of you who are asking about ports, I can suggest setting up config file in ~/.ssh/config. The file should contain something like:
Host server1.net
HostName 192.168.0.100
user root
Port 22
IdentityFile ~/.ssh/your_id
Host server2.net
HostName 192.168.0.101
User root
Port 12345
IdentityFile ~/.ssh/your_id
Host server3.net
HostName 192.168.0.102
User root
Port 54321
IdentityFile ~/.ssh/your_id
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-774809)
  5. ![](https://secure.gravatar.com/avatar/d3ba2a5a4a23a440426a9a93548c05f765035a37afeb22b4bca091d4e9a16172?s=50&d=blank&r=g)
burning_daylight
[ April 28, 2016 at 7:51 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-774792)
There is also tool , called cssh — it will work on any distro without “modern” libraries
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-774792)
  6. ![](https://secure.gravatar.com/avatar/0c5cce7039254bec86b05f5be12ad7ef61689ed4dd74a8ef1f5b346f8b73a11f?s=50&d=blank&r=g)
Norm
[ April 28, 2016 at 11:38 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-774708)
An alternative that come standard with Red Hat and Fedora is pdsh, installable with yum/dnf
yum install pdsh
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-774708)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 28, 2016 at 12:31 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-774718)
@Norm,
Thanks for informing us about that pdsh took, let me give a try and see how it is useful than dsh, will test it and write a detailed article on this, till then stay tuned..
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-774718)
  7. ![](https://secure.gravatar.com/avatar/a2e99f72064c0773dcd539fb4982fc90c089dc0cfc75a981a1d02522fcbc15a6?s=50&d=blank&r=g)
Dave
[ September 10, 2015 at 3:01 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-662363)
-c does not mean “command”:
–concurrent-shell | -c
Executes shell concurrently.
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-662363)
  8. ![](https://secure.gravatar.com/avatar/f74461b556f987425f88e8fbcdb0a7f839aa17b3952531c4325e4a0a6d89a3f1?s=50&d=blank&r=g)
Dustin
[ July 17, 2015 at 9:40 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-625900)
err: username@host:port (not IP at the end… No undo)
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-625900)
  9. ![](https://secure.gravatar.com/avatar/f74461b556f987425f88e8fbcdb0a7f839aa17b3952531c4325e4a0a6d89a3f1?s=50&d=blank&r=g)
Dustin
[ July 17, 2015 at 9:39 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-625899)
Try putting username@host:ip in the group or list file and see if it will find the proper port for your instance.
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-625899)
  10. ![](https://secure.gravatar.com/avatar/f036253f129d0bc42768f859fd9782011cbcc5df15b74bbf884b5bb170af60d1?s=50&d=blank&r=g)
Shaheel
[ May 9, 2015 at 6:50 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-565066)
Hi,
I have 3 machines in machinelist. but i can’t enter ssh key phrase for first and second, first and second asking key
dsh -aM -c uptime
root@x.x.x.x’s password: root@y.y.y.y’s password: root@z.z.z.z’s password:
only can enter 3rd server password
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-565066)
  11. ![](https://secure.gravatar.com/avatar/f036253f129d0bc42768f859fd9782011cbcc5df15b74bbf884b5bb170af60d1?s=50&d=blank&r=g)
Shaheel
[ May 9, 2015 at 6:05 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-565049)
How can use this with other SSH ports than 22. this only works with ssh port 22. How can use this with other ports
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-565049)
  12. ![](https://secure.gravatar.com/avatar/46b6c6d00104d971b5e22b04c0564b1f660740b074ffc16e07b971c026d0ba43?s=50&d=blank&r=g)
yashar esmaildokht
[ December 7, 2014 at 4:11 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-397786)
thanks , very usefully ,
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-397786)
  13. ![](https://secure.gravatar.com/avatar/2def72cb36ea86d67a19251bb2062a3a2b74951bccd63c9568795e2e73eeb535?s=50&d=blank&r=g)
domain
[ September 8, 2014 at 7:58 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-265831)
Hi! Do you know if they make any plugins to protect against hackers?
I’m kinda paranoid about losing everything I’ve worked hard on. Any recommendations?
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-265831)
  14. ![](https://secure.gravatar.com/avatar/ac0117b98559611ec25b2df01a4d3065c0c599c115f17f75f2edaee81ab8ffe5?s=50&d=blank&r=g)
liu
[ August 5, 2014 at 9:06 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-232636)
thanks very much
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-232636)
  15. ![](https://secure.gravatar.com/avatar/5c9f3f21e5753061724439775cee7aee3293cd155e9f8e5999b00dc4bafd6ec5?s=50&d=blank&r=g)
er0k
[ April 1, 2014 at 5:54 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-144192)
the -c flag does not mean the “command to be executed” , it means to run the command concurrently on all servers.
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-144192)
  16. ![](https://secure.gravatar.com/avatar/33c1471f48acbc60ba6818c1d3842ba861a8f7ac7f81128d6e7e2793f3318880?s=50&d=blank&r=g)
MACscr
[ February 19, 2014 at 10:41 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-124068)
Do how about dcp for file transfer? I dont see the option on my debian 7 system.
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-124068)
  17. ![](https://secure.gravatar.com/avatar/51e16a45c598c677a860b90e3cf8ee2ab1ebb7ef4142d6b68774ecb680949e18?s=50&d=blank&r=g)
niraj
[ October 28, 2013 at 4:48 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-62505)
How to add port other than 22 port.
I have added the machine but still its give the following error
dsh: no machine specified
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-62505)
     * ![](https://secure.gravatar.com/avatar/342e75ba54affd90050d5b946d0214854cd516ded35ae3f88b2d05d649b270f2?s=50&d=blank&r=g)
Rob Krul
[ October 31, 2013 at 8:14 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-63570)
@niraj
The easiest way to set up ssh connections to other hosts is to use a ~/.ssh/config file. The syntax is pretty simple:
Host (host)
HostName (host name)
IdentityFile ~/.ssh/your_id_file_rsa
Port (port number)
User (the username you use with SSH to login)
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-63570)
  18. ![](https://secure.gravatar.com/avatar/c4f1a832d0f6791656b82c70fe5ed6c930dbf42f89de98842750ec17b025f048?s=50&d=blank&r=g)
zcat
[ October 25, 2013 at 12:43 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-61425)
Pretty similar to the script I’m using here.
for host in {list of hosts}; do ssh $host “$@” &; done
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-61425)
  19. ![](https://secure.gravatar.com/avatar/342e75ba54affd90050d5b946d0214854cd516ded35ae3f88b2d05d649b270f2?s=50&d=blank&r=g)
Rob Krul
[ October 24, 2013 at 7:59 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-60780)
@Omipenguin:
What command are you trying to run over DSH?
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-60780)
  20. ![](https://secure.gravatar.com/avatar/1bc107ce0a453ff9a59ab41357dbdbd8611df195b10141fd5d92484f34b13c01?s=50&d=blank&r=g)
JGV
[ October 23, 2013 at 6:56 am  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-60185)
On CentOS/RHEL it’s just as easy as in Debian, no need to compile anything. Just:
yum –enablerepo=epel install pdsh
On Fedora, you don’t even need EPEL, it’s included in the standard repository:
yum install pdsh
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-60185)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 23, 2013 at 5:39 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-60397)
Dear Jorge,
Thanks for the findings, we really not aware of such pdsh tool. Will update the article.
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-60397)
  21. ![](https://secure.gravatar.com/avatar/505b4926ba5b27c30223414715c688b0d7e522342e4f22466316b86a462702bf?s=50&d=blank&r=g)
Omipenguin
[ October 22, 2013 at 11:00 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-60039)
Good article, But im getting this error
Pseudo-terminal will not be allocated because stdin is not a terminal.
System info
=========
Distributor ID: elementary OS
Description: elementary OS Luna
Release: 0.2
Codename: luna
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-60039)
  22. ![](https://secure.gravatar.com/avatar/0e6d740eca58e44dc783e7dbaa740b826b7c24ebcee6be15b838910f17366578?s=50&d=blank&r=g)
Sarfaraz Shaikh
[ October 22, 2013 at 8:32 pm  ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-59974)
You can also use clusterssh for running single command to multiple machine at a same time.
[Reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#comment-59974)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/#respond)
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
[Fd – The Best Alternative to ‘Find’ Command for Quick File Searching](https://www.tecmint.com/fd-alternative-to-find-command/)
[Transfer.sh – Easy File Sharing from Linux Commandline](https://www.tecmint.com/file-sharing-from-linux-commandline/)
[Autojump – Quickly Navigate Directories and Linux File System](https://www.tecmint.com/autojump-navigate-linux-directories-faster/)
[How to Create Users in Linux [15 useradd Command Examples]](https://www.tecmint.com/add-users-in-linux/)
[Ways to Use ‘find’ Command to Search Directories More Efficiently](https://www.tecmint.com/find-directory-in-linux/)
[How to Convert a /Home Directory to Partition in Linux](https://www.tecmint.com/convert-home-directory-partition-linux/)
## Linux Server Monitoring Tools
[Linux Performance Monitoring with Vmstat and Iostat Commands](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/)
[Pyinotify – Monitor Filesystem Changes in Real-Time in Linux](https://www.tecmint.com/pyinotify-monitor-filesystem-directory-changes-in-linux/)
[How to Setup Rsyslog Client to Send Logs to Rsyslog Server in CentOS 7](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/)
[How to Setup and Manage Log Rotation Using Logrotate in Linux](https://www.tecmint.com/install-logrotate-to-manage-log-rotation-in-linux/)
[Amplify – NGINX Monitoring Made Easy](https://www.tecmint.com/amplify-nginx-monitoring-tool/)
[How to Install Nagios Monitoring in RHEL, Rocky, and AlmaLinux](https://www.tecmint.com/install-nagios-in-linux/)
## Learn Linux Tricks & Tips
[Mhddfs – Combine Several Smaller Partition into One Large Virtual Storage](https://www.tecmint.com/combine-partitions-into-one-in-linux-using-mhddfs/)
[How to Check Which Apache Modules are Enabled/Loaded in Linux](https://www.tecmint.com/check-apache-modules-enabled/)
[fdupes – A Command Line Tool to Find and Delete Duplicate Files in Linux](https://www.tecmint.com/fdupes-find-and-delete-duplicate-files-in-linux/)
[How to Set and Unset Local, User and System Wide Environment Variables in Linux](https://www.tecmint.com/set-unset-environment-variables-in-linux/)
[How to Find MySQL, PHP and Apache Configuration Files](https://www.tecmint.com/find-mysql-php-apache-configuration-files/)
[How to Find a Specific String or Word in Files and Directories](https://www.tecmint.com/find-a-specific-string-or-word-in-files-and-directories/)
## Best Linux Tools
[10 Best API Gateways and Management Tools in 2024](https://www.tecmint.com/open-source-api-gateways-and-management-tools/)
[10 Most Popular Download Managers for Linux in 2023](https://www.tecmint.com/download-managers-for-linux/)
[15 Best Kali Linux Web Penetration Testing Tools](https://www.tecmint.com/kali-linux-web-penetration-testing-tools/)
[Top 5 Linux Programs for Students in 2025](https://www.tecmint.com/linux-programs-for-students/)
[The 8 Best Free Anti-Virus Programs for Linux](https://www.tecmint.com/best-antivirus-programs-for-linux/)
[Top 3 Open Source Virtual Data Room (VDR) for Linux](https://www.tecmint.com/open-source-virtual-data-room-for-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/using-dsh-distributed-shell-to-run-linux-commands-across-multiple-machines/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
