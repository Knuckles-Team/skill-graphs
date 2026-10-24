[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html)
    * [Example](https://docs.python.org/3/library/termios.html#example)


#### Previous topic
[`grp` — The group database](https://docs.python.org/3/library/grp.html "previous chapter")
#### Next topic
[`tty` — Terminal control functions](https://docs.python.org/3/library/tty.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=termios+%E2%80%94+POSIX+style+tty+control&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftermios.html&pagesource=library%2Ftermios.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tty.html "tty — Terminal control functions") |
  * [previous](https://docs.python.org/3/library/grp.html "grp — The group database") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html) »
  * [`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html)
  * |
  * Theme  Auto Light Dark |


#  `termios` — POSIX style tty control[¶](https://docs.python.org/3/library/termios.html#module-termios "Link to this heading")
* * *
This module provides an interface to the POSIX calls for tty I/O control. For a complete description of these calls, see _termios_ style tty I/O control configured during installation.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
All functions in this module take a file descriptor _fd_ as their first argument. This can be an integer file descriptor, such as returned by `sys.stdin.fileno()`, or a [file object](https://docs.python.org/3/glossary.html#term-file-object), such as `sys.stdin` itself.
This module also defines all the constants needed to work with the functions provided here; these have the same name as their counterparts in C. Please refer to your system documentation for more information on using these terminal control interfaces.
The module defines the following functions:

termios.tcgetattr(_fd_)[¶](https://docs.python.org/3/library/termios.html#termios.tcgetattr "Link to this definition")

Return a list containing the tty attributes for file descriptor _fd_ , as follows: `[iflag, oflag, cflag, lflag, ispeed, ospeed, cc]` where _cc_ is a list of the tty special characters (each a string of length 1, except the items with indices `VMIN` and `VTIME`, which are integers when these fields are defined). The interpretation of the flags and the speeds as well as the indexing in the _cc_ array must be done using the symbolic constants defined in the `termios` module.

termios.tcsetattr(_fd_ , _when_ , _attributes_)[¶](https://docs.python.org/3/library/termios.html#termios.tcsetattr "Link to this definition")

Set the tty attributes for file descriptor _fd_ from the _attributes_ , which is a list like the one returned by [`tcgetattr()`](https://docs.python.org/3/library/termios.html#termios.tcgetattr "termios.tcgetattr"). The _when_ argument determines when the attributes are changed:

termios.TCSANOW[¶](https://docs.python.org/3/library/termios.html#termios.TCSANOW "Link to this definition")

Change attributes immediately.

termios.TCSADRAIN[¶](https://docs.python.org/3/library/termios.html#termios.TCSADRAIN "Link to this definition")

Change attributes after transmitting all queued output.

termios.TCSAFLUSH[¶](https://docs.python.org/3/library/termios.html#termios.TCSAFLUSH "Link to this definition")

Change attributes after transmitting all queued output and discarding all queued input.

termios.tcsendbreak(_fd_ , _duration_)[¶](https://docs.python.org/3/library/termios.html#termios.tcsendbreak "Link to this definition")

Send a break on file descriptor _fd_. A zero _duration_ sends a break for 0.25–0.5 seconds; a nonzero _duration_ has a system dependent meaning.

termios.tcdrain(_fd_)[¶](https://docs.python.org/3/library/termios.html#termios.tcdrain "Link to this definition")

Wait until all output written to file descriptor _fd_ has been transmitted.

termios.tcflush(_fd_ , _queue_)[¶](https://docs.python.org/3/library/termios.html#termios.tcflush "Link to this definition")

Discard queued data on file descriptor _fd_. The _queue_ selector specifies which queue: `TCIFLUSH` for the input queue, `TCOFLUSH` for the output queue, or `TCIOFLUSH` for both queues.

termios.tcflow(_fd_ , _action_)[¶](https://docs.python.org/3/library/termios.html#termios.tcflow "Link to this definition")

Suspend or resume input or output on file descriptor _fd_. The _action_ argument can be `TCOOFF` to suspend output, `TCOON` to restart output, `TCIOFF` to suspend input, or `TCION` to restart input.

termios.tcgetwinsize(_fd_)[¶](https://docs.python.org/3/library/termios.html#termios.tcgetwinsize "Link to this definition")

Return a tuple `(ws_row, ws_col)` containing the tty window size for file descriptor _fd_. Requires `termios.TIOCGWINSZ` or `termios.TIOCGSIZE`.
Added in version 3.11.

termios.tcsetwinsize(_fd_ , _winsize_)[¶](https://docs.python.org/3/library/termios.html#termios.tcsetwinsize "Link to this definition")

Set the tty window size for file descriptor _fd_ from _winsize_ , which is a two-item tuple `(ws_row, ws_col)` like the one returned by [`tcgetwinsize()`](https://docs.python.org/3/library/termios.html#termios.tcgetwinsize "termios.tcgetwinsize"). Requires at least one of the pairs (`termios.TIOCGWINSZ`, `termios.TIOCSWINSZ`); (`termios.TIOCGSIZE`, `termios.TIOCSSIZE`) to be defined.
Added in version 3.11.
See also

Module [`tty`](https://docs.python.org/3/library/tty.html#module-tty "tty: Utility functions that perform common terminal control operations.")

Convenience functions for common terminal control operations.
## Example[¶](https://docs.python.org/3/library/termios.html#example "Link to this heading")
Here’s a function that prompts for a password with echoing turned off. Note the technique using a separate [`tcgetattr()`](https://docs.python.org/3/library/termios.html#termios.tcgetattr "termios.tcgetattr") call and a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) … [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) statement to ensure that the old tty attributes are restored exactly no matter what happens:
Copy```
def getpass(prompt="Password: "):
    import termios, sys
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ECHO          # lflags
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        passwd = input(prompt)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return passwd

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html)
    * [Example](https://docs.python.org/3/library/termios.html#example)


#### Previous topic
[`grp` — The group database](https://docs.python.org/3/library/grp.html "previous chapter")
#### Next topic
[`tty` — Terminal control functions](https://docs.python.org/3/library/tty.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=termios+%E2%80%94+POSIX+style+tty+control&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftermios.html&pagesource=library%2Ftermios.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/tty.html "tty — Terminal control functions") |
  * [previous](https://docs.python.org/3/library/grp.html "grp — The group database") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html) »
  * [`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
