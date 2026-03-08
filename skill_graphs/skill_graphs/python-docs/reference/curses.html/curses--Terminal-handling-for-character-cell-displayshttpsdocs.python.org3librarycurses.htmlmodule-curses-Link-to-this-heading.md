#  `curses` — Terminal handling for character-cell displays[¶](https://docs.python.org/3/library/curses.html#module-curses "Link to this heading")
**Source code:**
* * *
The `curses` module provides an interface to the curses library, the de-facto standard for portable advanced terminal handling.
While curses is most widely used in the Unix environment, versions are available for Windows, DOS, and possibly other systems as well. This extension module is designed to match the API of ncurses, an open-source curses library hosted on Linux and the BSD variants of Unix.
[Availability](https://docs.python.org/3/library/intro.html#availability): not Android, not iOS, not WASI.
This module is not supported on [mobile platforms](https://docs.python.org/3/library/intro.html#mobile-availability) or [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability).
This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module). If it is missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Note
Whenever the documentation mentions a _character_ it can be specified as an integer, a one-character Unicode string or a one-byte byte string.
Whenever the documentation mentions a _character string_ it can be specified as a Unicode string or a byte string.
See also

Module [`curses.ascii`](https://docs.python.org/3/library/curses.ascii.html#module-curses.ascii "curses.ascii: Constants and set-membership functions for ASCII characters.")

Utilities for working with ASCII characters, regardless of your locale settings.

Module [`curses.panel`](https://docs.python.org/3/library/curses.panel.html#module-curses.panel "curses.panel: A panel stack extension that adds depth to  curses windows.")

A panel stack extension that adds depth to curses windows.

Module [`curses.textpad`](https://docs.python.org/3/library/curses.html#module-curses.textpad "curses.textpad: Emacs-like input editing in a curses window.")

Editable text widget for curses supporting **Emacs** -like bindings.

[Curses Programming with Python](https://docs.python.org/3/howto/curses.html#curses-howto)

Tutorial material on using curses with Python, by Andrew Kuchling and Eric Raymond.
