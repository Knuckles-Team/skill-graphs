[Skip to content](https://www.tecmint.com/audit-linux-process-using-autrace-on-centos-rhel/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/audit-linux-process-using-autrace-on-centos-rhel/ "Linux Online Courses")
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


[](https://www.tecmint.com/audit-linux-process-using-autrace-on-centos-rhel/)
This article is our ongoing series on [Linux Auditing](https://www.tecmint.com/category/linux-auditing/), in our last three articles we have explained how to [audit Linux systems](https://www.tecmint.com/linux-system-auditing-with-auditd-tool-on-centos-rhel/) (**CentOS** and **RHEL**), [query auditd logs using ausearch](https://www.tecmint.com/query-audit-logs-using-ausearch-tool-on-centos-rhel/) and generate reports using aureport utility.
In this article, we will explain how to audit a given process using **autrace** utility, where we’ll analyze a process by tracing the system calls a process makes.
**Read Also** : [How to Trace Execution of Commands in Shell Script with Shell Tracing](https://www.tecmint.com/trace-shell-script-execution-in-linux/)
#### What is autrace?
**autrace** is a command line utility that runs a program until it exits, just like **strace** ; it adds the audit rules to trace a process and saves the audit information in **/var/www/audit/audit.log** file. For it to work (i.e before running the selected program), you must first delete all existing audit rules.
The syntax for using **autrace** is shown below, and it only accepts one option, `-r` which limits syscalls collected to ones required for assessing resource usage of the process:
```
# autrace -r program program-args

```

**Attention** : In the **autrace** man page, the syntax as follows, which is actually a documentation mistake. Because using this form, the program you run will assume you’re using one of its internal option thus resulting into an error or performing the default action enabled by the option.
```
# autrace program -r program-args

```

If you have any audit rules present, **autrace** shows the following error.
```
# autrace /usr/bin/df

```
![autrace Error](https://www.tecmint.com/wp-content/uploads/2017/09/autrace-error.png)autrace Error
First delete all the auditd rules with the following command.
```
# auditctl -D

```

Then proceed to run **autrace** with your target program. In this example, we are tracing the execution of [df command](https://www.tecmint.com/how-to-check-disk-space-in-linux/), which shows filesystem usage.
```
# autrace /usr/bin/df -h

```
![Trace df Command](https://www.tecmint.com/wp-content/uploads/2017/09/autrace-df-command.png)Trace df Command
From the screenshot above, you can find all the log entries to do with the trace, from the audit log file using [ausearch utility](https://www.tecmint.com/query-audit-logs-using-ausearch-tool-on-centos-rhel/) as follows.
```
# ausearch -i -p 2678

```

Where the option:
  * `-i` – enables interpreting of numeric values into text.
  * `-p` – passes the process ID to be searched.

![Audit Report of df Command](https://www.tecmint.com/wp-content/uploads/2017/09/Audit-df-Command.png)Audit Report of df Command
To generate a report about the trace details, you can build a command line of **ausearch** and **aureport** like this.
```
# ausearch -p 2678 --raw | aureport -i -f

```

Where:
  * `--raw` – tells ausearch to deliver raw input to aureport.
  * `-f` – enables reporting about files and af_unix sockets.
  * `-i` – allows interpreting of numeric values into text.

![Generate Trace Report of df Command](https://www.tecmint.com/wp-content/uploads/2017/09/generate-trace-report.png)Generate Trace Report of df Command
And using the command below, we are limiting the syscalls gathered to ones needed for analyzing resource usage of the df process.
```
# autrace -r /usr/bin/df -h

```

Assuming you have autraced a program for the last one week; meaning there is a lot of information dumped in the audit logs. To produce a report for only today’s records, use the `-ts` ausearch flag to specify the start date/time for searching:
```
# ausearch -ts today -p 2678 --raw | aureport -i -f

```
![Generate Trace Report based on Time](https://www.tecmint.com/wp-content/uploads/2017/09/generate-trace-report-based-on-time.png)Generate Trace Report based on Time
That’s it! this way you can trace and audit specific Linux process using **autrace** tool, for more information check man pages.
You can also read out these related, useful guides:
  1. [Sysdig – A Powerful System Monitoring and Troubleshooting Tool for Linux](https://www.tecmint.com/sysdig-system-monitoring-and-troubleshooting-tool-for-linux/)
  2. [BCC – Dynamic Tracing Tools for Linux Performance Monitoring, Networking and More](https://www.tecmint.com/bcc-best-linux-performance-monitoring-tools/)
  3. [30 Useful ‘ps Command’ Examples for Linux Process Monitoring](https://www.tecmint.com/ps-command-examples-for-linux-process-monitoring/)
  4. [CPUTool – Limit and Control CPU Utilization of Any Process in Linux](https://www.tecmint.com/cputool-limit-linux-process-cpu-usage-load/)
  5. [Find Top Running Processes by Highest Memory and CPU Usage in Linux](https://www.tecmint.com/find-linux-processes-memory-ram-cpu-usage/)


That’s all for now! You can ask any questions or share thoughts about this article via the comment from below. In the next article, we will describe how to configure PAM (Pluggable Authentication Module) for auditing of TTY input for specified users CentOS/RHEL.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[15 Useful ‘Sockstat Command Examples’ to Find Open Ports in FreeBSD](https://www.tecmint.com/sockstat-command-examples-to-find-open-ports-in-freebsd/)
Next article:
[How to Configure PAM to Audit Logging Shell User Activity](https://www.tecmint.com/configure-pam-to-audit-logging-shell-tty-user-activity/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/audit-linux-process-using-autrace-on-centos-rhel/#respond)** or
## Related Posts
[![Check Integrity With AIDE in Fedora](https://www.tecmint.com/wp-content/uploads/2019/01/Check-Integrity-With-AIDE-in-Fedora.png)](https://www.tecmint.com/check-integrity-with-aide-in-fedora/ "How to Check Integrity With AIDE in Fedora")
[![Audit User TTY Shell Activity](https://www.tecmint.com/wp-content/uploads/2017/09/Audit-User-TTY-Shell-Activity.png)](https://www.tecmint.com/configure-pam-to-audit-logging-shell-tty-user-activity/ "How to Configure PAM to Audit Logging Shell User Activity")
[![Create Audit Log Reports](https://www.tecmint.com/wp-content/uploads/2017/09/Create-Audit-Log-Report.png)](https://www.tecmint.com/create-reports-from-audit-logs-using-aureport-on-centos-rhel/ "How to Create Reports from Audit Logs Using ‘aureport’ on CentOS/RHEL")
[![Audit Logs Using ausearch Tool](https://www.tecmint.com/wp-content/uploads/2017/09/Audit-Logs-using-Ausearch-Tool.png)](https://www.tecmint.com/query-audit-logs-using-ausearch-tool-on-centos-rhel/ "How to Query Audit Logs Using ‘ausearch’ Tool on CentOS/RHEL")
[![Linux System Auditing with Auditd on CentOS](https://www.tecmint.com/wp-content/uploads/2017/09/CentOS-System-Auditing-with-Auditd.png)](https://www.tecmint.com/linux-system-auditing-with-auditd-tool-on-centos-rhel/ "Learn Linux System Auditing with Auditd Tool on CentOS/RHEL")
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/audit-linux-process-using-autrace-on-centos-rhel/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/audit-linux-process-using-autrace-on-centos-rhel/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=2116224916222418&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
