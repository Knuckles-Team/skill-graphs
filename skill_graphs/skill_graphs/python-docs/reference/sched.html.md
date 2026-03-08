[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`sched` — Event scheduler](https://docs.python.org/3/library/sched.html)
    * [Scheduler Objects](https://docs.python.org/3/library/sched.html#scheduler-objects)


#### Previous topic
[`subprocess` — Subprocess management](https://docs.python.org/3/library/subprocess.html "previous chapter")
#### Next topic
[`queue` — A synchronized queue class](https://docs.python.org/3/library/queue.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=sched+%E2%80%94+Event+scheduler&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsched.html&pagesource=library%2Fsched.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/queue.html "queue — A synchronized queue class") |
  * [previous](https://docs.python.org/3/library/subprocess.html "subprocess — Subprocess management") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`sched` — Event scheduler](https://docs.python.org/3/library/sched.html)
  * |
  * Theme  Auto Light Dark |


#  `sched` — Event scheduler[¶](https://docs.python.org/3/library/sched.html#module-sched "Link to this heading")
**Source code:**
* * *
The `sched` module defines a class which implements a general purpose event scheduler:

_class_ sched.scheduler(_timefunc =time.monotonic_, _delayfunc =time.sleep_)[¶](https://docs.python.org/3/library/sched.html#sched.scheduler "Link to this definition")

The `scheduler` class defines a generic interface to scheduling events. It needs two functions to actually deal with the “outside world” — _timefunc_ should be callable without arguments, and return a number (the “time”, in any units whatsoever). The _delayfunc_ function should be callable with one argument, compatible with the output of _timefunc_ , and should delay that many time units. _delayfunc_ will also be called with the argument `0` after each event is run to allow other threads an opportunity to run in multi-threaded applications.
Changed in version 3.3: _timefunc_ and _delayfunc_ parameters are optional.
Changed in version 3.3: `scheduler` class can be safely used in multi-threaded environments.
Example:
Copy```
>>> import sched, time
>>> s = sched.scheduler(time.time, time.sleep)
>>> def print_time(a='default'):
...     print("From print_time", time.time(), a)
...
>>> def print_some_times():
...     print(time.time())
...     s.enter(10, 1, print_time)
...     s.enter(5, 2, print_time, argument=('positional',))
...     # despite having higher priority, 'keyword' runs after 'positional' as enter() is relative
...     s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
...     s.enterabs(1_650_000_000, 10, print_time, argument=("first enterabs",))
...     s.enterabs(1_650_000_000, 5, print_time, argument=("second enterabs",))
...     s.run()
...     print(time.time())
...
>>> print_some_times()
1652342830.3640375
From print_time 1652342830.3642538 second enterabs
From print_time 1652342830.3643398 first enterabs
From print_time 1652342835.3694863 positional
From print_time 1652342835.3696074 keyword
From print_time 1652342840.369612 default
1652342840.3697174

```

## Scheduler Objects[¶](https://docs.python.org/3/library/sched.html#scheduler-objects "Link to this heading")
[`scheduler`](https://docs.python.org/3/library/sched.html#sched.scheduler "sched.scheduler") instances have the following methods and attributes:

scheduler.enterabs(_time_ , _priority_ , _action_ , _argument =()_, _kwargs ={}_)[¶](https://docs.python.org/3/library/sched.html#sched.scheduler.enterabs "Link to this definition")

Schedule a new event. The _time_ argument should be a numeric type compatible with the return value of the _timefunc_ function passed to the constructor. Events scheduled for the same _time_ will be executed in the order of their _priority_. A lower number represents a higher priority.
Executing the event means executing `action(*argument, **kwargs)`. _argument_ is a sequence holding the positional arguments for _action_. _kwargs_ is a dictionary holding the keyword arguments for _action_.
Return value is an event which may be used for later cancellation of the event (see [`cancel()`](https://docs.python.org/3/library/sched.html#sched.scheduler.cancel "sched.scheduler.cancel")).
Changed in version 3.3: _argument_ parameter is optional.
Changed in version 3.3: _kwargs_ parameter was added.

scheduler.enter(_delay_ , _priority_ , _action_ , _argument =()_, _kwargs ={}_)[¶](https://docs.python.org/3/library/sched.html#sched.scheduler.enter "Link to this definition")

Schedule an event for _delay_ more time units. Other than the relative time, the other arguments, the effect and the return value are the same as those for [`enterabs()`](https://docs.python.org/3/library/sched.html#sched.scheduler.enterabs "sched.scheduler.enterabs").
Changed in version 3.3: _argument_ parameter is optional.
Changed in version 3.3: _kwargs_ parameter was added.

scheduler.cancel(_event_)[¶](https://docs.python.org/3/library/sched.html#sched.scheduler.cancel "Link to this definition")

Remove the event from the queue. If _event_ is not an event currently in the queue, this method will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

scheduler.empty()[¶](https://docs.python.org/3/library/sched.html#sched.scheduler.empty "Link to this definition")

Return `True` if the event queue is empty.

scheduler.run(_blocking =True_)[¶](https://docs.python.org/3/library/sched.html#sched.scheduler.run "Link to this definition")

Run all scheduled events. This method will wait (using the _delayfunc_ function passed to the constructor) for the next event, then execute it and so on until there are no more scheduled events.
If _blocking_ is false executes the scheduled events due to expire soonest (if any) and then return the deadline of the next scheduled call in the scheduler (if any).
Either _action_ or _delayfunc_ can raise an exception. In either case, the scheduler will maintain a consistent state and propagate the exception. If an exception is raised by _action_ , the event will not be attempted in future calls to `run()`.
If a sequence of events takes longer to run than the time available before the next event, the scheduler will simply fall behind. No events will be dropped; the calling code is responsible for canceling events which are no longer pertinent.
Changed in version 3.3: _blocking_ parameter was added.

scheduler.queue[¶](https://docs.python.org/3/library/sched.html#sched.scheduler.queue "Link to this definition")

Read-only attribute returning a list of upcoming events in the order they will be run. Each event is shown as a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) with the following fields: time, priority, action, argument, kwargs.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`sched` — Event scheduler](https://docs.python.org/3/library/sched.html)
    * [Scheduler Objects](https://docs.python.org/3/library/sched.html#scheduler-objects)


#### Previous topic
[`subprocess` — Subprocess management](https://docs.python.org/3/library/subprocess.html "previous chapter")
#### Next topic
[`queue` — A synchronized queue class](https://docs.python.org/3/library/queue.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=sched+%E2%80%94+Event+scheduler&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsched.html&pagesource=library%2Fsched.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/queue.html "queue — A synchronized queue class") |
  * [previous](https://docs.python.org/3/library/subprocess.html "subprocess — Subprocess management") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`sched` — Event scheduler](https://docs.python.org/3/library/sched.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
