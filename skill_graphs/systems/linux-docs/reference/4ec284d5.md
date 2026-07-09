_`--enable-zlib`_

This allows the Module-Init-Tools package to handle compressed kernel modules.
Compile the package:
```
`make`
```

Install the package:
```
`make install`
```

###  6.50.2. Contents of Module-Init-Tools
**Installed programs:** depmod, insmod, insmod.static, lsmod (link to insmod), modinfo, modprobe (link to insmod), and rmmod (link to insmod)
###  Short Descriptions
**depmod** |  Creates a dependency file based on the symbols it finds in the existing set of modules; this dependency file is used by **modprobe** to automatically load the required modules
---|---
**insmod** |  Installs a loadable module in the running kernel
**insmod.static** |  A statically compiled version of **insmod**
**lsmod** |  Lists currently loaded modules
**modinfo** |  Examines an object file associated with a kernel module and displays any information that it can glean
**modprobe** |  Uses a dependency file, created by **depmod** , to automatically load relevant modules
**rmmod** |  Unloads modules from the running kernel
##  6.51. Patch-2.5.4
The Patch package contains a program for modifying or creating files by applying a “patch” file typically created by the **diff** program.
**Approximate build time:** 0.1 SBU
**Required disk space:** 1.5 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Glibc, Grep, Make, and Sed
###  6.51.1. Installation of Patch
Prepare Patch for compilation. The preprocessor flag _`-D_GNU_SOURCE`_ is only needed on the PowerPC platform. It can be left it out on other architectures:
```
`CPPFLAGS=-D_GNU_SOURCE ./configure --prefix=/usr`
```

Compile the package:
```
`make`
```

This package does not come with a test suite.
Install the package:
```
`make install`
```

###  6.51.2. Contents of Patch
**Installed program:** patch
###  Short Descriptions
**patch** |  Modifies files according to a patch file. A patch file is normally a difference listing created with the **diff** program. By applying these differences to the original files, **patch** creates the patched versions.
---|---
##  6.52. Procps-3.2.5
The Procps package contains programs for monitoring processes.
**Approximate build time:** 0.1 SBU
**Required disk space:** 2.3 MB
**Installation depends on:** Bash, Binutils, Coreutils, GCC, Glibc, Make, and Ncurses
###  6.52.1. Installation of Procps
Compile the package:
```
`make`
```

Install the package:
```
`make install`
```

###  6.52.2. Contents of Procps
**Installed programs:** free, kill, pgrep, pkill, pmap, ps, skill, snice, sysctl, tload, top, uptime, vmstat, w, and watch
**Installed library:** libproc.so
###  Short Descriptions
**free** |  Reports the amount of free and used memory (both physical and swap memory) in the system
---|---
**kill** |  Sends signals to processes
**pgrep** |  Looks up processes based on their name and other attributes
**pkill** |  Signals processes based on their name and other attributes
**pmap** |  Reports the memory map of the given process
**ps** |  Lists the current running processes
**skill** |  Sends signals to processes matching the given criteria
**snice** |  Changes the scheduling priority of processes matching the given criteria
**sysctl** |  Modifies kernel parameters at run time
**tload** |  Prints a graph of the current system load average
**top** |  Displays a list of the most CPU intensive processes; it provides an ongoing look at processor activity in real time
**uptime** |  Reports how long the system has been running, how many users are logged on, and the system load averages
**vmstat** |  Reports virtual memory statistics, giving information about processes, memory, paging, block Input/Output (IO), traps, and CPU activity
**w** |  Shows which users are currently logged on, where, and since when
**watch** |  Runs a given command repeatedly, displaying the first screen-full of its output; this allows a user to watch the output change over time
`libproc` |  Contains the functions used by most programs in this package
##  6.53. Psmisc-21.6
The Psmisc package contains programs for displaying information about running processes.
**Approximate build time:** 0.1 SBU
**Required disk space:** 1.7 MB
**Installation depends on:** Bash, Binutils, Coreutils, Diffutils, GCC, Gettext, Glibc, Grep, Make, Ncurses, and Sed
###  6.53.1. Installation of Psmisc
Prepare Psmisc for compilation:
```
`./configure --prefix=/usr --exec-prefix=""`
```

The meaning of the configure options:

_`--exec-prefix=""`_

This ensures that the Psmisc binaries will install into `/bin` instead of `/usr/bin`. This is the correct location according to the FHS, because some of the Psmisc binaries are used by the LFS-Bootscripts package.
Compile the package:
```
`make`
```

Install the package:
```
`make install`
```

There is no reason for the **pstree** and **pstree.x11** programs to reside in `/bin`. Therefore, move them to `/usr/bin`:
```
`mv -v /bin/pstree* /usr/bin`
```

By default, Psmisc's **pidof** program is not installed. This usually is not a problem because it is installed later in the Sysvinit package, which provides a better **pidof** program. If Sysvinit will not be used for a particular system, complete the installation of Psmisc by creating the following symlink:
```
`ln -sv killall /bin/pidof`
```

###  6.53.2. Contents of Psmisc
**Installed programs:** fuser, killall, pstree, and pstree.x11 (link to pstree)
###  Short Descriptions
**fuser** |  Reports the Process IDs (PIDs) of processes that use the given files or file systems
---|---
**killall** |  Kills processes by name; it sends a signal to all processes running any of the given commands
**pstree** |  Displays running processes as a tree
**pstree.x11** |  Same as **pstree** , except that it waits for confirmation before exiting
##  6.54. Shadow-4.0.9
The Shadow package contains programs for handling passwords in a secure way.
**Approximate build time:** 0.4 SBU
**Required disk space:** 13.7 MB
**Installation depends on:** Bash, Binutils, Bison, Coreutils, Diffutils, GCC, Gettext, Glibc, Grep, Make, and Sed
###  6.54.1. Installation of Shadow
###  Note
If you would like to enforce the use of strong passwords, refer to _`--with-libcrack`_ to the **configure** command below.
Prepare Shadow for compilation:
```
`./configure --libdir=/lib --enable-shared`
```

Disable the installation of the **groups** program and its man page, as Coreutils provides a better version:
```
`sed -i 's/groups$(EXEEXT) //' src/Makefile
sed -i '/groups/d' man/Makefile`
```

Compile the package:
```
`make`
```

Install the package:
```
`make install`
```

Shadow uses two files to configure authentication settings for the system. Install these two configuration files:
```
`cp -v etc/{limits,login.access} /etc`
```

Instead of using the default _crypt_ method, use the more secure _MD5_ method of password encryption, which also allows passwords longer than 8 characters. It is also necessary to change the obsolete `/var/spool/mail` location for user mailboxes that Shadow uses by default to the `/var/mail` location used currently. Both of these can be accomplished by changing the relevant configuration file while copying it to its destination:
###  Note
If you built Shadow with Cracklib support, insert the following into the **sed** given below:
```
`-e 's@DICTPATH.*@DICTPATH\t/lib/cracklib/pw_dict@'`
```

```
`sed -e's@#MD5_CRYPT_ENAB.no@MD5_CRYPT_ENAB yes@' \
    -e 's@/var/spool/mail@/var/mail@' \
    etc/login.defs.linux > /etc/login.defs`
```

Move a misplaced program to its proper location:
```
`mv -v /usr/bin/passwd /bin`
```

Move Shadow's libraries to more appropriate locations:
```
`mv -v /lib/libshadow.*a /usr/lib
rm -v /lib/libshadow.so
ln -sfv ../../lib/libshadow.so.0 /usr/lib/libshadow.so`
```

The _`-D`_ option of the **useradd** program requires the `/etc/default` directory for it to work properly:
```
`mkdir -v /etc/default`
```

###  6.54.2. Configuring Shadow
This package contains utilities to add, modify, and delete users and groups; set and change their passwords; and perform other administrative tasks. For a full explanation of what _password shadowing_ means, see the `doc/HOWTO` file within the unpacked source tree. If using Shadow support, keep in mind that programs which need to verify passwords (display managers, FTP programs, pop3 daemons, etc.) must be Shadow-compliant. That is, they need to be able to work with shadowed passwords.
To enable shadowed passwords, run the following command:
```
`pwconv`
```

To enable shadowed group passwords, run:
```
`grpconv`
```

Under normal circumstances, passwords will not have been created yet. However, if returning to this section later to enable shadowing, reset any current user passwords with the **passwd** command or any group passwords with the **gpasswd** command.
###  6.54.3. Setting the root password
Choose a password for user _root_ and set it by running:
```
`passwd root`
```

###  6.54.4. Contents of Shadow
**Installed programs:** chage, chfn, chpasswd, chsh, expiry, faillog, gpasswd, groupadd, groupdel, groupmod, grpck, grpconv, grpunconv, lastlog, login, logoutd, mkpasswd, newgrp, newusers, passwd, pwck, pwconv, pwunconv, sg (link to newgrp), useradd, userdel, usermod, vigr (link to vipw), and vipw
**Installed libraries:** libshadow.[a,so]
###  Short Descriptions
**chage** |  Used to change the maximum number of days between obligatory password changes
---|---
**chfn** |  Used to change a user's full name and other information
**chpasswd** |  Used to update the passwords of an entire series of user accounts
**chsh** |  Used to change a user's default login shell
**expiry** |  Checks and enforces the current password expiration policy
**faillog** |  Is used to examine the log of login failures, to set a maximum number of failures before an account is blocked, or to reset the failure count
**gpasswd** |  Is used to add and delete members and administrators to groups
**groupadd** |  Creates a group with the given name
**groupdel** |  Deletes the group with the given name
**groupmod** |  Is used to modify the given group's name or GID
**grpck** |  Verifies the integrity of the group files `/etc/group` and `/etc/gshadow`
**grpconv** |  Creates or updates the shadow group file from the normal group file
**grpunconv** |  Updates `/etc/group` from `/etc/gshadow` and then deletes the latter
**lastlog** |  Reports the most recent login of all users or of a given user
**login** |  Is used by the system to let users sign on
**logoutd** |  Is a daemon used to enforce restrictions on log-on time and ports
**mkpasswd** |  Generates random passwords
**newgrp** |  Is used to change the current GID during a login session
**newusers** |  Is used to create or update an entire series of user accounts
**passwd** |  Is used to change the password for a user or group account
**pwck** |  Verifies the integrity of the password files `/etc/passwd` and `/etc/shadow`
**pwconv** |  Creates or updates the shadow password file from the normal password file
**pwunconv** |  Updates `/etc/passwd` from `/etc/shadow` and then deletes the latter
**sg** |  Executes a given command while the user's GID is set to that of the given group
**su** |  Runs a shell with substitute user and group IDs
**useradd** |  Creates a new user with the given name, or updates the default new-user information
**userdel** |  Deletes the given user account
**usermod** |  Is used to modify the given user's login name, User Identification (UID), shell, initial group, home directory, etc.
**vigr** |  Edits the `/etc/group` or `/etc/gshadow` files
**vipw** |  Edits the `/etc/passwd` or `/etc/shadow` files
`libshadow` |  Contains functions used by most programs in this package
##  6.55. Sysklogd-1.4.1
The Sysklogd package contains programs for logging system messages, such as those given by the kernel when unusual things happen.
**Approximate build time:** 0.1 SBU
**Required disk space:** 704 KB
**Installation depends on:** Binutils, Coreutils, GCC, Glibc, Make
###  6.55.1. Installation of Sysklogd
The following patch fixes various issues, including a problem building Sysklogd with Linux 2.6 series kernels
```
`patch -Np1 -i ../sysklogd-1.4.1-fixes-1.patch`
```

Compile the package:
```
`make`
```

Install the package:
```
`make install`
```

###  6.55.2. Configuring Sysklogd
Create a new `/etc/syslog.conf` file by running the following:
```
`cat > /etc/syslog.conf << "EOF"
`# Begin /etc/syslog.conf

auth,authpriv.* -/var/log/auth.log
*.*;auth,authpriv.none -/var/log/sys.log
daemon.* -/var/log/daemon.log
kern.* -/var/log/kern.log
mail.* -/var/log/mail.log
user.* -/var/log/user.log
*.emerg *
