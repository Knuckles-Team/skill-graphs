[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
#### Previous topic
[`graphlib` — Functionality to operate with graph-like structures](https://docs.python.org/3/library/graphlib.html "previous chapter")
#### Next topic
[`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Numeric+and+Mathematical+Modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fnumeric.html&pagesource=library%2Fnumeric.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/numbers.html "numbers — Numeric abstract base classes") |
  * [previous](https://docs.python.org/3/library/graphlib.html "graphlib — Functionality to operate with graph-like structures") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html)
  * |
  * Theme  Auto Light Dark |


# Numeric and Mathematical Modules[¶](https://docs.python.org/3/library/numeric.html#numeric-and-mathematical-modules "Link to this heading")
The modules described in this chapter provide numeric and math-related functions and data types. The [`numbers`](https://docs.python.org/3/library/numbers.html#module-numbers "numbers: Numeric abstract base classes \(Complex, Real, Integral, etc.\).") module defines an abstract hierarchy of numeric types. The [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions \(sin\(\) etc.\).") and [`cmath`](https://docs.python.org/3/library/cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.") modules contain various mathematical functions for floating-point and complex numbers. The [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.") module supports exact representations of decimal numbers, using arbitrary precision arithmetic.
The following modules are documented in this chapter:
  * [`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html)
    * [The numeric tower](https://docs.python.org/3/library/numbers.html#the-numeric-tower)
    * [Notes for type implementers](https://docs.python.org/3/library/numbers.html#notes-for-type-implementers)
      * [Adding More Numeric ABCs](https://docs.python.org/3/library/numbers.html#adding-more-numeric-abcs)
      * [Implementing the arithmetic operations](https://docs.python.org/3/library/numbers.html#implementing-the-arithmetic-operations)
  * [`math` — Mathematical functions](https://docs.python.org/3/library/math.html)
    * [Number-theoretic functions](https://docs.python.org/3/library/math.html#number-theoretic-functions)
    * [Floating point arithmetic](https://docs.python.org/3/library/math.html#floating-point-arithmetic)
    * [Floating point manipulation functions](https://docs.python.org/3/library/math.html#floating-point-manipulation-functions)
    * [Power, exponential and logarithmic functions](https://docs.python.org/3/library/math.html#power-exponential-and-logarithmic-functions)
    * [Summation and product functions](https://docs.python.org/3/library/math.html#summation-and-product-functions)
    * [Angular conversion](https://docs.python.org/3/library/math.html#angular-conversion)
    * [Trigonometric functions](https://docs.python.org/3/library/math.html#trigonometric-functions)
    * [Hyperbolic functions](https://docs.python.org/3/library/math.html#hyperbolic-functions)
    * [Special functions](https://docs.python.org/3/library/math.html#special-functions)
    * [Constants](https://docs.python.org/3/library/math.html#constants)
  * [`cmath` — Mathematical functions for complex numbers](https://docs.python.org/3/library/cmath.html)
    * [Conversions to and from polar coordinates](https://docs.python.org/3/library/cmath.html#conversions-to-and-from-polar-coordinates)
    * [Power and logarithmic functions](https://docs.python.org/3/library/cmath.html#power-and-logarithmic-functions)
    * [Trigonometric functions](https://docs.python.org/3/library/cmath.html#trigonometric-functions)
    * [Hyperbolic functions](https://docs.python.org/3/library/cmath.html#hyperbolic-functions)
    * [Classification functions](https://docs.python.org/3/library/cmath.html#classification-functions)
    * [Constants](https://docs.python.org/3/library/cmath.html#constants)
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
  * [`fractions` — Rational numbers](https://docs.python.org/3/library/fractions.html)
  * [`random` — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html)
    * [Bookkeeping functions](https://docs.python.org/3/library/random.html#bookkeeping-functions)
    * [Functions for bytes](https://docs.python.org/3/library/random.html#functions-for-bytes)
    * [Functions for integers](https://docs.python.org/3/library/random.html#functions-for-integers)
    * [Functions for sequences](https://docs.python.org/3/library/random.html#functions-for-sequences)
    * [Discrete distributions](https://docs.python.org/3/library/random.html#discrete-distributions)
    * [Real-valued distributions](https://docs.python.org/3/library/random.html#real-valued-distributions)
    * [Alternative Generator](https://docs.python.org/3/library/random.html#alternative-generator)
    * [Notes on Reproducibility](https://docs.python.org/3/library/random.html#notes-on-reproducibility)
    * [Examples](https://docs.python.org/3/library/random.html#examples)
    * [Recipes](https://docs.python.org/3/library/random.html#recipes)
    * [Command-line usage](https://docs.python.org/3/library/random.html#command-line-usage)
    * [Command-line example](https://docs.python.org/3/library/random.html#command-line-example)
  * [`statistics` — Mathematical statistics functions](https://docs.python.org/3/library/statistics.html)
    * [Averages and measures of central location](https://docs.python.org/3/library/statistics.html#averages-and-measures-of-central-location)
    * [Measures of spread](https://docs.python.org/3/library/statistics.html#measures-of-spread)
    * [Statistics for relations between two inputs](https://docs.python.org/3/library/statistics.html#statistics-for-relations-between-two-inputs)
    * [Function details](https://docs.python.org/3/library/statistics.html#function-details)
    * [Exceptions](https://docs.python.org/3/library/statistics.html#exceptions)
    * [`NormalDist` objects](https://docs.python.org/3/library/statistics.html#normaldist-objects)
    * [Examples and Recipes](https://docs.python.org/3/library/statistics.html#examples-and-recipes)
      * [Classic probability problems](https://docs.python.org/3/library/statistics.html#classic-probability-problems)
      * [Monte Carlo inputs for simulations](https://docs.python.org/3/library/statistics.html#monte-carlo-inputs-for-simulations)
      * [Approximating binomial distributions](https://docs.python.org/3/library/statistics.html#approximating-binomial-distributions)
      * [Naive bayesian classifier](https://docs.python.org/3/library/statistics.html#naive-bayesian-classifier)


#### Previous topic
[`graphlib` — Functionality to operate with graph-like structures](https://docs.python.org/3/library/graphlib.html "previous chapter")
#### Next topic
[`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Numeric+and+Mathematical+Modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fnumeric.html&pagesource=library%2Fnumeric.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/numbers.html "numbers — Numeric abstract base classes") |
  * [previous](https://docs.python.org/3/library/graphlib.html "graphlib — Functionality to operate with graph-like structures") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
