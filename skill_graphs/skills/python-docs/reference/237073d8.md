# Built-in Functions[¶](https://docs.python.org/3/library/functions.html#built-in-functions "Link to this heading")
The Python interpreter has a number of functions and types built into it that are always available. They are listed here in alphabetical order.
Built-in Functions
---
**A** [`abs()`](https://docs.python.org/3/library/functions.html#abs "abs") [`aiter()`](https://docs.python.org/3/library/functions.html#aiter "aiter") [`all()`](https://docs.python.org/3/library/functions.html#all "all") [`anext()`](https://docs.python.org/3/library/functions.html#anext "anext") [`any()`](https://docs.python.org/3/library/functions.html#any "any") [`ascii()`](https://docs.python.org/3/library/functions.html#ascii "ascii")
**B** [`bin()`](https://docs.python.org/3/library/functions.html#bin "bin") [`bool()`](https://docs.python.org/3/library/functions.html#bool "bool") [`breakpoint()`](https://docs.python.org/3/library/functions.html#breakpoint "breakpoint") [`bytearray()`](https://docs.python.org/3/library/functions.html#func-bytearray) [`bytes()`](https://docs.python.org/3/library/functions.html#func-bytes)
**C** [`callable()`](https://docs.python.org/3/library/functions.html#callable "callable") [`chr()`](https://docs.python.org/3/library/functions.html#chr "chr") [`classmethod()`](https://docs.python.org/3/library/functions.html#classmethod "classmethod") [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile") [`complex()`](https://docs.python.org/3/library/functions.html#complex "complex")
**D** [`delattr()`](https://docs.python.org/3/library/functions.html#delattr "delattr") [`dict()`](https://docs.python.org/3/library/functions.html#func-dict) [`dir()`](https://docs.python.org/3/library/functions.html#dir "dir") [`divmod()`](https://docs.python.org/3/library/functions.html#divmod "divmod")
|  **E** [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate "enumerate") [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval") [`exec()`](https://docs.python.org/3/library/functions.html#exec "exec")
**F** [`filter()`](https://docs.python.org/3/library/functions.html#filter "filter") [`float()`](https://docs.python.org/3/library/functions.html#float "float") [`format()`](https://docs.python.org/3/library/functions.html#format "format") [`frozenset()`](https://docs.python.org/3/library/functions.html#func-frozenset)
**G** [`getattr()`](https://docs.python.org/3/library/functions.html#getattr "getattr") [`globals()`](https://docs.python.org/3/library/functions.html#globals "globals")
**H** [`hasattr()`](https://docs.python.org/3/library/functions.html#hasattr "hasattr") [`hash()`](https://docs.python.org/3/library/functions.html#hash "hash") [`help()`](https://docs.python.org/3/library/functions.html#help "help") [`hex()`](https://docs.python.org/3/library/functions.html#hex "hex")
**I** [`id()`](https://docs.python.org/3/library/functions.html#id "id") [`input()`](https://docs.python.org/3/library/functions.html#input "input") [`int()`](https://docs.python.org/3/library/functions.html#int "int") [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass "issubclass") [`iter()`](https://docs.python.org/3/library/functions.html#iter "iter") |  **L** [`len()`](https://docs.python.org/3/library/functions.html#len "len") [`list()`](https://docs.python.org/3/library/functions.html#func-list) [`locals()`](https://docs.python.org/3/library/functions.html#locals "locals")
**M** [`map()`](https://docs.python.org/3/library/functions.html#map "map") [`max()`](https://docs.python.org/3/library/functions.html#max "max") [`memoryview()`](https://docs.python.org/3/library/functions.html#func-memoryview) [`min()`](https://docs.python.org/3/library/functions.html#min "min")
**N** [`next()`](https://docs.python.org/3/library/functions.html#next "next")
**O** [`object()`](https://docs.python.org/3/library/functions.html#object "object") [`oct()`](https://docs.python.org/3/library/functions.html#oct "oct") [`open()`](https://docs.python.org/3/library/functions.html#open "open") [`ord()`](https://docs.python.org/3/library/functions.html#ord "ord")
**P** [`pow()`](https://docs.python.org/3/library/functions.html#pow "pow") [`print()`](https://docs.python.org/3/library/functions.html#print "print") [`property()`](https://docs.python.org/3/library/functions.html#property "property")



|  **R** [`range()`](https://docs.python.org/3/library/functions.html#func-range) [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") [`reversed()`](https://docs.python.org/3/library/functions.html#reversed "reversed") [`round()`](https://docs.python.org/3/library/functions.html#round "round")
**S** [`set()`](https://docs.python.org/3/library/functions.html#func-set) [`setattr()`](https://docs.python.org/3/library/functions.html#setattr "setattr") [`slice()`](https://docs.python.org/3/library/functions.html#slice "slice") [`sorted()`](https://docs.python.org/3/library/functions.html#sorted "sorted") [`staticmethod()`](https://docs.python.org/3/library/functions.html#staticmethod "staticmethod") [`str()`](https://docs.python.org/3/library/functions.html#func-str) [`sum()`](https://docs.python.org/3/library/functions.html#sum "sum") [`super()`](https://docs.python.org/3/library/functions.html#super "super")
**T** [`tuple()`](https://docs.python.org/3/library/functions.html#func-tuple) [`type()`](https://docs.python.org/3/library/functions.html#type "type")
**V** [`vars()`](https://docs.python.org/3/library/functions.html#vars "vars")
**Z** [`zip()`](https://docs.python.org/3/library/functions.html#zip "zip")
**_** [`__import__()`](https://docs.python.org/3/library/functions.html#import__ "__import__")

abs(_number_ , _/_)[¶](https://docs.python.org/3/library/functions.html#abs "Link to this definition")

Return the absolute value of a number. The argument may be an integer, a floating-point number, or an object implementing [`__abs__()`](https://docs.python.org/3/reference/datamodel.html#object.__abs__ "object.__abs__"). If the argument is a complex number, its magnitude is returned.

aiter(_async_iterable_ , _/_)[¶](https://docs.python.org/3/library/functions.html#aiter "Link to this definition")

Return an [asynchronous iterator](https://docs.python.org/3/glossary.html#term-asynchronous-iterator) for an [asynchronous iterable](https://docs.python.org/3/glossary.html#term-asynchronous-iterable). Equivalent to calling `x.__aiter__()`.
Note: Unlike [`iter()`](https://docs.python.org/3/library/functions.html#iter "iter"), `aiter()` has no 2-argument variant.
Added in version 3.10.

all(_iterable_ , _/_)[¶](https://docs.python.org/3/library/functions.html#all "Link to this definition")

Return `True` if all elements of the _iterable_ are true (or if the iterable is empty). Equivalent to:
Copy```
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

```


_awaitable _anext(_async_iterator_ , _/_)[¶](https://docs.python.org/3/library/functions.html#anext "Link to this definition")


_awaitable _anext(_async_iterator_ , _default_ , _/_)

When awaited, return the next item from the given [asynchronous iterator](https://docs.python.org/3/glossary.html#term-asynchronous-iterator), or _default_ if given and the iterator is exhausted.
This is the async variant of the [`next()`](https://docs.python.org/3/library/functions.html#next "next") builtin, and behaves similarly.
This calls the [`__anext__()`](https://docs.python.org/3/reference/datamodel.html#object.__anext__ "object.__anext__") method of _async_iterator_ , returning an [awaitable](https://docs.python.org/3/glossary.html#term-awaitable). Awaiting this returns the next value of the iterator. If _default_ is given, it is returned if the iterator is exhausted, otherwise [`StopAsyncIteration`](https://docs.python.org/3/library/exceptions.html#StopAsyncIteration "StopAsyncIteration") is raised.
Added in version 3.10.

any(_iterable_ , _/_)[¶](https://docs.python.org/3/library/functions.html#any "Link to this definition")

Return `True` if any element of the _iterable_ is true. If the iterable is empty, return `False`. Equivalent to:
Copy```
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

```


ascii(_object_ , _/_)[¶](https://docs.python.org/3/library/functions.html#ascii "Link to this definition")

As [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr"), return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by `repr()` using `\x`, `\u`, or `\U` escapes. This generates a string similar to that returned by `repr()` in Python 2.

bin(_integer_ , _/_)[¶](https://docs.python.org/3/library/functions.html#bin "Link to this definition")

Convert an integer number to a binary string prefixed with “0b”. The result is a valid Python expression. If _integer_ is not a Python [`int`](https://docs.python.org/3/library/functions.html#int "int") object, it has to define an [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") method that returns an integer. Some examples:
Copy```
>>> bin(3)
'0b11'
>>> bin(-10)
'-0b1010'

```

If the prefix “0b” is desired or not, you can use either of the following ways.
Copy```
>>> format(14, '#b'), format(14, 'b')
('0b1110', '1110')
>>> f'{14:#b}', f'{14:b}'
('0b1110', '1110')

```

See also [`enum.bin()`](https://docs.python.org/3/library/enum.html#enum.bin "enum.bin") to represent negative values as twos-complement.
See also [`format()`](https://docs.python.org/3/library/functions.html#format "format") for more information.

_class_ bool(_object =False_, _/_)[¶](https://docs.python.org/3/library/functions.html#bool "Link to this definition")

Return a Boolean value, i.e. one of `True` or `False`. The argument is converted using the standard [truth testing procedure](https://docs.python.org/3/library/stdtypes.html#truth). If the argument is false or omitted, this returns `False`; otherwise, it returns `True`. The `bool` class is a subclass of [`int`](https://docs.python.org/3/library/functions.html#int "int") (see [Numeric Types — int, float, complex](https://docs.python.org/3/library/stdtypes.html#typesnumeric)). It cannot be subclassed further. Its only instances are `False` and `True` (see [Boolean Type - bool](https://docs.python.org/3/library/stdtypes.html#typebool)).
Changed in version 3.7: The parameter is now positional-only.

breakpoint(_* args_, _** kws_)[¶](https://docs.python.org/3/library/functions.html#breakpoint "Link to this definition")

This function drops you into the debugger at the call site. Specifically, it calls [`sys.breakpointhook()`](https://docs.python.org/3/library/sys.html#sys.breakpointhook "sys.breakpointhook"), passing `args` and `kws` straight through. By default, `sys.breakpointhook()` calls [`pdb.set_trace()`](https://docs.python.org/3/library/pdb.html#pdb.set_trace "pdb.set_trace") expecting no arguments. In this case, it is purely a convenience function so you don’t have to explicitly import [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.") or type as much code to enter the debugger. However, `sys.breakpointhook()` can be set to some other function and `breakpoint()` will automatically call that, allowing you to drop into the debugger of choice. If `sys.breakpointhook()` is not accessible, this function will raise [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError").
By default, the behavior of `breakpoint()` can be changed with the [`PYTHONBREAKPOINT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONBREAKPOINT) environment variable. See [`sys.breakpointhook()`](https://docs.python.org/3/library/sys.html#sys.breakpointhook "sys.breakpointhook") for usage details.
Note that this is not guaranteed if [`sys.breakpointhook()`](https://docs.python.org/3/library/sys.html#sys.breakpointhook "sys.breakpointhook") has been replaced.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `builtins.breakpoint` with argument `breakpointhook`.
Added in version 3.7.

_class_ bytearray(_source =b''_)


_class_ bytearray(_source_ , _encoding_ , _errors ='strict'_)

Return a new array of bytes. The `bytearray` class is a mutable sequence of integers in the range 0 <= x < 256. It has most of the usual methods of mutable sequences, described in [Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable), as well as most methods that the [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") type has, see [Bytes and Bytearray Operations](https://docs.python.org/3/library/stdtypes.html#bytes-methods).
The optional _source_ parameter can be used to initialize the array in a few different ways:
  * If it is a _string_ , you must also give the _encoding_ (and optionally, _errors_) parameters; [`bytearray()`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") then converts the string to bytes using [`str.encode()`](https://docs.python.org/3/library/stdtypes.html#str.encode "str.encode").
  * If it is an _integer_ , the array will have that size and will be initialized with null bytes.
  * If it is an object conforming to the [buffer interface](https://docs.python.org/3/c-api/buffer.html#bufferobjects), a read-only buffer of the object will be used to initialize the bytes array.
  * If it is an _iterable_ , it must be an iterable of integers in the range `0 <= x < 256`, which are used as the initial contents of the array.


Without an argument, an array of size 0 is created.
See also [Binary Sequence Types — bytes, bytearray, memoryview](https://docs.python.org/3/library/stdtypes.html#binaryseq) and [Bytearray Objects](https://docs.python.org/3/library/stdtypes.html#typebytearray).

_class_ bytes(_source =b''_)


_class_ bytes(_source_ , _encoding_ , _errors ='strict'_)

Return a new “bytes” object which is an immutable sequence of integers in the range `0 <= x < 256`. `bytes` is an immutable version of [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") – it has the same non-mutating methods and the same indexing and slicing behavior.
Accordingly, constructor arguments are interpreted as for [`bytearray()`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray").
Bytes objects can also be created with literals, see [String and Bytes literals](https://docs.python.org/3/reference/lexical_analysis.html#strings).
See also [Binary Sequence Types — bytes, bytearray, memoryview](https://docs.python.org/3/library/stdtypes.html#binaryseq), [Bytes Objects](https://docs.python.org/3/library/stdtypes.html#typebytes), and [Bytes and Bytearray Operations](https://docs.python.org/3/library/stdtypes.html#bytes-methods).

callable(_object_ , _/_)[¶](https://docs.python.org/3/library/functions.html#callable "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the _object_ argument appears callable, [`False`](https://docs.python.org/3/library/constants.html#False "False") if not. If this returns `True`, it is still possible that a call fails, but if it is `False`, calling _object_ will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__") method.
Added in version 3.2: This function was first removed in Python 3.0 and then brought back in Python 3.2.

chr(_codepoint_ , _/_)[¶](https://docs.python.org/3/library/functions.html#chr "Link to this definition")

Return the string representing a character with the specified Unicode code point. For example, `chr(97)` returns the string `'a'`, while `chr(8364)` returns the string `'€'`. This is the inverse of [`ord()`](https://docs.python.org/3/library/functions.html#ord "ord").
The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised if it is outside that range.

@classmethod[¶](https://docs.python.org/3/library/functions.html#classmethod "Link to this definition")

Transform a method into a class method.
A class method receives the class as an implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom:
Copy```
class C:
    @classmethod
    def f(cls, arg1, arg2): ...

```

The `@classmethod` form is a function [decorator](https://docs.python.org/3/glossary.html#term-decorator) – see [Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function) for details.
A class method can be called either on the class (such as `C.f()`) or on an instance (such as `C().f()`). The instance is ignored except for its class. If a class method is called for a derived class, the derived class object is passed as the implied first argument.
Class methods are different than C++ or Java static methods. If you want those, see [`staticmethod()`](https://docs.python.org/3/library/functions.html#staticmethod "staticmethod") in this section. For more information on class methods, see [The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#types).
Changed in version 3.9: Class methods can now wrap other [descriptors](https://docs.python.org/3/glossary.html#term-descriptor) such as [`property()`](https://docs.python.org/3/library/functions.html#property "property").
Changed in version 3.10: Class methods now inherit the method attributes ([`__module__`](https://docs.python.org/3/reference/datamodel.html#function.__module__ "function.__module__"), [`__name__`](https://docs.python.org/3/reference/datamodel.html#function.__name__ "function.__name__"), [`__qualname__`](https://docs.python.org/3/reference/datamodel.html#function.__qualname__ "function.__qualname__"), [`__doc__`](https://docs.python.org/3/reference/datamodel.html#function.__doc__ "function.__doc__") and [`__annotations__`](https://docs.python.org/3/reference/datamodel.html#function.__annotations__ "function.__annotations__")) and have a new `__wrapped__` attribute.
Deprecated since version 3.11, removed in version 3.13: Class methods can no longer wrap other [descriptors](https://docs.python.org/3/glossary.html#term-descriptor) such as [`property()`](https://docs.python.org/3/library/functions.html#property "property").

compile(_source_ , _filename_ , _mode_ , _flags =0_, _dont_inherit =False_, _optimize =-1_)[¶](https://docs.python.org/3/library/functions.html#compile "Link to this definition")

Compile the _source_ into a code or AST object. Code objects can be executed by [`exec()`](https://docs.python.org/3/library/functions.html#exec "exec") or [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval"). _source_ can either be a normal string, a byte string, or an AST object. Refer to the [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.") module documentation for information on how to work with AST objects.
The _filename_ argument should give the file from which the code was read; pass some recognizable value if it wasn’t read from a file (`'<string>'` is commonly used).
The _mode_ argument specifies what kind of code must be compiled; it can be `'exec'` if _source_ consists of a sequence of statements, `'eval'` if it consists of a single expression, or `'single'` if it consists of a single interactive statement (in the latter case, expression statements that evaluate to something other than `None` will be printed).
The optional arguments _flags_ and _dont_inherit_ control which [compiler options](https://docs.python.org/3/library/ast.html#ast-compiler-flags) should be activated and which [future features](https://docs.python.org/3/reference/simple_stmts.html#future) should be allowed. If neither is present (or both are zero) the code is compiled with the same flags that affect the code that is calling `compile()`. If the _flags_ argument is given and _dont_inherit_ is not (or is zero) then the compiler options and the future statements specified by the _flags_ argument are used in addition to those that would be used anyway. If _dont_inherit_ is a non-zero integer then the _flags_ argument is it – the flags (future features and compiler options) in the surrounding code are ignored.
Compiler options and future statements are specified by bits which can be bitwise ORed together to specify multiple options. The bitfield required to specify a given future feature can be found as the [`compiler_flag`](https://docs.python.org/3/library/__future__.html#future__._Feature.compiler_flag "__future__._Feature.compiler_flag") attribute on the [`_Feature`](https://docs.python.org/3/library/__future__.html#future__._Feature "__future__._Feature") instance in the [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions") module. [Compiler flags](https://docs.python.org/3/library/ast.html#ast-compiler-flags) can be found in [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.") module, with `PyCF_` prefix.
The argument _optimize_ specifies the optimization level of the compiler; the default value of `-1` selects the optimization level of the interpreter as given by [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O) options. Explicit levels are `0` (no optimization; `__debug__` is true), `1` (asserts are removed, `__debug__` is false) or `2` (docstrings are removed too).
This function raises [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") or [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the compiled source is invalid.
If you want to parse Python code into its AST representation, see [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse").
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `compile` with arguments `source` and `filename`. This event may also be raised by implicit compilation.
Note
When compiling a string with multi-line code in `'single'` or `'eval'` mode, input must be terminated by at least one newline character. This is to facilitate detection of incomplete and complete statements in the [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.") module.
Warning
It is possible to crash the Python interpreter with a sufficiently large/complex string when compiling to an AST object due to stack depth limitations in Python’s AST compiler.
Changed in version 3.2: Allowed use of Windows and Mac newlines. Also, input in `'exec'` mode does not have to end in a newline anymore. Added the _optimize_ parameter.
Changed in version 3.5: Previously, [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") was raised when null bytes were encountered in _source_.
Added in version 3.8: `ast.PyCF_ALLOW_TOP_LEVEL_AWAIT` can now be passed in flags to enable support for top-level `await`, `async for`, and `async with`.

_class_ complex(_number =0_, _/_)[¶](https://docs.python.org/3/library/functions.html#complex "Link to this definition")


_class_ complex(_string_ , _/_)


_class_ complex(_real =0_, _imag =0_)

Convert a single string or number to a complex number, or create a complex number from real and imaginary parts.
Examples:
Copy```
>>> complex('+1.23')
(1.23+0j)
>>> complex('-4.5j')
-4.5j
>>> complex('-1.23+4.5j')
(-1.23+4.5j)
>>> complex('\t( -1.23+4.5J )\n')
(-1.23+4.5j)
>>> complex('-Infinity+NaNj')
(-inf+nanj)
>>> complex(1.23)
(1.23+0j)
>>> complex(imag=-4.5)
-4.5j
>>> complex(-1.23, 4.5)
(-1.23+4.5j)

```

If the argument is a string, it must contain either a real part (in the same format as for [`float()`](https://docs.python.org/3/library/functions.html#float "float")) or an imaginary part (in the same format but with a `'j'` or `'J'` suffix), or both real and imaginary parts (the sign of the imaginary part is mandatory in this case). The string can optionally be surrounded by whitespaces and the round parentheses `'('` and `')'`, which are ignored. The string must not contain whitespace between `'+'`, `'-'`, the `'j'` or `'J'` suffix, and the decimal number. For example, `complex('1+2j')` is fine, but `complex('1 + 2j')` raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"). More precisely, the input must conform to the [`complexvalue`](https://docs.python.org/3/library/functions.html#grammar-token-float-complexvalue) production rule in the following grammar, after parentheses and leading and trailing whitespace characters are removed:
```
**complexvalue**: [floatvalue](https://docs.python.org/3/library/functions.html#grammar-token-float-floatvalue) |
