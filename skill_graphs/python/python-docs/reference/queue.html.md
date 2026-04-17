[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`queue` — A synchronized queue class](https://docs.python.org/3/library/queue.html)
    * [Queue Objects](https://docs.python.org/3/library/queue.html#queue-objects)
      * [Waiting for task completion](https://docs.python.org/3/library/queue.html#waiting-for-task-completion)
      * [Terminating queues](https://docs.python.org/3/library/queue.html#terminating-queues)
    * [SimpleQueue Objects](https://docs.python.org/3/library/queue.html#simplequeue-objects)


#### Previous topic
[`sched` — Event scheduler](https://docs.python.org/3/library/sched.html "previous chapter")
#### Next topic
[`contextvars` — Context Variables](https://docs.python.org/3/library/contextvars.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=queue+%E2%80%94+A+synchronized+queue+class&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fqueue.html&pagesource=library%2Fqueue.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/contextvars.html "contextvars — Context Variables") |
  * [previous](https://docs.python.org/3/library/sched.html "sched — Event scheduler") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`queue` — A synchronized queue class](https://docs.python.org/3/library/queue.html)
  * |
  * Theme  Auto Light Dark |


#  `queue` — A synchronized queue class[¶](https://docs.python.org/3/library/queue.html#module-queue "Link to this heading")
**Source code:**
* * *
The `queue` module implements multi-producer, multi-consumer queues. It is especially useful in threaded programming when information must be exchanged safely between multiple threads. The [`Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") class in this module implements all the required locking semantics.
The module implements three types of queue, which differ only in the order in which the entries are retrieved. In a FIFO queue, the first tasks added are the first retrieved. In a LIFO queue, the most recently added entry is the first retrieved (operating like a stack). With a priority queue, the entries are kept sorted (using the [`heapq`](https://docs.python.org/3/library/heapq.html#module-heapq "heapq: Heap queue algorithm \(a.k.a. priority queue\).") module) and the lowest valued entry is retrieved first.
Internally, those three types of queues use locks to temporarily block competing threads; however, they are not designed to handle reentrancy within a thread.
In addition, the module implements a “simple” FIFO queue type, [`SimpleQueue`](https://docs.python.org/3/library/queue.html#queue.SimpleQueue "queue.SimpleQueue"), whose specific implementation provides additional guarantees in exchange for the smaller functionality.
The `queue` module defines the following classes and exceptions:

_class_ queue.Queue(_maxsize =0_)[¶](https://docs.python.org/3/library/queue.html#queue.Queue "Link to this definition")

Constructor for a FIFO queue. _maxsize_ is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If _maxsize_ is less than or equal to zero, the queue size is infinite.

_class_ queue.LifoQueue(_maxsize =0_)[¶](https://docs.python.org/3/library/queue.html#queue.LifoQueue "Link to this definition")

Constructor for a LIFO queue. _maxsize_ is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If _maxsize_ is less than or equal to zero, the queue size is infinite.

_class_ queue.PriorityQueue(_maxsize =0_)[¶](https://docs.python.org/3/library/queue.html#queue.PriorityQueue "Link to this definition")

Constructor for a priority queue. _maxsize_ is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If _maxsize_ is less than or equal to zero, the queue size is infinite.
The lowest valued entries are retrieved first (the lowest valued entry is the one that would be returned by `min(entries)`). A typical pattern for entries is a tuple in the form: `(priority_number, data)`.
If the _data_ elements are not comparable, the data can be wrapped in a class that ignores the data item and only compares the priority number:
Copy```
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

```


_class_ queue.SimpleQueue[¶](https://docs.python.org/3/library/queue.html#queue.SimpleQueue "Link to this definition")

Constructor for an unbounded FIFO queue. Simple queues lack advanced functionality such as task tracking.
Added in version 3.7.

_exception_ queue.Empty[¶](https://docs.python.org/3/library/queue.html#queue.Empty "Link to this definition")

Exception raised when non-blocking [`get()`](https://docs.python.org/3/library/queue.html#queue.Queue.get "queue.Queue.get") (or [`get_nowait()`](https://docs.python.org/3/library/queue.html#queue.Queue.get_nowait "queue.Queue.get_nowait")) is called on a [`Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") object which is empty.

_exception_ queue.Full[¶](https://docs.python.org/3/library/queue.html#queue.Full "Link to this definition")

Exception raised when non-blocking [`put()`](https://docs.python.org/3/library/queue.html#queue.Queue.put "queue.Queue.put") (or [`put_nowait()`](https://docs.python.org/3/library/queue.html#queue.Queue.put_nowait "queue.Queue.put_nowait")) is called on a [`Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") object which is full.

_exception_ queue.ShutDown[¶](https://docs.python.org/3/library/queue.html#queue.ShutDown "Link to this definition")

Exception raised when [`put()`](https://docs.python.org/3/library/queue.html#queue.Queue.put "queue.Queue.put") or [`get()`](https://docs.python.org/3/library/queue.html#queue.Queue.get "queue.Queue.get") is called on a [`Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") object which has been shut down.
Added in version 3.13.
## Queue Objects[¶](https://docs.python.org/3/library/queue.html#queue-objects "Link to this heading")
Queue objects ([`Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue"), [`LifoQueue`](https://docs.python.org/3/library/queue.html#queue.LifoQueue "queue.LifoQueue"), or [`PriorityQueue`](https://docs.python.org/3/library/queue.html#queue.PriorityQueue "queue.PriorityQueue")) provide the public methods described below.

Queue.qsize()[¶](https://docs.python.org/3/library/queue.html#queue.Queue.qsize "Link to this definition")

Return the approximate size of the queue. Note, qsize() > 0 doesn’t guarantee that a subsequent get() will not block, nor will qsize() < maxsize guarantee that put() will not block.

Queue.empty()[¶](https://docs.python.org/3/library/queue.html#queue.Queue.empty "Link to this definition")

Return `True` if the queue is empty, `False` otherwise. If empty() returns `True` it doesn’t guarantee that a subsequent call to put() will not block. Similarly, if empty() returns `False` it doesn’t guarantee that a subsequent call to get() will not block.

Queue.full()[¶](https://docs.python.org/3/library/queue.html#queue.Queue.full "Link to this definition")

Return `True` if the queue is full, `False` otherwise. If full() returns `True` it doesn’t guarantee that a subsequent call to get() will not block. Similarly, if full() returns `False` it doesn’t guarantee that a subsequent call to put() will not block.

Queue.put(_item_ , _block =True_, _timeout =None_)[¶](https://docs.python.org/3/library/queue.html#queue.Queue.put "Link to this definition")

Put _item_ into the queue. If optional args _block_ is true and _timeout_ is `None` (the default), block if necessary until a free slot is available. If _timeout_ is a positive number, it blocks at most _timeout_ seconds and raises the [`Full`](https://docs.python.org/3/library/queue.html#queue.Full "queue.Full") exception if no free slot was available within that time. Otherwise (_block_ is false), put an item on the queue if a free slot is immediately available, else raise the `Full` exception (_timeout_ is ignored in that case).
Raises [`ShutDown`](https://docs.python.org/3/library/queue.html#queue.ShutDown "queue.ShutDown") if the queue has been shut down.

Queue.put_nowait(_item_)[¶](https://docs.python.org/3/library/queue.html#queue.Queue.put_nowait "Link to this definition")

Equivalent to `put(item, block=False)`.

Queue.get(_block =True_, _timeout =None_)[¶](https://docs.python.org/3/library/queue.html#queue.Queue.get "Link to this definition")

Remove and return an item from the queue. If optional args _block_ is true and _timeout_ is `None` (the default), block if necessary until an item is available. If _timeout_ is a positive number, it blocks at most _timeout_ seconds and raises the [`Empty`](https://docs.python.org/3/library/queue.html#queue.Empty "queue.Empty") exception if no item was available within that time. Otherwise (_block_ is false), return an item if one is immediately available, else raise the `Empty` exception (_timeout_ is ignored in that case).
Prior to 3.0 on POSIX systems, and for all versions on Windows, if _block_ is true and _timeout_ is `None`, this operation goes into an uninterruptible wait on an underlying lock. This means that no exceptions can occur, and in particular a SIGINT will not trigger a [`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt "KeyboardInterrupt").
Raises [`ShutDown`](https://docs.python.org/3/library/queue.html#queue.ShutDown "queue.ShutDown") if the queue has been shut down and is empty, or if the queue has been shut down immediately.

Queue.get_nowait()[¶](https://docs.python.org/3/library/queue.html#queue.Queue.get_nowait "Link to this definition")

Equivalent to `get(False)`.
Two methods are offered to support tracking whether enqueued tasks have been fully processed by daemon consumer threads.

Queue.task_done()[¶](https://docs.python.org/3/library/queue.html#queue.Queue.task_done "Link to this definition")

Indicate that a formerly enqueued task is complete. Used by queue consumer threads. For each [`get()`](https://docs.python.org/3/library/queue.html#queue.Queue.get "queue.Queue.get") used to fetch a task, a subsequent call to `task_done()` tells the queue that the processing on the task is complete.
If a [`join()`](https://docs.python.org/3/library/queue.html#queue.Queue.join "queue.Queue.join") is currently blocking, it will resume when all items have been processed (meaning that a `task_done()` call was received for every item that had been [`put()`](https://docs.python.org/3/library/queue.html#queue.Queue.put "queue.Queue.put") into the queue).
Raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if called more times than there were items placed in the queue.

Queue.join()[¶](https://docs.python.org/3/library/queue.html#queue.Queue.join "Link to this definition")

Blocks until all items in the queue have been gotten and processed.
The count of unfinished tasks goes up whenever an item is added to the queue. The count goes down whenever a consumer thread calls [`task_done()`](https://docs.python.org/3/library/queue.html#queue.Queue.task_done "queue.Queue.task_done") to indicate that the item was retrieved and all work on it is complete. When the count of unfinished tasks drops to zero, `join()` unblocks.
### Waiting for task completion[¶](https://docs.python.org/3/library/queue.html#waiting-for-task-completion "Link to this heading")
Example of how to wait for enqueued tasks to be completed:
Copy```
import threading
import queue

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
for item in range(30):
    q.put(item)

# Block until all tasks are done.
q.join()
print('All work completed')

```

### Terminating queues[¶](https://docs.python.org/3/library/queue.html#terminating-queues "Link to this heading")
When no longer needed, [`Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") objects can be wound down until empty or terminated immediately with a hard shutdown.

Queue.shutdown(_immediate =False_)[¶](https://docs.python.org/3/library/queue.html#queue.Queue.shutdown "Link to this definition")

Put a [`Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") instance into a shutdown mode.
The queue can no longer grow. Future calls to [`put()`](https://docs.python.org/3/library/queue.html#queue.Queue.put "queue.Queue.put") raise [`ShutDown`](https://docs.python.org/3/library/queue.html#queue.ShutDown "queue.ShutDown"). Currently blocked callers of `put()` will be unblocked and will raise `ShutDown` in the formerly blocked thread.
If _immediate_ is false (the default), the queue can be wound down normally with [`get()`](https://docs.python.org/3/library/queue.html#queue.Queue.get "queue.Queue.get") calls to extract tasks that have already been loaded.
And if [`task_done()`](https://docs.python.org/3/library/queue.html#queue.Queue.task_done "queue.Queue.task_done") is called for each remaining task, a pending [`join()`](https://docs.python.org/3/library/queue.html#queue.Queue.join "queue.Queue.join") will be unblocked normally.
Once the queue is empty, future calls to [`get()`](https://docs.python.org/3/library/queue.html#queue.Queue.get "queue.Queue.get") will raise [`ShutDown`](https://docs.python.org/3/library/queue.html#queue.ShutDown "queue.ShutDown").
If _immediate_ is true, the queue is terminated immediately. The queue is drained to be completely empty and the count of unfinished tasks is reduced by the number of tasks drained. If unfinished tasks is zero, callers of [`join()`](https://docs.python.org/3/library/queue.html#queue.Queue.join "queue.Queue.join") are unblocked. Also, blocked callers of [`get()`](https://docs.python.org/3/library/queue.html#queue.Queue.get "queue.Queue.get") are unblocked and will raise [`ShutDown`](https://docs.python.org/3/library/queue.html#queue.ShutDown "queue.ShutDown") because the queue is empty.
Use caution when using [`join()`](https://docs.python.org/3/library/queue.html#queue.Queue.join "queue.Queue.join") with _immediate_ set to true. This unblocks the join even when no work has been done on the tasks, violating the usual invariant for joining a queue.
Added in version 3.13.
## SimpleQueue Objects[¶](https://docs.python.org/3/library/queue.html#simplequeue-objects "Link to this heading")
[`SimpleQueue`](https://docs.python.org/3/library/queue.html#queue.SimpleQueue "queue.SimpleQueue") objects provide the public methods described below.

SimpleQueue.qsize()[¶](https://docs.python.org/3/library/queue.html#queue.SimpleQueue.qsize "Link to this definition")

Return the approximate size of the queue. Note, qsize() > 0 doesn’t guarantee that a subsequent get() will not block.

SimpleQueue.empty()[¶](https://docs.python.org/3/library/queue.html#queue.SimpleQueue.empty "Link to this definition")

Return `True` if the queue is empty, `False` otherwise. If empty() returns `False` it doesn’t guarantee that a subsequent call to get() will not block.

SimpleQueue.put(_item_ , _block =True_, _timeout =None_)[¶](https://docs.python.org/3/library/queue.html#queue.SimpleQueue.put "Link to this definition")

Put _item_ into the queue. The method never blocks and always succeeds (except for potential low-level errors such as failure to allocate memory). The optional args _block_ and _timeout_ are ignored and only provided for compatibility with [`Queue.put()`](https://docs.python.org/3/library/queue.html#queue.Queue.put "queue.Queue.put").
**CPython implementation detail:** This method has a C implementation which is reentrant. That is, a `put()` or `get()` call can be interrupted by another `put()` call in the same thread without deadlocking or corrupting internal state inside the queue. This makes it appropriate for use in destructors such as `__del__` methods or [`weakref`](https://docs.python.org/3/library/weakref.html#module-weakref "weakref: Support for weak references and weak dictionaries.") callbacks.

SimpleQueue.put_nowait(_item_)[¶](https://docs.python.org/3/library/queue.html#queue.SimpleQueue.put_nowait "Link to this definition")

Equivalent to `put(item, block=False)`, provided for compatibility with [`Queue.put_nowait()`](https://docs.python.org/3/library/queue.html#queue.Queue.put_nowait "queue.Queue.put_nowait").

SimpleQueue.get(_block =True_, _timeout =None_)[¶](https://docs.python.org/3/library/queue.html#queue.SimpleQueue.get "Link to this definition")

Remove and return an item from the queue. If optional args _block_ is true and _timeout_ is `None` (the default), block if necessary until an item is available. If _timeout_ is a positive number, it blocks at most _timeout_ seconds and raises the [`Empty`](https://docs.python.org/3/library/queue.html#queue.Empty "queue.Empty") exception if no item was available within that time. Otherwise (_block_ is false), return an item if one is immediately available, else raise the `Empty` exception (_timeout_ is ignored in that case).

SimpleQueue.get_nowait()[¶](https://docs.python.org/3/library/queue.html#queue.SimpleQueue.get_nowait "Link to this definition")

Equivalent to `get(False)`.
See also

Class [`multiprocessing.Queue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue "multiprocessing.Queue")

A queue class for use in a multi-processing (rather than multi-threading) context.
[`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque") is an alternative implementation of unbounded queues with fast atomic [`append()`](https://docs.python.org/3/library/collections.html#collections.deque.append "collections.deque.append") and [`popleft()`](https://docs.python.org/3/library/collections.html#collections.deque.popleft "collections.deque.popleft") operations that do not require locking and also support indexing.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`queue` — A synchronized queue class](https://docs.python.org/3/library/queue.html)
    * [Queue Objects](https://docs.python.org/3/library/queue.html#queue-objects)
      * [Waiting for task completion](https://docs.python.org/3/library/queue.html#waiting-for-task-completion)
      * [Terminating queues](https://docs.python.org/3/library/queue.html#terminating-queues)
    * [SimpleQueue Objects](https://docs.python.org/3/library/queue.html#simplequeue-objects)


#### Previous topic
[`sched` — Event scheduler](https://docs.python.org/3/library/sched.html "previous chapter")
#### Next topic
[`contextvars` — Context Variables](https://docs.python.org/3/library/contextvars.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=queue+%E2%80%94+A+synchronized+queue+class&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fqueue.html&pagesource=library%2Fqueue.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/contextvars.html "contextvars — Context Variables") |
  * [previous](https://docs.python.org/3/library/sched.html "sched — Event scheduler") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`queue` — A synchronized queue class](https://docs.python.org/3/library/queue.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[FIFO]: first-in, first-out
  *[LIFO]: last-in, first-out
