#  `pickle` — Python object serialization[¶](https://docs.python.org/3/library/pickle.html#module-pickle "Link to this heading")
**Source code:**
* * *
The `pickle` module implements binary protocols for serializing and de-serializing a Python object structure. _“Pickling”_ is the process whereby a Python object hierarchy is converted into a byte stream, and _“unpickling”_ is the inverse operation, whereby a byte stream (from a [binary file](https://docs.python.org/3/glossary.html#term-binary-file) or [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” [[1]](https://docs.python.org/3/library/pickle.html#id7) or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.
Warning
The `pickle` module **is not secure**. Only unpickle data you trust.
It is possible to construct malicious pickle data which will **execute arbitrary code during unpickling**. Never unpickle data that could have come from an untrusted source, or that could have been tampered with.
Consider signing data with [`hmac`](https://docs.python.org/3/library/hmac.html#module-hmac "hmac: Keyed-Hashing for Message Authentication \(HMAC\) implementation") if you need to ensure that it has not been tampered with.
Safer serialization formats such as [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.") may be more appropriate if you are processing untrusted data. See [Comparison with json](https://docs.python.org/3/library/pickle.html#comparison-with-json).
## Relationship to other Python modules[¶](https://docs.python.org/3/library/pickle.html#relationship-to-other-python-modules "Link to this heading")
### Comparison with `marshal`[¶](https://docs.python.org/3/library/pickle.html#comparison-with-marshal "Link to this heading")
Python has a more primitive serialization module called [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back \(with different constraints\)."), but in general `pickle` should always be the preferred way to serialize Python objects. `marshal` exists primarily to support Python’s `.pyc` files.
The `pickle` module differs from [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back \(with different constraints\).") in several significant ways:
  * [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back \(with different constraints\).") cannot be used to serialize user-defined classes and their instances. `pickle` can save and restore class instances transparently, however the class definition must be importable and live in the same module as when the object was stored.
  * The [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back \(with different constraints\).") serialization format is not guaranteed to be portable across Python versions. Because its primary job in life is to support `.pyc` files, the Python implementers reserve the right to change the serialization format in non-backwards compatible ways should the need arise. The `pickle` serialization format is guaranteed to be backwards compatible across Python releases provided a compatible pickle protocol is chosen and pickling and unpickling code deals with Python 2 to Python 3 type differences if your data is crossing that unique breaking change language boundary.


### Comparison with `json`[¶](https://docs.python.org/3/library/pickle.html#comparison-with-json "Link to this heading")
There are fundamental differences between the pickle protocols and
  * JSON is a text serialization format (it outputs unicode text, although most of the time it is then encoded to `utf-8`), while pickle is a binary serialization format;
  * JSON is human-readable, while pickle is not;
  * JSON is interoperable and widely used outside of the Python ecosystem, while pickle is Python-specific;
  * JSON, by default, can only represent a subset of the Python built-in types, and no custom classes; pickle can represent an extremely large number of Python types (many of them automatically, by clever usage of Python’s introspection facilities; complex cases can be tackled by implementing [specific object APIs](https://docs.python.org/3/library/pickle.html#pickle-inst));
  * Unlike pickle, deserializing untrusted JSON does not in itself create an arbitrary code execution vulnerability.


See also
The [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.") module: a standard library module allowing JSON serialization and deserialization.
## Data stream format[¶](https://docs.python.org/3/library/pickle.html#data-stream-format "Link to this heading")
The data format used by `pickle` is Python-specific. This has the advantage that there are no restrictions imposed by external standards such as JSON (which can’t represent pointer sharing); however it means that non-Python programs may not be able to reconstruct pickled Python objects.
By default, the `pickle` data format uses a relatively compact binary representation. If you need optimal size characteristics, you can efficiently [compress](https://docs.python.org/3/library/archiving.html) pickled data.
The module [`pickletools`](https://docs.python.org/3/library/pickletools.html#module-pickletools "pickletools: Contains extensive comments about the pickle protocols and pickle-machine opcodes, as well as some useful functions.") contains tools for analyzing data streams generated by `pickle`. `pickletools` source code has extensive comments about opcodes used by pickle protocols.
There are currently 6 different protocols which can be used for pickling. The higher the protocol used, the more recent the version of Python needed to read the pickle produced.
  * Protocol version 0 is the original “human-readable” protocol and is backwards compatible with earlier versions of Python.
  * Protocol version 1 is an old binary format which is also compatible with earlier versions of Python.
  * Protocol version 2 was introduced in Python 2.3. It provides much more efficient pickling of [new-style classes](https://docs.python.org/3/glossary.html#term-new-style-class). Refer to [**PEP 307**](https://peps.python.org/pep-0307/) for information about improvements brought by protocol 2.
  * Protocol version 3 was added in Python 3.0. It has explicit support for [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects and cannot be unpickled by Python 2.x. This was the default protocol in Python 3.0–3.7.
  * Protocol version 4 was added in Python 3.4. It adds support for very large objects, pickling more kinds of objects, and some data format optimizations. This was the default protocol in Python 3.8–3.13. Refer to [**PEP 3154**](https://peps.python.org/pep-3154/) for information about improvements brought by protocol 4.
  * Protocol version 5 was added in Python 3.8. It adds support for out-of-band data and speedup for in-band data. It is the default protocol starting with Python 3.14. Refer to [**PEP 574**](https://peps.python.org/pep-0574/) for information about improvements brought by protocol 5.


Note
Serialization is a more primitive notion than persistence; although `pickle` reads and writes file objects, it does not handle the issue of naming persistent objects, nor the (even more complicated) issue of concurrent access to persistent objects. The `pickle` module can transform a complex object into a byte stream and it can transform the byte stream into an object with the same internal structure. Perhaps the most obvious thing to do with these byte streams is to write them onto a file, but it is also conceivable to send them across a network or store them in a database. The [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.") module provides a simple interface to pickle and unpickle objects on DBM-style database files.
## Module Interface[¶](https://docs.python.org/3/library/pickle.html#module-interface "Link to this heading")
To serialize an object hierarchy, you simply call the [`dumps()`](https://docs.python.org/3/library/pickle.html#pickle.dumps "pickle.dumps") function. Similarly, to de-serialize a data stream, you call the [`loads()`](https://docs.python.org/3/library/pickle.html#pickle.loads "pickle.loads") function. However, if you want more control over serialization and de-serialization, you can create a [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") or an [`Unpickler`](https://docs.python.org/3/library/pickle.html#pickle.Unpickler "pickle.Unpickler") object, respectively.
The `pickle` module provides the following constants:

pickle.HIGHEST_PROTOCOL[¶](https://docs.python.org/3/library/pickle.html#pickle.HIGHEST_PROTOCOL "Link to this definition")

An integer, the highest [protocol version](https://docs.python.org/3/library/pickle.html#pickle-protocols) available. This value can be passed as a _protocol_ value to functions [`dump()`](https://docs.python.org/3/library/pickle.html#pickle.dump "pickle.dump") and [`dumps()`](https://docs.python.org/3/library/pickle.html#pickle.dumps "pickle.dumps") as well as the [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") constructor.

pickle.DEFAULT_PROTOCOL[¶](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "Link to this definition")

An integer, the default [protocol version](https://docs.python.org/3/library/pickle.html#pickle-protocols) used for pickling. May be less than [`HIGHEST_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.HIGHEST_PROTOCOL "pickle.HIGHEST_PROTOCOL"). Currently the default protocol is 5, introduced in Python 3.8 and incompatible with previous versions. This version introduces support for out-of-band buffers, where [**PEP 3118**](https://peps.python.org/pep-3118/)-compatible data can be transmitted separately from the main pickle stream.
Changed in version 3.0: The default protocol is 3.
Changed in version 3.8: The default protocol is 4.
Changed in version 3.14: The default protocol is 5.
The `pickle` module provides the following functions to make the pickling process more convenient:

pickle.dump(_obj_ , _file_ , _protocol =None_, _*_ , _fix_imports =True_, _buffer_callback =None_)[¶](https://docs.python.org/3/library/pickle.html#pickle.dump "Link to this definition")

Write the pickled representation of the object _obj_ to the open [file object](https://docs.python.org/3/glossary.html#term-file-object) _file_. This is equivalent to `Pickler(file, protocol).dump(obj)`.
Arguments _file_ , _protocol_ , _fix_imports_ and _buffer_callback_ have the same meaning as in the [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") constructor.
Changed in version 3.8: The _buffer_callback_ argument was added.

pickle.dumps(_obj_ , _protocol =None_, _*_ , _fix_imports =True_, _buffer_callback =None_)[¶](https://docs.python.org/3/library/pickle.html#pickle.dumps "Link to this definition")

Return the pickled representation of the object _obj_ as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object, instead of writing it to a file.
Arguments _protocol_ , _fix_imports_ and _buffer_callback_ have the same meaning as in the [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") constructor.
Changed in version 3.8: The _buffer_callback_ argument was added.

pickle.load(_file_ , _*_ , _fix_imports =True_, _encoding ='ASCII'_, _errors ='strict'_, _buffers =None_)[¶](https://docs.python.org/3/library/pickle.html#pickle.load "Link to this definition")

Read the pickled representation of an object from the open [file object](https://docs.python.org/3/glossary.html#term-file-object) _file_ and return the reconstituted object hierarchy specified therein. This is equivalent to `Unpickler(file).load()`.
The protocol version of the pickle is detected automatically, so no protocol argument is needed. Bytes past the pickled representation of the object are ignored.
Arguments _file_ , _fix_imports_ , _encoding_ , _errors_ , _strict_ and _buffers_ have the same meaning as in the [`Unpickler`](https://docs.python.org/3/library/pickle.html#pickle.Unpickler "pickle.Unpickler") constructor.
Changed in version 3.8: The _buffers_ argument was added.

pickle.loads(_data_ , _/_ , _*_ , _fix_imports =True_, _encoding ='ASCII'_, _errors ='strict'_, _buffers =None_)[¶](https://docs.python.org/3/library/pickle.html#pickle.loads "Link to this definition")

Return the reconstituted object hierarchy of the pickled representation _data_ of an object. _data_ must be a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).
The protocol version of the pickle is detected automatically, so no protocol argument is needed. Bytes past the pickled representation of the object are ignored.
Arguments _fix_imports_ , _encoding_ , _errors_ , _strict_ and _buffers_ have the same meaning as in the [`Unpickler`](https://docs.python.org/3/library/pickle.html#pickle.Unpickler "pickle.Unpickler") constructor.
Changed in version 3.8: The _buffers_ argument was added.
The `pickle` module defines three exceptions:

_exception_ pickle.PickleError[¶](https://docs.python.org/3/library/pickle.html#pickle.PickleError "Link to this definition")

Common base class for the other pickling exceptions. It inherits from [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception").

_exception_ pickle.PicklingError[¶](https://docs.python.org/3/library/pickle.html#pickle.PicklingError "Link to this definition")

Error raised when an unpicklable object is encountered by [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler"). It inherits from [`PickleError`](https://docs.python.org/3/library/pickle.html#pickle.PickleError "pickle.PickleError").
Refer to [What can be pickled and unpickled?](https://docs.python.org/3/library/pickle.html#pickle-picklable) to learn what kinds of objects can be pickled.

_exception_ pickle.UnpicklingError[¶](https://docs.python.org/3/library/pickle.html#pickle.UnpicklingError "Link to this definition")

Error raised when there is a problem unpickling an object, such as a data corruption or a security violation. It inherits from [`PickleError`](https://docs.python.org/3/library/pickle.html#pickle.PickleError "pickle.PickleError").
Note that other exceptions may also be raised during unpickling, including (but not necessarily limited to) AttributeError, EOFError, ImportError, and IndexError.
The `pickle` module exports three classes, [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler"), [`Unpickler`](https://docs.python.org/3/library/pickle.html#pickle.Unpickler "pickle.Unpickler") and [`PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer"):

_class_ pickle.Pickler(_file_ , _protocol =None_, _*_ , _fix_imports =True_, _buffer_callback =None_)[¶](https://docs.python.org/3/library/pickle.html#pickle.Pickler "Link to this definition")

This takes a binary file for writing a pickle data stream.
The optional _protocol_ argument, an integer, tells the pickler to use the given protocol; supported protocols are 0 to [`HIGHEST_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.HIGHEST_PROTOCOL "pickle.HIGHEST_PROTOCOL"). If not specified, the default is [`DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL"). If a negative number is specified, `HIGHEST_PROTOCOL` is selected.
The _file_ argument must have a write() method that accepts a single bytes argument. It can thus be an on-disk file opened for binary writing, an [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") instance, or any other custom object that meets this interface.
If _fix_imports_ is true and _protocol_ is less than 3, pickle will try to map the new Python 3 names to the old module names used in Python 2, so that the pickle data stream is readable with Python 2.
If _buffer_callback_ is `None` (the default), buffer views are serialized into _file_ as part of the pickle stream.
If _buffer_callback_ is not `None`, then it can be called any number of times with a buffer view. If the callback returns a false value (such as `None`), the given buffer is [out-of-band](https://docs.python.org/3/library/pickle.html#pickle-oob); otherwise the buffer is serialized in-band, i.e. inside the pickle stream.
It is an error if _buffer_callback_ is not `None` and _protocol_ is `None` or smaller than 5.
Changed in version 3.8: The _buffer_callback_ argument was added.

dump(_obj_)[¶](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dump "Link to this definition")

Write the pickled representation of _obj_ to the open file object given in the constructor.

persistent_id(_obj_)[¶](https://docs.python.org/3/library/pickle.html#pickle.Pickler.persistent_id "Link to this definition")

Do nothing by default. This exists so a subclass can override it.
If `persistent_id()` returns `None`, _obj_ is pickled as usual. Any other value causes `Pickler` to emit the returned value as a persistent ID for _obj_. The meaning of this persistent ID should be defined by [`Unpickler.persistent_load()`](https://docs.python.org/3/library/pickle.html#pickle.Unpickler.persistent_load "pickle.Unpickler.persistent_load"). Note that the value returned by `persistent_id()` cannot itself have a persistent ID.
See [Persistence of External Objects](https://docs.python.org/3/library/pickle.html#pickle-persistent) for details and examples of uses.
Changed in version 3.13: Add the default implementation of this method in the C implementation of `Pickler`.

dispatch_table[¶](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "Link to this definition")

A pickler object’s dispatch table is a registry of _reduction functions_ of the kind which can be declared using [`copyreg.pickle()`](https://docs.python.org/3/library/copyreg.html#copyreg.pickle "copyreg.pickle"). It is a mapping whose keys are classes and whose values are reduction functions. A reduction function takes a single argument of the associated class and should conform to the same interface as a [`__reduce__()`](https://docs.python.org/3/library/pickle.html#object.__reduce__ "object.__reduce__") method.
By default, a pickler object will not have a [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table") attribute, and it will instead use the global dispatch table managed by the [`copyreg`](https://docs.python.org/3/library/copyreg.html#module-copyreg "copyreg: Register pickle support functions.") module. However, to customize the pickling for a specific pickler object one can set the `dispatch_table` attribute to a dict-like object. Alternatively, if a subclass of `Pickler` has a `dispatch_table` attribute then this will be used as the default dispatch table for instances of that class.
See [Dispatch Tables](https://docs.python.org/3/library/pickle.html#pickle-dispatch) for usage examples.
Added in version 3.3.

reducer_override(_obj_)[¶](https://docs.python.org/3/library/pickle.html#pickle.Pickler.reducer_override "Link to this definition")

Special reducer that can be defined in `Pickler` subclasses. This method has priority over any reducer in the [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table"). It should conform to the same interface as a [`__reduce__()`](https://docs.python.org/3/library/pickle.html#object.__reduce__ "object.__reduce__") method, and can optionally return [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented") to fallback on `dispatch_table`-registered reducers to pickle `obj`.
For a detailed example, see [Custom Reduction for Types, Functions, and Other Objects](https://docs.python.org/3/library/pickle.html#reducer-override).
Added in version 3.8.

fast[¶](https://docs.python.org/3/library/pickle.html#pickle.Pickler.fast "Link to this definition")

Deprecated. Enable fast mode if set to a true value. The fast mode disables the usage of memo, therefore speeding the pickling process by not generating superfluous PUT opcodes. It should not be used with self-referential objects, doing otherwise will cause `Pickler` to recurse infinitely.
Use [`pickletools.optimize()`](https://docs.python.org/3/library/pickletools.html#pickletools.optimize "pickletools.optimize") if you need more compact pickles.

clear_memo()[¶](https://docs.python.org/3/library/pickle.html#pickle.Pickler.clear_memo "Link to this definition")

Clears the pickler’s “memo”.
The memo is the data structure that remembers which objects the pickler has already seen, so that shared or recursive objects are pickled by reference and not by value. This method is useful when reusing picklers.

_class_ pickle.Unpickler(_file_ , _*_ , _fix_imports =True_, _encoding ='ASCII'_, _errors ='strict'_, _buffers =None_)[¶](https://docs.python.org/3/library/pickle.html#pickle.Unpickler "Link to this definition")

This takes a binary file for reading a pickle data stream.
The protocol version of the pickle is detected automatically, so no protocol argument is needed.
The argument _file_ must have three methods, a read() method that takes an integer argument, a readinto() method that takes a buffer argument and a readline() method that requires no arguments, as in the [`io.BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") interface. Thus _file_ can be an on-disk file opened for binary reading, an [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") object, or any other custom object that meets this interface.
The optional arguments _fix_imports_ , _encoding_ and _errors_ are used to control compatibility support for pickle stream generated by Python 2. If _fix_imports_ is true, pickle will try to map the old Python 2 names to the new names used in Python 3. The _encoding_ and _errors_ tell pickle how to decode 8-bit string instances pickled by Python 2; these default to ‘ASCII’ and ‘strict’, respectively. The _encoding_ can be ‘bytes’ to read these 8-bit string instances as bytes objects. Using `encoding='latin1'` is required for unpickling NumPy arrays and instances of [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime"), [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") and [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") pickled by Python 2.
If _buffers_ is `None` (the default), then all data necessary for deserialization must be contained in the pickle stream. This means that the _buffer_callback_ argument was `None` when a [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") was instantiated (or when [`dump()`](https://docs.python.org/3/library/pickle.html#pickle.dump "pickle.dump") or [`dumps()`](https://docs.python.org/3/library/pickle.html#pickle.dumps "pickle.dumps") was called).
If _buffers_ is not `None`, it should be an iterable of buffer-enabled objects that is consumed each time the pickle stream references an [out-of-band](https://docs.python.org/3/library/pickle.html#pickle-oob) buffer view. Such buffers have been given in order to the _buffer_callback_ of a Pickler object.
Changed in version 3.8: The _buffers_ argument was added.

load()[¶](https://docs.python.org/3/library/pickle.html#pickle.Unpickler.load "Link to this definition")

Read the pickled representation of an object from the open file object given in the constructor, and return the reconstituted object hierarchy specified therein. Bytes past the pickled representation of the object are ignored.

persistent_load(_pid_)[¶](https://docs.python.org/3/library/pickle.html#pickle.Unpickler.persistent_load "Link to this definition")

Raise an [`UnpicklingError`](https://docs.python.org/3/library/pickle.html#pickle.UnpicklingError "pickle.UnpicklingError") by default.
If defined, `persistent_load()` should return the object specified by the persistent ID _pid_. If an invalid persistent ID is encountered, an [`UnpicklingError`](https://docs.python.org/3/library/pickle.html#pickle.UnpicklingError "pickle.UnpicklingError") should be raised.
See [Persistence of External Objects](https://docs.python.org/3/library/pickle.html#pickle-persistent) for details and examples of uses.
Changed in version 3.13: Add the default implementation of this method in the C implementation of `Unpickler`.

find_class(_module_ , _name_)[¶](https://docs.python.org/3/library/pickle.html#pickle.Unpickler.find_class "Link to this definition")

Import _module_ if necessary and return the object called _name_ from it, where the _module_ and _name_ arguments are [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") objects. Note, unlike its name suggests, `find_class()` is also used for finding functions.
Subclasses may override this to gain control over what type of objects and how they can be loaded, potentially reducing security risks. Refer to [Restricting Globals](https://docs.python.org/3/library/pickle.html#pickle-restrict) for details.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `pickle.find_class` with arguments `module`, `name`.

_class_ pickle.PickleBuffer(_buffer_)[¶](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "Link to this definition")

A wrapper for a buffer representing picklable data. _buffer_ must be a [buffer-providing](https://docs.python.org/3/c-api/buffer.html#bufferobjects) object, such as a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) or a N-dimensional array.
`PickleBuffer` is itself a buffer provider, therefore it is possible to pass it to other APIs expecting a buffer-providing object, such as [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "memoryview").
`PickleBuffer` objects can only be serialized using pickle protocol 5 or higher. They are eligible for [out-of-band serialization](https://docs.python.org/3/library/pickle.html#pickle-oob).
Added in version 3.8.

raw()[¶](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer.raw "Link to this definition")

Return a [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "memoryview") of the memory area underlying this buffer. The returned object is a one-dimensional, C-contiguous memoryview with format `B` (unsigned bytes). [`BufferError`](https://docs.python.org/3/library/exceptions.html#BufferError "BufferError") is raised if the buffer is neither C- nor Fortran-contiguous.

release()[¶](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer.release "Link to this definition")

Release the underlying buffer exposed by the PickleBuffer object.
## What can be pickled and unpickled?[¶](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled "Link to this heading")
The following types can be pickled:
  * built-in constants (`None`, `True`, `False`, `Ellipsis`, and [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented"));
  * integers, floating-point numbers, complex numbers;
  * strings, bytes, bytearrays;
  * tuples, lists, sets, and dictionaries containing only picklable objects;
  * functions (built-in and user-defined) accessible from the top level of a module (using [`def`](https://docs.python.org/3/reference/compound_stmts.html#def), not [`lambda`](https://docs.python.org/3/reference/expressions.html#lambda));
  * classes accessible from the top level of a module;
  * instances of such classes for which the result of calling [`__getstate__()`](https://docs.python.org/3/library/pickle.html#object.__getstate__ "object.__getstate__") is picklable (see section [Pickling Class Instances](https://docs.python.org/3/library/pickle.html#pickle-inst) for details).


Attempts to pickle unpicklable objects will raise the [`PicklingError`](https://docs.python.org/3/library/pickle.html#pickle.PicklingError "pickle.PicklingError") exception; when this happens, an unspecified number of bytes may have already been written to the underlying file. Trying to pickle a highly recursive data structure may exceed the maximum recursion depth, a [`RecursionError`](https://docs.python.org/3/library/exceptions.html#RecursionError "RecursionError") will be raised in this case. You can carefully raise this limit with [`sys.setrecursionlimit()`](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit "sys.setrecursionlimit").
Note that functions (built-in and user-defined) are pickled by fully [qualified name](https://docs.python.org/3/glossary.html#term-qualified-name), not by value. [[2]](https://docs.python.org/3/library/pickle.html#id8) This means that only the function name is pickled, along with the name of the containing module and classes. Neither the function’s code, nor any of its function attributes are pickled. Thus the defining module must be importable in the unpickling environment, and the module must contain the named object, otherwise an exception will be raised. [[3]](https://docs.python.org/3/library/pickle.html#id9)
Similarly, classes are pickled by fully qualified name, so the same restrictions in the unpickling environment apply. Note that none of the class’s code or data is pickled, so in the following example the class attribute `attr` is not restored in the unpickling environment:
Copy```
class Foo:
    attr = 'A class attribute'

picklestring = pickle.dumps(Foo)

```

These restrictions are why picklable functions and classes must be defined at the top level of a module.
Similarly, when class instances are pickled, their class’s code and data are not pickled along with them. Only the instance data are pickled. This is done on purpose, so you can fix bugs in a class or add methods to the class and still load objects that were created with an earlier version of the class. If you plan to have long-lived objects that will see many versions of a class, it may be worthwhile to put a version number in the objects so that suitable conversions can be made by the class’s [`__setstate__()`](https://docs.python.org/3/library/pickle.html#object.__setstate__ "object.__setstate__") method.
## Pickling Class Instances[¶](https://docs.python.org/3/library/pickle.html#pickling-class-instances "Link to this heading")
In this section, we describe the general mechanisms available to you to define, customize, and control how class instances are pickled and unpickled.
In most cases, no additional code is needed to make instances picklable. By default, pickle will retrieve the class and the attributes of an instance via introspection. When a class instance is unpickled, its [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__") method is usually _not_ invoked. The default behaviour first creates an uninitialized instance and then restores the saved attributes. The following code shows an implementation of this behaviour:
Copy```
def save(obj):
    return (obj.__class__, obj.__dict__)

def restore(cls, attributes):
    obj = cls.__new__(cls)
    obj.__dict__.update(attributes)
    return obj

```

Classes can alter the default behaviour by providing one or several special methods:

object.__getnewargs_ex__()[¶](https://docs.python.org/3/library/pickle.html#object.__getnewargs_ex__ "Link to this definition")

In protocols 2 and newer, classes that implement the `__getnewargs_ex__()` method can dictate the values passed to the [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__") method upon unpickling. The method must return a pair `(args, kwargs)` where _args_ is a tuple of positional arguments and _kwargs_ a dictionary of named arguments for constructing the object. Those will be passed to the `__new__()` method upon unpickling.
You should implement this method if the [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__") method of your class requires keyword-only arguments. Otherwise, it is recommended for compatibility to implement [`__getnewargs__()`](https://docs.python.org/3/library/pickle.html#object.__getnewargs__ "object.__getnewargs__").
Changed in version 3.6: `__getnewargs_ex__()` is now used in protocols 2 and 3.

object.__getnewargs__()[¶](https://docs.python.org/3/library/pickle.html#object.__getnewargs__ "Link to this definition")

This method serves a similar purpose as [`__getnewargs_ex__()`](https://docs.python.org/3/library/pickle.html#object.__getnewargs_ex__ "object.__getnewargs_ex__"), but supports only positional arguments. It must return a tuple of arguments `args` which will be passed to the [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__") method upon unpickling.
`__getnewargs__()` will not be called if [`__getnewargs_ex__()`](https://docs.python.org/3/library/pickle.html#object.__getnewargs_ex__ "object.__getnewargs_ex__") is defined.
Changed in version 3.6: Before Python 3.6, `__getnewargs__()` was called instead of [`__getnewargs_ex__()`](https://docs.python.org/3/library/pickle.html#object.__getnewargs_ex__ "object.__getnewargs_ex__") in protocols 2 and 3.

object.__getstate__()[¶](https://docs.python.org/3/library/pickle.html#object.__getstate__ "Link to this definition")

Classes can further influence how their instances are pickled by overriding the method `__getstate__()`. It is called and the returned object is pickled as the contents for the instance, instead of a default state. There are several cases:
  * For a class that has no instance [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") and no [`__slots__`](https://docs.python.org/3/reference/datamodel.html#object.__slots__ "object.__slots__"), the default state is `None`.
  * For a class that has an instance [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") and no [`__slots__`](https://docs.python.org/3/reference/datamodel.html#object.__slots__ "object.__slots__"), the default state is `self.__dict__`.
  * For a class that has an instance [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") and [`__slots__`](https://docs.python.org/3/reference/datamodel.html#object.__slots__ "object.__slots__"), the default state is a tuple consisting of two dictionaries: `self.__dict__`, and a dictionary mapping slot names to slot values. Only slots that have a value are included in the latter.
  * For a class that has [`__slots__`](https://docs.python.org/3/reference/datamodel.html#object.__slots__ "object.__slots__") and no instance [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__"), the default state is a tuple whose first item is `None` and whose second item is a dictionary mapping slot names to slot values described in the previous bullet.


Changed in version 3.11: Added the default implementation of the `__getstate__()` method in the [`object`](https://docs.python.org/3/library/functions.html#object "object") class.

object.__setstate__(_state_)[¶](https://docs.python.org/3/library/pickle.html#object.__setstate__ "Link to this definition")

Upon unpickling, if the class defines `__setstate__()`, it is called with the unpickled state. In that case, there is no requirement for the state object to be a dictionary. Otherwise, the pickled state must be a dictionary and its items are assigned to the new instance’s dictionary.
Note
If [`__reduce__()`](https://docs.python.org/3/library/pickle.html#object.__reduce__ "object.__reduce__") returns a state with value `None` at pickling, the `__setstate__()` method will not be called upon unpickling.
Refer to the section [Handling Stateful Objects](https://docs.python.org/3/library/pickle.html#pickle-state) for more information about how to use the methods [`__getstate__()`](https://docs.python.org/3/library/pickle.html#object.__getstate__ "object.__getstate__") and [`__setstate__()`](https://docs.python.org/3/library/pickle.html#object.__setstate__ "object.__setstate__").
Note
At unpickling time, some methods like [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__"), [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__"), or [`__setattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__setattr__ "object.__setattr__") may be called upon the instance. In case those methods rely on some internal invariant being true, the type should implement [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__") to establish such an invariant, as [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__") is not called when unpickling an instance.
As we shall see, pickle does not use directly the methods described above. In fact, these methods are part of the copy protocol which implements the [`__reduce__()`](https://docs.python.org/3/library/pickle.html#object.__reduce__ "object.__reduce__") special method. The copy protocol provides a unified interface for retrieving the data necessary for pickling and copying objects. [[4]](https://docs.python.org/3/library/pickle.html#id10)
Although powerful, implementing [`__reduce__()`](https://docs.python.org/3/library/pickle.html#object.__reduce__ "object.__reduce__") directly in your classes is error prone. For this reason, class designers should use the high-level interface (i.e., [`__getnewargs_ex__()`](https://docs.python.org/3/library/pickle.html#object.__getnewargs_ex__ "object.__getnewargs_ex__"), [`__getstate__()`](https://docs.python.org/3/library/pickle.html#object.__getstate__ "object.__getstate__") and [`__setstate__()`](https://docs.python.org/3/library/pickle.html#object.__setstate__ "object.__setstate__")) whenever possible. We will show, however, cases where using `__reduce__()` is the only option or leads to more efficient pickling or both.

object.__reduce__()[¶](https://docs.python.org/3/library/pickle.html#object.__reduce__ "Link to this definition")

The interface is currently defined as follows. The `__reduce__()` method takes no argument and shall return either a string or preferably a tuple (the returned object is often referred to as the “reduce value”).
If a string is returned, the string should be interpreted as the name of a global variable. It should be the object’s local name relative to its module; the pickle module searches the module namespace to determine the object’s module. This behaviour is typically useful for singletons.
When a tuple is returned, it must be between two and six items long. Optional items can either be omitted, or `None` can be provided as their value. The semantics of each item are in order:
  * A callable object that will be called to create the initial version of the object.
  * A tuple of arguments for the callable object. An empty tuple must be given if the callable does not accept any argument.
  * Optionally, the object’s state, which will be passed to the object’s [`__setstate__()`](https://docs.python.org/3/library/pickle.html#object.__setstate__ "object.__setstate__") method as previously described. If the object has no such method then, the value must be a dictionary and it will be added to the object’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") attribute.
  * Optionally, an iterator (and not a sequence) yielding successive items. These items will be appended to the object either using `obj.append(item)` or, in batch, using `obj.extend(list_of_items)`. This is primarily used for list subclasses, but may be used by other classes as long as they have [`append()`](https://docs.python.org/3/library/stdtypes.html#sequence.append "sequence.append") and [`extend()`](https://docs.python.org/3/library/stdtypes.html#sequence.extend "sequence.extend") methods with the appropriate signature. (Whether `append()` or `extend()` is used depends on which pickle protocol version is used as well as the number of items to append, so both must be supported.)
  * Optionally, an iterator (not a sequence) yielding successive key-value pairs. These items will be stored to the object using `obj[key] = value`. This is primarily used for dictionary subclasses, but may be used by other classes as long as they implement [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__").
  * Optionally, a callable with a `(obj, state)` signature. This callable allows the user to programmatically control the state-updating behavior of a specific object, instead of using `obj`’s static [`__setstate__()`](https://docs.python.org/3/library/pickle.html#object.__setstate__ "object.__setstate__") method. If not `None`, this callable will have priority over `obj`’s `__setstate__()`.
Added in version 3.8: The optional sixth tuple item, `(obj, state)`, was added.



object.__reduce_ex__(_protocol_)[¶](https://docs.python.org/3/library/pickle.html#object.__reduce_ex__ "Link to this definition")

Alternatively, a `__reduce_ex__()` method may be defined. The only difference is this method should take a single integer argument, the protocol version. When defined, pickle will prefer it over the [`__reduce__()`](https://docs.python.org/3/library/pickle.html#object.__reduce__ "object.__reduce__") method. In addition, `__reduce__()` automatically becomes a synonym for the extended version. The main use for this method is to provide backwards-compatible reduce values for older Python releases.
### Persistence of External Objects[¶](https://docs.python.org/3/library/pickle.html#persistence-of-external-objects "Link to this heading")
For the benefit of object persistence, the `pickle` module supports the notion of a reference to an object outside the pickled data stream. Such objects are referenced by a persistent ID, which should be either a string of alphanumeric characters (for protocol 0) [[5]](https://docs.python.org/3/library/pickle.html#id11) or just an arbitrary object (for any newer protocol).
The resolution of such persistent IDs is not defined by the `pickle` module; it will delegate this resolution to the user-defined methods on the pickler and unpickler, [`persistent_id()`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.persistent_id "pickle.Pickler.persistent_id") and [`persistent_load()`](https://docs.python.org/3/library/pickle.html#pickle.Unpickler.persistent_load "pickle.Unpickler.persistent_load") respectively.
To pickle objects that have an external persistent ID, the pickler must have a custom [`persistent_id()`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.persistent_id "pickle.Pickler.persistent_id") method that takes an object as an argument and returns either `None` or the persistent ID for that object. When `None` is returned, the pickler simply pickles the object as normal. When a persistent ID string is returned, the pickler will pickle that object, along with a marker so that the unpickler will recognize it as a persistent ID.
To unpickle external objects, the unpickler must have a custom [`persistent_load()`](https://docs.python.org/3/library/pickle.html#pickle.Unpickler.persistent_load "pickle.Unpickler.persistent_load") method that takes a persistent ID object and returns the referenced object.
Here is a comprehensive example presenting how persistent ID can be used to pickle external objects by reference.
Copy```
