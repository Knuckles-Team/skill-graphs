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


[Legal Information](https://tldp.org/LDP/Pocket-Linux-Guide/html/legal.html)


1. [Copyright and License](https://tldp.org/LDP/Pocket-Linux-Guide/html/copyright.html)


2. [Disclaimer](https://tldp.org/LDP/Pocket-Linux-Guide/html/disclaimer.html)


[Introduction](https://tldp.org/LDP/Pocket-Linux-Guide/html/f60.html)


1. [About Pocket Linux](https://tldp.org/LDP/Pocket-Linux-Guide/html/x62.html)


2. [Prerequisite Skills](https://tldp.org/LDP/Pocket-Linux-Guide/html/x65.html)


3. [Project Format](https://tldp.org/LDP/Pocket-Linux-Guide/html/x77.html)


4. [Help & Support](https://tldp.org/LDP/Pocket-Linux-Guide/html/x91.html)


5. [Feedback](https://tldp.org/LDP/Pocket-Linux-Guide/html/x104.html)


1. [Project Initiation](https://tldp.org/LDP/Pocket-Linux-Guide/html/initiation.html)


1.1. [A Brief History of GNU/Linux](https://tldp.org/LDP/Pocket-Linux-Guide/html/x110.html)


1.2. [The Goal of Pocket Linux](https://tldp.org/LDP/Pocket-Linux-Guide/html/x118.html)


1.3. [Working Within The Constraints](https://tldp.org/LDP/Pocket-Linux-Guide/html/x132.html)


2. [A Simple Prototype](https://tldp.org/LDP/Pocket-Linux-Guide/html/phase1.html)


2.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/x140.html)


2.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/x150.html)


2.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/x185.html)


2.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/x311.html)


3. [Saving Space](https://tldp.org/LDP/Pocket-Linux-Guide/html/phase2.html)


3.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/x360.html)


3.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/x367.html)


3.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/x388.html)


3.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/x459.html)


4. [Some Basic Utilities](https://tldp.org/LDP/Pocket-Linux-Guide/html/phase3.html)


4.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/x495.html)


4.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/x510.html)


4.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/x581.html)


4.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/x677.html)


5. [Checking and Mounting Disks](https://tldp.org/LDP/Pocket-Linux-Guide/html/phase4.html)


5.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/x729.html)


5.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/x755.html)


5.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/x867.html)


5.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/x974.html)


6. [Automating Startup & Shutdown](https://tldp.org/LDP/Pocket-Linux-Guide/html/phase5.html)


6.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1036.html)


6.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1058.html)


6.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1127.html)


6.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1226.html)


7. [Enabling Multiple Users](https://tldp.org/LDP/Pocket-Linux-Guide/html/phase6.html)


7.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1257.html)


7.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1265.html)


7.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1378.html)


7.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1517.html)


8. [Filling in the Gaps](https://tldp.org/LDP/Pocket-Linux-Guide/html/phase7.html)


8.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1563.html)


8.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1601.html)


8.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1654.html)


8.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1737.html)


9. [Project Wrap Up](https://tldp.org/LDP/Pocket-Linux-Guide/html/wrap-up.html)


9.1. [Celebrating Accomplishments](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1801.html)


9.2. [Planning Next Steps](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1815.html)


A. [Hosting Applications](https://tldp.org/LDP/Pocket-Linux-Guide/html/a.html)


A.1. [Analysis](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1829.html)


A.2. [Design](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1841.html)


A.3. [Construction](https://tldp.org/LDP/Pocket-Linux-Guide/html/x1950.html)


A.4. [Implementation](https://tldp.org/LDP/Pocket-Linux-Guide/html/x2058.html)


B. [GNU Free Documentation License](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl.html)


B.1. [PREAMBLE](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl-0.html)


B.2. [APPLICABILITY AND DEFINITIONS](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl-1.html)


B.3. [VERBATIM COPYING](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl-2.html)


B.4. [COPYING IN QUANTITY](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl-3.html)


B.5. [MODIFICATIONS](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl-4.html)


B.6. [COMBINING DOCUMENTS](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl-5.html)


B.7. [COLLECTIONS OF DOCUMENTS](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl-6.html)


B.8. [AGGREGATION WITH INDEPENDENT WORKS](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl-7.html)


B.9. [TRANSLATION](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl-8.html)


B.10. [TERMINATION](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl-9.html)


B.11. [FUTURE REVISIONS OF THIS LICENSE](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl-10.html)


B.12. [ADDENDUM: How to use this License for your documents](https://tldp.org/LDP/Pocket-Linux-Guide/html/gfdl-addendum.html)

* * *
|  | [Next](https://tldp.org/LDP/Pocket-Linux-Guide/html/legal.html)
---|---|---
|  | Legal Information
