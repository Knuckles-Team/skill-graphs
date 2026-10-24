[Skip to content](https://www.tecmint.com/cloc-count-lines-of-code-in-linux/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/cloc-count-lines-of-code-in-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/cloc-count-lines-of-code-in-linux/)
While working on different projects, sometimes you might be required to provide a report or statistics of your progress, or simply to calculate the value of your code.
There is this simple yet powerful tool called “**cloc – count lines of code** ” that allows you to count all number of your code and exclude comments and blank lines at the same time.
It is available in all major Linux distributions and supports multiple programming languages and file extensions and does not have any specific requirements to be used.
In this tutorial you are going to learn how to install and use **cloc** on your Linux system.
### How to Install and Use Cloc in Linux Systems
Installing **cloc** is easy and simple. Below you can see how to install cloc in different operating systems with their related package managers:
```
$ sudo apt install cloc                  # Debian, Ubuntu
$ sudo yum install cloc                  # Red Hat, Fedora
$ sudo dnf install cloc                  # Fedora 22 or later
$ sudo pacman -S cloc                    # Arch
$ sudo emerge -av dev-util/cloc          # Gentoo https://packages.gentoo.org/packages/dev-util/cloc
$ sudo apk add cloc                      # Alpine Linux
$ sudo pkg install cloc                  # FreeBSD
$ sudo port install cloc                 # Mac OS X with MacPorts
$ brew install cloc                      # Mac OS X with Homebrew
$ npm install -g cloc                    # https://www.npmjs.com/package/cloc

```

**Cloc** can be used to [count lines in particular file](https://www.tecmint.com/wc-command-examples/) or in multiple files within directory. To use **cloc** simply type **cloc** followed by the file or directory which you wish to examine.
Here is an example from a file in bash. The file in question contains the following code in bash:
```
$ cat bash_script.sh

```
![Linux Bash Script](https://www.tecmint.com/wp-content/uploads/2018/10/Linux-Bash-Script.png)Linux Bash Script
Now lets run cloc on it.
```
$ cloc bash_script.sh

```
![Count Lines in File](https://www.tecmint.com/wp-content/uploads/2018/10/Count-Lines-in-File.png)Count Lines in File
As you can see it counted the number of files, blank lines, comments and lines of code.
Another cool feature of **cloc** is that can even be used on compressed files. For example, I have downloaded the latest WordPress archive and ran **cloc** on it.
```
$ cloc latest.tar.gz

```

Here is the result:
![Count Lines on Compressed File](https://www.tecmint.com/wp-content/uploads/2018/10/Count-Lines-on-Compressed-File.png)Count Lines on Compressed File
You can see that it recognizes the different types of code and separates the stats per language.
In case you need to get a report for multiple files in a directory you can use `“--by-file”` option, that will count the lines in each file and provide a report for them. This may take a while for projects with many files and thousands of lines of code.
The syntax is as follows:
```
$ cloc --by-file <directory>

```
![Count Lines on Multiple Files](https://www.tecmint.com/wp-content/uploads/2018/10/Count-Lines-on-Multiple-Files.png)Count Lines on Multiple Files
While the help of **cloc** is easily readable and understandable, I will include some of the extra options that can be used with **cloc** some users may find useful.
  * `--diff <set1> <set2>` – computes the differences in code between the source files of **set1** and **set2**. The input can be a mix of files and directories.
  * `--git` – forces the inputs to be recognized as git targets if the same are not first identified as file or directory names.
  * `--ignore-whitespace` – ignores the horizontal whitespace when comparing files with `--diff`.
  * `--max-file-size=<MB>` – if you want to skip files larger than the given amount MB.
  * `--exclude-dir=<dir1>,<dir2>` – exclude given comma separated directories.
  * `--exclude-ext=<ext1>,<ext2>` – exclude the given file extensions.
  * `--csv` – export results to CSV file format.
  * `--csv-delimiter=<C>` – use the character `<C>` as the delimiter.
  * `--out=<file>` – save the results to `<file>`.
  * `--quiet` – suppress all information messages and show only the final report.
  * `--sql=<file>` – write the results as create and insert statements that can be read by a database program such as SQLite.


##### Conclusion
**Cloc** is a little useful utility that is definitely good to have in your arsenal. While it may not be used on a daily basis, it can help you when you have to generate some report or if you are just curious how is your project going.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Limit File Download Speed Using Wget in Linux](https://www.tecmint.com/wget-limit-file-download-speed-in-linux/)
Next article:
[How to Install and Use Chrony in Linux](https://www.tecmint.com/install-chrony-in-centos-ubuntu-linux/)
![Photo of author](https://secure.gravatar.com/avatar/ea5f34ca326c00e992815e5c34104204b0b3bead372195de9eadbcb05880f786?s=100&d=blank&r=g)
Marin Todorov
I am a bachelor in computer science and a Linux Foundation Certified System Administrator. Currently working as a Senior Technical support in the hosting industry. In my free time I like testing new software and inline skating.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/cloc-count-lines-of-code-in-linux/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### 3 Comments
[Leave a Reply](https://www.tecmint.com/cloc-count-lines-of-code-in-linux/#reply-title)
  1. Looks like `'debian install npm'` is a pretty common search for devs trying to set up Node.js on Debian. Since npm is the default package manager for Node.js, it’s essential for installing and managing JavaScript packages.
Super useful if you’re starting with JS or building anything Node-related!
[Reply](https://www.tecmint.com/cloc-count-lines-of-code-in-linux/#comment-2329707)
  2. There is a new tool out, Loci.
Written entirely in nodejs, it produces similar results to **Cloc** , but in less time. It doesn’t have some of the value-added features, like Diff or in-archive scanning.
It is useful in a tightly controlled network where you can’t run an executable (like cloc.exe) or have access to Perl scripts (cloc.pl) but have nodejs.
[Reply](https://www.tecmint.com/cloc-count-lines-of-code-in-linux/#comment-1695562)
  3. So interesting article, I am a bank`s specialist system area, and we are searching for a tool to improve our numbers.
thanks
[Reply](https://www.tecmint.com/cloc-count-lines-of-code-in-linux/#comment-1149607)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/cloc-count-lines-of-code-in-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/cloc-count-lines-of-code-in-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
