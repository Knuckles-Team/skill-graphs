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
