```

Linux on the Road

Linux with Laptops, Notebooks, PDAs, Mobile Phones and Other Portable
Devices

Werner Heuser

      <wehe[AT]tuxmobil.org>

   Linux Mobile Edition  Edition
   Version 3.22

   TuxMobil

   Berlin

   Copyright � 2000-2011 Werner Heuser

   2011-12-12
   Revision History
   Revision 3.22   2011-12-12 Revised by: wh
   The address of the opensuse-mobile mailing list has been added, a
   section power management for graphics cards has been added, a short
   description of Intel's LinuxPowerTop project has been added, all
   references to Suspend2 have been changed to TuxOnIce, links to
   OpenSync and Funambol synchronization packages have been added, some
   notes about SSDs have been added, many URLs have been checked and
   some minor improvements have been made.
   Revision 3.21   2005-11-14 Revised by: wh
   Some more typos have been fixed.
   Revision 3.20   2005-11-14 Revised by: wh
   Some typos have been fixed.
   Revision 3.19   2005-11-14 Revised by: wh
   A link to keytouch has been added, minor changes have been made.
   Revision 3.18   2005-10-10 Revised by: wh
   Some URLs have been updated, spelling has been corrected, minor
   changes have been made.
   Revision 3.17.1 2005-09-28 Revised by: sh
   A technical and a language review have been performed by Sebastian
   Henschel. Numerous bugs have been fixed and many URLs have been
   updated.
   Revision 3.17   2005-08-28 Revised by: wh
   Some more tools added to external monitor/projector section, link to
   Zaurus Development with Damn Small Linux added to cross-compile
   section, some additions about acoustic management for hard disks
   added, references to X.org added to X11 sections, link to
   laptop-mode-tools added, some URLs updated, spelling cleaned, minor
   changes.
   Revision 3.16   2005-07-15 Revised by: wh
   Added some information about pcmciautils, link to SoftwareSuspend2
   added, localepurge for small HDDs, added chapter about FingerPrint
   Readers, added chapter about ExpressCards, link to Smart Battery
   System utils added to Batteries chapter, some additions to External
   Monitors chapter, links and descriptions added for: IBAM - the
   Intelligent Battery Monitor, lcdtest, DDCcontrol updated Credits
   section, minor changes.

   Mobile computer devices (laptops, notebooks, PDAs, mobile cell
   phones, portable audio and video players, digital cameras,
   calculators, wearables, ...) are different from desktop/tower
   computers. They use certain hardware such as PCMCIA cards, infrared
   and BlueTooth ports, wireless LAN, LCD displays, batteries, docking
   stations. Hardware parts cannot be changed as easily as in a
   desktops, e.g. the graphics card. Often their hardware is more
   limited (e.g. disk space, CPU speed). Though the performance gap to
   desktops is becoming smaller, e.g. in many instances, laptops or
   notebooks can become a desktop replacement.

   Hardware support for Linux (and other operating systems) and mobile
   computer devices is sometimes more limited (e.g. graphics chips,
   internal modems). They often use specialized hardware, hence finding
   a driver can be more difficult. Many times they are used in changing
   environments, so there is a need for multiple configurations and
   additional security strategies.

   Though there are laptop, notebook, PDA and mobile phone related
   HOWTOs available already, this guide contains a concise survey of
   documents related to mobile computer devices. Also Linux features,
   such as installation methods for laptops, notebooks and PDAs as well
   as configurations for different (network) environments are described.

   Although there are some caveats, Linux is a better choice for mobile
   computer devices than most other operating systems, because it
   supports numerous installation methods, works in many heterogeneous
   environments and needs smaller resources.

   Copyright (c) 2000-2011 Werner Heuser. For all chapters except
   "Lectures, Presentations, Animations and Slideshows" permission is
   granted to copy, distribute and/or modify this document under the
   terms of the GNU Free Documentation License, Version 1.1 or any later
   version published by the Free Software Foundation; with the Invariant
   Sections being "Preface" and "Credits", with the Front-Cover Texts
   being "Linux on the Road - the First Book on Mobile Linux", and with
   the Back-Cover Texts being the section "About the Author". A copy of
   the license is included in the section entitled "GNU Free
   Documentation License".
     ________________________________________________________________

   Table of Contents
   Preface

        1. About the Author
        2. Sponsoring
        3. About the Document
        4. Contact
        5. Disclaimer and Trademarks

   I. Laptops and Notebooks

        1. Which Laptop to Buy?
        2. Laptop Distributions
        3. Installation

   II. Handheld Devices - Personal Digital Assistants (PDAs)

        4. Palmtops, Personal Digital Assistants - PDAs, Handheld PCs -
                HPCs

        5. History of Linux on PDAs
        6. Linux PDAs
        7. Non-Linux PDAs - Ports and Tools
        8. Connectivity

   III. Tablet PCs / Pen PCs

        9. Tablet PCs / Pen PCs

   IV. Mobile (Cellular) Phones, Pagers, Calculators, Digital Cameras,
          Wearable Computing

        10. Mobile (Cellular) Phones, Pagers
        11. Calculators, Digital Cameras, Wearable Computing

   V. Mobile Hardware in Detail

        12. Hardware in Detail: CPU, Display, Keyboard, Sound and More
        13. Accessories: PCMCIA, USB and Other External Extensions

   VI. Kernel

        14. Kernel History

   VII. On the Road

        15. Different Environments
        16. Solutions with Mobile Computers

   VIII. Appendix

        A. Other Operating Systems
        B. Other Resources
        C. Repairing the Hardware
        D. Survey about Micro Linuxes
        E. Dealing with Limited Resources or Tuning the System
        F. Ecology and Laptops
        G. NeoMagic Graphics Chipset Series NM20xx
        H. Annotated Bibliography: Books For Linux Nomads
        I. Resources for Specific Laptop Brands
        J. Credits
        K. Copyrights

   List of Tables
   12-1. Arguments for the -t and -R option of gpm.

   List of Figures
   6-1. Screenshot of the YOPY PDA
   6-2. Screenshot of the SHARP Zaurus SL-5500 PDA.
   7-1. Screenshot of the HELIO PDA.
   7-2. Screenshot of the iPAQ PDA.
   7-3. Screenshot of the PALM-Pilot emulator POSE.
   12-1. Screenshot of cardinfo
   E-1. Screenshot of blackbox.
     ________________________________________________________________

Preface



   Life is the first gift, love is the second, and understanding is the
   third.
     [http://www.margepiercy.com/] Merge Piercy
     ________________________________________________________________

1. About the Author

   People like either laptops or desktops. I like to work with laptops
   rather than with desktops. I like Linux too. My first HOWTO was the
   [http://tuxmobil.org/howtos.html] Linux-Infrared-HOWTO about infrared
   support for Linux. My second is this one and my third the
   [http://computerecology.org/] Linux-Ecology-HOWTO , about some ways
   to use Linux in an ecology aware manner.

   Also I have written some pages about Linux with all the laptops I had
   a chance to put Linux on. You may find them at
   [http://tuxmobil.org/mylaptops.html] TuxMobil Linux Laptop and
   Notebook Survey.

   During the work with the Linux-Mobile-Guide I have also collected
   some surveys about laptop related hardware:
   [http://tuxmobil.org/graphic_linux.html] graphics chips ,
   unofficially supported PCMCIA cards ,
   [http://tuxmobil.org/modem_linux.html] internal modems ,
   [http://tuxmobil.org/ir_misc.html] infrared chips and other hardware.

   In May 2000 I have founded the German vendor [http://xtops.de/]
   Xtops.DE: Linux, Laptops, Notebooks, PDAs pre-installed, to sponsor
   the TuxMobil project.
     ________________________________________________________________

2. Sponsoring

2.1. How to and Why Sponsor?

   This guide is free of charge (except the printed version, which
   contains an additional part) and free in the sense of the General
   Public Licence - GPL. Though it requires much work and could gain
   more quality if I would have some more hardware. So if you have a
   spare laptop, even an old one or one which requires repair, please
   let me know. For the curious, the first issues of this guide have
   been written on a [http://tuxmobil.org/hp800e.html] HP OmniBook 800CT
   5/100.

   Or sponsor a banner ad at [http://tuxmobil.org/] TuxMobil: Linux with
   Laptops, Notebooks, PDAs, Mobile Phones and Portable Computers.

   You can hire me for readings or workshops on Linux with Laptops,
   Linux with PDAs, Repairing of Laptops and other Linux topics, too.
     ________________________________________________________________

2.2. Table of Sponsors

   This guide is currently sponsored by:

     * AgendaComputing (Berlin, Germany out-of-business)
     * [http://xtops.de/index.html] Xtops.DE - Pre-Installed Linux on
       Laptops, PDAs and Mobile Phones
     ________________________________________________________________

3. About the Document

   Mirrors, Translations, Versions, Formats, URLs
     ________________________________________________________________

3.1. URLs in this Document

   Many times I have mentioned MetaLab formerly known as SunSite. This
   site carries a heavy load, so do yourself a favor, use one of the
   [http://metalab.unc.edu/pub/Linux/MIRRORS.html] MetaLab mirrors .

   For Debian/GNU Linux the mirror URLs are organized in the scheme
   http://www.<country code, e.g. uk>.debian.org .

   Nearly all of the programs I mention are available as
   [http://www.debian.org/] Debian/GNU Linux package, or as RPM package.
   Look up your favorite RPM server, for instance [http://rpmfind.net/]
   rpmfind .
     ________________________________________________________________

3.2. Latest Version, Mirrors

   Former issues of this text are available at the [http://tldp.org/]
   THE LINUX DOCUMENTATION PROJECT - TLDP.

   The latest version of this document is available at
   [http://tuxmobil.org/howtos.html] TuxMobil - HOWTOs.
     ________________________________________________________________

3.3. Proposed Translations

   The following translations are under construction:

     * Chinese, John Lian <johnlian_AT_riverrich.com.tw>
     * Greek, Vassilis Rizopoulos <mscyvr_AT_scs.leeds.ac.uk>
     * Italian, Alessandro Grillo <Alessandro_Grillo_AT_tivoli.com>,
     * Japanese, Ryoichi Sato <rsato_AT_ipf.de>,
     * Portuguese, Gledson Evers <pulga_linux_AT_bol.com.br>
     * Slovenia, Ales Kosir <ales.kosir_AT_hermes.si>
     * Spanish, Jaime Robles <ea4abw_AT_amsat.org>

   Please contact me before starting a translation to avoid double work.
   Since a translation is a great amount of work, I recommend to do this
   work as a group, for instance together with your
   [http://lugww.counter.li.org/] local Linux Users Group - LUG.
     ________________________________________________________________

4. Contact

   This document isn't ready yet. If you like to write a chapter or even
   a smaller part by yourself, please feel free to contact me. Also your
   suggestions and recommendations and criticism are welcome. But please
   don't expect me to solve your laptop related problems if the solution
   is already documented. Please read all appropriate manual pages,
   HOWTOs and WWW sites first, than you may consider to contact me or
   search in the chapter Appendix B Other Resources mentioned below.

   Werner Heuser <wehe_at_tuxmobil.org>
     ________________________________________________________________

5. Disclaimer and Trademarks

   This is free documentation. It is distributed in the hope that it
   will be useful, but without any warranty. The information in this
   document is correct to the best of my knowledge, but there's a always
   a chance I've made some mistakes, so don't follow everything too
   blindly, especially if it seems wrong. Nothing here should have a
   detrimental effect on your computer, but just in case, I take no
   responsibility for any damages incurred from the use of the
   information contained herein.

   Some laptop manufacturers don't like to see a broken laptop with an
   operating system other than the one shipped with it, and may reload
   MS-Windows if you complain of a hardware problem. They may even
   declare the warranty void. Though in my humble opinion this isn't
   legal or at least not fair. Always have a backup of both the original
   configuration and your Linux installation if you have to get your
   laptop repaired.

   Though I hope trademarks will be superfluous sometimes (you may see
   what I mean at [http://www.opensource.org/osd.html] Open Source
   Definition ), I declare: If certain words are trademarks, the context
   should make it clear to whom they belong. For example "MS Windows NT"
   implies that "Windows NT" belongs to Microsoft (MS). "Mac" is a
   trademark by Apple Computer. Many of the designations used by
   manufacturers and sellers to distinguish their products are claimed
   as trademarks. Where those designations appear in this book, and I
   was aware of a trademark claim, the designations have been printed in
   caps or initial caps. All trademarks belong to their respective
   owners.

I. Laptops and Notebooks

   Table of Contents
   1. Which Laptop to Buy?

        1.1. Introduction
        1.2. Portables, Laptops/Notebooks, Sub/Mini-Notebooks, Palmtops,
                PDAs/HPCs

        1.3. Linux Features
        1.4. Main Hardware Features
        1.5. Sources of More Information
        1.6. Linux Compatibility Check
        1.7. Writing a Device Driver
        1.8. Buying a Second Hand Laptop
        1.9. No Hardware Recommendations
        1.10. Linux Laptop and PDA Vendor Survey

   2. Laptop Distributions

        2.1. Requirements
        2.2. Recommendation

   3. Installation

        3.1. Related Documentation
        3.2. Prerequisites - BIOS, Boot Options, Partitioning
        3.3. Linux Tools to Repartition a Hard Disk
        3.4. Laptop Installation Methods
        3.5. Common Problems During Installation
     ________________________________________________________________

Chapter 1. Which Laptop to Buy?

1.1. Introduction

   Portable computers may be divided into different categories. This is
   a subjective decision, but I try to do so. My groupings roughly
   follow the generally accepted marketing categories. The criteria
   could be:

    1. Weight: Often expressed in terms like Portables,
       Laptops/Notebooks, Sub/Mini-Notebooks, Palmtops/PDAs. There is no
       standard method to define the weight of a laptop, therefore the
       data provided by the manufacturers (and which are given below)
       have to be considered as approximations. The question is how the
       power supply (whether external or internal) or swappable parts
       like CD and floppy drive, are included in the weight.
       Most peripheral cables are appallingly heavy. If you get a
       subnotebook and carry it around with a bunch of external drives,
       cables, and port expander dongles and power converter, you may be
       lugging a heavier bag than if it were all in one box.
       Subnotebooks are useful mainly if you can afford to leave all the
       other junk behind.
    2. Supported Operating Systems: proprietary versus open
    3. Price: NoName versus Brand
    4. Hardware Features: display size, harddisk size, CPU speed,
       battery type, etc.
    5. Linux Support: graphics chip, sound card, infrared controller
       (IrDA�), internal modem, etc.
     ________________________________________________________________

1.2. Portables, Laptops/Notebooks, Sub/Mini-Notebooks, Palmtops, PDAs/HPCs

1.2.1. Portables

   Weight greater than 4.0 kg (9 lbs). Features like a PC, but in a
   smaller box and with LCD display. Examples: lunchbox or ruggedized
   laptops (e.g. [http://www.bsicomputer.com/] BSI Computer ).
     ________________________________________________________________

1.2.2. Laptops/Notebooks

   Weight between 1.7 and 4.0 kg (4 to 9 lbs). Features custom hardware
   and usually a special CPU. Examples: HP OmniBook 3100, COMPAQ Armada
   1592DT. The terms laptop and notebook seem equivalent to me.
     ________________________________________________________________

1.2.3. Sub-Notebooks/Mini-Notebooks

   Weight between 1.3 and 1.7 kg (3 to 4 lbs). Features: external floppy
   drive, external CD drive. Examples: HP OmniBook 800CT, Toshiba
   Libretto 100, COMPAQ Aero, SONY VAIO 505.
     ________________________________________________________________

1.2.4. Palmtops

   Weight between 0.7 and 1.3 kg (1.5 to 3 lbs). Features: proprietary
   commercial operating systems. Examples: HP200LX.
     ________________________________________________________________

1.2.5. Personal Digital Assistants (PDAs)/Handheld PCs (HPCs)

   Weight below 0.7 kg (1.5 lbs). Features: proprietary commercial
   operating systems and often non-Intel CPU with commercial operating
   systems like PalmOS, EPOC32, GEOS, Windows CE. Examples: Newton
   Message Pad, Palm III (former Pilot), Psion Series 3 and 5, CASIO
   Z-7000.
     ________________________________________________________________

1.2.6. Wearables

   Watches, digital pens, calculators, digital cameras, cellular phones
   and other wearables.
     ________________________________________________________________

1.3. Linux Features

   Due to a lack of support by some manufacturers, not every feature of
   a laptop is always supported or fully operational. The main devices
   which may cause trouble are: graphics chip, IrDA� port, sound card,
   PCMCIA controller , PnP devices and internal modem. Please try to get
   as much information about these topics before buying a laptop. But
   often it isn't quite easy to get the necessary information. Sometimes
   even the specifications or the hotline of the manufacturer aren't
   able to provide the information. Therefore I have included a Linux
   Compatibility Check chapter in every section of Part V in Linux on
   the Road Hardware In Detail below.

   Depending on your needs, you might investigate one of the vendors
   that provide laptops pre-loaded with Linux. By purchasing a
   pre-loaded Linux laptop, much of the guesswork and time spent
   downloading additional packages could be avoided. See TuxMobil for a
   survey of Linux laptop, notebook, PDA and mobile phone vendors.
     ________________________________________________________________

1.4. Main Hardware Features

   Besides its Linux features, there often are some main features which
   have to be considered when buying a laptop. For Linux features please
   see Part V in Linux on the Road Hardware In Detail below.
     ________________________________________________________________

1.4.1. Weight

   Don't underestimate the weight of a laptop. This weight is mainly
   influenced by:

    1. screen size
    2. battery type
    3. internal components, such as CD drive, floppy drive
    4. power supply
    5. material used for the case, usually they are either from plastics
       or from magnesium.
     ________________________________________________________________

1.4.2. Display

   Recent laptops come with active matrix (TFT) displays. Laptops with
   passive matrix (DSTN) are no longer manufactured. Active matrix
   displays have better color and contrast, but usually cost more and
   use more power. Also consider the screen size. Laptops may be
   purchased with screens up to 17". A bigger screen weighs more, costs
   more, and is harder to carry, but is good for a portable desktop
   replacement.
     ________________________________________________________________

1.4.3. Batteries

   The available battery types are Lithium Ion (LiIon), Nickel Metal
   Hydride ( NiMH) and Nickel Cadmium (NiCd). Though almost all current
   laptops come with LiIon batteries.

   LiIon batteries are the most expensive ones but a lot lighter than
   NiCd for the same energy content, and have minimal - but present -
   memory effects. NiMH is better than NiCd, but still rather heavy and
   does suffer some (although less than NiCd) memory effects.

   Unfortunately most laptops come with a proprietary battery size. So
   they are not interchangeable between different models.
     ________________________________________________________________

1.4.4. CPU

1.4.4.1. Supported CPU Families

   For details about systems which are supported by the Linux Kernel,
   see the [http://www.tux.org/lkml/] The linux-kernel mailing list FAQ.

    1. i286: Linux doesn't support this CPU family yet. But there are
       some efforts at [http://elks.sourceforge.net/] ELKS. If you like,
       you may use [http://www.cs.vu.nl/~ast/minix.html] Minix, which is
       also a free Unix operating system. Minix supports 8088 to 286
       CPUs with as little as 640K memory. Actually there are some
       [http://tuxmobil.org/286_mobile.html] laptops with ELKS and MINIX
       around.
    2. i386: This covers PCs based on Intel-compatible processors,
       including Intel's 386, 486, Pentium, Pentium Pro and Pentium II,
       and compatible processors by AMD, Cyrix and others. Most of the
       currently available laptops use Intel compatible CPUs and have
       quite good Linux support.
    3. m68k: This covers Amigas and Ataris having a Motorola 680x0
       processor for x>=2; with MMU. And the early Apple/Macintosh
       computers.
       There was a long series of Apple PowerBooks and other laptops
       based on the m68k chip. Macintosh Portable (an ugly 16-pound
       first attempt); PowerBook 100, 140, 170, 145, 160, 180c, 165c,
       520c, 540c, 550c, 190; Duo 210, 230, 250, 270c, 280. The
       PowerBook Duos were available at the same time as the PowerBooks,
       they were a sort of subnotebook, but were designed so that you
       could plug them into a base station (a DuoDock) with more RAM,
       peripherals, etcetera, so that they could also act as a desktop
       computer. The first PowerPC PowerBooks were the ill-starred
       PowerBook 5300 (after the 190) and the Duo 2300c.
       For a complete list of all Macintosh computers ever made, with
       specifications, see [http://www.apple-history.com/] Apple-History
       . For Linux installation reports see
       [http://tuxmobil.org/apple.html] Linux Laptop and Notebook
       Survey: Apple.
       The proper place to go for information on running Linux on m68k
       Macintoshes is [http://www.mac.linux-m68k.org/] linux-m68k.
       "Much like laptops of the Intel/Linux world, Mac laptops have
       generally different setups that can be very hard to figure out.
       Also, because of a general lack of machines to test, we are only
       aware of boots on the Powerbook 145, Powerbook 150, Powerbook
       170, Powerbook 180, and Powerbook 190. Even if it boots, we
       currently have no support for Powerbook-style ADB, the APM
       support, or just about anything else on them. This means the only
       way to log in is with a terminal hooked up to the serial
       interface, this has been tested on the 170."
       "Several Powerbooks have internal IDE which is supported. PCMCIA
       drivers will be forthcoming if someone can supply the necessary
       hardware information to write a driver. As always, an FPU is
       needed also. Many of the later models have the 68LC040 processor
       without FPU, and many of these processors are broken with respect
       to the FPU trap mechanism so they can't run regular Linux
       binaries even with FPU emulation. Current status on Powerbooks
       140, 160, 165, 165c, 180c, 190, 520 and Duos 210, 230, 250, 270c,
       280, and 280c is unknown."
       Also there are two Atari laptops, for which I don't have enough
       information. The following quotations are from the
       [http://capybara.sk-pttsc.lj.edus.si/yescrew/eng/atari.htm] Atari
       Gallery.
       "The STacy was released shortly after the Mega ST to provide a
       portable means of Atari computing. STacy computers were shipped
       with TOS v1.04.
       Designed to replace the STacy as the defacto portable ST
       computer, the ST Book brought the basic computing power of an ST
       to a lightweight notebook computer. This machine was only
       released in Europe and Atari only shipped a very small quantity.
       The ST Book was shipped with TOS v2.06."
       From Stok, Leon <stok_AT_YIS.NL>: The STacey and the ST Book,
       both can't run Linux since they are only shipped with an 68000
       CPU, which doesnt have a MMU unit.
       As far as I know Amiga has never produced laptops. One company
       manufactured kits to convert desktop Amigas to portables. These
       used regular Amiga motherboards so any Linux setup that supports
       the regular Amiga setups will support these.
    4. Alpha, Sparc, Sparc64 architectures: These are currently under
       construction. As far as I know there are only the
       [http://www.tadpole.com/] Tadpole SPARC and ALPHA laptops, and
       some other ALPHA laptops available.
       [http://www.naturetech.com.tw/] NatureTech offers also SPARC CPUs
       in laptops. The TuxMobil survey of
