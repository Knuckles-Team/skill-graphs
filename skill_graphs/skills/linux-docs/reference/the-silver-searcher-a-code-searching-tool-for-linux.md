[Skip to content](https://www.tecmint.com/the-silver-searcher-a-code-searching-tool-for-linux/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/the-silver-searcher-a-code-searching-tool-for-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/the-silver-searcher-a-code-searching-tool-for-linux/)
**The Silver Searcher** is a free and open source, cross platform source code searching tool similar to **ack** (a [grep-like tool](https://www.tecmint.com/12-practical-examples-of-linux-grep-command/) for programmers) but faster. It runs on Unix-like systems and Windows operating systems.
The major difference between the **silver searcher** and **ack** is that the former is designed for speed, and benchmark tests prove that it is indeed faster.
If you spend a lot of time reading and searching through your code, then you need this tool. It aims at being fast and ignoring files that you don’t want to be searched. In this guide, we will show how to install and use **The Silver Searcher** in **Linux**.
### How to Install and Use The Silver Searcher in Linux
The **silver searcher** package is available on most Linux distributions, you can easily install it via your package manager as shown.
```
$ sudo apt install silversearcher-ag					#Debian/Ubuntu
$ sudo yum install epel-release the_silver_searcher		        #RHEL/CentOS
$ sudo dnf install silversearcher-ag					#Fedora 22+
$ sudo zypper install the_silver_searcher				#openSUSE
$ sudo pacman -S the_silver_searcher           				#Arch

```

After installing it, you can run the **ag** command line tool with the following syntax.
```
$ ag file-type options PATTERN /path/to/file

```

To see a list of all supported file types, use the following command.
```
$ ag  --list-file-types

```

This example shows how to recursively search for all scripts that contain the word **“root”** under the directory **~/bin/**.
```
$ ag root ./bin/

```
![Search a Pattern in Files](https://www.tecmint.com/wp-content/uploads/2018/10/search-a-pattern-in-files-using-ag.png)Search a Pattern in Files
To print the filenames matching **PATTERN** and the number of matches in each file, other than the number of matching lines, use the `-c` switch as shown.
```
$ ag -c root ./bin/

```
![Print Number of Matches](https://www.tecmint.com/wp-content/uploads/2018/10/only-print-number-of-matches-in-each-line.png)Print Number of Matches
To match case-sensitively, add the `-s` flag as shown.
```
$ ag -cs ROOT ./bin/
$ ag -cs root ./bin/

```
![Match Case Sensitive](https://www.tecmint.com/wp-content/uploads/2018/10/match-case-senstively.png)Match Case Sensitive
To print statistics of of a search operation such as files scanned, time taken, etc., use the the `--stats` option.
```
$ ag -c root --stats ./bin/

```
![Print Search Operations Summary](https://www.tecmint.com/wp-content/uploads/2018/10/print-search-operation-stats.png)Print Search Operations Summary
The `-w` flag tells **ag** to only match whole words similar to [grep command](https://www.tecmint.com/linux-grep-commands-character-classes-bracket-expressions/).
```
$ ag -w root ./bin/

```

You can show column numbers in results using the `--column` option.
```
$ ag --column root ./bin/

```
![Show Column Numbers in Output](https://www.tecmint.com/wp-content/uploads/2018/10/show-column-numbers-in-output.png)Show Column Numbers in Output
You can also use **ag** to search through purely text files, using the `-t` switch and the `-a` switch is used to search all types of files. In addition, the `-u` switch enables searching though all files, including hidden files.
```
$ ag -t root /etc/
OR
$ ag -a root /etc/
OR
$ ag -u root /etc/

```

**Ag** also supports searching through the contents of compressed files, using the `-z` flag.
```
$ ag -z root wondershaper.gz

```
![Search Content in Compressed Files](https://www.tecmint.com/wp-content/uploads/2018/10/search-content-of-compressed-files.png)Search Content in Compressed Files
You can also enable following of symbolic links (symlinks in short) with the `-f` flag.
```
$ ag -tf root /etc/

```

By default, **ag** searches **25** directories deep, you can set the depth of the search using the `--depth` switch, for example.
```
$ ag --depth 40 -tf root /etc/

```

For more information, see the silver searcher’s man page for a complete list of usage options.
```
$ man ag

```

To find out, how the silver searcher works, see its Github repository:
That’s it! **The Silver Searcher** is a fast, useful tool for searching through files that make sense to search. It is intended for programmers for quickly searching though large source-code base. You can give it a try and share your thoughts, with us via the comment form below.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[10 tr Command Examples in Linux](https://www.tecmint.com/tr-command-examples-in-linux/)
Next article:
[Bat – A Cat Clone with Syntax Highlighting and Git Integration](https://www.tecmint.com/bat-a-cat-clone-with-syntax-highlighting/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/the-silver-searcher-a-code-searching-tool-for-linux/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/the-silver-searcher-a-code-searching-tool-for-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/the-silver-searcher-a-code-searching-tool-for-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
