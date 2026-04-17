
   From the [http://tldp.org/HOWTO/Hardware-HOWTO/] Hardware-HOWTO I
   know there is Trimble Mobile GPS available for Linux. You may also
   connect a GPS via a serial port. Most GPS receivers have a data port
   and can connect to a PC with a special serial cable.

     * Differential GPS is a technique to apply a correction factor from
       a known location to a GPS signal. This can substantially reduce
       the uncertainty in the GPS location. Normally the correction
       signal is acquired using a special radio receiver: dgpsip allows
       you to receive a DGPS signal via TCP/IP, and send it to the GPS
       connected to your serial port.
     * [http://www.wombat.ie/gps/] DGPS is a project to put together a
       low cost hardware and software solution for Differential GPS (in
       both real time mode using RTCM correction format and in post
       processed mode).
     * [http://www.mayko.com/gpsd.html] gpsd is a daemon that listens to
       a GPS or Loran receiver and translates the positional data to
       simplified format that can be more easily used by other programs,
       like chart plotters. The package comes with a sample client that
       plots the location of the currently visible GPS satellites (if
       available) and a speedometer. Added support for the DeLame
       EarthMate as well as a new 'speedometer' mini client.
     * The [http://www.gbdirect.co.uk/] QtGPS package contains a piece
       of software for UNIX/Linux/X and a GPS receiver. It performs
       logging and replaying of a journey, supporting a moving-map
       display. QtGPS works with Lat/Long and British OSGB (Ornance
       Survey) coordinate systems.
     * [http://www.geog.uni-hannover.de/grass/index.php] GRASS
       (Geographic Resources Analysis Support System) is a free software
       raster and vector based GIS, image processing system, graphics
       production system, and spatial modeling system.
     * [http://www.easy.net/users/fgiannan/xaprs/] XASTIR is a free APRS
       (Automatic Position Reporting System) program. APRS(tm) was
       developed to track mobile GPS stations with two-way radio to
       convey position reports, messaging, weather and more. XASTIR
       plots this information on a map on your screen where you can see
       the entire world or zoom down to street level.
     * [http://www.amphibious.org/gps.html] as-gps contains a basic
       support library for accessing the inexpensive ($20) Aisin-Seiki
       GPS Module previously available at mavin.com. The package also
       includes several simple console utilities for dumping satellite
       status, location, and time and for synchronizing the system
       clock.
     * [http://academy.cas.cz/~gis/] gmap is a map viewer with emphasis
       on temporal data. It hopes to evolve into a free and powerful
       Geographical Information System.
     * [http://www.mgix.com/gps3d/] gps3d is a set of utilities that
       lets you manipulate your GPS from your Linux box. One nice
       feature is the ability to view GPS data (track, waypoints, fix,
       etc.) on an OpenGL, 3D texture-mapped model of earth.
     ________________________________________________________________

16.12. Connection via Amateur Radio (HAM)

   As far as I know laptops are used in amateur radio contests. Please
   see HAM-HOWTO by Terry Dawson, VK2KTJ,
   <terry_AT_perf.no.itg.telstra.com.au>.

   [http://www.easy.net/users/fgiannan/xaprs/] XASTIR is a free APRS
   (Automatic Position Reporting System) program. APRS(tm) was developed
   to track mobile GPS stations with two-way radio to convey position
   reports, messaging, weather and more. XASTIR plots this information
   on a map on your screen where you can see the entire world or zoom
   down to street level.
     ________________________________________________________________

16.13. Satellite Watching

   Together with an antenna and software like seesat or sattrack you can
   use a laptop to locate a satellite for visual observation. You could
   also use xephem on a laptop when stargazing. See also the
   [http://tldp.org/HOWTO/Astronomy-HOWTO/] Astronomy-HOWTO .
     ________________________________________________________________

16.14. Aviation

   Many people are using laptops for aviation related topics. The
   [http://metalab.unc.edu/fplan/Aviation-HOWTO/] Aviation HOWTO
   provides pointers to software packages that run under the Linux
   operating system and are useful to private, commercial, or military
   pilots. The ultimate goal is to enable pilots to use the Linux
   operating system for all their aviation related computing needs.
     ________________________________________________________________

16.15. Blind or Visually Impaired Users

   There are some groups of which could gain a specific profit by using
   laptops. For instance blind or visually impaired people (I explicitly
   avoid to say handicapped people). See
   [http://tldp.org/HOWTO/Accessibility-HOWTO/] Accessibility-HOWTO and
   [http://leb.net/blinux/] Blinux - Linux for blind people for more
   information. brltty is a program which supports different braille
   terminals. Festival is a speech synthesis system. Screen and cursor
   magnifiers are available. See TuxMobil for a
   [http://tuxmobil.org/mobile_blind.html] small survey of laptop
   installation reports by or for blind people.

VIII. Appendix

   Table of Contents
   A. Other Operating Systems

        A.1. Microsoft DOS and Windows
        A.2. BSD UNIX
        A.3. OS/2
        A.4. NOVELL Netware
        A.5. Debian GNU/Hurd (hurd-i386)

   B. Other Resources

        B.1. Main WWW Resources
        B.2. Mailing Lists
        B.3. USENET Newsgroups
        B.4. Newsletters, RSS Channels
        B.5. Magazines, Blogs Newsletters
        B.6. General Laptop Information

   C. Repairing the Hardware
   D. Survey about Micro Linuxes
   E. Dealing with Limited Resources or Tuning the System

        E.1. Related Documentation
        E.2. Introduction
        E.3. Small Space
        E.4. Hard Disk Speed
        E.5. Small Memory
        E.6. Low CPU Speed
        E.7. Power Saving Techniques
        E.8. Kernel
        E.9. Tiny Applications and Distributions
        E.10. Hardware Upgrade

   F. Ecology and Laptops

        F.1. Ecological Comparisons of Computers

   G. NeoMagic Graphics Chipset Series NM20xx

        G.1. Introduction
        G.2. Textmode 100x37

   H. Annotated Bibliography: Books For Linux Nomads
   I. Resources for Specific Laptop Brands

        I.1. COMPAQ
        I.2. DELL
        I.3. IBM/Lenovo(TM) ThinkPad
        I.4. Sony VAIO
        I.5. Toshiba

   J. Credits
   K. Copyrights

        K.1. Copyrights
        K.2. GNU Free Documentation License - GFDL
     ________________________________________________________________

Appendix A. Other Operating Systems

A.1. Microsoft DOS and Windows

A.1.1. Introduction

   There are a few reasons which might make it necessary to put
   Micorosoft DOS/Windows and Linux together on one laptop. Often the
   support for the flash ROM of PCMCIA cards and modems is not available
   for Linux, or you have to retrieve hardware information, which is not
   visible with Linux, due to a lack of support by some hardware
   manufacturers. I'm not sure whether these tasks can be performed
   under an emulation like DOS-EMU, WINE or VMware.

   If you want Linux with X11, Netscape, etc., and
   Microsoft-Windows9x,NT,2000,XP things will be tight in a 1GB
   harddisk. Though I did so with a 810MB disk.
     ________________________________________________________________

A.1.2. DOS Tools to Repartition a Hard Disk

   Often you get a preinstalled version of Microsoft-Windows on your
   laptop. If you just want to shrink the Windows partition, you need a
   tool to resize the partition. Or you can remove the partition first,
   repartition, then reinstall. Most of the following information I
   found at the page of [http://libweb.sonoma.edu/mike/fujitsu/] Michael
   Egan <Michael.Egan_AT_sonoma.edu>.

   A well known and reliable commercial product is
   [http://www.powerquest.com/] Partition Magic from Power Quest.

   [http://www.bootitng.com] BootitNG is a shareware programm, which is
   capable of resizing NTFS, EXT2, EXT3 and ReiserFS partitions.

   System Commander 2000 by Symantec? resizes FAT32 partitions, unlike
   Partition Magic, SC2000 seems to be able to work without the presence
   of an installed Microsoft operating system (tough you may use
   Partition Magic from two standalone floppy disks).

   One more "newer" utility for repartitioning and resizing FAT
   partitions is Ranish Partition Manager/Utility (FAT-32 support is
   claimed for this as well, Linux support is taken into account.)
   [http://www.ranish.com/part/] Ranish Partition Manager/Utility .

   Many people have used FIPS 15c (which may support FAT-32)
   [http://bmrc.berkeley.edu/people/chaffee/fips/fips.html] FIPS for
   repartitioning FAT partition sizes.) Also, another version from a
   different source is FIPS 2.0 (claims to support FAT-32)
   [http://www.igd.fhg.de/~aschaefe/fips/] FIPS 2.0 for repartitioning
   FAT partition sizes.)
     ________________________________________________________________

A.1.3. Partition Sharing

   You may share your swap space between Linux and Windows. Please see
   "Dealing with Limited Resources" section.

   With Linux you can mount any kind of DOS/Windows partition of the
   type msdos, vfat and even compressed drives (Drivespace, etc.). For
   long file names use vfat and if you like autoconversion ( a nice
   feature for text files), you may do so by using the conv=auto option.
   I have used this in my /etc/fstab, but be aware this might cause some
   strange behaviour sometimes, look at the kernel docs for further
   details.

/dev/hda8    /dos/d    vfat    user,exec,nosuid,nodev,conv=auto    0    2

   The other way round there are also
   [http://www.chrysocome.net/projects] some tools, which provide a
   means to read and write ext2 partitions from Windows9x/NT.

   [http://www.it.fht-esslingen.de/~zimmerma/software/ltools.htm] LREAD
   is a tool suite for Windows 9x and Windows NT (or DOS or Windows 3.x
   for those who still have it) for accessing files on Linux harddisks
   (Linux's native Extended 2 filesystem).

   The tools allow to list directories, to copy files from Linux to DOS
   and to copy files from DOS to Linux. You also can delete files or
   modify access rights of Linux files from DOS/Windows.

   In combination with an included simple server program, you can also
   access your files from a remote client over the net (however, this
   might be a security risk, as access protection in this case is rather
   simple).
     ________________________________________________________________

A.1.3.1. LINE Is Not an Emulator

   [http://line.sourceforge.net] LINE executes unmodified Linux
   applications on Windows by intercepting Linux system calls. The Linux
   applications themselves are not emulated. They run directly on the
   CPU just like all other Windows applications.
     ________________________________________________________________

A.1.4. Installation without CD Drive

   You may use the CD drive of a desktop (or copy the content of the CD
   to the hard disk) and connect both machines with a null modem cable.
   Then use a DOS boot floppy and the program INTERLNK.EXE to connect
   both machines.
     ________________________________________________________________

A.1.5. Miscellaneous

   [http://www.travsoft.com/] TravSoft

   Windows/NT offers: RAS - Remote Access Service

   Windows/9x/NT offers the PPTP protocol to connect to remote sites via
   a TCP/IP tunnel. This protocol is also supported by Linux.
   [http://www.moretonbay.com/vpn/pptp.html] PoPToP is the PPTP server
   solution for Linux allowing Linux servers to function seamlessly in
   the PPTP VPN environment. This enables administrators to leverage the
   considerable benefits of both Microsoft clients and Linux servers.
   The current pre-release version supports Windows 95/98/NT PPTP
   clients and PPTP Linux clients. The PoPToP pre-release server is not
   yet fully optimised. On release, PoPToP will be fully compliant with
   IETF PPTP Internet Draft and it will seamlessly support Windows PPTP
   clients with the full range of encryption and authentication
   features.
     ________________________________________________________________

A.2. BSD UNIX

   FreeBSD is a version of the UNIX operating system that runs on PC
   hardware. It uses a different set of support for PCMCIA devices, APM,
   and other mobility related issues.

    1. [http://www.freebsd.org/~picobsd/] PicoBSD is a one floppy
       version of FreeBSD 3.0-current, which in its different variations
       allows you to have secure dialup access, small diskless router or
       even a dial-in server. And all this on only one standard 1.44MB
       floppy. It runs on a minimum 386SX CPU with 8MB of RAM (no HDD
       required!). You probably may also use it to install BSD on a
       laptop as described with micro Linuxes above.
    2. [http://www.jp.FreeBSD.org/PAO/] PAO: FreeBSD Mobile Computing
       Package
    3. [http://www.monarch.cs.cmu.edu/] The CMU Monarch Project offers
       implementations of Mobile-IPv4 and Mobile-IPv6 for FreeBSD.
    4. [http://www.yy.cs.keio.ac.jp/~sanpei/note-list.html] XF86Config
       Archive . A database of XF86Config files used by Linux and
       FreeBSD users. If you need an XF86Config file for your notebook
       or laptop, check out this site. (Some documents available in
       Japanese only.)
    5. AFAIK there is no IrDA� support yet.
    6. [http://lists.openresources.com/FreeBSD/freebsd-mobile/] Archive
       of the FreeBSD-Mobile mailing list . Sorry don't know how to
       subscribe yet.
    7. [http://www.jp.freebsd.org/PAO/LAPTOP_SURVEY/] Laptop Survey /
       FreeBSD - LTS is a project to collect information of laptop and
       NOTE-PC environments running FreeBSD. It provides information in
       English and Japanese. Please support this project.
     ________________________________________________________________

A.3. OS/2

   At [http://www.os2ss.com/users/DrMartinus/notebook.htm] The
   Notebook/2 Site by Dr. Martinus you may find information about
   different notebooks and PCMCIA cards working with OS/2.
     ________________________________________________________________

A.4. NOVELL Netware

   The client side with DOS/Windows9x style operating systems seems to
   be no problem, since there are many PCMCIA cards with drivers for
   Netware available. For Linux connections see the mars_nwe package.
   Also the Caldera Linux distribution is well known for its Novell
   support.

   I hadn't time to build a Netware server on a laptop yet and couldn't
   check whether there are network connections possible (PCMCIA driver
   for Netware server).
     ________________________________________________________________

A.5. Debian GNU/Hurd (hurd-i386)

   The GNU Hurd is a totally new operating system being put together by
   the GNU group. In fact, the GNU Hurd is the final component which
   makes it possible to built an entirely GNU OS -- and Debian GNU/Hurd
   is going to be one such (possibly even the first) GNU OS. The current
   project is founded on the i386 architecture, but expect the others to
   follow soon.

   The
   [http://www.urbanophile.com/arenn/hacking/hurd/hurd-hardware.html]
   GNU Hurd Hardware Compatibility Guide states that Hurd should work on
   laptops, but PCMCIA support isn't ready yet.
     ________________________________________________________________

Appendix B. Other Resources

B.1. Main WWW Resources

   Kenneth E. Harker maintains a quite valuable database at
   [http://www.linux-on-laptops.com/] Linux on Laptops . Please have a
   look at his site to get current information about laptop related
   mailing lists, newsgroups, magazines and newsletters, WWW sites and a
   big and up-to-date database about many different laptop pages.

   The author of this guide maintains the TuxMobil Linux Laptop and
   Notebook Installation Survey and a Linux compatibility database about
   different laptop, notebook and PDA hardware, such as
   [http://tuxmobil.org/pcmcia_linux.html] PCMCIA/CardBus/CF-Cards,
   [http://tuxmobil.org/graphic_linux.html] graphics cards,
   [http://tuxmobil.org/sound_linux.html] sound chips,
   [http://tuxmobil.org/ir_misc.html] IrDA devices, and more.
     ________________________________________________________________

B.2. Mailing Lists

   A survey of laptop mailing lists. Some of the addresses are taken
   from Kenneths page. All comments are by me:
     ________________________________________________________________

B.2.1. General Lists

   To join the Linux-Laptop-Mailing-List at TuxMobil visit the
   subscription page. There you may find the list archive, too. This is
   a new list, but offers a reasonable amount of members already.

   To join the Linux-Laptop-Mailing-List from Kernel.Org write a mail to
   <majordomo_at_vger.kernel.org> with subscribe linux-laptop in the
   subject. You will get a confirmation message than, which you have to
   reply appropriately. Note: This is the list formerly admininstrated
   by <majordomo_at_vger.rutgers.edu>. This was a list with much
   traffic, current traffic seems to be very low. The list seems to have
   lost most of its members since changing the address.

   A searchable mailing list archive (of the predecessor) is hosted in
   the miscellaneous section of [http://www.geocrawler.com] GeoCrawler.

   The [http://www.egroups.com/group/linuxonlaptop] eGroups Discussion
   Forum (linuxonlaptop) is dedicated to Linux on laptop issues. It has
   almost no traffic and is archived.

   Also the [http://www.egroups.com/group/linuxlaptop] eGroups
   Discussion Forum (linuxlaptop) is dedicated to Linux on laptop
   issues. It has almost no traffic and is archived.

   The
   [http://www.eecs.umich.edu/~steveh/linux-notebook/discussion.html]
   Linux Notebook HQ Discussion Forum is dedicated to Linux on laptop
   issues. It has almost no traffic and is archived.
     ________________________________________________________________

B.2.2. Lists Dedicated to a Linux Distribution

   There is now a debian-laptop mailing list. Any questions or
   discussions concerning running the Debian/GNU Linux operating
   system(s) on laptops are welcome. Send mail to
   <debian-laptop-request_at_lists.debian.org> with a subject of
   subscribe. Or visit the
   [http://www.debian.org/MailingLists/subscribe] Debian/GNU Linux site
   and use the online form. The list is archived and has a reasonable
   amount of traffic and a good quality.

   SuSE offers a mailing list for discussion about mobility in the
   openSUSE distribution <opensuse-mobile_AT_opensuse.org>. You may
   subscribe at the [http://en.opensuse.org/Communicate] SuSE mailing
   list portal. Before asking questions there have a look into the
   [http://en.opensuse.org/HCL/Laptops] OpenSuse Hardware Compatibility
   List - HCL: Laptops, the [http://lists.opensuse.org/opensuse-mobile/]
   opensuse-mobile mailing list archive and the
   [http://en.opensuse.org/Documentation] OpenSuSE documentation portal.
     ________________________________________________________________

B.2.3. Lists Dedicated to a Laptop or Manufacturer

   The [http://www.egroups.com/group/linux-dell-laptops]
   linux-dell-laptops is dedicated to Linux on DELL laptop issues. It
   has almost no traffic and is archived.

   The linux-thinkpad list is dedicated to Linux on IBM ThinkPads
   issues. It

   The linux-thinkpad list is dedicated to Linux on IBM ThinkPads
   issues. It has almost no traffic. Write a mail to
   <majordomo_at_bm-soft.com>.

   Also the [http://www.topica.com/lists/linux-thinkpad/] linux-thinkpad
   is dedicated to Linux on IBM ThinkPads issues. It has almost no
   traffic and is archived.

   The [http://www.onelist.com/subscribe.cgi/linux-on-portege]
   linux-toshiba-portege is dedicated to Linux on Toshiba Porteges
   issues. It has almost no traffic and is archived.

   The linux-tosh-40xx list is dedicated to Linux on Toshiba Satellite
   40xx issues. It has almost no traffic. Write a mail to
   <majordomo_at_geekstuff.co.uk>.
     ________________________________________________________________

B.3. USENET Newsgroups

   The USENET newsgroups can provide a source of information about
   aspects of running Linux on notebooks that haven't yet been
   documented. If you are unable to find the information you are looking
   for here or on any of the pages linked to from this site, a post to
   the USENET newsgroups may turn up an answer from someone that can
   help you.
     ________________________________________________________________

B.3.1. Linux Newsgroups

     * [news:comp.os.linux.portable] comp.os.linux.portable As far as I
       know there is no archive of this group yet.
     * [news:comp.os.linux.announce] comp.os.linux.announce
     * comp.sys.mac.portables
     * [news:comp.os.linux.answers] comp.os.linux.answers
     * [news:comp.os.linux.development.apps]
       comp.os.linux.development.apps
     * [news:comp.os.linux.development.system]
       comp.os.linux.development.system
     * [news:comp.os.linux.hardware] comp.os.linux.hardware
     * [news:comp.os.linux.misc] comp.os.linux.misc
     * [news:comp.os.linux.networking] comp.os.linux.networking
     * [news:comp.os.linux.setup] comp.os.linux.setup
     * [news:comp.os.linux.x] comp.os.linux.x
     ________________________________________________________________

B.3.2. PDA Newsgroups and IRC Channels

     * comp.sys.handhelds
     * comp.sys.newton.misc
     * comp.sys.palmtops
     * comp.sys.pen
     * #zaurus@irc.freenode.net
     * irc.freenode.net #opie #opie.de
     ________________________________________________________________

B.3.3. X Window System Newsgroups

     * [news:comp.windows.x] comp.windows.x
     * [news:comp.windows.x.announce] comp.windows.x.announce
     * [news:comp.windows.x.apps] comp.windows.x.apps
     * [news:comp.windows.x.i386unix] comp.windows.x.i386unix
     ________________________________________________________________

B.3.4. Hardware Newsgroups

     * [news:comp.sys.laptops] comp.sys.laptops
     * [news:alt.periphs.pcmcia] alt.periphs.pcmcia
     * [news:comp.sys.ibm.pc.hardware.chips]
       comp.sys.ibm.pc.hardware.chips
     * [news:comp.sys.ibm.pc.misc] comp.sys.ibm.pc.misc
     ________________________________________________________________

B.4. Newsletters, RSS Channels

     * The [http://tuxmobil.org/newsfeed.html] TuxMobil News (RDF/RSS)
       is also available as a [http:tuxmobil.org/mobile_news.html]
       monthly digest via e-mail.
     ________________________________________________________________

B.5. Magazines, Blogs Newsletters

   Magazines, blogs and newsletters about mobile computing in general.

     * [http://laptopical.com/] Laptopical: Laptops Weblog
     ________________________________________________________________

B.6. General Laptop Information

   These are sources of information of general use to laptop and
   notebook owners, regardless of the operating system used.

   [http://www.fcc.gov/oet/fccid/] Federal Communications Commission
   On-line Equipment Authorization Database If you are having problems
   identifying the manufacturer of a laptop or notebook computer (or
   other electronic device,) this site lets you search the FCC database
   based on the FCC ID number you can usually find on the equipment if
   it was marketed in the United States of America.
     ________________________________________________________________

Appendix C. Repairing the Hardware

   There are several different reasons that could make it necessary to
   open the case of a laptop, notebook or PDA.

    1. repair broken hardware
    2. get some hardware info, which isn't available otherwise, e.g.
       reading the sticker on an undetected chipset
    3. remove the speakers (speakerektomy, as described in
       [http://tldp.org/HOWTO/Visual-Bell.html] Visual-Bell-HOWTO )
    4. install overdrive for CPU
    5. reflash the BIOS
    6. change BIOS battery
    7. upgrade harddisk
    8. upgrade memory
    9. implement additional hardware, e.g. an internal wireless LAN
       miniPCI card

   Repairing a laptop can be quite expensive if you don't have a
   manufacturer's warranty. Sometimes professional support is bad. But
   opening a laptop case can be difficult. Often the procedures to
   upgrade the memory and the harddisk are described in the manual. For
   further details, you should try to get the maintenance/technical
   manual. Just be extremely careful and make notes as to where each
   screw goes. You must get most of them back in the right hole or you
   could ruin the machine by damaging the system board. Also after you
   get all the screws to an assembly out (some will be hidden) the parts
   are usually held together with plastic clips molded in, so you still
   must exercise care to separate them. Sometimes you need certain
   tools, for instance TORX screw drivers or a solder kit. Good luck.

   Warning

   Usually laptop and PDA manufacturers declare the warranty to be void
   if the case was opened by people other than their own staff. If you
   want to try it anyway you may find some interesting links about how
