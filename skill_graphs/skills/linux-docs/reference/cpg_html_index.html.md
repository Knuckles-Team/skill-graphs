#  Custom Linux: A Porting Guide
## Porting LinuxPPC to a Custom SBC
###  Shie Erlich

`<`

**Rafi Yanai -** my partner in the porting process
**Avi Rubenbach -** without whom this wouldn't be possible
**Revision History**
---
Revision 2.1 | 2003-03-08 | Revised by: gjf
Modified code example per author
Revision 2.0 | 2002-06-13 | Revised by: tab
Added GFDL per author
Revision 1.0 | 2002-05-13 | Revised by: SE
Initial release
* * *

**Table of Contents**


1. [Introduction](https://tldp.org/LDP/cpg/html/c35.html)


1.1. [Who needs to read this ?](https://tldp.org/LDP/cpg/html/x37.html)


1.2. [What do I need to know (why so much) ?](https://tldp.org/LDP/cpg/html/x40.html)


1.3. [The tools](https://tldp.org/LDP/cpg/html/x63.html)


1.4. [The hardware](https://tldp.org/LDP/cpg/html/x86.html)


1.5. [Copyright & License](https://tldp.org/LDP/cpg/html/x114.html)


2. [Bootcamp: How To Begin ?](https://tldp.org/LDP/cpg/html/c119.html)


2.1. [Creating a development environment](https://tldp.org/LDP/cpg/html/x121.html)


2.2. [Compiling the first kernel](https://tldp.org/LDP/cpg/html/x136.html)


2.3. [Booting the machine](https://tldp.org/LDP/cpg/html/x149.html)


3. [Booting In The Dark](https://tldp.org/LDP/cpg/html/c184.html)


3.1. [Debugging with print_str()](https://tldp.org/LDP/cpg/html/x186.html)


3.2. [Modifying code using compiler flags](https://tldp.org/LDP/cpg/html/x197.html)


3.3. [Getting the console to work](https://tldp.org/LDP/cpg/html/x205.html)


4. [Linux Still Isn't Booting](https://tldp.org/LDP/cpg/html/c233.html)


4.1. [Memory probing, RTC and decrementors](https://tldp.org/LDP/cpg/html/x235.html)


4.2. [Big-little endian (we should have known)](https://tldp.org/LDP/cpg/html/x247.html)


4.3. [Ethernet: our first PCI device](https://tldp.org/LDP/cpg/html/x259.html)


4.4. [Some Miscellaneous Issues](https://tldp.org/LDP/cpg/html/x273.html)


5. [Linux Is Booting ... What Now ?](https://tldp.org/LDP/cpg/html/c293.html)


5.1. [The 64 bit barrier](https://tldp.org/LDP/cpg/html/x295.html)


5.2. [Booting from flash](https://tldp.org/LDP/cpg/html/x305.html)


A. [GNU Free Documentation License](https://tldp.org/LDP/cpg/html/gfdl.html)


A.1. [PREAMBLE](https://tldp.org/LDP/cpg/html/gfdl-0.html)


A.2. [APPLICABILITY AND DEFINITIONS](https://tldp.org/LDP/cpg/html/gfdl-1.html)


A.3. [VERBATIM COPYING](https://tldp.org/LDP/cpg/html/gfdl-2.html)


A.4. [COPYING IN QUANTITY](https://tldp.org/LDP/cpg/html/gfdl-3.html)


A.5. [MODIFICATIONS](https://tldp.org/LDP/cpg/html/gfdl-4.html)


A.6. [COMBINING DOCUMENTS](https://tldp.org/LDP/cpg/html/gfdl-5.html)


A.7. [COLLECTIONS OF DOCUMENTS](https://tldp.org/LDP/cpg/html/gfdl-6.html)


A.8. [AGGREGATION WITH INDEPENDENT WORKS](https://tldp.org/LDP/cpg/html/gfdl-7.html)


A.9. [TRANSLATION](https://tldp.org/LDP/cpg/html/gfdl-8.html)


A.10. [TERMINATION](https://tldp.org/LDP/cpg/html/gfdl-9.html)


A.11. [FUTURE REVISIONS OF THIS LICENSE](https://tldp.org/LDP/cpg/html/gfdl-10.html)


A.12. [How to use this License for your documents](https://tldp.org/LDP/cpg/html/gfdl-11.html)


B. [Trademarks](https://tldp.org/LDP/cpg/html/trademarks.html)

* * *
|  | [Next](https://tldp.org/LDP/cpg/html/c35.html)
---|---|---
|  | Introduction
