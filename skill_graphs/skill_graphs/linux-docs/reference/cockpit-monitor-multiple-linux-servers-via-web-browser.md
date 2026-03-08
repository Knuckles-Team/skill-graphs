[Skip to content](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/sysstat-commands-to-monitor-linux/)
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
  * [Pro Courses](https://www.tecmint.com/sysstat-commands-to-monitor-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/sysstat-commands-to-monitor-linux/)
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
  * [Pro Courses](https://www.tecmint.com/sysstat-commands-to-monitor-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/sysstat-commands-to-monitor-linux/)
# 20 Useful Commands of ‘Sysstat’ Utilities (mpstat, pidstat, iostat and sar) for Linux Performance Monitoring
[Kuldeep Sharma](https://www.tecmint.com/author/kuldeepsharma47/ "View all posts by Kuldeep Sharma")Last Updated: February 9, 2018 Read Time: 9 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [7 Comments](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comments)
In our last article, we have learned about installing and upgrading the **sysstat** package and understanding briefly about the utilities which comes with the package.
  1. [Sysstat – Performance and Usage Activity Monitoring Tool For Linux](https://www.tecmint.com/install-sysstat-in-linux/)

![sysstat commands for linux monitoring](https://www.tecmint.com/wp-content/uploads/2014/09/sysstat-commands.png)20 Sysstat Commands for Linux Monitoring
Today, we are going to work with some interesting practical examples of **mpstat** , **pidstat** , **iostat** and **sar** utilities, which can help us to identify the issues. We have different options to use these utilities, I mean you can fire the commands manually with different options for different kind of work or you can create your customized scripts according to your requirements. You know Sysadmins are always bit Lazy, and always tried to find out the easy way to do the things with minimum efforts.
### mpstat – Processors Statistics
**1.** Using mpstat command without any option, will display the Global Average Activities by All CPUs.
```
**tecmint@tecmint** **~ $** mpstat

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

12:23:57  IST  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
12:23:57  IST  all   37.35    0.01    4.72    2.96    0.00    0.07    0.00    0.00    0.00   54.88

```

**2.** Using mpstat with option ‘**-P** ‘ (Indicate Processor Number) and ‘ALL’, will display statistics about all CPUs one by one starting from 0. 0 will the first one.
```
**tecmint@tecmint** **~ $** mpstat -P ALL

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

12:29:26  IST  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
12:29:26  IST  all   37.33    0.01    4.57    2.58    0.00    0.07    0.00    0.00    0.00   55.44
12:29:26  IST    0   37.90    0.01    4.96    2.62    0.00    0.03    0.00    0.00    0.00   54.48
12:29:26  IST    1   36.75    0.01    4.19    2.54    0.00    0.11    0.00    0.00    0.00   56.40

```

**3.** To display the statistics for **N** number of iterations after n seconds interval with average of each cpu use the following command.
```
**tecmint@tecmint** **~ $** mpstat -P ALL 2 5

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

12:36:21  IST  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
12:36:23  IST  all   53.38    0.00    2.26    0.00    0.00    0.00    0.00    0.00    0.00   44.36
12:36:23  IST    0   46.23    0.00    1.51    0.00    0.00    0.00    0.00    0.00    0.00   52.26
12:36:23  IST    1   60.80    0.00    3.02    0.00    0.00    0.00    0.00    0.00    0.00   36.18

12:36:23  IST  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
12:36:25  IST  all   34.18    0.00    2.30    0.00    0.00    0.00    0.00    0.00    0.00   63.52
12:36:25  IST    0   31.63    0.00    1.53    0.00    0.00    0.00    0.00    0.00    0.00   66.84
12:36:25  IST    1   36.73    0.00    2.55    0.00    0.00    0.00    0.00    0.00    0.00   60.71

12:36:25  IST  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
12:36:27  IST  all   33.42    0.00    5.06    0.25    0.00    0.25    0.00    0.00    0.00   61.01
12:36:27  IST    0   34.34    0.00    4.04    0.00    0.00    0.00    0.00    0.00    0.00   61.62
12:36:27  IST    1   32.82    0.00    6.15    0.51    0.00    0.00    0.00    0.00    0.00   60.51

```

**4.** The option ‘**I** ‘ will print total number of interrupt statistics about per processor.
```
**tecmint@tecmint** **~ $** mpstat -I

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

12:39:56  IST  CPU    intr/s
12:39:56  IST  all    651.04

12:39:56  IST  CPU        0/s        1/s        6/s        8/s        9/s       12/s       16/s       17/s       20/s       21/s       22/s       23/s       45/s       46/s       47/s      NMI/s      LOC/s      SPU/s      PMI/s      IWI/s      RTR/s      RES/s      CAL/s      TLB/s      TRM/s      THR/s      MCE/s      MCP/s      ERR/s      MIS/s
12:39:56  IST    0      76.27       1.73       0.00       0.00       0.42       0.33       0.00       0.06      11.46       0.00       0.00       0.01       7.62       1.87       0.05       0.33     182.26       0.00       0.33       3.03       0.00      22.66       0.16       5.14       0.00       0.00       0.00       0.00       0.00       0.00
12:39:56  IST    1      70.88       1.44       0.00       0.00       0.41       0.33       0.00      27.91      10.33       0.00       0.00       0.01       7.27       1.79       0.05       0.32     184.11       0.00       0.32       5.17       0.00      22.09       0.13       4.73       0.00       0.00       0.00       0.00       0.00       0.00

12:39:56  IST  CPU       HI/s    TIMER/s   NET_TX/s   NET_RX/s    BLOCK/s BLOCK_IOPOLL/s  TASKLET/s    SCHED/s  HRTIMER/s      RCU/s
12:39:56  IST    0       0.00     116.49       0.05       0.27       7.33       0.00       1.22      10.44       0.13      37.47
12:39:56  IST    1       0.00     111.65       0.05       0.41       7.07       0.00      56.36       9.97       0.13      41.38

```

**5.** Get all the above information in one command i.e. equivalent to “**-u -I ALL -p ALL** “.
```
**tecmint@tecmint** **~ $** mpstat -A

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

12:41:39  IST  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
12:41:39  IST  all   38.70    0.01    4.47    2.01    0.00    0.06    0.00    0.00    0.00   54.76
12:41:39  IST    0   39.15    0.01    4.82    2.05    0.00    0.02    0.00    0.00    0.00   53.95
12:41:39  IST    1   38.24    0.01    4.12    1.98    0.00    0.09    0.00    0.00    0.00   55.57

12:41:39  IST  CPU    intr/s
12:41:39  IST  all    651.73
12:41:39  IST    0    173.16
12:41:39  IST    1    225.89

12:41:39  IST  CPU        0/s        1/s        6/s        8/s        9/s       12/s       16/s       17/s       20/s       21/s       22/s       23/s       45/s       46/s       47/s      NMI/s      LOC/s      SPU/s      PMI/s      IWI/s      RTR/s      RES/s      CAL/s      TLB/s      TRM/s      THR/s      MCE/s      MCP/s      ERR/s      MIS/s
12:41:39  IST    0      76.04       1.77       0.00       0.00       0.41       0.36       0.00       0.06      11.60       0.00       0.00       0.01       7.42       1.83       0.05       0.34     182.89       0.00       0.34       2.97       0.00      22.69       0.16       5.22       0.00       0.00       0.00       0.00       0.00       0.00
12:41:39  IST    1      70.70       1.48       0.00       0.00       0.40       0.36       0.00      27.47      10.46       0.00       0.00       0.01       7.08       1.75       0.05       0.32     184.83       0.00       0.32       5.10       0.00      22.19       0.13       4.91       0.00       0.00       0.00       0.00       0.00       0.00

12:41:39  IST  CPU       HI/s    TIMER/s   NET_TX/s   NET_RX/s    BLOCK/s BLOCK_IOPOLL/s  TASKLET/s    SCHED/s  HRTIMER/s      RCU/s
12:41:39  IST    0       0.00     116.96       0.05       0.26       7.12       0.00       1.24      10.42       0.12      36.99
12:41:39  IST    1       0.00     112.25       0.05       0.40       6.88       0.00      55.05       9.93       0.13      41.20

```

### pidstat – Process and Kernel Threads Statistics
This is used for process monitoring and current threads, which are being managed by kernel. pidstat can also check the status about child processes and threads.
###### Syntax
```
# pidstat <OPTIONS> [INTERVAL] [COUNT]

```

**6.** Using pidstat command without any argument, will display all active tasks.
```
**tecmint@tecmint** **~ $** pidstat

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

12:47:24  IST   UID       PID    %usr %system  %guest    %CPU   CPU  Command
12:47:24  IST     0         1    0.01    0.12    0.00    0.13     1  init
12:47:24  IST     0         3    0.00    0.01    0.00    0.01     0  ksoftirqd/0
12:47:24  IST     0         9    0.00    0.04    0.00    0.04     0  rcu_sched
12:47:24  IST     0        10    0.00    0.00    0.00    0.00     0  watchdog/0
12:47:24  IST     0        11    0.00    0.00    0.00    0.00     1  watchdog/1
12:47:24  IST     0        12    0.00    0.00    0.00    0.00     1  migration/1
12:47:24  IST     0        13    0.00    0.01    0.00    0.01     1  ksoftirqd/1
12:47:24  IST     0        23    0.00    0.00    0.00    0.00     0  kworker/u9:0
12:47:24  IST     0        29    0.00    0.61    0.00    0.61     0  kworker/0:1
12:47:24  IST     0        30    0.00    0.06    0.00    0.06     1  kworker/1:1
12:47:24  IST     0       224    0.00    0.01    0.00    0.01     1  jbd2/sda1-8
12:47:24  IST     0       360    0.00    0.00    0.00    0.00     1  upstart-udev-br
12:47:24  IST     0       365    0.01    0.00    0.00    0.01     0  systemd-udevd
12:47:24  IST     0       476    0.00    0.00    0.00    0.00     0  kworker/u9:1

```

**7.** To print all active and non-active tasks use the option ‘**-p** ‘ (processes).
```
**tecmint@tecmint** **~ $** pidstat -p ALL

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

12:51:55  IST   UID       PID    %usr %system  %guest    %CPU   CPU  Command
12:51:55  IST     0         1    0.01    0.11    0.00    0.12     1  init
12:51:55  IST     0         2    0.00    0.00    0.00    0.00     0  kthreadd
12:51:55  IST     0         3    0.00    0.01    0.00    0.01     0  ksoftirqd/0
12:51:55  IST     0         5    0.00    0.00    0.00    0.00     0  kworker/0:0H
12:51:55  IST     0         7    0.00    0.00    0.00    0.00     0  migration/0
12:51:55  IST     0         8    0.00    0.00    0.00    0.00     0  rcu_bh
12:51:55  IST     0         9    0.00    0.04    0.00    0.04     1  rcu_sched
12:51:55  IST     0        10    0.00    0.00    0.00    0.00     0  watchdog/0
12:51:55  IST     0        11    0.00    0.00    0.00    0.00     1  watchdog/1
12:51:55  IST     0        12    0.00    0.00    0.00    0.00     1  migration/1
12:51:55  IST     0        13    0.00    0.01    0.00    0.01     1  ksoftirqd/1
12:51:55  IST     0        15    0.00    0.00    0.00    0.00     1  kworker/1:0H
12:51:55  IST     0        16    0.00    0.00    0.00    0.00     1  khelper
12:51:55  IST     0        17    0.00    0.00    0.00    0.00     0  kdevtmpfs
12:51:55  IST     0        18    0.00    0.00    0.00    0.00     0  netns
12:51:55  IST     0        19    0.00    0.00    0.00    0.00     0  writeback
12:51:55  IST     0        20    0.00    0.00    0.00    0.00     1  kintegrityd

```

**8.** Using pidstat command with ‘**-d 2** ‘ option, we can get I/O statistics and **2** is interval in seconds to get refreshed statistics. This option can be handy in situation, where your system is undergoing heavy I/O and you want to get clues about the processes consuming high resources.
```
**tecmint@tecmint** **~ $** pidstat -d 2

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

03:26:53  EDT       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command

03:26:55  EDT       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command
03:26:57  EDT       574      0.00    148.00      2.00  miniserv.pl

03:27:01  EDT       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command
03:27:03  EDT         1      0.00      8.00      2.00  init
03:27:03  EDT       450      0.00      2.00      0.00  rsyslogd
03:27:03  EDT       534    138.00     10.00      4.00  crond
03:27:03  EDT     25100      0.00      6.00      0.00  sendmail
03:27:03  EDT     30829      0.00      6.00      0.00  java


```

**9.** To know the cpu statistics along with all threads about the process id **4164** at interval of **2** sec for **3** times use the following command with option ‘**-t** ‘ (display statistics of selected process).
```
**tecmint@tecmint** **~ $** pidstat -t -p 4164 2 3

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

01:09:06  IST   UID      TGID       TID    %usr %system  %guest    %CPU   CPU  Command
01:09:08  IST  1000      4164         -   22.00    1.00    0.00   23.00     1  firefox
01:09:08  IST  1000         -      4164   20.00    0.50    0.00   20.50     1  |__firefox
01:09:08  IST  1000         -      4171    0.00    0.00    0.00    0.00     0  |__Gecko_IOThread
01:09:08  IST  1000         -      4172    0.00    0.00    0.00    0.00     0  |__Socket
01:09:08  IST  1000         -      4173    0.00    0.00    0.00    0.00     0  |__JS
01:09:08  IST  1000         -      4174    0.00    0.00    0.00    0.00     0  |__JS
01:09:08  IST  1000         -      4175    0.00    0.00    0.00    0.00     0  |__Hang
01:09:08  IST  1000         -      4176    0.00    0.00    0.00    0.00     1  |__gdbus
01:09:08  IST  1000         -      4177    0.00    0.00    0.00    0.00     1  |__gmain

```

**10.** Use the ‘**-rh** ‘ option, to know the about memory utilization of processes which are frequently varying their utilization in **2** second interval.
```
**tecmint@tecmint** **~ $** pidstat -rh 2 3

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

#      Time   UID       PID  minflt/s  majflt/s     VSZ    RSS   %MEM  Command
 1409816695  1000      3958   3378.22      0.00  707420 215972   5.32  cinnamon
 1409816695  1000      4164    406.93      0.00 1252024 461404  11.36  firefox
 1409816695  1000      6676    168.81      0.00    4436    984   0.02  pidstat

#      Time   UID       PID  minflt/s  majflt/s     VSZ    RSS   %MEM  Command
 1409816697     0      1601    644.00      0.00  506728 316788   7.80  Xorg
 1409816697  1000      3958   3412.00      0.00  707420 215972   5.32  cinnamon
 1409816697  1000      4164   2667.00      0.00 1259576 471724  11.62  firefox
 1409816697  1000      6676    172.50      0.00    4436   1020   0.03  pidstat

#      Time   UID       PID  minflt/s  majflt/s     VSZ    RSS   %MEM  Command
 1409816699     0      1601    644.00      0.00  506728 316788   7.80  Xorg
 1409816699  1000      3958   4094.00      0.00  710148 218700   5.39  cinnamon
 1409816699  1000      4164    599.00      0.00 1261944 476664  11.74  firefox
 1409816699  1000      6676    168.00      0.00    4436   1020   0.03  pidstat

```

**11.** To print all the process of containing string “**VB** “, use ‘**-t** ‘ option to see threads as well.
```
**tecmint@tecmint** **~ $** pidstat -G VB

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

01:09:06  IST   UID      PID      %usr 	%system  %guest    %CPU   CPU  	Command
01:09:08  IST  1000    1492     22.00     1.00    	 0.00   	 23.00     1  		VBoxService
01:09:08  IST  1000    1902     4164      20.00    	 0.50    	 0.00   	20.50     	VBoxClient
01:09:08  IST  1000    1922     4171      0.00    	 0.00    	 0.00    	0.00     	VBoxClient

```
```
**tecmint@tecmint** **~ $** pidstat  -t -G VB
Linux 2.6.32-431.el6.i686 (tecmint) 09/04/2014 _i686_	(2 CPU)

03:19:52 PM   UID      TGID       TID    %usr %system  %guest    %CPU   CPU  Command
03:19:52 PM     0      1479         -    0.01    0.12    0.00    0.13     1  VBoxService
03:19:52 PM     0         -      1482    0.00    0.00    0.00    0.00     0  |__timesync
03:19:52 PM     0         -      1483    0.01    0.06    0.00    0.06     0  |__vminfo
03:19:52 PM     0         -      1485    0.00    0.01    0.00    0.01     1  |__memballoon
03:19:52 PM     0         -      1486    0.00    0.01    0.00    0.01     1  |__vmstats
03:19:52 PM     0         -      1487    0.00    0.05    0.00    0.05     0  |__automount
03:19:52 PM     0      1913         -    0.00    0.00    0.00    0.00     0  VBoxClient
03:19:52 PM     0         -      1913    0.00    0.00    0.00    0.00     0  |__VBoxClient
03:19:52 PM     0         -      1942    0.00    0.00    0.00    0.00     0  |__SHCLIP
03:19:52 PM     0      1933         -    0.04    0.89    0.00    0.93     0  VBoxClient
03:19:52 PM     0         -      1936    0.04    0.89    0.00    0.93     1  |__X11-NOTIFY

```

**12.** To get realtime priority and scheduling information use option ‘**-R** ‘ .
```
**tecmint@tecmint** **~ $** pidstat -R

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

01:09:06  IST   UID      PID	 prio      policy 	Command
01:09:08  IST  1000    3     	 99	       FIFO		migration/0
01:09:08  IST  1000    5     	 99          FIFO	migration/0
01:09:08  IST  1000    6    	 99          FIFO	watchdog/0

```

Here, I am not going to cover about Iostat utility, as we are already covered it. Please have a look on “[Linux Performance Monitoring with Vmstat and Iostat](https://www.tecmint.com/linux-performance-monitoring-with-vmstat-and-iostat-commands/)” to get all details about iostat.
### sar – System Activity Reporter
Using “**sar** ” command, we can get the reports about whole system’s performance. This can help us to locate the system bottleneck and provide the help to find out the solutions to these annoying performance issues.
The Linux Kernel maintains some counter internally, which keeps track of all requests, their completion time and I/O block counts etc. From all these information, sar calculates rates and ratio of these request to find out about bottleneck areas.
The main thing about the sar is that, it reports all activities over a period if time. So, make sure that sar collect data on appropriate time (not on Lunch time or on weekend.:)
**13.** Following is a basic command to invoke sar. It will create one file named “**sarfile** ” in your current directory. The options ‘**-u** ‘ is for CPU details and will collect **5** reports at an interval of **2** seconds.
```
**tecmint@tecmint** **~ $** sar -u -o sarfile 2 5

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

01:42:28  IST     CPU     %user     %nice   %system   %iowait    %steal     %idle
01:42:30  IST     all     36.52      0.00      3.02      0.00      0.00     60.45
01:42:32  IST     all     43.32      0.00      5.04      0.00      0.00     51.64
01:42:34  IST     all     56.46      0.00      4.05      0.00      0.00     39.49
01:42:36  IST     all     44.44      0.00      3.79      0.00      0.00     51.77
01:42:38  IST     all     50.75      0.00      3.75      0.00      0.00     45.50
Average:        all     46.30      0.00      3.93      0.00      0.00     49.77

```

**14.** In the above example, we have invoked sar interactively. We also have an option to invoke it non-interactively via cron using scripts **/usr/local/lib/sa1** and **/usr/local/lib/sa2** (If you have used **/usr/local** as prefix during installation time).
  1. **/usr/local/lib/sa1** is a shell script that we can use for scheduling cron which will create daily binary log file.
  2. **/usr/local/lib/sa2** is a shell script will change binary log file to human-readable form.


Use the following Cron entries for making this non-interactive:
```
# Run sa1 shell script every 10 minutes for collecting data
*/2 * * * * /usr/local/lib/sa/sa1 2 10

# Generate a daily report in human readable format at 23:53
53 23 * * * /usr/local/lib/sa/sa2 -A

```

At the back-end sa1 script will call **sadc** (System Activity Data Collector) utility for fetching the data at a particular interval. **sa2** will call sar for changing binary log file to human readable form.
**15.** Check run queue length, total number of processes and load average using ‘**-q** ‘ option.
```
**tecmint@tecmint** **~ $** sar -q 2 5

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

02:00:44  IST   runq-sz  plist-sz   ldavg-1   ldavg-5  ldavg-15   blocked
02:00:46  IST         1       431      1.67      1.22      0.97         0
02:00:48  IST         4       431      1.70      1.23      0.97         0
02:00:50  IST         2       431      1.70      1.23      0.97         0
02:00:52  IST         2       431      1.70      1.23      0.97         0
02:00:54  IST         0       431      1.64      1.23      0.97         0
Average:            2       431      1.68      1.23      0.97         0

```

**16.** Check statistics about the mounted file systems using ‘**-F** ‘.
```
**tecmint@tecmint** **~ $** sar -F 2 4

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

02:02:31  IST  MBfsfree  MBfsused   %fsused  %ufsused     Ifree     Iused    %Iused FILESYSTEM
02:02:33  IST      1001       449     30.95    1213790475088.85  18919505    364463      1.89 /dev/sda1

02:02:33  IST  MBfsfree  MBfsused   %fsused  %ufsused     Ifree     Iused    %Iused FILESYSTEM
02:02:35  IST      1001       449     30.95    1213790475088.85  18919505    364463      1.89 /dev/sda1

02:02:35  IST  MBfsfree  MBfsused   %fsused  %ufsused     Ifree     Iused    %Iused FILESYSTEM
02:02:37  IST      1001       449     30.95    1213790475088.85  18919505    364463      1.89 /dev/sda1

02:02:37  IST  MBfsfree  MBfsused   %fsused  %ufsused     Ifree     Iused    %Iused FILESYSTEM
02:02:39  IST      1001       449     30.95    1213790475088.86  18919505    364463      1.89 /dev/sda1

Summary      MBfsfree  MBfsused   %fsused  %ufsused     Ifree     Iused    %Iused FILESYSTEM
Summary          1001       449     30.95    1213790475088.86  18919505    364463      1.89 /dev/sda1

```

**17.** View network statistics using ‘**-n DEV** ‘.
```
**tecmint@tecmint** **~ $** sar -n DEV 1 3 | egrep -v lo

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

02:11:59  IST     IFACE   rxpck/s   txpck/s    rxkB/s    txkB/s   rxcmp/s   txcmp/s  rxmcst/s
02:12:00  IST     wlan0      8.00     10.00      1.23      0.92      0.00      0.00      0.00
02:12:00  IST    vmnet8      0.00      0.00      0.00      0.00      0.00      0.00      0.00
02:12:00  IST      eth0      0.00      0.00      0.00      0.00      0.00      0.00      0.00
02:12:00  IST    vmnet1      0.00      0.00      0.00      0.00      0.00      0.00      0.00

```

**18.** View block device statistics like iostat using ‘**-d** ‘.
```
**tecmint@tecmint** **~ $** sar -d 1 3

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

02:13:17  IST       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
02:13:18  IST    dev8-0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

02:13:18  IST       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
02:13:19  IST    dev8-0      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00

02:13:19  IST       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
02:13:20  IST    dev8-0      7.00     32.00     80.00     16.00      0.11     15.43     15.43     10.80

```

**19.** To print memory statistics use ‘**-r** ‘ option.
```
**tecmint@tecmint** **~ $** sar -r 1 3

Linux 3.11.0-23-generic (tecmint.com) 	Thursday 04 September 2014 	_i686_	(2 CPU)

02:14:29  IST kbmemfree kbmemused  %memused kbbuffers  kbcached  kbcommit   %commit  kbactive   kbinact   kbdirty
02:14:30  IST   1465660   2594840     63.90    133052   1549644   3710800     45.35   1133148   1359792       392
02:14:31  IST   1472724   2587776     63.73    133060   1549792   3715504     45.40   1125816   1360000       836
02:14:32  IST   1469112   2591388     63.82    133060   1550036   3705288     45.28   1130252   1360168       804
Average:      1469165   2591335     63.82    133057   1549824   3710531     45.34   1129739   1359987       677

```

**20.** Using ‘**safd -d** ‘, we can extract data in format which can be processed using databases.
```
**tecmint@tecmint** **~ $** safd -d /var/log/sa/sa20140903 -- -n DEV | grep -v lo

 # hostname;interval;timestamp;IFACE;rxpck/s;txpck/s;rxkB/s;txkB/s;rxcmp/s;txcmp/s;rxmcst/s;%ifutil
tecmint;2;2014-09-03 07:53:29 UTC;eth0;1.50;0.00;0.13;0.00;0.00;0.00;0.00;0.00
tecmint;2;2014-09-03 07:53:31 UTC;eth0;2.00;0.00;0.18;0.00;0.00;0.00;0.00;0.00
tecmint;2;2014-09-03 07:53:33 UTC;eth0;1.00;0.00;0.09;0.00;0.00;0.00;0.00;0.00
tecmint;2;2014-09-03 07:53:35 UTC;eth0;2.00;0.00;0.18;0.00;0.00;0.00;0.00;0.00
tecmint;14778;2014-09-03 11:59:54 UTC;eth0;1.78;1.17;1.10;0.18;0.00;0.00;0.00;0.00
tecmint;2;2014-09-03 11:59:56 UTC;eth0;3.50;3.00;0.60;0.77;0.00;0.00;0.00;0.00
tecmint;2;2014-09-03 11:59:58 UTC;eth0;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00
tecmint;2;2014-09-03 12:00:00 UTC;eth0;0.00;0.00;0.00;0.00;0.00;0.00;0.00;0.00
tecmint;2;2014-09-03 12:00:02 UTC;eth0;0.50;0.50;0.48;0.03;0.00;0.00;0.00;0.00
tecmint;2;2014-09-03 12:00:04 UTC;eth0;2.50;3.50;0.21;2.05;0.00;0.00;0.00;0.00
tecmint;2;2014-09-03 12:00:06 UTC;eth0;1.49;1.00;0.62;0.06;0.00;0.00;0.00;0.00
tecmint;2;2014-09-03 12:00:08 UTC;eth0;0.50;0.00;0.03;0.00;0.00;0.00;0.00;0.00
tecmint;2;2014-09-03 12:00:10 UTC;eth0;0.50;0.50;0.03;0.04;0.00;0.00;0.00;0.00
tecmint;2;2014-09-03 12:00:12 UTC;eth0;1.00;0.50;0.12;0.04;0.00;0.00;0.00;0.00

```

You can also save this to a csv and then can draw chart for presentation kind of stuff as below.
![safd command](https://www.tecmint.com/wp-content/uploads/2014/09/sar-graph-620x172.png)Network Graph
That’s it for now, you can refer man pages for more information about each option and don’t forget to tell about article with your valuable comments.
Tags [sysstat](https://www.tecmint.com/tag/sysstat/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[The Story Behind ‘init’ and ‘systemd’: Why ‘init’ Needed to be Replaced with ‘systemd’ in Linux](https://www.tecmint.com/systemd-replaces-init-in-linux/)
Next article:
[Setup Master-Slave DNS Server Using “Bind” Tools in RHEL/CentOS 6.5](https://www.tecmint.com/setup-master-slave-dns-server-in-centos/)
![Photo of author](https://secure.gravatar.com/avatar/690880adda29542c7e416f7c51e4e5efd847d4f13cb823a1880d9a2f7659df43?s=100&d=blank&r=g)
Kuldeep Sharma
Currently, Working in Middleware(Jboss/Apache Tomcat) And POSIX related technologies. Having more than 5 years of experience and love to do R&D on different open source tools/technologies.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#respond)** or
## Related Posts
[![Linux Disk I/O Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2015/04/Linux-Disk-IO-Monitoring-Tools.png)](https://www.tecmint.com/monitor-linux-disk-io-performance/ "7 Best Tools to Monitor and Debug Disk I/O Performance in Linux")
[7 Best Tools to Monitor and Debug Disk I/O Performance in Linux](https://www.tecmint.com/monitor-linux-disk-io-performance/)
[![Disk Usage Monitoring Script in Linux](https://www.tecmint.com/wp-content/uploads/2014/01/linux-disk-usage-monitoring-shell-script.webp)](https://www.tecmint.com/monitor-disk-usage-bash-script/ "A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%")
[A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%](https://www.tecmint.com/monitor-disk-usage-bash-script/)
[![Linux Performance Monitoring with Command-Line Tools](https://www.tecmint.com/wp-content/uploads/2023/08/command-line-monitoring-tools-linux.webp)](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/ "24 Best Command Line Tools to Monitor Linux Performance")
[24 Best Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)
[![atop: System and process monitor for Linux](https://www.tecmint.com/wp-content/uploads/2025/06/atop-System-and-process-monitor-for-Linux.webp)](https://www.tecmint.com/atop-linux-performance-monitoring/ "How to Install ‘atop’ to Monitor Real-Time System Performance")
[How to Install ‘atop’ to Monitor Real-Time System Performance](https://www.tecmint.com/atop-linux-performance-monitoring/)
[![Bash Script to Monitor Linux Health Daily](https://www.tecmint.com/wp-content/uploads/2025/06/bash-script-automate-system-health-checks.webp)](https://www.tecmint.com/bash-script-automate-system-health-checks/ "How to Automate Daily Linux Health Checks with a Bash Script + Cron")
[How to Automate Daily Linux Health Checks with a Bash Script + Cron](https://www.tecmint.com/bash-script-automate-system-health-checks/)
[![Network Bandwidth Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2013/07/network-bandwidth-monitoring-tools.webp)](https://www.tecmint.com/network-bandwidth-monitoring-tools/ "5 Modern VnStat PHP Replacements for Bandwidth Monitoring")
[5 Modern VnStat PHP Replacements for Bandwidth Monitoring](https://www.tecmint.com/network-bandwidth-monitoring-tools/)
### 7 Comments
[Leave a Reply](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/abb6a1beadae18d1115a8a814023ce64837a2bac76455357cccd7a473ad5dae2?s=50&d=blank&r=g)
Sumit Kumar
[ March 21, 2019 at 2:15 pm  ](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-1115601)
Great tutorial. You could also analyze **sar** report to get charts and aggregated data. For that we can follow
[Reply](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-1115601)
  2. ![](https://secure.gravatar.com/avatar/c065ba5221ee3ca15a8a10d4310f9075b4fc1282e04e1ef04ea8e4fde78959a3?s=50&d=blank&r=g)
Mark
[ February 8, 2018 at 9:01 pm  ](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-967722)
I hesitate to comment on an old post but I did notice that on 20. Using ‘sadf’ the example for some reasons shows the cmd as ‘safd’ so initially I thought I didn’t have the package available. Otherwise very useful post.
[Reply](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-967722)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 9, 2018 at 10:48 am  ](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-967859)
@Mark,
Thanks for informing about that error, yes it was actually “**safd** ” command. Corrected in the article.
[Reply](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-967859)
  3. ![](https://secure.gravatar.com/avatar/be6a3e40739cc5c6331026be9a0668f4a45c772524c55968e4cf41e246241e6e?s=50&d=blank&r=g)
Sayyad
[ June 14, 2016 at 5:48 pm  ](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-791088)
Hi Kuldeep,
Thanks for the good info on SAR..,Not sure if this is a right platform to talk about problem with Sar version 8.1.5.
One of the issues with sar is that the “sar -A” command gives the datestamp exactly past one month in the first line of the output..
Any suggestion/help would be much appreciated..
Thanks,
-Sayyad
[Reply](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-791088)
     * ![](https://secure.gravatar.com/avatar/690880adda29542c7e416f7c51e4e5efd847d4f13cb823a1880d9a2f7659df43?s=50&d=blank&r=g)
Kuldeep
[ June 21, 2016 at 7:31 pm  ](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-793434)
Hi Sayyad,
8.1.5 seems quit old and at same time it was not stable release.
I would suggest to update the same and check results.
More Detail:
Thanks// Kuldeep
[Reply](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-793434)
  4. ![](https://secure.gravatar.com/avatar/690880adda29542c7e416f7c51e4e5efd847d4f13cb823a1880d9a2f7659df43?s=50&d=blank&r=g)
Kuldeep
[ September 5, 2014 at 5:01 pm  ](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-263287)
Thank you :) !!
You have to change “HISTORY” parameter to 30 days.
File need to modify:
/etc/sysconfig/sysstat
Paramter:
HISTORY=30
Thanks!!
[Reply](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-263287)
  5. ![](https://secure.gravatar.com/avatar/796ce49887647986f150ad3bc80eb2e07a8959bac01f0c4eed3f99dd94385923?s=50&d=blank&r=g)
guru
[ September 5, 2014 at 9:23 am  ](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-262899)
Hi Kuldeep,
Good Article.
I want sar to keep the record of last 30 days, how to do that?
[Reply](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#comment-262899)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/sysstat-commands-to-monitor-linux/#respond)
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
[4 Ways to Find Out Which Process Listening on a Particular Port](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/)
[How to Pipe Command Output to Other Commands in Linux](https://www.tecmint.com/pipe-command-output-to-other-commands/)
[How to Manage /etc with Version Control Using Etckeeper on Linux](https://www.tecmint.com/manage-etc-with-version-control-using-etckeeper/)
[8 Parted Commands to Manage Disk Partitions in Linux](https://www.tecmint.com/parted-command-create-linux-partitions/)
[How to Count Number of Files and Subdirectories inside a Given Directory](https://www.tecmint.com/count-files-and-directories-linux/)
[Dtrx – An Intelligent Archive Extraction (tar, zip, cpio, rpm, deb, rar) Tool for Linux](https://www.tecmint.com/dtrx-archive-extraction-tool-for-linux/)
## Linux Server Monitoring Tools
[How to Install Nagios Monitoring Tool on RHEL 8](https://www.tecmint.com/install-nagios-on-rhel-8/)
[How to Add Windows Host to Nagios Monitoring Server](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/)
[Limit CPU Usage of a Process in Linux with CPULimit Tool](https://www.tecmint.com/limit-cpu-usage-of-a-process-in-linux-with-cpulimit-tool/)
[How to Install Icinga2 on RHEL, Rocky and AlmaLinux](https://www.tecmint.com/install-icinga2-rhel-rocky-almalinux/)
[Suricata – A Intrusion Detection, Prevention, and Security Tool](https://www.tecmint.com/suricata-intrusion-detection-prevention-linux/)
[Monitor Server Resources with Collectd-web and Apache CGI in Linux](https://www.tecmint.com/monitor-linux-server-resources-with-collectd-web-and-apache-cgi/)
## Learn Linux Tricks & Tips
[How to Use ‘at’ Command to Schedule a Task on Given or Later Time in Linux](https://www.tecmint.com/linux-cron-alternative-at-command-to-schedule-tasks/)
[Learn How to Set Your $PATH Variables Permanently in Linux](https://www.tecmint.com/set-path-variable-linux-permanently/)
[How to View Colored Man Pages in Linux](https://www.tecmint.com/view-colored-man-pages-in-linux/)
[Learn The Basics of How Linux I/O (Input/Output) Redirection Works](https://www.tecmint.com/linux-io-input-output-redirection-operators/)
[Find Out All Live Hosts IP Addresses Connected on Network in Linux](https://www.tecmint.com/find-live-hosts-ip-addresses-on-linux-network/)
[How to Transfer Files Between Two Computers using nc and pv Commands](https://www.tecmint.com/transfer-files-between-two-linux-machines/)
## Best Linux Tools
[11 Best Open Source Note-Taking Apps for Linux](https://www.tecmint.com/note-taking-apps-linux/)
[11 Best Free and Low-Cost SSL Certificate Authorities](https://www.tecmint.com/best-ssl-certificate-authorities/)
[8 Useful GUI Email Clients for Linux Desktop](https://www.tecmint.com/linux-desktop-email-clients/)
[10 Best PuTTY Alternatives for SSH Remote Connection](https://www.tecmint.com/putty-alternatives/)
[7 Best Skype Alternatives for Linux in 2025](https://www.tecmint.com/skype-alternatives-for-linux/)
[10 Best PDF Document Viewers for Linux Systems](https://www.tecmint.com/linux-pdf-viewers-and-readers-tools/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/sysstat-commands-to-monitor-linux/ "Scroll back to top")
Search for:
