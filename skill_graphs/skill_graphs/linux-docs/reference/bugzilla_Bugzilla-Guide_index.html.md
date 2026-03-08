#  The Bugzilla Guide - 2.16.3 Release
###  Matthew P. Barnson
###  The Bugzilla Team
2003-04-23

This is the documentation for Bugzilla, the mozilla.org bug-tracking system. Bugzilla is an enterprise-class piece of software that powers issue-tracking for hundreds of organizations around the world, tracking millions of bugs.
This documentation is maintained in DocBook 4.1.2 XML format. Changes are best submitted as plain text or XML diffs, attached to a bug filed in
* * *

**Table of Contents**


1. [About This Guide](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/about.html)


1.1. [Copyright Information](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/copyright.html)


1.2. [Disclaimer](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/disclaimer.html)


1.3. [New Versions](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/newversions.html)


1.4. [Credits](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/credits.html)


1.5. [Document Conventions](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/conventions.html)


2. [Introduction](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/introduction.html)


2.1. [What is Bugzilla?](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/whatis.html)


2.2. [Why Should We Use Bugzilla?](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/why.html)


3. [Using Bugzilla](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/using.html)


3.1. [How do I use Bugzilla?](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/how.html)


3.2. [Hints and Tips](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/hintsandtips.html)


3.3. [User Preferences](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/userpreferences.html)


4. [Installation](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/installation.html)


4.1. [Step-by-step Install](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/stepbystep.html)


4.2. [Optional Additional Configuration](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/extraconfig.html)


4.3. [Win32 Installation Notes](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/win32.html)


4.4. [Mac OS X Installation Notes](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/osx.html)


4.5. [Troubleshooting](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/troubleshooting.html)


5. [Administering Bugzilla](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/administration.html)


5.1. [Bugzilla Configuration](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/parameters.html)


5.2. [User Administration](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/useradmin.html)


5.3. [Product, Component, Milestone, and Version Administration](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/programadmin.html)


5.4. [Voting](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/voting.html)


5.5. [Groups and Group Security](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/groups.html)


5.6. [Bugzilla Security](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/security.html)


5.7. [Template Customisation](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/cust-templates.html)


5.8. [Upgrading to New Releases](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/upgrading.html)


5.9. [Integrating Bugzilla with Third-Party Tools](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/integration.html)


A. [The Bugzilla FAQ](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/faq.html)


B. [The Bugzilla Database](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/database.html)


B.1. [Database Schema Chart](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/dbschema.html)


B.2. [MySQL Bugzilla Database Introduction](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/dbdoc.html)


C. [Useful Patches and Utilities for Bugzilla](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/patches.html)


C.1. [Apache `mod_rewrite` magic](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/rewrite.html)


C.2. [Command-line Bugzilla Queries](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/cmdline.html)


D. [Bugzilla Variants and Competitors](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/variants.html)


D.1. [Red Hat Bugzilla](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/variant-redhat.html)


D.2. [Loki Bugzilla (Fenris)](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/variant-fenris.html)


D.3. [Issuezilla](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/variant-issuezilla.html)


D.4. [Scarab](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/variant-scarab.html)


D.5. [Perforce SCM](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/variant-perforce.html)


D.6. [SourceForge](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/variant-sourceforge.html)


E. [GNU Free Documentation License](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl.html)


0. [PREAMBLE](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl-0.html)


1. [APPLICABILITY AND DEFINITIONS](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl-1.html)


2. [VERBATIM COPYING](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl-2.html)


3. [COPYING IN QUANTITY](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl-3.html)


4. [MODIFICATIONS](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl-4.html)


5. [COMBINING DOCUMENTS](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl-5.html)


6. [COLLECTIONS OF DOCUMENTS](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl-6.html)


7. [AGGREGATION WITH INDEPENDENT WORKS](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl-7.html)


8. [TRANSLATION](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl-8.html)


9. [TERMINATION](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl-9.html)


10. [FUTURE REVISIONS OF THIS LICENSE](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl-10.html)


[How to use this License for your documents](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/gfdl-howto.html)


[Glossary](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/glossary.html)


[Index](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/doc-index.html)


**List of Figures**


4-1. [Other File::Temp error messages](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/troubleshooting.html#trouble-filetemp-errors)


4-2. [Patch for File::Temp in Perl 5.6.0](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/troubleshooting.html#trouble-filetemp-patch)


**List of Examples**


4-1. [Installing ActivePerl ppd Modules on Microsoft Windows](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/win32.html#AEN861)


4-2. [Installing OpenInteract ppd Modules manually on Microsoft Windows](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/win32.html#AEN874)


4-3. [Removing encrypt() for Windows NT Bugzilla version 2.12 or earlier](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/win32.html#AEN1056)


5-1. [Upgrading using CVS](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/upgrading.html#upgrade-cvs)


5-2. [Upgrading using the tarball](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/upgrading.html#upgrade-tarball)


5-3. [Upgrading using patches](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/upgrading.html#upgrade-patches)

* * *
|  | [Next](https://tldp.org/LDP/bugzilla/Bugzilla-Guide/about.html)
---|---|---
|  | About This Guide
