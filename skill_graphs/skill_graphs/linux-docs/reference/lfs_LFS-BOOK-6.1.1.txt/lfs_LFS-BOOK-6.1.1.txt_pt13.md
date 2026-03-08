   kernel documentation or the documentation for that driver to find the
   proper major/minor numbers.

   2) A non-hardware device is required. This is most common with the
   Advanced Linux Sound Architecture (ALSA) project's Open Sound System
   (OSS) compatibility module. These types of devices can be handled in
   one of two ways:
     * Adding the module names to /etc/sysconfig/modules
     * Using an "install" line in /etc/modprobe.conf. This tells the
       modprobe command "when loading this module, also load this other
       module, at the same time." For example:
install snd-pcm modprobe -i snd-pcm ; modprobe \
    snd-pcm-oss ; true
       This will cause the system to load both the snd-pcm and
       snd-pcm-oss modules when any request is made to load the driver
       snd-pcm.

7.4.5. Useful Reading

   Additional helpful documentation is available at the following sites:
     * A Userspace Implementation of devfs
       [487]http://www.kroah.com/linux/talks/ols_2003_udev_paper/Reprint-
       Kroah-Hartman-OLS2003.pdf
     * udev FAQ
       [488]http://www.kernel.org/pub/linux/utils/kernel/hotplug/udev-FAQ
     * The Linux Kernel Driver Model
       [489]http://public.planetmirror.com/pub/lca/2003/proceedings/paper
       s/Patrick_Mochel/Patrick_Mochel.pdf

7.5. Configuring the setclock Script

   The setclock script reads the time from the hardware clock, also known
   as the BIOS or the Complementary Metal Oxide Semiconductor (CMOS)
   clock. If the hardware clock is set to UTC, this script will convert
   the hardware clock's time to the local time using the /etc/localtime
   file (which tells the hwclock program which timezone the user is in).
   There is no way to detect whether or not the hardware clock is set to
   UTC, so this needs to be configured manually.

   If you cannot remember whether or not the hardware clock is set to
   UTC, find out by running the hwclock --localtime --show command. This
   will display what the current time is according to the hardware clock.
   If this time matches whatever your watch says, then the hardware clock
   is set to local time. If the output from hwclock is not local time,
   chances are it is set to UTC time. Verify this by adding or
   subtracting the proper amount of hours for the timezone to the time
   shown by hwclock. For example, if you are currently in the MST
   timezone, which is also known as GMT -0700, add seven hours to the
   local time.

   Change the value of the UTC variable below to a value of 0 (zero) if
   the hardware clock is not set to UTC time.

   Create a new file /etc/sysconfig/clock by running the following:
cat > /etc/sysconfig/clock << "EOF"
# Begin /etc/sysconfig/clock

UTC=1

# End /etc/sysconfig/clock
EOF

   A good hint explaining how to deal with time on LFS is available at
   [490]http://www.linuxfromscratch.org/hints/downloads/files/time.txt.
   It explains issues such as time zones, UTC, and the TZ environment
   variable.

7.6. Configuring the Linux Console

   This section discusses how to configure the console bootscript that
   sets up the keyboard map and the console font. If non-ASCII characters
   (e.g., the British pound sign and Euro character) will not be used and
   the keyboard is a U.S. one, skip this section. Without the
   configuration file, the console bootscript will do nothing.

   The console script reads the /etc/sysconfig/console file for
   configuration information. Decide which keymap and screen font will be
   used. Various language-specific HOWTO's can also help with this (see
   [491]http://www.tldp.org/HOWTO/HOWTO-INDEX/other-lang.html. A pre-made
   /etc/sysconfig/console file with known settings for several countries
   was installed with the LFS-Bootscripts package, so the relevant
   section can be uncommented if the country is supported. If still in
   doubt, look in the /usr/share/kbd directory for valid keymaps and
   screen fonts. Read loadkeys(1) and setfont(8) to determine the correct
   arguments for these programs. Once decided, create the configuration
   file with the following command:
cat >/etc/sysconfig/console <<"EOF"
KEYMAP="[arguments for loadkeys]"
FONT="[arguments for setfont]"
EOF

   For example, for Spanish users who also want to use the Euro character
   (accessible by pressing AltGr+E), the following settings are correct:
cat >/etc/sysconfig/console <<"EOF"
KEYMAP="es euro2"
FONT="lat9-16 -u iso01"
EOF

Note

   The FONT line above is correct only for the ISO 8859-15 character set.
   If using ISO 8859-1 and, therefore, a pound sign instead of Euro, the
   correct FONT line would be:
FONT="lat1-16"

   If the KEYMAP or FONT variable is not set, the console initscript will
   not run the corresponding program.

   In some keymaps, the Backspace and Delete keys send characters
   different from ones in the default keymap built into the kernel. This
   confuses some applications. For example, Emacs displays its help
   (instead of erasing the character before the cursor) when Backspace is
   pressed. To check if the keymap in use is affected (this works only
   for i386 keymaps):
zgrep '\W14\W' [/path/to/your/keymap]

   If the keycode 14 is Backspace instead of Delete, create the following
   keymap snippet to fix this issue:
mkdir -pv /etc/kbd && cat > /etc/kbd/bs-sends-del <<"EOF"
                  keycode  14 = Delete Delete Delete Delete
              alt keycode  14 = Meta_Delete
        altgr alt keycode  14 = Meta_Delete
                  keycode 111 = Remove
    altgr control keycode 111 = Boot
      control alt keycode 111 = Boot
altgr control alt keycode 111 = Boot
EOF

   Tell the console script to load this snippet after the main keymap:
cat >>/etc/sysconfig/console <<"EOF"
KEYMAP_CORRECTIONS="/etc/kbd/bs-sends-del"
EOF

   To compile the keymap directly into the kernel instead of setting it
   every time from the console bootscript, follow the instructions given
   in [492]Section 8.3, "Linux-2.6.11.12." Doing this ensures that the
   keyboard will always work as expected, even when booting into
   maintenance mode (by passing init=/bin/sh to the kernel), because the
   console bootscript will not be run in that situation. Additionally,
   the kernel will not set the screen font automatically. This should not
   pose many problems because ASCII characters will be handled correctly,
   and it is unlikely that a user would need to rely on non-ASCII
   characters while in maintenance mode.

   Since the kernel will set up the keymap, it is possible to omit the
   KEYMAP variable from the /etc/sysconfig/console configuration file. It
   can also be left in place, if desired, without consequence. Keeping it
   could be beneficial if running several different kernels where it is
   difficult to ensure that the keymap is compiled into every one of
   them.

7.7. Configuring the sysklogd script

   The sysklogd script invokes the syslogd program with the -m 0 option.
   This option turns off the periodic timestamp mark that syslogd writes
   to the log files every 20 minutes by default. If you want to turn on
   this periodic timestamp mark, edit the sysklogd script and make the
   changes accordingly. See man syslogd for more information.

7.8. Creating the /etc/inputrc File

   The inputrc file handles keyboard mapping for specific situations.
   This file is the startup file used by Readline -- the input-related
   library -- used by Bash and most other shells.

   Most people do not need user-specific keyboard mappings so the command
   below creates a global /etc/inputrc used by everyone who logs in. If
   you later decide you need to override the defaults on a per-user
   basis, you can create a .inputrc file in the user's home directory
   with the modified mappings.

   For more information on how to edit the inputrc file, see info bash
   under the Readline Init File section. info readline is also a good
   source of information.

   Below is a generic global inputrc along with comments to explain what
   the various options do. Note that comments cannot be on the same line
   as commands. Create the file using the following command:
cat > /etc/inputrc << "EOF"
# Begin /etc/inputrc
# Modified by Chris Lynn <roryo@roryo.dynup.net>

# Allow the command prompt to wrap to the next line
set horizontal-scroll-mode Off

# Enable 8bit input
set meta-flag On
set input-meta On

# Turns off 8th bit stripping
set convert-meta Off

# Keep the 8th bit for display
set output-meta On

# none, visible or audible
set bell-style none

# All of the following map the escape sequence of the
# value contained inside the 1st argument to the
# readline specific functions

"\eOd": backward-word
"\eOc": forward-word

# for linux console
"\e[1~": beginning-of-line
"\e[4~": end-of-line
"\e[5~": beginning-of-history
"\e[6~": end-of-history
"\e[3~": delete-char
"\e[2~": quoted-insert

# for xterm
"\eOH": beginning-of-line
"\eOF": end-of-line

# for Konsole
"\e[H": beginning-of-line
"\e[F": end-of-line

# End /etc/inputrc
EOF

7.9. The Bash Shell Startup Files

   The shell program /bin/bash (hereafter referred to as "the shell")
   uses a collection of startup files to help create an environment to
   run in. Each file has a specific use and may affect login and
   interactive environments differently. The files in the /etc directory
   provide global settings. If an equivalent file exists in the home
   directory, it may override the global settings.

   An interactive login shell is started after a successful login, using
   /bin/login, by reading the /etc/passwd file. An interactive non-login
   shell is started at the command-line (e.g., [prompt]$/bin/bash). A
   non-interactive shell is usually present when a shell script is
   running. It is non-interactive because it is processing a script and
   not waiting for user input between commands.

   For more information, see info bash under the Bash Startup Files and
   Interactive Shells section.

   The files /etc/profile and ~/.bash_profile are read when the shell is
   invoked as an interactive login shell.

   The base /etc/profile below sets some environment variables necessary
   for native language support. Setting them properly results in:
     * The output of programs translated into the native language
     * Correct classification of characters into letters, digits and
       other classes. This is necessary for bash to properly accept
       non-ASCII characters in command lines in non-English locales
     * The correct alphabetical sorting order for the country
     * Appropriate default paper size
     * Correct formatting of monetary, time, and date values

   This script also sets the INPUTRC environment variable that makes Bash
   and Readline use the /etc/inputrc file created earlier.

   Replace [ll] below with the two-letter code for the desired language
   (e.g., "en") and [CC] with the two-letter code for the appropriate
   country (e.g., "GB"). [charmap] should be replaced with the canonical
   charmap for your chosen locale.

   The list of all locales supported by Glibc can be obtained by running
   the following command:
locale -a

   Locales can have a number of synonyms, e.g. "ISO-8859-1" is also
   referred to as "iso8859-1" and "iso88591". Some applications cannot
   handle the various synonyms correctly, so it is safest to choose the
   canonical name for a particular locale. To determine the canonical
   name, run the following command, where [locale name] is the output
   given by locale -a for your preferred locale ("en_GB.iso88591" in our
   example).
LC_ALL=[locale name] locale charmap

   For the "en_GB.iso88591" locale, the above command will print:
ISO-8859-1

   This results in a final locale setting of "en_GB.ISO-8859-1". It is
   important that the locale found using the heuristic above is tested
   prior to it being added to the Bash startup files:
LC_ALL=[locale name] locale country
LC_ALL=[locale name] locale language
LC_ALL=[locale name] locale charmap
LC_ALL=[locale name] locale int_curr_symbol
LC_ALL=[locale name] locale int_prefix

   The above commands should print the country and language names, the
   character encoding used by the locale, the local currency and the
   prefix to dial before the telephone number in order to get into the
   country. If any of the commands above fail with a message similar to
   the one shown below, this means that your locale was either not
   installed in Chapter 6 or is not supported by the default installation
   of Glibc.
locale: Cannot set LC_* to default locale: No such file or directory

   If this happens, you should either install the desired locale using
   the localedef command, or consider choosing a different locale.
   Further instructions assume that there are no such error messages from
   Glibc.

   Some packages beyond LFS may also lack support for your chosen locale.
   One example is the X library (part of the X Window System), which
   outputs the following error message:
Warning: locale not supported by Xlib, locale set to C

   Sometimes it is possible to fix this by removing the charmap part of
   the locale specification, as long as that does not change the
   character map that Glibc associates with the locale (this can be
   checked by running the locale charmap command in both locales). For
   example, one would have to change "de_DE.ISO-8859-15@euro" to
   "de_DE@euro" in order to get this locale recognized by Xlib.

   Other packages can also function incorrectly (but may not necessarily
   display any error messages) if the locale name does not meet their
   expectations. In those cases, investigating how other Linux
   distributions support your locale might provide some useful
   information.

   Once the proper locale settings have been determined, create the
   /etc/profile file:
cat > /etc/profile << "EOF"
# Begin /etc/profile

export LANG=[ll]_[CC].[charmap]
export INPUTRC=/etc/inputrc

# End /etc/profile
EOF

Note

   The "C" (default) and "en_US" (the recommended one for United States
   English users) locales are different.

   Setting the keyboard layout, screen font, and locale-related
   environment variables are the only internationalization steps needed
   to support locales that use ordinary single-byte encodings and
   left-to-right writing direction. More complex cases (including UTF-8
   based locales) require additional steps and additional patches because
   many applications tend to not work properly under such conditions.
   These steps and patches are not included in the LFS book and such
   locales are not yet supported by LFS.

7.10. Configuring the localnet Script

   Part of the job of the localnet script is setting the system's
   hostname. This needs to be configured in the /etc/sysconfig/network
   file.

   Create the /etc/sysconfig/network file and enter a hostname by
   running:
echo "HOSTNAME=[lfs]" > /etc/sysconfig/network

   [lfs] needs to be replaced with the name given to the computer. Do not
   enter the Fully Qualified Domain Name (FQDN) here. That information
   will be put in the /etc/hosts file in the next section.

7.11. Creating the /etc/hosts File

   If a network card is to be configured, decide on the IP address, FQDN,
   and possible aliases for use in the /etc/hosts file. The syntax is:
            <IP address> myhost.example.org aliases

   Unless the computer is to be visible to the Internet (i.e., there is a
   registered domain and a valid block of assigned IP addresses--most
   users do not have this), make sure that the IP address is in the
   private network IP address range. Valid ranges are:
    Class Networks
        A     10.0.0.0
        B     172.16.0.0 through 172.31.0.255
        C     192.168.0.0 through 192.168.255.255

   A valid IP address could be 192.168.1.1. A valid FQDN for this IP
   could be www.linuxfromscratch.org (not recommended because this is a
   valid registered domain address and could cause domain name server
   issues).

   Even if not using a network card, an FQDN is still required. This is
   necessary for certain programs to operate correctly.

   Create the /etc/hosts file by running:
cat > /etc/hosts << "EOF"
# Begin /etc/hosts (network card version)

127.0.0.1 localhost
[192.168.1.1] [<HOSTNAME>.example.org] [HOSTNAME]

# End /etc/hosts (network card version)
EOF

   The [192.168.1.1] and [<HOSTNAME>.example.org] values need to be
   changed for specific users or requirements (if assigned an IP address
   by a network/system administrator and the machine will be connected to
   an existing network).

   If a network card is not going to be configured, create the /etc/hosts
   file by running:
cat > /etc/hosts << "EOF"
# Begin /etc/hosts (no network card version)

127.0.0.1 [<HOSTNAME>.example.org] [HOSTNAME] localhost

# End /etc/hosts (no network card version)
EOF

7.12. Configuring the network Script

   This section only applies if a network card is to be configured.

   If a network card will not be used, there is likely no need to create
   any configuration files relating to network cards. If that is the
   case, remove the network symlinks from all run-level directories
   (/etc/rc.d/rc*.d).

7.12.1. Creating Network Interface Configuration Files

   Which interfaces are brought up and down by the network script depends
   on the files and directories in the /etc/sysconfig/network-devices
   hierarchy. This directory should contain a sub-directory for each
   interface to be configured, such as ifconfig.xyz, where "xyz" is a
   network interface name. Inside this directory would be files defining
   the attributes to this interface, such as its IP address(es), subnet
   masks, and so forth.

   The following command creates a sample ipv4 file for the eth0 device:
cd /etc/sysconfig/network-devices &&
mkdir -v ifconfig.eth0 &&
cat > ifconfig.eth0/ipv4 << "EOF"
ONBOOT=yes
SERVICE=ipv4-static
IP=192.168.1.1
GATEWAY=192.168.1.2
PREFIX=24
BROADCAST=192.168.1.255
EOF

   The values of these variables must be changed in every file to match
   the proper setup. If the ONBOOT variable is set to "yes" the network
   script will bring up the Network Interface Card (NIC) during booting
   of the system. If set to anything but "yes" the NIC will be ignored by
   the network script and not be brought up.

   The SERVICE variable defines the method used for obtaining the IP
   address. The LFS-Bootscripts package has a modular IP assignment
   format, and creating additional files in the
   /etc/sysconfig/network-devices/services directory allows other IP
   assignment methods. This is commonly used for Dynamic Host
   Configuration Protocol (DHCP), which is addressed in the BLFS book.

   The GATEWAY variable should contain the default gateway IP address, if
   one is present. If not, then comment out the variable entirely.

   The PREFIX variable needs to contain the number of bits used in the
   subnet. Each octet in an IP address is 8 bits. If the subnet's netmask
   is 255.255.255.0, then it is using the first three octets (24 bits) to
   specify the network number. If the netmask is 255.255.255.240, it
   would be using the first 28 bits. Prefixes longer than 24 bits are
   commonly used by DSL and cable-based Internet Service Providers
   (ISPs). In this example (PREFIX=24), the netmask is 255.255.255.0.
   Adjust the PREFIX variable according to your specific subnet.

7.12.2. Creating the /etc/resolv.conf File

   If the system is going to be connected to the Internet, it will need
   some means of Domain Name Service (DNS) name resolution to resolve
   Internet domain names to IP addresses, and vice versa. This is best
   achieved by placing the IP address of the DNS server, available from
   the ISP or network administrator, into /etc/resolv.conf. Create the
   file by running the following:
cat > /etc/resolv.conf << "EOF"
# Begin /etc/resolv.conf

domain {[Your Domain Name]}
nameserver [IP address of your primary nameserver]
nameserver [IP address of your secondary nameserver]

# End /etc/resolv.conf
EOF

   Replace [IP address of the nameserver] with the IP address of the DNS
   most appropriate for the setup. There will often be more than one
   entry (requirements demand secondary servers for fallback capability).
   If you only need or want one DNS server, remove the second nameserver
   line from the file. The IP address may also be a router on the local
   network.

Chapter 8. Making the LFS System Bootable

8.1. Introduction

   It is time to make the LFS system bootable. This chapter discusses
   creating an fstab file, building a kernel for the new LFS system, and
   installing the GRUB boot loader so that the LFS system can be selected
   for booting at startup.

8.2. Creating the /etc/fstab File

   The /etc/fstab file is used by some programs to determine where file
   systems are to be mounted by default, in which order, and which must
   be checked (for integrity errors) prior to mounting. Create a new file
   systems table like this:
cat > /etc/fstab << "EOF"
# Begin /etc/fstab

# file system  mount-point  type   options         dump  fsck
#                                                        order

/dev/[xxx]     /            [fff]  defaults        1     1
/dev/[yyy]     swap         swap   pri=1           0     0
proc           /proc        proc   defaults        0     0
sysfs          /sys         sysfs  defaults        0     0
devpts         /dev/pts     devpts gid=4,mode=620  0     0
shm            /dev/shm     tmpfs  defaults        0     0
# End /etc/fstab
EOF

   Replace [xxx], [yyy], and [fff] with the values appropriate for the
   system, for example, hda2, hda5, and ext2. For details on the six
   fields in this file, see man 5 fstab.

   When using a journalling file system, the 1 1 at the end of the line
   should be replaced with 0 0 because such a partition does not need to
   be dumped or checked.

   The /dev/shm mount point for tmpfs is included to allow enabling
   POSIX-shared memory. The kernel must have the required support built
   into it for this to work (more about this is in the next section).
   Please note that very little software currently uses POSIX-shared
   memory. Therefore, consider the /dev/shm mount point optional. For
   more information, see Documentation/filesystems/tmpfs.txt in the
   kernel source tree.

   There are other lines which may be added to the /etc/fstab file. One
   example is a line for USB devices:
            usbfs        /proc/bus/usb usbfs   devgid=14,devmode=0660 0 0

   This option will only work if "Support for Host-side USB" and "USB
   device filesystem" are configured in the kernel. If "Support for
   Host-side USB" is compiled as a module, then usbcore must be listed in
   /etc/sysconfig/modules.

8.3. Linux-2.6.11.12

   The Linux package contains the Linux kernel.
   Approximate build time: 4.20 SBU
   Required disk space: 181 MB
   Installation depends on: Bash, Binutils, Coreutils, Findutils, GCC,
   Glibc, Grep, Gzip, Make, Modutils, Perl, and Sed

8.3.1. Installation of the kernel

   Building the kernel involves a few steps--configuration, compilation,
   and installation. Read the README file in the kernel source tree for
   alternative methods to the way this book configures the kernel.

   Prepare for compilation by running the following command:
make mrproper

   This ensures that the kernel tree is absolutely clean. The kernel team
   recommends that this command be issued prior to each kernel
   compilation. Do not rely on the source tree being clean after
   un-tarring.

   If, in [493]Section 7.6, "Configuring the Linux Console," it was
   decided to compile the keymap into the kernel, issue the command
   below:
loadkeys -m /usr/share/kbd/keymaps/[path to  keymap] > \
    drivers/char/defkeymap.c

   For example, if using a Dutch keyboard, use
   /usr/share/kbd/keymaps/i386/qwerty/nl.map.gz.

   Configure the kernel via a menu-driven interface. BLFS has some
   information regarding particular kernel configuration requirements of
   packages outside of LFS at
   [494]http://www.linuxfromscratch.org/blfs/view/svn/longindex.html#kern
   el-config-index:
make menuconfig

   Alternatively, make oldconfig may be more appropriate in some
   situations. See the README file for more information.

   If desired, skip kernel configuration by copying the kernel config
   file, .config, from the host system (assuming it is available) to the
   unpacked linux-2.6.11.12 directory. However, we do not recommend this
   option. It is often better to explore all the configuration menus and
   create the kernel configuration from scratch.

Note

   NPTL requires the kernel to be compiled with GCC-3.x or later, in this
   case 3.4.3. It is not recommended to compile the kernel with
   GCC-2.95.x, as this causes failures in the Glibc test suite. Normally,
   this wouldn't be mentioned as LFS doesn't build GCC-2.95.x.
   Unfortunately, the kernel documentation is outdated and still claims
   GCC-2.95.3 is the recommended compiler.

   Compile the kernel image and modules:
make

   If using kernel modules, an /etc/modprobe.conf file may be needed.
   Information pertaining to modules and kernel configuration is located
   in the kernel documentation in the linux-2.6.11.12/Documentation
   directory. Also, modprobe.conf(5) may be of interest.

   Be very careful when reading other documentation relating to kernel
   modules because it usually applies to 2.4.x kernels only. As far as we
   know, kernel configuration issues specific to Hotplug and Udev are not
