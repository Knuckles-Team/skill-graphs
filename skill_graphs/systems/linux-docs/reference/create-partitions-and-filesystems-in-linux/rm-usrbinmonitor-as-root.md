# rm /usr/bin/monitor (as root)
or
$ sudo /usr/bin/monitor (on sudo based system)
and all done!
will add uninstall in the next version.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-565107)
  89. ![](https://secure.gravatar.com/avatar/e8cf9ba3cc55b659b5379a8331f83c84e15a06fd8f11988e46a26964450df916?s=50&d=blank&r=g)
Someguy McPants
[ May 9, 2015 at 8:19 am  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564543)
Word of advice: Pass your scripts through shellcheck.net and think about portability. This won’t run well on Solaris/HP-UX/etc
And I’m not sure I see the value in assigning variables for single use, especially to use in echo, when you should be using printf. Finally, don’t encourage the habit of “cat /some/file | someprocessing”. This is a useless use of cat (UUOC) (yes, google that). cat is for conCATenating files together, not for dumping file contents into a pipe – except for a few rare edge cases. This kind of cat usage is a glaring indicator of a newbie coder.
Example:
cat /etc/os-release | grep ‘NAME\|VERSION’
A better way to write this is:
grep ‘NAME\|VERSION’ /etc/os-release
I’ve rewritten the script in my own image, but I haven’t built much more into it, and I’ve intentionally left a couple of issues because my carefactor is low. See if you can spot them. Grab the code here:
Pass yours through shellcheck, then mine through shellcheck and compare. Learn why not to UUOC, why to use printf over echo, and how to quote variables properly.
Good luck!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564543)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 9, 2015 at 12:13 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564857)
Dear Someguy McPants
I have not written it for HP-UX and solaris. Moreover this project was just the work of a couple of hours of mine and not something i was funded/paid. But this is not the excuse i would give and will ask for some time to make it run on HP-UX and Solaris. I agree to your point that defining variables for single action is not recommended moreover using printf in place of echo and use cat as least as possible is true. I did this only to play safer, making a temporary copy of command and then grep/awk/sed/cut into it. I tried what you are suggesting now, while writing the script but it was getting a little complex with filter.
Don’t worry! i will be fixing it soon and add certain other system information to it as well as format it a little more.
Thanks for your concern and feedback.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564857)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 9, 2015 at 12:37 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564889)
Moreover the problem with your suggestion is
grep ‘NAME\|VERSION’ /etc/os-release will require root access and i tried to make this script run without root as far as possible. that’s why i used ip and not ifconfig. Thanks for writing such a nice critics :)
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564889)
  90. ![](https://secure.gravatar.com/avatar/c5434756832fbfac1636ba040df7eefa83d205f6266b16e1ac9ba931c6b4b2ef?s=50&d=blank&r=g)
dype
[ May 8, 2015 at 9:30 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564185)
Hi
Thanks for the script.
I replace “su -c “cp $scriptname /usr/bin/monitor” root”
by : sudo cp $scriptname /usr/bin/monitor
login as root is not allowed on the systems I manage.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564185)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 9, 2015 at 12:02 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564836)
Welcome dype.
thanks for your feedback!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564836)
  91. ![](https://secure.gravatar.com/avatar/5167c1201e21d0b3317430042d6cbb05c3a31c96307b6b3027214ac4022c3227?s=50&d=blank&r=g)
David Smith
[ May 8, 2015 at 9:10 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564158)
This is throwing an error in Ubuntu 10.04: “free: invalid option — ‘h'”, so it doesn’t report Ram, Swap and Disk Usages, and Filesystem stats.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564158)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 9, 2015 at 12:02 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564835)
David i have checked it on Debian, CentOS and Mint. it run well without any issue. give me some time and let me figure out why it is throwing such error on Ubuntu
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564835)
  92. ![](https://secure.gravatar.com/avatar/f43952e00391090419e367455804ac55513d0ed9b94d18d804ece2d044a1aaa6?s=50&d=blank&r=g)
Dhananja Kariyawasam
[ May 8, 2015 at 9:01 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564153)
Is this working for UNIX platform (Eg : Solaris) ?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564153)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 9, 2015 at 12:01 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564830)
Why don’t you check and let us know so that i can fix if any issue.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564830)
  93. ![](https://secure.gravatar.com/avatar/f15aa46b507dd6c659a7ddaa0e505f4c5e1e31ef5a7a93f8c7da6e89878afb2a?s=50&d=blank&r=g)
dali
[ May 8, 2015 at 5:22 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564032)
use monit
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-564032)
  94. ![](https://secure.gravatar.com/avatar/7ca222e13666a901cb7f96f3118f8ae567a8fda8116f1f5965bbe31f138be9c2?s=50&d=blank&r=g)
ramesh
[ May 8, 2015 at 3:21 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-563943)
I am working in hp bit confused abt sos report where to check the issue and failure components can you help me on creating script so tat all the information can get in one place
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-563943)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 8, 2015 at 3:47 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-563968)
Dear ramesh,
though i have never worked on HP-UX and i am not aware of how it reports. Will you please share a complete log of sos report and what information you want from that, in very clear language?
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-563968)
  95. ![](https://secure.gravatar.com/avatar/2205b25fb88d65b969b13cba22fc774178cd6040d78fb75dfc526558845ed821?s=50&d=blank&r=g)
Khaled Jamel
[ May 8, 2015 at 2:10 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-563882)
thanks for the script, its helpful for live status checking, just i think that it need more flexibility on disk size monitoring because it looks just to / /dev/sda running it on an ubuntu machine where system is installed on a separated part. and on LVM mode it shows an empty result.
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-563882)
     * ![](https://secure.gravatar.com/avatar/9528d5c8e619e606a64aea49dc1fd2bb0c16e11cd9a9f326d934fb4629a6bd67?s=50&d=blank&r=g)
Avishek Kumar
[ May 8, 2015 at 3:30 pm  ](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-563949)
Yeah! khaled Jamel
I have used sda* in the code you may include one more grep code there to look after all lvm.
It is not going to be any difficult.
Keep connected!
[Reply](https://www.tecmint.com/linux-server-health-monitoring-script/#comment-563949)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/linux-server-health-monitoring-script/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
## Upgrade Your Linux Learning with Pro.Tecmint
**If you find TecMint helpful** , consider supporting us by subscribing to [**Pro.Tecmint.com**](https://pro.tecmint.com) – our premium platform with exclusive guides, ad-free experience, early access to tutorials, and much more.

Your support helps us keep creating quality Linux content for everyone.
[ Get Lifetime Access ](https://pro.tecmint.com)
## Linux Commands and Tools
[How to Set Static IP Address and Configure Network in Linux](https://www.tecmint.com/set-add-static-ip-address-in-linux/)
[How to Check Remote Ports are Reachable Using ‘nc’ Command](https://www.tecmint.com/check-remote-port-in-linux/)
[8 Mysterious Uses of (!) Operator in Linux Commands](https://www.tecmint.com/logical-not-operator-linux-commands/)
[Fzf – A Quick Fuzzy File Search from Linux Terminal](https://www.tecmint.com/fzf-fuzzy-file-search-from-linux-terminal/)
[2 Ways to Create an ISO from a Bootable USB in Linux](https://www.tecmint.com/create-an-iso-from-a-bootable-usb-in-linux/)
[6 Useful Tools to Troubleshoot DNS Name Resolution Problems](https://www.tecmint.com/troubleshoot-dns-in-linux/)
## Linux Server Monitoring Tools
[Conky – A System Monitor Tool for Linux Desktop](https://www.tecmint.com/conky-system-monitor/)
[httpstat – A Curl Statistics Tool to Check Website Performance](https://www.tecmint.com/httpstat-curl-statistics-tool-check-website-performance/)
[How to Monitor Linux Server Security with Osquery](https://www.tecmint.com/monitor-linux-server-security-with-osquery/)
[How to Install Cacti with Cacti-Spine in Debian and Ubuntu](https://www.tecmint.com/install-cacti-with-cacti-spine-in-debian-and-ubuntu/)
[4 Useful Commandline Tools to Monitor MySQL Performance in Linux](https://www.tecmint.com/mysql-performance-monitoring/)
[LibreNMS – A Fully Featured Network Monitoring Tool for Linux](https://www.tecmint.com/install-librenms-monitoring-on-ubuntu-centos/)
## Learn Linux Tricks & Tips
[12 Useful PHP Commandline Usage Every Linux User Must Know](https://www.tecmint.com/execute-php-codes-functions-in-linux-commandline/)
[Display Command Output or File Contents in Column Format](https://www.tecmint.com/display-command-output-or-file-contents-in-column-format/)
[Powerline – Adds Statuslines and Prompts to Vim and Bash Shell](https://www.tecmint.com/powerline-plugin-for-vim/)
[How to Find Out List of All Open Ports in Linux](https://www.tecmint.com/find-open-ports-in-linux/)
[How to Save Command Output to a File in Linux](https://www.tecmint.com/save-command-output-to-a-file-in-linux/)
[How to Create a Password Protected ZIP File in Linux](https://www.tecmint.com/create-password-protected-zip-file-in-linux/)
## Best Linux Tools
[Top 3 Open Source Virtual Data Room (VDR) for Linux](https://www.tecmint.com/open-source-virtual-data-room-for-linux/)
[19 Best Open Source WYSIWYG HTML Editors in 2023](https://www.tecmint.com/wysiwyg-html-editors/)
[Top 5 Linux Programs for Students in 2025](https://www.tecmint.com/linux-programs-for-students/)
[Top 6 Partition Managers (CLI + GUI) for Linux](https://www.tecmint.com/linux-partition-managers/)
[Top 5 Open-Source OCR Tools for Linux in 2025](https://www.tecmint.com/best-linux-ocr-tools/)
[Top 6 Command Line Music Players for Linux Users](https://www.tecmint.com/command-line-music-players-for-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/linux-server-health-monitoring-script/ "Scroll back to top")
Search for:
