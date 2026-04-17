       [http://tuxmobil.org/mobile_solaris.html] Solaris on laptops and
       notebooks may also be helpful.
    5. StrongARM: a very low-power CPU found in [http://www.rebel.com/]
       Rebel.com's popular NetWinder (some kind of mobile computer,
       too), and actively supported in the Debian project, it is also in
       several WinCE machines, such as HP's Jornadas. Only the lack of
       tech specs prevents Linux from being ported to these tiny,
       long-battery-life machines. A full-scale StrongARM-based laptop
       would make a superb Linux platform.
       For PDAs with ARM/StrongARM CPU see the Part II in Linux on the
       RoadHandheld Devices part below.
    6. MIPS: Used in SGI mainframes and Cobalt Micro intranet
       appliances, chips based on this architecture are used in many
       Windows-CE machines. Linux has been ported to a few of these.
    7. AMD Processor: More about Linux on AMD processors may be found at
       [http://www.x86-64.org/] x86-64 org . At TuxMobil there is also a
       survey of [http://tuxmobil.org/cpu_amd.html] laptops with AMD
       CPUs .
    8. 64bit CPUs: At TuxMobil there is a survey of
       [http://tuxmobil.org/cpu_64bit.html] laptops with 64bit CPUs .
     ________________________________________________________________

1.4.4.2. Miscellaneous

   At higher speed, a CPU consumes more power and generates more heat.
   Therefore, in many laptops a special low-power CPU is used. Usually,
   this special CPU doesn't use as much power as a similar processor
   used in a desktop. These special CPUs are also more expensive. As a
   side effect you may find that laptops with a desktop CPU often have a
   quite noisy fan.
     ________________________________________________________________

1.4.5. Number of Spindles

   Laptops and notebooks are often described by the number of spindles.

    1. one spindle: harddisk. Usually sub-notebooks, often provided with
       an external optical drive (CD/DVD).
    2. two spindles: harddisk, optical drive (CD/DVD).
    3. three spindles: harddisk, optical drive (CD/DVD), floppy drive.
       These laptops are often used as desktop PC replacement.
     ________________________________________________________________

1.4.6. Cooling

   An enormously important issue. Anything based on PPC or Pentium will
   generate enormous amounts of heat which must be dissipated.
   Generally, this means either a fan, or a heat sink the size of the
   case. If it's a fan, the air path shouldn't get blocked, or it will
   overheat and burn out. This means machines with a fan mounted in the
   bottom are a big, big mistake: you can't use them on a soft surface.
     ________________________________________________________________

1.4.7. Keyboard Quality

   Though you might use your desktop computer to do longer writings, a
   good keyboard can save you some head- and fingeraches. Look
   especially for the location of special keys like: <ESC>, <TAB>,
   <Pos1>, <End>, <PageDown>, <PageUp> and the cursor keys.
     ________________________________________________________________

1.4.8. Price

   Laptops are quite expensive if you compare them with desktops (though
   maybe not if compared with LCD, IrDA�, PCMCIA capabilities). So you
   may decide between a brand or no-name product. Though I would like to
   encourage you to take a no-name product, there are some caveats. I
   have experienced that laptops break often, so you are better off,
   when you have an after-sales warranty, which is usually only offered
   with brand products. Or you may decide to take a second hand machine.
   When I tried this, I discovered that the laptop market is changing
   quite often. A new generation is released approximately every three
   months (compared by CPU speed, harddisk capacity, screen size etc.).
   So laptops become old very quick. But this scheme often isn't
   followed by the prices for second hand laptops. They seem too
   expensive to me. Anyway if you plan on purchasing a second hand
   machine, review my recommendations on checking the machine.
     ________________________________________________________________

1.4.9. Power Supply

   If you travel abroad pay attention to the voltage levels which are
   supported by the power supply. Also the power supply is usually one
   of the heavier parts of a laptop. Another caveat is the power plug,
   which often is different from country to country.
     ________________________________________________________________

1.5. Sources of More Information

   Specifications, manuals and manufacturer support often are not
   helpful. Therefore you should retrieve information from other sources
   too:

    1. [http://tuxmobil.org/mylaptops.html] TuxMobil Linux Laptop and
       Notebook Survey , this survey covers other UniXes (for example
       BSD, Solaris), too.
    2. [http://www.linux-on-laptops.com/] Linux on Laptops.

   General information about manufacturer support you may find in my
   [http://tuxmobil.org/laptop_manufacturer.html] Linux Status Survey of
   Laptop and Notebook Manufacturers , though don't expect to much Linux
   support from them yet. Sometimes the
   [http://tuxmobil.org/laptop_oem.html] Matrix of OEM/ODM Relations may
   help to find information for your laptop under another brand name.
     ________________________________________________________________

1.6. Linux Compatibility Check

1.6.1. Related Documentation

    1. [http://tldp.org/HOWTO/Hardware-HOWTO/] Hardware-HOWTO
    2. [http://tldp.org/HOWTO/Kernel-HOWTO/] Kernel-HOWTO
    3. PCMCIA-HOWTO
    4. [http://tldp.org/HOWTO/PCI-HOWTO.html] PCI-HOWTO
    5. [http://tldp.org/HOWTO/Plug-and-Play-HOWTO.html]
       Plug-and-Play-HOWTO
     ________________________________________________________________

1.6.2. Check Methods in General

   If you can't find the necessary information through the above
   mentioned sources, you are on your own. Luckily, Linux provides many
   means to help. For details see the section Part V in Linux on the
   Road Hardware In Detail below. In general you may use:

    1. First of all the kernel itself. Look up what kind of hardware is
       detected by the kernel. You get this information during boot time
       or by dmesg or by looking into /var/log/messages. For the very
       first boot messages check /var/log/boot.
    2. If your kernel supports the /proc file system you may get
       detailed information about PCI devices by cat /proc/pci Please
       read the kernel documentation pci.txt. You may get further
       information about unknown PCI devices at the
       [http://pciids.sf.net/] Linux PCI ID Repository, the home of the
       pci.ids file. From 2.1.82 kernels on you may use the lspci
       command from the pci-utils package.
    3. To retrieve information about Plug-and-Play (PNP) devices use
       isapnp-tools .
    4. Use scsi_info by David Hinds for SCSI devices or scsiinfo.

   If you don't want to install a complete Linux you may retrieve this
   information by using a micro Linux ( see Appendix A Appendix A). The
   package muLinux provides even a small systest program and TomsRtBt
   comes with memtest. To use memtest you have to copy it on a floppy dd
   if=/usr/lib/memtest of=/dev/fd0 and to reboot from this floppy.

   If your laptop came with Windows, you may determine a lot of hardware
   settings from the installation. Boot into DOS or Windows to get the
   information you need.

   Using Windows9x/NT to get hardware settings, basically boot Windows,
   then Start -> Settings -> Control Panel -> System -> Device Manager
   and write down everything, or make a hardcopy from the display using
   the <PRINT> key, plus keep a log of settings, hardware, memory, etc.

   Using MS-DOS and Windows3.1x you can use the command msd, which is an
   akronym for MicroSoft Diagnostics. Or you might try one of the
   numerous DOS shareware utilities: CHECK-IT, DR.HARD and others.

   Sometimes it's difficult to know what manufacturer has built the
   machine or parts of it actually. The
   [http://www.fcc.gov/oet/fccid/help.html] FCC "Federal Communications
   Commission On-line Equipment Authorization Database may be used, if
   you are having problems identifying the manufacturer of a laptop or
   notebook computer (or other electronic device,) this site lets you
   search the FCC database based on the FCC ID number you can usually
   find on the equipment if it was marketed in the United States of
   America."

   Many laptops are no more compatible with Windows than Linux. David
   Hinds, author of the PCMCIA drivers, points out that Toshiba
   notebooks use a proprietary Toshiba PCMCIA bridge chip that exhibits
   the same bugs under Windows as under Linux. IBM(TM) Thinkpads have
   serious BIOS problems that affect delivery of events to the power
   management daemon apmd. These bugs also affect MS-Windows, and are
   listed in IBM(TM)'s documentation as considerations.

   Some incompatibilities are temporary, for instance laptops that have
   Intel's USB chip will probably get full USB support, eventually.
     ________________________________________________________________

1.7. Writing a Device Driver

   If you encounter a device which is not yet supported by Linux, don't
   forget it's also possible to write a driver by yourself. You may look
   at the book from Alessandro Rubini, Andy Oram: Linux Device Drivers.
   There is even a free online issue [http://www.oreilly.com/openbook/]
   here .
     ________________________________________________________________

1.8. Buying a Second Hand Laptop

   Some recommendations to check a used laptop, before buying it:

    1. Review the surface of the case for visible damages.
    2. Check the display for pixel faults. Maybe it's useful to take a
       magnifying glass therefore. By the way: There is a standard for
       pixel faults etc. ISO 13406-2.
    3. Do an IO stress-test, .e.g. with the tool bonnie.
    4. You may use memtest and crashme to achieve a memory test.
    5. Do a CPU stress test, e.g. with the command md5sum /dev/urandom
       or by compiling a kernel.
    6. Check the floppy drive by formatting a floppy.
    7. Check the CD/DVD drive by reading and writing a CD/DVD.
    8. To check the battery seems difficult, because it needs some time:
       one charge and one work cycle. You may use battery-stats to do
       so, but note this tool only offer APM support, it is not
       available with ACPI support yet.
    9. To check the surface of the harddisk you may take e2fsck. There
       is also a Linux tool dosfsck or the other fsck tools.
   10. To test the entire disk (non-destructively), time it for
       performance, and determine its size, as root do: time dd
       if=/dev/had of=/dev/null bs=1024k .
   11. Check whether the machine seems to be stolen. I have provided a
       [http://tuxmobil.org/stolen_laptops.html] survey of databases for
       stolen laptops.

   AFAIK there is no Linux tool like the DOS tools CHECK-IT, DR. HARD,
   SYSDIAG and others. These tools include many of the tests in one
   integrated suite. One of the best in my humble opinion is the tool
   [http://members.datafast.net.au/~dft0802/] PC Diagnostics 95 made by
   Craig Hart. Despite the 95 in its name it's plain DOS, tiny ( 76KB
   program and 199KB data) reliable and free. Unfortunately it contains
   no check for the IrDA� port.

   Please note this quotation from the disclaimer: "This program is
   written with the target audience being a trained, experienced
   technician. It is NOT designed to be used by those ignorant of
   computer servicing. Displays are not pretty but functional.
   Information is not explained since we are not trying to educate. This
   software should be considered to be just like any other tool in a
   tech's toolbox. It is to be applied with care, in the right
   situation, in order to find answers to specific problems. If you are
   an end user who is less than confident of dealing with computer
   hardware, this is probably not a program for you."

   Laptop computers, unlike desktop machines, really do get used up.
   Lithium batteries are good for no more than 400 recharge cycles,
   sometimes much fewer. Keyboards wear out. LCD screen backlighting
   grows dim. Mouse buttons fail. Worst of all, connectors get loose as
   a result of vibration, causing intermittent failures (e.g. only when
   you hit the <Enter> key). We have heard of a machine used on the
   table in a train being shaken to unusability in one trip.
     ________________________________________________________________

1.9. No Hardware Recommendations

   It's difficult to give any recommendations for a certain laptop model
   in general. Your personal needs have to be taken into account. Also
   the market is changing very quickly. I guess every three months a new
   generation of laptops (with bigger harddisk space, higher CPU speed,
   more display size, etc.) comes into the market. So I don't give any
   model or brand specific recommendations. But you may check my
   [http://tuxmobil.org/laptop_manufacturer.html] Linux support of
   laptop and notebook manufacturers survey.

   A good way to check Linux hardware compatibility the next time you go
   shopping a laptop is using a [http://www.knoppix.org/] Knoppix
   CD/DVD. The Knoppix hardware detection works quite well and is often
   capable to check all laptop hardware.
     ________________________________________________________________

1.10. Linux Laptop and PDA Vendor Survey

   You may check the [http://tuxmobil.org/reseller.html] Linux Laptop,
   PDA and Mobile Phone Vendor Survey at TuxMobil for a reseller in your
   country. Some of them even sell laptops without Microsoft operating
   systems.

   Often it is difficult to get laptops without a pre-installed
   Microsoft operating system. In case you do not want to use it you may
   read [http://tuxmobil.org/ms_tax.html] some tips and tricks to get
   rid of the Microsoft tax. If you want to buy a recent machine check
   the [http://tuxmobil.org/recent_linux_laptops.html] Linux
   installation reports for recently available laptops and notebooks.
     ________________________________________________________________

Chapter 2. Laptop Distributions

2.1. Requirements

   From the [http://tldp.org/HOWTO/Battery-Powered/]
   Battery-Powered-HOWTO I got this recommendation (modified by WH):

   A Message to Linux Distributors: If you happen to be a Linux
   distributor, thank you for reading all this. Laptops are becoming
   more and more popular, but still most Linux distributions are not
   very well prepared for portable computing. Please make this section
   of this document obsolete, and make a few changes in your
   distribution.

   The installation routine should include a configuration, optimized
   for laptops. The minimal install is often not lean enough. There are
   a lot of things that a laptop user does not need on the road. Just a
   few examples. There is no need for three different versions of vi.
   Some portable systems do not need printing support.

   Don't forget to describe laptop-specific installation problems, e. g.
   how to install your distribution without a CD/DVD-ROM drive.

   Add better power management and seamless PCMCIA support to your
   distribution. Add a recompiled kernel and an alternative set of
   PCMCIA drivers with apm support that the user can install on demand.
   Include a precompiled apmd package with your distribution. Also
   include IrDA� infrared support and USB support.

   Add support for dynamically switching network configurations. Most
   Linux laptops travel between locations with different network
   settings (e. g. the network at home, the network at the office and
   the network at the university) and have to change the network ID very
   often.

   Add a convenient PPP dialer with an address book, that does not try
   to start multiple copies of the PPP daemon if you click on the button
   twice (e.g., the RedHat usernet tool). It would be nice to have the
   PPP dialer also display the connection speed and some statistics. One
   nice command line dialer that autodetects modems and PPP services is
   wvdial from [http://open.nit.ca/] OpenSourceInNitix.

   At TuxMobil you may find a huge number of links to
   [http://tuxmobil.org/mylaptops.html] laptop and notebook Linux
   installation reports. They are ordered by manufacturer and Linux
   distribution. Special categories are available for:

     * [http://tuxmobil.org/debian_linux.html] Debian,
     * [http://tuxmobil.org/gentoo_mobile.html] Gentoo,
     * [http://tuxmobil.org/distribution_linux_laptop_redhat.html]
       RedHat,
     * [http://tuxmobil.org/distribution_linux_laptop_suse.html] SuSE,
     * [http://tuxmobil.org/distribution_linux_laptop_ubuntu.html]
       Ubuntu,
     * [http://tuxmobil.org/distribution_linux_laptop_slackware.html]
       SlackWare,
     * [http://tuxmobil.org/distribution_linux_laptop_mandrake.html]
       Mandrake (Mandriva),
     * [http://tuxmobil.org/mobile_minix.html] Minix and
     * [http://tuxmobil.org/mobile_bsd.html] different kinds of BSD
       flavors.

   Some resources are available in [http://tuxmobil.org/lang.html]
   different languages, e.g.

     * in German [http://tuxmobil.de/] TuxMobil(DE): Linux on Mobile
       Computers
     * in Russian [http://tuxmobil.ru/] TuxMobil(RU): Linux on Mobile
       Computers
     * and in Chinese [http://tuxmobil.cn/] TuxMobil(CN): Linux on
       Mobile Computers.
     ________________________________________________________________

2.2. Recommendation

   The [http://www.debian.org] Debian/GNU Linux has most of the desired
   features for a laptop installation. The distribution has a quite
   flexible installation tool. The installation process is well
   documented, especially concerning the methods which are useful for
   laptops. All the binaries are tiny, because they are stripped. A
   mailing list debian-laptop including a searchable archive is
   provided. And Debian/GNU Linux is free.

   At the end of August 1999 the [http://tuxmobil.org/debian_linux.html]
   Debian Laptop Distribution - Proposal was issued. And some more
   laptop related packages and a Debian meta-package dedicated to
   laptops are on the way.

   Note: I know other Linux distributions work well with laptops, too. I
   even tried some of them, see my pages about certain laptops mentioned
   above.
     ________________________________________________________________

Chapter 3. Installation

3.1. Related Documentation

    1. [http://tldp.org/HOWTO/CDROM-HOWTO/] CDROM-HOWTO
    2. [http://tldp.org/HOWTO/CD-Writing-HOWTO.html] CD-Writing-HOWTO
    3. [http://tldp.org/HOWTO/Config-HOWTO/] Config-HOWTO
    4. [http://tldp.org/HOWTO/Diskless-HOWTO.html] Diskless-HOWTO
    5. [http://tldp.org/HOWTO/Installation-HOWTO/] Installation-HOWTO
    6. [http://tldp.org/HOWTO/Pre-Installation-Checklist/index.html]
       Pre-Installation-Checklist-HOWTO
    7. [http://tldp.org/HOWTO/Update.html] Update-HOWTO
    8. [http://tldp.org/HOWTO/Hard-Disk-Upgrade/]
       Hard-Disk-Upgrade-HOWTO
    9. [http://www.tldp.org/LDP/gs/gs.html] Linux Installation and
       Getting Started
   10. [http://www.debian.org/releases/stable/i386/install] Installing
       Debian/GNU Linux For Intel x86
   11. [http://tldp.org/HOWTO/Install-From-ZIP.html]
       Install-From-Zip-HOWTO
   12. [http://tldp.org/HOWTO/ZIP-Drive.html] ZIP-Drive-HOWTO
     ________________________________________________________________

3.2. Prerequisites - BIOS, Boot Options, Partitioning

3.2.1. BIOS

   When starting a fresh installation you should try with standard BIOS
   options. If something doesn't work you should try to modify BIOS
   options. For example a well known trouble maker is the Plug-and-Play
   - PnP option (which comes with different names). See also the BIOS
   section in the hardware section below.
     ________________________________________________________________

3.2.2. Boot Options

   There are many boot options, which have effects on the behavior of
   laptops, e.g. apm=on|off and acpi=on|off: For details see
   [http://tldp.org/HOWTO/BootPrompt-HOWTO.html] BootPrompt-HOWTO and
   the Kernel documentation in
   /usr/src/linux/Documentation/kernel-parameters.txt .
     ________________________________________________________________

3.2.3. Partitioning

   Partitioning can be done in a very sophisticated way. Currently I
   have only some first thoughts. I assume that with laptops there are
   still some reasons (e.g. updating the firmware of PCMCIA cards and
   BIOS) to share Linux and Windows9x/NT. Depending on your needs and
   the features of your laptop you could create the following
   partitions:

     * BIOS, some current BIOSes use a separate partition, for instance
       COMPAQ notebooks
     * suspend to disk, some laptops support this feature
     * swap space Linux
     * swap space Windows9x/NT
     * Linux base
     * Linux /home for personal data (please consider an encrypted
       partition for security reasons, for details about encryption see
       the according chapter below)
     * common data between Linux and Windows9x/NT
     * small (~32MB) boot partition for yaBoot (Linux/PPC boot loader),
       in HFS MacOS Standard format.

   Note this chapter isn't exhausting yet. Please read the appropriate
   HOWTOs first, e.g. the [http://tldp.org/HOWTO/Partition/]
   Partition-HOWTO .
     ________________________________________________________________

3.3. Linux Tools to Repartition a Hard Disk

3.3.1. GNU parted

   [http://www.gnu.org/software/parted] GNU parted allows you to create,
   destroy, resize and copy partitions. It currently supports ext2 and
   fat (fat16 and fat32) filesystems, Linux swap partitions, and MS-DOS
   disklabels, as well as Macintosh and PC98. For NTFS file systems see
   [http://mlf.linux.rulez.org/mlf/ezaz/ntfsresize.html] ntfsresize .
     ________________________________________________________________

3.3.2. ext2resize

   [http://ext2resize.sourceforge.net/] ext2resize is a program capable
   of resizing (shrinking and growing) ext2 and ext3 filesystems. Checks
   whether the new size the user gave is feasible (i.e. whether the
   filesystem isn't too occupied to shrink it), connected to the parted
   project.
     ________________________________________________________________

3.3.3. fixdisktable

   Something was recently published on the
   <linux-kernel_at_vger.rutgers.edu> mailing list about a partition
   recovery program. I have neither used , nor examined, nor read much
   about it (except for the HTML page.) It may be useful to some of you
   if you have problems with [http://www.igd.fhg.de/~aschaefe/fips/]
   FIPS , Ranish Partition Manager/Utility or Partition Magic destroying
   your partition information. You can find information on this
   partition-fixer named "fixdisktable" at
   [http://bmrc.berkeley.edu/people/chaffee/fat32.html] his pages. It is
   quite a ways down in that page. Or look for it
   [ftp://bmrc.berkeley.edu/pub/linux/rescue/] via ftp and locate the
   latest "fixdisktable" in that FTP directory. (Source and binary dist
   should be available.)
     ________________________________________________________________

3.3.4. Caveats

   Before repartitioning your hard disk take care about the disk layout.
   Especially look for hidden disk space or certain partitions used for
   suspend to disk or hibernation mode. Some laptops come with a
   partition which contains some BIOS programs (e.g. COMPAQ Armada
   1592DT). Search the manual carefully for tools like PHDISK.EXE,
   Suspend to Disk, Diagnostic TOOLS.

   [http://www.procyon.com/~pda/lphdisk/] Patrick D. Ashmore has
   recently released a Linux utility to prepare hibernation partitions
   for use with laptops and notebooks using Phoenix NoteBIOS. "This
   utility isn't needed to utilize the APM "Suspend-To-Disk" feature ...
   if you already have a valid hibernation partition, you should be able
   to use it from any operating system that can handle APM suspends.

   However, if one ever upgrades hard drive, memory, or repartitions
   their hard drive, they discover that they either have to do without
   the suspend-to-disk feature or boot to DOS and use the PHDISK.EXE
   program provided with their laptop or directly from Phoenix
   Technologies.

   Now, Linux users are free from this restriction. lphdisk is a Linux
   utility that properly prepares these partitions for use. Not only
   does this eliminate having to boot to DOS, but my utility does not
   exhibit some of the nastier bugs that its DOS counterpart has."

   Please see chapter DOS Tools to Repartition a Hard Disk, too.
     ________________________________________________________________

3.3.5. Multi Boot

   Please see the chapter chapter Chapter 15 Different Environments, for
   information about booting different operating systems from the same
   harddisk.
     ________________________________________________________________

3.4. Laptop Installation Methods



   There's More Than One Way To Do It - TMTOWTDI
     Larry Wall, Tom Christiansen & Randal L. Schwartz: Programming
   Perl, Sec. Ed. 1996 p. 10

   From the [http://tldp.org/HOWTO/Battery-Powered/]
   Battery-Powered-HOWTO : "Installing and using Linux on a laptop is
   usually no problem at all, so go ahead and give it a try. Unlike some
