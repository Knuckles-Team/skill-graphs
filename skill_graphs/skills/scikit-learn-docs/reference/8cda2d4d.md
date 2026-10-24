#  3.2. Tuning the hyper-parameters of an estimator[#](https://scikit-learn.org/stable/modules/grid_search.html#tuning-the-hyper-parameters-of-an-estimator "Link to this heading")
Hyper-parameters are parameters that are not directly learnt within estimators. In scikit-learn they are passed as arguments to the constructor of the estimator classes. Typical examples include `C`, `kernel` and `gamma` for Support Vector Classifier, `alpha` for Lasso, etc.
It is possible and recommended to search the hyper-parameter space for the best [cross validation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation) score.
Any parameter provided when constructing an estimator may be optimized in this manner. Specifically, to find the names and current values for all parameters for a given estimator, use:
```
estimator.get_params()

```
Copy to clipboard
A search consists of:
  * an estimator (regressor or classifier such as `sklearn.svm.SVC()`);
  * a parameter space;
  * a method for searching or sampling candidates;
  * a cross-validation scheme; and
  * a [score function](https://scikit-learn.org/stable/modules/grid_search.html#gridsearch-scoring).


Two generic approaches to parameter search are provided in scikit-learn: for given values, [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV") exhaustively considers all parameter combinations, while [`RandomizedSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV "sklearn.model_selection.RandomizedSearchCV") can sample a given number of candidates from a parameter space with a specified distribution. Both these tools have successive halving counterparts [`HalvingGridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingGridSearchCV.html#sklearn.model_selection.HalvingGridSearchCV "sklearn.model_selection.HalvingGridSearchCV") and [`HalvingRandomSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.HalvingRandomSearchCV.html#sklearn.model_selection.HalvingRandomSearchCV "sklearn.model_selection.HalvingRandomSearchCV"), which can be much faster at finding a good parameter combination.
After describing these tools we detail [best practices](https://scikit-learn.org/stable/modules/grid_search.html#grid-search-tips) applicable to these approaches. Some models allow for specialized, efficient parameter search strategies, outlined in [Alternatives to brute force parameter search](https://scikit-learn.org/stable/modules/grid_search.html#alternative-cv).
Note that it is common that a small subset of those parameters can have a large impact on the predictive or computation performance of the model while others can be left to their default values. It is recommended to read the docstring of the estimator class to get a finer understanding of their expected behavior, possibly by reading the enclosed reference to the literature.
