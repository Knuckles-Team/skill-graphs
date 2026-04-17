##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fmemory&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fmemory "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/memory.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/w/Talk%253Ac/memory.html "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/memory.html)
##### Views
  * [View](https://en.cppreference.com/w/c/memory.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/memory&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/memory&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/memory.html)
# Dynamic memory management
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
**Dynamic memory management**
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
**Dynamic memory management**
[malloc](https://en.cppreference.com/w/c/memory/malloc.html "c/memory/malloc")
---
[calloc](https://en.cppreference.com/w/c/memory/calloc.html "c/memory/calloc")
[realloc](https://en.cppreference.com/w/c/memory/realloc.html "c/memory/realloc")
[free](https://en.cppreference.com/w/c/memory/free.html "c/memory/free")
[free_sized](https://en.cppreference.com/w/c/memory/free_sized.html "c/memory/free sized") (C23)
[free_aligned_sized](https://en.cppreference.com/w/c/memory/free_aligned_sized.html "c/memory/free aligned sized") (C23)
[aligned_alloc](https://en.cppreference.com/w/c/memory/aligned_alloc.html "c/memory/aligned alloc") (C11)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/memory/navbar_content&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/memory&action=edit&section=1 "Edit section: Functions")] Functions
Defined in header `[`<stdlib.h>`](https://en.cppreference.com/w/c/header/stdlib.html "c/header/stdlib")`
---
[ malloc](https://en.cppreference.com/w/c/memory/malloc.html "c/memory/malloc") |  allocates memory
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/memory/dsc_malloc&action=edit)
[ calloc](https://en.cppreference.com/w/c/memory/calloc.html "c/memory/calloc") |  allocates and zeroes memory
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/memory/dsc_calloc&action=edit)
[ realloc](https://en.cppreference.com/w/c/memory/realloc.html "c/memory/realloc") |  expands previously allocated memory block
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/memory/dsc_realloc&action=edit)
[ free](https://en.cppreference.com/w/c/memory/free.html "c/memory/free") |  deallocates previously allocated memory
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/memory/dsc_free&action=edit)
[ free_sized](https://en.cppreference.com/w/c/memory/free_sized.html "c/memory/free sized") (C23) |  deallocates previously allocated sized memory
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/memory/dsc_free_sized&action=edit)
[ free_aligned_sized](https://en.cppreference.com/w/c/memory/free_aligned_sized.html "c/memory/free aligned sized") (C23) |  deallocates previously allocated sized and aligned memory
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/memory/dsc_free_aligned_sized&action=edit)
[ aligned_alloc](https://en.cppreference.com/w/c/memory/aligned_alloc.html "c/memory/aligned alloc") (C11) |  allocates aligned memory
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/memory/dsc_aligned_alloc&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/memory&action=edit&section=2 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/memory/c.html "cpp/memory/c") for C memory management library
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/memory&oldid=143505](https://en.cppreference.com/mwiki/index.php?title=c/memory&oldid=143505)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/memory.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/memory "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/memory "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/memory&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/memory&oldid=143505 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/memory&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/memory "c/memory")
  * [Česky](http://cs.cppreference.com/w/c/memory "c/memory")
  * [Deutsch](http://de.cppreference.com/w/c/memory "c/memory")
  * [Español](http://es.cppreference.com/w/c/memory "c/memory")
  * [Français](http://fr.cppreference.com/w/c/memory "c/memory")
  * [Italiano](http://it.cppreference.com/w/c/memory "c/memory")
  * [日本語](http://ja.cppreference.com/w/c/memory "c/memory")
  * [한국어](http://ko.cppreference.com/w/c/memory "c/memory")
  * [Polski](http://pl.cppreference.com/w/c/memory "c/memory")
  * [Português](http://pt.cppreference.com/w/c/memory "c/memory")
  * [Русский](http://ru.cppreference.com/w/c/memory "c/memory")
  * [Türkçe](http://tr.cppreference.com/w/c/memory "c/memory")
  * [中文](http://zh.cppreference.com/w/c/memory "c/memory")


  * This page was last modified on 18 September 2022, at 10:41.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
