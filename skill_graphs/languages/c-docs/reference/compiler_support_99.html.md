##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fcompiler+support%2F99&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fcompiler+support%2F99 "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/compiler_support/99.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/mwiki/index.php?title=Talk:c/compiler_support/99&action=edit&redlink=1 "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/compiler_support/99.html)
##### Views
  * [View](https://en.cppreference.com/w/c/compiler_support/99.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support/99&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support/99&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/compiler_support/99.html)
# Compiler support for C99
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")‎ | [compiler support](https://en.cppreference.com/w/c/compiler_support.html "c/compiler support")
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
[Compiler support](https://en.cppreference.com/w/c/compiler_support.html "c/compiler support")
**C99**
---
[ C23](https://en.cppreference.com/w/c/compiler_support/23.html "c/compiler support/23")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/compiler_support/navbar_content&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=Template:c/compiler_support/99&action=edit&section=T-1 "Template:c/compiler support/99")] C99 core language features
| This section is incomplete
Reason: needs to list C compilers, verification
---|---
C99 feature

| Paper(s)

|  GCC |  Clang |  MSVC |  Apple Clang |  EDG eccp |  Intel C++ |  Nvidia HPC C++ (ex PGI)* |  Nvidia nvcc |  Cray |
---|---|---|---|---|---|---|---|---|---|---|---
Universal-character-names in [identifiers](https://en.cppreference.com/w/c/language/identifiers.html "c/language/identifier") |  | 3.1  | Yes  | Yes  |  |  |  |  |  |
Increased [translation limits](https://en.cppreference.com/w/c/language/identifiers.html#Translation_limits "c/language/identifier") |  | 0.9  |  N/A |  |  |  |  |  |  |
// [comments](https://en.cppreference.com/w/c/comment.html "c/comment") |  | 2.7  | Yes  | Yes  |  |  |  |  |  |
[`restrict`](https://en.cppreference.com/w/c/language/restrict.html "c/language/restrict") pointers  |  | 2.95  | Yes  | partial* |  |  |  |  |  |
Enhanced [arithmetic types](https://en.cppreference.com/w/c/language/arithmetic_types.html "c/language/arithmetic types") |





| Yes  | partial  | Maybe  |  |  |  |  |  |
Flexible array members  |  | 3.0  | Yes  | Yes  |  |  |  |  |  |
[Variable-length array](https://en.cppreference.com/w/c/language/array.html#Variable-length_arrays "c/language/array") (VLA) types  |  | 0.9  | Yes  |  |  |  |  |  |  |
Variably-modified (VM) types  |  |  N/A | Yes  |  |  |  |  |  |  |
Designated initializers  |  | 3.0  | Yes  | Yes  |  |  |  |  |  |
Non-constant initializers  |  | 1.21  |  N/A |  |  |  |  |  |  |
Idempotent cvr-qualifiers  |  | 3.0  |  N/A |  |  |  |  |  |  |
Trailing comma in [enumerator-list](https://en.cppreference.com/w/c/language/enum.html "c/language/enum") |  | 0.9  | Yes  | Yes  |  |  |  |  |  |
Hexadecimal [floating constants](https://en.cppreference.com/w/c/language/floating_constant.html "c/language/floating constant") |  | 2.8  | Yes  | Yes  |  |  |  |  |  |
[Compound literals](https://en.cppreference.com/w/c/language/compound_literal.html "c/language/compound literal") |  | 3.1  | Yes  | Yes  |  |  |  |  |  |
Floating-point environment  |  | partial  | partial  |  |  |  |  |  |  |
Requiring truncation for divisions of signed integer types  |  | 0.9  |  N/A |  |  |  |  |  |  |
Implicit return 0; in the [`main()` function](https://en.cppreference.com/w/c/language/main_function.html "c/language/main function") |  | Yes  | Yes  | Yes  |  |  |  |  |  |
Declarations and statements in mixed order  |  | 3.0  | Yes  | Yes  |  |  |  |  |  |
init-statement in [`for`](https://en.cppreference.com/w/c/language/for.html "c/language/for") loops  |  | Yes  | Yes  | Yes  |  |  |  |  |  |
[`inline`](https://en.cppreference.com/w/c/language/inline.html "c/language/inline") functions  |  | 4.3  | Yes  | Yes  |  |  |  |  |  |
Predefined variable [`__func__`](https://en.cppreference.com/w/c/language/function_definition.html "c/language/function definition") |  | 2.95  | Yes  | Yes  |  |  |  |  |  |
Cvr-qualifiers and static in [] within function declarations  |  | 3.1  | Yes  |  |  |  |  |  |  |
[Variadic macros](https://en.cppreference.com/w/c/preprocessor/replace.html "c/preprocessor/replace") |  | 2.95  | Yes  | Yes  |  |  |  |  |  |
[`_Pragma`](https://en.cppreference.com/w/c/preprocessor/impl.html "c/preprocessor/impl") preprocessor operator  |  | 3.0  | Yes  | partial* |  |  |  |  |  |
Standard pragmas for floating-point evaluation  |
|  No  |  No  |  |  |  |  |  |  |


C99 feature  |

Paper(s)  |  GCC |  Clang |  MSVC |  Apple Clang |  EDG eccp |  Intel C++ |  Nvidia HPC C++ (ex PGI)* |  Nvidia nvcc |  Cray
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/compiler_support/99&oldid=145576](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support/99&oldid=145576)"
[Category](https://en.cppreference.com/w/Special:Categories "Special:Categories"):
  * [Todo with reason](https://en.cppreference.com/w/Category%253ATodo_with_reason.html "Category:Todo with reason")


##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/compiler_support/99.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/compiler_support/99 "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/compiler_support/99 "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support/99&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support/99&oldid=145576 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support/99&action=info)


  * In other languages


  * [Deutsch](http://de.cppreference.com/w/c/compiler_support/99 "c/compiler support/99")
  * [Español](http://es.cppreference.com/w/c/compiler_support/99 "c/compiler support/99")
  * [Français](http://fr.cppreference.com/w/c/compiler_support/99 "c/compiler support/99")
  * [Italiano](http://it.cppreference.com/w/c/compiler_support/99 "c/compiler support/99")
  * [日本語](http://ja.cppreference.com/w/c/compiler_support/99 "c/compiler support/99")
  * [Português](http://pt.cppreference.com/w/c/compiler_support/99 "c/compiler support/99")
  * [Polski](http://pl.cppreference.com/w/c/compiler_support/99 "c/compiler support/99")
  * [Русский](http://ru.cppreference.com/w/c/compiler_support/99 "c/compiler support/99")
  * [中文](http://zh.cppreference.com/w/c/compiler_support/99 "c/compiler support/99")


  * This page was last modified on 11 December 2022, at 19:29.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
