# Cockpit – A Powerful Tool to Monitor and Administer Multiple Linux Servers via Browser
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: November 5, 2021 Read Time: 4 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [45 Comments](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comments)
**Cockpit** is an easy-to-use, lightweight, and simple yet powerful remote manager for GNU/Linux servers, it’s an interactive server administration user interface that offers a live Linux session via a web browser.
It can run on several [RHEL-based Linux distributions](https://www.tecmint.com/redhat-based-linux-distributions/ "The Best RedHat-based Linux Distributions") and [Debian derivatives](https://www.tecmint.com/debian-based-linux-distributions/ "Best Debian-based Linux Distributions") including **Ubuntu** , **Linux Mint** , **Fedora** , **CentOS** , **Rocky Linux** , **AlmaLinux** , **Arch Linux** among others.
**Cockpit** makes Linux discoverable thereby enabling system administrators to easily and reliably carry out tasks such as starting containers, managing storage, network configurations, log inspections coupled with several others.
**[ You might also like:[20 Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/ "Linux Performance Monitoring Tools") ]**
While using it, users can easily switch between the [Linux terminal and web browser](https://www.tecmint.com/access-linux-server-terminal-in-web-browser-using-wetty/) without any hustles. Importantly, when a user starts a service via **Cockpit** , it can be stopped via the terminal, and just in case of an error that occurs in the terminal, it is shown in the Cockpit journal interface.
#### Features of Cockpit:
  * Enables managing of multiple servers in one Cockpit session.
  * Offers a web-based shell in a terminal window.
  * Containers can be managed via [Docker](https://www.tecmint.com/install-docker-and-learn-containers-in-centos-rhel-7-6/).
  * Supports efficient [management of system user accounts](https://www.tecmint.com/manage-users-and-groups-in-linux/).
  * Collects system performance information using the Performance Co-Pilot framework and displays it in a graph.
  * Supports gathering of system configuration and diagnostic information using sos-report.
  * Also supports a Kubernetes cluster or an Openshift v3 cluster.
  * Allows modification of network settings and many more.


### How to Install Cockpit in Linux Systems
You can install **Cockpit** in all Linux distributions from their default official repositories as shown:
#### Install Cockpit on Fedora and CentOS
To install and enable **Cockpit** on Fedora distributions, use the following commands.
```
# yum install cockpit
# systemctl enable --now cockpit.socket
# firewall-cmd --add-service=cockpit
# firewall-cmd --add-service=cockpit --permanent
# firewall-cmd --reload

```

#### Install Cockpit on Rocky Linux and AlmaLinux
To install and enable **Cockpit** on Rocky/AlmaLinux distributions, use the following commands.
```
# yum install cockpit
# systemctl enable --now cockpit.socket
# firewall-cmd --add-service=cockpit
# firewall-cmd --add-service=cockpit --permanent
# firewall-cmd --reload

```

#### Install Cockpit on RHEL
**Cockpit** is added to the Red Hat Enterprise Linux Extras repository from versions **7.1** and later:
```
# yum install cockpit
# systemctl enable --now cockpit.socket
# firewall-cmd --add-service=cockpit --permanent
# firewall-cmd --reload

```

#### Install Cockpit on Debian
The **cockpit** is included in Debian’s official repositories, and you can install it using the following commands.
```
# apt-get update
# apt-get install cockpit
# mkdir -p /usr/lib/x86_64-linux-gnu/udisks2/modules
# ufw allow 9090
# ufw allow 80

```

#### Install Cockpit on Ubuntu and Linux Mint
In Ubuntu and Linux Mint distributions, Cockpit is not included, but you can install it from the official **Cockpit PPA** by executing the following commands:
```
$ sudo add-apt-repository ppa:cockpit-project/cockpit
$ sudo apt-get update
$ sudo apt-get install cockpit
$ sudo systemctl enable --now cockpit.socket

```

#### Install Cockpit on Arch Linux
Arch Linux users can install Cockpit from the **Arch User Repository** using the following command.
```
# yaourt cockpit
# systemctl start cockpit
# systemctl enable cockpit.socket

```

### How to Use Cockpit in Linux
After Cockpit is installed successfully, you can access it using a web browser at the following locations.
```
https://ip-address:9090
OR
https://server.domain.com:9090

```

Enter system username and password to login in the interface below:
![Cockpit Web Interface](https://www.tecmint.com/wp-content/uploads/2016/10/Cockpit-Web-Interface.png)Cockpit Web Interface
After logging in, you will be presented with a summary of your system information and performance graphs for **CPU** , **Memory** , **Disk I/O** , and **Network** traffic as seen in the next image:
![Linux System Performance Summary](https://www.tecmint.com/wp-content/uploads/2016/10/Linux-System-Summary.png)Linux System Performance Summary
Next on the dashboard menu, is **Services**. Here you can view **Targets** , **System Services** , **Sockets** , **Timers,** and **Paths** pages.
The interface below shows running services on your system.
![Showing Current Running Services on Linux](https://www.tecmint.com/wp-content/uploads/2016/10/Showing-Linux-Running-Services.png)Showing Current Running Services on Linux
You can click on a single service to manage it. Simply click on the drop-down menus to get the functionality you want.
![View Linux Service Summary](https://www.tecmint.com/wp-content/uploads/2016/10/View-Linux-Service-Summary-Logs.png)View Linux Service Summary
The **Logs** menu item displays the logs page which allows for logs inspection. The logs are categorized into **Errors** , **Warnings** , **Notices,** and **All** as in the image below.
Additionally, you can as well view logs based on time such as logs for the last 24HRs or 7 days.
**Suggested Read:** [4 Best Log Monitoring and Management Tools for Linux](https://www.tecmint.com/best-linux-log-monitoring-and-management-tools/)
To inspect a single log entry, simply click on it.
![Linux Logs Monitoring](https://www.tecmint.com/wp-content/uploads/2016/10/Monitor-Linux-Logs.png)Linux Logs Monitoring
Cockpit also [enables you to manage user accounts](https://www.tecmint.com/rhcsa-exam-manage-users-and-groups/) on the system, go to **Tools** and click on **Accounts**. Clicking on a user account allows you to view the user’s account details.
![Manage Linux User Accounts](https://www.tecmint.com/wp-content/uploads/2016/10/Manage-Linux-User-Accounts.png)Manage Linux User Accounts
To add a system user, click on the “**Create New Account** ” button and enter the necessary user information in the interface below.
![Create User Account in Linux](https://www.tecmint.com/wp-content/uploads/2016/10/Create-Linux-User-Account.png)Create User Account in Linux
To get a terminal window, go to **Tools** **→** **Terminal**.
![Cockpit - Linux Web Terminal](https://www.tecmint.com/wp-content/uploads/2016/10/Linux-Web-Terminal.png)Cockpit – Linux Web Terminal
### How to Add Linux Server to Cockpit
**Important** : Be aware that you must install Cockpit on all remote Linux servers in order to monitor them on the Cockpit dashboard. So, please install it before adding any new server to Cockpit.
To add another server, click on **dashboard** , you will see the screen below. Click on the `(+)` sign and enter the server IP address. Remember that information for each server you add is displayed in Cockpit using a distinct color.
![Add Linux Server to Cockpit](https://www.tecmint.com/wp-content/uploads/2016/10/Add-Linux-Server-to-Cockpit.png)Add Linux Server to Cockpit ![Cockpit - Remote Linux Server Monitoring](https://www.tecmint.com/wp-content/uploads/2016/10/Cockpit-Remote-Linux-Server-Monitoring.png)Cockpit – Remote Linux Server Monitoring
Same way, you can add many Linux servers under Cockpit and manage them efficiently without any trouble.
That is it for now, however, you can explore more in case you have installed this simple and wonderful server, remote manager.
**Cockpit Official Documentation** :
For any questions or suggestions as well as feedback on the topic, do not hesitate to use the comment section below to get back to us.
Tags [linux monitoring](https://www.tecmint.com/tag/linux-monitoring/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Terminator – A Terminal Emulator to Manage Multiple Terminal Windows on Linux](https://www.tecmint.com/terminator-a-linux-terminal-emulator-to-manage-multiple-terminal-windows/)
Next article:
[How to Install Xubuntu Desktop on Ubuntu 20.04](https://www.tecmint.com/install-xubuntu-desktop-in-ubuntu/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#respond)** or
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
### 45 Comments
[Leave a Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/1c6a989553e68c5277b7f574442c4d54718bd3053b5fc2521e36562f9be646d2?s=50&d=blank&r=g)
Jalal
[ November 6, 2021 at 10:18 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1637370)
Hi,
Thanks a lot
Very nice and useful article.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1637370)
  2. ![](https://secure.gravatar.com/avatar/b573fb30e8d11ec1e5da2dc30855eec8e5f82106978e4ecc2af78217206671bd?s=50&d=blank&r=g)
Moorthy
[ December 25, 2020 at 6:36 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1404525)
I am getting errors while installing the cockpit in CentOS Linux release 7.7.1908 (Core). is it due to a repo issue? kindly advise
Error downloading packages:
cockpit-195.6-1.el7.centos.x86_64: [Errno 256] No more mirrors to try.
cockpit-system-195.6-1.el7.centos.noarch: [Errno 256] No more mirrors to try.
cockpit-ws-195.6-1.el7.centos.x86_64: [Errno 256] No more mirrors to try.
cockpit-bridge-195.6-1.el7.centos.x86_64: [Errno 256] No more mirrors to try.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1404525)
  3. ![](https://secure.gravatar.com/avatar/3d3ef12d1f8ea77e768b53342d5a69869ef68ef554343c3f3c25fce9064ce64a?s=50&d=blank&r=g)
jeff75
[ December 10, 2020 at 12:46 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1399573)
Hello ^^)
just a (dumb ?) question: Why the HTTPS: is slashed red in all the administration views?
could it be that the links aren’t secure at all between the servers and cockpit on the main admin computer?
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1399573)
  4. ![](https://secure.gravatar.com/avatar/af95386ce8ee2f02f8df5295d3fdb63ca0c88358cb2c6b5cc94ce44d539350da?s=50&d=blank&r=g)
Neil
[ September 4, 2020 at 12:07 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1360154)
Hey,
This is great and we have started to use it. One of our main goals is to use it for patch management. However, we have to click into each server to see there patch level and update. Is there any way or any thoughts on enhancing the dashboard so that an updates tab will be available. And even a way to select servers and update rather than individually.
Thanks
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1360154)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ September 4, 2020 at 11:16 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1360315)
@Neil
You can contact the developers of Cockpit-project:
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1360315)
       * ![](https://secure.gravatar.com/avatar/7dad02976a1fa06c2e10cefa57c633ffa1fc9ee89c97fbd1187ab10b6e031e19?s=50&d=blank&r=g)
Jordi Rubal
[ September 10, 2020 at 2:06 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1362099)
In order to do that you need Red Hat Satellite. In fact… you can even install the cockpit in all your Linux servers from Satellite.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1362099)
  5. ![](https://secure.gravatar.com/avatar/a730fef4c01780d01bd37e36e428a4efeb9c411a82c7800045b9185e9afc6ae8?s=50&d=blank&r=g)
Anil
[ April 16, 2020 at 3:15 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1327358)
I have installed on centos successfully it shows the details as Project website.
Version 195.1.
Licensed under: GNU LGPL version 2.1,
But unfortunately, I am not able to see storage selection on my webpage. Can anybody give the solution?
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1327358)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ April 17, 2020 at 11:54 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1328154)
@Anil
Have you checked the side menu items? And which CentOS version are you using?
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1328154)
       * ![](https://secure.gravatar.com/avatar/a730fef4c01780d01bd37e36e428a4efeb9c411a82c7800045b9185e9afc6ae8?s=50&d=blank&r=g)
Anil
[ April 17, 2020 at 1:26 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1328167)
@Aaron Thanks, Yes I checked. I am able to see the options are (System, Logs, Networking, Accounts, Services, Diagnostic reports, Kernel dump, SELinux, terminal. I am using CentOS 7.
And I am not able to see the dashboard too to add other servers…
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1328167)
         * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ April 18, 2020 at 1:01 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1328304)
@Anil
Let me try to install Cockpit on a fresh CentOS 7 installation and give you feedback later on. Thanks.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1328304)
  6. ![](https://secure.gravatar.com/avatar/3cda2ed9bf14997a0fe225e2189230f28000072ad18281815b004928b135752f?s=50&d=blank&r=g)
zack
[ March 13, 2020 at 10:08 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1321176)
This is interesting I will try it as we have 3 servers, seems good management all in one kit.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1321176)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ March 17, 2020 at 12:58 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1321680)
@zack
Give it a try and share your thoughts about it. Thanks.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1321680)
  7. ![](https://secure.gravatar.com/avatar/2631323b939201c4bec77814ea068a98dc0f2de90766a172ece889b4c7615a04?s=50&d=blank&r=g)
Sergio
[ January 23, 2020 at 11:55 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1313261)
I have installed on my Fedora 31, looks good but a few minor problems. I could not change the idle timeout (could not find the **/etc/cockpit/cockpit.conf**). Also, there are no graphs showing on pages `http://localhost:9090/system/graphs#/cpu`.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1313261)
  8. ![](https://secure.gravatar.com/avatar/e29eadc8a765ae5eef8b5adb51306691a2b7a64ac9838235945fdfb33755a438?s=50&d=blank&r=g)
nehru
[ July 7, 2018 at 5:20 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1013102)
Hi,
I have installed on Cent OS 7, but did not showing the Dashboard. Please share the info
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1013102)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ July 9, 2018 at 4:37 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1014314)
@nehru
Ensure that you have opened the port Cockpit listens(9090) on, in your firewall.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1014314)
       * ![](https://secure.gravatar.com/avatar/269cc66edc5ed60f8040989340ebee97d93e1d9172b63df211860f7ae4bdcc38?s=50&d=blank&r=g)
prashant kumar
[ July 10, 2018 at 4:19 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1014939)
I have disabled my firewall but still no option of dashboard.
cockpit Version 165.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1014939)
         * ![](https://secure.gravatar.com/avatar/130f25feda5bb9e3f392ca142ae53e0235ab126c935168881fd269e770a3f1e0?s=50&d=blank&r=g)
Paul
[ November 6, 2018 at 10:00 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1056376)
I had the same problem, but I found a simple fix: add /dashboard to your url and add the second server. From now on you should have the dashboard button in the menu.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1056376)
           * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ November 7, 2018 at 12:53 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1056657)
@Paul
Many thanks for sharing this useful solution.
           * ![](https://secure.gravatar.com/avatar/a730fef4c01780d01bd37e36e428a4efeb9c411a82c7800045b9185e9afc6ae8?s=50&d=blank&r=g)
Anil
[ April 16, 2020 at 3:09 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1327336)
Can you please more brief about how to add Dashboard..
  9. ![](https://secure.gravatar.com/avatar/b203a515c5628a92444067900e4ba4972a525128c0edfb50dbf3a272330fa7e5?s=50&d=blank&r=g)
MGi
[ January 1, 2018 at 7:50 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-956336)
Looks interesting, but it wants to install GUI on my server. That’s unacceptable.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-956336)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ January 2, 2018 at 11:25 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-956825)
@MGi
Yes, it’s a GUI so if you want to use it, then you have to install a GUI on your server.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-956825)
     * ![](https://secure.gravatar.com/avatar/48eb8f9fcc1f6ac256b7249433e75b5f3390ac162c21b238cafcbce1c3117400?s=50&d=blank&r=g)
guvnayyc
[ July 4, 2018 at 11:18 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1011213)
It’s a WebUI, it has the same security implications as SSH or console.
I’m guessing GUI is bad from your standpoint in respect to resource overhead (read: X-Window System, Desktop).
That’s not the case with the WebUI.
I just installed it on a head server and looking at the resources being logged in and managing a dozen other servers, it’s nominal.
Just putting it out there so you have a second point of reference.
Cheers, and good luck with your endeavour!!
Nick
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1011213)
       * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ July 5, 2018 at 2:40 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1011700)
@guvnayyc
Many thanks for sharing your thoughts with us.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-1011700)
  10. ![](https://secure.gravatar.com/avatar/5e159aac35c216e350a6f0b35ac40cd80605dc6fed505990a48fa6bfc4c8edc0?s=50&d=blank&r=g)
Sof
[ January 31, 2017 at 5:10 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-863773)
Did not work for me.
```
$ sudo apt-key adv --keyserver sks-keyservers.net --recv-keys F1BAA57C

```

I had to use :
```
$ sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys F1BAA57C

```
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-863773)
  11. ![](https://secure.gravatar.com/avatar/1a526f106f97726a12fe6b67fca7c1dfe84114e9b3a5851fe688e313cffde631?s=50&d=blank&r=g)
c4ifford
[ January 30, 2017 at 8:59 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-863587)
So I’m curious how this differs from Webmin or I’d go even as far to say as this is GUI implementation of anisble/puppet or the like.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-863587)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ January 31, 2017 at 1:21 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-863744)
@c4ifford
There is no much difference, the underlying system administration functionalities are more like the same. Only that Webmin offers several other functionalities compared to Cockpit.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-863744)
  12. ![](https://secure.gravatar.com/avatar/c8ae1fd29776bf24a465b68f1859fcfce271769c7430da6771d6c6f8e8b792d1?s=50&d=blank&r=g)
Tierro
[ January 28, 2017 at 1:56 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-863019)
I tried install this tool and i have a problem:
sudo apt-key adv –keyserver sks-keyservers.net –recv-keys F1BAA57C – done
sudo apt-get update – done
root:~# apt-get install cockpit
Reading package lists… Done
Building dependency tree
Reading state information… Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:
The following packages have unmet dependencies:
cockpit : Depends: cockpit-bridge (>= 129-0~unstable) but it is not going to be installed
Depends: cockpit-bridge (= 129-0~unstable) but it is not going to be installed
Depends: cockpit-dashboard (= 129-0~unstable) but it is not going to be installed
Depends: cockpit-ws (< 129-0~unstable.1~) but it is not going to be installed
Depends: cockpit-system (= 129-0~unstable) but it is not going to be installed
Recommends: cockpit-docker (= 129-0~unstable) but it is not going to be installed
Recommends: cockpit-storaged (= 129-0~unstable) but it is not going to be installed
Recommends: cockpit-networkmanager (= 129-0~unstable) but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-863019)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ January 30, 2017 at 1:58 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-863387)
@Tierro
Try to follow this installation steps for Debian from the official Cockpit website:
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-863387)
       * ![](https://secure.gravatar.com/avatar/c8ae1fd29776bf24a465b68f1859fcfce271769c7430da6771d6c6f8e8b792d1?s=50&d=blank&r=g)
Tierro
[ February 4, 2017 at 6:21 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-864643)
I tried. The same problem :(
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-864643)
  13. ![](https://secure.gravatar.com/avatar/60749e5fea03a612119ca8a908a7c3c63ad5206eb41fb01614bc35476a1aeab3?s=50&d=blank&r=g)
Pierpaolo
[ October 16, 2016 at 4:08 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-829120)
Fantastic tool!
Small typo in Ubuntu installation:
Wrong: sudo systemctl enable –now cockpit.sock
Correct: sudo systemctl enable –now cockpit.socket
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-829120)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 17, 2016 at 10:39 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-829308)
@Pierpaolo,
Thanks for finding it useful and that's a good catch, corrected in the writeup.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-829308)
  14. ![](https://secure.gravatar.com/avatar/7dad02976a1fa06c2e10cefa57c633ffa1fc9ee89c97fbd1187ab10b6e031e19?s=50&d=blank&r=g)
mightyme
[ October 11, 2016 at 7:34 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827870)
Do you know if I can perform patch management with cockpit? Or at least run yum update to several Red Hat 7.2 servers?
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827870)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ October 11, 2016 at 12:01 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827900)
@mightyme
I can not exactly tell, if you installed it already, you can see that it offers a centralized interface to access several servers but each server with its own terminal. And the commands you run only apply to a particular server unless you write scripts to achieve patch management or single command to update several servers at once.
It is only in the graphs where info from different servers is merged.However, you can ask the developers:
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827900)
  15. ![](https://secure.gravatar.com/avatar/aeba6ef09f70dd0ece2896e685d01eadd133046d438bd71893ae310ec333f0bb?s=50&d=blank&r=g)
Sophie
[ October 8, 2016 at 8:50 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827299)
Is Cockpit amd64 only? I’m getting the following error when trying to install on an Ubuntu-based distro:
Failed to fetch
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827299)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 10, 2016 at 1:11 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827674)
@Sophie,
Yes I think Cockpit supports only 64-bit machines..
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827674)
  16. ![](https://secure.gravatar.com/avatar/2bdade6525c45d8b1cb337c2c50cbaf801d6a523df04ebd88993ed1b7d2f2128?s=50&d=blank&r=g)
Chris Christensen
[ October 7, 2016 at 7:48 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827064)
Hi Aaron. The command for Arch is wrong (or mistyped). The command should be:
```
# yaourt -S cockpit
OR
# yaourt cockpit

```

Thanks for the great article!
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827064)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 8, 2016 at 11:40 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827211)
@Chris,
Thanks for updating about that typo regarding cockpit, corrected in the writeup…
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827211)
  17. ![](https://secure.gravatar.com/avatar/be4172a769be97c87418f5141c0a8bfdc716d2aad5ebb306d5637ce5679bfa31?s=50&d=blank&r=g)
lokesh
[ October 7, 2016 at 12:14 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826997)
will this tool support for citrix xen server.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826997)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ October 7, 2016 at 3:52 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827030)
@lokash
It probably can, however we are not totally sure about that, try to consult the developers for more information:
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-827030)
  18. ![](https://secure.gravatar.com/avatar/f1e24048abd3869f7ecb00d01b695ab947de0518f64ed4a3880ee9d422d38f47?s=50&d=blank&r=g)
Mark Allen
[ October 7, 2016 at 7:48 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826923)
Any chance of it working on a Suse server?
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826923)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 7, 2016 at 11:16 am  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826979)
@Mark,
Yes, Cockpit is available for Suse Linux too, you can find the instructions on how to install Cockpit on Suse Linux here:
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826979)
  19. ![](https://secure.gravatar.com/avatar/3fdae295997fc399402e542b206347ed09282c52bb56f5f56d9bf9d9aeebf1f0?s=50&d=blank&r=g)
Kunalsing
[ October 6, 2016 at 4:05 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826380)
Awesome Aaron
I Have used and deployed on development server for container monitoring & it works perfectly.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826380)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ October 6, 2016 at 6:29 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826470)
@kunalsing
That is great, thanks for the feedback, and offering us your experience with it.
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826470)
  20. ![](https://secure.gravatar.com/avatar/2fc28e759a491bfecbaa88c1d58048965b6b6cb714fbc6c49b3698312171db7c?s=50&d=blank&r=g)
Amon
[ October 6, 2016 at 1:28 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826297)
Does it work for debian on ARM (Raspbian)?
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826297)
     * ![](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=50&d=blank&r=g)
Aaron Kili
[ October 6, 2016 at 6:47 pm  ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826485)
@Amon
According to this guide, yes it works.
Try to read this installation guide for Raspbian:
[Reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#comment-826485)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/#respond)
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
[How to Monitor Progress of (Copy/Backup/Compress) Data using ‘pv’ Command](https://www.tecmint.com/monitor-copy-backup-tar-progress-in-linux-using-pv-command/)
[12 Ways to Find User Account Info and Login Details in Linux](https://www.tecmint.com/check-user-in-linux/)
[Googler: A Command Line Tool to Do ‘Google Search’ from Linux Terminal](https://www.tecmint.com/google-commandline-search-terminal/)
[How to Use ‘Yum History’ to Find Out Installed or Removed Packages Info](https://www.tecmint.com/view-yum-history-to-find-packages-info/)
[How to Run Shell Scripts with Sudo Command in Linux](https://www.tecmint.com/run-shell-scripts-with-sudo-command-in-linux/)
[How to Compare Local and Remote Files in Linux](https://www.tecmint.com/compare-local-and-remote-files-in-linux/)
## Linux Server Monitoring Tools
[rtop – An Interactive Tool to Monitor Remote Linux Server Over SSH](https://www.tecmint.com/rtop-monitor-remote-linux-server-over-ssh/)
[5 Tools to Scan a Linux Server for Malware and Rootkits](https://www.tecmint.com/scan-linux-for-malware-and-rootkits/)
[screenFetch – An Ultimate System Information Generator for Linux](https://www.tecmint.com/screenfetch-system-information-generator-for-linux/)
[20 Useful Commands of ‘Sysstat’ Utilities (mpstat, pidstat, iostat and sar) for Linux Performance Monitoring](https://www.tecmint.com/sysstat-commands-to-monitor-linux/)
[All You Need To Know About Processes in Linux [Comprehensive Guide]](https://www.tecmint.com/linux-process-management/)
[How to Install Zabbix Agent and Add Windows Host to Zabbix Monitoring – Part 4](https://www.tecmint.com/install-zabbix-agent-and-add-windows-host-to-zabbix-monioring/)
## Learn Linux Tricks & Tips
[How to Copy File Permissions and Ownership to Another File in Linux](https://www.tecmint.com/copy-file-permissions-and-ownership-to-another-file-in-linux/)
[4 Useful Tips on mkdir, tar and kill Commands in Linux](https://www.tecmint.com/mkdir-tar-and-kill-commands-in-linux/)
[How to Find and Remove Duplicate/Unwanted Files in Linux Using ‘FSlint’ Tool](https://www.tecmint.com/fslint-find-and-remove-duplicate-unwanted-files-in-linux/)
[How to Find Difference Between Two Directories Using Diff and Meld Tools](https://www.tecmint.com/compare-find-difference-between-two-directories-in-linux/)
[How to Create a Virtual HardDisk Volume Using a File in Linux](https://www.tecmint.com/create-virtual-harddisk-volume-in-linux/)
[Fd – The Best Alternative to ‘Find’ Command for Quick File Searching](https://www.tecmint.com/fd-alternative-to-find-command/)
## Best Linux Tools
[17 Best KDE Multimedia Applications for Linux](https://www.tecmint.com/kde-multimedia-applications/)
[5 Open Source Log Monitoring and Management Tools for Linux](https://www.tecmint.com/best-linux-log-monitoring-and-management-tools/)
[11 Best Graphical Git Clients and Git Repository Viewers for Linux](https://www.tecmint.com/best-gui-git-clients-git-repository-viewers-for-linux/)
[5 Best Platforms for Hosting Your Web Projects in 2024](https://www.tecmint.com/best-web-software-hosting-platforms/)
[3 Best Cloud-Based Music Apps for Linux](https://www.tecmint.com/cloud-music-player/)
[32 Best File Managers and Explorers [GUI + CLI] for Linux in 2024](https://www.tecmint.com/linux-file-managers/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/ "Scroll back to top")
Search for:
