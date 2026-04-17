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
