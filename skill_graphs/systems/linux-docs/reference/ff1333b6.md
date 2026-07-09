     ________________________________________________________________

12.17.2. Related Documentation

    1. [http://tldp.org/HOWTO/3-Button-Mouse.html] 3-Button-Mouse-HOWTO
       for serial mice
    2. [http://tldp.org/HOWTO/Kernel-HOWTO/] Kernel-HOWTO
     ________________________________________________________________

12.17.3. Mice Species

    1. Trackpad, Touchpad, are used with the majority of current laptops
    2. Trackball, e.g. COMPAQ LTE
    3. Pop-up-Mouse, e.g. HP OmniBook 800
    4. Trackpoint, Mouse-Pin, e.g. IBM(TM) ThinkPad and Toshiba laptops
    5. 3 Button Mice, e.g. IBM(TM) Thinkpads at least the 600s and some
       COMPAQ models e.g. Armada M700. I have heard rumor about a 3
       button mouse for Texas Instruments Travelmates, but couldn't
       verify this yet.
    6. Touchscreen, e.g. some Fujitsu-Siemens laptops, TabletPCs and
       PDAs
     ________________________________________________________________

12.17.4. PS/2 Mice

   Most of the mice used in laptops are PS/2 mice (actually I don't know
   one with another mouse protocol). You may communicate with the PS/2
   mouse through /dev/psaux or /dev/psmouse. If you use X Windows this
   device and the protocol has to be set in /etc/X11/XF86Config. In
   earlier releases, sometimes the GPM mouse manager and X Windows had
   trouble sharing a mouse when enabled at the same time. But as far as
   I know this is no problem anymore for the latest versions.

   Speaking of Emulate3Buttons, 100ms is usually better than the 50ms
   allowed in most default setups of /etc/X11/XF86Config for XFree86
   3.x:
Section "Pointer"
        ...
        Emulate3Buttons
        Emulate3Timeout    100
        ...
EndSection

   Or in /etc/X11/XF86Config-4 for XFree86 4.x:
Section "InputDevice"
        ...
        Option          "Emulate3Timeout"       "100"
        Option          "Emulate3Buttons"       "true"
        ...
EndSection
     ________________________________________________________________

12.17.5. Touchpad

   Usually a touchpad works with the PS/2 mouse device /dev/psaux and
   the PS/2 protocol (for GPM and X11, for X11 it seems also worth to
   check the GlidePointPS/2 protocol).

   The [http://w1.894.telia.com/~u89404340/touchpad/index.html]
   Synaptics TouchPad driver has the following functions (some functions
   require features from the touchpad that must be present, multifinger
   taps for example):

    1. Movement with adjustable, non-linear acceleration and speed
       (Options: MinSpeed, MaxSpeed, AccelFactor)
    2. Button events through short touching of the touchpad (Options:
       MaxTapTime, MaxTapMove)
    3. Double-Button events through double short touching of the
       touchpad
    4. Dragging through short touching and holding down the finger on
       the touchpad
    5. Middle and right button events on the upper and lower corner of
       the touchpad (Option: Edges)
    6. Scrolling (button four and five events) through moving the finger
       on the right side of the touchpad (Options: Edges,
       VertScrollDelta)
    7. The up/down button sends button four/five events
    8. Adjustable finger detection (Option: Finger)
    9. Ext Mouse repeater support - Alpha! (Option: Repeater)
   10. Multifinger taps: two finger for middle button and three finger
       for right button events
   11. Online configuration through shared-memory (in development)
       (Option: SHMConfig)

   The synclient command is provided with the driver sources (note it's
   not included in SuSE Linux, at least not until 9.3). The command
   queries and modifies the Synaptics TouchPad driver parameters on the
   fly.

   Tip

   Tipping with one, two or three fingers on the touchpad simultaneously
   results in pressing the left, middle and respectively the right
   mouse-button.

   There is also another touchpad driver available.
   [http://www.compass.com/synaptics/] The Synaptics Touchpad Linux
   Driver - tpconfig supports pointing devices used in notebooks by
   Acer, Compaq, Dell, Gateway, Olivetti, Texas Instruments, Winbook,
   and others.

   Dell and Sony have started incorporating a touchpad, touchstick from
   ALPS. They are in at least the Dell Latitude CPx and the Sony VAIO
   laptop lines. Maintainer Bruce Kall writes: "tpconfig does NOT
   support them at this time, but I am in the process of getting the API
   from ALPS and will be incorporating this in the next version of
   tpconfig. The Dell's also incorporate the ALPS GlideStick in the
   middle of the keyboard (like the stick pointer in some of the IBM
   Thinkpads). I also intend to support the disabling of "tapping" the
   GlideStick as well. Tapping of the touchpad/touchsticks drives me
   crazy, I'm not sure about you (causes the "selection" of things on
   the screen when you don't want to)!"

   tpconfig is a command-line utility to set options on Synaptics
   Touchpad and (now) ALPS Glidepad/ Stickpointers. Most people
   primarily use it to turn off the "tap mode" on laptop touchpads.

   How to use tpconfig: tpconfig is currently supported as a
   command-line configuration tool. The PS/2 port does not currently
   support sharing. Therefore the tpconfig utility will not work while
   any other mouse driver is loaded (e.g. gpm). This also means that you
   cannot use tpconfig while X Windows is running. The suggested use of
   tpconfig is to run it from a startup script before gpm is started.

   [http://rsim.cs.uiuc.edu/~sachs/tp-scroll/] IBM ThinkPad Scroll
   Daemon

   Not all touchpads are being from Synaptics, e.g some Gateways
   incorporate an EZ-Pad (Registered TM) and there might be other
   brands. The [http://www.synaptics.com/decaf/utilities/tprev.exe]
   TPREV.EXE utility will verify you have a Synaptics touchpad.

   The recent [ftp://ftp.prosa.it/pub/gpm/] gpm package (version >=1.8,
   maybe earlier versions contain touchpad support, too) includes the
   above mentioned Synaptics touchpad device driver. This device driver
   has been developed by H. Davies <hdavies_AT_ameritech.net>. Instead
   of using the PS/2 compatibility mode of touchpad devices, you can now
   use native touchpad mode with some pretty impressive features.

   In addition to translating finger motion into mouse motion and
   supporting the buttons, this support currently has several features
   (from the README):

     * a "tap" on the TouchPad causes a left mouse click
     * a "tap" followed quickly by a finger motion causes a left button
       drag type action.
     * a "tap" in one of the corners causes an action the default
       configuration is upper right causes middle mouse click and lower
       right causes right mouse click
     * more pressure on the touch pad speeds the motion of the cursor
     * a "tap" with a motion component (default > 2mm) initiates a toss
       and catch sequence. This is terminated by a finger touch on the
       pad (the toss also ends after 1 sec since that is the idle
       timeout period for the touchpad).
     * if the finger moves close to an edge then the mouse motion will
       be continued in that direction so that you don't need to pick up
       your finger and start moving again. This continued motion is
       pressure sensitive (more pressure is faster motion).

   These features can be enabled/disabled and many of them have time and
   speed parameters which can be adjusted to the taste of the user.

   It seems gpm is best known as a console biased tool. This is true,
   but you may use it as an X11 input device. gpm is used as a repeater
   device. In this way you can use both the built-in synaptics touchpad
   with all the features and at the same time a serial mouse (with three
   buttons). This all works smoothly together. X11 reads the mouse
   events from a named pipe /dev/gpmdata in a protocol it understands,
   which in my case is Mouse-Systems-Compatible (5bytes). Most 3-button
   mice use the default protocol. So a simple reconfiguration in
   XF86Config is all that is required, after starting gpm in an
   appropriate way, of course.

   gpm could be started on your laptop with the following arguments :
   /usr/bin/gpm -t synps2 -M -t ms -m /dev/ttyS0 . Both touchpad and
   serial mouse work in console and X11 mode. You do have to create the
   named pipe /dev/gpmdata yourself.

   Tapping with two fingers simultaneously to simulate a middle mouse
   button works on Logitech touchpads used in a few machines.

   Thanks to Geert Van der Plas for most of the touchpad chapter.
     ________________________________________________________________

12.17.6. Jog-Dial

   The "Jog-Dial" is an input device used in the SONY VAIO laptop
   series. You may find a
   [http://www004.upp.so-net.ne.jp/t-kinjo/vaio/index_e.html] Jog-Dial
   driver by Takaya Kinjo. Probably you have to change two things in the
   spicdriver/Makefile:

   CCFLAG has to be extended with -D_LOOSE_KERNEL_NAMES

   CCFLAG has to be extended with
   -I/usr/src/linux-<kernel-version>/include

   The README seems to be in Japanese, here is an English version.

$ tar xvzf jogutils.tar.gz
$ cd jogutils
$ make
$ su
# mknod /dev/spic c 60 0
# modprobe spicdriver/spicdriver
# exit
$ cp jogapp/rcfile ~/.jogapprc
$ jogapp/jogapp

   ISHIKAWA Mutsumi wrote the
   [http://perso.wanadoo.fr/pascal.brisset/vaio/] jogdiald driver, which
   runs entirely in user-space (no kernel modules required).

   [http://linuxbrit.co.uk/rsjog/] rsjog. is a modification of the
   [http://sjog.sourceforge.net/] sjog utility.
     ________________________________________________________________

12.17.7. Touchscreens

   The only modern laptops I know which include a touchscreen are the
   Fujitsu Biblo 112/142 (aka MC 30) and the Palmax PD 1000/1100 (aka
   IPC 1000/1100).

   The latest version of the [http://www.cs.nmsu.edu/~pfeiffer/#pen]
   Linux Compaq Concerto Pen Driver is available from Joe Pfeiffer's
   home page.

   A current survey of drivers you may find at my page
   [http://tuxmobil.org/touch_laptops.html] Touchscreen Laptops and
   Linux .
     ________________________________________________________________

12.17.8. Pen Devices, Mousepoints

   IBM and Toshiba laptops currently come with a pen devices instead of
   a mousepad or trackball.

   Tip

   It needs some time to get used to this kind of pointer device. It may
   help to rest your palm at the front rest. Also it's recommended to
   reduce the mouse speed.
     ________________________________________________________________

12.17.9. External Mouse

   For better handling, e.g. with a 3 button mouse you may use an
   external mouse. This is usually a serial mouse or a PS/2 mouse, or in
   our days a USB mouse, appropriate to the port your laptop offers.
   Usually this is no problem. The only thing I currently don't know a
   solution for is the automagic detection of a newly plugged in mouse
   from X11. To get it work you have to restart your X server.
     ________________________________________________________________

12.17.9.1. PS/2 Mouse

   For PS/2 ports there are so called Y-Cable available, which make it
   possible to use external mouse and external keyboard at the same time
   if your laptop supports this feature.

   Warning

   Don't plug in the external mouse while powered up. If you have
   separate mouse and keyboard ports, make sure you plug the mouse in
   the mouse port and the keyboard in the keyboard port. If you don't,
   you may have to do a hard reboot of the laptop to get it to recover.
     ________________________________________________________________

12.17.9.2. Wheel Mouse

   [http://jonatkins.org/imwheel/] Imwheel makes the wheel of your
   Intellimouse (and other wheel and stick mice) work in Linux/X11 to
   scroll windows up and down, or send keys to programs. It runs in the
   background as a daemon and requires little reconfiguration of the
   x setup. 4 or more button mice and Alps Glidepad 'Taps' may
   also be used. imwheel includes a modified gpm for an alternate method
   of wheel input.

   See also the [http://www.inria.fr/koala/colas/mouse-wheel-scroll/]
   WHEEL Mouse FAQ which describes how to get lots of X applications to
   recognise the scrolling action. For current instructions on XFree86
   4.x see [http://www.xfree86.org/current/mouse.html] XFree86 4.x -
   Mouse Docs.
     ________________________________________________________________

12.17.9.3. USB Mouse

   This part is taken from The Linux USB Sub-System by Brad Hards.
     ________________________________________________________________

12.17.9.3.1. USB Human Interface Device (HID) Configuration

12.17.9.3.1.1. General HID Configuration

   There are two options for using a USB mouse or a USB keyboard - the
   standalone Boot Protocol way and the full featured HID driver way.
   The Boot Protocol way is generally inferior, and this document
   describes the full featured way. The Boot Protocol way may be
   appropriate for embedded systems and other systems with resource
   constraints and no real need for the full keyboard and mouse
   capabilities.

   It is important to remember that the HID driver handles those devices
   (or actually those interfaces on each device) that claim to comply
   with the Human Interface Device (HID) specification. However the HID
   specification doesn't say anything about what the HID driver should
   do with information received from a HID device, or where the
   information that is sent to a device comes from, since this is
   obviously dependent on what the device is supposed to be doing, and
   what the operating system is. Linux (at the operating system kernel
   level) supports four interfaces to a HID device - keyboard, mouse,
   joystick and a generic interface, known as the event interface.
     ________________________________________________________________

12.17.9.3.1.2. HID Mouse Configuration

   In the kernel configuration stage, you need to turn on USB Human
   Interface Device (HID) support and Mouse Support Do not turn on USB
   HIDBP Mouse support. Perform the normal kernel rebuild and
   installation steps. If you are installing as modules, you need to
   load the input.o, hid.o and mousedev.o modules.

   Plug in a USB mouse and check that your mouse has been correctly
   sensed by the kernel. If you don't have a kernel message, look for
   the changes to /proc/bus/usb/devices.

   Since USB supports multiple identical devices, you can have multiple
   mice plugged in. You can get each mouse separately, or you can get
   them all mixed together. You almost always want the mixed version,
   and that is what will be used together. You need to set up a device
   node entry for the mixed mice. It is customary to create the entries
   for this device in the /dev/input/ directory.

   Use the following commands:
mkdir /dev/input
mknod /dev/input/mice c 13 63

   Tip

   If you are unsure whether you are configuring the right mouse device,
   use cat /dev/input/mice (or other appropriate devices names). In case
   you do this for the correct mouse, you should see some bizarre
   looking characters as you move the mouse or click any of the buttons.

   If you want to use the mouse under X, you have various options. Which
   one you select is dependent on what version of XFree86 you are using
   and whether you are using only USB for your mouse (or mice), or
   whether you want to use a USB mouse and some other kind of pointer
   device.

   You need to edit the XF86Config file (usually
   /usr/X11R6/lib/X11/XF86Config or /etc/X11/XF86Config).

   If you are using XFree86 version 4.0 or later, add an InputDevice
   section that looks like the following:
Section "InputDevice"
     Identifier  "USB Mice"
     Driver      "mouse"
     Option      "Protocol"   "IMPS/2"
     Option      "Device"     "/dev/input/mice"
EndSection

   or, if you want to use a wheel mouse, something like this may be more
   useful:
Section "InputDevice"
     Identifier  "USB Mice"
     Driver      "mouse"
     Option      "Protocol"   "IMPS/2"
     Option      "Device"     "/dev/input/mice"
     Option      "ZAxisMapping"   "4 5"
     Option      "Buttons"        "5"
EndSection

   Consult the [http://www.xfree86.org/current/mouse.html] current
   XFree86 documentation for a detailed explanation and more examples.

   You also need to add an entry to each applicable ServerLayout
   Section. These are normally at the end of the configuration file. If
   you only have a USB mouse (or USB mice), then replace the line with
   the "CorePointer" entry with the following line:
InputDevice "USB Mice" "CorePointer"

   If you want to use both a USB mouse (or USB mice) and some other kind
   of pointer device, then add (do not replace) the following line to
   the applicable ServerLayout sections:
InputDevice "USB Mice" "SendCoreEvents"

   If you are using only a USB mouse (or USB mice) with XFree86 3.3,
   edit the Pointer section so that it looks like the following:
Section "Pointer"
    Protocol    "IMPS/2"
    Device      "/dev/input/mice"
EndSection

   If you are trying to use a USB mouse (or USB mice) in addition to
   another pointer type device with XFree86 3.3, then you need to use
   the XInput extensions. Keep the existing Pointer (or modify it as
   required for the other device if you are doing an initial
   installation), and add the following entry (anywhere sensible,
   ideally in the Input devices area):
Section "Xinput"
   SubSection "Mouse"
  DeviceName   "USB Mice"
  Protocol     "IMPS/2"
  Port         "/dev/input/mice"
  AlwaysCore
   EndSubSection
EndSection

   Restart the X server. If you don't have any mouse support at this
   point, remember that Ctrl-Alt-F1 will get you a virtual terminal that
   you can use to kill the X server and start debugging from the error
   messages.

   If you want to use the mouse under gpm, run (or kill and restart if
   it is already running) gpm with the following options. gpm -m
   /dev/input/mice -t imps2 (as superuser). You can make this the
   default if you edit the initialisation files. These are typically
   named something like rc.d and are in /etc/rc.d/ on RedHat
   distributions.

   If you have both a USB mouse (or USB mice) and some other kind of
   pointer device, you may wish to use gpm in repeater mode. If you have
   a PS/2 mouse on /dev/psaux and a USB mouse (or USB mice) on
   /dev/input/mice, then the following gpm command would probably be
   appropriate: gpm -m /dev/input/mice -t imps2 -M -m /dev/psaux -t ps2
   -R imps2. Note that this will make the output appear on /dev/gpmdata,
   which is a FIFO and does not need to be created in advance. You can
   use this as the mouse "device" to non-X programs, and both mice will
   work together.

   Table 12-1. Arguments for the -t and -R option of gpm.
   option description
   ms     MicroSoft compatible serial mouse
   ps2    PS/2 or C&T 82C710
   bm     Logitech bus mouse
   bm     ATI XL bus mouse
   mb     MicroSoft bus mouse
   msc    Mouse Systems serial mouse
   logi   older mouse
   mman   Mouse Man protocol, serial Logitech mouse
   sun    SUN mouse, three button
   ms3    Intellimouse with wheel, at serial port
   imps2  Intellimouse with wheel, at PS/2 port
   pnp    PnP mice, alternative to ms
   mm     MM series
   bare   oldest serial two button mouse
     ________________________________________________________________

12.17.9.4. Wrist Input Device - Twiddler

   The gpm contains a driver for the Twiddler device at the serial port.
   For information about the Twiddler see [http://www.handykey.com/]
   Handykey Corporation .
     ________________________________________________________________

12.17.10. Macintosh PowerBooks

   PowerBooks have a trackpad and only one button, although you can plug
   in external multi-button USB mice. The usual thing is to map a couple
   of keys on the keyboard to the middle and right mouse buttons; your
   Linux distribution should come with instructions on how to configure
   this (it's not specific to laptops, as all Apple mice are
   single-button).

   If you are using the Xpmac server, the default is option-1 and
   option-2, and you can change this by passing -middlekey <keycode>
   -rightkey <keycode> arguments to Xpmac, and -nooptionmouse if you
   don't want the option key to be needed.

   If you are using XFree86, you pass adb_buttons=<middlekey>,<rightkey>
   kernel arguments (no option is required). I use adb_buttons=58,55 to
   map the option and Apple/command keys (which are little-used in
   Linux); use e.g. xev to find out the keycode for a given key.
     ________________________________________________________________

12.18. Advanced Power Management - APM

12.18.1. Linux Compatibility Check

   Start by reading the
   [http://tldp.org/HOWTO/Battery-Powered/index.html]
   Battery-Powered-mini-HOWTO.

   For APM to work the machine's firmware must implement the APM
   Specification. Linux supports versions 1.0 through 1.2 of the
   standard. To work with Linux the APM BIOS must support 32-bit
   protected mode connections.

   To display information about the APM BIOS on your system you can run
   dmesg | grep apm command or look in the /proc/apm file.
     ________________________________________________________________

12.18.2. Introduction

   APM support consists of two parts: kernel support and user-land
   support.
     ________________________________________________________________

12.18.2.1. Kernel Support

   You need a kernel that has the APM driver compiled in using the
   appropriate kernel configuration options. Currently most
   distributions do not ship kernels with the APM driver enabled so you
   may have to enable the driver using a boot option or to compile a
   custom kernel. Please see [http://tldp.org/HOWTO/Kernel-HOWTO/]
   Kernel-HOWTO or your distribution manual for details.

   The APM driver can be modularized but this is not recommended since
   many drivers will disable their APM features if the APM driver is not
   present when they initialize themselves.

   The available APM options are (please see
   Documentation/Configure.help in the kernel source tree for more
   details):

     * CONFIG_APM_IGNORE_USER_SUSPEND Just a workaround for some NEC
       Versa M series laptops.
     * CONFIG_APM_DO_ENABLE Enable APM features at boot time.
     * CONFIG_APM_CPU_IDLE Puts CPU in power save mode, if there is
       nothing to do for the kernel.
     * CONFIG_APM_DISPLAY_BLANK Some laptops can use this to turn off
       the LCD backlight when the screen blanker of the Linux virtual
       console blanks the screen. Note that this is only used by the
       virtual console screen blanker, and won't turn off the backlight
       when using the X Window system.
     * CONFIG_APM_POWER_OFF Turns the machine completely down, when
       using halt. This feature works with most laptops without
       problems.
     * CONFIG_APM_IGNORE_MULTIPLE_SUSPEND Just a workaround for IBM(TM)
       ThinkPad 560.
     * CONFIG_APM_IGNORE_SUSPEND_BOUNCE Just a workaround for Dell
       Inspiron 3200 and other notebooks.
     * CONFIG_APM_RTC_IS_GMT Stores time in Greenwich Mean Time format.
       It is in fact recommended to store GMT in your real time clock
       (RTC) in the BIOS.
     * CONFIG_APM_ALLOW_INTS Resolves some problems with Suspend to Disk
       for some laptops, for instance many newer IBM(TM) ThinkPads.
     * CONFIG_SMP Symmetric Multi-Processing support. This enables
       support for systems with more than one CPU. If you have a system
       with only one CPU, like most personal computers, say N. Though
       the default seems to be Y. So it may be enabled if you are
       unaware. I have got reports that SMP support enabled does
       interfere with APM. So with a single CPU machine like a laptop
       you are on the save side, when you N.

   Features of the APM driver according to the Kernel documentation file
   Documentation/Configure.help: "The system time will be reset after a
   USER RESUME operation, the /proc/apm device will provide battery
   status information, and user-space programs will receive notification
   of APM events (e.g., battery status change). "
     ________________________________________________________________

12.18.2.2. Userland Support

   The most important userland utility is
   [http://worldvisions.ca/~apenwarr/apmd/] apmd, a daemon that handles
   APM events.

   If you run a 2.2.x or later kernel and want to experiment, Gabor Kuti
   <seasons_AT_falcon.sch.bme.hu> has made a kernel patch that allows
   you to hibernate any Linux system to disk, even if your computers APM
   BIOS doesn't support it directly. In my humble opinion you don't need
   this features if your laptop provides a function key to invoke
   suspend mode directly.

   Please see the [http://tldp.org/HOWTO/Battery-Powered/] Battery
   Powered Linux Mini-HOWTO for detailed information.

   Here's what apmd can do:

     * apmd(8): logs the battery status to syslog every now and then and
       runs a proxy script that can take action before suspend or after
       resume
     * apm(1): prints the current battery status or suspends the
       computer
     * apmsleep(1): suspends the machine for a limited time
     * xapm(1x): provides a battery meter for X11
     * libapm.a: a library for writing APM applications

   Some APM firmware fails to restore mixer settings properly which can
   result in squeals of feedback in the music after the machine has
