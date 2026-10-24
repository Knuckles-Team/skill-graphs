[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`winsound` — Sound-playing interface for Windows](https://docs.python.org/3/library/winsound.html "previous chapter")
#### Next topic
[`shlex` — Simple lexical analysis](https://docs.python.org/3/library/shlex.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Unix-specific+services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funix.html&pagesource=library%2Funix.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/shlex.html "shlex — Simple lexical analysis") |
  * [previous](https://docs.python.org/3/library/winsound.html "winsound — Sound-playing interface for Windows") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html)
  * |
  * Theme  Auto Light Dark |


# Unix-specific services[¶](https://docs.python.org/3/library/unix.html#unix-specific-services "Link to this heading")
The modules described in this chapter provide interfaces to features that are unique to the Unix operating system, or in some cases to some or many variants of it. Here’s an overview:
  * [`shlex` — Simple lexical analysis](https://docs.python.org/3/library/shlex.html)
    * [shlex Objects](https://docs.python.org/3/library/shlex.html#shlex-objects)
    * [Parsing Rules](https://docs.python.org/3/library/shlex.html#parsing-rules)
    * [Improved Compatibility with Shells](https://docs.python.org/3/library/shlex.html#improved-compatibility-with-shells)
  * [`posix` — The most common POSIX system calls](https://docs.python.org/3/library/posix.html)
    * [Large File Support](https://docs.python.org/3/library/posix.html#large-file-support)
    * [Notable Module Contents](https://docs.python.org/3/library/posix.html#notable-module-contents)
  * [`pwd` — The password database](https://docs.python.org/3/library/pwd.html)
  * [`grp` — The group database](https://docs.python.org/3/library/grp.html)
  * [`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html)
    * [Example](https://docs.python.org/3/library/termios.html#example)
  * [`tty` — Terminal control functions](https://docs.python.org/3/library/tty.html)
  * [`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html)
    * [Example](https://docs.python.org/3/library/pty.html#example)
  * [`fcntl` — The `fcntl` and `ioctl` system calls](https://docs.python.org/3/library/fcntl.html)
  * [`resource` — Resource usage information](https://docs.python.org/3/library/resource.html)
    * [Resource Limits](https://docs.python.org/3/library/resource.html#resource-limits)
    * [Resource Usage](https://docs.python.org/3/library/resource.html#resource-usage)
  * [`syslog` — Unix syslog library routines](https://docs.python.org/3/library/syslog.html)
    * [Examples](https://docs.python.org/3/library/syslog.html#examples)
      * [Simple example](https://docs.python.org/3/library/syslog.html#simple-example)


#### Previous topic
[`winsound` — Sound-playing interface for Windows](https://docs.python.org/3/library/winsound.html "previous chapter")
#### Next topic
[`shlex` — Simple lexical analysis](https://docs.python.org/3/library/shlex.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Unix-specific+services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Funix.html&pagesource=library%2Funix.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/shlex.html "shlex — Simple lexical analysis") |
  * [previous](https://docs.python.org/3/library/winsound.html "winsound — Sound-playing interface for Windows") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
