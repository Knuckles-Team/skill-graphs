# SARG – Squid Analysis Report Generator and Internet Bandwidth Monitoring Tool
[Ravi Saive](https://www.tecmint.com/author/admin/ "View all posts by Ravi Saive")Last Updated: March 16, 2016 Read Time: 5 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [Squid](https://www.tecmint.com/category/squid-2/) [145 Comments](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comments)
**SARG** is an open source tool that allows you to analyse the squid log files and generates beautiful reports in **HTML** format with information about users, IP addresses, top accessed sites, total bandwidth usage, elapsed time, downloads, access denied websites, daily reports, weekly reports and monthly reports.
The **SARG** is very handy tool to view how much internet bandwidth is utilized by individual machines on the network and can watch on which websites the network’s users are accessing.
![Install Sarg Squid Log Analyzer](https://www.tecmint.com/wp-content/uploads/2014/01/Sarg-Squid-Log-Analyzer.png)Install Sarg Squid Log Analyzer in Linux
In this article I will guide you on how to install and configure **SARG** – **Squid Analysis Report Generator** on **RHEL** /**CentOS** /**Fedora** and **Debian** /**Ubuntu** /**Linux Mint** systems.
### Installing Sarg – Squid Log Analyzer in Linux
I assume that you already installed, configured and tested **Squid** server as a transparent proxy and **DNS** for the name resolution in caching mode. If not, please install and configure them first before moving further installation of **Sarg**.
**Important:** Please remember without the **Squid** and **DNS** setup, no use of installing sarg on the system it will won’t work at all. So, it’s a request to install them first before proceeding further to **Sarg** installation.
Follow these guides to install DNS and Squid in your Linux systems:
##### Install Cache-Only DNS Server
  1. [Install Cache Only DSN Server in RHEL/CentOS 7](https://www.tecmint.com/install-configure-cache-only-dns-server-in-rhel-centos-7/)
  2. [Install Cache Only DSN Server in RHEL/CentOS 6](https://www.tecmint.com/install-caching-only-dns-server-in-centos/)
  3. [Install Cache Only DSN Server in Ubuntu and Debian](https://www.tecmint.com/install-dns-server-in-ubuntu-14-04/)


##### Install Squid as Transparent Proxy
  1. [Setting Up Squid Transparent Proxy in Ubuntu and Debian](https://www.tecmint.com/install-squid-in-ubuntu/)
  2. [Install Squid Cache Server on RHEL and CentOS](https://www.tecmint.com/control-web-traffic-using-squid-and-cisco-router-in-linux/)


#### Step 1: Installing Sarg from Source
The ‘**sarg** ‘ package by default not included in **RedHat** based distributions, so we need to manually compile and install it from source tarball. For this, we need some additional pre-requisites packages to be installed on the system before compiling it from source.
##### On RedHat/CentOS/Fedora
```
# yum install –y gcc gd gd-devel make perl-GD wget httpd
```

Once you’ve installed all the required packages, download the latest **wget** command to download and install it as shown below.
```
# wget http://liquidtelecom.dl.sourceforge.net/project/sarg/sarg/sarg-2.3.10/sarg-2.3.10.tar.gz
# tar -xvzf sarg-2.3.10.tar.gz
# cd sarg-2.3.10
# ./configure
# make
# make install
```

##### On Debian/Ubuntu/Linux Mint
On **Debian** based distributions, **sarg** package can be easily install from the default repositories using **apt-get** package manager.
```
$ sudo apt-get install sarg
```

#### Step 2: Configuring Sarg
Now it’s time to edit some parameters in **SARG** main configuration file. The file contains lots of options to edit, but we will only edit required parameters like:
  1. Access logs path
  2. Output directory
  3. Date Format
  4. Overwrite report for the same date.


Open **sarg.conf** file with your choice of editor and make changes as shown below.
```
# vi /usr/local/etc/sarg.conf        [On **RedHat** based systems]
```
```
$ sudo nano /etc/sarg/sarg.conf        [On **Debian** based systems]
```

Now Uncomment and add the original path to your **squid access log** file.
```
# sarg.conf
#
# TAG:  access_log file
#       Where is the access.log file
#       sarg -l file
#
**access_log /var/log/squid/access.log**
```

Next, add the correct **Output directory** path to save the generate squid reports in that directory. Please note, under **Debian** based distributions the **Apache** web root directory is ‘**/var/www** ‘. So, please be careful while adding correct web root paths under your Linux distributions.
```
# TAG:  output_dir
#       The reports will be saved in that directory
#       sarg -o dir
#
**output_dir /var/www/html/squid-reports**
```

Set the correct **date format** for reports. For example, ‘**date_format e** ‘ will display reports in **‘dd/mm/yy** ‘ format.
```
# TAG:  date_format
#       Date format in reports: e (European=dd/mm/yy), u (American=mm/dd/yy), w (Weekly=yy.ww)
#
**date_format e**
```

Next, uncomment and set Overwrite report to ‘**Yes’**.
```
# TAG: overwrite_report yes|no
#      yes - if report date already exist then will be overwritten.
#       no - if report date already exist then will be renamed to filename.n, filename.n+1
#
**overwrite_report yes**
```

That’s it! Save and close the file.
#### Step 3: Generating Sarg Report
Once, you’ve done with the configuration part, it’s time to generate the squid log report using the following command.
```
# sarg -x        [On **RedHat** based systems]
```
```
# sudo sarg -x        [On **Debian** based systems]
```

##### Sample Output
```
[root@localhost squid]# sarg -x

SARG: Init
SARG: Loading configuration from /usr/local/etc/sarg.conf
SARG: Deleting temporary directory "/tmp/sarg"
SARG: Parameters:
SARG:           Hostname or IP address (-a) =
SARG:                    Useragent log (-b) =
SARG:                     Exclude file (-c) =
SARG:                  Date from-until (-d) =
SARG:    Email address to send reports (-e) =
SARG:                      Config file (-f) = /usr/local/etc/sarg.conf
SARG:                      Date format (-g) = USA (mm/dd/yyyy)
SARG:                        IP report (-i) = No
SARG:             Keep temporary files (-k) = No
SARG:                        Input log (-l) = /var/log/squid/access.log
SARG:               Resolve IP Address (-n) = No
SARG:                       Output dir (-o) = /var/www/html/squid-reports/
SARG: Use Ip Address instead of userid (-p) = No
SARG:                    Accessed site (-s) =
SARG:                             Time (-t) =
SARG:                             User (-u) =
SARG:                    Temporary dir (-w) = /tmp/sarg
SARG:                   Debug messages (-x) = Yes
SARG:                 Process messages (-z) = No
SARG:  Previous reports to keep (--lastlog) = 0
SARG:
SARG: sarg version: 2.3.7 May-30-2013
SARG: Reading access log file: /var/log/squid/access.log
SARG: Records in file: 355859, reading: 100.00%
SARG:    Records read: 355859, written: 355859, excluded: 0
SARG: Squid log format
SARG: Period: 2014 Jan 21
SARG: Sorting log /tmp/sarg/172_16_16_55.user_unsort
......
```

**Note** : The ‘**sarg -x’** command will read the ‘**sarg.conf** ‘ configuration file and takes the squid ‘**access.log** ‘ path and generates a report in html format.
#### Step 4: Assessing Sarg Report
The generated reports placed under ‘**/var/www/html/squid-reports/** ‘ or ‘**/var/www/squid-reports/** ‘ which can be accessed from the web browser using the address.
```
http://localhost/squid-reports
OR
http://ip-address/squid-reports
```

##### Sarg Main Window
![Squid Log Analyzer](https://www.tecmint.com/wp-content/uploads/2014/01/Squid-Log-Analyzer-1-620x430.png)Sarg Main Window
##### Specific Date
![Date Wise Report](https://www.tecmint.com/wp-content/uploads/2014/01/Squid-Log-Analyzer-2-620x430.png)Date Wise Report
##### User Report
![User Bandwidth Report](https://www.tecmint.com/wp-content/uploads/2014/01/Squid-Log-Analyzer-8-620x429.png)User Bandwidth Report
##### Top Accessed Sites
![Squid Top Accessed Sites](https://www.tecmint.com/wp-content/uploads/2014/01/Squid-Log-Analyzer-3-620x430.png)Top Accessed Sites
##### Top Sites and Users
![Squid Top Accessed Sites and Users](https://www.tecmint.com/wp-content/uploads/2014/01/Squid-Log-Analyzer-4-620x429.png)Top Accessed Sites and Users
##### Top Downloads
![Squid Top Downloads](https://www.tecmint.com/wp-content/uploads/2014/01/Squid-Log-Analyzer-5-620x430.png)Top Downloads
##### Denied Access
![Squid Denied Access](https://www.tecmint.com/wp-content/uploads/2014/01/Squid-Log-Analyzer-6-620x430.png)Denied Access Sites
##### Authentication Failures
![Squid Authentication Failures](https://www.tecmint.com/wp-content/uploads/2014/01/Squid-Log-Analyzer-7-620x429.png)Proxy Authentication Failures
#### Step 5: Automatic Generating Sarg Report
To automate the process of generating **sarg** report in given span of time via [cron jobs](https://www.tecmint.com/11-cron-scheduling-task-examples-in-linux/). For example, let’s assume you want to generate reports on **hourly** basis automatically, to do this, you need to configure a **Cron** job.
```
# crontab -e
```

Next, add the following line at the bottom of the file. Save and close it.
```
*** */1 * * * /usr/local/bin/sarg -x**
```

The above **Cron** rule will generate **SARG** report every **1 hour**.
### Reference Links
That’s it with **SARG**! I will be coming up with few more interesting articles on **Linux** , till then stay tuned to **TecMint.com** and don’t forget to add your valuable comments.
Tags [install sarg in linux](https://www.tecmint.com/tag/install-sarg-in-linux/), [sarg squid log analyzer](https://www.tecmint.com/tag/sarg-squid-log-analyzer/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[The Truth of Python and Perl – Features, Pros and Cons Discussed](https://www.tecmint.com/the-truth-of-python-and-perl-features-pros-and-cons-discussed/)
Next article:
[PHPlist – Open Source Email Newsletter Manager (Mass Mailing) Application for Linux](https://www.tecmint.com/phplist-open-source-email-newsletter-manager-mass-mailing-application-for-linux/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#respond)** or
