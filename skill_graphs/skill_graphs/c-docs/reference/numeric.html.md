##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fnumeric&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fnumeric "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/numeric.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/mwiki/index.php?title=Talk:c/numeric&action=edit&redlink=1 "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/numeric.html)
##### Views
  * [View](https://en.cppreference.com/w/c/numeric.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/numeric&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/numeric.html)
# Numerics
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
**Numerics**
[Date and time utilities](https://en.cppreference.com/w/c/chrono.html "c/chrono")
[Input/output support](https://en.cppreference.com/w/c/io.html "c/io")
[Localization support](https://en.cppreference.com/w/c/locale.html "c/locale")
[Concurrency support](https://en.cppreference.com/w/c/thread.html "c/thread") (C11)
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[Symbol index](https://en.cppreference.com/w/c/index.html "c/symbol index")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/navbar_content&action=edit)
**Numerics**
[Common mathematical functions](https://en.cppreference.com/w/c/numeric/math.html "c/numeric/math")
---
[Floating-point environment](https://en.cppreference.com/w/c/numeric/fenv.html "c/numeric/fenv") (C99)
[Pseudo-random number generation](https://en.cppreference.com/w/c/numeric/random.html "c/numeric/random")
[Complex number arithmetic](https://en.cppreference.com/w/c/numeric/complex.html "c/numeric/complex") (C99)
[Type-generic math](https://en.cppreference.com/w/c/numeric/tgmath.html "c/numeric/tgmath") (C99)
[Bit manipulation](https://en.cppreference.com/w/c/numeric.html#Bit_manipulation "c/numeric") (C23)
[Checked integer arithmetic](https://en.cppreference.com/w/c/numeric.html#Checked_integer_arithmetic "c/numeric") (C23)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/navbar_content&action=edit)
The C numerics library includes common mathematical functions and types, as well as support for random number generation.
## Contents
  * [1 Common mathematical functions](https://en.cppreference.com/w/c/numeric.html#Common_mathematical_functions)
  * [2 Floating-point environment](https://en.cppreference.com/w/c/numeric.html#Floating-point_environment)
  * [3 Pseudo-random number generation](https://en.cppreference.com/w/c/numeric.html#Pseudo-random_number_generation)
  * [4 Complex number arithmetic](https://en.cppreference.com/w/c/numeric.html#Complex_number_arithmetic)
  * [5 Type-generic math](https://en.cppreference.com/w/c/numeric.html#Type-generic_math)
  * [6 Bit manipulation (since C23)](https://en.cppreference.com/w/c/numeric.html#Bit_manipulation_.28since_C23.29)
  * [7 Checked integer arithmetic (since C23)](https://en.cppreference.com/w/c/numeric.html#Checked_integer_arithmetic_.28since_C23.29)
  * [8 See also](https://en.cppreference.com/w/c/numeric.html#See_also)


---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric&action=edit&section=1 "Edit section: Common mathematical functions")] [Common mathematical functions](https://en.cppreference.com/w/c/numeric/math.html "c/numeric/math")
The header [`<math.h>`](https://en.cppreference.com/w/c/header/math.html "c/header/math") provides [standard C library mathematical functions](https://en.cppreference.com/w/c/numeric/math.html "c/numeric/math") such as [fabs](https://en.cppreference.com/w/c/numeric/math/fabs.html "c/numeric/math/fabs"), [sqrt](https://en.cppreference.com/w/c/numeric/math/sqrt.html "c/numeric/math/sqrt"), and [sin](https://en.cppreference.com/w/c/numeric/math/sin.html "c/numeric/math/sin").
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric&action=edit&section=2 "Edit section: Floating-point environment")] [Floating-point environment](https://en.cppreference.com/w/c/numeric/fenv.html "c/numeric/fenv")
The header [`<fenv.h>`](https://en.cppreference.com/w/c/header/fenv.html "c/header/fenv") defines [flags and functions related to exceptional floating-point state](https://en.cppreference.com/w/c/numeric/fenv.html "c/numeric/fenv"), such as overflow and division by zero.
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric&action=edit&section=3 "Edit section: Pseudo-random number generation")] [Pseudo-random number generation](https://en.cppreference.com/w/c/numeric/random.html "c/numeric/random")
The header [`<stdlib.h>`](https://en.cppreference.com/w/c/header/stdlib.html "c/header/stdlib") also includes C-style random number generation via [srand](https://en.cppreference.com/w/c/numeric/random/srand.html "c/numeric/random/srand") and [rand](https://en.cppreference.com/w/c/numeric/random/rand.html "c/numeric/random/rand").
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric&action=edit&section=4 "Edit section: Complex number arithmetic")] [Complex number arithmetic](https://en.cppreference.com/w/c/numeric/complex.html "c/numeric/complex")
The header [`<complex.h>`](https://en.cppreference.com/w/c/header/complex.html "c/header/complex") provides types and functions to work with [complex numbers](https://en.cppreference.com/w/c/numeric/complex.html "c/numeric/complex").
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric&action=edit&section=5 "Edit section: Type-generic math")] [Type-generic math](https://en.cppreference.com/w/c/numeric/tgmath.html "c/numeric/tgmath")
The header [`<tgmath.h>`](https://en.cppreference.com/w/c/header/tgmath.html "c/header/tgmath") provides some macros for a function which names XXX:
  * real function:


  * float variant `XXXf`
  * double variant `XXX`
  * long double variant `XXXl`


  * complex function:


  * float variant `cXXXf`
  * double variant `cXXX`
  * long double variant `cXXXl`


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric&action=edit&section=6 "Edit section: Bit manipulation \(since C23\)")] [Bit manipulation](https://en.cppreference.com/w/c/numeric/bit_manip.html "c/numeric/bit manip") (since C23)
The header [`<stdbit.h>`](https://en.cppreference.com/w/c/header/stdbit.html "c/header/stdbit") provides macros and functions to work with the [byte ordering](https://en.cppreference.com/w/c/numeric/bit_manip.html#Macros "c/numeric/bit manip") and [byte and bit representation](https://en.cppreference.com/w/c/numeric/bit_manip.html#Functions "c/numeric/bit manip") of C objects.
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric&action=edit&section=7 "Edit section: Checked integer arithmetic \(since C23\)")] Checked integer arithmetic (since C23)
Provides some [type-generic macros](https://en.cppreference.com/w/c/language/generic.html "c/language/generic") for checked integer arithmetic:
Defined in header `[`<stdckdint.h>`](https://en.cppreference.com/w/c/header/stdckdint.html "c/header/stdckdint")`
---
[ ckd_add](https://en.cppreference.com/w/c/numeric/ckd_add.html "c/numeric/ckd add") (C23) |  checked addition operation on two integers
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_ckd_add&action=edit)
[ ckd_sub](https://en.cppreference.com/w/c/numeric/ckd_sub.html "c/numeric/ckd sub") (C23) |  checked subtraction operation on two integers
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_ckd_sub&action=edit)
[ ckd_mul](https://en.cppreference.com/w/c/numeric/ckd_mul.html "c/numeric/ckd mul") (C23) |  checked multiplication operation on two integers
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_ckd_mul&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric&action=edit&section=8 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/numeric.html "cpp/numeric") for Numerics library
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/numeric&oldid=180191](https://en.cppreference.com/mwiki/index.php?title=c/numeric&oldid=180191)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/numeric.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/numeric "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/numeric "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/numeric&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/numeric&oldid=180191 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/numeric&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/numeric "c/numeric")
  * [Česky](http://cs.cppreference.com/w/c/numeric "c/numeric")
  * [Deutsch](http://de.cppreference.com/w/c/numeric "c/numeric")
  * [Español](http://es.cppreference.com/w/c/numeric "c/numeric")
  * [Français](http://fr.cppreference.com/w/c/numeric "c/numeric")
  * [Italiano](http://it.cppreference.com/w/c/numeric "c/numeric")
  * [日本語](http://ja.cppreference.com/w/c/numeric "c/numeric")
  * [한국어](http://ko.cppreference.com/w/c/numeric "c/numeric")
  * [Polski](http://pl.cppreference.com/w/c/numeric "c/numeric")
  * [Português](http://pt.cppreference.com/w/c/numeric "c/numeric")
  * [Русский](http://ru.cppreference.com/w/c/numeric "c/numeric")
  * [Türkçe](http://tr.cppreference.com/w/c/numeric "c/numeric")
  * [中文](http://zh.cppreference.com/w/c/numeric "c/numeric")


  * This page was last modified on 5 February 2025, at 23:26.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
