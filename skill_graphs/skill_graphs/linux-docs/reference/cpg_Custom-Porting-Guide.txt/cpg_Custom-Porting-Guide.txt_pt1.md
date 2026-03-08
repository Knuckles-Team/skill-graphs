```
Custom Linux: A Porting Guide

Porting LinuxPPC to a Custom SBC

Shie Erlich


<shie@myrealbox.com>
����������

Rafi Yanai - my partner in the porting process

Avi Rubenbach - without whom this wouldn't be possible
Revision History
Revision 2.1           2003-03-08            Revised by: gjf
Modified code example per author
Revision 2.0           2002-06-13            Revised by: tab
Added GFDL per author
Revision 1.0           2002-05-13            Revised by: SE
Initial release
-----------------------------------------------------------------------------

Table of Contents
1. Introduction
    1.1. Who needs to read this ?
    1.2. What do I need to know (why so much) ?
    1.3. The tools
    1.4. The hardware
    1.5. Copyright & License


2. Bootcamp: How To Begin ?
    2.1. Creating a development environment
    2.2. Compiling the first kernel
    2.3. Booting the machine


3. Booting In The Dark
    3.1. Debugging with print_str()
    3.2. Modifying code using compiler flags
    3.3. Getting the console to work


4. Linux Still Isn't Booting
    4.1. Memory probing, RTC and decrementors
    4.2. Big-little endian (we should have known)
    4.3. Ethernet: our first PCI device
    4.4. Some Miscellaneous Issues


5. Linux Is Booting ... What Now ?
    5.1. The 64 bit barrier
    5.2. Booting from flash


A. GNU Free Documentation License
    A.1. PREAMBLE
    A.2. APPLICABILITY AND DEFINITIONS
    A.3. VERBATIM COPYING
    A.4. COPYING IN QUANTITY
    A.5. MODIFICATIONS
    A.6. COMBINING DOCUMENTS
    A.7. COLLECTIONS OF DOCUMENTS
    A.8. AGGREGATION WITH INDEPENDENT WORKS
    A.9. TRANSLATION
    A.10. TERMINATION
    A.11. FUTURE REVISIONS OF THIS LICENSE
    A.12. How to use this License for your documents


B. Trademarks

-----------------------------------------------------------------------------
Chapter 1. Introduction

1.1. Who needs to read this ?

This guide describes a work in progress, to port Linux to a custom
PowerPC-based board. This means making the operating system work on
unfamiliar hardware. Anyone who is on the same track might benefit from
reading this paper, as it highlights the pitfalls and problematic points
along the way.
-----------------------------------------------------------------------------

1.2. What do I need to know (why so much) ?

Before attempting to port Linux, know at least the following: (whenever
possible, a link to a proper information source is attached)

��*�Hardware: know what hardware you've got, how it works (if it works), and
    how is it initialized. Get all the hardware manuals you can - you'll
    probably need them. Also, never assume the hardware works the way it
    supposed to ! Hardware people do the darnest things :-(

��*�Basic understanding of drivers and how they work in Linux. Programming
    knowledge of simple drivers is an advantage - but not a must. [http://
    www.tldp.org/HOWTO/Module-HOWTO/index.html] http://www.tldp.org/HOWTO/
    Module-HOWTO/index.html

��*�How to work with Vision-ICE, how configure it and use it to load a binary
    kernel into the target RAM. Also, at the beginning, you'll need to know
    how to use ICE to debug in assembly.

��*�How to compile and configure a Linux kernel. [http://www.tldp.org/HOWTO/
    Kernel-HOWTO.html] http://www.tldp.org/HOWTO/Kernel-HOWTO.html

��*�The Linux boot process. [http://www.tldp.org/HOWTO/BootPrompt-HOWTO.html]
    http://www.tldp.org/HOWTO/BootPrompt-HOWTO.html

��*�Working knowledge of C programming is a must. Some assembly is sure to
    help. Also, it is best to get to know Makefiles. They tend to raise their
    ugly head once in a while.

��*�The Internet is your friend. All the information you need is probably on
    the net. You just have to know how to find it. Google is a good way to
    start; mailing lists and news groups usually keep the real gold.

��*�How to install Linux, configure it, administrate it and basically take
    care of everything it needs. This guide does not cover anything regarding
    system administration, setting up a server etc.


-----------------------------------------------------------------------------
1.3. The tools

This section describes the tools we used during the process. Most are trivial
to install and use. When necessary, consult the appropriate url or manual.

��*�HardHat Linux: First and foremost, HHLinux, now known as MontaVista
    Linux, is the distribution we started with. The distribution contains
    LSPs (same as BSPs) for PowerPC in a number of board configurations. For
    porting to our board, we took the LSP which is closest in hardware to our
    Artysyn PMPPC board, and started from there.

��*�LXR: This is THE killer tool, which allowed us to port Linux in a very
    short time. LXR is a cross referencer, which means it reads a piece of
    code (the Linux kernel, for example), and then allows browsing the code,
    searching through it and much more. I cannot emphasize enough how
    important this tool is. To see what the end result looks like, look at
    [http://lxr.linux.no/source] http://lxr.linux.no/source. LXR itself can
    be downloaded at [http://lxr.sf.net] http://lxr.sf.net

��*�VisionICE: A hardware debugger, which has the ability to stop, run and
    add breakpoint straight in the CPU. VisionIce is very usuful when no
    operating system is running, and allows to step in the kernel during boot
    process. The application can also be used to take a binary image of a
    kernel, load it into the target's RAM memory and run it - useful when
    you've got no boot loader.

��*�CVS: A version control system, allows you to keep multiple versions of
    the code. Other than backing up the code, it allows diffing between
    different version, and reverting to older version, when needed.

��*�A terminal program, like HyperTerminal or ProCOMM for Windows??, or
    minicom for Linux.


-----------------------------------------------------------------------------
1.4. The hardware

The board is based on PPC750 (PowerPC) processor. It is 6U VME64 standard.
The board is designed to host two PCI Mezzanine cards (CCPMC) - Mezzanine
cards that comply with Std CCPMC1386 can be attached.

��*�COP connector.

��*�1 MB of L2 cache.

��*�CPC700 system controller.

��*�128 MB SDRAM with ECC.

��*�Flash memory, divided to boot flash and user flash.

��*�NVRAM memory.

��*�I/O discretes.

��*�RS232 channels.

��*�General purpose registers.

��*�PCI 2.1 local bus.

��*�10/100 BaseT ethernet channel.

��*�VME64 system bus.


-----------------------------------------------------------------------------
1.5. Copyright & License

Copyright (c) 2002 Shie Elrich

Permission is granted to copy, distribute and/or modify this document under
the terms of the GNU Free Documentation License, Version 1.1 or any later
version published by the Free Software Foundation; with no Invariant
Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the
license is included in Appendix A.
-----------------------------------------------------------------------------

Chapter 2. Bootcamp: How To Begin ?

2.1. Creating a development environment

The minimum requirements are obviously a development station and a target.
However, the recommended way of working is having a third host which acts as
a server. The server runs several services such as ftp, telnet, NFS, tftp (if
needed) and CVS. The main role of the server is to run CVS and track version
control, however once you can boot the target from network, the server will
also hold the target images, and filesystem, which makes development much
easier.

Regardless, the first step is to install a tool-chain (compiler, linker etc.)
for your target. The HardHat Linux cdrom includes all the needed files, and
the installation sequence is documented in the HardHat Linux documentation.
During the installation, you must select your LSP (basic software for the
selected board), and HardHat will install a set of tools and a kernel source
tree matching your LSP.

We had a board that had vxWorks running on it, so we setup the target to boot
using the standard vxWorks loader. Once the loader initiated, we used
visionICE to take-over the target (so that vxWorks won't load an image file)
and load a Linux image into the target. What you need to do at this point is
get an ICE, connect it to the network and to the target - through a JTAG
connection - and install the ICE software on your host.

What should have been done so far:

��*�A Linux host installed, and the HardHat tool-chain.

��*�A working target (hardware should be functional)

��*�ICE is connected to the target and the network and its software usable.

��*�Optionally, a server running CVS, telnetd, NFS and FTP.


-----------------------------------------------------------------------------
2.2. Compiling the first kernel

If you've installed the Linux kernel that comes with HardHat, then
cross-compiling should already be enabled in the kernel Makefile. If your
kernel is not from the HardHat CD, you should enable cross-compiling in the
Makefile by defining a CROSS_COMPILE entry in the following manner: (a code
segment from the main Makefile)
CROSS_COMPILE   = /opt/hardhat/devkit/ppc/7xx/bin/ppc_7xx-
AS              = $(CROSS_COMPILE)as
LD              = $(CROSS_COMPILE)ld
CC              = $(CROSS_COMPILE)gcc

The Linux kernel is modular, and allows you to configure it and choose which
"blocks" should be compiled with the kernel. In order to do this, first cd /
usr/src/linux (assuming your kernel source code is installed at /usr/src/
linux). Once there, type make xconfig.After saving your options, you should
make vmlinux to create a kernel image suitably for using with VisionICE.

We will not go into more details here, as it's outside the scope of this
document. For more information, try [http://www.tldp.org/HOWTO/
Kernel-HOWTO.html] http://www.tldp.org/HOWTO/Kernel-HOWTO.html
-----------------------------------------------------------------------------

2.3. Booting the machine

First, configure the terminal program, in our case minicom, the following
way: 9600 bps, 8 bits, no parity, 1 stop bit and no flow control of any kind.
The serial port in Linux should be /dev/ttyS0 for COM1, /dev/ttyS1 for COM2
etc.

Start the target. You should see the vxWorks bootloader on your terminal
screen, and should be able to stop the boot sequence by pressing the space
bar.

Note We cannot use the vxWorks bootloader to load a Linux kernel since it
     looks in the ELF header and loads the image to the address written
     there. However, the Linux kernel, which uses virtual memory, is linked
     to a high-memory address, and vxWorks can't handle that.

Once the target is stopped, run the VisionICE software and perform the
following steps:

��*�Initialize the target by pressing Target|Initialize

��*�Press File|Load Executable. A dialog box will open, asking you to choose
    a file. Please choose your kernel image (vmlinux). Before pressing Load,
    don't forget to enter a value in the +/- Bias field.

    Tip The bias field makes it possible to tell ICE to load a certain image
        in a different address than what's stated in the ELF binary. We
        wanted to load the kernel into address 0x300000, and since the binary
        was linked to 0xC0000000, we entered -0xBFD00000.

��*�Once the image is loaded successfully, you can press Run or Step to start
    executing your kernel.


After pressing the Run button, nothing happened. At that moment, and for some
time after, it seemed that nothing was happening and the kernel was stuck. We
used ICE to step through the initialization code of the kernel and rule out
some potential problems, like virtual memory errors, only to finally discover
that the problem was simple: the kernel was indeed booting but since the
console (tty) driver had problems, we couldn't see anything!

Caution VisionICE is not the correct tool to use when debugging Linux. ICE
        doesn't know about virtual memory and protected mode (at least the
        version we had), and since the Linux kernel turns on virtual memory
        very early, ICE is only useful for debugging the first assembler
        statements. After VM is turned on, ICE starts crashing and giving
        weird results.
-----------------------------------------------------------------------------

Chapter 3. Booting In The Dark

3.1. Debugging with print_str()

As stated in the previous chapter, the machine starts to boot, but nothing
happens. At least, nothing that we can see. The screen is blank and no kernel
messages appear. At this point, you have to ask yourself, is it really
booting?

Since the console wouldn't start, and ICE died real fast, we had no choice.
We had to debug somehow, and the oldest way is good here - printing to the
screen. Obviously, we couldn't use printk(), so we wrote a short function
which pushes characters straight into the serial port. We used the boot
process "map" shown in the previous section, and inserted some prints along
the way. This helped us to know at what stage we are completing and where
we're dying. The following piece of code prints a single character to the
serial port, by polling it and waiting for it to be free.
                                 /* tx holding reg empty or tx    */
#define LSR_THREMPTY 0x20        /* fifo is empty (in fifo mode ) */
#define THR_REG      0x00        /* Transmit holding reg */
#define LSR_REG      0x05        /* Line status reg */
#define COM1_ADDRESS 0xFF600300  /* == replace with your UART address */

void print_char (char ch) {
        volatile  unsigned char status = 0;
        /* wait until txempty */
        while ((status & LSR_THREMPTY ) == 0)
                status = *((volatile unsigned char *)(COM1_ADDRESS + LSR_REG));

        *((volatile unsigned char *)(COM1_ADDRESS + THR_REG)) = ch;
}

Note There's a better code for printing directly to the serial port, however,
     it's a bit more complicated. You can find it in arch/ppc/boot/common/
     misc-common.c, using puts() or putc().
-----------------------------------------------------------------------------

3.2. Modifying code using compiler flags

Although it is not a porting issue, the way you modify your code matters.
It's easier if you do it right the first time. The Linux kernel uses standard
configuration flags CONFIG_XXXX (like CONFIG_PPC, CONFIG_ISA etc), which are
used to mark a certain machine, architecture or device. We defined ourselves
a new flag (let's call it CONFIG_TESTMACH), and surrounded our new/modified
code with these flags:
....original code....
#ifdef CONFIG_TESTMACH
....modified code....
#else
....original code....
#endif /* CONFIG_TESTMACH */
To "activate" our code, we added the new flag to the kernel configuration
file - .config - by adding CONFIG_TESTMACH=y to it. In the first stage, this
solution allows you a quick way to find the code you changed, but later the
flag you chose will allow you to add your code into the kernel tree and into
the configuration program (make xconfig).
-----------------------------------------------------------------------------

3.3. Getting the console to work

3.3.1. Forcing the kernel to boot our-way

Once we discovered the kernel was indeed booting, but the console wasn't
printing, it was time to begin. First, we forced the kernel to boot using a
specified configuration for the serial port, in our case 9600n1, and did not
allow any command line options or boot time considerations etc.

The first place to go is drivers/char/tty_io.c, to console_init(). This
function determines the console configuration at startup. Here's a small part
of it:
memset(, 0, sizeof(struct termios));
memcpy(tty_std_termios.c_cc, INIT_C_CC, NCCS);
tty_std_termios.c_iflag = ICRNL | IGNPAR;
tty_std_termios.c_oflag = OPOST | ONLCR;
tty_std_termios.c_cflag = CLOCAL | B9600 | CS8 | CREAD;
tty_std_termios.c_cflag &= ~(CRTSCTS);
tty_std_termios.c_lflag = ISIG | ICANON | ECHO | ECHOE | ECHOK | ECHOCTL | ECHOKE | IEXTEN;
tty_std_termios.c_iflag = ICRNL | IXON;
tty_std_termios.c_oflag = OPOST | ONLCR;
tty_std_termios.c_cflag = B38400 | CS8 | CREAD | HUPCL;
tty_std_termios.c_lflag = ISIG | ICANON | ECHO | ECHOE | ECHOK | ECHOCTL | ECHOKE | IEXTEN;
The first (naive) thing we tried, was to configure the console the way we
wanted. Of course, this didn't help us much ;-)

Disappointed but not discouraged, we remembered that we didn't have a
bootloader yet, and that we didn't really know if any option was being passed
on to the kernel. "Maybe the kernel gets some garbage for command line?" we
(again, naively) thought. So we tried to stop the kernel from parsing
command-line options, and manually inserted our command line. This didn't
help us much ;-)
-----------------------------------------------------------------------------

3.3.2. Non-standard hardware - just say no!

At that point, we didn't have a console, but we had time. So we dove a bit
deeper into the console issues. Looking at drivers/char/serial.c, we came
across serial_console_setup(). This function, apart from parsing command-line
options, also configures the serial port by writing directly to it. Our
hardware people decided it was a good time to let us know that our serial
port wasn't standard. The lines that are used for flow control were not
connected. We decided to remark-out the following line, which sets the RTS
and DTR lines high, because we just didn't have them.
serial_out(info, UART_MCR, UART_MCR_DTR | UART_MCR_RTS);
Ofcourse, this didn't help us much :-( The lesson learned here was check,
check, check your hardware!. Custom boards might not be standard, and the
porting will go a lot quicker if you know about it.
-----------------------------------------------------------------------------

3.3.3. Let there be light: calculating baud rate

Finally, we decided to check the baudrate. Did Linux mean what we thought it
meant when it said 9600? Possibly not, since we didn't know how it computed
that value. We've noticed that the file(s) include/asm-ppc/pmppc_serial.h
(replace pmppc with your board name) included a definition of BAUDBASE, which
is later used for everything regarding serial ports. It was computed using
the board's local bus frequency, bus clock to system clock ratio etc. This
seemed wrong, so we checked out what the base baud was in a vxWorks system we
had running on the board, and changed it to:
/*
 * system clock = 33Mhz, serial clock = system clock / 4
 * the following must hold: (divisor * BaudRate) == (System clock / 64)
 */
#define BASE_BAUD (33000000 / 4 / 16)
A quick compilation, and a reboot later we had a booting kernel visible
through our serial port. Success!
-----------------------------------------------------------------------------

Chapter 4. Linux Still Isn't Booting

4.1. Memory probing, RTC and decrementors

Now that the console was working, we could see the real problems. The system
wasn't booting yet. Since we were working with C code, we traced the code,
and found that a function called sdram_size() wasn't completing correctly.
The function probed a register for the size of the RAM, a register our board
doesn't have. We made the function return a given value of 128MB, it's an
ugly hack, but our board doesn't have a way of knowing the amount of RAM.

Wwe had the same problems with a bunch of functions called todc_XXXX, mainly
todc_get_rtc_time(), todc_set_rtc_time(), and time_init() since we don't have
a RTC (real-time clock) chip on our board, and those functions were using it.
For the time being, we made the todc_XXX function only set and get a constant
date and time, since our board doesn't have a bios battery and so cannot keep
time when powered off.

Once all this was done, we found todc_calibrate_descr(), which again uses the
RTC chip. We had to replace that function with our own:
void calibrate_decr() {
        int freq, divisor;
        freq = bus_freq();
        divisor = 4;
        tb_ticks_per_jiffy = freq / HZ / divisor;
        tb_to_us = mulhwu_scale_factor(freq / divisor, 1000000);
}
-----------------------------------------------------------------------------

4.2. Big-little endian (we should have known)

4.2.1. Probing the CPC700

Finally, we reached the PCI-probing part of the boot process, only to
discover that it didn't work. We tried communicating with the CPC700 using
cpc700_read_local_pci_cfgb(), which was supplied along with the PMPPC's LSP,
and tried to read CPC's config register. We should have gotten 0x1014, which
is the vendor ID, but we didn't. We realized that we were talking
little-endian and the CPC was listening in big-endian. We made a small patch
to the functions, so that we spoke big-endian to the CPC700. We could then
read the vendor ID correctly, but the rest of it still didn't work. We didn't
want to alter the code so that everything would be done big-endian style.
-----------------------------------------------------------------------------

4.2.2. Making CPC700 speak little-endian

We discovered that the CPC700 can be initialized to do automatic
byte-swapping, which does little-to-big endian conversion on the fly. As it
seems, our board was initialized to do just that. We added a small code
segment in setup_arch(), which checks if byte-swapping is enabled, and if so,
disables it:
while (cnt<2) {
        cpc700_read_local_pci_cfgb(0, );
        cpc700_read_local_pci_cfgb(1, );
        if (l == 0 && h == 0) {
                if (cnt == 0) {
                        printk("CPC700 byte swapping enabled - trying to disable ... ");
                        cpc700_write_pifcfg_be(0x18, 0); /* disable byte-swapping */
                } else {
                        printk("FAILED !!\n");
                        break;
                }
        } else {cd
                printk("byte swapping disabled.\n");
                break;
        }
        ++cnt;
}
