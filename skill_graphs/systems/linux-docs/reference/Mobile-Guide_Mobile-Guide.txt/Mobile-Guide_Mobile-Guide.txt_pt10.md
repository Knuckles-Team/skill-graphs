     * PS/2 mouse: works, but for 2.6 Kernels you have to specify the
       right mouse protocol psmouse_proto=imps (if psmouse is compiled
       as a module).
     * serial port: tested with serial mouse, doesn't seem to work,
       /dev/ttyUSB0 was assigned
     * parallel port: tested, device /dev/usb/usblp0 assigned, works
       e.g. with HP LaserJet 2100
     * LAN: usbnet loads, device eth1 was assigned, ifconfig or pump
       configures the network device
     * transfer port aka host link: works with usbnet module, use
       ifconfig usb0 to configure the network interface, (USB 1.1 host
       link B-type) untested

   Here is the output of dmesg for the Typhoon port replicator:
hub 1-0:1.0: new USB device on port 1, assigned address 26
hub 1-1:1.0: USB hub found
hub 1-1:1.0: 4 ports detected
hub 1-1:1.0: new USB device on port 3, assigned address 27
hub 1-1.3:1.0: USB hub found
hub 1-1.3:1.0: 4 ports detected
hub 1-1:1.0: new USB device on port 4, assigned address 28
eth1: register usbnet at usb-0000:00:07.2-1.4, ASIX AX8817x USB 2.0 Ethernet
hub 1-1.3:1.0: new USB device on port 1, assigned address 29
usb0: register usbnet at usb-0000:00:07.2-1.3.1, Prolific PL-2301/PL-2302
hub 1-1.3:1.0: new USB device on port 2, assigned address 30
drivers/usb/class/usblp.c: usblp0: USB Bidirectional printer dev 30 if 0 alt 1
 proto 2 vid 0x067B pid 0x2305
hub 1-1.3:1.0: new USB device on port 3, assigned address 31
pl2303 1-1.3.3:1.0: PL-2303 converter detected
usb 1-1.3.3: PL-2303 converter now attached to ttyUSB0 (or usb/tts/0 for devfs
)
hub 1-1.3:1.0: new USB device on port 4, assigned address 32
HID device not claimed by input or hiddev
hid: probe of 1-1.3.4:1.0 failed with error -5
input: Composite USB PS2 Converter USB to PS2 Adaptor  v1.09 on usb-0000:00:07
.2-1.3.4
HID device not claimed by input or hiddev
hid: probe of 1-1.3.4:1.1 failed with error -5
input: Composite USB PS2 Converter USB to PS2 Adaptor  v1.09 on usb-0000:00:07
.2-1.3.4
     ________________________________________________________________

12.25. Network Connections

12.25.1. Related Documentation

    1. [http://tldp.org/HOWTO/PLIP.html] PLIP-mini-HOWTO
    2. [http://tldp.org/HOWTO/NET3-4-HOWTO.html] Networking-HOWTO
    3. [http://tldp.org/HOWTO/Ethernet-HOWTO.html] Ethernet-HOWTO
     ________________________________________________________________

12.25.2. Connection Methods

   Almost all recent laptops are equipped with a built-in network card.
   This chapter shows some methods to connect older laptops without
   internal network cards.
     ________________________________________________________________

12.25.2.1. PCMCIA Network Card

   If your laptop supports PCMCIA this is the easiest and fastest way to
   get network support. Make sure your card is supported before buying
   one.
     ________________________________________________________________

12.25.2.2. Serial Null Modem Cable

   Probably the cheapest way to connect your laptop to another computer,
   but quite slow. You may use PPP or SLIP to start the connection.
     ________________________________________________________________

12.25.2.3. Parallel Port NIC (Pocket Adaptor)

   [http://www.unix-ag.uni-siegen.de/~nils/accton_linux.html] Accton
   Pocket Ethernet and Linux This ethernet adaptor uses a parallel port
   and delivers approximately 110k Bytes/s throughput for those
   notebooks that do not have PCMCIA slots.
     ________________________________________________________________

12.25.2.4. Parallel "Null" Modem Cable

   Offers more speed than a serial connection. Some laptops use chipsets
   that will not work with PLIP. Please see
   [http://tldp.org/HOWTO/PLIP.html] PLIP-HOWTO for details.
     ________________________________________________________________

12.25.2.5. Docking Station NIC

   I don't have experience with a NIC in a docking station yet.
     ________________________________________________________________

12.25.3. Wake-On-LAN

   Wake-On-LAN works with some laptops equipped with built-in network
   cards. [http://www.scyld.com/wakeonlan.html] Wake-On-LAN is the
   generic name for the AMD "Magic Packet" technology. It's very similar
   to the PCMCIA modem "wake on ring" signal line. The basic idea is
   that the network adapter has a very-low-power mode to monitor the
   network for special packet data that will wake up the machine. The
   [http://www.scyld.com/wakeonlan.html] etherwake package as well as
   the [http://gsd.di.uminho.pt/jpo/software/wakeonlan/] Wakeonlan Perl
   script are able to send 'magic packets' to wake-on-LAN enabled
   ethernet adapters and motherboards, in order to switch on remote
   computers. You may use ethtool to configure some special Wake-On-LAN
   settings.
     ________________________________________________________________

12.26. Built-In Modem

12.26.1. Modem Types

   There are three kinds of modems available: internal, PCMCIA card or
   external serial port modems. But some internal modems will not work
   with Linux these modems are usually called WinModem. This is caused
   by non-standard hardware. So you have to use either a PCMCIA card
   modem or an external modem (serial or USB). The
   [http://walbran.org/sean/linux/linmodem-howto.html] LinModem-HOWTO by
   Sean Walbran provides a detailed instruction how to deal with these
   kind of modems. My pages about [http://tuxmobil.org/modem_linux.html]
   Internal Modems in Laptops and
   [http://tuxmobil.org/minipci_linux.html] miniPCI Devices in Laptops
   provide a survey about the modem controllers used in different
   laptops.

   Quotation from the Kernel-FAQ: "9.Why aren't WinModems supported?
   (REG, quoting Edward S. Marshall) The problem is the lack of
   specifications for this hardware. Most companies producing so-called
   WinModems refuse to provide specifications which would allow
   non-Microsoft operating systems to use them. The basic issue is that
   they don't work like a traditional modem; they don't have a DSP, and
   make the CPU do all the work. Hence, you can't talk to them like a
   traditional modem, and you -need- to run the modem driver as a
   realtime task, or you'll have serious data loss issues under any kind
   of load. They're simply a poor design."

   "Win modems are lobotomized modems which expect Windows to do some of
   their thinking for them. If you do not have Windows, you do not have
   a connection. "

   Anyway, I have set up a page collecting information on laptops with
   internal modems at [http://tuxmobil.org/hardware.html] TuxMobil -
   Hardware . Maybe it's possible to run such modems with
   MS-Windows9x/NT emulators like wine or VMware, but I don't know it.

   The [http://linmodems.org] Linux WinModem Support and
   [http://www.xmodem.org/] the Xmodem.org (former Gromit Winmodem) page
   are more or less the standard as to whether a modem is real or not,
   and also contain directions to getting drivers for the few winmodems
   that do have Linux drivers.

   There is a driver for Lucent WinModems available. LucentPCI (binary
   only) driver, for PCI driven internal modems, see
   [http://linmodems.org] Linux WinModem Support and the
   [http://www.close.u-net.com/ltmodem.html] LTModem diagnostic tool.
     ________________________________________________________________

12.26.2. Caveats

   Warning

   Pay attention to the different kinds of phone lines: analog and ISDN.
   You can't connect an analog modem to an ISDN port and vice versa.
   Though there might be hybrid modems available. Connecting to the
   wrong port may even destroy your modem. Trick: If you are looking for
   an analog phone port in an office building which is usually wired
   with ISDN, take a look at the fax lines, they are often analog lines.

   Warning

   If your machine features an internal modem as well as an internal
   ethernet card, pay also attention to plug the right cable into the
   plug. Otherwise you may damage your hardware easily. It may even
   cause a fire.

   For tracking the packets on PPP you may use pppstats. Or pload this
   provides a graphical view of the traffic (in and out) of the PPP
   connection. It is based on athena widgets hence is very portable. It
   also uses very little CPU time.
     ________________________________________________________________

12.27. GPRS

   GPRS is a General Packet Radio Service, an add-on to GSM and TDMA
   cellular telephone standards used all over the world. It allows
   (almost) always-on Internet connections using GSM (or TDMA)
   telephones. It makes mobile internet usage on laptops fairly
   inexpensive. The [http://turtiainen.dna.fi/GPRS-HOWTO] GPRS-HOWTO is
   written by Esa Turtianen etu_AT_dna.fi and Jari Arkko
   Jari_AT_arkko.com
     ________________________________________________________________

12.28. SCSI

12.28.1. Linux Compatibility Check

   If unsure about the right SCSI support, compile a kernel with all
   available SCSI drivers as modules. Load each module step by step
   until you get the right one.
     ________________________________________________________________

12.28.2. Related Documentation

    1. [http://tldp.org/HOWTO/SCSI-2.4-HOWTO/index.html] SCSI-2.4-HOWTO
     ________________________________________________________________

12.28.3. Survey

   There is no current x86 laptop yet with a SCSI harddisk. Though there
   have been two models with a built in SCSI port: Texas Instruments TI
   4000 and HP OmniBook 800. Maybe the PowerBook G3 has a SCSI disk, but
   I didn't check this yet. The old Apple Powerbook Duo models had a
   SCSI hard disk.

   For other models, if you need SCSI support you may get it by using a
   SCSI-PCMCIA card or via a SCSI adapter in a docking station.
     ________________________________________________________________

12.29. Universal Serial Bus - USB

12.29.1. Linux Compatibility Check

   You should get information about the USB controller with cat
   /proc/pci and about USB devices with cat /proc/bus/usb/devices.
     ________________________________________________________________

12.29.2. Miscellaneous

   Newer laptops come equipped with the Universal Serial Bus - USB. The
   following USB devices are available, not all of them are fully
   supported by Linux yet: keyboard, mouse, printer, tablet, camera,
   cpia, webcam, MP3 player, modem, wireless LAN, audio, jukebox,
   scanner, storage (hard drive, memory stick), floppydrive, ZIP, Super
   Disk - LS 120, compact flash reader, CD, BlueTooth, ethernet, serial,
   joystick, USB Host-to-Host Cable, hub .

   Visit the [http://www.linux-usb.org/] USB Linux home page. Also I
   have set up a page collecting information about laptops and mobile
   devices using USB at the [http://tuxmobil.org/hardware.html] TuxMobil
   - Mobile Hardware Survey .

   Warning

   Please note, I have got a report that the power by a laptop via USB
   is not enough for some kind of devices, e.g. Web Cams or hard disks.
   But it seems to depend on the laptop and the specific device. With
   desktop Linux machines these USB devices work flawlessly, but with
   mobile devices not.
     ________________________________________________________________

12.30. FireWire - IEEE1394 - i.Link

   Firewire, also known as IEEE-1394 and iLink, is a high-speed serial
   bus system that was originally developed by Apple Computer.
   Currently, its widest implementation is for digital video; however,
   it has a lot of other uses. Like USB, Firewire is a serial protocol
   that supports hot-swapping. Firewire supports much higher speeds than
   USB. The [http://linux1394.sourceforge.net/] Linux IEEE 1394
   Subsystem provides support for IEEE 1394 (FireWire, i.Link). It
   consists of a kernel subsystem as well as applications.

   Also I have set up a page collecting information about laptops and
   FireWire at [http://tuxmobil.org/hardware.html] TuxMobil - Mobile
   Hardware Survey .
     ________________________________________________________________

12.31. Floppy Drive

12.31.1. Linux Compatibility Check

   Usually there are no problems connecting a floppy drive to a Linux
   laptop. But with a laptop floppy drive you may sometimes not be able
   to use every feature. I encountered the superformat command (from the
   fdutils package) couldn't format more than 1.44MB with my HP OmniBook
   800. You may also have difficulty when the floppy drive and CD drive
   are mutually exclusive, or when the floppy drive is a PCMCIA device
   (as with the Toshiba Libretto 100). With older laptops, there might
   be a minor problem if they use a 720K drive. As far as I know all
   distributions come with support for 1.44M (and sometimes 1.2M)
   floppies only. Though it's possible to install Linux anyway. Please
   see Installation chapter. Please see kernel documentation for boot
   time parameters concerning certain laptop floppy drives, for instance
   IBM(TM) ThinkPad. Or man bootparam .
     ________________________________________________________________

12.32. Optical Drives (CD/DVD)

12.32.1. CD-ROM

12.32.1.1. Related Documentation

     * [http://tldp.org/HOWTO/CDROM-HOWTO/] CDROM-HOWTO
     * [http://tldp.org/HOWTO/CD-Writing-HOWTO.html] CD-Writing-HOWTO
     ________________________________________________________________

12.32.1.2. Introduction

   Most notebooks today come with CD drives. If floppy and CD drive are
   swappable they are usually mutually exclusive, however many vendors
   (HP, Dell) provide cables which allow the floppy module to be
   connected to the parallel port. Sometimes the CD drives comes as
   external PCMCIA device (e.g. SONY), or as SCSI device (e.g. HP
   OmniBook 800), USB device (e.g. SONY), or as Firewire (e.g. SONY VAIO
   VX71P). Such an external devices might bear problems to install Linux
   from it.

   As far as I know there are SONY DiscMans available which have a port
   to connect them to a computer or even a SCSI port. I found an article
   published by Ziff-Davis Publishing Company (September 1996 issue, but
   missed to note the URL) written by Mitt Jones: "Portable PC Card
   CD-ROM drives transform laptops into mobile multimedia machines",
   which listed: Altec Lansing AMC2000 Portable Multimedia CD-ROM
   Center; Axonix ProMedia 6XR; CMS PlatinumPortable; EXP CDS420
   Multimedia Kit; H45 QuickPCMCIA CD; Liberty 115CD; Panasonic
   KXL-D740; Sony PRD-250WN CD-ROM Discman.

   To here music from internal CD drives usually works without problems.
   But note:

   Tip

   Some notebooks come with an external CD drive, you need an extra
   cable to connect the sound output of the drive to the sound input of
   the notebook.
     ________________________________________________________________

12.32.2. CD-RW

   Most notebooks today even come with internal or external CD writers.
   The internal usually work, see
   [http://tldp.org/HOWTO/CD-Writing-HOWTO.html] CD-Writing-HOWTO for
   details. But with the different external (PCMCIA, Firewire, USB)
   drives you probably need some tweaking.
     ________________________________________________________________

12.32.3. DVD Drive

   [http://linvdr.org/projects/regionset/] regionset adjusts and shows
   the region code of DVD drives.

   [http://www.trylinux.com/projects/udf/index.html] Universal Disk
   Format (UDF) Driver : "UDF is a newer CDROM filesystem standard
   that's required for DVD roms. It's meant to be a replacement for the
   ISO9660 filesystem used on today's CDROMs, but the immediate impact
   for most will be DVD. DVD multimedia cdroms use the UDF filesystem to
   contain MPEG audio and video streams. To access DVD cdroms you would
   need a DVD cdrom drive, the kernel driver for the cdrom drive, some
   kind of MPEG video support, and a UDF filesystem driver (like this
   one). Some DVD cdroms may contain both UDF filesystems and ISO9660
   filesystems. In that case, you could get by without UDF support."

   [http://www.linuxvideo.org/] DVD Video

   DVD formats:
Digital Versatile Disc
DVD-5  4.4GB 1side 1 coat ~ 2h video
DVD-9  8.5GB 1side 2 coat ~ 4h video
DVD-10 9.4GB 2side 1 coat ~ 4.5h video
DVD-18 17 GB 2side 2 coat ~ 8h video
     ________________________________________________________________

12.33. Hard Disk

12.33.1. Linux Compatibility Check

   Useful programs are hdparm, dmesg, fsck and fdisk .
     ________________________________________________________________

12.33.2. Utilities

   The [http://smartmontools.sourceforge.net/] smartmontools package
   contains two utility programs (smartctl and smartd) to control and
   monitor storage systems using the Self-Monitoring, Analysis and
   Reporting Technology System (SMART) built into most modern ATA and
   SCSI hard disks. In many cases, these utilities will provide advanced
   warning of disk degradation and failure.

   The [http://www.guzu.net/linux/hddtemp.php] hddtemp utility can read
   the temperature of S.M.A.R.T. hard disks.
     ________________________________________________________________

12.33.3. Solid-State-Disks - SSDs

   Solid-State-Disks (SSDS) need some optimization of the Linux file
   system before installing the operating system. Here are some
   [http://www.thomas-krenn.com/de/wiki/Partition_Alignment] tips and
   tricks for partition alignment. Also useful some tips from Theodore
   Ts'o about
   [http://thunk.org/tytso/blog/2009/02/20/aligning-filesystems-to-an-ss
   ds-erase-block-size/] aligning filesystems to an SSD's erase block
   size.
     ________________________________________________________________

12.33.4. Miscellaneous

   Be careful when using your laptop abroad. I have heard about some
   destroyed harddisks due to a magnetic field emitted from the
   magnetic-holds at the backresttable of the seats in a German railway
   waggon.

   Though I am quite satisfied with the quality of the hard disk in my
   laptop, when I removed it from the case I unintendedly dropped it. I
   recommend to be very careful.
     ________________________________________________________________

12.33.5. Form Factors

   AFAIK there are only two form factors for harddisks used in laptops.
   Since 2003 there is the 1.8" format. But much older and still the
   most common format is the 2.5" format. The 2.5" format seems to be
   available in different heights (Please note I couldn't verify this
   information yet):

     * 18mm: laptops built before 1996 usually have drives 18mm high
     * 12.7mm: I got a report about such disks but without a notebook
       model or manufacturer name
     * 11mm: since 1996 the drives are 11mm high
     * 9mm: many laptops, including the subnotebooks, now use a 9mm-high
       disk drive. The largest available in this format in late 1999 is
       IBM(TM) 12GN.
     * 9.5mm: Toshiba Libretto L70 and L100 have a 9.5mm HD
     * 8.45mm: Toshiba Libretto 20, 30, 50 and 60 have 8.45mm tall HDs
     * 6.35mm: Toshiba Libretto L1000 has a 6.35mm HD

   It might be possible to use a hard disk which doesn't fit with some
   case modifications.

   Some laptops come with a removable hard disk in a tray, for instance
   the KAPOK 9600D. There seem to be no SCSI drives for laptops
   available.
     ________________________________________________________________

12.33.6. Manufacturer Tools

   Some hard disk manufacturers offer dedicated tools to change hard
   disk parameters. For example Hitachi offers
   [http://www.hitachigst.com/hdd/support/download.htm] Drive Fitness
   Test (DFT), which provides a quick, reliable method to test SCSI and
   IDE hard disk drives, including Serial-ATA IDE drives. The Drive
   Fitness Test analyze function performs read tests without overwriting
   customer data. (However, Drive Fitness Test is bundled with some
   restoration utilities that will overwrite data.) The
   [http://www.hitachigst.com/hdd/support/download.htm] Feature Tool is
   a DOS-bootable tool for changing various ATA features.
     ________________________________________________________________

12.34. Hot-Swapping Devices (MultiBay, SelectBay, ..)

   Some laptops (usually the more expensive ones) come with a free slot,
   which may bear a second hard disk or CD/DVD drive. Every manufacturer
   seems to name it differently, names like MultiBay(TM) and
   SelectBay(TM) are common. Different Linux tools are available to
   handle these hot-swapping devices.

   thotswap is part of the [http://www.buzzard.me.uk/toshiba/index.html]
   Toshiba(tm) Linux Utilities it makes it possible to hotswap devices
   in the SelectBay.

   [http://timstadelmann.de/hotswap.html] Hotswap is a utility to
   register and deregister hotswappable IDE hardware. It is written to
   be used on Laptops with some sort of hardware bay to remove the
   module from the machine without rebooting it. Note that this utility
   is not required to insert or remove batteries or floppy disk drives;
   only for IDE devices.

   The hard disk management tool hdparm also comes with a hot swap
   option.

   Some bays can (in some cases only) carry a second battery. Currently
   I don't know how Linux can handle this. For example are there any
   tools, which show battery stats for the second battery?
     ________________________________________________________________

12.35. WireLess Network - WLAN



   For this let us found a city/ And we will name it Mahagonny/ That
   means: Net City/ She shall be like a Net/ That is set out to catch
   edible birds./ Everywhere there is toil and labor/ But here there is
   amusement/ For it is the uninhibited lust of men/ Not to suffer and
   to be allowed all things/ That is the essence of gold
     Bertolt Brecht, 1929
     ________________________________________________________________

12.35.1. Related Documentation

    1. [http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Linux.Wirel
       ess.drivers.html] Wireless-HOWTO I,
    2. [http://www.linux-wlan.org/] Wireless-HOWTO II and
    3. [http://www.fuw.edu.pl/~pliszka/hints/wireless.html]
       Wireless-HOWTO III.
     ________________________________________________________________

12.35.2. Introduction

   Many notebooks now come pre-equipped with wireless network support
   for the 802.11 protocol family. These devices are either based on
   [http://tuxmobil.org/minipci_linux.html] miniPCI or
   [http://tuxmobil.org/pcmcia_linux.html] PCMCIA. You may check that
   with either lspci or cardctl ident. External WLAN adapters are
   available as PCMCIA or CF-Cards and as USB devices. Details will
   follow in a later issue.
     ________________________________________________________________

12.36. BlueTooth

   Some laptops come pre-equipped with built-in BlueTooth support, but I
   had no time to investigate that any further. Actually I do not have
   such a machine to test Linux on it yet.
     ________________________________________________________________

12.37. Infrared Port



   Better red, than dead.
     Unknown AuthorEss
     ________________________________________________________________

12.37.1. Linux Compatibility Check

   To get the IrDA� port of your laptop working with Linux/IrDA� you may
   use StandardInfraRed (SIR) or FastInfraRed (FIR).
     ________________________________________________________________

12.37.1.1. SIR

   Up to 115.200bps, the infrared port emulates a serial port like the
   16550A UART. This will be detected by the kernel serial driver at
   boot time, or when you load the serial module. If infrared support is
   enabled in the BIOS, for most laptops you will get a kernel message
   like:

Serial driver version 4.25 with no serial options enabled
ttyS00 at 0x03f8 (irq = 4) is a 16550A     #first serial port /dev/ttyS0
ttyS01 at 0x3000 (irq = 10) is a 16550A    #e.g. infrared port
ttyS02 at 0x0300 (irq = 3) is a 16550A     #e.g. PCMCIA modem port
     ________________________________________________________________

12.37.1.2. FIR

   If you want to use up to 4Mbps, your machine has to be equipped with
   a certain FIR chip. You need a certain Linux/IrDA� driver to support
   this chip. Therefore you need exact information about the FIR chip.
   You may get this information in one of the following ways:

    1. Read the specification of the machine, though it is very rare
       that you will find enough and reliable information to use with
       Linux there.
    2. Try to find out whether the FIR chip is a PCI device. Do a cat
       /proc/pci . The appropriate files for 2.2.x kernels are in
       /proc/bus/pci . Though often the PCI information is incomplete.
       You may find the latest information about PCI devices and vendor
       numbers in the kernel documentation usually in
       /usr/src/linux/Documentation or at the page of
       [http://members.datafast.net.au/~dft0802/] Craig Hart . From
       kernel 2.1.82 on, you may use lspci from the pci-utils package,
       too.
    3. Use the DOS tool CTPCI330.EXE provided in ZIP format by the
       [http://www.heise.de/ct/ftp/ctsi.shtml] German computer magazine
       CT. The information provided by this program is sometimes better
       than that provided by the Linux tools.
    4. Try to get information about Plug-and-Play (PnP) devices. Though
       I didn't use them for this purpose yet, the isapnp tools, could
       be useful.
    5. If you have installed the Linux/IrDA� software load the FIR
       modules and watch the output of dmesg, whether FIR is detected or
       not.
    6. Another way how to figure it out explained by Thomas Davis
