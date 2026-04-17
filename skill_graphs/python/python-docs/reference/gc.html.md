[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html "previous chapter")
#### Next topic
[`inspect` — Inspect live objects](https://docs.python.org/3/library/inspect.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=gc+%E2%80%94+Garbage+Collector+interface&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgc.html&pagesource=library%2Fgc.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/inspect.html "inspect — Inspect live objects") |
  * [previous](https://docs.python.org/3/library/__future__.html "__future__ — Future statement definitions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`gc` — Garbage Collector interface](https://docs.python.org/3/library/gc.html)
  * |
  * Theme  Auto Light Dark |


#  `gc` — Garbage Collector interface[¶](https://docs.python.org/3/library/gc.html#module-gc "Link to this heading")
* * *
This module provides an interface to the optional garbage collector. It provides the ability to disable the collector, tune the collection frequency, and set debugging options. It also provides access to unreachable objects that the collector found but cannot free. Since the collector supplements the reference counting already used in Python, you can disable the collector if you are sure your program does not create reference cycles. Automatic collection can be disabled by calling `gc.disable()`. To debug a leaking program call `gc.set_debug(gc.DEBUG_LEAK)`. Notice that this includes `gc.DEBUG_SAVEALL`, causing garbage-collected objects to be saved in gc.garbage for inspection.
The `gc` module provides the following functions:

gc.enable()[¶](https://docs.python.org/3/library/gc.html#gc.enable "Link to this definition")

Enable automatic garbage collection.

gc.disable()[¶](https://docs.python.org/3/library/gc.html#gc.disable "Link to this definition")

Disable automatic garbage collection.

gc.isenabled()[¶](https://docs.python.org/3/library/gc.html#gc.isenabled "Link to this definition")

Return `True` if automatic collection is enabled.

gc.collect(_generation =2_)[¶](https://docs.python.org/3/library/gc.html#gc.collect "Link to this definition")

Perform a collection. The optional argument _generation_ may be an integer specifying which generation to collect (from 0 to 2). A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the generation number is invalid. The sum of collected objects and uncollectable objects is returned.
Calling `gc.collect(0)` will perform a GC collection on the young generation.
Calling `gc.collect(1)` will perform a GC collection on the young generation and an increment of the old generation.
Calling `gc.collect(2)` or `gc.collect()` performs a full collection
The free lists maintained for a number of built-in types are cleared whenever a full collection or collection of the highest generation (2) is run. Not all items in some free lists may be freed due to the particular implementation, in particular [`float`](https://docs.python.org/3/library/functions.html#float "float").
The effect of calling `gc.collect()` while the interpreter is already performing a collection is undefined.
Changed in version 3.14: `generation=1` performs an increment of collection.

gc.set_debug(_flags_)[¶](https://docs.python.org/3/library/gc.html#gc.set_debug "Link to this definition")

Set the garbage collection debugging flags. Debugging information will be written to `sys.stderr`. See below for a list of debugging flags which can be combined using bit operations to control debugging.

gc.get_debug()[¶](https://docs.python.org/3/library/gc.html#gc.get_debug "Link to this definition")

Return the debugging flags currently set.

gc.get_objects(_generation =None_)[¶](https://docs.python.org/3/library/gc.html#gc.get_objects "Link to this definition")

Returns a list of all objects tracked by the collector, excluding the list returned. If _generation_ is not `None`, return only the objects as follows:
  * 0: All objects in the young generation
  * 1: No objects, as there is no generation 1 (as of Python 3.14)
  * 2: All objects in the old generation


Changed in version 3.8: New _generation_ parameter.
Changed in version 3.14: Generation 1 is removed
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `gc.get_objects` with argument `generation`.

gc.get_stats()[¶](https://docs.python.org/3/library/gc.html#gc.get_stats "Link to this definition")

Return a list of three per-generation dictionaries containing collection statistics since interpreter start. The number of keys may change in the future, but currently each dictionary will contain the following items:
  * `collections` is the number of times this generation was collected;
  * `collected` is the total number of objects collected inside this generation;
  * `uncollectable` is the total number of objects which were found to be uncollectable (and were therefore moved to the [`garbage`](https://docs.python.org/3/library/gc.html#gc.garbage "gc.garbage") list) inside this generation.


Added in version 3.4.

gc.set_threshold(_threshold0_[, _threshold1_[, _threshold2_]])[¶](https://docs.python.org/3/library/gc.html#gc.set_threshold "Link to this definition")

Set the garbage collection thresholds (the collection frequency). Setting _threshold0_ to zero disables collection.
The GC classifies objects into two generations depending on whether they have survived a collection. New objects are placed in the young generation. If an object survives a collection it is moved into the old generation.
In order to decide when to run, the collector keeps track of the number of object allocations and deallocations since the last collection. When the number of allocations minus the number of deallocations exceeds _threshold0_ , collection starts. For each collection, all the objects in the young generation and some fraction of the old generation is collected.
In the free-threaded build, the increase in process memory usage is also checked before running the collector. If the memory usage has not increased by 10% since the last collection and the net number of object allocations has not exceeded 40 times _threshold0_ , the collection is not run.
The fraction of the old generation that is collected is **inversely** proportional to _threshold1_. The larger _threshold1_ is, the slower objects in the old generation are collected. For the default value of 10, 1% of the old generation is scanned during each collection.
_threshold2_ is ignored.
See
Changed in version 3.14: _threshold2_ is ignored

gc.get_count()[¶](https://docs.python.org/3/library/gc.html#gc.get_count "Link to this definition")

Return the current collection counts as a tuple of `(count0, count1, count2)`.

gc.get_threshold()[¶](https://docs.python.org/3/library/gc.html#gc.get_threshold "Link to this definition")

Return the current collection thresholds as a tuple of `(threshold0, threshold1, threshold2)`.

gc.get_referrers(_* objs_)[¶](https://docs.python.org/3/library/gc.html#gc.get_referrers "Link to this definition")

Return the list of objects that directly refer to any of objs. This function will only locate those containers which support garbage collection; extension types which do refer to other objects but do not support garbage collection will not be found.
Note that objects which have already been dereferenced, but which live in cycles and have not yet been collected by the garbage collector can be listed among the resulting referrers. To get only currently live objects, call [`collect()`](https://docs.python.org/3/library/gc.html#gc.collect "gc.collect") before calling `get_referrers()`.
Warning
Care must be taken when using objects returned by `get_referrers()` because some of them could still be under construction and hence in a temporarily invalid state. Avoid using `get_referrers()` for any purpose other than debugging.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `gc.get_referrers` with argument `objs`.

gc.get_referents(_* objs_)[¶](https://docs.python.org/3/library/gc.html#gc.get_referents "Link to this definition")

Return a list of objects directly referred to by any of the arguments. The referents returned are those objects visited by the arguments’ C-level [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse") methods (if any), and may not be all objects actually directly reachable. `tp_traverse` methods are supported only by objects that support garbage collection, and are only required to visit objects that may be involved in a cycle. So, for example, if an integer is directly reachable from an argument, that integer object may or may not appear in the result list.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `gc.get_referents` with argument `objs`.

gc.is_tracked(_obj_)[¶](https://docs.python.org/3/library/gc.html#gc.is_tracked "Link to this definition")

Returns `True` if the object is currently tracked by the garbage collector, `False` otherwise. As a general rule, instances of atomic types aren’t tracked and instances of non-atomic types (containers, user-defined objects…) are. However, some type-specific optimizations can be present in order to suppress the garbage collector footprint of simple instances (e.g. dicts containing only atomic keys and values):
Copy```
>>> gc.is_tracked(0)
False
>>> gc.is_tracked("a")
False
>>> gc.is_tracked([])
True
>>> gc.is_tracked({})
False
>>> gc.is_tracked({"a": 1})
True

```

Added in version 3.1.

gc.is_finalized(_obj_)[¶](https://docs.python.org/3/library/gc.html#gc.is_finalized "Link to this definition")

Returns `True` if the given object has been finalized by the garbage collector, `False` otherwise.
Copy```
>>> x = None
>>> class Lazarus:
...     def __del__(self):
...         global x
...         x = self
...
>>> lazarus = Lazarus()
>>> gc.is_finalized(lazarus)
False
>>> del lazarus
>>> gc.is_finalized(x)
True

```

Added in version 3.9.

gc.freeze()[¶](https://docs.python.org/3/library/gc.html#gc.freeze "Link to this definition")

Freeze all the objects tracked by the garbage collector; move them to a permanent generation and ignore them in all the future collections.
If a process will `fork()` without `exec()`, avoiding unnecessary copy-on-write in child processes will maximize memory sharing and reduce overall memory usage. This requires both avoiding creation of freed “holes” in memory pages in the parent process and ensuring that GC collections in child processes won’t touch the `gc_refs` counter of long-lived objects originating in the parent process. To accomplish both, call `gc.disable()` early in the parent process, `gc.freeze()` right before `fork()`, and `gc.enable()` early in child processes.
Added in version 3.7.

gc.unfreeze()[¶](https://docs.python.org/3/library/gc.html#gc.unfreeze "Link to this definition")

Unfreeze the objects in the permanent generation, put them back into the oldest generation.
Added in version 3.7.

gc.get_freeze_count()[¶](https://docs.python.org/3/library/gc.html#gc.get_freeze_count "Link to this definition")

Return the number of objects in the permanent generation.
Added in version 3.7.
The following variables are provided for read-only access (you can mutate the values but should not rebind them):

gc.garbage[¶](https://docs.python.org/3/library/gc.html#gc.garbage "Link to this definition")

A list of objects which the collector found to be unreachable but could not be freed (uncollectable objects). Starting with Python 3.4, this list should be empty most of the time, except when using instances of C extension types with a non-`NULL` `tp_del` slot.
If [`DEBUG_SAVEALL`](https://docs.python.org/3/library/gc.html#gc.DEBUG_SAVEALL "gc.DEBUG_SAVEALL") is set, then all unreachable objects will be added to this list rather than freed.
Changed in version 3.2: If this list is non-empty at [interpreter shutdown](https://docs.python.org/3/glossary.html#term-interpreter-shutdown), a [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning") is emitted, which is silent by default. If [`DEBUG_UNCOLLECTABLE`](https://docs.python.org/3/library/gc.html#gc.DEBUG_UNCOLLECTABLE "gc.DEBUG_UNCOLLECTABLE") is set, in addition all uncollectable objects are printed.
Changed in version 3.4: Following [**PEP 442**](https://peps.python.org/pep-0442/), objects with a [`__del__()`](https://docs.python.org/3/reference/datamodel.html#object.__del__ "object.__del__") method don’t end up in [`gc.garbage`](https://docs.python.org/3/library/gc.html#gc.garbage "gc.garbage") anymore.

gc.callbacks[¶](https://docs.python.org/3/library/gc.html#gc.callbacks "Link to this definition")

A list of callbacks that will be invoked by the garbage collector before and after collection. The callbacks will be called with two arguments, _phase_ and _info_.
_phase_ can be one of two values:
> “start”: The garbage collection is about to start.
> “stop”: The garbage collection has finished.
_info_ is a dict providing more information for the callback. The following keys are currently defined:
> “generation”: The oldest generation being collected.
> “collected”: When _phase_ is “stop”, the number of objects successfully collected.
> “uncollectable”: When _phase_ is “stop”, the number of objects that could not be collected and were put in [`garbage`](https://docs.python.org/3/library/gc.html#gc.garbage "gc.garbage").
Applications can add their own callbacks to this list. The primary use cases are:
> Gathering statistics about garbage collection, such as how often various generations are collected, and how long the collection takes.
> Allowing applications to identify and clear their own uncollectable types when they appear in [`garbage`](https://docs.python.org/3/library/gc.html#gc.garbage "gc.garbage").
Added in version 3.3.
The following constants are provided for use with [`set_debug()`](https://docs.python.org/3/library/gc.html#gc.set_debug "gc.set_debug"):

gc.DEBUG_STATS[¶](https://docs.python.org/3/library/gc.html#gc.DEBUG_STATS "Link to this definition")

Print statistics during collection. This information can be useful when tuning the collection frequency.

gc.DEBUG_COLLECTABLE[¶](https://docs.python.org/3/library/gc.html#gc.DEBUG_COLLECTABLE "Link to this definition")

Print information on collectable objects found.

gc.DEBUG_UNCOLLECTABLE[¶](https://docs.python.org/3/library/gc.html#gc.DEBUG_UNCOLLECTABLE "Link to this definition")

Print information of uncollectable objects found (objects which are not reachable but cannot be freed by the collector). These objects will be added to the `garbage` list.
Changed in version 3.2: Also print the contents of the [`garbage`](https://docs.python.org/3/library/gc.html#gc.garbage "gc.garbage") list at [interpreter shutdown](https://docs.python.org/3/glossary.html#term-interpreter-shutdown), if it isn’t empty.

gc.DEBUG_SAVEALL[¶](https://docs.python.org/3/library/gc.html#gc.DEBUG_SAVEALL "Link to this definition")

When set, all unreachable objects found will be appended to _garbage_ rather than being freed. This can be useful for debugging a leaking program.

gc.DEBUG_LEAK[¶](https://docs.python.org/3/library/gc.html#gc.DEBUG_LEAK "Link to this definition")

The debugging flags necessary for the collector to print information about a leaking program (equal to `DEBUG_COLLECTABLE | DEBUG_UNCOLLECTABLE | DEBUG_SAVEALL`).
#### Previous topic
[`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html "previous chapter")
#### Next topic
[`inspect` — Inspect live objects](https://docs.python.org/3/library/inspect.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=gc+%E2%80%94+Garbage+Collector+interface&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgc.html&pagesource=library%2Fgc.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/inspect.html "inspect — Inspect live objects") |
  * [previous](https://docs.python.org/3/library/__future__.html "__future__ — Future statement definitions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Python Runtime Services](https://docs.python.org/3/library/python.html) »
  * [`gc` — Garbage Collector interface](https://docs.python.org/3/library/gc.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
