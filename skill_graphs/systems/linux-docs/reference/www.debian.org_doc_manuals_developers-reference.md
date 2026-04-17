Debian Developer's Reference
---
|  |  [Next](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/scope.html)
* * *
#  Debian Developer's Reference
### Developer's Reference Team
`<`
###  Andreas Barth
###  Adam Di Carlo
###  Raphaël Hertzog
###  Lucas Nussbaum
###  Christian Schwarz
###  Ian Jackson
ver. 3.4.8
Copyright © 2004, 2005, 2006, 2007 Andreas Barth
Copyright © 1998, 1999, 2000, 2001, 2002, 2003 Adam Di Carlo
Copyright © 2002, 2003, 2008, 2009 Raphaël Hertzog
Copyright © 2008, 2009 Lucas Nussbaum
Copyright © 1997, 1998 Christian Schwarz
This manual is free software; you may redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version.
This is distributed in the hope that it will be useful, but _without any warranty_ ; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU General Public License for more details.
A copy of the GNU General Public License is available as `/usr/share/common-licenses/GPL-2` in the Debian GNU/Linux distribution or on the World Wide Web at
If you want to print this reference, you should use the [pdf version](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developers-reference.pdf). This page is also available in [French](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/index.fr.html), [German](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/index.de.html) and [Japanese](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/index.ja.html).
2012-06-25
* * *
**Table of Contents**

[1. Scope of This Document](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/scope.html)


[2. Applying to Become a Maintainer](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/new-maintainer.html)


[2.1. Getting started](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/new-maintainer.html#getting-started)


[2.2. Debian mentors and sponsors](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/new-maintainer.html#mentors)


[2.3. Registering as a Debian developer](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/new-maintainer.html#registering)


[3. Debian Developer's Duties](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html)


[3.1. Package Maintainer's Duties](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html#package-maintainer-duties)


[3.1.1. Work towards the next `stable` release](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html#help-release)


[3.1.2. Maintain packages in `stable`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html#maintain-stable)


[3.1.3. Manage release-critical bugs](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html#rc-bugs)


[3.1.4. Coordination with upstream developers](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html#upstream-coordination)


[3.2. Administrative Duties](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html#administrative-duties)


[3.2.1. Maintaining your Debian information](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html#user-maint)


[3.2.2. Maintaining your public key](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html#key-maint)


[3.2.3. Voting](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html#voting)


[3.2.4. Going on vacation gracefully](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html#inform-vacation)


[3.2.5. Retiring](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html#s3.7)


[3.2.6. Returning after retirement](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/developer-duties.html#returning)


[4. Resources for Debian Developers](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html)


[4.1. Mailing lists](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#mailing-lists)


[4.1.1. Basic rules for use](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#mailing-lists-rules)


[4.1.2. Core development mailing lists](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#core-devel-mailing-lists)


[4.1.3. Special lists](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#mailing-lists-special)


[4.1.4. Requesting new development-related lists](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#mailing-lists-new)


[4.2. IRC channels](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#irc-channels)


[4.3. Documentation](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#doc-rsrcs)


[4.4. Debian machines](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#server-machines)


[4.4.1. The bugs server](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#servers-bugs)


[4.4.2. The ftp-master server](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#servers-ftp-master)


[4.4.3. The www-master server](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#servers-www)


[4.4.4. The people web server](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#servers-people)


[4.4.5. The VCS servers](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#servers-vcs)


[4.4.6. chroots to different distributions](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#dchroot)


[4.5. The Developers Database](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#devel-db)


[4.6. The Debian archive](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#archive)


[4.6.1. Sections](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#archive-sections)


[4.6.2. Architectures](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#s4.6.2)


[4.6.3. Packages](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#s4.6.3)


[4.6.4. Distributions](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#s4.6.4)


[4.6.5. Release code names](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#codenames)


[4.7. Debian mirrors](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#mirrors)


[4.8. The Incoming system](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#incoming-system)


[4.9. Package information](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#pkg-info)


[4.9.1. On the web](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#pkg-info-web)


[4.9.2. The **dak ls** utility](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#dak-ls)


[4.10. The Package Tracking System](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#pkg-tracking-system)


[4.10.1. The PTS email interface](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#pts-commands)


[4.10.2. Filtering PTS mails](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#pts-mail-filtering)


[4.10.3. Forwarding VCS commits in the PTS](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#pts-vcs-commit)


[4.10.4. The PTS web interface](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#pts-web)


[4.11. Developer's packages overview](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#ddpo)


[4.12. Debian's FusionForge installation: Alioth](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#alioth)


[4.13. Goodies for Developers](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#developer-misc)


[4.13.1. LWN Subscriptions](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#lwn)


[4.13.2. Gandi.net Hosting Discount](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/resources.html#gandi)


[5. Managing Packages](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html)


[5.1. New packages](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#newpackage)


[5.2. Recording changes in the package](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#changelog-entries)


[5.3. Testing the package](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#sanitycheck)


[5.4. Layout of the source package](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#sourcelayout)


[5.5. Picking a distribution](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#distribution)


[5.5.1. Special case: uploads to the `stable` and `oldstable` distributions](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#upload-stable)


[5.5.2. Special case: uploads to `testing/testing-proposed-updates`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#upload-t-p-u)


[5.6. Uploading a package](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#upload)


[5.6.1. Uploading to `ftp-master`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#upload-ftp-master)


[5.6.2. Delayed uploads](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#delayed-incoming)


[5.6.3. Security uploads](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#s5.6.4)


[5.6.4. Other upload queues](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#s5.6.5)


[5.6.5. Notification that a new package has been installed](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#upload-notification)


[5.7. Specifying the package section, subsection and priority](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#override-file)


[5.8. Handling bugs](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#bug-handling)


[5.8.1. Monitoring bugs](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#bug-monitoring)


[5.8.2. Responding to bugs](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#bug-answering)


[5.8.3. Bug housekeeping](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#bug-housekeeping)


[5.8.4. When bugs are closed by new uploads](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#upload-bugfix)


[5.8.5. Handling security-related bugs](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#bug-security)


[5.9. Moving, removing, renaming, adopting, and orphaning packages](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#archive-manip)


[5.9.1. Moving packages](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#moving-pkgs)


[5.9.2. Removing packages](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#removing-pkgs)


[5.9.3. Replacing or renaming packages](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#s5.9.3)


[5.9.4. Orphaning a package](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#orphaning)


[5.9.5. Adopting a package](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#adopting)


[5.10. Porting and being ported](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#porting)


[5.10.1. Being kind to porters](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#kind-to-porters)


[5.10.2. Guidelines for porter uploads](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#porter-guidelines)


[5.10.3. Porting infrastructure and automation](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#porter-automation)


[5.10.4. When your package is _not_ portable](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#packages-arch-specific)


[5.10.5. Marking non-free packages as auto-buildable](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#non-free-buildd)


[5.11. Non-Maintainer Uploads (NMUs)](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#nmu)


[5.11.1. When and how to do an NMU](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#nmu-guidelines)


[5.11.2. NMUs and `debian/changelog`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#nmu-changelog)


[5.11.3. Using the `DELAYED/` queue](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#nmu-delayed)


[5.11.4. NMUs from the maintainer's point of view](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#nmu-maintainer)


[5.11.5. Source NMUs vs Binary-only NMUs (binNMUs)](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#nmu-binnmu)


[5.11.6. NMUs vs QA uploads](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#nmu-qa-upload)


[5.11.7. NMUs vs team uploads](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#nmu-team-upload)


[5.12. Collaborative maintenance](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#collaborative-maint)


[5.13. The testing distribution](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#testing)


[5.13.1. Basics](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#testing-basics)


[5.13.2. Updates from unstable](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#testing-unstable)


[5.13.3. Direct updates to testing](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#t-p-u)


[5.13.4. Frequently asked questions](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/pkgs.html#faq)


[6. Best Packaging Practices](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html)


[6.1. Best practices for `debian/rules`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-debian-rules)


[6.1.1. Helper scripts](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#helper-scripts)


[6.1.2. Separating your patches into multiple files](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#multiple-patches)


[6.1.3. Multiple binary packages](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#multiple-binary)


[6.2. Best practices for `debian/control`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-debian-control)


[6.2.1. General guidelines for package descriptions](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-desc-basics)


[6.2.2. The package synopsis, or short description](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-pkg-synopsis)


[6.2.3. The long description](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-pkg-desc)


[6.2.4. Upstream home page](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-upstream-info)


[6.2.5. Version Control System location](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-vcs)


[6.3. Best practices for `debian/changelog`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-debian-changelog)


[6.3.1. Writing useful changelog entries](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-changelog-do)


[6.3.2. Common misconceptions about changelog entries](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-changelog-misconceptions)


[6.3.3. Common errors in changelog entries](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-changelog-errors)


[6.3.4. Supplementing changelogs with `NEWS.Debian` files](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-news-debian)


[6.4. Best practices for maintainer scripts](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-debian-maint-scripts)


[6.5. Configuration management with `debconf`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-config-mgmt)


[6.5.1. Do not abuse debconf](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#s6.5.1)


[6.5.2. General recommendations for authors and translators](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#s6.5.2)


[6.5.3. Templates fields definition](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#s6.5.3)


[6.5.4. Templates fields specific style guide](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#s6.5.4)


[6.6. Internationalization](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-i18n)


[6.6.1. Handling debconf translations](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-i18n-debconf)


[6.6.2. Internationalized documentation](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-i18n-docs)


[6.7. Common packaging situations](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-common-situations)


[6.7.1. Packages using **autoconf** /**automake**](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-autotools)


[6.7.2. Libraries](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-libraries)


[6.7.3. Documentation](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-docs)


[6.7.4. Specific types of packages](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-other)


[6.7.5. Architecture-independent data](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-archindepdata)


[6.7.6. Needing a certain locale during build](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-locale)


[6.7.7. Make transition packages deborphan compliant](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-transition)


[6.7.8. Best practices for `.orig.tar.{gz,bz2,xz}` files](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-origtargz)


[6.7.9. Best practices for debug packages](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-dbg)


[6.7.10. Best practices for meta-packages](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/best-pkging-practices.html#bpp-meta)


[7. Beyond Packaging](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/beyond-pkging.html)


[7.1. Bug reporting](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/beyond-pkging.html#submit-bug)


[7.1.1. Reporting lots of bugs at once (mass bug filing)](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/beyond-pkging.html#submit-many-bugs)


[7.2. Quality Assurance effort](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/beyond-pkging.html#qa-effort)


[7.2.1. Daily work](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/beyond-pkging.html#qa-daily-work)


[7.2.2. Bug squashing parties](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/beyond-pkging.html#qa-bsp)


[7.3. Contacting other maintainers](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/beyond-pkging.html#contacting-maintainers)


[7.4. Dealing with inactive and/or unreachable maintainers](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/beyond-pkging.html#mia-qa)


[7.5. Interacting with prospective Debian developers](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/beyond-pkging.html#newmaint)


[7.5.1. Sponsoring packages](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/beyond-pkging.html#sponsoring)


[7.5.2. Advocating new developers](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/beyond-pkging.html#advocating-new-developers)


[7.5.3. Handling new maintainer applications](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/beyond-pkging.html#become-application-manager)


[8. Internationalization and Translations](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/l10n.html)


[8.1. How translations are handled within Debian](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/l10n.html#l10n-handling)


[8.2. I18N & L10N FAQ for maintainers](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/l10n.html#l10n-faqm)


[8.2.1. How to get a given text translated](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/l10n.html#l10n-faqm-tr)


[8.2.2. How to get a given translation reviewed](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/l10n.html#l10n-faqm-rev)


[8.2.3. How to get a given translation updated](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/l10n.html#l10n-faqm-update)


[8.2.4. How to handle a bug report concerning a translation](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/l10n.html#l10n-faqm-bug)


[8.3. I18N & L10N FAQ for translators](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/l10n.html#l10n-faqtr)


[8.3.1. How to help the translation effort](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/l10n.html#l10n-faqtr-help)


[8.3.2. How to provide a translation for inclusion in a package](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/l10n.html#l10n-faqtr-inc)


[8.4. Best current practice concerning l10n](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/l10n.html#l10n-best)


[A. Overview of Debian Maintainer Tools](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html)


[A.1. Core tools](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#tools-core)


[A.1.1. `dpkg-dev`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#dpkg-dev)


[A.1.2. `debconf`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#debconf)


[A.1.3. `fakeroot`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#fakeroot)


[A.2. Package lint tools](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#tools-lint)


[A.2.1. `lintian`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#lintian)


[A.2.2. **debdiff**](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#debdiff)


[A.3. Helpers for `debian/rules`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#tools-helpers)


[A.3.1. `debhelper`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#debhelper)


[A.3.2. `dh-make`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#dh-make)


[A.3.3. `equivs`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#equivs)


[A.4. Package builders](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#tools-builders)


[A.4.1. `cvs-buildpackage`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#cvs-buildpackage)


[A.4.2. `debootstrap`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#debootstrap)


[A.4.3. `pbuilder`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#pbuilder)


[A.4.4. `sbuild`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#sbuild)


[A.5. Package uploaders](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#uploaders)


[A.5.1. `dupload`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#dupload)


[A.5.2. `dput`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#dput)


[A.5.3. **dcut**](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#dcut)


[A.6. Maintenance automation](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#tools-maint-automate)


[A.6.1. `devscripts`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#devscripts)


[A.6.2. `autotools-dev`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#autotools-dev)


[A.6.3. `dpkg-repack`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#dpkg-repack)


[A.6.4. `alien`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#alien)


[A.6.5. `debsums`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#debsums)


[A.6.6. `dpkg-dev-el`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#dpkg-dev-el)


[A.6.7. **dpkg-depcheck**](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#dpkg-depcheck)


[A.7. Porting tools](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#tools-porting)


[A.7.1. `quinn-diff`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#quinn-diff)


[A.7.2. `dpkg-cross`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#dpkg-cross)


[A.8. Documentation and information](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#tools-doc)


[A.8.1. `docbook-xml`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#docbook-xml)


[A.8.2. `debiandoc-sgml`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#debiandoc-sgml)


[A.8.3. `debian-keyring`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#debian-keyring)


[A.8.4. `debian-maintainers`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#debian-maintainers)


[A.8.5. `debview`](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/tools.html#debview)

* * *
|  |  [Next](https://tldp.org/LDP/www.debian.org/doc/manuals/developers-reference/scope.html)
---|---|---
|  |  Chapter 1. Scope of This Document
