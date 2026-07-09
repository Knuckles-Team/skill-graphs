# End /etc/fstab`
EOF`
```

Replace _`[xxx]`_ , _`[yyy]`_ , and _`[fff]`_ with the values appropriate for the system, for example, `hda2`, `hda5`, and `ext2`. For details on the six fields in this file, see **man 5 fstab**.
When using a journalling file system, the _`1 1`_ at the end of the line should be replaced with _`0 0`_ because such a partition does not need to be dumped or checked.
The `/dev/shm` mount point for `tmpfs` is included to allow enabling POSIX-shared memory. The kernel must have the required support built into it for this to work (more about this is in the next section). Please note that very little software currently uses POSIX-shared memory. Therefore, consider the `/dev/shm` mount point optional. For more information, see `Documentation/filesystems/tmpfs.txt` in the kernel source tree.
There are other lines which may be added to the `/etc/fstab` file. One example is a line for USB devices:
```
            usbfs        /proc/bus/usb usbfs   devgid=14,devmode=0660 0 0
```

This option will only work if “Support for Host-side USB” and “USB device filesystem” are configured in the kernel. If “Support for Host-side USB” is compiled as a module, then `usbcore` must be listed in `/etc/sysconfig/modules`.
##  8.3. Linux-2.6.11.12
The Linux package contains the Linux kernel.
**Approximate build time:** 4.20 SBU
**Required disk space:** 181 MB
**Installation depends on:** Bash, Binutils, Coreutils, Findutils, GCC, Glibc, Grep, Gzip, Make, Modutils, Perl, and Sed
###  8.3.1. Installation of the kernel
Building the kernel involves a few steps—configuration, compilation, and installation. Read the `README` file in the kernel source tree for alternative methods to the way this book configures the kernel.
Prepare for compilation by running the following command:
```
`make mrproper`
```

This ensures that the kernel tree is absolutely clean. The kernel team recommends that this command be issued prior to each kernel compilation. Do not rely on the source tree being clean after un-tarring.
If, in [Section 7.6, “Configuring the Linux Console,”](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#ch-scripts-console "7.6. Configuring the Linux Console") it was decided to compile the keymap into the kernel, issue the command below:
```
`loadkeys -m /usr/share/kbd/keymaps/_`[path to  keymap]`_ > \
    drivers/char/defkeymap.c`
```

For example, if using a Dutch keyboard, use `/usr/share/kbd/keymaps/i386/qwerty/nl.map.gz`.
Configure the kernel via a menu-driven interface. BLFS has some information regarding particular kernel configuration requirements of packages outside of LFS at
```
`make menuconfig`
```

Alternatively, **make oldconfig** may be more appropriate in some situations. See the `README` file for more information.
If desired, skip kernel configuration by copying the kernel config file, `.config`, from the host system (assuming it is available) to the unpacked `linux-2.6.11.12` directory. However, we do not recommend this option. It is often better to explore all the configuration menus and create the kernel configuration from scratch.
###  Note
NPTL requires the kernel to be compiled with GCC-3.x or later, in this case 3.4.3. It is not recommended to compile the kernel with GCC-2.95.x, as this causes failures in the Glibc test suite. Normally, this wouldn't be mentioned as LFS doesn't build GCC-2.95.x. Unfortunately, the kernel documentation is outdated and still claims GCC-2.95.3 is the recommended compiler.
Compile the kernel image and modules:
```
`make`
```

If using kernel modules, an `/etc/modprobe.conf` file may be needed. Information pertaining to modules and kernel configuration is located in the kernel documentation in the `linux-2.6.11.12/Documentation` directory. Also, `modprobe.conf(5)` may be of interest.
Be very careful when reading other documentation relating to kernel modules because it usually applies to 2.4.x kernels only. As far as we know, kernel configuration issues specific to Hotplug and Udev are not documented. The problem is that Udev will create a device node only if Hotplug or a user-written script inserts the corresponding module into the kernel, and not all modules are detectable by Hotplug. Note that statements like the one below in the `/etc/modprobe.conf` file do not work with Udev:
```
alias char-major-XXX some-module
```

Because of the complications with Hotplug, Udev, and modules, we strongly recommend starting with a completely non-modular kernel configuration, especially if this is the first time using Udev.
Install the modules, if the kernel configuration uses them:
```
`make modules_install`
```

After kernel compilation is complete, additional steps are required to complete the installation. Some files need to be copied to the `/boot` directory.
The path to the kernel image may vary depending on the platform being used. The following command assumes an x86 architecture:
```
`cp -v arch/i386/boot/bzImage /boot/lfskernel-2.6.11.12`
```

`System.map` is a symbol file for the kernel. It maps the function entry points of every function in the kernel API, as well as the addresses of the kernel data structures for the running kernel. Issue the following command to install the map file:
```
`cp -v System.map /boot/System.map-2.6.11.12`
```

The kernel configuration file `.config` produced by the **make menuconfig** step above contains all the configuration selections for the kernel that was just compiled. It is a good idea to keep this file for future reference:
```
`cp -v .config /boot/config-2.6.11.12`
```

It is important to note that the files in the kernel source directory are not owned by _root_. Whenever a package is unpacked as user _root_ (like we did inside chroot), the files have the user and group IDs of whatever they were on the packager's computer. This is usually not a problem for any other package to be installed because the source tree is removed after the installation. However, the Linux source tree is often retained for a long time. Because of this, there is a chance that whatever user ID the packager used will be assigned to somebody on the machine. That person would then have write access to the kernel source.
If the kernel source tree is going to be retained, run **chown -R 0:0** on the `linux-2.6.11.12` directory to ensure all files are owned by user _root_.
###  Warning
Some kernel documentation recommends creating a symlink from `/usr/src/linux` pointing to the kernel source directory. This is specific to kernels prior to the 2.6 series and _must not_ be created on an LFS system as it can cause problems for packages you may wish to build once your base LFS system is complete.
Also, the headers in the system's `include` directory should _always_ be the ones against which Glibc was compiled, that is, the ones from the Linux-Libc-Headers package, and therefore, should _never_ be replaced by the kernel headers.
###  8.3.2. Contents of Linux
**Installed files:** config-2.6.11.12, lfskernel-2.6.11.12, and System.map-2.6.11.12
###  Short Descriptions
`config-2.6.11.12` |  Contains all the configuration selections for the kernel
---|---
`lfskernel-2.6.11.12` |  The engine of the Linux system. When turning on the computer, the kernel is the first part of the operating system that gets loaded. It detects and initializes all components of the computer's hardware, then makes these components available as a tree of files to the software and turns a single CPU into a multitasking machine capable of running scores of programs seemingly at the same time
`System.map-2.6.11.12` |  A list of addresses and symbols; it maps the entry points and addresses of all the functions and data structures in the kernel
##  8.4. Making the LFS System Bootable
Your shiny new LFS system is almost complete. One of the last things to do is to ensure that the system can be properly booted. The instructions below apply only to computers of IA-32 architecture, meaning mainstream PCs. Information on “boot loading” for other architectures should be available in the usual resource-specific locations for those architectures.
Boot loading can be a complex area, so a few cautionary words are in order. Be familiar with the current boot loader and any other operating systems present on the hard drive(s) that need to be bootable. Make sure that an emergency boot disk is ready to “rescue” the computer if the computer becomes unusable (un-bootable).
Earlier, we compiled and installed the GRUB boot loader software in preparation for this step. The procedure involves writing some special GRUB files to specific locations on the hard drive. We highly recommend creating a GRUB boot floppy diskette as a backup. Insert a blank floppy diskette and run the following commands:
```
`dd if=/boot/grub/stage1 of=/dev/fd0 bs=512 count=1
dd if=/boot/grub/stage2 of=/dev/fd0 bs=512 seek=1`
```

Remove the diskette and store it somewhere safe. Now, run the **grub** shell:
```
`grub`
```

GRUB uses its own naming structure for drives and partitions in the form of _(hdn,m)_ , where _n_ is the hard drive number and _m_ is the partition number, both starting from zero. For example, partition `hda1` is _(hd0,0)_ to GRUB and `hdb3` is _(hd1,2)_. In contrast to Linux, GRUB does not consider CD-ROM drives to be hard drives. For example, if using a CD on `hdb` and a second hard drive on `hdc`, that second hard drive would still be _(hd1)_.
Using the above information, determine the appropriate designator for the root partition (or boot partition, if a separate one is used). For the following example, it is assumed that the root (or separate boot) partition is `hda4`.
Tell GRUB where to search for its `stage{1,2}` files. The Tab key can be used everywhere to make GRUB show the alternatives:
```
`root (hd0,3)`
```

###  Warning
The following command will overwrite the current boot loader. Do not run the command if this is not desired, for example, if using a third party boot manager to manage the Master Boot Record (MBR). In this scenario, it would make more sense to install GRUB into the “boot sector” of the LFS partition. In this case, this next command would become **`setup (hd0,3)`**.
Tell GRUB to install itself into the MBR of `had`:
```
`setup (hd0)`
```

If all went well, GRUB will have reported finding its files in `/boot/grub`. That's all there is to it. Quit the **grub** shell:
```
`quit`
```

Create a “menu list” file defining GRUB's boot menu:
```
`cat > /boot/grub/menu.lst << "EOF"
`# Begin /boot/grub/menu.lst
