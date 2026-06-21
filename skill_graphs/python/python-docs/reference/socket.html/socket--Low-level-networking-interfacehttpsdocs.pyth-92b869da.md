#  `socket` — Low-level networking interface[¶](https://docs.python.org/3/library/socket.html#module-socket "Link to this heading")
**Source code:**
* * *
This module provides access to the BSD _socket_ interface. It is available on all modern Unix systems, Windows, MacOS, and probably additional platforms.
Note
Some behavior may be platform dependent, since calls are made to the operating system socket APIs.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
The Python interface is a straightforward transliteration of the Unix system call and library interface for sockets to Python’s object-oriented style: the [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket") function returns a _socket object_ whose methods implement the various socket system calls. Parameter types are somewhat higher-level than in the C interface: as with `read()` and `write()` operations on Python files, buffer allocation on receive operations is automatic, and buffer length is implicit on send operations.
See also

Module [`socketserver`](https://docs.python.org/3/library/socketserver.html#module-socketserver "socketserver: A framework for network servers.")

Classes that simplify writing network servers.

Module [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")

A TLS/SSL wrapper for socket objects.
