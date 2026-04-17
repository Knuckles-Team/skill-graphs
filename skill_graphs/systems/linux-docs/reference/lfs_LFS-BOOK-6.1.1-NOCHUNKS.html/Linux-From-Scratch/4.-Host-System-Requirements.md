##  4. Host System Requirements
The host must be running at least a 2.6.2 kernel compiled with GCC-3.0 or higher. There are two main reasons for this requirement. First, the Native POSIX Threading Library (NPTL) test suite will segfault if the host's kernel has not been compiled with GCC-3.0 or a later version. Second, the 2.6.2 or later version of the kernel is required for the use of Udev. Udev creates devices dynamically by reading from the `sysfs` file system. However, support for this filesystem has only recently been implemented in most of the kernel drivers. We must be sure that all critical system devices get created properly.
In order to determine whether the host kernel meets the requirements outlined above, run the following command:
```
`cat /proc/version`
```

This will produce output similar to:
```
`Linux version 2.6.2 (user@host) (gcc version 3.4.0) #1
    Tue Apr 20 21:22:18 GMT 2004`
```

If the results of the above command do not state that the host kernel is either 2.6.2 (or later), or that it was not compiled using a GCC-3.0 (or later) compiler, one will need to be installed. There are two methods you can take to solve this. First, see if your Linux vendor provides a 2.6.2 (or later) kernel package. If so, you may wish to install it. If your vendor doesn't offer a 2.6.2 (or later) kernel package, or you would prefer not to install it, then you can compile a 2.6 kernel yourself. Instructions for compiling the kernel and configuring the boot loader (assuming the host uses GRUB) are located in [Chapter 8](https://tldp.org/LDP/lfs/LFS-BOOK-6.1.1-NOCHUNKS.html#chapter-bootable). This second option can also be seen as a gauge of your current Linux skills. If this second requirement is too steep, then the LFS book will not likely be much use to you at this time.
