# Simple class representing a record in our database.
MemoRecord = namedtuple("MemoRecord", "key, task")

class DBPickler(pickle.Pickler):

    def persistent_id(self, obj):
        # Instead of pickling MemoRecord as a regular class instance, we emit a
        # persistent ID.
        if isinstance(obj, MemoRecord):
            # Here, our persistent ID is simply a tuple, containing a tag and a
            # key, which refers to a specific record in the database.
            return ("MemoRecord", obj.key)
        else:
            # If obj does not have a persistent ID, return None. This means obj
            # needs to be pickled as usual.
            return None


class DBUnpickler(pickle.Unpickler):

    def __init__(self, file, connection):
        super().__init__(file)
        self.connection = connection

    def persistent_load(self, pid):
        # This method is invoked whenever a persistent ID is encountered.
        # Here, pid is the tuple returned by DBPickler.
        cursor = self.connection.cursor()
        type_tag, key_id = pid
        if type_tag == "MemoRecord":
            # Fetch the referenced record from the database and return it.
            cursor.execute("SELECT * FROM memos WHERE key=?", (str(key_id),))
            key, task = cursor.fetchone()
            return MemoRecord(key, task)
        else:
            # Always raises an error if you cannot return the correct object.
            # Otherwise, the unpickler will think None is the object referenced
            # by the persistent ID.
            raise pickle.UnpicklingError("unsupported persistent object")


def main():
    import io
    import pprint

    # Initialize and populate our database.
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE memos(key INTEGER PRIMARY KEY, task TEXT)")
    tasks = (
        'give food to fish',
        'prepare group meeting',
        'fight with a zebra',
        )
    for task in tasks:
        cursor.execute("INSERT INTO memos VALUES(NULL, ?)", (task,))

    # Fetch the records to be pickled.
    cursor.execute("SELECT * FROM memos")
    memos = [MemoRecord(key, task) for key, task in cursor]
    # Save the records using our custom DBPickler.
    file = io.BytesIO()
    DBPickler(file).dump(memos)

    print("Pickled records:")
    pprint.pprint(memos)

    # Update a record, just for good measure.
    cursor.execute("UPDATE memos SET task='learn italian' WHERE key=1")

    # Load the records from the pickle data stream.
    file.seek(0)
    memos = DBUnpickler(file, conn).load()

    print("Unpickled records:")
    pprint.pprint(memos)


if __name__ == '__main__':
    main()

```

### Dispatch Tables[¶](https://docs.python.org/3/library/pickle.html#dispatch-tables "Link to this heading")
If one wants to customize pickling of some classes without disturbing any other code which depends on pickling, then one can create a pickler with a private dispatch table.
The global dispatch table managed by the [`copyreg`](https://docs.python.org/3/library/copyreg.html#module-copyreg "copyreg: Register pickle support functions.") module is available as `copyreg.dispatch_table`. Therefore, one may choose to use a modified copy of `copyreg.dispatch_table` as a private dispatch table.
For example
Copy```
f = io.BytesIO()
p = pickle.Pickler(f)
p.dispatch_table = copyreg.dispatch_table.copy()
p.dispatch_table[SomeClass] = reduce_SomeClass

```

creates an instance of [`pickle.Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") with a private dispatch table which handles the `SomeClass` class specially. Alternatively, the code
Copy```
class MyPickler(pickle.Pickler):
    dispatch_table = copyreg.dispatch_table.copy()
    dispatch_table[SomeClass] = reduce_SomeClass
f = io.BytesIO()
p = MyPickler(f)

```

does the same but all instances of `MyPickler` will by default share the private dispatch table. On the other hand, the code
Copy```
copyreg.pickle(SomeClass, reduce_SomeClass)
f = io.BytesIO()
p = pickle.Pickler(f)

```

modifies the global dispatch table shared by all users of the [`copyreg`](https://docs.python.org/3/library/copyreg.html#module-copyreg "copyreg: Register pickle support functions.") module.
### Handling Stateful Objects[¶](https://docs.python.org/3/library/pickle.html#handling-stateful-objects "Link to this heading")
Here’s an example that shows how to modify pickling behavior for a class. The `TextReader` class below opens a text file, and returns the line number and line contents each time its `readline()` method is called. If a `TextReader` instance is pickled, all attributes _except_ the file object member are saved. When the instance is unpickled, the file is reopened, and reading resumes from the last location. The `__setstate__()` and `__getstate__()` methods are used to implement this behavior.
Copy```
class TextReader:
    """Print and number lines in a text file."""

    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename)
        self.lineno = 0

    def readline(self):
        self.lineno += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        return "%i: %s" % (self.lineno, line)

    def __getstate__(self):
        # Copy the object's state from self.__dict__ which contains
        # all our instance attributes. Always use the dict.copy()
        # method to avoid modifying the original state.
        state = self.__dict__.copy()
        # Remove the unpicklable entries.
        del state['file']
        return state

    def __setstate__(self, state):
        # Restore instance attributes (i.e., filename and lineno).
        self.__dict__.update(state)
        # Restore the previously opened file's state. To do so, we need to
        # reopen it and read from it until the line count is restored.
        file = open(self.filename)
        for _ in range(self.lineno):
            file.readline()
        # Finally, save the file.
        self.file = file

```

A sample usage might be something like this:
Copy```
>>> reader = TextReader("hello.txt")
>>> reader.readline()
'1: Hello world!'
>>> reader.readline()
'2: I am line number two.'
>>> new_reader = pickle.loads(pickle.dumps(reader))
>>> new_reader.readline()
'3: Goodbye!'

```

## Custom Reduction for Types, Functions, and Other Objects[¶](https://docs.python.org/3/library/pickle.html#custom-reduction-for-types-functions-and-other-objects "Link to this heading")
Added in version 3.8.
Sometimes, [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table") may not be flexible enough. In particular we may want to customize pickling based on another criterion than the object’s type, or we may want to customize the pickling of functions and classes.
For those cases, it is possible to subclass from the [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") class and implement a [`reducer_override()`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.reducer_override "pickle.Pickler.reducer_override") method. This method can return an arbitrary reduction tuple (see [`__reduce__()`](https://docs.python.org/3/library/pickle.html#object.__reduce__ "object.__reduce__")). It can alternatively return [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented") to fallback to the traditional behavior.
If both the [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table") and [`reducer_override()`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.reducer_override "pickle.Pickler.reducer_override") are defined, then `reducer_override()` method takes priority.
Note
For performance reasons, [`reducer_override()`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.reducer_override "pickle.Pickler.reducer_override") may not be called for the following objects: `None`, `True`, `False`, and exact instances of [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") and [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple").
Here is a simple example where we allow pickling and reconstructing a given class:
Copy```
import io
import pickle

class MyClass:
    my_attribute = 1

class MyPickler(pickle.Pickler):
    def reducer_override(self, obj):
        """Custom reducer for MyClass."""
        if getattr(obj, "__name__", None) == "MyClass":
            return type, (obj.__name__, obj.__bases__,
                          {'my_attribute': obj.my_attribute})
        else:
            # For any other object, fallback to usual reduction
            return NotImplemented

f = io.BytesIO()
p = MyPickler(f)
p.dump(MyClass)

del MyClass

unpickled_class = pickle.loads(f.getvalue())

assert isinstance(unpickled_class, type)
assert unpickled_class.__name__ == "MyClass"
assert unpickled_class.my_attribute == 1

```

## Out-of-band Buffers[¶](https://docs.python.org/3/library/pickle.html#out-of-band-buffers "Link to this heading")
Added in version 3.8.
In some contexts, the `pickle` module is used to transfer massive amounts of data. Therefore, it can be important to minimize the number of memory copies, to preserve performance and resource consumption. However, normal operation of the `pickle` module, as it transforms a graph-like structure of objects into a sequential stream of bytes, intrinsically involves copying data to and from the pickle stream.
This constraint can be eschewed if both the _provider_ (the implementation of the object types to be transferred) and the _consumer_ (the implementation of the communications system) support the out-of-band transfer facilities provided by pickle protocol 5 and higher.
### Provider API[¶](https://docs.python.org/3/library/pickle.html#provider-api "Link to this heading")
The large data objects to be pickled must implement a [`__reduce_ex__()`](https://docs.python.org/3/library/pickle.html#object.__reduce_ex__ "object.__reduce_ex__") method specialized for protocol 5 and higher, which returns a [`PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer") instance (instead of e.g. a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object) for any large data.
A [`PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer") object _signals_ that the underlying buffer is eligible for out-of-band data transfer. Those objects remain compatible with normal usage of the `pickle` module. However, consumers can also opt-in to tell `pickle` that they will handle those buffers by themselves.
### Consumer API[¶](https://docs.python.org/3/library/pickle.html#consumer-api "Link to this heading")
A communications system can enable custom handling of the [`PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer") objects generated when serializing an object graph.
On the sending side, it needs to pass a _buffer_callback_ argument to [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") (or to the [`dump()`](https://docs.python.org/3/library/pickle.html#pickle.dump "pickle.dump") or [`dumps()`](https://docs.python.org/3/library/pickle.html#pickle.dumps "pickle.dumps") function), which will be called with each [`PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer") generated while pickling the object graph. Buffers accumulated by the _buffer_callback_ will not see their data copied into the pickle stream, only a cheap marker will be inserted.
On the receiving side, it needs to pass a _buffers_ argument to [`Unpickler`](https://docs.python.org/3/library/pickle.html#pickle.Unpickler "pickle.Unpickler") (or to the [`load()`](https://docs.python.org/3/library/pickle.html#pickle.load "pickle.load") or [`loads()`](https://docs.python.org/3/library/pickle.html#pickle.loads "pickle.loads") function), which is an iterable of the buffers which were passed to _buffer_callback_. That iterable should produce buffers in the same order as they were passed to _buffer_callback_. Those buffers will provide the data expected by the reconstructors of the objects whose pickling produced the original [`PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer") objects.
Between the sending side and the receiving side, the communications system is free to implement its own transfer mechanism for out-of-band buffers. Potential optimizations include the use of shared memory or datatype-dependent compression.
### Example[¶](https://docs.python.org/3/library/pickle.html#example "Link to this heading")
Here is a trivial example where we implement a [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") subclass able to participate in out-of-band buffer pickling:
Copy```
class ZeroCopyByteArray(bytearray):

    def __reduce_ex__(self, protocol):
        if protocol >= 5:
            return type(self)._reconstruct, (PickleBuffer(self),), None
        else:
            # PickleBuffer is forbidden with pickle protocols <= 4.
            return type(self)._reconstruct, (bytearray(self),)

    @classmethod
    def _reconstruct(cls, obj):
        with memoryview(obj) as m:
            # Get a handle over the original buffer object
            obj = m.obj
            if type(obj) is cls:
                # Original buffer object is a ZeroCopyByteArray, return it
                # as-is.
                return obj
            else:
                return cls(obj)

```

The reconstructor (the `_reconstruct` class method) returns the buffer’s providing object if it has the right type. This is an easy way to simulate zero-copy behaviour on this toy example.
On the consumer side, we can pickle those objects the usual way, which when unserialized will give us a copy of the original object:
Copy```
b = ZeroCopyByteArray(b"abc")
data = pickle.dumps(b, protocol=5)
new_b = pickle.loads(data)
print(b == new_b)  # True
print(b is new_b)  # False: a copy was made

```

But if we pass a _buffer_callback_ and then give back the accumulated buffers when unserializing, we are able to get back the original object:
Copy```
b = ZeroCopyByteArray(b"abc")
buffers = []
data = pickle.dumps(b, protocol=5, buffer_callback=buffers.append)
new_b = pickle.loads(data, buffers=buffers)
print(b == new_b)  # True
print(b is new_b)  # True: no copy was made

```

This example is limited by the fact that [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") allocates its own memory: you cannot create a `bytearray` instance that is backed by another object’s memory. However, third-party datatypes such as NumPy arrays do not have this limitation, and allow use of zero-copy pickling (or making as few copies as possible) when transferring between distinct processes or systems.
See also
[**PEP 574**](https://peps.python.org/pep-0574/) – Pickle protocol 5 with out-of-band data
## Restricting Globals[¶](https://docs.python.org/3/library/pickle.html#restricting-globals "Link to this heading")
By default, unpickling will import any class or function that it finds in the pickle data. For many applications, this behaviour is unacceptable as it permits the unpickler to import and invoke arbitrary code. Just consider what this hand-crafted pickle data stream does when loaded:
Copy```
>>> import pickle
>>> pickle.loads(b"cos\nsystem\n(S'echo hello world'\ntR.")
hello world
0

```

In this example, the unpickler imports the [`os.system()`](https://docs.python.org/3/library/os.html#os.system "os.system") function and then apply the string argument “echo hello world”. Although this example is inoffensive, it is not difficult to imagine one that could damage your system.
For this reason, you may want to control what gets unpickled by customizing [`Unpickler.find_class()`](https://docs.python.org/3/library/pickle.html#pickle.Unpickler.find_class "pickle.Unpickler.find_class"). Unlike its name suggests, `Unpickler.find_class()` is called whenever a global (i.e., a class or a function) is requested. Thus it is possible to either completely forbid globals or restrict them to a safe subset.
Here is an example of an unpickler allowing only few safe classes from the [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") module to be loaded:
Copy```
import builtins
import io
import pickle

safe_builtins = {
    'range',
    'complex',
    'set',
    'frozenset',
    'slice',
}

class RestrictedUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        # Only allow safe classes from builtins.
        if module == "builtins" and name in safe_builtins:
            return getattr(builtins, name)
        # Forbid everything else.
        raise pickle.UnpicklingError("global '%s.%s' is forbidden" %
                                     (module, name))

def restricted_loads(s):
    """Helper function analogous to pickle.loads()."""
    return RestrictedUnpickler(io.BytesIO(s)).load()

```

A sample usage of our unpickler working as intended:
Copy```
>>> restricted_loads(pickle.dumps([1, 2, range(15)]))
[1, 2, range(0, 15)]
>>> restricted_loads(b"cos\nsystem\n(S'echo hello world'\ntR.")
Traceback (most recent call last):
  ...
pickle.UnpicklingError: global 'os.system' is forbidden
>>> restricted_loads(b'cbuiltins\neval\n'
...                  b'(S\'getattr(__import__("os"), "system")'
...                  b'("echo hello world")\'\ntR.')
Traceback (most recent call last):
  ...
pickle.UnpicklingError: global 'builtins.eval' is forbidden

```

As our examples shows, you have to be careful with what you allow to be unpickled. Therefore if security is a concern, you may want to consider alternatives such as the marshalling API in [`xmlrpc.client`](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client "xmlrpc.client: XML-RPC client access.") or third-party solutions.
## Performance[¶](https://docs.python.org/3/library/pickle.html#performance "Link to this heading")
Recent versions of the pickle protocol (from protocol 2 and upwards) feature efficient binary encodings for several common features and built-in types. Also, the `pickle` module has a transparent optimizer written in C.
## Examples[¶](https://docs.python.org/3/library/pickle.html#examples "Link to this heading")
For the simplest code, use the [`dump()`](https://docs.python.org/3/library/pickle.html#pickle.dump "pickle.dump") and [`load()`](https://docs.python.org/3/library/pickle.html#pickle.load "pickle.load") functions.
Copy```
import pickle

# An arbitrary collection of objects supported by pickle.
data = {
    'a': [1, 2.0, 3+4j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('data.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

```

The following example reads the resulting pickled data.
Copy```
import pickle

with open('data.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)

```

## Command-line interface[¶](https://docs.python.org/3/library/pickle.html#command-line-interface "Link to this heading")
The `pickle` module can be invoked as a script from the command line, it will display contents of the pickle files. However, when the pickle file that you want to examine comes from an untrusted source, `-m pickletools` is a safer option because it does not execute pickle bytecode, see [pickletools CLI usage](https://docs.python.org/3/library/pickletools.html#pickletools-cli).
Copy```
python -m pickle pickle_file [pickle_file ...]

```

The following option is accepted:

pickle_file[¶](https://docs.python.org/3/library/pickle.html#cmdoption-pickle-arg-pickle_file "Link to this definition")

A pickle file to read, or `-` to indicate reading from standard input.
See also

Module [`copyreg`](https://docs.python.org/3/library/copyreg.html#module-copyreg "copyreg: Register pickle support functions.")

Pickle interface constructor registration for extension types.

Module [`pickletools`](https://docs.python.org/3/library/pickletools.html#module-pickletools "pickletools: Contains extensive comments about the pickle protocols and pickle-machine opcodes, as well as some useful functions.")

Tools for working with and analyzing pickled data.

Module [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.")

Indexed databases of objects; uses `pickle`.

Module [`copy`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.")

Shallow and deep object copying.

Module [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back \(with different constraints\).")

High-performance serialization of built-in types.
Footnotes
[[1](https://docs.python.org/3/library/pickle.html#id1)]
Don’t confuse this with the [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back \(with different constraints\).") module
[[2](https://docs.python.org/3/library/pickle.html#id3)]
This is why [`lambda`](https://docs.python.org/3/reference/expressions.html#lambda) functions cannot be pickled: all `lambda` functions share the same name: `<lambda>`.
[[3](https://docs.python.org/3/library/pickle.html#id4)]
The exception raised will likely be an [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") or an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") but it could be something else.
[[4](https://docs.python.org/3/library/pickle.html#id5)]
The [`copy`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.") module uses this protocol for shallow and deep copying operations.
[[5](https://docs.python.org/3/library/pickle.html#id6)]
The limitation on alphanumeric characters is due to the fact that persistent IDs in protocol 0 are delimited by the newline character. Therefore if any kind of newline characters occurs in persistent IDs, the resulting pickled data will become unreadable.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html)
    * [Relationship to other Python modules](https://docs.python.org/3/library/pickle.html#relationship-to-other-python-modules)
      * [Comparison with `marshal`](https://docs.python.org/3/library/pickle.html#comparison-with-marshal)
      * [Comparison with `json`](https://docs.python.org/3/library/pickle.html#comparison-with-json)
    * [Data stream format](https://docs.python.org/3/library/pickle.html#data-stream-format)
    * [Module Interface](https://docs.python.org/3/library/pickle.html#module-interface)
    * [What can be pickled and unpickled?](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled)
    * [Pickling Class Instances](https://docs.python.org/3/library/pickle.html#pickling-class-instances)
      * [Persistence of External Objects](https://docs.python.org/3/library/pickle.html#persistence-of-external-objects)
      * [Dispatch Tables](https://docs.python.org/3/library/pickle.html#dispatch-tables)
      * [Handling Stateful Objects](https://docs.python.org/3/library/pickle.html#handling-stateful-objects)
    * [Custom Reduction for Types, Functions, and Other Objects](https://docs.python.org/3/library/pickle.html#custom-reduction-for-types-functions-and-other-objects)
    * [Out-of-band Buffers](https://docs.python.org/3/library/pickle.html#out-of-band-buffers)
      * [Provider API](https://docs.python.org/3/library/pickle.html#provider-api)
      * [Consumer API](https://docs.python.org/3/library/pickle.html#consumer-api)
      * [Example](https://docs.python.org/3/library/pickle.html#example)
    * [Restricting Globals](https://docs.python.org/3/library/pickle.html#restricting-globals)
    * [Performance](https://docs.python.org/3/library/pickle.html#performance)
    * [Examples](https://docs.python.org/3/library/pickle.html#examples)
    * [Command-line interface](https://docs.python.org/3/library/pickle.html#command-line-interface)


#### Previous topic
[Data Persistence](https://docs.python.org/3/library/persistence.html "previous chapter")
#### Next topic
[`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pickle+%E2%80%94+Python+object+serialization&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpickle.html&pagesource=library%2Fpickle.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/copyreg.html "copyreg — Register pickle support functions") |
  * [previous](https://docs.python.org/3/library/persistence.html "Data Persistence") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Data Persistence](https://docs.python.org/3/library/persistence.html) »
  * [`pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html)
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
  *[/]: Positional-only parameter separator (PEP 570)
