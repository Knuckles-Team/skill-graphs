[Skip to content](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/)
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
  * [Pro Courses](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/)
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
  * [Pro Courses](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/)
# 10 Useful Sudoers Configurations for Setting ‘sudo’ in Linux
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: July 13, 2023 Read Time: 5 minsCategories [Linux Commands](https://www.tecmint.com/category/linux-commands/) [11 Comments](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comments)
In Linux and other Unix-like operating systems, only the **root** user can run all commands and perform certain critical operations on the system such as install and update, remove packages, [create users and groups](https://www.tecmint.com/add-users-in-linux/), modify important system configuration files and so on.
However, a system administrator who assumes the role of the root user can permit other normal system users with the help of [sudo command](https://www.tecmint.com/su-vs-sudo-and-how-to-configure-sudo-in-linux/) and a few configurations to run some commands as well as carry out a number of vital system operations including the ones mentioned above.
Alternatively, the system administrator can share the root user password (which is not a recommended method) so that normal system users have access to the root user account via **su** command.
**sudo** allows a permitted user to execute a command as root (or another user), as specified by the security policy:
  1. It reads and parses **/etc/sudoers** , looks up the invoking user and its permissions,
  2. then prompts the invoking user for a password (normally the user’s password, but it can as well be the target user’s password. Or it can be skipped with NOPASSWD tag),
  3. after that, sudo creates a child process in which it calls **setuid()** to switch to the target user
  4. next, it executes a shell or the command given as arguments in the child process above.


Below are ten **/etc/sudoers** file configurations to modify the behavior of **sudo** command using **Defaults** entries.
```
$ sudo cat /etc/sudoers

```

/etc/sudoers File
```
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
**Defaults	env_reset
Defaults	mail_badpass
Defaults	secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
Defaults	logfile="/var/log/sudo.log"
Defaults	lecture="always"
Defaults	badpass_message="Password is wrong, please try again"
Defaults	passwd_tries=5
Defaults	insults
Defaults	log_input,log_output**

```

#### Types of Defaults Entries
```
Defaults                parameter,   parameter_list     #affect all users on any host
Defaults@Host_List      parameter,   parameter_list     #affects all users on a specific host
Defaults:User_List      parameter,   parameter_list     #affects a specific user
Defaults!Cmnd_List      parameter,   parameter_list     #affects  a specific command
Defaults>Runas_List     parameter,   parameter_list     #affects commands being run as a specific user

```

For the scope of this guide, we will zero down to the first type of **Defaults** in the forms below. Parameters may be flags, integer values, strings, or lists.
You should note that flags are implicitly boolean and can be turned off using the `'!'` operator, and lists have two additional assignment operators, `+=` (add to list) and `-=` (remove from list).
```
Defaults     parameter
OR
Defaults     parameter=value
OR
Defaults     parameter -=value
Defaults     parameter +=value
OR
Defaults     !parameter

```

### 1. Set a Secure PATH
This is the path used for every command run with sudo, it has two importances:
  1. Used when a system administrator does not trust sudo users to have a secure PATH environment variable
  2. To separate “root path” and “user path”, only users defined by **exempt_group** are not affected by this setting.


To set it, add the line:
```
Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"

```

### 2. Enable sudo on TTY User Login Session
To enable sudo to be invoked from a real **tty** but not through methods such as **cron** or **cgi-bin** scripts, add the line:
```
Defaults  requiretty

```

### 3. Run Sudo Command Using a pty
A few times, attackers can run a malicious program (such as a virus or malware) using sudo, which would again fork a background process that remains on the user’s terminal device even when the main program has finished executing.
To avoid such a scenario, you can configure sudo to run other commands only from a **psuedo-pty** using the `use_pty` parameter, whether I/O logging is turned on or not as follows:
```
Defaults  use_pty

```

### 4. Create a Sudo Log File
By default, sudo logs through syslog(3). However, to specify a custom log file, use the logfile parameter like so:
```
Defaults  logfile="/var/log/sudo.log"

```

To log hostname and the four-digit year in the custom log file, use **log_host** and **log_year** parameters respectively as follows:
```
Defaults  log_host, log_year, logfile="/var/log/sudo.log"

```

Below is an example of a custom sudo log file:
![Create Custom Sudo Log File](https://www.tecmint.com/wp-content/uploads/2017/01/Create-Sudo-Log-File.png)Create Custom Sudo Log File
### 5. Log Sudo Command Input/Output
The **log_input** and **log_output** parameters enable sudo to run a command in pseudo-tty and log all user input and all output sent to the screen receptively.
The default I/O log directory is **/var/log/sudo-io** , and if there is a session sequence number, it is stored in this directory. You can specify a custom directory through the **iolog_dir** parameter.
```
Defaults   log_input, log_output

```

There are some escape sequences are supported such as `%{seq}` which expands to a monotonically increasing base-36 sequence number, such as 000001, where every two digits are used to form a new directory, e.g. **00/00/01** as in the example below:
```
$ cd /var/log/sudo-io/
$ ls
$ cd  00/00/01
$ ls
$ cat log

```
![Log sudo Input Output](https://www.tecmint.com/wp-content/uploads/2017/01/Log-sudo-Input-Output.png)Log sudo Input Output
You can view the rest of the files in that directory using the [cat command](https://www.tecmint.com/13-basic-cat-command-examples-in-linux/).
### 6. Lecture Sudo Users
To lecture sudo users about password usage on the system, use the **lecture** parameter as below.
It has 3 possible values:
  1. always – always lecture a user.
  2. once – only lecture a user the first time they execute sudo command (this is used when no value is specified)
  3. never – never lecture the user.

```

Defaults  lecture="always"

```

Additionally, you can set a custom lecture file with the **lecture_file** parameter, type the appropriate message in the file:
```
Defaults  lecture_file="/path/to/file"

```
![Lecture Sudo Users](https://www.tecmint.com/wp-content/uploads/2017/01/Lecture-Sudo-Users.png)Lecture Sudo Users
### 7. Show Custom Message When You Enter Wrong sudo Password
When a user enters a wrong password, a certain message is displayed on the command line. The default message is “**sorry, try again** ”, you can modify the message using the **badpass_message** parameter as follows:
```
Defaults  badpass_message="Password is wrong, please try again"

```

### 8. Increase sudo Password Tries Limit
The parameter **passwd_tries** is used to specify the number of times a user can try to enter a password.
The default value is 3:
```
Defaults   passwd_tries=5

```
![Increase Sudo Password Attempts](https://www.tecmint.com/wp-content/uploads/2017/01/Increase-Sudo-Password-Attempts.png)Increase Sudo Password Attempts
To set a password timeout (default is 5 minutes) using **passwd_timeout** parameter, add the line below:
```
Defaults   passwd_timeout=2

```

### 9. Let Sudo Insult You When You Enter Wrong Password
In case a user types a wrong password, sudo will display insults on the terminal with the insults parameter. This will automatically turn off the **badpass_message** parameter.
```
Defaults  insults

```
![Let's Sudo Insult You When Enter Wrong Password](https://www.tecmint.com/wp-content/uploads/2017/01/Sudo-Insult-Message.png)Let’s Sudo Insult You When Enter Wrong Password
**Read More** : [Let Sudo Insult You When You Enter Incorrect Password](https://www.tecmint.com/sudo-insult-when-enter-wrong-password/)
### 10. Learn More Sudo Configurations
Additionally, you can learn more **sudo** command configurations by reading: [Difference Between su and sudo and How to Configure sudo in Linux](https://www.tecmint.com/su-vs-sudo-and-how-to-configure-sudo-in-linux/).
That’s it! You can share other useful sudo command configurations or [tricks and tips with Linux](https://www.tecmint.com/tag/linux-tricks/) users out there via the comment section below.
Tags [Linux Tricks](https://www.tecmint.com/tag/linux-tricks/), [sudo commands](https://www.tecmint.com/tag/sudo-commands/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[12 Useful Commands For Filtering Text for Effective File Operations in Linux](https://www.tecmint.com/linux-file-operations-commands/)
Next article:
[3 Ways to Permanently and Securely Delete ‘Files and Directories’ in Linux](https://www.tecmint.com/permanently-and-securely-delete-files-directories-linux/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#respond)** or
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
### 11 Comments
[Leave a Reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/e9d972755b95ccac3dea64ccd45b8de81799efd4cdb765c05aa5003197b0d696?s=50&d=blank&r=g)
Ashok
[ September 15, 2021 at 12:26 am  ](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1588994)
Hello Aaron, thank you for sharing this info on sudo configuration. Is there a way for sudo to record **tty** commands run by a ldap user after sudo to a service account and store them to a file?
Example:
```
[user@test1] / # sudo su - oracle
[oracle@test1] /home/oracle # hostname
test1
[oracle@test1] /home/oracle # pwd
/home/oracle

```

How would I let sudo store these commands (hostname, pwd, etc) to a file after a user sudo to service account (oracle, etc) and run commands as that service account on a server? I have an audit requirement on AIX 7.2 servers to capture all TTY session commands run by a user after sudo to a service account hosted on each server.
Thank you for your time.
Thank you.
[Reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1588994)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ September 15, 2021 at 10:40 am  ](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1589161)
@Ashok,
First, create a log directory and set the sticky bit on it.
```
# mkdir -p /var/log/users_historylogs/
# chmod +t  /var/log/users_historylogs/

```

Next, create a new script file under **/etc/profile.d/** directory.
```
# vi /etc/profile.d/history_log.sh

```

And add the below content at the bottom, save, and exit.
```
_who_am_i=$(whoami|awk '{print $1}')
_ID=$(id -u $_who_am_i)

if [ "$_ID" > 0 ]
then
export HISTSIZE=10000
export HISTTIMEFORMAT='%F %T '
export HISTFILE=/var/log/users_historylogs/history-users-$(whoami | awk '{print $1}';exit)-$(date +%F)
export PROMPT_COMMAND='history -a'
fi

```

Set the permission and enable the script.
```
# chmod 770 /etc/profile.d/history_log.sh
# source /etc/profile.d/history_log.sh

```

Now all user executed commands history saved to log file…
[Reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1589161)
       * ![](https://secure.gravatar.com/avatar/e9d972755b95ccac3dea64ccd45b8de81799efd4cdb765c05aa5003197b0d696?s=50&d=blank&r=g)
Ashok B
[ September 16, 2021 at 4:18 am  ](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1589639)
Hi Ravi,
Thank you so much for the quick response. Does the same procedure apply on AIX 7.2 servers since it uses Korn shell by default? I see that the **/etc/profile.d** directory does not exist on AIX servers and I have implemented step 1 by adding those lines in **/etc/profile** to set up secondary logging for root which looks good as the file was created, not sure if I should add commands to the same **/etc/profile** file to setup secondary logging for other users except root. Thank you.
[Reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1589639)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ September 16, 2021 at 11:31 am  ](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1589808)
@Ashok,
I think you can add those lines to /etc/profile and see if it is working or not…
[Reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1589808)
       * ![](https://secure.gravatar.com/avatar/e9020296a6d00ff05b405aa31ed192eba3923b7e0b6c7ca0ecd31af2336b0918?s=50&d=blank&r=g)
Alajjana
[ February 10, 2023 at 1:37 am  ](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1961556)
This is a minor typo.
```
$(who am i | awk '{print $1}';exit)

```

should be:
```
$(whoami | awk '{print $1}';exit)

```

Fantastic. Thank you for this script.
[Reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1961556)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 10, 2023 at 12:28 pm  ](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1961775)
@Aljjana,
Thanks, corrected the command in the script…
[Reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1961775)
  2. ![](https://secure.gravatar.com/avatar/11a10bb7637f1978668bec5534d22f843ae630110dc27a2531a1da897c3eccfd?s=50&d=blank&r=g)
Ryan Quezada G.
[ March 22, 2020 at 9:42 pm  ](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1322539)
This is an excellent article. With this, I complement my knowledge about the root users and permissions.
[Reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1322539)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ March 25, 2020 at 1:51 pm  ](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1323340)
@Ryan
Great! We are grateful that this has helped you gain more knowledge about Linux. Many thanks for the useful feedback.
[Reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1323340)
  3. ![](https://secure.gravatar.com/avatar/6e5f2aff6284a57f5c6f478d1b13d39c5e1844651dfcefc9d58ab86457e71a62?s=50&d=blank&r=g)
Brain
[ November 11, 2018 at 8:05 pm  ](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1057980)
Hi,
Thanks for the nice overview.
Can you help with this?
I want to mount a special source without root privileges. So I made an entry in the **/etc/sudoers** file:
```
username       ALL = NOPASSWD: /sbin/mount.cifs, /bin/umount /mnt/folder

```

How can I restrict the source that I want to mount to be only one that can be mounted. Now username can mount everything.
Thanks in advance.
Bye,
[Reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1057980)
     * ![](https://secure.gravatar.com/avatar/2504b66e5a3b15eb0b9fe5b7838f446cbad71aa0bead4f0f8854507c49a87fbc?s=50&d=blank&r=g)
Garry Garrett
[ August 14, 2019 at 7:45 pm  ](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1224395)
I think what you may want to do is, instead of using **sudo** , add the mount to **/etc/fstab** , and include the option **“user”** (see the man page on “mount”). What this will do is allow ordinary users to mount/unmount the filesystem. That would allow ALL users to mount/unmount it. They can then say “**mount /mnt/folder** “. This mount option is specific to Linux and would not work on other flavors of Unix.
Another option would be to use the automounter. You could setup a direct automount map. Then whenever a user does “**cd /mnt/folder** “, it mounts. After it mounts, every 5 minutes, it half-heartedly attempts to unmount it, which will not be successful if it is still in use. Again, this would allow ALL users to mount it.
If you really want just the one user to be able to mount/unmount, then you’d need to spell out the full mount command (not **/sbin/mount.cifs**):
`user ALL = NOPASSWD: /bin/mount /path-to-device /mnt/folder, /bin/umount /mnt/folder`
(there might be some options you’ll want to specify after “mount”, e.g. “-o ro”, “-t cifs”, etc.). The user will then need to type the command-line exactly as it appears in sudoers (if they are not that savvy, create them an alias).
[Reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1224395)
       * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ August 19, 2019 at 2:16 pm  ](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1227978)
@Garry
These are practically better solutions, well explained. Am also testing them. Thanks for sharing.
[Reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#comment-1227978)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/#respond)
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
[How to Delete all Text in a File Using Vi/Vim Editor](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/)
[Mhddfs – Combine Several Smaller Partition into One Large Virtual Storage](https://www.tecmint.com/combine-partitions-into-one-in-linux-using-mhddfs/)
[How to Run Multiple Commands on Multiple Linux Servers](https://www.tecmint.com/run-multiple-commands-on-multiple-linux-servers/)
[How to Set Limits on User Running Processes in Linux](https://www.tecmint.com/set-limits-on-user-processes-using-ulimit-in-linux/)
[8 Linux Commands to Diagnose Hard Drive Issues in Linux](https://www.tecmint.com/fix-hard-drive-bottlenecks-in-linux/)
[15 ‘pwd’ (Print Working Directory) Command Examples in Linux](https://www.tecmint.com/pwd-command-examples/)
## Linux Server Monitoring Tools
[Htop – An Interactive Process Viewer for Linux](https://www.tecmint.com/htop-linux-process-monitoring/)
[4 Useful Commandline Tools to Monitor MySQL Performance in Linux](https://www.tecmint.com/mysql-performance-monitoring/)
[Netdata – A Real-Time Performance Monitoring Tool for Linux Systems](https://www.tecmint.com/netdata-real-time-linux-performance-network-monitoring-tool/)
[Darkstat – A Web Based Linux Network Traffic Analyzer](https://www.tecmint.com/darkstat-web-based-linux-network-traffic-analyzer/)
[Web VMStat: A Real Time System Statistics (Memory, CPU, Processes, etc) Monitoring Tool for Linux](https://www.tecmint.com/install-web-vmstat-in-linux/)
[How to Install Zabbix Agent and Add Windows Host to Zabbix Monitoring – Part 4](https://www.tecmint.com/install-zabbix-agent-and-add-windows-host-to-zabbix-monioring/)
## Learn Linux Tricks & Tips
[Powerline – Adds Statuslines and Prompts to Vim and Bash Shell](https://www.tecmint.com/powerline-plugin-for-vim/)
[4 Ways to Send Email Attachment from Linux Command Line](https://www.tecmint.com/send-email-attachment-from-linux-commandline/)
[Mhddfs – Combine Several Smaller Partition into One Large Virtual Storage](https://www.tecmint.com/combine-partitions-into-one-in-linux-using-mhddfs/)
[Easily Correct a Typo of Previous Command Using Carat (^) Symbol](https://www.tecmint.com/fix-correct-mistakes-typos-previous-command-in-linux/)
[How to Find and Remove Duplicate/Unwanted Files in Linux Using ‘FSlint’ Tool](https://www.tecmint.com/fslint-find-and-remove-duplicate-unwanted-files-in-linux/)
[How to Send a Message to Logged Users in Linux Terminal](https://www.tecmint.com/send-a-message-to-logged-users-in-linux-terminal/)
## Best Linux Tools
[10 Tools to Take or Capture Desktop Screenshots in Linux](https://www.tecmint.com/take-or-capture-desktop-screenshots-in-ubuntu-linux/)
[10 Best Tools to Install on Fresh Linux Mint Installation](https://www.tecmint.com/linux-mint-tools/)
[8 Best Open-Source Disk Cloning & Backup Tools for Linux (2024)](https://www.tecmint.com/linux-disk-cloning-tools/)
[8 Best MySQL/MariaDB GUI Tools for Linux in 2024](https://www.tecmint.com/mysql-gui-tools-for-linux/)
[How to Open and Edit Apple iWork Files on Linux](https://www.tecmint.com/open-and-edit-apple-iwork-files-on-linux/)
[8 Best RDP (Remote Desktop) Clients for Linux in 2024](https://www.tecmint.com/best-linux-rdp-remote-desktop-clients/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/sudoers-configurations-for-setting-sudo-in-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
