#  Pocket Linux Guide
###  David Horton

`<`

**Revision History**
---
Revision 3.1 | 2005-04-09 | Revised by: DH
Minor clarifications and spelling corrections.
Revision 3.0 | 2004-11-02 | Revised by: DH
Changed bootloader to GRUB rather than LILO. Updated versions on all source code packages. Made minor clarifications to some shell commands and scripts.
Revision 2.1 | 2004-02-18 | Revised by: DH
Corrected typos. Changed resource site hosting to SourceForge. Added appendix B to include the GNU Free Documentation License as part of this document.
Revision 2.0 | 2003-11-08 | Revised by: DH
Updated to use GNU coreutils in place of fileutils, sh-utils and textutils. Updated version numbers on many source code packages. Introduced Freshmeat as a resource for finding source code. Changed /etc/mtab to a real file rather than using a symlink to /proc/mounts. Corrected local_fs script errors. Updated email address.
Revision 1.2 | 2003-05-31 | Revised by: DH
Corrected errors in "strip -o library" commands.
Revision 1.1 | 2003-05-21 | Revised by: DH
Bug fixes, typo corrections and improved XML markup.
Revision 1.0 | 2003-02-17 | Revised by: DH
Initial Release, reviewed by LDP.
The Pocket Linux Guide is for anyone interested in learning the techniques of building a GNU/Linux system from source code. The guide is structured as a project that builds a small diskette-based GNU/Linux system called Pocket Linux. Each chapter explores a small piece of the overall system explaining how it works, why it is needed and how to build it. After completing the Pocket Linux project, readers should possess an enhanced knowledge of what makes GNU/Linux systems work as well as the confidence to explore larger, more complex source-code-only projects.
* * *

**Table of Contents**


[Legal Information](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#legal)


1. [Copyright and License](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#copyright)


2. [Disclaimer](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#disclaimer)


[Introduction](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN60)


1. [About Pocket Linux](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN62)


2. [Prerequisite Skills](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN65)


3. [Project Format](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN77)


4. [Help & Support](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN91)


5. [Feedback](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN104)


1. [Project Initiation](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#initiation)


1.1. [A Brief History of GNU/Linux](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN110)


1.2. [The Goal of Pocket Linux](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN118)


1.3. [Working Within The Constraints](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN132)


2. [A Simple Prototype](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#phase1)


2.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN140)


2.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN150)


2.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN185)


2.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN311)


3. [Saving Space](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#phase2)


3.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN360)


3.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN367)


3.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN388)


3.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN459)


4. [Some Basic Utilities](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#phase3)


4.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN495)


4.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN510)


4.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN581)


4.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN677)


5. [Checking and Mounting Disks](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#phase4)


5.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN729)


5.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN755)


5.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN867)


5.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN974)


6. [Automating Startup & Shutdown](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#phase5)


6.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1036)


6.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1058)


6.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1127)


6.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1226)


7. [Enabling Multiple Users](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#phase6)


7.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1257)


7.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1265)


7.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1378)


7.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1517)


8. [Filling in the Gaps](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#phase7)


8.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1563)


8.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1601)


8.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1654)


8.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1737)


9. [Project Wrap Up](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#wrap-up)


9.1. [Celebrating Accomplishments](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1801)


9.2. [Planning Next Steps](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1815)


A. [Hosting Applications](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#a)


A.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1829)


A.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1841)


A.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN1950)


A.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#AEN2058)


B. [GNU Free Documentation License](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl)


B.1. [PREAMBLE](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl-0)


B.2. [APPLICABILITY AND DEFINITIONS](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl-1)


B.3. [VERBATIM COPYING](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl-2)


B.4. [COPYING IN QUANTITY](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl-3)


B.5. [MODIFICATIONS](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl-4)


B.6. [COMBINING DOCUMENTS](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl-5)


B.7. [COLLECTIONS OF DOCUMENTS](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl-6)


B.8. [AGGREGATION WITH INDEPENDENT WORKS](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl-7)


B.9. [TRANSLATION](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl-8)


B.10. [TERMINATION](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl-9)


B.11. [FUTURE REVISIONS OF THIS LICENSE](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl-10)


B.12. [ADDENDUM: How to use this License for your documents](https://tldp.org/LDP/Pocket-Linux-Guide/html/Pocket-Linux-Guide.html#gfdl-addendum)

* * *
