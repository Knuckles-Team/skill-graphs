[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`pwd` — The password database](https://docs.python.org/3/library/pwd.html "previous chapter")
#### Next topic
[`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=grp+%E2%80%94+The+group+database&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgrp.html&pagesource=library%2Fgrp.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/termios.html "termios — POSIX style tty control") |
  * [previous](https://docs.python.org/3/library/pwd.html "pwd — The password database") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html) »
  * [`grp` — The group database](https://docs.python.org/3/library/grp.html)
  * |
  * Theme  Auto Light Dark |


#  `grp` — The group database[¶](https://docs.python.org/3/library/grp.html#module-grp "Link to this heading")
* * *
This module provides access to the Unix group database. It is available on all Unix versions.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not Android, not iOS.
Group database entries are reported as a tuple-like object, whose attributes correspond to the members of the `group` structure (Attribute field below, see `<grp.h>`):
Index | Attribute | Meaning
---|---|---
0 | gr_name | the name of the group
1 | gr_passwd | the (encrypted) group password; often empty
2 | gr_gid | the numerical group ID
3 | gr_mem | all the group member’s user names
The gid is an integer, name and password are strings, and the member list is a list of strings. (Note that most users are not explicitly listed as members of the group they are in according to the password database. Check both databases to get complete membership information. Also note that a `gr_name` that starts with a `+` or `-` is likely to be a YP/NIS reference and may not be accessible via [`getgrnam()`](https://docs.python.org/3/library/grp.html#grp.getgrnam "grp.getgrnam") or [`getgrgid()`](https://docs.python.org/3/library/grp.html#grp.getgrgid "grp.getgrgid").)
It defines the following items:

grp.getgrgid(_id_)[¶](https://docs.python.org/3/library/grp.html#grp.getgrgid "Link to this definition")

Return the group database entry for the given numeric group ID. [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised if the entry asked for cannot be found.
Changed in version 3.10: [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised for non-integer arguments like floats or strings.

grp.getgrnam(_name_)[¶](https://docs.python.org/3/library/grp.html#grp.getgrnam "Link to this definition")

Return the group database entry for the given group name. [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised if the entry asked for cannot be found.

grp.getgrall()[¶](https://docs.python.org/3/library/grp.html#grp.getgrall "Link to this definition")

Return a list of all available group entries, in arbitrary order.
See also

Module [`pwd`](https://docs.python.org/3/library/pwd.html#module-pwd "pwd: The password database \(getpwnam\(\) and friends\).")

An interface to the user database, similar to this.
#### Previous topic
[`pwd` — The password database](https://docs.python.org/3/library/pwd.html "previous chapter")
#### Next topic
[`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=grp+%E2%80%94+The+group+database&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgrp.html&pagesource=library%2Fgrp.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/termios.html "termios — POSIX style tty control") |
  * [previous](https://docs.python.org/3/library/pwd.html "pwd — The password database") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html) »
  * [`grp` — The group database](https://docs.python.org/3/library/grp.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
