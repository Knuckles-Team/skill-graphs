|tar: Removing leading / from absolute path names in                        |
|the archive                                                                |
|usr/src/                                                                   |
|usr/src/linux-1.2.10-includes/                                             |
|usr/src/linux-1.2.10-includes/include/                                     |
|usr/src/linux-1.2.10-includes/include/linux/                               |
|usr/src/linux-1.2.10-includes/include/linux/modules/                       |
|usr/src/linux-1.2.10-includes/include/asm-generic/                         |
|usr/src/linux-1.2.10-includes/include/asm-i386/                            |
|usr/src/linux-1.2.10-includes/include/asm-mips/                            |
|usr/src/linux-1.2.10-includes/include/asm-alpha/                           |
|usr/src/linux-1.2.10-includes/include/asm-m68k/                            |
|usr/src/linux-1.2.10-includes/include/asm-sparc/                           |
|usr/src/patch-1.2.11.gz                                                    |
|#                                                                          |
+---------------------------------------------------------------------------+
Unfortunately, tar can't notice when a file's inode information has changed,
for example, that its permission bits have been changed, or when its name has
been changed. This can be worked around using find and comparing current
filesystem state with lists of files that have been previously backed up.
Scripts and programs for doing this can be found on Linux ftp sites.
-----------------------------------------------------------------------------

12.4.2. Restoring files with tar

The --extract (-x) option for tar extracts files:
+---------------------------------------------------------------------------+
|# tar --extract --same-permissions                                         |
|--verbose --file                                                           |
|/dev/fd0H1440                                                              |
|usr/src/                                                                   |
|usr/src/linux                                                              |
|usr/src/linux-1.2.10-includes/                                             |
|usr/src/linux-1.2.10-includes/include/                                     |
|usr/src/linux-1.2.10-includes/include/linux/                               |
|usr/src/linux-1.2.10-includes/include/linux/hdreg.h                        |
|usr/src/linux-1.2.10-includes/include/linux/kernel.h                       |
|...                                                                        |
|#                                                                          |
+---------------------------------------------------------------------------+
You also extract only specific files or directories (which includes all their
files and subdirectories) by naming on the command line:
+---------------------------------------------------------------------------+
|# tar xpvf /dev/fd0H1440                                                   |
|usr/src/linux-1.2.10-includes/include/linux/hdreg.h                        |
|usr/src/linux-1.2.10-includes/include/linux/hdreg.h                        |
|#                                                                          |
+---------------------------------------------------------------------------+
Use the --list (-t) option, if you just want to see what files are on a
backup volume:
+---------------------------------------------------------------------------+
|# tar --list --file                                                        |
|/dev/fd0H1440                                                              |
|usr/src/                                                                   |
|usr/src/linux                                                              |
|usr/src/linux-1.2.10-includes/                                             |
|usr/src/linux-1.2.10-includes/include/                                     |
|usr/src/linux-1.2.10-includes/include/linux/                               |
|usr/src/linux-1.2.10-includes/include/linux/hdreg.h                        |
|usr/src/linux-1.2.10-includes/include/linux/kernel.h                       |
|...                                                                        |
|#                                                                          |
+---------------------------------------------------------------------------+
Note that tar always reads the backup volume sequentially, so for large
volumes it is rather slow. It is not possible, however, to use random access
database techniques when using a tape drive or some other sequential medium.

tar doesn't handle deleted files properly. If you need to restore a
filesystem from a full and an incremental backup, and you have deleted a file
between the two backups, it will exist again after you have done the restore.
This can be a big problem, if the file has sensitive data that should no
longer be available.
-----------------------------------------------------------------------------

12.5. Multilevel backups

The simple backup method outlined in the previous section is often quite
adequate for personal use or small sites. For more heavy duty use, multilevel
backups are more appropriate.

The simple method has two backup levels: full and incremental backups. This
can be generalized to any number of levels. A full backup would be level 0,
and the different levels of incremental backups levels 1, 2, 3, etc. At each
incremental backup level you back up everything that has changed since the
previous backup at the same or a previous level.

The purpose for doing this is that it allows a longer backup history cheaply.
In the example in the previous section, the backup history went back to the
previous full backup. This could be extended by having more tapes, but only a
week per new tape, which might be too expensive. A longer backup history is
useful, since deleted or corrupted files are often not noticed for a long
time. Even a version of a file that is not very up to date is better than no
file at all.

With multiple levels the backup history can be extended more cheaply. For
example, if we buy ten tapes, we could use tapes 1 and 2 for monthly backups
(first Friday each month), tapes 3 to 6 for weekly backups (other Fridays;
note that there can be five Fridays in one month, so we need four more
tapes), and tapes 7 to 10 for daily backups (Monday to Thursday). With only
four more tapes, we've been able to extend the backup history from two weeks
(after all daily tapes have been used) to two months. It is true that we
can't restore every version of each file during those two months, but what we
can restore is often good enough.

Figure 12-1 shows which backup level is used each day, and which backups can
be restored from at the end of the month.


Figure 12-1. A sample multilevel backup schedule.

[backup-timeline]

Backup levels can also be used to keep filesystem restoration time to a
minimum. If you have many incremental backups with monotonously growing level
numbers, you need to restore all of them if you need to rebuild the whole
filesystem. Instead you can use level numbers that aren't monotonous, and
keep down the number of backups to restore.

To minimize the number of tapes needed to restore, you could use a smaller
level for each incremental tape. However, then the time to make the backups
increases (each backup copies everything since the previous full backup). A
better scheme is suggested by the dump manual page and described by the table
XX (efficient-backup-levels). Use the following succession of backup levels:
3, 2, 5, 4, 7, 6, 9, 8, 9, etc. This keeps both the backup and restore times
low. The most you have to backup is two day's worth of work. The number of
tapes for a restore depends on how long you keep between full backups, but it
is less than in the simple schemes.


Table 12-1. Efficient backup scheme using many backup levels
+----+-----+--------------+---------------------------+
|Tape|Level|Backup (days) |Restore tapes              |
+----+-----+--------------+---------------------------+
|1   |0    |n/a           |1                          |
+----+-----+--------------+---------------------------+
|2   |3    |1             |1, 2                       |
+----+-----+--------------+---------------------------+
|3   |2    |2             |1, 3                       |
+----+-----+--------------+---------------------------+
|4   |5    |1             |1, 2, 4                    |
+----+-----+--------------+---------------------------+
|5   |4    |2             |1, 2, 5                    |
+----+-----+--------------+---------------------------+
|6   |7    |1             |1, 2, 5, 6                 |
+----+-----+--------------+---------------------------+
|7   |6    |2             |1, 2, 5, 7                 |
+----+-----+--------------+---------------------------+
|8   |9    |1             |1, 2, 5, 7, 8              |
+----+-----+--------------+---------------------------+
|9   |8    |2             |1, 2, 5, 7, 9              |
+----+-----+--------------+---------------------------+
|10  |9    |1             |1, 2, 5, 7, 9, 10          |
+----+-----+--------------+---------------------------+
|11  |9    |1             |1, 2, 5, 7, 9, 10, 11      |
+----+-----+--------------+---------------------------+
|... |9    |1             |1, 2, 5, 7, 9, 10, 11, ... |
+----+-----+--------------+---------------------------+

A fancy scheme can reduce the amount of labor needed, but it does mean there
are more things to keep track of. You must decide if it is worth it.

dump has built-in support for backup levels. For tar and cpio it must be
implemented with shell scripts.
-----------------------------------------------------------------------------

12.6. What to back up

You want to back up as much as possible. The major exception is software that
can be easily reinstalled, but even they may have configuration files that it
is important to back up, lest you need to do all the work to configure them
all over again. Another major exception is the /proc filesystem; since that
only contains data that the kernel always generates automatically, it is
never a good idea to back it up. Especially the /proc/kcore file is
unnecessary, since it is just an image of your current physical memory; it's
pretty large as well.

Gray areas include the news spool, log files, and many other things in /var.
You must decide what you consider important.

The obvious things to back up are user files (/home) and system configuration
files (/etc, but possibly other things scattered all over the filesystem).
-----------------------------------------------------------------------------

12.7. Compressed backups

Backups take a lot of space, which can cost quite a lot of money. To reduce
the space needed, the backups can be compressed. There are several ways of
doing this. Some programs have support for for compression built in; for
example, the --gzip (-z) option for GNU tar pipes the whole backup through
the gzip compression program, before writing it to the backup medium.

Unfortunately, compressed backups can cause trouble. Due to the nature of how
compression works, if a single bit is wrong, all the rest of the compressed
data will be unusable. Some backup programs have some built in error
correction, but no method can handle a large number of errors. This means
that if the backup is compressed the way GNU tar does it, with the whole
output compressed as a unit, a single error makes all the rest of the backup
lost. Backups must be reliable, and this method of compression is not a good
idea.

An alternative way is to compress each file separately. This still means that
the one file is lost, but all other files are unharmed. The lost file would
have been corrupted anyway, so this situation is not much worse than not
using compression at all. The afio program (a variant of cpio) can do this.

Compression takes some time, which may make the backup program unable to
write data fast enough for a tape drive. This can be avoided by buffering the
output (either internally, if the backup program if smart enough, or by using
another program), but even that might not work well enough. This should only
be a problem on slow computers.
-----------------------------------------------------------------------------

Chapter 13. Task Automation --To Be Added

    "Never put off until tomorrow what you can do the day after tomorrow.
    'Mark Twain'"


        Basic discussion on scripting, cron & at - refer to other HOWTO's for
        details. Discuss non-crontab cron jobs such at those in the /etc
        directory.


-----------------------------------------------------------------------------
Chapter 14. Keeping Time

    "Time is an illusion. Lunchtime double so." (Douglas Adams.)

This chapter explains how a Linux system keeps time, and what you need to do
to avoid causing trouble. Usually, you don't need to do anything about time,
but it is good to understand it.
-----------------------------------------------------------------------------

14.1. The concept of localtime

Time measurement is based on mostly regular natural phenomena, such as
alternating light and dark periods caused by the rotation of the planet. The
total time taken by two successive periods is constant, but the lengths of
the light and dark period vary. One simple constant is noon.

Noon is the time of the day when the Sun is at its highest position. Since
(according to recent research) the Earth is round, noon happens at different
times in different places. This leads to the concept of local time. Humans
measure time in many units, most of which are tied to natural phenomena like
noon. As long as you stay in the same place, it doesn't matter that local
times differ.

As soon as you need to communicate with distant places, you'll notice the
need for a common time. In modern times, most of the places in the world
communicate with most other places in the world, so a global standard for
measuring time has been defined. This time is called universal time (UT or
UTC, formerly known as Greenwich Mean Time or GMT, since it used to be local
time in Greenwich, England). When people with different local times need to
communicate, they can express times in universal time, so that there is no
confusion about when things should happen.

Each local time is called a time zone. While geography would allow all places
that have noon at the same time have the same time zone, politics makes it
difficult. For various reasons, many countries use daylight savings time,
that is, they move their clocks to have more natural light while they work,
and then move the clocks back during winter. Other countries do not do this.
Those that do, do not agree when the clocks should be moved, and they change
the rules from year to year. This makes time zone conversions definitely
non-trivial.

Time zones are best named by the location or by telling the difference
between local and universal time. In the US and some other countries, the
local time zones have a name and a three letter abbreviation. The
abbreviations are not unique, however, and should not be used unless the
country is also named. It is better to talk about the local time in, say,
Helsinki, than about East European time, since not all countries in Eastern
Europe follow the same rules.

Linux has a time zone package that knows about all existing time zones, and
that can easily be updated when the rules change. All the system
administrator needs to do is to select the appropriate time zone. Also, each
user can set his own time zone; this is important since many people work with
computers in different countries over the Internet. When the rules for
daylight savings time change in your local time zone, make sure you'll
upgrade at least that part of your Linux system. Other than setting the
system time zone and upgrading the time zone data files, there is little need
to bother about time.
-----------------------------------------------------------------------------

14.2. The hardware and software clocks

A personal computer has a battery driven hardware clock. The battery ensures
that the clock will work even if the rest of the computer is without
electricity. The hardware clock can be set from the BIOS setup screen or from
whatever operating system is running.

The Linux kernel keeps track of time independently from the hardware clock.
During the boot, Linux sets its own clock to the same time as the hardware
clock. After this, both clocks run independently. Linux maintains its own
clock because looking at the hardware is slow and complicated.

The kernel clock always shows universal time. This way, the kernel does not
need to know about time zones at all. The simplicity results in higher
reliability and makes it easier to update the time zone information. Each
process handles time zone conversions itself (using standard tools that are
part of the time zone package).

The hardware clock can be in local time or in universal time. It is usually
better to have it in universal time, because then you don't need to change
the hardware clock when daylight savings time begins or ends (UTC does not
have DST). Unfortunately, some PC operating systems, including MS-DOS,
Windows, and OS/2, assume the hardware clock shows local time. Linux can
handle either, but if the hardware clock shows local time, then it must be
modified when daylight savings time begins or ends (otherwise it wouldn't
show local time).
-----------------------------------------------------------------------------

14.3. Showing and setting time

In Linux, the system time zone is determined by the symbolic link /etc/
localtime. This link points to a time zone data file that describes the local
time zone. The time zone data files are located at either /usr/lib/zoneinfo
or /usr/share/zoneinfo depending on what distribution of Linux you use.

For example, on a SuSE system located in New Jersey the /etc/localtime link
would point to /usr/share/zoneinfo/US/Eastern. On a Debian system the /etc/
localtime link would point to /usr/lib/zoneinfo/US/Eastern.

If you fail to find the zoneinfo directory in either the /usr/lib or /usr/
share directories, either do a find /usr -print | grep zoneinfo or consult
your distribution's documentation.

What happens when you have a users located in a different timezone? A user
can change his private time zone by setting the TZ environment variable. If
it is unset, the system time zone is assumed. The syntax of the TZ variable
is described in the tzset manual page.

The date command shows the current date and time. For example:
+---------------------------------------------------------------------------+
|$ date                                                                     |
|Sun Jul 14 21:53:41 EET DST 1996                                           |
|$                                                                          |
+---------------------------------------------------------------------------+
That time is Sunday, 14th of July, 1996, at about ten before ten at the
evening, in the time zone called ``EET DST'' (which might be East European
Daylight Savings Time). date can also show the universal time:
+---------------------------------------------------------------------------+
|$ date -u                                                                  |
|Sun Jul 14 18:53:42 UTC 1996                                               |
|$                                                                          |
+---------------------------------------------------------------------------+
date is also used to set the kernel's software clock:
+---------------------------------------------------------------------------+
|# date 07142157                                                            |
|Sun Jul 14 21:57:00 EET DST 1996                                           |
|# date                                                                     |
|Sun Jul 14 21:57:02 EET DST 1996                                           |
|#                                                                          |
+---------------------------------------------------------------------------+
See the date manual page for more details; the syntax is a bit arcane. Only
root can set the time. While each user can have his own time zone, the clock
is the same for everyone.

Beware of the time command. This is not used to get the system time. Instead
it's used to time how long something takes. Refer the the time man page.

date only shows or sets the software clock. The clock commands synchronizes
the hardware and software clocks. It is used when the system boots, to read
the hardware clock and set the software clock. If you need to set both
clocks, you first set the software clock with date, and then the hardware
clock with clock -w.

The -u option to clock tells it that the hardware clock is in universal time.
You must use the -u option correctly. If you don't, your computer will be
quite confused about what the time is.

The clocks should be changed with care. Many parts of a Unix system require
the clocks to work correctly. For example, the cron daemon runs commands
periodically. If you change the clock, it can be confused of whether it needs
to run the commands or not. On one early Unix system, someone set the clock
twenty years into the future, and cron wanted to run all the periodic
commands for twenty years all at once. Current versions of cron can handle
this correctly, but you should still be careful. Big jumps or backward jumps
are more dangerous than smaller or forward ones.
-----------------------------------------------------------------------------

14.4. When the clock is wrong

The Linux software clock is not always accurate. It is kept running by a
periodic timer interrupt generated by PC hardware. If the system has too many
processes running, it may take too long to service the timer interrupt, and
the software clock starts slipping behind. The hardware clock runs
independently and is usually more accurate. If you boot your computer often
(as is the case for most systems that aren't servers), it will usually keep
fairly accurate time.

If you need to adjust the hardware clock, it is usually simplest to reboot,
go into the BIOS setup screen, and do it from there. This avoids all trouble
that changing system time might cause. If doing it via BIOS is not an option,
set the new time with date and clock (in that order), but be prepared to
reboot, if some part of the system starts acting funny.

Another method would be to use either hwclock -w or hwclock --systohc to sync
the hardware clock to the software clock. If you want to sync your software
clock to your hardware clock then you would use hwclock -s or hwclock
--hwtosys. For more information on this command read man hwclock.
-----------------------------------------------------------------------------

14.5. NTP - Network Time Protocol

A networked computer (even if just over a modem) can check its own clock
automatically by comparing it to the time on another computer known to keep
accurate time. Network Time Protocol (or NTP) does exactly that. It is a
method of verifying and correcting your computer's time by synchronizing it
with a another system. With NTP your system's time can be maintained to
within milliseconds of Coordinated Universal Time. Visit [http://www.time.gov
/about.html/] http://www.time.gov/about.html for more info.

For more casual Linux users, this is just a nice luxury. At my home all our
clocks are set based upon what my Linux system says the time is. For larger
organizations this "luxury" can become essential. Being able to search log
files for events based upon time can make life a lot easier and take a lot of
the "guess work" out of debugging.

Another example of how important NTP can be is with a SAN. Some SAN's require
NTP be configured and running properly to allow for proper synchronization
over filesystem usage, and proper timestamp control. Some SANs (and some
applications) can become confused when dealing with files that have
timestamps that are in the future.

Most Linux distributions come with a NTP package of some kind, either a .deb
or .rpm package. You can use that to install NTP, or you can download the
source files from [http://www.ntp.org/downloads.html] http://www.ntp.org/
downloads.html and compile it yourself. Either way, the basic configuration
is the same.
-----------------------------------------------------------------------------

14.6. Basic NTP configuration

The NTP program is configured using either the /etc/ntp.conf or /etc/
xntp.conf file depending on what distribution of Linux you have. I won't go
into too much detail on how to configure NTP. Instead I'll just cover the
basics.

An example of a basic ntp.conf file would look like:
+---------------------------------------------------------------------------+
|# --- GENERAL CONFIGURATION ---                                            |
|server  aaa.bbb.ccc.ddd                                                    |
|server  127.127.1.0                                                        |
|fudge   127.127.1.0 stratum 10                                             |
|                                                                           |
|# Drift file.                                                              |
