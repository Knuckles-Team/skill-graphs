[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`test` — Regression tests package for Python](https://docs.python.org/3/library/test.html "previous chapter")
#### Next topic
[Audit events table](https://docs.python.org/3/library/audit_events.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Debugging+and+Profiling&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdebug.html&pagesource=library%2Fdebug.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/audit_events.html "Audit events table") |
  * [previous](https://docs.python.org/3/library/test.html "test — Regression tests package for Python") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html)
  * |
  * Theme  Auto Light Dark |


# Debugging and Profiling[¶](https://docs.python.org/3/library/debug.html#debugging-and-profiling "Link to this heading")
These libraries help you with Python development: the debugger enables you to step through code, analyze stack frames and set breakpoints etc., and the profilers run code and give you a detailed breakdown of execution times, allowing you to identify bottlenecks in your programs. Auditing events provide visibility into runtime behaviors that would otherwise require intrusive debugging or patching.
  * [Audit events table](https://docs.python.org/3/library/audit_events.html)
  * [`bdb` — Debugger framework](https://docs.python.org/3/library/bdb.html)
  * [`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html)
    * [Dumping the traceback](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback)
    * [Dumping the C stack](https://docs.python.org/3/library/faulthandler.html#dumping-the-c-stack)
      * [C Stack Compatibility](https://docs.python.org/3/library/faulthandler.html#c-stack-compatibility)
    * [Fault handler state](https://docs.python.org/3/library/faulthandler.html#fault-handler-state)
    * [Dumping the tracebacks after a timeout](https://docs.python.org/3/library/faulthandler.html#dumping-the-tracebacks-after-a-timeout)
    * [Dumping the traceback on a user signal](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback-on-a-user-signal)
    * [Issue with file descriptors](https://docs.python.org/3/library/faulthandler.html#issue-with-file-descriptors)
    * [Example](https://docs.python.org/3/library/faulthandler.html#example)
  * [`pdb` — The Python Debugger](https://docs.python.org/3/library/pdb.html)
    * [Command-line interface](https://docs.python.org/3/library/pdb.html#command-line-interface)
    * [Debugger commands](https://docs.python.org/3/library/pdb.html#debugger-commands)
  * [The Python Profilers](https://docs.python.org/3/library/profile.html)
    * [Introduction to the profilers](https://docs.python.org/3/library/profile.html#introduction-to-the-profilers)
    * [Instant User’s Manual](https://docs.python.org/3/library/profile.html#instant-user-s-manual)
    * [`profile` and `cProfile` Module Reference](https://docs.python.org/3/library/profile.html#module-cProfile)
    * [The `Stats` Class](https://docs.python.org/3/library/profile.html#the-stats-class)
    * [What Is Deterministic Profiling?](https://docs.python.org/3/library/profile.html#what-is-deterministic-profiling)
    * [Limitations](https://docs.python.org/3/library/profile.html#limitations)
    * [Calibration](https://docs.python.org/3/library/profile.html#calibration)
    * [Using a custom timer](https://docs.python.org/3/library/profile.html#using-a-custom-timer)
  * [`timeit` — Measure execution time of small code snippets](https://docs.python.org/3/library/timeit.html)
    * [Basic Examples](https://docs.python.org/3/library/timeit.html#basic-examples)
    * [Python Interface](https://docs.python.org/3/library/timeit.html#python-interface)
    * [Command-Line Interface](https://docs.python.org/3/library/timeit.html#command-line-interface)
    * [Examples](https://docs.python.org/3/library/timeit.html#examples)
  * [`trace` — Trace or track Python statement execution](https://docs.python.org/3/library/trace.html)
    * [Command-Line Usage](https://docs.python.org/3/library/trace.html#command-line-usage)
      * [Main options](https://docs.python.org/3/library/trace.html#main-options)
      * [Modifiers](https://docs.python.org/3/library/trace.html#modifiers)
      * [Filters](https://docs.python.org/3/library/trace.html#filters)
    * [Programmatic Interface](https://docs.python.org/3/library/trace.html#programmatic-interface)
  * [`tracemalloc` — Trace memory allocations](https://docs.python.org/3/library/tracemalloc.html)
    * [Examples](https://docs.python.org/3/library/tracemalloc.html#examples)
      * [Display the top 10](https://docs.python.org/3/library/tracemalloc.html#display-the-top-10)
      * [Compute differences](https://docs.python.org/3/library/tracemalloc.html#compute-differences)
      * [Get the traceback of a memory block](https://docs.python.org/3/library/tracemalloc.html#get-the-traceback-of-a-memory-block)
      * [Pretty top](https://docs.python.org/3/library/tracemalloc.html#pretty-top)
        * [Record the current and peak size of all traced memory blocks](https://docs.python.org/3/library/tracemalloc.html#record-the-current-and-peak-size-of-all-traced-memory-blocks)
    * [API](https://docs.python.org/3/library/tracemalloc.html#api)
      * [Functions](https://docs.python.org/3/library/tracemalloc.html#functions)
      * [DomainFilter](https://docs.python.org/3/library/tracemalloc.html#domainfilter)
      * [Filter](https://docs.python.org/3/library/tracemalloc.html#filter)
      * [Frame](https://docs.python.org/3/library/tracemalloc.html#frame)
      * [Snapshot](https://docs.python.org/3/library/tracemalloc.html#snapshot)
      * [Statistic](https://docs.python.org/3/library/tracemalloc.html#statistic)
      * [StatisticDiff](https://docs.python.org/3/library/tracemalloc.html#statisticdiff)
      * [Trace](https://docs.python.org/3/library/tracemalloc.html#trace)
      * [Traceback](https://docs.python.org/3/library/tracemalloc.html#traceback)


#### Previous topic
[`test` — Regression tests package for Python](https://docs.python.org/3/library/test.html "previous chapter")
#### Next topic
[Audit events table](https://docs.python.org/3/library/audit_events.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Debugging+and+Profiling&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdebug.html&pagesource=library%2Fdebug.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/audit_events.html "Audit events table") |
  * [previous](https://docs.python.org/3/library/test.html "test — Regression tests package for Python") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
