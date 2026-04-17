[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`multiprocessing` — Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html "previous chapter")
#### Next topic
[The `concurrent` package](https://docs.python.org/3/library/concurrent.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=multiprocessing.shared_memory+%E2%80%94+Shared+memory+for+direct+access+across+processes&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmultiprocessing.shared_memory.html&pagesource=library%2Fmultiprocessing.shared_memory.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/concurrent.html "The concurrent package") |
  * [previous](https://docs.python.org/3/library/multiprocessing.html "multiprocessing — Process-based parallelism") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`multiprocessing.shared_memory` — Shared memory for direct access across processes](https://docs.python.org/3/library/multiprocessing.shared_memory.html)
  * |
  * Theme  Auto Light Dark |


#  `multiprocessing.shared_memory` — Shared memory for direct access across processes[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#module-multiprocessing.shared_memory "Link to this heading")
**Source code:**
Added in version 3.8.
* * *
This module provides a class, [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory"), for the allocation and management of shared memory to be accessed by one or more processes on a multicore or symmetric multiprocessor (SMP) machine. To assist with the life-cycle management of shared memory especially across distinct processes, a [`BaseManager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager "multiprocessing.managers.BaseManager") subclass, [`SharedMemoryManager`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager "multiprocessing.managers.SharedMemoryManager"), is also provided in the [`multiprocessing.managers`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.managers "multiprocessing.managers: Share data between process with shared objects.") module.
In this module, shared memory refers to “POSIX style” shared memory blocks (though is not necessarily implemented explicitly as such) and does not refer to “distributed shared memory”. This style of shared memory permits distinct processes to potentially read and write to a common (or shared) region of volatile memory. Processes are conventionally limited to only have access to their own process memory space but shared memory permits the sharing of data between processes, avoiding the need to instead send messages between processes containing that data. Sharing data directly via memory can provide significant performance benefits compared to sharing data via disk or socket or other communications requiring the serialization/deserialization and copying of data.

_class_ multiprocessing.shared_memory.SharedMemory(_name =None_, _create =False_, _size =0_, _*_ , _track =True_)[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "Link to this definition")

Create an instance of the `SharedMemory` class for either creating a new shared memory block or attaching to an existing shared memory block. Each shared memory block is assigned a unique name. In this way, one process can create a shared memory block with a particular name and a different process can attach to that same shared memory block using that same name.
As a resource for sharing data across processes, shared memory blocks may outlive the original process that created them. When one process no longer needs access to a shared memory block that might still be needed by other processes, the [`close()`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.close "multiprocessing.shared_memory.SharedMemory.close") method should be called. When a shared memory block is no longer needed by any process, the [`unlink()`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.unlink "multiprocessing.shared_memory.SharedMemory.unlink") method should be called to ensure proper cleanup.

Parameters:

  * **name** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "str") _|__None_) – The unique name for the requested shared memory, specified as a string. When creating a new shared memory block, if `None` (the default) is supplied for the name, a novel name will be generated.
  * **create** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – Control whether a new shared memory block is created (`True`) or an existing shared memory block is attached (`False`).
  * **size** ([_int_](https://docs.python.org/3/library/functions.html#int "int")) – The requested number of bytes when creating a new shared memory block. Because some platforms choose to allocate chunks of memory based upon that platform’s memory page size, the exact size of the shared memory block may be larger or equal to the size requested. When attaching to an existing shared memory block, the _size_ parameter is ignored.
  * **track** ([_bool_](https://docs.python.org/3/library/functions.html#bool "bool")) – When `True`, register the shared memory block with a resource tracker process on platforms where the OS does not do this automatically. The resource tracker ensures proper cleanup of the shared memory even if all other processes with access to the memory exit without doing so. Python processes created from a common ancestor using [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") facilities share a single resource tracker process, and the lifetime of shared memory segments is handled automatically among these processes. Python processes created in any other way will receive their own resource tracker when accessing shared memory with _track_ enabled. This will cause the shared memory to be deleted by the resource tracker of the first process that terminates. To avoid this issue, users of [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") or standalone Python processes should set _track_ to `False` when there is already another process in place that does the bookkeeping. _track_ is ignored on Windows, which has its own tracking and automatically deletes shared memory when all handles to it have been closed.


Changed in version 3.13: Added the _track_ parameter.

close()[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.close "Link to this definition")

Close the file descriptor/handle to the shared memory from this instance. `close()` should be called once access to the shared memory block from this instance is no longer needed. Depending on operating system, the underlying memory may or may not be freed even if all handles to it have been closed. To ensure proper cleanup, use the [`unlink()`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.unlink "multiprocessing.shared_memory.SharedMemory.unlink") method.

unlink()[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.unlink "Link to this definition")

Delete the underlying shared memory block. This should be called only once per shared memory block regardless of the number of handles to it, even in other processes. `unlink()` and [`close()`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.close "multiprocessing.shared_memory.SharedMemory.close") can be called in any order, but trying to access data inside a shared memory block after `unlink()` may result in memory access errors, depending on platform.
This method has no effect on Windows, where the only way to delete a shared memory block is to close all handles.

buf[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.buf "Link to this definition")

A memoryview of contents of the shared memory block.

name[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.name "Link to this definition")

Read-only access to the unique name of the shared memory block.

size[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.size "Link to this definition")

Read-only access to size in bytes of the shared memory block.
The following example demonstrates low-level use of [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory") instances:
Copy```
>>> from multiprocessing import shared_memory
>>> shm_a = shared_memory.SharedMemory(create=True, size=10)
>>> type(shm_a.buf)
<class 'memoryview'>
>>> buffer = shm_a.buf
>>> len(buffer)
10
>>> buffer[:4] = bytearray([22, 33, 44, 55])  # Modify multiple at once
>>> buffer[4] = 100                           # Modify single byte at a time
>>> # Attach to an existing shared memory block
>>> shm_b = shared_memory.SharedMemory(shm_a.name)
>>> import array
>>> array.array('b', shm_b.buf[:5])  # Copy the data into a new array.array
array('b', [22, 33, 44, 55, 100])
>>> shm_b.buf[:5] = b'howdy'  # Modify via shm_b using bytes
>>> bytes(shm_a.buf[:5])      # Access via shm_a
b'howdy'
>>> shm_b.close()   # Close each SharedMemory instance
>>> shm_a.close()
>>> shm_a.unlink()  # Call unlink only once to release the shared memory

```

The following example demonstrates a practical use of the [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory") class with `numpy.ndarray` from two distinct Python shells:
Copy```
>>> # In the first Python interactive shell
>>> import numpy as np
>>> a = np.array([1, 1, 2, 3, 5, 8])  # Start with an existing NumPy array
>>> from multiprocessing import shared_memory
>>> shm = shared_memory.SharedMemory(create=True, size=a.nbytes)
>>> # Now create a NumPy array backed by shared memory
>>> b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
>>> b[:] = a[:]  # Copy the original data into shared memory
>>> b
array([1, 1, 2, 3, 5, 8])
>>> type(b)
<class 'numpy.ndarray'>
>>> type(a)
<class 'numpy.ndarray'>
>>> shm.name  # We did not specify a name so one was chosen for us
'psm_21467_46075'

>>> # In either the same shell or a new Python shell on the same machine
>>> import numpy as np
>>> from multiprocessing import shared_memory
>>> # Attach to the existing shared memory block
>>> existing_shm = shared_memory.SharedMemory(name='psm_21467_46075')
>>> # Note that a.shape is (6,) and a.dtype is np.int64 in this example
>>> c = np.ndarray((6,), dtype=np.int64, buffer=existing_shm.buf)
>>> c
array([1, 1, 2, 3, 5, 8])
>>> c[-1] = 888
>>> c
array([  1,   1,   2,   3,   5, 888])

>>> # Back in the first Python interactive shell, b reflects this change
>>> b
array([  1,   1,   2,   3,   5, 888])

>>> # Clean up from within the second Python shell
>>> del c  # Unnecessary; merely emphasizing the array is no longer used
>>> existing_shm.close()

>>> # Clean up from within the first Python shell
>>> del b  # Unnecessary; merely emphasizing the array is no longer used
>>> shm.close()
>>> shm.unlink()  # Free and release the shared memory block at the very end

```


_class_ multiprocessing.managers.SharedMemoryManager([_address_[, _authkey_]])[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager "Link to this definition")

A subclass of [`multiprocessing.managers.BaseManager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager "multiprocessing.managers.BaseManager") which can be used for the management of shared memory blocks across processes.
A call to [`start()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.start "multiprocessing.managers.BaseManager.start") on a `SharedMemoryManager` instance causes a new process to be started. This new process’s sole purpose is to manage the life cycle of all shared memory blocks created through it. To trigger the release of all shared memory blocks managed by that process, call [`shutdown()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.shutdown "multiprocessing.managers.BaseManager.shutdown") on the instance. This triggers a [`unlink()`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.unlink "multiprocessing.shared_memory.SharedMemory.unlink") call on all of the [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager.SharedMemory "multiprocessing.managers.SharedMemoryManager.SharedMemory") objects managed by that process and then stops the process itself. By creating `SharedMemory` instances through a `SharedMemoryManager`, we avoid the need to manually track and trigger the freeing of shared memory resources.
This class provides methods for creating and returning [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager.SharedMemory "multiprocessing.managers.SharedMemoryManager.SharedMemory") instances and for creating a list-like object ([`ShareableList`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager.ShareableList "multiprocessing.managers.SharedMemoryManager.ShareableList")) backed by shared memory.
Refer to [`BaseManager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager "multiprocessing.managers.BaseManager") for a description of the inherited _address_ and _authkey_ optional input arguments and how they may be used to connect to an existing `SharedMemoryManager` service from other processes.

SharedMemory(_size_)[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager.SharedMemory "Link to this definition")

Create and return a new [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager.SharedMemory "multiprocessing.managers.SharedMemoryManager.SharedMemory") object with the specified _size_ in bytes.

ShareableList(_sequence_)[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager.ShareableList "Link to this definition")

Create and return a new [`ShareableList`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager.ShareableList "multiprocessing.managers.SharedMemoryManager.ShareableList") object, initialized by the values from the input _sequence_.
The following example demonstrates the basic mechanisms of a [`SharedMemoryManager`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager "multiprocessing.managers.SharedMemoryManager"):
Copy```
>>> from multiprocessing.managers import SharedMemoryManager
>>> smm = SharedMemoryManager()
>>> smm.start()  # Start the process that manages the shared memory blocks
>>> sl = smm.ShareableList(range(4))
>>> sl
ShareableList([0, 1, 2, 3], name='psm_6572_7512')
>>> raw_shm = smm.SharedMemory(size=128)
>>> another_sl = smm.ShareableList('alpha')
>>> another_sl
ShareableList(['a', 'l', 'p', 'h', 'a'], name='psm_6572_12221')
>>> smm.shutdown()  # Calls unlink() on sl, raw_shm, and another_sl

```

The following example depicts a potentially more convenient pattern for using [`SharedMemoryManager`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager "multiprocessing.managers.SharedMemoryManager") objects via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement to ensure that all shared memory blocks are released after they are no longer needed:
Copy```
>>> with SharedMemoryManager() as smm:
...     sl = smm.ShareableList(range(2000))
...     # Divide the work among two processes, storing partial results in sl
...     p1 = Process(target=do_work, args=(sl, 0, 1000))
...     p2 = Process(target=do_work, args=(sl, 1000, 2000))
...     p1.start()
...     p2.start()  # A multiprocessing.Pool might be more efficient
...     p1.join()
...     p2.join()   # Wait for all work to complete in both processes
...     total_result = sum(sl)  # Consolidate the partial results now in sl

```

When using a [`SharedMemoryManager`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager "multiprocessing.managers.SharedMemoryManager") in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement, the shared memory blocks created using that manager are all released when the `with` statement’s code block finishes execution.

_class_ multiprocessing.shared_memory.ShareableList(_sequence =None_, _*_ , _name =None_)[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList "Link to this definition")

Provide a mutable list-like object where all values stored within are stored in a shared memory block. This constrains storable values to the following built-in data types:
  * [`int`](https://docs.python.org/3/library/functions.html#int "int") (signed 64-bit)
  * [`float`](https://docs.python.org/3/library/functions.html#float "float")
  * [`bool`](https://docs.python.org/3/library/functions.html#bool "bool")
  * [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") (less than 10M bytes each when encoded as UTF-8)
  * [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") (less than 10M bytes each)
  * `None`


It also notably differs from the built-in [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") type in that these lists can not change their overall length (i.e. no `append()`, `insert()`, etc.) and do not support the dynamic creation of new `ShareableList` instances via slicing.
_sequence_ is used in populating a new `ShareableList` full of values. Set to `None` to instead attach to an already existing `ShareableList` by its unique shared memory name.
_name_ is the unique name for the requested shared memory, as described in the definition for [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory"). When attaching to an existing `ShareableList`, specify its shared memory block’s unique name while leaving _sequence_ set to `None`.
Note
A known issue exists for [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") values. If they end with `\x00` nul bytes or characters, those may be _silently stripped_ when fetching them by index from the `ShareableList`. This `.rstrip(b'\x00')` behavior is considered a bug and may go away in the future. See
For applications where rstripping of trailing nulls is a problem, work around it by always unconditionally appending an extra non-0 byte to the end of such values when storing and unconditionally removing it when fetching:
Copy```
>>> from multiprocessing import shared_memory
>>> nul_bug_demo = shared_memory.ShareableList(['?\x00', b'\x03\x02\x01\x00\x00\x00'])
>>> nul_bug_demo[0]
'?'
>>> nul_bug_demo[1]
b'\x03\x02\x01'
>>> nul_bug_demo.shm.unlink()
>>> padded = shared_memory.ShareableList(['?\x00\x07', b'\x03\x02\x01\x00\x00\x00\x07'])
>>> padded[0][:-1]
'?\x00'
>>> padded[1][:-1]
b'\x03\x02\x01\x00\x00\x00'
>>> padded.shm.unlink()

```


count(_value_)[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList.count "Link to this definition")

Return the number of occurrences of _value_.

index(_value_)[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList.index "Link to this definition")

Return first index position of _value_. Raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if _value_ is not present.

format[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList.format "Link to this definition")

Read-only attribute containing the [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.") packing format used by all currently stored values.

shm[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList.shm "Link to this definition")

The [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory") instance where the values are stored.
The following example demonstrates basic use of a [`ShareableList`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList "multiprocessing.shared_memory.ShareableList") instance:
Copy```
>>> from multiprocessing import shared_memory
>>> a = shared_memory.ShareableList(['howdy', b'HoWdY', -273.154, 100, None, True, 42])
>>> [ type(entry) for entry in a ]
[<class 'str'>, <class 'bytes'>, <class 'float'>, <class 'int'>, <class 'NoneType'>, <class 'bool'>, <class 'int'>]
>>> a[2]
-273.154
>>> a[2] = -78.5
>>> a[2]
-78.5
>>> a[2] = 'dry ice'  # Changing data types is supported as well
>>> a[2]
'dry ice'
>>> a[2] = 'larger than previously allocated storage space'
Traceback (most recent call last):
  ...
ValueError: exceeds available storage for existing str
>>> a[2]
'dry ice'
>>> len(a)
7
>>> a.index(42)
6
>>> a.count(b'howdy')
0
>>> a.count(b'HoWdY')
1
>>> a.shm.close()
>>> a.shm.unlink()
>>> del a  # Use of a ShareableList after call to unlink() is unsupported

```

The following example depicts how one, two, or many processes may access the same [`ShareableList`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList "multiprocessing.shared_memory.ShareableList") by supplying the name of the shared memory block behind it:
Copy```
>>> b = shared_memory.ShareableList(range(5))         # In a first process
>>> c = shared_memory.ShareableList(name=b.shm.name)  # In a second process
>>> c
ShareableList([0, 1, 2, 3, 4], name='...')
>>> c[-1] = -999
>>> b[-1]
-999
>>> b.shm.close()
>>> c.shm.close()
>>> c.shm.unlink()

```

The following examples demonstrates that [`ShareableList`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList "multiprocessing.shared_memory.ShareableList") (and underlying [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory")) objects can be pickled and unpickled if needed. Note, that it will still be the same shared object. This happens, because the deserialized object has the same unique name and is just attached to an existing object with the same name (if the object is still alive):
Copy```
>>> import pickle
>>> from multiprocessing import shared_memory
>>> sl = shared_memory.ShareableList(range(10))
>>> list(sl)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```

Copy```
>>> deserialized_sl = pickle.loads(pickle.dumps(sl))
>>> list(deserialized_sl)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```

Copy```
>>> sl[0] = -1
>>> deserialized_sl[1] = -2
>>> list(sl)
[-1, -2, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(deserialized_sl)
[-1, -2, 2, 3, 4, 5, 6, 7, 8, 9]

```

Copy```
>>> sl.shm.close()
>>> sl.shm.unlink()

```

#### Previous topic
[`multiprocessing` — Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html "previous chapter")
#### Next topic
[The `concurrent` package](https://docs.python.org/3/library/concurrent.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=multiprocessing.shared_memory+%E2%80%94+Shared+memory+for+direct+access+across+processes&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmultiprocessing.shared_memory.html&pagesource=library%2Fmultiprocessing.shared_memory.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/concurrent.html "The concurrent package") |
  * [previous](https://docs.python.org/3/library/multiprocessing.html "multiprocessing — Process-based parallelism") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Concurrent Execution](https://docs.python.org/3/library/concurrency.html) »
  * [`multiprocessing.shared_memory` — Shared memory for direct access across processes](https://docs.python.org/3/library/multiprocessing.shared_memory.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
