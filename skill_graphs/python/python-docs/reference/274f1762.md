## Random numbers[¶](https://docs.python.org/3/library/os.html#random-numbers "Link to this heading")

os.getrandom(_size_ , _flags =0_)[¶](https://docs.python.org/3/library/os.html#os.getrandom "Link to this definition")

Get up to _size_ random bytes. The function can return less bytes than requested.
These bytes can be used to seed user-space random number generators or for cryptographic purposes.
`getrandom()` relies on entropy gathered from device drivers and other sources of environmental noise. Unnecessarily reading large quantities of data will have a negative impact on other users of the `/dev/random` and `/dev/urandom` devices.
The flags argument is a bit mask that can contain zero or more of the following values ORed together: [`os.GRND_RANDOM`](https://docs.python.org/3/library/os.html#os.GRND_RANDOM "os.GRND_RANDOM") and [`GRND_NONBLOCK`](https://docs.python.org/3/library/os.html#os.GRND_NONBLOCK "os.GRND_NONBLOCK").
See also the
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 3.17.
Added in version 3.6.

os.urandom(_size_ , _/_)[¶](https://docs.python.org/3/library/os.html#os.urandom "Link to this definition")

Return a bytestring of _size_ random bytes suitable for cryptographic use.
This function returns random bytes from an OS-specific randomness source. The returned data should be unpredictable enough for cryptographic applications, though its exact quality depends on the OS implementation.
On Linux, if the `getrandom()` syscall is available, it is used in blocking mode: block until the system urandom entropy pool is initialized (128 bits of entropy are collected by the kernel). See the [**PEP 524**](https://peps.python.org/pep-0524/) for the rationale. On Linux, the [`getrandom()`](https://docs.python.org/3/library/os.html#os.getrandom "os.getrandom") function can be used to get random bytes in non-blocking mode (using the [`GRND_NONBLOCK`](https://docs.python.org/3/library/os.html#os.GRND_NONBLOCK "os.GRND_NONBLOCK") flag) or to poll until the system urandom entropy pool is initialized.
On a Unix-like system, random bytes are read from the `/dev/urandom` device. If the `/dev/urandom` device is not available or not readable, the [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") exception is raised.
On Windows, it will use `BCryptGenRandom()`.
See also
The [`secrets`](https://docs.python.org/3/library/secrets.html#module-secrets "secrets: Generate secure random numbers for managing secrets.") module provides higher level functions. For an easy-to-use interface to the random number generator provided by your platform, please see [`random.SystemRandom`](https://docs.python.org/3/library/random.html#random.SystemRandom "random.SystemRandom").
Changed in version 3.5: On Linux 3.17 and newer, the `getrandom()` syscall is now used when available. On OpenBSD 5.6 and newer, the C `getentropy()` function is now used. These functions avoid the usage of an internal file descriptor.
Changed in version 3.5.2: On Linux, if the `getrandom()` syscall blocks (the urandom entropy pool is not initialized yet), fall back on reading `/dev/urandom`.
Changed in version 3.6: On Linux, `getrandom()` is now used in blocking mode to increase the security.
Changed in version 3.11: On Windows, `BCryptGenRandom()` is used instead of `CryptGenRandom()` which is deprecated.

os.GRND_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.GRND_NONBLOCK "Link to this definition")

By default, when reading from `/dev/random`, [`getrandom()`](https://docs.python.org/3/library/os.html#os.getrandom "os.getrandom") blocks if no random bytes are available, and when reading from `/dev/urandom`, it blocks if the entropy pool has not yet been initialized.
If the `GRND_NONBLOCK` flag is set, then [`getrandom()`](https://docs.python.org/3/library/os.html#os.getrandom "os.getrandom") does not block in these cases, but instead immediately raises [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError").
Added in version 3.6.

os.GRND_RANDOM[¶](https://docs.python.org/3/library/os.html#os.GRND_RANDOM "Link to this definition")

If this bit is set, then random bytes are drawn from the `/dev/random` pool instead of the `/dev/urandom` pool.
Added in version 3.6.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`os` — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)
    * [File Names, Command Line Arguments, and Environment Variables](https://docs.python.org/3/library/os.html#file-names-command-line-arguments-and-environment-variables)
    * [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#python-utf-8-mode)
    * [Process Parameters](https://docs.python.org/3/library/os.html#process-parameters)
    * [File Object Creation](https://docs.python.org/3/library/os.html#file-object-creation)
    * [File Descriptor Operations](https://docs.python.org/3/library/os.html#file-descriptor-operations)
      * [Querying the size of a terminal](https://docs.python.org/3/library/os.html#querying-the-size-of-a-terminal)
      * [Inheritance of File Descriptors](https://docs.python.org/3/library/os.html#inheritance-of-file-descriptors)
    * [Files and Directories](https://docs.python.org/3/library/os.html#files-and-directories)
      * [Timer File Descriptors](https://docs.python.org/3/library/os.html#timer-file-descriptors)
      * [Linux extended attributes](https://docs.python.org/3/library/os.html#linux-extended-attributes)
    * [Process Management](https://docs.python.org/3/library/os.html#process-management)
    * [Interface to the scheduler](https://docs.python.org/3/library/os.html#interface-to-the-scheduler)
    * [Miscellaneous System Information](https://docs.python.org/3/library/os.html#miscellaneous-system-information)
    * [Random numbers](https://docs.python.org/3/library/os.html#random-numbers)


#### Previous topic
[Generic Operating System Services](https://docs.python.org/3/library/allows.html "previous chapter")
#### Next topic
[`io` — Core tools for working with streams](https://docs.python.org/3/library/io.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=os+%E2%80%94+Miscellaneous+operating+system+interfaces&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fos.html&pagesource=library%2Fos.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/io.html "io — Core tools for working with streams") |
  * [previous](https://docs.python.org/3/library/allows.html "Generic Operating System Services") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Generic Operating System Services](https://docs.python.org/3/library/allows.html) »
  * [`os` — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)
