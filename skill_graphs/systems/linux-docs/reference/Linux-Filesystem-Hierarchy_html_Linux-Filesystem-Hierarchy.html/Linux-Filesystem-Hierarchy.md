#  Linux Filesystem Hierarchy
## Version 0.65
###  Binh Nguyen

`<`

2004-07-30

This document outlines the set of requirements and guidelines for file and directory placement under the Linux operating system according to those of the FSSTND v2.3 final (January 29, 2004) and also its actual implementation on an arbitrary system. It is meant to be accessible to all members of the Linux community, be distribution independent and is intended to discuss the impact of the FSSTND and how it has managed to increase the efficiency of support interoperability of applications, system administration tools, development tools, and scripts as well as greater uniformity of documentation for these systems.
Copyright 2003 Binh Nguyen
Trademarks are owned by their owners.
Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.2; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled "GNU Free Documentation License".
* * *

**Table of Contents**


[Source and pre-formatted versions available](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#AEN18)


1. [Linux Filesystem Hierarchy](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#AEN23)


1.1. [Foreward](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#Foreward)


1.2. [The Root Directory](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#The-Root-Directory)


1.3. [/bin](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#bin)


1.4. [/boot](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#boot)


1.5. [/dev](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#dev)


1.6. [/etc](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#etc)


1.7. [/home](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#home)


1.8. [/initrd](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#initrd)


1.9. [/lib](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#lib)


1.10. [/lost+found](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#lostfound)


1.11. [/media](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#media)


1.12. [/mnt](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#mnt)


1.13. [/opt](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#opt)


1.14. [/proc](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#proc)


1.15. [/root](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#root)


1.16. [/sbin](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#sbin)


1.17. [/usr](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#usr)


1.18. [/var](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#var)


1.19. [/srv](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#srv)


1.20. [/tmp](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#tmp)


[Glossary](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#Glossary)


A. [UNIX System V Signals](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#Signals)


B. [Sources](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#Sources)


C. [About the Author](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#About-the-Author)


D. [Contributors](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#Contributors)


E. [Disclaimer](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#Disclaimer)


F. [Donations](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#Donations)


G. [Feedback](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#Feedback)


H. [GNU Free Documentation License](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl)


H.1. [PREAMBLE](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl-0)


H.2. [APPLICABILITY AND DEFINITIONS](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl-1)


H.3. [VERBATIM COPYING](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl-2)


H.4. [COPYING IN QUANTITY](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl-3)


H.5. [MODIFICATIONS](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl-4)


H.6. [COMBINING DOCUMENTS](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl-5)


H.7. [COLLECTIONS OF DOCUMENTS](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl-6)


H.8. [AGGREGATION WITH INDEPENDENT WORKS](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl-7)


H.9. [TRANSLATION](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl-8)


H.10. [TERMINATION](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl-9)


H.11. [FUTURE REVISIONS OF THIS LICENSE](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl-10)


H.12. [ADDENDUM: How to use this License for your documents](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/Linux-Filesystem-Hierarchy.html#gfdl-addendum)

* * *
