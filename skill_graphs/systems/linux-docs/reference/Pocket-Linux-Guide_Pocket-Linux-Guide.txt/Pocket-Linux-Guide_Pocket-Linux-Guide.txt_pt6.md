-----------------------------------------------------------------------------

8.4. Implementation

8.4.1. System startup

Boot from the diskset in the usual way and log in as root.
-----------------------------------------------------------------------------

8.4.2. Test the "more" script

Display kernel messages by piping the output of dmesg to more.

bash# dmesg | more

Examine the local_fs script by using more with a command-line argument.

bash# more /etc/init.d/local_fs
-----------------------------------------------------------------------------

8.4.3. Use ps to show running processes

Display processes for the user currently logged in.

bash# ps

Display all available information about all running processes.

bash# ps -ef
-----------------------------------------------------------------------------

8.4.4. Run a simple sed script

Use sed to display an alternate version of /etc/passwd.

bash# sed -e "s/Legacy/Old School/" /etc/passwd

Verify that sed did not make the changes permanent.

bash# cat /etc/passwd
-----------------------------------------------------------------------------

8.4.5. Test the "ed" editor

Use ed to change properties on the "daemon" user.

bash# ed -p*
ed* r /etc/passwd
ed* %p
ed* /daemon/s/Legacy/Old School/
ed* %p
ed* w
ed* q

Verify that the changes are permanent (at least until the system is
restarted.)

bash# cat /etc/passwd
-----------------------------------------------------------------------------

8.4.6. System shutdown

Bring the system down gracefully with the shutdown command.
-----------------------------------------------------------------------------

Chapter 9. Project Wrap Up

9.1. Celebrating Accomplishments

As the Pocket Linux Project draws to a close we should take a moment to
celebrate all of our accomplishments. Some of the highlights are listed
below:

��*�We have built a system, from source code only, that fully implements all
    of the commands described in the Filesystem Hierarchy Standard
    requirements for a root filesystem.

��*�We have learned how to use Internet resources to locate and download the
    source code needed to build a GNU/Linux system.

��*�We have written basic system startup and shutdown scripts and configured
    them to execute in the proper runlevels.

��*�We have included support for multiple users on virtual consoles and
    implemented permissions on system files.

��*�But most importantly, we have learned some good design techniques and
    project management skills that will enable us to tackle any future
    projects with ease and confidence.


-----------------------------------------------------------------------------
9.2. Planning Next Steps

The Pocket Linux system is nearly overflowing, so there really is no more
room to expand the current root diskette to support any additional commands
and features. This leaves us with a few choices of where to go next. We can:

��*�Find a way to expand the current system just enough to host a small
    application. (For more information about hosting applications with Pocket
    Linux, see Appendix A)

��*�Remove multi-user capability and some of the less often used commands
    from the root disk, replacing them with utilities like tar and gzip that
    would be useful for a rescue/restore diskset.

��*�Use the techniques we have learned to design and build an entire GNU/
    Linux system and install it on a more spacious hard disk partition. (For
    more information about building a larger system, check out the GNU/Linux
    System Architect Toolkit at: [http://architect.sourceforge.net/] http://
    architect.sourceforge.net/.)


Which ever path is chosen, we can move forward confidently, armed with the
knowledge we need to be successful in our endeavors.
-----------------------------------------------------------------------------

Appendix A. Hosting Applications

A.1. Analysis

An operating system by itself is not much fun. What makes an OS great is the
applications that can be run on top of it. Unfortunately, Pocket Linux
currently does not have much room for anything other than system programs.
Still, it would be nice to expand the system just enough to host some cool
applications. Obviously a full-blown X-Windows GUI is out of the question,
but running a small console based program should be within our reach.

Rather than doing a typical "hello world" program as an example, application
hosting will be demonstrated using a console based audio player called
mp3blaster. Building mp3blaster offers more technical challenge than "hello
world" and the finished product should be a lot more fun. However, it should
not be construed that a console-based jukebox is the only application for
Pocket Linux. On the contrary, after completing this phase the reader should
have the knowledge and tools to build almost any console-based program he or
she desires.

So what will it take to turn a pocket-sized GNU/Linux system into a
pocket-sized mp3 player? A few things are listed below.

��*�Add support for audio hardware.

��*�Create space for the mp3blaster program.

��*�Provide a convenient way to access audio files.


-----------------------------------------------------------------------------
A.2. Design

A.2.1. Support for audio hardware

There is a vast proliferation of audio hardware on the market and each sound
card has its own particular configuration. For details on how to set up a
particular sound card we can turn to the Sound-HOWTO available from The Linux
Documentation Project. In a broader sense, however, we can treat a sound card
like any other piece of new hardware. To add new hardware to a GNU/Linux
system we will need configure the kernel to recognize it and configure /dev
files on the root disk to access it.
-----------------------------------------------------------------------------

A.2.1.1. Kernel support for audio

In order to support sound cards, a new kernel will have to be built. It is
very important that audio hardware support be configured as built-in, because
Pocket Linux is not set up to handle kernel modules.
-----------------------------------------------------------------------------

A.2.1.2. Root disk support for audio

Searching devices.txt for the keyword "sound" will list quite a few possible
audio devices, but usually only /dev/dsp and /dev/mixer are required to get
sound from a PC. These two files control the digital audio output and mixer
controls, respectively.
-----------------------------------------------------------------------------

A.2.2. Creating space for the program

Probably the easiest way to create more space for the mp3blaster program is
to mount an additional storage device. There are several choices for mount
points. So far /usr, /home and /opt are all empty directories and any one of
them could be used to mount a floppy, CD-ROM or additional compressed ramdisk
image. The /usr directory is a logical choice for a place to put an
application, but what about the choice of media? Mp3blaster and its required
libraries are too big to fit on a 1.44M floppy and burning a CD-ROM seems
like a lot of work for one little program. So given these constraints, the
best choice would be to put the program on a compressed floppy.
-----------------------------------------------------------------------------

A.2.2.1. Mounting additional compressed floppies

Mounting CDs and uncompressed diskettes is easy, but what about loading
compressed images from floppy into ramdisk? It will have to be done manually,
because automatic mounting of compressed floppies only works for the root
diskette. And using mount /dev/fd0 will not work because there is no
filesystem on the diskette, there are only the contents of a gzip file. The
actual filesystem is contained inside the gzip file. So how can we mount the
filesystem buried beneath the gzip file? This puzzle can be solved by
examining at the steps used to create the familiar compressed root disk
floppy.

 1. A ramdisk is created, mounted and filled with files.

 2. The ramdisk device is unmounted.

 3. The contents of the ramdisk are dumped to an image file using dd.

 4. The image file is compressed with gzip.

 5. The compressed image file is written to floppy with dd.


If that is how the compressed image makes its way from ramdisk to compressed
floppy, then going from compressed floppy to ramdisk should be as simple as
running through the steps in reverse.

 1. The compressed image file is read from floppy with dd.

 2. The image file is uncompressed with gunzip.

 3. The contents of the image file are dumped into ramdisk using dd.

 4. The ramdisk device is mounted.

 5. The files are available.


We can cut out the intermediate image file by using a pipe to combine dd and
gunzip like this: dd if=/dev/fd0 | gunzip -cq > /dev/ram1. Now the compressed
floppy goes straight into ramdisk, decompressing on the fly.
-----------------------------------------------------------------------------

A.2.2.2. Root disk support for additional ramdisks

We already have kernel support for ramdisks, because we are using a
compressed root disk, but we will need to create more ramdisks in /dev.
Typically the kernel supports eight ramdisks on /dev/ram0 through /dev/ram7
with ram0 being used for the rootdisk. The devices.txt file included in the
Linux source code documentation will be helpful for matching devices to their
major and minor numbers.
-----------------------------------------------------------------------------

A.2.3. Accessing audio files

The sample mp3 file that we will be using in our example is small enough to
fit on an uncompressed floppy disk so that there is no need to burn a CD.
However, serious music lovers may want to have the capability to mount a
custom CD-ROM full of tunes and that option will require support for
additional hardware.
-----------------------------------------------------------------------------

A.2.3.1. CD-ROM hardware support

Most modern CD-ROM drives will use IDE devices like /dev/hdc or /dev/hdd. To
support these CD-ROM drives we will have to configure IDE support in the
kernel and create the appropriate device files on the root disk.
-----------------------------------------------------------------------------

A.2.3.2. CD-ROM filesystem support

CD-ROMs have different filesystems than hard disks and floppies. Most CD
burning applications use a filesystem called ISO-9660 and have the capability
to support Joliet or Rockridge extensions. We will have to include support
for these filesystems in the kernel in order to mount CD-ROMs.
-----------------------------------------------------------------------------

A.2.4. Other required files

We will want to have all of mp3blaster's required libraries and other
supporting files available as part of the compressed /usr image so that
mp3blaster can run correctly. The familiar ldd command can be used to
determine which libraries mp3blaster requires. Any additional libraries can
be placed in /usr/lib. Even though some of the libraries may appear in /lib
on the development system, they can still go in /usr/lib on the Pocket Linux
system. The dynamic linker, ld-linux.so, is smart enough to look in both
places when loading libraries.

Because mp3blaster uses the curses (or ncurses) screen control library there
is one additional file we need. The curses library needs to know the
characteristics of the terminal it is controlling and it gets that
information from the terminfo database. The terminfo database consists of all
the files under the /usr/share/terminfo directory and is very large compared
to our available disk space. But, since Pocket Linux only supports the PC
console, we only have one terminal type to worry about and therefore need
only one file. The piece of the terminfo database we need is the file /usr/
share/terminfo/l/linux, because we are using a "Linux" terminal. For more
information about the subject of curses, see John Strang's book entitled
"Programming with Curses" available from O'Reilly publishing.
-----------------------------------------------------------------------------

A.2.5. Summary of tasks

Between sound cards, ramdisks, CD-ROMs and terminfo there is quite a bit to
keep track of. So let's take a moment to organize and summarize the tasks
necessary to make the pocket jukebox a reality.

��*�Create a new kernel disk that includes built-in support for audio
    hardware, IDE devices and CD-ROM filesystems.

��*�Create the appropriate /dev files on the root disk to support audio
    hardware, additional ramdisks and IDE CD-ROMs.

��*�Install the gunzip utility to enable decompression of the usr image.

��*�Create a startup script to load a compressed image from floppy into a
    ramdisk and mount the ramdisk on /usr.

��*�Create a compressed floppy that holds the mp3blaster program, its
    required libraries and terminfo files.


-----------------------------------------------------------------------------
A.3. Construction

A.3.1. Create an enhanced boot disk

A.3.1.1. Build a new kernel

bash# cd /usr/src/linux
bash# make menuconfig

Be sure to configure support for the following:

��*�386 processor

��*�Floppy disk

��*�RAM disk

��*�Second extended (ext2) filesystem

��*�Virtual console

��*�Audio hardware

��*�CD-ROM hardware

��*�ISO-9660 and Joliet filesystems


bash# make dep
bash# make clean
bash# make bzImage
-----------------------------------------------------------------------------

A.3.1.2. Copy the kernel to diskette

Place the boot disk in drive fd0

bash# mount /dev/fd0 /mnt
bash# cp /usr/src/linux/arch/i386/boot/bzImage /mnt/boot/vmlinuz
-----------------------------------------------------------------------------

A.3.1.3. Unmount the boot disk

bash# cd /
bash# umount /mnt
-----------------------------------------------------------------------------

A.3.2. Create an enhanced root disk

A.3.2.1. Create additional device files

A.3.2.1.1. IDE CD-ROM

bash# mknod -m640 ~/staging/dev/hdc b 22 0
bash# mknod -m640 ~/staging/dev/hdd b 22 64

Optionally create additional IDE devices.
-----------------------------------------------------------------------------

A.3.2.1.2. Ramdisk

bash# mknod -m 640 ~/staging/dev/ram1 b 1 1
bash# mknod -m 640 ~/staging/dev/ram2 b 1 2
bash# mknod -m 640 ~/staging/dev/ram3 b 1 3
bash# mknod -m 640 ~/staging/dev/ram4 b 1 4
bash# mknod -m 640 ~/staging/dev/ram5 b 1 5
bash# mknod -m 640 ~/staging/dev/ram6 b 1 6
bash# mknod -m 640 ~/staging/dev/ram7 b 1 7
-----------------------------------------------------------------------------

A.3.2.1.3. Audio

bash# mknod -m664 ~/staging/dev/dsp c 14 3
bash# mknod -m664 ~/staging/dev/mixer c 14 0
-----------------------------------------------------------------------------

A.3.2.2. Install the gunzip binary

bash# cd /usr/src/gzip-1.2.4a
bash# export CC="gcc -mcpu=i386"
bash# ./configure --host=i386-pc-linux-gnu
bash# make
bash# strip gzip
bash# cp gzip ~/staging/bin
bash# ln -s gzip ~/staging/bin/gunzip

Don't forget to verify library requirements, check the ownership and check
permissions on the gzip binary.
-----------------------------------------------------------------------------

A.3.2.3. Write a startup script to mount a compressed floppy

Use a text editor to create the following script and save it as ~/staging/etc
/init.d/usr_image

#!/bin/sh
#
# usr_image - load compressed images from floppy into ramdisk and
#             mount on /usr.
#
echo -n "Is there a compressed diskette to load for /usr [y/N]? "
read REPLY
if [ "$REPLY" = "y" ] || [ "$REPLY" = "Y" ]; then
  echo -n "Please insert the /usr floppy into fd0 and press <ENTER>."
  read REPLY
  echo "Clearing /dev/ram1."
  dd if=/dev/zero of=/dev/ram1 bs=1k count=4096
  echo "Loading compressed image from /dev/fd0 into /dev/ram1..."
  (dd if=/dev/fd0 bs=1k | gunzip -cq) >/dev/ram1 2>/dev/null
  fsck -fp /dev/ram1
  if [ $? -gt 1 ]; then
    echo "Filesystem errors on /dev/ram1!  Manual intervention required."
  else
    echo "Mounting /usr."
    mount /dev/ram1 /usr
  fi
fi
#
# end of usr_image

Configure the script to run right after root is mounted.

bash# ln -s ../init.d/usr_image ~/staging/etc/rcS.d/S21usr_image
-----------------------------------------------------------------------------

A.3.2.4. Create a compressed root disk

bash# cd /
bash# dd if=/dev/zero of=/dev/ram7 bs=1k count=4096
bash# mke2fs -m0 /dev/ram7
bash# mount /dev/ram7 /mnt
bash# cp -dpR ~/staging/* /mnt
bash# umount /dev/ram7
bash# dd if=/dev/ram7 of=~/phase8-image bs=1k
bash# gzip -9 ~/phase8-image

Insert the diskette labeled "root disk" into drive fd0.

bash# dd if=~/phase8-image.gz of=/dev/fd0 bs=1k
-----------------------------------------------------------------------------

A.3.3. Create a compressed /usr disk for mp3blaster

The compressed /usr diskette will be created in using the same process that
is used to create the compressed root disk. We will copy files to a staging
area, copy the staging area to ramdisk, compress the ramdisk and write it to
diskette.
-----------------------------------------------------------------------------

A.3.3.1. Create a staging area

bash# mkdir ~/usr-staging
bash# cd ~/usr-staging
bash# mkdir bin lib
bash# mkdir -p share/terminfo/l
-----------------------------------------------------------------------------

A.3.3.2. Install the mp3blaster program

Download the latest version of mp3blaster source code from its home at [http:
//www.stack.nl/~brama/mp3blaster/] http://www.stack.nl/~brama/mp3blaster/.

bash# cd ~/usr/src/mp3blaster-3.2.0
bash# ./configure
bash# make
bash# cp src/mp3blaster ~/usr-staging/bin
-----------------------------------------------------------------------------

A.3.3.3. Copy additional libraries and terminfo

Use ldd to find out which libraries are needed for mp3blaster.

Note The following is an example from the author's development system. It is
     possible that different systems may yield slightly different results in
     terms of library requirements.

bash# cd ~/usr-staging/lib
bash# ldd ~/usr-staging/bin/mp3blaster
bash# cp /usr/lib/ncurses.so.5.0  .
bash# cp /usr/lib/stdc++.so.3 .
bash# cp /lib/libm.so.6 .
bash# cp /usr/lib/libgcc_s.so.1 .
bash# cd ~/usr-staging/share/terminfo/l
bash# cp /usr/share/terminfo/l/linux .
-----------------------------------------------------------------------------

A.3.3.4. Make a compressed image and copy it to diskette

bash# cd /
bash# dd if=/dev/zero of=/dev/ram7 bs=1k count=4096
bash# mke2fs -m0 /dev/ram7
bash# mount /dev/ram7 /mnt
bash# cp -dpR ~/usr-staging/* /mnt
bash# umount /dev/ram7
bash# dd if=/dev/ram7 of=~/mp3blaster-image bs=1k
bash# gzip -9 ~/mp3blaster-image

Insert the diskette labeled "mp3blaster" into drive fd0.

bash# dd if=~/mp3blaster-image.gz of=/dev/fd0 bs=1k
-----------------------------------------------------------------------------

A.3.4. Create a data diskette for testing

Go to the Internet site [http://www.paul.sladen.org] http://
www.paul.sladen.org and download the mp3 file of Linus Torvalds pronouncing
"Linux." The direct link is: [http://www.paul.sladen.org/pronunciation/
torvalds-says-linux.mp3] http://www.paul.sladen.org/pronunciation/
torvalds-says-linux.mp3. Create a Second Extended (ext2) filesystem on a
floppy and copy the mp3 file onto the diskette.
-----------------------------------------------------------------------------

A.4. Implementation

A.4.1. System Startup

 1. Boot from the kernel diskette.

 2. Insert the root floppy when prompted.

 3. When prompted for a /usr diskette, say 'Y'.

 4. Insert the mp3blaster diskette and press Enter.


-----------------------------------------------------------------------------
A.4.2. Verify that the /usr diskette loaded properly

bash# mount
bash# ls -lR /usr
-----------------------------------------------------------------------------

A.4.3. Check the audio device initialization

bash# dmesg | more

If everything worked there should be a line or two indicating that the kernel
found the audio hardware. The example below shows how the kernel might report
a Yamaha integrated sound system.

ymfpci: YMF740C at 0xf4000000 IRQ 10
ac97_codec: AC97 Audio codec, id: 0x4144:0x5303 (Analog Devices AD1819)
-----------------------------------------------------------------------------

A.4.4. Test audio output
