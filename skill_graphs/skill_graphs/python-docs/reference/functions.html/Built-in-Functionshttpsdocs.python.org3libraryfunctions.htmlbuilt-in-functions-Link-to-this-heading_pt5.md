Copy```
class C:
    @staticmethod
    def f(arg1, arg2, argN): ...

```

The `@staticmethod` form is a function [decorator](https://docs.python.org/3/glossary.html#term-decorator) – see [Function definitions](https://docs.python.org/3/reference/compound_stmts.html#function) for details.
A static method can be called either on the class (such as `C.f()`) or on an instance (such as `C().f()`). Moreover, the static method [descriptor](https://docs.python.org/3/glossary.html#term-descriptor) is also callable, so it can be used in the class definition (such as `f()`).
Static methods in Python are similar to those found in Java or C++. Also, see [`classmethod()`](https://docs.python.org/3/library/functions.html#classmethod "classmethod") for a variant that is useful for creating alternate class constructors.
Like all decorators, it is also possible to call `staticmethod` as a regular function and do something with its result. This is needed in some cases where you need a reference to a function from a class body and you want to avoid the automatic transformation to instance method. For these cases, use this idiom:
Copy```
def regular_function():
    ...

class C:
    method = staticmethod(regular_function)

```

For more information on static methods, see [The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#types).
Changed in version 3.10: Static methods now inherit the method attributes ([`__module__`](https://docs.python.org/3/reference/datamodel.html#function.__module__ "function.__module__"), [`__name__`](https://docs.python.org/3/reference/datamodel.html#function.__name__ "function.__name__"), [`__qualname__`](https://docs.python.org/3/reference/datamodel.html#function.__qualname__ "function.__qualname__"), [`__doc__`](https://docs.python.org/3/reference/datamodel.html#function.__doc__ "function.__doc__") and [`__annotations__`](https://docs.python.org/3/reference/datamodel.html#function.__annotations__ "function.__annotations__")), have a new `__wrapped__` attribute, and are now callable as regular functions.

_class_ str(_*_ , _encoding ='utf-8'_, _errors ='strict'_)


_class_ str(_object_)


_class_ str(_object_ , _encoding_ , _errors ='strict'_)


_class_ str(_object_ , _*_ , _errors_)

Return a `str` version of _object_. See [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") for details.
`str` is the built-in string [class](https://docs.python.org/3/glossary.html#term-class). For general information about strings, see [Text Sequence Type — str](https://docs.python.org/3/library/stdtypes.html#textseq).

sum(_iterable_ , _/_ , _start =0_)[¶](https://docs.python.org/3/library/functions.html#sum "Link to this definition")

Sums _start_ and the items of an _iterable_ from left to right and returns the total. The _iterable_ ’s items are normally numbers, and the start value is not allowed to be a string.
For some use cases, there are good alternatives to `sum()`. The preferred, fast way to concatenate a sequence of strings is by calling `''.join(sequence)`. To add floating-point values with extended precision, see [`math.fsum()`](https://docs.python.org/3/library/math.html#math.fsum "math.fsum"). To concatenate a series of iterables, consider using [`itertools.chain()`](https://docs.python.org/3/library/itertools.html#itertools.chain "itertools.chain").
Changed in version 3.8: The _start_ parameter can be specified as a keyword argument.
Changed in version 3.12: Summation of floats switched to an algorithm that gives higher accuracy and better commutativity on most builds.
Changed in version 3.14: Added specialization for summation of complexes, using same algorithm as for summation of floats.

_class_ super[¶](https://docs.python.org/3/library/functions.html#super "Link to this definition")


_class_ super(_type_ , _object_or_type =None_, _/_)

Return a proxy object that delegates method calls to a parent or sibling class of _type_. This is useful for accessing inherited methods that have been overridden in a class.
The _object_or_type_ determines the [method resolution order](https://docs.python.org/3/glossary.html#term-method-resolution-order) to be searched. The search starts from the class right after the _type_.
For example, if [`__mro__`](https://docs.python.org/3/reference/datamodel.html#type.__mro__ "type.__mro__") of _object_or_type_ is `D -> B -> C -> A -> object` and the value of _type_ is `B`, then [`super()`](https://docs.python.org/3/library/functions.html#super "super") searches `C -> A -> object`.
The [`__mro__`](https://docs.python.org/3/reference/datamodel.html#type.__mro__ "type.__mro__") attribute of the class corresponding to _object_or_type_ lists the method resolution search order used by both [`getattr()`](https://docs.python.org/3/library/functions.html#getattr "getattr") and [`super()`](https://docs.python.org/3/library/functions.html#super "super"). The attribute is dynamic and can change whenever the inheritance hierarchy is updated.
If the second argument is omitted, the super object returned is unbound. If the second argument is an object, `isinstance(obj, type)` must be true. If the second argument is a type, `issubclass(type2, type)` must be true (this is useful for classmethods).
When called directly within an ordinary method of a class, both arguments may be omitted (“zero-argument `super()`”). In this case, _type_ will be the enclosing class, and _obj_ will be the first argument of the immediately enclosing function (typically `self`). (This means that zero-argument `super()` will not work as expected within nested functions, including generator expressions, which implicitly create nested functions.)
There are two typical use cases for _super_. In a class hierarchy with single inheritance, _super_ can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of _super_ in other programming languages.
The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This use case is unique to Python and is not found in statically compiled languages or languages that only support single inheritance. This makes it possible to implement “diamond diagrams” where multiple base classes implement the same method. Good design dictates that such implementations have the same calling signature in every case (because the order of calls is determined at runtime, because that order adapts to changes in the class hierarchy, and because that order can include sibling classes that are unknown prior to runtime).
For both use cases, a typical superclass call looks like this:
Copy```
class C(B):
    def method(self, arg):
        super().method(arg)    # This does the same thing as:
                               # super(C, self).method(arg)

```

In addition to method lookups, [`super()`](https://docs.python.org/3/library/functions.html#super "super") also works for attribute lookups. One possible use case for this is calling [descriptors](https://docs.python.org/3/glossary.html#term-descriptor) in a parent or sibling class.
Note that [`super()`](https://docs.python.org/3/library/functions.html#super "super") is implemented as part of the binding process for explicit dotted attribute lookups such as `super().__getitem__(name)`. It does so by implementing its own [`__getattribute__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattribute__ "object.__getattribute__") method for searching classes in a predictable order that supports cooperative multiple inheritance. Accordingly, `super()` is undefined for implicit lookups using statements or operators such as `super()[name]`.
Also note that, aside from the zero argument form, [`super()`](https://docs.python.org/3/library/functions.html#super "super") is not limited to use inside methods. The two argument form specifies the arguments exactly and makes the appropriate references. The zero argument form only works inside a class definition, as the compiler fills in the necessary details to correctly retrieve the class being defined, as well as accessing the current instance for ordinary methods.
For practical suggestions on how to design cooperative classes using [`super()`](https://docs.python.org/3/library/functions.html#super "super"), see
Changed in version 3.14: `super` objects are now [`pickleable`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and [`copyable`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.").

_class_ tuple(_iterable =()_, _/_)

Rather than being a function, `tuple` is actually an immutable sequence type, as documented in [Tuples](https://docs.python.org/3/library/stdtypes.html#typesseq-tuple) and [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#typesseq).

_class_ type(_object_ , _/_)[¶](https://docs.python.org/3/library/functions.html#type "Link to this definition")


_class_ type(_name_ , _bases_ , _dict_ , _/_ , _** kwargs_)

With one argument, return the type of an _object_. The return value is a type object and generally the same object as returned by [`object.__class__`](https://docs.python.org/3/reference/datamodel.html#object.__class__ "object.__class__").
The [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance") built-in function is recommended for testing the type of an object, because it takes subclasses into account.
With three arguments, return a new type object. This is essentially a dynamic form of the [`class`](https://docs.python.org/3/reference/compound_stmts.html#class) statement. The _name_ string is the class name and becomes the [`__name__`](https://docs.python.org/3/reference/datamodel.html#type.__name__ "type.__name__") attribute. The _bases_ tuple contains the base classes and becomes the [`__bases__`](https://docs.python.org/3/reference/datamodel.html#type.__bases__ "type.__bases__") attribute; if empty, [`object`](https://docs.python.org/3/library/functions.html#object "object"), the ultimate base of all classes, is added. The _dict_ dictionary contains attribute and method definitions for the class body; it may be copied or wrapped before becoming the [`__dict__`](https://docs.python.org/3/reference/datamodel.html#type.__dict__ "type.__dict__") attribute. The following two statements create identical `type` objects:
Copy```
>>> class X:
...     a = 1
...
>>> X = type('X', (), dict(a=1))

```

See also:
  * [Documentation on attributes and methods on classes](https://docs.python.org/3/reference/datamodel.html#class-attrs-and-methods).
  * [Type Objects](https://docs.python.org/3/library/stdtypes.html#bltin-type-objects)


Keyword arguments provided to the three argument form are passed to the appropriate metaclass machinery (usually [`__init_subclass__()`](https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__ "object.__init_subclass__")) in the same way that keywords in a class definition (besides _metaclass_) would.
See also [Customizing class creation](https://docs.python.org/3/reference/datamodel.html#class-customization).
Changed in version 3.6: Subclasses of `type` which don’t override `type.__new__` may no longer use the one-argument form to get the type of an object.

vars()[¶](https://docs.python.org/3/library/functions.html#vars "Link to this definition")


vars(_object_ , _/_)

Return the [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") attribute for a module, class, instance, or any other object with a `__dict__` attribute.
Objects such as modules and instances have an updateable [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") attribute; however, other objects may have write restrictions on their `__dict__` attributes (for example, classes use a [`types.MappingProxyType`](https://docs.python.org/3/library/types.html#types.MappingProxyType "types.MappingProxyType") to prevent direct dictionary updates).
Without an argument, `vars()` acts like [`locals()`](https://docs.python.org/3/library/functions.html#locals "locals").
A [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception is raised if an object is specified but it doesn’t have a [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__") attribute (for example, if its class defines the [`__slots__`](https://docs.python.org/3/reference/datamodel.html#object.__slots__ "object.__slots__") attribute).
Changed in version 3.13: The result of calling this function without an argument has been updated as described for the [`locals()`](https://docs.python.org/3/library/functions.html#locals "locals") builtin.

zip(_* iterables_, _strict =False_)[¶](https://docs.python.org/3/library/functions.html#zip "Link to this definition")

Iterate over several iterables in parallel, producing tuples with an item from each one.
Example:
Copy```
>>> for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
...     print(item)
...
(1, 'sugar')
(2, 'spice')
(3, 'everything nice')

```

More formally: `zip()` returns an iterator of tuples, where the _i_ -th tuple contains the _i_ -th element from each of the argument iterables.
Another way to think of `zip()` is that it turns rows into columns, and columns into rows. This is similar to
`zip()` is lazy: The elements won’t be processed until the iterable is iterated on, e.g. by a `for` loop or by wrapping in a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list").
One thing to consider is that the iterables passed to `zip()` could have different lengths; sometimes by design, and sometimes because of a bug in the code that prepared these iterables. Python offers three different approaches to dealing with this issue:
  * By default, `zip()` stops when the shortest iterable is exhausted. It will ignore the remaining items in the longer iterables, cutting off the result to the length of the shortest iterable:
Copy```
>>> list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
[(0, 'fee'), (1, 'fi'), (2, 'fo')]

```

  * `zip()` is often used in cases where the iterables are assumed to be of equal length. In such cases, it’s recommended to use the `strict=True` option. Its output is the same as regular `zip()`:
Copy```
>>> list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True))
[('a', 1), ('b', 2), ('c', 3)]

```

Unlike the default behavior, it raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if one iterable is exhausted before the others:
Copy```
>>> for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):
...     print(item)
...
(0, 'fee')
(1, 'fi')
(2, 'fo')
Traceback (most recent call last):
  ...
ValueError: zip() argument 2 is longer than argument 1

```

Without the `strict=True` argument, any bug that results in iterables of different lengths will be silenced, possibly manifesting as a hard-to-find bug in another part of the program.
  * Shorter iterables can be padded with a constant value to make all the iterables have the same length. This is done by [`itertools.zip_longest()`](https://docs.python.org/3/library/itertools.html#itertools.zip_longest "itertools.zip_longest").


Edge cases: With a single iterable argument, `zip()` returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.
Tips and tricks:
  * The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering a data series into n-length groups using `zip(*[iter(s)]*n, strict=True)`. This repeats the _same_ iterator `n` times so that each output tuple has the result of `n` calls to the iterator. This has the effect of dividing the input into n-length chunks.
  * `zip()` in conjunction with the `*` operator can be used to unzip a list:
Copy```
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> list(zip(x, y))
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zip(x, y))
>>> x == list(x2) and y == list(y2)
True

```



Changed in version 3.10: Added the `strict` argument.

__import__(_name_ , _globals =None_, _locals =None_, _fromlist =()_, _level =0_)[¶](https://docs.python.org/3/library/functions.html#import__ "Link to this definition")

Note
This is an advanced function that is not needed in everyday Python programming, unlike [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module").
This function is invoked by the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement. It can be replaced (by importing the [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") module and assigning to `builtins.__import__`) in order to change semantics of the `import` statement, but doing so is **strongly** discouraged as it is usually simpler to use import hooks (see [**PEP 302**](https://peps.python.org/pep-0302/)) to attain the same goals and does not cause issues with code which assumes the default import implementation is in use. Direct use of `__import__()` is also discouraged in favor of [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module").
The function imports the module _name_ , potentially using the given _globals_ and _locals_ to determine how to interpret the name in a package context. The _fromlist_ gives the names of objects or submodules that should be imported from the module given by _name_. The standard implementation does not use its _locals_ argument at all and uses its _globals_ only to determine the package context of the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement.
_level_ specifies whether to use absolute or relative imports. `0` (the default) means only perform absolute imports. Positive values for _level_ indicate the number of parent directories to search relative to the directory of the module calling `__import__()` (see [**PEP 328**](https://peps.python.org/pep-0328/) for the details).
When the _name_ variable is of the form `package.module`, normally, the top-level package (the name up till the first dot) is returned, _not_ the module named by _name_. However, when a non-empty _fromlist_ argument is given, the module named by _name_ is returned.
For example, the statement `import spam` results in bytecode resembling the following code:
Copy```
spam = __import__('spam', globals(), locals(), [], 0)

```

The statement `import spam.ham` results in this call:
Copy```
spam = __import__('spam.ham', globals(), locals(), [], 0)

```

Note how `__import__()` returns the toplevel module here because this is the object that is bound to a name by the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement.
On the other hand, the statement `from spam.ham import eggs, sausage as saus` results in
Copy```
_temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
eggs = _temp.eggs
saus = _temp.sausage

```

Here, the `spam.ham` module is returned from `__import__()`. From this object, the names to import are retrieved and assigned to their respective names.
If you simply want to import a module (potentially within a package) by name, use [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module").
Changed in version 3.3: Negative values for _level_ are no longer supported (which also changes the default value to 0).
Changed in version 3.9: When the command line options [`-E`](https://docs.python.org/3/using/cmdline.html#cmdoption-E) or [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I) are being used, the environment variable [`PYTHONCASEOK`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONCASEOK) is now ignored.
Footnotes
[[1](https://docs.python.org/3/library/functions.html#id1)]
Note that the parser only accepts the Unix-style end of line convention. If you are reading the code from a file, make sure to use newline conversion mode to convert Windows or Mac-style newlines.
#### Previous topic
[Introduction](https://docs.python.org/3/library/intro.html "previous chapter")
#### Next topic
[Built-in Constants](https://docs.python.org/3/library/constants.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Built-in+Functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffunctions.html&pagesource=library%2Ffunctions.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/constants.html "Built-in Constants") |
  * [previous](https://docs.python.org/3/library/intro.html "Introduction") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Built-in Functions](https://docs.python.org/3/library/functions.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[/]: Positional-only parameter separator (PEP 570)
  *[*]: Keyword-only parameters separator (PEP 3102)
