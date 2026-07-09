# make install
I am getting out :::
[root@network1 zabbix-2.4.5]# make
make: *** No targets specified and no makefile found. Stop.
[root@network1 zabbix-2.4.5]#
[root@network1 zabbix-2.4.5]# make install
make: *** No rule to make target `install’. Stop.
[root@network1 zabbix-2.4.5]#
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-771553)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ April 11, 2016 at 12:56 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-772032)
Check if you installed gcc compiler. Also check if you switched to other directory than sources dir.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-772032)
       * ![](https://secure.gravatar.com/avatar/80ed01976e97119b8eda71c2fe2f7ae347c01f3258bf7db6b2d8d02cb89be89d?s=50&d=blank&r=g)
mudit
[ April 13, 2016 at 12:32 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-772347)
While I am running Command :: make install
my output is different from your output . Please help me .
See::
[root@network1 zabbix-2.4.5]# make install
Making install in src
make[1]: Entering directory `/root/zabbix-2.4.5/src’
make[2]: Entering directory `/root/zabbix-2.4.5/src’
make[3]: Entering directory `/root/zabbix-2.4.5/src’
make[3]: Nothing to be done for `install-exec-am’.
make[3]: Nothing to be done for `install-data-am’.
make[3]: Leaving directory `/root/zabbix-2.4.5/src’
make[2]: Leaving directory `/root/zabbix-2.4.5/src’
make[1]: Leaving directory `/root/zabbix-2.4.5/src’
Making install in database
make[1]: Entering directory `/root/zabbix-2.4.5/database’
make[2]: Entering directory `/root/zabbix-2.4.5/database’
make[2]: Nothing to be done for `install-exec-am’.
make[2]: Nothing to be done for `install-data-am’.
make[2]: Leaving directory `/root/zabbix-2.4.5/database’
make[1]: Leaving directory `/root/zabbix-2.4.5/database’
Making install in man
make[1]: Entering directory `/root/zabbix-2.4.5/man’
make[2]: Entering directory `/root/zabbix-2.4.5/man’
make[2]: Nothing to be done for `install-exec-am’.
make[2]: Leaving directory `/root/zabbix-2.4.5/man’
make[1]: Leaving directory `/root/zabbix-2.4.5/man’
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-772347)
  24. ![](https://secure.gravatar.com/avatar/4cb2318b34739f68a7cd65aebba704ac903e8de69d81563c4f623514f430bedb?s=50&d=blank&r=g)
James Otto
[ March 30, 2016 at 1:33 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-767141)
When I run the command
$ mysql_secure_installation
I am prompted to “Enter the current password for root” . Since one has not been setup yet, I just press enter. I get the following error
ERROR 2002 (HY000): Can’t connect to local MySQL server through socket ‘/var/lib/mysql/mysql.sock’ (2)
Any thoughts?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-767141)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ March 30, 2016 at 3:41 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-767523)
Try to start mysql daemon then issue mysql_secure_installation command.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-767523)
  25. ![](https://secure.gravatar.com/avatar/68a11f932d51c0060aa0bc37b4a9ef04af8f1d7c710b8433057734f04cd43a00?s=50&d=blank&r=g)
Andreus
[ March 4, 2016 at 6:01 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-756547)
Thank you for tutorial work here.
congratulations.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-756547)
  26. ![](https://secure.gravatar.com/avatar/e2ce60a6484a14585172935ac8c1acf9f2a14d22153302780652b99fef6a56be?s=50&d=blank&r=g)
bonar
[ March 2, 2016 at 9:32 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-756258)
hai i got the message “Zabbix server is not running, how can i solve this?
port 10050 and 10051 open
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-756258)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ March 2, 2016 at 12:29 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-756285)
Did you used service command to get the output of zabbix daemon? Because zabbix is installed from sources, it can only be started, in this case, with /usr/local/sbin/zabbix_server command. If you run service command against zabbix you won’t get any output, right?
Confirm zabbix is listening on specific ports with netstat command!
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-756285)
  27. ![](https://secure.gravatar.com/avatar/49175e6098b35a2bb898644c5a6cf7d20a11134096acf9e5ac42d29d71940b36?s=50&d=blank&r=g)
Juan
[ February 17, 2016 at 2:02 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-751772)
Hi, i did all, and i got the message “Zabbix server is not running, how can i solve this?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-751772)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ February 17, 2016 at 8:00 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-752364)
Run the script /usr/local/sbin/zabbix_server to start Zabbix server. Then run netstat -tlpn to confirm if zabbix service is listening on the default ports.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-752364)
  28. ![](https://secure.gravatar.com/avatar/306c2cb4843ed0a66797c5210159a9e8ee32e273e671cddbac36ed1f032d9c61?s=50&d=blank&r=g)
Raqeeb
[ February 7, 2016 at 1:06 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-748690)
Hi,
I want to install Zabbix agent without opening the port 10050.Is it possible to install if it so please help me to install the zabbix agent.And also please give me a tutorials on this
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-748690)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ February 8, 2016 at 6:03 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-749128)
If you don’t open the port 10050 how do you expect zabbix agent to communicate with the server. Is there a reason why you don’t want to add this firewall rule? In case you want to change agent port number replace ListenPort zabbix_agentd directive accordingly.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-749128)
  29. ![](https://secure.gravatar.com/avatar/1ffbe0f37482badfbfa6d2c48b3c6c7910945411d94343b79eea12d1647fdfa2?s=50&d=blank&r=g)
raj
[ February 2, 2016 at 1:08 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-747038)
Hi, I am newbie to zabbix and have some clarification on how to restart the zabbix-server agent?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-747038)
  30. ![](https://secure.gravatar.com/avatar/c4fc53b741f0b07c54ffc23fc3437edb9f3704edb83eb40e406ba9e2898b2407?s=50&d=blank&r=g)
KiRill
[ February 1, 2016 at 11:46 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-746683)
Hi again. It seems to be I’m unable to
zabbix_server start/stop/restart It just does not affect zabbix service.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-746683)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ February 3, 2016 at 8:53 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-747576)
killall zabbix_server with root permissions to stop.
/usr/local/sbin/zabbix_server to start.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-747576)
  31. ![](https://secure.gravatar.com/avatar/f9c4cca67e51c0cdf0409bb27c0a208aa5bbf7485cfdf3a29305950f76833846?s=50&d=blank&r=g)
Doku
[ January 30, 2016 at 9:06 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-746079)
Hi, thanks for the tutorial.
I have a question, I hope you can help me out. I am not that firm with Linux already, but in step 5 you created a zabbix-user in order to run the daemon process with unprevileged rights.
In Step 8-18 you start the daemon. But if i start the daemon as root (which i use), i guess the services run as root? Is that right? How can i make sure to start the services as zabbix-user?
yours D.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-746079)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ February 1, 2016 at 5:40 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-746760)
Even if the service is started from root account it will automatically switch to zabbix unprivileged user account.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-746760)
  32. ![](https://secure.gravatar.com/avatar/e9bee9741b2dc26eddd68827c76e4dc120a001161fd3c310864b65f95aa1d058?s=50&d=blank&r=g)
Delorian
[ January 28, 2016 at 5:54 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-745192)
A error message appears when i login in frontend: “zabbix server is not running the information displayed may not be current”
How i can fix it?
Thanks.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-745192)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ January 30, 2016 at 5:12 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-746018)
Edit /usr/local/etc/zabbix_server.conf file and make sure the line START is set to yes (START=yes). Also verify Selinux config and the firewall to see if it’s blocking zabbix port.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-746018)
  33. ![](https://secure.gravatar.com/avatar/c4fc53b741f0b07c54ffc23fc3437edb9f3704edb83eb40e406ba9e2898b2407?s=50&d=blank&r=g)
KiRill
[ January 19, 2016 at 1:33 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-741455)
Hi. Thanks for great instruction! I have encountered with following issue. Did everything step by step following your instruction, but noticed my zabbix graphs shows wrong date/time.
I believe this is due to wrong timezone, which must be defined in /etc/apache/conf-enabled/zabbix.conf, but this file (zabbix.conf) is missing. I see from other tutorials, timezone configures exactly in /etc/apache/conf-enabled/zabbix.conf.
Zabbix is running on Deb Jessie and timezone in /etc/php.ini is set correctly.
Please advise, how I may fix it. Thanks in advance.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-741455)
     * ![](https://secure.gravatar.com/avatar/c4fc53b741f0b07c54ffc23fc3437edb9f3704edb83eb40e406ba9e2898b2407?s=50&d=blank&r=g)
KiRill
[ January 19, 2016 at 4:48 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-741506)
Do not know what was root cause, but change of:
date.timezone = Asia/Tashkent
to
date.timezone = Etc/GMT+5 solved issue. I have no idea, why date.timezone string in /etc/php5/apache2/php.ini gives wrong date/time in case of my timezone.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-741506)
  34. ![](https://secure.gravatar.com/avatar/35a859c0d721ee369c7bf427aeb4033d06d53b600003986e72eba6e2fcae7e17?s=50&d=blank&r=g)
pugazhendhi
[ January 18, 2016 at 8:23 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-740871)
Hi,
I have installed and added hosts and templates but how to monitor the cpu, memory utilization. I tried all tabs can only see the configurations setup.
Thanks
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-740871)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ January 18, 2016 at 7:05 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-741092)
Go to Configuration –> Hosts –> Graphs, for your template, select the graph that you want to monitor, then ‘Copy selected to …’, then hit ‘Go’ and select the target host/template.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-741092)
  35. ![](https://secure.gravatar.com/avatar/35a859c0d721ee369c7bf427aeb4033d06d53b600003986e72eba6e2fcae7e17?s=50&d=blank&r=g)
pugazhendhi
[ January 15, 2016 at 6:53 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-739394)
Hi, I’m installing the Zabbix in RHEL 7.2 server, from Redhat I cannot find ssmtp package, can you please help me from where I can get the same. I google already but found ssmtp package for rhel6/5 not rhel7. Thanks in advance
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-739394)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ January 15, 2016 at 11:49 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-739495)
The ssmtp package does not belong, by default, to RHEL 7 original repositories, but can be found in EPEL repo. Install it with the following command: sudo yum install epel-release
Additional info about epel project can be found here:
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-739495)
  36. ![](https://secure.gravatar.com/avatar/ab85cbbf74deb916b27f75fd58a6cea1a1740bef8ea64a358a38b4c78b47ebdf?s=50&d=blank&r=g)
William
[ January 12, 2016 at 4:22 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-737677)
Greate! Very Good!
I like tecmint very much!
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-737677)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 12, 2016 at 1:57 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-737899)
@William,
Thanks for appreciating us and liking, keep visiting tecmint..
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-737899)
  37. ![](https://secure.gravatar.com/avatar/af2489e715b2d76dfccbfd03e5ca0f992c946c46acb515416a5f64b77fcf5a01?s=50&d=blank&r=g)
Matthias
[ January 9, 2016 at 5:23 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-736276)
thanks for the perfect todo
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-736276)
  38. ![](https://secure.gravatar.com/avatar/35a859c0d721ee369c7bf427aeb4033d06d53b600003986e72eba6e2fcae7e17?s=50&d=blank&r=g)
pugazhendhi
[ January 9, 2016 at 3:34 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-736235)
Hi, In the step 3: When the installation of Mariadb finishes, secure the database by issuing mysql_secure_installation command with system root privileges, I ran “# mysql_secure_installation”,
when asked for “Enter current password for root (enter for none):” I gave server root login password it doesn’t accept, i just pressed enter didn’t accept. Kindly assist here.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-736235)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 11, 2016 at 1:24 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-737263)
@pugazhendhi,
No need to type the current root password, just enter and when asked to set new mysql root password, set it there and carry further steps..
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-737263)
  39. ![](https://secure.gravatar.com/avatar/1a1e35e693d79c32cbf58931a610ac51f4ec831feef2a9158d1b2fcef8a2125d?s=50&d=blank&r=g)
Assis Regis Corrêa
[ December 14, 2015 at 7:23 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-724062)
good morning.
MariaDB [(none)]> grant all privileges on zabbix.* to zabbix@’localhost’ identified by ‘password’;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ‘identified by ‘password” at line 1
help-me please.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-724062)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ December 15, 2015 at 11:02 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-724347)
@Assis,
Yes, there is a error in your MySQL command, the correct way to run the command is:
```
MariaDB [(none)]> grant all privileges on zabbix.* to zabbix@'localhost' identified by 'password';

```
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-724347)
       * ![](https://secure.gravatar.com/avatar/1a1e35e693d79c32cbf58931a610ac51f4ec831feef2a9158d1b2fcef8a2125d?s=50&d=blank&r=g)
Assis Régis Corrêa
[ December 18, 2015 at 6:57 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-725720)
I got with the command below:
MariaDB [(none)]> grant all privileges on zabbix.* to zabbix@’%’ identified by ‘password’;
Thank you very much,
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-725720)
  40. ![](https://secure.gravatar.com/avatar/681da3df26e5dfedbb0aa8f679f02f375d2d28e4a7703db0ea2aeb97769ce0f7?s=50&d=blank&r=g)
donmay
[ November 26, 2015 at 2:40 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-714121)
hi thank you very much for the wonderful tutorial
please i am getting this error
441:20151126:100552.738 [Z3001] connection to database ‘zabbix’ failed: [2002] Can’t connect to local MySQL server through socket ‘/var/run/mysqld/mysql.sock’ (2)
441:20151126:100552.738 database is down: reconnecting in 10 seconds
is there something i am missing
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-714121)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 30, 2015 at 10:57 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-716649)
@Donmay,
The error clearly indicates that your MySQL service is not started, try to restart the MySQL service.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-716649)
       * ![](https://secure.gravatar.com/avatar/681da3df26e5dfedbb0aa8f679f02f375d2d28e4a7703db0ea2aeb97769ce0f7?s=50&d=blank&r=g)
donmay
[ December 4, 2015 at 12:25 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-718774)
thank you i treid restarting the server as well as also the server many times but it does not connect…..
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-718774)
         * ![](https://secure.gravatar.com/avatar/080661c98d054bc4c0f62e68c0f07afb20d5ca99c6d0dfb961542a9136b04b5e?s=50&d=blank&r=g)
Forty
[ December 4, 2015 at 4:47 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-719127)
Hello Donmay,
I had the same issue yesterday. Please check your config corresponding the right mysqld.sock filename.
In my case under /etc/mysql/my.cnf:
[mysqld_safe]
socket = /var/run/mysqld/mysqld.sock
nice = 0
This value has to be the same in config file /usr/local/etc/zabbix_server.conf in value “DBSocket”.
After installation my path configuration was:
/var/run/mysqld/mysql.sock
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-719127)
  41. ![](https://secure.gravatar.com/avatar/aee96b6f32ec748c931f086c7eaa25b7de626d12878025aa0ae62f947d9ca6ce?s=50&d=blank&r=g)
Volnei
[ November 17, 2015 at 6:27 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-707589)
It has step by step to make the update of this version of the most current Zabbix ?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-707589)
  42. ![](https://secure.gravatar.com/avatar/7d716ecc93a80966df85aae85a6420e3f344ecf13102f013a241725e6a4e72b8?s=50&d=blank&r=g)
Serkis
[ October 28, 2015 at 6:36 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-696878)
Hi man, don’t exist this path: “/usr/local/etc/zabbix_server.conf” in my installation. Nano creates a new file in blank, but don’t appear something write. I’m trying Zabbix 2.4.6.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-696878)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ October 29, 2015 at 2:30 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-697551)
Did you changed the installation path while compiling zabbix sources or installed zabbix from binary?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-697551)
  43. ![](https://secure.gravatar.com/avatar/1293a11b03dd9c7f3cda1c6dff81066ec971efa6b621157ab4c5eb6a0d7da882?s=50&d=blank&r=g)
tokanava
[ October 22, 2015 at 4:56 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-692017)
Hi! cool manual! correct…
tar xfz zaBix-2.4.5.tar.gz
