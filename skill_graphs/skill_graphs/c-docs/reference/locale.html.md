##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Flocale&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Flocale "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/locale.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/mwiki/index.php?title=Talk:c/locale&action=edit&redlink=1 "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/locale.html)
##### Views
  * [View](https://en.cppreference.com/w/c/locale.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/locale&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/locale&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/locale.html)
# Localization support
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")
[ C](https://en.cppreference.com/w/c.html "c")
[Compiler support](https://en.cppreference.com/w/c/compiler_support.html "c/compiler support")
---
[Language](https://en.cppreference.com/w/c/language.html "c/language")
[Headers](https://en.cppreference.com/w/c/header.html "c/header")
[Type support](https://en.cppreference.com/w/c/types.html "c/types")
[Program utilities](https://en.cppreference.com/w/c/program.html "c/program")
[Variadic function support](https://en.cppreference.com/w/c/variadic.html "c/variadic")
[Error handling](https://en.cppreference.com/w/c/error.html "c/error")
[Dynamic memory management](https://en.cppreference.com/w/c/memory.html "c/memory")
[Strings library](https://en.cppreference.com/w/c/string.html "c/string")
[Algorithms](https://en.cppreference.com/w/c/algorithm.html "c/algorithm")
[Numerics](https://en.cppreference.com/w/c/numeric.html "c/numeric")
[Date and time utilities](https://en.cppreference.com/w/c/chrono.html "c/chrono")
[Input/output support](https://en.cppreference.com/w/c/io.html "c/io")
**Localization support**
[Concurrency support](https://en.cppreference.com/w/c/thread.html "c/thread") (C11)
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[Symbol index](https://en.cppreference.com/w/c/index.html "c/symbol index")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/navbar_content&action=edit)
**Localization support**
[setlocale](https://en.cppreference.com/w/c/locale/setlocale.html "c/locale/setlocale")
---
[localeconv](https://en.cppreference.com/w/c/locale/localeconv.html "c/locale/localeconv")
[lconv](https://en.cppreference.com/w/c/locale/lconv.html "c/locale/lconv")
Locale categories
[LC_ALLLC_COLLATELC_CTYPELC_MONETARYLC_NUMERICLC_TIME](https://en.cppreference.com/w/c/locale/LC_categories.html "c/locale/LC categories")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/locale/navbar_content&action=edit)
Defined in header `[`<locale.h>`](https://en.cppreference.com/w/c/header/locale.html "c/header/locale")`
---
[ setlocale](https://en.cppreference.com/w/c/locale/setlocale.html "c/locale/setlocale") |  gets and sets the current C locale
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/locale/dsc_setlocale&action=edit)
[ localeconv](https://en.cppreference.com/w/c/locale/localeconv.html "c/locale/localeconv") |  queries numeric and monetary formatting details of the current locale
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/locale/dsc_localeconv&action=edit)
[ lconv](https://en.cppreference.com/w/c/locale/lconv.html "c/locale/lconv") |  formatting details, returned by [localeconv](https://en.cppreference.com/w/c/locale/localeconv.html "c/locale/localeconv")
(struct)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/locale/dsc_lconv&action=edit)
#####  Locale categories
[ LC_ALLLC_COLLATELC_CTYPELC_MONETARYLC_NUMERICLC_TIME](https://en.cppreference.com/w/c/locale/LC_categories.html "c/locale/LC categories") |  locale categories for [setlocale](https://en.cppreference.com/w/c/locale/setlocale.html "c/locale/setlocale")
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/locale/dsc_LC_categories&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/locale&action=edit&section=1 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 7.11 Localization <locale.h> (p: TBD)


  * 7.31.6 Localization <locale.h> (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 7.11 Localization <locale.h> (p: TBD)


  * 7.31.6 Localization <locale.h> (p: TBD)


  * C11 standard (ISO/IEC 9899:2011):


  * 7.11 Localization <locale.h> (p: 223-230)


  * 7.31.6 Localization <locale.h> (p: 455)


  * C99 standard (ISO/IEC 9899:1999):


  * 7.11 Localization <locale.h> (p: 204-211)


  * 7.26.5 Localization <locale.h> (p: 401)


  * C89/C90 standard (ISO/IEC 9899:1990):


  * 4.4 LOCALIZATION <locale.h>


  * 4.13.3 Localization <locale.h>


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/locale&action=edit&section=2 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/locale.html "cpp/locale") for Localization library
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/locale&oldid=180068](https://en.cppreference.com/mwiki/index.php?title=c/locale&oldid=180068)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/locale.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/locale "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/locale "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/locale&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/locale&oldid=180068 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/locale&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/locale "c/locale")
  * [Česky](http://cs.cppreference.com/w/c/locale "c/locale")
  * [Deutsch](http://de.cppreference.com/w/c/locale "c/locale")
  * [Español](http://es.cppreference.com/w/c/locale "c/locale")
  * [Français](http://fr.cppreference.com/w/c/locale "c/locale")
  * [Italiano](http://it.cppreference.com/w/c/locale "c/locale")
  * [日本語](http://ja.cppreference.com/w/c/locale "c/locale")
  * [한국어](http://ko.cppreference.com/w/c/locale "c/locale")
  * [Polski](http://pl.cppreference.com/w/c/locale "c/locale")
  * [Português](http://pt.cppreference.com/w/c/locale "c/locale")
  * [Русский](http://ru.cppreference.com/w/c/locale "c/locale")
  * [Türkçe](http://tr.cppreference.com/w/c/locale "c/locale")
  * [中文](http://zh.cppreference.com/w/c/locale "c/locale")


  * This page was last modified on 2 February 2025, at 21:35.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
