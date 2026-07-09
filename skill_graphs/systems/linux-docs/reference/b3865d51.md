# mysql -u cacti -p cacti < /usr/share/doc/cacti-1.1.24/cacti.sql
Enter password:
ERROR 1045 (28000): Access denied for user 'cacti'@'localhost' (using password: YES)
Forbidden
You don't have permission to access /cacti on this server.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-929775)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 1, 2017 at 11:02 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-929846)
@Sanmao,
Have you created Create MySQL Cacti Database? Please follow instructions carefully..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-929846)
       * ![](https://secure.gravatar.com/avatar/754d34752a9c9826876cf007e02974beb3008e2e5cfa15afd693a87208f109b9?s=50&d=blank&r=g)
Raju
[ December 18, 2017 at 3:19 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-951045)
i create the database but still, i am getting the error.
MariaDB [(none)]> GRANT ALL ON cacti.* TO cacti@localhost IDENTIFIED BY ‘raju’; Query OK, 0 rows affected (0.02 sec)
is that ok?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-951045)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ December 18, 2017 at 10:40 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-951175)
@Raju,
Yes the MySQL query for granting permission on Cacti database to user cacti is correct. Could you please check the logs or post error here?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-951175)
  27. ![](https://secure.gravatar.com/avatar/daaba2a9bfe2d841e6a6485c1fec3b93f4fc0ca71806954bd3e6fe86faa4247c?s=50&d=blank&r=g)
Arpit
[ October 23, 2017 at 12:07 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-926020)
Hi, I am install cacti successfully, but when i install plug-ins, it can’t work and i am install older version of cacti it is work fine please resolve this issue.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-926020)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 25, 2017 at 11:27 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-926750)
@Arpit,
What errors you see while installing cacti Plugins? could you share here so that we can help you out.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-926750)
  28. ![](https://secure.gravatar.com/avatar/3d1ce28111e1c95f7c8e98e9a65efba64c4e4609a5e60b31d06ffc97920641a8?s=50&d=blank&r=g)
Hkimleang
[ October 2, 2017 at 9:30 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-917129)
ERROR: Your MySQL TimeZone database is not populated. Please populate this database before proceeding.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-917129)
  29. ![](https://secure.gravatar.com/avatar/96588eb58b79507f8f71e88ffcfee56704134bc18a5ef52f1197fe8807c0b022?s=50&d=blank&r=g)
Danza
[ September 24, 2017 at 2:07 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-915731)
If I want use domain-name to access to my cacti server, instead of ip address. How could we do this?
For example: cacti.abc.com, instead of typing my ip address 192.168.X.X.
Thanks
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-915731)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ September 25, 2017 at 10:57 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-915887)
@Danza,
Create a local virtualhost on Apache and point DocumentRoot to Cacti directory and in your desktop machine add local domain to hosts file.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-915887)
  30. ![](https://secure.gravatar.com/avatar/5597e8165090cbe917595743b586ea0906a99ae5ab1087ecfb5d2bd1f39b0cf4?s=50&d=blank&r=g)
Maurin
[ May 19, 2017 at 12:52 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-890660)
when i tape ‘yum install cacti’ it says that no package cacti are available. What should i do ?!
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-890660)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 19, 2017 at 1:20 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-890668)
@Maurin,
First, you need to enable EPEL Repository in your system to install Cacti package.
```
# yum install epel-release
# yum install cacti

```
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-890668)
  31. ![](https://secure.gravatar.com/avatar/6a664c10f44be5d983dce96dc8b0f5a4a529fd2f0eb96723a9cc41aef6c00da4?s=50&d=blank&r=g)
sAm IT
[ May 4, 2017 at 5:20 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-887738)
when entering on browser
This page isn’t working
103.74.227.22 is currently unable to handle this request.
HTTP ERROR 500
but when I enter

then install screen appears.
what could be the problem, and how to get rid of it.
Note: I turned off my firewall still the same problem.
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-887738)
  32. ![](https://secure.gravatar.com/avatar/6a664c10f44be5d983dce96dc8b0f5a4a529fd2f0eb96723a9cc41aef6c00da4?s=50&d=blank&r=g)
sAm IT
[ May 4, 2017 at 5:14 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-887736)
hey Brother..
i have done everything .
only problem i am facing now is that when i enter

This page isn’t working
103.xx.101.10 is currently unable to handle this request.
HTTP ERROR 500
but if i enter

then the install screen is working.
what could be the problem and how to solve it ?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-887736)
     * ![](https://secure.gravatar.com/avatar/bb04588584928b7a8e077a6c76c90fbd97a163a4a4d016cec19b2d3b598bb298?s=50&d=blank&r=g)
Kelly
[ July 26, 2018 at 1:36 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-1018510)
I’m also getting a 500 error, I’ve gone through the procedures 3 times. What fixed it?
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-1018510)
  33. ![](https://secure.gravatar.com/avatar/6a664c10f44be5d983dce96dc8b0f5a4a529fd2f0eb96723a9cc41aef6c00da4?s=50&d=blank&r=g)
sAm IT
[ May 1, 2017 at 8:01 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-887350)
I am getting an error.
Error: your MYSQL timezone database is not populated. please populate the database before proceeding
I found many solutions on via google but none is working for me.
the most popular solutions are
1) shell> mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root mysql
when I run the above command it shows an arrow like this ( —-> ), after that I don’t know what to do.
2) second solution was
grant select on mysql.time_zone_name to cacti@localhost identified by ‘**your pass**)
when I run this second solution command it accepts it but still error is same.
please help ASAP
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-887350)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 2, 2017 at 11:42 am  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-887467)
@Sam,
Try these commands to fix that MYSQL timezone database is not populated error.
```
# cd cacti/cli
# php repair_database.php --force
# php upgrade_database.php

```

it will solve your problem..
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-887467)
       * ![](https://secure.gravatar.com/avatar/6a664c10f44be5d983dce96dc8b0f5a4a529fd2f0eb96723a9cc41aef6c00da4?s=50&d=blank&r=g)
sAm IT
[ May 2, 2017 at 3:38 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-887507)
thanks for the reply
now I am having an error at cacti installation wiz screen as
Spine Binary File Location: The path to Spine binary.
/usr/local/spine/bin/spine (X)
means there is some problem with the location of the file or maybe the file is not on correct location, or maybe the file is not present on the server
[Reply](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/#comment-887507)
         * ![](https://secure.gravatar.com/avatar/6a664c10f44be5d983dce96dc8b0f5a4a529fd2f0eb96723a9cc41aef6c00da4?s=50&d=blank&r=g)
sAm IT
[ May 2, 2017 at 7:28 pm  ](https://www.tecmint.com/install-cacti-network-monitoring-on-rhel-centos-fedora/comment-page-2/#comment-887536)
i found out that i have to install the spine manually done installing it and configuring it
im not getting how to set spine file location
second main issue im facing is that snmp queries not writable error at directory permissions checks screen
i saw a video a person entered command
