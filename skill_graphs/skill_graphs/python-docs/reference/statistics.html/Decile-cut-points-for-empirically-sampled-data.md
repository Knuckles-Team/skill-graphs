# Decile cut points for empirically sampled data
>>> data = [105, 129, 87, 86, 111, 111, 89, 81, 108, 92, 110,
...         100, 75, 105, 103, 109, 76, 119, 99, 91, 103, 129,
...         106, 101, 84, 111, 74, 87, 86, 103, 103, 106, 86,
...         111, 75, 87, 102, 121, 111, 88, 89, 101, 106, 95,
...         103, 107, 101, 81, 109, 104]
>>> [round(q, 1) for q in quantiles(data, n=10)]
[81.0, 86.2, 89.0, 99.4, 102.5, 103.6, 106.0, 109.8, 111.0]

```

Added in version 3.8.
Changed in version 3.13: No longer raises an exception for an input with only a single data point. This allows quantile estimates to be built up one sample point at a time becoming gradually more refined with each new data point.

statistics.covariance(_x_ , _y_ , _/_)[¶](https://docs.python.org/3/library/statistics.html#statistics.covariance "Link to this definition")

Return the sample covariance of two inputs _x_ and _y_. Covariance is a measure of the joint variability of two inputs.
Both inputs must be of the same length (no less than two), otherwise [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError") is raised.
Examples:
Copy```
>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> covariance(x, y)
0.75
>>> z = [9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> covariance(x, z)
-7.5
>>> covariance(z, x)
-7.5

```

Added in version 3.10.

statistics.correlation(_x_ , _y_ , _/_ , _*_ , _method ='linear'_)[¶](https://docs.python.org/3/library/statistics.html#statistics.correlation "Link to this definition")

Return the _r_ takes values between -1 and +1. It measures the strength and direction of a linear relationship.
If _method_ is “ranked”, computes
Spearman’s correlation coefficient is appropriate for ordinal data or for continuous data that doesn’t meet the linear proportion requirement for Pearson’s correlation coefficient.
Both inputs must be of the same length (no less than two), and need not to be constant, otherwise [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError") is raised.
Example with
Copy```
>>> # Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and  Neptune
>>> orbital_period = [88, 225, 365, 687, 4331, 10_756, 30_687, 60_190]    # days
>>> dist_from_sun = [58, 108, 150, 228, 778, 1_400, 2_900, 4_500] # million km

>>> # Show that a perfect monotonic relationship exists
>>> correlation(orbital_period, dist_from_sun, method='ranked')
1.0

>>> # Observe that a linear relationship is imperfect
>>> round(correlation(orbital_period, dist_from_sun), 4)
0.9882

>>> # Demonstrate Kepler's third law: There is a linear correlation
>>> # between the square of the orbital period and the cube of the
>>> # distance from the sun.
>>> period_squared = [p * p for p in orbital_period]
>>> dist_cubed = [d * d * d for d in dist_from_sun]
>>> round(correlation(period_squared, dist_cubed), 4)
1.0

```

Added in version 3.10.
Changed in version 3.12: Added support for Spearman’s rank correlation coefficient.

statistics.linear_regression(_x_ , _y_ , _/_ , _*_ , _proportional =False_)[¶](https://docs.python.org/3/library/statistics.html#statistics.linear_regression "Link to this definition")

Return the slope and intercept of _x_ and a dependent variable _y_ in terms of this linear function:
> _y = slope * x + intercept + noise_
where `slope` and `intercept` are the regression parameters that are estimated, and `noise` represents the variability of the data that was not explained by the linear regression (it is equal to the difference between predicted and actual values of the dependent variable).
Both inputs must be of the same length (no less than two), and the independent variable _x_ cannot be constant; otherwise a [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError") is raised.
For example, we can use the
Copy```
>>> year = [1971, 1975, 1979, 1982, 1983]
>>> films_total = [1, 2, 3, 4, 5]
>>> slope, intercept = linear_regression(year, films_total)
>>> round(slope * 2019 + intercept)
16

```

If _proportional_ is true, the independent variable _x_ and the dependent variable _y_ are assumed to be directly proportional. The data is fit to a line passing through the origin. Since the _intercept_ will always be 0.0, the underlying linear function simplifies to:
> _y = slope * x + noise_
Continuing the example from [`correlation()`](https://docs.python.org/3/library/statistics.html#statistics.correlation "statistics.correlation"), we look to see how well a model based on major planets can predict the orbital distances for dwarf planets:
Copy```
>>> model = linear_regression(period_squared, dist_cubed, proportional=True)
>>> slope = model.slope

>>> # Dwarf planets:   Pluto,  Eris,    Makemake, Haumea, Ceres
>>> orbital_periods = [90_560, 204_199, 111_845, 103_410, 1_680]  # days
>>> predicted_dist = [math.cbrt(slope * (p * p)) for p in orbital_periods]
>>> list(map(round, predicted_dist))
[5912, 10166, 6806, 6459, 414]

>>> [5_906, 10_152, 6_796, 6_450, 414]  # actual distance in million km
[5906, 10152, 6796, 6450, 414]

```

Added in version 3.10.
Changed in version 3.11: Added support for _proportional_.
## Exceptions[¶](https://docs.python.org/3/library/statistics.html#exceptions "Link to this heading")
A single exception is defined:

_exception_ statistics.StatisticsError[¶](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "Link to this definition")

Subclass of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") for statistics-related exceptions.
##  [`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist") objects[¶](https://docs.python.org/3/library/statistics.html#normaldist-objects "Link to this heading")
[`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist") is a tool for creating and manipulating normal distributions of a
Normal distributions arise from the

_class_ statistics.NormalDist(_mu =0.0_, _sigma =1.0_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "Link to this definition")

Returns a new _NormalDist_ object where _mu_ represents the _sigma_ represents the
If _sigma_ is negative, raises [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError").

mean[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.mean "Link to this definition")

A read-only property for the

median[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.median "Link to this definition")

A read-only property for the

mode[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.mode "Link to this definition")

A read-only property for the

stdev[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.stdev "Link to this definition")

A read-only property for the

variance[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.variance "Link to this definition")

A read-only property for the

_classmethod_ from_samples(_data_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.from_samples "Link to this definition")

Makes a normal distribution instance with _mu_ and _sigma_ parameters estimated from the _data_ using [`fmean()`](https://docs.python.org/3/library/statistics.html#statistics.fmean "statistics.fmean") and [`stdev()`](https://docs.python.org/3/library/statistics.html#statistics.stdev "statistics.stdev").
The _data_ can be any [iterable](https://docs.python.org/3/glossary.html#term-iterable) and should consist of values that can be converted to type [`float`](https://docs.python.org/3/library/functions.html#float "float"). If _data_ does not contain at least two elements, raises [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError") because it takes at least one point to estimate a central value and at least two points to estimate dispersion.

samples(_n_ , _*_ , _seed =None_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.samples "Link to this definition")

Generates _n_ random samples for a given mean and standard deviation. Returns a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") of [`float`](https://docs.python.org/3/library/functions.html#float "float") values.
If _seed_ is given, creates a new instance of the underlying random number generator. This is useful for creating reproducible results, even in a multi-threading context.
Changed in version 3.13.
Switched to a faster algorithm. To reproduce samples from previous versions, use [`random.seed()`](https://docs.python.org/3/library/random.html#random.seed "random.seed") and [`random.gauss()`](https://docs.python.org/3/library/random.html#random.gauss "random.gauss").

pdf(_x_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.pdf "Link to this definition")

Using a _X_ will be near the given value _x_. Mathematically, it is the limit of the ratio `P(x <= X < x+dx) / dx` as _dx_ approaches zero.
The relative likelihood is computed as the probability of a sample occurring in a narrow range divided by the width of the range (hence the word “density”). Since the likelihood is relative to other points, its value can be greater than `1.0`.

cdf(_x_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.cdf "Link to this definition")

Using a _X_ will be less than or equal to _x_. Mathematically, it is written `P(X <= x)`.

inv_cdf(_p_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.inv_cdf "Link to this definition")

Compute the inverse cumulative distribution function, also known as the `x : P(X <= x) = p`.
Finds the value _x_ of the random variable _X_ such that the probability of the variable being less than or equal to that value equals the given probability _p_.

overlap(_other_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.overlap "Link to this definition")

Measures the agreement between two normal probability distributions. Returns a value between 0.0 and 1.0 giving

quantiles(_n =4_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.quantiles "Link to this definition")

Divide the normal distribution into _n_ continuous intervals with equal probability. Returns a list of (n - 1) cut points separating the intervals.
Set _n_ to 4 for quartiles (the default). Set _n_ to 10 for deciles. Set _n_ to 100 for percentiles which gives the 99 cuts points that separate the normal distribution into 100 equal sized groups.

zscore(_x_)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.zscore "Link to this definition")

Compute the _x_ in terms of the number of standard deviations above or below the mean of the normal distribution: `(x - mean) / stdev`.
Added in version 3.9.
Instances of `NormalDist` support addition, subtraction, multiplication and division by a constant. These operations are used for translation and scaling. For example:
Copy```
>>> temperature_february = NormalDist(5, 2.5)             # Celsius
>>> temperature_february * (9/5) + 32                     # Fahrenheit
NormalDist(mu=41.0, sigma=4.5)

```

Dividing a constant by an instance of `NormalDist` is not supported because the result wouldn’t be normally distributed.
Since normal distributions arise from additive effects of independent variables, it is possible to `NormalDist`. For example:
Copy```
>>> birth_weights = NormalDist.from_samples([2.5, 3.1, 2.1, 2.4, 2.7, 3.5])
>>> drug_effects = NormalDist(0.4, 0.15)
>>> combined = birth_weights + drug_effects
>>> round(combined.mean, 1)
3.1
>>> round(combined.stdev, 1)
0.5

```

Added in version 3.8.
## Examples and Recipes[¶](https://docs.python.org/3/library/statistics.html#examples-and-recipes "Link to this heading")
### Classic probability problems[¶](https://docs.python.org/3/library/statistics.html#classic-probability-problems "Link to this heading")
[`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist") readily solves classic probability problems.
For example, given
Copy```
>>> sat = NormalDist(1060, 195)
>>> fraction = sat.cdf(1200 + 0.5) - sat.cdf(1100 - 0.5)
>>> round(fraction * 100.0, 1)
18.4

```

Find the
Copy```
>>> list(map(round, sat.quantiles()))
[928, 1060, 1192]
>>> list(map(round, sat.quantiles(n=10)))
[810, 896, 958, 1011, 1060, 1109, 1162, 1224, 1310]

```

### Monte Carlo inputs for simulations[¶](https://docs.python.org/3/library/statistics.html#monte-carlo-inputs-for-simulations "Link to this heading")
To estimate the distribution for a model that isn’t easy to solve analytically, [`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist") can generate input samples for a
Copy```
>>> def model(x, y, z):
...     return (3*x + 7*x*y - 5*y) / (11 * z)
...
>>> n = 100_000
>>> X = NormalDist(10, 2.5).samples(n, seed=3652260728)
>>> Y = NormalDist(15, 1.75).samples(n, seed=4582495471)
>>> Z = NormalDist(50, 1.25).samples(n, seed=6582483453)
>>> quantiles(map(model, X, Y, Z))
[1.4591308524824727, 1.8035946855390597, 2.175091447274739]

```

### Approximating binomial distributions[¶](https://docs.python.org/3/library/statistics.html#approximating-binomial-distributions "Link to this heading")
Normal distributions can be used to approximate
For example, an open source conference has 750 attendees and two rooms with a 500 person capacity. There is a talk about Python and another about Ruby. In previous conferences, 65% of the attendees preferred to listen to Python talks. Assuming the population preferences haven’t changed, what is the probability that the Python room will stay within its capacity limits?
Copy```
>>> n = 750             # Sample size
>>> p = 0.65            # Preference for Python
>>> q = 1.0 - p         # Preference for Ruby
>>> k = 500             # Room capacity

>>> # Approximation using the cumulative normal distribution
>>> from math import sqrt
>>> round(NormalDist(mu=n*p, sigma=sqrt(n*p*q)).cdf(k + 0.5), 4)
0.8402

>>> # Exact solution using the cumulative binomial distribution
>>> from math import comb, fsum
>>> round(fsum(comb(n, r) * p**r * q**(n-r) for r in range(k+1)), 4)
0.8402

>>> # Approximation using a simulation
>>> from random import seed, binomialvariate
>>> seed(8675309)
>>> mean(binomialvariate(n, p) <= k for i in range(10_000))
0.8406

```

### Naive bayesian classifier[¶](https://docs.python.org/3/library/statistics.html#naive-bayesian-classifier "Link to this heading")
Normal distributions commonly arise in machine learning problems.
Wikipedia has a
We’re given a training dataset with measurements for eight people. The measurements are assumed to be normally distributed, so we summarize the data with [`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist"):
Copy```
>>> height_male = NormalDist.from_samples([6, 5.92, 5.58, 5.92])
>>> height_female = NormalDist.from_samples([5, 5.5, 5.42, 5.75])
>>> weight_male = NormalDist.from_samples([180, 190, 170, 165])
>>> weight_female = NormalDist.from_samples([100, 150, 130, 150])
>>> foot_size_male = NormalDist.from_samples([12, 11, 12, 10])
>>> foot_size_female = NormalDist.from_samples([6, 8, 7, 9])

```

Next, we encounter a new person whose feature measurements are known but whose gender is unknown:
Copy```
>>> ht = 6.0        # height
>>> wt = 130        # weight
>>> fs = 8          # foot size

```

Starting with a 50%
Copy```
>>> prior_male = 0.5
>>> prior_female = 0.5
>>> posterior_male = (prior_male * height_male.pdf(ht) *
...                   weight_male.pdf(wt) * foot_size_male.pdf(fs))

>>> posterior_female = (prior_female * height_female.pdf(ht) *
...                     weight_female.pdf(wt) * foot_size_female.pdf(fs))

```

The final prediction goes to the largest posterior. This is known as the
Copy```
>>> 'male' if posterior_male > posterior_female else 'female'
'female'

```

### [Table of Contents](https://docs.python.org/3/contents.html)
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
[`random` — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html "previous chapter")
#### Next topic
[Functional Programming Modules](https://docs.python.org/3/library/functional.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=statistics+%E2%80%94+Mathematical+statistics+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fstatistics.html&pagesource=library%2Fstatistics.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/functional.html "Functional Programming Modules") |
  * [previous](https://docs.python.org/3/library/random.html "random — Generate pseudo-random numbers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Numeric and Mathematical Modules](https://docs.python.org/3/library/numeric.html) »
  * [`statistics` — Mathematical statistics functions](https://docs.python.org/3/library/statistics.html)
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
  *[/]: Positional-only parameter separator (PEP 570)
