
grub> kernel (fd0)/boot/vmlinuz init=/bin/sh root=/dev/fd0 load_ramdisk=1 prompt_ramdisk=1
   [Linux-bzImage, setup=0xc00, size=0xce29b]

grub> boot

Linux version 2.4.26
..
.. [various kernel messages]
..
VFS: Insert root floppy disk to be loaded into RAM disk and press ENTER
RAMDISK: ext2 filesystem found at block 0
RAMDISK: Loading 1440 blocks [1 disk] into ram disk... done.
VFS: Mounted root (ext2 filesystem) readonly.
Freeing unused kernel memory: 178k freed
# _
-----------------------------------------------------------------------------

2.4.2. Testing what works

Try out a few of BASH's built-in commands to see if things are working
properly.

bash# echo "Hello World"
bash# cd /
bash# pwd
bash# echo *
-----------------------------------------------------------------------------

2.4.3. Noting what does not work

Try out a few other familiar commands.

bash# ls /var
bash# mkdir /var/tmp

Notice that only commands internal to BASH actually work and that external
commands like ls and mkdir do not work at all. This shortcoming is something
that can be addressed in a future phase of the project. For now we should
just enjoy the fact that our prototype boot / root diskset works and that it
was not all that hard to build.
-----------------------------------------------------------------------------

2.4.4. System shutdown

Remove the diskette from fd0 and restart the system using CTRL-ALT-DELETE.
-----------------------------------------------------------------------------

Chapter 3. Saving Space

3.1. Analysis

One of the drawbacks in the prototype phase of the project was that the
diskset was not all that useful. The only commands that worked were the ones
built into the BASH shell. We could improve our root disk by installing
commands like cat, ls, mv, rm and so on. Unfortunately, we are short on
space. The current root disk has no shared libraries so each utility would
have to be statically-linked just like the BASH shell. A lot of big binaries
together with a static shell will rapidly exceed the tiny 1.44M of available
disk space. So our main goal in this phase should be to maximize space
savings on the root disk and pave the way for expanded functionality in the
next phase.
-----------------------------------------------------------------------------

3.2. Design

Take another look at the Bootdisk-HOWTO and notice how many utilities can be
squeezed onto a 1.44M floppy. There are three things that make this possible.
One is the use of shared libraries. The second is stripped binaries. And the
third is the use of a compressed filesystem. We can use all of these
techniques to save space on our root disk.
-----------------------------------------------------------------------------

3.2.1. Shared Libraries

First, in order to use shared libraries we will need to rebuild the BASH
shell. This time we will configure it without using the --enable-static-link
option. Once BASH is rebuilt we need to figure out which libraries it is
linked with and be sure to include them on the root disk. The ldd command
makes this job easy. By typing ldd bash on the command-line we can see a list
of all the shared libraries that BASH uses. As long as all these libraries
are copied to the root disk, the new BASH build should work fine.
-----------------------------------------------------------------------------

3.2.2. Stripped Binaries

Next, we should strip any binaries that get copied to the root disk. The
manpage for strip does not give much description of what it does other than
to say, "strip discards all symbols from the object files." It seems like
removing pieces of a binary would render it useless, but this is not the
case. The reason it works is because a large number of these discarded
symbols are used for debugging. While debugging symbols are very helpful to
programmers working to improve the code, they do not do much for the average
end-user other than take up more disk space. And since space is at a premium,
we should definitely remove as many symbols as possible from BASH and any
other binaries before we copy over them to the ramdisk.

The process of stripping files to save space also works with shared library
files. But when stripping libraries it is important to use the
--strip-unneeded option so as not to break them. Using --strip-unneeded
shrinks the file size, but leaves the symbols needed for relocation intact
which is something that shared libraries need to function properly.
-----------------------------------------------------------------------------

3.2.3. Compressed Root Filesystem

Finally, we can tackle the problem of how to build a compressed root
filesystem. The Bootdisk-HOWTO suggests three ways of constructing a
compressed root filesystem using either a ramdisk, a spare hard drive
partition or a loopback device. This project will concentrate on using the
ramdisk approach. It seems logical that if the root filesystem is going to be
run from a ramdisk, it may as well be built on a ramdisk. All we have to do
is create a second extended filesystem on a ramdisk device, mount it and copy
files to it. Once the filesystem is populated with all the files that the
root disk needs, we simply unmount it, compress it and write it out to
floppy.

Note For this to work, we need to make sure the system used for building has
     ramdisk support. If ramdisk is not available it is also possible to use
     a loopback device. See the Bootdisk-HOWTO for more information on using
     loopback devices.
-----------------------------------------------------------------------------

3.3. Construction

This section is written using ramdisk seven (/dev/ram7) to build the root
image. There is nothing particularly special about ramdisk seven and it is
possible to use any of the other available ramdisks provided they are not
already in use.
-----------------------------------------------------------------------------

3.3.1. Create a ramdisk

bash# dd if=/dev/zero of=/dev/ram7 bs=1k count=4096
bash# mke2fs -m0 /dev/ram7 4096
bash# mount /dev/ram7 /mnt
-----------------------------------------------------------------------------

3.3.2. Rebuild the BASH shell

bash# cd /usr/src/bash-3.0
bash# make distclean
bash# export CC="gcc -mcpu=i386"
bash# ./configure --enable-minimal-config --host=i386-pc-linux-gnu
bash# make
bash# strip bash
-----------------------------------------------------------------------------

3.3.3. Determine which libraries are required

bash# ldd bash

View the output from the ldd command. It should look similar to the example
below.
bash# ldd bash
  libdl.so.2 => /lib/libdl.so.2 (0x4001d000)
  libc.so.6 => /lib/libc.so.6 (0x40020000)
  /lib/ld-linux.so.2 => /lib/ld-linux.so.2 (0x40000000)

Note Some systems may have a slightly different library set up. For example,
     you may see libc.so.6 => /lib/tls/libc.so.6 rather than libc.so.6 => /
     lib/libc.so.6 as shown in the example. If your ldd output does not match
     the example then use the path given by your ldd command when completing
     the next step.
-----------------------------------------------------------------------------

3.3.4. Copy BASH and its libraries to the ramdisk

bash# mkdir /mnt/bin
bash# cp bash /mnt/bin
bash# ln -s bash /mnt/bin/sh
bash# mkdir /mnt/lib
bash# strip --strip-unneeded -o /mnt/lib/libdl.so.2 /lib/libdl.so.2
bash# strip --strip-unneeded -o /mnt/lib/libc.so.6 /lib/libc.so.6
bash# strip --strip-unneeded -o /mnt/lib/ld-linux.so.2 /lib/ld-linux.so.2
bash# chmod +x /mnt/lib/ld-linux.so.2

Note Using strip -o might seem an odd way to copy library files from the
     development system to the ramdisk. What it does is strip the symbols
     while the file is in transit from the source location to the
     destination. This has the effect of stripping symbols from the library
     on the ramdisk without altering the libraries on the development system.
     Unfortunately file permissions are lost when copying libraries this way
     which is why the chmod +x command is then used to set the execute flag
     for the rootdisk's dynamic loader.
-----------------------------------------------------------------------------

3.3.5. Create a console device

bash# mkdir /mnt/dev
bash# mknod /mnt/dev/console c 5 1
-----------------------------------------------------------------------------

3.3.6. Compress the ramdisk image

bash# cd /
bash# umount /dev/ram7
bash# dd if=/dev/ram7 of=~/phase2-image bs=1k count=4096
bash# gzip -9 ~/phase2-image
-----------------------------------------------------------------------------

3.3.7. Copy the compressed image to diskette

Insert the floppy labeled "root disk" into drive fd0.

bash# dd if=~/phase2-image.gz of=/dev/fd0 bs=1k
-----------------------------------------------------------------------------

3.4. Implementation

Successful implementation of this phase is probably the most difficult part
of the Pocket Linux Guide. If you need help getting things to work please
visit the Pocket Linux Guide Resource Site to browse the troubleshooting
forum and subscribe to the mailing list.
-----------------------------------------------------------------------------

3.4.1. System startup

Follow these steps to boot:

��*�Restart the PC using the boot disk from the previous chapter.

��*�At the grub> prompt, type kernel (fd0)/boot/vmlinuz init=/bin/sh root=/
    dev/fd0 load_ramdisk=1 prompt_ramdisk=1 and press Enter.

��*�Type boot at the grub> prompt and press Enter.

��*�Insert the new, compressed root disk when prompted.


The screen output should be similar to the following example:

GNU GRUB version 0.95

grub> kernel (fd0)/boot/vmlinuz init=/bin/sh root=/dev/fd0 load_ramdisk=1 prompt_ramdisk=1
   [Linux-bzImage, setup=0xc00, size=0xce29b]

grub> boot

Linux version 2.4.26
..
.. [various kernel messages]
..
VFS: Insert root floppy disk to be loaded into RAM disk and press ENTER
RAMDISK: Compressed image found at block 0
VFS: Mounted root (ext2 filesystem) readonly.
Freeing unused kernel memory: 178k freed
# _
-----------------------------------------------------------------------------

3.4.2. Verify results

If the implementation was successful, this new root disk should behave
exactly like the root disk from the previous chapter. The key difference is
that this compressed root disk has much more room to grow and we will put
this extra space to good use in the next phase of the project.
-----------------------------------------------------------------------------

3.4.3. System shutdown

Remove the diskette from fd0 and restart the system using CTRL-ALT-DELETE.
-----------------------------------------------------------------------------

Chapter 4. Some Basic Utilities

4.1. Analysis

In the previous chapter it might seem like we did not accomplish very much. A
lot of energy was expended redesigning the root disk, but the functionality
is basically the same as in the initial prototype phase. The root disk still
does not do very much. But we did make significant improvements when it comes
to space savings. In this chapter we will put that extra space to good use
and start cramming the root disk with as many utilities as it can hold.

The first two root disks we built only had shell built-in commands like echo
and pwd. This time it would be nice to have some of the commonly used
external commands like cat, ls, mkdir, rm and such on the root disk. Keeping
this in mind we can define the goals for this phase as follows:

��*�Retain all of the functionality from the previous root disk.

��*�Add some of the commonly used external commands.


-----------------------------------------------------------------------------
4.2. Design

4.2.1. Determining Required Commands

The first question that might come to mind is, "How do we know which commands
are needed?" It is possible to just start with cat and ls then install other
commands as we discover a need for them. But this is terribly inefficient. We
need a plan or a blueprint to work from. For this we can turn to the
Filesystem Hierarchy Standard (FHS) available from [http://www.pathname.com/
fhs/] http://www.pathname.com/fhs/. The FHS dictates which commands should be
present on a Linux system and where they should be placed in the directory
structure.
-----------------------------------------------------------------------------

4.2.2. Locating Source Code

The next logical question is, "Now that we know what we need, where do we get
the source code?" One way to find the answer to this question is to check the
manpages. We can either search the manpages included with one of the popular
GNU/Linux distributions or use one of the manpage search engines listed at
[http://www.tldp.org/docs.html#man] http://www.tldp.org/docs.html#man. One
thing that should tip us off as to where to find the source code for a
particular command is the email address listed for reporting bugs. For
example the cat manpage lists bug-textutils@gnu.org. From this email address
we can deduce that cat is part of the textutils package from [http://gnu.org]
GNU.
-----------------------------------------------------------------------------

4.2.3. Leveraging FHS

So let's look at the FHS requirements for the /bin directory. The first few
commands in the list are cat, chgrp, chmod, chown and cp. We already know
that cat is part of GNU's textutils. Using the next few commands as keywords
in a manpage search we discover that we need GNU's fileutils package for
chmod, chgrp, chown and cp. In fact quite a few of the commands in /bin come
from GNU's fileutils. The date command also comes from a GNU package called
sh-utils. So a good way to tackle the problem of finding source code might be
to group the commands together by package as shown below.

��*�The BASH shell -- echo, false, pwd, sh, true

��*�GNU textutils -- cat

��*�GNU fileutils -- chgrp, chmod, chown, cp, dd, df, ln, ls, mkdir, mknod,
    mv, rm, rmdir, sync

��*�GNU sh-utils -- date, hostname, stty, su, uname


These four packages do not contain all of the commands in the /bin directory,
but they do represent of over 70% of them. That should be enough to
accomplish our goal of adding some of the commonly used external commands. We
can worry about the other commands in later phases of the project.
-----------------------------------------------------------------------------

4.2.4. Downloading Source Code

To fetch the source code we simply need to connect to [ftp://ftp.gnu.org/gnu]
GNU's FTP site and navigate to the appropriate package directory.

When we get to the directory for textutils there are several versions
available. There is also a note informing us that the package has been
renamed to coreutils. The same message about coreutils appears in the
fileutils and sh-utils directories as well. So instead of downloading three
separate packages we can get everything in one convenient bundle in the
coreutils directory.
-----------------------------------------------------------------------------

4.3. Construction

Rather than copying files directly to the ramdisk, we can make things easier
by setting up a staging area. The staging area will give us room to work
without worrying about the space constraints of the ramdisk. It will also
provide a way to save our work and make it easier to enhance the rootdisk in
later phases of the project.

The staging procedure will work like this:

 1. Create a directory structure as defined in the FHS.

 2. Copy in the files from phase 2's root disk.

 3. Build the new package from source code.

 4. Install files into the correct FHS directories.

 5. Strip the binaries to save space.

 6. Check library dependencies.

 7. Copy to the whole directory structure to the ramdisk.

 8. Compress the ramdisk and write it out to floppy.


-----------------------------------------------------------------------------
4.3.1. Create a staging area

bash# mkdir ~/staging
bash# cd ~/staging
bash# mkdir bin boot dev etc home lib mnt opt proc root sbin tmp usr var
bash# mkdir var/log var/run
-----------------------------------------------------------------------------

4.3.2. Copy contents of phase 2 rootdisk

bash# dd if=~/phase2-image.gz | gunzip -c > /dev/ram7
bash# mount /dev/ram7 /mnt
bash# cp -dpR /mnt/* ~/staging
bash# umount /dev/ram7
bash# rmdir ~/staging/lost+found
-----------------------------------------------------------------------------

4.3.3. Install binaries from GNU coreutils

Download a recent version of coreutils from [ftp://ftp.gnu.org/gnu/coreutils
/] ftp://ftp.gnu.org/gnu/coreutils/

bash# cd /usr/src/coreutils-5.2.1
bash# export CC="gcc -mcpu=i386"
bash# ./configure --host=i386-pc-linux-gnu
bash# make
bash# cd src
bash# cp cat chgrp chmod chown cp date dd df ~/staging/bin
bash# cp hostname ln ls mkdir mkfifo mknod ~/staging/bin
bash# cp mv rm rmdir stty su sync uname ~/staging/bin
-----------------------------------------------------------------------------

4.3.4. Copy additional libraries

Check library requirements by using ldd on some of the new binaries.

bash# ldd ~/staging/bin/cat
bash# ldd ~/staging/bin/ls
bash# ldd ~/staging/bin/su
bash# ls ~/staging/lib

Note the differences in the required libraries, as shown by the ldd command,
and the libraries present in the staging area, as shown by the ls command,
then copy any missing libraries to the staging area.

bash# cp /lib/librt.so.1 ~/staging/lib
bash# cp /lib/libpthread.so.0 ~/staging/lib
bash# cp /lib/libcrypt.so.1 ~/staging/lib
-----------------------------------------------------------------------------

4.3.5. Strip binaries and libraries

bash# strip ~/staging/bin/*
bash# strip --strip-unneeded ~/staging/lib/*
-----------------------------------------------------------------------------

4.3.6. Create a compressed root disk image

bash# cd /
bash# dd if=/dev/zero of=/dev/ram7 bs=1k count=4096
bash# mke2fs -m0 /dev/ram7 4096
bash# mount /dev/ram7 /mnt
bash# cp -dpR ~/staging/* /mnt
bash# umount /dev/ram7
bash# dd if=/dev/ram7 of=~/phase3-image bs=1k count=4096
bash# gzip -9 ~/phase3-image

Note The process for creating the compressed root disk image will change very
     little throughout the remaining chapters. Writing a small script to
     handle this function can be a great time saver.
-----------------------------------------------------------------------------

4.3.7. Write the root disk image to floppy

Insert the diskette labeled "root disk" into drive fd0.

bash# dd if=~/phase3-image.gz of=/dev/fd0 bs=1k
-----------------------------------------------------------------------------

4.4. Implementation

We will need to have a read-write filesystem in order for some of the
commands to work. The kernel's normal behavior is to mount root as read-only,
but we can change this using a kernel option. By passing the kernel the rw
option before init=/bin/sh we will get a read-write root filesystem.
-----------------------------------------------------------------------------

4.4.1. System startup

Follow these steps to get the system running.

��*�Boot the PC from using the GRUB boot disk.

��*�At the grub> prompt, type kernel (fd0)/boot/vmlinuz rw init=/bin/sh root=
    /dev/fd0 load_ramdisk=1 prompt_ramdisk=1.

��*�Verify that you remembered to add the rw parameter and press Enter.

��*�Type boot and press Enter.

��*�Insert the recently created root disk when prompted.


The terminal display should look similar to the example below.

GNU GRUB version 0.95

grub> kernel (fd0)/boot/vmlinuz rw init=/bin/sh root=/dev/fd0 load_ramdisk=1 prompt_ramdisk=1
   [Linux-bzImage, setup=0xc00, size=0xce29b]

grub> boot

Linux version 2.4.26
