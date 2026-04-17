#  Linux Filesystem Hierarchy
## Version 0.65
###  Binh Nguyen

`<`

2004-07-30

This document outlines the set of requirements and guidelines for file and directory placement under the Linux operating system according to those of the FSSTND v2.3 final (January 29, 2004) and also its actual implementation on an arbitrary system. It is meant to be accessible to all members of the Linux community, be distribution independent and is intended to discuss the impact of the FSSTND and how it has managed to increase the efficiency of support interoperability of applications, system administration tools, development tools, and scripts as well as greater uniformity of documentation for these systems.
[Legal Notice](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/ln14.html)
* * *

**Table of Contents**


[Source and pre-formatted versions available](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/f18.html)


1. [Linux Filesystem Hierarchy](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/c23.html)


1.1. [Foreward](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/foreward.html)


1.2. [The Root Directory](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/the-root-directory.html)


1.3. [/bin](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/bin.html)


1.4. [/boot](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/boot.html)


1.5. [/dev](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/dev.html)


1.6. [/etc](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/etc.html)


1.7. [/home](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/home.html)


1.8. [/initrd](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/initrd.html)


1.9. [/lib](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/lib.html)


1.10. [/lost+found](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/lostfound.html)


1.11. [/media](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/media.html)


1.12. [/mnt](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/mnt.html)


1.13. [/opt](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/opt.html)


1.14. [/proc](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/proc.html)


1.15. [/root](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/root.html)


1.16. [/sbin](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/sbin.html)


1.17. [/usr](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/usr.html)


1.18. [/var](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/var.html)


1.19. [/srv](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/srv.html)


1.20. [/tmp](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/tmp.html)


[Glossary](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/glossary.html)


A. [UNIX System V Signals](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/signals.html)


B. [Sources](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/sources.html)


C. [About the Author](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/about-the-author.html)


D. [Contributors](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/contributors.html)


E. [Disclaimer](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/disclaimer.html)


F. [Donations](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/donations.html)


G. [Feedback](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/feedback.html)


H. [GNU Free Documentation License](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl.html)


H.1. [PREAMBLE](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl-0.html)


H.2. [APPLICABILITY AND DEFINITIONS](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl-1.html)


H.3. [VERBATIM COPYING](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl-2.html)


H.4. [COPYING IN QUANTITY](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl-3.html)


H.5. [MODIFICATIONS](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl-4.html)


H.6. [COMBINING DOCUMENTS](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl-5.html)


H.7. [COLLECTIONS OF DOCUMENTS](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl-6.html)


H.8. [AGGREGATION WITH INDEPENDENT WORKS](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl-7.html)


H.9. [TRANSLATION](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl-8.html)


H.10. [TERMINATION](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl-9.html)


H.11. [FUTURE REVISIONS OF THIS LICENSE](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl-10.html)


H.12. [ADDENDUM: How to use this License for your documents](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/gfdl-addendum.html)

* * *
|  | [Next](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/f18.html)
---|---|---
|  | Source and pre-formatted versions available
