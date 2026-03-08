##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Flanguage%2Finitialization&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Flanguage%2Finitialization "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/language/initialization.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/mwiki/index.php?title=Talk:c/language/initialization&action=edit&redlink=1 "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/language/initialization.html)
##### Views
  * [View](https://en.cppreference.com/w/c/language/initialization.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/language/initialization.html)
# Initialization
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
[Basic concepts](https://en.cppreference.com/w/c/language/basic_concepts.html "c/language/basic concepts")
---
[ Keywords](https://en.cppreference.com/w/c/keyword.html "c/keyword")
[ Preprocessor](https://en.cppreference.com/w/c/preprocessor.html "c/preprocessor")
[ Statements](https://en.cppreference.com/w/c/language/statements.html "c/language/statements")
[ Expressions](https://en.cppreference.com/w/c/language/operators.html "c/language/expressions")
**Initialization**
[ Declarations](https://en.cppreference.com/w/c/language/declarations.html "c/language/declarations")
[ Functions](https://en.cppreference.com/w/c/language/functions.html "c/language/functions")
Miscellaneous
[ History of C](https://en.cppreference.com/w/c/language/history.html "c/language/history")
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/language/navbar_content&action=edit)
**Initialization**
[ Explicit initialization](https://en.cppreference.com/w/c/language/initialization.html#Explicit_initialization "c/language/initialization")
---
[ Implicit initialization](https://en.cppreference.com/w/c/language/initialization.html#Implicit_initialization "c/language/initialization")
[ Empty initialization](https://en.cppreference.com/w/c/language/initialization.html#Empty_initialization "c/language/initialization")
[ Scalar initialization](https://en.cppreference.com/w/c/language/scalar_initialization.html "c/language/scalar initialization")
[ Array initialization](https://en.cppreference.com/w/c/language/array_initialization.html "c/language/array initialization")
[ Struct and union initialization](https://en.cppreference.com/w/c/language/struct_initialization.html "c/language/struct initialization")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/language/initialization/navbar_content&action=edit)
A [declaration](https://en.cppreference.com/w/c/language/declarations.html "c/language/declarations") of an object may provide its initial value through the process known as _initialization_.
For each [declarator](https://en.cppreference.com/w/c/language/declarations.html "c/language/declarations"), the initializer, if not omitted, may be one of the following:
---
`**=**` expression |  (1)  |
`**=**``**{**` initializer-list `**}**` |  (2)  |
`**=**``**{**``**}**` |  (3)  |  (since C23)
where initializer-list is a non-empty comma-separated list of initializer ﻿s (with an optional trailing comma), where each initializer has one of three possible forms:
---
expression |  (1)  |
`**{**` initializer-list `**}**` |  (2)  |
`**{**``**}**` |  (3)  |  (since C23)
designator-list `**=**` initializer |  (4)  |  (since C99)
where designator-list is a list of either array designators of the form `**[**` constant-expression `**]**`or struct/union member designators of the form`**.**` identifier ﻿; see [array initialization](https://en.cppreference.com/w/c/language/array_initialization.html "c/language/array initialization") and [struct initialization](https://en.cppreference.com/w/c/language/struct_initialization.html "c/language/struct initialization").  Note: besides initializers, brace-enclosed initializer-list may appear in [compound literals](https://en.cppreference.com/w/c/language/compound_literal.html "c/language/compound literal"), which are expressions of the form:  |
---
`**(**` type `**)**``**{**` initializer-list `**}**` |  |
`**(**` type `**)**``**{**``**}**` |  |  (since C23)
(since C99)
## Contents
  * [1 Explanation](https://en.cppreference.com/w/c/language/initialization.html#Explanation)
    * [1.1 Explicit initialization](https://en.cppreference.com/w/c/language/initialization.html#Explicit_initialization)
    * [1.2 Implicit initialization](https://en.cppreference.com/w/c/language/initialization.html#Implicit_initialization)
    * [1.3 Empty initialization](https://en.cppreference.com/w/c/language/initialization.html#Empty_initialization)
  * [2 Notes](https://en.cppreference.com/w/c/language/initialization.html#Notes)
  * [3 Example](https://en.cppreference.com/w/c/language/initialization.html#Example)
  * [4 References](https://en.cppreference.com/w/c/language/initialization.html#References)
  * [5 See also](https://en.cppreference.com/w/c/language/initialization.html#See_also)


---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&action=edit&section=1 "Edit section: Explanation")] Explanation
The initializer specifies the initial value stored in an object.
####  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&action=edit&section=2 "Edit section: Explicit initialization")] Explicit initialization
If an initializer is provided, see
  * [scalar initialization](https://en.cppreference.com/w/c/language/scalar_initialization.html "c/language/scalar initialization") for the initialization of scalar types
  * [array initialization](https://en.cppreference.com/w/c/language/array_initialization.html "c/language/array initialization") for the initialization of array types
  * [struct initialization](https://en.cppreference.com/w/c/language/struct_initialization.html "c/language/struct initialization") for the initialization of struct and union types.


####  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&action=edit&section=3 "Edit section: Implicit initialization")] Implicit initialization
If an initializer is not provided:
  * objects with automatic [storage duration](https://en.cppreference.com/w/c/language/storage_class_specifiers.html "c/language/storage duration") are initialized to indeterminate values (which may be [trap representations](https://en.cppreference.com/w/c/language/object.html "c/language/object"))
  * objects with static and thread-local [storage duration](https://en.cppreference.com/w/c/language/storage_class_specifiers.html "c/language/storage duration") are empty-initialized


####  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&action=edit&section=4 "Edit section: Empty initialization")] Empty initialization
An object is empty-initialized if it is explicitly initialized from initializer = {}.  | (since C23)
---|---
In some cases, an object is empty-initialized if it is not initialized explicitly, that is:
  * pointers are initialized to null pointer values of their types
  * objects of integral types are initialized to unsigned zero
  * objects of floating types are initialized to positive zero
  * all elements of arrays, all members of structs, and the first members of unions are empty-initialized, recursively, plus all padding bits are initialized to zero

    (on platforms where null pointer values and floating zeroes have all-bit-zero representations, this form of initialization for statistics is normally implemented by allocating them in the .bss section of the program image)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&action=edit&section=5 "Edit section: Notes")] Notes
When initializing an object of static or thread-local [storage duration](https://en.cppreference.com/w/c/language/storage_class_specifiers.html "c/language/storage duration"), every expression in the initializer must be a [constant expression](https://en.cppreference.com/w/c/language/constant_expression.html "c/language/constant expression") or [string literal](https://en.cppreference.com/w/c/language/string_literal.html "c/language/string literal").
Initializers cannot be used in declarations of objects of incomplete type, VLAs, and block-scope objects with linkage.
The initial values of function parameters are established as if by assignment from the arguments of a [function call](https://en.cppreference.com/w/c/language/operator_other.html#Function_call "c/language/operator other"), rather than by initialization.
If an indeterminate value is used as an argument to any standard library call, the behavior is undefined. Otherwise, the result of any expression involving indeterminate values is an indeterminate value (e.g. int n;, n may not compare equal to itself and it may appear to change its value on subsequent reads)
There is no special construct in C corresponding to [value initialization](https://en.cppreference.com/w/cpp/language/value_initialization.html "cpp/language/value initialization") in C++; however, = {0} (or (T){0} in compound literals)(since C99) can be used instead, as the C standard does not allow empty structs, empty unions, or arrays of zero length.  | (until C23)
---|---
The empty initializer = {} (or (T){} in compound literals) can be used to achieve the same semantics as [value initialization](https://en.cppreference.com/w/cpp/language/value_initialization.html "cpp/language/value initialization") in C++.  | (since C23)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&action=edit&section=6 "Edit section: Example")] Example
Run this code
```
#include <stdlib.h>
int a[2]; // initializes a to {0, 0}
int main(void)
{
    int i;          // initializes i to an indeterminate value
    static int j;   // initializes j to 0
    int k = 1;      // initializes k to 1
 
    // initializes int x[3] to 1,3,5
    // initializes int* p to &x[0]
    int x[] = { 1, 3, 5 }, *p = x;
 
    // initializes w (an array of two structs) to
    // { { {1,0,0}, 0}, { {2,0,0}, 0} }
    struct {int a[3], b;} w[] = {[0].a = {1}, [1].a[0] = 2};
 
    // function call expression can be used for a local variable
    char* ptr = [malloc](https://en.cppreference.com/w/c/memory/malloc.html)(10);
    [free](https://en.cppreference.com/w/c/memory/free.html)(ptr);
 
//  Error: objects with static storage duration require constant initializers
//  static char* ptr = malloc(10);
 
//  Error: VLA cannot be initialized
//  int vla[n] = {0};
}
```

###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&action=edit&section=7 "Edit section: References")] References
  * C17 standard (ISO/IEC 9899:2018):


  * 6.7.9 Initialization (p: 100-105)


  * C11 standard (ISO/IEC 9899:2011):


  * 6.7.9 Initialization (p: 139-144)


  * C99 standard (ISO/IEC 9899:1999):


  * 6.7.8 Initialization (p: 125-130)


  * C89/C90 standard (ISO/IEC 9899:1990):


  * 6.5.7 Initialization


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&action=edit&section=8 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/language/initialization.html "cpp/language/initialization") for Initialization
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&oldid=147022](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&oldid=147022)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/language/initialization.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/language/initialization "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/language/initialization "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&oldid=147022 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/language/initialization&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/language/initialization "c/language/initialization")
  * [Česky](http://cs.cppreference.com/w/c/language/initialization "c/language/initialization")
  * [Deutsch](http://de.cppreference.com/w/c/language/initialization "c/language/initialization")
  * [Español](http://es.cppreference.com/w/c/language/initialization "c/language/initialization")
  * [Français](http://fr.cppreference.com/w/c/language/initialization "c/language/initialization")
  * [Italiano](http://it.cppreference.com/w/c/language/initialization "c/language/initialization")
  * [日本語](http://ja.cppreference.com/w/c/language/initialization "c/language/initialization")
  * [한국어](http://ko.cppreference.com/w/c/language/initialization "c/language/initialization")
  * [Polski](http://pl.cppreference.com/w/c/language/initialization "c/language/initialization")
  * [Português](http://pt.cppreference.com/w/c/language/initialization "c/language/initialization")
  * [Русский](http://ru.cppreference.com/w/c/language/initialization "c/language/initialization")
  * [Türkçe](http://tr.cppreference.com/w/c/language/initialization "c/language/initialization")
  * [中文](http://zh.cppreference.com/w/c/language/initialization "c/language/initialization")


  * This page was last modified on 26 January 2023, at 10:03.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
