# How to Add Windows Host to Nagios Monitoring Server
[Ravi Saive](https://www.tecmint.com/author/admin/ "View all posts by Ravi Saive")Last Updated: January 7, 2015 Read Time: 7 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [108 Comments](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comments)
This article describes how to monitor **Windows** machines “**private** ” services such as **CPU load** , **Disk usage** , **Memory usage,** **Services** , etc. For this, we required to install an **NSClient++** addon on the **Windows** machine. The addon acts a proxy between the **Windows** machine and **Nagios** and monitors actual services by communicating with the **check_nt** plugin. The **check_nt** plugin already installed on the **Nagios Monitoring Server** , if you followed our **Nagios** installation guide.
We assume that you’ve already installed and configured **Nagios** server according to our following guides.
  1. [How to Install Nagios 4.0.1 on RHEL/CentOS 6.x/5.x and Fedora 19/18/17](https://www.tecmint.com/install-nagios-in-linux/)
  2. [Add Linux Host to Nagios Monitoring Server](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/)


To monitor **Windows Machines** you will need to follow several steps and they are:
  1. Install NSClient++ addon on the Windows Machine.
  2. Configure Nagios Server for monitoring Windows Machine.
  3. Add new host and service definitions for Windows machine monitoring.
  4. Restart the Nagios Service.


To make this guide simple and easier, a few of configuration already done for you in the **Nagios** installation.
  1. A **check_nt** command definition already added to the **command.cfg** file. This definition command is used by **check_nt** plugin to monitor Windows services.
  2. A windows-server host **template** already created in the **templates.cfg** file. This template allows you to add new Windows host definitions.


The above two files “**command.cfg** ” and “**templates.cfg** ” files can be found at **/usr/local/nagios/etc/objects/** directory. You can modify and add your own definitions that suits your requirement. But, I’d recommend you to follow the instructions described in this article and you will be successfully monitoring your windows host in less than **20 minutes**.
### Step 1: Installing NSClient++ Agent on Windows Machine
Please use the below instructions to install **NSClient++ Agent** on the **Remote Windows Host**. First download the latest stable version **NSClient++ 0.3.1** addon source files, which can be found at below link.
Once you’ve downloaded latest stable version, unzip the **NSClient++** files into a new **C:\NSClient++** directory.
Now open a **MS-DOS** command prompt from the **Start Screen** –> **Run** –> type ‘**cmd** ‘ and press enter and change to the **C:\NSClient++** directory.
```
C:\NSClient++
```

Next, register the **NSClient++** service on the system with the following command.
```
nsclient++ /install
```

Finally, install the **NSClient++ systray** with the following command.
```
nsclient++ SysTray
```

Open the **Windows Services Manager** and right click on **NSClient** go to **Properties** and then ‘**Log On** ‘ tab and click the check box that says “**Allow service to interact with the desktop** “. If it isn’t already allowed, please check the box to allow it to.
![Install NSClient++](https://www.tecmint.com/wp-content/uploads/2013/11/Install-NSClient++-620x413.png)Install NSClient++
Open **NSC.INI** file located at **C:\NSClient++** directory and uncomment all the modules defined in the “**modules** ” section, except for **CheckWMI.dll** and **RemoteConfiguration.dll**.
```
[modules]
;# NSCLIENT++ MODULES
;# A list with DLLs to load at startup.
;  You will need to enable some of these for NSClient++ to work.
; ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
; *                                                               *
; * N O T I C E ! ! ! - Y O U   H A V E   T O   E D I T   T H I S *
; *                                                               *
; ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
**FileLogger.dll
CheckSystem.dll
CheckDisk.dll
NSClientListener.dll
NRPEListener.dll
SysTray.dll
CheckEventLog.dll
CheckHelpers.dll**
;CheckWMI.dll
;
; RemoteConfiguration IS AN EXTREM EARLY IDEA SO DONT USE FOR PRODUCTION ENVIROMNEMTS!
;RemoteConfiguration.dll
; NSCA Agent is a new beta module use with care!
;NSCAAgent.dll
; LUA script module used to write your own "check daemon" (sort of) early beta.
;LUAScript.dll
; Script to check external scripts and/or internal aliases, early beta.
;CheckExternalScripts.dll
; Check other hosts through NRPE extreme beta and probably a bit dangerous! :)
;NRPEClient.dll
```

Uncomment the “**allowed_hosts** ” in the “**Settings** ” section and define the **IP address** of your **Nagios Monitoring Server** or leave it blank to allow any hosts to connect.
```
[Settings]
;# ALLOWED HOST ADDRESSES
;  This is a comma-delimited list of IP address of hosts that are allowed to talk to the all daemons.
;  If leave this blank anyone can access the daemon remotely (NSClient still requires a valid password).
;  The syntax is host or ip/mask so 192.168.0.0/24 will allow anyone on that subnet access
allowed_hosts=**172.16.27.41
**
```

Uncomment the “**port** ” in the “**NSClient** ” section and set to default port ‘**12489** ‘. Make sure to open ‘**12489** ‘ port on **Windows Firewall**.
```
[NSClient]
;# NSCLIENT PORT NUMBER
;  This is the port the NSClientListener.dll will listen to.
port=**12489
**
```

Finally start the **NSClient++** service with the following command.
```
nsclient++ /start
```

If your properly installed and configured, you should see a new icon in the system tray in yellow circle with a black ‘**M** ‘ inside.
### Step 2: Configuring Nagios Server and Add Windows Hosts
Now Login into **Nagios Server** and add some **object definitions** in **Nagios** configuration files to monitor new **Windows** machine. Open **windows.cfg** file for editing with **Vi** editor.
```
[root@tecmint]# vi /usr/local/nagios/etc/objects/windows.cfg
```

A sample Windows host definition already defined for the Windows machine, you can simply change the host definition like **host_name** , **alias** , and **address** fields to appropriate values of your **Windows** machine.
```
###############################################################################
###############################################################################
#
# HOST DEFINITIONS
#
###############################################################################
###############################################################################

# Define a host for the Windows machine we'll be monitoring
# Change the host_name, alias, and address to fit your situation

define host{
        use             windows-server  ; Inherit default values from a template
        host_name       winserver       ; The name we're giving to this host
        alias           My Windows Server       ; A longer name associated with the host
        address         172.31.41.53    ; IP address of the host
        }
```

Following services are already added and enabled in **windows.cfg** file. If you wish to add some more other service definitions that needs to be monitored, you can simple add those definitions to same configuration file. Make sure to change the **host_name** for these all services with **host_name** defined in the above step.
```
define service{
	use			generic-service
	host_name		winserver
	service_description	NSClient++ Version
	check_command		check_nt!CLIENTVERSION
	}

Add the following service definition to monitor the uptime of the Windows server.

define service{
	use			generic-service
	host_name		winserver
	service_description	Uptime
	check_command		check_nt!UPTIME
	}

Add the following service definition to monitor the CPU utilization on the Windows server and generate a CRITICAL alert if the 5-minute CPU load is 90% or more or a WARNING alert if the 5-minute load is 80% or greater.

define service{
	use			generic-service
	host_name		winserver
	service_description	CPU Load
	check_command		check_nt!CPULOAD!-l 5,80,90
	}

Add the following service definition to monitor memory usage on the Windows server and generate a CRITICAL alert if memory usage is 90% or more or a WARNING alert if memory usage is 80% or greater.

define service{
	use			generic-service
	host_name		winserver
	service_description	Memory Usage
	check_command		check_nt!MEMUSE!-w 80 -c 90
	}

Add the following service definition to monitor usage of the C:\ drive on the Windows server and generate a CRITICAL alert if disk usage is 90% or more or a WARNING alert if disk usage is 80% or greater.

define service{
	use			generic-service
	host_name		winserver
	service_description	C:\ Drive Space
	check_command		check_nt!USEDDISKSPACE!-l c -w 80 -c 90
	}

Add the following service definition to monitor the W3SVC service state on the Windows machine and generate a CRITICAL alert if the service is stopped.

define service{
	use			generic-service
	host_name		winserver
	service_description	W3SVC
	check_command		check_nt!SERVICESTATE!-d SHOWALL -l W3SVC
	}

Add the following service definition to monitor the Explorer.exe process on the Windows machine and generate a CRITICAL alert if the process is not running.

define service{
	use			generic-service
	host_name		winserver
	service_description	Explorer
	check_command		check_nt!PROCSTATE!-d SHOWALL -l Explorer.exe
	}
```

Lastly, uncomment the **windows.cfg** file in**/usr/local/nagios/etc/nagios.cfg**.
```
[root@tecmint]# vi /usr/local/nagios/etc/nagios.cfg
```
```
# Definitions for monitoring a Windows machine
**cfg_file=/usr/local/nagios/etc/objects/windows.cfg
**
```

Finally, verify the **Nagios** configuration files for any errors.
```
[root@tecmint]# /usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
```
```
Total Warnings: 0
Total Errors:   0

Things look okay - No serious problems were detected during the pre-flight check
```

If the verification process throws any error messages, fix those errors until the verification process completes without any error messages. Once’ you fix those errors, restart the Nagios service.
```
[root@tecmint]# service nagios restart

Running configuration check...done.
Stopping nagios: done.
Starting nagios: done.
```

That’s it. Now go to Nagios Monitoring Web interface at “**http://Your-server-IP-address/nagios** ” or “**http://FQDN/nagios** ” and Provide the username “**nagiosadmin** ” and password. Check that the **Remote Windows Host** was added and is being monitored.
![Nagios Monitor Windows Host](https://www.tecmint.com/wp-content/uploads/2013/11/Windows-Host-620x387.png)Nagios Monitor Windows Host
That’s it! for now, in my up-coming article I will show you how to add **Printer** and **Switches** to **Nagios Monitoring Server**. If you’re having any difficulties while adding **Windows** host to **Nagios**. Please do comment your queries via comment section, till then stay tuned to **Tecmint.com** for more such kind of valuable articles.
Tags [add windows to nagios](https://www.tecmint.com/tag/add-windows-to-nagios/), [monitor windows machine](https://www.tecmint.com/tag/monitor-windows-machine/), [nagios](https://www.tecmint.com/tag/nagios/), [nsclient++](https://www.tecmint.com/tag/nsclient/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Next article:
[CentOS 6.5 Released – Upgrade from CentOS 6.x to CentOS 6.5](https://www.tecmint.com/upgrade-centos/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#respond)** or
