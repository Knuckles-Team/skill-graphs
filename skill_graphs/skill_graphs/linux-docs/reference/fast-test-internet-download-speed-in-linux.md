[Skip to content](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#content "Skip to content")
**NEW:** Get Lifetime access to 8 courses, 3 certifications, 5 eBooks, and all future courses for just $199 - [[Claim Offer]](https://pro.tecmint.com/lifetime/)
[ ![Tecmint: Linux Howtos, Tutorials & Guides](https://www.tecmint.com/wp-content/uploads/2020/07/logo.png) ](https://www.tecmint.com/ "Tecmint: Linux Howtos, Tutorials & Guides")
[](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/)
Menu
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
  * [Pro Courses](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/)
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
  * [Pro Courses](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/ "Linux Online Courses")
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


[](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/)
# 10 Strace Commands for Troubleshooting and Debugging Linux Processes
[Aaron Kili](https://www.tecmint.com/author/aaronkili/ "View all posts by Aaron Kili")Last Updated: October 25, 2017 Read Time: 11 minsCategories [Monitoring Tools](https://www.tecmint.com/category/monitoring-tools/) [4 Comments](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#comments)
**strace** is a powerful command line tool for debugging and trouble shooting programs in Unix-like operating systems such as Linux. It captures and records all system calls made by a process and the signals received by the process.
**Read Also** : [How to Audit Linux Process Using ‘autrace’ on CentOS/RHEL](https://www.tecmint.com/audit-linux-process-using-autrace-on-centos-rhel/)
It displays the name of each system call together with its arguments enclosed in a parenthesis and its return value to standard error; you can optionally redirect it to a file as well.
In this article, we will explain 10 strace command examples for troubleshooting and debugging programs and processes in a Linux system.
### How to Install Strace Process Monitoring Tool in Linux
If **strace** is not pre-installed on your Linux system, run the appropriate command below for your distribution, to install it.
```
$ sudo apt install strace	#Debian/Ubuntu
# yum install strace		#RHEL/CentOS
# dnf install strace		#Fedora 22+

```

In case a program crashes or behaves in a way not expected, you can go through its systems calls to get a clue of what exactly happened during its execution. As we will see later on, system calls can be categorized under different events: those relating to process management, those that take a file as an argument, those that involve networking, memory mapping, signals, IPC and also file descriptor related system calls.
You can either run a program/command with strace or pass a PID to it using the `-p` option as in the following examples.
### 1. Trace Linux Command System Calls
You can simply run a command with **strace** like this, here we are tracing of all system calls made by the [df command](https://www.tecmint.com/how-to-check-disk-space-in-linux/).
```
**$ strace df -h**

execve("/bin/df", ["df", "-h"], [/* 50 vars */]) = 0
brk(NULL)                               = 0x136e000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f82f78fd000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
**open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3**
fstat(3, {st_mode=S_IFREG|0644, st_size=147662, ...}) = 0
mmap(NULL, 147662, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f82f78d8000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0P\t\2\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=1868984, ...}) = 0
mmap(NULL, 3971488, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f82f7310000
...

```

From the output above, you can see various types of system calls made by **df command** , for example.
```
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3

```

Where:
  * **open** – is the type of system call
  * **(“/etc/ld.so.cache”, O_RDONLY|O_CLOEXEC)** – system call argument
  * **3** – system call return value


Below is an sample output showing the write system calls, that displays **df command** output on the screen.
```
mmap(NULL, 26258, PROT_READ, MAP_SHARED, 3, 0) = 0x7f82f78f5000
close(3)                                = 0
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 1), ...}) = 0
write(1, "Filesystem      Size  Used Avail"..., 49Filesystem      Size  Used Avail Use% Mounted on
) = 49
write(1, "udev            3.9G     0  3.9G"..., 43udev            3.9G     0  3.9G   0% /dev
) = 43
write(1, "tmpfs           788M  9.6M  779M"..., 43tmpfs           788M  9.6M  779M   2% /run
) = 43
write(1, "/dev/sda10      324G  252G   56G"..., 40/dev/sda10      324G  252G   56G  82% /
) = 40
write(1, "tmpfs           3.9G  104M  3.8G"..., 47tmpfs           3.9G  104M  3.8G   3% /dev/shm
) = 47
write(1, "tmpfs           5.0M  4.0K  5.0M"..., 48tmpfs           5.0M  4.0K  5.0M   1% /run/lock
) = 48
write(1, "tmpfs           3.9G     0  3.9G"..., 53tmpfs           3.9G     0  3.9G   0% /sys/fs/cgroup
) = 53
write(1, "cgmfs           100K     0  100K"..., 56cgmfs           100K     0  100K   0% /run/cgmanager/fs
) = 56
write(1, "tmpfs           788M   36K  788M"..., 53tmpfs           788M   36K  788M   1% /run/user/1000
) = 53
close(1)                                = 0
close(2)                                = 0
exit_group(0)                           = ?
+++ exited with 0 +++

```

### 2. Trace Linux Process PID
If a process is already running, you can trace it by simply passing its **PID** as follows; this will fill your screen with continues output that shows system calls being made by the process, to end it, press `[Ctrl + C]`.
```
**$ sudo strace -p 3569**

strace: Process 3569 attached
restart_syscall(<... resuming interrupted poll ...>) = 1
recvmsg(4, {msg_name(0)=NULL, msg_iov(1)=[{"U\2\24\300!\247\330\0\3\24\4\0\20\0\0\0\0\0\0\24\24\24\24\24\0\0\3\37%\2\0\0", 4096}], msg_controllen=0, msg_flags=0}, 0) = 32
recvmsg(4, 0x7ffee4dbf870, 0)           = -1 EAGAIN (Resource temporarily unavailable)
recvmsg(4, 0x7ffee4dbf850, 0)           = -1 EAGAIN (Resource temporarily unavailable)
poll([{fd=3, events=POLLIN}, {fd=4, events=POLLIN}, {fd=5, events=POLLIN}, {fd=10, events=POLLIN}, {fd=30, events=POLLIN}, {fd=31, events=POLLIN}], 6, -1) = 1 ([{fd=31, revents=POLLIN}])
read(31, "\372", 1)                     = 1
recvmsg(4, 0x7ffee4dbf850, 0)           = -1 EAGAIN (Resource temporarily unavailable)
poll([{fd=3, events=POLLIN}, {fd=4, events=POLLIN}, {fd=5, events=POLLIN}, {fd=10, events=POLLIN}, {fd=30, events=POLLIN}, {fd=31, events=POLLIN}], 6, 0) = 1 ([{fd=31, revents=POLLIN}])
read(31, "\372", 1)                     = 1
recvmsg(4, 0x7ffee4dbf850, 0)           = -1 EAGAIN (Resource temporarily unavailable)
poll([{fd=3, events=POLLIN}, {fd=4, events=POLLIN}, {fd=5, events=POLLIN}, {fd=10, events=POLLIN}, {fd=30, events=POLLIN}, {fd=31, events=POLLIN}], 6, 0) = 0 (Timeout)
mprotect(0x207faa20000, 8192, PROT_READ|PROT_WRITE) = 0
mprotect(0x207faa20000, 8192, PROT_READ|PROT_EXEC) = 0
mprotect(0x207faa21000, 4096, PROT_READ|PROT_WRITE) = 0
mprotect(0x207faa21000, 4096, PROT_READ|PROT_EXEC) = 0
...

```

### 3. Get Summary of Linux Process
Using the `-c` flag, you can generate a report of total time, calls, and errors for each system call, as follows.
```
**$ sudo strace -c -p 3569**

strace: Process 3569 attached

^Cstrace: Process 3569 detached
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 99.73    0.016000           8      1971           poll
  0.16    0.000025           0       509        75 futex
  0.06    0.000010           0      1985      1966 recvmsg
  0.06    0.000009           0      2336           mprotect
  0.00    0.000000           0       478           read
  0.00    0.000000           0        13           write
  0.00    0.000000           0        29           mmap
  0.00    0.000000           0         9           munmap
  0.00    0.000000           0        18           writev
  0.00    0.000000           0       351           madvise
  0.00    0.000000           0         1           restart_syscall
------ ----------- ----------- --------- --------- ----------------
100.00    0.016044                  7700      2041 total

```

### 4. Print Instruction Pointer During System Call
The `-i` option displays the instruction pointer at the time of each system call made by the program.
```
**$ sudo strace -i df -h**

[00007f0d7534c777] execve("/bin/df", ["df", "-h"], [/* 17 vars */]) = 0
[00007faf9cafa4b9] brk(NULL)            = 0x12f0000
[00007faf9cafb387] access("/etc/ld.so.nohwcap", F_OK) = -1 ENOENT (No such file or directory)
[00007faf9cafb47a] mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7faf9cd03000
[00007faf9cafb387] access("/etc/ld.so.preload", R_OK) = -1 ENOENT (No such file or directory)
[00007faf9cafb327] open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
[00007faf9cafb2b4] fstat(3, {st_mode=S_IFREG|0644, st_size=147662, ...}) = 0
[00007faf9cafb47a] mmap(NULL, 147662, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7faf9ccde000
[00007faf9cafb427] close(3)             = 0
[00007faf9cafb387] access("/etc/ld.so.nohwcap", F_OK) = -1 ENOENT (No such file or directory)
[00007faf9cafb327] open("/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
[00007faf9cafb347] read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0P\t\2\0\0\0\0\0"..., 832) = 832
[00007faf9cafb2b4] fstat(3, {st_mode=S_IFREG|0755, st_size=1868984, ...}) = 0
[00007faf9cafb47a] mmap(NULL, 3971488, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7faf9c716000
[00007faf9cafb517] mprotect(0x7faf9c8d6000, 2097152, PROT_NONE) = 0
...

```

### 5. Show Time of Day For Each Trace Output Line
You can also print the time of day for each line in the trace output, by passing the `-t` flag.
```
**$ sudo strace -t df -h**

15:19:25 execve("/bin/df", ["df", "-h"], [/* 17 vars */]) = 0
15:19:25 brk(NULL)                      = 0x234c000
15:19:25 access("/etc/ld.so.nohwcap", F_OK) = -1 ENOENT (No such file or directory)
15:19:25 mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f8c7f1d9000
15:19:25 access("/etc/ld.so.preload", R_OK) = -1 ENOENT (No such file or directory)
15:19:25 open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
15:19:25 fstat(3, {st_mode=S_IFREG|0644, st_size=147662, ...}) = 0
15:19:25 mmap(NULL, 147662, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f8c7f1b4000
15:19:25 close(3)                       = 0
15:19:25 access("/etc/ld.so.nohwcap", F_OK) = -1 ENOENT (No such file or directory)
15:19:25 open("/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
15:19:25 read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0P\t\2\0\0\0\0\0"..., 832) = 832
15:19:25 fstat(3, {st_mode=S_IFREG|0755, st_size=1868984, ...}) = 0
15:19:25 mmap(NULL, 3971488, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f8c7ebec000
15:19:25 mprotect(0x7f8c7edac000, 2097152, PROT_NONE) = 0
...

```

### 6. Print Command Time Spent in System Calls
To shows the time difference between the starting and the end of each system call made by a program, use the `-T` option.
```
**$ sudo strace -T df -h**

execve("/bin/df", ["df", "-h"], [/* 17 vars */]) = 0 <0.000287>
brk(NULL)                               = 0xeca000 <0.000035>
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory) <0.000028>
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f9aff2b1000 <0.000020>
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory) <0.000019>
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3 <0.000022>
fstat(3, {st_mode=S_IFREG|0644, st_size=147662, ...}) = 0 <0.000015>
mmap(NULL, 147662, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f9aff28c000 <0.000019>
close(3)                                = 0 <0.000014>
...

```

### 7. Trace Only Specific System Calls
In the command below, `trace=write` is known as a qualifying expression, where **trace** is a qualifier (others include signal, abbrev, verbose, raw, read, or write). Here, **write** is the value of the qualifier.
The following command actually shows the system calls to print **df** output on standard output.
```
**$ sudo strace -e trace=write df -h**

write(1, "Filesystem      Size  Used Avail"..., 49Filesystem      Size  Used Avail Use% Mounted on
) = 49
write(1, "udev            3.9G     0  3.9G"..., 43udev            3.9G     0  3.9G   0% /dev
) = 43
write(1, "tmpfs           788M  9.6M  779M"..., 43tmpfs           788M  9.6M  779M   2% /run
) = 43
write(1, "/dev/sda10      324G  252G   56G"..., 40/dev/sda10      324G  252G   56G  82% /
) = 40
write(1, "tmpfs           3.9G  104M  3.8G"..., 47tmpfs           3.9G  104M  3.8G   3% /dev/shm
) = 47
write(1, "tmpfs           5.0M  4.0K  5.0M"..., 48tmpfs           5.0M  4.0K  5.0M   1% /run/lock
) = 48
write(1, "tmpfs           3.9G     0  3.9G"..., 53tmpfs           3.9G     0  3.9G   0% /sys/fs/cgroup
) = 53
write(1, "cgmfs           100K     0  100K"..., 56cgmfs           100K     0  100K   0% /run/cgmanager/fs
) = 56
write(1, "tmpfs           788M   28K  788M"..., 53tmpfs           788M   28K  788M   1% /run/user/1000
) = 53
+++ exited with 0 +++

```

Here are some additional commands about trace qualifier.
```
$ sudo strace -e trace=open,close df -h
$ sudo strace -e trace=open,close,read,write df -h
$ sudo strace -e trace=all df -h

```

### 8. Trace System Calls Based on a Certain Condition
Let’s look at how to trace system calls relating to a given class of events. This command can be used to trace all system calls involving process management.
```
**$ sudo strace -q -e trace=process df -h**

execve("/bin/df", ["df", "-h"], [/* 17 vars */]) = 0
arch_prctl(ARCH_SET_FS, 0x7fe2222ff700) = 0
Filesystem      Size  Used Avail Use% Mounted on
udev            3.9G     0  3.9G   0% /dev
tmpfs           788M  9.6M  779M   2% /run
/dev/sda10      324G  252G   56G  82% /
tmpfs           3.9G  104M  3.8G   3% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           3.9G     0  3.9G   0% /sys/fs/cgroup
cgmfs           100K     0  100K   0% /run/cgmanager/fs
tmpfs           788M   28K  788M   1% /run/user/1000
exit_group(0)                           = ?
+++ exited with 0 +++

```

Next, to trace all system calls that take a filename as an argument, run this command.
```
**$ sudo strace -q  -e trace=file df -h**

execve("/bin/df", ["df", "-h"], [/* 17 vars */]) = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
open("/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = 3
open("/usr/share/locale/locale.alias", O_RDONLY|O_CLOEXEC) = 3
...

```

To trace all system calls involving memory mapping, type.
```
**$ sudo strace -q -e trace=memory df -h**

brk(NULL)                               = 0x77a000
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fe8f4658000
mmap(NULL, 147662, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7fe8f4633000
mmap(NULL, 3971488, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fe8f406b000
mprotect(0x7fe8f422b000, 2097152, PROT_NONE) = 0
mmap(0x7fe8f442b000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1c0000) = 0x7fe8f442b000
mmap(0x7fe8f4431000, 14752, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fe8f4431000
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fe8f4632000
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fe8f4631000
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fe8f4630000
mprotect(0x7fe8f442b000, 16384, PROT_READ) = 0
mprotect(0x616000, 4096, PROT_READ)     = 0
mprotect(0x7fe8f465a000, 4096, PROT_READ) = 0
munmap(0x7fe8f4633000, 147662)          = 0
mmap(NULL, 2981280, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7fe8f3d93000
brk(NULL)                               = 0x77a000
brk(0x79b000)                           = 0x79b000
mmap(NULL, 619, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7fe8f4657000
mmap(NULL, 26258, PROT_READ, MAP_SHARED, 3, 0) = 0x7fe8f4650000
Filesystem      Size  Used Avail Use% Mounted on
udev            3.9G     0  3.9G   0% /dev
tmpfs           788M  9.6M  779M   2% /run
/dev/sda10      324G  252G   56G  82% /
tmpfs           3.9G  104M  3.8G   3% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           3.9G     0  3.9G   0% /sys/fs/cgroup
cgmfs           100K     0  100K   0% /run/cgmanager/fs
tmpfs           788M   28K  788M   1% /run/user/1000
+++ exited with 0 +++

```

You can trace all network and signals related system calls.
```
$ sudo strace -e trace=network df -h
$ sudo strace -e trace=signal df -h

```

### 9. Redirect Trace Output to File
To write the trace messages sent to standard error to a file, use the `-o` option. This means that only the command output is printed on the screen as shown below.
```
**$ sudo strace -o df_debug.txt df -h**

Filesystem      Size  Used Avail Use% Mounted on
udev            3.9G     0  3.9G   0% /dev
tmpfs           788M  9.6M  779M   2% /run
/dev/sda10      324G  252G   56G  82% /
tmpfs           3.9G  104M  3.8G   3% /dev/shm
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           3.9G     0  3.9G   0% /sys/fs/cgroup
cgmfs           100K     0  100K   0% /run/cgmanager/fs
tmpfs           788M   28K  788M   1% /run/user/1000

```

To look through the file, use [cat command](https://www.tecmint.com/13-basic-cat-command-examples-in-linux/).
```
$ cat df_debug.txt

```

### 10. Show Some Debugging Output of Strace
To show debugging information for strace tool, use the `-d` flag.
```
**$ strace -d df -h**

```

For additional information, see the strace man page.
```
$ man strace

```

Also read these useful related articles:
  1. [20 Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)
  2. [Sysdig – A Powerful System Monitoring and Troubleshooting Tool for Linux](https://www.tecmint.com/sysdig-system-monitoring-and-troubleshooting-tool-for-linux/)
  3. [How to Trace Execution of Commands in Shell Script with Shell Tracing](https://www.tecmint.com/trace-shell-script-execution-in-linux/)
  4. [BCC – Dynamic Tracing Tools for Linux Performance Monitoring, Networking and More](https://www.tecmint.com/bcc-best-linux-performance-monitoring-tools/)


In conclusion, **strace** is a remarkable tool for diagnosing cause(s) of program failure: it is a powerful debugging and trouble shooting. It is practically useful to experienced system administrators, programmers and hackers. To share any thoughts concerning this article, use the feedback form below.
Tags [linux monitoring](https://www.tecmint.com/tag/linux-monitoring/)
💡 **Want to Level Up Your Linux Skills?**
Check out [**Pro.Tecmint.com**](https://pro.tecmint.com) for **ad-free reading** , **exclusive guides** , **downloadable resources** , and **certification prep** (RHCSA, RHCE, LFCS) - all with lifetime access.
[🔐 Get Lifetime Access ](https://pro.tecmint.com)
Previous article:
[How to Create Hard and Symbolic Links in Linux](https://www.tecmint.com/create-hard-and-symbolic-links-in-linux/)
Next article:
[How To Protect Hard and Symbolic Links in CentOS/RHEL 7](https://www.tecmint.com/protect-hard-and-symbolic-links-in-centos-rhel/)
![Photo of author](https://secure.gravatar.com/avatar/87e5179d8a999bace5a9739e27a309e1dfaea9ef2c54c7310fe6235531340eb4?s=100&d=blank&r=g)
Aaron Kili
Aaron Kili is a Linux and F.O.S.S enthusiast, an upcoming Linux SysAdmin, web developer, and currently a content creator for TecMint who loves working with computers and strongly believes in sharing knowledge.
* * *
_Each tutorial at**TecMint** is created by a team of experienced Linux system administrators_ so that it meets our high-quality _standards._
Join the **[TecMint Weekly Newsletter](https://newsletter.tecmint.com/subscription?f=hj6Ohm9gck3Z0PQ2BBBTh892iaCbDV3jJJa3hD8ULUlubOgnbo8aF44vt2HZfdc36g)** (More Than **156,129** Linux Enthusiasts Have Subscribed)
**Was this article helpful?** Please **[add a comment](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#respond)** or
## Related Posts
[![Linux Disk I/O Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2015/04/Linux-Disk-IO-Monitoring-Tools.png)](https://www.tecmint.com/monitor-linux-disk-io-performance/ "7 Best Tools to Monitor and Debug Disk I/O Performance in Linux")
[7 Best Tools to Monitor and Debug Disk I/O Performance in Linux](https://www.tecmint.com/monitor-linux-disk-io-performance/)
[![Disk Usage Monitoring Script in Linux](https://www.tecmint.com/wp-content/uploads/2014/01/linux-disk-usage-monitoring-shell-script.webp)](https://www.tecmint.com/monitor-disk-usage-bash-script/ "A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%")
[A Shell Script to Monitor Disk Usage and Send an Alert if it Exceeds 80%](https://www.tecmint.com/monitor-disk-usage-bash-script/)
[![Linux Performance Monitoring with Command-Line Tools](https://www.tecmint.com/wp-content/uploads/2023/08/command-line-monitoring-tools-linux.webp)](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/ "24 Best Command Line Tools to Monitor Linux Performance")
[24 Best Command Line Tools to Monitor Linux Performance](https://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)
[![atop: System and process monitor for Linux](https://www.tecmint.com/wp-content/uploads/2025/06/atop-System-and-process-monitor-for-Linux.webp)](https://www.tecmint.com/atop-linux-performance-monitoring/ "How to Install ‘atop’ to Monitor Real-Time System Performance")
[How to Install ‘atop’ to Monitor Real-Time System Performance](https://www.tecmint.com/atop-linux-performance-monitoring/)
[![Bash Script to Monitor Linux Health Daily](https://www.tecmint.com/wp-content/uploads/2025/06/bash-script-automate-system-health-checks.webp)](https://www.tecmint.com/bash-script-automate-system-health-checks/ "How to Automate Daily Linux Health Checks with a Bash Script + Cron")
[How to Automate Daily Linux Health Checks with a Bash Script + Cron](https://www.tecmint.com/bash-script-automate-system-health-checks/)
[![Network Bandwidth Monitoring Tools](https://www.tecmint.com/wp-content/uploads/2013/07/network-bandwidth-monitoring-tools.webp)](https://www.tecmint.com/network-bandwidth-monitoring-tools/ "5 Modern VnStat PHP Replacements for Bandwidth Monitoring")
[5 Modern VnStat PHP Replacements for Bandwidth Monitoring](https://www.tecmint.com/network-bandwidth-monitoring-tools/)
### 4 Comments
[Leave a Reply](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#reply-title)
  1. ![](https://secure.gravatar.com/avatar/c33513c848771ab69d52b63c429a7958e4b60df69f0e1c94a6b0135d3f131b8f?s=50&d=blank&r=g)
Trevor Chandler
[ October 11, 2024 at 9:56 pm  ](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#comment-2227204)
On your #9 command example, is there any diiference and/or benefit in using the output redirection character (>), instead of the `-o` switch in the stace command?
```
sudo strace -o df_debug.txt df -h
vs.
sudo strace df -h > df_debug.txt

```
[Reply](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#comment-2227204)
     * ![](https://secure.gravatar.com/avatar/111f6b53ad24719104c1cc55e9902f4ef840d8dd7af46c9481ea3d6e0b0040bd?s=50&d=blank&r=g)
Ravi Saive
[ October 14, 2024 at 12:17 pm  ](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#comment-2227995)
@Trevor,
Yes, there is a difference!
Using sudo `strace -o df_debug.txt df -h` directs strace to save all trace output (including errors) directly to **df_debug.txt**. In contrast, `sudo strace df -h > df_debug.txt` only redirects the standard output of the df command to the file, not the strace output.
For capturing detailed tracing information, the `-o` switch is more effective.
[Reply](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#comment-2227995)
  2. ![](https://secure.gravatar.com/avatar/7c3edd7f44d39321a291e6c4ea9b8ff18a85a34f78635c4bc339802d2a638725?s=50&d=blank&r=g)
Ano Nymos
[ December 17, 2023 at 11:23 pm  ](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#comment-2116202)
There are many duplicates of the output to each of your command examples.
[Reply](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#comment-2116202)
  3. ![](https://secure.gravatar.com/avatar/89ed6c8946120f5fd839a8492997096638feb9f6cb8a9a209abab4dee1d7019e?s=50&d=blank&r=g)
Robin Smith
[ October 14, 2020 at 2:28 pm  ](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#comment-1374379)
Excellent hints thanks
[Reply](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#comment-1374379)


### Got Something to Say? Join the Discussion... [Cancel reply](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/#respond)
Thank you for taking the time to share your thoughts with us. We appreciate your decision to leave a comment and value your contribution to the discussion. It's important to note that we moderate all comments in accordance with our [comment policy](https://www.tecmint.com/comment-policy/) to ensure a respectful and constructive conversation.
Rest assured that your email address will remain private and will not be published or shared with anyone. We prioritize the privacy and security of our users.
Comment
Name Email
Save my name, email, and website in this browser for the next time I comment.
Δ
## Upgrade Your Linux Learning with Pro.Tecmint
**If you find TecMint helpful** , consider supporting us by subscribing to [**Pro.Tecmint.com**](https://pro.tecmint.com) – our premium platform with exclusive guides, ad-free experience, early access to tutorials, and much more.

Your support helps us keep creating quality Linux content for everyone.
[ Get Lifetime Access ](https://pro.tecmint.com)
## Linux Commands and Tools
[5 Command Line Ways to Find Out Linux System is 32-bit or 64-bit](https://www.tecmint.com/find-out-linux-system-is-32-bit-or-64-bit/)
[How to Delete Root Mails (Mailbox) File in Linux](https://www.tecmint.com/delete-root-mails-mailbox-file-in-linux/)
[What’s Difference Between Grep, Egrep and Fgrep in Linux?](https://www.tecmint.com/difference-between-grep-egrep-and-fgrep-in-linux/)
[How to Show Asterisks While Typing Sudo Password in Linux](https://www.tecmint.com/show-asterisks-sudo-password-in-linux/)
[How to Create and Extract Zip Files to Specific Directory in Linux](https://www.tecmint.com/unzip-extract-zip-files-to-specific-directory-in-linux/)
[How to Monitor Progress of (Copy/Backup/Compress) Data using ‘pv’ Command](https://www.tecmint.com/monitor-copy-backup-tar-progress-in-linux-using-pv-command/)
## Linux Server Monitoring Tools
[Trickle – Control Network Traffic Bandwidth Of Applications in a Linux](https://www.tecmint.com/limit-linux-network-bandwidth-usage-with-trickle/)
[How to Install and Configure Zabbix Agents on Remote Linux – Part 3](https://www.tecmint.com/install-and-configure-zabbix-agents-on-centos-redhat-and-debian/)
[btop: A Modern and Resourceful System Monitor](https://www.tecmint.com/btop-system-monitoring-tool-for-linux/)
[10 Tips On How to Use Wireshark to Analyze Packets in Your Network](https://www.tecmint.com/wireshark-network-traffic-analyzer-for-linux/)
[4 Tools to Manage EXT2, EXT3 and EXT4 Health in Linux](https://www.tecmint.com/manage-ext2-ext3-and-ext4-health-in-linux/)
[Swatchdog – Simple Log File Watcher in Real-Time in Linux](https://www.tecmint.com/swatch-linux-log-file-watcher/)
## Learn Linux Tricks & Tips
[How to Change Linux Partition Label Names on EXT4 / EXT3 / EXT2 and Swap](https://www.tecmint.com/change-modify-linux-disk-partition-label-names/)
[4 Ways to Disable Root Account in Linux](https://www.tecmint.com/disable-root-login-in-linux/)
[How to Count Word Occurrences in a Text File](https://www.tecmint.com/count-word-occurrences-in-linux-text-file/)
[How to Auto Execute Commands/Scripts During Reboot or Startup](https://www.tecmint.com/auto-execute-linux-scripts-during-reboot-or-startup/)
[Fd – The Best Alternative to ‘Find’ Command for Quick File Searching](https://www.tecmint.com/fd-alternative-to-find-command/)
[4 Ways to Generate a Strong Pre-Shared Key (PSK) in Linux](https://www.tecmint.com/generate-pre-shared-key-in-linux/)
## Best Linux Tools
[3 Best Cloud-Based Music Apps for Linux](https://www.tecmint.com/cloud-music-player/)
[Top 6 Linux Apps You Should Install This Week (Sept 15-21)](https://www.tecmint.com/linux-apps-to-try-this-week-september-15-21/)
[8 Best HTML & CSS Code Editors for Linux](https://www.tecmint.com/html-css-editors-linux/)
[4 Best Tools for Creating Fillable PDF Forms on Linux](https://www.tecmint.com/create-pdf-forms-linux/)
[How to Install Microsoft Teams, Slack, and Discord on Linux Desktop](https://www.tecmint.com/install-microsoft-teams-slack-discord-linux/)
[11 Best PDF Editors to Edit PDF Documents in Linux](https://www.tecmint.com/pdf-editors-linux/)
Privacy Manager
Tecmint: Linux Howtos, Tutorials & Guides © 2026. All Rights Reserved.
The material in this site cannot be republished either online or offline, without our permission.
Hosting Sponsored by : [Linode Cloud Hosting](https://www.tecmint.com/go/linode)
[ ](https://www.tecmint.com/strace-commands-for-troubleshooting-and-debugging-linux/ "Scroll back to top")
Search for:
