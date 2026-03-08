##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fpreprocessor&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fpreprocessor "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/preprocessor.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/mwiki/index.php?title=Talk:c/preprocessor&action=edit&redlink=1 "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/preprocessor.html)
##### Views
  * [View](https://en.cppreference.com/w/c/preprocessor.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/preprocessor.html)
# Preprocessor
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
[Localization support](https://en.cppreference.com/w/c/locale.html "c/locale")
[Concurrency support](https://en.cppreference.com/w/c/thread.html "c/thread") (C11)
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[Symbol index](https://en.cppreference.com/w/c/index.html "c/symbol index")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/navbar_content&action=edit)
[ C language](https://en.cppreference.com/w/c/language.html "c/language")
[Basic concepts](https://en.cppreference.com/w/c/language/basic_concepts.html "c/language/basic concepts")
---
[ Keywords](https://en.cppreference.com/w/c/keyword.html "c/keyword")
**Preprocessor**
[ Statements](https://en.cppreference.com/w/c/language/statements.html "c/language/statements")
[ Expressions](https://en.cppreference.com/w/c/language/operators.html "c/language/expressions")
[ Initialization](https://en.cppreference.com/w/c/language/initialization.html "c/language/initialization")
[ Declarations](https://en.cppreference.com/w/c/language/declarations.html "c/language/declarations")
[ Functions](https://en.cppreference.com/w/c/language/functions.html "c/language/functions")
Miscellaneous
[ History of C](https://en.cppreference.com/w/c/language/history.html "c/language/history")
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/language/navbar_content&action=edit)
**Preprocessor**
[#if#ifdef#ifndef#else#elif#elifdef#elifndef#endif](https://en.cppreference.com/w/c/preprocessor/conditional.html "c/preprocessor/conditional") (C23)(C23)
---
[#define#undef#,## operators](https://en.cppreference.com/w/c/preprocessor/replace.html "c/preprocessor/replace")
[#include__has_include](https://en.cppreference.com/w/c/preprocessor/include.html "c/preprocessor/include") (C23)
[#error#warning](https://en.cppreference.com/w/c/preprocessor/warning.html "c/preprocessor/error") (C23)
[#pragma_Pragma](https://en.cppreference.com/w/c/preprocessor/impl.html "c/preprocessor/impl") (C99)
[#line](https://en.cppreference.com/w/c/preprocessor/line.html "c/preprocessor/line")
[#embed__has_embed](https://en.cppreference.com/w/c/preprocessor/embed.html "c/preprocessor/embed") (C23)(C23)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/preprocessor/navbar_content&action=edit)
The preprocessor is executed at [translation phase 4](https://en.cppreference.com/w/c/language/translation_phases.html#Phase_4 "c/language/translation phases"), before the compilation. The result of preprocessing is a single file which is then passed to the actual compiler.
## Contents
  * [1 Directives](https://en.cppreference.com/w/c/preprocessor.html#Directives)
  * [2 Capabilities](https://en.cppreference.com/w/c/preprocessor.html#Capabilities)
  * [3 Footnotes](https://en.cppreference.com/w/c/preprocessor.html#Footnotes)
  * [4 Example](https://en.cppreference.com/w/c/preprocessor.html#Example)
  * [5 References](https://en.cppreference.com/w/c/preprocessor.html#References)
  * [6 See also](https://en.cppreference.com/w/c/preprocessor.html#See_also)


---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&action=edit&section=1 "Edit section: Directives")] Directives
The preprocessing directives control the behavior of the preprocessor. Each directive occupies one line and has the following format:
  * `#` character
  * preprocessing instruction (one of `define`, `undef`, `include`, `if`, `ifdef`, `ifndef`, `else`, `elif`, `elifdef`, `elifndef`(since C23), `endif`, `line`, `embed`(since C23), `error`, `warning`(since C23), `pragma`) [[1]](https://en.cppreference.com/w/c/preprocessor.html#cite_note-1)
  * arguments (depends on the instruction)
  * line break.


The null directive (`#` followed by a line break) is allowed and has no effect.
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&action=edit&section=2 "Edit section: Capabilities")] Capabilities
The preprocessor has the source file translation capabilities:
  * **[conditionally](https://en.cppreference.com/w/c/preprocessor/conditional.html "c/preprocessor/conditional")** compile of parts of source file (controlled by directive `#if`, `#ifdef`, `#ifndef`, `#else`, `#elif`, `#elifdef`, `#elifndef`(since C23) and `#endif`).
  * **[replace](https://en.cppreference.com/w/c/preprocessor/replace.html "c/preprocessor/replace")** text macros while possibly concatenating or quoting identifiers (controlled by directives `#define` and `#undef`, and operators `#` and `##`)
  * **[include](https://en.cppreference.com/w/c/preprocessor/include.html "c/preprocessor/include")** other files (controlled by directive `#include` and checked with `__has_include`(since C23))
  * cause an **[error](https://en.cppreference.com/w/c/preprocessor/warning.html "c/preprocessor/error")** or **[warning](https://en.cppreference.com/w/c/preprocessor/warning.html "c/preprocessor/error")**(since C23) (controlled by directive `#error` or `#warning` respectively(since C23))


The following aspects of the preprocessor can be controlled:
  * **[implementation defined](https://en.cppreference.com/w/c/preprocessor/impl.html "c/preprocessor/impl")** behavior (controlled by directive `#pragma` and operator `_Pragma`(since C99))
  * **[file name and line information](https://en.cppreference.com/w/c/preprocessor/line.html "c/preprocessor/line")** available to the preprocessor (controlled by directives `#line`)


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&action=edit&section=3 "Edit section: Footnotes")] Footnotes
  1. [↑](https://en.cppreference.com/w/c/preprocessor.html#cite_ref-1) These are the directives defined by the standard. The standard does not define behavior for other directives: they might be ignored, have some useful meaning, or make the program ill-formed. Even if otherwise ignored, they are removed from the source code when the preprocessor is done. A common non-standard extension is the directive [#warning](https://en.cppreference.com/w/c/preprocessor/warning.html "c/preprocessor/error") which emits a user-defined message during compilation.(until C23)


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&action=edit&section=4 "Edit section: Example")] Example
| This section is incomplete
Reason: no example
---|---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&action=edit&section=5 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 6.10 Preprocessing directives (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 6.10 Preprocessing directives (p: 117-129)


  * C11 standard (ISO/IEC 9899:2011):


  * 6.10 Preprocessing directives (p: 160-178)


  * C99 standard (ISO/IEC 9899:1999):


  * 6.10 Preprocessing directives (p: 145-162)


  * C89/C90 standard (ISO/IEC 9899:1990):


  * 3.8 Preprocessing directives


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&action=edit&section=6 "Edit section: See also")] See also
[C documentation](https://en.cppreference.com/w/c/preprocessor/replace.html#Predefined_macros "c/preprocessor/replace") for Predefined Macro Symbols
---
[C documentation](https://en.cppreference.com/w/c/symbol_index/macro.html "c/symbol index/macro") for Macro Symbol Index
[C++ documentation](https://en.cppreference.com/w/cpp/preprocessor.html "cpp/preprocessor") for Preprocessor
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&oldid=179530](https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&oldid=179530)"
[Category](https://en.cppreference.com/w/Special:Categories "Special:Categories"):
  * [Todo no example](https://en.cppreference.com/w/Category%253ATodo_no_example.html "Category:Todo no example")


##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/preprocessor.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/preprocessor "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/preprocessor "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&oldid=179530 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/preprocessor&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/preprocessor "c/preprocessor")
  * [Česky](http://cs.cppreference.com/w/c/preprocessor "c/preprocessor")
  * [Deutsch](http://de.cppreference.com/w/c/preprocessor "c/preprocessor")
  * [Español](http://es.cppreference.com/w/c/preprocessor "c/preprocessor")
  * [Français](http://fr.cppreference.com/w/c/preprocessor "c/preprocessor")
  * [Italiano](http://it.cppreference.com/w/c/preprocessor "c/preprocessor")
  * [日本語](http://ja.cppreference.com/w/c/preprocessor "c/preprocessor")
  * [한국어](http://ko.cppreference.com/w/c/preprocessor "c/preprocessor")
  * [Polski](http://pl.cppreference.com/w/c/preprocessor "c/preprocessor")
  * [Português](http://pt.cppreference.com/w/c/preprocessor "c/preprocessor")
  * [Русский](http://ru.cppreference.com/w/c/preprocessor "c/preprocessor")
  * [Türkçe](http://tr.cppreference.com/w/c/preprocessor "c/preprocessor")
  * [中文](http://zh.cppreference.com/w/c/preprocessor "c/preprocessor")


  * This page was last modified on 12 January 2025, at 15:20.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
