#  3.2. Prerequisites - BIOS, Boot Options, Partitioning
##  3.2.1. BIOS
When starting a fresh installation you should try with standard BIOS options. If something doesn't work you should try to modify BIOS options. For example a well known trouble maker is the Plug-and-Play - PnP option (which comes with different names). See also the BIOS section in the hardware section below.
* * *
##  3.2.2. Boot Options
There are many boot options, which have effects on the behavior of laptops, e.g. **apm=on|off** and **acpi=on|off** : For details see [BootPrompt-HOWTO](http://tldp.org/HOWTO/BootPrompt-HOWTO.html) and the Kernel documentation in `/usr/src/linux/Documentation/kernel-parameters.txt` .
* * *
##  3.2.3. Partitioning
Partitioning can be done in a very sophisticated way. Currently I have only some first thoughts. I assume that with laptops there are still some reasons (e.g. updating the firmware of PCMCIA cards and BIOS) to share Linux and Windows9x/NT. Depending on your needs and the features of your laptop you could create the following partitions:
  * BIOS, some current BIOSes use a separate partition, for instance COMPAQ notebooks
  * suspend to disk, some laptops support this feature
  * swap space Linux
  * swap space Windows9x/NT
  * Linux base
  * Linux `/home` for personal data (please consider an encrypted partition for security reasons, for details about encryption see the according chapter below)
  * common data between Linux and Windows9x/NT
  * small (~32MB) boot partition for yaBoot (Linux/PPC boot loader), in HFS _MacOS Standard_ format.


Note this chapter isn't exhausting yet. Please read the appropriate HOWTOs first, e.g. the [Partition-HOWTO](http://tldp.org/HOWTO/Partition/) .
* * *
