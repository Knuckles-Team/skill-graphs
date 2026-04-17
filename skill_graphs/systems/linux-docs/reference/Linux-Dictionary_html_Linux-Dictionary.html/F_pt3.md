
**File conversion utility**

A utility program that converts text or graphoics files created with one program to the file format used by another program. The best application programs now include a conversion utility that can handle a dozen or more file formats. From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**file extension**

In filenames, the group of letters after the period is called the file extension.From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**File format**

The patterns and standards that a program uses to store data on disk. Few programs store data in ASCII format. Most use a proprietry file format that other programs cannot read, ensuring that customers continue to use the company's program and enabling the programmers to include special features that standard formats might not allow. See file conversion utilitu and native file format. From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**File fragmentattion**

The allocation of a file in noncontiguoug sectors on a floppy or hard disk. Fragmentation occues because of multiple file delections and write operations. File gramentattion can seriously reduce disk efficiency, because a disk drive's rad/write head must travel longer distances to retrieve a file that's scattered all over the disk. Defragmenting can improve disk efficiency by as much as 50 percent by rewriting files so that they are placed in contiguous clusters. See defragmentation. From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**File Locking**

Often, one would like a process to have exclusive access to a file. By this we mean that only one process can access the file at any one time. Consider a mail folder: if two processes were to write to the folder simultaneously, it could become corrupted. We also sometimes want to ensure that a program can never be run twice at the same time; this insurance is another use for ``locking.'' In the case of a mail folder, if the file is being written to, then no other process should try read it or write to it: and we would like to create a write lock on the file. However if the file is being read from, no other process should try to write to it: and we would like to create a read lock on the file. Write locks are sometimes called exclusive locks; read locks are sometimes called shared locks. Often, exclusive locks are preferred for simplicity. Locking can be implemented by simply creating a temporary file to indicate to other processes to wait before trying some kind of access. UNIX also has some more sophisticated builtin functions. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**File locking**

On a network, a method of concurrency control that ensures the integrity of data. File locking prevents moe than one user from accessing and altering a file at the same time. See Local Area Network (LAN). From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**File Manager**

software that allows you to select, copy, move, and open files and directories in a graphical environment. From Linux Guide @FirstLinux Examples of file managers on Linux include konqueror for KDE and mc (Midnight Commander). The Windows equivalent would be Windows Explorer. From Binh <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**file name**

The name given to a file to distinguish one piece of data from others. Modern operating systems such as Red Hat Linux allow long and descriptive file names with few restrictions (for example, all alphanumeric characters and spaces are allowed). From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**File Ownerships**

Each file on a system is owned by a particular user and also owned by a particular group. When you run ls -al, you can see the user that owns the file in the third column and the group that owns the file in the fourth column (these will often be identical, indicating that the file's group is a group to which only the user belongs). To change the ownership of the file, simply use the chown, change ownerships, command as follows. chown <user>[:<group>] <filename> From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**file server**

A process that provides access to a file from remote devices. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**File server**

In a Local Area Network (LAN), a computer that stoes on its hard disk the application programs and data files for all workstations in the network. In a peer-to-peer network, all workstations act as file servers, because each workstattion can provide files to other workstations. In the more common client/server architecture, a single, high-powered machine with a huge hard disk is set aside to function as the file server for all the workstations (clients) in the network. See Network Operating System (NOS). From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**File System**

A set of programs that tells an operating system how to access and interpret the contents of a disk or tape drive, or other storage medium. Common file systems include: FAT and FAT-32 (DOS/Windows), HPFS (OS/2), NFS, NTFS (Windows NT/2000), and others. From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**file system**

The method in which an operating system organizes and manages files. Red Hat Linux uses a hierarchical file system in which files are stored in directories and subdirectories. From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**file system**

the physical or logical device that holds a collection of files and directories. This might be a hard disk drive or a partition on a disk drive. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**File Transfer Protocol (FTP)**

A protocol used for transferring files between machines on networks such as LANs and the Internet. In a typical FTP session, a client logs onto an FTP server, views directory listings, and downloads files from the server. FTP sessions can either be anonymous or require authentication for access. From Redhat-9-Glossary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**file type**

A description of the function of a file. These types include ordinary files, directories, and special files, which represent devices in the system. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**file-kanji**

kanji code checker This package contains file2. File2 tests each argument in an attempt to classify it to JIS, EUC, SJIS, ascii and UNKNOWN. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**file-rc**

Alternative boot mechanism using a single configuration file This package provides an alternative mechanism to boot the system, to shut it down and to change runlevels. The /etc/rc?.d/* links will be converted into one single configuration file /etc/runlevel.conf instead, which is easier to administrate than symlinks, and is also more flexible. The package will automatically convert your existing symlinks into the file method on installation, and convert the file back into symlinks on removal. Both mechanisms are compatible through /etc/init.d/rc, /etc/init.d/rcS, /usr/sbin/update-rc.d, and /usr/sbin/invoke-rc.d scripts. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**file-roller**

File Roller is an archive manager for the GNOME environment. This means that you can : create and modify archives; view the content of an archive; view afile contained in the archive; extract files from the archive. File Roller is only a front-end (a graphical interface) to archiving programs like tar and zip. The supported file types are : Tar archives uncompressed (.tar) or compressed with gzip (.tar.gz , .tgz), bzip (.tar.bz , .tbz), bzip2 (.tar.bz2 , .tbz2), compress (.tar.Z , .taz), lzop (.tar.lzo , .tzo), Zip archives (.zip), Jar archives (.jar , .ear , .war), Lha archives (.lzh), Rar archives (.rar), Single files compressed with gzip, bzip, bzip2, compress, lzop From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**file-types-capplet**

allows you to configure how files of various types should be handled. From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**filemenu-applet**

A directory navigation GNOME applet. File Menu Applet is a small GNOME panel application which creates a file manager. File Menu Applet is not designed to replace your existing file manager, but instead work with it. It supports standard drag and drop, GNOME file types, and Nautilus icons. One may use it for small tasks such a easily attaching files to emails in Evolution or Sylpheed by dragging them out of File Menu Applet into the composer window. It's also excellent for selecting songs to play from your MP3 or OGG collection. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Filename**

A unique name assigned to a file when the file is written on a disk. From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**filerunner**

X-Based FTP program & file manager FileRunner is an X-Based FTP program. It gives you a windowed view of files on your local system and a remote system. It allows transferring multiple files at once, tagging of files, etc. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Files**

Common to every computer system invented is the file. A file holds a single contiguous block of data. Any kind of data can be stored in a file, and there is no data that cannot be stored in a file. Furthermore, there is no kind of data that is stored anywhere else except in files. A file holds data of the same type, for instance, a single picture will be stored in one file. During production, this book had each chapter stored in a file. It is uncommon for different types of data (say, text and pictures) to be stored together in the same file because it is inconvenient. A computer will typically contain about 10,000 files that have a great many purposes. Each file will have its own name. The file name on a LINUX or UNIX machine can be up to 256 characters long. From Rute-Users-Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**filesystem**

The methods and data structures that an operating system uses to keep track of files on a disk or partition; the way the files are organized on the disk. Also used to describe a partition or disk that is used to store the files or the type of the filesystem. From Linux Administrator's Guide <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**filetraq**

Small utility to keep track of changes in config files. FileTraq is just a shell script that reads a list of files to watch, runs diff against each file and its backup, and reports any discrepancies, along with keeping a dated backup of the original. It's designed to be run as a cron job. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**fileutils**

GNU file management utilities This package contains the essential system utilities to manipulate files on your system. Included in this package are commands to change the permissions on files, list the files in a directory, create new directories, and list free disk space, among other things. The specific utilities included are: chgrp chmod chown cp dd df dir dircolors du install ln ls mkdir mkfifo mknod mv rm rmdir shred touch vdir sync. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**fileutils**

The fileutils package includes a number of GNU versions of common andpopular file management utilities. Fileutils includes the following tools: chgrp (changes a file's group ownership), chown (changes a file's ownership), chmod (changes a file's permissions), cp (copies files), dd (copies and converts files), df (shows a filesystem's diskusage), dir (gives a brief directory listing), dircolors (the setup program for the color version of the ls command), du (shows disk usage), install (copies files and sets permissions), ln (creates file links), ls (lists directory contents), mkdir (creates directories),mkfifo (creates FIFOs or named pipes), mknod (creates special files),mv (renames files), rm (removes/deletes files), rmdir (removes empty directories), sync (synchronizes memory and disk), touch (changes file timestamps), and vdir (provides long directory listings). From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**filler**

Simple game in Java Filler is a simple two-player game written in java. The object of the game is to conquer more area of the playing board than your opponent. This game requires a java 2 runtime environment. Try www.blackdown.de or java.sun.com From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**FILO**

First In Last Out From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**filter**

A program that filters local email via forward/pipe filter is one of the original mailfiltering programs written for UNIX. (originally a part of the 'elm' mailer) Install it via a pipe(|) reference in $HOME/.forward, and let it separate your incoming email into different personal mailboxes. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Filter**

A program that reads data (from a file, program output or command line entry) as input, processes it according to a set of predefined conditions (for example, sorted alphabetically) and outputs the processed data. Some filters include Awk, Grep, Sed and Sort. From I-gloss <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**filter**

A program that takes a set of data (usually in a file) as input, processes the data, and makes the processed data its output. Some examples of filters include grep, sort, awk, and sed. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Filter**

Any utility program that functions automatically to screen data. In electronic mail, you can use a filter to delete unwanted messages automatically. From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Filter**

Hardware or software designed to restrict access to certain areas on the Internet. From Glossary of Distance Education and Internet Terminology <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**filterproxy**

A filtering proxy, which can among other things remove ads. FilterProxy is a Perl script that acts as a generic web proxy. It is unique in that it allows "Modules" to be installed that can perform arbitrary transformations on HTML(or any other mime-type). Currently it filters ads, and compresses HTML content (for a 5-1 speedup on modems!) Configuration is done with web forms. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**filters**

a collection of filters, including B1FF and the Swedish Chef A collection of filters to do all sorts of strange things to text. This includes such favorites as B1FF and the Swedish Chef, and a wide range of others. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**FIMAS**

Financial Institution Message Authentication Standard (banking, ANSI) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**find**

search for files in a directory hierarchy From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**find2perl**

translate find command lines to Perl code From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**findaffix**

Interactive spelling checking From whatis <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**findimagedupes**

Finds visually similar or duplicate images findimagedupes is a commandline utility which performs a rough "visual diff" to two images. This allows you to compare two images or a whole tree of images and determine if any are similar or identical. The program can optionally export a GQView compatible collection file, so you can deal with the duplicates visually. On common image types, findimagedupes seems to be around 98% accurate. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**findutils**

The findutils package contains programs which will help you locatefiles on your system. The find utility searches through a hierarchy of directories looking for files which match a certain set of criteria(such as a filename pattern). The locate utility searches a database (create by updatedb) to quickly find a file matching a given pattern. The xargs utility builds and executes command lines from standard input arguments (usually lists of file names generated by the findcommand). You should install find utils because it includes tools that are very useful for finding things on your system. From Mandrake 9.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**findutils**

The findutils package contains programs which will help you locatefiles on your system. The find utility searches through a hierarchy of directories looking for files which match a certain set of criteria (such as a filename pattern). The xargs utility builds and executescommand lines from standard input arguments (usually lists of filenames generated by the find command). From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**findutils**

utilities for finding files--find, xargs, and locate These utilities find files meeting specified criteria and perform various actions on the files which are found. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Finger**

A Unix command that provides information about users logged in, and can also be used to retrieve the .plan and .project files from a users home directory. From KADOWKEV <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**finger**

A user information lookup program that shows a person's full name, most recent log-in time, and other information. From Linux Guide @FirstLinux <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Finger**

An Internet software tool for locating people on other Internet sites. Finger is also sometimes used to give access to non-personal information, but the most common use is to see if a person has an account at a particular Internet site. Many sites do not allow incoming Finger requests, but many do. From Matisse <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Finger**

An Internet utility that enables you to obtain information about a use who has an electronic mail address. Normally, this information is limited to the person's full name, job title, and address. However, the use can set up finger to retrieve one or more text files that contain information (such as a resume) that the user wants to make public. From QUECID <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**finger**

Finger is a utility that displays information about system users (login name, home directory, name, how long they have been logged in, etc.). The finger package includes a standard finger client. You should install finger if you would like to retrieve finger information from other systems. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**finger**

In UNIX, the finger service provides information about a users. Fingering a user, such as running the command "finger rob@robertgraham.com", will often display the contents of the .plan file. Fingering no specific user, such as finger @robertgraham.com, will list all the users who are logged on. Fingering users is often done during the reconnaissance phase of an attack. Example: The following shows the output of the command "finger rob@rh5.robertgraham.com": Login: rob Name: Robert David Graham Directory: /home/rob Shell: /bin/bash On since Fri Dec 3 18:13 (PST) on ttyp0 from gemini No mail. No Plan Key point: The finger command reveals extensive information. For example, if I were attacking the above machine, I would notice that the user is running bash Therefore, I may try something like http://rh5.robertgraham.com/ against the user, which in about 1% of the cases will give me a history file of recent commands they've entered, which may contain passwords and such. Key point: There are a number of fun things you can do with finger. The first is that you can use the "finger bounce" technique. Finger servers will often forward requests for you. The command: finger rob@robertgraham.com@example.com will query example.com for rob@robertgraham.com. You can use this technique to hide where your are coming from. On some systems, you can do a DoS attack by sending a finger command like: finger rob@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@robertgraham.com causing the system to go into a loop trying to resolve this. There are also special names you can finger. An empty name will sometimes list the currently logged on users, or sometimes all users with accounts on a machine. The special names of "0", "*", "**" will sometimes have similar effects. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**finger**

User information lookup program. finger displays information about the system users. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**finger**

[WAITS, via BSD Unix] 1. n. A program that displays information about a particular user or all users logged on the system, or a remote system. Typically shows full name, last login time, idle time, terminal line, and terminal location (where applicable). May also display a plan file left by the user (see also Hacking X for Y). 2. vt. To apply finger to a username. 3. vt. By extension, to check a human's current state by any means. "Foodp?" "T!" "OK, finger Lisa and see if she's idle." 4. Any picture (composed of ASCII characters) depicting `the finger'. Originally a humorous component of one's plan file to deter the curious fingerer (sense 2), it has entered the arsenal of some flamers. From Jargon Dictionary <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**finger-server**

Finger is a utility that displays information about system users(login name, home directory, name, how long they've been logged in,etc.). The finger-server package includes a standard finger server. From Redhat 8.0 RPM <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**fingerd**

Remote user information server. Fingerd is a simple daemon based on RFC1196 that provides an interface to the "finger" program at most network sites. The program is supposed to return a friendly, human-oriented status report on either the system at the moment or a particular person in depth. From Debian 3.0r0 APT <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**fingerprint**

A common scan hackers perform nowadays is fingerprinting a system in order to figure out what operating system it is running. The two main types of fingerprinting are Queso, which sends weird TCP flags, and nmap, which sends weird TCP options. Narrowing down the operating system is important. For example, attempting Windows-specific hacks against a UNIX system is pointless. Fingerprinting is possible because the TCP/IP specifications do not fully define the behavior of a protocol stack. Therefore, by sending unusual (undefined) network traffic at a system, the hacker will receive responses unique to that system. Key point: One of the key reasons for fingerprinting a system is to search for "old" or "unusual" systems. Non-computer devices like routers, printers, modem banks, etc. are not written to the same level of security standards as real computers. In addition, a hacker may be able to find old SunOS 4 systems which are rife with well-known security flaws. From Hacking-Lexicon <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**Finnix**

Finnix is a self-contained, bootable Linux CD distribution, based on Red Hat Linux 6.1. Finnix was created as a system maintenance distribution. You can mount hard drives, set up network devices, repair filesystems, and pretty much do anything you can do with a regular distribution. A CD-based distribution. From LWN Distribution List <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**FIOC**

Frame Input/Output Controller From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**FIP**

Facility Interface Processor From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**FIP**

Factory Instrumentation Protocol From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**FIP**

Fluorescent Indicator Panel From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**FIPA**

Foundation for Intelligent Physical Agents (org., Agents) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**FIPS**

Federal Information Processing Standard (NIST, USA) From VERA <http://www.tldp.org/LDP/Linux-Dictionary/html/index.html>

**FIR**
