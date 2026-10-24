[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
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


#### Previous topic
[`fractions` — Rational numbers](https://docs.python.org/3/library/fractions.html "previous chapter")
#### Next topic
[`statistics` — Mathematical statistics functions](https://docs.python.org/3/library/statistics.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=random+%E2%80%94+Generate+pseudo-random+numbers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Frandom.html&pagesource=library%2Frandom.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/statistics.html "statistics — Mathematical statistics functions") |
  * [previous](https://docs.python.org/3/library/fractions.html "fractions — Rational numbers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html) »
  * [`random` — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html)
  * |
  * Theme  Auto Light Dark |


#  `random` — Generate pseudo-random numbers[¶](https://docs.python.org/3/library/random.html#module-random "Link to this heading")
**Source code:**
* * *
This module implements pseudo-random number generators for various distributions.
For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.
On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions. For generating distributions of angles, the von Mises distribution is available.
Almost all module functions depend on the basic function [`random()`](https://docs.python.org/3/library/random.html#random.random "random.random"), which generates a random float uniformly in the half-open range `0.0 <= X < 1.0`. Python uses the Mersenne Twister as the core generator. It produces 53-bit precision floats and has a period of 2**19937-1. The underlying implementation in C is both fast and threadsafe. The Mersenne Twister is one of the most extensively tested random number generators in existence. However, being completely deterministic, it is not suitable for all purposes, and is completely unsuitable for cryptographic purposes.
The functions supplied by this module are actually bound methods of a hidden instance of the [`random.Random`](https://docs.python.org/3/library/random.html#random.Random "random.Random") class. You can instantiate your own instances of [`Random`](https://docs.python.org/3/library/random.html#random.Random "random.Random") to get generators that don’t share state.
Class [`Random`](https://docs.python.org/3/library/random.html#random.Random "random.Random") can also be subclassed if you want to use a different basic generator of your own devising: see the documentation on that class for more details.
The `random` module also provides the [`SystemRandom`](https://docs.python.org/3/library/random.html#random.SystemRandom "random.SystemRandom") class which uses the system function [`os.urandom()`](https://docs.python.org/3/library/os.html#os.urandom "os.urandom") to generate random numbers from sources provided by the operating system.
Warning
The pseudo-random generators of this module should not be used for security purposes. For security or cryptographic uses, see the [`secrets`](https://docs.python.org/3/library/secrets.html#module-secrets "secrets: Generate secure random numbers for managing secrets.") module.
See also
M. Matsumoto and T. Nishimura, “Mersenne Twister: A 623-dimensionally equidistributed uniform pseudorandom number generator”, ACM Transactions on Modeling and Computer Simulation Vol. 8, No. 1, January pp.3–30 1998.
Note
The global random number generator and instances of [`Random`](https://docs.python.org/3/library/random.html#random.Random "random.Random") are thread-safe. However, in the free-threaded build, concurrent calls to the global generator or to the same instance of `Random` may encounter contention and poor performance. Consider using separate instances of `Random` per thread instead.
## Bookkeeping functions[¶](https://docs.python.org/3/library/random.html#bookkeeping-functions "Link to this heading")

random.seed(_a =None_, _version =2_)[¶](https://docs.python.org/3/library/random.html#random.seed "Link to this definition")

Initialize the random number generator.
If _a_ is omitted or `None`, the current system time is used. If randomness sources are provided by the operating system, they are used instead of the system time (see the [`os.urandom()`](https://docs.python.org/3/library/os.html#os.urandom "os.urandom") function for details on availability).
If _a_ is an int, its absolute value is used directly.
With version 2 (the default), a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") object gets converted to an [`int`](https://docs.python.org/3/library/functions.html#int "int") and all of its bits are used.
With version 1 (provided for reproducing random sequences from older versions of Python), the algorithm for [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") and [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") generates a narrower range of seeds.
Changed in version 3.2: Moved to the version 2 scheme which uses all of the bits in a string seed.
Changed in version 3.11: The _seed_ must be one of the following types: `None`, [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray").

random.getstate()[¶](https://docs.python.org/3/library/random.html#random.getstate "Link to this definition")

Return an object capturing the current internal state of the generator. This object can be passed to [`setstate()`](https://docs.python.org/3/library/random.html#random.setstate "random.setstate") to restore the state.

random.setstate(_state_)[¶](https://docs.python.org/3/library/random.html#random.setstate "Link to this definition")

_state_ should have been obtained from a previous call to [`getstate()`](https://docs.python.org/3/library/random.html#random.getstate "random.getstate"), and `setstate()` restores the internal state of the generator to what it was at the time `getstate()` was called.
## Functions for bytes[¶](https://docs.python.org/3/library/random.html#functions-for-bytes "Link to this heading")

random.randbytes(_n_)[¶](https://docs.python.org/3/library/random.html#random.randbytes "Link to this definition")

Generate _n_ random bytes.
This method should not be used for generating security tokens. Use [`secrets.token_bytes()`](https://docs.python.org/3/library/secrets.html#secrets.token_bytes "secrets.token_bytes") instead.
Added in version 3.9.
## Functions for integers[¶](https://docs.python.org/3/library/random.html#functions-for-integers "Link to this heading")

random.randrange(_stop_)[¶](https://docs.python.org/3/library/random.html#random.randrange "Link to this definition")


random.randrange(_start_ , _stop_[, _step_])

Return a randomly selected element from `range(start, stop, step)`.
This is roughly equivalent to `choice(range(start, stop, step))` but supports arbitrarily large ranges and is optimized for common cases.
The positional argument pattern matches the [`range()`](https://docs.python.org/3/library/stdtypes.html#range "range") function.
Keyword arguments should not be used because they can be interpreted in unexpected ways. For example `randrange(start=100)` is interpreted as `randrange(0, 100, 1)`.
Changed in version 3.2: [`randrange()`](https://docs.python.org/3/library/random.html#random.randrange "random.randrange") is more sophisticated about producing equally distributed values. Formerly it used a style like `int(random()*n)` which could produce slightly uneven distributions.
Changed in version 3.12: Automatic conversion of non-integer types is no longer supported. Calls such as `randrange(10.0)` and `randrange(Fraction(10, 1))` now raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").

random.randint(_a_ , _b_)[¶](https://docs.python.org/3/library/random.html#random.randint "Link to this definition")

Return a random integer _N_ such that `a <= N <= b`. Alias for `randrange(a, b+1)`.

random.getrandbits(_k_)[¶](https://docs.python.org/3/library/random.html#random.getrandbits "Link to this definition")

Returns a non-negative Python integer with _k_ random bits. This method is supplied with the Mersenne Twister generator and some other generators may also provide it as an optional part of the API. When available, [`getrandbits()`](https://docs.python.org/3/library/random.html#random.getrandbits "random.getrandbits") enables [`randrange()`](https://docs.python.org/3/library/random.html#random.randrange "random.randrange") to handle arbitrarily large ranges.
Changed in version 3.9: This method now accepts zero for _k_.
## Functions for sequences[¶](https://docs.python.org/3/library/random.html#functions-for-sequences "Link to this heading")

random.choice(_seq_)[¶](https://docs.python.org/3/library/random.html#random.choice "Link to this definition")

Return a random element from the non-empty sequence _seq_. If _seq_ is empty, raises [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError").

random.choices(_population_ , _weights =None_, _*_ , _cum_weights =None_, _k =1_)[¶](https://docs.python.org/3/library/random.html#random.choices "Link to this definition")

Return a _k_ sized list of elements chosen from the _population_ with replacement. If the _population_ is empty, raises [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError").
If a _weights_ sequence is specified, selections are made according to the relative weights. Alternatively, if a _cum_weights_ sequence is given, the selections are made according to the cumulative weights (perhaps computed using [`itertools.accumulate()`](https://docs.python.org/3/library/itertools.html#itertools.accumulate "itertools.accumulate")). For example, the relative weights `[10, 5, 30, 5]` are equivalent to the cumulative weights `[10, 15, 45, 50]`. Internally, the relative weights are converted to cumulative weights before making selections, so supplying the cumulative weights saves work.
If neither _weights_ nor _cum_weights_ are specified, selections are made with equal probability. If a weights sequence is supplied, it must be the same length as the _population_ sequence. It is a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") to specify both _weights_ and _cum_weights_.
The _weights_ or _cum_weights_ can use any numeric type that interoperates with the [`float`](https://docs.python.org/3/library/functions.html#float "float") values returned by [`random()`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") (that includes integers, floats, and fractions but excludes decimals). Weights are assumed to be non-negative and finite. A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if all weights are zero.
For a given seed, the `choices()` function with equal weighting typically produces a different sequence than repeated calls to [`choice()`](https://docs.python.org/3/library/random.html#random.choice "random.choice"). The algorithm used by `choices()` uses floating-point arithmetic for internal consistency and speed. The algorithm used by `choice()` defaults to integer arithmetic with repeated selections to avoid small biases from round-off error.
Added in version 3.6.
Changed in version 3.9: Raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if all weights are zero.

random.shuffle(_x_)[¶](https://docs.python.org/3/library/random.html#random.shuffle "Link to this definition")

Shuffle the sequence _x_ in place.
To shuffle an immutable sequence and return a new shuffled list, use `sample(x, k=len(x))` instead.
Note that even for small `len(x)`, the total number of permutations of _x_ can quickly grow larger than the period of most random number generators. This implies that most permutations of a long sequence can never be generated. For example, a sequence of length 2080 is the largest that can fit within the period of the Mersenne Twister random number generator.
Changed in version 3.11: Removed the optional parameter _random_.

random.sample(_population_ , _k_ , _*_ , _counts =None_)[¶](https://docs.python.org/3/library/random.html#random.sample "Link to this definition")

Return a _k_ length list of unique elements chosen from the population sequence. Used for random sampling without replacement.
Returns a new list containing elements from the population while leaving the original population unchanged. The resulting list is in selection order so that all sub-slices will also be valid random samples. This allows raffle winners (the sample) to be partitioned into grand prize and second place winners (the subslices).
Members of the population need not be [hashable](https://docs.python.org/3/glossary.html#term-hashable) or unique. If the population contains repeats, then each occurrence is a possible selection in the sample.
Repeated elements can be specified one at a time or with the optional keyword-only _counts_ parameter. For example, `sample(['red', 'blue'], counts=[4, 2], k=5)` is equivalent to `sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)`.
To choose a sample from a range of integers, use a [`range()`](https://docs.python.org/3/library/stdtypes.html#range "range") object as an argument. This is especially fast and space efficient for sampling from a large population: `sample(range(10000000), k=60)`.
If the sample size is larger than the population size, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
Changed in version 3.9: Added the _counts_ parameter.
Changed in version 3.11: The _population_ must be a sequence. Automatic conversion of sets to lists is no longer supported.
## Discrete distributions[¶](https://docs.python.org/3/library/random.html#discrete-distributions "Link to this heading")
The following function generates a discrete distribution.

random.binomialvariate(_n =1_, _p =0.5_)[¶](https://docs.python.org/3/library/random.html#random.binomialvariate "Link to this definition")

_n_ independent trials with the probability of success in each trial being _p_ :
Mathematically equivalent to:
Copy```
sum(random() < p for i in range(n))

```

The number of trials _n_ should be a non-negative integer. The probability of success _p_ should be between `0.0 <= p <= 1.0`. The result is an integer in the range `0 <= X <= n`.
Added in version 3.12.
## Real-valued distributions[¶](https://docs.python.org/3/library/random.html#real-valued-distributions "Link to this heading")
The following functions generate specific real-valued distributions. Function parameters are named after the corresponding variables in the distribution’s equation, as used in common mathematical practice; most of these equations can be found in any statistics text.

random.random()[¶](https://docs.python.org/3/library/random.html#random.random "Link to this definition")

Return the next random floating-point number in the range `0.0 <= X < 1.0`

random.uniform(_a_ , _b_)[¶](https://docs.python.org/3/library/random.html#random.uniform "Link to this definition")

Return a random floating-point number _N_ such that `a <= N <= b` for `a <= b` and `b <= N <= a` for `b < a`.
The end-point value `b` may or may not be included in the range depending on floating-point rounding in the expression `a + (b-a) * random()`.

random.triangular(_low_ , _high_ , _mode_)[¶](https://docs.python.org/3/library/random.html#random.triangular "Link to this definition")

Return a random floating-point number _N_ such that `low <= N <= high` and with the specified _mode_ between those bounds. The _low_ and _high_ bounds default to zero and one. The _mode_ argument defaults to the midpoint between the bounds, giving a symmetric distribution.

random.betavariate(_alpha_ , _beta_)[¶](https://docs.python.org/3/library/random.html#random.betavariate "Link to this definition")

Beta distribution. Conditions on the parameters are `alpha > 0` and `beta > 0`. Returned values range between 0 and 1.

random.expovariate(_lambd =1.0_)[¶](https://docs.python.org/3/library/random.html#random.expovariate "Link to this definition")

Exponential distribution. _lambd_ is 1.0 divided by the desired mean. It should be nonzero. (The parameter would be called “lambda”, but that is a reserved word in Python.) Returned values range from 0 to positive infinity if _lambd_ is positive, and from negative infinity to 0 if _lambd_ is negative.
Changed in version 3.12: Added the default value for `lambd`.

random.gammavariate(_alpha_ , _beta_)[¶](https://docs.python.org/3/library/random.html#random.gammavariate "Link to this definition")

Gamma distribution. (_Not_ the gamma function!) The shape and scale parameters, _alpha_ and _beta_ , must have positive values. (Calling conventions vary and some sources define ‘beta’ as the inverse of the scale).
The probability distribution function is:
Copy```
          x ** (alpha - 1) * math.exp(-x / beta)
pdf(x) =  --------------------------------------
            math.gamma(alpha) * beta ** alpha

```


random.gauss(_mu =0.0_, _sigma =1.0_)[¶](https://docs.python.org/3/library/random.html#random.gauss "Link to this definition")

Normal distribution, also called the Gaussian distribution. _mu_ is the mean, and _sigma_ is the standard deviation. This is slightly faster than the [`normalvariate()`](https://docs.python.org/3/library/random.html#random.normalvariate "random.normalvariate") function defined below.
Multithreading note: When two threads call this function simultaneously, it is possible that they will receive the same return value. This can be avoided in three ways. 1) Have each thread use a different instance of the random number generator. 2) Put locks around all calls. 3) Use the slower, but thread-safe [`normalvariate()`](https://docs.python.org/3/library/random.html#random.normalvariate "random.normalvariate") function instead.
Changed in version 3.11: _mu_ and _sigma_ now have default arguments.

random.lognormvariate(_mu_ , _sigma_)[¶](https://docs.python.org/3/library/random.html#random.lognormvariate "Link to this definition")

Log normal distribution. If you take the natural logarithm of this distribution, you’ll get a normal distribution with mean _mu_ and standard deviation _sigma_. _mu_ can have any value, and _sigma_ must be greater than zero.

random.normalvariate(_mu =0.0_, _sigma =1.0_)[¶](https://docs.python.org/3/library/random.html#random.normalvariate "Link to this definition")

Normal distribution. _mu_ is the mean, and _sigma_ is the standard deviation.
Changed in version 3.11: _mu_ and _sigma_ now have default arguments.

random.vonmisesvariate(_mu_ , _kappa_)[¶](https://docs.python.org/3/library/random.html#random.vonmisesvariate "Link to this definition")

_mu_ is the mean angle, expressed in radians between 0 and 2*_pi_ , and _kappa_ is the concentration parameter, which must be greater than or equal to zero. If _kappa_ is equal to zero, this distribution reduces to a uniform random angle over the range 0 to 2*_pi_.

random.paretovariate(_alpha_)[¶](https://docs.python.org/3/library/random.html#random.paretovariate "Link to this definition")

Pareto distribution. _alpha_ is the shape parameter.

random.weibullvariate(_alpha_ , _beta_)[¶](https://docs.python.org/3/library/random.html#random.weibullvariate "Link to this definition")

Weibull distribution. _alpha_ is the scale parameter and _beta_ is the shape parameter.
## Alternative Generator[¶](https://docs.python.org/3/library/random.html#alternative-generator "Link to this heading")

_class_ random.Random([_seed_])[¶](https://docs.python.org/3/library/random.html#random.Random "Link to this definition")

Class that implements the default pseudo-random number generator used by the `random` module.
Changed in version 3.11: Formerly the _seed_ could be any hashable object. Now it is limited to: `None`, [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray").
Subclasses of `Random` should override the following methods if they wish to make use of a different basic generator:

seed(_a =None_, _version =2_)[¶](https://docs.python.org/3/library/random.html#random.Random.seed "Link to this definition")

Override this method in subclasses to customise the [`seed()`](https://docs.python.org/3/library/random.html#random.seed "random.seed") behaviour of `Random` instances.

getstate()[¶](https://docs.python.org/3/library/random.html#random.Random.getstate "Link to this definition")

Override this method in subclasses to customise the [`getstate()`](https://docs.python.org/3/library/random.html#random.getstate "random.getstate") behaviour of `Random` instances.

setstate(_state_)[¶](https://docs.python.org/3/library/random.html#random.Random.setstate "Link to this definition")

Override this method in subclasses to customise the [`setstate()`](https://docs.python.org/3/library/random.html#random.setstate "random.setstate") behaviour of `Random` instances.

random()[¶](https://docs.python.org/3/library/random.html#random.Random.random "Link to this definition")

Override this method in subclasses to customise the [`random()`](https://docs.python.org/3/library/random.html#random.random "random.random") behaviour of `Random` instances.
Optionally, a custom generator subclass can also supply the following method:

getrandbits(_k_)[¶](https://docs.python.org/3/library/random.html#random.Random.getrandbits "Link to this definition")

Override this method in subclasses to customise the [`getrandbits()`](https://docs.python.org/3/library/random.html#random.getrandbits "random.getrandbits") behaviour of `Random` instances.

randbytes(_n_)[¶](https://docs.python.org/3/library/random.html#random.Random.randbytes "Link to this definition")

Override this method in subclasses to customise the [`randbytes()`](https://docs.python.org/3/library/random.html#random.randbytes "random.randbytes") behaviour of `Random` instances.

_class_ random.SystemRandom([_seed_])[¶](https://docs.python.org/3/library/random.html#random.SystemRandom "Link to this definition")

Class that uses the [`os.urandom()`](https://docs.python.org/3/library/os.html#os.urandom "os.urandom") function for generating random numbers from sources provided by the operating system. Not available on all systems. Does not rely on software state, and sequences are not reproducible. Accordingly, the [`seed()`](https://docs.python.org/3/library/random.html#random.seed "random.seed") method has no effect and is ignored. The [`getstate()`](https://docs.python.org/3/library/random.html#random.getstate "random.getstate") and [`setstate()`](https://docs.python.org/3/library/random.html#random.setstate "random.setstate") methods raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") if called.
## Notes on Reproducibility[¶](https://docs.python.org/3/library/random.html#notes-on-reproducibility "Link to this heading")
Sometimes it is useful to be able to reproduce the sequences given by a pseudo-random number generator. By reusing a seed value, the same sequence should be reproducible from run to run as long as multiple threads are not running.
Most of the random module’s algorithms and seeding functions are subject to change across Python versions, but two aspects are guaranteed not to change:
  * If a new seeding method is added, then a backward compatible seeder will be offered.
  * The generator’s [`random()`](https://docs.python.org/3/library/random.html#random.Random.random "random.Random.random") method will continue to produce the same sequence when the compatible seeder is given the same seed.


## Examples[¶](https://docs.python.org/3/library/random.html#examples "Link to this heading")
Basic examples:
Copy```
>>> random()                          # Random float:  0.0 <= x < 1.0
0.37444887175646646

>>> uniform(2.5, 10.0)                # Random float:  2.5 <= x <= 10.0
3.1800146073117523

>>> expovariate(1 / 5)                # Interval between arrivals averaging 5 seconds
5.148957571865031

>>> randrange(10)                     # Integer from 0 to 9 inclusive
7

>>> randrange(0, 101, 2)              # Even integer from 0 to 100 inclusive
26

>>> choice(['win', 'lose', 'draw'])   # Single random element from a sequence
'draw'

>>> deck = 'ace two three four'.split()
>>> shuffle(deck)                     # Shuffle a list
>>> deck
['four', 'two', 'ace', 'three']

>>> sample([10, 20, 30, 40, 50], k=4) # Four samples without replacement
[40, 10, 50, 30]

```

Simulations:
Copy```
>>> # Six roulette wheel spins (weighted sampling with replacement)
>>> choices(['red', 'black', 'green'], [18, 18, 2], k=6)
['red', 'green', 'black', 'black', 'red', 'black']

>>> # Deal 20 cards without replacement from a deck
>>> # of 52 playing cards, and determine the proportion of cards
>>> # with a ten-value:  ten, jack, queen, or king.
>>> deal = sample(['tens', 'low cards'], counts=[16, 36], k=20)
>>> deal.count('tens') / 20
0.15

>>> # Estimate the probability of getting 5 or more heads from 7 spins
>>> # of a biased coin that settles on heads 60% of the time.
>>> sum(binomialvariate(n=7, p=0.6) >= 5 for i in range(10_000)) / 10_000
0.4169

>>> # Probability of the median of 5 samples being in middle two quartiles
>>> def trial():
...     return 2_500 <= sorted(choices(range(10_000), k=5))[2] < 7_500
...
>>> sum(trial() for i in range(10_000)) / 10_000
0.7958

```

Example of
Copy```
# https://www.thoughtco.com/example-of-bootstrapping-3126155
from statistics import fmean as mean
from random import choices

data = [41, 50, 29, 37, 81, 30, 73, 63, 20, 35, 68, 22, 60, 31, 95]
means = sorted(mean(choices(data, k=len(data))) for i in range(100))
print(f'The sample mean of {mean(data):.1f} has a 90% confidence '
      f'interval from {means[5]:.1f} to {means[94]:.1f}')

```

Example of a
Copy```
# Example from "Statistics is Easy" by Dennis Shasha and Manda Wilson
from statistics import fmean as mean
from random import shuffle

drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]
observed_diff = mean(drug) - mean(placebo)

n = 10_000
count = 0
combined = drug + placebo
for i in range(n):
    shuffle(combined)
    new_diff = mean(combined[:len(drug)]) - mean(combined[len(drug):])
    count += (new_diff >= observed_diff)

print(f'{n} label reshufflings produced only {count} instances with a difference')
print(f'at least as extreme as the observed difference of {observed_diff:.1f}.')
print(f'The one-sided p-value of {count / n:.4f} leads us to reject the null')
print(f'hypothesis that there is no difference between the drug and the placebo.')

```

Simulation of arrival times and service deliveries for a multiserver queue:
Copy```
from heapq import heapify, heapreplace
from random import expovariate, gauss
from statistics import mean, quantiles

average_arrival_interval = 5.6
average_service_time = 15.0
stdev_service_time = 3.5
num_servers = 3

waits = []
arrival_time = 0.0
servers = [0.0] * num_servers  # time when each server becomes available
heapify(servers)
for i in range(1_000_000):
    arrival_time += expovariate(1.0 / average_arrival_interval)
    next_server_available = servers[0]
    wait = max(0.0, next_server_available - arrival_time)
    waits.append(wait)
    service_duration = max(0.0, gauss(average_service_time, stdev_service_time))
    service_completed = arrival_time + wait + service_duration
    heapreplace(servers, service_completed)

print(f'Mean wait: {mean(waits):.1f}   Max wait: {max(waits):.1f}')
print('Quartiles:', [round(q, 1) for q in quantiles(waits)])

```

See also
## Recipes[¶](https://docs.python.org/3/library/random.html#recipes "Link to this heading")
These recipes show how to efficiently make random selections from the combinatoric iterators in the [`itertools`](https://docs.python.org/3/library/itertools.html#module-itertools "itertools: Functions creating iterators for efficient looping.") module:
Copy```
import random

def random_product(*iterables, repeat=1):
    "Random selection from itertools.product(*iterables, repeat=repeat)"
    pools = tuple(map(tuple, iterables)) * repeat
    return tuple(map(random.choice, pools))

def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))

def random_combination(iterable, r):
    "Random selection from itertools.combinations(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)

def random_combination_with_replacement(iterable, r):
    "Choose r elements with replacement.  Order the result to match the iterable."
    # Result will be in set(itertools.combinations_with_replacement(iterable, r)).
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.choices(range(n), k=r))
    return tuple(pool[i] for i in indices)

def random_derangement(iterable):
    "Choose a permutation where no element stays in its original position."
    seq = tuple(iterable)
    if len(seq) < 2:
        if not seq:
            return ()
        raise IndexError('No derangments to choose from')
    perm = list(range(len(seq)))
    start = tuple(perm)
    while True:
        random.shuffle(perm)
        if all(p != q for p, q in zip(start, perm)):
            return tuple([seq[i] for i in perm])

```

The default [`random()`](https://docs.python.org/3/library/random.html#random.random "random.random") returns multiples of 2⁻⁵³ in the range _0.0 ≤ x < 1.0_. All such numbers are evenly spaced and are exactly representable as Python floats. However, many other representable floats in that interval are not possible selections. For example, `0.05954861408025609` isn’t an integer multiple of 2⁻⁵³.
The following recipe takes a different approach. All floats in the interval are possible selections. The mantissa comes from a uniform distribution of integers in the range _2⁵² ≤ mantissa < 2⁵³_. The exponent comes from a geometric distribution where exponents smaller than _-53_ occur half as often as the next larger exponent.
Copy```
from random import Random
from math import ldexp

class FullRandom(Random):

    def random(self):
        mantissa = 0x10_0000_0000_0000 | self.getrandbits(52)
        exponent = -53
        x = 0
        while not x:
            x = self.getrandbits(32)
            exponent += x.bit_length() - 32
        return ldexp(mantissa, exponent)

```

All [real valued distributions](https://docs.python.org/3/library/random.html#real-valued-distributions) in the class will use the new method:
Copy```
>>> fr = FullRandom()
>>> fr.random()
0.05954861408025609
>>> fr.expovariate(0.25)
8.87925541791544

```

The recipe is conceptually equivalent to an algorithm that chooses from all the multiples of 2⁻¹⁰⁷⁴ in the range _0.0 ≤ x < 1.0_. All such numbers are evenly spaced, but most have to be rounded down to the nearest representable Python float. (The value 2⁻¹⁰⁷⁴ is the smallest positive unnormalized float and is equal to `math.ulp(0.0)`.)
See also
[`random()`](https://docs.python.org/3/library/random.html#random.random "random.random").
## Command-line usage[¶](https://docs.python.org/3/library/random.html#command-line-usage "Link to this heading")
Added in version 3.13.
The `random` module can be executed from the command line.
Copy```
python -m random [-h] [-c CHOICE [CHOICE ...] | -i N | -f N] [input ...]

```

The following options are accepted:

-h, --help[¶](https://docs.python.org/3/library/random.html#cmdoption-random-h "Link to this definition")

Show the help message and exit.

-c CHOICE [CHOICE ...][¶](https://docs.python.org/3/library/random.html#cmdoption-random-c "Link to this definition")


--choice CHOICE [CHOICE ...][¶](https://docs.python.org/3/library/random.html#cmdoption-random-choice "Link to this definition")

Print a random choice, using [`choice()`](https://docs.python.org/3/library/random.html#random.choice "random.choice").

-i <N>[¶](https://docs.python.org/3/library/random.html#cmdoption-random-i "Link to this definition")


--integer <N>[¶](https://docs.python.org/3/library/random.html#cmdoption-random-integer "Link to this definition")

Print a random integer between 1 and N inclusive, using [`randint()`](https://docs.python.org/3/library/random.html#random.randint "random.randint").

-f <N>[¶](https://docs.python.org/3/library/random.html#cmdoption-random-f "Link to this definition")


--float <N>[¶](https://docs.python.org/3/library/random.html#cmdoption-random-float "Link to this definition")

Print a random floating-point number between 0 and N inclusive, using [`uniform()`](https://docs.python.org/3/library/random.html#random.uniform "random.uniform").
If no options are given, the output depends on the input:
  * String or multiple: same as [`--choice`](https://docs.python.org/3/library/random.html#cmdoption-random-choice).
  * Integer: same as [`--integer`](https://docs.python.org/3/library/random.html#cmdoption-random-integer).
  * Float: same as [`--float`](https://docs.python.org/3/library/random.html#cmdoption-random-float).


## Command-line example[¶](https://docs.python.org/3/library/random.html#command-line-example "Link to this heading")
Here are some examples of the `random` command-line interface:
Copy```
$ # Choose one at random
$ python -m random egg bacon sausage spam "Lobster Thermidor aux crevettes with a Mornay sauce"
Lobster Thermidor aux crevettes with a Mornay sauce

$ # Random integer
$ python -m random 6
6

$ # Random floating-point number
$ python -m random 1.8
1.7080016272295635

$ # With explicit arguments
$ python  -m random --choice egg bacon sausage spam "Lobster Thermidor aux crevettes with a Mornay sauce"
egg

$ python -m random --integer 6
3

$ python -m random --float 1.8
1.5666339105010318

$ python -m random --integer 6
5

$ python -m random --float 6
3.1942323316565915

```

### [Table of Contents](https://docs.python.org/3/contents.html)
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


#### Previous topic
[`fractions` — Rational numbers](https://docs.python.org/3/library/fractions.html "previous chapter")
#### Next topic
[`statistics` — Mathematical statistics functions](https://docs.python.org/3/library/statistics.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=random+%E2%80%94+Generate+pseudo-random+numbers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Frandom.html&pagesource=library%2Frandom.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/statistics.html "statistics — Mathematical statistics functions") |
  * [previous](https://docs.python.org/3/library/fractions.html "fractions — Rational numbers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html) »
  * [`random` — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html)
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
