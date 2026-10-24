#  The Linux Kernel Module Programming Guide
Peter Jay Salzman
Ori Pomerantz

[Copyright](https://tldp.org/LDP/lkmpg/2.4/html/ln14.html) © 2001 Peter Jay Salzman
2003-04-04 ver 2.4.0

* * *

**Table of Contents**


[Foreword](https://tldp.org/LDP/lkmpg/2.4/html/f23.html)


1. [Acknowledgements](https://tldp.org/LDP/lkmpg/2.4/html/x25.html)


2. [Authorship And Copyright](https://tldp.org/LDP/lkmpg/2.4/html/x34.html)


3. [Nota Bene](https://tldp.org/LDP/lkmpg/2.4/html/x37.html)


1. [Introduction](https://tldp.org/LDP/lkmpg/2.4/html/c43.html)


1.1. [What Is A Kernel Module?](https://tldp.org/LDP/lkmpg/2.4/html/x45.html)


1.2. [How Do Modules Get Into The Kernel?](https://tldp.org/LDP/lkmpg/2.4/html/x49.html)


2. [Hello World](https://tldp.org/LDP/lkmpg/2.4/html/c147.html)


2.1. [Hello, World (part 1): The Simplest Module](https://tldp.org/LDP/lkmpg/2.4/html/x149.html)


2.2. [Compiling Kernel Modules](https://tldp.org/LDP/lkmpg/2.4/html/x208.html)


2.3. [Hello World (part 2)](https://tldp.org/LDP/lkmpg/2.4/html/hello2.html)


2.4. [Hello World (part 3): The `__init` and `__exit` Macros](https://tldp.org/LDP/lkmpg/2.4/html/x281.html)


2.5. [Hello World (part 4): Licensing and Module Documentation](https://tldp.org/LDP/lkmpg/2.4/html/x321.html)


2.6. [Passing Command Line Arguments to a Module](https://tldp.org/LDP/lkmpg/2.4/html/x354.html)


2.7. [Modules Spanning Multiple Files](https://tldp.org/LDP/lkmpg/2.4/html/x385.html)


3. [Preliminaries](https://tldp.org/LDP/lkmpg/2.4/html/c435.html)


3.1. [Modules vs Programs](https://tldp.org/LDP/lkmpg/2.4/html/x437.html)


4. [Character Device Files](https://tldp.org/LDP/lkmpg/2.4/html/c577.html)


4.1. [Character Device Drivers](https://tldp.org/LDP/lkmpg/2.4/html/x579.html)


5. [The /proc File System](https://tldp.org/LDP/lkmpg/2.4/html/c722.html)


5.1. [The /proc File System](https://tldp.org/LDP/lkmpg/2.4/html/x724.html)


6. [Using /proc For Input](https://tldp.org/LDP/lkmpg/2.4/html/c768.html)


6.1. [Using /proc For Input](https://tldp.org/LDP/lkmpg/2.4/html/x770.html)


7. [Talking To Device Files](https://tldp.org/LDP/lkmpg/2.4/html/c854.html)


7.1. [Talking to Device Files (writes and IOCTLs)}](https://tldp.org/LDP/lkmpg/2.4/html/x856.html)


8. [System Calls](https://tldp.org/LDP/lkmpg/2.4/html/c937.html)


8.1. [System Calls](https://tldp.org/LDP/lkmpg/2.4/html/x939.html)


9. [Blocking Processes](https://tldp.org/LDP/lkmpg/2.4/html/c1012.html)


9.1. [Blocking Processes](https://tldp.org/LDP/lkmpg/2.4/html/x1014.html)


10. [Replacing Printks](https://tldp.org/LDP/lkmpg/2.4/html/c1115.html)


10.1. [Replacing `printk`](https://tldp.org/LDP/lkmpg/2.4/html/x1117.html)


11. [Scheduling Tasks](https://tldp.org/LDP/lkmpg/2.4/html/c1149.html)


11.1. [Scheduling Tasks](https://tldp.org/LDP/lkmpg/2.4/html/x1151.html)


12. [Interrupt Handlers](https://tldp.org/LDP/lkmpg/2.4/html/interrupthandlers.html)


12.1. [Interrupt Handlers](https://tldp.org/LDP/lkmpg/2.4/html/x1210.html)


13. [Symmetric Multi Processing](https://tldp.org/LDP/lkmpg/2.4/html/c1294.html)


13.1. [Symmetrical Multi-Processing](https://tldp.org/LDP/lkmpg/2.4/html/x1296.html)


14. [Common Pitfalls](https://tldp.org/LDP/lkmpg/2.4/html/c1320.html)


14.1. [Common Pitfalls](https://tldp.org/LDP/lkmpg/2.4/html/x1322.html)


A. [Changes: 2.0 To 2.2](https://tldp.org/LDP/lkmpg/2.4/html/a1357.html)


A.1. [Changes between 2.0 and 2.2](https://tldp.org/LDP/lkmpg/2.4/html/x1359.html)


B. [Where To Go From Here](https://tldp.org/LDP/lkmpg/2.4/html/a1486.html)


B.1. [Where From Here?](https://tldp.org/LDP/lkmpg/2.4/html/x1488.html)


[Index](https://tldp.org/LDP/lkmpg/2.4/html/doc-index.html)


**List of Examples**


2-1. [hello-1.c](https://tldp.org/LDP/lkmpg/2.4/html/x149.html#AEN156)


2-2. [Makefile for a basic kernel module](https://tldp.org/LDP/lkmpg/2.4/html/x208.html#AEN246)


2-3. [hello-2.c](https://tldp.org/LDP/lkmpg/2.4/html/hello2.html#AEN272)


2-4. [Makefile for both our modules](https://tldp.org/LDP/lkmpg/2.4/html/hello2.html#AEN276)


2-5. [hello-3.c](https://tldp.org/LDP/lkmpg/2.4/html/x281.html#AEN311)


2-6. [hello-4.c](https://tldp.org/LDP/lkmpg/2.4/html/x321.html#AEN351)


2-7. [hello-5.c](https://tldp.org/LDP/lkmpg/2.4/html/x354.html#AEN380)


2-8. [start.c](https://tldp.org/LDP/lkmpg/2.4/html/x385.html#AEN421)


2-9. [stop.c](https://tldp.org/LDP/lkmpg/2.4/html/x385.html#AEN428)


2-10. [Makefile for a multi-filed module](https://tldp.org/LDP/lkmpg/2.4/html/x385.html#AEN432)


4-1. [chardev.c](https://tldp.org/LDP/lkmpg/2.4/html/x579.html#AEN700)


4-2. [some title](https://tldp.org/LDP/lkmpg/2.4/html/x579.html#AEN717)


5-1. [procfs.c](https://tldp.org/LDP/lkmpg/2.4/html/x724.html#AEN765)


6-1. [procfs.c](https://tldp.org/LDP/lkmpg/2.4/html/x770.html#AEN851)


7-1. [chardev.c](https://tldp.org/LDP/lkmpg/2.4/html/x856.html#AEN915)


7-2. [chardev.h](https://tldp.org/LDP/lkmpg/2.4/html/x856.html#AEN922)


7-3. [ioctl.c](https://tldp.org/LDP/lkmpg/2.4/html/x856.html#AEN934)


8-1. [syscall.c](https://tldp.org/LDP/lkmpg/2.4/html/x939.html#AEN1009)


9-1. [sleep.c](https://tldp.org/LDP/lkmpg/2.4/html/x1014.html#AEN1112)


10-1. [print_string.c](https://tldp.org/LDP/lkmpg/2.4/html/x1117.html#AEN1146)


11-1. [sched.c](https://tldp.org/LDP/lkmpg/2.4/html/x1151.html#AEN1205)


12-1. [intrpt.c](https://tldp.org/LDP/lkmpg/2.4/html/x1210.html#AEN1291)

* * *
|  | [Next](https://tldp.org/LDP/lkmpg/2.4/html/f23.html)
---|---|---
|  | Foreword
