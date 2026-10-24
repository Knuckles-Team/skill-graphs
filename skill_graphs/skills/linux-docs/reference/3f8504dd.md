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
