# Produce one item
with cv:
    make_an_item_available()
    cv.notify()

```

The `while` loop checking for the application’s condition is necessary because [`wait()`](https://docs.python.org/3/library/threading.html#threading.Condition.wait "threading.Condition.wait") can return after an arbitrary long time, and the condition which prompted the [`notify()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify "threading.Condition.notify") call may no longer hold true. This is inherent to multi-threaded programming. The [`wait_for()`](https://docs.python.org/3/library/threading.html#threading.Condition.wait_for "threading.Condition.wait_for") method can be used to automate the condition checking, and eases the computation of timeouts:
Copy```
# Consume an item
with cv:
    cv.wait_for(an_item_is_available)
    get_an_available_item()

```

To choose between [`notify()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify "threading.Condition.notify") and [`notify_all()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify_all "threading.Condition.notify_all"), consider whether one state change can be interesting for only one or several waiting threads. E.g. in a typical producer-consumer situation, adding one item to the buffer only needs to wake up one consumer thread.

_class_ threading.Condition(_lock =None_)[¶](https://docs.python.org/3/library/threading.html#threading.Condition "Link to this definition")

This class implements condition variable objects. A condition variable allows one or more threads to wait until they are notified by another thread.
If the _lock_ argument is given and not `None`, it must be a [`Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock") or [`RLock`](https://docs.python.org/3/library/threading.html#threading.RLock "threading.RLock") object, and it is used as the underlying lock. Otherwise, a new `RLock` object is created and used as the underlying lock.
Changed in version 3.3: changed from a factory function to a class.

acquire(_* args_)[¶](https://docs.python.org/3/library/threading.html#threading.Condition.acquire "Link to this definition")

Acquire the underlying lock. This method calls the corresponding method on the underlying lock; the return value is whatever that method returns.

release()[¶](https://docs.python.org/3/library/threading.html#threading.Condition.release "Link to this definition")

Release the underlying lock. This method calls the corresponding method on the underlying lock; there is no return value.

locked()[¶](https://docs.python.org/3/library/threading.html#threading.Condition.locked "Link to this definition")

Return a boolean indicating whether this object is locked right now.
Added in version 3.14.

wait(_timeout =None_)[¶](https://docs.python.org/3/library/threading.html#threading.Condition.wait "Link to this definition")

Wait until notified or until a timeout occurs. If the calling thread has not acquired the lock when this method is called, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised.
This method releases the underlying lock, and then blocks until it is awakened by a [`notify()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify "threading.Condition.notify") or [`notify_all()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify_all "threading.Condition.notify_all") call for the same condition variable in another thread, or until the optional timeout occurs. Once awakened or timed out, it re-acquires the lock and returns.
When the _timeout_ argument is present and not `None`, it should be a floating-point number specifying a timeout for the operation in seconds (or fractions thereof).
When the underlying lock is an [`RLock`](https://docs.python.org/3/library/threading.html#threading.RLock "threading.RLock"), it is not released using its [`release()`](https://docs.python.org/3/library/threading.html#threading.Condition.release "threading.Condition.release") method, since this may not actually unlock the lock when it was acquired multiple times recursively. Instead, an internal interface of the `RLock` class is used, which really unlocks it even when it has been recursively acquired several times. Another internal interface is then used to restore the recursion level when the lock is reacquired.
The return value is `True` unless a given _timeout_ expired, in which case it is `False`.
Changed in version 3.2: Previously, the method always returned `None`.

wait_for(_predicate_ , _timeout =None_)[¶](https://docs.python.org/3/library/threading.html#threading.Condition.wait_for "Link to this definition")

Wait until a condition evaluates to true. _predicate_ should be a callable which result will be interpreted as a boolean value. A _timeout_ may be provided giving the maximum time to wait.
This utility method may call [`wait()`](https://docs.python.org/3/library/threading.html#threading.Condition.wait "threading.Condition.wait") repeatedly until the predicate is satisfied, or until a timeout occurs. The return value is the last return value of the predicate and will evaluate to `False` if the method timed out.
Ignoring the timeout feature, calling this method is roughly equivalent to writing:
Copy```
while not predicate():
    cv.wait()

```

Therefore, the same rules apply as with [`wait()`](https://docs.python.org/3/library/threading.html#threading.Condition.wait "threading.Condition.wait"): The lock must be held when called and is re-acquired on return. The predicate is evaluated with the lock held.
Added in version 3.2.

notify(_n =1_)[¶](https://docs.python.org/3/library/threading.html#threading.Condition.notify "Link to this definition")

By default, wake up one thread waiting on this condition, if any. If the calling thread has not acquired the lock when this method is called, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised.
This method wakes up at most _n_ of the threads waiting for the condition variable; it is a no-op if no threads are waiting.
The current implementation wakes up exactly _n_ threads, if at least _n_ threads are waiting. However, it’s not safe to rely on this behavior. A future, optimized implementation may occasionally wake up more than _n_ threads.
Note: an awakened thread does not actually return from its [`wait()`](https://docs.python.org/3/library/threading.html#threading.Condition.wait "threading.Condition.wait") call until it can reacquire the lock. Since `notify()` does not release the lock, its caller should.

notify_all()[¶](https://docs.python.org/3/library/threading.html#threading.Condition.notify_all "Link to this definition")

Wake up all threads waiting on this condition. This method acts like [`notify()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify "threading.Condition.notify"), but wakes up all waiting threads instead of one. If the calling thread has not acquired the lock when this method is called, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") is raised.
The method `notifyAll` is a deprecated alias for this method.
### Semaphore objects[¶](https://docs.python.org/3/library/threading.html#semaphore-objects "Link to this heading")
This is one of the oldest synchronization primitives in the history of computer science, invented by the early Dutch computer scientist Edsger W. Dijkstra (he used the names `P()` and `V()` instead of [`acquire()`](https://docs.python.org/3/library/threading.html#threading.Semaphore.acquire "threading.Semaphore.acquire") and [`release()`](https://docs.python.org/3/library/threading.html#threading.Semaphore.release "threading.Semaphore.release")).
A semaphore manages an internal counter which is decremented by each [`acquire()`](https://docs.python.org/3/library/threading.html#threading.Semaphore.acquire "threading.Semaphore.acquire") call and incremented by each [`release()`](https://docs.python.org/3/library/threading.html#threading.Semaphore.release "threading.Semaphore.release") call. The counter can never go below zero; when `acquire()` finds that it is zero, it blocks, waiting until some other thread calls `release()`.
Semaphores also support the [context management protocol](https://docs.python.org/3/library/threading.html#with-locks).

_class_ threading.Semaphore(_value =1_)[¶](https://docs.python.org/3/library/threading.html#threading.Semaphore "Link to this definition")

This class implements semaphore objects. A semaphore manages an atomic counter representing the number of [`release()`](https://docs.python.org/3/library/threading.html#threading.Semaphore.release "threading.Semaphore.release") calls minus the number of [`acquire()`](https://docs.python.org/3/library/threading.html#threading.Semaphore.acquire "threading.Semaphore.acquire") calls, plus an initial value. The `acquire()` method blocks if necessary until it can return without making the counter negative. If not given, _value_ defaults to 1.
The optional argument gives the initial _value_ for the internal counter; it defaults to `1`. If the _value_ given is less than 0, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
Changed in version 3.3: changed from a factory function to a class.

acquire(_blocking =True_, _timeout =None_)[¶](https://docs.python.org/3/library/threading.html#threading.Semaphore.acquire "Link to this definition")

Acquire a semaphore.
When invoked without arguments:
  * If the internal counter is larger than zero on entry, decrement it by one and return `True` immediately.
  * If the internal counter is zero on entry, block until awoken by a call to [`release()`](https://docs.python.org/3/library/threading.html#threading.Semaphore.release "threading.Semaphore.release"). Once awoken (and the counter is greater than 0), decrement the counter by 1 and return `True`. Exactly one thread will be awoken by each call to `release()`. The order in which threads are awoken should not be relied on.


When invoked with _blocking_ set to `False`, do not block. If a call without an argument would block, return `False` immediately; otherwise, do the same thing as when called without arguments, and return `True`.
When invoked with a _timeout_ other than `None`, it will block for at most _timeout_ seconds. If acquire does not complete successfully in that interval, return `False`. Return `True` otherwise.
Changed in version 3.2: The _timeout_ parameter is new.

release(_n =1_)[¶](https://docs.python.org/3/library/threading.html#threading.Semaphore.release "Link to this definition")

Release a semaphore, incrementing the internal counter by _n_. When it was zero on entry and other threads are waiting for it to become larger than zero again, wake up _n_ of those threads.
Changed in version 3.9: Added the _n_ parameter to release multiple waiting threads at once.

_class_ threading.BoundedSemaphore(_value =1_)[¶](https://docs.python.org/3/library/threading.html#threading.BoundedSemaphore "Link to this definition")

Class implementing bounded semaphore objects. A bounded semaphore checks to make sure its current value doesn’t exceed its initial value. If it does, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. In most situations semaphores are used to guard resources with limited capacity. If the semaphore is released too many times it’s a sign of a bug. If not given, _value_ defaults to 1.
Changed in version 3.3: changed from a factory function to a class.
###  [`Semaphore`](https://docs.python.org/3/library/threading.html#threading.Semaphore "threading.Semaphore") example[¶](https://docs.python.org/3/library/threading.html#semaphore-example "Link to this heading")
Semaphores are often used to guard resources with limited capacity, for example, a database server. In any situation where the size of the resource is fixed, you should use a bounded semaphore. Before spawning any worker threads, your main thread would initialize the semaphore:
Copy```
maxconnections = 5
# ...
pool_sema = BoundedSemaphore(value=maxconnections)

```

Once spawned, worker threads call the semaphore’s acquire and release methods when they need to connect to the server:
Copy```
with pool_sema:
    conn = connectdb()
    try:
        # ... use connection ...
    finally:
        conn.close()

```

The use of a bounded semaphore reduces the chance that a programming error which causes the semaphore to be released more than it’s acquired will go undetected.
### Event objects[¶](https://docs.python.org/3/library/threading.html#event-objects "Link to this heading")
This is one of the simplest mechanisms for communication between threads: one thread signals an event and other threads wait for it.
An event object manages an internal flag that can be set to true with the [`set()`](https://docs.python.org/3/library/threading.html#threading.Event.set "threading.Event.set") method and reset to false with the [`clear()`](https://docs.python.org/3/library/threading.html#threading.Event.clear "threading.Event.clear") method. The [`wait()`](https://docs.python.org/3/library/threading.html#threading.Event.wait "threading.Event.wait") method blocks until the flag is true.

_class_ threading.Event[¶](https://docs.python.org/3/library/threading.html#threading.Event "Link to this definition")

Class implementing event objects. An event manages a flag that can be set to true with the [`set()`](https://docs.python.org/3/library/threading.html#threading.Event.set "threading.Event.set") method and reset to false with the [`clear()`](https://docs.python.org/3/library/threading.html#threading.Event.clear "threading.Event.clear") method. The [`wait()`](https://docs.python.org/3/library/threading.html#threading.Event.wait "threading.Event.wait") method blocks until the flag is true. The flag is initially false.
Changed in version 3.3: changed from a factory function to a class.

is_set()[¶](https://docs.python.org/3/library/threading.html#threading.Event.is_set "Link to this definition")

Return `True` if and only if the internal flag is true.
The method `isSet` is a deprecated alias for this method.

set()[¶](https://docs.python.org/3/library/threading.html#threading.Event.set "Link to this definition")

Set the internal flag to true. All threads waiting for it to become true are awakened. Threads that call [`wait()`](https://docs.python.org/3/library/threading.html#threading.Event.wait "threading.Event.wait") once the flag is true will not block at all.

clear()[¶](https://docs.python.org/3/library/threading.html#threading.Event.clear "Link to this definition")

Reset the internal flag to false. Subsequently, threads calling [`wait()`](https://docs.python.org/3/library/threading.html#threading.Event.wait "threading.Event.wait") will block until [`set()`](https://docs.python.org/3/library/threading.html#threading.Event.set "threading.Event.set") is called to set the internal flag to true again.

wait(_timeout =None_)[¶](https://docs.python.org/3/library/threading.html#threading.Event.wait "Link to this definition")

Block as long as the internal flag is false and the timeout, if given, has not expired. The return value represents the reason that this blocking method returned; `True` if returning because the internal flag is set to true, or `False` if a timeout is given and the internal flag did not become true within the given wait time.
When the timeout argument is present and not `None`, it should be a floating-point number specifying a timeout for the operation in seconds, or fractions thereof.
Changed in version 3.1: Previously, the method always returned `None`.
### Timer objects[¶](https://docs.python.org/3/library/threading.html#timer-objects "Link to this heading")
This class represents an action that should be run only after a certain amount of time has passed — a timer. [`Timer`](https://docs.python.org/3/library/threading.html#threading.Timer "threading.Timer") is a subclass of [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") and as such also functions as an example of creating custom threads.
Timers are started, as with threads, by calling their [`Timer.start`](https://docs.python.org/3/library/threading.html#threading.Thread.start "threading.Thread.start") method. The timer can be stopped (before its action has begun) by calling the [`cancel()`](https://docs.python.org/3/library/threading.html#threading.Timer.cancel "threading.Timer.cancel") method. The interval the timer will wait before executing its action may not be exactly the same as the interval specified by the user.
For example:
Copy```
def hello():
    print("hello, world")

t = Timer(30.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed

```


_class_ threading.Timer(_interval_ , _function_ , _args =None_, _kwargs =None_)[¶](https://docs.python.org/3/library/threading.html#threading.Timer "Link to this definition")

Create a timer that will run _function_ with arguments _args_ and keyword arguments _kwargs_ , after _interval_ seconds have passed. If _args_ is `None` (the default) then an empty list will be used. If _kwargs_ is `None` (the default) then an empty dict will be used.
Changed in version 3.3: changed from a factory function to a class.

cancel()[¶](https://docs.python.org/3/library/threading.html#threading.Timer.cancel "Link to this definition")

Stop the timer, and cancel the execution of the timer’s action. This will only work if the timer is still in its waiting stage.
### Barrier objects[¶](https://docs.python.org/3/library/threading.html#barrier-objects "Link to this heading")
Added in version 3.2.
This class provides a simple synchronization primitive for use by a fixed number of threads that need to wait for each other. Each of the threads tries to pass the barrier by calling the [`wait()`](https://docs.python.org/3/library/threading.html#threading.Barrier.wait "threading.Barrier.wait") method and will block until all of the threads have made their `wait()` calls. At this point, the threads are released simultaneously.
The barrier can be reused any number of times for the same number of threads.
As an example, here is a simple way to synchronize a client and server thread:
Copy```
b = Barrier(2, timeout=5)

def server():
    start_server()
    b.wait()
    while True:
        connection = accept_connection()
        process_server_connection(connection)

def client():
    b.wait()
    while True:
        connection = make_connection()
        process_client_connection(connection)

```


_class_ threading.Barrier(_parties_ , _action =None_, _timeout =None_)[¶](https://docs.python.org/3/library/threading.html#threading.Barrier "Link to this definition")

Create a barrier object for _parties_ number of threads. An _action_ , when provided, is a callable to be called by one of the threads when they are released. _timeout_ is the default timeout value if none is specified for the [`wait()`](https://docs.python.org/3/library/threading.html#threading.Barrier.wait "threading.Barrier.wait") method.

wait(_timeout =None_)[¶](https://docs.python.org/3/library/threading.html#threading.Barrier.wait "Link to this definition")

Pass the barrier. When all the threads party to the barrier have called this function, they are all released simultaneously. If a _timeout_ is provided, it is used in preference to any that was supplied to the class constructor.
The return value is an integer in the range 0 to _parties_ – 1, different for each thread. This can be used to select a thread to do some special housekeeping, e.g.:
Copy```
i = barrier.wait()
if i == 0:
    # Only one thread needs to print this
    print("passed the barrier")

```

If an _action_ was provided to the constructor, one of the threads will have called it prior to being released. Should this call raise an error, the barrier is put into the broken state.
If the call times out, the barrier is put into the broken state.
This method may raise a [`BrokenBarrierError`](https://docs.python.org/3/library/threading.html#threading.BrokenBarrierError "threading.BrokenBarrierError") exception if the barrier is broken or reset while a thread is waiting.

reset()[¶](https://docs.python.org/3/library/threading.html#threading.Barrier.reset "Link to this definition")

Return the barrier to the default, empty state. Any threads waiting on it will receive the [`BrokenBarrierError`](https://docs.python.org/3/library/threading.html#threading.BrokenBarrierError "threading.BrokenBarrierError") exception.
Note that using this function may require some external synchronization if there are other threads whose state is unknown. If a barrier is broken it may be better to just leave it and create a new one.

abort()[¶](https://docs.python.org/3/library/threading.html#threading.Barrier.abort "Link to this definition")

Put the barrier into a broken state. This causes any active or future calls to [`wait()`](https://docs.python.org/3/library/threading.html#threading.Barrier.wait "threading.Barrier.wait") to fail with the [`BrokenBarrierError`](https://docs.python.org/3/library/threading.html#threading.BrokenBarrierError "threading.BrokenBarrierError"). Use this for example if one of the threads needs to abort, to avoid deadlocking the application.
It may be preferable to simply create the barrier with a sensible _timeout_ value to automatically guard against one of the threads going awry.

parties[¶](https://docs.python.org/3/library/threading.html#threading.Barrier.parties "Link to this definition")

The number of threads required to pass the barrier.

n_waiting[¶](https://docs.python.org/3/library/threading.html#threading.Barrier.n_waiting "Link to this definition")

The number of threads currently waiting in the barrier.

broken[¶](https://docs.python.org/3/library/threading.html#threading.Barrier.broken "Link to this definition")

A boolean that is `True` if the barrier is in the broken state.

_exception_ threading.BrokenBarrierError[¶](https://docs.python.org/3/library/threading.html#threading.BrokenBarrierError "Link to this definition")

This exception, a subclass of [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError"), is raised when the [`Barrier`](https://docs.python.org/3/library/threading.html#threading.Barrier "threading.Barrier") object is reset or broken.
## Using locks, conditions, and semaphores in the `with` statement[¶](https://docs.python.org/3/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement "Link to this heading")
All of the objects provided by this module that have `acquire` and `release` methods can be used as context managers for a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. The `acquire` method will be called when the block is entered, and `release` will be called when the block is exited. Hence, the following snippet:
Copy```
with some_lock:
    # do something...

```

is equivalent to:
Copy```
some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()

```

Currently, [`Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock"), [`RLock`](https://docs.python.org/3/library/threading.html#threading.RLock "threading.RLock"), [`Condition`](https://docs.python.org/3/library/threading.html#threading.Condition "threading.Condition"), [`Semaphore`](https://docs.python.org/3/library/threading.html#threading.Semaphore "threading.Semaphore"), and [`BoundedSemaphore`](https://docs.python.org/3/library/threading.html#threading.BoundedSemaphore "threading.BoundedSemaphore") objects may be used as [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement context managers.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`threading` — Thread-based parallelism](https://docs.python.org/3/library/threading.html)
    * [Introduction](https://docs.python.org/3/library/threading.html#introduction)
    * [GIL and performance considerations](https://docs.python.org/3/library/threading.html#gil-and-performance-considerations)
    * [Reference](https://docs.python.org/3/library/threading.html#reference)
      * [Thread-local data](https://docs.python.org/3/library/threading.html#thread-local-data)
      * [Thread objects](https://docs.python.org/3/library/threading.html#thread-objects)
      * [Lock objects](https://docs.python.org/3/library/threading.html#lock-objects)
      * [RLock objects](https://docs.python.org/3/library/threading.html#rlock-objects)
      * [Condition objects](https://docs.python.org/3/library/threading.html#condition-objects)
      * [Semaphore objects](https://docs.python.org/3/library/threading.html#semaphore-objects)
      * [`Semaphore` example](https://docs.python.org/3/library/threading.html#semaphore-example)
      * [Event objects](https://docs.python.org/3/library/threading.html#event-objects)
      * [Timer objects](https://docs.python.org/3/library/threading.html#timer-objects)
      * [Barrier objects](https://docs.python.org/3/library/threading.html#barrier-objects)
    * [Using locks, conditions, and semaphores in the `with` statement](https://docs.python.org/3/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement)


#### Previous topic
[Concurrent Execution](https://docs.python.org/3/library/concurrency.html "previous chapter")
#### Next topic
[`multiprocessing` — Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=threading+%E2%80%94+Thread-based+parallelism&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fthreading.html&pagesource=library%2Fthreading.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/multiprocessing.html "multiprocessing — Process-based parallelism") |
  * [previous](https://docs.python.org/3/library/concurrency.html "Concurrent Execution") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`threading` — Thread-based parallelism](https://docs.python.org/3/library/threading.html)
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
