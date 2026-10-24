[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`optparse` — Parser for command line options](https://docs.python.org/3/library/optparse.html "previous chapter")
#### Next topic
[`fileinput` — Iterate over lines from multiple input streams](https://docs.python.org/3/library/fileinput.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=getpass+%E2%80%94+Portable+password+input&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgetpass.html&pagesource=library%2Fgetpass.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/fileinput.html "fileinput — Iterate over lines from multiple input streams") |
  * [previous](https://docs.python.org/3/library/optparse.html "optparse — Parser for command line options") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`getpass` — Portable password input](https://docs.python.org/3/library/getpass.html)
  * |
  * Theme  Auto Light Dark |


#  `getpass` — Portable password input[¶](https://docs.python.org/3/library/getpass.html#module-getpass "Link to this heading")
**Source code:**
* * *
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
The `getpass` module provides two functions:

getpass.getpass(_prompt ='Password: '_, _stream =None_, _*_ , _echo_char =None_)[¶](https://docs.python.org/3/library/getpass.html#getpass.getpass "Link to this definition")

Prompt the user for a password without echoing. The user is prompted using the string _prompt_ , which defaults to `'Password: '`. On Unix, the prompt is written to the file-like object _stream_ using the replace error handler if needed. _stream_ defaults to the controlling terminal (`/dev/tty`) or if that is unavailable to `sys.stderr` (this argument is ignored on Windows).
The _echo_char_ argument controls how user input is displayed while typing. If _echo_char_ is `None` (default), input remains hidden. Otherwise, _echo_char_ must be a single printable ASCII character and each typed character is replaced by it. For example, `echo_char='*'` will display asterisks instead of the actual input.
If echo free input is unavailable getpass() falls back to printing a warning message to _stream_ and reading from `sys.stdin` and issuing a [`GetPassWarning`](https://docs.python.org/3/library/getpass.html#getpass.GetPassWarning "getpass.GetPassWarning").
Note
If you call getpass from within IDLE, the input may be done in the terminal you launched IDLE from rather than the idle window itself.
Note
On Unix systems, when _echo_char_ is set, the terminal will be configured to operate in `Ctrl`+`U` will not work and may insert unexpected characters into the input.
Changed in version 3.14: Added the _echo_char_ parameter for keyboard feedback.

_exception_ getpass.GetPassWarning[¶](https://docs.python.org/3/library/getpass.html#getpass.GetPassWarning "Link to this definition")

A [`UserWarning`](https://docs.python.org/3/library/exceptions.html#UserWarning "UserWarning") subclass issued when password input may be echoed.

getpass.getuser()[¶](https://docs.python.org/3/library/getpass.html#getpass.getuser "Link to this definition")

Return the “login name” of the user.
This function checks the environment variables `LOGNAME`, `USER`, `LNAME` and `USERNAME`, in order, and returns the value of the first one which is set to a non-empty string. If none are set, the login name from the password database is returned on systems which support the [`pwd`](https://docs.python.org/3/library/pwd.html#module-pwd "pwd: The password database \(getpwnam\(\) and friends\).") module, otherwise, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised.
In general, this function should be preferred over [`os.getlogin()`](https://docs.python.org/3/library/os.html#os.getlogin "os.getlogin").
Changed in version 3.13: Previously, various exceptions beyond just [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") were raised.
#### Previous topic
[`optparse` — Parser for command line options](https://docs.python.org/3/library/optparse.html "previous chapter")
#### Next topic
[`fileinput` — Iterate over lines from multiple input streams](https://docs.python.org/3/library/fileinput.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=getpass+%E2%80%94+Portable+password+input&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgetpass.html&pagesource=library%2Fgetpass.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/fileinput.html "fileinput — Iterate over lines from multiple input streams") |
  * [previous](https://docs.python.org/3/library/optparse.html "optparse — Parser for command line options") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
  * [`getpass` — Portable password input](https://docs.python.org/3/library/getpass.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
