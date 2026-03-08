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
  * [SLFS Home](https://www.linuxfromscratch.org/slfs/index.html)
  * [News](https://www.linuxfromscratch.org/slfs/news.html)
  * [Download](https://www.linuxfromscratch.org/slfs/download.html)
  * [Support](https://www.linuxfromscratch.org/slfs/view/dev/introduction/askhelp.html)
  * [Advisories](https://www.linuxfromscratch.org/slfs/advisories.html)


# What is Supplemental Linux From Scratch?
Supplemental Linux From Scratch aims to supplement an LFS installation and supports LFS, MLFS, BLFS, and GLFS. In essence, SLFS is a sort of BLFS 2, but doesn't include any of the pages from BLFS, except for some cases where a package needs to be re-installed for compatibility.
The focus of SLFS is generalized and contains a wide array of packages to install from, such as general monitoring utilities like htop or BTOP++ or fetch programs like fastfetch, to video game emulators like Dolphin or Mupen64Plus, graphical environments like Hyprland and CDE, multimedia libraries that enhance existing packages in BLFS (FFmpeg and MLT) like Rubberband and LADSPA-SDK, and support for binaries and containers like Fuse2 and Flatpak. This list isn't exaughstive.
As the focus of SLFS is similar to BLFS, it also exists to offload any potential BLFS package additions to reduce burden on maintainers of BLFS.
Since BLFS provides such a large base of packages, SLFS externally links to a given page if a package calls for a dependency in BLFS. At other times, the links will point to within the book or GLFS.
## Why would I want a SLFS system?
BLFS provides a lot of packages that can get users to either 100% of 80% of what they need from a system. The problem is the remaining percentage of packages that may have complicated installation instructions or just takes too long to do manually. SLFS helps bridge the gap and gets users closer to that 100%.
## What can I do with my SLFS system?
You will be able to use various system monitoring utilities, fetch programs, a YouTube video downloading tool, SDL3, various terminal emulators, application launchers, screenshot tools, wallpapers selectors, OBS-Studio, IMEs, various graphical environments like Hyprland, CDE, and Wayfire, various computer and video game emulators, a Minecraft launcher, SVR4-style tooling, Flatpak, and enable libvpl and Intel-MediaSDK support in various packages.
## Read the Book Online
SLFS has different versions that line up with LFS/MLFS+BLFS+GLFS releases. In the past, SLFS had support for both SysVinit and Systemd, but now only Systemd is supported. The past versions exist as historical and educational material.
### Current Stable
These are the current stable versions of SLFS that are known to work with an LFS/MLFS, BLFS, and GLFS stable platform.
  * [SLFS stable, uses BLFS and GLFS stable links](https://www.linuxfromscratch.org/slfs/view/stable/)


### Development
This is SLFS in its current development state. A lot of effort is made to ensure that the development version is as stable as can. However, there can still be problems that can occur. In the past, this was the only way to read the book online without grabbing a copy or rendering the book yourself. Because of that, stability was and still is a major concern. Now, everyone has more options.
  * [SLFS development, uses BLFS and GLFS development links](https://www.linuxfromscratch.org/slfs/view/dev/)


### Other versions
If you want to see older versions, you can browse all releases [here](https://www.linuxfromscratch.org/slfs/view/).
## Thanks to
The [SLFS contributors](https://www.linuxfromscratch.org/slfs/view/dev/introduction/credits.html).


© 1998-2026 Gerard Beekmans. Website design by Jeremy Huntwork & Matthew Burgess.
