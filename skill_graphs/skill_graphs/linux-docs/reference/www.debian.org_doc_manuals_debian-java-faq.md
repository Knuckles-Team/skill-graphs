* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch10.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-debian-java-lenny.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-debian-java-squeeze.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch4.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch5.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch6.html) ] [ [7](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-browser-java.html) ] [ [8](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch8.html) ] [ [9](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch9.html) ] [ [10](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch10.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html) ]
* * *
#  Debian Java FAQ.

* * *
##  Abstract
Answers to Frequently Asked Questions on Debian and Java (Note: some information is not up-to-date). Any changes/corrections to this FAQ are appreciated. Please send them to the Debian Bug Tracking System as described in [Sending bugs on this FAQ, Section 1.3](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html#s-bugs).
* * *
##  Copyright Notice
This document may be freely redistributed or modified in any form provided your changes are clearly documented. This document may be redistributed for fee or free, and may be modified (including translation from one type of media or file format to another or from one spoken language to another) provided that all changes from the original are clearly marked as such.
* * *
##  Contents
  * [1 Introduction](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html)
    * [1.1 Introduction to this FAQ](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html#s1.1)
    * [1.2 Location of this FAQ](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html#s1.2)
    * [1.3 Sending bugs on this FAQ](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html#s-bugs)
    * [1.4 What is Java?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html#s1.4)
    * [1.5 Where can I ask questions about Java on Debian?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html#s1.5)
    * [1.6 Complementary information](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html#s-moreinfo)
    * [1.7 Uncovered issues](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html#s-pending)
  * [2 Status of Java in Debian GNU/Linux 5.0 (Lenny)](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-debian-java-lenny.html)
    * [2.1 What is new in Lenny?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-debian-java-lenny.html#s2.1)
  * [3 Status of Java in Debian Squeeze](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-debian-java-squeeze.html)
    * [3.1 What is new in Squeeze?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-debian-java-squeeze.html#s3.1)
    * [3.2 What are the most important changes in the Java policy?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-debian-java-squeeze.html#s3.2)
    * [3.3 What have been removed in Squeeze?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-debian-java-squeeze.html#s3.3)
  * [4 Java Development](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch4.html)
    * [4.1 What full-fledged Java development platforms are available in Debian?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch4.html#s4.1)
    * [4.2 What free platforms are there and how can I contribute?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch4.html#s-free)
    * [4.3 Questions on platforms and license concerns](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch4.html#s-license-concerns)
    * [4.4 Making Debian packages for Java programs.](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch4.html#s4.4)
  * [5 Managing Java (for users and administrators)](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch5.html)
  * [6 Java Virtual Machines (JVM)](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch6.html)
    * [6.1 What JVMs are available in Debian?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch6.html#s6.1)
    * [6.2 What Java Compilers are available in Debian?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch6.html#s6.2)
    * [6.3 What API do these JVMs provide?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch6.html#s6.3)
    * [6.4 Are there known problems?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch6.html#s6.4)
    * [6.5 Do I need a JVM to run a Java program in Debian?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch6.html#s6.5)
  * [7 Java Plugins for Browsers](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-browser-java.html)
  * [8 Java Servlets](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch8.html)
    * [8.1 How can I make Java servlets work?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch8.html#s8.1)
  * [9 Java Policy](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch9.html)
    * [9.1 Is there a Java policy for Debian?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch9.html#s9.1)
    * [9.2 Are there holes in the Java Policy?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch9.html#s9.2)
  * [10 Other Java alternatives for Debian](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch10.html)
    * [10.1 Java programs not yet available on Debian](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch10.html#s10.1)


* * *
[ [previous](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch10.html) ] [ [Contents](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/#contents) ] [ [1](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html) ] [ [2](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-debian-java-lenny.html) ] [ [3](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-debian-java-squeeze.html) ] [ [4](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch4.html) ] [ [5](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch5.html) ] [ [6](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch6.html) ] [ [7](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch-browser-java.html) ] [ [8](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch8.html) ] [ [9](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch9.html) ] [ [10](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch10.html) ] [ [next](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-java-faq/ch1.html) ]
* * *
Debian Java FAQ.
$Revision: 7831 $, $Date: 2010-12-04 20:17:15 +0000 (Sat, 04 Dec 2010) $

Torsten Werner
Niels Thykier
Javier Fern�ndez-Sanguino Pe�a


* * *
