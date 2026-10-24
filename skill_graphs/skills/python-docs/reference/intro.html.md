[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [Introduction](https://docs.python.org/3/library/intro.html)
    * [Notes on availability](https://docs.python.org/3/library/intro.html#notes-on-availability)
      * [WebAssembly platforms](https://docs.python.org/3/library/intro.html#webassembly-platforms)
      * [Mobile platforms](https://docs.python.org/3/library/intro.html#mobile-platforms)


#### Previous topic
[The Python Standard Library](https://docs.python.org/3/library/index.html "previous chapter")
#### Next topic
[Built-in Functions](https://docs.python.org/3/library/functions.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Introduction&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fintro.html&pagesource=library%2Fintro.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/functions.html "Built-in Functions") |
  * [previous](https://docs.python.org/3/library/index.html "The Python Standard Library") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Introduction](https://docs.python.org/3/library/intro.html)
  * |
  * Theme  Auto Light Dark |


# Introduction[¶](https://docs.python.org/3/library/intro.html#introduction "Link to this heading")
The “Python library” contains several different kinds of components.
It contains data types that would normally be considered part of the “core” of a language, such as numbers and lists. For these types, the Python language core defines the form of literals and places some constraints on their semantics, but does not fully define the semantics. (On the other hand, the language core does define syntactic properties like the spelling and priorities of operators.)
The library also contains built-in functions and exceptions — objects that can be used by all Python code without the need of an [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement. Some of these are defined by the core language, but many are not essential for the core semantics and are only described here.
The bulk of the library, however, consists of a collection of modules. There are many ways to dissect this collection. Some modules are written in C and built in to the Python interpreter; others are written in Python and imported in source form. Some modules provide interfaces that are highly specific to Python, like printing a stack trace; some provide interfaces that are specific to particular operating systems, such as access to specific hardware; others provide interfaces that are specific to a particular application domain, like the World Wide Web. Some modules are available in all versions and ports of Python; others are only available when the underlying system supports or requires them; yet others are available only when a particular configuration option was chosen at the time when Python was compiled and installed.
This manual is organized “from the inside out:” it first describes the built-in functions, data types and exceptions, and finally the modules, grouped in chapters of related modules.
This means that if you start reading this manual from the start, and skip to the next chapter when you get bored, you will get a reasonable overview of the available modules and application areas that are supported by the Python library. Of course, you don’t _have_ to read it like a novel — you can also browse the table of contents (in front of the manual), or look for a specific function, module or term in the index (in the back). And finally, if you enjoy learning about random subjects, you choose a random page number (see module [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.")) and read a section or two. Regardless of the order in which you read the sections of this manual, it helps to start with chapter [Built-in Functions](https://docs.python.org/3/library/functions.html#built-in-funcs), as the remainder of the manual assumes familiarity with this material.
Let the show begin!
## Notes on availability[¶](https://docs.python.org/3/library/intro.html#notes-on-availability "Link to this heading")
  * An “Availability: Unix” note means that this function is commonly found on Unix systems. It does not make any claims about its existence on a specific operating system.
  * If not separately noted, all functions that claim “Availability: Unix” are supported on macOS, iOS and Android, all of which build on a Unix core.
  * If an availability note contains both a minimum Kernel version and a minimum libc version, then both conditions must hold. For example a feature with note _Availability: Linux >= 3.17 with glibc >= 2.27_ requires both Linux 3.17 or newer and glibc 2.27 or newer.


### WebAssembly platforms[¶](https://docs.python.org/3/library/intro.html#webassembly-platforms "Link to this heading")
The `wasm32-emscripten` (`wasm32-wasi` ([`sleep()`](https://docs.python.org/3/library/time.html#time.sleep "time.sleep") block the browser event loop.
The properties and behavior of Python on WebAssembly platforms depend on the
For Python in the browser, users should consider `XMLHttpRequest` and `Fetch` APIs.
  * Process-related APIs are not available or always fail with an error. That includes APIs that spawn new processes ([`fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork"), [`execve()`](https://docs.python.org/3/library/os.html#os.execve "os.execve")), wait for processes ([`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")), send signals ([`kill()`](https://docs.python.org/3/library/os.html#os.kill "os.kill")), or otherwise interact with processes. The [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") is importable but does not work.
  * The [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") module is available, but is limited and behaves differently from other platforms. On Emscripten, sockets are always non-blocking and require additional JavaScript code and helpers on the server to proxy TCP through WebSockets; see
  * Some functions are stubs that either don’t do anything and always return hardcoded values.
  * Functions related to file descriptors, file permissions, file ownership, and links are limited and don’t support some operations. For example, WASI does not permit symlinks with absolute file names.


### Mobile platforms[¶](https://docs.python.org/3/library/intro.html#mobile-platforms "Link to this heading")
Android and iOS are, in most respects, POSIX operating systems. File I/O, socket handling, and threading all behave as they would on any POSIX operating system. However, there are several major differences:
  * Mobile platforms can only use Python in “embedded” mode. There is no Python REPL, and no ability to use separate executables such as **python** or **pip**. To add Python code to your mobile app, you must use the [Python embedding API](https://docs.python.org/3/extending/embedding.html#embedding). For more details, see [Using Python on Android](https://docs.python.org/3/using/android.html#using-android) and [Using Python on iOS](https://docs.python.org/3/using/ios.html#using-ios).
  * Subprocesses:
    * On Android, creating subprocesses is possible but [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") is not available.
    * An iOS app cannot use any form of subprocessing, multiprocessing, or inter-process communication. If an iOS app attempts to create a subprocess, the process creating the subprocess will either lock up, or crash. An iOS app has no visibility of other applications that are running, nor any ability to communicate with other running applications, outside of the iOS-specific APIs that exist for this purpose.
  * Mobile apps have limited access to modify system resources (such as the system clock). These resources will often be _readable_ , but attempts to modify those resources will usually fail.
  * Console input and output:
    * On Android, the native `stdout` and `stderr` are not connected to anything, so Python installs its own streams which redirect messages to the system log. These can be seen under the tags `python.stdout` and `python.stderr` respectively.
    * iOS apps have a limited concept of console output. `stdout` and `stderr` _exist_ , and content written to `stdout` and `stderr` will be visible in logs when running in Xcode, but this content _won’t_ be recorded in the system log. If a user who has installed your app provides their app logs as a diagnostic aid, they will not include any detail written to `stdout` or `stderr`.
    * Mobile apps have no usable `stdin` at all. While apps can display an on-screen keyboard, this is a software feature, not something that is attached to `stdin`.
As a result, Python modules that involve console manipulation (such as [`curses`](https://docs.python.org/3/library/curses.html#module-curses "curses: An interface to the curses library, providing portable terminal handling.") and [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")) are not available on mobile platforms.


### [Table of Contents](https://docs.python.org/3/contents.html)
  * [Introduction](https://docs.python.org/3/library/intro.html)
    * [Notes on availability](https://docs.python.org/3/library/intro.html#notes-on-availability)
      * [WebAssembly platforms](https://docs.python.org/3/library/intro.html#webassembly-platforms)
      * [Mobile platforms](https://docs.python.org/3/library/intro.html#mobile-platforms)


#### Previous topic
[The Python Standard Library](https://docs.python.org/3/library/index.html "previous chapter")
#### Next topic
[Built-in Functions](https://docs.python.org/3/library/functions.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Introduction&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fintro.html&pagesource=library%2Fintro.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/functions.html "Built-in Functions") |
  * [previous](https://docs.python.org/3/library/index.html "The Python Standard Library") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Introduction](https://docs.python.org/3/library/intro.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
