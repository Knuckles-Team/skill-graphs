##  3.1.2. Cross validation iterators[#](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators "Link to this heading")
The following sections list utilities to generate indices that can be used to generate dataset splits according to different cross validation strategies.
###  3.1.2.1. Cross-validation iterators for i.i.d. data[#](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-i-i-d-data "Link to this heading")
Assuming that some data is Independent and Identically Distributed (i.i.d.) is making the assumption that all samples stem from the same generative process and that the generative process is assumed to have no memory of past generated samples.
The following cross-validators can be used in such cases.
Note
While i.i.d. data is a common assumption in machine learning theory, it rarely holds in practice. If one knows that the samples have been generated using a time-dependent process, it is safer to use a [time-series aware cross-validation scheme](https://scikit-learn.org/stable/modules/cross_validation.html#timeseries-cv). Similarly, if we know that the generative process has a group structure (samples collected from different subjects, experiments, measurement devices), it is safer to use [group-wise cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html#group-cv).
####  3.1.2.1.1. K-fold[#](https://scikit-learn.org/stable/modules/cross_validation.html#k-fold "Link to this heading")
[`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold") divides all the samples in k groups of samples, called folds (if k=n, this is equivalent to the _Leave One Out_ strategy), of equal sizes (if possible). The prediction function is learned using k−1 folds, and the fold left out is used for test.
Example of 2-fold cross-validation on a dataset with 4 samples:
```
>>> import numpy as np
>>> from sklearn.model_selection import KFold

>>> X = ["a", "b", "c", "d"]
>>> kf = KFold(n_splits=2)
>>> for train, test in kf.split(X):
...     print("%s %s" % (train, test))
[2 3] [0 1]
[0 1] [2 3]

```
Copy to clipboard
Here is a visualization of the cross-validation behavior. Note that [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold") is not affected by classes or groups.
[![../_images/sphx_glr_plot_cv_indices_006.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_006.png) ](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)
Each fold is constituted by two arrays: the first one is related to the _training set_ , and the second one to the _test set_. Thus, one can create the training/test sets using numpy indexing:
```
>>> X = np.array([[0., 0.], [1., 1.], [-1., -1.], [2., 2.]])
>>> y = np.array([0, 1, 0, 1])
>>> X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]

```
Copy to clipboard
####  3.1.2.1.2. Repeated K-Fold[#](https://scikit-learn.org/stable/modules/cross_validation.html#repeated-k-fold "Link to this heading")
[`RepeatedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#sklearn.model_selection.RepeatedKFold "sklearn.model_selection.RepeatedKFold") repeats [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold") n times, producing different splits in each repetition.
Example of 2-fold K-Fold repeated 2 times:
```
>>> import numpy as np
>>> from sklearn.model_selection import RepeatedKFold
>>> X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
>>> random_state = 12883823
>>> rkf = RepeatedKFold(n_splits=2, n_repeats=2, random_state=random_state)
>>> for train, test in rkf.split(X):
...     print("%s %s" % (train, test))
...
[2 3] [0 1]
[0 1] [2 3]
[0 2] [1 3]
[1 3] [0 2]

```
Copy to clipboard
Similarly, [`RepeatedStratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold") repeats [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold") n times with different randomization in each repetition.
####  3.1.2.1.3. Leave One Out (LOO)[#](https://scikit-learn.org/stable/modules/cross_validation.html#leave-one-out-loo "Link to this heading")
[`LeaveOneOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut "sklearn.model_selection.LeaveOneOut") (or LOO) is a simple cross-validation. Each learning set is created by taking all the samples except one, the test set being the sample left out. Thus, for n samples, we have n different training sets and n different test sets. This cross-validation procedure does not waste much data as only one sample is removed from the training set:
```
>>> from sklearn.model_selection import LeaveOneOut

>>> X = [1, 2, 3, 4]
>>> loo = LeaveOneOut()
>>> for train, test in loo.split(X):
...     print("%s %s" % (train, test))
[1 2 3] [0]
[0 2 3] [1]
[0 1 3] [2]
[0 1 2] [3]

```
Copy to clipboard
Potential users of LOO for model selection should weigh a few known caveats. When compared with k-fold cross validation, one builds n models from n samples instead of k models, where n>k. Moreover, each is trained on n−1 samples rather than (k−1)n/k. In both ways, assuming k is not too large and k<n, LOO is more computationally expensive than k-fold cross validation.
In terms of accuracy, LOO often results in high variance as an estimator for the test error. Intuitively, since n−1 of the n samples are used to build each model, models constructed from folds are virtually identical to each other and to the model built from the entire training set.
However, if the learning curve is steep for the training size in question, then 5 or 10-fold cross validation can overestimate the generalization error.
As a general rule, most authors and empirical evidence suggest that 5 or 10-fold cross validation should be preferred to LOO.
References[#](https://scikit-learn.org/stable/modules/cross_validation.html#references "Link to this dropdown")
  * T. Hastie, R. Tibshirani, J. Friedman,
  * L. Breiman, P. Spector
  * R. Kohavi,
  * R. Bharat Rao, G. Fung, R. Rosales,
  * G. James, D. Witten, T. Hastie, R. Tibshirani,


####  3.1.2.1.4. Leave P Out (LPO)[#](https://scikit-learn.org/stable/modules/cross_validation.html#leave-p-out-lpo "Link to this heading")
[`LeavePOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePOut.html#sklearn.model_selection.LeavePOut "sklearn.model_selection.LeavePOut") is very similar to [`LeaveOneOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut "sklearn.model_selection.LeaveOneOut") as it creates all the possible training/test sets by removing p samples from the complete set. For n samples, this produces (np) train-test pairs. Unlike [`LeaveOneOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneOut.html#sklearn.model_selection.LeaveOneOut "sklearn.model_selection.LeaveOneOut") and [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold"), the test sets will overlap for p>1.
Example of Leave-2-Out on a dataset with 4 samples:
```
>>> from sklearn.model_selection import LeavePOut

>>> X = np.ones(4)
>>> lpo = LeavePOut(p=2)
>>> for train, test in lpo.split(X):
...     print("%s %s" % (train, test))
[2 3] [0 1]
[1 3] [0 2]
[1 2] [0 3]
[0 3] [1 2]
[0 2] [1 3]
[0 1] [2 3]

```
Copy to clipboard
####  3.1.2.1.5. Random permutations cross-validation a.k.a. Shuffle & Split[#](https://scikit-learn.org/stable/modules/cross_validation.html#random-permutations-cross-validation-a-k-a-shuffle-split "Link to this heading")
The [`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit") iterator will generate a user defined number of independent train / test dataset splits. Samples are first shuffled and then split into a pair of train and test sets.
It is possible to control the randomness for reproducibility of the results by explicitly seeding the `random_state` pseudo random number generator.
Here is a usage example:
```
>>> from sklearn.model_selection import ShuffleSplit
>>> X = np.arange(10)
>>> ss = ShuffleSplit(n_splits=5, test_size=0.25, random_state=0)
>>> for train_index, test_index in ss.split(X):
...     print("%s %s" % (train_index, test_index))
[9 1 6 7 3 0 5] [2 8 4]
[2 9 8 0 6 7 4] [3 5 1]
[4 5 1 0 6 9 7] [2 3 8]
[2 7 5 8 0 3 4] [6 1 9]
[4 1 0 6 8 9 3] [5 2 7]

```
Copy to clipboard
Here is a visualization of the cross-validation behavior. Note that [`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit") is not affected by classes or groups.
[![../_images/sphx_glr_plot_cv_indices_008.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_008.png) ](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)
[`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit") is thus a good alternative to [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold") cross validation that allows a finer control on the number of iterations and the proportion of samples on each side of the train / test split.
###  3.1.2.2. Cross-validation iterators with stratification based on class labels[#](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-with-stratification-based-on-class-labels "Link to this heading")
Some classification tasks can naturally exhibit rare classes: for instance, there could be orders of magnitude more negative observations than positive observations (e.g. medical screening, fraud detection, etc). As a result, cross-validation splitting can generate train or validation folds without any occurrence of a particular class. This typically leads to undefined classification metrics (e.g. ROC AUC), exceptions raised when attempting to call [fit](https://scikit-learn.org/stable/glossary.html#term-fit) or missing columns in the output of the `predict_proba` or `decision_function` methods of multiclass classifiers trained on different folds.
To mitigate such problems, splitters such as [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold") and [`StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit") implement stratified sampling to ensure that relative class frequencies are approximately preserved in each fold.
Note
Stratified sampling was introduced in scikit-learn to workaround the aforementioned engineering problems rather than solve a statistical one.
Stratification makes cross-validation folds more homogeneous, and as a result hides some of the variability inherent to fitting models with a limited number of observations.
As a result, stratification can artificially shrink the spread of the metric measured across cross-validation iterations: the inter-fold variability does no longer reflect the uncertainty in the performance of classifiers in the presence of rare classes.
####  3.1.2.2.1. Stratified K-fold[#](https://scikit-learn.org/stable/modules/cross_validation.html#stratified-k-fold "Link to this heading")
[`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold") is a variation of _K-fold_ which returns _stratified_ folds: each set contains approximately the same percentage of samples of each target class as the complete set.
Here is an example of stratified 3-fold cross-validation on a dataset with 50 samples from two unbalanced classes. We show the number of samples in each class and compare with [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold").
```
>>> from sklearn.model_selection import StratifiedKFold, KFold
>>> import numpy as np
>>> X, y = np.ones((50, 1)), np.hstack(([0] * 45, [1] * 5))
>>> skf = StratifiedKFold(n_splits=3)
>>> for train, test in skf.split(X, y):
...     print('train -  {}   |   test -  {}'.format(
...         np.bincount(y[train]), np.bincount(y[test])))
train -  [30  3]   |   test -  [15  2]
train -  [30  3]   |   test -  [15  2]
train -  [30  4]   |   test -  [15  1]
>>> kf = KFold(n_splits=3)
>>> for train, test in kf.split(X, y):
...     print('train -  {}   |   test -  {}'.format(
...         np.bincount(y[train]), np.bincount(y[test])))
train -  [28  5]   |   test -  [17]
train -  [28  5]   |   test -  [17]
train -  [34]   |   test -  [11  5]

```
Copy to clipboard
We can see that [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold") preserves the class ratios (approximately 1 / 10) in both train and test datasets.
Here is a visualization of the cross-validation behavior.
[![../_images/sphx_glr_plot_cv_indices_009.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_009.png) ](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)
[`RepeatedStratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html#sklearn.model_selection.RepeatedStratifiedKFold "sklearn.model_selection.RepeatedStratifiedKFold") can be used to repeat Stratified K-Fold n times with different randomization in each repetition.
####  3.1.2.2.2. Stratified Shuffle Split[#](https://scikit-learn.org/stable/modules/cross_validation.html#stratified-shuffle-split "Link to this heading")
[`StratifiedShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html#sklearn.model_selection.StratifiedShuffleSplit "sklearn.model_selection.StratifiedShuffleSplit") is a variation of _ShuffleSplit_ , which returns stratified splits, _i.e._ which creates splits by preserving the same percentage for each target class as in the complete set.
Here is a visualization of the cross-validation behavior.
[![../_images/sphx_glr_plot_cv_indices_012.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_012.png) ](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)
###  3.1.2.3. Predefined fold-splits / Validation-sets[#](https://scikit-learn.org/stable/modules/cross_validation.html#predefined-fold-splits-validation-sets "Link to this heading")
For some datasets, a pre-defined split of the data into training- and validation fold or into several cross-validation folds already exists. Using [`PredefinedSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.PredefinedSplit.html#sklearn.model_selection.PredefinedSplit "sklearn.model_selection.PredefinedSplit") it is possible to use these folds e.g. when searching for hyperparameters.
For example, when using a validation set, set the `test_fold` to 0 for all samples that are part of the validation set, and to -1 for all other samples.
###  3.1.2.4. Cross-validation iterators for grouped data[#](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-iterators-for-grouped-data "Link to this heading")
The i.i.d. assumption is broken if the underlying generative process yields groups of dependent samples.
Such a grouping of data is domain specific. An example would be when there is medical data collected from multiple patients, with multiple samples taken from each patient. And such data is likely to be dependent on the individual group. In our example, the patient id for each sample will be its group identifier.
In this case we would like to know if a model trained on a particular set of groups generalizes well to the unseen groups. To measure this, we need to ensure that all the samples in the validation fold come from groups that are not represented at all in the paired training fold.
The following cross-validation splitters can be used to do that. The grouping identifier for the samples is specified via the `groups` parameter.
####  3.1.2.4.1. Group K-fold[#](https://scikit-learn.org/stable/modules/cross_validation.html#group-k-fold "Link to this heading")
[`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold") is a variation of K-fold which ensures that the same group is not represented in both testing and training sets. For example if the data is obtained from different subjects with several samples per-subject and if the model is flexible enough to learn from highly person specific features it could fail to generalize to new subjects. [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold") makes it possible to detect this kind of overfitting situations.
Imagine you have three subjects, each with an associated number from 1 to 3:
```
>>> from sklearn.model_selection import GroupKFold

>>> X = [0.1, 0.2, 2.2, 2.4, 2.3, 4.55, 5.8, 8.8, 9, 10]
>>> y = ["a", "b", "b", "b", "c", "c", "c", "d", "d", "d"]
>>> groups = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]

>>> gkf = GroupKFold(n_splits=3)
>>> for train, test in gkf.split(X, y, groups=groups):
...     print("%s %s" % (train, test))
[0 1 2 3 4 5] [6 7 8 9]
[0 1 2 6 7 8 9] [3 4 5]
[3 4 5 6 7 8 9] [0 1 2]

```
Copy to clipboard
Each subject is in a different testing fold, and the same subject is never in both testing and training. Notice that the folds do not have exactly the same size due to the imbalance in the data. If class proportions must be balanced across folds, [`StratifiedGroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold "sklearn.model_selection.StratifiedGroupKFold") is a better option.
Here is a visualization of the cross-validation behavior.
[![../_images/sphx_glr_plot_cv_indices_007.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_007.png) ](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)
Similar to [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold"), the test sets from [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold") will form a complete partition of all the data.
While [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold") attempts to place the same number of samples in each fold when `shuffle=False`, when `shuffle=True` it attempts to place an equal number of distinct groups in each fold (but does not account for group sizes).
####  3.1.2.4.2. StratifiedGroupKFold[#](https://scikit-learn.org/stable/modules/cross_validation.html#stratifiedgroupkfold "Link to this heading")
[`StratifiedGroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedGroupKFold.html#sklearn.model_selection.StratifiedGroupKFold "sklearn.model_selection.StratifiedGroupKFold") is a cross-validation scheme that combines both [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold "sklearn.model_selection.StratifiedKFold") and [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold"). The idea is to try to preserve the distribution of classes in each split while keeping each group within a single split. That might be useful when you have an unbalanced dataset so that using just [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold") might produce skewed splits.
Example:
```
>>> from sklearn.model_selection import StratifiedGroupKFold
>>> X = list(range(18))
>>> y = [1] * 6 + [0] * 12
>>> groups = [1, 2, 3, 3, 4, 4, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 6]
>>> sgkf = StratifiedGroupKFold(n_splits=3)
>>> for train, test in sgkf.split(X, y, groups=groups):
...     print("%s %s" % (train, test))
[ 0  2  3  4  5  6  7 10 11 15 16 17] [ 1  8  9 12 13 14]
[ 0  1  4  5  6  7  8  9 11 12 13 14] [ 2  3 10 15 16 17]
[ 1  2  3  8  9 10 12 13 14 15 16 17] [ 0  4  5  6  7 11]

```
Copy to clipboard
Implementation notes[#](https://scikit-learn.org/stable/modules/cross_validation.html#implementation-notes "Link to this dropdown")
  * With the current implementation full shuffle is not possible in most scenarios. When shuffle=True, the following happens:
    1. All groups are shuffled.
    2. Groups are sorted by standard deviation of classes using stable sort.
    3. Sorted groups are iterated over and assigned to folds.
That means that only groups with the same standard deviation of class distribution will be shuffled, which might be useful when each group has only a single class.
  * The algorithm greedily assigns each group to one of n_splits test sets, choosing the test set that minimises the variance in class distribution across test sets. Group assignment proceeds from groups with highest to lowest variance in class frequency, i.e. large groups peaked on one or few classes are assigned first.
  * This split is suboptimal in a sense that it might produce imbalanced splits even if perfect stratification is possible. If you have relatively close distribution of classes in each group, using [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold") is better.


Here is a visualization of cross-validation behavior for uneven groups:
[![../_images/sphx_glr_plot_cv_indices_005.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_005.png) ](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)
####  3.1.2.4.3. Leave One Group Out[#](https://scikit-learn.org/stable/modules/cross_validation.html#leave-one-group-out "Link to this heading")
[`LeaveOneGroupOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut "sklearn.model_selection.LeaveOneGroupOut") is a cross-validation scheme where each split holds out samples belonging to one specific group. Group information is provided via an array that encodes the group of each sample.
Each training set is thus constituted by all the samples except the ones related to a specific group. This is the same as [`LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut") with `n_groups=1` and the same as [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html#sklearn.model_selection.GroupKFold "sklearn.model_selection.GroupKFold") with `n_splits` equal to the number of unique labels passed to the `groups` parameter.
For example, in the cases of multiple experiments, [`LeaveOneGroupOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut "sklearn.model_selection.LeaveOneGroupOut") can be used to create a cross-validation based on the different experiments: we create a training set using the samples of all the experiments except one:
```
>>> from sklearn.model_selection import LeaveOneGroupOut

>>> X = [1, 5, 10, 50, 60, 70, 80]
>>> y = [0, 1, 1, 2, 2, 2, 2]
>>> groups = [1, 1, 2, 2, 3, 3, 3]
>>> logo = LeaveOneGroupOut()
>>> for train, test in logo.split(X, y, groups=groups):
...     print("%s %s" % (train, test))
[2 3 4 5 6] [0 1]
[0 1 4 5 6] [2 3]
[0 1 2 3] [4 5 6]

```
Copy to clipboard
Another common application is to use time information: for instance the groups could be the year of collection of the samples and thus allow for cross-validation against time-based splits.
####  3.1.2.4.4. Leave P Groups Out[#](https://scikit-learn.org/stable/modules/cross_validation.html#leave-p-groups-out "Link to this heading")
[`LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut") is similar to [`LeaveOneGroupOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeaveOneGroupOut.html#sklearn.model_selection.LeaveOneGroupOut "sklearn.model_selection.LeaveOneGroupOut"), but removes samples related to P groups for each training/test set. All possible combinations of P groups are left out, meaning test sets will overlap for P>1.
Example of Leave-2-Group Out:
```
>>> from sklearn.model_selection import LeavePGroupsOut

>>> X = np.arange(6)
>>> y = [1, 1, 1, 2, 2, 2]
>>> groups = [1, 1, 2, 2, 3, 3]
>>> lpgo = LeavePGroupsOut(n_groups=2)
>>> for train, test in lpgo.split(X, y, groups=groups):
...     print("%s %s" % (train, test))
[4 5] [0 1 2 3]
[2 3] [0 1 4 5]
[0 1] [2 3 4 5]

```
Copy to clipboard
####  3.1.2.4.5. Group Shuffle Split[#](https://scikit-learn.org/stable/modules/cross_validation.html#group-shuffle-split "Link to this heading")
The [`GroupShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit "sklearn.model_selection.GroupShuffleSplit") iterator behaves as a combination of [`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit") and [`LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut"), and generates a sequence of randomized partitions in which a subset of groups are held out for each split. Each train/test split is performed independently meaning there is no guaranteed relationship between successive test sets.
Here is a usage example:
```
>>> from sklearn.model_selection import GroupShuffleSplit

>>> X = [0.1, 0.2, 2.2, 2.4, 2.3, 4.55, 5.8, 0.001]
>>> y = ["a", "b", "b", "b", "c", "c", "c", "a"]
>>> groups = [1, 1, 2, 2, 3, 3, 4, 4]
>>> gss = GroupShuffleSplit(n_splits=4, test_size=0.5, random_state=0)
>>> for train, test in gss.split(X, y, groups=groups):
...     print("%s %s" % (train, test))
...
[0 1 2 3] [4 5 6 7]
[2 3 6 7] [0 1 4 5]
[2 3 4 5] [0 1 6 7]
[4 5 6 7] [0 1 2 3]

```
Copy to clipboard
Here is a visualization of the cross-validation behavior.
[![../_images/sphx_glr_plot_cv_indices_011.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_011.png) ](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)
This class is useful when the behavior of [`LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut") is desired, but the number of groups is large enough that generating all possible partitions with P groups withheld would be prohibitively expensive. In such a scenario, [`GroupShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupShuffleSplit.html#sklearn.model_selection.GroupShuffleSplit "sklearn.model_selection.GroupShuffleSplit") provides a random sample (with replacement) of the train / test splits generated by [`LeavePGroupsOut`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.LeavePGroupsOut.html#sklearn.model_selection.LeavePGroupsOut "sklearn.model_selection.LeavePGroupsOut").
###  3.1.2.5. Using cross-validation iterators to split train and test[#](https://scikit-learn.org/stable/modules/cross_validation.html#using-cross-validation-iterators-to-split-train-and-test "Link to this heading")
The above group cross-validation functions may also be useful for splitting a dataset into training and testing subsets. Note that the convenience function [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split") is a wrapper around [`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit") and thus only allows for stratified splitting (using the class labels) and cannot account for groups.
To perform the train and test split, use the indices for the train and test subsets yielded by the generator output by the `split()` method of the cross-validation splitter. For example:
```
>>> import numpy as np
>>> from sklearn.model_selection import GroupShuffleSplit

>>> X = np.array([0.1, 0.2, 2.2, 2.4, 2.3, 4.55, 5.8, 0.001])
>>> y = np.array(["a", "b", "b", "b", "c", "c", "c", "a"])
>>> groups = np.array([1, 1, 2, 2, 3, 3, 4, 4])
>>> train_indx, test_indx = next(
...     GroupShuffleSplit(random_state=7).split(X, y, groups)
... )
>>> X_train, X_test, y_train, y_test = \
...     X[train_indx], X[test_indx], y[train_indx], y[test_indx]
>>> X_train.shape, X_test.shape
((6,), (2,))
>>> np.unique(groups[train_indx]), np.unique(groups[test_indx])
(array([1, 2, 4]), array([3]))

```
Copy to clipboard
###  3.1.2.6. Cross validation of time series data[#](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation-of-time-series-data "Link to this heading")
Time series data is characterized by the correlation between observations that are near in time (_autocorrelation_). However, classical cross-validation techniques such as [`KFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold "sklearn.model_selection.KFold") and [`ShuffleSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html#sklearn.model_selection.ShuffleSplit "sklearn.model_selection.ShuffleSplit") assume the samples are independent and identically distributed, and would result in unreasonable correlation between training and testing instances (yielding poor estimates of generalization error) on time series data. Therefore, it is very important to evaluate our model for time series data on the “future” observations least like those that are used to train the model. To achieve this, one solution is provided by [`TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit").
####  3.1.2.6.1. Time Series Split[#](https://scikit-learn.org/stable/modules/cross_validation.html#time-series-split "Link to this heading")
[`TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html#sklearn.model_selection.TimeSeriesSplit "sklearn.model_selection.TimeSeriesSplit") is a variation of _k-fold_ which returns first k folds as train set and the (k+1) th fold as test set. Note that unlike standard cross-validation methods, successive training sets are supersets of those that come before them. Also, it adds all surplus data to the first training partition, which is always used to train the model.
This class can be used to cross-validate time series data samples that are observed at fixed time intervals. Indeed, the folds must represent the same duration, in order to have comparable metrics across folds.
Example of 3-split time series cross-validation on a dataset with 6 samples:
```
>>> from sklearn.model_selection import TimeSeriesSplit

>>> X = np.array([[1, 2], [3, 4], [1, 2], [3, 4], [1, 2], [3, 4]])
>>> y = np.array([1, 2, 3, 4, 5, 6])
>>> tscv = TimeSeriesSplit(n_splits=3)
>>> print(tscv)
TimeSeriesSplit(gap=0, max_train_size=None, n_splits=3, test_size=None)
>>> for train, test in tscv.split(X):
...     print("%s %s" % (train, test))
[0 1 2] [3]
[0 1 2 3] [4]
[0 1 2 3 4] [5]

```
Copy to clipboard
Here is a visualization of the cross-validation behavior.
[![../_images/sphx_glr_plot_cv_indices_013.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_013.png) ](https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html)
