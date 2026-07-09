# Wait for all threads to finish
for t in threads:
    t.join()

```

Changed in version 3.7: This module used to be optional, it is now always available.
See also
[`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor") offers a higher level interface to push tasks to a background thread without blocking execution of the calling thread, while still being able to retrieve their results when needed.
[`queue`](https://docs.python.org/3/library/queue.html#module-queue "queue: A synchronized queue class.") provides a thread-safe interface for exchanging data between running threads.
[`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") offers an alternative approach to achieving task level concurrency without requiring the use of multiple operating system threads.
Note
In the Python 2.x series, this module contained `camelCase` names for some methods and functions. These are deprecated as of Python 3.10, but they are still supported for compatibility with Python 2.5 and lower.
**CPython implementation detail:** In CPython, due to the [Global Interpreter Lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock), only one thread can execute Python code at once (even though certain performance-oriented libraries might overcome this limitation). If you want your application to make better use of the computational resources of multi-core machines, you are advised to use [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") or [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor"). However, threading is still an appropriate model if you want to run multiple I/O-bound tasks simultaneously.
## GIL and performance considerations[¶](https://docs.python.org/3/library/threading.html#gil-and-performance-considerations "Link to this heading")
Unlike the [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") module, which uses separate processes to bypass the [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock) (GIL), the threading module operates within a single process, meaning that all threads share the same memory space. However, the GIL limits the performance gains of threading when it comes to CPU-bound tasks, as only one thread can execute Python bytecode at a time. Despite this, threads remain a useful tool for achieving concurrency in many scenarios.
As of Python 3.13, [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading) builds can disable the GIL, enabling true parallel execution of threads, but this feature is not available by default (see [**PEP 703**](https://peps.python.org/pep-0703/)).
## Reference[¶](https://docs.python.org/3/library/threading.html#reference "Link to this heading")
This module defines the following functions:

threading.active_count()[¶](https://docs.python.org/3/library/threading.html#threading.active_count "Link to this definition")

Return the number of [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") objects currently alive. The returned count is equal to the length of the list returned by [`enumerate()`](https://docs.python.org/3/library/threading.html#threading.enumerate "threading.enumerate").
The function `activeCount` is a deprecated alias for this function.

threading.current_thread()[¶](https://docs.python.org/3/library/threading.html#threading.current_thread "Link to this definition")

Return the current [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") object, corresponding to the caller’s thread of control. If the caller’s thread of control was not created through the `threading` module, a dummy thread object with limited functionality is returned.
The function `currentThread` is a deprecated alias for this function.

threading.excepthook(_args_ , _/_)[¶](https://docs.python.org/3/library/threading.html#threading.excepthook "Link to this definition")

Handle uncaught exception raised by [`Thread.run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run").
The _args_ argument has the following attributes:
  * _exc_type_ : Exception type.
  * _exc_value_ : Exception value, can be `None`.
  * _exc_traceback_ : Exception traceback, can be `None`.
  * _thread_ : Thread which raised the exception, can be `None`.


If _exc_type_ is [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "SystemExit"), the exception is silently ignored. Otherwise, the exception is printed out on [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr").
If this function raises an exception, [`sys.excepthook()`](https://docs.python.org/3/library/sys.html#sys.excepthook "sys.excepthook") is called to handle it.
[`threading.excepthook()`](https://docs.python.org/3/library/threading.html#threading.excepthook "threading.excepthook") can be overridden to control how uncaught exceptions raised by [`Thread.run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run") are handled.
Storing _exc_value_ using a custom hook can create a reference cycle. It should be cleared explicitly to break the reference cycle when the exception is no longer needed.
Storing _thread_ using a custom hook can resurrect it if it is set to an object which is being finalized. Avoid storing _thread_ after the custom hook completes to avoid resurrecting objects.
See also
[`sys.excepthook()`](https://docs.python.org/3/library/sys.html#sys.excepthook "sys.excepthook") handles uncaught exceptions.
Added in version 3.8.

threading.__excepthook__[¶](https://docs.python.org/3/library/threading.html#threading.__excepthook__ "Link to this definition")

Holds the original value of [`threading.excepthook()`](https://docs.python.org/3/library/threading.html#threading.excepthook "threading.excepthook"). It is saved so that the original value can be restored in case they happen to get replaced with broken or alternative objects.
Added in version 3.10.

threading.get_ident()[¶](https://docs.python.org/3/library/threading.html#threading.get_ident "Link to this definition")

Return the ‘thread identifier’ of the current thread. This is a nonzero integer. Its value has no direct meaning; it is intended as a magic cookie to be used e.g. to index a dictionary of thread-specific data. Thread identifiers may be recycled when a thread exits and another thread is created.
Added in version 3.3.

threading.get_native_id()[¶](https://docs.python.org/3/library/threading.html#threading.get_native_id "Link to this definition")

Return the native integral Thread ID of the current thread assigned by the kernel. This is a non-negative integer. Its value may be used to uniquely identify this particular thread system-wide (until the thread terminates, after which the value may be recycled by the OS).
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX, DragonFlyBSD, GNU/kFreeBSD.
Added in version 3.8.
Changed in version 3.13: Added support for GNU/kFreeBSD.

threading.enumerate()[¶](https://docs.python.org/3/library/threading.html#threading.enumerate "Link to this definition")

Return a list of all [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") objects currently active. The list includes daemonic threads and dummy thread objects created by [`current_thread()`](https://docs.python.org/3/library/threading.html#threading.current_thread "threading.current_thread"). It excludes terminated threads and threads that have not yet been started. However, the main thread is always part of the result, even when terminated.

threading.main_thread()[¶](https://docs.python.org/3/library/threading.html#threading.main_thread "Link to this definition")

Return the main [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") object. In normal conditions, the main thread is the thread from which the Python interpreter was started.
Added in version 3.4.

threading.settrace(_func_)[¶](https://docs.python.org/3/library/threading.html#threading.settrace "Link to this definition")

Set a trace function for all threads started from the `threading` module. The _func_ will be passed to [`sys.settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace") for each thread, before its [`run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run") method is called.

threading.settrace_all_threads(_func_)[¶](https://docs.python.org/3/library/threading.html#threading.settrace_all_threads "Link to this definition")

Set a trace function for all threads started from the `threading` module and all Python threads that are currently executing.
The _func_ will be passed to [`sys.settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace") for each thread, before its [`run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run") method is called.
Added in version 3.12.

threading.gettrace()[¶](https://docs.python.org/3/library/threading.html#threading.gettrace "Link to this definition")

Get the trace function as set by [`settrace()`](https://docs.python.org/3/library/threading.html#threading.settrace "threading.settrace").
Added in version 3.10.

threading.setprofile(_func_)[¶](https://docs.python.org/3/library/threading.html#threading.setprofile "Link to this definition")

Set a profile function for all threads started from the `threading` module. The _func_ will be passed to [`sys.setprofile()`](https://docs.python.org/3/library/sys.html#sys.setprofile "sys.setprofile") for each thread, before its [`run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run") method is called.

threading.setprofile_all_threads(_func_)[¶](https://docs.python.org/3/library/threading.html#threading.setprofile_all_threads "Link to this definition")

Set a profile function for all threads started from the `threading` module and all Python threads that are currently executing.
The _func_ will be passed to [`sys.setprofile()`](https://docs.python.org/3/library/sys.html#sys.setprofile "sys.setprofile") for each thread, before its [`run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run") method is called.
Added in version 3.12.

threading.getprofile()[¶](https://docs.python.org/3/library/threading.html#threading.getprofile "Link to this definition")

Get the profiler function as set by [`setprofile()`](https://docs.python.org/3/library/threading.html#threading.setprofile "threading.setprofile").
Added in version 3.10.

threading.stack_size([_size_])[¶](https://docs.python.org/3/library/threading.html#threading.stack_size "Link to this definition")

Return the thread stack size used when creating new threads. The optional _size_ argument specifies the stack size to be used for subsequently created threads, and must be 0 (use platform or configured default) or a positive integer value of at least 32,768 (32 KiB). If _size_ is not specified, 0 is used. If changing the thread stack size is unsupported, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised. If the specified stack size is invalid, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised and the stack size is unmodified. 32 KiB is currently the minimum supported stack size value to guarantee sufficient stack space for the interpreter itself. Note that some platforms may have particular restrictions on values for the stack size, such as requiring a minimum stack size > 32 KiB or requiring allocation in multiples of the system memory page size - platform documentation should be referred to for more information (4 KiB pages are common; using multiples of 4096 for the stack size is the suggested approach in the absence of more specific information).
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows, pthreads.
Unix platforms with POSIX threads support.
This module also defines the following constant:

threading.TIMEOUT_MAX[¶](https://docs.python.org/3/library/threading.html#threading.TIMEOUT_MAX "Link to this definition")

The maximum value allowed for the _timeout_ parameter of blocking functions ([`Lock.acquire()`](https://docs.python.org/3/library/threading.html#threading.Lock.acquire "threading.Lock.acquire"), [`RLock.acquire()`](https://docs.python.org/3/library/threading.html#threading.RLock.acquire "threading.RLock.acquire"), [`Condition.wait()`](https://docs.python.org/3/library/threading.html#threading.Condition.wait "threading.Condition.wait"), etc.). Specifying a timeout greater than this value will raise an [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError").
Added in version 3.2.
This module defines a number of classes, which are detailed in the sections below.
The design of this module is loosely based on Java’s threading model. However, where Java makes locks and condition variables basic behavior of every object, they are separate objects in Python. Python’s [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") class supports a subset of the behavior of Java’s Thread class; currently, there are no priorities, no thread groups, and threads cannot be destroyed, stopped, suspended, resumed, or interrupted. The static methods of Java’s Thread class, when implemented, are mapped to module-level functions.
All of the methods described below are executed atomically.
### Thread-local data[¶](https://docs.python.org/3/library/threading.html#thread-local-data "Link to this heading")
Thread-local data is data whose values are thread specific. If you have data that you want to be local to a thread, create a [`local`](https://docs.python.org/3/library/threading.html#threading.local "threading.local") object and use its attributes:
Copy```
>>> mydata = local()
>>> mydata.number = 42
>>> mydata.number
42

```

You can also access the [`local`](https://docs.python.org/3/library/threading.html#threading.local "threading.local")-object’s dictionary:
Copy```
>>> mydata.__dict__
{'number': 42}
>>> mydata.__dict__.setdefault('widgets', [])
[]
>>> mydata.widgets
[]

```

If we access the data in a different thread:
Copy```
>>> log = []
>>> def f():
...     items = sorted(mydata.__dict__.items())
...     log.append(items)
...     mydata.number = 11
...     log.append(mydata.number)

>>> import threading
>>> thread = threading.Thread(target=f)
>>> thread.start()
>>> thread.join()
>>> log
[[], 11]

```

we get different data. Furthermore, changes made in the other thread don’t affect data seen in this thread:
Copy```
>>> mydata.number
42

```

Of course, values you get from a [`local`](https://docs.python.org/3/library/threading.html#threading.local "threading.local") object, including their [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") attribute, are for whatever thread was current at the time the attribute was read. For that reason, you generally don’t want to save these values across threads, as they apply only to the thread they came from.
You can create custom [`local`](https://docs.python.org/3/library/threading.html#threading.local "threading.local") objects by subclassing the `local` class:
Copy```
>>> class MyLocal(local):
...     number = 2
...     def __init__(self, /, **kw):
...         self.__dict__.update(kw)
...     def squared(self):
...         return self.number ** 2

```

This can be useful to support default values, methods and initialization. Note that if you define an [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__") method, it will be called each time the [`local`](https://docs.python.org/3/library/threading.html#threading.local "threading.local") object is used in a separate thread. This is necessary to initialize each thread’s dictionary.
Now if we create a [`local`](https://docs.python.org/3/library/threading.html#threading.local "threading.local") object:
Copy```
>>> mydata = MyLocal(color='red')

```

we have a default number:
Copy```
>>> mydata.number
2

```

an initial color:
Copy```
>>> mydata.color
'red'
>>> del mydata.color

```

And a method that operates on the data:
Copy```
>>> mydata.squared()
4

```

As before, we can access the data in a separate thread:
Copy```
>>> log = []
>>> thread = threading.Thread(target=f)
>>> thread.start()
>>> thread.join()
>>> log
[[('color', 'red')], 11]

```

without affecting this thread’s data:
Copy```
>>> mydata.number
2
>>> mydata.color
Traceback (most recent call last):
...
AttributeError: 'MyLocal' object has no attribute 'color'

```

Note that subclasses can define [__slots__](https://docs.python.org/3/glossary.html#term-__slots__), but they are not thread local. They are shared across threads:
Copy```
>>> class MyLocal(local):
...     __slots__ = 'number'

>>> mydata = MyLocal()
>>> mydata.number = 42
>>> mydata.color = 'red'

```

So, the separate thread:
Copy```
>>> thread = threading.Thread(target=f)
>>> thread.start()
>>> thread.join()

```

affects what we see:
Copy```
>>> mydata.number
11

```


_class_ threading.local[¶](https://docs.python.org/3/library/threading.html#threading.local "Link to this definition")

A class that represents thread-local data.
### Thread objects[¶](https://docs.python.org/3/library/threading.html#thread-objects "Link to this heading")
The [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") class represents an activity that is run in a separate thread of control. There are two ways to specify the activity: by passing a callable object to the constructor, or by overriding the [`run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run") method in a subclass. No other methods (except for the constructor) should be overridden in a subclass. In other words, _only_ override the `__init__()` and `run()` methods of this class.
Once a thread object is created, its activity must be started by calling the thread’s [`start()`](https://docs.python.org/3/library/threading.html#threading.Thread.start "threading.Thread.start") method. This invokes the [`run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run") method in a separate thread of control.
Once the thread’s activity is started, the thread is considered ‘alive’. It stops being alive when its [`run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run") method terminates – either normally, or by raising an unhandled exception. The [`is_alive()`](https://docs.python.org/3/library/threading.html#threading.Thread.is_alive "threading.Thread.is_alive") method tests whether the thread is alive.
Other threads can call a thread’s [`join()`](https://docs.python.org/3/library/threading.html#threading.Thread.join "threading.Thread.join") method. This blocks the calling thread until the thread whose `join()` method is called is terminated.
A thread has a name. The name can be passed to the constructor, and read or changed through the [`name`](https://docs.python.org/3/library/threading.html#threading.Thread.name "threading.Thread.name") attribute.
If the [`run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run") method raises an exception, [`threading.excepthook()`](https://docs.python.org/3/library/threading.html#threading.excepthook "threading.excepthook") is called to handle it. By default, `threading.excepthook()` ignores silently [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "SystemExit").
A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set through the [`daemon`](https://docs.python.org/3/library/threading.html#threading.Thread.daemon "threading.Thread.daemon") property or the _daemon_ constructor argument.
Note
Daemon threads are abruptly stopped at shutdown. Their resources (such as open files, database transactions, etc.) may not be released properly. If you want your threads to stop gracefully, make them non-daemonic and use a suitable signalling mechanism such as an [`Event`](https://docs.python.org/3/library/threading.html#threading.Event "threading.Event").
There is a “main thread” object; this corresponds to the initial thread of control in the Python program. It is not a daemon thread.
There is the possibility that “dummy thread objects” are created. These are thread objects corresponding to “alien threads”, which are threads of control started outside the threading module, such as directly from C code. Dummy thread objects have limited functionality; they are always considered alive and daemonic, and cannot be [joined](https://docs.python.org/3/library/threading.html#meth-thread-join). They are never deleted, since it is impossible to detect the termination of alien threads.

_class_ threading.Thread(_group =None_, _target =None_, _name =None_, _args =()_, _kwargs ={}_, _*_ , _daemon =None_, _context =None_)[¶](https://docs.python.org/3/library/threading.html#threading.Thread "Link to this definition")

This constructor should always be called with keyword arguments. Arguments are:
_group_ should be `None`; reserved for future extension when a `ThreadGroup` class is implemented.
_target_ is the callable object to be invoked by the [`run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run") method. Defaults to `None`, meaning nothing is called.
_name_ is the thread name. By default, a unique name is constructed of the form “Thread-_N_ ” where _N_ is a small decimal number, or “Thread-_N_ (target)” where “target” is `target.__name__` if the _target_ argument is specified.
_args_ is a list or tuple of arguments for the target invocation. Defaults to `()`.
_kwargs_ is a dictionary of keyword arguments for the target invocation. Defaults to `{}`.
If not `None`, _daemon_ explicitly sets whether the thread is daemonic. If `None` (the default), the daemonic property is inherited from the current thread.
_context_ is the [`Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context") value to use when starting the thread. The default value is `None` which indicates that the [`sys.flags.thread_inherit_context`](https://docs.python.org/3/library/sys.html#sys.flags.thread_inherit_context "sys.flags.thread_inherit_context") flag controls the behaviour. If the flag is true, threads will start with a copy of the context of the caller of [`start()`](https://docs.python.org/3/library/threading.html#threading.Thread.start "threading.Thread.start"). If false, they will start with an empty context. To explicitly start with an empty context, pass a new instance of [`Context()`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context"). To explicitly start with a copy of the current context, pass the value from [`copy_context()`](https://docs.python.org/3/library/contextvars.html#contextvars.copy_context "contextvars.copy_context"). The flag defaults true on free-threaded builds and false otherwise.
If the subclass overrides the constructor, it must make sure to invoke the base class constructor (`Thread.__init__()`) before doing anything else to the thread.
Changed in version 3.3: Added the _daemon_ parameter.
Changed in version 3.10: Use the _target_ name if _name_ argument is omitted.
Changed in version 3.14: Added the _context_ parameter.

start()[¶](https://docs.python.org/3/library/threading.html#threading.Thread.start "Link to this definition")

Start the thread’s activity.
It must be called at most once per thread object. It arranges for the object’s [`run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run") method to be invoked in a separate thread of control.
This method will raise a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") if called more than once on the same thread object.
If supported, set the operating system thread name to [`threading.Thread.name`](https://docs.python.org/3/library/threading.html#threading.Thread.name "threading.Thread.name"). The name can be truncated depending on the operating system thread name limits.
Changed in version 3.14: Set the operating system thread name.

run()[¶](https://docs.python.org/3/library/threading.html#threading.Thread.run "Link to this definition")

Method representing the thread’s activity.
You may override this method in a subclass. The standard `run()` method invokes the callable object passed to the object’s constructor as the _target_ argument, if any, with positional and keyword arguments taken from the _args_ and _kwargs_ arguments, respectively.
Using list or tuple as the _args_ argument which passed to the `Thread` could achieve the same effect.
Example:
Copy```
>>> from threading import Thread
>>> t = Thread(target=print, args=[1])
>>> t.run()
1
>>> t = Thread(target=print, args=(1,))
>>> t.run()
1

```


join(_timeout =None_)[¶](https://docs.python.org/3/library/threading.html#threading.Thread.join "Link to this definition")

Wait until the thread terminates. This blocks the calling thread until the thread whose `join()` method is called terminates – either normally or through an unhandled exception – or until the optional timeout occurs.
When the _timeout_ argument is present and not `None`, it should be a floating-point number specifying a timeout for the operation in seconds (or fractions thereof). As `join()` always returns `None`, you must call [`is_alive()`](https://docs.python.org/3/library/threading.html#threading.Thread.is_alive "threading.Thread.is_alive") after `join()` to decide whether a timeout happened – if the thread is still alive, the `join()` call timed out.
When the _timeout_ argument is not present or `None`, the operation will block until the thread terminates.
A thread can be joined many times.
`join()` raises a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") if an attempt is made to join the current thread as that would cause a deadlock. It is also an error to `join()` a thread before it has been started and attempts to do so raise the same exception.
If an attempt is made to join a running daemonic thread in late stages of [Python finalization](https://docs.python.org/3/glossary.html#term-interpreter-shutdown) `join()` raises a [`PythonFinalizationError`](https://docs.python.org/3/library/exceptions.html#PythonFinalizationError "PythonFinalizationError").
Changed in version 3.14: May raise [`PythonFinalizationError`](https://docs.python.org/3/library/exceptions.html#PythonFinalizationError "PythonFinalizationError").

name[¶](https://docs.python.org/3/library/threading.html#threading.Thread.name "Link to this definition")

A string used for identification purposes only. It has no semantics. Multiple threads may be given the same name. The initial name is set by the constructor.
On some platforms, the thread name is set at the operating system level when the thread starts, so that it is visible in task managers. This name may be truncated to fit in a system-specific limit (for example, 15 bytes on Linux or 63 bytes on macOS).
Changes to _name_ are only reflected at the OS level when the currently running thread is renamed. (Setting the _name_ attribute of a different thread only updates the Python Thread object.)

getName()[¶](https://docs.python.org/3/library/threading.html#threading.Thread.getName "Link to this definition")


setName()[¶](https://docs.python.org/3/library/threading.html#threading.Thread.setName "Link to this definition")

Deprecated getter/setter API for [`name`](https://docs.python.org/3/library/threading.html#threading.Thread.name "threading.Thread.name"); use it directly as a property instead.
Deprecated since version 3.10.

ident[¶](https://docs.python.org/3/library/threading.html#threading.Thread.ident "Link to this definition")

The ‘thread identifier’ of this thread or `None` if the thread has not been started. This is a nonzero integer. See the [`get_ident()`](https://docs.python.org/3/library/threading.html#threading.get_ident "threading.get_ident") function. Thread identifiers may be recycled when a thread exits and another thread is created. The identifier is available even after the thread has exited.

native_id[¶](https://docs.python.org/3/library/threading.html#threading.Thread.native_id "Link to this definition")

The Thread ID (`TID`) of this thread, as assigned by the OS (kernel). This is a non-negative integer, or `None` if the thread has not been started. See the [`get_native_id()`](https://docs.python.org/3/library/threading.html#threading.get_native_id "threading.get_native_id") function. This value may be used to uniquely identify this particular thread system-wide (until the thread terminates, after which the value may be recycled by the OS).
Note
Similar to Process IDs, Thread IDs are only valid (guaranteed unique system-wide) from the time the thread is created until the thread has been terminated.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX, DragonFlyBSD.
Added in version 3.8.

is_alive()[¶](https://docs.python.org/3/library/threading.html#threading.Thread.is_alive "Link to this definition")

Return whether the thread is alive.
This method returns `True` just before the [`run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run") method starts until just after the `run()` method terminates. The module function [`enumerate()`](https://docs.python.org/3/library/threading.html#threading.enumerate "threading.enumerate") returns a list of all alive threads.

daemon[¶](https://docs.python.org/3/library/threading.html#threading.Thread.daemon "Link to this definition")

A boolean value indicating whether this thread is a daemon thread (`True`) or not (`False`). This must be set before [`start()`](https://docs.python.org/3/library/threading.html#threading.Thread.start "threading.Thread.start") is called, otherwise [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised. Its initial value is inherited from the creating thread; the main thread is not a daemon thread and therefore all threads created in the main thread default to `daemon` = `False`.
The entire Python program exits when no alive non-daemon threads are left.

isDaemon()[¶](https://docs.python.org/3/library/threading.html#threading.Thread.isDaemon "Link to this definition")


setDaemon()[¶](https://docs.python.org/3/library/threading.html#threading.Thread.setDaemon "Link to this definition")

Deprecated getter/setter API for [`daemon`](https://docs.python.org/3/library/threading.html#threading.Thread.daemon "threading.Thread.daemon"); use it directly as a property instead.
Deprecated since version 3.10.
### Lock objects[¶](https://docs.python.org/3/library/threading.html#lock-objects "Link to this heading")
A primitive lock is a synchronization primitive that is not owned by a particular thread when locked. In Python, it is currently the lowest level synchronization primitive available, implemented directly by the [`_thread`](https://docs.python.org/3/library/_thread.html#module-_thread "_thread: Low-level threading API.") extension module.
A primitive lock is in one of two states, “locked” or “unlocked”. It is created in the unlocked state. It has two basic methods, [`acquire()`](https://docs.python.org/3/library/threading.html#threading.Lock.acquire "threading.Lock.acquire") and [`release()`](https://docs.python.org/3/library/threading.html#threading.Lock.release "threading.Lock.release"). When the state is unlocked, `acquire()` changes the state to locked and returns immediately. When the state is locked, `acquire()` blocks until a call to `release()` in another thread changes it to unlocked, then the `acquire()` call resets it to locked and returns. The `release()` method should only be called in the locked state; it changes the state to unlocked and returns immediately. If an attempt is made to release an unlocked lock, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") will be raised.
Locks also support the [context management protocol](https://docs.python.org/3/library/threading.html#with-locks).
When more than one thread is blocked in [`acquire()`](https://docs.python.org/3/library/threading.html#threading.Lock.acquire "threading.Lock.acquire") waiting for the state to turn to unlocked, only one thread proceeds when a [`release()`](https://docs.python.org/3/library/threading.html#threading.Lock.release "threading.Lock.release") call resets the state to unlocked; which one of the waiting threads proceeds is not defined, and may vary across implementations.
All methods are executed atomically.

_class_ threading.Lock[¶](https://docs.python.org/3/library/threading.html#threading.Lock "Link to this definition")

The class implementing primitive lock objects. Once a thread has acquired a lock, subsequent attempts to acquire it block, until it is released; any thread may release it.
Changed in version 3.13: `Lock` is now a class. In earlier Pythons, `Lock` was a factory function which returned an instance of the underlying private lock type.

acquire(_blocking =True_, _timeout =-1_)[¶](https://docs.python.org/3/library/threading.html#threading.Lock.acquire "Link to this definition")

Acquire a lock, blocking or non-blocking.
When invoked with the _blocking_ argument set to `True` (the default), block until the lock is unlocked, then set it to locked and return `True`.
When invoked with the _blocking_ argument set to `False`, do not block. If a call with _blocking_ set to `True` would block, return `False` immediately; otherwise, set the lock to locked and return `True`.
When invoked with the floating-point _timeout_ argument set to a positive value, block for at most the number of seconds specified by _timeout_ and as long as the lock cannot be acquired. A _timeout_ argument of `-1` specifies an unbounded wait. It is forbidden to specify a _timeout_ when _blocking_ is `False`.
The return value is `True` if the lock is acquired successfully, `False` if not (for example if the _timeout_ expired).
Changed in version 3.2: The _timeout_ parameter is new.
Changed in version 3.2: Lock acquisition can now be interrupted by signals on POSIX if the underlying threading implementation supports it.
Changed in version 3.14: Lock acquisition can now be interrupted by signals on Windows.

release()[¶](https://docs.python.org/3/library/threading.html#threading.Lock.release "Link to this definition")

Release a lock. This can be called from any thread, not only the thread which has acquired the lock.
When the lock is locked, reset it to unlocked, and return. If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed.
When invoked on an unlocked lock, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised.
There is no return value.

locked()[¶](https://docs.python.org/3/library/threading.html#threading.Lock.locked "Link to this definition")

Return `True` if the lock is acquired.
### RLock objects[¶](https://docs.python.org/3/library/threading.html#rlock-objects "Link to this heading")
A reentrant lock is a synchronization primitive that may be acquired multiple times by the same thread. Internally, it uses the concepts of “owning thread” and “recursion level” in addition to the locked/unlocked state used by primitive locks. In the locked state, some thread owns the lock; in the unlocked state, no thread owns it.
Threads call a lock’s [`acquire()`](https://docs.python.org/3/library/threading.html#threading.RLock.acquire "threading.RLock.acquire") method to lock it, and its [`release()`](https://docs.python.org/3/library/threading.html#threading.Lock.release "threading.Lock.release") method to unlock it.
Note
Reentrant locks support the [context management protocol](https://docs.python.org/3/library/threading.html#with-locks), so it is recommended to use [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) instead of manually calling [`acquire()`](https://docs.python.org/3/library/threading.html#threading.RLock.acquire "threading.RLock.acquire") and [`release()`](https://docs.python.org/3/library/threading.html#threading.RLock.release "threading.RLock.release") to handle acquiring and releasing the lock for a block of code.
RLock’s [`acquire()`](https://docs.python.org/3/library/threading.html#threading.RLock.acquire "threading.RLock.acquire")/[`release()`](https://docs.python.org/3/library/threading.html#threading.RLock.release "threading.RLock.release") call pairs may be nested, unlike Lock’s [`acquire()`](https://docs.python.org/3/library/threading.html#threading.Lock.acquire "threading.Lock.acquire")/[`release()`](https://docs.python.org/3/library/threading.html#threading.Lock.release "threading.Lock.release"). Only the final `release()` (the `release()` of the outermost pair) resets the lock to an unlocked state and allows another thread blocked in `acquire()` to proceed.
[`acquire()`](https://docs.python.org/3/library/threading.html#threading.RLock.acquire "threading.RLock.acquire")/[`release()`](https://docs.python.org/3/library/threading.html#threading.RLock.release "threading.RLock.release") must be used in pairs: each acquire must have a release in the thread that has acquired the lock. Failing to call release as many times the lock has been acquired can lead to deadlock.

_class_ threading.RLock[¶](https://docs.python.org/3/library/threading.html#threading.RLock "Link to this definition")

This class implements reentrant lock objects. A reentrant lock must be released by the thread that acquired it. Once a thread has acquired a reentrant lock, the same thread may acquire it again without blocking; the thread must release it once for each time it has acquired it.
Note that `RLock` is actually a factory function which returns an instance of the most efficient version of the concrete RLock class that is supported by the platform.

acquire(_blocking =True_, _timeout =-1_)[¶](https://docs.python.org/3/library/threading.html#threading.RLock.acquire "Link to this definition")

Acquire a lock, blocking or non-blocking.
See also

[Using RLock as a context manager](https://docs.python.org/3/library/threading.html#with-locks)

Recommended over manual `acquire()` and [`release()`](https://docs.python.org/3/library/threading.html#threading.RLock.release "threading.RLock.release") calls whenever practical.
When invoked with the _blocking_ argument set to `True` (the default):
>   * If no thread owns the lock, acquire the lock and return immediately.
>   * If another thread owns the lock, block until we are able to acquire lock, or _timeout_ , if set to a positive float value.
>   * If the same thread owns the lock, acquire the lock again, and return immediately. This is the difference between [`Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock") and `RLock`; `Lock` handles this case the same as the previous, blocking until the lock can be acquired.
>

When invoked with the _blocking_ argument set to `False`:
>   * If no thread owns the lock, acquire the lock and return immediately.
>   * If another thread owns the lock, return immediately.
>   * If the same thread owns the lock, acquire the lock again and return immediately.
>

In all cases, if the thread was able to acquire the lock, return `True`. If the thread was unable to acquire the lock (i.e. if not blocking or the timeout was reached) return `False`.
If called multiple times, failing to call [`release()`](https://docs.python.org/3/library/threading.html#threading.RLock.release "threading.RLock.release") as many times may lead to deadlock. Consider using `RLock` as a context manager rather than calling acquire/release directly.
Changed in version 3.2: The _timeout_ parameter is new.

release()[¶](https://docs.python.org/3/library/threading.html#threading.RLock.release "Link to this definition")

Release a lock, decrementing the recursion level. If after the decrement it is zero, reset the lock to unlocked (not owned by any thread), and if any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed. If after the decrement the recursion level is still nonzero, the lock remains locked and owned by the calling thread.
Only call this method when the calling thread owns the lock. A [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised if this method is called when the lock is not acquired.
There is no return value.

locked()[¶](https://docs.python.org/3/library/threading.html#threading.RLock.locked "Link to this definition")

Return a boolean indicating whether this object is locked right now.
Added in version 3.14.
### Condition objects[¶](https://docs.python.org/3/library/threading.html#condition-objects "Link to this heading")
A condition variable is always associated with some kind of lock; this can be passed in or one will be created by default. Passing one in is useful when several condition variables must share the same lock. The lock is part of the condition object: you don’t have to track it separately.
A condition variable obeys the [context management protocol](https://docs.python.org/3/library/threading.html#with-locks): using the `with` statement acquires the associated lock for the duration of the enclosed block. The [`acquire()`](https://docs.python.org/3/library/threading.html#threading.Condition.acquire "threading.Condition.acquire") and [`release()`](https://docs.python.org/3/library/threading.html#threading.Condition.release "threading.Condition.release") methods also call the corresponding methods of the associated lock.
Other methods must be called with the associated lock held. The [`wait()`](https://docs.python.org/3/library/threading.html#threading.Condition.wait "threading.Condition.wait") method releases the lock, and then blocks until another thread awakens it by calling [`notify()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify "threading.Condition.notify") or [`notify_all()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify_all "threading.Condition.notify_all"). Once awakened, `wait()` re-acquires the lock and returns. It is also possible to specify a timeout.
The [`notify()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify "threading.Condition.notify") method wakes up one of the threads waiting for the condition variable, if any are waiting. The [`notify_all()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify_all "threading.Condition.notify_all") method wakes up all threads waiting for the condition variable.
Note: the [`notify()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify "threading.Condition.notify") and [`notify_all()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify_all "threading.Condition.notify_all") methods don’t release the lock; this means that the thread or threads awakened will not return from their [`wait()`](https://docs.python.org/3/library/threading.html#threading.Condition.wait "threading.Condition.wait") call immediately, but only when the thread that called `notify()` or `notify_all()` finally relinquishes ownership of the lock.
The typical programming style using condition variables uses the lock to synchronize access to some shared state; threads that are interested in a particular change of state call [`wait()`](https://docs.python.org/3/library/threading.html#threading.Condition.wait "threading.Condition.wait") repeatedly until they see the desired state, while threads that modify the state call [`notify()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify "threading.Condition.notify") or [`notify_all()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify_all "threading.Condition.notify_all") when they change the state in such a way that it could possibly be a desired state for one of the waiters. For example, the following code is a generic producer-consumer situation with unlimited buffer capacity:
Copy```
