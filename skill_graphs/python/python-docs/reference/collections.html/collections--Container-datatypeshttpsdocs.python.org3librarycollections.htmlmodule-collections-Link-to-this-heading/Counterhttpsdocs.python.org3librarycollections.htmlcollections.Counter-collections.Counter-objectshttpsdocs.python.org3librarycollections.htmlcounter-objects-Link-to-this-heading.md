##  [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter") objects[¶](https://docs.python.org/3/library/collections.html#counter-objects "Link to this heading")
A counter tool is provided to support convenient and rapid tallies. For example:
Copy```
>>> # Tally occurrences of words in a list
>>> cnt = Counter()
>>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
...     cnt[word] += 1
...
>>> cnt
Counter({'blue': 3, 'red': 2, 'green': 1})

>>> # Find the ten most common words in Hamlet
>>> import re
>>> words = re.findall(r'\w+', open('hamlet.txt').read().lower())
>>> Counter(words).most_common(10)
[('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631),
 ('you', 554),  ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

```


_class_ collections.Counter([_iterable-or-mapping_])[¶](https://docs.python.org/3/library/collections.html#collections.Counter "Link to this definition")

A `Counter` is a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") subclass for counting [hashable](https://docs.python.org/3/glossary.html#term-hashable) objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The `Counter` class is similar to bags or multisets in other languages.
Elements are counted from an _iterable_ or initialized from another _mapping_ (or counter):
Copy```
>>> c = Counter()                           # a new, empty counter
>>> c = Counter('gallahad')                 # a new counter from an iterable
>>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
>>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args

```

Counter objects have a dictionary interface except that they return a zero count for missing items instead of raising a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError"):
Copy```
>>> c = Counter(['eggs', 'ham'])
>>> c['bacon']                              # count of a missing element is zero
0

```

Setting a count to zero does not remove an element from a counter. Use `del` to remove it entirely:
Copy```
>>> c['sausage'] = 0                        # counter entry with a zero count
>>> del c['sausage']                        # del actually removes the entry

```

Added in version 3.1.
Changed in version 3.7: As a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") subclass, `Counter` inherited the capability to remember insertion order. Math operations on _Counter_ objects also preserve order. Results are ordered according to when an element is first encountered in the left operand and then by the order encountered in the right operand.
Counter objects support additional methods beyond those available for all dictionaries:

elements()[¶](https://docs.python.org/3/library/collections.html#collections.Counter.elements "Link to this definition")

Return an iterator over elements repeating each as many times as its count. Elements are returned in the order first encountered. If an element’s count is less than one, `elements()` will ignore it.
Copy```
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> sorted(c.elements())
['a', 'a', 'a', 'a', 'b', 'b']

```


most_common([_n_])[¶](https://docs.python.org/3/library/collections.html#collections.Counter.most_common "Link to this definition")

Return a list of the _n_ most common elements and their counts from the most common to the least. If _n_ is omitted or `None`, `most_common()` returns _all_ elements in the counter. Elements with equal counts are ordered in the order first encountered:
Copy```
>>> Counter('abracadabra').most_common(3)
[('a', 5), ('b', 2), ('r', 2)]

```


subtract([_iterable-or-mapping_])[¶](https://docs.python.org/3/library/collections.html#collections.Counter.subtract "Link to this definition")

Elements are subtracted from an _iterable_ or from another _mapping_ (or counter). Like [`dict.update()`](https://docs.python.org/3/library/stdtypes.html#dict.update "dict.update") but subtracts counts instead of replacing them. Both inputs and outputs may be zero or negative.
Copy```
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> d = Counter(a=1, b=2, c=3, d=4)
>>> c.subtract(d)
>>> c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

```

Added in version 3.2.

total()[¶](https://docs.python.org/3/library/collections.html#collections.Counter.total "Link to this definition")

Compute the sum of the counts.
Copy```
>>> c = Counter(a=10, b=5, c=0)
>>> c.total()
15

```

Added in version 3.10.
The usual dictionary methods are available for `Counter` objects except for two which work differently for counters.

fromkeys(_iterable_)[¶](https://docs.python.org/3/library/collections.html#collections.Counter.fromkeys "Link to this definition")

This class method is not implemented for `Counter` objects.

update([_iterable-or-mapping_])[¶](https://docs.python.org/3/library/collections.html#collections.Counter.update "Link to this definition")

Elements are counted from an _iterable_ or added-in from another _mapping_ (or counter). Like [`dict.update()`](https://docs.python.org/3/library/stdtypes.html#dict.update "dict.update") but adds counts instead of replacing them. Also, the _iterable_ is expected to be a sequence of elements, not a sequence of `(key, value)` pairs.
Counters support rich comparison operators for equality, subset, and superset relationships: `==`, `!=`, `<`, `<=`, `>`, `>=`. All of those tests treat missing elements as having zero counts so that `Counter(a=1) == Counter(a=1, b=0)` returns true.
Changed in version 3.10: Rich comparison operations were added.
Changed in version 3.10: In equality tests, missing elements are treated as having zero counts. Formerly, `Counter(a=3)` and `Counter(a=3, b=0)` were considered distinct.
Common patterns for working with [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter") objects:
Copy```
c.total()                       # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # access the (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts

```

Several mathematical operations are provided for combining [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter") objects to produce multisets (counters that have counts greater than zero). Addition and subtraction combine counters by adding or subtracting the counts of corresponding elements. Intersection and union return the minimum and maximum of corresponding counts. Equality and inclusion compare corresponding counts. Each operation can accept inputs with signed counts, but the output will exclude results with counts of zero or less.
Copy```
>>> c = Counter(a=3, b=1)
>>> d = Counter(a=1, b=2)
>>> c + d                       # add two counters together:  c[x] + d[x]
Counter({'a': 4, 'b': 3})
>>> c - d                       # subtract (keeping only positive counts)
Counter({'a': 2})
>>> c & d                       # intersection:  min(c[x], d[x])
Counter({'a': 1, 'b': 1})
>>> c | d                       # union:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})
>>> c == d                      # equality:  c[x] == d[x]
False
>>> c <= d                      # inclusion:  c[x] <= d[x]
False

```

Unary addition and subtraction are shortcuts for adding an empty counter or subtracting from an empty counter.
Copy```
>>> c = Counter(a=2, b=-4)
>>> +c
Counter({'a': 2})
>>> -c
Counter({'b': 4})

```

Added in version 3.3: Added support for unary plus, unary minus, and in-place multiset operations.
Note
Counters were primarily designed to work with positive integers to represent running counts; however, care was taken to not unnecessarily preclude use cases needing other types or negative values. To help with those use cases, this section documents the minimum range and type restrictions.
  * The [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter") class itself is a dictionary subclass with no restrictions on its keys and values. The values are intended to be numbers representing counts, but you _could_ store anything in the value field.
  * The [`most_common()`](https://docs.python.org/3/library/collections.html#collections.Counter.most_common "collections.Counter.most_common") method requires only that the values be orderable.
  * For in-place operations such as `c[key] += 1`, the value type need only support addition and subtraction. So fractions, floats, and decimals would work and negative values are supported. The same is also true for [`update()`](https://docs.python.org/3/library/collections.html#collections.Counter.update "collections.Counter.update") and [`subtract()`](https://docs.python.org/3/library/collections.html#collections.Counter.subtract "collections.Counter.subtract") which allow negative and zero values for both inputs and outputs.
  * The multiset methods are designed only for use cases with positive values. The inputs may be negative or zero, but only outputs with positive values are created. There are no type restrictions, but the value type needs to support addition, subtraction, and comparison.
  * The [`elements()`](https://docs.python.org/3/library/collections.html#collections.Counter.elements "collections.Counter.elements") method requires integer counts. It ignores zero and negative counts.


See also
  * Wikipedia entry for
  * For mathematical operations on multisets and their use cases, see _Knuth, Donald. The Art of Computer Programming Volume II, Section 4.6.3, Exercise 19_.
  * To enumerate all distinct multisets of a given size over a given set of elements, see [`itertools.combinations_with_replacement()`](https://docs.python.org/3/library/itertools.html#itertools.combinations_with_replacement "itertools.combinations_with_replacement"):
Copy```
map(Counter, combinations_with_replacement('ABC', 2)) # --> AA AB AC BB BC CC

```
