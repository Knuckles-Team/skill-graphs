[Skip to content](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/)
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
  * [Pro Courses](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/)
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
  * [Pro Courses](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/)
# How to Use ‘fsck’ to Repair Linux File System Errors
[Marin Todorov](https://www.tecmint.com/author/marintodorov89/ "View all posts by Marin Todorov")Last Updated: July 14, 2023 Read Time: 4 minsCategories [Linux Commands](https://www.tecmint.com/category/linux-commands/), [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [39 Comments](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comments)
[Linux Filesystems](https://www.tecmint.com/linux-directory-structure-and-important-files-paths-explained/ "Linux Filesystem Structure") are responsible for organizing how data is stored and recovered. One way or another, with time, the filesystem may become corrupted and certain parts of it may not be accessible. If your filesystem develops such inconsistency it is recommended to verify its integrity.
This can be completed via a system utility called **fsck** (**file system consistency check**), which checks the root file system automatically during boot time or ran manually.
In this article, we are going to review the **fsck command** and its usage to help you repair Linux disk errors.

Table of Contents
Toggle
  * [When to Use fsck Command in Linux](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#When_to_Use_fsck_Command_in_Linux)
    * [fsck Command Options](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#fsck_Command_Options)
  * [Run fsck Command to Repair Linux File System Errors](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#Run_fsck_Command_to_Repair_Linux_File_System_Errors)
    * [Understanding fsck Exit Codes](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#Understanding_fsck_Exit_Codes)
    * [Fsck Repair Linux Filesystem](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#Fsck_Repair_Linux_Filesystem)
  * [How to Run fsck on Linux Root Partition](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#How_to_Run_fsck_on_Linux_Root_Partition)
    * [Force fsck Upon System Boot](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#Force_fsck_Upon_System_Boot)
    * [Run fsck in Rescue Mode](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#Run_fsck_in_Rescue_Mode)
      * [Conclusion](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#Conclusion)


There are different scenarios when you will want to run **fsck**. Here are a few examples:
  * The system fails to boot.
  * Files on the system become corrupt (often you may see input/output error).
  * The attached drive (including flash drives/SD cards) is not working as expected.


The **fsck command** needs to be run with superuser privileges or **root**. You can use it with different arguments. Their usage depends on your specific case. Below you will see some of the more important options:
  * `-A` – Used for checking all filesystems. The list is taken from `/etc/fstab`.
  * `-C` – Show progress bar.
  * `-l` – Locks the device to guarantee no other program will try to use the partition during the check.
  * `-M` – Do not check mounted filesystems.
  * `-N` – Only show what would be done – no actual changes are made.
  * `-P` – If you want to check filesystems in parallel, including root.
  * `-R` – Do not check the root filesystem. This is useful only with ‘`-A`‘.
  * `-r` – Provide statistics for each device that is being checked.
  * `-T` – Does not show the title.
  * `-t` – Exclusively specify the [Linux filesystem types](https://www.tecmint.com/find-file-types-in-linux/ "Find Out File Types in Linux") to be checked. Types can be comma-separated lists.
  * `-V` – Provide a description of what is being done.


In order to run **fsck** , you will need to ensure that the partition you are going to check is not mounted. For the purpose of this article, I will use my second drive `/dev/sdb` mounted in `/mnt`.
Here is what happens if I try to run **fsck** when the partition is mounted.
```
# fsck /dev/sdb

```
![Run fsck on Mounted Partition](https://www.tecmint.com/wp-content/uploads/2018/09/Run-fsck-on-Mounted-Partition.png)Run fsck on Mounted Partition
To avoid this unmount the partition using.
```
# umount /dev/sdb

```

Then **fsck** can be safely run with.
```
# fsck /dev/sdb

```
![Run fsck on Linux Partition](https://www.tecmint.com/wp-content/uploads/2018/09/Run-fsck-on-Linux-Partition.png)Run fsck on Linux Partition
After running **fsck** , it will return an exit code. These codes can be seen in fsck’s manual by running:
```
**# man fsck**

0      No errors
1      Filesystem errors corrected
2      System should be rebooted
4      Filesystem errors were left uncorrected
8      Operational error
16     Usage or syntax error
32     Checking canceled by user request
128    Shared-library error

```

Sometimes more than one error can be found on a filesystem. In such cases, you may want **fsck** to automatically attempt to correct the errors. This can be done with:
```
# fsck -y /dev/sdb

```

The `-y` flag, automatically `“yes”` to any prompts from fsck to correct an error.
Similarly, you can run the same on all filesystems (without **root**):
```
$ fsck -AR -y

```

In some cases, you may need to run **fsck** on the **root** partition of your system. Since you cannot run **fsck** while the partition is mounted, you can try one of these options:
  * Force fsck upon system boot
  * Run fsck in rescue mode


We will review both situations.
This is relatively easy to complete, the only thing you need to do is create a file called **forcefsck** in the root partition of your system. Use the following command:
```
# touch /forcefsck

```

Then you can simply force or schedule a [reboot of your system](https://www.tecmint.com/disable-shutdown-and-reboot-commands-in-linux/ "Reboot Commands in Linux"). During the next bootup, the **fsck** will be performed. If downtime is critical, it is recommended to plan this carefully, since if there are many used inodes on your system, **fsck** may take some extra time.
After your system boots, check if the file still exists:
```
# ls /forcefsck

```

If it does, you may want to remove it in order to avoid **fsck** on every system boot.
Running **fsck** in **rescue mode** requires a few more steps. First, prepare your system for **reboot**. Stop any critical services like **MySQL/MariaDB** etc and then type.
```
# reboot

```

During the boot, hold down the `shift` key so that the grub menu is shown. Select “**Advanced options** ”.
![Grub Advance Options](https://www.tecmint.com/wp-content/uploads/2018/09/Grub-Advance-Options.png)Grub Advanced Options
Then choose “**Recovery mode** ”.
![Select Linux Recovery Mode](https://www.tecmint.com/wp-content/uploads/2018/09/Select-Linux-Recovery-Mode.png)Select Linux Recovery Mode
In the next menu select “**fsck** ”.
![Select fsck Utility](https://www.tecmint.com/wp-content/uploads/2018/09/Select-fsck-Utility.png)Select fsck Utility
You will be asked if you wish to have your `/` filesystem remounted. Select `“yes”`.
![Confirm Root Filesystem](https://www.tecmint.com/wp-content/uploads/2018/09/Confirm-Root-Filesystem.png)Confirm Root Filesystem
You should see something similar to this.
![Running fsck Filesystem Check](https://www.tecmint.com/wp-content/uploads/2018/09/Running-fsck-Filesystem-Check.png)Running fsck Filesystem Check
You can then resume normal boot, by selecting **“Resume”**.
![Select Normal Boot](https://www.tecmint.com/wp-content/uploads/2018/09/Select-Normal-Boot.png)Select Normal Boot
In this tutorial, you learned how to use fsck and run consistency checks on different Linux filesystems. If you have any questions about **fsck** , please do not hesitate to submit them in the comment section below.
Tags [fsck command examples](https://www.tecmint.com/tag/fsck-command-examples/), [Linux Filesystem Repair](https://www.tecmint.com/tag/linux-filesystem-repair/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[20 Most Commonly Asked MySQL Interview Questions](https://www.tecmint.com/mysql-interview-questions/)
Next article:
[How To Install MySQL Server on Ubuntu 22.04/Ubuntu 20.04](https://www.tecmint.com/install-mysql-ubuntu/)
![Photo of author](https://secure.gravatar.com/avatar/ea5f34ca326c00e992815e5c34104204b0b3bead372195de9eadbcb05880f786?s=100&d=blank&r=g)
Marin Todorov
I am a bachelor in computer science and a Linux Foundation Certified System Administrator. Currently working as a Senior Technical support in the hosting industry. In my free time I like testing new software and inline skating.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#respond)** or
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
### 39 Comments
[Leave a Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/218886ba3ca9b857bed554b08640f1398fe644e24de7c26eafac538f42b99a6c?s=50&d=blank&r=g)
MisterX
[ April 14, 2024 at 2:11 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-2158098)
This is the wrong instruction, on a Debian system, the HDD will be broken.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-2158098)
  2. ![](https://secure.gravatar.com/avatar/9d832a1c52dc824d91247651b25978f2dc6dd6e29c2a6ab2d1d1b25f954c4218?s=50&d=blank&r=g)
Sam Kumar
[ September 15, 2023 at 11:11 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-2060169)
Thank you for this. I used the first option of **fsck** command and it seems to have worked like a charm.
I appreciate your contributing to the community.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-2060169)
  3. ![](https://secure.gravatar.com/avatar/4822e41675306ec9d90d67f798558573b58ca67f0c0f7508925faac737c85539?s=50&d=blank&r=g)
Potat
[ January 20, 2023 at 4:42 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1949166)
When I typed **fsck /dev/SDA -a** , it showed me this,
```
fsck from util-linux 2.38.1
fsck.ext2: Bad magic number in super-block while trying to open /dev/SDA
/dev/SDA :
the super-block could not be read or does not describe a valid ext2/ext3/ext4 filesystem.

```

If the device is valid and it really contains an ext2/ext3/ext4 filesystem (and if not swap or ufs or something else), then the superblock is corrupt, and you might try running e2fsck with an alternate superblock:
```
# e2fsck -b 8193 or e2fsck -b 32768

```

Found a dos partition table in **/dev/SDA**.
When I try to run the **e2fsck** commands it gave, it shows **sh: syntax error: unexpected newline**.
And then when I try to **unmount /dev/SDA** it can’t unmount because it’s an invalid argument?
I’m a total beginner at Linux and I really don’t know what to do now
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1949166)
     * ![](https://secure.gravatar.com/avatar/d6d7477c764cf387ae3cd381bfae073b6971fdef46760e58b9d119d0ae69b118?s=50&d=blank&r=g)
DaVince
[ January 31, 2023 at 3:57 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1954412)
Capitalization and spelling matter on the shell. Device names are never capitalized (so sda, not SDA). unmount should be **umount** , too.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1954412)
  4. ![](https://secure.gravatar.com/avatar/64dedfaa6bb39c20aadf553db995ccd894147aad8ff2748e807f1a5cca1d78d3?s=50&d=blank&r=g)
Sarah
[ July 29, 2022 at 7:22 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1852956)
I updated to the newest version of Ubuntu, now it will not boot. I get the BusyBox black screen and when I used the exit command, here’s the output:
/init: line 866: logsave: not found
Failure: File system check of the root filesystem failed
The root filesystem in /dev/sda6 requires a manual fsck
But when I attempt to do so, I get a text file busy error.
How can I fix this?
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1852956)
  5. ![](https://secure.gravatar.com/avatar/96eb2325e8ee06a46cf61c8bb793553864bd66893e6d0b24ca1d6bcafbe1b527?s=50&d=blank&r=g)
John Shellshear
[ January 1, 2022 at 8:28 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1693963)
Good morning, happy new year to you.
Thank you for the article and your time spent on this website your time spent doing this is very much appreciated by me. I am using a laptop and ran a disk check using the smart control application which stated errors were found.
Although I deleted the partition and reformatted the drive the errors remained which made me curious about error checking and cyclic redundancy checks which lead me to do a little research on physical drive checks and more detailed analysis.
Doing searching online drove me here and to the **FSCK** command which even though I had wiped the drive still showed a wealth of errors (As I ran it without the `-y` flag initially), your article provided some clarity I was missing and made me wonder if some of these errors are reached because there is still junk data left on the drive because I have not low-level formatted it.
So now I am running the command as `'sudo fsck -y -c /dev/sdb'`
Now it will search for errors, fix them as found, and display ongoing progress… Which begs the question… If I low-level formatted this drive by overwriting it with zero, would these errors then be wiped free? And if that is true, then the error that may still be found would be from smart control querying the device bios to see if it’s detected possible hardware failure (As the drive would now be wiped completely clean of any software issues) which means that fsck is really only untangling crosslinked files/sectors/clusters, etc.
Forgive the stupid questions, I am not well educated on computer drives from a hardware perspective, or a read/write/data perspective so I am aware I’m ignorant and most articles I’ve read only give so much in-depth information.
In any case, I am going to let this command run in its entirety and see what the outcome is. Thank you for your time. Thank you for the article.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1693963)
  6. ![](https://secure.gravatar.com/avatar/d653adec599816a0c7f6dd7aed7baea5fc7e2e6075bda1a562c363d67d22107d?s=50&d=blank&r=g)
Csaba
[ December 31, 2021 at 6:20 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1693155)
Does Linux (**ubuntu**) install run fsck before installing? or format automatically “note” the problematic sectors on the new partitions? I try to install Ubuntu and always ran into disc problems How to force a correction before the install?
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1693155)
  7. ![](https://secure.gravatar.com/avatar/3e86888365821f85893f864819f046f1a85e1341f94186af700f26e1db6cd0c2?s=50&d=blank&r=g)
zubair ahmad
[ September 10, 2021 at 12:59 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1586107)
Would be better to get this on youtube.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1586107)
     * ![](https://secure.gravatar.com/avatar/d6d7477c764cf387ae3cd381bfae073b6971fdef46760e58b9d119d0ae69b118?s=50&d=blank&r=g)
DaVince
[ September 13, 2021 at 2:14 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1588322)
Not at all. You can’t copy text out of a video. Text articles work well for this kind of explanation.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1588322)
  8. ![](https://secure.gravatar.com/avatar/0c92c5af80b3447264a75c655c6fec2e83828163b3f286b71d543cd96b4387bf?s=50&d=blank&r=g)
Mani
[ December 1, 2020 at 10:09 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1396896)
Hi Ravi,
I have an issue below on my **Centos 7.7** 64 bit, when i check the log **/var/log/dmesg**.
I have running **RAID1** with two hard disk another one internal hard disk mount manually, now i have unmount another hard disk and showing below message. But the system is booting properly without any issue. Could you help me, what’s the issue and how to solve it.
11.231467] FAT-fs (sdb1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
#df -h
Filesystem Size Used Avail Use% Mounted on
devtmpfs 3.8G 0 3.8G 0% /dev
tmpfs 3.8G 4.0K 3.8G 1% /dev/shm
tmpfs 3.8G 41M 3.8G 2% /run
tmpfs 3.8G 0 3.8G 0% /sys/fs/cgroup
/dev/mapper/centos-root 908G 548G 361G 61% /
/dev/sdb2 3.8G 271M 3.5G 8% /boot
/dev/sdb1 3.8G 12M 3.8G 1% /boot/efi
tmpfs 778M 0 778M 0% /run/user/2
tmpfs 778M 0 778M 0% /run/user/0
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1396896)
  9. ![](https://secure.gravatar.com/avatar/b19360650a19382008f42e3a396283c4987d6784cf93ca9446f6c582db736680?s=50&d=blank&r=g)
Peter
[ November 29, 2020 at 1:38 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1395815)
Want to thank you so much, your advice helped me to fix my Linux-system. I thought I would have to throw away my laptop, now it runs again :-).
Thank you!
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1395815)
     * ![](https://secure.gravatar.com/avatar/d6d7477c764cf387ae3cd381bfae073b6971fdef46760e58b9d119d0ae69b118?s=50&d=blank&r=g)
DaVince
[ December 22, 2020 at 10:49 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1403452)
Just a note, but you probably never have to throw out an entire laptop if the drive fails. Almost all laptops allow quick and easy replacement of the hard drive… Still a good thing you could fix it through just software though. :)
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1403452)
  10. ![](https://secure.gravatar.com/avatar/0769ca6f5d745213d09e4c2cee417c6f5772e133b0b94fdcc6de82d3af30d94f?s=50&d=blank&r=g)
Robercleiton
[ August 18, 2020 at 6:59 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1354050)
Does it support swap partition?
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1354050)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 18, 2020 at 9:58 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1354084)
@Robercleiton,
No, it won’t work, because swap partition does not contain any data and there is no point in repairing it. If swap partition is corrupted, you can fix it using mkswap command.
```
$ sudo mkswap /dev/sda2 #sda2 is swap partition device name
$ sudo swapon /dev/sda2

```
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1354084)
  11. ![](https://secure.gravatar.com/avatar/dd91c1a157d992d789eb401da250cae2344f180d104b25f85600a4852960ddcd?s=50&d=blank&r=g)
L
[ June 10, 2020 at 9:33 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1337071)
Doesn’t work. I have a 32 bits Ubuntu-based system. When I try to use **Gparted** , it says that I must have a more recent version of **e2fsprogs**. When I use **fsck** , it says the same thing. I tried to update through **Synaptic** , it doesn’t see a newer version. I tried to add the PPA (**ppa:hloeung/e2fsprogs**), it shows a mistake, and thus doesn’t show newer packages.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1337071)
     * ![](https://secure.gravatar.com/avatar/d6d7477c764cf387ae3cd381bfae073b6971fdef46760e58b9d119d0ae69b118?s=50&d=blank&r=g)
DaVince
[ December 22, 2020 at 11:02 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1403457)
This is likely related to the fact that 32-bit builds of Ubuntu and Ubuntu packages have been dropped. The PPA you mention also only has a 64-bit build.
If moving to a 64-bit distro isn’t an option, perhaps you can build a 32-bit version of e2fsprogs from the source.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1403457)
  12. ![](https://secure.gravatar.com/avatar/58f8a50af624cfcc3b0838c02fdbb87d514366b703ba17241ae186874056a574?s=50&d=blank&r=g)
pete
[ April 14, 2020 at 1:00 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1326461)
**systemd** broke the well-known `sudo touch /forcefsck` method in 2015.
Since then, it hasn’t worked.
There is an obtuse grub command that does work or just boot from alternate media, like from a “**Try Ubuntu** ” flash drive, then run the **fsck** from that environment.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1326461)
  13. ![](https://secure.gravatar.com/avatar/75f37a4fa1899eeeac99a19ed6822952e472d8b33a3fcad24337f9675c6817ee?s=50&d=blank&r=g)
Anthony
[ April 10, 2020 at 5:01 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1325887)
Hi,
I ran `fsck -y`.
The volume could not be repaired after 3 attempts
Any suggestions?
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1325887)
  14. ![](https://secure.gravatar.com/avatar/1feb3ab121906844ed15e63ab2bc5e49acbd1475f656a0fadf78382865c14593?s=50&d=blank&r=g)
Torben Friis
[ March 5, 2020 at 1:54 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1320086)
Hi,
I did a umount and:
```
torben@torben-Aspire-E5-773G:~$ sudo fsck /dev/sdb6
fsck from util-linux 2.31.1
e2fsck 1.44.1 (24-Mar-2018)
/dev/sdb6: clean, 185609/30433280 files, 4058434/121728256 blocks

```

No return code, but the file disappeared (not in fstab, but in lsblk). What happened? Can I get it back?
Best regards
torben
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1320086)
  15. ![](https://secure.gravatar.com/avatar/3d2854a3aacd3cbd1879559d729332908de9b7dede7f02cc9170e46c2b95ade2?s=50&d=blank&r=g)
Peter
[ December 26, 2019 at 6:28 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1308599)
Recovery options in this guide are obsolete.
You can no longer check all filesystems with the recovery menu since all filesystems mount as read-write. The logic of the recovery boot menu is broken now.
Also, adding `/forcefsck` no longer works on recent Ubuntu versions with systemd.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1308599)
  16. ![](https://secure.gravatar.com/avatar/90a4abe91f19216f89104cff8b3ecf87e4f96461677c8afb46ea045c30da6535?s=50&d=blank&r=g)
Shaan
[ November 14, 2019 at 8:54 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1288955)
Hello,
I need to run **fsck** on root, but for some reason creation of **forcefsck** does not result in a file systems consistency check upon **sudo reboot** it just takes me directly to the GRUB menu.
Any advice?
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1288955)
  17. ![](https://secure.gravatar.com/avatar/b77a4256cadc0c6fba7fd26a1a1d35c7ff9883fc4964944006278fbe1ce5bbb9?s=50&d=blank&r=g)
Ricardo
[ October 13, 2019 at 3:27 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1267881)
This was an awesome little guide! However, why doesn’t it work for me? I think it has to do with the fact that I’ve set up my OS to use LVM, even when I use `touch /forcefsck`, the log states that I should no longer use forcefsck but rather use the command in grub… any idea?
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1267881)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 14, 2019 at 10:43 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1268352)
@Ricardo,
Could you share the screenshot or output of the forcefsck command?
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1268352)
  18. ![](https://secure.gravatar.com/avatar/3b39248a39e4ba3ebe62c387b359cc6156f2520471352a18a0356994da456c71?s=50&d=blank&r=g)
Robert
[ August 27, 2019 at 11:49 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1232887)
Lifesaver, short and accurate article..
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1232887)
  19. ![](https://secure.gravatar.com/avatar/5fc3e1438b559363cc5fd1b28260532eef7009a500cb1c5face7226cc28a6512?s=50&d=blank&r=g)
Domingo
[ May 24, 2019 at 5:07 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1157162)
Thank a lot Sir, was very useful
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1157162)
  20. ![](https://secure.gravatar.com/avatar/a6e4dd841d9c4a1927fc44e77baefae8c0d9270b0b18fc5d2afb352a0ba611c2?s=50&d=blank&r=g)
Michael Plemmons
[ April 18, 2019 at 11:59 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1134545)
I tried it from the recovery mode and I get to the screen to switch to read/write and click **yes** , then it says `dev/sda1` is mounted and takes me back to recovery menu.
If I click **fsck** again, it says this operation requires me to be in read-only mode and the last operation requested switched me to read/write. To go back to read-only, reboot the system. I’ve done this over and over. I’m in **Ubuntu 18.10**. Any ideas? Thanks
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1134545)
     * ![](https://secure.gravatar.com/avatar/c0cb1a76f648e666648589441348d363c19d6e4730d6ec8c7031dc22c98ac1ba?s=50&d=blank&r=g)
Mike
[ April 20, 2019 at 4:49 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1136025)
I have exact same problem with Mint 19.1 virtual machine on VirtualBox.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1136025)
     * ![](https://secure.gravatar.com/avatar/fd7198faaed615d1867068fa0ad447eb5bcbc0ef8bd030508b360d19fe8af31c?s=50&d=blank&r=g)
Udaka
[ September 25, 2019 at 12:20 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1254183)
I have the exact same issue – it says `**dev/sda1** ` is mounted and aborts and when I try again it says now it has to be `**readonly** ` – did you manage to get it fixed?
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1254183)
  21. ![](https://secure.gravatar.com/avatar/3803650465a6324d04d842b6dc92f90e3e3580f1991c463e577879e07cf7b909?s=50&d=blank&r=g)
Hung
[ April 8, 2019 at 4:20 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1127681)
I have a VPS CentOS 7, If following this tutorial, will i lose my data on vps ?
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1127681)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 9, 2019 at 10:35 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1128153)
@Hung,
Not at all, fsck only scans for filesystem errors and fix it
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1128153)
  22. ![](https://secure.gravatar.com/avatar/25eeef67d91ba71eefc527ac1a71c207a63e4ee64f7b0a6a6b17129be850a583?s=50&d=blank&r=g)
Jim
[ April 3, 2019 at 10:13 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1125029)
What version of Ubuntu does this article relate to? People like me are still using 16.04 because of all of 18.04’s problems and I don’t see the graphic just below the line, “You can then resume to normal boot, by selecting “Resume”. Is that GUI ONLY in 18.04?
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1125029)
  23. ![](https://secure.gravatar.com/avatar/a1ee11a1894fbddbd388f7f548c7778e5931038da9ce5581a44abf4bb3a3ee47?s=50&d=blank&r=g)
Rajan bhandari
[ March 14, 2019 at 10:47 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1112587)
My PC is not showing 64 bit while I try to install it. What to do please help me..
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1112587)
  24. ![](https://secure.gravatar.com/avatar/a86b3d9d99a9a59f4ec062d7cf97b3f6c51d63a86c8b8de1b569f9191b7cbff5?s=50&d=blank&r=g)
R. Owen Sterling
[ March 7, 2019 at 12:56 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1108781)
Classic Ubuntu user arrogance, to equate Ubuntu with all of Linux in the headline, then list *Ubuntu-specific recovery-mode options as if they were universal. Just about every “recovery mode” I’ve ever seen, even under GRUB 2, is a command line prompt with very limited options. Well the first half of the article is universal, at least.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1108781)
  25. ![](https://secure.gravatar.com/avatar/263cbf0a79c3561232933b81d0fd6a32baf3bbd76d57be6b3e8b542860842b8c?s=50&d=blank&r=g)
Tswelelopele Tsele
[ February 28, 2019 at 1:40 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1105906)
Still doesn’t work. I can’t access root, my command starts with (initramfs)
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1105906)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 28, 2019 at 10:32 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1106077)
@Tsele,
Your question is not clear, could you elaborate more..
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1106077)
  26. ![](https://secure.gravatar.com/avatar/ea5f34ca326c00e992815e5c34104204b0b3bead372195de9eadbcb05880f786?s=50&d=blank&r=g)
Marin Todorov
[ October 3, 2018 at 12:10 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1042779)
@Eric, if you have an issue with a windows partition, it would be better to use **chkdsk** windows utility. In Linux, there is **fsck.ntfs** which is a symlink to **ntfsfix**.
**ntfsfix** is a utility that fixes some common NTFS problems. ntfsfix is NOT a Linux version of chkdsk. It only repairs some fundamental NTFS inconsistencies, resets the NTFS journal file and schedules an NTFS consistency check for the first boot into Windows.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1042779)
  27. ![](https://secure.gravatar.com/avatar/5be5758c52b2eb42653a309a9fc21a76d69c43e5f96ce2e00bb47469e7bd92d8?s=50&d=blank&r=g)
Eric D.
[ October 2, 2018 at 7:12 pm  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1042475)
Interesting, but what about an external drive that giving problems running Windows 10? will fsck “**fix** ” that drive as well? And is the syntax the same? (Just point your Linux machine to it and run fsck??)
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1042475)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 3, 2018 at 11:06 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1042772)
@Eric,
I don’t think fsck recognize windows filesystem, never tried it. I think you should give a try and see..:)
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1042772)
     * ![](https://secure.gravatar.com/avatar/a86b3d9d99a9a59f4ec062d7cf97b3f6c51d63a86c8b8de1b569f9191b7cbff5?s=50&d=blank&r=g)
R. Owen Sterling
[ March 7, 2019 at 1:00 am  ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1108784)
If you have the **ntfs4g** binaries installed, **fsck** can evaluate and even fix said partitions; that said, Windows specific tools, such as **CHKDSK** are (for once) less destructive and get better results if you’re trying to preserve as much data as possible.
[Reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#comment-1108784)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/#respond)
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
[How to Delete Root Mails (Mailbox) File in Linux](https://www.tecmint.com/delete-root-mails-mailbox-file-in-linux/)
[How To Create a Linux Swap File](https://www.tecmint.com/create-a-linux-swap-file/)
[How to Fix “bash: curl: command not found” Error](https://www.tecmint.com/bash-curl-command-not-found-error/)
[How to Use the Cat Command in Linux [22 Useful Examples]](https://www.tecmint.com/cat-command-linux/)
[Fast – Test Your Internet Download Speed from Linux Terminal](https://www.tecmint.com/fast-test-internet-download-speed-in-linux/)
[How to Use diff3 Command for File Merging in Linux](https://www.tecmint.com/diff3-command-in-linux/)
## Linux Server Monitoring Tools
[Monitor Server Resources with Collectd-web and Apache CGI in Linux](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/)
[How To Install Elasticsearch, Logstash, and Kibana (ELK Stack) on RHEL](https://www.tecmint.com/install-elasticsearch-logstash-and-kibana-elk-stack-on-centos-rhel-7/)
[Installing “PHP Server Monitor” Tool using LEMP or LAMP Stack in Arch Linux](https://www.tecmint.com/install-php-server-monitor-in-arch-linux/)
[Htop – An Interactive Process Viewer for Linux](https://www.tecmint.com/htop-linux-process-monitoring/)
[Iotop – Monitor Linux Disk I/O Activity and Usage Per-Process Basis](https://www.tecmint.com/iotop-monitor-linux-disk-io-activity-per-process/)
[Petiti – An Open Source Log Analysis Tool for Linux SysAdmins](https://www.tecmint.com/petiti-log-analysis-tool-for-linux-sysadmins/)
## Learn Linux Tricks & Tips
[How to Use ‘Yum History’ to Find Out Installed or Removed Packages Info](https://www.tecmint.com/view-yum-history-to-find-packages-info/)
[How to Run Linux Commands in Background and Detach in Terminal](https://www.tecmint.com/run-linux-command-in-background/)
[How to Create a Password Protected ZIP File in Linux](https://www.tecmint.com/create-password-protected-zip-file-in-linux/)
[How to Find and Remove Duplicate/Unwanted Files in Linux Using ‘FSlint’ Tool](https://www.tecmint.com/fslint-find-and-remove-duplicate-unwanted-files-in-linux/)
[7 Ways to Determine the File System Type in Linux (Ext2, Ext3 or Ext4)](https://www.tecmint.com/find-linux-filesystem-type/)
[Find Out All Live Hosts IP Addresses Connected on Network in Linux](https://www.tecmint.com/find-live-hosts-ip-addresses-on-linux-network/)
## Best Linux Tools
[13 Most Used Microsoft Office Alternatives for Linux](https://www.tecmint.com/microsoft-office-alternatives-for-linux/)
[5 Best Microsoft Word Alternatives for Linux in 2024](https://www.tecmint.com/microsoft-word-alternatives-linux/)
[Top 3 Open Source Virtual Data Room (VDR) for Linux](https://www.tecmint.com/open-source-virtual-data-room-for-linux/)
[How to Open and Edit Apple iWork Files on Linux](https://www.tecmint.com/open-and-edit-apple-iwork-files-on-linux/)
[5 Best Reference Management Software for Linux in 2024](https://www.tecmint.com/reference-management-software/)
[Top 6 Telegram Bots to Boost Your Productivity in 2025](https://www.tecmint.com/best-telegram-bots/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/ "Scroll back to top")
Search for:
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
