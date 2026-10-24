* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-novas.en.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch1.en.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-basico.en.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-helpers.en.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-search.en.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-sourcehandling.en.html) ] [ [7](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-erros.en.html) ] [ [8](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-distros.en.html) ] [ [9](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-agradecimentos.en.html) ] [ [10](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-novas.en.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch1.en.html) ]
* * *
#  APT HOWTO (Obsolete Documentation)

* * *
##  Abstract
This document intends to provide the user with a good understanding of the workings of the Debian package management utility, APT. Its goal is to make life easier for new Debian users and to help those who wish to deepen their understanding of the administration of this system. It was created for the Debian project in order to help improve the support available for users of this distribution.
* * *
##  Copyright Notice
Copyright © 2001, 2002, 2003, 2004 Gustavo Noronha Silva
This manual is free software; you may redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version.
This is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU General Public License for more details.
A copy of the GNU General Public License is available as /usr/share/common-licenses/GPL in the Debian GNU/Linux distribution or on the World Wide Web at the GNU General Public Licence. You can also obtain it by writing to the Free Software Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
* * *
##  Contents
  * [1 Introduction](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch1.en.html)
  * [2 Basic Configuration](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-basico.en.html)
    * [2.1 The /etc/apt/sources.list file](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-basico.en.html#s-sources.list)
    * [2.2 How to use APT locally](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-basico.en.html#s-dpkg-scanpackages)
    * [2.3 Deciding which mirror is the best to include in the sources.list file: netselect, netselect-apt](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-basico.en.html#s-netselect)
    * [2.4 Adding a CD-ROM to the sources.list file](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-basico.en.html#s-cdrom)
  * [3 Managing packages](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html)
    * [3.1 Updating the list of available packages](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html#s-update)
    * [3.2 Installing packages](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html#s-install)
    * [3.3 Removing packages](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html#s-remove)
    * [3.4 Upgrading packages](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html#s-upgrade)
    * [3.5 Upgrading to a new release](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html#s-dist-upgrade)
    * [3.6 Removing unused package files: apt-get clean and autoclean](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html#s-clean)
    * [3.7 Using APT with dselect](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html#s-dselect-upgrade)
    * [3.8 How to keep a mixed system](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html#s-default-version)
    * [3.9 How to upgrade packages from specific versions of Debian](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html#s-apt-show-versions)
    * [3.10 How to keep specific versions of packages installed (complex)](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html#s-pin)
  * [4 Very useful helpers](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-helpers.en.html)
    * [4.1 How to install locally compiled packages: equivs](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-helpers.en.html#s-equivs)
    * [4.2 Removing unused locale files: localepurge](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-helpers.en.html#s-localepurge)
    * [4.3 How to know what packages may be upgraded](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-helpers.en.html#s-helper-show-versions)
  * [5 Getting information about packages.](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-search.en.html)
    * [5.1 Discovering package names](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-search.en.html#s-cache)
    * [5.2 Using dpkg to find package names](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-search.en.html#s-dpkg-search)
    * [5.3 How to install packages "on demand"](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-search.en.html#s-auto-apt)
    * [5.4 How to discover to which package a file belongs](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-search.en.html#s-apt-file)
    * [5.5 How to keep informed about the changes in the packages.](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-search.en.html#s-apt-listchanges)
  * [6 Working with source packages](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-sourcehandling.en.html)
    * [6.1 Downloading source packages](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-sourcehandling.en.html#s-source)
    * [6.2 Packages needed for compiling a source package](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-sourcehandling.en.html#s-build-dep)
  * [7 How to deal with errors](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-erros.en.html)
    * [7.1 Common errors](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-erros.en.html#s-erros-comuns)
    * [7.2 Where can I find help?](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-erros.en.html#s-help)
  * [8 What distributions support APT?](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-distros.en.html)
  * [9 Credits](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-agradecimentos.en.html)
  * [10 New versions of this tutorial](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-novas.en.html)


* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-novas.en.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch1.en.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-basico.en.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-apt-get.en.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-helpers.en.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-search.en.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-sourcehandling.en.html) ] [ [7](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-erros.en.html) ] [ [8](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-distros.en.html) ] [ [9](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-agradecimentos.en.html) ] [ [10](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch-novas.en.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/apt-howto/ch1.en.html) ]
* * *
APT HOWTO (Obsolete Documentation)
1.8.11 - August 2005

Gustavo Noronha Silva


* * *
