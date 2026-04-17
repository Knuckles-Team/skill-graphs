[Skip to content](https://www.tecmint.com/delete-large-directory-linux/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/delete-large-directory-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/delete-large-directory-linux/)
File management is one of the common tasks that a user undertakes on a Linux system, which includes [creating](https://www.tecmint.com/mkdir-command-examples/ "Create Directory in Linux"), [copying](https://www.tecmint.com/cp-command-examples/ "Copy Files and Directories in Linux"), [moving](https://www.tecmint.com/mv-command-linux-examples/ "Move Files in LInux"), modifying, and [deleting files and directories](https://www.tecmint.com/linux-rm-command-examples/ "Delete Files in Linux").
This article provides a few command-line tips on how you can [delete a large directory](https://www.tecmint.com/delete-huge-files-in-linux/ "Delete Large Directory Files in Linux") that contains thousands of files in a Linux system.

Table of Contents
Toggle
  * [Delete Files in Linux](https://www.tecmint.com/delete-large-directory-linux/#Delete_Files_in_Linux)
  * [Delete Directory in Linux](https://www.tecmint.com/delete-large-directory-linux/#Delete_Directory_in_Linux)
  * [Delete a Large Directory with Tons of Files](https://www.tecmint.com/delete-large-directory-linux/#Delete_a_Large_Directory_with_Tons_of_Files)
    * [Delete Files With Inode Number in Linux](https://www.tecmint.com/delete-large-directory-linux/#Delete_Files_With_Inode_Number_in_Linux)
    * [Create a Directory with Thousands of Files](https://www.tecmint.com/delete-large-directory-linux/#Create_a_Directory_with_Thousands_of_Files)
    * [Fastest Way to Delete Directory in Linux](https://www.tecmint.com/delete-large-directory-linux/#Fastest_Way_to_Delete_Directory_in_Linux)
    * [Delete Large Directory with Find Command](https://www.tecmint.com/delete-large-directory-linux/#Delete_Large_Directory_with_Find_Command)
    * [Delete Large Directory with Perl Command](https://www.tecmint.com/delete-large-directory-linux/#Delete_Large_Directory_with_Perl_Command)
      *         * [Conclusion](https://www.tecmint.com/delete-large-directory-linux/#Conclusion)


The most common way of deleting files on a Linux system is using the [rm command](https://www.tecmint.com/linux-rm-command-examples/ "rm Command in Linux"), which takes the following syntax format:
```
$ rm [ options ] sample_file.txt

```

For example, to delete a text file called **file1.txt** , run the command:
```
$ rm file1.txt

```

To forcefully remove a file without being asked for permission, pass the `-f` flag as follows.
```
$ rm -f file1.txt

```

To remove or delete a directory called **sample_directory** , run the following command:
```
$ rm -rf sample_directory

```

The `-r` option recursively deletes the directory alongside all the subdirectories and files contained therein.
To delete or remove an empty directory use the [rmdir command](https://www.tecmint.com/rmdir-command-examples/ "rmdir Command in Linux"), which comes in handy when you want to remove an empty directory called **test_directory** as shown:
```
$ rmdir test_directory

```

When the **rm command** is executed, the filesystem only removes the link to the file, which makes the file unavailable to the user, but in the real sense, the file’s data itself remains intact on the disk.
Therefore, when the **rm command** is issued, only the reference to the files is removed, which frees up the storage blocks in the filesystem.
As such, there exist several avenues to delete files in Linux.
For example, you can delete a file using its inode number. You can find out a file’s inode number using the [stat command](https://www.tecmint.com/linux-stat-command-examples/ "Linux stat Command") as shown.
```
**$ stat file1.txt**

File: file.txt
  Size: 4076      	Blocks: 8          IO Block: 4096   regular file
Device: 801h/2049d	**Inode: 1573697**     Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/ tecmint)   Gid: ( 1000/ tecmint)
Access: 2023-05-08 12:10:55.656070248 +0530
Modify: 2023-05-08 12:10:55.656070248 +0530
Change: 2023-05-08 12:10:55.656070248 +0530

```

In addition, you can pass the `-i` flag in the [ls command](https://www.tecmint.com/15-basic-ls-command-examples-in-linux/ "Linux ls Command") when listing files inside a directory.
```
**$ ls -li**

**1573697** .rw-rw-r-- tecmint tecmint 4.0 KB Mon May  8 12:10:55 2023  file1.txt

```

To remove the file using its inode, use the [find command](https://www.tecmint.com/35-practical-examples-of-linux-find-command/ "Linux find Command") as shown in the syntax below.
```
$ find /path/to/file -inum **INODE_NUM** -exec rm -i {} +

```

In our example, to remove file **file1.txt** that sits in the current directory, the command will be:
```
$ find /path/to/file -inum **1573697** -exec rm -i {} +

```

Hit `'y'` to confirm the removal and press **ENTER**.
![Delete Files By Inode Number](https://www.tecmint.com/wp-content/uploads/2023/05/Delete-Files-By-Inode-Number.png)Delete Files By Inode Number
Let us now see how to delete large directories with thousands of files.
The good old **rm** command is the fastest way of deleting a large directory with thousands of files. To demonstrate this, we will, first, [create a sample directory](https://www.tecmint.com/mkdir-command-examples/ "Create Directory in Linux") and navigate into it.
```
$ mkdir test_dir
$ cd test_dir

```

Next, we will create an insanely huge number of files, in this case, **500,000** text files using the following [bash for a loop](https://www.tecmint.com/bash-for-loop-linux/ "Bash For Loop in Linux").
```
$ time for item in {1..500000}; do touch file_name$item.txt; done

```

**NOTE** : The above command is resource intensive and, hence, consumes substantial CPU and RAM. It also takes quite some time depending on your system specifications. In my case, I’m running a VM with 4GB RAM and 3 CPUs.
![Create Thousands of Files in Linux](https://www.tecmint.com/wp-content/uploads/2023/05/Create-Thousands-of-Files-in-Linux.png)Create Thousands of Files in Linux
The fastest way to delete a large directory is using the good old **rm** directory as shown below. Here, the time option displays the time taken to successfully execute the command.
```
$ time rm -rf /test_dir

```
![Fastest Way to Delete Large Directory](https://www.tecmint.com/wp-content/uploads/2023/05/Fastest-Way-to-Delete-Large-Directory.png)Fastest Way to Delete Large Directory
From the output, you can see that it has taken roughly 6 seconds to delete the entire directory.
Another way to delete large directories is using the [find command](https://www.tecmint.com/find-files-quickly-in-linux-terminal/ "Find Files Quickly in Linux") as shown in the following syntax.
```
$ time find /path/to/directory -delete

```

Although not as fast as the **rm** command it still gets the job done.
```
$ time find test_dir -delete

```
![Find Command - Delete Large Directory](https://www.tecmint.com/wp-content/uploads/2023/05/Find-Command-Delete-Large-Directory.png)Find Command – Delete Large Directory
Another approach is to use the **Perl** scripting language inside the directory to remove tons of files.
```
$ cd test_dir
$ time perl -e 'for(<*>){((stat)[9]<(unlink))}'

```
![Perl Command - Delete Large Directory](https://www.tecmint.com/wp-content/uploads/2023/05/Perl-Command-Delete-Large-Directory.png)Perl Command – Delete Large Directory
From the output, you can this that it took much longer to delete all the files in the directory than the previous commands that we looked at earlier.
There you have it. In this guide, we have looked at how you can delete large directories that contain thousands of files on a Linux system.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Psensor – Monitor Linux Hardware Temperature [Motherboard and CPU]](https://www.tecmint.com/psensor-monitors-hardware-temperature-in-linux/)
Next article:
[iPerf3 – Test Network Speed/Throughput in Linux](https://www.tecmint.com/test-network-throughput-in-linux/)
![Photo of author](https://secure.gravatar.com/avatar/67ddcc66fdc1a9535834e142c47bd9968dbb70df7ddd5f627dfbc3452c6849eb?s=100&d=blank&r=g)
Winnie Ondara
My name is Winnie, a Linux enthusiast and passionate tech writer in Linux and DevOPs topics. I enjoy keeping abreast with the latest technologies in the Linux ecosystem and trying out new tools provided by the FOSS community.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/delete-large-directory-linux/#respond)** or
## Related Posts
[![Convert .MD to PDF in Linux](https://www.tecmint.com/wp-content/uploads/2025/01/convert-md-to-pdf-linux.webp)](https://www.tecmint.com/convert-md-to-pdf-on-linux/ "How to Convert Markdown \(.MD\) Files to PDF on Linux")
[![Clifm - Terminal File Manager](https://www.tecmint.com/wp-content/uploads/2024/08/Clifm-Terminal-File-Manager-for-Linux.png)](https://www.tecmint.com/clifm-fast-commandline-file-manager/ "Clifm – Lightning-Fast Command Line File Manager for Linux")
[![Minify JS and CSS Files in Linux](https://www.tecmint.com/wp-content/uploads/2024/08/Minify-JS-CSS-Files-in-Linux.webp)](https://www.tecmint.com/minify-css-and-js-files-linux/ "How to Minify CSS and JS Files Using Linux Command Line")
[![Convert WebM Video in Linux](https://www.tecmint.com/wp-content/uploads/2024/06/Convert-WebM-Video-in-Linux.png)](https://www.tecmint.com/convert-webm-video-linux/ "How to Convert WebM Videos to Any Format on Linux")
[![Install LZ4 in Linux](https://www.tecmint.com/wp-content/uploads/2024/06/install-lz4-linux.png)](https://www.tecmint.com/install-lz4-linux/ "LZ4 for Linux: Install, Use & Speed Up File Compression \(Examples\)")
[![Create ISO from Directory in Linux](https://www.tecmint.com/wp-content/uploads/2024/06/Create-ISO-File-from-a-Directory.webp)](https://www.tecmint.com/create-iso-from-directory-linux/ "How to Make ISO from Directory in Linux")
### 4 Comments
[Leave a Reply](https://www.tecmint.com/delete-large-directory-linux/#reply-title)
  1. If it took *84 minutes* to touch 500k 0-byte files, you’re doing something wrong.
On a 2011 core-i5 iMac with OSX High Sierra 10.13 running against a Firewire-800 spinning disk with APFS filesystem:
```
$ time echo {1..100000} |xargs -P 2 -n 1 touch

```

# Parallel process 2x / time
Begin:
Thu May 11 09:01:03 CDT 2023
real 1m47.971s
user 1m11.711s
sys 1m44.261s
Thu May 11 09:02:51 CDT 2023
End
xargs ~30% CPU,
Terminal ~20% cpu – and you can also preface the create command with ‘**nice** ‘.
As for deleting a directory with thousands of files, I’d argue the *safest* way to do so would be to use **Midnight Commander**. Navigate to the directory, hit `F8`, and it asks for confirmation, no unexpected results.
[Reply](https://www.tecmint.com/delete-large-directory-linux/#comment-2012980)
  2. This will not work on directories with a large number of files, where the shell (like **bash**) runs out of memory. There the **find** /**exec** **rm** method is a valid solution.
[Reply](https://www.tecmint.com/delete-large-directory-linux/#comment-2011709)
     * @Andreas,
Could you share one example, of how the find/exec rm method is a valid solution for this? It would be a great help for all Linux users…
[Reply](https://www.tecmint.com/delete-large-directory-linux/#comment-2011942)
  3. Really very good article for deleting lakhs of files in a directory in Linux.
[Reply](https://www.tecmint.com/delete-large-directory-linux/#comment-2011642)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/delete-large-directory-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/delete-large-directory-linux/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
