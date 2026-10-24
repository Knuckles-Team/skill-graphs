#  Linux on the Road
## Linux with Laptops, Notebooks, PDAs, Mobile Phones and Other Portable Devices
###  Werner Heuser

`<`

Linux Mobile Edition Edition
Version 3.22

TuxMobil

Berlin
[Copyright](https://tldp.org/LDP/Mobile-Guide/html/ln21.html) © 2000-2011 Werner Heuser
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
* * *

**Table of Contents**


[Preface](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p0-preface.html)


1. [About the Author](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p0c1s1-about-the-author.html)


2. [Sponsoring](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p0c1s2-sponsoring.html)


3. [About the Document](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p0c1s3-about-the-document.html)


4. [Contact](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p0c1s4-contact.html)


5. [Disclaimer and Trademarks](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p0c1s5-disclaimer-and-trademarks.html)


I. [Laptops and Notebooks](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p1-getting-started.html)


1. [Which Laptop to Buy?](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p1c1-which-laptop-to-buy.html)


2. [Laptop Distributions](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p1c2-laptop-distribution.html)


3. [Installation](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p1c3-installation.html)


II. [Handheld Devices - Personal Digital Assistants (PDAs)](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p3-handheld-devices-pdas.html)


4. [Palmtops, Personal Digital Assistants - PDAs, Handheld PCs - HPCs](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p3c1-palmtops-pdas-handhelds.html)


5. [History of Linux on PDAs](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p3c2-linux-pdas-history.html)


6. [Linux PDAs](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p3c2-linux-pdas.html)


7. [Non-Linux PDAs - Ports and Tools](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p3c2-linux-for-pdas-ports-and-tools.html)


8. [Connectivity](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p3c4-connectivity.html)


III. [Tablet PCs / Pen PCs](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p4-tablet-pc.html)


9. [Tablet PCs / Pen PCs](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p4c1-tablet-intro.html)


IV. [Mobile (Cellular) Phones, Pagers, Calculators, Digital Cameras, Wearable Computing](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p4-cell-phones.html)


10. [Mobile (Cellular) Phones, Pagers](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p4c1-cell-phones.html)


11. [Calculators, Digital Cameras, Wearable Computing](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p4c1-wearables.html)


V. [Mobile Hardware in Detail](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p2-mobile-hardware.html)


12. [Hardware in Detail: CPU, Display, Keyboard, Sound and More](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p2c1-hardware-in-detail.html)


13. [Accessories: PCMCIA, USB and Other External Extensions](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p2c2-accessories.html)


VI. [Kernel](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p5-kernel.html)


14. [Kernel History](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p5c1-kernel-history.html)


VII. [On the Road](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p5-on-the-road.html)


15. [Different Environments](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p5c1-different-environments.html)


16. [Solutions with Mobile Computers](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p5c2-solutions-with-laptops.html)


VIII. [Appendix](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p6-appendix.html)


A. [Other Operating Systems](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-a1-other-operating-systems.html)


B. [Other Resources](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-a2-other-resources.html)


C. [Repairing the Hardware](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-a3-repairing-the-hardware.html)


D. [Survey about Micro Linuxes](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-a4-survey-micro-linuxes.html)


E. [Dealing with Limited Resources or Tuning the System](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-a5-limited-resources.html)


F. [Ecology and Laptops](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-a6-ecology.html)


G. [NeoMagic Graphics Chipset Series NM20xx](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-a6-neomagic-chip.html)


H. [Annotated Bibliography: Books For Linux Nomads](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-a7-annotated-bibliography.html)


I. [Resources for Specific Laptop Brands](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-a8-resources-specific-laptops.html)


J. [Credits](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-a10-credits.html)


K. [Copyrights](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-a11-copyrights.html)


**List of Tables**


12-1. [Arguments for the **-t** and **-R** option of **gpm**.](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p2c1s7-pointing-devices.html#AEN2613)


**List of Figures**


6-1. [Screenshot of the YOPY PDA](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p3c2s8-yopy.html#AEN1188)


6-2. [Screenshot of the SHARP Zaurus SL-5500 PDA.](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p3c2s8-zaurus.html#AEN1201)


7-1. [Screenshot of the HELIO PDA.](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p3c2s2-helio.html#AEN1404)


7-2. [Screenshot of the iPAQ PDA.](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p3c2s3-ipaq.html#AEN1426)


7-3. [Screenshot of the PALM-Pilot emulator POSE.](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p3c2s6-palm-pilot.html#AEN1480)


12-1. [Screenshot of cardinfo](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p2c1s2-pcmcia-controller.html#AEN1949)


E-1. [Screenshot of **blackbox**.](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p6a5s9-tiny-applications.html#AEN5435)

* * *
|  | [Next](https://tldp.org/LDP/Mobile-Guide/html/mobile-guide-p0-preface.html)
---|---|---
|  | Preface
