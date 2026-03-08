[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`contextvars` — Context Variables](https://docs.python.org/3/library/contextvars.html "previous chapter")
#### Next topic
[Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=_thread+%E2%80%94+Low-level+threading+API&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2F_thread.html&pagesource=library%2F_thread.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ipc.html "Networking and Interprocess Communication") |
  * [previous](https://docs.python.org/3/library/contextvars.html "contextvars — Context Variables") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`_thread` — Low-level threading API](https://docs.python.org/3/library/_thread.html)
  * |
  * Theme  Auto Light Dark |


#  `_thread` — Low-level threading API[¶](https://docs.python.org/3/library/_thread.html#module-_thread "Link to this heading")
* * *
This module provides low-level primitives for working with multiple threads (also called _light-weight processes_ or _tasks_) — multiple threads of control sharing their global data space. For synchronization, simple locks (also called _mutexes_ or _binary semaphores_) are provided. The [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.") module provides an easier to use and higher-level threading API built on top of this module.
Changed in version 3.7: This module used to be optional, it is now always available.
This module defines the following constants and functions:

_exception_ _thread.error[¶](https://docs.python.org/3/library/_thread.html#thread.error "Link to this definition")

Raised on thread-specific errors.
Changed in version 3.3: This is now a synonym of the built-in [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError").

_thread.LockType[¶](https://docs.python.org/3/library/_thread.html#thread.LockType "Link to this definition")

This is the type of lock objects.

_thread.start_new_thread(_function_ , _args_[, _kwargs_])[¶](https://docs.python.org/3/library/_thread.html#thread.start_new_thread "Link to this definition")

Start a new thread and return its identifier. The thread executes the function _function_ with the argument list _args_ (which must be a tuple). The optional _kwargs_ argument specifies a dictionary of keyword arguments.
When the function returns, the thread silently exits.
When the function terminates with an unhandled exception, [`sys.unraisablehook()`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook") is called to handle the exception. The _object_ attribute of the hook argument is _function_. By default, a stack trace is printed and then the thread exits (but other threads continue to run).
When the function raises a [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "SystemExit") exception, it is silently ignored.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `_thread.start_new_thread` with arguments `function`, `args`, `kwargs`.
Changed in version 3.8: [`sys.unraisablehook()`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook") is now used to handle unhandled exceptions.

_thread.interrupt_main(_signum =signal.SIGINT_, _/_)[¶](https://docs.python.org/3/library/_thread.html#thread.interrupt_main "Link to this definition")

Simulate the effect of a signal arriving in the main thread. A thread can use this function to interrupt the main thread, though there is no guarantee that the interruption will happen immediately.
If given, _signum_ is the number of the signal to simulate. If _signum_ is not given, [`signal.SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT") is simulated.
If the given signal isn’t handled by Python (it was set to [`signal.SIG_DFL`](https://docs.python.org/3/library/signal.html#signal.SIG_DFL "signal.SIG_DFL") or [`signal.SIG_IGN`](https://docs.python.org/3/library/signal.html#signal.SIG_IGN "signal.SIG_IGN")), this function does nothing.
Changed in version 3.10: The _signum_ argument is added to customize the signal number.
Note
This does not emit the corresponding signal but schedules a call to the associated handler (if it exists). If you want to truly emit the signal, use [`signal.raise_signal()`](https://docs.python.org/3/library/signal.html#signal.raise_signal "signal.raise_signal").

_thread.exit()[¶](https://docs.python.org/3/library/_thread.html#thread.exit "Link to this definition")

Raise the [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "SystemExit") exception. When not caught, this will cause the thread to exit silently.

_thread.allocate_lock()[¶](https://docs.python.org/3/library/_thread.html#thread.allocate_lock "Link to this definition")

Return a new lock object. Methods of locks are described below. The lock is initially unlocked.

_thread.get_ident()[¶](https://docs.python.org/3/library/_thread.html#thread.get_ident "Link to this definition")

Return the ‘thread identifier’ of the current thread. This is a nonzero integer. Its value has no direct meaning; it is intended as a magic cookie to be used e.g. to index a dictionary of thread-specific data. Thread identifiers may be recycled when a thread exits and another thread is created.

_thread.get_native_id()[¶](https://docs.python.org/3/library/_thread.html#thread.get_native_id "Link to this definition")

Return the native integral Thread ID of the current thread assigned by the kernel. This is a non-negative integer. Its value may be used to uniquely identify this particular thread system-wide (until the thread terminates, after which the value may be recycled by the OS).
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX, DragonFlyBSD, GNU/kFreeBSD.
Added in version 3.8.
Changed in version 3.13: Added support for GNU/kFreeBSD.

_thread.stack_size([_size_])[¶](https://docs.python.org/3/library/_thread.html#thread.stack_size "Link to this definition")

Return the thread stack size used when creating new threads. The optional _size_ argument specifies the stack size to be used for subsequently created threads, and must be 0 (use platform or configured default) or a positive integer value of at least 32,768 (32 KiB). If _size_ is not specified, 0 is used. If changing the thread stack size is unsupported, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised. If the specified stack size is invalid, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised and the stack size is unmodified. 32 KiB is currently the minimum supported stack size value to guarantee sufficient stack space for the interpreter itself. Note that some platforms may have particular restrictions on values for the stack size, such as requiring a minimum stack size > 32 KiB or requiring allocation in multiples of the system memory page size - platform documentation should be referred to for more information (4 KiB pages are common; using multiples of 4096 for the stack size is the suggested approach in the absence of more specific information).
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows, pthreads.
Unix platforms with POSIX threads support.

_thread.TIMEOUT_MAX[¶](https://docs.python.org/3/library/_thread.html#thread.TIMEOUT_MAX "Link to this definition")

The maximum value allowed for the _timeout_ parameter of [`Lock.acquire`](https://docs.python.org/3/library/threading.html#threading.Lock.acquire "threading.Lock.acquire"). Specifying a timeout greater than this value will raise an [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError").
Added in version 3.2.
Lock objects have the following methods:

lock.acquire(_blocking =True_, _timeout =-1_)[¶](https://docs.python.org/3/library/_thread.html#thread.lock.acquire "Link to this definition")

Without any optional argument, this method acquires the lock unconditionally, if necessary waiting until it is released by another thread (only one thread at a time can acquire a lock — that’s their reason for existence).
If the _blocking_ argument is present, the action depends on its value: if it is false, the lock is only acquired if it can be acquired immediately without waiting, while if it is true, the lock is acquired unconditionally as above.
If the floating-point _timeout_ argument is present and positive, it specifies the maximum wait time in seconds before returning. A negative _timeout_ argument specifies an unbounded wait. You cannot specify a _timeout_ if _blocking_ is false.
The return value is `True` if the lock is acquired successfully, `False` if not.
Changed in version 3.2: The _timeout_ parameter is new.
Changed in version 3.2: Lock acquires can now be interrupted by signals on POSIX.
Changed in version 3.14: Lock acquires can now be interrupted by signals on Windows.

lock.release()[¶](https://docs.python.org/3/library/_thread.html#thread.lock.release "Link to this definition")

Releases the lock. The lock must have been acquired earlier, but not necessarily by the same thread.

lock.locked()[¶](https://docs.python.org/3/library/_thread.html#thread.lock.locked "Link to this definition")

Return the status of the lock: `True` if it has been acquired by some thread, `False` if not.
In addition to these methods, lock objects can also be used via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement, e.g.:
Copy```
import _thread

a_lock = _thread.allocate_lock()

with a_lock:
    print("a_lock is locked while this executes")

```

**Caveats:**
  * Interrupts always go to the main thread (the [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt") exception will be received by that thread.)
  * Calling [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit") or raising the [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "SystemExit") exception is equivalent to calling [`_thread.exit()`](https://docs.python.org/3/library/_thread.html#thread.exit "_thread.exit").
  * When the main thread exits, it is system defined whether the other threads survive. On most systems, they are killed without executing [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) … [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) clauses or executing object destructors.


#### Previous topic
[`contextvars` — Context Variables](https://docs.python.org/3/library/contextvars.html "previous chapter")
#### Next topic
[Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=_thread+%E2%80%94+Low-level+threading+API&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2F_thread.html&pagesource=library%2F_thread.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ipc.html "Networking and Interprocess Communication") |
  * [previous](https://docs.python.org/3/library/contextvars.html "contextvars — Context Variables") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`_thread` — Low-level threading API](https://docs.python.org/3/library/_thread.html)
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
