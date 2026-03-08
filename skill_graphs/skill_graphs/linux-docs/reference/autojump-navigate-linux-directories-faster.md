[Skip to content](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/autojump-navigate-linux-directories-faster/ "Linux Online Courses")
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


[](https://www.tecmint.com/autojump-navigate-linux-directories-faster/)
Those Linux users who mainly work with Linux command Line via console/terminal feels the real power of Linux. However, it may sometimes be painful to navigate inside the [Linux Hierarchical file system](https://www.tecmint.com/linux-directory-structure-and-important-files-paths-explained/ "Linux Directory Structure"), especially for newbies.
There is a Linux command-line utility called **autojump** , which was written in Python by **Joël Schaerer** and now maintained by **+William Ting** , which is an advanced version of the [cd command](https://www.tecmint.com/cd-command-in-linux/).
**Autojump** is a command-line tool that offers a faster way to navigate the Linux file system by keeping the database of directories that the user visits frequently. It works by keeping an eye on the directories that the user navigates and then assigning importance to each directory based on how regularly the user visits.
This allows users to quickly jump to a frequently visited directory. Autojump navigates to the required directory more quickly as compared to the traditional cd command.
#### Features of autojump
  * Free and open source application and distributed under GPL V3
  * A self-learning utility that learns from the user’s navigation habit.
  * Faster navigation. No need to include the subdirectories’ names.
  * Available in the repository to be downloaded for [most of the standard Linux distributions](https://www.tecmint.com/best-linux-distributions-for-beginners/ "Linux Distributions for Beginners") including Debian, Ubuntu, Mint, Arch, Gentoo, Slackware, CentOS, RedHat, and Fedora.
  * Available for other platforms as well, like OS X (Using Homebrew) and Windows (enabled by Clink)
  * Using autojump you may jump to any specific directory or to a child directory. Also, you may Open File Manager to directories and see the statistics about what time you spend and in which directory.


### Step 1: Do a Full System Update
**1.** Do a system **Update** /**Upgrade** as a **root** user to ensure you have the latest version of **Python** installed.
```
# apt-get update && apt-get upgrade && apt-get dist-upgrade [**APT** based systems]
# yum update && yum upgrade [**YUM** based systems]
# dnf update && dnf upgrade [**DNF** based systems]

```

It is important to note here that, on **[YUM](https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/ "Yum Command in Linux")** or **[DNF-based](https://www.tecmint.com/dnf-commands-for-fedora-rpm-package-management/ "DNF Command in Linux")** systems, **update** and **upgrade** perform the same things and most of the time interchangeable, unlike **APT-based** systems.
### Step 2: Download and Install Autojump
**2.** As stated above, **autojump** is already available in the repositories of [most Linux distributions](https://www.tecmint.com/top-most-popular-linux-distributions/ "Most Popular Linux Distributions"). You may just install it using the **Package Manager**.
On [RedHat-based distributions](https://www.tecmint.com/redhat-based-linux-distributions/ "RedHat-based Linux Distributions"), you need to [enable the EPEL repository](https://www.tecmint.com/install-epel-repo-rhel-rocky-almalinux/ "Install EPEL Repository in Linux") by running `yum install epel-release` command.
#### Install Autojump from Repositories
```
$ sudo apt install autojump      [On **Debian, Ubuntu and Mint**]
$ sudo yum install autojump       [On **RHEL/CentOS/Fedora** and **Rocky/AlmaLinux**]
$ sudo emerge -a autojump        [On **Gentoo Linux**]
$ sudo apk add autojump          [On **Alpine Linux**]
$ sudo pacman -S autojump        [On **Arch Linux**]
$ sudo zypper install autojump   [On **OpenSUSE**]

```

However, if you want to install **autojump** from the source, you need to clone the source code and execute the **Python** script, as:
#### Installing Autojum from Source
Install **git** , if not installed, which is required to clone the **autojump** git repository.
```
$ sudo apt install git      [On **Debian, Ubuntu and Mint**]
$ sudo yum install git      [On **RHEL/CentOS/Fedora** and **Rocky/AlmaLinux**]
$ sudo emerge -a git        [On **Gentoo Linux**]
$ sudo apk add git          [On **Alpine Linux**]
$ sudo pacman -S git        [On **Arch Linux**]
$ sudo zypper install git   [On **OpenSUSE**]

```

Once **git** has been installed, log in as **normal** user and then clone **autojump** as:
```
$ git clone git://github.com/joelthelion/autojump.git

```

Next, switch to the downloaded directory using the **cd** command.
```
$ cd autojump

```

Now, make the script file executable and run the install script as the **root** user.
```
# chmod 755 install.py
# ./install.py

```

### Step 3: Autojump Configuration
**3.** On [Debian and its derivatives](https://www.tecmint.com/debian-based-linux-distributions/ "Best Debian-based Linux Distributions") (**Ubuntu** , **Mint** ,…), it is important to activate the **autojump** utility.
To activate the **autojump** utility temporarily, i.e., effective till you close the current session, or open a new session, you need to run the following commands as a **normal** user:
```
$ source /usr/share/autojump/autojump.sh on startup
OR
$ source /usr/share/autojump/autojump.bash on startup

```

To permanently add activation to the **BASH** shell, you need to run the below command.
```
$ echo '. /usr/share/autojump/autojump.sh' >> ~/.bashrc
Or
$ echo '. /usr/share/autojump/autojump.bash' >> ~/.bashrc

```

### Step 4: Quickly Change Linux Directory Using Autojump
**4.** As said earlier, **autojump** will jump to only those directories which have been `cd` earlier. So before we start testing we are going to ‘**cd** ‘ a few directories and create a few as well.
Here is what I did.
```
$ cd
$ cd
$ cd Desktop/
$ cd
$ cd Documents/
$ cd
$ cd Downloads/
$ cd
$ cd Music/
$ cd
$ cd Pictures/
$ cd
$ cd Public/
$ cd
$ cd Templates
$ cd
$ cd /var/www/
$ cd
$ mkdir autojump-test/
$ cd
$ mkdir autojump-test/a/ && cd autojump-test/a/
$ cd
$ mkdir autojump-test/b/ && cd autojump-test/b/
$ cd
$ mkdir autojump-test/c/ && cd autojump-test/c/
$ cd

```

Now we have a **cd** to the above directory and created a few directories for testing, we are ready to go.
The usage of `j` is a wrapper around autojump. You may use **j** in place of the **autojump** command and vice versa.
**5.** Check the version of installed autojump using `-v` option.
```
$ j -v
or
$ autojump -v

```
![Check Autojump Version](https://www.tecmint.com/wp-content/uploads/2015/06/Check-Autojump-Version.png)Check Autojump Version
**6.** Jump to a previously visited directory ‘**/var/www** ‘.
```
$ j www

```
![Jump To Directory](https://www.tecmint.com/wp-content/uploads/2015/06/Jump-To-Directory.png)Jump To Directory
**7.** Jump to the previously visited parent/child directory ‘**/home/avi/autojump-test/b** ‘ without typing a sub-directory name.
```
$ jc b

```
![Jump to Child Directory](https://www.tecmint.com/wp-content/uploads/2015/06/Jump-to-Child-Directory.png)Jump to Child Directory
**8.** You can open a file manager that says **GNOME Nautilus** from the command-line, instead of jumping to a directory using the following command.
```
$ jo www

```
![Jump to Directory](https://www.tecmint.com/wp-content/uploads/2015/06/Jump-to-Direcotory.png)Jump to Directory ![Open Directory in File Browser](https://www.tecmint.com/wp-content/uploads/2015/06/Open-Directory-in-File-Browser-620x383.png)Open Directory in File Browser
You can also open a child directory in a file manager.
```
$ jco c

```
![Open Child Directory](https://www.tecmint.com/wp-content/uploads/2015/06/Open-Child-Directory1.png)Open Child Directory ![Open Child Directory in File Browser](https://www.tecmint.com/wp-content/uploads/2015/06/Open-Child-Directory-in-File-Browser1-620x383.png)Open Child Directory in File Browser
**9.** Check stats of each folder key weight and overall key weight along with total directory weight. Folder key weight is the representation of the total time spent in that folder. Directory weight is the number of directories in the list.
```
$ j --stat

```
![Check Directory Statistics](https://www.tecmint.com/wp-content/uploads/2015/06/Check-Statistics-511x450.png)Check Directory Statistics
**Tip** : The file where **autojump** stores run log and error log files in the folder `~/.local/share/autojump/`. Don’t overwrite these files, or else you may lose all your stats.
```
$ ls -l ~/.local/share/autojump/

```
![Autojump Logs](https://www.tecmint.com/wp-content/uploads/2015/06/Autojump-Logs.png)Autojump Logs
**10.** You may seek help if required simply as:
```
$ j --help
```
![Autojump Help and Options](https://www.tecmint.com/wp-content/uploads/2015/06/Autojump-help-options-620x450.png)Autojump Help and Options
### How Autojump Works
  *     * **autojump** lets you jump to only those directories to which you have already **cd**. Once you **cd** to a particular directory, it gets logged into the **autojump** database and thereafter autojump can work. You can not jump to a directory to which you have not cd, after setting up autojump, no matter what.
    * You can not jump to a directory, the name of which begins with a dash `(-)`. You may consider reading my post on the [Manipulation of files and directories](https://www.tecmint.com/manage-linux-filenames-with-special-characters/) that start with `'-'` or other special characters
    * In BASH Shell autojump keeps track of directories by modifying **$PROMPT_COMMAND**. It is strictly recommended not to overwrite **$PROMPT_COMMAND**. If you have to add [other Linux commands](https://www.tecmint.com/essential-linux-commands/ "Essential Linux Commands") to existing **$PROMPT_COMMAND** , append it to the last to existing **$APPEND_PROMPT**.


##### Conclusion
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[bd – Quickly Go Back to a Parent Directory Instead of Typing “cd ../../..” Redundantly](https://www.tecmint.com/bd-go-back-to-linux-directory/)
Next article:
[How to Install and Run Rust on Linux](https://www.tecmint.com/install-rust-linux/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### 16 Comments
[Leave a Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#reply-title)
  1. And it’s totally unnecessary to do ``apt-get dist-upgrade``, just do:
```
$ sudo apt install autojump
OR
$ sudo apt-get install autojump

```
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-811460)
  2. Very awesome, more Linux articles need to learn from you guys. Very well-put-together instructions and I love it, thank you for your work and knowledge base sharing.
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-806014)
  3. Love its script but I can’t get it to work with `j`, it seems to only accept **autojump** as a command. running on mint 17.3.
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-772693)
     * @Vince,
Thanks for finding this tool useful, have you seen any output with `j`? both `j` and **autojump** command gives the same output? could you share?
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-773121)
     * I’ve recently rewritten this tool with Go: github.com/suzaku/shonenjump/
You only need to download a binary for your platform, so it’s easier to install than the original one written in Python.
What’s more, it’s much faster.
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-778974)
       * @Satoru,
This is Ravi Saive, the founder of Tecmint.com.
Thanks for sharing your tool with us, why not you write a review on the same that includes installation as well and send it for publication on TecMint.com?
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-778988)
  4. I use **Fedora Linux** and I installed **autojump** from the Fedora repository, but the `j` command is not recognized and the command for bash activation gets “**file or command not found** “.
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-613072)
  5. I am using **Fedora Linux** and **autojump** is in the Fedora repository. Version is 21.7.1-4. I have installed autojump but I get the error message “**j: command not found** ” and I tried activate **autojump** temporarily, but the error message was: “**bash: /usr/share/autojump/autojump.sh: file or directory not found** “.
Indeed, I tried to activate autojump permanently, but I got an error message too.
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-612857)
     * I had to use `rpm -ql autojump` to see where `autojump.sh` is located because it seems like the path that is given in the post for the location of `autojump.sh` is wrong. Or search for `autojump.sh` and add those commands at the end of the post.
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-625947)
  6. Notable fact: bash has a simplistic directory bookmarking feature.
Defining the first two lines in `.bashrc` allows directory jumping:
```
~$ shopt -s cdable_vars
~$ export foo=/usr/share/lib/foo/bar
~$ cd foo
/usr/share/lib/foo/bar $

```

Here’s a screencast about it:
nevertheless, **autojump** is a cool productivity tool.
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-612719)
  7. It gives this error when I try to install it.
```
./install.py
  File "./install.py", line 40
    with open(os.path.join(etc_dir, 'autojump.sh'), 'a') as f:
            ^
SyntaxError: invalid syntax

```
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-612641)
     * @omipenguin,
Let me know your Python Version and OS details. You may email me your SSH access at `avishek1210[at]gmail.com`, for better assistance.
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-612653)
  8. I have installed it through **yum** in Centos 6.3, When I type the command “`autojump -v`“, it gives me the following error “**Unknown command line argument: option -v not recognized** “.
When I run `j` or `autojump`, it executes but not going to the directory.
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-611362)
     * @balu
I have already mentioned that **autojump** learns from you. After installing it, you need to train it. cd to your most frequently visited directories and then it will work.
However, if you could not do it, you may write me an email @ avishek1210[at]gmail.com with your input commands. your Output Message and your SSH access very clearly, so that I can assist.
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-611620)
  9. It’s a good command. I think it will be better if integrate some functions from **pushd** /**popd**.
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-611174)
     * Agree! Chang Limin.
[Reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#comment-611622)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/autojump-navigate-linux-directories-faster/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/autojump-navigate-linux-directories-faster/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=1102818510433317&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
