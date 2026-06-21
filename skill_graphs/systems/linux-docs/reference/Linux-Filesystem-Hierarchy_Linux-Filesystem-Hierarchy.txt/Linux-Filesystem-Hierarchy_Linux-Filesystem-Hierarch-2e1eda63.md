          0 XT-PIC cascade 3: 531695
          XT-PIC aha152x 4: 2014133
          XT-PIC serial 5: 44401
          XT-PIC pcnet_cs 8: 2
          XT-PIC rtc 11: 8
          XT-PIC i82365 12: 182918
          XT-PIC PS/2 Mouse 13: 1
          XT-PIC fpu 14: 1232265
          XT-PIC ide0 15: 7
          XT-PIC ide1 NMI: 0



        In 2.4 based kernels a couple of lines were added to this file LOC &
        ERR (this is the output of an SMP machine):


        # cat /proc/interrupts




          CPU0 CPU1
          0: 1243498 1214548 IO-APIC-edge timer
          1: 8949 8958 IO-APIC-edge keyboard
          2: 0 0 XT-PIC cascade
          5: 11286 10161 IO-APIC-edge soundblaster
          8: 1 0 IO-APIC-edge rtc
          9: 27422 27407 IO-APIC-edge 3c503
          12: 113645 113873 IO-APIC-edge PS/2 Mouse
          13: 0 0 XT-PIC fpu 14: 22491 24012 IO-APIC-edge ide0
          15: 2183 2415 IO-APIC-edge ide1
          17: 30564 30414 IO-APIC-level eth0
          18: 177 164 IO-APIC-level bttv NMI: 2457961 2457959
                      LOC: 2457882 2457881 ERR: 2155



        NMI is incremented in this case because every timer interrupt
        generates a NMI (Non Maskable Interrupt) which is used by the NMI
        Watchdog to detect lookups.


        LOC is the local interrupt counter of the internal APIC of every CPU.


        ERR is incremented in the case of errors in the IO-APIC bus (the bus
        that connects the CPUs in an SMP system. This means that an error has
        been detected, the IO-APIC automatically retries the transmission, so
        it should not be a big problem, but you should read the SMP-FAQ.


        In this context it could be interesting to note the new irq directory
        in 2.4. It could be used to set IRQ to CPU affinity, this means that
        you can "hook" an IRQ to only one CPU, or to exclude a CPU from
        handling IRQs. The contents of the irq subdir is one subdir for each
        IRQ, and one file; prof_cpu_mask. For example,



          # ls /proc/irq/ 0 10 12 14 16 18 2 4 6 8 prof_cpu_mask
                          1 11 13 15 17 19 3 5 7 9




          # ls /proc/irq/0/ smp_affinity



        The contents of the prof_cpu_mask file and each smp_affinity file for
        each IRQ is the same by default:



          # cat /proc/irq/0/smp_affinity
          ffffffff



        It's a bitmask, in which you can specify which CPUs can handle the
        IRQ, you can set it by doing:


        # echo 1 > /proc/irq/prof_cpu_mask


        This means that only the first CPU will handle the IRQ, but you can
        also echo 5 which means that only the first and fourth CPU can handle
        the IRQ. The way IRQs are routed is handled by the IO-APIC, and its
        Round Robin between all the CPUs which are allowed to handle it. As
        usual the kernel has more info than you and does a better job than
        you, so the defaults are the best choice for almost everyone.



/proc/iomem
    Memory map.

/proc/ioports
    Which I/O ports are in use at the moment.

/proc/irq
    Masks for irq to cpu affinity.

/proc/isapnp
      ISA PnP (Plug&Play) Info.

/proc/kcore
    An image of the physical memory of the system (can be ELF or A.OUT
    (deprecated in 2.4)). This is exactly the same size as your physical
    memory, but does not really take up that much memory; it is generated on
    the fly as programs access it. (Remember: unless you copy it elsewhere,
    nothing under /proc takes up any disk space at all.)

/proc/kmsg
    Messages output by the kernel. These are also routed to syslog.

/proc/ksyms
    Kernel symbol table.

/proc/loadavg
    The 'load average' of the system; three indicators of how much work the
    system has done during the last 1, 5 & 15 minutes.

/proc/locks
    Kernel locks.

/proc/meminfo
    Information about memory usage, both physical and swap. Concatenating
    this file produces similar results to using 'free' or the first few lines
    of 'top'.

/proc/misc
    Miscellaneous pieces of information. This is for information that has no
    real place within the rest of the proc filesystem.

/proc/modules
    Kernel modules currently loaded. Typically its output is the same as that
    given by the 'lsmod' command.

/proc/mounts
    Mounted filesystems

/proc/mtrr
    Information regarding mtrrs. (On Intel P6 family processors (Pentium Pro,
    Pentium II and later) the Memory Type Range Registers (MTRRs) may be used
    to control processor access to memory ranges. This is most useful when
    you have a video (VGA) card on a PCI or AGP bus. Enabling write-combining
    allows bus write transfers to be combined into a larger transfer before
    bursting over the PCI/AGP bus. This can increase performance of image
    write operations 2.5 times or more. The Cyrix 6x86, 6x86MX and M II
    processors have Address Range Registers (ARRs) which provide a similar
    functionality to MTRRs. For these, the ARRs are used to emulate the
    MTRRs. The AMD K6-2 (stepping 8 and above) and K6-3 processors have two
    MTRRs. These are supported. The AMD Athlon family provide 8 Intel style
    MTRRs. The Centaur C6 (WinChip) has 8 MCRs, allowing write-combining.
    These are also supported. The VIA Cyrix III and VIA C3 CPUs offer 8 Intel
    style MTRRs.) For more details regarding mtrr technology see /usr/src/
    linux/Documentation/mtrr.txt.

/proc/net
    Status information about network protocols.

IPv6 information


    /proc/net/udp6
          UDP sockets (IPv6).

    /proc/net/tcp6
        TCP sockets (IPv6).

    /proc/net/raw6
          Raw device statistics (IPv6).

    /proc/net/igmp6
        IP multicast addresses, which this host joined (IPv6).

    /proc/net/if_inet6
        List of IPv6 interface addresses.

    /proc/net/ipv6_route
        Kernel routing table for IPv6.

    /proc/net/rt6_stats
        Global IPv6 routing tables statistics.

    /proc/net/sockstat6
        Socket statistics (IPv6).

    /proc/net/snmp6
        Snmp data (IPv6).



General Network information


    /proc/net/arp
          Kernel ARP table.

    /proc/net/dev
        network devices with statistics.

    /proc/net/dev_mcast
        the Layer2 multicast groups which a device is listening to (interface
        index, label, number of references, number of bound addresses).

    /proc/net/dev_stat
        network device status.

    /proc/net/ip_fwchains
          Firewall chain linkage.

    /proc/net/ip_fwnames
        Firewall chain names.

    /proc/net/ip_masq
          Directory containing the masquerading tables.

    /proc/net/ip_masquerade
        Major masquerading table.

    /proc/net/netstat
        Network statistics.

    /proc/net/raw
          raw device statistics.

    /proc/net/route
        Kernel routing table.

    /proc/net/rpc
          Directory containing rpc info.

    /proc/net/rt_cache
        Routing cache.

    /proc/net/snmp
        SNMP data.

    /proc/net/sockstat
        Socket statistics.

    /proc/net/tcp
          TCP sockets.

    /proc/net/tr_rif
          Token ring RIF routing table.

    /proc/net/udp
        UDP sockets.

    /proc/net/unix
        UNIX domain sockets.

    /proc/net/wireless
          Wireless interface data (Wavelan etc).

    /proc/net/igmp
        IP multicast addresses, which this host joined.

    /proc/net/psched
        Global packet scheduler parameters.

    /proc/net/netlink
        List of PF_NETLINK sockets.

    /proc/net/ip_mr_vifs
        List of multicast virtual interfaces.

    /proc/net/ip_mr_cache
        List of multicast routing cache.

        You can use this information to see which network devices are
        available in your system and how much traffic was routed over those
        devices. In addition, each Channel Bond interface has its own
        directory. For example, the bond0 device will have a directory called
        /proc/net/bond0/. It will contain information that is specific to
        that bond, such as the current slaves of the bond, the link status of
        the slaves, and how many times the slaves link has failed.



/proc/parport
      The directory /proc/parport contains information about the parallel
    ports of your system. It has one subdirectory for each port, named after
    the port number (0,1,2,...).

    /proc/parport/autoprobe
          Any IEEE-1284 device ID information that has been acquired.

    /proc/parport/devices
        list of the device drivers using that port. A + will appear by the
        name of the device currently using the port (it might not appear
        against any).

    /proc/parport/hardware
        Parallel port's base address, IRQ line and DMA channel.

    /proc/parport/irq
        IRQ that parport is using for that port. This is in a separate file
        to allow you to alter it by writing a new value in (IRQ number or
        none).



/proc/partitions
    Table of partitions known to the system

/proc/pci, /proc/bus/pci
      Depreciated info of PCI bus.

/proc/rtc
    Real time clock

/proc/scsi
    If you have a SCSI host adapter in your system, you'll find a
    subdirectory named after the driver for this adapter in /proc/scsi.
    You'll also see a list of all recognized SCSI devices in /proc/scsi. The
    directory named after the driver has one file for each adapter found in
    the system. These files contain information about the controller,
    including the used IRQ and the IO address range. The amount of
    information shown is dependent on the adapter you use.

/proc/self
    A symbolic link to the process directory of the program that is looking
    at /proc. When two processes look at /proc, they get different links.
    This is mainly a convenience to make it easier for programs to get at
    their process directory.

/proc/slabinfo
      The slabinfo file gives information about memory usage at the slab
    level. Linux uses slab pools for memory management above page level in
    version 2.2. Commonly used objects have their own slab pool (such as
    network buffers, directory cache, and so on).

/proc/stat
    Overall/various statistics about the system, such as the number of page
    faults since the system was booted.

/proc/swaps
    Swap space utilization

/proc/sys
      This is not only a source of information, it also allows you to change
    parameters within the kernel without the need for recompilation or even a
    system reboot. Take care when attempting this as it can both optimize
    your system and also crash it. It is advisable to read both documentation
    and source before actually making adjustments. The entries in /proc may
    change slightly between kernel versions, so if there is any doubt review
    the kernel documentation in the directory /usr/src/linux/Documentation.
    Under some circumstances, you may have no alternative but to reboot the
    machine once an error occurs. To change a value, simply echo the new
    value into the file. An example is given below in the section on the file
    system data. Of course, you need to be 'root' to do any of this. You can
    create your own boot script to perform this every time your system boots.

/proc/sys/fs
    Contains file system data. This subdirectory contains specific file
    system, file handle, inode, dentry and quota information.

    dentry-state
        Status of the directory cache. Since directory entries are
        dynamically allocated and deallocated, this file indicates the
        current status. It holds six values, in which the last two are not
        used and are always zero. The others are listed below:



          File      Content
          nr_dentry Almost always zero
          nr_unused Number of unused cache entries
          age_limit in seconds after the entry may be
                    reclaimed, when memory is short want_pages internally


    dquot-max
          The file dquot-max shows the maximum number of cached disk quota
        entries.

    dquot-nr
          shows the number of allocated disk quota entries and the number of
        free disk quota entries. If the number of available cached disk
        quotas is very low and you have a large number of simultaneous system
        users, you might want to raise the limit.

    file-nr and file-max
        The kernel allocates file handles dynamically, but doesn't free them
        again at this time. The value in file-max denotes the maximum number
        of file handles that the Linux kernel will allocate. When you get a
        lot of error messages about running out of file handles, you might
        want to raise this limit. The default value is 4096. To change it,
        just write the new number into the file:


          # cat /proc/sys/fs/file-max
          4096
          # echo 8192 > /proc/sys/fs/file-max
          # cat /proc/sys/fs/file-max
          8192



        This method of revision is useful for all customizable parameters of
        the kernel - simply echo the new value to the corresponding file.


        The three values in file-nr denote the number of allocated file
        handles, the number of used file handles, and the maximum number of
        file handles. When the allocated file handles come close to the
        maximum, but the number of actually used handles is far behind,
        you've encountered a peak in your usage of file handles and you don't
        need to increase the maximum.

    inode-state, inode-nr and inode-max
        As with file handles, the kernel allocates the inode structures
        dynamically, but can't free them yet.


        The value in inode-max denotes the maximum number of inode handlers.
        This value should be 3 to 4 times larger than the value in file-max,
        since stdin, stdout, and network sockets also need an inode struct to
        handle them. If you regularly run out of inodes, you should increase
        this value.


        The file inode-nr contains the first two items from inode-state, so
        we'll skip to that file...


        inode-state contains three actual numbers and four dummy values. The
        numbers are nr_inodes, nr_free_inodes, and preshrink (in order of
        appearance).

    nr_inodes
        Denotes the number of inodes the system has allocated. This can be
        slightly more than inode-max because Linux allocates them one pageful
        at a time.

    nr_free_inodes
        Represents the number of free inodes and preshrink is nonzero when
        nr_inodes is greater than inode-max and the system needs to prune the
        inode list instead of allocating more.

    super-nr and super-max
          Again, super block structures are allocated by the kernel, but not
        freed. The file super-max contains the maximum number of super block
        handlers, where super-nr shows the number of currently allocated
        ones. Every mounted file system needs a super block, so if you plan
        to mount lots of file systems, you may want to increase these
        numbers.

    binfmt_misc
          This handles the kernel support for miscellaneous binary formats.
        binfmt_misc provides the ability to register additional binary
        formats to the kernel without compiling an additional module/kernel.
        Therefore, binfmt_misc needs to know magic numbers at the beginning
        or the filename extension of the binary. It works by maintaining a
        linked list of structs that contain a description of a binary format,
        including a magic with size (or the filename extension), offset and
        mask, and the interpreter name. On request it invokes the given
        interpreter with the original program as argument, as binfmt_java and
        binfmt_em86 and binfmt_mz do. Since binfmt_misc does not define any
        default binary-formats, you have to register an additional
        binary-format. There are two general files in binfmt_misc and one
        file per registered format. The two general files are register and
        status. To register a new binary format you have to issue the command
        echo :name:type:offset:magic:mask:interpreter: > /proc/sys/fs/
        binfmt_misc/register with appropriate name (the name for the /
        proc-dir entry), offset (defaults to 0, if omitted), magic, mask
        (which can be omitted, defaults to all 0xff) and last but not least,
        the interpreter that is to be invoked (for example and testing /bin/
        echo). Type can be M for usual magic matching or E for filename
        extension matching (give extension in place of magic). If you do a
        cat on the file /proc/sys/fs/binfmt_misc/status, you will get the
        current status (enabled/disabled) of binfmt_misc. Change the status
        by echoing 0 (disables) or 1 (enables) or -1 (caution: this clears
        all previously registered binary formats) to status. For example echo
        0 > status to disable binfmt_misc (temporarily). Each registered
        handler has an entry in /proc/sys/fs/binfmt_misc. These files perform
        the same function as status, but their scope is limited to the actual
        binary format. By 'cating' this file, you also receive all related
        information about the interpreter/magic of the binfmt. An example of
        the usage of binfmt_misc (emulate binfmt_java) follows:


          cd /proc/sys/fs/binfmt_misc
          echo ':Java:M::\xca\xfe\xba\xbe::/usr/local/java/bin/javawrapper:'
          > register
          echo ':HTML:E::html::/usr/local/java/bin/appletviewer:'
          > register
          echo ':Applet:M::<!--applet::/usr/local/java/bin/appletviewer:' >
          register
          echo ':DEXE:M::\x0eDEX::/usr/bin/dosexec:' < register



          These four lines add support for Java executables and Java applets
        (like binfmt_java, additionally recognizing the .html extension with
        no need to put <!--applet> to every applet file). You have to install
        the JDK and the shell-script /usr/local/java/bin/javawrapper too. It
        works around the brokenness of the Java filename handling. To add a
        Java binary, just create a link to the class-file somewhere in the
        path.



/proc/sys/kernel
    This directory reflects general kernel behaviors and the contents will be
    dependent upon your configuration. Here you'll find the most important
    files, along with descriptions of what they mean and how to use them.

    /proc/sys/kernel/acct
        The file contains three values; highwater, lowwater, and frequency.
        It exists only when BSD-style process accounting is enabled. These
        values control its behavior. If the free space on the file system
        where the log lives goes below lowwater percentage, accounting
        suspends. If it goes above highwater percentage, accounting resumes.
        Frequency determines how often you check the amount of free space
        (value is in seconds). Default settings are: 4, 2, and 30. That is,
        suspend accounting if there is less than 2 percent free; resume it if
        we have a value of 3 or more percent; consider information about the
        amount of free space valid for 30 seconds

    /proc/sys/kernel/ctrl-alt-del
          When the value in this file is 0, ctrl-alt-del is trapped and sent
        to the init program to handle a graceful restart. However, when the
        value is greater that zero, Linux's reaction to this key combination
        will be an immediate reboot, without syncing its dirty buffers. It
        should be noted that when a program (like dosemu) has the keyboard in
        raw mode, the ctrl-alt-del is intercepted by the program before it
        ever reaches the kernel tty layer, and it is up to the program to
        decide what to do with it.

    /proc/sys/kernel/domainname, /proc/sys/kernel/hostname
          These files can be controlled to set the NIS domainname and
        hostname of your box. For the classic darkstar.drop.org a simple: #
        echo "darkstar" > /proc/sys/kernel/hostname # echo "drop.org" > /proc
        /sys/kernel/domainname would suffice to set your hostname and NIS
        domainname. /proc/sys/kernel/osrelease, /proc/sys/kernel/ostype, /
        proc/sys/kernel/version The names make it pretty obvious what these
        fields contain: # cat /proc/sys/kernel/osrelease 2.2.12 # cat /proc/
        sys/kernel/ostype Linux # cat /proc/sys/kernel/version #4 Fri Oct 1
        12:41:14 PDT 1999 The files osrelease and ostype should be clear
        enough. Version needs a little more clarification. The #4 means that
        this is the 4th kernel built from this source base and the date after
        it indicates the time the kernel was built. The only way to tune
        these values is to rebuild the kernel.

    /proc/sys/kernel/panic
          The value in this file represents the number of seconds the kernel
        waits before rebooting on a panic. When you use the software
        watchdog, the recommended setting is 60. If set to 0, the auto reboot
        after a kernel panic is disabled, which is the default setting.

    /proc/sys/kernel/printk
        The four values in printk denote * console_loglevel, *
        default_message_loglevel, * minimum_console_level and *
        default_console_loglevel respectively. These values influence printk
        () behavior when printing or logging error messages, which come from
        inside the kernel. See syslog(2) for more information on the
        different log levels.

    /proc/sys/kernel/console_loglevel
          Messages with a higher priority than this will be printed to the
        console.

    /proc/sys/kernel/default_message_level
          Messages without an explicit priority will be printed with this
        priority.

    /proc/sys/kernel/minimum_console_loglevel
          Minimum (highest) value to which the console_loglevel can be set.

    /proc/sys/kernel/default_console_loglevel
          Default value for console_loglevel.

    /proc/sys/kernel/sg-big-buff
