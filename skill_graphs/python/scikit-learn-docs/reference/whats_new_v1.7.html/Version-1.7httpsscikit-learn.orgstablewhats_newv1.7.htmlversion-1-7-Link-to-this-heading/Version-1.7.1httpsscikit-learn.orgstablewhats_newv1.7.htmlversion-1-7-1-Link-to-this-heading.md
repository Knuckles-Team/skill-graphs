## Version 1.7.1[#](https://scikit-learn.org/stable/whats_new/v1.7.html#version-1-7-1 "Link to this heading")
**July 2025**
###  [`sklearn.base`](https://scikit-learn.org/stable/api/sklearn.base.html#module-sklearn.base "sklearn.base")[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-base "Link to this heading")
  * Fix Fix regression in HTML representation when detecting the non-default parameters that where of array-like types. By


###  [`sklearn.compose`](https://scikit-learn.org/stable/api/sklearn.compose.html#module-sklearn.compose "sklearn.compose")[#](https://scikit-learn.org/stable/whats_new/v1.7.html#id1 "Link to this heading")
  * Fix [`compose.ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html#sklearn.compose.ColumnTransformer "sklearn.compose.ColumnTransformer") now correctly preserves non-default index when mixing pandas Series and Dataframes. By


###  [`sklearn.datasets`](https://scikit-learn.org/stable/api/sklearn.datasets.html#module-sklearn.datasets "sklearn.datasets")[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-datasets "Link to this heading")
  * Fix Fixed a regression preventing to extract the downloaded dataset in [`datasets.fetch_20newsgroups`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups "sklearn.datasets.fetch_20newsgroups"), [`datasets.fetch_20newsgroups_vectorized`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized "sklearn.datasets.fetch_20newsgroups_vectorized"), [`datasets.fetch_lfw_people`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#sklearn.datasets.fetch_lfw_people "sklearn.datasets.fetch_lfw_people") and [`datasets.fetch_lfw_pairs`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html#sklearn.datasets.fetch_lfw_pairs "sklearn.datasets.fetch_lfw_pairs"). This only affects Python versions `>=3.10.0,<=3.10.11` and `>=3.11.0,<=3.11.3`. By


###  [`sklearn.inspection`](https://scikit-learn.org/stable/api/sklearn.inspection.html#module-sklearn.inspection "sklearn.inspection")[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-inspection "Link to this heading")
  * Fix Fix multiple issues in the multiclass setting of [`inspection.DecisionBoundaryDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.inspection.DecisionBoundaryDisplay.html#sklearn.inspection.DecisionBoundaryDisplay "sklearn.inspection.DecisionBoundaryDisplay"):
    * `contour` plotting now correctly shows the decision boundary.
    * `cmap` and `colors` are now properly ignored in favor of `multiclass_colors`.
    * Linear segmented colormaps are now fully supported.
By


###  [`sklearn.naive_bayes`](https://scikit-learn.org/stable/api/sklearn.naive_bayes.html#module-sklearn.naive_bayes "sklearn.naive_bayes")[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-naive-bayes "Link to this heading")
  * Fix [`naive_bayes.CategoricalNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB "sklearn.naive_bayes.CategoricalNB") now correctly declares that it accepts categorical features in the tags returned by its `__sklearn_tags__` method. By


###  [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")[#](https://scikit-learn.org/stable/whats_new/v1.7.html#sklearn-utils "Link to this heading")
  * Fix Fixed a spurious warning (about the number of unique classes being greater than 50% of the number of samples) that could occur when passing `classes` [`utils.multiclass.type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target"). By
