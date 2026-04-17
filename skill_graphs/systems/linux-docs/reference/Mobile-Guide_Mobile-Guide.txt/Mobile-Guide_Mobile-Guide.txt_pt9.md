   resumed. A solution is to set up the proxy script so that it calls a
   mixer application after resume.

   From the apmsleep(1) man page: Some computers, especially laptops,
   can wake up from a low-power suspend to DRAM mode using the Real-time
   clock (RTC) chip. Apmsleep can be used to set the alarm time in the
   RTC and to go into suspend or standby mode. An interrupt from the RTC
   causes the computer to wake-up. The program detects this event, by
   waiting for a leap in the kernel time and terminates successfully. If
   no time leap occurs within one minute, or something goes wrong, the
   exit value will be non-zero. Apmsleep is part of the apmd package.

   In 2001 Richard Gooch wrote a simple apmd alternative which is
   available in the [http://www.atnf.csiro.au/~rgooch/linux/] pmutils
   package.

   Also, take a look at apmcd (apm based crontab) at
   [ftp://ftp.binary9.net/pub/linux/] ftp://ftp.binary9.net/pub/linux/ .
   This tool was written by [http://mrnick.binary9.net/] Nicolas J. Leon
   <nicholas_AT_binary9.net>.
     ________________________________________________________________

12.18.3. Caveats

   If you use another operating system at the same computer make sure
   that its "suspend" and "hibernate" features don't write to partitions
   that are used by Linux.
     ________________________________________________________________

12.18.4. Troubleshooting

   If your machine worked with 2.0.x kernels but not with the 2.2.x
   series, take this advice from Klaus Franken kfr_AT_klaus.franken.de :
   "The default changed in 2.2. Search in the init-scripts for halt and
   change it to halt -p or poweroff. See man halt , if you don't have
   this option you need a newer version of halt." You may find it in the
   SysVinit package.

   On some new machines (for instance HP Omnibook 4150 - 366 MHz model)
   when accessing /proc/apm, you may get a kernel fault general
   protection fault: f000. [http://www.canb.auug.org.au/~sfr/] Stephen
   Rothwell explaines: "This is your APM BIOS attempting to use a real
   mode segment while in protected mode, i.e. it is a bug in your BIOS.
   .. We have seen a few of these recently, except all the others are in
   the power off code in the BIOS where we can work around it by
   returning to real mode before attempting to power off. Here we cannot
   do this."

   According to Kernel docs Documentation/Configure.help: "Some other
   things you should try when experiencing seemingly random, weird
   problems:

    1. make sure that you have enough swap space and that it is enabled
       swapon -s.
    2. pass the no-hlt option to the kernel.
    3. switch on floating point emulation in the kernel and pass the
       no387 option to the kernel.
    4. pass the floppy=nodma option to the kernel.
    5. pass the mem=4M option to the kernel (thereby disabling all but
       the first 4 MB of RAM).
    6. make sure that the CPU is not over clocked (doesn't seem suitable
       for mobile machines).
    7. read the [http://www.bitwizard.nl/sig11/] sig11 FAQ .
    8. disable the cache from your BIOS settings.
    9. install a fan for the video card or exchange video RAM (doesn't
       seem suitable for mobile machines).
   10. install a better fan for the CPU (doesn't seem suitable for
       mobile machines).
   11. exchange RAM chips (doesn't seem suitable for mobile machines).
   12. exchange the motherboard (doesn't seem suitable for mobile
       machines).
     ________________________________________________________________

12.18.5. APM and PCMCIA

   From the PCMCIA-HOWTO: "Card Services can be compiled with support
   for APM (Advanced Power Management) if you've configured your kernel
   with APM support. ... The PCMCIA modules will automatically be
   configured for APM if a compatible version is detected on your
   system. Whether or not APM is configured, you can use cardctl suspend
   before suspending your laptop, and cardctl resume after resuming, to
   cleanly shut down and restart your PCMCIA cards. This will not work
   with a modem that is in use, because the serial driver isn't able to
   save and restore the modem operating parameters. APM seems to be
   unstable on some systems. If you experience trouble with APM and
   PCMCIA on your system, try to narrow down the problem to one package
   or the other before reporting a bug. Some drivers, notably the PCMCIA
   SCSI drivers, cannot recover from a suspend/resume cycle. When using
   a PCMCIA SCSI card, always use cardctl eject prior to suspending the
   system.".
     ________________________________________________________________

12.18.6. APM and Resuming X Windows

   Some machines have APM firmware that fails to save and restore
   display controller chip registers across a suspend. Earlier versions
   of the XFree86 X server did not restore the screen properly after
   resume, a problem which was addressed by
   [http://www.linuxlaptops.com/ll/xresume.html] Linux Laptops. However,
   contemporary versions of XFree86 mostly do the right thing.

   Sometimes X and APM don't work smoothly together. The machine might
   even hang. A recommendation from Steve Rader: Some linux systems have
   their X11 server hang when doing apm -s. Folks with this affliction
   might want to switch to the console virtual terminal and then suspend
   chvt 1; apm -s as root, or, more appropriately sudo chvt 1; sudo apm
   -s. I have these commands in a script, say, my-suspend and then do
   xapmload --click-command my-suspend .
     ________________________________________________________________

12.18.7. Software Suspend

   [http://www.sourceforge.net/projects/swsusp] Software suspend enables
   the possibility of suspending a machine. It doesn't need APM. You may
   suspend your machine by either pressing Sysrq-d or with swsusp or
   shutdown -z (patch for sysvinit needed). It creates an image which is
   saved in your active swaps. By the next booting the kernel detects
   the saved image, restores the memory from it and then it continues to
   run as before you've suspended. If you don't want the previous state
   to continue use the noresume kernel option.

   Software suspends may even be better than hibernate, because now I
   can suspend my Linux system, boot into Microsoft Windows, perform a
   few illegal operations and be shut down, and then restart my Linux
   setup exactly where I left off! This is something that cannot be done
   with hibernation, since that always restores the last state that you
   suspended from, be it Microsoft Windows or Linux. So if I want to
   switch to Microsoft Windows to play games or do anything else, I can
   leave my Linux desktop exactly as it is and return to how I left it.

   In recent 2.6 kernels SoftWareSuspend is part of the kernel. You may
   find it in the section Power Management. But there are also backports
   to 2.4 available.

   Since the original Software Suspend code was written by Gabor Kuti
   and Pavel Machek back in 1998, three different implementations have
   been created for the 2.6 kernel, all forks of the same original
   codebase.

   [http://www.tuxonice.net/] TuxOnIce, former known as Software Suspend
   2, has a long feature list, including the ability to cancel a suspend
   by pressing Escape, image compression to save time and space, a
   versatile plugin architecture, and support for machines with Highmem,
   preemption and SMP.
     ________________________________________________________________

12.18.8. Tips and Tricks

12.18.8.1. Battery Status on Text Console

   You may use the following entry in .bashrc to show the battery level
   on the command prompt.
     ________________________________________________________________

12.18.8.1.1. When Using APM

export PS1="\$(cat /proc/apm | awk '{print \$7}') \h:\w\$ "
     ________________________________________________________________

12.18.8.1.2. When Using ACPI

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
 if [ `cat /proc/acpi/battery/BAT0/state | grep present: |cut -d\  -f18` = "ye
s" ]; then
  {
   CAPACITY=`cat /proc/acpi/battery/BAT0/info |grep "design capacity:"|cut -d\
  -f11`
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
       if [ `cat /proc/acpi/battery/BAT0/state | grep present: |cut -d\  -f18`
 = "no" ]; then
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
     PS1='\[\e[$(acpi_color)m\][$(acpi_charge)$(acpi_percent)][\t] \u:\w\$>\[\
e[0;37m\] '
   }

   #  linux  console
   if  [  "$TERM"  =  "linux"  ];  then
     PROMPT_COMMAND=acpi_color_prompt
   fi

   function  echo_acpi
   {
     echo -n "($(acpi_charge)$(acpi_percent)) "
   }
     ________________________________________________________________

12.18.8.2. Debian GNU/Linux

   All "normal" Debian GNU/Linux kernels are APM capable, they just need
   an append line added to the boot loader configuration file (e.g.
   /etc/lilo.conf.
append="apm=on"

   You might use the following parameters (with the appropriate changes)
   in your boot loader configuration file (e.g. /etc/lilo.conf to
   experiment with ACPI and APM, when compiled in the same kernel. Usage
   of APM and ACPI at the same time doesn't work, see Kernel docs for
   details.
append="acpi=off apm=on"
     ________________________________________________________________

12.19. ACPI

12.19.1. Related Documentation

    1. [http://xtrinsic.com/geek/articles/acpi.phtml] ACPI-HOWTO I by
       Emma Jane Hogbin
    2. [http://www.columbia.edu/~ariel/acpi/acpi_howto.txt] ACPI-HOWTO
       II by Ariel Glenn. This document describes how to compile,
       install, and use the ACPI driver for Linux and its associated
       applications.
    3. [http://www.cpqlinux.com/acpi-howto.html] ACPI-HOWTO III
    4. [http://acpi.sourceforge.net/wiki] ACPI4Linux Project and its
       [http://acpi.sourceforge.net/wiki] Wiki
    5. [http://www.acpi.info/] ACPI Info provides the ACPI
       specification.
    6. Section 12.3 the CPU chapter of this guide
     ________________________________________________________________

12.19.2. ACPI Details

   ACPI stands for Advanced Configuration and Power Interface. This is a
   specification by Toshiba, Intel and Microsoft. Besides many other
   things it also defines power management. This is why it is often
   compared to APM.

   You might use the following parameters (with the appropriate changes)
   in your boot loader configuration file (e.g. /etc/lilo.conf to
   experiment with ACPI and APM, when compiled in the same kernel. Usage
   of APM and ACPI at the same time doesn't work, see Kernel docs for
   details.
append="acpi=on apm=off"

   The [http://sourceforge.net/projects/acpi] Linux ACPI Project is
   committed to the development of fundamental ACPI (Advanced
   Configuration and Power Interface) components for Linux. This
   includes a generic ACPI table parser, AML interpreter, bus and device
   drivers, policy, user interface, and support tools.

   The [http://www.netego.de/hpc?p=acpipower&l=en] E-AcpiPower epplet is
   based on E-Power. It is modified to read battery status information
   using the new acpi kernel module, making it much more accurate and
   reliable than the old APM method.

   [http://rffr.de/acpi] TCL/TK script which allows setting the ACPI CPU
   performance state using a graphical interface under Linux.

   [http://grahame.angrygoats.net/acpi.shtml] Linux ACPI client is a
   command-line tool, similar to the apm command, that provides
   information on battery status, AC power, and thermal readings.
     ________________________________________________________________

12.20. Power Management Unit - PMU (PowerBook)

   PowerBooks don't support the APM specification, but they have a
   separate protocol for their PMU (Power Management Unit). There is a
   free (GPL) daemon called pmud that handles power management; it can
   monitor the battery level, put the machine to sleep, and set
   different levels of power consumption. It was written by Stephan
   Leemburg. There is also an older utility called snooze available from
   the same sites that just puts the PowerBook to sleep.
   [http://pbbuttons.berlios.de/] PBButtons now includes the
   functionality of pmud.

   Cron works fine on my laptop as I never shut it off completely. I
   only put it to sleep. When it wakes up, the unexecuted cron jobs from
   the sleep period all run.

   This part is a courtesy of Steven G. Johnson.
     ________________________________________________________________

12.21. Batteries



   May the batteries be with you.
     Unknown AuthorEss

   For information about available battery types, take a look at the
   Hardware Features chapter above.

   Please see the [http://tldp.org/HOWTO/Battery-Powered/] Battery
   Powered Linux Mini-HOWTO and the
   [http://tuxmobil.org/mobile_battery.html] TuxMobil battery page for
   further information. A survey of
   [http://tuxmobil.org/energy_laptops.html] other means to supply power
   for mobile computers e.g. solar energy is available at TuxMobil. For
   general information about batteries see the
   [http://www.technick.net/public/code/cp_dpage.php?aiocp_dp=guide_bpw2
   _00_toc] Battery FAQ.

   [http://www.canb.auug.org.au/~sfr/] Stephen Rothwell proposed a patch
   that will add multiple battery support to the kernel APM.

   From the mobile-update page (modified by WH): Discharge the battery.
   If your battery runs only for about 20 minutes, you probably suffer
   from memory effects. Most laptops do not discharge the battery
   properly. With low powered devices like old computer fans they can be
   discharged completely. This removes memory effects. You should do so
   even with LiIon batteries, though they don't suffer much from memory
   effect (the manual of an IBM(TM) Thinkpad says to cycle the batteries
   through a full charge/discharge cycle 3 times every few months or
   so).

   Warning

   Try this at your own risk! Make sure the voltage of the fans is
   compatible to your battery. It works for me.

   In the US, this company has most batteries for anything and can
   rebuild many that are no longer manufactured: Batteries Plus, 2045
   Pleasant Hill Road, Duluth, GA 30096 +1 770 495 1644.

   The [http://karl.jorgensen.com/battery-stats/] battery-stats package
   collects statistics about the (lack of) charge on laptop batteries.
   It also contains a simple graph utility to show the battery charge
   over time or detect a misbehaviour of the battery which might
   announce a coming end of batterylife. Battery-stats knows nothing
   about electrochemical stuff going on inside batteries - hence it will
   not try to make any predictions whatsoever. But somebody with
   knowledge of batteries should be able to tell whether they are
   behaving OK. This package uses APM; there is no support for ACPI yet.

   [http://ibam.sourceforge.net/] IBAM (Intelligent BAttery Monitor) is
   an advanced battery monitor for laptops, which uses statistical and
   adaptive linear methods to provide accurate estimations of minutes of
   battery left or of the time needed until full recharge. This package
   uses APM; there is no support for ACPI yet.

   [http://www-leland.stanford.edu/~bbense/toys/] A hacked rclock .
   Booker C. Bense has hacked the rclock program to include a simple
   battery power meter on the clock face.

   [http://www.jaist.ac.jp/~daisuke/Linux/xbatstat.html] xbatstat . A
   battery level status checker for Linux and X.
     ________________________________________________________________

12.21.1. Smart Battery Support

   The [https://sourceforge.net/projects/sbs-linux/] sbsutils package is
   a set of utilities programs to handle the Smart Battery on laptops,
   it offers Linux kernel & ACPI support for the Smart Battery System
   found in some laptop computers.
     ________________________________________________________________

12.21.2. How to Improve Battery Uptime

   These are the most important factors which have influence on the
   battery uptime. Please see the appropriate chapters for power saving
   tips:

     * Section 12.3 CPU
     * fan
     * Section 12.22 memory
     * Section 12.6graphics card
     * Section 12.33 hard disk drive
     * Section 12.32 optical drive

   Getting your computer to use the least amount of power can be
   problematic. Intel's [http://www.linuxpowertop.org/index.php]
   http://www.linuxpowertop.org/index.php project provides information
   on reducing power usage, tips, and tricks for Intel-based computers
   running Linux. As a first step, Intel has released PowerTOP, a tool
   that helps you find what software is using the most power. By fixing
   (or closing) these applications or processes, you can immediately see
   the power savings in the tool. You'll also see the estimated time
   left for battery power if you are running a laptop. The Tips & Tricks
   page has fixes for a lot of the issues that are already found.
     ________________________________________________________________

12.22. Memory

   Unfortunately some laptops come with proprietary memory chips. So
   they are not interchangeable between different models. But this seems
   changing. With some models it's very difficult to install the memory
   if you have to open the case in detail. But this is also changing.
   Places were the memory can be changed easily are dedicated
   maintenance cover on the backside or often if you only have to remove
   the keyboard.
     ________________________________________________________________

12.23. Plug-and-Play Devices (PnP)

   The Plug and Play driver project for Linux is a project to create
   support within the Linux kernel (see [http://linux.org/] Linux.Org
   for more information) for handling Plug and Play (and other semi-PnP)
   devices in a clean, consistent way. It aims to allow a driver of any
   type of hardware to have this hardware configured by the PnP driver
   in the kernel. This driver is then notified when the device is
   reconfigured, or even removed from the system, so as to allow for
   graceful action in these circumstances.

   ISA PnP tools is another useful package.

   The latest PCMCIA driver package (>3.1.0) has utilities lspnp and
   setpnp to manipulate PNP settings.
     ________________________________________________________________

12.24. Docking Station / Port Replicator

12.24.1. Definitions

   First some definitions. There is a difference between docking station
   and port replicator.

   I use the term docking station for a box which contains slots to put
   some interface cards in, and space to put a harddisk, etc. in. This
   box can be permanently connected to a PC. A port replicator is just a
   copy of the laptop ports which may be connected permanently to a PC.
     ________________________________________________________________

12.24.2. Other Solutions

   I don't use a docking station myself. They seem really expensive and
   I can't see any usefulness. Alright you have to deal with some more
   cables, but is it worth so much money? Docking stations are useful in
   an office environment when you have a permanent network connection,
   or need the docking station's expansion bus slots (e.g. for some
   excotic SCSI device).

   Also all docking stations I know are proprietary models, so if you
   change your laptop you have to change this device, too. I just found
   one exception a docking station which connects to your laptop via
   IrDA� the IRDocking IR-660 by [http://www.tekram.com/] Tekram . It
   supports these connectors: 10Base-T (RJ-45); PS/2 Keyboard; PS/2
   Mouse; 25-Pin Printer Port (LPT); IR Transceiver; Power (6 VDC). So
   it seems that a VGA port and a port to connect a desktop PC directly
   are missing. This device should work with Linux/IrDA�, though I
   couldn't check it out.

   I would prefer to buy a PC instead and connect it via network to the
   laptop.

   Or use an external display, which usually works well as described
   above, and an external keyboard and mouse. If your laptop supports an
   extra PS/2 port you may use a cheap solution a Y-cable, which
   connects the PS/2 port to an external keyboard and an external
   monitor. Note: Your laptop probably has support for the Y-cable
   feature, e.g. the COMPAQ Armada 1592DT.
     ________________________________________________________________

12.24.3. Docking Station Connection Methods

   AFAIK there are four solutions to connect a laptop to a docking
   station:

    1. SCSI port (very seldom)
    2. parallel port
    3. (proprietary) docking port (common)
    4. USB (often offered by third party manufacturers)

   From Martin J. Evans "The main problem with docking stations is
   getting the operating system to detect you are docked. Fortunately,
   you can examine the devices available in /proc and thus detect a
   docked state. With this in mind a few simple scripts is all you need
   to get your machine configured correctly in a docked state.

   You may want to build support for the docking station hardware as
   modules instead of putting it directly into the kernel. This will
   save space in your kernel but your choice probably largely depends on
   how often you are docked.

   1) Supporting additional disks on the docking station SCSI card

   To my mind the best way of doing this is to:

    1. Either build support for the SCSI card into the kernel or build
       it as a module.
    2. Put the mount points into /etc/fstab but use the "noauto" flag to
       prevent them from being mounted automatically with the mount -a
       flag. In this way, when you are docked you can explicitly mount
       the partitions off any disk connected to the docking station SCSI
       card.

   2) Supporting additional network adaptors in the docking station

   You can use a similar method to that outlined above for the graphics
   card. Check the /proc filesystem in your rc scripts to see if you are
   docked and then set up your network connections appropriately. "

   Once you determine this information, you may use a script, similar to
   the following example, to configure the connection to your docking
   station at startup. The script is provided by Friedhelm Kueck:

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
     ________________________________________________________________

12.24.4. Universal USB Port Replicators

   I have used a Typhoon USB 2.0 7in1 Docking Station made by
   [http://www.anubisline.com/] Anubis P/N 83057 to check the Linux
   compatibility of such devices. Actually this device should be named
   port replicator, because it does not have any extension slots. This
   device doesn't have a VGA port to connect to an external display.
   Only a few USB docking stations have this feature. It would be nice
   to get a report whether a VGA port works or not. Tested with laptop
   COMPAQ M700 (USB 1.1) and custom made kernel 2.6.1. Note the port
   replicator didn't work with an Apple PowerBook G4.

   How does its different ports work with Linux:

     * USB 2.0 A-type downstream: works with external hard disk and
       mouse out of the box
     * USB 2.0 A-type downstream: see above
     * PS/2 keyboard: works out of the box
