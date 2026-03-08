#  `multiprocessing` — Process-based parallelism[¶](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "Link to this heading")
**Source code:**
* * *
[Availability](https://docs.python.org/3/library/intro.html#availability): not Android, not iOS, not WASI.
This module is not supported on [mobile platforms](https://docs.python.org/3/library/intro.html#mobile-availability) or [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability).
## Introduction[¶](https://docs.python.org/3/library/multiprocessing.html#introduction "Link to this heading")
`multiprocessing` is a package that supports spawning processes using an API similar to the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.") module. The `multiprocessing` package offers both local and remote concurrency, effectively side-stepping the [Global Interpreter Lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock) by using subprocesses instead of threads. Due to this, the `multiprocessing` module allows the programmer to fully leverage multiple processors on a given machine. It runs on both POSIX and Windows.
The `multiprocessing` module also introduces the [`Pool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool") object which offers a convenient means of parallelizing the execution of a function across multiple input values, distributing the input data across processes (data parallelism). The following example demonstrates the common practice of defining such functions in a module so that child processes can successfully import that module. This basic example of data parallelism using `Pool`,
Copy```
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

```

will print to standard output
Copy```
[1, 4, 9]

```

The `multiprocessing` module also introduces APIs which do not have analogs in the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.") module, like the ability to [`terminate`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.terminate "multiprocessing.Process.terminate"), [`interrupt`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.interrupt "multiprocessing.Process.interrupt") or [`kill`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.kill "multiprocessing.Process.kill") a running process.
See also
[`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor") offers a higher level interface to push tasks to a background process without blocking execution of the calling process. Compared to using the [`Pool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool") interface directly, the [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures "concurrent.futures: Execute computations concurrently using threads or processes.") API more readily allows the submission of work to the underlying process pool to be separated from waiting for the results.
### The [`Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process") class[¶](https://docs.python.org/3/library/multiprocessing.html#the-process-class "Link to this heading")
In `multiprocessing`, processes are spawned by creating a [`Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process") object and then calling its [`start()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.start "multiprocessing.Process.start") method. `Process` follows the API of [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread"). A trivial example of a multiprocess program is
Copy```
from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

```

To show the individual process IDs involved, here is an expanded example:
Copy```
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

```

For an explanation of why the `if __name__ == '__main__'` part is necessary, see [Programming guidelines](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming).
The arguments to [`Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process") usually need to be unpickleable from within the child process. If you tried typing the above example directly into a REPL it could lead to an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") in the child process trying to locate the _f_ function in the `__main__` module.
### Contexts and start methods[¶](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods "Link to this heading")
Depending on the platform, `multiprocessing` supports three ways to start a process. These _start methods_ are
>

_spawn_

> The parent process starts a fresh Python interpreter process. The child process will only inherit those resources necessary to run the process object’s [`run()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.run "multiprocessing.Process.run") method. In particular, unnecessary file descriptors and handles from the parent process will not be inherited. Starting a process using this method is rather slow compared to using _fork_ or _forkserver_.
> Available on POSIX and Windows platforms. The default on Windows and macOS.

_fork_

> The parent process uses [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork") to fork the Python interpreter. The child process, when it begins, is effectively identical to the parent process. All resources of the parent are inherited by the child process. Note that safely forking a multithreaded process is problematic.
> Available on POSIX systems.
> Changed in version 3.14: This is no longer the default start method on any platform. Code that requires _fork_ must explicitly specify that via [`get_context()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.get_context "multiprocessing.get_context") or [`set_start_method()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_start_method "multiprocessing.set_start_method").
> Changed in version 3.12: If Python is able to detect that your process has multiple threads, the [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork") function that this start method calls internally will raise a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning"). Use a different start method. See the `os.fork()` documentation for further explanation.

_forkserver_

> When the program starts and selects the _forkserver_ start method, a server process is spawned. From then on, whenever a new process is needed, the parent process connects to the server and requests that it fork a new process. The fork server process is single threaded unless system libraries or preloaded imports spawn threads as a side-effect so it is generally safe for it to use [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork"). No unnecessary resources are inherited.
> Available on POSIX platforms which support passing file descriptors over Unix pipes such as Linux. The default on those.
> Changed in version 3.14: This became the default start method on POSIX platforms.
Changed in version 3.4: _spawn_ added on all POSIX platforms, and _forkserver_ added for some POSIX platforms. Child processes no longer inherit all of the parents inheritable handles on Windows.
Changed in version 3.8: On macOS, the _spawn_ start method is now the default. The _fork_ start method should be considered unsafe as it can lead to crashes of the subprocess as macOS system libraries may start threads. See [bpo-33725](https://bugs.python.org/issue?@action=redirect&bpo=33725).
Changed in version 3.14: On POSIX platforms the default start method was changed from _fork_ to _forkserver_ to retain the performance but avoid common multithreaded process incompatibilities. See
On POSIX using the _spawn_ or _forkserver_ start methods will also start a _resource tracker_ process which tracks the unlinked named system resources (such as named semaphores or [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory") objects) created by processes of the program. When all processes have exited the resource tracker unlinks any remaining tracked object. Usually there should be none, but if a process was killed by a signal there may be some “leaked” resources. (Neither leaked semaphores nor shared memory segments will be automatically unlinked until the next reboot. This is problematic for both objects because the system allows only a limited number of named semaphores, and shared memory segments occupy some space in the main memory.)
To select a start method you use the [`set_start_method()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_start_method "multiprocessing.set_start_method") in the `if __name__ == '__main__'` clause of the main module. For example:
Copy```
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    p = mp.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()

```

[`set_start_method()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_start_method "multiprocessing.set_start_method") should not be used more than once in the program.
Alternatively, you can use [`get_context()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.get_context "multiprocessing.get_context") to obtain a context object. Context objects have the same API as the multiprocessing module, and allow one to use multiple start methods in the same program.
Copy```
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()

```

Note that objects related to one context may not be compatible with processes for a different context. In particular, locks created using the _fork_ context cannot be passed to processes started using the _spawn_ or _forkserver_ start methods.
Libraries using `multiprocessing` or [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor") should be designed to allow their users to provide their own multiprocessing context. Using a specific context of your own within a library can lead to incompatibilities with the rest of the library user’s application. Always document if your library requires a specific start method.
Warning
The `'spawn'` and `'forkserver'` start methods generally cannot be used with “frozen” executables (i.e., binaries produced by packages like **PyInstaller** and **cx_Freeze**) on POSIX systems. The `'fork'` start method may work if code does not use threads.
### Exchanging objects between processes[¶](https://docs.python.org/3/library/multiprocessing.html#exchanging-objects-between-processes "Link to this heading")
`multiprocessing` supports two types of communication channel between processes:
**Queues**
> The [`Queue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue "multiprocessing.Queue") class is a near clone of [`queue.Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue"). For example:
> Copy```
from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()

```

> Queues are thread and process safe. Any object put into a `multiprocessing` queue will be serialized.
**Pipes**
> The [`Pipe()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Pipe "multiprocessing.Pipe") function returns a pair of connection objects connected by a pipe which by default is duplex (two-way). For example:
> Copy```
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()

```

> The two connection objects returned by [`Pipe()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Pipe "multiprocessing.Pipe") represent the two ends of the pipe. Each connection object has `send()` and `recv()` methods (among others). Note that data in a pipe may become corrupted if two processes (or threads) try to read from or write to the _same_ end of the pipe at the same time. Of course there is no risk of corruption from processes using different ends of the pipe at the same time.
> The `send()` method serializes the object and `recv()` re-creates the object.
### Synchronization between processes[¶](https://docs.python.org/3/library/multiprocessing.html#synchronization-between-processes "Link to this heading")
`multiprocessing` contains equivalents of all the synchronization primitives from [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism."). For instance one can use a lock to ensure that only one process prints to standard output at a time:
Copy```
from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()

```

Without using the lock output from the different processes is liable to get all mixed up.
### Sharing state between processes[¶](https://docs.python.org/3/library/multiprocessing.html#sharing-state-between-processes "Link to this heading")
As mentioned above, when doing concurrent programming it is usually best to avoid using shared state as far as possible. This is particularly true when using multiple processes.
However, if you really do need to use some shared data then `multiprocessing` provides a couple of ways of doing so.
**Shared memory**
> Data can be stored in a shared memory map using [`Value`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Value "multiprocessing.Value") or [`Array`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Array "multiprocessing.Array"). For example, the following code
> Copy```
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])

```

> will print
> Copy```
3.1415927
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

```

> The `'d'` and `'i'` arguments used when creating `num` and `arr` are typecodes of the kind used by the [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.") module: `'d'` indicates a double precision float and `'i'` indicates a signed integer. These shared objects will be process and thread-safe.
> For more flexibility in using shared memory one can use the [`multiprocessing.sharedctypes`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.sharedctypes "multiprocessing.sharedctypes: Allocate ctypes objects from shared memory.") module which supports the creation of arbitrary ctypes objects allocated from shared memory.
**Server process**
> A manager object returned by [`Manager()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Manager "multiprocessing.Manager") controls a server process which holds Python objects and allows other processes to manipulate them using proxies.
> A manager returned by [`Manager()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Manager "multiprocessing.Manager") will support types [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), [`Namespace`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.Namespace "multiprocessing.managers.Namespace"), [`Lock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock "multiprocessing.Lock"), [`RLock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.RLock "multiprocessing.RLock"), [`Semaphore`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Semaphore "multiprocessing.Semaphore"), [`BoundedSemaphore`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.BoundedSemaphore "multiprocessing.BoundedSemaphore"), [`Condition`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Condition "multiprocessing.Condition"), [`Event`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Event "multiprocessing.Event"), [`Barrier`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Barrier "multiprocessing.Barrier"), [`Queue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue "multiprocessing.Queue"), [`Value`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Value "multiprocessing.Value") and [`Array`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Array "multiprocessing.Array"). For example,
> Copy```
from multiprocessing import Process, Manager

def f(d, l, s):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()
    s.add('a')
    s.add('b')

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))
        s = manager.set()

        p = Process(target=f, args=(d, l, s))
        p.start()
        p.join()

        print(d)
        print(l)
        print(s)

```

> will print
> Copy```
{0.25: None, 1: '1', '2': 2}
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
{'a', 'b'}

```

> Server process managers are more flexible than using shared memory objects because they can be made to support arbitrary object types. Also, a single manager can be shared by processes on different computers over a network. They are, however, slower than using shared memory.
### Using a pool of workers[¶](https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers "Link to this heading")
The [`Pool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool") class represents a pool of worker processes. It has methods which allows tasks to be offloaded to the worker processes in a few different ways.
For example:
Copy```
from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    return x*x

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # print same numbers in arbitrary order
        for i in pool.imap_unordered(f, range(10)):
            print(i)

        # evaluate "f(20)" asynchronously
        res = pool.apply_async(f, (20,))      # runs in *only* one process
        print(res.get(timeout=1))             # prints "400"

        # evaluate "os.getpid()" asynchronously
        res = pool.apply_async(os.getpid, ()) # runs in *only* one process
        print(res.get(timeout=1))             # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        # make a single worker sleep for 10 seconds
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")

```

Note that the methods of a pool should only ever be used by the process which created it.
Note
Functionality within this package requires that the `__main__` module be importable by the children. This is covered in [Programming guidelines](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming) however it is worth pointing out here. This means that some examples, such as the [`multiprocessing.pool.Pool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool") examples will not work in the interactive interpreter. For example:
Copy```
>>> from multiprocessing import Pool
>>> p = Pool(5)
>>> def f(x):
...     return x*x
...
>>> with p:
...     p.map(f, [1,2,3])
Process PoolWorker-1:
Process PoolWorker-2:
Process PoolWorker-3:
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
AttributeError: Can't get attribute 'f' on <module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>
AttributeError: Can't get attribute 'f' on <module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>
AttributeError: Can't get attribute 'f' on <module '__main__' (<class '_frozen_importlib.BuiltinImporter'>)>

```

(If you try this it will actually output three full tracebacks interleaved in a semi-random fashion, and then you may have to stop the parent process somehow.)
## Reference[¶](https://docs.python.org/3/library/multiprocessing.html#reference "Link to this heading")
The `multiprocessing` package mostly replicates the API of the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.") module.
### Global start method[¶](https://docs.python.org/3/library/multiprocessing.html#global-start-method "Link to this heading")
Python supports several ways to create and initialize a process. The global start method sets the default mechanism for creating a process.
Several multiprocessing functions and methods that may also instantiate certain objects will implicitly set the global start method to the system’s default, if it hasn’t been set already. The global start method can only be set once. If you need to change the start method from the system default, you must proactively set the global start method before calling functions or methods, or creating these objects.
###  [`Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process") and exceptions[¶](https://docs.python.org/3/library/multiprocessing.html#process-and-exceptions "Link to this heading")

_class_ multiprocessing.Process(_group =None_, _target =None_, _name =None_, _args =()_, _kwargs ={}_, _*_ , _daemon =None_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "Link to this definition")

Process objects represent activity that is run in a separate process. The `Process` class has equivalents of all the methods of [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread").
The constructor should always be called with keyword arguments. _group_ should always be `None`; it exists solely for compatibility with [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread"). _target_ is the callable object to be invoked by the [`run()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.run "multiprocessing.Process.run") method. It defaults to `None`, meaning nothing is called. _name_ is the process name (see [`name`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.name "multiprocessing.Process.name") for more details). _args_ is the argument tuple for the target invocation. _kwargs_ is a dictionary of keyword arguments for the target invocation. If provided, the keyword-only _daemon_ argument sets the process [`daemon`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.daemon "multiprocessing.Process.daemon") flag to `True` or `False`. If `None` (the default), this flag will be inherited from the creating process.
By default, no arguments are passed to _target_. The _args_ argument, which defaults to `()`, can be used to specify a list or tuple of the arguments to pass to _target_.
If a subclass overrides the constructor, it must make sure it invokes the base class constructor (`super().__init__()`) before doing anything else to the process.
Note
In general, all arguments to `Process` must be picklable. This is frequently observed when trying to create a `Process` or use a [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor") from a REPL with a locally defined _target_ function.
Passing a callable object defined in the current REPL session causes the child process to die via an uncaught [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") exception when starting as _target_ must have been defined within an importable module in order to be loaded during unpickling.
Example of this uncatchable error from the child:
Copy```
>>> import multiprocessing as mp
>>> def knigit():
...     print("Ni!")
...
>>> process = mp.Process(target=knigit)
>>> process.start()
>>> Traceback (most recent call last):
  File ".../multiprocessing/spawn.py", line ..., in spawn_main
  File ".../multiprocessing/spawn.py", line ..., in _main
AttributeError: module '__main__' has no attribute 'knigit'
>>> process
<SpawnProcess name='SpawnProcess-1' pid=379473 parent=378707 stopped exitcode=1>

```

See [The spawn and forkserver start methods](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming-spawn). While this restriction is not true if using the `"fork"` start method, as of Python `3.14` that is no longer the default on any platform. See [Contexts and start methods](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-start-methods). See also
Changed in version 3.3: Added the _daemon_ parameter.

run()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.run "Link to this definition")

Method representing the process’s activity.
You may override this method in a subclass. The standard `run()` method invokes the callable object passed to the object’s constructor as the target argument, if any, with sequential and keyword arguments taken from the _args_ and _kwargs_ arguments, respectively.
Using a list or tuple as the _args_ argument passed to `Process` achieves the same effect.
Example:
Copy```
>>> from multiprocessing import Process
>>> p = Process(target=print, args=[1])
>>> p.run()
1
>>> p = Process(target=print, args=(1,))
>>> p.run()
1

```


start()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.start "Link to this definition")

Start the process’s activity.
This must be called at most once per process object. It arranges for the object’s [`run()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.run "multiprocessing.Process.run") method to be invoked in a separate process.

join([_timeout_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.join "Link to this definition")

If the optional argument _timeout_ is `None` (the default), the method blocks until the process whose `join()` method is called terminates. If _timeout_ is a positive number, it blocks at most _timeout_ seconds. Note that the method returns `None` if its process terminates or if the method times out. Check the process’s [`exitcode`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.exitcode "multiprocessing.Process.exitcode") to determine if it terminated.
A process can be joined many times.
A process cannot join itself because this would cause a deadlock. It is an error to attempt to join a process before it has been started.

name[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.name "Link to this definition")

The process’s name. The name is a string used for identification purposes only. It has no semantics. Multiple processes may be given the same name.
The initial name is set by the constructor. If no explicit name is provided to the constructor, a name of the form ‘Process-N1:N2:…:Nk’ is constructed, where each Nk is the N-th child of its parent.

is_alive()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.is_alive "Link to this definition")

Return whether the process is alive.
Roughly, a process object is alive from the moment the [`start()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.start "multiprocessing.Process.start") method returns until the child process terminates.

daemon[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.daemon "Link to this definition")

The process’s daemon flag, a Boolean value. This must be set before [`start()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.start "multiprocessing.Process.start") is called.
The initial value is inherited from the creating process.
When a process exits, it attempts to terminate all of its daemonic child processes.
Note that a daemonic process is not allowed to create child processes. Otherwise a daemonic process would leave its children orphaned if it gets terminated when its parent process exits. Additionally, these are **not** Unix daemons or services, they are normal processes that will be terminated (and not joined) if non-daemonic processes have exited.
In addition to the [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") API, `Process` objects also support the following attributes and methods:

pid[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.pid "Link to this definition")

Return the process ID. Before the process is spawned, this will be `None`.

exitcode[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.exitcode "Link to this definition")

The child’s exit code. This will be `None` if the process has not yet terminated.
If the child’s [`run()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.run "multiprocessing.Process.run") method returned normally, the exit code will be 0. If it terminated via [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit") with an integer argument _N_ , the exit code will be _N_.
If the child terminated due to an exception not caught within [`run()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.run "multiprocessing.Process.run"), the exit code will be 1. If it was terminated by signal _N_ , the exit code will be the negative value _-N_.

authkey[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.authkey "Link to this definition")

The process’s authentication key (a byte string).
When `multiprocessing` is initialized the main process is assigned a random string using [`os.urandom()`](https://docs.python.org/3/library/os.html#os.urandom "os.urandom").
When a `Process` object is created, it will inherit the authentication key of its parent process, although this may be changed by setting [`authkey`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.authkey "multiprocessing.Process.authkey") to another byte string.
See [Authentication keys](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-auth-keys).

sentinel[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.sentinel "Link to this definition")

A numeric handle of a system object which will become “ready” when the process ends.
You can use this value if you want to wait on several events at once using [`multiprocessing.connection.wait()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.wait "multiprocessing.connection.wait"). Otherwise calling [`join()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.join "multiprocessing.Process.join") is simpler.
On Windows, this is an OS handle usable with the `WaitForSingleObject` and `WaitForMultipleObjects` family of API calls. On POSIX, this is a file descriptor usable with primitives from the [`select`](https://docs.python.org/3/library/select.html#module-select "select: Wait for I/O completion on multiple streams.") module.
Added in version 3.3.

interrupt()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.interrupt "Link to this definition")

Terminate the process. Works on POSIX using the [`SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT") signal. Behavior on Windows is undefined.
By default, this terminates the child process by raising [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt"). This behavior can be altered by setting the respective signal handler in the child process [`signal.signal()`](https://docs.python.org/3/library/signal.html#signal.signal "signal.signal") for [`SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT").
Note: if the child process catches and discards [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt"), the process will not be terminated.
Note: the default behavior will also set [`exitcode`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.exitcode "multiprocessing.Process.exitcode") to `1` as if an uncaught exception was raised in the child process. To have a different `exitcode` you may simply catch [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt") and call `exit(your_code)`.
Added in version 3.14.

terminate()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.terminate "Link to this definition")

Terminate the process. On POSIX this is done using the [`SIGTERM`](https://docs.python.org/3/library/signal.html#signal.SIGTERM "signal.SIGTERM") signal; on Windows `TerminateProcess()` is used. Note that exit handlers and finally clauses, etc., will not be executed.
Note that descendant processes of the process will _not_ be terminated – they will simply become orphaned.
Warning
If this method is used when the associated process is using a pipe or queue then the pipe or queue is liable to become corrupted and may become unusable by other process. Similarly, if the process has acquired a lock or semaphore etc. then terminating it is liable to cause other processes to deadlock.

kill()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.kill "Link to this definition")

Same as [`terminate()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.terminate "multiprocessing.Process.terminate") but using the `SIGKILL` signal on POSIX.
Added in version 3.7.

close()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.close "Link to this definition")

Close the `Process` object, releasing all resources associated with it. [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the underlying process is still running. Once `close()` returns successfully, most other methods and attributes of the `Process` object will raise `ValueError`.
Added in version 3.7.
Note that the [`start()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.start "multiprocessing.Process.start"), [`join()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.join "multiprocessing.Process.join"), [`is_alive()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.is_alive "multiprocessing.Process.is_alive"), [`terminate()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.terminate "multiprocessing.Process.terminate") and [`exitcode`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.exitcode "multiprocessing.Process.exitcode") methods should only be called by the process that created the process object.
Example usage of some of the methods of `Process`:
Copy```
>>> import multiprocessing, time, signal
>>> mp_context = multiprocessing.get_context('spawn')
>>> p = mp_context.Process(target=time.sleep, args=(1000,))
>>> print(p, p.is_alive())
<...Process ... initial> False
>>> p.start()
>>> print(p, p.is_alive())
<...Process ... started> True
>>> p.terminate()
>>> time.sleep(0.1)
>>> print(p, p.is_alive())
<...Process ... stopped exitcode=-SIGTERM> False
>>> p.exitcode == -signal.SIGTERM
True

```


_exception_ multiprocessing.ProcessError[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.ProcessError "Link to this definition")

The base class of all `multiprocessing` exceptions.

_exception_ multiprocessing.BufferTooShort[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.BufferTooShort "Link to this definition")

Exception raised by `Connection.recv_bytes_into()` when the supplied buffer object is too small for the message read.
If `e` is an instance of `BufferTooShort` then `e.args[0]` will give the message as a byte string.

_exception_ multiprocessing.AuthenticationError[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.AuthenticationError "Link to this definition")

Raised when there is an authentication error.

_exception_ multiprocessing.TimeoutError[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.TimeoutError "Link to this definition")

Raised by methods with a timeout when the timeout expires.
### Pipes and Queues[¶](https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues "Link to this heading")
When using multiple processes, one generally uses message passing for communication between processes and avoids having to use any synchronization primitives like locks.
For passing messages one can use [`Pipe()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Pipe "multiprocessing.Pipe") (for a connection between two processes) or a queue (which allows multiple producers and consumers).
The [`Queue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue "multiprocessing.Queue"), [`SimpleQueue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.SimpleQueue "multiprocessing.SimpleQueue") and [`JoinableQueue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.JoinableQueue "multiprocessing.JoinableQueue") types are multi-producer, multi-consumer FIFO queues modelled on the [`queue.Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") class in the standard library. They differ in that `Queue` lacks the [`task_done()`](https://docs.python.org/3/library/queue.html#queue.Queue.task_done "queue.Queue.task_done") and [`join()`](https://docs.python.org/3/library/queue.html#queue.Queue.join "queue.Queue.join") methods introduced into Python 2.5’s `queue.Queue` class.
If you use [`JoinableQueue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.JoinableQueue "multiprocessing.JoinableQueue") then you **must** call [`JoinableQueue.task_done()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.JoinableQueue.task_done "multiprocessing.JoinableQueue.task_done") for each task removed from the queue or else the semaphore used to count the number of unfinished tasks may eventually overflow, raising an exception.
One difference from other Python queue implementations, is that `multiprocessing` queues serializes all objects that are put into them using [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back."). The object returned by the get method is a re-created object that does not share memory with the original object.
Note that one can also create a shared queue by using a manager object – see [Managers](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-managers).
Note
`multiprocessing` uses the usual [`queue.Empty`](https://docs.python.org/3/library/queue.html#queue.Empty "queue.Empty") and [`queue.Full`](https://docs.python.org/3/library/queue.html#queue.Full "queue.Full") exceptions to signal a timeout. They are not available in the `multiprocessing` namespace so you need to import them from [`queue`](https://docs.python.org/3/library/queue.html#module-queue "queue: A synchronized queue class.").
Note
When an object is put on a queue, the object is pickled and a background thread later flushes the pickled data to an underlying pipe. This has some consequences which are a little surprising, but should not cause any practical difficulties – if they really bother you then you can instead use a queue created with a [manager](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-managers).
  1. After putting an object on an empty queue there may be an infinitesimal delay before the queue’s [`empty()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.empty "multiprocessing.Queue.empty") method returns [`False`](https://docs.python.org/3/library/constants.html#False "False") and [`get_nowait()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.get_nowait "multiprocessing.Queue.get_nowait") can return without raising [`queue.Empty`](https://docs.python.org/3/library/queue.html#queue.Empty "queue.Empty").
  2. If multiple processes are enqueuing objects, it is possible for the objects to be received at the other end out-of-order. However, objects enqueued by the same process will always be in the expected order with respect to each other.


Warning
If a process is killed using [`Process.terminate()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.terminate "multiprocessing.Process.terminate") or [`os.kill()`](https://docs.python.org/3/library/os.html#os.kill "os.kill") while it is trying to use a [`Queue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue "multiprocessing.Queue"), then the data in the queue is likely to become corrupted. This may cause any other process to get an exception when it tries to use the queue later on.
Warning
As mentioned above, if a child process has put items on a queue (and it has not used [`JoinableQueue.cancel_join_thread`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.cancel_join_thread "multiprocessing.Queue.cancel_join_thread")), then that process will not terminate until all buffered items have been flushed to the pipe.
This means that if you try joining that process you may get a deadlock unless you are sure that all items which have been put on the queue have been consumed. Similarly, if the child process is non-daemonic then the parent process may hang on exit when it tries to join all its non-daemonic children.
Note that a queue created using a manager does not have this issue. See [Programming guidelines](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming).
For an example of the usage of queues for interprocess communication see [Examples](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-examples).

multiprocessing.Pipe(_duplex =True_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Pipe "Link to this definition")

Returns a pair `(conn1, conn2)` of [`Connection`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection "multiprocessing.connection.Connection") objects representing the ends of a pipe.
If _duplex_ is `True` (the default) then the pipe is bidirectional. If _duplex_ is `False` then the pipe is unidirectional: `conn1` can only be used for receiving messages and `conn2` can only be used for sending messages.
The `send()` method serializes the object using [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and the `recv()` re-creates the object.

_class_ multiprocessing.Queue([_maxsize_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue "Link to this definition")

Returns a process shared queue implemented using a pipe and a few locks/semaphores. When a process first puts an item on the queue a feeder thread is started which transfers objects from a buffer into the pipe.
Instantiating this class may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.
The usual [`queue.Empty`](https://docs.python.org/3/library/queue.html#queue.Empty "queue.Empty") and [`queue.Full`](https://docs.python.org/3/library/queue.html#queue.Full "queue.Full") exceptions from the standard library’s [`queue`](https://docs.python.org/3/library/queue.html#module-queue "queue: A synchronized queue class.") module are raised to signal timeouts.
`Queue` implements all the methods of [`queue.Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") except for [`task_done()`](https://docs.python.org/3/library/queue.html#queue.Queue.task_done "queue.Queue.task_done") and [`join()`](https://docs.python.org/3/library/queue.html#queue.Queue.join "queue.Queue.join").

qsize()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.qsize "Link to this definition")

Return the approximate size of the queue. Because of multithreading/multiprocessing semantics, this number is not reliable.
Note that this may raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") on platforms like macOS where `sem_getvalue()` is not implemented.

empty()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.empty "Link to this definition")

Return `True` if the queue is empty, `False` otherwise. Because of multithreading/multiprocessing semantics, this is not reliable.
May raise an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") on closed queues. (not guaranteed)

full()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.full "Link to this definition")

Return `True` if the queue is full, `False` otherwise. Because of multithreading/multiprocessing semantics, this is not reliable.

put(_obj_[, _block_[, _timeout_]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.put "Link to this definition")

Put obj into the queue. If the optional argument _block_ is `True` (the default) and _timeout_ is `None` (the default), block if necessary until a free slot is available. If _timeout_ is a positive number, it blocks at most _timeout_ seconds and raises the [`queue.Full`](https://docs.python.org/3/library/queue.html#queue.Full "queue.Full") exception if no free slot was available within that time. Otherwise (_block_ is `False`), put an item on the queue if a free slot is immediately available, else raise the `queue.Full` exception (_timeout_ is ignored in that case).
Changed in version 3.8: If the queue is closed, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised instead of [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError").

put_nowait(_obj_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.put_nowait "Link to this definition")

Equivalent to `put(obj, False)`.

get([_block_[, _timeout_]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.get "Link to this definition")

Remove and return an item from the queue. If optional args _block_ is `True` (the default) and _timeout_ is `None` (the default), block if necessary until an item is available. If _timeout_ is a positive number, it blocks at most _timeout_ seconds and raises the [`queue.Empty`](https://docs.python.org/3/library/queue.html#queue.Empty "queue.Empty") exception if no item was available within that time. Otherwise (block is `False`), return an item if one is immediately available, else raise the `queue.Empty` exception (_timeout_ is ignored in that case).
Changed in version 3.8: If the queue is closed, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised instead of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

get_nowait()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.get_nowait "Link to this definition")

Equivalent to `get(False)`.
[`multiprocessing.Queue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue "multiprocessing.Queue") has a few additional methods not found in [`queue.Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue"). These methods are usually unnecessary for most code:

close()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.close "Link to this definition")

Close the queue: release internal resources.
A queue must not be used anymore after it is closed. For example, [`get()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.get "multiprocessing.Queue.get"), [`put()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.put "multiprocessing.Queue.put") and [`empty()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.empty "multiprocessing.Queue.empty") methods must no longer be called.
The background thread will quit once it has flushed all buffered data to the pipe. This is called automatically when the queue is garbage collected.

join_thread()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.join_thread "Link to this definition")

Join the background thread. This can only be used after [`close()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.close "multiprocessing.Queue.close") has been called. It blocks until the background thread exits, ensuring that all data in the buffer has been flushed to the pipe.
By default if a process is not the creator of the queue then on exit it will attempt to join the queue’s background thread. The process can call [`cancel_join_thread()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.cancel_join_thread "multiprocessing.Queue.cancel_join_thread") to make `join_thread()` do nothing.

cancel_join_thread()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.cancel_join_thread "Link to this definition")

Prevent [`join_thread()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.join_thread "multiprocessing.Queue.join_thread") from blocking. In particular, this prevents the background thread from being joined automatically when the process exits – see `join_thread()`.
A better name for this method might be `allow_exit_without_flush()`. It is likely to cause enqueued data to be lost, and you almost certainly will not need to use it. It is really only there if you need the current process to exit immediately without waiting to flush enqueued data to the underlying pipe, and you don’t care about lost data.
Note
This class’s functionality requires a functioning shared semaphore implementation on the host operating system. Without one, the functionality in this class will be disabled, and attempts to instantiate a `Queue` will result in an [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError"). See [bpo-3770](https://bugs.python.org/issue?@action=redirect&bpo=3770) for additional information. The same holds true for any of the specialized queue types listed below.

_class_ multiprocessing.SimpleQueue[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.SimpleQueue "Link to this definition")

It is a simplified [`Queue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue "multiprocessing.Queue") type, very close to a locked [`Pipe`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Pipe "multiprocessing.Pipe").
Instantiating this class may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.

close()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.SimpleQueue.close "Link to this definition")

Close the queue: release internal resources.
A queue must not be used anymore after it is closed. For example, [`get()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.SimpleQueue.get "multiprocessing.SimpleQueue.get"), [`put()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.SimpleQueue.put "multiprocessing.SimpleQueue.put") and [`empty()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.SimpleQueue.empty "multiprocessing.SimpleQueue.empty") methods must no longer be called.
Added in version 3.9.

empty()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.SimpleQueue.empty "Link to this definition")

Return `True` if the queue is empty, `False` otherwise.
Always raises an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if the SimpleQueue is closed.

get()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.SimpleQueue.get "Link to this definition")

Remove and return an item from the queue.

put(_item_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.SimpleQueue.put "Link to this definition")

Put _item_ into the queue.

_class_ multiprocessing.JoinableQueue([_maxsize_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.JoinableQueue "Link to this definition")

`JoinableQueue`, a [`Queue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue "multiprocessing.Queue") subclass, is a queue which additionally has [`task_done()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.JoinableQueue.task_done "multiprocessing.JoinableQueue.task_done") and [`join()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.JoinableQueue.join "multiprocessing.JoinableQueue.join") methods.
Instantiating this class may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.

task_done()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.JoinableQueue.task_done "Link to this definition")

Indicate that a formerly enqueued task is complete. Used by queue consumers. For each [`get()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.get "multiprocessing.Queue.get") used to fetch a task, a subsequent call to `task_done()` tells the queue that the processing on the task is complete.
If a [`join()`](https://docs.python.org/3/library/queue.html#queue.Queue.join "queue.Queue.join") is currently blocking, it will resume when all items have been processed (meaning that a `task_done()` call was received for every item that had been [`put()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.put "multiprocessing.Queue.put") into the queue).
Raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if called more times than there were items placed in the queue.

join()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.JoinableQueue.join "Link to this definition")

Block until all items in the queue have been gotten and processed.
The count of unfinished tasks goes up whenever an item is added to the queue. The count goes down whenever a consumer calls [`task_done()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.JoinableQueue.task_done "multiprocessing.JoinableQueue.task_done") to indicate that the item was retrieved and all work on it is complete. When the count of unfinished tasks drops to zero, [`join()`](https://docs.python.org/3/library/queue.html#queue.Queue.join "queue.Queue.join") unblocks.
### Miscellaneous[¶](https://docs.python.org/3/library/multiprocessing.html#miscellaneous "Link to this heading")

multiprocessing.active_children()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.active_children "Link to this definition")

Return list of all live children of the current process.
Calling this has the side effect of “joining” any processes which have already finished.

multiprocessing.cpu_count()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.cpu_count "Link to this definition")

Return the number of CPUs in the system.
This number is not equivalent to the number of CPUs the current process can use. The number of usable CPUs can be obtained with [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count") (or `len(os.sched_getaffinity(0))`).
When the number of CPUs cannot be determined a [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") is raised.
See also
[`os.cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count") [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count")
Changed in version 3.13: The return value can also be overridden using the [`-X cpu_count`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) flag or [`PYTHON_CPU_COUNT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CPU_COUNT) as this is merely a wrapper around the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") cpu count APIs.

multiprocessing.current_process()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.current_process "Link to this definition")

Return the [`Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process") object corresponding to the current process.
An analogue of [`threading.current_thread()`](https://docs.python.org/3/library/threading.html#threading.current_thread "threading.current_thread").

multiprocessing.parent_process()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.parent_process "Link to this definition")

Return the [`Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process") object corresponding to the parent process of the [`current_process()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.current_process "multiprocessing.current_process"). For the main process, `parent_process` will be `None`.
Added in version 3.8.

multiprocessing.freeze_support()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.freeze_support "Link to this definition")

Add support for when a program which uses `multiprocessing` has been frozen to produce an executable. (Has been tested with **py2exe** , **PyInstaller** and **cx_Freeze**.)
One needs to call this function straight after the `if __name__ == '__main__'` line of the main module. For example:
Copy```
from multiprocessing import Process, freeze_support

def f():
    print('hello world!')

if __name__ == '__main__':
    freeze_support()
    Process(target=f).start()

```

If the `freeze_support()` line is omitted then trying to run the frozen executable will raise [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError").
Calling `freeze_support()` has no effect when the start method is not _spawn_. In addition, if the module is being run normally by the Python interpreter (the program has not been frozen), then `freeze_support()` has no effect.

multiprocessing.get_all_start_methods()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.get_all_start_methods "Link to this definition")

Returns a list of the supported start methods, the first of which is the default. The possible start methods are `'fork'`, `'spawn'` and `'forkserver'`. Not all platforms support all methods. See [Contexts and start methods](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-start-methods).
Added in version 3.4.

multiprocessing.get_context(_method =None_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.get_context "Link to this definition")

Return a context object which has the same attributes as the `multiprocessing` module.
If _method_ is `None` then the default context is returned. Note that if the global start method has not been set, this will set it to the system default See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details. Otherwise _method_ should be `'fork'`, `'spawn'`, `'forkserver'`. [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the specified start method is not available. See [Contexts and start methods](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-start-methods).
Added in version 3.4.

multiprocessing.get_start_method(_allow_none =False_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.get_start_method "Link to this definition")

Return the name of start method used for starting processes.
If the global start method is not set and _allow_none_ is `False`, the global start method is set to the default, and its name is returned. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.
The return value can be `'fork'`, `'spawn'`, `'forkserver'` or `None`. See [Contexts and start methods](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-start-methods).
Added in version 3.4.
Changed in version 3.8: On macOS, the _spawn_ start method is now the default. The _fork_ start method should be considered unsafe as it can lead to crashes of the subprocess. See [bpo-33725](https://bugs.python.org/issue?@action=redirect&bpo=33725).

multiprocessing.set_executable(_executable_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_executable "Link to this definition")

Set the path of the Python interpreter to use when starting a child process. (By default [`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable") is used). Embedders will probably need to do something like
Copy```
set_executable(os.path.join(sys.exec_prefix, 'pythonw.exe'))

```

before they can create child processes.
Changed in version 3.4: Now supported on POSIX when the `'spawn'` start method is used.
Changed in version 3.11: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

multiprocessing.set_forkserver_preload(_module_names_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_forkserver_preload "Link to this definition")

Set a list of module names for the forkserver main process to attempt to import so that their already imported state is inherited by forked processes. Any [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") when doing so is silently ignored. This can be used as a performance enhancement to avoid repeated work in every process.
For this to work, it must be called before the forkserver process has been launched (before creating a `Pool` or starting a [`Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process")).
Only meaningful when using the `'forkserver'` start method. See [Contexts and start methods](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-start-methods).
Added in version 3.4.

multiprocessing.set_start_method(_method_ , _force =False_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_start_method "Link to this definition")

Set the method which should be used to start child processes. The _method_ argument can be `'fork'`, `'spawn'` or `'forkserver'`. Raises [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") if the start method has already been set and _force_ is not `True`. If _method_ is `None` and _force_ is `True` then the start method is set to `None`. If _method_ is `None` and _force_ is `False` then the context is set to the default context.
Note that this should be called at most once, and it should be protected inside the `if __name__ == '__main__'` clause of the main module.
See [Contexts and start methods](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-start-methods).
Added in version 3.4.
Note
`multiprocessing` contains no analogues of [`threading.active_count()`](https://docs.python.org/3/library/threading.html#threading.active_count "threading.active_count"), [`threading.enumerate()`](https://docs.python.org/3/library/threading.html#threading.enumerate "threading.enumerate"), [`threading.settrace()`](https://docs.python.org/3/library/threading.html#threading.settrace "threading.settrace"), [`threading.setprofile()`](https://docs.python.org/3/library/threading.html#threading.setprofile "threading.setprofile"), [`threading.Timer`](https://docs.python.org/3/library/threading.html#threading.Timer "threading.Timer"), or [`threading.local`](https://docs.python.org/3/library/threading.html#threading.local "threading.local").
### Connection Objects[¶](https://docs.python.org/3/library/multiprocessing.html#connection-objects "Link to this heading")
Connection objects allow the sending and receiving of picklable objects or strings. They can be thought of as message oriented connected sockets.
Connection objects are usually created using [`Pipe`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Pipe "multiprocessing.Pipe") – see also [Listeners and Clients](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-listeners-clients).

_class_ multiprocessing.connection.Connection[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection "Link to this definition")


send(_obj_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.send "Link to this definition")

Send an object to the other end of the connection which should be read using [`recv()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.recv "multiprocessing.connection.Connection.recv").
The object must be picklable. Very large pickles (approximately 32 MiB+, though it depends on the OS) may raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") exception.

recv()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.recv "Link to this definition")

Return an object sent from the other end of the connection using [`send()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.send "multiprocessing.connection.Connection.send"). Blocks until there is something to receive. Raises [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError "EOFError") if there is nothing left to receive and the other end was closed.

fileno()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.fileno "Link to this definition")

Return the file descriptor or handle used by the connection.

close()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.close "Link to this definition")

Close the connection.
This is called automatically when the connection is garbage collected.

poll([_timeout_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.poll "Link to this definition")

Return whether there is any data available to be read.
If _timeout_ is not specified then it will return immediately. If _timeout_ is a number then this specifies the maximum time in seconds to block. If _timeout_ is `None` then an infinite timeout is used.
Note that multiple connection objects may be polled at once by using [`multiprocessing.connection.wait()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.wait "multiprocessing.connection.wait").

send_bytes(_buffer_[, _offset_[, _size_]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.send_bytes "Link to this definition")

Send byte data from a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) as a complete message.
If _offset_ is given then data is read from that position in _buffer_. If _size_ is given then that many bytes will be read from buffer. Very large buffers (approximately 32 MiB+, though it depends on the OS) may raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") exception

recv_bytes([_maxlength_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.recv_bytes "Link to this definition")

Return a complete message of byte data sent from the other end of the connection as a string. Blocks until there is something to receive. Raises [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError "EOFError") if there is nothing left to receive and the other end has closed.
If _maxlength_ is specified and the message is longer than _maxlength_ then [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised and the connection will no longer be readable.
Changed in version 3.3: This function used to raise [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError"), which is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

recv_bytes_into(_buffer_[, _offset_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.recv_bytes_into "Link to this definition")

Read into _buffer_ a complete message of byte data sent from the other end of the connection and return the number of bytes in the message. Blocks until there is something to receive. Raises [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError "EOFError") if there is nothing left to receive and the other end was closed.
_buffer_ must be a writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object). If _offset_ is given then the message will be written into the buffer from that position. Offset must be a non-negative integer less than the length of _buffer_ (in bytes).
If the buffer is too short then a `BufferTooShort` exception is raised and the complete message is available as `e.args[0]` where `e` is the exception instance.
Changed in version 3.3: Connection objects themselves can now be transferred between processes using [`Connection.send()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.send "multiprocessing.connection.Connection.send") and [`Connection.recv()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.recv "multiprocessing.connection.Connection.recv").
Connection objects also now support the context management protocol – see [Context Manager Types](https://docs.python.org/3/library/stdtypes.html#typecontextmanager). [`__enter__()`](https://docs.python.org/3/library/stdtypes.html#contextmanager.__enter__ "contextmanager.__enter__") returns the connection object, and [`__exit__()`](https://docs.python.org/3/library/stdtypes.html#contextmanager.__exit__ "contextmanager.__exit__") calls [`close()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.close "multiprocessing.connection.Connection.close").
For example:
Copy```
>>> from multiprocessing import Pipe
>>> a, b = Pipe()
>>> a.send([1, 'hello', None])
>>> b.recv()
[1, 'hello', None]
>>> b.send_bytes(b'thank you')
>>> a.recv_bytes()
b'thank you'
>>> import array
>>> arr1 = array.array('i', range(5))
>>> arr2 = array.array('i', [0] * 10)
>>> a.send_bytes(arr1)
>>> count = b.recv_bytes_into(arr2)
>>> assert count == len(arr1) * arr1.itemsize
>>> arr2
array('i', [0, 1, 2, 3, 4, 0, 0, 0, 0, 0])

```

Warning
The [`Connection.recv()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.recv "multiprocessing.connection.Connection.recv") method automatically unpickles the data it receives, which can be a security risk unless you can trust the process which sent the message.
Therefore, unless the connection object was produced using `Pipe()` you should only use the [`recv()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.recv "multiprocessing.connection.Connection.recv") and [`send()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.send "multiprocessing.connection.Connection.send") methods after performing some sort of authentication. See [Authentication keys](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-auth-keys).
Warning
If a process is killed while it is trying to read or write to a pipe then the data in the pipe is likely to become corrupted, because it may become impossible to be sure where the message boundaries lie.
### Synchronization primitives[¶](https://docs.python.org/3/library/multiprocessing.html#synchronization-primitives "Link to this heading")
Generally synchronization primitives are not as necessary in a multiprocess program as they are in a multithreaded program. See the documentation for [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.") module.
Note that one can also create synchronization primitives by using a manager object – see [Managers](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-managers).

_class_ multiprocessing.Barrier(_parties_[, _action_[, _timeout_]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Barrier "Link to this definition")

A barrier object: a clone of [`threading.Barrier`](https://docs.python.org/3/library/threading.html#threading.Barrier "threading.Barrier").
Instantiating this class may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.
Added in version 3.3.

_class_ multiprocessing.BoundedSemaphore([_value_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.BoundedSemaphore "Link to this definition")

A bounded semaphore object: a close analog of [`threading.BoundedSemaphore`](https://docs.python.org/3/library/threading.html#threading.BoundedSemaphore "threading.BoundedSemaphore").
Instantiating this class may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.
A solitary difference from its close analog exists: its `acquire` method’s first argument is named _block_ , as is consistent with [`Lock.acquire()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock.acquire "multiprocessing.Lock.acquire").

locked()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.BoundedSemaphore.locked "Link to this definition")

Return a boolean indicating whether this object is locked right now.
Added in version 3.14.
Note
On macOS, this is indistinguishable from [`Semaphore`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Semaphore "multiprocessing.Semaphore") because `sem_getvalue()` is not implemented on that platform.

_class_ multiprocessing.Condition([_lock_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Condition "Link to this definition")

A condition variable: an alias for [`threading.Condition`](https://docs.python.org/3/library/threading.html#threading.Condition "threading.Condition").
If _lock_ is specified then it should be a [`Lock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock "multiprocessing.Lock") or [`RLock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.RLock "multiprocessing.RLock") object from `multiprocessing`.
Instantiating this class may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.
Changed in version 3.3: The [`wait_for()`](https://docs.python.org/3/library/threading.html#threading.Condition.wait_for "threading.Condition.wait_for") method was added.

_class_ multiprocessing.Event[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Event "Link to this definition")

A clone of [`threading.Event`](https://docs.python.org/3/library/threading.html#threading.Event "threading.Event").
Instantiating this class may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.

_class_ multiprocessing.Lock[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock "Link to this definition")

A non-recursive lock object: a close analog of [`threading.Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock"). Once a process or thread has acquired a lock, subsequent attempts to acquire it from any process or thread will block until it is released; any process or thread may release it. The concepts and behaviors of `threading.Lock` as it applies to threads are replicated here in [`multiprocessing.Lock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock "multiprocessing.Lock") as it applies to either processes or threads, except as noted.
Note that `Lock` is actually a factory function which returns an instance of `multiprocessing.synchronize.Lock` initialized with a default context.
Instantiating this class may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.
`Lock` supports the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) protocol and thus may be used in [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statements.

acquire(_block =True_, _timeout =None_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock.acquire "Link to this definition")

Acquire a lock, blocking or non-blocking.
With the _block_ argument set to `True` (the default), the method call will block until the lock is in an unlocked state, then set it to locked and return `True`. Note that the name of this first argument differs from that in [`threading.Lock.acquire()`](https://docs.python.org/3/library/threading.html#threading.Lock.acquire "threading.Lock.acquire").
With the _block_ argument set to `False`, the method call does not block. If the lock is currently in a locked state, return `False`; otherwise set the lock to a locked state and return `True`.
When invoked with a positive, floating-point value for _timeout_ , block for at most the number of seconds specified by _timeout_ as long as the lock can not be acquired. Invocations with a negative value for _timeout_ are equivalent to a _timeout_ of zero. Invocations with a _timeout_ value of `None` (the default) set the timeout period to infinite. Note that the treatment of negative or `None` values for _timeout_ differs from the implemented behavior in [`threading.Lock.acquire()`](https://docs.python.org/3/library/threading.html#threading.Lock.acquire "threading.Lock.acquire"). The _timeout_ argument has no practical implications if the _block_ argument is set to `False` and is thus ignored. Returns `True` if the lock has been acquired or `False` if the timeout period has elapsed.

release()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock.release "Link to this definition")

Release a lock. This can be called from any process or thread, not only the process or thread which originally acquired the lock.
Behavior is the same as in [`threading.Lock.release()`](https://docs.python.org/3/library/threading.html#threading.Lock.release "threading.Lock.release") except that when invoked on an unlocked lock, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.

locked()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock.locked "Link to this definition")

Return a boolean indicating whether this object is locked right now.
Added in version 3.14.

_class_ multiprocessing.RLock[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.RLock "Link to this definition")

A recursive lock object: a close analog of [`threading.RLock`](https://docs.python.org/3/library/threading.html#threading.RLock "threading.RLock"). A recursive lock must be released by the process or thread that acquired it. Once a process or thread has acquired a recursive lock, the same process or thread may acquire it again without blocking; that process or thread must release it once for each time it has been acquired.
Note that `RLock` is actually a factory function which returns an instance of `multiprocessing.synchronize.RLock` initialized with a default context.
Instantiating this class may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.
`RLock` supports the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) protocol and thus may be used in [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statements.

acquire(_block =True_, _timeout =None_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.RLock.acquire "Link to this definition")

Acquire a lock, blocking or non-blocking.
When invoked with the _block_ argument set to `True`, block until the lock is in an unlocked state (not owned by any process or thread) unless the lock is already owned by the current process or thread. The current process or thread then takes ownership of the lock (if it does not already have ownership) and the recursion level inside the lock increments by one, resulting in a return value of `True`. Note that there are several differences in this first argument’s behavior compared to the implementation of [`threading.RLock.acquire()`](https://docs.python.org/3/library/threading.html#threading.RLock.acquire "threading.RLock.acquire"), starting with the name of the argument itself.
When invoked with the _block_ argument set to `False`, do not block. If the lock has already been acquired (and thus is owned) by another process or thread, the current process or thread does not take ownership and the recursion level within the lock is not changed, resulting in a return value of `False`. If the lock is in an unlocked state, the current process or thread takes ownership and the recursion level is incremented, resulting in a return value of `True`.
Use and behaviors of the _timeout_ argument are the same as in [`Lock.acquire()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock.acquire "multiprocessing.Lock.acquire"). Note that some of these behaviors of _timeout_ differ from the implemented behaviors in [`threading.RLock.acquire()`](https://docs.python.org/3/library/threading.html#threading.RLock.acquire "threading.RLock.acquire").

release()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.RLock.release "Link to this definition")

Release a lock, decrementing the recursion level. If after the decrement the recursion level is zero, reset the lock to unlocked (not owned by any process or thread) and if any other processes or threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed. If after the decrement the recursion level is still nonzero, the lock remains locked and owned by the calling process or thread.
Only call this method when the calling process or thread owns the lock. An [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") is raised if this method is called by a process or thread other than the owner or if the lock is in an unlocked (unowned) state. Note that the type of exception raised in this situation differs from the implemented behavior in [`threading.RLock.release()`](https://docs.python.org/3/library/threading.html#threading.RLock.release "threading.RLock.release").

locked()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.RLock.locked "Link to this definition")

Return a boolean indicating whether this object is locked right now.
Added in version 3.14.

_class_ multiprocessing.Semaphore([_value_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Semaphore "Link to this definition")

A semaphore object: a close analog of [`threading.Semaphore`](https://docs.python.org/3/library/threading.html#threading.Semaphore "threading.Semaphore").
Instantiating this class may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.
A solitary difference from its close analog exists: its `acquire` method’s first argument is named _block_ , as is consistent with [`Lock.acquire()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock.acquire "multiprocessing.Lock.acquire").

get_value()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Semaphore.get_value "Link to this definition")

Return the current value of semaphore.
Note that this may raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") on platforms like macOS where `sem_getvalue()` is not implemented.

locked()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Semaphore.locked "Link to this definition")

Return a boolean indicating whether this object is locked right now.
Added in version 3.14.
Note
On macOS, `sem_timedwait` is unsupported, so calling `acquire()` with a timeout will emulate that function’s behavior using a sleeping loop.
Note
Some of this package’s functionality requires a functioning shared semaphore implementation on the host operating system. Without one, the `multiprocessing.synchronize` module will be disabled, and attempts to import it will result in an [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError"). See [bpo-3770](https://bugs.python.org/issue?@action=redirect&bpo=3770) for additional information.
### Shared [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.") Objects[¶](https://docs.python.org/3/library/multiprocessing.html#shared-ctypes-objects "Link to this heading")
It is possible to create shared objects using shared memory which can be inherited by child processes.

multiprocessing.Value(_typecode_or_type_ , _* args_, _lock =True_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Value "Link to this definition")

Return a [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.") object allocated from shared memory. By default the return value is actually a synchronized wrapper for the object. The object itself can be accessed via the _value_ attribute of a [`Value`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Value "multiprocessing.Value").
_typecode_or_type_ determines the type of the returned object: it is either a ctypes type or a one character typecode of the kind used by the [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.") module. _*args_ is passed on to the constructor for the type.
If _lock_ is `True` (the default) then a new recursive lock object is created to synchronize access to the value. If _lock_ is a [`Lock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock "multiprocessing.Lock") or [`RLock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.RLock "multiprocessing.RLock") object then that will be used to synchronize access to the value. If _lock_ is `False` then access to the returned object will not be automatically protected by a lock, so it will not necessarily be “process-safe”.
Operations like `+=` which involve a read and write are not atomic. So if, for instance, you want to atomically increment a shared value it is insufficient to just do
Copy```
counter.value += 1

```

Assuming the associated lock is recursive (which it is by default) you can instead do
Copy```
with counter.get_lock():
    counter.value += 1

```

Note that _lock_ is a keyword-only argument.

multiprocessing.Array(_typecode_or_type_ , _size_or_initializer_ , _*_ , _lock =True_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Array "Link to this definition")

Return a ctypes array allocated from shared memory. By default the return value is actually a synchronized wrapper for the array.
_typecode_or_type_ determines the type of the elements of the returned array: it is either a [ctypes type](https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types) or a one character typecode of the kind used by the [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.") module with the exception of `'w'`, which is not supported. In addition, the `'c'` typecode is an alias for [`ctypes.c_char`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char "ctypes.c_char"). If _size_or_initializer_ is an integer, then it determines the length of the array, and the array will be initially zeroed. Otherwise, _size_or_initializer_ is a sequence which is used to initialize the array and whose length determines the length of the array.
If _lock_ is `True` (the default) then a new lock object is created to synchronize access to the value. If _lock_ is a [`Lock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock "multiprocessing.Lock") or [`RLock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.RLock "multiprocessing.RLock") object then that will be used to synchronize access to the value. If _lock_ is `False` then access to the returned object will not be automatically protected by a lock, so it will not necessarily be “process-safe”.
Note that _lock_ is a keyword only argument.
Note that an array of [`ctypes.c_char`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char "ctypes.c_char") has _value_ and _raw_ attributes which allow one to use it to store and retrieve strings.
#### The `multiprocessing.sharedctypes` module[¶](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.sharedctypes "Link to this heading")
The `multiprocessing.sharedctypes` module provides functions for allocating [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.") objects from shared memory which can be inherited by child processes.
Note
Although it is possible to store a pointer in shared memory remember that this will refer to a location in the address space of a specific process. However, the pointer is quite likely to be invalid in the context of a second process and trying to dereference the pointer from the second process may cause a crash.

multiprocessing.sharedctypes.RawArray(_typecode_or_type_ , _size_or_initializer_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.sharedctypes.RawArray "Link to this definition")

Return a ctypes array allocated from shared memory.
_typecode_or_type_ determines the type of the elements of the returned array: it is either a ctypes type or a one character typecode of the kind used by the [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.") module. If _size_or_initializer_ is an integer then it determines the length of the array, and the array will be initially zeroed. Otherwise _size_or_initializer_ is a sequence which is used to initialize the array and whose length determines the length of the array.
Note that setting and getting an element is potentially non-atomic – use [`Array()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.sharedctypes.Array "multiprocessing.sharedctypes.Array") instead to make sure that access is automatically synchronized using a lock.

multiprocessing.sharedctypes.RawValue(_typecode_or_type_ , _* args_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.sharedctypes.RawValue "Link to this definition")

Return a ctypes object allocated from shared memory.
_typecode_or_type_ determines the type of the returned object: it is either a ctypes type or a one character typecode of the kind used by the [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.") module. _*args_ is passed on to the constructor for the type.
Note that setting and getting the value is potentially non-atomic – use [`Value()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.sharedctypes.Value "multiprocessing.sharedctypes.Value") instead to make sure that access is automatically synchronized using a lock.
Note that an array of [`ctypes.c_char`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char "ctypes.c_char") has `value` and `raw` attributes which allow one to use it to store and retrieve strings – see documentation for [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.").

multiprocessing.sharedctypes.Array(_typecode_or_type_ , _size_or_initializer_ , _*_ , _lock =True_, _ctx =None_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.sharedctypes.Array "Link to this definition")

The same as [`RawArray()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.sharedctypes.RawArray "multiprocessing.sharedctypes.RawArray") except that depending on the value of _lock_ a process-safe synchronization wrapper may be returned instead of a raw ctypes array.
If _lock_ is `True` (the default) then a new lock object is created to synchronize access to the value. If _lock_ is a [`Lock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock "multiprocessing.Lock") or [`RLock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.RLock "multiprocessing.RLock") object then that will be used to synchronize access to the value. If _lock_ is `False` then access to the returned object will not be automatically protected by a lock, so it will not necessarily be “process-safe”.
_ctx_ is a context object, or `None` (use the current context). If `None`, calling this may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.
Note that _lock_ and _ctx_ are keyword-only parameters.

multiprocessing.sharedctypes.Value(_typecode_or_type_ , _* args_, _lock =True_, _ctx =None_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.sharedctypes.Value "Link to this definition")

The same as [`RawValue()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.sharedctypes.RawValue "multiprocessing.sharedctypes.RawValue") except that depending on the value of _lock_ a process-safe synchronization wrapper may be returned instead of a raw ctypes object.
If _lock_ is `True` (the default) then a new lock object is created to synchronize access to the value. If _lock_ is a [`Lock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Lock "multiprocessing.Lock") or [`RLock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.RLock "multiprocessing.RLock") object then that will be used to synchronize access to the value. If _lock_ is `False` then access to the returned object will not be automatically protected by a lock, so it will not necessarily be “process-safe”.
_ctx_ is a context object, or `None` (use the current context). If `None`, calling this may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.
Note that _lock_ and _ctx_ are keyword-only parameters.

multiprocessing.sharedctypes.copy(_obj_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.sharedctypes.copy "Link to this definition")

Return a ctypes object allocated from shared memory which is a copy of the ctypes object _obj_.

multiprocessing.sharedctypes.synchronized(_obj_ , _lock =None_, _ctx =None_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.sharedctypes.synchronized "Link to this definition")

Return a process-safe wrapper object for a ctypes object which uses _lock_ to synchronize access. If _lock_ is `None` (the default) then a [`multiprocessing.RLock`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.RLock "multiprocessing.RLock") object is created automatically.
_ctx_ is a context object, or `None` (use the current context). If `None`, calling this may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.
A synchronized wrapper will have two methods in addition to those of the object it wraps: `get_obj()` returns the wrapped object and `get_lock()` returns the lock object used for synchronization.
Note that accessing the ctypes object through the wrapper can be a lot slower than accessing the raw ctypes object.
Changed in version 3.5: Synchronized objects support the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) protocol.
The table below compares the syntax for creating shared ctypes objects from shared memory with the normal ctypes syntax. (In the table `MyStruct` is some subclass of [`ctypes.Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "ctypes.Structure").)
ctypes | sharedctypes using type | sharedctypes using typecode
---|---|---
c_double(2.4) | RawValue(c_double, 2.4) | RawValue(‘d’, 2.4)
MyStruct(4, 6) | RawValue(MyStruct, 4, 6) |
(c_short * 7)() | RawArray(c_short, 7) | RawArray(‘h’, 7)
(c_int * 3)(9, 2, 8) | RawArray(c_int, (9, 2, 8)) | RawArray(‘i’, (9, 2, 8))
Below is an example where a number of ctypes objects are modified by a child process:
Copy```
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double

class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]

def modify(n, x, s, A):
    n.value **= 2
    x.value **= 2
    s.value = s.value.upper()
    for a in A:
        a.x **= 2
        a.y **= 2

if __name__ == '__main__':
    lock = Lock()

    n = Value('i', 7)
    x = Value(c_double, 1.0/3.0, lock=False)
    s = Array('c', b'hello world', lock=lock)
    A = Array(Point, [(1.875,-6.25), (-5.75,2.0), (2.375,9.5)], lock=lock)

    p = Process(target=modify, args=(n, x, s, A))
    p.start()
    p.join()

    print(n.value)
    print(x.value)
    print(s.value)
    print([(a.x, a.y) for a in A])

```

The results printed are
```
49
0.1111111111111111
HELLO WORLD
[(3.515625, 39.0625), (33.0625, 4.0), (5.640625, 90.25)]

```

### Managers[¶](https://docs.python.org/3/library/multiprocessing.html#managers "Link to this heading")
Managers provide a way to create data which can be shared between different processes, including sharing over a network between processes running on different machines. A manager object controls a server process which manages _shared objects_. Other processes can access the shared objects by using proxies.

multiprocessing.Manager()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Manager "Link to this definition")

Returns a started [`SyncManager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager "multiprocessing.managers.SyncManager") object which can be used for sharing objects between processes. The returned manager object corresponds to a spawned child process and has methods which will create shared objects and return corresponding proxies.
Manager processes will be shutdown as soon as they are garbage collected or their parent process exits. The manager classes are defined in the [`multiprocessing.managers`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.managers "multiprocessing.managers: Share data between process with shared objects.") module:

_class_ multiprocessing.managers.BaseManager(_address =None_, _authkey =None_, _serializer ='pickle'_, _ctx =None_, _*_ , _shutdown_timeout =1.0_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager "Link to this definition")

Create a BaseManager object.
Once created one should call [`start()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.start "multiprocessing.managers.BaseManager.start") or `get_server().serve_forever()` to ensure that the manager object refers to a started manager process.
_address_ is the address on which the manager process listens for new connections. If _address_ is `None` then an arbitrary one is chosen.
_authkey_ is the authentication key which will be used to check the validity of incoming connections to the server process. If _authkey_ is `None` then `current_process().authkey` is used. Otherwise _authkey_ is used and it must be a byte string.
_serializer_ must be `'pickle'` (use [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") serialization) or `'xmlrpclib'` (use [`xmlrpc.client`](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client "xmlrpc.client: XML-RPC client access.") serialization).
_ctx_ is a context object, or `None` (use the current context). If `None`, calling this may set the global start method. See [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method) for more details.
_shutdown_timeout_ is a timeout in seconds used to wait until the process used by the manager completes in the [`shutdown()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.shutdown "multiprocessing.managers.BaseManager.shutdown") method. If the shutdown times out, the process is terminated. If terminating the process also times out, the process is killed.
Changed in version 3.11: Added the _shutdown_timeout_ parameter.

start([_initializer_[, _initargs_]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.start "Link to this definition")

Start a subprocess to start the manager. If _initializer_ is not `None` then the subprocess will call `initializer(*initargs)` when it starts.

get_server()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.get_server "Link to this definition")

Returns a `Server` object which represents the actual server under the control of the Manager. The `Server` object supports the `serve_forever()` method:
Copy```
>>> from multiprocessing.managers import BaseManager
>>> manager = BaseManager(address=('', 50000), authkey=b'abc')
>>> server = manager.get_server()
>>> server.serve_forever()

```

`Server` additionally has an [`address`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.address "multiprocessing.managers.BaseManager.address") attribute.

connect()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.connect "Link to this definition")

Connect a local manager object to a remote manager process:
Copy```
>>> from multiprocessing.managers import BaseManager
>>> m = BaseManager(address=('127.0.0.1', 50000), authkey=b'abc')
>>> m.connect()

```


shutdown()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.shutdown "Link to this definition")

Stop the process used by the manager. This is only available if [`start()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.start "multiprocessing.managers.BaseManager.start") has been used to start the server process.
This can be called multiple times.

register(_typeid_[, _callable_[, _proxytype_[, _exposed_[, _method_to_typeid_[, _create_method_]]]]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.register "Link to this definition")

A classmethod which can be used for registering a type or callable with the manager class.
_typeid_ is a “type identifier” which is used to identify a particular type of shared object. This must be a string.
_callable_ is a callable used for creating objects for this type identifier. If a manager instance will be connected to the server using the [`connect()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.connect "multiprocessing.managers.BaseManager.connect") method, or if the _create_method_ argument is `False` then this can be left as `None`.
_proxytype_ is a subclass of [`BaseProxy`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseProxy "multiprocessing.managers.BaseProxy") which is used to create proxies for shared objects with this _typeid_. If `None` then a proxy class is created automatically.
_exposed_ is used to specify a sequence of method names which proxies for this typeid should be allowed to access using [`BaseProxy._callmethod()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseProxy._callmethod "multiprocessing.managers.BaseProxy._callmethod"). (If _exposed_ is `None` then `proxytype._exposed_` is used instead if it exists.) In the case where no exposed list is specified, all “public methods” of the shared object will be accessible. (Here a “public method” means any attribute which has a [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__") method and whose name does not begin with `'_'`.)
_method_to_typeid_ is a mapping used to specify the return type of those exposed methods which should return a proxy. It maps method names to typeid strings. (If _method_to_typeid_ is `None` then `proxytype._method_to_typeid_` is used instead if it exists.) If a method’s name is not a key of this mapping or if the mapping is `None` then the object returned by the method will be copied by value.
_create_method_ determines whether a method should be created with name _typeid_ which can be used to tell the server process to create a new shared object and return a proxy for it. By default it is `True`.
`BaseManager` instances also have one read-only property:

address[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.address "Link to this definition")

The address used by the manager.
Changed in version 3.3: Manager objects support the context management protocol – see [Context Manager Types](https://docs.python.org/3/library/stdtypes.html#typecontextmanager). [`__enter__()`](https://docs.python.org/3/library/stdtypes.html#contextmanager.__enter__ "contextmanager.__enter__") starts the server process (if it has not already started) and then returns the manager object. [`__exit__()`](https://docs.python.org/3/library/stdtypes.html#contextmanager.__exit__ "contextmanager.__exit__") calls [`shutdown()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.shutdown "multiprocessing.managers.BaseManager.shutdown").
In previous versions [`__enter__()`](https://docs.python.org/3/library/stdtypes.html#contextmanager.__enter__ "contextmanager.__enter__") did not start the manager’s server process if it was not already started.

_class_ multiprocessing.managers.SyncManager[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager "Link to this definition")

A subclass of [`BaseManager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager "multiprocessing.managers.BaseManager") which can be used for the synchronization of processes. Objects of this type are returned by [`multiprocessing.Manager()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Manager "multiprocessing.Manager").
Its methods create and return [Proxy Objects](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-proxy-objects) for a number of commonly used data types to be synchronized across processes. This notably includes shared lists and dictionaries.

Barrier(_parties_[, _action_[, _timeout_]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.Barrier "Link to this definition")

Create a shared [`threading.Barrier`](https://docs.python.org/3/library/threading.html#threading.Barrier "threading.Barrier") object and return a proxy for it.
Added in version 3.3.

BoundedSemaphore([_value_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.BoundedSemaphore "Link to this definition")

Create a shared [`threading.BoundedSemaphore`](https://docs.python.org/3/library/threading.html#threading.BoundedSemaphore "threading.BoundedSemaphore") object and return a proxy for it.

Condition([_lock_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.Condition "Link to this definition")

Create a shared [`threading.Condition`](https://docs.python.org/3/library/threading.html#threading.Condition "threading.Condition") object and return a proxy for it.
If _lock_ is supplied then it should be a proxy for a [`threading.Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock") or [`threading.RLock`](https://docs.python.org/3/library/threading.html#threading.RLock "threading.RLock") object.
Changed in version 3.3: The [`wait_for()`](https://docs.python.org/3/library/threading.html#threading.Condition.wait_for "threading.Condition.wait_for") method was added.

Event()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.Event "Link to this definition")

Create a shared [`threading.Event`](https://docs.python.org/3/library/threading.html#threading.Event "threading.Event") object and return a proxy for it.

Lock()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.Lock "Link to this definition")

Create a shared [`threading.Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock") object and return a proxy for it.

Namespace()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.Namespace "Link to this definition")

Create a shared [`Namespace`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.Namespace "multiprocessing.managers.Namespace") object and return a proxy for it.

Queue([_maxsize_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.Queue "Link to this definition")

Create a shared [`queue.Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") object and return a proxy for it.

RLock()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.RLock "Link to this definition")

Create a shared [`threading.RLock`](https://docs.python.org/3/library/threading.html#threading.RLock "threading.RLock") object and return a proxy for it.

Semaphore([_value_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.Semaphore "Link to this definition")

Create a shared [`threading.Semaphore`](https://docs.python.org/3/library/threading.html#threading.Semaphore "threading.Semaphore") object and return a proxy for it.

Array(_typecode_ , _sequence_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.Array "Link to this definition")

Create an array and return a proxy for it.

Value(_typecode_ , _value_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.Value "Link to this definition")

Create an object with a writable `value` attribute and return a proxy for it.

dict()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.dict "Link to this definition")


dict(_mapping_)


dict(_sequence_)

Create a shared [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") object and return a proxy for it.

list()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.list "Link to this definition")


list(_sequence_)

Create a shared [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") object and return a proxy for it.

set()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager.set "Link to this definition")


set(_sequence_)


set(_mapping_)

Create a shared [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") object and return a proxy for it.
Added in version 3.14: [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") support was added.
Changed in version 3.6: Shared objects are capable of being nested. For example, a shared container object such as a shared list can contain other shared objects which will all be managed and synchronized by the `SyncManager`.

_class_ multiprocessing.managers.Namespace[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.Namespace "Link to this definition")

A type that can register with [`SyncManager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager "multiprocessing.managers.SyncManager").
A namespace object has no public methods, but does have writable attributes. Its representation shows the values of its attributes.
However, when using a proxy for a namespace object, an attribute beginning with `'_'` will be an attribute of the proxy and not an attribute of the referent:
Copy```
>>> mp_context = multiprocessing.get_context('spawn')
>>> manager = mp_context.Manager()
>>> Global = manager.Namespace()
>>> Global.x = 10
>>> Global.y = 'hello'
>>> Global._z = 12.3    # this is an attribute of the proxy
>>> print(Global)
Namespace(x=10, y='hello')

```

#### Customized managers[¶](https://docs.python.org/3/library/multiprocessing.html#customized-managers "Link to this heading")
To create one’s own manager, one creates a subclass of [`BaseManager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager "multiprocessing.managers.BaseManager") and uses the [`register()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.register "multiprocessing.managers.BaseManager.register") classmethod to register new types or callables with the manager class. For example:
Copy```
from multiprocessing.managers import BaseManager

class MathsClass:
    def add(self, x, y):
        return x + y
    def mul(self, x, y):
        return x * y

class MyManager(BaseManager):
    pass

MyManager.register('Maths', MathsClass)

if __name__ == '__main__':
    with MyManager() as manager:
        maths = manager.Maths()
        print(maths.add(4, 3))         # prints 7
        print(maths.mul(7, 8))         # prints 56

```

#### Using a remote manager[¶](https://docs.python.org/3/library/multiprocessing.html#using-a-remote-manager "Link to this heading")
It is possible to run a manager server on one machine and have clients use it from other machines (assuming that the firewalls involved allow it).
Running the following commands creates a server for a single shared queue which remote clients can access:
Copy```
>>> from multiprocessing.managers import BaseManager
>>> from queue import Queue
>>> queue = Queue()
>>> class QueueManager(BaseManager): pass
>>> QueueManager.register('get_queue', callable=lambda:queue)
>>> m = QueueManager(address=('', 50000), authkey=b'abracadabra')
>>> s = m.get_server()
>>> s.serve_forever()

```

One client can access the server as follows:
Copy```
>>> from multiprocessing.managers import BaseManager
>>> class QueueManager(BaseManager): pass
>>> QueueManager.register('get_queue')
>>> m = QueueManager(address=('foo.bar.org', 50000), authkey=b'abracadabra')
>>> m.connect()
>>> queue = m.get_queue()
>>> queue.put('hello')

```

Another client can also use it:
Copy```
>>> from multiprocessing.managers import BaseManager
>>> class QueueManager(BaseManager): pass
>>> QueueManager.register('get_queue')
>>> m = QueueManager(address=('foo.bar.org', 50000), authkey=b'abracadabra')
>>> m.connect()
>>> queue = m.get_queue()
>>> queue.get()
'hello'

```

Local processes can also access that queue, using the code from above on the client to access it remotely:
Copy```
>>> from multiprocessing import Process, Queue
>>> from multiprocessing.managers import BaseManager
>>> class Worker(Process):
...     def __init__(self, q):
...         self.q = q
...         super().__init__()
...     def run(self):
...         self.q.put('local hello')
...
>>> queue = Queue()
>>> w = Worker(queue)
>>> w.start()
>>> class QueueManager(BaseManager): pass
...
>>> QueueManager.register('get_queue', callable=lambda: queue)
>>> m = QueueManager(address=('', 50000), authkey=b'abracadabra')
>>> s = m.get_server()
>>> s.serve_forever()

```

### Proxy Objects[¶](https://docs.python.org/3/library/multiprocessing.html#proxy-objects "Link to this heading")
A proxy is an object which _refers_ to a shared object which lives (presumably) in a different process. The shared object is said to be the _referent_ of the proxy. Multiple proxy objects may have the same referent.
A proxy object has methods which invoke corresponding methods of its referent (although not every method of the referent will necessarily be available through the proxy). In this way, a proxy can be used just like its referent can:
Copy```
>>> mp_context = multiprocessing.get_context('spawn')
>>> manager = mp_context.Manager()
>>> l = manager.list([i*i for i in range(10)])
>>> print(l)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> print(repr(l))
<ListProxy object, typeid 'list' at 0x...>
>>> l[4]
16
>>> l[2:5]
[4, 9, 16]

```

Notice that applying [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") to a proxy will return the representation of the referent, whereas applying [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") will return the representation of the proxy.
An important feature of proxy objects is that they are picklable so they can be passed between processes. As such, a referent can contain [Proxy Objects](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-proxy-objects). This permits nesting of these managed lists, dicts, and other multiprocessing-proxy_objects:
Copy```
>>> a = manager.list()
>>> b = manager.list()
>>> a.append(b)         # referent of a now contains referent of b
>>> print(a, b)
[<ListProxy object, typeid 'list' at ...>] []
>>> b.append('hello')
>>> print(a[0], b)
['hello'] ['hello']

```

Similarly, dict and list proxies may be nested inside one another:
Copy```
>>> l_outer = manager.list([ manager.dict() for i in range(2) ])
>>> d_first_inner = l_outer[0]
>>> d_first_inner['a'] = 1
>>> d_first_inner['b'] = 2
>>> l_outer[1]['c'] = 3
>>> l_outer[1]['z'] = 26
>>> print(l_outer[0])
{'a': 1, 'b': 2}
>>> print(l_outer[1])
{'c': 3, 'z': 26}

```

If standard (non-proxy) [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") or [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") objects are contained in a referent, modifications to those mutable values will not be propagated through the manager because the proxy has no way of knowing when the values contained within are modified. However, storing a value in a container proxy (which triggers a `__setitem__` on the proxy object) does propagate through the manager and so to effectively modify such an item, one could re-assign the modified value to the container proxy:
Copy```
# create a list proxy and append a mutable object (a dictionary)
lproxy = manager.list()
lproxy.append({})
# now mutate the dictionary
d = lproxy[0]
d['a'] = 1
d['b'] = 2
# at this point, the changes to d are not yet synced, but by
# updating the dictionary, the proxy is notified of the change
lproxy[0] = d

```

This approach is perhaps less convenient than employing nested [Proxy Objects](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-proxy-objects) for most use cases but also demonstrates a level of control over the synchronization.
Note
The proxy types in `multiprocessing` do nothing to support comparisons by value. So, for instance, we have:
Copy```
>>> manager.list([1,2,3]) == [1,2,3]
False

```

One should just use a copy of the referent instead when making comparisons.

_class_ multiprocessing.managers.BaseProxy[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseProxy "Link to this definition")

Proxy objects are instances of subclasses of `BaseProxy`.

_callmethod(_methodname_[, _args_[, _kwds_]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseProxy._callmethod "Link to this definition")

Call and return the result of a method of the proxy’s referent.
If `proxy` is a proxy whose referent is `obj` then the expression
Copy```
proxy._callmethod(methodname, args, kwds)

```

will evaluate the expression
Copy```
getattr(obj, methodname)(*args, **kwds)

```

in the manager’s process.
The returned value will be a copy of the result of the call or a proxy to a new shared object – see documentation for the _method_to_typeid_ argument of [`BaseManager.register()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.register "multiprocessing.managers.BaseManager.register").
If an exception is raised by the call, then is re-raised by `_callmethod()`. If some other exception is raised in the manager’s process then this is converted into a `RemoteError` exception and is raised by `_callmethod()`.
Note in particular that an exception will be raised if _methodname_ has not been _exposed_.
An example of the usage of `_callmethod()`:
Copy```
>>> l = manager.list(range(10))
>>> l._callmethod('__len__')
10
>>> l._callmethod('__getitem__', (slice(2, 7),)) # equivalent to l[2:7]
[2, 3, 4, 5, 6]
>>> l._callmethod('__getitem__', (20,))          # equivalent to l[20]
Traceback (most recent call last):
...
IndexError: list index out of range

```


_getvalue()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseProxy._getvalue "Link to this definition")

Return a copy of the referent.
If the referent is unpicklable then this will raise an exception.

__repr__()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseProxy.__repr__ "Link to this definition")

Return a representation of the proxy object.

__str__()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseProxy.__str__ "Link to this definition")

Return the representation of the referent.
#### Cleanup[¶](https://docs.python.org/3/library/multiprocessing.html#cleanup "Link to this heading")
A proxy object uses a weakref callback so that when it gets garbage collected it deregisters itself from the manager which owns its referent.
A shared object gets deleted from the manager process when there are no longer any proxies referring to it.
### Process Pools[¶](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.pool "Link to this heading")
One can create a pool of processes which will carry out tasks submitted to it with the [`Pool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool") class.

_class_ multiprocessing.pool.Pool([_processes_[, _initializer_[, _initargs_[, _maxtasksperchild_[, _context_]]]]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "Link to this definition")

A process pool object which controls a pool of worker processes to which jobs can be submitted. It supports asynchronous results with timeouts and callbacks and has a parallel map implementation.
_processes_ is the number of worker processes to use. If _processes_ is `None` then the number returned by [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count") is used.
If _initializer_ is not `None` then each worker process will call `initializer(*initargs)` when it starts.
_maxtasksperchild_ is the number of tasks a worker process can complete before it will exit and be replaced with a fresh worker process, to enable unused resources to be freed. The default _maxtasksperchild_ is `None`, which means worker processes will live as long as the pool.
_context_ can be used to specify the context used for starting the worker processes. Usually a pool is created using the function `multiprocessing.Pool()` or the [`Pool()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool") method of a context object. In both cases _context_ is set appropriately. If `None`, calling this function will have the side effect of setting the current global start method if it has not been set already. See the `get_context()` function.
Note that the methods of the pool object should only be called by the process which created the pool.
Warning
[`multiprocessing.pool`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.pool "multiprocessing.pool: Create pools of processes.") objects have internal resources that need to be properly managed (like any other resource) by using the pool as a context manager or by calling [`close()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.close "multiprocessing.pool.Pool.close") and [`terminate()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.terminate "multiprocessing.pool.Pool.terminate") manually. Failure to do this can lead to the process hanging on finalization.
Note that it is **not correct** to rely on the garbage collector to destroy the pool as CPython does not assure that the finalizer of the pool will be called (see [`object.__del__()`](https://docs.python.org/3/reference/datamodel.html#object.__del__ "object.__del__") for more information).
Changed in version 3.2: Added the _maxtasksperchild_ parameter.
Changed in version 3.4: Added the _context_ parameter.
Changed in version 3.13: _processes_ uses [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count") by default, instead of [`os.cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count").
Note
Worker processes within a `Pool` typically live for the complete duration of the Pool’s work queue. A frequent pattern found in other systems (such as Apache, mod_wsgi, etc) to free resources held by workers is to allow a worker within a pool to complete only a set amount of work before exiting, being cleaned up and a new process spawned to replace the old one. The _maxtasksperchild_ argument to the `Pool` exposes this ability to the end user.

apply(_func_[, _args_[, _kwds_]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.apply "Link to this definition")

Call _func_ with arguments _args_ and keyword arguments _kwds_. It blocks until the result is ready. Given this blocks, [`apply_async()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.apply_async "multiprocessing.pool.Pool.apply_async") is better suited for performing work in parallel. Additionally, _func_ is only executed in one of the workers of the pool.

apply_async(_func_[, _args_[, _kwds_[, _callback_[, _error_callback_]]]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.apply_async "Link to this definition")

A variant of the [`apply()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.apply "multiprocessing.pool.Pool.apply") method which returns a [`AsyncResult`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.AsyncResult "multiprocessing.pool.AsyncResult") object.
If _callback_ is specified then it should be a callable which accepts a single argument. When the result becomes ready _callback_ is applied to it, that is unless the call failed, in which case the _error_callback_ is applied instead.
If _error_callback_ is specified then it should be a callable which accepts a single argument. If the target function fails, then the _error_callback_ is called with the exception instance.
Callbacks should complete immediately since otherwise the thread which handles the results will get blocked.

map(_func_ , _iterable_[, _chunksize_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map "Link to this definition")

A parallel equivalent of the [`map()`](https://docs.python.org/3/library/functions.html#map "map") built-in function (it supports only one _iterable_ argument though, for multiple iterables see [`starmap()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.starmap "multiprocessing.pool.Pool.starmap")). It blocks until the result is ready.
This method chops the iterable into a number of chunks which it submits to the process pool as separate tasks. The (approximate) size of these chunks can be specified by setting _chunksize_ to a positive integer.
Note that it may cause high memory usage for very long iterables. Consider using [`imap()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.imap "multiprocessing.pool.Pool.imap") or [`imap_unordered()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.imap_unordered "multiprocessing.pool.Pool.imap_unordered") with explicit _chunksize_ option for better efficiency.

map_async(_func_ , _iterable_[, _chunksize_[, _callback_[, _error_callback_]]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map_async "Link to this definition")

A variant of the [`map()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map "multiprocessing.pool.Pool.map") method which returns a [`AsyncResult`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.AsyncResult "multiprocessing.pool.AsyncResult") object.
If _callback_ is specified then it should be a callable which accepts a single argument. When the result becomes ready _callback_ is applied to it, that is unless the call failed, in which case the _error_callback_ is applied instead.
If _error_callback_ is specified then it should be a callable which accepts a single argument. If the target function fails, then the _error_callback_ is called with the exception instance.
Callbacks should complete immediately since otherwise the thread which handles the results will get blocked.

imap(_func_ , _iterable_[, _chunksize_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.imap "Link to this definition")

A lazier version of [`map()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map "multiprocessing.pool.Pool.map").
The _chunksize_ argument is the same as the one used by the [`map()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map "multiprocessing.pool.Pool.map") method. For very long iterables using a large value for _chunksize_ can make the job complete **much** faster than using the default value of `1`.
Also if _chunksize_ is `1` then the `next()` method of the iterator returned by the `imap()` method has an optional _timeout_ parameter: `next(timeout)` will raise [`multiprocessing.TimeoutError`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.TimeoutError "multiprocessing.TimeoutError") if the result cannot be returned within _timeout_ seconds.

imap_unordered(_func_ , _iterable_[, _chunksize_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.imap_unordered "Link to this definition")

The same as [`imap()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.imap "multiprocessing.pool.Pool.imap") except that the ordering of the results from the returned iterator should be considered arbitrary. (Only when there is only one worker process is the order guaranteed to be “correct”.)

starmap(_func_ , _iterable_[, _chunksize_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.starmap "Link to this definition")

Like [`map()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map "multiprocessing.pool.Pool.map") except that the elements of the _iterable_ are expected to be iterables that are unpacked as arguments.
Hence an _iterable_ of `[(1,2), (3, 4)]` results in `[func(1,2), func(3,4)]`.
Added in version 3.3.

starmap_async(_func_ , _iterable_[, _chunksize_[, _callback_[, _error_callback_]]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.starmap_async "Link to this definition")

A combination of [`starmap()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.starmap "multiprocessing.pool.Pool.starmap") and [`map_async()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map_async "multiprocessing.pool.Pool.map_async") that iterates over _iterable_ of iterables and calls _func_ with the iterables unpacked. Returns a result object.
Added in version 3.3.

close()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.close "Link to this definition")

Prevents any more tasks from being submitted to the pool. Once all the tasks have been completed the worker processes will exit.

terminate()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.terminate "Link to this definition")

Stops the worker processes immediately without completing outstanding work. When the pool object is garbage collected `terminate()` will be called immediately.

join()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.join "Link to this definition")

Wait for the worker processes to exit. One must call [`close()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.close "multiprocessing.pool.Pool.close") or [`terminate()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.terminate "multiprocessing.pool.Pool.terminate") before using `join()`.
Changed in version 3.3: Pool objects now support the context management protocol – see [Context Manager Types](https://docs.python.org/3/library/stdtypes.html#typecontextmanager). [`__enter__()`](https://docs.python.org/3/library/stdtypes.html#contextmanager.__enter__ "contextmanager.__enter__") returns the pool object, and [`__exit__()`](https://docs.python.org/3/library/stdtypes.html#contextmanager.__exit__ "contextmanager.__exit__") calls [`terminate()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.terminate "multiprocessing.pool.Pool.terminate").

_class_ multiprocessing.pool.AsyncResult[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.AsyncResult "Link to this definition")

The class of the result returned by [`Pool.apply_async()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.apply_async "multiprocessing.pool.Pool.apply_async") and [`Pool.map_async()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map_async "multiprocessing.pool.Pool.map_async").

get([_timeout_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.AsyncResult.get "Link to this definition")

Return the result when it arrives. If _timeout_ is not `None` and the result does not arrive within _timeout_ seconds then [`multiprocessing.TimeoutError`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.TimeoutError "multiprocessing.TimeoutError") is raised. If the remote call raised an exception then that exception will be reraised by `get()`.

wait([_timeout_])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.AsyncResult.wait "Link to this definition")

Wait until the result is available or until _timeout_ seconds pass.

ready()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.AsyncResult.ready "Link to this definition")

Return whether the call has completed.

successful()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.AsyncResult.successful "Link to this definition")

Return whether the call completed without raising an exception. Will raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the result is not ready.
Changed in version 3.7: If the result is not ready, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised instead of [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError").
The following example demonstrates the use of a pool:
Copy```
from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(processes=4) as pool:         # start 4 worker processes
        result = pool.apply_async(f, (10,)) # evaluate "f(10)" asynchronously in a single process
        print(result.get(timeout=1))        # prints "100" unless your computer is *very* slow

        print(pool.map(f, range(10)))       # prints "[0, 1, 4,..., 81]"

        it = pool.imap(f, range(10))
        print(next(it))                     # prints "0"
        print(next(it))                     # prints "1"
        print(it.next(timeout=1))           # prints "4" unless your computer is *very* slow

        result = pool.apply_async(time.sleep, (10,))
        print(result.get(timeout=1))        # raises multiprocessing.TimeoutError

```

### Listeners and Clients[¶](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.connection "Link to this heading")
Usually message passing between processes is done using queues or by using [`Connection`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection "multiprocessing.connection.Connection") objects returned by [`Pipe()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Pipe "multiprocessing.Pipe").
However, the `multiprocessing.connection` module allows some extra flexibility. It basically gives a high level message oriented API for dealing with sockets or Windows named pipes. It also has support for _digest authentication_ using the [`hmac`](https://docs.python.org/3/library/hmac.html#module-hmac "hmac: Keyed-Hashing for Message Authentication \(HMAC\) implementation") module, and for polling multiple connections at the same time.

multiprocessing.connection.deliver_challenge(_connection_ , _authkey_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.deliver_challenge "Link to this definition")

Send a randomly generated message to the other end of the connection and wait for a reply.
If the reply matches the digest of the message using _authkey_ as the key then a welcome message is sent to the other end of the connection. Otherwise [`AuthenticationError`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.AuthenticationError "multiprocessing.AuthenticationError") is raised.

multiprocessing.connection.answer_challenge(_connection_ , _authkey_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.answer_challenge "Link to this definition")

Receive a message, calculate the digest of the message using _authkey_ as the key, and then send the digest back.
If a welcome message is not received, then [`AuthenticationError`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.AuthenticationError "multiprocessing.AuthenticationError") is raised.

multiprocessing.connection.Client(_address_[, _family_[, _authkey_]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Client "Link to this definition")

Attempt to set up a connection to the listener which is using address _address_ , returning a [`Connection`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection "multiprocessing.connection.Connection").
The type of the connection is determined by _family_ argument, but this can generally be omitted since it can usually be inferred from the format of _address_. (See [Address Formats](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-address-formats))
If _authkey_ is given and not `None`, it should be a byte string and will be used as the secret key for an HMAC-based authentication challenge. No authentication is done if _authkey_ is `None`. [`AuthenticationError`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.AuthenticationError "multiprocessing.AuthenticationError") is raised if authentication fails. See [Authentication keys](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-auth-keys).

_class_ multiprocessing.connection.Listener([_address_[, _family_[, _backlog_[, _authkey_]]]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Listener "Link to this definition")

A wrapper for a bound socket or Windows named pipe which is ‘listening’ for connections.
_address_ is the address to be used by the bound socket or named pipe of the listener object.
Note
If an address of ‘0.0.0.0’ is used, the address will not be a connectable end point on Windows. If you require a connectable end-point, you should use ‘127.0.0.1’.
_family_ is the type of socket (or named pipe) to use. This can be one of the strings `'AF_INET'` (for a TCP socket), `'AF_UNIX'` (for a Unix domain socket) or `'AF_PIPE'` (for a Windows named pipe). Of these only the first is guaranteed to be available. If _family_ is `None` then the family is inferred from the format of _address_. If _address_ is also `None` then a default is chosen. This default is the family which is assumed to be the fastest available. See [Address Formats](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-address-formats). Note that if _family_ is `'AF_UNIX'` and address is `None` then the socket will be created in a private temporary directory created using [`tempfile.mkstemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp "tempfile.mkstemp").
If the listener object uses a socket then _backlog_ (1 by default) is passed to the [`listen()`](https://docs.python.org/3/library/socket.html#socket.socket.listen "socket.socket.listen") method of the socket once it has been bound.
If _authkey_ is given and not `None`, it should be a byte string and will be used as the secret key for an HMAC-based authentication challenge. No authentication is done if _authkey_ is `None`. [`AuthenticationError`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.AuthenticationError "multiprocessing.AuthenticationError") is raised if authentication fails. See [Authentication keys](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-auth-keys).

accept()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Listener.accept "Link to this definition")

Accept a connection on the bound socket or named pipe of the listener object and return a [`Connection`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection "multiprocessing.connection.Connection") object. If authentication is attempted and fails, then [`AuthenticationError`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.AuthenticationError "multiprocessing.AuthenticationError") is raised.

close()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Listener.close "Link to this definition")

Close the bound socket or named pipe of the listener object. This is called automatically when the listener is garbage collected. However it is advisable to call it explicitly.
Listener objects have the following read-only properties:

address[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Listener.address "Link to this definition")

The address which is being used by the Listener object.

last_accepted[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Listener.last_accepted "Link to this definition")

The address from which the last accepted connection came. If this is unavailable then it is `None`.
Changed in version 3.3: Listener objects now support the context management protocol – see [Context Manager Types](https://docs.python.org/3/library/stdtypes.html#typecontextmanager). [`__enter__()`](https://docs.python.org/3/library/stdtypes.html#contextmanager.__enter__ "contextmanager.__enter__") returns the listener object, and [`__exit__()`](https://docs.python.org/3/library/stdtypes.html#contextmanager.__exit__ "contextmanager.__exit__") calls [`close()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Listener.close "multiprocessing.connection.Listener.close").

multiprocessing.connection.wait(_object_list_ , _timeout =None_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.wait "Link to this definition")

Wait till an object in _object_list_ is ready. Returns the list of those objects in _object_list_ which are ready. If _timeout_ is a float then the call blocks for at most that many seconds. If _timeout_ is `None` then it will block for an unlimited period. A negative timeout is equivalent to a zero timeout.
For both POSIX and Windows, an object can appear in _object_list_ if it is
  * a readable [`Connection`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection "multiprocessing.connection.Connection") object;
  * a connected and readable [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket") object; or
  * the [`sentinel`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.sentinel "multiprocessing.Process.sentinel") attribute of a [`Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process") object.


A connection or socket object is ready when there is data available to be read from it, or the other end has been closed.
**POSIX** : `wait(object_list, timeout)` almost equivalent `select.select(object_list, [], [], timeout)`. The difference is that, if [`select.select()`](https://docs.python.org/3/library/select.html#select.select "select.select") is interrupted by a signal, it can raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") with an error number of `EINTR`, whereas `wait()` will not.
**Windows** : An item in _object_list_ must either be an integer handle which is waitable (according to the definition used by the documentation of the Win32 function `WaitForMultipleObjects()`) or it can be an object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method which returns a socket handle or pipe handle. (Note that pipe handles and socket handles are **not** waitable handles.)
Added in version 3.3.
**Examples**
The following server code creates a listener which uses `'secret password'` as an authentication key. It then waits for a connection and sends some data to the client:
Copy```
from multiprocessing.connection import Listener
from array import array

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'

with Listener(address, authkey=b'secret password') as listener:
    with listener.accept() as conn:
        print('connection accepted from', listener.last_accepted)

        conn.send([2.25, None, 'junk', float])

        conn.send_bytes(b'hello')

        conn.send_bytes(array('i', [42, 1729]))

```

The following code connects to the server and receives some data from the server:
Copy```
from multiprocessing.connection import Client
from array import array

address = ('localhost', 6000)

with Client(address, authkey=b'secret password') as conn:
    print(conn.recv())                  # => [2.25, None, 'junk', float]

    print(conn.recv_bytes())            # => 'hello'

    arr = array('i', [0, 0, 0, 0, 0])
    print(conn.recv_bytes_into(arr))    # => 8
    print(arr)                          # => array('i', [42, 1729, 0, 0, 0])

```

The following code uses [`wait()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.wait "multiprocessing.connection.wait") to wait for messages from multiple processes at once:
Copy```
from multiprocessing import Process, Pipe, current_process
from multiprocessing.connection import wait

def foo(w):
    for i in range(10):
        w.send((i, current_process().name))
    w.close()

if __name__ == '__main__':
    readers = []

    for i in range(4):
        r, w = Pipe(duplex=False)
        readers.append(r)
        p = Process(target=foo, args=(w,))
        p.start()
        # We close the writable end of the pipe now to be sure that
        # p is the only process which owns a handle for it.  This
        # ensures that when p closes its handle for the writable end,
        # wait() will promptly report the readable end as being ready.
        w.close()

    while readers:
        for r in wait(readers):
            try:
                msg = r.recv()
            except EOFError:
                readers.remove(r)
            else:
                print(msg)

```

#### Address Formats[¶](https://docs.python.org/3/library/multiprocessing.html#address-formats "Link to this heading")
  * An `'AF_INET'` address is a tuple of the form `(hostname, port)` where _hostname_ is a string and _port_ is an integer.
  * An `'AF_UNIX'` address is a string representing a filename on the filesystem.
  * An `'AF_PIPE'` address is a string of the form `r'\\.\pipe\_PipeName_'`. To use[`Client()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Client "multiprocessing.connection.Client") to connect to a named pipe on a remote computer called _ServerName_ one should use an address of the form `r'\\_ServerName_\pipe\_PipeName_'`instead.


Note that any string beginning with two backslashes is assumed by default to be an `'AF_PIPE'` address rather than an `'AF_UNIX'` address.
### Authentication keys[¶](https://docs.python.org/3/library/multiprocessing.html#authentication-keys "Link to this heading")
When one uses [`Connection.recv`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection.recv "multiprocessing.connection.Connection.recv"), the data received is automatically unpickled. Unfortunately unpickling data from an untrusted source is a security risk. Therefore [`Listener`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Listener "multiprocessing.connection.Listener") and [`Client()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Client "multiprocessing.connection.Client") use the [`hmac`](https://docs.python.org/3/library/hmac.html#module-hmac "hmac: Keyed-Hashing for Message Authentication \(HMAC\) implementation") module to provide digest authentication.
An authentication key is a byte string which can be thought of as a password: once a connection is established both ends will demand proof that the other knows the authentication key. (Demonstrating that both ends are using the same key does **not** involve sending the key over the connection.)
If authentication is requested but no authentication key is specified then the return value of `current_process().authkey` is used (see [`Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process")). This value will be automatically inherited by any `Process` object that the current process creates. This means that (by default) all processes of a multi-process program will share a single authentication key which can be used when setting up connections between themselves.
Suitable authentication keys can also be generated by using [`os.urandom()`](https://docs.python.org/3/library/os.html#os.urandom "os.urandom").
### Logging[¶](https://docs.python.org/3/library/multiprocessing.html#logging "Link to this heading")
Some support for logging is available. Note, however, that the [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.") package does not use process shared locks so it is possible (depending on the handler type) for messages from different processes to get mixed up.

multiprocessing.get_logger()[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.get_logger "Link to this definition")

Returns the logger used by `multiprocessing`. If necessary, a new one will be created.
When first created the logger has level [`logging.NOTSET`](https://docs.python.org/3/library/logging.html#logging.NOTSET "logging.NOTSET") and no default handler. Messages sent to this logger will not by default propagate to the root logger.
Note that on Windows child processes will only inherit the level of the parent process’s logger – any other customization of the logger will not be inherited.

multiprocessing.log_to_stderr(_level =None_)[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.log_to_stderr "Link to this definition")

This function performs a call to [`get_logger()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.get_logger "multiprocessing.get_logger") but in addition to returning the logger created by get_logger, it adds a handler which sends output to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") using format `'[%(levelname)s/%(processName)s] %(message)s'`. You can modify `levelname` of the logger by passing a `level` argument.
Below is an example session with logging turned on:
Copy```
>>> import multiprocessing, logging
>>> logger = multiprocessing.log_to_stderr()
>>> logger.setLevel(logging.INFO)
>>> logger.warning('doomed')
[WARNING/MainProcess] doomed
>>> m = multiprocessing.Manager()
[INFO/SyncManager-...] child process calling self.run()
[INFO/SyncManager-...] created temp directory /.../pymp-...
[INFO/SyncManager-...] manager serving at '/.../listener-...'
>>> del m
[INFO/MainProcess] sending shutdown message to manager
[INFO/SyncManager-...] manager exiting with exitcode 0

```

For a full table of logging levels, see the [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.") module.
### The `multiprocessing.dummy` module[¶](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.dummy "Link to this heading")
`multiprocessing.dummy` replicates the API of `multiprocessing` but is no more than a wrapper around the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.") module.
In particular, the `Pool` function provided by `multiprocessing.dummy` returns an instance of [`ThreadPool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.ThreadPool "multiprocessing.pool.ThreadPool"), which is a subclass of [`Pool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool") that supports all the same method calls but uses a pool of worker threads rather than worker processes.

_class_ multiprocessing.pool.ThreadPool([_processes_[, _initializer_[, _initargs_]]])[¶](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.ThreadPool "Link to this definition")

A thread pool object which controls a pool of worker threads to which jobs can be submitted. `ThreadPool` instances are fully interface compatible with [`Pool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool") instances, and their resources must also be properly managed, either by using the pool as a context manager or by calling [`close()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.close "multiprocessing.pool.Pool.close") and [`terminate()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.terminate "multiprocessing.pool.Pool.terminate") manually.
_processes_ is the number of worker threads to use. If _processes_ is `None` then the number returned by [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count") is used.
If _initializer_ is not `None` then each worker process will call `initializer(*initargs)` when it starts.
Unlike [`Pool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool"), _maxtasksperchild_ and _context_ cannot be provided.
Note
A `ThreadPool` shares the same interface as [`Pool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool"), which is designed around a pool of processes and predates the introduction of the [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures "concurrent.futures: Execute computations concurrently using threads or processes.") module. As such, it inherits some operations that don’t make sense for a pool backed by threads, and it has its own type for representing the status of asynchronous jobs, [`AsyncResult`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.AsyncResult "multiprocessing.pool.AsyncResult"), that is not understood by any other libraries.
Users should generally prefer to use [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor"), which has a simpler interface that was designed around threads from the start, and which returns [`concurrent.futures.Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future") instances that are compatible with many other libraries, including [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.").
## Programming guidelines[¶](https://docs.python.org/3/library/multiprocessing.html#programming-guidelines "Link to this heading")
There are certain guidelines and idioms which should be adhered to when using `multiprocessing`.
### All start methods[¶](https://docs.python.org/3/library/multiprocessing.html#all-start-methods "Link to this heading")
The following applies to all start methods.
Avoid shared state
> As far as possible one should try to avoid shifting large amounts of data between processes.
> It is probably best to stick to using queues or pipes for communication between processes rather than using the lower level synchronization primitives.
Picklability
> Ensure that the arguments to the methods of proxies are picklable.
Thread safety of proxies
> Do not use a proxy object from more than one thread unless you protect it with a lock.
> (There is never a problem with different processes using the _same_ proxy.)
Joining zombie processes
> On POSIX when a process finishes but has not been joined it becomes a zombie. There should never be very many because each time a new process starts (or [`active_children()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.active_children "multiprocessing.active_children") is called) all completed processes which have not yet been joined will be joined. Also calling a finished process’s [`Process.is_alive`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.is_alive "multiprocessing.Process.is_alive") will join the process. Even so it is probably good practice to explicitly join all the processes that you start.
Better to inherit than pickle/unpickle
> When using the _spawn_ or _forkserver_ start methods many types from `multiprocessing` need to be picklable so that child processes can use them. However, one should generally avoid sending shared objects to other processes using pipes or queues. Instead you should arrange the program so that a process which needs access to a shared resource created elsewhere can inherit it from an ancestor process.
Avoid terminating processes
> Using the [`Process.terminate`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.terminate "multiprocessing.Process.terminate") method to stop a process is liable to cause any shared resources (such as locks, semaphores, pipes and queues) currently being used by the process to become broken or unavailable to other processes.
> Therefore it is probably best to only consider using [`Process.terminate`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.terminate "multiprocessing.Process.terminate") on processes which never use any shared resources.
Joining processes that use queues
> Bear in mind that a process that has put items in a queue will wait before terminating until all the buffered items are fed by the “feeder” thread to the underlying pipe. (The child process can call the [`Queue.cancel_join_thread`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue.cancel_join_thread "multiprocessing.Queue.cancel_join_thread") method of the queue to avoid this behaviour.)
> This means that whenever you use a queue you need to make sure that all items which have been put on the queue will eventually be removed before the process is joined. Otherwise you cannot be sure that processes which have put items on the queue will terminate. Remember also that non-daemonic processes will be joined automatically.
> An example which will deadlock is the following:
> Copy```
from multiprocessing import Process, Queue

def f(q):
    q.put('X' * 1000000)

if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue,))
    p.start()
    p.join()                    # this deadlocks
    obj = queue.get()

```

> A fix here would be to swap the last two lines (or simply remove the `p.join()` line).
Explicitly pass resources to child processes
> On POSIX using the _fork_ start method, a child process can make use of a shared resource created in a parent process using a global resource. However, it is better to pass the object as an argument to the constructor for the child process.
> Apart from making the code (potentially) compatible with Windows and the other start methods this also ensures that as long as the child process is still alive the object will not be garbage collected in the parent process. This might be important if some resource is freed when the object is garbage collected in the parent process.
> So for instance
> Copy```
from multiprocessing import Process, Lock

def f():
    ... do something using "lock" ...

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        Process(target=f).start()

```

> should be rewritten as
> Copy```
from multiprocessing import Process, Lock

def f(l):
    ... do something using "l" ...

if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        Process(target=f, args=(lock,)).start()

```

Beware of replacing [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin") with a “file like object”
> `multiprocessing` originally unconditionally called:
> Copy```
os.close(sys.stdin.fileno())

```

> in the `multiprocessing.Process._bootstrap()` method — this resulted in issues with processes-in-processes. This has been changed to:
> Copy```
sys.stdin.close()
sys.stdin = open(os.open(os.devnull, os.O_RDONLY), closefd=False)

```

> Which solves the fundamental issue of processes colliding with each other resulting in a bad file descriptor error, but introduces a potential danger to applications which replace [`sys.stdin()`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin") with a “file-like object” with output buffering. This danger is that if multiple processes call [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close") on this file-like object, it could result in the same data being flushed to the object multiple times, resulting in corruption.
> If you write a file-like object and implement your own caching, you can make it fork-safe by storing the pid whenever you append to the cache, and discarding the cache when the pid changes. For example:
> Copy```
@property
def cache(self):
    pid = os.getpid()
    if pid != self._pid:
        self._pid = pid
        self._cache = []
    return self._cache

```

> For more information, see [bpo-5155](https://bugs.python.org/issue?@action=redirect&bpo=5155), [bpo-5313](https://bugs.python.org/issue?@action=redirect&bpo=5313) and [bpo-5331](https://bugs.python.org/issue?@action=redirect&bpo=5331)
### The _spawn_ and _forkserver_ start methods[¶](https://docs.python.org/3/library/multiprocessing.html#the-spawn-and-forkserver-start-methods "Link to this heading")
There are a few extra restrictions which don’t apply to the _fork_ start method.
More picklability
> Ensure that all arguments to [`Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process") are picklable. Also, if you subclass `Process.__init__`, you must make sure that instances will be picklable when the [`Process.start`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.start "multiprocessing.Process.start") method is called.
Global variables
> Bear in mind that if code run in a child process tries to access a global variable, then the value it sees (if any) may not be the same as the value in the parent process at the time that [`Process.start`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.start "multiprocessing.Process.start") was called.
> However, global variables which are just module level constants cause no problems.
Safe importing of main module
> Make sure that the main module can be safely imported by a new Python interpreter without causing unintended side effects (such as starting a new process).
> For example, using the _spawn_ or _forkserver_ start method running the following module would fail with a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError"):
> Copy```
from multiprocessing import Process

def foo():
    print('hello')

p = Process(target=foo)
p.start()

```

> Instead one should protect the “entry point” of the program by using `if __name__ == '__main__':` as follows:
> Copy```
from multiprocessing import Process, freeze_support, set_start_method

def foo():
    print('hello')

if __name__ == '__main__':
    freeze_support()
    set_start_method('spawn')
    p = Process(target=foo)
    p.start()

```

> (The `freeze_support()` line can be omitted if the program will be run normally instead of frozen.)
> This allows the newly spawned Python interpreter to safely import the module and then run the module’s `foo()` function.
> Similar restrictions apply if a pool or manager is created in the main module.
## Examples[¶](https://docs.python.org/3/library/multiprocessing.html#examples "Link to this heading")
Demonstration of how to create and use customized managers and proxies:
Copy```
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager, BaseProxy
import operator

##

class Foo:
    def f(self):
        print('you called Foo.f()')
    def g(self):
        print('you called Foo.g()')
    def _h(self):
        print('you called Foo._h()')

# A simple generator function
def baz():
    for i in range(10):
        yield i*i

# Proxy type for generator objects
class GeneratorProxy(BaseProxy):
    _exposed_ = ['__next__']
    def __iter__(self):
        return self
    def __next__(self):
        return self._callmethod('__next__')

# Function to return the operator module
def get_operator_module():
    return operator

##

class MyManager(BaseManager):
    pass

# register the Foo class; make `f()` and `g()` accessible via proxy
MyManager.register('Foo1', Foo)

# register the Foo class; make `g()` and `_h()` accessible via proxy
MyManager.register('Foo2', Foo, exposed=('g', '_h'))

# register the generator function baz; use `GeneratorProxy` to make proxies
MyManager.register('baz', baz, proxytype=GeneratorProxy)

# register get_operator_module(); make public functions accessible via proxy
MyManager.register('operator', get_operator_module)

##

def test():
    manager = MyManager()
    manager.start()

    print('-' * 20)

    f1 = manager.Foo1()
    f1.f()
    f1.g()
    assert not hasattr(f1, '_h')
    assert sorted(f1._exposed_) == sorted(['f', 'g'])

    print('-' * 20)

    f2 = manager.Foo2()
    f2.g()
    f2._h()
    assert not hasattr(f2, 'f')
    assert sorted(f2._exposed_) == sorted(['g', '_h'])

    print('-' * 20)

    it = manager.baz()
    for i in it:
        print('<%d>' % i, end=' ')
    print()

    print('-' * 20)

    op = manager.operator()
    print('op.add(23, 45) =', op.add(23, 45))
    print('op.pow(2, 94) =', op.pow(2, 94))
    print('op._exposed_ =', op._exposed_)

##

if __name__ == '__main__':
    freeze_support()
    test()

```

Using [`Pool`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool "multiprocessing.pool.Pool"):
Copy```
import multiprocessing
import time
import random
import sys
