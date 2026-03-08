[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html)
    * [`/dev/poll` Polling Objects](https://docs.python.org/3/library/select.html#dev-poll-polling-objects)
    * [Edge and Level Trigger Polling (epoll) Objects](https://docs.python.org/3/library/select.html#edge-and-level-trigger-polling-epoll-objects)
    * [Polling Objects](https://docs.python.org/3/library/select.html#polling-objects)
    * [Kqueue Objects](https://docs.python.org/3/library/select.html#kqueue-objects)
    * [Kevent Objects](https://docs.python.org/3/library/select.html#kevent-objects)


#### Previous topic
[`ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html "previous chapter")
#### Next topic
[`selectors` — High-level I/O multiplexing](https://docs.python.org/3/library/selectors.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=select+%E2%80%94+Waiting+for+I%2FO+completion&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fselect.html&pagesource=library%2Fselect.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/selectors.html "selectors — High-level I/O multiplexing") |
  * [previous](https://docs.python.org/3/library/ssl.html "ssl — TLS/SSL wrapper for socket objects") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
  * [`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html)
  * |
  * Theme  Auto Light Dark |


#  `select` — Waiting for I/O completion[¶](https://docs.python.org/3/library/select.html#module-select "Link to this heading")
* * *
This module provides access to the `select()` and `poll()` functions available in most operating systems, `devpoll()` available on Solaris and derivatives, `epoll()` available on Linux 2.5+ and `kqueue()` available on most BSD. Note that on Windows, it only works for sockets; on other operating systems, it also works for other file types (in particular, on Unix, it works on pipes). It cannot be used on regular files to determine whether a file has grown since it was last read.
Note
The [`selectors`](https://docs.python.org/3/library/selectors.html#module-selectors "selectors: High-level I/O multiplexing.") module allows high-level and efficient I/O multiplexing, built upon the `select` module primitives. Users are encouraged to use the `selectors` module instead, unless they want precise control over the OS-level primitives used.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
The module defines the following:

_exception_ select.error[¶](https://docs.python.org/3/library/select.html#select.error "Link to this definition")

A deprecated alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
Changed in version 3.3: Following [**PEP 3151**](https://peps.python.org/pep-3151/), this class was made an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

select.devpoll()[¶](https://docs.python.org/3/library/select.html#select.devpoll "Link to this definition")

(Only supported on Solaris and derivatives.) Returns a `/dev/poll` polling object; see section [/dev/poll Polling Objects](https://docs.python.org/3/library/select.html#devpoll-objects) below for the methods supported by devpoll objects.
`devpoll()` objects are linked to the number of file descriptors allowed at the time of instantiation. If your program reduces this value, `devpoll()` will fail. If your program increases this value, `devpoll()` may return an incomplete list of active file descriptors.
The new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
Added in version 3.3.
Changed in version 3.4: The new file descriptor is now non-inheritable.

select.epoll(_sizehint =-1_, _flags =0_)[¶](https://docs.python.org/3/library/select.html#select.epoll "Link to this definition")

(Only supported on Linux 2.5.44 and newer.) Return an edge polling object, which can be used as Edge or Level Triggered interface for I/O events.
_sizehint_ informs epoll about the expected number of events to be registered. It must be positive, or `-1` to use the default. It is only used on older systems where `epoll_create1()` is not available; otherwise it has no effect (though its value is still checked).
_flags_ is deprecated and completely ignored. However, when supplied, its value must be `0` or `select.EPOLL_CLOEXEC`, otherwise `OSError` is raised.
See the [Edge and Level Trigger Polling (epoll) Objects](https://docs.python.org/3/library/select.html#epoll-objects) section below for the methods supported by epolling objects.
`epoll` objects support the context management protocol: when used in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement, the new file descriptor is automatically closed at the end of the block.
The new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
Changed in version 3.3: Added the _flags_ parameter.
Changed in version 3.4: Support for the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement was added. The new file descriptor is now non-inheritable.
Deprecated since version 3.4: The _flags_ parameter. `select.EPOLL_CLOEXEC` is used by default now. Use [`os.set_inheritable()`](https://docs.python.org/3/library/os.html#os.set_inheritable "os.set_inheritable") to make the file descriptor inheritable.

select.poll()[¶](https://docs.python.org/3/library/select.html#select.poll "Link to this definition")

(Not supported by all operating systems.) Returns a polling object, which supports registering and unregistering file descriptors, and then polling them for I/O events; see section [Polling Objects](https://docs.python.org/3/library/select.html#poll-objects) below for the methods supported by polling objects.

select.kqueue()[¶](https://docs.python.org/3/library/select.html#select.kqueue "Link to this definition")

(Only supported on BSD.) Returns a kernel queue object; see section [Kqueue Objects](https://docs.python.org/3/library/select.html#kqueue-objects) below for the methods supported by kqueue objects.
The new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
Changed in version 3.4: The new file descriptor is now non-inheritable.

select.kevent(_ident_ , _filter =KQ_FILTER_READ_, _flags =KQ_EV_ADD_, _fflags =0_, _data =0_, _udata =0_)[¶](https://docs.python.org/3/library/select.html#select.kevent "Link to this definition")

(Only supported on BSD.) Returns a kernel event object; see section [Kevent Objects](https://docs.python.org/3/library/select.html#kevent-objects) below for the methods supported by kevent objects.

select.select(_rlist_ , _wlist_ , _xlist_ , _timeout =None_)[¶](https://docs.python.org/3/library/select.html#select.select "Link to this definition")

This is a straightforward interface to the Unix `select()` system call. The first three arguments are iterables of ‘waitable objects’: either integers representing file descriptors or objects with a parameterless method named [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") returning such an integer:
  * _rlist_ : wait until ready for reading
  * _wlist_ : wait until ready for writing
  * _xlist_ : wait for an “exceptional condition” (see the manual page for what your system considers such a condition)


Empty iterables are allowed, but acceptance of three empty iterables is platform-dependent. (It is known to work on Unix but not on Windows.) The optional _timeout_ argument specifies a time-out as a floating-point number in seconds. When the _timeout_ argument is omitted or `None`, the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and never blocks.
The return value is a triple of lists of objects that are ready: subsets of the first three arguments. When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.
Among the acceptable object types in the iterables are Python [file objects](https://docs.python.org/3/glossary.html#term-file-object) (e.g. `sys.stdin`, or objects returned by [`open()`](https://docs.python.org/3/library/functions.html#open "open") or [`os.popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen")), socket objects returned by [`socket.socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket"). You may also define a _wrapper_ class yourself, as long as it has an appropriate [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method (that really returns a file descriptor, not just a random integer).
Note
File objects on Windows are not acceptable, but sockets are. On Windows, the underlying `select()` function is provided by the WinSock library, and does not handle file descriptors that don’t originate from WinSock.
Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale), instead of raising [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError").

select.PIPE_BUF[¶](https://docs.python.org/3/library/select.html#select.PIPE_BUF "Link to this definition")

The minimum number of bytes which can be written without blocking to a pipe when the pipe has been reported as ready for writing by [`select()`](https://docs.python.org/3/library/select.html#select.select "select.select"), `poll()` or another interface in this module. This doesn’t apply to other kinds of file-like objects such as sockets.
This value is guaranteed by POSIX to be at least 512.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix
Added in version 3.2.
##  `/dev/poll` Polling Objects[¶](https://docs.python.org/3/library/select.html#dev-poll-polling-objects "Link to this heading")
Solaris and derivatives have `/dev/poll`. While `select()` is _O_(_highest file descriptor_) and `poll()` is _O_(_number of file descriptors_), `/dev/poll` is _O_(_active file descriptors_).
`/dev/poll` behaviour is very close to the standard `poll()` object.

devpoll.close()[¶](https://docs.python.org/3/library/select.html#select.devpoll.close "Link to this definition")

Close the file descriptor of the polling object.
Added in version 3.4.

devpoll.closed[¶](https://docs.python.org/3/library/select.html#select.devpoll.closed "Link to this definition")

`True` if the polling object is closed.
Added in version 3.4.

devpoll.fileno()[¶](https://docs.python.org/3/library/select.html#select.devpoll.fileno "Link to this definition")

Return the file descriptor number of the polling object.
Added in version 3.4.

devpoll.register(_fd_[, _eventmask_])[¶](https://docs.python.org/3/library/select.html#select.devpoll.register "Link to this definition")

Register a file descriptor with the polling object. Future calls to the [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll") method will then check whether the file descriptor has any pending I/O events. _fd_ can be either an integer, or an object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method that returns an integer. File objects implement `fileno()`, so they can also be used as the argument.
_eventmask_ is an optional bitmask describing the type of events you want to check for. The constants are the same as with `poll()` object. The default value is a combination of the constants `POLLIN`, `POLLPRI`, and `POLLOUT`.
Warning
Registering a file descriptor that’s already registered is not an error, but the result is undefined. The appropriate action is to unregister or modify it first. This is an important difference compared with `poll()`.

devpoll.modify(_fd_[, _eventmask_])[¶](https://docs.python.org/3/library/select.html#select.devpoll.modify "Link to this definition")

This method does an [`unregister()`](https://docs.python.org/3/library/select.html#select.devpoll.unregister "select.devpoll.unregister") followed by a [`register()`](https://docs.python.org/3/library/select.html#select.devpoll.register "select.devpoll.register"). It is (a bit) more efficient than doing the same explicitly.

devpoll.unregister(_fd_)[¶](https://docs.python.org/3/library/select.html#select.devpoll.unregister "Link to this definition")

Remove a file descriptor being tracked by a polling object. Just like the [`register()`](https://docs.python.org/3/library/select.html#select.devpoll.register "select.devpoll.register") method, _fd_ can be an integer or an object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method that returns an integer.
Attempting to remove a file descriptor that was never registered is safely ignored.

devpoll.poll([_timeout_])[¶](https://docs.python.org/3/library/select.html#select.devpoll.poll "Link to this definition")

Polls the set of registered file descriptors, and returns a possibly empty list containing `(fd, event)` 2-tuples for the descriptors that have events or errors to report. _fd_ is the file descriptor, and _event_ is a bitmask with bits set for the reported events for that descriptor — `POLLIN` for waiting input, `POLLOUT` to indicate that the descriptor can be written to, and so forth. An empty list indicates that the call timed out and no file descriptors had any events to report. If _timeout_ is given, it specifies the length of time in milliseconds which the system will wait for events before returning. If _timeout_ is omitted, -1, or [`None`](https://docs.python.org/3/library/constants.html#None "None"), the call will block until there is an event for this poll object.
Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale), instead of raising [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError").
## Edge and Level Trigger Polling (epoll) Objects[¶](https://docs.python.org/3/library/select.html#edge-and-level-trigger-polling-epoll-objects "Link to this heading")
> _eventmask_
> Constant | Meaning
> ---|---
> `EPOLLIN` | Available for read
> `EPOLLOUT` | Available for write
> `EPOLLPRI` | Urgent data for read
> `EPOLLERR` | Error condition happened on the assoc. fd
> `EPOLLHUP` | Hang up happened on the assoc. fd
> `EPOLLET` | Set Edge Trigger behavior, the default is Level Trigger behavior
> `EPOLLONESHOT` | Set one-shot behavior. After one event is pulled out, the fd is internally disabled
> `EPOLLEXCLUSIVE` | Wake only one epoll object when the associated fd has an event. The default (if this flag is not set) is to wake all epoll objects polling on a fd.
> `EPOLLRDHUP` | Stream socket peer closed connection or shut down writing half of connection.
> `EPOLLRDNORM` | Equivalent to `EPOLLIN`
> `EPOLLRDBAND` | Priority data band can be read.
> `EPOLLWRNORM` | Equivalent to `EPOLLOUT`
> `EPOLLWRBAND` | Priority data may be written.
> `EPOLLMSG` | Ignored.
> `EPOLLWAKEUP` | Prevents sleep during event waiting.
> Added in version 3.6: `EPOLLEXCLUSIVE` was added. It’s only supported by Linux Kernel 4.5 or later.
> Added in version 3.14: `EPOLLWAKEUP` was added. It’s only supported by Linux Kernel 3.5 or later.

epoll.close()[¶](https://docs.python.org/3/library/select.html#select.epoll.close "Link to this definition")

Close the control file descriptor of the epoll object.

epoll.closed[¶](https://docs.python.org/3/library/select.html#select.epoll.closed "Link to this definition")

`True` if the epoll object is closed.

epoll.fileno()[¶](https://docs.python.org/3/library/select.html#select.epoll.fileno "Link to this definition")

Return the file descriptor number of the control fd.

epoll.fromfd(_fd_)[¶](https://docs.python.org/3/library/select.html#select.epoll.fromfd "Link to this definition")

Create an epoll object from a given file descriptor.

epoll.register(_fd_[, _eventmask_])[¶](https://docs.python.org/3/library/select.html#select.epoll.register "Link to this definition")

Register a fd descriptor with the epoll object.

epoll.modify(_fd_ , _eventmask_)[¶](https://docs.python.org/3/library/select.html#select.epoll.modify "Link to this definition")

Modify a registered file descriptor.

epoll.unregister(_fd_)[¶](https://docs.python.org/3/library/select.html#select.epoll.unregister "Link to this definition")

Remove a registered file descriptor from the epoll object.
Changed in version 3.9: The method no longer ignores the [`EBADF`](https://docs.python.org/3/library/errno.html#errno.EBADF "errno.EBADF") error.

epoll.poll(_timeout =None_, _maxevents =-1_)[¶](https://docs.python.org/3/library/select.html#select.epoll.poll "Link to this definition")

Wait for events. timeout in seconds (float)
Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale), instead of raising [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError").
## Polling Objects[¶](https://docs.python.org/3/library/select.html#polling-objects "Link to this heading")
The `poll()` system call, supported on most Unix systems, provides better scalability for network servers that service many, many clients at the same time. `poll()` scales better because the system call only requires listing the file descriptors of interest, while `select()` builds a bitmap, turns on bits for the fds of interest, and then afterward the whole bitmap has to be linearly scanned again. `select()` is _O_(_highest file descriptor_), while `poll()` is _O_(_number of file descriptors_).

poll.register(_fd_[, _eventmask_])[¶](https://docs.python.org/3/library/select.html#select.poll.register "Link to this definition")

Register a file descriptor with the polling object. Future calls to the [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll") method will then check whether the file descriptor has any pending I/O events. _fd_ can be either an integer, or an object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method that returns an integer. File objects implement `fileno()`, so they can also be used as the argument.
_eventmask_ is an optional bitmask describing the type of events you want to check for, and can be a combination of the constants `POLLIN`, `POLLPRI`, and `POLLOUT`, described in the table below. If not specified, the default value used will check for all 3 types of events.
Constant | Meaning
---|---
`POLLIN` | There is data to read
`POLLPRI` | There is urgent data to read
`POLLOUT` | Ready for output: writing will not block
`POLLERR` | Error condition of some sort
`POLLHUP` | Hung up
`POLLRDHUP` | Stream socket peer closed connection, or shut down writing half of connection
`POLLNVAL` | Invalid request: descriptor not open
Registering a file descriptor that’s already registered is not an error, and has the same effect as registering the descriptor exactly once.

poll.modify(_fd_ , _eventmask_)[¶](https://docs.python.org/3/library/select.html#select.poll.modify "Link to this definition")

Modifies an already registered fd. This has the same effect as `register(fd, eventmask)`. Attempting to modify a file descriptor that was never registered causes an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception with errno `ENOENT` to be raised.

poll.unregister(_fd_)[¶](https://docs.python.org/3/library/select.html#select.poll.unregister "Link to this definition")

Remove a file descriptor being tracked by a polling object. Just like the [`register()`](https://docs.python.org/3/library/select.html#select.poll.register "select.poll.register") method, _fd_ can be an integer or an object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method that returns an integer.
Attempting to remove a file descriptor that was never registered causes a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception to be raised.

poll.poll([_timeout_])[¶](https://docs.python.org/3/library/select.html#select.poll.poll "Link to this definition")

Polls the set of registered file descriptors, and returns a possibly empty list containing `(fd, event)` 2-tuples for the descriptors that have events or errors to report. _fd_ is the file descriptor, and _event_ is a bitmask with bits set for the reported events for that descriptor — `POLLIN` for waiting input, `POLLOUT` to indicate that the descriptor can be written to, and so forth. An empty list indicates that the call timed out and no file descriptors had any events to report. If _timeout_ is given, it specifies the length of time in milliseconds which the system will wait for events before returning. If _timeout_ is omitted, negative, or [`None`](https://docs.python.org/3/library/constants.html#None "None"), the call will block until there is an event for this poll object.
Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale), instead of raising [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError").
## Kqueue Objects[¶](https://docs.python.org/3/library/select.html#kqueue-objects "Link to this heading")

kqueue.close()[¶](https://docs.python.org/3/library/select.html#select.kqueue.close "Link to this definition")

Close the control file descriptor of the kqueue object.

kqueue.closed[¶](https://docs.python.org/3/library/select.html#select.kqueue.closed "Link to this definition")

`True` if the kqueue object is closed.

kqueue.fileno()[¶](https://docs.python.org/3/library/select.html#select.kqueue.fileno "Link to this definition")

Return the file descriptor number of the control fd.

kqueue.fromfd(_fd_)[¶](https://docs.python.org/3/library/select.html#select.kqueue.fromfd "Link to this definition")

Create a kqueue object from a given file descriptor.

kqueue.control(_changelist_ , _max_events_[, _timeout_]) → eventlist[¶](https://docs.python.org/3/library/select.html#select.kqueue.control "Link to this definition")

Low level interface to kevent
  * changelist must be an iterable of kevent objects or `None`
  * max_events must be 0 or a positive integer
  * timeout in seconds (floats possible); the default is `None`, to wait forever


Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale), instead of raising [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError").
## Kevent Objects[¶](https://docs.python.org/3/library/select.html#kevent-objects "Link to this heading")

kevent.ident[¶](https://docs.python.org/3/library/select.html#select.kevent.ident "Link to this definition")

Value used to identify the event. The interpretation depends on the filter but it’s usually the file descriptor. In the constructor ident can either be an int or an object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method. kevent stores the integer internally.

kevent.filter[¶](https://docs.python.org/3/library/select.html#select.kevent.filter "Link to this definition")

Name of the kernel filter.
Constant | Meaning
---|---
`KQ_FILTER_READ` | Takes a descriptor and returns whenever there is data available to read
`KQ_FILTER_WRITE` | Takes a descriptor and returns whenever there is data available to write
`KQ_FILTER_AIO` | AIO requests
`KQ_FILTER_VNODE` | Returns when one or more of the requested events watched in _fflag_ occurs
`KQ_FILTER_PROC` | Watch for events on a process id
`KQ_FILTER_NETDEV` | Watch for events on a network device [not available on macOS]
`KQ_FILTER_SIGNAL` | Returns whenever the watched signal is delivered to the process
`KQ_FILTER_TIMER` | Establishes an arbitrary timer

kevent.flags[¶](https://docs.python.org/3/library/select.html#select.kevent.flags "Link to this definition")

Filter action.
Constant | Meaning
---|---
`KQ_EV_ADD` | Adds or modifies an event
`KQ_EV_DELETE` | Removes an event from the queue
`KQ_EV_ENABLE` | Permits control() to return the event
`KQ_EV_DISABLE` | Disables event
`KQ_EV_ONESHOT` | Removes event after first occurrence
`KQ_EV_CLEAR` | Reset the state after an event is retrieved
`KQ_EV_SYSFLAGS` | internal event
`KQ_EV_FLAG1` | internal event
`KQ_EV_EOF` | Filter specific EOF condition
`KQ_EV_ERROR` | See return values

kevent.fflags[¶](https://docs.python.org/3/library/select.html#select.kevent.fflags "Link to this definition")

Filter specific flags.
`KQ_FILTER_READ` and `KQ_FILTER_WRITE` filter flags:
Constant | Meaning
---|---
`KQ_NOTE_LOWAT` | low water mark of a socket buffer
`KQ_FILTER_VNODE` filter flags:
Constant | Meaning
---|---
`KQ_NOTE_DELETE` | _unlink()_ was called
`KQ_NOTE_WRITE` | a write occurred
`KQ_NOTE_EXTEND` | the file was extended
`KQ_NOTE_ATTRIB` | an attribute was changed
`KQ_NOTE_LINK` | the link count has changed
`KQ_NOTE_RENAME` | the file was renamed
`KQ_NOTE_REVOKE` | access to the file was revoked
`KQ_FILTER_PROC` filter flags:
Constant | Meaning
---|---
`KQ_NOTE_EXIT` | the process has exited
`KQ_NOTE_FORK` | the process has called _fork()_
`KQ_NOTE_EXEC` | the process has executed a new process
`KQ_NOTE_PCTRLMASK` | internal filter flag
`KQ_NOTE_PDATAMASK` | internal filter flag
`KQ_NOTE_TRACK` | follow a process across _fork()_
`KQ_NOTE_CHILD` | returned on the child process for _NOTE_TRACK_
`KQ_NOTE_TRACKERR` | unable to attach to a child
`KQ_FILTER_NETDEV` filter flags (not available on macOS):
Constant | Meaning
---|---
`KQ_NOTE_LINKUP` | link is up
`KQ_NOTE_LINKDOWN` | link is down
`KQ_NOTE_LINKINV` | link state is invalid

kevent.data[¶](https://docs.python.org/3/library/select.html#select.kevent.data "Link to this definition")

Filter specific data.

kevent.udata[¶](https://docs.python.org/3/library/select.html#select.kevent.udata "Link to this definition")

User defined value.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html)
    * [`/dev/poll` Polling Objects](https://docs.python.org/3/library/select.html#dev-poll-polling-objects)
    * [Edge and Level Trigger Polling (epoll) Objects](https://docs.python.org/3/library/select.html#edge-and-level-trigger-polling-epoll-objects)
    * [Polling Objects](https://docs.python.org/3/library/select.html#polling-objects)
    * [Kqueue Objects](https://docs.python.org/3/library/select.html#kqueue-objects)
    * [Kevent Objects](https://docs.python.org/3/library/select.html#kevent-objects)


#### Previous topic
[`ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html "previous chapter")
#### Next topic
[`selectors` — High-level I/O multiplexing](https://docs.python.org/3/library/selectors.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=select+%E2%80%94+Waiting+for+I%2FO+completion&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fselect.html&pagesource=library%2Fselect.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/selectors.html "selectors — High-level I/O multiplexing") |
  * [previous](https://docs.python.org/3/library/ssl.html "ssl — TLS/SSL wrapper for socket objects") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
  * [`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
