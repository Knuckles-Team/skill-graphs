## Version 1.6.1[#](https://scikit-learn.org/stable/whats_new/v1.6.html#version-1-6-1 "Link to this heading")
**January 2025**
### Changed models[#](https://scikit-learn.org/stable/whats_new/v1.6.html#changed-models "Link to this heading")
  * Fix The `tags.input_tags.sparse` flag was corrected for a majority of estimators. By


### Changes impacting many modules[#](https://scikit-learn.org/stable/whats_new/v1.6.html#changes-impacting-many-modules "Link to this heading")
  * Fix `_more_tags`, `_get_tags`, and `_safe_tags` are now raising a


###  [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-metrics "Link to this heading")
  * Fix Fix regression when scikit-learn metric called on PyTorch CPU tensors would raise an error (with array API dispatch disabled which is the default). By


###  [`sklearn.model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-model-selection "Link to this heading")
  * Fix [`cross_validate`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_validate.html#sklearn.model_selection.cross_validate "sklearn.model_selection.cross_validate"), [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html#sklearn.model_selection.cross_val_predict "sklearn.model_selection.cross_val_predict"), and [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score "sklearn.model_selection.cross_val_score") now accept `params=None` when metadata routing is enabled. By


###  [`sklearn.tree`](https://scikit-learn.org/stable/api/sklearn.tree.html#module-sklearn.tree "sklearn.tree")[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-tree "Link to this heading")
  * Fix Use `log2` instead of `ln` for building trees to maintain behavior of previous versions. By


###  [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")[#](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-utils "Link to this heading")
  * Enhancement `utils.estimator_checks.check_estimator_sparse_tag` ensures that the estimator tag `input_tags.sparse` is consistent with its `fit` method (accepting sparse input `X` or raising the appropriate error). By
  * Fix Raise a `DeprecationWarning` when there is no concrete implementation of `__sklearn_tags__` in the MRO of the estimator. We request to inherit from `BaseEstimator` that implements `__sklearn_tags__`. By
