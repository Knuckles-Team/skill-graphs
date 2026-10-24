[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`timeit` — Measure execution time of small code snippets](https://docs.python.org/3/library/timeit.html)
    * [Basic Examples](https://docs.python.org/3/library/timeit.html#basic-examples)
    * [Python Interface](https://docs.python.org/3/library/timeit.html#python-interface)
    * [Command-Line Interface](https://docs.python.org/3/library/timeit.html#command-line-interface)
    * [Examples](https://docs.python.org/3/library/timeit.html#examples)


#### Previous topic
[The Python Profilers](https://docs.python.org/3/library/profile.html "previous chapter")
#### Next topic
[`trace` — Trace or track Python statement execution](https://docs.python.org/3/library/trace.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=timeit+%E2%80%94+Measure+execution+time+of+small+code+snippets&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftimeit.html&pagesource=library%2Ftimeit.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/trace.html "trace — Trace or track Python statement execution") |
  * [previous](https://docs.python.org/3/library/profile.html "The Python Profilers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html) »
  * [`timeit` — Measure execution time of small code snippets](https://docs.python.org/3/library/timeit.html)
  * |
  * Theme  Auto Light Dark |


#  `timeit` — Measure execution time of small code snippets[¶](https://docs.python.org/3/library/timeit.html#module-timeit "Link to this heading")
**Source code:**
* * *
This module provides a simple way to time small bits of Python code. It has both a [Command-Line Interface](https://docs.python.org/3/library/timeit.html#timeit-command-line-interface) as well as a [callable](https://docs.python.org/3/library/timeit.html#python-interface) one. It avoids a number of common traps for measuring execution times. See also Tim Peters’ introduction to the “Algorithms” chapter in the second edition of _Python Cookbook_ , published by O’Reilly.
## Basic Examples[¶](https://docs.python.org/3/library/timeit.html#basic-examples "Link to this heading")
The following example shows how the [Command-Line Interface](https://docs.python.org/3/library/timeit.html#timeit-command-line-interface) can be used to compare three different expressions:
Copy```
$ python -m timeit "'-'.join(str(n) for n in range(100))"
10000 loops, best of 5: 30.2 usec per loop
$ python -m timeit "'-'.join([str(n) for n in range(100)])"
10000 loops, best of 5: 27.5 usec per loop
$ python -m timeit "'-'.join(map(str, range(100)))"
10000 loops, best of 5: 23.2 usec per loop

```

This can be achieved from the [Python Interface](https://docs.python.org/3/library/timeit.html#python-interface) with:
Copy```
>>> import timeit
>>> timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
0.3018611848820001
>>> timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
0.2727368790656328
>>> timeit.timeit('"-".join(map(str, range(100)))', number=10000)
0.23702679807320237

```

A callable can also be passed from the [Python Interface](https://docs.python.org/3/library/timeit.html#python-interface):
Copy```
>>> timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
0.19665591977536678

```

Note however that [`timeit()`](https://docs.python.org/3/library/timeit.html#timeit.timeit "timeit.timeit") will automatically determine the number of repetitions only when the command-line interface is used. In the [Examples](https://docs.python.org/3/library/timeit.html#timeit-examples) section you can find more advanced examples.
## Python Interface[¶](https://docs.python.org/3/library/timeit.html#python-interface "Link to this heading")
The module defines three convenience functions and a public class:

timeit.timeit(_stmt='pass'_ , _setup='pass'_ , _timer= <default timer>_, _number=1000000_ , _globals=None_)[¶](https://docs.python.org/3/library/timeit.html#timeit.timeit "Link to this definition")

Create a [`Timer`](https://docs.python.org/3/library/timeit.html#timeit.Timer "timeit.Timer") instance with the given statement, _setup_ code and _timer_ function and run its [`timeit()`](https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit "timeit.Timer.timeit") method with _number_ executions. The optional _globals_ argument specifies a namespace in which to execute the code.
Changed in version 3.5: The optional _globals_ parameter was added.

timeit.repeat(_stmt='pass'_ , _setup='pass'_ , _timer= <default timer>_, _repeat=5_ , _number=1000000_ , _globals=None_)[¶](https://docs.python.org/3/library/timeit.html#timeit.repeat "Link to this definition")

Create a [`Timer`](https://docs.python.org/3/library/timeit.html#timeit.Timer "timeit.Timer") instance with the given statement, _setup_ code and _timer_ function and run its [`repeat()`](https://docs.python.org/3/library/timeit.html#timeit.Timer.repeat "timeit.Timer.repeat") method with the given _repeat_ count and _number_ executions. The optional _globals_ argument specifies a namespace in which to execute the code.
Changed in version 3.5: The optional _globals_ parameter was added.
Changed in version 3.7: Default value of _repeat_ changed from 3 to 5.

timeit.default_timer()[¶](https://docs.python.org/3/library/timeit.html#timeit.default_timer "Link to this definition")

The default timer, which is always time.perf_counter(), returns float seconds. An alternative, time.perf_counter_ns, returns integer nanoseconds.
Changed in version 3.3: [`time.perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter "time.perf_counter") is now the default timer.

_class_ timeit.Timer(_stmt='pass'_ , _setup='pass'_ , _timer= <timer function>_, _globals=None_)[¶](https://docs.python.org/3/library/timeit.html#timeit.Timer "Link to this definition")

Class for timing execution speed of small code snippets.
The constructor takes a statement to be timed, an additional statement used for setup, and a timer function. Both statements default to `'pass'`; the timer function is platform-dependent (see the module doc string). _stmt_ and _setup_ may also contain multiple statements separated by `;` or newlines, as long as they don’t contain multi-line string literals. The statement will by default be executed within timeit’s namespace; this behavior can be controlled by passing a namespace to _globals_.
To measure the execution time of the first statement, use the [`timeit()`](https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit "timeit.Timer.timeit") method. The [`repeat()`](https://docs.python.org/3/library/timeit.html#timeit.Timer.repeat "timeit.Timer.repeat") and [`autorange()`](https://docs.python.org/3/library/timeit.html#timeit.Timer.autorange "timeit.Timer.autorange") methods are convenience methods to call `timeit()` multiple times.
The execution time of _setup_ is excluded from the overall timed execution run.
The _stmt_ and _setup_ parameters can also take objects that are callable without arguments. This will embed calls to them in a timer function that will then be executed by [`timeit()`](https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit "timeit.Timer.timeit"). Note that the timing overhead is a little larger in this case because of the extra function calls.
Changed in version 3.5: The optional _globals_ parameter was added.

timeit(_number =1000000_)[¶](https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit "Link to this definition")

Time _number_ executions of the main statement. This executes the setup statement once, and then returns the time it takes to execute the main statement a number of times. The default timer returns seconds as a float. The argument is the number of times through the loop, defaulting to one million. The main statement, the setup statement and the timer function to be used are passed to the constructor.
Note
By default, `timeit()` temporarily turns off [garbage collection](https://docs.python.org/3/glossary.html#term-garbage-collection) during the timing. The advantage of this approach is that it makes independent timings more comparable. The disadvantage is that GC may be an important component of the performance of the function being measured. If so, GC can be re-enabled as the first statement in the _setup_ string. For example:
Copy```
timeit.Timer('for i in range(10): oct(i)', 'gc.enable()').timeit()

```


autorange(_callback =None_)[¶](https://docs.python.org/3/library/timeit.html#timeit.Timer.autorange "Link to this definition")

Automatically determine how many times to call [`timeit()`](https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit "timeit.Timer.timeit").
This is a convenience function that calls [`timeit()`](https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit "timeit.Timer.timeit") repeatedly so that the total time >= 0.2 second, returning the eventual (number of loops, time taken for that number of loops). It calls `timeit()` with increasing numbers from the sequence 1, 2, 5, 10, 20, 50, … until the time taken is at least 0.2 seconds.
If _callback_ is given and is not `None`, it will be called after each trial with two arguments: `callback(number, time_taken)`.
Added in version 3.6.

repeat(_repeat =5_, _number =1000000_)[¶](https://docs.python.org/3/library/timeit.html#timeit.Timer.repeat "Link to this definition")

Call [`timeit()`](https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit "timeit.Timer.timeit") a few times.
This is a convenience function that calls the [`timeit()`](https://docs.python.org/3/library/timeit.html#timeit.Timer.timeit "timeit.Timer.timeit") repeatedly, returning a list of results. The first argument specifies how many times to call `timeit()`. The second argument specifies the _number_ argument for `timeit()`.
Note
It’s tempting to calculate mean and standard deviation from the result vector and report these. However, this is not very useful. In a typical case, the lowest value gives a lower bound for how fast your machine can run the given code snippet; higher values in the result vector are typically not caused by variability in Python’s speed, but by other processes interfering with your timing accuracy. So the [`min()`](https://docs.python.org/3/library/functions.html#min "min") of the result is probably the only number you should be interested in. After that, you should look at the entire vector and apply common sense rather than statistics.
Changed in version 3.7: Default value of _repeat_ changed from 3 to 5.

print_exc(_file =None_)[¶](https://docs.python.org/3/library/timeit.html#timeit.Timer.print_exc "Link to this definition")

Helper to print a traceback from the timed code.
Typical use:
Copy```
t = Timer(...)       # outside the try/except
try:
    t.timeit(...)    # or t.repeat(...)
except Exception:
    t.print_exc()

```

The advantage over the standard traceback is that source lines in the compiled template will be displayed. The optional _file_ argument directs where the traceback is sent; it defaults to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr").
## Command-Line Interface[¶](https://docs.python.org/3/library/timeit.html#command-line-interface "Link to this heading")
When called as a program from the command line, the following form is used:
Copy```
python -m timeit [-n N] [-r N] [-u U] [-s S] [-p] [-v] [-h] [statement ...]

```

Where the following options are understood:

-n N, --number=N[¶](https://docs.python.org/3/library/timeit.html#cmdoption-timeit-n "Link to this definition")

how many times to execute ‘statement’

-r N, --repeat=N[¶](https://docs.python.org/3/library/timeit.html#cmdoption-timeit-r "Link to this definition")

how many times to repeat the timer (default 5)

-s S, --setup=S[¶](https://docs.python.org/3/library/timeit.html#cmdoption-timeit-s "Link to this definition")

statement to be executed once initially (default `pass`)

-p, --process[¶](https://docs.python.org/3/library/timeit.html#cmdoption-timeit-p "Link to this definition")

measure process time, not wallclock time, using [`time.process_time()`](https://docs.python.org/3/library/time.html#time.process_time "time.process_time") instead of [`time.perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter "time.perf_counter"), which is the default
Added in version 3.3.

-u, --unit=U[¶](https://docs.python.org/3/library/timeit.html#cmdoption-timeit-u "Link to this definition")

specify a time unit for timer output; can select `nsec`, `usec`, `msec`, or `sec`
Added in version 3.5.

-v, --verbose[¶](https://docs.python.org/3/library/timeit.html#cmdoption-timeit-v "Link to this definition")

print raw timing results; repeat for more digits precision

-h, --help[¶](https://docs.python.org/3/library/timeit.html#cmdoption-timeit-h "Link to this definition")

print a short usage message and exit
A multi-line statement may be given by specifying each line as a separate statement argument; indented lines are possible by enclosing an argument in quotes and using leading spaces. Multiple [`-s`](https://docs.python.org/3/library/timeit.html#cmdoption-timeit-s) options are treated similarly.
If [`-n`](https://docs.python.org/3/library/timeit.html#cmdoption-timeit-n) is not given, a suitable number of loops is calculated by trying increasing numbers from the sequence 1, 2, 5, 10, 20, 50, … until the total time is at least 0.2 seconds.
[`default_timer()`](https://docs.python.org/3/library/timeit.html#timeit.default_timer "timeit.default_timer") measurements can be affected by other programs running on the same machine, so the best thing to do when accurate timing is necessary is to repeat the timing a few times and use the best time. The [`-r`](https://docs.python.org/3/library/timeit.html#cmdoption-timeit-r) option is good for this; the default of 5 repetitions is probably enough in most cases. You can use [`time.process_time()`](https://docs.python.org/3/library/time.html#time.process_time "time.process_time") to measure CPU time.
Note
There is a certain baseline overhead associated with executing a pass statement. The code here doesn’t try to hide it, but you should be aware of it. The baseline overhead can be measured by invoking the program without arguments, and it might differ between Python versions.
## Examples[¶](https://docs.python.org/3/library/timeit.html#examples "Link to this heading")
It is possible to provide a setup statement that is executed only once at the beginning:
Copy```
$ python -m timeit -s "text = 'sample string'; char = 'g'" "char in text"
5000000 loops, best of 5: 0.0877 usec per loop
$ python -m timeit -s "text = 'sample string'; char = 'g'" "text.find(char)"
1000000 loops, best of 5: 0.342 usec per loop

```

In the output, there are three fields. The loop count, which tells you how many times the statement body was run per timing loop repetition. The repetition count (‘best of 5’) which tells you how many times the timing loop was repeated, and finally the time the statement body took on average within the best repetition of the timing loop. That is, the time the fastest repetition took divided by the loop count.
Copy```
>>> import timeit
>>> timeit.timeit('char in text', setup='text = "sample string"; char = "g"')
0.41440500499993504
>>> timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"')
1.7246671520006203

```

The same can be done using the [`Timer`](https://docs.python.org/3/library/timeit.html#timeit.Timer "timeit.Timer") class and its methods:
Copy```
>>> import timeit
>>> t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
>>> t.timeit()
0.3955516149999312
>>> t.repeat()
[0.40183617287970225, 0.37027556854118704, 0.38344867356679524, 0.3712595970846668, 0.37866875250654886]

```

The following examples show how to time expressions that contain multiple lines. Here we compare the cost of using [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr "hasattr") vs. [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)/[`except`](https://docs.python.org/3/reference/compound_stmts.html#except) to test for missing and present object attributes:
Copy```
$ python -m timeit "try:" "  str.__bool__" "except AttributeError:" "  pass"
20000 loops, best of 5: 15.7 usec per loop
$ python -m timeit "if hasattr(str, '__bool__'): pass"
50000 loops, best of 5: 4.26 usec per loop

$ python -m timeit "try:" "  int.__bool__" "except AttributeError:" "  pass"
200000 loops, best of 5: 1.43 usec per loop
$ python -m timeit "if hasattr(int, '__bool__'): pass"
100000 loops, best of 5: 2.23 usec per loop

```

Copy```
>>> import timeit
>>> # attribute is missing
>>> s = """\
... try:
...     str.__bool__
... except AttributeError:
...     pass
... """
>>> timeit.timeit(stmt=s, number=100000)
0.9138244460009446
>>> s = "if hasattr(str, '__bool__'): pass"
>>> timeit.timeit(stmt=s, number=100000)
0.5829014980008651
>>>
>>> # attribute is present
>>> s = """\
... try:
...     int.__bool__
... except AttributeError:
...     pass
... """
>>> timeit.timeit(stmt=s, number=100000)
0.04215312199994514
>>> s = "if hasattr(int, '__bool__'): pass"
>>> timeit.timeit(stmt=s, number=100000)
0.08588060699912603

```

To give the `timeit` module access to functions you define, you can pass a _setup_ parameter which contains an import statement:
Copy```
def test():
    """Stupid test function"""
    L = [i for i in range(100)]

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))

```

Another option is to pass [`globals()`](https://docs.python.org/3/library/functions.html#globals "globals") to the _globals_ parameter, which will cause the code to be executed within your current global namespace. This can be more convenient than individually specifying imports:
Copy```
def f(x):
    return x**2
def g(x):
    return x**4
def h(x):
    return x**8

import timeit
print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`timeit` — Measure execution time of small code snippets](https://docs.python.org/3/library/timeit.html)
    * [Basic Examples](https://docs.python.org/3/library/timeit.html#basic-examples)
    * [Python Interface](https://docs.python.org/3/library/timeit.html#python-interface)
    * [Command-Line Interface](https://docs.python.org/3/library/timeit.html#command-line-interface)
    * [Examples](https://docs.python.org/3/library/timeit.html#examples)


#### Previous topic
[The Python Profilers](https://docs.python.org/3/library/profile.html "previous chapter")
#### Next topic
[`trace` — Trace or track Python statement execution](https://docs.python.org/3/library/trace.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=timeit+%E2%80%94+Measure+execution+time+of+small+code+snippets&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftimeit.html&pagesource=library%2Ftimeit.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/trace.html "trace — Trace or track Python statement execution") |
  * [previous](https://docs.python.org/3/library/profile.html "The Python Profilers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html) »
  * [`timeit` — Measure execution time of small code snippets](https://docs.python.org/3/library/timeit.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
