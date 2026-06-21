# Monit – A Open Source Tool for Managing and Monitoring Linux System
[Ravi Saive](https://www.tecmint.com/author/admin/ "View all posts by Ravi Saive")Last Updated: July 22, 2022 Read Time: 4 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [49 Comments](https://www.tecmint.com/monit-linux-services-monitoring/#comments)
**processes** , **files** , **directories** , **checksums** , **permissions** , **filesystems,** and services like **Apache** , **Nginx** , **MySQL** , **FTP** , **SSH** , **SMTP** , and so on in a **UNIX/Linux** based systems and provides an excellent and helpful monitoring functionality to system administrators.
The monit has a user-friendly web interface where you can directly view the system status and setup up processes using a native HTTP(S) web server or via the command line interface. This means you must have web server like **Apache** or **Nginx** installed on your system to access and view the monit web interface.
**[ You might also like:[20 Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/ "Command Line Tools to Monitor Linux Performance") ]**
#### What Monit Can Do
Monit has the ability to start a process if it is not running, restart a process if not responding, and stop a process if uses high resources. Additionally, you can also use Monit to monitor **files** , **directories,** and **filesystems for changes** , **checksum changes** , **file size changes,** or **timestamp changes**.
With **Monit,** you can able to monitor remote hosts’ **TCP/IP** port, **server protocols,** and **ping**. Monit keeps its own log file and alerts about any critical error conditions and recovery status.
This article is written to describe a simple guide on **Monit** installation and configuration on [RHEL-based](https://www.tecmint.com/redhat-based-linux-distributions/ "The Best RedHat-based Linux Distributions") and [Debian-based](https://www.tecmint.com/debian-based-linux-distributions/ "Best Debian-based Linux Distributions") Linux distributions.
### Step 1: Installing Monit in Linux
By default, the **Monit** monitoring program is not available from the default system base repositories, you need to add and enable a third-party [epel repository](https://www.tecmint.com/install-epel-repository-on-centos/) to install the **monit** package under RHEL-based distributions such as **CentOS** , **Rocky Linux,** and **AlmaLinux**.
```
**--------- On RHEL 9 based Systems ---------**
# dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm

**--------- On RHEL 8 based Systems ---------**
# dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

**--------- On RHEL 7 based Systems ---------**
# yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

```

Once you’ve added the epel repository, install the **Monit** package by running the following [yum command](https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/ "Yum Command Examples").
```
# yum install monit
OR
# dnf install monit  [On **Fedora Linux**]

```
![Install Monit in RHEL](https://www.tecmint.com/wp-content/uploads/2013/04/Install-Monit-in-RHEL.png) Install Monit in RHEL
For **Ubuntu/Debian/Linux Mint** user’s can easily install using the [apt command](https://www.tecmint.com/apt-advanced-package-command-examples-in-ubuntu/ "APT Command Examples") as shown.
```
$ sudo apt install monit

```

### Step 2: Configuring Monit in Linux
**Monit** is very easy to configure, in fact, the configuration files are created to be very easily readable and making them easier for users to understand. It is designed to monitor the running services every 2 minutes and keeps the logs in “**/var/log/monit** “.
**Monit** has a web interface that runs on port **2812** using a web server. To enable the web interface you need to make changes in the monit configuration file.
The main configuration file of monit located at **/etc/monit.conf** under (**RedHat/CentOS/Fedora**) and **/etc/monit/monitrc** file for (**Ubuntu/Debian/Linux Mint**).
Open this file using your choice of editor.
```
# vi /etc/monitrc
Or
$ sudo nano /etc/monit/monitrc

```

Next, uncomment the following section and add the IP address or domain name of your server, allow anyone to connect and change the monit user and password or you can use default ones.
```
set httpd port 2812 and
     use address 0.0.0.0  # only accept connections from localhost
     allow 0.0.0.0/0        # allow localhost to connect to the server and
     allow admin:monit      # require user 'admin' with password 'monit'
     allow @monit           # allow users of group 'monit' to connect (rw)
     allow @users readonly  # allow users of group 'users' to connect readonly

```
![Configure Monit in Linux](https://www.tecmint.com/wp-content/uploads/2013/04/Configure-Monit-in-Linux.png)Configure Monit in Linux
Once you’ve configured it, you need to start, enable and verify the **monit** service to reload the new configuration settings.
```
# systemctl start monit
# systemctl enable monit
# systemctl status monit

```
![Start Monit in RHEL](https://www.tecmint.com/wp-content/uploads/2013/04/Start-Monit-in-RHEL.png)Start Monit in RHEL
Now, you will be able to access the monit web interface by navigating to the following URLs.
```
http://localhost:2812
OR
http://ip-address:2812
Or
http://example.com:2812

```

Then enter the user name as “**admin** ” and password as “**monit** “. You should get a screen similar to the one below.
![Monit Login](https://www.tecmint.com/wp-content/uploads/2013/04/Monit-Login.png)Monit Login ![Monit Service Manager](https://www.tecmint.com/wp-content/uploads/2013/04/Monit-Service-Manager.png)Monit Service Manager ![Monit System Status](https://www.tecmint.com/wp-content/uploads/2013/04/Monit-System-Status.png)Monit System Status
### Step 3: Adding Linux Services to Monit Monitoring
Once the **monit** web interfaces are correctly set up, start adding the programs that you want to monitor into the **/etc/monitrc** under (**RedHat/CentOS/Fedora**) and **/etc/monit/monitrc** file for (**Ubuntu/Debian/Linux Mint**) at the bottom.
Following are some useful configuration examples for monit, which can be very helpful to see how a service is running, where it keeps its profile, how to start and stop a service, etc.
#### Monitor Apache in Monit
```
check process httpd with pidfile /var/run/httpd.pid
group apache
start program = "/usr/bin/systemctl httpd start"
stop program = "/usr/bin/systemctl httpd stop"
if failed host 127.0.0.1 port 80
protocol http then restart
if 5 restarts within 5 cycles then timeout

```

#### Monitor Apache2 in Monit
```
check process apache with pidfile /run/apache2.pid
start program = "/usr/bin/systemctl apache2 start" with timeout 60 seconds
stop program  = "/usr/bin/systemctl apache2 stop"

```

#### Monitor Nginx in Monit
```
check process nginx with pidfile /var/run/nginx.pid
start program = "/usr/bin/systemctl nginx start"
stop program = "/usr/bin/systemctl nginx stop"

```

#### Monitor MySQL in Monit
```
check process mysqld with pidfile /var/run/mysqld/mysqld.pid
group mysql
start program = "/usr/bin/systemctl mysqld start"
stop program = "/usr/bin/systemctl mysqld stop"
if failed host 127.0.0.1 port 3306 then restart
if 5 restarts within 5 cycles then timeout

```

#### Monitor SSH in Monit
```
check process sshd with pidfile /var/run/sshd.pid
start program "/usr/bin/systemctl sshd start"
stop program "/usr/bin/systemctl sshd stop"
if failed host 127.0.0.1 port 22 protocol ssh then restart
if 5 restarts within 5 cycles then timeout

```

Once you’ve configured all programs for monitoring, check monit syntax for errors. If found any errors fix them, it’s not so tough to figure out what went wrong. When you get a message like “**Control file syntax OK** “, or if you see no errors, you can proceed ahead.
```
# monit -t
Or
$ sudo monit -t

```

After fixing all possible errors, you can type the following command to start the monit service.
```
# systemctl monit restart
OR
$ sudo systemctl monit restart

```

This is how looks monit after adding all Linux services for monitoring.
![Linux Monitoring Services with Monit](https://www.tecmint.com/wp-content/uploads/2013/04/Linux-Monitoring-Services-with-monit.png)Linux Monitoring Services with Monit
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Configure a CA SSL Certificate in HAProxy](https://www.tecmint.com/configure-ssl-certificate-haproxy/)
Next article:
[30 Ways to Validate Configuration Files or Scripts in Linux](https://www.tecmint.com/check-configuration-files-linux/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/monit-linux-services-monitoring/#respond)** or
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
### 49 Comments
[Leave a Reply](https://www.tecmint.com/monit-linux-services-monitoring/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/6bcac9c86beae28afe99bb2b8712057b214548d93dde4645a3b7bed8051ef511?s=50&d=blank&r=g)
Poornresh
[ August 2, 2022 at 10:55 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-1855592)
Is it possible to collect telemetry data through Monit? I mean to know whether Monit can be used as a replacement for Opentelemetry.
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-1855592)
  2. ![](https://secure.gravatar.com/avatar/977b25417de2911040b7d3a0a2dad1e4d86607d1be73d61e8610449df6660a56?s=50&d=blank&r=g)
mike
[ July 27, 2022 at 2:37 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-1851323)
Yes, to monitor multiple hosts from a single dashboard you need to install **M-monit** , an enterprise application, with a one-time license fee (it is not expensive).
We use **Mmonit** at my work to monitor over 100 hosts, has email and slack notifications and metric charts, an excellent monitoring tool that’s much easier to set up and maintain than Nagios.
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-1851323)
  3. ![](https://secure.gravatar.com/avatar/1b669d65f5fe51a473648b3707a7159a2f03b5cfe8c694ccb33ddbc93d1f953c?s=50&d=blank&r=g)
EMILLY VITORIA SILVA BATISTA
[ July 26, 2021 at 7:17 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-1554781)
What are the disadvantages of MONIT?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-1554781)
  4. ![](https://secure.gravatar.com/avatar/63d42121d33f15e6e3397b943473cae221e2b61ff2530d331ed2ecf508965893?s=50&d=blank&r=g)
Sandip Bose
[ February 23, 2021 at 10:17 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-1439023)
Very helpful documentation on monit. I have a problem sending email alerts for events/service changes and I am getting the error message in the apigee-monit.log –
[EST Feb 22 23:34:38] error : Mail: STARTTLS required but the mail server doesn’t support it
Alert handler failed, retry scheduled for next cycle.
How can I work around this error ?
```
# vi /opt/apigee/data/apigee-monit/my-mail-config.conf

```
```
SET MAILSERVER  x.com PORT 25
USERNAME "EnterpriseServiceBus@x.com"  PASSWORD ""

# USING SSL, WITH TIMEOUT 30  SECONDS
  USING TLS
SET MAIL-FORMAT {
  from: apigeeadmin@x.com
  subject: Monit Alert -- Service: $SERVICE $EVENT on $HOST
}
SET ALERT sandip.bose@x.com

```
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-1439023)
  5. ![](https://secure.gravatar.com/avatar/38cdab79f9c50a9bd213cd9da33cbb789a5b6987f463e14e6cf5ec00aeab6c93?s=50&d=blank&r=g)
QuangPH
[ October 6, 2017 at 10:41 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-919443)
Do it monitor multi remote servers ?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-919443)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 6, 2017 at 12:02 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-919456)
@Quang,
Unfortunately, no its build to monitor remote servers, for that there is Nagios, you can install and monitor multiple remote Linux and Windows machines. For installation check out this article – <https://www.tecmint.com/install-nagios-in-linux/>
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-919456)
       * ![](https://secure.gravatar.com/avatar/38cdab79f9c50a9bd213cd9da33cbb789a5b6987f463e14e6cf5ec00aeab6c93?s=50&d=blank&r=g)
QuangPH
[ October 6, 2017 at 1:26 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-919470)
yes, but i see monit has useful function auto restart service when fail or not running, that a great !!!
have nagios-plugin do that?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-919470)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 6, 2017 at 3:50 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-919494)
@QuangPH,
No nagios plugin doesn’t provide auto restart of services functionality..
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-919494)
  6. ![](https://secure.gravatar.com/avatar/1ff4b99057c5c2e65455503240b9693a9d5940bcfa68b0669c6065e00b0cf225?s=50&d=blank&r=g)
Rafael
[ May 2, 2017 at 6:54 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-887423)
This tutorial is very good. I’m using Debian8, Nginx and ISPConfig. The article does not cite whether it needs or works with Apache or Nginx. So, will it work to monitor any service, either one or the other, and the rest, correct?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-887423)
  7. ![](https://secure.gravatar.com/avatar/badb911eb7986eb0dfa2658ac908f1786cfe6cb0d933e1661bd9328649353a6d?s=50&d=blank&r=g)
ASIF
[ April 21, 2016 at 11:19 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-773451)
Not able to install the monit package.. can you please help?
Last login: Wed Apr 20 14:00:19 2016 from 192.168.124.1
[root@www ~]# yum install monit -y
Loaded plugins: product-id, refresh-packagekit, security, subscription-manager
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
Local-Repo | 2.9 kB 00:00
Setting up Install Process
No package monit available.
Error: Nothing to do
[root@www ~]# yum install monit* -y –nogpgcheck
Loaded plugins: product-id, refresh-packagekit, security, subscription-manager
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
Setting up Install Process
No package monit* available.
Error: Nothing to do
[root@www ~]# rpm -q monit*
package monit* is not installed
[root@www ~]# rpm -ivh monit*
error: File not found by glob: monit*
[root@www ~]#
[root@www ~]#
[root@www ~]#
[root@www ~]# yum –enablerepo=epel install monit
Loaded plugins: product-id, refresh-packagekit, security, subscription-manager
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
[root@www ~]# yum –enablerepo=epel install monit -y –nogpgcheck
Loaded plugins: product-id, refresh-packagekit, security, subscription-manager
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-773451)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 21, 2016 at 11:43 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-773454)
@Asif,
First register your RHEL distributions to RHN subscription management portal to install and get updates for new packages, here is the guide on how to register RHEL distribution to RHN network <https://www.tecmint.com/enable-redhat-subscription-reposiories-and-updates-for-rhel-7/>
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-773454)
  8. ![](https://secure.gravatar.com/avatar/cd8d8a3f0b97f8b4dbdb2a8bc130469b6a5c161461b432276ce39dc75439ec5b?s=50&d=blank&r=g)
Question
[ November 21, 2015 at 4:31 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-710506)
I am looking for a tool that lists/logs all “read / write / sent / received” activities of any process in detail additionally.
Is that possible with this tool?
It would also be nice to restrict a critical process instead of deleting it like security tools like to do. I am also looking for a tool that monitors installation activities and maybe backups modified system values or at least let me know. Could anyone give me an advisement?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-710506)
     * ![](https://secure.gravatar.com/avatar/cd8d8a3f0b97f8b4dbdb2a8bc130469b6a5c161461b432276ce39dc75439ec5b?s=50&d=blank&r=g)
Question
[ November 21, 2015 at 5:14 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-710520)
I need also be sure about any access for example keyboard and mouse or other peripherals. Those psycho attacks are state of the art and there is no easy way to get sure about it so far or I just haven t found the right tool yet.
I will have a look if anyone has a suggestion for me later on. Thanks for reading :)
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-710520)
  9. ![](https://secure.gravatar.com/avatar/67feafaffd4a2246bacee38c378e813ab473011ec8d1a8801674c45ff6467620?s=50&d=blank&r=g)
Andrei L.
[ November 3, 2015 at 1:14 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-700121)
If “yum install monit” doesn’t work, try with “yum –enablerepo=epel install monit”
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-700121)
  10. ![](https://secure.gravatar.com/avatar/b78b7f65f006110c2ae6b93414bf795b815121b2a5e322d7dfdcdeefcb30d370?s=50&d=blank&r=g)
Octopus
[ August 19, 2015 at 7:42 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-647070)
Nice tutorial, just a small typo here: ” following command to stat the monit service”
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-647070)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 20, 2015 at 10:44 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-647431)
@Octopus,
Thanks for pointing out that typo, corrected in the article..
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-647431)
  11. ![](https://secure.gravatar.com/avatar/9fe72371bbaba8c2c9c5930f009dc2b2e0de158a37d4d273117632ea477249ad?s=50&d=blank&r=g)
Marcel
[ June 3, 2015 at 12:22 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-587800)
Thanks for this article btw ;)
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-587800)
  12. ![](https://secure.gravatar.com/avatar/9fe72371bbaba8c2c9c5930f009dc2b2e0de158a37d4d273117632ea477249ad?s=50&d=blank&r=g)
Marcel
[ June 3, 2015 at 12:21 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-587799)
Typo:
tail -f /var/log/monit
must be
tail -f /var/log/monit.log
Right?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-587799)
  13. ![](https://secure.gravatar.com/avatar/29a57c995cd82f09d077f97e74e6349601070c1796bdf3368c9d3e45c75780fb?s=50&d=blank&r=g)
Abhishek
[ April 9, 2015 at 6:21 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-538143)
Hi,
Can you please tell me how to send alert through monit if someone ssh server.
Thanks
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-538143)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 9, 2015 at 11:17 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-538297)
@Abhishek,
To get alerts about your server, just add the email address in monit.conf file.
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-538297)
  14. ![](https://secure.gravatar.com/avatar/607211400feaf8969755028ff055c47772f059d1b2dfa3ea0101541d865a5dbc?s=50&d=blank&r=g)
Stefan
[ February 9, 2015 at 12:13 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-478353)
Is monit able to monitor logging of services?
For instance, if a service hangs (stops logging) but the process is still running so it still has a pid. Will it be able to monitor that and force a kill on the pid and initiate a restart?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-478353)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 9, 2015 at 1:11 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-478404)
@Stefan,
It’s just a monitoring tool that monitors and alerts about the services which are in critical state, it doesn’t take any actions like you saying, you’ve to kill and restart manually..
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-478404)
  15. ![](https://secure.gravatar.com/avatar/950f25c6a842ed7e8a0247437a622e6b82280af42c56c35b7502e8ef5acaecb0?s=50&d=blank&r=g)
ejaz
[ July 11, 2014 at 10:51 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-212160)
can you send me step by step installation monit. on Ubuntu 12.04 32 desktop
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-212160)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 11, 2014 at 1:31 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-212241)
The given instructions also works on Ubuntu 12.04 32-bit Desktop. Have you tried these instructions?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-212241)
  16. ![](https://secure.gravatar.com/avatar/45f116fa047f09afda76c13a852448e07c8540c57fd520101ede3652e186a665?s=50&d=blank&r=g)
Jean
[ May 5, 2014 at 9:32 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-158287)
Hi Ravi,
Thx for this post. It really helps. i’m using Ubuntu 12.10 server, and i was wondering if it should be “mysql” instead of “mysqld” on the third and fourth row for the MySql monitoring services :
check process mysqld with pidfile /var/run/mysqld/mysqld.pid
group mysql
start program = “/etc/init.d/mysqld start”
stop program = “/etc/init.d/mysqld stop”
if failed host 127.0.0.1 port 3306 then restart
if 5 restarts within 5 cycles then timeout
Because when i use “mysqld” an error occur.
thx a lot
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-158287)
  17. ![](https://secure.gravatar.com/avatar/9dbeab8421a828caf7bbebf3e25c69a974aaa34e7638eec99eed07ae48fbc62f?s=50&d=blank&r=g)
Al
[ April 30, 2014 at 11:35 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-155839)
I am unable to access the webUI page and the message I am getting is “The connection was interrupted”and firewall is disabled already. below is my configuration:
set httpd port 2812 and
use address 172.16.172.200 # only accept connection from localhost
allow 172.16.172.200 # allow localhost to connect to the server and
allow admin:monit # require user ‘admin’ with password ‘monit’
allow @monit # allow users of group ‘monit’ to connect (rw)
allow @users readonly # allow users of group ‘users’ to connect readonly
Any help would be appreciated
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-155839)
  18. ![](https://secure.gravatar.com/avatar/12919d5da2c08095208541943f8c301d9ded040d304bbd3cfda4f916ddddc062?s=50&d=blank&r=g)
Mann
[ April 14, 2014 at 4:32 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-148635)
check system is not working for the remote host neither the running services are showing up in Monit window
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-148635)
  19. ![](https://secure.gravatar.com/avatar/12919d5da2c08095208541943f8c301d9ded040d304bbd3cfda4f916ddddc062?s=50&d=blank&r=g)
Mann
[ April 10, 2014 at 5:28 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-147302)
how to monitor windows machine with monit ???
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-147302)
  20. ![](https://secure.gravatar.com/avatar/e152e743f9627b8057bdc56150bb860eae70bc698276256c0e6cf753152b7793?s=50&d=blank&r=g)
Brent
[ March 3, 2014 at 8:13 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-129133)
Very nice. I’m quite new to linux and this tutorial got me through the basics without getting bogged down in all the different things that you can use monit for.
I appreciated you specifying the commands for the different linux versions. Often tutorials on websites assume you are using a certain flavor of linux, but never mention what that flavor is.
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-129133)
  21. ![](https://secure.gravatar.com/avatar/4a1ccc4ddfd32c70a1098cbcbbd70681bb88cb7fcd2b61836a972c78b047f77f?s=50&d=blank&r=g)
imran
[ March 1, 2014 at 2:32 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-128165)
I have written an article for moit and mmonit, to control your monit instance through web interface. hope this will help some one.


[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-128165)
  22. ![](https://secure.gravatar.com/avatar/514e948ec0e19cbd2247f7f4dca4d4bbc01e428bd9260c14ae056d77073f1d12?s=50&d=blank&r=g)
feroz
[ February 19, 2014 at 1:09 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-124098)
how to install it on server i have logged into my server using ssh, installed the monit , the monit status command showing everything fine in the ssh console,but i am unable to access the web panel from browser as
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-124098)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 19, 2014 at 1:18 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-124103)
Have you opened port 2812 on firewall?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-124103)
       * ![](https://secure.gravatar.com/avatar/514e948ec0e19cbd2247f7f4dca4d4bbc01e428bd9260c14ae056d77073f1d12?s=50&d=blank&r=g)
feroz
[ February 19, 2014 at 4:39 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-124145)
thanks that was the problem, now worked
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-124145)
       * ![](https://secure.gravatar.com/avatar/514e948ec0e19cbd2247f7f4dca4d4bbc01e428bd9260c14ae056d77073f1d12?s=50&d=blank&r=g)
feroz
[ February 19, 2014 at 5:46 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-124159)
Hi,do you know how can i show the server’s time in the browser’s panel?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-124159)
  23. ![](https://secure.gravatar.com/avatar/5d3b877df2a1fe91a56a7d0574cafa561cd9b102d91a6b356961d8d9d1b2cd80?s=50&d=blank&r=g)
venkat
[ January 8, 2014 at 5:52 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-102836)
i monitored all services using monit tool except
tomcat server i create tomcat as service also but process Id not created how to monitor tomcat using monit tool this is i am using tomcat script
#!/bin/bash
