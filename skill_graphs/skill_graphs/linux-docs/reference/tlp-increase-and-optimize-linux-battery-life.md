[Skip to content](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/ "Linux Online Courses")
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


[](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/)
**TLP** is a free open-source, feature-rich, and command-line tool for advanced power management, which helps to optimize battery life in laptops powered by Linux.
It runs on every laptop brand, and ships in with a default configuration already tuned to effectively and reliably maintain battery life, so you can simply install and use it.
It performs power saving by allowing you to configure how devices such as CPU, disk, USBs, PCIs, and radio devices should utilize power when your laptop is running on battery.
#### TLP Features:
  * It is highly configurable through various power-saving parameters.
  * It uses automated background tasks.
  * Uses kernel laptop mode and dirty buffer timeouts.
  * Supports processor frequency scaling including “turbo boost” and “turbo core”.
  * Has a power-aware process scheduler for multi-core/hyper-threading.
  * Provides for runtime power management for PCI(e) bus devices.
  * PCI Express active state power management (PCIe ASPM).
  * Supports radeon graphics power management (KMS and DPM).
  * Has an I/O scheduler (per disk).
  * Offers USB autosuspend with blacklist.
  * Supports Wifi power saving mode.
  * Also offers an Audio power-saving mode.
  * Offers hard disk advanced power management level and spin-down timeout (per disk).
  * Also supports SATA aggressive link power management (ALPM) and so much more.


### How to Install TLP Battery Management Tool in Linux
**TLP** package can be easily installed on **Ubuntu** as well as the corresponding **Linux Mint** using the **TLP-PPA** repository as shown.
```
sudo add-apt-repository ppa:linrunner/tlp
sudo apt update
sudo apt install tlp tlp-rdw

```

On **Debian** , the newer TLP packages are available via the official Debian repositories. Add the following line to your **/etc/apt/sources.list** file.
```
deb http://ftp.debian.org/debian DIST-backports main

```

and then update the system package cache and install it.
```
sudo apt update
sudo apt install tlp tlp-rdw

```

On **RHEL** , **Arch Linux,** and **OpenSUSE** , execute the following command as per your distribution.
```
dnf install tlp tlp-rdw     [On RHEL]
pacman -S tlp  tlp-rdw      [On Arch Linux]
zypper install tlp tlp-rdw  [On OpenSUSE]

```

### How to Use TLP to Optimize Battery Life in Linux
Once you have installed **TLP** , its configuration file is **/etc/default/tlp** and you will have the following commands to use:
  * **tlp** – apply laptop power saving settings
  * **tlp-stat** – displays all power-saving settings
  * **tlp-pcilist** – displays PCI(e) device data
  * **tlp-sublist** – for viewing USB device data


It should start automatically as a service, you can check if it is running under SystemD using the [systemctl command](https://www.tecmint.com/manage-services-using-systemd-and-systemctl-in-linux/).
```
$ sudo systemctl status tlp

```

After the service starts running, you have to restart the system to actually start using it. But you can prevent this by manually applying the current laptop power saving settings with root privileges using the [sudo command](https://www.tecmint.com/su-vs-sudo-and-how-to-configure-sudo-in-linux/), like so.
```
$ sudo tlp start

```

Afterward, confirm that it is running using the following command, which actually shows system information and TLP status.
```
$ sudo tlp-stat -s

```
![Show System and TLP Information](https://www.tecmint.com/wp-content/uploads/2018/01/Show-System-Information.png)Show System and TLP Information
**Important** : As we mentioned before, it uses automated background tasks but you will not see any TLP background process or daemon in [ps command](https://www.tecmint.com/ps-command-examples-for-linux-process-monitoring/) output.
To view the current TLP configuration, run the following command with `-c` option.
```
$ sudo tlp-stat -c

```
![Show TLP Configuration](https://www.tecmint.com/wp-content/uploads/2018/01/Show-TLP-Configuration.png)Show TLP Configuration
To display all power settings run the following command.
```
$ sudo tlp-stat

```
![Show Power Saving Settings](https://www.tecmint.com/wp-content/uploads/2018/01/show-power-saving-settings.png)Show Power Saving Settings
To display Linux battery information, run the following command with `-b` switch.
```
$ sudo tlp-stat -b

```
![Show Linux Battery Information](https://www.tecmint.com/wp-content/uploads/2018/01/show-battery-information.png)Show Linux Battery Information
To display the Temperatures and Fan Speed of the system, run the following command with `-t` switch.
```
$ sudo tlp-stat -t

```
![Show CPU Temperature and Fan Speed](https://www.tecmint.com/wp-content/uploads/2018/01/show-cpu-temp-and-fan-speed.png)Show CPU Temperature and Fan Speed
To display Processor Data, run the following command with `-p` switch.
```
$ sudo tlp-stat -p

```
![Show Processor Data](https://www.tecmint.com/wp-content/uploads/2018/01/show-processor-data.png)Show Processor Data
To display any Warnings, run the following command with `-w` switch.
```
$ sudo tlp-stat -w

```

**Note** : If you are using **ThinkPad** , there are certain specific packages you need to install for your distribution, that you can check from the
**[ You might also like:[PowerTop – Monitors Power Usage and Improve Battery Life](https://www.tecmint.com/powertop-monitors-linux-laptop-battery-usage/) ]**
**TLP** is a useful tool for all laptops powered by Linux operating systems. Give us your thoughts about it via the comment form below, and you can let us know of any other similar tools you have come across as well.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[6 Best Whiteboard Applications for Your Linux Systems](https://www.tecmint.com/linux-whiteboard-applications/)
Next article:
[PowerTop – Monitors Power Usage and Improve Laptop Battery Life](https://www.tecmint.com/powertop-monitors-linux-laptop-battery-usage/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#respond)** or
## Related Posts
[![LocalSend Share Files Between Linux and Windows](https://www.tecmint.com/wp-content/uploads/2016/09/localsend-share-files-between-linux-and-windows.webp)](https://www.tecmint.com/localsend-share-files-linux-windows/ "LocalSend – Local Network File Sharing Between Linux, Windows and Mac")
[![Why the Modern World Runs on Linux](https://www.tecmint.com/wp-content/uploads/2014/02/Why-Modern-World-Runs-on-Linux.webp)](https://www.tecmint.com/why-the-world-runs-on-linux/ "Why Linux Powers Everything From Your Coffee Machine to Mars Rovers")
[![introduction to makefiles gnu make in Linux](https://www.tecmint.com/wp-content/uploads/2014/03/introduction-to-makefiles-gnu-make.webp)](https://www.tecmint.com/introduction-to-makefiles-gnu-make/ "A Brief Introduction to Makefiles and GNU Make for Beginners")
[![mkcert: Make Locally-Trusted Development Certificates on Linux](https://www.tecmint.com/wp-content/uploads/2025/07/mkcert-Create-Trusted-SSL-Certificates-for-Local-Development.webp)](https://www.tecmint.com/mkcert-create-ssl-certs-for-local-development/ "mkcert: Make Locally-Trusted Development Certificates on Linux")
[![Fix Kernel Panic in Linux](https://www.tecmint.com/wp-content/uploads/2013/12/Fix-Kernel-Panic-in-Linux.webp)](https://www.tecmint.com/fix-kernel-panic-linux/ "How to Trigger and Fix a Linux Kernel Panic")
[![LogKey - Monitor Keyboard Keystrokes in Linux](https://www.tecmint.com/wp-content/uploads/2014/01/LogKeys-Monitor-Keyboard-Keystrokes-in-Linux.webp)](https://www.tecmint.com/logkeys-monitor-keyboard-keystroke-linux/ "LogKeys: Monitor Keyboard Keystrokes in Linux")
### 22 Comments
[Leave a Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#reply-title)
  1. Very good indeed, but, care to explain where and how to edit the configuration file or files?
Thanks in advance.
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-2205059)
     * @Ceaualbi,
Thank you for your feedback!
To edit the configuration file for **TLP** , you’ll need to open the **/etc/tlp.conf** file and make this changes in the file, and don’t forget to restart TLP to apply the new settings.
```
sudo systemctl restart tlp

```
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-2205250)
  2. Hi,
```
tlp-sublist – for viewing USB device data

```

must be
```
tlp-usblist – for viewing USB device data

```

thanks for good article
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-2133171)
  3. +++ Battery Status
/sys/class/power_supply/BAT1/manufacturer = PAC
/sys/class/power_supply/BAT1/model_name = CP700280-01
/sys/class/power_supply/BAT1/cycle_count = 61
/sys/class/power_supply/BAT1/charge_full_design = 4500 [mAh]
/sys/class/power_supply/BAT1/charge_full = 4333 [mAh]
/sys/class/power_supply/BAT1/charge_now = 2024 [mAh]
/sys/class/power_supply/BAT1/current_now = 0 [mA]
/sys/class/power_supply/BAT1/status = Charging
Charge = 46.7 [%]
Capacity = 96.3 [%]
The battery is not charging, and the laptop turns off when the charger is disconnected. Tried removing, putting it back, etc. What can be the reason? “current now” here shows “0”.
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-1614026)
  4. So I just have to install it and reboot to get it working right?
I am having an Acer Aspire 315-51z
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-1336018)
     * @Anirudh,
No need to reboot, just start the **tlp** service using the following command.
```
$ sudo systemctl status tlp

```
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-1336162)
  5. All these tools does is cause a flurry of SELinux messages. I very quickly got tired of SENotify pinging me with messages every 3-4 minutes, so I removed TLP.
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-1335558)
  6. Hi,
Does anybody knows how to handle tlp with audio in battery mode.
When the laptop is connected to the power the audio is ok, but after a while in battery mode the laptop remains without audio. When it gets again the 100% of battery connected to the power the laptop recovers the audio.
I have selected regarding the audio settings:
```
SOUND_POWER_SAVE_ON_AC=0
SOUND_POWER_SAVE_ON_BAT=0
SOUND_POWER_SAVE_CONTROLLER=N

```

With these I try to remove the control to TLP for audio purposes, but even with that configuration on battery mode I have no audio.
Thanks
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-1096154)
     * @Alberto
Take a look at the TLP settings for audio:
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-1096320)
  7. I am using **Ubuntu 18.04**. I am facing a LAN connection problem. The problem is when I start my laptop it will connect to the LAN but once I disconnect it it won’t reconnect. Then I will have to put the laptop in sleep mode and then it would reconnect.
Every time I reinstalled Ubuntu and the problem didn’t showed up for the first 3-4 days and then again the same problem happens. But this time I think I have figured out the reason behind this. there was no issue till today when I installed tlp and started it.
Only after tlp it showed the same problem again. I googled and got to know that tlp activation changes some settings in order to save battery. Is it possible that tlp is the culprit. If so is there any way I can disable a particular setting so that tlp keeps working and I get rid of the problem. And yes I have my laptop dual booted with windows 10 and there is no such issue in windows 10. So certainly it is specific to Ubuntu. I think I have to change some settings. Can someone please help
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-1047280)
  8. The TLP module appears to be the cause of problems with Intel network drivers. You could tell me how to stop the service by restoring the options of Default???
TLP Start | true | bat | false | ac | usb | bayoff | discharge | setcharge | fullcharge | recalibrate | stat | diskid
Seems to keep settings also removed the tool
Several users on Fedora and not only report problems to Intel network card drivers and the cause is TLP
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-988824)
     * @IVA
I have read through the thread but didn’t see any one directly mention TLP module as the cause of problems with Intel network drivers, although some answers have stressed about disabling Active-State Power Management but not connection with TLP.
You can completely remove it, including config files with this command:
$sudo apt-get purge tlp tlp-rdw
Once you have removed it, try to check if the cause of problems with Intel network drivers was actually TLP, and give us some feedback.
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-988952)
       * Look I ran in doubt a clean installation of Fedora 28 without TLP… No problem…..
The problem arise the next reboot after the installation of TLP…… Is that and since it is no longer installed I see no more error reported!!!!
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-989012)
         * @Ivan
Okay, it could have caused the problems with Intel network drivers, which your were facing and other Fedora users. And by the way, the correct command for removing it on Fedora is:
#dnf remove tlp tlp-rdw
Thanks for the feedback, we will update this article to include this issue. You can also raise this issue to the developer via:
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-989168)
           * Also removed the settings given to the kernel remain, otherwise I think until there I would have arrived….
The developer is already a week knows of the problem from me reported on GIT!!!!!
Anyway we Blog I follow you very much!!!!
     * I don’t know how to stop certain service on Fedora, but on Ubuntu you would run ‘**sudo systemctl stop tlp** ‘.
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-1100309)
  9. Hi,
I used tlp on my ubuntu 16.04 partitioned with LVM, it causes me a lot of system crashes, which force me to hard reset laptop on each crash.
Does any one have idea about this issue ?
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-958789)
     * @cortexdz
Try contacting the developers by posting the issue here:
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-958796)
  10. Under lubuntu 16.04 lts, can xfce power manager and tlp coexist? if not how to disable xfce power manager?
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-958409)
     * @Jai
Try to go to Session and Startup->Application Autostart, then locate Power Manager in the list and uncheck it. If you fail to find it, you can check the documentation for xfce.
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-958714)
       * I already tried through “Default applications for LXSession->LXSession configuration->Autostart, uncheked power manager” as Admin user and normal user. It is not making any difference. Xfce Power manager always present.
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-958879)
         * @Jai
Try to contact the developers of Xfce, possibly on via the project homepage:
[Reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#comment-959314)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/tlp-increase-and-optimize-linux-battery-life/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=1102348856092499&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
