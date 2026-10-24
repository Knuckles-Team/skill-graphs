##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fnumeric%2Fbit+manip&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fnumeric%2Fbit+manip "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/numeric/bit_manip.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/mwiki/index.php?title=Talk:c/numeric/bit_manip&action=edit&redlink=1 "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/numeric/bit_manip.html)
##### Views
  * [View](https://en.cppreference.com/w/c/numeric/bit_manip.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit_manip&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit_manip&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/numeric/bit_manip.html)
# Bit manipulation (since C23)
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
[Floating-point environment](https://en.cppreference.com/w/c/numeric/fenv.html "c/numeric/fenv") (C99)
[Pseudo-random number generation](https://en.cppreference.com/w/c/numeric/random.html "c/numeric/random")
[Complex number arithmetic](https://en.cppreference.com/w/c/numeric/complex.html "c/numeric/complex") (C99)
[Type-generic math](https://en.cppreference.com/w/c/numeric/tgmath.html "c/numeric/tgmath") (C99)
[Bit manipulation](https://en.cppreference.com/w/c/numeric.html#Bit_manipulation "c/numeric") (C23)
[Checked integer arithmetic](https://en.cppreference.com/w/c/numeric.html#Checked_integer_arithmetic "c/numeric") (C23)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/navbar_content&action=edit)
[Bit manipulation](https://en.cppreference.com/w/c/numeric.html#Bit_manipulation_.28since_C23.29 "c/numeric")
[Functions](https://en.cppreference.com/w/c/numeric/bit_manip.html#Functions "c/numeric/bit manip")
---
[stdc_leading_zeros](https://en.cppreference.com/w/c/numeric/bit/stdc_leading_zeros.html "c/numeric/bit/stdc leading zeros") (C23)
[stdc_leading_ones](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_leading_ones&action=edit&redlink=1 "c/numeric/bit/stdc leading ones \(page does not exist\)") (C23)
[stdc_trailing_zeros](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_trailing_zeros&action=edit&redlink=1 "c/numeric/bit/stdc trailing zeros \(page does not exist\)") (C23)
[stdc_trailing_ones](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_trailing_ones&action=edit&redlink=1 "c/numeric/bit/stdc trailing ones \(page does not exist\)") (C23)
[stdc_first_leading_zero](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_first_leading_zero&action=edit&redlink=1 "c/numeric/bit/stdc first leading zero \(page does not exist\)") (C23)
[stdc_first_leading_one](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_first_leading_one&action=edit&redlink=1 "c/numeric/bit/stdc first leading one \(page does not exist\)") (C23)
[stdc_first_trailing_zero](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_first_trailing_zero&action=edit&redlink=1 "c/numeric/bit/stdc first trailing zero \(page does not exist\)") (C23)
[stdc_first_trailing_one](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_first_trailing_one&action=edit&redlink=1 "c/numeric/bit/stdc first trailing one \(page does not exist\)") (C23)
[stdc_count_zeros](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_count_zeros&action=edit&redlink=1 "c/numeric/bit/stdc count zeros \(page does not exist\)") (C23)
[stdc_count_ones](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_count_ones&action=edit&redlink=1 "c/numeric/bit/stdc count ones \(page does not exist\)") (C23)
[stdc_has_single_bit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_has_single_bit&action=edit&redlink=1 "c/numeric/bit/stdc has single bit \(page does not exist\)") (C23)
[stdc_bit_width](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_bit_width&action=edit&redlink=1 "c/numeric/bit/stdc bit width \(page does not exist\)") (C23)
[stdc_bit_floor](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_bit_floor&action=edit&redlink=1 "c/numeric/bit/stdc bit floor \(page does not exist\)") (C23)
[stdc_bit_ceil](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_bit_ceil&action=edit&redlink=1 "c/numeric/bit/stdc bit ceil \(page does not exist\)") (C23)
[Macro constants](https://en.cppreference.com/w/c/numeric/bit_manip.html#Macro_constants "c/numeric/bit manip")
[__STDC_ENDIAN_LITTLE__
__STDC_ENDIAN_BIG__
__STDC_ENDIAN_NATIVE__](https://en.cppreference.com/w/c/numeric/endian.html "c/numeric/bit/endian") (C23)(C23)(C23)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/bit/navbar_content&action=edit)
|
## Contents
  * [1 Functions](https://en.cppreference.com/w/c/numeric/bit_manip.html#Functions)
  * [2 Macro constants](https://en.cppreference.com/w/c/numeric/bit_manip.html#Macro_constants)
  * [3 References](https://en.cppreference.com/w/c/numeric/bit_manip.html#References)
  * [4 See also](https://en.cppreference.com/w/c/numeric/bit_manip.html#See_also)


---
###  Functions
Defined in header `[`<stdbit.h>`](https://en.cppreference.com/w/c/header/stdbit.html "c/header/stdbit")`
[ stdc_leading_zeros](https://en.cppreference.com/w/c/numeric/bit/stdc_leading_zeros.html "c/numeric/bit/stdc leading zeros") (C23) |  counts the number of consecutive ​0​ bits, starting from the most significant bit
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_leading_zeros&action=edit)
[ stdc_leading_ones](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_leading_ones&action=edit&redlink=1 "c/numeric/bit/stdc leading ones \(page does not exist\)") (C23) |  counts the number of consecutive 1 bits, starting from the most significant bit
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_leading_ones&action=edit)
[ stdc_trailing_zeros](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_trailing_zeros&action=edit&redlink=1 "c/numeric/bit/stdc trailing zeros \(page does not exist\)") (C23) |  counts the number of consecutive ​0​ bits, starting from the least significant bit
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_trailing_zeros&action=edit)
[ stdc_trailing_ones](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_trailing_ones&action=edit&redlink=1 "c/numeric/bit/stdc trailing ones \(page does not exist\)") (C23) |  counts the number of consecutive 1 bits, starting from the least significant bit
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_trailing_ones&action=edit)
[ stdc_first_leading_zero](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_first_leading_zero&action=edit&redlink=1 "c/numeric/bit/stdc first leading zero \(page does not exist\)") (C23) |  finds the first position of ​0​ bit, starting from the most significant bit
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_first_leading_zero&action=edit)
[ stdc_first_leading_one](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_first_leading_one&action=edit&redlink=1 "c/numeric/bit/stdc first leading one \(page does not exist\)") (C23) |  finds the first position of 1 bit, starting from the most significant bit
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_first_leading_one&action=edit)
[ stdc_first_trailing_zero](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_first_trailing_zero&action=edit&redlink=1 "c/numeric/bit/stdc first trailing zero \(page does not exist\)") (C23) |  finds the first position of ​0​ bit, starting from the least significant bit
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_first_trailing_zero&action=edit)
[ stdc_first_trailing_one](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_first_trailing_one&action=edit&redlink=1 "c/numeric/bit/stdc first trailing one \(page does not exist\)") (C23) |  finds the first position of 1 bit, starting from the least significant bit
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_first_trailing_one&action=edit)
[ stdc_count_zeros](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_count_zeros&action=edit&redlink=1 "c/numeric/bit/stdc count zeros \(page does not exist\)") (C23) |  counts the number of ​0​ bits in an unsigned integer
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_count_zeros&action=edit)
[ stdc_count_ones](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_count_ones&action=edit&redlink=1 "c/numeric/bit/stdc count ones \(page does not exist\)") (C23) |  counts the number of 1 bits in an unsigned integer
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_count_ones&action=edit)
[ stdc_has_single_bit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_has_single_bit&action=edit&redlink=1 "c/numeric/bit/stdc has single bit \(page does not exist\)") (C23) |  checks if a number is an integral power of 2
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_has_single_bit&action=edit)
[ stdc_bit_width](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_bit_width&action=edit&redlink=1 "c/numeric/bit/stdc bit width \(page does not exist\)") (C23) |  finds the smallest number of bits needed to represent the given value
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_bit_width&action=edit)
[ stdc_bit_floor](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_bit_floor&action=edit&redlink=1 "c/numeric/bit/stdc bit floor \(page does not exist\)") (C23) |  finds the largest integral power of 2 not greater than the given value
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_bit_floor&action=edit)
[ stdc_bit_ceil](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit/stdc_bit_ceil&action=edit&redlink=1 "c/numeric/bit/stdc bit ceil \(page does not exist\)") (C23) |  finds the smallest integral power of 2 not less than the given value
(type-generic function macro)[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_stdc_bit_ceil&action=edit)
###  Macro constants
Defined in header `[`<stdbit.h>`](https://en.cppreference.com/w/c/header/stdbit.html "c/header/stdbit")`
[ __STDC_ENDIAN_LITTLE____STDC_ENDIAN_BIG__ __STDC_ENDIAN_NATIVE__](https://en.cppreference.com/w/c/numeric/endian.html "c/numeric/bit/endian") (C23) |  indicates the endianness of scalar types
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/numeric/dsc_endian&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit_manip&action=edit&section=1 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 7.18 Bit and byte utilities <stdbit.h>


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit_manip&action=edit&section=2 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/utility/bit.html "cpp/utility/bit") for Bit manipulation
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit_manip&oldid=180023](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit_manip&oldid=180023)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/numeric/bit_manip.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/numeric/bit_manip "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/numeric/bit_manip "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit_manip&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit_manip&oldid=180023 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/numeric/bit_manip&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")
  * [Česky](http://cs.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")
  * [Deutsch](http://de.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")
  * [Español](http://es.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")
  * [Français](http://fr.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")
  * [Italiano](http://it.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")
  * [日本語](http://ja.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")
  * [한국어](http://ko.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")
  * [Polski](http://pl.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")
  * [Português](http://pt.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")
  * [Русский](http://ru.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")
  * [Türkçe](http://tr.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")
  * [中文](http://zh.cppreference.com/w/c/numeric/bit_manip "c/numeric/bit manip")


  * This page was last modified on 1 February 2025, at 09:22.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
