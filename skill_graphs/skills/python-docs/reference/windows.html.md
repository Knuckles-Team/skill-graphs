[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`pickletools` — Tools for pickle developers](https://docs.python.org/3/library/pickletools.html "previous chapter")
#### Next topic
[`msvcrt` — Useful routines from the MS VC++ runtime](https://docs.python.org/3/library/msvcrt.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=MS+Windows+Specific+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fwindows.html&pagesource=library%2Fwindows.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/msvcrt.html "msvcrt — Useful routines from the MS VC++ runtime") |
  * [previous](https://docs.python.org/3/library/pickletools.html "pickletools — Tools for pickle developers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [MS Windows Specific Services](https://docs.python.org/3/library/windows.html)
  * |
  * Theme  Auto Light Dark |


# MS Windows Specific Services[¶](https://docs.python.org/3/library/windows.html#ms-windows-specific-services "Link to this heading")
This chapter describes modules that are only available on MS Windows platforms.
  * [`msvcrt` — Useful routines from the MS VC++ runtime](https://docs.python.org/3/library/msvcrt.html)
    * [File Operations](https://docs.python.org/3/library/msvcrt.html#file-operations)
    * [Console I/O](https://docs.python.org/3/library/msvcrt.html#console-i-o)
    * [Other Functions](https://docs.python.org/3/library/msvcrt.html#other-functions)
  * [`winreg` — Windows registry access](https://docs.python.org/3/library/winreg.html)
    * [Functions](https://docs.python.org/3/library/winreg.html#functions)
    * [Constants](https://docs.python.org/3/library/winreg.html#constants)
      * [HKEY_* Constants](https://docs.python.org/3/library/winreg.html#hkey-constants)
      * [Access Rights](https://docs.python.org/3/library/winreg.html#access-rights)
        * [64-bit Specific](https://docs.python.org/3/library/winreg.html#bit-specific)
      * [Value Types](https://docs.python.org/3/library/winreg.html#value-types)
    * [Registry Handle Objects](https://docs.python.org/3/library/winreg.html#registry-handle-objects)
  * [`winsound` — Sound-playing interface for Windows](https://docs.python.org/3/library/winsound.html)


#### Previous topic
[`pickletools` — Tools for pickle developers](https://docs.python.org/3/library/pickletools.html "previous chapter")
#### Next topic
[`msvcrt` — Useful routines from the MS VC++ runtime](https://docs.python.org/3/library/msvcrt.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=MS+Windows+Specific+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fwindows.html&pagesource=library%2Fwindows.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/msvcrt.html "msvcrt — Useful routines from the MS VC++ runtime") |
  * [previous](https://docs.python.org/3/library/pickletools.html "pickletools — Tools for pickle developers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [MS Windows Specific Services](https://docs.python.org/3/library/windows.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
