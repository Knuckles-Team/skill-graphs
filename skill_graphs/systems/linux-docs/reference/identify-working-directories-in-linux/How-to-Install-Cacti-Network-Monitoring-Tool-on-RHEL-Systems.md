# How to Install Cacti (Network Monitoring) Tool on RHEL Systems
[Ravi Saive](https://www.tecmint.com/author/admin/ "View all posts by Ravi Saive")Last Updated: April 15, 2024 Read Time: 5 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [383 Comments](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comments)
The **Cacti** tool is an open-source, web-based solution for [network monitoring](https://www.tecmint.com/linux-performance-monitoring-tools/ "Network Monitoring Tools") and system graphing in IT businesses. Cacti allows users to poll services regularly to create graphs using RRDtool.
It’s typically used to graph time-series data for metrics like [network bandwidth utilization](https://www.tecmint.com/linux-network-bandwidth-monitoring-tools/ "Linux Bandwidth Monitoring Tools"), [CPU load](https://www.tecmint.com/understand-linux-load-averages-and-monitor-performance/ "Linux Load Average"), [running processes](https://www.tecmint.com/find-linux-processes-memory-ram-cpu-usage/ "Find Top Running Processes"), [disk space](https://www.tecmint.com/how-to-check-disk-space-in-linux/ "Check Disk Space Usage"), and more.
In this how-to, we will demonstrate how to install and set up a comprehensive network monitoring application called **Cacti** using the **Net-SNMP** tool on [RHEL-based distributions](https://www.tecmint.com/redhat-based-linux-distributions/ "RedHat-based Linux Distributions") such as **CentOS Stream** , **Fedora** , **Rocky** , and **Alma Linux** , using the [YUM](https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/ "Linux YUM Command") and [DNF](https://www.tecmint.com/dnf-commands-for-fedora-rpm-package-management/ "Linux DNF Command") package manager tools.
#### Cacti Required Packages
The **Cacti** required the following packages to be installed on your Linux operating system.
  * **Apache** : A Web server to display network graphs created by **PHP** and **RRDTool**.
  * **MySQL** : A Database server to store cacti information.
  * **PHP** : A script module to create graphs using **RRDToo** l.
  * **PHP-SNMP** : A **PHP** extension for **SNMP** to access data.
  * **NET-SNMP** : An SNMP (**Simple Network Management Protocol**) is used to manage the network.
  * **RRDTool** : A database tool to manage and retrieve time series data like **CPU load** , **Network Bandwidth,** etc.


For demonstration purposes, we used **Rocky Linux 9** to install the Cacti tool, but the same instructions work for all RHEL-based distributions.
