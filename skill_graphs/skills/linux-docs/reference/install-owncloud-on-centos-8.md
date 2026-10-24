[Skip to content](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/)
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
  * [Pro Courses](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/ "Linux Online Courses")
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


[](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/)
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
  * [Pro Courses](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/ "Linux Online Courses")
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


[](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/)
# How to Set Priority of a Running Process in Linux
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: April 29, 2024 Read Time: 5 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [8 Comments](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comments)
In this article, we’ll briefly explain the **kernel scheduler** (also known as the **process scheduler**), and **process priority** , which are topics beyond the scope of this guide.
Then we will dive into a little bit of [Linux process management](https://www.tecmint.com/rhcsa-exam-boot-process-and-process-management/): see how to run a program or command with modified priority and also change the priority of [running Linux processes](https://www.tecmint.com/find-linux-processes-memory-ram-cpu-usage/ "Find Top Running Processes").
**[ You might also like:[How to Monitor & Limit User Processes in Linux](https://www.tecmint.com/monitor-linux-processes-and-set-process-limits-per-user/ "Monitor & Control: Linux Processes per User") ]**
## Understanding the Linux Kernel Scheduler
A kernel scheduler is a component of the kernel responsible for selecting the most appropriate process to run next from all the processes that are ready to execute.
It manages the allocation of CPU time among these processes on the system. A process is considered runnable when it is waiting solely for CPU time and is prepared to be executed.
The scheduler forms the core of multitasking in Linux, using a priority-based scheduling algorithm to choose between the runnable processes in the system. It ranks processes based on the most deserving as well as the need for CPU time.
## Understanding Process Priority and Nice Value
The kernel stores a great deal of information about processes including process priority which is simply the scheduling priority attached to a process. Processes with a higher priority will be executed before those with a lower priority, while processes with the same priority are scheduled one after the next, repeatedly.
There are a total of **140** priorities and two distinct priority ranges implemented in Linux. The first one is a nice value (**niceness**) which ranges from `-20` (highest priority value) to `19` (lowest priority value) and the default is `0`, this is what we will uncover in this guide.
The other is the real-time priority, which ranges from **1** to **99** by default, then **100** to **139** are meant for user-space.
One important characteristic of Linux is dynamic priority-based scheduling, which allows the nice value of processes to be changed (increased or decreased) depending on your needs, as we’ll see later on.
## How to Check Nice Value of Linux Processes
To see the nice values of processes, we can use utilities such as [ps](https://www.tecmint.com/ps-command-examples-for-linux-process-monitoring/), [top](https://www.tecmint.com/12-top-command-examples-in-linux/) or [htop](https://www.tecmint.com/htop-linux-process-monitoring/).
To view processes nice value with ps command in user-defined format (here the `NI` the column shows the niceness of processes).
```
ps -eo pid,ppid,ni,comm

```
![View Linux Processes Nice Values](https://www.tecmint.com/wp-content/uploads/2017/09/View-Processes-Nice-Values.png)View Linux Processes Nice Values
Alternatively, you can use **top** or **htop** utilities to view Linux processes’ nice values as shown.
```
top
htop

```
![Check Linux Process Nice Values using Top Command](https://www.tecmint.com/wp-content/uploads/2017/09/View-Process-Nice-Values-using-top.png)Check Linux Process Nice Values using Top Command ![Check Linux Process Nice Values using Htop Command](https://www.tecmint.com/wp-content/uploads/2017/09/View-Process-Nice-Values-using-htop.png)Check Linux Process Nice Values using Htop Command
### Difference Between PR or PRI and NI
From the **top** and **htop** outputs above, you’ll notice that there is a column called `PR` and `PRI` receptively which shows the priority of a process.
This, therefore, means that:
  * `NI` – is the nice value, which is a user-space concept, while
  * `PR` or `PRI` – is the process’s actual priority, as seen by the Linux kernel.


### How To Calculate PR or PRI Values
```
Total number of priorities = 140
Real time priority range(PR or PRI):  0 to 99
User space priority range: 100 to 139

```

Nice value range (NI): -20 to 19
```
PR = 20 + NI
PR = 20 + (-20 to + 19)
PR = 20 + -20  to 20 + 19
PR = 0 to 39 which is same as 100 to 139.

```

But if you see a `rt` rather than a number as shown in the screenshot below, it basically means the process is running under real-time scheduling priority.
![Linux rt Process](https://www.tecmint.com/wp-content/uploads/2017/09/Linux-rt-example.png)Linux rt Process
## How to Run A Command with a Given Nice Value in Linux
Here, we will look at how to prioritize the [CPU usage of a program](https://www.tecmint.com/find-linux-processes-memory-ram-cpu-usage/ "Find Top Running Processes by CPU Usage") or command. If you have a very CPU-intensive program or task, but you also understand that it might take a long time to complete, you can set it a high or favorable priority using the **nice command**.
The syntax is as follows:
```
nice -n niceness-value [command args]
OR
nice -niceness-value [command args]
OR
nice --adjustment=niceness-value [command args]

```

Important:
  * If no value is provided, nice sets a priority of 10 by default.
  * A command or program run without nice defaults to a priority of zero.
  * Only root can run a command or program with increased or high priority.
  * Normal users can only run a command or program with low priority.


For example, instead of starting a program or command with the default priority, you can start it with a specific priority using the following nice command.
```
sudo nice -n 5 tar -czf backup.tar.gz ./Documents/*
OR
sudo nice --adjustment=5 tar -czf backup.tar.gz ./Documents/*

```

You can also use the third method which is a little confusing, especially for negative niceness values.
```
sudo nice -5 tar -czf backup.tar.gz  ./Documents/*

```

## Change the Scheduling Priority of a Process in Linux
As we mentioned before, Linux allows dynamic priority-based scheduling. Therefore, if a program is already running, you can change its priority with the **renice command** in this form:
```
renice -n  -12  -p 1055
renice -n -2  -u apache

```
![Change Process Priority](https://www.tecmint.com/wp-content/uploads/2017/09/Change-Process-Priority.png)Change Process Priority
From the sample **top** output below, the niceness of the **teamspe+** with PID **1055** is now `-12` and for all processes owned by user apache is `-2`.
Still using this output, you can see the formula **PR = 20 + NI** stands,
```
PR for ts3server = 20 + -12 = 8
PR for apache processes = 20 + -2 = 18

```
![Watch Processes Nice Values](https://www.tecmint.com/wp-content/uploads/2017/09/Watch-Processes-Nice-Values.png)Watch Processes Nice Values
Any changes you make with the **renice command** to a user’s processes nice values are only applicable until the next reboot. To set permanent default values, read the next section.
## How To Set Default Nice Value Of a Specific User’s Processes
You can set the default nice value of a particular user or group in the **/etc/security/limits.conf** file. Its primary function is to define the resource limits for the users logged in via PAM.
The syntax for defining a limit for a user is as follows (and the possible values of the various columns are explained in the file):
```
#<domain>   <type>  <item>  <value>

```

Now use the syntax below where hard – means enforcing hard links and soft means – enforcing the soft limits.
```
<username>  <hard|soft>  priority  <nice value>

```

Alternatively, create a file under **/etc/security/limits.d/** which overrides settings in the main file above, and these files are read in alphabetical order.
Start by creating the file **/etc/security/limits.d/tecmint-priority.conf** for user **tecmint** :
```
vi /etc/security/limits.d/tecmint-priority.conf

```

Then add this configuration to it:
```
tecmint  hard  priority  10

```

Save and close the file. From now on, any process owned by **tecmint** will have a nice value of **10** and PR of **30**.
For more information, read the man pages of **nice** and **renice** :
```
man nice
man renice

```

You might also like to read the following articles about Linux process management.
  * [How to Find and Kill Running Processes in Linux](https://www.tecmint.com/find-and-kill-running-processes-pid-in-linux/)
  * [A Guide to Kill, Pkill, and Killall Commands to Terminate a Process in Linux](https://www.tecmint.com/how-to-kill-a-process-in-linux/)
  * [How to Monitor System Usage, Outages, and Troubleshoot Linux Servers](https://www.tecmint.com/linux-system-monitoring-troubleshooting-tools/)
  * [CPUTool – Limit and Control CPU Utilization of Any Process in Linux](https://www.tecmint.com/cputool-limit-linux-process-cpu-usage-load/)


In this article, we briefly explained the kernel scheduler, and process priority, looked at how to run a program or command with modified priority, and also changed the priority of active Linux processes.
You can share any thoughts regarding this topic via the feedback form below.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install Kodi on Ubuntu-based Linux Distributions](https://www.tecmint.com/install-kodi-on-ubuntu/)
Next article:
[How to Enable or Disable SELinux Booleans for Apache](https://www.tecmint.com/enable-disable-apache-boolean-values/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#respond)** or
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
### 8 Comments
[Leave a Reply](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/fc29a040754a796607f46a128e6b54e53d1491994ec3326df3ef015c23bb8f37?s=50&d=blank&r=g)
Gwyneth Llewelyn
[ October 13, 2021 at 6:50 pm  ](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1607535)
As @Will mentioned over a year ago, setting nice/renice manually is great, but it will only last until the end of the user session.
If your system is started via `systemd` (most distros, including many embedded systems such as NAS, are slowly moving towards `systemd` as the _de facto_ standard way of booting a Linux server), you will very likely manage services by configuring files inside `/etc/systemd/system` or thereabouts. You can set the nice level at boot time by adding the directive `Nice=XX` where XX can be set from -20 (highest priority) and 19 (lowest priority) — the default value is zero.
Source:
[Reply](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1607535)
  2. ![](https://secure.gravatar.com/avatar/df87729b19eb2def825b52e7b0bd11275d4cfe8f5c9c9a8bf7b2a9900df00d89?s=50&d=blank&r=g)
Will
[ April 26, 2020 at 3:09 am  ](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1329757)
The last section explains how to set a whole group of processes to be a given niceness. How do I set just one process instead of a whole group? As an example, I have a Linux system running the **OpenMediaVault NAS** array. My objective is to set the **omv-engined** process and the **smbd** process as a **-20** niceness.
[Reply](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1329757)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ April 27, 2020 at 11:50 am  ](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1330383)
@Will
Just run this command specifying your process:
```
$ sudo nice -5 process_name arguments1 arguement2 ....

```

If it’s already running, renice it like this(replace 1055 with the actual process ID):
```
$ sudo renice -n  -12  -p 1055

```
[Reply](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1330383)
       * ![](https://secure.gravatar.com/avatar/df87729b19eb2def825b52e7b0bd11275d4cfe8f5c9c9a8bf7b2a9900df00d89?s=50&d=blank&r=g)
Will
[ April 30, 2020 at 9:46 pm  ](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1331086)
Sorry, I meant permanently. As I understand it **Renice** and **Nice** only are in effect until the next user session. I want the processes to always run under that priority without me issuing a command every time.
[Reply](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1331086)
  3. ![](https://secure.gravatar.com/avatar/341553f1a94d8b5419a5f39c43e777dc994f61bac9496b162ab16d2c837d14ea?s=50&d=blank&r=g)
Dr. GN Rao
[ November 11, 2019 at 12:25 pm  ](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1286311)
It is not clear how a task with priority **0** (nice value of **-20**) instead of **39** (nice value of 19) gets higher preference in execution, since it is stated in the article that “Processes with a higher priority will be executed before those with a lower priority…”.
Probably you may have to explain the handling of user space task priority in kernel in more detail! Otherwise, it’s a nice, well-written article. Keep it up!
[Reply](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1286311)
     * ![](https://secure.gravatar.com/avatar/1264eeb8f74f10b17e918e9e67111245cedc033d4e2b847c1e04b40ea80b017a?s=50&d=blank&r=g)
Bo
[ July 20, 2022 at 1:34 pm  ](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1848237)
Everywhere I’ve seen the same confusing “explanation” and they make it even worse.
The correct understanding is I suppose:
```

high priority = lower priority value

```

Another confusing thing, see the output of:
```
# renice -n -12 $PID

```

is: old priority 0 new priority – 12?
When in reality is the nice value!!! because the old priority is 20 and new 8!
[Reply](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1848237)
  4. ![](https://secure.gravatar.com/avatar/4854291b0adc270107927593805555146a8a0b683ce597cf3f7cd60a63c1e2d8?s=50&d=blank&r=g)
de Solages
[ November 2, 2019 at 7:39 am  ](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1281137)
Hello. There is a typo in this page:
“It’s primary function is to define the resource limits for the users logged in via PAM.”
should be “Its primary function (…)”.
[Reply](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1281137)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 4, 2019 at 10:48 am  ](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1282434)
@de,
Thanks, corrected the typo in the article..
[Reply](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#comment-1282434)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/#respond)
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
[How to Add or Remove Linux User From Group](https://www.tecmint.com/add-or-remove-user-from-group-in-linux/)
[Zaloha.sh – A Simple Local Directory Synchronizer Script for Linux](https://www.tecmint.com/local-directory-synchronizer-for-linux/)
[Mutt – A Command Line Email Client to Send Mails from Terminal](https://www.tecmint.com/send-mail-from-command-line-using-mutt-command/)
[13 CLI Tools Every Developer Should Master in 2025](https://www.tecmint.com/linux-cli-tools-for-developers/)
[How to Create a Shared Directory for All Users in Linux](https://www.tecmint.com/create-a-shared-directory-in-linux/)
[How to Use Heredoc in Shell Scripting](https://www.tecmint.com/use-heredoc-in-shell-scripting/)
## Linux Server Monitoring Tools
[Nmon – Monitor Linux System and Network Performance](https://www.tecmint.com/nmon-linux-performance-monitor/)
[How to Automate Daily Linux Health Checks with a Bash Script + Cron](https://www.tecmint.com/bash-script-automate-system-health-checks/)
[How to Boost Linux Server Internet Speed with TCP BBR](https://www.tecmint.com/increase-linux-server-internet-speed-with-tcp-bbr/)
[How to Monitor Apache Performance using Netdata on CentOS 7](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/)
[How to Monitor Ubuntu Performance Using Netdata](https://www.tecmint.com/monitor-ubuntu-performance-using-netdata/)
[Sysdig – A Powerful System Monitoring and Troubleshooting Tool for Linux](https://www.tecmint.com/sysdig-system-monitoring-and-troubleshooting-tool-for-linux/)
## Learn Linux Tricks & Tips
[How to Search and Remove Directories Recursively on Linux](https://www.tecmint.com/find-remove-directory-in-linux/)
[How to Test Website Loading Speed in Linux Terminal](https://www.tecmint.com/test-website-loading-speed-in-linux-terminal/)
[How to Create Hard and Symbolic Links in Linux](https://www.tecmint.com/create-hard-and-symbolic-links-in-linux/)
[How to Append Text to End of File in Linux](https://www.tecmint.com/append-text-to-end-of-file-in-linux/)
[Linux_Logo – Print ASCII Logo Of Linux with System Information](https://www.tecmint.com/print-linux-logo-ascii/)
[Tips to Create ISO from CD, Watch User Activity and Check Memory Usages of Browser](https://www.tecmint.com/creating-cdrom-iso-image-watch-user-activity-in-linux/)
## Best Linux Tools
[Universal Package Managers for Linux: Snap, Flatpak, and AppImage](https://www.tecmint.com/cross-distribution-package-managers-for-linux/)
[10 Best File Comparison and Difference (Diff) Tools for Linux](https://www.tecmint.com/best-linux-file-diff-tools-comparison/)
[27 Best Tools for VMware Administrators in 2024](https://www.tecmint.com/vmware-administrators-tools/)
[10 Top Open Source Reverse Proxy Servers for Linux](https://www.tecmint.com/open-source-reverse-proxy-servers-for-linux/)
[Top 6 Partition Managers (CLI + GUI) for Linux](https://www.tecmint.com/linux-partition-managers/)
[16 Best Notepad++ Alternatives for Linux in 2025](https://www.tecmint.com/best-notepad-alternatives-for-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/set-linux-process-priority-using-nice-and-renice-commands/ "Scroll back to top")
Search for:
