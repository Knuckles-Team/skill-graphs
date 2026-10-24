## Recipes[¶](https://docs.python.org/3/library/decimal.html#recipes "Link to this heading")
Here are a few recipes that serve as utility functions and that demonstrate ways to work with the [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") class:
Copy```
def moneyfmt(value, places=2, curr='', sep=',', dp='.',
             pos='', neg='-', trailneg=''):
    """Convert Decimal to a money formatted string.

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank

    >>> d = Decimal('-1234567.8901')
    >>> moneyfmt(d, curr='$')
    '-$1,234,567.89'
    >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
    '1.234.568-'
    >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
    '($1,234,567.89)'
    >>> moneyfmt(Decimal(123456789), sep=' ')
    '123 456 789.00'
    >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
    '<0.02>'

    """
    q = Decimal(10) ** -places      # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = list(map(str, digits))
    build, next = result.append, digits.pop
    if sign:
        build(trailneg)
    for i in range(places):
        build(next() if digits else '0')
    if places:
        build(dp)
    if not digits:
        build('0')
    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return ''.join(reversed(result))

def pi():
    """Compute Pi to the current precision.

    >>> print(pi())
    3.141592653589793238462643383

    """
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s               # unary plus applies the new precision

def exp(x):
    """Return e raised to the power of x.  Result type matches input type.

    >>> print(exp(Decimal(1)))
    2.718281828459045235360287471
    >>> print(exp(Decimal(2)))
    7.389056098930650227230427461
    >>> print(exp(2.0))
    7.38905609893
    >>> print(exp(2+0j))
    (7.38905609893+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x
        s += num / fact
    getcontext().prec -= 2
    return +s

def cos(x):
    """Return the cosine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(cos(Decimal('0.5')))
    0.8775825618903727161162815826
    >>> print(cos(0.5))
    0.87758256189
    >>> print(cos(0.5+0j))
    (0.87758256189+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def sin(x):
    """Return the sine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(sin(Decimal('0.5')))
    0.4794255386042030002732879352
    >>> print(sin(0.5))
    0.479425538604
    >>> print(sin(0.5+0j))
    (0.479425538604+0j)

    """
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

```

## Decimal FAQ[¶](https://docs.python.org/3/library/decimal.html#decimal-faq "Link to this heading")
Q: It is cumbersome to type `decimal.Decimal('1234.5')`. Is there a way to minimize typing when using the interactive interpreter?
A: Some users abbreviate the constructor to just a single letter:
Copy```
>>> D = decimal.Decimal
>>> D('1.23') + D('3.45')
Decimal('4.68')

```

Q: In a fixed-point application with two decimal places, some inputs have many places and need to be rounded. Others are not supposed to have excess digits and need to be validated. What methods should be used?
A: The [`quantize()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.quantize "decimal.Decimal.quantize") method rounds to a fixed number of decimal places. If the [`Inexact`](https://docs.python.org/3/library/decimal.html#decimal.Inexact "decimal.Inexact") trap is set, it is also useful for validation:
Copy```
>>> TWOPLACES = Decimal(10) ** -2       # same as Decimal('0.01')

```

Copy```
>>> # Round to two places
>>> Decimal('3.214').quantize(TWOPLACES)
Decimal('3.21')

```

Copy```
>>> # Validate that a number does not exceed two places
>>> Decimal('3.21').quantize(TWOPLACES, context=Context(traps=[Inexact]))
Decimal('3.21')

```

Copy```
>>> Decimal('3.214').quantize(TWOPLACES, context=Context(traps=[Inexact]))
Traceback (most recent call last):
   ...
Inexact: None

```

Q: Once I have valid two place inputs, how do I maintain that invariant throughout an application?
A: Some operations like addition, subtraction, and multiplication by an integer will automatically preserve fixed point. Others operations, like division and non-integer multiplication, will change the number of decimal places and need to be followed-up with a [`quantize()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.quantize "decimal.Decimal.quantize") step:
Copy```
>>> a = Decimal('102.72')           # Initial fixed-point values
>>> b = Decimal('3.17')
>>> a + b                           # Addition preserves fixed-point
Decimal('105.89')
>>> a - b
Decimal('99.55')
>>> a * 42                          # So does integer multiplication
Decimal('4314.24')
>>> (a * b).quantize(TWOPLACES)     # Must quantize non-integer multiplication
Decimal('325.62')
>>> (b / a).quantize(TWOPLACES)     # And quantize division
Decimal('0.03')

```

In developing fixed-point applications, it is convenient to define functions to handle the [`quantize()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.quantize "decimal.Decimal.quantize") step:
Copy```
>>> def mul(x, y, fp=TWOPLACES):
...     return (x * y).quantize(fp)
...
>>> def div(x, y, fp=TWOPLACES):
...     return (x / y).quantize(fp)

```

Copy```
>>> mul(a, b)                       # Automatically preserve fixed-point
Decimal('325.62')
>>> div(b, a)
Decimal('0.03')

```

Q: There are many ways to express the same value. The numbers `200`, `200.000`, `2E2`, and `.02E+4` all have the same value at various precisions. Is there a way to transform them to a single recognizable canonical value?
A: The [`normalize()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.normalize "decimal.Decimal.normalize") method maps all equivalent values to a single representative:
Copy```
>>> values = map(Decimal, '200 200.000 2E2 .02E+4'.split())
>>> [v.normalize() for v in values]
[Decimal('2E+2'), Decimal('2E+2'), Decimal('2E+2'), Decimal('2E+2')]

```

Q: When does rounding occur in a computation?
A: It occurs _after_ the computation. The philosophy of the decimal specification is that numbers are considered exact and are created independent of the current context. They can even have greater precision than current context. Computations process with those exact inputs and then rounding (or other context operations) is applied to the _result_ of the computation:
Copy```
>>> getcontext().prec = 5
>>> pi = Decimal('3.1415926535')   # More than 5 digits
>>> pi                             # All digits are retained
Decimal('3.1415926535')
>>> pi + 0                         # Rounded after an addition
Decimal('3.1416')
>>> pi - Decimal('0.00005')        # Subtract unrounded numbers, then round
Decimal('3.1415')
>>> pi + 0 - Decimal('0.00005').   # Intermediate values are rounded
Decimal('3.1416')

```

Q: Some decimal values always print with exponential notation. Is there a way to get a non-exponential representation?
A: For some values, exponential notation is the only way to express the number of significant places in the coefficient. For example, expressing `5.0E+3` as `5000` keeps the value constant but cannot show the original’s two-place significance.
If an application does not care about tracking significance, it is easy to remove the exponent and trailing zeroes, losing significance, but keeping the value unchanged:
Copy```
>>> def remove_exponent(d):
...     return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

```

Copy```
>>> remove_exponent(Decimal('5E+3'))
Decimal('5000')

```

Q: Is there a way to convert a regular float to a [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")?
A: Yes, any binary floating-point number can be exactly expressed as a Decimal though an exact conversion may take more precision than intuition would suggest:
Copy```
>>> Decimal(math.pi)
Decimal('3.141592653589793115997963468544185161590576171875')

```

Q: Within a complex calculation, how can I make sure that I haven’t gotten a spurious result because of insufficient precision or rounding anomalies.
A: The decimal module makes it easy to test results. A best practice is to re-run calculations using greater precision and with various rounding modes. Widely differing results indicate insufficient precision, rounding mode issues, ill-conditioned inputs, or a numerically unstable algorithm.
Q: I noticed that context precision is applied to the results of operations but not to the inputs. Is there anything to watch out for when mixing values of different precisions?
A: Yes. The principle is that all values are considered to be exact and so is the arithmetic on those values. Only the results are rounded. The advantage for inputs is that “what you type is what you get”. A disadvantage is that the results can look odd if you forget that the inputs haven’t been rounded:
Copy```
>>> getcontext().prec = 3
>>> Decimal('3.104') + Decimal('2.104')
Decimal('5.21')
>>> Decimal('3.104') + Decimal('0.000') + Decimal('2.104')
Decimal('5.20')

```

The solution is either to increase precision or to force rounding of inputs using the unary plus operation:
Copy```
>>> getcontext().prec = 3
>>> +Decimal('1.23456789')      # unary plus triggers rounding
Decimal('1.23')

```

Alternatively, inputs can be rounded upon creation using the [`Context.create_decimal()`](https://docs.python.org/3/library/decimal.html#decimal.Context.create_decimal "decimal.Context.create_decimal") method:
Copy```
>>> Context(prec=5, rounding=ROUND_DOWN).create_decimal('1.2345678')
Decimal('1.2345')

```

Q: Is the CPython implementation fast for large numbers?
A: Yes. In the CPython and PyPy3 implementations, the C/CFFI versions of the decimal module integrate the high speed [[1]](https://docs.python.org/3/library/decimal.html#id4). `libmpdec` uses
The context must be adapted for exact arbitrary precision arithmetic. [`Emin`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emin "decimal.Context.Emin") and [`Emax`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emax "decimal.Context.Emax") should always be set to the maximum values, [`clamp`](https://docs.python.org/3/library/decimal.html#decimal.Context.clamp "decimal.Context.clamp") should always be 0 (the default). Setting [`prec`](https://docs.python.org/3/library/decimal.html#decimal.Context.prec "decimal.Context.prec") requires some care.
The easiest approach for trying out bignum arithmetic is to use the maximum value for [`prec`](https://docs.python.org/3/library/decimal.html#decimal.Context.prec "decimal.Context.prec") as well [[2]](https://docs.python.org/3/library/decimal.html#id5):
Copy```
>>> setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX, Emin=MIN_EMIN))
>>> x = Decimal(2) ** 256
>>> x / 128
Decimal('904625697166532776746648320380374280103671755200316906558262375061821325312')

```

For inexact results, [`MAX_PREC`](https://docs.python.org/3/library/decimal.html#decimal.MAX_PREC "decimal.MAX_PREC") is far too large on 64-bit platforms and the available memory will be insufficient:
Copy```
>>> Decimal(1) / 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
MemoryError

```

On systems with overallocation (e.g. Linux), a more sophisticated approach is to adjust [`prec`](https://docs.python.org/3/library/decimal.html#decimal.Context.prec "decimal.Context.prec") to the amount of available RAM. Suppose that you have 8GB of RAM and expect 10 simultaneous operands using a maximum of 500MB each:
Copy```
>>> import sys
>>>
>>> # Maximum number of digits for a single operand using 500MB in 8-byte words
>>> # with 19 digits per word (4-byte and 9 digits for the 32-bit build):
>>> maxdigits = 19 * ((500 * 1024**2) // 8)
>>>
>>> # Check that this works:
>>> c = Context(prec=maxdigits, Emax=MAX_EMAX, Emin=MIN_EMIN)
>>> c.traps[Inexact] = True
>>> setcontext(c)
>>>
>>> # Fill the available precision with nines:
>>> x = Decimal(0).logical_invert() * 9
>>> sys.getsizeof(x)
524288112
>>> x + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  decimal.Inexact: [<class 'decimal.Inexact'>]

```

In general (and especially on systems without overallocation), it is recommended to estimate even tighter bounds and set the [`Inexact`](https://docs.python.org/3/library/decimal.html#decimal.Inexact "decimal.Inexact") trap if all calculations are expected to be exact.
[[1](https://docs.python.org/3/library/decimal.html#id2)]
Added in version 3.3.
[[2](https://docs.python.org/3/library/decimal.html#id3)]
Changed in version 3.9: This approach now works for all exact results except for non-integer powers.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`decimal` — Decimal fixed-point and floating-point arithmetic](https://docs.python.org/3/library/decimal.html)
    * [Quick-start tutorial](https://docs.python.org/3/library/decimal.html#quick-start-tutorial)
    * [Decimal objects](https://docs.python.org/3/library/decimal.html#decimal-objects)
      * [Logical operands](https://docs.python.org/3/library/decimal.html#logical-operands)
    * [Context objects](https://docs.python.org/3/library/decimal.html#context-objects)
    * [Constants](https://docs.python.org/3/library/decimal.html#constants)
    * [Rounding modes](https://docs.python.org/3/library/decimal.html#rounding-modes)
    * [Signals](https://docs.python.org/3/library/decimal.html#signals)
    * [Floating-point notes](https://docs.python.org/3/library/decimal.html#floating-point-notes)
      * [Mitigating round-off error with increased precision](https://docs.python.org/3/library/decimal.html#mitigating-round-off-error-with-increased-precision)
      * [Special values](https://docs.python.org/3/library/decimal.html#special-values)
    * [Working with threads](https://docs.python.org/3/library/decimal.html#working-with-threads)
    * [Recipes](https://docs.python.org/3/library/decimal.html#recipes)
    * [Decimal FAQ](https://docs.python.org/3/library/decimal.html#decimal-faq)


#### Previous topic
[`cmath` — Mathematical functions for complex numbers](https://docs.python.org/3/library/cmath.html "previous chapter")
#### Next topic
[`fractions` — Rational numbers](https://docs.python.org/3/library/fractions.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=decimal+%E2%80%94+Decimal+fixed-point+and+floating-point+arithmetic&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdecimal.html&pagesource=library%2Fdecimal.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/fractions.html "fractions — Rational numbers") |
  * [previous](https://docs.python.org/3/library/cmath.html "cmath — Mathematical functions for complex numbers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html) »
  * [`decimal` — Decimal fixed-point and floating-point arithmetic](https://docs.python.org/3/library/decimal.html)
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
