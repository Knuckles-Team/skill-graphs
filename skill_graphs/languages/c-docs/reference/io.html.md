##### [ cppreference.com ](https://en.cppreference.com/index.html)
[Create account](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fio&type=signup)
  * [Log in](https://en.cppreference.com/mwiki/index.php?title=Special:UserLogin&returnto=c%2Fio "You are encouraged to log in; however, it is not mandatory \[o\]")


##### Namespaces
  * [Page](https://en.cppreference.com/w/c/io.html "View the content page \[c\]")
  * [Discussion](https://en.cppreference.com/w/Talk%253Ac/io.html "Discussion about the content page \[t\]")


#####  Variants[](https://en.cppreference.com/w/c/io.html)
##### Views
  * [View](https://en.cppreference.com/w/c/io.html)
  * [Edit](https://en.cppreference.com/mwiki/index.php?title=c/io&action=edit "You can edit this page. Please use the preview button before saving \[e\]")
  * [History](https://en.cppreference.com/mwiki/index.php?title=c/io&action=history "Past revisions of this page \[h\]")


#####  Actions[](https://en.cppreference.com/w/c/io.html)
![ads via Carbon](https://ad.double-click.net/ddm/trackimp/N718679.452584BUYSELLADS.COM/B29332811.401293654;dc_trk_aid=593420481;dc_trk_cid=207494836;ord=177299882;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$;gdpr_consent=$;ltd=;dc_tdv=1)
# File input/output
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
**Input/output support**
[Localization support](https://en.cppreference.com/w/c/locale.html "c/locale")
[Concurrency support](https://en.cppreference.com/w/c/thread.html "c/thread") (C11)
[Technical Specifications](https://en.cppreference.com/w/c/experimental.html "c/experimental")
[Symbol index](https://en.cppreference.com/w/c/index.html "c/symbol index")
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/navbar_content&action=edit)
**File input/output**
Types and objects
---
|  | [stdinstdoutstderr](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams")
---
| [FILE](https://en.cppreference.com/w/c/io/FILE.html "c/io/FILE")
---
[fpos_t](https://en.cppreference.com/w/c/io/fpos_t.html "c/io/fpos t")


| Functions
---
File access
|  [fopenfopen_s](https://en.cppreference.com/w/c/io/fopen.html "c/io/fopen") (C11)
---
[freopenfreopen_s](https://en.cppreference.com/w/c/io/freopen.html "c/io/freopen") (C11)
[fwide](https://en.cppreference.com/w/c/io/fwide.html "c/io/fwide") (C95)
| [setbuf](https://en.cppreference.com/w/c/io/setbuf.html "c/io/setbuf")
---
[setvbuf](https://en.cppreference.com/w/c/io/setvbuf.html "c/io/setvbuf")
[fclose](https://en.cppreference.com/w/c/io/fclose.html "c/io/fclose")
[fflush](https://en.cppreference.com/w/c/io/fflush.html "c/io/fflush")


Unformatted input/output
| [fgetc](https://en.cppreference.com/w/c/io/fgetc.html "c/io/fgetc")
---
[fgets](https://en.cppreference.com/w/c/io/fgets.html "c/io/fgets")
[fputc](https://en.cppreference.com/w/c/io/putc.html "c/io/fputc")
[fputs](https://en.cppreference.com/w/c/io/fputs.html "c/io/fputs")
[getchar](https://en.cppreference.com/w/c/io/getchar.html "c/io/getchar")
[getsgets_s](https://en.cppreference.com/w/c/io/gets.html "c/io/gets") (until C11)(C11)
[putchar](https://en.cppreference.com/w/c/io/putchar.html "c/io/putchar")
[puts](https://en.cppreference.com/w/c/io/puts.html "c/io/puts")
[ungetc](https://en.cppreference.com/w/c/io/ungetc.html "c/io/ungetc")
|  [fgetwcgetwc](https://en.cppreference.com/w/c/io/fgetwc.html "c/io/fgetwc") (C95)(C95)
---
[fgetws](https://en.cppreference.com/w/c/io/fgetws.html "c/io/fgetws") (C95)
[fputwcputwc](https://en.cppreference.com/w/c/io/fputwc.html "c/io/fputwc") (C95)(C95)
[fputws](https://en.cppreference.com/w/c/io/fputws.html "c/io/fputws") (C95)
[getwchar](https://en.cppreference.com/w/c/io/getwchar.html "c/io/getwchar") (C95)
[putwchar](https://en.cppreference.com/w/c/io/putwchar.html "c/io/putwchar") (C95)
[ungetwc](https://en.cppreference.com/w/c/io/ungetwc.html "c/io/ungetwc") (C95)


Formatted input
|  [scanffscanfsscanfscanf_sfscanf_ssscanf_s](https://en.cppreference.com/w/c/io/fscanf.html "c/io/fscanf") (C11)(C11)(C11)
---
[wscanffwscanfswscanfwscanf_sfwscanf_sswscanf_s](https://en.cppreference.com/w/c/io/fwscanf.html "c/io/fwscanf") (C95)(C95)(C95)(C11)(C11)(C11)
|  [vscanfvfscanfvsscanfvscanf_svfscanf_svsscanf_s](https://en.cppreference.com/w/c/io/vfscanf.html "c/io/vfscanf") (C99)(C99)(C99)(C11)(C11)(C11)
---
[vwscanfvfwscanfvswscanfvwscanf_svfwscanf_svswscanf_s](https://en.cppreference.com/w/c/io/vfwscanf.html "c/io/vfwscanf") (C99)(C99)(C99)(C11)(C11)(C11)
| Direct input/output
---
| [fread](https://en.cppreference.com/w/c/io/fread.html "c/io/fread")
---
| [fwrite](https://en.cppreference.com/w/c/io/fwrite.html "c/io/fwrite")
---
Formatted output
|  [printffprintfsprintfsnprintfprintf_sfprintf_ssprintf_ssnprintf_s](https://en.cppreference.com/w/c/io/fprintf.html "c/io/fprintf") (C99)(C11)(C11)(C11)(C11)
---
[wprintffwprintfswprintfwprintf_sfwprintf_sswprintf_ssnwprintf_s](https://en.cppreference.com/w/c/io/fwprintf.html "c/io/fwprintf") (C95)(C95)(C95)(C11)(C11)(C11)(C11)
|  [vprintfvfprintfvsprintfvsnprintfvprintf_svfprintf_svsprintf_svsnprintf_s](https://en.cppreference.com/w/c/io/vfprintf.html "c/io/vfprintf") (C99)(C11)(C11)(C11)(C11)
---
[vwprintfvfwprintfvswprintfvwprintf_svfwprintf_svswprintf_svsnwprintf_s](https://en.cppreference.com/w/c/io/vfwprintf.html "c/io/vfwprintf") (C95)(C95)(C95)(C11)(C11)(C11)(C11)
File positioning
| [ftell](https://en.cppreference.com/w/c/io/ftell.html "c/io/ftell")
---
[fgetpos](https://en.cppreference.com/w/c/io/fgetpos.html "c/io/fgetpos")
[fseek](https://en.cppreference.com/w/c/io/fseek.html "c/io/fseek")
| [fsetpos](https://en.cppreference.com/w/c/io/fsetpos.html "c/io/fsetpos")
---
[rewind](https://en.cppreference.com/w/c/io/rewind.html "c/io/rewind")


Error handling
| [clearerr](https://en.cppreference.com/w/c/io/clearerr.html "c/io/clearerr")
---
[feof](https://en.cppreference.com/w/c/io/feof.html "c/io/feof")
| [ferror](https://en.cppreference.com/w/c/io/ferror.html "c/io/ferror")
---
[perror](https://en.cppreference.com/w/c/io/perror.html "c/io/perror")
Operations on files
| [remove](https://en.cppreference.com/w/c/io/remove.html "c/io/remove")
---
[tmpfiletmpfile_s](https://en.cppreference.com/w/c/io/tmpfile.html "c/io/tmpfile") (C11)
| [rename](https://en.cppreference.com/w/c/io/rename.html "c/io/rename")
---
[tmpnamtmpnam_s](https://en.cppreference.com/w/c/io/tmpnam.html "c/io/tmpnam") (C11)
[[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/navbar_content&action=edit)
The [`<stdio.h>`](https://en.cppreference.com/w/c/header/stdio.html "c/header/stdio") header provides generic file operation support and supplies functions with narrow character input/output capabilities.
The [`<wchar.h>`](https://en.cppreference.com/w/c/header/wchar.html "c/header/wchar") header supplies functions with wide character input/output capabilities.
I/O streams are denoted by objects of type [FILE](https://en.cppreference.com/w/c/io/FILE.html "c/io/FILE") that can only be accessed and manipulated through pointers of type [FILE](https://en.cppreference.com/w/c/io/FILE.html)*. Each stream is associated with an external physical device (file, standard input stream, printer, serial port, etc).
## Contents
  * [1 Types](https://en.cppreference.com/w/c/io.html#Types)
  * [2 Predefined standard streams](https://en.cppreference.com/w/c/io.html#Predefined_standard_streams)
  * [3 Functions](https://en.cppreference.com/w/c/io.html#Functions)
    * [3.1 File access](https://en.cppreference.com/w/c/io.html#File_access)
    * [3.2 Direct input/output](https://en.cppreference.com/w/c/io.html#Direct_input.2Foutput)
    * [3.3 Unformatted input/output](https://en.cppreference.com/w/c/io.html#Unformatted_input.2Foutput)
      * [3.3.1 Narrow character](https://en.cppreference.com/w/c/io.html#Narrow_character)
      * [3.3.2 Wide character](https://en.cppreference.com/w/c/io.html#Wide_character)
    * [3.4 Formatted input/output](https://en.cppreference.com/w/c/io.html#Formatted_input.2Foutput)
      * [3.4.1 Narrow character](https://en.cppreference.com/w/c/io.html#Narrow_character_2)
      * [3.4.2 Wide character](https://en.cppreference.com/w/c/io.html#Wide_character_2)
    * [3.5 File positioning](https://en.cppreference.com/w/c/io.html#File_positioning)
    * [3.6 Error handling](https://en.cppreference.com/w/c/io.html#Error_handling)
    * [3.7 Operations on files](https://en.cppreference.com/w/c/io.html#Operations_on_files)
  * [4 Macro constants](https://en.cppreference.com/w/c/io.html#Macro_constants)
  * [5 References](https://en.cppreference.com/w/c/io.html#References)
  * [6 See also](https://en.cppreference.com/w/c/io.html#See_also)


---
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/io&action=edit&section=1 "Edit section: Types")] Types
Defined in header `[`<stdio.h>`](https://en.cppreference.com/w/c/header/stdio.html "c/header/stdio")`
---
[ FILE](https://en.cppreference.com/w/c/io/FILE.html "c/io/FILE") |  object type, capable of holding all information needed to control a C I/O stream
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_FILE&action=edit)
[ fpos_t](https://en.cppreference.com/w/c/io/fpos_t.html "c/io/fpos t") |  non-array complete object type, capable of uniquely specifying a position and multibyte parser state in a file
(typedef) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fpos_t&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/io&action=edit&section=2 "Edit section: Predefined standard streams")] Predefined standard streams
Defined in header `[`<stdio.h>`](https://en.cppreference.com/w/c/header/stdio.html "c/header/stdio")`
---
[ stdinstdoutstderr](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams") |  expression of type [FILE](https://en.cppreference.com/w/c/io/FILE.html)* associated with the input stream
expression of type [FILE](https://en.cppreference.com/w/c/io/FILE.html)* associated with the output stream
expression of type [FILE](https://en.cppreference.com/w/c/io/FILE.html)* associated with the error output stream
(macro constant) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_std_streams&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/io&action=edit&section=3 "Edit section: Functions")] Functions
#####  File access
---
Defined in header `[`<stdio.h>`](https://en.cppreference.com/w/c/header/stdio.html "c/header/stdio")`
[ fopenfopen_s](https://en.cppreference.com/w/c/io/fopen.html "c/io/fopen") (C11) |  opens a file
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fopen&action=edit)
[ freopenfreopen_s](https://en.cppreference.com/w/c/io/freopen.html "c/io/freopen") (C11) |  open an existing stream with a different name
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_freopen&action=edit)
[ fclose](https://en.cppreference.com/w/c/io/fclose.html "c/io/fclose") |  closes a file
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fclose&action=edit)
[ fflush](https://en.cppreference.com/w/c/io/fflush.html "c/io/fflush") |  synchronizes an output stream with the actual file
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fflush&action=edit)
[ setbuf](https://en.cppreference.com/w/c/io/setbuf.html "c/io/setbuf") |  sets the buffer for a file stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_setbuf&action=edit)
[ setvbuf](https://en.cppreference.com/w/c/io/setvbuf.html "c/io/setvbuf") |  sets the buffer and its size for a file stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_setvbuf&action=edit)
Defined in header `[`<wchar.h>`](https://en.cppreference.com/w/c/header/wchar.html "c/header/wchar")`
[ fwide](https://en.cppreference.com/w/c/io/fwide.html "c/io/fwide") (C95) |  switches a file stream between wide character I/O and narrow character I/O
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fwide&action=edit)
#####  Direct input/output
Defined in header `[`<stdio.h>`](https://en.cppreference.com/w/c/header/stdio.html "c/header/stdio")`
[ fread](https://en.cppreference.com/w/c/io/fread.html "c/io/fread") |  reads from a file
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fread&action=edit)
[ fwrite](https://en.cppreference.com/w/c/io/fwrite.html "c/io/fwrite") |  writes to a file
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fwrite&action=edit)
#####  Unformatted input/output
######  Narrow character
Defined in header `[`<stdio.h>`](https://en.cppreference.com/w/c/header/stdio.html "c/header/stdio")`
[ fgetcgetc](https://en.cppreference.com/w/c/io/fgetc.html "c/io/fgetc") |  gets a character from a file stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fgetc&action=edit)
[ fgets](https://en.cppreference.com/w/c/io/fgets.html "c/io/fgets") |  gets a character string from a file stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fgets&action=edit)
[ fputcputc](https://en.cppreference.com/w/c/io/putc.html "c/io/fputc") |  writes a character to a file stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fputc&action=edit)
[ fputs](https://en.cppreference.com/w/c/io/fputs.html "c/io/fputs") |  writes a character string to a file stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fputs&action=edit)
[ getchar](https://en.cppreference.com/w/c/io/getchar.html "c/io/getchar") |  reads a character from [stdin](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams")
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_getchar&action=edit)
[ getsgets_s](https://en.cppreference.com/w/c/io/gets.html "c/io/gets") (removed in C11)(C11) |  reads a character string from [stdin](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams")
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_gets&action=edit)
[ putchar](https://en.cppreference.com/w/c/io/putchar.html "c/io/putchar") |  writes a character to [stdout](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams")
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_putchar&action=edit)
[ puts](https://en.cppreference.com/w/c/io/puts.html "c/io/puts") |  writes a character string to [stdout](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams")
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_puts&action=edit)
[ ungetc](https://en.cppreference.com/w/c/io/ungetc.html "c/io/ungetc") |  puts a character back into a file stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_ungetc&action=edit)
######  Wide character
Defined in header `[`<wchar.h>`](https://en.cppreference.com/w/c/header/wchar.html "c/header/wchar")`
[ fgetwcgetwc](https://en.cppreference.com/w/c/io/fgetwc.html "c/io/fgetwc") (C95) |  gets a wide character from a file stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fgetwc&action=edit)
[ fgetws](https://en.cppreference.com/w/c/io/fgetws.html "c/io/fgetws") (C95) |  gets a wide string from a file stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fgetws&action=edit)
[ fputwcputwc](https://en.cppreference.com/w/c/io/fputwc.html "c/io/fputwc") (C95) |  writes a wide character to a file stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fputwc&action=edit)
[ fputws](https://en.cppreference.com/w/c/io/fputws.html "c/io/fputws") (C95) |  writes a wide string to a file stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fputws&action=edit)
[ getwchar](https://en.cppreference.com/w/c/io/getwchar.html "c/io/getwchar") (C95) |  reads a wide character from [stdin](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams")
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_getwchar&action=edit)
[ putwchar](https://en.cppreference.com/w/c/io/putwchar.html "c/io/putwchar") (C95) |  writes a wide character to [stdout](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams")
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_putwchar&action=edit)
[ ungetwc](https://en.cppreference.com/w/c/io/ungetwc.html "c/io/ungetwc") (C95) |  puts a wide character back into a file stream
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_ungetwc&action=edit)
#####  Formatted input/output
######  Narrow character
Defined in header `[`<stdio.h>`](https://en.cppreference.com/w/c/header/stdio.html "c/header/stdio")`
[ scanffscanfsscanfscanf_sfscanf_ssscanf_s](https://en.cppreference.com/w/c/io/fscanf.html "c/io/fscanf") (C11)(C11)(C11) |  reads formatted input from [stdin](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams"), a file stream or a buffer
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fscanf&action=edit)
[ vscanfvfscanfvsscanfvscanf_svfscanf_svsscanf_s](https://en.cppreference.com/w/c/io/vfscanf.html "c/io/vfscanf") (C99)(C99)(C99)(C11)(C11)(C11) |  reads formatted input from [stdin](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams"), a file stream or a buffer
using variable argument list
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_vfscanf&action=edit)
[ printffprintfsprintfsnprintfprintf_sfprintf_ssprintf_ssnprintf_s](https://en.cppreference.com/w/c/io/fprintf.html "c/io/fprintf") (C99)(C11)(C11)(C11)(C11) |  prints formatted output to [stdout](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams"), a file stream or a buffer
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fprintf&action=edit)
[ vprintfvfprintfvsprintfvsnprintfvprintf_svfprintf_svsprintf_svsnprintf_s](https://en.cppreference.com/w/c/io/vfprintf.html "c/io/vfprintf") (C99)(C11)(C11)(C11)(C11) |  prints formatted output to [stdout](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams"), a file stream or a buffer
using variable argument list
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_vfprintf&action=edit)
######  Wide character
Defined in header `[`<wchar.h>`](https://en.cppreference.com/w/c/header/wchar.html "c/header/wchar")`
[ wscanffwscanfswscanfwscanf_sfwscanf_sswscanf_s](https://en.cppreference.com/w/c/io/fwscanf.html "c/io/fwscanf") (C95)(C95)(C95)(C11)(C11)(C11) |  reads formatted wide character input from [stdin](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams"), a file stream or a buffer
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fwscanf&action=edit)
[ vwscanfvfwscanfvswscanfvwscanf_svfwscanf_svswscanf_s](https://en.cppreference.com/w/c/io/vfwscanf.html "c/io/vfwscanf") (C99)(C99)(C99)(C11)(C11)(C11) |  reads formatted wide character input from [stdin](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams"), a file stream
or a buffer using variable argument list
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_vfwscanf&action=edit)
[ wprintffwprintfswprintfwprintf_sfwprintf_sswprintf_ssnwprintf_s](https://en.cppreference.com/w/c/io/fwprintf.html "c/io/fwprintf") (C95)(C95)(C95)(C11)(C11)(C11)(C11) |  prints formatted wide character output to [stdout](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams"), a file stream or a buffer
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fwprintf&action=edit)
[ vwprintfvfwprintfvswprintfvwprintf_svfwprintf_svswprintf_svsnwprintf_s](https://en.cppreference.com/w/c/io/vfwprintf.html "c/io/vfwprintf") (C95)(C95)(C95)(C11)(C11)(C11)(C11) |  prints formatted wide character output to [stdout](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams"), a file stream
or a buffer using variable argument list
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_vfwprintf&action=edit)
#####  File positioning
Defined in header `[`<stdio.h>`](https://en.cppreference.com/w/c/header/stdio.html "c/header/stdio")`
[ ftell](https://en.cppreference.com/w/c/io/ftell.html "c/io/ftell") |  returns the current file position indicator
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_ftell&action=edit)
[ fgetpos](https://en.cppreference.com/w/c/io/fgetpos.html "c/io/fgetpos") |  gets the file position indicator
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fgetpos&action=edit)
[ fseek](https://en.cppreference.com/w/c/io/fseek.html "c/io/fseek") |  moves the file position indicator to a specific location in a file
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fseek&action=edit)
[ fsetpos](https://en.cppreference.com/w/c/io/fsetpos.html "c/io/fsetpos") |  moves the file position indicator to a specific location in a file
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_fsetpos&action=edit)
[ rewind](https://en.cppreference.com/w/c/io/rewind.html "c/io/rewind") |  moves the file position indicator to the beginning in a file
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_rewind&action=edit)
#####  Error handling
Defined in header `[`<stdio.h>`](https://en.cppreference.com/w/c/header/stdio.html "c/header/stdio")`
[ clearerr](https://en.cppreference.com/w/c/io/clearerr.html "c/io/clearerr") |  clears errors
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_clearerr&action=edit)
[ feof](https://en.cppreference.com/w/c/io/feof.html "c/io/feof") |  checks for the end-of-file
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_feof&action=edit)
[ ferror](https://en.cppreference.com/w/c/io/ferror.html "c/io/ferror") |  checks for a file error
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_ferror&action=edit)
[ perror](https://en.cppreference.com/w/c/io/perror.html "c/io/perror") |  displays a character string corresponding of the current error to [stderr](https://en.cppreference.com/w/c/io/std_streams.html "c/io/std streams")
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_perror&action=edit)
#####  Operations on files
Defined in header `[`<stdio.h>`](https://en.cppreference.com/w/c/header/stdio.html "c/header/stdio")`
[ remove](https://en.cppreference.com/w/c/io/remove.html "c/io/remove") |  erases a file
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_remove&action=edit)
[ rename](https://en.cppreference.com/w/c/io/rename.html "c/io/rename") |  renames a file
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_rename&action=edit)
[ tmpfiletmpfile_s](https://en.cppreference.com/w/c/io/tmpfile.html "c/io/tmpfile") (C11) |  returns a pointer to a temporary file
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_tmpfile&action=edit)
[ tmpnamtmpnam_s](https://en.cppreference.com/w/c/io/tmpnam.html "c/io/tmpnam") (C11) |  returns a unique filename
(function) [[edit]](https://en.cppreference.com/mwiki/index.php?title=Template:c/io/dsc_tmpnam&action=edit)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/io&action=edit&section=4 "Edit section: Macro constants")] Macro constants
Defined in header `[`<stdio.h>`](https://en.cppreference.com/w/c/header/stdio.html "c/header/stdio")`
---
EOF |  integer constant expression of type int and negative value
(macro constant)
FOPEN_MAX |  maximum number of files that can be open simultaneously
(macro constant)
FILENAME_MAX |  size needed for an array of char to hold the longest supported file name
(macro constant)
BUFSIZ |  size of the buffer used by [setbuf](https://en.cppreference.com/w/c/io/setbuf.html "c/io/setbuf")
(macro constant)
_IOFBF_IOLBF_IONBF |  argument to [setvbuf](https://en.cppreference.com/w/c/io/setvbuf.html "c/io/setvbuf") indicating fully buffered I/O
argument to [setvbuf](https://en.cppreference.com/w/c/io/setvbuf.html "c/io/setvbuf") indicating line buffered I/O
argument to [setvbuf](https://en.cppreference.com/w/c/io/setvbuf.html "c/io/setvbuf") indicating unbuffered I/O
(macro constant)
SEEK_SETSEEK_CURSEEK_END |  argument to [fseek](https://en.cppreference.com/w/c/io/fseek.html "c/io/fseek") indicating seeking from beginning of the file
argument to [fseek](https://en.cppreference.com/w/c/io/fseek.html "c/io/fseek") indicating seeking from the current file position
argument to [fseek](https://en.cppreference.com/w/c/io/fseek.html "c/io/fseek") indicating seeking from end of the file
(macro constant)
TMP_MAXTMP_MAX_S (C11) |  maximum number of unique filenames that can be generated by [tmpnam](https://en.cppreference.com/w/c/io/tmpnam.html "c/io/tmpnam")
maximum number of unique filenames that can be generated by tmpnam_s
(macro constant)
L_tmpnamL_tmpnam_s (C11) |  size needed for an array of char to hold the result of [tmpnam](https://en.cppreference.com/w/c/io/tmpnam.html "c/io/tmpnam")
size needed for an array of char to hold the result of tmpnam_s
(macro constant)
###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/io&action=edit&section=5 "Edit section: References")] References
  * C23 standard (ISO/IEC 9899:2024):


  * 7.21 Input/output <stdio.h> (p: TBD)


  * 7.29 Extended multibyte and wide character utilities <wchar.h> (p: TBD)


  * 7.31.11 Input/output <stdio.h> (p: TBD)


  * 7.31.16 Extended multibyte and wide character utilities <wchar.h> (p: TBD)


  * K.3.5 Input/output <stdio.h> (p: TBD)


  * C17 standard (ISO/IEC 9899:2018):


  * 7.21 Input/output <stdio.h> (p: TBD)


  * 7.29 Extended multibyte and wide character utilities <wchar.h> (p: TBD)


  * 7.31.11 Input/output <stdio.h> (p: TBD)


  * 7.31.16 Extended multibyte and wide character utilities <wchar.h> (p: TBD)


  * K.3.5 Input/output <stdio.h> (p: TBD)


  * C11 standard (ISO/IEC 9899:2011):


  * 7.21 Input/output <stdio.h> (p: 296-339)


  * 7.29 Extended multibyte and wide character utilities <wchar.h> (p: 402-446)


  * 7.31.11 Input/output <stdio.h> (p: 456)


  * 7.31.16 Extended multibyte and wide character utilities <wchar.h> (p: 456)


  * K.3.5 Input/output <stdio.h> (p: 586-603)


  * C99 standard (ISO/IEC 9899:1999):


  * 7.19 Input/output <stdio.h> (p: 262-305)


  * 7.24 Extended multibyte and wide character utilities <wchar.h> (p: 348-392)


  * 7.26.9 Input/output <stdio.h> (p: 402)


  * 7.26.12 Extended multibyte and wide character utilities <wchar.h> (p: 402)


  * C89/C90 standard (ISO/IEC 9899:1990):


  * 4.9 INPUT/OUTPUT <stdio.h>


  * 4.13.6 Input/output <stdio.h>


###  [[edit](https://en.cppreference.com/mwiki/index.php?title=c/io&action=edit&section=6 "Edit section: See also")] See also
[C++ documentation](https://en.cppreference.com/w/cpp/io/c.html "cpp/io/c") for C-style file input/output
---
Retrieved from "[https://en.cppreference.com/mwiki/index.php?title=c/io&oldid=180208](https://en.cppreference.com/mwiki/index.php?title=c/io&oldid=180208)"
##### Navigation
  * [Support us](http://www.cppreference.com/support)
  * [Recent changes](https://en.cppreference.com/w/Special:RecentChanges "A list of recent changes in the wiki \[r\]")
  * [FAQ](https://en.cppreference.com/w/Cppreference%253AAbout.html)
  * [Offline version](https://en.cppreference.com/w/Cppreference%253AArchives.html)


#####  Toolbox[](https://en.cppreference.com/w/c/io.html)
  * [What links here](https://en.cppreference.com/w/Special:WhatLinksHere/c/io "A list of all wiki pages that link here \[j\]")
  * [Related changes](https://en.cppreference.com/w/Special:RecentChangesLinked/c/io "Recent changes in pages linked from this page \[k\]")
  * [Upload file](http://upload.cppreference.com/w/Special:Upload "Upload files \[u\]")
  * [Special pages](https://en.cppreference.com/w/Special:SpecialPages "A list of all special pages \[q\]")
  * [Printable version](https://en.cppreference.com/mwiki/index.php?title=c/io&printable=yes "Printable version of this page \[p\]")
  * [Permanent link](https://en.cppreference.com/mwiki/index.php?title=c/io&oldid=180208 "Permanent link to this revision of the page")
  * [Page information](https://en.cppreference.com/mwiki/index.php?title=c/io&action=info)


  * In other languages


  * [العربية](http://ar.cppreference.com/w/c/io "c/io")
  * [Česky](http://cs.cppreference.com/w/c/io "c/io")
  * [Deutsch](http://de.cppreference.com/w/c/io "c/io")
  * [Español](http://es.cppreference.com/w/c/io "c/io")
  * [Français](http://fr.cppreference.com/w/c/io "c/io")
  * [Italiano](http://it.cppreference.com/w/c/io "c/io")
  * [日本語](http://ja.cppreference.com/w/c/io "c/io")
  * [한국어](http://ko.cppreference.com/w/c/io "c/io")
  * [Polski](http://pl.cppreference.com/w/c/io "c/io")
  * [Português](http://pt.cppreference.com/w/c/io "c/io")
  * [Русский](http://ru.cppreference.com/w/c/io "c/io")
  * [Türkçe](http://tr.cppreference.com/w/c/io "c/io")
  * [中文](http://zh.cppreference.com/w/c/io "c/io")


  * This page was last modified on 6 February 2025, at 17:26.


  * [Privacy policy](https://en.cppreference.com/w/Cppreference%253APrivacy_policy.html "Cppreference:Privacy policy")
  * [About cppreference.com](https://en.cppreference.com/w/Cppreference%253AAbout.html "Cppreference:About")
  * [Disclaimers](https://en.cppreference.com/w/Cppreference%253AGeneral_disclaimer.html "Cppreference:General disclaimer")
