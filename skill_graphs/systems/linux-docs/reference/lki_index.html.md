[Next](https://tldp.org/LDP/lki/lki-1.html) Previous Contents
* * *
# Linux Kernel 2.4 Internals
## Tigran Aivazian `tigran@veritas.com`
7 August 2002 (29 Av 6001)
* * *
_Introduction to the Linux 2.4 kernel. The latest copy of this document can be always downloaded from:`(quintela@fi.udc.es)` , Francis Galiegue `(fg@mandrakesoft.com)`, Hakjun Mun `(juniorm@orgio.net)`, Matt Kraai `(kraai@alumni.carnegiemellon.edu)`, Nicholas Dronen `(ndronen@frii.com)`, Samuel S Chessman `(chessman@tux.org)`, Nadeem Hasan `(nhasan@nadmm.com)`, Michael Svetlik `(m.svetlik@ssi-schaefer-peem.com)` for various corrections and suggestions. The Linux Page Cache chapter was written by: Christoph Hellwig `(hch@caldera.de)`. The IPC Mechanisms chapter was written by: Russell Weight `(weightr@us.ibm.com)` and Mingming Cao `(mcao@us.ibm.com)`_
* * *
##  1. [Booting](https://tldp.org/LDP/lki/lki-1.html)
  * [1.1 Building the Linux Kernel Image](https://tldp.org/LDP/lki/lki-1.html#ss1.1)
  * [1.2 Booting: Overview](https://tldp.org/LDP/lki/lki-1.html#ss1.2)
  * [1.3 Booting: BIOS POST](https://tldp.org/LDP/lki/lki-1.html#ss1.3)
  * [1.4 Booting: bootsector and setup](https://tldp.org/LDP/lki/lki-1.html#ss1.4)
  * [1.5 Using LILO as a bootloader ](https://tldp.org/LDP/lki/lki-1.html#ss1.5)
  * [1.6 High level initialisation ](https://tldp.org/LDP/lki/lki-1.html#ss1.6)
  * [1.7 SMP Bootup on x86](https://tldp.org/LDP/lki/lki-1.html#ss1.7)
  * [1.8 Freeing initialisation data and code](https://tldp.org/LDP/lki/lki-1.html#ss1.8)
  * [1.9 Processing kernel command line](https://tldp.org/LDP/lki/lki-1.html#ss1.9)


##  2. [Process and Interrupt Management](https://tldp.org/LDP/lki/lki-2.html)
  * [2.1 Task Structure and Process Table](https://tldp.org/LDP/lki/lki-2.html#ss2.1)
  * [2.2 Creation and termination of tasks and kernel threads](https://tldp.org/LDP/lki/lki-2.html#ss2.2)
  * [2.3 Linux Scheduler](https://tldp.org/LDP/lki/lki-2.html#ss2.3)
  * [2.4 Linux linked list implementation](https://tldp.org/LDP/lki/lki-2.html#ss2.4)
  * [2.5 Wait Queues](https://tldp.org/LDP/lki/lki-2.html#ss2.5)
  * [2.6 Kernel Timers](https://tldp.org/LDP/lki/lki-2.html#ss2.6)
  * [2.7 Bottom Halves](https://tldp.org/LDP/lki/lki-2.html#ss2.7)
  * [2.8 Task Queues](https://tldp.org/LDP/lki/lki-2.html#ss2.8)
  * [2.9 Tasklets](https://tldp.org/LDP/lki/lki-2.html#ss2.9)
  * [2.10 Softirqs](https://tldp.org/LDP/lki/lki-2.html#ss2.10)
  * [2.11 How System Calls Are Implemented on i386 Architecture?](https://tldp.org/LDP/lki/lki-2.html#ss2.11)
  * [2.12 Atomic Operations](https://tldp.org/LDP/lki/lki-2.html#ss2.12)
  * [2.13 Spinlocks, Read-write Spinlocks and Big-Reader Spinlocks](https://tldp.org/LDP/lki/lki-2.html#ss2.13)
  * [2.14 Semaphores and read/write Semaphores](https://tldp.org/LDP/lki/lki-2.html#ss2.14)
  * [2.15 Kernel Support for Loading Modules](https://tldp.org/LDP/lki/lki-2.html#ss2.15)


##  3. [Virtual Filesystem (VFS)](https://tldp.org/LDP/lki/lki-3.html)
  * [3.1 Inode Caches and Interaction with Dcache](https://tldp.org/LDP/lki/lki-3.html#ss3.1)
  * [3.2 Filesystem Registration/Unregistration](https://tldp.org/LDP/lki/lki-3.html#ss3.2)
  * [3.3 File Descriptor Management](https://tldp.org/LDP/lki/lki-3.html#ss3.3)
  * [3.4 File Structure Management](https://tldp.org/LDP/lki/lki-3.html#ss3.4)
  * [3.5 Superblock and Mountpoint Management](https://tldp.org/LDP/lki/lki-3.html#ss3.5)
  * [3.6 Example Virtual Filesystem: pipefs](https://tldp.org/LDP/lki/lki-3.html#ss3.6)
  * [3.7 Example Disk Filesystem: BFS](https://tldp.org/LDP/lki/lki-3.html#ss3.7)
  * [3.8 Execution Domains and Binary Formats](https://tldp.org/LDP/lki/lki-3.html#ss3.8)


##  4. [Linux Page Cache](https://tldp.org/LDP/lki/lki-4.html)
##  5. [IPC mechanisms](https://tldp.org/LDP/lki/lki-5.html)
  * [5.1 Semaphores](https://tldp.org/LDP/lki/lki-5.html#ss5.1)
  * [5.2 Message queues](https://tldp.org/LDP/lki/lki-5.html#ss5.2)
  * [5.3 Shared Memory](https://tldp.org/LDP/lki/lki-5.html#ss5.3)
  * [5.4 Linux IPC Primitives](https://tldp.org/LDP/lki/lki-5.html#ss5.4)


* * *
[Next](https://tldp.org/LDP/lki/lki-1.html) Previous Contents
