[Skip to content](https://www.tecmint.com/install-arduino-ide-on-linux/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/install-arduino-ide-on-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/install-arduino-ide-on-linux/)
**Arduino** is a widely-used, open-source electronics platform used to create devices that interact with their environment using sensors and actuators. It consists of a programmable hardware board and a software (**Integrated Development Environment(IDE)**) for writing and uploading programs to the board.
Before you can start building projects using **Arduino** , you need to set up the **IDE** to program your boards. The **Arduino (IDE)** is a free open-source and cross-platform desktop application that allows you to write code and upload it to the board. It runs on Linux, Windows, and Mac OS X, and Linux.
In this article, we will explain how to install the latest version of the Arduino Software (IDE) on Linux machines.
### Installing Arduino IDE on Linux Systems
The **Arduino Software (IDE)** is a package that does not require any particular process for the various Linux distributions. The only needed requirement is the 32-bit or 64-bit version of the operating system.
#### Download the Arduino Software (IDE)
Go to the **Arduino Software (IDE)** for your supported system architecture. You can choose between the 32-bit, 64-bit, and ARM versions, as it is very crucial to select the right version for your Linux distribution.
Alternatively, you can use the following [wget command](https://www.tecmint.com/10-wget-command-examples-in-linux/) to download the Arduino Software (IDE) package directly on the terminal.
```
$ wget https://downloads.arduino.cc/arduino-1.8.12-linux64.tar.xz

```
![Download Arduino IDE in Linux](https://www.tecmint.com/wp-content/uploads/2020/02/Download-Arduino-IDE-in-Linux.png)Download Arduino IDE in Linux
Next, extract the downloaded archive file using the [tar command](https://www.tecmint.com/18-tar-command-examples-in-linux/).
```
$ tar -xvf arduino-1.8.12-linux64.tar.xz

```
![Extract Arduino IDE in Linux](https://www.tecmint.com/wp-content/uploads/2020/02/Extract-Arduino-IDE-in-Linux.png)Extract Arduino IDE in Linux
#### Run Arduino IDE Install Script
Now move into the extracted `arduino-1.8.12` directory and run the installation script with root privileges as shown.
```
$ cd arduino-1.8.12/
$ sudo ./install.sh

```
![Install Arduino IDE in Linux](https://www.tecmint.com/wp-content/uploads/2020/02/Install-Arduino-IDE-in-Linux.png)Install Arduino IDE in Linux
Once the installation is done, a desktop icon will be created on your desktop, to launch the IDE, double click on it.
![Running Arduino IDE in Linux](https://www.tecmint.com/wp-content/uploads/2020/02/Running-Arduino-IDE-in-Linux.png)Running Arduino IDE in Linux
It might happen that, you will get an error “**Error opening serial port** ” while uploading a sketch after you have selected your board and the serial port. To fix this error, run the following command (replace `tecmint` with your username).
```
$ sudo usermod -a -G dialout tecmint

```

Besides, if you have a good internet connection, you can use the
That’s it for now! For more information and advanced usage instructions, see the
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[eXtern OS – A NodeJS Based Linux Distribution](https://www.tecmint.com/externos-nodejs-based-linux-distribution/)
Next article:
[How to Install Google Chrome on Kali Linux](https://www.tecmint.com/install-google-chrome-on-kali-linux/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/install-arduino-ide-on-linux/#respond)** or
## Related Posts
[![Best Notepad++ Alternatives For Linux](https://www.tecmint.com/wp-content/uploads/2019/04/Best-Notepad-Alternatives-For-Linux.png)](https://www.tecmint.com/best-notepad-alternatives-for-linux/ "16 Best Notepad++ Alternatives for Linux in 2025")
[![Learn Emacs Editor](https://www.tecmint.com/wp-content/uploads/2024/03/Learn-Emacs-Editor.webp)](https://www.tecmint.com/emacs-text-editor/ "Emacs 30.1 Released: New Features, Installation, and Usage Guide")
[![Nano Syntax Highlighting](https://www.tecmint.com/wp-content/uploads/2024/11/Nano-Syntax-highlighting.webp)](https://www.tecmint.com/nano-editor-syntax-highlighting/ "How to Use Syntax Highlighting in Nano Editor")
[![Etherpad - Collaborative Document Editor for Linux](https://www.tecmint.com/wp-content/uploads/2013/12/Etherpad-collaborative-document-editor-for-Linux.webp)](https://www.tecmint.com/etherpad-collaborative-document-editor-for-linux/ "Etherpad: A Real-Time Online Collaborative Document Editor")
[![Learn Vi/Vim Editor in Linux](https://www.tecmint.com/wp-content/uploads/2015/09/Learn-vi-and-vim-editor-in-linux.png)](https://www.tecmint.com/how-to-use-vi-and-vim-editor-in-linux/ "Vim Mastery Continues: 8 More Powerful Tips for Linux Admins \(Part 2\)")
[![Linux Vi and Vim Tricks and Tips](https://www.tecmint.com/wp-content/uploads/2015/09/Linux-Vi-Vim-Tricks-and-Tips.png)](https://www.tecmint.com/learn-vi-and-vim-editor-tips-and-tricks-in-linux/ "Learn Useful ‘Vi/Vim’ Tips and Tricks for Beginners – Part 1")
### 3 Comments
[Leave a Reply](https://www.tecmint.com/install-arduino-ide-on-linux/#reply-title)
  1. I have just switched to Linux from Windows and have set up the Arduino IDE. However when I try to access the program manager I get:
`Error downloading https://downloads.arduino.cc/libraries/library_index.json`
Any ideas, please?
[Reply](https://www.tecmint.com/install-arduino-ide-on-linux/#comment-1588846)
  2. Well, correction – your solution ‘**usermod** ‘ command DID WORK for me after all.
Problem was, I had to LOG OUT (user) then log in again. THEN it worked.
Thanks very much !!
[Reply](https://www.tecmint.com/install-arduino-ide-on-linux/#comment-1411013)
  3. Running Slackware 14.2 64-bit with Arduino 1.8.3 gives the ‘**serial port error** ‘ described above. Adding group ‘**dialout** ‘ does not work – ‘**usermod** ‘ command just returns (as root); then users ‘groups’ are still not changed. So cannot use arduino apparently.
[Reply](https://www.tecmint.com/install-arduino-ide-on-linux/#comment-1410999)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/install-arduino-ide-on-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/install-arduino-ide-on-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=8650516707490125&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
