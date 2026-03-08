[Skip to content](https://www.tecmint.com/monitor-disk-usage-bash-script/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/monitor-disk-usage-bash-script/)
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
  * [Pro Courses](https://www.tecmint.com/monitor-disk-usage-bash-script/ "Linux Online Courses")
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


[](https://www.tecmint.com/monitor-disk-usage-bash-script/)
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
  * [Pro Courses](https://www.tecmint.com/monitor-disk-usage-bash-script/ "Linux Online Courses")
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


[](https://www.tecmint.com/monitor-disk-usage-bash-script/)
# A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%
[Ravi Saive](https://www.tecmint.com/author/admin/ "View all posts by Ravi Saive")Last Updated: September 17, 2025 Read Time: 5 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [4 Comments](https://www.tecmint.com/monitor-disk-usage-bash-script/#comments)
If you’ve ever run a Linux system in production or even just kept a personal server, you’ll know that running out of disk space is one of the most frustrating issues. Suddenly, your applications stop working, databases won’t write new data, and log files keep filling up like a runaway train.
The good news is that **Linux** makes it surprisingly easy to [monitor disk usage](https://www.tecmint.com/linux-tools-to-monitor-disk-partition-usage/ "Monitor Linux Disk Partitions Usage") and catch problems before they happen. All you need is a small shell script, a bit of logic, and maybe an email alert (or a message to your Slack channel, if you’re fancy).
In this article, we’ll build a simple script that checks your disk usage and sends an alert if it goes over 80%.
## Step 1: Check Disk Usage on Linux
Before writing a script, you need to know your current disk space usage on your system using the [df command](https://www.tecmint.com/how-to-check-disk-space-in-linux/ "Check Disk Space Usage").
```
df -h

```

The `-h` flag means “**human-readable** ”, so instead of showing raw blocks of data, it formats the output in **GB** and **MB** , which is much easier to understand.
![Check Linux Disk Usage](https://www.tecmint.com/wp-content/uploads/2014/01/Check-Linux-Disk-Usage.png)Check Linux Disk Usage
In the example above, the root partition `/` (`/dev/sda1`) is sitting at `45%`, which is perfectly healthy, but once it starts climbing past `80%`, that’s our red flag; it means space is running out.
## Step 2: Create a Script to Monitor Disk Usage
Now that you know how to check disk usage manually, let’s turn it into something automatic using a shell script, which are great for such things because they let us take commands we normally run and tie them together with a little bit of logic.
Here’s a very simple script to monitor your root `(/)` partition:
```
#!/bin/bash

# Set threshold (percentage)
THRESHOLD=80

# Extract the usage percentage for root filesystem
USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

# Compare usage against threshold
if [ "$USAGE" -ge "$THRESHOLD" ]; then
    echo "Warning: Disk usage is at ${USAGE}% on $(hostname)" | mail -s "Disk Alert: $(hostname)" user@example.com
fi

```

Let’s break down what’s happening here:
  * `THRESHOLD=80` → This is the limit we care about, anything higher is too risky.
  * `df -h /` → This checks the root filesystem only.
  * `awk 'NR==2 {print $5}'` → From the df output, this grabs the “**Use%** ” column.
  * `sed 's/%//'` → Strips off the `%` sign so we can treat it as a number.
  * The `if` block → If the disk usage goes above the threshold, it triggers an alert.


Right now, the script sends an email using the **mail** command. If you haven’t set up email on your system, don’t worry, I’ll show you how to set it up.
## Step 3: Monitor All Partitions Disk Usage
Most servers don’t rely on a single partition; instead, they’re typically split into several, such as `/`, `/home`, `/var`, or even `/data`. If you only keep an eye on the root `(/)` partition, you risk missing critical issues elsewhere, for example, if `/var` fills up with logs, your applications could fail even though `/` still has plenty of space.
Here’s a slightly improved version that checks all mounted filesystems:
```
#!/bin/bash

THRESHOLD=80

# Loop through each filesystem listed by df
df -h | grep '^/dev/' | while read line; do
    USAGE=$(echo $line | awk '{print $5}' | sed 's/%//')
    PART=$(echo $line | awk '{print $6}')

    if [ "$USAGE" -ge "$THRESHOLD" ]; then
        echo "Warning: Partition $PART is at ${USAGE}% on $(hostname)" | mail -s "Disk Alert: $(hostname)" user@example.com
    fi
done

```

Now, instead of checking just `/`, it runs through every filesystem under `/dev/` and if any partition crosses `80%`, you’ll get a warning email.
## Step 4: Automating the Script with Cron
**Cron** is a simple scheduling service on Linux that can [run commands at fixed times](https://www.tecmint.com/create-and-manage-cron-jobs-on-linux/ "Create Cron Jobs on Linux") or intervals. You can use it to make your disk monitoring script run automatically, say, every hour.
To set it up, open your crontab with:
```
crontab -e

```

Add this line at the bottom:
```
0 * * * * /path/to/disk_check.sh

```

This means:
  * `0` → run at the start of the hour.
  * `* * * *` → every hour, every day.
  * `/path/to/disk_check.sh` → replace this with the actual location of your script.


Save and exit, and cron will take care of the rest. From now on, your script will quietly check disk usage in the background and alert you if things look bad.
## Step 5: Testing the Script
Before you rely on this script, it’s smart to test it. After all, you don’t want to wait until your disk is actually 80% full to find out if your alert system works.
The easiest way to test is by temporarily lowering the threshold:
```
THRESHOLD=1

```

That way, the script will almost certainly trigger an alert right away since most partitions are at least `1%` full. Once you confirm that emails or logs are working, change it back to `80`.
If you’re not ready to configure email, you can replace the **mail** command with something simpler, like:
```
echo "Warning: Partition $PART is at ${USAGE}% on $(hostname)"

```

This will just print the alert to your terminal, which is useful for quick debugging.
## Step 6: Setting Up Email Notifications
Our script uses the mail command to send alerts, but this tool isn’t always available by default. You’ll need to install it first:
```
sudo apt install mailutils  [On Debian]
sudo yum install mailx      [On RHEL]

```

Once installed, you should make sure your server can actually send emails, which may require some extra setup, like configuring [Postfix](https://www.tecmint.com/setup-postfix-mail-server-and-dovecot-with-mariadb-in-centos/ "Setup Postfix Mail Server"), **Gmail SMTP** , or a third-party service such as **SendGrid**.
If you don’t want to deal with email right now, you can still make the script useful by logging alerts to a file:
```
echo "Disk usage alert: $PART at $USAGE%" >> /var/log/disk_alert.log

```

That way, you can check the log later or use the following command to watch alerts in real time.
```
tail -f /var/log/disk_alert.log

```

## Step 7: When to Go Beyond Shell Scripts
Shell scripts are great for learning and are often enough for a single server or small project, but if you’re running multiple servers or need more detailed monitoring, you’ll probably want to move to dedicated monitoring tools.
  * [Nagios](https://www.tecmint.com/install-nagios-xi-on-ubuntu/ "Install Nagios XI on Ubuntu") → One of the oldest and most reliable monitoring systems.
  * [Zabbix](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/ "Install Zabbix on Linux") → Good if you want dashboards, graphs, and a central place to monitor many servers.
  * **Prometheus + Grafana** → A modern setup where **Prometheus** collects metrics, and **Grafana** makes beautiful dashboards to visualize them.


##### Wrapping Up
With just a few lines of shell scripting, you’ve created a lightweight disk monitoring system that keeps an eye on your partitions and warns you before things get critical.
By setting a threshold, adding a bit of logic, and scheduling it with cron, you’ve automated a task that would otherwise require constant manual checks, which means fewer surprises, fewer outages, and more peace of mind.
If you want to take your Linux automation further, check out our related guide: [How to Automate Daily Linux Health Checks with a Bash Script + Cron](https://www.tecmint.com/bash-script-automate-system-health-checks/ "Automate Daily Linux Health Checks").
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Top 6 Linux Apps You Should Install This Week (Sept 15-21)](https://www.tecmint.com/linux-apps-to-try-this-week-september-15-21/)
Next article:
[How to Install cPanel & WHM on AlmaLinux 9](https://www.tecmint.com/install-cpanel-whm-almalinux/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/monitor-disk-usage-bash-script/#respond)** or
## Related Posts
[![Linux Disk I/O Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2015/04/Linux-Disk-IO-Monitoring-Tools.png)](https://www.tecmint.com/monitor-linux-disk-io-performance/ "7 Best Tools to Monitor and Debug Disk I/O Performance in Linux")
[7 Best Tools to Monitor and Debug Disk I/O Performance in Linux](https://www.tecmint.com/monitor-linux-disk-io-performance/)
[![Linux Performance Monitoring with Command-Line Tools](https://www.tecmint.com/wp-content/uploads/2023/08/command-line-monitoring-tools-linux.webp)](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/ "24 Best Command Line Tools to Monitor Linux Performance")
[24 Best Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)
[![atop: System and process monitor for Linux](https://www.tecmint.com/wp-content/uploads/2025/06/atop-System-and-process-monitor-for-Linux.webp)](https://www.tecmint.com/atop-linux-performance-monitoring/ "How to Install ‘atop’ to Monitor Real-Time System Performance")
[How to Install ‘atop’ to Monitor Real-Time System Performance](https://www.tecmint.com/atop-linux-performance-monitoring/)
[![Bash Script to Monitor Linux Health Daily](https://www.tecmint.com/wp-content/uploads/2025/06/bash-script-automate-system-health-checks.webp)](https://www.tecmint.com/bash-script-automate-system-health-checks/ "How to Automate Daily Linux Health Checks with a Bash Script + Cron")
[How to Automate Daily Linux Health Checks with a Bash Script + Cron](https://www.tecmint.com/bash-script-automate-system-health-checks/)
[![Network Bandwidth Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2013/07/network-bandwidth-monitoring-tools.webp)](https://www.tecmint.com/network-bandwidth-monitoring-tools/ "5 Modern VnStat PHP Replacements for Bandwidth Monitoring")
[5 Modern VnStat PHP Replacements for Bandwidth Monitoring](https://www.tecmint.com/network-bandwidth-monitoring-tools/)
[![btop Linux monitoring tool](https://www.tecmint.com/wp-content/uploads/2025/02/btop-linux-system-monitoring-tool.png)](https://www.tecmint.com/btop-system-monitoring-tool-for-linux/ "btop: A Modern and Resourceful System Monitor")
[btop: A Modern and Resourceful System Monitor](https://www.tecmint.com/btop-system-monitoring-tool-for-linux/)
### 4 Comments
[Leave a Reply](https://www.tecmint.com/monitor-disk-usage-bash-script/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/1c6a989553e68c5277b7f574442c4d54718bd3053b5fc2521e36562f9be646d2?s=50&d=blank&r=g)
Jalal Hajigholamali
[ September 22, 2025 at 1:06 pm  ](https://www.tecmint.com/monitor-disk-usage-bash-script/#comment-2344306)
Thanks for sharing! I tested it on my system and it works perfectly.
[Reply](https://www.tecmint.com/monitor-disk-usage-bash-script/#comment-2344306)
  2. ![](https://secure.gravatar.com/avatar/?s=50&d=blank&r=g)
Liam T
[ July 3, 2025 at 6:43 pm  ](https://www.tecmint.com/monitor-disk-usage-bash-script/#comment-99387)
I tried the script on my Ubuntu server and it worked perfectly. Love the simplicity of it. Now I’m thinking about adding logging too.
[Reply](https://www.tecmint.com/monitor-disk-usage-bash-script/#comment-99387)
  3. ![](https://secure.gravatar.com/avatar/?s=50&d=blank&r=g)
Daniel R
[ January 27, 2025 at 4:03 pm  ](https://www.tecmint.com/monitor-disk-usage-bash-script/#comment-114287)
Can anyone suggest how to integrate this with Slack instead of email? Would love to get alerts right in my channel.
[Reply](https://www.tecmint.com/monitor-disk-usage-bash-script/#comment-114287)
  4. ![](https://secure.gravatar.com/avatar/ea2c580cdbb4f779fc97b74e03482c42db4647dcf662dbaafb6d76e32fbc4f80?s=50&d=blank&r=g)
Jitendra.K
[ September 27, 2024 at 4:06 pm  ](https://www.tecmint.com/monitor-disk-usage-bash-script/#comment-114289)
Thanks for this guide!
I just set up the script on my home server, and I love that it sends me alerts before things get critical.
[Reply](https://www.tecmint.com/monitor-disk-usage-bash-script/#comment-114289)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/monitor-disk-usage-bash-script/#respond)
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
[How to Delete Root Mails (Mailbox) File in Linux](https://www.tecmint.com/delete-root-mails-mailbox-file-in-linux/)
[How to Repair and Defragment Linux System Partitions and Directories](https://www.tecmint.com/defragment-linux-system-partitions-and-directories/)
[Linux rmdir Command Examples for Beginners](https://www.tecmint.com/rmdir-command-examples/)
[Stop Using Only cd: Learn pushd, popd, and zoxide in Linux](https://www.tecmint.com/cd-command-in-linux/)
[PacVim – A Game That Teaches You Vim Commands](https://www.tecmint.com/learn-vi-commands-with-pacvim-game/)
[20 Netstat Commands for Linux Network Management](https://www.tecmint.com/20-netstat-commands-for-linux-network-management/)
## Linux Server Monitoring Tools
[Sysdig – A Powerful System Monitoring and Troubleshooting Tool for Linux](https://www.tecmint.com/sysdig-system-monitoring-and-troubleshooting-tool-for-linux/)
[How to Use ‘fsck’ to Repair Linux File System Errors](https://www.tecmint.com/fsck-repair-file-system-errors-in-linux/)
[How to Setup Central Logging Server with Rsyslog in Linux](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/)
[Cockpit – A Powerful Tool to Monitor and Administer Multiple Linux Servers via Browser](https://www.tecmint.com/cockpit-monitor-multiple-linux-servers-via-web-browser/)
[4 Useful Commandline Tools to Monitor MySQL Performance in Linux](https://www.tecmint.com/mysql-performance-monitoring/)
[10 Tips On How to Use Wireshark to Analyze Packets in Your Network](https://www.tecmint.com/wireshark-network-traffic-analyzer-for-linux/)
## Learn Linux Tricks & Tips
[Bash-it – Bash Framework to Control Your Scripts and Aliases](https://www.tecmint.com/bash-it-control-shell-scripts-aliases-in-linux/)
[How to Christmassify Your Linux Terminal and Shell](https://www.tecmint.com/christmassify-linux-terminal-and-shell/)
[How to Add a New Disk to an Existing Linux Server](https://www.tecmint.com/add-new-disk-to-an-existing-linux/)
[How to Set and Unset Local, User and System Wide Environment Variables in Linux](https://www.tecmint.com/set-unset-environment-variables-in-linux/)
[4 Ways to Batch Convert Your PNG to JPG and Vice-Versa](https://www.tecmint.com/linux-image-conversion-tools/)
[How to Clear BASH Command Line History in Linux](https://www.tecmint.com/clear-command-line-history-in-linux/)
## Best Linux Tools
[16 Best Microsoft Teams Alternatives For Linux in 2024](https://www.tecmint.com/microsoft-teams-alternatives/)
[32 Best File Managers and Explorers [GUI + CLI] for Linux in 2024](https://www.tecmint.com/linux-file-managers/)
[11 Best GitHub Alternatives to Host Open Source Projects](https://www.tecmint.com/github-alternatives-to-host-open-source-projects/)
[18 Best NodeJS Frameworks for App Development in 2023](https://www.tecmint.com/best-nodejs-frameworks-for-developers/)
[11 Best GUI Tools for Linux System Administrators in 2024](https://www.tecmint.com/gui-tools-for-linux-system-administrators/)
[11 Best Screen Recorders For Linux in 2024](https://www.tecmint.com/best-linux-screen-recorders-for-desktop-screen-recording/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/monitor-disk-usage-bash-script/ "Scroll back to top")
Search for:
