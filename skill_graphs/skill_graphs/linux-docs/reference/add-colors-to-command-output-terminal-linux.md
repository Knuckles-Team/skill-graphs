[Skip to content](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/#content "Skip to content")
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
Menu
  * [Learn Linux](https://www.tecmint.com/free-online-linux-learning-guide-for-beginners/ "Start Learning Linux")
  * [Linux Distros](https://www.tecmint.com/best-linux-distributions/ "Linux Distributions")
    * [Linux Distros for Beginners](https://www.tecmint.com/best-linux-distributions-for-beginners/)
    * [Linux Distros for Experts](https://www.tecmint.com/linux-distro-for-power-users/ "Widely Used Distros")
    * [New Linux Distros](https://www.tecmint.com/new-linux-distributions/)
    * [Linux Server Distros](https://www.tecmint.com/10-best-linux-server-distributions/)
    * [Secure Linux Distros](https://www.tecmint.com/best-security-centric-linux-distributions/)
    * [CentOS Alternatives](https://www.tecmint.com/centos-alternative-distributions/ "CentOS Alternative Distros")
    * [RedHat Distributions](https://www.tecmint.com/redhat-based-linux-distributions/ "RedHat Based Distros")
    * [Debian Distributions](https://www.tecmint.com/debian-based-linux-distributions/ "Debian Based Distros")
    * [Ubuntu Distributions](https://www.tecmint.com/ubuntu-based-linux-distributions/ "Ubuntu Based Distros")
    * [Arch Linux Distros](https://www.tecmint.com/arch-based-linux-distributions/ "Arch Linux Based Distros")
    * [Rolling Linux Distros](https://www.tecmint.com/best-rolling-release-linux-distributions/)
    * [KDE Linux Distros](https://www.tecmint.com/best-linux-distributions-for-kde-plasma/ "KDE Based Distros")
    * [Linux Distros for Old PC](https://www.tecmint.com/linux-distributions-for-old-computers/ "Linux Distros for Older Computers")
    * [Linux Distros for Kids](https://www.tecmint.com/best-linux-distributions-for-kids/)
    * [Linux Distributions for Students](https://www.tecmint.com/linux-distros-students/)
    * [Linux Distros for Windows](https://www.tecmint.com/best-alternative-linux-distributions-for-windows-users/)
  * [Commands](https://www.tecmint.com/category/linux-commands/ "Linux Commands")
    * [A – Z Linux Commands](https://www.tecmint.com/linux-commands-cheat-sheet/)
    * [100+ Linux Commands](https://www.tecmint.com/essential-linux-commands/ "Essential Linux Commands")
  * [Tools](https://www.tecmint.com/category/top-tools/ "Best Linux Software")
  * [Pro Courses](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/ "Linux Online Courses")
    * [Bash Scripting](https://pro.tecmint.com/learn-bash-scripting/ "Bash Scripting for Beginners")
    * [Learn Linux](https://pro.tecmint.com/learn-linux/ "Master Linux in 7 Days")
    * [AI for Linux](https://pro.tecmint.com/ai-for-linux/ "AI for Linux Course")
    * [RHCSA Certification](https://pro.tecmint.com/rhcsa-certification-course/ "RHCSA Certification Course")
    * [RHCE Certification](https://pro.tecmint.com/rhce-certification-course/ "RHCE Certification Course")
    * [LFCS Certification](https://pro.tecmint.com/lfcs-certification-course/ "LFCS Certification Course")
  *     * [RHCSA Exam](https://www.tecmint.com/rhcsa-exam-reviewing-essential-commands-system-documentation/ "RHCSA Certification eBook")
    * [RHCE Exam](https://www.tecmint.com/how-to-setup-and-configure-static-network-routing-in-rhel/ "RHCE Certification eBook")
    * [LFCS Exam](https://www.tecmint.com/sed-command-to-create-edit-and-manipulate-files-in-linux/ "LFCS Certification eBook")
    * [LFCE Exam](https://www.tecmint.com/installing-network-services-and-configuring-services-at-system-boot/ "LFCE Certification eBook")
    * [LFCA Exam](https://www.tecmint.com/understanding-linux-operating-system/ "LFCA Certification eBook")
    * [Ansible Exam](https://www.tecmint.com/understand-core-components-of-ansible/ "Ansible Certification eBook")
  * [About](https://www.tecmint.com/who-we-are/)
    * [Contact](https://www.tecmint.com/contact-us/ "Contact Us")
    * [Hiring](https://www.tecmint.com/hiring/ "Write for Us")
    * [Newsletter](https://www.tecmint.com/subscribe-to-blog/ "Linux Weekly Newsletter")
    * [Testimonials](https://www.tecmint.com/testimonials/)
    * [Donate](https://www.tecmint.com/donate-to-tecmint/ "Support TecMint")
    * [Advertise](https://www.tecmint.com/advertise/ "TecMint Sponsorship Opportunities")
    * [Submit Article Request](https://www.tecmint.com/submit-article-request/)
    * [Suggest an Update](https://www.tecmint.com/suggest-an-update/)


[](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/)
In this article, we will review a cool and simple way of giving a command screen output a rainbow colors and slowing down its output speed as well for one reason or the other.
The [lolcat program](https://www.tecmint.com/lolcat-command-to-output-rainbow-of-colors-in-linux-terminal/) is used for the above purpose. It basically functions by concatenating files, or standard input, to standard output in a similar way as the [cat command](https://www.tecmint.com/13-basic-cat-command-examples-in-linux/), overrides the default screen output color of a particular command and adds rainbow coloring to it.
### How to Install Lolcat Program in Linux
**Lolcat** program is available on almost all modern Linux distributions from its default repository, but the available version bit older. Alternatively you can install latest version of **lolcat** from git repository using this following guide.
  1. [Install Lolcat to Output Rainbow Of Colors in Linux Terminal](https://www.tecmint.com/lolcat-command-to-output-rainbow-of-colors-in-linux-terminal/)


Once lolcat installed, the basic syntax for running **lolcat** is:
```
$ lolcat [options] [files] ...

```

It comes with several options that control its behavior, below are a few of the most considerable flags we will emphasis for the scope of this guide:
  1. `-a` – passes every input line through an animation effect.
  2. `-d` – specifies the duration (number of steps before displaying next line) of the animation effect, the default value is 12.
  3. `-s` – it specifies the speed (frame rate- number of steps per second) of the animation effect, default value is 20.
  4. `-f` – enables forcing of coloring in case standard output is not a tty.


You can find more options in the **lolcat** man page:
```
$ man lolcat

```

### How to Use Lolcat in Linux
To use **lolcat** , simply pipe the output of any relevant command to it and watch the magic.
For example:
```
$ ls -l | lolcat -as 25

```

![colorful Linux Terminal Output](https://www.tecmint.com/wp-content/uploads/2016/12/Colorful-Linux-Terminal-Output.gif)
Besides you can alter the default speed, in the following command, we will use a relatively slow speed of **10** steps per second:
```
$ ls -l | lolcat -as 10

```

You can use any command with **lolcat** display output in colorful fashion on Linux terminal, few commands say ps, date and cal as:
```
$ ps | lolcat
$ date | lolcat
$ cal | lolcat

```

In this article, we have looked at how to significantly reduce the speed of a command screen output and give it a rainbow coloring effect.
As usual, you can address to us any questions or comments concerning this article via the feedback section below. Lastly, you can mention to us any useful Linux commands you have discovered there.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Perform Syntax Checking Debugging Mode in Shell Scripts](https://www.tecmint.com/check-syntax-in-shell-script/)
Next article:
[Deal: Get Machine Learning and Artificial Intelligence Course (91% Off)](https://www.tecmint.com/machine-learning-artificial-intelligence-course/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### 3 Comments
[Leave a Reply](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/#reply-title)
  1. Can you tell me a way to add this in **bashrc** so that it works every time on the terminal and I don’t have to pipe my stdout to lolcat every time
[Reply](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/#comment-1394239)
  2. Funny but not useful! :)
[Reply](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/#comment-847824)
     * @Ice
Yap, it’s not exactly useful to experienced Linux users but newbies may find it a little interesting. Thanks for the feedback.
[Reply](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/#comment-847891)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/add-colors-to-command-output-terminal-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)![](https://sync.smartadserver.com/getuid?url=https%3A%2F%2Fids.ad.gt%2Fapi%2Fv1%2Fsmart_match%3Fid%3DAU1D-0100-001772949750-XXM2FI1H-SG2Q%26sas_uid%3D%5bsas_uid%5d&gdpr=0)![](https://bh.contextweb.com/bh/rtset?pid=562316&ev=1&rurl=https://ids.ad.gt/api/v1/ppnt_match?uid=%%VGUID%%&id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&gdpr=0)![](https://sync.1rx.io/usersync/audigent/0?dspret=1&redir=https%3A%2F%2Fids.ad.gt%2Fapi%2Fv1%2Funruly%3Fid%3DAU1D-0100-001772949750-XXM2FI1H-SG2Q%26unruly_id%3D%5BRX_UUID%5D&gdpr=0)![](https://sync.colossusssp.com/ebfa23da174faa55634171c5e49d0152.gif?puid=AU1D-0100-001772949750-XXM2FI1H-SG2Q&redir=http%3A%2F%2Fids.ad.gt%2Fapi%2Fv1%2Fcolossus%3Fcls_id%3D%5BUID%5D%26id%3DAU1D-0100-001772949750-XXM2FI1H-SG2Q)![](https://ssum-sec.casalemedia.com/ium?sourceid=15&uid=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000&gdpr=0)![](https://onetag-sys.com/match/?int_id=180&uid=AU1D-0100-001772949750-XXM2FI1H-SG2Q&gdpr=0)![](https://dpm.demdex.net/ibs:dpid=348447&dpuuid=AU1D-0100-001772949750-XXM2FI1H-SG2Q&redir=https%3A%2F%2Fids.ad.gt%2Fapi%2Fv1%2Fadb_match%3Fadb%3D%24%7BDD_UUID%7D%26id%3DAU1D-0100-001772949750-XXM2FI1H-SG2Q&gdpr=0)
