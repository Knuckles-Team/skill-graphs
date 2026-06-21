  * Binary files are buffered in fixed-size chunks; the size of the buffer is `max(min(blocksize, 8 MiB), DEFAULT_BUFFER_SIZE)` when the device block size is available. On most systems, the buffer will typically be 128 kilobytes long.
  * “Interactive” text files (files for which [`isatty()`](https://docs.python.org/3/library/io.html#io.IOBase.isatty "io.IOBase.isatty") returns `True`) use line buffering. Other text files use the policy described above for binary files.


_encoding_ is the name of the encoding used to decode or encode the file. This should only be used in text mode. The default encoding is platform dependent (whatever [`locale.getencoding()`](https://docs.python.org/3/library/locale.html#locale.getencoding "locale.getencoding") returns), but any [text encoding](https://docs.python.org/3/glossary.html#term-text-encoding) supported by Python can be used. See the [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.") module for the list of supported encodings.
_errors_ is an optional string that specifies how encoding and decoding errors are to be handled—this cannot be used in binary mode. A variety of standard error handlers are available (listed under [Error Handlers](https://docs.python.org/3/library/codecs.html#error-handlers)), though any error handling name that has been registered with [`codecs.register_error()`](https://docs.python.org/3/library/codecs.html#codecs.register_error "codecs.register_error") is also valid. The standard names include:
  * `'strict'` to raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") exception if there is an encoding error. The default value of `None` has the same effect.
  * `'ignore'` ignores errors. Note that ignoring encoding errors can lead to data loss.
  * `'replace'` causes a replacement marker (such as `'?'`) to be inserted where there is malformed data.
  * `'surrogateescape'` will represent any incorrect bytes as low surrogate code units ranging from U+DC80 to U+DCFF. These surrogate code units will then be turned back into the same bytes when the `surrogateescape` error handler is used when writing data. This is useful for processing files in an unknown encoding.
  * `'xmlcharrefreplace'` is only supported when writing to a file. Characters not supported by the encoding are replaced with the appropriate XML character reference `&#_nnn_;`.
  * `'backslashreplace'` replaces malformed data by Python’s backslashed escape sequences.
  * `'namereplace'` (also only supported when writing) replaces unsupported characters with `\N{...}` escape sequences.


_newline_ determines how to parse newline characters from the stream. It can be `None`, `''`, `'\n'`, `'\r'`, and `'\r\n'`. It works as follows:
  * When reading input from the stream, if _newline_ is `None`, universal newlines mode is enabled. Lines in the input can end in `'\n'`, `'\r'`, or `'\r\n'`, and these are translated into `'\n'` before being returned to the caller. If it is `''`, universal newlines mode is enabled, but line endings are returned to the caller untranslated. If it has any of the other legal values, input lines are only terminated by the given string, and the line ending is returned to the caller untranslated.
  * When writing output to the stream, if _newline_ is `None`, any `'\n'` characters written are translated to the system default line separator, [`os.linesep`](https://docs.python.org/3/library/os.html#os.linesep "os.linesep"). If _newline_ is `''` or `'\n'`, no translation takes place. If _newline_ is any of the other legal values, any `'\n'` characters written are translated to the given string.


If _closefd_ is `False` and a file descriptor rather than a filename was given, the underlying file descriptor will be kept open when the file is closed. If a filename is given _closefd_ must be `True` (the default); otherwise, an error will be raised.
A custom opener can be used by passing a callable as _opener_. The underlying file descriptor for the file object is then obtained by calling _opener_ with (_file_ , _flags_). _opener_ must return an open file descriptor (passing [`os.open`](https://docs.python.org/3/library/os.html#os.open "os.open") as _opener_ results in functionality similar to passing `None`).
The newly created file is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
The following example uses the [dir_fd](https://docs.python.org/3/library/os.html#dir-fd) parameter of the [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open") function to open a file relative to a given directory:
Copy```
>>> import os
>>> dir_fd = os.open('somedir', os.O_RDONLY)
>>> def opener(path, flags):
...     return os.open(path, flags, dir_fd=dir_fd)
...
>>> with open('spamspam.txt', 'w', opener=opener) as f:
...     print('This will be written to somedir/spamspam.txt', file=f)
...
>>> os.close(dir_fd)  # don't leak a file descriptor

```

The type of [file object](https://docs.python.org/3/glossary.html#term-file-object) returned by the `open()` function depends on the mode. When `open()` is used to open a file in a text mode (`'w'`, `'r'`, `'wt'`, `'rt'`, etc.), it returns a subclass of [`io.TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") (specifically [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")). When used to open a file in a binary mode with buffering, the returned class is a subclass of [`io.BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase"). The exact class varies: in read binary mode, it returns an [`io.BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader"); in write binary and append binary modes, it returns an [`io.BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter"), and in read/write mode, it returns an [`io.BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom"). When buffering is disabled, the raw stream, a subclass of [`io.RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase"), [`io.FileIO`](https://docs.python.org/3/library/io.html#io.FileIO "io.FileIO"), is returned.
See also the file handling modules, such as [`fileinput`](https://docs.python.org/3/library/fileinput.html#module-fileinput "fileinput: Loop over standard input or a list of files."), [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.") (where `open()` is declared), [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces."), [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames."), [`tempfile`](https://docs.python.org/3/library/tempfile.html#module-tempfile "tempfile: Generate temporary files and directories."), and [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.").
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `open` with arguments `path`, `mode`, `flags`.
The `mode` and `flags` arguments may have been modified or inferred from the original call.
Changed in version 3.3:
  * The _opener_ parameter was added.
  * The `'x'` mode was added.
  * [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") used to be raised, it is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
  * [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") is now raised if the file opened in exclusive creation mode (`'x'`) already exists.


Changed in version 3.4:
  * The file is now non-inheritable.


Changed in version 3.5:
  * If the system call is interrupted and the signal handler does not raise an exception, the function now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).
  * The `'namereplace'` error handler was added.


Changed in version 3.6:
  * Support added to accept objects implementing [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike").
  * On Windows, opening a console buffer may return a subclass of [`io.RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") other than [`io.FileIO`](https://docs.python.org/3/library/io.html#io.FileIO "io.FileIO").


Changed in version 3.11: The `'U'` mode has been removed.

ord(_character_ , _/_)[¶](https://docs.python.org/3/library/functions.html#ord "Link to this definition")

Return the ordinal value of a character.
If the argument is a one-character string, return the Unicode code point of that character. For example, `ord('a')` returns the integer `97` and `ord('€')` (Euro sign) returns `8364`. This is the inverse of [`chr()`](https://docs.python.org/3/library/functions.html#chr "chr").
If the argument is a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") object of length 1, return its single byte value. For example, `ord(b'a')` returns the integer `97`.

pow(_base_ , _exp_ , _mod =None_)[¶](https://docs.python.org/3/library/functions.html#pow "Link to this definition")

Return _base_ to the power _exp_ ; if _mod_ is present, return _base_ to the power _exp_ , modulo _mod_ (computed more efficiently than `pow(base, exp) % mod`). The two-argument form `pow(base, exp)` is equivalent to using the power operator: `base**exp`.
When arguments are builtin numeric types with mixed operand types, the coercion rules for binary arithmetic operators apply. For [`int`](https://docs.python.org/3/library/functions.html#int "int") operands, the result has the same type as the operands (after coercion) unless the second argument is negative; in that case, all arguments are converted to float and a float result is delivered. For example, `pow(10, 2)` returns `100`, but `pow(10, -2)` returns `0.01`. For a negative base of type `int` or [`float`](https://docs.python.org/3/library/functions.html#float "float") and a non-integral exponent, a complex result is delivered. For example, `pow(-9, 0.5)` returns a value close to `3j`. Whereas, for a negative base of type `int` or `float` with an integral exponent, a float result is delivered. For example, `pow(-9, 2.0)` returns `81.0`.
For [`int`](https://docs.python.org/3/library/functions.html#int "int") operands _base_ and _exp_ , if _mod_ is present, _mod_ must also be of integer type and _mod_ must be nonzero. If _mod_ is present and _exp_ is negative, _base_ must be relatively prime to _mod_. In that case, `pow(inv_base, -exp, mod)` is returned, where _inv_base_ is an inverse to _base_ modulo _mod_.
Here’s an example of computing an inverse for `38` modulo `97`:
Copy```
>>> pow(38, -1, mod=97)
23
>>> 23 * 38 % 97 == 1
True

```

Changed in version 3.8: For [`int`](https://docs.python.org/3/library/functions.html#int "int") operands, the three-argument form of `pow` now allows the second argument to be negative, permitting computation of modular inverses.
Changed in version 3.8: Allow keyword arguments. Formerly, only positional arguments were supported.

print(_* objects_, _sep =' '_, _end ='\n'_, _file =None_, _flush =False_)[¶](https://docs.python.org/3/library/functions.html#print "Link to this definition")

Print _objects_ to the text stream _file_ , separated by _sep_ and followed by _end_. _sep_ , _end_ , _file_ , and _flush_ , if present, must be given as keyword arguments.
All non-keyword arguments are converted to strings like [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") does and written to the stream, separated by _sep_ and followed by _end_. Both _sep_ and _end_ must be strings; they can also be `None`, which means to use the default values. If no _objects_ are given, `print()` will just write _end_.
The _file_ argument must be an object with a `write(string)` method; if it is not present or `None`, [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") will be used. Since printed arguments are converted to text strings, `print()` cannot be used with binary mode file objects. For these, use `file.write(...)` instead.
Output buffering is usually determined by _file_. However, if _flush_ is true, the stream is forcibly flushed.
Changed in version 3.3: Added the _flush_ keyword argument.

_class_ property(_fget =None_, _fset =None_, _fdel =None_, _doc =None_)[¶](https://docs.python.org/3/library/functions.html#property "Link to this definition")

Return a property attribute.
_fget_ is a function for getting an attribute value. _fset_ is a function for setting an attribute value. _fdel_ is a function for deleting an attribute value. And _doc_ creates a docstring for the attribute.
A typical use is to define a managed attribute `x`:
Copy```
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

```

If _c_ is an instance of _C_ , `c.x` will invoke the getter, `c.x = value` will invoke the setter, and `del c.x` the deleter.
If given, _doc_ will be the docstring of the property attribute. Otherwise, the property will copy _fget_ ’s docstring (if it exists). This makes it possible to create read-only properties easily using [`property()`](https://docs.python.org/3/library/functions.html#property "property") as a [decorator](https://docs.python.org/3/glossary.html#term-decorator):
Copy```
class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

```

The `@property` decorator turns the `voltage()` method into a “getter” for a read-only attribute with the same name, and it sets the docstring for _voltage_ to “Get the current voltage.”

@getter[¶](https://docs.python.org/3/library/functions.html#property.getter "Link to this definition")


@setter[¶](https://docs.python.org/3/library/functions.html#property.setter "Link to this definition")


@deleter[¶](https://docs.python.org/3/library/functions.html#property.deleter "Link to this definition")

A property object has `getter`, `setter`, and `deleter` methods usable as decorators that create a copy of the property with the corresponding accessor function set to the decorated function. This is best explained with an example:
Copy```
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

```

This code is exactly equivalent to the first example. Be sure to give the additional functions the same name as the original property (`x` in this case.)
The returned property object also has the attributes `fget`, `fset`, and `fdel` corresponding to the constructor arguments.
Changed in version 3.5: The docstrings of property objects are now writeable.

__name__[¶](https://docs.python.org/3/library/functions.html#property.__name__ "Link to this definition")

Attribute holding the name of the property. The name of the property can be changed at runtime.
Added in version 3.13.

_class_ range(_stop_ , _/_)


_class_ range(_start_ , _stop_ , _step =1_, _/_)

Rather than being a function, `range` is actually an immutable sequence type, as documented in [Ranges](https://docs.python.org/3/library/stdtypes.html#typesseq-range) and [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#typesseq).

repr(_object_ , _/_)[¶](https://docs.python.org/3/library/functions.html#repr "Link to this definition")

Return a string containing a printable representation of an object. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval"); otherwise, the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__") method. If [`sys.displayhook()`](https://docs.python.org/3/library/sys.html#sys.displayhook "sys.displayhook") is not accessible, this function will raise [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError").
This class has a custom representation that can be evaluated:
Copy```
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __repr__(self):
      return f"Person('{self.name}', {self.age})"

```


reversed(_object_ , _/_)[¶](https://docs.python.org/3/library/functions.html#reversed "Link to this definition")

Return a reverse [iterator](https://docs.python.org/3/glossary.html#term-iterator). The argument must be an object which has a [`__reversed__()`](https://docs.python.org/3/reference/datamodel.html#object.__reversed__ "object.__reversed__") method or supports the sequence protocol (the [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__") method and the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__") method with integer arguments starting at `0`).

round(_number_ , _ndigits =None_)[¶](https://docs.python.org/3/library/functions.html#round "Link to this definition")

Return _number_ rounded to _ndigits_ precision after the decimal point. If _ndigits_ is omitted or is `None`, it returns the nearest integer to its input.
For the built-in types supporting `round()`, values are rounded to the closest multiple of 10 to the power minus _ndigits_ ; if two multiples are equally close, rounding is done toward the even choice (so, for example, both `round(0.5)` and `round(-0.5)` are `0`, and `round(1.5)` is `2`). Any integer value is valid for _ndigits_ (positive, zero, or negative). The return value is an integer if _ndigits_ is omitted or `None`. Otherwise, the return value has the same type as _number_.
For a general Python object `number`, `round` delegates to `number.__round__`.
Note
The behavior of `round()` for floats can be surprising: for example, `round(2.675, 2)` gives `2.67` instead of the expected `2.68`. This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float. See [Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues) for more information.

_class_ set(_iterable =()_, _/_)

Return a new `set` object, optionally with elements taken from _iterable_. `set` is a built-in class. See `set` and [Set Types — set, frozenset](https://docs.python.org/3/library/stdtypes.html#types-set) for documentation about this class.
For other containers see the built-in [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"), and [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") classes, as well as the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes") module.

setattr(_object_ , _name_ , _value_ , _/_)[¶](https://docs.python.org/3/library/functions.html#setattr "Link to this definition")

This is the counterpart of [`getattr()`](https://docs.python.org/3/library/functions.html#getattr "getattr"). The arguments are an object, a string, and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, `setattr(x, 'foobar', 123)` is equivalent to `x.foobar = 123`.
_name_ need not be a Python identifier as defined in [Names (identifiers and keywords)](https://docs.python.org/3/reference/lexical_analysis.html#identifiers) unless the object chooses to enforce that, for example in a custom [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__") or via [`__slots__`](https://docs.python.org/3/reference/datamodel.html#object.__slots__ "object.__slots__"). An attribute whose name is not an identifier will not be accessible using the dot notation, but is accessible through [`getattr()`](https://docs.python.org/3/library/functions.html#getattr "getattr") etc..
Note
Since [private name mangling](https://docs.python.org/3/reference/expressions.html#private-name-mangling) happens at compilation time, one must manually mangle a private attribute’s (attributes with two leading underscores) name in order to set it with `setattr()`.

_class_ slice(_stop_ , _/_)[¶](https://docs.python.org/3/library/functions.html#slice "Link to this definition")


_class_ slice(_start_ , _stop_ , _step =None_, _/_)

Return a [slice](https://docs.python.org/3/glossary.html#term-slice) object representing the set of indices specified by `range(start, stop, step)`. The _start_ and _step_ arguments default to `None`.
Slice objects are also generated when [slicing syntax](https://docs.python.org/3/reference/expressions.html#slicings) is used. For example: `a[start:stop:step]` or `a[start:stop, i]`.
See [`itertools.islice()`](https://docs.python.org/3/library/itertools.html#itertools.islice "itertools.islice") for an alternate version that returns an [iterator](https://docs.python.org/3/glossary.html#term-iterator).

start[¶](https://docs.python.org/3/library/functions.html#slice.start "Link to this definition")


stop[¶](https://docs.python.org/3/library/functions.html#slice.stop "Link to this definition")


step[¶](https://docs.python.org/3/library/functions.html#slice.step "Link to this definition")

These read-only attributes are set to the argument values (or their default). They have no other explicit functionality; however, they are used by NumPy and other third-party packages.
Changed in version 3.12: Slice objects are now [hashable](https://docs.python.org/3/glossary.html#term-hashable) (provided [`start`](https://docs.python.org/3/library/functions.html#slice.start "slice.start"), [`stop`](https://docs.python.org/3/library/functions.html#slice.stop "slice.stop"), and [`step`](https://docs.python.org/3/library/functions.html#slice.step "slice.step") are hashable).

sorted(_iterable_ , _/_ , _*_ , _key =None_, _reverse =False_)[¶](https://docs.python.org/3/library/functions.html#sorted "Link to this definition")

Return a new sorted list from the items in _iterable_.
Has two optional arguments which must be specified as keyword arguments.
_key_ specifies a function of one argument that is used to extract a comparison key from each element in _iterable_ (for example, `key=str.lower`). The default value is `None` (compare the elements directly).
_reverse_ is a boolean value. If set to `True`, then the list elements are sorted as if each comparison were reversed.
Use [`functools.cmp_to_key()`](https://docs.python.org/3/library/functools.html#functools.cmp_to_key "functools.cmp_to_key") to convert an old-style _cmp_ function to a _key_ function.
The built-in `sorted()` function is guaranteed to be stable. A sort is stable if it guarantees not to change the relative order of elements that compare equal — this is helpful for sorting in multiple passes (for example, sort by department, then by salary grade).
The sort algorithm uses only `<` comparisons between items. While defining an [`__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__") method will suffice for sorting, [**PEP 8**](https://peps.python.org/pep-0008/) recommends that all six [rich comparisons](https://docs.python.org/3/reference/expressions.html#comparisons) be implemented. This will help avoid bugs when using the same data with other ordering tools such as [`max()`](https://docs.python.org/3/library/functions.html#max "max") that rely on a different underlying method. Implementing all six comparisons also helps avoid confusion for mixed type comparisons which can call the reflected [`__gt__()`](https://docs.python.org/3/reference/datamodel.html#object.__gt__ "object.__gt__") method.
For sorting examples and a brief sorting tutorial, see [Sorting Techniques](https://docs.python.org/3/howto/sorting.html#sortinghowto).

@staticmethod[¶](https://docs.python.org/3/library/functions.html#staticmethod "Link to this definition")

Transform a method into a static method.
A static method does not receive an implicit first argument. To declare a static method, use this idiom:
