##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fchrono&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fchrono "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/chrono.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/w/Talk%253Ac/chrono.html "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/chrono.html)
##### Views
  * [View](https://en.cppreference.com/w/c/chrono.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/chrono&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/chrono&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/chrono.html)
# Date and time utilities
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
**Date and time utilities**
[Input/output support](https://en.cppreference.com/w/c/io.html "c/io")
[Localization support](https://en.cppreference.com/w/c/locale.html "c/locale")
[Concurrency support](https://en.cppreference.com/w/c/thread.html "c/thread") (C11)
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[Symbol index](https://en.cppreference.com/w/c/index.html "c/symbol index")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/navbar_content&action=edit)
**Date and time utilities**
Functions
---
Time manipulation
[difftime](https://en.cppreference.com/w/c/chrono/difftime.html "c/chrono/difftime")
[time](https://en.cppreference.com/w/c/chrono/time.html "c/chrono/time")
[clock](https://en.cppreference.com/w/c/chrono/clock.html "c/chrono/clock")
[timespec_get](https://en.cppreference.com/w/c/chrono/timespec_get.html "c/chrono/timespec get") (C11)
[timespec_getres](https://en.cppreference.com/w/c/chrono/timespec_getres.html "c/chrono/timespec getres") (C23)
Format conversions
[asctimeasctime_s](https://en.cppreference.com/w/c/chrono/asctime.html "c/chrono/asctime") (deprecated in C23)(C11)
[ctimectime_s](https://en.cppreference.com/w/c/chrono/ctime.html "c/chrono/ctime") (deprecated in C23)(C11)
[strftime](https://en.cppreference.com/w/c/chrono/strftime.html "c/chrono/strftime")
[wcsftime](https://en.cppreference.com/w/c/chrono/wcsftime.html "c/chrono/wcsftime") (C95)
[gmtimegmtime_rgmtime_s](https://en.cppreference.com/w/c/chrono/gmtime.html "c/chrono/gmtime") (C23)(C11)
[localtimelocaltime_rlocaltime_s](https://en.cppreference.com/w/c/chrono/localtime.html "c/chrono/localtime") (C23)(C11)
[mktime](https://en.cppreference.com/w/c/chrono/mktime.html "c/chrono/mktime")
Constants
[CLOCKS_PER_SEC](https://en.cppreference.com/w/c/chrono/CLOCKS_PER_SEC.html "c/chrono/CLOCKS PER SEC")
Types
[tm](https://en.cppreference.com/w/c/chrono/tm.html "c/chrono/tm")
[time_t](https://en.cppreference.com/w/c/chrono/time_t.html "c/chrono/time t")
[clock_t](https://en.cppreference.com/w/c/chrono/clock_t.html "c/chrono/clock t")
[timespec](https://en.cppreference.com/w/c/chrono/timespec.html "c/chrono/timespec") (C11)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/navbar_content&action=edit)
## Contents
  * [1 Functions](https://en.cppreference.com/w/c/chrono.html#Functions)
    * [1.1 Time manipulation](https://en.cppreference.com/w/c/chrono.html#Time_manipulation)
    * [1.2 Format conversions](https://en.cppreference.com/w/c/chrono.html#Format_conversions)
  * [2 Constants](https://en.cppreference.com/w/c/chrono.html#Constants)
  * [3 Types](https://en.cppreference.com/w/c/chrono.html#Types)
  * [4 References](https://en.cppreference.com/w/c/chrono.html#References)
  * [5 See also](https://en.cppreference.com/w/c/chrono.html#See_also)


---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/chrono&action=edit&section=1 "Edit section: Functions")] Functions
#####  Time manipulation
---
Defined in header `[`<time.h>`](https://en.cppreference.com/w/c/header/time.html "c/header/time")`
[ difftime](https://en.cppreference.com/w/c/chrono/difftime.html "c/chrono/difftime") |  computes the difference between times
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_difftime&action=edit)
[ time](https://en.cppreference.com/w/c/chrono/time.html "c/chrono/time") |  returns the current calendar time of the system as time since epoch
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_time&action=edit)
[ clock](https://en.cppreference.com/w/c/chrono/clock.html "c/chrono/clock") |  returns raw processor clock time since the program is started
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_clock&action=edit)
[ timespec_get](https://en.cppreference.com/w/c/chrono/timespec_get.html "c/chrono/timespec get") (C11) |  returns the calendar time in seconds and nanoseconds based on a given time base
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_timespec_get&action=edit)
[ timespec_getres](https://en.cppreference.com/w/c/chrono/timespec_getres.html "c/chrono/timespec getres") (C23) |  returns the resolution of calendar time based on a given time base
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_timespec_getres&action=edit)
#####  Format conversions
Defined in header `[`<time.h>`](https://en.cppreference.com/w/c/header/time.html "c/header/time")`
[ asctimeasctime_s](https://en.cppreference.com/w/c/chrono/asctime.html "c/chrono/asctime") (deprecated in C23)(C11) |  converts a [tm](https://en.cppreference.com/w/c/chrono/tm.html "c/chrono/tm") object to a textual representation
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_asctime&action=edit)
[ ctimectime_s](https://en.cppreference.com/w/c/chrono/ctime.html "c/chrono/ctime") (deprecated in C23)(C11) |  converts a [time_t](https://en.cppreference.com/w/c/chrono/time_t.html "c/chrono/time t") object to a textual representation
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_ctime&action=edit)
[ strftime](https://en.cppreference.com/w/c/chrono/strftime.html "c/chrono/strftime") |  converts a [tm](https://en.cppreference.com/w/c/chrono/tm.html "c/chrono/tm") object to custom textual representation
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_strftime&action=edit)
Defined in header `[`<wchar.h>`](https://en.cppreference.com/w/c/header/wchar.html "c/header/wchar")`
[ wcsftime](https://en.cppreference.com/w/c/chrono/wcsftime.html "c/chrono/wcsftime") (C95) |  converts a [tm](https://en.cppreference.com/w/c/chrono/tm.html "c/chrono/tm") object to custom wide string textual representation
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_wcsftime&action=edit)
Defined in header `[`<time.h>`](https://en.cppreference.com/w/c/header/time.html "c/header/time")`
[ gmtimegmtime_rgmtime_s](https://en.cppreference.com/w/c/chrono/gmtime.html "c/chrono/gmtime") (C23)(C11) |  converts time since epoch to calendar time expressed as Coordinated Universal Time (UTC)
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_gmtime&action=edit)
[ localtimelocaltime_rlocaltime_s](https://en.cppreference.com/w/c/chrono/localtime.html "c/chrono/localtime") (C23)(C11) |  converts time since epoch to calendar time expressed as local time
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_localtime&action=edit)
[ mktime](https://en.cppreference.com/w/c/chrono/mktime.html "c/chrono/mktime") |  converts calendar time to time since epoch
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_mktime&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/chrono&action=edit&section=2 "Edit section: Constants")] Constants
Defined in header `[`<time.h>`](https://en.cppreference.com/w/c/header/time.html "c/header/time")`
---
[ CLOCKS_PER_SEC](https://en.cppreference.com/w/c/chrono/CLOCKS_PER_SEC.html "c/chrono/CLOCKS PER SEC") |  number of processor clock ticks per second
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_CLOCKS_PER_SEC&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/chrono&action=edit&section=3 "Edit section: Types")] Types
Defined in header `[`<time.h>`](https://en.cppreference.com/w/c/header/time.html "c/header/time")`
---
[ tm](https://en.cppreference.com/w/c/chrono/tm.html "c/chrono/tm") |  calendar time type
(struct)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_tm&action=edit)
[ time_t](https://en.cppreference.com/w/c/chrono/time_t.html "c/chrono/time t") |  calendar time since epoch type
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_time_t&action=edit)
[ clock_t](https://en.cppreference.com/w/c/chrono/clock_t.html "c/chrono/clock t") |  processor time since era type
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_clock_t&action=edit)
[ timespec](https://en.cppreference.com/w/c/chrono/timespec.html "c/chrono/timespec") (C11) |  time in seconds and nanoseconds
(struct)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/chrono/dsc_timespec&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/chrono&action=edit&section=4 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 7.27 Date and time <time.h> (p: TBD)


  * 7.29.5.1 The wcsftime function (p: TBD)


  * 7.31.14 Date and time <time.h> (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 7.27 Date and time <time.h> (p: 284-291)


  * 7.29.5.1 The wcsftime function (p: 320-321)


  * 7.31.14 Date and time <time.h> (p: 333)


  * C11 standard (ISO/IEC 9899:2011):


  * 7.27 Date and time <time.h> (p: 388-397)


  * 7.29.5.1 The wcsftime function (p: 439-440)


  * 7.31.14 Date and time <time.h> (p: 456)


  * C99 standard (ISO/IEC 9899:1999):


  * 7.23 Date and time <time.h> (p: 338-347)


  * 7.24.5.1 The wcsftime function (p: 385-386)


  * C89/C90 standard (ISO/IEC 9899:1990):


  * 4.12 DATE AND TIME <time.h>


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/chrono&action=edit&section=5 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/chrono/c.html "cpp/chrono/c") for C Date and time utilities
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/chrono&oldid=180683](https://en.cppreference.com/mwiki/index.php?title=c/chrono&oldid=180683)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/chrono.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/chrono "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/chrono "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/chrono&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/chrono&oldid=180683 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/chrono&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/chrono "c/chrono")
  * [Česky](http://cs.cppreference.com/w/c/chrono "c/chrono")
  * [Deutsch](http://de.cppreference.com/w/c/chrono "c/chrono")
  * [Español](http://es.cppreference.com/w/c/chrono "c/chrono")
  * [Français](http://fr.cppreference.com/w/c/chrono "c/chrono")
  * [Italiano](http://it.cppreference.com/w/c/chrono "c/chrono")
  * [日本語](http://ja.cppreference.com/w/c/chrono "c/chrono")
  * [한국어](http://ko.cppreference.com/w/c/chrono "c/chrono")
  * [Polski](http://pl.cppreference.com/w/c/chrono "c/chrono")
  * [Português](http://pt.cppreference.com/w/c/chrono "c/chrono")
  * [Русский](http://ru.cppreference.com/w/c/chrono "c/chrono")
  * [Türkçe](http://tr.cppreference.com/w/c/chrono "c/chrono")
  * [中文](http://zh.cppreference.com/w/c/chrono "c/chrono")


  * This page was last modified on 15 February 2025, at 00:14.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
