[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html)
    * [The numeric tower](https://docs.python.org/3/library/numbers.html#the-numeric-tower)
    * [Notes for type implementers](https://docs.python.org/3/library/numbers.html#notes-for-type-implementers)
      * [Adding More Numeric ABCs](https://docs.python.org/3/library/numbers.html#adding-more-numeric-abcs)
      * [Implementing the arithmetic operations](https://docs.python.org/3/library/numbers.html#implementing-the-arithmetic-operations)


#### Previous topic
[Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html "previous chapter")
#### Next topic
[`math` — Mathematical functions](https://docs.python.org/3/library/math.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=numbers+%E2%80%94+Numeric+abstract+base+classes&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fnumbers.html&pagesource=library%2Fnumbers.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/math.html "math — Mathematical functions") |
  * [previous](https://docs.python.org/3/library/numeric.html "Numeric and Mathematical Modules") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html) »
  * [`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html)
  * |
  * Theme  Auto Light Dark |


#  `numbers` — Numeric abstract base classes[¶](https://docs.python.org/3/library/numbers.html#module-numbers "Link to this heading")
**Source code:**
* * *
The `numbers` module ([**PEP 3141**](https://peps.python.org/pep-3141/)) defines a hierarchy of numeric [abstract base classes](https://docs.python.org/3/glossary.html#term-abstract-base-class) which progressively define more operations. None of the types defined in this module are intended to be instantiated.

_class_ numbers.Number[¶](https://docs.python.org/3/library/numbers.html#numbers.Number "Link to this definition")

The root of the numeric hierarchy. If you just want to check if an argument _x_ is a number, without caring what kind, use `isinstance(x, Number)`.
## The numeric tower[¶](https://docs.python.org/3/library/numbers.html#the-numeric-tower "Link to this heading")

_class_ numbers.Complex[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex "Link to this definition")

Subclasses of this type describe complex numbers and include the operations that work on the built-in [`complex`](https://docs.python.org/3/library/functions.html#complex "complex") type. These are: conversions to `complex` and [`bool`](https://docs.python.org/3/library/functions.html#bool "bool"), [`real`](https://docs.python.org/3/library/numbers.html#numbers.Complex.real "numbers.Complex.real"), [`imag`](https://docs.python.org/3/library/numbers.html#numbers.Complex.imag "numbers.Complex.imag"), `+`, `-`, `*`, `/`, `**`, [`abs()`](https://docs.python.org/3/library/functions.html#abs "abs"), [`conjugate()`](https://docs.python.org/3/library/numbers.html#numbers.Complex.conjugate "numbers.Complex.conjugate"), `==`, and `!=`. All except `-` and `!=` are abstract.

real[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex.real "Link to this definition")

Abstract. Retrieves the real component of this number.

imag[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex.imag "Link to this definition")

Abstract. Retrieves the imaginary component of this number.

_abstractmethod_ conjugate()[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex.conjugate "Link to this definition")

Abstract. Returns the complex conjugate. For example, `(1+3j).conjugate() == (1-3j)`.

_class_ numbers.Real[¶](https://docs.python.org/3/library/numbers.html#numbers.Real "Link to this definition")

To [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex"), `Real` adds the operations that work on real numbers.
In short, those are: a conversion to [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`math.trunc()`](https://docs.python.org/3/library/math.html#math.trunc "math.trunc"), [`round()`](https://docs.python.org/3/library/functions.html#round "round"), [`math.floor()`](https://docs.python.org/3/library/math.html#math.floor "math.floor"), [`math.ceil()`](https://docs.python.org/3/library/math.html#math.ceil "math.ceil"), [`divmod()`](https://docs.python.org/3/library/functions.html#divmod "divmod"), `//`, `%`, `<`, `<=`, `>`, and `>=`.
Real also provides defaults for [`complex()`](https://docs.python.org/3/library/functions.html#complex "complex"), [`real`](https://docs.python.org/3/library/numbers.html#numbers.Complex.real "numbers.Complex.real"), [`imag`](https://docs.python.org/3/library/numbers.html#numbers.Complex.imag "numbers.Complex.imag"), and [`conjugate()`](https://docs.python.org/3/library/numbers.html#numbers.Complex.conjugate "numbers.Complex.conjugate").

_class_ numbers.Rational[¶](https://docs.python.org/3/library/numbers.html#numbers.Rational "Link to this definition")

Subtypes [`Real`](https://docs.python.org/3/library/numbers.html#numbers.Real "numbers.Real") and adds [`numerator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.numerator "numbers.Rational.numerator") and [`denominator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.denominator "numbers.Rational.denominator") properties. It also provides a default for [`float()`](https://docs.python.org/3/library/functions.html#float "float").
The [`numerator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.numerator "numbers.Rational.numerator") and [`denominator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.denominator "numbers.Rational.denominator") values should be instances of [`Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral") and should be in lowest terms with `denominator` positive.

numerator[¶](https://docs.python.org/3/library/numbers.html#numbers.Rational.numerator "Link to this definition")

Abstract. The numerator of this rational number.

denominator[¶](https://docs.python.org/3/library/numbers.html#numbers.Rational.denominator "Link to this definition")

Abstract. The denominator of this rational number.

_class_ numbers.Integral[¶](https://docs.python.org/3/library/numbers.html#numbers.Integral "Link to this definition")

Subtypes [`Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational "numbers.Rational") and adds a conversion to [`int`](https://docs.python.org/3/library/functions.html#int "int"). Provides defaults for [`float()`](https://docs.python.org/3/library/functions.html#float "float"), [`numerator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.numerator "numbers.Rational.numerator"), and [`denominator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.denominator "numbers.Rational.denominator"). Adds abstract methods for [`pow()`](https://docs.python.org/3/library/functions.html#pow "pow") with modulus and bit-string operations: `<<`, `>>`, `&`, `^`, `|`, `~`.
## Notes for type implementers[¶](https://docs.python.org/3/library/numbers.html#notes-for-type-implementers "Link to this heading")
Implementers should be careful to make equal numbers equal and hash them to the same values. This may be subtle if there are two different extensions of the real numbers. For example, [`fractions.Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction") implements [`hash()`](https://docs.python.org/3/library/functions.html#hash "hash") as follows:
Copy```
def __hash__(self):
    if self.denominator == 1:
        # Get integers right.
        return hash(self.numerator)
    # Expensive check, but definitely correct.
    if self == float(self):
        return hash(float(self))
    else:
        # Use tuple's hash to avoid a high collision rate on
        # simple fractions.
        return hash((self.numerator, self.denominator))

```

### Adding More Numeric ABCs[¶](https://docs.python.org/3/library/numbers.html#adding-more-numeric-abcs "Link to this heading")
There are, of course, more possible ABCs for numbers, and this would be a poor hierarchy if it precluded the possibility of adding those. You can add `MyFoo` between [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex") and [`Real`](https://docs.python.org/3/library/numbers.html#numbers.Real "numbers.Real") with:
Copy```
class MyFoo(Complex): ...
MyFoo.register(Real)

```

### Implementing the arithmetic operations[¶](https://docs.python.org/3/library/numbers.html#implementing-the-arithmetic-operations "Link to this heading")
We want to implement the arithmetic operations so that mixed-mode operations either call an implementation whose author knew about the types of both arguments, or convert both to the nearest built in type and do the operation there. For subtypes of [`Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral"), this means that [`__add__()`](https://docs.python.org/3/reference/datamodel.html#object.__add__ "object.__add__") and [`__radd__()`](https://docs.python.org/3/reference/datamodel.html#object.__radd__ "object.__radd__") should be defined as:
Copy```
class MyIntegral(Integral):

    def __add__(self, other):
        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(self, other)
        elif isinstance(other, OtherTypeIKnowAbout):
            return do_my_other_adding_stuff(self, other)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(other, self)
        elif isinstance(other, OtherTypeIKnowAbout):
            return do_my_other_adding_stuff(other, self)
        elif isinstance(other, Integral):
            return int(other) + int(self)
        elif isinstance(other, Real):
            return float(other) + float(self)
        elif isinstance(other, Complex):
            return complex(other) + complex(self)
        else:
            return NotImplemented

```

There are 5 different cases for a mixed-type operation on subclasses of [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex"). I’ll refer to all of the above code that doesn’t refer to `MyIntegral` and `OtherTypeIKnowAbout` as “boilerplate”. `a` will be an instance of `A`, which is a subtype of `Complex` (`a : A <: Complex`), and `b : B <: Complex`. I’ll consider `a + b`:
  1. If `A` defines an [`__add__()`](https://docs.python.org/3/reference/datamodel.html#object.__add__ "object.__add__") which accepts `b`, all is well.
  2. If `A` falls back to the boilerplate code, and it were to return a value from [`__add__()`](https://docs.python.org/3/reference/datamodel.html#object.__add__ "object.__add__"), we’d miss the possibility that `B` defines a more intelligent [`__radd__()`](https://docs.python.org/3/reference/datamodel.html#object.__radd__ "object.__radd__"), so the boilerplate should return [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented") from `__add__()`. (Or `A` may not implement `__add__()` at all.)
  3. Then `B`’s [`__radd__()`](https://docs.python.org/3/reference/datamodel.html#object.__radd__ "object.__radd__") gets a chance. If it accepts `a`, all is well.
  4. If it falls back to the boilerplate, there are no more possible methods to try, so this is where the default implementation should live.
  5. If `B <: A`, Python tries `B.__radd__` before `A.__add__`. This is ok, because it was implemented with knowledge of `A`, so it can handle those instances before delegating to [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex").


If `A <: Complex` and `B <: Real` without sharing any other knowledge, then the appropriate shared operation is the one involving the built in [`complex`](https://docs.python.org/3/library/functions.html#complex "complex"), and both [`__radd__()`](https://docs.python.org/3/reference/datamodel.html#object.__radd__ "object.__radd__") s land there, so `a+b == b+a`.
Because most of the operations on any given type will be very similar, it can be useful to define a helper function which generates the forward and reverse instances of any given operator. For example, [`fractions.Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction") uses:
Copy```
def _operator_fallbacks(monomorphic_operator, fallback_operator):
    def forward(a, b):
        if isinstance(b, (int, Fraction)):
            return monomorphic_operator(a, b)
        elif isinstance(b, float):
            return fallback_operator(float(a), b)
        elif isinstance(b, complex):
            return fallback_operator(complex(a), b)
        else:
            return NotImplemented
    forward.__name__ = '__' + fallback_operator.__name__ + '__'
    forward.__doc__ = monomorphic_operator.__doc__

    def reverse(b, a):
        if isinstance(a, Rational):
            # Includes ints.
            return monomorphic_operator(a, b)
        elif isinstance(a, Real):
            return fallback_operator(float(a), float(b))
        elif isinstance(a, Complex):
            return fallback_operator(complex(a), complex(b))
        else:
            return NotImplemented
    reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
    reverse.__doc__ = monomorphic_operator.__doc__

    return forward, reverse

def _add(a, b):
    """a + b"""
    return Fraction(a.numerator * b.denominator +
                    b.numerator * a.denominator,
                    a.denominator * b.denominator)

__add__, __radd__ = _operator_fallbacks(_add, operator.add)

# ...

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html)
    * [The numeric tower](https://docs.python.org/3/library/numbers.html#the-numeric-tower)
    * [Notes for type implementers](https://docs.python.org/3/library/numbers.html#notes-for-type-implementers)
      * [Adding More Numeric ABCs](https://docs.python.org/3/library/numbers.html#adding-more-numeric-abcs)
      * [Implementing the arithmetic operations](https://docs.python.org/3/library/numbers.html#implementing-the-arithmetic-operations)


#### Previous topic
[Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html "previous chapter")
#### Next topic
[`math` — Mathematical functions](https://docs.python.org/3/library/math.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=numbers+%E2%80%94+Numeric+abstract+base+classes&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fnumbers.html&pagesource=library%2Fnumbers.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/math.html "math — Mathematical functions") |
  * [previous](https://docs.python.org/3/library/numeric.html "Numeric and Mathematical Modules") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html) »
  * [`numbers` — Numeric abstract base classes](https://docs.python.org/3/library/numbers.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
