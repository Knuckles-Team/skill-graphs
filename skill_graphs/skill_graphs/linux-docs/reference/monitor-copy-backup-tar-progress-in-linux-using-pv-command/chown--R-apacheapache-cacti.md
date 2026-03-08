# chown -R apache:apache cacti
and the issue got resolved ..but he entered this command in a directory names as “html” . may be he created it or whatever ..i cant find this directory
please help
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-887536)
  34. ![](https://secure.gravatar.com/avatar/df43e5fc515b366378e195d0290e1f94bbb5800ff718637c289b33aa32b5d08f?s=50&d=blank&r=g)
D Singh
[ April 24, 2017 at 12:58 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-885601)
my cron job never runs. If I run it mannually I get following error:
```
[root@7cacti share]# cacti php -q /usr/share/cacti/poller.php
bash: cacti: command not found
[root@7cacti share]#

```
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-885601)
  35. ![](https://secure.gravatar.com/avatar/5c75b559e3304c5ed2c2d7c3ad28f71d2414f2fad9ee84a97c8c984ecf73d15c?s=50&d=blank&r=g)
Jack
[ April 20, 2017 at 1:51 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-884716)
Thanx Ravi! Everything is working great so far with one hiccup. All the devices report ‘Up’. I add the create graphs for the device but when I view the graphs they are all blank. However, if I click on the graph in real-time the graph is populated. I am not sure what to do at this point any ideas?
Thanks
jack
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-884716)
  36. ![](https://secure.gravatar.com/avatar/5c75b559e3304c5ed2c2d7c3ad28f71d2414f2fad9ee84a97c8c984ecf73d15c?s=50&d=blank&r=g)
Jack
[ April 18, 2017 at 2:03 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-884361)
Will these instructions work on Fedora 25 server?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-884361)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 18, 2017 at 1:02 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-884443)
@Jack,
Yes, you can easily install Cacti on Fedora 25 by following these instructions..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-884443)
  37. ![](https://secure.gravatar.com/avatar/af85f593e58f64c9070aecd317e2f456bde2cd78316ed537cac7397a1f032c96?s=50&d=blank&r=g)
Deepak
[ February 13, 2017 at 3:40 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-867040)
Hello,
I having this error “**FATAL: Cannot connect to MySQL server on ‘localhost** ‘. Please make sure you have specified a valid MySQL database name in ‘**include/config.php** ‘ ” When I tried to connect the webserver. I am installing in a hyper-V enviorment with host also in same subnet . Do I need to change anything from the above? the “localhost ” would remain the same right ?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-867040)
     * ![](https://secure.gravatar.com/avatar/af85f593e58f64c9070aecd317e2f456bde2cd78316ed537cac7397a1f032c96?s=50&d=blank&r=g)
Deepak
[ February 14, 2017 at 6:59 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-867332)
this one settled now as I had to change the password on database !
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-867332)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 14, 2017 at 11:09 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-867380)
@Deepak,
Please include the correct host and database settings in **include/config.php** file and make sure your MySQL is running..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-867380)
  38. ![](https://secure.gravatar.com/avatar/877061554f153ec21bc566a495c4324141cdee305e27d975f77c88c1fab33173?s=50&d=blank&r=g)
Jason
[ January 11, 2017 at 12:56 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-858572)
Ravi,
Maybe it’s just me but to get back to the last comments in this thread on your webpage I’ve had to hit the newer comments button literally about 15 times. You really need a button that takes everyone to the end.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-858572)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 11, 2017 at 11:16 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-858681)
@Jason,
Actually its difficult to show all comments in one page, it will make the page bigger in size and leads to slow loading, that’s the reason we have to break the comments into pages for easier navigation..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-858681)
  39. ![](https://secure.gravatar.com/avatar/877061554f153ec21bc566a495c4324141cdee305e27d975f77c88c1fab33173?s=50&d=blank&r=g)
Jason
[ January 10, 2017 at 3:51 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-858471)
Nick,
In the instructions
GRANT ALL ON cacti.* TO cacti@localhost IDENTIFIED BY ‘tecmint’;
So you might want to try the password “tecmint” versus “YES”
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-858471)
  40. ![](https://secure.gravatar.com/avatar/877061554f153ec21bc566a495c4324141cdee305e27d975f77c88c1fab33173?s=50&d=blank&r=g)
Jason Hollis
[ January 9, 2017 at 4:58 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-858209)
I have run all the steps successfully as best I can validate. I’m running the latest Fedora with Apache 2.4 and I can’t get to
Any hints?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-858209)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 10, 2017 at 10:54 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-858432)
@Jason,
I think Cacti installation was not successful, try to follow the instructions again carefully and see, if you still gets same error try to view the logs files of cacti and see what error it showing there?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-858432)
  41. ![](https://secure.gravatar.com/avatar/1d87c468ca9b1838848cf0d8b0b4412b302d23c2188899f3b96ea378f72c373f?s=50&d=blank&r=g)
Nick
[ December 14, 2016 at 7:48 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-847572)
I seemed to have missed something. When I type: [root@tecmint ~]# mysql -u cacti -p cacti < /usr/share/doc/cacti-0.8.8b/cacti.sql
(This is the correct location of the cacti.sql db on my machine)
Where is that password coming from? Am I creating a user called cacti on the local machine? I tried editing the db.php so that the $database_username was 'cacti' and the password was [password] but I get access denied when I use that password. I also tried creating a user on the local host named 'cacti' and giving it a password but I get the same error.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-847572)
     * ![](https://secure.gravatar.com/avatar/1d87c468ca9b1838848cf0d8b0b4412b302d23c2188899f3b96ea378f72c373f?s=50&d=blank&r=g)
Nick
[ December 14, 2016 at 7:56 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-847580)
Just to be clear, the error I get after attempting to use any passwords I’ve set is:
ERROR 1045 (28000): Access denied for user ‘cacti’@’localhost’ (using password: YES)
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-847580)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ December 15, 2016 at 1:06 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-847875)
@Nick,
Have you followed **Set MySQL Password** and **Create MySQL Cacti Database** sections in the article carefully? if not try to follow these steps and set root password (if not set) and create cacti user as shown…then you can able to import cacti database to cacti db..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-847875)
  42. ![](https://secure.gravatar.com/avatar/653863fe509f3e2e081613d543b4acd85420fa131f7da657d7b55310cfaf2e27?s=50&d=blank&r=g)
Leng
[ November 26, 2016 at 1:36 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-841563)
Dear Support,
I have a problem on show **cacti.log** on cacti. It say “**Error /usr/share/cacti/log/cacti.log is not readable** “. I try to give full permission to user apache and cacti but it still got same error.
[root@localhost log]# ll /usr/share/cacti/log/cacti.log
-rwxrwxrwx. 1 apache cacti 1606 Nov 26 03:00 /usr/share/cacti/log/cacti.log
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-841563)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 26, 2016 at 12:34 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-841719)
@Leng,
I think you should assign permission apache user like:
```
chown -R apache:apache cacti.log

```
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-841719)
  43. ![](https://secure.gravatar.com/avatar/46d06959ac08a33a9030f1c4b0776816528189f35cf5ca17de25d2ce82c86ba2?s=50&d=blank&r=g)
karim
[ November 10, 2016 at 3:36 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-836997)
Hi, Ravi
I followed step by step for centos7 and when i go to
I have this message : You don’t have permission to access /cacti/ on this server.
Why ? how can i resolve it ?
thank you
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-836997)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 14, 2016 at 3:19 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-837901)
@Karim,
Make sure you’ve disabled SELinux mode, if not disable it and try again..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-837901)
  44. ![](https://secure.gravatar.com/avatar/46d06959ac08a33a9030f1c4b0776816528189f35cf5ca17de25d2ce82c86ba2?s=50&d=blank&r=g)
karim
[ November 7, 2016 at 4:52 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-836042)
Hi, i am from Paris and i followed your tutorial, i have this error at this step ;
mysql -u cacti -p cacti < /usr/share/doc/cacti-0.8.8b/cacti.sql
Enter password: (what is the password ???)
ERROR 1045 (28000): Access denied for user 'cacti'@'localhost' (using password: YES)
Could you help me ? I use CentOS 7.2
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-836042)
     * ![](https://secure.gravatar.com/avatar/1d87c468ca9b1838848cf0d8b0b4412b302d23c2188899f3b96ea378f72c373f?s=50&d=blank&r=g)
Paul
[ December 15, 2016 at 1:24 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-847697)
I have the same error. I think it has something to do with the way the guide sets the username compared to the default username but I can’t figure it out.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-847697)
  45. ![](https://secure.gravatar.com/avatar/77ee828bee50be35abc2ae7bf9b8a5564df963b85c0d171325edd5cedf0dd9cc?s=50&d=blank&r=g)
shantanu
[ November 7, 2016 at 3:21 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-836018)
Hi,
I have configured cacti. It was asking for the login details as well but at the password change page it is showing below error:
“The requested URL /auth_changepassword.php was not found on this server.”
Please suggest.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-836018)
  46. ![](https://secure.gravatar.com/avatar/312614e63a7d0eda4b00644967fbcfac5e90737095540b11817a2af93858f327?s=50&d=blank&r=g)
Aun Ali
[ October 24, 2016 at 9:38 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-831410)
Dear Ravi,
Thanks for your support , one more thing ..it seems to be a time mismatch in cacti time range..i have edited RTC to local timezone but still my graphs are not showing on current timings instead they are shown with a differnce of 5 hours. My timezone is Asia/Karachi
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-831410)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 25, 2016 at 12:47 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-831563)
@Aun,
I think you should sync your sever time with NTP, here is the guide on how to do it: <https://www.tecmint.com/install-ntp-server-in-centos/>
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-831563)
  47. ![](https://secure.gravatar.com/avatar/312614e63a7d0eda4b00644967fbcfac5e90737095540b11817a2af93858f327?s=50&d=blank&r=g)
Aun Ali
[ October 22, 2016 at 3:51 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-830862)
Dear Ravi,
Hope you are fine. I have installed cacti as per your guide and I have then added Localhost in devices and template of load average, I am getting NAN value in graphs, should i wait for 24 hours to get it to poll ??
I have disabled SElinux and run this command as you told (php /usr/share/cacti/poller.php), I hope for your usual support..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-830862)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 24, 2016 at 11:01 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-831289)
@Aun,
Yes, I am find, hope you too as well, yes you should wait at least 24 hours after running poller.php script to gather data and generate report using graphs..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-831289)
  48. ![](https://secure.gravatar.com/avatar/312614e63a7d0eda4b00644967fbcfac5e90737095540b11817a2af93858f327?s=50&d=blank&r=g)
Aun Ali
[ October 19, 2016 at 4:56 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-829904)
Hi Ravi,
I get Http Error 500 when i go
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-829904)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 19, 2016 at 5:20 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-829911)
@Aun,
It seems your Cacti installation was not successful, I suggest you to follow instructions carefully and step-by-step to avoid any issues..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-829911)
  49. ![](https://secure.gravatar.com/avatar/4ca8cf91c42eece1ac37500bc188ec1b4b6d9de841909ef2452ade4d5d6f5b47?s=50&d=blank&r=g)
pranil more
[ September 27, 2016 at 7:01 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-821346)
Please provide configure guide in network monitor tool for cacti.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-821346)
  50. ![](https://secure.gravatar.com/avatar/3736ab8cbf2065534acf3adb6ac197708fe6b24bae42bc5986234cd164281a33?s=50&d=blank&r=g)
Ali Cuesta
[ September 20, 2016 at 4:55 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-819533)
Assalamu ‘alaikum wa rahmatullahi wa barakatuh​.
Dear Ravi,
I really appreciated your effort doing this. I have only one problem encountered which is [ERROR: FILE NOT FOUND] /usr/share/cacti/log/cacti.log.
Would you please advise if I have to create manually the cacti.log file. Thank you very much in advance.
Kind regards,
Ali
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-819533)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ September 20, 2016 at 5:37 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-819538)
@Ali,
Yes, you can create manually that Cacti log file as shown:
```
# mkdir /var/log/cacti
# touch /var/log/cacti/cacti.log

```
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-819538)
       * ![](https://secure.gravatar.com/avatar/3736ab8cbf2065534acf3adb6ac197708fe6b24bae42bc5986234cd164281a33?s=50&d=blank&r=g)
Ali Cuesta
[ September 21, 2016 at 1:28 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-819751)
All set Ravi. Your the man.
[OK: FILE FOUND]
Thank you so much. ^_^
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-819751)
  51. ![](https://secure.gravatar.com/avatar/39ae8a997abf90cd318cd0b6358f27183ef41c35d5fa975ec42cc7629ff79dfd?s=50&d=blank&r=g)
Cvaa
[ September 9, 2016 at 2:25 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-814636)
Hi,
I have been trying to install cacti monitoring tools for one of our internal server, unforfunalty im facing this issue while the installation process going on..
Step: Install Cacti Tables to MySQL
