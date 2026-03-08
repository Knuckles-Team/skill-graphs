# Feature importances with a forest of trees[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#feature-importances-with-a-forest-of-trees "Link to this heading")
This example shows the use of a forest of trees to evaluate the importance of features on an artificial classification task. The blue bars are the feature importances of the forest, along with their inter-trees variability represented by the error bars.
As expected, the plot suggests that 3 features are informative, while the remaining are not.
```
# Authors: The scikit-learn developers
# SPDX-License-Identifier: BSD-3-Clause

import matplotlib.pyplot as plt

```
Copy to clipboard
## Data generation and model fitting[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#data-generation-and-model-fitting "Link to this heading")
We generate a synthetic dataset with only 3 informative features. We will explicitly not shuffle the dataset to ensure that the informative features will correspond to the three first columns of X. In addition, we will split our dataset into training and testing subsets.
```
from sklearn.datasets import [make_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.model_selection import [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y = [make_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")(
    n_samples=1000,
    n_features=10,
    n_informative=3,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    random_state=0,
    shuffle=False,
)
X_train, X_test, y_train, y_test = [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")(X, y, stratify=y, random_state=42)

```
Copy to clipboard
A random forest classifier will be fitted to compute the feature importances.
```
from sklearn.ensemble import [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")

feature_names = [f"feature {i}" for i in range(X.shape[1])]
forest = [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")(random_state=0)
forest.fit(X_train, y_train)

```
Copy to clipboard
```
RandomForestClassifier(random_state=0)
```
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**
RandomForestClassifier
[?Documentation for RandomForestClassifier](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html)iFitted
Parameters |  [ n_estimators n_estimators: int, default=100

The number of trees in the forest.

.. versionchanged:: 0.22
The default value of ``n_estimators`` changed from 10 to 100
in 0.22. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_estimators,-int%2C%20default%3D100) | 100
---|---|---
|  [ criterion criterion: {"gini", "entropy", "log_loss"}, default="gini"

The function to measure the quality of a split. Supported criteria are
"gini" for the Gini impurity and "log_loss" and "entropy" both for the
Shannon information gain, see :ref:`tree_mathematical_formulation`.
Note: This parameter is tree-specific. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=criterion,-%7B%22gini%22%2C%20%22entropy%22%2C%20%22log_loss%22%7D%2C%20default%3D%22gini%22) | 'gini'
|  [ max_depth max_depth: int, default=None

The maximum depth of the tree. If None, then nodes are expanded until
all leaves are pure or until all leaves contain less than
min_samples_split samples. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_depth,-int%2C%20default%3DNone) | None
|  [ min_samples_split min_samples_split: int or float, default=2

The minimum number of samples required to split an internal node:

- If int, then consider `min_samples_split` as the minimum number.
- If float, then `min_samples_split` is a fraction and
`ceil(min_samples_split * n_samples)` are the minimum
number of samples for each split.

.. versionchanged:: 0.18
Added float values for fractions. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_samples_split,-int%20or%20float%2C%20default%3D2) | 2
|  [ min_samples_leaf min_samples_leaf: int or float, default=1

The minimum number of samples required to be at a leaf node.
A split point at any depth will only be considered if it leaves at
least ``min_samples_leaf`` training samples in each of the left and
right branches. This may have the effect of smoothing the model,
especially in regression.

- If int, then consider `min_samples_leaf` as the minimum number.
- If float, then `min_samples_leaf` is a fraction and
`ceil(min_samples_leaf * n_samples)` are the minimum
number of samples for each node.

.. versionchanged:: 0.18
Added float values for fractions. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_samples_leaf,-int%20or%20float%2C%20default%3D1) | 1
|  [ min_weight_fraction_leaf min_weight_fraction_leaf: float, default=0.0

The minimum weighted fraction of the sum total of weights (of all
the input samples) required to be at a leaf node. Samples have
equal weight when sample_weight is not provided. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_weight_fraction_leaf,-float%2C%20default%3D0.0) | 0.0
|  [ max_features max_features: {"sqrt", "log2", None}, int or float, default="sqrt"

The number of features to consider when looking for the best split:

- If int, then consider `max_features` features at each split.
- If float, then `max_features` is a fraction and
`max(1, int(max_features * n_features_in_))` features are considered at each
split.
- If "sqrt", then `max_features=sqrt(n_features)`.
- If "log2", then `max_features=log2(n_features)`.
- If None, then `max_features=n_features`.

.. versionchanged:: 1.1
The default of `max_features` changed from `"auto"` to `"sqrt"`.

Note: the search for a split does not stop until at least one
valid partition of the node samples is found, even if it requires to
effectively inspect more than ``max_features`` features. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_features,-%7B%22sqrt%22%2C%20%22log2%22%2C%20None%7D%2C%20int%20or%20float%2C%20default%3D%22sqrt%22) | 'sqrt'
|  [ max_leaf_nodes max_leaf_nodes: int, default=None

Grow trees with ``max_leaf_nodes`` in best-first fashion.
Best nodes are defined as relative reduction in impurity.
If None then unlimited number of leaf nodes. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_leaf_nodes,-int%2C%20default%3DNone) | None
|  [ min_impurity_decrease min_impurity_decrease: float, default=0.0

A node will be split if this split induces a decrease of the impurity
greater than or equal to this value.

The weighted impurity decrease equation is the following::

N_t / N * (impurity - N_t_R / N_t * right_impurity
- N_t_L / N_t * left_impurity)

where ``N`` is the total number of samples, ``N_t`` is the number of
samples at the current node, ``N_t_L`` is the number of samples in the
left child, and ``N_t_R`` is the number of samples in the right child.

``N``, ``N_t``, ``N_t_R`` and ``N_t_L`` all refer to the weighted sum,
if ``sample_weight`` is passed.

.. versionadded:: 0.19 ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=min_impurity_decrease,-float%2C%20default%3D0.0) | 0.0
|  [ bootstrap bootstrap: bool, default=True

Whether bootstrap samples are used when building trees. If False, the
whole dataset is used to build each tree. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=bootstrap,-bool%2C%20default%3DTrue) | True
|  [ oob_score oob_score: bool or callable, default=False

Whether to use out-of-bag samples to estimate the generalization score.
By default, :func:`~sklearn.metrics.accuracy_score` is used.
Provide a callable with signature `metric(y_true, y_pred)` to use a
custom metric. Only available if `bootstrap=True`.

For an illustration of out-of-bag (OOB) error estimation, see the example
:ref:`sphx_glr_auto_examples_ensemble_plot_ensemble_oob.py`. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=oob_score,-bool%20or%20callable%2C%20default%3DFalse) | False
|  [ n_jobs n_jobs: int, default=None

The number of jobs to run in parallel. :meth:`fit`, :meth:`predict`,
:meth:`decision_path` and :meth:`apply` are all parallelized over the
trees. ``None`` means 1 unless in a :obj:`joblib.parallel_backend`
context. ``-1`` means using all processors. See :term:`Glossary
` for more details. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None
|  [ random_state random_state: int, RandomState instance or None, default=None

Controls both the randomness of the bootstrapping of the samples used
when building trees (if ``bootstrap=True``) and the sampling of the
features to consider when looking for the best split at each node
(if ``max_features < n_features``).
See :term:`Glossary ` for details. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=random_state,-int%2C%20RandomState%20instance%20or%20None%2C%20default%3DNone) | 0
|  [ verbose verbose: int, default=0

Controls the verbosity when fitting and predicting. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=verbose,-int%2C%20default%3D0) | 0
|  [ warm_start warm_start: bool, default=False

When set to ``True``, reuse the solution of the previous call to fit
and add more estimators to the ensemble, otherwise, just fit a whole
new forest. See :term:`Glossary ` and
:ref:`tree_ensemble_warm_start` for details. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False
|  [ class_weight class_weight: {"balanced", "balanced_subsample"}, dict or list of dicts, default=None

Weights associated with classes in the form ``{class_label: weight}``.
If not given, all classes are supposed to have weight one. For
multi-output problems, a list of dicts can be provided in the same
order as the columns of y.

Note that for multioutput (including multilabel) weights should be
defined for each class of every column in its own dict. For example,
for four-class multilabel classification weights should be
[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}] instead of
[{1:1}, {2:5}, {3:1}, {4:1}].

The "balanced" mode uses the values of y to automatically adjust
weights inversely proportional to class frequencies in the input data
as ``n_samples / (n_classes * np.bincount(y))``

The "balanced_subsample" mode is the same as "balanced" except that
weights are computed based on the bootstrap sample for every tree
grown.

For multi-output, the weights of each column of y will be multiplied.

Note that these weights will be multiplied with sample_weight (passed
through the fit method) if sample_weight is specified. ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=class_weight,-%7B%22balanced%22%2C%20%22balanced_subsample%22%7D%2C%20dict%20or%20list%20of%20dicts%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3DNone) | None
|  [ ccp_alpha ccp_alpha: non-negative float, default=0.0

Complexity parameter used for Minimal Cost-Complexity Pruning. The
subtree with the largest cost complexity that is smaller than
``ccp_alpha`` will be chosen. By default, no pruning is performed. See
:ref:`minimal_cost_complexity_pruning` for details. See
:ref:`sphx_glr_auto_examples_tree_plot_cost_complexity_pruning.py`
for an example of such pruning.

.. versionadded:: 0.22 ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=ccp_alpha,-non-negative%20float%2C%20default%3D0.0) | 0.0
|  [ max_samples max_samples: int or float, default=None

If bootstrap is True, the number of samples to draw from X
to train each base estimator.

- If None (default), then draw `X.shape[0]` samples.
- If int, then draw `max_samples` samples.
- If float, then draw `max(round(n_samples * max_samples), 1)` samples. Thus,
`max_samples` should be in the interval `(0.0, 1.0]`.

.. versionadded:: 0.22 ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=max_samples,-int%20or%20float%2C%20default%3DNone) | None
|  [ monotonic_cst monotonic_cst: array-like of int of shape (n_features), default=None

Indicates the monotonicity constraint to enforce on each feature.
- 1: monotonic increase
- 0: no constraint
- -1: monotonic decrease

If monotonic_cst is None, no constraints are applied.

Monotonicity constraints are not supported for:
- multiclass classifications (i.e. when `n_classes > 2`),
- multioutput classifications (i.e. when `n_outputs_ > 1`),
- classifications trained on data with missing values.

The constraints hold over the probability of the positive class.

Read more in the :ref:`User Guide `.

.. versionadded:: 1.4 ](https://scikit-learn.org/1.8/modules/generated/sklearn.ensemble.RandomForestClassifier.html#:~:text=monotonic_cst,-array-like%20of%20int%20of%20shape%20%28n_features%29%2C%20default%3DNone) | None



## Feature importance based on mean decrease in impurity[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#feature-importance-based-on-mean-decrease-in-impurity "Link to this heading")
Feature importances are provided by the fitted attribute `feature_importances_` and they are computed as the mean and standard deviation of accumulation of the impurity decrease within each tree.
Warning
Impurity-based feature importances can be misleading for **high cardinality** features (many unique values). See [Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html#permutation-importance) as an alternative below.
```
import time

import numpy as np

start_time = ()
importances = forest.feature_importances_
std = ([tree.feature_importances_ for tree in forest.estimators_], axis=0)
elapsed_time = () - start_time

print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

```
Copy to clipboard
```
Elapsed time to compute the importances: 0.018 seconds

```
Copy to clipboard
Let’s plot the impurity-based importance.
```
import pandas as pd

forest_importances = (importances, index=feature_names)

fig, ax = ()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurity")
fig.tight_layout()

```
Copy to clipboard
![Feature importances using MDI](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_importances_001.png)
We observe that, as expected, the three first features are found important.
## Feature importance based on feature permutation[#](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#feature-importance-based-on-feature-permutation "Link to this heading")
Permutation feature importance overcomes limitations of the impurity-based feature importance: they do not have a bias toward high-cardinality features and can be computed on a left-out test set.
```
from sklearn.inspection import [permutation_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")

start_time = ()
result = [permutation_importance](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html#sklearn.inspection.permutation_importance "sklearn.inspection.permutation_importance")(
    forest, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)
elapsed_time = () - start_time
print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

forest_importances = (result.importances_mean, index=feature_names)

```
Copy to clipboard
```
Elapsed time to compute the importances: 1.203 seconds

```
Copy to clipboard
The computation for full permutation importance is more costly. Each feature is shuffled n times and the model is used to make predictions on the permuted data to see the drop in performance. Please see [Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html#permutation-importance) for more details. We can now plot the importance ranking.
```
fig, ax = ()
forest_importances.plot.bar(yerr=result.importances_std, ax=ax)
ax.set_title("Feature importances using permutation on full model")
ax.set_ylabel("Mean accuracy decrease")
fig.tight_layout()
()

```
Copy to clipboard
![Feature importances using permutation on full model](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_importances_002.png)
The same features are detected as most important using both methods. Although the relative importances vary. As seen on the plots, MDI is less likely than permutation importance to fully omit a feature.
**Total running time of the script:** (0 minutes 1.722 seconds)
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo11.svg) ](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_forest_importances.ipynb)
[`Download Jupyter notebook: plot_forest_importances.ipynb`](https://scikit-learn.org/stable/_downloads/5e3b69cd18b43dd31a46a35ccba413e7/plot_forest_importances.ipynb)
[`Download Python source code: plot_forest_importances.py`](https://scikit-learn.org/stable/_downloads/74c6ab6570af7f9379b15af6a1323943/plot_forest_importances.py)
[`Download zipped: plot_forest_importances.zip`](https://scikit-learn.org/stable/_downloads/175dc7cd79fedbe3d38829513430275a/plot_forest_importances.zip)
Related examples
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_thumb.png)
[Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html)
Permutation Importance vs Random Forest Feature Importance (MDI)
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_permutation_importance_multicollinear_thumb.png)
[Permutation Importance with Multicollinear or Correlated Features](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance_multicollinear.html)
Permutation Importance with Multicollinear or Correlated Features
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_gradient_boosting_regression_thumb.png)
[Gradient Boosting regression](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html)
Gradient Boosting regression
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_0_22_0_thumb.png)
[Release Highlights for scikit-learn 0.22](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_0_22_0.html)
Release Highlights for scikit-learn 0.22
[ previous Early stopping in Gradient Boosting ](https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_early_stopping.html "previous page") [ next Feature transformations with ensembles of trees ](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html "next page")
On this page
  * [Data generation and model fitting](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#data-generation-and-model-fitting)
  * [Feature importance based on mean decrease in impurity](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#feature-importance-based-on-mean-decrease-in-impurity)
  * [Feature importance based on feature permutation](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#feature-importance-based-on-feature-permutation)


### This Page
  * [Show Source](https://scikit-learn.org/stable/_sources/auto_examples/ensemble/plot_forest_importances.rst.txt)


[ Download source code ](https://scikit-learn.org/stable/_downloads/74c6ab6570af7f9379b15af6a1323943/plot_forest_importances.py)
[ Download Jupyter notebook ](https://scikit-learn.org/stable/_downloads/5e3b69cd18b43dd31a46a35ccba413e7/plot_forest_importances.ipynb)
[ Download zipped ](https://scikit-learn.org/stable/_downloads/175dc7cd79fedbe3d38829513430275a/plot_forest_importances.zip)
[ ![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo11.svg) ](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/ensemble/plot_forest_importances.ipynb)
© Copyright 2007 - 2025, scikit-learn developers (BSD License).
