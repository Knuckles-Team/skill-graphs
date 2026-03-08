[Skip to content](https://www.tecmint.com/add-or-remove-user-from-group-in-linux/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/add-or-remove-user-from-group-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/add-or-remove-user-from-group-in-linux/)
[Linux](https://www.tecmint.com/what-is-linux/ "What Is Linux?") is by default a multi-user system (meaning many users can connect to it simultaneously and work), thus [Linux user management](https://www.tecmint.com/linux-user-account-management/ "User Account Management") is one of the fundamental tasks of a system administrator, which includes everything from [creating](https://www.tecmint.com/add-users-in-linux/ "Create User in Linux"), [updating](https://www.tecmint.com/usermod-command-examples/ "Modify User in LInux"), and [deleting user accounts](https://www.tecmint.com/delete-remove-a-user-account-with-home-directory-in-linux/ "Delete User Accounts in Linux") or user groups on a Linux system.
In this short quick article, you will learn how to add or remove a user from a group in a Linux system.
## Check a User Group in Linux
To find out what group a user is in, just run the following `groups` command and provide the **username** (**tecmint** in this example) as an argument.
```
# groups tecmint

**tecmint : tecmint wheel**

```

To find out the group of root user in Linux, just run the `groups` command without any argument.
```
# group

**root**

```
![Check a User Group in Linux](https://www.tecmint.com/wp-content/uploads/2020/09/Check-User-Group-in-Linux.png) Check a User Group in Linux
## Add a User to a Group in Linux
Before trying to add a user to a **group** , ensure that the user exists on the system. To add a user to a certain group, use the [usermod command](https://www.tecmint.com/usermod-command-examples/ "Usermod Command Examples") with the `-a` flag which tells the **usermod** to add a user to the supplementary group(s), and the `-G` option specifies the actual groups in the following format.
In this example, **tecmint** is the username and **postgres** is the group name:
```
# usermod -aG **postgres** tecmint
# groups tecmint

```
![Add User to Group in Linux](https://www.tecmint.com/wp-content/uploads/2020/09/Add-User-to-Group-in-Linux.png) Add User to Group in Linux
## Remove a User from a Group in Linux
To remove a user from a group, use the **gpasswd** command with the `-d` option as follows.
```
# gpasswd -d tecmint postgres
# groups tecmint

```
![Remove User from Group in Linux](https://www.tecmint.com/wp-content/uploads/2020/09/Remove-User-from-Group-in-Linux.png)Remove User from Group in Linux
Additionally, on [Ubuntu and its derivatives](https://www.tecmint.com/ubuntu-based-linux-distributions/ "Ubuntu-Based Linux Distributions"), you can remove a user from a specific group using the `deluser` command as follows (where **tecmint** is the username and **postgres** is the group name).
```
$ sudo deluser tecmint postgres

```

For more information, see the man pages for each of the different commands we have used in this article.
```
$ man groups
$ man usermod
$ man gpasswd
$ man deluser

```

You will also find the following user management guides very useful:
  * [3 Ways to Change a Users Default Shell in Linux](https://www.tecmint.com/change-a-users-default-shell-in-linux/ "Change User Shell in Linux")
  * [How to Monitor Linux Commands Executed by System Users in Real-time](https://www.tecmint.com/monitor-linux-commands-executed-by-system-users-in-real-time/ "Monitor Linux User Commands")
  * [whowatch – Monitor Linux Users and Processes in Real-Time](https://www.tecmint.com/whowatch-monitor-linux-users-and-processes-in-real-time/ "Monitor Linux User Processes")
  * [How to Create Multiple User Accounts in Linux](https://www.tecmint.com/create-multiple-user-accounts-in-linux/ "How to Create Multiple User Accounts in Linux")
  * [How to Force User to Change Password at Next Login in Linux](https://www.tecmint.com/force-user-to-change-password-next-login-in-linux/ "How to Force User to Change Password at Next Login in Linux")
  * [How to Manage User Password Expiration and Aging in Linux](https://www.tecmint.com/manage-user-password-expiration-and-aging-in-linux/ "How to Manage User Password Expiration and Aging in Linux")
  * [How to Lock User Accounts After Failed Login Attempts](https://www.tecmint.com/lock-user-accounts-after-failed-login-attempts-in-linux/ "How to Lock User Accounts After Failed Login Attempts")


💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[15 Useful Performance and Network Monitoring Tools for Linux](https://www.tecmint.com/linux-performance-monitoring-tools/)
Next article:
[How to Run Linux Commands in Background and Detach in Terminal](https://www.tecmint.com/run-linux-command-in-background/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/add-or-remove-user-from-group-in-linux/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/add-or-remove-user-from-group-in-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/add-or-remove-user-from-group-in-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
