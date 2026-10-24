     ________________________________________________________________

12.6.5.1. Tools

   The [http://www.stud.uni-hamburg.de/users/lennart/projects/atitvout/]
   atitvout utility may be used for executing several configuration
   commands for the TV Out connector of ATI Rage Mobility P/M graphics
   boards under GNU/Linux on x86. It is intended primarily to enable TV
   Out support after bootup and for switching the used TV standard from
   NTSC to PAL.

   [http://www.probo.com/timr/savage40.html] s3switch will allow you to
   switch your display between the various output devices supported by
   the Savage (CRT, LCD, TV).

   [http://sourceforge.net/projects/nv-tv-out] nv-tv-out is a tool to
   enable TV-Out on Linux for NVidia cards. It does not need the kernel,
   supports multiple TV encoder chips. You may use all the features of
   the chip, down to direct register access, and all resolutions and
   sizes the chip supports.

   [http://www16.plala.or.jp/mano-a-mano/i810switch.html] i810switch is
   an utility for switching the LCD and external VGA displays on and
   off, with almost every graphics chip from Intel's i8xx family,
   including Centrino.

   [http://sourceforge.net/projects/i855crt] i855crt is an userspace
   driver that can enable the CRT out (port for external monitor) on
   Intel 855GM based laptops.
     ________________________________________________________________

12.6.5.2. Solutions

   Klaus Weidner has described a
   [http://mailman.linux-thinkpad.org/pipermail/linux-thinkpad/2003-Nove
   mber/013701.html] Dual monitor setup without using xinerama, but
   x2vnc instead. This approach allows to add and remove the second
   monitor dynamically without reconfiguring or restarting anything.
     ________________________________________________________________

12.6.6. Power Management for Graphics Cards

   The uptime on batteries can be improved by enabling the power
   management features of the graphics card. There are tools available
   to change the clock frequency and to shut down the backlight of the
   display. Usually these tools are specific for a graphics card or a
   graphics card manufacturer. Here are some techniques for graphics
   cards made by ATI.

   The proprietary fglrx driver from ATI needs to be enabled by adding
   the PowerState option to the Device Section in the /etc/X11/xorg.conf
   X11 configuration file:

Section "Device"
Identifier "aticonfig-Device[0]"
Driver "fglrx"
Option "PowerState" "1"
EndSection

   After rebooting or re-starting X11 you can start the power save mode
   with the command aticonfig --set-powerstate=1 --effective=now. Use
   aticonfig --list-powerstates to get all available powerstates.

   For ATI Radeon graphics cards the rovclock tool can be used to save
   power e.g. rovclock -c 80 -m 80 to use only 80MHz chip and memory
   frequency. The command radeontool light off switches the backlight
   off, if closing the lid or using an extra key is not an option.

   The [http://lkml.org/lkml/2006/10/9/83] ACPI backlight driver by
   Holger Macht in 2.6.x for IBM, Toshiba, ASUS laptops adds support for
   the generic backlight interface below /sys/class/backlight. The patch
   keeps the procfs brightness handling for backward compatibility. For
   this to archive, the patch adds two generic functions brightness_get
   and brightness_set to be used both by the procfs related and the
   sysfs related methods.
     ________________________________________________________________

12.6.7. Miscellaneous

   Sometimes you may encounter a display not working properly in text
   mode. Currently I don't have any recommendations, please see
   [http://tldp.org/HOWTO/Keyboard-and-Console-HOWTO.html]
   Keyboard-and-Console-HOWTO .

   Take care of the backlight as far as I know this device can only bear
   a limited number of uptime circles. So avoid using screensavers too
   much.

   For problems with X Windows and APM please see the APM chapter.

   [http://www.srcf.ucam.org/~mjg59/vbetool/] vbetool uses LRMI in order
   to run code from the video BIOS. Currently, it is able to alter DPMS
   states, save/restore video card state, and attempt to initialize the
   video card from scratch. It exists primarily in order to increase the
   chances of successfully recovering video state after an ACPI S3
   suspend-to-RAM.
     ________________________________________________________________

12.7. DVI Port

   As far as I know DVI ports don't work with Linux yet. But anyway here
   are links to installation reports about
   [http://tuxmobil.org/laptop_dvi_linux.html] Linux on laptops and
   notebooks with DVI ports.
     ________________________________________________________________

12.8. Video Port / ZV Port

   Some high end laptops come with a video or ZV port (NTSC/PAL). Since
   I don't have a laptop with a ZV or video port yet, I can provide only
   some URLs [http://www.thp.uni-koeln.de/~rjkm/linux/bttv.html] BTTV
   (driver) [http://www.mathematik.uni-kl.de/~wenk/xwintv.html] xwintv
   (tvviewer). For further information see
   [http://www.exploits.org/v4l/] Video4Linux . To collect information
   about laptops with video port I have setup a page at
   [http://tuxmobil.org/hardware.html] TuxMobil - Hardware .
   Alternatively to the ZV port you might use the USB port.
     ________________________________________________________________

12.9. LCD Display

   This chapter isn't ready yet, it will contain information about the
   lifetime of backlights, differences between CRT and LCD displays,
   anti-aliasing with LCD displays, the ISO 13406-2 standard about pixel
   defects, a survey of common resolutions: VGA, SVGA, XGA and more
   soon. See also the screensaver chapter and the touchscreen section in
   the chapter Part III in Linux on the Road Tablet PC and PDA.
     ________________________________________________________________

12.9.1. Laptop Displays

12.9.1.1. Applications

   [http://www.brouhaha.com/~eric/software/lcdtest/] lcdtest is a
   utility to display LCD monitor test patterns. It may be useful in
   finding pixels that are stuck on or off. lcdtest uses the SDL
   library, and has only been tested on Linux with X, but may work on
   other platforms.

   [http://ddccontrol.sourceforge.net/] DDCcontrol is a program used to
   control monitor parameters, like brightness and contrast, by
   software, i.e. without using the OSD (On Screen Display) and the
   buttons in front of the monitor.
     ________________________________________________________________

12.9.1.2. Fonts

   [http://www.iki.fi/too/sw/fat8x16-x-font.readme] fat8x16-x-font is a
   8x16 pixel fixed width font to be used in physically small but high
   resolution displays. Such displays can be found for example in
   notebook computers with 1400x1050 and 1600x1200 14" displays.
     ________________________________________________________________

12.9.2. PDA Displays

   [http://userpage.fu-berlin.de/~cantsin/homepage/computing/hacks/pxl20
   00/README.html] pxl2000 is a free ISO 8859-15 (i.e. ISO 8859-1 with
   Euro symbol) encoded monowidth dot matrix typeface for the X Window
   system (X11). It is currently available in nine sizes: 4x8, 5x10,
   6x12, 7x14, 8x16, 9x18, 10x20, 11x22 and 12x24 pixels. It's design
   objectives are:

     * Readability; fitness to be used as a default screen font,
       especially on reverse-color X11 terminals
     * Optimization for program code through visually distinct
       characters L, l, 1, 7, |, I, i and 0, O and more.
     * Complete ISO 8859-15 character set.
     * Many point sizes to ensure optical consistency across different
       computers with different screen resolutions (encompassing
       anything from PDA displays to 20" screens).
     * Fitness for displaying ASCII art and codework/code poetry, from
       viewing graphics in aview, watching TV in ttv and DVDs in mplayer
       with -vo aa to reading mailinglists like _arc.hive_, 7-11 and
       writing in mutt.
     * Clean, minimalist visual design; no serifs, a square minuscule
       base matrix, rounded edges. This is a computer terminal font; it
       should not look like a low-res imitation of print type.

   The author Florian Cramer employs this font in his "anti-desktop"
   setup consisting of the ratpoison window manager and GNU screen
   inside an rxvt terminal (with reverse color and no scrollbars),
   similar to what is described in this
   [http://palm.freshmeat.net/articles/view/581/] FreshMeat article .
     ________________________________________________________________

12.10. Sound

12.10.1. Linux Compatibility Check

   The only way I know to check this, is to compile the different sound
   drivers into the kernel and check whether they are detected or not.
   The best way to do so, is to compile them as modules because it's
   easier to load different parameters such as interrupts and IO ports
   this way. For the 2.2.x kernels, read
   /usr/src/linux/Documentation/sound/Introduction by Wade Hampton. This
   document may help you get started with sound. Also, you might try one
   of the commercial sound drivers mentionend below. To check whether
   sound works or not you may try e.g. xmms and one of the sounds
   provided in /usr/share/sounds.
     ________________________________________________________________

12.10.2. Related Documentation

    1. [http://www.tldp.org/] Sound-HOWTO
    2. [http://www.tldp.org/] Visual-Bell-mini-HOWTO
    3. You may find also some good sound HOWTOs at the
       [http://www.djcj.org/LAU/guide/] Linux Audio Users Guide - LAU
     ________________________________________________________________

12.10.3. Survey Sound Drivers

    1. ALSA [http://www.alsa-project.org/] Advanced Linux Sound
       Architecture . The Advanced Linux Sound Architecture aims to: be
       a fully-modularized sound driver which supports kerneld/kmod,
       ensure compatibility with most binary OSS/Lite applications,
       create an ALSA Library (C,C++) which covers the ALSA Kernel API
       for applications, and create ALSA Manager, an interactive
       configuration program for the driver. With Kernel 2.6 these
       modules will be part of the Linux Kernel.
    2. UNIX Sound System Lite / OSS provides commercial sound card
       drivers for most popular sound cards under Linux. These drivers
       support digital audio, MIDI, Synthesizers and mixers found on
       sound cards. These sound drivers comply with the Open Sound
       System API specification. OSS provides a user-friendly GUI which
       makes the installation of sound drivers and configuration of
       sound cards very simple. OSS supports over 200 brand name sound
       cards. OSS drivers provide automatic sound card detection,
       Plug-n-Play support, support for PCI audio soundcards and
       support.
    3. As a last resort you may try the speaker module pcsnd, which
       tries to emulate a soundcard.
     ________________________________________________________________

12.10.4. Additional Soundcards

   [http://www.digigram.com/products/VXpocket.html] VXPocket looks like
   a finally medium2high-end soundcard solution for onboardwise badly
   equipped laptops. Note: I didn't check whether this is a PCMCIA card
   or not. PCMCIA sound cards are probably not supported.

   Also USB may be an alternative. Most USB audio devices are supported
   by recent kernels. An example is Labtec Axis 712 Stereo Headset
   (headphones and microphone) which works in full-duplex mode. For more
   info about this and other Linux-compatible USB audio devices see the
   [http://www.qbik.ch/usb/devices/] USB Survey and my
   [http://tuxmobil.org/usb_linux.html] Mobile USB Linux Hardware Survey
   .
     ________________________________________________________________

12.10.5. External and Internal CD Drives

   For playing CDs/DVDs from an external or internal CD/DVD drive, see
   chapter Section 12.32 CD/DVD Drive below.
     ________________________________________________________________

12.11. Keyboard

12.11.1. Linux Compatibility Check

   Usually there are no problems with Linux and the keyboard. Though
   there are two minor caveats: First the setleds program might not
   work. Second the key mapping might not fit your needs. Some UNIX
   users and vi users expect to find the <CONTROL> key to the left of
   the <A> key. Many PC-type keyboards have the <CAPS-LOCK> key there.
   You may use xmodmap or loadkeys to re-map the keyboard. Some laptops
   (e.g., Toshiba) allow you to swap the <CAPS-LOCK> and <CONTROL> keys.
   Mark Alexander offered this solution in the linux-laptop mailing
   list: On RedHat, it's a one-line patch to
   /usr/lib/kbd/keytables/us.map , or whatever file is referenced in
   /etc/sysconfig/keyboard:

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
     ________________________________________________________________

12.11.2. External (Second) Keyboard

   A second (or external) keyboard can be attached using the PS/2 port
   (I suppose this is not possible via the serial port, since there is
   no keyboard controller for the serial port) or via USB port. Also
   there is one laptop with a detachable keyboard the Siemens Scenic
   Mobile 800. This machine uses an infrared connection to the keyboard,
   but I don't know whether this works with Linux.
     ________________________________________________________________

12.11.2.1. External USB Keyboard Configuration

   You may not need any operating system support at all to use a USB
   keyboard if you have a PC architecture. There are several BIOS
   available where the BIOS can provide USB support from a keyboard
   plugged into the root hub on the motherboard. This may or may not
   work through other hubs and does not normally work with add-in
   boards, so you might want to add in support anyway. You definitely
   want to add keyboard support if you activate operating system
   support, as the Linux USB support will disable the BIOS support. You
   also need to use Linux USB keyboard support if you want to use any of
   the "multimedia" types keys that are provided with some USB
   keyboards.

   In the kernel configuration stage, you need to turn on USB Human
   Interface Device (HID) support and Keyboard support. Do not turn on
   USB HIDBP Keyboard support. Perform the normal kernel rebuild and
   installation steps. If you are installing as modules, you need to
   load the hid.o, input.o and keybdev.o modules.

   Check the kernel logs to ensure that your keyboard is being correctly
   sensed by the kernel.

   At this point, you should be able to use your USB keyboard as a
   normal keyboard. Be aware that LILO is not USB aware, and that unless
   your BIOS supports a legacy USB keyboard, you may not be able to
   select a non-default boot image using the USB keyboard. I have
   personally used a USB keyboard (and USB mouse) and experienced no
   problems.
     ________________________________________________________________

12.11.2.2. External PS/2 Keyboard

   Warning

   Don't plug the external keyboard in while the laptop is booted, or
   plug the mouse in the keyboard port and the keyboard in the mouse
   port. On a Toshiba, this caused one user to have to completely
   shutdown the laptop, remove the keyboard/mouse, and do a cold reboot.

   For PS/2 ports there is a so called Y-Cable available, which makes it
   possible to use external mouse and external keyboard at the same time
   if your laptop supports this feature.

   [http://linuxconsole.sourceforge.net/input/adapters.html] Parport to
   AUX port adapter In some cases one kbd port and one aux port is not
   enough and you may want to add another keyboard or mouse. You can use
   this adapter, together with the parkbd module for that.

   On some laptops a splitter works to allow both mouse and keyboard to
   be plugged in; on others it doesn't work at all. If you want to use
   both, you better check that it works.
     ________________________________________________________________

12.12. Extra Keys / Hot Keys

12.12.1. Related Documentation

    1. [http://tldp.org/HOWTO/Keyboard-and-Console-HOWTO.html]
       Keyboard-and-Console-HOWTO
     ________________________________________________________________

12.12.2. Utilities

   Some laptops offer extra buttons, e.g. - internet, mail keys, or zone
   keys. If the Linux kernel and XFree86/X.org generate key codes for
   them, hotkeys or just plain xmodmap (see the man page of this X11
   programm for details) may be helpful. If Linux doesn't know about the
   keys, you'll have to patch the kernel first. Though I'm not quite
   sure some tools don't seem to require this, I don't understand how it
   works yet. You may also use [http://www.geocities.com/wmalms/] xhkeys
   . This tool allows you to assign an action to any key that is
   otherwise unused in X (such as the "menu" key on a 105 key keyboard,
   extra keys on some keyboard models, or odd keys on laptops). The
   action assigned to a key or key combination (key and modifiers) can
   be a builtin operation, a call to an external application, the
   sending of a key event (simulating a key press/release), or the
   sending of a mouse button event (simulating a button press/release).

   Tip

   To get information about unknown keyboard or mouse events you may use
   showkey and mev (the last one is from the gpm package) on a console
   screen. But some of the extra keys are not found with these tools.

   [http://keytouch.sourceforge.net/] keyTouch makes it possible to
   easily configure the extra function keys of a keyboard (like
   multimedia keys). It allows the user to define which program will be
   executed when a key is pressed. By using keyTouch-editor the user can
   easily create a keyboard file for his or her laptop to get the laptop
   supported.

   akdaemon is a userland daemon to invoke "the fun keys" by accessing a
   dev node offered by the complementary
   [http://sourceforge.net/projects/akdaemon/] kernel patch or the
   [http://home.zonnet.nl/vanrein/linux/funkey/] funkey programm .

   The [http://ypwong.org/hotkeys/] hotkeys package is supposed to
   listen for those multimedia keys.

   Special ("easy access") buttons are supported by
   [http://lineak.sourceforge.net] LinEAK . Here is an example
   lineakd.conf file:
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

   [http://hocwp.free.fr/xbindkeys/xbindkeys.html] xbindkeys is a
   program that associates keys or mouse buttons to shell commands under
   X. After a little configuration, it can start many commands with the
   keyboard (e.g. control+alt+x starts an xterm) or with the mouse
   buttons.

   [http://www.hadess.net/misc-code.php3] ACME is a small GNOME tool to
   make use of the multimedia buttons present on most laptops and
   Internet keyboards: Volume, Brightness, Power, Eject, My Home,
   Search, E-Mail, Sleep, Screensaver, Finance, WWW, Calculator, Record,
   Close Window, Shade Window, Play, Stop, Pause, Previous, Next,
   Groups, Media, Refresh, and Help buttons. It works on all the
   platforms GNOME supports (laptops and PCs). It uses either OSS or
   ALSA for Volume control.

   For some laptop series there are Linux utilities available to control
   special hotkeys and other features.

     * [http://www.buzzard.me.uk/toshiba/index.html] toshutils by
       Jonathan Buzzard for some Toshiba models.
     * [http://sourceforge.net/projects/tclkeymon/] Tclkeymon is a
       daemon for Toshiba laptops that use ACPI and the Toshiba ACPI
       extensions. It monitors function keys and Toshiba-specific
       buttons (including the CD player buttons and the state of the
       laptop lid) and responds appropriately.
     * [http://tpctl.sourceforge.net] tpctl IBM ThinkPad configuration
       tools for Linux by Thomas Hood.
     * [http://savannah.nongnu.org/projects/tpb/] ThinkPad Buttons
       enables the special keys that are found on the keyboard of an IBM
       ThinkPad. It is possible to bind a program to each of the
       buttons. It has an on-screen display (OSD) to show volume, mute,
       LCD brightness, and some other things.
     * [http://rsim.cs.uiuc.edu/~sachs/tp-scroll/] IBM ThinkPad Scroll
       Daemon
     * [http://people.debian.org/~dz/i8k/] i8k utils for DELL laptops.
     * [http://www.cakey.de/acerhk/] hotkey Linux driver for ACER
       laptops.
     * [http://www.blinkenlights.ch/cgi-bin/fm.pl?get=osle] OSL is a
       simple pbbuttonsd (used on Apple laptops to access the 'special
       keys' like volume, eject, etc.) client. It uses the xosd-lib to
       display the current values which makes it look a lot more like
       OSX than other pbbuttonsd-clients.
     * [http://pbbuttons.berlios.de/] PBButtons enables hotkeys on Apple
       iBook/PowerBook/TiBook. I have heard it works well on x86
       architectures, too.
     * [http://www.dreamind.de/ikeyd.shtml] ikeyd is a simple daemon
       which sets the volume or ejects a CDROM when hotkeys are pressed
       on an iBook/TiBook.
     * [http://perso.wanadoo.fr/pascal.brisset/vaio/] jogdiald for the
       Jog-Dial on SONY laptops offers support for extra keys, too.
     * [http://sourceforge.net/projects/omke/] omke is a set of small
       programs and patches to configure some advanced features of your
       HP OmniBook (usually things that HP has not documented) such as
       enabling/disabling the extra onetouch/multimedia keys. This tool
       works also for some Toshiba notebooks.
     ________________________________________________________________

12.13. Function Key

   The function key (often labelled Fn on the key) is usually used to
   switch on a simulated numeric keyboard, which is provided as a
   separate keypad on desktop keyboards. For those who don't want to use
   the simulation there are additional external numeric keypads
   available for PS/2 ports and I suppose USB ports. Also the function
   key may be used in combination with some F-keys to change display
   brightness, adjust the speaker volume or mute them, lock the
   keyboard, switch between external and internal display, use different
   suspend modes and more. Sometimes these key combinations work out of
   the box with Linux. Some require dedicated tools, for these tools see
   the Hotkey chapter above.
     ________________________________________________________________

12.14. Power Key

   The power key often has different functions, besides power on and off
   it may be used to wake up the machine from suspend mode. This is
   usually achieved by pressing the power button for just a few seconds
   only. If you press it longer (app. more than 5 seconds) it will power
   down fully.

   With modern laptops supporting ACPI it's also possible to achieve
   power off, with ACPI via the /proc/apci/ interface.
     ________________________________________________________________

12.15. Extra LEDs

   Some laptops offer extra LED, e.g. - mail - LEDs. The tool setleds
   (which is part of [http://lct.sourceforge.net/] Linux Console Tools)
   can be helpful to make use of them.
     ________________________________________________________________

12.16. Numeric Keypad

   On desktop keyboards the numeric keypad is usually separated from the
   character set, but laptops don't have a separated numeric keypad.
   There are different ways to emulate one, e.g. with the Fn key or with
   NUM-LOCK key. Also external numeric keyboards which connect to the
   PS/2 port (or USB, RS232) are available.

   As described above, the numeric keyboard has to be used if you want
   to change the X11 resolution by typing <CTL><ALT><+> or
   <CTL><ALT><->. If this doesn't work or is too complicated, you may
   use [http://www.dakotacom.net/~donut/programs/gvidm.html] gvidm
   Running gvidm will pop up a list of available modes and allows the
   user to select one if desired. This makes it perfect for running from
   an application menu or a hotkey, so you don't have to use ram for an
   applet constantly running. If you are running dual or multi-head
   displays, it will give you a list of screens so you can select the
   appropriate one. Also you may use xvidtune [-next | -prev ]. To check
   the current resolution you may use xwininfo -root, if xvidtune is not
   at hand.
     ________________________________________________________________

12.17. Pointing Devices - Mice and Their Relatives

12.17.1. Linux Compatibility Check

   You may check your mouse with the mev command from the GPM package.
