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


1. [Introduction](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/introduction.html)


1.1. [Who would want to read this guide?](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/who-would-want-to-read-this-guide.html)


1.2. [Who would not want to read this guide?](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/who-would-not-want-to-read-this-guide.html)


1.3. [Availability of sources](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/sources-of-document.html)


1.4. [Conventions used in this guide](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/conventions.html)


1.5. [Resources used to create this document](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/resources-used-to-create-this-document.html)


1.6. [Feedback](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/feedback.html)


1.7. [Contributors](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/contributors.html)


2. [Legal](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/legal.html)


2.1. [Disclaimer](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/disclaimer.html)


2.2. [License](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/license.html)


3. [The Unix Tools Philosophy](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/the-unix-tools-philosophy.html)


4. [Shell Tips](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/shell-tips.html)


4.1. [General Shell Tips](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/general-shell-tips.html)


4.2. [The command-line history](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/the-command-line-history.html)


4.3. [Other Key combinations](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/other-key-combinations.html)


4.4. [Virtual Terminals and screen](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/virtual-terminals.html)


5. [Help](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/help.html)


6. [Directing Input/Output](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/directing-input-ouput.html)


6.1. [Concept Definitions](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/concept-definitions.html)


6.2. [Usage](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/usage-input-output.html)


6.3. [Command Substitution](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/command-substitution.html)


6.4. [Performing more than one command](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/performing-more-than-one-command.html)


7. [Working with the file-system](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/working-with-the-file-system.html)


7.1. [Moving around the filesystem](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/using-filesystem.html)


7.2. [Working with files and folders](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/working-files-folders.html)


7.3. [Mass Rename/copy/link Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/mass-rename.html)


8. [Finding information about the system](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/finding-information.html)


8.1. [Date/Time/Calendars](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/date-time-calendars.html)


8.2. [Finding information about partitions](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/hard-disk-partition-info.html)


9. [Controlling the system](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/controlling-the-system.html)


9.1. [Mounting and Unmounting (Floppy/CDROM/Hard-drive Partitions)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/mounting-and-unmounting.html)


9.2. [Shutting Down/Rebooting the System](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/shutting-down.html)


9.3. [Controlling Processes](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/controlling-processes.html)


9.4. [Controlling services](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/controlling-services.html)


10. [Managing users](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/managing-users.html)


10.1. [Users/Groups](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/users-and-groups.html)


11. [Text Related Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/text-related-tools.html)


11.1. [Text Editors](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/text-editors.html)


11.2. [Text Viewing Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/text-viewing-tools.html)


11.3. [Text Information Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/text-information-tools.html)


11.4. [Text manipulation tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/text-manipulation-tools.html)


11.5. [Text Conversion/Filter Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/text-filter-tools.html)


11.6. [Finding Text Within Files](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/finding-text-within-files.html)


12. [Mathematical tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/mathematical-tools.html)


13. [Network Commands](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/network-commands.html)


13.1. [Network Configuration](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/network-configuration.html)


13.2. [Internet Specific Commands](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/internet-specific-commands.html)


13.3. [Remote Administration Related](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/remote-administration.html)


14. [Security](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/security.html)


14.1. [Some basic Security Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/some-basic-security-tools.html)


14.2. [File Permissions](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/file-permissions.html)


15. [Archiving Files](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/backing-up-files.html)


15.1. [tar (tape archiver)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/tar.html)


15.2. [rsync](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/rsync.html)


15.3. [Compression](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/compression.html)


16. [Graphics tools (command line based)](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/graphics-tools.html)


17. [Working with MS-DOS files](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/working-with-ms-dos.html)


18. [Scheduling Commands to run in the background](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/scheduling.html)


19. [Miscellaneous](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/miscellaneous.html)


20. [Mini-Guides](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/mini-guides.html)


20.1. [RPM: Redhat Package Management System](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/rpm.html)


20.2. [Checking the Hard Disk for errors](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/checking-the-hard-disk.html)


20.3. [Duplicating disks](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/duplicating-disks.html)


20.4. [Wildcards](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/wildcards.html)


A. [Appendix](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/a12264.html)


A.1. [Finding Packages/Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/finding-packages-tools.html)


A.2. [Further Reading](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/further-reading.html)


A.3. [GNU Free Documentation License](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/gnu-free-documentation-licence.html)


[Bibliography](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/references.html)


[Index](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/doc-index.html)

* * *
|  | [Next](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/introduction.html)
---|---|---
|  | Introduction
