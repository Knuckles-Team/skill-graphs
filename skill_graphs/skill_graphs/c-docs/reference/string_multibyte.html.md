##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fstring%2Fmultibyte&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fstring%2Fmultibyte "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/string/multibyte.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/w/Talk%253Ac/string/multibyte.html "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/string/multibyte.html)
##### Views
  * [View](https://en.cppreference.com/w/c/string/multibyte.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/string/multibyte&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/string/multibyte&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/string/multibyte.html)
![ads via Carbon](https://ad.doubleclick.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B29332811.421611894;dc_trk_aid=613858970;dc_trk_cid=235700574;ord=177295382;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1)
# Null-terminated multibyte strings
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")‎ | [string](https://en.cppreference.com/w/c/string.html "c/string")
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
[ Strings library](https://en.cppreference.com/w/c/string.html "c/string")
[Null-terminated byte strings](https://en.cppreference.com/w/c/string/byte.html "c/string/byte")
---
**Null-terminated multibyte strings**
[Null-terminated wide strings](https://en.cppreference.com/w/c/string/wide.html "c/string/wide")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/navbar_content&action=edit)
**Null-terminated multibyte strings**
[Functions](https://en.cppreference.com/w/c/string/multibyte.html#Functions "c/string/multibyte")
---
[Wide/multibyte conversions](https://en.cppreference.com/w/c/string/multibyte.html#Multibyte.2Fwide_character_conversions "c/string/multibyte")
[mbsinit](https://en.cppreference.com/w/c/string/multibyte/mbsinit.html "c/string/multibyte/mbsinit") (C95)
|  [mbstowcsmbstowcs_s](https://en.cppreference.com/w/c/string/multibyte/mbstowcs.html "c/string/multibyte/mbstowcs") (C11)
---
[btowc](https://en.cppreference.com/w/c/string/multibyte/btowc.html "c/string/multibyte/btowc") (C95)
[mbrtowc](https://en.cppreference.com/w/c/string/multibyte/mbrtowc.html "c/string/multibyte/mbrtowc") (C95)
[mbsrtowcsmbsrtowcs_s](https://en.cppreference.com/w/c/string/multibyte/mbsrtowcs.html "c/string/multibyte/mbsrtowcs") (C95)(C11)
[mbrtoc8](https://en.cppreference.com/w/c/string/multibyte/mbrtoc8.html "c/string/multibyte/mbrtoc8") (C23)
[c8rtomb](https://en.cppreference.com/w/c/string/multibyte/c8rtomb.html "c/string/multibyte/c8rtomb") (C23)
[mbrtoc16](https://en.cppreference.com/w/c/string/multibyte/mbrtoc16.html "c/string/multibyte/mbrtoc16") (C11)
[c16rtomb](https://en.cppreference.com/w/c/string/multibyte/c16rtomb.html "c/string/multibyte/c16rtomb") (C11)
[c32rtomb](https://en.cppreference.com/w/c/string/multibyte/c32rtomb.html "c/string/multibyte/c32rtomb") (C11)
[mbrtoc32](https://en.cppreference.com/w/c/string/multibyte/mbrtoc32.html "c/string/multibyte/mbrtoc32") (C11)
| [mblen](https://en.cppreference.com/w/c/string/multibyte/mblen.html "c/string/multibyte/mblen")
---
[mbtowc](https://en.cppreference.com/w/c/string/multibyte/mbtowc.html "c/string/multibyte/mbtowc")
[wctombwctomb_s](https://en.cppreference.com/w/c/string/multibyte/wctomb.html "c/string/multibyte/wctomb") (C11)
[wcstombswcstombs_s](https://en.cppreference.com/w/c/string/multibyte/wcstombs.html "c/string/multibyte/wcstombs") (C11)
[wctob](https://en.cppreference.com/w/c/string/multibyte/wctob.html "c/string/multibyte/wctob") (C95)
[wcrtombwcrtomb_s](https://en.cppreference.com/w/c/string/multibyte/wcrtomb.html "c/string/multibyte/wcrtomb") (C95)(C11)
[wcsrtombswcsrtombs_s](https://en.cppreference.com/w/c/string/multibyte/wcsrtombs.html "c/string/multibyte/wcsrtombs") (C95)(C11)
[mbrlen](https://en.cppreference.com/w/c/string/multibyte/mbrlen.html "c/string/multibyte/mbrlen") (C95)
[Types](https://en.cppreference.com/w/c/string/multibyte.html#Types "c/string/multibyte")
|  [mbstate_t](https://en.cppreference.com/w/c/string/multibyte/mbstate_t.html "c/string/multibyte/mbstate t") (C95)
---
[char8_t](https://en.cppreference.com/w/c/string/multibyte/char8_t.html "c/string/multibyte/char8 t") (C23)
|  [char16_t](https://en.cppreference.com/w/c/string/multibyte/char16_t.html "c/string/multibyte/char16 t") (C11)
---
[char32_t](https://en.cppreference.com/w/c/string/multibyte/char32_t.html "c/string/multibyte/char32 t") (C11)
[Macros](https://en.cppreference.com/w/c/string/multibyte.html#Macros "c/string/multibyte")
| [MB_LEN_MAX](https://en.cppreference.com/w/c/string/multibyte.html#Macros "c/string/multibyte")
---
| [MB_CUR_MAX](https://en.cppreference.com/w/c/string/multibyte.html#Macros "c/string/multibyte")
---
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/navbar_content&action=edit)
A null-terminated multibyte string (NTMBS), or "multibyte string", is a sequence of nonzero bytes followed by a byte with value zero (the terminating null character).
Each character stored in the string may occupy more than one byte. The encoding used to represent characters in a multibyte character string is locale-specific: it may be UTF-8, GB18030, EUC-JP, Shift-JIS, etc. For example, the char array {'\xe4','\xbd','\xa0','\xe5','\xa5','\xbd','\0'} is an NTMBS holding the string "你好" in UTF-8 multibyte encoding: the first three bytes encode the character 你, the next three bytes encode the character 好. The same string encoded in GB18030 is the char array {'\xc4', '\xe3', '\xba', '\xc3', '\0'}, where each of the two characters is encoded as a two-byte sequence.
In some multibyte encodings, any given multibyte character sequence may represent different characters depending on the previous byte sequences, known as "shift sequences". Such encodings are known as state-dependent: knowledge of the current shift state is required to interpret each character. An NTMBS is only valid if it begins and ends in the initial shift state: if a shift sequence was used, the corresponding unshift sequence has to be present before the terminating null character. Examples of such encodings are BOCU-1 and
A multibyte character string is layout-compatible with [null-terminated byte string](https://en.cppreference.com/w/c/string/byte.html "c/string/byte") (NTBS), that is, can be stored, copied, and examined using the same facilities, except for calculating the number of characters. If the correct locale is in effect, I/O functions also handle multibyte strings. Multibyte strings can be converted to and from wide strings using the following locale-dependent conversion functions:
## Contents
  * [1 Functions](https://en.cppreference.com/w/c/string/multibyte.html#Functions)
    * [1.1 Multibyte/wide character conversions](https://en.cppreference.com/w/c/string/multibyte.html#Multibyte.2Fwide_character_conversions)
  * [2 Types](https://en.cppreference.com/w/c/string/multibyte.html#Types)
  * [3 Macros](https://en.cppreference.com/w/c/string/multibyte.html#Macros)
  * [4 References](https://en.cppreference.com/w/c/string/multibyte.html#References)
  * [5 See also](https://en.cppreference.com/w/c/string/multibyte.html#See_also)


---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/string/multibyte&action=edit&section=1 "Edit section: Functions")] Functions
#####  Multibyte/wide character conversions
---
Defined in header `[`<stdlib.h>`](https://en.cppreference.com/w/c/header/stdlib.html "c/header/stdlib")`
[ mblen](https://en.cppreference.com/w/c/string/multibyte/mblen.html "c/string/multibyte/mblen") |  returns the number of bytes in the next multibyte character
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_mblen&action=edit)
[ mbtowc](https://en.cppreference.com/w/c/string/multibyte/mbtowc.html "c/string/multibyte/mbtowc") |  converts the next multibyte character to wide character
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_mbtowc&action=edit)
[ wctombwctomb_s](https://en.cppreference.com/w/c/string/multibyte/wctomb.html "c/string/multibyte/wctomb") (C11) |  converts a wide character to its multibyte representation
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_wctomb&action=edit)
[ mbstowcsmbstowcs_s](https://en.cppreference.com/w/c/string/multibyte/mbstowcs.html "c/string/multibyte/mbstowcs") (C11) |  converts a narrow multibyte character string to wide string
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_mbstowcs&action=edit)
[ wcstombswcstombs_s](https://en.cppreference.com/w/c/string/multibyte/wcstombs.html "c/string/multibyte/wcstombs") (C11) |  converts a wide string to narrow multibyte character string
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_wcstombs&action=edit)
Defined in header `[`<wchar.h>`](https://en.cppreference.com/w/c/header/wchar.html "c/header/wchar")`
[ mbsinit](https://en.cppreference.com/w/c/string/multibyte/mbsinit.html "c/string/multibyte/mbsinit") (C95) |  checks if the mbstate_t object represents initial shift state
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_mbsinit&action=edit)
[ btowc](https://en.cppreference.com/w/c/string/multibyte/btowc.html "c/string/multibyte/btowc") (C95) |  widens a single-byte narrow character to wide character, if possible
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_btowc&action=edit)
[ wctob](https://en.cppreference.com/w/c/string/multibyte/wctob.html "c/string/multibyte/wctob") (C95) |  narrows a wide character to a single-byte narrow character, if possible
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_wctob&action=edit)
[ mbrlen](https://en.cppreference.com/w/c/string/multibyte/mbrlen.html "c/string/multibyte/mbrlen") (C95) |  returns the number of bytes in the next multibyte character, given state
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_mbrlen&action=edit)
[ mbrtowc](https://en.cppreference.com/w/c/string/multibyte/mbrtowc.html "c/string/multibyte/mbrtowc") (C95) |  converts the next multibyte character to wide character, given state
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_mbrtowc&action=edit)
[ wcrtombwcrtomb_s](https://en.cppreference.com/w/c/string/multibyte/wcrtomb.html "c/string/multibyte/wcrtomb") (C95)(C11) |  converts a wide character to its multibyte representation, given state
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_wcrtomb&action=edit)
[ mbsrtowcsmbsrtowcs_s](https://en.cppreference.com/w/c/string/multibyte/mbsrtowcs.html "c/string/multibyte/mbsrtowcs") (C95)(C11) |  converts a narrow multibyte character string to wide string, given state
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_mbsrtowcs&action=edit)
[ wcsrtombswcsrtombs_s](https://en.cppreference.com/w/c/string/multibyte/wcsrtombs.html "c/string/multibyte/wcsrtombs") (C95)(C11) |  converts a wide string to narrow multibyte character string, given state
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_wcsrtombs&action=edit)
Defined in header `[`<uchar.h>`](https://en.cppreference.com/w/c/header/uchar.html "c/header/uchar")`
[ mbrtoc8](https://en.cppreference.com/w/c/string/multibyte/mbrtoc8.html "c/string/multibyte/mbrtoc8") (C23) |  converts a narrow multibyte character to UTF-8 encoding
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_mbrtoc8&action=edit)
[ c8rtomb](https://en.cppreference.com/w/c/string/multibyte/c8rtomb.html "c/string/multibyte/c8rtomb") (C23) |  converts UTF-8 string to narrow multibyte encoding
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_c8rtomb&action=edit)
[ mbrtoc16](https://en.cppreference.com/w/c/string/multibyte/mbrtoc16.html "c/string/multibyte/mbrtoc16") (C11) |  converts a narrow multibyte character to UTF-16 encoding
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_mbrtoc16&action=edit)
[ c16rtomb](https://en.cppreference.com/w/c/string/multibyte/c16rtomb.html "c/string/multibyte/c16rtomb") (C11) |  converts a UTF-16 character to narrow multibyte encoding
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_c16rtomb&action=edit)
[ mbrtoc32](https://en.cppreference.com/w/c/string/multibyte/mbrtoc32.html "c/string/multibyte/mbrtoc32") (C11) |  converts a narrow multibyte character to UTF-32 encoding
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_mbrtoc32&action=edit)
[ c32rtomb](https://en.cppreference.com/w/c/string/multibyte/c32rtomb.html "c/string/multibyte/c32rtomb") (C11) |  converts a UTF-32 character to narrow multibyte encoding
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_c32rtomb&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/string/multibyte&action=edit&section=2 "Edit section: Types")] Types
Defined in header `[`<uchar.h>`](https://en.cppreference.com/w/c/header/uchar.html "c/header/uchar")`
---
Defined in header `[`<wchar.h>`](https://en.cppreference.com/w/c/header/wchar.html "c/header/wchar")`
[ mbstate_t](https://en.cppreference.com/w/c/string/multibyte/mbstate_t.html "c/string/multibyte/mbstate t") (C95) |  conversion state information necessary to iterate multibyte character strings
(class) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_mbstate_t&action=edit)
Defined in header `[`<uchar.h>`](https://en.cppreference.com/w/c/header/uchar.html "c/header/uchar")`
[ char8_t](https://en.cppreference.com/w/c/string/multibyte/char8_t.html "c/string/multibyte/char8 t") (C23) |  8-bit character type
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_char8_t&action=edit)
[ char16_t](https://en.cppreference.com/w/c/string/multibyte/char16_t.html "c/string/multibyte/char16 t") (C11) |  16-bit character type
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_char16_t&action=edit)
[ char32_t](https://en.cppreference.com/w/c/string/multibyte/char32_t.html "c/string/multibyte/char32 t") (C11) |  32-bit character type
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_char32_t&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/string/multibyte&action=edit&section=3 "Edit section: Macros")] Macros
Defined in header `[`<limits.h>`](https://en.cppreference.com/w/c/header/limits.html "c/header/limits")`
---
MB_LEN_MAX |  maximum number of bytes in a multibyte character, for any supported locale
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_MB_LEN_MAX&action=edit)
Defined in header `[`<stdlib.h>`](https://en.cppreference.com/w/c/header/stdlib.html "c/header/stdlib")`
MB_CUR_MAX |  maximum number of bytes in a multibyte character, in the current locale
(macro variable) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/string/multibyte/dsc_MB_CUR_MAX&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/string/multibyte&action=edit&section=4 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 7.10 Sizes of integer types <limits.h> (p: TBD)


  * 7.22 General utilities <stdlib.h> (p: TBD)


  * 7.28 Unicode utilities <uchar.h> (p: TBD)


  * 7.29 Extended multibyte and wide character utilities <wchar.h> (p: TBD)


  * 7.31.12 General utilities <stdlib.h> (p: TBD)


  * 7.31.16 Extended multibyte and wide character utilities <wchar.h> (p: TBD)


  * K.3.6 General utilities <stdlib.h> (p: TBD)


  * K.3.9 Extended multibyte and wide character utilities <wchar.h> (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 7.10 Sizes of integer types <limits.h> (p: TBD)


  * 7.22 General utilities <stdlib.h> (p: TBD)


  * 7.28 Unicode utilities <uchar.h> (p: TBD)


  * 7.29 Extended multibyte and wide character utilities <wchar.h> (p: TBD)


  * 7.31.12 General utilities <stdlib.h> (p: TBD)


  * 7.31.16 Extended multibyte and wide character utilities <wchar.h> (p: TBD)


  * K.3.6 General utilities <stdlib.h> (p: TBD)


  * K.3.9 Extended multibyte and wide character utilities <wchar.h> (p: TBD)


  * C11 standard (ISO/IEC 9899:2011):


  * 7.10 Sizes of integer types <limits.h> (p: 222)


  * 7.22 General utilities <stdlib.h> (p: 340-360)


  * 7.28 Unicode utilities <uchar.h> (p: 398-401)


  * 7.29 Extended multibyte and wide character utilities <wchar.h> (p: 402-446)


  * 7.31.12 General utilities <stdlib.h> (p: 456)


  * 7.31.16 Extended multibyte and wide character utilities <wchar.h> (p: 456)


  * K.3.6 General utilities <stdlib.h> (p: 604-614)


  * K.3.9 Extended multibyte and wide character utilities <wchar.h> (p: 627-651)


  * C99 standard (ISO/IEC 9899:1999):


  * 7.10 Sizes of integer types <limits.h> (p: 203)


  * 7.20 General utilities <stdlib.h> (p: 306-324)


  * 7.24 Extended multibyte and wide character utilities <wchar.h> (p: 348-392)


  * 7.26.10 General utilities <stdlib.h> (p: 402)


  * 7.26.12 Extended multibyte and wide character utilities <wchar.h> (p: 402)


  * C89/C90 standard (ISO/IEC 9899:1990):


  * 4.1.4 Limits <float.h> and <limits.h>


  * 4.10 GENERAL UTILITIES <stdlib.h>


  * 4.13.7 General utilities <stdlib.h>


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/string/multibyte&action=edit&section=5 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/string/multibyte.html "cpp/string/multibyte") for Null-terminated multibyte strings
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/string/multibyte&oldid=180687](https://en.cppreference.com/mwiki/index.php?title=c/string/multibyte&oldid=180687)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/string/multibyte.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/string/multibyte "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/string/multibyte "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/string/multibyte&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/string/multibyte&oldid=180687 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/string/multibyte&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/string/multibyte "c/string/multibyte")
  * [Česky](http://cs.cppreference.com/w/c/string/multibyte "c/string/multibyte")
  * [Deutsch](http://de.cppreference.com/w/c/string/multibyte "c/string/multibyte")
  * [Español](http://es.cppreference.com/w/c/string/multibyte "c/string/multibyte")
  * [Français](http://fr.cppreference.com/w/c/string/multibyte "c/string/multibyte")
  * [Italiano](http://it.cppreference.com/w/c/string/multibyte "c/string/multibyte")
  * [日本語](http://ja.cppreference.com/w/c/string/multibyte "c/string/multibyte")
  * [한국어](http://ko.cppreference.com/w/c/string/multibyte "c/string/multibyte")
  * [Polski](http://pl.cppreference.com/w/c/string/multibyte "c/string/multibyte")
  * [Português](http://pt.cppreference.com/w/c/string/multibyte "c/string/multibyte")
  * [Русский](http://ru.cppreference.com/w/c/string/multibyte "c/string/multibyte")
  * [Türkçe](http://tr.cppreference.com/w/c/string/multibyte "c/string/multibyte")
  * [中文](http://zh.cppreference.com/w/c/string/multibyte "c/string/multibyte")


  * This page was last modified on 15 February 2025, at 00:32.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
