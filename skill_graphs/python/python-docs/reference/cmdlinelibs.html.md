[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`ctypes` — A foreign function library for Python](https://docs.python.org/3/library/ctypes.html "previous chapter")
#### Next topic
[`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Command-line+interface+libraries&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcmdlinelibs.html&pagesource=library%2Fcmdlinelibs.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/argparse.html "argparse — Parser for command-line options, arguments and subcommands") |
  * [previous](https://docs.python.org/3/library/ctypes.html "ctypes — A foreign function library for Python") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html)
  * |
  * Theme  Auto Light Dark |


# Command-line interface libraries[¶](https://docs.python.org/3/library/cmdlinelibs.html#command-line-interface-libraries "Link to this heading")
The modules described in this chapter assist with implementing command line and terminal interfaces for applications.
Here’s an overview:
  * [`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html)
  * [`optparse` — Parser for command line options](https://docs.python.org/3/library/optparse.html)
  * [`getpass` — Portable password input](https://docs.python.org/3/library/getpass.html)
  * [`fileinput` — Iterate over lines from multiple input streams](https://docs.python.org/3/library/fileinput.html)
  * [`curses` — Terminal handling for character-cell displays](https://docs.python.org/3/library/curses.html)
  * [`curses.textpad` — Text input widget for curses programs](https://docs.python.org/3/library/curses.html#module-curses.textpad)
  * [`curses.ascii` — Utilities for ASCII characters](https://docs.python.org/3/library/curses.ascii.html)
  * [`curses.panel` — A panel stack extension for curses](https://docs.python.org/3/library/curses.panel.html)
  * [`cmd` — Support for line-oriented command interpreters](https://docs.python.org/3/library/cmd.html)


#### Previous topic
[`ctypes` — A foreign function library for Python](https://docs.python.org/3/library/ctypes.html "previous chapter")
#### Next topic
[`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Command-line+interface+libraries&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcmdlinelibs.html&pagesource=library%2Fcmdlinelibs.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/argparse.html "argparse — Parser for command-line options, arguments and subcommands") |
  * [previous](https://docs.python.org/3/library/ctypes.html "ctypes — A foreign function library for Python") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
