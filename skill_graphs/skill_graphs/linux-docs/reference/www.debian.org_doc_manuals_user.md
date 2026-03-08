* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch20.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/user/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch1.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-logging-in.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-manpages.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-files.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-shells.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch6.html) ] [ [7](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch7.html) ] [ [8](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-editors.html) ] [ [9](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch9.html) ] [ [10](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch10.html) ] [ [11](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch11.html) ] [ [12](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch12.html) ] [ [13](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch13.html) ] [ [14](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch14.html) ] [ [15](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch15.html) ] [ [16](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch16.html) ] [ [17](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-xwin.html) ] [ [18](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch18.html) ] [ [19](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch19.html) ] [ [20](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch20.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch1.html) ]
* * *
#  Debian User Reference Manual (Obsolete Documentation)

* * *
##  Abstract
The Debian User Reference Manual covers everything a user should know about a Debian GNU/Linux system from a user's view point. It fills the gap between the Debian Tutorial and the manual and info pages of individual packages.
* * *
##  Copyright Notice
Copyright © 1997 Ardo van Rangelrooij, 1998 Oliver Elphick
This manual is free software; you may redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version.
This is distributed in the hope that it will be useful, but _without any warranty_ ; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License with your Debian GNU/Linux system, in /usr/doc/copyright/GPL, or with the `debiandoc-sgml` source package as the file COPYING. If not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
* * *
##  Contents
  * [1 Introduction](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch1.html)
  * [2 Overview of a Debian GNU/Linux System](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-logging-in.html)
  * [3 Documentation](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-manpages.html)
  * [4 Files and File Systems](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-files.html)
    * [4.1 Basic Concepts](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-files.html#s-files-basics)
    * [4.2 Basic file commands - a tutorial](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-files.html#s-files-commands)
    * [4.3 What files are on my Debian system? Where should I put my own files?](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-files.html#s-files-structure)
    * [4.4 File ownership and permissions](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-files.html#s-files-permissions)
    * [4.5 Filesystems](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-files.html#s-files-filesystems)
    * [4.6 How to access particular devices (including hard disk partitions and floppy drives)](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-files.html#s-files-devices)
    * [4.7 Miscellaneous topics](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-files.html#s-files-misc)
    * [4.8 Advanced Topics](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-files.html#s-files-advanced)
  * [5 Shells](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-shells.html)
  * [6 Basic Commands and Tools](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch6.html)
    * [6.1 What this chapter covers](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch6.html#s6.1)
    * [6.2 Running commands](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch6.html#s6.2)
    * [6.3 Regular expressions](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch6.html#s-regexp)
  * [7 Advanced Commands and Tools](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch7.html)
  * [8 Text Editing](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-editors.html)
  * [9 Text Processing](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch9.html)
    * [9.1 What this chapter covers](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch9.html#s9.1)
    * [9.2 Text processing](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch9.html#s9.2)
    * [9.3 LaTeX](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch9.html#s9.3)
  * [10 Programming](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch10.html)
    * [10.1 What this chapter covers](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch10.html#s10.1)
  * [11 Science](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch11.html)
    * [11.1 What this chapter covers](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch11.html#s11.1)
    * [11.2 Plotting](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch11.html#s11.2)
    * [11.3 Combining diagrams](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch11.html#s11.3)
  * [12 Games](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch12.html)
  * [13 Sound](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch13.html)
  * [14 Image Manipulation](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch14.html)
  * [15 Networking](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch15.html)
  * [16 Databases](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch16.html)
    * [16.1 What this chapter covers](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch16.html#s16.1)
  * [17 X Windows](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-xwin.html)
  * [18 X Windows Managers](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch18.html)
  * [19 X Windows Applications](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch19.html)
  * [20 Index](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch20.html)


* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch20.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/user/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch1.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-logging-in.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-manpages.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-files.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-shells.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch6.html) ] [ [7](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch7.html) ] [ [8](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-editors.html) ] [ [9](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch9.html) ] [ [10](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch10.html) ] [ [11](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch11.html) ] [ [12](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch12.html) ] [ [13](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch13.html) ] [ [14](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch14.html) ] [ [15](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch15.html) ] [ [16](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch16.html) ] [ [17](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch-xwin.html) ] [ [18](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch18.html) ] [ [19](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch19.html) ] [ [20](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch20.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/user/ch1.html) ]
* * *
Debian User Reference Manual (Obsolete Documentation)
version 0.1, 29 December 2009

Ardo van Rangelrooij
Jason D. Waterman
Thalia L. Hooker
Havoc Pennington
Oliver Elphick - Maintainer
Bruce Every
Karl-Heinz Zimmer
Andreas Franzen


* * *
