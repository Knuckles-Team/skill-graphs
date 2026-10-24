## Comment navigation
[← Older Comments](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-2/#comments)
  1. ![](https://secure.gravatar.com/avatar/fae52d411d699a00f877a27e0590f071b2d701a57244b7ba4a146f9c05c2cd4f?s=50&d=blank&r=g)
chandrakant
[ October 6, 2025 at 12:42 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-2348282)
I am getting this error for ./configure command
[root@localhost nagios-plugins-2.3.3]# ./configure
configure: error: working directory cannot be determined
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-2348282)
  2. ![](https://secure.gravatar.com/avatar/18943bf8e0dcfe9391643e095e1cc4b86e4b8295abeab8c509241094c14ca2ba?s=50&d=blank&r=g)
Rajan Dubey
[ January 16, 2025 at 3:26 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-2261316)
Can I add a remote server using the Nagios GUI?
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-2261316)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 17, 2025 at 10:31 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-2261690)
@Rajan,
Yes, if you’re using **Nagios XI** , it provides a user-friendly web interface that allows you to add remote servers easily.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-2261690)
  3. ![](https://secure.gravatar.com/avatar/18bc1ced02293a89e93adf26e2d3ab8b979ca60ba271438c064b0164471be306?s=50&d=blank&r=g)
Souleymane
[ February 1, 2023 at 9:58 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1955589)
I got the following error while running the `make all` command.
```
# make all

./nrpe.c:287:9: warning: ‘ENGINE_load_builtin_engines’ is deprecated:
Since OpenSSL 3.0 [-Wdeprecated-declarations]
  287 |         ENGINE_load_builtin_engines();
      |         ^~~~~~~~~~~~~~~~~~~~~~~~~~~

```

So I fixed it by using the latest version nrpe-4.1 from github:
```
$ wget https://github.com/NagiosEnterprises/nrpe/releases/download/nrpe-4.1.0/nrpe-4.1.0.tar.gz

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1955589)
  4. ![](https://secure.gravatar.com/avatar/57619c45918cfcf0aa60de111796f8837b6061f1adcc0e5b0d3a7703256f2a86?s=50&d=blank&r=g)
Naresh
[ June 15, 2022 at 7:58 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1825979)
I am getting an error that says:
“Redirecting to /bin/systemctl start nagios.service
Job for nagios.service failed because the control process exited with an error code. See “systemctl status nagios.service” and “journalctl -xe” for details.”
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1825979)
  5. ![](https://secure.gravatar.com/avatar/8b205292819d51c8328421f2d379476a89ffbb8c981d476ff36c6c473459736c?s=50&d=blank&r=g)
Bobby Johnson
[ May 14, 2021 at 7:16 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1490547)
Hello,
I am administering our NAGIOS XI server (v5.5.9) and it is working fine and monitoring LINUX hosts with a variety of LINUX OS v7.9 and lower. This is my first use of CentOS8.x node in our environment and I’m unable to get the tools installed for monitoring using the steps outlined above.
In my case, the verification in Step 8 fails —
```
[root@servername tmp]# /usr/local/nagios/libexec/check_nrpe -H localhost
CHECK_NRPE: Error - Could not connect to ::4c3a:433a:4b3a:413a: Connection reset by peer
[root@servername tmp]# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1
CHECK_NRPE: Error - Could not connect to 127.0.0.1: Connection reset by peer

```

Also, I cannot verify the Step 10 “**Customize NRPE Commands** ” file **/usr/local/nagios/etc/nrpe.cfg** because the directory **/usr/local/nagios/etc/** is not installed.
Any suggestions?
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1490547)
  6. ![](https://secure.gravatar.com/avatar/0d4384633073a55d5ab06a2cfe4a7cbc231b26560b49b030e63c3a4c3b161394?s=50&d=blank&r=g)
Pratik
[ March 16, 2021 at 4:26 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1451604)
I need help, I just want to ask you if, the Nagios, Nagios-Plugins, NRPE, and Xinetd are installed in one machine or different?
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1451604)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 17, 2021 at 10:32 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1452347)
@Partik,
Nagios is installed on the server machine, and Nagios-Plugins, NRPE, and Xinetd are installed on client machines…
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1452347)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 23, 2023 at 11:44 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1987513)
@Pratik,
You must install Nagios-Plugins, NRPE, and Xinetd on a remote Linux host that you want to monitor under the Nagios server.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1987513)
  7. ![](https://secure.gravatar.com/avatar/eb4758ddca8d80601f9beb8d4212751c589ae9627977ae61d5867ae549cda53a?s=50&d=blank&r=g)
Gautam Kumar
[ January 13, 2021 at 10:12 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1414860)
Dear Tecmit team,
Why I am getting the below error while installing **nrpe**?
```
[root@remotehost1 nrpe-nrpe-4.0.3]# make install-daemon-config
make: *** No rule to make target `install-daemon-config'.  Stop.

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1414860)
     * ![](https://secure.gravatar.com/avatar/54f217c1ea2a11b88dc33fd14e71ab32dea1ba5a993dc51cd374a1ae248d3f12?s=50&d=blank&r=g)
Tim Perkins
[ May 18, 2022 at 3:41 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1798403)
I am also getting:
```
make: *** No rule to make target `install-daemon-config'.  Stop.
```

What do we need to do to work around that?
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1798403)
       * ![](https://secure.gravatar.com/avatar/54f217c1ea2a11b88dc33fd14e71ab32dea1ba5a993dc51cd374a1ae248d3f12?s=50&d=blank&r=g)
Tim Perkins
[ May 18, 2022 at 4:30 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1798420)
Solved it, see this article:
`https://support.nagios.com/kb/article.php?id=515`
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1798420)
  8. ![](https://secure.gravatar.com/avatar/f67b2400b4c78cf4c74dd9106349ce9e2fef7e62f874f931380780b07f99ae29?s=50&d=blank&r=g)
Mushir
[ January 11, 2021 at 11:26 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1413249)
CHECK_NRPE STATE CRITICAL: Socket timeout after 10 seconds.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1413249)
  9. ![](https://secure.gravatar.com/avatar/bd842122465e8063afb661ea23e5fdb3e7b9ba6950a3d5c10275ff480bf69fb3?s=50&d=blank&r=g)
Anukool
[ December 11, 2020 at 1:41 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1399845)
Yes, `ps -ef | grep -i` is the best way to check for any process running. You can also use the [top command](https://www.tecmint.com/12-top-command-examples-in-linux/ "12 TOP Command Examples in Linux") to check the same.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1399845)
  10. ![](https://secure.gravatar.com/avatar/37e62744f87a3f4ad947044d43d14c6782ac2b0709eab69f75aba9ec54c1a2c3?s=50&d=blank&r=g)
Rachael
[ December 10, 2020 at 12:14 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1399563)
I was hoping to find a few more examples. I am trying to figure out how to check for specific processes running on my servers. For example, if I wanted to know if Firefox was running. How do you write a **command_check** to perform a `ps -ef |grep -i firefox` or something of the sort?
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1399563)
  11. ![](https://secure.gravatar.com/avatar/619d846d01af7bf061c89e6a0f7bfdd12a9635098fc7959656f86d6d90480277?s=50&d=blank&r=g)
Anuraag
[ March 6, 2020 at 11:50 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1320214)
Tried this:
```
# /usr/local/nagios/libexec/check_nrpe -H localhost

```

and getting this error:
```
connect to address ::1 port 5666: Connection refused
connect to address 127.0.0.1 port 5666: Connection refused
connect to host localhost port 5666: Connection refused

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1320214)
     * ![](https://secure.gravatar.com/avatar/c4a7ccc3867e2837c614cedd57494276a077163f1a7eb9c7890bcd5160887489?s=50&d=blank&r=g)
gopi
[ May 19, 2020 at 10:14 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1334429)
```
# chown nagios.nagios /usr/local/nagios/var

```

Enter the above command to change ownership and start the **nrpe** service.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1334429)
  12. ![](https://secure.gravatar.com/avatar/95caa66a7bcaa17a68e7d718c57e95b2b669f6de7388bef8a6c94a0c84a1a890?s=50&d=blank&r=g)
yss
[ February 19, 2020 at 12:03 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1317608)
Do we have to restart nagios every time after we added a new host?
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1317608)
  13. ![](https://secure.gravatar.com/avatar/80ecadabc890a64ef896a6ceb7c7ecc7b00cc43f920ff75d4b0d3f0eb63da5a7?s=50&d=blank&r=g)
Amar
[ November 22, 2019 at 6:16 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1293805)
```
# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1
NRPE v3.2.1

```
```
# /usr/local/nagios/libexec/check_nrpe -H 18.224.246.251
CHECK_NRPE: Error - Could not connect to 18.224.246.251: Connection reset by peer

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1293805)
  14. ![](https://secure.gravatar.com/avatar/19fa3a5838365be80c46214566fdbb0edc33eb506a1df1adda80ee6e92845b2e?s=50&d=blank&r=g)
Atul jaiswal
[ October 13, 2019 at 4:58 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1267925)
Hi,
Good work but some errors while configuring the remote host.
1) While installing nrpe the command given as shown below:
```
[root@tecmint nagios]# tar xzf nrpe-3.2.1.tar.gz
[root@tecmint nrpe-3.2]# cd nrpe-3.2

```

I think it should be `cd nrpe-3.2.1`.
2) I am getting an error while executing the below command.
```
[root@tecmint nrpe-3.2]# make install-daemon-config
[root@localhost nrpe-3.2.1]# make install-daemon-config
make: *** No rule to make target `install-daemon-config'.  Stop.

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1267925)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 14, 2019 at 10:39 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1268349)
@Atul,
Yes, it should be `cd nrpe-3.2.1` and I have corrected it in the article.
The error you get is because you have missed installing the required dependencies.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1268349)
       * ![](https://secure.gravatar.com/avatar/19fa3a5838365be80c46214566fdbb0edc33eb506a1df1adda80ee6e92845b2e?s=50&d=blank&r=g)
Atul jaiswal
[ October 14, 2019 at 10:52 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1268355)
Which command or which dependency can you please give me that command?
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1268355)
       * ![](https://secure.gravatar.com/avatar/eb4758ddca8d80601f9beb8d4212751c589ae9627977ae61d5867ae549cda53a?s=50&d=blank&r=g)
Gautam Kumar
[ January 13, 2021 at 10:18 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1414863)
I am also getting the same error please explain which dependencies I am missing.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1414863)
  15. ![](https://secure.gravatar.com/avatar/80ecadabc890a64ef896a6ceb7c7ecc7b00cc43f920ff75d4b0d3f0eb63da5a7?s=50&d=blank&r=g)
amar
[ September 13, 2019 at 12:47 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1243202)
Hi, This error is coming while I am restarting the **Nagios** service for email configuration.
```
[root@india objects]# service nagios restart

```

**Sample Output** :
```
Running configuration check...
Nagios Core 4.4.3
Copyright (c) 2009-present Nagios Core Development Team and Community Contributors
Copyright (c) 1999-2009 Ethan Galstad
Last Modified: 2019-01-15
License: GPL

Website: https://www.nagios.org
Reading configuration data...
   Read main config file okay...
Error: Template 'linux-server' specified in host definition could not be not found (config file '/usr/local/nagios/etc/objects/localhost.cfg', starting on line 21)
Error: Service notification period '24×7' specified for contact 'nagiosadmin' is not defined anywhere!
Error: Could not register contact (config file '/usr/local/nagios/etc/objects/contacts.cfg', starting on line 27)
   Error processing object config files!


***> One or more problems was encountered while processing the config files...

     Check your configuration file(s) to ensure that they contain valid
     directives and data definitions.  If you are upgrading from a previous
     version of Nagios, you should be aware that some variables/definitions
     may have been removed or modified in this version.  Make sure to read
     the HTML documentation regarding the config files, as well as the
     'Whats New' section to find out what has changed.
```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1243202)
  16. ![](https://secure.gravatar.com/avatar/3196f83af6efb9a1a5f302aa8b06991b67cf120b18770e3f09d61662e5e7401c?s=50&d=blank&r=g)
buddy
[ September 11, 2019 at 1:22 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1241870)
I want to know the meaning of this nagios status information as I am new to the Linux platform.
HTTP WARNING: HTTP/1.1 404 – 1234 bytes in 0.004 second response time.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1241870)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ September 12, 2019 at 10:36 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1242555)
@Buddy,
The **404** error means the page is not found, it means your **Apache** is running but the requested page is not found…
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1242555)
  17. ![](https://secure.gravatar.com/avatar/fbf11d538d3a9d7a4225bedda9803b57e3e3a5a7b4ba869ab60cd99bb8254caa?s=50&d=blank&r=g)
David B
[ May 13, 2019 at 11:24 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1151416)
What if I am installing a third server? How do I apply the service file I append the same info to the bottom and change the hostname to a new host but the Nagios monitor displays unknown services (**NRPE: Unable to read output**) for the service. The host was added fine.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1151416)
     * ![](https://secure.gravatar.com/avatar/fc65c42059b78d458c5a260100238de4bda1677a8ad6784746860748a1eb4ca3?s=50&d=blank&r=g)
Shyja SL
[ May 14, 2019 at 2:00 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1151941)
Hi David,
Try restarting **NRPE** on remote client after the config changes:
```
Command : /etc/init.d/nrpe restart (similar command)

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1151941)
  18. ![](https://secure.gravatar.com/avatar/fc65c42059b78d458c5a260100238de4bda1677a8ad6784746860748a1eb4ca3?s=50&d=blank&r=g)
Shyja SL
[ May 1, 2019 at 3:11 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1143980)
Hi,
I have installed **nagioscore-4.4.1** , **nagios-plugins-2.2.1** & **nrpe-3.0.1** on my machine. **Nagios Server** is **CentOS** and Remote host is **Suse Linux**.
I am getting error ‘**CHECK_NRPE: Error – Could not connect to 10.211.7.5: Connection reset by peer** ‘
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1143980)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 2, 2019 at 10:57 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1144453)
@Shayja,
Does it work with the localhost IP address (127.0.0.1)? If yes, might you need to disable IPv6 support? Another solution is, to search for the following line in **/etc/xinetd.d/nrpe** file.
```
"disable = yes"

```

and simply change it to “**no** “, then:
```
"disable = no"

```

Restart the service.
```
# systemctl restart xinetd.service
# systemctl restart nrpe or # service nrpe restart (if not systemd)

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1144453)
       * ![](https://secure.gravatar.com/avatar/fc65c42059b78d458c5a260100238de4bda1677a8ad6784746860748a1eb4ca3?s=50&d=blank&r=g)
Shyja SL
[ May 2, 2019 at 11:48 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1144481)
Hi @Ravi Saive,
Thanks for your reply. After the change, I am getting the below error in Nagios Server.
```
Output from Remote Client
bhmlxab:/etc/rc.d # /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1
NRPE v3.0.1

```

Output from Nagios Server.
```
[root@YLASP150 objects]# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1
CHECK_NRPE: Receive header underflow - only -1 bytes received (4 expected).

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1144481)
  19. ![](https://secure.gravatar.com/avatar/70f9b42ca9cc061171c15df7cd161fbcd6100c0c41c498522ff31a2e2bd16d7d?s=50&d=blank&r=g)
ashokkumar
[ March 29, 2019 at 9:08 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1121534)
How to add the host IP address and users in the nagios server?
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1121534)
  20. ![](https://secure.gravatar.com/avatar/861ee365b2b77903a9d0dec40c6e14c1f14b0352044cbdff35e90a85a1fba89f?s=50&d=blank&r=g)
Jagadeesh
[ March 26, 2019 at 5:33 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1118482)
As I mentioned in my previous comment…
```
connect to address ::1 port 5666: Connection refused
connect to address 127.0.0.1 port 5666: Connection refused
connect to host localhost port 5666: Connection refused

```

I followed two methods.
**1.** I tried to open port for 5666 in iptables
**2.** I disabled iptables and tried for some time.
but am getting the same issues…
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1118482)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 27, 2019 at 11:02 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1119178)
@Jagadeesh,
First, verify that the port **5666** is running using the following command.
```
# netstat -at | grep nrpe

```

If not, you should check your **NRPE** installation…
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1119178)
  21. ![](https://secure.gravatar.com/avatar/861ee365b2b77903a9d0dec40c6e14c1f14b0352044cbdff35e90a85a1fba89f?s=50&d=blank&r=g)
Jagadeesh
[ March 26, 2019 at 1:46 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1118061)
I still get the same error:
```
connect to address ::1 port 5666: Connection refused
connect to address 127.0.0.1 port 5666: Connection refused
connect to host localhost port 5666: Connection refused

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1118061)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 26, 2019 at 10:38 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1118295)
@Jagadeesh,
Please open the Nagios NRPE Port 5666 on the firewall to allow connection from remote machines…
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1118295)
       * ![](https://secure.gravatar.com/avatar/861ee365b2b77903a9d0dec40c6e14c1f14b0352044cbdff35e90a85a1fba89f?s=50&d=blank&r=g)
Jagadeesh
[ March 26, 2019 at 12:37 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1118344)
I tried two things.
**1.** I tried to open port for 5666 in iptables
**2.** I disabled iptables and tried for some time.
I tried both but am getting the same issues.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1118344)
         * ![](https://secure.gravatar.com/avatar/861ee365b2b77903a9d0dec40c6e14c1f14b0352044cbdff35e90a85a1fba89f?s=50&d=blank&r=g)
Jagadeesh
[ March 26, 2019 at 1:26 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1118372)
This tutorial is very very confusing because which part will do on the server and which will be done on the remote machine is not clear.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1118372)
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 26, 2019 at 2:21 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1118392)
@Jagadeesh,
If you know how Nagios works, you should clearly understand how these instructions work…
  22. ![](https://secure.gravatar.com/avatar/861ee365b2b77903a9d0dec40c6e14c1f14b0352044cbdff35e90a85a1fba89f?s=50&d=blank&r=g)
Jagadeesh
[ March 26, 2019 at 12:39 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1118030)
I can’t install **xinted** in centos 6.10. Please anyone tell me.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1118030)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 26, 2019 at 10:40 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1118297)
@Jagadeesh,
It’s easy, just run the following command to install **Xinetd** on **CentOS** or **Fedora**.
```
# yum install xinetd

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1118297)
  23. ![](https://secure.gravatar.com/avatar/0fafba14650800be7e6a32a677d9c111abe27cb3bfeb25796d36bf53ec623d96?s=50&d=blank&r=g)
Andi
[ December 12, 2018 at 3:50 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1082764)
I am getting the following error while compiling Nagios:
```
make: *** No rule to make target `install-daemon-config'.  Stop.

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1082764)
  24. ![](https://secure.gravatar.com/avatar/90085c13af655a8bbbcada5773972653cf860382a10eeb06d7f03554fccf1929?s=50&d=blank&r=g)
vishal
[ December 5, 2018 at 2:40 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1079539)
Getting this error, Kindly let me know what is the issue.
```
/extinterface/southern_region/chpt/citpl/02/received/csv/: Does not exist

```

I have checked the permission and member of nagios user of port user
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1079539)
  25. ![](https://secure.gravatar.com/avatar/c1fc39972de75e67acaf312dc703a6cf7c941f4b3f3598df9be175a40c88beb9?s=50&d=blank&r=g)
sabir
[ November 1, 2018 at 2:10 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1054781)
Hi bro, I added multiple Linux servers to Nagios server but all added server showing same `"/"` partition sizes and swap sizes, my partitions are created with LVM in all configuration files i modified “**Hostname, alias, IPaddress** “, is there any modifications i have to do?
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1054781)
  26. ![](https://secure.gravatar.com/avatar/1f06f9101702c4d07374c46b7b087c2f86f05e7586a22a238e705be02523c775?s=50&d=blank&r=g)
MS Zaid
[ August 9, 2018 at 12:23 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1022293)
How to remove the nrpe 3.2.1 setup from scratch in the client machine?
I want to remove all the files & folders related nrpe and want make a fresh start. Assist me in it
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1022293)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 9, 2018 at 4:23 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1022328)
@Zaid,
Use [find command](https://www.tecmint.com/35-practical-examples-of-linux-find-command/) to locate all NRPE relate files and delete them..
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1022328)
  27. ![](https://secure.gravatar.com/avatar/1f06f9101702c4d07374c46b7b087c2f86f05e7586a22a238e705be02523c775?s=50&d=blank&r=g)
MS Zaid
[ August 9, 2018 at 12:16 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1022292)
[root@tlaserver21 nrpe-3.2.1]# /usr/local/nagios/libexec/check_nrpe -H localhost
CHECK_NRPE: Error – Could not connect to ::1c00:0:ffff:ffff: Connection reset by peer
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1022292)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 9, 2018 at 4:26 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1022329)
@Zaid,
Please enable IPv6 in networking and also open NRPE port on Firewall..
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1022329)
  28. ![](https://secure.gravatar.com/avatar/1f06f9101702c4d07374c46b7b087c2f86f05e7586a22a238e705be02523c775?s=50&d=blank&r=g)
MS Zaid
[ August 8, 2018 at 10:59 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1021918)
```
[root@server1 nagios]# wget http://liquidtelecom.dl.sourceforge.net/project/nagios/nrpe-3.x/nrpe-3.0.tar.gz

```

##### Sample Output
```
--2018-07-24 12:15:14--  http://liquidtelecom.dl.sourceforge.net/project/nagios/nrpe-3.x/nrpe-3.0.tar.gz
Resolving liquidtelecom.dl.sourceforge.net... 197.155.77.8
Connecting to liquidtelecom.dl.sourceforge.net|197.155.77.8|:80... connected.
HTTP request sent, awaiting response... 302 Found
Location: http://downloads.sourceforge.net/project/nagios/nrpe-3.x/nrpe-3.0.tar.gz
--2018-07-24 12:15:16--  http://downloads.sourceforge.net/project/nagios/nrpe-3.x/nrpe-3.0.tar.gz
Resolving downloads.sourceforge.net... 216.105.38.13
Connecting to downloads.sourceforge.net|216.105.38.13|:80... connected.
HTTP request sent, awaiting response... 404 Not Found
2018-07-24 12:15:18 ERROR 404: Not Found.

```

can you please update the url of nrpe 3.0 plugin.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1021918)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ August 8, 2018 at 12:58 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1021951)
@Mszaid,
Thanks for pointing out, I’ve updated the URL of NRPE to latest version i.e 3.2.1.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-1021951)
  29. ![](https://secure.gravatar.com/avatar/eb71b9572b2afab1f1dd978836cedb0ac817828a2c19560f305d578335201164?s=50&d=blank&r=g)
rasmita
[ May 3, 2018 at 3:22 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-988963)
make: *** No rule to make target `**install-daemon-config** ‘. Stop.
You have new mail in /var/spool/mail/root
[root@nrpe-3.0]# make install-xinetd
make: *** No rule to make target `install-xinetd’. Stop.
[root@cloud86 nrpe-3.0]# make install-inetd
No inetd file to install
make: *** [install-
getting above error
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-988963)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 3, 2018 at 4:04 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-988973)
@Rasmita,
Please install all needed packages for Nagios to compile as shown.
```
# yum install -y gcc glibc glibc-common gd gd-devel make net-snmp openssl-devel xinetd

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-988973)
       * ![](https://secure.gravatar.com/avatar/de7101f8ce1bcc592eb35a19acfb871f3454efa9eaf664bf760e863d585c767a?s=50&d=blank&r=g)
Muabarak Ali Mohd Mustafa
[ May 8, 2018 at 7:02 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-990472)
every package is installed and latest but still the same issue
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-990472)
         * ![](https://secure.gravatar.com/avatar/bf1dfae865a1dd29f92396600e4c3c77515814529e3f0f2f4c607651df420b23?s=50&d=blank&r=g)
Jahal_Postaria
[ May 30, 2018 at 5:40 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-999131)
same error as received by mubarak. All the package is installed and latest
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-999131)
           * ![](https://secure.gravatar.com/avatar/f6adf09a28bd00cce7dc6a4d1cf6b154385e826662e4bfa0c3345254ab27f2bd?s=50&d=blank&r=g)
Marcus
[ October 14, 2018 at 1:44 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-1047783)
Same issue here. There appears to be a missing step in the instructions. I’ve validated that all the listed packages are installed–my guess is that there is a package missing, and it is not listed in these instructions.
  30. ![](https://secure.gravatar.com/avatar/3bda684365b0c67d7563ab05b318fa132aa037ce06514bf8b6b536f483f0bfce?s=50&d=blank&r=g)
Partha Sarathi Dash
[ May 1, 2018 at 12:34 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-988351)
I downloaded nrpe plugin tarball on nagios server and extracted it in **/root/nagios/**. Now when I am going inside that directory and running `./configure` it is giving me these error. Can any one help me!!!
```
checking for Kerberos include files... configure: WARNING: could not find include files
checking for pkg-config... pkg-config
checking for SSL headers... configure: error: Cannot find ssl headers

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-988351)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 2, 2018 at 10:29 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-988597)
@Partha,
Please first install required libraries on your Linux distribution you are using.
```
[root@tecmint]# yum install -y gcc glibc glibc-common gd gd-devel make net-snmp openssl-devel

```
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-988597)
  31. ![](https://secure.gravatar.com/avatar/0b2746364efd2cbeaaa005448f65c76ab042847767a8cefd87e3c34b227f716c?s=50&d=blank&r=g)
Ravat Tailor
[ April 27, 2018 at 2:12 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-987247)
Hi, How can I provide remote server port in **host.cfg** file.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-987247)
  32. ![](https://secure.gravatar.com/avatar/43ddd298449f8f68c9d4c0eab1145fd0cd7327fd34c76962aef399049830d9d8?s=50&d=blank&r=g)
ajay
[ April 25, 2018 at 7:48 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-986558)
```
$ sudo yum install gcc glibc glibc-common gd gd-devel make net-snmp openssl-devel xinetd unzip

```

this command shows:
```
Loaded plugins: product-id, refresh-packagekit, subscription-manager
Updating Red Hat repositories.
Setting up Install Process
No package gd available.
No package gd-devel available.
No package openssl-devel available.
Nothing to do

```

what it means?
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-986558)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 26, 2018 at 11:33 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-986807)
@Ajay,
You need to [enable Red Hat subscription](https://www.tecmint.com/enable-redhat-subscription-reposiories-and-updates-for-rhel-7/) to make use of their repositories to install software packages.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-986807)
  33. ![](https://secure.gravatar.com/avatar/6400b63bcee6d283c98b300ec16fb7868fd95576b549cf82ff48e78dfc327168?s=50&d=blank&r=g)
Henrich
[ April 2, 2018 at 2:19 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-979611)
Good day,
I am stuck at extracting the file **tar -xvf nagios-plugins-2.1.2.tar.gz** , it only says
```
gzip: stdin: not in gzip format
tar: Child not returned status 1
tar: Error is not recoverable: exiting now

```

I already installed unzip, gzip and tar. Do you have any ideas on how to solve this?
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-979611)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 3, 2018 at 12:08 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-979749)
@Henrich,
It seems your download tar archive is corrupted or damaged during download, try to download new copy tar archive file and then extract it again..
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-979749)
       * ![](https://secure.gravatar.com/avatar/7a67eb2069ad4638bddaf2118dffce8ce60a436256e8a74373401a3fe04a799b?s=50&d=blank&r=g)
Henrich
[ April 5, 2018 at 9:50 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-980146)
@Ravi,
Thanks a lot bro, I remove the file and download again. It works
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-980146)
  34. ![](https://secure.gravatar.com/avatar/9290d177c795a77ceb5d532f14d5032c7cb8db5996a16edead15b0737031bb56?s=50&d=blank&r=g)
Nitish Joshi
[ March 30, 2018 at 4:52 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-978971)
Hi Ravi,
A very basic question!!!
I have installed Nagios on an EC2 instance and its up and running. But now when I try to access
I have configured port 80 for inbound rules in the security group still I am unable to access the web-interface.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-978971)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ April 3, 2018 at 12:26 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-979755)
@Nitish,
Does
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-979755)
  35. ![](https://secure.gravatar.com/avatar/205a2553bd07e041addb60e14b80309fbec0a38f89767e793f8888b0169fd4a4?s=50&d=blank&r=g)
Nath
[ March 29, 2018 at 4:40 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-978763)
Hi Guys,
I am new for Nagios i need document to install Nagios and Monitoring for linux and windows servers in Nagios.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-978763)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 30, 2018 at 10:11 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-978919)
@Nath,
Please follow the [Nagios installation guide](https://www.tecmint.com/install-nagios-in-linux/).
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-978919)
  36. ![](https://secure.gravatar.com/avatar/10d0d8fb9105f840a757ae6060484587a7e8d6d84e22ab9a508a2b145239c569?s=50&d=blank&r=g)
Jyotsna
[ November 15, 2017 at 4:59 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-935727)
Hi Ravi,
I see two sets of configuration files, one set in **/usr/local/nagios/etc** and another in **/etc/nagios/**.
Which one of them is picked? Am trying to add hostgroups to nagios but its not picking up the hosts information.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-935727)
  37. ![](https://secure.gravatar.com/avatar/5c9dc1621dfbea9e3ac9c62bbbfd4a5e89b261c8362862cdfbf0aad4c8144206?s=50&d=blank&r=g)
Dilip Kumar
[ July 4, 2017 at 8:48 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-898174)
nrpe tcp/5666 #nrpe : Hash is Missing
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-898174)
  38. ![](https://secure.gravatar.com/avatar/9646a5584212faec4cb9952414c421483fb0b4f371507cac63269e7e06dfafb1?s=50&d=blank&r=g)
Piotr
[ March 29, 2017 at 4:21 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-879547)
Hi Ravi,
I have the same problem as Partha:
[root@host nrpe-3.0]# make install-plugin
cd ./src/; make install-plugin
make[1]: Entering directory `/root/nagios/nrpe-3.0/src’
/usr/bin/install -c -m 755 -d /usr/local/nagios/bin
/usr/bin/install -c -m 755 ../uninstall /usr/local/nagios/bin/nrpe-uninstall
/usr/bin/install -c -m 775 -o nagios -g nagios -d /usr/local/nagios/libexec
/usr/bin/install -c -m 775 -o nagios -g nagios -d /usr/local/nagios/libexec
/usr/bin/install -c -m 775 -o nagios -g nagios check_nrpe /usr/local/nagios/libexec
make[1]: Leaving directory `/root/nagios/nrpe-3.0/src’
[root@host nrpe-3.0]# make install-daemon
cd ./src/; make install-daemon
make[1]: Entering directory `/root/nagios/nrpe-3.0/src’
/usr/bin/install -c -m 755 -d /usr/local/nagios/bin
/usr/bin/install -c -m 755 ../uninstall /usr/local/nagios/bin/nrpe-uninstall
/usr/bin/install -c -m 755 nrpe /usr/local/nagios/bin
/usr/bin/install -c -m 755 -o nagios -g nagios -d /usr/local/nagios/var
/usr/bin/install -c -m 644 ../startup/tmpfile.conf /usr/lib/tmpfiles.d/nrpe.conf
make[1]: Leaving directory `/root/nagios/nrpe-3.0/src’
#I guess problem starts here#
[root@host nrpe-3.0]# make install-daemon-config
make: *** No rule to make target `install-daemon-config’. Stop.
[root@host nrpe-3.0]# make install-xinetd
make: *** No rule to make target `install-xinetd’. Stop.
[root@host nrpe-3.0]# make install-inetd
/usr/bin/install -c -m 644 startup/default-xinetd /etc/xinetd.d/nrpe
***** MAKE SURE ‘nrpe 5666/tcp’ IS IN YOUR /etc/services FILE
Would appreciate your advice.
Regards,
Piotr
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-879547)
     * ![](https://secure.gravatar.com/avatar/9646a5584212faec4cb9952414c421483fb0b4f371507cac63269e7e06dfafb1?s=50&d=blank&r=g)
Piotr
[ March 29, 2017 at 5:33 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-879577)
Hi there,
Used these instructions to setup NRPE and it KIND OF worked:

I mean I got it running but now stumbled upon another problem and cannot find any solution anywhere.
———————
[root@host init.d]# /usr/local/nagios/libexec/check_nrpe -H localhost
CHECK_NRPE: Error – Could not connect to ::3668:6c6e:7556:0: Connection reset by peer
[root@host init.d]# /usr/local/nagios/libexec/check_nrpe -H localhost -c check_load
CHECK_NRPE: Error – Could not connect to ::3668:6c6e:7556:0: Connection reset by peer
————————
HELP!
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-879577)
       * ![](https://secure.gravatar.com/avatar/fcd7c42ef4bb1b7bce9736fe106349b8398f9579d421f0d7fc2f7f1063c26836?s=50&d=blank&r=g)
Debojyoti Bose
[ December 3, 2017 at 12:14 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-943650)
1) /usr/local/nagios/etc/nrpe.cfg must be present
2)grep -i disable /etc/xinetd.d/nrpe
disable = no
3)If you don’t need IPv6 try disabling it in /etc/sysctl.conf
