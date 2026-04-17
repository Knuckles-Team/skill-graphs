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
  * [ALFS Home](https://www.linuxfromscratch.org/alfs/index.html)
  * [News](https://www.linuxfromscratch.org/alfs/news.html)
  * [Download](https://www.linuxfromscratch.org/alfs/download.html)
  * [Documentation](https://www.linuxfromscratch.org/alfs/documentation.html)
  * [Support](https://www.linuxfromscratch.org/support.html)
  * [Mailing Lists](https://www.linuxfromscratch.org/mail.html)
  * [Wiki](https://wiki.linuxfromscratch.org/alfs)
  * [Contribute](https://www.linuxfromscratch.org/contribute.html)
  * [Website Mirrors](https://www.linuxfromscratch.org/mirrors.html)


# What is Automated Linux From Scratch?
Automated Linux From Scratch (ALFS) started as an ambitious project with the aim of building a set of packages automatically. Due to lack of manpower, it evolved towards an automation of the LFS book, mainly used by book editors to assess the quality of the instructions. It is also available for all to help building their LFS system. It also allows building packages from the BLFS book, but that needs some manual intervention.
## Why would I want to use ALFS?
After having gone through the LFS and BLFS books more than 2 or 3 times, you will quickly appreciate the ability to automate the task of compiling the software you want for your systems.
The goal of ALFS is to _automate_ the process of creating an LFS system. It seeks to follow the book as closely as possible by directly extracting instructions from the XML sources. This is the reason why it may also be used as a test of the current book instructions.
## How is ALFS implemented?
The official implementation of ALFS is called _jhalfs_. It was originally created by Jeremy Huntwork, then developed and maintained by Manuel Canales Esparcia, George Boudreau, Thomas Pegg, and Pierre Labastie. It has become a light-weight, practical method of automating an LFS build. It is a Bash shell script that makes use of Git and xsltproc to first download the XML sources of the Linux From Scratch book and then extract any necessary commands, placing them into executable shell scripts. If you do not already have the necessary source packages in place on your system, jhalfs can fetch them. Finally, jhalfs generates a Makefile which will control the execution of the shell scripts, allowing for recovery if the build should encounter an error. A framework to use package management has been added by Pierre Labastie.
Due to a lack of developers, jhalfs is maintained as a rolling release. It can be obtained by cloning the git repository:
git clone https://git.linuxfromscratch.org/jhalfs.git jhalfs
An extension of ALFS aimed at automating the building of packages in the BLFS book is now included in jhalfs. It still needs editing some scripts (about 1%), mainly when the book layout diverges from standard, but works rather well and most of the packages can be built automatically.
## History
Before jhalfs, an implementation named nALFS was developed. A more ambitious project, named simply alfs was designed around 2004, but was never pushed to completion.
### nALFS
The first ALFS implementation was nALFS by Neven Has. nALFS was a small program written in C. It first parsed an XML profile that contained information concerning the LFS build process into a series of internal commands. It could then execute these at your discretion, thus automating the compilation of LFS.
### alfs
There were many in-depth features that had been requested for ALFS implementations. Because of this, development had been slated for an entirely new build tool which would have been called alfs. Eventually, the ease of use of jhalfs ultimately pushed development of alfs to the bottom of the stack.
## Who's who:
  * Project Leader and Developer/Maintainer: Pierre Labastie
  * Former Maintainer: Thomas Pegg
  * Former Developers(jhalfs): Jeremy Huntwork, George Boudreau
  * Former Developer(jhalfs, blfs tools): Manuel Canales Esparcia



© 1998-2026 Gerard Beekmans. Website design by Jeremy Huntwork & Matthew Burgess.
