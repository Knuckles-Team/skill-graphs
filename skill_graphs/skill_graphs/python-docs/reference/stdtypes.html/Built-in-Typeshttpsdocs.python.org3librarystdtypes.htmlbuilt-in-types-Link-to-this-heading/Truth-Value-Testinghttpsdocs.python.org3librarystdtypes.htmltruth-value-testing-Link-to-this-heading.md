## Truth Value Testing[¶](https://docs.python.org/3/library/stdtypes.html#truth-value-testing "Link to this heading")
Any object can be tested for truth value, for use in an [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) or [`while`](https://docs.python.org/3/reference/compound_stmts.html#while) condition or as operand of the Boolean operations below.
By default, an object is considered true unless its class defines either a [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__ "object.__bool__") method that returns `False` or a [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__") method that returns zero, when called with the object. [[1]](https://docs.python.org/3/library/stdtypes.html#id12) If one of the methods raises an exception when called, the exception is propagated and the object does not have a truth value (for example, [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented")). Here are most of the built-in objects considered false:
  * constants defined to be false: `None` and `False`
  * zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
  * empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`


Operations and built-in functions that have a Boolean result always return `0` or `False` for false and `1` or `True` for true, unless otherwise stated. (Important exception: the Boolean operations `or` and `and` always return one of their operands.)
