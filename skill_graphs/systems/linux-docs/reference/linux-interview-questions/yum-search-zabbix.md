# yum search zabbix*
Did clean by `yum clean all` and after that, I tried to remove them by `yum remove Zabbix` but it shows there is no package installed.
Try to delete Zabbix-release by `rpm -e Zabbix-release` but didn’t find anything.
I want 6.2 but Zabbix 50 and 4 conflict with them and also didn’t be deleted. One more thing did anyone let me know where the **zabbix.arch** files placed.
–> Finished Dependency Resolution
Error: zabbix50 conflicts with zabbix40-4.0.39-1.el7.x86_64
You could try using –skip-broken to work around the problem
You could try running: rpm -Va –nofiles –nodigest
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1927449)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ December 12, 2022 at 11:51 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1928620)
@Desh,
First, you need to remove the already installed **zabbix40** which is not Zabbix official package as shown.
```
# yum remove zabbix40

```

After removing all **zabbix40** packages, you can follow the guide to install Zabbix from official repo as shown in this article…
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1928620)
  3. ![](https://secure.gravatar.com/avatar/02912fe32c6b0949362adf870dc0edf8bdaca349acd1b7cb7861ae68da318814?s=50&d=blank&r=g)
Pankaj Sharma
[ October 18, 2022 at 7:45 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1900602)
How to resolve the error:
`skipping https://repo.zabbix.com/zabbix/5.4/rhel/7/x86_64/zabbix-release-5.4-1.el7.noarch.rpm
 - transfer failed`
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1900602)
  4. ![](https://secure.gravatar.com/avatar/06716a8d2ca8ffcf8fccf6db8b720570356e0a238afa812450572e60a1a91422?s=50&d=blank&r=g)
Kapil Sharma
[ January 9, 2022 at 5:26 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1698945)
**zabbix.conf** file is not found using the above guide?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1698945)
  5. ![](https://secure.gravatar.com/avatar/80286fab7ffbb4915e0081cf2c19461df634d60f5fdda95d18bf59dabab19892?s=50&d=blank&r=g)
vishwajeet dharmpal kamble
[ October 25, 2021 at 5:52 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1620844)
Awesome article, please post on updated version and troubleshooting solution on Zabbix.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1620844)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 27, 2021 at 3:12 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1623076)
@vishwanjeet,
We’ve updated the Zabbix article to the latest version as requested…
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1623076)
  6. ![](https://secure.gravatar.com/avatar/cfbc52eee454d022066def8f0dac77092e9c5c5be5fbec88036f539d0f20fe96?s=50&d=blank&r=g)
George Jebaraj
[ April 12, 2021 at 1:21 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1474878)
How to add a windows client on the Zabbix server?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1474878)
  7. ![](https://secure.gravatar.com/avatar/8c87b08f359648fca3610f2a5a4e7be2b71ceab09880d035bb5350a5af57e812?s=50&d=blank&r=g)
Hung Vo
[ March 12, 2019 at 5:51 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1111120)
I have error **date.timezone** , can’t install even i did edit `php.ini` still have issue any idea?
Thanks
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1111120)
  8. ![](https://secure.gravatar.com/avatar/008dfeff68868edf7d0be0496c695fbc799de1d249f8d37091a5ea137adca9c8?s=50&d=blank&r=g)
jose
[ July 30, 2018 at 7:53 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1019569)
I solved installing **zabbix 4.0** in **Debian 9**.
```
# wget http://repo.zabbix.com/zabbix/3.5/debian/pool/main/z/zabbix-release/zabbix-release_3.5-1%2Bstretch_all.deb
# dpkg -i zabbix-release_3.5-1+stretch_all.deb
# apt-get update
# apt-get install zabbix-server-mysql (zabbix 4.0)

```
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1019569)
  9. ![](https://secure.gravatar.com/avatar/008dfeff68868edf7d0be0496c695fbc799de1d249f8d37091a5ea137adca9c8?s=50&d=blank&r=g)
jose
[ July 30, 2018 at 5:46 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1019542)
At the point 4 the packet **libmysql-dev** send package **libmysqld-dev** is not available and **libmariadbd18** , **libmariadbd-dev** is available.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1019542)
  10. ![](https://secure.gravatar.com/avatar/396b874e880c53f113e06ee5e8cfe153cfa622a9ea8847ca44bf69c9dfe14e89?s=50&d=blank&r=g)
wyzel
[ July 30, 2018 at 8:53 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1019454)
At the point 15, the URL should be:
```
http://192.168.1.151/zabbix/setup.php
OR
https://192.168.1.151/zabbix/setup.php

```
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1019454)
  11. ![](https://secure.gravatar.com/avatar/008dfeff68868edf7d0be0496c695fbc799de1d249f8d37091a5ea137adca9c8?s=50&d=blank&r=g)
jose uzin
[ July 28, 2018 at 8:19 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1019158)
You don´t create the zabbix user in the system is necessary?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1019158)
  12. ![](https://secure.gravatar.com/avatar/08d4496b5950593fa641860a1c47740818552e6be88c95e2ee745868921f5dea?s=50&d=blank&r=g)
vipul
[ July 21, 2018 at 5:31 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1017689)
please remove php-bcmath- “-” remove this from command
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-1017689)
  13. ![](https://secure.gravatar.com/avatar/416224f0bd57fd1cb812637fbb744a1162d094b774b2031c7bc20e7feaa01a2e?s=50&d=blank&r=g)
johnn
[ February 28, 2018 at 9:34 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-973213)
Hello Matei,
I find a little spelling mistake through the guide:
“MariaDB [(none)]> create database zabbixdb character set utf8 collate utf8_bin;”
Thanks for detailed sharing and hope this helps.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-973213)
  14. ![](https://secure.gravatar.com/avatar/336773483293e6782b7dcaaf88997a1e5eb75d69dcc3ab87532bc6a406a87b44?s=50&d=blank&r=g)
suresh
[ January 16, 2018 at 1:55 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-961153)
database name has typo error which creates the issues while login.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-961153)
  15. ![](https://secure.gravatar.com/avatar/3e899696b98700030861dda6007ed5f0f4e77186af3055d3f5e97369ff459b65?s=50&d=blank&r=g)
carlos
[ October 18, 2017 at 4:04 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-924238)
Good Day,
Finally I found a direct tutorial and to the core of how to install this application so novel, after about 30 failed installation attempts of other pages, this was the only one that actually helped me.
Thank you! I will be attentive to your forum!
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-924238)
  16. ![](https://secure.gravatar.com/avatar/3cd7b9329ff85ceedd598a74abb3c04247ecf8fb739aa96446175df306f5f771?s=50&d=blank&r=g)
NOV Piseth
[ March 19, 2017 at 4:11 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-876618)
I just shared my experience Zabbix with CentOS 7. in case you not yet disabled firewall and selinux you need to some command for allow Zabbix and httpd work together as below:
```
# firewall-cmd --zone=public --add-port=80/tcp --permanent
# firewall-cmd --zone=public --add-port=10050/tcp --permanent
# firewall-cmd --zone=public --add-port=10051/tcp --permanent
# firewall-cmd --reload

```

SELinux rule
```
# setsebool -P httpd_can_network_connect on
# setsebool -P httpd_can_connect_zabbix 1
# setsebool -P zabbix_can_network 1

```

and restart apache and zabbix server.
if not like this you will see the message announce that;
your zabbix server is not running….
for who have problem the same as me.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-876618)
  17. ![](https://secure.gravatar.com/avatar/16edfd7b938c6a56b66e95903455d718eb9d9a87ec7085cd9bacd8ea75ee0bb5?s=50&d=blank&r=g)
Ranjeet Kumar
[ August 30, 2016 at 11:17 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-811038)
Dear Sir,
please help me to solve this issue in CentOS7 how can i enabled this i am tired to resolve this issue.
PHP bcmath off Fail
PHP mbstring off Fail
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-811038)
     * ![](https://secure.gravatar.com/avatar/e7a250579bc7b675f8ba7ec48b64c58691dd029f9a438b65577e013bd7c08437?s=50&d=blank&r=g)
Danny
[ December 3, 2016 at 3:22 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-843855)
Hi,
dnf install php-bcmath php-mbstring
That’s it.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-843855)
  18. ![](https://secure.gravatar.com/avatar/7b58a4f6a27996573dd69e731c09fd3a314146b6c5c5a92b2762b6add8af4815?s=50&d=blank&r=g)
ShadLaye
[ August 25, 2016 at 9:39 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-809612)
Hi! i’m senegalese and i speak english a little. But i confirm it’s work for me 100% on debian. Thank’s for this topic. Good luck for the next!
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-809612)
  19. ![](https://secure.gravatar.com/avatar/c130f1413b5b76bdbd78dcef650f001c4752ca17f4c50f0ac12b96f721ba7451?s=50&d=blank&r=g)
Kostyanius
[ June 11, 2016 at 3:26 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-790195)
I have followed step by step according to this instruction. But it is not working for Debian 8. I am getting an error message: Zabbix server is not running.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-790195)
     * ![](https://secure.gravatar.com/avatar/c130f1413b5b76bdbd78dcef650f001c4752ca17f4c50f0ac12b96f721ba7451?s=50&d=blank&r=g)
Kostyanius
[ June 11, 2016 at 6:39 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-790316)
My mistake. There were two users (root and zabbix) in zabbix config file, that caused an issue with db connection. After i commented out the root user there the issue has gone.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-790316)
       * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ June 21, 2016 at 7:53 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-793446)
Good to know is working…
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-793446)
         * ![](https://secure.gravatar.com/avatar/dd2548c1c0bd9541363a7e9a4432f5e734b2886129665e7a0561650c700a75cf?s=50&d=blank&r=g)
ahmed
[ November 29, 2016 at 5:13 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-842779)
please type the step because it is not work with me ??
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-842779)
       * ![](https://secure.gravatar.com/avatar/1396420428f95fc71ac03993f91ce9de85926f11f3d3826738ca7f2e88ebb01b?s=50&d=blank&r=g)
daniel
[ March 24, 2017 at 8:05 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-877918)
i have the same problem but your solution didn’t work with me.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-877918)
         * ![](https://secure.gravatar.com/avatar/1396420428f95fc71ac03993f91ce9de85926f11f3d3826738ca7f2e88ebb01b?s=50&d=blank&r=g)
daniel
[ March 24, 2017 at 8:22 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-877922)
got it !! i just have restart my server on debian
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-877922)
     * ![](https://secure.gravatar.com/avatar/1396420428f95fc71ac03993f91ce9de85926f11f3d3826738ca7f2e88ebb01b?s=50&d=blank&r=g)
daniel
[ March 24, 2017 at 8:06 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-877919)
i’am using debian jessie as os
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-877919)
  20. ![](https://secure.gravatar.com/avatar/7edbe11365f2e71d3b42705e468e7d94414415227d37b3eca30dec3a7600a2b3?s=50&d=blank&r=g)
morteza mohammadi
[ June 6, 2016 at 5:38 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-788950)
hi guys
installed successfully now i want know what's open port needed in the zabbix server and slave server added to zabbix?
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-788950)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ June 6, 2016 at 6:23 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-788967)
Zabbix server: 10051
Zabbix-agents: 10050
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-788967)
  21. ![](https://secure.gravatar.com/avatar/97c5847b75f028de33213b165fd2fc428cbd5c2603debc65c6e035a8a1a92a6e?s=50&d=blank&r=g)
Jorge
[ April 24, 2016 at 10:11 am  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-773964)
Hy, guys.
I have the same problem, Zabbix server is running No localhost, in debian. After review again the tutorial i realize that when i edit the configuration file line “DBSocket=/var/run/mysqld/mysqld.sock” i keep the default “mysql.sock” in the end. After edit to “mysqld.sock” it works.
Txs for the tutorial.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-773964)
  22. ![](https://secure.gravatar.com/avatar/80ed01976e97119b8eda71c2fe2f7ae347c01f3258bf7db6b2d8d02cb89be89d?s=50&d=blank&r=g)
mudit
[ April 9, 2016 at 10:47 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-771558)
I am unable to locate file :: /usr/local/etc/zabbix_server.conf
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-771558)
     * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ April 11, 2016 at 12:52 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-772031)
If locate command doesn’t show you the file, update the database with the command: updatedb.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-772031)
       * ![](https://secure.gravatar.com/avatar/80ed01976e97119b8eda71c2fe2f7ae347c01f3258bf7db6b2d8d02cb89be89d?s=50&d=blank&r=g)
mudit
[ April 13, 2016 at 12:33 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-772348)
command: updatedb. this did not help me .
Still , unable to locate file :: /usr/local/etc/zabbix_server.conf
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-772348)
         * ![](https://secure.gravatar.com/avatar/f29eecc33465f4d4d08c50d4ee5bc73b9d8159264c6494e7ec50812a5db5f292?s=50&d=blank&r=g)
Matei Cezar
[ April 13, 2016 at 11:42 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-772415)
Maybe on ./configure you’ve changed the destination path for your installation.
[Reply](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-772415)
  23. ![](https://secure.gravatar.com/avatar/80ed01976e97119b8eda71c2fe2f7ae347c01f3258bf7db6b2d8d02cb89be89d?s=50&d=blank&r=g)
mudit
[ April 9, 2016 at 10:32 pm  ](https://www.tecmint.com/install-and-configure-zabbix-monitoring-on-debian-centos-rhel/#comment-771553)
When I am running command:::
