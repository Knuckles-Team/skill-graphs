
  The setup will differ from host to host. Therefore, no program
  should rely on this location.

  If you want to find out a user's home directory, you should use the
  getpwent(3) library function rather than relying on /etc/passwd because
  user information may be stored remotely using systems such as NIS.

  User specific configuration files for applications are stored in the
  user's home directory in a file that starts with the '.' character
  (a "dot file"). If an application needs to create more than one dot
  file then they should be placed in a subdirectory with a name starting
  with a '.' character, (a "dot directory"). In this case the
  configuration files should not start with the '.' character.

  It is recommended that apart from autosave and lock files programs
  should refrain from creating non dot files or directories in a home
  directory without user intervention.

-----------------------------------------------------------------------------

1.8. /initrd


initrd provides the capability to load a RAM disk by the boot
loader. This RAM disk can then be mounted as the root file
system and programs can be run from it. Afterwards, a new
root file system can be mounted from a different device. The
previous root (from initrd) is then moved to a directory and
can be subsequently unmounted.

initrd is mainly designed to allow system startup to occur
in two phases, where the kernel comes up with a minimum set
of compiled-in drivers, and where additional modules are
loaded from initrd.

Operation
---------

When using initrd, the system typically boots as follows:

 1) the boot loader loads the kernel and the initial RAM disk
 2) the kernel converts initrd into a "normal" RAM disk and
    frees the memory used by initrd
 3) initrd is mounted read-write as root
 4) /linuxrc is executed (this can be any valid executable,
 including shell scripts; it is run with uid 0 and can do
 basically everything init can do)
 5) linuxrc mounts the "real" root file system
 6) linuxrc places the root file system at the root directory
    using the pivot_root system call
 7) the usual boot sequence (e.g. invocation of /sbin/init) is
    performed on the root file system
 8) the initrd file system is removed

Note that changing the root directory does not involve unmounting
it. It is therefore possible to leave processes running on initrd
during that procedure. Also note that file systems mounted under
initrd continue to be accessible.

Usage scenarios
---------------

The main motivation for implementing initrd was to allow
for modular kernel configuration at system installation.
The procedure would work as follows:

 1) system boots from floppy or other media with a minimal kernel
    (e.g. support for RAM disks, initrd, a.out, and the Ext2 FS)
    and loads initrd
 2) /linuxrc determines what is needed to (1) mount the "real" root
    FS (i.e. device type, device drivers, file system) and (2) the
    distribution media (e.g. CD-ROM, network, tape, ...). This can
    be done by asking the user, by auto-probing, or by using a
    hybrid approach.
 3) /linuxrc loads the necessary kernel modules
 4) /linuxrc creates and populates the root file system (this
    doesn't have to be a very usable system yet)
 5) /linuxrc invokes pivot_root to change the root file system and
    execs - via chroot - a program that continues the installation
 6) the boot loader is installed
 7) the boot loader is configured to load an initrd with the set of
    modules that was used to bring up the system (e.g. /initrd can
    be modified, then unmounted, and finally, the image is written
    from /dev/ram0 or /dev/rd/0 to a file)
 8) now the system is bootable and additional installation tasks
    can be performed

The key role of initrd here is to reuse the configuration data
during normal system operation without requiring the use of a
bloated "generic" kernel or re-compiling or re-linking the kernel.

A second scenario is for installations where Linux runs on systems
with different hardware configurations in a single administrative
domain. In such cases, it is desirable to generate only a small set
of kernels (ideally only one) and to keep the system-specific part
of configuration information as small as possible. In this case, a
common initrd could be generated with all the necessary modules.
Then, only /linuxrc or a file read by it would have to be different.

A third scenario are more convenient recovery disks, because
information like the location of the root FS partition doesn't have
to be provided at boot time, but the system loaded from initrd can
invoke a user-friendly dialog and it can also perform some sanity
checks (or even some form of auto-detection).

Last not least, CD-ROM distributors may use it for better installation
from CD, e.g. by using a boot floppy and bootstrapping a bigger RAM disk
via initrd from CD; or by booting via a loader like LOADLIN or directly
from the CD-ROM, and loading the RAM disk from CD without need of floppies.
-----------------------------------------------------------------------------

1.9. /lib

 The /lib directory contains kernel modules and those shared library images
(the C programming code library) needed to boot the system and run the
commands in the root filesystem, ie. by binaries in /bin and /sbin. Libraries
are readily identifiable through their filename extension of *.so. Windows
equivalent to a shared library would be a DLL (dynamically linked library)
file. They are essential for basic system functionality. Kernel modules
(drivers) are in the subdirectory /lib/modules/'kernel-version'. To ensure
proper module compilation you should ensure that /lib/modules/
'kernel-version'/kernel/build points to /usr/src/'kernel-version' or ensure
that the Makefile knows where the kernel source itself are located.



/lib/'machine-architecture'
    Contains platform/architecture dependent libraries.

/lib/iptables
    iptables shared library files.

/lib/kbd
    Contains various keymaps.

/lib/modules/'kernel-version'
    The home of all the kernel modules. The organisation of files here is
    reasonably clear so no requires no elaboration.

/lib/modules/'kernel-version'/isapnpmap.dep
      has details on ISA based cards, the modules that they require and
    various other attributes.

/lib/modules/'kernel-version'/modules.dep
      lists all modules dependencies. This file can be updated using the
    depmod command.

/lib/modules/'kernel-version'/pcimap
    is the PCI equivalent of the /lib/modules/'kernel-version'/isapnpmap.dep
    file.

/lib/modules/'kernel-version'/usbmap
    is the USB equivalent of the /lib/modules/'kernel-version'/isapnpmap.dep
    file.

/lib/oss
      All OSS (Open Sound System) files are installed here by default.

/lib/security
    PAM library files.



The FSSTND states that the /lib directory contains those shared library
images needed to boot the system and run the commands in the root filesystem,
ie. by binaries in /bin and /sbin.

Shared libraries that are only necessary for binaries in /usr (such as any
X Window binaries) must not be in /lib. Only the shared libraries required
to run binaries in /bin and /sbin may be here. In particular, the library
libm.so.* may also be placed in /usr/lib if it is not required by anything
in /bin or /sbin.

At least one of each of the following filename patterns are required (they
may be files, or symbolic links):

libc.so.* The dynamically-linked C library (optional)
ld*       The execution time linker/loader (optional)

If a C preprocessor is installed, /lib/cpp must be a reference to it, for
historical reasons. The usual placement of this binary is /usr/bin/cpp.

The following directories, or symbolic links to directories, must be in
/lib, if the corresponding subsystem is installed:

modules   Loadable kernel modules (optional)

/lib<qual> : Alternate format essential shared libraries (optional)

There may be one or more variants of the /lib directory on systems which
support more than one binary format requiring separate libraries.

This is commonly used for 64-bit or 32-bit support on systems which support
multiple binary formats, but require libraries of the same name. In this
case, /lib32 and /lib64 might be the library directories, and /lib a symlink
to one of them.

If one or more of these directories exist, the requirements for their contents
are the same as the normal /lib directory, except that /lib<qual>/cpp is
not required.

/lib<qual>/cpp is still permitted: this allows the case where /lib and
/lib<qual> are the same (one is a symbolic link to the other).
-----------------------------------------------------------------------------

1.10. /lost+found

  As was explained earlier during the overview of the FSSTND, Linux should
always go through a proper shutdown. Sometimes your system might crash or a
power failure might take the machine down. Either way, at the next boot, a
lengthy filesystem check (the speed of this check is dependent on the type of
filesystem that you actually use. ie. ext3 is faster than ext2 because it is
a journalled filesystem) using fsck will be done. Fsck will go through the
system and try to recover any corrupt files that it finds. The result of this
recovery operation will be placed in this directory. The files recovered are
not likely to be complete or make much sense but there always is a chance
that something worthwhile is recovered. Each partition has its own lost+found
directory. If you find files in there, try to move them back to their
original location. If you find something like a broken symbolic link to
'file', you have to reinstall the file/s from the corresponding RPM, since
your file system got damaged so badly that the files were mutilated beyond
recognition. Below is an example of a /lost+found directory. As you can see,
the vast majority of files contained here are in actual fact sockets. As for
the rest of the other files they were found to be damaged system files and
personal files. These files were not able to be recovered.


      total 368
      -rw-r--r-- 1 root root 110891 Oct 5 14:14 #388200
      -rw-r--r-- 1 root root 215 Oct 5 14:14 #388201
      -rw-r--r-- 1 root root 110303 Oct 6 23:09 #388813
      -rw-r--r-- 1 root root 141 Oct 6 23:09 #388814
      -rw-r--r-- 1 root root 110604 Oct 6 23:09 #388815a
      -rw-r--r-- 1 root root 194 Oct 6 23:09 #388816
      srwxr-xr-x 1 root root 0 Oct 6 13:00 #51430
      srwxr-xr-x 1 root root 0 Oct 6 00:23 #51433
      -rw------- 1 root root 63 Oct 6 00:23 #51434
      srwxr-xr-x 1 root root 0 Oct 6 13:00 #51436
      srwxrwxrwx 1 root root 0 Oct 6 00:23 #51437
      srwx------ 1 root root 0 Oct 6 00:23 #51438
      -rw------- 1 root root 63 Oct 6 13:00 #51439
      srwxrwxrwx 1 root root 0 Oct 6 13:00 #51440
      srwx------ 1 root root 0 Oct 6 13:00 #51442
      -rw------- 1 root root 63 Oct 6 23:09 #51443
      srwx------ 1 root root 0 Oct 6 10:40 #51445
      srwxrwxrwx 1 root root 0 Oct 6 23:09 #51446
      srwx------ 1 root root 0 Oct 6 23:09 #51448

-----------------------------------------------------------------------------

1.11. /media

 Amid much controversy and consternation on the part of system and network
administrators a directory containing mount points for removable media has
now been created. Funnily enough, it has been named /media.


This directory contains subdirectories which are used as mount points for
removable media such as floppy disks, cdroms and zip disks.

The motivation for the creation of this directory has been that historically
there have been a number of other different places used to mount removable
media such as /cdrom, /mnt or /mnt/cdrom. Placing the mount points for all
removable media directly in the root directory would potentially result in
a large number of extra directories in /. Although the use of subdirectories
in /mnt as a mount point has recently been common, it conflicts with a much
older tradition of using /mnt directly as a temporary mount point.

The following directories, or symbolic links to directories, must be in /media,
if the corresponding subsystem is installed:

floppy     Floppy drive (optional)
cdrom      CD-ROM drive (optional)
cdrecorder CD writer (optional)
zip        Zip drive (optional)

On systems where more than one device exists for mounting a certain type of
media, mount directories can be created by appending a digit to the name of
those available above starting with '0', but the unqualified name must also
exist.

A compliant implementation with two CDROM drives might have /media/cdrom0
and /media/cdrom1 with /media/cdrom a symlink to either of these.

 Please see the section on the /mnt directory to achieve a better
understanding of the process on mounting and unmounting filesystems.
-----------------------------------------------------------------------------

1.12. /mnt

This is a generic mount point under which you mount your filesystems or
devices. Mounting is the process by which you make a filesystem available to
the system. After mounting your files will be accessible under the
mount-point. This directory usually contains mount points or sub-directories
where you mount your floppy and your CD. You can also create additional
mount-points here if you wish. Standard mount points would include /mnt/cdrom
and /mnt/floppy. There is no limitation to creating a mount-point anywhere on
your system but by convention and for sheer practicality do not litter your
file system with mount-points. It should be noted that some distributions
like Debian allocate /floppy and /cdrom as mount points while Redhat and
Mandrake puts them in /mnt/floppy and /mnt/cdrom respectively.

  However, it should be noted that as of FSSTND version 2.3 the purpose of
this directory has changed.


  This directory is provided so that the system administrator may temporarily
  mount a filesystem as needed. The content of this directory is a local issue
  and should not affect the manner in which any program is run.

  This directory must not be used by installation programs: a suitable temporary
  directory not in use by the system must be used instead.

-----------------------------------------------------------------------------

1.12.1. Mounting and unmounting

Before one can use a filesystem, it has to be mounted. The operating system
then does various bookkeeping things to make sure that everything works.
Since all files in UNIX are in a single directory tree, the mount operation
will make it look like the contents of the new filesystem are the contents of
an existing subdirectory in some already mounted filesystem.

The mounts could be done as in the following example:

  $ mount /dev/hda2 /home
  $ mount /dev/hda3 /usr
  $

The mount command takes two arguments. The first one is the device file
corresponding to the disk or partition containing the filesystem. The second
one is the directory below which it will be mounted. After these commands the
contents of the two filesystems look just like the contents of the /home and
/usr directories, respectively. One would then say that ``/dev/hda2 is
mounted on /home'', and similarly for /usr. To look at either filesystem, one
would look at the contents of the directory on which it has been mounted,
just as if it were any other directory. Note the difference between the
device file, /dev/hda2, and the mounted-on directory, /home. The device file
gives access to the raw contents of the disk, the mounted-on directory gives
access to the files on the disk. The mounted-on directory is called the mount
point.

Linux supports many filesystem types. mount tries to guess the type of the
filesystem. You can also use the -t fstype option to specify the type
directly; this is sometimes necessary, since the heuristics mount uses do not
always work. For example, to mount an MS-DOS floppy, you could use the
following command:
  $ mount -t msdos /dev/fd0 /floppy
   $


The mounted-on directory need not be empty, although it must exist. Any files
in it, however, will be inaccessible by name while the filesystem is mounted.
(Any files that have already been opened will still be accessible. Files that
have hard links from other directories can be accessed using those names.)
There is no harm done with this, and it can even be useful. For instance,
some people like to have /tmp and /var/tmp synonymous, and make /tmp be a
symbolic link to /var/tmp. When the system is booted, before the /var
filesystem is mounted, a /var/tmp directory residing on the root filesystem
is used instead. When /var is mounted, it will make the /var/tmp directory on
the root filesystem inaccessible. If /var/tmp didn't exist on the root
filesystem, it would be impossible to use temporary files before mounting /
var.

If you don't intend to write anything to the filesystem, use the -r switch
for mount to do a read-only mount. This will make the kernel stop any
attempts at writing to the filesystem, and will also stop the kernel from
updating file access times in the inodes. Read-only mounts are necessary for
unwritable media, e.g., CD-ROMs.

The alert reader has already noticed a slight logistical problem. How is the
first filesystem (called the root filesystem, because it contains the root
directory) mounted, since it obviously can't be mounted on another
filesystem? Well, the answer is that it is done by magic.

For more information, see the kernel source or the Kernel Hackers' Guide.

The root filesystem is magically mounted at boot time, and one can rely on it
to always be mounted. If the root filesystem can't be mounted, the system
does not boot. The name of the filesystem that is magically mounted as root
is either compiled into the kernel, or set using LILO or rdev.

The root filesystem is usually first mounted read-only. The startup scripts
will then run fsck to verify its validity, and if there are no problems, they
will re-mount it so that writes will also be allowed. fsck must not be run on
a mounted filesystem, since any changes to the filesystem while fsck is
running will cause trouble. Since the root filesystem is mounted read-only
while it is being checked, fsck can fix any problems without worry, since the
remount operation will flush any metadata that the filesystem keeps in
memory.

On many systems there are other filesystems that should also be mounted
automatically at boot time. These are specified in the /etc/fstab file; see
the fstab man page for details on the format. The details of exactly when the
extra filesystems are mounted depend on many factors, and can be configured
by each administrator if need be.

When a filesystem no longer needs to be mounted, it can be unmounted with
