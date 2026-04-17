#  Linux on the Road
## Linux with Laptops, Notebooks, PDAs, Mobile Phones and Other Portable Devices
###  Werner Heuser

`<`

Linux Mobile Edition Edition
Version 3.22

TuxMobil

Berlin
Copyright © 2000-2011 Werner Heuser
2011-12-12

**Revision History**
---
Revision 3.22 | 2011-12-12 | Revised by: wh
The address of the opensuse-mobile mailing list has been added, a section power management for graphics cards has been added, a short description of Intel's LinuxPowerTop project has been added, all references to Suspend2 have been changed to TuxOnIce, links to OpenSync and Funambol synchronization packages have been added, some notes about SSDs have been added, many URLs have been checked and some minor improvements have been made.
Revision 3.21 | 2005-11-14 | Revised by: wh
Some more typos have been fixed.
Revision 3.20 | 2005-11-14 | Revised by: wh
Some typos have been fixed.
Revision 3.19 | 2005-11-14 | Revised by: wh
A link to keytouch has been added, minor changes have been made.
Revision 3.18 | 2005-10-10 | Revised by: wh
Some URLs have been updated, spelling has been corrected, minor changes have been made.
Revision 3.17.1 | 2005-09-28 | Revised by: sh
A technical and a language review have been performed by Sebastian Henschel. Numerous bugs have been fixed and many URLs have been updated.
Revision 3.17 | 2005-08-28 | Revised by: wh
Some more tools added to external monitor/projector section, link to Zaurus Development with Damn Small Linux added to cross-compile section, some additions about acoustic management for hard disks added, references to X.org added to X11 sections, link to laptop-mode-tools added, some URLs updated, spelling cleaned, minor changes.
Revision 3.16 | 2005-07-15 | Revised by: wh
Added some information about pcmciautils, link to SoftwareSuspend2 added, localepurge for small HDDs, added chapter about FingerPrint Readers, added chapter about ExpressCards, link to Smart Battery System utils added to Batteries chapter, some additions to External Monitors chapter, links and descriptions added for: IBAM - the Intelligent Battery Monitor, lcdtest, DDCcontrol updated Credits section, minor changes.
Mobile computer devices (laptops, notebooks, PDAs, mobile cell phones, portable audio and video players, digital cameras, calculators, wearables, ...) are different from desktop/tower computers. They use certain hardware such as PCMCIA cards, infrared and BlueTooth ports, wireless LAN, LCD displays, batteries, docking stations. Hardware parts cannot be changed as easily as in a desktops, e.g. the graphics card. Often their hardware is more limited (e.g. disk space, CPU speed). Though the performance gap to desktops is becoming smaller, e.g. in many instances, laptops or notebooks can become a desktop replacement.
Hardware support for Linux (and other operating systems) and mobile computer devices is sometimes more limited (e.g. graphics chips, internal modems). They often use specialized hardware, hence finding a driver can be more difficult. Many times they are used in changing environments, so there is a need for multiple configurations and additional security strategies.
Though there are laptop, notebook, PDA and mobile phone related HOWTOs available already, this guide contains a concise survey of documents related to mobile computer devices. Also Linux features, such as installation methods for laptops, notebooks and PDAs as well as configurations for different (network) environments are described.
Although there are some caveats, Linux is a better choice for mobile computer devices than most other operating systems, because it supports numerous installation methods, works in many heterogeneous environments and needs smaller resources.
Copyright (c) 2000-2011 Werner Heuser. For all chapters except "Lectures, Presentations, Animations and Slideshows" permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with the Invariant Sections being "Preface" and "Credits", with the Front-Cover Texts being "Linux on the Road - the First Book on Mobile Linux", and with the Back-Cover Texts being the section "About the Author". A copy of the license is included in the section entitled "GNU Free Documentation License".
* * *

**Table of Contents**


[Preface](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p0-preface)


1. [About the Author](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p0c1s1-about-the-author)


2. [Sponsoring](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p0c1s2-sponsoring)


3. [About the Document](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p0c1s3-about-the-document)


4. [Contact](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p0c1s4-contact)


5. [Disclaimer and Trademarks](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p0c1s5-disclaimer-and-trademarks)


I. [Laptops and Notebooks](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1-getting-started)


1. [Which Laptop to Buy?](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1-which-laptop-to-buy)


2. [Laptop Distributions](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c2-laptop-distribution)


3. [Installation](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c3-installation)


II. [Handheld Devices - Personal Digital Assistants (PDAs)](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3-handheld-devices-pdas)


4. [Palmtops, Personal Digital Assistants - PDAs, Handheld PCs - HPCs](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c1-palmtops-pdas-handhelds)


5. [History of Linux on PDAs](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2-linux-pdas-history)


6. [Linux PDAs](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2-linux-pdas)


7. [Non-Linux PDAs - Ports and Tools](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2-linux-for-pdas-ports-and-tools)


8. [Connectivity](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c4-connectivity)


III. [Tablet PCs / Pen PCs](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4-tablet-pc)


9. [Tablet PCs / Pen PCs](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1-tablet-intro)


IV. [Mobile (Cellular) Phones, Pagers, Calculators, Digital Cameras, Wearable Computing](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4-cell-phones)


10. [Mobile (Cellular) Phones, Pagers](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1-cell-phones)


11. [Calculators, Digital Cameras, Wearable Computing](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1-wearables)


V. [Mobile Hardware in Detail](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2-mobile-hardware)


12. [Hardware in Detail: CPU, Display, Keyboard, Sound and More](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1-hardware-in-detail)


13. [Accessories: PCMCIA, USB and Other External Extensions](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2-accessories)


VI. [Kernel](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5-kernel)


14. [Kernel History](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1-kernel-history)


VII. [On the Road](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5-on-the-road)


15. [Different Environments](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1-different-environments)


16. [Solutions with Mobile Computers](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2-solutions-with-laptops)


VIII. [Appendix](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6-appendix)


A. [Other Operating Systems](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a1-other-operating-systems)


B. [Other Resources](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a2-other-resources)


C. [Repairing the Hardware](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a3-repairing-the-hardware)


D. [Survey about Micro Linuxes](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a4-survey-micro-linuxes)


E. [Dealing with Limited Resources or Tuning the System](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a5-limited-resources)


F. [Ecology and Laptops](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a6-ecology)


G. [NeoMagic Graphics Chipset Series NM20xx](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a6-neomagic-chip)


H. [Annotated Bibliography: Books For Linux Nomads](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a7-annotated-bibliography)


I. [Resources for Specific Laptop Brands](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a8-resources-specific-laptops)


J. [Credits](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a10-credits)


K. [Copyrights](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a11-copyrights)


**List of Tables**


12-1. [Arguments for the **-t** and **-R** option of **gpm**.](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#AEN2613)


**List of Figures**


6-1. [Screenshot of the YOPY PDA](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#AEN1188)


6-2. [Screenshot of the SHARP Zaurus SL-5500 PDA.](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#AEN1201)


7-1. [Screenshot of the HELIO PDA.](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#AEN1404)


7-2. [Screenshot of the iPAQ PDA.](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#AEN1426)


7-3. [Screenshot of the PALM-Pilot emulator POSE.](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#AEN1480)


12-1. [Screenshot of cardinfo](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#AEN1949)


E-1. [Screenshot of **blackbox**.](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#AEN5435)

* * *
#  Preface
| _Life is the first gift, love is the second, and understanding is the third._
---|---
|
* * *
#  1. About the Author
People like either laptops or desktops. I like to work with laptops rather than with desktops. I like Linux too. My first HOWTO was the
Also I have written some pages about Linux with all the laptops I had a chance to put Linux on. You may find them at
During the work with the Linux-Mobile-Guide I have also collected some surveys about laptop related hardware: _unofficially_
In May 2000 I have founded the German vendor
* * *
#  2. Sponsoring
##  2.1. How to and Why Sponsor?
This guide is free of charge (except the printed version, which contains an additional part) and free in the sense of the General Public Licence - GPL. Though it requires much work and could gain more quality if I would have some more hardware. So if you have a spare laptop, even an old one or one which requires repair, please let me know. For the curious, the first issues of this guide have been written on a
Or sponsor a banner ad at
You can hire me for readings or workshops on _Linux with Laptops_ , _Linux with PDAs_ , _Repairing of Laptops_ and other Linux topics, too.
* * *
##  2.2. Table of Sponsors
This guide is currently sponsored by:
  * AgendaComputing (Berlin, Germany out-of-business)


* * *
#  3. About the Document
Mirrors, Translations, Versions, Formats, URLs
* * *
##  3.1. URLs in this Document
Many times I have mentioned _MetaLab_ formerly known as _SunSite_. This site carries a heavy load, so do yourself a favor, use one of the
For _Debian/GNU Linux_ the mirror URLs are organized in the scheme **http://www. <country code, e.g. uk>.debian.org** .
Nearly all of the programs I mention are available as
* * *
##  3.2. Latest Version, Mirrors
Former issues of this text are available at the [THE LINUX DOCUMENTATION PROJECT - TLDP](http://tldp.org/).
The latest version of this document is available at
* * *
##  3.3. Proposed Translations
The following translations are under construction:
  * Chinese, John Lian <johnlian_AT_riverrich.com.tw>
  * Greek, Vassilis Rizopoulos <mscyvr_AT_scs.leeds.ac.uk>
  * Italian, Alessandro Grillo <Alessandro_Grillo_AT_tivoli.com>,
  * Japanese, Ryoichi Sato <rsato_AT_ipf.de>,
  * Portuguese, Gledson Evers <pulga_linux_AT_bol.com.br>
  * Slovenia, Ales Kosir <ales.kosir_AT_hermes.si>
  * Spanish, Jaime Robles <ea4abw_AT_amsat.org>


Please contact me before starting a translation to avoid double work. Since a translation is a great amount of work, I recommend to do this work as a group, for instance together with your
* * *
#  4. Contact
This document isn't ready yet. If you like to write a chapter or even a smaller part by yourself, please feel free to contact me. Also your suggestions and recommendations and criticism are welcome. But please don't expect me to solve your laptop related problems if the solution is already documented. Please read all appropriate manual pages, HOWTOs and WWW sites first, than you may consider to contact me or search in the chapter [Appendix B](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a2-other-resources) Other Resources mentioned below.
Werner Heuser <wehe_at_tuxmobil.org>
* * *
#  5. Disclaimer and Trademarks
This is free documentation. It is distributed in the hope that it will be useful, but without any warranty. The information in this document is correct to the best of my knowledge, but there's a always a chance I've made some mistakes, so don't follow everything too blindly, especially if it seems wrong. Nothing here should have a detrimental effect on your computer, but just in case, I take no responsibility for any damages incurred from the use of the information contained herein.
Some laptop manufacturers don't like to see a broken laptop with an operating system other than the one shipped with it, and may reload MS-Windows if you complain of a hardware problem. They may even declare the warranty void. Though in my humble opinion this isn't legal or at least not fair. Always have a backup of both the original configuration and your Linux installation if you have to get your laptop repaired.
Though I hope trademarks will be superfluous sometimes (you may see what I mean at
# I. Laptops and Notebooks

**Table of Contents**


1. [Which Laptop to Buy?](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1-which-laptop-to-buy)


1.1. [Introduction](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1s1-introduction)


1.2. [Portables, Laptops/Notebooks, Sub/Mini-Notebooks, Palmtops, PDAs/HPCs](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1s2-portables-laptops-notebooks-pdas)


1.3. [Linux Features](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1s3-linux-features)


1.4. [Main Hardware Features](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1s4-main-hardware-features)


1.5. [Sources of More Information](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1s5-sources-of-more-information)


1.6. [Linux Compatibility Check](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1s6-linux-compatibility-check)


1.7. [Writing a Device Driver](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1s7-writing-a-device-driver)


1.8. [Buying a Second Hand Laptop](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1s8-buying-a-second-hand-laptop)


1.9. [No Hardware Recommendations](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1s9-no-hardware-recommendations)


1.10. [Linux Laptop and PDA Vendor Survey](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1s9-reseller)


2. [Laptop Distributions](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c2-laptop-distribution)


2.1. [Requirements](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c2s1-requirements)


2.2. [Recommendation](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c2s2-recommendation)


3. [Installation](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c3-installation)


3.1. [Related Documentation](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c3s1-related-howtos)


3.2. [Prerequisites - BIOS, Boot Options, Partitioning](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c3s2-prerequisites-partitioning)


3.3. [Linux Tools to Repartition a Hard Disk](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c3s3-linux-tools-to-repartition)


3.4. [Laptop Installation Methods](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c3s4-installation-methods)


3.5. [Common Problems During Installation](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c3s15-common-problems-installation)

* * *
#  Chapter 1. Which Laptop to Buy?
#  1.1. Introduction
Portable computers may be divided into different categories. This is a subjective decision, but I try to do so. My groupings roughly follow the generally accepted marketing categories. The criteria could be:
  1. Weight: Often expressed in terms like Portables, Laptops/Notebooks, Sub/Mini-Notebooks, Palmtops/PDAs. There is no standard method to define the weight of a laptop, therefore the data provided by the manufacturers (and which are given below) have to be considered as approximations. The question is how the power supply (whether external or internal) or swappable parts like CD and floppy drive, are included in the weight.
Most peripheral cables are appallingly heavy. If you get a subnotebook and carry it around with a bunch of external drives, cables, and _port expander_ dongles and power converter, you may be lugging a heavier bag than if it were all in one box. Subnotebooks are useful mainly if you can afford to leave all the other junk behind.
  2. Supported Operating Systems: proprietary versus open
  3. Price: NoName versus Brand
  4. Hardware Features: display size, harddisk size, CPU speed, battery type, etc.
  5. Linux Support: graphics chip, sound card, infrared controller (IrDA®), internal modem, etc.


* * *
#  1.2. Portables, Laptops/Notebooks, Sub/Mini-Notebooks, Palmtops, PDAs/HPCs
##  1.2.1. Portables
Weight greater than 4.0 kg (9 lbs). Features like a PC, but in a smaller box and with LCD display. Examples: lunchbox or ruggedized laptops (e.g.
* * *
##  1.2.2. Laptops/Notebooks
Weight between 1.7 and 4.0 kg (4 to 9 lbs). Features custom hardware and usually a special CPU. Examples: HP OmniBook 3100, COMPAQ Armada 1592DT. The terms _laptop_ and _notebook_ seem equivalent to me.
* * *
##  1.2.3. Sub-Notebooks/Mini-Notebooks
Weight between 1.3 and 1.7 kg (3 to 4 lbs). Features: external floppy drive, external CD drive. Examples: HP OmniBook 800CT, Toshiba Libretto 100, COMPAQ Aero, SONY VAIO 505.
* * *
##  1.2.4. Palmtops
Weight between 0.7 and 1.3 kg (1.5 to 3 lbs). Features: proprietary commercial operating systems. Examples: HP200LX.
* * *
##  1.2.5. Personal Digital Assistants (PDAs)/Handheld PCs (HPCs)
Weight below 0.7 kg (1.5 lbs). Features: proprietary commercial operating systems and often non-Intel CPU with commercial operating systems like PalmOS, EPOC32, GEOS, Windows CE. Examples: Newton Message Pad, Palm III (former Pilot), Psion Series 3 and 5, CASIO Z-7000.
* * *
##  1.2.6. Wearables
Watches, digital pens, calculators, digital cameras, cellular phones and other wearables.
* * *
#  1.3. Linux Features
Due to a lack of support by some manufacturers, not every feature of a laptop is always supported or fully operational. The main devices which may cause trouble are: graphics chip, IrDA® port, sound card, PCMCIA controller , PnP devices and internal modem. Please try to get as much information about these topics before buying a laptop. But often it isn't quite easy to get the necessary information. Sometimes even the specifications or the hotline of the manufacturer aren't able to provide the information. Therefore I have included a Linux Compatibility Check chapter in every section of [Part V in _Linux on the Road_](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2-mobile-hardware) Hardware In Detail below.
Depending on your needs, you might investigate one of the vendors that provide laptops pre-loaded with Linux. By purchasing a pre-loaded Linux laptop, much of the guesswork and time spent downloading additional packages could be avoided. See TuxMobil for a
* * *
#  1.4. Main Hardware Features
Besides its Linux features, there often are some _main features_ which have to be considered when buying a laptop. For _Linux features_ please see [Part V in _Linux on the Road_](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2-mobile-hardware) Hardware In Detail below.
* * *
##  1.4.1. Weight
Don't underestimate the weight of a laptop. This weight is mainly influenced by:
  1. screen size
  2. battery type
  3. internal components, such as CD drive, floppy drive
  4. power supply
  5. material used for the case, usually they are either from plastics or from magnesium.


* * *
##  1.4.2. Display
Recent laptops come with _active_ matrix (TFT) displays. Laptops with _passive_ matrix (DSTN) are no longer manufactured. Active matrix displays have better color and contrast, but usually cost more and use more power. Also consider the screen size. Laptops may be purchased with screens up to 17". A bigger screen weighs more, costs more, and is harder to carry, but is good for a portable desktop replacement.
* * *
##  1.4.3. Batteries
The available battery types are _Lithium Ion (LiIon)_ , _Nickel Metal Hydride ( NiMH)_ and _Nickel Cadmium (NiCd)_. Though almost all current laptops come with LiIon batteries.
LiIon batteries are the most expensive ones but a lot lighter than NiCd for the same energy content, and have minimal - but present - memory effects. NiMH is better than NiCd, but still rather heavy and does suffer some (although less than NiCd) memory effects.
Unfortunately most laptops come with a proprietary battery size. So they are not interchangeable between different models.
* * *
##  1.4.4. CPU
###  1.4.4.1. Supported CPU Families
For details about systems which are supported by the Linux Kernel, see the
  1. i286: Linux doesn't support this CPU family yet. But there are some efforts at
  2. i386: This covers PCs based on Intel-compatible processors, including Intel's 386, 486, Pentium, Pentium Pro and Pentium II, and compatible processors by AMD, Cyrix and others. Most of the currently available laptops use Intel compatible CPUs and have quite good Linux support.
  3. m68k: This covers Amigas and Ataris having a Motorola 680x0 processor for x>=2; with MMU. And the early Apple/Macintosh computers.
There was a long series of Apple PowerBooks and other laptops based on the m68k chip. Macintosh Portable (an ugly 16-pound first attempt); PowerBook 100, 140, 170, 145, 160, 180c, 165c, 520c, 540c, 550c, 190; Duo 210, 230, 250, 270c, 280. The PowerBook Duos were available at the same time as the PowerBooks, they were a sort of subnotebook, but were designed so that you could plug them into a base station (a DuoDock) with more RAM, peripherals, etcetera, so that they could also act as a desktop computer. The first PowerPC PowerBooks were the ill-starred PowerBook 5300 (after the 190) and the Duo 2300c.
For a complete list of all Macintosh computers ever made, with specifications, see
The proper place to go for information on running Linux on m68k Macintoshes is
"Much like laptops of the Intel/Linux world, Mac laptops have generally different setups that can be very hard to figure out. Also, because of a general lack of machines to test, we are only aware of boots on the Powerbook 145, Powerbook 150, Powerbook 170, Powerbook 180, and Powerbook 190. Even if it boots, we currently have no support for Powerbook-style ADB, the APM support, or just about anything else on them. This means the only way to log in is with a terminal hooked up to the serial interface, this has been tested on the 170."
"Several Powerbooks have internal IDE which is supported. PCMCIA drivers will be forthcoming if someone can supply the necessary hardware information to write a driver. As always, an FPU is needed also. Many of the later models have the 68LC040 processor without FPU, and many of these processors are broken with respect to the FPU trap mechanism so they can't run regular Linux binaries even with FPU emulation. Current status on Powerbooks 140, 160, 165, 165c, 180c, 190, 520 and Duos 210, 230, 250, 270c, 280, and 280c is unknown."
Also there are two Atari laptops, for which I don't have enough information. The following quotations are from the
"The _STacy_ was released shortly after the _Mega ST_ to provide a portable means of Atari computing. STacy computers were shipped with TOS v1.04.
Designed to replace the _STacy_ as the defacto portable ST computer, the _ST Book_ brought the basic computing power of an ST to a lightweight notebook computer. This machine was only released in Europe and Atari only shipped a very small quantity. The ST Book was shipped with TOS v2.06."
From Stok, Leon <stok_AT_YIS.NL>: The STacey and the ST Book, both can't run Linux since they are only shipped with an 68000 CPU, which doesnt have a MMU unit.
As far as I know Amiga has never produced laptops. One company manufactured kits to convert desktop Amigas to portables. These used regular Amiga motherboards so any Linux setup that supports the regular Amiga setups will support these.
  4. Alpha, Sparc, Sparc64 architectures: These are currently under construction. As far as I know there are only the
  5. StrongARM: a very low-power CPU found in
For PDAs with ARM/StrongARM CPU see the [Part II in _Linux on the Road_](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3-handheld-devices-pdas)Handheld Devices part below.
  6. MIPS: Used in SGI mainframes and Cobalt Micro intranet appliances, chips based on this architecture are used in many Windows-CE machines. Linux has been ported to a few of these.
  7. AMD Processor: More about Linux on AMD processors may be found at
  8. 64bit CPUs: At TuxMobil there is a survey of


* * *
###  1.4.4.2. Miscellaneous
At higher speed, a CPU consumes more power and generates more heat. Therefore, in many laptops a special low-power CPU is used. Usually, this special CPU doesn't use as much power as a similar processor used in a desktop. These special CPUs are also more expensive. As a side effect you may find that laptops with a desktop CPU often have a quite noisy fan.
* * *
##  1.4.5. Number of Spindles
Laptops and notebooks are often described by the number of spindles.
  1. one spindle: harddisk. Usually sub-notebooks, often provided with an external optical drive (CD/DVD).
  2. two spindles: harddisk, optical drive (CD/DVD).
  3. three spindles: harddisk, optical drive (CD/DVD), floppy drive. These laptops are often used as desktop PC replacement.


* * *
##  1.4.6. Cooling
An enormously important issue. Anything based on PPC or Pentium will generate enormous amounts of heat which must be dissipated. Generally, this means either a fan, or a heat sink the size of the case. If it's a fan, the air path shouldn't get blocked, or it will overheat and burn out. This means machines with a fan mounted in the bottom are a big, big mistake: you can't use them on a soft surface.
* * *
##  1.4.7. Keyboard Quality
Though you might use your desktop computer to do longer writings, a good keyboard can save you some head- and fingeraches. Look especially for the location of special keys like: **< ESC>**, **< TAB>**, **< Pos1>**, **< End>**, **< PageDown>**, **< PageUp>** and the cursor keys.
* * *
##  1.4.8. Price
Laptops are quite expensive if you compare them with desktops (though maybe not if compared with LCD, IrDA®, PCMCIA capabilities). So you may decide between a brand or no-name product. Though I would like to encourage you to take a _no-name_ product, there are some caveats. I have experienced that laptops break often, so you are better off, when you have an after-sales warranty, which is usually only offered with brand products. Or you may decide to take a _second hand_ machine. When I tried this, I discovered that the laptop market is changing quite often. A new generation is released approximately every three months (compared by CPU speed, harddisk capacity, screen size etc.). So laptops become old very quick. But this scheme often isn't followed by the prices for second hand laptops. They seem too expensive to me. Anyway if you plan on purchasing a second hand machine, review my recommendations on checking the machine.
* * *
##  1.4.9. Power Supply
If you travel abroad pay attention to the voltage levels which are supported by the power supply. Also the power supply is usually one of the heavier parts of a laptop. Another caveat is the power plug, which often is different from country to country.
* * *
#  1.5. Sources of More Information
Specifications, manuals and manufacturer support often are not helpful. Therefore you should retrieve information from other sources too:
General information about manufacturer support you may find in my
* * *
#  1.6. Linux Compatibility Check
##  1.6.1. Related Documentation
  1. [Hardware-HOWTO](http://tldp.org/HOWTO/Hardware-HOWTO/)
  2. [Kernel-HOWTO](http://tldp.org/HOWTO/Kernel-HOWTO/)
  3. [PCI-HOWTO](http://tldp.org/HOWTO/PCI-HOWTO.html)
  4. [Plug-and-Play-HOWTO](http://tldp.org/HOWTO/Plug-and-Play-HOWTO.html)


* * *
##  1.6.2. Check Methods in General
If you can't find the necessary information through the above mentioned sources, you are on your own. Luckily, Linux provides many means to help. For details see the section [Part V in _Linux on the Road_](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2-mobile-hardware) Hardware In Detail below. In general you may use:
  1. First of all the kernel itself. Look up what kind of hardware is detected by the kernel. You get this information during boot time or by **dmesg** or by looking into `/var/log/messages`. For the very first boot messages check `/var/log/boot`.
  2. If your kernel supports the `/proc` file system you may get detailed information about PCI devices by **cat /proc/pci** Please read the kernel documentation `pci.txt`. You may get further information about unknown PCI devices at the **lspci** command from the **pci-utils** package.
  3. To retrieve information about Plug-and-Play (PNP) devices use **isapnp-tools** .
  4. Use **scsi_info** by David Hinds for SCSI devices or **scsiinfo**.


If you don't want to install a complete Linux you may retrieve this information by using a micro Linux ( see [Appendix A](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a1-other-operating-systems) Appendix A). The package **muLinux** provides even a small **systest** program and **TomsRtBt** comes with **memtest**. To use **memtest** you have to copy it on a floppy **dd if=/usr/lib/memtest of=/dev/fd0** and to reboot from this floppy.
If your laptop came with Windows, you may determine a lot of hardware settings from the installation. Boot into DOS or Windows to get the information you need.
Using Windows9x/NT to get hardware settings, basically boot Windows, then **Start - > Settings -> Control Panel -> System -> Device Manager** and write down everything, or make a hardcopy from the display using the **< PRINT>** key, plus keep a log of settings, hardware, memory, etc.
Using MS-DOS and Windows3.1x you can use the command **msd** , which is an akronym for MicroSoft Diagnostics. Or you might try one of the numerous DOS shareware utilities: **CHECK-IT** , **DR.HARD** and others.
Sometimes it's difficult to know what manufacturer has built the machine or parts of it actually. The
Many laptops are no more compatible with Windows than Linux. David Hinds, author of the PCMCIA drivers, points out that Toshiba notebooks use a proprietary Toshiba PCMCIA bridge chip that exhibits the same bugs under Windows as under Linux. IBM™ Thinkpads have serious BIOS problems that affect delivery of events to the power management daemon **apmd**. These bugs also affect MS-Windows, and are listed in IBM™'s documentation as _considerations_.
Some incompatibilities are temporary, for instance laptops that have Intel's USB chip will probably get full USB support, eventually.
* * *
#  1.7. Writing a Device Driver
If you encounter a device which is not yet supported by Linux, don't forget it's also possible to write a driver by yourself. You may look at the book from Alessandro Rubini, Andy Oram: Linux Device Drivers. There is even a free online issue
* * *
#  1.8. Buying a Second Hand Laptop
Some recommendations to check a used laptop, before buying it:
  1. Review the surface of the case for visible damages.
  2. Check the display for pixel faults. Maybe it's useful to take a magnifying glass therefore. By the way: There is a standard for pixel faults etc. ISO 13406-2.
  3. Do an IO stress-test, .e.g. with the tool **bonnie**.
  4. You may use **memtest** and **crashme** to achieve a memory test.
  5. Do a CPU stress test, e.g. with the command **md5sum /dev/urandom** or by compiling a kernel.
  6. Check the floppy drive by formatting a floppy.
  7. Check the CD/DVD drive by reading and writing a CD/DVD.
  8. To check the battery seems difficult, because it needs some time: one charge and one work cycle. You may use **battery-stats** to do so, but note this tool only offer APM support, it is not available with ACPI support yet.
  9. To check the surface of the harddisk you may take **e2fsck**. There is also a Linux tool **dosfsck** or the other **fsck** tools.
  10. To test the entire disk (non-destructively), time it for performance, and determine its size, as root do: **time dd if=/dev/had of=/dev/null bs=1024k** .
  11. Check whether the machine seems to be stolen. I have provided a


AFAIK there is no Linux tool like the DOS tools CHECK-IT, DR. HARD, SYSDIAG and others. These tools include many of the tests in one integrated suite. One of the best in my humble opinion is the tool IrDA® port.
Please note this quotation from the disclaimer: "This program is written with the target audience being a trained, experienced technician. It is NOT designed to be used by those ignorant of computer servicing. Displays are not _pretty_ but functional. Information is not explained since we are not trying to educate. This software should be considered to be just like any other tool in a tech's toolbox. It is to be applied with care, in the right situation, in order to find answers to specific problems. If you are an end user who is less than confident of dealing with computer hardware, this is probably not a program for you."
Laptop computers, unlike desktop machines, really do get used up. _Lithium batteries_ are good for no more than 400 recharge cycles, sometimes much fewer. _Keyboards_ wear out. _LCD screen backlighting_ grows dim. _Mouse buttons_ fail. Worst of all, _connectors_ get loose as a result of vibration, causing intermittent failures (e.g. only when you hit the <Enter> key). We have heard of a machine used on the table in a train being shaken to unusability in one trip.
* * *
#  1.9. No Hardware Recommendations
It's difficult to give any recommendations for a certain laptop model in general. Your personal needs have to be taken into account. Also the market is changing very quickly. I guess every three months a new generation of laptops (with bigger harddisk space, higher CPU speed, more display size, etc.) comes into the market. So I don't give any model or brand specific recommendations. But you may check my
A good way to check Linux hardware compatibility the next time you go shopping a laptop is using a
* * *
#  1.10. Linux Laptop and PDA Vendor Survey
You may check the
Often it is difficult to get laptops without a pre-installed Microsoft operating system. In case you do not want to use it you may read
* * *
#  Chapter 2. Laptop Distributions
#  2.1. Requirements
From the [Battery-Powered-HOWTO](http://tldp.org/HOWTO/Battery-Powered/) I got this recommendation (modified by WH):
A Message to Linux Distributors: If you happen to be a Linux distributor, thank you for reading all this. Laptops are becoming more and more popular, but still most Linux distributions are not very well prepared for portable computing. Please make this section of this document obsolete, and make a few changes in your distribution.
The installation routine should include a configuration, optimized for laptops. The _minimal install_ is often not lean enough. There are a lot of things that a laptop user does not need on the road. Just a few examples. There is no need for three different versions of **vi**. Some portable systems do not need printing support.
Don't forget to describe _laptop-specific installation problems_ , e. g. how to install your distribution without a CD/DVD-ROM drive.
Add better _power management_ and seamless _PCMCIA support_ to your distribution. Add a recompiled kernel and an alternative set of PCMCIA drivers with _apm support_ that the user can install on demand. Include a precompiled _apmd package_ with your distribution. Also include IrDA® infrared support and USB support.
Add support for dynamically _switching network configurations_. Most Linux laptops travel between locations with different network settings (e. g. the network at home, the network at the office and the network at the university) and have to change the network ID very often.
Add a _convenient PPP dialer_ with an address book, that does not try to start multiple copies of the PPP daemon if you click on the button twice (e.g., the RedHat **usernet** tool). It would be nice to have the PPP dialer also display the connection speed and some statistics. One nice command line dialer that autodetects modems and PPP services is **wvdial** from
At TuxMobil you may find a huge number of links to
  * in German
  * in Russian
  * and in Chinese


* * *
#  2.2. Recommendation
The _debian-laptop_ including a searchable archive is provided. And Debian/GNU Linux is free.
At the end of August 1999 the _meta-package_ dedicated to laptops are on the way.
Note: I know other Linux distributions work well with laptops, too. I even tried some of them, see my pages about certain laptops mentioned above.
* * *
#  Chapter 3. Installation
#  3.1. Related Documentation
  1. [CDROM-HOWTO](http://tldp.org/HOWTO/CDROM-HOWTO/)
  2. [CD-Writing-HOWTO](http://tldp.org/HOWTO/CD-Writing-HOWTO.html)
  3. [Config-HOWTO](http://tldp.org/HOWTO/Config-HOWTO/)
  4. [Diskless-HOWTO](http://tldp.org/HOWTO/Diskless-HOWTO.html)
  5. [Installation-HOWTO](http://tldp.org/HOWTO/Installation-HOWTO/)
  6. [Pre-Installation-Checklist-HOWTO](http://tldp.org/HOWTO/Pre-Installation-Checklist/index.html)
  7. [Update-HOWTO](http://tldp.org/HOWTO/Update.html)
  8. [Hard-Disk-Upgrade-HOWTO](http://tldp.org/HOWTO/Hard-Disk-Upgrade/)
  9. [Linux Installation and Getting Started](http://www.tldp.org/LDP/gs/gs.html)
  10. [Install-From-Zip-HOWTO](http://tldp.org/HOWTO/Install-From-ZIP.html)
  11. [ZIP-Drive-HOWTO](http://tldp.org/HOWTO/ZIP-Drive.html)


* * *
#  3.2. Prerequisites - BIOS, Boot Options, Partitioning
##  3.2.1. BIOS
When starting a fresh installation you should try with standard BIOS options. If something doesn't work you should try to modify BIOS options. For example a well known trouble maker is the Plug-and-Play - PnP option (which comes with different names). See also the BIOS section in the hardware section below.
* * *
##  3.2.2. Boot Options
There are many boot options, which have effects on the behavior of laptops, e.g. **apm=on|off** and **acpi=on|off** : For details see [BootPrompt-HOWTO](http://tldp.org/HOWTO/BootPrompt-HOWTO.html) and the Kernel documentation in `/usr/src/linux/Documentation/kernel-parameters.txt` .
* * *
##  3.2.3. Partitioning
Partitioning can be done in a very sophisticated way. Currently I have only some first thoughts. I assume that with laptops there are still some reasons (e.g. updating the firmware of PCMCIA cards and BIOS) to share Linux and Windows9x/NT. Depending on your needs and the features of your laptop you could create the following partitions:
  * BIOS, some current BIOSes use a separate partition, for instance COMPAQ notebooks
  * suspend to disk, some laptops support this feature
  * swap space Linux
  * swap space Windows9x/NT
  * Linux base
  * Linux `/home` for personal data (please consider an encrypted partition for security reasons, for details about encryption see the according chapter below)
  * common data between Linux and Windows9x/NT
  * small (~32MB) boot partition for yaBoot (Linux/PPC boot loader), in HFS _MacOS Standard_ format.


Note this chapter isn't exhausting yet. Please read the appropriate HOWTOs first, e.g. the [Partition-HOWTO](http://tldp.org/HOWTO/Partition/) .
* * *
#  3.3. Linux Tools to Repartition a Hard Disk
##  3.3.1. GNU parted
* * *
##  3.3.2. ext2resize
**parted** project.
* * *
##  3.3.3. fixdisktable
Something was recently published on the <linux-kernel_at_vger.rutgers.edu> mailing list about a partition recovery program. I have neither used , nor examined, nor read much about it (except for the HTML page.) It may be useful to some of you if you have problems with
* * *
##  3.3.4. Caveats
Before repartitioning your hard disk take care about the disk layout. Especially look for hidden disk space or certain partitions used for _suspend to disk_ or _hibernation_ mode. Some laptops come with a partition which contains some BIOS programs (e.g. COMPAQ Armada 1592DT). Search the manual carefully for tools like **PHDISK.EXE** , Suspend to Disk, Diagnostic TOOLS.
APM "Suspend-To-Disk" feature ... if you already have a valid hibernation partition, you should be able to use it from any operating system that can handle APM suspends.
However, if one ever upgrades hard drive, memory, or repartitions their hard drive, they discover that they either have to do without the suspend-to-disk feature or boot to DOS and use the **PHDISK.EXE** program provided with their laptop or directly from Phoenix Technologies.
Now, Linux users are free from this restriction. **lphdisk** is a Linux utility that properly prepares these partitions for use. Not only does this eliminate having to boot to DOS, but my utility does not exhibit some of the nastier bugs that its DOS counterpart has."
Please see chapter DOS Tools to Repartition a Hard Disk, too.
* * *
##  3.3.5. Multi Boot
Please see the chapter chapter [Chapter 15](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1-different-environments) Different Environments, for information about booting different operating systems from the same harddisk.
* * *
#  3.4. Laptop Installation Methods
| _There's More Than One Way To Do It - TMTOWTDI_
---|---
| _Larry Wall, Tom Christiansen & Randal L. Schwartz: Programming Perl, Sec. Ed. 1996 p. 10 _
From the [Battery-Powered-HOWTO](http://tldp.org/HOWTO/Battery-Powered/) : "Installing and using Linux on a laptop is usually no problem at all, so go ahead and give it a try. Unlike some other operating systems, Linux still supports and runs well on even very old hardware, so you might give your outdated portable a new purpose in life by installing Linux on it."
One of the great benefits of Linux are its numerous and flexible installation features, which I don't want to describe in detail. Instead I try to focus on _laptop specific methods_ , which are necessary only in certain circumstances.
Most current distributions support installation methods which are useful for laptops, including installation from CD-ROM/DVD, via PCMCIA and NFS (or maybe SMB). Please see the documents which are provided with these distributions for further details or take a look at the above mentioned manuals and HOWTOs.
* * *
##  3.4.1. From a Boot Floppy plus CD/DVD-ROM - The Traditional Way
With modern laptops, the traditional Linux installation method (from one boot floppy, one support floppy and a package of CD-ROMs or one DVD) should be no problem, if there is a floppy drive and a CD-ROM drive available. Though with certain laptops you might get trouble, if you can not use _the floppy drive and the CD/DVD-ROM drive_ simultaneously, or if the floppy drive is _only available as a PCMCIA device_, as with the Toshiba Libretto 100. Some laptops support also booting and therefore installation completely from a CD drive, as reported for the SONY VAIO in the [VAIO+Linux-HOWTO](http://tldp.org/HOWTO/VAIO+Linux.html) . Note: Check the BIOS for the CD boot option and make sure your Linux distribution comes on a bootable CD.
Certain laptops will only boot _zImage_ kernels. _bzImage_ kernels won't work. This is a known problem with the IBM™ Thinkpad 600 and Toshiba Tecra series, for instance. Some distributions provide certain boot floppies for these machines or for machines with limited memory resources,
* * *
##  3.4.2. From a CD/DVD-ROM - The Usual Way
Newer laptops are able to boot a Linux distribution from a bootable CD/DVD-ROM. This allows installation without a floppy disk drive. If the CD/DVD drive is _only available as a PCMCIA device_, as with the SONY VAIO PCG-Z600TEK, see the chapter about installing from PCMCIA devices below.
* * *
##  3.4.3. From a DOS or Windows Partition on the same Machine
This is a short description of how to install from a CD-ROM under DOS without using boot or supplemental floppy diskettes. This is especially useful for notebooks with _swappable floppy and CD-ROM components_ (if both are mutually exclusive) or if they are _only available as PCMCIA devices_. I have taken this method from
  1. Get the following files from your nearest Debian FTP mirror and put them into a directory on your DOS partition: **resc1440.bin drv1440.bin base2_1.tgz root.bin linux install.bat** and **loadlin.exe**.
  2. Boot into DOS (not Windows) without any drivers being loaded. To do this, you have to press <**F8** > at exactly the right moment during boot.
  3. Execute **install.bat** from the directory where you have put the downloaded files.
  4. Reboot the system and install the rest of the distribution, you may now use all the advanced features such as PCMCIA, PPP and others.


This should work for other distributions as well. Maybe you have to do some appropriate changes.
* * *
##  3.4.4. From a Second Machine With a Micro Linux On a Floppy
###  3.4.4.1. Introduction
Because of their small or nonexistent footprint, micro-Linuxes are especially suited to run on laptops, particularly if you use a company-provided laptop running Windows9x/NT. Or for installation purposes using another non Linux machine. There are several _micro_ Linux distributions out there that boot from one or two floppies and run off a ramdisk. See [Appendix A](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a1-other-operating-systems) Appendix A for a listing of distributions.
I tried the following with **muLinux** ( available at **muLinux** doesn't support PCMCIA yet, you may use **TomsRtBt** instead. In turn **TomsRtBt** doesn't support **PPP** but provides **slip**. Note: Since version 7.0 **muLinux** provides an Add-On with PCMCIA support.
I have described how to copy an already existing partition, but it might also be possible to achieve a customized installation. Note: Usually you would try to achieve an installation via NFS, which is supported by many distributions. Or if your sources are not at a Linux machine you might try the SMB protocol with SAMBA, which is also supported by **muLinux** .
* * *
###  3.4.4.2. Prerequisites
You need two machines equipped with Linux. With the laptop (client/destination) on which you want to install Linux use the muLinux floppy. The other machine (server/source) may be a usual Linux box or also using muLinux. Though its low transfer rate I use a serial null modem cable because its cheap. You may apply the appropriate method using a PCMCIA network card and a crossover network cable or a HUB, or a parallel "null modem" cable and PLIP. As the basic protocol I used PPP, but you may also use SLIP. For the data-transfer I used **nc**. Note: this is an abbreviation for **netcat** , some distributions use this as the program name. You may use **ftp** , **tftp** , **rsh** , **ssh** , **dd** , **rcp** , **kermit** , **NFS** , **SMB** and other programs instead. If you prefer encrypted connections there is
Basic requirements are:
  1. A good knowledge about using Linux. You have to know exactly what you are doing, if not you might end destroying former installations.
  2. A null modem serial cable.


* * *
###  3.4.4.3. Source Machine
At your _source_ machine issue the following commands (attention: IP address, port number, partition and tty are just examples!):
  1. Edit `/etc/ppp/options`, it should contain only:
```
/dev/ttyS0
115200
passive

```

---
  2. With muLinux versions 3.x you may even use the convenient command **setup -f ppp** .
  3. Start PPP: **pppd** .
  4. Configure the PPP network device: **ifconfig ppp0 192.168.0.1** .
  5. Add the default route: **route add default gw 192.168.0.1** .
  6. Check the network connection: **ping 192.168.0.2** , though the destination machine isn't up yet.
  7. Start the transfer from another console, remember **< LEFT-ALT><Fx>**: **cat /dev/hda2 | gzip -c | nc -l -p 5555** .
  8. After the transfer (there are no more harddisk writings) stop the ping: **killall ping** .


* * *
###  3.4.4.4. Destination Machine
At the _destination_ machine issue:
  1. Edit `/etc/ppp/options`, it should contain only:
```
/dev/ttyS0
115200
passive

```

---
  2. With muLinux versions >= 3.x you may even use the convenient command **setup -f ppp** .
  3. Start PPP: **pppd** .
  4. Configure the PPP network device: **ifconfig ppp0 192.168.0.2** .
  5. Add the default route: **route add default gw 192.168.0.2** .
  6. Check the network connection, by pinging to the source machine: **ping 192.168.0.1** .
  7. Change to another console and get the data from the server: **nc 192.168.0.1 5555 | gzip -dc >/dev/hda4** .
  8. 400 MB may take app. 6 hours, but your mileage may vary.
  9. Stop the transfer, when it is finished with: **< CTL><C>** . This can probably be avoided (but I didn't test it) by adding a timeout of 3 seconds using the **-w 3** parameter for **nc** at the destination machine **nc -w 3 192.168.0.1 5555 | gzip -dc >/dev/hda4**
  10. After the transfer is completed, stop the ping: **killall ping** .


* * *
###  3.4.4.5. Configuration of the Destination Machine after the Transfer
  1. Edit `/etc/fstab` .
  2. Edit `/etc/lilo.conf` and `/etc/lilo.msg` and start **lilo** .
  3. Set the new root device to the kernel: **rdev image root_device** .


* * *
###  3.4.4.6. Miscellaneous
  1. You may use **bzip2** the same way as **gzip** (untested).
  2. Since **rshd** , **sshd** , **ftpd** daemons are not available with muLinux, you have to build your own file transfer mechanism with **nc** also known as **netcat** , as described above.
  3. I had to set up both PPP sides very quickly or the connection broke, I don't know why.
  4. Speed optimization has to be done. Maybe these PPP options will help: **asyncmap 0** or **local**.
  5. I checked this only with a destination partition greater than the source partition. Please check **dd** instead of **cat** therefore.
Or do the following (untested): At the destination machine **cd** into the root directory `/` and do **nc -l -p 5555 | bzip2 -dc | tar xvf -**. At the source machine **cd** into the root directory `/` and do **tar cvf - . | bzip2 | nc -w 3 192.168.0.2 5555**. This should shorten the time needed for the operation, too. Because only the allocated blocks need to be transferred.
  6. Don't **mount** the destination partition.


* * *
##  3.4.5. From a Second (Desktop) Machine With a Hard Disk Adapter
From Adam Sulmicki <adam_AT_cfar.unc.edu> I got this hint: Most but not all harddisks in laptops are removable, but this might be not an easy task. You could just buy one of those cheap 2.5" IDE converters/adapters which allow you to connect this harddisk temporarily to a desktop PC with IDE subsystem, and install Linux as usual using that PC. You may do so using the harddisk as the first IDE drive or besides as the second IDE drive. But then you need to be sure that the bootloader (e.g. **lilo**) writes to the right partition. Also you have to make sure that you use the same translation style as your laptop is going to use (i.e. LBA vs. LARGE vs. CHS ). You will find additional information in the [Hard-Disk-Upgrade-HOWTO](http://tldp.org/HOWTO/Hard-Disk-Upgrade/index.html). You might copy an existing partition, but it is also possible to achieve a customized installation. Instead of a desktop PC you may use a second laptop, which may offer better features like a CD/DVD, to put the harddisk in.
The most common adapter formats are 2.5" IDE adapters (Parallel ATA - PATA). As far as I know Serial ATA (SATA) harddisks are not available for laptops yet. But they could be attached to Serial ATA interfaces in a desktop PC even without an adapter (at least I guess, but I will verify this as soon as I have SATA equipment available). Some small subnotebooks feature 1.8" harddisks with ZIF connectors. These connectors are ATA compatible, and IDE adaptors for them are available also.
* * *
##  3.4.6. From a PCMCIA Device
Since I don't have a laptop which comes with a PCMCIA _floppy drive_ (for instance Toshiba Libretto 100), I couldn't check this method. Please see the chapter Booting from a PCMCIA Device in the PCMCIA _harddisk_ is possible.
Anyway, when you are able to boot from a floppy and the laptop provides a PCMCIA slot, it should be possible to use different PCMCIA cards to connect to another machine, to an external SCSI device, different external CD and ZIP drives and others. Usually these methods are described in the documentation which is provided with the distribution.
The Sony Vaio (PCG-Z600) comes with an external USB-Floppy and an external CD-ROM (PCMCIA). You can boot from the CD-ROM, but afterwards Linux doesn't recognize the same drive anymore so that you can't install from it. You'll have to add the bootparameter **linux ide2=0x180,0x360** (or 0x180,0x386?) at the LILO boot prompt if you want Linux to recognize a PCMCIA CDROM after the kernel has booted.
* * *
##  3.4.7. From a Parallel Port ZIP Drive
I couldn't check this method by myself, because I don't have such a device. Please check the appropriate [Install-From-Zip-HOWTO](http://tldp.org/HOWTO/Install-From-ZIP.html) . Also I don't know how much these installation methods are supported by the Linux distributions or the micro Linuxes. I suppose you have to fiddle around a bit to get this working.
From Jeremy Impson <jdimpson_AT_acm.org>: I installed Red Hat 6.1 on a Libretto 50CT. It only has a PCMCIA floppy drive. (Which BTW isn't well supported by the default PCMCIA floppy driver. I needed to download a patch from some Linux on Libretto web site.)
Linux will boot off the PCMCIA floppy drive, however. It just can't go back to the floppy after loading the kernel. My Libretto (the 50CT) only has one PCMCIA slot (later models had two slots, or I could have gotten the enhanced port replicator, which gave it another slot). So I couldn't boot off a floppy and then mount a remote filesystem.
So I downloaded ZipSlack (Slackware designed for running from a ZIP disk) and used another PC to load it onto a ZIP disk. I attached the ZIP drive to the Libretto (via the parallel port on the regular port replicator that comes with it) and booted from the Slackware boot disk in the PCMCIA floppy drive. When booted, I removed the floppy drive and inserted and configured a network PCMCIA card. At this point the kernel is in memory and it is using the filesystem on the ZIP disk.
I partitioned and formatted the Libretto's harddrive and then ftp'd Red Hat 6.1 installation source onto one of the new partitions (the partition that would become `/home` when everything gets done). This is the key: if you don't have enough disk space to have the installation files plus enough to actually install the OS on to, this method won't work.
I shut down the ZipSlack kernel and rebooted it using a RedHat install disk in the floppy drive. I pointed it at the RH6.1 installation media already on the harddrive and started the install.
* * *
##  3.4.8. From a Parallel Port CD Drive (MicroSolutions BackPack)
I had tried myself to install Linux using the MicroSolutions BackPack parallel CD-ROM drive. It is fully supported by Linux and I haven't had any major problem running it. Until version 2.0.36 it is supported by its own module (**bpck**) while in later versions it has been merged in the more general parallel port ide adaptors (the **paride** module that relays then of course on more specific low level drivers, which in the BackPack case is still called **bpck**).
In RedHat 5.x based installations the **bpck** module is available already at installation stage so you'll just have to select the BackPack cdrom from the _Other CD-ROMs_ at the installation stage and then give it some more options (but **autoprobe** should work just fine).
In RedHat 6.x (which uses 2.2.x kernels and should then use **paride**), the BackPack support was dropped. So to install the distribution from such a device, you will have to customize the bootdisk (adding the necessary modules) and the installation will be done without any problem.
Federico Pellegrin has customized a RedHat bootdisk that includes all the parallel CDROM devices that are supported by the distribution Linux kernel version (2.2.12) that should then work on all the supported parallel CDROM devices (even if he only tested it on his MicroSolutions BackPack since he doesn't have other similar hardware). You can find
As from RedHat 6.2 a supplementary driver disk was included in the distribution to support the paride devices. You'll just have to create the driver disk (the image file is **paride.img** and can be found in the `images/drivers` directory) in the usual way and insert it when the installer will ask for it.
Of course I suppose there isn't any problem in installing any other Linux distribution using such a device as long as you can add and configure the appropriate modules at the very beginning of the installation stage, but I haven't tested any.
You should take care of the mode the parallel port uses (ECP, EPP, Output only, PS/2) since some of them may cause your laptop to suddenly freeze or cause serious data corruption. On the other side some modes make the communication dramatically slow (I found the best choice on my laptop the PS/2, but you should make some tests).
This chapter is a courtesy of Federico Pellegrin. Please check also the [CDROM-HOWTO](http://tldp.org/HOWTO/CDROM-HOWTO/).
* * *
##  3.4.9. From a Parallel Port Using a Second Machine
PLIP Network Install
I got this courtesy by Nathan Myers <ncm_AT_cantrip.org>: "Many distributions support installing via a network, using FTP, HTTP, or NFS. It is increasingly common for laptops to have only a single PCMCIA slot, already occupied by the boot floppy drive. Usually the boot floppy image has drivers for neither the floppy drive itself, nor the PCMCIA subsystem. Thus, the only network interface available may be the parallel port.
Installation via the parallel port using the PLIP protocol has been demonstrated on, at least, Red Hat. All you need is a _Laplink_ parallel cable, cheap at any computer store. See the [PLIP-HOWTO](http://tldp.org/HOWTO/PLIP.html) for details on setting up the connection. Note that (uniquely) the RedHat installation requires that the other end of the PLIP connection be configured to use ARP (apparently because RedHat uses the DOS driver in their installer). On the host, either **export** your CD file system on NFS, or **mount** it where the ftp or web daemon can find it, as needed for the installation."
The [PLIP Install HOWTO](http://www.tldp.org/HOWTO/PLIP-Install-HOWTO.html) by Gilles Lamiral describes how to install a Linux distribution on a computer without ethernet card, nor CD drive, but just a local floppy drive and a remote NFS server attached by a nullmodem parallel cable.
* * *
##  3.4.10. From a USB Storage Device (Stick, CD, DVD, Floppy)
If booting from an USB device is supported from the BIOS, it is possible to install Linux from this drive. Besides some old laptops, almost all laptops equipped with USB ports support this feature.
First you have to configure the BIOS to boot from an USB device. Sometimes it is possible to use a certain key combination (e.g. <ESC>) during the boot process to select the boot device.
Second you have to install Linux on the boot medium (let's say an USB-Stick) and make it bootable. There are some special Linux distributions available, which are dedicated for such purposes, e.g.:
* * *
##  3.4.11. Installing via Network Interface
On most modern laptops and notebooks with integrated network card, a network installation via the PXE protocol is easy to achieve. This comes in handy especially if there is no CD or DVD drive available.
* * *
###  3.4.11.1. How to Prepare the Source Machine
For my installation I have used a Knoppix CD in the source machine. Just enable the Terminal Server (KNOPPIX->Server-Dienste->Terminal-Server KNOPPIX-Services-Start-> KNOPPIX Terminal Server) For almost any laptop model the default network drivers should work. Disable secure options, otherwise you will not be able to become the root user on the target machine. Besides using Knoppix, there are numerous ways to prepare the source machine for PXE. I haven't checked the EtherBoot protocol yet, but this might work too.
* * *
###  3.4.11.2. How to Prepare the Target Machine
Look up the BIOS for something like a NetBoot Option and set it on. Boot the machine and choose booting from the network device. This is usually achieved by pressing a certain key during boot up or by preselecting the network interface as the boot device in the BIOS. Now Knoppix should come up. Open a shell and do an **su** to become root. To achieve a hard disk installation do either **knx-hdinstall** for Knoppix <=3.3 or **knoppix-installer** for Knoppix >=3.3.
* * *
##  3.4.12. Installing via VNC
You might ask why do a laptop installation via the VNC protocol? Indeed I know only of one reason to do so. Imagine you want to use a laptop with a broken keyboard you may use the keyboard of the remote machine to achieve the installation. Though you have to do a few key stroke to initiate the VNC installation! You have to prepare the source machine accordingly (instructions how to do so will follow later). For recent SuSE versions the distribution is already prepared, see the handbook for details.
* * *
##  3.4.13. Installing Linux on Small Machines
If you have less than 8MB memory and want to install via NFS you may get the message "fork: out of memory". To handle this problem, use **fdisk** to make a swap partition (**fdisk** should be on the install floppy or take one of the mini Linuxes described above). Then try to boot from the install floppy again. Before configuring the NFS connection change to another console (for instance by pressing <ALT><F2>) and issue **swapon /dev/xxx** (xxx = swap partition ). Thanks to Thomas Schmaltz.
Bruce Richardson has written the [4MB-Laptop-HOWTO](http://tldp.org/HOWTO/4mb-Laptops.html) on installing a modern Linux distribution (specifically Slackware 7.0) onto laptops with 4MB RAM and <= 200MB hard disks. Another HOWTO is
* * *
##  3.4.14. Installing Linux on Apple Macintosh PowerBooks and iBooks
Macintosh PowerBooks these days come with a CD/DVD drive but not a floppy drive, but the Linux distributions for PPC support booting and installation off of a CD without any need for a floppy.
Sometimes, when you boot the installer on the PowerBooks, the screen is black; this is easily fixed by tapping the brightness key on the keyboard (somehow, the screen brightness gets reset to zero).
If you have a very recent PowerBook, it may not be supported by the kernel on the installation CD. You can get around this by booting off of a recent kernel downloaded onto your hard drive and using a ramdisk on the CD or hard drive, while still loading the installation packages from the CD (the default). (See the instructions available online for yaBoot or BootX, the Linux/PPC boot loaders; yaBoot is currently better-supported on the newest machines.)
They can also boot/install from the Macintosh (HFS) partition on the internal hard disk.
This part is a courtesy of Steven G. Johnson.
For Linux installation reports see
* * *
##  3.4.15. Mass Installation
###  3.4.15.1. 2.5" to 3.5" IDE Adapter
If you have a 2,5" to 3,5" IDE drive adapter you can install one of the laptops, and with a desktop computer clone this harddisk to the disks of the other 99 laptops. You can use the DOS utility GHOST (works pretty with ext2) or with tar if the desktop works in linux. You only need an additional boot disk for the reinstall of the **lilo** in each laptop and change the hostname and IP address. These adapter are usually quite cheap (app . ten dollar, but difficult to get) .
* * *
###  3.4.15.2. SystemImager
* * *
###  3.4.15.3. Debian/GNU Linux
You might want to take a look at
* * *
###  3.4.15.4. SuSE
The package ALICE - Automatic Linux Installation and Configuration Environment, offers CVS-based configuration files and configuration templates.
* * *
###  3.4.15.5. Replicator
Replicator is a set of scripts to automate the duplication of a Debian GNU/Linux installation from one computer to another. Replicator makes an effort to take into account differences in hardware (like HD size, video card) and in software configuration (such as partitioning). After the initial configuration, the scripts will create a bootdisk that allows you to completely (re)install a Debian box by booting from the floppy and answering a yes/no question.
* * *
###  3.4.15.6. partimage
* * *
#  3.5. Common Problems During Installation
##  3.5.1. Display Problems (Missing Lines, Thick Borders)
A common problem during Linux installation (or afterwards) on laptops are missing lines at the bottom of the text console display, so the last command lines or the login prompt are not shown on the screen. Depending on the problem it might help:
  * Either using FrameBuffer, e.g. using a Kernel with framebuffer support and a boot option like **vga=791** , for details see the [FrameBuffer-HOWTO](http://tldp.org/HOWTO/Framebuffer-HOWTO.html).
  * Or disabling FrameBuffer, e.g. using a boot option like **vga=normal** or another resolution Also, you could try passing **video=vga16:off** on the installer boot prompt.
  * As a workaround often it is possible to switch to a second console e.g. <ALT>+<F2> , because this effect is often only related to the first console.
  * Check if there are VGA and video boot options configured in the bootloader (e.g. grub, lilo). Try to disable them at least partly, look for options like **ywrap** , etc.
  * Check the BIOS for display settings, often (older) Toshiba laptops behave like this.
  * Issue the command **resize** to get the correct screen size into the system.
  * If none of the above helps, you may try to run a start-up-script, which has to run at the end of the boot process. The script has to contain the **clear** command and/or the **reset**.


# II. Handheld Devices - Personal Digital Assistants (PDAs)

**Table of Contents**


4. [Palmtops, Personal Digital Assistants - PDAs, Handheld PCs - HPCs](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c1-palmtops-pdas-handhelds)


4.1. [Resources](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c1s1-resources)


5. [History of Linux on PDAs](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2-linux-pdas-history)


5.1. [Itsy](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2s4-itsy)


6. [Linux PDAs](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2-linux-pdas)


6.1. [AgendaComputing: Agenda VR3](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2s1-agenda-vr3)


6.2. [Samsung: YOPY](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2s8-yopy)


6.3. [SHARP SL-5000/5500/C700-860/C3x00/6000 aka Zaurus](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2s8-zaurus)


7. [Non-Linux PDAs - Ports and Tools](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2-linux-for-pdas-ports-and-tools)


7.1. [HELIO](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2s2-helio)


7.2. [iPAQ](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2s3-ipaq)


7.3. [Newton Message Pad](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2s5-newton-message-pad)


7.4. [PALM-Pilot](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2s6-palm-pilot)


7.5. [HandSpring VISOR](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2s6-handspring-visor)


7.6. [Psion 5](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c2s7-psion-5)


8. [Connectivity](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c4-connectivity)


8.1. [From a Linux Box to a non Linux PDA](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c4s1-introduction)

* * *
#  Chapter 4. Palmtops, Personal Digital Assistants - PDAs, Handheld PCs - HPCs
| _Linux PDAs, because using your palm isn't as good as the real thing._
---|---
| _Motto of_
* * *
#  4.1. Resources
  1. Highly recommended is the page by Russell King
  2. For more information on Virtual Network Computing, see
  3. PDAs and infrared remote control, see
  4. There is also the
  5. I have setup a page about
  6. These newsgroups for PDA application developers are available:
codewarrior.embedded; codewarrior.games; codewarrior.linux; codewarrior.mac; codewarrior.palm; codewarrior.unix; codewarrior.windows;


* * *
#  Chapter 5. History of Linux on PDAs
This chapter is not complete yet, there should be more information on 286 based PDAs which were Linux capable.
* * *
#  5.1. Itsy
The Itsy prototype offered considerably more computing power and memory than other PDAs of its time, enabling demanding applications such as speech recognition. It was designed as an open platform to facilitate innovative research projects. The base Itsy hardware provided a flexible interface for adding a custom daughtercard, and Itsy software has been based on the Linux OS and standard GNU tools.
* * *
##  5.1.1. Resources
  1. COMPAQ/Digital is the manufacturer of the


* * *
#  Chapter 6. Linux PDAs
The most known Linux PDAs in these days are the
There are different free distributions for Linux PDAs available, e.g.:
Most of the software for the newer PDAs can be obtained as pre-compiled IPK packages. You may search the _feed_. For an example see the
Besides these well-known Linux PDAs I will also try to point to ports for other PDAs and to tools to achieve connectivity to non-Linux PDAs, cell phones and desktop computers.
* * *
#  6.1. AgendaComputing: Agenda VR3
##  6.1.1. Resources
  1. The manufacturer of the first dedicated Linux PDA the Agenda VR3 is AgendaComputing (out-of-business).


* * *
#  6.2. Samsung: YOPY
##  6.2.1. Resources
  1. The German


**Figure 6-1. Screenshot of the YOPY PDA**
![](https://tldp.org/LDP/Mobile-Guide/html/images/yopy.png)
* * *
#  6.3. SHARP SL-5000/5500/C700-860/C3x00/6000 aka Zaurus
The SHARP Zaurus SL-5000/5500 wasn't the first Linux PDA, but the one with the greatest success in the Linux community and beyond.
**Figure 6-2. Screenshot of the SHARP Zaurus SL-5500 PDA.**
![](https://tldp.org/LDP/Mobile-Guide/html/images/zaurus1.png)
* * *
##  6.3.1. The SHARP System
You may find the official site for information about Linux on the Zaurus at
* * *
##  6.3.2. The Community Systems
Currently I know of two running systems: OpenZaurus and Debian (unofficial).
* * *
###  6.3.2.1. OpenZaurus
* * *
###  6.3.2.2. Debian
The current, unofficial version of
* * *
###  6.3.2.3. PocketWorkStation
Here are some of the features of
  * Full Debian GNU/Linux operating environment, with easy access to the many GB of available software. Want the Konqueror web browser and have 50MB free space on your SD card? Run **apt-get install konqueror** , go eat lunch and come back to find it ready to run. No porting needed.
  * Includes X11 able to run most Linux applications - it supports virtual screens larger than the physical screen, realtime anti-aliased scaling and rotation, 3-mouse-button emulation and a full keyboard (useful i.e. if you need to send Ctrl-Alt-Del to an application).
  * VNC client fbvnc (same features as X11 above) - remote administer your NT box from your Zaurus.
  * Runs completely out of a single directory (a 256MB SD card is ideal), no re-flashing or modification of the existing operating system is required.
  * Switch between QTopia and X11 whenever you like without rebooting or needing to stop any of your X11 applications.


* * *
##  6.3.3. Synchronization with your Linux PC
The QTopia-Desktop is available as a download from
* * *
##  6.3.4. External Serial Keyboard
So far I was not able to get it going. There is a site which offers a **inputattach** , which you can also get from there (source or binary for ARM). I got a Happy Hacking Keyboard Lite with a PS/2 connector. An adaptor translates to serial which itself is plugged into to the Collie serial <-> serial connector. I do not know if this chain is even possible to work. The provided patch applied with only one failing hunk which made a trivial change in the sources (include/linux/serio.h) necessary; check the output. After having re-configured the SHARP kernel config and having compiled the modules, I transferred them to the Zaurus. The modules marked and created are: newtonkbd.o, serio.o, serport.o and perhaps stowaway.o from drivers/char/joystick/ and input.o and keybdev.o from drivers/input/. When you start **inputattach** , you have to use the line **inputattach --newtonkbd /dev/ttyS0** , _not_ ttySA0 as stated on the website. For some strange reason, the Collie serial driver does not comply to the official StrongARM documentation of the kernel, which states that the serial ports are accessible via /dev/ttySAx. And because the serial_collie.o is already compiled into the Sharp kernel, you do not have to load the generic module serial.o. Well, I also tried the serial_collie.o as a module, while it was still compiled into the kernel. There were no complaints when loading it, but the system froze unpredictably, so I had to do a soft-reset quite often. Why can I load a module whose code is already in the kernel, I wonder... Anyway, it does not work. :( I tried inputattach in the --dump mode (you have to undefine a variable in the source and recompile) and it seems that there is nothing happening between the serial port and the keyboard. The call for select (man 2 select) fails due to a timeout.
* * *
##  6.3.5. Cross-Compiling
###  6.3.5.1. Kernel
In order to build the kernel, initrd and applications you need a cross-compiling environment, GCC is preferred. `/usr/share/info/iostream.ifo.gz` to `/usr/share/info/iostream-295.info.gz`. You should get some pointers for other systems at the
* * *
###  6.3.5.2. Applications
Check the
* * *
###  6.3.5.3. Tool Chains
Werner Schulte explains how to build a OPIE development Live CD. The CD contains an ISO image with the tools and methods described in his
Instructions for building a
A
* * *
##  6.3.6. Caveats
SHARP introduced a proprietary serial interface at the bottom of the Zaurus SL-5x00 series. You can buy an adaptor to a regular serial interface from them, but unfortunately, the plug is very thick and you cannot open the slide for the keyboard anymore. Hopefully, you can still plug an external keyboard into this port! You can at least plug the power cord into the adaptor so you do not have to run on battery. There are third-party adaptors available, which overcome this caveat.
There is no speaker for the soundchip of the SL-5500. You have to use the socket for the headphones to hear OggVorbis and the alikes. The buzzer currently supports only 14 different sounds defined in `<kernel-source>/include/asm-arm/sharp_char.h` , check for **SHARP_BUZ_ALL_SOUNDS**.
* * *
##  6.3.7. Resources
###  6.3.7.1. Manufacturer: SHARP
* * *
###  6.3.7.2. Kernel and Community Distributions
* * *
###  6.3.7.3. FAQs, Forums, etc.
* * *
###  6.3.7.4. Applications, Desktop Environments
  1. The


* * *
###  6.3.7.5. Software Indexes
* * *
##  6.3.8. Conversion from Palm Pilot to Zaurus
See my
* * *
#  Chapter 7. Non-Linux PDAs - Ports and Tools
#  7.1. HELIO
Currently the HELIO is only available with the proprietary VT operating system. See
* * *
##  7.1.1. Resources
  1. The manufacturer of the HELIO is
  2. PocketLinux has a port under the GPL, as well as Debian and Redhat packages. But the URL http://www.pocketlinux.com/ seems no longer available.


**Figure 7-1. Screenshot of the HELIO PDA.**
![](https://tldp.org/LDP/Mobile-Guide/html/images/home_helio_03.png)
* * *
#  7.2. iPAQ
Currently the iPAQ PDAs by COMPAQ/HP are distributed only with a WinCE operating system.
* * *
##  7.2.1. Resources
  1. The manufacturer of the iPAQ PDAs is


**Figure 7-2. Screenshot of the iPAQ PDA.**
![](https://tldp.org/LDP/Mobile-Guide/html/images/h3650.png)
* * *
##  7.2.2. Braille Terminal
* * *
#  7.3. Newton Message Pad
The Newton Message Pad was one of the first PDAs.
* * *
##  7.3.1. Resources
  1. Apple is the manufacturer of the


* * *
#  7.4. PALM-Pilot
##  7.4.1. Resources
  1. 3COM is the manufacturer of the
  2. [PalmOS-HOWTO](http://tldp.org/HOWTO/PalmOS-HOWTO/) (former Pilot-HOWTO) by David H. Silber.
  3. UNIX machine to put up a (tiny) X Window on a 3COM PalmPilot.


**Figure 7-3. Screenshot of the PALM-Pilot emulator POSE.**
![](https://tldp.org/LDP/Mobile-Guide/html/images/pose.png)
* * *
#  7.5. HandSpring VISOR
The HandSpring VISOR is a clone of the PALM-Pilot PDA.
* * *
##  7.5.1. USB
From `/usr/src/linux/Documentation/usb/usb-serial.txt`:
HandSpring Visor USB docking station. There is a
Handspring VISOR Platinum serial port is tunneld through USB, so load usbserial.o with module parameters vendor=0x82d product=0x100 (usbmgr.conf) USB is made active by starting the HotSync synchronisation per: **pilot-xfer /dev/ttyUSB0 -b -/visor/**
* * *
#  7.6. Psion 5
Currently I have information about a port for the Psion 5 and nothing about the Psion 3 series.
* * *
##  7.6.1. Resources
  1. [Psion-HOWTO](http://tldp.org/HOWTO/Psion-HOWTO.html).
  2. The


* * *
#  Chapter 8. Connectivity
#  8.1. From a Linux Box to a non Linux PDA
The purpose of the
Some more information about connectivity and synchronisation tools, as well as emulators and other software you may find at
# III. Tablet PCs / Pen PCs

**Table of Contents**


9. [Tablet PCs / Pen PCs](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1-tablet-intro)


9.1. [Introduction](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#AEN1536)


9.2. [Display](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1-tablet-display)


9.3. [Handwriting Recognition](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1-tablet-handwriting)


9.4. [Keyboard](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1-tablet-keyboard)


9.5. [Wireless LAN](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1-tablet-wlan)


9.6. [Examples](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1-tablet-examples)

* * *
#  Chapter 9. Tablet PCs / Pen PCs
#  9.1. Introduction
Tablet PCs are a special kind of notebooks. Usually without keyboard (or equipped with an external and remote keyboard), they feature a touchscreen (therefore they were also named Pen PCs) and access to wireless LAN. In a certain sense they can be compared with PDAs. Microsoft has created a special edition of their operating system for Tablet PCs and published a so-called specification. In 2003 the first Tablet PCs according to this specification entered the market. Though there have been appropriate devices with Linux many years before. See the
* * *
#  9.2. Display
##  9.2.1. Touchscreen
The [XFree86-Touch-Screen-HOWTO](http://www.tldp.org/HOWTO/XFree86-Touch-Screen-HOWTO.html) describes how to setup X11 for touchscreens. There is also a short
* * *
##  9.2.2. Screen Rotation
###  9.2.2.1. X-Windows
Some XFree86 drivers support a rotation of the display content. Use this entry in the configuration file (DEGREE can become CW - 90 degree clockwise , CCW - 90 degree counterclockwise , UD - 180 degree upside down, but which options actually work depends on the drivers:
```
Option "Rotate" "DEGREE"

```

---
From version 4.3 on **xrandr** supports only resolution settings but no rotation. But the Tiny-X server by RandR developer Keith Packard (Xkdrive) implements all of the RandR features. But this is usually not included in the major distributions. Currently
* * *
###  9.2.2.2. Utilities
There are some rotation utilities for Linux PDAs available, but I haven't tested them for Tablet PCs yet. Search the
* * *
#  9.3. Handwriting Recognition
* * *
#  9.4. Keyboard
##  9.4.1. Soft Keyboard / On Screen Keyboard
###  9.4.1.1. xvkbd
* * *
###  9.4.1.2. GNOME On-screen Keyboard (GOK)
The
* * *
##  9.4.2. Remote Keyboard
Some Tablet PCs are equipped with a remote keyboard. Data between keyboard and Tablet PC may be interchanged via InfraRed, BlueTooth or other means. If these solutions are hardware based only, they should work easily with Linux. Otherwise you probably need the technical specifications from the manufacturer.
* * *
##  9.4.3. Virtual Keyboard
There are different approaches for virtual (non physical) keyboards. Whether they work with Linux or not I could not verify yet.
* * *
#  9.5. Wireless LAN
Please see the chapter [Section 12.35](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s24-wlan) Wireless LAN below.
* * *
#  9.6. Examples
At TuxMobil there is a survey of
# IV. Mobile (Cellular) Phones, Pagers, Calculators, Digital Cameras, Wearable Computing

**Table of Contents**


10. [Mobile (Cellular) Phones, Pagers](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1-cell-phones)


10.1. [Mobile (Cellular) Phones](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1s1-cellular-phones)


10.2. [Pagers - SMS Messages](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1s2-pagers)


11. [Calculators, Digital Cameras, Wearable Computing](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1-wearables)


11.1. [Digital Cameras](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1s3-digital-cameras)


11.2. [Pocket Calculators](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1s4-calculators)


11.3. [Wearable Computing](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1s5-wearable-computing)


11.4. [Watches](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1s6-watches)


11.5. [Play Station Portable](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4c1s6-game-consoles)

* * *
#  Chapter 10. Mobile (Cellular) Phones, Pagers
You may find a
* * *
#  10.1. Mobile (Cellular) Phones
##  10.1.1. Connectivity to Mobile (Cellular) Phones with non-Linux Operating System
For NOKIA cellular phones see
Kannel also works as an SMS gateway for GSM networks. Almost all GSM phones can send and receive SMS messages, so this is a way to serve many more clients than just those using a new WAP phone.
* * *
##  10.1.2. Mobile (Cellular) Phones with a Linux Operating System
There are some
* * *
#  10.2. Pagers - SMS Messages
_Lingua::EN::Squeeze_ to compress the text down to as little as 40% of its original size, so you can get much more of your e-mail into the 160 character limit imposed by SMS. It is fully MIME compatible, and has many configurable options, including removal of quoted text. Ideal for use with procmail. A Perl script for sending the output to a typical e-mail to SMS web gateway is included.
**telnet**. The command-line client already exists for Linux, Solaris and HP-UX. A basic web interface is provided. A Win32 client is in the works.
_From:_ and _Subject:_ header are included in each mail announced.
* * *
#  Chapter 11. Calculators, Digital Cameras, Wearable Computing
| _We are all cyborgs._
---|---
| _probably from "Cyborg Manifesto" by Donna J. Haraway in Simians, Cyborgs, and Women. The Reinvention of Nature. New York: Routledge, 1991_
Though in my opinion related to the topic, these devices are not much covered in this text, yet. For general information about Embedded Systems, see
* * *
#  11.1. Digital Cameras
##  11.1.1. Related Documentation
* * *
##  11.1.2. Introduction
For information about cellular phones and digital cameras see the
Newsgroup: rec.photo.digital .
The Flashpath adapter is a diskette like device which is used to transfer data from a digital camera to a computer. See _it is not officially certified_ and released under GPL.
* * *
#  11.2. Pocket Calculators
Information about calculators e.g. HP-48 is at
See also at my pages about
* * *
#  11.3. Wearable Computing
Also related to Linux and mobile computers seems wearable computing.
See also
* * *
#  11.4. Watches
The LCD).
* * *
#  11.5. Play Station Portable
# V. Mobile Hardware in Detail

**Table of Contents**


12. [Hardware in Detail: CPU, Display, Keyboard, Sound and More](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1-hardware-in-detail)


12.1. [Introduction](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s1-intro)


12.2. [BIOS](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s1-bios)


12.3. [CPU](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s1-cpu)


12.4. [Centrino(tm), Centrino-Duo(tm)](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s1-centrino)


12.5. [PCMCIA Controller](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s2-pcmcia-controller)


12.6. [Graphics Chip](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s4-graphic-chip)


12.7. [DVI Port](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s24-dvi-port)


12.8. [Video Port / ZV Port](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s24-video-port-zv-port)


12.9. [LCD Display](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s4-lcd-display)


12.10. [Sound](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s5-sound)


12.11. [Keyboard](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s6-keyboard)


12.12. [Extra Keys / Hot Keys](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s8-ext-keys)


12.13. [Function Key](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s8-func-keys)


12.14. [Power Key](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s8-power-keys)


12.15. [Extra LEDs](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s8-ext-leds)


12.16. [Numeric Keypad](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s8-numeric-keypad)


12.17. [Pointing Devices - Mice and Their Relatives](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s7-pointing-devices)


12.18. [Advanced Power Management - APM](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s8-apm)


12.19. [ACPI](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s9-acpi)


12.20. [Power Management Unit - PMU (PowerBook)](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s10-pmu)


12.21. [Batteries](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s11-batteries)


12.22. [Memory](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s12-memory)


12.23. [Plug-and-Play Devices (PnP)](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s13-pnp)


12.24. [Docking Station / Port Replicator](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s14-docking-station-port-replicator)


12.25. [Network Connections](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s15-network-connections)


12.26. [Built-In Modem](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s16-modem)


12.27. [GPRS](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s17-gprs)


12.28. [SCSI](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s17-scsi)


12.29. [Universal Serial Bus - USB](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s18-usb)


12.30. [FireWire - IEEE1394 - i.Link](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s19-firewire)


12.31. [Floppy Drive](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s20-floppy-drive)


12.32. [Optical Drives (CD/DVD)](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s21-cd-drive)


12.33. [Hard Disk](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s23-harddisk)


12.34. [Hot-Swapping Devices (MultiBay, SelectBay, ..)](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s24-hotswap)


12.35. [WireLess Network - WLAN](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s24-wlan)


12.36. [BlueTooth](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s3-bluetooth)


12.37. [Infrared Port](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s3-infrared-port)


12.38. [FingerPrint Reader](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2s2-fingerprint-reader)


13. [Accessories: PCMCIA, USB and Other External Extensions](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2-accessories)


13.1. [PCMCIA Cards](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2s1-pcmcia-cards)


13.2. [ExpressCards](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2s2-expresscards)


13.3. [SmartCards](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2s2-smartcards)


13.4. [SDIO Cards](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2s2-sdio-cards)


13.5. [Memory Technology Devices - RAM and Flash Cards](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2s3-memory-technology-devices)


13.6. [Memory Stick](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2s1-memory-stick)


13.7. [Card Readers for SD/MMC/Memory Stick](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2s1-card-reader)


13.8. [USB Devices](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2s4-usb-devices)


13.9. [Printers and Scanners](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2s4-printers-and-scanners)


13.10. [Serial Devices](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c4s1-pda-serial-devices)


13.11. [External Storage Devices](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p3c4s1-external-storage)


13.12. [Power and Phone Plugs, Power Supply](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2s5-power-and-phone-plugs)


13.13. [Bags and Suitcases](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c2s6-bags-and-suitcases)

* * *
#  Chapter 12. Hardware in Detail: CPU, Display, Keyboard, Sound and More
#  12.1. Introduction
The following text about mobile hardware, is applicable to all kinds of mobile devices running Linux: laptops, notebook, PDAs, handheld PCs, mobile phones, wearables and more. Though sometimes you have to make the appropriate changes.
* * *
#  12.2. BIOS
Before setting up any hardware you should have a look into the BIOS. Often you may find a solution already there, e.g. options to set up the display, APM or ACPI, DMA, IrDA, PCMCIA, sound, SpeedStep, and more.
If you run into unresolvable trouble when configuring the hardware, try a BIOS upgrade from the manufacturer. For this task you usually need one of the Microsoft so-called operating systems. Or at least a DOS disk or CD.
Flashing BIOSes has become often quite complex as both DOS and floppies are fading away. Things aren't any easier when running exclusively GNU/Linux. Luckily, it is possible to
Some newer laptops e.g. ASUS M5200A are equipped with a BIOS, which is able to update itself.
The
Alternative approaches are
* * *
##  12.2.1. SMBios
There is also an alternative implementation of a DMI table decoder.
* * *
#  12.3. CPU
You may find a survey about CPUs used in mobile devices, which are Linux-supported in the chapter [Chapter 1](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p1c1-which-laptop-to-buy) Which Laptop to Buy? above.
* * *
##  12.3.1. SpeedStep
Speedstep is a feature of recent CPUs made by Intel, which lets you set CPU frequency. There are different Linux tools to get this to work. Similar features are also available for other CPUs from AMD or the StrongARM CPU, I will describe this in a later issue (assistance welcome).
Before configuring SpeedStep have a look into the BIOS options.
* * *
###  12.3.1.1. SpeedStep Tool
The **cat /proc/cpuinfo** :
```
   model name : Intel(R) Pentium(R) III Mobile CPU 1000MHz

```

---
It does not work with the mobile version of the Pentium-III: ```
   model name : Pentium III (Coppermine)

```

---
* * *
###  12.3.1.2. CPUFREQ
You might want to check into the
* * *
####  12.3.1.2.1. cpufreqd
* * *
####  12.3.1.2.2. cpudyn
* * *
####  12.3.1.2.3. cpuspeedy
* * *
####  12.3.1.2.4. powernowd
* * *
###  12.3.1.3. Laptop Mode
The
* * *
###  12.3.1.4. SONY VAIO SPIC Daemon
The **sonypi** kernel module to detect the AC adapter status and the LCD backlight, and cpufreq for CPU frequency scaling.
* * *
###  12.3.1.5. CPUIDLE
A
* * *
###  12.3.1.6. ACPI
If you have enabled ACPI support in the Kernel you may also set the SpeedStep parameters via the `/proc/apci/` interface, e.g. **echo 1 > /proc/acpi/processor/CPU0/performance** will make the CPU speed down. Note: the spaces in the command are important! Note also: this feature is deprecated for Kernel > 2.6.11. Or use this script provided by Sebastian Henschel.
```
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

```

---
* * *
#  12.4. Centrino(tm), Centrino-Duo(tm)
Intels Centrino(TM) technology consists of three parts: a Pentium M processor, a chipset, and a wireless module. Let's see how these parts are supported under Linux so far.
Here you may find current information about
* * *
##  12.4.1. CPU: Pentium-M
Robert Freund has written a concise
* * *
##  12.4.2. Chipset: 855/915
The Intel 855/915 chipset families are designed to deliver better performance at lower power. The chipsets are available as discrete memory controller hub (e.g. Intel 855PM). Or as an integrated graphics and memory controller hub (e.g. Intel 855GM). Intel provides the Extreme Graphics driver for Linux, which includes AGP GART and DRM kernel modules as a binary files. I have no experience with this drivers, because the chipsets work with XFree86/X.org drivers, too. The Pentium-M CPU may come accompanied with other graphics chipsets too, e.g. from ATI, nVIDIA or Trident.
* * *
##  12.4.3. Wireless LAN: PRO/wireless 2100/2200 LAN Mini-PCI Adapter
There are different solutions to get these cards running with Linux: drivers from Intel, NDIS wrapper and Linuxant driverloader (commercial).
Intel didn't provide drivers, when the begun to sell their Centrino technology. During this time there have been other solutions: Some vendors refuse to release technical specifications or even a binary Linux driver for their WLAN cards. NDIS wrapper tries to solve this by making a kernel module that can load NDIS (Microsoft-Windows Network Driver Interface Specification) drivers. Currently there are two implementations available. The commercial
As another workaround was the usage of a Linux-supported
* * *
##  12.4.4. Conclusion
Though Linux support is not yet complete, some features of the Centrino(TM) technology already make it worthwhile to take into account when buying your next laptop. Though the new CPUs are named so similarly to existing ones that some people mix them up, they are completely different inside. Compared to the Pentium-4 Mobile CPU, the Pentium-M will allow a smaller form factor for laptops, making them more portable and lighter. Because of their higher clockspeed, the Pentium-4 CPUs have produced too much heat to build them into slimline notebook cases. Therefore, very flat notebooks have only been available from Apple or with a Pentium III Mobile CPU. Also, the battery power the Pentium-M consumes for a given level of performance will decrease, but I do not have a benchmark about how much the savings actually are yet. PENN Computing offers a nice
Laptops based on the Centrino(TM) features are already very popular in the Linux community.
* * *
#  12.5. PCMCIA Controller
##  12.5.1. Linux Compatibility Check
With the **probe** command, which is included in the PCMCIA-CS package by David Hinds you can get the type of the PCMCIA controller. Also available by the command **cat /proc/pci**.
* * *
##  12.5.2. Related Documentation
* * *
##  12.5.3. PCMCIA Configuration - Survey
In the mailing lists where I'm a member, the question "How can I set up PCMCIA support, after the Linux installation?" comes up sometimes. Therefore I try to give a short survey. But the authoritative source for the latest information about the _PCMCIA Card Services for Linux_, including documentation, files, and generic PCMCIA information is the PCMCIA and APM see the chapter APM.
* * *
###  12.5.3.1. Software
  1. Install the newest available PCMCIA-CS package, if you take a rpm or deb package it is quite easy.
  2. Read the PCMCIA HOWTO, usually included in the PCMCIA-CS package.
  3. If necessary, install a new kernel.
  4. Make sure your kernel has module support and PCMCIA support enabled (and often APM support)
  5. Make sure your kernel also includes support for the cards you want to use, e.g. network support for a NIC card, serial support for a modem card, SCSI support for a SCSI card and so on.
  6. If you have a custom made kernel, don't forget to compile the PCMCIA-CS source against your kernel.


* * *
###  12.5.3.2. PCMCIA Controller
  1. Use the **probe** command to get information whether your PCMCIA controller is detected or not.
  2. Edit the file `/etc/sysconfig/pcmcia`. It should include **PCMCIA=y** and the type of your PCMCIA controller, e.g. **PCIC=i82365**. Since Kernel 2.6 there is a standard driver **PCIC=yenta_socket**.
  3. Start the PCMCIA services typically via **/etc/init.d/pcmcia start**. If you get two high beeps, everything should be fine.
  4. If something doesn't work, check the messages in `/var/log/messages` .


* * *
###  12.5.3.3. PCMCIA Card
  1. Check your card with **cardctl ident** .
  2. If your card is not in `/etc/pcmcia/config`, edit the file `/etc/pcmcia/<MYCARD>.conf` appropriately. Take an entry in the first file as a model. You may try every driver, just in case it might work, for instance the **pcnet_cs** supports many NE2000 compatible PCMCIA network cards. Note: it is a bad practice to edit `/etc/pcmcia/config` directly, because all changes will be lost with the next update.
  3. A list of supported cards is included in the PCMCIA-CS package. The current list you may find at
Since there are not all cards mentioned I have set up a
  4. If you use a X11 GUI, you can use **cardinfo** to insert, suspend, or restart a PCMCIA card via a nice graphical interface.


**Figure 12-1. Screenshot of cardinfo**
![](https://tldp.org/LDP/Mobile-Guide/html/images/cardinfo.png)
* * *
#  12.6. Graphics Chip
##  12.6.1. Linux Compatibility Check
###  12.6.1.1. Video Mode
Attention: The **SuperProbe** is deprecated. The tool **SuperProbe** is part of XFree86 and is able to check many graphics chips. Please read the documentation carefully, because it might crash your hardware. From **man SuperProbe** :
"**SuperProbe** is a program that will attempt to determine the type of video hardware installed in an EISA/ISA/VLB-bus system by checking for known registers in various combinations at various locations (MicroChannel and PCI machines may not be fully supported; many work with the use of the **-no_bios** option). This is an error-prone process, especially on UNIX (which usually has a lot more esoteric hardware installed than MS-DOS system do), so **SuperProbe** may likely need help from the user.
At this time, **SuperProbe** can identify MDA, Hercules, CGA, MCGA, EGA, VGA, and an entire horde of SVGA chipsets (see the -info option, below). It can also identify several HiColor/True-color RAMDACs in use on SVGA boards, and the amount of video memory installed (for many chipsets). It can identify 8514/A and some derivatives, but not XGA, or PGC (although the author intends to add those capabilities). Nor can it identify other esoteric video hardware (like Targa, TIGA, or Microfield boards).":
For testing reasons start the X11 server with **X 2 > <error.msg>**. And try to change the resolution by typing **< CTL><ALT><+>** or **< CTL><ALT><->**. Note: the + or - sign have to be taken from the numeric pad, which can be emulated at the letter pad or with the **Fn** key by some laptops.
* * *
###  12.6.1.2. Text Mode
Just watch the display and determine if it works properly. If not, try to enable different video modes at startup time. Setting up X11 can sometimes be an exercise in trial and error.
* * *
##  12.6.2. Related Documentation
  1. First of all the `/usr/share/doc/xfree86*`. Or the
  2. [XFree86-HOWTO](http://tldp.org/HOWTO/XFree86-HOWTO/)
  3. [XFree86-Video-Timings-HOWTO](http://tldp.org/HOWTO/XFree86-Video-Timings-HOWTO/)
  4. [XFree86-XInside-HOWTO](http://tldp.org/HOWTO/XFree86-XInside.html)
  5. [X-Big-Cursor-mini-HOWTO](http://tldp.org/HOWTO/X-Big-Cursor.html) (useful when running X11 on a notebook with low contrast LCD)
  6. [Keyboard-and-Console-HOWTO](http://tldp.org/HOWTO/Keyboard-and-Console-HOWTO.html)
  7. [Framebuffer-HOWTO](http://tldp.org/HOWTO/Framebuffer-HOWTO.html)


* * *
##  12.6.3. Survey X11-Servers
You might discover that some features of your laptop are not supported by
  1. VESA Frame-Buffer-Device, available with 2.2.x kernels and XFree86 3.3.2 or greater. See `/usr/src/linux/Documentation` .
Please check the latest release of


If you can't get an appropriate X11 server working, but cannot afford a commercial X11 server you may try the VGA16 or the mono server included in XFree86.
* * *
##  12.6.4. Resources
You may find a survey about
* * *
##  12.6.5. External Monitors: LCD, CRT, TV, Projector
There are several different methods to activate support for an external monitor: as a _BIOS option_ or during runtime with a _keystroke_ e.g. **< Fn>+<F4>**.
Read the X11 docs about your graphics chip carefully, for instance for the NeoMagic NM20xx chips you have to edit `/etc/XF86Config` by configuring **intern_disp** and **extern_disp**. Note: As far as I know these options are only valid for XFree86 3.3.x, for XFree86 4.x I couldn't find a similar option.
If you can't get the external monitor to work with XFree86, try a demo version of the commercial X11 servers mentioned above. Also check with the RedHat and SuSE WWW sites as they may have new, binary-only, X11 servers that may work with your laptop. Or check X11 servers from
* * *
###  12.6.5.1. Tools
The
* * *
###  12.6.5.2. Solutions
Klaus Weidner has described a **x2vnc** instead. This approach allows to add and remove the second monitor dynamically without reconfiguring or restarting anything.
* * *
##  12.6.6. Power Management for Graphics Cards
The uptime on batteries can be improved by enabling the power management features of the graphics card. There are tools available to change the clock frequency and to shut down the backlight of the display. Usually these tools are specific for a graphics card or a graphics card manufacturer. Here are some techniques for graphics cards made by ATI.
The proprietary `fglrx` driver from ATI needs to be enabled by adding the PowerState option to the Device Section in the `/etc/X11/xorg.conf` X11 configuration file:
```
Section "Device"
Identifier "aticonfig-Device[0]"
Driver "fglrx"
Option "PowerState" "1"
EndSection

```

---
After rebooting or re-starting X11 you can start the power save mode with the command **aticonfig --set-powerstate=1 --effective=now**. Use **aticonfig --list-powerstates** to get all available powerstates.
For ATI Radeon graphics cards the **rovclock** tool can be used to save power e.g. **rovclock -c 80 -m 80** to use only 80MHz chip and memory frequency. The command **radeontool light off** switches the backlight off, if closing the lid or using an extra key is not an option.
The `/sys/class/backlight`. The patch keeps the procfs brightness handling for backward compatibility. For this to archive, the patch adds two generic functions brightness_get and brightness_set to be used both by the procfs related and the sysfs related methods.
* * *
##  12.6.7. Miscellaneous
Sometimes you may encounter a display not working properly in text mode. Currently I don't have any recommendations, please see [Keyboard-and-Console-HOWTO](http://tldp.org/HOWTO/Keyboard-and-Console-HOWTO.html) .
Take care of the _backlight_ as far as I know this device can only bear a limited number of uptime circles. So avoid using screensavers too much.
For problems with X Windows and APM please see the APM chapter.
* * *
#  12.7. DVI Port
As far as I know DVI ports don't work with Linux yet. But anyway here are links to installation reports about
* * *
#  12.8. Video Port / ZV Port
Some high end laptops come with a video or ZV port (NTSC/PAL). Since I don't have a laptop with a ZV or video port yet, I can provide only some URLs USB port.
* * *
#  12.9. LCD Display
This chapter isn't ready yet, it will contain information about the lifetime of backlights, differences between CRT and LCD displays, anti-aliasing with LCD displays, the ISO 13406-2 standard about pixel defects, a survey of common resolutions: VGA, SVGA, XGA and more soon. See also the screensaver chapter and the touchscreen section in the chapter [Part III in _Linux on the Road_](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p4-tablet-pc) Tablet PC and PDA.
* * *
##  12.9.1. Laptop Displays
###  12.9.1.1. Applications
* * *
###  12.9.1.2. Fonts
* * *
##  12.9.2. PDA Displays
  * Readability; fitness to be used as a default screen font, especially on reverse-color X11 terminals
  * Optimization for program code through visually distinct characters L, l, 1, 7, |, I, i and 0, O and more.
  * Complete ISO 8859-15 character set.
  * Many point sizes to ensure optical consistency across different computers with different screen resolutions (encompassing anything from PDA displays to 20" screens).
  * Fitness for displaying ASCII art and codework/code poetry, from viewing graphics in aview, watching TV in ttv and DVDs in **mplayer** with **-vo aa** to reading mailinglists like _arc.hive_, 7-11 and writing in **mutt**.
  * Clean, minimalist visual design; no serifs, a square minuscule base matrix, rounded edges. This is a computer terminal font; it should not look like a low-res imitation of print type.


The author Florian Cramer employs this font in his "anti-desktop" setup consisting of the **ratpoison** window manager and GNU screen inside an **rxvt** terminal (with reverse color and no scrollbars), similar to what is described in this
* * *
#  12.10. Sound
##  12.10.1. Linux Compatibility Check
The only way I know to check this, is to compile the different sound drivers into the kernel and check whether they are detected or not. The best way to do so, is to compile them as modules because it's easier to load different parameters such as interrupts and IO ports this way. For the 2.2.x kernels, read `/usr/src/linux/Documentation/sound/Introduction` by Wade Hampton. This document may help you get started with sound. Also, you might try one of the commercial sound drivers mentionend below. To check whether sound works or not you may try e.g. **xmms** and one of the sounds provided in `/usr/share/sounds`.
* * *
##  12.10.2. Related Documentation
  1. [Sound-HOWTO](http://www.tldp.org/)
  2. [Visual-Bell-mini-HOWTO](http://www.tldp.org/)
  3. You may find also some good sound HOWTOs at the


* * *
##  12.10.3. Survey Sound Drivers
  1. ALSA ALSA Library (C,C++) which covers the ALSA Kernel API for applications, and create ALSA Manager, an interactive configuration program for the driver. With Kernel 2.6 these modules will be part of the Linux Kernel.
  2. As a last resort you may try the speaker module **pcsnd** , which tries to emulate a soundcard.


* * *
##  12.10.4. Additional Soundcards
PCMCIA card or not. PCMCIA sound cards are probably not supported.
Also USB may be an alternative. Most USB audio devices are supported by recent kernels. An example is Labtec Axis 712 Stereo Headset (headphones and microphone) which works in full-duplex mode. For more info about this and other Linux-compatible USB audio devices see the
* * *
##  12.10.5. External and Internal CD Drives
For playing CDs/DVDs from an external or internal CD/DVD drive, see chapter [Section 12.32](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s21-cd-drive) CD/DVD Drive below.
* * *
#  12.11. Keyboard
##  12.11.1. Linux Compatibility Check
Usually there are no problems with Linux and the keyboard. Though there are two minor caveats: First the **setleds** program might not work. Second the key mapping might not fit your needs. Some UNIX users and **vi** users expect to find the <CONTROL> key to the left of the <A> key. Many PC-type keyboards have the <CAPS-LOCK> key there. You may use **xmodmap** or **loadkeys** to re-map the keyboard. Some laptops (e.g., Toshiba) allow you to swap the <CAPS-LOCK> and <CONTROL> keys. Mark Alexander offered this solution in the linux-laptop mailing list: On RedHat, it's a one-line patch to `/usr/lib/kbd/keytables/us.map` , or whatever file is referenced in `/etc/sysconfig/keyboard`:
```
*** us.map~     Tue Oct 31 14:00:07 1995
--- us.map      Thu Aug 28 13:36:03 1997
*** 113,119 ****
keycode  57 = space            space
        control keycode  57 = nul
        alt     keycode  57 = Meta_space
! keycode  58 = Caps_Lock
keycode  59 = F1               F11              Console_13
        control keycode  59 = F1
        alt     keycode  59 = Console_1
--- 113,119 ----
keycode  57 = space            space
        control keycode  57 = nul
        alt     keycode  57 = Meta_space
! keycode  58 = Control
keycode  59 = F1               F11              Console_13
        control keycode  59 = F1
        alt     keycode  59 = Console_1

```

---
* * *
##  12.11.2. External (Second) Keyboard
A second (or external) keyboard can be attached using the PS/2 port (I suppose this is not possible via the serial port, since there is no keyboard controller for the serial port) or via USB port. Also there is one laptop with a detachable keyboard the Siemens Scenic Mobile 800. This machine uses an infrared connection to the keyboard, but I don't know whether this works with Linux.
* * *
###  12.11.2.1. External USB Keyboard Configuration
You may not need any operating system support at all to use a USB keyboard if you have a PC architecture. There are several BIOS available where the BIOS can provide USB support from a keyboard plugged into the root hub on the motherboard. This may or may not work through other hubs and does not normally work with add-in boards, so you might want to add in support anyway. You definitely want to add keyboard support if you activate operating system support, as the Linux USB support will disable the BIOS support. You also need to use Linux USB keyboard support if you want to use any of the "multimedia" types keys that are provided with some USB keyboards.
In the kernel configuration stage, you need to turn on USB Human Interface Device (HID) support and Keyboard support. Do not turn on USB HIDBP Keyboard support. Perform the normal kernel rebuild and installation steps. If you are installing as modules, you need to load the hid.o, input.o and keybdev.o modules.
Check the kernel logs to ensure that your keyboard is being correctly sensed by the kernel.
At this point, you should be able to use your USB keyboard as a normal keyboard. Be aware that LILO is not USB aware, and that unless your BIOS supports a legacy USB keyboard, you may not be able to select a non-default boot image using the USB keyboard. I have personally used a USB keyboard (and USB mouse) and experienced no problems.
* * *
###  12.11.2.2. External PS/2 Keyboard
![Warning](https://tldp.org/LDP/Mobile-Guide/images/warning.gif) |  Don't plug the external keyboard in while the laptop is booted, or plug the mouse in the keyboard port and the keyboard in the mouse port. On a Toshiba, this caused one user to have to completely shutdown the laptop, remove the keyboard/mouse, and do a cold reboot.
---|---
For PS/2 ports there is a so called Y-Cable available, which makes it possible to use external mouse and external keyboard at the same time if your laptop supports this feature.
**parkbd** module for that.
On some laptops a splitter works to allow both mouse and keyboard to be plugged in; on others it doesn't work at all. If you want to use both, you better check that it works.
* * *
#  12.12. Extra Keys / Hot Keys
##  12.12.1. Related Documentation
  1. [Keyboard-and-Console-HOWTO](http://tldp.org/HOWTO/Keyboard-and-Console-HOWTO.html)


* * *
##  12.12.2. Utilities
Some laptops offer extra buttons, e.g. - internet, mail keys, or zone keys. If the Linux kernel and XFree86/X.org generate key codes for them, **hotkeys** or just plain **xmodmap** (see the man page of this X11 programm for details) may be helpful. If Linux doesn't know about the keys, you'll have to patch the kernel first. Though I'm not quite sure some tools don't seem to require this, I don't understand how it works yet. You may also use
![Tip](https://tldp.org/LDP/Mobile-Guide/images/tip.gif) |  To get information about unknown keyboard or mouse events you may use **showkey** and **mev** (the last one is from the **gpm** package) on a console screen. But some of the extra keys are not found with these tools.
---|---
**akdaemon** is a userland daemon to invoke "the fun keys" by accessing a dev node offered by the complementary
The
Special ("easy access") buttons are supported by `lineakd.conf` file:
```
# LinEAK Configuration file for Compaq Easy Access Key 2800 (6 keys)

# Global settings
KeyboardType            = CIKP800
CdromDevice             = /dev/cdrom
MixerDevice             = /dev/mixer

# Specific keys of your keyboard
internet        = xosview
search          = kfind
mail            = kmail
multimedia      = "artsdsp xmms"
voldown         = "aumix -v -2"
volup           = "aumix -v +2"

# end lineakd.conf

```

---
For some laptop series there are Linux utilities available to control special hotkeys and other features.
* * *
#  12.13. Function Key
The function key (often labelled Fn on the key) is usually used to switch on a simulated numeric keyboard, which is provided as a separate keypad on desktop keyboards. For those who don't want to use the simulation there are additional external numeric keypads available for PS/2 ports and I suppose USB ports. Also the function key may be used in combination with some F-keys to change display brightness, adjust the speaker volume or mute them, lock the keyboard, switch between external and internal display, use different suspend modes and more. Sometimes these key combinations work out of the box with Linux. Some require dedicated tools, for these tools see the Hotkey chapter above.
* * *
#  12.14. Power Key
The power key often has different functions, besides power on and off it may be used to wake up the machine from suspend mode. This is usually achieved by pressing the power button for just a few seconds only. If you press it longer (app. more than 5 seconds) it will power down fully.
With modern laptops supporting ACPI it's also possible to achieve power off, with ACPI via the `/proc/apci/` interface.
* * *
#  12.15. Extra LEDs
Some laptops offer extra LED, e.g. - mail - LEDs. The tool **setleds** (which is part of
* * *
#  12.16. Numeric Keypad
On desktop keyboards the numeric keypad is usually separated from the character set, but laptops don't have a separated numeric keypad. There are different ways to emulate one, e.g. with the **Fn** key or with **NUM-LOCK** key. Also external numeric keyboards which connect to the PS/2 port (or USB, RS232) are available.
As described above, the numeric keyboard has to be used if you want to change the X11 resolution by typing **< CTL><ALT><+>** or **< CTL><ALT><->**. If this doesn't work or is too complicated, you may use **gvidm** will pop up a list of available modes and allows the user to select one if desired. This makes it perfect for running from an application menu or a hotkey, so you don't have to use ram for an applet constantly running. If you are running dual or multi-head displays, it will give you a list of screens so you can select the appropriate one. Also you may use **xvidtune [-next | -prev ]**. To check the current resolution you may use **xwininfo -root** , if **xvidtune** is not at hand.
* * *
#  12.17. Pointing Devices - Mice and Their Relatives
##  12.17.1. Linux Compatibility Check
You may check your mouse with the **mev** command from the GPM package.
* * *
##  12.17.2. Related Documentation
  1. [3-Button-Mouse-HOWTO](http://tldp.org/HOWTO/3-Button-Mouse.html) for serial mice
  2. [Kernel-HOWTO](http://tldp.org/HOWTO/Kernel-HOWTO/)


* * *
##  12.17.3. Mice Species
  1. Trackpad, Touchpad, are used with the majority of current laptops
  2. Trackball, e.g. COMPAQ LTE
  3. Pop-up-Mouse, e.g. HP OmniBook 800
  4. Trackpoint, Mouse-Pin, e.g. IBM™ ThinkPad and Toshiba laptops
  5. 3 Button Mice, e.g. IBM™ Thinkpads at least the 600s and some COMPAQ models e.g. Armada M700. I have heard rumor about a 3 button mouse for Texas Instruments Travelmates, but couldn't verify this yet.
  6. Touchscreen, e.g. some Fujitsu-Siemens laptops, TabletPCs and PDAs


* * *
##  12.17.4. PS/2 Mice
Most of the mice used in laptops are PS/2 mice (actually I don't know one with another mouse protocol). You may communicate with the PS/2 mouse through `/dev/psaux` or `/dev/psmouse`. If you use X Windows this device and the protocol has to be set in `/etc/X11/XF86Config`. In earlier releases, sometimes the GPM mouse manager and X Windows had trouble sharing a mouse when enabled at the same time. But as far as I know this is no problem anymore for the latest versions.
Speaking of Emulate3Buttons, 100ms is usually better than the 50ms allowed in most default setups of `/etc/X11/XF86Config` for XFree86 3.x:
```
Section "Pointer"
	...
	Emulate3Buttons
	Emulate3Timeout    100
	...
EndSection

```

---
Or in `/etc/X11/XF86Config-4` for XFree86 4.x:
```
Section "InputDevice"
	...
	Option		"Emulate3Timeout"	"100"
	Option		"Emulate3Buttons"	"true"
	...
EndSection

```

---
* * *
##  12.17.5. Touchpad
Usually a touchpad works with the PS/2 mouse device `/dev/psaux` and the PS/2 protocol (for GPM and X11, for X11 it seems also worth to check the GlidePointPS/2 protocol).
The
  1. Movement with adjustable, non-linear acceleration and speed (Options: MinSpeed, MaxSpeed, AccelFactor)
  2. Button events through short touching of the touchpad (Options: MaxTapTime, MaxTapMove)
  3. Double-Button events through double short touching of the touchpad
  4. Dragging through short touching and holding down the finger on the touchpad
  5. Middle and right button events on the upper and lower corner of the touchpad (Option: Edges)
  6. Scrolling (button four and five events) through moving the finger on the right side of the touchpad (Options: Edges, VertScrollDelta)
  7. The up/down button sends button four/five events
  8. Adjustable finger detection (Option: Finger)
  9. Ext Mouse repeater support - Alpha! (Option: Repeater)
  10. Multifinger taps: two finger for middle button and three finger for right button events
  11. Online configuration through shared-memory (in development) (Option: SHMConfig)


The **synclient** command is provided with the driver sources (note it's not included in SuSE Linux, at least not until 9.3). The command queries and modifies the Synaptics TouchPad driver parameters on the fly.
![Tip](https://tldp.org/LDP/Mobile-Guide/images/tip.gif) |  Tipping with one, two or three fingers on the touchpad simultaneously results in pressing the left, middle and respectively the right mouse-button.
---|---
There is also another touchpad driver available. **tpconfig** supports pointing devices used in notebooks by Acer, Compaq, Dell, Gateway, Olivetti, Texas Instruments, Winbook, and others.
Dell and Sony have started incorporating a touchpad, touchstick from ALPS. They are in at least the Dell Latitude CPx and the Sony VAIO laptop lines. Maintainer Bruce Kall writes: "**tpconfig** does NOT support them at this time, but I am in the process of getting the API from ALPS and will be incorporating this in the next version of **tpconfig**. The Dell's also incorporate the ALPS GlideStick in the middle of the keyboard (like the stick pointer in some of the IBM Thinkpads). I also intend to support the disabling of "tapping" the GlideStick as well. Tapping of the touchpad/touchsticks drives me crazy, I'm not sure about you (causes the "selection" of things on the screen when you don't want to)!"
**tpconfig** is a command-line utility to set options on Synaptics Touchpad and (now) ALPS Glidepad/ Stickpointers. Most people primarily use it to turn off the "tap mode" on laptop touchpads.
How to use **tpconfig** : **tpconfig** is currently supported as a command-line configuration tool. The PS/2 port does not currently support sharing. Therefore the **tpconfig** utility will not work while any other mouse driver is loaded (e.g. **gpm**). This also means that you cannot use **tpconfig** while X Windows is running. The suggested use of **tpconfig** is to run it from a startup script before gpm is started.
Not all touchpads are being from Synaptics, e.g some Gateways incorporate an EZ-Pad (Registered TM) and there might be other brands. The
The recent
In addition to translating finger motion into mouse motion and supporting the buttons, this support currently has several features (from the README):
  * a "tap" on the TouchPad causes a left mouse click
  * a "tap" followed quickly by a finger motion causes a left button drag type action.
  * a "tap" in one of the corners causes an action the default configuration is upper right causes middle mouse click and lower right causes right mouse click
  * more pressure on the touch pad speeds the motion of the cursor
  * a "tap" with a motion component (default > 2mm) initiates a toss and catch sequence. This is terminated by a finger touch on the pad (the toss also ends after 1 sec since that is the idle timeout period for the touchpad).
  * if the finger moves close to an edge then the mouse motion will be continued in that direction so that you don't need to pick up your finger and start moving again. This continued motion is pressure sensitive (more pressure is faster motion).


These features can be enabled/disabled and many of them have time and speed parameters which can be adjusted to the taste of the user.
It seems **gpm** is best known as a console biased tool. This is true, but you may use it as an X11 input device. **gpm** is used as a repeater device. In this way you can use both the built-in synaptics touchpad with all the features and at the same time a serial mouse (with three buttons). This all works smoothly together. X11 reads the mouse events from a named pipe `/dev/gpmdata` in a protocol it understands, which in my case is _Mouse-Systems-Compatible_ (5bytes). Most 3-button mice use the default protocol. So a simple reconfiguration in XF86Config is all that is required, after starting **gpm** in an appropriate way, of course.
**gpm** could be started on your laptop with the following arguments : **/usr/bin/gpm -t synps2 -M -t ms -m /dev/ttyS0** . Both touchpad and serial mouse work in console and X11 mode. You do have to create the named pipe `/dev/gpmdata` yourself.
Tapping with two fingers simultaneously to simulate a middle mouse button works on Logitech touchpads used in a few machines.
Thanks to Geert Van der Plas for most of the touchpad chapter.
* * *
##  12.17.6. Jog-Dial
The "Jog-Dial" is an input device used in the SONY VAIO laptop series. You may find a `spicdriver/Makefile`:
**CCFLAG** has to be extended with **-D_LOOSE_KERNEL_NAMES**
**CCFLAG** has to be extended with **-I/usr/src/linux- <kernel-version>/include**
The README seems to be in Japanese, here is an English version.
```
$ tar xvzf jogutils.tar.gz
$ cd jogutils
$ make
$ su
# mknod /dev/spic c 60 0
# modprobe spicdriver/spicdriver
# exit
$ cp jogapp/rcfile ~/.jogapprc
$ jogapp/jogapp

```

---
ISHIKAWA Mutsumi wrote the
* * *
##  12.17.7. Touchscreens
The only modern laptops I know which include a touchscreen are the Fujitsu Biblo 112/142 (aka MC 30) and the Palmax PD 1000/1100 (aka IPC 1000/1100).
The latest version of the
A current survey of drivers you may find at my page
* * *
##  12.17.8. Pen Devices, Mousepoints
IBM and Toshiba laptops currently come with a pen devices instead of a mousepad or trackball.
![Tip](https://tldp.org/LDP/Mobile-Guide/images/tip.gif) |  It needs some time to get used to this kind of pointer device. It may help to rest your palm at the front rest. Also it's recommended to reduce the mouse speed.
---|---
* * *
##  12.17.9. External Mouse
For better handling, e.g. with a 3 button mouse you may use an external mouse. This is usually a serial mouse or a PS/2 mouse, or in our days a USB mouse, appropriate to the port your laptop offers. Usually this is no problem. The only thing I currently don't know a solution for is the automagic detection of a newly plugged in mouse from X11. To get it work you have to restart your X server.
* * *
###  12.17.9.1. PS/2 Mouse
For PS/2 ports there are so called Y-Cable available, which make it possible to use external mouse and external keyboard at the same time if your laptop supports this feature.
![Warning](https://tldp.org/LDP/Mobile-Guide/images/warning.gif) |  Don't plug in the external mouse while powered up. If you have separate mouse and keyboard ports, make sure you plug the mouse in the mouse port and the keyboard in the keyboard port. If you don't, you may have to do a hard reboot of the laptop to get it to recover.
---|---
* * *
###  12.17.9.2. Wheel Mouse
**imwheel** includes a modified **gpm** for an alternate method of wheel input.
See also the
* * *
###  12.17.9.3. USB Mouse
This part is taken from The Linux USB Sub-System by Brad Hards.
* * *
####  12.17.9.3.1. USB Human Interface Device (HID) Configuration
#####  12.17.9.3.1.1. General HID Configuration
There are two options for using a USB mouse or a USB keyboard - the standalone Boot Protocol way and the full featured HID driver way. The Boot Protocol way is generally inferior, and this document describes the full featured way. The Boot Protocol way may be appropriate for embedded systems and other systems with resource constraints and no real need for the full keyboard and mouse capabilities.
It is important to remember that the HID driver handles those devices (or actually those interfaces on each device) that claim to comply with the Human Interface Device (HID) specification. However the HID specification doesn't say anything about what the HID driver should do with information received from a HID device, or where the information that is sent to a device comes from, since this is obviously dependent on what the device is supposed to be doing, and what the operating system is. Linux (at the operating system kernel level) supports four interfaces to a HID device - keyboard, mouse, joystick and a generic interface, known as the event interface.
* * *
#####  12.17.9.3.1.2. HID Mouse Configuration
In the kernel configuration stage, you need to turn on USB Human Interface Device (HID) support and Mouse Support Do not turn on USB HIDBP Mouse support. Perform the normal kernel rebuild and installation steps. If you are installing as modules, you need to load the `input.o`, `hid.o` and `mousedev.o` modules.
Plug in a USB mouse and check that your mouse has been correctly sensed by the kernel. If you don't have a kernel message, look for the changes to `/proc/bus/usb/devices`.
Since USB supports multiple identical devices, you can have multiple mice plugged in. You can get each mouse separately, or you can get them all mixed together. You almost always want the mixed version, and that is what will be used together. You need to set up a device node entry for the mixed mice. It is customary to create the entries for this device in the /dev/input/ directory.
Use the following commands:
```
mkdir /dev/input
mknod /dev/input/mice c 13 63

```

---
![Tip](https://tldp.org/LDP/Mobile-Guide/images/tip.gif) |  If you are unsure whether you are configuring the right mouse device, use **cat /dev/input/mice** (or other appropriate devices names). In case you do this for the correct mouse, you should see some bizarre looking characters as you move the mouse or click any of the buttons.
---|---
If you want to use the mouse under X, you have various options. Which one you select is dependent on what version of XFree86 you are using and whether you are using only USB for your mouse (or mice), or whether you want to use a USB mouse and some other kind of pointer device.
You need to edit the `XF86Config` file (usually `/usr/X11R6/lib/X11/XF86Config` or `/etc/X11/XF86Config`).
If you are using XFree86 version 4.0 or later, add an InputDevice section that looks like the following:
```
Section "InputDevice"
     Identifier  "USB Mice"
     Driver      "mouse"
     Option      "Protocol"   "IMPS/2"
     Option      "Device"     "/dev/input/mice"
EndSection

```

---
or, if you want to use a wheel mouse, something like this may be more useful: ```
Section "InputDevice"
     Identifier  "USB Mice"
     Driver      "mouse"
     Option      "Protocol"   "IMPS/2"
     Option      "Device"     "/dev/input/mice"
     Option      "ZAxisMapping"   "4 5"
     Option      "Buttons"        "5"
EndSection

```

---
Consult the
You also need to add an entry to each applicable ServerLayout Section. These are normally at the end of the configuration file. If you only have a USB mouse (or USB mice), then replace the line with the "CorePointer" entry with the following line:
```
InputDevice "USB Mice" "CorePointer"

```

---
If you want to use both a USB mouse (or USB mice) and some other kind of pointer device, then add (do not replace) the following line to the applicable ServerLayout sections:
```
InputDevice "USB Mice" "SendCoreEvents"

```

---
If you are using only a USB mouse (or USB mice) with XFree86 3.3, edit the Pointer section so that it looks like the following:
```
Section "Pointer"
    Protocol    "IMPS/2"
    Device      "/dev/input/mice"
EndSection

```

---
If you are trying to use a USB mouse (or USB mice) in addition to another pointer type device with XFree86 3.3, then you need to use the XInput extensions. Keep the existing Pointer (or modify it as required for the other device if you are doing an initial installation), and add the following entry (anywhere sensible, ideally in the Input devices area):
```
Section "Xinput"
   SubSection "Mouse"
  DeviceName   "USB Mice"
  Protocol     "IMPS/2"
  Port         "/dev/input/mice"
  AlwaysCore
   EndSubSection
EndSection

```

---
Restart the X server. If you don't have any mouse support at this point, remember that Ctrl-Alt-F1 will get you a virtual terminal that you can use to kill the X server and start debugging from the error messages.
If you want to use the mouse under gpm, run (or kill and restart if it is already running) gpm with the following options. **gpm -m /dev/input/mice -t imps2** (as superuser). You can make this the default if you edit the initialisation files. These are typically named something like rc.d and are in `/etc/rc.d/` on RedHat distributions.
If you have both a USB mouse (or USB mice) and some other kind of pointer device, you may wish to use gpm in repeater mode. If you have a PS/2 mouse on /dev/psaux and a USB mouse (or USB mice) on /dev/input/mice, then the following **gpm** command would probably be appropriate: **gpm -m /dev/input/mice -t imps2 -M -m /dev/psaux -t ps2 -R imps2**. Note that this will make the output appear on `/dev/gpmdata`, which is a FIFO and does not need to be created in advance. You can use this as the mouse "device" to non-X programs, and both mice will work together.
**Table 12-1. Arguments for the**-t** and **-R** option of **gpm**.**
option | description
---|---
ms | MicroSoft compatible serial mouse
ps2 | PS/2 or C&T 82C710
bm | Logitech bus mouse
bm | ATI XL bus mouse
mb | MicroSoft bus mouse
msc | Mouse Systems serial mouse
logi | older mouse
mman | Mouse Man protocol, serial Logitech mouse
sun | SUN mouse, three button
ms3 | Intellimouse with wheel, at serial port
imps2 | Intellimouse with wheel, at PS/2 port
pnp | PnP mice, alternative to **ms**
mm | MM series
bare | oldest serial two button mouse
* * *
###  12.17.9.4. Wrist Input Device - Twiddler
The **gpm** contains a driver for the Twiddler device at the serial port. For information about the Twiddler see
* * *
##  12.17.10. Macintosh PowerBooks
PowerBooks have a trackpad and only one button, although you can plug in external multi-button USB mice. The usual thing is to map a couple of keys on the keyboard to the middle and right mouse buttons; your Linux distribution should come with instructions on how to configure this (it's not specific to laptops, as all Apple mice are single-button).
If you are using the **Xpmac** server, the default is option-1 and option-2, and you can change this by passing **-middlekey <keycode>** **-rightkey <keycode>** arguments to **Xpmac** , and **-nooptionmouse** if you don't want the option key to be needed.
If you are using XFree86, you pass **adb_buttons= <middlekey>**,**< rightkey>** kernel arguments (no option is required). I use **adb_buttons=58,55** to map the option and Apple/command keys (which are little-used in Linux); use e.g. **xev** to find out the keycode for a given key.
* * *
#  12.18. Advanced Power Management - APM
##  12.18.1. Linux Compatibility Check
Start by reading the [Battery-Powered-mini-HOWTO](http://tldp.org/HOWTO/Battery-Powered/index.html).
For APM to work the machine's firmware must implement the APM Specification. Linux supports versions 1.0 through 1.2 of the standard. To work with Linux the APM BIOS must support 32-bit protected mode connections.
To display information about the APM BIOS on your system you can run **dmesg | grep apm** command or look in the `/proc/apm` file.
* * *
##  12.18.2. Introduction
APM support consists of two parts: _kernel_ support and _user-land_ support.
* * *
###  12.18.2.1. Kernel Support
You need a kernel that has the APM driver compiled in using the appropriate kernel configuration options. Currently most distributions do not ship kernels with the APM driver enabled so you may have to enable the driver using a boot option or to compile a custom kernel. Please see [Kernel-HOWTO](http://tldp.org/HOWTO/Kernel-HOWTO/) or your distribution manual for details.
The APM driver can be modularized but this is not recommended since many drivers will disable their APM features if the APM driver is not present when they initialize themselves.
The available APM options are (please see `Documentation/Configure.help` in the kernel source tree for more details):
  * **CONFIG_APM_IGNORE_USER_SUSPEND** Just a workaround for some NEC Versa M series laptops.
  * **CONFIG_APM_DO_ENABLE** Enable APM features at boot time.
  * **CONFIG_APM_CPU_IDLE** Puts CPU in power save mode, if there is nothing to do for the kernel.
  * **CONFIG_APM_DISPLAY_BLANK** Some laptops can use this to turn off the LCD backlight when the screen blanker of the Linux virtual console blanks the screen. Note that this is only used by the virtual console screen blanker, and won't turn off the backlight when using the X Window system.
  * **CONFIG_APM_POWER_OFF** Turns the machine completely down, when using **halt**. This feature works with most laptops without problems.
  * **CONFIG_APM_IGNORE_MULTIPLE_SUSPEND** Just a workaround for IBM™ ThinkPad 560.
  * **CONFIG_APM_IGNORE_SUSPEND_BOUNCE** Just a workaround for Dell Inspiron 3200 and other notebooks.
  * **CONFIG_APM_RTC_IS_GMT** Stores time in Greenwich Mean Time format. It is in fact recommended to store GMT in your real time clock (RTC) in the BIOS.
  * **CONFIG_APM_ALLOW_INTS** Resolves some problems with _Suspend to Disk_ for some laptops, for instance many newer IBM™ ThinkPads.
  * **CONFIG_SMP** Symmetric Multi-Processing support. This enables support for systems with more than one CPU. If you have a system with only one CPU, like most personal computers, say N. Though the default seems to be Y. So it may be enabled if you are unaware. I have got reports that SMP support enabled does interfere with APM. So with a single CPU machine like a laptop you are on the save side, when you N.


Features of the APM driver according to the Kernel documentation file `Documentation/Configure.help`: "The system time will be reset after a USER RESUME operation, the `/proc/apm` device will provide battery status information, and user-space programs will receive notification of APM _events_ (e.g., battery status change). "
* * *
###  12.18.2.2. Userland Support
The most important _userland_ utility is APM events.
If you run a 2.2.x or later kernel and want to experiment, Gabor Kuti <seasons_AT_falcon.sch.bme.hu> has made a kernel patch that allows you to _hibernate_ any Linux system to disk, even if your computers APM BIOS doesn't support it directly. In my humble opinion you don't need this features if your laptop provides a function key to invoke suspend mode directly.
Please see the [Battery Powered Linux Mini-HOWTO](http://tldp.org/HOWTO/Battery-Powered/) for detailed information.
Here's what **apmd** can do:
  * apmd(8): logs the battery status to syslog every now and then and runs a proxy script that can take action before suspend or after resume
  * apm(1): prints the current battery status or suspends the computer
  * apmsleep(1): suspends the machine for a limited time
  * xapm(1x): provides a battery meter for X11
  * libapm.a: a library for writing APM applications


Some APM firmware fails to restore mixer settings properly which can result in squeals of feedback in the music after the machine has resumed. A solution is to set up the proxy script so that it calls a mixer application after resume.
From the apmsleep(1) man page: Some computers, especially laptops, can wake up from a low-power suspend to DRAM mode using the Real-time clock (RTC) chip. Apmsleep can be used to set the alarm time in the RTC and to go into suspend or standby mode. An interrupt from the RTC causes the computer to wake-up. The program detects this event, by waiting for a leap in the kernel time and terminates successfully. If no time leap occurs within one minute, or something goes wrong, the exit value will be non-zero. Apmsleep is part of the **apmd** package.
In 2001 Richard Gooch wrote a simple **apmd** alternative which is available in the
Also, take a look at **apmcd** (**apm** based crontab) at
* * *
##  12.18.3. Caveats
If you use another operating system at the same computer make sure that its "suspend" and "hibernate" features don't write to partitions that are used by Linux.
* * *
##  12.18.4. Troubleshooting
If your machine worked with 2.0.x kernels but not with the 2.2.x series, take this advice from Klaus Franken kfr_AT_klaus.franken.de : "The default changed in 2.2. Search in the init-scripts for **halt** and change it to **halt -p** or **poweroff**. See **man halt** , if you don't have this option you need a newer version of **halt**." You may find it in the **SysVinit** package.
On some new machines (for instance HP Omnibook 4150 - 366 MHz model) when accessing `/proc/apm`, you may get a kernel fault **general protection fault: f000**. APM BIOS attempting to use a real mode segment while in protected mode, i.e. it is a bug in your BIOS. .. We have seen a few of these recently, except all the others are in the power off code in the BIOS where we can work around it by returning to real mode before attempting to power off. Here we cannot do this."
According to Kernel docs `Documentation/Configure.help`: "Some other things you should try when experiencing seemingly random, _weird_ problems:
  1. make sure that you have enough swap space and that it is enabled **swapon -s**.
  2. pass the **no-hlt** option to the kernel.
  3. switch on floating point emulation in the kernel and pass the **no387** option to the kernel.
  4. pass the **floppy=nodma** option to the kernel.
  5. pass the **mem=4M** option to the kernel (thereby disabling all but the first 4 MB of RAM).
  6. make sure that the CPU is not over clocked (doesn't seem suitable for mobile machines).
  7. read the
  8. disable the cache from your BIOS settings.
  9. install a fan for the video card or exchange video RAM (doesn't seem suitable for mobile machines).
  10. install a better fan for the CPU (doesn't seem suitable for mobile machines).
  11. exchange RAM chips (doesn't seem suitable for mobile machines).
  12. exchange the motherboard (doesn't seem suitable for mobile machines).


* * *
##  12.18.5. APM and PCMCIA
From the APM (Advanced Power Management) if you've configured your kernel with APM support. ... The PCMCIA modules will automatically be configured for APM if a compatible version is detected on your system. Whether or not APM is configured, you can use **cardctl suspend** before suspending your laptop, and **cardctl resume** after resuming, to cleanly shut down and restart your PCMCIA cards. This will not work with a modem that is in use, because the serial driver isn't able to save and restore the modem operating parameters. APM seems to be unstable on some systems. If you experience trouble with APM and PCMCIA on your system, try to narrow down the problem to one package or the other before reporting a bug. Some drivers, notably the PCMCIA SCSI drivers, cannot recover from a suspend/resume cycle. When using a PCMCIA SCSI card, always use **cardctl eject** prior to suspending the system.".
* * *
##  12.18.6. APM and Resuming X Windows
Some machines have APM firmware that fails to save and restore display controller chip registers across a suspend. Earlier versions of the XFree86 X server did not restore the screen properly after resume, a problem which was addressed by
Sometimes X and APM don't work smoothly together. The machine might even hang. A recommendation from Steve Rader: Some linux systems have their X11 server hang when doing **apm -s**. Folks with this affliction might want to switch to the console virtual terminal and then suspend **chvt 1; apm -s** as root, or, more appropriately **sudo chvt 1; sudo apm -s**. I have these commands in a script, say, **my-suspend** and then do **xapmload --click-command my-suspend** .
* * *
##  12.18.7. Software Suspend
**swsusp** or **shutdown -z** (patch for **sysvinit** needed). It creates an image which is saved in your active swaps. By the next booting the kernel detects the saved image, restores the memory from it and then it continues to run as before you've suspended. If you don't want the previous state to continue use the **noresume** kernel option.
Software suspends may even be better than hibernate, because now I can suspend my Linux system, boot into Microsoft Windows, perform a few illegal operations and be shut down, and then restart my Linux setup exactly where I left off! This is something that cannot be done with hibernation, since that always restores the last state that you suspended from, be it Microsoft Windows or Linux. So if I want to switch to Microsoft Windows to play games or do anything else, I can leave my Linux desktop exactly as it is and return to how I left it.
In recent 2.6 kernels SoftWareSuspend is part of the kernel. You may find it in the section Power Management. But there are also backports to 2.4 available.
Since the original Software Suspend code was written by Gabor Kuti and Pavel Machek back in 1998, three different implementations have been created for the 2.6 kernel, all forks of the same original codebase.
* * *
##  12.18.8. Tips and Tricks
###  12.18.8.1. Battery Status on Text Console
You may use the following entry in `.bashrc` to show the battery level on the command prompt.
* * *
####  12.18.8.1.1. When Using APM
```
export PS1="\$(cat /proc/apm | awk '{print \$7}') \h:\w\$ "

```

---
* * *
####  12.18.8.1.2. When Using ACPI
```
# Color the bash prompt in function of the percentage of battery
# with acpi subsystem.
# Based on the originally apm based script that has been posted
# on debian-laptop by
# Jason Kraftcheck <kraftche at cae.wisc.edu>.
#
# This script is licensed under the GNU GPL version 2 or later,
# see /usr/share/common-licences/GPL on a Debian system or
# http://www.gnu.org/copyleft/gpl.html on the web.

# (c) 2003 Fabio 'farnis' Sirna <farnis at libero dot it>

function acpi_percent()
{
 if [ `cat /proc/acpi/battery/BAT0/state | grep present: |cut -d\  -f18` = "yes" ]; then
  {
   CAPACITY=`cat /proc/acpi/battery/BAT0/info |grep "design capacity:"|cut -d\  -f11`
   LEVEL=`cat /proc/acpi/battery/BAT0/state | grep remaining|cut -d\  -f8`
   ACPI_PERCENT=`echo $(( $LEVEL * 100 / $CAPACITY ))`
   if [ "$LEVEL" = "$CAPACITY" ]; then
    echo FULL
   else
    echo $ACPI_PERCENT%
   fi
  }
 else echo "NO BATTERY"
 fi
}

function acpi_charge()
{
 ACPI_CHARGE=`cat /proc/acpi/ac_adapter/AC/state | cut -d\  -f20`
 case $ACPI_CHARGE in
       *on-line*)
         ACPI_CHARGE="+" ;;
       *off-line*)
         ACPI_CHARGE="-" ;;
     esac
     echo $ACPI_CHARGE
}

function acpi_color()
   {
     if  [  "$(acpi_charge)"  =  "+"  ];  then
      {
       if [ `cat /proc/acpi/battery/BAT0/state | grep present: |cut -d\  -f18` = "no" ]; then
        echo  "0;31"
       else echo  "1;32"
      fi
     }
     else
       case  $(acpi_percent)  in
          10?%)  echo  "0;32"  ;;
           9?%)  echo  "0;32"  ;;
           8?%)  echo  "0;32"  ;;
           7?%)  echo  "0;32"  ;;
           6?%)  echo  "0;32"  ;;
           5?%)  echo  "0;32"  ;;
           4?%)  echo  "0;33"  ;;
           3?%)  echo  "0;33"  ;;
           2?%)  echo  "0;33"  ;;
           1?%)  echo  "0;31"  ;;
            ?%)  echo  "0;31;5"  ;;
             *)  echo  "0;35"  ;;

       esac
     fi
   }

function  acpi_color_prompt
   {
     PS1='\[\e[$(acpi_color)m\][$(acpi_charge)$(acpi_percent)][\t] \u:\w\$>\[\e[0;37m\] '
   }

   #  linux  console
   if  [  "$TERM"  =  "linux"  ];  then
     PROMPT_COMMAND=acpi_color_prompt
   fi

   function  echo_acpi
   {
     echo -n "($(acpi_charge)$(acpi_percent)) "
   }

```

---
* * *
###  12.18.8.2. Debian GNU/Linux
All "normal" Debian GNU/Linux kernels are APM capable, they just need an append line added to the boot loader configuration file (e.g. `/etc/lilo.conf`.
```
append="apm=on"

```

---
You might use the following parameters (with the appropriate changes) in your boot loader configuration file (e.g. `/etc/lilo.conf` to experiment with ACPI and APM, when compiled in the same kernel. Usage of APM and ACPI at the same time doesn't work, see Kernel docs for details.
```
append="acpi=off apm=on"

```

---
* * *
#  12.19. ACPI
##  12.19.1. Related Documentation
  1. ACPI driver for Linux and its associated applications.
  2. [Section 12.3](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s1-cpu) the CPU chapter of this guide


* * *
##  12.19.2. ACPI Details
ACPI stands for _Advanced Configuration and Power Interface_. This is a specification by Toshiba, Intel and Microsoft. Besides many other things it also defines power management. This is why it is often compared to APM.
You might use the following parameters (with the appropriate changes) in your boot loader configuration file (e.g. `/etc/lilo.conf` to experiment with ACPI and APM, when compiled in the same kernel. Usage of APM and ACPI at the same time doesn't work, see Kernel docs for details.
```
append="acpi=on apm=off"

```

---
The
The
**apm** command, that provides information on battery status, AC power, and thermal readings.
* * *
#  12.20. Power Management Unit - PMU (PowerBook)
PowerBooks don't support the APM specification, but they have a separate protocol for their PMU (Power Management Unit). There is a free (GPL) daemon called **pmud** that handles power management; it can monitor the battery level, put the machine to sleep, and set different levels of power consumption. It was written by Stephan Leemburg. There is also an older utility called **snooze** available from the same sites that just puts the PowerBook to sleep. **pmud**.
Cron works fine on my laptop as I never shut it off completely. I only put it to sleep. When it wakes up, the unexecuted **cron** jobs from the sleep period all run.
This part is a courtesy of Steven G. Johnson.
* * *
#  12.21. Batteries
| _May the batteries be with you._
---|---
| _Unknown AuthorEss_
For information about available battery types, take a look at the Hardware Features chapter above.
Please see the [Battery Powered Linux Mini-HOWTO](http://tldp.org/HOWTO/Battery-Powered/) and the
From the **mobile-update** page (modified by WH): Discharge the battery. If your battery runs only for about 20 minutes, you probably suffer from memory effects. Most laptops do not discharge the battery properly. With low powered devices like old computer fans they can be discharged completely. This removes memory effects. You should do so even with LiIon batteries, though they don't suffer much from memory effect (the manual of an IBM™ Thinkpad says to cycle the batteries through a full charge/discharge cycle 3 times every few months or so).
![Warning](https://tldp.org/LDP/Mobile-Guide/images/warning.gif) |  Try this at your own risk! Make sure the voltage of the fans is compatible to your battery. It works for me.
---|---
In the US, this company has most batteries for anything and can rebuild many that are no longer manufactured: Batteries Plus, 2045 Pleasant Hill Road, Duluth, GA 30096 +1 770 495 1644.
The
_rclock_ program to include a simple battery power meter on the clock face.
* * *
##  12.21.1. Smart Battery Support
The
* * *
##  12.21.2. How to Improve Battery Uptime
These are the most important factors which have influence on the battery uptime. Please see the appropriate chapters for power saving tips:
  * [Section 12.3](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s1-cpu) CPU
  * fan
  * [Section 12.22](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s12-memory) memory
  * [Section 12.6](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s4-graphic-chip)graphics card
  * [Section 12.33](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s23-harddisk) hard disk drive
  * [Section 12.32](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s21-cd-drive) optical drive


Getting your computer to use the least amount of power can be problematic. Intel's
* * *
#  12.22. Memory
Unfortunately some laptops come with proprietary memory chips. So they are not interchangeable between different models. But this seems changing. With some models it's very difficult to install the memory if you have to open the case in detail. But this is also changing. Places were the memory can be changed easily are dedicated maintenance cover on the backside or often if you only have to remove the keyboard.
* * *
#  12.23. Plug-and-Play Devices (PnP)
The _Plug and Play driver project_ for Linux is a project to create support within the Linux kernel (see
_ISA PnP tools_ is another useful package.
The latest PCMCIA driver package (>3.1.0) has utilities **lspnp** and **setpnp** to manipulate PNP settings.
* * *
#  12.24. Docking Station / Port Replicator
##  12.24.1. Definitions
First some definitions. There is a difference between _docking station_ and _port replicator_.
I use the term _docking station_ for a box which contains slots to put some interface cards in, and space to put a harddisk, etc. in. This box can be permanently connected to a PC. A _port replicator_ is just a copy of the laptop ports which may be connected permanently to a PC.
* * *
##  12.24.2. Other Solutions
I don't use a docking station myself. They seem really expensive and I can't see any usefulness. Alright you have to deal with some more cables, but is it worth so much money? Docking stations are useful in an office environment when you have a permanent network connection, or need the docking station's expansion bus slots (e.g. for some excotic SCSI device).
Also all docking stations I know are proprietary models, so if you change your laptop you have to change this device, too. I just found one exception a docking station which connects to your laptop via IrDA® the IRDocking IR-660 by IrDA®, though I couldn't check it out.
I would prefer to buy a PC instead and connect it via _network_ to the laptop.
Or use an external display, which usually works well as described above, and an external keyboard and mouse. If your laptop supports an extra PS/2 port you may use a cheap solution a _Y-cable_ , which connects the PS/2 port to an external keyboard and an external monitor. Note: Your laptop probably has support for the _Y-cable_ feature, e.g. the COMPAQ Armada 1592DT.
* * *
##  12.24.3. Docking Station Connection Methods
AFAIK there are _four solutions_ to connect a laptop to a docking station:
  1. SCSI port (very seldom)
  2. parallel port
  3. (proprietary) docking port (common)
  4. USB (often offered by third party manufacturers)


From Martin J. Evans "The main problem with docking stations is getting the operating system to detect you are docked. Fortunately, you can examine the devices available in `/proc` and thus detect a docked state. With this in mind a few simple scripts is all you need to get your machine configured correctly in a docked state.
You may want to build support for the docking station hardware as modules instead of putting it directly into the kernel. This will save space in your kernel but your choice probably largely depends on how often you are docked.
1) Supporting _additional disks_ on the docking station SCSI card
To my mind the best way of doing this is to:
  1. Either build support for the SCSI card into the kernel or build it as a module.
  2. Put the mount points into `/etc/fstab` but use the "noauto" flag to prevent them from being mounted automatically with the **mount -a** flag. In this way, when you are docked you can explicitly mount the partitions off any disk connected to the docking station SCSI card.


2) Supporting _additional network adaptors_ in the docking station
You can use a similar method to that outlined above for the graphics card. Check the `/proc` filesystem in your rc scripts to see if you are docked and then set up your network connections appropriately. "
Once you determine this information, you may use a script, similar to the following example, to configure the connection to your docking station at startup. The script is provided by Friedhelm Kueck:
```
# check, if laptop is in docking-station (4 PCMCIA slots available)
# or if it is standalone (2 slots available)
# Start after cardmgr has started
#
# Friedhelm Kueck mailto:fk_AT_impress.de
# 08-Sep-1998
#
# Find No. of Sockets
SOCKETS=`tail -1 /var/run/stab | cut -d ":" -f 1`
case "$SOCKETS" in
"Socket 3")
echo Laptop is in Dockingstation ...
echo Disabling internal LCD Display for X11
echo
cp /etc/XF86Config_extern /etc/XF86Config
#
# Setup of PCMCIA Network Interface after start of cardmgr
#
echo
echo "Setting up eth0 for use at Network ..."
echo
/sbin/ifconfig eth0 10.1.9.5 netmask 255.255.0.0 broadcast 10.1.255.255
/sbin/route add -net 10.1.0.0 gw 10.1.9.5
/sbin/route add default gw 10.1.10.1
;;

"Socket 1")
echo Laptop is standalone
echo Disabling external Monitor for X11
cp /etc/XF86Config_intern /etc/XF86Config
echo
echo Network device NOT setup
;;
esac

```

---
* * *
##  12.24.4. Universal USB Port Replicators
I have used a Typhoon USB 2.0 7in1 Docking Station made by
How does its different ports work with Linux:
  * USB 2.0 A-type downstream: works with external hard disk and mouse out of the box
  * USB 2.0 A-type downstream: see above
  * PS/2 keyboard: works out of the box
  * PS/2 mouse: works, but for 2.6 Kernels you have to specify the right mouse protocol **psmouse_proto=imps** (if psmouse is compiled as a module).
  * serial port: tested with serial mouse, doesn't seem to work, **/dev/ttyUSB0** was assigned
  * parallel port: tested, device **/dev/usb/usblp0** assigned, works e.g. with HP LaserJet 2100
  * LAN: usbnet loads, device eth1 was assigned, **ifconfig** or **pump** configures the network device
  * transfer port aka host link: works with usbnet module, use **ifconfig usb0** to configure the network interface, (USB 1.1 host link B-type) untested


Here is the output of **dmesg** for the Typhoon port replicator:
```
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
drivers/usb/class/usblp.c: usblp0: USB Bidirectional printer dev 30 if 0 alt 1 proto 2 vid 0x067B pid 0x2305
hub 1-1.3:1.0: new USB device on port 3, assigned address 31
pl2303 1-1.3.3:1.0: PL-2303 converter detected
usb 1-1.3.3: PL-2303 converter now attached to ttyUSB0 (or usb/tts/0 for devfs)
hub 1-1.3:1.0: new USB device on port 4, assigned address 32
HID device not claimed by input or hiddev
hid: probe of 1-1.3.4:1.0 failed with error -5
input: Composite USB PS2 Converter USB to PS2 Adaptor  v1.09 on usb-0000:00:07.2-1.3.4
HID device not claimed by input or hiddev
hid: probe of 1-1.3.4:1.1 failed with error -5
input: Composite USB PS2 Converter USB to PS2 Adaptor  v1.09 on usb-0000:00:07.2-1.3.4

```

---
* * *
#  12.25. Network Connections
##  12.25.1. Related Documentation
  1. [PLIP-mini-HOWTO](http://tldp.org/HOWTO/PLIP.html)
  2. [Networking-HOWTO](http://tldp.org/HOWTO/NET3-4-HOWTO.html)
  3. [Ethernet-HOWTO](http://tldp.org/HOWTO/Ethernet-HOWTO.html)


* * *
##  12.25.2. Connection Methods
Almost all recent laptops are equipped with a built-in network card. This chapter shows some methods to connect older laptops without internal network cards.
* * *
###  12.25.2.1. PCMCIA Network Card
If your laptop supports PCMCIA this is the easiest and fastest way to get network support. Make sure your card is supported before buying one.
* * *
###  12.25.2.2. Serial Null Modem Cable
Probably the cheapest way to connect your laptop to another computer, but quite slow. You may use PPP or SLIP to start the connection.
* * *
###  12.25.2.3. Parallel Port NIC (Pocket Adaptor)
PCMCIA slots.
* * *
###  12.25.2.4. Parallel "Null" Modem Cable
Offers more speed than a serial connection. Some laptops use chipsets that will not work with PLIP. Please see [PLIP-HOWTO](http://tldp.org/HOWTO/PLIP.html) for details.
* * *
###  12.25.2.5. Docking Station NIC
I don't have experience with a NIC in a docking station yet.
* * *
##  12.25.3. Wake-On-LAN
Wake-On-LAN works with some laptops equipped with built-in network cards. **ethtool** to configure some special Wake-On-LAN settings.
* * *
#  12.26. Built-In Modem
##  12.26.1. Modem Types
There are three kinds of modems available: internal, PCMCIA card or external serial port modems. But some internal modems will not work with Linux these modems are usually called WinModem. This is caused by non-standard hardware. So you have to use either a PCMCIA card modem or an external modem (serial or USB). The
Quotation from the Kernel-FAQ: "9.Why aren't WinModems supported? (REG, quoting Edward S. Marshall) The problem is the lack of specifications for this hardware. Most companies producing so-called _WinModems_ refuse to provide specifications which would allow non-Microsoft operating systems to use them. The basic issue is that they don't work like a traditional modem; they don't have a DSP, and make the CPU do all the work. Hence, you can't talk to them like a traditional modem, and you -need- to run the modem driver as a realtime task, or you'll have serious data loss issues under any kind of load. They're simply a poor design."
"_Win_ modems are lobotomized modems which expect Windows to do some of their thinking for them. If you do not have Windows, you do not have a connection. "
Anyway, I have set up a page collecting information on laptops with internal modems at **wine** or **VMware** , but I don't know it.
The
There is a driver for Lucent WinModems available. LucentPCI (binary only) driver, for PCI driven internal modems, see
* * *
##  12.26.2. Caveats
![Warning](https://tldp.org/LDP/Mobile-Guide/images/warning.gif) |  Pay attention to the different kinds of phone lines: analog and ISDN. You can't connect an analog modem to an ISDN port and vice versa. Though there might be hybrid modems available. Connecting to the wrong port may even destroy your modem. Trick: If you are looking for an analog phone port in an office building which is usually wired with ISDN, take a look at the fax lines, they are often analog lines.
---|---
![Warning](https://tldp.org/LDP/Mobile-Guide/images/warning.gif) |  If your machine features an internal modem as well as an internal ethernet card, pay also attention to plug the right cable into the plug. Otherwise you may damage your hardware easily. It may even cause a fire.
---|---
For tracking the packets on PPP you may use **pppstats**. Or **pload** this provides a graphical view of the traffic (in and out) of the PPP connection. It is based on athena widgets hence is very portable. It also uses very little CPU time.
* * *
#  12.27. GPRS
GPRS is a General Packet Radio Service, an add-on to GSM and TDMA cellular telephone standards used all over the world. It allows (almost) always-on Internet connections using GSM (or TDMA) telephones. It makes mobile internet usage on laptops fairly inexpensive. The
* * *
#  12.28. SCSI
##  12.28.1. Linux Compatibility Check
If unsure about the right SCSI support, compile a kernel with all available SCSI drivers as modules. Load each module step by step until you get the right one.
* * *
##  12.28.2. Related Documentation
  1. [SCSI-2.4-HOWTO](http://tldp.org/HOWTO/SCSI-2.4-HOWTO/index.html)


* * *
##  12.28.3. Survey
There is no current x86 laptop yet with a SCSI harddisk. Though there have been two models with a built in SCSI port: Texas Instruments TI 4000 and HP OmniBook 800. Maybe the PowerBook G3 has a SCSI disk, but I didn't check this yet. The old Apple Powerbook Duo models had a SCSI hard disk.
For other models, if you need SCSI support you may get it by using a SCSI-PCMCIA card or via a SCSI adapter in a docking station.
* * *
#  12.29. Universal Serial Bus - USB
##  12.29.1. Linux Compatibility Check
You should get information about the USB controller with **cat /proc/pci** and about USB devices with **cat /proc/bus/usb/devices**.
* * *
##  12.29.2. Miscellaneous
Newer laptops come equipped with the Universal Serial Bus - USB. The following USB devices are available, not all of them are fully supported by Linux yet: keyboard, mouse, printer, tablet, camera, cpia, webcam, MP3 player, modem, wireless LAN, audio, jukebox, scanner, storage (hard drive, memory stick), floppydrive, ZIP, Super Disk - LS 120, compact flash reader, CD, BlueTooth, ethernet, serial, joystick, USB Host-to-Host Cable, hub .
Visit the USB at the
![Warning](https://tldp.org/LDP/Mobile-Guide/images/warning.gif) |  Please note, I have got a report that the power by a laptop via USB is not enough for some kind of devices, e.g. Web Cams or hard disks. But it seems to depend on the laptop and the specific device. With desktop Linux machines these USB devices work flawlessly, but with mobile devices not.
---|---
* * *
#  12.30. FireWire - IEEE1394 - i.Link
Firewire, also known as IEEE-1394 and iLink, is a high-speed serial bus system that was originally developed by Apple Computer. Currently, its widest implementation is for digital video; however, it has a lot of other uses. Like USB, Firewire is a serial protocol that supports hot-swapping. Firewire supports much higher speeds than USB. The
Also I have set up a page collecting information about laptops and FireWire at
* * *
#  12.31. Floppy Drive
##  12.31.1. Linux Compatibility Check
Usually there are no problems connecting a floppy drive to a Linux laptop. But with a laptop floppy drive you may sometimes not be able to use every feature. I encountered the **superformat** command (from the fdutils package) couldn't format more than 1.44MB with my HP OmniBook 800. You may also have difficulty when the floppy drive and CD drive are mutually exclusive, or when the floppy drive is a PCMCIA device (as with the Toshiba Libretto 100). With older laptops, there might be a minor problem if they use a 720K drive. As far as I know all distributions come with support for 1.44M (and sometimes 1.2M) floppies only. Though it's possible to install Linux anyway. Please see Installation chapter. Please see kernel documentation for boot time parameters concerning certain laptop floppy drives, for instance IBM™ ThinkPad. Or **man bootparam** .
* * *
#  12.32. Optical Drives (CD/DVD)
##  12.32.1. CD-ROM
###  12.32.1.1. Related Documentation
  * [CDROM-HOWTO](http://tldp.org/HOWTO/CDROM-HOWTO/)
  * [CD-Writing-HOWTO](http://tldp.org/HOWTO/CD-Writing-HOWTO.html)


* * *
###  12.32.1.2. Introduction
Most notebooks today come with CD drives. If floppy and CD drive are swappable they are usually mutually exclusive, however many vendors (HP, Dell) provide cables which allow the floppy module to be connected to the parallel port. Sometimes the CD drives comes as external PCMCIA device (e.g. SONY), or as SCSI device (e.g. HP OmniBook 800), USB device (e.g. SONY), or as Firewire (e.g. SONY VAIO VX71P). Such an external devices might bear problems to install Linux from it.
As far as I know there are SONY DiscMans available which have a port to connect them to a computer or even a SCSI port. I found an article published by Ziff-Davis Publishing Company (September 1996 issue, but missed to note the URL) written by Mitt Jones: "Portable PC Card CD-ROM drives transform laptops into mobile multimedia machines", which listed: Altec Lansing AMC2000 Portable Multimedia CD-ROM Center; Axonix ProMedia 6XR; CMS PlatinumPortable; EXP CDS420 Multimedia Kit; H45 QuickPCMCIA CD; Liberty 115CD; Panasonic KXL-D740; Sony PRD-250WN CD-ROM Discman.
To here music from internal CD drives usually works without problems. But note:
![Tip](https://tldp.org/LDP/Mobile-Guide/images/tip.gif) |  Some notebooks come with an external CD drive, you need an extra cable to connect the sound output of the drive to the sound input of the notebook.
---|---
* * *
##  12.32.2. CD-RW
Most notebooks today even come with internal or external CD writers. The internal usually work, see [CD-Writing-HOWTO](http://tldp.org/HOWTO/CD-Writing-HOWTO.html) for details. But with the different external (PCMCIA, Firewire, USB) drives you probably need some tweaking.
* * *
##  12.32.3. DVD Drive
DVD roms. It's meant to be a replacement for the ISO9660 filesystem used on today's CDROMs, but the immediate impact for most will be DVD. DVD multimedia cdroms use the UDF filesystem to contain MPEG audio and video streams. To access DVD cdroms you would need a DVD cdrom drive, the kernel driver for the cdrom drive, some kind of MPEG video support, and a UDF filesystem driver (like this one). Some DVD cdroms may contain both UDF filesystems and ISO9660 filesystems. In that case, you could get by without UDF support."
DVD formats:
```
Digital Versatile Disc
DVD-5  4.4GB 1side 1 coat ~ 2h video
DVD-9  8.5GB 1side 2 coat ~ 4h video
DVD-10 9.4GB 2side 1 coat ~ 4.5h video
DVD-18 17 GB 2side 2 coat ~ 8h video

```

---
* * *
#  12.33. Hard Disk
##  12.33.1. Linux Compatibility Check
Useful programs are **hdparm** , **dmesg** , **fsck** and **fdisk** .
* * *
##  12.33.2. Utilities
The
The
* * *
##  12.33.3. Solid-State-Disks - SSDs
Solid-State-Disks (SSDS) need some optimization of the Linux file system before installing the operating system. Here are some
* * *
##  12.33.4. Miscellaneous
Be careful when using your laptop abroad. I have heard about some destroyed harddisks due to a magnetic field emitted from the magnetic-holds at the backresttable of the seats in a German railway waggon.
Though I am quite satisfied with the quality of the hard disk in my laptop, when I removed it from the case I unintendedly dropped it. I recommend to be very careful.
* * *
##  12.33.5. Form Factors
AFAIK there are only two form factors for harddisks used in laptops. Since 2003 there is the 1.8" format. But much older and still the most common format is the 2.5" format. The 2.5" format seems to be available in different heights (Please note I couldn't verify this information yet):
  * 18mm: laptops built before 1996 usually have drives 18mm high
  * 12.7mm: I got a report about such disks but without a notebook model or manufacturer name
  * 11mm: since 1996 the drives are 11mm high
  * 9mm: many laptops, including the subnotebooks, now use a 9mm-high disk drive. The largest available in this format in late 1999 is IBM™ _12GN_.
  * 9.5mm: Toshiba Libretto L70 and L100 have a 9.5mm HD
  * 8.45mm: Toshiba Libretto 20, 30, 50 and 60 have 8.45mm tall HDs
  * 6.35mm: Toshiba Libretto L1000 has a 6.35mm HD


It might be possible to use a hard disk which doesn't fit with some case modifications.
Some laptops come with a removable hard disk in a tray, for instance the KAPOK 9600D. There seem to be no SCSI drives for laptops available.
* * *
##  12.33.6. Manufacturer Tools
Some hard disk manufacturers offer dedicated tools to change hard disk parameters. For example Hitachi offers
* * *
#  12.34. Hot-Swapping Devices (MultiBay, SelectBay, ..)
Some laptops (usually the more expensive ones) come with a free slot, which may bear a second hard disk or CD/DVD drive. Every manufacturer seems to name it differently, names like MultiBay(TM) and SelectBay(TM) are common. Different Linux tools are available to handle these hot-swapping devices.
thotswap is part of the
The hard disk management tool **hdparm** also comes with a hot swap option.
Some bays can (in some cases only) carry a second battery. Currently I don't know how Linux can handle this. For example are there any tools, which show battery stats for the second battery?
* * *
#  12.35. WireLess Network - WLAN
| _For this let us found a city/ And we will name it Mahagonny/ That means: Net City/ She shall be like a Net/ That is set out to catch edible birds./ Everywhere there is toil and labor/ But here there is amusement/ For it is the uninhibited lust of men/ Not to suffer and to be allowed all things/ That is the essence of gold_
---|---
| _Bertolt Brecht, 1929_
* * *
##  12.35.1. Related Documentation
* * *
##  12.35.2. Introduction
Many notebooks now come pre-equipped with wireless network support for the 802.11 protocol family. These devices are either based on **lspci** or **cardctl ident**. External WLAN adapters are available as PCMCIA or CF-Cards and as USB devices. Details will follow in a later issue.
* * *
#  12.36. BlueTooth
Some laptops come pre-equipped with built-in BlueTooth support, but I had no time to investigate that any further. Actually I do not have such a machine to test Linux on it yet.
* * *
#  12.37. Infrared Port
| _Better red, than dead._
---|---
| _Unknown AuthorEss_
* * *
##  12.37.1. Linux Compatibility Check
To get the IrDA® port of your laptop working with Linux/IrDA® you may use StandardInfraRed (SIR) or FastInfraRed (FIR).
* * *
###  12.37.1.1. SIR
Up to 115.200bps, the infrared port emulates a serial port like the 16550A UART. This will be detected by the kernel serial driver at boot time, or when you load the `serial` module. If infrared support is enabled in the BIOS, for most laptops you will get a kernel message like:
```
Serial driver version 4.25 with no serial options enabled
ttyS00 at 0x03f8 (irq = 4) is a 16550A     #first serial port /dev/ttyS0
ttyS01 at 0x3000 (irq = 10) is a 16550A    #e.g. infrared port
ttyS02 at 0x0300 (irq = 3) is a 16550A     #e.g. PCMCIA modem port

```

---
* * *
###  12.37.1.2. FIR
If you want to use up to 4Mbps, your machine has to be equipped with a certain FIR chip. You need a certain Linux/IrDA® driver to support this chip. Therefore you need exact information about the FIR chip. You may get this information in one of the following ways:
  1. Read the _specification_ of the machine, though it is very rare that you will find enough and reliable information to use with Linux there.
  2. Try to find out whether the FIR chip is a _PCI_ device. Do a **cat /proc/pci** . The appropriate files for 2.2.x kernels are in `/proc/bus/pci` . Though often the PCI information is incomplete. You may find the latest information about PCI devices and vendor numbers in the kernel documentation usually in `/usr/src/linux/Documentation` or at the page of **lspci** from the **pci-utils** package, too.
  3. Use the _DOS tool_ **CTPCI330.EXE** provided in ZIP format by the
  4. Try to get information about _Plug-and-Play (PnP)_ devices. Though I didn't use them for this purpose yet, the **isapnp** tools, could be useful.
  5. If you have installed the _Linux/ IrDA® software_ load the FIR modules and watch the output of **dmesg** , whether FIR is detected or not.
  6. Another way how to figure it out explained by Thomas Davis (modified by WH): "Dig through the FTP site of the vendor, find the _Windows9x FIR drivers_ , and they have (for a SMC chip):
```
-rw-rw-r--   1 ratbert  ratbert       743 Apr  3  1997 smcirlap.inf
-rw-rw-r--   1 ratbert  ratbert     17021 Mar 24  1997 smcirlap.vxd
-rw-rw-r--   1 ratbert  ratbert      1903 Jul 18  1997 smcser.inf
-rw-rw-r--   1 ratbert  ratbert     31350 Jun  7  1997 smcser.vxd

```

---
If in doubt, always look for the .inf/.vxd drivers for Windows95. Windows95 doesn't ship with _ANY_ FIR drivers. (they are all third party, mostly from Counterpoint, who was assimilated by ESI)."
  7. Also Thomas Davis found a package of small DOS **FINDCHIP.EXE**. And includes a **FIRSETUP.EXE** utility that is supposed to be able to set all values except the chip address. Furthermore it contains **BIOSDUMP.EXE** , which produces this output:
Example 1 (from a COMPAQ Armada 1592DT)
```
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

```

---
Result 1:
**Irq Tag, Mask (bit mapped - ) = 0x0010 = 0000 0000 0000 0001 0000** so, it's IRQ 4. (start at 0, count up ..), so this is a SIR only device, at IRQ=4, IO=x03e8.
Example 2 (from an unknown machine)
```
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

```

---
Result 2:
a) it's a SMC IrCC chip
b) one portion is at 0x02f8, has an io-extent of 8 bytes; irq = 3
c) another portion is at 0x02e8, io-extent of 8 bytes; dma = 1 (0x02 =0000 0010)
![Warning](https://tldp.org/LDP/Mobile-Guide/images/warning.gif) |  The package is not intended for the end user, and some of the utilities could be harmful. The only documentation in the package is in Microsoft Word format. Linux users may read this with
---|---
  8. Use the _Device Manager_ of the MicroSoft Windows9x/NT operating system.
  9. You may also use the _hardware surveys_ mentioned below.
  10. And as a last resort, you may even _open the laptop_ and look at the writings at the chipsets themselves.


* * *
###  12.37.1.3. Hardware Survey
I have made an IrDA hardware survey at
To make this list more valuable, it is necessary to collect more information about the infrared devices in different hardware. You can help by sending me a short e-mail containing the exact name of the hardware you have and which type of infrared controller is used.
Please let me know also how well Linux/IrDA® worked (at which tty, port and interrupt it works and the corresponding infrared device, e.g. printer, cellular phone).
Also you can help by contributing detailed technological information about some infrared devices, which is necessary for the development of drivers for Linux.
* * *
##  12.37.2. Related Documentation
* * *
##  12.37.3. IrDA® Configuration - Survey
###  12.37.3.1. IrDA®
The Linux infrared support is still experimental, but rapidly improving. I try to describe the installation in a short survey. Please read my
* * *
####  12.37.3.1.1. Kernel
  1. Get a 2.4.x kernel and the latest Linux/IrDA patches from the
  2. Compile it with all IrDA® options enabled.
  3. Also enable experimental, sysctl, serial and network support.


* * *
####  12.37.3.1.2. Software
  1. Get the Linux IrDA® software **irda-utils** at
  2. Untar the package.
  3. Do a **make depend; make all; make install**


* * *
####  12.37.3.1.3. Hardware
  1. Enable the IrDA® support in the BIOS.
  2. Check for SIR or FIR support, as described above.
  3. Start the Linux/IrDA® service with **irattach DEVICE -s 1** .
  4. Watch the kernel output with **dmesg** .


* * *
###  12.37.3.2. Linux Infrared Remote Control - LIRC
* * *
#  12.38. FingerPrint Reader
UPEK, provider of popular fingerprint sensors to IBM's T42 notebooks and others, has announced that they will be providing a BioAPI compliant library to perform biometric authentication under Linux. There is also a proposed
* * *
#  Chapter 13. Accessories: PCMCIA, USB and Other External Extensions
#  13.1. PCMCIA Cards
##  13.1.1. Card Families
  1. Ethernet adapter
  2. Token Ring adapter
  3. Ethernet + Modem / GSM
  4. Fax-Modem / GSM adapter
  5. SCSI adapter
  6. I/O cards: RS232, LPT, RS422, RS485, GamePort, IrDA®, Radio, Video
  7. Memory cards
  8. harddisks
  9. 2.5" harddisk adapters


For desktops there are PCMCIA slots for ISA and PCI bus available.
* * *
##  13.1.2. Linux Compatibility Check
With the command **cardctl ident** you may get information about your card. If your card is not mentioned in `/etc/pcmcia/config`, create a file `/etc/pcmcia/<MYCARD>.conf` appropriately. Take an entry in the first file as a model. You may try every driver, just in case it might work, for instance the **pcnet_cs** supports many NE2000 compatible PCMCIA network cards. Note: it is a bad practice to edit `/etc/pcmcia/config` directly, because all changes will be lost with the next update. After creating `/etc/pcmcia/<MYCARD>.conf` restart the PCMCIA services. This may not be enough to get the card to work, but works sometimes for no-name network cards or modem cards. If you get a card to work or have written a new driver please don't forget to announce this to
Since not all cards are mentioned there, I have set up a
* * *
#  13.2. ExpressCards
ExpressCard is the official standard for modular expansion for desktop and mobile systems based on PCI-Express. These cards offer a smaller and faster PC Card solution. Here is the
* * *
#  13.3. SmartCards
SmartCard reader, see Project Muscle -
* * *
#  13.4. SDIO Cards
Looking for
* * *
#  13.5. Memory Technology Devices - RAM and Flash Cards
PCMCIA code, to prevent duplication of code and effort, yet its main target is small embedded systems, so it will be possible to compile the drivers into the kernel for use as a root filesystem, and a close eye will be kept on the memory footprint.
* * *
#  13.6. Memory Stick
The Memory Stick is a proprietary memory device, in the beginning only used in devices made by SONY. But now they are available in mobile computers made by other manufacturers, too. The current sticks are USB devices and work with all recent kernels. After loading the `usb-storage` you may mount them as SCSI devices, often as `/dev/sda` or `/dev/sdb`. For older laptops see the appropriate pages at Linux-on-Laptops.
There is also a SONY Memory Stick Floppy Adapter - MSAC-FD2M. I don't know whether this works with Linux.
* * *
#  13.7. Card Readers for SD/MMC/Memory Stick
##  13.7.1. External Readers
All external SD/MMC/CF-Card/Memory Stick readers are USB devices and work fine with the **usb-storage** module. The only caveat which might occur is that you may have difficulties to determine the device assignment. Just use **dmesg** after you have connected the reader. The command should show a SCSI device like `/dev/sda1` assigned to the USB drive.
* * *
##  13.7.2. Internal Readers
Currently there are three kinds of devices available: USB, PCMCIA and PCI devices.
USB devices are seldom, but usually work out of the box. They behave like the external readers mentioned above.
Some readers are PCMCIA/CardBus devices. Often such a reader is located near the CardBus slot. The command **cardctl ident** will reveal these cards.
For some laptops and notebooks a
Some proprietary devices are not yet known to work with Linux. Except the readers built into the SHARP Linux PDAs, but the driver is closed source and available as a binary only for the ARM CPU.
* * *
#  13.8. USB Devices
For more info about this and other Linux-compatible USB devices see the
* * *
##  13.8.1. Ethernet Devices
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

Any Pegasus II based board also are supported. If you have devices with vendor IDs other than noted above you should add them in the driver code and send a message to <petkan_AT_dce.bg> for update.
* * *
##  13.8.2. BlueTooth Dongles
There are many dongles around. I have made some experience with the
* * *
##  13.8.3. Port Replicators/Docking Stations
I do not have experience with these devices yet. But I expect that it will be difficult, if not impossible, to get them to run with Linux. For other kinds of port replicators and docking stations see the appropriate section in the laptop chapter.
* * *
#  13.9. Printers and Scanners
##  13.9.1. Survey of Mobile Printers and Scanners
For a survey of ports and protocol to print via a mobile or stationary printer see the Different Environments chapter below.
  1. IrDA®. By properly I mean as a pseudo-PostScript device by way of **ghostscript** and a modified **lpd**.
How:
     * linux-2.2.7-ac2-irda6
     * **/proc/sys/net/irda/slot_timeout** increased to 10 (essential or discovery fails)
     * **ghostscript** DEVICE set to bjc600
     * `printcap` includes:
```
:xc#01777777:\
:fc#017:\
:fs#020000010002:

```

---
     * and **lpd** had to be modified to accept the ulong _fs_ and to handle _xc_ (which is documented but not coded in the lpd's I have looked at). "
For further information look at his page
Tim Auckland wrote: Would my version of **lpd** help? **unixlpr** is a portable version of the lpr/lpd suite, compatible with traditional versions and **:ms=** field (also seen in SunOS 4) and the ability to print directly to TCP connected printers without needing special filters. **ms** allows you to configure the tty using stty arguments directly, so if stty can handle the extended flags, my **lpd** should handle IrDA® _out of the box_. You can find the latest **unixlpr**
  2. HP: DeskJet 340Cbi. This is a small, portable, low-duty-cycle printer. It prints either black, or color (3 color). I have had some problems with it loading paper. Overall, the small size and portability make it a nice unit for use with laptops. I use the HP 500/500C driver with Linux.
  3. Olivetti: JP-90
  4. PCMCIA port.


AFAIK only the HP DeskJet 340Cbi and the BJC-80 machine have an infrared port. Pay attention to the supplied voltage of the power supply if you plan to travel abroad. I couldn't check the scan functionalities with Linux yet.
* * *
##  13.9.2. Scanner and OCR Software
_Scanner Access Now Easy_ and is an application programming interface (API) that provides standardized access to any raster image scanner hardware (flatbed scanner, hand-held scanner, video- and still-cameras, frame-grabbers, etc.). The SANE standard is free and its discussion and development is open to everybody. The current source code is written for UNIX (including Linux) and is available under the GNU public license (commercial application and backends are welcome, too, however).
For scanner drivers see
* * *
##  13.9.3. Connectivity
There are different ways to connect a printer or scanner to a laptop. For printers usually: parallel port, serial port, USB and IrDA® port. For scanners usually: parallel port, SCSI (via PCMCIA or generic SCSI port), USB and PCMCIA port. All of them need the appropriate kernel drivers.
* * *
#  13.10. Serial Devices
##  13.10.1. Keyspan PDA Serial Adapter
Single port DB-9 serial adapter, pushed as a PDA adapter for iMacs (mostly sold in Macintosh catalogs, comes in a translucent white/green dongle). Fairly simple device.
* * *
#  13.11. External Storage Devices
##  13.11.1. External Hard Disks
There are external hard disk cases with different connectors available: PCMCIA, USB and FireWire. Cases are available for 2.5" (laptop hard disks), 3.5" (desktop hard disks) and 5.25" (CD-Writer). All of them work very well together with Linux. Especially I like the cases for 2.5" hard disks, you may upgrade your current laptop hard disk and use the old one to put it into the external box to extend your hard disk space.
Caveat: After wake up from suspend mode, the external hard drive can't work. To cure this problem these remedies might help: Disconnect the external drive and then plug it in again. Or use an AC adapter to power the external drive. Though this seems inconvenient in a suspend situation. But since the external drive gets the power from the adapter, there is no disconnection from power as will be if power is provided from USB.
Caveat: Take care that the jumpers are set to Master. Almost all external hard disk cases will not work when the jumpers are set to Slave or Cable Select.
* * *
#  13.12. Power and Phone Plugs, Power Supply
When travelling abroad you might consider to take a set of different power and phone plugs with you. Also, it's useful if you can change the input voltage of the power supply, for instance from 110V in the US to 220V in Germany. There also power supplies for 12V batteries from cars.
Some models of power plugs:
```
                ____                                  _
               / () \     _   _       _       _     _(_)_
frontal view: |()  ()|   (_)=(_)     (_)     (_)   (_) (_)
               ------

abbreviation.:    C13       C8         ??     PS/2    C5

symbol......:    ??        ??        -O)-    N.N.    N.N.

```

---
![Warning](https://tldp.org/LDP/Mobile-Guide/images/warning.gif) |  Though some -O)- shaped plug may seem to be compatible with your laptop, because of the appropriate physical size, take extreme care it uses the same plus-minus voltage scheme, for instance plus for the inner ring and minus for the outer one. Often, but not always, there are the appropriate symbols near the plug.
---|---
More about laptop and PDA power supplies at
* * *
#  13.13. Bags and Suitcases
You probably wonder, why I include this topic here. But shortly after using my COMPAQ Armada 1592DT I recognized that the rear side of the machine (where the ports are arranged) was slightly damaged. Though I have taken much care when transporting the laptop, this was caused by putting the bag on the floor. It seems that the laptop has so much weight, that it bounces inside the bag on its own rear side. So I decided to put a soft pad into the bag before loading the laptop. A good bag is highly recommended if you take your laptop on trips, or take it home every night.
Laptops computers are frequently demolished in their carrying bag. The two main causes of demolition are poking the LC display and banging the edges. A good case has very stiff sides to spread out pokes, and lots of energy-absorbent padding around the edges to help when you whack it on the door jamb. Few cases actually have either of these features.
More laptops are lost to theft than damage, so camouflage is a wise too. Emerson, Tom # El Monte <TOMEMERSON_AT_ms.globalpay.com> wrote: "I use for a laptop _travelling bag_ : a Pyrex _casserole carrier_ bag. Yup, you might think it _odd_ to use a casserole bag for a laptop, but it turns out it has several advantages:
  * The one I use has a microwavable heating pad in it - while I don't actually heat this pad (it's meant to keep food warm while in transport), it does provide padding underneath the laptop. The carrier I have only has a lower - heating - pad, but there is also a similar carrier that has both a lower - heating - pad and an upper - cooling - pad - placed in the freezer to get it cold - -- the intent is that you keep one or the other in the bag to keep your food hot or cold as desired. A secondary advantage to the - cooling pad - pad is that if you've - chilled - it before taking the computer out for the day, it will keep the CPU cooler while you're running the laptop...
  * the top of the bag has a zipper on three sides, so it - opens - the same way as my laptop - I don't even need to take it out of the carrier to use the laptop
  * there is enough room at the side of the bag to store the external power supply, a regular Logitech mouseman, and the network - dongle - with BNC/TP ports - and if I had it, the modem/phone port as well -
  * there is enough clearance on top of the machine to include a handful of CD's or diskettes, if needed.
  * when it's left - unattended - in a car, it's less likely to be stolen - think about it, if you were a thief walking through a parking lot and eyeing the contents of cars, a - laptop bag - is instantly recognizable as holding a laptop computer - something that can be fenced at a pretty hefty profit, but if you saw a casserole carrier in the front seat of a car, would you think it contained anything OTHER than a casserole? - and probably half-eaten, at that... - Unless you are a hungry thief, chances are you'll skip this and move on.
  * likewise, I've heard that keeping a laptop computer in a diaper bag is another good - camouflage - technique - who in their right mind is going to steal a bag of - dirty - diapers?"


# VI. Kernel

**Table of Contents**


14. [Kernel History](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1-kernel-history)


14.1. [Kernel 2.4](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s1-kernel-2-4)


14.2. [Kernel 2.6](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p2c1s1-kernel-2-6)


14.3. [Kernel Configuration for Laptops](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a12-kernel-configuration)

* * *
#  Chapter 14. Kernel History
The kernel chapter isn't ready yet. Just some notes about important changes with kernel 2.4 and 2.6 related to mobile computers. As well as some notes about Kernel configurations for laptops.
* * *
#  14.1. Kernel 2.4
##  14.1.1. PCMCIA
From " PCMCIA (Personal Computer Memory Card International Association) is an international standards body and trade association with over 200 member companies that was founded in 1989 to establish standards for Integrated Circuit cards and to promote interchangeability among mobile computers where ruggedness, low power, and small size were critical. As the needs of mobile computer users have changed, so has the PC Card Standard. By 1991, PCMCIA had defined an I/O interface for the same 68 pin connector initially used for memory cards. At the same time, the Socket Services Specification was added and was soon followed by the Card Services Specification as developers realized that common software would be needed to enhance compatibility. " The cards are available in different formats: Type I, II, III.
A quotation from the `../Documentation/Changes` file: "PCMCIA (PC Card) support is now partially implemented in the main kernel source. Pay attention when you recompile your kernel. If you need to use the **PCMCIA-CS** modules, then don't compile the kernel's PCMCIA support. If you don't need to use the PCMCIA-CS modules (i.e. all the drivers you need are in the kernel sources), then don't compile them; you won't need anything in there. Also, be sure to upgrade to the latest **PCMCIA-CS** release." Further information you may get from the README-2.4 included with this package.
You may find an example kernel configuration for laptops in the [Section 14.3](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a12-kernel-configuration).
* * *
##  14.1.2. Powermanagement
At the moment there are two power management drivers in the linux kernel (AFAIK). They each have different userspace interfaces `/proc/apm/` and `/dev/apmctl/` and `/proc/acpi/` or something.
For further information see the page of **powermanager**.
With kernel 2.4 there is ACPI available, see ACPI chapter below.
The SuSE
* * *
##  14.1.3. Hotplug
There is a new
Kernel Support for Hot-Plugable Devices
```
CONFIG_HOTPLUG
  Say Y here if you want to plug devices into your computer while
  the system is running, and be able to use them quickly. In many
  cases, the devices can likewise be unplugged at any time too.

  One well known example of this is PCMCIA- or PC-cards, credit-card
  size devices such as network cards, modems or hard drives which are
  plugged into slots found on all modern laptop computers. Another
  example, used on modern desktops as well as laptops, is USB.

  Enable HOTPLUG and KMOD, and build a modular kernel. Get
  **/sbin/hotplug**) to
  load modules and set up software needed to use devices as
  you hotplug them.

```

---
* * *
#  14.2. Kernel 2.6
##  14.2.1. PCMCIA
* * *
#  14.3. Kernel Configuration for Laptops
You may find an example for 2.4.x kernels _Don't_ use this file by default, please use always **make config** , **make menuconfig** or **make xconfig** to create a kernel configuration file. See [Kernel-HOWTO](http://tldp.org/HOWTO/Kernel-HOWTO/) (from TLDP) for details. Thomas Hertweck has written another useful
# VII. On the Road

**Table of Contents**


15. [Different Environments](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1-different-environments)


15.1. [Related Documentation](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1s1-related-howtos)


15.2. [Configuration Tools](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1s2-configuration-tools)


15.3. [E-Mail](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1s3-e-mail)


15.4. [Data Transport Between Different Machines (Synchronization)](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1s3-data-transport)


15.5. [Backup](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1s4-backups)


15.6. [Connections to Servers](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1s4-connections-to-servers)


15.7. [Security in Different Environments](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1s5-security-in-different-environments)


15.8. [Theft Protection](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1s6-theft-protection)


15.9. [Dealing with Down Times (Cron Jobs)](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1s7-dealing-with-down-times)


15.10. [Mobile Printing](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1s8-mobile-printing)


15.11. [Noise Reduction](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c1s8-noise-reduction)


16. [Solutions with Mobile Computers](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2-solutions-with-laptops)


16.1. [Introduction](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s1-introduction)


16.2. [Mobile Network Analyzer](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s2-mobile-network-analyzer)


16.3. [Mobile Router](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s3-mobile-router)


16.4. [Hacking and Cracking Networks](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s4-hacking-and-cracking-networks)


16.5. [Mobile Data Collection](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s5-mobile-data-collection)


16.6. [Mobile Office](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s6-mobile-office)


16.7. [Connection to Digital Camera](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s7-digital-camera)


16.8. [Connection to QuickCam (Video)](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s8-quickcam)


16.9. [Connection to Television Set](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s9-television-set)


16.10. [Connection to Cellular Phone](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s10-cellular-phone)


16.11. [Connection to Global Positioning System (GPS)](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s11-gps)


16.12. [Connection via Amateur Radio (HAM)](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s12-ham)


16.13. [Satellite Watching](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s13-satellite-watching)


16.14. [Aviation](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s14-aviation)


16.15. [Blind or Visually Impaired Users](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p5c2s15-blind-or-visually-impaired-users)

* * *
#  Chapter 15. Different Environments
| _Tell me and I might forget. Show me and I can remember. Involve me and I will understand._
---|---
| _Confucius, 450 B.C._
* * *
#  15.1. Related Documentation
  1. [Security-HOWTO](http://tldp.org/HOWTO/Security-HOWTO/index.html)
  2. [Multiboot-with-LILO-HOWTO](http://tldp.org/HOWTO/Multiboot-with-LILO.html)
  3. [Ethernet-HOWTO](http://tldp.org/HOWTO/Ethernet-HOWTO.html)
  4. [Networking-HOWTO](http://tldp.org/HOWTO/NET3-4-HOWTO.html)
  5. [Offline-Mailing-mini-HOWTO](http://tldp.org/HOWTO/Offline-Mailing.html)
  6. [Plip-HOWTO](http://tldp.org/HOWTO/PLIP.html)
  7. [Slip-PPP-Emulator-HOWTO](http://tldp.org/HOWTO/SLIP-PPP-Emulator/)


If you are using Debian GNU/Linux then you should refer to the Debian Reference chapter entitled "Network configuration". Debian contains a number of packages that help to make roaming among different networks effortless.
* * *
#  15.2. Configuration Tools
##  15.2.1. NetEnv
Do you use your laptop in different network environments? At home? In the office? At a customers site?
If yes, the small package "netenv" might be useful for you. When booting your laptop it provides you with a simple interface from which you can choose the current network environment. The first time in a new environment, you can enter the basic data and save it for later reuse.
Netenv sets up a file containing variable assignments which describe the current environment. This can be used by the PCMCIA setup scheme, e.g. like the one that comes with Debian/GNU Linux and perhaps others.
The netenv data can be used for things like:
  1. Network Device: Configure the network device for different environments.
  2. Choose a proper `XF86Config`: Think of using your laptop standalone with touchpad vs. connected to a CRT monitor along with an external mouse. For example, a wheel mouse could be used when docked, but the driver is not compatible with the normal trackpoint or touchpad.
  3. Windowmanager: You can set up your windowmanager appropriate to the current location of your machine.
  4. Printing Environment: The netenv data can easily be used to set up the printing environment.


Netenv is available at **dialog(1)** for its menu interface. Netenv was developed by Gerd Bavendiek.
* * *
##  15.2.2. System Configuration Profile Management - SCPM
SuSE's
* * *
##  15.2.3. ifplugd
* * *
##  15.2.4. divine
  * you describe the possible networks in /etc/divine.conf, including one or more machines that are probably up (routers and NIS servers come to mind).
  * at boot time, you run divine.
  * **divine** starts a thread that injects fake arp requests into the network. The thread will try again up to three times, pausing 1 second between retries. If the last try times out again, the thread will print an error message, leave the interface in the original state and exit cleanly.
  * the main thread just looks for arp replies and exits if one is found.
  * You have one `resolv.conf` per network, for example `/etc/resolv.conf.default` and `/etc/resolv.conf.work`. **divine** will symlink one of them to `/etc/resolv.conf` for you.
  * You can specify a proxy server plus port and divine will write the proxy server to `/etc/proxy`. This can be evaluated inside your shell startup script, like this (**zsh**):
```
export http_proxy="http://`</etc/proxy`/"

```

---
The included perl script edit-netscape-proxy.pl will edit the proxy settings in your Netscape 4 preferences file.
  * You can even specify an additional script to be run for each selection. You can use this to edit `/etc/printcap` or `/etc/issue` or do something else I forgot.


The point about **divine** in contrast to other solutions is that other solutions normally use **ping** or something like that. **divine** can check a large number of networks instantaneously, assuming that the machines you ping answer within one second (.4 seconds are normal on Ethernets). And pinging an unknown address will do an arp request anyway, so why not do an arp request in the first place?"
* * *
##  15.2.5. Mobile IP
From the [Networking-HOWTO](http://tldp.org/HOWTO/NET3-4-HOWTO.html) : "The term _IP Mobility_ describes the ability of a host that is able to move its network connection from one point on the Internet to another without changing its IP address or losing connectivity. Usually when an IP host changes its point of connectivity it must also change its IP address. IP Mobility overcomes this problem by allocating a fixed IP address to the mobile host and using IP encapsulation (tunneling) with automatic routing to ensure that datagrams destined for it are routed to the actual IP address it is currently using."
See also
* * *
###  15.2.5.1. Resources
Sources: Kenneth E. Harker and Dag Brattli
* * *
##  15.2.6. DHCP/BootP
DHCP and BootP are also useful for working in different environments. Please see the [DHCP-HOWTO](http://tldp.org/HOWTO/DHCP/index.html) .
* * *
##  15.2.7. PPPD Options
The **pppd** command can be configured via several different files: **pppd file /etc/ppp/ <your_options>** .
* * *
##  15.2.8. /etc/init.d
You may even choose to do your configuration by editing the `/etc/init.d` files manually.
* * *
##  15.2.9. PCMCIA - Schemes
How can I have separate PCMCIA device setups for home and work? This is fairly easy using PCMCIA _scheme_ support. Use two configuration schemes, called **home** and **work**. For details please read the appropriate chapter in the
* * *
##  15.2.10. Bootloaders
###  15.2.10.1. LILO
From Martin J. Evans I have taken this recommendation: The first point to note is that **init** will take any arguments of the form **name=value** as environment variable assignments if they are not recognized as something else. This means you can set environment variables from the LILO boot prompt before your rc scripts run. I set the **LOCATION** environment variable depending on where I am when I boot Linux. e.g.
```
LILO: linux LOCATION=home

```

---
Or ```
LILO: linux LOCATION=work

```

---
Or simply ```
LILO: linux

```

---
where failing to set **LOCATION** means the same as **LOCATION=home** (i.e. my default). Instead of typing **LOCATION=place** each time you boot you can add an entry to your `/etc/lilo.conf` file and use the append instruction. e.g. ```
# Linux bootable partition for booting Linux at home
#
image = /vmlinuz
root = /dev/hda3
label = linux
read-only
# Linux bootable partition config ends
#
# Linux bootable partition for booting Linux at work
#
image = /vmlinuz
root = /dev/hda3
label = work
read-only
append="LOCATION=work"
# Linux bootable partition config ends

```

---
With the example above you can use "linux" for booting at home and "work" for booting at work.
Armed with the facility above, you can now edit the relevant rc scripts to test ENVIRONMENT before running **ifconfig** , setting up **route** etc.
* * *
###  15.2.10.2. Other Bootloaders
There are several other bootloaders which are often overlooked. Besides LILO, have a look at loadlin, CHooseOS (CHOS) (not GPL), GRand Unified Bootloader (GRUB), System Commander and take a look at
* * *
##  15.2.11. X-Windows
From Steve <steve_AT_cygnet.co.uk> I got a configuration for X Windows with an external monitor: Note that I have introduced a neat trick! For my nice 17" monitor I start X11 with no options and get the default 16-bit 1152x864 display - but when using the LCD screen I specify a 15-bit display (**startx -- -bpp 15**) and get the correct 800x600 resolution automatically. This saves having to have two X11 config files.
* * *
##  15.2.12. More Info
* * *
#  15.3. E-Mail
##  15.3.1. Introduction
A short introduction about how to setup email on a laptop used at home (dial-up) and work (ethernet) by Peter Englmaier <ppe_AT_pa.uky.edu>:
* * *
###  15.3.1.1. Features
As a laptop user, I have special demands for my email setup. The setup described below, enables me to:
  * Read my email from _home_ using a POP email server, which is supplied by my university, but could also be setup on a _work_ place computer.
  * Write email from home with the _right_ return address in the email (which does not mention my computer name).
  * Read/write my email while working on a workstation without access to my laptop or the POP email server (as a backup).
  * Read my email while working on my laptop connected to the ethernet of our institut.
  * Direct email while connected via ethernet (faster than the fetchmail method).
  * Indirect email (over pop mail server) while not connected to the ethernet at work (either at home via modem or somewhere else via ethernet).
  * Use any emailer, e.g. **elm** or the simple **mail** command.
  * Sort incoming email, delete spam, split email-collections (digests) into separate emails


The configuration is based on **sendmail** , **fetchmail** , and a _remote pop account_ for email.
* * *
###  15.3.1.2. Configuration of sendmail
This is the most complicated part. Having installed the **sendmail-cf** package, I created a file named `/usr/lib/sendmail-cf/laptop.mc`:
```
divert(-1)
include(`../m4/cf.m4')
define(`confDEF_USER_ID',''8:12'')
define(`confBIND_OPTS',`-DNSRCH -DEFNAMES')

# here you define your domain
define(`confDOMAIN_NAME',''pa.uky.edu'')
OSTYPE(`linux')
undefine(`UUCP_RELAY')
undefine(`BITNET_RELAY')

# there we send outgoing email
define(`SMART_HOST',`server1.pa.uky.edu')

# there we send mail to users my laptop does not know
define(`LUSER_RELAY',`server1.pa.uky.edu')

# again the domain, we want to be seen as
MASQUERADE_AS(pa.uky.edu)
FEATURE(allmasquerade)
FEATURE(nouucp)
FEATURE(nodns)
FEATURE(nocanonify)
FEATURE(redirect)
FEATURE(always_add_domain)
FEATURE(use_cw_file)
FEATURE(local_procmail)
MAILER(procmail)
MAILER(smtp)
HACK(check_mail3,`hash -a@JUNK /etc/mail/deny')
HACK(use_ip,`/etc/mail/ip_allow')
HACK(use_names,`/etc/mail/name_allow')
HACK(use_relayto,`/etc/mail/relay_allow')
HACK(check_rcpt4)
HACK(check_relay3)

```

---
This looks more complicated as it is. All it does is, that it redirectes outbound mail to server1 (SMART_HOST) and also mail for local users which are not known (LUSER_RELAY). That way, I can write email to my colleques without using their full email address. More important: the From line in my email points back to my MASQUARADE_AS domain and not directly to my laptop. If this where not the case, email returned with the _reply_ button might not reach me. You must restart **sendmail** for changes to take effect. Note: this configuration is for Redhat 5.2 systems. You may have to change some details.
Now, all what is needed is to generate the `/etc/sendmail.cf `file **m4 laptop.mc >/etc/sendmail.cf** and to add all possible domain names my laptop should respond to in `/etc/sendmail.cw`:
```
# sendmail.cw - include all aliases for your machine here.
laptop
laptop.pa.uky.edu
128.17.18.30
guest1
guest1.somewhere.org

```

---
It is important to have all aliases in this file, otherwise **sendmail** will not accept the mail (and will reply _we don't relay_ to the sender). Finally, you must now test the setup by sending email, replying to mail for all possible configurations. Any misconfiguration can result in loss of email.
* * *
###  15.3.1.3. Configuration for fetchmail on Laptop
One method to get the email into your machine is through **fetchmail**. Fetchmail periodically checks for new email at one or more remote mail servers. I use the following fetchmail configuration file (in my user home directory): `fetchmailrc`
```
set postmaster "myusername"
set daemon 900
poll pop.uky.edu with proto POP3
user "mypopusername" there with password "mypoppassword" is mylaptopusername here

```

---
Fetchmail will just get the email and send it to **sendmail** which will it deliver into your `/var/spool/mail/$USER` file.
* * *
###  15.3.1.4. Forward E-Mail to the Laptop
On my work station I have the following `.forward` file:
```
me@pop.account.edu,me@server1

```

---
Here server1 is the machine where I keep my mailbox. All email is send to the pop account to be picked up later by my laptop (using **fetchmail**). However, when my laptop is connected via ethernet, I want my email to go directly to the laptop, instead of pop:
```
me@laptop,me@server1

```

---
In both cases, a backup of my email is send to server1 (where I also can read it, in case I cannot get my laptop). I keep/store all email on the laptop.
Switching is done by three script files and a crontab file (on the workstation):
`forward_pop`
```
#!/bin/sh
echo "me@pop.account.edu,me@server1" > ${HOME}/.forward

```

---
`forward_laptop`
```
#!/bin/sh
echo "ppe@laptop,ppe@server1" > ${HOME}/.forward
crontab ${HOME}/mycrontab
${HOME}/utl/check_laptop

```

---
`check_laptop`
```
#!/bin/sh
if /usr/sbin/ping -c 1 laptop  >/dev/null 2>&1 ; then
   :
else
   # redirect mail to pop
   ${HOME}/utl/forward_pop
   sleep 10
if /usr/sbin/ping -c 1 laptop  >/dev/null 2>&1 ; then
      # back to normal
      ${HOME}/utl/forward_laptop
else
# deactivate crontab check
/bin/crontab -l | grep -v check_laptop >${HOME}/tmp/mycrontab.tmp
      /bin/crontab ${HOME}/tmp/mycrontab.tmp
      rm -f ${HOME}/tmp/mycrontab.tmp
fi
fi

```

---
`mycrontab`
```
# mycrontab
0,10,20,30,40,50 * * * * ${HOME}/utl/check_laptop

```

---
Each time I connect the laptop to the ethernet, I have to run **forward_laptop** , and each time I disconnect I run forward_pop. In case I forget to run **forward_pop** , the crontab job runs it for me less then 10 minutes later. To do all that automatically, I change the network script files on my laptop as follows:
`/sbin/ifdown` (this script runs, whenever a network device is stopped, new stuff between BEGIN and END)
```
...
fi
# BEGIN new stuff
# turn off forwarding email
mail ppe <<EOF
turning off forwarding email
device = ${DEVICE}
hostname = `hostname`
EOF
if [ "${DEVICE}" = "eth0" -a "`hostname`"
= "laptop" ]; then
su -lc "ssh -l myusername server1
utl/forward_pop" myusername >& /dev/null
fi
# END new stuff

ifconfig ${DEVICE} down
exec /etc/sysconfig/network-scripts/ifdown-post $CONFIG

```

---
Note, that the script checks for the value of hostname. In case, I am connected to a foreign ethernet, my hostname and ip-address will be something else, e.g. guest1.
`/etc/sysconfig/network-scripts/ifup-post` (this script is run, whenever a network device is started)
```
# Notify programs that have requested notification
do_netreport
# BEGIN new stuff
# check for email -- I'm using fetchmail for this
if [ "${DEVICE}" = "eth0" -o "${DEVICE}"
= "ppp0" ]; then
su -lc fetchmail myusername >& /dev/null &
fi
# set clock if connected to ethernet, redirect email
if [ "${DEVICE}" = "eth0" -a "`hostname`" = "zaphod" ]; then
( rdate -s server1 ; hwclock --systohc --utc ) >& /dev/null &
# forward email
su -lc "ssh -l myusername gradj utl/forward_laptop" myusername >& /dev/null &
fi
# END new stuff

exit 0

```

---
* * *
###  15.3.1.5. Processing Incoming E-Mail with procmail
This step is completely optional. The above described sendmail configuration calls **procmail** for each received email, but you could have called **procmail** using the **.forward** file (see the procmail man page). Procmail is a handy tool to block spam and to sort incoming email.
You need to setup a **.procmailrc** file to use **procmail**. See the man page for procmail, procmailrc, and procmailex (examples). My setup demonstrates, how to ignore certain email messages and split email-collections (digest) into pieces:
```
# -- mail filtering -- procmail is called by sendmail --
PATH=/bin:/usr/bin
MAILDIR=$HOME/Mail
LOGFILE=$MAILDIR/from
# keep in mind:
# use ":0:" when writing to a file
# use ":0"  when writing to a device, e.g. /dev/null, or send email

# - make a backup of *all* incoming mail, but ignore mail tagged below -
:0 c:
*! ^Sissa-Repro
backup

# - keep only last 50 messages
:0 ic
| cd backup && rm -f dummy `ls -t msg.* | sed -e 1,50d`

# - delete email coming through the 'postdocs' email list, when
# it is not of any interest
:0
* ^From.*postdocs
* ^From.*Ernst Richter /dev/null :0
* ^From.*postdocs
* ^Subject.*card charge
/dev/null
# Split mailing list from the sissa preprint server into individual emails
# - this is quite complicated :(   I can flip through the list much
#   faster and ignore preprints which have uninteresting titles. Instead of
#   having to browse through the whole list, my mailer will just present a
#   list of papers.
# 1. split it in individual messages
:0
* ^From no-reply@xxx.lanl.gov
| formail +1 -de -A "Sissa-Repro: true" -s procmail
# 2. reformat messages a bit
# 2.1. extract 'Title:' from email-Body and add to email-header
as 'Subject:'
:0 b
* ^Sissa-Repro
*! ^Subject
TITLE=| formail -xTitle:
:0 a
|formail -A "Subject: $TITLE " -s procmail

# 2.2. store in my incoming sissa-email folder. Here, we could
#      also reject (and thereafter delete) uninteresting 'Subjects'
#      we could also mark more interesting subjects as urgend or send a copy
#      to regular mail box.
:0:
* ^Sissa-Repro
* ^Subject
*! ^replaced with
sissa

```

---
By the way, there is a **tk** GUI tool to configure **procmail** (I think it is called **dotfiles**).
* * *
##  15.3.2. Email with UUCP
Another possible solution for Email is to use UUCP. This software was made for disconnected machines, and is by far the easiest solution if you have several users on your laptop (we are talking about UNIX, remember?), each with his/her own account.
Unlike what most people think, UUCP does not need a serial connection: it works fine over TCP/IP, so your UUCP partner can be any machine on the Internet, if it is reachable from your network attachment point. Here is the UUCP `sys` for a typical laptop:
```
system mylaptop
time any
chat "" \d\d\r\c ogin: \d\L word: \P
address uucp.mypartner.org
port TCP

```

---
* * *
##  15.3.3. MailSync
* * *
#  15.4. Data Transport Between Different Machines (Synchronization)
I don't have experience with this topic yet. So just a survey about some means of data transport and maintaining data consistency between different machines.
* * *
##  15.4.1. Useful Hardware
  1. external harddisks
  2. ZIP drive


Wade Hampton wrote: "You may use MS-DOS formatted ZIP and floppy discs for data transfer. You may be able to also use LS120. If you have SCSI, you could use JAZ, MO or possibly DVD-RAM (any SCSI disc that you could write to). I have the internal ZIP for my Toshiba 700CT. It works great (I use **automount** to mount it). I use VFAT on the ZIP disks so I can move them to Windows boxes, Linux boxes, NT, give them to coworkers, etc. One problem, I must SHUTDOWN to swap the internal CD with the ZIP."
* * *
##  15.4.2. Useful Software
###  15.4.2.1. Version Management Software
Although it is certainly not their main aim, version management software like CVS (Concurrent Version System) are a perfect tool when you work on several machines and you have trouble keeping them in sync (something which is often called "disconnected filesystems" in the computer science literature). Unlike programs like **rsync** , which are asymmetric (one side is the master and its files override those of the slave), CVS accept that you make changes on several machines, and try afterwards to merge them. Asymmetric tools are good only when you can respect a strict discipline, when you switch from one machine to another. On the contrary, tools like CVS are more forgetful.
To synchronize two or more machines (typically a desktop and a laptop), just choose a CVS repository somewhere on the network. It can be on one of the machines you want to synchronize or on a third host. Anyway, this machine should be easily reachable via the network and have good disks.
Then, **cvs co** the module you want to work on, edit it, and **cvs commit** when you reached a synch point and are connected. If you made changes on both hosts, CVS will try to merge them (it typically succeeds automatically) or give in and ask you to resolve it by hand.
The typical limits of this solution: CVS does not deal well with binary files, so this solution is more for users of vi or emacs than for GIMP fans. CVS has trouble with some UNIX goodies like symbolic links.
For more information on CVS, see the
* * *
###  15.4.2.2. CODA Filesystem
The UNIX file name-space that is mapped on to a collection of dedicated file servers. But Coda represents a substantial improvement over AFS because it offers considerably higher availability in the face of server and network failures. The improvement in availability is achieved using the complementary techniques of server replication and disconnected operation. Disconnected operation proven especially valuable in supporting portable computers .
* * *
###  15.4.2.3. unison
**unison** shares a number of features with tools such as configuration management packages (**CVS** , **PRCS** , etc.) distributed filesystems ( _uni-directional_ mirroring utilities (**rsync** , etc.) and other synchronizers ( Intellisync, Reconcile, etc). However, there are a number of points where it differs:
  * **unison** runs on both MicroSoft-Windows (95, 98, NT, and 2k) and Unix (Solaris, Linux, etc.) systems ( for ARM based Linux PDAs see the **unison** works _across_ platforms, allowing you to synchronize a Microsoft-Windows laptop with a Unix server, for example.
  * Unlike a distributed filesystem, **unison** is a user-level program: there is no need to hack (or own!) the kernel, or to have superuser privileges on either host.
  * Unlike simple mirroring or backup utilities, **unison** can deal with updates to both replicas of a distributed directory structure. Updates that do not conflict are propagated automatically. Conflicting updates are detected and displayed.
  * **unison** works between any pair of machines connected to the internet, communicating over either a direct socket link or tunneling over an **rsh** or an encrypted **ssh** connection. It is careful with network bandwidth, and runs well over slow links such as PPP connections.
  * **unison** has a clear and precise specification.
  * **unison** is resilient to failure. It is careful to leave the replicas and its own private structures in a sensible state at all times, even in case of abnormal termination or communication failures.
  * **unison** is free; full source code is available under the GNU Public License.


* * *
###  15.4.2.4. OpenSync, MultiSync
* * *
###  15.4.2.5. Funambol
* * *
###  15.4.2.6. Tsync
* * *
###  15.4.2.7. InterMezzo
* * *
###  15.4.2.8. WWWsync
* * *
###  15.4.2.9. rsync
**rsync** is a program that allows files to be copied to and from remote machines in much the same way as **rcp**. It has many more options than **rcp** , and uses the _rsync remote-update protocol_ to greatly speedup file transfers when the destination file already exists. The _rsync remote-update protocol_ allows **rsync** to transfer just the differences between two sets of files across the network link.
* * *
###  15.4.2.10. Xfiles - file tree synchronization and cross-validation
Xfiles is an interactive utility for comparing and merging one file tree with another over a network. It supports freeform work on several machines (no need to keep track of what files are changed on which machine). Xfiles can also be used as a cross-validating disk <-> disk backup strategy (portions of a disk may go bad at any time, with no simple indication of which files were affected. Cross-validate against a second disk before backup to make sure you aren't backing up bad data).
A client/server program (GUI on the client) traverses a file tree and reports any files that are missing on the server machine, missing on the client machine, or different. For each such file, the file size/sizes and modification date(s) are shown, and a comparison (using UNIX diff) can be obtained. For files that are missing from one tree, _similarly named_ files in that tree are reported. Inconsistent files can then be copied in either direction or deleted on either machine. The file trees do not need to be accessible via nfs. Files checksums are computed in parallel, so largely similar trees can be compared over a slow network link. The client and server processes can also be run on the same machine. File selection and interaction with a revision control system such as RCS can be handled by scripting using jpython. Requirements Java1.1 or later and JFC/Swing1.1 are needed.
* * *
###  15.4.2.11. sitecopy
Sitecopy is for copying locally stored websites to remote web servers. The program will upload files to the server which have changed locally, and delete files from the server which have been removed locally, to keep the remote site synchronized with the local site, with a single command. The aim is to remove the hassle of uploading and deleting individual files using an FTP client.
* * *
##  15.4.3. DataConversion: AddressBooks, BookMarks, Todo-Lists, LDAP, Webpages
Transferring user data from one mobile device to another one, often requires some tools to extract the data from the source device before importing them into the target device, for example if you want to change your favorite mobile phone. Or if you want to use the addressbook from your mobile with your PDA, too. Here are some tools for
* * *
#  15.5. Backup
To me data on mobile computers are even more likely to be damaged or lost than on desktop computers. So backups are even more important. There are different solutions for backups in mobile environments. I will describe them in one of the next issues.
For backups on removable media like CD-R/RW or DVD-R/RW you may boot from a Knoppix Live CD/DVD using the **toram** boot option. This way Knoppix will be completely loaded into RAM and you may remove the Knoppix CD/DVD from the drive to replace it with the backup media. Note: this will only work if your laptop provides more than 1GB RAM.
* * *
#  15.6. Connections to Servers
From Dirk Janssen <dirkj_AT_u.arizona.edu>: Here are several good ways of working on your laptop from your desktop machine. If you have a separate desktop machine at work, you might want to use that as a terminal server to your laptop. This means you get the larger screen and the better keyboard, without having to worry about syncing files. The easiest way to do this is to install ssh on both sides, and ssh from your desktop (running X) to the laptop. Ssh will provide a secure connection and, crucially, a secure X connection between the two machines. If you type, for example, **emacs &** in the ssh shell, emacs will start a window on your desktop machine while running on your laptop.
There are various ways in which you can make this situation more productive/complicated. Emacs, for one thing, can open windows (called frames by emacs) on separate displays by using **make-frame-on-display**. This way, you can have the same emacs displaying on your desktop and your laptop: A dual headed system is born.
For other programs, you usually have to decide at startup time on which screen you want them. To run them on the laptop screen, start them as usual. To run them on the desktop screen, start them from the ssh shell on the desktop or redirect their screens using the DISPLAY variable. Some programs also accept a **-display** option. Read the documentation on **xauth** on how to set this up. An easy way out is to find out which pseudo display ssh has created for you by typing **echo $DISPLAY** in the ssh shell. Assuming your desktop is called **olli** and your laptop **stan** , this will usually produce something like **stan:10**. This means that processes on stan (the laptop) display on what they think is the 10th screen of stan, which by some ssh magic is actually relayed (in a secure way) to the screen of olli.
There are some ways in which you can dynamically move windows from one machine to another. A very interesting approach is taken by **xmove** , but this program lacks a good user interface (any volunteers?). Xmove creates a pseudo screen (similar to the stan:10 that ssh creates) and windows that have their DISPLAY set to this pseudo screen can be moved back and forth between real screens (provided all screens use the same color depth).
Alternatively, you can run an one of the several programs that open a **virtual root window** : A window on your desktop that contains other windows. It looks a lot like running an emulator. With these programs, you can start your processes on stan, then move all their windows to olli, then work for a while, and then move them back so you can continue working on stan. Hibernate your laptop and repeat ad infinitum. Check out xmx and VNC for this.
If this is all too complicated for you, but you like to use the two screens at the same time, consider at least installing x2x. This little tool makes it possible to move your mouse from one screen to the other, and the keyboard focus goes with it. To run it, you need another ssh going from stan (the laptop) to olli (the desktop): ie. type **ssh olli** in a stan xterm. Keep this shell running and find out which pseudo screen was created with **echo $DISPLAY**. This will return something like **olli:10** (see above for explanation). Now, type this in any shell on olli: **x2x -west -to olli:10** (and I mean, in a shell that runs on olli and displays on olli, not an ssh shell) This creates a little black band to on the left (west) side of your desktop's screen. Whenever you move the mouse over this, the mouse on screen olli:10 will move. Because olli:10 is just an ssh-created alias for the screen of stan, the mouse on your laptop will move and you can type there by only moving your head, not your hands.
A note on X-security: Playing around with various screen programs is much easier if you issue an **xhost +** on either computer. But this is extremely unsafe. Do this only when you are not connected to any larger network. If you have everything working, spend some time on getting xauth to work. If you use xdm, it is usually easy. Otherwise, consider starting your Xserver with the same magic cookie all the time. This is less safe, but still pretty safe, and it means that you have to copy the cookies only once. Check the startup scripts (.xserverrc, .xinitrc, .xsession, etc) for something like **cookie="MIT-MAGIC-COOKIE-1 `keygen`"** and change that into (invent your own cookie here): **cookie="MIT-MAGIC-COOKIE-1 12345678901234567890abcdefabcdef"**
* * *
#  15.7. Security in Different Environments
##  15.7.1. Introduction
I am not a computer security expert, but I think that security associated with mobile devices requires specific attention. Please read the
Please read also the
* * *
##  15.7.2. Means of Security
  1. Antivirus policy: For Linux there are some anti virus programs available. Check the BIOS for an option to disable writing at the boot sector.
  2. Laptop as a security risk itself: Since a laptop can easily be used to intrude a network, it seems a good policy to ask the system administrator for permission before connecting a laptop to a network.
  3. Secure Protocol: When connecting to a remote server always use a secure protocol (for instance **ssh**) or tunneling **tunnelv** , **pptp** and **APOP** for POP accounts.


* * *
#  15.8. Theft Protection
##  15.8.1. Means to Protect the Data
  1. Encryption: the Linux Kernel offers different options. This
  2. Here are some
  3. User passwords: can be easily bypassed if the intruder gets physical access to your machine.
  4. Hard Disk Passwords:
  5. BIOS passwords: are easily crackable at least with older laptop models. Some manufacturers have now a second boot password (IBM).
If you use a BIOS password/boot loader security, ADVERTISE IT! Paste a sticker (or tape a piece of paper) on the top of your laptop, saying something like:
```
                           WARNING

This laptop is password protected. The password can only be removed
by an authorized [manufacturer's name] technician presented with
proof of ownership. So don't even think of stealing it, because
it won't do you any good.

```

---
  6. Before you buy a second hand machine, check whether the machine seems to be stolen. I have provided a survey of


* * *
##  15.8.2. Means to Protect the Hardware
  1. Laptop lock: Almost all (if not all) of the new laptops come with a slot for the lock, and if yours doesn't have one, most locks come with a kit to add a slot. One of Targus' Defcon locks even has a motion sensor, so you don't have to lock it up to a secure place, if you don't have one around.
The only drawback that I can think of is that it takes a couple extra seconds to set up or pack up your laptop. It takes about 30 seconds to snap into place and makes it impossible to quickly walk away with the laptop. It won't stop a determined thief with the time to unscrew the legs of the desk or one that wanders around with a substantial pair of wire cutters in hand, but I feel pretty secure leaving the laptop on my desk while I go to meetings or lunch.
Well known manufacturers of dedicated laptop locks are
  2. Name plates: to reduce the possibility of theft, you may want to have a nameplate (name, phone, e-mail, address) made and affixed to the cover of the laptop. A nice one will cost you about $12, and can be made by any good trophy shop. They'll glue it on for you too. You could use double-sided tape instead, but glue is more permanent. So it's easy to return, but will look beaten and abused if these are removed. You may even make an engravement into the laptop cover (inside). And even better into every removable part (hard disk, battery, CD/DVD drive, power unit). If this machine ever gets to a repair office, I might get the machine back. Make sure you remember to update the plates if you move.
If you don't mind marking up a piece of equipment worth several thousand dollars, make sure your laptop has some distinguishing feature that is easily recognizable, e.g. a bunch of stickers pasted on it. Not only does it make your laptop easier to recognize, my guess is that people would be less likely to steal it.
It might even be useful to have a sticker that clearly says "Does Not Run Windows". This is at least an argument for having your bootloader stop at the bootloader prompt, rather than mosey onwards into a colorful XDM login.
  3. Link **xlock** to **apm** services. What about setting a system such as when the laptop is unused for a while, instead of using normal apm service and suspend the machine, makes it run an xlock, disable the apm services in a way such that they do not suspend the machine automatically and start a 'laptop-protection daemon'. When the xlock disappears, the daemon is stopped and the apm services are restarted (so you might use the apm services yourself).
In the case somebody unplugs the machine while under the xlock (without giving the password), then the daemon would detect it and could start doing some preventive action, such as: - playing a sound with maximum volume saying "I am getting stolen". - this daemon could also register to a fixed local server and do a ping every now and then. If the ping stops before the daemon unregister to the server, then server then can take other actions, such as sending SMS message, starting a video camera, in the room, etc. The apm services down would make the stealer unable to use the hot keys to suspend/stop the machine, isn't it?
  4. You can change the "pollution preventer" logo at startup on AWARD BIOSES. See instructions from
  5. Boot loader: a boot loader may be used to put your name and phone number (or whatever text you choose) into the boot sequence before the operating system is loaded. This provides a label that can't be removed by editing files or even doing a simple format of the harddisk. Some boot loaders (e.g. LILO) offer a password option, which is highly recommend (note without it's very easy to get root access).
  6. Camouflage: if you carry a dedicated laptop bag, this can be spotted by a thief easily. So think about getting another kind of bag.
  7. Serial Number: note the serial number in a secure place. This will be necessary if your laptop gets stolen.
  8. Insurance: There are some dedicated insurances, see my page
  9. Use of software that connects and identifies itself: As far as I know there was an old DOS utility that did something like this. It embedded itself into the bootsector and upon a certain keycombination it would throw a serial number onto the screen and play an audio code through the speaker (in case th monitor was no longer usable for whatever reason). You were supposed to register the serial number with the company that produced the utility.
The laptop can send a mail with its real IP address if connected (mail with a print of **ifconfig** started by `/etc/ppp/ip-up` or by a **cron** job (if connected at a company-network).
  10. Always remove the external devices and secure them in another place/room. Set the BIOS to boot on the hard disk first as a default setting and remove boot on other devices if possible. Also try to plug the power supply in the least accessible plug. So if your machine get stolen in your office the 'quick way' (e.g. during a 5 sec. cigarette break), the stealer won't perhaps have time to get the power supply, neither the time to get the drives. Perhaps he/she will end up with a less useful laptop and you may recover it.
  11. Electronic Devices (Transponders): There are also devices available, which can be detected remote via satellites, see my page


* * *
##  15.8.3. The Day After
Your primary goal is to prevent your laptop from being stolen in the first place. Your secondary goal is to recover it after it is stolen. Report it to the police station ASAP. Check the local newsgroup (in case...) or even post in it.
I have provided a
* * *
##  15.8.4. Resources
The chapter about theft protection has taken some advantages of ideas of Lionel "Trollhunter" Bouchpan-Lerust-Juery and a discussion, which has taken place in the
* * *
#  15.9. Dealing with Down Times (Cron Jobs)
A cron-like program that doesn't go by time: **anacron** (like "anac(h)ronistic") is a periodic command scheduler. It executes commands at intervals specified in days. Unlike **cron** , it does not assume that the system is running continuously. It can therefore be used to control the execution of daily, weekly and monthly jobs (or anything with a period of n days), on systems that don't run 24 hours a day. When installed and configured properly, **anacron** will make sure that the commands are run at the specified intervals as closely as machine-uptime permits.
**cron** daemon. Like the original program it runs specified jobs at periodic intervals. However, the original **crond** relies on the computer running continuously, otherwise jobs will be missed. This problem is addressed by **hc-cron** , that is indended for use on _home-computers_ that are typically turned off several times a day; **hc-cron** will remember the time when it was shut down and catch up jobs that have occurred during down time when it is started again.
* * *
#  15.10. Mobile Printing
There are different techniques to print from mobile computers. You may use mobile printer hardware (see chapter Printers and Scanners above) or print via a stationary printer. To connect to a mobile or stationary printer or printer server you may use many protocols:
  1. InfraRed - IrLPT/IrCOMM: See the
  2. InfraRed - IrOBEX: See the
  3. BlueTooth: See the
  4. wireless network - WLAN
  5. network - LAN
  6. rlpr - remote line printer
  7. Server Message Block - SMB, via SAMBA
  8. parallel port
  9. serial port
  10. USB port


* * *
#  15.11. Noise Reduction
Due to the proliferation of cellular phones and walkmans it's not quite common in our days to take care of a quiet environment. Anyway I want to give some recommendations for the polite ones.
Computer noises are caused by hardware (fan, optical drive, hard disk) and applications.
* * *
##  15.11.1. Console (Shell) and X11
The beeping of X11 windows can be configured to a shorter and lower pitched tone or even to a blunt "thump" with **xset b ...** options (a lower pitched tone is usually less annoying and distracting). Independently of that, most xterm-compatible windows and shells can be configured to make "visual bell" instead of "audio bell". For the console **setterm -blength 0** and for X11 **xset b off** turns the bell off. See also the [Visible-Bell-Howto](http://tldp.org/HOWTO/Visual-Bell.html).
* * *
##  15.11.2. PCMCIA
When starting your laptop with PCMCIA-CS configured correctly, this will be shown by two high beeps. If you want to avoid this put **CARDMGR_OPTS="-q"** into the PCMCIA configuration file, e.g. `/etc/default/pcmcia` for Debian/GNU Linux.
To avoid the dialtones during the modem dialing add
```
module "serial_cs" opts "do_sound=0"

```

---
to `/etc/pcmcia/config.opts` (from **man serial_cs**). This will disable speaker output completely, but the **AT M** command should let you selectively control when the speaker is active, e.g. **AT M0** turns off the modem's speaker.
* * *
##  15.11.3. USB
**usbmgr** configuration file `/etc/usbmgr.conf`.
```
### BEEP
# beep off
# beep on

```

---
* * *
##  15.11.4. Hotplug
Add an entry into the configuration file `/etc/sysconfig/hotplug`.
```
HOTPLUG_BEEP="no"

```

---
* * *
##  15.11.5. Fan
![Warning](https://tldp.org/LDP/Mobile-Guide/images/warning.gif) |  Please make sure what you are doing, when configuring the fan. Your laptop may overheat and die, in case you have done something wrong. Just in case you want to check the fan try to cause a heavy CPU load, for example by issuing **md5sum /dev/urandom**. Now **top** will show an increased CPU load and the fan should began to run eventually. Note: usually you need to have been connected to power, otherwise the CPU might reduce load by itself. Also watch for the CPU temperature **acpi -bt** or **cat /proc/acpi/thermal_zone/***.
---|---
For some laptop series there are Linux utilities available to control the fan and other features.
* * *
###  15.11.5.1. Known Problems
With some laptops the fan is always on or at least very often. Here are some remedies.
* * *
####  15.11.5.1.1. Reduction of CPU Frequency
In some cases the fan is always on because the CPU is working with highest frequency. You may use either
* * *
####  15.11.5.1.2. IRQ Problems with ParPort Module
Sometimes the `parport` causes the fan to be always on. You may edit the `/etc/modules.conf` to cure this:
```
 alias parport_lowlevel parport_pc
 options parport_pc io=378 irq=7

```

---
The IO address and the IRQ number depend on the hardware settings or the BIOS configuration. Often the IRQ does not need to be given. The problem and its solution was discussed in the
* * *
####  15.11.5.1.3. ACPI
Sometimes a setting in the `/proc/acpi/` might also help.
* * *
####  15.11.5.1.4. Miscellaneous
Pressing the Fn+z key kombination tells the BIOS to recheck the sensors and stops the fan, for DELL laptops.
* * *
##  15.11.6. Harddisk
To avoid unnecessary hard disk noise you may use the same techniques as described in the power saving chapter above. Modern laptop and notebook hard drives come with a so-called "Acoustic Management", just have a look into the manual to get an overview about the possible settings.
Some hard disk manufacturers offer dedicated tools, e.g. Hitachi's **hdparm -M** offers some Acoustic Management options.
* * *
##  15.11.7. Miscellaneous Applications
You may configure **vi** with the **flash** option, so it will use a flash in case of an error, instead of a bell. So just put this line into your `.vimrc` or at the **vim** prompt:
```
set flash

```

---
or try ```
set visualbell

```

---
* * *
#  Chapter 16. Solutions with Mobile Computers
#  16.1. Introduction
The power and capabilities of laptops and PDAs are sometimes limited as described above. But in turn, they have a feature which desktops don't have their mobility. I try to give a survey about applications which make sense in connection with mobile computers.
* * *
#  16.2. Mobile Network Analyzer
I'm not an expert in this field, so I just mention the tools I know. Please check also for other applications. Besides the usual tools **tcpdump** , **netcat** , there are two applications I prefer, which may be used to analyze network traffic:
The UNIX and Windows NT.
UNIX tool that shows the network usage, similar to what the popular top UNIX command does. **ntop** is based on **libpcap** and it has been written in a portable way in order to virtually run on every UNIX platform and on Win32 as well. **ntop** can be used in both interactive or web mode. In the first case, **ntop** displays the network status on the user's terminal. In web mode a web browser (e.g. netscape) can attach to **ntop** (that acts as a web server) and get a dump of the network status. In the latter case, **ntop** can be seen as a simple RMON-like agent with an embedded web interface.
* * *
#  16.3. Mobile Router
Though designed to work from a single floppy, the _Linux Router Project (LRP)_ , seems useful in combination with a laptop, too.
* * *
#  16.4. Hacking and Cracking Networks
When thinking about the powers of laptops, hacking and cracking networks may come into mind. I don't want to handle this topic here, but instead recommend the
* * *
#  16.5. Mobile Data Collection
##  16.5.1. Related Documentation
  1. [Coffee-HOWTO](http://tldp.org/HOWTO/Coffee.html)
  2. [AX-25-HOWTO](http://tldp.org/HOWTO/AX25-HOWTO/)
  3. [Serial-HOWTO](http://tldp.org/HOWTO/Serial-HOWTO.html)
  4. [Serial-Programming-HOWTO](http://tldp.org/HOWTO/Serial-Programming-HOWTO/)


* * *
##  16.5.2. Applications
A Linux laptop can be used to collect data outside an office, e.g. geodesy data, sales data, network checks, patient data in a hospital and others. There is support for wireless data connections via cellular phone modems and amateur radio. I am not sure whether PCMCIA radio cards are supported, see
* * *
##  16.5.3. Specific Environments
There are laptops available with cases build for a rugged environment (even waterproof laptops). In some environments, for instance in hospitals, take care of the Electro-Magnetic-Compatibility of the laptop. This is influenced by many factors, for instance by the material used to build the case. Usually magnesium cases shield better than the ones made of plastics.
* * *
#  16.6. Mobile Office
With
* * *
#  16.7. Connection to Digital Camera
AFAIK there are currently three methods to connect a digital camera to a laptop: the infrared port (IrDA®), serial port and maybe USB. There are also some auxiliary programs for conversion of pictures, etc.
Eric <dago_AT_tkg.att.ne.jp> wrote: "I finally succeeded in downloading pictures from my digital camera, but not exactly the way I expected, i.e. not through USB port but using PCMCIA card port and memory stick device, part of digital camera hardware. Anyway, some interesting things to mention:
Sony (pretending using a standard) uses the msdos format to store images as JPEG files ; so the best way to have your OS recognizing them is to mount the raw device like a msdos filesystem; using mount directly doesn't work (don't know why) but an entry in the /etc/fstab file allows you to mount the device correctly. i.e.:
```
/dev/hde1    /mnt/camera    msdos     user,noauto,ro    0    0

```

---
Of course, **newfs** before **mount** works too, but there is nothing to see at all ;-) I think both **noauto** and **ro** are important flags; I tried without it and it didn't work. Somehow the mount I got seems buggy . And if **ro** is missing, the camera doesn't recognize back the memory stick and it needs to be msdos-formatted.
Appropriate to the camera documentation , both PCMCIA and USB port behave the same (for Mac and Windoze - i.e. you see a file system auto mounted) - I deduce for Linux it should be the same thing too, as long as the USB driver is installed. I think now that mounting USB raw device the way I did with PCMCIA should work, but I still couldn't find which device to use."
**gPhoto**. The utility is a simple command-line program for standalone downloading of photos from the cameras.
**gPhoto** sports a new HTML engine that allows the creation of gallery themes (HTML templates with special tags) making publishing images to the world wide web a snap. A directory browse mode is implemented making it easy to create an HTML gallery from images already on your computer. Support for the Canon PowerShot A50, Kodak DC-240/280 USB, and Mustek MDC-800 digital cameras.
UNIX box. Bruce D. Lightner <lightner_AT_metaflow.com> has added support for Win32 and DOS platforms. Note that the program does not have any GUI, it is plain command-line even on Windows. For a GUI, check out the **phototk** program.
* * *
#  16.8. Connection to QuickCam (Video)
AFAIK there are three methods to connect a video camera to a laptop: a ZV port, FireWire and maybe USB, but I don't know how this works with Linux. I have heard rumors about using a sound card for video data transfer to a Linux box, see **sane** package which is build for scanner support, this should contain support for still-grabbers as well.
USB ports. Also SONY has announced a webcam with USB port. See a survey at
* * *
#  16.9. Connection to Television Set
If you have a ZV port in the laptop, it should be easy to connect it to a TV set, using either NSCA or PAL, but I don't know whether either works with Linux.
* * *
#  16.10. Connection to Cellular Phone
AFAIK there are two methods to connect a cellular phone to a laptop: via the _infrared port_ (IrDA®) or via the _serial port_. See the Linux/IrDA® project for the current status of IrDA® connections. As far as I know only the Ericsson SH888, the Nokia 8110 and the Siemens S25 provide infrared support.
* * *
#  16.11. Connection to Global Positioning System (GPS)
From the [Hardware-HOWTO](http://tldp.org/HOWTO/Hardware-HOWTO/) I know there is _Trimble Mobile GPS_ available for Linux. You may also connect a GPS via a serial port. Most GPS receivers have a data port and can connect to a PC with a special serial cable.
  * Differential GPS is a technique to apply a correction factor from a known location to a GPS signal. This can substantially reduce the uncertainty in the GPS location. Normally the correction signal is acquired using a special radio receiver: **dgpsip** allows you to receive a DGPS signal via TCP/IP, and send it to the GPS connected to your serial port.
  * The UNIX/Linux/X and a GPS receiver. It performs logging and replaying of a journey, supporting a moving-map display. QtGPS works with Lat/Long and British OSGB (Ornance Survey) coordinate systems.


* * *
#  16.12. Connection via Amateur Radio (HAM)
As far as I know laptops are used in amateur radio contests. Please see HAM-HOWTO by Terry Dawson, _VK2KTJ_ , <terry_AT_perf.no.itg.telstra.com.au>.
* * *
#  16.13. Satellite Watching
Together with an antenna and software like **seesat** or **sattrack** you can use a laptop to locate a satellite for visual observation. You could also use **xephem** on a laptop when stargazing. See also the [Astronomy-HOWTO](http://tldp.org/HOWTO/Astronomy-HOWTO/) .
* * *
#  16.14. Aviation
Many people are using laptops for aviation related topics. The
* * *
#  16.15. Blind or Visually Impaired Users
There are some groups of which could gain a specific profit by using laptops. For instance blind or visually impaired people (I explicitly avoid to say handicapped people). See [Accessibility-HOWTO](http://tldp.org/HOWTO/Accessibility-HOWTO/) and **brltty** is a program which supports different braille terminals. **Festival** is a speech synthesis system. Screen and cursor magnifiers are available. See TuxMobil for a
# VIII. Appendix

**Table of Contents**


A. [Other Operating Systems](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a1-other-operating-systems)


A.1. [Microsoft DOS and Windows](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a1s1-dos-windows9x-nt)


A.2. [BSD UNIX](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a1s2-bsd-unix)


A.3. [OS/2](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a1s3-os-2)


A.4. [NOVELL Netware](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a1s4-novell-netware)


A.5. [Debian GNU/Hurd (hurd-i386)](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a1s5-debian-gnu-hurd)


B. [Other Resources](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a2-other-resources)


B.1. [Main WWW Resources](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a2s1-main-www-resources)


B.2. [Mailing Lists](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a2s2-mailing-lists)


B.3. [USENET Newsgroups](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a2s3-usenet-newsgroups)


B.4. [Newsletters, RSS Channels](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a2s4-rss-channels)


B.5. [Magazines, Blogs Newsletters](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a2s4-magazines-and-newsletters)


B.6. [General Laptop Information](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a2s5-general-laptop-information)


C. [Repairing the Hardware](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a3-repairing-the-hardware)


D. [Survey about Micro Linuxes](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a4-survey-micro-linuxes)


E. [Dealing with Limited Resources or Tuning the System](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a5-limited-resources)


E.1. [Related Documentation](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a5s1-related-howtos)


E.2. [Introduction](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a5s2-introduction)


E.3. [Small Space](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a5s3-small-space)


E.4. [Hard Disk Speed](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a5s4-harddisk-speed)


E.5. [Small Memory](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a5s5-small-memory)


E.6. [Low CPU Speed](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a5s6-low-cpu-speed)


E.7. [Power Saving Techniques](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a5s7-power-saving-techniques)


E.8. [Kernel](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a5s8-kernel)


E.9. [Tiny Applications and Distributions](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a5s9-tiny-applications)


E.10. [Hardware Upgrade](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a5s10-hardware-upgrade)


F. [Ecology and Laptops](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a6-ecology)


F.1. [Ecological Comparisons of Computers](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a6s1-ecology)


G. [NeoMagic Graphics Chipset Series NM20xx](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a6-neomagic-chip)


G.1. [Introduction](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a6s1-introduction)


G.2. [Textmode 100x37](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a6s2-textmode-100-37)


H. [Annotated Bibliography: Books For Linux Nomads](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a7-annotated-bibliography)


I. [Resources for Specific Laptop Brands](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a8-resources-specific-laptops)


I.1. [COMPAQ](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a8s2-compaq)


I.2. [DELL](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a8s3-dell)


I.3. [IBM/Lenovo™ ThinkPad](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a8s4-ibm)


I.4. [Sony VAIO](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a8s5-sony)


I.5. [Toshiba](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a8s6-toshiba)


J. [Credits](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a10-credits)


K. [Copyrights](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a11-copyrights)


K.1. [Copyrights](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a11s1-copyrights)


K.2. [GNU Free Documentation License - GFDL](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-p6a11s2-gfdl)

* * *
#  Appendix A. Other Operating Systems
#  A.1. Microsoft DOS and Windows
##  A.1.1. Introduction
There are a few reasons which might make it necessary to put Micorosoft DOS/Windows and Linux together on one laptop. Often the support for the flash ROM of PCMCIA cards and modems is not available for Linux, or you have to retrieve hardware information, which is not visible with Linux, due to a lack of support by some hardware manufacturers. I'm not sure whether these tasks can be performed under an emulation like DOS-EMU, WINE or VMware.
If you want Linux with X11, Netscape, etc., and Microsoft-Windows9x,NT,2000,XP things will be tight in a 1GB harddisk. Though I did so with a 810MB disk.
* * *
##  A.1.2. DOS Tools to Repartition a Hard Disk
Often you get a preinstalled version of Microsoft-Windows on your laptop. If you just want to shrink the Windows partition, you need a tool to resize the partition. Or you can remove the partition first, repartition, then reinstall. Most of the following information I found at the page of
A well known and reliable commercial product is
**System Commander 2000** by Symantec? resizes FAT32 partitions, unlike Partition Magic, SC2000 seems to be able to work without the presence of an installed Microsoft operating system (tough you may use Partition Magic from two standalone floppy disks).
One more "newer" utility for repartitioning and resizing FAT partitions is _Ranish Partition Manager/Utility_ (FAT-32 support is claimed for this as well, Linux support is taken into account.)
Many people have used _FIPS 15c_ (which may support FAT-32)
* * *
##  A.1.3. Partition Sharing
You may share your swap space between Linux and Windows. Please see "Dealing with Limited Resources" section.
With Linux you can mount any kind of DOS/Windows partition of the type **msdos** , **vfat** and even compressed drives (Drivespace, etc.). For long file names use **vfat** and if you like autoconversion ( a nice feature for text files), you may do so by using the **conv=auto** option. I have used this in my `/etc/fstab`, but be aware this might cause some strange behaviour sometimes, look at the kernel docs for further details.
```
/dev/hda8    /dos/d    vfat    user,exec,nosuid,nodev,conv=auto    0    2

```

---
The other way round there are also
The tools allow to list directories, to copy files from Linux to DOS and to copy files from DOS to Linux. You also can delete files or modify access rights of Linux files from DOS/Windows.
In combination with an included simple server program, you can also access your files from a remote client over the net (however, this might be a security risk, as access protection in this case is rather simple).
* * *
###  A.1.3.1. LINE Is Not an Emulator
* * *
##  A.1.4. Installation without CD Drive
You may use the CD drive of a desktop (or copy the content of the CD to the hard disk) and connect both machines with a null modem cable. Then use a DOS boot floppy and the program **INTERLNK.EXE** to connect both machines.
* * *
##  A.1.5. Miscellaneous
Windows/NT offers: RAS - Remote Access Service
Windows/9x/NT offers the PPTP protocol to connect to remote sites via a TCP/IP tunnel. This protocol is also supported by Linux.
* * *
#  A.2. BSD UNIX
FreeBSD is a version of the UNIX operating system that runs on PC hardware. It uses a different set of support for PCMCIA devices, APM, and other mobility related issues.
  1. AFAIK there is no IrDA® support yet.


* * *
#  A.3. OS/2
At PCMCIA cards working with OS/2.
* * *
#  A.4. NOVELL Netware
The client side with DOS/Windows9x style operating systems seems to be no problem, since there are many PCMCIA cards with drivers for Netware available. For Linux connections see the **mars_nwe** package. Also the Caldera Linux distribution is well known for its Novell support.
I hadn't time to build a Netware server on a laptop yet and couldn't check whether there are network connections possible (PCMCIA driver for Netware server).
* * *
#  A.5. Debian GNU/Hurd (hurd-i386)
The GNU Hurd is a totally new operating system being put together by the GNU group. In fact, the GNU Hurd is the final component which makes it possible to built an entirely GNU OS -- and Debian GNU/Hurd is going to be one such (possibly even the first) GNU OS. The current project is founded on the i386 architecture, but expect the others to follow soon.
The PCMCIA support isn't ready yet.
* * *
#  Appendix B. Other Resources
#  B.1. Main WWW Resources
Kenneth E. Harker maintains a quite valuable database at
The author of this guide maintains the
* * *
#  B.2. Mailing Lists
A survey of laptop mailing lists. Some of the addresses are taken from Kenneths page. All comments are by me:
* * *
##  B.2.1. General Lists
To join the _Linux-Laptop-Mailing-List_ at TuxMobil visit the
To join the _Linux-Laptop-Mailing-List_ from Kernel.Org write a mail to <majordomo_at_vger.kernel.org> with **subscribe linux-laptop** in the subject. You will get a confirmation message than, which you have to reply appropriately. Note: This is the list formerly admininstrated by <majordomo_at_vger.rutgers.edu>. This was a list with much traffic, current traffic seems to be very low. The list seems to have lost most of its members since changing the address.
A searchable mailing list archive (of the predecessor) is hosted in the miscellaneous section of
The
Also the
The
* * *
##  B.2.2. Lists Dedicated to a Linux Distribution
There is now a _debian-laptop mailing list_. Any questions or discussions concerning running the Debian/GNU Linux operating system(s) on laptops are welcome. Send mail to <debian-laptop-request_at_lists.debian.org> with a subject of **subscribe**. Or visit the
SuSE offers a mailing list for discussion about mobility in the openSUSE distribution <opensuse-mobile_AT_opensuse.org>. You may subscribe at the
* * *
##  B.2.3. Lists Dedicated to a Laptop or Manufacturer
The
The linux-thinkpad list is dedicated to Linux on IBM ThinkPads issues. It
The linux-thinkpad list is dedicated to Linux on IBM ThinkPads issues. It has almost no traffic. Write a mail to <majordomo_at_bm-soft.com>.
Also the
The
The linux-tosh-40xx list is dedicated to Linux on Toshiba Satellite 40xx issues. It has almost no traffic. Write a mail to <majordomo_at_geekstuff.co.uk>.
* * *
#  B.3. USENET Newsgroups
The USENET newsgroups can provide a source of information about aspects of running Linux on notebooks that haven't yet been documented. If you are unable to find the information you are looking for here or on any of the pages linked to from this site, a post to the USENET newsgroups may turn up an answer from someone that can help you.
* * *
##  B.3.1. Linux Newsgroups
  * [comp.os.linux.portable](news:comp.os.linux.portable) As far as I know there is no archive of this group yet.
  * [comp.os.linux.announce](news:comp.os.linux.announce)
  * comp.sys.mac.portables
  * [comp.os.linux.answers](news:comp.os.linux.answers)
  * [comp.os.linux.development.apps](news:comp.os.linux.development.apps)
  * [comp.os.linux.development.system](news:comp.os.linux.development.system)
  * [comp.os.linux.hardware](news:comp.os.linux.hardware)
  * [comp.os.linux.misc](news:comp.os.linux.misc)
  * [comp.os.linux.networking](news:comp.os.linux.networking)
  * [comp.os.linux.setup](news:comp.os.linux.setup)
  * [comp.os.linux.x](news:comp.os.linux.x)


* * *
##  B.3.2. PDA Newsgroups and IRC Channels
  * comp.sys.handhelds
  * comp.sys.newton.misc
  * comp.sys.palmtops
  * comp.sys.pen
  * #zaurus@irc.freenode.net
  * irc.freenode.net #opie #opie.de


* * *
##  B.3.3. X Window System Newsgroups
  * [comp.windows.x](news:comp.windows.x)
  * [comp.windows.x.announce](news:comp.windows.x.announce)
  * [comp.windows.x.apps](news:comp.windows.x.apps)
  * [comp.windows.x.i386unix](news:comp.windows.x.i386unix)


* * *
##  B.3.4. Hardware Newsgroups
  * [comp.sys.laptops](news:comp.sys.laptops)
  * [alt.periphs.pcmcia](news:alt.periphs.pcmcia)
  * [comp.sys.ibm.pc.hardware.chips](news:comp.sys.ibm.pc.hardware.chips)
  * [comp.sys.ibm.pc.misc](news:comp.sys.ibm.pc.misc)


* * *
#  B.4. Newsletters, RSS Channels
  * The [monthly digest via e-mail](http:tuxmobil.org/mobile_news.html).


* * *
#  B.5. Magazines, Blogs Newsletters
Magazines, blogs and newsletters about mobile computing in general.
* * *
#  B.6. General Laptop Information
These are sources of information of general use to laptop and notebook owners, regardless of the operating system used.
* * *
#  Appendix C. Repairing the Hardware
There are several different reasons that could make it necessary to open the case of a laptop, notebook or PDA.
  1. repair broken hardware
  2. get some hardware info, which isn't available otherwise, e.g. reading the sticker on an undetected chipset
  3. remove the speakers (speakerektomy, as described in [Visual-Bell-HOWTO](http://tldp.org/HOWTO/Visual-Bell.html) )
  4. install overdrive for CPU
  5. reflash the BIOS
  6. change BIOS battery
  7. upgrade harddisk
  8. upgrade memory
  9. implement additional hardware, e.g. an internal wireless LAN miniPCI card


Repairing a laptop can be quite expensive if you don't have a manufacturer's warranty. Sometimes professional support is bad. But opening a laptop case can be difficult. Often the procedures to upgrade the memory and the harddisk are described in the manual. For further details, you should try to get the maintenance/technical manual. Just be extremely careful and make notes as to where each screw goes. You must get most of them back in the right hole or you could ruin the machine by damaging the system board. Also after you get all the screws to an assembly out (some will be hidden) the parts are usually held together with plastic clips molded in, so you still must exercise care to separate them. Sometimes you need certain tools, for instance TORX screw drivers or a solder kit. Good luck.
![Warning](https://tldp.org/LDP/Mobile-Guide/images/warning.gif) |  Usually laptop and PDA manufacturers declare the warranty to be void if the case was opened by people other than their own staff. If you want to try it anyway you may find some interesting links about how to
---|---
* * *
#  Appendix D. Survey about Micro Linuxes
Because of their small or non-existent footprint, micro-Linuxes are especially suited to run on laptops - particularly if you use a company-provided laptop running Microsoft-Windows9x/NT. Or for installation purposes using another non Linux machine. There are several _micro_ Linux distributions out there that boot from one or two floppies or CD/DVD.
Also a [BootDisk-HOWTO](http://tldp.org/HOWTO/Bootdisk-HOWTO/index.html) is available. Thanks to Matthew D. Franz maintainer of
  1. Trinux
  2. **fdisk** and **mkfs.ext2** so that a harddisk install can be done. Useful to boot up on old machines with less than 4MB of RAM.
  3. See also the packages at [Boot-Disk-HOWTO](http://tldp.org/HOWTO/Bootdisk-HOWTO/index.html) .
  4. You may also consider some of the boot floppies provided by various distributions falling into this category, e.g. the boot/rescue floppy of Debian/GNU Linux.
  5. If you like to build your own flavour of a boot floppy you may do so manually, as described in the [Boot-Disk-HOWTO](http://tldp.org/HOWTO/Bootdisk-HOWTO/index.html) or using some helper tools, for instance **mkrboot** (provided at least as a Debian/GNU Linux package) or **pcinitrd** , which is part of the PCMCIA-CS package by David Hinds.
  6. Also you might try to build your Linux system on a ZIP drive. This is described in the [ZIP-Install-HOWTO](http://tldp.org/HOWTO/ZIP-Install.html) .


* * *
#  Appendix E. Dealing with Limited Resources or Tuning the System
#  E.1. Related Documentation
  1. [LBX-HOWTO](http://www.tldp.org/HOWTO/LBX.html)
  2. [Small-Memory-HOWTO](http://tldp.org/HOWTO/Small-Memory/)


* * *
#  E.2. Introduction
As mentioned in the introduction laptops sometimes have less resources if you compare them to desktops. To deal with limited space, memory, CPU speed and battery power, I have written this chapter.
* * *
#  E.3. Small Space
##  E.3.1. Introduction
There are different types of techniques to gain more disk space, such as sharing of space, freeing unused or redundant space, filesystem tuning and compression. Note: some of these techniques use memory instead of disk space. As you will see, there are many small steps necessary to free some space.
* * *
##  E.3.2. Techniques
  1. Stripping: Though many distributions come with stripped binaries today it is useful to check this. For details see **man strip**. To find every unstripped file you can use the **file** command or more convenient the tool **findstrip**. Attention: don't strip libraries, sometimes the wrong symbols are removed due to a bad programming technique. Or use the **--strip-unneeded** option.
  2. Perforation: **zum(1)** reads a file list on stdin and attempts to perforate these files. Perforation means, that series of null bytes are replaced by **lseek** , thus giving the file system a chance of not allocating real disk space for those bytes. Example: **find . -type f | xargs zum**
  3. Remove Odd Files and Duplicates: Check your system for core files, emacs recovery files <#FILE#> vi recovery files <FILE>.swp, RPM recovery files <FILE>.rpmorig and **patch** recovery files. Find duplicates, you may try **finddup**. Choose a system to name your backup, temporary and test files, e.g. with a signature at the end.
  4. Clean Temporary Files: , e.g. `/tmp`, there is even a tool **tmpwatch**.
  5. Shorten the Log Files: usually the files in `/var/log`. You may use **logrotate** to achieve this task.
  6. Remove Files: Remove files which are not "necessary" under all circumstances such as man pages, documentation `/usr/doc` and sources e.g. `/usr/src` .
  7. Unnecessary Libraries: You may use the **binstats** package to find unused libraries (Thanks to Tom Ed White).
  8. Filesystem: Choose a filesystem which treats disk space economically e.g. **rsfs**. Tune your filesystem e.g. **tune2fs**. Choose an appropriate partition and block size.
  9. Reduce Kernel Size: Either by using only the necessary kernel features and/or making a compressed kernel image **bzImage**.
  10. Compression: I didn't check this but as far as I know you may compress your filesystem with **gzip** and decompress it on the fly. Alternatively you may choose to compress only certain files. You can even execute compressed files with **zexec**
  11. Compressed Filesystems: - For e2fs filesystems there is a compression version available
-
  12. Partition Sharing: You may share swap-space (see [Swap-Space-HOWTO](http://tldp.org/HOWTO/Swap-Space.html)) or data partitions between different OS (see **mount**). For mounting MS-DOS Windows95 compressed drives (doublespace, drivespace) you may use **dmsdos**
  13. Libraries: Take another (older) library, for instance **libc5** , this library seems to be smaller than **libc6** also known as **glibc2** .
  14. Kernel: If your needs are fitted with an older kernel version, you can save some space.
  15. GUI: Avoid as much Graphical User Interface (GUI) as possible.
  16. Tiny Distributions: There are some distributions available which fit from one 3.5" floppy to 10MB disk space and fit for small memories, too. See [Appendix A](https://tldp.org/LDP/Mobile-Guide/html/Mobile-Guide.html#mobile-guide-a1-other-operating-systems) Appendix D and below.
  17. External Storage Devices (Hard Disks, ZIP Drives, NFS, SAMBA): Since many notebooks may be limited in their expandability, using the parallel port is an attractive option. There are external hard disks and ZIP Drives available. Usually they are also connectable via PCMCIA. Another way is using the resources of another machine through NFS or SAMBA etc.
  18. Purging of uneeded locales: **localepurge** for Debian is just a simple script to recover disk space wasted for unneeded locale files and localized man pages. Depending on your installation, it is possible to save some 200, 300, or even more megabytes of disk space usually dedicated for locales you'll probably never have any usage for.


* * *
#  E.4. Hard Disk Speed
Use the tool **hdparm** to set up better harddisk performance. Though I have seen laptop disk enabled with _striping_ , I can't see a reason to do so, because in my humble opinion also known as RAID0 striping needs at least two different disks to increase performance. Before using **hdparm** check the BIOS settings for harddisk parameters like DMA or ATA4 or 32bit transfer. The bad thing is that if something is disabled there - it can not be enabled with **hdparm**!
See UNIX and LINUX Computing Journal: `/proc`.
* * *
#  E.5. Small Memory
##  E.5.1. Related Documentation
  1. [Small-Memory-HOWTO](http://tldp.org/HOWTO/Small-Memory/index.html)
  2. [Module-HOWTO](http://tldp.org/HOWTO/Module-HOWTO/)
  3. [Kerneld-HOWTO](http://tldp.org/HOWTO/Kerneld/)


* * *
##  E.5.2. Techniques
Check the memory usage with **free** and **top**.
_memory areas of the same content_ that remain undetected by the operating system. Typically, these areas contain data that have been generated on startup and remain unchanged for longer periods. With **mergemem** such areas are detected and shared. The sharing is performed on the operating system level and is invisible to the user level programs. **mergemem** is particularly useful if you run many instances of interpreters and emulators (like Java or Prolog) that keep their code in private data areas. But also other programs can take advantage albeit to a lesser degree.
You may also reduce the _kernel size_ as much as possible by removing any feature which is not necessary for your needs and by modularizing the kernel as much as possible.
Also you may shutdown every service or _daemon_ which is not needed, e.g. **lpd** , **mountd** , **nfsd** and close some _virtual consoles_. Please see [Small-Memory-HOWTO](http://tldp.org/HOWTO/Small-Memory/) for details.
And of course use _swap space_ , when possible.
If possible you use the resources of another machine, for instance with X11, VNC or even **telnet**. For more information on Virtual Network Computing (VNC), see
* * *
#  E.6. Low CPU Speed
You may want to overdrive the CPU speed but this can damage your hardware and I don't have experience with it. For some examples look at
* * *
#  E.7. Power Saving Techniques
  1. If you don't need infrared support, disable it in the BIOS or shutdown the IrDA® device driver. There are also some IrDA® features of the kernel which are useful for saving power.
  2. PCMCIA services consume much power, so shut them down if you don't need them.
  3. I'm not sure to which extend the _backlight_ consumes power.
![Warning](https://tldp.org/LDP/Mobile-Guide/images/warning.gif) |  As far as I know this device can only bear a limited number of uptime circles. So avoid using screensavers, which turn off the backlight.
---|---
If you want do it anyhow, you may use **xset +dpms** and **xset dpms 0 0 300** This turns the screen off after 5 minutes of inactivity. Works only if the display is DPMS capable.
  4. For some examples to build batteries with increased uptime up to 8 hours look at
  5. For information about APM look at the chapter APM above.
  6. The "noatime" option when mouting filesystems tells the kernel to _not_ update the _access time_ information of the file. This information, although sometimes useful, is not used by most people. Therefore, you can safely disable it, then preventing disk access each time you **cat** a file. Here is an example of a `/etc/fstab` with this power-saving option: **/dev/hda7 /var ext2 defaults,noatime 0 2**
  7. _hdparm_ is a Linux disk utility that lets you set spin-down timeouts and other disk parameters.
  8. **update** daemon, **mobile-update** minimizes disk spin ups and reduces disk uptime. It flushes buffers only when other disk activity is present. To ensure a consistent file system call **sync** manually. Otherwise files may be lost on power failure. **mobile-update** does not use APM. So it works also on older systems.
  9. **noflushd** monitors disk activity and spins down disks that have been idle for more than <timeout> seconds. It requires a kernel >=2.2.11 . Useful in combination with **hdparm** and **mount** with _noatime_ option to bring down disk activity.
Here are some comments and thoughts by Nat Makarevitch about a possible approach which may reduce the disk activity under Linux (sparing energy, especially with noflushd) the file Documentation/filesystems/proc.txt of the Linux sourcetree documents some useful features, esp. in the `/proc/sys/vm` section. Under Linux 2.2 I used:
```
echo "100 5000 8 256 500 60000 60000 1884 2" > /proc/sys/vm/bdflush

```

---
especially under Linux 2.4 which uses its spare time to 'pre-save' the less-used memory pages into the swap, increasing the disk activity I tried to figure the more adequate parameters (Linux 2.4.9, 192 MB RAM, Toshiba 3480 laptop) beware: some of those parameters may be dangerous or useless (I have not gathered serious data about the practical efficiency). moreover do not forget that delaying disk writes of data is intrinsically dangerous ```
echo 99 512 32 512 0 300000 60 0 0 > /proc/sys/vm/bdflush
# is '60' the max value for age_super?
echo 1 1 96 > /proc/sys/vm/buffermem
echo 512 128 32 > /proc/sys/vm/kswapd
echo 1 10 96 > /proc/sys/vm/pagecache

```

---
  10. The _Klibreta_ , too.
  11. At Kenneth E. Harker's page there is a recommendation for LCDproc LCD display. This program shows, among other things, battery status on notebooks." I tried this package and found that it connects only to the external LCD 20x4 display , which is a LCD display connected to a serial port. I can't see any use for a laptop yet, but you might use it to build a wearable.
  12. The
  13. _KAPM_ , _Kbatmon_ and _Kcmlaptop_. Written by Paul Campbell _kcmlaptop_ is a set of KDE control panels that implements laptop computer support functions, it includes a dockable battery status monitor for laptops - in short a little icon in the KDE status bar that shows how much battery time you have left. It also will warn you when power is getting low and allows you to configure power saving options. Similar packages you may find at the GNOME project
  14. Please see the [Battery-Powered-HOWTO](http://tldp.org/HOWTO/Battery-Powered/) for further information.


Some more words about disks spin down with **noflushd** or **hdparm** utilities. The objective is to reduce hard disk usage to minimum, because on most laptops it is the primary source of noise and energy consumption. The "noflushd" daemon is a replacement of "update" which makes buffer updates on disk only when some other data is being read from the disk (the behavior of "update" is to flush buffers every 5 seconds, and it usually generates constant disk activity, so that the disk never becomes idle). "noflushd" also sets the disk spindown time and automatically calls "sync" before spindown. The syntax is something like "noflushd -n 5 /dev/had". Using "noflushd" may cause loss of data if some files were edited while the disk was parked and not sync'ed, e.g. if the power was suddenly lost.
The **hdparm** utility can set the sleep time too, and also tune the IDE disk parameters for better performance. Make sure that the kernel IDE parameter "Use DMA by default when available" (section "Block devices") is enabled.
However, it is not enough to enable **noflushd** or IDE disk sleep time to make the disk effectively silent, because the system in most default installations is running many cron jobs, writes to log files, uses swap and so on. This activity is not always desirable, especially if the computer is standalone (not on network) and is used mostly by one user. Here are some recommendations.
First, the cron daemon and friends (anacron, atd, logrotate, sendmail / exim / ...) could be removed from the system if the services they run (such as, cleaning /tmp directories and logs, checking email etc.) are not needed.
Secondly, the syslogd configuration file `/etc/syslog.conf` should be modified to reduce the number of log files and messages logged, and also to have "-" signs before every file name (which means that the system will not have to sync the disk every time a message is logged).
Also, it is advisable to add "mark:none;" to the "syslog" strings, so that the "strich strich strich MARK strich strich strich" messages do not get written to the log files every half an hour. Typical Linux installations today have too many log files for the home user.
Finally, the disk may not go to sleep when a lot of swap space is in use. Type "free" and see how much swap is being used and how much free RAM is available. If you think there is enough free RAM to work without swap, or if there is a lot of swap used AND also a lot of free RAM, consider freeing the swap space ("su; swapoff -a; swapon -a") or switching the swap space off altogether ("su; swapoff -a"). Working without swap should be fine on systems with 64MB or more of RAM. (Working without swap will reduce the available memory, of course, and some software crashes without warning when it runs out of memory. But, adding swap will not prevent the crash resulting from some runaway memory consumuing software, it will only delay it, and it will make the system swap a lot before it happens.)
With these changes in the system, one could get the laptop to work for extended periods of time with its hard disk switched off.
The kernel can be configured with "Yes" to "APM Support" and "Enable console blanking using APM" (section "General setup"). Then the LCD screen lamp will shut off in console mode (so not just the screen goes black, but also the lamp). In X mode, the same effect can be obtained with "xset +dpms" (enable DPMS function) and "xset s blank" (enable screen blanking). One can add these commands to the X window session or window manager initialization scripts.
The computer's BIOS energy savings options (hard disk sleep time, video blanking time and so on) are probably not useful and in some cases may even cause crashes. Therefore they could be disabled in the laptop's BIOS.
* * *
#  E.8. Kernel
##  E.8.1. Related Documentation
  * [Kernel-HOWTO](http://tldp.org/HOWTO/Kernel-HOWTO/)
  * [BootPrompt-HOWTO](http://tldp.org/HOWTO/BootPrompt-HOWTO.html)


Many kernel features are related to laptops. For instance APM, IrDA®, PCMCIA and some options for certain laptops, e.g. IBM™ ThinkPads. In some distributions they are not included by default. And the kernel is usually bigger than necessary. So it's seems a good idea to customize the kernel. Though this task might seem difficult for the beginner it is highly recommended. Since this involves dangerous operations you need to be careful. But, if you can install a better kernel successfully, you've earned your intermediate Linux sysadmin merit badge. - I will not handle this here, because this topic is already covered in other documents.
Compile a modular kernel with modules for CDROM, floppy, pcmcia, sound and any other peripherals. It will allow to delay loading of these modules until these devices are actually used, and it may help recover the system after a hardware failure, e.g. a bad CDROM, because a module can be removed and re-inserted without restarting the system.
* * *
#  E.9. Tiny Applications and Distributions
A small collection yet, but I'm looking for more information.
  1. BOA - "Lightweight and High Performance WebServer. **boa** is a single-tasking HTTP server. That means that unlike traditional web servers, it does not fork for each incoming connection, nor does it fork many copies of itself to handle multiple connections. It internally multiplexes all of the ongoing HTTP connections, and forks only for CGI programs (which must be separate processes.) Preliminary tests show boa is capable of handling several hundred hits per second on a 100 MHz Pentium."
  2. MGR - a graphical windows system, which uses much less resources than X.
  3. Low Bandwidth X:
Alan Cox in LINUX REDUX February 1998 " .. there are two that handle _normal_ applications very nicely. LBX (Low Bandwidth X) is the _official_ application of the X11 Consortium (now
  4. **Figure E-1. Screenshot of**blackbox**.**
![](https://tldp.org/LDP/Mobile-Guide/html/images/blackbox.png)
  5. UNIX systems.
  6. linux-lite - distribution based on a 1.x.x kernel for systems with only 2MB memory and 10MB harddisk. URL see above.
  7. **fdisk** and **mkfs.ext2** so that a harddisk install can be done. Useful to boot up on old machines with less than 4MB of RAM.
  8. cLIeNUX - client-use-oriented Linux distribution.
  9. UNIX useful for very small systems, such as 286 CPU and 640K RAM . There is even X11 support named mini-x by
  10. **screen** - tiny but powerful console manager. John M. Fisk <fiskjm_AT_ctrvax.vanderbilt.edu> in _at the console_."
  11. tinyirc - "A tiny, stripped down IRC Client. Doesn't have most of the more advance commands in the ircII family of IRC Clients, nor does it have any color, but it works, and it's tiny."
  12. JOVE Jonathans Own Version of Emacs, a small but powerful editor. .


* * *
#  E.10. Hardware Upgrade
You may also take into account to upgrade the hardware itself, though this may have some caveats, see chapter Open a Laptop Case above. If you need a survey about the possibilities, you can take a look at
* * *
#  Appendix F. Ecology and Laptops
#  F.1. Ecological Comparisons of Computers
Scientists of
LCD displays need less energy than other monitors. For this reason laptops are the most ecological types of the compared computers. They need the smallest amount of energy when they are used. And 3 year old laptops are better than new ones since their processors need less energy than new ones. There is also an article in the German computer magazine
Some more stuff about Linux as a means to save our environment is included in the
* * *
#  Appendix G. NeoMagic Graphics Chipset Series NM20xx
#  G.1. Introduction
The NeoMagic graphics chipset series NM20xx has been popular in laptops build around 1996. For a long time this graphics chip was only supported by commercial X11 servers, since the middle of 1998 RedHat provided a binary X11 server manufactured by PrecisionInsight. Since version 3.3.3 the appropriate X11 server is also available in XFree86.
* * *
#  G.2. Textmode 100x37
This chapter is a courtesy of Cedric Adjih , though I have changed some minor parts. Please note: Another method to achieve a better resolution in text mode is the use of the framebuffer driver (as explained in the X-Windows chapter above). This method requires kernel reconfiguration (some Linux distributions include an appropriate kernel already) and a new entry (vga=NNN) in `/etc/lilo.conf`. In text mode it works even with VESA BIOSes before version 2.0, at least on the models I could test it. Though the SVGATextMode method could be faster (couldn't check this yet).
An apparently little known fact about the Neomagic chipset NM20xx is that you can run text mode in 100x37 (i.e. 800x600). This text mode is very nice (as opposed to the 80x25 which is ugly). I tried this with a HP OmniBook 800 and suppose it might work with other laptops using the NeoMagic chip, too.
The main problem is that is a bit difficult to set up, and if you're going wrong with the commands **SVGATextMode** or **restoretextmode** some results on the LCD might be frightening. Although I didn't manage to break my LCD with many attempts going wrong, DISCLAIMER: THIS MIGHT DAMAGE YOUR HARDWARE. YOU HAVE BEEN WARNED. FOLLOW THE FOLLOWING INSTRUCTIONS AT YOUR OWN RISKS. I'M NOT RESPONSIBLE IF SOMETHING BAD HAPPENS.
* * *
##  G.2.1. Survey
You need to do _three_ main steps:
  1. Enable Linux to boot in 800x600 textmode. The problem is that you won't see any text before the following two steps aren't done.
  2. Automatically run **restoretextmode** with correct register data.
  3. Automatically run **SVGATextMode**.


* * *
##  G.2.2. More Details
All the files I have modified, are available for now on
* * *
###  G.2.2.1. Enabling Linux to Boot in 800x600
Recent kernels (2.2.x) need to be compiled with CONFIG_VIDEO_GFX_HACK defined. Default is off. (look in `/usr/src/linux-2.2.x/arch/i386/boot/video.S`)
This is done by passing the parameter **vga=770** to older kernels or **vga=7** to 2.2.x kernels. Example with `lilo.conf`:
```
image=/boot/bzImage-modif
label=22
append="svgatextmode=100x37x8_SVGA" #explained later
vga=7
read-only

```

---
* * *
###  G.2.2.2. Running restoretextmode and SVGATextMode at Boot Time
Running **restoretextmode** and **SVGATextMode** at Boot Time. You must arrange to run **restoretextmode <name of some textreg.dat file>** and **SVGATextMode 100x37x8_SVGA** at boot time.
An example `textreg.dat` for restoretextmode (obtained using **savetextmode**) is in my tar archive in `tmp/`, and an example `/etc/TextConfig`.
Since I'm lazy, I've simply put **SVGATextMode** and **restoretextmode** in the `/etc/rc.boot/kbd` file from my Debian/GNU Linux which get executed at boot time (also available in the tar archive).
* * *
###  G.2.2.3. Now the Key Point
Annoying things will be displayed if you don't use the right SVGATextMode in the right video text mode: this is why I also pass the environmental variable **"svgatextmode=100x37x8_SVGA"** (arbitrary name) to the kernel (using append=xxx in lilo.conf) when I also set **vga=7** : the script `/etc/rc.boot/kbd` tests this variable and calls **restoretextmode** and **SVGATextMode** IF AND ONLY IF.
* * *
##  G.2.3. Road Map
  1. Recompile the kernel 2.2.x with CONFIG_VIDEO_GFX_HACK
  2. Insert the restoretextmode with the correct parameter in the initialisation script, with no other changes.
  3. Boot with normal text mode (80x25) but restoretextmode: you should see the screen going to 100x37, but with only 80x25 usable. Don't use SVGATextMode yet.
  4. It is much better to conditionnalize your initialize code as I did, to keep the possibility of booting in both modes: you may test this now with some reboots (starting restoretextmode or not).
  5. Boot with 100x37 text mode using parameter **vga=7** (lilo.conf), you should see white background at some point, but the characters will be black on black. This is ok. You'll have to reboot blindly now.
  6. Insert the <path>/SVGATextMode 100x37x8_SVGA after the restoretextmode in initialization scripts.
  7. Reboot with **vga=7** (lilo.conf)
  8. Should be OK now. Enjoy.


* * *
#  Appendix H. Annotated Bibliography: Books For Linux Nomads
Scott Mueller: Upgrading and Repairing Laptops, 2003
From the publisher: "Scott Mueller goes where no computer book author has gone before right past all the warranty stickers, the hidden screws, and the fear factor to produce a real owner's manual that every laptop owner should have on his desk. This book shows the upgrades users can perform, the ones that are better left to the manufacturer, and how to use add-on peripherals to make the most of a laptop. The CD contains one-of-a-kind video showing just what's inside a portable PC."
Other resources:
Chris Hurley, Michael Puchol, Russ Rogers, Frank Thornton: WarDriving - Drive, Detect, Defend, A Guide to Wireless Security, 2004
From the Publisher: "Wardriving has brought some of the top people in the wireless industry together to put together a truly informative book on what wardriving is and the tools that should be part of any IT department's arsenal that either has wireless or is looking to deploy it." -John Kleinschmidt, Michiganwireless.org Founder The practice of WarDriving is a unique combination of hobby, sociological research, and security assessment. The act of driving or walking through urban areas with a wireless-equipped laptop to map both protected and un-protected wireless networks has sparked intense debate amongst lawmakers, security professionals, and the telecommunications industry. This first ever book on WarDriving is written from the inside perspective of those who have created the tools that make WarDriving possible and those who gather, analyze, and maintain data on all secured and open wireless access points in very major, metropolitan area worldwide. These insiders also provide the information to secure your wireless network before it is exploited by criminal hackers. Wireless networks have become a way of life in the past two years. As more wireless networks are deployed the need to secure them increases. This book educates users of wireless networks as well as those who run the networks about the insecurities associated with wireless networking. This effort is called WarDriving. In order to successfully WarDrive there are hardware and software tool required. This book covers those tools, along with cost estimates and recommendations. Since there are hundreds of possible configurations that can be used for WarDriving, some of the most popular are presented to help readers decide what to buy for their own WarDriving setup. Many of the tools that a WarDriver uses are the same tools that could be used by an attacker to gain unauthorized access to a wireless network. Since this is not the goal of a WarDriver, the methodology that users can use to ethically WarDrive is presented. In addition, complete coverage of WarDriving applications, such as NetStumbler, MiniStumbler; and Kismet, are covered."
TuxMobil Resources:
Isidor Buchmann: Batteries in a Portable World - A Handbook on Rechargeable Batteries for Non-Engineers, 2001
From the Publisher: "Batteries in a Portable World fills a definite need for practical information about rechargeable batteries. Quite often, performance specifications for batteries and chargers are based on ideal conditions. Manufacturers carry out battery tests on brand new equipment and in a protected environment, removed from the stress of daily use. In Batteries in a Portable World, Mr. Buchmann observes the battery in everyday life in the hands of the common user. By reading Batteries in a Portable World, you will acquire a better understanding of the strengths and limitations of the battery. You will learn how to prolong battery life; become familiar with recommended maintenance methods and discover ways to restore a weak battery, if such a method is available for that battery type. Knowing how to take care of your batteries prolongs service life, improves reliability of portable equipment and saves money. Best of all, well-performing batteries need replacement less often, reducing the environmental concern of battery disposal."
TuxMobil Resources:
This book contains a chapter about mobile security.
TuxMobil Resources:
* * *
#  Appendix I. Resources for Specific Laptop Brands
Certain laptops have found some more enthusiastic Linux users, than other models. This list is probably not comprehensive:
* * *
#  I.1. COMPAQ
The latest version of the
* * *
#  I.2. DELL
Mailing list at
Manufacturer Linux information:
* * *
#  I.3. IBM/Lenovo™ ThinkPad
ThinkPad Configuration Tool for Linux by Thomas Hood
_Running Linux on IBM™ThinkPads_, to join send an email to **linux-thinkpad-subscribe_at_topica.com** , to post send mail to **linux-thinkpad_at_topica.com** . See
* * *
#  I.4. Sony VAIO
For installation on VAIOs via external CD drive, see chapter Installation above. Some hints for the Jog-Dial you may find in the chapter Mice Species. The SONY VAIO C1 series includes some models, which are based on the first dedicated mobile CPU, the CRUSOE. The CRUSOE is manufactured by
There is also a VAIO C1 related Linux mailing list, too <linux-c1_at_gnu.org>.
The
* * *
#  I.5. Toshiba
_Klibreta_ , too.
Mailing lists:
Toshiba itself offers now
* * *
#  Appendix J. Credits
I would like to thank the many people who assisted with corrections and suggestions. Their contributions have made this work far better than I could ever have done alone. Especially I would like to thank:
  * First of all Kenneth E. Harker , from his page
  * The other authors from [THE LINUX DOCUMENTATION PROJECT - TLDP](http://tldp.org/) .
  * The members of the
  * The members of the Linux-Laptop Mailing List.
  * The members of the Debian-Laptop Mailing List.
  * The members of the SuSE-Laptop Mailing List.
  * The visitors and contributors of my
  * Cedric Adjih , wrote the chapter about the NeoMagic chipset.
  * Amlaukka
  * Michele Andreoli, maintainer of
  * Ben Attias .
  * Gerd Bavendiek ,
  * John Beimler , provided the URL of **photopc**.
  * Ludger Berse .
  * Stephane Bortzmeyer for his suggestions about email with UUCP, the use of CVS or related tools to synchronize two machines, and the **noatime** mount option.
  * Lionel, "trollhunter" Bouchpan-Lerust-Juery
  * Felix Braun .
  * David Burley
  * David Chien
  * Sven Crouse for information about touchpads
  * Eric wrote how to transfer pictures from a digital camera.
  * Brian Edmonds
  * Peter Englmaier , provided the chapter about a sophisticated email setup.
  * Joel Eriksson , for information about Atari laptops.
  * Heiko Ettelbrueck
  * Gledson Evers , started the Portuguese translation.
  * Klaus Franken .
  * Bill Gjestvang .
  * Alessandro Grillo , started the Italian translation.
  * Sven Grounsell
  * Mikael Gueck
  * Marcus Hagn has written some powersaving tweaks
  * W. Wade, Hampton , did much of spell, grammar and style checking and added many valuable information.
  * Sebastian Henschel prepared some sections of the PDA chapter and more
  * David Hinds, the maintainer of the
  * Karsten Hopp
  * Scott Hurring
  * JK
  * Uwe SV Kubosch , hints about Amiga
  * Jeremy D. Impson provided instructions about installing on a Toshiba Libretto 50CT
  * Adrian D. Jensen , provided some notes on removable hard disks
  * Steven G. Johnson , provided most of the information about Apple/Macintosh m68k machines and LinuxPPC on the PowerBook.
  * Dan Kegel , pointed me to the Toshiba Linux page.
  * Gilles Lamiral for providing the PLIP Install-HOWTO.
  * Sian Leitch , suggestions on style
  * [Hardware-HOWTO](http://tldp.org/HOWTO/Hardware-HOWTO/).
  * Anderson MacKay ,
  * Nat Makarevitch gave suggestions how to use **noflushd**
  * Jari Malinen, for support with HUT Mobile IP (now Dynamics Mobile IP).
  * Paul Mansfield , ICQ:13391313 information about removable hard disks
  * Stefan Martig .
  * Marco Michna , from
  * Harald Milz , from
  * Emerson, Tom # El Monte , for his idea about laptop bags.
  * Dan Mueth author of the
  * Louis A. Mulieri , information about removable hard disks
  * Nathan Myers , from
  * Leandro Noferin , for proofreading the _italian_ parts.
  * Ulrich Oelmann , gave valuable additions about the installation with **muLinux**.
  * Michael Opdenacker, for tips and tricks about PDAs and moral support
  * Federico Pellegrin , provided the chapter about installation from a parallel port CD drive
  * Sean 'Shaleh' Perry, , Debian maintainer of **anacron** and other packages, for Debian support.
  * Igor Pesando .
  * Benjamin C. Pierce
  * Lucio Pileggi , provided information about the Siemens S25 cellular phone.
  * Jacek Pliszka , provided information about miscellaneous topics, e.g. USB devices, external floppy and CD drives.
  * Lorn 'ljp' Potter (Qtopia Community Liaison) gave some improvements for the PDA chapter
  * Steve Rader .
  * Bruce Richardson
  * Pete Rotheroe
  * Simon Rowe
  * Frank Schneider .
  * Hans Schou , FlashPath for Linux
  * Martin "Joey" Schulze
  * Chandran Shukla .
  * Fabio Sirna provided a script to show the battery status in console mode with ACPI
  * Adam Spiers .
  * Peter Sprenger .
  * Bill Staehle
  * Leon Stok
  * Christian Stolte
  * Peter Teuben , for some suggestions about hard disks.
  * Bob Toxin .
  * Thomas Traber .
  * Geert Van der Plas , provided information about the touchpad driver included in the GPM.
  * Marcel Ovidiu Vlad .
  * Michael Wiedmann ,
  * Tim Williams , pointed me to System Commander 2000 partition manager
  * Serge Winitzki wrote some recommendations for noise reduction and/or energy saving
  * Richard Worwood


Sorry, but probably I have forgotten to mention everybody who helped.
* * *
#  Appendix K. Copyrights
| _GNU GPL "The source will be with you ... always!"_
---|---
| _N.N._
* * *
#  K.1. Copyrights
For all chapters except "Lectures, Presentations, Animations and Slideshows" permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation; with the Invariant Sections being "Preface" and "Credits", with the Front-Cover Texts being "Linux on the Road - the First Book on Mobile Linux", and with the Back-Cover Texts being the section "About the Author". A copy of the license is included in the section entitled "GNU Free Documentation License".
Copyright for the included pictures belongs to their respective owners.
* * *
#  K.2. GNU Free Documentation License - GFDL
Version 1.1, March 2000
Copyright (C) 2000 Free Software Foundation, Inc. 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.
* * *
##  K.2.1. 0. PREAMBLE
The purpose of this License is to make a manual, textbook, or other written document "free" in the sense of freedom: to assure everyone the effective freedom to copy and redistribute it, with or without modifying it, either commercially or noncommercially. Secondarily, this License preserves for the author and publisher a way to get credit for their work, while not being considered responsible for modifications made by others.
This License is a kind of "copyleft", which means that derivative works of the document must themselves be free in the same sense. It complements the GNU General Public License, which is a copyleft license designed for free software.
We have designed this License in order to use it for manuals for free software, because free software needs free documentation: a free program should come with manuals providing the same freedoms that the software does. But this License is not limited to software manuals; it can be used for any textual work, regardless of subject matter or whether it is published as a printed book. We recommend this License principally for works whose purpose is instruction or reference.
* * *
##  K.2.2. 1. APPLICABILITY AND DEFINITIONS
This License applies to any manual or other work that contains a notice placed by the copyright holder saying it can be distributed under the terms of this License. The "Document", below, refers to any such manual or work. Any member of the public is a licensee, and is addressed as "you".
A "Modified Version" of the Document means any work containing the Document or a portion of it, either copied verbatim, or with modifications and/or translated into another language.
A "Secondary Section" is a named appendix or a front-matter section of the Document that deals exclusively with the relationship of the publishers or authors of the Document to the Document's overall subject (or to related matters) and contains nothing that could fall directly within that overall subject. (For example, if the Document is in part a textbook of mathematics, a Secondary Section may not explain any mathematics.) The relationship could be a matter of historical connection with the subject or with related matters, or of legal, commercial, philosophical, ethical or political position regarding them.
The "Invariant Sections" are certain Secondary Sections whose titles are designated, as being those of Invariant Sections, in the notice that says that the Document is released under this License.
The "Cover Texts" are certain short passages of text that are listed, as Front-Cover Texts or Back-Cover Texts, in the notice that says that the Document is released under this License.
A "Transparent" copy of the Document means a machine-readable copy, represented in a format whose specification is available to the general public, whose contents can be viewed and edited directly and straightforwardly with generic text editors or (for images composed of pixels) generic paint programs or (for drawings) some widely available drawing editor, and that is suitable for input to text formatters or for automatic translation to a variety of formats suitable for input to text formatters. A copy made in an otherwise Transparent file format whose markup has been designed to thwart or discourage subsequent modification by readers is not Transparent. A copy that is not "Transparent" is called "Opaque".
Examples of suitable formats for Transparent copies include plain ASCII without markup, Texinfo input format, LaTeX input format, SGML or XML using a publicly available DTD, and standard-conforming simple HTML designed for human modification. Opaque formats include PostScript, PDF, proprietary formats that can be read and edited only by proprietary word processors, SGML or XML for which the DTD and/or processing tools are not generally available, and the machine-generated HTML produced by some word processors for output purposes only.
The "Title Page" means, for a printed book, the title page itself, plus such following pages as are needed to hold, legibly, the material this License requires to appear in the title page. For works in formats which do not have any title page as such, "Title Page" means the text near the most prominent appearance of the work's title, preceding the beginning of the body of the text.
* * *
##  K.2.3. 2. VERBATIM COPYING
You may copy and distribute the Document in any medium, either commercially or noncommercially, provided that this License, the copyright notices, and the license notice saying this License applies to the Document are reproduced in all copies, and that you add no other conditions whatsoever to those of this License. You may not use technical measures to obstruct or control the reading or further copying of the copies you make or distribute. However, you may accept compensation in exchange for copies. If you distribute a large enough number of copies you must also follow the conditions in section 3.
You may also lend copies, under the same conditions stated above, and you may publicly display copies.
* * *
##  K.2.4. 3. COPYING IN QUANTITY
If you publish printed copies of the Document numbering more than 100, and the Document's license notice requires Cover Texts, you must enclose the copies in covers that carry, clearly and legibly, all these Cover Texts: Front-Cover Texts on the front cover, and Back-Cover Texts on the back cover. Both covers must also clearly and legibly identify you as the publisher of these copies. The front cover must present the full title with all words of the title equally prominent and visible. You may add other material on the covers in addition. Copying with changes limited to the covers, as long as they preserve the title of the Document and satisfy these conditions, can be treated as verbatim copying in other respects.
If the required texts for either cover are too voluminous to fit legibly, you should put the first ones listed (as many as fit reasonably) on the actual cover, and continue the rest onto adjacent pages.
If you publish or distribute Opaque copies of the Document numbering more than 100, you must either include a machine-readable Transparent copy along with each Opaque copy, or state in or with each Opaque copy a publicly-accessible computer-network location containing a complete Transparent copy of the Document, free of added material, which the general network-using public has access to download anonymously at no charge using public-standard network protocols. If you use the latter option, you must take reasonably prudent steps, when you begin distribution of Opaque copies in quantity, to ensure that this Transparent copy will remain thus accessible at the stated location until at least one year after the last time you distribute an Opaque copy (directly or through your agents or retailers) of that edition to the public.
It is requested, but not required, that you contact the authors of the Document well before redistributing any large number of copies, to give them a chance to provide you with an updated version of the Document.
* * *
##  K.2.5. 4. MODIFICATIONS
You may copy and distribute a Modified Version of the Document under the conditions of sections 2 and 3 above, provided that you release the Modified Version under precisely this License, with the Modified Version filling the role of the Document, thus licensing distribution and modification of the Modified Version to whoever possesses a copy of it. In addition, you must do these things in the Modified Version:
A. Use in the Title Page (and on the covers, if any) a title distinct from that of the Document, and from those of previous versions (which should, if there were any, be listed in the History section of the Document). You may use the same title as a previous version if the original publisher of that version gives permission.
B. List on the Title Page, as authors, one or more persons or entities responsible for authorship of the modifications in the Modified Version, together with at least five of the principal authors of the Document (all of its principal authors, if it has less than five).
C. State on the Title page the name of the publisher of the Modified Version, as the publisher.
D. Preserve all the copyright notices of the Document.
E. Add an appropriate copyright notice for your modifications adjacent to the other copyright notices.
F. Include, immediately after the copyright notices, a license notice giving the public permission to use the Modified Version under the terms of this License, in the form shown in the Addendum below.
G. Preserve in that license notice the full lists of Invariant Sections and required Cover Texts given in the Document's license notice.
H. Include an unaltered copy of this License.
I. Preserve the section entitled "History", and its title, and add to it an item stating at least the title, year, new authors, and publisher of the Modified Version as given on the Title Page. If there is no section entitled "History" in the Document, create one stating the title, year, authors, and publisher of the Document as given on its Title Page, then add an item describing the Modified Version as stated in the previous sentence.
J. Preserve the network location, if any, given in the Document for public access to a Transparent copy of the Document, and likewise the network locations given in the Document for previous versions it was based on. These may be placed in the "History" section. You may omit a network location for a work that was published at least four years before the Document itself, or if the original publisher of the version it refers to gives permission.
K. In any section entitled "Acknowledgements" or "Dedications", preserve the section's title, and preserve in the section all the substance and tone of each of the contributor acknowledgements and/or dedications given therein.
L. Preserve all the Invariant Sections of the Document, unaltered in their text and in their titles. Section numbers or the equivalent are not considered part of the section titles.
M. Delete any section entitled "Endorsements". Such a section may not be included in the Modified Version.
N. Do not retitle any existing section as "Endorsements" or to conflict in title with any Invariant Section.
If the Modified Version includes new front-matter sections or appendices that qualify as Secondary Sections and contain no material copied from the Document, you may at your option designate some or all of these sections as invariant. To do this, add their titles to the list of Invariant Sections in the Modified Version's license notice. These titles must be distinct from any other section titles.
You may add a section entitled "Endorsements", provided it contains nothing but endorsements of your Modified Version by various parties for example, statements of peer review or that the text has been approved by an organization as the authoritative definition of a standard.
You may add a passage of up to five words as a Front-Cover Text, and a passage of up to 25 words as a Back-Cover Text, to the end of the list of Cover Texts in the Modified Version. Only one passage of Front-Cover Text and one of Back-Cover Text may be added by (or through arrangements made by) any one entity. If the Document already includes a cover text for the same cover, previously added by you or by arrangement made by the same entity you are acting on behalf of, you may not add another; but you may replace the old one, on explicit permission from the previous publisher that added the old one.
The author(s) and publisher(s) of the Document do not by this License give permission to use their names for publicity for or to assert or imply endorsement of any Modified Version.
* * *
##  K.2.6. 5. COMBINING DOCUMENTS
You may combine the Document with other documents released under this License, under the terms defined in section 4 above for modified versions, provided that you include in the combination all of the Invariant Sections of all of the original documents, unmodified, and list them all as Invariant Sections of your combined work in its license notice.
The combined work need only contain one copy of this License, and multiple identical Invariant Sections may be replaced with a single copy. If there are multiple Invariant Sections with the same name but different contents, make the title of each such section unique by adding at the end of it, in parentheses, the name of the original author or publisher of that section if known, or else a unique number. Make the same adjustment to the section titles in the list of Invariant Sections in the license notice of the combined work.
In the combination, you must combine any sections entitled "History" in the various original documents, forming one section entitled "History"; likewise combine any sections entitled "Acknowledgements", and any sections entitled "Dedications". You must delete all sections entitled "Endorsements."
* * *
##  K.2.7. 6. COLLECTIONS OF DOCUMENTS
You may make a collection consisting of the Document and other documents released under this License, and replace the individual copies of this License in the various documents with a single copy that is included in the collection, provided that you follow the rules of this License for verbatim copying of each of the documents in all other respects.
You may extract a single document from such a collection, and distribute it individually under this License, provided you insert a copy of this License into the extracted document, and follow this License in all other respects regarding verbatim copying of that document.
* * *
##  K.2.8. 7. AGGREGATION WITH INDEPENDENT WORKS
A compilation of the Document or its derivatives with other separate and independent documents or works, in or on a volume of a storage or distribution medium, does not as a whole count as a Modified Version of the Document, provided no compilation copyright is claimed for the compilation. Such a compilation is called an "aggregate", and this License does not apply to the other self-contained works thus compiled with the Document, on account of their being thus compiled, if they are not themselves derivative works of the Document.
If the Cover Text requirement of section 3 is applicable to these copies of the Document, then if the Document is less than one quarter of the entire aggregate, the Document's Cover Texts may be placed on covers that surround only the Document within the aggregate. Otherwise they must appear on covers around the whole aggregate.
* * *
##  K.2.9. 8. TRANSLATION
Translation is considered a kind of modification, so you may distribute translations of the Document under the terms of section 4. Replacing Invariant Sections with translations requires special permission from their copyright holders, but you may include translations of some or all Invariant Sections in addition to the original versions of these Invariant Sections. You may include a translation of this License provided that you also include the original English version of this License. In case of a disagreement between the translation and the original English version of this License, the original English version will prevail.
* * *
##  K.2.10. 9. TERMINATION
You may not copy, modify, sublicense, or distribute the Document except as expressly provided for under this License. Any other attempt to copy, modify, sublicense or distribute the Document is void, and will automatically terminate your rights under this License. However, parties who have received copies, or rights, from you under this License will not have their licenses terminated so long as such parties remain in full compliance.
* * *
##  K.2.11. 10. FUTURE REVISIONS OF THIS LICENSE
The Free Software Foundation may publish new, revised versions of the GNU Free Documentation License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. See http://www.gnu.org/copyleft/.
Each version of the License is given a distinguishing version number. If the Document specifies that a particular numbered version of this License "or any later version" applies to it, you have the option of following the terms and conditions either of that specified version or of any later version that has been published (not as a draft) by the Free Software Foundation. If the Document does not specify a version number of this License, you may choose any version ever published (not as a draft) by the Free Software Foundation.
