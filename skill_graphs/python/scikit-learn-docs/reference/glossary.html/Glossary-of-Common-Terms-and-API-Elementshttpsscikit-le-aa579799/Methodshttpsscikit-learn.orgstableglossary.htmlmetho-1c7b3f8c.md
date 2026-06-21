## Methods[#](https://scikit-learn.org/stable/glossary.html#methods "Link to this heading")

`decision_function`[#](https://scikit-learn.org/stable/glossary.html#term-decision_function "Link to this term")

In a fitted [classifier](https://scikit-learn.org/stable/glossary.html#term-classifier) or [outlier detector](https://scikit-learn.org/stable/glossary.html#term-outlier-detector), predicts a “soft” score for each sample in relation to each class, rather than the “hard” categorical prediction produced by [predict](https://scikit-learn.org/stable/glossary.html#term-predict). Its input is usually only some observed data, [X](https://scikit-learn.org/stable/glossary.html#term-X).
If the estimator was not already [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted), calling this method should raise a [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError").
Output conventions:

binary classification

A 1-dimensional array, where values strictly greater than zero indicate the positive class (i.e. the last class in [classes_](https://scikit-learn.org/stable/glossary.html#term-classes_)).

multiclass classification

A 2-dimensional array, where the row-wise arg-maximum is the predicted class. Columns are ordered according to [classes_](https://scikit-learn.org/stable/glossary.html#term-classes_).

multilabel classification

Scikit-learn is inconsistent in its representation of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel) decision functions. It may be represented one of two ways:
  * List of 2d arrays, each array of shape: (`n_samples`, 2), like in multiclass multioutput. List is of length `n_labels`.
  * Single 2d array of shape (`n_samples`, `n_labels`), with each ‘column’ in the array corresponding to the individual binary classification decisions. This is identical to the multiclass classification format, though its semantics differ: it should be interpreted, like in the binary case, by thresholding at 0.



multioutput classification

A list of 2d arrays, corresponding to each multiclass decision function.

outlier detection

A 1-dimensional array, where a value greater than or equal to zero indicates an inlier.

`fit`[#](https://scikit-learn.org/stable/glossary.html#term-fit "Link to this term")

The `fit` method is provided on every estimator. It usually takes some [samples](https://scikit-learn.org/stable/glossary.html#term-samples) `X`, [targets](https://scikit-learn.org/stable/glossary.html#term-targets) `y` if the model is supervised, and potentially other [sample properties](https://scikit-learn.org/stable/glossary.html#term-sample-properties) such as [sample_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight). It should:
  * clear any prior [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes) stored on the estimator, unless [warm_start](https://scikit-learn.org/stable/glossary.html#term-warm_start) is used;
  * validate and interpret any [parameters](https://scikit-learn.org/stable/glossary.html#term-parameters), ideally raising an error if invalid;
  * validate the input data;
  * estimate and store model attributes from the estimated parameters and provided data; and
  * return the now [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted) estimator to facilitate method chaining.


[Target Types](https://scikit-learn.org/stable/glossary.html#glossary-target-types) describes possible formats for `y`.

`fit_predict`[#](https://scikit-learn.org/stable/glossary.html#term-fit_predict "Link to this term")

Used especially for [unsupervised](https://scikit-learn.org/stable/glossary.html#term-unsupervised), [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive) estimators, this fits the model and returns the predictions (similar to [predict](https://scikit-learn.org/stable/glossary.html#term-predict)) on the training data. In clusterers, these predictions are also stored in the [labels_](https://scikit-learn.org/stable/glossary.html#term-labels_) attribute, and the output of `.fit_predict(X)` is usually equivalent to `.fit(X).predict(X)`. The parameters to `fit_predict` are the same as those to `fit`.

`fit_transform`[#](https://scikit-learn.org/stable/glossary.html#term-fit_transform "Link to this term")

A method on [transformers](https://scikit-learn.org/stable/glossary.html#term-transformers) which fits the estimator and returns the transformed training data. It takes parameters as in [fit](https://scikit-learn.org/stable/glossary.html#term-fit) and its output should have the same shape as calling `.fit(X, ...).transform(X)`. There are nonetheless rare cases where `.fit_transform(X, ...)` and `.fit(X, ...).transform(X)` do not return the same value, wherein training data needs to be handled differently (due to model blending in stacked ensembles, for instance; such cases should be clearly documented). [Transductive](https://scikit-learn.org/stable/glossary.html#term-transductive) transformers may also provide `fit_transform` but not [transform](https://scikit-learn.org/stable/glossary.html#term-transform).
One reason to implement `fit_transform` is that performing `fit` and `transform` separately would be less efficient than together. [`base.TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin") provides a default implementation, providing a consistent interface across transformers where `fit_transform` is or is not specialized.
In [inductive](https://scikit-learn.org/stable/glossary.html#term-inductive) learning – where the goal is to learn a generalized model that can be applied to new data – users should be careful not to apply `fit_transform` to the entirety of a dataset (i.e. training and test data together) before further modelling, as this results in [data leakage](https://scikit-learn.org/stable/glossary.html#term-data-leakage).

`get_feature_names_out`[#](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out "Link to this term")

Primarily for [feature extractors](https://scikit-learn.org/stable/glossary.html#term-feature-extractors), but also used for other transformers to provide string names for each column in the output of the estimator’s [transform](https://scikit-learn.org/stable/glossary.html#term-transform) method. It outputs an array of strings and may take an array-like of strings as input, corresponding to the names of input columns from which output column names can be generated. If `input_features` is not passed in, then the `feature_names_in_` attribute will be used. If the `feature_names_in_` attribute is not defined, then the input names are named `[x0, x1, ..., x(n_features_in_ - 1)]`.

`get_n_splits`[#](https://scikit-learn.org/stable/glossary.html#term-get_n_splits "Link to this term")

On a [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter) (not an estimator), returns the number of elements one would get if iterating through the return value of [split](https://scikit-learn.org/stable/glossary.html#term-split) given the same parameters. Takes the same parameters as split.

`get_params`[#](https://scikit-learn.org/stable/glossary.html#term-get_params "Link to this term")

Gets all [parameters](https://scikit-learn.org/stable/glossary.html#term-parameters), and their values, that can be set using [set_params](https://scikit-learn.org/stable/glossary.html#term-set_params). A parameter `deep` can be used, when set to False to only return those parameters not including `__`, i.e. not due to indirection via contained estimators.
Most estimators adopt the definition from [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator"), which simply adopts the parameters defined for `__init__`. [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline"), among others, reimplements `get_params` to declare the estimators named in its `steps` parameters as themselves being parameters.

`partial_fit`[#](https://scikit-learn.org/stable/glossary.html#term-partial_fit "Link to this term")

Facilitates fitting an estimator in an online fashion. Unlike `fit`, repeatedly calling `partial_fit` does not clear the model, but updates it with the data provided. The portion of data provided to `partial_fit` may be called a mini-batch. Each mini-batch must be of consistent shape, etc. In iterative estimators, `partial_fit` often only performs a single iteration.
`partial_fit` may also be used for [out-of-core](https://scikit-learn.org/stable/glossary.html#term-out-of-core) learning, although usually limited to the case where learning can be performed online, i.e. the model is usable after each `partial_fit` and there is no separate processing needed to finalize the model. [`cluster.Birch`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.Birch.html#sklearn.cluster.Birch "sklearn.cluster.Birch") introduces the convention that calling `partial_fit(X)` will produce a model that is not finalized, but the model can be finalized by calling `partial_fit()` i.e. without passing a further mini-batch.
Generally, estimator parameters should not be modified between calls to `partial_fit`, although `partial_fit` should validate them as well as the new mini-batch of data. In contrast, `warm_start` is used to repeatedly fit the same estimator with the same data but varying parameters.
Like `fit`, `partial_fit` should return the estimator object.
To clear the model, a new estimator should be constructed, for instance with [`base.clone`](https://scikit-learn.org/stable/modules/generated/sklearn.base.clone.html#sklearn.base.clone "sklearn.base.clone").
Note: Using `partial_fit` after `fit` results in undefined behavior.

`predict`[#](https://scikit-learn.org/stable/glossary.html#term-predict "Link to this term")

Makes a prediction for each sample, usually only taking [X](https://scikit-learn.org/stable/glossary.html#term-X) as input (but see under regressor output conventions below). In a [classifier](https://scikit-learn.org/stable/glossary.html#term-classifier) or [regressor](https://scikit-learn.org/stable/glossary.html#term-regressor), this prediction is in the same target space used in fitting (e.g. one of {‘red’, ‘amber’, ‘green’} if the `y` in fitting consisted of these strings). Despite this, even when `y` passed to [fit](https://scikit-learn.org/stable/glossary.html#term-fit) is a list or other array-like, the output of `predict` should always be an array or sparse matrix. In a [clusterer](https://scikit-learn.org/stable/glossary.html#term-clusterer) or [outlier detector](https://scikit-learn.org/stable/glossary.html#term-outlier-detector) the prediction is an integer.
If the estimator was not already [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted), calling this method should raise a [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError").
Output conventions:

classifier

An array of shape `(n_samples,)` `(n_samples, n_outputs)`. [Multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel) data may be represented as a sparse matrix if a sparse matrix was used in fitting. Each element should be one of the values in the classifier’s [classes_](https://scikit-learn.org/stable/glossary.html#term-classes_) attribute.

clusterer

An array of shape `(n_samples,)` where each value is from 0 to `n_clusters - 1` if the corresponding sample is clustered, and -1 if the sample is not clustered, as in [`cluster.dbscan`](https://scikit-learn.org/stable/modules/generated/dbscan-function.html#sklearn.cluster.dbscan "sklearn.cluster.dbscan").

outlier detector

An array of shape `(n_samples,)` where each value is -1 for an outlier and 1 otherwise.

regressor

A numeric array of shape `(n_samples,)`, usually float64. Some regressors have extra options in their `predict` method, allowing them to return standard deviation (`return_std=True`) or covariance (`return_cov=True`) relative to the predicted value. In this case, the return value is a tuple of arrays corresponding to (prediction mean, std, cov) as required.

`predict_log_proba`[#](https://scikit-learn.org/stable/glossary.html#term-predict_log_proba "Link to this term")

The natural logarithm of the output of [predict_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba), provided to facilitate numerical stability.

`predict_proba`[#](https://scikit-learn.org/stable/glossary.html#term-predict_proba "Link to this term")

A method in [classifiers](https://scikit-learn.org/stable/glossary.html#term-classifiers) and [clusterers](https://scikit-learn.org/stable/glossary.html#term-clusterers) that can return probability estimates for each class/cluster. Its input is usually only some observed data, [X](https://scikit-learn.org/stable/glossary.html#term-X).
If the estimator was not already [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted), calling this method should raise a [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError").
Output conventions are like those for [decision_function](https://scikit-learn.org/stable/glossary.html#term-decision_function) except in the [binary](https://scikit-learn.org/stable/glossary.html#term-binary) classification case, where one column is output for each class (while `decision_function` outputs a 1d array). For binary and multiclass predictions, each row should add to 1.
Like other methods, `predict_proba` should only be present when the estimator can make probabilistic predictions (see [duck typing](https://scikit-learn.org/stable/glossary.html#term-duck-typing)). This means that the presence of the method may depend on estimator parameters (e.g. in [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")) or training data (e.g. in [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV")) and may only appear after fitting.

`score`[#](https://scikit-learn.org/stable/glossary.html#term-score "Link to this term")

A method on an estimator, usually a [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor), which evaluates its predictions on a given dataset, and returns a single numerical score. A greater return value should indicate better predictions; accuracy is used for classifiers and R^2 for regressors by default.
If the estimator was not already [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted), calling this method should raise a [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError").
Some estimators implement a custom, estimator-specific score function, often the likelihood of the data under the model.

`score_samples`[#](https://scikit-learn.org/stable/glossary.html#term-score_samples "Link to this term")

A method that returns a score for each given sample. The exact definition of _score_ varies from one class to another. In the case of density estimation, it can be the log density model on the data, and in the case of outlier detection, it can be the opposite of the outlier factor of the data.
If the estimator was not already [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted), calling this method should raise a [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError").

`set_params`[#](https://scikit-learn.org/stable/glossary.html#term-set_params "Link to this term")

Available in any estimator, takes keyword arguments corresponding to keys in [get_params](https://scikit-learn.org/stable/glossary.html#term-get_params). Each is provided a new value to assign such that calling `get_params` after `set_params` will reflect the changed [parameters](https://scikit-learn.org/stable/glossary.html#term-parameters). Most estimators use the implementation in [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator"), which handles nested parameters and otherwise sets the parameter as an attribute on the estimator. The method is overridden in [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline") and related estimators.

`split`[#](https://scikit-learn.org/stable/glossary.html#term-split "Link to this term")

On a [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter) (not an estimator), this method accepts parameters ([X](https://scikit-learn.org/stable/glossary.html#term-X), [y](https://scikit-learn.org/stable/glossary.html#term-y), [groups](https://scikit-learn.org/stable/glossary.html#term-groups)), where all may be optional, and returns an iterator over `(train_idx, test_idx)` pairs. Each of {train,test}_idx is a 1d integer array, with values from 0 from `X.shape[0] - 1` of any length, such that no values appear in both some `train_idx` and its corresponding `test_idx`.

`transform`[#](https://scikit-learn.org/stable/glossary.html#term-transform "Link to this term")

In a [transformer](https://scikit-learn.org/stable/glossary.html#term-transformer), transforms the input, usually only [X](https://scikit-learn.org/stable/glossary.html#term-X), into some transformed space (conventionally notated as [Xt](https://scikit-learn.org/stable/glossary.html#term-Xt)). Output is an array or sparse matrix of length [n_samples](https://scikit-learn.org/stable/glossary.html#term-n_samples) and with the number of columns fixed after [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting).
If the estimator was not already [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted), calling this method should raise a [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError").
