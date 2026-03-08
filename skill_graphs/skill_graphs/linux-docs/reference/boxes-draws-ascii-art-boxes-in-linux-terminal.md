[Skip to content](https://www.tecmint.com/boxes-draws-ascii-art-boxes-in-linux-terminal/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/boxes-draws-ascii-art-boxes-in-linux-terminal/ "Linux Online Courses")
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


[](https://www.tecmint.com/boxes-draws-ascii-art-boxes-in-linux-terminal/)
**Boxes** is a simple, configurable command line program which can draw any kind of box around its input text. It filters text and draws shapes around it – it’s practically a text filter. In fact it is designed to be integrated with your editor as a text filter (supports Vim default). It can draw shapes ranging from simple boxes to [complex ASCII art](https://www.tecmint.com/create-ascii-text-banners-in-linux-terminal/).
In this article, we will learn how to use the boxes utility to draw shapes in the Linux terminal.
### How to Install Boxes Utility in Linux
To install the **boxes** utility in Linux, use the appropriate command for your distribution.
```
$ sudo apt install boxes  [On **Debian/Ubuntu**]
$ sudo yum install boxes  [On **CentOS/RHEL**]
$ sudo dnf install boxes  [On **Fedora**]

```

Now that you have boxes installed, note that it uses the `$HOME/.boxes` user specific configuration file or the **/etc/boxes/boxes-config** system-wide configuration file.
Let’s have [some Linux terminal fun](https://www.tecmint.com/20-funny-commands-of-linux-or-linux-is-fun-in-terminal/).
To see the default boxes design, simply provide some input text to it as shown.
```
**$ echo "Hey, this is Tecmint.com! Thanks for following us." | boxes**

**/******************************************************/
/* Hey, this is Tecmint.com! Thanks for following us. */
/******************************************************/**

```

To specify another design, use the `-d` flag as shown.
```
**$ echo "Hey, this is Tecmint.com! Thanks for following us." | boxes -d boy**
**
                        .-"""-.
                       / .===. \
                       \/ 6 6 \/
                       ( \___/ )
  _________________ooo__\_____/_____________________
 /                                                  \
| Hey, this is Tecmint.com! Thanks for following us. |
 \______________________________ooo_________________/
                       |  |  |
                       |_ | _|
                       |  |  |
                       |__|__|
                       /-'Y'-\
                      (__/ \__)**


```

To align or position text inside the box, use the `-a` flag. Let’s demonstrate how this works with the following example (where the `c` means center).
```
**$ echo "Hey, this is Tecmint.com! Thanks for following us." | boxes -d diamonds**
**
       /\          /\          /\          /\          /\
    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\
 /\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\
//\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\
\\//\/Hey, this is Tecmint.com! Thanks for following us.  \/\\//
 \/                                                          \/
 /\                                                          /\
//\\                                                        //\\
\\//                                                        \\//
 \/                                                          \/
 /\                                                          /\
//\\/\                                                    /\//\\
\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\//
 \/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/
    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/
       \/          \/          \/          \/          \/**

```
```
**$ echo "Hey, this is Tecmint.com! Thanks for following us." | boxes -d diamonds -a c**

**       /\          /\          /\          /\          /\
    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\
 /\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\
//\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\
\\//\/                                                    \/\\//
 \/                                                          \/
 /\                                                          /\
//\\   Hey, this is Tecmint.com! Thanks for following us.   //\\
\\//                                                        \\//
 \/                                                          \/
 /\                                                          /\
//\\/\                                                    /\//\\
\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\//
 \/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/
    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/
       \/          \/          \/          \/          \/**

```

In the Christmas season, you can use the santa design to send your family and friends happy holiday messages, for example.
```
**$ echo "Tecmint.com wishes you a Merry Christmas and a Happy New Year 2019" | boxes -d santa**
**
                                 .-"``"-.
                                /______; \
                               {_______}\|
                               (/ a a \)(_)
                               (.-.).-.)
  _______________________ooo__(    ^    )___________________________
 /                             '-.___.-'                            \
| Tecmint.com wishes you a Merry Christmas and a Happy New Year 2019 |
 \________________________________________ooo_______________________/
                               |_  |  _|  jgs
                               \___|___/
                               {___|___}
                                |_ | _|
                                /-'Y'-\
                               (__/ \__)**

```

To list all available designs/styles, run the following command.
```
**$ boxes -l**

**59 Available Styles in "/etc/boxes/boxes-config":
-------------------------------------------------

ada-box
(public domain), coded by Neil Bird <neil.bird@rdel.co.uk>:

    ---------------
    --           --
    --           --
    ---------------


ada-cmt
(public domain), coded by Neil Bird <neil.bird@rdel.co.uk>:

    --
    -- regular Ada
    -- comments
...**

```

It supports line justification, box size specification, text padding, indentation, use of regular expressions and much more.
Valentine’s day coming closer, and you wanted to impress your girlfriend or wife in a Linux way, then use boxes as shown.
```
**$ echo -e "\n\tMe: Will you be my Valentine?\n\tGirl: No way\n\tMe: sudo will you be my Valentine?\n\tGirl: Yes..yes..yes! Let's go!" | boxes -d boy**
**
                        .-"""-.
                       / .===. \
                       \/ 6 6 \/
                       ( \___/ )
          _________ooo__\_____/_____________
         /                                  \
        |                                    |
        | Me: Will you be my Valentine?      |
        | Girl: No way                       |
        | Me: sudo will you be my Valentine? |
        | Girl: Yes..yes..yes! Let's go!     |
         \______________________ooo_________/
                       |  |  |
                       |_ | _|
                       |  |  |
                       |__|__|
                       /-'Y'-\
                      (__/ \__)**

```

For more information and examples, go to
**Boxes** is a command line utility that draws a box around its input text. In this article, we will learn how to install and use boxes utility to draw shapes in the Linux terminal. Use the feedback form below to share your thoughts about it.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[5 Useful Ways to Do Arithmetic in Linux Terminal](https://www.tecmint.com/arithmetic-in-linux-terminal/)
Next article:
[ext3grep – Recover Deleted Files on Debian and Ubuntu](https://www.tecmint.com/ext3grep-recover-deleted-files-on-ubuntu-debian/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/boxes-draws-ascii-art-boxes-in-linux-terminal/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### 2 Comments
[Leave a Reply](https://www.tecmint.com/boxes-draws-ascii-art-boxes-in-linux-terminal/#reply-title)
  1. These commands are not explained well for Linux beginners…
[Reply](https://www.tecmint.com/boxes-draws-ascii-art-boxes-in-linux-terminal/#comment-1706666)
  2. Mint Mate 20.1 does not like boxes especially using custom configuration **$HOME/.** boxes
The developer has no clue as to why it generates errors – Mint…
I wrote my own awk script to do basic box drawing
[Reply](https://www.tecmint.com/boxes-draws-ascii-art-boxes-in-linux-terminal/#comment-1596386)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/boxes-draws-ascii-art-boxes-in-linux-terminal/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/boxes-draws-ascii-art-boxes-in-linux-terminal/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
