[Skip to content](https://www.tecmint.com/chown-command-examples/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/chown-command-examples/ "Linux Online Courses")
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


[](https://www.tecmint.com/chown-command-examples/)
_**Brief: In this beginner’s guide, we will discuss some practical examples of the chown command. After following this guide, users will be able to manage file ownership effectively in Linux.**_
In Linux, [everything is a file](https://www.tecmint.com/explanation-of-everything-is-a-file-and-types-of-files-in-linux/ "Everything is a File in Linux"), which means, all input/output resources, such as files, directories, disk drives, printers, etc are exposed as files through the file system namespace. In addition to this, there is ownership associated with each and every file in Linux.
The ownership is represented by two entities – **user** and **group**. The combination of access permissions and ownership allows Linux to implement an access control mechanism in an effective way.
In this guide, we will learn about the **chown command**. As the name suggests, the **chown command** is used to change the ownership of the files. After following this guide, beginners will be able to use the **chown command** effectively while working with Linux systems.
#### chown Command Syntax
The syntax of the **chown command** is as follows:
```
$ chown [OPTION]... [OWNER][:[GROUP]] [FILE-1] [FILE-2]...[FILE-N]

```

Now let’s understand the usage of the **chown command** with some practical examples in Linux.
### 1. How to Find the Ownership of the File
The easiest way to find the owner of the file is using the [ls command](https://www.tecmint.com/15-basic-ls-command-examples-in-linux/ "ls Command Examples in Linux"), which will list the user and group of the file.
```
$ touch file-1.txt
$ ls -l file-1.txt

```
![Check File Ownership in Linux](https://www.tecmint.com/wp-content/uploads/2018/04/Check-File-Ownership-in-Linux.png)Check File Ownership in Linux
In the above output, we can see that the file is owned by the **tecmint** user and group. This information is represented by the third and fourth columns respectively.
### 2. How to Change Ownership of File
The **chown command** allows us to change the ownership of the file. Let’s see its usage by setting user **narendra** as the owner of the file:
```
$ sudo chown narendra file-1.txt

```

Now, let’s verify that ownership of the file has been changed:
```
$ ls -l file-1.txt

```
![Change File Ownership in Linux](https://www.tecmint.com/wp-content/uploads/2018/04/Change-File-Ownership-in-Linux.png)Change File Ownership in Linux
### 3. How to Change Group Ownership of File
Similar to the user, we can also change the group ownership of the file using the **chown** command. So, let’s set group ownership of the file to the group – **narendra** :
```
$ sudo chown :narendra file-1.txt

```

It is important to note that, we have to use a colon `(:)` with the group name while changing the group ownership.
Now, let’s verify the group ownership of the file:
```
$ ls -l file-1.txt

```
![Change File Group Ownership in Linux](https://www.tecmint.com/wp-content/uploads/2018/04/Change-File-Group-Ownership-in-Linux.png)Change File Group Ownership in Linux
### 4. How to Change Ownership and Group of File
In the previous examples, we used the **chown** command twice. First, to change the user ownership and then to change the group ownership. However, we can change both user and group using a single command.
Let’s reset the file ownership to the user and group **tecmint** , using the following command:
```
$ sudo chown tecmint:tecmint file-1.txt

```

In this example, we have used the colon `(:)` character to separate the user and group. The value before the colon represents the **user** whereas the value after the colon represents the **group**.
Now, let’s check the updated file ownership:
```
$ ls -l file-1.txt

```
![Change File Ownership and-Group](https://www.tecmint.com/wp-content/uploads/2018/04/Change-File-Ownership-and-Group-in-Linux.png)Change File Ownership and-Group
### 5. How to Change Ownership of the Symbolic Link
By default, the **chown** command dereferences the symbolic link, which means, if the input file is a symbolic link then it changes the ownership of the reference file instead of the symbolic link itself.
However, we can override the default behavior using the `-h` option as shown in the following example.
First, [create a symbolic link](https://www.tecmint.com/create-hard-and-symbolic-links-in-linux/ "Create Hard and Symbolic Links in Linux") and verify that it’s pointing to the correct reference file:
```
$ ln -s file-1.txt symlink
$ ls -l symlink

```

Next, change the ownership of the symbolic link using the `-h` option:
```
$ sudo chown -h narendra:narendra symlink

```

Finally, verify the ownership of the symbolic link and its reference file:
```
$ ls -l symlink file-1.txt

```
![Change Ownership of Symbolic Link](https://www.tecmint.com/wp-content/uploads/2018/04/Change-Ownership-of-Symbolic-Link.png)Change Ownership of Symbolic Link
### 6. How to Transfer File Ownership to the User
Sometimes, we need to update the ownership of the file only after validating its current ownership. In such cases, we can use the `--from` option of the **chown** command as shown.
```
$ sudo chown -h --from narendra:narendra tecmint:tecmint symlink

```

In this example, the `--from` option represents the current owner of the file whereas the next argument represents the new ownership. So the above command updates the ownership of the file – symlink, only if the file is owned by the user and group – **narendra**.
Now, let’s check the updated ownership of the file:
```
$ ls -l symlink

```
![Transfer File Ownership to User in Linux](https://www.tecmint.com/wp-content/uploads/2018/04/Transfer-File-Ownership-to-User.png)Transfer File Ownership to the User in Linux
In this example, we have specified both user and group using the colon `(:)` character. However, we can specify either of them as discussed in the previous examples.
### 7. How to Copy Ownership From Another File
Sometimes, it’s convenient to copy the ownership from the existing file instead of providing the same from the command line. In such scenarios, we can use the `--reference` option with the **chown** command, which represents the file from which ownership is to be copied.
First, create a new file and change its ownership:
```
$ touch file-2.txt
$ sudo chown narendra:narendra file-2.txt

```

Now, let’s check the current ownership of both files:
```
$ ls -l file-1.txt file-2.txt

```

Next, set the ownership of the **file-2.txt** file the same as the **file-1.txt** using the following command:
```
$ sudo chown --reference=file-1.txt file-2.txt

```

Finally, verify that the ownership has been updated successfully:
```
$ ls -l file-1.txt file-2.txt

```
![Copy Ownership From Another File in Linux](https://www.tecmint.com/wp-content/uploads/2018/04/Copy-File-Ownership-From-Another-File.png)Copy Ownership From Another File in Linux
In the above output, we can see that now both files have the same ownership.
### 8. How to Change Ownership of the Directory Recursively
We can use the **chown** command to change the ownership of the directory as well. However, the default behavior of the command is non-recursive.
It means that the **chown** command will change the ownership of the input directory only. However, we can override this default behavior using the `-R` option as shown in the following example.
First, create a directory and two files into it:
```
$ mkdir dir-1
$ touch dir-1/demo-1.txt dir-1/demo-2.txt

```

Next, check the ownership of the directory and its files:
```
$ ls -ld dir-1
$ ls -l dir-1

```

Then, change the ownership of the directory and its files in a recursive way:
```
$ sudo chown -R narendra:narendra dir-1

```

Finally, verify the ownership of the directory and its files:
```
$ ls -ld dir-1
$ ls -l dir-1

```
![Change Directory Ownership Recursively in Linux](https://www.tecmint.com/wp-content/uploads/2018/04/Change-Directory-Ownership-Recursively.png)Change Directory Ownership Recursively in Linux
### 9. How to Print Chown Command Process Details
By default, the **chown** command doesn’t print anything on the terminal after changing the ownership. Hence, so far we have been using the `-l` option of the [ls command](https://www.tecmint.com/linux-ls-command-tricks/ "ls Command Tricks for Every Linux User") to verify the updated ownership.
To overcome this limitation, we can enable the verbose mode of the command that prints the diagnostics for each processed file. This option gives meaningful information when we use it with the `-R` option:
So, let’s use the `-v` option of the command to enable the verbose mode:
```
$ sudo chown -Rv tecmint:tecmint dir-1

```

Now, let’s check the output of the command:
![Enable Chown Verbose Mode in Linux](https://www.tecmint.com/wp-content/uploads/2018/04/Enable-Chown-Verbose-Mode-in-Linux.png)Enable Chown Verbose Mode in Linux
### 10. How to Suppress Chown Command Errors
Like other [Linux commands](https://www.tecmint.com/most-used-linux-commands/ "Most Commonly Used Linux Commands"), **chown** also provides meaningful information in case of error scenarios. The error can happen due to various reasons, such as non-existing files, groups, or users, insufficient permission to perform certain operations, and so on.
However, sometimes we don’t want to show these error messages. In such cases, we can use the `-f` option of the command to suppress the error messages.
To understand this in a better way, let’s try to change the ownership of the non-existing file:
```
$ sudo chown -f narendra:narendra non-existing-file.txt
$ echo $?
1

```

Now, let’s see the output of the command:
![Suppress Chown Command Errors in Linux](https://www.tecmint.com/wp-content/uploads/2018/04/Suppress-Chown-Command-Errors.png)Suppress Chown Command Errors in Linux
As we can see, the above command doesn’t show any error. However, the command reports failure using the non-zero return value.
### 11. How to Change File User and Group ID
So far, we used the user and group names to change the ownership of the file. However, we can also use the user and group IDs to achieve the same result.
First, use the **id** command to find the user and group ID of the user – **narendra** :
```
$ id narendra

```

Now, let’s use the user and group ID **1001** with the **chown** command:
```
$ ls -l file-1.txt
$ sudo chown 1001:1001 file-1.txt

```

Finally, verify that the ownership has been updated successfully:
```
$ ls -l file-1.txt

```
![Change File Ownership UID and GID in Linux](https://www.tecmint.com/wp-content/uploads/2018/04/Change-File-Ownership-UID-and-GID-in-Linux.png)Change File Ownership UID and GID in Linux
In this article, we discussed some practical examples of the **chown** command. One can use these examples in day-to-day life to boost productivity while working with Linux systems.
_**Do you know of any other best example of the chown command in Linux? Let us know your views in the comments below.**_
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Useful PuTTY Configuration Tips and Tricks](https://www.tecmint.com/putty-configuration-tips-and-tricks/)
Next article:
[Shell In A Box – A Web-Based SSH Terminal to Access Linux via Browser](https://www.tecmint.com/shellinabox-web-based-ssh-linux-terminal/)
![Photo of author](https://secure.gravatar.com/avatar/043721451ba3c67ab7c1e510f30b1af43862d4b5e97012854c0cadf8aa37ecbc?s=100&d=blank&r=g)
Narendra K
I'm an experienced and passionate software engineer with in-depth experience in Linux, Distributed systems, DevOps, and Cloud. My expertise lies in back-end web development, and the main languages in my tech stack are Java, Spring, Python, and Go. I’m a lifelong learner and an open-source enthusiast.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/chown-command-examples/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### 4 Comments
[Leave a Reply](https://www.tecmint.com/chown-command-examples/#reply-title)
  1. @dragonmouth,
No, they are not the same. In example #4 we are using user and group names whereas in example #11 we are using the ids associated with them. We can use either name or id with the chown command. For example, the below command uses the combination of the user id and group name:
$ sudo chown 1001:narendra file-1.txt
[Reply](https://www.tecmint.com/chown-command-examples/#comment-1926725)
  2. Isn’t Example #4 and Example #11 the same? In Example #4 you are changing the alpha userid and groupid while in example #11 you are changing the numeric IDs.
[Reply](https://www.tecmint.com/chown-command-examples/#comment-1926555)
  3. @dragonmouth,
Here, the main intention is to show the updated ownership. There are multiple ways to achieve this. For example, using the **ls command** or `-v` flag. We can use either of them.
In addition to this, we can also use the **stat** command as shown below:
`$ stat -c "Owner = %U, Group = %G" file-1.txt
 Owner = narendra, Group = narendra`
[Reply](https://www.tecmint.com/chown-command-examples/#comment-1923864)
  4. In Example #11, why don’t you use the `"-v"` flag instead of the “**ls** ” command?
[Reply](https://www.tecmint.com/chown-command-examples/#comment-1923459)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/chown-command-examples/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/chown-command-examples/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
