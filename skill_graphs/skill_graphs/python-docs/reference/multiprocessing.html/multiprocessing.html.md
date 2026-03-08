[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
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


#### Previous topic
[`threading` — Thread-based parallelism](https://docs.python.org/3/library/threading.html "previous chapter")
#### Next topic
[`multiprocessing.shared_memory` — Shared memory for direct access across processes](https://docs.python.org/3/library/multiprocessing.shared_memory.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=multiprocessing+%E2%80%94+Process-based+parallelism&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmultiprocessing.html&pagesource=library%2Fmultiprocessing.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/multiprocessing.shared_memory.html "multiprocessing.shared_memory — Shared memory for direct access across processes") |
  * [previous](https://docs.python.org/3/library/threading.html "threading — Thread-based parallelism") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`multiprocessing` — Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html)
  * |
  * Theme  Auto Light Dark |
