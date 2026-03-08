[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`cmd` — Support for line-oriented command interpreters](https://docs.python.org/3/library/cmd.html "previous chapter")
#### Next topic
[`threading` — Thread-based parallelism](https://docs.python.org/3/library/threading.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Concurrent+Execution&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fconcurrency.html&pagesource=library%2Fconcurrency.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/threading.html "threading — Thread-based parallelism") |
  * [previous](https://docs.python.org/3/library/cmd.html "cmd — Support for line-oriented command interpreters") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html)
  * |
  * Theme  Auto Light Dark |


# Concurrent Execution[¶](https://docs.python.org/3/library/concurrency.html#concurrent-execution "Link to this heading")
The modules described in this chapter provide support for concurrent execution of code. The appropriate choice of tool will depend on the task to be executed (CPU bound vs IO bound) and preferred style of development (event driven cooperative multitasking vs preemptive multitasking). Here’s an overview:
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
  * [`multiprocessing` — Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html)
    * [Introduction](https://docs.python.org/3/library/multiprocessing.html#introduction)
      * [The `Process` class](https://docs.python.org/3/library/multiprocessing.html#the-process-class)
      * [Contexts and start methods](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods)
      * [Exchanging objects between processes](https://docs.python.org/3/library/multiprocessing.html#exchanging-objects-between-processes)
      * [Synchronization between processes](https://docs.python.org/3/library/multiprocessing.html#synchronization-between-processes)
      * [Sharing state between processes](https://docs.python.org/3/library/multiprocessing.html#sharing-state-between-processes)
      * [Using a pool of workers](https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers)
    * [Reference](https://docs.python.org/3/library/multiprocessing.html#reference)
      * [Global start method](https://docs.python.org/3/library/multiprocessing.html#global-start-method)
      * [`Process` and exceptions](https://docs.python.org/3/library/multiprocessing.html#process-and-exceptions)
      * [Pipes and Queues](https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues)
      * [Miscellaneous](https://docs.python.org/3/library/multiprocessing.html#miscellaneous)
      * [Connection Objects](https://docs.python.org/3/library/multiprocessing.html#connection-objects)
      * [Synchronization primitives](https://docs.python.org/3/library/multiprocessing.html#synchronization-primitives)
      * [Shared `ctypes` Objects](https://docs.python.org/3/library/multiprocessing.html#shared-ctypes-objects)
        * [The `multiprocessing.sharedctypes` module](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.sharedctypes)
      * [Managers](https://docs.python.org/3/library/multiprocessing.html#managers)
        * [Customized managers](https://docs.python.org/3/library/multiprocessing.html#customized-managers)
        * [Using a remote manager](https://docs.python.org/3/library/multiprocessing.html#using-a-remote-manager)
      * [Proxy Objects](https://docs.python.org/3/library/multiprocessing.html#proxy-objects)
        * [Cleanup](https://docs.python.org/3/library/multiprocessing.html#cleanup)
      * [Process Pools](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.pool)
      * [Listeners and Clients](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.connection)
        * [Address Formats](https://docs.python.org/3/library/multiprocessing.html#address-formats)
      * [Authentication keys](https://docs.python.org/3/library/multiprocessing.html#authentication-keys)
      * [Logging](https://docs.python.org/3/library/multiprocessing.html#logging)
      * [The `multiprocessing.dummy` module](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.dummy)
    * [Programming guidelines](https://docs.python.org/3/library/multiprocessing.html#programming-guidelines)
      * [All start methods](https://docs.python.org/3/library/multiprocessing.html#all-start-methods)
      * [The _spawn_ and _forkserver_ start methods](https://docs.python.org/3/library/multiprocessing.html#the-spawn-and-forkserver-start-methods)
    * [Examples](https://docs.python.org/3/library/multiprocessing.html#examples)
  * [`multiprocessing.shared_memory` — Shared memory for direct access across processes](https://docs.python.org/3/library/multiprocessing.shared_memory.html)
  * [The `concurrent` package](https://docs.python.org/3/library/concurrent.html)
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
  * [`concurrent.interpreters` — Multiple interpreters in the same process](https://docs.python.org/3/library/concurrent.interpreters.html)
    * [Key details](https://docs.python.org/3/library/concurrent.interpreters.html#key-details)
    * [Introduction](https://docs.python.org/3/library/concurrent.interpreters.html#introduction)
      * [Multiple Interpreters and Isolation](https://docs.python.org/3/library/concurrent.interpreters.html#multiple-interpreters-and-isolation)
      * [Running in an Interpreter](https://docs.python.org/3/library/concurrent.interpreters.html#running-in-an-interpreter)
      * [Concurrency and Parallelism](https://docs.python.org/3/library/concurrent.interpreters.html#concurrency-and-parallelism)
      * [Communication Between Interpreters](https://docs.python.org/3/library/concurrent.interpreters.html#communication-between-interpreters)
      * [“Sharing” Objects](https://docs.python.org/3/library/concurrent.interpreters.html#sharing-objects)
    * [Reference](https://docs.python.org/3/library/concurrent.interpreters.html#reference)
      * [Interpreter objects](https://docs.python.org/3/library/concurrent.interpreters.html#interpreter-objects)
      * [Exceptions](https://docs.python.org/3/library/concurrent.interpreters.html#exceptions)
      * [Communicating Between Interpreters](https://docs.python.org/3/library/concurrent.interpreters.html#communicating-between-interpreters)
    * [Basic usage](https://docs.python.org/3/library/concurrent.interpreters.html#basic-usage)
  * [`subprocess` — Subprocess management](https://docs.python.org/3/library/subprocess.html)
    * [Using the `subprocess` Module](https://docs.python.org/3/library/subprocess.html#using-the-subprocess-module)
      * [Frequently Used Arguments](https://docs.python.org/3/library/subprocess.html#frequently-used-arguments)
      * [Popen Constructor](https://docs.python.org/3/library/subprocess.html#popen-constructor)
      * [Exceptions](https://docs.python.org/3/library/subprocess.html#exceptions)
    * [Security Considerations](https://docs.python.org/3/library/subprocess.html#security-considerations)
    * [Popen Objects](https://docs.python.org/3/library/subprocess.html#popen-objects)
    * [Windows Popen Helpers](https://docs.python.org/3/library/subprocess.html#windows-popen-helpers)
      * [Windows Constants](https://docs.python.org/3/library/subprocess.html#windows-constants)
    * [Older high-level API](https://docs.python.org/3/library/subprocess.html#older-high-level-api)
    * [Replacing Older Functions with the `subprocess` Module](https://docs.python.org/3/library/subprocess.html#replacing-older-functions-with-the-subprocess-module)
      * [Replacing **/bin/sh** shell command substitution](https://docs.python.org/3/library/subprocess.html#replacing-bin-sh-shell-command-substitution)
      * [Replacing shell pipeline](https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline)
      * [Replacing `os.system()`](https://docs.python.org/3/library/subprocess.html#replacing-os-system)
      * [Replacing the `os.spawn` family](https://docs.python.org/3/library/subprocess.html#replacing-the-os-spawn-family)
      * [Replacing `os.popen()`](https://docs.python.org/3/library/subprocess.html#replacing-os-popen)
    * [Legacy Shell Invocation Functions](https://docs.python.org/3/library/subprocess.html#legacy-shell-invocation-functions)
    * [Notes](https://docs.python.org/3/library/subprocess.html#notes)
      * [Timeout Behavior](https://docs.python.org/3/library/subprocess.html#timeout-behavior)
      * [Converting an argument sequence to a string on Windows](https://docs.python.org/3/library/subprocess.html#converting-an-argument-sequence-to-a-string-on-windows)
      * [Disable use of `posix_spawn()`](https://docs.python.org/3/library/subprocess.html#disable-use-of-posix-spawn)
  * [`sched` — Event scheduler](https://docs.python.org/3/library/sched.html)
    * [Scheduler Objects](https://docs.python.org/3/library/sched.html#scheduler-objects)
  * [`queue` — A synchronized queue class](https://docs.python.org/3/library/queue.html)
    * [Queue Objects](https://docs.python.org/3/library/queue.html#queue-objects)
      * [Waiting for task completion](https://docs.python.org/3/library/queue.html#waiting-for-task-completion)
      * [Terminating queues](https://docs.python.org/3/library/queue.html#terminating-queues)
    * [SimpleQueue Objects](https://docs.python.org/3/library/queue.html#simplequeue-objects)
  * [`contextvars` — Context Variables](https://docs.python.org/3/library/contextvars.html)
    * [Context Variables](https://docs.python.org/3/library/contextvars.html#context-variables)
    * [Manual Context Management](https://docs.python.org/3/library/contextvars.html#manual-context-management)
    * [asyncio support](https://docs.python.org/3/library/contextvars.html#asyncio-support)


The following are support modules for some of the above services:
  * [`_thread` — Low-level threading API](https://docs.python.org/3/library/_thread.html)


#### Previous topic
[`cmd` — Support for line-oriented command interpreters](https://docs.python.org/3/library/cmd.html "previous chapter")
#### Next topic
[`threading` — Thread-based parallelism](https://docs.python.org/3/library/threading.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Concurrent+Execution&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fconcurrency.html&pagesource=library%2Fconcurrency.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/threading.html "threading — Thread-based parallelism") |
  * [previous](https://docs.python.org/3/library/cmd.html "cmd — Support for line-oriented command interpreters") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
