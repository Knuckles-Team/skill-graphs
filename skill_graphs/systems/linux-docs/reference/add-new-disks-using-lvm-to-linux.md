[Skip to content](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/)
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
  * [Pro Courses](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/)
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
  * [Pro Courses](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/)
# How to Add New Disks Using LVM to an Existing Linux System
[Lakshmi Dhandapani](https://www.tecmint.com/author/lakshmi/ "View all posts by Lakshmi Dhandapani")Last Updated: July 14, 2023 Read Time: 2 minsCategories [Linux Commands](https://www.tecmint.com/category/linux-commands/) [9 Comments](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comments)
[LVM (Logical Volume Management)](https://www.tecmint.com/create-lvm-storage-in-linux/) is a flexible and advanced option available to manage hard disks in most of the major Linux distributions. It is easy to manage the disks with LVM than the tradition tools like [fdisk](https://www.tecmint.com/fdisk-commands-to-manage-linux-disk-partitions/), [parted](https://www.tecmint.com/parted-command-to-create-resize-rescue-linux-disk-partitions/) or **gparted**.
Some of the terms which you need to understand while using LVM:
  * **Physical Volume (PV)** : Consists of Raw disks or RAID arrays or other storage devices.
  * **Volume Group (VG)** : Combines the physical volumes into storage groups.
  * **Logical Volume (LV)** : VG’s are divided into LV’s and are mounted as partitions.


In this article, we will take you through the steps to configure Disks using LVM in existing Linux machine by creating PV, VG’s and LV’s.
**Note** : If you don’t what to use LVM, you can add disk directly to an existing Linux system using these guides.
  1. [How to Add a New Disk to Linux System](https://www.tecmint.com/add-new-disk-to-an-existing-linux/)
  2. [How to Add a New Disk Larger Than 2TB to Linux System](https://www.tecmint.com/add-disk-larger-than-2tb-to-an-existing-linux/)


Let’s consider a scenario where there are **2 HDD** of **20GB** and **10GB** , but we need to add only 2 partitions one of **12GB** and another **13GB**. We can achieve this using LVM method only.
Once the disks has been added, you can list them using the following command.
```
# fdisk -l

```
![Verify Hard Disks](https://www.tecmint.com/wp-content/uploads/2017/04/Verify-Hard-Disks-in-Linux.png)Verify Hard Disks
**1.** Now partitions both the disks `/dev/xvdc` and `/dev/xvdd` using fdisk command as shown.
```
# fdisk /dev/xvdc
# fdisk /dev/xvdd

```

Use `n` to create the partition and save the changes with `w` command.
![Partition Hark Disks](https://www.tecmint.com/wp-content/uploads/2017/04/Partition-Hark-Disks.png)Partition Hark Disks
**2.** After partitioning, use the following command to verify the partitions.
```
# fdisk -l

```
![Verify New Partitions](https://www.tecmint.com/wp-content/uploads/2017/04/Verify-New-Partitions.png)Verify New Partitions
**3.** Create Physical Volume (PV).
```
# pvcreate /dev/xvdc1
# pvcreate /dev/xvdd1

```
![Create Physical Volume](https://www.tecmint.com/wp-content/uploads/2017/04/Create-Physical-Volume.png)Create Physical Volume
**4.** Create Volume Group (VG).
```
# vgcreate testvg /dev/xvdc1 /dev/xvdd1

```

Here, “**testvg** ” is the VG name.
![Create Volume Group](https://www.tecmint.com/wp-content/uploads/2017/04/Create-Volume-Group.png)Create Volume Group
**5.** Now use “**vgdisplay** ” to list all details about the VG’s in the system.
```
# vgdisplay
OR
# vgdisplay testvg

```
![List Volume Group](https://www.tecmint.com/wp-content/uploads/2017/04/List-Volume-Group.png)List Volume Group
**6.** Create Logical Volumes (LV).
```
# lvcreate -n lv_data1 --size 12G testvg
# lvcreate -n lv_data2 --size 14G testvg

```

Here, “**lv_data1** ” and “**lv_data2** ” are LV name.
![Create Logical Volumes](https://www.tecmint.com/wp-content/uploads/2017/04/Create-Logical-Volumes.png)Create Logical Volumes
**7.** Now use “**lvdisplay** ” to list all details about the Logical volumes available in the system.
```
# lvdisplay
OR
# lvdisplay testvg

```
![List Logical Volumes](https://www.tecmint.com/wp-content/uploads/2017/04/List-Logical-Volumes.png)List Logical Volumes
**8.** Format the Logical Volums (LV’s) to ext4 format.
```
# mkfs.ext4 /dev/testvg/lv_data1
# mkfs.ext4/dev/testvg/lv_data2

```
![Format LV to Ext4 Format](https://www.tecmint.com/wp-content/uploads/2017/04/Format-LV-to-Ext4-Format.png)Format LV to Ext4 Format
**9.** Finally, mount the file system.
```
# mount /dev/testvg/lv_data1 /data1
# mount /dev/testvg/lv_data2 /data2

```

Make sure to create `data1` and `data2` directories before mounting the filesystem.
![Mount Filesystem](https://www.tecmint.com/wp-content/uploads/2017/04/Mount-Filesystem.png)Mount Filesystem
That’s it! In this article, we discussed how to create a partition using LVM. If you have any comments or queries regarding this, feel free to post in the comments.
Tags [lvm](https://www.tecmint.com/tag/lvm/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Deal: Learn Network Security With This 4-Course Cyber Security Bundle](https://www.tecmint.com/learn-network-security-with-cyber-security-course/)
Next article:
[10 Reasons Why You Should Use Vi/Vim Text Editor in Linux](https://www.tecmint.com/reasons-to-learn-vi-vim-editor-in-linux/)
![Photo of author](https://secure.gravatar.com/avatar/46b1838a370485295736cd10b85fba77acf6e44d25035b8ee682e9e2dc22c4b6?s=100&d=blank&r=g)
Lakshmi Dhandapani
I work on various platforms including IBM-AIX, Solaris, HP-UX, and storage technologies ONTAP and OneFS and have hands on experience on Oracle Database.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#respond)** or
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
### 9 Comments
[Leave a Reply](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/ceb8447109b676e76ad537d1f14f4e5800388dc8192a4c31eab58c13a430a660?s=50&d=blank&r=g)
Scott G.
[ April 19, 2023 at 1:25 am  ](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1998613)
Why would you people create partitions? The WHOLE point of **lvm** is to replace traditional partitions with something more flexible. On a physical disk, it’s just a redundancy, but in the virtual world, you are just creating a partition prison for your data that you cannot easily expand.
If you **pvcreate** on the raw device instead of a partition, should that raw device ever change sizes (as in growing a virtual disk), it is trivial to expand it to use the space. With a partition, it’s a huge problem.
There is no benefit to a partition, other than for admins who still use **fdisk** instead of **lsblk** to see disk volumes. The ONLY place you need a partition is for your boot volume, as that is a limitation of traditional hardware.
[Reply](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1998613)
  2. ![](https://secure.gravatar.com/avatar/56b43b384d95d7b935972b392f762a5fb088287d4972000ff2049bf0d7afb15f?s=50&d=blank&r=g)
dragonmouth
[ May 1, 2021 at 2:55 am  ](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1484213)
I was taught that the hard drive naming convention in Linux is ‘**/dev/hdx#** ‘ or ‘**/dev/sdx#** ‘. In the article, you are using ‘**xvdc** ‘ and ‘**xvdd** ‘.
```
# fdisk /dev/xvdc
# fdisk /dev/xvdd

```

Have I been misinformed?
[Reply](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1484213)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 3, 2021 at 11:18 am  ](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1485092)
@Drgaonmouth,
We have used cloud virtual storage devices for this setup, that’s why the naming is XVD.
[Reply](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1485092)
  3. ![](https://secure.gravatar.com/avatar/c8e594ac24987adf2f2088b5058e7efef4d40030f71012b72cafbf4e4519ad46?s=50&d=blank&r=g)
mykrkuoo
[ April 18, 2020 at 2:03 am  ](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1328247)
Can just a single partition be part of a logical device? I have a **Win10** notebook. The **Win10** requirements occupy most of the space on sda. Can I set up a small Linux partition on sda that connects with a physical USB disk I keep plugged into the machine to make up a logical disk for Linux? My Win install is MBR, non-UEFI, not secure boot, but would that make any difference?
[Reply](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1328247)
  4. ![](https://secure.gravatar.com/avatar/ce47afb51b823f8c8c47fc444b9ad7089103ae5353972a2eb516f9f866715da5?s=50&d=blank&r=g)
Brett Holman
[ January 4, 2020 at 5:33 am  ](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1310193)
It may be worth adding a final step about updating **/etc/fstab** so that the mount is persistent across boots.
[Reply](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1310193)
  5. ![](https://secure.gravatar.com/avatar/ef9992c3ba34d20375419e70db578fae2eabc81f7cdde00fac81f12838806076?s=50&d=blank&r=g)
Sajal
[ May 25, 2019 at 10:52 pm  ](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1157696)
Any idea how can I automate this task using shell script along with multipath configuration
[Reply](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1157696)
  6. ![](https://secure.gravatar.com/avatar/44e05ae038834e653cbe5822a69bcde5e8dc21c7ca9a016f3155027b14870829?s=50&d=blank&r=g)
ganesh
[ February 12, 2019 at 8:53 pm  ](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1100629)
for create LVM we need to select type 8e.
[Reply](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1100629)
  7. ![](https://secure.gravatar.com/avatar/feced550a97b5ed1ef049eb147e8c1e8a06221ee5c63f339301c08efa4fff02b?s=50&d=blank&r=g)
george
[ August 23, 2018 at 11:13 pm  ](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1026810)
Hi nice article. I noticed that you did’t change the partition type to **lv** i.e. **8e** but created a **83** type. I thought we needed to create a **8e** type partition to be able to create a physical volume or is this distro specific.
[Reply](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-1026810)
  8. ![](https://secure.gravatar.com/avatar/838f66940c8beb882b803c4d84ebdc4ccca2a38dae19e3d4659d99a76055b73f?s=50&d=blank&r=g)
Shiraz
[ May 29, 2018 at 1:44 pm  ](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-998551)
You did not set the Partition type hex code 8e for the LVM created. This will create issues later
[Reply](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#comment-998551)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/#respond)
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
[Learn How to Set Your $PATH Variables Permanently in Linux](https://www.tecmint.com/set-path-variable-linux-permanently/)
[How to Block USB Storage Devices in Linux Servers](https://www.tecmint.com/block-usb-storage-devices-in-linux/)
[30 Useful Linux Commands for System Administrators](https://www.tecmint.com/useful-linux-commands-for-system-administrators/)
[26 Security Hardening Tips for Modern Linux Servers](https://www.tecmint.com/linux-server-hardening-security-tips/)
[Googler: A Command Line Tool to Do ‘Google Search’ from Linux Terminal](https://www.tecmint.com/google-commandline-search-terminal/)
[How to Get Hardware Information with Dmidecode Command on Linux](https://www.tecmint.com/how-to-get-hardware-information-with-dmidecode-command-on-linux/)
## Linux Server Monitoring Tools
[How to Setup Rsyslog Client to Send Logs to Rsyslog Server in CentOS 7](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/)
[5 Tools to Scan a Linux Server for Malware and Rootkits](https://www.tecmint.com/scan-linux-for-malware-and-rootkits/)
[How to Automate Daily Linux Health Checks with a Bash Script + Cron](https://www.tecmint.com/bash-script-automate-system-health-checks/)
[systemd-analyze – Find System Boot-up Performance Statistics in Linux](https://www.tecmint.com/systemd-analyze-monitor-linux-bootup-performance/)
[How to Use ‘fsck’ to Repair Linux File System Errors](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/)
[A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%](https://www.tecmint.com/monitor-disk-usage-bash-script/)
## Learn Linux Tricks & Tips
[How to Find and Sort Files Based on Modification Date and Time in Linux](https://www.tecmint.com/find-and-sort-files-modification-date-and-time-in-linux/)
[How to Optimize and Compress JPEG or PNG Images in Linux Commandline](https://www.tecmint.com/optimize-and-compress-jpeg-or-png-batch-images-linux-commandline/)
[How to Find Difference Between Two Directories Using Diff and Meld Tools](https://www.tecmint.com/compare-find-difference-between-two-directories-in-linux/)
[How to Create Hard and Symbolic Links in Linux](https://www.tecmint.com/create-hard-and-symbolic-links-in-linux/)
[Understanding Shell Commands Easily Using “Explain Shell” Script in Linux](https://www.tecmint.com/explain-shell-commands-in-the-linux-shell/)
[How to Force User to Change Password at Next Login in Linux](https://www.tecmint.com/force-user-to-change-password-next-login-in-linux/)
## Best Linux Tools
[27 Best Tools for VMware Administrators in 2024](https://www.tecmint.com/vmware-administrators-tools/)
[15 Best Open Source Music Making Software for Linux in 2024](https://www.tecmint.com/free-music-creation-or-audio-editing-softwares-for-linux/)
[10 Best PDF Document Viewers for Linux Systems](https://www.tecmint.com/linux-pdf-viewers-and-readers-tools/)
[10 Best Google Drive Clients for Linux in 2023](https://www.tecmint.com/google-drive-clients-linux/)
[Top 7 Apps to Install for Your Nextcloud Instance](https://www.tecmint.com/nextcloud-apps/)
[5 Top Open-Source Microsoft 365 Alternatives for Linux](https://www.tecmint.com/microsoft-365-alternatives/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/add-new-disks-using-lvm-to-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
