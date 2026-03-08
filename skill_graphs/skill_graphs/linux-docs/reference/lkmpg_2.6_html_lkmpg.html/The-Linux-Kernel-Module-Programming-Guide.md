#  The Linux Kernel Module Programming Guide
Peter Jay Salzman
Michael Burian
Ori Pomerantz

Copyright © 2001 Peter Jay Salzman
2007-05-18 ver 2.6.4

The Linux Kernel Module Programming Guide is a free book; you may reproduce and/or modify it under the terms of the Open Software License, version 1.1. You can obtain a copy of this license at
This book is distributed in the hope it will be useful, but without any warranty, without even the implied warranty of merchantability or fitness for a particular purpose.
The author encourages wide distribution of this book for personal or commercial use, provided the above copyright notice remains intact and the method adheres to the provisions of the Open Software License. In summary, you may copy and distribute this book free of charge or for a profit. No explicit permission is required from the author for reproduction of this book in any medium, physical or electronic.
Derivative works and translations of this document must be placed under the Open Software License, and the original copyright notice must remain intact. If you have contributed new material to this book, you must make the material and source code available for your revisions. Please make revisions and updates available directly to the document maintainer, Peter Jay Salzman `<`. This will allow for the merging of updates and provide consistent revisions to the Linux community.
If you publish or distribute this book commercially, donations, royalties, and/or printed copies are greatly appreciated by the author and the [Linux Documentation Project](http://www.tldp.org) (LDP). Contributing in this way shows your support for free software and the LDP. If you have questions or comments, please contact the address above.
* * *

**Table of Contents**


[Foreword](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN25)


1. [Authorship](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN27)


2. [Versioning and Notes](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN30)


3. [Acknowledgements](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN35)


1. [Introduction](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN38)


1.1. [What Is A Kernel Module?](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN40)


1.2. [How Do Modules Get Into The Kernel?](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN44)


2. [Hello World](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN119)


2.1. [Hello, World (part 1): The Simplest Module](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN121)


2.2. [Compiling Kernel Modules](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN181)


2.3. [Hello World (part 2)](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#HELLO2)


2.4. [Hello World (part 3): The `__init` and `__exit` Macros](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN245)


2.5. [Hello World (part 4): Licensing and Module Documentation](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN279)


2.6. [Passing Command Line Arguments to a Module](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN323)


2.7. [Modules Spanning Multiple Files](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN351)


2.8. [Building modules for a precompiled kernel](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN380)


3. [Preliminaries](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN425)


3.1. [Modules vs Programs](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN427)


4. [Character Device Files](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN567)


4.1. [Character Device Drivers](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN569)


5. [The /proc File System](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN708)


5.1. [The /proc File System](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN710)


5.2. [Read and Write a /proc File](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN769)


5.3. [Manage /proc file with standard filesystem](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN810)


5.4. [Manage /proc file with seq_file](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN861)


6. [Using /proc For Input](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN885)


6.1. [TODO: Write a chapter about sysfs](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN887)


7. [Talking To Device Files](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN890)


7.1. [Talking to Device Files (writes and IOCTLs)](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN892)


8. [System Calls](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN976)


8.1. [System Calls](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN978)


9. [Blocking Processes](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1050)


9.1. [Blocking Processes](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1052)


10. [Replacing Printks](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1159)


10.1. [Replacing `printk`](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1161)


10.2. [Flashing keyboard LEDs](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1194)


11. [Scheduling Tasks](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1209)


11.1. [Scheduling Tasks](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1211)


12. [Interrupt Handlers](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#INTERRUPTHANDLERS)


12.1. [Interrupt Handlers](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1256)


13. [Symmetric Multi Processing](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1324)


13.1. [Symmetrical Multi-Processing](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1326)


14. [Common Pitfalls](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1350)


14.1. [Common Pitfalls](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1352)


A. [Changes: 2.0 To 2.2](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1387)


A.1. [Changes between 2.4 and 2.6](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1389)


B. [Where To Go From Here](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1403)


B.1. [Where From Here?](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1405)


[Index](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#DOC-INDEX)


**List of Figures**


5-1. [How seq_file works](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN868)


**List of Examples**


2-1. [hello-1.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN128)


2-2. [Makefile for a basic kernel module](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN189)


2-3. [hello-2.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN232)


2-4. [Makefile for both our modules](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN237)


2-5. [hello-3.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN275)


2-6. [hello-4.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN319)


2-7. [hello-5.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN345)


2-8. [start.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN361)


2-9. [stop.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN369)


2-10. [Makefile](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN374)


4-1. [chardev.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN687)


5-1. [procfs1.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN765)


5-2. [procfs2.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN806)


5-3. [procfs3.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN853)


5-4. [procfs4.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN872)


7-1. [chardev.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN951)


7-2. [chardev.h](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN959)


7-3. [ioctl.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN972)


8-1. [syscall.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1046)


9-1. [sleep.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1151)


9-2. [cat_noblock.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1155)


10-1. [print_string.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1190)


10-2. [kbleds.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1201)


11-1. [sched.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1250)


12-1. [intrpt.c](https://tldp.org/LDP/lkmpg/2.6/html/lkmpg.html#AEN1320)

* * *
