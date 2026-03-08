[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
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
[`trace` — Trace or track Python statement execution](https://docs.python.org/3/library/trace.html "previous chapter")
#### Next topic
[Software Packaging and Distribution](https://docs.python.org/3/library/distribution.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tracemalloc+%E2%80%94+Trace+memory+allocations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftracemalloc.html&pagesource=library%2Ftracemalloc.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/distribution.html "Software Packaging and Distribution") |
  * [previous](https://docs.python.org/3/library/trace.html "trace — Trace or track Python statement execution") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html) »
  * [`tracemalloc` — Trace memory allocations](https://docs.python.org/3/library/tracemalloc.html)
  * |
  * Theme  Auto Light Dark |


#  `tracemalloc` — Trace memory allocations[¶](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "Link to this heading")
Added in version 3.4.
**Source code:**
* * *
The tracemalloc module is a debug tool to trace memory blocks allocated by Python. It provides the following information:
  * Traceback where an object was allocated
  * Statistics on allocated memory blocks per filename and per line number: total size, number and average size of allocated memory blocks
  * Compute the differences between two snapshots to detect memory leaks


To trace most memory blocks allocated by Python, the module should be started as early as possible by setting the [`PYTHONTRACEMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONTRACEMALLOC) environment variable to `1`, or by using [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) `tracemalloc` command line option. The [`tracemalloc.start()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.start "tracemalloc.start") function can be called at runtime to start tracing Python memory allocations.
By default, a trace of an allocated memory block only stores the most recent frame (1 frame). To store 25 frames at startup: set the [`PYTHONTRACEMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONTRACEMALLOC) environment variable to `25`, or use the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) `tracemalloc=25` command line option.
## Examples[¶](https://docs.python.org/3/library/tracemalloc.html#examples "Link to this heading")
### Display the top 10[¶](https://docs.python.org/3/library/tracemalloc.html#display-the-top-10 "Link to this heading")
Display the 10 files allocating the most memory:
Copy```
import tracemalloc

tracemalloc.start()

# ... run your application ...

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)

```

Example of output of the Python test suite:
Copy```
[ Top 10 ]
<frozen importlib._bootstrap>:716: size=4855 KiB, count=39328, average=126 B
<frozen importlib._bootstrap>:284: size=521 KiB, count=3199, average=167 B
/usr/lib/python3.4/collections/__init__.py:368: size=244 KiB, count=2315, average=108 B
/usr/lib/python3.4/unittest/case.py:381: size=185 KiB, count=779, average=243 B
/usr/lib/python3.4/unittest/case.py:402: size=154 KiB, count=378, average=416 B
/usr/lib/python3.4/abc.py:133: size=88.7 KiB, count=347, average=262 B
<frozen importlib._bootstrap>:1446: size=70.4 KiB, count=911, average=79 B
<frozen importlib._bootstrap>:1454: size=52.0 KiB, count=25, average=2131 B
<string>:5: size=49.7 KiB, count=148, average=344 B
/usr/lib/python3.4/sysconfig.py:411: size=48.0 KiB, count=1, average=48.0 KiB

```

We can see that Python loaded `4855 KiB` data (bytecode and constants) from modules and that the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes") module allocated `244 KiB` to build [`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") types.
See [`Snapshot.statistics()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.statistics "tracemalloc.Snapshot.statistics") for more options.
### Compute differences[¶](https://docs.python.org/3/library/tracemalloc.html#compute-differences "Link to this heading")
Take two snapshots and display the differences:
Copy```
import tracemalloc
tracemalloc.start()
# ... start your application ...

snapshot1 = tracemalloc.take_snapshot()
# ... call the function leaking memory ...
snapshot2 = tracemalloc.take_snapshot()

top_stats = snapshot2.compare_to(snapshot1, 'lineno')

print("[ Top 10 differences ]")
for stat in top_stats[:10]:
    print(stat)

```

Example of output before/after running some tests of the Python test suite:
Copy```
[ Top 10 differences ]
<frozen importlib._bootstrap>:716: size=8173 KiB (+4428 KiB), count=71332 (+39369), average=117 B
/usr/lib/python3.4/linecache.py:127: size=940 KiB (+940 KiB), count=8106 (+8106), average=119 B
/usr/lib/python3.4/unittest/case.py:571: size=298 KiB (+298 KiB), count=589 (+589), average=519 B
<frozen importlib._bootstrap>:284: size=1005 KiB (+166 KiB), count=7423 (+1526), average=139 B
/usr/lib/python3.4/mimetypes.py:217: size=112 KiB (+112 KiB), count=1334 (+1334), average=86 B
/usr/lib/python3.4/http/server.py:848: size=96.0 KiB (+96.0 KiB), count=1 (+1), average=96.0 KiB
/usr/lib/python3.4/inspect.py:1465: size=83.5 KiB (+83.5 KiB), count=109 (+109), average=784 B
/usr/lib/python3.4/unittest/mock.py:491: size=77.7 KiB (+77.7 KiB), count=143 (+143), average=557 B
/usr/lib/python3.4/urllib/parse.py:476: size=71.8 KiB (+71.8 KiB), count=969 (+969), average=76 B
/usr/lib/python3.4/contextlib.py:38: size=67.2 KiB (+67.2 KiB), count=126 (+126), average=546 B

```

We can see that Python has loaded `8173 KiB` of module data (bytecode and constants), and that this is `4428 KiB` more than had been loaded before the tests, when the previous snapshot was taken. Similarly, the [`linecache`](https://docs.python.org/3/library/linecache.html#module-linecache "linecache: Provides random access to individual lines from text files.") module has cached `940 KiB` of Python source code to format tracebacks, all of it since the previous snapshot.
If the system has little free memory, snapshots can be written on disk using the [`Snapshot.dump()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.dump "tracemalloc.Snapshot.dump") method to analyze the snapshot offline. Then use the [`Snapshot.load()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.load "tracemalloc.Snapshot.load") method reload the snapshot.
### Get the traceback of a memory block[¶](https://docs.python.org/3/library/tracemalloc.html#get-the-traceback-of-a-memory-block "Link to this heading")
Code to display the traceback of the biggest memory block:
Copy```
import tracemalloc

# Store 25 frames
tracemalloc.start(25)

# ... run your application ...

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')

# pick the biggest memory block
stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
for line in stat.traceback.format():
    print(line)

```

Example of output of the Python test suite (traceback limited to 25 frames):
Copy```
903 memory blocks: 870.1 KiB
  File "<frozen importlib._bootstrap>", line 716
  File "<frozen importlib._bootstrap>", line 1036
  File "<frozen importlib._bootstrap>", line 934
  File "<frozen importlib._bootstrap>", line 1068
  File "<frozen importlib._bootstrap>", line 619
  File "<frozen importlib._bootstrap>", line 1581
  File "<frozen importlib._bootstrap>", line 1614
  File "/usr/lib/python3.4/doctest.py", line 101
    import pdb
  File "<frozen importlib._bootstrap>", line 284
  File "<frozen importlib._bootstrap>", line 938
  File "<frozen importlib._bootstrap>", line 1068
  File "<frozen importlib._bootstrap>", line 619
  File "<frozen importlib._bootstrap>", line 1581
  File "<frozen importlib._bootstrap>", line 1614
  File "/usr/lib/python3.4/test/support/__init__.py", line 1728
    import doctest
  File "/usr/lib/python3.4/test/test_pickletools.py", line 21
    support.run_doctest(pickletools)
  File "/usr/lib/python3.4/test/regrtest.py", line 1276
    test_runner()
  File "/usr/lib/python3.4/test/regrtest.py", line 976
    display_failure=not verbose)
  File "/usr/lib/python3.4/test/regrtest.py", line 761
    match_tests=ns.match_tests)
  File "/usr/lib/python3.4/test/regrtest.py", line 1563
    main()
  File "/usr/lib/python3.4/test/__main__.py", line 3
    regrtest.main_in_temp_cwd()
  File "/usr/lib/python3.4/runpy.py", line 73
    exec(code, run_globals)
  File "/usr/lib/python3.4/runpy.py", line 160
    "__main__", fname, loader, pkg_name)

```

We can see that the most memory was allocated in the [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.") module to load data (bytecode and constants) from modules: `870.1 KiB`. The traceback is where the `importlib` loaded data most recently: on the `import pdb` line of the [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") module. The traceback may change if a new module is loaded.
### Pretty top[¶](https://docs.python.org/3/library/tracemalloc.html#pretty-top "Link to this heading")
Code to display the 10 lines allocating the most memory with a pretty output, ignoring `<frozen importlib._bootstrap>` and `<unknown>` files:
Copy```
import linecache
import os
import tracemalloc

def display_top(snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print("#%s: %s:%s: %.1f KiB"
              % (index, frame.filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))

tracemalloc.start()

# ... run your application ...

snapshot = tracemalloc.take_snapshot()
display_top(snapshot)

```

Example of output of the Python test suite:
Copy```
Top 10 lines
#1: Lib/base64.py:414: 419.8 KiB
    _b85chars2 = [(a + b) for a in _b85chars for b in _b85chars]
#2: Lib/base64.py:306: 419.8 KiB
    _a85chars2 = [(a + b) for a in _a85chars for b in _a85chars]
#3: collections/__init__.py:368: 293.6 KiB
    exec(class_definition, namespace)
#4: Lib/abc.py:133: 115.2 KiB
    cls = super().__new__(mcls, name, bases, namespace)
#5: unittest/case.py:574: 103.1 KiB
    testMethod()
#6: Lib/linecache.py:127: 95.4 KiB
    lines = fp.readlines()
#7: urllib/parse.py:476: 71.8 KiB
    for a in _hexdig for b in _hexdig}
#8: <string>:5: 62.0 KiB
#9: Lib/_weakrefset.py:37: 60.0 KiB
    self.data = set()
#10: Lib/base64.py:142: 59.8 KiB
    _b32tab2 = [a + b for a in _b32tab for b in _b32tab]
6220 other: 3602.8 KiB
Total allocated size: 5303.1 KiB

```

See [`Snapshot.statistics()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.statistics "tracemalloc.Snapshot.statistics") for more options.
#### Record the current and peak size of all traced memory blocks[¶](https://docs.python.org/3/library/tracemalloc.html#record-the-current-and-peak-size-of-all-traced-memory-blocks "Link to this heading")
The following code computes two sums like `0 + 1 + 2 + ...` inefficiently, by creating a list of those numbers. This list consumes a lot of memory temporarily. We can use [`get_traced_memory()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_traced_memory "tracemalloc.get_traced_memory") and [`reset_peak()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.reset_peak "tracemalloc.reset_peak") to observe the small memory usage after the sum is computed as well as the peak memory usage during the computations:
Copy```
import tracemalloc

tracemalloc.start()

# Example code: compute a sum with a large temporary list
large_sum = sum(list(range(100000)))

first_size, first_peak = tracemalloc.get_traced_memory()

tracemalloc.reset_peak()

# Example code: compute a sum with a small temporary list
small_sum = sum(list(range(1000)))

second_size, second_peak = tracemalloc.get_traced_memory()

print(f"{first_size=}, {first_peak=}")
print(f"{second_size=}, {second_peak=}")

```

Output:
Copy```
first_size=664, first_peak=3592984
second_size=804, second_peak=29704

```

Using [`reset_peak()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.reset_peak "tracemalloc.reset_peak") ensured we could accurately record the peak during the computation of `small_sum`, even though it is much smaller than the overall peak size of memory blocks since the [`start()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.start "tracemalloc.start") call. Without the call to `reset_peak()`, `second_peak` would still be the peak from the computation `large_sum` (that is, equal to `first_peak`). In this case, both peaks are much higher than the final memory usage, and which suggests we could optimise (by removing the unnecessary call to [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), and writing `sum(range(...))`).
## API[¶](https://docs.python.org/3/library/tracemalloc.html#api "Link to this heading")
### Functions[¶](https://docs.python.org/3/library/tracemalloc.html#functions "Link to this heading")

tracemalloc.clear_traces()[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.clear_traces "Link to this definition")

Clear traces of memory blocks allocated by Python.
See also [`stop()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.stop "tracemalloc.stop").

tracemalloc.get_object_traceback(_obj_)[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_object_traceback "Link to this definition")

Get the traceback where the Python object _obj_ was allocated. Return a [`Traceback`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Traceback "tracemalloc.Traceback") instance, or `None` if the `tracemalloc` module is not tracing memory allocations or did not trace the allocation of the object.
See also [`gc.get_referrers()`](https://docs.python.org/3/library/gc.html#gc.get_referrers "gc.get_referrers") and [`sys.getsizeof()`](https://docs.python.org/3/library/sys.html#sys.getsizeof "sys.getsizeof") functions.

tracemalloc.get_traceback_limit()[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_traceback_limit "Link to this definition")

Get the maximum number of frames stored in the traceback of a trace.
The `tracemalloc` module must be tracing memory allocations to get the limit, otherwise an exception is raised.
The limit is set by the [`start()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.start "tracemalloc.start") function.

tracemalloc.get_traced_memory()[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_traced_memory "Link to this definition")

Get the current size and peak size of memory blocks traced by the `tracemalloc` module as a tuple: `(current: int, peak: int)`.

tracemalloc.reset_peak()[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.reset_peak "Link to this definition")

Set the peak size of memory blocks traced by the `tracemalloc` module to the current size.
Do nothing if the `tracemalloc` module is not tracing memory allocations.
This function only modifies the recorded peak size, and does not modify or clear any traces, unlike [`clear_traces()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.clear_traces "tracemalloc.clear_traces"). Snapshots taken with [`take_snapshot()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.take_snapshot "tracemalloc.take_snapshot") before a call to `reset_peak()` can be meaningfully compared to snapshots taken after the call.
See also [`get_traced_memory()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_traced_memory "tracemalloc.get_traced_memory").
Added in version 3.9.

tracemalloc.get_tracemalloc_memory()[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_tracemalloc_memory "Link to this definition")

Get the memory usage in bytes of the `tracemalloc` module used to store traces of memory blocks. Return an [`int`](https://docs.python.org/3/library/functions.html#int "int").

tracemalloc.is_tracing()[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.is_tracing "Link to this definition")

`True` if the `tracemalloc` module is tracing Python memory allocations, `False` otherwise.
See also [`start()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.start "tracemalloc.start") and [`stop()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.stop "tracemalloc.stop") functions.

tracemalloc.start(_nframe :[int](https://docs.python.org/3/library/functions.html#int "int")=1_)[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.start "Link to this definition")

Start tracing Python memory allocations: install hooks on Python memory allocators. Collected tracebacks of traces will be limited to _nframe_ frames. By default, a trace of a memory block only stores the most recent frame: the limit is `1`. _nframe_ must be greater or equal to `1`.
You can still read the original number of total frames that composed the traceback by looking at the [`Traceback.total_nframe`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Traceback.total_nframe "tracemalloc.Traceback.total_nframe") attribute.
Storing more than `1` frame is only useful to compute statistics grouped by `'traceback'` or to compute cumulative statistics: see the [`Snapshot.compare_to()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.compare_to "tracemalloc.Snapshot.compare_to") and [`Snapshot.statistics()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.statistics "tracemalloc.Snapshot.statistics") methods.
Storing more frames increases the memory and CPU overhead of the `tracemalloc` module. Use the [`get_tracemalloc_memory()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_tracemalloc_memory "tracemalloc.get_tracemalloc_memory") function to measure how much memory is used by the `tracemalloc` module.
The [`PYTHONTRACEMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONTRACEMALLOC) environment variable (`PYTHONTRACEMALLOC=NFRAME`) and the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) `tracemalloc=NFRAME` command line option can be used to start tracing at startup.
See also [`stop()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.stop "tracemalloc.stop"), [`is_tracing()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.is_tracing "tracemalloc.is_tracing") and [`get_traceback_limit()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_traceback_limit "tracemalloc.get_traceback_limit") functions.

tracemalloc.stop()[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.stop "Link to this definition")

Stop tracing Python memory allocations: uninstall hooks on Python memory allocators. Also clears all previously collected traces of memory blocks allocated by Python.
Call [`take_snapshot()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.take_snapshot "tracemalloc.take_snapshot") function to take a snapshot of traces before clearing them.
See also [`start()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.start "tracemalloc.start"), [`is_tracing()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.is_tracing "tracemalloc.is_tracing") and [`clear_traces()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.clear_traces "tracemalloc.clear_traces") functions.

tracemalloc.take_snapshot()[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.take_snapshot "Link to this definition")

Take a snapshot of traces of memory blocks allocated by Python. Return a new [`Snapshot`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot "tracemalloc.Snapshot") instance.
The snapshot does not include memory blocks allocated before the `tracemalloc` module started to trace memory allocations.
Tracebacks of traces are limited to [`get_traceback_limit()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_traceback_limit "tracemalloc.get_traceback_limit") frames. Use the _nframe_ parameter of the [`start()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.start "tracemalloc.start") function to store more frames.
The `tracemalloc` module must be tracing memory allocations to take a snapshot, see the [`start()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.start "tracemalloc.start") function.
See also the [`get_object_traceback()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_object_traceback "tracemalloc.get_object_traceback") function.
### DomainFilter[¶](https://docs.python.org/3/library/tracemalloc.html#domainfilter "Link to this heading")

_class_ tracemalloc.DomainFilter(_inclusive :[bool](https://docs.python.org/3/library/functions.html#bool "bool")_, _domain :[int](https://docs.python.org/3/library/functions.html#int "int")_)[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.DomainFilter "Link to this definition")

Filter traces of memory blocks by their address space (domain).
Added in version 3.6.

inclusive[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.DomainFilter.inclusive "Link to this definition")

If _inclusive_ is `True` (include), match memory blocks allocated in the address space [`domain`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.DomainFilter.domain "tracemalloc.DomainFilter.domain").
If _inclusive_ is `False` (exclude), match memory blocks not allocated in the address space [`domain`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.DomainFilter.domain "tracemalloc.DomainFilter.domain").

domain[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.DomainFilter.domain "Link to this definition")

Address space of a memory block (`int`). Read-only property.
### Filter[¶](https://docs.python.org/3/library/tracemalloc.html#filter "Link to this heading")

_class_ tracemalloc.Filter(_inclusive :[bool](https://docs.python.org/3/library/functions.html#bool "bool")_, _filename_pattern :[str](https://docs.python.org/3/library/stdtypes.html#str "str")_, _lineno :[int](https://docs.python.org/3/library/functions.html#int "int")=None_, _all_frames :[bool](https://docs.python.org/3/library/functions.html#bool "bool")=False_, _domain :[int](https://docs.python.org/3/library/functions.html#int "int")=None_)[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Filter "Link to this definition")

Filter on traces of memory blocks.
See the [`fnmatch.fnmatch()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "fnmatch.fnmatch") function for the syntax of _filename_pattern_. The `'.pyc'` file extension is replaced with `'.py'`.
Examples:
  * `Filter(True, subprocess.__file__)` only includes traces of the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") module
  * `Filter(False, tracemalloc.__file__)` excludes traces of the `tracemalloc` module
  * `Filter(False, "<unknown>")` excludes empty tracebacks


Changed in version 3.5: The `'.pyo'` file extension is no longer replaced with `'.py'`.
Changed in version 3.6: Added the [`domain`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Filter.domain "tracemalloc.Filter.domain") attribute.

domain[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Filter.domain "Link to this definition")

Address space of a memory block (`int` or `None`).
tracemalloc uses the domain `0` to trace memory allocations made by Python. C extensions can use other domains to trace other resources.

inclusive[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Filter.inclusive "Link to this definition")

If _inclusive_ is `True` (include), only match memory blocks allocated in a file with a name matching [`filename_pattern`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Filter.filename_pattern "tracemalloc.Filter.filename_pattern") at line number [`lineno`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Filter.lineno "tracemalloc.Filter.lineno").
If _inclusive_ is `False` (exclude), ignore memory blocks allocated in a file with a name matching [`filename_pattern`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Filter.filename_pattern "tracemalloc.Filter.filename_pattern") at line number [`lineno`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Filter.lineno "tracemalloc.Filter.lineno").

lineno[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Filter.lineno "Link to this definition")

Line number (`int`) of the filter. If _lineno_ is `None`, the filter matches any line number.

filename_pattern[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Filter.filename_pattern "Link to this definition")

Filename pattern of the filter (`str`). Read-only property.

all_frames[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Filter.all_frames "Link to this definition")

If _all_frames_ is `True`, all frames of the traceback are checked. If _all_frames_ is `False`, only the most recent frame is checked.
This attribute has no effect if the traceback limit is `1`. See the [`get_traceback_limit()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_traceback_limit "tracemalloc.get_traceback_limit") function and [`Snapshot.traceback_limit`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.traceback_limit "tracemalloc.Snapshot.traceback_limit") attribute.
### Frame[¶](https://docs.python.org/3/library/tracemalloc.html#frame "Link to this heading")

_class_ tracemalloc.Frame[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Frame "Link to this definition")

Frame of a traceback.
The [`Traceback`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Traceback "tracemalloc.Traceback") class is a sequence of `Frame` instances.

filename[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Frame.filename "Link to this definition")

Filename (`str`).

lineno[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Frame.lineno "Link to this definition")

Line number (`int`).
### Snapshot[¶](https://docs.python.org/3/library/tracemalloc.html#snapshot "Link to this heading")

_class_ tracemalloc.Snapshot[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot "Link to this definition")

Snapshot of traces of memory blocks allocated by Python.
The [`take_snapshot()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.take_snapshot "tracemalloc.take_snapshot") function creates a snapshot instance.

compare_to(_old_snapshot :Snapshot_, _key_type :[str](https://docs.python.org/3/library/stdtypes.html#str "str")_, _cumulative :[bool](https://docs.python.org/3/library/functions.html#bool "bool")=False_)[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.compare_to "Link to this definition")

Compute the differences with an old snapshot. Get statistics as a sorted list of [`StatisticDiff`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.StatisticDiff "tracemalloc.StatisticDiff") instances grouped by _key_type_.
See the [`Snapshot.statistics()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.statistics "tracemalloc.Snapshot.statistics") method for _key_type_ and _cumulative_ parameters.
The result is sorted from the biggest to the smallest by: absolute value of [`StatisticDiff.size_diff`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.StatisticDiff.size_diff "tracemalloc.StatisticDiff.size_diff"), [`StatisticDiff.size`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.StatisticDiff.size "tracemalloc.StatisticDiff.size"), absolute value of [`StatisticDiff.count_diff`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.StatisticDiff.count_diff "tracemalloc.StatisticDiff.count_diff"), [`Statistic.count`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Statistic.count "tracemalloc.Statistic.count") and then by [`StatisticDiff.traceback`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.StatisticDiff.traceback "tracemalloc.StatisticDiff.traceback").

dump(_filename_)[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.dump "Link to this definition")

Write the snapshot into a file.
Use [`load()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.load "tracemalloc.Snapshot.load") to reload the snapshot.

filter_traces(_filters_)[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.filter_traces "Link to this definition")

Create a new `Snapshot` instance with a filtered [`traces`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.traces "tracemalloc.Snapshot.traces") sequence, _filters_ is a list of [`DomainFilter`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.DomainFilter "tracemalloc.DomainFilter") and [`Filter`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Filter "tracemalloc.Filter") instances. If _filters_ is an empty list, return a new `Snapshot` instance with a copy of the traces.
All inclusive filters are applied at once, a trace is ignored if no inclusive filters match it. A trace is ignored if at least one exclusive filter matches it.
Changed in version 3.6: [`DomainFilter`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.DomainFilter "tracemalloc.DomainFilter") instances are now also accepted in _filters_.

_classmethod_ load(_filename_)[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.load "Link to this definition")

Load a snapshot from a file.
See also [`dump()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.dump "tracemalloc.Snapshot.dump").

statistics(_key_type :[str](https://docs.python.org/3/library/stdtypes.html#str "str")_, _cumulative :[bool](https://docs.python.org/3/library/functions.html#bool "bool")=False_)[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.statistics "Link to this definition")

Get statistics as a sorted list of [`Statistic`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Statistic "tracemalloc.Statistic") instances grouped by _key_type_ :
key_type | description
---|---
`'filename'` | filename
`'lineno'` | filename and line number
`'traceback'` | traceback
If _cumulative_ is `True`, cumulate size and count of memory blocks of all frames of the traceback of a trace, not only the most recent frame. The cumulative mode can only be used with _key_type_ equal to `'filename'` and `'lineno'`.
The result is sorted from the biggest to the smallest by: [`Statistic.size`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Statistic.size "tracemalloc.Statistic.size"), [`Statistic.count`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Statistic.count "tracemalloc.Statistic.count") and then by [`Statistic.traceback`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Statistic.traceback "tracemalloc.Statistic.traceback").

traceback_limit[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.traceback_limit "Link to this definition")

Maximum number of frames stored in the traceback of [`traces`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.traces "tracemalloc.Snapshot.traces"): result of the [`get_traceback_limit()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_traceback_limit "tracemalloc.get_traceback_limit") when the snapshot was taken.

traces[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.traces "Link to this definition")

Traces of all memory blocks allocated by Python: sequence of [`Trace`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Trace "tracemalloc.Trace") instances.
The sequence has an undefined order. Use the [`Snapshot.statistics()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.statistics "tracemalloc.Snapshot.statistics") method to get a sorted list of statistics.
### Statistic[¶](https://docs.python.org/3/library/tracemalloc.html#statistic "Link to this heading")

_class_ tracemalloc.Statistic[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Statistic "Link to this definition")

Statistic on memory allocations.
[`Snapshot.statistics()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.statistics "tracemalloc.Snapshot.statistics") returns a list of `Statistic` instances.
See also the [`StatisticDiff`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.StatisticDiff "tracemalloc.StatisticDiff") class.

count[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Statistic.count "Link to this definition")

Number of memory blocks (`int`).

size[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Statistic.size "Link to this definition")

Total size of memory blocks in bytes (`int`).

traceback[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Statistic.traceback "Link to this definition")

Traceback where the memory block was allocated, [`Traceback`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Traceback "tracemalloc.Traceback") instance.
### StatisticDiff[¶](https://docs.python.org/3/library/tracemalloc.html#statisticdiff "Link to this heading")

_class_ tracemalloc.StatisticDiff[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.StatisticDiff "Link to this definition")

Statistic difference on memory allocations between an old and a new [`Snapshot`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot "tracemalloc.Snapshot") instance.
[`Snapshot.compare_to()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.compare_to "tracemalloc.Snapshot.compare_to") returns a list of `StatisticDiff` instances. See also the [`Statistic`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Statistic "tracemalloc.Statistic") class.

count[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.StatisticDiff.count "Link to this definition")

Number of memory blocks in the new snapshot (`int`): `0` if the memory blocks have been released in the new snapshot.

count_diff[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.StatisticDiff.count_diff "Link to this definition")

Difference of number of memory blocks between the old and the new snapshots (`int`): `0` if the memory blocks have been allocated in the new snapshot.

size[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.StatisticDiff.size "Link to this definition")

Total size of memory blocks in bytes in the new snapshot (`int`): `0` if the memory blocks have been released in the new snapshot.

size_diff[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.StatisticDiff.size_diff "Link to this definition")

Difference of total size of memory blocks in bytes between the old and the new snapshots (`int`): `0` if the memory blocks have been allocated in the new snapshot.

traceback[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.StatisticDiff.traceback "Link to this definition")

Traceback where the memory blocks were allocated, [`Traceback`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Traceback "tracemalloc.Traceback") instance.
### Trace[¶](https://docs.python.org/3/library/tracemalloc.html#trace "Link to this heading")

_class_ tracemalloc.Trace[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Trace "Link to this definition")

Trace of a memory block.
The [`Snapshot.traces`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Snapshot.traces "tracemalloc.Snapshot.traces") attribute is a sequence of `Trace` instances.
Changed in version 3.6: Added the [`domain`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Trace.domain "tracemalloc.Trace.domain") attribute.

domain[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Trace.domain "Link to this definition")

Address space of a memory block (`int`). Read-only property.
tracemalloc uses the domain `0` to trace memory allocations made by Python. C extensions can use other domains to trace other resources.

size[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Trace.size "Link to this definition")

Size of the memory block in bytes (`int`).

traceback[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Trace.traceback "Link to this definition")

Traceback where the memory block was allocated, [`Traceback`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Traceback "tracemalloc.Traceback") instance.
### Traceback[¶](https://docs.python.org/3/library/tracemalloc.html#traceback "Link to this heading")

_class_ tracemalloc.Traceback[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Traceback "Link to this definition")

Sequence of [`Frame`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Frame "tracemalloc.Frame") instances sorted from the oldest frame to the most recent frame.
A traceback contains at least `1` frame. If the `tracemalloc` module failed to get a frame, the filename `"<unknown>"` at line number `0` is used.
When a snapshot is taken, tracebacks of traces are limited to [`get_traceback_limit()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.get_traceback_limit "tracemalloc.get_traceback_limit") frames. See the [`take_snapshot()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.take_snapshot "tracemalloc.take_snapshot") function. The original number of frames of the traceback is stored in the [`Traceback.total_nframe`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Traceback.total_nframe "tracemalloc.Traceback.total_nframe") attribute. That allows one to know if a traceback has been truncated by the traceback limit.
The [`Trace.traceback`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Trace.traceback "tracemalloc.Trace.traceback") attribute is a `Traceback` instance.
Changed in version 3.7: Frames are now sorted from the oldest to the most recent, instead of most recent to oldest.

total_nframe[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Traceback.total_nframe "Link to this definition")

Total number of frames that composed the traceback before truncation. This attribute can be set to `None` if the information is not available.
Changed in version 3.9: The [`Traceback.total_nframe`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Traceback.total_nframe "tracemalloc.Traceback.total_nframe") attribute was added.

format(_limit =None_, _most_recent_first =False_)[¶](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.Traceback.format "Link to this definition")

Format the traceback as a list of lines. Use the [`linecache`](https://docs.python.org/3/library/linecache.html#module-linecache "linecache: Provides random access to individual lines from text files.") module to retrieve lines from the source code. If _limit_ is set, format the _limit_ most recent frames if _limit_ is positive. Otherwise, format the `abs(limit)` oldest frames. If _most_recent_first_ is `True`, the order of the formatted frames is reversed, returning the most recent frame first instead of last.
Similar to the [`traceback.format_tb()`](https://docs.python.org/3/library/traceback.html#traceback.format_tb "traceback.format_tb") function, except that `format()` does not include newlines.
Example:
Copy```
print("Traceback (most recent call first):")
for line in traceback:
    print(line)

```

Output:
Copy```
Traceback (most recent call first):
  File "test.py", line 9
    obj = Object()
  File "test.py", line 12
    tb = tracemalloc.get_object_traceback(f())

```

### [Table of Contents](https://docs.python.org/3/contents.html)
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
[`trace` — Trace or track Python statement execution](https://docs.python.org/3/library/trace.html "previous chapter")
#### Next topic
[Software Packaging and Distribution](https://docs.python.org/3/library/distribution.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tracemalloc+%E2%80%94+Trace+memory+allocations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftracemalloc.html&pagesource=library%2Ftracemalloc.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/distribution.html "Software Packaging and Distribution") |
  * [previous](https://docs.python.org/3/library/trace.html "trace — Trace or track Python statement execution") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Debugging and Profiling](https://docs.python.org/3/library/debug.html) »
  * [`tracemalloc` — Trace memory allocations](https://docs.python.org/3/library/tracemalloc.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
