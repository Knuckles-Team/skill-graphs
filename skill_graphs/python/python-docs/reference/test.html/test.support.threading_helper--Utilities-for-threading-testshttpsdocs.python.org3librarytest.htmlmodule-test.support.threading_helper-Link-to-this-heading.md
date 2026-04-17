#  `test.support.threading_helper` — Utilities for threading tests[¶](https://docs.python.org/3/library/test.html#module-test.support.threading_helper "Link to this heading")
The `test.support.threading_helper` module provides support for threading tests.
Added in version 3.10.

test.support.threading_helper.join_thread(_thread_ , _timeout =None_)[¶](https://docs.python.org/3/library/test.html#test.support.threading_helper.join_thread "Link to this definition")

Join a _thread_ within _timeout_. Raise an [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") if thread is still alive after _timeout_ seconds.

@test.support.threading_helper.reap_threads[¶](https://docs.python.org/3/library/test.html#test.support.threading_helper.reap_threads "Link to this definition")

Decorator to ensure the threads are cleaned up even if the test fails.

test.support.threading_helper.start_threads(_threads_ , _unlock =None_)[¶](https://docs.python.org/3/library/test.html#test.support.threading_helper.start_threads "Link to this definition")

Context manager to start _threads_ , which is a sequence of threads. _unlock_ is a function called after the threads are started, even if an exception was raised; an example would be [`threading.Event.set()`](https://docs.python.org/3/library/threading.html#threading.Event.set "threading.Event.set"). `start_threads` will attempt to join the started threads upon exit.

test.support.threading_helper.threading_cleanup(_* original_values_)[¶](https://docs.python.org/3/library/test.html#test.support.threading_helper.threading_cleanup "Link to this definition")

Cleanup up threads not specified in _original_values_. Designed to emit a warning if a test leaves running threads in the background.

test.support.threading_helper.threading_setup()[¶](https://docs.python.org/3/library/test.html#test.support.threading_helper.threading_setup "Link to this definition")

Return current thread count and copy of dangling threads.

test.support.threading_helper.wait_threads_exit(_timeout =None_)[¶](https://docs.python.org/3/library/test.html#test.support.threading_helper.wait_threads_exit "Link to this definition")

Context manager to wait until all threads created in the `with` statement exit.

test.support.threading_helper.catch_threading_exception()[¶](https://docs.python.org/3/library/test.html#test.support.threading_helper.catch_threading_exception "Link to this definition")

Context manager catching [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread") exception using [`threading.excepthook()`](https://docs.python.org/3/library/threading.html#threading.excepthook "threading.excepthook").
Attributes set when an exception is caught:
  * `exc_type`
  * `exc_value`
  * `exc_traceback`
  * `thread`


See [`threading.excepthook()`](https://docs.python.org/3/library/threading.html#threading.excepthook "threading.excepthook") documentation.
These attributes are deleted at the context manager exit.
Usage:
Copy```
with threading_helper.catch_threading_exception() as cm:
    # code spawning a thread which raises an exception
    ...

    # check the thread exception, use cm attributes:
    # exc_type, exc_value, exc_traceback, thread
    ...
