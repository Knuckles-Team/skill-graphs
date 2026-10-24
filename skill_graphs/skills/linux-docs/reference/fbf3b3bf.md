#  12.37. Infrared Port
| _Better red, than dead._
---|---
| _Unknown AuthorEss_
* * *
##  12.37.1. Linux Compatibility Check
To get the IrDA® port of your laptop working with Linux/IrDA® you may use StandardInfraRed (SIR) or FastInfraRed (FIR).
* * *
###  12.37.1.1. SIR
Up to 115.200bps, the infrared port emulates a serial port like the 16550A UART. This will be detected by the kernel serial driver at boot time, or when you load the `serial` module. If infrared support is enabled in the BIOS, for most laptops you will get a kernel message like:
```

Serial driver version 4.25 with no serial options enabled
ttyS00 at 0x03f8 (irq = 4) is a 16550A     #first serial port /dev/ttyS0
ttyS01 at 0x3000 (irq = 10) is a 16550A    #e.g. infrared port
ttyS02 at 0x0300 (irq = 3) is a 16550A     #e.g. PCMCIA modem port

```

---
* * *
###  12.37.1.2. FIR
If you want to use up to 4Mbps, your machine has to be equipped with a certain FIR chip. You need a certain Linux/IrDA® driver to support this chip. Therefore you need exact information about the FIR chip. You may get this information in one of the following ways:
  1. Read the _specification_ of the machine, though it is very rare that you will find enough and reliable information to use with Linux there.
  2. Try to find out whether the FIR chip is a _PCI_ device. Do a **cat /proc/pci** . The appropriate files for 2.2.x kernels are in `/proc/bus/pci` . Though often the PCI information is incomplete. You may find the latest information about PCI devices and vendor numbers in the kernel documentation usually in `/usr/src/linux/Documentation` or at the page of **lspci** from the **pci-utils** package, too.
  3. Use the _DOS tool_ **CTPCI330.EXE** provided in ZIP format by the
  4. Try to get information about _Plug-and-Play (PnP)_ devices. Though I didn't use them for this purpose yet, the **isapnp** tools, could be useful.
  5. If you have installed the _Linux/ IrDA® software_ load the FIR modules and watch the output of **dmesg** , whether FIR is detected or not.
  6. Another way how to figure it out explained by Thomas Davis (modified by WH): "Dig through the FTP site of the vendor, find the _Windows9x FIR drivers_ , and they have (for a SMC chip):
```

-rw-rw-r--   1 ratbert  ratbert       743 Apr  3  1997 smcirlap.inf
-rw-rw-r--   1 ratbert  ratbert     17021 Mar 24  1997 smcirlap.vxd
-rw-rw-r--   1 ratbert  ratbert      1903 Jul 18  1997 smcser.inf
-rw-rw-r--   1 ratbert  ratbert     31350 Jun  7  1997 smcser.vxd

```

---
If in doubt, always look for the .inf/.vxd drivers for Windows95. Windows95 doesn't ship with _ANY_ FIR drivers. (they are all third party, mostly from Counterpoint, who was assimilated by ESI)."
  7. Also Thomas Davis found a package of small DOS **FINDCHIP.EXE**. And includes a **FIRSETUP.EXE** utility that is supposed to be able to set all values except the chip address. Furthermore it contains **BIOSDUMP.EXE** , which produces this output:
Example 1 (from a COMPAQ Armada 1592DT)
```

In current devNode:
           Size      = 78
           Handle    = 14
           ID        = 0x1105D041 = 'PNP0511' -- Generic IrDA SIR
Types:  Base = 0x07, Sub = 0x00,  Interface = 0x02
Comm. Device, RS-232, 16550-compatible
Attribute = 0x80
                CAN be disabled
                CAN be configured
BOTH Static & Dynamic configuration
Allocated Resource Descriptor Block TAG's:
TAG=0x47, Length=7 I/O Tag, 16-bit Decode
Min=0x03E8, Max=0x03E8
Align=0x00, Range=0x08
TAG=0x22, Length=2 IRQ Tag, Mask=0x0010
TAG=0x79, Length=1 END Tag, Data=0x2F

```

---
Result 1:
**Irq Tag, Mask (bit mapped - ) = 0x0010 = 0000 0000 0000 0001 0000** so, it's IRQ 4. (start at 0, count up ..), so this is a SIR only device, at IRQ=4, IO=x03e8.
Example 2 (from an unknown machine)
```

In current devNode:
          Size      = 529
          Handle    = 14
          ID        = 0x10F0A34D = 'SMCF010' -- SMC IrCC
Types:  Base = 0x07, Sub = 0x00,  Interface = 0x02
Comm. Device, RS-232, 16550-compatible
Attribute = 0x80
               CAN be disabled
               CAN be configured
BOTH Static & Dynamic configuration

Allocated Resource Descriptor Block TAG's:
TAG=0x47, Length=7 I/O Tag, 16-bit Decode
Min=0x02F8, Max=0x02F8
Align=0x00, Range=0x08
TAG=0x22, Length=2 IRQ Tag, Mask=0x0008
TAG=0x47, Length=7 I/O Tag, 16-bit Decode
Min=0x02E8, Max=0x02E8
Align=0x00, Range=0x08
TAG=0x2A, Length=2 DMA Tag, Mask=0x02, Info=0x08
TAG=0x79, Length=1 END Tag, Data=0x00

```

---
Result 2:
a) it's a SMC IrCC chip
b) one portion is at 0x02f8, has an io-extent of 8 bytes; irq = 3
c) another portion is at 0x02e8, io-extent of 8 bytes; dma = 1 (0x02 =0000 0010)
![Warning](https://tldp.org/LDP/Mobile-Guide/images/warning.gif) |  The package is not intended for the end user, and some of the utilities could be harmful. The only documentation in the package is in Microsoft Word format. Linux users may read this with
---|---
  8. Use the _Device Manager_ of the MicroSoft Windows9x/NT operating system.
  9. You may also use the _hardware surveys_ mentioned below.
  10. And as a last resort, you may even _open the laptop_ and look at the writings at the chipsets themselves.


* * *
###  12.37.1.3. Hardware Survey
I have made an IrDA hardware survey at
To make this list more valuable, it is necessary to collect more information about the infrared devices in different hardware. You can help by sending me a short e-mail containing the exact name of the hardware you have and which type of infrared controller is used.
Please let me know also how well Linux/IrDA® worked (at which tty, port and interrupt it works and the corresponding infrared device, e.g. printer, cellular phone).
Also you can help by contributing detailed technological information about some infrared devices, which is necessary for the development of drivers for Linux.
* * *
##  12.37.2. Related Documentation
* * *
##  12.37.3. IrDA® Configuration - Survey
###  12.37.3.1. IrDA®
The Linux infrared support is still experimental, but rapidly improving. I try to describe the installation in a short survey. Please read my
* * *
####  12.37.3.1.1. Kernel
  1. Get a 2.4.x kernel and the latest Linux/IrDA patches from the
  2. Compile it with all IrDA® options enabled.
  3. Also enable experimental, sysctl, serial and network support.


* * *
####  12.37.3.1.2. Software
  1. Get the Linux IrDA® software **irda-utils** at
  2. Untar the package.
  3. Do a **make depend; make all; make install**


* * *
####  12.37.3.1.3. Hardware
  1. Enable the IrDA® support in the BIOS.
  2. Check for SIR or FIR support, as described above.
  3. Start the Linux/IrDA® service with **irattach DEVICE -s 1** .
  4. Watch the kernel output with **dmesg** .


* * *
###  12.37.3.2. Linux Infrared Remote Control - LIRC
* * *
