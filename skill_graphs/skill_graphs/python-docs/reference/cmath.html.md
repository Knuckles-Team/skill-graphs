[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`cmath` — Mathematical functions for complex numbers](https://docs.python.org/3/library/cmath.html)
    * [Conversions to and from polar coordinates](https://docs.python.org/3/library/cmath.html#conversions-to-and-from-polar-coordinates)
    * [Power and logarithmic functions](https://docs.python.org/3/library/cmath.html#power-and-logarithmic-functions)
    * [Trigonometric functions](https://docs.python.org/3/library/cmath.html#trigonometric-functions)
    * [Hyperbolic functions](https://docs.python.org/3/library/cmath.html#hyperbolic-functions)
    * [Classification functions](https://docs.python.org/3/library/cmath.html#classification-functions)
    * [Constants](https://docs.python.org/3/library/cmath.html#constants)


#### Previous topic
[`math` — Mathematical functions](https://docs.python.org/3/library/math.html "previous chapter")
#### Next topic
[`decimal` — Decimal fixed-point and floating-point arithmetic](https://docs.python.org/3/library/decimal.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=cmath+%E2%80%94+Mathematical+functions+for+complex+numbers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcmath.html&pagesource=library%2Fcmath.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/decimal.html "decimal — Decimal fixed-point and floating-point arithmetic") |
  * [previous](https://docs.python.org/3/library/math.html "math — Mathematical functions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html) »
  * [`cmath` — Mathematical functions for complex numbers](https://docs.python.org/3/library/cmath.html)
  * |
  * Theme  Auto Light Dark |


#  `cmath` — Mathematical functions for complex numbers[¶](https://docs.python.org/3/library/cmath.html#module-cmath "Link to this heading")
* * *
This module provides access to mathematical functions for complex numbers. The functions in this module accept integers, floating-point numbers or complex numbers as arguments. They will also accept any Python object that has either a [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__") or a [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__") method: these methods are used to convert the object to a complex or floating-point number, respectively, and the function is then applied to the result of the conversion.
Note
For functions involving branch cuts, we have the problem of deciding how to define those functions on the cut itself. Following Kahan’s “Branch cuts for complex elementary functions” paper, as well as Annex G of C99 and later C standards, we use the sign of zero to distinguish one side of the branch cut from the other: for a branch cut along (a portion of) the real axis we look at the sign of the imaginary part, while for a branch cut along the imaginary axis we look at the sign of the real part.
For example, the [`cmath.sqrt()`](https://docs.python.org/3/library/cmath.html#cmath.sqrt "cmath.sqrt") function has a branch cut along the negative real axis. An argument of `-2-0j` is treated as though it lies _below_ the branch cut, and so gives a result on the negative imaginary axis:
Copy```
>>> cmath.sqrt(-2-0j)
-1.4142135623730951j

```

But an argument of `-2+0j` is treated as though it lies above the branch cut:
Copy```
>>> cmath.sqrt(-2+0j)
1.4142135623730951j

```

**Conversions to and from polar coordinates**
---
[`phase(z)`](https://docs.python.org/3/library/cmath.html#cmath.phase "cmath.phase") | Return the phase of _z_
[`polar(z)`](https://docs.python.org/3/library/cmath.html#cmath.polar "cmath.polar") | Return the representation of _z_ in polar coordinates
[`rect(r, phi)`](https://docs.python.org/3/library/cmath.html#cmath.rect "cmath.rect") | Return the complex number _z_ with polar coordinates _r_ and _phi_
**Power and logarithmic functions**
[`exp(z)`](https://docs.python.org/3/library/cmath.html#cmath.exp "cmath.exp") | Return _e_ raised to the power _z_
[`log(z[, base])`](https://docs.python.org/3/library/cmath.html#cmath.log "cmath.log") | Return the logarithm of _z_ to the given _base_ (_e_ by default)
[`log10(z)`](https://docs.python.org/3/library/cmath.html#cmath.log10 "cmath.log10") | Return the base-10 logarithm of _z_
[`sqrt(z)`](https://docs.python.org/3/library/cmath.html#cmath.sqrt "cmath.sqrt") | Return the square root of _z_
**Trigonometric functions**
[`acos(z)`](https://docs.python.org/3/library/cmath.html#cmath.acos "cmath.acos") | Return the arc cosine of _z_
[`asin(z)`](https://docs.python.org/3/library/cmath.html#cmath.asin "cmath.asin") | Return the arc sine of _z_
[`atan(z)`](https://docs.python.org/3/library/cmath.html#cmath.atan "cmath.atan") | Return the arc tangent of _z_
[`cos(z)`](https://docs.python.org/3/library/cmath.html#cmath.cos "cmath.cos") | Return the cosine of _z_
[`sin(z)`](https://docs.python.org/3/library/cmath.html#cmath.sin "cmath.sin") | Return the sine of _z_
[`tan(z)`](https://docs.python.org/3/library/cmath.html#cmath.tan "cmath.tan") | Return the tangent of _z_
**Hyperbolic functions**
[`acosh(z)`](https://docs.python.org/3/library/cmath.html#cmath.acosh "cmath.acosh") | Return the inverse hyperbolic cosine of _z_
[`asinh(z)`](https://docs.python.org/3/library/cmath.html#cmath.asinh "cmath.asinh") | Return the inverse hyperbolic sine of _z_
[`atanh(z)`](https://docs.python.org/3/library/cmath.html#cmath.atanh "cmath.atanh") | Return the inverse hyperbolic tangent of _z_
[`cosh(z)`](https://docs.python.org/3/library/cmath.html#cmath.cosh "cmath.cosh") | Return the hyperbolic cosine of _z_
[`sinh(z)`](https://docs.python.org/3/library/cmath.html#cmath.sinh "cmath.sinh") | Return the hyperbolic sine of _z_
[`tanh(z)`](https://docs.python.org/3/library/cmath.html#cmath.tanh "cmath.tanh") | Return the hyperbolic tangent of _z_
**Classification functions**
[`isfinite(z)`](https://docs.python.org/3/library/cmath.html#cmath.isfinite "cmath.isfinite") | Check if all components of _z_ are finite
[`isinf(z)`](https://docs.python.org/3/library/cmath.html#cmath.isinf "cmath.isinf") | Check if any component of _z_ is infinite
[`isnan(z)`](https://docs.python.org/3/library/cmath.html#cmath.isnan "cmath.isnan") | Check if any component of _z_ is a NaN
[`isclose(a, b, *, rel_tol, abs_tol)`](https://docs.python.org/3/library/cmath.html#cmath.isclose "cmath.isclose") | Check if the values _a_ and _b_ are close to each other
**Constants**
[`pi`](https://docs.python.org/3/library/cmath.html#cmath.pi "cmath.pi") | _π_ = 3.141592…
[`e`](https://docs.python.org/3/library/cmath.html#cmath.e "cmath.e") | _e_ = 2.718281…
[`tau`](https://docs.python.org/3/library/cmath.html#cmath.tau "cmath.tau") | _τ_ = 2 _π_ = 6.283185…
[`inf`](https://docs.python.org/3/library/cmath.html#cmath.inf "cmath.inf") | Positive infinity
[`infj`](https://docs.python.org/3/library/cmath.html#cmath.infj "cmath.infj") | Pure imaginary infinity
[`nan`](https://docs.python.org/3/library/cmath.html#cmath.nan "cmath.nan") | “Not a number” (NaN)
[`nanj`](https://docs.python.org/3/library/cmath.html#cmath.nanj "cmath.nanj") | Pure imaginary NaN
## Conversions to and from polar coordinates[¶](https://docs.python.org/3/library/cmath.html#conversions-to-and-from-polar-coordinates "Link to this heading")
A Python complex number `z` is stored internally using _rectangular_ or _Cartesian_ coordinates. It is completely determined by its _real part_ `z.real` and its _imaginary part_ `z.imag`.
_Polar coordinates_ give an alternative way to represent a complex number. In polar coordinates, a complex number _z_ is defined by the modulus _r_ and the phase angle _phi_. The modulus _r_ is the distance from _z_ to the origin, while the phase _phi_ is the counterclockwise angle, measured in radians, from the positive x-axis to the line segment that joins the origin to _z_.
The following functions can be used to convert from the native rectangular coordinates to polar coordinates and back.

cmath.phase(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.phase "Link to this definition")

Return the phase of _z_ (also known as the _argument_ of _z_), as a float. `phase(z)` is equivalent to `math.atan2(z.imag, z.real)`. The result lies in the range [-_π_ , _π_], and the branch cut for this operation lies along the negative real axis. The sign of the result is the same as the sign of `z.imag`, even when `z.imag` is zero:
Copy```
>>> phase(-1+0j)
3.141592653589793
>>> phase(-1-0j)
-3.141592653589793

```

Note
The modulus (absolute value) of a complex number _z_ can be computed using the built-in [`abs()`](https://docs.python.org/3/library/functions.html#abs "abs") function. There is no separate `cmath` module function for this operation.

cmath.polar(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.polar "Link to this definition")

Return the representation of _z_ in polar coordinates. Returns a pair `(r, phi)` where _r_ is the modulus of _z_ and _phi_ is the phase of _z_. `polar(z)` is equivalent to `(abs(z), phase(z))`.

cmath.rect(_r_ , _phi_)[¶](https://docs.python.org/3/library/cmath.html#cmath.rect "Link to this definition")

Return the complex number _z_ with polar coordinates _r_ and _phi_. Equivalent to `complex(r * math.cos(phi), r * math.sin(phi))`.
## Power and logarithmic functions[¶](https://docs.python.org/3/library/cmath.html#power-and-logarithmic-functions "Link to this heading")

cmath.exp(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.exp "Link to this definition")

Return _e_ raised to the power _z_ , where _e_ is the base of natural logarithms.

cmath.log(_z_[, _base_])[¶](https://docs.python.org/3/library/cmath.html#cmath.log "Link to this definition")

Return the logarithm of _z_ to the given _base_. If the _base_ is not specified, returns the natural logarithm of _z_. There is one branch cut, from 0 along the negative real axis to -∞.

cmath.log10(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.log10 "Link to this definition")

Return the base-10 logarithm of _z_. This has the same branch cut as [`log()`](https://docs.python.org/3/library/cmath.html#cmath.log "cmath.log").

cmath.sqrt(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.sqrt "Link to this definition")

Return the square root of _z_. This has the same branch cut as [`log()`](https://docs.python.org/3/library/cmath.html#cmath.log "cmath.log").
## Trigonometric functions[¶](https://docs.python.org/3/library/cmath.html#trigonometric-functions "Link to this heading")

cmath.acos(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.acos "Link to this definition")

Return the arc cosine of _z_. There are two branch cuts: One extends right from 1 along the real axis to ∞. The other extends left from -1 along the real axis to -∞.

cmath.asin(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.asin "Link to this definition")

Return the arc sine of _z_. This has the same branch cuts as [`acos()`](https://docs.python.org/3/library/cmath.html#cmath.acos "cmath.acos").

cmath.atan(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.atan "Link to this definition")

Return the arc tangent of _z_. There are two branch cuts: One extends from `1j` along the imaginary axis to `∞j`. The other extends from `-1j` along the imaginary axis to `-∞j`.

cmath.cos(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.cos "Link to this definition")

Return the cosine of _z_.

cmath.sin(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.sin "Link to this definition")

Return the sine of _z_.

cmath.tan(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.tan "Link to this definition")

Return the tangent of _z_.
## Hyperbolic functions[¶](https://docs.python.org/3/library/cmath.html#hyperbolic-functions "Link to this heading")

cmath.acosh(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.acosh "Link to this definition")

Return the inverse hyperbolic cosine of _z_. There is one branch cut, extending left from 1 along the real axis to -∞.

cmath.asinh(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.asinh "Link to this definition")

Return the inverse hyperbolic sine of _z_. There are two branch cuts: One extends from `1j` along the imaginary axis to `∞j`. The other extends from `-1j` along the imaginary axis to `-∞j`.

cmath.atanh(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.atanh "Link to this definition")

Return the inverse hyperbolic tangent of _z_. There are two branch cuts: One extends from `1` along the real axis to `∞`. The other extends from `-1` along the real axis to `-∞`.

cmath.cosh(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.cosh "Link to this definition")

Return the hyperbolic cosine of _z_.

cmath.sinh(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.sinh "Link to this definition")

Return the hyperbolic sine of _z_.

cmath.tanh(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.tanh "Link to this definition")

Return the hyperbolic tangent of _z_.
## Classification functions[¶](https://docs.python.org/3/library/cmath.html#classification-functions "Link to this heading")

cmath.isfinite(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.isfinite "Link to this definition")

Return `True` if both the real and imaginary parts of _z_ are finite, and `False` otherwise.
Added in version 3.2.

cmath.isinf(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.isinf "Link to this definition")

Return `True` if either the real or the imaginary part of _z_ is an infinity, and `False` otherwise.

cmath.isnan(_z_)[¶](https://docs.python.org/3/library/cmath.html#cmath.isnan "Link to this definition")

Return `True` if either the real or the imaginary part of _z_ is a NaN, and `False` otherwise.

cmath.isclose(_a_ , _b_ , _*_ , _rel_tol =1e-09_, _abs_tol =0.0_)[¶](https://docs.python.org/3/library/cmath.html#cmath.isclose "Link to this definition")

Return `True` if the values _a_ and _b_ are close to each other and `False` otherwise.
Whether or not two values are considered close is determined according to given absolute and relative tolerances. If no errors occur, the result will be: `abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`.
_rel_tol_ is the relative tolerance – it is the maximum allowed difference between _a_ and _b_ , relative to the larger absolute value of _a_ or _b_. For example, to set a tolerance of 5%, pass `rel_tol=0.05`. The default tolerance is `1e-09`, which assures that the two values are the same within about 9 decimal digits. _rel_tol_ must be nonnegative and less than `1.0`.
_abs_tol_ is the absolute tolerance; it defaults to `0.0` and it must be nonnegative. When comparing `x` to `0.0`, `isclose(x, 0)` is computed as `abs(x) <= rel_tol  * abs(x)`, which is `False` for any `x` and rel_tol less than `1.0`. So add an appropriate positive abs_tol argument to the call.
The IEEE 754 special values of `NaN`, `inf`, and `-inf` will be handled according to IEEE rules. Specifically, `NaN` is not considered close to any other value, including `NaN`. `inf` and `-inf` are only considered close to themselves.
Added in version 3.5.
See also
[**PEP 485**](https://peps.python.org/pep-0485/) – A function for testing approximate equality
## Constants[¶](https://docs.python.org/3/library/cmath.html#constants "Link to this heading")

cmath.pi[¶](https://docs.python.org/3/library/cmath.html#cmath.pi "Link to this definition")

The mathematical constant _π_ , as a float.

cmath.e[¶](https://docs.python.org/3/library/cmath.html#cmath.e "Link to this definition")

The mathematical constant _e_ , as a float.

cmath.tau[¶](https://docs.python.org/3/library/cmath.html#cmath.tau "Link to this definition")

The mathematical constant _τ_ , as a float.
Added in version 3.6.

cmath.inf[¶](https://docs.python.org/3/library/cmath.html#cmath.inf "Link to this definition")

Floating-point positive infinity. Equivalent to `float('inf')`.
Added in version 3.6.

cmath.infj[¶](https://docs.python.org/3/library/cmath.html#cmath.infj "Link to this definition")

Complex number with zero real part and positive infinity imaginary part. Equivalent to `complex(0.0, float('inf'))`.
Added in version 3.6.

cmath.nan[¶](https://docs.python.org/3/library/cmath.html#cmath.nan "Link to this definition")

A floating-point “not a number” (NaN) value. Equivalent to `float('nan')`. See also [`math.nan`](https://docs.python.org/3/library/math.html#math.nan "math.nan").
Added in version 3.6.

cmath.nanj[¶](https://docs.python.org/3/library/cmath.html#cmath.nanj "Link to this definition")

Complex number with zero real part and NaN imaginary part. Equivalent to `complex(0.0, float('nan'))`.
Added in version 3.6.
Note that the selection of functions is similar, but not identical, to that in module [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions \(sin\(\) etc.\)."). The reason for having two modules is that some users aren’t interested in complex numbers, and perhaps don’t even know what they are. They would rather have `math.sqrt(-1)` raise an exception than return a complex number. Also note that the functions defined in `cmath` always return a complex number, even if the answer can be expressed as a real number (in which case the complex number has an imaginary part of zero).
A note on branch cuts: They are curves along which the given function fails to be continuous. They are a necessary feature of many complex functions. It is assumed that if you need to compute with complex functions, you will understand about branch cuts. Consult almost any (not too elementary) book on complex variables for enlightenment. For information of the proper choice of branch cuts for numerical purposes, a good reference should be the following:
See also
Kahan, W: Branch cuts for complex elementary functions; or, Much ado about nothing’s sign bit. In Iserles, A., and Powell, M. (eds.), The state of the art in numerical analysis. Clarendon Press (1987) pp165–211.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`cmath` — Mathematical functions for complex numbers](https://docs.python.org/3/library/cmath.html)
    * [Conversions to and from polar coordinates](https://docs.python.org/3/library/cmath.html#conversions-to-and-from-polar-coordinates)
    * [Power and logarithmic functions](https://docs.python.org/3/library/cmath.html#power-and-logarithmic-functions)
    * [Trigonometric functions](https://docs.python.org/3/library/cmath.html#trigonometric-functions)
    * [Hyperbolic functions](https://docs.python.org/3/library/cmath.html#hyperbolic-functions)
    * [Classification functions](https://docs.python.org/3/library/cmath.html#classification-functions)
    * [Constants](https://docs.python.org/3/library/cmath.html#constants)


#### Previous topic
[`math` — Mathematical functions](https://docs.python.org/3/library/math.html "previous chapter")
#### Next topic
[`decimal` — Decimal fixed-point and floating-point arithmetic](https://docs.python.org/3/library/decimal.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=cmath+%E2%80%94+Mathematical+functions+for+complex+numbers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcmath.html&pagesource=library%2Fcmath.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/decimal.html "decimal — Decimal fixed-point and floating-point arithmetic") |
  * [previous](https://docs.python.org/3/library/math.html "math — Mathematical functions") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html) »
  * [`cmath` — Mathematical functions for complex numbers](https://docs.python.org/3/library/cmath.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
