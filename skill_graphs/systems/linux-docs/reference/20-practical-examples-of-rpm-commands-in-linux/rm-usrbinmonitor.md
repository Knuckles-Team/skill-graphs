# rm /usr/bin/monitor
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-625089)
  65. ![](https://secure.gravatar.com/avatar/b7630566a0477f19e351c76679ff72ff716bf842deab26c8a7ff667b908f656b?s=50&d=blank&r=g)
Cheta
[ July 15, 2015 at 6:46 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-624806)
How do i uninstall it if i don’t want to use it
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-624806)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ July 16, 2015 at 9:21 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-625090)
Cheta,
To remove this installed script from your system, run the below command as root, exactly as it is.
# rm /usr/bin/monitor
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-625090)
  66. ![](https://secure.gravatar.com/avatar/f8ea573d78a311375ae56f34056d2aecfee042fb76f333e73eadbdb581fe1356?s=50&d=blank&r=g)
shanker
[ June 8, 2015 at 7:51 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-592363)
memory usage should be this
free | grep -v + > /tmp/ramcache
and disk usage should be this
df -h| egrep -i ‘Filesystem|/dev/.da*’ > /tmp/diskusage in centos system and ubuntu
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-592363)
  67. ![](https://secure.gravatar.com/avatar/21760347a77d9aeeba0ec7824eb5421dba1b83abb623c21aeba6b652ff4d9e4e?s=50&d=blank&r=g)
Luis
[ June 6, 2015 at 4:30 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-590346)
where can i get the source code?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-590346)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ June 6, 2015 at 8:46 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-590538)
Please download the script as suggested using wget command, in the guide above.
The downloaded file contains all the source code, you need.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-590538)
  68. ![](https://secure.gravatar.com/avatar/15a996d1f9273e18a0e38ce09be5b4652b7179c5dfa54d8401f1e364d3f96514?s=50&d=blank&r=g)
sivaraman
[ June 5, 2015 at 10:53 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589491)
Thanks
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589491)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ June 8, 2015 at 3:19 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-592666)
Welcome @ sivaraman,
Keep Connected!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-592666)
  69. ![](https://secure.gravatar.com/avatar/0658d4c4e277bd9fad276046d0d932588eabb418e5e5771dc6feb0ab81324d17?s=50&d=blank&r=g)
Ahmed Shibani
[ June 4, 2015 at 5:49 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-588807)
Small fix, move the #! /bin/bash line to the top of the file. Otherwise the script won’t run properly if not using any other shell such as sh or zsh.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-588807)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ June 5, 2015 at 10:03 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589448)
Dear Ahmed Shibani,
Agree with you. Also it has been recommended by a lots of users.
Thanks for your feedback.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589448)
  70. ![](https://secure.gravatar.com/avatar/ce80734abf8b004539a6ec8b8627ef311137ea94c76402aa29127af60b55db2a?s=50&d=blank&r=g)
sleep_walker
[ June 4, 2015 at 12:45 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-588678)
This script is ugly as hell.
1] `cat file | grep regex’ instead of `grep regex file’
2] cat | grep | grep | grep – and only to create temp file which will be processed after that again !!!
3] running top instead of reading /proc/loadavg directly
4] cat | sed | awk – why don’t you create one script either for sed or awk?
5] why to store into tmpfile when not necessary?
who > tmpfile
echo && cat
use instead
echo && who
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-588678)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ June 5, 2015 at 10:00 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589441)
ohh thankyou! sleep_walker
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589441)
  71. ![](https://secure.gravatar.com/avatar/105db3d42d6a8752ad679c2de38de6bd6da67159b06f0e9be89e1f36e7d6e333?s=50&d=blank&r=g)
dominix
[ June 4, 2015 at 6:21 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-588391)
I would recommend scan for nameserver this way:
cat /etc/resolv.conf |awk ‘/^nameserver/{print $2}’
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-588391)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ June 5, 2015 at 10:02 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589446)
Taken into account @dominix
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589446)
  72. ![](https://secure.gravatar.com/avatar/373db98a53aeec1a9652a8fa85c29c0dd5ba15010b566d155abf47d7f30ae533?s=50&d=blank&r=g)
Kristal
[ June 2, 2015 at 11:50 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-586833)
Other than swap and ram this worked really well on CentOS release 6.6 (Final). Thank you.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-586833)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ June 5, 2015 at 10:00 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589439)
Dear Kristal, In your case RAM and SWAP output was not clear as indicated by you. I have tested it on Debian and Mint. I agree that due to difference in implementation of same thing by different distros, differently, there could be an issue like this. Let me know what distribution you tested it upon, so that i can work to make it compatible.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589439)
  73. ![](https://secure.gravatar.com/avatar/3a24a8eac3eb2a1f3a7a03aaae211de60b49c6f71f0556ce652485cd9ec89c58?s=50&d=blank&r=g)
Hardik
[ June 1, 2015 at 6:18 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-586171)
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-586171)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ June 5, 2015 at 10:03 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589452)
Nice link Hardik,
We have already shown how to run and install script in the article.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589452)
  74. ![](https://secure.gravatar.com/avatar/3a24a8eac3eb2a1f3a7a03aaae211de60b49c6f71f0556ce652485cd9ec89c58?s=50&d=blank&r=g)
Hardik
[ June 1, 2015 at 6:15 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-586166)
im running ubunt and loged in as root ,was able to download but says permission denied when installing , any help please!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-586166)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ June 5, 2015 at 9:57 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589437)
All you need to do is read the article again!
For quick tips
1. Download the script
2. chmod 755 Script_name.sh
3. ./Script_name.sh
Alternatively, to install
4. ./Script_name.sh -i
Welcome!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589437)
  75. ![](https://secure.gravatar.com/avatar/48a62cd8bb2ed888685aaf2ba23a577506b3aaa7b72c4d9b0ec7fbb40eeb53be?s=50&d=blank&r=g)
Savvas
[ June 1, 2015 at 2:42 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-586061)
Really nice @ Debian Jessie
Thank you!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-586061)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ June 5, 2015 at 9:56 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589435)
Welcome @Savvas, Keep Connected!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-589435)
  76. ![](https://secure.gravatar.com/avatar/879e6bac1962199946e4ad73c4d6a46e586c6fc317342159cb709ad8d35e92b1?s=50&d=blank&r=g)
Luca
[ May 19, 2015 at 8:54 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-576099)
Very good script, thanks!
Any chance to have a parameter to avoid screen clear?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-576099)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 20, 2015 at 11:24 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-576504)
Dear Luca,
you want to avoid screen clearing at the beginning of the script?
If yes you may just put a # in the beginning of script where the text matches ‘clear’, save and execute.
Also let me know why you don’t want to clear the screen?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-576504)
       * ![](https://secure.gravatar.com/avatar/879e6bac1962199946e4ad73c4d6a46e586c6fc317342159cb709ad8d35e92b1?s=50&d=blank&r=g)
Luca
[ May 22, 2015 at 7:07 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-578692)
I simply don’t like so much, that’s it ;) Thanks for the suggestions.
I’m checking on CentOS 6.6 (virtualized on qemu) but
– os type is not detected
– there are issues with detection of ram, disk (I understand could be a mess with various partitions) and load average
Internet: Connected
Operating System Type : GNU/Linux
cat: /etc/os-release: No such file or directory
OS Name : OS Version : Architecture : x86_64
Kernel Release : 2.6.32-504.12.2.el6.x86_64
Hostname : qapv12
Internal IP : xxxxxxxx
External IP : xxxxxxxx
Name Servers : xxxxxxxx
Logged In users :
luca pts/0 2015-05-22 13:29 (xxxxxxxxx)
free: invalid option — ‘h’
usage: free [-b|-k|-m|-g] [-l] [-o] [-t] [-s delay] [-c count] [-V]
-b,-k,-m,-g show output in bytes, KB, MB, or GB
-l show detailed low and high memory statistics
-o use old format (no -/+buffers/cache line)
-t display total for RAM + swap
-s update every [delay] seconds
-c update [count] times
-a show available memory if exported by kernel (>80 characters per line)
-V display version information and exit
Ram Usages :
Swap Usages :
Disk Usages :
Filesystem Size Used Avail Use% Mounted on
Load Average : loadaverage:0.13,
System Uptime Days/(HH:MM) : 59 days
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-578692)
         * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 25, 2015 at 10:54 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-581566)
Dear Luca,
as said earlier such difference in output is because of difference in implementation of same thing by different Linux Distribution. Give me some time so that i can modify it for CentOS GNU/Linux, so that next time you can say “I Like this Very Much.” Keep Connected. Thanks.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-581566)
  77. ![](https://secure.gravatar.com/avatar/d8cd4b5fc5e9dbb8de7b87a86e59ca98a698230b6fd3f4ec901da20ba22f27c6?s=50&d=blank&r=g)
Kurt
[ May 19, 2015 at 6:43 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-575695)
Why not use Conky?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-575695)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 19, 2015 at 10:16 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-575824)
Because you may not have GUI (Headed) Server specially in Enterprise and Production.
P.S : Conky runs in GUI
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-575824)
  78. ![](https://secure.gravatar.com/avatar/91f687aa3dffc7e39de0774a9a4d88a523981900ccbbc471f47e0bd556aec939?s=50&d=blank&r=g)
Pedro
[ May 18, 2015 at 5:24 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-574996)
Hi,
Didn’t worked properly in Centos:
– no OS Name and Version
– Outputs the error in the free command (free: invalid option — ‘h’ …)
– Also no Ram, Swap and Disk usages
Regards
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-574996)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 18, 2015 at 11:40 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-575322)
Pedro,
Due to non-uniform implementation of same command and switch differently by different distribution this is not working as it should be.
The good thing is i am working on next release of this on git.
Will soon fix those issues. Till then keep connected. Enjoy
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-575322)
  79. ![](https://secure.gravatar.com/avatar/2cadc1d185e2a5b46835f5715ae26092c31fd50ac51d16ac79a780c1ae16c12f?s=50&d=blank&r=g)
Aryan
[ May 18, 2015 at 5:01 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-574985)
its not working with FreeBSD
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-574985)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 18, 2015 at 11:41 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-575324)
@ Aryan
Due to non-uniform implementation of same command and switch differently by different distribution this is not working as it should be.
The good thing is i am working on next release of this on git.
Will soon fix those issues. Till then keep connected. Enjoy
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-575324)
  80. ![](https://secure.gravatar.com/avatar/d7a5894358ce9fc71df66d78ba03eecececf2c57ca1f8612c0c01583a175a389?s=50&d=blank&r=g)
smaxx
[ May 15, 2015 at 1:24 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-571719)
I like this script and may use in my teaching. However I found two issues that already have been mentioned. With Mageia4 I also get errors with ‘hostname -I’ (woks fine with ‘hostname -i’) and ‘free -h’ (works better with ‘free -m’). Just o confirm that this is not just an issue with Ubuntu.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-571719)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 16, 2015 at 4:17 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-572870)
smaxx we are happy to know that you find this script helpful. Moreover It is a proud to listen that our script will be used by a nation builder aka teacher to our future generation. Thanks for your’s tips. It is quite expected as all Linux System don’t follow same/Universal way of implementing commands and configuration.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-572870)
  81. ![](https://secure.gravatar.com/avatar/ddcfcd4ef8a5a792f5682dd7d58f93eaf2bc16b1bdc4fda2f7b285648e860333?s=50&d=blank&r=g)
Subhranil Dey
[ May 15, 2015 at 12:11 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-571032)
well make curl to install automatically too.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-571032)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 16, 2015 at 4:18 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-572871)
@Subhranil Dey, Thanks for your feedback. We are working on the next version of this script where we would improved user’s experience and add a few things. Keep Connected!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-572871)
  82. ![](https://secure.gravatar.com/avatar/7bc74c1f32bc4b069c435d8b12b2d8b1a67f18d96c151a22dcab56c1a48dd358?s=50&d=blank&r=g)
Gen
[ May 12, 2015 at 8:51 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-568292)
Thanks, this is a very helpful script for SysAdmins.
We are also trying to help the day-to-day of SysAdmins in the capacity of uptime and performance monitoring with a tool called Happy Apps: monitoring without the noise. Free accounts at
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-568292)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 16, 2015 at 4:19 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-572872)
Thanks for the nice Link. We would like to know if there is any affiliating program you have for us?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-572872)
  83. ![](https://secure.gravatar.com/avatar/a8bbf7ab773278f15fcb45c8dc627ddc4c678bc8b4059318c514631f758bdef1?s=50&d=blank&r=g)
Verner Kjærsgaard
[ May 12, 2015 at 4:16 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-568112)
Hi, great script!
– but ‘hostname -I’ doesn’t work in openSuse12.3, I think it should be a normal ‘i’, not a capital one…
Best regards,
Verner K.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-568112)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 16, 2015 at 4:20 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-572873)
@ Verner Kjaersgaard,
Agree its bcz of different implementation of same thing by different distributions. We will be fixing this in our next release. Keep Connected!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-572873)
  84. ![](https://secure.gravatar.com/avatar/33f6dad8f15c2a2320072caa469d472b9a3e5a9a3b5180fd4ee54e6e8da84e0c?s=50&d=blank&r=g)
Gaurav
[ May 11, 2015 at 5:14 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-566875)
Which app you use for creating gifs?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-566875)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 16, 2015 at 4:22 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-572876)
Dear Gaurav,
That is an small application written by us but as of now it has not been named. Neither has been decided to publish the application under what License.
Any help/suggestion in script is welcome.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-572876)
  85. ![](https://secure.gravatar.com/avatar/0b45d2f31ce30599520ca99185fca211d87ed9c42185f2899fed38e70e9e7aab?s=50&d=blank&r=g)
Shamrock
[ May 11, 2015 at 4:39 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-566811)
Doesn’t work properly under xen.
