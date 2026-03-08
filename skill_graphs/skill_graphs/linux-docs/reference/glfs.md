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
  * [GLFS Home](https://www.linuxfromscratch.org/glfs/index.html)
  * [News](https://www.linuxfromscratch.org/glfs/news.html)
  * [Download](https://www.linuxfromscratch.org/glfs/download.html)
  * [Support](https://www.linuxfromscratch.org/glfs/view/dev/introduction/askhelp.html)
  * [Advisories](https://www.linuxfromscratch.org/glfs/advisories.html)


# What is Gaming Linux From Scratch?
Gaming Linux From Scratch, which is based on the [BLFS book](https://www.linuxfromscratch.org/blfs), helps you install gaming support software, like Steam or Wine, on a new x86_64 LFS system.
Depending on what you want to install and its type, you may need Multilib Linux From Scratch (MLFS).
For Steam, it requires 32-bit software as the core of the client is 32-bit. With Wine, it depends on the build type. You can build for pure 64-bit, which is not recommended, and you can do pure 32-bit, which is also not recommended. However, there are two WoW64 modes, an older one and a newer one. WoW64 allows running both 64-bit and 32-bit Windows apps and games on x86_64. The new WoW64 mode doesn't need any Linux 32-bit libraries but needs the i686 MinGW-w64 toolchain, which also doesn't need any Linux 32-bit libraries. The older WoW64 mode on the other hand does require 32-bit libraries.
In cases where 32-bit libraries are needed, [MLFS](https://www.linuxfromscratch.org/mlfs) is a required prerequisuite for this book. [MLFS with 32-bit](https://www.linuxfromscratch.org/mlfs/dev-m32/) is the recommended choice to save disk usage and build times. x32-bit at present time is not very useful for Steam or Wine and seems to have some motions of being phased out. MLFS allows you to build 32-bit apps and libraries, the libraries being the most important part to get Steam and pure 32-bit or older WoW64 for Wine to work.
## Why would I want a GLFS system?
Installing binary-only software on an LFS system is a contentious topic in the LFS community. However, a lot of people still want to play games and use Windows software on their new LFS system. GLFS shows how to go about it, allowing your LFS system to be a viable gaming platform. If you don't care about gaming, this book is probably not for you but it still offers instructions on how to install certain packages for 32-bit on 64-bit. It also offers instructions on how to install libglvnd, NVIDIA, CUDA, MinGW-w64, and Wine which you may still want to use.
## What can I do with my GLFS system?
You will be able to use Steam, play popular games using Vulkan and OpenGL, use the proprietary NVIDIA driver and CUDA if wanted, and run Windows software via Wine. For Windows software (through Steam and Wine), you will be able to convert the Direct3D instructions to Vulkan for optimal performance.
## Read the Book Online
GLFS has different versions that line up with LFS+MLFS+BLFS+SLFS releases. In the past, GLFS had support for both SysVinit and Systemd, but now only Systemd is supported. The past versions exist as historical and educational material.
### Current Stable
These are the current stable versions of GLFS that are known to work with an LFS/MLFS, BLFS, and SLFS stable platform.
  * [GLFS stable, uses MLFS and BLFS stable links](https://www.linuxfromscratch.org/glfs/view/stable/)


### Development
This is GLFS in its current development state. A lot of effort is made to ensure that the development version is as stable as can. However, there can still be problems that can occur. In the past, this was the only way to read the book online without grabbing a copy or rendering the book yourself. Because of that, stability was and still is a major concern. Now, everyone has more options.
  * [GLFS development, uses MLFS and BLFS development links](https://www.linuxfromscratch.org/glfs/view/dev/)


### Other versions
If you want to see older versions, you can browse all releases [here](https://www.linuxfromscratch.org/glfs/view/).
## Thanks to
Douglas Reno, Rahul Chandra, Thomas Trepl, Xi Ruoyao, and the [GLFS contributors](https://www.linuxfromscratch.org/glfs/view/stable/introduction/credits.html)


© 1998-2026 Gerard Beekmans. Website design by Jeremy Huntwork & Matthew Burgess.
