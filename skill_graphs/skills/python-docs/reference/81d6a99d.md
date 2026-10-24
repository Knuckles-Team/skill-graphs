# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))

```

## InterpreterPoolExecutor[¶](https://docs.python.org/3/library/concurrent.futures.html#interpreterpoolexecutor "Link to this heading")
Added in version 3.14.
The [`InterpreterPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor "concurrent.futures.InterpreterPoolExecutor") class uses a pool of interpreters to execute calls asynchronously. It is a [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor") subclass, which means each worker is running in its own thread. The difference here is that each worker has its own interpreter, and runs each task using that interpreter.
The biggest benefit to using interpreters instead of only threads is true multi-core parallelism. Each interpreter has its own [Global Interpreter Lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock), so code running in one interpreter can run on one CPU core, while code in another interpreter runs unblocked on a different core.
The tradeoff is that writing concurrent code for use with multiple interpreters can take extra effort. However, this is because it forces you to be deliberate about how and when interpreters interact, and to be explicit about what data is shared between interpreters. This results in several benefits that help balance the extra effort, including true multi-core parallelism, For example, code written this way can make it easier to reason about concurrency. Another major benefit is that you don’t have to deal with several of the big pain points of using threads, like race conditions.
Each worker’s interpreter is isolated from all the other interpreters. “Isolated” means each interpreter has its own runtime state and operates completely independently. For example, if you redirect [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") in one interpreter, it will not be automatically redirected to any other interpreter. If you import a module in one interpreter, it is not automatically imported in any other. You would need to import the module separately in interpreter where you need it. In fact, each module imported in an interpreter is a completely separate object from the same module in a different interpreter, including [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions."), [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace."), and even `__main__`.
Isolation means a mutable object, or other data, cannot be used by more than one interpreter at the same time. That effectively means interpreters cannot actually share such objects or data. Instead, each interpreter must have its own copy, and you will have to synchronize any changes between the copies manually. Immutable objects and data, like the builtin singletons, strings, and tuples of immutable objects, don’t have these limitations.
Communicating and synchronizing between interpreters is most effectively done using dedicated tools, like those proposed in [**PEP 734**](https://peps.python.org/pep-0734/). One less efficient alternative is to serialize with [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and then send the bytes over a shared [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") or [`pipe`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe").

_class_ concurrent.futures.InterpreterPoolExecutor(_max_workers =None_, _thread_name_prefix =''_, _initializer =None_, _initargs =()_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor "Link to this definition")

A [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor") subclass that executes calls asynchronously using a pool of at most _max_workers_ threads. Each thread runs tasks in its own interpreter. The worker interpreters are isolated from each other, which means each has its own runtime state and that they can’t share any mutable objects or other data. Each interpreter has its own [Global Interpreter Lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock), which means code run with this executor has true multi-core parallelism.
The optional _initializer_ and _initargs_ arguments have the same meaning as for `ThreadPoolExecutor`: the initializer is run when each worker is created, though in this case it is run in the worker’s interpreter. The executor serializes the _initializer_ and _initargs_ using [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") when sending them to the worker’s interpreter.
Note
The executor may replace uncaught exceptions from _initializer_ with [`ExecutionFailed`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.ExecutionFailed "concurrent.interpreters.ExecutionFailed").
Other caveats from parent [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor") apply here.
[`submit()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.submit "concurrent.futures.Executor.submit") and [`map()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.map "concurrent.futures.Executor.map") work like normal, except the worker serializes the callable and arguments using [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") when sending them to its interpreter. The worker likewise serializes the return value when sending it back.
When a worker’s current task raises an uncaught exception, the worker always tries to preserve the exception as-is. If that is successful then it also sets the `__cause__` to a corresponding [`ExecutionFailed`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.ExecutionFailed "concurrent.interpreters.ExecutionFailed") instance, which contains a summary of the original exception. In the uncommon case that the worker is not able to preserve the original as-is then it directly preserves the corresponding `ExecutionFailed` instance instead.
## ProcessPoolExecutor[¶](https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor "Link to this heading")
The [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor") class is an [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") subclass that uses a pool of processes to execute calls asynchronously. `ProcessPoolExecutor` uses the [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") module, which allows it to side-step the [Global Interpreter Lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock) but also means that only picklable objects can be executed and returned.
The `__main__` module must be importable by worker subprocesses. This means that [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor") will not work in the interactive interpreter.
Calling [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") or [`Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future") methods from a callable submitted to a [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor") will result in deadlock.
Note that the restrictions on functions and arguments needing to picklable as per [`multiprocessing.Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process") apply when using [`submit()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.submit "concurrent.futures.Executor.submit") and [`map()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.map "concurrent.futures.Executor.map") on a [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor"). A function defined in a REPL or a lambda should not be expected to work.

_class_ concurrent.futures.ProcessPoolExecutor(_max_workers =None_, _mp_context =None_, _initializer =None_, _initargs =()_, _max_tasks_per_child =None_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "Link to this definition")

An [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") subclass that executes calls asynchronously using a pool of at most _max_workers_ processes. If _max_workers_ is `None` or not given, it will default to [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count"). If _max_workers_ is less than or equal to `0`, then a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised. On Windows, _max_workers_ must be less than or equal to `61`. If it is not then `ValueError` will be raised. If _max_workers_ is `None`, then the default chosen will be at most `61`, even if more processors are available. _mp_context_ can be a [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") context or `None`. It will be used to launch the workers. If _mp_context_ is `None` or not given, the default `multiprocessing` context is used. See [Contexts and start methods](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-start-methods).
_initializer_ is an optional callable that is called at the start of each worker process; _initargs_ is a tuple of arguments passed to the initializer. Should _initializer_ raise an exception, all currently pending jobs will raise a [`BrokenProcessPool`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.process.BrokenProcessPool "concurrent.futures.process.BrokenProcessPool"), as well as any attempt to submit more jobs to the pool.
_max_tasks_per_child_ is an optional argument that specifies the maximum number of tasks a single process can execute before it will exit and be replaced with a fresh worker process. By default _max_tasks_per_child_ is `None` which means worker processes will live as long as the pool. When a max is specified, the “spawn” multiprocessing start method will be used by default in absence of a _mp_context_ parameter. This feature is incompatible with the “fork” start method.
Note
Bugs have been reported when using the _max_tasks_per_child_ feature that can result in the `ProcessPoolExecutor` hanging in some circumstances. Follow its eventual resolution in
Changed in version 3.3: When one of the worker processes terminates abruptly, a [`BrokenProcessPool`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.process.BrokenProcessPool "concurrent.futures.process.BrokenProcessPool") error is now raised. Previously, behaviour was undefined but operations on the executor or its futures would often freeze or deadlock.
Changed in version 3.7: The _mp_context_ argument was added to allow users to control the start_method for worker processes created by the pool.
Added the _initializer_ and _initargs_ arguments.
Changed in version 3.11: The _max_tasks_per_child_ argument was added to allow users to control the lifetime of workers in the pool.
Changed in version 3.12: On POSIX systems, if your application has multiple threads and the [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") context uses the `"fork"` start method: The [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork") function called internally to spawn workers may raise a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning"). Pass a _mp_context_ configured to use a different start method. See the `os.fork()` documentation for further explanation.
Changed in version 3.13: _max_workers_ uses [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count") by default, instead of [`os.cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count").
Changed in version 3.14: The default process start method (see [Contexts and start methods](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-start-methods)) changed away from _fork_. If you require the _fork_ start method for `ProcessPoolExecutor` you must explicitly pass `mp_context=multiprocessing.get_context("fork")`.

terminate_workers()[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor.terminate_workers "Link to this definition")

Attempt to terminate all living worker processes immediately by calling [`Process.terminate`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.terminate "multiprocessing.Process.terminate") on each of them. Internally, it will also call [`Executor.shutdown()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.shutdown "concurrent.futures.Executor.shutdown") to ensure that all other resources associated with the executor are freed.
After calling this method the caller should no longer submit tasks to the executor.
Added in version 3.14.

kill_workers()[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor.kill_workers "Link to this definition")

Attempt to kill all living worker processes immediately by calling [`Process.kill`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.kill "multiprocessing.Process.kill") on each of them. Internally, it will also call [`Executor.shutdown()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.shutdown "concurrent.futures.Executor.shutdown") to ensure that all other resources associated with the executor are freed.
After calling this method the caller should no longer submit tasks to the executor.
Added in version 3.14.
### ProcessPoolExecutor Example[¶](https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor-example "Link to this heading")
Copy```
import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()

```

## Future Objects[¶](https://docs.python.org/3/library/concurrent.futures.html#future-objects "Link to this heading")
The [`Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future") class encapsulates the asynchronous execution of a callable. `Future` instances are created by [`Executor.submit()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.submit "concurrent.futures.Executor.submit").

_class_ concurrent.futures.Future[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "Link to this definition")

Encapsulates the asynchronous execution of a callable. `Future` instances are created by [`Executor.submit()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.submit "concurrent.futures.Executor.submit") and should not be created directly except for testing.

cancel()[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.cancel "Link to this definition")

Attempt to cancel the call. If the call is currently being executed or finished running and cannot be cancelled then the method will return `False`, otherwise the call will be cancelled and the method will return `True`.

cancelled()[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.cancelled "Link to this definition")

Return `True` if the call was successfully cancelled.

running()[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.running "Link to this definition")

Return `True` if the call is currently being executed and cannot be cancelled.

done()[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.done "Link to this definition")

Return `True` if the call was successfully cancelled or finished running.

result(_timeout =None_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.result "Link to this definition")

Return the value returned by the call. If the call hasn’t yet completed then this method will wait up to _timeout_ seconds. If the call hasn’t completed in _timeout_ seconds, then a [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError "TimeoutError") will be raised. _timeout_ can be an int or float. If _timeout_ is not specified or `None`, there is no limit to the wait time.
If the future is cancelled before completing then [`CancelledError`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.CancelledError "concurrent.futures.CancelledError") will be raised.
If the call raised an exception, this method will raise the same exception.

exception(_timeout =None_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.exception "Link to this definition")

Return the exception raised by the call. If the call hasn’t yet completed then this method will wait up to _timeout_ seconds. If the call hasn’t completed in _timeout_ seconds, then a [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError "TimeoutError") will be raised. _timeout_ can be an int or float. If _timeout_ is not specified or `None`, there is no limit to the wait time.
If the future is cancelled before completing then [`CancelledError`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.CancelledError "concurrent.futures.CancelledError") will be raised.
If the call completed without raising, `None` is returned.

add_done_callback(_fn_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.add_done_callback "Link to this definition")

Attaches the callable _fn_ to the future. _fn_ will be called, with the future as its only argument, when the future is cancelled or finishes running.
Added callables are called in the order that they were added and are always called in a thread belonging to the process that added them. If the callable raises an [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") subclass, it will be logged and ignored. If the callable raises a [`BaseException`](https://docs.python.org/3/library/exceptions.html#BaseException "BaseException") subclass, the behavior is undefined.
If the future has already completed or been cancelled, _fn_ will be called immediately.
The following `Future` methods are meant for use in unit tests and [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") implementations.

set_running_or_notify_cancel()[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.set_running_or_notify_cancel "Link to this definition")

This method should only be called by [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") implementations before executing the work associated with the `Future` and by unit tests.
If the method returns `False` then the `Future` was cancelled, i.e. [`Future.cancel()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.cancel "concurrent.futures.Future.cancel") was called and returned `True`. Any threads waiting on the `Future` completing (i.e. through [`as_completed()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.as_completed "concurrent.futures.as_completed") or [`wait()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.wait "concurrent.futures.wait")) will be woken up.
If the method returns `True` then the `Future` was not cancelled and has been put in the running state, i.e. calls to [`Future.running()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.running "concurrent.futures.Future.running") will return `True`.
This method can only be called once and cannot be called after [`Future.set_result()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.set_result "concurrent.futures.Future.set_result") or [`Future.set_exception()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.set_exception "concurrent.futures.Future.set_exception") have been called.

set_result(_result_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.set_result "Link to this definition")

Sets the result of the work associated with the `Future` to _result_.
This method should only be used by [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") implementations and unit tests.
Changed in version 3.8: This method raises [`concurrent.futures.InvalidStateError`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.InvalidStateError "concurrent.futures.InvalidStateError") if the `Future` is already done.

set_exception(_exception_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.set_exception "Link to this definition")

Sets the result of the work associated with the `Future` to the [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") _exception_.
This method should only be used by [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") implementations and unit tests.
Changed in version 3.8: This method raises [`concurrent.futures.InvalidStateError`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.InvalidStateError "concurrent.futures.InvalidStateError") if the `Future` is already done.
## Module Functions[¶](https://docs.python.org/3/library/concurrent.futures.html#module-functions "Link to this heading")

concurrent.futures.wait(_fs_ , _timeout =None_, _return_when =ALL_COMPLETED_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.wait "Link to this definition")

Wait for the [`Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future") instances (possibly created by different [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") instances) given by _fs_ to complete. Duplicate futures given to _fs_ are removed and will be returned only once. Returns a named 2-tuple of sets. The first set, named `done`, contains the futures that completed (finished or cancelled futures) before the wait completed. The second set, named `not_done`, contains the futures that did not complete (pending or running futures).
_timeout_ can be used to control the maximum number of seconds to wait before returning. _timeout_ can be an int or float. If _timeout_ is not specified or `None`, there is no limit to the wait time.
_return_when_ indicates when this function should return. It must be one of the following constants:
Constant | Description
---|---

concurrent.futures.FIRST_COMPLETED[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.FIRST_COMPLETED "Link to this definition")
| The function will return when any future finishes or is cancelled.

concurrent.futures.FIRST_EXCEPTION[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.FIRST_EXCEPTION "Link to this definition")
| The function will return when any future finishes by raising an exception. If no future raises an exception then it is equivalent to [`ALL_COMPLETED`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ALL_COMPLETED "concurrent.futures.ALL_COMPLETED").

concurrent.futures.ALL_COMPLETED[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ALL_COMPLETED "Link to this definition")
| The function will return when all futures finish or are cancelled.

concurrent.futures.as_completed(_fs_ , _timeout =None_)[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.as_completed "Link to this definition")

Returns an iterator over the [`Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future") instances (possibly created by different [`Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor") instances) given by _fs_ that yields futures as they complete (finished or cancelled futures). Any futures given by _fs_ that are duplicated will be returned once. Any futures that completed before `as_completed()` is called will be yielded first. The returned iterator raises a [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError "TimeoutError") if [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") is called and the result isn’t available after _timeout_ seconds from the original call to `as_completed()`. _timeout_ can be an int or float. If _timeout_ is not specified or `None`, there is no limit to the wait time.
See also

[**PEP 3148**](https://peps.python.org/pep-3148/) – futures - execute computations asynchronously

The proposal which described this feature for inclusion in the Python standard library.
## Exception classes[¶](https://docs.python.org/3/library/concurrent.futures.html#exception-classes "Link to this heading")

_exception_ concurrent.futures.CancelledError[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.CancelledError "Link to this definition")

Raised when a future is cancelled.

_exception_ concurrent.futures.TimeoutError[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.TimeoutError "Link to this definition")

A deprecated alias of `TimeoutError`, raised when a future operation exceeds the given timeout.
Changed in version 3.11: This class was made an alias of `TimeoutError`.

_exception_ concurrent.futures.BrokenExecutor[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.BrokenExecutor "Link to this definition")

Derived from [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError"), this exception class is raised when an executor is broken for some reason, and cannot be used to submit or execute new tasks.
Added in version 3.7.

_exception_ concurrent.futures.InvalidStateError[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.InvalidStateError "Link to this definition")

Raised when an operation is performed on a future that is not allowed in the current state.
Added in version 3.8.

_exception_ concurrent.futures.thread.BrokenThreadPool[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.thread.BrokenThreadPool "Link to this definition")

Derived from [`BrokenExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.BrokenExecutor "concurrent.futures.BrokenExecutor"), this exception class is raised when one of the workers of a [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor") has failed initializing.
Added in version 3.7.

_exception_ concurrent.futures.interpreter.BrokenInterpreterPool[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.interpreter.BrokenInterpreterPool "Link to this definition")

Derived from [`BrokenThreadPool`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.thread.BrokenThreadPool "concurrent.futures.thread.BrokenThreadPool"), this exception class is raised when one of the workers of a [`InterpreterPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor "concurrent.futures.InterpreterPoolExecutor") has failed initializing.
Added in version 3.14.

_exception_ concurrent.futures.process.BrokenProcessPool[¶](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.process.BrokenProcessPool "Link to this definition")

Derived from [`BrokenExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.BrokenExecutor "concurrent.futures.BrokenExecutor") (formerly [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError")), this exception class is raised when one of the workers of a [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor") has terminated in a non-clean fashion (for example, if it was killed from the outside).
Added in version 3.3.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`concurrent.futures` — Launching parallel tasks](https://docs.python.org/3/library/concurrent.futures.html)
    * [Executor Objects](https://docs.python.org/3/library/concurrent.futures.html#executor-objects)
    * [ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor)
      * [ThreadPoolExecutor Example](https://docs.python.org/3/library/concurrent.futures.html#threadpoolexecutor-example)
    * [InterpreterPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#interpreterpoolexecutor)
    * [ProcessPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor)
      * [ProcessPoolExecutor Example](https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor-example)
    * [Future Objects](https://docs.python.org/3/library/concurrent.futures.html#future-objects)
    * [Module Functions](https://docs.python.org/3/library/concurrent.futures.html#module-functions)
    * [Exception classes](https://docs.python.org/3/library/concurrent.futures.html#exception-classes)


#### Previous topic
[The `concurrent` package](https://docs.python.org/3/library/concurrent.html "previous chapter")
#### Next topic
[`concurrent.interpreters` — Multiple interpreters in the same process](https://docs.python.org/3/library/concurrent.interpreters.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=concurrent.futures+%E2%80%94+Launching+parallel+tasks&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fconcurrent.futures.html&pagesource=library%2Fconcurrent.futures.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/concurrent.interpreters.html "concurrent.interpreters — Multiple interpreters in the same process") |
  * [previous](https://docs.python.org/3/library/concurrent.html "The concurrent package") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`concurrent.futures` — Launching parallel tasks](https://docs.python.org/3/library/concurrent.futures.html)
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
