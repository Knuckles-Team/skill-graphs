   customize the kernel. Though this task might seem difficult for the
   beginner it is highly recommended. Since this involves dangerous
   operations you need to be careful. But, if you can install a better
   kernel successfully, you've earned your intermediate Linux sysadmin
   merit badge. - I will not handle this here, because this topic is
   already covered in other documents.

   Compile a modular kernel with modules for CDROM, floppy, pcmcia,
   sound and any other peripherals. It will allow to delay loading of
   these modules until these devices are actually used, and it may help
   recover the system after a hardware failure, e.g. a bad CDROM,
   because a module can be removed and re-inserted without restarting
   the system.
     ________________________________________________________________

E.9. Tiny Applications and Distributions

   A small collection yet, but I'm looking for more information.

    1. BOA - "Lightweight and High Performance WebServer. boa is a
       single-tasking HTTP server. That means that unlike traditional
       web servers, it does not fork for each incoming connection, nor
       does it fork many copies of itself to handle multiple
       connections. It internally multiplexes all of the ongoing HTTP
       connections, and forks only for CGI programs (which must be
       separate processes.) Preliminary tests show boa is capable of
       handling several hundred hits per second on a 100 MHz Pentium."
    2. MGR - a graphical windows system, which uses much less resources
       than X.
    3. Low Bandwidth X:
       Alan Cox in LINUX REDUX February 1998 " .. there are two that
       handle normal applications very nicely. LBX (Low Bandwidth X) is
       the official application of the X11 Consortium (now
       [http://www.opengroup.org/] OpenGroup.
       [http://www.vigor.nu/dxpc/] Dxpc is the alternative most people
       prefer. These systems act as proxy X11 servers and compress
       datastreams by well over 50 percent for normal requests, often
       reaching a reduction to 25 percent of the original bandwidth
       usage. With dxpc, X Windows applications are quite usable over a
       28.8 modem link or across the Internet."
    4. [http://blackboxwm.sf.net/] blackbox - "This is a window manager
       for X. It is similar in many respects to such popular packages as
       Window Maker, Enlightenment, and FVWM2. You might be interested
       in this package if you are tired of window managers that are a
       heavy drain on your system resources, but you still want an
       attractive and modern-looking interface."
       Figure E-1. Screenshot of blackbox.
       [blackbox.png]
    5. [http://www.xfce.org] xfce is a lightweight and stable desktop
       environment for various UNIX systems.
    6. linux-lite - distribution based on a 1.x.x kernel for systems
       with only 2MB memory and 10MB harddisk. URL see above.
    7. [http://www.superant.com/smalllinux/] SmallLinux is a three disk
       micro-distribution of Linux and utilities. Based on kernel
       1.2.11. Root disk is ext2 format and has fdisk and mkfs.ext2 so
       that a harddisk install can be done. Useful to boot up on old
       machines with less than 4MB of RAM.
    8. cLIeNUX - client-use-oriented Linux distribution.
    9. [http://www.cs.vu.nl/~ast/minix.html] minix , not a Linux but a
       UNIX useful for very small systems, such as 286 CPU and 640K RAM
       . There is even X11 support named mini-x by
       [ftp://ftp.linux.org.uk/pub/linux/alan/] David I. Bell .
   10. screen - tiny but powerful console manager. John M. Fisk
       <fiskjm_AT_ctrvax.vanderbilt.edu> in
       [http://www.linuxgazette.com/issue01to08/lg_issue7.html#screen]
       LINUX GAZETTE :"It's a GUI, GUI, GUI, GUI world! " -- or so the
       major OS manufacturers would have you belief. Truth is, that
       while this is increasingly the case, there are times when the
       command line interface (CLI) is still a very good choice for
       getting things done. It's fast, generally efficient, and is a
       good choice on memory or CPU constrained machines. And don't
       forget that there are still a lot of very nifty things that can
       be done at the console."
   11. tinyirc - "A tiny, stripped down IRC Client. Doesn't have most of
       the more advance commands in the ircII family of IRC Clients, nor
       does it have any color, but it works, and it's tiny."
   12. JOVE Jonathans Own Version of Emacs, a small but powerful editor.
       .
     ________________________________________________________________

E.10. Hardware Upgrade

   You may also take into account to upgrade the hardware itself, though
   this may have some caveats, see chapter Open a Laptop Case above. If
   you need a survey about the possibilities, you can take a look at
   [http://repair4laptop.org/] Repair4Laptop: repair, disassemble,
   upgrade or mod laptops or notebooks.
     ________________________________________________________________

Appendix F. Ecology and Laptops

F.1. Ecological Comparisons of Computers

   Scientists of [http://www.reuse-computer.de/] ReUse project located
   at the [http://tu-berlin.de/] Technical University of Berlin recently
   compared the energy consumption of different computer types along the
   life cycle. The production of computers actually needs 535 kWh which
   is 10 % less than 4 years ago. Most of the energy will be consumed
   while the computer is used for example at work for 8 hours/day. The
   energy consumption of new computers with 2,5-3 GHz processors is even
   in the stand-bye-mode still 100 Watt, whereas a 1,4 GHz PC needs 80
   Watt and a 4 year old PC only needed 60 Watt. Therefore from the
   ecological point of view it is better to buy an old computer that
   didn't need the energy for a new production and which consumes less
   electricity while it is being used.

   LCD displays need less energy than other monitors. For this reason
   laptops are the most ecological types of the compared computers. They
   need the smallest amount of energy when they are used. And 3 year old
   laptops are better than new ones since their processors need less
   energy than new ones. There is also an article in the German computer
   magazine [http://heise.de/ct/] C't 21/ 2003.

   Some more stuff about Linux as a means to save our environment is
   included in the [http://computerecology.org/] Linux-Ecology-HOWTO.
     ________________________________________________________________

Appendix G. NeoMagic Graphics Chipset Series NM20xx

G.1. Introduction

   The NeoMagic graphics chipset series NM20xx has been popular in
   laptops build around 1996. For a long time this graphics chip was
   only supported by commercial X11 servers, since the middle of 1998
   RedHat provided a binary X11 server manufactured by PrecisionInsight.
   Since version 3.3.3 the appropriate X11 server is also available in
   XFree86.
     ________________________________________________________________

G.2. Textmode 100x37

   This chapter is a courtesy of Cedric Adjih , though I have changed
   some minor parts. Please note: Another method to achieve a better
   resolution in text mode is the use of the framebuffer driver (as
   explained in the X-Windows chapter above). This method requires
   kernel reconfiguration (some Linux distributions include an
   appropriate kernel already) and a new entry (vga=NNN) in
   /etc/lilo.conf. In text mode it works even with VESA BIOSes before
   version 2.0, at least on the models I could test it. Though the
   SVGATextMode method could be faster (couldn't check this yet).

   An apparently little known fact about the Neomagic chipset NM20xx is
   that you can run text mode in 100x37 (i.e. 800x600). This text mode
   is very nice (as opposed to the 80x25 which is ugly). I tried this
   with a HP OmniBook 800 and suppose it might work with other laptops
   using the NeoMagic chip, too.

   The main problem is that is a bit difficult to set up, and if you're
   going wrong with the commands SVGATextMode or restoretextmode some
   results on the LCD might be frightening. Although I didn't manage to
   break my LCD with many attempts going wrong, DISCLAIMER: THIS MIGHT
   DAMAGE YOUR HARDWARE. YOU HAVE BEEN WARNED. FOLLOW THE FOLLOWING
   INSTRUCTIONS AT YOUR OWN RISKS. I'M NOT RESPONSIBLE IF SOMETHING BAD
   HAPPENS.
     ________________________________________________________________

G.2.1. Survey

   You need to do three main steps:

    1. Enable Linux to boot in 800x600 textmode. The problem is that you
       won't see any text before the following two steps aren't done.
    2. Automatically run restoretextmode with correct register data.
    3. Automatically run SVGATextMode.
     ________________________________________________________________

G.2.2. More Details

   All the files I have modified, are available for now on
   [http://starship.python.net/crew/adjih/data/cda-omni-trick.tar.gz] my
   pages
     ________________________________________________________________

G.2.2.1. Enabling Linux to Boot in 800x600

   Recent kernels (2.2.x) need to be compiled with CONFIG_VIDEO_GFX_HACK
   defined. Default is off. (look in
   /usr/src/linux-2.2.x/arch/i386/boot/video.S)

   This is done by passing the parameter vga=770 to older kernels or
   vga=7 to 2.2.x kernels. Example with lilo.conf:

image=/boot/bzImage-modif
label=22
append="svgatextmode=100x37x8_SVGA" #explained later
vga=7
read-only
     ________________________________________________________________

G.2.2.2. Running restoretextmode and SVGATextMode at Boot Time

   Running restoretextmode and SVGATextMode at Boot Time. You must
   arrange to run restoretextmode <name of some textreg.dat file> and
   SVGATextMode 100x37x8_SVGA at boot time.

   An example textreg.dat for restoretextmode (obtained using
   savetextmode) is in my tar archive in tmp/, and an example
   /etc/TextConfig.

   Since I'm lazy, I've simply put SVGATextMode and restoretextmode in
   the /etc/rc.boot/kbd file from my Debian/GNU Linux which get executed
   at boot time (also available in the tar archive).
     ________________________________________________________________

G.2.2.3. Now the Key Point

   Annoying things will be displayed if you don't use the right
   SVGATextMode in the right video text mode: this is why I also pass
   the environmental variable "svgatextmode=100x37x8_SVGA" (arbitrary
   name) to the kernel (using append=xxx in lilo.conf) when I also set
   vga=7: the script /etc/rc.boot/kbd tests this variable and calls
   restoretextmode and SVGATextMode IF AND ONLY IF.
     ________________________________________________________________

G.2.3. Road Map

    1. Recompile the kernel 2.2.x with CONFIG_VIDEO_GFX_HACK
    2. Insert the restoretextmode with the correct parameter in the
       initialisation script, with no other changes.
    3. Boot with normal text mode (80x25) but restoretextmode: you
       should see the screen going to 100x37, but with only 80x25
       usable. Don't use SVGATextMode yet.
    4. It is much better to conditionnalize your initialize code as I
       did, to keep the possibility of booting in both modes: you may
       test this now with some reboots (starting restoretextmode or
       not).
    5. Boot with 100x37 text mode using parameter vga=7 (lilo.conf), you
       should see white background at some point, but the characters
       will be black on black. This is ok. You'll have to reboot blindly
       now.
    6. Insert the <path>/SVGATextMode 100x37x8_SVGA after the
       restoretextmode in initialization scripts.
    7. Reboot with vga=7 (lilo.conf)
    8. Should be OK now. Enjoy.
     ________________________________________________________________

Appendix H. Annotated Bibliography: Books For Linux Nomads

   Scott Mueller: Upgrading and Repairing Laptops, 2003

   From the publisher: "Scott Mueller goes where no computer book author
   has gone before right past all the warranty stickers, the hidden
   screws, and the fear factor to produce a real owner's manual that
   every laptop owner should have on his desk. This book shows the
   upgrades users can perform, the ones that are better left to the
   manufacturer, and how to use add-on peripherals to make the most of a
   laptop. The CD contains one-of-a-kind video showing just what's
   inside a portable PC."
   [http://www.amazon.com/exec/obidos/ASIN/0789728001/lilaclinuxwithla]
   Amazon Order.

   Other resources:

     * [http://repair4laptop.org/] upgrading, repairing and modding
       laptops or notebooks
     * [http://repair4pda.org/] upgrading, repairing and modding PDAs
       and HandHelds
     * [http://repair4mobilephone.org/] upgrading, repairing and modding
       mobile (cell) phones
     * [http://repair4player.org/] upgrading, repairing and modding
       mobile media players

   Chris Hurley, Michael Puchol, Russ Rogers, Frank Thornton: WarDriving
   - Drive, Detect, Defend, A Guide to Wireless Security, 2004

   From the Publisher: "Wardriving has brought some of the top people in
   the wireless industry together to put together a truly informative
   book on what wardriving is and the tools that should be part of any
   IT department's arsenal that either has wireless or is looking to
   deploy it." -John Kleinschmidt, Michiganwireless.org Founder The
   practice of WarDriving is a unique combination of hobby, sociological
   research, and security assessment. The act of driving or walking
   through urban areas with a wireless-equipped laptop to map both
   protected and un-protected wireless networks has sparked intense
   debate amongst lawmakers, security professionals, and the
   telecommunications industry. This first ever book on WarDriving is
   written from the inside perspective of those who have created the
   tools that make WarDriving possible and those who gather, analyze,
   and maintain data on all secured and open wireless access points in
   very major, metropolitan area worldwide. These insiders also provide
   the information to secure your wireless network before it is
   exploited by criminal hackers. Wireless networks have become a way of
   life in the past two years. As more wireless networks are deployed
   the need to secure them increases. This book educates users of
   wireless networks as well as those who run the networks about the
   insecurities associated with wireless networking. This effort is
   called WarDriving. In order to successfully WarDrive there are
   hardware and software tool required. This book covers those tools,
   along with cost estimates and recommendations. Since there are
   hundreds of possible configurations that can be used for WarDriving,
   some of the most popular are presented to help readers decide what to
   buy for their own WarDriving setup. Many of the tools that a
   WarDriver uses are the same tools that could be used by an attacker
   to gain unauthorized access to a wireless network. Since this is not
   the goal of a WarDriver, the methodology that users can use to
   ethically WarDrive is presented. In addition, complete coverage of
   WarDriving applications, such as NetStumbler, MiniStumbler; and
   Kismet, are covered."
   [http://www.amazon.com/exec/obidos/ASIN/1931836035/lilaclinuxwithla]
   Amazon Order.

   TuxMobil Resources:

     * [http://tuxmobil.org/wireless_unix.html] Linux and Wireless LANs
     * [http://tuxmobil.org/manet_linux.html] Linux and Mobile AdHoc
       Networks - MANETs
     * [http://tuxmobil.org/wireless_community.html] Linux and Wireless
       Communities Around the World
     * [http://tuxmobil.org/linux_wireless_access_point.html] Linux and
       Wireless Access Points - WLAN APs
     * [http://tuxmobil.org/linux_wireless_sniffer.html] Linux and
       Wireless Sniffer Applications

   Isidor Buchmann: Batteries in a Portable World - A Handbook on
   Rechargeable Batteries for Non-Engineers, 2001

   From the Publisher: "Batteries in a Portable World fills a definite
   need for practical information about rechargeable batteries. Quite
   often, performance specifications for batteries and chargers are
   based on ideal conditions. Manufacturers carry out battery tests on
   brand new equipment and in a protected environment, removed from the
   stress of daily use. In Batteries in a Portable World, Mr. Buchmann
   observes the battery in everyday life in the hands of the common
   user. By reading Batteries in a Portable World, you will acquire a
   better understanding of the strengths and limitations of the battery.
   You will learn how to prolong battery life; become familiar with
   recommended maintenance methods and discover ways to restore a weak
   battery, if such a method is available for that battery type. Knowing
   how to take care of your batteries prolongs service life, improves
   reliability of portable equipment and saves money. Best of all,
   well-performing batteries need replacement less often, reducing the
   environmental concern of battery disposal."
   [http://www.amazon.com/exec/obidos/ASIN/0968211828/lilaclinuxwithla]
   Amazon Order.

   TuxMobil Resources:

     * [http://tuxmobil.org/energy_laptops.html] Power Supplies for
       Laptops and PDAs
     * [http://tuxmobil.org/mobile_battery.html] Linux Tools for Laptop,
       Notebook and PDA Batteries

   [http://www.verysecurelinux.com/] Bob Toxin: Real World Linux
   Security: Intrusion Detection, Prevention, and Recovery 2nd Ed., 2002

   This book contains a chapter about mobile security.
   [http://www.amazon.com/exec/obidos/ASIN/0130464562/lilaclinuxwithla]
   Amazon Order.

   TuxMobil Resources:

     * [http://tuxmobil.org/mobile_security.html] Security for Mobile
       Linux Computers
     * [http://tuxmobil.org/stolen_laptops.html] Theft and Loss
       Protection for Linux Laptops, Notebooks and PDAs
     ________________________________________________________________

Appendix I. Resources for Specific Laptop Brands

   Certain laptops have found some more enthusiastic Linux users, than
   other models. This list is probably not comprehensive:
     ________________________________________________________________

I.1. COMPAQ

   [http://www.zenspider.com/~pwilk/aero_stuff.html] COMPAQ Contura
   Aero-FAQ.

   The latest version of the
   [http://www.cs.nmsu.edu/~pfeiffer/index_old.html#linux] Linux Compaq
   Concerto Pen Driver is available from Joe Pfeiffer's home page.
     ________________________________________________________________

I.2. DELL

   Mailing list at [http://www.egroups.com/group/linux-dell-laptops]
   linux-dell-laptops

   Manufacturer Linux information:
   [http://linux.dell.com/desktops.shtml] DELL
     ________________________________________________________________

I.3. IBM/Lenovo(TM) ThinkPad

   ThinkPad Configuration Tool for Linux by Thomas Hood
   [http://tpctl.sourceforge.net/] tpctl

   Running Linux on IBM(TM)ThinkPads, to join send an email to
   linux-thinkpad-subscribe_at_topica.com, to post send mail to
   linux-thinkpad_at_topica.com . See
   [http://www.topica.com/lists/linux-thinkpad/] here for details.

   [http://www.slack.stanford.edu/~strauman/pers/tp4utils/] TrackPoint
   driver by Till Straumann.
     ________________________________________________________________

I.4. Sony VAIO

   For installation on VAIOs via external CD drive, see chapter
   Installation above. Some hints for the Jog-Dial you may find in the
   chapter Mice Species. The SONY VAIO C1 series includes some models,
   which are based on the first dedicated mobile CPU, the CRUSOE. The
   CRUSOE is manufactured by [http://www.transmeta.com/] TransMeta . At
   TransMeta you may find information about the binary compatibility of
   the CRUSOE. The [http://samba.org/picturebook/] Sony PCG-C1XS
   Picturebook Camera Capture program captures images and movies on a
   Sony VAIO picturebook PCG-C1XS, taking advantage of the built in CCD
   camera and hardware JPEG encoder. It features PPM capture, JPEG
   capture (hardware JPEG), AVI capture of MJPEG, MJPEG capture of
   separate frames (for MPEG encoding), setting of
   brightness/contrast/etc., and a 1:4 sub-sampling option.

   There is also a VAIO C1 related Linux mailing list, too
   <linux-c1_at_gnu.org>.

   [http://frijoles.com/c1-info/faq.html] Sony Vaio C1 FAQ mostly
   MS-Windows related, but contains useful hardware information and a
   mailing list.

   The [http://spicd.raszi.hu/] SONY VAIO SPIC daemon is a fast and
   small hack for create a working apmd to Sony VAIO laptops. It uses
   the sonypi kernel module to detect the AC adapter status and the LCD
   backlight, and cpufreq for CPU frequency change.

   [http://www.alcove-labs.org/en/software/sonypi/] spicctrl uses the
   sonypi interface provided by /dev/sonypi and the Linux kernel.
     ________________________________________________________________

I.5. Toshiba

   [http://www.buzzard.me.uk/toshiba/index.html] Toshiba Linux Utilities
   are a set of Linux utilities for controlling the fan, supervisor
   passwords, and hot key functions of Toshiba Pentium notebooks.
   Utilities to change supervisor passwords and adjust power/battery
   modes are included. There is a KDE package Klibreta, too.

   Mailing lists:
   [http://www.onelist.com/subscribe.cgi/linux-on-portege]
   linux-on-portege , Linux on Toshiba Satellite 40xx linux-tosh-40xx
   <majordomo_at_geekstuff.co.uk>.

   Toshiba itself offers now
   [http://linux.toshiba-dme.co.jp/linux/index.htm] Toshiba Linux
   Support (Japanese branch) and
   [http://newsletter.toshiba-tro.de/main/index.html] Toshiba Linux
   Support (German branch) .
     ________________________________________________________________

Appendix J. Credits

   I would like to thank the many people who assisted with corrections
   and suggestions. Their contributions have made this work far better
   than I could ever have done alone. Especially I would like to thank:

     * First of all Kenneth E. Harker , from his page
       [http://www.linux-on-laptops.com/] Linux on Laptops I have
       included much material into this HOWTO, but didn't always quote
       him verbatim.
     * The other authors from [http://tldp.org/] THE LINUX DOCUMENTATION
       PROJECT - TLDP .
     * The members of the Linux/IrDA� Project .
     * The members of the Linux-Laptop Mailing List.
     * The members of the Debian-Laptop Mailing List.
     * The members of the SuSE-Laptop Mailing List.
     * The visitors and contributors of my [http://tuxmobil.org/]
       TuxMobil project.
     * Cedric Adjih , wrote the chapter about the NeoMagic chipset.
     * Amlaukka
     * Michele Andreoli, maintainer of [http://sunsite.auc.dk/mulinux/]
       muLinux.
     * [http://www.procyon.com/~pda/lphdisk/] Patrick D. Ashmore
     * Ben Attias .
     * Gerd Bavendiek , [http://netenv.sourceforge.net] netenv
     * John Beimler , provided the URL of photopc.
     * [http://www.nemein.com] Henri Bergius
     * Ludger Berse .
     * Stephane Bortzmeyer for his suggestions about email with UUCP,
       the use of CVS or related tools to synchronize two machines, and
       the noatime mount option.
     * Lionel, "trollhunter" Bouchpan-Lerust-Juery
     * Felix Braun .
     * David Burley
     * David Chien
     * Sven Crouse for information about touchpads
     * Eric wrote how to transfer pictures from a digital camera.
     * [http://home.snafu.de/ingo.dietzel/] Ingo Dietzel , for his
       patience with the project.
     * Brian Edmonds
     * Peter Englmaier , provided the chapter about a sophisticated
       email setup.
     * Joel Eriksson , for information about Atari laptops.
     * Heiko Ettelbrueck
     * Gledson Evers , started the Portuguese translation.
     * Klaus Franken .
     * [http://www.guido.germano.com] Guido Germano , for information
       about the Macintosh Powerbook 145B.
     * Bill Gjestvang .
     * [http://splitbrain.org/] Andreas Gohr prepared some sections of
       the PDA chapter and more
     * Alessandro Grillo , started the Italian translation.
     * Sven Grounsell [http://tuxhilfe.de/] TuxHilfe
     * Mikael Gueck
     * Marcus Hagn has written some powersaving tweaks
     * W. Wade, Hampton , did much of spell, grammar and style checking
       and added many valuable information.
     * Sebastian Henschel prepared some sections of the PDA chapter and
       more
     * David Hinds, the maintainer of the PCMCIA-CS package.
     * Karsten Hopp
     * Scott Hurring
     * JK
     * Uwe SV Kubosch , hints about Amiga
     * Jeremy D. Impson provided instructions about installing on a
       Toshiba Libretto 50CT [http://nwc.syr.edu/~jdimpson] Jeremy D.
       Impson
     * Adrian D. Jensen , provided some notes on removable hard disks
     * Steven G. Johnson , provided most of the information about
       Apple/Macintosh m68k machines and LinuxPPC on the PowerBook.
     * Dan Kegel , pointed me to the Toshiba Linux page.
     * [http://www.mk-stuff.de/] Michael Kupsch
     * Gilles Lamiral for providing the PLIP Install-HOWTO.
     * Sian Leitch , suggestions on style
     * [http://www.leo.org/~loescher/] Stephan Loescher
     * [http://home.pages.de/~lufthans/] LuftHans , announced this HOWTO
       to the maintainer of the [http://tldp.org/HOWTO/Hardware-HOWTO/]
       Hardware-HOWTO.
     * Anderson MacKay , [http://linux.rice.edu] RLUG - Rice University
       Linux User Group , gave many different detailed recommendations.
