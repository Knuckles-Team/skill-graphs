[Skip to content](https://www.tecmint.com/install-and-connect-an-agent-to-pandora-fms-server/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/install-and-connect-an-agent-to-pandora-fms-server/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-and-connect-an-agent-to-pandora-fms-server/)
A **Pandora FMS Agent** is an application installed on computers to be monitored using the [Pandora FMS Monitoring System](https://www.tecmint.com/install-pandora-fms-in-ubuntu/). Software agents perform checks on server resources (such as CPU, RAM, storage devices, etc.) and installed applications and services (such as Nginx, Apache, MySQL/MariaDB, PostgreSQL, etc.); they send the collected data to the **Pandora FMS Servers** in XML format using one of the following protocols: SSH, FTP, NFS, Tentacle (protocol) or any other data transfer means.
**Note** : Agents are only needed for server and resource monitoring, while network equipment monitoring is done remotely thus no need to install software agents.
This article shows how to install **Pandora FMS** software agents and connect them to a Pandora FMS Server instance for monitoring. This guide assumes that you already have a [running instance of a Pandora FMS server](https://www.tecmint.com/install-pandora-fms-in-ubuntu/).
### Installing Pandora FMS Agents in Linux Systems
On CentOS and RHEL distributions, run the following commands to install the required dependencies packages, then download the latest version of the Pandora FMS agent RPM package and install it.
```
# yum install wget perl-Sys-Syslog perl-YAML-Tiny
# wget https://sourceforge.net/projects/pandora/files/Pandora%20FMS%207.0NG/743/RHEL_CentOS/pandorafms_agent_unix-7.0NG.743-1.noarch.rpm
# yum install pandorafms_agent_unix-7.0NG.743-1.noarch.rpm

```

On **Ubuntu** and **Debian** distributions, issue the following commands to download the latest agent DEB package and install it.
```
$ wget https://sourceforge.net/projects/pandora/files/Pandora%20FMS%207.0NG/743/Debian_Ubuntu/pandorafms.agent_unix_7.0NG.743.deb
$ sudo dpkg -i pandorafms.agent_unix_7.0NG.743.deb
$ sudo apt-get -f install

```

### Configuring Pandora FMS Agents in Linux Systems
After successfully installing the software agent package, configure it to communicate with the **Pandora FMS** server, in the **/etc/pandora/pandora_agent.conf** configuration file.
```
# vi /etc/pandora/pandora_agent.conf

```

Look for the server configuration parameter and set its value to the IP address of the Pandora FMS server as shown in the following screenshot.
![Configure Pandora FMS Agent](https://www.tecmint.com/wp-content/uploads/2020/02/configure-pandorafms-agent.png)Configure Pandora FMS Agent
Save the file and then start the Pandora agent daemon service, enable it to auto-start at system boot and verify the service is up and running.
```
# systemctl start pandora_agent_daemon.service
# systemctl enable pandora_agent_daemon.service
# systemctl status pandora_agent_daemon.service

```

### Adding New Agent to Pandora FMS Server
Next, you need to add the new agent via the Pandora FMS console. Go to the web browser and log into the Pandora FMS server console and then go to **Resources** ==> **Manage Agents**.
![Pandora FMS Resources Tab](https://www.tecmint.com/wp-content/uploads/2020/02/click-on-resources-menu.png)Pandora FMS Resources Tab
From the next screen, click on **Create agent** to define a new agent.
![Create a New Agent in Pandora FMS](https://www.tecmint.com/wp-content/uploads/2020/02/create-new-agent-feature.png)Create a New Agent in Pandora FMS
At the **Agent Manager** page, define a new agent by filling the form as shown in the following screenshot. Once you are done, click on **Create**.
![Add Agent Details and Create](https://www.tecmint.com/wp-content/uploads/2020/02/create-new-agent.png)Add Agent Details and Create
After adding agents, they should reflect in the front page summary as highlighted in the following screenshot.
![Pandora FMS Agent Summary](https://www.tecmint.com/wp-content/uploads/2020/02/console-front-page.png)Pandora FMS Agent Summary
If you view the newly created agent under **Agent** details and highlight its status indicator, it should show no monitors. So you need to create modules for monitoring the host the agent is running on, as explained in the next section.
![View Pandora FMS Agent Details](https://www.tecmint.com/wp-content/uploads/2020/02/view-agent-details.png)View Pandora FMS Agent Details
### Configuring a Module for Remote Agent Monitoring
For this guide, we will create a module to check if the remote host is live (can be pinged). To create a module, go to **Resource** ==> **Manage agents**. At the **Agents** defined in the **Pandora FMS** screen, click on the **agent name** to edit it.
![Open Agent to Define Module](https://www.tecmint.com/wp-content/uploads/2020/02/agents-defined.png)Open Agent to Define Module
Once it loads, click on the **Modules** link as highlighted in the following screenshot.
![View Agent Modules](https://www.tecmint.com/wp-content/uploads/2020/02/view-agent-modules.png)View Agent Modules
Then select the **module type** (e.g Create a **new network server module**) from the next screen and click **Create**.
![Select A Agent Module Type](https://www.tecmint.com/wp-content/uploads/2020/02/select-module-type.png)Select A Agent Module Type
From the next screen, select the module **component** group (e.g **Network Management**) and its actual check type (e.g **Host Alive**). Then fill in the other fields, and ensure that the **Target IP** is of the host to be monitored. Then click **Create**.
![Agent Module Created](https://www.tecmint.com/wp-content/uploads/2020/02/module-created-successfully.png)Agent Module Created
Next, refresh the console and try to view the **agent** under **Agent** details, and highlight its status indicator, it should show “**All monitors are OK** ”. And under **modules** , it should show that there is one module that is in a normal state.
![Check Status of Agent in Pandora FMS](https://www.tecmint.com/wp-content/uploads/2020/02/agent-monitors-have-been-activated.png)Check Status of Agent in Pandora FMS
When you open the **agent** now, it should display some monitoring information as highlighted in the following screenshot.
![Agent Monitoring Overview](https://www.tecmint.com/wp-content/uploads/2020/02/agent-displaying-monitoring-information.png)Agent Monitoring Overview
To test if the module is working fine, you can shut down the remote host and reset the modules for the agent. It should indicate a **critical status** (RED color).
![Agent Critical Status Alert](https://www.tecmint.com/wp-content/uploads/2020/02/agent-Critical-Status.png)Agent Critical Status Alert
That’s all! The next step is to learn how to use advanced features of the PandoraFMS system and configure it to monitor your IT infrastructure, by creating more servers, agents and modules, alerts, events, reports, and so much more. For more information, see the
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install Java on Arch Linux](https://www.tecmint.com/install-java-on-arch-linux/)
Next article:
[How to Set Up IPsec-based VPN with Strongswan on Debian and Ubuntu](https://www.tecmint.com/setup-ipsec-vpn-with-strongswan-on-debian-ubuntu/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-and-connect-an-agent-to-pandora-fms-server/#respond)** or
## Related Posts
[![Linux Disk I/O Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2015/04/Linux-Disk-IO-Monitoring-Tools.png)](https://www.tecmint.com/monitor-linux-disk-io-performance/ "7 Best Tools to Monitor and Debug Disk I/O Performance in Linux")
[![Disk Usage Monitoring Script in Linux](https://www.tecmint.com/wp-content/uploads/2014/01/linux-disk-usage-monitoring-shell-script.webp)](https://www.tecmint.com/monitor-disk-usage-bash-script/ "A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%")
[![Linux Performance Monitoring with Command-Line Tools](https://www.tecmint.com/wp-content/uploads/2023/08/command-line-monitoring-tools-linux.webp)](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/ "24 Best Command Line Tools to Monitor Linux Performance")
[![atop: System and process monitor for Linux](https://www.tecmint.com/wp-content/uploads/2025/06/atop-System-and-process-monitor-for-Linux.webp)](https://www.tecmint.com/atop-linux-performance-monitoring/ "How to Install ‘atop’ to Monitor Real-Time System Performance")
[![Bash Script to Monitor Linux Health Daily](https://www.tecmint.com/wp-content/uploads/2025/06/bash-script-automate-system-health-checks.webp)](https://www.tecmint.com/bash-script-automate-system-health-checks/ "How to Automate Daily Linux Health Checks with a Bash Script + Cron")
[![Network Bandwidth Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2013/07/network-bandwidth-monitoring-tools.webp)](https://www.tecmint.com/network-bandwidth-monitoring-tools/ "5 Modern VnStat PHP Replacements for Bandwidth Monitoring")
### 2 Comments
[Leave a Reply](https://www.tecmint.com/install-and-connect-an-agent-to-pandora-fms-server/#reply-title)
  1. Hello, I did following the tutorial that you have provided, but, after selecting the module agent, there will be the next page called base option. And there are plenty of blanks that I need to fulfill until then I just inserting what the tutorial stated (host alive) and so on. But still, I can’t initialize the module. It still blue in color. How can I solve the problem, I have done ping the IP Add and it exists, turn off the firewall but then still not running.
[Reply](https://www.tecmint.com/install-and-connect-an-agent-to-pandora-fms-server/#comment-1317583)
     * @Dummy
I can’t replicate your issue. Try to restart the Pandora_agent-daemon service:
```
$ sudo systemctl restart pandora_agent_daemon.service
OR
#systemctl restart pandora_agent_daemon.service

```

Then refresh the PandoraFMS console.
For more information, see the official documentation:
[Reply](https://www.tecmint.com/install-and-connect-an-agent-to-pandora-fms-server/#comment-1317618)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-and-connect-an-agent-to-pandora-fms-server/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/install-and-connect-an-agent-to-pandora-fms-server/ "Scroll back to top")
Search for:
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=1331519825635051&rc=)
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
