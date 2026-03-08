##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fcompiler+support&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fcompiler+support "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/compiler_support.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/mwiki/index.php?title=Talk:c/compiler_support&action=edit&redlink=1 "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/compiler_support.html)
##### Views
  * [View](https://en.cppreference.com/w/c/compiler_support.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/compiler_support.html)
# C compiler support
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")
[ C](https://en.cppreference.com/w/c.html "c")
**Compiler support**
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
**Compiler support**
[ C99](https://en.cppreference.com/w/c/compiler_support/99.html "c/compiler support/99")
---
[ C23](https://en.cppreference.com/w/c/compiler_support/23.html "c/compiler support/23")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/compiler_support/navbar_content&action=edit)
![](https://upload.cppreference.com/mwiki/images/3/31/Imbox_notice.png) |  This page is maintained as best-effort and may lag behind most recent compiler releases. If you see something is out-of-date, please help us by updating it!
---|---
## Contents
  * [1 C23 features](https://en.cppreference.com/w/c/compiler_support.html#C23_features)
    * [1.1 C23 core language features](https://en.cppreference.com/w/c/compiler_support.html#C23_core_language_features)
    * [1.2 C23 library features](https://en.cppreference.com/w/c/compiler_support.html#C23_library_features)
  * [2 C99 features](https://en.cppreference.com/w/c/compiler_support.html#C99_features)
    * [2.1 C99 core language features](https://en.cppreference.com/w/c/compiler_support.html#C99_core_language_features)
    * [2.2 See also](https://en.cppreference.com/w/c/compiler_support.html#See_also)


---
##  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support&action=edit&section=1 "Edit section: C23 features")] C23 features
Note that this list may change, as the draft C23/2x standard evolves.
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/compiler_support/23&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=Template:c/compiler_support/23&action=edit&section=T-1 "Template:c/compiler support/23")] C23 core language features
| This section is incomplete
Reason: status for Apple Clang and other compilers supporting C2x
---|---
C23 feature

| Paper(s)

|  GCC |  Clang |  MSVC |  Apple Clang |  EDG eccp |  Intel C++ |  Nvidia HPC C++ (ex PGI)* |  Nvidia nvcc |  Cray |
---|---|---|---|---|---|---|---|---|---|---|---
[`static_assert`](https://en.cppreference.com/w/c/language/static_assert.html "c/language/ Static assert") with no message  |  | 9  | 9  | Yes  | Yes  | 6.5  | 2021.1.2 (clang based)  |  |  |
`[[nodiscard[](https://en.cppreference.com/w/c/language/attributes/nodiscard.html "c/language/attributes/nodiscard")]]` |  | 10  | 9  |  | Yes  | 6.4  | 2021.1.2 (clang based)  |  |  |
`[[maybe_unused[](https://en.cppreference.com/w/c/language/attributes/maybe_unused.html "c/language/attributes/maybe unused")]]` |  | 10  | 9  |  | Yes  | 6.4  | 2021.1.2 (clang based)  |  |  |
`[[deprecated[](https://en.cppreference.com/w/c/language/attributes/deprecated.html "c/language/attributes/deprecated")]]` |  | 10  | 9  |  | Yes  | 6.4  | 2021.1.2 (clang based)  |  |  |
[Attributes](https://en.cppreference.com/w/c/language/attributes.html "c/language/attributes") |
| 10  | 9  |  | Yes  | 6.4  | 2021.1.2 (clang based)  |  |  |
IEEE 754 decimal floating-point types  |  | 4.2 (partial)*
12  |  |  |  |  | 13.0 (partial)* |  |  |
`[[fallthrough[](https://en.cppreference.com/w/c/language/attributes/fallthrough.html "c/language/attributes/fallthrough")]]` |  | 10  | 9  |  | Yes  | 6.4  | 2021.1.2 (clang based)  |  |  |
[`u8` character constants](https://en.cppreference.com/w/c/language/character_constant.html "c/language/character constant") |  | 10  | 15  |  |  | 6.5  | 2022.2  |  |  |
Removal of [function definitions](https://en.cppreference.com/w/c/language/function_definition.html "c/language/function definition") without prototype  |  | 10  | 15  |  |  |  | 2022.2  |  |  |
`[[nodiscard[](https://en.cppreference.com/w/c/language/attributes/nodiscard.html "c/language/attributes/nodiscard")]]` with message  |  | 11  | 10  |  | Yes  | 6.4  | 2021.1.2 (clang based)  |  |  |
Unnamed parameters in function definitions  |  | 11  | 11  |  | Yes  | 6.4  | 2021.1.2 (clang based)  |  |  |
[Labels](https://en.cppreference.com/w/c/language/statements.html#Labels "c/language/statements") before declarations and end of blocks  |  | 11  | 16  |  Partial* |  | 6.5  | 17.0* |  |  |
[Binary integer constants](https://en.cppreference.com/w/c/language/integer_constant.html "c/language/integer constant") |  | 4.3*
11  | 2.9*
9  |  19.0 (2015)** | Yes  | 6.5  | 11.0* |  |  |
[`__has_c_attribute`](https://en.cppreference.com/w/c/language/attributes.html#Attribute_testing "c/language/attributes") in preprocessor conditionals  |  | 11  | 9  |  | Yes  | 6.5  | 2021.1.2 (clang based)  |  |  |
Allow duplicate attributes  |  | 11  | 13  |  | Yes  | 6.5  | 2021.4 (clang-based  |  |  |
IEEE 754 interchange and extended types  |  | 7 (partial)*
14  | 6 (partial)* |  |  Partial* |  |  |  |  |
Digit separators  |  | 12  | 13  |  19.0 (2015)** | Yes  | 6.5  | 18.0* |  |  |
[`#elifdef` and `#elifndef`](https://en.cppreference.com/w/c/preprocessor/conditional.html "c/preprocessor/conditional") |  | 12  | 13  |  19.40* |  13.1.6* | 6.5  | 2021.4  |  |  |
Type change of [`u8` string literals](https://en.cppreference.com/w/c/language/string_literal.html "c/language/string literal") |  | 13  |  |  |  |  |  |  |  |
`[[maybe_unused[](https://en.cppreference.com/w/c/language/attributes/maybe_unused.html "c/language/attributes/maybe unused")]]` for labels  |  | 11  | 16  |  |  | 6.5  | 2022.2  |  |  |
[` #warning`](https://en.cppreference.com/w/c/preprocessor/warning.html "c/preprocessor/error") |  | Yes  | Yes  |  | Yes  | 6.5  | Yes  |  |  |
Bit-precise integer types (_BitInt)  |  | 14 (partial)* | 15  |  |  | 6.5  | 2022.2  |  |  |
`[[noreturn[](https://en.cppreference.com/w/c/language/attributes/noreturn.html "c/language/attributes/noreturn")]]` |  | 13  | 15  |  |  | 6.5  | 2022.2  |  |  |
Suffixes for bit-precise integer constants  |  | 14  | 15  |  |  |  | 2022.2  |  |  |
[`__has_include`](https://en.cppreference.com/w/c/preprocessor/include.html "c/preprocessor/include") in preprocessor conditionals  |  | 5  | Yes  |  19.11* | Yes  | 6.5  | 18.0  |  |  |
Identifier Syntax using Unicode Standard Annex 31  |  | 13  | 15  |  |  | 6.5  | 2022.2  |  |  |
Removal of [function declarations](https://en.cppreference.com/w/c/language/function_declaration.html "c/language/function declaration") without prototype  |  | 13  | 15  |  |  |  | 2022.2  |  |  |
[Empty initializers](https://en.cppreference.com/w/c/language/initialization.html#Empty_initialization "c/language/initialization") |  |  Partial*
13  |  Partial* |  |  Partial* |  Partial* |  Partial* |  |  |
[`typeof`](https://en.cppreference.com/w/c/language/typeof_unqual.html "c/language/typeof") and [`typeof_unqual`](https://en.cppreference.com/w/c/language/typeof_unqual.html "c/language/typeof") |
|  Partial*
13  |  Partial*
16  |  19.39* |  Partial* |  Partial* |  Partial* |  |  |  Partial*
New spelling of keywords  |  | 13  | 16  |  |  | 6.5  |  |  |  |
Predefined [true and false](https://en.cppreference.com/w/c/language/bool_constant.html "c/language/bool constant") |  | 13  | 15  |  |  |  | 2022.2  |  |  |
`[[unsequenced[](https://en.cppreference.com/w/c/language/attributes/reproducible.html "c/language/attributes/unsequenced")]]` and `[[reproducible[](https://en.cppreference.com/w/c/language/attributes/reproducible.html "c/language/attributes/reproducible")]]` |  | 15  |  |  |  |  |  |  |  |
Relax requirements for [variadic parameter list](https://en.cppreference.com/w/c/language/variadic.html "c/language/variadic") |  | 13  | 16  |  |  | 6.5  | 2023.1  |  |  |
Type inference in object definitions  |  | 13  | 18  |  |  |  |  |  |  |
[` #embed`](https://en.cppreference.com/w/c/preprocessor/embed.html "c/preprocessor/embed") |  | 15  | 19  |  |  |  |  |  |  |
[`constexpr`](https://en.cppreference.com/w/c/language/constexpr.html "c/language/constexpr") objects  |  | 13  | 19  |  |  |  |  |  |  |
Improved Normal Enumerations  |  | 13  | 20* |  |  |  |  |  |  |
Enumerations with fixed underlying types  |  | 13  | 20* |  |  |  |  |  |  |
[`__VA_OPT__`](https://en.cppreference.com/w/c/preprocessor/replace.html#Function-like_macros "c/preprocessor/replace") |  | 8
13  | 12  |  19.39* |  | 6.5  |  |  |  |
Storage-class specifiers for compound literals  |  | 13  |  |  |  |  |  |  |  |
[`nullptr`](https://en.cppreference.com/w/c/language/nullptr.html "c/language/nullptr") |  | 13  | 16  |  |  |  |  |  |  |


C23 feature  |

Paper(s)  |  GCC |  Clang |  MSVC |  Apple Clang |  EDG eccp |  Intel C++ |  Nvidia HPC C++ (ex PGI)* |  Nvidia nvcc |  Cray
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=Template:c/compiler_support/23&action=edit&section=T-2 "Template:c/compiler support/23")] C23 library features
| This section is incomplete
Reason: a different list for C standard libraries
---|---
##  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support&action=edit&section=2 "Edit section: C99 features")] C99 features
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/compiler_support/99&action=edit)
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


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support&action=edit&section=3 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/compiler_support.html "cpp/compiler support") for compiler support
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/compiler_support&oldid=145580](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support&oldid=145580)"
[Category](https://en.cppreference.com/w/Special:Categories "Special:Categories"):
  * [Todo with reason](https://en.cppreference.com/w/Category%253ATodo_with_reason.html "Category:Todo with reason")


##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/compiler_support.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/compiler_support "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/compiler_support "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support&oldid=145580 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/compiler_support&action=info)


  * In other languages


  * [Español](http://es.cppreference.com/w/c/compiler_support "c/compiler support")
  * [日本語](http://ja.cppreference.com/w/c/compiler_support "c/compiler support")
  * [Polski](http://pl.cppreference.com/w/c/compiler_support "c/compiler support")
  * [Русский](http://ru.cppreference.com/w/c/compiler_support "c/compiler support")
  * [中文](http://zh.cppreference.com/w/c/compiler_support "c/compiler support")


  * This page was last modified on 11 December 2022, at 19:41.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
