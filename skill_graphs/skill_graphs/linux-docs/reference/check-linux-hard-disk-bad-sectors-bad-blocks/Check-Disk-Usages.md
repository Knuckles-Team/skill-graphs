# Check Disk Usages
 df -h| grep 'Filesystem\|da*' |grep -v tmpfs> /tmp/diskusage
 echo -e '\E[32m'"Disk Usages :" $tecreset
 cat /tmp/diskusage

# Check Disk Usages
df -h| grep ‘Filesystem\|/dev/sda*’ > /tmp/diskusage
#result:
Disk Usages :
/dev/sda2 439G 71M 417G 1% /home
i change >>
df -h| grep ‘Filesystem\|/dev’| sed ‘/tmpfs/d’ > /tmp/diskusage
#result:
Disk Usages :
/dev/root 20G 661M 18G 4% /
/dev/sda2 439G 71M 417G 1% /home
Bye Ex.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801609)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 25, 2016 at 11:19 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-802049)
@Ex_rat,
Thanks for the changes and sharing the same with us, hope it will help other Linux users..
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-802049)
  34. ![](https://secure.gravatar.com/avatar/4f2d0693690cbb324e00ec4ed125c5b33a48df416d967ff62105be1f8ed3e1d5?s=50&d=blank&r=g)
Andres Tarallo
[ July 13, 2016 at 12:30 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-798787)
Hi,
I’ve discovered your script a month ago, thanks a former colleague. I’ve executed it on SuSE Enterprise (SLES), with some failures. I’m debugging it and making capable of running on other Linux other than Ubuntu.
I want to upload the original script to GITHUB, to upload there my contributions. May I count with your blessing to do so?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-798787)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 13, 2016 at 12:48 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-798887)
@Andres,
Thanks for making the script compatible for all Linux distributions, but make sure you should give credit to Tecmint.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-798887)
       * ![](https://secure.gravatar.com/avatar/4f2d0693690cbb324e00ec4ed125c5b33a48df416d967ff62105be1f8ed3e1d5?s=50&d=blank&r=g)
Andres Tarallo
[ July 14, 2016 at 2:42 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-799047)
@Ravi,
I’ll credit Tecmint. It’s not my intention to delete the header or remove references to Tecmint.
As said before it would be nice to have your blessing to upload the original Script to GITHUB, then I’ll be uploading there my changes.
Feel free to write me a private message, the original script is great.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-799047)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 14, 2016 at 12:01 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-799126)
@Andres,
Thanks for keeping the Credit and yes our blessings always with you friend, yes you can push the script to the Github project and let me know once you done..
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-799126)
           * ![](https://secure.gravatar.com/avatar/4245267a689b24710ef0bed6e29322f98e199ce02654eb1fd447f33e5d4febc7?s=50&d=blank&r=g)
Alji Mohamed
[ July 14, 2016 at 1:34 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-799153)
Let me know that too, thank you
           * ![](https://secure.gravatar.com/avatar/4f2d0693690cbb324e00ec4ed125c5b33a48df416d967ff62105be1f8ed3e1d5?s=50&d=blank&r=g)
Andres Tarallo
[ July 22, 2016 at 9:21 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801415)
Hi @Ravi,
The script is uploaded to GITHUB,
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 23, 2016 at 10:46 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801541)
@Andres,
Thanks for uploading the script on GitHub and also thanks for keeping its development…
       * ![](https://secure.gravatar.com/avatar/f7f6c171ef225c7530b098d406403c3261bcd34e5f2ba8b5a54a8338e13e097b?s=50&d=blank&r=g)
tushar jambhekar
[ July 22, 2016 at 11:13 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801328)
HI Ravi,
I’m also using SuSE Enterprise 11 Sp3 & getting many incorrect out-put.Here I’m attaching it:
OS Name : OS Version : Architecture : x86_64
Kernel Release : 3.0.76-0.11-default
Hostname : DC1SAPCSSRT
hostname: invalid option — ‘I’
Usage: hostname [-v] {hostname|-F file} set hostname (from file)
domainname [-v] {nisdomain|-F file} set NIS domainname (from file)
hostname [-v] [-d|-f|-s|-a|-i|-y|-n] display formatted name
hostname [-v] display hostname
hostname -V|–version|-h|–help print info and exit
dnsdomainname=hostname -d, {yp,nis,}domainname=hostname -y
-s, –short short host name
-a, –alias alias names
-i, –ip-address addresses for the hostname
-f, –fqdn, –long long host name (FQDN)
-d, –domain DNS domain name
-y, –yp, –nis NIS/YP domainname
-F, –file read hostname or NIS domainname from given file
This command can read or set the hostname or the NIS domainname. You can
also read the DNS domain or the FQDN (fully qualified domain name).
Unless you are using bind or NIS for host lookups you can change the
FQDN (Fully Qualified Domain Name) and the DNS domain name (which is
part of the FQDN) in the /etc/hosts file.
Internal IP :
External IP :
Name Servers : Before static /etc/sysconfig/network/config NETCONFIG_DNS_STATIC_SEARCHLIST NETCONFIG_DNS_STATIC_SERVERS NETCONFIG_DNS_FORWARDER or NETCONFIG_DNS_POLICY=” See Note: may only, file Please intelenetglobal.com 10.200.132.15 10.200.132.16
Logged In users :
tushar pts/0 Jul 22 10:35 (10.10.11.229)
free: invalid option — ‘h’
usage: free [-b|-k|-m|-g] [-l] [-o] [-t] [-s delay] [-c count] [-V]
-b,-k,-m,-g show output in bytes, KB, MB, or GB
-l show detailed low and high memory statistics
-o use old format (no -/+buffers/cache line)
-t display total for RAM + swap
-s update every [delay] seconds
-c update [count] times
-V display version information and exit
Ram Usages :
Swap Usages :
Disk Usages :
Filesystem Size Used Avail Use% Mounted on
/dev/sda1 18G 12G 5.1G 70% /
/dev/sda3 9.9G 1.2G 8.3G 12% /tmp
/dev/sda5 9.9G 2.5G 6.9G 27% /usr/sap/SRT
/dev/sda6 5.0G 970M 3.8G 21% /sapmnt/SRT
/dev/sda7 2.0G 172M 1.7G 9% /usr/sap/hostctrl
/dev/sda8 9.9G 1.4G 8.0G 15% /usr/sap/trans
/dev/sda10 1.4T 1.2T 140G 90% /oracle
/dev/sda9 20G 5.1G 14G 27% /oracle/SRT/112_64
Load Average : loadaverage:0.24,
System Uptime Days/(HH:MM) : 21 days
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801328)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 22, 2016 at 12:07 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801341)
@Tushar,
You just need to change the options available on your Linux distribution in the script to make it compatible with your Linux OS, because every Linux flavor has different options, so just use accordingly..
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801341)
         * ![](https://secure.gravatar.com/avatar/4f2d0693690cbb324e00ec4ed125c5b33a48df416d967ff62105be1f8ed3e1d5?s=50&d=blank&r=g)
Andres Tarallo
[ July 22, 2016 at 9:25 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801418)
Hi !!!!
I’ve been working on fixing that Issues on SuSE. I have them working on the script uploaded to github:
The fixes that are specific to SuSE/OpenSuSE are in the Development branch. Please take the script from there, you’re also welcome to contribute code and suggestions.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801418)
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 23, 2016 at 10:43 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801539)
@Andres,
Thanks for putting your efforts in making the script compatible with SuSE distribution, I haven’t yet checked the script on SuSE, but will certainly give a try today and see how it works..
           * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 23, 2016 at 11:01 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801545)
@Andres,
I’ve included the Github link to script in the article, so that users can download and keep further development of script under Tecmint license..
  35. ![](https://secure.gravatar.com/avatar/63c7fe4efbe73d87c34bdb67b97fa877ce624fd7374986c71a4384a5e040386c?s=50&d=blank&r=g)
emmanuelbuhay
[ June 18, 2016 at 1:27 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-792208)
At first my public ip address wasn’t displaying so i changed ipecho.net to myipaddress.com via vim but still didn’t work, found out i didn’t install curl yet because i did a “curl -s ipecho.net” or was it “curl -s myipaddress.com” and it didn’t recognize curl, since i changed tecmint.sh and forgot the exact syntax in the “curl -s ipecho.net” line, i just re-downloaded it and re-executed it and it finally worked! was happy to see all values, i had fun hahaha thanks and keep the educational contents coming! :)
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-792208)
     * ![](https://secure.gravatar.com/avatar/4f2d0693690cbb324e00ec4ed125c5b33a48df416d967ff62105be1f8ed3e1d5?s=50&d=blank&r=g)
Andres Tarallo
[ July 14, 2016 at 2:45 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-799048)
CURL is not mandatory to any distro I’m aware off. It’s very popular so many people think that it’s installed by default.
I’ll add to the modified script (I’m working actually) to check for CURL availability.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-799048)
     * ![](https://secure.gravatar.com/avatar/4f2d0693690cbb324e00ec4ed125c5b33a48df416d967ff62105be1f8ed3e1d5?s=50&d=blank&r=g)
Andres Tarallo
[ July 22, 2016 at 9:27 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801419)
I’ve added a check for availability of CURL, you can find the script on:
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801419)
       * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ July 23, 2016 at 10:40 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801538)
@Andres,
Thanks a ton for uploading the script to Github and also making the script available for development, will download and test it, if its works perfectly on all Linux distributions, will replace the current script with this new one..
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-801538)
  36. ![](https://secure.gravatar.com/avatar/4245267a689b24710ef0bed6e29322f98e199ce02654eb1fd447f33e5d4febc7?s=50&d=blank&r=g)
Alji Mohamed
[ June 13, 2016 at 5:46 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-790610)
Can you please share it on Github so we can fork it and optimize it
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-790610)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 21, 2016 at 11:24 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-793289)
@Alji,
Sure, we will share this script on Github…
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-793289)
       * ![](https://secure.gravatar.com/avatar/4245267a689b24710ef0bed6e29322f98e199ce02654eb1fd447f33e5d4febc7?s=50&d=blank&r=g)
ALJI Mohamed
[ June 22, 2016 at 6:22 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-793820)
can you please let me know by comment when it is available on github ? thank you
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-793820)
         * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ June 23, 2016 at 11:37 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-794106)
@Alji,
Hopefully by this weekend will upload this script on github, will let you know..
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-794106)
           * ![](https://secure.gravatar.com/avatar/4245267a689b24710ef0bed6e29322f98e199ce02654eb1fd447f33e5d4febc7?s=50&d=blank&r=g)
ALJI Mohamed
[ June 25, 2016 at 4:23 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-794804)
the weekend is here :D
  37. ![](https://secure.gravatar.com/avatar/ede12a59e3c23775639e4be8752937cf83c10cfd0034889f96cc29868370d1df?s=50&d=blank&r=g)
David
[ June 12, 2016 at 2:18 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-790375)
Running Fedora 23 workstation
Network interface is not eth0 (enp3s0)
My server is not 192.168.1.1 (192.168.1.10)
ifconfig –
enp3s0: flags=4163 mtu 1500
inet 192.168.1.168 netmask 255.255.255.0 broadcast 192.168.1.255
inet6 fe80::867b:ebff:fe3d:7c63 prefixlen 64 scopeid 0x20
ether 84:7b:eb:3d:7c:63 txqueuelen 1000 (Ethernet)
RX packets 118056 bytes 110385471 (105.2 MiB)
RX errors 0 dropped 0 overruns 0 frame 0
TX packets 72364 bytes 9256712 (8.8 MiB)
TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
lo: flags=73 mtu 65536
inet 127.0.0.1 netmask 255.0.0.0
inet6 ::1 prefixlen 128 scopeid 0x10
loop txqueuelen 1 (Local Loopback)
RX packets 21 bytes 1753 (1.7 KiB)
RX errors 0 dropped 0 overruns 0 frame 0
TX packets 21 bytes 1753 (1.7 KiB)
TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
virbr0: flags=4099 mtu 1500
inet 192.168.124.1 netmask 255.255.255.0 broadcast 192.168.124.255
ether 52:54:00:88:3b:b9 txqueuelen 1000 (Ethernet)
RX packets 0 bytes 0 (0.0 B)
RX errors 0 dropped 0 overruns 0 frame 0
TX packets 0 bytes 0 (0.0 B)
TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0
Note the spaces at the start of the lines – I used -d ‘ ‘ and -f14 for RX and TX
/etc/os-release
NAME=Fedora
VERSION=”23 (Workstation Edition)”
ID=fedora
VERSION_ID=23
PRETTY_NAME=”Fedora 23 (Workstation Edition)”
ANSI_COLOR=”0;34″
CPE_NAME=”cpe:/o:fedoraproject:fedora:23″
HOME_URL=”https://fedoraproject.org/”
BUG_REPORT_URL=”https://bugzilla.redhat.com/”
REDHAT_BUGZILLA_PRODUCT=”Fedora”
REDHAT_BUGZILLA_PRODUCT_VERSION=23
REDHAT_SUPPORT_PRODUCT=”Fedora”
REDHAT_SUPPORT_PRODUCT_VERSION=23
PRIVACY_POLICY_URL=https://fedoraproject.org/wiki/Legal:PrivacyPolicy
VARIANT=”Workstation Edition”
VARIANT_ID=workstation
Note PRETTY_NAME and CPE_NAME
/etc/resolve.conf
# Check Disk Usages
df -h| grep ‘Filesystem\|/dev/sda*’ > /tmp/diskusage
echo -e ‘\E[32m'”Disk Usages :” $tecreset
cat /tmp/diskusage
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-566811)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 16, 2015 at 4:24 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-572878)
Dear Shamrock,
i don’t have a xen setup to test and fix the discrepancies, however if i could get a ssh access to a xen setup i would like to customize the script till it is fixed. Thanks for taking the time and providing us with your valuable feedback. Keep Connected!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-572878)
  86. ![](https://secure.gravatar.com/avatar/21985ec3ccc409da0128cd97e0abb3b5ba991258d286572c016a719eabe80f4e?s=50&d=blank&r=g)
Madhur
[ May 10, 2015 at 4:15 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-565729)
why not use conky

[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-565729)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 11, 2015 at 11:32 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-566398)
Because you may not be running a GUI server always specially in enterprise and production.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-566398)
  87. ![](https://secure.gravatar.com/avatar/36064cb505514e9dddda5de85dac05c1ed884166f6b063ff1f7b7f36f5f7a3e7?s=50&d=blank&r=g)
Ronaldo
[ May 9, 2015 at 8:39 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-565101)
Very nice script, thanks so much.Linux forever 100 % optimal O.S.
i found a issue see:
./tecmint_monitor.sh: linha 79: curl: commando não encontrado curl: command not found
I use peppermint 5 ( Ubuntu 14.04 based ) and great O.S.
thanks and advance ( keep running ;) )
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-565101)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 9, 2015 at 8:45 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-565104)
$ sudo apt-get install curl
and then run script. it should run without any error.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-565104)
  88. ![](https://secure.gravatar.com/avatar/a51aa4f5964c925a0447a655f4e30bb7e4cdcdcd0102638e66f83c61e62d36f3?s=50&d=blank&r=g)
Ravikumar Wagh
[ May 9, 2015 at 8:22 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-565095)
Thanks for this post ….. If Want to remove it… what is process to do..
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-565095)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 9, 2015 at 8:48 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-565107)
If you have installed it you may like to remove it as
