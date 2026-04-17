# /usr/share/doc/cacti-0.8.8b/cacti.sql
[root@localhost ~]# mysql -u cacti -p cacti < /usr/share/doc/cacti-0.8.8b/ cacti.sql
-bash: /usr/share/doc/cacti-0.8.8b/: No such file or directory
What could be the issue for the above step?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-814636)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ September 9, 2016 at 2:32 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-814638)
@Cvaa,
The error is self explanatory, the file `cacti.sql` doesn’t exist on the specified location, do you see the file under `/usr/share/doc/cacti-0.8.8b/` directory?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-814638)
  52. ![](https://secure.gravatar.com/avatar/04ded867620fe0080b9b4576b4820044d972f6864516f8d806e0ad3555bab149?s=50&d=blank&r=g)
Chris Led
[ August 17, 2016 at 1:44 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-807369)
Ravi,
Can you ping me offline to discuss the issue I am having?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-807369)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 17, 2016 at 11:12 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-807450)
@Chris,
You can contact me at
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-807450)
  53. ![](https://secure.gravatar.com/avatar/04ded867620fe0080b9b4576b4820044d972f6864516f8d806e0ad3555bab149?s=50&d=blank&r=g)
Chris
[ August 17, 2016 at 1:28 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-807363)
Still no luck….Built a new VM server and did the same install, without any security loaded. Any ideas are welcome.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-807363)
  54. ![](https://secure.gravatar.com/avatar/a753a7c9f7800c695fe602e4f8ab7bd31d0dcc7cfe259d6e4e230dcec03399df?s=50&d=blank&r=g)
Chris Led
[ August 12, 2016 at 1:23 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-806382)
I have cacti working as shown in this howto. I appreciate all your effort. It has been a learning experience…
My issues are that the RRD background is shown and the SNMP is capturing stats.
I do not get any actual graph data.
If you can contact me offline or respond soonest. RHEL 7.2 with SELINUX permissive.
I can send pics if you need them. Debugging shows snmp working and the DB talking…..
tried 777 etc before and get the same results…thank in advance.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-806382)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 12, 2016 at 10:54 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-806461)
@Chris,
Thanks for appreciating our efforts in creating such easy article for you guys, regarding your issue, just give a day to pull the data from the server, or else you can manually run the poller.php script to update the graphs on the fly..
```
# php /usr/share/cacti/poller.php

```
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-806461)
  55. ![](https://secure.gravatar.com/avatar/cde5e956ae19290ea2c305307c7eaeca78c41529f1a29037074e8407beb494c5?s=50&d=blank&r=g)
max
[ August 9, 2016 at 12:49 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-805769)
HI
under settings there is a – RRDTool Default Font Path option
what do i need to put in this field?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-805769)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 9, 2016 at 1:11 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-805773)
@Max,
No need to add anything, we are not using any fancy fonts for graphs, just skip this step and continue cacti installation.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-805773)
       * ![](https://secure.gravatar.com/avatar/cde5e956ae19290ea2c305307c7eaeca78c41529f1a29037074e8407beb494c5?s=50&d=blank&r=g)
max
[ August 9, 2016 at 1:58 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-805781)
I’m done the installation. Now i’m facing problem to add device, I added my pc to devices but the status is unknown, no graph is generate and just showing broken image. Any solution?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-805781)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 9, 2016 at 3:00 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-805795)
@Max,
Have you disabled SELinux mode? could you share the screenshot of the graph with us? so that we can help you out..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-805795)
           * ![](https://secure.gravatar.com/avatar/cde5e956ae19290ea2c305307c7eaeca78c41529f1a29037074e8407beb494c5?s=50&d=blank&r=g)
max
[ August 10, 2016 at 6:36 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-805938)
Hi Ravi,
Yes, I already disabled SELinux mode. Please refer link below.
Screenshot:
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 10, 2016 at 11:15 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-805982)
@Max,
Check two things, first check the logs under /var/log/ what error exactly you seeing in the logs and secondly try to run the following command and see what output you getting on the screen, share both results with me..
```
# php /usr/share/cacti/poller.php

```

  56. ![](https://secure.gravatar.com/avatar/85f66510785c9c5028fe9be93287f0eb99245075bb2caa1db9917301a7508b02?s=50&d=blank&r=g)
erramah
[ August 6, 2016 at 10:30 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-805123)
HI Ravi,
I re-install cacti from the scratch but now I have the same problem all guys have in
[NOT FOUND] Cacti Log File Path: The path to your Cacti log file.
/usr/share/cacti/log/cacti.log
[ERROR: FILE NOT FOUND].
so please if there is any solution for this because i searched and i didn’t
find the solution.
thanks Ravi for your support
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-805123)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 8, 2016 at 11:24 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-805520)
@Erramah,
This should resolve your issue.
```
# mkdir /var/log/cacti
# touch /var/log/cacti/cacti.log

```
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-805520)
       * ![](https://secure.gravatar.com/avatar/f64747f0426d19d393679765056b74b43dd0451ea8e1154807645ec0ff753a65?s=50&d=blank&r=g)
Joey
[ August 9, 2016 at 9:52 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-805745)
It’s works!.. awesome.. thanks Ravi.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-805745)
  57. ![](https://secure.gravatar.com/avatar/cde5e956ae19290ea2c305307c7eaeca78c41529f1a29037074e8407beb494c5?s=50&d=blank&r=g)
misterbux
[ August 4, 2016 at 12:56 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-804458)
Dear,
I follow everything from this guidelines but after I entering to browser by using
What should I do? Your advise is much appreciated.
Thank you.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-804458)
     * ![](https://secure.gravatar.com/avatar/cde5e956ae19290ea2c305307c7eaeca78c41529f1a29037074e8407beb494c5?s=50&d=blank&r=g)
misterbux
[ August 4, 2016 at 2:00 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-804471)
Dear Ravi,
Problem was resolved after I reconfigure the include.php. But the problem now, the graph doesn’t appear, it’s showing broken image. Kindly assist. Looking forward for you reply.
Thank you.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-804471)
       * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 4, 2016 at 2:50 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-804480)
@Misterbux,
Try to disable SELinux and see..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-804480)
         * ![](https://secure.gravatar.com/avatar/cde5e956ae19290ea2c305307c7eaeca78c41529f1a29037074e8407beb494c5?s=50&d=blank&r=g)
misterbux
[ August 4, 2016 at 3:27 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-804494)
Dear Ravi,
I will try and revert back to you the outcome.
Thanks.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-804494)
  58. ![](https://secure.gravatar.com/avatar/85f66510785c9c5028fe9be93287f0eb99245075bb2caa1db9917301a7508b02?s=50&d=blank&r=g)
erramah
[ July 31, 2016 at 10:25 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-803487)
Hello Ravi,
Thank you for these useful information I really appreciate you. I really need using cacti in my work. so I followed all the steps correctly. however, when I entered my ip add **The requested URL cacti** was not found on this server.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-803487)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 1, 2016 at 11:22 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-803637)
@Erramah,
It seems your Cacti installation wasn’t successful, try following the instructions carefully again and make sure your SELinux is in disabled mode..If you don’t know how to make SELinux to disable state, try reading our article here: <https://www.tecmint.com/disable-selinux-temporarily-permanently-in-centos-rhel-fedora/>
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-803637)
  59. ![](https://secure.gravatar.com/avatar/10b2b222becaafb7f34675bf1b6589f7bd7aeb46a0ef6b4e3fc2a61fcae0b241?s=50&d=blank&r=g)
Chris
[ July 7, 2016 at 11:09 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-798038)
Re:
[NOT FOUND] Cacti Log File Path: The path to your Cacti log file.
/usr/share/cacti/log/cacti.log
[ERROR: FILE NOT FOUND]
This should resolve your issue.
mkdir /var/log/cacti
touch /var/log/cacti/cacti.log
/usr/share/cacti/log is a symlink to /var/log/cacti which doesn’t exist
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-798038)
  60. ![](https://secure.gravatar.com/avatar/b6f700d8f929986b1674e43f94dc3516912c62142636526742221e5dab495298?s=50&d=blank&r=g)
Samuel
[ July 5, 2016 at 10:31 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-797507)
I got the same error as Saguu
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-797507)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 5, 2016 at 12:33 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-797516)
@Samuel,
May I know on which Linux distribution version you guys trying? so that I can setup locally on my VM to test it myself and will give you proper solution to this problem. I still think its something that Cacti was not installed properly or may be bug in the cacti release..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-797516)
       * ![](https://secure.gravatar.com/avatar/ba6e49555feca119abca541a84314c78412f2a6b596aac7e8303d3a46f661b02?s=50&d=blank&r=g)
Saguu
[ July 5, 2016 at 1:04 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-797523)
@Ravi
For information : CentOS 6.8 and cacti version 0.8.8h from repo el6
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-797523)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 5, 2016 at 2:03 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-797532)
@Saguu,
Thanks for sharing Linux OS information, will give a try right away with solution…stay tuned till then..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-797532)
  61. ![](https://secure.gravatar.com/avatar/ba6e49555feca119abca541a84314c78412f2a6b596aac7e8303d3a46f661b02?s=50&d=blank&r=g)
Saguu
[ July 5, 2016 at 12:28 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-797424)
Hello, I just try again in a moment. But it still does not work. It seems that this is a problem of authorization on file .. What do you think?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-797424)
  62. ![](https://secure.gravatar.com/avatar/ba6e49555feca119abca541a84314c78412f2a6b596aac7e8303d3a46f661b02?s=50&d=blank&r=g)
Saguu
[ July 4, 2016 at 3:20 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-797302)
Nice job ! Perhaps, i have a problem with
In this page, i have this error :
[NOT FOUND] Cacti Log File Path: The path to your Cacti log file.
/usr/share/cacti/log/cacti.log
[ERROR: FILE NOT FOUND]
Have you an idea for this ?
Regards,
Saguu
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-797302)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 4, 2016 at 3:38 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-797307)
@Saguu,
I don’t think your Cacti installation was successful, please try to re-install again and see..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-797307)
       * ![](https://secure.gravatar.com/avatar/ba6e49555feca119abca541a84314c78412f2a6b596aac7e8303d3a46f661b02?s=50&d=blank&r=g)
Saguu
[ July 4, 2016 at 3:43 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-797309)
Nice try but it’s the second installation (clean VM). I followed your tutorial step by step. :(
For information : CentOS 6.8 and cacti version 0.8.8h from repo el6
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-797309)
  63. ![](https://secure.gravatar.com/avatar/2b01ee514d978be9db6a7dce10cad6b569b94ced7a1b285c0b996d0ec98c3c8d?s=50&d=blank&r=g)
Sandalia
[ June 18, 2016 at 5:16 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-792095)
Thank you! Very clear and concise!
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-792095)
  64. ![](https://secure.gravatar.com/avatar/d26ec96fca673635ce9a2b5d74c460abe2a732691bf4e47d1d375527dd04564c?s=50&d=blank&r=g)
Linux Student
[ June 15, 2016 at 5:00 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-791314)
Hello,
Please could someone advise, I am not getting any graphs and it displays broken image.
mysql> show databases;
+——————–+
| Database |
+——————–+
| information_schema |
| cacti |
| mysql |
| test |
+——————–+
I am only using username root on mysql…
vi /etc/cron.d/cacti
*/5 * * * * root /usr/bin/php /usr/share/cacti/poller.php > /dev/null 2>&1
vi /etc/cacti/db.php
$database_type = “mysql”;
$database_default = “cacti”;
$database_hostname = “localhost”;
$database_username = “root”;
$database_password = “xxxxxxxx”;
$database_port = “3306”;
$database_ssl = false;
cd /usr/share/cacti/
ls -ls
8 -rw-r–r– 1 root root 5860 May 9 16:20 about.php
8 -rw-r–r– 1 root root 5348 May 9 16:20 auth_changepassword.php
16 -rw-r–r– 1 root root 14690 May 9 16:20 auth_login.php
12 -rw-r–r– 1 root root 10366 Jun 15 12:26 cacti.log
20 -rw-r–r– 1 root root 20257 May 9 16:20 cdef.php
0 lrwxrwxrwx 1 root root 18 Jun 14 12:24 cli -> /var/lib/cacti/cli
28 -rwxr-xr-x 1 root root 26620 May 9 16:20 cmd.php
8 -rw-r–r– 1 root root 6731 May 9 16:20 color.php
24 -rw-r–r– 1 root root 23082 May 9 16:20 data_input.php
36 -rw-r–r– 1 root root 33807 May 9 16:20 data_queries.php
60 -rw-r–r– 1 root root 57419 May 9 16:20 data_sources.php
32 -rw-r–r– 1 root root 31482 May 9 16:20 data_templates.php
8 -rw-r–r– 1 root root 6108 May 9 16:20 gprint_presets.php
4 -rw-r–r– 1 root root 3657 May 9 16:20 graph_image.php
16 -rw-r–r– 1 root root 13060 May 9 16:20 graph.php
12 -rw-r–r– 1 root root 9438 May 9 16:20 graph_settings.php
20 -rw-r–r– 1 root root 17980 May 9 16:20 graphs_items.php
40 -rw-r–r– 1 root root 39491 May 9 16:20 graphs_new.php
60 -rw-r–r– 1 root root 57810 May 9 16:20 graphs.php
12 -rw-r–r– 1 root root 10229 May 9 16:20 graph_templates_inputs.php
20 -rw-r–r– 1 root root 18710 May 9 16:20 graph_templates_items.php
28 -rw-r–r– 1 root root 25602 May 9 16:20 graph_templates.php
44 -rw-r–r– 1 root root 42189 May 9 16:20 graph_view.php
8 -rw-r–r– 1 root root 6480 May 9 16:20 graph_xport.php
56 -rw-r–r– 1 root root 57011 May 9 16:20 host.php
20 -rw-r–r– 1 root root 18756 May 9 16:20 host_templates.php
4 drwxr-xr-x 2 root root 4096 Jun 14 12:24 images
4 drwxr-xr-x 5 root root 4096 Jun 14 12:24 include
4 -rw-r–r– 1 root root 2323 May 9 16:20 index.php
4 drwxr-xr-x 2 root root 4096 Jun 14 12:24 install
4 drwxr-xr-x 3 root root 4096 Jun 14 12:24 lib
0 lrwxrwxrwx 1 root root 15 Jun 14 12:24 log -> /var/log/cacti/
4 -rw-r–r– 1 root root 2838 May 9 16:20 logout.php
4 drwxr-xr-x 2 root root 4096 Jun 14 12:24 plugins
28 -rw-r–r– 1 root root 24716 May 9 16:20 plugins.php
8 -rw-r–r– 1 root root 4310 May 9 16:20 poller_commands.php
4 -rw-r–r– 1 root root 3374 May 9 16:20 poller_export.php
20 -rwxr-xr-x 1 root root 18596 May 9 16:20 poller.php
4 drwxr-xr-x 5 root root 4096 Jun 14 12:24 resource
0 lrwxrwxrwx 1 root root 18 Jun 14 12:24 rra -> /var/lib/cacti/rra
8 -rw-r–r– 1 root root 7475 May 9 16:20 rra.php
0 lrwxrwxrwx 1 root root 22 Jun 14 12:24 scripts -> /var/lib/cacti/scripts
12 -rw-r–r– 1 root root 10819 May 9 16:20 script_server.php
8 -rw-r–r– 1 root root 6202 May 9 16:20 settings.php
8 -rw-r–r– 1 root root 6227 May 9 16:20 templates_export.php
8 -rw-r–r– 1 root root 5771 May 9 16:20 templates_import.php
20 -rw-r–r– 1 root root 19673 May 9 16:20 tree.php
44 -rw-r–r– 1 root root 42623 May 9 16:20 user_admin.php
60 -rw-r–r– 1 root root 58501 May 9 16:20 utilities.php
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-791314)
     * ![](https://secure.gravatar.com/avatar/d26ec96fca673635ce9a2b5d74c460abe2a732691bf4e47d1d375527dd04564c?s=50&d=blank&r=g)
assad
[ August 17, 2016 at 6:10 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-807539)
Thanks tecmint for responding to my post. The problem was symbolic link to log file
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-807539)
  65. ![](https://secure.gravatar.com/avatar/5c94a1d3b4432bae159b84e32efeea7a9095befc933a0cd4263d999988088063?s=50&d=blank&r=g)
sv-lex
[ June 9, 2016 at 7:56 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-789938)
Hi!
Thanks for manual, just installed on Centos 6.8. When allowing 80 port in firewall better to use insertion (iptables -I), because in my case, rules was added after reject rule, and http service was unavailable
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-789938)
  66. ![](https://secure.gravatar.com/avatar/06911fe94130b23139c7c2b526771baa4f30788cb0a2e25ea0586fbea8539e50?s=50&d=blank&r=g)
Pablo
[ June 6, 2016 at 6:58 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-788980)
Hi, for installing plugins on Cacti, do i need to install anything else, do you have a manual for this version of Cacti 0.8.8g?
Regards,
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-788980)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 7, 2016 at 11:46 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-789364)
@Pablo,
No you don’t need to install anything else, other than Cacti and this article shows instructions for the cacti 0.8.8b version and I am sure there’s nothing much difference in Cacti 0.8.8g.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-789364)
  67. ![](https://secure.gravatar.com/avatar/60d283f7ad9e3e97bb3b4932f5c6cccf766c3becad3423fc47c861cef8af9cb6?s=50&d=blank&r=g)
Volkan
[ May 30, 2016 at 6:59 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785117)
Hi. I make what is missing?

Images do not appear :/
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785117)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 31, 2016 at 11:34 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785290)
@Volkan,
Thanks for sharing the screenshot, I think it’s due to SELinux, could you disable it and check again?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785290)
       * ![](https://secure.gravatar.com/avatar/60d283f7ad9e3e97bb3b4932f5c6cccf766c3becad3423fc47c861cef8af9cb6?s=50&d=blank&r=g)
Volkan
[ May 31, 2016 at 12:23 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785303)
Thank you Ravi. I could not find a solution, and erased everything :D Now I’ll try to install again. (CentOS 6.8 64BIT)
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785303)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 31, 2016 at 12:25 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785306)
@Volkan,
Good luck, and make sure to follow instructions carefully, if you stuck somewhere around while installing Cacti, do comment here, I will love to help you out..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785306)
           * ![](https://secure.gravatar.com/avatar/60d283f7ad9e3e97bb3b4932f5c6cccf766c3becad3423fc47c861cef8af9cb6?s=50&d=blank&r=g)
Volkan
[ May 31, 2016 at 2:14 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785325)
