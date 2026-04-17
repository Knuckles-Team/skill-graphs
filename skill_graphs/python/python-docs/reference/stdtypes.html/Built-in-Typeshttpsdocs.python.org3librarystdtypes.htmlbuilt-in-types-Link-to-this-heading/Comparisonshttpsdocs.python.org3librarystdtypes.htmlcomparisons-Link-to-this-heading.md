## Comparisons[¶](https://docs.python.org/3/library/stdtypes.html#comparisons "Link to this heading")
There are eight comparison operations in Python. They all have the same priority (which is higher than that of the Boolean operations). Comparisons can be chained arbitrarily; for example, `x < y <= z` is equivalent to `x < y and y <= z`, except that _y_ is evaluated only once (but in both cases _z_ is not evaluated at all when `x < y` is found to be false).
This table summarizes the comparison operations:
Operation | Meaning
---|---
`<` | strictly less than
`<=` | less than or equal
`>` | strictly greater than
`>=` | greater than or equal
`==` | equal
`!=` | not equal
`is` | object identity
`is not` | negated object identity
Unless stated otherwise, objects of different types never compare equal. The `==` operator is always defined but for some object types (for example, class objects) is equivalent to [`is`](https://docs.python.org/3/reference/expressions.html#is). The `<`, `<=`, `>` and `>=` operators are only defined where they make sense; for example, they raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception when one of the arguments is a complex number.
Non-identical instances of a class normally compare as non-equal unless the class defines the [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__") method.
Instances of a class cannot be ordered with respect to other instances of the same class, or other types of object, unless the class defines enough of the methods [`__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__"), [`__le__()`](https://docs.python.org/3/reference/datamodel.html#object.__le__ "object.__le__"), [`__gt__()`](https://docs.python.org/3/reference/datamodel.html#object.__gt__ "object.__gt__"), and [`__ge__()`](https://docs.python.org/3/reference/datamodel.html#object.__ge__ "object.__ge__") (in general, `__lt__()` and [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__") are sufficient, if you want the conventional meanings of the comparison operators).
The behavior of the [`is`](https://docs.python.org/3/reference/expressions.html#is) and [`is not`](https://docs.python.org/3/reference/expressions.html#is-not) operators cannot be customized; also they can be applied to any two objects and never raise an exception.
Two more operations with the same syntactic priority, [`in`](https://docs.python.org/3/reference/expressions.html#in) and [`not in`](https://docs.python.org/3/reference/expressions.html#not-in), are supported by types that are [iterable](https://docs.python.org/3/glossary.html#term-iterable) or implement the [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__") method.
