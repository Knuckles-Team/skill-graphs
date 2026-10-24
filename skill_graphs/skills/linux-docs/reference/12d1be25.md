       place, if you don't have one around.
       The only drawback that I can think of is that it takes a couple
       extra seconds to set up or pack up your laptop. It takes about 30
       seconds to snap into place and makes it impossible to quickly
       walk away with the laptop. It won't stop a determined thief with
       the time to unscrew the legs of the desk or one that wanders
       around with a substantial pair of wire cutters in hand, but I
       feel pretty secure leaving the laptop on my desk while I go to
       meetings or lunch.
       Well known manufacturers of dedicated laptop locks are
       [http://www.kensignton.com] Kensignton and TARGUS.
    2. Name plates: to reduce the possibility of theft, you may want to
       have a nameplate (name, phone, e-mail, address) made and affixed
       to the cover of the laptop. A nice one will cost you about $12,
       and can be made by any good trophy shop. They'll glue it on for
       you too. You could use double-sided tape instead, but glue is
       more permanent. So it's easy to return, but will look beaten and
       abused if these are removed. You may even make an engravement
       into the laptop cover (inside). And even better into every
       removable part (hard disk, battery, CD/DVD drive, power unit). If
       this machine ever gets to a repair office, I might get the
       machine back. Make sure you remember to update the plates if you
       move.
       If you don't mind marking up a piece of equipment worth several
       thousand dollars, make sure your laptop has some distinguishing
       feature that is easily recognizable, e.g. a bunch of stickers
       pasted on it. Not only does it make your laptop easier to
       recognize, my guess is that people would be less likely to steal
       it.
       It might even be useful to have a sticker that clearly says "Does
       Not Run Windows". This is at least an argument for having your
       bootloader stop at the bootloader prompt, rather than mosey
       onwards into a colorful XDM login.
    3. Link xlock to apm services. What about setting a system such as
       when the laptop is unused for a while, instead of using normal
       apm service and suspend the machine, makes it run an xlock,
       disable the apm services in a way such that they do not suspend
       the machine automatically and start a 'laptop-protection daemon'.
       When the xlock disappears, the daemon is stopped and the apm
       services are restarted (so you might use the apm services
       yourself).
       In the case somebody unplugs the machine while under the xlock
       (without giving the password), then the daemon would detect it
       and could start doing some preventive action, such as: - playing
       a sound with maximum volume saying "I am getting stolen". - this
       daemon could also register to a fixed local server and do a ping
       every now and then. If the ping stops before the daemon
       unregister to the server, then server then can take other
       actions, such as sending SMS message, starting a video camera, in
       the room, etc. The apm services down would make the stealer
       unable to use the hot keys to suspend/stop the machine, isn't it?
    4. You can change the "pollution preventer" logo at startup on AWARD
       BIOSES. See instructions from
       [http://geggus.net/sven/linux-bootlogo.html] Sven Geggus. For IBM
       ThinkPads there is a dedicated DOS utility for burning your
       bizcard data into the BIOS boot screen.
    5. Boot loader: a boot loader may be used to put your name and phone
       number (or whatever text you choose) into the boot sequence
       before the operating system is loaded. This provides a label that
       can't be removed by editing files or even doing a simple format
       of the harddisk. Some boot loaders (e.g. LILO) offer a password
       option, which is highly recommend (note without it's very easy to
       get root access).
    6. Camouflage: if you carry a dedicated laptop bag, this can be
       spotted by a thief easily. So think about getting another kind of
       bag.
    7. Serial Number: note the serial number in a secure place. This
       will be necessary if your laptop gets stolen.
    8. Insurance: There are some dedicated insurances, see my page
       [http://tuxmobil.org/stolen_laptops.html] Database of Stolen
       Laptops.
    9. Use of software that connects and identifies itself: As far as I
       know there was an old DOS utility that did something like this.
       It embedded itself into the bootsector and upon a certain
       keycombination it would throw a serial number onto the screen and
       play an audio code through the speaker (in case th monitor was no
       longer usable for whatever reason). You were supposed to register
       the serial number with the company that produced the utility.
       The laptop can send a mail with its real IP address if connected
       (mail with a print of ifconfig started by /etc/ppp/ip-up or by a
       cron job (if connected at a company-network).
   10. Always remove the external devices and secure them in another
       place/room. Set the BIOS to boot on the hard disk first as a
       default setting and remove boot on other devices if possible.
       Also try to plug the power supply in the least accessible plug.
       So if your machine get stolen in your office the 'quick way'
       (e.g. during a 5 sec. cigarette break), the stealer won't perhaps
       have time to get the power supply, neither the time to get the
       drives. Perhaps he/she will end up with a less useful laptop and
       you may recover it.
   11. Electronic Devices (Transponders): There are also devices
       available, which can be detected remote via satellites, see my
       page [http://tuxmobil.org/stolen_laptops.html] about stolen
       laptops for a survey.
     ________________________________________________________________

15.8.3. The Day After

   Your primary goal is to prevent your laptop from being stolen in the
   first place. Your secondary goal is to recover it after it is stolen.
   Report it to the police station ASAP. Check the local newsgroup (in
   case...) or even post in it.

   I have provided a [http://tuxmobil.org/stolen_laptops.html] survey of
   databases for stolen laptops.
     ________________________________________________________________

15.8.4. Resources

   The chapter about theft protection has taken some advantages of ideas
   of Lionel "Trollhunter" Bouchpan-Lerust-Juery and a discussion, which
   has taken place in the [http://www.debian.org/MailingLists/subscribe]
   debian-laptop mailing list in January 2001.
     ________________________________________________________________

15.9. Dealing with Down Times (Cron Jobs)

   A cron-like program that doesn't go by time: anacron (like
   "anac(h)ronistic") is a periodic command scheduler. It executes
   commands at intervals specified in days. Unlike cron, it does not
   assume that the system is running continuously. It can therefore be
   used to control the execution of daily, weekly and monthly jobs (or
   anything with a period of n days), on systems that don't run 24 hours
   a day. When installed and configured properly, anacron will make sure
   that the commands are run at the specified intervals as closely as
   machine-uptime permits.

   [http://metalab.unc.edu/pub/Linux/system/daemons/cron] hc-cron is a
   modified version of Paul Vixie's widely used cron daemon. Like the
   original program it runs specified jobs at periodic intervals.
   However, the original crond relies on the computer running
   continuously, otherwise jobs will be missed. This problem is
   addressed by hc-cron, that is indended for use on home-computers that
   are typically turned off several times a day; hc-cron will remember
   the time when it was shut down and catch up jobs that have occurred
   during down time when it is started again.
     ________________________________________________________________

15.10. Mobile Printing

   There are different techniques to print from mobile computers. You
   may use mobile printer hardware (see chapter Printers and Scanners
   above) or print via a stationary printer. To connect to a mobile or
   stationary printer or printer server you may use many protocols:

    1. InfraRed - IrLPT/IrCOMM: See the
       [http://tuxmobil.org/howtos.html] InfraRed-HOWTO.
    2. InfraRed - IrOBEX: See the [http://tuxmobil.org/howtos.html]
       InfraRed-HOWTO.
    3. BlueTooth: See the
       [http://www.holtmann.org/linux/bluetooth/cups.html] Bluetooth
       printing backend for CUPS At the moment this backend only
       provides native printing for Bluetooth serial port enabled
       printers, but for the future the support of Basic Printing (BPP)
       and Hardcopy Cable Replacement (HCRP) is planned.
    4. wireless network - WLAN
    5. network - LAN
    6. rlpr - remote line printer
    7. Server Message Block - SMB, via SAMBA
    8. parallel port
    9. serial port
   10. USB port
     ________________________________________________________________

15.11. Noise Reduction

   Due to the proliferation of cellular phones and walkmans it's not
   quite common in our days to take care of a quiet environment. Anyway
   I want to give some recommendations for the polite ones.

   Computer noises are caused by hardware (fan, optical drive, hard
   disk) and applications.
     ________________________________________________________________

15.11.1. Console (Shell) and X11

   The beeping of X11 windows can be configured to a shorter and lower
   pitched tone or even to a blunt "thump" with xset b ... options (a
   lower pitched tone is usually less annoying and distracting).
   Independently of that, most xterm-compatible windows and shells can
   be configured to make "visual bell" instead of "audio bell". For the
   console setterm -blength 0 and for X11 xset b off turns the bell off.
   See also the PCMCIA-HOWTO and much more details in the
   [http://tldp.org/HOWTO/Visual-Bell.html] Visible-Bell-Howto.
     ________________________________________________________________

15.11.2. PCMCIA

   When starting your laptop with PCMCIA-CS configured correctly, this
   will be shown by two high beeps. If you want to avoid this put
   CARDMGR_OPTS="-q" into the PCMCIA configuration file, e.g.
   /etc/default/pcmcia for Debian/GNU Linux.

   To avoid the dialtones during the modem dialing add

module "serial_cs" opts "do_sound=0"

   to /etc/pcmcia/config.opts (from man serial_cs). This will disable
   speaker output completely, but the AT M command should let you
   selectively control when the speaker is active, e.g. AT M0 turns off
   the modem's speaker.
     ________________________________________________________________

15.11.3. USB

   usbmgr configuration file /etc/usbmgr.conf.
### BEEP
# beep off
# beep on
     ________________________________________________________________

15.11.4. Hotplug

   Add an entry into the configuration file /etc/sysconfig/hotplug.
HOTPLUG_BEEP="no"
     ________________________________________________________________

15.11.5. Fan

   Warning

   Please make sure what you are doing, when configuring the fan. Your
   laptop may overheat and die, in case you have done something wrong.
   Just in case you want to check the fan try to cause a heavy CPU load,
   for example by issuing md5sum /dev/urandom. Now top will show an
   increased CPU load and the fan should began to run eventually. Note:
   usually you need to have been connected to power, otherwise the CPU
   might reduce load by itself. Also watch for the CPU temperature acpi
   -bt or cat /proc/acpi/thermal_zone/*.

   For some laptop series there are Linux utilities available to control
   the fan and other features.

     * [http://www.buzzard.me.uk/toshiba/index.html] Toshutils by
       Jonathan Buzzard for some Toshiba models.
     * [http://tpctl.sourceforge.net] tpctl IBM ThinkPad configuration
       tools for Linux by Thomas Hood.
     * [http://people.debian.org/~dz/i8k/] i8k utils for DELL laptops.
     ________________________________________________________________

15.11.5.1. Known Problems

   With some laptops the fan is always on or at least very often. Here
   are some remedies.
     ________________________________________________________________

15.11.5.1.1. Reduction of CPU Frequency

   In some cases the fan is always on because the CPU is working with
   highest frequency. You may use either
   [http://sourceforge.net/projects/cpufreqd] cpufreqd or
   [http://mnm.uib.es/~gallir/cpudyn/] cpudyn to cure this.
     ________________________________________________________________

15.11.5.1.2. IRQ Problems with ParPort Module

   Sometimes the parport causes the fan to be always on. You may edit
   the /etc/modules.conf to cure this:
 alias parport_lowlevel parport_pc
 options parport_pc io=378 irq=7

   The IO address and the IRQ number depend on the hardware settings or
   the BIOS configuration. Often the IRQ does not need to be given. The
   problem and its solution was discussed in the
   [http://lists.opensuse.org/opensuse-mobile-de/2002-11/msg00174.html]
   SuSE Laptop Mailing List (in German).
     ________________________________________________________________

15.11.5.1.3. ACPI

   Sometimes a setting in the /proc/acpi/ might also help.
     ________________________________________________________________

15.11.5.1.4. Miscellaneous

   Pressing the Fn+z key kombination tells the BIOS to recheck the
   sensors and stops the fan, for DELL laptops.
     ________________________________________________________________

15.11.6. Harddisk

   To avoid unnecessary hard disk noise you may use the same techniques
   as described in the power saving chapter above. Modern laptop and
   notebook hard drives come with a so-called "Acoustic Management",
   just have a look into the manual to get an overview about the
   possible settings.

   Some hard disk manufacturers offer dedicated tools, e.g. Hitachi's
   [http://www.hitachigst.com/hdd/support/download.htm] Feature Tool
   allows to change the drive Automatic Acoustic Management settings to
   the Lowest acoustic emanation setting (Quiet Seek Mode), or Maximum
   performance level (Normal Seek Mode). Also hdparm -M offers some
   Acoustic Management options.
     ________________________________________________________________

15.11.7. Miscellaneous Applications

   You may configure vi with the flash option, so it will use a flash in
   case of an error, instead of a bell. So just put this line into your
   .vimrc or at the vim prompt:
set flash

   or try
set visualbell
     ________________________________________________________________

Chapter 16. Solutions with Mobile Computers

16.1. Introduction

   The power and capabilities of laptops and PDAs are sometimes limited
   as described above. But in turn, they have a feature which desktops
   don't have their mobility. I try to give a survey about applications
   which make sense in connection with mobile computers.
     ________________________________________________________________

16.2. Mobile Network Analyzer

   I'm not an expert in this field, so I just mention the tools I know.
   Please check also for other applications. Besides the usual tools
   tcpdump, netcat, there are two applications I prefer, which may be
   used to analyze network traffic:

   The [http://www.ee.ethz.ch/stats/mrtg/] Multi Router Traffic Grapher
   (MRTG) is a tool to monitor the traffic load on network-links. MRTG
   generates HTML pages containing GIF images which provide a LIVE
   visual representation of this traffic. MRTG is based on Perl and C
   and works under UNIX and Windows NT.

   [http://ntop.org/] Network Top - ntop is a UNIX tool that shows the
   network usage, similar to what the popular top UNIX command does.
   ntop is based on libpcap and it has been written in a portable way in
   order to virtually run on every UNIX platform and on Win32 as well.
   ntop can be used in both interactive or web mode. In the first case,
   ntop displays the network status on the user's terminal. In web mode
   a web browser (e.g. netscape) can attach to ntop (that acts as a web
   server) and get a dump of the network status. In the latter case,
   ntop can be seen as a simple RMON-like agent with an embedded web
   interface.
     ________________________________________________________________

16.3. Mobile Router

   Though designed to work from a single floppy, the Linux Router
   Project (LRP) , seems useful in combination with a laptop, too.
     ________________________________________________________________

16.4. Hacking and Cracking Networks

   When thinking about the powers of laptops, hacking and cracking
   networks may come into mind. I don't want to handle this topic here,
   but instead recommend the
   [http://www.linuxsecurity.com/Security-HOWTO] Security-HOWTO .
     ________________________________________________________________

16.5. Mobile Data Collection

16.5.1. Related Documentation

    1. [http://tldp.org/HOWTO/Coffee.html] Coffee-HOWTO
    2. [http://tldp.org/HOWTO/AX25-HOWTO/] AX-25-HOWTO
    3. [http://tldp.org/HOWTO/Serial-HOWTO.html] Serial-HOWTO
    4. [http://tldp.org/HOWTO/Serial-Programming-HOWTO/]
       Serial-Programming-HOWTO
     ________________________________________________________________

16.5.2. Applications

   A Linux laptop can be used to collect data outside an office, e.g.
   geodesy data, sales data, network checks, patient data in a hospital
   and others. There is support for wireless data connections via
   cellular phone modems and amateur radio. I am not sure whether PCMCIA
   radio cards are supported, see [http://www.aironet.com/] Aironet
   Wireless Communications.
     ________________________________________________________________

16.5.3. Specific Environments

   There are laptops available with cases build for a rugged environment
   (even waterproof laptops). In some environments, for instance in
   hospitals, take care of the Electro-Magnetic-Compatibility of the
   laptop. This is influenced by many factors, for instance by the
   material used to build the case. Usually magnesium cases shield
   better than the ones made of plastics.
     ________________________________________________________________

16.6. Mobile Office

   With [http://www.kde.org] KDE (K-Office), [http://www.gnome.org/]
   Gnome and the commercial products WordPerfect, Staroffice and
   [http://www.applix.com/] Applixware Linux has more and more business
   software applications. With the corresponding hardware, e.g. a
   portable printer and a cellular phone which connects to your laptop,
   you will have a very nice mobile office.
     ________________________________________________________________

16.7. Connection to Digital Camera

   AFAIK there are currently three methods to connect a digital camera
   to a laptop: the infrared port (IrDA�), serial port and maybe USB.
   There are also some auxiliary programs for conversion of pictures,
   etc.

   Eric <dago_AT_tkg.att.ne.jp> wrote: "I finally succeeded in
   downloading pictures from my digital camera, but not exactly the way
   I expected, i.e. not through USB port but using PCMCIA card port and
   memory stick device, part of digital camera hardware. Anyway, some
   interesting things to mention:

   Sony (pretending using a standard) uses the msdos format to store
   images as JPEG files ; so the best way to have your OS recognizing
   them is to mount the raw device like a msdos filesystem; using mount
   directly doesn't work (don't know why) but an entry in the /etc/fstab
   file allows you to mount the device correctly. i.e.:
/dev/hde1    /mnt/camera    msdos     user,noauto,ro    0    0

   Of course, newfs before mount works too, but there is nothing to see
   at all ;-) I think both noauto and ro are important flags; I tried
   without it and it didn't work. Somehow the mount I got seems buggy .
   And if ro is missing, the camera doesn't recognize back the memory
   stick and it needs to be msdos-formatted.

   Appropriate to the camera documentation , both PCMCIA and USB port
   behave the same (for Mac and Windoze - i.e. you see a file system
   auto mounted) - I deduce for Linux it should be the same thing too,
   as long as the USB driver is installed. I think now that mounting USB
   raw device the way I did with PCMCIA should work, but I still
   couldn't find which device to use."

   [http://digitalux.netpedia.net/] OpenDiS (Open Digita Support) is a
   library and utility program for cameras such as the Kodak DC-220,
   DC-260, DC-265, and DC-280, that run Flashpoint's Digita operating
   system. The library is a unix implementation of the Digita Host
   Interface Specification, intended for embedding Digita support in
   other products such as gPhoto. The utility is a simple command-line
   program for standalone downloading of photos from the cameras.

   [http://www.gphoto.org/] gPhoto enables you to take a photo from any
   digital camera, load it onto your PC running a free operating system
   like GNU/Linux, print it, email it, put it on your web site, save it
   on your storage media in popular graphics formats or just view it on
   your monitor. gPhoto sports a new HTML engine that allows the
   creation of gallery themes (HTML templates with special tags) making
   publishing images to the world wide web a snap. A directory browse
   mode is implemented making it easy to create an HTML gallery from
   images already on your computer. Support for the Canon PowerShot A50,
   Kodak DC-240/280 USB, and Mustek MDC-800 digital cameras.

   [http://www.lightner.net/lightner/bruce/ppc_use.html] photopc is a
   library and a command-line frontend to manipulate digital still
   cameras based on Fujitsu chipset and Siarra Imaging firmware. The
   program is known to work with Agfa, Epson and Olympus cameras. Should
   also work with Sanyo, but this is untested. The cameras typically
   come with software for Windows and for Mac, and no description of the
   protocol. With this tool, they are manageable from a UNIX box. Bruce
   D. Lightner <lightner_AT_metaflow.com> has added support for Win32
   and DOS platforms. Note that the program does not have any GUI, it is
   plain command-line even on Windows. For a GUI, check out the phototk
   program.

   [http://kdc2tiff.sourceforge.net/] kdc2tiff is software to convert
   .kdc images from Kodak's DC120 digital camera to .tiff or .jpg files.
   This software pays particular attention to aspect ratio, high quality
   scaling, contrast adjustment, gamma correction, and image rotation.

   [http://www.netspace.net.au/~bmiller/linux/rdc2e/] rdc2e is a command
   line tool that downloads images from a Ricoh RDC-2E digital camera.
   It is available as either a source tar ball or a RedHat 6.1 i386 RPM.

   [http://www.debian.org/Packages/unstable/graphics/fujiplay.html]
   fujiplay Interface for Fuji digital cameras.
     ________________________________________________________________

16.8. Connection to QuickCam (Video)

   AFAIK there are three methods to connect a video camera to a laptop:
   a ZV port, FireWire and maybe USB, but I don't know how this works
   with Linux. I have heard rumors about using a sound card for video
   data transfer to a Linux box, see [http://worldvisions.ca/~apenwarr/]
   apenwarr . I have heard rumors about a Linux-QuickCam-mini-HOWTO, but
   couldn't find a reliable URL yet. Check the sane package which is
   build for scanner support, this should contain support for
   still-grabbers as well.

   [http://kmc-utils.sourceforge.net/] kmc_remote provides a graphical
   interface for controlling Kodak Motion Corder fast digital cameras
   over a serial connection. kmc_remote is built on the kmc_serial
   library, part of the kmc_utils package. kmc_remote provides a virtual
   button panel and simple one-touch commands for changing system
   variables which would involve multiple button operations on the real
   camera button console. Buttons, record settings (image size, record
   rate, shutter speed, trigger mode, burst mode), and playback rate
   control should be fully functional. All camera models are supported,
   as well as both PAL and NTSC video.

   [http://www.intel.com/PCcamera/] Intel PC Camera Pro Pack is one of
   the first webcams with USB ports. Also SONY has announced a webcam
   with USB port. See a survey at
   [http://www.steves-digicams.com/text_navigator.html] Steve's Digicams
   .
     ________________________________________________________________

16.9. Connection to Television Set

   If you have a ZV port in the laptop, it should be easy to connect it
   to a TV set, using either NSCA or PAL, but I don't know whether
   either works with Linux.
     ________________________________________________________________

16.10. Connection to Cellular Phone

   AFAIK there are two methods to connect a cellular phone to a laptop:
   via the infrared port (IrDA�) or via the serial port. See the
   Linux/IrDA� project for the current status of IrDA� connections. As
   far as I know only the Ericsson SH888, the Nokia 8110 and the Siemens
   S25 provide infrared support.
     ________________________________________________________________

16.11. Connection to Global Positioning System (GPS)
