[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html)
    * [Example](https://docs.python.org/3/library/pty.html#example)


#### Previous topic
[`tty` — Terminal control functions](https://docs.python.org/3/library/tty.html "previous chapter")
#### Next topic
[`fcntl` — The `fcntl` and `ioctl` system calls](https://docs.python.org/3/library/fcntl.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pty+%E2%80%94+Pseudo-terminal+utilities&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpty.html&pagesource=library%2Fpty.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/fcntl.html "fcntl — The fcntl and ioctl system calls") |
  * [previous](https://docs.python.org/3/library/tty.html "tty — Terminal control functions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html) »
  * [`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html)
  * |
  * Theme  Auto Light Dark |


#  `pty` — Pseudo-terminal utilities[¶](https://docs.python.org/3/library/pty.html#module-pty "Link to this heading")
**Source code:**
* * *
The `pty` module defines operations for handling the pseudo-terminal concept: starting another process and being able to write to and read from its controlling terminal programmatically.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Pseudo-terminal handling is highly platform dependent. This code is mainly tested on Linux, FreeBSD, and macOS (it is supposed to work on other POSIX platforms but it’s not been thoroughly tested).
The `pty` module defines the following functions:

pty.fork()[¶](https://docs.python.org/3/library/pty.html#pty.fork "Link to this definition")

Fork. Connect the child’s controlling terminal to a pseudo-terminal. Return value is `(pid, fd)`. Note that the child gets _pid_ 0, and the _fd_ is _invalid_. The parent’s return value is the _pid_ of the child, and _fd_ is a file descriptor connected to the child’s controlling terminal (and also to the child’s standard input and output).
Warning
On macOS the use of this function is unsafe when mixed with using higher-level system APIs, and that includes using [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.").

pty.openpty()[¶](https://docs.python.org/3/library/pty.html#pty.openpty "Link to this definition")

Open a new pseudo-terminal pair, using [`os.openpty()`](https://docs.python.org/3/library/os.html#os.openpty "os.openpty") if possible, or emulation code for generic Unix systems. Return a pair of file descriptors `(master, slave)`, for the master and the slave end, respectively.

pty.spawn(_argv_[, _master_read_[, _stdin_read_]])[¶](https://docs.python.org/3/library/pty.html#pty.spawn "Link to this definition")

Spawn a process, and connect its controlling terminal with the current process’s standard io. This is often used to baffle programs which insist on reading from the controlling terminal. It is expected that the process spawned behind the pty will eventually terminate, and when it does _spawn_ will return.
A loop copies STDIN of the current process to the child and data received from the child to STDOUT of the current process. It is not signaled to the child if STDIN of the current process closes down.
The functions _master_read_ and _stdin_read_ are passed a file descriptor which they should read from, and they should always return a byte string. In order to force spawn to return before the child process exits an empty byte array should be returned to signal end of file.
The default implementation for both functions will read and return up to 1024 bytes each time the function is called. The _master_read_ callback is passed the pseudoterminal’s master file descriptor to read output from the child process, and _stdin_read_ is passed file descriptor 0, to read from the parent process’s standard input.
Returning an empty byte string from either callback is interpreted as an end-of-file (EOF) condition, and that callback will not be called after that. If _stdin_read_ signals EOF the controlling terminal can no longer communicate with the parent process OR the child process. Unless the child process will quit without any input, _spawn_ will then loop forever. If _master_read_ signals EOF the same behavior results (on linux at least).
Return the exit status value from [`os.waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid") on the child process.
[`os.waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode") can be used to convert the exit status into an exit code.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `pty.spawn` with argument `argv`.
Changed in version 3.4: `spawn()` now returns the status value from [`os.waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid") on the child process.
## Example[¶](https://docs.python.org/3/library/pty.html#example "Link to this heading")
The following program acts like the Unix command
Copy```
import argparse
import os
import pty
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('-a', dest='append', action='store_true')
parser.add_argument('-p', dest='use_python', action='store_true')
parser.add_argument('filename', nargs='?', default='typescript')
options = parser.parse_args()

shell = sys.executable if options.use_python else os.environ.get('SHELL', 'sh')
filename = options.filename
mode = 'ab' if options.append else 'wb'

with open(filename, mode) as script:
    def read(fd):
        data = os.read(fd, 1024)
        script.write(data)
        return data

    print('Script started, file is', filename)
    script.write(('Script started on %s\n' % time.asctime()).encode())

    pty.spawn(shell, read)

    script.write(('Script done on %s\n' % time.asctime()).encode())
    print('Script done, file is', filename)

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html)
    * [Example](https://docs.python.org/3/library/pty.html#example)


#### Previous topic
[`tty` — Terminal control functions](https://docs.python.org/3/library/tty.html "previous chapter")
#### Next topic
[`fcntl` — The `fcntl` and `ioctl` system calls](https://docs.python.org/3/library/fcntl.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pty+%E2%80%94+Pseudo-terminal+utilities&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpty.html&pagesource=library%2Fpty.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/fcntl.html "fcntl — The fcntl and ioctl system calls") |
  * [previous](https://docs.python.org/3/library/tty.html "tty — Terminal control functions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Unix-specific services](https://docs.python.org/3/library/unix.html) »
  * [`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
