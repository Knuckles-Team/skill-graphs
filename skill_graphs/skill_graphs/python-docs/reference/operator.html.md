[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`operator` — Standard operators as functions](https://docs.python.org/3/library/operator.html)
    * [Mapping Operators to Functions](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions)
    * [In-place Operators](https://docs.python.org/3/library/operator.html#in-place-operators)


#### Previous topic
[`functools` — Higher-order functions and operations on callable objects](https://docs.python.org/3/library/functools.html "previous chapter")
#### Next topic
[File and Directory Access](https://docs.python.org/3/library/filesys.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=operator+%E2%80%94+Standard+operators+as+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Foperator.html&pagesource=library%2Foperator.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/filesys.html "File and Directory Access") |
  * [previous](https://docs.python.org/3/library/functools.html "functools — Higher-order functions and operations on callable objects") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Functional Programming Modules](https://docs.python.org/3/library/functional.html) »
  * [`operator` — Standard operators as functions](https://docs.python.org/3/library/operator.html)
  * |
  * Theme  Auto Light Dark |


#  `operator` — Standard operators as functions[¶](https://docs.python.org/3/library/operator.html#module-operator "Link to this heading")
**Source code:**
* * *
The `operator` module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, `operator.add(x, y)` is equivalent to the expression `x+y`. Many function names are those used for special methods, without the double underscores. For backward compatibility, many of these have a variant with the double underscores kept. The variants without the double underscores are preferred for clarity.
The functions fall into categories that perform object comparisons, logical operations, mathematical operations and sequence operations.
The object comparison functions are useful for all objects, and are named after the rich comparison operators they support:

operator.lt(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.lt "Link to this definition")


operator.le(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.le "Link to this definition")


operator.eq(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.eq "Link to this definition")


operator.ne(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.ne "Link to this definition")


operator.ge(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.ge "Link to this definition")


operator.gt(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.gt "Link to this definition")


operator.__lt__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__lt__ "Link to this definition")


operator.__le__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__le__ "Link to this definition")


operator.__eq__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__eq__ "Link to this definition")


operator.__ne__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__ne__ "Link to this definition")


operator.__ge__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__ge__ "Link to this definition")


operator.__gt__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__gt__ "Link to this definition")

Perform “rich comparisons” between _a_ and _b_. Specifically, `lt(a, b)` is equivalent to `a < b`, `le(a, b)` is equivalent to `a <= b`, `eq(a, b)` is equivalent to `a == b`, `ne(a, b)` is equivalent to `a != b`, `gt(a, b)` is equivalent to `a > b` and `ge(a, b)` is equivalent to `a >= b`. Note that these functions can return any value, which may or may not be interpretable as a Boolean value. See [Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons) for more information about rich comparisons.
The logical operations are also generally applicable to all objects, and support truth tests, identity tests, and boolean operations:

operator.not_(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.not_ "Link to this definition")


operator.__not__(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.__not__ "Link to this definition")

Return the outcome of [`not`](https://docs.python.org/3/reference/expressions.html#not) _obj_. (Note that there is no `__not__()` method for object instances; only the interpreter core defines this operation. The result is affected by the [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__ "object.__bool__") and [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__") methods.)

operator.truth(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.truth "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if _obj_ is true, and [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise. This is equivalent to using the [`bool`](https://docs.python.org/3/library/functions.html#bool "bool") constructor.

operator.is_(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.is_ "Link to this definition")

Return `a is b`. Tests object identity.

operator.is_not(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.is_not "Link to this definition")

Return `a is not b`. Tests object identity.

operator.is_none(_a_)[¶](https://docs.python.org/3/library/operator.html#operator.is_none "Link to this definition")

Return `a is None`. Tests object identity.
Added in version 3.14.

operator.is_not_none(_a_)[¶](https://docs.python.org/3/library/operator.html#operator.is_not_none "Link to this definition")

Return `a is not None`. Tests object identity.
Added in version 3.14.
The mathematical and bitwise operations are the most numerous:

operator.abs(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.abs "Link to this definition")


operator.__abs__(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.__abs__ "Link to this definition")

Return the absolute value of _obj_.

operator.add(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.add "Link to this definition")


operator.__add__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__add__ "Link to this definition")

Return `a + b`, for _a_ and _b_ numbers.

operator.and_(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.and_ "Link to this definition")


operator.__and__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__and__ "Link to this definition")

Return the bitwise and of _a_ and _b_.

operator.floordiv(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.floordiv "Link to this definition")


operator.__floordiv__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__floordiv__ "Link to this definition")

Return `a // b`.

operator.index(_a_)[¶](https://docs.python.org/3/library/operator.html#operator.index "Link to this definition")


operator.__index__(_a_)[¶](https://docs.python.org/3/library/operator.html#operator.__index__ "Link to this definition")

Return _a_ converted to an integer. Equivalent to `a.__index__()`.
Changed in version 3.10: The result always has exact type [`int`](https://docs.python.org/3/library/functions.html#int "int"). Previously, the result could have been an instance of a subclass of `int`.

operator.inv(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.inv "Link to this definition")


operator.invert(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.invert "Link to this definition")


operator.__inv__(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.__inv__ "Link to this definition")


operator.__invert__(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.__invert__ "Link to this definition")

Return the bitwise inverse of the number _obj_. This is equivalent to `~obj`.

operator.lshift(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.lshift "Link to this definition")


operator.__lshift__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__lshift__ "Link to this definition")

Return _a_ shifted left by _b_.

operator.mod(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.mod "Link to this definition")


operator.__mod__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__mod__ "Link to this definition")

Return `a % b`.

operator.mul(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.mul "Link to this definition")


operator.__mul__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__mul__ "Link to this definition")

Return `a * b`, for _a_ and _b_ numbers.

operator.matmul(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.matmul "Link to this definition")


operator.__matmul__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__matmul__ "Link to this definition")

Return `a @ b`.
Added in version 3.5.

operator.neg(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.neg "Link to this definition")


operator.__neg__(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.__neg__ "Link to this definition")

Return _obj_ negated (`-obj`).

operator.or_(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.or_ "Link to this definition")


operator.__or__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__or__ "Link to this definition")

Return the bitwise or of _a_ and _b_.

operator.pos(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.pos "Link to this definition")


operator.__pos__(_obj_)[¶](https://docs.python.org/3/library/operator.html#operator.__pos__ "Link to this definition")

Return _obj_ positive (`+obj`).

operator.pow(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.pow "Link to this definition")


operator.__pow__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__pow__ "Link to this definition")

Return `a ** b`, for _a_ and _b_ numbers.

operator.rshift(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.rshift "Link to this definition")


operator.__rshift__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__rshift__ "Link to this definition")

Return _a_ shifted right by _b_.

operator.sub(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.sub "Link to this definition")


operator.__sub__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__sub__ "Link to this definition")

Return `a - b`.

operator.truediv(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.truediv "Link to this definition")


operator.__truediv__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__truediv__ "Link to this definition")

Return `a / b` where 2/3 is .66 rather than 0. This is also known as “true” division.

operator.xor(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.xor "Link to this definition")


operator.__xor__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__xor__ "Link to this definition")

Return the bitwise exclusive or of _a_ and _b_.
Operations which work with sequences (some of them with mappings too) include:

operator.concat(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.concat "Link to this definition")


operator.__concat__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__concat__ "Link to this definition")

Return `a + b` for _a_ and _b_ sequences.

operator.contains(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.contains "Link to this definition")


operator.__contains__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__contains__ "Link to this definition")

Return the outcome of the test `b in a`. Note the reversed operands.

operator.countOf(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.countOf "Link to this definition")

Return the number of occurrences of _b_ in _a_.

operator.delitem(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.delitem "Link to this definition")


operator.__delitem__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__delitem__ "Link to this definition")

Remove the value of _a_ at index _b_.

operator.getitem(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.getitem "Link to this definition")


operator.__getitem__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__getitem__ "Link to this definition")

Return the value of _a_ at index _b_.

operator.indexOf(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.indexOf "Link to this definition")

Return the index of the first of occurrence of _b_ in _a_.

operator.setitem(_a_ , _b_ , _c_)[¶](https://docs.python.org/3/library/operator.html#operator.setitem "Link to this definition")


operator.__setitem__(_a_ , _b_ , _c_)[¶](https://docs.python.org/3/library/operator.html#operator.__setitem__ "Link to this definition")

Set the value of _a_ at index _b_ to _c_.

operator.length_hint(_obj_ , _default =0_)[¶](https://docs.python.org/3/library/operator.html#operator.length_hint "Link to this definition")

Return an estimated length for the object _obj_. First try to return its actual length, then an estimate using [`object.__length_hint__()`](https://docs.python.org/3/reference/datamodel.html#object.__length_hint__ "object.__length_hint__"), and finally return the default value.
Added in version 3.4.
The following operation works with callables:

operator.call(_obj_ , _/_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/operator.html#operator.call "Link to this definition")


operator.__call__(_obj_ , _/_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/operator.html#operator.__call__ "Link to this definition")

Return `obj(*args, **kwargs)`.
Added in version 3.11.
The `operator` module also defines tools for generalized attribute and item lookups. These are useful for making fast field extractors as arguments for [`map()`](https://docs.python.org/3/library/functions.html#map "map"), [`sorted()`](https://docs.python.org/3/library/functions.html#sorted "sorted"), [`itertools.groupby()`](https://docs.python.org/3/library/itertools.html#itertools.groupby "itertools.groupby"), or other functions that expect a function argument.

operator.attrgetter(_attr_)[¶](https://docs.python.org/3/library/operator.html#operator.attrgetter "Link to this definition")


operator.attrgetter(_* attrs_)

Return a callable object that fetches _attr_ from its operand. If more than one attribute is requested, returns a tuple of attributes. The attribute names can also contain dots. For example:
  * After `f = attrgetter('name')`, the call `f(b)` returns `b.name`.
  * After `f = attrgetter('name', 'date')`, the call `f(b)` returns `(b.name, b.date)`.
  * After `f = attrgetter('name.first', 'name.last')`, the call `f(b)` returns `(b.name.first, b.name.last)`.


Equivalent to:
Copy```
def attrgetter(*items):
    if any(not isinstance(item, str) for item in items):
        raise TypeError('attribute name must be a string')
    if len(items) == 1:
        attr = items[0]
        def g(obj):
            return resolve_attr(obj, attr)
    else:
        def g(obj):
            return tuple(resolve_attr(obj, attr) for attr in items)
    return g

def resolve_attr(obj, attr):
    for name in attr.split("."):
        obj = getattr(obj, name)
    return obj

```


operator.itemgetter(_item_)[¶](https://docs.python.org/3/library/operator.html#operator.itemgetter "Link to this definition")


operator.itemgetter(_* items_)

Return a callable object that fetches _item_ from its operand using the operand’s [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__") method. If multiple items are specified, returns a tuple of lookup values. For example:
  * After `f = itemgetter(2)`, the call `f(r)` returns `r[2]`.
  * After `g = itemgetter(2, 5, 3)`, the call `g(r)` returns `(r[2], r[5], r[3])`.


Equivalent to:
Copy```
def itemgetter(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g

```

The items can be any type accepted by the operand’s [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__") method. Dictionaries accept any [hashable](https://docs.python.org/3/glossary.html#term-hashable) value. Lists, tuples, and strings accept an index or a slice:
Copy```
>>> itemgetter(1)('ABCDEFG')
'B'
>>> itemgetter(1, 3, 5)('ABCDEFG')
('B', 'D', 'F')
>>> itemgetter(slice(2, None))('ABCDEFG')
'CDEFG'
>>> soldier = dict(rank='captain', name='dotterbart')
>>> itemgetter('rank')(soldier)
'captain'

```

Example of using `itemgetter()` to retrieve specific fields from a tuple record:
Copy```
>>> inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
>>> getcount = itemgetter(1)
>>> list(map(getcount, inventory))
[3, 2, 5, 1]
>>> sorted(inventory, key=getcount)
[('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]

```


operator.methodcaller(_name_ , _/_ , _* args_, _** kwargs_)[¶](https://docs.python.org/3/library/operator.html#operator.methodcaller "Link to this definition")

Return a callable object that calls the method _name_ on its operand. If additional arguments and/or keyword arguments are given, they will be given to the method as well. For example:
  * After `f = methodcaller('name')`, the call `f(b)` returns `b.name()`.
  * After `f = methodcaller('name', 'foo', bar=1)`, the call `f(b)` returns `b.name('foo', bar=1)`.


Equivalent to:
Copy```
def methodcaller(name, /, *args, **kwargs):
    def caller(obj):
        return getattr(obj, name)(*args, **kwargs)
    return caller

```

## Mapping Operators to Functions[¶](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions "Link to this heading")
This table shows how abstract operations correspond to operator symbols in the Python syntax and the functions in the `operator` module.
Operation | Syntax | Function
---|---|---
Addition | `a + b` | `add(a, b)`
Concatenation | `seq1 + seq2` | `concat(seq1, seq2)`
Containment Test | `obj in seq` | `contains(seq, obj)`
Division | `a / b` | `truediv(a, b)`
Division | `a // b` | `floordiv(a, b)`
Bitwise And | `a & b` | `and_(a, b)`
Bitwise Exclusive Or | `a ^ b` | `xor(a, b)`
Bitwise Inversion | `~ a` | `invert(a)`
Bitwise Or | `a | b` | `or_(a, b)`
Exponentiation | `a ** b` | `pow(a, b)`
Identity | `a is b` | `is_(a, b)`
Identity | `a is not b` | `is_not(a, b)`
Identity | `a is None` | `is_none(a)`
Identity | `a is not None` | `is_not_none(a)`
Indexed Assignment | `obj[k] = v` | `setitem(obj, k, v)`
Indexed Deletion | `del obj[k]` | `delitem(obj, k)`
Indexing | `obj[k]` | `getitem(obj, k)`
Left Shift | `a << b` | `lshift(a, b)`
Modulo | `a % b` | `mod(a, b)`
Multiplication | `a * b` | `mul(a, b)`
Matrix Multiplication | `a @ b` | `matmul(a, b)`
Negation (Arithmetic) | `- a` | `neg(a)`
Negation (Logical) | `not a` | `not_(a)`
Positive | `+ a` | `pos(a)`
Right Shift | `a >> b` | `rshift(a, b)`
Slice Assignment | `seq[i:j] = values` | `setitem(seq, slice(i, j), values)`
Slice Deletion | `del seq[i:j]` | `delitem(seq, slice(i, j))`
Slicing | `seq[i:j]` | `getitem(seq, slice(i, j))`
String Formatting | `s % obj` | `mod(s, obj)`
Subtraction | `a - b` | `sub(a, b)`
Truth Test | `obj` | `truth(obj)`
Ordering | `a < b` | `lt(a, b)`
Ordering | `a <= b` | `le(a, b)`
Equality | `a == b` | `eq(a, b)`
Difference | `a != b` | `ne(a, b)`
Ordering | `a >= b` | `ge(a, b)`
Ordering | `a > b` | `gt(a, b)`
## In-place Operators[¶](https://docs.python.org/3/library/operator.html#in-place-operators "Link to this heading")
Many operations have an “in-place” version. Listed below are functions providing a more primitive access to in-place operators than the usual syntax does; for example, the [statement](https://docs.python.org/3/glossary.html#term-statement) `x += y` is equivalent to `x = operator.iadd(x, y)`. Another way to put it is to say that `z = operator.iadd(x, y)` is equivalent to the compound statement `z = x; z += y`.
In those examples, note that when an in-place method is called, the computation and assignment are performed in two separate steps. The in-place functions listed below only do the first step, calling the in-place method. The second step, assignment, is not handled.
For immutable targets such as strings, numbers, and tuples, the updated value is computed, but not assigned back to the input variable:
Copy```
>>> a = 'hello'
>>> iadd(a, ' world')
'hello world'
>>> a
'hello'

```

For mutable targets such as lists and dictionaries, the in-place method will perform the update, so no subsequent assignment is necessary:
Copy```
>>> s = ['h', 'e', 'l', 'l', 'o']
>>> iadd(s, [' ', 'w', 'o', 'r', 'l', 'd'])
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> s
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

```


operator.iadd(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.iadd "Link to this definition")


operator.__iadd__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__iadd__ "Link to this definition")

`a = iadd(a, b)` is equivalent to `a += b`.

operator.iand(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.iand "Link to this definition")


operator.__iand__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__iand__ "Link to this definition")

`a = iand(a, b)` is equivalent to `a &= b`.

operator.iconcat(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.iconcat "Link to this definition")


operator.__iconcat__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__iconcat__ "Link to this definition")

`a = iconcat(a, b)` is equivalent to `a += b` for _a_ and _b_ sequences.

operator.ifloordiv(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.ifloordiv "Link to this definition")


operator.__ifloordiv__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__ifloordiv__ "Link to this definition")

`a = ifloordiv(a, b)` is equivalent to `a //= b`.

operator.ilshift(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.ilshift "Link to this definition")


operator.__ilshift__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__ilshift__ "Link to this definition")

`a = ilshift(a, b)` is equivalent to `a <<= b`.

operator.imod(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.imod "Link to this definition")


operator.__imod__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__imod__ "Link to this definition")

`a = imod(a, b)` is equivalent to `a %= b`.

operator.imul(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.imul "Link to this definition")


operator.__imul__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__imul__ "Link to this definition")

`a = imul(a, b)` is equivalent to `a *= b`.

operator.imatmul(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.imatmul "Link to this definition")


operator.__imatmul__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__imatmul__ "Link to this definition")

`a = imatmul(a, b)` is equivalent to `a @= b`.
Added in version 3.5.

operator.ior(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.ior "Link to this definition")


operator.__ior__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__ior__ "Link to this definition")

`a = ior(a, b)` is equivalent to `a |= b`.

operator.ipow(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.ipow "Link to this definition")


operator.__ipow__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__ipow__ "Link to this definition")

`a = ipow(a, b)` is equivalent to `a **= b`.

operator.irshift(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.irshift "Link to this definition")


operator.__irshift__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__irshift__ "Link to this definition")

`a = irshift(a, b)` is equivalent to `a >>= b`.

operator.isub(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.isub "Link to this definition")


operator.__isub__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__isub__ "Link to this definition")

`a = isub(a, b)` is equivalent to `a -= b`.

operator.itruediv(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.itruediv "Link to this definition")


operator.__itruediv__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__itruediv__ "Link to this definition")

`a = itruediv(a, b)` is equivalent to `a /= b`.

operator.ixor(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.ixor "Link to this definition")


operator.__ixor__(_a_ , _b_)[¶](https://docs.python.org/3/library/operator.html#operator.__ixor__ "Link to this definition")

`a = ixor(a, b)` is equivalent to `a ^= b`.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`operator` — Standard operators as functions](https://docs.python.org/3/library/operator.html)
    * [Mapping Operators to Functions](https://docs.python.org/3/library/operator.html#mapping-operators-to-functions)
    * [In-place Operators](https://docs.python.org/3/library/operator.html#in-place-operators)


#### Previous topic
[`functools` — Higher-order functions and operations on callable objects](https://docs.python.org/3/library/functools.html "previous chapter")
#### Next topic
[File and Directory Access](https://docs.python.org/3/library/filesys.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=operator+%E2%80%94+Standard+operators+as+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Foperator.html&pagesource=library%2Foperator.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/filesys.html "File and Directory Access") |
  * [previous](https://docs.python.org/3/library/functools.html "functools — Higher-order functions and operations on callable objects") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Functional Programming Modules](https://docs.python.org/3/library/functional.html) »
  * [`operator` — Standard operators as functions](https://docs.python.org/3/library/operator.html)
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
