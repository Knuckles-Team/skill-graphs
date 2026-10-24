* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ap-latex-enc.en.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-intro.en.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-auto-config.en.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-FAQ.en.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-about.en.html) ] [ [A](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ap-latex-enc.en.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-intro.en.html) ]
* * *
#  Debian Euro HOWTO (Obsolete Documentation)

* * *
##  Copyright Notice
Copyright © 2001, 2002, 2003 Javier Fern�ndez-Sanguino Pe�a.
This document is distributed under the terms of the GNU Public License available at
* * *
##  Contents
  * [1 Introduction](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-intro.en.html)
    * [1.1 Why euro support?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-intro.en.html#s1.1)
    * [1.2 What is the euro symbol?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-intro.en.html#s1.2)
    * [1.3 Why all this fuss for just one character?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-intro.en.html#s1.3)
    * [1.4 Standards](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-intro.en.html#s1.4)
    * [1.5 Is Debian euro-ready?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-intro.en.html#s1.5)
  * [2 Automatic configuration](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-auto-config.en.html)
    * [2.1 The language-env package](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-auto-config.en.html#s2.1)
    * [2.2 The euro-support package](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-auto-config.en.html#s2.2)
      * [2.2.1 The euro-test program](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-auto-config.en.html#s2.2.1)
    * [2.3 The user-euro-XXX packages](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-auto-config.en.html#s2.3)
  * [3 Configuring euro support](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html)
    * [3.1 Initial considerations](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html#s3.1)
    * [3.2 Localisation issues](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html#s-localisation)
      * [3.2.1 Locales in Debian 3.0](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html#s3.2.1)
      * [3.2.2 Locales in Debian 2.2](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html#s3.2.2)
    * [3.3 Configuring the Console](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html#s3.3)
      * [3.3.1 Configuring the console keyboard](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html#s3.3.1)
      * [3.3.2 How the keyboard is loaded in Debian](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html#s3.3.2)
      * [3.3.3 Configuring the console fonts](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html#s3.3.3)
    * [3.4 Configuring the X environment](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html#s3.4)
      * [3.4.1 Keyboard configuration](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html#s3.4.1)
      * [3.4.2 Font configuration](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html#s-xfree86-fonts)
  * [4 Euro support in applications](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html)
    * [4.1 Why talk about applications?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.1)
    * [4.2 Applications with known euro support](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2)
      * [4.2.1 XTerm and its derivatives](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.1)
      * [4.2.2 GNOME Terminal](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.2)
      * [4.2.3 RXVT and its derivatives](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.3)
      * [4.2.4 Eterm](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.4)
      * [4.2.5 gVim](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.5)
      * [4.2.6 Emacs, XEmacs](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.6)
      * [4.2.7 GNOME and GTK+](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.7)
      * [4.2.8 KDE](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.8)
      * [4.2.9 Apache](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.9)
      * [4.2.10 Mutt](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.10)
      * [4.2.11 LaTeX](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.11)
      * [4.2.12 Kword](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.12)
      * [4.2.13 LyX](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.13)
      * [4.2.14 groff (nroff, troff, grotty)](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.14)
      * [4.2.15 Debiandoc-sgml](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.15)
      * [4.2.16 Tgif](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.16)
      * [4.2.17 Perl](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.2.17)
    * [4.3 Applications that do not support the euro character](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html#s4.3)
  * [5 Frequently Asked Questions](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-FAQ.en.html)
    * [5.1 I see a strange character instead of the euro](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-FAQ.en.html#s5.1)
    * [5.2 The euro character gets lost when switching from X to console](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-FAQ.en.html#s5.2)
    * [5.3 How do I see if my keyboard is properly configured?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-FAQ.en.html#s5.3)
    * [5.4 How do I see if I can represent euros properly?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-FAQ.en.html#s5.4)
    * [5.5 I'm using framebuffer, can I represent euros on console?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-FAQ.en.html#s5.5)
    * [5.6 I can input the euro character when running 'euro-test' but this behaviour is lost when X is restarted.](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-FAQ.en.html#s5.6)
    * [5.7 What is the longterm solution for this issue?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-FAQ.en.html#s5.7)
  * [6 About this document](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-about.en.html)
    * [6.1 Why this document?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-about.en.html#s6.1)
    * [6.2 References](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-about.en.html#s-references)
    * [6.3 Changelog/History](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-about.en.html#s6.3)
    * [6.4 Pending issues](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-about.en.html#s-pending)
    * [6.5 Acknowledgements](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-about.en.html#s-acknowledge)
  * [A File definitions for LaTeX](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ap-latex-enc.en.html)
    * [A.1 Latin9.def](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ap-latex-enc.en.html#sA.1)
    * [A.2 latin10.def](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ap-latex-enc.en.html#sA.2)


* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ap-latex-enc.en.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-intro.en.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-auto-config.en.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-configure.en.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-applications.en.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-FAQ.en.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-about.en.html) ] [ [A](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ap-latex-enc.en.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-euro-support/ch-intro.en.html) ]
* * *
Debian Euro HOWTO (Obsolete Documentation)
version 1.2, june 4th 2003.

Javier Fern�ndez-Sanguino Pe�a


* * *
