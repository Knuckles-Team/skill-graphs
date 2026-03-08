   Linux Laptop and Notebook Survey: Apple.
     ________________________________________________________________

3.4.15. Mass Installation

3.4.15.1. 2.5" to 3.5" IDE Adapter

   If you have a 2,5" to 3,5" IDE drive adapter you can install one of
   the laptops, and with a desktop computer clone this harddisk to the
   disks of the other 99 laptops. You can use the DOS utility GHOST
   (works pretty with ext2) or with tar if the desktop works in linux.
   You only need an additional boot disk for the reinstall of the lilo
   in each laptop and change the hostname and IP address. These adapter
   are usually quite cheap (app . ten dollar, but difficult to get) .
     ________________________________________________________________

3.4.15.2. SystemImager

   [http://systemimager.sourceforge.net] VA SystemImager is software
   that makes the installation of Linux to masses of similar machines
   relatively easy. It also makes software distribution, configuration,
   and operating system updates easy. You can even update from one Linux
   release version to another! VA SystemImager can also be used for
   content management on web servers. It is most useful in environments
   where you have large numbers of identical machines. Some typical
   environments include: Internet server farms, high performance
   clusters, computer labs, or corporate desktop environments where all
   workstations have the same basic hardware configuration.
     ________________________________________________________________

3.4.15.3. Debian/GNU Linux

   You might want to take a look at
   [http://www.informatik.uni-koeln.de/fai] FAI - Fully Automatic
   Installation.
     ________________________________________________________________

3.4.15.4. SuSE

   The package ALICE - Automatic Linux Installation and Configuration
   Environment, offers CVS-based configuration files and configuration
   templates.
     ________________________________________________________________

3.4.15.5. Replicator

   Replicator is a set of scripts to automate the duplication of a
   Debian GNU/Linux installation from one computer to another.
   Replicator makes an effort to take into account differences in
   hardware (like HD size, video card) and in software configuration
   (such as partitioning). After the initial configuration, the scripts
   will create a bootdisk that allows you to completely (re)install a
   Debian box by booting from the floppy and answering a yes/no
   question.
     ________________________________________________________________

3.4.15.6. partimage

   [http://partimage.sourceforge.net/] Partition Image is a Linux/UNIX
   utility which saves partitions in the ext2fs (the linux standard),
   ReiserFS (a new journalized and powerful file system) or FAT16/32
   (MS-DOS and MS-Windows file systems) file system format to an image
   file. The image file can be compressed in the GZIP/BZIP2 formats to
   save disk space, and split into multiple files to be copied on
   floppies (ZIP for example).
     ________________________________________________________________

3.5. Common Problems During Installation

3.5.1. Display Problems (Missing Lines, Thick Borders)

   A common problem during Linux installation (or afterwards) on laptops
   are missing lines at the bottom of the text console display, so the
   last command lines or the login prompt are not shown on the screen.
   Depending on the problem it might help:

     * Either using FrameBuffer, e.g. using a Kernel with framebuffer
       support and a boot option like vga=791, for details see the
       [http://tldp.org/HOWTO/Framebuffer-HOWTO.html] FrameBuffer-HOWTO.
     * Or disabling FrameBuffer, e.g. using a boot option like
       vga=normal or another resolution Also, you could try passing
       video=vga16:off on the installer boot prompt.
     * As a workaround often it is possible to switch to a second
       console e.g. <ALT>+<F2> , because this effect is often only
       related to the first console.
     * Check if there are VGA and video boot options configured in the
       bootloader (e.g. grub, lilo). Try to disable them at least
       partly, look for options like ywrap, etc.
     * Check the BIOS for display settings, often (older) Toshiba
       laptops behave like this.
     * Issue the command resize to get the correct screen size into the
       system.
     * If none of the above helps, you may try to run a start-up-script,
       which has to run at the end of the boot process. The script has
       to contain the clear command and/or the reset.

II. Handheld Devices - Personal Digital Assistants (PDAs)

   Table of Contents
   4. Palmtops, Personal Digital Assistants - PDAs, Handheld PCs - HPCs

        4.1. Resources

   5. History of Linux on PDAs

        5.1. Itsy

   6. Linux PDAs

        6.1. AgendaComputing: Agenda VR3
        6.2. Samsung: YOPY
        6.3. SHARP SL-5000/5500/C700-860/C3x00/6000 aka Zaurus

   7. Non-Linux PDAs - Ports and Tools

        7.1. HELIO
        7.2. iPAQ
        7.3. Newton Message Pad
        7.4. PALM-Pilot
        7.5. HandSpring VISOR
        7.6. Psion 5

   8. Connectivity

        8.1. From a Linux Box to a non Linux PDA
     ________________________________________________________________

Chapter 4. Palmtops, Personal Digital Assistants - PDAs, Handheld PCs -
HPCs



   Linux PDAs, because using your palm isn't as good as the real thing.
     Motto of [http://zaurus.loveslinux.com] ZaurusLovesLinux
     ________________________________________________________________

4.1. Resources

    1. Highly recommended is the page by Russell King
       [http://www.arm.uk.linux.org/~rmk/] ARM Linux about PDAs with ARM
       CPU and with links to other Linux related PDA sites.
    2. For more information on Virtual Network Computing, see
       [http://www.realvnc.com/] VNC .
    3. PDAs and infrared remote control, see
       [http://hp.vector.co.jp/authors/VA005810/remocon/remocone.htm]
       Hiromu Okada .
    4. There is also the [http://www.cdpubs.com/hhsys/archives.html]
       Handheld Systems(TM) On-line Archives and a search engine about
       palmtop related topics [http://www.palmtop.net/] Palmtop.Net/ .
    5. I have setup a page about [http://tuxmobil.org/pda_linux.html]
       Linux with PDAs and Handheld PCs , too.
    6. These newsgroups for PDA application developers are available:
       codewarrior.embedded; codewarrior.games; codewarrior.linux;
       codewarrior.mac; codewarrior.palm; codewarrior.unix;
       codewarrior.windows;
     ________________________________________________________________

Chapter 5. History of Linux on PDAs

   This chapter is not complete yet, there should be more information on
   286 based PDAs which were Linux capable.
     ________________________________________________________________

5.1. Itsy

   The Itsy prototype offered considerably more computing power and
   memory than other PDAs of its time, enabling demanding applications
   such as speech recognition. It was designed as an open platform to
   facilitate innovative research projects. The base Itsy hardware
   provided a flexible interface for adding a custom daughtercard, and
   Itsy software has been based on the Linux OS and standard GNU tools.
     ________________________________________________________________

5.1.1. Resources

    1. COMPAQ/Digital is the manufacturer of the
       [http://research.compaq.com/wrl/projects/itsy/] Itsy.
     ________________________________________________________________

Chapter 6. Linux PDAs

   The most known Linux PDAs in these days are the
   [http://tuxmobil.org/pda_survey_agenda.html] Agenda VR3 by
   AgendaComputing (out-of-production), the
   [http://tuxmobil.org/pda_survey_compaq.html] iPAQ by HP/COMPAQ, the
   [http://tuxmobil.org/pda_survey_sharp.html] Zaurus series by SHARP,
   and the [http://tuxmobil.org/pda_survey_samsung.html] Yopy by Samsung
   (out-of-production). Except the iPAQ all of them are true Linux PDAs,
   they are pre-equipped with Linux by their manufacturers.

   There are different free distributions for Linux PDAs available,
   e.g.: [http://www.trolltech.com/] QT Embedded (pre-installed on the
   SHARP Zaurus), [http://opie.handhelds.org/] Opie,
   [http://familiar.handhelds.org/] Familiar. The
   [http://gpe.handhelds.org/] Gnome Palmtop Environment - GPE aims to
   provide a Free Software GUI environment for palmtop/handheld
   computers running the GNU/Linux operating system. GPE uses the X
   Window System, and the GTK+ widget toolkit.

   Most of the software for the newer PDAs can be obtained as
   pre-compiled IPK packages. You may search the
   [http://www.killefiz.de/zaurus/] Zaurus Software Index - ZSI or
   [http://ipkgfind.handhelds.org/] ipkgfind for the package you need.
   To install these packages you may choose different methods. One
   method is to install directly via a HTTP connection called feed. For
   an example see the [http://tuxmobil.org/feed.html] TuxMobil IPK feed.

   Besides these well-known Linux PDAs I will also try to point to ports
   for other PDAs and to tools to achieve connectivity to non-Linux
   PDAs, cell phones and desktop computers.
     ________________________________________________________________

6.1. AgendaComputing: Agenda VR3

6.1.1. Resources

    1. The manufacturer of the first dedicated Linux PDA the Agenda VR3
       is AgendaComputing (out-of-business).
     ________________________________________________________________

6.2. Samsung: YOPY

6.2.1. Resources

    1. [http://www.samsung.com/] Samsung is the manufacturer of the
       Yopy.
    2. The German
       [http://www.linux-magazin.de/News/index_html?newsid=519]
       Linux-Magazin about the YOPY.

   Figure 6-1. Screenshot of the YOPY PDA

   [yopy.png]
     ________________________________________________________________

6.3. SHARP SL-5000/5500/C700-860/C3x00/6000 aka Zaurus

   The SHARP Zaurus SL-5000/5500 wasn't the first Linux PDA, but the one
   with the greatest success in the Linux community and beyond.

   Figure 6-2. Screenshot of the SHARP Zaurus SL-5500 PDA.

   [zaurus1.png]
     ________________________________________________________________

6.3.1. The SHARP System

   You may find the official site for information about Linux on the
   Zaurus at [http://developer.ezaurus.com/] SHARP Japan (in Japanese).
   You can get the official kernel, either complete or just the patches
   for the Zaurus there. You can also get the official root-filesystem,
   that is the initrd, but without the [http://qpe.sourceforge.net/]
   QTopia environment. Check the documentation at SHARP how to create
   your zImage, bootflag and initrd for flashing the ROM of the Zaurus
   with your custom setup. Or go to your country-specific division of
   SHARP to get a complete ROM in one file called "ospack", which is
   [http://www.zaurus.de/] Zaurus.DE for Germany or
   [http://www.myzaurus.com/] MyZaurus for the US versions. The kernel
   is rather old: 2.4.6 with 2.4.6-rmk2-patches and some more from
   [http://www.lineo.com/] Lineo. The rmk-patches are from
   [http://www.arm.uk.linux.org/] Linux ARM Community. The root
   filesystem from SHARP is known for its weird structure with symbolic
   links all over the place. The custom compile worked. Remember to hit
   the "/"-key when the Zaurus displays "Wait... ", so you can choose to
   start a login instead of QTopia, which is not available then. Unless
   you downloaded QTopia, (cross-)compiled it and installed it into the
   root filesystem. BTW, you can create a new user with "adduser", a
   command provided by BusyBox. [http://www.busybox.org/] BusyBox ,
   provides nearly all UNIX-commands available on the official system.
     ________________________________________________________________

6.3.2. The Community Systems

   Currently I know of two running systems: OpenZaurus and Debian
   (unofficial).
     ________________________________________________________________

6.3.2.1. OpenZaurus

   [http://openzaurus.org/] OpenZaurus tries to create the same
   environment as the one from SHARP, but based upon free software only.
   At the moment, it still uses the old kernel from Sharp, but slightly
   modified in regards of usage of the FLASH-ROM as RAM and division of
   RAM between RAMDISK and RAM. Unfortunately, the driver for the
   SD-controller is binary-only and thus non-free. But also SHARP itself
   tries to convince the vendor, SDCA, to provide the sources for the
   public. Moreover, [http://openzaurus.org/] OpenZaurus created a sane
   root-filesystem we all know from our regular Linux systems. It also
   replaces QTopia by [http://opie.handhelds.org] Open Palmtop
   Integrated Environment - OPIE , which is a fork from QTopia with no
   relations to Trolltech anymore. All applications from QTopia should
   run on OPIE, but not quite: The Doom-like game called Zraycast does
   not run on OPIE, but does on QTopia (more or less). You can download
   a ready zimage, bootflag and initrd directly or checkout the sources
   from CVS. The downloaded images worked fine.
     ________________________________________________________________

6.3.2.2. Debian

   The current, unofficial version of
   [http://people.debian.org/~mdz/zaurus/] Debian Zaurus really tries to
   be a regular Debian system with apt and X. A simple version of dpkg
   is already shipped with [http://www.busybox.org/] BusyBox , which
   makes it a little bit easier. The maintainer has therefore stripped
   down some more tools to fit them into the Flash-ROM. It uses the
   kernel provided by [http://openzaurus.org/] OpenZaurus and thus the
   one from Sharp. There are some issues with the RAMdisk, calibration
   of the stylus and sleep / power-off/-on. As soon as it is in a more
   stable state, it will join forces with
   [http://emdebian.sourceforge.net/] EmDebian and the sources will
   become available (probably already furnished upon request). The
   downloaded images still have to be tweaked. :) All systems, including
   the sources from SHARP, are set to use the US keyboard layout (or the
   German keyboard). It seems that the keymap available is fixed in the
   kernel and there are no user-space tools installed per default to
   change this. Perhaps I will give the package "console-tools" on
   Debian a try.
     ________________________________________________________________

6.3.2.3. PocketWorkStation

   Here are some of the features of [http://www.pocketworkstation.net/]
   PocketWorkStation a Debian/GNU Linux distribution for PDAs:

     * Full Debian GNU/Linux operating environment, with easy access to
       the many GB of available software. Want the Konqueror web browser
       and have 50MB free space on your SD card? Run apt-get install
       konqueror, go eat lunch and come back to find it ready to run. No
       porting needed.
     * Includes X11 able to run most Linux applications - it supports
       virtual screens larger than the physical screen, realtime
       anti-aliased scaling and rotation, 3-mouse-button emulation and a
       full keyboard (useful i.e. if you need to send Ctrl-Alt-Del to an
       application).
     * VNC client fbvnc (same features as X11 above) - remote administer
       your NT box from your Zaurus.
     * Runs completely out of a single directory (a 256MB SD card is
       ideal), no re-flashing or modification of the existing operating
       system is required.
     * Switch between QTopia and X11 whenever you like without rebooting
       or needing to stop any of your X11 applications.
     ________________________________________________________________

6.3.3. Synchronization with your Linux PC

   The QTopia-Desktop is available as a download from
   [http://www.trolltech.com/developer/download/qtopia.html] Trolltech
   for free (as in beer): There is a [http://docs.zaurus.com] FAQ, which
   explains the necessary steps for setup (Ethernet-over-USB). It is not
   quite up-to-date, because SHARP has tightened the security with their
   current ROM-release, so you have to give the IP-address 192.168.129.1
   to your usb0 network device. You have to download and compile a patch
   for your kernel to use the driver usbdnet (see aforementioned
   website). Afterwards, a connection between the QTopia-Desktop and the
   Zaurus is possible. I had a lot of problems with the usb network
   layer on my system and could not sync properly. A switch from the
   driver uhci to usb-uhci for my host dit it. Just recently I had to
   reboot my notebook and the Zaurus due to a hiccup in the
   corresponding usb-net drivers. The network via an ethernet-card in
   the CF-slot is much more reliable than the connection via usb and you
   can still use the keyboard. The disadvantage is, that you cannot have
   a storage device in your CF-slot while you are on-line.
     ________________________________________________________________

6.3.4. External Serial Keyboard

   So far I was not able to get it going. There is a site which offers a
   [http://www.doc.ic.ac.uk/~jpc1/linux/ipaq/serial.html] serial
   keyboard driver and a patch for the iPAQ . Since the iPAQ and the
   Zaurus are based on the same CPU architecture, StrongArm, I hope that
   the driver provided there will also work on the Zaurus. You also need
   a user-space tool called inputattach, which you can also get from
   there (source or binary for ARM). I got a Happy Hacking Keyboard Lite
   with a PS/2 connector. An adaptor translates to serial which itself
   is plugged into to the Collie serial <-> serial connector. I do not
   know if this chain is even possible to work. The provided patch
   applied with only one failing hunk which made a trivial change in the
   sources (include/linux/serio.h) necessary; check the output. After
   having re-configured the SHARP kernel config and having compiled the
   modules, I transferred them to the Zaurus. The modules marked and
   created are: newtonkbd.o, serio.o, serport.o and perhaps stowaway.o
   from drivers/char/joystick/ and input.o and keybdev.o from
   drivers/input/. When you start inputattach, you have to use the line
   inputattach --newtonkbd /dev/ttyS0, _not_ ttySA0 as stated on the
   website. For some strange reason, the Collie serial driver does not
   comply to the official StrongARM documentation of the kernel, which
   states that the serial ports are accessible via /dev/ttySAx. And
   because the serial_collie.o is already compiled into the Sharp
   kernel, you do not have to load the generic module serial.o. Well, I
   also tried the serial_collie.o as a module, while it was still
   compiled into the kernel. There were no complaints when loading it,
   but the system froze unpredictably, so I had to do a soft-reset quite
   often. Why can I load a module whose code is already in the kernel, I
   wonder... Anyway, it does not work. :( I tried inputattach in the
   --dump mode (you have to undefine a variable in the source and
   recompile) and it seems that there is nothing happening between the
   serial port and the keyboard. The call for select (man 2 select)
   fails due to a timeout.
     ________________________________________________________________

6.3.5. Cross-Compiling

6.3.5.1. Kernel

   In order to build the kernel, initrd and applications you need a
   cross-compiling environment, GCC is preferred.
   [http://emdebian.sourceforge.net/] EmDebian offers .deb packages for
   Debian GNU/Linux i386. Note: you have to look up the download links
   in the old site (a link is provided on the new site), because they
   are missing on the new site (though the download page exists). There
   are some dependency problems with the g++ and libstdc++-dev packages
   which can be "resolved" with a --force-depends. The package
   libstdc++-dev has some problems finding an info-file: just create a
   symlink from /usr/share/info/iostream.ifo.gz to
   /usr/share/info/iostream-295.info.gz. You should get some pointers
   for other systems at the [http://www.arm.uk.linux.org/] Linux ARM
   Community. Once installed, you can grab a standard kernel, apply the
   current ARM-patches and modify the top Makefile to target the
   arm-architecture. I did not try that so far.
     ________________________________________________________________

6.3.5.2. Applications

   Check the [http://qpe.sourceforge.net/sharp.html] QTopia pages for
   more info and the [http://qpe.sourceforge.net/development.html]
   QTopia - Development pages.
     ________________________________________________________________

6.3.5.3. Tool Chains

   Werner Schulte explains how to build a OPIE development Live CD. The
   CD contains an ISO image with the tools and methods described in his
   [http://www.uv-ac.de/opiedev] Opie Development HOWTO - LiveCD
   chapter. The CD allows the user to crosscompile OPIE programs without
   having a cross-compiler installed on his linux-box (also i386
   embedded available).

   Instructions for building a
   [http://www.lucid-cake.net/osx_arm/index_en.html] cross-compiling GCC
   for the Zaurus under Mac OS X.

   A [http://www.pellicosystems.com/demolinux/zdemolinux/index.html]
   DemoLinux distribution to show the Trolltech Qtopia development
   environment for the SHARP Zaurus Personal Mobility Tool or any ARM
   based device running the Trolltech QPE system provided by Pellico
   Systems.

   [http://kopsisengineering.com/kopsis/SharpZaurusSdkDsl] Zaurus
   Development with Damn Small Linux offers a cross-development
   environment to build binaries for the ARM processor used in the SHARP
   Zaurus Linux PDAs. You may run it either inside the QEMU virtual
   machine or from a Live CD.

   [http://free-electrons.com/community/tools/kernelkit/en] KernelKit is
   a Knoppix derivative dedicated to developers of Linux device drivers
   and Free Software embedded systems. In particular, it includes uClibc
   cross-compiling toolchains for several embedded architectures
   (currently ARM, i386, MIPS, mipsel, PPC, and m68k) and emulators
   (currently qemu and SkyEye). It can be used for demonstration or
   training purposes, or by developers who cannot install GNU/Linux on
   their workstations.
     ________________________________________________________________

6.3.6. Caveats

   SHARP introduced a proprietary serial interface at the bottom of the
   Zaurus SL-5x00 series. You can buy an adaptor to a regular serial
   interface from them, but unfortunately, the plug is very thick and
   you cannot open the slide for the keyboard anymore. Hopefully, you
   can still plug an external keyboard into this port! You can at least
   plug the power cord into the adaptor so you do not have to run on
   battery. There are third-party adaptors available, which overcome
   this caveat.

   There is no speaker for the soundchip of the SL-5500. You have to use
   the socket for the headphones to hear OggVorbis and the alikes. The
   buzzer currently supports only 14 different sounds defined in
   <kernel-source>/include/asm-arm/sharp_char.h , check for
   SHARP_BUZ_ALL_SOUNDS.
     ________________________________________________________________

6.3.7. Resources

6.3.7.1. Manufacturer: SHARP

    1. [http://docs.zaurus.com] ZaurusZone.
    2. [http://more.sbc.co.jp/slj/linux.asp] Sharp Linux/Java PDA Linux
       Information
    3. [http://www.zaurus.com/dev/] Sharp Zaurus Developer's Program
     ________________________________________________________________

6.3.7.2. Kernel and Community Distributions

    1. [http://www.arm.uk.linux.org/] ARM Linux
    2. [http://emdebian.sourceforge.net/] Emdebian
    3. [http://openzaurus.org/] OpenZaurus Project
    4. [http://www.doc.ic.ac.uk/~jpc1/linux/ipaq/serial.html] Linux
       serial keyboards
     ________________________________________________________________

6.3.7.3. FAQs, Forums, etc.

    1. [http://zaurus.help4free.de/html/modules/news/] Sharp Zaurus
       Hilfe und Support Community (German)
    2. [http://www.zaurususergroup.com/modules.php?op=modload&name=FAQ&f
       ile=index] Unofficial Sharp Zaurus SL-5500 FAQ
    3. [http://docs.zaurus.com] Sharp Zaurus - Developer Site
    4. [http://www.handhelds.org] handhelds.org - mobile Devices
     ________________________________________________________________

6.3.7.4. Applications, Desktop Environments

    1. [http://opie.handhelds.org] Open Palmtop Integrated Environment
       (OPIE)
    2. [http://gpe.handhelds.org] GPE Palmtop Environment, GTK-based
       alternative to OPIE
    3. [http://qpe.sourceforge.net] QTopia
    4. [http://www.trolltech.com/developer/download/qtopia.html]
       QTopia-Desktop
    5. The [http://www.uv-ac.de/ipaqhelp] iPAQ and Zaurus Development
       using QPE handbook by Werner Schulte describes how to install the
       Familiar Linux and Qtopia / OPIE on the Compaq iPAQ Handheld (and
       SHARP Zaurus) and how to develop applications for the iPAQ/Zaurus
       using the Familiar distribution and QPE desktop from Trolltech or
       OPIE (the free clone).
     ________________________________________________________________

6.3.7.5. Software Indexes

    1. [http://www.killefiz.de/zaurus/] Zaurus Software Index - ZSI
    2. [http://ipkgfind.handhelds.org] IPKGfind Software Index
     ________________________________________________________________

6.3.8. Conversion from Palm Pilot to Zaurus

   See my [http://tuxmobil.org/go2z.html] survey of applications and
   conversion tools between a conventional PDA operating system (only
