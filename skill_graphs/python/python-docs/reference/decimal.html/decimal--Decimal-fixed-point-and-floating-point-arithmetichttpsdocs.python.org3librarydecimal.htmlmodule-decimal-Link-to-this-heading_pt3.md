Added in version 3.14.
New contexts can also be created using the [`Context`](https://docs.python.org/3/library/decimal.html#decimal.Context "decimal.Context") constructor described below. In addition, the module provides three pre-made contexts:

decimal.BasicContext[¶](https://docs.python.org/3/library/decimal.html#decimal.BasicContext "Link to this definition")

This is a standard context defined by the General Decimal Arithmetic Specification. Precision is set to nine. Rounding is set to [`ROUND_HALF_UP`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_HALF_UP "decimal.ROUND_HALF_UP"). All flags are cleared. All traps are enabled (treated as exceptions) except [`Inexact`](https://docs.python.org/3/library/decimal.html#decimal.Inexact "decimal.Inexact"), [`Rounded`](https://docs.python.org/3/library/decimal.html#decimal.Rounded "decimal.Rounded"), and [`Subnormal`](https://docs.python.org/3/library/decimal.html#decimal.Subnormal "decimal.Subnormal").
Because many of the traps are enabled, this context is useful for debugging.

decimal.ExtendedContext[¶](https://docs.python.org/3/library/decimal.html#decimal.ExtendedContext "Link to this definition")

This is a standard context defined by the General Decimal Arithmetic Specification. Precision is set to nine. Rounding is set to [`ROUND_HALF_EVEN`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_HALF_EVEN "decimal.ROUND_HALF_EVEN"). All flags are cleared. No traps are enabled (so that exceptions are not raised during computations).
Because the traps are disabled, this context is useful for applications that prefer to have result value of `NaN` or `Infinity` instead of raising exceptions. This allows an application to complete a run in the presence of conditions that would otherwise halt the program.

decimal.DefaultContext[¶](https://docs.python.org/3/library/decimal.html#decimal.DefaultContext "Link to this definition")

This context is used by the [`Context`](https://docs.python.org/3/library/decimal.html#decimal.Context "decimal.Context") constructor as a prototype for new contexts. Changing a field (such a precision) has the effect of changing the default for new contexts created by the `Context` constructor.
This context is most useful in multi-threaded environments. Changing one of the fields before threads are started has the effect of setting system-wide defaults. Changing the fields after threads have started is not recommended as it would require thread synchronization to prevent race conditions.
In single threaded environments, it is preferable to not use this context at all. Instead, simply create contexts explicitly as described below.
The default values are [`Context.prec`](https://docs.python.org/3/library/decimal.html#decimal.Context.prec "decimal.Context.prec")=`28`, [`Context.rounding`](https://docs.python.org/3/library/decimal.html#decimal.Context.rounding "decimal.Context.rounding")=[`ROUND_HALF_EVEN`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_HALF_EVEN "decimal.ROUND_HALF_EVEN"), and enabled traps for [`Overflow`](https://docs.python.org/3/library/decimal.html#decimal.Overflow "decimal.Overflow"), [`InvalidOperation`](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "decimal.InvalidOperation"), and [`DivisionByZero`](https://docs.python.org/3/library/decimal.html#decimal.DivisionByZero "decimal.DivisionByZero").
In addition to the three supplied contexts, new contexts can be created with the [`Context`](https://docs.python.org/3/library/decimal.html#decimal.Context "decimal.Context") constructor.

_class_ decimal.Context(_prec =None_, _rounding =None_, _Emin =None_, _Emax =None_, _capitals =None_, _clamp =None_, _flags =None_, _traps =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context "Link to this definition")

Creates a new context. If a field is not specified or is [`None`](https://docs.python.org/3/library/constants.html#None "None"), the default values are copied from the [`DefaultContext`](https://docs.python.org/3/library/decimal.html#decimal.DefaultContext "decimal.DefaultContext"). If the _flags_ field is not specified or is `None`, all flags are cleared.

prec[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.prec "Link to this definition")

An integer in the range [`1`, [`MAX_PREC`](https://docs.python.org/3/library/decimal.html#decimal.MAX_PREC "decimal.MAX_PREC")] that sets the precision for arithmetic operations in the context.

rounding[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.rounding "Link to this definition")

One of the constants listed in the section [Rounding Modes](https://docs.python.org/3/library/decimal.html#rounding-modes).

traps[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.traps "Link to this definition")


flags[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.flags "Link to this definition")

Lists of any signals to be set. Generally, new contexts should only set traps and leave the flags clear.

Emin[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.Emin "Link to this definition")


Emax[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.Emax "Link to this definition")

Integers specifying the outer limits allowable for exponents. _Emin_ must be in the range [[`MIN_EMIN`](https://docs.python.org/3/library/decimal.html#decimal.MIN_EMIN "decimal.MIN_EMIN"), `0`], _Emax_ in the range [`0`, [`MAX_EMAX`](https://docs.python.org/3/library/decimal.html#decimal.MAX_EMAX "decimal.MAX_EMAX")].

capitals[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.capitals "Link to this definition")

Either `0` or `1` (the default). If set to `1`, exponents are printed with a capital `E`; otherwise, a lowercase `e` is used: `Decimal('6.02e+23')`.

clamp[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.clamp "Link to this definition")

Either `0` (the default) or `1`. If set to `1`, the exponent `e` of a [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") instance representable in this context is strictly limited to the range `Emin - prec + 1 <= e <= Emax - prec + 1`. If _clamp_ is `0` then a weaker condition holds: the adjusted exponent of the `Decimal` instance is at most [`Emax`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emax "decimal.Context.Emax"). When _clamp_ is `1`, a large normal number will, where possible, have its exponent reduced and a corresponding number of zeros added to its coefficient, in order to fit the exponent constraints; this preserves the value of the number but loses information about significant trailing zeros. For example:
Copy```
>>> Context(prec=6, Emax=999, clamp=1).create_decimal('1.23e999')
Decimal('1.23000E+999')

```

A _clamp_ value of `1` allows compatibility with the fixed-width decimal interchange formats specified in IEEE 754.
The `Context` class defines several general purpose methods as well as a large number of methods for doing arithmetic directly in a given context. In addition, for each of the [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") methods described above (with the exception of the [`adjusted()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.adjusted "decimal.Decimal.adjusted") and [`as_tuple()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.as_tuple "decimal.Decimal.as_tuple") methods) there is a corresponding `Context` method. For example, for a `Context` instance `C` and `Decimal` instance `x`, `C.exp(x)` is equivalent to `x.exp(context=C)`. Each `Context` method accepts a Python integer (an instance of [`int`](https://docs.python.org/3/library/functions.html#int "int")) anywhere that a Decimal instance is accepted.

clear_flags()[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.clear_flags "Link to this definition")

Resets all of the flags to `0`.

clear_traps()[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.clear_traps "Link to this definition")

Resets all of the traps to `0`.
Added in version 3.3.

copy()[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.copy "Link to this definition")

Return a duplicate of the context.

copy_decimal(_num_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.copy_decimal "Link to this definition")

Return a copy of the Decimal instance num.

create_decimal(_num ='0'_, _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.create_decimal "Link to this definition")

Creates a new Decimal instance from _num_ but using _self_ as context. Unlike the [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") constructor, the context precision, rounding method, flags, and traps are applied to the conversion.
This is useful because constants are often given to a greater precision than is needed by the application. Another benefit is that rounding immediately eliminates unintended effects from digits beyond the current precision. In the following example, using unrounded inputs means that adding zero to a sum can change the result:
Copy```
>>> getcontext().prec = 3
>>> Decimal('3.4445') + Decimal('1.0023')
Decimal('4.45')
>>> Decimal('3.4445') + Decimal(0) + Decimal('1.0023')
Decimal('4.44')

```

This method implements the to-number operation of the IBM specification. If the argument is a string, no leading or trailing whitespace or underscores are permitted.

create_decimal_from_float(_f_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.create_decimal_from_float "Link to this definition")

Creates a new Decimal instance from a float _f_ but rounding using _self_ as the context. Unlike the [`Decimal.from_float()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.from_float "decimal.Decimal.from_float") class method, the context precision, rounding method, flags, and traps are applied to the conversion.
Copy```
>>> context = Context(prec=5, rounding=ROUND_DOWN)
>>> context.create_decimal_from_float(math.pi)
Decimal('3.1415')
>>> context = Context(prec=5, traps=[Inexact])
>>> context.create_decimal_from_float(math.pi)
Traceback (most recent call last):
    ...
decimal.Inexact: None

```

Added in version 3.1.

Etiny()[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.Etiny "Link to this definition")

Returns a value equal to `Emin - prec + 1` which is the minimum exponent value for subnormal results. When underflow occurs, the exponent is set to [`Etiny`](https://docs.python.org/3/library/decimal.html#decimal.Context.Etiny "decimal.Context.Etiny").

Etop()[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.Etop "Link to this definition")

Returns a value equal to `Emax - prec + 1`.
The usual approach to working with decimals is to create [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") instances and then apply arithmetic operations which take place within the current context for the active thread. An alternative approach is to use context methods for calculating within a specific context. The methods are similar to those for the `Decimal` class and are only briefly recounted here.

abs(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.abs "Link to this definition")

Returns the absolute value of _x_.

add(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.add "Link to this definition")

Return the sum of _x_ and _y_.

canonical(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.canonical "Link to this definition")

Returns the same Decimal object _x_.

compare(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.compare "Link to this definition")

Compares _x_ and _y_ numerically.

compare_signal(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.compare_signal "Link to this definition")

Compares the values of the two operands numerically.

compare_total(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.compare_total "Link to this definition")

Compares two operands using their abstract representation.

compare_total_mag(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.compare_total_mag "Link to this definition")

Compares two operands using their abstract representation, ignoring sign.

copy_abs(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.copy_abs "Link to this definition")

Returns a copy of _x_ with the sign set to 0.

copy_negate(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.copy_negate "Link to this definition")

Returns a copy of _x_ with the sign inverted.

copy_sign(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.copy_sign "Link to this definition")

Copies the sign from _y_ to _x_.

divide(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.divide "Link to this definition")

Return _x_ divided by _y_.

divide_int(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.divide_int "Link to this definition")

Return _x_ divided by _y_ , truncated to an integer.

divmod(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.divmod "Link to this definition")

Divides two numbers and returns the integer part of the result.

exp(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.exp "Link to this definition")

Returns `e ** x`.

fma(_x_ , _y_ , _z_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.fma "Link to this definition")

Returns _x_ multiplied by _y_ , plus _z_.

is_canonical(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.is_canonical "Link to this definition")

Returns `True` if _x_ is canonical; otherwise returns `False`.

is_finite(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.is_finite "Link to this definition")

Returns `True` if _x_ is finite; otherwise returns `False`.

is_infinite(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.is_infinite "Link to this definition")

Returns `True` if _x_ is infinite; otherwise returns `False`.

is_nan(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.is_nan "Link to this definition")

Returns `True` if _x_ is a qNaN or sNaN; otherwise returns `False`.

is_normal(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.is_normal "Link to this definition")

Returns `True` if _x_ is a normal number; otherwise returns `False`.

is_qnan(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.is_qnan "Link to this definition")

Returns `True` if _x_ is a quiet NaN; otherwise returns `False`.

is_signed(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.is_signed "Link to this definition")

Returns `True` if _x_ is negative; otherwise returns `False`.

is_snan(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.is_snan "Link to this definition")

Returns `True` if _x_ is a signaling NaN; otherwise returns `False`.

is_subnormal(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.is_subnormal "Link to this definition")

Returns `True` if _x_ is subnormal; otherwise returns `False`.

is_zero(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.is_zero "Link to this definition")

Returns `True` if _x_ is a zero; otherwise returns `False`.

ln(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.ln "Link to this definition")

Returns the natural (base e) logarithm of _x_.

log10(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.log10 "Link to this definition")

Returns the base 10 logarithm of _x_.

logb(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.logb "Link to this definition")

Returns the exponent of the magnitude of the operand’s MSD.

logical_and(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.logical_and "Link to this definition")

Applies the logical operation _and_ between each operand’s digits.

logical_invert(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.logical_invert "Link to this definition")

Invert all the digits in _x_.

logical_or(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.logical_or "Link to this definition")

Applies the logical operation _or_ between each operand’s digits.

logical_xor(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.logical_xor "Link to this definition")

Applies the logical operation _xor_ between each operand’s digits.

max(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.max "Link to this definition")

Compares two values numerically and returns the maximum.

max_mag(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.max_mag "Link to this definition")

Compares the values numerically with their sign ignored.

min(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.min "Link to this definition")

Compares two values numerically and returns the minimum.

min_mag(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.min_mag "Link to this definition")

Compares the values numerically with their sign ignored.

minus(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.minus "Link to this definition")

Minus corresponds to the unary prefix minus operator in Python.

multiply(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.multiply "Link to this definition")

Return the product of _x_ and _y_.

next_minus(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.next_minus "Link to this definition")

Returns the largest representable number smaller than _x_.

next_plus(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.next_plus "Link to this definition")

Returns the smallest representable number larger than _x_.

next_toward(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.next_toward "Link to this definition")

Returns the number closest to _x_ , in direction towards _y_.

normalize(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.normalize "Link to this definition")

Reduces _x_ to its simplest form.

number_class(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.number_class "Link to this definition")

Returns an indication of the class of _x_.

plus(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.plus "Link to this definition")

Plus corresponds to the unary prefix plus operator in Python. This operation applies the context precision and rounding, so it is _not_ an identity operation.

power(_x_ , _y_ , _modulo =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.power "Link to this definition")

Return `x` to the power of `y`, reduced modulo `modulo` if given.
With two arguments, compute `x**y`. If `x` is negative then `y` must be integral. The result will be inexact unless `y` is integral and the result is finite and can be expressed exactly in ‘precision’ digits. The rounding mode of the context is used. Results are always correctly rounded in the Python version.
`Decimal(0) ** Decimal(0)` results in `InvalidOperation`, and if `InvalidOperation` is not trapped, then results in `Decimal('NaN')`.
Changed in version 3.3: The C module computes `power()` in terms of the correctly rounded [`exp()`](https://docs.python.org/3/library/decimal.html#decimal.Context.exp "decimal.Context.exp") and [`ln()`](https://docs.python.org/3/library/decimal.html#decimal.Context.ln "decimal.Context.ln") functions. The result is well-defined but only “almost always correctly rounded”.
With three arguments, compute `(x**y) % modulo`. For the three argument form, the following restrictions on the arguments hold:
  * all three arguments must be integral
  * `y` must be nonnegative
  * at least one of `x` or `y` must be nonzero
  * `modulo` must be nonzero and have at most ‘precision’ digits


The value resulting from `Context.power(x, y, modulo)` is equal to the value that would be obtained by computing `(x**y) % modulo` with unbounded precision, but is computed more efficiently. The exponent of the result is zero, regardless of the exponents of `x`, `y` and `modulo`. The result is always exact.

quantize(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.quantize "Link to this definition")

Returns a value equal to _x_ (rounded), having the exponent of _y_.

radix()[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.radix "Link to this definition")

Just returns 10, as this is Decimal, :)

remainder(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.remainder "Link to this definition")

Returns the remainder from integer division.
The sign of the result, if non-zero, is the same as that of the original dividend.

remainder_near(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.remainder_near "Link to this definition")

Returns `x - y * n`, where _n_ is the integer nearest the exact value of `x / y` (if the result is 0 then its sign will be the sign of _x_).

rotate(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.rotate "Link to this definition")

Returns a rotated copy of _x_ , _y_ times.

same_quantum(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.same_quantum "Link to this definition")

Returns `True` if the two operands have the same exponent.

scaleb(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.scaleb "Link to this definition")

Returns the first operand after adding the second value its exp.

shift(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.shift "Link to this definition")

Returns a shifted copy of _x_ , _y_ times.

sqrt(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.sqrt "Link to this definition")

Square root of a non-negative number to context precision.

subtract(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.subtract "Link to this definition")

Return the difference between _x_ and _y_.

to_eng_string(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.to_eng_string "Link to this definition")

Convert to a string, using engineering notation if an exponent is needed.
Engineering notation has an exponent which is a multiple of 3. This can leave up to 3 digits to the left of the decimal place and may require the addition of either one or two trailing zeros.

to_integral_exact(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.to_integral_exact "Link to this definition")

Rounds to an integer.

to_sci_string(_x_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Context.to_sci_string "Link to this definition")

Converts a number to a string using scientific notation.
