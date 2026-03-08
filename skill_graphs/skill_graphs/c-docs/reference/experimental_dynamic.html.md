##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fexperimental%2Fdynamic&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fexperimental%2Fdynamic "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/experimental/dynamic.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/mwiki/index.php?title=Talk:c/experimental/dynamic&action=edit&redlink=1 "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/experimental/dynamic.html)
##### Views
  * [View](https://en.cppreference.com/w/c/experimental/dynamic.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/experimental/dynamic&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/experimental/dynamic&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/experimental/dynamic.html)
# Dynamic memory extensions
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")‎ | [experimental](https://en.cppreference.com/w/c/experimental.html "c/experimental")
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
[ Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[ Extensions for embedded processors](https://en.cppreference.com/mwiki/index.php?title=c/experimental/embedded&action=edit&redlink=1 "c/experimental/embedded \(page does not exist\)")
---
**Dynamic memory extensions**
[ Floating-point extensions part 1: Binary floating-point](https://en.cppreference.com/w/c/experimental/fpext1.html "c/experimental/fpext1")
[ Floating-point extensions part 4: Supplementary functions](https://en.cppreference.com/w/c/experimental/fpext4.html "c/experimental/fpext4")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/navbar_content&action=edit)
**Dynamic memory extensions**
[fmemopen](https://en.cppreference.com/mwiki/index.php?title=c/experimental/dynamic/fmemopen&action=edit&redlink=1 "c/experimental/dynamic/fmemopen \(page does not exist\)")
---
[open_memstreamopen_wmemstream](https://en.cppreference.com/mwiki/index.php?title=c/experimental/dynamic/open_memstream&action=edit&redlink=1 "c/experimental/dynamic/open memstream \(page does not exist\)")
[asprintfaswprintfvasprintfvaswprintf](https://en.cppreference.com/w/c/experimental/dynamic/asprintf.html "c/experimental/dynamic/asprintf")
[getlinegetwlinegetdelimgetwdelim](https://en.cppreference.com/w/c/experimental/dynamic/getline.html "c/experimental/dynamic/getline")
[strdup](https://en.cppreference.com/w/c/experimental/dynamic/strdup.html "c/experimental/dynamic/strdup")
[strndup](https://en.cppreference.com/w/c/experimental/dynamic/strndup.html "c/experimental/dynamic/strndup")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/dynamic/navbar_content&action=edit)
Extensions to the C Library Part II: Dynamic Allocation Functions, ISO/IEC TR 24731-2:2010, defines the following new components for the C standard library:
__STDC_ALLOC_LIB__ |  integer constant of type long indicating conformance level
(macro constant)
---|---
Defined in header `[`<stdio.h>`](https://en.cppreference.com/w/c/header/stdio.html "c/header/stdio")`
[ fmemopen](https://en.cppreference.com/mwiki/index.php?title=c/experimental/dynamic/fmemopen&action=edit&redlink=1 "c/experimental/dynamic/fmemopen \(page does not exist\)") (dynamic memory TR) |  opens a fixed-size memory buffer as an I/O stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/dynamic/dsc_fmemopen&action=edit)
[ open_memstreamopen_wmemstream](https://en.cppreference.com/mwiki/index.php?title=c/experimental/dynamic/open_memstream&action=edit&redlink=1 "c/experimental/dynamic/open memstream \(page does not exist\)") (dynamic memory TR) |  opens a dynamically resized memory buffer as an I/O stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/dynamic/dsc_open_memstream&action=edit)
[ asprintfaswprintfvasprintfvaswprintf](https://en.cppreference.com/w/c/experimental/dynamic/asprintf.html "c/experimental/dynamic/asprintf") (dynamic memory TR) |  variants of [sprintf](https://en.cppreference.com/w/c/io/fprintf.html "c/io/fprintf") etc that write to automatically-allocated buffer and return a pointer to it
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/dynamic/dsc_asprintf&action=edit)
[ getlinegetwlinegetdelimgetwdelim](https://en.cppreference.com/w/c/experimental/dynamic/getline.html "c/experimental/dynamic/getline") (dynamic memory TR) |  read from a stream into an automatically resized buffer until delimiter/end of line
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/dynamic/dsc_getline&action=edit)
Defined in header `[`<string.h>`](https://en.cppreference.com/w/c/header/string.html "c/header/string")`
[ strdup](https://en.cppreference.com/w/c/experimental/dynamic/strdup.html "c/experimental/dynamic/strdup") (dynamic memory TR) |  allocate a copy of a string
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/dynamic/dsc_strdup&action=edit)
[ strndup](https://en.cppreference.com/w/c/experimental/dynamic/strndup.html "c/experimental/dynamic/strndup") (dynamic memory TR) |  allocate a copy of a string up to specified size
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/experimental/dynamic/dsc_strndup&action=edit)
This library extension also introduces assignment-allocation character `**m**`for use with`**%s**`,`**%[**`, and`**%c**`conversion specifiers in[fscanf](https://en.cppreference.com/w/c/io/fscanf.html "c/io/fscanf") and [fwscanf](https://en.cppreference.com/w/c/io/fwscanf.html "c/io/fwscanf") family of functions.
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/experimental/dynamic&action=edit&section=1 "Edit section: Notes")] Notes
The functions `fmemopen`, `open_memstream`, `open_wmemstream`, `getdelim`, `getline`, `strdup`, `strndup`, and the extensions to `fscanf` are available in
The functions `asprintf` and `vasprintf` are available in Linux Standard Base (ISO/IEC IS 23360:2006)
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/experimental/dynamic&oldid=104628](https://en.cppreference.com/mwiki/index.php?title=c/experimental/dynamic&oldid=104628)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/experimental/dynamic.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/experimental/dynamic "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/experimental/dynamic "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/experimental/dynamic&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/experimental/dynamic&oldid=104628 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/experimental/dynamic&action=info)


  * In other languages


  * [日本語](http://ja.cppreference.com/w/c/experimental/dynamic "c/experimental/dynamic")
  * [中文](http://zh.cppreference.com/w/c/experimental/dynamic "c/experimental/dynamic")


  * This page was last modified on 5 July 2018, at 18:55.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
