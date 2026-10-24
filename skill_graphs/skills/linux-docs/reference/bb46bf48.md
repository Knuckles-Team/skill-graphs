# TEMP Files
TMPFILE=/tmp/sarg-reports.$RANDOM
ERRORS=”${TMPFILE}.errors”
TODAY=$(date –date “today” +%d/%m/%Y)
YESTERDAY=$(date –date “1 day ago” +%d/%m/%Y)
WEEKAGO=$(date –date “1 week ago” +%d/%m/%Y)
MONTHAGO=$(date –date “1 month ago” +01/%m/%Y)-$(date –date “1 month ago” +31/%m/%Y)
#This is for sarg daily report
#/usr/local/bin/sarg -f /usr/local/etc/sarg.conf -d $YESTERDAY >$ERRORS 2>&1
/usr/local/bin/sarg -f /usr/local/etc/sarg.conf -d “${YESTERDAY}-${TODAY}” > “${ERRORS}” 2>&1
#This if for sarg weekly report
#/usr/local/bin/sarg -f /usr/local/etc/sarg.conf -d $WEEKAGO >$ERRORS 2>&1
#/usr/local/bin/sarg -f /usr/local/etc/sarg.conf -d “${WEEKAGO}-${TODAY}” > “${ERRORS}” 2>&1
#This if for sarg monthly report
#/usr/local/bin/sarg -f /usr/local/etc/sarg.conf -x -z -d $MONTHAGO >$ERRORS 2>&1
#/usr/local/bin/sarg -f /usr/local/etc/sarg.conf -x -z -d ${MONTHAGO}-${TODAY}” > “${ERRORS}” 2>&1
[/code]
Thx
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-753019)
  29. ![](https://secure.gravatar.com/avatar/b449f9820bfd865070b05433bc972f4b20d40ab8a6ca755434b92a831b007774?s=50&d=blank&r=g)
thusitha
[ November 15, 2015 at 11:43 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-706457)
after editing the sarg.conf file as you mentioned, it gives error after ‘sarg -x’
SARG: Cannot set the locale LC_ALL to the environment variable.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-706457)
     * ![](https://secure.gravatar.com/avatar/b449f9820bfd865070b05433bc972f4b20d40ab8a6ca755434b92a831b007774?s=50&d=blank&r=g)
thusitha
[ November 16, 2015 at 9:14 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-706861)
Hi, I found the solution. I forgot that I was connecting remotely . Different locales on the ssh server and client was causing the problem. So I Edit /etc/ssh/ssh_config in my local machine and comment out SendEnv LANG LC_* line. now it works. Hope this will help someone.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-706861)
       * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 16, 2015 at 10:43 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-706895)
@Thusitha,
Thanks for tip, hope so it will be helpful to others…
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-706895)
  30. ![](https://secure.gravatar.com/avatar/e8330dca0a05eb4e97d689266fae853706af5ee875e87f81f846abfeaffcd957?s=50&d=blank&r=g)
fatboycsaba
[ August 13, 2015 at 11:01 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-642892)
I direct all internet traffic through Squid3 proxy and run sarg reports everyday. Sarg reports is always showing 20% less usage than my ISP which is Telstra Bigpond. What are the additional MBytes that are unaccounted for?
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-642892)
  31. ![](https://secure.gravatar.com/avatar/f17c6e379e3e72a5d74e92c6e43d61f2e7e1748be527377eca0f89481ba2c586?s=50&d=blank&r=g)
Nirghum
[ May 28, 2015 at 2:05 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-583509)
Thanks Ravi. Great post.But I am bit confused about authentication of html page.Can you help me how to add a user with password for sarg output-report page.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-583509)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 28, 2015 at 2:53 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-583520)
@Nirghum,
You mean password protect html page with user credentials?
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-583520)
  32. ![](https://secure.gravatar.com/avatar/ca720e638b88e0da42b64001dd45c5f02c1b545cdc2a813c85256a187fa956cb?s=50&d=blank&r=g)
Deepak
[ May 25, 2015 at 6:10 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-581773)
How to Showing USER Name in SARG reports , IP Showing already
please help
Thanks
Deepak
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-581773)
  33. ![](https://secure.gravatar.com/avatar/89e2e7b6bb4b41817895cf62bd4cc5ae1e2edb3ff137b831f7ff26a9e489c5a6?s=50&d=blank&r=g)
Jason Rendon
[ May 20, 2015 at 12:36 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-576204)
Thank you very much , it helped me a lot .
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-576204)
  34. ![](https://secure.gravatar.com/avatar/c4c3e553d84a4cc066e00872dc295725ba0b7bbae5d64962798e75cab910a163?s=50&d=blank&r=g)
Ali
[ February 27, 2015 at 3:47 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-494492)
Starting httpd: (98)Address already in use: make_sock: could not bind to address
Getting above error while starting httpd service as squid also using same port 80
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-494492)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 27, 2015 at 5:10 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-494551)
@Ali,
You can’t use same port for two different services..please change either..or use any one..
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-494551)
  35. ![](https://secure.gravatar.com/avatar/9192d6144911d7ac413df2227bcc5795303652a93497630a1db7e0eaa1a74957?s=50&d=blank&r=g)
tewelde
[ February 27, 2015 at 12:11 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-494367)
@ravi I am waiting you your response is there any progress beside you
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-494367)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 27, 2015 at 12:26 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-494377)
@Tewelde,
Please give me a day or 2, will update you by Monday….
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-494377)
       * ![](https://secure.gravatar.com/avatar/9192d6144911d7ac413df2227bcc5795303652a93497630a1db7e0eaa1a74957?s=50&d=blank&r=g)
tewelde
[ March 3, 2015 at 1:04 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-497429)
thank you @RAVI for your great effort I will wait you
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-497429)
       * ![](https://secure.gravatar.com/avatar/9192d6144911d7ac413df2227bcc5795303652a93497630a1db7e0eaa1a74957?s=50&d=blank&r=g)
tewelde
[ March 4, 2015 at 12:56 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-498026)
Finally solved from this site

[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-498026)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 4, 2015 at 1:01 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-498027)
@Tewelde,
That’s good to hear, can you tell us what’s the problem and and how you solved, so that it will help other users..
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-498027)
           * ![](https://secure.gravatar.com/avatar/9192d6144911d7ac413df2227bcc5795303652a93497630a1db7e0eaa1a74957?s=50&d=blank&r=g)
tewelde
[ March 5, 2015 at 2:07 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-499023)
I have only correct the full path in the document root then when i try to access by IP address it works but when I try to browse Ip address/sarg it doesn't work
DocumentRoot “/var/www/sarg”
Options FollowSymLinks
AllowOverride All
AuthType Basic
AuthName “Please enter Valid password to access sarg”
AuthUserFile /etc/apache2/passwd
Require valid-user
Options Indexes FollowSymLinks MultiViews
AllowOverride All
Order allow,deny
allow from all
Order allow,deny
allow from all
ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
AllowOverride all
Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
Order allow,deny
Allow from all
it works fine for me but now the only problem is it doesn’t generate report automatically?
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 5, 2015 at 3:49 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-499112)
@Tewelde,
Have you added correct path to your squid access log file in sarg.conf file? are the logs are generating properly? is the path exists? please verify all these…
  36. ![](https://secure.gravatar.com/avatar/9192d6144911d7ac413df2227bcc5795303652a93497630a1db7e0eaa1a74957?s=50&d=blank&r=g)
tewelde
[ February 24, 2015 at 2:38 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-491369)
i have installed sarg-squid analysis under debian based on this instruction but finally i can’t browse with in browser it gives me an error
Not Found
The requested URL /squid-reports was not found on this server.
Apache/2.2.22 (Debian) Server at 10.*.*.* Port 80
and my apache error log is
please help me i realy need it
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-491369)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 24, 2015 at 3:50 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-491388)
@Tewelde,
It’s due to wrong Apache document directory configuration in sarg.conf file, it should be ‘/var/www’ for debian based distros, not /var/www/html..Correct the path in the sarg.conf file and try again…let me know if any errors..
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-491388)
       * ![](https://secure.gravatar.com/avatar/9192d6144911d7ac413df2227bcc5795303652a93497630a1db7e0eaa1a74957?s=50&d=blank&r=g)
tewelde
[ February 25, 2015 at 11:18 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-492226)
Dear Ravi,
i have already try but nothing change still the error is the same
Not Found
The requested URL /sarg was not found on this server.
Apache/2.2.22 (Debian) Server at 10.*.*.* Port 80
i have try to correct document directory in apache even it is not working
and sarg.conf configuration n look like this
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-492226)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 25, 2015 at 11:24 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-492230)
@tewelde,
Can you please tell us on which Debian version you’re trying? I will try myself let’s see how things works..
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-492230)
           * ![](https://secure.gravatar.com/avatar/9192d6144911d7ac413df2227bcc5795303652a93497630a1db7e0eaa1a74957?s=50&d=blank&r=g)
tewelde
[ February 25, 2015 at 12:08 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-492246)
i am using
#lsb_release -a
No LSB modules are available.
Distributor ID: Debian
Description: Debian GNU/Linux 7.1 (wheezy)
Release: 7.1
Codename: wheezy
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 25, 2015 at 12:20 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-492251)
@tewelde,
Thanks for the information, I will test it myself and will update you..give me a day or 2..
  37. ![](https://secure.gravatar.com/avatar/fa9b680793c36901c67cc283bf2c5ca74a3ae8cc01ec8fbc4dc9aaef1a1afc79?s=50&d=blank&r=g)
LeeYY
[ January 21, 2015 at 1:49 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-458613)
Sorry but do I need to enable Apache service in Squid server in order to view the report? I have configured accordingly but I cannot view the report. Please advise.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-458613)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 21, 2015 at 5:44 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-458735)
@LeeYY,
Yes, you must have working Apache service to view reports..
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-458735)
       * ![](https://secure.gravatar.com/avatar/fa9b680793c36901c67cc283bf2c5ca74a3ae8cc01ec8fbc4dc9aaef1a1afc79?s=50&d=blank&r=g)
LeeYY
[ January 22, 2015 at 9:17 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-459434)
Hi,
Tested OK. Thank you very much!
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-459434)
         * ![](https://secure.gravatar.com/avatar/fa9b680793c36901c67cc283bf2c5ca74a3ae8cc01ec8fbc4dc9aaef1a1afc79?s=50&d=blank&r=g)
LeeYY
[ January 23, 2015 at 7:34 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-460231)
Hi Ravi,
I have added “* * 1 * * /usr/local/bin/sarg -x” in crontab -e, but the report is not generated automatically. What will be the possibility?
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-460231)
  38. ![](https://secure.gravatar.com/avatar/4835de3931ce86067118b91c636feeb6bbefdd3e61363b89692a9a5cbb3325e6?s=50&d=blank&r=g)
abdou
[ January 19, 2015 at 7:15 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-457022)
Hello Ravi,
I install SARG and everything work fine , I have the report each hour and I could access through the web page of these reports, however , I have always the (Top sites and Sites & Users and Downloads) even in my sarg.conf I have this line:
report_type topusers topsites sites_users users_sites date_time denied auth_failures site_user_time_date downloads
I tried to access to a denied website and even try to access to my website with wrong credentials.
any ideas ? thanks in advance.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-457022)
  39. ![](https://secure.gravatar.com/avatar/e5b4ceb8abe3a238013fb9f99632be66b51ab190f0ada123a6060c44c32989fa?s=50&d=blank&r=g)
Muunyu syulikwa
[ November 28, 2014 at 2:25 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-385422)
hi i configured sarg following your config am using ubuntu 14.04 and runing zentyal proxy with squid3, when i run the sarg -x command i get the below errors
SARG: Init
SARG: Loading configuration from /etc/sarg/sarg.conf
SARG: Unknown option resolve_ip
SARG: Loading exclude host file from: /etc/sarg/exclude_hosts
SARG: Loading exclude file from: /etc/sarg/exclude_users
SARG: Parameters:
SARG: Hostname or IP address (-a) =
SARG: Useragent log (-b) =
SARG: Exclude file (-c) = /etc/sarg/exclude_hosts
SARG: Date from-until (-d) =
SARG: Email address to send reports (-e) =
SARG: Config file (-f) = /etc/sarg/sarg.conf
SARG: Date format (-g) = Europe (dd/mm/yyyy)
SARG: IP report (-i) = No
SARG: Keep temporary files (-k) = No
SARG: Input log (-l) = /var/log/squid3/access.log
SARG: Resolve IP Address (-n) = No
SARG: Output dir (-o) = /var/lib/sarg/
SARG: Use Ip Address instead of userid (-p) = No
SARG: Accessed site (-s) =
SARG: Time (-t) =
SARG: User (-u) =
SARG: Temporary dir (-w) = /tmp/sarg
SARG: Debug messages (-x) = Yes
SARG: Process messages (-z) = No
SARG: Previous reports to keep (–lastlog) = 0
SARG:
SARG: sarg version: 2.3.6 Arp-21-2013
SARG: Loading User table: /etc/sarg/usertab
SARG: Reading access log file: /var/log/squid3/access.log
SARG: Records read: 4699, written: 4699, excluded: 0
SARG: Squid log format
SARG: Period: 28 Nov 2014
SARG: Sorting log /tmp/sarg/10_100_100_117.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_117
SARG: Sorting log /tmp/sarg/10_100_100_69.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_69
SARG: Sorting log /tmp/sarg/10_100_100_57.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_57
SARG: Sorting log /tmp/sarg/10_100_100_51.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_51
SARG: Sorting log /tmp/sarg/10_100_100_94.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_94
SARG: Sorting log /tmp/sarg/10_100_100_100.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_100
SARG: Sorting log /tmp/sarg/10_100_100_76.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_76
SARG: Sorting log /tmp/sarg/10_100_100_120.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_120
SARG: Sorting log /tmp/sarg/10_100_100_78.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_78
SARG: Sorting log /tmp/sarg/10_100_100_53.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_53
SARG: Sorting log /tmp/sarg/10_100_100_75.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_75
SARG: Sorting log /tmp/sarg/10_100_100_83.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_83
SARG: Sorting log /tmp/sarg/10_100_100_80.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_80
SARG: Sorting log /tmp/sarg/10_100_100_65.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_65
SARG: Sorting log /tmp/sarg/10_100_100_61.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_61
SARG: Sorting log /tmp/sarg/10_100_100_85.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_85
SARG: Sorting log /tmp/sarg/10_100_100_84.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_84
SARG: Sorting log /tmp/sarg/10_100_100_121.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_121
SARG: Sorting log /tmp/sarg/10_100_100_74.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_74
SARG: Sorting log /tmp/sarg/10_100_100_50.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_50
SARG: Sorting log /tmp/sarg/10_100_100_91.user_unsort
SARG: Making file: /tmp/sarg/10_100_100_91
SARG: Sorting file: /tmp/sarg/10_100_100_117.utmp
SARG: Making report: 10.100.100.117
SARG: Sorting file: /tmp/sarg/10_100_100_69.utmp
SARG: Making report: 10.100.100.69
SARG: Sorting file: /tmp/sarg/10_100_100_57.utmp
SARG: Making report: 10.100.100.57
SARG: Sorting file: /tmp/sarg/10_100_100_51.utmp
SARG: Making report: 10.100.100.51
SARG: Sorting file: /tmp/sarg/10_100_100_94.utmp
SARG: Making report: 10.100.100.94
SARG: Sorting file: /tmp/sarg/10_100_100_100.utmp
SARG: Making report: 10.100.100.100
SARG: Sorting file: /tmp/sarg/10_100_100_76.utmp
SARG: Making report: 10.100.100.76
SARG: Sorting file: /tmp/sarg/10_100_100_120.utmp
SARG: Making report: 10.100.100.120
SARG: Sorting file: /tmp/sarg/10_100_100_78.utmp
SARG: Making report: 10.100.100.78
SARG: Sorting file: /tmp/sarg/10_100_100_53.utmp
SARG: Making report: 10.100.100.53
SARG: Sorting file: /tmp/sarg/10_100_100_75.utmp
SARG: Making report: 10.100.100.75
SARG: Sorting file: /tmp/sarg/10_100_100_83.utmp
SARG: Making report: 10.100.100.83
SARG: Sorting file: /tmp/sarg/10_100_100_80.utmp
SARG: Making report: 10.100.100.80
SARG: Sorting file: /tmp/sarg/10_100_100_65.utmp
SARG: Making report: 10.100.100.65
SARG: Sorting file: /tmp/sarg/10_100_100_61.utmp
SARG: Making report: 10.100.100.61
SARG: Sorting file: /tmp/sarg/10_100_100_85.utmp
SARG: Making report: 10.100.100.85
SARG: Sorting file: /tmp/sarg/10_100_100_84.utmp
SARG: Making report: 10.100.100.84
SARG: Sorting file: /tmp/sarg/10_100_100_121.utmp
SARG: Making report: 10.100.100.121
SARG: Sorting file: /tmp/sarg/10_100_100_74.utmp
SARG: Making report: 10.100.100.74
SARG: Sorting file: /tmp/sarg/10_100_100_50.utmp
SARG: Making report: 10.100.100.50
SARG: Sorting file: /tmp/sarg/10_100_100_91.utmp
SARG: Making report: 10.100.100.91
SARG: Making index.html
SARG: The directory “/var/lib/sarg/sarg-general” looks like a report directory but doesn’t contain a sarg-date file. You should delete it
SARG: The directory “/var/lib/sarg/sarg-date” looks like a report directory but doesn’t contain a sarg-date file. You should delete it
SARG: The directory “/var/lib/sarg/sarg-sites” looks like a report directory but doesn’t contain a sarg-date file. You should delete it
SARG: The directory “/var/lib/sarg/sarg-users” looks like a report directory but doesn’t contain a sarg-date file. You should delete it
SARG: Purging temporary file sarg-general
SARG: End
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-385422)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 29, 2014 at 12:12 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-386399)
No idea man..sorry..
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-386399)
  40. ![](https://secure.gravatar.com/avatar/451efbde316724d0e30639384992b1b0aeacbaeefb1dbc391e73f81663598404?s=50&d=blank&r=g)
lambkin
[ November 18, 2014 at 2:03 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-375440)
hi Ravi,
i have a question about sarg set up to access squid log file . my circumstances is sarg and squid on the separate server . how to setup sarg to access remote squid access log ?
thank you in advance.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-375440)
  41. ![](https://secure.gravatar.com/avatar/e163d5b82a792a994f9a6fb998d95f7ec7584a845140549fe2f42aa8ee0a2848?s=50&d=blank&r=g)
prasad
[ November 7, 2014 at 3:45 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-362056)
[root@slave ~]# sarg
bash: sarg: command not found
what to do now ?
i followed as per your suggestions only , every thing is installed successfully.
Please replay
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-362056)
     * ![](https://secure.gravatar.com/avatar/e163d5b82a792a994f9a6fb998d95f7ec7584a845140549fe2f42aa8ee0a2848?s=50&d=blank&r=g)
prasad
[ November 7, 2014 at 3:48 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-362062)
sorry i got it
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-362062)
  42. ![](https://secure.gravatar.com/avatar/21d829b4a698f3e888aa6b0ce7919ad03f9b4525509726d0e78ec18cc3457437?s=50&d=blank&r=g)
sara
[ October 9, 2014 at 3:30 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-327051)
i did not get your point plz give me the solution
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-327051)
  43. ![](https://secure.gravatar.com/avatar/928eba9f47504241ffecd70df13f9031ab83648f8928f7bebc7fc3b0019f77b1?s=50&d=blank&r=g)
Di
[ October 3, 2014 at 6:27 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-320171)
Hello,
Can you tell me in which programming language sarg is written?
Thanks
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-320171)
  44. ![](https://secure.gravatar.com/avatar/21d829b4a698f3e888aa6b0ce7919ad03f9b4525509726d0e78ec18cc3457437?s=50&d=blank&r=g)
sara
[ October 1, 2014 at 2:03 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-318024)
hi ravi,
i have centos 6.4 at x86_64 and got following error while running sarg 2.3.1. Plz help on this
[root@20proxy@pu bin]# sarg -x -z
SARG: Init
SARG: Loading configuration from /etc/sarg/sarg.conf
SARG: TAG: access_log /var/log/squid/access.log
SARG: TAG: output_dir /var/www/html/squid-reports
SARG: TAG: resolve_ip yes
SARG: TAG: date_format e
SARG: TAG: overwrite_report yes
SARG: TAG: mail_utility mail
SARG: TAG: show_successful_message no
SARG: TAG: external_css_file /var/www/sarg/sarg.css
SARG: Parameters:
SARG: Hostname or IP address (-a) =
SARG: Useragent log (-b) =
SARG: Exclude file (-c) =
SARG: Date from-until (-d) =
SARG: Email address to send reports (-e) =
SARG: Config file (-f) = /etc/sarg/sarg.conf
SARG: Date format (-g) = Europe (dd/mm/yyyy)
SARG: IP report (-i) = No
SARG: Input log (-l) = /var/log/squid/access.log
SARG: Resolve IP Address (-n) = Yes
SARG: Output dir (-o) = /var/www/html/squid-reports/
SARG: Use Ip Address instead of userid (-p) = No
SARG: Accessed site (-s) =
SARG: Time (-t) =
SARG: User (-u) =
SARG: Temporary dir (-w) = /tmp/sarg
SARG: Debug messages (-x) = Yes
SARG: Process messages (-z) = Yes
SARG:
SARG: sarg version: 2.3.1 Sep-18-2010
SARG: Reading access log file: /var/log/squid/access.log
SARG: getword loop detected after 255 bytes.41%
SARG: Line=”29/Sep/2014:02:22:39 +0500 10.0.31.114 NONE/400 }▒>�>”�>#ǆ>HƆ>(ǆ>▒]7▒6t▒▒ov&▒1▒O▒$▒%▒h|▒▒▒▒▒hU▒jK▒▒w▒&▒▒▒▒$gР▒݀▒▒B▒▒2▒W▒g▒▒▒▒)▒▒▒u,%▒;▒▒l5▒▒e▒▒8)*▒▒NK▒!▒▒C▒rf▒!▒▒▒ģO▒ծ▒b+▒▒$▒▒▒▒Y▒▒ż▒▒▒▒a▒hI▒]7▒6t▒▒ov&▒1▒O▒▒I▒▒▒▒q@ig▒▒C!D▒{▒āll▒▒▒▒}▒
▒▒▒A▒u▒8▒▒͔▒1▒▒▒\▒N▒▒▒▒▒3▒▒;▒!C+▒▒▒▒▒▒Pt>▒▒▒▒▒p”▒VqBK▒▒N▒ԯ▒a▒▒c▒j▒▒%”jĻ▒~
CVՉm▒�>”�>#ǆ>HƆ>(ǆ>▒]7▒6t▒▒ov&▒1▒O▒$▒%▒h|▒▒▒▒▒hU▒jK▒▒w▒&▒▒▒▒$gР▒݀▒▒B▒▒2▒W▒g▒▒▒▒)▒▒▒u,%▒;▒▒l5▒▒e▒▒8)*▒▒NK▒!▒▒C▒rf▒!▒▒▒ģO▒ծ▒b+▒▒$▒▒▒▒Y▒▒ż▒▒▒▒a▒hI▒]7▒6t▒▒ov&▒1▒O▒▒I▒▒▒▒q@ig▒▒C!D▒{▒āll▒▒▒▒}▒
▒▒▒A▒u▒8▒▒͔▒1▒▒▒\▒N▒▒▒▒▒3▒▒;▒!C+▒▒▒▒▒▒Pt>▒▒▒▒▒p”▒VqBK▒▒N▒ԯ▒a▒▒c▒j▒▒%”jĻ▒~
CVՉm▒<▒▒6NLũ▒
▒2Pr▒▒0▒wGa▒$▒▒▒"▒▒[▒▒z▒▒y▒▒%▒▒{ፏ▒o
▒▒7▒]\▒T$▒Z▒r|▒~*▒▒r▒▒-▒.▒▒▒h▒N▒▒3d▒▒▒ %BC%8B%91%C3;%0E%CD2%C4k%27E%A3%B4!%7E%10D%B8$5%9B%84%96%F3%E6h%FC%1F%D07%DCa%CE%ACl%1Ce%B4%FEf%BD%5Bkd"
SARG: searching for 'x20'
SARG: getword backtrace:
SARG: 1:sarg() [0x4054b7]
SARG: 2:sarg() [0x405ac9]
SARG: 3:sarg() [0x40ab82]
SARG: 4:/lib64/libc.so.6(__libc_start_main+0xfd) [0x7facdd6e4d5d]
SARG: 5:sarg() [0x4029a9]
SARG: Maybe you have a broken amount of data in your /var/log/squid/access.log file
[root@20proxy@pu bin]# PuTTYPuTTYPuTTYPuTTYPuTTYPuTTYPuTTYPuTT
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-318024)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 1, 2014 at 5:50 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-318192)
The error indicating that your squid file has broken data (chunk characters), due to this the file is not processing properly, either remove the chunk data or re-create new log file.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-318192)
       * ![](https://secure.gravatar.com/avatar/21d829b4a698f3e888aa6b0ce7919ad03f9b4525509726d0e78ec18cc3457437?s=50&d=blank&r=g)
sara
[ October 2, 2014 at 11:01 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-318866)
Thanks for your reply, I got your point and found log files are rotating on weekly basis so sarg failed to get all log data from access.log. Now guide me how can i close this rotation and i did not find any logfile_rotation directive in squid.conf and as you said above i made a new access.log file and sarg got success to read the log file but did not write. Plz guide me with commands if needed
squidGuard-1.4-9.el6.x86_64
squid-3.1.23-1.el6.x86_64
Result
[root@20proxy@pu bin]# sarg -x -z
SARG: Init
SARG: Loading configuration from /etc/sarg/sarg.conf
SARG: TAG: access_log /var/log/squid/access.log
SARG: TAG: output_dir /var/www/html/squid-reports
SARG: TAG: resolve_ip yes
SARG: TAG: date_format e
SARG: TAG: overwrite_report yes
SARG: TAG: mail_utility mail
SARG: TAG: show_successful_message no
SARG: TAG: external_css_file /var/www/sarg/sarg.css
SARG: Parameters:
SARG: Hostname or IP address (-a) =
SARG: Useragent log (-b) =
SARG: Exclude file (-c) =
SARG: Date from-until (-d) =
SARG: Email address to send reports (-e) =
SARG: Config file (-f) = /etc/sarg/sarg.conf
SARG: Date format (-g) = Europe (dd/mm/yyyy)
SARG: IP report (-i) = No
SARG: Input log (-l) = /var/log/squid/access.log
SARG: Resolve IP Address (-n) = Yes
SARG: Output dir (-o) = /var/www/html/squid-reports/
SARG: Use Ip Address instead of userid (-p) = No
SARG: Accessed site (-s) =
SARG: Time (-t) =
SARG: User (-u) =
SARG: Temporary dir (-w) = /tmp/sarg
SARG: Debug messages (-x) = Yes
SARG: Process messages (-z) = Yes
SARG:
SARG: sarg version: 2.3.1 Sep-18-2010
SARG: Reading access log file: /var/log/squid/access.log
SARG: Records in file: 31515, reading: 100.00%
SARG: Records read: 31536, written: 0, excluded: 87
SARG: Squid log format
SARG: No records found
SARG: End
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-318866)
         * ![](https://secure.gravatar.com/avatar/b82e3bae9e96045a7e2aa9e4d7005bacbace19f76746e420859e6484a61dcf27?s=50&d=blank&r=g)
chanthy
[ November 3, 2016 at 9:37 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-834339)
how to resolve this sir? please help guid .
root@debian:~# sarg -x -z
SARG: Init
SARG: Loading configuration from /etc/sarg/sarg.conf
SARG: TAG: access_log /var/log/squid3/access.log
SARG: TAG: title “Squid User Access Reports”
SARG: TAG: font_face Tahoma,Verdana,Arial
SARG: TAG: header_color darkblue
SARG: TAG: header_bgcolor blanchedalmond
SARG: TAG: font_size 9px
SARG: TAG: background_color white
SARG: TAG: text_color #000000
SARG: TAG: text_bgcolor lavender
…..
SARG: sarg version: 2.3.6 Arp-21-2013
SARG: Loading User table: /etc/sarg/usertab
SARG: Reading access log file: /var/log/squid3/access.log
SARG: Records read: 85, written: 85, excluded: 0
SARG: Squid log format
SARG: (info) date=02/11/2016
SARG: (info) period=02 Nov 2016
SARG: Period: 02 Nov 2016
SARG: (info) outdirname=/var/lib/sarg/02Nov2016-02Nov2016
SARG: Sorting log /tmp/sarg/192_168_0_200.user_unsort
SARG: Making file: /tmp/sarg/192_168_0_200
SARG: (info) Dansguardian report not produced because no dansguardian configuration file was provided
SARG: (info) No redirector logs provided to produce that kind of report
SARG: (info) No downloaded files to report
SARG: (info) Authentication failures report not produced because it is empty
SARG: (info) Redirector report not generated because it is empty
SARG: Sorting file: /tmp/sarg/192_168_0_200.utmp
SARG: Making report: 192.168.0.200
SARG: Making index.html
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-834339)
  45. ![](https://secure.gravatar.com/avatar/954aa928fae4fddb0260801099215baf34a1c28b124b9c1f36fb483b458354f3?s=50&d=blank&r=g)
Santosh
[ September 18, 2014 at 12:31 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-276931)
Hello,
Can any one provide me the details how to rotate squid log on daily basis? right now it is rotating on weekly basis.
Regards
Santosh
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-276931)
  46. ![](https://secure.gravatar.com/avatar/bb5b3d5f0d1f21b1b0adee315125b6dfdcf64559ecef2ef6cdba0de5e4718cb0?s=50&d=blank&r=g)
Rizky
[ July 14, 2014 at 8:14 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-214168)
hi Ravi, i already install sarg on my cache server, all process complete well, but i cannot access
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-214168)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 14, 2014 at 5:20 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-214433)
Is your Port 80 is opened on the iptable firewall? have you tested the link from the local machine using
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-214433)
  47. ![](https://secure.gravatar.com/avatar/539ec4c09ac6bb626852151f472b71d661d2e60b413e59234a54b3ffbb9e0f1a?s=50&d=blank&r=g)
lloyd
[ July 2, 2014 at 5:16 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-205591)
File not found /var/log/squid/access.log
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-205591)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 3, 2014 at 1:23 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-206263)
May be path to squid log file different in your Linux distribution. Please check and add the correct squid log paths in configuration.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-206263)
  48. ![](https://secure.gravatar.com/avatar/21a105eaf295612f6035af396cbc7a78476464de28c83ce79800e23de0430bb2?s=50&d=blank&r=g)
Faisal
[ June 20, 2014 at 12:50 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-196598)
HI,
I have successful install and configure sarg report my question is how can i restricted sarg url example
Regards
Faisal Khan
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-196598)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 20, 2014 at 3:47 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-196692)
You can use Apache .htaccess to password protect that directory. Please use our search form to search for apache password protect article.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-196692)
  49. ![](https://secure.gravatar.com/avatar/f4da8e2b4b60a24eab7f07961871c2d7f804780db05395e801b356f244110823?s=50&d=blank&r=g)
Eben
[ May 22, 2014 at 6:18 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-168269)
Did the installation then run the reporting, I can log on to the site and I see the logs with the dates, but when I click on them I get a error.
The site could be temporarily unavailable or too busy. Try again in a few moments.
If you are unable to load any pages, check your computer’s network connection.
If your computer or network is protected by a firewall or proxy, make sure that Firefox is permitted to access the Web.
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-168269)
  50. ![](https://secure.gravatar.com/avatar/f4da8e2b4b60a24eab7f07961871c2d7f804780db05395e801b356f244110823?s=50&d=blank&r=g)
Eben
[ May 22, 2014 at 6:11 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-168263)
The installation wend well no problems, but when I go the the reports I can see them on the web page, but
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-168263)
  51. ![](https://secure.gravatar.com/avatar/624b00ae55022434d247a12269a5b4121f25f3ed9666cb4ad04787638155d11b?s=50&d=blank&r=g)
mir
[ April 26, 2014 at 4:34 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-153687)
Actually above error resolved by this
Thanks
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-153687)
  52. ![](https://secure.gravatar.com/avatar/624b00ae55022434d247a12269a5b4121f25f3ed9666cb4ad04787638155d11b?s=50&d=blank&r=g)
mir
[ April 26, 2014 at 3:40 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-153673)
Please help me to resolve following error.
I hv already installed all dependencies above mentioned.
ver 2.3.8
gcc -std=gnu99 -c -I. -DBINDIR=\”/usr/local/bin\” -DSYSCONFDIR=\”/usr/local/etc\” -DFONTDIR=\”/usr/local/share/sarg/fonts\” -DIMAGEDIR=\”/usr/local/share/sarg/images\” -DSARGPHPDIR=\”/var/www/html\” -DLOCALEDIR=\”/usr/local/share/locale\” -DPACKAGE_NAME=\”sarg\” -DPACKAGE_TARNAME=\”sarg\” -DPACKAGE_VERSION=\”2.3.8\” -DPACKAGE_STRING=\”sarg\ 2.3.8\” -DPACKAGE_BUGREPORT=\”\” -DPACKAGE_URL=\”\” -DHAVE_DIRENT_H=1 -DSTDC_HEADERS=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_MEMORY_H=1 -DHAVE_STRINGS_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_STDINT_H=1 -DHAVE_UNISTD_H=1 -DHAVE_STDIO_H=1 -DHAVE_STDLIB_H=1 -DHAVE_STRING_H=1 -DHAVE_STRINGS_H=1 -DHAVE_SYS_TIME_H=1 -DHAVE_TIME_H=1 -DHAVE_UNISTD_H=1 -DHAVE_DIRENT_H=1 -DHAVE_SYS_TYPES_H=1 -DHAVE_SYS_SOCKET_H=1 -DHAVE_NETDB_H=1 -DHAVE_ARPA_INET_H=1 -DHAVE_NETINET_IN_H=1 -DHAVE_SYS_STAT_H=1 -DHAVE_CTYPE_H=1 -DHAVE_ERRNO_H=1 -DHAVE_SYS_RESOURCE_H=1 -DHAVE_SYS_WAIT_H=1 -DHAVE_STDARG_H=1 -DHAVE_INTTYPES_H=1 -DHAVE_LIMITS_H=1 -DHAVE_LOCALE_H=1 -DHAVE_EXECINFO_H=1 -DHAVE_MATH_H=1 -DHAVE_LIBINTL_H=1 -DHAVE_LIBGEN_H=1 -DHAVE_STDBOOL_H=1 -DHAVE_GETOPT_H=1 -DHAVE_FCNTL_H=1 -DHAVE_GD_H=1 -DHAVE_GDFONTL_H=1 -DHAVE_GDFONTT_H=1 -DHAVE_GDFONTS_H=1 -DHAVE_GDFONTMB_H=1 -DHAVE_GDFONTG_H=1 -DHAVE_LDAP_H=1 -DHAVE_ICONV=1 -DICONV_CONST= -DHAVE_ICONV_H=1 -DHAVE_PCRE_H=1 -DENABLE_NLS=1 -DHAVE_GETTEXT=1 -DHAVE_DCGETTEXT=1 -DHAVE_FOPEN64=1 -D_LARGEFILE64_SOURCE=1 -DHAVE_BZERO=1 -DHAVE_BACKTRACE=1 -DHAVE_SYMLINK=1 -DHAVE_LSTAT=1 -DHAVE_GETNAMEINFO=1 -DHAVE_GETADDRINFO=1 -DHAVE_MKSTEMP=1 -DSIZEOF_RLIM_T=8 -DRLIM_STRING=\”%lli\” -g -O2 -Wall -Wno-sign-compare -Wextra -Wno-unused-parameter -Werror=implicit-function-declaration -Werror=format log.c
log.c: In function ‘main’:
log.c:1506: error: format ‘%li’ expects type ‘long int’, but argument 7 has type ‘long long int’
log.c:1513: error: format ‘%li’ expects type ‘long int’, but argument 8 has type ‘long long int’
log.c:1564: error: format ‘%li’ expects type ‘long int’, but argument 2 has type ‘long long int’
make: *** [log.o] Error 1
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-153673)
  53. ![](https://secure.gravatar.com/avatar/97cbd2e77479096a5589d34197c33def015fb83771c612934ad91150b358fa48?s=50&d=blank&r=g)
KC Sim
[ April 24, 2014 at 11:34 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-152621)
Can i generate the traffic report by certain IP and within certain period of time for e.g. 1/Apr/2014 to 5/Apr/2015?
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-152621)
  54. ![](https://secure.gravatar.com/avatar/a59260fda83e4106e89a878fd08a56b3e6c7186ac0b9a8e94f8262e4604693c2?s=50&d=blank&r=g)
chandoo
[ March 18, 2014 at 2:46 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-138130)
Hi
Everything went well, But i can’t view the reports through my browser. Whenever i type
The requested URL /squid-reports was not found on this server.
Apache/2.2.17 (Fedora) Server at 192.168.50.4 Port 80 please help!!
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-138130)
  55. ![](https://secure.gravatar.com/avatar/a735f3d0e3e4999beb342d80d2e2e6b5b7a3455c79c647dc76e17f7629dbb740?s=50&d=blank&r=g)
R.bibin
[ March 18, 2014 at 1:11 am  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-137880)
hi ravi,
i got a good result upto sample output,but i have not been get a access report in web browser.pls help me
[Reply](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-137880)
  56. ![](https://secure.gravatar.com/avatar/37412819cfa9ea7f74071cf799e4a66c95d656aed29d0f3f99f3d8e5bea0dd5b?s=50&d=blank&r=g)
Turko
[ March 11, 2014 at 10:11 pm  ](https://www.tecmint.com/sarg-squid-analysis-report-generator-and-internet-bandwidth-monitoring-tool/#comment-134367)
Hello friend ..
excellent tutorial
you can help me with this?
to give the command. / configure
gives me the following error:
configure: pcre.h was not found so the regexp won’t be available in the hostalias
and then to make the
