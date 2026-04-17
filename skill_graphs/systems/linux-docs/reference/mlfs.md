[ ![Linux From Scratch | Your Distro, Your Rules](https://www.linuxfromscratch.org/images/linux-from-scratch.png) ](https://www.linuxfromscratch.org/index.html)
Web LFS
  * [Patches](https://www.linuxfromscratch.org/patches/)
  * [Hints](https://www.linuxfromscratch.org/hints/)
  * [SLFS](https://www.linuxfromscratch.org/slfs/)
  * [GLFS](https://www.linuxfromscratch.org/glfs/)
  * [MLFS](https://www.linuxfromscratch.org/mlfs/)
  * [ALFS](https://www.linuxfromscratch.org/alfs/)
  * [BLFS](https://www.linuxfromscratch.org/blfs/)
  * [LFS](https://www.linuxfromscratch.org/lfs/)


  * [Home](https://www.linuxfromscratch.org/)
  * [MLFS Home](https://www.linuxfromscratch.org/mlfs/index.html)
  * [News](https://www.linuxfromscratch.org/mlfs/news.html)
  * [Download](https://www.linuxfromscratch.org/mlfs/download.html)
  * [Support](https://www.linuxfromscratch.org/support.html)
  * [Mailing Lists](https://www.linuxfromscratch.org/mail.html)


# What is Multilib Linux From Scratch?
Multilib Linux From Scratch is a variant of the [LFS book](https://www.linuxfromscratch.org/lfs/view/development/) which sets up an LFS system that is able to build and execute 32-bit binaries.
Most x86 systems in the hands of users today are 64-bit, but 32-bit systems are still in use and in some cases are actively produced. They used to be a lot more common and had a lot of software made for them. From this, there are certain cases where a project is only for 32-bit or requires that the operating system can run 32-bit software.
The problem is that 32-bit software is different from 64-bit software. Differences range from using different registers, different kernel codes, among more. With some help from the kernel, most 64-bit CPUs can emulate 32-bit software. However, it is likely that the 32-bit software depends on more software in that same format. That's the biggest issue that MLFS solves. The book arms the system with the libraries necessary for basic 32-bit emulation alongside the tools that are necessary to build them.
Furthermore, this book covers the installation of x32-bit libraries. x32-bit software operates with 64-bit instructions but only with a 32-bit address space. Typically, only software that is open source can target x32-bit. Most proprietary software never bother with it.
## Why would I want an MLFS system?
There are various situations in which you would need the ability to run 32-bit software. For instance, some software may be proprietary and is intended to run on the most systems possible. In this case, 32-bit can be seen as a baseline, which 64-bit CPUs can emulate. Other times, the target software is very old and the developers stopped targeting x86 in the way that they used to. 32-bit software thus ends up as an artifact of its time but may be necessary nonetheless as it may be the only viable driver for a given device. Other instances can be a result of virtualization. [GLFS](https://www.linuxfromscratch.org/glfs) and [SLFS](https://www.linuxfromscratch.org/slfs) have packages that fall into those camps.
## Read the Book Online
MLFS has different versions that include different bit sizes and what LFS version it lines up with.
### Current Stable
This is the stable release of MLFS that is known to work with BLFS, GLFS, and SLFS 13.0 with identical instructions to LFS-13.0.
  * [MLFS-13.0 with 32-bit and x32-bit](https://www.linuxfromscratch.org/mlfs/view/13.0/)
  * [MLFS-13.0 with 32-bit](https://www.linuxfromscratch.org/mlfs/view/13.0-m32/)
  * [MLFS-13.0 with x32-bit](https://www.linuxfromscratch.org/mlfs/view/13.0-mx32/)


### Development
  * [MLFS development with 32-bit and x32-bit](https://www.linuxfromscratch.org/mlfs/view/dev/)
  * [MLFS development with 32-bit](https://www.linuxfromscratch.org/mlfs/view/dev-m32/)
  * [MLFS development with x32-bit](https://www.linuxfromscratch.org/mlfs/view/dev-mx32/)


## Going Beyond MLFS
While MLFS is a variant of LFS, there isn't a variant of BLFS that is as big as BLFS with multilib instructions; however, a good substitute is [GLFS](https://www.linuxfromscratch.org/glfs) which builds a good amount of 32-bit libraries and enables 32-bit support in various toolchains like LLVM and Rustc. Take and leave according to what you need.
Something worth keeping in mind is BLFS, GLFS, and SLFS are actively tested with systems built with MLFS. Compatibility is strong. Using MLFS instead of LFS is safe and is tested at the same time the rest of the LFS books are.
## Thanks to
  * Editor: Zeckma
  * Previous editor: Thomas Trepl
  * Previous MLFS contributor: DJ Lucas
  * Active MLFS contributor: Douglas Reno
  * Active MLFS contributor: Xi Ruoyao
  * William Feely who started a
  * Plus many more.



© 1998-2026 Gerard Beekmans. Website design by Jeremy Huntwork & Matthew Burgess.
