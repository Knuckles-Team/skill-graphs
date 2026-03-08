# grep -i ipv6 /etc/sysctl.conf
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
Then run sysctl -p
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-943650)
     * ![](https://secure.gravatar.com/avatar/7cd0b9d84d323917ef64ffcde4893a626f143bc3f838589daddc02139de50b5d?s=50&d=blank&r=g)
Aldo
[ November 24, 2017 at 1:12 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-939568)
Hi,
I have the same problem as you, how did you resolve this?
Thanks.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-939568)
  39. ![](https://secure.gravatar.com/avatar/3bda684365b0c67d7563ab05b318fa132aa037ce06514bf8b6b536f483f0bfce?s=50&d=blank&r=g)
Partha sarathi Dash
[ March 25, 2017 at 1:16 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-878115)
Hello Ravi,
I stuck on this command “make install-daemon-config”. It is showing the error “make: *** No rule to make target `install-daemon-config’. Stop”.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-878115)
     * ![](https://secure.gravatar.com/avatar/9646a5584212faec4cb9952414c421483fb0b4f371507cac63269e7e06dfafb1?s=50&d=blank&r=g)
Piotr
[ March 29, 2017 at 5:33 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-879578)
Check this one mate
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-879578)
  40. ![](https://secure.gravatar.com/avatar/c3cd10f4657e0b2784ab95d8939af5edd8911ec4bf0e1bd2a274a1a935ea8350?s=50&d=blank&r=g)
nirmal
[ March 8, 2017 at 10:45 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-873941)
Hi, thanks for the tutorial
let me know how to add windows host to nagios server.
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-873941)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ March 8, 2017 at 12:57 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-873978)
@Nirmal,
Here is the guide that shows [how to add Windows host to Nagios](https://www.tecmint.com/how-to-add-windows-host-to-nagios-monitoring-server/).
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-873978)
  41. ![](https://secure.gravatar.com/avatar/9690d0a55e7f648fc311bf4152e7187affe339dd8baab6801b7cdc13b4a67623?s=50&d=blank&r=g)
Mani
[ February 23, 2017 at 9:38 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-870108)
I am having the same problem. The check_nrpe file is not in the /usr/local/nagios/libexec/ directory
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-870108)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 23, 2017 at 10:18 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-870113)
@Mani,
That means your NRPE installation was not successful, try to install again and see if the nrpe plugin available from libexec directory…
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-870113)
  42. ![](https://secure.gravatar.com/avatar/a2cecc551e65cb211268c72e08739cfc3d8a07267fb40cea67f37080803ebf51?s=50&d=blank&r=g)
Satyam
[ February 17, 2017 at 7:48 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-868651)
Hi Ravi
On Nagios Monitoring Server
Not able to perform step 2
[root@tecmint]# /usr/local/nagios/libexec/check_nrpe -H
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-868651)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ February 18, 2017 at 10:25 am  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-868858)
@Satyam,
What error you getting on the screen while checking NRPE version with host?
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-868858)
       * ![](https://secure.gravatar.com/avatar/a2cecc551e65cb211268c72e08739cfc3d8a07267fb40cea67f37080803ebf51?s=50&d=blank&r=g)
Satyam
[ February 19, 2017 at 4:20 pm  ](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/comment-page-3/#comment-869272)
No such file and directory found, according to your document, it should show version of Nagios. Second question, i want to monitor **“ps -ef | grep -i gmvuser”** from remote machine, how to add entry for that in **/usr/local/nagios/etc/nrpe.cfg** file at remote server .
[Reply](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/#comment-869272)
