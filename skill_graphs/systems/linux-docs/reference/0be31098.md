   PalmOS yet, WinCE/Pocket PC and Epoc will follow hopefully) and a
   Linux PDA.
     ________________________________________________________________

Chapter 7. Non-Linux PDAs - Ports and Tools

7.1. HELIO

   Currently the HELIO is only available with the proprietary VT
   operating system. See [http://www.fms-computer.com] FMS for
   information about the Linux port.
     ________________________________________________________________

7.1.1. Resources

    1. The manufacturer of the HELIO is [http://www.vtech.com] VTech .
    2. [http://vhl-tools.sourceforge.net/] vhl-tools (dead link) , a
       SourceForge project, works on utilities, patches, documentation
       and integration of Open Source software for Linux on the VTech
       Helio PDA.
    3. PocketLinux has a port under the GPL, as well as Debian and
       Redhat packages. But the URL http://www.pocketlinux.com/ seems no
       longer available.
    4. [http://www.kernelconcepts.de/helio/] KernelConcepts
    5. [http://www.linux-mips.org/linux-vr/tools.html] VR Org cross
       compiler
    6. [http://www.linux-community.de/News/] Linux-Magazin

   Figure 7-1. Screenshot of the HELIO PDA.

   [home_helio_03.png]
     ________________________________________________________________

7.2. iPAQ

   Currently the iPAQ PDAs by COMPAQ/HP are distributed only with a
   WinCE operating system.
     ________________________________________________________________

7.2.1. Resources

    1. The manufacturer of the iPAQ PDAs is
       [http://www.compaq.com/products/handhelds/pocketpc/index.html]
       COMPAQ/HP.

   Figure 7-2. Screenshot of the iPAQ PDA.

   [h3650.png]
     ________________________________________________________________

7.2.2. Braille Terminal

   [http://pages.infinite.net/sdoyon/] Stephane Doyon wrote to the iPAQ
   mailing list: "We (Nicolas Pitre and myself) have successfully ported
   BRLTTY to the iPaq and tested the setup by interfacing with a
   BrailleLite 18 through the serial port. BRLTTY is a program that
   allows access to the Linux text-mode console using various brands of
   Braille displays. The BrailleLite is a small electronic Braille
   notetaker device which can act as a small refreshable Braille
   display. It also has keys so I can not only read but also type. So
   there's just the iPaq and the BrailleLite device (with a horrible
   cable in between) and that's all I need to fully use the console on
   the iPaq (in text-mode). A pretty powerful setup, yet very small. At
   the Ottawa Linux Symposium in July, using a network card in my iPaq
   and borrowing the internet connection they supplied, I was actually
   able to logon to the net and go read my E-mail, using ssh, pine and
   lynx! It should be possible to duplicate this setup with other
   Braille display models or other PDAs."
     ________________________________________________________________

7.3. Newton Message Pad

   The Newton Message Pad was one of the first PDAs.
     ________________________________________________________________

7.3.1. Resources

    1. Apple is the manufacturer of the [http://www.apple.com] Newton
       Message Pad.
    2. [http://privat.swol.de/ReinholdSchoeb/Newton/] Newton and Linux
       Mini-HOWTO .
     ________________________________________________________________

7.4. PALM-Pilot

7.4.1. Resources

    1. 3COM is the manufacturer of the [http://www.3com.com/]
       PALM-Pilot.
    2. [http://tldp.org/HOWTO/PalmOS-HOWTO/] PalmOS-HOWTO (former
       Pilot-HOWTO) by David H. Silber.
    3. [http://www.pilot-link.org/] PilotLink and XCoPilot PilotLink is
       an utility that performs data transfers from 3com PalmPilot
       handheld computers to your Linux machine. XCoPilot is an emulator
       of the PalmPilot operating system that runs under Linux.
    4. [http://www.uclinux.org/] ucLinux
    5. [http://www.icsi.berkeley.edu/~minenko/PalmVNC] PalmVNC is an
       implementation of the Virtual Network Client architecture that
       will allow you to use a Linux or other UNIX machine to put up a
       (tiny) X Window on a 3COM PalmPilot.
    6. [http://tuxmobil.org/pda_linux_palm.html] Survey of Linux and BSD
       Applications for the Palm

   Figure 7-3. Screenshot of the PALM-Pilot emulator POSE.

   [pose.png]
     ________________________________________________________________

7.5. HandSpring VISOR

   The HandSpring VISOR is a clone of the PALM-Pilot PDA.
     ________________________________________________________________

7.5.1. USB

   From /usr/src/linux/Documentation/usb/usb-serial.txt:

   HandSpring Visor USB docking station. There is a
   [http://usbvisor.sourceforge.net/] webpage and mailing lists.

   Handspring VISOR Platinum serial port is tunneld through USB, so load
   usbserial.o with module parameters vendor=0x82d product=0x100
   (usbmgr.conf) USB is made active by starting the HotSync
   synchronisation per: pilot-xfer /dev/ttyUSB0 -b -/visor/
     ________________________________________________________________

7.6. Psion 5

   Currently I have information about a port for the Psion 5 and nothing
   about the Psion 3 series.
     ________________________________________________________________

7.6.1. Resources

    1. [http://tldp.org/HOWTO/Psion-HOWTO.html] Psion-HOWTO.
    2. [http://plptools.sourceforge.net/] PLPtools is a set of libraries
       and utilities for enabling Unix (mainly Linux) systems to
       communicate with a Psion palmtop over a serial line. On Linux, a
       connection over IrDA, using the IrCOMM feature is also possible.
       A shared library encapsulates the highlevel protocol
       (PsionLinkProtocol) and thus makes it easy to write applications
       without extensive knowledge of the protocol itself. A daemon
       (ncpd) handles the serial connection and provides it's services
       on a local TCP socket.
    3. The [http://linux-7110.sourceforge.net/] OpenPsion (formerly
       PsiLinux/Linux7k) is a project to port the unix-like operating
       system Linux to a small group of palmtops.
     ________________________________________________________________

Chapter 8. Connectivity

8.1. From a Linux Box to a non Linux PDA

   [http://www.adaptive-enterprises.com.au/~d/software/xcerdisp/]
   Xcerdisp is an X Windows equivalent of Microsoft's Remote Display
   Control powertoy. It listens for connections from the Windows CE
   cerdisp client on your PocketPC, and lets you see and control your
   handheld via X. It may be necessary to use the
   [http://synce.sourceforge.net/] SynCE tools to get your handheld
   connected to the network.

   The purpose of the [http://synce.sourceforge.net/] SynCE project is
   to provide a means of communication with a Windows CE or Pocket PC
   device from a computer running Linux, *BSD, or another Unix system.

   [http://www.jardino.nildram.co.uk/] KDE Pocket PC Contacts Import
   lets you import your Windows CE (or PocketPC) contacts into KDE's
   address book.

   Some more information about connectivity and synchronisation tools,
   as well as emulators and other software you may find at
   [http://tuxmobil.org/pda_linux.html] TuxMobil - PDA and in the
   [http://tuxmobil.org/howtos.html] Linux-Infrared-HOWTO .

III. Tablet PCs / Pen PCs

   Table of Contents
   9. Tablet PCs / Pen PCs

        9.1. Introduction
        9.2. Display
        9.3. Handwriting Recognition
        9.4. Keyboard
        9.5. Wireless LAN
        9.6. Examples
     ________________________________________________________________

Chapter 9. Tablet PCs / Pen PCs

9.1. Introduction

   Tablet PCs are a special kind of notebooks. Usually without keyboard
   (or equipped with an external and remote keyboard), they feature a
   touchscreen (therefore they were also named Pen PCs) and access to
   wireless LAN. In a certain sense they can be compared with PDAs.
   Microsoft has created a special edition of their operating system for
   Tablet PCs and published a so-called specification. In 2003 the first
   Tablet PCs according to this specification entered the market. Though
   there have been appropriate devices with Linux many years before. See
   the [http://tuxmobil.org/touch_laptops.html] survey of Linux touch
   screen laptops and the [http://tuxmobil.org/detach_disp.html] survey
   of Linux laptops with detachable displays and finally a
   [http://tuxmobil.org/tablet_unix.html] survey about Linux on Tablet
   PCs, WebPads, NotePads and PenPCs. They are used for data acquisition
   in stores, in the field or in hospitals. Or as a book reader or
   webbrowser (therefore they are also named WebPads). Their hardware
   features require some dedicated Linux solutions.
     ________________________________________________________________

9.2. Display

9.2.1. Touchscreen

   The [http://www.tldp.org/HOWTO/XFree86-Touch-Screen-HOWTO.html]
   XFree86-Touch-Screen-HOWTO describes how to setup X11 for
   touchscreens. There is also a short
   [http://tuxmobil.org/touch_laptops.html] survey of Linux laptops,
   which feature a touchscreen and/or have a pen as an input device and
   a [http://tuxmobil.org/tablet_unix.html] survey about Linux on Tablet
   PCs.
     ________________________________________________________________

9.2.2. Screen Rotation

9.2.2.1. X-Windows

   Some XFree86 drivers support a rotation of the display content. Use
   this entry in the configuration file (DEGREE can become CW - 90
   degree clockwise , CCW - 90 degree counterclockwise , UD - 180 degree
   upside down, but which options actually work depends on the drivers:
Option "Rotate" "DEGREE"

   From version 4.3 on [http://xfree86.org/] XFree86 contains the RandR
   extension (X resize and Rotate Extension), which makes it possible to
   change the display resolution on the fly without restarting X11. The
   tool xrandr supports only resolution settings but no rotation. But
   the Tiny-X server by RandR developer Keith Packard (Xkdrive)
   implements all of the RandR features. But this is usually not
   included in the major distributions. Currently [http://x.org/] X.Org
   doesn't seem to support rotate and resize.
     ________________________________________________________________

9.2.2.2. Utilities

   There are some rotation utilities for Linux PDAs available, but I
   haven't tested them for Tablet PCs yet. Search the
   [http://killefiz.de/zaurus/] Zaurus Software Index - ZSI.
     ________________________________________________________________

9.3. Handwriting Recognition

   [http://handhelds.org/cgi-bin/cvsweb.cgi/apps/xstroke/] xstroke is a
   full-screen gesture recognition program written for the X Window
   System. It captures gestures that are performed with a pointer
   device, (such as a mouse, a stylus, or a pen/tablet), recognizes the
   gestures and performs actions based on the gestures. xstroke has been
   developed on Linux systems, (i386 and StrongARM), but should be quite
   portable to any UNIX-like system with X.

   [http://www.handhelds.org/projects/xscribble.html] Xscribble is an X
   application that allows a user of a touch screen to input characters
   into X applications, using a uni-stroke (Graffiti like) alphabet. It
   uses the X test extension to allow synthesis of characters as though
   they had been typed on a keyboard. Though it was designed for Linux
   on PDAs it might work with Tablet PCs as well.

   [http://www.yudit.org/] Yudit is a Unicode text editor for the X
   Window System. It can do True Type font rendering, printing,
   transliterated keyboard input, and handwriting recognition with no
   dependencies on external engines. Its conversion utilities can
   convert text between various encodings. Keyboard input maps can also
   act like text converters.
     ________________________________________________________________

9.4. Keyboard

9.4.1. Soft Keyboard / On Screen Keyboard

9.4.1.1. xvkbd

   [http://homepage3.nifty.com/tsato/xvkbd/] xvkbd is a virtual
   (graphical) keyboard program for X which provides a facility to enter
   characters onto other clients software by clicking a keyboard
   displayed on the screen. It also has facility to send characters
   specified as the command line option to other client.
     ________________________________________________________________

9.4.1.2. GNOME On-screen Keyboard (GOK)

   The [http://www.gok.ca/] GNOME On-screen Keyboard (GOK) is a dynamic
   on-screen keyboard for UNIX and UNIX-like operating systems. It
   features Direct Selection, Dwell Selection, Automatic Scanning and
   Inverse Scanning access methods and includes word completion.
     ________________________________________________________________

9.4.2. Remote Keyboard

   Some Tablet PCs are equipped with a remote keyboard. Data between
   keyboard and Tablet PC may be interchanged via InfraRed, BlueTooth or
   other means. If these solutions are hardware based only, they should
   work easily with Linux. Otherwise you probably need the technical
   specifications from the manufacturer.
     ________________________________________________________________

9.4.3. Virtual Keyboard

   There are different approaches for virtual (non physical) keyboards.
   Whether they work with Linux or not I could not verify yet.

     * [http://www.vkb.co.il/] Viki made by VKB
     * [http://www.canesta.com/] Keyboard Perception Chipset made by
       Canesta
     * [http://www.senseboard.com/] SenseBoard
     * [http://www.lightglove.com/] LightGlove
     * [http://www.sait.samsung.co.kr/] Scurry made by SAIT
     * [http://www.kittytech.com/] Kitty
     ________________________________________________________________

9.5. Wireless LAN

   Please see the chapter Section 12.35 Wireless LAN below.
     ________________________________________________________________

9.6. Examples

     * [http://www.softwarekombinat.de/linux-point510.html] Fujitsu:
       Point 510
     * [http://libxg.free.fr/point/point.htm] Fujitsu: Point 510
     * [http://www.paceblade.de/?a=2&p=1493] PaceBlade: PaceBook
     * [http://simpad.sourceforge.net] Siemens: SimPAD

   At TuxMobil there is a survey of
   [http://tuxmobil.org/tablet_unix.html] Linux installations on Tablet
   PCs, Pen PCs and WebPads.

IV. Mobile (Cellular) Phones, Pagers, Calculators, Digital Cameras,
Wearable Computing

   Table of Contents
   10. Mobile (Cellular) Phones, Pagers

        10.1. Mobile (Cellular) Phones
        10.2. Pagers - SMS Messages

   11. Calculators, Digital Cameras, Wearable Computing

        11.1. Digital Cameras
        11.2. Pocket Calculators
        11.3. Wearable Computing
        11.4. Watches
        11.5. Play Station Portable
     ________________________________________________________________

Chapter 10. Mobile (Cellular) Phones, Pagers

   You may find a [http://tuxmobil.org/phones_linux.html] Linux
   compatibility survey of mobile phones at TuxMobil. This survey
   contains also links to useful applications and to mobile phones
   driven by the Linux operating system.
     ________________________________________________________________

10.1. Mobile (Cellular) Phones

10.1.1. Connectivity to Mobile (Cellular) Phones with non-Linux Operating
System

   For NOKIA cellular phones see [http://www.gnokii.org/] GNOKII
   project. And Linux [http://www.version6.net/misc/nserver.html]
   Nserver. This project aims to produce a GPL replacement for Nokia's
   Windows Nserver, and maybe improve upon it along the way. Initially
   it will emulate the Windows 3.1 version (ie. allow backup, restore
   and install).

   [http://www.openwap.org/] openWAP is an open source project for the
   implementation of the Wireless Application Protocol (WAP) for use
   with browsers, servers and tools. WAP is used by PDA devices, cell
   phones, pagers and other wireless devices to transmit internet
   content to these devices. The project is still in its early stages
   and nothing can be downloaded yet.

   [http://www.pxh.de/fs/gsmlib/download/] GSMLIB is a library to access
   GSM mobile phones through GSM modems. Features include: modification
   of phonebooks stored in the mobile phone or on the SIM card, reading
   and writing of SMS messages stored in the mobile phone, sending and
   reception of SMS messages. Additionally, some simple command line
   programs are provided to use these features.

   [http://www.kannel.org/] Kannel is an open source WAP gateway. It
   attempts to provide this essential part of the WAP infrastructure
   freely to everyone so that the market potential for WAP services,
   both from wireless operators and specialized service providers, will
   be realized as efficiently as possible.

   Kannel also works as an SMS gateway for GSM networks. Almost all GSM
   phones can send and receive SMS messages, so this is a way to serve
   many more clients than just those using a new WAP phone.
     ________________________________________________________________

10.1.2. Mobile (Cellular) Phones with a Linux Operating System

   There are some [http://tuxmobil.org/phones_linux.html] mobile phones
   with Linux operating system available. As well as
   [http://tuxmobil.org/mobile_phone_linux_distributions.html] Linux
   distributions for mobile (cell) phones.
     ________________________________________________________________

10.2. Pagers - SMS Messages

   [http://www.qpage.org/] QuickPage is a client/server software package
   that enables you to send messages to an alphanumeric pager. The
   client accepts a message from the user and forwards it to a server
   using SNPP. The server uses a modem to transmit the message to the
   recipient's paging service using the TAP protocol (also known as the
   IXO protocol).

   [http://daniel.haxx.se/projects/mail2sms/] mail2sms converts a (MIME)
   mail to a short message, allowing search/replace, conditional rules,
   date/time dependent actions, customizing the output format, etc. The
   output defaults to 160 characters, which is perfectly suitable for
   sending the text to a GSM telephone as an SMS message. This software
   does not include any code for actually sending the text to anything
   else but another program or stdout.

   [http://www.new.ox.ac.uk/~adam/computing/email2sms/] email2sms is a
   filter written in Perl which converts an e-mail into a form suitable
   for sending as an SMS message. Its main advantage over the
   alternatives is that it uses the CPAN module Lingua::EN::Squeeze to
   compress the text down to as little as 40% of its original size, so
   you can get much more of your e-mail into the 160 character limit
   imposed by SMS. It is fully MIME compatible, and has many
   configurable options, including removal of quoted text. Ideal for use
   with procmail. A Perl script for sending the output to a typical
   e-mail to SMS web gateway is included.

   [http://smslink.sourceforge.net/] SMSLink implements a client/server
   gateway to the SMS protocol. It requires the use of dedicated
   hardware though (a serial GSM module). Both SMS emission and
   reception are supported. The server only runs under Linux at the
   present time and also supports interactive mode via telnet. The
   command-line client already exists for Linux, Solaris and HP-UX. A
   basic web interface is provided. A Win32 client is in the works.

   [http://lide.pruvodce.cz/~wayne/] nmsms is a very simple program to
   announce incoming email to an SMS address (email address) defined at
   compile time. The original From: and Subject: header are included in
   each mail announced.
     ________________________________________________________________

Chapter 11. Calculators, Digital Cameras, Wearable Computing



   We are all cyborgs.
     probably from "Cyborg Manifesto" by Donna J. Haraway in Simians,
   Cyborgs, and Women. The Reinvention of Nature. New York: Routledge,
   1991

   Though in my opinion related to the topic, these devices are not much
   covered in this text, yet. For general information about Embedded
   Systems, see [http://www.embedded.com] Embedded.com . For Linux
   information, see [http://elks.sourceforge.net/] ELKS and the
   [http://uclinux.org/] uCLinux project. See also the news group
   comp.arch.embedded
     ________________________________________________________________

11.1. Digital Cameras

11.1.1. Related Documentation

    1. [http://www.marblehorse.org/projects/documentation/kodak/]
       Kodak-Digital-Camera-HOWTO by David Burley
       <khemicals_AT_marblehorse.org> .
     ________________________________________________________________

11.1.2. Introduction

   For information about cellular phones and digital cameras see the
   [http://tuxmobil.org/ir_misc.html] Infrared Devices and Linux Survey
   and my [http://tuxmobil.org/howtos.html] InfraRed-HOWTO .

   Newsgroup: rec.photo.digital .

   The Flashpath adapter is a diskette like device which is used to
   transfer data from a digital camera to a computer. See
   [http://www.smartdisk.com/Downloads/FPDrivers/LinuxDownload.htm]
   Flashpath for Linux and James Radley's
   [http://www.susie.demon.co.uk/flashpath.html] flashpath homepage .
   Note: it is not officially certified and released under GPL.
     ________________________________________________________________

11.2. Pocket Calculators

   Information about calculators e.g. HP-48 is at
   [http://www.hpcalc.org/] HP-Calculator.Org, they are hosting the
   [http://www.hpcalc.org/hp48/docs/faq/48faq.html] HP-48 FAQ.
   [http://www.columbia.edu/kermit/hp48.html] HP-48 Kermit Hints and
   Tips shows how to talk to the HP48 via its serial-line Kermit
   protocol. The HP-48 may also be used as a
   [http://www.opensourcepartners.nl/~costar/hp48/] Linux terminal.

   See also at my pages about [http://tuxmobil.org/ir_misc.html] Linux
   with Infrared Devices and [http://tuxmobil.org/calculators_unix.html]
   Linux and Pocket Calculators .

   [http://www.multimania.com/rlievin/] GtkTiLink is a program which
   allows you to transfer data between a Texas Instruments calculator
   and a computer. It works with all cables (parallel, serial, Black and
   Gray TI Graph Link). It supports the TI82, TI89, TI92 and TI92+
   calculators. It can send/receive data and backups, make a capture of
   the calculator screen and do remote control.
     ________________________________________________________________

11.3. Wearable Computing

   Also related to Linux and mobile computers seems wearable computing.

   See also [http://www.media.mit.edu/wearables/] MIT ,
   [http://wearables.blu.org/] Wearables Central and
   [http://www.wearcomp.org/] WearComp .
     ________________________________________________________________

11.4. Watches

   The [http://datalink.fries.net/] datalink library allows sending
   information to the Timex DataLink watches. The original datalink
   library supports the DataLink models 70 , 150 and 150 S watch and has
   been extended to work with the DataLink Ironman Triathlon watch. It
   has been tested with the SVGA output on the Ironman watch only, other
   output devices and other watches may or may not work, I have no
   reports either way. The display must be a CRT display (not a LCD).
     ________________________________________________________________

11.5. Play Station Portable

   [http://qpspmanager.sourceforge.net/] qpspmanager is a program to
   manage the files on a memorystick as used by a Sony Playstation
   Portable.

V. Mobile Hardware in Detail

   Table of Contents
   12. Hardware in Detail: CPU, Display, Keyboard, Sound and More

        12.1. Introduction
        12.2. BIOS
        12.3. CPU
        12.4. Centrino(tm), Centrino-Duo(tm)
        12.5. PCMCIA Controller
        12.6. Graphics Chip
        12.7. DVI Port
        12.8. Video Port / ZV Port
        12.9. LCD Display
        12.10. Sound
        12.11. Keyboard
        12.12. Extra Keys / Hot Keys
        12.13. Function Key
        12.14. Power Key
        12.15. Extra LEDs
        12.16. Numeric Keypad
        12.17. Pointing Devices - Mice and Their Relatives
        12.18. Advanced Power Management - APM
        12.19. ACPI
        12.20. Power Management Unit - PMU (PowerBook)
        12.21. Batteries
        12.22. Memory
        12.23. Plug-and-Play Devices (PnP)
        12.24. Docking Station / Port Replicator
        12.25. Network Connections
        12.26. Built-In Modem
        12.27. GPRS
        12.28. SCSI
        12.29. Universal Serial Bus - USB
        12.30. FireWire - IEEE1394 - i.Link
        12.31. Floppy Drive
        12.32. Optical Drives (CD/DVD)
        12.33. Hard Disk
        12.34. Hot-Swapping Devices (MultiBay, SelectBay, ..)
        12.35. WireLess Network - WLAN
        12.36. BlueTooth
        12.37. Infrared Port
        12.38. FingerPrint Reader

   13. Accessories: PCMCIA, USB and Other External Extensions

        13.1. PCMCIA Cards
        13.2. ExpressCards
        13.3. SmartCards
        13.4. SDIO Cards
        13.5. Memory Technology Devices - RAM and Flash Cards
        13.6. Memory Stick
        13.7. Card Readers for SD/MMC/Memory Stick
        13.8. USB Devices
        13.9. Printers and Scanners
        13.10. Serial Devices
        13.11. External Storage Devices
        13.12. Power and Phone Plugs, Power Supply
        13.13. Bags and Suitcases
     ________________________________________________________________

Chapter 12. Hardware in Detail: CPU, Display, Keyboard, Sound and More

12.1. Introduction

   The following text about mobile hardware, is applicable to all kinds
