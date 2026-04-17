   Memory Card International Association) is an international standards
   body and trade association with over 200 member companies that was
   founded in 1989 to establish standards for Integrated Circuit cards
   and to promote interchangeability among mobile computers where
   ruggedness, low power, and small size were critical. As the needs of
   mobile computer users have changed, so has the PC Card Standard. By
   1991, PCMCIA had defined an I/O interface for the same 68 pin
   connector initially used for memory cards. At the same time, the
   Socket Services Specification was added and was soon followed by the
   Card Services Specification as developers realized that common
   software would be needed to enhance compatibility. " The cards are
   available in different formats: Type I, II, III.

   A quotation from the ../Documentation/Changes file: "PCMCIA (PC Card)
   support is now partially implemented in the main kernel source. Pay
   attention when you recompile your kernel. If you need to use the
   PCMCIA-CS modules, then don't compile the kernel's PCMCIA support. If
   you don't need to use the PCMCIA-CS modules (i.e. all the drivers you
   need are in the kernel sources), then don't compile them; you won't
   need anything in there. Also, be sure to upgrade to the latest
   PCMCIA-CS release." Further information you may get from the
   README-2.4 included with this package.

   You may find an example kernel configuration for laptops in the
   Section 14.3.
     ________________________________________________________________

14.1.2. Powermanagement

   At the moment there are two power management drivers in the linux
   kernel (AFAIK). They each have different userspace interfaces
   /proc/apm/ and /dev/apmctl/ and /proc/acpi/ or something.

   For further information see the page of
   [http://john.fremlin.de/linux/offbutton/index.html] John Fremlin . He
   has also written a program named powermanager.

   With kernel 2.4 there is ACPI available, see ACPI chapter below.

   The SuSE
   [http://forge.novell.com/modules/xfmod/cvs/cvsbrowse.php/powersave/]
   Powersave Daemon provides battery, temperature, AC, and CPU frequency
   control and monitoring along with proper suspend to disk/RAM and
   standby support with shell hooks that are easy to extend. It supports
   APM and ACPI machines and can control a hard disk's advanced power
   and acoustic management settings. It is perfect for laptops and
   workstations that need to run quietly with low power consumption, or
   switch to full performance mode if needed. Self definable power
   schemes give full control over power control features and allow easy
   and automatic switching between performance or power saving settings
   for each hardware component.
     ________________________________________________________________

14.1.3. Hotplug

   There is a new
   [http://lists.sourceforge.net/lists/listinfo/linux-hotplug-devel]
   mailing list for developers interested in any aspects of the Linux
   kernel hotplug ability and functionality. This would include (but is
   not restricted to) USB, PCMCIA, SCSI, Firewire, and probably PCI
   developers. There is an initial
   [http://sourceforge.net/projects/linux-hotplug/] SourceForge site.

   Kernel Support for Hot-Plugable Devices
CONFIG_HOTPLUG
  Say Y here if you want to plug devices into your computer while
  the system is running, and be able to use them quickly. In many
  cases, the devices can likewise be unplugged at any time too.

  One well known example of this is PCMCIA- or PC-cards, credit-card
  size devices such as network cards, modems or hard drives which are
  plugged into slots found on all modern laptop computers. Another
  example, used on modern desktops as well as laptops, is USB.

  Enable HOTPLUG and KMOD, and build a modular kernel. Get
  [http://linux-hotplug.sourceforge.net] agent software
  and install it. Then your kernel will automatically call out to a
  user mode "policy agent" (/sbin/hotplug) to
  load modules and set up software needed to use devices as
  you hotplug them.
     ________________________________________________________________

14.2. Kernel 2.6

14.2.1. PCMCIA

   [http://kernel.org/pub/linux/utils/kernel/pcmcia/pcmcia.html]
   PCMCIAutils contains hotplug scripts and initialization tools
   necessary to allow the PCMCIA subsystem to behave (almost) as every
   other hotpluggable bus system (e.g. USB, IEEE1394). Please note that
   the kernel support for this new feature is only present since
   2.6.13-rc1.
     ________________________________________________________________

14.3. Kernel Configuration for Laptops

   You may find an example for 2.4.x kernels
   [http://tuxmobil.org/kernel_config_laptop.html] here Please note:
   Don't use this file by default, please use always make config, make
   menuconfig or make xconfig to create a kernel configuration file. See
   [http://tldp.org/HOWTO/Kernel-HOWTO/] Kernel-HOWTO (from TLDP) for
   details. Thomas Hertweck has written another useful
   [http://www.thomashertweck.de/kernel.html] Linux-Kernel-HOWTO (but it
   is only available in German and Italian).

   [http://savannah.nongnu.org/projects/laptopkernel/] laptopkernel is a
   patchset for the Linux kernel containing several useful patches for
   laptop-users. It contains acpi, software suspend, supermount and some
   hardware compatibility patches. Unfortunately this project is not
   maintained anymore since 2003.

VII. On the Road

   Table of Contents
   15. Different Environments

        15.1. Related Documentation
        15.2. Configuration Tools
        15.3. E-Mail
        15.4. Data Transport Between Different Machines
                (Synchronization)

        15.5. Backup
        15.6. Connections to Servers
        15.7. Security in Different Environments
        15.8. Theft Protection
        15.9. Dealing with Down Times (Cron Jobs)
        15.10. Mobile Printing
        15.11. Noise Reduction

   16. Solutions with Mobile Computers

        16.1. Introduction
        16.2. Mobile Network Analyzer
        16.3. Mobile Router
        16.4. Hacking and Cracking Networks
        16.5. Mobile Data Collection
        16.6. Mobile Office
        16.7. Connection to Digital Camera
        16.8. Connection to QuickCam (Video)
        16.9. Connection to Television Set
        16.10. Connection to Cellular Phone
        16.11. Connection to Global Positioning System (GPS)
        16.12. Connection via Amateur Radio (HAM)
        16.13. Satellite Watching
        16.14. Aviation
        16.15. Blind or Visually Impaired Users
     ________________________________________________________________

Chapter 15. Different Environments



   Tell me and I might forget. Show me and I can remember. Involve me
   and I will understand.
     Confucius, 450 B.C.
     ________________________________________________________________

15.1. Related Documentation

    1. [http://tldp.org/HOWTO/Security-HOWTO/index.html] Security-HOWTO
    2. [http://tldp.org/HOWTO/Multiboot-with-LILO.html]
       Multiboot-with-LILO-HOWTO
    3. [http://tldp.org/HOWTO/Ethernet-HOWTO.html] Ethernet-HOWTO
    4. [http://tldp.org/HOWTO/NET3-4-HOWTO.html] Networking-HOWTO
    5. [http://tldp.org/HOWTO/Offline-Mailing.html]
       Offline-Mailing-mini-HOWTO
    6. [http://tldp.org/HOWTO/PLIP.html] Plip-HOWTO
    7. [http://tldp.org/HOWTO/SLIP-PPP-Emulator/]
       Slip-PPP-Emulator-HOWTO

   If you are using Debian GNU/Linux then you should refer to the Debian
   Reference chapter entitled "Network configuration". Debian contains a
   number of packages that help to make roaming among different networks
   effortless.
     ________________________________________________________________

15.2. Configuration Tools

15.2.1. NetEnv

   Do you use your laptop in different network environments? At home? In
   the office? At a customers site?

   If yes, the small package "netenv" might be useful for you. When
   booting your laptop it provides you with a simple interface from
   which you can choose the current network environment. The first time
   in a new environment, you can enter the basic data and save it for
   later reuse.

   Netenv sets up a file containing variable assignments which describe
   the current environment. This can be used by the PCMCIA setup scheme,
   e.g. like the one that comes with Debian/GNU Linux and perhaps
   others.

   The netenv data can be used for things like:

    1. Network Device: Configure the network device for different
       environments.
    2. Choose a proper XF86Config: Think of using your laptop standalone
       with touchpad vs. connected to a CRT monitor along with an
       external mouse. For example, a wheel mouse could be used when
       docked, but the driver is not compatible with the normal
       trackpoint or touchpad.
    3. Windowmanager: You can set up your windowmanager appropriate to
       the current location of your machine.
    4. Printing Environment: The netenv data can easily be used to set
       up the printing environment.

   Netenv is available at [http://netenv.sourceforge.net] netenv home.
   It depends on dialog(1) for its menu interface. Netenv was developed
   by Gerd Bavendiek.
     ________________________________________________________________

15.2.2. System Configuration Profile Management - SCPM

   SuSE's [http://forge.novell.com/modules/xfmod/project/?scpm] System
   Configuration Profile Management - SCPM software allows you to switch
   configuration profiles. You can boot directly into one profile and
   then switch to another profile at run time. This is the successor of
   SuSE's older "scheme" management software.
     ________________________________________________________________

15.2.3. ifplugd

   [http://0pointer.de/lennart/projects/ifplugd/] ifplugd is a
   lightweight Linux daemon which configures the network automatically
   when a cable is plugged in and deconfigures it when the cable is
   pulled. It is primarily intended for usage with laptops. It relies on
   the distribution's native network configuration subsystem, and is
   thus not very intrusive.
     ________________________________________________________________

15.2.4. divine

   [http://www.fefe.de/divine/] divine is an utility for people who use
   their machines in different networks all the time. "The idea is this:

     * you describe the possible networks in /etc/divine.conf, including
       one or more machines that are probably up (routers and NIS
       servers come to mind).
     * at boot time, you run divine.
     * divine starts a thread that injects fake arp requests into the
       network. The thread will try again up to three times, pausing 1
       second between retries. If the last try times out again, the
       thread will print an error message, leave the interface in the
       original state and exit cleanly.
     * the main thread just looks for arp replies and exits if one is
       found.
     * You have one resolv.conf per network, for example
       /etc/resolv.conf.default and /etc/resolv.conf.work. divine will
       symlink one of them to /etc/resolv.conf for you.
     * You can specify a proxy server plus port and divine will write
       the proxy server to /etc/proxy. This can be evaluated inside your
       shell startup script, like this (zsh):

export http_proxy="http://`</etc/proxy`/"

       The included perl script edit-netscape-proxy.pl will edit the
       proxy settings in your Netscape 4 preferences file.
     * You can even specify an additional script to be run for each
       selection. You can use this to edit /etc/printcap or /etc/issue
       or do something else I forgot.

   The point about divine in contrast to other solutions is that other
   solutions normally use ping or something like that. divine can check
   a large number of networks instantaneously, assuming that the
   machines you ping answer within one second (.4 seconds are normal on
   Ethernets). And pinging an unknown address will do an arp request
   anyway, so why not do an arp request in the first place?"
     ________________________________________________________________

15.2.5. Mobile IP

   From the [http://tldp.org/HOWTO/NET3-4-HOWTO.html] Networking-HOWTO :
   "The term IP Mobility describes the ability of a host that is able to
   move its network connection from one point on the Internet to another
   without changing its IP address or losing connectivity. Usually when
   an IP host changes its point of connectivity it must also change its
   IP address. IP Mobility overcomes this problem by allocating a fixed
   IP address to the mobile host and using IP encapsulation (tunneling)
   with automatic routing to ensure that datagrams destined for it are
   routed to the actual IP address it is currently using."

   [http://dynamics.sourceforge.net/] Dynamics Mobile IP is a dynamical,
   hierarchical Mobile IP system for Linux operating system. The
   implementation enables a hierarchical model for IP mobility, thus
   decreasing the location update times as a mobile host moves. Dynamics
   system has been designed Wireless LAN technology in mind, and the
   system has optimized functionality for mobility in WLAN.

   See also [http://tuxmobil.org/manet_linux.html] Linux and Mobile
   AdHoc Networks - MANETs.
     ________________________________________________________________

15.2.5.1. Resources

    1. [http://www.hpl.hp.com/personal/Jean_Tourrilhes/MobileIP/index.ht
       ml] Linux Mobile IP from HP Labs Bristol by Manuel Rodriguez.
    2. [http://mosquitonet.Stanford.EDU/software/mip.html] MosquitoNet
       Mobile IP
    3. [http://http.cs.berkeley.edu/~randy/Daedalus/BARWAN/] Bay Area
       Research Wireless Access Network - BARWAN

   Sources: Kenneth E. Harker and Dag Brattli
     ________________________________________________________________

15.2.6. DHCP/BootP

   DHCP and BootP are also useful for working in different environments.
   Please see the [http://tldp.org/HOWTO/DHCP/index.html] DHCP-HOWTO .
     ________________________________________________________________

15.2.7. PPPD Options

   The pppd command can be configured via several different files: pppd
   file /etc/ppp/<your_options> .
     ________________________________________________________________

15.2.8. /etc/init.d

   You may even choose to do your configuration by editing the
   /etc/init.d files manually.
     ________________________________________________________________

15.2.9. PCMCIA - Schemes

   How can I have separate PCMCIA device setups for home and work? This
   is fairly easy using PCMCIA scheme support. Use two configuration
   schemes, called home and work. For details please read the
   appropriate chapter in the PCMCIA-HOWTO.
     ________________________________________________________________

15.2.10. Bootloaders

15.2.10.1. LILO

   From Martin J. Evans I have taken this recommendation: The first
   point to note is that init will take any arguments of the form
   name=value as environment variable assignments if they are not
   recognized as something else. This means you can set environment
   variables from the LILO boot prompt before your rc scripts run. I set
   the LOCATION environment variable depending on where I am when I boot
   Linux. e.g.
LILO: linux LOCATION=home

   Or
LILO: linux LOCATION=work

   Or simply
LILO: linux

   where failing to set LOCATION means the same as LOCATION=home (i.e.
   my default). Instead of typing LOCATION=place each time you boot you
   can add an entry to your /etc/lilo.conf file and use the append
   instruction. e.g.
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

   With the example above you can use "linux" for booting at home and
   "work" for booting at work.

   Armed with the facility above, you can now edit the relevant rc
   scripts to test ENVIRONMENT before running ifconfig, setting up route
   etc.
     ________________________________________________________________

15.2.10.2. Other Bootloaders

   There are several other bootloaders which are often overlooked.
   Besides LILO, have a look at loadlin, CHooseOS (CHOS) (not GPL),
   GRand Unified Bootloader (GRUB), System Commander and take a look at
   [ftp://metalab.unc.edu/pub/Linux/system/boot/loaders/]
   ftp://metalab.unc.edu/pub/Linux/system/boot/loaders/ . The MicroSoft
   Windows-NT boot loader or OS/2 boot loader may even be used.
     ________________________________________________________________

15.2.11. X-Windows

   From Steve <steve_AT_cygnet.co.uk> I got a configuration for X
   Windows with an external monitor: Note that I have introduced a neat
   trick! For my nice 17" monitor I start X11 with no options and get
   the default 16-bit 1152x864 display - but when using the LCD screen I
   specify a 15-bit display (startx -- -bpp 15) and get the correct
   800x600 resolution automatically. This saves having to have two X11
   config files.
     ________________________________________________________________

15.2.12. More Info

   [http://www.ssc.com/lg/issue20/laptop.html] Using a Laptop in
   Different Environments by Gerd Bavendiek . This article appeared in
   the August, 1997 issue of the [http://www.ssc.com/lg/] Linux Gazette
   . This is an excellent, short technical article describing an easy
   way to setup your Linux notebook to boot into different network and
   printing configurations, especially useful for those who use their
   machines at home as well as other locations such as in the office, at
   school, or at a customer site.
     ________________________________________________________________

15.3. E-Mail

15.3.1. Introduction

   A short introduction about how to setup email on a laptop used at
   home (dial-up) and work (ethernet) by Peter Englmaier
   <ppe_AT_pa.uky.edu>:
     ________________________________________________________________

15.3.1.1. Features

   As a laptop user, I have special demands for my email setup. The
   setup described below, enables me to:

     * Read my email from home using a POP email server, which is
       supplied by my university, but could also be setup on a work
       place computer.
     * Write email from home with the right return address in the email
       (which does not mention my computer name).
     * Read/write my email while working on a workstation without access
       to my laptop or the POP email server (as a backup).
     * Read my email while working on my laptop connected to the
       ethernet of our institut.
     * Direct email while connected via ethernet (faster than the
       fetchmail method).
     * Indirect email (over pop mail server) while not connected to the
       ethernet at work (either at home via modem or somewhere else via
       ethernet).
     * Use any emailer, e.g. elm or the simple mail command.
     * Sort incoming email, delete spam, split email-collections
       (digests) into separate emails

   The configuration is based on sendmail, fetchmail, and a remote pop
   account for email.
     ________________________________________________________________

15.3.1.2. Configuration of sendmail

   This is the most complicated part. Having installed the sendmail-cf
   package, I created a file named /usr/lib/sendmail-cf/laptop.mc:

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

   This looks more complicated as it is. All it does is, that it
   redirectes outbound mail to server1 (SMART_HOST) and also mail for
   local users which are not known (LUSER_RELAY). That way, I can write
   email to my colleques without using their full email address. More
   important: the From line in my email points back to my MASQUARADE_AS
   domain and not directly to my laptop. If this where not the case,
   email returned with the reply button might not reach me. You must
   restart sendmail for changes to take effect. Note: this configuration
   is for Redhat 5.2 systems. You may have to change some details.

   Now, all what is needed is to generate the /etc/sendmail.cf file m4
   laptop.mc >/etc/sendmail.cf and to add all possible domain names my
   laptop should respond to in /etc/sendmail.cw:

# sendmail.cw - include all aliases for your machine here.
laptop
laptop.pa.uky.edu
128.17.18.30
guest1
guest1.somewhere.org

   It is important to have all aliases in this file, otherwise sendmail
   will not accept the mail (and will reply we don't relay to the
   sender). Finally, you must now test the setup by sending email,
   replying to mail for all possible configurations. Any
   misconfiguration can result in loss of email.
     ________________________________________________________________

15.3.1.3. Configuration for fetchmail on Laptop

   One method to get the email into your machine is through fetchmail.
   Fetchmail periodically checks for new email at one or more remote
   mail servers. I use the following fetchmail configuration file (in my
   user home directory): fetchmailrc

set postmaster "myusername"
set daemon 900
poll pop.uky.edu with proto POP3
user "mypopusername" there with password "mypoppassword" is mylaptopusername h
ere

   Fetchmail will just get the email and send it to sendmail which will
   it deliver into your /var/spool/mail/$USER file.
     ________________________________________________________________

15.3.1.4. Forward E-Mail to the Laptop

   On my work station I have the following .forward file:

me@pop.account.edu,me@server1

   Here server1 is the machine where I keep my mailbox. All email is
   send to the pop account to be picked up later by my laptop (using
   fetchmail). However, when my laptop is connected via ethernet, I want
   my email to go directly to the laptop, instead of pop:

me@laptop,me@server1

   In both cases, a backup of my email is send to server1 (where I also
   can read it, in case I cannot get my laptop). I keep/store all email
   on the laptop.

   Switching is done by three script files and a crontab file (on the
   workstation):

   forward_pop

#!/bin/sh
echo "me@pop.account.edu,me@server1" > ${HOME}/.forward

   forward_laptop

#!/bin/sh
echo "ppe@laptop,ppe@server1" > ${HOME}/.forward
crontab ${HOME}/mycrontab
${HOME}/utl/check_laptop

   check_laptop

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

   mycrontab

# mycrontab
0,10,20,30,40,50 * * * * ${HOME}/utl/check_laptop

   Each time I connect the laptop to the ethernet, I have to run
   forward_laptop, and each time I disconnect I run forward_pop. In case
   I forget to run forward_pop, the crontab job runs it for me less then
   10 minutes later. To do all that automatically, I change the network
   script files on my laptop as follows:

   /sbin/ifdown (this script runs, whenever a network device is stopped,
   new stuff between BEGIN and END)

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

   Note, that the script checks for the value of hostname. In case, I am
   connected to a foreign ethernet, my hostname and ip-address will be
   something else, e.g. guest1.

   /etc/sysconfig/network-scripts/ifup-post (this script is run,
   whenever a network device is started)

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
     ________________________________________________________________
