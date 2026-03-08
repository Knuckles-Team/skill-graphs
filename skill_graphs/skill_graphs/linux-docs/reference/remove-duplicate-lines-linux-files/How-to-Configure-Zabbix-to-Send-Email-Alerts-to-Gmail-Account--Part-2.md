# How to Configure Zabbix to Send Email Alerts to Gmail Account – Part 2
[Matei Cezar](https://www.tecmint.com/author/cezarmatei/ "View all posts by Matei Cezar")Last Updated: October 28, 2021 Read Time: 5 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/), [Zabbix](https://www.tecmint.com/category/zabbix/) [52 Comments](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comments)
If you are using **Zabbix** to monitor your infrastructure you might want to receive email alerts from your local domain somewhere on a public internet domain, even if you don’t own a valid registered internet domain name with a mail server which you can configure on your own.
This tutorial will briefly discuss how to set up a **Zabbix** server to send mail reports to a **Gmail** address by using the **SSMTP** program, without the need to install and configure any local **MTA** daemon, such as **Postfix** , **Exim,** etc.
#### Requirements
  * [How to Install Zabbix on RHEL/CentOS and Debian/Ubuntu – Part 1](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/ "Install Zabbix in Linux")


### Step 1: Install and Configure SSMTP
**1.** **SSMTP** is a small software, which does not fulfill any of the functionality of a mail server, but only delivers emails from a local machine to an external email address on a **mailhub**.
To install the **SSMTP** program alongside with **mailutils** package that you will use to send mails, issue the following command on your [RedHat-based distros](https://www.tecmint.com/redhat-based-linux-distributions/ "The Best RedHat-based Linux Distributions") and [Debian like server](https://www.tecmint.com/debian-based-linux-distributions/ "Best Debian-based Linux Distributions"):
```
# yum install msmtp mailx               [On **RHEL**/**CentOS**]
$ sudo apt-get install ssmtp mailutils       [On **Debian/Ubuntu**]

```

**2.** After the packages are installed on the system, configure the **SSMTP** program to send local emails to your **Gmail** account by opening the main configuration file for editing with your favorite text editor and root privileges and use the following parameter settings:
```
# vi /etc/msmtprc                       [On **RHEL**/**CentOS**]
$ sudo nano /etc/ssmtp/ssmtp.conf            [On **Debian/Ubuntu**]

```

**MSMTP** settings for **GMAIL** account.
Configuration of /etc/msmtprc
```
#set default values for all following accounts.
defaults
auth           on
tls            on
tls_trust_file    /etc/pki/tls/certs/ca-bundle.crt
logfile        ~/.msmtp.log
# Gmail
account        gmail
host           smtp.gmail.com
port           587
from           admin@xx.com
user           admin@xx.com
password       gmailpassword

# Set a default account
account default : gmail

```

**SSMTP** settings for **GMAIL** account.
Configuration of /etc/ssmtp/ssmtp.conf
```
root=gmail-username@gmail.com
mailhub=smtp.gmail.com:587
rewriteDomain=your_local_domain
hostname=your_local_FQDN
UseTLS=Yes
UseSTARTTLS=Yes
AuthUser=Gmail_username
AuthPass=Gmail_password
FromLineOverride=YES

```
![Configure Zabbix Email Alerts](https://www.tecmint.com/wp-content/uploads/2015/08/Configure-Zabbix-Email-Alerts-599x450.png)Configure Zabbix Email Alerts
### Step 2: Gmail Tests for Zabbix Email Alerts
**3.** On the next step it’s time to send a locally generated email to a **Gmail** account by issuing the below command.
```
# echo "Body test email from 'hostname -f' "| mail -s "subject here" gmail_user@gmail.com

```
![Gmail Tests](https://www.tecmint.com/wp-content/uploads/2015/08/Gmail-Tests-620x148.png)Gmail Tests
**4.** Normally, **Gmail** prevents different types of authentications to their servers from your account, so, in case you get the error “**mail: cannot send a message: Process exited with non-zero status** ”, then login to your Gmail account from the browser and navigate to the following link
![Manage Secure Gmail Apps](https://www.tecmint.com/wp-content/uploads/2015/08/Manage-Secure-Gmail-Apps-620x268.png)Manage Secure Gmail Apps
**5.** After you have turned on the **Less Secure Apps** feature on your **Gmail** account, run the above mail command again and verify your Inbox after a few seconds to check if the locally generated email has been successfully delivered – you should normally see the email has incoming from Gmail.
![Mail Delivery Confirm](https://www.tecmint.com/wp-content/uploads/2015/08/Mail-Delivery-Confirm-620x249.jpg)Mail Delivery Confirm
### Step 3: Configure Zabbix Sendmail Script
**6.** Further, based on the `$(which mail)` command creates the following Bash script to Zabbix **alertscripts** directory with the following content and gives it execute permissions:
```
# vi /usr/local/share/zabbix/alertscripts/zabbix-sendmail            [On **RHEL**/**CentOS**]
$ sudo nano /usr/local/share/zabbix/alertscripts/zabbix-sendmail     [On **Debian/Ubuntu**]

```

Script content:
```
#!/bin/bash
echo "$3" | /usr/bin/mail -s "$2" $1

```
![Configure Sendmail Zabbix](https://www.tecmint.com/wp-content/uploads/2015/08/Configure-Sendmail-Zabbix-620x202.png)Configure Sendmail Zabbix
Next, set the execute permission on the script file.
```
# chmod +x /usr/local/share/zabbix/alertscripts/zabbix-sendmail

```

**7.** Next, as previously, test the script functionality by sending a local **email to a Gmail** account. The way to run the script with positional parameters is explained above:
```
# /usr/local/share/zabbix/alertscripts/zabbix-sendmail gmail_username@gmail.com "Subject here" "Body of the message here"

```
![Send Mail to Gmail Account from Linux](https://www.tecmint.com/wp-content/uploads/2015/08/Linux-Send-Mail-to-Gmail-Account-620x71.png)Send Mail to Gmail Account
Afterward, verify **Gmail** Inbox and check if the new local message has arrived.
![Verify Mail Delivery](https://www.tecmint.com/wp-content/uploads/2015/08/Verify-Mail-Delivery-620x263.jpg)Verify Mail Delivery
### Step 4: Configure Zabbix to Send Alerts to Gmail
**8.** If the tests so far we’re successful, then you can move to the next step and set up Zabbix to send generated email alerts to Gmail. First, log in to the Zabbix web interface and navigate to the following menu: **Administration** -> **Media types** -> **Create** media type.
![Zabbix Administration](https://www.tecmint.com/wp-content/uploads/2015/08/Zabbix-Administration-620x238.png)Zabbix Administration
**9.** On the next screen enter an arbitrary **Name** to uniquely identify the script in the **Zabbix** configurations (in this example **Send-Email-Script** is used), choose **Script** as **Type** from the list and enter the name of the Bash script created earlier (**zabbix-sendmail** used in this tutorial) to send email from the command line (don’t use the path for the script, only the script name). When you’re done, hit the **Add** button below to reflect changes.
![Create Zabbix Email Alerts](https://www.tecmint.com/wp-content/uploads/2015/08/Create-Zabbix-Email-Alerts-620x264.png)Create Zabbix Email Alerts
**10.** Further, let’s configure an email address to which you will send Zabbix alerts. Go to **Profile** -> **Media** -> **Add** and a new pop-up window should appear.
Here, select the name of the script that you have earlier named (in this example **Send-Email-Script** is used) for **Type** , enter the **Gmail** address to which you will send emails, choose the time period (week, hours) when email reports should be active for sending, choose the severity of the messages that you want to receive on your Gmail address, select **Enabled** as **Status** and hit the **Add** button to add the media. Finally hit the **Update** button to apply the configuration.
![Configure Zabbix Mail Address](https://www.tecmint.com/wp-content/uploads/2015/08/Configure-Zabbix-Mail-Alerts-620x417.png)Configure Zabbix Mail Address ![Zabbix Update Configuration](https://www.tecmint.com/wp-content/uploads/2015/08/Zabbix-Update-Configuration-620x242.png)Zabbix Update Configuration
**11.** On the next step, enable the default Zabbix alerts by navigating to **Configuration** -> **Actions** , select as the **Event Source** – > **Triggers** from the right menu, and hit on **Disabled Status** in order to enable it. Repeat the step for **Event Source** – > **Internal** or other custom-created Actions and you’re done.
![Enable Default Zabbix Mail Alert](https://www.tecmint.com/wp-content/uploads/2015/08/Enable-Default-Zabbix-Mail-Alert-620x232.png)Enable Default Zabbix Mail Alert ![Zabbix Enabled Actions](https://www.tecmint.com/wp-content/uploads/2015/08/Zabbix-Enabled-Actions-620x241.png)Zabbix Enabled Actions
Wait for a while for **Zabbix** to start to gather information and generate some reports, then verify your **Gmail Inbox** and you should see some **Zabbix alerts** submitted so far.
![Zabbix Monitoring Mail Alerts](https://www.tecmint.com/wp-content/uploads/2015/08/Zabbix-Monitoring-Mail-Alerts-620x218.jpg)Zabbix Monitoring Mail Alerts
That’s all! Although this guide was mainly focused on sending Zabbix alerts to a Gmail account using **Gmail SMTP** server as a mailhub, using the same configuration you can, also, push Zabbix email alerts further to other valid internet email accounts by relying on Gmail to route your emails through SMTP servers.
Tags [zabbix](https://www.tecmint.com/tag/zabbix/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Install Zabbix on RHEL/CentOS and Debian/Ubuntu – Part 1](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/)
Next article:
[How to Install and Configure Zabbix Agents on Remote Linux – Part 3](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/)
![Photo of author](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=100&d=blank&r=g)
Matei Cezar
I'am a computer addicted guy, a fan of open source and linux based system software, have about 4 years experience with Linux distributions desktop, servers and bash scripting.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#respond)** or
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
### 52 Comments
[Leave a Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/e7fd98347ad3a060a75481867d6c5e19034bd284f07a2120e7fda28f1ac54279?s=50&d=blank&r=g)
djiman wabi
[ April 2, 2020 at 3:27 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-1324625)
Good Evening…
Please we do not understand how you could make the script file.
```
# vi /usr/local/share/zabbix/alertscripts/zabbix-sendmail [On RHEL / CentOS 7]
$ sudo nano/usr/local/share/zabbix/alertscripts / zabbix-sendmail [On Debian 8]

```
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-1324625)
     * ![](https://secure.gravatar.com/avatar/e21fc25cbd98c2c9e23d9bce01af395b4225605dd05ac9c48d7bf2d408c5df63?s=50&d=blank&r=g)
Jens Pauwels
[ April 28, 2020 at 2:35 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-1330643)
Hello,
I also was not able to find that file on that location. Please check the server conf file at **/etc/zabbix/zabbix_server.conf** and look for ‘**alertscripts** ‘ path.
My default folder was **/usr/lib/zabbix/alertscripts** for some reason.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-1330643)
  2. ![](https://secure.gravatar.com/avatar/4a4bfaf5219c663df569b8ee40fa9e32f701402251e33120b20c5dabbd3126c5?s=50&d=blank&r=g)
Andreas Geesen
[ February 5, 2020 at 9:32 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-1314862)
I stumbled onto this howto and was mildly irritated by the use of **SSMTP** but then for anybody using RedHat it might be harder to install the alternative **Nullmailer**.
In systems of the **Debian** family-like **Raspi** and **Ubuntu** , both are available. **Nullmailer** should be preferred because it is currently still maintained. In Red Hat’s descendants, you are more likely to find SSMTP. It has not been changed since 2014, although there are security concerns afaik.
While SSMTP dumps messages directly to the configured SMTP server and terminates immediately, Nullmailer works like a “real” mail server: The program uses a queue into which it accepts messages and which it processes regularly. Accordingly, a Nullmailer process runs permanently. Sending via Nullmailer is, therefore, more robust. SSMTP is more suitable as an extra in containers.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-1314862)
  3. ![](https://secure.gravatar.com/avatar/bf2150a2387867fbdb6bc56f24ec9867477e9658c312e507cff2b784d4210883?s=50&d=blank&r=g)
Rajesh
[ December 25, 2019 at 2:43 pm  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-1308333)
Hi! The issue is: we are getting trigger alert emails as downloadable files. We need to download a file and then only we can see what is inside that file. We want alert as texts. Can anyone please help us out regarding this.
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-1308333)
  4. ![](https://secure.gravatar.com/avatar/77a3faffea0ad0abaa44bad6e79927f6e790d40e846b680feefb3d8a69b1d0be?s=50&d=blank&r=g)
Kevin Stretch
[ January 31, 2019 at 1:08 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-1098140)
Could not get the old command to work with Office365. Try this one instead (don’t forget to add the command line arguments in the Zabbix dashboard)
`/usr/bin/mail -s "$2" -r "HARDCODE_FROM_ADDRESS" "$1" <<< "$3"`
[Reply](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-1098140)
  5. ![](https://secure.gravatar.com/avatar/38448c10237893de3d60dd9595a5164fd94f421565ae8824aca5391bd17c5885?s=50&d=blank&r=g)
Sai
[ November 30, 2017 at 3:23 am  ](https://www.tecmint.com/configure-zabbix-to-send-email-alerts-to-gmail/#comment-942256)
Hey Hi,
I have followed the procedure up to the allow access for less secure apps in my gmail account following your indications.But I am getting the error like this
