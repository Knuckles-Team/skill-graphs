## Class APIs and Estimator Types[#](https://scikit-learn.org/stable/glossary.html#class-apis-and-estimator-types "Link to this heading")

classifier[#](https://scikit-learn.org/stable/glossary.html#term-classifier "Link to this term")


classifiers[#](https://scikit-learn.org/stable/glossary.html#term-classifiers "Link to this term")

A [supervised](https://scikit-learn.org/stable/glossary.html#term-supervised) (or [semi-supervised](https://scikit-learn.org/stable/glossary.html#term-semi-supervised)) [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor) with a finite set of discrete possible output values.
A classifier supports modeling some of [binary](https://scikit-learn.org/stable/glossary.html#term-binary), [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass), [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel), or [multiclass multioutput](https://scikit-learn.org/stable/glossary.html#term-multiclass-multioutput) targets. Within scikit-learn, all classifiers support multi-class classification, defaulting to using a one-vs-rest strategy over the binary classification problem.
Classifiers must store a [classes_](https://scikit-learn.org/stable/glossary.html#term-classes_) attribute after fitting, and inherit from [`base.ClassifierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin"), which sets their corresponding [estimator tags](https://scikit-learn.org/stable/glossary.html#term-estimator-tags) correctly.
A classifier can be distinguished from other estimators with [`is_classifier`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_classifier.html#sklearn.base.is_classifier "sklearn.base.is_classifier").
A classifier must implement:
  * [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
  * [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
  * [score](https://scikit-learn.org/stable/glossary.html#term-score)


It may also be appropriate to implement [decision_function](https://scikit-learn.org/stable/glossary.html#term-decision_function), [predict_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba) and [predict_log_proba](https://scikit-learn.org/stable/glossary.html#term-predict_log_proba).

clusterer[#](https://scikit-learn.org/stable/glossary.html#term-clusterer "Link to this term")


clusterers[#](https://scikit-learn.org/stable/glossary.html#term-clusterers "Link to this term")

A [unsupervised](https://scikit-learn.org/stable/glossary.html#term-unsupervised) [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor) with a finite set of discrete output values.
A clusterer usually stores [labels_](https://scikit-learn.org/stable/glossary.html#term-labels_) after fitting, and must do so if it is [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive).
A clusterer must implement:
  * [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
  * [fit_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict) if [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive)
  * [predict](https://scikit-learn.org/stable/glossary.html#term-predict) if [inductive](https://scikit-learn.org/stable/glossary.html#term-inductive)



density estimator[#](https://scikit-learn.org/stable/glossary.html#term-density-estimator "Link to this term")

An [unsupervised](https://scikit-learn.org/stable/glossary.html#term-unsupervised) estimation of input probability density function. Commonly used techniques are:
  * [Kernel Density Estimation](https://scikit-learn.org/stable/modules/density.html#kernel-density) - uses a kernel function, controlled by the bandwidth parameter to represent density;
  * [Gaussian mixture](https://scikit-learn.org/stable/modules/mixture.html#mixture) - uses mixture of Gaussian models to represent density.



estimator[#](https://scikit-learn.org/stable/glossary.html#term-estimator "Link to this term")


estimators[#](https://scikit-learn.org/stable/glossary.html#term-estimators "Link to this term")

An object which manages the estimation and decoding of a model. The model is estimated as a deterministic function of:
  * [parameters](https://scikit-learn.org/stable/glossary.html#term-parameters) provided in object construction or with [set_params](https://scikit-learn.org/stable/glossary.html#term-set_params);
  * the global [random_state](https://scikit-learn.org/stable/glossary.html#term-random_state) parameter is set to None; and
  * any data or [sample properties](https://scikit-learn.org/stable/glossary.html#term-sample-properties) passed to the most recent call to [fit](https://scikit-learn.org/stable/glossary.html#term-fit), [fit_transform](https://scikit-learn.org/stable/glossary.html#term-fit_transform) or [fit_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict), or data similarly passed in a sequence of calls to [partial_fit](https://scikit-learn.org/stable/glossary.html#term-partial_fit).


The estimated model is stored in public and private [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes) on the estimator instance, facilitating decoding through prediction and transformation methods.
Estimators must provide a [fit](https://scikit-learn.org/stable/glossary.html#term-fit) method, and should provide [set_params](https://scikit-learn.org/stable/glossary.html#term-set_params) and [get_params](https://scikit-learn.org/stable/glossary.html#term-get_params), although these are usually provided by inheritance from [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator").
The core functionality of some estimators may also be available as a [function](https://scikit-learn.org/stable/glossary.html#term-function).

feature extractor[#](https://scikit-learn.org/stable/glossary.html#term-feature-extractor "Link to this term")


feature extractors[#](https://scikit-learn.org/stable/glossary.html#term-feature-extractors "Link to this term")

A [transformer](https://scikit-learn.org/stable/glossary.html#term-transformer) which takes input where each sample is not represented as an [array-like](https://scikit-learn.org/stable/glossary.html#term-array-like) object of fixed length, and produces an [array-like](https://scikit-learn.org/stable/glossary.html#term-array-like) object of [features](https://scikit-learn.org/stable/glossary.html#term-features) for each sample (and thus a 2-dimensional array-like for a set of samples). In other words, it (lossily) maps a non-rectangular data representation into [rectangular](https://scikit-learn.org/stable/glossary.html#term-rectangular) data.
Feature extractors must implement at least:
  * [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
  * [transform](https://scikit-learn.org/stable/glossary.html#term-transform)
  * [get_feature_names_out](https://scikit-learn.org/stable/glossary.html#term-get_feature_names_out)



meta-estimator[#](https://scikit-learn.org/stable/glossary.html#term-meta-estimator "Link to this term")


meta-estimators[#](https://scikit-learn.org/stable/glossary.html#term-meta-estimators "Link to this term")


metaestimator[#](https://scikit-learn.org/stable/glossary.html#term-metaestimator "Link to this term")


metaestimators[#](https://scikit-learn.org/stable/glossary.html#term-metaestimators "Link to this term")

An [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator) which takes another estimator as a parameter. Examples include [`pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline"), [`model_selection.GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV"), [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel") and [`ensemble.BaggingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.BaggingClassifier.html#sklearn.ensemble.BaggingClassifier "sklearn.ensemble.BaggingClassifier").
In a meta-estimator’s [fit](https://scikit-learn.org/stable/glossary.html#term-fit) method, any contained estimators should be [cloned](https://scikit-learn.org/stable/glossary.html#term-cloned) before they are fit.
An exception to this is that an estimator may explicitly document that it accepts a pre-fitted estimator (e.g. using `prefit=True` in [`feature_selection.SelectFromModel`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel "sklearn.feature_selection.SelectFromModel")). One known issue with this is that the pre-fitted estimator will lose its model if the meta-estimator is cloned. A meta-estimator should have `fit` called before prediction, even if all contained estimators are pre-fitted.
In cases where a meta-estimator’s primary behaviors (e.g. [predict](https://scikit-learn.org/stable/glossary.html#term-predict) or [transform](https://scikit-learn.org/stable/glossary.html#term-transform) implementation) are functions of prediction/transformation methods of the provided _base estimator_ (or multiple base estimators), a meta-estimator should provide at least the standard methods provided by the base estimator. It may not be possible to identify which methods are provided by the underlying estimator until the meta-estimator has been [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted) (see also [duck typing](https://scikit-learn.org/stable/glossary.html#term-duck-typing)), for which [`utils.metaestimators.available_if`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.metaestimators.available_if.html#sklearn.utils.metaestimators.available_if "sklearn.utils.metaestimators.available_if") may help. It should also provide (or modify) the [estimator tags](https://scikit-learn.org/stable/glossary.html#term-estimator-tags) and [classes_](https://scikit-learn.org/stable/glossary.html#term-classes_) attribute provided by the base estimator.
Meta-estimators should be careful to validate data as minimally as possible before passing it to an underlying estimator. This saves computation time, and may, for instance, allow the underlying estimator to easily work with data that is not [rectangular](https://scikit-learn.org/stable/glossary.html#term-rectangular).

outlier detector[#](https://scikit-learn.org/stable/glossary.html#term-outlier-detector "Link to this term")


outlier detectors[#](https://scikit-learn.org/stable/glossary.html#term-outlier-detectors "Link to this term")

An [unsupervised](https://scikit-learn.org/stable/glossary.html#term-unsupervised) binary [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor) which models the distinction between core and outlying samples.
Outlier detectors must implement:
  * [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
  * [fit_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict) if [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive)
  * [predict](https://scikit-learn.org/stable/glossary.html#term-predict) if [inductive](https://scikit-learn.org/stable/glossary.html#term-inductive)


Inductive outlier detectors may also implement [decision_function](https://scikit-learn.org/stable/glossary.html#term-decision_function) to give a normalized inlier score where outliers have score below 0. [score_samples](https://scikit-learn.org/stable/glossary.html#term-score_samples) may provide an unnormalized score per sample.

predictor[#](https://scikit-learn.org/stable/glossary.html#term-predictor "Link to this term")


predictors[#](https://scikit-learn.org/stable/glossary.html#term-predictors "Link to this term")

An [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator) supporting [predict](https://scikit-learn.org/stable/glossary.html#term-predict) and/or [fit_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict). This encompasses [classifier](https://scikit-learn.org/stable/glossary.html#term-classifier), [regressor](https://scikit-learn.org/stable/glossary.html#term-regressor), [outlier detector](https://scikit-learn.org/stable/glossary.html#term-outlier-detector) and [clusterer](https://scikit-learn.org/stable/glossary.html#term-clusterer).
In statistics, “predictors” refers to [features](https://scikit-learn.org/stable/glossary.html#term-features).

regressor[#](https://scikit-learn.org/stable/glossary.html#term-regressor "Link to this term")


regressors[#](https://scikit-learn.org/stable/glossary.html#term-regressors "Link to this term")

A [supervised](https://scikit-learn.org/stable/glossary.html#term-supervised) (or [semi-supervised](https://scikit-learn.org/stable/glossary.html#term-semi-supervised)) [predictor](https://scikit-learn.org/stable/glossary.html#term-predictor) with [continuous](https://scikit-learn.org/stable/glossary.html#term-continuous) output values.
Regressors inherit from [`base.RegressorMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin "sklearn.base.RegressorMixin"), which sets their [estimator tags](https://scikit-learn.org/stable/glossary.html#term-estimator-tags) correctly.
A regressor can be distinguished from other estimators with [`is_regressor`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_regressor.html#sklearn.base.is_regressor "sklearn.base.is_regressor").
A regressor must implement:
  * [fit](https://scikit-learn.org/stable/glossary.html#term-fit)
  * [predict](https://scikit-learn.org/stable/glossary.html#term-predict)
  * [score](https://scikit-learn.org/stable/glossary.html#term-score)



transformer[#](https://scikit-learn.org/stable/glossary.html#term-transformer "Link to this term")


transformers[#](https://scikit-learn.org/stable/glossary.html#term-transformers "Link to this term")

An estimator supporting [transform](https://scikit-learn.org/stable/glossary.html#term-transform) and/or [fit_transform](https://scikit-learn.org/stable/glossary.html#term-fit_transform). A purely [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive) transformer, such as [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE"), may not implement `transform`.

vectorizer[#](https://scikit-learn.org/stable/glossary.html#term-vectorizer "Link to this term")


vectorizers[#](https://scikit-learn.org/stable/glossary.html#term-vectorizers "Link to this term")

See [feature extractor](https://scikit-learn.org/stable/glossary.html#term-feature-extractor).
There are further APIs specifically related to a small family of estimators, such as:

cross-validation splitter[#](https://scikit-learn.org/stable/glossary.html#term-cross-validation-splitter "Link to this term")


CV splitter[#](https://scikit-learn.org/stable/glossary.html#term-CV-splitter "Link to this term")


cross-validation generator[#](https://scikit-learn.org/stable/glossary.html#term-cross-validation-generator "Link to this term")

A non-estimator family of classes used to split a dataset into a sequence of train and test portions (see [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)), by providing [split](https://scikit-learn.org/stable/glossary.html#term-split) and [get_n_splits](https://scikit-learn.org/stable/glossary.html#term-get_n_splits) methods. Note that unlike estimators, these do not have [fit](https://scikit-learn.org/stable/glossary.html#term-fit) methods and do not provide [set_params](https://scikit-learn.org/stable/glossary.html#term-set_params) or [get_params](https://scikit-learn.org/stable/glossary.html#term-get_params). Parameter validation may be performed in `__init__`.

cross-validation estimator[#](https://scikit-learn.org/stable/glossary.html#term-cross-validation-estimator "Link to this term")

An estimator that has built-in cross-validation capabilities to automatically select the best hyper-parameters (see the [User Guide](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)). Some example of cross-validation estimators are [`ElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV") and [`LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV"). Cross-validation estimators are named `EstimatorCV` and tend to be roughly equivalent to `GridSearchCV(Estimator(), ...)`. The advantage of using a cross-validation estimator over the canonical [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator) class along with [grid search](https://scikit-learn.org/stable/modules/grid_search.html#grid-search) is that they can take advantage of warm-starting by reusing precomputed results in the previous steps of the cross-validation process. This generally leads to speed improvements. An exception is the [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV") class, which can instead perform efficient Leave-One-Out (LOO) CV. By default, all these estimators, apart from [`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV") with an LOO-CV, will be refitted on the full training dataset after finding the best combination of hyper-parameters.

scorer[#](https://scikit-learn.org/stable/glossary.html#term-scorer "Link to this term")

A non-estimator callable object which evaluates an estimator on given test data, returning a number. Unlike [evaluation metrics](https://scikit-learn.org/stable/glossary.html#term-evaluation-metrics), a greater returned number must correspond with a _better_ score. See [The scoring parameter: defining model evaluation rules](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter).
Further examples:
  * [`metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric")
  * [`gaussian_process.kernels.Kernel`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.kernels.Kernel.html#sklearn.gaussian_process.kernels.Kernel "sklearn.gaussian_process.kernels.Kernel")
  * `tree.Criterion`
