## Version 1.7.2[#](https://scikit-learn.org/stable/whats_new/v1.7.html#version-1-7-2 "Link to this heading")
**September 2025**
###  [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-compose "Link to this heading")
  * Fix [`compose.TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor") now passes the transformed target to the regressor with the same number of dimensions as the original target. By


###  [`sklearn.feature_extraction`](https://scikit-learn.org/stable/api/sklearn.feature_extraction.html#module-sklearn.feature_extraction "sklearn.feature_extraction")[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-feature-extraction "Link to this heading")
  * Fix Set the tag `requires_fit=False` for the classes [`feature_extraction.FeatureHasher`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher "sklearn.feature_extraction.FeatureHasher") and [`feature_extraction.text.HashingVectorizer`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html#sklearn.feature_extraction.text.HashingVectorizer "sklearn.feature_extraction.text.HashingVectorizer"). By


###  [`sklearn.impute`](https://scikit-learn.org/stable/api/sklearn.impute.html#module-sklearn.impute "sklearn.impute")[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-impute "Link to this heading")
  * Fix Fixed a bug in [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer") with `strategy="most_frequent"` when there is a tie in the most frequent value and the input data has mixed types. By


###  [`sklearn.linear_model`](https://scikit-learn.org/stable/api/sklearn.linear_model.html#module-sklearn.linear_model "sklearn.linear_model")[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-linear-model "Link to this heading")
  * Fix Fixed a bug with `solver="newton-cholesky"` on multi-class problems in [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV") and in [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression") when used with `warm_start=True`. The bug appeared either with `fit_intercept=True` or with `penalty=None` (both resulting in unpenalized parameters for the solver). The coefficients and intercepts of the last class as provided by warm start were partially wrongly overwritten by zero. By


###  [`sklearn.pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline")[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-pipeline "Link to this heading")
  * Fix [`pipeline.FeatureUnion`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion "sklearn.pipeline.FeatureUnion") now validates that all transformers return 2D outputs and raises an informative error when transformers return 1D outputs, preventing silent failures that previously produced meaningless concatenated results. By
