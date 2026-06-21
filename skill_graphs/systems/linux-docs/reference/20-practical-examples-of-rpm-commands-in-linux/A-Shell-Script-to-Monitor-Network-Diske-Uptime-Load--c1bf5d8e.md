# A Shell Script to Monitor Network, Diske, Uptime, Load, and RAM in Linux
[Ravi Saive](https://www.tecmint.com/author/admin/ "View all posts by Ravi Saive")Last Updated: April 5, 2024 Read Time: 3 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [Shell Scripting](https://www.tecmint.com/category/shell-scripting/) [189 Comments](https://www.tecmint.com/linux-server-health-monitoring-script/#comments)
The duty of a System Administrator is really tough as they have to [monitor the servers](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/ "Linux Monitoring Tools"), users, logs, [create backups](https://www.tecmint.com/linux-system-backup-tools/ "Linux Backup Tools"), and so on. For the [most repetitive tasks](https://www.tecmint.com/using-shell-script-to-automate-linux-system-maintenance-tasks/ "Linux System Maintenance Tasks"), many administrators write scripts to automate their day-to-day work.
Here, we have [written a shell script](https://www.tecmint.com/create-shell-scripts-in-linux/ "Create Shell Scripts in Linux") that aims to help newbies by providing information about their [system, network](https://www.tecmint.com/linux-performance-monitoring-tools/ "Network Monitoring Tools"), users, load, RAM, host, internal IP, external IP, [uptime](https://www.tecmint.com/linux-uptime-command-examples/ "Linux Uptime Command"), etc. While it may not automate all tasks of a typical system admin, it can be helpful in certain situations.
We have taken care of formatting the output to a certain extent. The script doesn’t contain any malicious content and it can be run using a normal user account. In fact, it is recommended to run this script as a user and not as root.
![Linux Server Health Monitoring](https://www.tecmint.com/wp-content/uploads/2015/05/Linux-Health-Monitoring.png)Shell Script to Monitor Linux System Health
You are free to use, modify, or redistribute the piece of code below, provided that you give proper credit to **Tecmint** and the author. We have customized the output to ensure that only the required output is generated.
Additionally, we have utilized variables that are typically unused by the Linux system and are likely available.
##### Dependency
There is no dependency required to use this shell script on a [standard Linux Distribution](https://www.tecmint.com/top-most-popular-linux-distributions/ "Popular Linux Distributions"). Moreover the script don’t requires root permission for execution purpose. However if you want to install it, you need to enter root password once.
## How Do I Install and Run Shell Script
First, use following [wget command](https://www.tecmint.com/10-wget-command-examples-in-linux/ "Download Files Using Wget Command") to download the monitor script `"tecmint_monitor.sh"` and make it executable by setting appropriate permissions.
```
wget https://tecmint.com/wp-content/scripts/tecmint_monitor.sh
chmod 755 tecmint_monitor.sh

```

It is strongly advised to install the script as user and not as root. It will ask for root password and will install the necessary components at required places.
To install `"tecmint_monitor.sh"` script, simple use `-i` (install) option as shown below.
```
./tecmint_monitor.sh -i

```

Enter **root** password when prompted. If everything goes well you will get a success message like shown below.
```
Password:
Congratulations! Script Installed, now run monitor command

```

After installation, you can run the script by calling command `'monitor'` from any location or user.
```
monitor

```

If you don’t like to install it, you need to include the location every-time you want to run it.
```
./Path/to/script/tecmint_monitor.sh

```

Now run monitor command from anywhere using any user account simply as:
```
monitor

```

![TecMint Monitor Script in Action](https://www.tecmint.com/wp-content/uploads/2015/05/TecMint-Monitor-Script.gif)
As soon as you run the command you get various System related information which are:
  * Internet Connectivity
  * OS Type
  * OS Name
  * OS Version
  * Architecture
  * Kernel Release
  * Hostname
  * Internal IP
  * External IP
  * Name Servers
  * Logged In users
  * Ram Usages
  * Swap Usages
  * Disk Usages
  * Load Average
  * System Uptime


Check the installed version of script using `-v` (version) switch.
```
monitor -v

tecmint_monitor version 0.1
Designed by Tecmint.com
Released Under Apache 2.0 License

```

##### Conclusion
This script is working out of the box on a few machines I have checked. It should work the same for you as well. If you find any bugs, let us know in the comments. This is not the end; it’s just the beginning. You can take it to any level from here.
We’ve received a few complaints that the script is not working on [some Linux distributions](https://www.tecmint.com/best-linux-distributions-for-beginners/ "Linux Distributions for Beginners"). One of our regular readers, **Mr. Andres Tarallo** , has taken the initiative and made the script compatible with all Linux distributions. You can find the updated script on
If you feel like editing the script and taking it further, you are free to do so, giving us proper credit. Also, share the updated script with us so that we can update this article and give you proper credit.
Don’t forget to share your thoughts or your script with us. We’re here to help you. Thank you for all the love you have given us. Keep Connected! Stay tuned.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[5 Best Microsoft Word Alternatives for Linux in 2024](https://www.tecmint.com/microsoft-word-alternatives-linux/)
Next article:
[How to Install Apache, MySQL/MariaDB and PHP in Linux](https://www.tecmint.com/install-apache-mysql-php-on-redhat-centos-fedora/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/linux-server-health-monitoring-script/#respond)** or
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
### 189 Comments
[Leave a Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/14c100141ec675cc514c6d66eddb6a8321e6473697094211a300d98e1c582c1c?s=50&d=blank&r=g)
Sven
[ April 5, 2024 at 3:20 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-2155500)
Great script, but it shows only one external IP. I have ipv4 and ipv6. I see only ipv6.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-2155500)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 8, 2024 at 10:37 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-2156487)
@Sven,
To include checking IPv6 address alongside IPv4, you can modify the script as follows:
```
# Check Internal IPv4 and IPv6
internalip=$(hostname -I)
echo -e '\E[32m'"Internal IPv4 :" $tecreset $(echo $internalip | awk '{print $1}')
echo -e '\E[32m'"Internal IPv6 :" $tecreset $(echo $internalip | awk '{print $2}')

# Check External IPv4 and IPv6
externalip=$(curl -s ifconfig.me)
echo -e '\E[32m'"External IPv4 : $tecreset "$(echo $externalip | awk '{print $1}')
echo -e '\E[32m'"External IPv6 : $tecreset "$(echo $externalip | awk '{print $2}')

```
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-2156487)
  2. ![](https://secure.gravatar.com/avatar/8ae081e4982df30d3cd2ed5b8f5f2b9675ca4da8082ce58a9a921dfa4bb16736?s=50&d=blank&r=g)
nova
[ December 29, 2021 at 5:21 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1691799)
Thank you so much, tecmint group. The script is great and working…
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1691799)
  3. ![](https://secure.gravatar.com/avatar/8ae081e4982df30d3cd2ed5b8f5f2b9675ca4da8082ce58a9a921dfa4bb16736?s=50&d=blank&r=g)
Nova Nova
[ December 29, 2021 at 3:50 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1691779)
Good day, sir, I have copied the GitHub link to download the script, but I received an error message, the page was not found.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1691779)
  4. ![](https://secure.gravatar.com/avatar/d1f92f40289c5e3de26dee43aabc15033bfab736005db3be115525ab41b14fa9?s=50&d=blank&r=g)
Bayu
[ July 14, 2020 at 10:23 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1344761)
Hi, can you help me? your script `tecmint_monitoring.sh` not working to get data `df -h` because my server on AWS cloud.
How to get data `df -h` to show inyour script `tecmint_montoring.sh` if i’ve filesystem like this:
```
Filesystem      Size  Used Avail Use% Mounted on
udev            2.0G     0  2.0G   0% /dev
tmpfs           395M  804K  394M   1% /run
/dev/xvda1       30G   18G   12G  60% /
tmpfs           2.0G     0  2.0G   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           2.0G     0  2.0G   0% /sys/fs/cgroup
/dev/loop0       29M   29M     0 100% /snap/amazon-ssm-agent/2012
/dev/loop1       97M   97M     0 100% /snap/core/9436
/dev/loop2       18M   18M     0 100% /snap/amazon-ssm-agent/1566
/dev/loop3       98M   98M     0 100% /snap/core/9289
tmpfs           395M     0  395M   0% /run/user/1000

```

thanks
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1344761)
     * ![](https://secure.gravatar.com/avatar/8c2fdc1484fc6282a8cb3d2b4be8a5bf18a0b75300a3932df7f7cce64a14092b?s=50&d=blank&r=g)
Omkar
[ July 15, 2020 at 3:00 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1344873)
Hi Bayu,
Just remove **“| grep ‘Filesystem\|/dev/sda*'”** from “# Check Disk Usages” line.
You will get all the mount points in the display. You have run the installation command again to reflect the changes.
regards,
Omkar
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1344873)
       * ![](https://secure.gravatar.com/avatar/d1f92f40289c5e3de26dee43aabc15033bfab736005db3be115525ab41b14fa9?s=50&d=blank&r=g)
Bayu
[ July 18, 2020 at 2:06 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1345422)
OK, thank you very much.
that’s works for me, and now I will send the results using email. I have used this instruction
```
#! / bin / bash
./tecmint_monitor.sh 2> & 1> script.out
mail -r alert@mydomain.com -s "Server monitoring result" youremail@domain.com <script.out

```

but there is still an error like this:
```
./tecmint_monitor.sh: 26: ./tecmint_monitor.sh: [[: not found
./tecmint_monitor.sh: 36: ./tecmint_monitor.sh: [[: not found
./tecmint_monitor.sh: 43: ./tecmint_monitor.sh: [[: not found

```

can you help me again?
thanks
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1345422)
  5. ![](https://secure.gravatar.com/avatar/5472ff4dc1541d3762e05ac1efa2b5668fcc1674506cc09db20031abe8de0587?s=50&d=blank&r=g)
Anoop
[ April 17, 2020 at 12:00 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1328156)
How to remove this script from server
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1328156)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 17, 2020 at 1:02 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1328162)
@Anoop,
Just remove the downloaded script…
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1328162)
  6. ![](https://secure.gravatar.com/avatar/b3980f0f9ab3e106b8934557f5a07f7c61020daa8b7c08ed4b68a14a8571f370?s=50&d=blank&r=g)
yuravg
[ March 6, 2020 at 3:07 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1320173)
For ‘OS Version’ : Linux Debian GNU/Linux 9 (stretch) 4.9.0-11-amd64(4.9.0-11-amd64 x86_64)
‘top -n 1 -b’ stdout:
top – 22:27:53 up 13 min, 9 users, load average: 1.70, 2.23, 1.63
So ‘tecmint_monitor.sh’ display:
Load Average : average:2.02,2.35,
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1320173)
  7. ![](https://secure.gravatar.com/avatar/2bb3d1c3988df1ec642b187d49defb81ddfdbb647f1c42eeee01f5245b866d89?s=50&d=blank&r=g)
singaravelan
[ March 4, 2020 at 11:16 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1319952)
Include this also in GitHub link.
```
# Last Reboot Time
lastreboottime=$(who -b | awk '{print $3,$4}')
echo -e '\E[32m'"Last Reboot Time :" $tecreset $lastreboottime

```
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1319952)
  8. ![](https://secure.gravatar.com/avatar/11512a00ca7269944571867013024b9c6e3311f6e9b21adf43e4a3c8ba2b5aa5?s=50&d=blank&r=g)
Sivakumar
[ September 16, 2019 at 1:34 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1245308)
While running the given script in Ubuntu 18.04.3 LTS by using sh command, it throughout error like below.
`tecmint_monitor.sh: 23: tecmint_monitor.sh: [[: not found
 tecmint_monitor.sh: 33: tecmint_monitor.sh: [[: not found
 tecmint_monitor.sh: 40: tecmint_monitor.sh: [[: not found`
Please check and do the needful
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1245308)
  9. ![](https://secure.gravatar.com/avatar/de33d46b067fe3348725fe410e1de282349fb09eadf9abae56399490968ef091?s=50&d=blank&r=g)
Rumesh
[ August 29, 2019 at 9:41 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1233721)
How i can put it to run continuously?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1233721)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 29, 2019 at 10:23 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1233742)
@Rumesh,
Use a [cron scheduler command](https://www.tecmint.com/11-cron-scheduling-task-examples-in-linux/) to run it every hour or every day.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1233742)
  10. ![](https://secure.gravatar.com/avatar/40dbe9867f04ee656df82b758c0dbb92e9860e552abea7faa794cd64a4969a86?s=50&d=blank&r=g)
John Hosie
[ March 6, 2019 at 2:23 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1108288)
Followed your instructions to install on RHEL 5.8, and then ran “monitor”, with the results below:
```
[root@civaky3 ~]# monitor

```

##### Sample Output
```
Internet:  Connected
Operating System Type :  GNU/Linux
cat: /etc/os-release: No such file or directory
OS Name : OS Version : Architecture :  x86_64
Kernel Release :  2.6.18-308.13.1.el5
Hostname :  civaky3.truthtechnologies.com
hostname: invalid option -- I
Usage: hostname [-v] {hostname|-F file}      set hostname (from file)
       domainname [-v] {nisdomain|-F file}   set NIS domainname (from file)
       hostname [-v] [-d|-f|-s|-a|-i|-y|-n]  display formatted name
       hostname [-v]                         display hostname

       hostname -V|--version|-h|--help       print info and exit

    dnsdomainname=hostname -d, {yp,nis,}domainname=hostname -y

    -s, --short           short host name
    -a, --alias           alias names
    -i, --ip-address      addresses for the hostname
    -f, --fqdn, --long    long host name (FQDN)
    -d, --domain          DNS domain name
    -y, --yp, --nis       NIS/YP domainname
    -F, --file            read hostname or NIS domainname from given file

   This command can read or set the hostname or the NIS domainname. You can
   also read the DNS domain or the FQDN (fully qualified domain name).
   Unless you are using bind or NIS for host lookups you can change the
   FQDN (Fully Qualified Domain Name) and the DNS domain name (which is
   part of the FQDN) in the /etc/hosts file.
Internal IP :
External IP :  208.82.219.167
Name Servers :  204.117.214.10 199.2.252.10
Logged In users :
jhosie   pts/2        2019-03-05 15:45 (65.123.231.210)
free: invalid option -- h
usage: free [-b|-k|-m|-g] [-l] [-o] [-t] [-s delay] [-c count] [-V]
  -b,-k,-m,-g show output in bytes, KB, MB, or GB
  -l show detailed low and high memory statistics
  -o use old format (no -/+buffers/cache line)
  -t display total for RAM + swap
  -s update every [delay] seconds
  -c update [count] times
  -V display version information and exit
Ram Usages :
Swap Usages :
Disk Usages :
Filesystem            Size  Used Avail Use% Mounted on
/dev/sda3              97M   40M   52M  44% /boot
Load Average :  loadaverage:0.18,
System Uptime Days/(HH:MM) :  331 days

```

It would be nice to know what it was supposed to do. I’m sure it wasn’t what happened.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1108288)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 6, 2019 at 10:21 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1108421)
@John,
You are using very old distribution, just update the `hostname` and `free` command options supported by your distro in the script.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1108421)
  11. ![](https://secure.gravatar.com/avatar/c8a6a5ad810ee44666d6e2ea82e010fee4b46c9fa19ee1c38ff68901376f538f?s=50&d=blank&r=g)
Junaid
[ December 11, 2018 at 4:33 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1082645)
How to send its output as an email?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1082645)
     * ![](https://secure.gravatar.com/avatar/44cb61f3df69fbb4d0447713514ccfbc66658faf9a262475803298611e2e2a7a?s=50&d=blank&r=g)
Mansur Ul Hasan
[ December 11, 2018 at 8:34 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1082667)
Redirect stdout to file and then use mail function to mail to your email
for this wrap your script into another bash script and run that
```
vim anotherscript.sh

```

Put below content into script
```
#!/bin/bash
./Path/to/script/tecmint_monitor.sh 2>&1 > script.out

mail -r alert@mydomain.com -s "Server monitoring result "  youremail@domain.com < script.out

```

Now run your script
```
# sh anotherscript.sh

```
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1082667)
  12. ![](https://secure.gravatar.com/avatar/1b4b9f91e7caecf686a7b1ff27da128fd12ff62fb4edf44bdb2926e0cd65ebf2?s=50&d=blank&r=g)
Baljit Singh
[ November 19, 2018 at 11:06 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1061482)
How to run this script against multiple servers?
Do I need to install this script to all the servers then extract the data, Please advise
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1061482)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 20, 2018 at 10:32 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1061885)
@Baljit,
Yes, you have to install this Linux monitoring script on all Linux servers to monitor.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1061885)
       * ![](https://secure.gravatar.com/avatar/c8a6a5ad810ee44666d6e2ea82e010fee4b46c9fa19ee1c38ff68901376f538f?s=50&d=blank&r=g)
Junaid
[ December 11, 2018 at 4:34 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1082646)
How to get its output in mail?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1082646)
  13. ![](https://secure.gravatar.com/avatar/aa66d81a6763c3a684fe7f1ea3d99db2f7666c44c51513b20244e2cbb8ce4e40?s=50&d=blank&r=g)
Prasad M
[ November 2, 2018 at 10:00 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1055018)
Hi Andres Tarallo,
Good day!, as I am working on Migration work for 250+ servers, wanted to collect the server related info along with cluster details.
I would need your help to how to identify the servers are configured in cluster (VCS, RedHat Cluster, SCS, VxVM).
Please suggest.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1055018)
  14. ![](https://secure.gravatar.com/avatar/49512b3de77caa67c3d69735e5d2210f4dc8f3e622daf0c72776900a2821ef99?s=50&d=blank&r=g)
Rasheed
[ August 1, 2018 at 1:01 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1019919)
the information loads up really slow on my server
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1019919)
  15. ![](https://secure.gravatar.com/avatar/722576bc7618126553f9389d2a7a6a1611d69a63c3d11391d69f6bf1e925aa97?s=50&d=blank&r=g)
joejoe
[ May 7, 2018 at 8:41 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-990177)
What if I want to run this script against a list of 100 remote servers and put that all that data in a nice spreadsheet how do I get that accomplished
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-990177)
     * ![](https://secure.gravatar.com/avatar/4f2d0693690cbb324e00ec4ed125c5b33a48df416d967ff62105be1f8ed3e1d5?s=50&d=blank&r=g)
Andres Tarallo
[ August 1, 2018 at 9:56 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1020165)
You could run the script via ssh. It won’t be a difficult task to make it run. Putting data on a Spreadsheet will require more work, maybe programming in Python/PERL or your favourite language with a API for dealing with spreadsheets.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-1020165)
  16. ![](https://secure.gravatar.com/avatar/9ef1c3c9c6143d05ca0920b29360b8fc0d28041e4d3b199ceda4dc887fff24d0?s=50&d=blank&r=g)
Ruparam Choudhary
[ March 11, 2018 at 7:48 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-975338)
how can we find on squid that which internal ip is sending request to any-site by using Tls1.0
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-975338)
  17. ![](https://secure.gravatar.com/avatar/9ef1c3c9c6143d05ca0920b29360b8fc0d28041e4d3b199ceda4dc887fff24d0?s=50&d=blank&r=g)
Ruparam Choudhary
[ March 11, 2018 at 7:44 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-975337)
Very good job
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-975337)
  18. ![](https://secure.gravatar.com/avatar/44f61ab5125423bbf537fb6e15822c88825425f7eead8f12c80630e2f9aff7f8?s=50&d=blank&r=g)
Ganesh
[ November 30, 2017 at 7:31 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-942554)
Hey Tecmint,
Thanks for the awesome script! Made my job more easier. And appreciating the author for taking initiative in writing this simple script.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-942554)
  19. ![](https://secure.gravatar.com/avatar/78735bbc27a4fb9db1c5aacfe0f60771da55397bee3bdc1b2e240cc30201f5f4?s=50&d=blank&r=g)
Daniel
[ November 30, 2017 at 4:21 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-942498)
Authentication failure and I put my pass correctly???!!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-942498)
  20. ![](https://secure.gravatar.com/avatar/633fb3d71fc39eea83f7bfceb3a190867ec44f8170e53cd40131043f3b11704a?s=50&d=blank&r=g)
Shahid
[ August 22, 2017 at 7:11 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-907716)
“Edward” just use “-m” by changing free -h to free -m
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-907716)
  21. ![](https://secure.gravatar.com/avatar/1ded167c6363c97409dae7092558fbef069231f5cd8d7efe96442567a2b3225d?s=50&d=blank&r=g)
Edward
[ July 17, 2017 at 10:58 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-900172)
The Free -h is giving an error.
I tried -l and -m but the monitor still outputs -h. As though it isn't reading the file. any ideas?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-900172)
  22. ![](https://secure.gravatar.com/avatar/f464956703ff549c4667ba77470d99a5589e0d08a9a2459b0b33d9ca090d3665?s=50&d=blank&r=g)
Tom
[ June 8, 2017 at 6:40 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-894367)
GetVersionFromFile()
{
VERSION=`cat $1 | tr “\n” ‘ ‘ | sed s/.*VERSION.*=\ // `
}
I put # front of them，The Script‘s result did not change.What is their role?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-894367)
  23. ![](https://secure.gravatar.com/avatar/942b19d62de8a974bc8911adf9fe4977ce4074f7341ca3daaf21c0644b47cd6c?s=50&d=blank&r=g)
trilochan
[ May 24, 2017 at 5:17 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-891849)
Hi, I want this script output in mail, how to do please suggest me.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-891849)
  24. ![](https://secure.gravatar.com/avatar/fb27ac0f88102877d97c8b77583bce230f801c846d22c9d702ccf7a3773fecd7?s=50&d=blank&r=g)
fernandofvh
[ May 14, 2017 at 7:28 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-889577)
That love is only the logical answer to your work. Thanks.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-889577)
  25. ![](https://secure.gravatar.com/avatar/5dfd21b9a865993f2b510e19c7d2865bc3d6d2b28ac5671b87514d63b73fc64f?s=50&d=blank&r=g)
Rob
[ April 6, 2017 at 3:38 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-881495)
Hi can you help me with this shell script for system admin.
Create system admin menu with options below. And design the shell script to trap all exit/escape/suspend signals, so the user cannot do anything outside the menu. (Like output never getout of terminal when pressing cntrl + c, Only Quot command should terminate output)
As a second step, start creating menu options. For example:
u) manage users
n) manage network
q) quit
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-881495)
  26. ![](https://secure.gravatar.com/avatar/44cb61f3df69fbb4d0447713514ccfbc66658faf9a262475803298611e2e2a7a?s=50&d=blank&r=g)
Mansur
[ March 8, 2017 at 12:31 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-873968)
I was having some issues while running on centos so i made some edits.
`
 #! /bin/bash
