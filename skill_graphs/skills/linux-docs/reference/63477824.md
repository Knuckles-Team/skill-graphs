#  The Linux Kernel Module Programming Guide
Peter Jay Salzman
Ori Pomerantz

Copyright © 2001 Peter Jay Salzman
2003-04-04 ver 2.4.0

The Linux Kernel Module Programming Guide is a free book; you may reproduce and/or modify it under the terms of the Open Software License, version 1.1. You can obtain a copy of this license at
This book is distributed in the hope it will be useful, but without any warranty, without even the implied warranty of merchantability or fitness for a particular purpose.
The author encourages wide distribution of this book for personal or commercial use, provided the above copyright notice remains intact and the method adheres to the provisions of the Open Software License. In summary, you may copy and distribute this book free of charge or for a profit. No explicit permission is required from the author for reproduction of this book in any medium, physical or electronic.
Derivative works and translations of this document must be placed under the Open Software License, and the original copyright notice must remain intact. If you have contributed new material to this book, you must make the material and source code available for your revisions. Please make revisions and updates available directly to the document maintainer, Peter Jay Salzman `<`. This will allow for the merging of updates and provide consistent revisions to the Linux community.
If you publish or distribute this book commercially, donations, royalties, and/or printed copies are greatly appreciated by the author and the [Linux Documentation Project](http://www.tldp.org) (LDP). Contributing in this way shows your support for free software and the LDP. If you have questions or comments, please contact the address above.
* * *

**Table of Contents**


[Foreword](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN23)


1. [Acknowledgements](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN25)


2. [Authorship And Copyright](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN34)


3. [Nota Bene](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN37)


1. [Introduction](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN43)


1.1. [What Is A Kernel Module?](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN45)


1.2. [How Do Modules Get Into The Kernel?](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN49)


2. [Hello World](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN147)


2.1. [Hello, World (part 1): The Simplest Module](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN149)


2.2. [Compiling Kernel Modules](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN208)


2.3. [Hello World (part 2)](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#HELLO2)


2.4. [Hello World (part 3): The `__init` and `__exit` Macros](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN281)


2.5. [Hello World (part 4): Licensing and Module Documentation](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN321)


2.6. [Passing Command Line Arguments to a Module](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN354)


2.7. [Modules Spanning Multiple Files](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN385)


3. [Preliminaries](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN435)


3.1. [Modules vs Programs](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN437)


4. [Character Device Files](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN577)


4.1. [Character Device Drivers](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN579)


5. [The /proc File System](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN722)


5.1. [The /proc File System](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN724)


6. [Using /proc For Input](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN768)


6.1. [Using /proc For Input](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN770)


7. [Talking To Device Files](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN854)


7.1. [Talking to Device Files (writes and IOCTLs)}](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN856)


8. [System Calls](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN937)


8.1. [System Calls](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN939)


9. [Blocking Processes](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1012)


9.1. [Blocking Processes](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1014)


10. [Replacing Printks](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1115)


10.1. [Replacing `printk`](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1117)


11. [Scheduling Tasks](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1149)


11.1. [Scheduling Tasks](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1151)


12. [Interrupt Handlers](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#INTERRUPTHANDLERS)


12.1. [Interrupt Handlers](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1210)


13. [Symmetric Multi Processing](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1294)


13.1. [Symmetrical Multi-Processing](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1296)


14. [Common Pitfalls](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1320)


14.1. [Common Pitfalls](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1322)


A. [Changes: 2.0 To 2.2](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1357)


A.1. [Changes between 2.0 and 2.2](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1359)


B. [Where To Go From Here](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1486)


B.1. [Where From Here?](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1488)


[Index](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#DOC-INDEX)


**List of Examples**


2-1. [hello-1.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN156)


2-2. [Makefile for a basic kernel module](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN246)


2-3. [hello-2.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN272)


2-4. [Makefile for both our modules](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN276)


2-5. [hello-3.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN311)


2-6. [hello-4.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN351)


2-7. [hello-5.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN380)


2-8. [start.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN421)


2-9. [stop.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN428)


2-10. [Makefile for a multi-filed module](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN432)


4-1. [chardev.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN700)


4-2. [some title](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN717)


5-1. [procfs.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN765)


6-1. [procfs.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN851)


7-1. [chardev.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN915)


7-2. [chardev.h](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN922)


7-3. [ioctl.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN934)


8-1. [syscall.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1009)


9-1. [sleep.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1112)


10-1. [print_string.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1146)


11-1. [sched.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1205)


12-1. [intrpt.c](https://tldp.org/LDP/lkmpg/2.4/html/lkmpg.html#AEN1291)

* * *
