[Skip to content](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/)
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
  * [Pro Courses](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/ "Linux Online Courses")
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


[](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/)
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
  * [Pro Courses](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/ "Linux Online Courses")
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


[](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/)
# Linux Performance Monitoring with Vmstat and Iostat Commands
[Ravi Saive](https://www.tecmint.com/author/admin/ "View all posts by Ravi Saive")Last Updated: July 14, 2023 Read Time: 4 minsCategories [Linux Commands](https://www.tecmint.com/category/linux-commands/), [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [23 Comments](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comments)
This is our ongoing series of [Linux Commands](https://www.tecmint.com/linux-commands-cheat-sheet/ "Linux Commands with Examples") and [Linux Performance Monitoring](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/ "Linux Performance Monitoring Commands"), in this article, you will learn about **Vmstat** and **Iostat** commands, which are available on all major **Unix-like** (**Linux/Unix/FreeBSD/Solaris**) Operating Systems.
**vmstat** command (also known as virtual memory statistic tool) shows information about processes, memory, disk, and CPU activity in Linux, whereas the **iostat** command is used to monitor CPU utilization, system input/output statistics for all the disks and partitions.
If **vmstat** and **iostat** commands are not available in your Linux machine, please install the **sysstat** package. The **vmstat** , **sar,** and **iostat** commands are the collection of package included in [sysstat – the system monitoring tools](https://www.tecmint.com/install-sysstat-in-linux/ "Linux System Performance Monitoring Tools").
You may download and install **sysstat** using the source tarball from link
### Install Sysstat in Linux
```
$ sudo apt install sysstat         [On **Debian, Ubuntu and Mint**]
$ sudo yum install sysstat         [On **RHEL/CentOS/Fedora** and **Rocky Linux/AlmaLinux**]
$ sudo emerge -a app-admin/sysstat [On **Gentoo Linux**]
$ sudo pacman -S sysstat           [On **Arch Linux**]
$ sudo zypper install sysstat      [On **OpenSUSE**]

```
![Install Sysstat in Linux](https://www.tecmint.com/wp-content/uploads/2012/09/Install-Sysstat-in-Linux.png) Install Sysstat in Linux
### Learn Vmstat Command Examples in Linux
In this section, you will learn about 6 vmstat command examples and usage with screenshots.
#### 1. List Active and Inactive Memory
In the below example, there are six columns. The significance of the columns are explained on the man page of **vmstat** in detail. The most important fields are **free** under memory and **si, so** under the swap column.
```
**[root@tecmint ~]# vmstat -a**

procs -----------memory---------- ---swap-- -----io---- --system-- -----cpu-----
 r  b   swpd   free  inact active   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 810420  97380  70628    0    0   115     4   89   79  1  6 90  3  0
```

  * **Free** – Amount of free/idle memory spaces.
  * **si** – Swapped in every second from disk in KiloBytes.
  * **so** – Swapped out every second to disk in KiloBytes.


**Note:** If you run **vmstat** without parameters it will display a summary report since system boot.
#### 2. Execute vmstat ‘X’ seconds and (‘Number of times)
With this command, **vmstat** execute every two seconds and stop automatically after executing six intervals.
```
**[root@tecmint ~]# vmstat 2 6**

procs -----------memory---------- ---swap-- -----io---- --system-- -----cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0 810420  22064 101368    0    0    56     3   50   57  0  3 95  2  0
 0  0      0 810412  22064 101368    0    0     0     0   16   35  0  0 100  0  0
 0  0      0 810412  22064 101368    0    0     0     0   14   35  0  0 100  0  0
 0  0      0 810412  22064 101368    0    0     0     0   17   38  0  0 100  0  0
 0  0      0 810412  22064 101368    0    0     0     0   17   35  0  0 100  0  0
 0  0      0 810412  22064 101368    0    0     0     0   18   36  0  1 100  0  0
```

#### 3. Vmstat with Timestamps
**vmstat** command with `-t` parameter shows timestamps with every line printed as shown below.
```
**[tecmint@tecmint ~]$ vmstat -t 1 5**

procs -----------memory---------- ---swap-- -----io---- --system-- -----cpu------ ---timestamp---
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0 632028  24992 192244    0    0    70     5   55   78  1  3 95  1  0        2012-09-02 14:57:18 IST
 1  0      0 632028  24992 192244    0    0     0     0  171  514  1  5 94  0  0        2012-09-02 14:57:19 IST
 1  0      0 631904  24992 192244    0    0     0     0  195  600  0  5 95  0  0        2012-09-02 14:57:20 IST
 0  0      0 631780  24992 192244    0    0     0     0  156  524  0  5 95  0  0        2012-09-02 14:57:21 IST
 1  0      0 631656  24992 192244    0    0     0     0  189  592  0  5 95  0  0        2012-09-02 14:57:22 IST
```

#### 4. Statistics of Various Counter
**vmstat** command with `-s` switch displays summary of various event counters and memory statistics.
```
**[tecmint@tecmint ~]$ vmstat -s**

      1030800  total memory
       524656  used memory
       277784  active memory
       185920  inactive memory
       506144  free memory
        26864  buffer memory
       310104  swap cache
      2064376  total swap
            0  used swap
      2064376  free swap
         4539 non-nice user cpu ticks
            0 nice user cpu ticks
        11569 system cpu ticks
       329608 idle cpu ticks
         5012 IO-wait cpu ticks
           79 IRQ cpu ticks
           74 softirq cpu ticks
            0 stolen cpu ticks
       336038 pages paged in
        67945 pages paged out
            0 pages swapped in
            0 pages swapped out
       258526 interrupts
       392439 CPU context switches
   1346574857 boot time
         2309 forks
```

#### 5. Monitor Linux Disks Statistics
**vmstat** with `-d` option display all disks statistics of Linux.
```
**[tecmint@tecmint ~]$ vmstat -d**

disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
ram0       0      0       0       0      0      0       0       0      0      0
ram1       0      0       0       0      0      0       0       0      0      0
ram2       0      0       0       0      0      0       0       0      0      0
ram3       0      0       0       0      0      0       0       0      0      0
ram4       0      0       0       0      0      0       0       0      0      0
ram5       0      0       0       0      0      0       0       0      0      0
ram6       0      0       0       0      0      0       0       0      0      0
ram7       0      0       0       0      0      0       0       0      0      0
ram8       0      0       0       0      0      0       0       0      0      0
ram9       0      0       0       0      0      0       0       0      0      0
ram10      0      0       0       0      0      0       0       0      0      0
ram11      0      0       0       0      0      0       0       0      0      0
ram12      0      0       0       0      0      0       0       0      0      0
ram13      0      0       0       0      0      0       0       0      0      0
ram14      0      0       0       0      0      0       0       0      0      0
ram15      0      0       0       0      0      0       0       0      0      0
loop0      0      0       0       0      0      0       0       0      0      0
loop1      0      0       0       0      0      0       0       0      0      0
loop2      0      0       0       0      0      0       0       0      0      0
loop3      0      0       0       0      0      0       0       0      0      0
loop4      0      0       0       0      0      0       0       0      0      0
loop5      0      0       0       0      0      0       0       0      0      0
loop6      0      0       0       0      0      0       0       0      0      0
loop7      0      0       0       0      0      0       0       0      0      0
sr0        0      0       0       0      0      0       0       0      0      0
sda     7712   5145  668732  409619   3282  28884  257402  644566      0    126
dm-0   11578      0  659242 1113017  32163      0  257384 8460026      0    126
dm-1     324      0    2592    3845      0      0       0       0      0      2
```

#### 6. Display Statistics in Megabytes
The **vmstat** displays memory statistics in kilobytes by default, but you can also display reports with memory sizes in megabytes with the argument `-S M`. Consider the following example.
```
**[root@tecmint ~]# vmstat -S M 1 5**

procs -----------memory---------- ---swap-- -----io---- --system-- -----cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0    346     53    476    0    0    95     8   42   55  0  2 96  2  0
 0  0      0    346     53    476    0    0     0     0   12   15  0  0 100  0  0
 0  0      0    346     53    476    0    0     0     0   32   62  0  0 100  0  0
 0  0      0    346     53    476    0    0     0     0   15   13  0  0 100  0  0
 0  0      0    346     53    476    0    0     0     0   34   61  0  1 99  0  0
```

### Learn Iostat Command Examples in Linux
In this section, you will learn about 6 iostat command examples and usage with screenshots.
#### 7. Display CPU and I/O Statistics of Disks
**iostat** without arguments displays **CPU** and **I/O** statistics of all partitions as shown below.
```
**[root@tecmint ~]# iostat**

Linux 2.6.32-279.el6.i686 (tecmint.com)         09/03/2012      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.12    0.01    1.54    2.08    0.00   96.24

Device:            tps   Blk_read/s   Blk_wrtn/s   Blk_read   Blk_wrtn
sda               3.59       161.02        13.48    1086002      90882
dm-0              5.76       159.71        13.47    1077154      90864
dm-1              0.05         0.38         0.00       2576          0
```

#### 8. Shows Linux CPU Statistics
**iostat** with `-c` arguments displays only **CPU** statistics as shown below.
```
**[root@tecmint ~]# iostat -c**

Linux 2.6.32-279.el6.i686 (tecmint.com)         09/03/2012      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.12    0.01    1.47    1.98    0.00   96.42
```

#### 9. Shows Linux Disks I/O Statistics
**iostat** with `-d` arguments display only disk **I/O** statistics of all partitions as shown.
```
**[root@tecmint ~]# iostat -d**

Linux 2.6.32-279.el6.i686 (tecmint.com)         09/03/2012      _i686_  (1 CPU)

Device:            tps   Blk_read/s   Blk_wrtn/s   Blk_read   Blk_wrtn
sda               3.35       149.81        12.66    1086002      91746
dm-0              5.37       148.59        12.65    1077154      91728
dm-1              0.04         0.36         0.00       2576          0
```

#### 10. Shows I/O Statistics of Specific Device
By default, it displays statistics of all partitions, with `-p` and device name arguments display only disks **I/O** statistics for specific device only as shown.
```
**[root@tecmint ~]# iostat -p sda**

Linux 2.6.32-279.el6.i686 (tecmint.com)         09/03/2012      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.11    0.01    1.44    1.92    0.00   96.52

Device:            tps   Blk_read/s   Blk_wrtn/s   Blk_read   Blk_wrtn
sda               3.32       148.52        12.55    1086002      91770
sda1              0.07         0.56         0.00       4120         18
sda2              3.22       147.79        12.55    1080650      91752
```

#### 11. Display LVM Statistics
With `-N` (Uppercase) parameter displays only **LVM** statistics as shown.
```
**[root@tecmint ~]# iostat -N**

Linux 2.6.32-279.el6.i686 (tecmint.com)         09/03/2012      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.11    0.01    1.39    1.85    0.00   96.64

Device:            tps   Blk_read/s   Blk_wrtn/s   Blk_read   Blk_wrtn
sda               3.20       142.84        12.16    1086002      92466
vg_tecmint-lv_root     5.13       141.68        12.16    1077154      92448
vg_tecmint-lv_swap     0.04         0.34         0.00       2576          0
```

#### 12. Check Iostat Version
With `-V` (Uppercase) parameter display version of **iostat** as shown.
```
**[root@tecmint ~]# iostat -V**

sysstat version 11.7.3
(C) Sebastien Godard (sysstat  orange.fr)
```

The **vmstat** and **iostat** contain a number of columns and flags which may not possible to explain in detail. If you want to know more about it you may refer man page of **vmstat** and **iostat**.
```
# man vmstat
# man iostat

```

Please share it if you find this article is useful through our comment box below.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[13 Linux Network Configuration and Troubleshooting Commands](https://www.tecmint.com/linux-network-configuration-and-troubleshooting-commands/)
Next article:
[How to Setup MySQL Replication in RHEL, Rocky and AlmaLinux](https://www.tecmint.com/setup-mysql-replication-rhel-rocky-almalinux/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#respond)** or
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
### 23 Comments
[Leave a Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/62d3b6ee530bcbdf3cba4983bc151e406c1e9a9c0194050a840061ef0391f97d?s=50&d=blank&r=g)
Pavan
[ August 26, 2021 at 11:36 am  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-1574983)
Hi Ravi,
I am doing load testing Linux servers (need to write CPU, Memory, Disk performance metrics to file for 1-hour load test duration) which command I have to write to get the metrics to write into a csv file
Thanks,
Pavan
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-1574983)
  2. ![](https://secure.gravatar.com/avatar/56b43b384d95d7b935972b392f762a5fb088287d4972000ff2049bf0d7afb15f?s=50&d=blank&r=g)
dragonmouth
[ December 14, 2019 at 8:41 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-1306126)
“Install Sysstat in Linux” – The directions given are for Red Hat-based distros, NOT for all Linux distros.
In Example 6, lower case ‘**k** ‘ and ‘**m** ‘ will display statistics in decimal kilobytes and megabytes. Upper case ‘**K** ‘ and ‘**M** ‘ will display statistics in hex kilobytes and megabytes. Option `-S` switches between the two formats. The write up does not make that point clear.
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-1306126)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ December 16, 2019 at 1:55 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-1306767)
@Dragonmouth,
Thanks for notifying, I have updated the article and included instructions for other Linux distributions as well with a correct explanation about point 6 as pointed by you…
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-1306767)
  3. ![](https://secure.gravatar.com/avatar/a51aa4f5964c925a0447a655f4e30bb7e4cdcdcd0102638e66f83c61e62d36f3?s=50&d=blank&r=g)
Ravikumar Wagh
[ July 3, 2016 at 6:36 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-797131)
Hello,
How to find out which disk is failed.
Thanks
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-797131)
  4. ![](https://secure.gravatar.com/avatar/293d3d0a6b263c2e99d0888c71995483299dc81ba3b383a4638861817fe405b4?s=50&d=blank&r=g)
Ravi
[ May 3, 2016 at 5:22 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-775969)
How to check CPU utilization Linux Kernel Module wise??
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-775969)
  5. ![](https://secure.gravatar.com/avatar/feaefa44a8a430e4e99968ac183f02b7ddb899b70425df686c124bc5b35e1b20?s=50&d=blank&r=g)
Nerizi
[ December 6, 2015 at 3:04 am  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-719839)
Hello friend, I also wanted to point out that in debian Linux (Ubuntu here) that the vmstat -t parameter does not work. Thank you
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-719839)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ December 7, 2015 at 11:28 am  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-720627)
@Nerizi,
Thanks for your findings, is there any alternative command for same **vmstat -t** in Debian/Ubuntu?
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-720627)
  6. ![](https://secure.gravatar.com/avatar/feaefa44a8a430e4e99968ac183f02b7ddb899b70425df686c124bc5b35e1b20?s=50&d=blank&r=g)
Nerizi
[ December 6, 2015 at 2:33 am  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-719827)
Is there a way to display only the following parameters every 5 seconds:
the current time, CPU utilization, current memory utilization, current disk space utilization, and currently logged in users at the same? Thanks!
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-719827)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ December 7, 2015 at 11:39 am  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-720639)
@Nerizi,
You can use following command to monitor current time, logged in users, load average.
```
# watch -n 5 uptime

```

For CPU and Disk utilization you can use our following shell script that will monitor your entire system..
<https://www.tecmint.com/linux-server-health-monitoring-script/>
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-720639)
  7. ![](https://secure.gravatar.com/avatar/13f86b3a89c00b03341687a72363a72b63d2a6096158f9f79d62f50975a66284?s=50&d=blank&r=g)
vijay
[ April 11, 2015 at 4:17 am  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-539683)
How to get historical data of disk I/O using “iostat” command which is possible in “sar” command.
Thanks
Vijay
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-539683)
  8. ![](https://secure.gravatar.com/avatar/b0fc543c2feb25aaff8d0314712b867986fdccef4dc4be162924b09743f6925b?s=50&d=blank&r=g)
Raghu
[ September 20, 2014 at 10:30 am  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-278978)
what does iostat -k 10 means, and please any body let me know
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-278978)
     * ![](https://secure.gravatar.com/avatar/759a8105b86188061402593b2b7bd0af224dc7773ccfde68f55bc2426baa1f0c?s=50&d=blank&r=g)
mangeshkumar
[ October 29, 2014 at 12:55 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-351698)
show iostat statistical info every 10 sec in Kilo Bytes
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-351698)
  9. ![](https://secure.gravatar.com/avatar/aaa9cb98b1aebd28ae629159365287cd53de7c1e16cb9ba27ddfbbd50dfd4a5d?s=50&d=blank&r=g)
Markus Aurelius
[ July 27, 2014 at 11:24 am  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-225130)
You wrote :
Free – Amount of free/idle memory spaces.
But can you tell me what exactly you mean by “Amount”?
Is it COUNT OF TOTAL FREE PAGE BLOCKS (In most case 1 Page Block = 4096 Bits)
or measured in MBytes or Mbits Or KByes or Kbits ??
Please clarify?
How would your calculate free memory in Mega Bits?
Replay Must.
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-225130)
  10. ![](https://secure.gravatar.com/avatar/c2093f9a1aad64e1cc6f345969a9337a63c5bc1cf6ef46af72a3bc32b1241e70?s=50&d=blank&r=g)
Amar Tiwari
[ July 9, 2014 at 5:02 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-210733)
Hello Sir,
I want to know that how can we know bottelneck by looking these output. Please tell me according to CPU, Memory and HDD.
Thanks for reply.
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-210733)
  11. ![](https://secure.gravatar.com/avatar/18bf44f6ff33cf15234521d202830722811570274027cfd61f211777f916df87?s=50&d=blank&r=g)
Krishna
[ April 9, 2014 at 2:23 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-146937)
Just to mention, vmstat is not from package sysstat, it is from procps
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-146937)
  12. ![](https://secure.gravatar.com/avatar/f88e2637c8e680dcb58368c0bdbc1c1e0ea34ab341ae58558bddb3fd134dc916?s=50&d=blank&r=g)
Pavan
[ February 26, 2014 at 4:13 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-126942)
Can we show only vmstat cpu? If so, how?
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-126942)
  13. ![](https://secure.gravatar.com/avatar/aaa9cb98b1aebd28ae629159365287cd53de7c1e16cb9ba27ddfbbd50dfd4a5d?s=50&d=blank&r=g)
Mark
[ August 18, 2013 at 6:15 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-34457)
I have a question.
I wanted to print vmstat with timestamp on LinuxMint 13 with bash shell but seems your
command
vmstat -t
does not works. It says there is no such argument as -t.
Is there other command for vmstat on OS like Linux Mint/Ubuntu which i can use to print vmstat with Timestamp.
I know it works for AIX but not for LM/Ubuntu. :S
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-34457)
  14. ![](https://secure.gravatar.com/avatar/de1e5280b5340ed68e3579e8b948ff85b050c7b1cad2d0222f7da02363744121?s=50&d=blank&r=g)
quydo
[ July 3, 2013 at 1:46 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-30077)
@YM:
iostat -d 5 | tee -a monitor.txt
Log will appear in screen and save to monitor.txt simultaneously :D
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-30077)
  15. ![](https://secure.gravatar.com/avatar/e1f6a76120b194883d29025462bcb2b8fa153f1dc5081e492caccbff88524514?s=50&d=blank&r=g)
YM
[ June 28, 2013 at 3:59 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-29860)
Thank you.
Was able to write io logs, but when tried the same, i get “netstat: extra arguments”, but when tried netstat -a, logs were written into a file.
Please advice me on how to overcome this?
Thanks in advance.
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-29860)
  16. ![](https://secure.gravatar.com/avatar/e1f6a76120b194883d29025462bcb2b8fa153f1dc5081e492caccbff88524514?s=50&d=blank&r=g)
YM
[ June 25, 2013 at 4:54 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-29729)
i need to monitor iostat and netstat for the app server, i need to monitor it for a particular time period with a time interval of 5 sec and write these logs to a particular file. am not sure of how do i do that. please gice suggestions.
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-29729)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 25, 2013 at 5:58 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-29730)
Do that this way, The below command append output to file “monitor.txt” every 5 seconds.
```
# iostat -d 5 >> monitor.txt

```

Same way do it for netstat.
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-29730)
  17. ![](https://secure.gravatar.com/avatar/50ae8698dd665ad0e644158e2c48774aea1198f991b743f77c066fe5b3f42bf4?s=50&d=blank&r=g)
asd
[ April 23, 2013 at 4:08 pm  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-26659)
you made a mistake
si – Swapped in every second from disk in Kilo Bytes.
si – Swapped out every second to disk in Kilo Bytes.
(i think you meant so second time)
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-26659)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 24, 2013 at 11:50 am  ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-26731)
Thanks. its corrected now..
[Reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#comment-26731)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/#respond)
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
[Linux Fun – How to Create ASCII Text Banners in Terminal](https://www.tecmint.com/create-ascii-text-banners-in-linux-terminal/)
[How to Force User to Change Password at Next Login in Linux](https://www.tecmint.com/force-user-to-change-password-next-login-in-linux/)
[6 Best CLI Tools to Search Plain-Text Data Using Regular Expressions](https://www.tecmint.com/command-line-tools-to-search-strings-or-patterns-in-files/)
[How to Use Wget Command in Linux with Examples](https://www.tecmint.com/10-wget-command-examples-in-linux/)
[13 Practical Examples of Using the Gzip Command in Linux](https://www.tecmint.com/gzip-command-in-linux/)
[How to Automatically Restart a Service After Failure on SysVinit and Upstart](https://www.tecmint.com/automatically-restart-services-on-non-systemd-linux/)
## Linux Server Monitoring Tools
[How to Monitor Docker Containers with Zabbix Monitoring Tool](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/)
[How to Configure Zabbix to Send Email Alerts to Gmail Account – Part 2](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/)
[How to Install Cacti (Network Monitoring) Tool on RHEL Systems](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/)
[6 Key Performance Metrics to Monitor in Linux Servers – Part 1](https://www.tecmint.com/monitor-linux-cpu-utilization/)
[screenFetch – An Ultimate System Information Generator for Linux](https://www.tecmint.com/screenfetch-system-information-generator-for-linux/)
[Smem – Reports Memory Consumption Per-Process and Per-User in Linux](https://www.tecmint.com/smem-linux-memory-usage-per-process-per-user/)
## Learn Linux Tricks & Tips
[Mhddfs – Combine Several Smaller Partition into One Large Virtual Storage](https://www.tecmint.com/combine-partitions-into-one-in-linux-using-mhddfs/)
[Understanding Shell Commands Easily Using “Explain Shell” Script in Linux](https://www.tecmint.com/explain-shell-commands-in-the-linux-shell/)
[How to Monitor Progress of (Copy/Backup/Compress) Data using ‘pv’ Command](https://www.tecmint.com/monitor-copy-backup-tar-progress-in-linux-using-pv-command/)
[4 Ways to Send Email Attachment from Linux Command Line](https://www.tecmint.com/send-email-attachment-from-linux-commandline/)
[How to Find Out List of All Open Ports in Linux](https://www.tecmint.com/find-open-ports-in-linux/)
[8 Parted Commands to Manage Disk Partitions in Linux](https://www.tecmint.com/parted-command-create-linux-partitions/)
## Best Linux Tools
[10 Best Flowchart and Diagramming Software for Linux](https://www.tecmint.com/best-flowchart-and-diagramming-software-for-linux/)
[10 Best Linux File and Disk Encryption Tools (2024)](https://www.tecmint.com/file-and-disk-encryption-tools-for-linux/)
[18 Must-Try Web Browsers for Linux Users in 2024](https://www.tecmint.com/linux-web-browsers/)
[5 Best PDF to Word Converters for Linux](https://www.tecmint.com/pdf-to-word-converters/)
[8 Best Mail Transfer Agents (MTA’s) for Linux](https://www.tecmint.com/best-mail-transfer-agents-mta-for-linux/)
[6 Best Modern Linux ‘init’ Systems (1992-2025)](https://www.tecmint.com/best-linux-init-systems/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/ "Scroll back to top")
Search for:
