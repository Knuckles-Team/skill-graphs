              [floatvalue](https://docs.python.org/3/library/functions.html#grammar-token-float-floatvalue) ("j" | "J") |
              [floatvalue](https://docs.python.org/3/library/functions.html#grammar-token-float-floatvalue) [sign](https://docs.python.org/3/library/functions.html#grammar-token-float-sign) [absfloatvalue](https://docs.python.org/3/library/functions.html#grammar-token-float-absfloatvalue) ("j" | "J")

```

If the argument is a number, the constructor serves as a numeric conversion like [`int`](https://docs.python.org/3/library/functions.html#int "int") and [`float`](https://docs.python.org/3/library/functions.html#float "float"). For a general Python object `x`, `complex(x)` delegates to `x.__complex__()`. If [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__") is not defined then it falls back to [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__"). If `__float__()` is not defined then it falls back to [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__").
If two arguments are provided or keyword arguments are used, each argument may be any numeric type (including complex). If both arguments are real numbers, return a complex number with the real component _real_ and the imaginary component _imag_. If both arguments are complex numbers, return a complex number with the real component `real.real-imag.imag` and the imaginary component `real.imag+imag.real`. If one of arguments is a real number, only its real component is used in the above expressions.
See also [`complex.from_number()`](https://docs.python.org/3/library/stdtypes.html#complex.from_number "complex.from_number") which only accepts a single numeric argument.
If all arguments are omitted, returns `0j`.
The complex type is described in [Numeric Types — int, float, complex](https://docs.python.org/3/library/stdtypes.html#typesnumeric).
Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.
Changed in version 3.8: Falls back to [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") if [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__") and [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__") are not defined.
Deprecated since version 3.14: Passing a complex number as the _real_ or _imag_ argument is now deprecated; it should only be passed as a single positional argument.

delattr(_object_ , _name_ , _/_)[¶](https://docs.python.org/3/library/functions.html#delattr "Link to this definition")

This is a relative of [`setattr()`](https://docs.python.org/3/library/functions.html#setattr "setattr"). The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, `delattr(x, 'foobar')` is equivalent to `del x.foobar`. _name_ need not be a Python identifier (see `setattr()`).

_class_ dict(_** kwargs_)


_class_ dict(_mapping_ , _/_ , _** kwargs_)


_class_ dict(_iterable_ , _/_ , _** kwargs_)

Create a new dictionary. The `dict` object is the dictionary class. See `dict` and [Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#typesmapping) for documentation about this class.
For other containers see the built-in [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), and [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") classes, as well as the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes") module.

dir()[¶](https://docs.python.org/3/library/functions.html#dir "Link to this definition")


dir(_object_ , _/_)

Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.
If the object has a method named [`__dir__()`](https://docs.python.org/3/reference/datamodel.html#object.__dir__ "object.__dir__"), this method will be called and must return the list of attributes. This allows objects that implement a custom [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__") or [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__") function to customize the way `dir()` reports their attributes.
If the object does not provide [`__dir__()`](https://docs.python.org/3/reference/datamodel.html#object.__dir__ "object.__dir__"), the function tries its best to gather information from the object’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") attribute, if defined, and from its type object. The resulting list is not necessarily complete and may be inaccurate when the object has a custom [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__").
The default `dir()` mechanism behaves differently with different types of objects, as it attempts to produce the most relevant, rather than complete, information:
  * If the object is a module object, the list contains the names of the module’s attributes.
  * If the object is a type or class object, the list contains the names of its attributes, and recursively of the attributes of its bases.
  * Otherwise, the list contains the object’s attributes’ names, the names of its class’s attributes, and recursively of the attributes of its class’s base classes.


The resulting list is sorted alphabetically. For example:
Copy```
>>> import struct
>>> dir()   # show the names in the module namespace
['__builtins__', '__name__', 'struct']
>>> dir(struct)   # show the names in the struct module
['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
 '__initializing__', '__loader__', '__name__', '__package__',
 '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']
>>> class Shape:
...     def __dir__(self):
...         return ['area', 'perimeter', 'location']
...
>>> s = Shape()
>>> dir(s)
['area', 'location', 'perimeter']

```

Note
Because `dir()` is supplied primarily as a convenience for use at an interactive prompt, it tries to supply an interesting set of names more than it tries to supply a rigorously or consistently defined set of names, and its detailed behavior may change across releases. For example, metaclass attributes are not in the result list when the argument is a class.

divmod(_a_ , _b_ , _/_)[¶](https://docs.python.org/3/library/functions.html#divmod "Link to this definition")

Take two (non-complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division. With mixed operand types, the rules for binary arithmetic operators apply. For integers, the result is the same as `(a // b, a % b)`. For floating-point numbers the result is `(q, a % b)`, where _q_ is usually `math.floor(a / b)` but may be 1 less than that. In any case `q * b + a % b` is very close to _a_ , if `a % b` is non-zero it has the same sign as _b_ , and `0 <= abs(a % b) < abs(b)`.

enumerate(_iterable_ , _start =0_)[¶](https://docs.python.org/3/library/functions.html#enumerate "Link to this definition")

Return an enumerate object. _iterable_ must be a sequence, an [iterator](https://docs.python.org/3/glossary.html#term-iterator), or some other object which supports iteration. The [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") method of the iterator returned by `enumerate()` returns a tuple containing a count (from _start_ which defaults to 0) and the values obtained from iterating over _iterable_.
Copy```
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

```

Equivalent to:
Copy```
def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1

```


eval(_source_ , _/_ , _globals =None_, _locals =None_)[¶](https://docs.python.org/3/library/functions.html#eval "Link to this definition")


Parameters:

  * **source** ([`str`](https://docs.python.org/3/library/stdtypes.html#str "str") | [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)) – A Python expression.
  * **globals** ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") | `None`) – The global namespace (default: `None`).
  * **locals** ([mapping](https://docs.python.org/3/glossary.html#term-mapping) | `None`) – The local namespace (default: `None`).



Returns:

The result of the evaluated expression.

Raises:

Syntax errors are reported as exceptions.
Warning
This function executes arbitrary code. Calling it with user-supplied input may lead to security vulnerabilities.
The _source_ argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the _globals_ and _locals_ mappings as global and local namespace. If the _globals_ dictionary is present and does not contain a value for the key `__builtins__`, a reference to the dictionary of the built-in module [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") is inserted under that key before _source_ is parsed. That way you can control what builtins are available to the executed code by inserting your own `__builtins__` dictionary into _globals_ before passing it to `eval()`. If the _locals_ mapping is omitted it defaults to the _globals_ dictionary. If both mappings are omitted, the source is executed with the _globals_ and _locals_ in the environment where `eval()` is called. Note, _eval()_ will only have access to the [nested scopes](https://docs.python.org/3/glossary.html#term-nested-scope) (non-locals) in the enclosing environment if they are already referenced in the scope that is calling `eval()` (e.g. via a [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) statement).
Example:
Copy```
>>> x = 1
>>> eval('x+1')
2

```

This function can also be used to execute arbitrary code objects (such as those created by [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile")). In this case, pass a code object instead of a string. If the code object has been compiled with `'exec'` as the _mode_ argument, `eval()`'s return value will be `None`.
Hints: dynamic execution of statements is supported by the [`exec()`](https://docs.python.org/3/library/functions.html#exec "exec") function. The [`globals()`](https://docs.python.org/3/library/functions.html#globals "globals") and [`locals()`](https://docs.python.org/3/library/functions.html#locals "locals") functions return the current global and local dictionary, respectively, which may be useful to pass around for use by `eval()` or `exec()`.
If the given source is a string, then leading and trailing spaces and tabs are stripped.
See [`ast.literal_eval()`](https://docs.python.org/3/library/ast.html#ast.literal_eval "ast.literal_eval") for a function that can safely evaluate strings with expressions containing only literals.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `exec` with the code object as the argument. Code compilation events may also be raised.
Changed in version 3.13: The _globals_ and _locals_ arguments can now be passed as keywords.
Changed in version 3.13: The semantics of the default _locals_ namespace have been adjusted as described for the [`locals()`](https://docs.python.org/3/library/functions.html#locals "locals") builtin.

exec(_source_ , _/_ , _globals =None_, _locals =None_, _*_ , _closure =None_)[¶](https://docs.python.org/3/library/functions.html#exec "Link to this definition")

Warning
This function executes arbitrary code. Calling it with user-supplied input may lead to security vulnerabilities.
This function supports dynamic execution of Python code. _source_ must be either a string or a code object. If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). [[1]](https://docs.python.org/3/library/functions.html#id2) If it is a code object, it is simply executed. In all cases, the code that’s executed is expected to be valid as file input (see the section [File input](https://docs.python.org/3/reference/toplevel_components.html#file-input) in the Reference Manual). Be aware that the [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal), [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield), and [`return`](https://docs.python.org/3/reference/simple_stmts.html#return) statements may not be used outside of function definitions even within the context of code passed to the `exec()` function. The return value is `None`.
In all cases, if the optional parts are omitted, the code is executed in the current scope. If only _globals_ is provided, it must be a dictionary (and not a subclass of dictionary), which will be used for both the global and the local variables. If _globals_ and _locals_ are given, they are used for the global and local variables, respectively. If provided, _locals_ can be any mapping object. Remember that at the module level, globals and locals are the same dictionary.
Note
When `exec` gets two separate objects as _globals_ and _locals_ , the code will be executed as if it were embedded in a class definition. This means functions and classes defined in the executed code will not be able to access variables assigned at the top level (as the “top level” variables are treated as class variables in a class definition).
If the _globals_ dictionary does not contain a value for the key `__builtins__`, a reference to the dictionary of the built-in module [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") is inserted under that key. That way you can control what builtins are available to the executed code by inserting your own `__builtins__` dictionary into _globals_ before passing it to `exec()`.
The _closure_ argument specifies a closure–a tuple of cellvars. It’s only valid when the _object_ is a code object containing [free (closure) variables](https://docs.python.org/3/glossary.html#term-closure-variable). The length of the tuple must exactly match the length of the code object’s [`co_freevars`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_freevars "codeobject.co_freevars") attribute.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `exec` with the code object as the argument. Code compilation events may also be raised.
Note
The built-in functions [`globals()`](https://docs.python.org/3/library/functions.html#globals "globals") and [`locals()`](https://docs.python.org/3/library/functions.html#locals "locals") return the current global and local namespace, respectively, which may be useful to pass around for use as the second and third argument to `exec()`.
Note
The default _locals_ act as described for function [`locals()`](https://docs.python.org/3/library/functions.html#locals "locals") below. Pass an explicit _locals_ dictionary if you need to see effects of the code on _locals_ after function `exec()` returns.
Changed in version 3.11: Added the _closure_ parameter.
Changed in version 3.13: The _globals_ and _locals_ arguments can now be passed as keywords.
Changed in version 3.13: The semantics of the default _locals_ namespace have been adjusted as described for the [`locals()`](https://docs.python.org/3/library/functions.html#locals "locals") builtin.

filter(_function_ , _iterable_ , _/_)[¶](https://docs.python.org/3/library/functions.html#filter "Link to this definition")

Construct an iterator from those elements of _iterable_ for which _function_ is true. _iterable_ may be either a sequence, a container which supports iteration, or an iterator. If _function_ is `None`, the identity function is assumed, that is, all elements of _iterable_ that are false are removed.
Note that `filter(function, iterable)` is equivalent to the generator expression `(item for item in iterable if function(item))` if function is not `None` and `(item for item in iterable if item)` if function is `None`.
See [`itertools.filterfalse()`](https://docs.python.org/3/library/itertools.html#itertools.filterfalse "itertools.filterfalse") for the complementary function that returns elements of _iterable_ for which _function_ is false.

_class_ float(_number =0.0_, _/_)[¶](https://docs.python.org/3/library/functions.html#float "Link to this definition")


_class_ float(_string_ , _/_)

Return a floating-point number constructed from a number or a string.
Examples:
Copy```
>>> float('+1.23')
1.23
>>> float('   -12345\n')
-12345.0
>>> float('1e-003')
0.001
>>> float('+1E6')
1000000.0
>>> float('-Infinity')
-inf

```

If the argument is a string, it should contain a decimal number, optionally preceded by a sign, and optionally embedded in whitespace. The optional sign may be `'+'` or `'-'`; a `'+'` sign has no effect on the value produced. The argument may also be a string representing a NaN (not-a-number), or positive or negative infinity. More precisely, the input must conform to the [`floatvalue`](https://docs.python.org/3/library/functions.html#grammar-token-float-floatvalue) production rule in the following grammar, after leading and trailing whitespace characters are removed:
```
**sign**:          "+" | "-"
**infinity**:      "Infinity" | "inf"
**nan**:           "nan"
**digit**:         <a Unicode decimal digit, i.e. characters in Unicode general category Nd>
**digitpart**:     [digit](https://docs.python.org/3/library/functions.html#grammar-token-float-digit) (["_"] [digit](https://docs.python.org/3/library/functions.html#grammar-token-float-digit))*
**number**:        [[digitpart](https://docs.python.org/3/library/functions.html#grammar-token-float-digitpart)] "." [digitpart](https://docs.python.org/3/library/functions.html#grammar-token-float-digitpart) | [digitpart](https://docs.python.org/3/library/functions.html#grammar-token-float-digitpart) ["."]
**exponent**:      ("e" | "E") [[sign](https://docs.python.org/3/library/functions.html#grammar-token-float-sign)] [digitpart](https://docs.python.org/3/library/functions.html#grammar-token-float-digitpart)
**floatnumber**:   [number](https://docs.python.org/3/library/functions.html#grammar-token-float-number) [[exponent](https://docs.python.org/3/library/functions.html#grammar-token-float-exponent)]
**absfloatvalue**: [floatnumber](https://docs.python.org/3/library/functions.html#grammar-token-float-floatnumber) | [infinity](https://docs.python.org/3/library/functions.html#grammar-token-float-infinity) | [nan](https://docs.python.org/3/library/functions.html#grammar-token-float-nan)
**floatvalue**:    [[sign](https://docs.python.org/3/library/functions.html#grammar-token-float-sign)] [absfloatvalue](https://docs.python.org/3/library/functions.html#grammar-token-float-absfloatvalue)

```

Case is not significant, so, for example, “inf”, “Inf”, “INFINITY”, and “iNfINity” are all acceptable spellings for positive infinity.
Otherwise, if the argument is an integer or a floating-point number, a floating-point number with the same value (within Python’s floating-point precision) is returned. If the argument is outside the range of a Python float, an [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") will be raised.
For a general Python object `x`, `float(x)` delegates to `x.__float__()`. If [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__") is not defined then it falls back to [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__").
See also [`float.from_number()`](https://docs.python.org/3/library/stdtypes.html#float.from_number "float.from_number") which only accepts a numeric argument.
If no argument is given, `0.0` is returned.
The float type is described in [Numeric Types — int, float, complex](https://docs.python.org/3/library/stdtypes.html#typesnumeric).
Changed in version 3.6: Grouping digits with underscores as in code literals is allowed.
Changed in version 3.7: The parameter is now positional-only.
Changed in version 3.8: Falls back to [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") if [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__") is not defined.

format(_value_ , _format_spec =''_, _/_)[¶](https://docs.python.org/3/library/functions.html#format "Link to this definition")

Convert a _value_ to a “formatted” representation, as controlled by _format_spec_. The interpretation of _format_spec_ will depend on the type of the _value_ argument; however, there is a standard formatting syntax that is used by most built-in types: [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec).
The default _format_spec_ is an empty string which usually gives the same effect as calling [`str(value)`](https://docs.python.org/3/library/stdtypes.html#str "str").
A call to `format(value, format_spec)` is translated to `type(value).__format__(value, format_spec)` which bypasses the instance dictionary when searching for the value’s [`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__ "object.__format__") method. A [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception is raised if the method search reaches [`object`](https://docs.python.org/3/library/functions.html#object "object") and the _format_spec_ is non-empty, or if either the _format_spec_ or the return value are not strings.
Changed in version 3.4: `object().__format__(format_spec)` raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if _format_spec_ is not an empty string.

_class_ frozenset(_iterable =()_, _/_)

Return a new `frozenset` object, optionally with elements taken from _iterable_. `frozenset` is a built-in class. See `frozenset` and [Set Types — set, frozenset](https://docs.python.org/3/library/stdtypes.html#types-set) for documentation about this class.
For other containers see the built-in [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"), and [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") classes, as well as the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes") module.

getattr(_object_ , _name_ , _/_)[¶](https://docs.python.org/3/library/functions.html#getattr "Link to this definition")


getattr(_object_ , _name_ , _default_ , _/_)

Return the value of the named attribute of _object_. _name_ must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, `getattr(x, 'foobar')` is equivalent to `x.foobar`. If the named attribute does not exist, _default_ is returned if provided, otherwise [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") is raised. _name_ need not be a Python identifier (see [`setattr()`](https://docs.python.org/3/library/functions.html#setattr "setattr")).
Note
Since [private name mangling](https://docs.python.org/3/reference/expressions.html#private-name-mangling) happens at compilation time, one must manually mangle a private attribute’s (attributes with two leading underscores) name in order to retrieve it with `getattr()`.

globals()[¶](https://docs.python.org/3/library/functions.html#globals "Link to this definition")

Return the dictionary implementing the current module namespace. For code within functions, this is set when the function is defined and remains the same regardless of where the function is called.

hasattr(_object_ , _name_ , _/_)[¶](https://docs.python.org/3/library/functions.html#hasattr "Link to this definition")

The arguments are an object and a string. The result is `True` if the string is the name of one of the object’s attributes, `False` if not. (This is implemented by calling `getattr(object, name)` and seeing whether it raises an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") or not.)

hash(_object_ , _/_)[¶](https://docs.python.org/3/library/functions.html#hash "Link to this definition")

Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).
