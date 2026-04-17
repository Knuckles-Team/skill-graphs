[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`msvcrt` — Useful routines from the MS VC++ runtime](https://docs.python.org/3/library/msvcrt.html)
    * [File Operations](https://docs.python.org/3/library/msvcrt.html#file-operations)
    * [Console I/O](https://docs.python.org/3/library/msvcrt.html#console-i-o)
    * [Other Functions](https://docs.python.org/3/library/msvcrt.html#other-functions)


#### Previous topic
[MS Windows Specific Services](https://docs.python.org/3/library/windows.html "previous chapter")
#### Next topic
[`winreg` — Windows registry access](https://docs.python.org/3/library/winreg.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=msvcrt+%E2%80%94+Useful+routines+from+the+MS+VC%2B%2B+runtime&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmsvcrt.html&pagesource=library%2Fmsvcrt.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/winreg.html "winreg — Windows registry access") |
  * [previous](https://docs.python.org/3/library/windows.html "MS Windows Specific Services") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [MS Windows Specific Services](https://docs.python.org/3/library/windows.html) »
  * [`msvcrt` — Useful routines from the MS VC++ runtime](https://docs.python.org/3/library/msvcrt.html)
  * |
  * Theme  Auto Light Dark |


#  `msvcrt` — Useful routines from the MS VC++ runtime[¶](https://docs.python.org/3/library/msvcrt.html#module-msvcrt "Link to this heading")
* * *
These functions provide access to some useful capabilities on Windows platforms. Some higher-level modules use these functions to build the Windows implementations of their services. For example, the [`getpass`](https://docs.python.org/3/library/getpass.html#module-getpass "getpass: Portable reading of passwords and retrieval of the userid.") module uses this in the implementation of the [`getpass()`](https://docs.python.org/3/library/getpass.html#module-getpass "getpass: Portable reading of passwords and retrieval of the userid.") function.
Further documentation on these functions can be found in the Platform API documentation.
The module implements both the normal and wide char variants of the console I/O api. The normal API deals only with ASCII characters and is of limited use for internationalized applications. The wide char API should be used where ever possible.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Changed in version 3.3: Operations in this module now raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") where [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") was raised.
## File Operations[¶](https://docs.python.org/3/library/msvcrt.html#file-operations "Link to this heading")

msvcrt.locking(_fd_ , _mode_ , _nbytes_)[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.locking "Link to this definition")

Lock part of a file based on file descriptor _fd_ from the C runtime. Raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") on failure. The locked region of the file extends from the current file position for _nbytes_ bytes, and may continue beyond the end of the file. _mode_ must be one of the `LK_*` constants listed below. Multiple regions in a file may be locked at the same time, but may not overlap. Adjacent regions are not merged; they must be unlocked individually.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `msvcrt.locking` with arguments `fd`, `mode`, `nbytes`.

msvcrt.LK_LOCK[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.LK_LOCK "Link to this definition")


msvcrt.LK_RLCK[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.LK_RLCK "Link to this definition")

Locks the specified bytes. If the bytes cannot be locked, the program immediately tries again after 1 second. If, after 10 attempts, the bytes cannot be locked, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised.

msvcrt.LK_NBLCK[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.LK_NBLCK "Link to this definition")


msvcrt.LK_NBRLCK[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.LK_NBRLCK "Link to this definition")

Locks the specified bytes. If the bytes cannot be locked, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised.

msvcrt.LK_UNLCK[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.LK_UNLCK "Link to this definition")

Unlocks the specified bytes, which must have been previously locked.

msvcrt.setmode(_fd_ , _flags_)[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.setmode "Link to this definition")

Set the line-end translation mode for the file descriptor _fd_. To set it to text mode, _flags_ should be [`os.O_TEXT`](https://docs.python.org/3/library/os.html#os.O_TEXT "os.O_TEXT"); for binary, it should be [`os.O_BINARY`](https://docs.python.org/3/library/os.html#os.O_BINARY "os.O_BINARY").

msvcrt.open_osfhandle(_handle_ , _flags_)[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.open_osfhandle "Link to this definition")

Create a C runtime file descriptor from the file handle _handle_. The _flags_ parameter should be a bitwise OR of [`os.O_APPEND`](https://docs.python.org/3/library/os.html#os.O_APPEND "os.O_APPEND"), [`os.O_RDONLY`](https://docs.python.org/3/library/os.html#os.O_RDONLY "os.O_RDONLY"), [`os.O_TEXT`](https://docs.python.org/3/library/os.html#os.O_TEXT "os.O_TEXT") and [`os.O_NOINHERIT`](https://docs.python.org/3/library/os.html#os.O_NOINHERIT "os.O_NOINHERIT"). The returned file descriptor may be used as a parameter to [`os.fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen") to create a file object.
The file descriptor is inheritable by default. Pass [`os.O_NOINHERIT`](https://docs.python.org/3/library/os.html#os.O_NOINHERIT "os.O_NOINHERIT") flag to make it non inheritable.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `msvcrt.open_osfhandle` with arguments `handle`, `flags`.

msvcrt.get_osfhandle(_fd_)[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.get_osfhandle "Link to this definition")

Return the file handle for the file descriptor _fd_. Raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if _fd_ is not recognized.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `msvcrt.get_osfhandle` with argument `fd`.
## Console I/O[¶](https://docs.python.org/3/library/msvcrt.html#console-i-o "Link to this heading")

msvcrt.kbhit()[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.kbhit "Link to this definition")

Returns a nonzero value if a keypress is waiting to be read. Otherwise, return 0.

msvcrt.getch()[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.getch "Link to this definition")

Read a keypress and return the resulting character as a byte string. Nothing is echoed to the console. This call will block if a keypress is not already available, but will not wait for `Enter` to be pressed. If the pressed key was a special function key, this will return `'\000'` or `'\xe0'`; the next call will return the keycode. The `Control`-`C` keypress cannot be read with this function.

msvcrt.getwch()[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.getwch "Link to this definition")

Wide char variant of [`getch()`](https://docs.python.org/3/library/msvcrt.html#msvcrt.getch "msvcrt.getch"), returning a Unicode value.

msvcrt.getche()[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.getche "Link to this definition")

Similar to [`getch()`](https://docs.python.org/3/library/msvcrt.html#msvcrt.getch "msvcrt.getch"), but the keypress will be echoed if it represents a printable character.

msvcrt.getwche()[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.getwche "Link to this definition")

Wide char variant of [`getche()`](https://docs.python.org/3/library/msvcrt.html#msvcrt.getche "msvcrt.getche"), returning a Unicode value.

msvcrt.putch(_char_)[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.putch "Link to this definition")

Print the byte string _char_ to the console without buffering.

msvcrt.putwch(_unicode_char_)[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.putwch "Link to this definition")

Wide char variant of [`putch()`](https://docs.python.org/3/library/msvcrt.html#msvcrt.putch "msvcrt.putch"), accepting a Unicode value.

msvcrt.ungetch(_char_)[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.ungetch "Link to this definition")

Cause the byte string _char_ to be “pushed back” into the console buffer; it will be the next character read by [`getch()`](https://docs.python.org/3/library/msvcrt.html#msvcrt.getch "msvcrt.getch") or [`getche()`](https://docs.python.org/3/library/msvcrt.html#msvcrt.getche "msvcrt.getche").

msvcrt.ungetwch(_unicode_char_)[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.ungetwch "Link to this definition")

Wide char variant of [`ungetch()`](https://docs.python.org/3/library/msvcrt.html#msvcrt.ungetch "msvcrt.ungetch"), accepting a Unicode value.
## Other Functions[¶](https://docs.python.org/3/library/msvcrt.html#other-functions "Link to this heading")

msvcrt.heapmin()[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.heapmin "Link to this definition")

Force the `malloc()` heap to clean itself up and return unused blocks to the operating system. On failure, this raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

msvcrt.set_error_mode(_mode_)[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.set_error_mode "Link to this definition")

Changes the location where the C runtime writes an error message for an error that might end the program. _mode_ must be one of the `OUT_*` constants listed below or [`REPORT_ERRMODE`](https://docs.python.org/3/library/msvcrt.html#msvcrt.REPORT_ERRMODE "msvcrt.REPORT_ERRMODE"). Returns the old setting or -1 if an error occurs. Only available in [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build).

msvcrt.OUT_TO_DEFAULT[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.OUT_TO_DEFAULT "Link to this definition")

Error sink is determined by the app’s type. Only available in [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build).

msvcrt.OUT_TO_STDERR[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.OUT_TO_STDERR "Link to this definition")

Error sink is a standard error. Only available in [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build).

msvcrt.OUT_TO_MSGBOX[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.OUT_TO_MSGBOX "Link to this definition")

Error sink is a message box. Only available in [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build).

msvcrt.REPORT_ERRMODE[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.REPORT_ERRMODE "Link to this definition")

Report the current error mode value. Only available in [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build).

msvcrt.CrtSetReportMode(_type_ , _mode_)[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.CrtSetReportMode "Link to this definition")

Specifies the destination or destinations for a specific report type generated by `_CrtDbgReport()` in the MS VC++ runtime. _type_ must be one of the `CRT_*` constants listed below. _mode_ must be one of the `CRTDBG_*` constants listed below. Only available in [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build).

msvcrt.CrtSetReportFile(_type_ , _file_)[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.CrtSetReportFile "Link to this definition")

After you use [`CrtSetReportMode()`](https://docs.python.org/3/library/msvcrt.html#msvcrt.CrtSetReportMode "msvcrt.CrtSetReportMode") to specify [`CRTDBG_MODE_FILE`](https://docs.python.org/3/library/msvcrt.html#msvcrt.CRTDBG_MODE_FILE "msvcrt.CRTDBG_MODE_FILE"), you can specify the file handle to receive the message text. _type_ must be one of the `CRT_*` constants listed below. _file_ should be the file handle your want specified. Only available in [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build).

msvcrt.CRT_WARN[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.CRT_WARN "Link to this definition")

Warnings, messages, and information that doesn’t need immediate attention.

msvcrt.CRT_ERROR[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.CRT_ERROR "Link to this definition")

Errors, unrecoverable problems, and issues that require immediate attention.

msvcrt.CRT_ASSERT[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.CRT_ASSERT "Link to this definition")

Assertion failures.

msvcrt.CRTDBG_MODE_DEBUG[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.CRTDBG_MODE_DEBUG "Link to this definition")

Writes the message to the debugger’s output window.

msvcrt.CRTDBG_MODE_FILE[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.CRTDBG_MODE_FILE "Link to this definition")

Writes the message to a user-supplied file handle. [`CrtSetReportFile()`](https://docs.python.org/3/library/msvcrt.html#msvcrt.CrtSetReportFile "msvcrt.CrtSetReportFile") should be called to define the specific file or stream to use as the destination.

msvcrt.CRTDBG_MODE_WNDW[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.CRTDBG_MODE_WNDW "Link to this definition")

Creates a message box to display the message along with the `Abort`, `Retry`, and `Ignore` buttons.

msvcrt.CRTDBG_REPORT_MODE[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.CRTDBG_REPORT_MODE "Link to this definition")

Returns current _mode_ for the specified _type_.

msvcrt.CRT_ASSEMBLY_VERSION[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.CRT_ASSEMBLY_VERSION "Link to this definition")

The CRT Assembly version, from the `crtassem.h` header file.

msvcrt.VC_ASSEMBLY_PUBLICKEYTOKEN[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.VC_ASSEMBLY_PUBLICKEYTOKEN "Link to this definition")

The VC Assembly public key token, from the `crtassem.h` header file.

msvcrt.LIBRARIES_ASSEMBLY_NAME_PREFIX[¶](https://docs.python.org/3/library/msvcrt.html#msvcrt.LIBRARIES_ASSEMBLY_NAME_PREFIX "Link to this definition")

The Libraries Assembly name prefix, from the `crtassem.h` header file.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`msvcrt` — Useful routines from the MS VC++ runtime](https://docs.python.org/3/library/msvcrt.html)
    * [File Operations](https://docs.python.org/3/library/msvcrt.html#file-operations)
    * [Console I/O](https://docs.python.org/3/library/msvcrt.html#console-i-o)
    * [Other Functions](https://docs.python.org/3/library/msvcrt.html#other-functions)


#### Previous topic
[MS Windows Specific Services](https://docs.python.org/3/library/windows.html "previous chapter")
#### Next topic
[`winreg` — Windows registry access](https://docs.python.org/3/library/winreg.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=msvcrt+%E2%80%94+Useful+routines+from+the+MS+VC%2B%2B+runtime&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmsvcrt.html&pagesource=library%2Fmsvcrt.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/winreg.html "winreg — Windows registry access") |
  * [previous](https://docs.python.org/3/library/windows.html "MS Windows Specific Services") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [MS Windows Specific Services](https://docs.python.org/3/library/windows.html) »
  * [`msvcrt` — Useful routines from the MS VC++ runtime](https://docs.python.org/3/library/msvcrt.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
