[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [Thread Safety Guarantees](https://docs.python.org/3/library/threadsafety.html)
    * [Thread safety for list objects](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-list-objects)
    * [Thread safety for dict objects](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-dict-objects)


#### Previous topic
[Built-in Exceptions](https://docs.python.org/3/library/exceptions.html "previous chapter")
#### Next topic
[Text Processing Services](https://docs.python.org/3/library/text.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Thread+Safety+Guarantees&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fthreadsafety.html&pagesource=library%2Fthreadsafety.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/text.html "Text Processing Services") |
  * [previous](https://docs.python.org/3/library/exceptions.html "Built-in Exceptions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Thread Safety Guarantees](https://docs.python.org/3/library/threadsafety.html)
  * |
  * Theme  Auto Light Dark |


# Thread Safety Guarantees[¶](https://docs.python.org/3/library/threadsafety.html#thread-safety-guarantees "Link to this heading")
This page documents thread-safety guarantees for built-in types in Python’s free-threaded build. The guarantees described here apply when using Python with the [GIL](https://docs.python.org/3/glossary.html#term-GIL) disabled (free-threaded mode). When the GIL is enabled, most operations are implicitly serialized.
For general guidance on writing thread-safe code in free-threaded Python, see [Python support for free threading](https://docs.python.org/3/howto/free-threading-python.html#freethreading-python-howto).
## Thread safety for list objects[¶](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-list-objects "Link to this heading")
Reading a single element from a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") is [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation):
Copy```
lst[i]   # list.__getitem__

```

The following methods traverse the list and use [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation) reads of each item to perform their function. That means that they may return results affected by concurrent modifications:
Copy```
item in lst
lst.index(item)
lst.count(item)

```

All of the above operations avoid acquiring [per-object locks](https://docs.python.org/3/glossary.html#term-per-object-lock). They do not block concurrent modifications. Other operations that hold a lock will not block these from observing intermediate states.
All other operations from here on block using the [per-object lock](https://docs.python.org/3/glossary.html#term-per-object-lock).
Writing a single item via `lst[i] = x` is safe to call from multiple threads and will not corrupt the list.
The following operations return new objects and appear [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation) to other threads:
Copy```
lst1 + lst2    # concatenates two lists into a new list
x * lst        # repeats lst x times into a new list
lst.copy()     # returns a shallow copy of the list

```

The following methods that only operate on a single element with no shifting required are [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation):
Copy```
lst.append(x)  # append to the end of the list, no shifting required
lst.pop()      # pop element from the end of the list, no shifting required

```

The [`clear()`](https://docs.python.org/3/library/stdtypes.html#list.clear "list.clear") method is also [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation). Other threads cannot observe elements being removed.
The [`sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort "list.sort") method is not [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation). Other threads cannot observe intermediate states during sorting, but the list appears empty for the duration of the sort.
The following operations may allow [lock-free](https://docs.python.org/3/glossary.html#term-lock-free) operations to observe intermediate states since they modify multiple elements in place:
Copy```
lst.insert(idx, item)  # shifts elements
lst.pop(idx)           # idx not at the end of the list, shifts elements
lst *= x               # copies elements in place

```

The [`remove()`](https://docs.python.org/3/library/stdtypes.html#list.remove "list.remove") method may allow concurrent modifications since element comparison may execute arbitrary Python code (via [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")).
[`extend()`](https://docs.python.org/3/library/stdtypes.html#list.extend "list.extend") is safe to call from multiple threads. However, its guarantees depend on the iterable passed to it. If it is a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"), a [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), a [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset"), a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") or a [dictionary view object](https://docs.python.org/3/library/stdtypes.html#dict-views) (but not their subclasses), the `extend` operation is safe from concurrent modifications to the iterable. Otherwise, an iterator is created which can be concurrently modified by another thread. The same applies to inplace concatenation of a list with other iterables when using `lst += iterable`.
Similarly, assigning to a list slice with `lst[i:j] = iterable` is safe to call from multiple threads, but `iterable` is only locked when it is also a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") (but not its subclasses).
Operations that involve multiple accesses, as well as iteration, are never atomic. For example:
Copy```
# NOT atomic: read-modify-write
lst[i] = lst[i] + 1

# NOT atomic: check-then-act
if lst:
    item = lst.pop()

# NOT thread-safe: iteration while modifying
for item in lst:
    process(item)  # another thread may modify lst

```

Consider external synchronization when sharing [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") instances across threads.
## Thread safety for dict objects[¶](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-dict-objects "Link to this heading")
Creating a dictionary with the [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") constructor is atomic when the argument to it is a `dict` or a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"). When using the [`dict.fromkeys()`](https://docs.python.org/3/library/stdtypes.html#dict.fromkeys "dict.fromkeys") method, dictionary creation is atomic when the argument is a `dict`, `tuple`, [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") or [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset").
The following operations and functions are [lock-free](https://docs.python.org/3/glossary.html#term-lock-free) and [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation).
Copy```
d[key]       # dict.__getitem__
d.get(key)   # dict.get
key in d     # dict.__contains__
len(d)       # dict.__len__

```

All other operations from here on hold the [per-object lock](https://docs.python.org/3/glossary.html#term-per-object-lock).
Writing or removing a single item is safe to call from multiple threads and will not corrupt the dictionary:
Copy```
d[key] = value        # write
del d[key]            # delete
d.pop(key)            # remove and return
d.popitem()           # remove and return last item
d.setdefault(key, v)  # insert if missing

```

These operations may compare keys using [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__"), which can execute arbitrary Python code. During such comparisons, the dictionary may be modified by another thread. For built-in types like [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`int`](https://docs.python.org/3/library/functions.html#int "int"), and [`float`](https://docs.python.org/3/library/functions.html#float "float"), that implement `__eq__()` in C, the underlying lock is not released during comparisons and this is not a concern.
The following operations return new objects and hold the [per-object lock](https://docs.python.org/3/glossary.html#term-per-object-lock) for the duration of the operation:
Copy```
d.copy()      # returns a shallow copy of the dictionary
d | other     # merges two dicts into a new dict
d.keys()      # returns a new dict_keys view object
d.values()    # returns a new dict_values view object
d.items()     # returns a new dict_items view object

```

The [`clear()`](https://docs.python.org/3/library/stdtypes.html#dict.clear "dict.clear") method holds the lock for its duration. Other threads cannot observe elements being removed.
The following operations lock both dictionaries. For [`update()`](https://docs.python.org/3/library/stdtypes.html#dict.update "dict.update") and `|=`, this applies only when the other operand is a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") that uses the standard dict iterator (but not subclasses that override iteration). For equality comparison, this applies to `dict` and its subclasses:
Copy```
d.update(other_dict)  # both locked when other_dict is a dict
d |= other_dict       # both locked when other_dict is a dict
d == other_dict       # both locked for dict and subclasses

```

All comparison operations also compare values using [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__"), so for non-built-in types the lock may be released during comparison.
[`fromkeys()`](https://docs.python.org/3/library/stdtypes.html#dict.fromkeys "dict.fromkeys") locks both the new dictionary and the iterable when the iterable is exactly a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), or [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") (not subclasses):
Copy```
dict.fromkeys(a_dict)      # locks both
dict.fromkeys(a_set)       # locks both
dict.fromkeys(a_frozenset) # locks both

```

When updating from a non-dict iterable, only the target dictionary is locked. The iterable may be concurrently modified by another thread:
Copy```
d.update(iterable)        # iterable is not a dict: only d locked
d |= iterable             # iterable is not a dict: only d locked
dict.fromkeys(iterable)   # iterable is not a dict/set/frozenset: only result locked

```

Operations that involve multiple accesses, as well as iteration, are never atomic:
Copy```
# NOT atomic: read-modify-write
d[key] = d[key] + 1

# NOT atomic: check-then-act (TOCTOU)
if key in d:
    del d[key]

# NOT thread-safe: iteration while modifying
for key, value in d.items():
    process(key)  # another thread may modify d

```

To avoid time-of-check to time-of-use (TOCTOU) issues, use atomic operations or handle exceptions:
Copy```
# Use pop() with default instead of check-then-delete
d.pop(key, None)

# Or handle the exception
try:
    del d[key]
except KeyError:
    pass

```

To safely iterate over a dictionary that may be modified by another thread, iterate over a copy:
Copy```
# Make a copy to iterate safely
for key, value in d.copy().items():
    process(key)

```

Consider external synchronization when sharing [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") instances across threads.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [Thread Safety Guarantees](https://docs.python.org/3/library/threadsafety.html)
    * [Thread safety for list objects](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-list-objects)
    * [Thread safety for dict objects](https://docs.python.org/3/library/threadsafety.html#thread-safety-for-dict-objects)


#### Previous topic
[Built-in Exceptions](https://docs.python.org/3/library/exceptions.html "previous chapter")
#### Next topic
[Text Processing Services](https://docs.python.org/3/library/text.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Thread+Safety+Guarantees&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fthreadsafety.html&pagesource=library%2Fthreadsafety.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/text.html "Text Processing Services") |
  * [previous](https://docs.python.org/3/library/exceptions.html "Built-in Exceptions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Thread Safety Guarantees](https://docs.python.org/3/library/threadsafety.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
