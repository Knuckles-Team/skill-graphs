Copy```
>>> Decimal(1).exp()
Decimal('2.718281828459045235360287471')
>>> Decimal(321).exp()
Decimal('2.561702493119680037517373933E+139')

```


_classmethod_ from_float(_f_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.from_float "Link to this definition")

Alternative constructor that only accepts instances of [`float`](https://docs.python.org/3/library/functions.html#float "float") or [`int`](https://docs.python.org/3/library/functions.html#int "int").
Note `Decimal.from_float(0.1)` is not the same as `Decimal('0.1')`. Since 0.1 is not exactly representable in binary floating point, the value is stored as the nearest representable value which is `0x1.999999999999ap-4`. That equivalent value in decimal is `0.1000000000000000055511151231257827021181583404541015625`.
Note
From Python 3.2 onwards, a `Decimal` instance can also be constructed directly from a [`float`](https://docs.python.org/3/library/functions.html#float "float").
Copy```
>>> Decimal.from_float(0.1)
Decimal('0.1000000000000000055511151231257827021181583404541015625')
>>> Decimal.from_float(float('nan'))
Decimal('NaN')
>>> Decimal.from_float(float('inf'))
Decimal('Infinity')
>>> Decimal.from_float(float('-inf'))
Decimal('-Infinity')

```

Added in version 3.1.

_classmethod_ from_number(_number_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.from_number "Link to this definition")

Alternative constructor that only accepts instances of [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`int`](https://docs.python.org/3/library/functions.html#int "int") or `Decimal`, but not strings or tuples.
Copy```
>>> Decimal.from_number(314)
Decimal('314')
>>> Decimal.from_number(0.1)
Decimal('0.1000000000000000055511151231257827021181583404541015625')
>>> Decimal.from_number(Decimal('3.14'))
Decimal('3.14')

```

Added in version 3.14.

fma(_other_ , _third_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.fma "Link to this definition")

Fused multiply-add. Return self*other+third with no rounding of the intermediate product self*other.
Copy```
>>> Decimal(2).fma(3, 5)
Decimal('11')

```


is_canonical()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.is_canonical "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the argument is canonical and [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise. Currently, a `Decimal` instance is always canonical, so this operation always returns `True`.

is_finite()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.is_finite "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the argument is a finite number, and [`False`](https://docs.python.org/3/library/constants.html#False "False") if the argument is an infinity or a NaN.

is_infinite()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.is_infinite "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the argument is either positive or negative infinity and [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise.

is_nan()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.is_nan "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the argument is a (quiet or signaling) NaN and [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise.

is_normal(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.is_normal "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the argument is a _normal_ finite number. Return [`False`](https://docs.python.org/3/library/constants.html#False "False") if the argument is zero, subnormal, infinite or a NaN.

is_qnan()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.is_qnan "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the argument is a quiet NaN, and [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise.

is_signed()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.is_signed "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the argument has a negative sign and [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise. Note that zeros and NaNs can both carry signs.

is_snan()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.is_snan "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the argument is a signaling NaN and [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise.

is_subnormal(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.is_subnormal "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the argument is subnormal, and [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise.

is_zero()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.is_zero "Link to this definition")

Return [`True`](https://docs.python.org/3/library/constants.html#True "True") if the argument is a (positive or negative) zero and [`False`](https://docs.python.org/3/library/constants.html#False "False") otherwise.

ln(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.ln "Link to this definition")

Return the natural (base e) logarithm of the operand. The result is correctly rounded using the [`ROUND_HALF_EVEN`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_HALF_EVEN "decimal.ROUND_HALF_EVEN") rounding mode.

log10(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.log10 "Link to this definition")

Return the base ten logarithm of the operand. The result is correctly rounded using the [`ROUND_HALF_EVEN`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_HALF_EVEN "decimal.ROUND_HALF_EVEN") rounding mode.

logb(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logb "Link to this definition")

For a nonzero number, return the adjusted exponent of its operand as a `Decimal` instance. If the operand is a zero then `Decimal('-Infinity')` is returned and the [`DivisionByZero`](https://docs.python.org/3/library/decimal.html#decimal.DivisionByZero "decimal.DivisionByZero") flag is raised. If the operand is an infinity then `Decimal('Infinity')` is returned.

logical_and(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_and "Link to this definition")

`logical_and()` is a logical operation which takes two _logical operands_ (see [Logical operands](https://docs.python.org/3/library/decimal.html#logical-operands-label)). The result is the digit-wise `and` of the two operands.

logical_invert(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_invert "Link to this definition")

`logical_invert()` is a logical operation. The result is the digit-wise inversion of the operand.

logical_or(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_or "Link to this definition")

`logical_or()` is a logical operation which takes two _logical operands_ (see [Logical operands](https://docs.python.org/3/library/decimal.html#logical-operands-label)). The result is the digit-wise `or` of the two operands.

logical_xor(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_xor "Link to this definition")

`logical_xor()` is a logical operation which takes two _logical operands_ (see [Logical operands](https://docs.python.org/3/library/decimal.html#logical-operands-label)). The result is the digit-wise exclusive or of the two operands.

max(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.max "Link to this definition")

Like `max(self, other)` except that the context rounding rule is applied before returning and that `NaN` values are either signaled or ignored (depending on the context and whether they are signaling or quiet).

max_mag(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.max_mag "Link to this definition")

Similar to the [`max()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.max "decimal.Decimal.max") method, but the comparison is done using the absolute values of the operands.

min(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.min "Link to this definition")

Like `min(self, other)` except that the context rounding rule is applied before returning and that `NaN` values are either signaled or ignored (depending on the context and whether they are signaling or quiet).

min_mag(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.min_mag "Link to this definition")

Similar to the [`min()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.min "decimal.Decimal.min") method, but the comparison is done using the absolute values of the operands.

next_minus(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.next_minus "Link to this definition")

Return the largest number representable in the given context (or in the current thread’s context if no context is given) that is smaller than the given operand.

next_plus(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.next_plus "Link to this definition")

Return the smallest number representable in the given context (or in the current thread’s context if no context is given) that is larger than the given operand.

next_toward(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.next_toward "Link to this definition")

If the two operands are unequal, return the number closest to the first operand in the direction of the second operand. If both operands are numerically equal, return a copy of the first operand with the sign set to be the same as the sign of the second operand.

normalize(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.normalize "Link to this definition")

Used for producing canonical values of an equivalence class within either the current context or the specified context.
This has the same semantics as the unary plus operation, except that if the final result is finite it is reduced to its simplest form, with all trailing zeros removed and its sign preserved. That is, while the coefficient is non-zero and a multiple of ten the coefficient is divided by ten and the exponent is incremented by 1. Otherwise (the coefficient is zero) the exponent is set to 0. In all cases the sign is unchanged.
For example, `Decimal('32.100')` and `Decimal('0.321000e+2')` both normalize to the equivalent value `Decimal('32.1')`.
Note that rounding is applied _before_ reducing to simplest form.
In the latest versions of the specification, this operation is also known as `reduce`.

number_class(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.number_class "Link to this definition")

Return a string describing the _class_ of the operand. The returned value is one of the following ten strings.
  * `"-Infinity"`, indicating that the operand is negative infinity.
  * `"-Normal"`, indicating that the operand is a negative normal number.
  * `"-Subnormal"`, indicating that the operand is negative and subnormal.
  * `"-Zero"`, indicating that the operand is a negative zero.
  * `"+Zero"`, indicating that the operand is a positive zero.
  * `"+Subnormal"`, indicating that the operand is positive and subnormal.
  * `"+Normal"`, indicating that the operand is a positive normal number.
  * `"+Infinity"`, indicating that the operand is positive infinity.
  * `"NaN"`, indicating that the operand is a quiet NaN (Not a Number).
  * `"sNaN"`, indicating that the operand is a signaling NaN.



quantize(_exp_ , _rounding =None_, _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.quantize "Link to this definition")

Return a value equal to the first operand after rounding and having the exponent of the second operand.
Copy```
>>> Decimal('1.41421356').quantize(Decimal('1.000'))
Decimal('1.414')

```

Unlike other operations, if the length of the coefficient after the quantize operation would be greater than precision, then an [`InvalidOperation`](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "decimal.InvalidOperation") is signaled. This guarantees that, unless there is an error condition, the quantized exponent is always equal to that of the right-hand operand.
Also unlike other operations, quantize never signals Underflow, even if the result is subnormal and inexact.
If the exponent of the second operand is larger than that of the first then rounding may be necessary. In this case, the rounding mode is determined by the `rounding` argument if given, else by the given `context` argument; if neither argument is given the rounding mode of the current thread’s context is used.
An error is returned whenever the resulting exponent is greater than [`Emax`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emax "decimal.Context.Emax") or less than [`Etiny()`](https://docs.python.org/3/library/decimal.html#decimal.Context.Etiny "decimal.Context.Etiny").

radix()[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.radix "Link to this definition")

Return `Decimal(10)`, the radix (base) in which the `Decimal` class does all its arithmetic. Included for compatibility with the specification.

remainder_near(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.remainder_near "Link to this definition")

Return the remainder from dividing _self_ by _other_. This differs from `self % other` in that the sign of the remainder is chosen so as to minimize its absolute value. More precisely, the return value is `self - n * other` where `n` is the integer nearest to the exact value of `self / other`, and if two integers are equally near then the even one is chosen.
If the result is zero then its sign will be the sign of _self_.
Copy```
>>> Decimal(18).remainder_near(Decimal(10))
Decimal('-2')
>>> Decimal(25).remainder_near(Decimal(10))
Decimal('5')
>>> Decimal(35).remainder_near(Decimal(10))
Decimal('-5')

```


rotate(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.rotate "Link to this definition")

Return the result of rotating the digits of the first operand by an amount specified by the second operand. The second operand must be an integer in the range -precision through precision. The absolute value of the second operand gives the number of places to rotate. If the second operand is positive then rotation is to the left; otherwise rotation is to the right. The coefficient of the first operand is padded on the left with zeros to length precision if necessary. The sign and exponent of the first operand are unchanged.

same_quantum(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.same_quantum "Link to this definition")

Test whether self and other have the same exponent or whether both are `NaN`.
This operation is unaffected by context and is quiet: no flags are changed and no rounding is performed. As an exception, the C version may raise InvalidOperation if the second operand cannot be converted exactly.

scaleb(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.scaleb "Link to this definition")

Return the first operand with exponent adjusted by the second. Equivalently, return the first operand multiplied by `10**other`. The second operand must be an integer.

shift(_other_ , _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.shift "Link to this definition")

Return the result of shifting the digits of the first operand by an amount specified by the second operand. The second operand must be an integer in the range -precision through precision. The absolute value of the second operand gives the number of places to shift. If the second operand is positive then the shift is to the left; otherwise the shift is to the right. Digits shifted into the coefficient are zeros. The sign and exponent of the first operand are unchanged.

sqrt(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.sqrt "Link to this definition")

Return the square root of the argument to full precision.

to_eng_string(_context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.to_eng_string "Link to this definition")

Convert to a string, using engineering notation if an exponent is needed.
Engineering notation has an exponent which is a multiple of 3. This can leave up to 3 digits to the left of the decimal place and may require the addition of either one or two trailing zeros.
For example, this converts `Decimal('123E+1')` to `Decimal('1.23E+3')`.

to_integral(_rounding =None_, _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.to_integral "Link to this definition")

Identical to the [`to_integral_value()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.to_integral_value "decimal.Decimal.to_integral_value") method. The `to_integral` name has been kept for compatibility with older versions.

to_integral_exact(_rounding =None_, _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.to_integral_exact "Link to this definition")

Round to the nearest integer, signaling [`Inexact`](https://docs.python.org/3/library/decimal.html#decimal.Inexact "decimal.Inexact") or [`Rounded`](https://docs.python.org/3/library/decimal.html#decimal.Rounded "decimal.Rounded") as appropriate if rounding occurs. The rounding mode is determined by the `rounding` parameter if given, else by the given `context`. If neither parameter is given then the rounding mode of the current context is used.

to_integral_value(_rounding =None_, _context =None_)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal.to_integral_value "Link to this definition")

Round to the nearest integer without signaling [`Inexact`](https://docs.python.org/3/library/decimal.html#decimal.Inexact "decimal.Inexact") or [`Rounded`](https://docs.python.org/3/library/decimal.html#decimal.Rounded "decimal.Rounded"). If given, applies _rounding_ ; otherwise, uses the rounding method in either the supplied _context_ or the current context.
Decimal numbers can be rounded using the [`round()`](https://docs.python.org/3/library/functions.html#round "round") function:

round(number)


round(number, ndigits)

If _ndigits_ is not given or `None`, returns the nearest [`int`](https://docs.python.org/3/library/functions.html#int "int") to _number_ , rounding ties to even, and ignoring the rounding mode of the `Decimal` context. Raises [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") if _number_ is an infinity or [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if it is a (quiet or signaling) NaN.
If _ndigits_ is an [`int`](https://docs.python.org/3/library/functions.html#int "int"), the context’s rounding mode is respected and a `Decimal` representing _number_ rounded to the nearest multiple of `Decimal('1E-ndigits')` is returned; in this case, `round(number, ndigits)` is equivalent to `self.quantize(Decimal('1E-ndigits'))`. Returns `Decimal('NaN')` if _number_ is a quiet NaN. Raises [`InvalidOperation`](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "decimal.InvalidOperation") if _number_ is an infinity, a signaling NaN, or if the length of the coefficient after the quantize operation would be greater than the current context’s precision. In other words, for the non-corner cases:
  * if _ndigits_ is positive, return _number_ rounded to _ndigits_ decimal places;
  * if _ndigits_ is zero, return _number_ rounded to the nearest integer;
  * if _ndigits_ is negative, return _number_ rounded to the nearest multiple of `10**abs(ndigits)`.


For example:
Copy```
>>> from decimal import Decimal, getcontext, ROUND_DOWN
>>> getcontext().rounding = ROUND_DOWN
>>> round(Decimal('3.75'))     # context rounding ignored
4
>>> round(Decimal('3.5'))      # round-ties-to-even
4
>>> round(Decimal('3.75'), 0)  # uses the context rounding
Decimal('3')
>>> round(Decimal('3.75'), 1)
Decimal('3.7')
>>> round(Decimal('3.75'), -1)
Decimal('0E+1')

```

### Logical operands[¶](https://docs.python.org/3/library/decimal.html#logical-operands "Link to this heading")
The [`logical_and()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_and "decimal.Decimal.logical_and"), [`logical_invert()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_invert "decimal.Decimal.logical_invert"), [`logical_or()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_or "decimal.Decimal.logical_or"), and [`logical_xor()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_xor "decimal.Decimal.logical_xor") methods expect their arguments to be _logical operands_. A _logical operand_ is a [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") instance whose exponent and sign are both zero, and whose digits are all either `0` or `1`.
## Context objects[¶](https://docs.python.org/3/library/decimal.html#context-objects "Link to this heading")
Contexts are environments for arithmetic operations. They govern precision, set rules for rounding, determine which signals are treated as exceptions, and limit the range for exponents.
Each thread has its own current context which is accessed or changed using the [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext") and [`setcontext()`](https://docs.python.org/3/library/decimal.html#decimal.setcontext "decimal.setcontext") functions:

decimal.getcontext()[¶](https://docs.python.org/3/library/decimal.html#decimal.getcontext "Link to this definition")

Return the current context for the active thread.

decimal.setcontext(_c_ , _/_)[¶](https://docs.python.org/3/library/decimal.html#decimal.setcontext "Link to this definition")

Set the current context for the active thread to _c_.
You can also use the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement and the [`localcontext()`](https://docs.python.org/3/library/decimal.html#decimal.localcontext "decimal.localcontext") function to temporarily change the active context.

decimal.localcontext(_ctx =None_, _** kwargs_)[¶](https://docs.python.org/3/library/decimal.html#decimal.localcontext "Link to this definition")

Return a context manager that will set the current context for the active thread to a copy of _ctx_ on entry to the with-statement and restore the previous context when exiting the with-statement. If no context is specified, a copy of the current context is used. The _kwargs_ argument is used to set the attributes of the new context.
For example, the following code sets the current decimal precision to 42 places, performs a calculation, and then automatically restores the previous context:
Copy```
from decimal import localcontext

with localcontext() as ctx:
    ctx.prec = 42   # Perform a high precision calculation
    s = calculate_something()
s = +s  # Round the final result back to the default precision

```

Using keyword arguments, the code would be the following:
Copy```
from decimal import localcontext

with localcontext(prec=42) as ctx:
    s = calculate_something()
s = +s

```

Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if _kwargs_ supplies an attribute that [`Context`](https://docs.python.org/3/library/decimal.html#decimal.Context "decimal.Context") doesn’t support. Raises either `TypeError` or [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if _kwargs_ supplies an invalid value for an attribute.
Changed in version 3.11: [`localcontext()`](https://docs.python.org/3/library/decimal.html#decimal.localcontext "decimal.localcontext") now supports setting context attributes through the use of keyword arguments.

decimal.IEEEContext(_bits_)[¶](https://docs.python.org/3/library/decimal.html#decimal.IEEEContext "Link to this definition")

Return a context object initialized to the proper values for one of the IEEE interchange formats. The argument must be a multiple of 32 and less than [`IEEE_CONTEXT_MAX_BITS`](https://docs.python.org/3/library/decimal.html#decimal.IEEE_CONTEXT_MAX_BITS "decimal.IEEE_CONTEXT_MAX_BITS").
