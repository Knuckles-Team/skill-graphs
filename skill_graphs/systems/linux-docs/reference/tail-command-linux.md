[Skip to content](https://www.tecmint.com/tail-command-linux/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/tail-command-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/tail-command-linux/)
As Linux users, we often work with long-running [background Linux processes](https://www.tecmint.com/find-linux-processes-memory-ram-cpu-usage/ "Find Top Running Processes in Linux"), which are called daemons or services. Some of the common examples of the services are [Secure Shell (sshd)](https://www.tecmint.com/ssh-command-usage/ "Basic SSH Command Usage in Linux"), Network Manager (networkd), Volume Manager (LVM), [Cron](https://www.tecmint.com/11-cron-scheduling-task-examples-in-linux/ "Cron Examples in Linux"), and the list goes on.
Many times we need to [monitor the logs](https://www.tecmint.com/best-linux-log-monitoring-and-management-tools/ "Log Monitoring Tools for Linux") of these services to debug the system issues. However, one of the main challenges is that these services generate a lot of logs and most of the time going through these logs makes it cumbersome, this is where we can use the **tail command**.
tail command is a command-line utility, similar to the [head command](https://www.tecmint.com/head-command-examples/ "head Command in Linux") that reads a file and prints the last 10 lines (content) of one or more files to standard output.
In this practical guide, we will learn about the tail command. By the end of this guide, Linux command-line users will be able to use the tail command effectively.

Table of Contents
Toggle
  * [tail Command Syntax](https://www.tecmint.com/tail-command-linux/#tail_Command_Syntax)
  * [1. Print Last 10 Lines Of File in Linux](https://www.tecmint.com/tail-command-linux/#1_Print_Last_10_Lines_Of_File_in_Linux)
  * [2. Print Last N Lines of File in Linux](https://www.tecmint.com/tail-command-linux/#2_Print_Last_N_Lines_of_File_in_Linux)
  * [3. Ignore First N Lines of a File in Linux](https://www.tecmint.com/tail-command-linux/#3_Ignore_First_N_Lines_of_a_File_in_Linux)
  * [4. Show Last N Characters of the File](https://www.tecmint.com/tail-command-linux/#4_Show_Last_N_Characters_of_the_File)
  * [5. Remove First N Characters of File](https://www.tecmint.com/tail-command-linux/#5_Remove_First_N_Characters_of_File)
  * [6. Show File Name in Header](https://www.tecmint.com/tail-command-linux/#6_Show_File_Name_in_Header)
  * [7. Show File Name as Header in Multiple Files](https://www.tecmint.com/tail-command-linux/#7_Show_File_Name_as_Header_in_Multiple_Files)
  * [8. How to Disable Display Header in File](https://www.tecmint.com/tail-command-linux/#8_How_to_Disable_Display_Header_in_File)
  * [9. How to Watch a File for Changes](https://www.tecmint.com/tail-command-linux/#9_How_to_Watch_a_File_for_Changes)


The syntax of the **tail** command is similar to [other Linux commands](https://www.tecmint.com/essential-linux-commands/ "Linux Commands"):
```
$ tail [OPTIONS] [FILE-1] [FILE-2] ...

```

By default, the **tail** command prints the last **10** lines of the given file as shown.
```
**$ tail /var/log/secure**


Apr  2 14:17:24 TecMint sshd[201178]: Disconnected from user tecmint 192.168.0.162 port 59774
Apr  2 14:17:24 TecMint sshd[201165]: pam_unix(sshd:session): session closed for user tecmint
Apr  2 14:29:12 TecMint sshd[201366]: Accepted password for tecmint from 192.168.0.162 port 56378 ssh2
Apr  2 14:29:12 TecMint systemd[201371]: pam_unix(systemd-user:session): session opened for user tecmint(uid=1002) by (uid=0)
Apr  2 14:29:12 TecMint sshd[201366]: pam_unix(sshd:session): session opened for user tecmint(uid=1002) by (uid=0)
Apr  2 14:29:12 TecMint sshd[201382]: Received disconnect from 192.168.0.162 port 56378:11: disconnected by user
Apr  2 14:29:12 TecMint sshd[201382]: Disconnected from user tecmint 192.168.0.162 port 56378
Apr  2 14:29:12 TecMint sshd[201366]: pam_unix(sshd:session): session closed for user tecmint
Apr  2 15:12:55 TecMint sshd[202049]: Accepted password for root from 192.168.0.162 port 53334 ssh2
Apr  2 15:12:55 TecMint sshd[202049]: pam_unix(sshd:session): session opened for user root(uid=0) by (uid=0)

```

Here, we can see that the above command shows the last ten lines from the **/var/log/secure** file.
In the last example, the command prints the last 10 lines of the given file. However, we can use the `-n` option which allows us to limit the number of lines to be printed on the screen as shown.
```
**$ tail -n 3 /var/log/secure**

Apr  2 14:29:12 TecMint sshd[201366]: pam_unix(sshd:session): session closed for user tecmint
Apr  2 15:12:55 TecMint sshd[202049]: Accepted password for root from 192.168.0.162 port 53334 ssh2
Apr  2 15:12:55 TecMint sshd[202049]: pam_unix(sshd:session): session opened for user root(uid=0) by (uid=0)

```

In this example, we can see that now the command shows the last three lines only instead of the ten lines.
Here, we can use the plus `(+)` symbol with the `-n` option, which allows us to control the starting point from the given file.
To understand this, let’s use the `+5` value to start the output from the 5th line:
```
**$ tail -n +5 /var/log/secure**

Apr  2 14:17:24 TecMint sshd[201178]: Disconnected from user tecmint 192.168.0.162 port 59774
Apr  2 14:17:24 TecMint sshd[201165]: pam_unix(sshd:session): session closed for user tecmint
Apr  2 14:29:12 TecMint sshd[201366]: Accepted password for tecmint from 192.168.0.162 port 56378 ssh2
Apr  2 14:29:12 TecMint systemd[201371]: pam_unix(systemd-user:session): session opened for user tecmint(uid=1002) by (uid=0)
Apr  2 14:29:12 TecMint sshd[201366]: pam_unix(sshd:session): session opened for user tecmint(uid=1002) by (uid=0)
Apr  2 14:29:12 TecMint sshd[201382]: Received disconnect from 192.168.0.162 port 56378:11: disconnected by user
Apr  2 14:29:12 TecMint sshd[201382]: Disconnected from user tecmint 192.168.0.162 port 56378
Apr  2 14:29:12 TecMint sshd[201366]: pam_unix(sshd:session): session closed for user tecmint
Apr  2 15:12:55 TecMint sshd[202049]: Accepted password for root from 192.168.0.162 port 53334 ssh2
Apr  2 15:12:55 TecMint sshd[202049]: pam_unix(sshd:session): session opened for user root(uid=0) by (uid=0)

```

Similar to lines, we can also use the command to display the last `N` characters of the file using the `-c` option as shown below:
```
**$ tail -c 7 /var/log/secure**

(uid=0)

```

In this example, we can see that the command shows the last seven **ASCII** characters of the given file.
Similarly, we can use the plus symbol `(+)` with the `-c` option to skip the first `N` character. So let’s skip the first line of the file using the below command:
```
**$ tail -c +5 /var/log/secure**

Apr  2 03:02:59 TecMint sudo[162801]: root : TTY=pts/2 ; PWD=/root ; USER=root ; COMMAND=/bin/dnf install R
Apr  2 03:02:59 TecMint sudo[162801]: pam_unix(sudo:session): session opened for user root(uid=0) by root(uid=0)
Apr  2 03:03:02 TecMint sudo[162801]: pam_unix(sudo:session): session closed for user root
Apr  2 03:11:17 TecMint groupadd[163602]: group added to /etc/group: name=avahi, GID=70
Apr  2 03:11:18 TecMint groupadd[163602]: group added to /etc/gshadow: name=avahi
Apr  2 03:11:18 TecMint groupadd[163602]: new group: name=avahi, GID=70
Apr  2 03:11:19 TecMint useradd[163610]: new user: name=avahi, UID=70, GID=70, home=/var/run/avahi-daemon, shell=/sbin/nologin, from=none
Apr  2 03:13:41 TecMint groupadd[163704]: group added to /etc/group: name=colord, GID=986
Apr  2 03:13:41 TecMint groupadd[163704]: group added to /etc/gshadow: name=colord

```

Here, we can see that the command shows all the lines except the first line.
We can instruct the **tail** command to display the current file name as a display header, which comes in handy while working with multiple files.
So, let’s use the `-v` option to enable the display header:
```
**$ tail -n 3 -v /var/log/secure**

==>/var/log/secure <==
Apr  2 14:29:12 TecMint sshd[201366]: pam_unix(sshd:session): session closed for user tecmint
Apr  2 15:12:55 TecMint sshd[202049]: Accepted password for root from 192.168.0.162 port 53334 ssh2
Apr  2 15:12:55 TecMint sshd[202049]: pam_unix(sshd:session): session opened for user root(uid=0) by (uid=0)

```

In the above output, `==> /var/log/secure <==` represents the display header.
Just like any other file-processing command, we can also use multiple files with the **tail** command. In such cases, the display header gets used to separate the file contents.
```
**$ tail -n 3 -v /var/log/secure /var/log/secure-20230402**

==> /var/log/secure <==
Apr  2 14:29:12 TecMint sshd[201366]: pam_unix(sshd:session): session closed for user tecmint
Apr  2 15:12:55 TecMint sshd[202049]: Accepted password for root from 192.168.0.162 port 53334 ssh2
Apr  2 15:12:55 TecMint sshd[202049]: pam_unix(sshd:session): session opened for user root(uid=0) by (uid=0)

==> /var/log/secure-20230402 <==
Mar 31 03:50:53 TecMint groupadd[156163]: new group: name=docker, GID=987
Mar 31 04:46:11 TecMint sshd[159403]: Accepted password for root from 192.168.0.162 port 46480 ssh2
Mar 31 04:46:11 TecMint sshd[159403]: pam_unix(sshd:session): session opened for user root(uid=0) by (uid=0)

```

In the above output, we can see the display header for each file.
In the previous example, we saw that the command enables the display header while working with multiple files. However, we can suppress this default behavior using the `-q` option.
```
**$ tail -q -n 3 /var/log/secure /var/log/secure-20230402**

Apr  2 14:29:12 TecMint sshd[201366]: pam_unix(sshd:session): session closed for user tecmint
Apr  2 15:12:55 TecMint sshd[202049]: Accepted password for root from 192.168.0.162 port 53334 ssh2
Apr  2 15:12:55 TecMint sshd[202049]: pam_unix(sshd:session): session opened for user root(uid=0) by (uid=0)
Mar 31 03:50:53 TecMint groupadd[156163]: new group: name=docker, GID=987
Mar 31 04:46:11 TecMint sshd[159403]: Accepted password for root from 192.168.0.162 port 46480 ssh2
Mar 31 04:46:11 TecMint sshd[159403]: pam_unix(sshd:session): session opened for user root(uid=0) by (uid=0)

```

Here, we can see that now the command displays the file contents one after another without any display header.
So far we saw that the tail command exits once it processes the required number of lines or characters. However, sometimes we want to view the newly generated logs as well.
In such cases, we can use the `-f` option with the command, which allows us to monitor the file for changes in a real-time.
To understand this, first, let’s execute the below command in the first terminal:
```
**$ tail -f /var/log/messages**


Apr  2 15:13:28 TecMint NetworkManager[741]:   [1680462808.8441] policy: set-hostname: current hostname was changed outside NetworkManager: 'TecMint'
Apr  2 15:13:28 TecMint systemd[1]: Starting Network Manager Script Dispatcher Service...
Apr  2 15:13:28 TecMint systemd[1]: Started Network Manager Script Dispatcher Service.
Apr  2 15:13:37 TecMint arpwatch[11001]: rename arp.dat -> arp.dat-: Operation not permitted
Apr  2 15:13:38 TecMint systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Apr  2 15:13:58 TecMint systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Apr  2 15:18:03 TecMint systemd[1]: Starting dnf makecache...
Apr  2 15:18:03 TecMint dnf[202235]: Metadata cache refreshed recently.
Apr  2 15:18:03 TecMint systemd[1]: dnf-makecache.service: Deactivated successfully.
Apr  2 15:18:03 TecMint systemd[1]: Finished dnf makecache.

```

Here, we can see that the command is waiting infinitely after displaying the last ten lines:
Next, let’s open another terminal and append some text to the **numbers-2.txt** file:
```
$ echo "View Logs in Real-Time" >> /var/log/messages

```

Now, let’s switch to the first terminal to view the newly added text:
```
**$ tail -f /var/log/messages**

Apr  2 15:13:28 TecMint NetworkManager[741]:   [1680462808.8441] policy: set-hostname: current hostname was changed outside NetworkManager: 'TecMint'
Apr  2 15:13:28 TecMint systemd[1]: Starting Network Manager Script Dispatcher Service...
Apr  2 15:13:28 TecMint systemd[1]: Started Network Manager Script Dispatcher Service.
Apr  2 15:13:37 TecMint arpwatch[11001]: rename arp.dat -> arp.dat-: Operation not permitted
Apr  2 15:13:38 TecMint systemd[1]: NetworkManager-dispatcher.service: Deactivated successfully.
Apr  2 15:13:58 TecMint systemd[1]: systemd-hostnamed.service: Deactivated successfully.
Apr  2 15:18:03 TecMint systemd[1]: Starting dnf makecache...
Apr  2 15:18:03 TecMint dnf[202235]: Metadata cache refreshed recently.
Apr  2 15:18:03 TecMint systemd[1]: dnf-makecache.service: Deactivated successfully.
Apr  2 15:18:03 TecMint systemd[1]: Finished dnf makecache.
**View Logs in Real-Time**

```

Here, we can see that the tail command shows the newly added text.
Do you know of any other best example of the tail command in Linux? Let us know your views in the comments below.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[10 SCP Commands to Transfer Files/Folders in Linux](https://www.tecmint.com/scp-commands-examples/)
Next article:
[12 Ping Command Examples to Test Your Network](https://www.tecmint.com/ping-command/)
![Photo of author](https://secure.gravatar.com/avatar/043721451ba3c67ab7c1e510f30b1af43862d4b5e97012854c0cadf8aa37ecbc?s=100&d=blank&r=g)
Narendra K
I'm an experienced and passionate software engineer with in-depth experience in Linux, Distributed systems, DevOps, and Cloud. My expertise lies in back-end web development, and the main languages in my tech stack are Java, Spring, Python, and Go. I’m a lifelong learner and an open-source enthusiast.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/tail-command-linux/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/tail-command-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/tail-command-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
