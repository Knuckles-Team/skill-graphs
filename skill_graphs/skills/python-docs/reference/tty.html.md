[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html "previous chapter")
#### Next topic
[`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tty+%E2%80%94+Terminal+control+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftty.html&pagesource=library%2Ftty.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pty.html "pty — Pseudo-terminal utilities") |
  * [previous](https://docs.python.org/3/library/termios.html "termios — POSIX style tty control") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html) »
  * [`tty` — Terminal control functions](https://docs.python.org/3/library/tty.html)
  * |
  * Theme  Auto Light Dark |


#  `tty` — Terminal control functions[¶](https://docs.python.org/3/library/tty.html#module-tty "Link to this heading")
**Source code:**
* * *
The `tty` module defines functions for putting the tty into cbreak and raw modes.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Because it requires the [`termios`](https://docs.python.org/3/library/termios.html#module-termios "termios: POSIX style tty control.") module, it will work only on Unix.
The `tty` module defines the following functions:

tty.cfmakeraw(_mode_)[¶](https://docs.python.org/3/library/tty.html#tty.cfmakeraw "Link to this definition")

Convert the tty attribute list _mode_ , which is a list like the one returned by [`termios.tcgetattr()`](https://docs.python.org/3/library/termios.html#termios.tcgetattr "termios.tcgetattr"), to that of a tty in raw mode.
Added in version 3.12.

tty.cfmakecbreak(_mode_)[¶](https://docs.python.org/3/library/tty.html#tty.cfmakecbreak "Link to this definition")

Convert the tty attribute list _mode_ , which is a list like the one returned by [`termios.tcgetattr()`](https://docs.python.org/3/library/termios.html#termios.tcgetattr "termios.tcgetattr"), to that of a tty in cbreak mode.
This clears the `ECHO` and `ICANON` local mode flags in _mode_ as well as setting the minimum input to 1 byte with no delay.
Added in version 3.12.
Changed in version 3.12.2: The `ICRNL` flag is no longer cleared. This matches Linux and macOS `stty cbreak` behavior and what [`setcbreak()`](https://docs.python.org/3/library/tty.html#tty.setcbreak "tty.setcbreak") historically did.

tty.setraw(_fd_ , _when =termios.TCSAFLUSH_)[¶](https://docs.python.org/3/library/tty.html#tty.setraw "Link to this definition")

Change the mode of the file descriptor _fd_ to raw. If _when_ is omitted, it defaults to [`termios.TCSAFLUSH`](https://docs.python.org/3/library/termios.html#termios.TCSAFLUSH "termios.TCSAFLUSH"), and is passed to [`termios.tcsetattr()`](https://docs.python.org/3/library/termios.html#termios.tcsetattr "termios.tcsetattr"). The return value of [`termios.tcgetattr()`](https://docs.python.org/3/library/termios.html#termios.tcgetattr "termios.tcgetattr") is saved before setting _fd_ to raw mode; this value is returned.
Changed in version 3.12: The return value is now the original tty attributes, instead of `None`.

tty.setcbreak(_fd_ , _when =termios.TCSAFLUSH_)[¶](https://docs.python.org/3/library/tty.html#tty.setcbreak "Link to this definition")

Change the mode of file descriptor _fd_ to cbreak. If _when_ is omitted, it defaults to [`termios.TCSAFLUSH`](https://docs.python.org/3/library/termios.html#termios.TCSAFLUSH "termios.TCSAFLUSH"), and is passed to [`termios.tcsetattr()`](https://docs.python.org/3/library/termios.html#termios.tcsetattr "termios.tcsetattr"). The return value of [`termios.tcgetattr()`](https://docs.python.org/3/library/termios.html#termios.tcgetattr "termios.tcgetattr") is saved before setting _fd_ to cbreak mode; this value is returned.
This clears the `ECHO` and `ICANON` local mode flags as well as setting the minimum input to 1 byte with no delay.
Changed in version 3.12: The return value is now the original tty attributes, instead of `None`.
Changed in version 3.12.2: The `ICRNL` flag is no longer cleared. This restores the behavior of Python 3.11 and earlier as well as matching what Linux, macOS, & BSDs describe in their `stty(1)` man pages regarding cbreak mode.
See also

Module [`termios`](https://docs.python.org/3/library/termios.html#module-termios "termios: POSIX style tty control.")

Low-level terminal control interface.
#### Previous topic
[`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html "previous chapter")
#### Next topic
[`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tty+%E2%80%94+Terminal+control+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftty.html&pagesource=library%2Ftty.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/pty.html "pty — Pseudo-terminal utilities") |
  * [previous](https://docs.python.org/3/library/termios.html "termios — POSIX style tty control") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html) »
  * [`tty` — Terminal control functions](https://docs.python.org/3/library/tty.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
