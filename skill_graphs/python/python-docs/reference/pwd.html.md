[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`posix` — The most common POSIX system calls](https://docs.python.org/3/library/posix.html "previous chapter")
#### Next topic
[`grp` — The group database](https://docs.python.org/3/library/grp.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pwd+%E2%80%94+The+password+database&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpwd.html&pagesource=library%2Fpwd.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/grp.html "grp — The group database") |
  * [previous](https://docs.python.org/3/library/posix.html "posix — The most common POSIX system calls") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html) »
  * [`pwd` — The password database](https://docs.python.org/3/library/pwd.html)
  * |
  * Theme  Auto Light Dark |


#  `pwd` — The password database[¶](https://docs.python.org/3/library/pwd.html#module-pwd "Link to this heading")
* * *
This module provides access to the Unix user account and password database. It is available on all Unix versions.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not iOS.
Password database entries are reported as a tuple-like object, whose attributes correspond to the members of the `passwd` structure (Attribute field below, see `<pwd.h>`):
Index | Attribute | Meaning
---|---|---
0 | `pw_name` | Login name
1 | `pw_passwd` | Optional encrypted password
2 | `pw_uid` | Numerical user ID
3 | `pw_gid` | Numerical group ID
4 | `pw_gecos` | User name or comment field
5 | `pw_dir` | User home directory
6 | `pw_shell` | User command interpreter
The uid and gid items are integers, all others are strings. [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised if the entry asked for cannot be found.
Note
In traditional Unix the field `pw_passwd` usually contains a password encrypted with a DES derived algorithm. However most modern unices use a so-called _shadow password_ system. On those unices the _pw_passwd_ field only contains an asterisk (`'*'`) or the letter `'x'` where the encrypted password is stored in a file `/etc/shadow` which is not world readable. Whether the _pw_passwd_ field contains anything useful is system-dependent.
It defines the following items:

pwd.getpwuid(_uid_)[¶](https://docs.python.org/3/library/pwd.html#pwd.getpwuid "Link to this definition")

Return the password database entry for the given numeric user ID.

pwd.getpwnam(_name_)[¶](https://docs.python.org/3/library/pwd.html#pwd.getpwnam "Link to this definition")

Return the password database entry for the given user name.

pwd.getpwall()[¶](https://docs.python.org/3/library/pwd.html#pwd.getpwall "Link to this definition")

Return a list of all available password database entries, in arbitrary order.
See also

Module [`grp`](https://docs.python.org/3/library/grp.html#module-grp "grp: The group database \(getgrnam\(\) and friends\).")

An interface to the group database, similar to this.
#### Previous topic
[`posix` — The most common POSIX system calls](https://docs.python.org/3/library/posix.html "previous chapter")
#### Next topic
[`grp` — The group database](https://docs.python.org/3/library/grp.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pwd+%E2%80%94+The+password+database&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpwd.html&pagesource=library%2Fpwd.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/grp.html "grp — The group database") |
  * [previous](https://docs.python.org/3/library/posix.html "posix — The most common POSIX system calls") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html) »
  * [`pwd` — The password database](https://docs.python.org/3/library/pwd.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
