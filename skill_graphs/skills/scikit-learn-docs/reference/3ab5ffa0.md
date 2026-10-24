## General Concepts[#](https://scikit-learn.org/stable/glossary.html#general-concepts "Link to this heading")

1d[#](https://scikit-learn.org/stable/glossary.html#term-1d "Link to this term")


1d array[#](https://scikit-learn.org/stable/glossary.html#term-1d-array "Link to this term")

One-dimensional array. A NumPy array whose `.shape` has length 1. A vector.

2d[#](https://scikit-learn.org/stable/glossary.html#term-2d "Link to this term")


2d array[#](https://scikit-learn.org/stable/glossary.html#term-2d-array "Link to this term")

Two-dimensional array. A NumPy array whose `.shape` has length 2. Often represents a matrix.

API[#](https://scikit-learn.org/stable/glossary.html#term-API "Link to this term")

Refers to both the _specific_ interfaces for estimators implemented in Scikit-learn and the _generalized_ conventions across types of estimators as described in this glossary and [overviewed in the contributor documentation](https://scikit-learn.org/stable/developers/develop.html#api-overview).
The specific interfaces that constitute Scikit-learn’s public API are largely documented in [API Reference](https://scikit-learn.org/stable/api/index.html#api-ref). However, we less formally consider anything as public API if none of the identifiers required to access it begins with `_`. We generally try to maintain [backwards compatibility](https://scikit-learn.org/stable/glossary.html#term-backwards-compatibility) for all objects in the public API.
Private API, including functions, modules and methods beginning `_` are not assured to be stable.

array-like[#](https://scikit-learn.org/stable/glossary.html#term-array-like "Link to this term")

The most common data format for _input_ to Scikit-learn estimators and functions, array-like is any type object for which
This includes:
  * a numpy array
  * a list of numbers
  * a list of length-k lists of numbers for some fixed length k
  * a
  * a numeric


Other array API inputs, but see [Array API support (experimental)](https://scikit-learn.org/stable/modules/array_api.html#array-api) for the preferred way of using these:
  * a
  * a


It excludes:
  * a [sparse matrix](https://scikit-learn.org/stable/glossary.html#term-sparse-matrix)
  * a sparse array
  * an iterator
  * a generator


Note that _output_ from scikit-learn estimators and functions (e.g. predictions) should generally be arrays or sparse matrices, or lists thereof (as in multi-output [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")’s `predict_proba`). An estimator where `predict()` returns a list or a `pandas.Series` is not valid.

attribute[#](https://scikit-learn.org/stable/glossary.html#term-attribute "Link to this term")


attributes[#](https://scikit-learn.org/stable/glossary.html#term-attributes "Link to this term")

We mostly use attribute to refer to how model information is stored on an estimator during fitting. Any public attribute stored on an estimator instance is required to begin with an alphabetic character and end in a single underscore if it is set in [fit](https://scikit-learn.org/stable/glossary.html#term-fit) or [partial_fit](https://scikit-learn.org/stable/glossary.html#term-partial_fit). These are what is documented under an estimator’s _Attributes_ documentation. The information stored in attributes is usually either: sufficient statistics used for prediction or transformation; [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive) outputs such as [labels_](https://scikit-learn.org/stable/glossary.html#term-labels_) or [embedding_](https://scikit-learn.org/stable/glossary.html#term-embedding_); or diagnostic data, such as [feature_importances_](https://scikit-learn.org/stable/glossary.html#term-feature_importances_). Common attributes are listed [below](https://scikit-learn.org/stable/glossary.html#glossary-attributes).
A public attribute may have the same name as a constructor [parameter](https://scikit-learn.org/stable/glossary.html#term-parameter), with a `_` appended. This is used to store a validated or estimated version of the user’s input. For example, [`decomposition.PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA") is constructed with an `n_components` parameter. From this, together with other parameters and the data, PCA estimates the attribute `n_components_`.
Further private attributes used in prediction/transformation/etc. may also be set when fitting. These begin with a single underscore and are not assured to be stable for public access.
A public attribute on an estimator instance that does not end in an underscore should be the stored, unmodified value of an `__init__` [parameter](https://scikit-learn.org/stable/glossary.html#term-parameter) of the same name. Because of this equivalence, these are documented under an estimator’s _Parameters_ documentation.

backwards compatibility[#](https://scikit-learn.org/stable/glossary.html#term-backwards-compatibility "Link to this term")

We generally try to maintain backward compatibility (i.e. interfaces and behaviors may be extended but not changed or removed) from release to release but this comes with some exceptions:

Public API only

The behavior of objects accessed through private identifiers (those beginning `_`) may be changed arbitrarily between versions.

As documented

We will generally assume that the users have adhered to the documented parameter types and ranges. If the documentation asks for a list and the user gives a tuple, we do not assure consistent behavior from version to version.

Deprecation

Behaviors may change following a [deprecation](https://scikit-learn.org/stable/glossary.html#term-deprecation) period (usually two releases long). Warnings are issued using Python’s

Keyword arguments

We may sometimes assume that all optional parameters (other than X and y to [fit](https://scikit-learn.org/stable/glossary.html#term-fit) and similar methods) are passed as keyword arguments only and may be positionally reordered.

Bug fixes and enhancements

Bug fixes and – less often – enhancements may change the behavior of estimators, including the predictions of an estimator trained on the same data and [random_state](https://scikit-learn.org/stable/glossary.html#term-random_state). When this happens, we attempt to note it clearly in the changelog.

Serialization

We make no assurances that pickling an estimator in one version will allow it to be unpickled to an equivalent model in the subsequent version. (For estimators in the sklearn package, we issue a warning when this unpickling is attempted, even if it may happen to work.) See [Security & Maintainability Limitations](https://scikit-learn.org/stable/model_persistence.html#persistence-limitations).

[`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator")

We provide limited backwards compatibility assurances for the estimator checks: we may add extra requirements on estimators tested with this function, usually when these were informally assumed but not formally tested.
Despite this informal contract with our users, the software is provided as is, as stated in the license. When a release inadvertently introduces changes that are not backward compatible, these are known as software regressions.

callable[#](https://scikit-learn.org/stable/glossary.html#term-callable "Link to this term")

A function, class or an object which implements the `__call__` method; anything that returns True when the argument of

categorical feature[#](https://scikit-learn.org/stable/glossary.html#term-categorical-feature "Link to this term")

A categorical or nominal [feature](https://scikit-learn.org/stable/glossary.html#term-feature) is one that has a finite set of discrete values across the population of data. These are commonly represented as columns of integers or strings. Strings will be rejected by most scikit-learn estimators, and integers will be treated as ordinal or count-valued. For the use with most estimators, categorical variables should be one-hot encoded. Notable exceptions include tree-based models such as random forests and gradient boosting models that often work better and faster with integer-coded categorical variables. [`OrdinalEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder "sklearn.preprocessing.OrdinalEncoder") helps encoding string-valued categorical features as ordinal integers, and [`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder "sklearn.preprocessing.OneHotEncoder") can be used to one-hot encode categorical features. See also [Encoding categorical features](https://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-categorical-features) and the

clone[#](https://scikit-learn.org/stable/glossary.html#term-clone "Link to this term")


cloned[#](https://scikit-learn.org/stable/glossary.html#term-cloned "Link to this term")

To copy an [estimator instance](https://scikit-learn.org/stable/glossary.html#term-estimator-instance) and create a new one with identical [parameters](https://scikit-learn.org/stable/glossary.html#term-parameters), but without any fitted [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes), using [`clone`](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone "sklearn.base.clone").
When `fit` is called, a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator) usually clones a wrapped estimator instance before fitting the cloned instance. (Exceptions, for legacy reasons, include [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline") and [`FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion").)
If the estimator’s `random_state` parameter is an integer (or if the estimator doesn’t have a `random_state` parameter), an _exact clone_ is returned: the clone and the original estimator will give the exact same results. Otherwise, _statistical clone_ is returned: the clone might yield different results from the original estimator. More details can be found in [Controlling randomness](https://scikit-learn.org/stable/common_pitfalls.html#randomness).

common tests[#](https://scikit-learn.org/stable/glossary.html#term-common-tests "Link to this term")

This refers to the tests run on almost every estimator class in Scikit-learn to check they comply with basic API conventions. They are available for external use through [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator") or [`utils.estimator_checks.parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks"), with most of the implementation in `sklearn/utils/estimator_checks.py`.
Note: Some exceptions to the common testing regime are currently hard-coded into the library, but we hope to replace this by marking exceptional behaviours on the estimator using semantic [estimator tags](https://scikit-learn.org/stable/glossary.html#term-estimator-tags).

cross-fitting[#](https://scikit-learn.org/stable/glossary.html#term-cross-fitting "Link to this term")


cross fitting[#](https://scikit-learn.org/stable/glossary.html#term-0 "Link to this term")

A resampling method that iteratively partitions data into mutually exclusive subsets to fit two stages. During the first stage, the mutually exclusive subsets enable predictions or transformations to be computed on data not seen during training. The computed data is then used in the second stage. The objective is to avoid having any overfitting in the first stage introduce bias into the input data distribution of the second stage. For examples of its use, see: [`TargetEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.TargetEncoder.html#sklearn.preprocessing.TargetEncoder "sklearn.preprocessing.TargetEncoder"), [`StackingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html#sklearn.ensemble.StackingClassifier "sklearn.ensemble.StackingClassifier"), [`StackingRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingRegressor.html#sklearn.ensemble.StackingRegressor "sklearn.ensemble.StackingRegressor") and [`CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV").

cross-validation[#](https://scikit-learn.org/stable/glossary.html#term-cross-validation "Link to this term")


cross validation[#](https://scikit-learn.org/stable/glossary.html#term-1 "Link to this term")

A resampling method that iteratively partitions data into mutually exclusive ‘train’ and ‘test’ subsets so model performance can be evaluated on unseen data. This conserves data as avoids the need to hold out a ‘validation’ dataset and accounts for variability as multiple rounds of cross validation are generally performed. See [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation) for more details.

deprecation[#](https://scikit-learn.org/stable/glossary.html#term-deprecation "Link to this term")

We use deprecation to slowly violate our [backwards compatibility](https://scikit-learn.org/stable/glossary.html#term-backwards-compatibility) assurances, usually to:
  * change the default value of a parameter; or
  * remove a parameter, attribute, method, class, etc.


We will ordinarily issue a warning when a deprecated element is used, although there may be limitations to this. For instance, we will raise a warning when someone sets a parameter that has been deprecated, but may not when they access that parameter’s attribute on the estimator instance.
See the [Contributors’ Guide](https://scikit-learn.org/stable/developers/contributing.html#contributing-deprecation).

dimensionality[#](https://scikit-learn.org/stable/glossary.html#term-dimensionality "Link to this term")

May be used to refer to the number of [features](https://scikit-learn.org/stable/glossary.html#term-features) (i.e. [n_features](https://scikit-learn.org/stable/glossary.html#term-n_features)), or columns in a 2d feature matrix. Dimensions are, however, also used to refer to the length of a NumPy array’s shape, distinguishing a 1d array from a 2d matrix.

docstring[#](https://scikit-learn.org/stable/glossary.html#term-docstring "Link to this term")

The embedded documentation for a module, class, function, etc., usually in code as a string at the beginning of the object’s definition, and accessible as the object’s `__doc__` attribute.
We try to adhere to

double underscore[#](https://scikit-learn.org/stable/glossary.html#term-double-underscore "Link to this term")


double underscore notation[#](https://scikit-learn.org/stable/glossary.html#term-double-underscore-notation "Link to this term")

When specifying parameter names for nested estimators, `__` may be used to separate between parent and child in some contexts. The most common use is when setting parameters through a meta-estimator with [set_params](https://scikit-learn.org/stable/glossary.html#term-set_params) and hence in specifying a search grid in [parameter search](https://scikit-learn.org/stable/modules/grid_search.html#grid-search). See [parameter](https://scikit-learn.org/stable/glossary.html#term-parameter). It is also used in [`pipeline.Pipeline.fit`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline.fit "sklearn.pipeline.Pipeline.fit") for passing [sample properties](https://scikit-learn.org/stable/glossary.html#term-sample-properties) to the `fit` methods of estimators in the pipeline.

dtype[#](https://scikit-learn.org/stable/glossary.html#term-dtype "Link to this term")


data type[#](https://scikit-learn.org/stable/glossary.html#term-data-type "Link to this term")

NumPy arrays assume a homogeneous data type throughout, available in the `.dtype` attribute of an array (or sparse matrix). We generally assume simple data types for scikit-learn data: float or integer. We may support object or string data types for arrays before encoding or vectorizing. Our estimators do not work with struct arrays, for instance.
Our documentation can sometimes give information about the dtype precision, e.g. `np.int32`, `np.int64`, etc. When the precision is provided, it refers to the NumPy dtype. If an arbitrary precision is used, the documentation will refer to dtype `integer` or `floating`. Note that in this case, the precision can be platform dependent. The `numeric` dtype refers to accepting both `integer` and `floating`.
When it comes to choosing between 64-bit dtype (i.e. `np.float64` and `np.int64`) and 32-bit dtype (i.e. `np.float32` and `np.int32`), it boils down to a trade-off between efficiency and precision. The 64-bit types offer more accurate results due to their lower floating-point error, but demand more computational resources, resulting in slower operations and increased memory usage. In contrast, 32-bit types promise enhanced operation speed and reduced memory consumption, but introduce a larger floating-point error. The efficiency improvements are dependent on lower level optimization such as vectorization, single instruction multiple dispatch (SIMD), or cache optimization but crucially on the compatibility of the algorithm in use.
Specifically, the choice of precision should account for whether the employed algorithm can effectively leverage `np.float32`. Some algorithms, especially certain minimization methods, are exclusively coded for `np.float64`, meaning that even if `np.float32` is passed, it triggers an automatic conversion back to `np.float64`. This not only negates the intended computational savings but also introduces additional overhead, making operations with `np.float32` unexpectedly slower and more memory-intensive due to this extra conversion step.

duck typing[#](https://scikit-learn.org/stable/glossary.html#term-duck-typing "Link to this term")

We try to apply `isinstance` where possible, and rely on the presence or absence of attributes to determine an object’s behaviour. Some nuance is required when following this approach:
  * For some estimators, an attribute may only be available once it is [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted). For instance, we cannot a priori determine if [predict_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba) is available in a grid search where the grid includes alternating between a probabilistic and a non-probabilistic predictor in the final step of the pipeline. In the following, we can only determine if `clf` is probabilistic after fitting it on some data:
```
>>> from sklearn.model_selection import GridSearchCV
>>> from sklearn.linear_model import SGDClassifier
>>> clf = GridSearchCV(SGDClassifier(),
...                    param_grid={'loss': ['log_loss', 'hinge']})

```
Copy to clipboard
This means that we can only check for duck-typed attributes after fitting, and that we must be careful to make [meta-estimators](https://scikit-learn.org/stable/glossary.html#term-meta-estimators) only present attributes according to the state of the underlying estimator after fitting.
  * Checking if an attribute is present (using `hasattr`) is in general just as expensive as getting the attribute (`getattr` or dot notation). In some cases, getting the attribute may indeed be expensive (e.g. for some implementations of [feature_importances_](https://scikit-learn.org/stable/glossary.html#term-feature_importances_), which may suggest this is an API design flaw). So code which does `hasattr` followed by `getattr` should be avoided; `getattr` within a try-except block is preferred.
  * For determining some aspects of an estimator’s expectations or support for some feature, we use [estimator tags](https://scikit-learn.org/stable/glossary.html#term-estimator-tags) instead of duck typing.



early stopping[#](https://scikit-learn.org/stable/glossary.html#term-early-stopping "Link to this term")

This consists in stopping an iterative optimization method before the convergence of the training loss, to avoid over-fitting. This is generally done by monitoring the generalization score on a validation set. When available, it is activated through the parameter `early_stopping` or by setting a positive [n_iter_no_change](https://scikit-learn.org/stable/glossary.html#term-n_iter_no_change).

estimator instance[#](https://scikit-learn.org/stable/glossary.html#term-estimator-instance "Link to this term")

We sometimes use this terminology to distinguish an [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator) class from a constructed instance. For example, in the following, `cls` is an estimator class, while `est1` and `est2` are instances:
```
cls = RandomForestClassifier
est1 = cls()
est2 = RandomForestClassifier()

```
Copy to clipboard

examples[#](https://scikit-learn.org/stable/glossary.html#term-examples "Link to this term")

We try to give examples of basic usage for most functions and classes in the API:
  * as doctests in their docstrings (i.e. within the `sklearn/` library code itself).
  * as examples in the [example gallery](https://scikit-learn.org/stable/auto_examples/index.html#general-examples) rendered (using `examples/` directory, exemplifying key features or parameters of the estimator/function. These should also be referenced from the User Guide.
  * sometimes in the [User Guide](https://scikit-learn.org/stable/user_guide.html#user-guide) (built from `doc/`) alongside a technical description of the estimator.



experimental[#](https://scikit-learn.org/stable/glossary.html#term-experimental "Link to this term")

An experimental tool is already usable but its public API, such as default parameter values or fitted attributes, is still subject to change in future versions without the usual [deprecation](https://scikit-learn.org/stable/glossary.html#term-deprecation) warning policy.

evaluation metric[#](https://scikit-learn.org/stable/glossary.html#term-evaluation-metric "Link to this term")


evaluation metrics[#](https://scikit-learn.org/stable/glossary.html#term-evaluation-metrics "Link to this term")

Evaluation metrics give a measure of how well a model performs. We may use this term specifically to refer to the functions in [`metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics") (disregarding [`pairwise`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics.pairwise "sklearn.metrics.pairwise")), as distinct from the [score](https://scikit-learn.org/stable/glossary.html#term-score) method and the [scoring](https://scikit-learn.org/stable/glossary.html#term-scoring) API used in cross validation. See [Metrics and scoring: quantifying the quality of predictions](https://scikit-learn.org/stable/modules/model_evaluation.html#model-evaluation).
These functions usually accept a ground truth (or the raw data where the metric evaluates clustering without a ground truth) and a prediction, be it the output of [predict](https://scikit-learn.org/stable/glossary.html#term-predict) (`y_pred`), of [predict_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba) (`y_proba`), or of an arbitrary score function including [decision_function](https://scikit-learn.org/stable/glossary.html#term-decision_function) (`y_score`). Functions are usually named to end with `_score` if a greater score indicates a better model, and `_loss` if a lesser score indicates a better model. This diversity of interface motivates the scoring API.
Note that some estimators can calculate metrics that are not included in [`metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics") and are estimator-specific, notably model likelihoods.

estimator tags[#](https://scikit-learn.org/stable/glossary.html#term-estimator-tags "Link to this term")

Estimator tags describe certain capabilities of an estimator. This would enable some runtime behaviors based on estimator inspection, but it also allows each estimator to be tested for appropriate invariances while being excepted from other [common tests](https://scikit-learn.org/stable/glossary.html#term-common-tests).
