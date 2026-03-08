[Skip to content](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/)
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
  * [Pro Courses](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/ "Linux Online Courses")
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


[](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/)
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
  * [Pro Courses](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/ "Linux Online Courses")
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


[](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/)
# How to Monitor Docker Containers with Zabbix Monitoring Tool
[James Kiarie](https://www.tecmint.com/author/james2030kiarie/ "View all posts by James Kiarie")Last Updated: November 17, 2021 Read Time: 7 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [Zabbix](https://www.tecmint.com/category/zabbix/) [Leave a comment](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/#respond)
**Docker** is arguably one of the most cherished **DevOps** tools that streamline the development, deployment, and shipping of applications inside containers.
The concept of containerization entails leveraging container images. These are small, lightweight, and standalone executable packages that include everything that is needed to run an application including the source code, libraries and dependencies, and configuration files.
By doing so, the application can run in almost any computing environment; traditional IT infrastructure, cloud, and a myriad of Linux / UNIX flavors.
Monitoring containers helps operation teams to identify underlying issues and resolve them in a timely fashion. Container monitoring encompasses capturing basic metrics such as [CPU usage](https://www.tecmint.com/find-linux-processes-memory-ram-cpu-usage/ "Find CPU Usage in Linux"), [memory utilization](https://www.tecmint.com/find-processes-by-memory-usage-top-batch-mode/ "Find Linux Memory Usage"), container size, and [bandwidth utilization](https://www.tecmint.com/linux-network-bandwidth-monitoring-tools/ "Monitor Linux Bandwidth Utilization") to mention a few. Additionally, you can gather [real-time logs](https://www.tecmint.com/open-source-centralized-linux-log-management-tools/ "Linux Open Source Log Management Tools") which are helpful in debugging and alerting the IT team when to scale up.
**Zabbix** is a popular IT infrastructure monitoring tool that keeps an eye on almost every element of your environment including physical devices such as servers and network devices such as routers and switches. It can also monitor applications, services, and databases.
In this guide, we will show you how you can monitor **Docker** containers using the **Zabbix** monitoring tool in Linux.
#### Requirements
Here is what you need before getting started:
First up, ensure that you have two nodes – The first node is the Zabbix server. This is the node from which we will monitor the remote **Docker** server. We have an article on:
  * [How to Install Zabbix on Rocky Linux and AlmaLinux](https://www.tecmint.com/install-zabbix-rockylinux-almalinux/ "How to Install Zabbix on Rocky Linux and AlmaLinux")
  * [How to Install Zabbix Monitoring Tool on Debian 11/10](https://www.tecmint.com/install-zabbix-on-debian-10/ "How to Install Zabbix Monitoring Tool on Debian 11/10")
  * [How to Install Zabbix on RHEL 8](https://www.tecmint.com/install-zabbix-on-rhel-8/ "How to Install Zabbix on RHEL 8")
  * [How to Install Zabbix on Ubuntu](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/ "How to Install Zabbix on Ubuntu")


The second node is the **Docker** server on which **Docker** is installed. This is the node from where we will run Docker containers and monitor container activity.
  * [How to Install Docker on Rocky Linux and AlmaLinux](https://www.tecmint.com/install-docker-in-rocky-linux-and-almalinux/ "How to Install Docker on Rocky Linux and AlmaLinux")
  * [How to Install and Use Docker on Ubuntu 20.04](https://www.tecmint.com/install-docker-on-ubuntu/ "How to Install and Use Docker on Ubuntu 20.04")
  * [How to Install Docker in CentOS and RHEL 8/7](https://www.tecmint.com/install-docker-and-learn-containers-in-centos-rhel-7-6/ "Install Docker in CentOS and RHEL 8/7")


Next, ensure that you have SSH access to your **Docker** server node with a sudo user already configured.
With your setup in place, you can now roll your sleeves!
### Step 1: Install Zabbix-Agent in Linux
To monitor **Docker** containers on the remote server, you need to install a **Zabbix agent** , which is a monitoring agent that is deployed on a target node to actively monitor system metrics and other applications.
First, you need to install the **Zabbix** repository on the **Docker** node.
```
**----------- On Ubuntu 20.04 -----------**
$ sudo wget https://repo.zabbix.com/zabbix/5.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.4-1+ubuntu20.04_all.deb
$ sudo dpkg -i zabbix-release_5.4-1+ubuntu20.04_all.deb
$ sudo apt update
$ sudo apt install zabbix-agent2

**----------- On RHEL-based Distro -----------**
$ sudo rpm -Uvh https://repo.zabbix.com/zabbix/5.4/rhel/8/x86_64/zabbix-release-5.4-1.el8.noarch.rpm
$ sudo dnf update
$ sudo dnf install zabbix-agent

**----------- On Debian 11 -----------**
$ sudo wget https://repo.zabbix.com/zabbix/5.4/debian/pool/main/z/zabbix-release/zabbix-release_5.4-1%2Bdebian11_all.deb
$ sudo dpkg -i zabbix-release_5.4-1%2Bdebian11_all.deb
$ sudo apt update
$ sudo apt install zabbix-agent2

**----------- On Debian 10 -----------**
$ sudo wget https://repo.zabbix.com/zabbix/5.4/debian/pool/main/z/zabbix-release/zabbix-release_5.4-1%2Bdebian10_all.deb
$ sudo dpkg -i zabbix-release_5.4-1%2Bdebian10_all.deb
$ sudo apt update
$ sudo apt install zabbix-agent2

```

### Step 2: Configure Zabbix-Agent in Linux
By default, the **Zabbix** agent is set to ship metrics to the **Zabbix** server on the same host it is installed. Since our objective is to monitor **docker** containers on the remote server, some additional configurations are required.
Therefore, access the **Zabbix** agent configuration file.
```
$ sudo vim /etc/zabbix/zabbix_agent2.conf

```

The configuration file contains settings that specify the address where the metrics are sent to, the port used for connections and so much more. For the most part, the default settings will work just fine.
To configure the **Zabbix** agent to send metrics to the **Zabbix** server, locate the directive which is configured to ship metrics to the loopback address, or simply put, the same host system.
```
Server=127.0.0.1

```

Set the address to reflect the Zabbix server’s address
```
Server=zabbix-server-IP

```

Additionally, navigate to the ‘**Active checks** ’ section and change the directive to point to the Zabbix server’s IP address.
```
ServerActive=zabbix-server-IP

```

Be sure to also adjust the hostname of the Docker server accordingly. The hostname of my Docker server is **Ubuntu20**.
```
Hostname=Ubuntu20

```

Then save the changes and exit the Zabbix configuration file.
For the Zabbix agent to keep an eye on Docker containers, you need to add the Zabbix user, which is installed by default, to the docker group.
```
$ sudo usermod -aG docker zabbix

```

To apply the changes made to the configuration file, restart the Zabbix-agent service and enable it to start on system startup.
```
$ sudo systemctl restart zabbix-agent2
$ sudo systemctl enable zabbix-agent2

```

Confirm the running status of the Zabbix agent as follows.
```
$ sudo systemctl status zabbix-agent2

```
![Check Zabbix Agent Status](https://www.tecmint.com/wp-content/uploads/2021/11/Check-Zabbix-Agent-Status.png)Check Zabbix Agent Status
Zabbix agent listens on port **10050**. If you have a [UFW firewall](https://www.tecmint.com/setup-ufw-firewall-on-ubuntu-and-debian/ "How to Setup UFW Firewall on Ubuntu and Debian") or [firewalld](https://www.tecmint.com/configure-firewalld-in-centos-7/ "How to Configure FirewallD in RHEL, CentOS and Fedora") running, consider opening the port as follows.
```
**----------- On UFW Firewall -----------**
$ sudo ufw allow 10050/tcp
$ sudo ufw reload

**----------- On Firewalld -----------**
$ sudo firewall-cmd --add-port=10050/tcp --permanent
$ sudo firewall-cmd --reload

```

Great! We are now at the halfway mark. The Zabbix agent can now ship the **Docker** container metrics to the Zabbix server.
In the next step, we will add the **Docker** server to the **Zabbix** web interface and monitor Docker containers.
### Step 3: Add the Docker to Zabbix Server for Monitoring
To monitor a remote host, you need to add it to the **Zabbix** server’s dashboard via a browser. Zabbix provides myriad templates for various services and applications. We will link the appropriate template to the Docker host to specifically monitor containers. But first, access the Zabbix server’s login page.
```
http://zabbix-server-ip/zabbix

```
![Zabbix Login](https://www.tecmint.com/wp-content/uploads/2021/11/Zabbix-Login-1.png)Zabbix Login
Once you have logged in, navigate to the right sidebar and click on ‘**Configuration** ’ then ‘**Hosts** ’.
![Zabbix Host Configuration](https://www.tecmint.com/wp-content/uploads/2021/11/Zabbix-Host-Configuration.png)Zabbix Host Configuration
At the far top-right corner, click on ‘**Create host** ’.
![Zabbix Create Host](https://www.tecmint.com/wp-content/uploads/2021/11/Zabbix-Create-Host.png)Zabbix Create Host
Fill in the details of the **Docker** server such as the **hostname** & **visible** name. For Groups, Type in ‘**Docker Groups** ’ (every host must be associated with a group).
Below the ‘**Interfaces** ’ label click on ‘**Add** ’ and in the menu that appears select ‘**Agent** ’.
![Add Host to Zabbix Monitoring](https://www.tecmint.com/wp-content/uploads/2021/11/Add-Host-to-Zabbix.png)Add Host to Zabbix Monitoring
Next, fill out the Docker server’s private IP address and ensure that the port is set to **10050**.
![Add Docker Server to Zabbix](https://www.tecmint.com/wp-content/uploads/2021/11/Add-Docker-Server-to-Zabbix.png)Add Docker Server to Zabbix
Next, click on the **Templates** tab, and in the ‘**Link new templates** ’ section, specify ‘**Docker by Zabbix agent 2** ’. Then click the ‘**Add** ’ button.
![Link Zabbix Template to Docker](https://www.tecmint.com/wp-content/uploads/2021/11/Link-Zabbix-Template-to-Docker.png)Link Zabbix Template to Docker
When you click the Add button, the remote Docker host will automatically be added as indicated.
![Zabbix Docker Monitoring](https://www.tecmint.com/wp-content/uploads/2021/11/Zabbix-Docker-Monitoring.png)Zabbix Docker Monitoring
At this point, the Zabbix server is now monitoring your Docker server. In the next step, we will deploy a container and check out which metrics can be monitored.
### Step 4: Monitoring Docker Metrics in Zabbix Monitoring
To begin monitoring **Docker** metrics, we are going to launch a test container. So, head back to your **Docker** server and launch a container.
In this example, we will pull a **Ubuntu** container image and create a container called **docker_test_container**. We will then gain shell access using the `-it` option. The entire command for the operations is as follows.
```
$ sudo docker run --name docker_test_container -it ubuntu bash

```
![Create Ubuntu Container Image in Docker](https://www.tecmint.com/wp-content/uploads/2021/11/Create-Ubuntu-Container-Image-in-Docker.png)Create Ubuntu Container Image in Docker
You can try something ambitious such as installing software packages such as **Apache** or **MariaDB** in order to generate some metrics such as CPU utilization and network traffic.
Now head back to the **Zabbix** server dashboard. Click on ‘**Monitoring** ’ then ‘**Hosts** ’. Click on the name of your Docker server and in the menu option that appears, select ‘**Latest data** ’.
![Zabbix Monitoring Hosts](https://www.tecmint.com/wp-content/uploads/2021/11/Zabbix-Monitoring-Hosts.png)Zabbix Monitoring Hosts
After a few minutes of deploying the container, the Zabbix server will detect the container and start populating some statistics.
![Zabbix Monitoring Docker Host](https://www.tecmint.com/wp-content/uploads/2021/11/Zabbix-Monitoring-Docker-Host.png)Zabbix Monitoring Docker Host
You can also view the graphs of the various container metrics by clicking on the ‘**graphs** ’ options of the Docker server on the ‘**Hosts** ’ page. Below you can see the CPU & Memory usage metrics.
![Zabbix Monitoring Docker Performance](https://www.tecmint.com/wp-content/uploads/2021/11/Zabbix-Monitoring-Docker-Performance.png)Zabbix Monitoring Docker Performance
To simulate the container crash, we will unexpectedly exit from the container by running the command below in the container shell.
```
# exit 2

```

This implies that we have terminated the container with an error code of 2. This is recorded within the container’s metadata. To view the alert, navigate to the left sidebar and click on ‘**Monitoring** ’ then ‘**Dashboard** ’.
The alert is displayed below.
![Zabbix Docker Warnings](https://www.tecmint.com/wp-content/uploads/2021/11/Zabbix-Docker-Warnings.png)Zabbix Docker Warnings
To rectify the error, simply start the container again.
```
$ sudo docker start docker_test_container

```

And this brings us to the end of this guide. We have walked you through a step-by-step procedure of how you can Monitor **Docker** containers using the **Zabbix** monitoring tool.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Integrate ONLYOFFICE Docs with Alfresco on Ubuntu](https://www.tecmint.com/integrate-onlyoffice-docs-alfresco-ubuntu/)
Next article:
[How to Upgrade CentOS 7 to CentOS 8 Linux](https://www.tecmint.com/upgrade-centos-7-to-centos-8/)
![Photo of author](https://secure.gravatar.com/avatar/3b060d6a6c8d6305817bda1435529b27f2d4f900a7998bd703a17094636601a9?s=100&d=blank&r=g)
James Kiarie
This is James, a certified Linux administrator and a tech enthusiast who loves keeping in touch with emerging trends in the tech world. When I'm not running commands on the terminal, I'm taking listening to some cool music. taking a casual stroll or watching a nice movie.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/#respond)** or
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
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/#respond)
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
[How to Delete All Files in a Folder Except Certain Extensions](https://www.tecmint.com/delete-files-except-certain-file-extensions/)
[Linux mkdir Command Examples](https://www.tecmint.com/mkdir-command-examples/)
[How to Disable Bluetooth at Linux Startup](https://www.tecmint.com/disable-bluetooth-linux/)
[8 Linux Commands to Diagnose Hard Drive Issues in Linux](https://www.tecmint.com/fix-hard-drive-bottlenecks-in-linux/)
[11 Lesser Known Useful Linux Commands](https://www.tecmint.com/lesser-known-linux-commands/)
[12 ss Command Examples to Monitor Network Connections](https://www.tecmint.com/ss-command-examples-in-linux/)
## Linux Server Monitoring Tools
[ctop – Top-like Interface for Monitoring Docker Containers](https://www.tecmint.com/ctop-monitor-docker-containers/)
[4 Ways to Watch or Monitor Log Files in Real Time](https://www.tecmint.com/watch-or-monitor-linux-log-files-in-real-time/)
[Bandwhich – A Network Bandwidth Utilization Tool for Linux](https://www.tecmint.com/bandwhich-monitor-linux-network-bandwidth-utilization/)
[Collectl: An Advanced All-in-One Performance Monitoring Tool for Linux](https://www.tecmint.com/collectl-linux-performance-reporting-monitoring/)
[10 Tips On How to Use Wireshark to Analyze Packets in Your Network](https://www.tecmint.com/wireshark-network-traffic-analyzer-for-linux/)
[How to Setup Rsyslog Client to Send Logs to Rsyslog Server in CentOS 7](https://www.tecmint.com/setup-rsyslog-client-to-send-logs-to-rsyslog-server-in-centos-7/)
## Learn Linux Tricks & Tips
[How to Clear BASH Command Line History in Linux](https://www.tecmint.com/clear-command-line-history-in-linux/)
[10 Practical Examples Using Wildcards to Match Filenames in Linux](https://www.tecmint.com/use-wildcards-to-match-filenames-in-linux/)
[Add Rainbow Colors to Linux Command Output in Slow Motion](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/)
[6 Best CLI Tools to Search Plain-Text Data Using Regular Expressions](https://www.tecmint.com/command-line-tools-to-search-strings-or-patterns-in-files/)
[5 Ways to Empty or Delete a Large File Content in Linux](https://www.tecmint.com/empty-delete-file-content-linux/)
[Bash-it – Bash Framework to Control Your Scripts and Aliases](https://www.tecmint.com/bash-it-control-shell-scripts-aliases-in-linux/)
## Best Linux Tools
[8 Best PowerPoint Alternatives for Linux](https://www.tecmint.com/powerpoint-alternatives-for-linux/)
[8 Best Command-Line/Terminal Email Clients for Linux](https://www.tecmint.com/best-commandline-email-clients-for-linux/)
[16 Best Microsoft Teams Alternatives For Linux in 2024](https://www.tecmint.com/microsoft-teams-alternatives/)
[5 GUI Tools to Free Up Space on Debian, Ubuntu and Linux Mint](https://www.tecmint.com/free-disk-space-ubuntu-linux-mint/)
[5 Best Microsoft Word Alternatives for Linux in 2024](https://www.tecmint.com/microsoft-word-alternatives-linux/)
[16 Best Notepad++ Alternatives for Linux in 2025](https://www.tecmint.com/best-notepad-alternatives-for-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/monitor-docker-containers-with-zabbix-monitoring/ "Scroll back to top")
Search for:
