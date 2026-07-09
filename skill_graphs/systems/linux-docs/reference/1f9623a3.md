   of mobile devices running Linux: laptops, notebook, PDAs, handheld
   PCs, mobile phones, wearables and more. Though sometimes you have to
   make the appropriate changes.
     ________________________________________________________________

12.2. BIOS

   Before setting up any hardware you should have a look into the BIOS.
   Often you may find a solution already there, e.g. options to set up
   the display, APM or ACPI, DMA, IrDA, PCMCIA, sound, SpeedStep, and
   more.

   If you run into unresolvable trouble when configuring the hardware,
   try a BIOS upgrade from the manufacturer. For this task you usually
   need one of the Microsoft so-called operating systems. Or at least a
   DOS disk or CD.

   Flashing BIOSes has become often quite complex as both DOS and
   floppies are fading away. Things aren't any easier when running
   exclusively GNU/Linux. Luckily, it is possible to
   [http://freshrpms.net/docs/bios-flash/] create a bootable CD-ROM with
   GNU/Linux, which enables one to actually flash a BIOS using a DOS
   utility without requiring Windows, MS-DOS or a floppy drive.

   Some newer laptops e.g. ASUS M5200A are equipped with a BIOS, which
   is able to update itself.

   The [http://www.nenie.org/misc/flashbootcd.html] Motherboard Flash
   Boot CD from Linux Mini HOWTO gives a short summary of how to create
   a boot disk to flash a BIOS on a PC, from Linux (or another Unix)
   when one has no floppy drive and no access to a DOS/Windows machine.

   [http://www.linuxbios.org] LinuxBIOS aims to replace the normal BIOS
   found on PCs, Alphas, and other machines with a Linux kernel that can
   boot Linux from a cold start. LinuxBIOS is primarily Linux - about 10
   lines of patches to the current Linux kernel. Additionally, the
   startup code - about 500 lines of assembly and 5000 lines of C -
   executes 16 instructions to get into 32-bit mode and then performs
   DRAM and other hardware initialization required before Linux can take
   over. There are even two reports about LinuxBIOS on laptops.

   Alternative approaches are [http://openbios.org/] OpenBIOS and
   [http://freebios.sourceforge.net/] FreeBIOS.
     ________________________________________________________________

12.2.1. SMBios

   [http://www.dmtf.org/standards/dmi/] Desktop Management Interface
   (DMI) Standards generate a standard framework for managing and
   tracking components in a desktop pc, notebook or server. DMI was the
   first desktop management standard. The DMI Home Page is a repository
   of all DMI-related information from the specification to tools to
   support to the Product Registry of DMI-certified products.

   [http://www.nongnu.org/dmidecode/] Dmidecode reports information
   about your system's hardware as described in your system BIOS
   according to the SMBIOS/DMI standard (see a sample output). This
   information typically includes system manufacturer, model name,
   serial number, BIOS version, asset tag as well as a lot of other
   details of varying level of interest and reliability depending on the
   manufacturer. This will often include usage status for the CPU
   sockets, expansion slots (e.g. AGP, PCI, ISA) and memory module
   slots, and the list of I/O ports (e.g. serial, parallel, USB).

   There is also an alternative implementation of a DMI table decoder.
   [http://linux.dell.com/libsmbios/main/index.html] Libsmbios is a
   cross-platform library intended to be used to obtain common
   information available in a BIOS using a unified API. Currently, it
   can programmatically access any information in the SMBIOS tables. It
   also has the ability to obtain Dell system-specific information such
   as the Dell System ID number, service tag, and asset tag. Future
   plans include APIs for $PIR and mptable mapping. There is a C API for
   some of the more commonly used functions, and example binaries to
   show off most of the facilities.
     ________________________________________________________________

12.3. CPU

   You may find a survey about CPUs used in mobile devices, which are
   Linux-supported in the chapter Chapter 1 Which Laptop to Buy? above.
     ________________________________________________________________

12.3.1. SpeedStep

   Speedstep is a feature of recent CPUs made by Intel, which lets you
   set CPU frequency. There are different Linux tools to get this to
   work. Similar features are also available for other CPUs from AMD or
   the StrongARM CPU, I will describe this in a later issue (assistance
   welcome).

   Before configuring SpeedStep have a look into the BIOS options.
     ________________________________________________________________

12.3.1.1. SpeedStep Tool

   The [http://www.goof.com/pcg/marc/speedstep.html] SpeedStep tool
   works with Mobile Pentium-III CPUs only. See output from cat
   /proc/cpuinfo:
   model name : Intel(R) Pentium(R) III Mobile CPU 1000MHz

   It does not work with the mobile version of the Pentium-III:
   model name : Pentium III (Coppermine)
     ________________________________________________________________

12.3.1.2. CPUFREQ

   You might want to check into the
   [http://www.kernel.org/pub/linux/utils/kernel/cpufreq/cpufreq.html]
   cpufreq patch for the linux-2.4/2.5 kernels: CPU clock frequency
   scaling for Linux, on x86 and ARM based processors. This module
   provides a user-space and standard kernel-space interface to this
   feature, along ARM system-on-a-chip devices to cope with processor
   clock changes. Since the power consumed by a processor is directly
   related to the speed at which it is running, keeping the clock speed
   as low as possible allows you to get more run-time out of your
   battery. Some people use this to adjust their clock speed many times
   a second to optimise performance vs battery life. See also the
   [http://www.arm.linux.org.uk/cvs/] CVS repository .
     ________________________________________________________________

12.3.1.2.1. cpufreqd

   [http://www.sf.net/projects/cpufreqd] cpufreqd is meant to be a
   replacement of the speedstep applet you can find on some other
   operating systems, it monitors battery level, AC state and running
   programs and adjusts the frequency governor according to a set of
   rules specified in the config file. It works both with APM and ACPI.
     ________________________________________________________________

12.3.1.2.2. cpudyn

   [http://mnm.uib.es/~gallir/cpudyn/] cpudyn controls the speed in
   Intel SpeedStep and PowerPC machines with the cpufreq compiled in the
   kernel. It saves battery and lowers temperature, without affecting
   the performance of interactive applications.
     ________________________________________________________________

12.3.1.2.3. cpuspeedy

   [http://cpuspeedy.sourceforge.net] cpuspeedy allows you to change the
   clock speed and voltage of CPUs using Linux's CPUFreq driver. It is a
   user space program, so it will work on every processor supported by
   the kernel's CPUFreq driver.
     ________________________________________________________________

12.3.1.2.4. powernowd

   [http://www.deater.net/john/powernowd.html] PowerNowd is a simple
   client daemon for the Linux cpufreq driver using the sysfs interface.
   It sits in the background and changes CPU speed in configurable
   "steps" according to usage. Written in C, its emphasis is on speed
   and simplicity. It is very configurable, and supports non-x86 and SMP
   systems.
     ________________________________________________________________

12.3.1.3. Laptop Mode

   [http://samwel.tk/laptop_mode/] Laptop mode is a kernel "mode" that
   allows you to extend the battery life of your laptop. It does this by
   intelligently grouping write activity on your disks, so that only
   reads of uncached data result in a disk spinup. It has been reported
   to cause a significant improvement in battery life (for usage
   patterns that allow it).

   The [http://samwel.tk/laptop_mode/] Laptop Mode Tools package spins
   down your hard drive like noflushd, but it works also on journalling
   filesystems. It integrates with apmd/acpid/pbbuttonsd to enable this
   behaviour only when you are running on battery power. It also adjusts
   some hdparm settings and remounts your filesystems noatime, and it
   can adjust your maximum CPU frequency.
     ________________________________________________________________

12.3.1.4. SONY VAIO SPIC Daemon

   The [http://spicd.raszi.hu/] SONY VAIO SPIC daemon is a fast and
   small hack to create a working apmd to Sony VAIO laptops. It uses the
   sonypi kernel module to detect the AC adapter status and the LCD
   backlight, and cpufreq for CPU frequency scaling.
     ________________________________________________________________

12.3.1.5. CPUIDLE

   A [http://www.heatsink-guide.com/cpuidle.htm] software utility that
   will make your CPU run cooler? Sounds pretty strange, huh? Let me
   explain: Have you ever thought of the fact that your CPU is idle most
   of the time when you're using your computer? For example, when you're
   using your word processor, writing emails, browsing the web, the CPU
   does nothing else than just wait for user input. In fact, it will use
   up to 30W and produce substantial amounts of heat doing nothing. Good
   operating systems, like Linux, NT and OS/2 have a so-called "idle
   loop" - a loop that's always executed when the CPU has nothing to do.
   This loop consists of halt (HLT) instructions. CPUs like the AMD K6,
   the Cyrix 6x86 and 6x86MX have a special feature called
   "suspend-on-halt". This means that every time the CPU executes a hlt
   instruction, it will go into "suspend mode" for a short time. So,
   while the idle loop is being executed, the CPU will be in suspend
   mode, use much less power, and stay much cooler. Of course, this does
   not affect performance at all! The user won't even notice that his
   CPU is in suspend mode most of the time (unless he touches the
   heatsink).
     ________________________________________________________________

12.3.1.6. ACPI

   If you have enabled ACPI support in the Kernel you may also set the
   SpeedStep parameters via the /proc/apci/ interface, e.g. echo 1 >
   /proc/acpi/processor/CPU0/performance will make the CPU speed down.
   Note: the spaces in the command are important! Note also: this
   feature is deprecated for Kernel > 2.6.11. Or use this script
   provided by Sebastian Henschel.
#! /bin/sh

# /etc/init.d/slowcpu: slow down cpu or accelerate it via speedstep

test -e /proc/acpi/processor/CPU0/performance || exit 0

case "$1" in
    start)
    echo "Setting CPU0-Speed to: 733 MHz."
    echo 1 > /proc/acpi/processor/CPU0/performance
        ;;
    stop)
    echo "Setting CPU0-Speed to: 1133 MHz."
    echo 0 > /proc/acpi/processor/CPU0/performance
        ;;
    force-reload|restart)
        ;;

    *)
        echo "Usage: $0 {start|stop}"
        exit 1
esac

exit 0
     ________________________________________________________________

12.4. Centrino(tm), Centrino-Duo(tm)

   Intels Centrino(TM) technology consists of three parts: a Pentium M
   processor, a chipset, and a wireless module. Let's see how these
   parts are supported under Linux so far.

   Here you may find current information about
   [http://tuxmobil.org/centrino.html] Linux on Centrino laptops and
   notebooks.
     ________________________________________________________________

12.4.1. CPU: Pentium-M

   Robert Freund has written a concise [http://rffr.de/acpi] HOWTO about
   controlling ACPI Centrino(TM) features via software in Linux. He
   describes how to control CPU frequency and other energy saving modes,
   as well as how to get information about the battery state.
     ________________________________________________________________

12.4.2. Chipset: 855/915

   The Intel 855/915 chipset families are designed to deliver better
   performance at lower power. The chipsets are available as discrete
   memory controller hub (e.g. Intel 855PM). Or as an integrated
   graphics and memory controller hub (e.g. Intel 855GM). Intel provides
   the Extreme Graphics driver for Linux, which includes AGP GART and
   DRM kernel modules as a binary files. I have no experience with this
   drivers, because the chipsets work with XFree86/X.org drivers, too.
   The Pentium-M CPU may come accompanied with other graphics chipsets
   too, e.g. from ATI, nVIDIA or Trident.
     ________________________________________________________________

12.4.3. Wireless LAN: PRO/wireless 2100/2200 LAN Mini-PCI Adapter

   There are different solutions to get these cards running with Linux:
   drivers from Intel, NDIS wrapper and Linuxant driverloader
   (commercial).

   [http://ipw2100.sourceforge.net/] ipw2100, Intel's Open Source driver
   with included firmware, for the first Centrino generation (incl. WEP
   and WPA together with HostAP). For the second generation of Intel's
   miniPCI modules: PRO/Wireless 2200BG (802.11g/802.11i), the
   [http://ipw2200.sourceforge.net/] ipw2200 project provides a driver.
   Third generation PRO/Wireless 2915ABG (IEEE 802.11b, 802.11g und
   802.11a) miniPCI cards will be supported by the
   [http://ipw2200.sourceforge.net/] ipw2200 project, too.

   Intel didn't provide drivers, when the begun to sell their Centrino
   technology. During this time there have been other solutions: Some
   vendors refuse to release technical specifications or even a binary
   Linux driver for their WLAN cards. NDIS wrapper tries to solve this
   by making a kernel module that can load NDIS (Microsoft-Windows
   Network Driver Interface Specification) drivers. Currently there are
   two implementations available. The commercial
   [http://www.linuxant.com/driverloader/] Linuxant Driverloader
   supports a broad range of chipsets including Intel's PRO/Wireless
   2100 LAN Mini-PCI Adapter. There is also
   [http://ndiswrapper.sourceforge.net/] ndiswrapper an Open Source
   solution by Pontus Fuchs.

   As another workaround was the usage of a Linux-supported
   [http://tuxmobil.org/minipci_linux.html] miniPCI WLAN card. These
   cards are difficult to get, but some desktop WLAN PCI cards contain
   miniPCI cards. Often it is a tedious task to build them into a
   laptop. Kernel maintainer Theodore Tytso has written a
   [http://www.thunk.org/tytso/linux/t40.html] manual about achieving
   this task. You may also use a wireless PCMCIA or CF card instead.
   This solution may provide more flexibility, because you may use a
   PCMCIA or CF card in different devices and choose the Linux driver of
   your choice. You may also extend the wireless range by adding
   antennas to some cards. For Linux compatibility there is the
   [http://tuxmobil.org/pcmcia_linux.html] TuxMobil PCMCIA/CF Card
   Survey. In the future, manufacturers will probably offer alternative
   miniPCI solutions. DELL is already doing so for their Latitude D
   series.
     ________________________________________________________________

12.4.4. Conclusion

   Though Linux support is not yet complete, some features of the
   Centrino(TM) technology already make it worthwhile to take into
   account when buying your next laptop. Though the new CPUs are named
   so similarly to existing ones that some people mix them up, they are
   completely different inside. Compared to the Pentium-4 Mobile CPU,
   the Pentium-M will allow a smaller form factor for laptops, making
   them more portable and lighter. Because of their higher clockspeed,
   the Pentium-4 CPUs have produced too much heat to build them into
   slimline notebook cases. Therefore, very flat notebooks have only
   been available from Apple or with a Pentium III Mobile CPU. Also, the
   battery power the Pentium-M consumes for a given level of performance
   will decrease, but I do not have a benchmark about how much the
   savings actually are yet. PENN Computing offers a nice
   [http://www.upenn.edu/computing/provider/docs/centrinoprovider.html]
   comparison of Pentium-M and Pentium-4 Mobile. Note: The character M
   in Pentium-M suggests "mobile". Therefore some people mix this kind
   of CPU with the mobile versions of the Pentium-III/Pentium-4 CPU.

   Laptops based on the Centrino(TM) features are already very popular
   in the Linux community. [http://tuxmobil.org/centrino.html]
   Installation reports for almost all Centrino based laptops available
   at TuxMobil.
     ________________________________________________________________

12.5. PCMCIA Controller

12.5.1. Linux Compatibility Check

   With the probe command, which is included in the PCMCIA-CS package by
   David Hinds you can get the type of the PCMCIA controller. Also
   available by the command cat /proc/pci.
     ________________________________________________________________

12.5.2. Related Documentation

    1. PCMCIA-HOWTO
     ________________________________________________________________

12.5.3. PCMCIA Configuration - Survey

   In the mailing lists where I'm a member, the question "How can I set
   up PCMCIA support, after the Linux installation?" comes up sometimes.
   Therefore I try to give a short survey. But the authoritative source
   for the latest information about the PCMCIA Card Services for Linux,
   including documentation, files, and generic PCMCIA information is the
   Linux PCMCIA Information Page . For problems with PCMCIA and APM see
   the chapter APM.
     ________________________________________________________________

12.5.3.1. Software

    1. Install the newest available PCMCIA-CS package, if you take a rpm
       or deb package it is quite easy.
    2. Read the PCMCIA HOWTO, usually included in the PCMCIA-CS package.
    3. If necessary, install a new kernel.
    4. Make sure your kernel has module support and PCMCIA support
       enabled (and often APM support)
    5. Make sure your kernel also includes support for the cards you
       want to use, e.g. network support for a NIC card, serial support
       for a modem card, SCSI support for a SCSI card and so on.
    6. If you have a custom made kernel, don't forget to compile the
       PCMCIA-CS source against your kernel.
     ________________________________________________________________

12.5.3.2. PCMCIA Controller

    1. Use the probe command to get information whether your PCMCIA
       controller is detected or not.
    2. Edit the file /etc/sysconfig/pcmcia. It should include PCMCIA=y
       and the type of your PCMCIA controller, e.g. PCIC=i82365. Since
       Kernel 2.6 there is a standard driver PCIC=yenta_socket.
    3. Start the PCMCIA services typically via /etc/init.d/pcmcia start.
       If you get two high beeps, everything should be fine.
    4. If something doesn't work, check the messages in
       /var/log/messages .
     ________________________________________________________________

12.5.3.3. PCMCIA Card

    1. Check your card with cardctl ident .
    2. If your card is not in /etc/pcmcia/config, edit the file
       /etc/pcmcia/<MYCARD>.conf appropriately. Take an entry in the
       first file as a model. You may try every driver, just in case it
       might work, for instance the pcnet_cs supports many NE2000
       compatible PCMCIA network cards. Note: it is a bad practice to
       edit /etc/pcmcia/config directly, because all changes will be
       lost with the next update.
    3. A list of supported cards is included in the PCMCIA-CS package.
       The current list you may find at
       [http://pcmcia-cs.sourceforge.net/ftp/SUPPORTED.CARDS]
       SUPPORTED.CARDS.
       Since there are not all cards mentioned I have set up a PCMCIA
       Cards Survey of Cards Supported by Linux .
    4. If you use a X11 GUI, you can use cardinfo to insert, suspend, or
       restart a PCMCIA card via a nice graphical interface.

   Figure 12-1. Screenshot of cardinfo

   [cardinfo.png]
     ________________________________________________________________

12.6. Graphics Chip

12.6.1. Linux Compatibility Check

12.6.1.1. Video Mode

   Attention: The SuperProbe is deprecated. The tool SuperProbe is part
   of XFree86 and is able to check many graphics chips. Please read the
   documentation carefully, because it might crash your hardware. From
   man SuperProbe:

   "SuperProbe is a program that will attempt to determine the type of
   video hardware installed in an EISA/ISA/VLB-bus system by checking
   for known registers in various combinations at various locations
   (MicroChannel and PCI machines may not be fully supported; many work
   with the use of the -no_bios option). This is an error-prone process,
   especially on UNIX (which usually has a lot more esoteric hardware
   installed than MS-DOS system do), so SuperProbe may likely need help
   from the user.

   At this time, SuperProbe can identify MDA, Hercules, CGA, MCGA, EGA,
   VGA, and an entire horde of SVGA chipsets (see the -info option,
   below). It can also identify several HiColor/True-color RAMDACs in
   use on SVGA boards, and the amount of video memory installed (for
   many chipsets). It can identify 8514/A and some derivatives, but not
   XGA, or PGC (although the author intends to add those capabilities).
   Nor can it identify other esoteric video hardware (like Targa, TIGA,
   or Microfield boards).":

   For testing reasons start the X11 server with X 2> <error.msg>. And
   try to change the resolution by typing <CTL><ALT><+> or
   <CTL><ALT><->. Note: the + or - sign have to be taken from the
   numeric pad, which can be emulated at the letter pad or with the Fn
   key by some laptops.
     ________________________________________________________________

12.6.1.2. Text Mode

   Just watch the display and determine if it works properly. If not,
   try to enable different video modes at startup time. Setting up X11
   can sometimes be an exercise in trial and error.
     ________________________________________________________________

12.6.2. Related Documentation

    1. First of all the [http://www.xfree86.org/] XFree86 documentation
       itself. Often locally available at /usr/share/doc/xfree86*. Or
       the [http://x.org/] X.Org documentation.
    2. [http://tldp.org/HOWTO/XFree86-HOWTO/] XFree86-HOWTO
    3. [http://tldp.org/HOWTO/XFree86-Video-Timings-HOWTO/]
       XFree86-Video-Timings-HOWTO
    4. [http://tldp.org/HOWTO/XFree86-XInside.html]
       XFree86-XInside-HOWTO
    5. [http://tldp.org/HOWTO/X-Big-Cursor.html] X-Big-Cursor-mini-HOWTO
       (useful when running X11 on a notebook with low contrast LCD)
    6. [http://tldp.org/HOWTO/Keyboard-and-Console-HOWTO.html]
       Keyboard-and-Console-HOWTO
    7. [http://tldp.org/HOWTO/Framebuffer-HOWTO.html] Framebuffer-HOWTO
     ________________________________________________________________

12.6.3. Survey X11-Servers

   You might discover that some features of your laptop are not
   supported by [http://www.xfree86.org/] XFree86 or [http://x.org/]
   X.Org. , e.g. high resolutions, accelerated X or an external monitor.
   Therefore I give a survey of available X11 servers.

    1. [http://www.xfree86.org/] XFree86
    2. [http://x.org/] X.Org.
    3. VESA Frame-Buffer-Device, available with 2.2.x kernels and
       XFree86 3.3.2 or greater. See [http://linux-fbdev.org/] FBDev.ORG
       and [http://www.strusel007.de/linux/fb.html] FB FAQ and kernel
       source /usr/src/linux/Documentation .
       Please check the latest release of [http://directfb.org/]
       DirectFB for a dedicated Framebuffer Driver for the NeoMagic chip
       and other chipsets, with support for acceleration. DirectFB is a
       thin library that provides developers with hardware graphics
       acceleration, input device handling and abstraction, an
       integrated windowing system with support for translucent windows
       and multiple display layers on top of the Linux framebuffer
       device. It is a complete hardware abstraction layer with software
       fallbacks for every graphics operation that is not supported by
       the underlying hardware.
    4. [http://www.xig.com/] Xi Graphics , commercial, also known under
       their former names AcceleratedX or Xinside.
    5. [http://www.scitechsoft.com/] SciTech, commercial.
    6. [http://www.metrolink.com/] Metro-X, commercial.

   If you can't get an appropriate X11 server working, but cannot afford
   a commercial X11 server you may try the VGA16 or the mono server
   included in XFree86.
     ________________________________________________________________

12.6.4. Resources

   You may find a survey about current graphics chips used in laptops
   and notebooks at TuxMobil.
     ________________________________________________________________

12.6.5. External Monitors: LCD, CRT, TV, Projector

   There are several different methods to activate support for an
   external monitor: as a BIOS option or during runtime with a keystroke
   e.g. <Fn>+<F4>.

   Read the X11 docs about your graphics chip carefully, for instance
   for the NeoMagic NM20xx chips you have to edit /etc/XF86Config by
   configuring intern_disp and extern_disp. Note: As far as I know these
   options are only valid for XFree86 3.3.x, for XFree86 4.x I couldn't
   find a similar option.

   If you can't get the external monitor to work with XFree86, try a
   demo version of the commercial X11 servers mentioned above. Also
   check with the RedHat and SuSE WWW sites as they may have new,
   binary-only, X11 servers that may work with your laptop. Or check X11
   servers from [http://x.org/] X.Org.
