#  `concurrent.futures` — Launching parallel tasks[¶](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures "Link to this heading")
Added in version 3.2.
**Source code:**
* * *
The `concurrent.futures` module provides a high-level interface for asynchronously executing callables.
The asynchronous execution can be performed with threads, using [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor") or [`InterpreterPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor "concurrent.futures.InterpreterPoolExecutor"), or separate processes, using [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor"). Each implements the same interface, which is defined by the abstract [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") class.
[`concurrent.futures.Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future") must not be confused with [`asyncio.Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future"), which is designed for use with [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") tasks and coroutines. See the [asyncio’s Future](https://docs.python.org/3/library/asyncio-future.html) documentation for a detailed comparison of the two.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
## Executor Objects[¶](https://docs.python.org/3/library/concurrent.futures.html#executor-objects "Link to this heading")

_class_ concurrent.futures.Executor[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "Link to this definition")

An abstract class that provides methods to execute calls asynchronously. It should not be used directly, but through its concrete subclasses.

submit(_fn_ , _/_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.submit "Link to this definition")

Schedules the callable, _fn_ , to be executed as `fn(*args, **kwargs)` and returns a [`Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future") object representing the execution of the callable.
Copy```
with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())

```


map(_fn_ , _* iterables_, _timeout =None_, _chunksize =1_, _buffersize =None_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.map "Link to this definition")

Similar to [`map(fn, *iterables)`](https://docs.python.org/3/library/functions.html#map "map") except:
  * The _iterables_ are collected immediately rather than lazily, unless a _buffersize_ is specified to limit the number of submitted tasks whose results have not yet been yielded. If the buffer is full, iteration over the _iterables_ pauses until a result is yielded from the buffer.
  * _fn_ is executed asynchronously and several calls to _fn_ may be made concurrently.


The returned iterator raises a [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError "TimeoutError") if [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") is called and the result isn’t available after _timeout_ seconds from the original call to `Executor.map()`. _timeout_ can be an int or a float. If _timeout_ is not specified or `None`, there is no limit to the wait time.
If a _fn_ call raises an exception, then that exception will be raised when its value is retrieved from the iterator.
When using [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor"), this method chops _iterables_ into a number of chunks which it submits to the pool as separate tasks. The (approximate) size of these chunks can be specified by setting _chunksize_ to a positive integer. For very long iterables, using a large value for _chunksize_ can significantly improve performance compared to the default size of 1. With [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor") and [`InterpreterPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor "concurrent.futures.InterpreterPoolExecutor"), _chunksize_ has no effect.
Changed in version 3.5: Added the _chunksize_ parameter.
Changed in version 3.14: Added the _buffersize_ parameter.

shutdown(_wait =True_, _*_ , _cancel_futures =False_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.shutdown "Link to this definition")

Signal the executor that it should free any resources that it is using when the currently pending futures are done executing. Calls to [`Executor.submit()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.submit "concurrent.futures.Executor.submit") and [`Executor.map()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.map "concurrent.futures.Executor.map") made after shutdown will raise [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError").
If _wait_ is `True` then this method will not return until all the pending futures are done executing and the resources associated with the executor have been freed. If _wait_ is `False` then this method will return immediately and the resources associated with the executor will be freed when all pending futures are done executing. Regardless of the value of _wait_ , the entire Python program will not exit until all pending futures are done executing.
If _cancel_futures_ is `True`, this method will cancel all pending futures that the executor has not started running. Any futures that are completed or running won’t be cancelled, regardless of the value of _cancel_futures_.
If both _cancel_futures_ and _wait_ are `True`, all futures that the executor has started running will be completed prior to this method returning. The remaining futures are cancelled.
You can avoid having to call this method explicitly if you use the executor as a [context manager](https://docs.python.org/3/glossary.html#term-context-manager) via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement, which will shutdown the `Executor` (waiting as if `Executor.shutdown()` were called with _wait_ set to `True`):
Copy```
import shutil
with ThreadPoolExecutor(max_workers=4) as e:
    e.submit(shutil.copy, 'src1.txt', 'dest1.txt')
    e.submit(shutil.copy, 'src2.txt', 'dest2.txt')
    e.submit(shutil.copy, 'src3.txt', 'dest3.txt')
    e.submit(shutil.copy, 'src4.txt', 'dest4.txt')

```

Changed in version 3.9: Added _cancel_futures_.
## ThreadPoolExecutor[¶](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor "Link to this heading")
[`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor") is an [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") subclass that uses a pool of threads to execute calls asynchronously.
Deadlocks can occur when the callable associated with a [`Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future") waits on the results of another `Future`. For example:
Copy```
import time
def wait_on_b():
    time.sleep(5)
    print(b.result())  # b will never complete because it is waiting on a.
    return 5

def wait_on_a():
    time.sleep(5)
    print(a.result())  # a will never complete because it is waiting on b.
    return 6


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)

```

And:
Copy```
def wait_on_future():
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    print(f.result())

executor = ThreadPoolExecutor(max_workers=1)
executor.submit(wait_on_future)

```


_class_ concurrent.futures.ThreadPoolExecutor(_max_workers =None_, _thread_name_prefix =''_, _initializer =None_, _initargs =()_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "Link to this definition")

An [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") subclass that uses a pool of at most _max_workers_ threads to execute calls asynchronously.
All threads enqueued to `ThreadPoolExecutor` will be joined before the interpreter can exit. Note that the exit handler which does this is executed _before_ any exit handlers added using `atexit`. This means exceptions in the main thread must be caught and handled in order to signal threads to exit gracefully. For this reason, it is recommended that `ThreadPoolExecutor` not be used for long-running tasks.
_initializer_ is an optional callable that is called at the start of each worker thread; _initargs_ is a tuple of arguments passed to the initializer. Should _initializer_ raise an exception, all currently pending jobs will raise a [`BrokenThreadPool`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.thread.BrokenThreadPool "concurrent.futures.thread.BrokenThreadPool"), as well as any attempt to submit more jobs to the pool.
Changed in version 3.5: If _max_workers_ is `None` or not given, it will default to the number of processors on the machine, multiplied by `5`, assuming that `ThreadPoolExecutor` is often used to overlap I/O instead of CPU work and the number of workers should be higher than the number of workers for [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor").
Changed in version 3.6: Added the _thread_name_prefix_ parameter to allow users to control the [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") names for worker threads created by the pool for easier debugging.
Changed in version 3.7: Added the _initializer_ and _initargs_ arguments.
Changed in version 3.8: Default value of _max_workers_ is changed to `min(32, os.cpu_count() + 4)`. This default value preserves at least 5 workers for I/O bound tasks. It utilizes at most 32 CPU cores for CPU bound tasks which release the GIL. And it avoids using very large resources implicitly on many-core machines.
ThreadPoolExecutor now reuses idle worker threads before starting _max_workers_ worker threads too.
Changed in version 3.13: Default value of _max_workers_ is changed to `min(32, (os.process_cpu_count() or 1) + 4)`.
### ThreadPoolExecutor Example[¶](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor-example "Link to this heading")
Copy```
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://nonexistent-subdomain.python.org/']
