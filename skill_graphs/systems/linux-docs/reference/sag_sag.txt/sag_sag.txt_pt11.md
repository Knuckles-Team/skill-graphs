While crack can be run by intruders, it can also be run by the system
administrator to avoid bad passwords. Good passwords can also be enforced by
the passwd program; this is in fact more effective in CPU cycles, since
cracking passwords requires quite a lot of computation.

The user group database is kept in /etc/group; for systems with shadow
passwords, there can be a /etc/shadow.group.

root usually can't login via most terminals or the network, only via
terminals listed in the /etc/securetty file. This makes it necessary to get
physical access to one of these terminals. It is, however, possible to log in
via any terminal as any other user, and use the su command to become root.
-----------------------------------------------------------------------------

10.6. Shell startup

When an interactive login shell starts, it automatically executes one or more
pre-defined files. Different shells execute different files; see the
documentation of each shell for further information.

Most shells first run some global file, for example, the Bourne shell (/bin/
sh) and its derivatives execute /etc/profile; in addition, they execute
.profile in the user's home directory. /etc/profile allows the system
administrator to have set up a common user environment, especially by setting
the PATH to include local command directories in addition to the normal ones.
On the other hand, .profile allows the user to customize the environment to
his own tastes by overriding, if necessary, the default environment.
-----------------------------------------------------------------------------

Chapter 11. Managing user accounts

    "The similarities of sysadmins and drug dealers: both measure stuff in
    Ks, and both have users." (Old, tired computer joke.)

This chapter explains how to create new user accounts, how to modify the
properties of those accounts, and how to remove the accounts. Different Linux
systems have different tools for doing this.
-----------------------------------------------------------------------------

11.1. What's an account?

When a computer is used by many people it is usually necessary to
differentiate between the users, for example, so that their private files can
be kept private. This is important even if the computer can only be used by a
single person at a time, as with most microcomputers. Thus, each user is
given a unique username, and that name is used to log in.

There's more to a user than just a name, however. An account is all the
files, resources, and information belonging to one user. The term hints at
banks, and in a commercial system each account usually has some money
attached to it, and that money vanishes at different speeds depending on how
much the user stresses the system. For example, disk space might have a price
per megabyte and day, and processing time might have a price per second.
-----------------------------------------------------------------------------

11.2. Creating a user

The Linux kernel itself treats users are mere numbers. Each user is
identified by a unique integer, the user id or uid, because numbers are
faster and easier for a computer to process than textual names. A separate
database outside the kernel assigns a textual name, the username, to each
user id. The database contains additional information as well.

To create a user, you need to add information about the user to the user
database, and create a home directory for him. It may also be necessary to
educate the user, and set up a suitable initial environment for him.

Most Linux distributions come with a program for creating accounts. There are
several such programs available. Two command line alternatives are adduser
and useradd; there may be a GUI tool as well. Whatever the program, the
result is that there is little if any manual work to be done. Even if the
details are many and intricate, these programs make everything seem trivial.
However, Section 11.2.4 describes how to do it by hand.
-----------------------------------------------------------------------------

11.2.1. /etc/passwd and other informative files

The basic user database in a Unix system is the text file, /etc/passwd
(called the password file), which lists all valid usernames and their
associated information. The file has one line per username, and is divided
into seven colon-delimited fields:

��*�Username.

��*�Previously this was where the user's password was stored.

��*�Numeric user id.

��*�Numeric group id.

��*�Full name or other description of account.

��*�Home directory.

��*�Login shell (program to run at login).


The format is explained in more detail on the passwd manual page.

Most Linux systems use shadow passwords. As mentioned, previously passwords
were stored in the /etc/passwd file. This newer method of storing the
password: the encrypted password is stored in a separate file, /etc/shadow,
which only root can read. The /etc/passwd file only contains a special marker
in the second field. Any program that needs to verify a user is setuid, and
can therefore access the shadow password file. Normal programs, which only
use the other fields in the password file, can't get at the password.
-----------------------------------------------------------------------------

11.2.2. Picking numeric user and group ids

On most systems it doesn't matter what the numeric user and group ids are,
but if you use the Network filesystem (NFS), you need to have the same uid
and gid on all systems. This is because NFS also identifies users with the
numeric uids. If you aren't using NFS, you can let your account creation tool
pick them automatically.

If you are using NFS, you'll have to be invent a mechanism for synchronizing
account information. One alternative is to the NIS system (see XXX
network-admin-guide).

However, you should try to avoid reusing numeric uids (and textual
usernames), because the new owner of the uid (or username) may get access to
the old owner's files (or mail, or whatever).
-----------------------------------------------------------------------------

11.2.3. Initial environment: /etc/skel

When the home directory for a new user is created, it is initialized with
files from the /etc/skel directory. The system administrator can create files
in /etc/skel that will provide a nice default environment for users. For
example, he might create a /etc/skel/.profile that sets the EDITOR
environment variable to some editor that is friendly towards new users.

However, it is usually best to try to keep /etc/skel as small as possible,
since it will be next to impossible to update existing users' files. For
example, if the name of the friendly editor changes, all existing users would
have to edit their .profile. The system administrator could try to do it
automatically, with a script, but that is almost certain going to break
someone's file.

Whenever possible, it is better to put global configuration into global
files, such as /etc/profile. This way it is possible to update it without
breaking users' own setups.
-----------------------------------------------------------------------------

11.2.4. Creating a user by hand

To create a new account manually, follow these steps:

��*�Edit /etc/passwd with vipw and add a new line for the new account. Be
    careful with the syntax. Do not edit directly with an editor! vipw locks
    the file, so that other commands won't try to update it at the same time.
    You should make the password field be `*', so that it is impossible to
    log in.

��*�Similarly, edit /etc/group with vigr, if you need to create a new group
    as well.

��*�Create the home directory of the user with mkdir.

��*�Copy the files from /etc/skel to the new home directory.

��*�Fix ownerships and permissions with chown and chmod. The -R option is
    most useful. The correct permissions vary a little from one site to
    another, but usually the following commands do the right thing:
    +---------------------------------------------------------------+
    |cd /home/newusername                                           |
    |chown -R username.group .                                      |
    |chmod -R go=u,go-w .                                           |
    |chmod go= .                                                    |
    +---------------------------------------------------------------+

��*�Set the password with passwd.


After you set the password in the last step, the account will work. You
shouldn't set it until everything else has been done, otherwise the user may
inadvertently log in while you're still copying the files.

It is sometimes necessary to create dummy accounts that are not used by
people. For example, to set up an anonymous FTP server (so that anyone can
download files from it, without having to get an account first), you need to
create an account called ftp. In such cases, it is usually not necessary to
set the password (last step above). Indeed, it is better not to, so that
no-one can use the account, unless they first become root, since root can
become any user.
-----------------------------------------------------------------------------

11.3. Changing user properties

There are a few commands for changing various properties of an account (i.e.,
the relevant field in /etc/passwd):

chfn
    Change the full name field.

chsh
    Change the login shell.

passwd
    Change the password.


The super-user may use these commands to change the properties of any
account. Normal users can only change the properties of their own account. It
may sometimes be necessary to disable these commands (with chmod) for normal
users, for example in an environment with many novice users.

Other tasks need to be done by hand. For example, to change the username, you
need to edit /etc/passwd directly (with vipw, remember). Likewise, to add or
remove the user to more groups, you need to edit /etc/group (with vigr). Such
tasks tend to be rare, however, and should be done with caution: for example,
if you change the username, e-mail will no longer reach the user, unless you
also create a mail alias.
-----------------------------------------------------------------------------

11.4. Removing a user

To remove a user, you first remove all his files, mailboxes, mail aliases,
print jobs, cron and at jobs, and all other references to the user. Then you
remove the relevant lines from /etc/passwd and /etc/group (remember to remove
the username from all groups it's been added to). It may be a good idea to
first disable the account (see below), before you start removing stuff, to
prevent the user from using the account while it is being removed.

Remember that users may have files outside their home directory. The find
command can find them:
+---------------------------------------------------------------------------+
|find / -user username                                                      |
+---------------------------------------------------------------------------+
However, note that the above command will take a long time, if you have large
disks. If you mount network disks, you need to be careful so that you won't
trash the network or the server.

Some Linux distributions come with special commands to do this; look for
deluser or userdel. However, it is easy to do it by hand as well, and the
commands might not do everything.
-----------------------------------------------------------------------------

11.5. Disabling a user temporarily

It is sometimes necessary to temporarily disable an account, without removing
it. For example, the user might not have paid his fees, or the system
administrator may suspect that a cracker has got the password of that
account.

The best way to disable an account is to change its shell into a special
program that just prints a message. This way, whoever tries to log into the
account, will fail, and will know why. The message can tell the user to
contact the system administrator so that any problems may be dealt with.

It would also be possible to change the username or password to something
else, but then the user won't know what is going on. Confused users mean more
work.

A simple way to create the special programs is to write `tail scripts':
+---------------------------------------------------------------------------+
|#!/usr/bin/tail +2                                                         |
|This account has been closed due to a security breach.                     |
|Please call 555-1234 and wait for the men in black to arrive.              |
+---------------------------------------------------------------------------+
The first two characters (`#!') tell the kernel that the rest of the line is
a command that needs to be run to interpret this file. The tail command in
this case outputs everything except the first line to the standard output.

If user billg is suspected of a security breach, the system administrator
would do something like this:
+---------------------------------------------------------------------------+
|# chsh -s                                                                  |
|/usr/local/lib/no-login/security billg                                     |
|# su - tester                                                              |
|This account has been closed due to a security breach.                     |
|Please call 555-1234 and wait for the men in black to arrive.              |
|#                                                                          |
+---------------------------------------------------------------------------+
The purpose of the su is to test that the change worked, of course.

Tail scripts should be kept in a separate directory, so that their names
don't interfere with normal user commands.
-----------------------------------------------------------------------------

Chapter 12. Backups

    Hardware�is�indeterministically�reliable.�
    Software�is�deterministically�unreliable.
    People�are�indeterministically�unreliable.
    Nature�is�deterministically�reliable.

This chapter explains about why, how, and when to make backups, and how to
restore things from backups.
-----------------------------------------------------------------------------

12.1. On the importance of being backed up

Your data is valuable. It will cost you time and effort re-create it, and
that costs money or at least personal grief and tears; sometimes it can't
even be re-created, e.g., if it is the results of some experiments. Since it
is an investment, you should protect it and take steps to avoid losing it.

There are basically four reasons why you might lose data: hardware failures,
software bugs, human action, or natural disasters. Although modern hardware
tends to be quite reliable, it can still break seemingly spontaneously. The
most critical piece of hardware for storing data is the hard disk, which
relies on tiny magnetic fields remaining intact in a world filled with
electromagnetic noise. Modern software doesn't even tend to be reliable; a
rock solid program is an exception, not a rule. Humans are quite unreliable,
they will either make a mistake, or they will be malicious and destroy data
on purpose. Nature might not be evil, but it can wreak havoc even when being
good. All in all, it is a small miracle that anything works at all.

Backups are a way to protect the investment in data. By having several copies
of the data, it does not matter as much if one is destroyed (the cost is only
that of the restoration of the lost data from the backup).

It is important to do backups properly. Like everything else that is related
to the physical world, backups will fail sooner or later. Part of doing
backups well is to make sure they work; you don't want to notice that your
backups didn't work. Adding insult to injury, you might have a bad crash just
as you're making the backup; if you have only one backup medium, it might
destroyed as well, leaving you with the smoking ashes of hard work. Or you
might notice, when trying to restore, that you forgot to back up something
important, like the user database on a 15000 user site. Best of all, all your
backups might be working perfectly, but the last known tape drive reading the
kind of tapes you used was the one that now has a bucketful of water in it.

When it comes to backups, paranoia is in the job description.
-----------------------------------------------------------------------------

12.2. Selecting the backup medium

The most important decision regarding backups is the choice of backup medium.
You need to consider cost, reliability, speed, availability, and usability.

Cost is important, since you should preferably have several times more backup
storage than what you need for the data. A cheap medium is usually a must.

Reliability is extremely important, since a broken backup can make a grown
man cry. A backup medium must be able to hold data without corruption for
years. The way you use the medium affects it reliability as a backup medium.
A hard disk is typically very reliable, but as a backup medium it is not very
reliable, if it is in the same computer as the disk you are backing up.

Speed is usually not very important, if backups can be done without
interaction. It doesn't matter if a backup takes two hours, as long as it
needs no supervision. On the other hand, if the backup can't be done when the
computer would otherwise be idle, then speed is an issue.

Availability is obviously necessary, since you can't use a backup medium if
it doesn't exist. Less obvious is the need for the medium to be available
even in the future, and on computers other than your own. Otherwise you may
not be able to restore your backups after a disaster.

Usability is a large factor in how often backups are made. The easier it is
to make backups, the better. A backup medium mustn't be hard or boring to
use.

The typical alternatives are floppies and tapes. Floppies are very cheap,
fairly reliable, not very fast, very available, but not very usable for large
amounts of data. Tapes are cheap to somewhat expensive, fairly reliable,
fairly fast, quite available, and, depending on the size of the tape, quite
comfortable.

There are other alternatives. They are usually not very good on availability,
but if that is not a problem, they can be better in other ways. For example,
magneto-optical disks can have good sides of both floppies (they're random
access, making restoration of a single file quick) and tapes (contain a lot
of data).
-----------------------------------------------------------------------------

12.3. Selecting the backup tool

There are many tools that can be used to make backups. The traditional UNIX
tools used for backups are tar, cpio, and dump. In addition, there are large
number of third party packages (both freeware and commercial) that can be
used. The choice of backup medium can affect the choice of tool.

tar and cpio are similar, and mostly equivalent from a backup point of view.
Both are capable of storing files on tapes, and retrieving files from them.
Both are capable of using almost any media, since the kernel device drivers
take care of the low level device handling and the devices all tend to look
alike to user level programs. Some UNIX versions of tar and cpio may have
problems with unusual files (symbolic links, device files, files with very
long pathnames, and so on), but the Linux versions should handle all files
correctly.

dump is different in that it reads the filesystem directly and not via the
filesystem. It is also written specifically for backups; tar and cpio are
really for archiving files, although they work for backups as well.

Reading the filesystem directly has some advantages. It makes it possible to
back files up without affecting their time stamps; for tar and cpio, you
would have to mount the filesystem read-only first. Directly reading the
filesystem is also more effective, if everything needs to be backed up, since
it can be done with much less disk head movement. The major disadvantage is
that it makes the backup program specific to one filesystem type; the Linux
dump program understands the ext2 filesystem only.

dump also directly supports backup levels (which we'll be discussing below);
with tar and cpio this has to be implemented with other tools.

A comparison of the third party backup tools is beyond the scope of this
book. The Linux Software Map lists many of the freeware ones.
-----------------------------------------------------------------------------

12.4. Simple backups

A simple backup scheme is to back up everything once, then back up everything
that has been modified since the previous backup. The first backup is called
a full backup, the subsequent ones are incremental backups. A full backup is
often more laborious than incremental ones, since there is more data to write
to the tape and a full backup might not fit onto one tape (or floppy).
Restoring from incremental backups can be many times more work than from a
full one. Restoration can be optimized so that you always back up everything
since the previous full backup; this way, backups are a bit more work, but
there should never be a need to restore more than a full backup and an
incremental backup.

If you want to make backups every day and have six tapes, you could use tape
1 for the first full backup (say, on a Friday), and tapes 2 to 5 for the
incremental backups (Monday through Thursday). Then you make a new full
backup on tape 6 (second Friday), and start doing incremental ones with tapes
2 to 5 again. You don't want to overwrite tape 1 until you've got a new full
backup, lest something happens while you're making the full backup. After
you've made a full backup to tape 6, you want to keep tape 1 somewhere else,
so that when your other backup tapes are destroyed in the fire, you still
have at least something left. When you need to make the next full backup, you
fetch tape 1 and leave tape 6 in its place.

If you have more than six tapes, you can use the extra ones for full backups.
Each time you make a full backup, you use the oldest tape. This way you can
have full backups from several previous weeks, which is good if you want to
find an old, now deleted file, or an old version of a file.
-----------------------------------------------------------------------------

12.4.1. Making backups with tar

A full backup can easily be made with tar:
+---------------------------------------------------------------------------+
|# tar --create --file /dev/ftape                                           |
|/usr/src                                                                   |
|tar: Removing leading / from absolute path names in                        |
|the archive                                                                |
|#                                                                          |
+---------------------------------------------------------------------------+
The example above uses the GNU version of tar and its long option names. The
traditional version of tar only understands single character options. The GNU
version can also handle backups that don't fit on one tape or floppy, and
also very long paths; not all traditional versions can do these things.
(Linux only uses GNU tar.)

If your backup doesn't fit on one tape, you need to use the --multi-volume
(-M) option:
+---------------------------------------------------------------------------+
|# tar -cMf /dev/fd0H1440                                                   |
|/usr/src                                                                   |
|tar: Removing leading / from absolute path names in                        |
|the archive                                                                |
|Prepare volume #2 for /dev/fd0H1440 and hit return:                        |
|#                                                                          |
+---------------------------------------------------------------------------+
Note that you should format the floppies before you begin the backup, or else
use another window or virtual terminal and do it when tar asks for a new
floppy.

After you've made a backup, you should check that it is OK, using the
--compare (-d) option:
+---------------------------------------------------------------------------+
|# tar --compare --verbose -f                                               |
|/dev/ftape                                                                 |
|usr/src/                                                                   |
|usr/src/linux                                                              |
|usr/src/linux-1.2.10-includes/                                             |
|....                                                                       |
|#                                                                          |
+---------------------------------------------------------------------------+
Failing to check a backup means that you will not notice that your backups
aren't working until after you've lost the original data.

An incremental backup can be done with tar using the --newer (-N) option:
+---------------------------------------------------------------------------+
|# tar --create --newer '8 Sep 1995'                                        |
|--file /dev/ftape /usr/src                                                 |
|--verbose                                                                  |
