to hold them, they will then be swapped out (to some other swap space). If
there is not enough virtual memory to hold all of the pages Linux will start
to thrash; after a long while it should recover, but meanwhile the system is
unusable. You should check (e.g., with free) that there is enough free memory
before removing a swap space from use.

All the swap spaces that are used automatically with swapon -a can be removed
from use with swapoff -a; it looks at the file /etc/fstab to find what to
remove. Any manually used swap spaces will remain in use.

Sometimes a lot of swap space can be in use even though there is a lot of
free physical memory. This can happen for instance if at one point there is
need to swap, but later a big process that occupied much of the physical
memory terminates and frees the memory. The swapped-out data is not
automatically swapped in until it is needed, so the physical memory may
remain free for a long time. There is no need to worry about this, but it can
be comforting to know what is happening.
-----------------------------------------------------------------------------

6.4. Sharing swap spaces with other operating systems

Virtual memory is built into many operating systems. Since they each need it
only when they are running, i.e., never at the same time, the swap spaces of
all but the currently running one are being wasted. It would be more
efficient for them to share a single swap space. This is possible, but can
require a bit of hacking. The Tips-HOWTO at http://www.tldp.org/HOWTO/
Tips-HOWTO.html, which contains some advice on how to implement this.
-----------------------------------------------------------------------------

6.5. Allocating swap space

Some people will tell you that you should allocate twice as much swap space
as you have physical memory, but this is a bogus rule. Here's how to do it
properly:

��*�Estimate your total memory needs. This is the largest amount of memory
    you'll probably need at a time, that is the sum of the memory
    requirements of all the programs you want to run at the same time. This
    can be done by running at the same time all the programs you are likely
    to ever be running at the same time.

    For instance, if you want to run X, you should allocate about 8 MB for
    it, gcc wants several megabytes (some files need an unusually large
    amount, up to tens of megabytes, but usually about four should do), and
    so on. The kernel will use about a megabyte by itself, and the usual
    shells and other small utilities perhaps a few hundred kilobytes (say a
    megabyte together). There is no need to try to be exact, rough estimates
    are fine, but you might want to be on the pessimistic side.

    Remember that if there are going to be several people using the system at
    the same time, they are all going to consume memory. However, if two
    people run the same program at the same time, the total memory
    consumption is usually not double, since code pages and shared libraries
    exist only once.

    The free and ps commands are useful for estimating the memory needs.

��*�Add some security to the estimate in step 1. This is because estimates of
    program sizes will probably be wrong, because you'll probably forget some
    programs you want to run, and to make certain that you have some extra
    space just in case. A couple of megabytes should be fine. (It is better
    to allocate too much than too little swap space, but there's no need to
    over-do it and allocate the whole disk, since unused swap space is wasted
    space; see later about adding more swap.) Also, since it is nicer to deal
    with even numbers, you can round the value up to the next full megabyte.

��*�Based on the computations above, you know how much memory you'll be
    needing in total. So, in order to allocate swap space, you just need to
    subtract the size of your physical memory from the total memory needed,
    and you know how much swap space you need. (On some versions of UNIX, you
    need to allocate space for an image of the physical memory as well, so
    the amount computed in step 2 is what you need and you shouldn't do the
    subtraction.)

��*�If your calculated swap space is very much larger than your physical
    memory (more than a couple times larger), you should probably invest in
    more physical memory, otherwise performance will be too low.


It's a good idea to have at least some swap space, even if your calculations
indicate that you need none. Linux uses swap space somewhat aggressively, so
that as much physical memory as possible can be kept free. Linux will swap
out memory pages that have not been used, even if the memory is not yet
needed for anything. This avoids waiting for swapping when it is needed: the
swapping can be done earlier, when the disk is otherwise idle.

Swap space can be divided among several disks. This can sometimes improve
performance, depending on the relative speeds of the disks and the access
patterns of the disks. You might want to experiment with a few schemes, but
be aware that doing the experiments properly is quite difficult. You should
not believe claims that any one scheme is superior to any other, since it
won't always be true.
-----------------------------------------------------------------------------

6.6. The buffer cache

Reading from a disk is very slow compared to accessing (real) memory. In
addition, it is common to read the same part of a disk several times during
relatively short periods of time. For example, one might first read an e-mail
message, then read the letter into an editor when replying to it, then make
the mail program read it again when copying it to a folder. Or, consider how
often the command ls might be run on a system with many users. By reading the
information from disk only once and then keeping it in memory until no longer
needed, one can speed up all but the first read. This is called disk
buffering, and the memory used for the purpose is called the buffer cache.

Since memory is, unfortunately, a finite, nay, scarce resource, the buffer
cache usually cannot be big enough (it can't hold all the data one ever wants
to use). When the cache fills up, the data that has been unused for the
longest time is discarded and the memory thus freed is used for the new data.

Disk buffering works for writes as well. On the one hand, data that is
written is often soon read again (e.g., a source code file is saved to a
file, then read by the compiler), so putting data that is written in the
cache is a good idea. On the other hand, by only putting the data into the
cache, not writing it to disk at once, the program that writes runs quicker.
The writes can then be done in the background, without slowing down the other
programs.

Most operating systems have buffer caches (although they might be called
something else), but not all of them work according to the above principles.
Some are write-through: the data is written to disk at once (it is kept in
the cache as well, of course). The cache is called write-back if the writes
are done at a later time. Write-back is more efficient than write-through,
but also a bit more prone to errors: if the machine crashes, or the power is
cut at a bad moment, or the floppy is removed from the disk drive before the
data in the cache waiting to be written gets written, the changes in the
cache are usually lost. This might even mean that the filesystem (if there is
one) is not in full working order, perhaps because the unwritten data held
important changes to the bookkeeping information.

Because of this, you should never turn off the power without using a proper
shutdown procedure or remove a floppy from the disk drive until it has been
unmounted (if it was mounted) or after whatever program is using it has
signaled that it is finished and the floppy drive light doesn't shine
anymore. The sync command flushes the buffer, i.e., forces all unwritten data
to be written to disk, and can be used when one wants to be sure that
everything is safely written. In traditional UNIX systems, there is a program
called update running in the background which does a sync every 30 seconds,
so it is usually not necessary to use sync. Linux has an additional daemon,
bdflush, which does a more imperfect sync more frequently to avoid the sudden
freeze due to heavy disk I/O that sync sometimes causes.

Under Linux, bdflush is started by update. There is usually no reason to
worry about it, but if bdflush happens to die for some reason, the kernel
will warn about this, and you should start it by hand (/sbin/update).

The cache does not actually buffer files, but blocks, which are the smallest
units of disk I/O (under Linux, they are usually 1 KB). This way, also
directories, super blocks, other filesystem bookkeeping data, and
non-filesystem disks are cached.

The effectiveness of a cache is primarily decided by its size. A small cache
is next to useless: it will hold so little data that all cached data is
flushed from the cache before it is reused. The critical size depends on how
much data is read and written, and how often the same data is accessed. The
only way to know is to experiment.

If the cache is of a fixed size, it is not very good to have it too big,
either, because that might make the free memory too small and cause swapping
(which is also slow). To make the most efficient use of real memory, Linux
automatically uses all free RAM for buffer cache, but also automatically
makes the cache smaller when programs need more memory.

Under Linux, you do not need to do anything to make use of the cache, it
happens completely automatically. Except for following the proper procedures
for shutdown and removing floppies, you do not need to worry about it.
-----------------------------------------------------------------------------

Chapter 7. System Monitoring

    "That's Hall Monitor to you!"Spongebob Squarepants

One of the most important responsibilities a system administrator has, is
monitoring their systems. As a system administrator you'll need the ability
to find out what is happening on your system at any given time. Whether it's
the percentage of system's resources currently used, what commands are being
run, or who is logged on. This chapter will cover how to monitor your system,
and in some cases, how to resolve problems that may arise.

When a performance issue arises, there are 4 main areas to consider: CPU,
Memory, Disk I/O, and Network. The ability to determine where the bottleneck
is can save you a lot of time.
-----------------------------------------------------------------------------

7.1. System Resources

Being able to monitor the performance of your system is essential. If system
resources become to low it can cause a lot of problems. System resources can
be taken up by individual users, or by services your system may host such as
email or web pages. The ability to know what is happening can help determine
whether system upgrades are needed, or if some services need to be moved to
another machine.
-----------------------------------------------------------------------------

7.1.1. The top command.

The most common of these commands is top. The top will display a continually
updating report of system resource usage.
+---------------------------------------------------------------------------------+
|# top                                                                            |
| 12:10:49  up 1 day,  3:47,  7 users,  load average: 0.23, 0.19, 0.10            |
|125 processes: 105 sleeping, 2 running, 18 zombie, 0 stopped                     |
|CPU states:   5.1% user   1.1% system   0.0% nice   0.0% iowait  93.6% idle      |
|Mem:   512716k av,  506176k used,    6540k free,       0k shrd,   21888k buff    |
|Swap: 1044216k av,  161672k used,  882544k free                  199388k cached  |
|                                                                                 |
|  PID USER     PRI  NI  SIZE  RSS SHARE STAT %CPU %MEM   TIME CPU COMMAND        |
| 2330 root      15   0  161M  70M  2132 S     4.9 14.0  1000m   0 X              |
| 2605 weeksa    15   0  8240 6340  3804 S     0.3  1.2   1:12   0 kdeinit        |
| 3413 weeksa    15   0  6668 5324  3216 R     0.3  1.0   0:20   0 kdeinit        |
|18734 root      15   0  1192 1192   868 R     0.3  0.2   0:00   0 top            |
| 1619 root      15   0   776  608   504 S     0.1  0.1   0:53   0 dhclient       |
|    1 root      15   0   480  448   424 S     0.0  0.0   0:03   0 init           |
|    2 root      15   0     0    0     0 SW    0.0  0.0   0:00   0 keventd        |
|    3 root      15   0     0    0     0 SW    0.0  0.0   0:00   0 kapmd          |
|    4 root      35  19     0    0     0 SWN   0.0  0.0   0:00   0 ksoftirqd_CPU0 |
|    9 root      25   0     0    0     0 SW    0.0  0.0   0:00   0 bdflush        |
|    5 root      15   0     0    0     0 SW    0.0  0.0   0:00   0 kswapd         |
|   10 root      15   0     0    0     0 SW    0.0  0.0   0:00   0 kupdated       |
|   11 root      25   0     0    0     0 SW    0.0  0.0   0:00   0 mdrecoveryd    |
|   15 root      15   0     0    0     0 SW    0.0  0.0   0:01   0 kjournald      |
|   81 root      25   0     0    0     0 SW    0.0  0.0   0:00   0 khubd          |
| 1188 root      15   0     0    0     0 SW    0.0  0.0   0:00   0 kjournald      |
| 1675 root      15   0   604  572   520 S     0.0  0.1   0:00   0 syslogd        |
| 1679 root      15   0   428  376   372 S     0.0  0.0   0:00   0 klogd          |
| 1707 rpc       15   0   516  440   436 S     0.0  0.0   0:00   0 portmap        |
| 1776 root      25   0   476  428   424 S     0.0  0.0   0:00   0 apmd           |
| 1813 root      25   0   752  528   524 S     0.0  0.1   0:00   0 sshd           |
| 1828 root      25   0   704  548   544 S     0.0  0.1   0:00   0 xinetd         |
| 1847 ntp       15   0  2396 2396  2160 S     0.0  0.4   0:00   0 ntpd           |
| 1930 root      24   0    76    4     0 S     0.0  0.0   0:00   0 rpc.rquotad    |
+---------------------------------------------------------------------------------+

The top portion of the report lists information such as the system time,
uptime, CPU usage, physical ans swap memory usage, and number of processes.
Below that is a list of the processes sorted by CPU utilization.

You can modify the output of top while is is running. If you hit an i, top
will no longer display idle processes. Hit i again to see them again. Hitting
M will sort by memory usage, S will sort by how long they processes have been
running, and P will sort by CPU usage again.

In addition to viewing options, you can also modify processes from within the
top command. You can use u to view processes owned by a specific user, k to
kill processes, and r to renice them.

For more in-depth information about processes you can look in the /proc
filesystem. In the /proc filesystem you will find a series of sub-directories
with numeric names. These directories are associated with the processes ids
of currently running processes. In each directory you will find a series of
files containing information about the process.

YOU MUST TAKE EXTREME CAUTION TO NOT MODIFY THESE FILES, DOING SO MAY CAUSE
SYSTEM PROBLEMS!
-----------------------------------------------------------------------------

7.1.2. The iostat command.

The iostat will display the current CPU load average and disk I/O
information. This is a great command to monitor your disk I/O usage.
+---------------------------------------------------------------------------+
|# iostat                                                                   |
|Linux 2.4.20-24.9 (myhost)       12/23/2003                                |
|                                                                           |
|avg-cpu:  %user   %nice    %sys   %idle                                    |
|          62.09    0.32    2.97   34.62                                    |
|                                                                           |
|Device:            tps   Blk_read/s   Blk_wrtn/s   Blk_read   Blk_wrtn     |
|dev3-0            2.22        15.20        47.16    1546846    4799520     |
+---------------------------------------------------------------------------+
For 2.4 kernels the devices is names using the device's major and minor
number. In this case the device listed is /dev/had. To have iostat print this
out for you, use the -x.
+----------------------------------------------------------------------------------------------+
|# iostat -x                                                                                   |
|Linux 2.4.20-24.9 (myhost)       12/23/2003                                                   |
|                                                                                              |
|avg-cpu:  %user   %nice    %sys   %idle                                                       |
|          62.01    0.32    2.97   34.71                                                       |
|                                                                                              |
|Device:  rrqm/s wrqm/s r/s  w/s rsec/s wsec/s rkB/s wkB/s avgrq-sz avgqu-sz await svctm %util |
|/dev/hdc   0.00   0.00 .00 0.00   0.00   0.00  0.00  0.00     0.00     2.35  0.00  0.00 14.71 |
|/dev/had   1.13   4.50 .81 1.39  15.18  47.14  7.59 23.57    28.24     1.99 63.76 70.48 15.56 |
|/dev/hda1  1.08   3.98 .73 1.27  14.49  42.05  7.25 21.02    28.22     0.44 21.82  4.97  1.00 |
|/dev/hda2  0.00   0.51 .07 0.12   0.55   5.07  0.27  2.54    30.35     0.97 52.67 61.73  2.99 |
|/dev/hda3  0.05   0.01 .02 0.00   0.14   0.02  0.07  0.01     8.51     0.00 12.55  2.95  0.01 |
+----------------------------------------------------------------------------------------------+

The iostat man page contains a detailed explanation of what each of these
columns mean.
-----------------------------------------------------------------------------

7.1.3. The ps command

The ps will provide you a list of processes currently running. There is a
wide variety of options that this command gives you.

A common use would be to list all processes currently running. To do this you
would use the ps -ef command. (Screen output from this command is too large
to include, the following is only a partial output.)
+-----------------------------------------------------------------------------------------+
|UID        PID  PPID  C STIME TTY          TIME CMD                                      |
|root         1     0  0 Dec22 ?        00:00:03 init                                     |
|root         2     1  0 Dec22 ?        00:00:00 [keventd]                                |
|root         3     1  0 Dec22 ?        00:00:00 [kapmd]                                  |
|root         4     1  0 Dec22 ?        00:00:00 [ksoftirqd_CPU0]                         |
|root         9     1  0 Dec22 ?        00:00:00 [bdflush]                                |
|root         5     1  0 Dec22 ?        00:00:00 [kswapd]                                 |
|root         6     1  0 Dec22 ?        00:00:00 [kscand/DMA]                             |
|root         7     1  0 Dec22 ?        00:01:28 [kscand/Normal]                          |
|root         8     1  0 Dec22 ?        00:00:00 [kscand/HighMem]                         |
|root        10     1  0 Dec22 ?        00:00:00 [kupdated]                               |
|root        11     1  0 Dec22 ?        00:00:00 [mdrecoveryd]                            |
|root        15     1  0 Dec22 ?        00:00:01 [kjournald]                              |
|root        81     1  0 Dec22 ?        00:00:00 [khubd]                                  |
|root      1188     1  0 Dec22 ?        00:00:00 [kjournald]                              |
|root      1675     1  0 Dec22 ?        00:00:00 syslogd -m 0                             |
|root      1679     1  0 Dec22 ?        00:00:00 klogd -x                                 |
|rpc       1707     1  0 Dec22 ?        00:00:00 portmap                                  |
|root      1813     1  0 Dec22 ?        00:00:00 /usr/sbin/sshd                           |
|ntp       1847     1  0 Dec22 ?        00:00:00 ntpd -U ntp                              |
|root      1930     1  0 Dec22 ?        00:00:00 rpc.rquotad                              |
|root      1934     1  0 Dec22 ?        00:00:00 [nfsd]                                   |
|root      1942     1  0 Dec22 ?        00:00:00 [lockd]                                  |
|root      1943     1  0 Dec22 ?        00:00:00 [rpciod]                                 |
|root      1949     1  0 Dec22 ?        00:00:00 rpc.mountd                               |
|root      1961     1  0 Dec22 ?        00:00:00 /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf |
|root      2057     1  0 Dec22 ?        00:00:00 /usr/bin/spamd -d -c -a                  |
|root      2066     1  0 Dec22 ?        00:00:00 gpm -t ps/2 -m /dev/psaux                |
|bin       2076     1  0 Dec22 ?        00:00:00 /usr/sbin/cannaserver -syslog -u bin     |
|root      2087     1  0 Dec22 ?        00:00:00 crond                                    |
|daemon    2195     1  0 Dec22 ?        00:00:00 /usr/sbin/atd                            |
|root      2215     1  0 Dec22 ?        00:00:11 /usr/sbin/rcd                            |
|weeksa    3414  3413  0 Dec22 pts/1    00:00:00 /bin/bash                                |
|weeksa    4342  3413  0 Dec22 pts/2    00:00:00 /bin/bash                                |
|weeksa   19121 18668  0 12:58 pts/2    00:00:00 ps -ef                                   |
+-----------------------------------------------------------------------------------------+

The first column shows who owns the process. The second column is the process
ID. The Third column is the parent process ID. This is the process that
generated, or started, the process. The forth column is the CPU usage (in
percent). The fifth column is the start time, of date if the process has been
running long enough. The sixth column is the tty associated with the process,
if applicable. The seventh column is the cumulitive CPU usage (total amount
of CPU time is has used while running). The eighth column is the command
itself.

With this information you can see exactly what is running on your system and
kill run-away processes, or those that are causing problems.
-----------------------------------------------------------------------------

7.1.4. The vmstat command

The vmstat command will provide a report showing statistics for system
processes, memory, swap, I/O, and the CPU. These statistics are generated
using data from the last time the command was run to the present. In the case
of the command never being run, the data will be from the last reboot until
the present.


+-------------------------------------------------------------------------------+
|# vmstat                                                                       |
|   procs                      memory      swap          io     system      cpu |
| r  b  w   swpd   free   buff  cache   si   so    bi    bo   in    cs us sy id |
| 0  0  0 181604  17000  26296 201120    0    2     8    24  149     9 61  3 36 |
+-------------------------------------------------------------------------------+

The following was taken from the vmstat man page.


    FIELD�DESCRIPTIONS
    Procs
    ����r:�The�number�of�processes�waiting�for�run�time.
    ����b:�The�number�of�processes�in�uninterruptible�sleep.
    ����w:�The�number�of�processes�swapped�out�but�otherwise�runnable.��This
    �������field�is�calculated,�but�Linux�never�desperation�swaps.

    Memory
    ����swpd:�the�amount�of�virtual�memory�used�(kB).
    ����free:�the�amount�of�idle�memory�(kB).
    ����buff:�the�amount�of�memory�used�as�buffers�(kB).

    Swap
    ����si:�Amount�of�memory�swapped�in�from�disk�(kB/s).
    ����so:�Amount�of�memory�swapped�to�disk�(kB/s).

    IO
    ����bi:�Blocks�sent�to�a�block�device�(blocks/s).
    ����bo:�Blocks�received�from�a�block�device�(blocks/s).

    System
    ����in:�The�number�of�interrupts�per�second,�including�the�clock.
    ����cs:�The�number�of�context�switches�per�second.

    CPU
    ����These�are�percentages�of�total�CPU�time.
    ����us:�user�time
    ����sy:�system�time
    ����id:�idle�time

-----------------------------------------------------------------------------
7.1.5. The lsof command

The lsof command will print out a list of every file that is in use. Since
Linux considers everythihng a file, this list can be very long. However, this
command can be useful in diagnosing problems. An example of this is if you
wish to unmount a filesystem, but you are being told that it is in use. You
could use this command and grep for the name of the filesystem to see who is
using it.

Or suppose you want to see all files in use by a particular process. To do
this you would use lsof -p -processid-.
-----------------------------------------------------------------------------

7.1.6. Finding More Utilities

To learn more about what command line tools are available, Chris Karakas has
