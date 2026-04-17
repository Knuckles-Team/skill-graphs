## Signals[¶](https://docs.python.org/3/library/decimal.html#signals "Link to this heading")
Signals represent conditions that arise during computation. Each corresponds to one context flag and one context trap enabler.
The context flag is set whenever the condition is encountered. After the computation, flags may be checked for informational purposes (for instance, to determine whether a computation was exact). After checking the flags, be sure to clear all flags before starting the next computation.
If the context’s trap enabler is set for the signal, then the condition causes a Python exception to be raised. For example, if the [`DivisionByZero`](https://docs.python.org/3/library/decimal.html#decimal.DivisionByZero "decimal.DivisionByZero") trap is set, then a [`DivisionByZero`](https://docs.python.org/3/library/decimal.html#decimal.DivisionByZero "decimal.DivisionByZero") exception is raised upon encountering the condition.

_class_ decimal.Clamped[¶](https://docs.python.org/3/library/decimal.html#decimal.Clamped "Link to this definition")

Altered an exponent to fit representation constraints.
Typically, clamping occurs when an exponent falls outside the context’s [`Emin`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emin "decimal.Context.Emin") and [`Emax`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emax "decimal.Context.Emax") limits. If possible, the exponent is reduced to fit by adding zeros to the coefficient.

_class_ decimal.DecimalException[¶](https://docs.python.org/3/library/decimal.html#decimal.DecimalException "Link to this definition")

Base class for other signals and a subclass of [`ArithmeticError`](https://docs.python.org/3/library/exceptions.html#ArithmeticError "ArithmeticError").

_class_ decimal.DivisionByZero[¶](https://docs.python.org/3/library/decimal.html#decimal.DivisionByZero "Link to this definition")

Signals the division of a non-infinite number by zero.
Can occur with division, modulo division, or when raising a number to a negative power. If this signal is not trapped, returns `Infinity` or `-Infinity` with the sign determined by the inputs to the calculation.

_class_ decimal.Inexact[¶](https://docs.python.org/3/library/decimal.html#decimal.Inexact "Link to this definition")

Indicates that rounding occurred and the result is not exact.
Signals when non-zero digits were discarded during rounding. The rounded result is returned. The signal flag or trap is used to detect when results are inexact.

_class_ decimal.InvalidOperation[¶](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "Link to this definition")

An invalid operation was performed.
Indicates that an operation was requested that does not make sense. If not trapped, returns `NaN`. Possible causes include:
Copy```
Infinity - Infinity
0 * Infinity
Infinity / Infinity
x % 0
Infinity % x
sqrt(-x) and x > 0
0 ** 0
x ** (non-integer)
x ** Infinity

```


_class_ decimal.Overflow[¶](https://docs.python.org/3/library/decimal.html#decimal.Overflow "Link to this definition")

Numerical overflow.
Indicates the exponent is larger than [`Context.Emax`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emax "decimal.Context.Emax") after rounding has occurred. If not trapped, the result depends on the rounding mode, either pulling inward to the largest representable finite number or rounding outward to `Infinity`. In either case, [`Inexact`](https://docs.python.org/3/library/decimal.html#decimal.Inexact "decimal.Inexact") and [`Rounded`](https://docs.python.org/3/library/decimal.html#decimal.Rounded "decimal.Rounded") are also signaled.

_class_ decimal.Rounded[¶](https://docs.python.org/3/library/decimal.html#decimal.Rounded "Link to this definition")

Rounding occurred though possibly no information was lost.
Signaled whenever rounding discards digits; even if those digits are zero (such as rounding `5.00` to `5.0`). If not trapped, returns the result unchanged. This signal is used to detect loss of significant digits.

_class_ decimal.Subnormal[¶](https://docs.python.org/3/library/decimal.html#decimal.Subnormal "Link to this definition")

Exponent was lower than [`Emin`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emin "decimal.Context.Emin") prior to rounding.
Occurs when an operation result is subnormal (the exponent is too small). If not trapped, returns the result unchanged.

_class_ decimal.Underflow[¶](https://docs.python.org/3/library/decimal.html#decimal.Underflow "Link to this definition")

Numerical underflow with result rounded to zero.
Occurs when a subnormal result is pushed to zero by rounding. [`Inexact`](https://docs.python.org/3/library/decimal.html#decimal.Inexact "decimal.Inexact") and [`Subnormal`](https://docs.python.org/3/library/decimal.html#decimal.Subnormal "decimal.Subnormal") are also signaled.

_class_ decimal.FloatOperation[¶](https://docs.python.org/3/library/decimal.html#decimal.FloatOperation "Link to this definition")

Enable stricter semantics for mixing floats and Decimals.
If the signal is not trapped (default), mixing floats and Decimals is permitted in the [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") constructor, [`create_decimal()`](https://docs.python.org/3/library/decimal.html#decimal.Context.create_decimal "decimal.Context.create_decimal") and all comparison operators. Both conversion and comparisons are exact. Any occurrence of a mixed operation is silently recorded by setting `FloatOperation` in the context flags. Explicit conversions with [`from_float()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.from_float "decimal.Decimal.from_float") or [`create_decimal_from_float()`](https://docs.python.org/3/library/decimal.html#decimal.Context.create_decimal_from_float "decimal.Context.create_decimal_from_float") do not set the flag.
Otherwise (the signal is trapped), only equality comparisons and explicit conversions are silent. All other mixed operations raise `FloatOperation`.
The following table summarizes the hierarchy of signals:
Copy```
exceptions.ArithmeticError(exceptions.Exception)
    DecimalException
        Clamped
        DivisionByZero(DecimalException, exceptions.ZeroDivisionError)
        Inexact
            Overflow(Inexact, Rounded)
            Underflow(Inexact, Rounded, Subnormal)
        InvalidOperation
        Rounded
        Subnormal
        FloatOperation(DecimalException, exceptions.TypeError)

```
