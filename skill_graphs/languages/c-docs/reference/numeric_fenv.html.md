##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fnumeric%2Ffenv&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fnumeric%2Ffenv "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/numeric/fenv.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/w/Talk%253Ac/numeric/fenv.html "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/numeric/fenv.html)
##### Views
  * [View](https://en.cppreference.com/w/c/numeric/fenv.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/fenv&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/numeric/fenv&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/numeric/fenv.html)
![ads via Carbon](https://ad.double-click.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B29332811.401293654;dc_trk_aid=593420481;dc_trk_cid=207494836;ord=177299884;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1)
# Floating-point environment
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")‎ | [numeric](https://en.cppreference.com/w/c/numeric.html "c/numeric")
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
[Localization support](https://en.cppreference.com/w/c/locale.html "c/locale")
[Concurrency support](https://en.cppreference.com/w/c/thread.html "c/thread") (C11)
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[Symbol index](https://en.cppreference.com/w/c/index.html "c/symbol index")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/navbar_content&action=edit)
[ Numerics](https://en.cppreference.com/w/c/numeric.html "c/numeric")
[Common mathematical functions](https://en.cppreference.com/w/c/numeric/math.html "c/numeric/math")
---
**Floating-point environment** (C99)
[Pseudo-random number generation](https://en.cppreference.com/w/c/numeric/random.html "c/numeric/random")
[Complex number arithmetic](https://en.cppreference.com/w/c/numeric/complex.html "c/numeric/complex") (C99)
[Type-generic math](https://en.cppreference.com/w/c/numeric/tgmath.html "c/numeric/tgmath") (C99)
[Bit manipulation](https://en.cppreference.com/w/c/numeric.html#Bit_manipulation "c/numeric") (C23)
[Checked integer arithmetic](https://en.cppreference.com/w/c/numeric.html#Checked_integer_arithmetic "c/numeric") (C23)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/navbar_content&action=edit)
**Floating-point environment**
Functions
---
[feclearexcept](https://en.cppreference.com/w/c/numeric/fenv/feclearexcept.html "c/numeric/fenv/feclearexcept") (C99)
[fetestexcept](https://en.cppreference.com/w/c/numeric/fenv/fetestexcept.html "c/numeric/fenv/fetestexcept") (C99)
[feraiseexcept](https://en.cppreference.com/w/c/numeric/fenv/feraiseexcept.html "c/numeric/fenv/feraiseexcept") (C99)
[fegetexceptflagfesetexceptflag](https://en.cppreference.com/w/c/numeric/fenv/feexceptflag.html "c/numeric/fenv/feexceptflag") (C99)(C99)
[fegetroundfesetround](https://en.cppreference.com/w/c/numeric/fenv/feround.html "c/numeric/fenv/feround") (C99)(C99)
[fegetenvfesetenv](https://en.cppreference.com/w/c/numeric/fenv/feenv.html "c/numeric/fenv/feenv") (C99)
[feholdexcept](https://en.cppreference.com/w/c/numeric/fenv/feholdexcept.html "c/numeric/fenv/feholdexcept") (C99)
[feupdateenv](https://en.cppreference.com/w/c/numeric/fenv/feupdateenv.html "c/numeric/fenv/feupdateenv") (C99)
Macro constants
[FE_ALL_EXCEPTFE_DIVBYZEROFE_INEXACTFE_INVALIDFE_OVERFLOWFE_UNDERFLOW](https://en.cppreference.com/w/c/numeric/fenv/FE_exceptions.html "c/numeric/fenv/FE exceptions") (C99)
[FE_DOWNWARDFE_TONEARESTFE_TOWARDZEROFE_UPWARD](https://en.cppreference.com/w/c/numeric/fenv/FE_round.html "c/numeric/fenv/FE round") (C99)
[FE_DFL_ENV](https://en.cppreference.com/w/c/numeric/fenv/FE_DFL_ENV.html "c/numeric/fenv/FE DFL ENV") (C99)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/fenv/navbar_content&action=edit)
The floating-point environment is the set of floating-point status flags and control modes supported by the implementation. It is thread-local, each thread inherits the initial state of its floating-point environment from the parent thread. Floating-point operations modify the floating-point status flags to indicate abnormal results or auxiliary information. The state of floating-point control modes affects the outcomes of some floating-point operations.
The floating-point environment access and modification is only meaningful when [` #pragma STDC FENV_ACCESS`](https://en.cppreference.com/w/cpp/preprocessor/impl.html "cpp/preprocessor/impl") is set to `ON`. Otherwise the implementation is free to assume that floating-point control modes are always the default ones and that floating-point status flags are never tested or modified. In practice, few current compilers, such as HP aCC, Oracle Studio, and IBM XL, support the #pragma explicitly, but most compilers allow meaningful access to the floating-point environment anyway.
## Contents
  * [1 Types](https://en.cppreference.com/w/c/numeric/fenv.html#Types)
  * [2 Functions](https://en.cppreference.com/w/c/numeric/fenv.html#Functions)
  * [3 Macros](https://en.cppreference.com/w/c/numeric/fenv.html#Macros)
  * [4 References](https://en.cppreference.com/w/c/numeric/fenv.html#References)
  * [5 See also](https://en.cppreference.com/w/c/numeric/fenv.html#See_also)


---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/fenv&action=edit&section=1 "Edit section: Types")] Types
Defined in header `[`<fenv.h>`](https://en.cppreference.com/w/c/header/fenv.html "c/header/fenv")`
---
fenv_t |  The type representing the entire floating-point environment
fexcept_t |  The type representing all floating-point status flags collectively
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/fenv&action=edit&section=2 "Edit section: Functions")] Functions
[ feclearexcept](https://en.cppreference.com/w/c/numeric/fenv/feclearexcept.html "c/numeric/fenv/feclearexcept") (C99) |  clears the specified floating-point status flags
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/fenv/dsc_feclearexcept&action=edit)
---|---
[ fetestexcept](https://en.cppreference.com/w/c/numeric/fenv/fetestexcept.html "c/numeric/fenv/fetestexcept") (C99) |  determines which of the specified floating-point status flags are set
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/fenv/dsc_fetestexcept&action=edit)
[ feraiseexcept](https://en.cppreference.com/w/c/numeric/fenv/feraiseexcept.html "c/numeric/fenv/feraiseexcept") (C99) |  raises the specified floating-point exceptions
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/fenv/dsc_feraiseexcept&action=edit)
[ fegetexceptflagfesetexceptflag](https://en.cppreference.com/w/c/numeric/fenv/feexceptflag.html "c/numeric/fenv/feexceptflag") (C99)(C99) |  copies the state of the specified floating-point status flags from or to the floating-point environment
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/fenv/dsc_feexceptflag&action=edit)
[ fegetroundfesetround](https://en.cppreference.com/w/c/numeric/fenv/feround.html "c/numeric/fenv/feround") (C99)(C99) |  gets or sets rounding direction
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/fenv/dsc_feround&action=edit)
[ fegetenvfesetenv](https://en.cppreference.com/w/c/numeric/fenv/feenv.html "c/numeric/fenv/feenv") (C99) |  saves or restores the current floating-point environment
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/fenv/dsc_feenv&action=edit)
[ feholdexcept](https://en.cppreference.com/w/c/numeric/fenv/feholdexcept.html "c/numeric/fenv/feholdexcept") (C99) |  saves the environment, clears all status flags and ignores all future errors
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/fenv/dsc_feholdexcept&action=edit)
[ feupdateenv](https://en.cppreference.com/w/c/numeric/fenv/feupdateenv.html "c/numeric/fenv/feupdateenv") (C99) |  restores the floating-point environment and raises the previously raise exceptions
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/fenv/dsc_feupdateenv&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/fenv&action=edit&section=3 "Edit section: Macros")] Macros
[ FE_ALL_EXCEPTFE_DIVBYZEROFE_INEXACTFE_INVALIDFE_OVERFLOWFE_UNDERFLOW](https://en.cppreference.com/w/c/numeric/fenv/FE_exceptions.html "c/numeric/fenv/FE exceptions") (C99) |  floating-point exceptions
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/fenv/dsc_FE_exceptions&action=edit)
---|---
[ FE_DOWNWARDFE_TONEARESTFE_TOWARDZEROFE_UPWARD](https://en.cppreference.com/w/c/numeric/fenv/FE_round.html "c/numeric/fenv/FE round") (C99) |  floating-point rounding direction
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/fenv/dsc_FE_round&action=edit)
[ FE_DFL_ENV](https://en.cppreference.com/w/c/numeric/fenv/FE_DFL_ENV.html "c/numeric/fenv/FE DFL ENV") (C99) |  default floating-point environment
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/fenv/dsc_FE_DFL_ENV&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/fenv&action=edit&section=4 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 7.6 Floating-point environment <fenv.h> (p: TBD)


  * 7.31.4 Floating-point environment <fenv.h> (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 7.6 Floating-point environment <fenv.h> (p: 150-156)


  * 7.31.4 Floating-point environment <fenv.h> (p: 332)


  * C11 standard (ISO/IEC 9899:2011):


  * 7.6 Floating-point environment <fenv.h> (p: 206-215)


  * 7.31.4 Floating-point environment <fenv.h> (p: 455)


  * C99 standard (ISO/IEC 9899:1999):


  * 7.6 Floating-point environment <fenv.h> (p: 187-196)


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/fenv&action=edit&section=5 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/numeric/fenv.html "cpp/numeric/fenv") for Floating-point environment
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/numeric/fenv&oldid=180048](https://en.cppreference.com/mwiki/index.php?title=c/numeric/fenv&oldid=180048)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/numeric/fenv.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/numeric/fenv "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/numeric/fenv "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/numeric/fenv&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/numeric/fenv&oldid=180048 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/numeric/fenv&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")
  * [Česky](http://cs.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")
  * [Deutsch](http://de.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")
  * [Español](http://es.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")
  * [Français](http://fr.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")
  * [Italiano](http://it.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")
  * [日本語](http://ja.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")
  * [한국어](http://ko.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")
  * [Polski](http://pl.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")
  * [Português](http://pt.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")
  * [Русский](http://ru.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")
  * [Türkçe](http://tr.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")
  * [中文](http://zh.cppreference.com/w/c/numeric/fenv "c/numeric/fenv")


  * This page was last modified on 2 February 2025, at 04:24.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
