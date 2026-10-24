#  The Linux Kernel Module Programming Guide
Peter Jay Salzman
Michael Burian
Ori Pomerantz

[Copyright](https://tldp.org/LDP/lkmpg/2.6/html/ln16.html) © 2001 Peter Jay Salzman
2007-05-18 ver 2.6.4

* * *

**Table of Contents**


[Foreword](https://tldp.org/LDP/lkmpg/2.6/html/f25.html)


1. [Authorship](https://tldp.org/LDP/lkmpg/2.6/html/x27.html)


2. [Versioning and Notes](https://tldp.org/LDP/lkmpg/2.6/html/x30.html)


3. [Acknowledgements](https://tldp.org/LDP/lkmpg/2.6/html/x35.html)


1. [Introduction](https://tldp.org/LDP/lkmpg/2.6/html/c38.html)


1.1. [What Is A Kernel Module?](https://tldp.org/LDP/lkmpg/2.6/html/x40.html)


1.2. [How Do Modules Get Into The Kernel?](https://tldp.org/LDP/lkmpg/2.6/html/x44.html)


2. [Hello World](https://tldp.org/LDP/lkmpg/2.6/html/c119.html)


2.1. [Hello, World (part 1): The Simplest Module](https://tldp.org/LDP/lkmpg/2.6/html/x121.html)


2.2. [Compiling Kernel Modules](https://tldp.org/LDP/lkmpg/2.6/html/x181.html)


2.3. [Hello World (part 2)](https://tldp.org/LDP/lkmpg/2.6/html/hello2.html)


2.4. [Hello World (part 3): The `__init` and `__exit` Macros](https://tldp.org/LDP/lkmpg/2.6/html/x245.html)


2.5. [Hello World (part 4): Licensing and Module Documentation](https://tldp.org/LDP/lkmpg/2.6/html/x279.html)


2.6. [Passing Command Line Arguments to a Module](https://tldp.org/LDP/lkmpg/2.6/html/x323.html)


2.7. [Modules Spanning Multiple Files](https://tldp.org/LDP/lkmpg/2.6/html/x351.html)


2.8. [Building modules for a precompiled kernel](https://tldp.org/LDP/lkmpg/2.6/html/x380.html)


3. [Preliminaries](https://tldp.org/LDP/lkmpg/2.6/html/c425.html)


3.1. [Modules vs Programs](https://tldp.org/LDP/lkmpg/2.6/html/x427.html)


4. [Character Device Files](https://tldp.org/LDP/lkmpg/2.6/html/c567.html)


4.1. [Character Device Drivers](https://tldp.org/LDP/lkmpg/2.6/html/x569.html)


5. [The /proc File System](https://tldp.org/LDP/lkmpg/2.6/html/c708.html)


5.1. [The /proc File System](https://tldp.org/LDP/lkmpg/2.6/html/x710.html)


5.2. [Read and Write a /proc File](https://tldp.org/LDP/lkmpg/2.6/html/x769.html)


5.3. [Manage /proc file with standard filesystem](https://tldp.org/LDP/lkmpg/2.6/html/x810.html)


5.4. [Manage /proc file with seq_file](https://tldp.org/LDP/lkmpg/2.6/html/x861.html)


6. [Using /proc For Input](https://tldp.org/LDP/lkmpg/2.6/html/c885.html)


6.1. [TODO: Write a chapter about sysfs](https://tldp.org/LDP/lkmpg/2.6/html/x887.html)


7. [Talking To Device Files](https://tldp.org/LDP/lkmpg/2.6/html/c890.html)


7.1. [Talking to Device Files (writes and IOCTLs)](https://tldp.org/LDP/lkmpg/2.6/html/x892.html)


8. [System Calls](https://tldp.org/LDP/lkmpg/2.6/html/c976.html)


8.1. [System Calls](https://tldp.org/LDP/lkmpg/2.6/html/x978.html)


9. [Blocking Processes](https://tldp.org/LDP/lkmpg/2.6/html/c1050.html)


9.1. [Blocking Processes](https://tldp.org/LDP/lkmpg/2.6/html/x1052.html)


10. [Replacing Printks](https://tldp.org/LDP/lkmpg/2.6/html/c1159.html)


10.1. [Replacing `printk`](https://tldp.org/LDP/lkmpg/2.6/html/x1161.html)


10.2. [Flashing keyboard LEDs](https://tldp.org/LDP/lkmpg/2.6/html/x1194.html)


11. [Scheduling Tasks](https://tldp.org/LDP/lkmpg/2.6/html/c1209.html)


11.1. [Scheduling Tasks](https://tldp.org/LDP/lkmpg/2.6/html/x1211.html)


12. [Interrupt Handlers](https://tldp.org/LDP/lkmpg/2.6/html/interrupthandlers.html)


12.1. [Interrupt Handlers](https://tldp.org/LDP/lkmpg/2.6/html/x1256.html)


13. [Symmetric Multi Processing](https://tldp.org/LDP/lkmpg/2.6/html/c1324.html)


13.1. [Symmetrical Multi-Processing](https://tldp.org/LDP/lkmpg/2.6/html/x1326.html)


14. [Common Pitfalls](https://tldp.org/LDP/lkmpg/2.6/html/c1350.html)


14.1. [Common Pitfalls](https://tldp.org/LDP/lkmpg/2.6/html/x1352.html)


A. [Changes: 2.0 To 2.2](https://tldp.org/LDP/lkmpg/2.6/html/a1387.html)


A.1. [Changes between 2.4 and 2.6](https://tldp.org/LDP/lkmpg/2.6/html/x1389.html)


B. [Where To Go From Here](https://tldp.org/LDP/lkmpg/2.6/html/a1403.html)


B.1. [Where From Here?](https://tldp.org/LDP/lkmpg/2.6/html/x1405.html)


[Index](https://tldp.org/LDP/lkmpg/2.6/html/doc-index.html)


**List of Figures**


5-1. [How seq_file works](https://tldp.org/LDP/lkmpg/2.6/html/x861.html#AEN868)


**List of Examples**


2-1. [hello-1.c](https://tldp.org/LDP/lkmpg/2.6/html/x121.html#AEN128)


2-2. [Makefile for a basic kernel module](https://tldp.org/LDP/lkmpg/2.6/html/x181.html#AEN189)


2-3. [hello-2.c](https://tldp.org/LDP/lkmpg/2.6/html/hello2.html#AEN232)


2-4. [Makefile for both our modules](https://tldp.org/LDP/lkmpg/2.6/html/hello2.html#AEN237)


2-5. [hello-3.c](https://tldp.org/LDP/lkmpg/2.6/html/x245.html#AEN275)


2-6. [hello-4.c](https://tldp.org/LDP/lkmpg/2.6/html/x279.html#AEN319)


2-7. [hello-5.c](https://tldp.org/LDP/lkmpg/2.6/html/x323.html#AEN345)


2-8. [start.c](https://tldp.org/LDP/lkmpg/2.6/html/x351.html#AEN361)


2-9. [stop.c](https://tldp.org/LDP/lkmpg/2.6/html/x351.html#AEN369)


2-10. [Makefile](https://tldp.org/LDP/lkmpg/2.6/html/x351.html#AEN374)


4-1. [chardev.c](https://tldp.org/LDP/lkmpg/2.6/html/x569.html#AEN687)


5-1. [procfs1.c](https://tldp.org/LDP/lkmpg/2.6/html/x710.html#AEN765)


5-2. [procfs2.c](https://tldp.org/LDP/lkmpg/2.6/html/x769.html#AEN806)


5-3. [procfs3.c](https://tldp.org/LDP/lkmpg/2.6/html/x810.html#AEN853)


5-4. [procfs4.c](https://tldp.org/LDP/lkmpg/2.6/html/x861.html#AEN872)


7-1. [chardev.c](https://tldp.org/LDP/lkmpg/2.6/html/x892.html#AEN951)


7-2. [chardev.h](https://tldp.org/LDP/lkmpg/2.6/html/x892.html#AEN959)


7-3. [ioctl.c](https://tldp.org/LDP/lkmpg/2.6/html/x892.html#AEN972)


8-1. [syscall.c](https://tldp.org/LDP/lkmpg/2.6/html/x978.html#AEN1046)


9-1. [sleep.c](https://tldp.org/LDP/lkmpg/2.6/html/x1052.html#AEN1151)


9-2. [cat_noblock.c](https://tldp.org/LDP/lkmpg/2.6/html/x1052.html#AEN1155)


10-1. [print_string.c](https://tldp.org/LDP/lkmpg/2.6/html/x1161.html#AEN1190)


10-2. [kbleds.c](https://tldp.org/LDP/lkmpg/2.6/html/x1194.html#AEN1201)


11-1. [sched.c](https://tldp.org/LDP/lkmpg/2.6/html/x1211.html#AEN1250)


12-1. [intrpt.c](https://tldp.org/LDP/lkmpg/2.6/html/x1256.html#AEN1320)

* * *
|  | [Next](https://tldp.org/LDP/lkmpg/2.6/html/f25.html)
---|---|---
|  | Foreword
