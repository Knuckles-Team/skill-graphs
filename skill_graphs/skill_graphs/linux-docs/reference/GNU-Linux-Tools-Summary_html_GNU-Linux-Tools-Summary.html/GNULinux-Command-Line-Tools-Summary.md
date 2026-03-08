#  GNU/Linux Command-Line Tools Summary
###  Gareth Anderson

`<`

**Chris Karakas -** Conversion from LyX to DocBook SGML, Index generation
**Revision History**
---
Revision 1.2 | 15th April 2006 | Revised by: GA
Corrected typing errors, generated new, much smaller index (more accurate in my opinion). Updated errors in document for TLDP.
Revision 1.1 | 28th February 2006 | Revised by: CK
Corrected typos, generated new index (9000 index entries!).
Revision 1.0 | 6th February 2006 | Revised by: GA
Major restructuring, now in a docbook book format. Removed large chunks of content and revised other parts (removed chapters and sectioned some areas more). This is likely the final release by the author, I hope that someone finds this guide useful as I do not intend to continue work on this guide.
Revision 0.7.1 | 25th February 2005 | Revised by: CK
Set special characters in math mode, produced PDF and PS with Computer Modern fonts in OT1 encoding and created correct SGML for key combinations.
Revision 0.7 | 5th December 2004 | Revised by: GA
Updated document with new grammatical review. Re-ordered the entire Text section. Removed a fair amount of content.
Revision v0.6 | 20th April 2004 | Revised by: GA
Attempted to fix document according to TLDP criticisms. Added notes and tips more sectioning. Now complying to the open group standards for the UNIX
system trademark. Document should be ready for TLDP site.
Revision v0.5 | 6th October 2003 | Revised by: GA
Fixed a variety of errors as according to the review and made some consistency improvements to the document.
Revision v0.4 | 15th July 2003 | Revised by: GA
Made small improvements to the document as suggested (so far) by the thorough TLDP review, improved consistency of document and made small content additions.
Revision v0.3 | 26th June 2003 | Revised by: GA
Minor errors fixed, updated the appendix with information for finding where a tool is from. Fixed referencing/citation problems and improved further reading and intro sections, added an audio section.
Revision v0.2 | 20th April 2003 | Revised by: GA
This is the initial public release. Added more code-style then before, broke text-section into more subsections. Improved consistency of document and fixed various index entries.
Revision v0.1 | 27th March 2003 | Revised by: GA
This is the initial draft release (the first release to be converted from LyX to DocBook SGML).
This document is an attempt to provide a summary of useful command-line tools available to a GNU/Linux based operating system, the tools listed are designed to benefit the majority of users and have being chosen at the authors discretion. This document is not a comprehensive list of _every_ existent tool available to a GNU/Linux based system, nor does it have in-depth explanations of how things work. It is a summary which can be used to learn about and how to use many of the tools available to a GNU/Linux based operating system.
* * *

**Table of Contents**


1. [Introduction](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#INTRODUCTION)


1.1. [Who would want to read this guide?](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#WHO-WOULD-WANT-TO-READ-THIS-GUIDE)


1.2. [Who would not want to read this guide?](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#WHO-WOULD-NOT-WANT-TO-READ-THIS-GUIDE)


1.3. [Availability of sources](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#SOURCES-OF-DOCUMENT)


1.4. [Conventions used in this guide](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#CONVENTIONS)


1.5. [Resources used to create this document](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#RESOURCES-USED-TO-CREATE-THIS-DOCUMENT)


1.6. [Feedback](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FEEDBACK)


1.7. [Contributors](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#CONTRIBUTORS)


2. [Legal](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#LEGAL)


2.1. [Disclaimer](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#DISCLAIMER)


2.2. [License](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#LICENSE)


3. [The Unix Tools Philosophy](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#THE-UNIX-TOOLS-PHILOSOPHY)


4. [Shell Tips](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#SHELL-TIPS)


4.1. [General Shell Tips](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#GENERAL-SHELL-TIPS)


4.2. [The command-line history](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#THE-COMMAND-LINE-HISTORY)


4.3. [Other Key combinations](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#OTHER-KEY-COMBINATIONS)


4.4. [Virtual Terminals and screen](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#VIRTUAL-TERMINALS)


5. [Help](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#HELP)


6. [Directing Input/Output](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#DIRECTING-INPUT-OUPUT)


6.1. [Concept Definitions](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#CONCEPT-DEFINITIONS)


6.2. [Usage](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#USAGE-INPUT-OUTPUT)


6.3. [Command Substitution](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#COMMAND-SUBSTITUTION)


6.4. [Performing more than one command](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#PERFORMING-MORE-THAN-ONE-COMMAND)


7. [Working with the file-system](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#WORKING-WITH-THE-FILE-SYSTEM)


7.1. [Moving around the filesystem](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#USING-FILESYSTEM)


7.2. [Working with files and folders](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#WORKING-FILES-FOLDERS)


7.3. [Mass Rename/copy/link Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#MASS-RENAME)


8. [Finding information about the system](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FINDING-INFORMATION)


8.1. [Date/Time/Calendars](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#DATE-TIME-CALENDARS)


8.2. [Finding information about partitions](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#HARD-DISK-PARTITION-INFO)


9. [Controlling the system](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#CONTROLLING-THE-SYSTEM)


9.1. [Mounting and Unmounting (Floppy/CDROM/Hard-drive Partitions)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#MOUNTING-AND-UNMOUNTING)


9.2. [Shutting Down/Rebooting the System](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#SHUTTING-DOWN)


9.3. [Controlling Processes](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#CONTROLLING-PROCESSES)


9.4. [Controlling services](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#CONTROLLING-SERVICES)


10. [Managing users](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#MANAGING-USERS)


10.1. [Users/Groups](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#USERS-AND-GROUPS)


11. [Text Related Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#TEXT-RELATED-TOOLS)


11.1. [Text Editors](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#TEXT-EDITORS)


11.2. [Text Viewing Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#TEXT-VIEWING-TOOLS)


11.3. [Text Information Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#TEXT-INFORMATION-TOOLS)


11.4. [Text manipulation tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#TEXT-MANIPULATION-TOOLS)


11.5. [Text Conversion/Filter Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#TEXT-FILTER-TOOLS)


11.6. [Finding Text Within Files](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FINDING-TEXT-WITHIN-FILES)


12. [Mathematical tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#MATHEMATICAL-TOOLS)


13. [Network Commands](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#NETWORK-COMMANDS)


13.1. [Network Configuration](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#NETWORK-CONFIGURATION)


13.2. [Internet Specific Commands](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#INTERNET-SPECIFIC-COMMANDS)


13.3. [Remote Administration Related](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#REMOTE-ADMINISTRATION)


14. [Security](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#SECURITY)


14.1. [Some basic Security Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#SOME-BASIC-SECURITY-TOOLS)


14.2. [File Permissions](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FILE-PERMISSIONS)


15. [Archiving Files](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#BACKING-UP-FILES)


15.1. [tar (tape archiver)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#TAR)


15.2. [rsync](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#RSYNC)


15.3. [Compression](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#COMPRESSION)


16. [Graphics tools (command line based)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#GRAPHICS-TOOLS)


17. [Working with MS-DOS files](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#WORKING-WITH-MS-DOS)


18. [Scheduling Commands to run in the background](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#SCHEDULING)


19. [Miscellaneous](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#MISCELLANEOUS)


20. [Mini-Guides](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#MINI-GUIDES)


20.1. [RPM: Redhat Package Management System](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#RPM)


20.2. [Checking the Hard Disk for errors](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#CHECKING-THE-HARD-DISK)


20.3. [Duplicating disks](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#DUPLICATING-DISKS)


20.4. [Wildcards](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#WILDCARDS)


A. [Appendix](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#AEN12264)


A.1. [Finding Packages/Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FINDING-PACKAGES-TOOLS)


A.2. [Further Reading](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#FURTHER-READING)


A.3. [GNU Free Documentation License](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#GNU-FREE-DOCUMENTATION-LICENCE)


[Bibliography](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#REFERENCES)


[Index](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/GNU-Linux-Tools-Summary.html#DOC-INDEX)

* * *
