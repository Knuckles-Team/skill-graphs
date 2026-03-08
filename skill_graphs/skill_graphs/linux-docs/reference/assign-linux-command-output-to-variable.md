[Skip to content](https://www.tecmint.com/assign-linux-command-output-to-variable/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/assign-linux-command-output-to-variable/ "Linux Online Courses")
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


[](https://www.tecmint.com/assign-linux-command-output-to-variable/)
When you run a command, it produces some kind of output: either the result of a program is suppose to produce or status/error messages of the program execution details. Sometimes, you may want to store the output of a command in a variable to be used in a later operation.
In this post, we will review the different ways of assigning the output of a shell command to a variable, specifically useful for shell scripting purpose.
To store the output of a command in a variable, you can use the shell command substitution feature in the forms below:
```
variable_name=$(command)
variable_name=$(command [option ...] arg1 arg2 ...)
OR
variable_name='command'
variable_name='command [option ...] arg1 arg2 ...'

```

Below are a few examples of using command substitution.
In this first example, we will store the value of `who` (which shows who is logged on the system) command in the variable `CURRENT_USERS` user:
```
$ CURRENT_USERS=$(who)

```

Then we can use the variable in a sentence displayed using the [echo command](https://www.tecmint.com/echo-command-in-linux/) like so:
```
$ echo -e "The following users are logged on the system:\n\n $CURRENT_USERS"

```

In the command above: the flag `-e` means interpret any escape sequences ( such as `\n` for newline) used. To avoid wasting time as well as memory, simply perform the command substitution within the [echo command](https://www.tecmint.com/echo-command-in-linux/) as follows:
```
$ echo -e "The following users are logged on the system:\n\n $(who)"

```
![Shows Current Logged Users in Linux](https://www.tecmint.com/wp-content/uploads/2017/01/Shows-Current-Logged-Users-in-Linux.png)Shows Current Logged Users in Linux
Next, to demonstrate the concept using the second form; we can store the total number of files in the current working directory in a variable called `FILES` and **echo** it later as follows:
```
$ FILES=`sudo find . -type f -print | wc -l`
$ echo "There are $FILES in the current working directory."

```
![Show Number of Files in Directory](https://www.tecmint.com/wp-content/uploads/2017/01/Show-Number-of-Files-in-Directory.png)Show Number of Files in Directory
That’s it for now, in this article, we explained the methods of assigning the output of a shell command to a variable. You can add your thoughts to this post via the feedback section below.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Deal: Get Full Stack Programmer Bundle (97% Off)](https://www.tecmint.com/computer-science-programming-course/)
Next article:
[Deal: Learn Professional Certified Data Science with Python Course (90% Off)](https://www.tecmint.com/learn-data-science-python-course/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/assign-linux-command-output-to-variable/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### 10 Comments
[Leave a Reply](https://www.tecmint.com/assign-linux-command-output-to-variable/#reply-title)
  1. In my case it does not work for:
```
currentModule=$(module list python)
echo "Current loaded module is $currentModule"

```
[Reply](https://www.tecmint.com/assign-linux-command-output-to-variable/#comment-1755122)
     * The command **module list python** writes to the command line:
Currently Loaded Modules Matching: python/3.7.4
[Reply](https://www.tecmint.com/assign-linux-command-output-to-variable/#comment-1755123)
  2. You missed process substitution. For example: read uid gid < <(grep ^root /etc/passwd | awk -F: '{print $3 " " $4}') This allows you to set 2 or more variables if you mant.
[Reply](https://www.tecmint.com/assign-linux-command-output-to-variable/#comment-863470)
     * @Micheal
Yap, how did i forget to mention this, it’s so helpful while writing scripts. Thanks for the reminder.
[Reply](https://www.tecmint.com/assign-linux-command-output-to-variable/#comment-863535)
  3. Why is $(…) preferred over `…` (backticks):

[Reply](https://www.tecmint.com/assign-linux-command-output-to-variable/#comment-860898)
     * @Anonymous
Many thanks for providing this useful link.
[Reply](https://www.tecmint.com/assign-linux-command-output-to-variable/#comment-861013)
       * From the link Above “The backtick is also easily confused with a single quote.”
This happened in this article for the first figure.
```
...
OR
variable_name='command'
variable_name='command [option ...] arg1 arg2 ...'
...

```
[Reply](https://www.tecmint.com/assign-linux-command-output-to-variable/#comment-1329708)
         * @Depressing
True, it was a typo during publishing. We will modify the article as soon as possible. Thanks for the feedback.
[Reply](https://www.tecmint.com/assign-linux-command-output-to-variable/#comment-1330387)
  4. Is there a way to store the result of the command ONLY if there is no error during the command ?
[Reply](https://www.tecmint.com/assign-linux-command-output-to-variable/#comment-860837)
     * @Hedy
That is exactly what we explained in the article. To separate the result of a command from error messages, you can perform output/error redirection to files other than the screen. Then read the result from the file.
Read more about output redirection from here: <https://www.tecmint.com/linux-io-input-output-redirection-operators/>
[Reply](https://www.tecmint.com/assign-linux-command-output-to-variable/#comment-861011)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/assign-linux-command-output-to-variable/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/assign-linux-command-output-to-variable/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
