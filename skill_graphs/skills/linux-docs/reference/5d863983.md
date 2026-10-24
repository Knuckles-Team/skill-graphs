# Level Up Linux: 20 Advanced Commands for Mid-Level Users
[Ravi Saive](https://www.tecmint.com/author/admin/ "View all posts by Ravi Saive")Last Updated: February 27, 2024 Read Time: 10 minsCategories [Linux Commands](https://www.tecmint.com/category/linux-commands/) [56 Comments](https://www.tecmint.com/20-advanced-commands-for-middle-level-linux-users/#comments)
You may have found the first article, ‘[Useful Commands for Beginners](https://www.tecmint.com/useful-linux-commands-for-newbies/ "Linux Commands for Newbies")‘ very helpful, as it was intended for newbies, this article is tailored for middle-level and advanced users.
It covers topics such as customizing search, [understanding processes](https://www.tecmint.com/linux-process-management/ "Processes in Linux") and how to [terminate them](https://www.tecmint.com/find-and-kill-running-processes-pid-in-linux/ "Kill Running Processes in Linux"), optimizing the [Linux terminal for productivity](https://www.tecmint.com/linux-terminal-emulators/ "Best Linux Terminals"), and compiling C, C++, and Java programs in a Unix-like environment.
### 21. find Command
The [find command](https://www.tecmint.com/35-practical-examples-of-linux-find-command/ "Linux Find Command") is used to search for files in the given directory, hierarchically starting at the parent directory and moving to sub-directories.
```
find -name *.sh

```
![Find All Files with Extension](https://www.tecmint.com/wp-content/uploads/2013/05/Find-All-Files-with-Extension.png)Find All Files with Extension
The `-name` option makes the search case sensitive. You can use the `-iname` option to find case-insensitive files with different capitalization patterns in the extension.
The `*` is a wildcard and searches all the files having an extension `.sh` you can use a filename or a part of the file name to customize the output.
```
find -iname *.SH

```

The following command is used to search for all files having extension `".tar.gz"` in the current directory and its subdirectories including mounted devices.
```
find -name *.tar.gz

```

### 22. grep Command
The [grep command](https://www.tecmint.com/12-practical-examples-of-linux-grep-command/ "Linux Grep Command") searches a specified file for lines that contain a match to provided strings or words.
In this case, it is used to search for the ‘**tecmint** ‘ user in the ‘**/etc/passwd** ‘ file.
```
grep tecmint /etc/passwd

```

The `-i` option is used to search for the string “**TECMINT** ” (case-insensitive) in the ‘**/etc/passwd** ‘ file.
```
grep -i TECMINT /etc/passwd

```

The `-r` option is used to recursively search for the string “**127.0.0.1** ” in the ‘**/etc/hosts** ‘ file.
```
grep -r "127.0.0.1" /etc/hosts

```
![Grep Case-Insensitive String in File](https://www.tecmint.com/wp-content/uploads/2013/05/Grep-Case-Insensitive-String-in-File.png)Grep Case-Insensitive String in File
### 23. man Command
The [man command](https://www.tecmint.com/linux-man-pages/ "Use Man Pages in Linux") is the system’s manual pager, which provides online documentation for all the possible options with a command and its usage.
Almost all the [Linux commands](https://www.tecmint.com/essential-linux-commands/ "Essential Linux Commands") come with their corresponding manual pages. For example, the following ‘**man cat** ‘ (Manual page for [cat command](https://www.tecmint.com/13-basic-cat-command-examples-in-linux/)) and ‘**man ls** ‘ (Manual page for [command ls](https://www.tecmint.com/15-basic-ls-command-examples-in-linux/)) display the manual pages for a given command.
```
man cat
man ls

```
![View Command Manual Pages](https://www.tecmint.com/wp-content/uploads/2013/05/View-Command-Manual-Pages.png)View Command Manual Pages
### 24. ps Command
The [ps command](https://www.tecmint.com/ps-command-examples-for-linux-process-monitoring/ "ps Command Examples") gives the status of running processes with a unique **ID** called **PID**.
```
ps

```

To [list status of all the processes](https://www.tecmint.com/find-linux-processes-memory-ram-cpu-usage/ "Find Top Running Processes") along with process **ID** and **PID** , use option `-A`.
```
ps -A

```

The **ps** command is very useful when you want to know which processes are running or may need **PID** sometimes, for a [process to be killed](https://www.tecmint.com/find-and-kill-running-processes-pid-in-linux/ "Kill Running Processes in Linux"). You can use it with the grep command to find customized output.
```
ps -A | grep -i ssh

```

Here **ps** is pipelined with **grep** command to find customised and relevant output of our need.
![List Currently Running Processes](https://www.tecmint.com/wp-content/uploads/2013/05/List-Currently-Running-Processes.png)List Currently Running Processes
### 25. kill Command
The [kill command](https://www.tecmint.com/how-to-kill-a-process-in-linux/ "Kill a Process in Linux") in Linux is crucial for terminating unresponsive or irrelevant processes efficiently. Unlike Windows, where restarting is often required after killing a process, Linux allows you to kill and restart processes without rebooting the entire system.
For example, if you need to terminate the ‘**firefox** ‘ program if it’s not responding, you can use the **ps** command along with **grep** to find the process pid and then use the ‘**kill** ‘ command to stop the process.
```
ps -A | grep -i firefox
kill 69881

```

Every time you re-run a process or start a system, a new **pid** is generated for each process and you can know about the currently running processes and their **pid** using the command ‘**ps** ‘.
![Kill Running Processes](https://www.tecmint.com/wp-content/uploads/2013/05/Kill-Running-Processes.png)Kill Running Processes
Another way to kill the same process is.
```
pkill apache2

```

The **kill** command requires **job id/process****id** for sending signals, whereas, in **pkill** , you have an option of using a pattern, specifying process owner, etc.
### 26. whereis Command
The [whereis command](https://www.tecmint.com/find-linux-command-description-and-location/ "Find a ‘Binary Command’ Description") is used to locate the **Binary** , **Sources,** and **Manual Pages** of the command.
For example, to locate the **Binary** , **Sources,** and **Manual Pages** of the command ‘**ls** ‘ and ‘**kill** ‘.
```
whereis ls
whereis kill

```
![Find Command Binary Location](https://www.tecmint.com/wp-content/uploads/2013/05/Find-Command-Binary-Location.png)Find Command Binary Location
The **whereis** command is useful to know where the binaries are installed for manual editing sometimes.
### 27. systemctl Command
The [systemctl command](https://www.tecmint.com/manage-services-using-systemd-and-systemctl-in-linux/ "Manage Services Using Systemctl") controls the starting, stopping, restarting, enabling, disabling, and checking of the status of a service or program.
```
sudo systemctl start sshd
sudo systemctl stop sshd
sudo systemctl restart sshd
sudo systemctl enable sshd
sudo systemctl disable sshd
sudo systemctl status sshd

```

### 28. alias Command
The [alias command](https://www.tecmint.com/create-alias-in-linux/ "Create Alias in Linux") is a built-in shell command that lets you assign a name for a long command or [frequently used command](https://www.tecmint.com/remember-linux-commands/ "Remember Linux Commands").
I frequently use the [‘ls -l’ command](https://www.tecmint.com/ls-command-in-linux/ "Basic ls Command Examples"), which consists of 5 characters, including spaces. Therefore, I created an alias for it as `'l'`.
```
alias l='ls -l'

```

check if it works or not.
```
l

```
![Create Command Alias in Linux](https://www.tecmint.com/wp-content/uploads/2013/05/Create-Command-Alias-in-Linux.png)Create Command Alias in Linux
To remove alias `'l'`, use the following ‘**unalias** ‘ command.
```
unalias l

```

check, if ‘**l** ‘ still is an alias or not.
```
l

l: command not found

```

Adding a bit of [fun to Linux commands](https://www.tecmint.com/funny-linux-commands/ "Funniest Linux Commands") by creating aliases for specific important commands to other important commands.
```
alias cd='ls -l' (set alias of ls -l to cd)
alias su='pwd'   (set alias of pwd to su)

```

Now, imagine the humor when your friend types the [cd command](https://www.tecmint.com/cd-command-in-linux/ "cd Command in Linux"), expecting to change directories but instead gets a directory listing. Similarly, if he attempts ‘**su** ‘, all he sees is the location of the working directory.
You can remove the alias later using the ‘**unalias** ‘ command, as explained above.
### 29. df Command
The [df command](https://www.tecmint.com/how-to-check-disk-space-in-linux/ "Check Disk Space Usage") is used to show the information about disk space usage on the file system. It shows the total, used, and available space on each mounted file system.
```
df -h

```

The `-h` option is used to print the disk space usage in a human-readable format, showing sizes in gigabytes (GB) and megabytes (MB) for each mounted file system on your system.
![Show Linux Disk Usage](https://www.tecmint.com/wp-content/uploads/2013/05/Show-Linux-Disk-Usage.png)Show Linux Disk Usage
### 30. du Command
The [du command](https://www.tecmint.com/check-linux-disk-usage-of-files-and-directories/ "Find Disk Usage of Files") is used to show the disk space usage of files and directories, which includes the total disk space occupied by a specific file or directory, including the space used by its subdirectories.
```
du -h

```

The `-h` option is used to print the file usage in a human-readable format, showing sizes in gigabytes (GB) and megabytes (MB).
![Show File Disk Usage](https://www.tecmint.com/wp-content/uploads/2013/05/Show-File-Disk-Usage.png)Show File Disk Usage
### 31. rm Command
The [rm command](https://www.tecmint.com/remove-directory-linux/ "Delete Files in Linux") stands for remove, which is used to remove or delete files and directories permanently from the file system.
The basic syntax for removing a file is:
```
rm file

```

The basic syntax for removing a directory is:
```
rm -rf directory

```

The `-r` (recursive, removes directories and their contents) and `-f` (force remove files without prompts for confirmation).
The `"rm -rf"` command is a destructive command. If you accidentally execute it in the wrong directory, all files and the directory itself are permanently lost.
### 32. echo Command
The [echo command](https://www.tecmint.com/echo-command-in-linux/ "echo command in Linux") as the name suggests echoes a text on the standard output. It has nothing to do with the shell, nor does the shell read the output of the echo command.
However, in an interactive script, an echo passes the message to the user through the terminal. It is one of the commands that is commonly used in scripting, interactive scripting.
```
echo "Tecmint.com is a very good website"

Tecmint.com is a very good website

```

Let’s create a small interactive bash script that will display a personalized welcome message on the terminal.
```
#!/bin/bash

echo "Welcome to the Interactive Welcome Script!"
echo "----------------------------------------"

# Prompt the user to enter their name
echo "Please enter your name:"
read name

# Display a personalized welcome message
echo "Hello, $name! Welcome to the interactive script. Have a great day!"

```

Save this script in a file, for example, **welcome_script.sh,** and make the script executable using the command.
```
chmod +x welcome_script.sh

```

Then, you can run it by typing in the terminal.
```
./welcome_script.sh

```
![Interactive Bash Script](https://www.tecmint.com/wp-content/uploads/2024/02/Interactive-Bash-Script.png)Interactive Bash Script
### 33. passwd Command
The **passwd** command is used to change own password or another user’s password when executed by the sudo privileges.
For example, to change the password for the current user, simply type:
```
passwd

```

If you have the sudo privileges, you can change another user’s password by specifying the username:
```
sudo passwd username

```

### 34. lpr Command
The **lpr** command is used for submitting print jobs to a printer. It sends files to a printer’s print queue, allowing users to print documents from the command line.
```
lpr document.txt

```

The ‘**lpq** ‘ command lets you view the status of a printer (whether it’s up or not), and the jobs (files) waiting to be printed.
### 35. cmp Command
The **cmp** command compares two files of any type and writes the results to the standard output. By default, ‘**cmp** ‘ returns 0 if the files are the same; if they differ, the byte and line number at which the first difference occurred is reported.
To provide examples for the **cmp** command, let’s consider two files:
```
cat file1.txt

Hi My name is Tecmint

```
```
cat file2.txt

Hi My name is tecmint [dot] com

```

Now, let’s compare two files and see the output of the command.
```
cmp file1.txt file2.txt

file1.txt file2.txt differ: byte 15, line 1
```

### 36. wget Command
The [wget command](https://www.tecmint.com/10-wget-command-examples-in-linux/ "Wget Command in Linux") is a free utility for non-interactive (i.e., can work in the background) download of files from the web. It supports **HTTP** , **HTTPS** , **FTP** protocols, and **HTTP** proxies.
For example, to download a file named “[Server-Health.sh](https://www.tecmint.com/basic-shell-programming-part-ii/ "Shell Scripts for Linux")” from a website, you would use:
```
wget https://www.tecmint.com/wp-content/scripts/Server-Health.sh

```

### 37. mount Command
The **mount** command is used to mount a filesystem that doesn’t mount itself. You need root permission to mount a device.
First, run ‘**lsblk** ‘ after plugging in your filesystem and identify your device, and note down your device’s assigned name.
```
lsblk

NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0 931.5G  0 disk
├─sda1   8:1    0 923.6G  0 part /
├─sda2   8:2    0     1K  0 part
└─sda5   8:5    0   7.9G  0 part [SWAP]
sr0     11:0    1  1024M  0 rom
sdb      8:16   1   3.7G  0 disk
└─sdb1   8:17   1   3.7G  0 part
```

From this screen it was clear that I plugged in a **4 GB** pendrive thus ‘**sdb1** ‘ is my filesystem to be mounted. Become a **root** to perform this operation and change to the **/dev** directory where all the file system is mounted.
```
su
cd /dev

```

Create a directory named anything that should be relevant for reference.
```
mkdir usb

```

Now mount filesystem ‘**sdb1** ‘ to directory ‘**usb** ‘.
```
mount /dev/sdb1 /dev/usb

```

Now you can navigate to **/dev/usb** from the terminal or **X-windows** system and access files from the mounted directory.
### 38. gcc Command
The **gcc** is the in-built compiler for the ‘**c** ‘ language in the linux environment. A simple **c** program, save it on your desktop as **Hello.c** (remember the ‘**.c** ‘ extension is a must).
```
#include <stdio.h>
int main()
{
  printf("Hello world\n");
  return 0;
}
```

Next, compile and run it.
```
gcc Hello.c
./a.out

Hello world

```

On compiling a **c** program the output is automatically generated to a new file “**a.out** ” and every time you compile a **c** program same file “**a.out** ” gets modified.
Hence it is good advice to define an output file during compilation and thus there is no risk of overwriting to output file.
```
gcc -o Hello Hello.c

```

Here ‘**-o** ‘ sends the output to the ‘**Hello** ‘ file and not ‘**a.out** ‘.
### 39. g++ Command
The **g++** is the in-built compiler for ‘**C++** ‘ , the first object-oriented programming language. A simple **C++** program, save it on your desktop as **Add.cpp** (remember the ‘**.cpp** ‘ extension is a must).
```
#include <iostream>

using namespace std;

int main()
    {
          int a;
          int b;
          cout<<"Enter first number:\n";
          cin >> a;
          cout <<"Enter the second number:\n";
          cin>> b;
          cin.ignore();
          int result = a + b;
          cout<<"Result is"<<"  "<<result<<endl;
          cin.get();
          return 0;
     }

```

Next, compile and run it.
```
g++ Add.cpp
./a.out

Enter the first number:
...
...

```

On compiling a **C++** program the output is automatically generated to a new file “**a.out** ” and every time you compile a **C++** program same file “**a.out** ” gets modified.
Hence it is good advice to define an output file during compilation and thus there is no risk of overwriting to output file.
```
g++ -o Add Add.cpp
./Add

Enter the first number:
...
...

```

### 40. java Command
**Java** is one of the world’s highly used programming languages and is considered fast, secure, and reliable. Most of the web-based service of today runs on Java.
Create a simple Java program by pasting the below test to a file, named **tecmint.java** (remember the ‘**.java** ‘ extension is a must).
```
class tecmint {
  public static void main(String[] arguments) {
    System.out.println("Tecmint ");
  }
}
```

Next, compile and run it.
```
javac tecmint.java
java tecmint

```

Almost every distribution comes packed with a **gcc compiler** , major number of distros have inbuilt **G++** and **Java compilers** , while some may not. You can [apt](https://www.tecmint.com/apt-command-in-linux/ "apt Command") or [yum](https://www.tecmint.com/20-linux-yum-yellowdog-updater-modified-commands-for-package-mangement/ "Yum Command") the required package.
Don’t forget to mention your valuable comment and the type of article you want to see here. I will soon be back with an interesting topic about the [lesser-known facts about Linux](https://www.tecmint.com/lesser-known-facts-about-gnu-linux/ "Linux Facts You Probably Didn’t Know").
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[Top 5 Command Line Browsers for Linux](https://www.tecmint.com/command-line-web-browsers/)
Next article:
[6 Most Notable Open Source Centralized Log Management Tools](https://www.tecmint.com/open-source-centralized-linux-log-management-tools/)
![Photo of author](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=100&d=blank&r=g)
Ravi Saive
I'm Ravi Saive, an award-winning entrepreneur and founder of several successful 5-figure online businesses, including TecMint.com, GeeksMint.com, UbuntuMint.com, and the premium learning hub Pro.Tecmint.com.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/20-advanced-commands-for-middle-level-linux-users/#respond)** or
