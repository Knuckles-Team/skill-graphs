[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`selectors` — High-level I/O multiplexing](https://docs.python.org/3/library/selectors.html)
    * [Introduction](https://docs.python.org/3/library/selectors.html#introduction)
    * [Classes](https://docs.python.org/3/library/selectors.html#classes)
    * [Examples](https://docs.python.org/3/library/selectors.html#examples)


#### Previous topic
[`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html "previous chapter")
#### Next topic
[`signal` — Set handlers for asynchronous events](https://docs.python.org/3/library/signal.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=selectors+%E2%80%94+High-level+I%2FO+multiplexing&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fselectors.html&pagesource=library%2Fselectors.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/signal.html "signal — Set handlers for asynchronous events") |
  * [previous](https://docs.python.org/3/library/select.html "select — Waiting for I/O completion") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
  * [`selectors` — High-level I/O multiplexing](https://docs.python.org/3/library/selectors.html)
  * |
  * Theme  Auto Light Dark |


#  `selectors` — High-level I/O multiplexing[¶](https://docs.python.org/3/library/selectors.html#module-selectors "Link to this heading")
Added in version 3.4.
**Source code:**
* * *
## Introduction[¶](https://docs.python.org/3/library/selectors.html#introduction "Link to this heading")
This module allows high-level and efficient I/O multiplexing, built upon the [`select`](https://docs.python.org/3/library/select.html#module-select "select: Wait for I/O completion on multiple streams.") module primitives. Users are encouraged to use this module instead, unless they want precise control over the OS-level primitives used.
It defines a [`BaseSelector`](https://docs.python.org/3/library/selectors.html#selectors.BaseSelector "selectors.BaseSelector") abstract base class, along with several concrete implementations ([`KqueueSelector`](https://docs.python.org/3/library/selectors.html#selectors.KqueueSelector "selectors.KqueueSelector"), [`EpollSelector`](https://docs.python.org/3/library/selectors.html#selectors.EpollSelector "selectors.EpollSelector")…), that can be used to wait for I/O readiness notification on multiple file objects. In the following, “file object” refers to any object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method, or a raw file descriptor. See [file object](https://docs.python.org/3/glossary.html#term-file-object).
[`DefaultSelector`](https://docs.python.org/3/library/selectors.html#selectors.DefaultSelector "selectors.DefaultSelector") is an alias to the most efficient implementation available on the current platform: this should be the default choice for most users.
Note
The type of file objects supported depends on the platform: on Windows, sockets are supported, but not pipes, whereas on Unix, both are supported (some other types may be supported as well, such as fifos or special file devices).
See also

[`select`](https://docs.python.org/3/library/select.html#module-select "select: Wait for I/O completion on multiple streams.")

Low-level I/O multiplexing module.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
## Classes[¶](https://docs.python.org/3/library/selectors.html#classes "Link to this heading")
Classes hierarchy:
Copy```
BaseSelector
+-- SelectSelector
+-- PollSelector
+-- EpollSelector
+-- DevpollSelector
+-- KqueueSelector

```

In the following, _events_ is a bitwise mask indicating which I/O events should be waited for on a given file object. It can be a combination of the module’s constants below:
> Constant | Meaning
> ---|---

selectors.EVENT_READ[¶](https://docs.python.org/3/library/selectors.html#selectors.EVENT_READ "Link to this definition")
| Available for read

selectors.EVENT_WRITE[¶](https://docs.python.org/3/library/selectors.html#selectors.EVENT_WRITE "Link to this definition")
| Available for write

_class_ selectors.SelectorKey[¶](https://docs.python.org/3/library/selectors.html#selectors.SelectorKey "Link to this definition")

A `SelectorKey` is a [`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") used to associate a file object to its underlying file descriptor, selected event mask and attached data. It is returned by several [`BaseSelector`](https://docs.python.org/3/library/selectors.html#selectors.BaseSelector "selectors.BaseSelector") methods.

fileobj[¶](https://docs.python.org/3/library/selectors.html#selectors.SelectorKey.fileobj "Link to this definition")

File object registered.

fd[¶](https://docs.python.org/3/library/selectors.html#selectors.SelectorKey.fd "Link to this definition")

Underlying file descriptor.

events[¶](https://docs.python.org/3/library/selectors.html#selectors.SelectorKey.events "Link to this definition")

Events that must be waited for on this file object.

data[¶](https://docs.python.org/3/library/selectors.html#selectors.SelectorKey.data "Link to this definition")

Optional opaque data associated to this file object: for example, this could be used to store a per-client session ID.

_class_ selectors.BaseSelector[¶](https://docs.python.org/3/library/selectors.html#selectors.BaseSelector "Link to this definition")

A `BaseSelector` is used to wait for I/O event readiness on multiple file objects. It supports file stream registration, unregistration, and a method to wait for I/O events on those streams, with an optional timeout. It’s an abstract base class, so cannot be instantiated. Use [`DefaultSelector`](https://docs.python.org/3/library/selectors.html#selectors.DefaultSelector "selectors.DefaultSelector") instead, or one of [`SelectSelector`](https://docs.python.org/3/library/selectors.html#selectors.SelectSelector "selectors.SelectSelector"), [`KqueueSelector`](https://docs.python.org/3/library/selectors.html#selectors.KqueueSelector "selectors.KqueueSelector") etc. if you want to specifically use an implementation, and your platform supports it. `BaseSelector` and its concrete implementations support the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) protocol.

_abstractmethod_ register(_fileobj_ , _events_ , _data =None_)[¶](https://docs.python.org/3/library/selectors.html#selectors.BaseSelector.register "Link to this definition")

Register a file object for selection, monitoring it for I/O events.
_fileobj_ is the file object to monitor. It may either be an integer file descriptor or an object with a `fileno()` method. _events_ is a bitwise mask of events to monitor. _data_ is an opaque object.
This returns a new [`SelectorKey`](https://docs.python.org/3/library/selectors.html#selectors.SelectorKey "selectors.SelectorKey") instance, or raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") in case of invalid event mask or file descriptor, or [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") if the file object is already registered.

_abstractmethod_ unregister(_fileobj_)[¶](https://docs.python.org/3/library/selectors.html#selectors.BaseSelector.unregister "Link to this definition")

Unregister a file object from selection, removing it from monitoring. A file object shall be unregistered prior to being closed.
_fileobj_ must be a file object previously registered.
This returns the associated [`SelectorKey`](https://docs.python.org/3/library/selectors.html#selectors.SelectorKey "selectors.SelectorKey") instance, or raises a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") if _fileobj_ is not registered. It will raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if _fileobj_ is invalid (e.g. it has no `fileno()` method or its `fileno()` method has an invalid return value).

modify(_fileobj_ , _events_ , _data =None_)[¶](https://docs.python.org/3/library/selectors.html#selectors.BaseSelector.modify "Link to this definition")

Change a registered file object’s monitored events or attached data.
This is equivalent to `BaseSelector.unregister(fileobj)` followed by `BaseSelector.register(fileobj, events, data)`, except that it can be implemented more efficiently.
This returns a new [`SelectorKey`](https://docs.python.org/3/library/selectors.html#selectors.SelectorKey "selectors.SelectorKey") instance, or raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") in case of invalid event mask or file descriptor, or [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") if the file object is not registered.

_abstractmethod_ select(_timeout =None_)[¶](https://docs.python.org/3/library/selectors.html#selectors.BaseSelector.select "Link to this definition")

Wait until some registered file objects become ready, or the timeout expires.
If `timeout > 0`, this specifies the maximum wait time, in seconds. If `timeout <= 0`, the call won’t block, and will report the currently ready file objects. If _timeout_ is `None`, the call will block until a monitored file object becomes ready.
This returns a list of `(key, events)` tuples, one for each ready file object.
_key_ is the [`SelectorKey`](https://docs.python.org/3/library/selectors.html#selectors.SelectorKey "selectors.SelectorKey") instance corresponding to a ready file object. _events_ is a bitmask of events ready on this file object.
Note
This method can return before any file object becomes ready or the timeout has elapsed if the current process receives a signal: in this case, an empty list will be returned.
Changed in version 3.5: The selector is now retried with a recomputed timeout when interrupted by a signal if the signal handler did not raise an exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale), instead of returning an empty list of events before the timeout.

close()[¶](https://docs.python.org/3/library/selectors.html#selectors.BaseSelector.close "Link to this definition")

Close the selector.
This must be called to make sure that any underlying resource is freed. The selector shall not be used once it has been closed.

get_key(_fileobj_)[¶](https://docs.python.org/3/library/selectors.html#selectors.BaseSelector.get_key "Link to this definition")

Return the key associated with a registered file object.
This returns the [`SelectorKey`](https://docs.python.org/3/library/selectors.html#selectors.SelectorKey "selectors.SelectorKey") instance associated to this file object, or raises [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") if the file object is not registered.

_abstractmethod_ get_map()[¶](https://docs.python.org/3/library/selectors.html#selectors.BaseSelector.get_map "Link to this definition")

Return a mapping of file objects to selector keys.
This returns a [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping") instance mapping registered file objects to their associated [`SelectorKey`](https://docs.python.org/3/library/selectors.html#selectors.SelectorKey "selectors.SelectorKey") instance.

_class_ selectors.DefaultSelector[¶](https://docs.python.org/3/library/selectors.html#selectors.DefaultSelector "Link to this definition")

The default selector class, using the most efficient implementation available on the current platform. This should be the default choice for most users.

_class_ selectors.SelectSelector[¶](https://docs.python.org/3/library/selectors.html#selectors.SelectSelector "Link to this definition")

[`select.select()`](https://docs.python.org/3/library/select.html#select.select "select.select")-based selector.

_class_ selectors.PollSelector[¶](https://docs.python.org/3/library/selectors.html#selectors.PollSelector "Link to this definition")

[`select.poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll")-based selector.

_class_ selectors.EpollSelector[¶](https://docs.python.org/3/library/selectors.html#selectors.EpollSelector "Link to this definition")

[`select.epoll()`](https://docs.python.org/3/library/select.html#select.epoll "select.epoll")-based selector.

fileno()[¶](https://docs.python.org/3/library/selectors.html#selectors.EpollSelector.fileno "Link to this definition")

This returns the file descriptor used by the underlying [`select.epoll()`](https://docs.python.org/3/library/select.html#select.epoll "select.epoll") object.

_class_ selectors.DevpollSelector[¶](https://docs.python.org/3/library/selectors.html#selectors.DevpollSelector "Link to this definition")

[`select.devpoll()`](https://docs.python.org/3/library/select.html#select.devpoll "select.devpoll")-based selector.

fileno()[¶](https://docs.python.org/3/library/selectors.html#selectors.DevpollSelector.fileno "Link to this definition")

This returns the file descriptor used by the underlying [`select.devpoll()`](https://docs.python.org/3/library/select.html#select.devpoll "select.devpoll") object.
Added in version 3.5.

_class_ selectors.KqueueSelector[¶](https://docs.python.org/3/library/selectors.html#selectors.KqueueSelector "Link to this definition")

[`select.kqueue()`](https://docs.python.org/3/library/select.html#select.kqueue "select.kqueue")-based selector.

fileno()[¶](https://docs.python.org/3/library/selectors.html#selectors.KqueueSelector.fileno "Link to this definition")

This returns the file descriptor used by the underlying [`select.kqueue()`](https://docs.python.org/3/library/select.html#select.kqueue "select.kqueue") object.
## Examples[¶](https://docs.python.org/3/library/selectors.html#examples "Link to this heading")
Here is a simple echo server implementation:
Copy```
import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 1234))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`selectors` — High-level I/O multiplexing](https://docs.python.org/3/library/selectors.html)
    * [Introduction](https://docs.python.org/3/library/selectors.html#introduction)
    * [Classes](https://docs.python.org/3/library/selectors.html#classes)
    * [Examples](https://docs.python.org/3/library/selectors.html#examples)


#### Previous topic
[`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html "previous chapter")
#### Next topic
[`signal` — Set handlers for asynchronous events](https://docs.python.org/3/library/signal.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=selectors+%E2%80%94+High-level+I%2FO+multiplexing&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fselectors.html&pagesource=library%2Fselectors.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/signal.html "signal — Set handlers for asynchronous events") |
  * [previous](https://docs.python.org/3/library/select.html "select — Waiting for I/O completion") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
  * [`selectors` — High-level I/O multiplexing](https://docs.python.org/3/library/selectors.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
