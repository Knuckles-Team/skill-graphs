## Parameters[#](https://scikit-learn.org/stable/glossary.html#parameters "Link to this heading")
These common parameter names, specifically used in estimator construction (see concept [parameter](https://scikit-learn.org/stable/glossary.html#term-parameter)), sometimes also appear as parameters of functions or non-estimator constructors.

`class_weight`[#](https://scikit-learn.org/stable/glossary.html#term-class_weight "Link to this term")

Used to specify sample weights when fitting classifiers as a function of the [target](https://scikit-learn.org/stable/glossary.html#term-target) class. Where [sample_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight) is also supported and given, it is multiplied by the `class_weight` contribution. Similarly, where `class_weight` is used in a [multioutput](https://scikit-learn.org/stable/glossary.html#term-multioutput) (including [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)) tasks, the weights are multiplied across outputs (i.e. columns of `y`).
By default, all samples have equal weight such that classes are effectively weighted by their prevalence in the training data. This could be achieved explicitly with `class_weight={label1: 1, label2: 1, ...}` for all class labels.
More generally, `class_weight` is specified as a dict mapping class labels to weights (`{class_label: weight}`), such that each sample of the named class is given that weight.
`class_weight='balanced'` can be used to give all classes equal weight by giving each sample a weight inversely related to its class’s prevalence in the training data: `n_samples / (n_classes * np.bincount(y))`. Class weights will be used differently depending on the algorithm: for linear models (such as linear SVM or logistic regression), the class weights will alter the loss function by weighting the loss of each sample by its class weight. For tree-based algorithms, the class weights will be used for reweighting the splitting criterion. **Note** however that this rebalancing does not take the weight of samples in each class into account.
For multioutput classification, a list of dicts is used to specify weights for each output. For example, for four-class multilabel classification weights should be `[{0: 1, 1: 1}, {0: 1, 1: 5}, {0: 1, 1: 1}, {0: 1, 1: 1}]` instead of `[{1:1}, {2:5}, {3:1}, {4:1}]`.
The `class_weight` parameter is validated and interpreted with [`utils.class_weight.compute_class_weight`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.class_weight.compute_class_weight.html#sklearn.utils.class_weight.compute_class_weight "sklearn.utils.class_weight.compute_class_weight").

`cv`[#](https://scikit-learn.org/stable/glossary.html#term-cv "Link to this term")

Determines a cross validation splitting strategy, as used in cross-validation based routines. `cv` is also available in estimators such as [`multioutput.ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain") or [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV") which use the predictions of one estimator as training data for another, to not overfit the training supervision.
Possible inputs for `cv` are usually:
  * An integer, specifying the number of folds in K-fold cross validation. K-fold will be stratified over classes if the estimator is a classifier (determined by [`base.is_classifier`](https://scikit-learn.org/stable/modules/generated/sklearn.base.is_classifier.html#sklearn.base.is_classifier "sklearn.base.is_classifier")) and the [targets](https://scikit-learn.org/stable/glossary.html#term-targets) may represent a binary or multiclass (but not multioutput) classification problem (determined by [`utils.multiclass.type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")).
  * A [cross-validation splitter](https://scikit-learn.org/stable/glossary.html#term-cross-validation-splitter) instance. Refer to the [User Guide](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation) for splitters available within Scikit-learn.
  * An iterable yielding train/test splits.


With some exceptions (especially where not using cross validation at all is an option), the default is 5-fold.
`cv` values are validated and interpreted with [`model_selection.check_cv`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.check_cv.html#sklearn.model_selection.check_cv "sklearn.model_selection.check_cv").

`kernel`[#](https://scikit-learn.org/stable/glossary.html#term-kernel "Link to this term")

Specifies the kernel function to be used by Kernel Method algorithms. For example, the estimators [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC") and [`gaussian_process.GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier") both have a `kernel` parameter that takes the name of the kernel to use as string or a callable kernel function used to compute the kernel matrix. For more reference, see the [Kernel Approximation](https://scikit-learn.org/stable/modules/kernel_approximation.html#kernel-approximation) and the [Gaussian Processes](https://scikit-learn.org/stable/modules/gaussian_process.html#gaussian-process) user guides.

`max_iter`[#](https://scikit-learn.org/stable/glossary.html#term-max_iter "Link to this term")

For estimators involving iterative optimization, this determines the maximum number of iterations to be performed in [fit](https://scikit-learn.org/stable/glossary.html#term-fit). If `max_iter` iterations are run without convergence, a [`exceptions.ConvergenceWarning`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.ConvergenceWarning.html#sklearn.exceptions.ConvergenceWarning "sklearn.exceptions.ConvergenceWarning") should be raised. Note that the interpretation of “a single iteration” is inconsistent across estimators: some, but not all, use it to mean a single epoch (i.e. a pass over every sample in the data).

`memory`[#](https://scikit-learn.org/stable/glossary.html#term-memory "Link to this term")

Some estimators make use of `fit` is called again, those partial solutions have been memoized and can be reused.
A `memory` parameter can be specified as a string with a path to a directory, or a `cache` method) can be used.
`memory` values are validated and interpreted with [`utils.validation.check_memory`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_memory.html#sklearn.utils.validation.check_memory "sklearn.utils.validation.check_memory").

`metric`[#](https://scikit-learn.org/stable/glossary.html#term-metric "Link to this term")

As a parameter, this is the scheme for determining the distance between two data points. See [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances"). In practice, for some algorithms, an improper distance metric (one that does not obey the triangle inequality, such as Cosine Distance) may be used.
Note: Hierarchical clustering uses `affinity` with this meaning.
We also use _metric_ to refer to [evaluation metrics](https://scikit-learn.org/stable/glossary.html#term-evaluation-metrics), but avoid using this sense as a parameter name.

`n_components`[#](https://scikit-learn.org/stable/glossary.html#term-n_components "Link to this term")

The number of features which a [transformer](https://scikit-learn.org/stable/glossary.html#term-transformer) should transform the input into. See [components_](https://scikit-learn.org/stable/glossary.html#term-components_) for the special case of affine projection.

`n_iter_no_change`[#](https://scikit-learn.org/stable/glossary.html#term-n_iter_no_change "Link to this term")

Number of iterations with no improvement to wait before stopping the iterative procedure. This is also known as a _patience_ parameter. It is typically used with [early stopping](https://scikit-learn.org/stable/glossary.html#term-early-stopping) to avoid stopping too early.

`n_jobs`[#](https://scikit-learn.org/stable/glossary.html#term-n_jobs "Link to this term")

This parameter is used to specify how many concurrent processes or threads should be used for routines that are parallelized with [joblib](https://scikit-learn.org/stable/glossary.html#term-joblib).
`n_jobs` is an integer, specifying the maximum number of concurrently running workers. If 1 is given, no joblib parallelism is used at all, which is useful for debugging. If set to -1, all CPUs are used. For `n_jobs` below -1, (n_cpus + 1 + n_jobs) are used. For example with `n_jobs=-2`, all CPUs but one are used.
`n_jobs` is `None` by default, which means _unset_ ; it will generally be interpreted as `n_jobs=1`, unless the current
Note that even if `n_jobs=1`, low-level parallelism (via Numpy and OpenMP) might be used in some configuration.
For more details on the use of `joblib` and its interactions with scikit-learn, please refer to our [parallelism notes](https://scikit-learn.org/stable/computing/parallelism.html#parallelism).

`pos_label`[#](https://scikit-learn.org/stable/glossary.html#term-pos_label "Link to this term")

Value with which positive labels must be encoded in binary classification problems in which the positive class is not assumed. This value is typically required to compute asymmetric evaluation metrics such as precision and recall.

`random_state`[#](https://scikit-learn.org/stable/glossary.html#term-random_state "Link to this term")

Whenever randomization is part of a Scikit-learn algorithm, a `random_state` parameter may be provided to control the random number generator used. Note that the mere presence of `random_state` doesn’t mean that randomization is always used, as it may be dependent on another parameter, e.g. `shuffle`, being set.
The passed value will have an effect on the reproducibility of the results returned by the function ([fit](https://scikit-learn.org/stable/glossary.html#term-fit), [split](https://scikit-learn.org/stable/glossary.html#term-split), or any other function like [`k_means`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.k_means.html#sklearn.cluster.k_means "sklearn.cluster.k_means")). `random_state`’s value may be:

None (default)

Use the global random state instance from

An integer

Use a new random number generator seeded by the given integer. Using an int will produce the same results across different calls. However, it may be worthwhile checking that your results are stable across a number of different distinct random seeds. Popular integer random seeds are 0 and `[0, 2**32 - 1]`.

A

Use the provided random state, only affecting other users of that same random state instance. Calling the function multiple times will reuse the same instance, and will produce different results.
[`utils.check_random_state`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_random_state.html#sklearn.utils.check_random_state "sklearn.utils.check_random_state") is used internally to validate the input `random_state` and return a
For more details on how to control the randomness of scikit-learn objects and avoid common pitfalls, you may refer to [Controlling randomness](https://scikit-learn.org/stable/common_pitfalls.html#randomness).

`scoring`[#](https://scikit-learn.org/stable/glossary.html#term-scoring "Link to this term")

Depending on the object, can specify:
  * the score function to be maximized (usually by [cross validation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)),
  * the multiple score functions to be reported,
  * the score function to be used to check early stopping, or
  * for visualization related objects, the score function to output or plot


The score function can be a string accepted by [`metrics.get_scorer`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.get_scorer.html#sklearn.metrics.get_scorer "sklearn.metrics.get_scorer") or a callable [scorer](https://scikit-learn.org/stable/glossary.html#term-scorer), not to be confused with an [evaluation metric](https://scikit-learn.org/stable/glossary.html#term-evaluation-metric), as the latter have a more diverse API. `scoring` may also be set to None, in which case the estimator’s [score](https://scikit-learn.org/stable/glossary.html#term-score) method is used. See [The scoring parameter: defining model evaluation rules](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter) in the User Guide.
Where multiple metrics can be evaluated, `scoring` may be given either as a list of unique strings, a dictionary with names as keys and callables as values or a callable that returns a dictionary. Note that this does _not_ specify which score function is to be maximized, and another parameter such as `refit` may be used for this purpose.
The `scoring` parameter is validated and interpreted using [`metrics.check_scoring`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.check_scoring.html#sklearn.metrics.check_scoring "sklearn.metrics.check_scoring").

`verbose`[#](https://scikit-learn.org/stable/glossary.html#term-verbose "Link to this term")

Logging is not handled very consistently in Scikit-learn at present, but when it is provided as an option, the `verbose` parameter is usually available to choose no logging (set to False). Any True value should enable some logging, but larger integers (e.g. above 10) may be needed for full verbosity. Verbose logs are usually printed to Standard Output. Estimators should not produce any output on Standard Output with the default `verbose` setting.

`warm_start`[#](https://scikit-learn.org/stable/glossary.html#term-warm_start "Link to this term")

When fitting an estimator repeatedly on the same dataset, but for multiple parameter values (such as to find the value maximizing performance as in [grid search](https://scikit-learn.org/stable/modules/grid_search.html#grid-search)), it may be possible to reuse aspects of the model learned from the previous parameter value, saving time. When `warm_start` is true, the existing [fitted](https://scikit-learn.org/stable/glossary.html#term-fitted) model [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes) are used to initialize the new model in a subsequent call to [fit](https://scikit-learn.org/stable/glossary.html#term-fit).
Note that this is only applicable for some models and some parameters, and even some orders of parameter values. In general, there is an interaction between `warm_start` and the parameter controlling the number of iterations of the estimator.
For estimators imported from [`ensemble`](https://scikit-learn.org/stable/api/sklearn.ensemble.html#module-sklearn.ensemble "sklearn.ensemble"), `warm_start` will interact with `n_estimators` or `max_iter`. For these models, the number of iterations, reported via `len(estimators_)` or `n_iter_`, corresponds the total number of estimators/iterations learnt since the initialization of the model. Thus, if a model was already initialized with `N` estimators, and `fit` is called with `n_estimators` or `max_iter` set to `M`, the model will train `M - N` new estimators.
Other models, usually using gradient-based solvers, have a different behavior. They all expose a `max_iter` parameter. The reported `n_iter_` corresponds to the number of iterations done during the last call to `fit` and will be at most `max_iter`. Thus, we do not consider the state of the estimator since the initialization.
[partial_fit](https://scikit-learn.org/stable/glossary.html#term-partial_fit) also retains the model between calls, but differs: with `warm_start` the parameters change and the data is (more-or-less) constant across calls to `fit`; with `partial_fit`, the mini-batch of data changes and model parameters stay fixed.
There are cases where you want to use `warm_start` to fit on different, but closely related data. For example, one may initially fit to a subset of the data, then fine-tune the parameter search on the full dataset. For classification, all data in a sequence of `warm_start` calls to `fit` must include samples from each class.
