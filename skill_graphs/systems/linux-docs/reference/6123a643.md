# LFS News

LFS-13.0 Release
     _Bruce Dubbs - 2026/03/05_
The Linux From Scratch community announces the release of LFS Version 13.0.
Major changes include toolchain updates to binutils-2.46 and glibc-2.43. In total, 36 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 6.18.10.
Packages that have security updates include: expat, glibc, openssl, Python, vim, and zlib. See the [Security Advisories](https://www.linuxfromscratch.org/lfs/advisories/12.4.html) for details.
Overall there have been 100 commits to LFS since the previous stable version of the book.
You can read the systemd version of the book online at [LFS-systemd](https://www.linuxfromscratch.org/lfs/view/13.0-systemd/), or [download-systemd](https://www.linuxfromscratch.org/lfs/downloads/13.0-systemd/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS-13.0-rc1 Release
     _Bruce Dubbs - 2026/02/14_
The Linux From Scratch community announces the release of LFS Version 13.0-rc1. It is a preliminary release of LFS-13.0.
Major changes include toolchain updates to binutils-2.46.0 and glibc-2.43. In total, 36 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 6.18.10.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
# LFS News

LFS-11.0-rc3 Release
     _Bruce Dubbs - 2021/08/25_
The Linux From Scratch community announces the release of LFS Version 11.0-rc3. It is a preliminary release of LFS-11.0.
This version of the Linux From Scratch book has been released due to a critical security vulnerability in openssl. This vulnerability has been fixed in LFS 11.0-rc3 by updating to the latest version: openssl-1.1.1l (version 1.1.1 lower case L). Usage of LFS 11.0-rc1 or LFS 11.0-rc2 is deemed unsafe and insecure.
In addition to the above, we took the opportunity to update several other packages from the recent -rc releases to the latest stable versions: e2fsprogs, meson, the linux kernel, util-linux, and libcap.
This version of the Linux From Scratch book has changed from a split-/usr to a merged-/usr configuration. This brings LFS into a similar configuration to most recent distributions.
Major changes include toolchain updates to binutils-2.37 and glibc-2.34. In total, 38 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 5.13.12.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/11.0-rc3/), or [download](https://www.linuxfromscratch.org/lfs/downloads/11.0-rc3/) to read locally.
You can read the systemd version of the book online at [LFS-systemd-rc3](https://www.linuxfromscratch.org/lfs/view/11.0-systemd-rc3/), or [download-systemd-rc3](https://www.linuxfromscratch.org/lfs/downloads/11.0-systemd-rc3/) to read locally.
Please direct any comments about this release to the LFS development team at
# LFS News

LFS-11.0-rc2 Release
     _Douglas Reno - 2021/08/20_
The Linux From Scratch community announces the release of LFS Version 11.0-rc2. It is a preliminary release of LFS-11.0.
This version of the Linux From Scratch book has been released due to a critical security vulnerability in glibc-2.34. This vulnerability has been fixed in LFS 11.0-rc2 via a simple sed in Chapter 8. Usage of LFS 11.0-rc1 is deemed unsafe and insecure.
This version of the Linux From Scratch book has changed from a split-/usr to a merged-/usr configuration. This brings LFS into a similar configuration to most recent distributions.
Major changes include toolchain updates to binutils-2.37 and glibc-2.34. In total, 38 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 5.13.10.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/11.0-rc2/), or [download](https://www.linuxfromscratch.org/lfs/downloads/11.0-rc2/) to read locally.
You can read the systemd version of the book online at [LFS-systemd-rc2](https://www.linuxfromscratch.org/lfs/view/11.0-systemd-rc2/), or [download-systemd-rc2](https://www.linuxfromscratch.org/lfs/downloads/11.0-systemd-rc2/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS-11.0-rc1 Release
     _Douglas Reno - 2021/08/15_
The Linux From Scratch community announces the release of LFS Version 11.0-rc1. It is a preliminary release of LFS-11.0.
This version of the Linux From Scratch book has changed from a split-/usr to a merged-/usr configuration. This brings LFS into a similar configuration to most recent distributions.
Major changes include toolchain updates to binutils-2.37 and glibc-2.34. In total, 38 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 5.13.10.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/11.0-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/11.0-rc1/) to read locally.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/11.0-systemd-rc1/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/11.0-systemd-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS Stable Version 10.1 Release
     _Bruce Dubbs - 2021/03/01_
The Linux From Scratch community announces the release of LFS Version 10.1. Major changes include toolchain updates to glibc-2.33, and binutils-2.36.1. In total, 40 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 5.10.17.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/10.1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/10.1/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd](https://www.linuxfromscratch.org/lfs/view/10.1-systemd/), or [download-systemd](https://www.linuxfromscratch.org/lfs/downloads/10.1-systemd/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS-10.1-rc1 Release
     _Bruce Dubbs - 2021/02/19_
The Linux From Scratch community announces the release of LFS Version 10.1-rc1. It is a preliminary release of LFS-10.1. Major changes include toolchain updates to binutils-2.36.1 and glibc-2.33. In total, 40 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 5.10.17.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/10.1-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/10.1-rc1/) to read locally.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/10.1-systemd-rc1/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/10.1-systemd-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS Stable Version 10.0 Release
     _Bruce Dubbs - 2020/09/01_
The Linux From Scratch community announces the release of LFS Version 10.0.
This version of the book has undergone a major reorganization. It uses enhanced cross-compilation techniques and an environment isolated from the host system to build tools for the final system. This reduces both the chance for changing the the host system and the potential of the host system influencing the LFS build process.
Major package updates include toolchain versions glibc-2.32, gccc-10.2.0, and binutils-2.35. In total, 37 packages were updated since the last release. The Linux kernel has also been updated to version 5.8.3.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/10.0/), or [download](https://www.linuxfromscratch.org/lfs/downloads/10.0/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd](https://www.linuxfromscratch.org/lfs/view/10.0-systemd/), or [download-systemd](https://www.linuxfromscratch.org/lfs/downloads/10.0-systemd/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS-10.0-rc1 Release
     _Bruce Dubbs - 2020/08/15_
The Linux From Scratch community announces the release of LFS Version 10.0-rc1. It is a preliminary release of LFS-10.0. This version of the book has undergone a major reorganization. It uses enhanced cross-compilation techniques and an environment isolated from the host system to build tools for the final system. This reduces both the chance for changing the the host system and the potential of the host system influencing the LFS build process.
Other major changes include toolchain updates to binutils-2.35, gcc-10.2.0, and glibc-2.32. In total, 37 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 5.8.1.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/10.0-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/10.0-rc1/) to read locally.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/10.0-systemd-rc1/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/10.0-systemd-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS Stable Version 9.1 Release
     _Bruce Dubbs - 2020/03/01_
The Linux From Scratch community announces the release of LFS Version 9.1. Major changes include toolchain updates to glibc-2.31, and binutils-2.34. A new package, zstd-1.4.4, has also been added. In total, 35 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 5.5.3.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/9.1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/9.1/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd](https://www.linuxfromscratch.org/lfs/view/9.1-systemd/), or [download-systemd](https://www.linuxfromscratch.org/lfs/downloads/9.1-systemd/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 9.1-rc1 Release
     _Bruce Dubbs - 2020/02/14_
The Linux From Scratch community announces the release of LFS Version 9.1-rc1. It is a preliminary release of LFS-9.1. Major changes include toolchain updates to binutils-2.34 and glibc-2.31. In total, 36 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 5.5.3.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/9.1-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/9.1-rc1/) to read locally.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/9.1-systemd-rc1/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/9.1-systemd-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS Stable Version 9.0 Release
     _Bruce Dubbs - 2019/09/01_
The Linux From Scratch community announces the release of LFS Version 9.0. Major changes include toolchain updates to glibc-2.30, and gcc-9.2.0. In total, 33 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 5.2.8.
Note that the major version of LFS has changed to 9. This has been done to keep LFS and BLFS version numbers synchronized. The BLFS System V version has added the elogind package which now allowed Gnome to be added.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/9.0/), or [download](https://www.linuxfromscratch.org/lfs/downloads/9.0/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd](https://www.linuxfromscratch.org/lfs/view/9.0-systemd/), or [download-systemd](https://www.linuxfromscratch.org/lfs/downloads/9.0-systemd/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 9.0-rc1 Release
     _Bruce Dubbs - 2019/08/15_
The Linux From Scratch community announces the release of LFS Version 9.0-rc1. It is a preliminary release of LFS-9.0. Major changes include toolchain updates to gcc-9.2.0 and glibc-2.30. In total, 33 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 5.2.8.
Note that the major version of LFS has changed to 9. This has been done to keep LFS and BLFS version numbers synchronized. The BLFS System V version has added the elogind package which now allows Gnome to be built in the new environment.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/9.0-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/9.0-rc1/) to read locally.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/9.0-systemd-rc1/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/9.0-systemd-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS Stable Version 8.4 Release
     _Bruce Dubbs - 2019/03/01_
The Linux From Scratch community announces the release of LFS Version 8.4. Major changes include toolchain updates to glibc-2.29, binutils-2.32, and bash-5.0. In total, 34 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.20.12.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/8.4/), or [download](https://www.linuxfromscratch.org/lfs/downloads/8.4/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd](https://www.linuxfromscratch.org/lfs/view/8.4-systemd/), or [download-systemd](https://www.linuxfromscratch.org/lfs/downloads/8.4-systemd/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 8.4-rc1 Release
     _Bruce Dubbs - 2019/02/15_
The Linux From Scratch community announces the release of LFS Version 8.4-rc1. It is a preliminary release of LFS-8.4. Major changes include toolchain updates to glibc-2.29 and binutils-2.32. In total, 34 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.20.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/8.4-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/8.4-rc1/) to read locally.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/8.4-systemd-rc1/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/8.4-systemd-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS Stable Version 8.3 Release
     _Bruce Dubbs - 2018/09/01_
The Linux From Scratch community announces the release of LFS Version 8.3. Major changes include toolchain updates to glibc-2.28, binutils-2.31.1, and and gcc-8.2.0. In total, 31 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.18.5.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/8.3/), or [download](https://www.linuxfromscratch.org/lfs/downloads/8.3/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd](https://www.linuxfromscratch.org/lfs/view/8.3-systemd/), or [download-systemd](https://www.linuxfromscratch.org/lfs/downloads/8.3-systemd/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 8.3-rc2 Release
     _Bruce Dubbs - 2018/08/16_
The Linux From Scratch community announces the release of LFS Version 8.3-rc2. This is an update to 8.3-rc1 due to security related releases in the kernel and openssl. At the same time updates to expat and iproute2 that were released after the previous release candidate are also included.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/8.3-rc2/), or [download](https://www.linuxfromscratch.org/lfs/downloads/8.3-rc2/) to read locally.
You can read the systemd version of the book online at [LFS-systemd-rc2](https://www.linuxfromscratch.org/lfs/view/8.3-systemd-rc2/), or [download-systemd-rc2](https://www.linuxfromscratch.org/lfs/downloads/8.3-systemd-rc2/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 8.3-rc1 Release
     _Bruce Dubbs - 2018/08/13_
The Linux From Scratch community announces the release of LFS Version 8.3-rc1. It is a preliminary release of LFS-8.3. Major changes include toolchain updates to glibc-2.28, binutils-2.31.1, and and gcc-8.2.0. In total, 31 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.18.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/8.3-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/8.3-rc1/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/8.3-systemd-rc1/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/8.3-systemd-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS Stable Version 8.2 Release
     _Bruce Dubbs - 2018/03/02_
The Linux From Scratch community announces the release of LFS Version 8.2. Major changes include toolchain updates to glibc-2.27, binutils-2.30, and and gcc-7.3.0. In total, 34 packages were updated since the last release. In addition five new packages have been moved to the base LFS book from BLFS: libffi, openssl, Python3, ninja, and meson. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.15.3.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/8.2/), or [download](https://www.linuxfromscratch.org/lfs/downloads/8.2/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd](https://www.linuxfromscratch.org/lfs/view/8.2-systemd/), or [download-systemd](https://www.linuxfromscratch.org/lfs/downloads/8.2-systemd/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 8.2-rc1 Release
     _Bruce Dubbs - 2018/02/16_
The Linux From Scratch community announces the release of LFS Version 8.2-rc1. It is a preliminary release of LFS-8.2. Major changes include toolchain updates to glibc-2.27, binutils-2.30, and and gcc-7.0.0. In total, 34 packages were updated since the last release. In addition five new packages have been moved ot the base LFS book from BLFS: libffi, openssl, Python3, ninja, and meson. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.15.3.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/8.2-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/8.2-rc1/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/8.2-systemd-rc1/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/8.2-systemd-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS Stable Version 8.1 Release
     _Bruce Dubbs - 2017/09/01_
The Linux From Scratch community announces the release of LFS Version 8.1. Major changes include toolchain updates to glibc-2.26, binutils-2.29, and and gcc-7.2.0. In total, 32 packages were updated since the last stable release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.12.7.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/8.1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/8.1/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd](https://www.linuxfromscratch.org/lfs/view/8.1-systemd/), or [download-systemd](https://www.linuxfromscratch.org/lfs/downloads/8.1-systemd/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 8.1-rc2 Release
     _Bruce Dubbs - 2017/08/18_
The Linux From Scratch community announces the release of LFS Version 8.1-rc2. It differs from version 8.1-rc1 only in the build options given to glibc in Chapter 6.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/8.1-rc2/), or [download](https://www.linuxfromscratch.org/lfs/downloads/8.1-rc2/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/8.1-systemd-rc2/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/8.1-systemd-rc2/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 8.1-rc1 Release
     _Bruce Dubbs - 2017/08/16_
The Linux From Scratch community announces the release of LFS Version 8.1-rc1. It is a preliminary release of LFS-8.1. Major changes include toolchain updates to glibc-2.25, binutils-2.29, and and gcc-7.2.0. In total, 32 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.12.7.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/8.1-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/8.1-rc1/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/8.1-systemd-rc1/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/8.1-systemd-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS Stable Version 8.0 Release
     _Bruce Dubbs - 2017/02/25_
The Linux From Scratch community announces the release of LFS Version 8.0. Major changes include toolchain updates to glibc-2.25 and and gcc-6.3.0. In total, 28 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.9.9.
This is a new major version of LFS. The change to 8.0 is due to the removal of the symbolic link from /lib to /lib64 and the complete removal of /usr/lib64. An additional feature is that the gold linker (/usr/bin/ld.gold) is now available although it is not the default linker.
This is a coordinated release and both System V and systemd versions of the book have been updated.
You can read the [System V book online](https://www.linuxfromscratch.org/lfs/view/8.0/), or go to the [System V download](https://www.linuxfromscratch.org/lfs/downloads/8.0/) site to read locally.
You can read the [systemd book online](https://www.linuxfromscratch.org/lfs/view/8.0-systemd/), or go to the [systemd download](https://www.linuxfromscratch.org/lfs/downloads/8.0-systemd/) site to read locally.
Please direct any comments about this release to the LFS development team at

LFS 8.0-rc1 Release
     _Bruce Dubbs - 2017/02/14_
The Linux From Scratch community announces the release of LFS Version 8.0-rc1. It is a preliminary release of LFS-8.0. Major changes include toolchain updates to glibc-2.25 and and gcc-6.3.0. In total, 28 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.9.9.
This is a new major version of LFS. The change to 8.0 is due to the removal of the symbolic link from /lib to /lib64 and the complete removal of /usr/lib64. An additional feature is that the gold linker (/usr/bin/ld.gold) is now available although it is not the default linker.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/8.0-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/8.0-rc1/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/8.0-systemd-rc1/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/8.0-systemd-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS Stable Version 7.10 Release
     _Bruce Dubbs - 2016/09/07_
The Linux From Scratch community announces the release of LFS Version 7.10. It is a major release with toolchain updates to glibc-2.24, binutils-2.27, and gcc-6.2.0. In total, 29 packages were updated and changes to text have been made throughout the book.
This is a coordinated release and both System V and systemd versions of the book have been updated.
You can read the [System V book online](https://www.linuxfromscratch.org/lfs/view/7.10/), or go to the [System V download](https://www.linuxfromscratch.org/lfs/downloads/7.10/) site to read locally.
You can read the [systemd book online](https://www.linuxfromscratch.org/lfs/view/7.10-systemd/), or go to the [systemd download](https://www.linuxfromscratch.org/lfs/downloads/7.10-systemd/) site to read locally.
Please direct any comments about this release to the LFS development team at

LFS 7.10-rc1 Release
     _Bruce Dubbs - 2016/08/24_
The Linux From Scratch community announces the release of LFS Version 7.10-rc1. It is a preliminary release of LFS-7.10. Major changes include toolchain updates to binutils-2.27, glibc-2.24, and gcc-6.2.0. In total, 29 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.7.2.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/7.10-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/7.10-rc1/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/7.10-systemd-rc1/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/7.10-systemd-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS Stable Systemd Version 7.9 Release
     _Bruce Dubbs - 2016/03/08_
The Linux From Scratch community announces the release of LFS Stable Systemd Version 7.9. It is a major release with toolchain updates to glibc-2.23, binutils-2.26, gcc-5.3.0, and systemd-229. In total, 26 packages were updated and changes to text have been made throughout the book.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/7.9-systemd/), or [download](https://www.linuxfromscratch.org/lfs/downloads/7.9-systemd/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 7.9 Stable Release
     _Bruce Dubbs - 2016/03/08_
The Linux From Scratch community announces the release of LFS Stable Version 7.9. It is a major release with toolchain updates to glibc-2.23, binutils-2.26, and gcc-5.3.0. In total, 25 packages were updated and changes to text have been made throughout the book.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/7.9/), or [download](https://www.linuxfromscratch.org/lfs/downloads/7.9/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 7.9-rc2 Release
     _Bruce Dubbs - 2016/02/19_
The Linux From Scratch community announces the release of LFS Version 7.9-rc2. It is a preliminary release of LFS-7.9. Major changes include toolchain updates to binutils-2.26, glibc-2.23, and gcc-5.3.0. In total, 25 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.4.2.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/7.9-rc2/), or [download](https://www.linuxfromscratch.org/lfs/downloads/7.9-rc2/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd-rc2](https://www.linuxfromscratch.org/lfs/view/7.9-systemd-rc2/), or [download-systemd-rc2](https://www.linuxfromscratch.org/lfs/downloads/7.9-systemd-rc2/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 7.9-rc1 Release
     _Bruce Dubbs - 2016/02/14_
The Linux From Scratch community announces the release of LFS Version 7.9-rc1. It is a preliminary release of LFS-7.9. Major changes include toolchain updates to binutils-2.26 and gcc-5.3.0. In total, 24 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.4.1.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/7.9-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/7.9-rc1/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initialization and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd-rc1](https://www.linuxfromscratch.org/lfs/view/7.9-systemd-rc1/), or [download-systemd-rc1](https://www.linuxfromscratch.org/lfs/downloads/7.9-systemd-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 7.8 Stable Release
     _Bruce Dubbs - 2015/10/01_
The Linux From Scratch community announces the release of LFS Stable Version 7.8. It is a major release with toolchain updates to glibc-2.22, binutils-2.25.1, and gcc-5.2.0. In total, 30 packages were updated and changes to bootscripts and text have been made throughout the book.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/7.8/), or [download](https://www.linuxfromscratch.org/lfs/downloads/7.8/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also being released. This package implements the newer systemd style of system initializaion and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd](https://www.linuxfromscratch.org/lfs/view/7.8-systemd/), or [download-systemd](https://www.linuxfromscratch.org/lfs/downloads/7.8-systemd/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 7.8-rc1 Release
     _Bruce Dubbs - 2015/09/07_
The Linux From Scratch community announces the release of LFS Version 7.8-rc1. It is a preliminary release of LFS-7.8. Major changes include toolchain updates to binutils-2.25.1, glibc-2.22, and gcc-5.2.0. In total, 30 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 4.2.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/7.8-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/7.8-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 7.7 Stable Release
     _Bruce Dubbs - 2015/03/06_
The Linux From Scratch community announces the release of LFS Stable Version 7.7. It is a major release with toolchain updates to glibc-2.21 and gcc-4.9.2. In total, 30 packages were updated and changes to bootscripts and text have been made throughout the book.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/7.7/), or [download](https://www.linuxfromscratch.org/lfs/downloads/7.7/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 7.7-rc1 Release
     _Bruce Dubbs - 2015/02/19_
The Linux From Scratch community announces the release of LFS Version 7.7-rc1. It is a preliminary release of LFS-7.7. Major changes include toolchain updates to binutils-2.25, glibc-2.21, and gcc-4.9.2. In total, 30 packages were updated since the last release. Changes to the text have also been made throughout the book. The Linux kernel has also been updated to version 3.19.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/7.7-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/7.7-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 7.6 Stable Release
     _Bruce Dubbs - 2014/09/23_
The Linux From Scratch community announces the release of LFS Stable Version 7.6. It is a major release with toolchain updates to glibc-2.20 and gcc-4.9.1. In total, 26 packages were updated and 8 packages added from LFS-7.5 and changes to bootscripts and text have been made throughout the book.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/7.6/), or [download](https://www.linuxfromscratch.org/lfs/downloads/7.6/) to read locally.
In coordination with this release, a new version of LFS using the systemd package is also bint released. This package implements the newer systemd style of system initializaion and control and is consistent with LFS in most packages.
You can read the systemd version of the book online at [LFS-systemd](https://www.linuxfromscratch.org/lfs/view/7.6-systemd/), or [download-systemd](https://www.linuxfromscratch.org/lfs/downloads/7.6-systemd/) to read locally.
Please direct any comments about this release to the LFS development team at

LFS 7.6-rc1 Release
     _Bruce Dubbs - 2014/09/08_
The Linux From Scratch community announces the release of LFS Version 7.6-rc1. It is a preliminary release of LFS-7.6 Major changes include toolchain updates to glibc-2.20 and gcc-4.9.1. Another major change is the use of the eudev package as a replacement for extracting udev from the systemd source code. In total, 26 packages were updated and 8 packages added since the last release. Changes to the text has been made throughout the book. The linux kernel has also been updated to version 3.16.2.
We encourage all users to read through this release of the book and test the instructions so that we can make the final release as good as possible.
You can read the book [online](https://www.linuxfromscratch.org/lfs/view/7.6-rc1/), or [download](https://www.linuxfromscratch.org/lfs/downloads/7.6-rc1/) to read locally.
Please direct any comments about this release to the LFS development team at

© 1998-2026 Gerard Beekmans. Website design by Jeremy Huntwork & Matthew Burgess.
