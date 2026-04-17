Thank you Ravi. I found my mistake.;
#*/5 * * * * cacti /usr/bin/php /usr/share/cacti/poller.php > /dev/null 2>&1
I delete the # sign :D
Now it is running smoothly.
I’ll try to build add-ons. (plugins)
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 31, 2016 at 3:06 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785331)
@Volkan,
I am glad that finally you found the mistake yourself and corrected, good luck for rest of things..
  68. ![](https://secure.gravatar.com/avatar/3d2a62fa9c0cb8601e6c075b1fbcc4847a31a255d430f8f546f0f53c463658e9?s=50&d=blank&r=g)
Dennis
[ May 30, 2016 at 8:29 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785003)
HI Ravi,
Just want to know why my graph all show “rrd file does not exist”?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785003)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 30, 2016 at 11:14 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785034)
@Dennis,
Please let me know what’s the group:owner permission of rrd files and directory? it should be apache:apache to function properly..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785034)
       * ![](https://secure.gravatar.com/avatar/3d2a62fa9c0cb8601e6c075b1fbcc4847a31a255d430f8f546f0f53c463658e9?s=50&d=blank&r=g)
Dennis
[ May 31, 2016 at 6:11 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785233)
[root@hpdcentos3 ~]# ls -l /usr/share | grep rrd
drwxr-xr-x. 2 root root 6 Nov 21 2015 rrdtool
[root@hpdcentos3 ~]# ls -l /usr/share/cacti/lib | grep rrd
-rw-r–r–. 1 root root 91557 Feb 8 03:26 rrd.php
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785233)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 31, 2016 at 11:31 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785287)
@Dennis,
It should be user/group apache, change the **rrd** directory and files ownership to apache recursively as shown
```
# chown -R apache:apache path-to-rrd-directory

```
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785287)
           * ![](https://secure.gravatar.com/avatar/3d2a62fa9c0cb8601e6c075b1fbcc4847a31a255d430f8f546f0f53c463658e9?s=50&d=blank&r=g)
Dennis
[ May 31, 2016 at 3:08 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785333)
now my graph doesnt show any CPU utilization.
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 31, 2016 at 3:57 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785344)
@Dennis,
After making changes, did you ran the **poller.php** file manually to collect data?
           * ![](https://secure.gravatar.com/avatar/3d2a62fa9c0cb8601e6c075b1fbcc4847a31a255d430f8f546f0f53c463658e9?s=50&d=blank&r=g)
Dennis
[ May 31, 2016 at 4:59 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785361)
Hi Ravi, how to run the poller.php?
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 31, 2016 at 5:20 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785365)
@Dennis,
Here is the command to execute and populate cacti graphs with data..
```
# /usr/bin/php /usr/share/cacti/poller.php

```

           * ![](https://secure.gravatar.com/avatar/3d2a62fa9c0cb8601e6c075b1fbcc4847a31a255d430f8f546f0f53c463658e9?s=50&d=blank&r=g)
Dennis
[ June 3, 2016 at 10:01 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-786742)
Hi Ravi,
thanks, I’ve run the command you gave me. But my poller time seems a bit off, it seem to be pulling data from my servers at 8 hrs late. i check all timezones are set to +8 including the ones in php.ini file. Please advise.
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 3, 2016 at 11:16 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-786768)
@Dennis,
Better sync your server time with NTP, here is the guide on how to do it <https://www.tecmint.com/install-ntp-server-in-centos/>
           * ![](https://secure.gravatar.com/avatar/3d2a62fa9c0cb8601e6c075b1fbcc4847a31a255d430f8f546f0f53c463658e9?s=50&d=blank&r=g)
Dennis
[ June 3, 2016 at 11:55 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-786794)
Hi Ravie,
Have setup NTP and configured according to yout tutorial. here is my system date.
[root@hpdcentos3 local]# **date**
Fri Jun 3 14:20:52 MYT 2016
[root@hpdcentos3 local]# **timedatectl**
Local time: Fri 2016-06-03 14:21:11 MYT
Universal time: Fri 2016-06-03 06:21:11 UTC
RTC time: Fri 2016-06-03 06:21:11
Time zone: Asia/Kuala_Lumpur (MYT, +0800)
NTP enabled: yes
NTP synchronized: yes
RTC in local TZ: no
DST active: n/a
[root@hpdcentos3 local]# **date -R**
Fri, 03 Jun 2016 14:21:36 +0800
[root@hpdcentos3 local]# **date**
Fri Jun 3 14:21:40 MYT 2016
[root@hpdcentos3 local]#
but my graph is still 8hr late.
did i miss anything??
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 4, 2016 at 11:27 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-787506)
@Dennis,
Everything seems perfect, don’t know why such delay in generating graphs, let me dig into this and get back to you..
  69. ![](https://secure.gravatar.com/avatar/037e06aadc4d762fc62def99524693e6dddfd98efbeddcf2dcb102703010cf20?s=50&d=blank&r=g)
Nick
[ May 28, 2016 at 11:08 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-784758)
what is the cacti user password?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-784758)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 30, 2016 at 11:20 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785039)
@Nick,
It should be **admin** as username and password as **admin** , try it and see..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785039)
  70. ![](https://secure.gravatar.com/avatar/ab8ae1585ed86cc28486e759fb4c6d23e51f40cbb83b9925ca5c31e378080add?s=50&d=blank&r=g)
Gabriel
[ May 28, 2016 at 1:32 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-784570)
After installing and doing all the steps of the guide I go to my cacti page and see just a blank page. Please your help I’m trying to install this server for 2 weeks now.
Thanks
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-784570)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 28, 2016 at 10:38 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-784645)
@Gabriel,
Sorry to hear that, may I know on which Linux distributions you’re trying? and you’ve followed cacti installation instructions correctly, could you give a try again? or else give me access to your server, let me setup for you for free.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-784645)
       * ![](https://secure.gravatar.com/avatar/06911fe94130b23139c7c2b526771baa4f30788cb0a2e25ea0586fbea8539e50?s=50&d=blank&r=g)
Pablo
[ May 30, 2016 at 6:04 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785105)
Hello Ravi,
Thanks for your reply, I’m installing Cacti on CentOS 6.3. I’ve followed all the instructions. I should re-install again?
Regards,
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785105)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 31, 2016 at 11:47 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785295)
@Pablo,
Give a re-try and see, if you still not able to install properly, will help out in setting up.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785295)
           * ![](https://secure.gravatar.com/avatar/ab8ae1585ed86cc28486e759fb4c6d23e51f40cbb83b9925ca5c31e378080add?s=50&d=blank&r=g)
Gabriel
[ June 1, 2016 at 12:48 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785459)
Ravi, i just finished the re-install and the cacti server started and is working now, a little weird, thank you for your help anyway.
Regards,
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 1, 2016 at 1:08 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785624)
@Gabriel,
Good to know that finally you managed to install Cacti successfully…
       * ![](https://secure.gravatar.com/avatar/ab8ae1585ed86cc28486e759fb4c6d23e51f40cbb83b9925ca5c31e378080add?s=50&d=blank&r=g)
Gabriel
[ May 30, 2016 at 11:34 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785165)
If you could please I can give you access through TV.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785165)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 31, 2016 at 11:32 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-785288)
@Gabriel,
Please mail the TeamViewer details to
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-785288)
  71. ![](https://secure.gravatar.com/avatar/06911fe94130b23139c7c2b526771baa4f30788cb0a2e25ea0586fbea8539e50?s=50&d=blank&r=g)
Plaza
[ May 28, 2016 at 1:20 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-784566)
I followed all the steps and all I see is a blank page, please your help with this.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-784566)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 28, 2016 at 10:39 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-784646)
@Plaza,
Please let me know on which Linux distributions you’re trying to install cacti? have you installed all required packages correctly?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-784646)
  72. ![](https://secure.gravatar.com/avatar/2ba70697bba7819219a419f4ef2b081d2ea3577f34c13b8acecbefeafaa705ea?s=50&d=blank&r=g)
trongtrong
[ May 20, 2016 at 10:01 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-782406)
hi, t have error “SNMP ERROR” when t try “add new device”, pls help me fix this
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-782406)
  73. ![](https://secure.gravatar.com/avatar/3d2a62fa9c0cb8601e6c075b1fbcc4847a31a255d430f8f546f0f53c463658e9?s=50&d=blank&r=g)
Dennis
[ May 18, 2016 at 11:09 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-781639)
it is also not pulling any data from my servers using snmp but data from network switches came thru.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-781639)
  74. ![](https://secure.gravatar.com/avatar/3d2a62fa9c0cb8601e6c075b1fbcc4847a31a255d430f8f546f0f53c463658e9?s=50&d=blank&r=g)
Dennis
[ May 18, 2016 at 11:07 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-781638)
Hi, my graphs are 8hours late. How do i go about this? Thx
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-781638)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 18, 2016 at 11:55 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-781655)
@Dennis,
I think you should sync your system time with NTP to have proper graphs based on correct time, just check your system time is correct?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-781655)
       * ![](https://secure.gravatar.com/avatar/3d2a62fa9c0cb8601e6c075b1fbcc4847a31a255d430f8f546f0f53c463658e9?s=50&d=blank&r=g)
Dennis
[ May 19, 2016 at 10:26 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-782002)
hi Ravi,
i read in another forum that suggest to install webmin. After i install & configured admin hardware time setting, my graph time is accurate.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-782002)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 19, 2016 at 12:06 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-782047)
@Dennis,
Thanks for sharing your findings, and I am glad that it finally showing correct graphs based on time…
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-782047)
  75. ![](https://secure.gravatar.com/avatar/759f9a220e5d2d10fac4c49969b4706d9ef2716b36889c5f1782b3ba9f7e1e82?s=50&d=blank&r=g)
Banu
[ May 4, 2016 at 2:54 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-776330)
Where’s the cacti path installed?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-776330)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 4, 2016 at 3:04 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-776333)
@Banu,
There isn’t any one place, the Cacti tool gets installed all over the file-system, but the main configuration files resides under **/etc/cacti** directory..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-776333)
  76. ![](https://secure.gravatar.com/avatar/c0f3850e26e8f3888c46a76ce651454f35d366493448561d446a65f18f5a6a3a?s=50&d=blank&r=g)
Szilard
[ April 22, 2016 at 12:35 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-773648)
In case of mysql is not on localhost you also need to enable network access for httpd (SElinux) else you will have errors like :
FATAL: Cannot connect to MySQL server on ‘192.168.1.10’. Please make sure you have specified a valid MySQL database name in ‘include/config.php’
setsebool -P httpd_can_network_connect=1
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-773648)
  77. ![](https://secure.gravatar.com/avatar/6c3b1af0b98d39e4ee7e2510b558236091bac79906370e97dcae94edcb61a20d?s=50&d=blank&r=g)
Zaya
[ April 18, 2016 at 6:37 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-773054)
I have a problem same as Jhay, When I have got “FATAL: Cannot connect to MySQL server on ‘10.0.0.1’. Please make sure you have specified a valid MySQL database name in ‘include/config.php’”.
My server is running on 10.0.0.1.
I have created cacti database on mysql, and mysql is working fine. How I can solve?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-773054)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 19, 2016 at 10:01 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-773115)
@Zaya,
Please add the 10.0.0.1 IP address in **db.php** file under **/etc/cacti/** directory like this:
```
$database_hostname = "10.0.0.1";

```

I hope it will solve your MySQL connectivity problem..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-773115)
  78. ![](https://secure.gravatar.com/avatar/4cb2318b34739f68a7cd65aebba704ac903e8de69d81563c4f623514f430bedb?s=50&d=blank&r=g)
James Otto
[ March 29, 2016 at 9:12 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-767078)
When I try to start mysql service I get the following error
[vagrant@server1 /]$ sudo service mysqld start
Redirecting to /bin/systemctl start mysqld.service
Failed to start mysqld.service: Unit mysqld.service failed to load: No such file or directory.
What file or directory is missing?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-767078)
  79. ![](https://secure.gravatar.com/avatar/b419e71710068e78a70999fbe17b8602c872117325190b586e0562888b8e6310?s=50&d=blank&r=g)
Guilherme Henrique
[ March 10, 2016 at 6:57 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-758491)
Dear Mr. Ravi Saive, thank you for a great explanation.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-758491)
  80. ![](https://secure.gravatar.com/avatar/834e6a4d1d43c09c3543603c4a77538f828005e05f6c61eaa3ec569ed07735f8?s=50&d=blank&r=g)
Subhasish Bhattacharya
[ February 18, 2016 at 6:12 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-752666)
Dear Mr. Ravi Can you please provide some thorough tutorial on oracle DBA administration. from very first installation to common problems manage/troubleshoot oracle 11G/12C. I will be thankful to you.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-752666)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 18, 2016 at 7:03 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-752681)
@Subhasish,
We’ve already covered about Oracle related articles, here is the installation of Oracle 11g and 12c:
<https://www.tecmint.com/oracle-database-11g-release-2-installation-in-linux/>
<https://www.tecmint.com/oracle-12c-installation-in-centos-6/>
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-752681)
  81. ![](https://secure.gravatar.com/avatar/6bf5eef8028cfcffd1531582f5c07b9f2ed6bfa60276608944577de5622d5c54?s=50&d=blank&r=g)
Jhay Brombuela
[ February 15, 2016 at 6:58 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-750947)
Hi
I have error on Cacti Installation which is “FATAL: Cannot connect to MySQL server on ‘localhost’. Please make sure you have specified a valid MySQL database name in ‘include/config.php'” pls help me to fix this
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-750947)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 15, 2016 at 11:07 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-751012)
@Jhay,
It’s clear that the MySQL cacti database doesn’t exits on the server, have you created Cacti database in the MySQL server, before attempting installation? Please create one as instructed it this article and try again the installation..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-751012)
       * ![](https://secure.gravatar.com/avatar/6bf5eef8028cfcffd1531582f5c07b9f2ed6bfa60276608944577de5622d5c54?s=50&d=blank&r=g)
Jhay Brombuela
[ February 18, 2016 at 11:25 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-752566)
Hi Sir @Ravi Saive, I already fixed my problem. I noticed the password that i set in MySql Settings for cacti was not match to my root password. I am now able to use CACTI. Thank you for your response and thanks for this great tutorial. Hope you post a tutorial of Installation and configuration of Samba file server and Squid proxy server. God bless you Sir….
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-752566)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 18, 2016 at 2:18 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-752599)
@Jhay,
That’s good to hear that you’ve fixed problem yourself and thanks for appreciating my work. Yes, we’re already covered about Samba and Squid server related articles here, you can go through it.
<https://www.tecmint.com/setup-samba-file-sharing-for-linux-windows-clients/>
<https://www.tecmint.com/configure-squid-server-in-linux/>
Keep visiting and God bless you too brother..:)
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-752599)
  82. ![](https://secure.gravatar.com/avatar/362df876ef585d08ee46c5888ddd49e69dcf88dc1c5b442632aea5b8dff397ee?s=50&d=blank&r=g)
Jolene9
[ February 11, 2016 at 1:36 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-749952)
Hi,
I have finished Cacti installations but i still can’t see graphs. For rrd files RRDTools says ‘ERROR: opening ‘/usr/share/cacti/rra/localhost_load_1min_5.rrd’: No such file or directory’.. I’ve tried changing the group ownership of rra directory to apache as mentioned above but it didn’t work.
What I’m supposed to do next? Hope that there’s someone who can help here.
Thanks!
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-749952)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 13, 2016 at 12:53 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-750467)
@Jolene,
It seems that rrdtool tool didn’t generating those files, it could be the permission issues on /usr/share/cacti/ directory or try to rebuild Poller Cache from System Utilities (bottom of console).
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-750467)
       * ![](https://secure.gravatar.com/avatar/dff067596f412e801add4c0a80d9c2ac15fd7dc59ce71ded6eb7ab46c3f8c8d9?s=50&d=blank&r=g)
Aleksei
[ February 19, 2016 at 12:31 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-752996)
I have another problem, that all graps are not showing anything, they are empty, just none.
Where the problem could be?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-752996)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 20, 2016 at 10:41 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-753481)
@Aleksei,
Please check your SELinux settings and try to disable it and run the poller cron again and see the graphs are generating or not. Also check logs for any errors..
