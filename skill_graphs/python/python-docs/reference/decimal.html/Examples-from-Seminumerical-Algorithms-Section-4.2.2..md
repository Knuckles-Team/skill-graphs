# Examples from Seminumerical Algorithms, Section 4.2.2.
>>> from decimal import Decimal, getcontext
>>> getcontext().prec = 8

>>> u, v, w = Decimal(11111113), Decimal(-11111111), Decimal('7.51111111')
>>> (u + v) + w
Decimal('9.5111111')
>>> u + (v + w)
Decimal('10')

>>> u, v, w = Decimal(20000), Decimal(-6), Decimal('6.0000003')
>>> (u*v) + (u*w)
Decimal('0.01')
>>> u * (v+w)
Decimal('0.0060000')

```

The `decimal` module makes it possible to restore the identities by expanding the precision sufficiently to avoid loss of significance:
Copy```
>>> getcontext().prec = 20
>>> u, v, w = Decimal(11111113), Decimal(-11111111), Decimal('7.51111111')
>>> (u + v) + w
Decimal('9.51111111')
>>> u + (v + w)
Decimal('9.51111111')
>>>
>>> u, v, w = Decimal(20000), Decimal(-6), Decimal('6.0000003')
>>> (u*v) + (u*w)
Decimal('0.0060000')
>>> u * (v+w)
Decimal('0.0060000')

```

### Special values[¶](https://docs.python.org/3/library/decimal.html#special-values "Link to this heading")
The number system for the `decimal` module provides special values including `NaN`, `sNaN`, `-Infinity`, `Infinity`, and two zeros, `+0` and `-0`.
Infinities can be constructed directly with: `Decimal('Infinity')`. Also, they can arise from dividing by zero when the [`DivisionByZero`](https://docs.python.org/3/library/decimal.html#decimal.DivisionByZero "decimal.DivisionByZero") signal is not trapped. Likewise, when the [`Overflow`](https://docs.python.org/3/library/decimal.html#decimal.Overflow "decimal.Overflow") signal is not trapped, infinity can result from rounding beyond the limits of the largest representable number.
The infinities are signed (affine) and can be used in arithmetic operations where they get treated as very large, indeterminate numbers. For instance, adding a constant to infinity gives another infinite result.
Some operations are indeterminate and return `NaN`, or if the [`InvalidOperation`](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "decimal.InvalidOperation") signal is trapped, raise an exception. For example, `0/0` returns `NaN` which means “not a number”. This variety of `NaN` is quiet and, once created, will flow through other computations always resulting in another `NaN`. This behavior can be useful for a series of computations that occasionally have missing inputs — it allows the calculation to proceed while flagging specific results as invalid.
A variant is `sNaN` which signals rather than remaining quiet after every operation. This is a useful return value when an invalid result needs to interrupt a calculation for special handling.
The behavior of Python’s comparison operators can be a little surprising where a `NaN` is involved. A test for equality where one of the operands is a quiet or signaling `NaN` always returns [`False`](https://docs.python.org/3/library/constants.html#False "False") (even when doing `Decimal('NaN')==Decimal('NaN')`), while a test for inequality always returns [`True`](https://docs.python.org/3/library/constants.html#True "True"). An attempt to compare two Decimals using any of the `<`, `<=`, `>` or `>=` operators will raise the [`InvalidOperation`](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "decimal.InvalidOperation") signal if either operand is a `NaN`, and return `False` if this signal is not trapped. Note that the General Decimal Arithmetic specification does not specify the behavior of direct comparisons; these rules for comparisons involving a `NaN` were taken from the IEEE 854 standard (see Table 3 in section 5.7). To ensure strict standards-compliance, use the [`compare()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.compare "decimal.Decimal.compare") and [`compare_signal()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.compare_signal "decimal.Decimal.compare_signal") methods instead.
The signed zeros can result from calculations that underflow. They keep the sign that would have resulted if the calculation had been carried out to greater precision. Since their magnitude is zero, both positive and negative zeros are treated as equal and their sign is informational.
In addition to the two signed zeros which are distinct yet equal, there are various representations of zero with differing precisions yet equivalent in value. This takes a bit of getting used to. For an eye accustomed to normalized floating-point representations, it is not immediately obvious that the following calculation returns a value equal to zero:
Copy```
>>> 1 / Decimal('Infinity')
Decimal('0E-1000026')

```

## Working with threads[¶](https://docs.python.org/3/library/decimal.html#working-with-threads "Link to this heading")
The [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext") function accesses a different [`Context`](https://docs.python.org/3/library/decimal.html#decimal.Context "decimal.Context") object for each thread. Having separate thread contexts means that threads may make changes (such as `getcontext().prec=10`) without interfering with other threads.
Likewise, the [`setcontext()`](https://docs.python.org/3/library/decimal.html#decimal.setcontext "decimal.setcontext") function automatically assigns its target to the current thread.
If [`setcontext()`](https://docs.python.org/3/library/decimal.html#decimal.setcontext "decimal.setcontext") has not been called before [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext"), then `getcontext()` will automatically create a new context for use in the current thread. New context objects have default values set from the [`decimal.DefaultContext`](https://docs.python.org/3/library/decimal.html#decimal.DefaultContext "decimal.DefaultContext") object.
The [`sys.flags.thread_inherit_context`](https://docs.python.org/3/library/sys.html#sys.flags.thread_inherit_context "sys.flags.thread_inherit_context") flag affects the context for new threads. If the flag is false, new threads will start with an empty context. In this case, [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext") will create a new context object when called and use the default values from _DefaultContext_. If the flag is true, new threads will start with a copy of context from the caller of [`threading.Thread.start()`](https://docs.python.org/3/library/threading.html#threading.Thread.start "threading.Thread.start").
To control the defaults so that each thread will use the same values throughout the application, directly modify the _DefaultContext_ object. This should be done _before_ any threads are started so that there won’t be a race condition between threads calling [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext"). For example:
Copy```
# Set applicationwide defaults for all threads about to be launched
DefaultContext.prec = 12
DefaultContext.rounding = ROUND_DOWN
DefaultContext.traps = ExtendedContext.traps.copy()
DefaultContext.traps[InvalidOperation] = 1
setcontext(DefaultContext)

# Afterwards, the threads can be started
t1.start()
t2.start()
t3.start()
 . . .

```
