[Skip to content](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/)
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
  * [Pro Courses](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/)
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
  * [Pro Courses](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/)
# bmon – A Powerful Network Bandwidth Monitoring and Debugging Tool for Linux
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: February 3, 2017 Read Time: 4 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [7 Comments](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comments)
**bmon** is a simple yet powerful, text-based [network monitoring and debugging tool](https://www.tecmint.com/bcc-best-linux-performance-monitoring-tools/) for Unix-like systems, which captures networking related statistics and displays them visually in a human friendly format. It is a reliable and effective real-time bandwidth monitor and rate estimator.
It can read input using an assortment of input modules and presents output in various output modes, including an interactive curses user interface as well as a programmable text output for scripting purposes.
**Suggested Read:** [20 Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)
### Install bmon Bandwidth Monitoring Tool in Linux
Almost all Linux distributions has **bmon** package in the default repositories and can be easily install from default package manger, but the available version might be little older.
```
$ sudo yum install bmon      [**On RHEL/CentOS/Fedora**]
$ sudo dnf install bmon      [**On Fedora 22+**]
$ sudo apt-get install bmon  [**On Debian/Ubuntu/Mint**]

```

Alternatively, you can get `.rpm` and `.deb` packages for your Linux distribution from
If you wanted to have a most recent version of **bmon** (i.e version **4.0**), you need to build it from source using following commands.
#### On CentOS, RHEL and Fedora
```
$ git clone https://github.com/tgraf/bmon.git
$ cd bmon
$ sudo yum install make libconfuse-devel libnl3-devel libnl-route3-devel ncurses-devel
$ sudo ./autogen.sh
$ sudo./configure
$ sudo make
$ sudo make install

```

#### On Debian, Ubuntu and Linux Mint
```
$ git clone https://github.com/tgraf/bmon.git
$ cd bmon
$ sudo apt-get install build-essential make libconfuse-dev libnl-3-dev libnl-route-3-dev libncurses-dev pkg-config dh-autoreconf
$ sudo ./autogen.sh
$ sudo ./configure
$ sudo make
$ sudo make install

```

### How to Use bmon Bandwidth Monitoring Tool in Linux
Run it as below (for starters: **RX** means received bytes per second and **TX** refers to transmitted bytes per second):
```
$ bmon

```

![bmon - Linux Bandwidth Monitoring](https://www.tecmint.com/wp-content/uploads/2017/02/bmon-Linux-Bandwidth-Monitoring.gif)
To view more detailed graphical statistics/information of bandwidth usage, press `d` key and refer screnshot below.
![bmon - Detailed Bandwidth Statistics](https://www.tecmint.com/wp-content/uploads/2017/02/bmon-Detailed-Bandwidth-Statistics.gif)
Press `[Shift + ?]` to view the quick reference below. To exit the interface, press **[Shift + ?]** again.
![bmon - Quick Reference](https://www.tecmint.com/wp-content/uploads/2017/02/bmon-Quick-Reference.png)bmon – Quick Reference
To view statistics of a given interface, select it using the `Up` and `Down` arrows. However, to monitor a specific interface only, specify it as an argument on the command line as follows.
**Suggested Read:** [13 Tools to Monitor Linux Performance](https://www.tecmint.com/linux-performance-monitoring-tools/)
The flag `-p` sets a policy defining which network interfaces to display, in the example below, we will be monitoring the `enp1s0` network interface:
```
$ bmon -p enp1s0

```
![bmon - Monitor Ethernet Bandwidth](https://www.tecmint.com/wp-content/uploads/2017/02/bmon-Monitor-Ethernet-Bandwidth.png)bmon – Monitor Ethernet Bandwidth
To use **bit per second** instead of **bytes per second** , use the `-b` flag like so:
```
$ bmon -bp enp1s0

```

We can also define the intervals per second with the `-r` flag as follows:
```
$ bmon -r 5 -p enp1s0

```

### How to Use bmon Input Modules
**bmon** has a number of input modules that offer statistical data about interfaces, which includes:
  1. **netlink** – employs the Netlink protocol to collect interface and traffic control statistics from the kernel. This is the default input module.
  2. **proc** — reads interface statistics from the **/proc/net/dev** file. It is considered a legacy interface and offered for backwards compatibly. It is a fallback module in case the Netlink interface is not available.
  3. **dummy** – this is a programmable input module for debugging and testing purposes.
  4. **null** – disables data collection.


To find additional info about a module, invoke the it with the “**help** ” option set as follows:
```
$ bmon -i netlink:help

```

The next command will invoke **bmon** with the **proc** input module enabled:
```
$ bmon -i proc -p enp1s0

```

### How to Use bmon Output Modules
**bmon** also uses output modules to display or export the statistical data collected by the input modules above, which includes:
  1. **curses** – this is an interactive curses based text user interface, it offers real time rate estimations and a graphical representation of each attribute. It is the default output mode.
  2. **ascii** – is a straightforward programmable text output meant for human consumption. It can display list of interfaces, detailed counters and graphs to the console. It is the default fallback output mode when curses is not available.
  3. **format** – is a fully scriptable output mode, it’s meant for consumption by other programs-meaning we can use its output values at a later time in scripts or programs for analysis and more.
  4. **null** – this disables output.


To get more info concerning a module, run the it with the “**help** ” flag set like so:
```
$ bmon -o curses:help

```

The command that follows will invoke **bmon** in **ascii** output mode:
```
$ bmon -p enp1s0 -o ascii

```
![bmon - Ascii Output Mode](https://www.tecmint.com/wp-content/uploads/2017/02/bmon-Ascii-Output-Mode.png)bmon – Ascii Output Mode
We can run the format output module as well, then use the values obtained for scripting or in another program:
```
$ bmon -p enp1s0 -o format

```
![bmon - Format Output Mode](https://www.tecmint.com/wp-content/uploads/2017/02/bmon-format-output-mode.png)bmon – Format Output Mode
For additional usage info, options and examples, read the **bmon** man page:
```
$ man bmon

```

Visit the bmon Github repository:
That’s all for now, test the various features of **bmon** in different scenarios and share your thoughts about it with us via the comment section below.
Tags [linux monitoring](https://www.tecmint.com/tag/linux-monitoring/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Configure Custom SSH Connections to Simplify Remote Access](https://www.tecmint.com/configure-custom-ssh-connection-in-linux/)
Next article:
[How to Configure Network Between Guest VM and Host in Oracle VirtualBox](https://www.tecmint.com/network-between-guest-vm-and-host-virtualbox/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#respond)** or
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
[Leave a Reply](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/0cdebc5704c67c880165130c0c6f0a3ff962d2a518dfee8962b4b4a16bf6260a?s=50&d=blank&r=g)
Jesse Thiam
[ June 8, 2022 at 11:25 am  ](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-1820086)
Hi is there any way I can embed or view it as html/php via web browser instead of viewing it on the terminal of Linux? Thank you for your answers…
[Reply](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-1820086)
  2. ![](https://secure.gravatar.com/avatar/b28e027955e95b3c20f710207f776ae528d88a28426a3f561d0ec1809e56dde3?s=50&d=blank&r=g)
Guy Boisvert
[ November 26, 2018 at 5:56 pm  ](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-1067468)
This tool seems to be very good! The only thing i find strange is that the detailed view seems to only show IPv6 stats (there’s only IP6 in the detailed list). Where is IPv4 (main event here!!) ? Checked man pages, googled around to no avail. I’m using Ubuntu 18.04.
[Reply](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-1067468)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ November 27, 2018 at 11:14 pm  ](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-1069144)
@Guy
Thanks for sharing your concern with us, you can post this question to the developer at:
[Reply](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-1069144)
  3. ![](https://secure.gravatar.com/avatar/23c8df05456984c5d5cace744a8ba9ad46fc1c886e76bb8590b8e0f92d96c0e9?s=50&d=blank&r=g)
harish
[ February 8, 2017 at 3:26 pm  ](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-865519)
Hi,
I am facing issues about nagios users for viewing particular host and services. please help me how i can create user in nagios core and dedicate host to that user
[Reply](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-865519)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ February 9, 2017 at 1:28 pm  ](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-865839)
@harish
Follow the steps below:
1- Start by creating new contact definitions for your client, for example: contact_name user1.
2- Then create contact groups or you can add the new contact for you existing group, depending on the checks that you want to permit.
3- Closely use the new Contact Group with customers email and your main admin. Note you can either use existing Host Groups or create new HostGroups if you choose to.
4- Finally, add htaccess user to your htpasswd file (htpasswd.users), it important that the username matches the name on your Contact(user1).
Hope this gives your a rough idea of what to do.
[Reply](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-865839)
  4. ![](https://secure.gravatar.com/avatar/4daf4414ed04740d9b99fb56b3a9e0c4fa27a90efe9c61df3f5b9b029cb7286c?s=50&d=blank&r=g)
batchen
[ February 5, 2017 at 2:37 pm  ](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-864774)
I got a lot of errors when installing on centos. I got my error fixed installing this missing packages:
```
# yum install git autoconf automake gcc

```
[Reply](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-864774)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ February 7, 2017 at 3:00 pm  ](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-865196)
@batchen
Many thanks for the feedback, this will be so useful to other CentOS users.
[Reply](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#comment-865196)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/#respond)
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
[How to Use Wget Command in Linux with Examples](https://www.tecmint.com/10-wget-command-examples-in-linux/)
[How To Create A File In Linux: Echo, Touch, Tee and Cat Commands](https://www.tecmint.com/create-file-linux/)
[How to Append a Line After a String in a File Using sed Command](https://www.tecmint.com/sed-add-a-line-after-string-in-file/)
[How to Convert From RPM to DEB and DEB to RPM Package Using Alien](https://www.tecmint.com/convert-from-rpm-to-deb-and-deb-to-rpm-package-using-alien/)
[How to Use Chown Command to Change File Ownership [11 Examples]](https://www.tecmint.com/chown-command-examples/)
[How to Install Zip and Unzip in Linux](https://www.tecmint.com/install-zip-and-unzip-in-linux/)
## Linux Server Monitoring Tools
[How to Monitor Docker Containers with Zabbix Monitoring Tool](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/)
[How to Add Windows Host to Nagios Monitoring Server](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/)
[ntopng – Web-Based Network Traffic and Security Monitoring Tool](https://www.tecmint.com/ntopng-network-traffic-tool/)
[CBM – Shows Network Bandwidth in Ubuntu](https://www.tecmint.com/cbm-shows-network-bandwidth-traffic-in-ubuntu/)
[Collectl: An Advanced All-in-One Performance Monitoring Tool for Linux](https://www.tecmint.com/collectl-linux-performance-reporting-monitoring/)
[screenFetch – An Ultimate System Information Generator for Linux](https://www.tecmint.com/screenfetch-system-information-generator-for-linux/)
## Learn Linux Tricks & Tips
[How to Recover a Deleted File in Linux](https://www.tecmint.com/recover-deleted-file-in-linux/)
[6 Best CLI Tools to Search Plain-Text Data Using Regular Expressions](https://www.tecmint.com/command-line-tools-to-search-strings-or-patterns-in-files/)
[How to Copy File Permissions and Ownership to Another File in Linux](https://www.tecmint.com/copy-file-permissions-and-ownership-to-another-file-in-linux/)
[How to Create a Shared Directory for All Users in Linux](https://www.tecmint.com/create-a-shared-directory-in-linux/)
[How to Compress and Decompress a .bz2 File in Linux](https://www.tecmint.com/linux-compress-decompress-bz2-files-using-bzip2/)
[Add Rainbow Colors to Linux Command Output in Slow Motion](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/)
## Best Linux Tools
[8 Useful GUI Email Clients for Linux Desktop](https://www.tecmint.com/linux-desktop-email-clients/)
[8 Best IRC Clients for Linux in 2024](https://www.tecmint.com/best-irc-clients-for-linux/)
[7 Best Calendar Apps for Linux Desktop in 2024](https://www.tecmint.com/best-calendar-apps-linux-desktop/)
[11 Best Self-Hosted Alternatives to Google Photos](https://www.tecmint.com/google-photos-alternatives/)
[Top 5 Open-Source OCR Tools for Linux in 2025](https://www.tecmint.com/best-linux-ocr-tools/)
[7 Best Email Clients for Linux Systems](https://www.tecmint.com/best-email-clients-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/ "Scroll back to top")
Search for:
