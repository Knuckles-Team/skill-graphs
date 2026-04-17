##  1.11.2. Random forests and other randomized tree ensembles[#](https://scikit-learn.org/stable/modules/ensemble.html#random-forests-and-other-randomized-tree-ensembles "Link to this heading")
The [`sklearn.ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble") module includes two averaging algorithms based on randomized [decision trees](https://scikit-learn.org/stable/modules/tree.html#tree): the RandomForest algorithm and the Extra-Trees method. Both algorithms are perturb-and-combine techniques [[B1998]](https://scikit-learn.org/stable/modules/ensemble.html#b1998) specifically designed for trees. This means a diverse set of classifiers is created by introducing randomness in the classifier construction. The prediction of the ensemble is given as the averaged prediction of the individual classifiers.
As other classifiers, forest classifiers have to be fitted with two arrays: a sparse or dense array X of shape `(n_samples, n_features)` holding the training samples, and an array Y of shape `(n_samples,)` holding the target values (class labels) for the training samples:
```
>>> from sklearn.ensemble import RandomForestClassifier
>>> X = [[0, 0], [1, 1]]
>>> Y = [0, 1]
>>> clf = RandomForestClassifier(n_estimators=10)
>>> clf = clf.fit(X, Y)

```
Copy to clipboard
Like [decision trees](https://scikit-learn.org/stable/modules/tree.html#tree), forests of trees also extend to [multi-output problems](https://scikit-learn.org/stable/modules/tree.html#tree-multioutput) (if Y is an array of shape `(n_samples, n_outputs)`).
###  1.11.2.1. Random Forests[#](https://scikit-learn.org/stable/modules/ensemble.html#random-forests "Link to this heading")
In random forests (see [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier") and [`RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor") classes), each tree in the ensemble is built from a sample drawn with replacement (i.e., a bootstrap sample) from the training set.
During the construction of each tree in the forest, a random subset of the features is considered. The size of this subset is controlled by the `max_features` parameter; it may include either all input features or a random subset of them (see the [parameter tuning guidelines](https://scikit-learn.org/stable/modules/ensemble.html#random-forest-parameters) for more details).
The purpose of these two sources of randomness (bootstrapping the samples and randomly selecting features at each split) is to decrease the variance of the forest estimator. Indeed, individual decision trees typically exhibit high variance and tend to overfit. The injected randomness in forests yield decision trees with somewhat decoupled prediction errors. By taking an average of those predictions, some errors can cancel out. Random forests achieve a reduced variance by combining diverse trees, sometimes at the cost of a slight increase in bias. In practice the variance reduction is often significant hence yielding an overall better model.
When growing each tree in the forest, the “best” split (i.e. equivalent to passing `splitter="best"` to the underlying decision trees) is chosen according to the impurity criterion. See the [CART mathematical formulation](https://scikit-learn.org/stable/modules/tree.html#tree-mathematical-formulation) for more details.
In contrast to the original publication [[B2001]](https://scikit-learn.org/stable/modules/ensemble.html#b2001), the scikit-learn implementation combines classifiers by averaging their probabilistic prediction, instead of letting each classifier vote for a single class.
A competitive alternative to random forests are [Histogram-Based Gradient Boosting](https://scikit-learn.org/stable/modules/ensemble.html#histogram-based-gradient-boosting) (HGBT) models:
  * Building trees: Random forests typically rely on deep trees (that overfit individually) which uses much computational resources, as they require several splittings and evaluations of candidate splits. Boosting models build shallow trees (that underfit individually) which are faster to fit and predict.
  * Sequential boosting: In HGBT, the decision trees are built sequentially, where each tree is trained to correct the errors made by the previous ones. This allows them to iteratively improve the model’s performance using relatively few trees. In contrast, random forests use a majority vote to predict the outcome, which can require a larger number of trees to achieve the same level of accuracy.
  * Efficient binning: HGBT uses an efficient binning algorithm that can handle large datasets with a high number of features. The binning algorithm can pre-process the data to speed up the subsequent tree construction (see [Why it’s faster](https://scikit-learn.org/stable/modules/ensemble.html#why-it-s-faster)). In contrast, the scikit-learn implementation of random forests does not use binning and relies on exact splitting, which can be computationally expensive.


Overall, the computational cost of HGBT versus RF depends on the specific characteristics of the dataset and the modeling task. It’s a good idea to try both models and compare their performance and computational efficiency on your specific problem to determine which model is the best fit.
Examples
  * [Comparing Random Forests and Histogram Gradient Boosting models](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_hist_grad_boosting_comparison.html#sphx-glr-auto-examples-ensemble-plot-forest-hist-grad-boosting-comparison-py)


###  1.11.2.2. Extremely Randomized Trees[#](https://scikit-learn.org/stable/modules/ensemble.html#extremely-randomized-trees "Link to this heading")
In extremely randomized trees (see [`ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier") and [`ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor") classes), randomness goes one step further in the way splits are computed. As in random forests, a random subset of candidate features is used, but instead of looking for the most discriminative thresholds, thresholds are drawn at random for each candidate feature and the best of these randomly-generated thresholds is picked as the splitting rule. This usually allows to reduce the variance of the model a bit more, at the expense of a slightly greater increase in bias:
```
>>> from sklearn.model_selection import cross_val_score
>>> from sklearn.datasets import make_blobs
>>> from sklearn.ensemble import RandomForestClassifier
>>> from sklearn.ensemble import ExtraTreesClassifier
>>> from sklearn.tree import DecisionTreeClassifier

>>> X, y = make_blobs(n_samples=10000, n_features=10, centers=100,
...     random_state=0)

>>> clf = DecisionTreeClassifier(max_depth=None, min_samples_split=2,
...     random_state=0)
>>> scores = cross_val_score(clf, X, y, cv=5)
>>> scores.mean()
np.float64(0.98)

>>> clf = RandomForestClassifier(n_estimators=10, max_depth=None,
...     min_samples_split=2, random_state=0)
>>> scores = cross_val_score(clf, X, y, cv=5)
>>> scores.mean()
np.float64(0.999)

>>> clf = ExtraTreesClassifier(n_estimators=10, max_depth=None,
...     min_samples_split=2, random_state=0)
>>> scores = cross_val_score(clf, X, y, cv=5)
>>> scores.mean() > 0.999
np.True_

```
Copy to clipboard
[![../_images/sphx_glr_plot_forest_iris_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_forest_iris_001.png) ](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html)
###  1.11.2.3. Parameters[#](https://scikit-learn.org/stable/modules/ensemble.html#parameters "Link to this heading")
The main parameters to adjust when using these methods is `n_estimators` and `max_features`. The former is the number of trees in the forest. The larger the better, but also the longer it will take to compute. In addition, note that results will stop getting significantly better beyond a critical number of trees. The latter is the size of the random subsets of features to consider when splitting a node. The lower the greater the reduction of variance, but also the greater the increase in bias. Empirical good default values are `max_features=1.0` or equivalently `max_features=None` (always considering all features instead of a random subset) for regression problems, and `max_features="sqrt"` (using a random subset of size `sqrt(n_features)`) for classification tasks (where `n_features` is the number of features in the data). The default value of `max_features=1.0` is equivalent to bagged trees and more randomness can be achieved by setting smaller values (e.g. 0.3 is a typical default in the literature). Good results are often achieved when setting `max_depth=None` in combination with `min_samples_split=2` (i.e., when fully developing the trees). Bear in mind though that these values are usually not optimal, and might result in models that consume a lot of RAM. The best parameter values should always be cross-validated. In addition, note that in random forests, bootstrap samples are used by default (`bootstrap=True`) while the default strategy for extra-trees is to use the whole dataset (`bootstrap=False`). When using bootstrap sampling the generalization error can be estimated on the left out or out-of-bag samples. This can be enabled by setting `oob_score=True`.
Note
The size of the model with the default parameters is O(M∗N∗log(N)), where M is the number of trees and N is the number of samples. In order to reduce the size of the model, you can change these parameters: `min_samples_split`, `max_leaf_nodes`, `max_depth` and `min_samples_leaf`.
###  1.11.2.4. Parallelization[#](https://scikit-learn.org/stable/modules/ensemble.html#parallelization "Link to this heading")
Finally, this module also features the parallel construction of the trees and the parallel computation of the predictions through the `n_jobs` parameter. If `n_jobs=k` then computations are partitioned into `k` jobs, and run on `k` cores of the machine. If `n_jobs=-1` then all cores available on the machine are used. Note that because of inter-process communication overhead, the speedup might not be linear (i.e., using `k` jobs will unfortunately not be `k` times as fast). Significant speedup can still be achieved though when building a large number of trees, or when building a single tree requires a fair amount of time (e.g., on large datasets).
Examples
  * [Plot the decision surfaces of ensembles of trees on the iris dataset](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_iris.html#sphx-glr-auto-examples-ensemble-plot-forest-iris-py)
  * [Face completion with a multi-output estimators](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multioutput_face_completion.html#sphx-glr-auto-examples-miscellaneous-plot-multioutput-face-completion-py)


References
[[B2001](https://scikit-learn.org/stable/modules/ensemble.html#id17)]
  1. Breiman, “Random Forests”, Machine Learning, 45(1), 5-32, 2001.


[[B1998](https://scikit-learn.org/stable/modules/ensemble.html#id16)]
  1. Breiman, “Arcing Classifiers”, Annals of Statistics 1998.


  * P. Geurts, D. Ernst., and L. Wehenkel, “Extremely randomized trees”, Machine Learning, 63(1), 3-42, 2006.


###  1.11.2.5. Feature importance evaluation[#](https://scikit-learn.org/stable/modules/ensemble.html#feature-importance-evaluation "Link to this heading")
The relative rank (i.e. depth) of a feature used as a decision node in a tree can be used to assess the relative importance of that feature with respect to the predictability of the target variable. Features used at the top of the tree contribute to the final prediction decision of a larger fraction of the input samples. The **expected fraction of the samples** they contribute to can thus be used as an estimate of the **relative importance of the features**. In scikit-learn, the fraction of samples a feature contributes to is combined with the decrease in impurity from splitting them to create a normalized estimate of the predictive power of that feature.
By **averaging** the estimates of predictive ability over several randomized trees one can **reduce the variance** of such an estimate and use it for feature selection. This is known as the mean decrease in impurity, or MDI. Refer to [[L2014]](https://scikit-learn.org/stable/modules/ensemble.html#l2014) for more information on MDI and feature importance evaluation with Random Forests.
Warning
The impurity-based feature importances computed on tree-based models suffer from two flaws that can lead to misleading conclusions. First they are computed on statistics derived from the training dataset and therefore **do not necessarily inform us on which features are most important to make good predictions on held-out dataset**. Secondly, **they favor high cardinality features** , that is features with many unique values. [Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html#permutation-importance) is an alternative to impurity-based feature importance that does not suffer from these flaws. These two methods of obtaining feature importance are explored in: [Permutation Importance vs Random Forest Feature Importance (MDI)](https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-py).
In practice those estimates are stored as an attribute named `feature_importances_` on the fitted model. This is an array with shape `(n_features,)` whose values are positive and sum to 1.0. The higher the value, the more important is the contribution of the matching feature to the prediction function.
Examples
  * [Feature importances with a forest of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html#sphx-glr-auto-examples-ensemble-plot-forest-importances-py)


References
[[L2014](https://scikit-learn.org/stable/modules/ensemble.html#id18)]
G. Louppe,
###  1.11.2.6. Totally Random Trees Embedding[#](https://scikit-learn.org/stable/modules/ensemble.html#totally-random-trees-embedding "Link to this heading")
[`RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding") implements an unsupervised transformation of the data. Using a forest of completely random trees, [`RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding") encodes the data by the indices of the leaves a data point ends up in. This index is then encoded in a one-of-K manner, leading to a high dimensional, sparse binary coding. This coding can be computed very efficiently and can then be used as a basis for other learning tasks. The size and sparsity of the code can be influenced by choosing the number of trees and the maximum depth per tree. For each tree in the ensemble, the coding contains one entry of one. The size of the coding is at most `n_estimators * 2 ** max_depth`, the maximum number of leaves in the forest.
As neighboring data points are more likely to lie within the same leaf of a tree, the transformation performs an implicit, non-parametric density estimation.
Examples
  * [Hashing feature transformation using Totally Random Trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_random_forest_embedding.html#sphx-glr-auto-examples-ensemble-plot-random-forest-embedding-py)
  * [Manifold learning on handwritten digits: Locally Linear Embedding, Isomap…](https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html#sphx-glr-auto-examples-manifold-plot-lle-digits-py) compares non-linear dimensionality reduction techniques on handwritten digits.
  * [Feature transformations with ensembles of trees](https://scikit-learn.org/stable/auto_examples/ensemble/plot_feature_transformation.html#sphx-glr-auto-examples-ensemble-plot-feature-transformation-py) compares supervised and unsupervised tree based feature transformations.


See also
[Manifold learning](https://scikit-learn.org/stable/modules/manifold.html#manifold) techniques can also be useful to derive non-linear representations of feature space, also these approaches focus also on dimensionality reduction.
###  1.11.2.7. Fitting additional trees[#](https://scikit-learn.org/stable/modules/ensemble.html#fitting-additional-trees "Link to this heading")
RandomForest, Extra-Trees and [`RandomTreesEmbedding`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomTreesEmbedding.html#sklearn.ensemble.RandomTreesEmbedding "sklearn.ensemble.RandomTreesEmbedding") estimators all support `warm_start=True` which allows you to add more trees to an already fitted model.
```
>>> from sklearn.datasets import make_classification
>>> from sklearn.ensemble import RandomForestClassifier

>>> X, y = make_classification(n_samples=100, random_state=1)
>>> clf = RandomForestClassifier(n_estimators=10)
>>> clf = clf.fit(X, y)  # fit with 10 trees
>>> len(clf.estimators_)
10
>>> # set warm_start and increase num of estimators
>>> _ = clf.set_params(n_estimators=20, warm_start=True)
>>> _ = clf.fit(X, y) # fit additional 10 trees
>>> len(clf.estimators_)
20

```
Copy to clipboard
When `random_state` is also set, the internal random state is also preserved between `fit` calls. This means that training a model once with `n` estimators is the same as building the model iteratively via multiple `fit` calls, where the final number of estimators is equal to `n`.
```
>>> clf = RandomForestClassifier(n_estimators=20)  # set `n_estimators` to 10 + 10
>>> _ = clf.fit(X, y)  # fit `estimators_` will be the same as `clf` above

```
Copy to clipboard
Note that this differs from the usual behavior of [random_state](https://scikit-learn.org/stable/glossary.html#term-random_state) in that it does _not_ result in the same result across different calls.
