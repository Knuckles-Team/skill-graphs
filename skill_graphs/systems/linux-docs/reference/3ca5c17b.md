#  A.3. Construction
##  A.3.1. Create an enhanced boot disk
###  A.3.1.1. Build a new kernel
```
bash# cd /usr/src/linux
bash# make menuconfig
```

---
Be sure to configure support for the following:
  * 386 processor
  * Floppy disk
  * RAM disk
  * Second extended (ext2) filesystem
  * Virtual console
  * Audio hardware
  * CD-ROM hardware
  * ISO-9660 and Joliet filesystems

```
bash# make dep
bash# make clean
bash# make bzImage
```

---
* * *
###  A.3.1.2. Copy the kernel to diskette
Place the boot disk in drive fd0
```
bash# mount /dev/fd0 /mnt
bash# cp /usr/src/linux/arch/i386/boot/bzImage /mnt/boot/vmlinuz
```

---
* * *
###  A.3.1.3. Unmount the boot disk
```
bash# cd /
bash# umount /mnt
```

---
* * *
##  A.3.2. Create an enhanced root disk
###  A.3.2.1. Create additional device files
####  A.3.2.1.1. IDE CD-ROM
```
bash# mknod -m640 ~/staging/dev/hdc b 22 0
bash# mknod -m640 ~/staging/dev/hdd b 22 64
```

---
Optionally create additional IDE devices.
* * *
####  A.3.2.1.2. Ramdisk
```
bash# mknod -m 640 ~/staging/dev/ram1 b 1 1
bash# mknod -m 640 ~/staging/dev/ram2 b 1 2
bash# mknod -m 640 ~/staging/dev/ram3 b 1 3
bash# mknod -m 640 ~/staging/dev/ram4 b 1 4
bash# mknod -m 640 ~/staging/dev/ram5 b 1 5
bash# mknod -m 640 ~/staging/dev/ram6 b 1 6
bash# mknod -m 640 ~/staging/dev/ram7 b 1 7
```

---
* * *
####  A.3.2.1.3. Audio
```
bash# mknod -m664 ~/staging/dev/dsp c 14 3
bash# mknod -m664 ~/staging/dev/mixer c 14 0
```

---
* * *
###  A.3.2.2. Install the gunzip binary
```
bash# cd /usr/src/gzip-1.2.4a
bash# export CC="gcc -mcpu=i386"
bash# ./configure --host=i386-pc-linux-gnu
bash# make
bash# strip gzip
bash# cp gzip ~/staging/bin
bash# ln -s gzip ~/staging/bin/gunzip
```

---
Don't forget to verify library requirements, check the ownership and check permissions on the gzip binary.
* * *
###  A.3.2.3. Write a startup script to mount a compressed floppy
Use a text editor to create the following script and save it as `~/staging/etc/init.d/usr_image`
```
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
```

---
Configure the script to run right after root is mounted.
```
bash# ln -s ../init.d/usr_image ~/staging/etc/rcS.d/S21usr_image
```

---
* * *
###  A.3.2.4. Create a compressed root disk
```
bash# cd /
bash# dd if=/dev/zero of=/dev/ram7 bs=1k count=4096
bash# mke2fs -m0 /dev/ram7
bash# mount /dev/ram7 /mnt
bash# cp -dpR ~/staging/* /mnt
bash# umount /dev/ram7
bash# dd if=/dev/ram7 of=~/phase8-image bs=1k
bash# gzip -9 ~/phase8-image
```

---
Insert the diskette labeled "root disk" into drive fd0.
```
bash# dd if=~/phase8-image.gz of=/dev/fd0 bs=1k
```

---
* * *
##  A.3.3. Create a compressed /usr disk for mp3blaster
The compressed /usr diskette will be created in using the same process that is used to create the compressed root disk. We will copy files to a staging area, copy the staging area to ramdisk, compress the ramdisk and write it to diskette.
* * *
###  A.3.3.1. Create a staging area
```
bash# mkdir ~/usr-staging
bash# cd ~/usr-staging
bash# mkdir bin lib
bash# mkdir -p share/terminfo/l
```

---
* * *
###  A.3.3.2. Install the mp3blaster program
Download the latest version of mp3blaster source code from its home at
```
bash# cd ~/usr/src/mp3blaster-3.2.0
bash# ./configure
bash# make
bash# cp src/mp3blaster ~/usr-staging/bin
```

---
* * *
###  A.3.3.3. Copy additional libraries and terminfo
Use **ldd** to find out which libraries are needed for mp3blaster.
![Note](https://tldp.org/LDP/Pocket-Linux-Guide/images/note.gif) | The following is an example from the author's development system. It is possible that different systems may yield slightly different results in terms of library requirements.
---|---
```
bash# cd ~/usr-staging/lib
bash# ldd ~/usr-staging/bin/mp3blaster
bash# cp /usr/lib/ncurses.so.5.0  .
bash# cp /usr/lib/stdc++.so.3 .
bash# cp /lib/libm.so.6 .
bash# cp /usr/lib/libgcc_s.so.1 .
bash# cd ~/usr-staging/share/terminfo/l
bash# cp /usr/share/terminfo/l/linux .
```

---
* * *
###  A.3.3.4. Make a compressed image and copy it to diskette
```
bash# cd /
bash# dd if=/dev/zero of=/dev/ram7 bs=1k count=4096
bash# mke2fs -m0 /dev/ram7
bash# mount /dev/ram7 /mnt
bash# cp -dpR ~/usr-staging/* /mnt
bash# umount /dev/ram7
bash# dd if=/dev/ram7 of=~/mp3blaster-image bs=1k
bash# gzip -9 ~/mp3blaster-image
```

---
Insert the diskette labeled "mp3blaster" into drive fd0.
```
bash# dd if=~/mp3blaster-image.gz of=/dev/fd0 bs=1k
```

---
* * *
##  A.3.4. Create a data diskette for testing
Go to the Internet site
* * *
