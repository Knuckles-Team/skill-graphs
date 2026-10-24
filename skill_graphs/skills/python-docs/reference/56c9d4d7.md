#  `decimal` — Decimal fixed-point and floating-point arithmetic[¶](https://docs.python.org/3/library/decimal.html#module-decimal "Link to this heading")
**Source code:**
* * *
The `decimal` module provides support for fast correctly rounded decimal floating-point arithmetic. It offers several advantages over the [`float`](https://docs.python.org/3/library/functions.html#float "float") datatype:
  * Decimal “is based on a
  * Decimal numbers can be represented exactly. In contrast, numbers like `1.1` and `2.2` do not have exact representations in binary floating point. End users typically would not expect `1.1 + 2.2` to display as `3.3000000000000003` as it does with binary floating point.
  * The exactness carries over into arithmetic. In decimal floating point, `0.1 + 0.1 + 0.1 - 0.3` is exactly equal to zero. In binary floating point, the result is `5.5511151231257827e-017`. While near to zero, the differences prevent reliable equality testing and differences can accumulate. For this reason, decimal is preferred in accounting applications which have strict equality invariants.
  * The decimal module incorporates a notion of significant places so that `1.30 + 1.20` is `2.50`. The trailing zero is kept to indicate significance. This is the customary presentation for monetary applications. For multiplication, the “schoolbook” approach uses all the figures in the multiplicands. For instance, `1.3 * 1.2` gives `1.56` while `1.30 * 1.20` gives `1.5600`.
  * Unlike hardware based binary floating point, the decimal module has a user alterable precision (defaulting to 28 places) which can be as large as needed for a given problem:
Copy```
>>> from decimal import *
>>> getcontext().prec = 6
>>> Decimal(1) / Decimal(7)
Decimal('0.142857')
>>> getcontext().prec = 28
>>> Decimal(1) / Decimal(7)
Decimal('0.1428571428571428571428571429')

```

  * Both binary and decimal floating point are implemented in terms of published standards. While the built-in float type exposes only a modest portion of its capabilities, the decimal module exposes all required parts of the standard. When needed, the programmer has full control over rounding and signal handling. This includes an option to enforce exact arithmetic by using exceptions to block any inexact operations.
  * The decimal module was designed to support “without prejudice, both exact unrounded decimal arithmetic (sometimes called fixed-point arithmetic) and rounded floating-point arithmetic.” – excerpt from the decimal arithmetic specification.


The module design is centered around three concepts: the decimal number, the context for arithmetic, and signals.
A decimal number is immutable. It has a sign, coefficient digits, and an exponent. To preserve significance, the coefficient digits do not truncate trailing zeros. Decimals also include special values such as `Infinity`, `-Infinity`, and `NaN`. The standard also differentiates `-0` from `+0`.
The context for arithmetic is an environment specifying precision, rounding rules, limits on exponents, flags indicating the results of operations, and trap enablers which determine whether signals are treated as exceptions. Rounding options include [`ROUND_CEILING`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_CEILING "decimal.ROUND_CEILING"), [`ROUND_DOWN`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_DOWN "decimal.ROUND_DOWN"), [`ROUND_FLOOR`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_FLOOR "decimal.ROUND_FLOOR"), [`ROUND_HALF_DOWN`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_HALF_DOWN "decimal.ROUND_HALF_DOWN"), [`ROUND_HALF_EVEN`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_HALF_EVEN "decimal.ROUND_HALF_EVEN"), [`ROUND_HALF_UP`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_HALF_UP "decimal.ROUND_HALF_UP"), [`ROUND_UP`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_UP "decimal.ROUND_UP"), and [`ROUND_05UP`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_05UP "decimal.ROUND_05UP").
Signals are groups of exceptional conditions arising during the course of computation. Depending on the needs of the application, signals may be ignored, considered as informational, or treated as exceptions. The signals in the decimal module are: [`Clamped`](https://docs.python.org/3/library/decimal.html#decimal.Clamped "decimal.Clamped"), [`InvalidOperation`](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "decimal.InvalidOperation"), [`DivisionByZero`](https://docs.python.org/3/library/decimal.html#decimal.DivisionByZero "decimal.DivisionByZero"), [`Inexact`](https://docs.python.org/3/library/decimal.html#decimal.Inexact "decimal.Inexact"), [`Rounded`](https://docs.python.org/3/library/decimal.html#decimal.Rounded "decimal.Rounded"), [`Subnormal`](https://docs.python.org/3/library/decimal.html#decimal.Subnormal "decimal.Subnormal"), [`Overflow`](https://docs.python.org/3/library/decimal.html#decimal.Overflow "decimal.Overflow"), [`Underflow`](https://docs.python.org/3/library/decimal.html#decimal.Underflow "decimal.Underflow") and [`FloatOperation`](https://docs.python.org/3/library/decimal.html#decimal.FloatOperation "decimal.FloatOperation").
For each signal there is a flag and a trap enabler. When a signal is encountered, its flag is set to one, then, if the trap enabler is set to one, an exception is raised. Flags are sticky, so the user needs to reset them before monitoring a calculation.
See also
  * IBM’s General Decimal Arithmetic Specification,


## Quick-start tutorial[¶](https://docs.python.org/3/library/decimal.html#quick-start-tutorial "Link to this heading")
The usual start to using decimals is importing the module, viewing the current context with [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext") and, if necessary, setting new values for precision, rounding, or enabled traps:
Copy```
>>> from decimal import *
>>> getcontext()
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
        capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
        InvalidOperation])

>>> getcontext().prec = 7       # Set a new precision

```

Decimal instances can be constructed from integers, strings, floats, or tuples. Construction from an integer or a float performs an exact conversion of the value of that integer or float. Decimal numbers include special values such as `NaN` which stands for “Not a number”, positive and negative `Infinity`, and `-0`:
Copy```
>>> getcontext().prec = 28
>>> Decimal(10)
Decimal('10')
>>> Decimal('3.14')
Decimal('3.14')
>>> Decimal(3.14)
Decimal('3.140000000000000124344978758017532527446746826171875')
>>> Decimal((0, (3, 1, 4), -2))
Decimal('3.14')
>>> Decimal(str(2.0 ** 0.5))
Decimal('1.4142135623730951')
>>> Decimal(2) ** Decimal('0.5')
Decimal('1.414213562373095048801688724')
>>> Decimal('NaN')
Decimal('NaN')
>>> Decimal('-Infinity')
Decimal('-Infinity')

```

If the [`FloatOperation`](https://docs.python.org/3/library/decimal.html#decimal.FloatOperation "decimal.FloatOperation") signal is trapped, accidental mixing of decimals and floats in constructors or ordering comparisons raises an exception:
Copy```
>>> c = getcontext()
>>> c.traps[FloatOperation] = True
>>> Decimal(3.14)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
>>> Decimal('3.5') < 3.7
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
>>> Decimal('3.5') == 3.5
True

```

Added in version 3.3.
The significance of a new Decimal is determined solely by the number of digits input. Context precision and rounding only come into play during arithmetic operations.
Copy```
>>> getcontext().prec = 6
>>> Decimal('3.0')
Decimal('3.0')
>>> Decimal('3.1415926535')
Decimal('3.1415926535')
>>> Decimal('3.1415926535') + Decimal('2.7182818285')
Decimal('5.85987')
>>> getcontext().rounding = ROUND_UP
>>> Decimal('3.1415926535') + Decimal('2.7182818285')
Decimal('5.85988')

```

If the internal limits of the C version are exceeded, constructing a decimal raises [`InvalidOperation`](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "decimal.InvalidOperation"):
Copy```
>>> Decimal("1e9999999999999999999")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
decimal.InvalidOperation: [<class 'decimal.InvalidOperation'>]

```

Changed in version 3.3.
Decimals interact well with much of the rest of Python. Here is a small decimal floating-point flying circus:
Copy```
>>> data = list(map(Decimal, '1.34 1.87 3.45 2.35 1.00 0.03 9.25'.split()))
>>> max(data)
Decimal('9.25')
>>> min(data)
Decimal('0.03')
>>> sorted(data)
[Decimal('0.03'), Decimal('1.00'), Decimal('1.34'), Decimal('1.87'),
 Decimal('2.35'), Decimal('3.45'), Decimal('9.25')]
>>> sum(data)
Decimal('19.29')
>>> a,b,c = data[:3]
>>> str(a)
'1.34'
>>> float(a)
1.34
>>> round(a, 1)
Decimal('1.3')
>>> int(a)
1
>>> a * 5
Decimal('6.70')
>>> a * b
Decimal('2.5058')
>>> c % a
Decimal('0.77')

```

Decimals can be formatted (with [`format()`](https://docs.python.org/3/library/functions.html#format "format") built-in or [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)) in fixed-point or scientific notation, using the same formatting syntax (see [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec)) as builtin [`float`](https://docs.python.org/3/library/functions.html#float "float") type:
Copy```
>>> format(Decimal('2.675'), "f")
'2.675'
>>> format(Decimal('2.675'), ".2f")
'2.68'
>>> f"{Decimal('2.675'):.2f}"
'2.68'
>>> format(Decimal('2.675'), ".2e")
'2.68e+0'
>>> with localcontext() as ctx:
...     ctx.rounding = ROUND_DOWN
...     print(format(Decimal('2.675'), ".2f"))
...
2.67

```

And some mathematical functions are also available to Decimal:
Copy```
>>> getcontext().prec = 28
>>> Decimal(2).sqrt()
Decimal('1.414213562373095048801688724')
>>> Decimal(1).exp()
Decimal('2.718281828459045235360287471')
>>> Decimal('10').ln()
Decimal('2.302585092994045684017991455')
>>> Decimal('10').log10()
Decimal('1')

```

The [`quantize()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.quantize "decimal.Decimal.quantize") method rounds a number to a fixed exponent. This method is useful for monetary applications that often round results to a fixed number of places:
Copy```
>>> Decimal('7.325').quantize(Decimal('.01'), rounding=ROUND_DOWN)
Decimal('7.32')
>>> Decimal('7.325').quantize(Decimal('1.'), rounding=ROUND_UP)
Decimal('8')

```

As shown above, the [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext") function accesses the current context and allows the settings to be changed. This approach meets the needs of most applications.
For more advanced work, it may be useful to create alternate contexts using the [`Context()`](https://docs.python.org/3/library/decimal.html#decimal.Context "decimal.Context") constructor. To make an alternate active, use the [`setcontext()`](https://docs.python.org/3/library/decimal.html#decimal.setcontext "decimal.setcontext") function.
In accordance with the standard, the `decimal` module provides two ready to use standard contexts, [`BasicContext`](https://docs.python.org/3/library/decimal.html#decimal.BasicContext "decimal.BasicContext") and [`ExtendedContext`](https://docs.python.org/3/library/decimal.html#decimal.ExtendedContext "decimal.ExtendedContext"). The former is especially useful for debugging because many of the traps are enabled:
Copy```
>>> myothercontext = Context(prec=60, rounding=ROUND_HALF_DOWN)
>>> setcontext(myothercontext)
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857142857142857142857142857')

>>> ExtendedContext
Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
        capitals=1, clamp=0, flags=[], traps=[])
>>> setcontext(ExtendedContext)
>>> Decimal(1) / Decimal(7)
Decimal('0.142857143')
>>> Decimal(42) / Decimal(0)
Decimal('Infinity')

>>> setcontext(BasicContext)
>>> Decimal(42) / Decimal(0)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in -toplevel-
    Decimal(42) / Decimal(0)
DivisionByZero: x / 0

```

Contexts also have signal flags for monitoring exceptional conditions encountered during computations. The flags remain set until explicitly cleared, so it is best to clear the flags before each set of monitored computations by using the [`clear_flags()`](https://docs.python.org/3/library/decimal.html#decimal.Context.clear_flags "decimal.Context.clear_flags") method.
Copy```
>>> setcontext(ExtendedContext)
>>> getcontext().clear_flags()
>>> Decimal(355) / Decimal(113)
Decimal('3.14159292')
>>> getcontext()
Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
        capitals=1, clamp=0, flags=[Inexact, Rounded], traps=[])

```

The _flags_ entry shows that the rational approximation to pi was rounded (digits beyond the context precision were thrown away) and that the result is inexact (some of the discarded digits were non-zero).
Individual traps are set using the dictionary in the [`traps`](https://docs.python.org/3/library/decimal.html#decimal.Context.traps "decimal.Context.traps") attribute of a context:
Copy```
>>> setcontext(ExtendedContext)
>>> Decimal(1) / Decimal(0)
Decimal('Infinity')
>>> getcontext().traps[DivisionByZero] = 1
>>> Decimal(1) / Decimal(0)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in -toplevel-
    Decimal(1) / Decimal(0)
DivisionByZero: x / 0

```

Most programs adjust the current context only once, at the beginning of the program. And, in many applications, data is converted to [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") with a single cast inside a loop. With context set and decimals created, the bulk of the program manipulates the data no differently than with other Python numeric types.
## Decimal objects[¶](https://docs.python.org/3/library/decimal.html#decimal-objects "Link to this heading")

_class_ decimal.Decimal(_value ='0'_, _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal "Link to this definition")

Construct a new `Decimal` object based from _value_.
_value_ can be an integer, string, tuple, [`float`](https://docs.python.org/3/library/functions.html#float "float"), or another `Decimal` object. If no _value_ is given, returns `Decimal('0')`. If _value_ is a string, it should conform to the decimal numeric string syntax after leading and trailing whitespace characters, as well as underscores throughout, are removed:
Copy```
sign           ::=  '+' | '-'
digit          ::=  '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
indicator      ::=  'e' | 'E'
digits         ::=  digit [digit]...
decimal-part   ::=  digits '.' [digits] | ['.'] digits
exponent-part  ::=  indicator [sign] digits
infinity       ::=  'Infinity' | 'Inf'
nan            ::=  'NaN' [digits] | 'sNaN' [digits]
numeric-value  ::=  decimal-part [exponent-part] | infinity
numeric-string ::=  [sign] numeric-value | [sign] nan

```

Other Unicode decimal digits are also permitted where `digit` appears above. These include decimal digits from various other alphabets (for example, Arabic-Indic and Devanāgarī digits) along with the fullwidth digits `'\uff10'` through `'\uff19'`. Case is not significant, so, for example, `inf`, `Inf`, `INFINITY`, and `iNfINity` are all acceptable spellings for positive infinity.
If _value_ is a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"), it should have three components, a sign (`0` for positive or `1` for negative), a `tuple` of digits, and an integer exponent. For example, `Decimal((0, (1, 4, 1, 4), -3))` returns `Decimal('1.414')`.
If _value_ is a [`float`](https://docs.python.org/3/library/functions.html#float "float"), the binary floating-point value is losslessly converted to its exact decimal equivalent. This conversion can often require 53 or more digits of precision. For example, `Decimal(float('1.1'))` converts to `Decimal('1.100000000000000088817841970012523233890533447265625')`.
The _context_ precision does not affect how many digits are stored. That is determined exclusively by the number of digits in _value_. For example, `Decimal('3.00000')` records all five zeros even if the context precision is only three.
The purpose of the _context_ argument is determining what to do if _value_ is a malformed string. If the context traps [`InvalidOperation`](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "decimal.InvalidOperation"), an exception is raised; otherwise, the constructor returns a new Decimal with the value of `NaN`.
Once constructed, `Decimal` objects are immutable.
Changed in version 3.2: The argument to the constructor is now permitted to be a [`float`](https://docs.python.org/3/library/functions.html#float "float") instance.
Changed in version 3.3: [`float`](https://docs.python.org/3/library/functions.html#float "float") arguments raise an exception if the [`FloatOperation`](https://docs.python.org/3/library/decimal.html#decimal.FloatOperation "decimal.FloatOperation") trap is set. By default the trap is off.
Changed in version 3.6: Underscores are allowed for grouping, as with integral and floating-point literals in code.
Decimal floating-point objects share many properties with the other built-in numeric types such as [`float`](https://docs.python.org/3/library/functions.html#float "float") and [`int`](https://docs.python.org/3/library/functions.html#int "int"). All of the usual math operations and special methods apply. Likewise, decimal objects can be copied, pickled, printed, used as dictionary keys, used as set elements, compared, sorted, and coerced to another type (such as `float` or `int`).
There are some small differences between arithmetic on Decimal objects and arithmetic on integers and floats. When the remainder operator `%` is applied to Decimal objects, the sign of the result is the sign of the _dividend_ rather than the sign of the divisor:
Copy```
>>> (-7) % 4
1
>>> Decimal(-7) % Decimal(4)
Decimal('-3')

```

The integer division operator `//` behaves analogously, returning the integer part of the true quotient (truncating towards zero) rather than its floor, so as to preserve the usual identity `x == (x // y) * y + x % y`:
Copy```
>>> -7 // 4
-2
>>> Decimal(-7) // Decimal(4)
Decimal('-1')

```

The `%` and `//` operators implement the `remainder` and `divide-integer` operations (respectively) as described in the specification.
Decimal objects cannot generally be combined with floats or instances of [`fractions.Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction") in arithmetic operations: an attempt to add a `Decimal` to a [`float`](https://docs.python.org/3/library/functions.html#float "float"), for example, will raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). However, it is possible to use Python’s comparison operators to compare a `Decimal` instance `x` with another number `y`. This avoids confusing results when doing equality comparisons between numbers of different types.
Changed in version 3.2: Mixed-type comparisons between `Decimal` instances and other numeric types are now fully supported.
In addition to the standard numeric properties, decimal floating-point objects also have a number of specialized methods:

adjusted()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.adjusted "Link to this definition")

Return the adjusted exponent after shifting out the coefficient’s rightmost digits until only the lead digit remains: `Decimal('321e+5').adjusted()` returns seven. Used for determining the position of the most significant digit with respect to the decimal point.

as_integer_ratio()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.as_integer_ratio "Link to this definition")

Return a pair `(n, d)` of integers that represent the given `Decimal` instance as a fraction, in lowest terms and with a positive denominator:
Copy```
>>> Decimal('-3.14').as_integer_ratio()
(-157, 50)

```

The conversion is exact. Raise OverflowError on infinities and ValueError on NaNs.
Added in version 3.6.

as_tuple()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.as_tuple "Link to this definition")

Return a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) representation of the number: `DecimalTuple(sign, digits, exponent)`.

canonical()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.canonical "Link to this definition")

Return the canonical encoding of the argument. Currently, the encoding of a `Decimal` instance is always canonical, so this operation returns its argument unchanged.

compare(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.compare "Link to this definition")

Compare the values of two Decimal instances. `compare()` returns a Decimal instance, and if either operand is a NaN then the result is a NaN:
Copy```
a or b is a NaN  ==> Decimal('NaN')
a < b            ==> Decimal('-1')
a == b           ==> Decimal('0')
a > b            ==> Decimal('1')

```


compare_signal(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.compare_signal "Link to this definition")

This operation is identical to the [`compare()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.compare "decimal.Decimal.compare") method, except that all NaNs signal. That is, if neither operand is a signaling NaN then any quiet NaN operand is treated as though it were a signaling NaN.

compare_total(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.compare_total "Link to this definition")

Compare two operands using their abstract representation rather than their numerical value. Similar to the [`compare()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.compare "decimal.Decimal.compare") method, but the result gives a total ordering on `Decimal` instances. Two `Decimal` instances with the same numeric value but different representations compare unequal in this ordering:
Copy```
>>> Decimal('12.0').compare_total(Decimal('12'))
Decimal('-1')

```

Quiet and signaling NaNs are also included in the total ordering. The result of this function is `Decimal('0')` if both operands have the same representation, `Decimal('-1')` if the first operand is lower in the total order than the second, and `Decimal('1')` if the first operand is higher in the total order than the second operand. See the specification for details of the total order.
This operation is unaffected by context and is quiet: no flags are changed and no rounding is performed. As an exception, the C version may raise InvalidOperation if the second operand cannot be converted exactly.

compare_total_mag(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.compare_total_mag "Link to this definition")

Compare two operands using their abstract representation rather than their value as in [`compare_total()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.compare_total "decimal.Decimal.compare_total"), but ignoring the sign of each operand. `x.compare_total_mag(y)` is equivalent to `x.copy_abs().compare_total(y.copy_abs())`.
This operation is unaffected by context and is quiet: no flags are changed and no rounding is performed. As an exception, the C version may raise InvalidOperation if the second operand cannot be converted exactly.

conjugate()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.conjugate "Link to this definition")

Just returns self, this method is only to comply with the Decimal Specification.

copy_abs()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.copy_abs "Link to this definition")

Return the absolute value of the argument. This operation is unaffected by the context and is quiet: no flags are changed and no rounding is performed.

copy_negate()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.copy_negate "Link to this definition")

Return the negation of the argument. This operation is unaffected by the context and is quiet: no flags are changed and no rounding is performed.

copy_sign(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.copy_sign "Link to this definition")

Return a copy of the first operand with the sign set to be the same as the sign of the second operand. For example:
Copy```
>>> Decimal('2.3').copy_sign(Decimal('-1.5'))
Decimal('-2.3')

```

This operation is unaffected by context and is quiet: no flags are changed and no rounding is performed. As an exception, the C version may raise InvalidOperation if the second operand cannot be converted exactly.

exp(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp "Link to this definition")

Return the value of the (natural) exponential function `e**x` at the given number. The result is correctly rounded using the [`ROUND_HALF_EVEN`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_HALF_EVEN "decimal.ROUND_HALF_EVEN") rounding mode.
