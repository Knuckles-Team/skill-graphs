##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fvariadic&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fvariadic "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/variadic.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/mwiki/index.php?title=Talk:c/variadic&action=edit&redlink=1 "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/variadic.html)
##### Views
  * [View](https://en.cppreference.com/w/c/variadic.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/variadic&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/variadic&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/variadic.html)
![ads via Carbon](https://ad.double-click.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B29332811.401293666;dc_trk_aid=593420487;dc_trk_cid=207494836;ord=177299885;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1)
# Variadic functions
From cppreference.com
< [c](https://en.cppreference.com/w/c.html "c")
[ C](https://en.cppreference.com/w/c.html "c")
[Compiler support](https://en.cppreference.com/w/c/compiler_support.html "c/compiler support")
---
[Language](https://en.cppreference.com/w/c/language.html "c/language")
[Headers](https://en.cppreference.com/w/c/header.html "c/header")
[Type support](https://en.cppreference.com/w/c/types.html "c/types")
[Program utilities](https://en.cppreference.com/w/c/program.html "c/program")
**Variadic function support**
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
**Variadic functions**
[va_start](https://en.cppreference.com/w/c/variadic/va_start.html "c/variadic/va start")
---
[va_arg](https://en.cppreference.com/w/c/variadic/va_arg.html "c/variadic/va arg")
[va_copy](https://en.cppreference.com/w/c/variadic/va_copy.html "c/variadic/va copy") (C99)
[va_end](https://en.cppreference.com/w/c/variadic/va_end.html "c/variadic/va end")
[va_list](https://en.cppreference.com/w/c/variadic/va_list.html "c/variadic/va list")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/variadic/navbar_content&action=edit)
Variadic functions are functions (e.g. [printf](https://en.cppreference.com/w/c/io/fprintf.html "c/io/fprintf")) which take a variable number of arguments.
The declaration of a variadic function uses an ellipsis as the last parameter, e.g. int [printf](https://en.cppreference.com/w/c/io/fprintf.html)(const char* format, ...);. See [variadic arguments](https://en.cppreference.com/w/c/language/variadic.html "c/language/variadic") for additional detail on the syntax and automatic argument conversions.
Accessing the variadic arguments from the function body uses the following library facilities:
|
## Contents
  * [1 Types](https://en.cppreference.com/w/c/variadic.html#Types)
  * [2 Macros](https://en.cppreference.com/w/c/variadic.html#Macros)
  * [3 Example](https://en.cppreference.com/w/c/variadic.html#Example)
  * [4 References](https://en.cppreference.com/w/c/variadic.html#References)
  * [5 See also](https://en.cppreference.com/w/c/variadic.html#See_also)


---
#####  Types
[ va_list](https://en.cppreference.com/w/c/variadic/va_list.html "c/variadic/va list") |  holds the information needed by va_start, va_arg, va_end, and va_copy
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/variadic/dsc_va_list&action=edit)
#####  Macros
Defined in header `[`<stdarg.h>`](https://en.cppreference.com/w/c/header/stdarg.html "c/header/stdarg")`
[ va_start](https://en.cppreference.com/w/c/variadic/va_start.html "c/variadic/va start") |  enables access to variadic function arguments
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/variadic/dsc_va_start&action=edit)
[ va_arg](https://en.cppreference.com/w/c/variadic/va_arg.html "c/variadic/va arg") |  accesses the next variadic function argument
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/variadic/dsc_va_arg&action=edit)
[ va_copy](https://en.cppreference.com/w/c/variadic/va_copy.html "c/variadic/va copy") (C99) |  makes a copy of the variadic function arguments
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/variadic/dsc_va_copy&action=edit)
[ va_end](https://en.cppreference.com/w/c/variadic/va_end.html "c/variadic/va end") |  ends traversal of the variadic function arguments
(function macro) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/variadic/dsc_va_end&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/variadic&action=edit&section=1 "Edit section: Example")] Example
Print values of different types.
Run this code
```
#include <stdarg.h>
#include <stdio.h>
 
void simple_printf(const char* fmt, ...)
{
    va_list args;
 
    for (va_start(args, fmt); *fmt != '\0'; ++fmt)
    {
        switch(*fmt)
        {
            case 'd':
            {
                int i = va_arg(args, int);
                [printf](https://en.cppreference.com/w/c/io/fprintf.html)("%d\n", i);
                break;
            }
            case 'c':
            {
                // A 'char' variable will be promoted to 'int'
                // A character literal in C is already 'int' by itself
                int c = va_arg(args, int);
                [printf](https://en.cppreference.com/w/c/io/fprintf.html)("%c\n", c);
                break;
            }
            case 'f':
            {
                double d = va_arg(args, double);
                [printf](https://en.cppreference.com/w/c/io/fprintf.html)("%f\n", d);
                break;
            }
            default:
                [puts](https://en.cppreference.com/w/c/io/puts.html)("Unknown formatter!");
                goto END;
        }
    }
END:
    va_end(args);
}
 
int main(void)
{
    simple_printf("dcff", 3, 'a', 1.969, 42.5);
}
```

Output:
```
3
a
1.969000
42.50000
```

###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/variadic&action=edit&section=2 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 7.16 Variable arguments <stdarg.h> (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 7.16 Variable arguments <stdarg.h> (p: TBD)


  * C11 standard (ISO/IEC 9899:2011):


  * 7.16 Variable arguments <stdarg.h> (p: 269-272)


  * C99 standard (ISO/IEC 9899:1999):


  * 7.15 Variable arguments <stdarg.h> (p: 249-252)


  * C89/C90 standard (ISO/IEC 9899:1990):


  * 4.8 VARIABLE ARGUMENTS <stdarg.h>


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/variadic&action=edit&section=3 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/utility/variadic.html "cpp/utility/variadic") for Variadic functions
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/variadic&oldid=180120](https://en.cppreference.com/mwiki/index.php?title=c/variadic&oldid=180120)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/variadic.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/variadic "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/variadic "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/variadic&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/variadic&oldid=180120 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/variadic&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/variadic "c/variadic")
  * [Česky](http://cs.cppreference.com/w/c/variadic "c/variadic")
  * [Deutsch](http://de.cppreference.com/w/c/variadic "c/variadic")
  * [Español](http://es.cppreference.com/w/c/variadic "c/variadic")
  * [Français](http://fr.cppreference.com/w/c/variadic "c/variadic")
  * [Italiano](http://it.cppreference.com/w/c/variadic "c/variadic")
  * [日本語](http://ja.cppreference.com/w/c/variadic "c/variadic")
  * [한국어](http://ko.cppreference.com/w/c/variadic "c/variadic")
  * [Polski](http://pl.cppreference.com/w/c/variadic "c/variadic")
  * [Português](http://pt.cppreference.com/w/c/variadic "c/variadic")
  * [Русский](http://ru.cppreference.com/w/c/variadic "c/variadic")
  * [Türkçe](http://tr.cppreference.com/w/c/variadic "c/variadic")
  * [中文](http://zh.cppreference.com/w/c/variadic "c/variadic")


  * This page was last modified on 4 February 2025, at 02:22.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
