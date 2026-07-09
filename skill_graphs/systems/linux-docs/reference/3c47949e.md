    Domain-Name Dispute-Resolution Policy can be invoked. Also known as
    Domain Name System, Domain Name Service, Domain Name Server.

 environment variable
     A variable that is available to any program that is started by the
    shell.

 ESD
     Enlightened Sound Daemon. This program is designed to mix together
    several digitized audio streams for playback by a single device.

 filesystem
     The methods and data structures that an operating system uses to keep
    track of files on a disk or partition; the way the files are organized on
    the disk. Also used to describe a partition or disk that is used to store
    the files or the type of the filesystem.

 FSSTND
     Often the group, which creates the Linux File System Structure document,
    or the document itself, is referred to as the 'FSSTND'. This is short for
    "file system standard". This document has helped to standardize the
    layout of file systems on Linux systems everywhere. Since the original
    release of the standard, most distributors have adopted it in whole or in
    part, much to the benefit of all Linux users. It is now often referred to
    as the FHS (Filesystem Hierarchy Standard) document though since its
    incorporation into the LSB (Linux Standards Base) Project.

 GUI
     Graphical User Interface. The use of pictures rather than just words to
    represent the input and output of a program. A program with a GUI runs
    under some windowing system (e.g. The X Window System, Microsoft Windows,
    Acorn RISC OS, NEXTSTEP). The program displays certain icons, buttons,
    dialogue boxes etc. in its windows on the screen and the user controls it
    mainly by moving a pointer on the screen (typically controlled by a
    mouse) and selecting certain objects by pressing buttons on the mouse
    while the pointer is pointing at them. Though Apple Computer would like
    to claim they invented the GUI with their Macintosh operating system, the
    concept originated in the early 1970s at Xerox's PARC laboratory.

 hard link
     A directory entry, which maps a filename to an inode, number. A file may
    have multiple names or hard links. The link count gives the number of
    names by which a file is accessible. Hard links do not allow multiple
    names for directories and do not allow multiple names in different
    filesystems.

 init
     'init' process is the first user level process started by the kernel.
    init has many important duties, such as starting getty (so that users can
    log in), implementing run levels, and taking care of orphaned processes.
    This chapter explains how init is configured and how you can make use of
    the different run levels. init is one of those programs that are
    absolutely essential to the operation of a Linux system, but that you
    still can mostly ignore. Usually, you only need to worry about init if
    you hook up serial terminals, dial-in (not dial-out) modems, or if you
    want to change the default run level. When the kernel has started (has
    been loaded into memory, has started running, and has initialized all
    device drivers and data structures and such), it finishes its own part of
    the boot process by starting a user level program, init. Thus, init is
    always the first process (its process number is always 1). The kernel
    looks for init in a few locations that have been historically used for
    it, but the proper location for it is /sbin/init. If the kernel can't
    find init, it tries to run /bin/sh, and if that also fails, the startup
    of the system fails. When init starts, it completes the boot process by
    doing a number of administrative tasks, such as checking filesystems,
    cleaning up /tmp, starting various services, and starting a getty for
    each terminal and virtual console where users should be able to log in.
    After the system is properly up, init restarts getty for each terminal
    after a user has logged out (so that the next user can log in). init also
    adopts orphan processes: when a process starts a child process and dies
    before its child, the child immediately becomes a child of init. This is
    important for various technical reasons, but it is good to know it, since
    it makes it easier to understand process lists and process tree graphs.
    init itself is not allowed to die. You can't kill init even with SIGKILL.
    There are a few variants of init available. Most Linux distributions use
    sysvinit (written by Miquel van Smoorenburg), which is based on the
    System V init design. The BSD versions of Unix have a different init. The
    primary difference is run levels: System V has them, BSD doesn't.

 inode
     An inode is the address of a disk block. When you see the inode
    information through ls, ls prints the address of the first block in the
    file. You can use this information to tell if two files are really the
    same file with different names (links). A file has several components: a
    name, contents, and administrative information such as permissions and
    modification times. The administrative information is stored in the inode
    (over the years, the hyphen fell out of "i-node"), along with essential
    system data such as how long it is, where on the disc the contents of the
    file are stored, and so on. There are three times in the inode: the time
    that the contents of the file were last modified (written); the time that
    the file was last used (read or executed); and the time that the inode
    itself was last changed, for example to set the permissions. Altering the
    contents of the file does not affect its usage time and changing the
    permissions affects only the inode change time. It is important to
    understand inodes, not only to appreciate the options on ls, but because
    in a strong sense the inodes are the files. All the directory hierarchy
    does is provide convenient names for files. The system's internal name
    for the file is its i-number: the number of the inode holding the file's
    information.

 kernel
     Part of an operating system that implements the interaction with
    hardware and the sharing of resources.

 libraries
     Executables should have no undefined symbols, only useful symbols; all
    useful programs refer to symbols they do not define (eg. printf or
    write). These references are resolved by pulling object files from
    libraries into the executable.

 link
     A symbolic link (alias in MacOS and shortcut under Windows) is a file
    that points to another file; this is a commonly used tool. A hard-link
    rarely created by the user, is a filename that points to a block of data
    that has several other filenames as well.

 man page
     Every version of UNIX comes with an extensive collection of online help
    pages called man pages (short for manual pages). The man pages are the
    authoritative documentation about your UNIX system. They contain complete
    information about both the kernel and all the utilities.

 MTA
     Mail Transfer Agents. Alongside the web, mail is the top reason for the
    popularity of the Internet. E-mail is an inexpensive and fast method of
    time-shifted messaging which, much like the Web, is actually based around
    sending and receiving plain text files. The protocol used is called the
    Simple Mail Transfer Protocol (SMTP). The server programs that implement
    SMTP to move mail from one server to another are called MTAs. Once upon a
    time users would have to Telnet into an SMTP server and use a command
    line mail program like 'mutt' or 'pine' to check their mail. Now, GUI
    based e-mail clients like Mozilla, Kmail and Outlook allow users to check
    their email off of a local SMTP sever. Additional protocols like POP3 and
    IMAP4 are used between the SMTP server and desktop mail client to allow
    clients to manipulate files on, and download from, their local mail
    server. The programs that implement POP3 and IMAP4 are called Mail
    Delivery Agents (MDAs). They are generally separate from MTAs.

 NFS
     Network File System, is the UNIX equivalent of Server Message Block
    (SMB). It is a way through which different machines can import and export
    local files between each other. Like SMB though, NFS sends information
    including user passwords unencrypted, so it's best to limit its usage to
    within your local network.

 operating system
     Software that shares a computer system's resources (processor, memory,
    disk space, network bandwidth, and so on) between users and the
    application programs they run. Controls access to the system to provide
    security.

 PAM
     Pluggable Authentication Modules. A suite of shared libraries that
    determine how a user will be authenticated. For example, conventionally
    UNIX users authenticate themselves by supplying a password at the
    password prompt after they have typed their name at the login prompt. In
    many circumstances, such as internal access to workstations, this simple
    form of authentication is considered sufficient. In other cases, more
    information is warranted. If a user wants to log in to an internal system
    from an external source, like the Internet, more or alternative
    information may be required - perhaps a one-time password. PAM provides
    this type of capability and much more. Most important, PAM modules allow
    you to configure your environment with the necessary level of security.

 PATH
     The shell looks for commands and programs in a list of file paths stored
    in the PATH environment variable. An environment variable stores
    information in a place where other programs and commands can access it.
    Environment variables store information such as the shell that you are
    using, your login name, and your current working directory. To see a list
    of all the environment variables currently defined; type 'set' at the
    prompt. When you type a command at the shell prompt, the shell will look
    for that command's program file in each directory listed in the PATH
    variable, in order. The first program found matching the command you
    typed will be run. If the command's program file is not in a directory
    listed in you PATH environment variable, the shell returns a "commands
    not found" error. By default, the shell does not look in your current
    working directory or your home directory for commands This is really a
    security mechanism so that you don't execute programs by accident. What
    if a malicious user put a harmful program called ls in your home
    directory? If you typed ls and the shell looked for the fake program in
    your home directory before the real program in the /bin directory, what
    do you think would happen? If you thought bad things, you are on the
    right track. Since your PATH doesn't have the current directory as one of
    its search locations, programs in your current directory must be called
    with an absolute path of a relative path specified as './program-name'.
    To see what directories are part of your PATH enter this command: # echo
    $PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/
    bin/X11

 pipes and sockets
     Special files that programs use to communicate with one another. They
    are rarely seen, but you might be able to see a socket or two in the /dev
    / directory.

 process identifier
     Shown in the heading of the ps command as PID. The unique number
    assigned to every process running in the system.

 rpc
     Remote Procedure Calls. It enables a system to make calls to programs
    such as NFS across the network transparently, enabling each system to
    interpret the calls as if they were local. In this case, it would make
    exported filesystems appear as thought they were local.

 set group ID (SGID)
     The SGID permission causes a script to run with its group set to the
    group of the script, rather than the group of the user who started it. It
    is normally considered extremely bad practice to run a program in this
    way as it can pose many security problems. Later versions of the Linux
    kernel will even prohibit the running of shell scripts that have this
    attribute set.

 set user ID (SUID)
     The SUID permission causes a script to run as the user who is the owner
    of the script, rather than the user who started it. It is normally
    considered extremely bad practice to run a program in this way as it can
    pose many security problems. Later versions of the Linux kernel will even
    prohibit the running of shell scripts that have this attribute set.

 signal
     Software interrupts sent to a program to indicate that an important
    event has occurred. The events can vary from user requests to illegal
    memory access errors. Some signals, like the interrupt signal, indicate
    that a user has asked the program to do something that is not in the
    usual flow of control.

 SSH
     The Secure Shell, or SSH, provides a way of running command line and
    graphical applications, and transferring files, over an encrypted
    connection, all that will be seen is junk. It is both a protocol and a
    suite of small command line applications, which can be used for various
    functions. SSH replaces the old Telnet application, and can be used for
    secure remote administration of machines across the Internet. However, it
    also has other features. SSH increases the ease of running applications
    remotely by setting up X permissions automatically. If you can log into a
    machine, it allows you to run a graphical application on it, unlike
    Telnet, which requires users to have an understanding of the X
    authentication mechanisms that are manipulated through the xauth and
    xhost commands. SSH also has inbuilt compression, which allows your
    graphic applications to run much faster over the network. SCP (Secure
    Copy) and SFTP (Secure FTP) allow transfer of files over the remote link,
    either via SSH's own command line utilities or graphical tools like
    Gnome's GFTP. Like Telnet, SSH is cross-platform. You can find SSH server
    and clients for Linux, Unix and all flavours of Windows, BeOS, PalmOS,
    Java and embedded Oses used in routers.

 STDERR
     Standard error. A special type of output used for error messages. The
    file descriptor for STDERR is 2.

 STDIN
     Standard input. User input is read from STDIN. The file descriptor for
    STDIN is 0.

 STDOUT
     Standard output. The output of scripts is usually to STDOUT. The file
    descriptor for STDOUT is 1.

 symbol table
     The part of an object table that gives the value of each symbol (usually
    as a section name and an offset) is called the symbol table. Executables
    may also have a symbol table, with this one giving the final values of
    the symbols. Debuggers use the symbol table to present addresses to the
    user in a symbolic, rather than a numeric form. It is possible to strip
    the symbol table from executables resulting in a smaller sized executable
    but this prevents meaningful debugging.

 symbolic link or soft link
     A special filetype, which is a small pointer file, allowing multiple
    names for the same file. Unlike hard links, symbolic links can be made
    for directories and can be made across filesystems. Commands that access
    the file being pointed to are said to follow the symbolic link. Commands
    that access the link itself do not follow the symbolic link.

 system call
     The services provided by the kernel to application programs, and the way
    in which they are invoked. See section 2 of the manual pages.

 system program
     Programs that implement high level functionality of an operating system,
    i.e., things that aren't directly dependent on the hardware. May
    sometimes require special privileges to run (e.g., for delivering
    electronic mail), but often just commonly thought of as part of the
    system (e.g., a compiler).

 tcp-wrappers
     Almost all of the services provided through inetd are invoked through
    tcp-wrappers by way of the tcp-wrappers daemon, tcpd. The tcp-wrappers
    mechanism provides access control list restrictions and logging for all
    service requests to the service it wraps. It may be used for either TCP
    or TCP services as long as the services are invoked through a central
    daemon process such as inetd. These programs log the client host name of
    incoming telnet, ftp, rsh, rlogin, finger etc.... requests. Security
    options are access control per host, domain and/or service; detection of
    host name spoofing or host address spoofing; booby traps to implement an
    early-warning system.

 ZSH
     Zsh was developed by Paul Falstad as a replacement for both the Bourne
    and C shell. It incorporates features of all the other shells (such as
    file name completion and a history mechanism) as well as new
    capabilities. Zsh is considered similar to the Korn shell. Falstad
    intended to create in zsh a shell that would do whatever a programmer
    might reasonably hope it would do. Zsh is popular with advanced users.
    Along with the Korn shell and the C shell, the Bourne shell remains among
    the three most widely used and is included with all UNIX systems. The
    Bourne shell is often considered the best shell for developing scripts.


-----------------------------------------------------------------------------
Appendix A. UNIX System V Signals

Symbol     Number   Action       Meaning
SIGHUP     1        exit         Hangs up.
SIGINT     2        exit         Interrupts.
SIGQUIT    3        core dump    Quits.
SIGILL     4        core dump    Illegal instruction.
SIGTRAP    5        core dump    Trace trap.
SIGIOT     6        core dump    IOT instruction.
SIGEMT     7        core dump    MT instruction.
SIGFPE     8        core dump    Floating point exception.
SIGKILL    9        exit         Kills (cannot be caught or ignored).
SIGBUS     10       core dump    Bus error.
SIGSEGV    11       core dump    Segmentation violation.
SIGSYS     12       core dump    Bad argument to system call.
SIGPIPE    13       exit         Writes on a pipe with no one to read it.
SIGALRM    14       exit         Alarm clock.
SIGTERM    15       exit         Software termination signal.
-----------------------------------------------------------------------------

Appendix B. Sources

��*�The UNIX programming environment, Brian W. Kernighan, Rob Pike, Prentice
    Hall, New Jersey, 1984.


��*�Newnes UNIX Pocket Book, Steve Heath, Butterworth-Heinemann, Great
    Britain, 1998.


��*�Suse Linux Installation and Configuration, Nazeeh Amin El-Dirghami &
    Youssef A. Abu Kwaik, QUE Corporation, USA, 2000.


��*�Inside Linux, Michael J. Tobler, New Riders Publishing, USA, 2001.


��*�Linux in a Nutshell 2nd Edition, Ellen Siever, O'Reilly & Associates
    Inc., CA, USA, 1999


��*�Using Caldera OpenLinux Special Edition, Allan Smart, Erik Ratcliffe, Tim
    Bird, David Bandel, QUE Corporation, USA, 1999.


��*�Linux System Security (The Administrator's Guide to Open Source Security
    Tools), Scott Mann & Ellen L. Mitchell, Prentice-Hall, New-Jersey, 2000.


��*�XFree86 For Linux (Uncommon Solutions for the Technical Professional),
    Aron Hsiao, QUE Corporation, USA, 1999.


��*�Complete Idiot's Guide to Linux Second Edition, Manuel Alberto Ricart,
    QUE Corporation, USA, 1999.


��*�Lions' Commentary on UNIX 6th Edition with Source Code, John Lions,
    Peer-to-Peer Communications Incorporated, USA, 1996.


��*�The Linux System Administrators' Guide Version 0.6.1, Lars Wirzenius,
    liw@iki.fi, Finland, 1998.


��*�SAMS Teach Yourself Shell Programming in 24 Hours, Sriranga
    Veerararaghavan, SAMS Publishing, USA, 1999.


��*�433-252 Software Development: Principles and Tools, Zoltan Somogyi, Les
    Kitchen, The University of Melbourne, Department of Computer Science and
    Software Engineering, Australia, 2002.


��*�The Advanced Linux Pocketbook, Ashton Mills, ashtonmills@bigpond.com, ACP
    Publishing Pty Ltd, Australia, 2001.


��*�http://www.pathname.com/fhs


��*�http://www.atnf.csiro.au/people/rgooch/linux/docs/devfs.html


��*�http://freeos.com/articles/3102/


��*�http://freeos.com/articles/2879/


��*�http://www.linuxjournal.com/article.php?sid=1104


��*�http://www.mlinux.org/projects/present/filesys/slide01.html


��*�http://www.mil.ufl.edu/linuxhelp/linuxfilesystem.pdf


��*�http://www.nsa.gov/selinux/doc/slinux/node57.html


��*�http://www.linuxnow.com/tutorial/fs/fs.html


��*�http://info.cqu.edu.au/courses/aut2001/85321/resources/study_guide/
    chapter_4


��*�http://lwn.net/2001/features/ols/pdf/pdf/devfs.pdf


��*�/usr/src/linux/Documentation/filesystems/proc.txt, Terrehon Bowden <
    terrehon@pacbell.net>, Bodo Bauer <bb@ricochet.net>, Jorge Nerin <
    comandante@zaralinux.com>


��*�/usr/share/doc/FAQ/Linux-FAQ/index.html, ftp://rtfm.mit.edu/pub/
    usenet-by-hierarchy/comp/os/linux/misc/, David Merrill, david -AT-
    lupercalia.net, Robert Kiesling, rkiesling@mainmatter.com, Linux
    Frequently Asked Questions with Answers, 2001-12-04.


��*�/usr/share/doc/sysvinit/README.runlevels.gz


��*�/usr/src/linux/Documentation/initrd.txt, Werner Almesberger <
    werner.almesberger@epfl.ch> and Hans Lermen <lermen@fgan.de>, 2000.


��*�http://www.opussoftware.com/tutorial/TutMakefile.htm


��*�http://www.cc.gatech.edu/people/home/oxblood/Linux_Doc.txt


��*�http://users.erols.com/mmmcd/lilo/boot_sequence.html


��*�hints.linuxfromscratch.org/hints/grub-howto.txt


��*�http://www.fifi.org/cgi-bin/man2html?initrd+4


��*�http://www.linuxsa.org.au/meetings/1997-06/fsstnd/fsstnd.html


��*�http://public.csusm.edu/public/guests/history/netinfo/arpa.html


��*�http://whatis.techtarget.com/definition/0,,sid9_gci214635,00.html


��*�http://whatis.techtarget.com/definition/0,,sid9_gci213627,00.html


��*�http://www.darpa.mil/


��*�http://hostingworks.com/support/dict.phtml?foldoc=
    Defense%2BAdvanced%2BResearch%2BProjects%2BAgency


��*�http://www.linuxsa.org.au/meetings/1997-06/fsstnd/fsstnd.html


��*�http://compnetworking.about.com/library/glossary/bldef-dns.htm


��*�http://www.scala.com/definition/graphical-user-interface.html


��*�http://hostingworks.com/support/dict.phtml?foldoc=
    Graphical+User+Interface


��*�http://www.mostang.com/sane/intro.html


-----------------------------------------------------------------------------
Appendix C. About the Author

  Binh Nguyen was born, 26 March 1983, Melbourne, Victoria. He studied at St
Josephs Marist Brothers College, North Fitzroy until receiving a scholarship
to St Kevin's College, Toorak in 1998.

  He is currently a university undergraduate studying computer science and
physics at the University of Melbourne. His main interests in each area are
in Operating Systems and Quantum Mechanics respectively.

  His background is strongly biased towards science and mathematics.
Nonetheless, he does have an appreciation for the arts, humanities and sport.
A reasonably proficient musician (flute), he is currently pondering whether
he should complete his musical studies to obtain a diploma so that he can
teach. In high school, he was a member of the athletics, basketball,
football, cricket and swimming squads. He speaks English predominately but is
also able to communicate in Vietnamese and French. When younger he also
possessed the ability to communicate in Chinese and Italian.

  Although brought up as a Buddhist and studying at Catholic/Christian
schools all his life as well as studying scripture during his final year of
high school he considers himself an atheist.

  At this moment in time, he works part-time as a (commercial) researcher/
developer on Linux related projects with his current focus being on software
distribution mechanisms.

  Two of his technical documents have been incorporated into the Linux
Documentation Project ("Linux Dictionary" and "Linux Filesystem Hierarchy",
[www.tldp.org/guides.html]   www.tldp.org/guides.html). Furthermore, they are
being used as reference books in at least ten universities around the world
(University of Southern Queensland (Australia), Universidad Michoacana
(Mexico), Hong Kong Polytechnic University (Hong Kong), Universidade de Sao
Paolo (Brazil), University of Southern California (United States of America),
University of Wales Swansea (United Kingdom), University of Ulster (Ireland),
Universit�t Duisburg-Essen (Germany), Universidad Rey Juan Carlos (Spain),
