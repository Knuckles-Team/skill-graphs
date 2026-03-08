       (modified by WH): "Dig through the FTP site of the vendor, find
       the Windows9x FIR drivers, and they have (for a SMC chip):

-rw-rw-r--   1 ratbert  ratbert       743 Apr  3  1997 smcirlap.inf
-rw-rw-r--   1 ratbert  ratbert     17021 Mar 24  1997 smcirlap.vxd
-rw-rw-r--   1 ratbert  ratbert      1903 Jul 18  1997 smcser.inf
-rw-rw-r--   1 ratbert  ratbert     31350 Jun  7  1997 smcser.vxd

       If in doubt, always look for the .inf/.vxd drivers for Windows95.
       Windows95 doesn't ship with _ANY_ FIR drivers. (they are all
       third party, mostly from Counterpoint, who was assimilated by
       ESI)."
    7. Also Thomas Davis found a package of small DOS
       [ftp://ftp.smsc.com/pub/appsoftware/] utilities made by SMC. The
       package contains FINDCHIP.EXE. And includes a FIRSETUP.EXE
       utility that is supposed to be able to set all values except the
       chip address. Furthermore it contains BIOSDUMP.EXE, which
       produces this output:
       Example 1 (from a COMPAQ Armada 1592DT)

In current devNode:
           Size      = 78
           Handle    = 14
           ID        = 0x1105D041 = 'PNP0511' -- Generic IrDA SIR
Types:  Base = 0x07, Sub = 0x00,  Interface = 0x02
Comm. Device, RS-232, 16550-compatible
Attribute = 0x80
                CAN be disabled
                CAN be configured
BOTH Static & Dynamic configuration
Allocated Resource Descriptor Block TAG's:
TAG=0x47, Length=7 I/O Tag, 16-bit Decode
Min=0x03E8, Max=0x03E8
Align=0x00, Range=0x08
TAG=0x22, Length=2 IRQ Tag, Mask=0x0010
TAG=0x79, Length=1 END Tag, Data=0x2F

       Result 1:
       Irq Tag, Mask (bit mapped - ) = 0x0010 = 0000 0000 0000 0001 0000
       so, it's IRQ 4. (start at 0, count up ..), so this is a SIR only
       device, at IRQ=4, IO=x03e8.
       Example 2 (from an unknown machine)

In current devNode:
          Size      = 529
          Handle    = 14
          ID        = 0x10F0A34D = 'SMCF010' -- SMC IrCC
Types:  Base = 0x07, Sub = 0x00,  Interface = 0x02
Comm. Device, RS-232, 16550-compatible
Attribute = 0x80
               CAN be disabled
               CAN be configured
BOTH Static & Dynamic configuration

Allocated Resource Descriptor Block TAG's:
TAG=0x47, Length=7 I/O Tag, 16-bit Decode
Min=0x02F8, Max=0x02F8
Align=0x00, Range=0x08
TAG=0x22, Length=2 IRQ Tag, Mask=0x0008
TAG=0x47, Length=7 I/O Tag, 16-bit Decode
Min=0x02E8, Max=0x02E8
Align=0x00, Range=0x08
TAG=0x2A, Length=2 DMA Tag, Mask=0x02, Info=0x08
TAG=0x79, Length=1 END Tag, Data=0x00

       Result 2:
       a) it's a SMC IrCC chip
       b) one portion is at 0x02f8, has an io-extent of 8 bytes; irq = 3
       c) another portion is at 0x02e8, io-extent of 8 bytes; dma = 1
       (0x02 =0000 0010)

   Warning

   The package is not intended for the end user, and some of the
   utilities could be harmful. The only documentation in the package is
   in Microsoft Word format. Linux users may read this with
   [http://www.fe.msk.ru/~vitus/catdoc/] catdoc.
    8. Use the Device Manager of the MicroSoft Windows9x/NT operating
       system.
    9. You may also use the hardware surveys mentioned below.
   10. And as a last resort, you may even open the laptop and look at
       the writings at the chipsets themselves.
     ________________________________________________________________

12.37.1.3. Hardware Survey

   I have made an IrDA hardware survey at
   [http://tuxmobil.org/ir_misc.html] TuxMobil . This list also contains
   information about infrared capable devices which are not mentioned
   here (mice, printers, remote control, transceivers, etc.).

   To make this list more valuable, it is necessary to collect more
   information about the infrared devices in different hardware. You can
   help by sending me a short e-mail containing the exact name of the
   hardware you have and which type of infrared controller is used.

   Please let me know also how well Linux/IrDA� worked (at which tty,
   port and interrupt it works and the corresponding infrared device,
   e.g. printer, cellular phone).

   Also you can help by contributing detailed technological information
   about some infrared devices, which is necessary for the development
   of drivers for Linux.
     ________________________________________________________________

12.37.2. Related Documentation

    1. [http://tuxmobil.org/howtos.html] Linux-Infrared-HOWTO
     ________________________________________________________________

12.37.3. IrDA� Configuration - Survey

12.37.3.1. IrDA�

   The Linux infrared support is still experimental, but rapidly
   improving. I try to describe the installation in a short survey.
   Please read my [http://tuxmobil.org/howtos.html] Linux-Infrared-HOWTO
   for detailed information. And visit the [http://irda.sourceforge.net]
   Linux/IrDA Project.
     ________________________________________________________________

12.37.3.1.1. Kernel

    1. Get a 2.4.x kernel and the latest Linux/IrDA patches from the
       [http://irda.sourceforge.net] Linux/IrDA Project.
    2. Compile it with all IrDA� options enabled.
    3. Also enable experimental, sysctl, serial and network support.
     ________________________________________________________________

12.37.3.1.2. Software

    1. Get the Linux IrDA� software irda-utils at
       [http://irda.sourceforge.net/] The Linux IrDA Project .
    2. Untar the package.
    3. Do a make depend; make all; make install
     ________________________________________________________________

12.37.3.1.3. Hardware

    1. Enable the IrDA� support in the BIOS.
    2. Check for SIR or FIR support, as described above.
    3. Start the Linux/IrDA� service with irattach DEVICE -s 1 .
    4. Watch the kernel output with dmesg .
     ________________________________________________________________

12.37.3.2. Linux Infrared Remote Control - LIRC

   [http://www.lirc.org] Linux Infrared Remote Control LIRC is a package
   that supports receiving and sending IR signals of the most common IR
   remote controls. It contains a device driver for hardware connected
   to the serial port, a daemon that decodes and sends IR signals using
   this device driver, a mouse daemon that translates IR signals to
   mouse movements and a couple of user programs that allow to control
   your computer with a remote control. I don't have valid information
   about how much infrared remote control is working with laptop
   infrared devices.
     ________________________________________________________________

12.38. FingerPrint Reader

   UPEK, provider of popular fingerprint sensors to IBM's T42 notebooks
   and others, has announced that they will be providing a BioAPI
   compliant library to perform biometric authentication under Linux.
   There is also a proposed
   [http://linuxbiometrics.com/modules/news/article.php?storyid=16]
   FingerPrint Reade driver.
     ________________________________________________________________

Chapter 13. Accessories: PCMCIA, USB and Other External Extensions

13.1. PCMCIA Cards

13.1.1. Card Families

    1. Ethernet adapter
    2. Token Ring adapter
    3. Ethernet + Modem / GSM
    4. Fax-Modem / GSM adapter
    5. SCSI adapter
    6. I/O cards: RS232, LPT, RS422, RS485, GamePort, IrDA�, Radio,
       Video
    7. Memory cards
    8. harddisks
    9. 2.5" harddisk adapters

   For desktops there are PCMCIA slots for ISA and PCI bus available.
     ________________________________________________________________

13.1.2. Linux Compatibility Check

   With the command cardctl ident you may get information about your
   card. If your card is not mentioned in /etc/pcmcia/config, create a
   file /etc/pcmcia/<MYCARD>.conf appropriately. Take an entry in the
   first file as a model. You may try every driver, just in case it
   might work, for instance the pcnet_cs supports many NE2000 compatible
   PCMCIA network cards. Note: it is a bad practice to edit
   /etc/pcmcia/config directly, because all changes will be lost with
   the next update. After creating /etc/pcmcia/<MYCARD>.conf restart the
   PCMCIA services. This may not be enough to get the card to work, but
   works sometimes for no-name network cards or modem cards. If you get
   a card to work or have written a new driver please don't forget to
   announce this to the developer of the PCMCIA-CS package David Hinds.
   Look at the current issue of
   [http://pcmcia-cs.sourceforge.net/ftp/SUPPORTED.CARDS]
   SUPPORTED.CARDS to get information about supported cards.

   Since not all cards are mentioned there, I have set up a Survey of
   PCMCIA/CardBus/CF Cards Supported by Linux.
     ________________________________________________________________

13.2. ExpressCards

   ExpressCard is the official standard for modular expansion for
   desktop and mobile systems based on PCI-Express. These cards offer a
   smaller and faster PC Card solution. Here is the Linux Hardware
   Compatibility List - HCL for ExpressCards, which includes a survey of
   [http://tuxmobil.org/expresscard_linux.html] Linux installations on
   laptops and notebooks which feature an ExpressCard slot.
     ________________________________________________________________

13.3. SmartCards

   SmartCard reader, see Project Muscle -
   [http://www.linuxnet.com/smartcard/index.html] Movement for the Use
   of Smart Cards in a Linux Environment and the
   [http://tuxmobil.org/smart_linux.html] Linux Hardware Compatibility
   List - HCL for SmartCards.
     ________________________________________________________________

13.4. SDIO Cards

   Looking for [http://tuxmobil.org/sdio_linux.html] Linux drivers for
   SDIO cards? There is almost nothing available yet. But here are at
   least some pointers.
     ________________________________________________________________

13.5. Memory Technology Devices - RAM and Flash Cards

   [http://www.linux-mtd.infradead.org/] The Linux Memory Technology
   Device project aims to provide a unified subsystem for handling RAM
   and Flash cards (Memory Technology Devices). It is intended to be
   compatible with the Linux PCMCIA code, to prevent duplication of code
   and effort, yet its main target is small embedded systems, so it will
   be possible to compile the drivers into the kernel for use as a root
   filesystem, and a close eye will be kept on the memory footprint.
     ________________________________________________________________

13.6. Memory Stick

   The Memory Stick is a proprietary memory device, in the beginning
   only used in devices made by SONY. But now they are available in
   mobile computers made by other manufacturers, too. The current sticks
   are USB devices and work with all recent kernels. After loading the
   usb-storage you may mount them as SCSI devices, often as /dev/sda or
   /dev/sdb. For older laptops see the appropriate pages at
   Linux-on-Laptops.

   There is also a SONY Memory Stick Floppy Adapter - MSAC-FD2M. I don't
   know whether this works with Linux.
     ________________________________________________________________

13.7. Card Readers for SD/MMC/Memory Stick

13.7.1. External Readers

   All external SD/MMC/CF-Card/Memory Stick readers are USB devices and
   work fine with the usb-storage module. The only caveat which might
   occur is that you may have difficulties to determine the device
   assignment. Just use dmesg after you have connected the reader. The
   command should show a SCSI device like /dev/sda1 assigned to the USB
   drive.
     ________________________________________________________________

13.7.2. Internal Readers

   Currently there are three kinds of devices available: USB, PCMCIA and
   PCI devices.

   USB devices are seldom, but usually work out of the box. They behave
   like the external readers mentioned above.

   Some readers are PCMCIA/CardBus devices. Often such a reader is
   located near the CardBus slot. The command cardctl ident will reveal
   these cards.

   For some laptops and notebooks a [http://projects.drzeus.cx/wbsd]
   driver for the Winbond's W83L518D and W83L519D SD/MMC card reader is
   available.

   Some proprietary devices are not yet known to work with Linux. Except
   the readers built into the SHARP Linux PDAs, but the driver is closed
   source and available as a binary only for the ARM CPU.
     ________________________________________________________________

13.8. USB Devices

   For more info about this and other Linux-compatible USB devices see
   the [http://www.qbik.ch/usb/devices/] USB Survey and my
   [http://tuxmobil.org/usb_linux.html] Mobile USB Linux Hardware Survey
   .
     ________________________________________________________________

13.8.1. Ethernet Devices

   From kernel source 2.4.4:

     * ADMtek AN986 Pegasus (eval. board)
     * ADMtek ADM8511 Pegasus II (eval. board)
     * Accton 10/100
     * Billington USB-100
     * Corega FEter USB-TX
     * MELCO/BUFFALO LUA-TX
     * D-Link DSB-650TX, DSB-650TX-PNA, DSB-650, DU-E10, DU-E100
     * Linksys USB100TX, USB10TX
     * LANEED Ethernet LD-USB/TX
     * SMC 202
     * SOHOware NUB Ethernet

   Any Pegasus II based board also are supported. If you have devices
   with vendor IDs other than noted above you should add them in the
   driver code and send a message to <petkan_AT_dce.bg> for update.
     ________________________________________________________________

13.8.2. BlueTooth Dongles

   There are many dongles around. I have made some experience with the
   [http://www.aircable.net/] AIRcable for laptops and PDAs (e.g.
   SHARP's Zaurus models SL-5x00 and C-7x0). This USB dongle kit
   provides a fast, convenient way of connecting mobile Linux computers
   to another personal computer or notebook computer or mobile phone
   without any cabling. The AIRcable uses a BlueTooth connection without
   the need to set up a complicated BlueTooth configuration. For
   example: The AIRcable Zaurus-USB can be used for syncing the Zaurus
   (ZaurusManager, Intellisync), for Qtopia desktop and for network
   connections through the PC (Linux, Windows and Apple) running pppd.
   You may find further details and a
   [http://tuxmobil.org/bluetooth_linux.html] survey of compatible
   mobile phones etc. at TuxMobil.
     ________________________________________________________________

13.8.3. Port Replicators/Docking Stations

   I do not have experience with these devices yet. But I expect that it
   will be difficult, if not impossible, to get them to run with Linux.
   For other kinds of port replicators and docking stations see the
   appropriate section in the laptop chapter.
     ________________________________________________________________

13.9. Printers and Scanners

13.9.1. Survey of Mobile Printers and Scanners

   For a survey of ports and protocol to print via a mobile or
   stationary printer see the Different Environments chapter below.

    1. [http://www.canon.com/] CANON : BJC-80 (this printer can also be
       used as a scanner with the optional scan head!) David F. Davey
       wrote: "I finally have a Canon BJC-80 printer working properly
       with IrDA�. By properly I mean as a pseudo-PostScript device by
       way of ghostscript and a modified lpd.
       How:
          + linux-2.2.7-ac2-irda6
          + /proc/sys/net/irda/slot_timeout increased to 10 (essential
            or discovery fails)
          + ghostscript DEVICE set to bjc600
          + printcap includes:

:xc#01777777:\
:fc#017:\
:fs#020000010002:

          + and lpd had to be modified to accept the ulong fs and to
            handle xc (which is documented but not coded in the lpd's I
            have looked at). "
       For further information look at his page
       [http://www.windclimber.net/linux/bjc-80.pcgi] BJC-80 .
       Tim Auckland wrote: Would my version of lpd help? unixlpr is a
       portable version of the lpr/lpd suite, compatible with
       traditional versions and [http://rfc.net] RFC 1179 and with a
       couple of minor extensions, including the :ms= field (also seen
       in SunOS 4) and the ability to print directly to TCP connected
       printers without needing special filters. ms allows you to
       configure the tty using stty arguments directly, so if stty can
       handle the extended flags, my lpd should handle IrDA� out of the
       box. You can find the latest unixlpr
       [http://www.geocities.com/CapeCanaveral/Hall/7203/Printing/] here
       .
    2. [http://www.canon.com/] CANON : BJC-50 65% of the size of the
       BJC-80, Li-Ion battery included, and basically the same features
       as the BJC-80.
    3. [http://www.canon.com/] CANON : BJ-30
    4. [http://www.citizen-america.com/] Citizen : CN-60
    5. [http://www.pentaxtech.com/] Pentax : Pocketjet
    6. HP: DeskJet 340Cbi. This is a small, portable, low-duty-cycle
       printer. It prints either black, or color (3 color). I have had
       some problems with it loading paper. Overall, the small size and
       portability make it a nice unit for use with laptops. I use the
       HP 500/500C driver with Linux.
    7. Olivetti: JP-90
    8. [http://www.maxpointgmbh.de] MaxPoint : TravelScan, mobile
       scanner for the PCMCIA port.

   AFAIK only the HP DeskJet 340Cbi and the BJC-80 machine have an
   infrared port. Pay attention to the supplied voltage of the power
   supply if you plan to travel abroad. I couldn't check the scan
   functionalities with Linux yet.
     ________________________________________________________________

13.9.2. Scanner and OCR Software

   [http://www.mostang.com/sane/] SANE stands for Scanner Access Now
   Easy and is an application programming interface (API) that provides
   standardized access to any raster image scanner hardware (flatbed
   scanner, hand-held scanner, video- and still-cameras, frame-grabbers,
   etc.). The SANE standard is free and its discussion and development
   is open to everybody. The current source code is written for UNIX
   (including Linux) and is available under the GNU public license
   (commercial application and backends are welcome, too, however).

   [http://altmark.nat.uni-magdeburg.de/~jschulen/ocr/] GOCR is optical
   character recognition software. It converts PGM files into ASC files.

   For scanner drivers see [http://www.willamowius.de/scanner.html]
   Linux Drivers for Handheld Scanners.
     ________________________________________________________________

13.9.3. Connectivity

   There are different ways to connect a printer or scanner to a laptop.
   For printers usually: parallel port, serial port, USB and IrDA� port.
   For scanners usually: parallel port, SCSI (via PCMCIA or generic SCSI
   port), USB and PCMCIA port. All of them need the appropriate kernel
   drivers.
     ________________________________________________________________

13.10. Serial Devices

13.10.1. Keyspan PDA Serial Adapter

   Single port DB-9 serial adapter, pushed as a PDA adapter for iMacs
   (mostly sold in Macintosh catalogs, comes in a translucent
   white/green dongle). Fairly simple device.
     ________________________________________________________________

13.11. External Storage Devices

13.11.1. External Hard Disks

   There are external hard disk cases with different connectors
   available: PCMCIA, USB and FireWire. Cases are available for 2.5"
   (laptop hard disks), 3.5" (desktop hard disks) and 5.25" (CD-Writer).
   All of them work very well together with Linux. Especially I like the
   cases for 2.5" hard disks, you may upgrade your current laptop hard
   disk and use the old one to put it into the external box to extend
   your hard disk space.

   Caveat: After wake up from suspend mode, the external hard drive
   can't work. To cure this problem these remedies might help:
   Disconnect the external drive and then plug it in again. Or use an AC
   adapter to power the external drive. Though this seems inconvenient
   in a suspend situation. But since the external drive gets the power
   from the adapter, there is no disconnection from power as will be if
   power is provided from USB.

   Caveat: Take care that the jumpers are set to Master. Almost all
   external hard disk cases will not work when the jumpers are set to
   Slave or Cable Select.
     ________________________________________________________________

13.12. Power and Phone Plugs, Power Supply

   When travelling abroad you might consider to take a set of different
   power and phone plugs with you. Also, it's useful if you can change
   the input voltage of the power supply, for instance from 110V in the
   US to 220V in Germany. There also power supplies for 12V batteries
   from cars.

   Some models of power plugs:
                ____                                  _
               / () \     _   _       _       _     _(_)_
frontal view: |()  ()|   (_)=(_)     (_)     (_)   (_) (_)
               ------

abbreviation.:    C13       C8         ??     PS/2    C5

symbol......:    ??        ??        -O)-    N.N.    N.N.

   Warning

   Though some -O)- shaped plug may seem to be compatible with your
   laptop, because of the appropriate physical size, take extreme care
   it uses the same plus-minus voltage scheme, for instance plus for the
   inner ring and minus for the outer one. Often, but not always, there
   are the appropriate symbols near the plug.

   More about laptop and PDA power supplies at
   [http://tuxmobil.org/energy_laptops.html] TuxMobil.
     ________________________________________________________________

13.13. Bags and Suitcases

   You probably wonder, why I include this topic here. But shortly after
   using my COMPAQ Armada 1592DT I recognized that the rear side of the
   machine (where the ports are arranged) was slightly damaged. Though I
   have taken much care when transporting the laptop, this was caused by
   putting the bag on the floor. It seems that the laptop has so much
   weight, that it bounces inside the bag on its own rear side. So I
   decided to put a soft pad into the bag before loading the laptop. A
   good bag is highly recommended if you take your laptop on trips, or
   take it home every night.

   Laptops computers are frequently demolished in their carrying bag.
   The two main causes of demolition are poking the LC display and
   banging the edges. A good case has very stiff sides to spread out
   pokes, and lots of energy-absorbent padding around the edges to help
   when you whack it on the door jamb. Few cases actually have either of
   these features.

   More laptops are lost to theft than damage, so camouflage is a wise
   too. Emerson, Tom # El Monte <TOMEMERSON_AT_ms.globalpay.com> wrote:
   "I use for a laptop travelling bag: a Pyrex casserole carrier bag.
   Yup, you might think it odd to use a casserole bag for a laptop, but
   it turns out it has several advantages:

     * The one I use has a microwavable heating pad in it - while I
       don't actually heat this pad (it's meant to keep food warm while
       in transport), it does provide padding underneath the laptop. The
       carrier I have only has a lower - heating - pad, but there is
       also a similar carrier that has both a lower - heating - pad and
       an upper - cooling - pad - placed in the freezer to get it cold -
       -- the intent is that you keep one or the other in the bag to
       keep your food hot or cold as desired. A secondary advantage to
       the - cooling pad - pad is that if you've - chilled - it before
       taking the computer out for the day, it will keep the CPU cooler
       while you're running the laptop...
     * the top of the bag has a zipper on three sides, so it - opens -
       the same way as my laptop - I don't even need to take it out of
       the carrier to use the laptop
     * there is enough room at the side of the bag to store the external
       power supply, a regular Logitech mouseman, and the network -
       dongle - with BNC/TP ports - and if I had it, the modem/phone
       port as well -
     * there is enough clearance on top of the machine to include a
       handful of CD's or diskettes, if needed.
     * when it's left - unattended - in a car, it's less likely to be
       stolen - think about it, if you were a thief walking through a
       parking lot and eyeing the contents of cars, a - laptop bag - is
       instantly recognizable as holding a laptop computer - something
       that can be fenced at a pretty hefty profit, but if you saw a
       casserole carrier in the front seat of a car, would you think it
       contained anything OTHER than a casserole? - and probably
       half-eaten, at that... - Unless you are a hungry thief, chances
       are you'll skip this and move on.
     * likewise, I've heard that keeping a laptop computer in a diaper
       bag is another good - camouflage - technique - who in their right
       mind is going to steal a bag of - dirty - diapers?"

VI. Kernel

   Table of Contents
   14. Kernel History

        14.1. Kernel 2.4
        14.2. Kernel 2.6
        14.3. Kernel Configuration for Laptops
     ________________________________________________________________

Chapter 14. Kernel History

   The kernel chapter isn't ready yet. Just some notes about important
   changes with kernel 2.4 and 2.6 related to mobile computers. As well
   as some notes about Kernel configurations for laptops.
     ________________________________________________________________

14.1. Kernel 2.4

14.1.1. PCMCIA

   From [http://www.pcmcia.org/] PCMCIA.ORG: " PCMCIA (Personal Computer
