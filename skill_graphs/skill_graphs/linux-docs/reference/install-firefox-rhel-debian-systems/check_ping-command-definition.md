# ‘check_ping’ command definition
define command{
command_name check_ssh_ping
command_line /usr/local/nagios/libexec/check_by_ssh -H $HOSTADDRESS$ -C “/usr/local/nagios/libexec/check_ping -H $HOSTADDRESS$ -w 100.0,80% -c 150.0,100% -p 5”
}
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-284184)
  39. ![](https://secure.gravatar.com/avatar/9bdb8a070207c7a01d4b252066d8b529345a859f76afb69743cf97621312971c?s=50&d=blank&r=g)
Ramesh
[ September 19, 2014 at 6:55 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-278226)
Great! i have not get any problem to follow this instruction.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-278226)
  40. ![](https://secure.gravatar.com/avatar/5c144b2289f3648378b6e17cee80f0a479b6e247c08087e626081a7fa07d6799?s=50&d=blank&r=g)
Krishna Mohan
[ July 24, 2014 at 5:45 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-222700)
Hi Ravi,
I have a one question. i have installed nrpe client in one linux sever and have monitoring service and server in the host server..
Now i need to install a new pulgin in client machine it is not available on the below mentioned location. an you please tell me the steps how to install a new pulgin in the client machine.
/usr/local/nagios/libexec in this location.
Thanks in advance.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-222700)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 25, 2014 at 1:23 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-223327)
This means your client plugin installation was unsuccessful. Please try to follow instructions carefully.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-223327)
       * ![](https://secure.gravatar.com/avatar/5c144b2289f3648378b6e17cee80f0a479b6e247c08087e626081a7fa07d6799?s=50&d=blank&r=g)
Krishna Mohan
[ July 28, 2014 at 11:32 am  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-225838)
Thanks for reply. I have installed client pulgin,it was installed successfully i am able to monitor .But i need to monitor a new service like file utilisation of the client in host. For that we dont have a perdefined plugin so i have download a plugin from the google.. how to install nee service plugin.
Thanks in advance.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-225838)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 28, 2014 at 8:48 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-226168)
Why you need a additional plugin, just use default check_disk plugin to achieve this.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-226168)
  41. ![](https://secure.gravatar.com/avatar/1ac1f38abd37f991e61dffb1d299b5de09889a090d05bfa99c7569189e9a43cc?s=50&d=blank&r=g)
Vishal Wadkar
[ July 18, 2014 at 12:12 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-217106)
Hi,
Ravi gr8 Artical but After installing nagios and opening web page I get below error when clicking any of the tab in homepage of nagios core
Internal Server Error
The server encountered an internal error or misconfiguration and was unable to complete your request.
Please contact the server administrator, root@localhost and inform them of the time the error occurred, and anything you might have done that may have caused the error.
More information about this error may be available in the server error log.
Apache/2.2.15 (CentOS) Server at 10.7.70.196 Port 80
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-217106)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 21, 2014 at 5:47 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-219751)
It seems that your nagios configuration is incorrect. You should check your error logs for the problem. Another problem is, may be your SELinux is enabled, If yes, just run the following command to grant permission on the nagios folder.
```
# chcon -R -t httpd_sys_content_t /usr/local/nagios

```
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-219751)
  42. ![](https://secure.gravatar.com/avatar/eb36ffcc2ecdf247b0f7af4a555db32c7b44921a25eefc4c8e445b3b41e208bd?s=50&d=blank&r=g)
Jonathan Baird
[ June 25, 2014 at 5:51 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-200578)
Hi,
Could you please help me with changing the port on a remote Windows host? I need to monitor 8 remote hosts at one particular site, so I need to come in on different ports to access the 8 machines. Is there a way to change the port the NSClient listens on from 12489? I have added “port – 12490” and restarted all the services etc but this doesn’t seem to work.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-200578)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 26, 2014 at 12:33 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-201095)
You can change the NSClient++ port by editing the NSC.ini file and change port number from 12489 to 12490 and restart the NSClient++ service. And also at Nagios server commmads.cfg file, make changes as shown.
```
check_nt -p 12489 argument in /usr/local/nagios/etc/objects/commands.cfg

```
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-201095)
  43. ![](https://secure.gravatar.com/avatar/e4e4d23aef658e90de661a7a831b7f883b1bb52e7c463431737ab9dfd3872dda?s=50&d=blank&r=g)
sanyog
[ June 20, 2014 at 12:21 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-196576)
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg , i try the following command it reply /usr/local/nagios/bin/nagios no such files or directory . so i manually create directory even it replay same msg.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-196576)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 20, 2014 at 3:48 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-196693)
It seems your installation is incomplete, please follow the instructions correctly
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-196693)
  44. ![](https://secure.gravatar.com/avatar/4ed4d41c7c5614adad222d21d7b43262e2948d5b638b0c6271a787ab5a01e773?s=50&d=blank&r=g)
Kevin Vu
[ May 28, 2014 at 2:49 am  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-177974)
Hello Ravi Saive,
Can you help me to unlock the Nagios password?
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-177974)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ May 28, 2014 at 4:06 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-178443)
Please run the following command to reset/unlock Nagios password.
```
# htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin

```
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-178443)
  45. ![](https://secure.gravatar.com/avatar/0b9f6dbafc49e7a95641414cb00f76f2fbf2ddccf956832f59f3871d5cb71e75?s=50&d=blank&r=g)
Arun
[ March 25, 2014 at 3:06 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-141558)
HI
I need monitor Windows log file and a parse a particular word from there. My Nagios in CentOS 6. Based on that parsed word, have to show the server is on/off in Nagios dashboard. Can you please help on that ?
Thanks
Arun
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-141558)
  46. ![](https://secure.gravatar.com/avatar/f77a3fa84f5eb31b9b70b3a2e0cf32c2dff2e9722c612f5b5070bc8ad31ab13c?s=50&d=blank&r=g)
Ashish
[ March 20, 2014 at 3:10 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-139089)
Hi Ravi,
Please guide how can we add multiple windows or Linux Host in Nagios Server.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-139089)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 20, 2014 at 5:02 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-139141)
I will write a detailed article on how to add Linux and Windows hosts to Nagios Server in my upcoming article.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-139141)
       * ![](https://secure.gravatar.com/avatar/ccc08a2630768bed56e12a443d73672aeabcea279cdd1307085640ed0373348b?s=50&d=blank&r=g)
Steve
[ January 20, 2015 at 7:40 am  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-457444)
Hi Ravi,
I note yet see your new article about ” how to add Linux and Windows hosts to Nagios Server” Could you help share link in comment, please?
Thanks in advance!
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-457444)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 20, 2015 at 11:15 am  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-457615)
@Steve,
At the bottom of the this article, you will find links to how to add Linux and Windows host to Nagios monitoring server.
<https://www.tecmint.com/install-nagios-in-linux/>
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-457615)
  47. ![](https://secure.gravatar.com/avatar/a59260fda83e4106e89a878fd08a56b3e6c7186ac0b9a8e94f8262e4604693c2?s=50&d=blank&r=g)
chandu
[ March 18, 2014 at 1:03 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-138085)
Hello every one
i have installed the nagios but mail notification is not working. and how add the second machine in the server.
i have added …
vi /usr/local/nagios/etc/objects/windows.cfg using by the command…
define host{
use windows-server ; Inherit default values from a Windows server template (make sure you keep this line!)
host_name winserver
alias My Windows Server
address 192.168.50.01 192.168.50.10
}
but its not showing second one …
please help me about the issue !
Thanks
chandoo
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-138085)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 18, 2014 at 2:28 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-138118)
Please install SMTP services on your Linux system to get email notifications about Nagios.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-138118)
       * ![](https://secure.gravatar.com/avatar/f77a3fa84f5eb31b9b70b3a2e0cf32c2dff2e9722c612f5b5070bc8ad31ab13c?s=50&d=blank&r=g)
Ashish
[ March 20, 2014 at 3:12 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-139091)
how add the second machine in the server
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-139091)
  48. ![](https://secure.gravatar.com/avatar/47845e86d86b22ad222de33753d0ac076b803ba811c726fbd03eb29d2833a725?s=50&d=blank&r=g)
subbu
[ February 13, 2014 at 7:39 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-122340)
Hello,
My nagios server is publicly accessible on the internet. and I would like to monitor windows hosts which are in private network ex: 192.168.0.0. In such cases what is the better solution.
Please Help me.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-122340)
  49. ![](https://secure.gravatar.com/avatar/3961c3d80affc2310005d75ddd23665d512f01c87603cdb776a089db306c6b77?s=50&d=blank&r=g)
Madura
[ February 7, 2014 at 9:06 am  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-120063)
Hello,
I followed your instructions and set Nagios to monitor one of my Windows machine, it works great. So thank you so…much. My problem is when I try to monitor a another windows machine, it does not work.
These are the steps I followed,
1) Created a new .CFG file called newhost.cfg and added the details related to that machine.
2) Edited the nagios.cfg file to append the newhost.cfg file.
3) Installed NSClient++ and did the necessary configurations.
But finally i’m getting this error when I try to restart the nagios service.
Running configuration check… CONFIG ERROR! Restart aborted. Check your Nagios configuration.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-120063)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 7, 2014 at 10:37 am  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-120102)
May be some configuration problem, will try at my end and update you..
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-120102)
  50. ![](https://secure.gravatar.com/avatar/d174f0d2d649ab30e2bf40ac1581d30ca40f7ae1e9743af145fa42159ed351e9?s=50&d=blank&r=g)
sk
[ February 4, 2014 at 6:32 am  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-118598)
Hi Ravi, after adding Windows host in Nagios server getting CRITICAL – Socket timeout after 20 seconds error for all services expect ping, need your help in solving this issue.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-118598)
  51. ![](https://secure.gravatar.com/avatar/50a64d0130bd225bfffb5d2e603e8b24fb9c6d3c61b0681ca3c334ced47cd999?s=50&d=blank&r=g)
Oded Gold
[ February 3, 2014 at 12:31 am  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-117727)
Hi
These instructions are great but when I tried to install the NSClient++ from the download link on a virtual machine I get the following error message
“The installation is not supported by this processor type”
Does anyone have a solution for this?
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-117727)
  52. ![](https://secure.gravatar.com/avatar/15d55ef615cb079ef8a33ee0528f37b7f5bc4227ee81af7fb25d396a11d89edc?s=50&d=blank&r=g)
hung
[ January 23, 2014 at 7:30 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-111684)
what if i want to add another windows host for monitoring?thanks
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-111684)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ January 24, 2014 at 3:14 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-112222)
Just add the host entry in hosts file and define their services in services.cfg file.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-112222)
       * ![](https://secure.gravatar.com/avatar/15d55ef615cb079ef8a33ee0528f37b7f5bc4227ee81af7fb25d396a11d89edc?s=50&d=blank&r=g)
hung
[ January 25, 2014 at 7:58 am  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-112631)
excuse me! please give me more details.
where are the hosts file and the services.cfg?
and how to add one more host
thanks i really appriciate
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-112631)
  53. ![](https://secure.gravatar.com/avatar/25c4d36d7d155381576a0f7f770d5a67444d3450e02f24b58b6ba6c844252129?s=50&d=blank&r=g)
Sarith
[ December 13, 2013 at 7:56 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-84965)
Hi ..
After I downloaded NSCP-0.4.1.73-x64 and setup it require ip of nagios server and password but I don’t understand about pasword .What is password ? ANd I also get error : “NSClient – ERROR: Invalid password” . Can you help me ?
Thanks
Sarith
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-84965)
     * ![](https://secure.gravatar.com/avatar/587917ba8a2f1233fc292793d3c4e39c5b45d2253fec34e667b9ea5f39f76e3c?s=50&d=blank&r=g)
Gerard
[ December 18, 2013 at 2:20 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-87430)
Hello, I’m having issues also with this “Invalid password” when the password is correct but still this error occur.
Is there any working NSClient you can give?
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-87430)
       * ![](https://secure.gravatar.com/avatar/16cd445bad41853fc58ec43b2741b193f53f2297a412323cda45ffdc987c6083?s=50&d=blank&r=g)
sandeep suman
[ February 22, 2014 at 2:38 am  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-124961)
hi sir, i am also getting the same problem of invalid password when i try to see added host on my nagios server…… its a serious problem. all passwords are correct but still a problem..
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-124961)
         * ![](https://secure.gravatar.com/avatar/4ca5099fcaee53d99641ee761fd4ac8747408b5aa5620f083a6cc2d4b6283bef?s=50&d=blank&r=g)
shoheb shaikh
[ April 23, 2014 at 5:31 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-152307)
for password like error just do one thing that,
uncomment the password in NSC.ini
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-152307)
  54. ![](https://secure.gravatar.com/avatar/e7c02f2464bc0a1e0029c3f223af3864a70f28d5db0f90948f42f6daab936cc7?s=50&d=blank&r=g)
Freman
[ November 26, 2013 at 11:56 am  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-75678)
Hi Ravi,
Do you have any userful plugins to monitor windows hosts’ interfaces traffic for nagios?
I had used the check_traffic.sh tools , but it was not work well for me.
I need the one can automatically discover the interfaces and monitor those.
Any suggestion is appriciate for me.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-75678)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ November 26, 2013 at 7:57 pm  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-75799)
No idea man! but will look out for something better, give me some time.
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-75799)
  55. ![](https://secure.gravatar.com/avatar/d9c5fac132c24eddf9fefc5a939d6833d3bfe9f3704e846c4fafdf4eccf7f359?s=50&d=blank&r=g)
Nicolargo
[ November 24, 2013 at 3:39 am  ](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-74760)
You can also used the combo: Glances on the Windows host and CheckGlances on the Nagios server.
Have a look on it here:
[Reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#comment-74760)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
