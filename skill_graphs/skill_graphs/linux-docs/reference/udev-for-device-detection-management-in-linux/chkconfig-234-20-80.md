# chkconfig: 234 20 80
JAVA_HOME=/usr/sunjdk/jdk1.7.0_25
PATH=$PATH:$HOME/bin:$JAVA_HOME/bin
export JAVA_HOME
export PATH
CATALINA_HOME=/tomcat-7.0.27/
case $1 in
start)
sh /tomcat-home/bin/startup.sh
;;
stop)
sh /tomcat-home/bin/shutdown.sh
;;
restart)
sh /tomcat-home/bin/shutdown.sh
sh /tomcat-home/bin/startup.sh
;;
esac
exit 0
please guide me
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-102836)
  24. ![](https://secure.gravatar.com/avatar/17324c8bce9b14e4c5468352d425bf7c728c8a3cf1dd11547e7deca66b354be4?s=50&d=blank&r=g)
Madan
[ December 4, 2013 at 7:58 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-80585)
Hi,
I have issue with my monit configuration. When I include specific file to include in the monitrc file it does not start but if I include the fulle directory like “include /etc/monit.d/*”. It work perfectly.
Pleass advise.
Thanks.
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-80585)
  25. ![](https://secure.gravatar.com/avatar/08d15dd51cf8268c3073b7d87507ccad228e98961675d5967adaabec66b1b2a7?s=50&d=blank&r=g)
Moose
[ July 30, 2013 at 11:23 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-32038)
Hi,
I have an issue to access monit GUI after start the monit service.
In monit.conf i keep the config file as default
set httpd port 2812 and
use address localhost # only accept connection from localhost
allow localhost # allow localhost to connect to the server and
allow admin:monit # require user ‘admin’ with password ‘monit’
allow @monit # allow users of group ‘monit’ to connect (rw)
allow @users readonly # allow users of group ‘users’ to connect readonly
And try to access using server ip i.e: 10.1.30.3:2812 but the page is unable to connect
In /var/log/monit it shows denied connection from non-authorized client
Do u have any idea on above issue?
Ur help is highly appreciated
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-32038)
  26. ![](https://secure.gravatar.com/avatar/1a18ceb9acab08404197e29bb07c100c5a38f4538188776b5db78f142c3faac5?s=50&d=blank&r=g)
Gopi
[ July 16, 2013 at 11:36 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-30769)
Thank You very much..
How to add multiple mysql remote services
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-30769)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 16, 2013 at 1:43 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-30793)
create separate services for MySQL and define each IP address in the code that you wish to monitor.
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-30793)
  27. ![](https://secure.gravatar.com/avatar/1a18ceb9acab08404197e29bb07c100c5a38f4538188776b5db78f142c3faac5?s=50&d=blank&r=g)
Gopi
[ July 15, 2013 at 2:59 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-30596)
How to monitor remote hosts….?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-30596)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 15, 2013 at 3:28 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-30599)
For remote host monitoring, just replace the IP with remote host in each code that you want to monitor the respective service.
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-30599)
       * ![](https://secure.gravatar.com/avatar/1a18ceb9acab08404197e29bb07c100c5a38f4538188776b5db78f142c3faac5?s=50&d=blank&r=g)
Gopi
[ July 16, 2013 at 10:09 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-30747)
Thank you very much….!
how to monitor multiple mysql remote services…..?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-30747)
  28. ![](https://secure.gravatar.com/avatar/467587f4f4217c28e5511da0c1ebb386b0990c00e0c47fd39b912e17dbc75c47?s=50&d=blank&r=g)
Aswin Roy
[ June 6, 2013 at 4:51 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-28777)
Can you give me the code to monitor MySQL on another computer on the same network?
I am using this code:
check host remote with address 192.168.0.187
if failed icmp type echo count 3 with timeout 3 seconds then alert
if failed port 3306 protocol mysql with timeout 15 seconds then alert
But, connection failed. It says “cannot open connection to INET via TCP.” What to do?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-28777)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 6, 2013 at 6:32 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-28781)
The code is already given above, just replace IP there and make sure port 3306 is opened on that remote machine.
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-28781)
  29. ![](https://secure.gravatar.com/avatar/8b2c30debb578d57ca9a09ff042bda0bc8a25d9631764b699a1cd9bcdde6dc3c?s=50&d=blank&r=g)
Kevin
[ April 30, 2013 at 6:58 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-27115)
And of course I see the M/Monit banner just after I hit send :)
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-27115)
  30. ![](https://secure.gravatar.com/avatar/8b2c30debb578d57ca9a09ff042bda0bc8a25d9631764b699a1cd9bcdde6dc3c?s=50&d=blank&r=g)
Kevin
[ April 30, 2013 at 6:56 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-27114)
Pretty cool. Is it possible to monitor a bunch of servers on the front page?
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-27114)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 30, 2013 at 8:20 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-27118)
Yes! you can monitor bunch of server by simply creating each block for each service, like this.
```
check host example.com with address
172.16.25.125
if failed port 80 protocol httpd with timeout 15 seconds
then exec "/usr/bin/ssh root@example.com /etc/init.d/httpd restart"

```
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-27118)
  31. ![](https://secure.gravatar.com/avatar/4b193d87028f4f345491d1db041ad256c064c3450f2b79c1638113b783250a28?s=50&d=blank&r=g)
Alan
[ April 5, 2013 at 12:09 am  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-25037)
Great article, I just implemented this on a few VM’s. Thank you very much!
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-25037)
  32. ![](https://secure.gravatar.com/avatar/6c8c309339430e10fc573b9eb4e872c9cf16299c5d3565f8d6474b4fbc5402e4?s=50&d=blank&r=g)
Babu
[ April 4, 2013 at 1:30 pm  ](https://www.tecmint.com/monit-linux-services-monitoring/#comment-25022)
Greate .
[Reply](https://www.tecmint.com/monit-linux-services-monitoring/#comment-25022)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/monit-linux-services-monitoring/#respond)
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
[Mutt – A Command Line Email Client to Send Mails from Terminal](https://www.tecmint.com/send-mail-from-command-line-using-mutt-command/)
[Terminalizer – Record Your Linux Terminal and Generate Animated GIF](https://www.tecmint.com/terminalizer-record-your-linux-terminal-in-gif/)
[10 Must-Know sFTP Commands for Linux File Transfers](https://www.tecmint.com/sftp-command-examples/)
[How to Delete all Text in a File Using Vi/Vim Editor](https://www.tecmint.com/delete-all-text-in-a-file-using-vi-editor/)
[How to List Files Installed From a RPM or DEB Package in Linux](https://www.tecmint.com/list-files-installed-from-rpm-deb-package-in-linux/)
[Boxes – Draws ASCII Art Boxes and Shapes in Linux Terminal](https://www.tecmint.com/boxes-draws-ascii-art-boxes-in-linux-terminal/)
## Linux Server Monitoring Tools
[How to Do Security Auditing of Linux System Using Lynis Tool](https://www.tecmint.com/linux-security-auditing-and-scanning-with-lynis-tool/)
[How to Monitor Linux Server and Process Metrics from Browser](https://www.tecmint.com/monitor-linux-server-in-realtime/)
[ngxtop – Monitor Nginx Log Files in Real Time in Linux](https://www.tecmint.com/ngxtop-monitor-nginx-log-files-in-real-time-in-linux/)
[Monitor Server Logs in Real-Time with “Log.io” Tool on RHEL/CentOS 7/6](https://www.tecmint.com/linux-server-log-monitoring-with-log-io/)
[IPTraf-ng – A Console-Based Network Monitoring Tool](https://www.tecmint.com/iptraf-ng-linux-network-monitoring/)
[How to Monitor Linux Commands Executed by System Users in Real-time](https://www.tecmint.com/monitor-linux-commands-executed-by-system-users-in-real-time/)
## Learn Linux Tricks & Tips
[Display Command Output or File Contents in Column Format](https://www.tecmint.com/display-command-output-or-file-contents-in-column-format/)
[Lolcat – Display Text in Rainbow Colors in Linux Terminal](https://www.tecmint.com/lolcat-color-output-linux-terminal/)
[10 Useful Linux Command Line Tricks for Newbies – Part 2](https://www.tecmint.com/10-useful-linux-command-line-tricks-for-newbies/)
[How to Use ‘cat’ and ‘tac’ Commands with Examples in Linux](https://www.tecmint.com/learn-linux-cat-command-and-tac-command/)
[Use ‘pushd’ and ‘popd’ for Efficient Filesystem Navigation in Linux](https://www.tecmint.com/pushd-and-popd-linux-filesystem-navigation/)
[How to Append Text to End of File in Linux](https://www.tecmint.com/append-text-to-end-of-file-in-linux/)
## Best Linux Tools
[Universal Package Managers for Linux: Snap, Flatpak, and AppImage](https://www.tecmint.com/cross-distribution-package-managers-for-linux/)
[3 Best Cloud-Based Music Apps for Linux](https://www.tecmint.com/cloud-music-player/)
[How to Install Microsoft Teams, Slack, and Discord on Linux Desktop](https://www.tecmint.com/install-microsoft-teams-slack-discord-linux/)
[16 Open Source Cloud Storage Software for Linux in 2024](https://www.tecmint.com/free-open-source-cloud-storage-tools-for-linux/)
[15 Best Open Source Music Making Software for Linux in 2024](https://www.tecmint.com/free-music-creation-or-audio-editing-softwares-for-linux/)
[Top 4 Google Docs Alternatives for Linux in 2024](https://www.tecmint.com/google-docs-alternatives/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/monit-linux-services-monitoring/ "Scroll back to top")
Search for:
