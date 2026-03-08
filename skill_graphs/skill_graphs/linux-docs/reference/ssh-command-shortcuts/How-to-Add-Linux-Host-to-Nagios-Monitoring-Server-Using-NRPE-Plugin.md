# How to Add Linux Host to Nagios Monitoring Server Using NRPE Plugin
[Ravi Saive](https://www.tecmint.com/author/admin/ "View all posts by Ravi Saive")Last Updated: December 15, 2022 Read Time: 9 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [Nagios](https://www.tecmint.com/category/nagios/) [529 Comments](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comments)
In the first part of the Nagios series article, we’ve explained in detail how to install and configure the latest version of **Nagios Core** and **Nagios Plugins** in [RHEL-based distributions](https://www.tecmint.com/redhat-based-linux-distributions/ "Best RedHat-based Linux Distributions") such as **CentOS Stream** , **Rocky Linux** , **AlmaLinux,** and **Fedora**.
In this article, we will show you how to add a **Remote Linux** machine and its services to the **Nagios Core Monitoring** host using **NRPE** (**Nagios Remote Plugin Executor**) agent.
We hope you already have **Nagios Core** installed and running properly. If not, please use the following installation guide to install it on the system.
**[ You might also like:[How to Install Nagios Monitoring in RHEL, Rocky, and AlmaLinux](https://www.tecmint.com/install-nagios-in-linux/ "Install Nagios Monitoring in RHEL, Rocky, and AlmaLinux") ]**
If you are planning to add a remote **Windows** host to the **Nagios** monitoring server, use the following guide:
**[ You might also like:[How to Add Windows Host to Nagios Monitoring Server](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/ "Add Windows Host to Nagios Monitoring Server") ]**
Once you’ve installed it, you can proceed further to install the **NRPE** agent on your **Remote Linux** host. Before heading further, let us give you a short description of **NRPE**.
Table of Contents
Toggle
  * [What is NRPE?](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#What_is_NRPE)
  * [Installation of NRPE Plugin in Nagios Server and Remote Linux Host](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Installation_of_NRPE_Plugin_in_Nagios_Server_and_Remote_Linux_Host)
    * [Installing Nagios Plugins and NRPE On Remote Linux Host](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Installing_Nagios_Plugins_and_NRPE_On_Remote_Linux_Host)
      * [Step 1: Install Required Dependencies](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_1_Install_Required_Dependencies)
      * [Step 2: Create Nagios User](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_2_Create_Nagios_User)
      * [Step 3: Install the Nagios Plugins](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_3_Install_the_Nagios_Plugins)
      * [Step 4: Extract Nagios Plugins](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_4_Extract_Nagios_Plugins)
      * [Step 5: Compile and Install Nagios Plugins](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_5_Compile_and_Install_Nagios_Plugins)
      * [Step 6: Installing NRPE Plugin](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_6_Installing_NRPE_Plugin)
      * [Step 7: Configuring NRPE Plugin](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_7_Configuring_NRPE_Plugin)
      * [Step 8: Open NRPE Port in Firewall](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_8_Open_NRPE_Port_in_Firewall)
      * [Step 8: Verify NRPE Daemon Locally](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_8_Verify_NRPE_Daemon_Locally)
      * [Step 9: Customize NRPE Commands](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_9_Customize_NRPE_Commands)
    * [Installing NRPE On Nagios Monitoring Server](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Installing_NRPE_On_Nagios_Monitoring_Server)
      * [Step 1: Install NRPE Plugin in Nagios](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_1_Install_NRPE_Plugin_in_Nagios)
      * [Step 2: Verify NRPE Daemon Remotely](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_2_Verify_NRPE_Daemon_Remotely)
  * [Adding Remote Linux Host to Nagios Monitoring Server](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Adding_Remote_Linux_Host_to_Nagios_Monitoring_Server)
    *       * [Step 1: Creating Nagios Host and Services File](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_1_Creating_Nagios_Host_and_Services_File)
      * [Step 2: Configuring Nagios Host and Services File](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_2_Configuring_Nagios_Host_and_Services_File)
      * [Step 3: Configuring NRPE Command Definition](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_3_Configuring_NRPE_Command_Definition)
      * [Step 4: Monitoring Remote Linux in Nagios](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Step_4_Monitoring_Remote_Linux_in_Nagios)
      * [Conclusion](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#Conclusion)


The **NRPE** (**Nagios Remote Plugin Executor**) plugin allows you to monitor any remote **Linux** /**Unix** services, network devices, or resources like **CPU load** , **Swap** , **Memory usage** , **Online users** , etc. on local/remote Linux machines.
After all, these local resources are not mostly exposed to external machines, an **NRPE** agent must be installed and configured on the remote machines.
**Note** : The **NRPE** addon requires that **Nagios Plugins** must be installed on the remote Linux machine. Without these, the **NRPE** daemon will not work and will not monitor anything.
To use the **NRPE** , you will need to do some additional tasks on both the **Nagios Monitoring Server** and the **Remote Linux Host** that the NRPE is installed on. We will be covering both installation parts separately.
Please use the below instructions to install **Nagios Plugins** and **NRPE** daemon on the **Remote Linux Host**.
We need to install required libraries like **gcc** , **glibc** , **glibc-common,** and **GD** and its development libraries using the [yum package manager](https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/ "Linux YUM Command Examples").
```
# yum install -y gcc glibc glibc-common gd gd-devel make net-snmp openssl-devel tar wget

```

Create a new nagios user account and set a password.
```
# useradd nagios
# passwd nagios

```

Create a directory for nagios plugin installation and all its future downloads.
```
# mkdir /root/nagios
# cd /root/nagios

```

Now [wget command](https://www.tecmint.com/10-wget-command-examples-in-linux/).
```
# wget https://nagios-plugins.org/download/nagios-plugins-2.3.3.tar.gz

```

Run the following [tar command](https://www.tecmint.com/18-tar-command-examples-in-linux/) to extract the source code tarball.
```
# tar -xvf nagios-plugins-2.3.3.tar.gz

```

After, extracting one new folder will appear in that directory.
```
**# ls -l**

total 2724
drwxr-xr-x. 15 root root    4096 Mar 11  2020 nagios-plugins-2.3.3
-rw-r--r--.  1 root root 2782610 Mar 11  2020 nagios-plugins-2.3.3.tar.gz

```

Next, compile and install nagios plugins using the following commands
```
# cd nagios-plugins-2.3.3
# ./configure
# make
# make install

```

Set the permissions on the plugin directory using the [chown command](https://www.tecmint.com/chown-command-examples/ "Chown Command Examples").
```
# chown nagios.nagios /usr/local/nagios
# chown -R nagios.nagios /usr/local/nagios/libexec

```

To install the nrpe plugin, first, [wget command](https://www.tecmint.com/10-wget-command-examples-in-linux/ "Wget Linux File Downloader").
```
# cd /root/nagios
# wget https://github.com/NagiosEnterprises/nrpe/releases/download/nrpe-4.0.2/nrpe-4.0.2.tar.gz

```

Unpack the NRPE source code tarball.
```
# tar xzf nrpe-4.0.2.tar.gz
# cd nrpe-4.0.2

```

Compile and install the **NRPE** addon.
```
# ./configure
# make all

```

**Note** : If you get the following error while running the ‘**make all** ‘ command:
```
In file included from ../include/common.h:34,
                 from ./nrpe.c:38:
/usr/include/openssl/err.h:413:15: note: declared here
  413 | unsigned long ERR_get_error_line_data(const char **file, int *line,
      |               ^~~~~~~~~~~~~~~~~~~~~~~
/usr/bin/ld: /tmp/ccWQBjHb.o: in function `init_ssl':
/root/nagios/nrpe-4.0.2/src/./nrpe.c:474: undefined reference to `get_dh2048'
collect2: error: ld returned 1 exit status
make[1]: *** [Makefile:48: nrpe] Error 1

```

Then, you need to disable SSL for nrpe configuration with `./configure --disable-ssl` flag as shown.
```
# ./configure --disable-ssl
# make all

```

Next, install the NRPE plugin daemon, and sample config files.
```
# make install-plugin
# make install-daemon
# make install-config

```

Install the **NRPE** daemon under **systemd** as a service.
```
# make install-init

```

Now open **/usr/local/nagios/etc/nrpe.cfg** file and add the **local host** and **IP address** of the **Nagios Monitoring Server**.
```
allowed_hosts=127.0.0.1,192.168.102

```

Next, enable and restart the nrpe service.
```
# systemctl enable nrpe
# systemctl restart nrpe

```

Make sure that the **Firewall** on the local machine will allow the **NRPE** daemon to be accessed from remote servers. To do this, run the following iptables command.
```
# firewall-cmd --zone=public --add-port=5666/tcp
# firewall-cmd --zone=public --add-port=5666/tcp --permanent

```

Run the following [netstat command](https://www.tecmint.com/20-netstat-commands-for-linux-network-management/ "Netstat Command Examples") to verify the NRPE daemon working correctly under **systemd**.
```
**# netstat -at | grep nrpe
OR
# netstat -na | grep "5666"**


tcp        0      0 0.0.0.0:nrpe            0.0.0.0:*               LISTEN
tcp6       0      0 [::]:nrpe               [::]:*                  LISTEN

```

If you get output similar to the above, means it working correctly. If not, make sure to check the following things.
  * Make sure to check that the nrpe entry is correctly added in the**/etc/services** file.
  * The **allowed_hosts** contains an entry for “**nagios_ip_address** ” in the **/usr/local/nagios/etc/nrpe.cfg** file.
  * Check for the errors in the **system log** files for about **nrpe** and fix those problems.


Next, verify the NRPE daemon is functioning properly by running the “**check_nrpe** ” command that was installed earlier for testing purposes.
```
# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1

```

You will get the following string on the screen, it shows you what version of NRPE is installed:
```
NRPE v4.0.2

```

The default NRPE configuration file that got installed has several command definitions that will be used to monitor this machine. The sample configuration file is located at.
```
# vi /usr/local/nagios/etc/nrpe.cfg

```

The following are the default command definitions that are located at the bottom of the configuration file. For the time being, we assume you are using these commands. You can check them by using the following commands.
```
# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1 -c check_users

USERS OK - 1 users currently logged in |users=1;5;10;0
```
```
# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1 -c check_load

OK - load average: 3.90, 4.37, 3.94|load1=3.900;15.000;30.000;0; load5=4.370;10.000;25.000;0; load15=3.940;5.000;20.000;0;
```
```
# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1 -c check_hda1

DISK OK - free space: /boot 154 MB (84% inode=99%);| /boot=29MB;154;173;0;193
```
```
# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1 -c check_total_procs

PROCS CRITICAL: 297 processes
```
```
# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1 -c check_zombie_procs

PROCS OK: 0 processes with STATE = Z
```

You can edit and add new command definitions by editing the NRPE config file. Finally, you’ve successfully installed and configured NRPE agent on the **Remote Linux Host**.
Now it’s time to install an **NRPE** component and add some services to your **Nagios Monitoring Server** …
Now login into your **Nagios Monitoring Server**. Here you will need to do the following things:
  * Install the **check_nrpe** plugin.
  * Create a **Nagios command definition** using the **check_nrpe** plugin.
  * Create a **Nagios host** and **add service definitions** for monitoring the **remote Linux host**.


Go to the nagios download directory and **wget** command.
```
# cd /root/nagios
# wget https://github.com/NagiosEnterprises/nrpe/releases/download/nrpe-4.0.2/nrpe-4.0.2.tar.gz
```

Unpack the NRPE source code tarball.
```
# tar xzf nrpe-4.0.2.tar.gz
# cd nrpe-4.0.2

```

Compile and install the NRPE addon.
```
# ./configure
# make all
# make install-plugin
# make install-daemon
# make install-init

```

Make sure that the **check_nrpe** plugin can communicate with the **NRPE** daemon on the remote **Linux** host. Add the **IP address** in the command below with the IP address of your **Remote Linux** host.
```
# /usr/local/nagios/libexec/check_nrpe -H **<remote_linux_ip_address>**

```

You will get a string back that shows you what version of NRPE is installed on the remote host, like this:
```
NRPE v4.0.2
```

If your receive a plugin time-out error, then check the following things.
  * Make sure your firewall isn’t blocking the communication between the **remote host** and the **monitoring host**.
  * Make sure that the **NRPE** daemon is installed correctly under **systemd**.
  * Make sure that the **remote Linux** host firewall rules block the **monitoring server** from communicating with the **NRPE** daemon.


To add a remote host you need to create two new files “**hosts.cfg** ” and “**services.cfg** ” under the “**/usr/local/nagios/etc/** ” location.
```
# cd /usr/local/nagios/etc/
# touch hosts.cfg
# touch services.cfg

```

Now add these two files to the main Nagios configuration file. Open the **nagios.cfg** file with any editor.
```
# vi /usr/local/nagios/etc/nagios.cfg

```

Now add the two newly created files as shown below.
```
# You can specify individual object config files as shown below:
cfg_file=/usr/local/nagios/etc/hosts.cfg
cfg_file=/usr/local/nagios/etc/services.cfg

```

Now open **hosts.cfg** file and add the **default host template name** and **define remote hosts** as shown below. Make sure to replace **host_name** , **alias** , and **address** with your remote host server details.
```
# vi /usr/local/nagios/etc/hosts.cfg
```
```
## Default Linux Host Template ##
define host{
name                            linux-box               ; Name of this template
use                             generic-host            ; Inherit default values
check_period                    24x7
check_interval                  5
retry_interval                  1
max_check_attempts              10
check_command                   check-host-alive
notification_period             24x7
notification_interval           30
notification_options            d,r
contact_groups                  admins
register                        0                       ; DONT REGISTER THIS - ITS A TEMPLATE
}

## Default
define host{
use                             linux-box               ; Inherit default values from a template
**host_name                       tecmint		        ; The name we're giving to this server**
**alias                           CentOS 6                ; A longer name for the server**
**address                         5.175.142.66            ; IP address of Remote Linux host**
}
```

Next open **services.cfg** file and add the following services to be monitored.
```
# vi /usr/local/nagios/etc/services.cfg
```
```
define service{
        use                     generic-service
        host_name               tecmint
        service_description     CPU Load
        check_command           check_nrpe!check_load
        }

define service{
        use                     generic-service
        host_name               tecmint
        service_description     Total Processes
        check_command           check_nrpe!check_total_procs
        }

define service{
        use                     generic-service
        host_name               tecmint
        service_description     Current Users
        check_command           check_nrpe!check_users
        }

define service{
        use                     generic-service
        host_name               tecmint
        service_description     SSH Monitoring
        check_command           check_nrpe!check_ssh
        }

define service{
        use                     generic-service
        host_name               tecmint
        service_description     FTP Monitoring
        check_command           check_nrpe!check_ftp
        }
```

Now NRPE command definition needs to be created in **commands.cfg** file.
```
# vi /usr/local/nagios/etc/objects/commands.cfg

```

Add the following NRPE command definition at the bottom of the file.
```
###############################################################################
# NRPE CHECK COMMAND
#
# Command to use NRPE to check remote host systems
###############################################################################

define command{
        command_name check_nrpe
        command_line $USER1$/check_nrpe -H $HOSTADDRESS$ -c $ARG1$
        }
```

Finally, verify Nagios Configuration files for any errors.
```
# /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg

Total Warnings: 0
Total Errors:   0

```

Finally, restart Nagios to apply recent configuration changes:
```
# systemctl restart nagios

```

Now go to the **Nagios Monitoring Web** interface at “**http://Your-server-IP-address/nagios** ” or “**http://FQDN/nagios”** and Provide the username “**nagiosadmin** ” and **password**. Check that the **Remote Linux Host** was added and is being monitored.
![Monitoring Remote Linux Host in Nagios](https://www.tecmint.com/wp-content/uploads/2013/11/Monitoring-Remote-Linux-Host-in-Nagios.png)Monitoring Remote Linux Host in Nagios
That’s it! for now, in my upcoming article, I will show you how to add a **Windows host** to **Nagios monitoring Server**. If you’re facing any difficulties while adding the remote host to **Nagios**.
Please do comment on your queries or problem via the comment section, till then stay tuned to **Tecmint.com** for more such valuable articles.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install Nagios Monitoring in RHEL, Rocky, and AlmaLinux](https://www.tecmint.com/install-nagios-in-linux/)
Next article:
[How To Run a Cron Job Every 30 Seconds in Linux](https://www.tecmint.com/run-cronjob-every-x-seconds/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#respond)** or
