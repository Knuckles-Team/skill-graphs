#  A.2. Design
##  A.2.1. Support for audio hardware
There is a vast proliferation of audio hardware on the market and each sound card has its own particular configuration. For details on how to set up a particular sound card we can turn to the Sound-HOWTO available from [The Linux Documentation Project](http://www.tldp.org). In a broader sense, however, we can treat a sound card like any other piece of new hardware. To add new hardware to a GNU/Linux system we will need configure the kernel to recognize it and configure `/dev` files on the root disk to access it.
* * *
###  A.2.1.1. Kernel support for audio
In order to support sound cards, a new kernel will have to be built. It is very important that audio hardware support be configured as built-in, because Pocket Linux is not set up to handle kernel modules.
* * *
###  A.2.1.2. Root disk support for audio
Searching `devices.txt` for the keyword "sound" will list quite a few possible audio devices, but usually only `/dev/dsp` and `/dev/mixer` are required to get sound from a PC. These two files control the digital audio output and mixer controls, respectively.
* * *
##  A.2.2. Creating space for the program
Probably the easiest way to create more space for the mp3blaster program is to mount an additional storage device. There are several choices for mount points. So far `/usr`, `/home` and `/opt` are all empty directories and any one of them could be used to mount a floppy, CD-ROM or additional compressed ramdisk image. The `/usr` directory is a logical choice for a place to put an application, but what about the choice of media? Mp3blaster and its required libraries are too big to fit on a 1.44M floppy and burning a CD-ROM seems like a lot of work for one little program. So given these constraints, the best choice would be to put the program on a compressed floppy.
* * *
###  A.2.2.1. Mounting additional compressed floppies
Mounting CDs and uncompressed diskettes is easy, but what about loading compressed images from floppy into ramdisk? It will have to be done manually, because automatic mounting of compressed floppies only works for the root diskette. And using **mount /dev/fd0** will not work because there is no filesystem on the diskette, there are only the contents of a gzip file. The actual filesystem is contained inside the gzip file. So how can we mount the filesystem buried beneath the gzip file? This puzzle can be solved by examining at the steps used to create the familiar compressed root disk floppy.
  1. A ramdisk is created, mounted and filled with files.
  2. The ramdisk device is unmounted.
  3. The contents of the ramdisk are dumped to an image file using **dd**.
  4. The image file is compressed with **gzip**.
  5. The compressed image file is written to floppy with **dd**.


If that is how the compressed image makes its way from ramdisk to compressed floppy, then going from compressed floppy to ramdisk should be as simple as running through the steps in reverse.
  1. The compressed image file is read from floppy with **dd**.
  2. The image file is uncompressed with **gunzip**.
  3. The contents of the image file are dumped into ramdisk using **dd**.
  4. The ramdisk device is mounted.
  5. The files are available.


We can cut out the intermediate image file by using a pipe to combine **dd** and **gunzip** like this: **dd if=/dev/fd0 | gunzip -cq > /dev/ram1**. Now the compressed floppy goes straight into ramdisk, decompressing on the fly.
* * *
###  A.2.2.2. Root disk support for additional ramdisks
We already have kernel support for ramdisks, because we are using a compressed root disk, but we will need to create more ramdisks in `/dev`. Typically the kernel supports eight ramdisks on `/dev/ram0` through `/dev/ram7` with `ram0` being used for the rootdisk. The `devices.txt` file included in the Linux source code documentation will be helpful for matching devices to their major and minor numbers.
* * *
##  A.2.3. Accessing audio files
The sample mp3 file that we will be using in our example is small enough to fit on an uncompressed floppy disk so that there is no need to burn a CD. However, serious music lovers may want to have the capability to mount a custom CD-ROM full of tunes and that option will require support for additional hardware.
* * *
###  A.2.3.1. CD-ROM hardware support
Most modern CD-ROM drives will use IDE devices like `/dev/hdc` or `/dev/hdd`. To support these CD-ROM drives we will have to configure IDE support in the kernel and create the appropriate device files on the root disk.
* * *
###  A.2.3.2. CD-ROM filesystem support
CD-ROMs have different filesystems than hard disks and floppies. Most CD burning applications use a filesystem called ISO-9660 and have the capability to support Joliet or Rockridge extensions. We will have to include support for these filesystems in the kernel in order to mount CD-ROMs.
* * *
##  A.2.4. Other required files
We will want to have all of mp3blaster's required libraries and other supporting files available as part of the compressed `/usr` image so that mp3blaster can run correctly. The familiar **ldd** command can be used to determine which libraries mp3blaster requires. Any additional libraries can be placed in `/usr/lib`. Even though some of the libraries may appear in `/lib` on the development system, they can still go in `/usr/lib` on the Pocket Linux system. The dynamic linker, `ld-linux.so`, is smart enough to look in both places when loading libraries.
Because mp3blaster uses the curses (or ncurses) screen control library there is one additional file we need. The curses library needs to know the characteristics of the terminal it is controlling and it gets that information from the terminfo database. The terminfo database consists of all the files under the `/usr/share/terminfo` directory and is very large compared to our available disk space. But, since Pocket Linux only supports the PC console, we only have one terminal type to worry about and therefore need only one file. The piece of the terminfo database we need is the file `/usr/share/terminfo/l/linux`, because we are using a "Linux" terminal. For more information about the subject of curses, see John Strang's book entitled "Programming with Curses" available from
* * *
##  A.2.5. Summary of tasks
Between sound cards, ramdisks, CD-ROMs and terminfo there is quite a bit to keep track of. So let's take a moment to organize and summarize the tasks necessary to make the pocket jukebox a reality.
  * Create a new kernel disk that includes built-in support for audio hardware, IDE devices and CD-ROM filesystems.
  * Create the appropriate `/dev` files on the root disk to support audio hardware, additional ramdisks and IDE CD-ROMs.
  * Install the **gunzip** utility to enable decompression of the usr image.
  * Create a startup script to load a compressed image from floppy into a ramdisk and mount the ramdisk on `/usr`.
  * Create a compressed floppy that holds the mp3blaster program, its required libraries and terminfo files.


* * *
