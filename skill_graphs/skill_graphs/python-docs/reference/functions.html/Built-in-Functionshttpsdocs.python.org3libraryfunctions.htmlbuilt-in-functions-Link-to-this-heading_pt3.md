Note
For objects with custom [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__") methods, note that `hash()` truncates the return value based on the bit width of the host machine.

help()[¶](https://docs.python.org/3/library/functions.html#help "Link to this definition")


help(_request_)

Invoke the built-in help system. (This function is intended for interactive use.) If no argument is given, the interactive help system starts on the interpreter console. If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console. If the argument is any other kind of object, a help page on the object is generated.
Note that if a slash(/) appears in the parameter list of a function when invoking `help()`, it means that the parameters prior to the slash are positional-only. For more info, see [the FAQ entry on positional-only parameters](https://docs.python.org/3/faq/programming.html#faq-positional-only-arguments).
This function is added to the built-in namespace by the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") module.
Changed in version 3.4: Changes to [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.") and [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.") mean that the reported signatures for callables are now more comprehensive and consistent.

hex(_integer_ , _/_)[¶](https://docs.python.org/3/library/functions.html#hex "Link to this definition")

Convert an integer number to a lowercase hexadecimal string prefixed with “0x”. If _integer_ is not a Python [`int`](https://docs.python.org/3/library/functions.html#int "int") object, it has to define an [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") method that returns an integer. Some examples:
Copy```
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'

```

If you want to convert an integer number to an uppercase or lower hexadecimal string with prefix or not, you can use either of the following ways:
Copy```
>>> '%#x' % 255, '%x' % 255, '%X' % 255
('0xff', 'ff', 'FF')
>>> format(255, '#x'), format(255, 'x'), format(255, 'X')
('0xff', 'ff', 'FF')
>>> f'{255:#x}', f'{255:x}', f'{255:X}'
('0xff', 'ff', 'FF')

```

See also [`format()`](https://docs.python.org/3/library/functions.html#format "format") for more information.
See also [`int()`](https://docs.python.org/3/library/functions.html#int "int") for converting a hexadecimal string to an integer using a base of 16.
Note
To obtain a hexadecimal string representation for a float, use the [`float.hex()`](https://docs.python.org/3/library/stdtypes.html#float.hex "float.hex") method.

id(_object_ , _/_)[¶](https://docs.python.org/3/library/functions.html#id "Link to this definition")

Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same `id()` value.
**CPython implementation detail:** This is the address of the object in memory.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `builtins.id` with argument `id`.

input()[¶](https://docs.python.org/3/library/functions.html#input "Link to this definition")


input(_prompt_ , _/_)

If the _prompt_ argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError "EOFError") is raised. Example:
Copy```
>>> s = input('--> ')
--> Monty Python's Flying Circus
>>> s
"Monty Python's Flying Circus"

```

If the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") module was loaded, then `input()` will use it to provide elaborate line editing and history features.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `builtins.input` with argument `prompt` before reading input
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `builtins.input/result` with the result after successfully reading input.

_class_ int(_number =0_, _/_)[¶](https://docs.python.org/3/library/functions.html#int "Link to this definition")


_class_ int(_string_ , _/_ , _base =10_)

Return an integer object constructed from a number or a string, or return `0` if no arguments are given.
Examples:
Copy```
>>> int(123.45)
123
>>> int('123')
123
>>> int('   -12_345\n')
-12345
>>> int('FACE', 16)
64206
>>> int('0xface', 0)
64206
>>> int('01110011', base=2)
115

```

If the argument defines [`__int__()`](https://docs.python.org/3/reference/datamodel.html#object.__int__ "object.__int__"), `int(x)` returns `x.__int__()`. If the argument defines [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__"), it returns `x.__index__()`. For floating-point numbers, this truncates towards zero.
If the argument is not a number or if _base_ is given, then it must be a string, [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") instance representing an integer in radix _base_. Optionally, the string can be preceded by `+` or `-` (with no space in between), have leading zeros, be surrounded by whitespace, and have single underscores interspersed between digits.
A base-n integer string contains digits, each representing a value from 0 to n-1. The values 0–9 can be represented by any Unicode decimal digit. The values 10–35 can be represented by `a` to `z` (or `A` to `Z`). The default _base_ is 10. The allowed bases are 0 and 2–36. Base-2, -8, and -16 strings can be optionally prefixed with `0b`/`0B`, `0o`/`0O`, or `0x`/`0X`, as with integer literals in code. For base 0, the string is interpreted in a similar way to an [integer literal in code](https://docs.python.org/3/reference/lexical_analysis.html#integers), in that the actual base is 2, 8, 10, or 16 as determined by the prefix. Base 0 also disallows leading zeros: `int('010', 0)` is not legal, while `int('010')` and `int('010', 8)` are.
The integer type is described in [Numeric Types — int, float, complex](https://docs.python.org/3/library/stdtypes.html#typesnumeric).
Changed in version 3.4: If _base_ is not an instance of `int` and the _base_ object has a [`base.__index__`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") method, that method is called to obtain an integer for the base. Previous versions used [`base.__int__`](https://docs.python.org/3/reference/datamodel.html#object.__int__ "object.__int__") instead of `base.__index__`.
Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.
Changed in version 3.7: The first parameter is now positional-only.
Changed in version 3.8: Falls back to [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") if [`__int__()`](https://docs.python.org/3/reference/datamodel.html#object.__int__ "object.__int__") is not defined.
Changed in version 3.11: `int` string inputs and string representations can be limited to help avoid denial of service attacks. A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised when the limit is exceeded while converting a string to an `int` or when converting an `int` into a string would exceed the limit. See the [integer string conversion length limitation](https://docs.python.org/3/library/stdtypes.html#int-max-str-digits) documentation.
Changed in version 3.14: [`int()`](https://docs.python.org/3/library/functions.html#int "int") no longer delegates to the [`__trunc__()`](https://docs.python.org/3/reference/datamodel.html#object.__trunc__ "object.__trunc__") method.

isinstance(_object_ , _classinfo_ , _/_)[¶](https://docs.python.org/3/library/functions.html#isinstance "Link to this definition")

Return `True` if the _object_ argument is an instance of the _classinfo_ argument, or of a (direct, indirect, or [virtual](https://docs.python.org/3/glossary.html#term-abstract-base-class)) subclass thereof. If _object_ is not an object of the given type, the function always returns `False`. If _classinfo_ is a tuple of type objects (or recursively, other such tuples) or a [Union Type](https://docs.python.org/3/library/stdtypes.html#types-union) of multiple types, return `True` if _object_ is an instance of any of the types. If _classinfo_ is not a type or tuple of types and such tuples, a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception is raised. `TypeError` may not be raised for an invalid type if an earlier check succeeds.
Changed in version 3.10: _classinfo_ can be a [Union Type](https://docs.python.org/3/library/stdtypes.html#types-union).

issubclass(_class_ , _classinfo_ , _/_)[¶](https://docs.python.org/3/library/functions.html#issubclass "Link to this definition")

Return `True` if _class_ is a subclass (direct, indirect, or [virtual](https://docs.python.org/3/glossary.html#term-abstract-base-class)) of _classinfo_. A class is considered a subclass of itself. _classinfo_ may be a tuple of class objects (or recursively, other such tuples) or a [Union Type](https://docs.python.org/3/library/stdtypes.html#types-union), in which case return `True` if _class_ is a subclass of any entry in _classinfo_. In any other case, a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception is raised.
Changed in version 3.10: _classinfo_ can be a [Union Type](https://docs.python.org/3/library/stdtypes.html#types-union).

iter(_iterable_ , _/_)[¶](https://docs.python.org/3/library/functions.html#iter "Link to this definition")


iter(_callable_ , _sentinel_ , _/_)

Return an [iterator](https://docs.python.org/3/glossary.html#term-iterator) object. The first argument is interpreted very differently depending on the presence of the second argument. Without a second argument, the single argument must be a collection object which supports the [iterable](https://docs.python.org/3/glossary.html#term-iterable) protocol (the [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__ "object.__iter__") method), or it must support the sequence protocol (the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__") method with integer arguments starting at `0`). If it does not support either of those protocols, [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised. If the second argument, _sentinel_ , is given, then the first argument must be a callable object. The iterator created in this case will call _callable_ with no arguments for each call to its [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") method; if the value returned is equal to _sentinel_ , [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration") will be raised, otherwise the value will be returned.
See also [Iterator Types](https://docs.python.org/3/library/stdtypes.html#typeiter).
One useful application of the second form of `iter()` is to build a block-reader. For example, reading fixed-width blocks from a binary database file until the end of file is reached:
Copy```
from functools import partial
with open('mydata.db', 'rb') as f:
    for block in iter(partial(f.read, 64), b''):
        process_block(block)

```


len(_object_ , _/_)[¶](https://docs.python.org/3/library/functions.html#len "Link to this definition")

Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).
**CPython implementation detail:** `len` raises [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") on lengths larger than [`sys.maxsize`](https://docs.python.org/3/library/sys.html#sys.maxsize "sys.maxsize"), such as [`range(2 ** 100)`](https://docs.python.org/3/library/stdtypes.html#range "range").

_class_ list(_iterable =()_, _/_)

Rather than being a function, `list` is actually a mutable sequence type, as documented in [Lists](https://docs.python.org/3/library/stdtypes.html#typesseq-list) and [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#typesseq).

locals()[¶](https://docs.python.org/3/library/functions.html#locals "Link to this definition")

Return a mapping object representing the current local symbol table, with variable names as the keys, and their currently bound references as the values.
At module scope, as well as when using [`exec()`](https://docs.python.org/3/library/functions.html#exec "exec") or [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval") with a single namespace, this function returns the same namespace as [`globals()`](https://docs.python.org/3/library/functions.html#globals "globals").
At class scope, it returns the namespace that will be passed to the metaclass constructor.
When using `exec()` or `eval()` with separate local and global arguments, it returns the local namespace passed in to the function call.
In all of the above cases, each call to `locals()` in a given frame of execution will return the _same_ mapping object. Changes made through the mapping object returned from `locals()` will be visible as assigned, reassigned, or deleted local variables, and assigning, reassigning, or deleting local variables will immediately affect the contents of the returned mapping object.
In an [optimized scope](https://docs.python.org/3/glossary.html#term-optimized-scope) (including functions, generators, and coroutines), each call to `locals()` instead returns a fresh dictionary containing the current bindings of the function’s local variables and any nonlocal cell references. In this case, name binding changes made via the returned dict are _not_ written back to the corresponding local variables or nonlocal cell references, and assigning, reassigning, or deleting local variables and nonlocal cell references does _not_ affect the contents of previously returned dictionaries.
Calling `locals()` as part of a comprehension in a function, generator, or coroutine is equivalent to calling it in the containing scope, except that the comprehension’s initialised iteration variables will be included. In other scopes, it behaves as if the comprehension were running as a nested function.
Calling `locals()` as part of a generator expression is equivalent to calling it in a nested generator function.
Changed in version 3.12: The behaviour of `locals()` in a comprehension has been updated as described in [**PEP 709**](https://peps.python.org/pep-0709/).
Changed in version 3.13: As part of [**PEP 667**](https://peps.python.org/pep-0667/), the semantics of mutating the mapping objects returned from this function are now defined. The behavior in [optimized scopes](https://docs.python.org/3/glossary.html#term-optimized-scope) is now as described above. Aside from being defined, the behaviour in other scopes remains unchanged from previous versions.

map(_function_ , _iterable_ , _/_ , _* iterables_, _strict =False_)[¶](https://docs.python.org/3/library/functions.html#map "Link to this definition")

Return an iterator that applies _function_ to every item of _iterable_ , yielding the results. If additional _iterables_ arguments are passed, _function_ must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. If _strict_ is `True` and one of the iterables is exhausted before the others, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. For cases where the function inputs are already arranged into argument tuples, see [`itertools.starmap()`](https://docs.python.org/3/library/itertools.html#itertools.starmap "itertools.starmap").
Changed in version 3.14: Added the _strict_ parameter.

max(_iterable_ , _/_ , _*_ , _key =None_)[¶](https://docs.python.org/3/library/functions.html#max "Link to this definition")


max(_iterable_ , _/_ , _*_ , _default_ , _key =None_)


max(_arg1_ , _arg2_ , _/_ , _* args_, _key =None_)

Return the largest item in an iterable or the largest of two or more arguments.
If one positional argument is provided, it should be an [iterable](https://docs.python.org/3/glossary.html#term-iterable). The largest item in the iterable is returned. If two or more positional arguments are provided, the largest of the positional arguments is returned.
There are two optional keyword-only arguments. The _key_ argument specifies a one-argument ordering function like that used for [`list.sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort "list.sort"). The _default_ argument specifies an object to return if the provided iterable is empty. If the iterable is empty and _default_ is not provided, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
If multiple items are maximal, the function returns the first one encountered. This is consistent with other sort-stability preserving tools such as `sorted(iterable, key=keyfunc, reverse=True)[0]` and `heapq.nlargest(1, iterable, key=keyfunc)`.
Changed in version 3.4: Added the _default_ keyword-only parameter.
Changed in version 3.8: The _key_ can be `None`.

_class_ memoryview(_object_)

Return a “memory view” object created from the given argument. See [Memory Views](https://docs.python.org/3/library/stdtypes.html#typememoryview) for more information.

min(_iterable_ , _/_ , _*_ , _key =None_)[¶](https://docs.python.org/3/library/functions.html#min "Link to this definition")


min(_iterable_ , _/_ , _*_ , _default_ , _key =None_)


min(_arg1_ , _arg2_ , _/_ , _* args_, _key =None_)

Return the smallest item in an iterable or the smallest of two or more arguments.
If one positional argument is provided, it should be an [iterable](https://docs.python.org/3/glossary.html#term-iterable). The smallest item in the iterable is returned. If two or more positional arguments are provided, the smallest of the positional arguments is returned.
There are two optional keyword-only arguments. The _key_ argument specifies a one-argument ordering function like that used for [`list.sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort "list.sort"). The _default_ argument specifies an object to return if the provided iterable is empty. If the iterable is empty and _default_ is not provided, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
If multiple items are minimal, the function returns the first one encountered. This is consistent with other sort-stability preserving tools such as `sorted(iterable, key=keyfunc)[0]` and `heapq.nsmallest(1, iterable, key=keyfunc)`.
Changed in version 3.4: Added the _default_ keyword-only parameter.
Changed in version 3.8: The _key_ can be `None`.

next(_iterator_ , _/_)[¶](https://docs.python.org/3/library/functions.html#next "Link to this definition")


next(_iterator_ , _default_ , _/_)

Retrieve the next item from the [iterator](https://docs.python.org/3/glossary.html#term-iterator) by calling its [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") method. If _default_ is given, it is returned if the iterator is exhausted, otherwise [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration") is raised.

_class_ object[¶](https://docs.python.org/3/library/functions.html#object "Link to this definition")

This is the ultimate base class of all other classes. It has methods that are common to all instances of Python classes. When the constructor is called, it returns a new featureless object. The constructor does not accept any arguments.
Note
`object` instances do _not_ have [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") attributes, so you can’t assign arbitrary attributes to an instance of `object`.

oct(_integer_ , _/_)[¶](https://docs.python.org/3/library/functions.html#oct "Link to this definition")

Convert an integer number to an octal string prefixed with “0o”. The result is a valid Python expression. If _integer_ is not a Python [`int`](https://docs.python.org/3/library/functions.html#int "int") object, it has to define an [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") method that returns an integer. For example:
Copy```
>>> oct(8)
'0o10'
>>> oct(-56)
'-0o70'

```

If you want to convert an integer number to an octal string either with the prefix “0o” or not, you can use either of the following ways.
Copy```
>>> '%#o' % 10, '%o' % 10
('0o12', '12')
>>> format(10, '#o'), format(10, 'o')
('0o12', '12')
>>> f'{10:#o}', f'{10:o}'
('0o12', '12')

```

See also [`format()`](https://docs.python.org/3/library/functions.html#format "format") for more information.

open(_file_ , _mode ='r'_, _buffering =-1_, _encoding =None_, _errors =None_, _newline =None_, _closefd =True_, _opener =None_)[¶](https://docs.python.org/3/library/functions.html#open "Link to this definition")

Open _file_ and return a corresponding [file object](https://docs.python.org/3/glossary.html#term-file-object). If the file cannot be opened, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised. See [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#tut-files) for more examples of how to use this function.
_file_ is a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) giving the pathname (absolute or relative to the current working directory) of the file to be opened or an integer file descriptor of the file to be wrapped. (If a file descriptor is given, it is closed when the returned I/O object is closed unless _closefd_ is set to `False`.)
_mode_ is an optional string that specifies the mode in which the file is opened. It defaults to `'r'` which means open for reading in text mode. Other common values are `'w'` for writing (truncating the file if it already exists), `'x'` for exclusive creation, and `'a'` for appending (which on _some_ Unix systems, means that _all_ writes append to the end of the file regardless of the current seek position). In text mode, if _encoding_ is not specified the encoding used is platform-dependent: [`locale.getencoding()`](https://docs.python.org/3/library/locale.html#locale.getencoding "locale.getencoding") is called to get the current locale encoding. (For reading and writing raw bytes use binary mode and leave _encoding_ unspecified.) The available modes are:
Character | Meaning
---|---
`'r'` | open for reading (default)
`'w'` | open for writing, truncating the file first
`'x'` | open for exclusive creation, failing if the file already exists
`'a'` | open for writing, appending to the end of file if it exists
`'b'` | binary mode
`'t'` | text mode (default)
`'+'` | open for updating (reading and writing)
The default mode is `'r'` (open for reading text, a synonym of `'rt'`). Modes `'w+'` and `'w+b'` open and truncate the file. Modes `'r+'` and `'r+b'` open the file with no truncation.
As mentioned in the [Overview](https://docs.python.org/3/library/io.html#io-overview), Python distinguishes between binary and text I/O. Files opened in binary mode (including `'b'` in the _mode_ argument) return contents as [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects without any decoding. In text mode (the default, or when `'t'` is included in the _mode_ argument), the contents of the file are returned as [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), the bytes having been first decoded using a platform-dependent encoding or using the specified _encoding_ if given.
Note
Python doesn’t depend on the underlying operating system’s notion of text files; all the processing is done by Python itself, and is therefore platform-independent.
_buffering_ is an optional integer used to set the buffering policy. Pass 0 to switch buffering off (only allowed in binary mode), 1 to select line buffering (only usable when writing in text mode), and an integer > 1 to indicate the size in bytes of a fixed-size chunk buffer. Note that specifying a buffer size this way applies for binary buffered I/O, but `TextIOWrapper` (i.e., files opened with `mode='r+'`) would have another buffering. To disable buffering in `TextIOWrapper`, consider using the `write_through` flag for [`io.TextIOWrapper.reconfigure()`](https://docs.python.org/3/library/io.html#io.TextIOWrapper.reconfigure "io.TextIOWrapper.reconfigure"). When no _buffering_ argument is given, the default buffering policy works as follows:
