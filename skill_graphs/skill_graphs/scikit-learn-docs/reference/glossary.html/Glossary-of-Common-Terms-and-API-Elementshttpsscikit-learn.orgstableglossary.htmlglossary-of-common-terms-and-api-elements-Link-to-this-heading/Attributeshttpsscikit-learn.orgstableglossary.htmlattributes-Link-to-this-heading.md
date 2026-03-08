## Attributes[#](https://scikit-learn.org/stable/glossary.html#attributes "Link to this heading")
See concept [attribute](https://scikit-learn.org/stable/glossary.html#term-attribute).

`classes_`[#](https://scikit-learn.org/stable/glossary.html#term-classes_ "Link to this term")

A list of class labels known to the [classifier](https://scikit-learn.org/stable/glossary.html#term-classifier), mapping each label to a numerical index used in the model representation our output. For instance, the array output from [predict_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba) has columns aligned with `classes_`. For [multi-output](https://scikit-learn.org/stable/glossary.html#term-multi-output) classifiers, `classes_` should be a list of lists, with one class listing for each output. For each output, the classes should be sorted (numerically, or lexicographically for strings).
`classes_` and the mapping to indices is often managed with [`preprocessing.LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder").

`components_`[#](https://scikit-learn.org/stable/glossary.html#term-components_ "Link to this term")

An affine transformation matrix of shape `(n_components, n_features)` used in many linear [transformers](https://scikit-learn.org/stable/glossary.html#term-transformers) where [n_components](https://scikit-learn.org/stable/glossary.html#term-n_components) is the number of output features and [n_features](https://scikit-learn.org/stable/glossary.html#term-n_features) is the number of input features.
See also [coef_](https://scikit-learn.org/stable/glossary.html#term-coef_) which is a similar attribute for linear predictors.

`coef_`[#](https://scikit-learn.org/stable/glossary.html#term-coef_ "Link to this term")

The weight/coefficient matrix of a generalized linear model [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor), of shape `(n_features,)` for binary classification and single-output regression, `(n_classes, n_features)` for multiclass classification and `(n_targets, n_features)` for multi-output regression. Note this does not include the intercept (or bias) term, which is stored in `intercept_`.
When available, `feature_importances_` is not usually provided as well, but can be calculated as the norm of each feature’s entry in `coef_`.
See also [components_](https://scikit-learn.org/stable/glossary.html#term-components_) which is a similar attribute for linear transformers.

`embedding_`[#](https://scikit-learn.org/stable/glossary.html#term-embedding_ "Link to this term")

An embedding of the training data in [manifold learning](https://scikit-learn.org/stable/modules/manifold.html#manifold) estimators, with shape `(n_samples, n_components)`, identical to the output of [fit_transform](https://scikit-learn.org/stable/glossary.html#term-fit_transform). See also [labels_](https://scikit-learn.org/stable/glossary.html#term-labels_).

`n_iter_`[#](https://scikit-learn.org/stable/glossary.html#term-n_iter_ "Link to this term")

The number of iterations actually performed when fitting an iterative estimator that may stop upon convergence. See also [max_iter](https://scikit-learn.org/stable/glossary.html#term-max_iter).

`feature_importances_`[#](https://scikit-learn.org/stable/glossary.html#term-feature_importances_ "Link to this term")

A vector of shape `(n_features,)` available in some [predictors](https://scikit-learn.org/stable/glossary.html#term-predictors) to provide a relative measure of the importance of each feature in the predictions of the model.

`labels_`[#](https://scikit-learn.org/stable/glossary.html#term-labels_ "Link to this term")

A vector containing a cluster label for each sample of the training data in [clusterers](https://scikit-learn.org/stable/glossary.html#term-clusterers), identical to the output of [fit_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict). See also [embedding_](https://scikit-learn.org/stable/glossary.html#term-embedding_).
