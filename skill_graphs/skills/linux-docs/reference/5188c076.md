# lvdisplay /dev/vg_oluyomi/lv_oluyomi
Hope you problem solved, let me know if there still you face the issue.
{ user do fuser } This means you currently using the file system. if you use lazy umount you can umount it even the filesystem under use. Just use -l option with umount.
example: # umount -l /mnt/oluyomi
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-347222)
         * ![](https://secure.gravatar.com/avatar/b3c48a9a8a1a063b56ea9db4062de7d8fd260e657cc8c7fdcbf2b751e48a1547?s=50&d=blank&r=g)
venky
[ December 12, 2014 at 1:52 pm  ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-408480)
you are not specify the reducing symbol
ex:- extend means add + symbol
lvextend -L +150M /dev/mapper/vg_new
reduce means add – symbol
umount /home
e2fsck /dev/mapper/vg_nw
resize2fs /dev/mapper/vg_new 150M
lvcreduce -L -150M /dev/mapper/vg_new
[Reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#comment-408480)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/#respond)
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
[2 Ways to Create an ISO from a Bootable USB in Linux](https://www.tecmint.com/create-an-iso-from-a-bootable-usb-in-linux/)
[5 Command Line Tools to Find Files Quickly in Linux](https://www.tecmint.com/find-files-quickly-in-linux-terminal/)
[How to Check a Particular Package is Installed on Linux](https://www.tecmint.com/check-package-installed-linux/)
[An Easy Way to Hide Files and Directories in Linux](https://www.tecmint.com/hide-files-and-directories-in-linux/)
[5 Advanced Archive Tools for Linux Command Line – Part 2](https://www.tecmint.com/linux-archive-tools/)
[Ways to Use ‘find’ Command to Search Directories More Efficiently](https://www.tecmint.com/find-directory-in-linux/)
## Linux Server Monitoring Tools
[How to Setup Central Logging Server with Rsyslog in Linux](https://www.tecmint.com/install-rsyslog-centralized-logging-in-centos-ubuntu/)
[10 Tips On How to Use Wireshark to Analyze Packets in Your Network](https://www.tecmint.com/wireshark-network-traffic-analyzer-for-linux/)
[All You Need To Know About Processes in Linux [Comprehensive Guide]](https://www.tecmint.com/linux-process-management/)
[systemd-analyze – Find System Boot-up Performance Statistics in Linux](https://www.tecmint.com/systemd-analyze-monitor-linux-bootup-performance/)
[How to Create a Centralized Log Server with Rsyslog in CentOS/RHEL 7](https://www.tecmint.com/create-centralized-log-server-with-rsyslog-in-centos-7/)
[ngxtop – Monitor Nginx Log Files in Real Time in Linux](https://www.tecmint.com/ngxtop-monitor-nginx-log-files-in-real-time-in-linux/)
## Learn Linux Tricks & Tips
[How to Use ‘at’ Command to Schedule a Task on Given or Later Time in Linux](https://www.tecmint.com/linux-cron-alternative-at-command-to-schedule-tasks/)
[How to Copy a File to Multiple Directories in Linux](https://www.tecmint.com/copy-file-to-multiple-directories-in-linux/)
[How to Set Limits on User Running Processes in Linux](https://www.tecmint.com/set-limits-on-user-processes-using-ulimit-in-linux/)
[How to Create Hard and Symbolic Links in Linux](https://www.tecmint.com/create-hard-and-symbolic-links-in-linux/)
[How to Change Default Apache ‘DocumentRoot’ Directory in Linux](https://www.tecmint.com/change-root-directory-of-apache-web-server/)
[Find Top Running Processes by Highest Memory and CPU Usage in Linux](https://www.tecmint.com/find-linux-processes-memory-ram-cpu-usage/)
## Best Linux Tools
[8 Best SSH Clients for Linux in 2024](https://www.tecmint.com/ssh-clients-linux/)
[15 Best Free and Open Source Software (FOSS) Programs for Linux](https://www.tecmint.com/best-free-open-source-tools-for-linux/)
[10 Tools to Take or Capture Desktop Screenshots in Linux](https://www.tecmint.com/take-or-capture-desktop-screenshots-in-ubuntu-linux/)
[Top 6 Telegram Bots to Boost Your Productivity in 2025](https://www.tecmint.com/best-telegram-bots/)
[8 Best Command-Line/Terminal Email Clients for Linux](https://www.tecmint.com/best-commandline-email-clients-for-linux/)
[7 Best Email Clients for Linux Systems](https://www.tecmint.com/best-email-clients-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/extend-and-reduce-lvms-in-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
