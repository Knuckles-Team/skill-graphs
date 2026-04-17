[Skip to content](https://www.tecmint.com/zstd-fast-data-compression-algorithm-used-by-facebook/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/zstd-fast-data-compression-algorithm-used-by-facebook/ "Linux Online Courses")
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


[](https://www.tecmint.com/zstd-fast-data-compression-algorithm-used-by-facebook/)
**Zstandard** (also known as **zstd**) is a free open source, fast real-time data compression program with better compression ratios, developed by **Facebook**. It is a [lossless compression algorithm](https://www.tecmint.com/xz-command-examples-in-linux/) written in **C** (there is a re-implementation in **Java**) – its thus a native Linux program.
**Read Also** : [10 7zip (Data Comperssion) Command Examples in Linux](https://www.tecmint.com/7zip-command-examples-in-linux/)
When required, it can trade compression speed for stronger compression ratios (compression speed vs compression ratio trade-off can be configured by small increments), vice versa. It has a special mode for small data compression, known as dictionary compression, and can build dictionaries from any sample set provided. It comes with a command line utility for creating and decoding **.zst** , **.gz** , **.xz** and **.lz4** files.
Importantly, **Zstandard** has a rich collection of APIs, supports almost all popular programming languages including Python, Java, JavaScript, Nodejs, Perl, Ruby, C#, Go, Rust, PHP, Switft, and lots more.
It is actively used to compress large volumes of data in multiple formats and use cases in **Facebook** ; services such as **Amazon Redshift** data warehousing; databases such as Hadoop and Redis; the Tor network and many other applications including games.
The following results are obtained by doing several fast compression algorithms tests on a server running Linux Debian using
![Zstandard Compression Testing](https://www.tecmint.com/wp-content/uploads/2018/06/Zstandard-Compression-Testing.png)Zstandard Compression Testing
### How to Install Zstandard Compression Tool in Linux
To install **Zstandard** on a Linux distribution, you need to compile it from sources, but before that first you need to install the necessary development tools on your system using your distribution package manager as shown.
```
$ sudo apt update && sudo apt install build-essential		#Ubuntu/Debian
# yum group install "Development Tools" 			#CentOS/REHL
# dnf groupinstall "C Development Tools and Libraries"		#Fedora 22+

```

Once all the needed development tools installed, now you can download the source package, move into the local repo directory, build the binary and install it as shown.
```
$ cd ~/Downloads
$ git clone https://github.com/facebook/zstd.git
$ cd zstd
$ make
$ sudo make install

```

Once **Zstandard** installed, now we can move further to learn some basic usage of **Zstd** command examples in the following section.
### Learn 10 Zstd Command Usage Examples in Linux
Zstd’s command line syntax is generally similar to that of **gzip** and **xz** tools, with a few differences.
**1.** To create a `.zst` compression file, simply provide a filename to compress it or use the `-z` flag also means compress, which is the default action.
```
$ zstd etcher-1.3.1-x86_64.AppImage
OR
$ zstd -z etcher-1.3.1-x86_64.AppImage

```

**2.** To decompress a `.zst` compression file, use the `-d` flag or the **unzstd** utility as shown.
```
$ zstd -d etcher-1.3.1-x86_64.AppImage.zst
OR
$ unzstd etcher-1.3.1-x86_64.AppImage.zst

```

**3.** To remove source file after an operation, by default, the source file is not deleted after successful compression or decompression, to delete it, use the `--rm` option.
```
$ ls etcher-1.3.1-x86_64.AppImage
$ zstd --rm  etcher-1.3.1-x86_64.AppImage
$ ls etcher-1.3.1-x86_64.AppImage

```

**4.** To set a compression level, zstd has a number of operation modifiers, for instance you can specify a compression level as `-6`(a number 1-19, default is 3) as shown.
```
$ zstd -6 --rm etcher-1.3.1-x86_64.AppImage

```

**5.** To set a compression speed, zstd has a compression speed ratio **1-10** , the default compression speed is **1**. You can trade compression ratio for compression speed with the `--fast` option, the higher the number the faster the compression speed.
```
$ zstd --fast=10 etcher-1.3.1-x86_64.AppImage

```

**6.** To display information about a compressed file, use the `-l` flag, which is used to display information about a compressed file, for example.
```
$ zstd -l etcher-1.3.1-x86_64.AppImage.zst

```

**7.** To test the integrity of a compressed files, use the `-t` flag as shown.
```
$ zstd -t etcher-1.3.1-x86_64.AppImage.zst

```

**8.** To enable verbose mode, use the `-v` option.
```
$ zstd -v -5 etcher-1.3.1-x86_64.AppImage

```

**9.** To use other file compression or decompression formats such as gzip, xz, lzma, and lz4, using the `--format=FORMAT` as shown.
```
$ zstd -v --format=gzip etcher-1.3.1-x86_64.AppImage
$ zstd -v --format=xz  etcher-1.3.1-x86_64.AppImage

```

**10.** To set a zstd process priority to real-time, you can use the option **–priority=rt** as shown.
```
$zstd --priority=rt etcher-1.3.1-x86_64.AppImage

```

The `-r` flag instructs zstd to operate recursively on dictionaries. You can find lots of useful and advanced options, how to read or create dictionaries by consulting the zstd man page.
```
$ man zstd

```

**Zstandard Github Repository** :
**Zstandard** is a fast real-time, lossless data compression algorithm and compression tool which offers high compression ratios. Try it out and share your thoughts about it or ask questions via the feedback form below.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Monitor Apache Performance using Netdata on CentOS 7](https://www.tecmint.com/monitor-apache-performance-using-netdata-on-centos/)
Next article:
[How to Migrate from GitHub to GitLab](https://www.tecmint.com/migrate-from-github-to-gitlab/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/zstd-fast-data-compression-algorithm-used-by-facebook/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### 2 Comments
[Leave a Reply](https://www.tecmint.com/zstd-fast-data-compression-algorithm-used-by-facebook/#reply-title)
  1. I think there is a mistake in point 2
It says, To decompress a .zst compression file, use the **-d** flag or the **unzstd** utility as shown.
```
$ zstd -d etcher-1.3.1-x86_64.AppImage
OR
$ unzstd etcher-1.3.1-x86_64.AppImage

```

Instead it should be
To decompress a **.zst** compression file, use the **-d** flag or the unzstd utility as shown.
```
$ zstd -d etcher-1.3.1-x86_64.AppImage.zst
OR
$ unzstd etcher-1.3.1-x86_64.AppImage.zst

```
[Reply](https://www.tecmint.com/zstd-fast-data-compression-algorithm-used-by-facebook/#comment-1091525)
     * @Ismail,
Thanks for pointing out, corrected in the article.
[Reply](https://www.tecmint.com/zstd-fast-data-compression-algorithm-used-by-facebook/#comment-1091854)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/zstd-fast-data-compression-algorithm-used-by-facebook/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/zstd-fast-data-compression-algorithm-used-by-facebook/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://pagead2.googlesyndication.com/pagead/sodar?id=sodar2&v=253&li=gpt_m202603050101&jk=5366676034716614&rc=)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
