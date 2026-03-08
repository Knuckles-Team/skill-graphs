##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Flanguage%2Fbasic+concepts&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Flanguage%2Fbasic+concepts "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/language/basic_concepts.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/w/Talk%253Ac/language/basic_concepts.html "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/language/basic_concepts.html)
##### Views
  * [View](https://en.cppreference.com/w/c/language/basic_concepts.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/language/basic_concepts&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/language/basic_concepts&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/language/basic_concepts.html)
# Basic concepts
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")‎ | [language](https://en.cppreference.com/w/c/language.html "c/language")
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
**Basic concepts**
---
[ Keywords](https://en.cppreference.com/w/c/keyword.html "c/keyword")
[ Preprocessor](https://en.cppreference.com/w/c/preprocessor.html "c/preprocessor")
[ Statements](https://en.cppreference.com/w/c/language/statements.html "c/language/statements")
[ Expressions](https://en.cppreference.com/w/c/language/operators.html "c/language/expressions")
[ Initialization](https://en.cppreference.com/w/c/language/initialization.html "c/language/initialization")
[ Declarations](https://en.cppreference.com/w/c/language/declarations.html "c/language/declarations")
[ Functions](https://en.cppreference.com/w/c/language/functions.html "c/language/functions")
Miscellaneous
[ History of C](https://en.cppreference.com/w/c/language/history.html "c/language/history")
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/language/navbar_content&action=edit)
**Basic Concepts**
[ Comments](https://en.cppreference.com/w/c/comment.html "c/comment")
---
[ ASCII](https://en.cppreference.com/w/c/language/ascii.html "c/language/ascii")
[ Character sets](https://en.cppreference.com/w/c/language/charset.html "c/language/charset")
[ Translation phases](https://en.cppreference.com/w/c/language/translation_phases.html "c/language/translation phases")
[Punctuation](https://en.cppreference.com/w/c/language/punctuators.html "c/language/punctuators")
[Identifier](https://en.cppreference.com/w/c/language/identifiers.html "c/language/identifier")
[Scope](https://en.cppreference.com/w/c/language/scope.html "c/language/scope")
[Lifetime](https://en.cppreference.com/w/c/language/lifetime.html "c/language/lifetime")
[Lookup and name spaces](https://en.cppreference.com/w/c/language/name_space.html "c/language/name space")
[Type](https://en.cppreference.com/w/c/language/compatible_type.html "c/language/type")
[Arithmetic types](https://en.cppreference.com/w/c/language/arithmetic_types.html "c/language/arithmetic types")
[Objects and alignment](https://en.cppreference.com/w/c/language/object.html "c/language/object")
[The main() function](https://en.cppreference.com/w/c/language/main_function.html "c/language/main function")
[The as-if rule](https://en.cppreference.com/w/c/language/as_if.html "c/language/as if")
[Undefined behavior](https://en.cppreference.com/w/c/language/behavior.html "c/language/behavior")
[Memory model and data races](https://en.cppreference.com/w/c/language/memory_model.html "c/language/memory model")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/language/basics/navbar_content&action=edit)
This section provides definitions for the specific terminology and the concepts used when describing the C programming language.
A C program is a sequence of text files (typically header and source files) that contain [declarations](https://en.cppreference.com/w/c/language/declarations.html "c/language/declarations"). They undergo [translation](https://en.cppreference.com/w/c/language/translation_phases.html "c/language/translation phases") to become an executable program, which is executed when the OS calls its [main function](https://en.cppreference.com/w/c/language/main_function.html "c/language/main function") (unless it is itself the OS or another _freestanding_ program, in which case the entry point is implementation-defined).
Certain words in a C program have special meaning, they are [keywords](https://en.cppreference.com/w/c/keyword.html "c/keyword"). Others can be used as [identifiers](https://en.cppreference.com/w/c/language/identifiers.html "c/language/identifier"), which may be used to identify [objects](https://en.cppreference.com/w/c/language/object.html "c/language/object"), [functions](https://en.cppreference.com/w/c/language/functions.html "c/language/functions"), [struct](https://en.cppreference.com/w/c/language/struct.html "c/language/struct"), [union](https://en.cppreference.com/w/c/language/union.html "c/language/union"), or [enumeration](https://en.cppreference.com/w/c/language/enum.html "c/language/enum") tags, their members, [typedef](https://en.cppreference.com/w/c/language/typedef.html "c/language/typedef") names, [labels](https://en.cppreference.com/w/c/language/statements.html#Labels "c/language/statements"), or [macros](https://en.cppreference.com/w/c/preprocessor/replace.html "c/preprocessor/replace").
Each identifier (other than macro) is only valid within a part of the program called its [scope](https://en.cppreference.com/w/c/language/scope.html "c/language/scope") and belongs to one of four kinds of [name spaces](https://en.cppreference.com/w/c/language/name_space.html "c/language/name space"). Some identifiers have [linkage](https://en.cppreference.com/w/c/language/storage_class_specifiers.html "c/language/storage duration") which makes them refer to the same entities when they appear in different scopes or translation units.
Definitions of functions include sequences of [statements](https://en.cppreference.com/w/c/language/statements.html "c/language/statements") and [declarations](https://en.cppreference.com/w/c/language/declarations.html "c/language/declarations"), some of which include [expressions](https://en.cppreference.com/w/c/language/operators.html "c/language/expressions"), which specify the computations to be performed by the program.
[Declarations](https://en.cppreference.com/w/c/language/declarations.html "c/language/declarations") and [expressions](https://en.cppreference.com/w/c/language/operators.html "c/language/expressions") create, destroy, access, and manipulate [objects](https://en.cppreference.com/w/c/language/object.html "c/language/object"). Each [object](https://en.cppreference.com/w/c/language/object.html "c/language/object"), [function](https://en.cppreference.com/w/c/language/functions.html "c/language/functions"), and [expression](https://en.cppreference.com/w/c/language/operators.html "c/language/expressions") in C is associated with a [type](https://en.cppreference.com/w/c/language/compatible_type.html "c/language/type").
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/basic_concepts&action=edit&section=1 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/language/basics.html "cpp/language/basic concepts") for Basic concepts
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/language/basic_concepts&oldid=133988](https://en.cppreference.com/mwiki/index.php?title=c/language/basic_concepts&oldid=133988)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/language/basic_concepts.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/language/basic_concepts "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/language/basic_concepts "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/language/basic_concepts&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/language/basic_concepts&oldid=133988 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/language/basic_concepts&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")
  * [Česky](http://cs.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")
  * [Deutsch](http://de.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")
  * [Español](http://es.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")
  * [Français](http://fr.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")
  * [Italiano](http://it.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")
  * [日本語](http://ja.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")
  * [한국어](http://ko.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")
  * [Polski](http://pl.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")
  * [Português](http://pt.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")
  * [Русский](http://ru.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")
  * [Türkçe](http://tr.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")
  * [中文](http://zh.cppreference.com/w/c/language/basic_concepts "c/language/basic concepts")


  * This page was last modified on 1 October 2021, at 00:44.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
