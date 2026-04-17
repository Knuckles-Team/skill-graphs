##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Ftypes&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Ftypes "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/types.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/w/Talk%253Ac/types.html "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/types.html)
##### Views
  * [View](https://en.cppreference.com/w/c/types.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/types&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/types&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/types.html)
# Type support
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")
[ C](https://en.cppreference.com/w/c.html "c")
[Compiler support](https://en.cppreference.com/w/c/compiler_support.html "c/compiler support")
---
[Language](https://en.cppreference.com/w/c/language.html "c/language")
[Headers](https://en.cppreference.com/w/c/header.html "c/header")
**Type support**
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
**Type support**
[size_t](https://en.cppreference.com/w/c/types/size_t.html "c/types/size t")
---
[ptrdiff_t](https://en.cppreference.com/w/c/types/ptrdiff_t.html "c/types/ptrdiff t")
[nullptr_t](https://en.cppreference.com/w/c/types/nullptr_t.html "c/types/nullptr t") (C23)
[NULL](https://en.cppreference.com/w/c/types/NULL.html "c/types/NULL")
[max_align_t](https://en.cppreference.com/w/c/types/max_align_t.html "c/types/max align t") (C11)
[offsetof](https://en.cppreference.com/w/c/types/offsetof.html "c/types/offsetof")
[ Numeric limits](https://en.cppreference.com/w/c/types/limits.html "c/types/limits")
[ Fixed width integer types](https://en.cppreference.com/w/c/types/integer.html "c/types/integer") (C99)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/types/navbar_content&action=edit)
See also [type system overview](https://en.cppreference.com/w/c/language/types.html "c/language/types") and [arithmetic types defined by the language](https://en.cppreference.com/w/c/language/arithmetic_types.html "c/language/arithmetic types").
## Contents
  * [1 Basic types](https://en.cppreference.com/w/c/types.html#Basic_types)
    * [1.1 Additional basic types and convenience macros](https://en.cppreference.com/w/c/types.html#Additional_basic_types_and_convenience_macros)
    * [1.2 Fixed width integer types (since C99)](https://en.cppreference.com/w/c/types.html#Fixed_width_integer_types_.28since_C99.29)
    * [1.3 Numeric limits](https://en.cppreference.com/w/c/types.html#Numeric_limits)
  * [2 Notes](https://en.cppreference.com/w/c/types.html#Notes)
  * [3 Example](https://en.cppreference.com/w/c/types.html#Example)
  * [4 References](https://en.cppreference.com/w/c/types.html#References)
  * [5 See also](https://en.cppreference.com/w/c/types.html#See_also)


---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/types&action=edit&section=1 "Edit section: Basic types")] Basic types
####  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/types&action=edit&section=2 "Edit section: Additional basic types and convenience macros")] Additional basic types and convenience macros
Defined in header `[`<stddef.h>`](https://en.cppreference.com/w/c/header/stddef.html "c/header/stddef")`
---
[ size_t](https://en.cppreference.com/w/c/types/size_t.html "c/types/size t") |  unsigned integer type returned by the [`sizeof`](https://en.cppreference.com/w/c/language/sizeof.html "c/language/sizeof") operator
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/types/dsc_size_t&action=edit)
[ ptrdiff_t](https://en.cppreference.com/w/c/types/ptrdiff_t.html "c/types/ptrdiff t") |  signed integer type returned when subtracting two pointers
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/types/dsc_ptrdiff_t&action=edit)
[ nullptr_t](https://en.cppreference.com/w/c/types/nullptr_t.html "c/types/nullptr t") (C23) |  the type of the predefined null pointer constant [`nullptr`](https://en.cppreference.com/w/c/language/nullptr.html "c/language/nullptr")
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/types/dsc_nullptr_t&action=edit)
[ NULL](https://en.cppreference.com/w/c/types/NULL.html "c/types/NULL") |  implementation-defined null pointer constant
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/types/dsc_NULL&action=edit)
[ max_align_t](https://en.cppreference.com/w/c/types/max_align_t.html "c/types/max align t") (C11) |  a type with alignment requirement as great as any other scalar type
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/types/dsc_max_align_t&action=edit)
[ offsetof](https://en.cppreference.com/w/c/types/offsetof.html "c/types/offsetof") |  byte offset from the beginning of a struct type to specified member
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/types/dsc_offsetof&action=edit)
Defined in header `[`<stdbool.h>`](https://en.cppreference.com/w/c/header/stdbool.html "c/header/stdbool")`
bool (C99)(removed in C23) |  convenience macro, expands to [`_Bool`](https://en.cppreference.com/w/c/keyword/_Bool.html "c/keyword/ Bool")
(keyword macro)
true (C99)(removed in C23) |  expands to integer constant 1
(macro constant)
false (C99)(removed in C23) |  expands to integer constant ​0​
(macro constant)
__bool_true_false_are_defined (C99)(deprecated in C23) |  expands to integer constant 1
(macro constant)
Defined in header `[`<stdalign.h>`](https://en.cppreference.com/w/c/header/stdalign.html "c/header/stdalign")`
alignas (C11)(removed in C23) |  convenience macro, expands to keyword [`_Alignas`](https://en.cppreference.com/w/c/keyword/_Alignas.html "c/keyword/ Alignas")
(keyword macro)
alignof (C11)(removed in C23) |  convenience macro, expands to keyword [`_Alignof`](https://en.cppreference.com/w/c/keyword/_Alignof.html "c/keyword/ Alignof")
(keyword macro)
__alignas_is_defined (C11)(removed in C23) |  expands to integer constant 1
(macro constant)
__alignof_is_defined (C11)(removed in C23) |  expands to integer constant 1
(macro constant)
Defined in header `[`<stdnoreturn.h>`](https://en.cppreference.com/w/c/header/stdnoreturn.html "c/header/stdnoreturn")`
noreturn (C11)(deprecated in C23) |  convenience macro, expands to [`_Noreturn`](https://en.cppreference.com/w/c/keyword/_Noreturn.html "c/keyword/ Noreturn")
(keyword macro)
####  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/types&action=edit&section=3 "Edit section: Fixed width integer types \(since C99\)")] [Fixed width integer types](https://en.cppreference.com/w/c/types/integer.html "c/types/integer") (since C99)
####  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/types&action=edit&section=4 "Edit section: Numeric limits")] [Numeric limits](https://en.cppreference.com/w/c/types/limits.html "c/types/limits")
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/types&action=edit&section=5 "Edit section: Notes")] Notes
The type of true and false is int rather than _Bool.  A program may undefine and perhaps then redefine the macros bool, true and false. However, such ability is a deprecated feature.  |  (since C99)
(until C23)
---|---
The type of true and false is bool. It is unspecified whether any of bool, _Bool, true, or false is implemented as a predefined macro.  If bool, true, or false (but not _Bool) is defined as a predefined macro, a program may undefine and perhaps redefine it.  | (since C23)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/types&action=edit&section=6 "Edit section: Example")] Example
Run this code
```
#include <stdalign.h>
#include <stdbool.h>
#include <stdio.h>
 
int main(void)
{
    [printf](https://en.cppreference.com/w/c/io/fprintf.html)("%d %d %d\n", true && false, true || false, !false);
    [printf](https://en.cppreference.com/w/c/io/fprintf.html)("%d %d\n", true ^ true, true + true);
    [printf](https://en.cppreference.com/w/c/io/fprintf.html)("%zu\n", alignof(short));
}
```

Possible output:
```
0 1 1
0 2
2
```

###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/types&action=edit&section=7 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 7.15 Alignment <stdalign.h> (p: TBD)


  * 7.18 Boolean type and values <stdbool.h> (p: TBD)


  * 7.19 Common definitions <stddef.h> (p: TBD)


  * 7.23 _Noreturn <stdnoreturn.h> (p: TBD)


  * 7.31.9 Boolean type and values <stdbool.h> (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 7.15 Alignment <stdalign.h> (p: 196)


  * 7.18 Boolean type and values <stdbool.h> (p: 210)


  * 7.19 Common definitions <stddef.h> (p: 211)


  * 7.23 _Noreturn <stdnoreturn.h> (p: 263)


  * 7.31.9 Boolean type and values <stdbool.h> (p: 332)


  * C11 standard (ISO/IEC 9899:2011):


  * 7.15 Alignment <stdalign.h> (p: 268)


  * 7.18 Boolean type and values <stdbool.h> (p: 287)


  * 7.19 Common definitions <stddef.h> (p: 288)


  * 7.23 _Noreturn <stdnoreturn.h> (p: 361)


  * 7.31.9 Boolean type and values <stdbool.h> (p: 456)


  * C99 standard (ISO/IEC 9899:1999):


  * 7.18 Boolean type and values <stdbool.h> (p: 253)


  * 7.19 Common definitions <stddef.h> (p: 254)


  * 7.26.7 Boolean type and values <stdbool.h> (p: 401)


  * C89/C90 standard (ISO/IEC 9899:1990):


  * 4.1.5 Common definitions <stddef.h>


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/types&action=edit&section=8 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/utility/rtti.html "cpp/types") for Type support library
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/types&oldid=180056](https://en.cppreference.com/mwiki/index.php?title=c/types&oldid=180056)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/types.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/types "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/types "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/types&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/types&oldid=180056 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/types&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/types "c/types")
  * [Česky](http://cs.cppreference.com/w/c/types "c/types")
  * [Deutsch](http://de.cppreference.com/w/c/types "c/types")
  * [Español](http://es.cppreference.com/w/c/types "c/types")
  * [Français](http://fr.cppreference.com/w/c/types "c/types")
  * [Italiano](http://it.cppreference.com/w/c/types "c/types")
  * [日本語](http://ja.cppreference.com/w/c/types "c/types")
  * [한국어](http://ko.cppreference.com/w/c/types "c/types")
  * [Polski](http://pl.cppreference.com/w/c/types "c/types")
  * [Português](http://pt.cppreference.com/w/c/types "c/types")
  * [Русский](http://ru.cppreference.com/w/c/types "c/types")
  * [Türkçe](http://tr.cppreference.com/w/c/types "c/types")
  * [中文](http://zh.cppreference.com/w/c/types "c/types")


  * This page was last modified on 2 February 2025, at 05:58.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
