[Skip to content](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/)
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
  * [Pro Courses](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/ "Linux Online Courses")
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


[](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/)
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
  * [Pro Courses](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/ "Linux Online Courses")
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


[](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/)
# A Shell Script to Send Email Alert When Memory Gets Low
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: November 29, 2017 Read Time: 3 minsCategories [Bash Shell](https://www.tecmint.com/category/bash-shell/), [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [18 Comments](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comments)
A powerful aspect of Unix/Linux shell programs such as **bash** , is their amazing support for common programming constructs that enable you to make decisions, execute commands repeatedly, create new functions, and so much more. You can write commands in a file known as a shell script and execute them collectively.
This offers you a reliable and effective means of system administration. You can write [scripts to automate tasks](https://www.tecmint.com/using-shell-script-to-automate-linux-system-maintenance-tasks/), for instance daily back ups, system updates etc; create new custom commands/utilities/tools and beyond. You can write scripts to help you keep up with what’s unfolding on a server.
One of the critical components of a server is memory (**RAM**), it greatly impacts on overall performance of a system.
In this article, we will share a small but useful shell script to send an alert email to one or more system administrator(s), if server memory is running low.
This is script is particularly useful for keeping an eye on **Linux VPS** (**Virtual Private Servers**) with small amount of memory, say of about **1GB** (approximately **990MB**).
#### Testing Environment Setup
  1. A **CentOS/RHEL 7** production server with **mailx** utility installed with working [postfix mail server](https://www.tecmint.com/setup-postfix-mail-server-and-dovecot-with-mariadb-in-centos/).


This is how the **alertmemory.sh** script works: first it checks the free memory size, then determines if amount of free memory is less or equal to a specified size (**100** MB for the purpose of this guide), used as a bench mark for the least acceptable free memory size.
If this condition is true, it will generate a list of the [top 10 processes consuming server RAM](https://www.tecmint.com/find-linux-processes-memory-ram-cpu-usage/) and sends an alert email to specified email addresses.
**Note** : You will have to make a few changes to script (especially the mail sender utility, use the appropriate flags) to meet your Linux distributions requirements.
Shell Script to Check Server Memory
```
#!/bin/bash
#######################################################################################
#Script Name    :alertmemory.sh
#Description    :send alert mail when server memory is running low
#Args           :
#Author         :Aaron Kili Kisinga
#Email          :aaronkilik@gmail.com
#License       : GNU GPL-3
#######################################################################################
## declare mail variables
##email subject
subject="**Server Memory Status Alert**"
##sending mail as
from="**server.monitor@example.com**"
## sending mail to
to="**admin1@example.com**"
## send carbon copy to
also_to="**admin2@example.com**"

## get total free memory size in megabytes(MB)
free=$(free -mt | grep Total | awk '{print $4}')

## check if free memory is less or equals to  **100MB**
if [[ "$free" -le **100**  ]]; then
        ## get top processes consuming system memory and save to temporary file
        ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head >/tmp/top_proccesses_consuming_memory.txt

        file=/tmp/top_proccesses_consuming_memory.txt
        ## send email if system memory is running low
        echo -e "Warning, server memory is running low!\n\nFree memory: $free MB" | mailx -a "$file" -s "$subject" -r "$from" -c "$to" "$also_to"
fi

exit 0

```

After creating your script **/etc/scripts/alertmemory.sh** , make it executable and symlink to cron.hourly.
```
# chmod +x /etc/scripts/alertmemory.sh
# ln -s -t /etc/cron.hourly/alertmemory.sh /etc/scripts/alertmemory.sh

```

This means that the above script will be run after every 1 hour as long as the server is running.
**Tip** : You can test if it is working as intended, set the bench mark value a little high to easily trigger an email to be sent, and specify a small interval of about 5 minutes.
Then keep on checking from the command line using the [free command](https://www.tecmint.com/check-memory-usage-in-linux/) provided in the script. Once you confirm that it is working, define the actual values you would like to use.
Below is a screenshot showing a sample alert email.
![Linux Memory Email Alert](https://www.tecmint.com/wp-content/uploads/2017/11/Linux-Memory-Email-Alert.png)Linux Memory Email Alert
That’s all! In this article, we explained how to use shell script to send alert emails to system administrators in case server memory (RAM) is running low. You can share any thoughts relating to this topic, with us via the feedback form below.
Tags [shell scripting](https://www.tecmint.com/tag/shell-scripting/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[4 Ways to Speed Up SSH Connections in Linux](https://www.tecmint.com/speed-up-ssh-connections-in-linux/)
Next article:
[How to Check Integrity of File and Directory Using “AIDE” in Linux](https://www.tecmint.com/check-integrity-of-file-and-directory-using-aide-in-linux/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#respond)** or
## Related Posts
[![bash vs zsh vs fish](https://www.tecmint.com/wp-content/uploads/2013/11/bash-vs-zsh-vs-fish.webp)](https://www.tecmint.com/bash-vs-zsh-vs-fish/ "Terminal Showdown: Bash vs Zsh vs Fish for Power Users")
[Terminal Showdown: Bash vs Zsh vs Fish for Power Users](https://www.tecmint.com/bash-vs-zsh-vs-fish/)
[![Calculating Mathematical Expressions in Bash](https://www.tecmint.com/wp-content/uploads/2013/09/bash-math-operations.webp)](https://www.tecmint.com/mathematical-operations-in-shell-scripting/ "Calculating Mathematical Expressions in Shell Scripting – Part 5")
[Calculating Mathematical Expressions in Shell Scripting – Part 5](https://www.tecmint.com/mathematical-operations-in-shell-scripting/)
[![rbash - Restricted Bash Shell](https://www.tecmint.com/wp-content/uploads/2014/01/rbash-restricted-bash-shell.webp)](https://www.tecmint.com/rbash-restricted-bash-shell/ "rbash – A Restricted Bash Shell Explained with Practical Examples")
[rbash – A Restricted Bash Shell Explained with Practical Examples](https://www.tecmint.com/rbash-restricted-bash-shell/)
[![Learn Basic Mathematical Operations in Bash](https://www.tecmint.com/wp-content/uploads/2024/07/Basic-Mathematical-Operations-in-Bash.png)](https://www.tecmint.com/basic-mathematical-operations-in-bash/ "Learn Basic Mathematical Operations in Bash Scripting – Part IV")
[Learn Basic Mathematical Operations in Bash Scripting – Part IV](https://www.tecmint.com/basic-mathematical-operations-in-bash/)
[![Learn Practical BASH Scripting](https://www.tecmint.com/wp-content/uploads/2024/02/Learn-Practical-BASH-Scripting.png)](https://www.tecmint.com/sailing-through-the-world-of-linux-bash-scripting-part-iii/ "Learn Practical BASH Scripting Projects – Part III")
[Learn Practical BASH Scripting Projects – Part III](https://www.tecmint.com/sailing-through-the-world-of-linux-bash-scripting-part-iii/)
[![Linux Server Health Script](https://www.tecmint.com/wp-content/uploads/2013/07/Linux-Server-Health-Script.png)](https://www.tecmint.com/basic-shell-programming-part-ii/ "5 Useful Shell Scripts for Linux Newbies – Part II")
[5 Useful Shell Scripts for Linux Newbies – Part II](https://www.tecmint.com/basic-shell-programming-part-ii/)
### 18 Comments
[Leave a Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/b3db5179850f1a344dde82d038d9f4fb5d6de09f98ff640fb433df1930e9add9?s=50&d=blank&r=g)
Addy
[ February 21, 2023 at 9:57 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1969758)
Hi,
I need a script for an Email Alert when the Productin MQ configuration changes to Active-Active instead of Active-Passive.
Help Appreciated.
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1969758)
  2. ![](https://secure.gravatar.com/avatar/ec9be0f6696ce0746c8b3c4750bd0281017f001b0f2d0bfdca8468b50db8ca3e?s=50&d=blank&r=g)
hari
[ February 1, 2023 at 10:29 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1955595)
Hi,
I need a script for when the server got shutdown and startup we get an email alert.
Kindly help with anyone.
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1955595)
  3. ![](https://secure.gravatar.com/avatar/1b7be388225dadb08cf4e8f8dc83cbe6da2a363cabbe929a46165dc8e84ecc30?s=50&d=blank&r=g)
divya
[ December 10, 2021 at 1:56 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1675154)
I have to send a mail if the utilization percentage is greater than 90.
can you please tell me how?
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1675154)
     * ![](https://secure.gravatar.com/avatar/10f5e702f389716091649eccf14496151a3c51f3b7069402d564323127ac45fc?s=50&d=blank&r=g)
Padma
[ January 12, 2022 at 1:28 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1699907)
Hi, I have the same requirement, can someone help me with this?
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1699907)
       * ![](https://secure.gravatar.com/avatar/10f5e702f389716091649eccf14496151a3c51f3b7069402d564323127ac45fc?s=50&d=blank&r=g)
Padma
[ January 12, 2022 at 1:32 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1699908)
I want to get an email if one of my processors is using 90 percent of memory from the allocated heap memory. For example, I have a process **Headset: -Xmx4096m** (heap memory). As soon as it reaches 90% of the allocated heap memory, I need to get an email.
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1699908)
  4. ![](https://secure.gravatar.com/avatar/f7022f5bef1532e6497586a256f2790b1820a1063db1ab47f4c6b8ad622c8acf?s=50&d=blank&r=g)
uday
[ February 19, 2021 at 4:24 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1437362)
Hi Aaron,
Does this script supports even DL’s or only restricted to email.
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1437362)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ February 23, 2021 at 12:26 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1439128)
@uday
It only supports email but you can modify it to suit your use case.
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1439128)
  5. ![](https://secure.gravatar.com/avatar/402244f6a302251ed30698cf7b615ab55361a03b6c49693e8bb83412972ec522?s=50&d=blank&r=g)
Thomas
[ December 8, 2020 at 10:23 am  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1399124)
This script will just be executed every hour, not when your Memory is running low…
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1399124)
  6. ![](https://secure.gravatar.com/avatar/984e873edac119531ba794b8ef5a318ebea8e99dbd26ef0a47e0944933673479?s=50&d=blank&r=g)
Sachin
[ July 26, 2020 at 12:18 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1347654)
Create a job it would check component if server down to send the email admin or someone
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1347654)
  7. ![](https://secure.gravatar.com/avatar/c7a8bc3dfdbb8c02f5bc6bb88c638dfd5ab8d2a159fa309bb4e7264202b680dd?s=50&d=blank&r=g)
Ronnie Redd
[ November 18, 2018 at 12:53 am  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1060743)
mailx doesn’t send the file?
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1060743)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ November 20, 2018 at 1:53 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1062026)
@Ronnie
Try to troubleshoot to find out why mailx is not sending the file, or configure another mail client in the script.
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1062026)
  8. ![](https://secure.gravatar.com/avatar/0064176a78f271211647cbd05ee353fb13474fe2aded39a11ac6ec2dbd3911a2?s=50&d=blank&r=g)
Jaro
[ November 30, 2017 at 6:35 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-942537)
Thank You, Aaron! An idea for next article: how to create separate php log file and send it by email as attachment every day.
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-942537)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ December 2, 2017 at 3:15 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-943483)
@Jaro
Welcome, thanks for giving us a topic to research about, i will surely work on this.
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-943483)
  9. ![](https://secure.gravatar.com/avatar/e9337c65d5f1122bfcd4e4c04cad97e194012eabf41121b588ff715c756437e9?s=50&d=blank&r=g)
houghi
[ November 30, 2017 at 1:57 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-942442)
Instead of placing the script in /etc, place it in /usr/local/bin or $HOME/bin as a user or /usr/local/sbin if you are root.
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-942442)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ November 30, 2017 at 3:07 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-942473)
@houghi
Thanks for the recommendation, we will consider doing this in future guides.
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-942473)
  10. ![](https://secure.gravatar.com/avatar/13ea45c20430788c9f5edf15bdbe524380fb197ab6d511d8723856576e815686?s=50&d=blank&r=g)
HZ
[ November 30, 2017 at 12:51 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-942423)
This:
```
free=$(free -mt | grep Total | awk '{print $4}')

```

is a really ugly solution. If you want to filter a text and do something with the filtered values in awk/perl/etc, don’t use grep!
Try something like this, please:
```
free=$(free -mt | awk '/Total/{ print $4 }' )

```
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-942423)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ November 30, 2017 at 3:06 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-942472)
@HZ
Oh yeah. Many thanks for this useful tip.
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-942472)
     * ![](https://secure.gravatar.com/avatar/dafb1cb88c10f5a69118854a52b6efe98572acdb2bec1895082f6cebc864fad6?s=50&d=blank&r=g)
01101001b
[ August 4, 2018 at 9:38 pm  ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1020749)
“a really ugly solution”? Please, don’t exaggerate. Let’s say instead you don’t like it. Your solution is a bit cleaner (I’ll give you that) but not much else.
[Reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#comment-1020749)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/#respond)
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
[Fping – A High Performance Ping Tool for Linux](https://www.tecmint.com/ping-multiple-linux-hosts-using-fping/)
[12 Useful Commands For Filtering Text for Effective File Operations in Linux](https://www.tecmint.com/linux-file-operations-commands/)
[fuser – Find and Kill Processes by File, Directory, or Port](https://www.tecmint.com/fuser-find-monitor-kill-linux-processes/)
[How to Split Large ‘tar’ Archive into Multiple Files of Certain Size](https://www.tecmint.com/split-large-tar-into-multiple-files-of-certain-size/)
[Understanding APT, APT-Cache and Their Frequently Used Commands](https://www.tecmint.com/apt-get-and-apt-cache-and-their-frequently-used-commands/)
[Most Commonly Used Linux Commands You Should Know](https://www.tecmint.com/most-used-linux-commands/)
## Linux Server Monitoring Tools
[Collectl: An Advanced All-in-One Performance Monitoring Tool for Linux](https://www.tecmint.com/collectl-linux-performance-reporting-monitoring/)
[ngxtop – Monitor Nginx Log Files in Real Time in Linux](https://www.tecmint.com/ngxtop-monitor-nginx-log-files-in-real-time-in-linux/)
[Amplify – NGINX Monitoring Made Easy](https://www.tecmint.com/amplify-nginx-monitoring-tool/)
[Install Nagios Core on openSUSE 15.3 Linux](https://www.tecmint.com/install-nagios-opensuse/)
[ngrep – A Network Packet Analyzer for Linux](https://www.tecmint.com/ngrep-network-packet-analyzer-for-linux/)
[How to Install Nagios XI on Ubuntu 22.04](https://www.tecmint.com/install-nagios-xi-on-ubuntu/)
## Learn Linux Tricks & Tips
[How to Create Multiple User Accounts in Linux](https://www.tecmint.com/create-multiple-user-accounts-in-linux/)
[How to Clone a Partition or Hard drive in Linux](https://www.tecmint.com/clone-linux-partitions/)
[How to Change Default Apache ‘DocumentRoot’ Directory in Linux](https://www.tecmint.com/change-root-directory-of-apache-web-server/)
[How to Delete HUGE (100-200GB) Files in Linux](https://www.tecmint.com/delete-huge-files-in-linux/)
[How to Force User to Change Password at Next Login in Linux](https://www.tecmint.com/force-user-to-change-password-next-login-in-linux/)
[12 Ways to Find User Account Info and Login Details in Linux](https://www.tecmint.com/check-user-in-linux/)
## Best Linux Tools
[4 Best Tools for Creating Fillable PDF Forms on Linux](https://www.tecmint.com/create-pdf-forms-linux/)
[5 Open Source Log Monitoring and Management Tools for Linux](https://www.tecmint.com/best-linux-log-monitoring-and-management-tools/)
[7 Best Audio and Video Players for Gnome Desktop](https://www.tecmint.com/best-video-players-for-gnome-desktop/)
[5 GUI Tools to Free Up Space on Debian, Ubuntu and Linux Mint](https://www.tecmint.com/free-disk-space-ubuntu-linux-mint/)
[15 Best Open Source Music Making Software for Linux in 2024](https://www.tecmint.com/free-music-creation-or-audio-editing-softwares-for-linux/)
[10 Tools to Make Bootable USB Drive from ISO in 2026](https://www.tecmint.com/linux-bootable-usb-creators/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/shell-script-to-send-email-alert-when-memory-low/ "Scroll back to top")
Search for:
