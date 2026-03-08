# /etc/init.d/zabbix_server
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-691655)
           * ![](https://secure.gravatar.com/avatar/db6ae12effea4d8224a71ecb503df65accabbc510073c10e26cff60889a58c66?s=50&d=blank&r=g)
Tangles
[ October 22, 2015 at 8:14 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-691677)
Another problem encountered was booting
```
# apt-get install rcconf
# rcconf

```

  46. ![](https://secure.gravatar.com/avatar/df41f2ce488627645ff84bef85f13ad2f2657c7287b09f431d3f91c091c0fbd4?s=50&d=blank&r=g)
reza
[ July 23, 2015 at 12:27 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-628993)
Hi
Thats Nice !
so thanks, ;)
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-628993)
  47. ![](https://secure.gravatar.com/avatar/43e1e010b8ffe4d954910c5e7ff6249acf161b5ac051de6219aeaececbafa8dd?s=50&d=blank&r=g)
sarfaraz
[ July 15, 2015 at 1:19 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-624645)
Good read ! I am looking forward to the monitoring setup. Specially if you could SNMPchecks and nagios plugins a bit that would be nice. Does zabbix provide an agent for Linux/Windows Host like ICinga2 does ? What level of SNMP granularity is built into Zabbix ?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-624645)
  48. ![](https://secure.gravatar.com/avatar/e3d0f9debece829189a3ba762d5eba362c7df82ae8e0ea859ff6b289137f5c74?s=50&d=blank&r=g)
Eduardo Hernacki
[ July 14, 2015 at 4:49 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-624184)
Why are you using /etc/rc.local to startup the services? Seriously?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-624184)
     * ![](https://secure.gravatar.com/avatar/50136dbf8e50d81191a1ac124290ae16c02399e2abcb49cdbeb04ae0e4b5482f?s=50&d=blank&r=g)
Matei Cezar
[ July 14, 2015 at 8:16 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-624234)
Yes, because the official zabbix sources does’nt provide any systemd services conf files. Also, the old upstart (init.d) scripts are not fully compatible and run a little bit tricky on systemd, so i suggest you use this method for now to be safe!
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-624234)
  49. ![](https://secure.gravatar.com/avatar/956781a7724acc239ed19e1e47285f9957b2733f6d30e3b776a40ca51503695b?s=50&d=blank&r=g)
pinkman
[ July 14, 2015 at 3:22 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-624168)
will you do Zabbix proxy configuration also ??
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-624168)
  50. ![](https://secure.gravatar.com/avatar/af162005ae67ccda12e769df6c2c14eb27fa8dfb218da09c25b6b64e0fc65e5e?s=50&d=blank&r=g)
Udaya Sri Kariyawasam
[ July 14, 2015 at 2:52 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-624153)
Could you please put a post on how to configure sms alerts in zabbix?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-624153)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 14, 2015 at 4:20 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-624176)
@Udaya,
Surely, in our upcoming articles, we will show how to set email and sms alerts to get critical notifications..just stay tuned for the updates..
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-624176)
       * ![](https://secure.gravatar.com/avatar/af162005ae67ccda12e769df6c2c14eb27fa8dfb218da09c25b6b64e0fc65e5e?s=50&d=blank&r=g)
Udaya Sri Kariyawasam
[ July 21, 2015 at 3:51 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-627983)
Can you just give a clue on how to configure SMS alerts? I tried with minicom but it didn’t work for me.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-627983)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#respond)
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
[fuser – Find and Kill Processes by File, Directory, or Port](https://www.tecmint.com/fuser-find-monitor-kill-linux-processes/)
[How to Check How Long a Process Has Been Running in Linux](https://www.tecmint.com/check-running-process-time-in-linux/)
[20 mysqladmin Commands for MYSQL/MariaDB Database Administration](https://www.tecmint.com/mysqladmin-commands-for-database-administration-in-linux/)
[How to Find Out Who is Using a File in Linux](https://www.tecmint.com/find-out-who-is-using-a-file-in-linux/)
[2 Ways to Re-run Last Executed Commands in Linux](https://www.tecmint.com/run-last-executed-commands-in-linux/)
[15 Practical Examples of ‘echo’ command in Linux](https://www.tecmint.com/echo-command-in-linux/)
## Linux Server Monitoring Tools
[Arpwatch – Monitor Ethernet Activity {IP and Mac Address} in Linux](https://www.tecmint.com/monitor-ethernet-activity-in-linux/)
[10 Strace Commands for Troubleshooting and Debugging Linux Processes](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/)
[How to Add Linux Host to Nagios Monitoring Server Using NRPE Plugin](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/)
[Suricata – A Intrusion Detection, Prevention, and Security Tool](https://www.tecmint.com/suricata-intrusion-detection-prevention-linux/)
[How to Monitor Ubuntu Performance Using Netdata](https://www.tecmint.com/monitor-ubuntu-performance-using-netdata/)
[Installing “PHP Server Monitor” Tool using LEMP or LAMP Stack in Arch Linux](https://www.tecmint.com/install-php-server-monitor-in-arch-linux/)
## Learn Linux Tricks & Tips
[How to Find Out List of All Open Ports in Linux](https://www.tecmint.com/find-open-ports-in-linux/)
[How to Delete HUGE (100-200GB) Files in Linux](https://www.tecmint.com/delete-huge-files-in-linux/)
[How to Monitor Progress of (Copy/Backup/Compress) Data using ‘pv’ Command](https://www.tecmint.com/monitor-copy-backup-tar-progress-in-linux-using-pv-command/)
[Show a Custom Message to Users Before Linux Server Shutdown](https://www.tecmint.com/show-linux-server-shutdown-message/)
[Linux Tricks: Play Game in Chrome, Text-to-Speech, Schedule a Job and Watch Commands in Linux](https://www.tecmint.com/text-to-speech-in-terminal-schedule-a-job-and-watch-commands-in-linux/)
[How to Configure Custom SSH Connections to Simplify Remote Access](https://www.tecmint.com/configure-custom-ssh-connection-in-linux/)
## Best Linux Tools
[5 GUI Tools to Free Up Space on Debian, Ubuntu and Linux Mint](https://www.tecmint.com/free-disk-space-ubuntu-linux-mint/)
[4 Best Twitter Clients for Linux in 2024 (Updated)](https://www.tecmint.com/best-linux-twitter-clients/)
[16 Best Microsoft Teams Alternatives For Linux in 2024](https://www.tecmint.com/microsoft-teams-alternatives/)
[9 Best Microsoft Excel Alternatives for Linux](https://www.tecmint.com/microsoft-excel-alternatives-for-linux/)
[16 Best Notepad++ Alternatives for Linux in 2025](https://www.tecmint.com/best-notepad-alternatives-for-linux/)
[11 Best PDF Editors to Edit PDF Documents in Linux](https://www.tecmint.com/pdf-editors-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/ "Scroll back to top")
Search for:
