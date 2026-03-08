[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`atexit` — Exit handlers](https://docs.python.org/3/library/atexit.html)
    * [`atexit` Example](https://docs.python.org/3/library/atexit.html#atexit-example)


#### Previous topic
[`abc` — Abstract Base Classes](https://docs.python.org/3/library/abc.html "previous chapter")
#### Next topic
[`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=atexit+%E2%80%94+Exit+handlers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fatexit.html&pagesource=library%2Fatexit.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/traceback.html "traceback — Print or retrieve a stack traceback") |
  * [previous](https://docs.python.org/3/library/abc.html "abc — Abstract Base Classes") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`atexit` — Exit handlers](https://docs.python.org/3/library/atexit.html)
  * |
  * Theme  Auto Light Dark |


#  `atexit` — Exit handlers[¶](https://docs.python.org/3/library/atexit.html#module-atexit "Link to this heading")
* * *
The `atexit` module defines functions to register and unregister cleanup functions. Functions thus registered are automatically executed upon normal interpreter termination. `atexit` runs these functions in the _reverse_ order in which they were registered; if you register `A`, `B`, and `C`, at interpreter termination time they will be run in the order `C`, `B`, `A`.
**Note:** The functions registered via this module are not called when the program is killed by a signal not handled by Python, when a Python fatal internal error is detected, or when [`os._exit()`](https://docs.python.org/3/library/os.html#os._exit "os._exit") is called.
**Note:** The effect of registering or unregistering functions from within a cleanup function is undefined.
Changed in version 3.7: When used with C-API subinterpreters, registered functions are local to the interpreter they were registered in.

atexit.register(_func_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/atexit.html#atexit.register "Link to this definition")

Register _func_ as a function to be executed at termination. Any optional arguments that are to be passed to _func_ must be passed as arguments to `register()`. It is possible to register the same function and arguments more than once.
At normal program termination (for instance, if [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit") is called or the main module’s execution completes), all functions registered are called in last in, first out order. The assumption is that lower level modules will normally be imported before higher level modules and thus must be cleaned up later.
If an exception is raised during execution of the exit handlers, a traceback is printed (unless [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "SystemExit") is raised) and the exception information is saved. After all exit handlers have had a chance to run, the last exception to be raised is re-raised.
This function returns _func_ , which makes it possible to use it as a decorator.
Warning
Starting new threads or calling [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork") from a registered function can lead to race condition between the main Python runtime thread freeing thread states while internal [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.") routines or the new process try to use that state. This can lead to crashes rather than clean shutdown.
Changed in version 3.12: Attempts to start a new thread or [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork") a new process in a registered function now leads to [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError").

atexit.unregister(_func_)[¶](https://docs.python.org/3/library/atexit.html#atexit.unregister "Link to this definition")

Remove _func_ from the list of functions to be run at interpreter shutdown. `unregister()` silently does nothing if _func_ was not previously registered. If _func_ has been registered more than once, every occurrence of that function in the `atexit` call stack will be removed. Equality comparisons (`==`) are used internally during unregistration, so function references do not need to have matching identities.
See also

Module [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")

Useful example of `atexit` to read and write [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") history files.
##  `atexit` Example[¶](https://docs.python.org/3/library/atexit.html#atexit-example "Link to this heading")
The following simple example demonstrates how a module can initialize a counter from a file when it is imported and save the counter’s updated value automatically when the program terminates without relying on the application making an explicit call into this module at termination.
Copy```
try:
    with open('counterfile') as infile:
        _count = int(infile.read())
except FileNotFoundError:
    _count = 0

def incrcounter(n):
    global _count
    _count = _count + n

def savecounter():
    with open('counterfile', 'w') as outfile:
        outfile.write('%d' % _count)

import atexit

atexit.register(savecounter)

```

Positional and keyword arguments may also be passed to [`register()`](https://docs.python.org/3/library/atexit.html#atexit.register "atexit.register") to be passed along to the registered function when it is called:
Copy```
def goodbye(name, adjective):
    print('Goodbye %s, it was %s to meet you.' % (name, adjective))

import atexit

atexit.register(goodbye, 'Donny', 'nice')
# or:
atexit.register(goodbye, adjective='nice', name='Donny')

```

Usage as a [decorator](https://docs.python.org/3/glossary.html#term-decorator):
Copy```
import atexit

@atexit.register
def goodbye():
    print('You are now leaving the Python sector.')

```

This only works with functions that can be called without arguments.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`atexit` — Exit handlers](https://docs.python.org/3/library/atexit.html)
    * [`atexit` Example](https://docs.python.org/3/library/atexit.html#atexit-example)


#### Previous topic
[`abc` — Abstract Base Classes](https://docs.python.org/3/library/abc.html "previous chapter")
#### Next topic
[`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=atexit+%E2%80%94+Exit+handlers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fatexit.html&pagesource=library%2Fatexit.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/traceback.html "traceback — Print or retrieve a stack traceback") |
  * [previous](https://docs.python.org/3/library/abc.html "abc — Abstract Base Classes") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`atexit` — Exit handlers](https://docs.python.org/3/library/atexit.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
