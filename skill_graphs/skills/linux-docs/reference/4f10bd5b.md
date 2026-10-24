
15.3.1.5. Processing Incoming E-Mail with procmail

   This step is completely optional. The above described sendmail
   configuration calls procmail for each received email, but you could
   have called procmail using the .forward file (see the procmail man
   page). Procmail is a handy tool to block spam and to sort incoming
   email.

   You need to setup a .procmailrc file to use procmail. See the man
   page for procmail, procmailrc, and procmailex (examples). My setup
   demonstrates, how to ignore certain email messages and split
   email-collections (digest) into pieces:

# -- mail filtering -- procmail is called by sendmail --
PATH=/bin:/usr/bin
MAILDIR=$HOME/Mail
LOGFILE=$MAILDIR/from
# keep in mind:
# use ":0:" when writing to a file
# use ":0"  when writing to a device, e.g. /dev/null, or send email

# - make a backup of *all* incoming mail, but ignore mail tagged below -
:0 c:
*! ^Sissa-Repro
backup

# - keep only last 50 messages
:0 ic
| cd backup && rm -f dummy `ls -t msg.* | sed -e 1,50d`

# - delete email coming through the 'postdocs' email list, when
# it is not of any interest
:0
* ^From.*postdocs
* ^From.*Ernst Richter /dev/null :0
* ^From.*postdocs
* ^Subject.*card charge
/dev/null
# Split mailing list from the sissa preprint server into individual emails
# - this is quite complicated :(   I can flip through the list much
#   faster and ignore preprints which have uninteresting titles. Instead of
#   having to browse through the whole list, my mailer will just present a
#   list of papers.
# 1. split it in individual messages
:0
* ^From no-reply@xxx.lanl.gov
| formail +1 -de -A "Sissa-Repro: true" -s procmail
# 2. reformat messages a bit
# 2.1. extract 'Title:' from email-Body and add to email-header
as 'Subject:'
:0 b
* ^Sissa-Repro
*! ^Subject
TITLE=| formail -xTitle:
:0 a
|formail -A "Subject: $TITLE " -s procmail

# 2.2. store in my incoming sissa-email folder. Here, we could
#      also reject (and thereafter delete) uninteresting 'Subjects'
#      we could also mark more interesting subjects as urgend or send a copy
#      to regular mail box.
:0:
* ^Sissa-Repro
* ^Subject
*! ^replaced with
sissa

   By the way, there is a tk GUI tool to configure procmail (I think it
   is called dotfiles).
     ________________________________________________________________

15.3.2. Email with UUCP

   Another possible solution for Email is to use UUCP. This software was
   made for disconnected machines, and is by far the easiest solution if
   you have several users on your laptop (we are talking about UNIX,
   remember?), each with his/her own account.

   Unlike what most people think, UUCP does not need a serial
   connection: it works fine over TCP/IP, so your UUCP partner can be
   any machine on the Internet, if it is reachable from your network
   attachment point. Here is the UUCP sys for a typical laptop:
system mylaptop
time any
chat "" \d\d\r\c ogin: \d\L word: \P
address uucp.mypartner.org
port TCP
     ________________________________________________________________

15.3.3. MailSync

   [http://mailsync.sourceforge.net/] Mailsync is a way of synchronizing
   a collection of mailboxes. The algorithm is a 3-way diff. Two
   mailboxes are simultaneously compared to a record of the state of
   both mailboxes at last sync. New messages and message deletions are
   propagated between the two mailboxes. Mailsync can synchronize local
   mailbox files in many formats and remote mailboxes over IMAP, POP,
   and IMAPS.
     ________________________________________________________________

15.4. Data Transport Between Different Machines (Synchronization)

   I don't have experience with this topic yet. So just a survey about
   some means of data transport and maintaining data consistency between
   different machines.
     ________________________________________________________________

15.4.1. Useful Hardware

    1. external harddisks
    2. ZIP drive

   Wade Hampton wrote: "You may use MS-DOS formatted ZIP and floppy
   discs for data transfer. You may be able to also use LS120. If you
   have SCSI, you could use JAZ, MO or possibly DVD-RAM (any SCSI disc
   that you could write to). I have the internal ZIP for my Toshiba
   700CT. It works great (I use automount to mount it). I use VFAT on
   the ZIP disks so I can move them to Windows boxes, Linux boxes, NT,
   give them to coworkers, etc. One problem, I must SHUTDOWN to swap the
   internal CD with the ZIP."
     ________________________________________________________________

15.4.2. Useful Software

15.4.2.1. Version Management Software

   Although it is certainly not their main aim, version management
   software like CVS (Concurrent Version System) are a perfect tool when
   you work on several machines and you have trouble keeping them in
   sync (something which is often called "disconnected filesystems" in
   the computer science literature). Unlike programs like rsync, which
   are asymmetric (one side is the master and its files override those
   of the slave), CVS accept that you make changes on several machines,
   and try afterwards to merge them. Asymmetric tools are good only when
   you can respect a strict discipline, when you switch from one machine
   to another. On the contrary, tools like CVS are more forgetful.

   To synchronize two or more machines (typically a desktop and a
   laptop), just choose a CVS repository somewhere on the network. It
   can be on one of the machines you want to synchronize or on a third
   host. Anyway, this machine should be easily reachable via the network
   and have good disks.

   Then, cvs co the module you want to work on, edit it, and cvs commit
   when you reached a synch point and are connected. If you made changes
   on both hosts, CVS will try to merge them (it typically succeeds
   automatically) or give in and ask you to resolve it by hand.

   The typical limits of this solution: CVS does not deal well with
   binary files, so this solution is more for users of vi or emacs than
   for GIMP fans. CVS has trouble with some UNIX goodies like symbolic
   links.

   For more information on CVS, see the
   [http://www.loria.fr/~molli/cvs-index.html] Web page . The CVS
   documentation is excellent (in info format).
     ________________________________________________________________

15.4.2.2. CODA Filesystem

   The [http://www.coda.cs.cmu.edu/] CODA File System is a descendant of
   the Andrew File System. Like AFS, Coda offers location-transparent
   access to a shared UNIX file name-space that is mapped on to a
   collection of dedicated file servers. But Coda represents a
   substantial improvement over AFS because it offers considerably
   higher availability in the face of server and network failures. The
   improvement in availability is achieved using the complementary
   techniques of server replication and disconnected operation.
   Disconnected operation proven especially valuable in supporting
   portable computers .
     ________________________________________________________________

15.4.2.3. unison

   [http://www.cis.upenn.edu/~bcpierce/unison/] unison is a
   file-synchronization tool for Unix and Windows. It allows two
   replicas of a collection of files and directories to be stored on
   different hosts (or different disks on the same host), modified
   separately, and then brought up to date by propagating the changes in
   each replica to the other. Unison was written by researchers with an
   eye for well-defined replication semantics: they were very fussy
   about safety, and made sure to handle gracefully things like
   premature termination etc. Unison is symmetric/bidirectional (unlike
   rsync), works fine with binaries (unlike cvs), and is a user-level
   program (unlike most distributed filesystems). It also makes a
   reasonable attempt to synchronize transparently between Unix/Linux
   and Windows filesystems, which is no small feat. Drawbacks: it does
   not do version control, and does not handle synchronization among
   more than 2 file trees. unison shares a number of features with tools
   such as configuration management packages (CVS, PRCS, etc.)
   distributed filesystems ( [http://www.coda.cs.cmu.edu/] CODA , etc.)
   uni-directional mirroring utilities (rsync, etc.) and other
   synchronizers ( Intellisync, Reconcile, etc). However, there are a
   number of points where it differs:

     * unison runs on both MicroSoft-Windows (95, 98, NT, and 2k) and
       Unix (Solaris, Linux, etc.) systems ( for ARM based Linux PDAs
       see the [http://tuxmobil.org/feed.html] TuxMobil IPK feed .
       Moreover, unison works across platforms, allowing you to
       synchronize a Microsoft-Windows laptop with a Unix server, for
       example.
     * Unlike a distributed filesystem, unison is a user-level program:
       there is no need to hack (or own!) the kernel, or to have
       superuser privileges on either host.
     * Unlike simple mirroring or backup utilities, unison can deal with
       updates to both replicas of a distributed directory structure.
       Updates that do not conflict are propagated automatically.
       Conflicting updates are detected and displayed.
     * unison works between any pair of machines connected to the
       internet, communicating over either a direct socket link or
       tunneling over an rsh or an encrypted ssh connection. It is
       careful with network bandwidth, and runs well over slow links
       such as PPP connections.
     * unison has a clear and precise specification.
     * unison is resilient to failure. It is careful to leave the
       replicas and its own private structures in a sensible state at
       all times, even in case of abnormal termination or communication
       failures.
     * unison is free; full source code is available under the GNU
       Public License.
     ________________________________________________________________

15.4.2.4. OpenSync, MultiSync

   [http://www.opensync.org/] OpenSync is the successor of KitchenSync
   and MultiSync. OpenSync is a synchronization framework that is
   platform and distribution independent. It consists of a powerful
   sync-engine and several plugins that can be used to connect to
   devices. OpenSync is very flexible and capable of synchronizing any
   type of data, including contacts, calendar, tasks, notes and files.

   [http://multisync.sourceforge.net] MultiSync is a free modular
   program to synchronize calendars, address books, and other PIM data
   between programs on your computer and other computers, mobile
   devices, PDAs or cell phones. Currently MultiSync has plugins for
   Ximian Evolution calendars and IrMC Mobile Client calendars
   (supported by the Sony/Ericsson T68i) via Bluetooth, IrDA, or a cable
   connection.
     ________________________________________________________________

15.4.2.5. Funambol

   [http://www.funambol.com/opensource/] Funambol is an open source
   mobile application server software that provides push email, address
   book and calendar (PIM) data synchronization, application
   provisioning, and device management for wireless devices and PCs,
   leveraging standard protocols. For users, this means BlackBerry-like
   capabilities on commodity handsets. Funambol is also a software
   development platform for mobile applications. It provides client and
   server side Java APIs, and facilitates the development, deployment
   and management of any mobile project. Funambol is the de facto
   standard implementation of the Open Mobile Alliance Data
   Synchronization and Device Management protocols (OMA DS and DM,
   formerly known as SyncML). Funambol is replaces the former sync4J
   tools.
     ________________________________________________________________

15.4.2.6. Tsync

   [http://sourceforge.net/projects/tsyncd/] Tsync (Transparent)
   Synchronization is a user-level daemon that provides transparent
   synchronization amongst a set of computers. Tsync uses a peer-to-peer
   architecture for scalability, efficiency, and robustness.
     ________________________________________________________________

15.4.2.7. InterMezzo

   [http://inter-mezzo.org/] InterMezzo is a new distributed file system
   with a focus on high availability. InterMezzo is an Open Source
   project, currently on Linux (2.2 and 2.3). A primary target of
   development is to provide support for flexible replication of
   directories, with disconnected operation and a persistent cache. For
   example, we want to make it easy to manage copies of home directories
   on multiple computers, and solve the laptop/desktop synchronization
   problems. On a larger scale we aim to provide replication of large
   file repositories, for example to support high availability for
   servers. InterMezzo was deeply inspired by the Coda File System, but
   totally re-designed and re-engineered.
     ________________________________________________________________

15.4.2.8. WWWsync

   [http://www.alfie.demon.co.uk/wwwsync/] WWWsync/ is a program written
   in Perl that will update your web pages by ftp from your local pages.
   This was originally written for updating Demon home-pages, but will
   work with other providers which provide direct FTP access to your web
   pages. I didn't check this for laptop purposes yet.
     ________________________________________________________________

15.4.2.9. rsync

   rsync is a program that allows files to be copied to and from remote
   machines in much the same way as rcp. It has many more options than
   rcp, and uses the rsync remote-update protocol to greatly speedup
   file transfers when the destination file already exists. The rsync
   remote-update protocol allows rsync to transfer just the differences
   between two sets of files across the network link.
     ________________________________________________________________

15.4.2.10. Xfiles - file tree synchronization and cross-validation

   Xfiles is an interactive utility for comparing and merging one file
   tree with another over a network. It supports freeform work on
   several machines (no need to keep track of what files are changed on
   which machine). Xfiles can also be used as a cross-validating disk
   <-> disk backup strategy (portions of a disk may go bad at any time,
   with no simple indication of which files were affected.
   Cross-validate against a second disk before backup to make sure you
   aren't backing up bad data).

   A client/server program (GUI on the client) traverses a file tree and
   reports any files that are missing on the server machine, missing on
   the client machine, or different. For each such file, the file
   size/sizes and modification date(s) are shown, and a comparison
   (using UNIX diff) can be obtained. For files that are missing from
   one tree, similarly named files in that tree are reported.
   Inconsistent files can then be copied in either direction or deleted
   on either machine. The file trees do not need to be accessible via
   nfs. Files checksums are computed in parallel, so largely similar
   trees can be compared over a slow network link. The client and server
   processes can also be run on the same machine. File selection and
   interaction with a revision control system such as RCS can be handled
   by scripting using jpython. Requirements Java1.1 or later and
   JFC/Swing1.1 are needed. [http://www.idiom.com/~zilla] Xfiles.
     ________________________________________________________________

15.4.2.11. sitecopy

   Sitecopy is for copying locally stored websites to remote web
   servers. The program will upload files to the server which have
   changed locally, and delete files from the server which have been
   removed locally, to keep the remote site synchronized with the local
   site, with a single command. The aim is to remove the hassle of
   uploading and deleting individual files using an FTP client.
   [http://www.lyra.org/sitecopy] sitecopy.
     ________________________________________________________________

15.4.3. DataConversion: AddressBooks, BookMarks, Todo-Lists, LDAP, Webpages

   Transferring user data from one mobile device to another one, often
   requires some tools to extract the data from the source device before
   importing them into the target device, for example if you want to
   change your favorite mobile phone. Or if you want to use the
   addressbook from your mobile with your PDA, too. Here are some tools
   for [http://dataconv.org/apps_bookmarks.html] bookmark conversion,
   [http://dataconv.org/apps_addresses.html] addressbook migration,
   [http://dataconv.org/apps_vcard.html] vCard extraction,
   [http://dataconv.org/apps_ldap.html] LDAP merging and
   [http://dataconv.org/apps_pda.html] data conversion for PDAs and
   HandHeld PCs.
     ________________________________________________________________

15.5. Backup

   To me data on mobile computers are even more likely to be damaged or
   lost than on desktop computers. So backups are even more important.
   There are different solutions for backups in mobile environments. I
   will describe them in one of the next issues.

   For backups on removable media like CD-R/RW or DVD-R/RW you may boot
   from a Knoppix Live CD/DVD using the toram boot option. This way
   Knoppix will be completely loaded into RAM and you may remove the
   Knoppix CD/DVD from the drive to replace it with the backup media.
   Note: this will only work if your laptop provides more than 1GB RAM.
     ________________________________________________________________

15.6. Connections to Servers

   From Dirk Janssen <dirkj_AT_u.arizona.edu>: Here are several good
   ways of working on your laptop from your desktop machine. If you have
   a separate desktop machine at work, you might want to use that as a
   terminal server to your laptop. This means you get the larger screen
   and the better keyboard, without having to worry about syncing files.
   The easiest way to do this is to install ssh on both sides, and ssh
   from your desktop (running X) to the laptop. Ssh will provide a
   secure connection and, crucially, a secure X connection between the
   two machines. If you type, for example, emacs & in the ssh shell,
   emacs will start a window on your desktop machine while running on
   your laptop.

   There are various ways in which you can make this situation more
   productive/complicated. Emacs, for one thing, can open windows
   (called frames by emacs) on separate displays by using
   make-frame-on-display. This way, you can have the same emacs
   displaying on your desktop and your laptop: A dual headed system is
   born.

   For other programs, you usually have to decide at startup time on
   which screen you want them. To run them on the laptop screen, start
   them as usual. To run them on the desktop screen, start them from the
   ssh shell on the desktop or redirect their screens using the DISPLAY
   variable. Some programs also accept a -display option. Read the
   documentation on xauth on how to set this up. An easy way out is to
   find out which pseudo display ssh has created for you by typing echo
   $DISPLAY in the ssh shell. Assuming your desktop is called olli and
   your laptop stan, this will usually produce something like stan:10.
   This means that processes on stan (the laptop) display on what they
   think is the 10th screen of stan, which by some ssh magic is actually
   relayed (in a secure way) to the screen of olli.

   There are some ways in which you can dynamically move windows from
   one machine to another. A very interesting approach is taken by
   xmove, but this program lacks a good user interface (any
   volunteers?). Xmove creates a pseudo screen (similar to the stan:10
   that ssh creates) and windows that have their DISPLAY set to this
   pseudo screen can be moved back and forth between real screens
   (provided all screens use the same color depth).

   Alternatively, you can run an one of the several programs that open a
   virtual root window: A window on your desktop that contains other
   windows. It looks a lot like running an emulator. With these
   programs, you can start your processes on stan, then move all their
   windows to olli, then work for a while, and then move them back so
   you can continue working on stan. Hibernate your laptop and repeat ad
   infinitum. Check out xmx and VNC for this.

   If this is all too complicated for you, but you like to use the two
   screens at the same time, consider at least installing x2x. This
   little tool makes it possible to move your mouse from one screen to
   the other, and the keyboard focus goes with it. To run it, you need
   another ssh going from stan (the laptop) to olli (the desktop): ie.
   type ssh olli in a stan xterm. Keep this shell running and find out
   which pseudo screen was created with echo $DISPLAY. This will return
   something like olli:10 (see above for explanation). Now, type this in
   any shell on olli: x2x -west -to olli:10 (and I mean, in a shell that
   runs on olli and displays on olli, not an ssh shell) This creates a
   little black band to on the left (west) side of your desktop's
   screen. Whenever you move the mouse over this, the mouse on screen
   olli:10 will move. Because olli:10 is just an ssh-created alias for
   the screen of stan, the mouse on your laptop will move and you can
   type there by only moving your head, not your hands.

   A note on X-security: Playing around with various screen programs is
   much easier if you issue an xhost + on either computer. But this is
   extremely unsafe. Do this only when you are not connected to any
   larger network. If you have everything working, spend some time on
   getting xauth to work. If you use xdm, it is usually easy. Otherwise,
   consider starting your Xserver with the same magic cookie all the
   time. This is less safe, but still pretty safe, and it means that you
   have to copy the cookies only once. Check the startup scripts
   (.xserverrc, .xinitrc, .xsession, etc) for something like
   cookie="MIT-MAGIC-COOKIE-1 `keygen`" and change that into (invent
   your own cookie here): cookie="MIT-MAGIC-COOKIE-1
   12345678901234567890abcdefabcdef"
     ________________________________________________________________

15.7. Security in Different Environments

15.7.1. Introduction

   I am not a computer security expert, but I think that security
   associated with mobile devices requires specific attention. Please
   read the [http://www.linuxsecurity.com/Security-HOWTO] Security-HOWTO
   by Kevin Fenzi and Dave Wreski for more information. I just collected
   some information below. Note, these means are just small steps to
   additional security, though I recommend that you use them.

   Please read also the [https://www.seifried.org/lasg/] Linux
   Administrator's Security Guide (LASG) - FAQ by Kurt Seifried.
     ________________________________________________________________

15.7.2. Means of Security

    1. Antivirus policy: For Linux there are some anti virus programs
       available. Check the BIOS for an option to disable writing at the
       boot sector.
    2. Laptop as a security risk itself: Since a laptop can easily be
       used to intrude a network, it seems a good policy to ask the
       system administrator for permission before connecting a laptop to
       a network.
    3. Secure Protocol: When connecting to a remote server always use a
       secure protocol (for instance ssh) or tunneling tunnelv , pptp
       and APOP for POP accounts.
     ________________________________________________________________

15.8. Theft Protection

15.8.1. Means to Protect the Data

    1. Encryption: the Linux Kernel offers different options. This
       [http://shappyhopper.co.uk/b2154/sharedencryptedhowto.cgi]
       Encrypted dual boot single hard drive system HOWTO, explains how
       to secure your system using nothing but Free Software. It was
       primarily written for people with a dual boot laptop, describing
       free tools to encrypt Microsoft Windows as well as Linux
       partitions.
    2. Here are some [http://tuxmobil.org/smart_linux.html] Linux guides
       for laptops with built-in SmartCard-Reader.
    3. User passwords: can be easily bypassed if the intruder gets
       physical access to your machine.
    4. Hard Disk Passwords:
    5. BIOS passwords: are easily crackable at least with older laptop
       models. Some manufacturers have now a second boot password (IBM).
       If you use a BIOS password/boot loader security, ADVERTISE IT!
       Paste a sticker (or tape a piece of paper) on the top of your
       laptop, saying something like:

                           WARNING

This laptop is password protected. The password can only be removed
by an authorized [manufacturer's name] technician presented with
proof of ownership. So don't even think of stealing it, because
it won't do you any good.

    6. Before you buy a second hand machine, check whether the machine
       seems to be stolen. I have provided a survey of
       [http://tuxmobil.org/stolen_laptops.html] databases for stolen
       laptops.
     ________________________________________________________________

15.8.2. Means to Protect the Hardware

    1. Laptop lock: Almost all (if not all) of the new laptops come with
       a slot for the lock, and if yours doesn't have one, most locks
       come with a kit to add a slot. One of Targus' Defcon locks even
       has a motion sensor, so you don't have to lock it up to a secure
