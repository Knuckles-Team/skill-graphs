#  Chapter 13. Network Commands
The network commands chapter explains various tools which can be useful when networking with other computers both within the network and across the internet, obtaining more information about other computers. This chapter also includes information on tools for network configuration, file transfer and working with remote machines.

netstat

Displays contents of /proc/net files. It works with the Linux Network Subsystem, it will tell you what the status of ports are ie. open, closed, waiting, masquerade connections. It will also display various other things. It has many different options.

tcpdump

This is a sniffer, a program that captures packets off a network interface and interprets them for you. It understands all basic internet protocols, and can be used to save entire packets for later inspection.

ping

The ping command (named after the sound of an active sonar system) sends echo requests to the host you specify on the command line, and lists the responses received their round trip time.
You simply use ping as:
```
ping ip_or_host_name
```

---
Note to stop ping (otherwise it goes forever) use **CTRL** -**C** (break).
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Please note**
---|---
|  Using ping/smbmount/ssh or other UNIX system programs with a computer name rather than IP address will only work if you have the computer listed in your /etc/hosts file. Here is an example: | ```
192.168.1.100 new
```

---
This line says that their is a computer called “new” with IP address 192.168.1.100. Now that it exists in the /etc/hosts file I don't have to type the IP address anymore, just the name “new”.

hostname

Tells the user the host name of the computer they are logged into. Note: may be called _host._

traceroute

_traceroute_ will show the route of a packet. It attempts to list the series of hosts through which your packets travel on their way to a given destination. Also have a look at _xtraceroute_ (one of several graphical equivalents of this program).
Command syntax:
```
traceroute machine_name_or_ip
```

---

tracepath

_tracepath_ performs a very similar function to _traceroute_ the main difference is that _tracepath_ doesn't take complicated options.
Command syntax:
```
tracepath machine_name_or_ip
```

---

findsmb

_findsmb_ is used to list info about machines that respond to SMB name queries (for example windows based machines sharing their hard disk's).
Command syntax:
```
findsmb
```

---
This would find all machines possible, you may need to specify a particular subnet to query those machines only...

nmap

“ network exploration tool and security scanner”. _nmap_ is a very advanced network tool used to query machines (local or remote) as to whether they are up and what ports are open on these machines.
A simple usage example:
```
nmap machine_name
```

---
This would query your own machine as to what ports it keeps open. _nmap_ is a very powerful tool, documentation is available on the
* * *
#  13.1. Network Configuration

ifconfig

This command is used to configure network interfaces, or to display their current configuration. In addition to activating and deactivating interfaces with the “up” and “down” settings, this command is necessary for setting an interface's address information if you don't have the _ifcfg_ script.
Use _ifconfig_ as either:
```
ifconfig
```

---
This will simply list all information on all network devices currently up.
```
ifconfig eth0 down
```

---
This will take eth0 (assuming the device exists) down, it won't be able to receive or send anything until you put the device back “up” again.
Clearly there are a lot more options for this tool, you will need to read the manual/info page to learn more about them.

ifup

Use _ifup device-name_ to bring an interface up by following a script (which will contain your default networking settings). Simply type _ifup_ and you will get help on using the script.
For example typing:
```
ifup eth0
```

---
Will bring eth0 up if it is currently down.

ifdown

Use _ifdown device-name_ to bring an interface down using a script (which will contain your default network settings). Simply type _ifdown_ and you will get help on using the script.
For example typing:
```
ifdown eth0
```

---
Will bring eth0 down if it is currently up.

ifcfg

Use _ifcfg_ to configure a particular interface. Simply type ifcfg to get help on using this script.
For example, to change eth0 from 192.168.0.1 to 192.168.0.2 you could do:
```
ifcfg eth0 del 192.168.0.1
ifcfg eth0 add 192.168.0.2
```

---
The first command takes eth0 down and removes that stored IP address and the second one brings it back up with the new address.

route

The _route_ command is the tool used to display or modify the routing table. To add a gateway as the default you would type:
```
route add default gw some_computer
```

---
* * *
#  13.2. Internet Specific Commands
Note that should DNS not be configured correctly on your machine, you need to edit “/etc/resolv.conf” to make things work...

host

Performs a simple lookup of an internet address (using the Domain Name System, DNS). Simply type:
```
host ip_address
```

---
or
```
host domain_name
```

---

dig

The "domain information groper" tool. More advanced then _host_... If you give a hostname as an argument to output information about that host, including it's IP address, hostname and various other information.
For example, to look up information about “www.amazon.com” type:
```
dig www.amazon.com
```

---
To find the host name for a given IP address (ie a reverse lookup), use _dig_ with the _`-x'_ option.
```
dig -x 100.42.30.95
```

---
This will look up the address (which may or may not exist) and returns the address of the host, for example if that was the address of “http://slashdot.org” then it would return “http://slashdot.org”.
_dig_ takes a huge number of options (at the point of being too many), refer to the manual page for more information.

whois

(now BW whois) is used to look up the contact information from the “whois” databases, the servers are only likely to hold major sites. Note that contact information is likely to be hidden or restricted as it is often abused by crackers and others looking for a way to cause malicious damage to organisation's.

wget

(GNU Web get) used to download files from the World Wide Web.
To archive a single web-site, use the _-m_ or _--mirror_ (mirror) option.
Use _-nc_(no clobber) option to stop _wget_ from overwriting a file if you already have it.
Use the _-c_ or _--continue_ option to continue a file that was unfinished by wget or another program.
Simple usage example:
```
wget url_for_file
```

---
This would simply get a file from a site.
_wget_ can also retrieve multiple files using standard wildcards, the same as the type used in bash, like *, [ ], ?. Simply use _wget_ as per normal but use single quotation marks (' ') on the URL to prevent bash from expanding the wildcards. There are complications if you are retrieving from a http site (see below...).
Advanced usage example, (used from _wget_ manual page):
```
wget --spider --force-html -i bookmarks.html
```

---
This will parse the file bookmarks.html and check that all the links exist.
Advanced usage: this is how you can download multiple files using http (using a wildcard...).
Notes: http doesn't support downloading using standard wildcards, ftp does so you may use wildcards with ftp and it will work fine. A work-around for this http limitation is shown below:
```
wget -r -l1 --no-parent -A.gif http://www.website.com[[6]](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FTN.AEN8967)
```

---
This will download (recursively), to a depth of one, in other words in the current directory and not below that. This command will ignore references to the parent directory, and downloads anything that ends in “.gif”. If you wanted to download say, anything that ends with “.pdf” as well than add a _-A.pdf_ before the website address. Simply change the website address and the type of file being downloaded to download something else. Note that doing _-A.gif_ is the same as doing _-A “*.gif_ ” (double quotes only, single quotes will not work).
_wget_ has many more options refer to the examples section of the manual page, this tool is very well documented.
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Alternative website downloaders**
---|---
| You may like to try alternatives like httrack. A full GUI website downloader written in python and available for GNU/Linux

curl

_curl_ is another remote downloader. This remote downloader is designed to work without user interaction and supports a variety of protocols, can upload/download and has a large number of tricks/work-arounds for various things. It can access dictionary servers (dict), ldap servers, ftp, http, gopher, see the manual page for full details.
To access the full manual (which is huge) for this command type:
```
curl -M
```

---
For general usage you can use it like _wget_. You can also login using a user name by using the _-u_ option and typing your username and password like this:
```
curl -u username:password http://www.placetodownload/file
```

---
To upload using ftp you the _-T_ option:
```
curl -T file_name ftp://ftp.uploadsite.com
```

---
To continue a file use the _-C_ option:
```
curl -C - -o file http://www.site.com
```

---
* * *
#  13.3. Remote Administration Related

ssh

Secure shell, remotely login on a machine running the _sshd_ daemon. Once you are logged in you have a secure shell and are able to execute various commands on that computer such as copy files, reboot the computer, just like it was your own GNU/Linux PC.
Or you can use _ssh_ with a full hostname to connect to a remote machine (as in across the internet).
Examples:
```
ssh hostname
```

---
Connect to a remote system with your current username, you will obviously need the password of the user on the other machine.
```
ssh username@hostname
```

---
Connect to a remote system with your a different username, you will obviously need the password of the user on the other machine.

scp

Secure copy, part of the ssh package. Allows you to copy files from one computer to another computer, use _-r_ to copy recursively (copy entire directories and subdirectories).
_scp_ 's syntax is always
```
scp machineToBeCopiedFrom machineToBeCopiedTo
```

---
Where either machine can be a local directory (on the current filesystem /) or a remote machine. Remote machines are usually _machinesFullName:/directory_ (if you omit the directory part it will just assume the home directory of the username you are logging in with).
The example below copies all files from the current directory (not including any directories), the command will login to “new” using the username of the person currently logged in on the local computer, the files will be copied to the root directory of the remote computer called “new” (which is probably on the LAN):
```
scp * new:/
```

---
You could also copy files from another computer to another computer. Let's say you are on a computer called “p100”. And you want to copy files (and directories) from “hp166” (in the /tmp directory and anything below that) to “new” and put the files in new's temporary directory. You could do:
```
scp -r hp166:/tmp new:/tmp
```

---
Assuming you were logged in as “fred” you would need passwords for user “fred” on the computers hp166 and new. Add an _user_name@_ before the computer name to login under a different user name.
For example to perform the above command with user “root” on hp166 and “anon” on new you would type:
```
scp -r root@hp166:/tmp anon@new:/tmp
```

---
To copy from a remote machine to a local computer you simply do things in reverse:
```
scp remoteMachine:/mystuff/* .
```

---
This will copy files on the remote machine in the directory “mystuff” to your local computer.
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Remote Machines**
---|---
| Please note that when working with a remote machine you need to have a : (colon) after the machine name even if you want the files in their home directory. Otherwise the command will fail.

sftp

Secure ftp, another part of the ssh package. This command is similar to ftp but uses an encrypted tunnel to connect to an ftp server and is therefore more secure than just plain _ftp_.
The command usage is very similar to _ftp_ (the command-line tool), _sftp_ (once running) uses commands such as _help_(for help), _put_ (send files to the server), _get_ (download files from the server) and various others, refer to the manual page and internal documentation for further details.
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Graphical programs**
---|---
| Sometimes its easier to manage files with a GUI, many of these programs do have good GUI equivalents, try searching the internet or sites like
* * *
#  Chapter 14. Security
The security chapter is designed to give the user a very basic level of understanding of security within the GNU/Linux operating system. This chapter also has information on the UNIX system style file permissions used on most GNU/Linux machines.
More comprehensive guides can be found at the [Linux Documentation Project](http://www.tldp.org), such as the [Linux Security howto](http://www.tldp.org/HOWTO/Security-HOWTO/) authored by Kevin Fenzi and Dave Wreski.
There are also sites such as RPM based distributions (Redhat/Mandriva/SuSE).

Changing�root's�password

This trick works well if you have forgotten your superuser password, type _linux single_ at a LILO/Grub prompt. Then _passwd_ once the system has started and you are at a console.

Grub:

If you are using grub go to the relevant line (the one with the kernel and various options) then press 'e' for edit and add “single” on to the end of the lines that boot the kernel. Then hit [Enter] and press 'b' (to boot).

Lilo:

If you are using lilo press escape and type “ linux single” and then hit [Enter] to boot.
![Caution](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/caution.gif) | **Security Warning**
---|---
|  This is also a basic security hazard if you have others using your computer and security is a concern, you may like to add a password to your LILO or Grub prompt to stop this from being done.

umask

The umask is a value set by the shell. It controls the default permissions of any file created during that shell session. This information is inherited from the shell's parent and is normally set in some configuration file by the root user (in my case /etc/profile).
umask has an unusual way of doing things ...to set the umask you must describe file permissions by saying what will be disabled.
You can do this by doing 777 minus the file permissions you want. Note that _umask_ works with numbers only, for an explanation please see, [Section 14.2](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FILE-PERMISSIONS)
For example:
You want the default during a particular shell session to be equivalent to _chmod 750_ (user has r/w/x, group has r/x and other has no permissions), then the command you would use would be:
```
umask 027
```

---
* * *
#  14.1. Some basic Security Tools

md5sum

Compute an md5 checksum (128-bit) for file “file_name” to verify it's integrity. You normally use the “ md5sum -c” option to check against a given file (often with a “.asc” extension) to check whether the various files are correct, this comes in handy when downloading isos as the checking is automated for you.
Command syntax:
```
md5sum file_name
```

---

mkpasswd�-l�10

This command will make a random password of length ten characters. This password generator creates passwords that are designed to be hard to guess. There are similar alternatives to this program scattered around the internet.
* * *
#  14.2. File Permissions
Use _ls -l_ to see the permissions of files (list-long). They will appear like this, note that I have added spaces between permissions to make it easier to read:
Where: r = read, w = write, x = execute
```
  -  rwx   rw-   r--  1 ![\(1\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/1.gif) newuser newuser
type![\(2\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/2.gif)owner![\(3\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/3.gif)group![\(4\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/4.gif)others![\(5\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/5.gif)
```

---

[![\(1\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/1.gif)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#LINKS)
     This number is the number of hard links (pointers) to this file. You can use _ln_ to create another hard-link to the file.

[![\(2\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/2.gif)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#TYPE)
     This is the type of file. '-' means a regular file, 'd' would mean a directory, 'l' would mean a link. There are also other types such as 'c' for character device and 'b' for block device (found in the /dev/ directory).

[![\(3\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/3.gif)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#OWNER)
     These are the permissions for the owner of the file (the user who created the file).

[![\(4\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/4.gif)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#GROUP)
     These are the permissions for the group, any users who belong is the same group as the user who created the file will have these permissions.

[![\(5\)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/callouts/5.gif)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#OTHERS)
     These are the permissions for everyone else. Any user who is outside the group will have these permissions to the file.
The two names at the end are the username and group respectively.

chmod

Change file access permissions for a file(s).
There are two methods to change permissions using _chmod_ ; letters or numbers.

Letters�Method:

use a + or - (plus or minus sign) to add or remove permissions for a file respectively. Use an equals sign =, to specify new permissions and remove the old ones for the particular type of user(s).
You can use _chmod letter_ where the letters are:
_a_ (all (everyone))_, u_ (user)_,_ _g_ (group) and _o_ (other).
Examples:
```
chmod u+rw somefile
```

---
This would give the user read and write permission.
```
chmod o-rwx somefile
```

---
This will remove read/write/execute permissions from other users (doesn't include users within your group).
```
chmod a+r_ _somefile
```

---
This will give everyone read permission for the file.
```
chmod a=rx somefile
```

---
This would give everyone execute and read permission to the file, if anyone had write permission it would be removed.

Numbers�Method:

you can also use numbers (instead of letters) to change file permissions. Where:
r (read) = 4 w (write) = 2 x (execute) = 1
Numbers can be added together so you can specify read/write/execute permissions; read+write = 6, read+execute = 5, read+write+execute = 7
Examples:
```
chmod 777 somefile
```

---
This would give everyone read/write/execute permission on “this_file”. The first number is user, second is group and third is everyone else (other).
```
chmod 521 somefile
```

---
This would give the user read and execute permission, and the group write permission (but not read permission!) and everyone else execute permission. (Note that it's just an example, settings like that don't really make sense...).

chown

Changes the ownership rights of a file (hence the name 'chown' - change owner). This program can only be used by root.
Use the _-R_ option to change things recursively, in other words, all matching files including those in subdirectories.
Command syntax:
```
chown owner:group the_file_name
```

---

sticky�bit

Only the person who created the file within a directory may delete it, even if other people have write permission. You can turn it on by typing:
```
chmod 1700_ _somedirectory (where 1 = sticky bit)
```

---
or (where _t_ represents the sticky bit)
```
chmod +t somedirectory
```

---
To turn it off you would need to type:
```
chmod 0700 somefile (where the zero would mean no sticky bit)
```

---
or (where _t_ represents the sticky bit)
```
chmod -t somefile
```

---
Note that the permissions aren't relevant in the numbers example, only the first number (1 = on, 0 = off).
An example of a sticky directory is usually /tmp

suid

Allow SUID/SGID (switch user ID/switch group ID) access. You would normally use _chmod_ to turn this on or off for a particular file, suid is generally considered a security hazard so be careful when using this.
Example:
```
chmod u+s file_name
```

---
This will give everyone permission to execute the file with the permissions of the user who set the +s switch.
![Caution](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/caution.gif) | **Security Hazard**
---|---
| This is obviously a security hazard. You should avoid using the suid flag unless necessary.

chattr

_-R_ option to change files recursively,_chattr_ has a large number of attributes which can be set on a file, read the manual page for further information.
Example:
```
chattr +i /sbin/lilo.conf[[7]](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FTN.AEN9835)
```

---
This sets the 'immutable' flag on a file. Use a '+' to add attributes and a '-' to take them away. The +i will prevent any changes (accidental or otherwise) to the “lilo.conf” file. If you wish to modify the lilo.conf file you will need to unset the immutable flag:_chattr -i_. Note some flags can only be used by root; _-i_ , _-a_ and probably many others.
Note there are many different attributes that chattr can change, here are a few more which may be useful:
  * A (no Access time) --- if a file or directory has this attribute set, whenever it is accessed, either for reading of for writing, it's last access time will not be updated. This can be useful, for example, on files or directories which are very often accessed for reading, especially since this parameter is the only one which changes on an inode when it's opened.
  * a (append only) --- if a file has this attribute set and is open for writing, the only operation possible will be to append data to it's previous contents. For a directory, this means that you can only add files to it, but not rename or delete any existing file. Only root can set or clear this attribute.
  * s (secure deletion) --- when such a file or directory with this attribute set is deleted, the blocks it was occupying on disk are written back with zeroes (similar to using _shred_). Note that this does work on the ext2, and ext3 filesystems but is unlikely to work on others (please see the documentation for the filesystem you are using). You may also like to see _shred_ , please see [Chapter 7](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#WORKING-WITH-THE-FILE-SYSTEM)



lsattr

(list attributes). This will list if whether a file has any special attributes (as set by chattr). Use the _-R_ option to list recursively and try using the _-d_ option to list directories like other files rather than listing their contents.
Command syntax:
```
lsattr
```

---
This will list files in the current directory, you may also like to specify a directory or a file:
```
lsattr /directory/or/file
```

---
* * *
#  Chapter 15. Archiving Files
The archiving files chapter provides some basic information on the simple programs that you can use to archive files. You will often see these programs used when you try to install programs without using a package management tool.
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **This is not a backup guide**
---|---
|  Please note that while _tar_ is useful for regular purposes, and possibly combined with bash scripting or similar it can become useful, it is not a great program for performing real backups of data. You should try searching the internet if you are looking for backup programs on GNU/Linux or try [Section 15.2](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#RSYNC).
* * *
#  15.1. tar (tape archiver)
Type _tar_ then _-option(s)_
Options list:
  * -c --- create.
  * -v --- verbose, give more output, show what files are being worked with (extracted or added).
  * -f --- file (create or extract from file) - should always be the last option otherwise the command will not work.
  * -z --- put the file though gzip or use gunzip on the file first.
  * -x --- extract the files from the tarball.
  * -p --- preserves dates, permissions of the original files.
  * -j --- send archive through bzip2.
  * --exclude=pattern --- this will stop certain files from being archived (using a standard wild-card pattern) or a single file name.



tar�examples

�
```
tar -cvpf name_of_file.tar files_to_be_backed_up
```

---
This would create a tape archive (no compressing).
```
tar -zxvpf my_tar_file.tar.gz
```

---
This would extract files (verbosely) from a gzipped tape archive.
* * *
#  15.2. rsync

rsync

_rsync_ is a replacement for the old _rcp_ (remote-copy) command. It can use _ssh_ for encryption and is a very flexible tool, it can copy from local machine to local machine, from local to remote (and vice-versa), and to and from rsync servers.
_rsync_ uses an advanced differencing algorithm, so when to copies or syncs something it will (a) only copy new/changed files and (b) if the files have being changed it will copy the differences between the files (not the entire file). Using this method _rsync_ saves time and bandwidth.
_rsync_ also has advanced exclusion options similar to GNU tar. _rsync_ has a well written manual page, for further information read the _rsync_ documentation online or type:
```
man rsync
```

---
If you wish to visit the rsync site you will find it over
* * *
#  15.3. Compression
There are two main compression utilities used in GNU/Linux. It's normal to first “tar” a bunch of files (using the _tar_ program of course) and then compress them with either _bzip2_ or _gzip_. Of course either of these tools could be used without tar, although they are not designed to work on more than one file (they use the UNIX tools philosophy, let _tar_ group the files, they will do the compression...this simplifies their program). It's normal to use _tar_ and then use these tools on them, or use _tar_ with the correct options to use these compression programs.

GNU�zip�(gzip)

gzip is the GNU zip compression program and probably the most common compression format on UNIX-like operating systems.
```
gzip your_tar_file.tar
```

---
This will compress a tar archive with GNU zip, usually with a .gz extension. Gzip can compress any type of file, it doesn't have to be a tar archive.
```
gunzip your_file.gz
```

---
This will decompress a gzipped file, and leave the contents in the current directory.

bzip2

bzip2 is a newer compression program that offers superior compression to gzip at the cost of more processor time.
```
bzip2 your_tar_file.tar
```

---
This will compress a tar archive with the bzip2 compression program, usually with a .bz extension. bzip2 can compress any type of file, it doesn't have to be a tar archive.
```
bunzip2 your_file.tar.bz2
```

---
This will decompress a file compressed by bzip2, and leave the contents in the current directory.

zipinfo

Use _zipinfo_ to find detailed information about a zip archive (the ones usually generally used by ms-dos and windows, for example winzip).
Command syntax:
```
zipinfo zip_file.zip
```

---

zipgrep

Will run _grep_ to look for files within a zip file (ms-dos style, for example winzip) without manually decompressing the file first.
Command syntax:
```
zipgrep pattern zip_file.zip
```

---

bzip2recover

Used to recover files from a damaged bzip2 archive. It simply extracts out all the working blocks as there own bzip2 archives, you can than use _bzip2 -t_ on each file to test the integrity of them and extract the working files.

bzme

Will convert a file that is zipped or gzipped to a file compressed using _bzip2_.
Command syntax:
```
bzme filename
```

---
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Tip**
---|---
|  Both gzip and bzip2 supply tools to work within compressed files for example listing the files within the archive, running _less_ on them, using _grep_ to find files within the archive et cetera. For gzip the commands are prefixed with z, _zcat, zless, zgrep_. For bzip2 the commands are prefixed with bz, _bzcat, bzless, bzgrep_.
* * *
#  Chapter 16. Graphics tools (command line based)
The graphics tools chapter explains some image programs that can be called from the command-line. While I have found image programs that can be used from the command-line, zgv is the only one I've ever heard of, I did not find them very useful. All the tools listed use the X windowing system to work and simply run from the command line (so they can be scripted/automated if necessary).

montage

Creates a 'montage', an image created of many other images, arranged in a random fashion.
Command syntax:
```
montage r34.jpg r32.jpg skylines* skyline_images.miff
```

---
The above would create a “montage” of images (it would tile a certain number of images) into a composite image called “skyline_images.miff”, you could always use _display_ to view the image.
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Note**
---|---
| Note that the images are converted to the same size (scaled) so they can be tiled together.

convert

To convert the file format of an image to another image format. _convert_ is used to change a files format, for example from a jpeg to a bitmap or one of many other formats._convert_ can also manipulate the images as well (see the man page or the ImageMagick site).
Example from Jpeg to PNG format:
```
convert JPEG: thisfile.jpg PNG: thisfile.png
```

---

import

Captures screen-shots from the X server and saves them to a file. A screen-dump of what X is doing.
Command syntax:
```
import file_name
```

---

display

_display_ is used to display (output) images on the screen. Once open you are can also perform editing functions and are able to read/write images. It has various interesting options such as the ability to display images as a slide show and the ability to capture screenshots of a single window on-screen.
Command syntax (for displaying an image):
```
display image_name
```

---
To display a slide show of images, open the images you want possibly using a wildcard, for example:
```
display *.jpg
```

---
And then click on the image to bring up the menu and then look under the miscellaneous menu for the slide show option.
![Caution](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/caution.gif) | **Speed Warning**
---|---
| Be careful when opening multiple large sized images (especially on a slow machine) and putting the slide show on a small delay between image changes. Your processor will be overloaded and it will take a significant amount of time to be able to close ImageMagick.

identify

Will identify the type of image as well as it's size, colour depth and various other information. Use the _-verbose_ option to show detailed information on the particular file(s).
Command syntax:
```
identify image_name
```

---

mogrify

_mogrify_ is another ImageMagick command which is used to transform images in a number of different ways, including scaling, rotation and various other effects. This command can work on a single file or in batch.
For example, to convert a large number of tiff files to jpeg files you could type:
```
mogrify -format jpeg *.tiff
```

---
This command has the power to do a number of things in batch including making thumbnails of sets of images.
For this you could type:[[8]](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FTN.AEN10641)
```
mogrify -geometry 120x120 *.jpg
```

---

showrgb

_showrgb_ is used to uncompile an rgb colour-name database. The default is the one that X was built with. This database can be used to find the correct colour combination for a particular colour (well it can be used as a rough guide anyway).
To list the colours from the X database, simply type:
```
showrgb
```

---
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **Please note:**
---|---
|  All tools listed, excluding _showrgb_ are part of the ImageMagick package. Type _man ImageMagick_ for a full list of available commands. Or see the ImageMagick site
* * *
#  Chapter 17. Working with MS-DOS files
Use the mtools programs to work with ms-dos based files, execute _mtools_ for a full listing of available m* tools. There are a lot of files within the mtools package for working with ms-dos disks, also try the info documentation of mtools for more details.
![Note](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/note.gif) | **The use of slashes**
---|---
| Note that with mtools commands you can use the slashes on the a: part either way (ie. backslash (windows-style) or forward slash (UNIX system style)).

mformat

Formats an unmounted disk as an ms-dos floppy disk. Usage is similar to the ms-dos format utility, to format the first floppy disk you can type:
```
mformat a:
```

---

mcopy

Copies files from an ms-dos disk when it's not mounted. Similar to the ms-dos copy command except it's more advanced.
Command syntax:
```
mcopy a:/file_or_files /destination/directory
```

---

mmount

Mount an ms-dos disk, without using the normal UNIX system mount.
For example:
```
mmount a: /mnt/floppy
```

---
This will mount the floppy under /mnt/floppy (this option may or may not be necessary, it depends on your /etc/fstab setup).

mbadblocks

Scans an ms-dos (fat formatted disk) for bad blocks, it marks any unused bad blocks as “bad” so they won't be used.
Example:
```
mbadblocks a:
```

---

dosfsck

This program is used to check and repair ms-dos based filesystems. Use the _-a_ option to automatically repair the filesystem (ie don't ask the user questions), the _-t_ option to mark un-readable clusters as bad and the _-v_ option to be more verbose (print more information).
Example:
```
dosfsck -at /dev/fd0
```

---
This would check your floppy disk for any errors (and bad sectors) and repair them automatically.
* * *
#  Chapter 18. Scheduling Commands to run in the background
There are two main tools used to perform scheduled tasks, _at_ and _cron_. You may also like to try

at

'at' executes a command once on a particular day, at a particular time. _at_ will add a particular command to be executed.
Examples:
```
at 21:30
```

---
You then type the commands you want executed then press the end-of-file key (normally **CTRL** -**D** ). Also try:
```
at now + time
```

---
This will run at the current time + the hours/mins/seconds you specify (use _at now + 1 hour_ to have command(s) run in 1 hour from now...)
You can also use the _-f_ option to have at execute a particular file (a shell script).
```
at -f shell_script now + 1 hour
```

---
This would run the shell script 1 hour from now.

atq

Will list jobs currently in queue for the user who executed it, if root executes at it will list all jobs in queue for the at daemon. Doesn't need or take any options.

atrm

Will remove a job from the 'at' queue.
Command syntax:
```
atrm job_no
```

---
Will delete the job “job_no” (use _atq_ to find out the number of the job)

cron

cron can be used to schedule a particular function to occur every minute, hour, day, week, or month.
It's normal to use the crontab to perform the editing functions as this automates the process for the cron daemon and makes it easier for normal users to use cron.
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Anacron**
---|---
|  _anacron_ is another tool designed for systems which are not always on, such as home computers While _cron_ will not run if the computer is off, _anacron_ will simply run the command when the computer is next on (it catches up with things).

crontab

_crontab_ is used to edit, read and remove the files which the cron daemon reads.
Options for crontab (use _crontab -option(s)_):
  * _-e_ --- to edit the file.
  * _-l_ --- to list the contents of the file.
  * _-u username_ --- use the _-u_ with a username argument to work with another users crontab file.


When using _crontab -e_ you have a number of fields (6) what they mean is listed below:
Field | Allowed Values
---|---
minute | 0-59
hour | 0-23
day of month | 1-31
month | 1-12 (or names, see below)
day of week | 0-7 (0 or 7 is Sun, or use three letter names)
There are also a number of shortcut methods for common tasks, including:[[9]](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FTN.AEN11136)
  * _@reboot_ --- run command at reboot
  * _@yearly_ --- same as 0 0 1 1 *
  * _@annually_ --- same as @yearly
  * _@monthly_ --- same as 0 0 1 * *
  * _@weekly_ --- same as 0 0 * * 0
  * _@daily_ --- same as 0 0 * * *
  * _@midnight_ --- same as @daily
  * _@hourly_ --- same as 0 * * * *


[[10]](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FTN.AEN11169)
Note that * (asterisk) is used to mean anything (similar to the wildcard). For example if you leave the day part (the 5th place) with an asterisk it would mean everyday.
Lists are allowed. A list is a set of numbers (or ranges) separated by commas. Examples: ``1,2,5,9'', ``0-4,8-12”.
Step values can be used in conjunction with ranges. Following a range with ``/<number>'' specifies skips of the number's value through the range. For example, ``0-23/2'' can be used in the hours field to specify command execution every other hour (the alternative in the V7 standard is ``0,2,4,6,8,10,12,14,16,18,20,22''). Steps are also permitted after an asterisk, so if you want to say ``every two hours'', just use ``*/2''.
When writing a crontab entry you simply type in six fields separated by spaces, the first five are those listed in the table (using numbers or letters and numbers as appropriate), the 6th field is the command to be executed and any options, cron will read everything up until the newline.
Example:
```
5 4 * * sun echo "run at 5 after 4 every sunday"
```

---
This would run the echo command with the string shown at 4:05 every Sunday.
* * *
#  Chapter 19. Miscellaneous
The miscellaneous chapter contains commands that don't really fit into the other sections of this guide.

renaming�extensions

To rename all of the files in the current directory with a '.htm' extension to '.html', type:
```
$ chcase -x 's/htm/html/' '*.htm'
```

---
You can get a copy of _the chcase_ perl script
For more complex renaming you should read [Section 7.3](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#MASS-RENAME)

rel[[11]](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FTN.AEN11315)

Use rel to analyze text files for relevance to a given set of keywords. It outputs the names of those files that are relevant to the given keywords, ranked in order of relevance; if a file does not meet the criteria, it is not outputted in the relevance listing.

units�man�page

There is a man page, part of the Linux Programmers Manual called “units”. It displays various information on the various scientific measurements (such as mega, giga et cetera). This manual page also has a short discussion about the argument over which standard should be used to measure data (ie. the kibibyte vs kilobyte).
To access this man page type:
```
man 7 units
```

---

fortune

_fortune_ is a tool which will print a random, hopefully interesting quote or entertaining short piece of writing. There are options to customise which area the epigrams should come from. Just type _fortune_ to get a random epigram from any section.
Simply type:
```
fortune
```

---
* * *
#  Chapter 20. Mini-Guides
The mini-guides chapter is a section of the document that describes certain concepts in more depth than the usual command descriptions. The information listed is fairly specific as I have tried to avoid the duplication of too much information that is already online.
* * *
#  20.1. RPM: Redhat Package Management System

Checking

Installed RPM's
Use the _rpm -V_ option to check whether or not a package has been modified.
For example:
```
rpm -V textutils
```

---
If none of the files from the textutils package have changed then rpm will exit without outputting any data. If, on the other hand, the program has changed, you may see something like this:
```
U.5....T /bin/cat
```

---
This isn't as cryptic as it appears. The line returned from _rpm -V_ contains any number of eight characters plus the full path to the file. Here are the characters and their meaning:[[12]](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FTN.AEN11507)
  * S --- File size differs
  * M --- Mode differs (includes permissions and file type)
  * 5 --- MD5 sum differs
  * D --- Device major/minor number mismatch
  * L --- ReadLink(2) path mismatch
  * U --- User ownership differs
  * G --- Group ownership differs
  * T --- mTime differs


![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Mandriva Users Note**
---|---
|  Mandriva Linux uses a customised version of RPM called urpmi (It consists of the urpm* commands, urpmi to install, urpme to remove and urpmf and urpmq to query).  This customised version has advantages over standard RPM, including automatic-dependency solving and Debian apt-get style functions (ability to download programs over the internet and have all dependencies resolved automatically).  The urpm* commands are all described in detail in Mandriva's documentation and various sources online.
* * *
#  20.2. Checking the Hard Disk for errors
Checking the hard disk for errors on your primary drive is very, very rarely required in GNU/Linux, most checking is automated on start-up if it is required. If you do need to check the hard disk for errors you will first need to unmount it. Then use the file system checker, _fsck_.
```
fsck.file_system_type
```

---
If you had an ext3 file-system then it would be:
```
fsck.ext3
```

---
![Tip](https://tldp.org/LDP/GNU-Linux-Tools-Summary/images/tip.gif) | **Also try**
---|---
|  You can also try using:  | ```
fsck -t file_system_type
```

---
* * *
