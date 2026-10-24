[Skip to content](https://www.tecmint.com/scp-commands-examples/#content "Skip to content")
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
  * [Pro Courses](https://www.tecmint.com/scp-commands-examples/ "Linux Online Courses")
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


[](https://www.tecmint.com/scp-commands-examples/)
Linux administrators should be familiar with the command-line environment. Since **GUI** (**Graphical User Interface**) mode in Linux servers is not common to be installed.
**[SSH](https://www.tecmint.com/install-openssh-server-in-linux/ "Install SSH In Linux")** may be the [most popular protocol](https://www.tecmint.com/ssh-clients-linux/ "Most SSH Clients for Linux") to enable Linux administrators to manage the servers in a remote secure way. Built in with **SSH** command there is **SCP** command, which is used to [copy file(s) between servers](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "Rsync Copying Files Between Linux Servers") in a secure way.
**You might also like:**
  * [How to Secure and Harden SSH Server](https://www.tecmint.com/secure-openssh-server/ "Secure OpenSSH Server")
  * [Basic SSH Command Usage and Configuration in Linux](https://www.tecmint.com/ssh-command-usage/ "Basic SSH Command Usage in Linux")
  * [How to Prevent SSH Brute-Force Login Attacks in Linux](https://www.tecmint.com/prevent-ssh-brute-force-login-attacks/ "Prevent SSH Brute-Force Attacks")


The below command will read as copy “**source_file_name** ” into “**destination_folder** ” at “**destination_host** ” using the “**username** ” account.
```
scp source_file_name username@destination_host:destination_folder
```

There are many parameters in the **SCP** command that you can use. Here are the parameters that may use on daily basis usage.

Table of Contents
Toggle
    * [Basic Syntax of SCP Command](https://www.tecmint.com/scp-commands-examples/#Basic_Syntax_of_SCP_Command)
  * [Securely Transfer Files in Linux](https://www.tecmint.com/scp-commands-examples/#Securely_Transfer_Files_in_Linux)
    * [Copy File From Local Host to Remote Server](https://www.tecmint.com/scp-commands-examples/#Copy_File_From_Local_Host_to_Remote_Server)
    * [Copy File From Remote Host to Local Host](https://www.tecmint.com/scp-commands-examples/#Copy_File_From_Remote_Host_to_Local_Host)
    * [Copy File From Remote Host to Another Host](https://www.tecmint.com/scp-commands-examples/#Copy_File_From_Remote_Host_to_Another_Host)
  * [Copy Files with Original Creation Date and Time](https://www.tecmint.com/scp-commands-examples/#Copy_Files_with_Original_Creation_Date_and_Time)
  * [Scp Compression While Copying Files](https://www.tecmint.com/scp-commands-examples/#Scp_Compression_While_Copying_Files)
  * [Change SCP Cipher to Encrypt Files](https://www.tecmint.com/scp-commands-examples/#Change_SCP_Cipher_to_Encrypt_Files)
  * [Limiting Bandwidth Usage with SCP Command](https://www.tecmint.com/scp-commands-examples/#Limiting_Bandwidth_Usage_with_SCP_Command)
  * [SCP with a Different Port](https://www.tecmint.com/scp-commands-examples/#SCP_with_a_Different_Port)
  * [SCP – Copy Files and Directories Recursively](https://www.tecmint.com/scp-commands-examples/#SCP_%E2%80%93_Copy_Files_and_Directories_Recursively)
  * [SCP – Disable Progress Messages](https://www.tecmint.com/scp-commands-examples/#SCP_%E2%80%93_Disable_Progress_Messages)
  * [SCP – Copy Files Using Proxy](https://www.tecmint.com/scp-commands-examples/#SCP_%E2%80%93_Copy_Files_Using_Proxy)
    * [Choose a Different ssh_config File](https://www.tecmint.com/scp-commands-examples/#Choose_a_Different_ssh_config_File)


The basic **SCP** command without parameters will copy the files in the background. Users will see nothing unless the process is done or some error appears.
You can use the “`-v`” parameter to print debug information into the screen. It can help you debug connection, authentication, and configuration problems.
The following command copies a file “**scp-cheatsheet.pdf** ” from a local to a remote Linux system under **/home/tecmint** directory.
```
$ scp -v scp-cheatsheet.pdf tecmint@192.168.0.183:/home/tecmint/.

```

**Sample Output** :
SCP – Copy File to Remote Linux Server
```
Executing: program /usr/bin/ssh host 192.168.0.183, user tecmint, command scp -v -t /home/tecmint/.
OpenSSH_8.2p1 Ubuntu-4ubuntu0.5, OpenSSL 1.1.1f  31 Mar 2020
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
debug1: /etc/ssh/ssh_config line 21: Applying options for *
debug1: Connecting to 192.168.0.183 [192.168.0.183] port 22.
debug1: Connection established.
debug1: identity file /home/tecmint/.ssh/id_rsa type -1
debug1: identity file /home/tecmint/.ssh/id_rsa-cert type -1
debug1: identity file /home/tecmint/.ssh/id_dsa type -1
debug1: identity file /home/tecmint/.ssh/id_dsa-cert type -1
debug1: identity file /home/tecmint/.ssh/id_ecdsa type -1
debug1: identity file /home/tecmint/.ssh/id_ecdsa-cert type -1
debug1: identity file /home/tecmint/.ssh/id_ecdsa_sk type -1
debug1: identity file /home/tecmint/.ssh/id_ecdsa_sk-cert type -1
debug1: identity file /home/tecmint/.ssh/id_ed25519 type -1
debug1: identity file /home/tecmint/.ssh/id_ed25519-cert type -1
debug1: identity file /home/tecmint/.ssh/id_ed25519_sk type -1
debug1: identity file /home/tecmint/.ssh/id_ed25519_sk-cert type -1
debug1: identity file /home/tecmint/.ssh/id_xmss type -1
...

```

The following command copies a file “**ssh-cheatsheet.pdf** ” from a remote host to a local system under **/home/tecmint** directory.
```
$ scp -v tecmint@192.168.0.183:/home/ravi/ssh-cheatsheet.pdf /home/tecmint/.

```

**Sample Output** :
SCP – Copy File to Local System
```
Executing: program /usr/bin/ssh host 192.168.0.183, user tecmint, command scp -v -f /home/ravi/ssh-cheatsheet.pdf
OpenSSH_8.2p1 Ubuntu-4ubuntu0.5, OpenSSL 1.1.1f  31 Mar 2020
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: include /etc/ssh/ssh_config.d/*.conf matched no files
debug1: /etc/ssh/ssh_config line 21: Applying options for *
debug1: Connecting to 192.168.0.183 [192.168.0.183] port 22.
debug1: Connection established.
debug1: identity file /home/tecmint/.ssh/id_rsa type -1
debug1: identity file /home/tecmint/.ssh/id_rsa-cert type -1
debug1: identity file /home/tecmint/.ssh/id_dsa type -1
debug1: identity file /home/tecmint/.ssh/id_dsa-cert type -1
debug1: identity file /home/tecmint/.ssh/id_ecdsa type -1
debug1: identity file /home/tecmint/.ssh/id_ecdsa-cert type -1
debug1: identity file /home/tecmint/.ssh/id_ecdsa_sk type -1
debug1: identity file /home/tecmint/.ssh/id_ecdsa_sk-cert type -1
debug1: identity file /home/tecmint/.ssh/id_ed25519 type -1
debug1: identity file /home/tecmint/.ssh/id_ed25519-cert type -1
debug1: identity file /home/tecmint/.ssh/id_ed25519_sk type -1
...

```

The following command copies a file “**ssh-cheatsheet.pdf** ” from a remote host to another remote host system under **/home/tecmint** directory.
```
$ scp -v tecmint@192.168.0.183:/home/ravi/ssh-cheatsheet.pdf tecmint@192.168.0.102:/home/anusha/.

```

The “`-p`” parameter will preserve files’ original modification and access times while copying files along with the estimated time and the connection speed will appear on the screen.
```
$ scp -p scp-cheatsheet.pdf tecmint@192.168.0.183:/home/tecmint/.

```

**Sample Output** :
SCP – Preserve File Timestamps
```
tecmint@192.168.0.183's password:
scp-cheatsheet.pdf                                                                                                                                                                 100%  531   721.4KB/s   00:00

```

One of the parameters that can faster your file transfer is the “`-C`” parameter, which is used to [compress your files](https://www.tecmint.com/tar-command-examples-linux/ "Tar Command in Linux") on the go. The unique thing is that compression only happens in the network. When the file has arrived at the destination server, it will be returning to the original size as before the compression happened.
Take a look at these commands. It is using a single file of **93 Mb**.
```
$ scp -pv messages.log mrarianto@202.x.x.x:.

```

**Sample Output** :
SCP Transfers File Without Compression
```
Executing: program /usr/bin/ssh host 202.x.x.x, user mrarianto, command scp -v -p -t.
OpenSSH_6.0p1 Debian-3, OpenSSL 1.0.1c 10 May 2012
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: Applying options for *
debug1: Connecting to 202.x.x.x [202.x.x.x] port 22.
debug1: Connection established.
debug1: identity file /home/pungki/.ssh/id_rsa type -1
debug1: Found key in /home/pungki/.ssh/known_hosts:1
debug1: ssh_rsa_verify: signature correct
debug1: Trying private key: /home/pungki/.ssh/id_rsa
debug1: Next authentication method: password
mrarianto@202.x.x.x's password:
debug1: Authentication succeeded (password).
Authenticated to 202.x.x.x ([202.x.x.x]:22).
debug1: Sending command: scp -v -p -t.
File mtime 1323853868 atime 1380425711
Sending file timestamps: T1323853868 0 1380425711 0
messages.log 100% 93MB 58.6KB/s 27:05
Transferred: sent 97614832, received 25976 bytes, in 1661.3 seconds
Bytes per second: sent 58758.4, received 15.6
debug1: Exit status 0
```

Copying files without the “`-C`” parameter will result in **1661.3** seconds. You may compare the result to the command below using the “`-C"` parameter.
```
$ scp -Cpv messages.log mrarianto@202.x.x.x:.

```

**Sample Output** :
SCP – Transfers File with Compression
```
Executing: program /usr/bin/ssh host 202.x.x.x, user mrarianto, command scp -v -p -t.
OpenSSH_6.0p1 Debian-3, OpenSSL 1.0.1c 10 May 2012
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: Applying options for *
debug1: Connecting to 202.x.x.x [202.x.x.x] port 22.
debug1: Connection established.
debug1: identity file /home/pungki/.ssh/id_rsa type -1
debug1: Host '202.x.x.x' is known and matches the RSA host key.
debug1: Found key in /home/pungki/.ssh/known_hosts:1
debug1: ssh_rsa_verify: signature correct
debug1: Next authentication method: publickey
debug1: Trying private key: /home/pungki/.ssh/id_rsa
debug1: Next authentication method: password
mrarianto@202.x.x.x's password:
debug1: Enabling compression at level 6.
debug1: Authentication succeeded (password).
Authenticated to 202.x.x.x ([202.x.x.x]:22).
debug1: channel 0: new [client-session]
debug1: Sending command: scp -v -p -t .
File mtime 1323853868 atime 1380428748
Sending file timestamps: T1323853868 0 1380428748 0
Sink: T1323853868 0 1380428748 0
Sending file modes: C0600 97517300 messages.log
messages.log 100% 93MB 602.7KB/s 02:38
Transferred: sent 8905840, received 15768 bytes, in 162.5 seconds
Bytes per second: sent 54813.9, received 97.0
debug1: Exit status 0
debug1: compress outgoing: raw data 97571111, compressed 8806191, factor 0.09
debug1: compress incoming: raw data 7885, compressed 3821, factor 0.48

```

As you can see, when you are using compression, the transfer process is done in **162.5** seconds. It is **10** times faster than not using the “`-C`” parameter. If you are copying a lot of files across the network, the “`-C`” parameter would help you to decrease the total time you need.
The thing that we should notice is that the compression method will not work on any files. When the source file is already compressed, you will not find any improvement there. Files such as **.zip** , **.rar** , **pictures** , and **.iso** files will not be affected by the “`-C`” parameter.
By default, **SCP** uses “**AES-128** ” to encrypt files. If you want to change to another cipher to encrypt it, you can use the “`-c`” parameter.
Take a look at this command.
```
$ scp -c 3des Label.pdf mrarianto@202.x.x.x:.

mrarianto@202.x.x.x's password:
Label.pdf 100% 3672KB 282.5KB/s 00:13

```

The above command tells **SCP** to use the **3des algorithm** to encrypt the file. Please be careful that this parameter using “`-c`” not “`-C`“.
Another parameter that may be useful is the “`-l`” parameter. The “**-l** ” parameter will [limit the bandwidth to use](https://www.tecmint.com/limit-linux-network-bandwidth-usage-with-trickle/ "Limit Network Bandwidth Usage in Linux"). It will be useful if you do an automation script to copy a lot of files, but you don’t want the bandwidth to be drained by the **SCP** process.
```
$ scp -l 400 Label.pdf mrarianto@202.x.x.x:.

mrarianto@202.x.x.x's password:
Label.pdf 100% 3672KB 50.3KB/s 01:13

```

The **400** value behind the “`-l`” parameter is mean that we limit the bandwidth for the **SCP** process to only **50 KB/sec**.
One thing to remember is that bandwidth is specified in **Kilobits** /**sec** (**kbps**). It means that **8 bits** are equal to **1 byte**.
While **SCP** counts in **Kilobyte** /**sec** (**KB/s**). So if you want to limit your bandwidth to an **SCP** maximum of only **50** **KB/s** , you need to set it to **50 x 8** = **400**.
Usually, **SCP** is using port **22** as a default port, but for security reasons, you may [change the port to another port](https://www.tecmint.com/change-ssh-port-in-linux/ "How to Change SSH Port in Linux"). For example, we are using port **2249**.
Then the command should be like this.
```
$ scp -P 2249 Label.pdf mrarianto@202.x.x.x:.

mrarianto@202.x.x.x's password:
Label.pdf 100% 3672KB 262.3KB/s 00:14

```

Make sure that it uses a capital “`P`” not “`p`” since “`p`” is already used for preserved times and modes.
Sometimes we need to copy the directory and all **files/directories** inside it. It will be better if we can do it in a single command using the “`-r`” parameter, which copies the entire directory recursively.
```
$ scp -r documents mrarianto@202.x.x.x:.

mrarianto@202.x.x.x's password:
Label.pdf 100% 3672KB 282.5KB/s 00:13
scp.txt 100% 10KB 9.8KB/s 00:00

```

When the copy process is done, at the destination server you will find a directory named “**documents** ” with all its files. The folder “**documents** ” is automatically created.
If you choose not to see the progress meter and warning / diagnostic messages from SCP, you may disable it using the “`-q`” parameter. Here’s an example.
```
$ scp -q Label.pdf mrarianto@202.x.x.x:.

mrarianto@202.x.x.x's password:
pungki@mint ~/Documents $

```

As you can see, after you enter the password, there is no information about the SCP process. After the process is complete, you will see a prompt again.
The proxy server is usually used in the office environment. Natively, **SCP** is not a proxy configured. When your environment using a proxy, you have to “**tell** ” SCP to communicate with the proxy.
Here’s the scenario. The proxy address is **10.0.96.6** and the proxy port is **8080**. The proxy also implemented user authentication. First, you need to create the “**~/.ssh/config”** file. Second, you put this command inside it.
```
ProxyCommand /usr/bin/corkscrew 10.0.96.6 8080 %h %p ~/.ssh/proxyauth
```

Then you need to create the file “**~/.ssh/proxyauth** ” which contains.
```
myusername:mypassword
```

After that, you can do SCP transparently as usual.
Please notice that the **corkscrew** is might not be installed yet on your system. On my **Linux Mint** , I need to install it first, using the standard Linux Mint installation procedure.
```
$ apt-get install corkscrew

```

For other [yum-based systems](https://www.tecmint.com/redhat-based-linux-distributions/ "Best RedHat-based Linux Distributions"), users can install corkscrew using the following [yum command](https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/ "Linux YUM Command").
```
# yum install corkscrew
```

Another thing is that since the “**~/.ssh/proxyauth** ” file contains your “**username** ” and “**password** ” in clear-text format, please make sure that the file can be accessed by you only.
For mobile users who often switch between the company networks and public networks, it will be suffering to always change settings in SCP. It is better if we can put a different **ssh_config** file to match our needs.
Proxy is used in the company network but not in the public network and you regularly switch networks.
```
$ scp -F /home/pungki/proxy_ssh_config Label.pdf

mrarianto@202.x.x.x:.
mrarianto@202.x.x.x's password:
Label.pdf 100% 3672KB 282.5KB/s 00:13
```

By default “**ssh_config** ” file per user will be placed in “**~/.ssh/config** “. Creating a specific “**ssh_config** ” file with proxy compatibility will make it easier to switch between networks.
When you are on the company network, you can use the “`-F`” parameter. When you are on a public network, you can skip the “`-F`” parameter.
**You might also like:**
  * [Pscp – Transfer Files to Multiple Linux Servers](https://www.tecmint.com/copy-files-to-multiple-linux-servers/ "Pscp – Transfer Files to Multiple Linux Servers")
  * [How to Copy Files and Directories in Linux [14 cp Command Examples]](https://www.tecmint.com/cp-command-examples/ "How to Copy Files and Directories in Linux")
  * [10 sFTP Command Examples to Transfer Files in Linux](https://www.tecmint.com/sftp-command-examples/ "sFTP Command Examples")


That’s all about **SCP**. You can see **man pages** of **SCP** for more detail. Please feel free to leave comments and suggestions.
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Installation of Ubuntu 22.04 Server with LAMP Stack](https://www.tecmint.com/install-ubuntu-server-22-04/)
Next article:
[9 Practical Examples of Tail Command in Linux](https://www.tecmint.com/tail-command-linux/)
![Photo of author](https://secure.gravatar.com/avatar/25bda0197fec49687a4e647ed4a682a22e2217f1e9b3f9db1224bbc6fd6f7cb7?s=100&d=blank&r=g)
Pungki Arianto
Currently I am a Linux/Unix administrator. But I also play Windows both in server and desktop area. Interested in information technology, information security and writing.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/scp-commands-examples/#respond)** or
## Related Posts
[![Rsync Sync Files in Linux](https://www.tecmint.com/wp-content/uploads/2026/03/rsync-Sync-Files-in-Linux.webp)](https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/ "How to Use Rsync Command: 16 Examples for Linux File Sync")
[![ifconfig command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/ifconfig-command-in-Linux.webp)](https://www.tecmint.com/ifconfig-command-examples/ "15 Useful “ifconfig” Commands to Configure Network Interface in Linux")
[![Find Largest Files and Directories Size in Linux](https://www.tecmint.com/wp-content/uploads/2016/01/Find-Largest-Files-Directories-Size-in-Linux.png)](https://www.tecmint.com/find-top-large-directories-and-files-sizes-in-linux/ "How to Find Most Used Disk Space Directories and Files in Linux")
[![Find Which Process Using Port in Linux](https://www.tecmint.com/wp-content/uploads/2017/07/Find-Which-Process-Using-Port-in-Linux.png)](https://www.tecmint.com/find-out-which-process-listening-on-a-particular-port/ "4 Ways to Find Out Which Process Listening on a Particular Port")
[![Find Command Location and Description in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/Find-Command-Location-and-Description-in-Linux.webp)](https://www.tecmint.com/find-linux-command-description-and-location/ "How to Find Command Location and Description in Linux")
[![How to Use Column Command in Linux](https://www.tecmint.com/wp-content/uploads/2026/02/linux-column-command-examples.webp)](https://www.tecmint.com/linux-column-command/ "How to Use the Linux column Command to Format Text into Tables")
### 58 Comments
[Leave a Reply](https://www.tecmint.com/scp-commands-examples/#reply-title)
  1. I mistakenly closed the putty window after launching the copy with scp on VMWare Host. How can I view the progressive percentage by reconnecting?
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-1867490)
  2. Brilliant Post on Linux SCP command and usage…
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-1675510)
  3. Use **zmodem** for small files, much easier but a bit slower.
To copy a file to a Linux SSH terminal, just drag and drop it onto the terminal shell window (make sure you are in the right directory where you want the file to be.)
And to copy a file from Linux, back to your ssh terminal, just type “**sz filename.ext** “, and you will get a popup asking where to save it. This works at least with ZenTerm and Putty.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-1589080)
  4. Hi Team,
I am having some log files with different timestamps. What is the command for **scp** to get the files between two timestamps? Thanks in advance.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-1353504)
  5. Hi, I’m sending a directory of size **13G** to other servers using the SCP command. it is copying more than 36G and get No Space left on device error.
can you please let me know how that is possible
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-1332283)
  6. I liked the `-C` option. Saves time!
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-1203974)
  7. More then one option i.e. `-r` and `-v` can be used.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-1137644)
  8. Hi Pungki Arianto,
We’ve two servers, but how can we execute a file from another environment without providing passwords.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-1059875)
     * @Hemant,
For passwordless authentication, try to [setup SSH Passwordless login](https://www.tecmint.com/ssh-passwordless-login-using-ssh-keygen-in-5-easy-steps/) and then try to execute the file without entering password.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-1060152)
  9. Hi,
Is there any way to copy a file using scp without entering a password except sshkeygen? I want to put my credentials in a file and the scp script read this.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-1004437)
     * @Kundan,
Sorry there isn’t any way, the only option is SSH-Keygen i.e. [SSH Passwordless login](https://www.tecmint.com/ssh-passwordless-login-using-ssh-keygen-in-5-easy-steps/).
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-1004513)
  10. There are two Linux server, if i want to send 2 GB file from one to another, so from which command i can send? more importantly, i should get an email on my account that your file has been sent.
Please help me..
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-989759)
     * @Urwah,
To send file or directory from one Linux server to other Linux server use:
```
# scp source_file_name username@destination_host:destination_folder

```
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-990056)
  11. Thank you!very helpful
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-973665)
  12. While copying files from server to client using scp from server system RAM decreasing constantly how to limit it? Size of the file 90gb RAM 15gb in server machine..
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-879257)
  13. I used the below scp command to transfer files, but I don’t find the destination location where all the files copied successfully. I didn’t mention the destination location and put a dot in the end. Please help me to locate the files copied.
```
# scp sourcefile/*.fmb root@destination-host:.

```
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-821775)
     * @Fasih,
You can find all your files under root home directory, `dot (.)` means it will copy root current directory i.e. `/root`..
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-821808)
       * Thanks buddy. I got them.
thanks again :)
Fish
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-821898)
  14. Thanks for this very useful post. I see nowadays many universities are encouraging students to use SFTP and SSH instead of FTP, which I think is a good practice. I’m curious what you think about Web RTC and if you think it will be widely implement by individuals and companies.
—
Sam Smith
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-789819)
  15. Why do files often get missed when doing a transfer? We have a 400mb on server A and when finished transferring the folder size is 130mb on server B?
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-783284)
     * @Adam,
No that’s not possible, it should be same size on server B, may be you’re doing some mistake while transferring data from server A, please check carefully and do a transfer over scp..
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-783552)
     * Probably you did SCP recursively, that is copy all files and folders inside a folder being copied.
Use **SCP -r command** , see “Copy files inside directory recursively section above”
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-975865)
  16. I love it when looking around for linux tutorial and found a good one written by old friend. Hi Pungki!
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-766834)
     * Hi Dan, it’s nice to know that you read my article!
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-776511)
  17. It is useful article. But you may mention how to copy local to remote, remote to local, remote to remote and all. Anyway it’s good.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-614654)
  18. Nice Article. After reading entire article- Very impressive.. Most of the time I was used general scp -pr, now I understand the importance of this scp command with detailed info. New thing is learned scp -C… Good to hear all and very good article.(DBA)
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-591804)
  19. Nice article. Covers more useful SCP options in a detailed manner….. Helps me alot to learn about SCP command. thank you for your information..
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-506422)
  20. Great article. I had an issue with a password-less login via ssh and rsync. There was a Linux ftp server that had a mounted CIFS (Win2003) share on the back end. For the life of me I couldn’t get rsync to copy. So…my wild guess was the CIFS mount was under a windows security contact where as rsync had no access to.
I tried scp and now I can copy file (flawless).
Just my two cents. Again great article!
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-503444)
  21. Hi, thanks for sharing. One question: I try copy a folder in Linux to Windows… by command line in Linux. Exactly through .sh file (Is a automatic backup). Both PC are in same LAN. This is my instruction:
scp /srv/zimbra_mail/
But it doesn’t work. ¿Can you help me? Thanks
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-457980)
     * @Andres,
You can’t just scp from Linux to Windows..it would not work..to use scp both machines must be Linux..
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-458551)
     * SCP is part of SSH protocol. If you are copying between two machines then both needs to support SSH.
So if you need to copy from linux(by default ssh is included) to windows you will have to install SSH server on windows PC.
Any machine can support scp to any machine just note that both must have ssh server installed.
Thanks.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-491039)
       * @Namick,
I completely agree with your point..ssh is must on both end to communicate…
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-491302)
  22. How to send file from selected file (ls command) ?
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-381763)
     * I am not really understanding what you meant.
If you can get the filename from ls command, then you can put the file name after the scp command.
Example : $ scp file_name destination
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-382089)
  23. Helpful blog
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-286986)
  24. I SSHed into my iphone, and attempted to copy a file onto localhost. When asked for a password, i entered my password i use to log into the localhost, however i get a password incorrect error. any suggestions?
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-249820)
  25. I also want to let you know how this was helpful for me!
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-229172)
  26. Hi,
I just want to say you All guys for sharing helpful information . Please keep it up so we can learn a lot :) :)
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-228474)
  27. What is the path syntax for copying a file from a Linux box to a Windows box? I will have a key so my command would like:
scp $FILE_HOME/${CSV1} svc_usercopy@$job_server:”D:\Kronos Master File Directory\Employees\Employees Import.csv”
I don’t know if the Linux server cares what the Windows directory looks like or not. Any ideas on how this should look?
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-221002)
     * No idea, never ever tried this.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-221603)
  28. Excellent write up. Very helpful. Thank you! But the local user directory on Mac OS X wasn’t being recognized for me. It kept throwing me a ‘no such directory’ error. I could only get it to find a folder in my root directory, but the transfer broke off and nothing was actually copied, possibly due to permissions accessing a root directory, for which I needed a password just to create a new folder. Any suggestions?
My command was as follows, for copying remote to local: scp -prC root@lvps178-77-101-202:/var/www/vhosts ~/Downloads/ppcom-backup
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-148585)
  29. Incredibly useful stuff. Thank so much for publishing. -C is a life saver!
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-147055)
  30. This is a terrific post! It helped me to backup all of my data from my previous computer to my new one. The “scp -r” and you just saved me a lot of money! Haha
Thank you so much and keep going on sharing all of this helpful stuff to all the Linux community.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-143763)
  31. Hi,
Thanks for sharing important information, but however it does not solve my problem.
I have one backup server and one main ftp server. I have to execute a script from backup server to move the files from a path1 on main ftp server to another path2 on the same main ftp server. I can not use ssh for this.
Can you suggest me how can i perform this??
Any information and guidance will be appreciable.
Thanks again for the information.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-126917)
  32. Just wanted to know in detail how we can use different config file.
Would be really great if you provide the detailed description.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-114167)
  33. Thanks a lot for the info …
Its very useful.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-114162)
  34. Thanks a lot – very useful! Keep writing, please!
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-71021)
     * Thank you very much.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-72387)
  35. SCP displays the speed in KB/s would be better to say. You should clarify it more that the parameter expects bits, but it displays in bytes..
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-54684)
  36. “While SCP counts in Kilobyte/sec (KB/s). So if you want to limit your bandwidth for SCP maximum only 50 KB/s, you need to set it into 50 x 8 = 400.”
SCP counts in kilobits, you mean. Kb/s. Otherwise you wouldn’t have to multiply..
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-54682)
     * Yes. It was my mistake.
I mean SCP count in kilobits. I cross checked with SCP manual pages. Thank you
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-55184)
  37. It’s worth noting that rsync will happily copy over ssh and will therefore do all of the above with the same security but with much more powerful copying options.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-54613)
     * And rsync will also copy hidden files while scp does not
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-377237)
  38. scp -Cpv messages.log mrarianto@202.x.x.x:.
compress option most useful to me as i transfer lot of files that could be compressed.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-54568)
     * Thank you. Nice to see this article can be useful
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-55175)
  39. nice write up on most common scp usage examples. it will surely be useful to anyone looking on how to use scp.
to add to it, one can also use scp to edit/create files remotely using vim+scp. for example, to edit /etc/hosts on a remote server where ssh is listening on port 8822 one can do:
vim scp://root@:8822//etc/hosts
if ssh is on its default port 22 then the :8822 part can be omitted
it comes handy sometimes so I thought will share it with you ;)
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-54378)
     * Thank you for your share. It is handy :)
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-55185)
  40. Thanks, great and valuable summary.
[Reply](https://www.tecmint.com/scp-commands-examples/#comment-54161)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/scp-commands-examples/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
[ ](https://www.tecmint.com/scp-commands-examples/ "Scroll back to top")
Search for:
![Freestar](https://a.pub.network/core/imgs/fslogo-green.svg)
![](https://ids.ad.gt/api/v1/halo_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q&halo_id=060kjedj2g597969c979c9f999d66666666ywmkwsqy62606i626i6o666k000000)![](https://ids4.ad.gt/api/v1/ip_match?id=AU1D-0100-001772949750-XXM2FI1H-SG2Q)
