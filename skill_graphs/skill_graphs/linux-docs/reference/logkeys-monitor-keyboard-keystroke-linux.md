[Skip to content](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/)
**Keylogging** , short for “**keystroke logging** ” is the process of recording the keys struck on a keyboard, usually without the user’s knowledge.
Keyloggers can be implemented via hardware or software:
  * Hardware keyloggers intercept data at the physical level (e.g., between the keyboard and computer).
  * Software keyloggers, like **LogKeys** , capture keystrokes through the operating system.


This article explains how to use a popular open-source Linux keylogger called **LogKeys** for educational or testing purposes only. Unauthorized use of keyloggers to monitor someone else’s activity is unethical and illegal.
## What is LogKeys?
**LogKeys** is an open-source keylogger for Linux that captures and logs keyboard input, including characters, function keys, and special keys. It is designed to work reliably across a wide [range of Linux systems](https://www.tecmint.com/top-most-popular-linux-distributions/ "Popular Linux Distributions") without crashing the X server.
LogKeys also correctly handles modifier keys like `Alt` and `Shift`, and is compatible with both USB and serial keyboards.
While there are numerous keylogger tools available for **Windows** , **Linux** has fewer well-supported options. Although **LogKeys** has not been actively maintained since 2019, it remains one of the more stable and functional keyloggers available for Linux as of today.
## Installation of Logkeys in Linux
If you’ve previously installed Linux packages from a tarball (source), you should find installing the **LogKeys** package straightforward.
However, if you’ve never built a package from source before, you’ll need to install some required development tools first, such as **C++** compilers and **GCC** libraries, before proceeding.
### Installing Prerequisites
Before building **LogKeys** from source, ensure your system has the required development tools and libraries installed:
**On Debian/Ubuntu** :
```
sudo apt update
sudo apt install build-essential autotools-dev autoconf kbd

```

**On Fedora/CentOS/RHEL** :
```
sudo dnf install automake make gcc-c++ kbd

```

**On openSUSE** :
```
sudo zypper install automake gcc-c++ kbd

```

On **Arch Linux** :
```
sudo pacman -S base-devel kbd

```

### Installing LogKeys from Source
First, download the latest **LogKeys** source package using the [wget command](https://www.tecmint.com/10-wget-command-examples-in-linux/ "Download Files with Wget Command"), then, extract the ZIP archive and navigate into the extracted directory:
```
wget https://github.com/kernc/logkeys/archive/master.zip
unzip master.zip
cd logkeys-master/

```

or clone the repository using [Git](https://www.tecmint.com/git-basics/ "Learn the Basics of Git"), as shown below:
```
git clone https://github.com/kernc/logkeys.git
cd logkeys

```

Next, run the following commands to build and install **LogKeys** :
```
./autogen.sh         # Generate build configuration scripts
cd build                  # Switch to build directory
../configure              # Configure the build
make                      # Compile the source code
sudo make install         # Install binaries and man pages

```

If you encounter issues related to keyboard layout or character encoding, regenerate your locale settings:
```
sudo locale-gen

```

## Usage of LogKeys in Linux
Once **LogKeys** is installed, you can begin using it to monitor and log keyboard input using the following commands.
### Start Keylogging
This command starts the keylogging process, which must be run with superuser (root) privileges because it needs access to low-level input devices. Once started, **LogKeys** begins recording all keystrokes and saves them to the default log file: `/var/log/logkeys.log`.
**Note** : You won’t see any output in the terminal; logging runs silently in the background.
```
sudo logkeys --start

```

### Stop Keylogging
This command terminates the keylogging process that was started earlier, which is important to stop **LogKeys** when you’re done, both to conserve system resources and to ensure the log file is safely closed.
```
sudo logkeys --kill

```

### Get Help / View Available Options
The following command will displays all available command-line options and flags you can use with LogKeys.
```
logkeys --help

```

Useful options include:
  * `--start` : Start the logger
  * `--kill` : Stop the logger
  * `--output <file>` : Specify a custom log output file
  * `--no-func-keys` : Don’t log function keys (`F1-F12`)
  * `--no-control-keys` : Skip control characters (e.g., `Ctrl+C`, `Backspace`)


### View the Logged Keystrokes
The [cat command](https://www.tecmint.com/cat-command-linux/ "Cat View File Contents") displays the contents of the default log file where **LogKeys** saves keystrokes.
```
sudo cat /var/log/logkeys.log

```

You can also open it with a text editor like [nano](https://www.tecmint.com/learn-nano-text-editor-in-linux/ "How to Use Nano Text Editor in Linux") or `less`:
```
sudo nano /var/log/logkeys.log
or
sudo less /var/log/logkeys.log

```

## Uninstall LogKeys in Linux
To remove **LogKeys** from your system and clean up the installed binaries, manuals, and scripts, use the following commands:
```
cd build
sudo make uninstall

```

This will remove all files that were installed with make install, including the logkeys binary and man pages.
##### Conclusion
**LogKeys** is a powerful keylogger for Linux that enables users to monitor keystrokes in a variety of environments. Its compatibility with modern systems and ease of installation make it a valuable tool for security auditing, parental control testing, and educational research.
However, it’s crucial to emphasize that keylogging should only be used in ethical, lawful contexts—such as with explicit user consent or for personal system monitoring. Misuse can lead to serious legal consequences. Use responsibly and stay informed.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[15 Linux Interview Questions with Answers (Level Up) – Part 2](https://www.tecmint.com/linux-interview-questions-and-answers/)
Next article:
[10 Must-Know Linux Commands You Probably Missed – Part 4](https://www.tecmint.com/secret-linux-commands/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#respond)** or
## Related Posts
[![LocalSend Share Files Between Linux and Windows](https://www.tecmint.com/wp-content/uploads/2016/09/localsend-share-files-between-linux-and-windows.webp)](https://www.tecmint.com/localsend-share-files-linux-windows/ "LocalSend – Local Network File Sharing Between Linux, Windows and Mac")
[![Why the Modern World Runs on Linux](https://www.tecmint.com/wp-content/uploads/2014/02/Why-Modern-World-Runs-on-Linux.webp)](https://www.tecmint.com/why-the-world-runs-on-linux/ "Why Linux Powers Everything From Your Coffee Machine to Mars Rovers")
[![introduction to makefiles gnu make in Linux](https://www.tecmint.com/wp-content/uploads/2014/03/introduction-to-makefiles-gnu-make.webp)](https://www.tecmint.com/introduction-to-makefiles-gnu-make/ "A Brief Introduction to Makefiles and GNU Make for Beginners")
[![mkcert: Make Locally-Trusted Development Certificates on Linux](https://www.tecmint.com/wp-content/uploads/2025/07/mkcert-Create-Trusted-SSL-Certificates-for-Local-Development.webp)](https://www.tecmint.com/mkcert-create-ssl-certs-for-local-development/ "mkcert: Make Locally-Trusted Development Certificates on Linux")
[![Fix Kernel Panic in Linux](https://www.tecmint.com/wp-content/uploads/2013/12/Fix-Kernel-Panic-in-Linux.webp)](https://www.tecmint.com/fix-kernel-panic-linux/ "How to Trigger and Fix a Linux Kernel Panic")
[![Midori - Lightweight Linux Web Browser](https://www.tecmint.com/wp-content/uploads/2014/01/midori-lightweight-linux-browser.webp)](https://www.tecmint.com/midori-lightweight-linux-browser/ "Midori: Lightweight, Fast, and Privacy-Focused Web Browser for Linux")
### 29 Comments
[Leave a Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#reply-title)
  1. Hi, what if the remote terminal to which we have gained access does not have ‘**su** ‘, ‘**sudo** ‘, ‘**apt** ‘ commands enabled? How then can we install your script?
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-1359342)
  2. Does this work only on the terminal — or also on websites and such?
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-877847)
  3. Any insight on this issue —
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-871848)
  4. all is good but in the log file i see gibrish. i dont know but it looks like yours. any idea how to fix it?
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-779415)
     * You’ll need to fix the character mapping as explained here
(I realize this is an old post but in case someone else comes across your question)
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-1582478)
  5. I’m not getting anything when entering sudo locale-gen. It just says Generating locales (this may take a while) then Generation complete.
I’m running Kali 2 Distro
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-707246)
     * @Anthony,
That means the command executed successfully, then you can use following command start logging keys:
```
# logkeys ­s

```

You can Kill logkeys process by typing:
```
# logkeys ­k

```
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-707416)
  6. how to remove keylogger in cent os
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-704550)
     * @Amit,
If you’ve installed from source, just find and remove all files related to keylogger to complete remove it from system.
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-704985)
  7. hai can u let me know how to install Monitor Keyboard Keystrokes Using ‘LogKeys’ in centos 6.6
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-702107)
     * @Venu,
The given instructions in this article, will also works on CentOS 6.6. Have you tried the steps? let me know..
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-702119)
  8. Nice =), so far for my system security this happens when you boot my system without it’s special usb key i made for it….. automatically connects to nearest hotspot, connects to tor, enables sshd on tor as hidden service, pings my terminal via tor, starts capturing the screen via /dev/fb0 and takes pictures via the webcam and uploads them via tor to my terminal, 4 times a minute…. so having this makes the security so much more…… so many many thanks for such a useful things…. cheers….. __A
all that's missing now is package capture and mouse tracking….. bottom line, dont nick my laptop as i will be knocking on your door =)
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-677143)
  9. Nice and very helpful article. I have done all the steps as in the post and but my log file is empty. Your help is much appreciated .
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-538071)
  10. I tried installing logkeys in my vps Centos, but got the following error and could not find any solution :
===
checking for /dev/input… no
configure: error: Input event interface devices not found in expected location /dev/input/eventX !
===
please assist
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-469930)
     * try making the file at the specified location /dev/input/eventx manually with root permission and try to execute once again. Let us know.
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-472630)
  11. I don’t understand the tutorial. I get all the way to the last part and that’s where it gets confusing. The log file does not represent what I typed. Even the picture that you have showing does not represent what YOU typed either. I don’t understand how to read the log file or what’s going on here?
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-405919)
     * Dear Henrx its the raw data which you can not use directly.
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-472628)
  12. Thanks for the complete tutorial. It worked for me. But, how do we make the tracker automatically start every time?
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-394188)
     * You may write a script and make it start automatically at System Boot.
Here is the Process Algo.
1. Write Script
2. sudo mv /script /etc/init.d/
3. sudo chmod +x /etc/init.d/script
4. sudo update-rc.d script defaults
#Script should now start on boot.
The script would be very simple, which will just trigger the command!
Hope it Helps
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-394264)
       * what is the script to auto start the keylogger
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-702201)
         * @Amit,
You mean auto start keylogger at system boot? if yes, then add the following command to /etc/rc.local file to auto start at system boot..
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-702210)
  13. [root@localhost logkeys-0.1.1a]# locale-gen
bash: locale-gen: command not found
[root@localhost logkeys-0.1.1a]#
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-357221)
     * On which distro you’re trying?
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-357540)
  14. Er… Chris Jones.. that was… no “T”… :-)
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-168062)
     * Sorry chris unable to understand you.
will you be more clear please!
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-472631)
  15. I appreciate your effort. The problem as I see it is that at the end of the day logkeys provides heaps of raw data in a hard-to-read format. Not directly usable. Aren’t there any tools that can be run against a logkeys log file that give some idea of what you did during the day… (not limited to e.g.) stuff like… total number of key presses… total number of times each key was pressed… for each key pressed.. what percentage of the total it accounts for.. times when you were actually typing.. typing speed… total time you actually typed… etc. ? these are just a few examples of stuff that comes to mind without giving it much thought… so there’s surely a lot more… Naturally it would be nice to have the possibility to graph all those stats… If such tools are not available the only purpose of the logkeys program would appear to let someone with administrator privileges snoop on whatever other users of the system are typing.
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-167983)
     * hahaha
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-472632)
  16. hello
please replace
../configure > ./configure
locale-­gen > sudo locale-gen
logkeys ­s > sudo logkeys – s
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-127896)
     * Yeah! thanks for correcting, those were typos..:)
[Reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#comment-128143)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=1061414053440602&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
