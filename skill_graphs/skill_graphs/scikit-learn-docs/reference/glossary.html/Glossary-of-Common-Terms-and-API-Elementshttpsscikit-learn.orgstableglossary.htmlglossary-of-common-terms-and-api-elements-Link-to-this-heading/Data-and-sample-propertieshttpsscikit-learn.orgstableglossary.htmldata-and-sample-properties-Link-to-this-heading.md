## Data and sample properties[#](https://scikit-learn.org/stable/glossary.html#data-and-sample-properties "Link to this heading")
See concept [sample property](https://scikit-learn.org/stable/glossary.html#term-sample-property).

`groups`[#](https://scikit-learn.org/stable/glossary.html#term-groups "Link to this term")

Used in cross-validation routines to identify samples that are correlated. Each value is an identifier such that, in a supporting [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter), samples from some `groups` value may not appear in both a training set and its corresponding test set. See [Cross-validation iterators for grouped data](https://scikit-learn.org/stable/modules/cross_validation.html#group-cv).

`sample_weight`[#](https://scikit-learn.org/stable/glossary.html#term-sample_weight "Link to this term")

A weight for each data point. Intuitively, if all weights are integers, using them in an estimator or a [scorer](https://scikit-learn.org/stable/glossary.html#term-scorer) is like duplicating each data point as many times as the weight value. Weights can also be specified as floats, and can have the same effect as above, as many estimators and scorers are scale invariant. For example, weights `[1, 2, 3]` would be equivalent to weights `[0.1, 0.2, 0.3]` as they differ by a constant factor of 10. Note however that several estimators are not invariant to the scale of weights.
`sample_weight` can be both an argument of the estimator’s [fit](https://scikit-learn.org/stable/glossary.html#term-fit) method for model training or a parameter of a [scorer](https://scikit-learn.org/stable/glossary.html#term-scorer) for model evaluation. These callables are said to _consume_ the sample weights while other components of scikit-learn can _route_ the weights to the underlying estimators or scorers (see [Metadata Routing](https://scikit-learn.org/stable/glossary.html#glossary-metadata-routing)).
Weighting samples can be useful in several contexts. For instance, if the training data is not uniformly sampled from the target population, it can be corrected by weighting the training data points based on the
Some model hyper-parameters are expressed in terms of a discrete number of data points in a region of the feature space. When fitting with sample weights, a count of data points is often automatically converted to a sum of their weights, but this is not always the case. Please refer to the model docstring for details.
In classification, weights can also be specified for all samples belonging to a given target class with the [class_weight](https://scikit-learn.org/stable/glossary.html#term-class_weight) estimator [parameter](https://scikit-learn.org/stable/glossary.html#term-parameter). If both `sample_weight` and `class_weight` are provided, the final weight assigned to a sample is the product of the two.
At the time of writing (version 1.8), not all scikit-learn estimators correctly implement the weight-repetition equivalence property. The
Furthermore, some estimators have a stochastic fit method. For instance, [`cluster.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans "sklearn.cluster.KMeans") depends on a random initialization, bagging models randomly resample from the training data, etc. In this case, the sample weight-repetition equivalence property described above does not hold exactly. However, it should hold at least in expectation over the randomness of the fitting procedure.

`X`[#](https://scikit-learn.org/stable/glossary.html#term-X "Link to this term")

Denotes data that is observed at training and prediction time, used as independent variables in learning. The notation is uppercase to denote that it is ordinarily a matrix (see [rectangular](https://scikit-learn.org/stable/glossary.html#term-rectangular)). When a matrix, each sample may be represented by a [feature](https://scikit-learn.org/stable/glossary.html#term-feature) vector, or a vector of [precomputed](https://scikit-learn.org/stable/glossary.html#term-precomputed) (dis)similarity with each training sample. `X` may also not be a matrix, and may require a [feature extractor](https://scikit-learn.org/stable/glossary.html#term-feature-extractor) or a [pairwise metric](https://scikit-learn.org/stable/glossary.html#term-pairwise-metric) to turn it into one before learning a model.

`Xt`[#](https://scikit-learn.org/stable/glossary.html#term-Xt "Link to this term")

Shorthand for “transformed [X](https://scikit-learn.org/stable/glossary.html#term-X)”.

`y`[#](https://scikit-learn.org/stable/glossary.html#term-y "Link to this term")


`Y`[#](https://scikit-learn.org/stable/glossary.html#term-Y "Link to this term")

Denotes data that may be observed at training time as the dependent variable in learning, but which is unavailable at prediction time, and is usually the [target](https://scikit-learn.org/stable/glossary.html#term-target) of prediction. The notation may be uppercase to denote that it is a matrix, representing [multi-output](https://scikit-learn.org/stable/glossary.html#term-multi-output) targets, for instance; but usually we use `y` and sometimes do so even when multiple outputs are assumed.
[ previous Older Versions ](https://scikit-learn.org/stable/whats_new/older_versions.html "previous page") [ next Frequently Asked Questions ](https://scikit-learn.org/stable/faq.html "next page")
On this page
  * [General Concepts](https://scikit-learn.org/stable/glossary.html#general-concepts)
  * [Class APIs and Estimator Types](https://scikit-learn.org/stable/glossary.html#class-apis-and-estimator-types)
  * [Metadata Routing](https://scikit-learn.org/stable/glossary.html#metadata-routing)
  * [Target Types](https://scikit-learn.org/stable/glossary.html#target-types)
  * [Methods](https://scikit-learn.org/stable/glossary.html#methods)
  * [Parameters](https://scikit-learn.org/stable/glossary.html#parameters)
  * [Attributes](https://scikit-learn.org/stable/glossary.html#attributes)
  * [Data and sample properties](https://scikit-learn.org/stable/glossary.html#data-and-sample-properties)


### This Page
  * [Show Source](https://scikit-learn.org/stable/_sources/glossary.rst.txt)


© Copyright 2007 - 2025, scikit-learn developers (BSD License).
