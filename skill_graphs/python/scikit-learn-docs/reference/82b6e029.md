Some aspects of estimator tags are currently determined through the [duck typing](https://scikit-learn.org/stable/glossary.html#term-duck-typing) of methods like `predict_proba` and through some special attributes on estimator objects:
For more detailed info, see [Estimator Tags](https://scikit-learn.org/stable/developers/develop.html#estimator-tags).

feature[#](https://scikit-learn.org/stable/glossary.html#term-feature "Link to this term")


features[#](https://scikit-learn.org/stable/glossary.html#term-features "Link to this term")


feature vector[#](https://scikit-learn.org/stable/glossary.html#term-feature-vector "Link to this term")

In the abstract, a feature is a function (in its mathematical sense) mapping a sampled object to a numeric or categorical quantity. “Feature” is also commonly used to refer to these quantities, being the individual elements of a vector representing a sample. In a data matrix, features are represented as columns: each column contains the result of applying a feature function to a set of samples.
Elsewhere features are known as attributes, predictors, regressors, or independent variables.
Nearly all estimators in scikit-learn assume that features are numeric, finite and not missing, even when they have semantically distinct domains and distributions (categorical, ordinal, count-valued, real-valued, interval). See also [categorical feature](https://scikit-learn.org/stable/glossary.html#term-categorical-feature) and [missing values](https://scikit-learn.org/stable/glossary.html#term-missing-values).
`n_features` indicates the number of features in a dataset.

fitting[#](https://scikit-learn.org/stable/glossary.html#term-fitting "Link to this term")

Calling [fit](https://scikit-learn.org/stable/glossary.html#term-fit) (or [fit_transform](https://scikit-learn.org/stable/glossary.html#term-fit_transform), [fit_predict](https://scikit-learn.org/stable/glossary.html#term-fit_predict), etc.) on an estimator.

fitted[#](https://scikit-learn.org/stable/glossary.html#term-fitted "Link to this term")

The state of an estimator after [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting).
There is no conventional procedure for checking if an estimator is fitted. However, an estimator that is not fitted:
  * should raise [`exceptions.NotFittedError`](https://scikit-learn.org/stable/modules/generated/sklearn.exceptions.NotFittedError.html#sklearn.exceptions.NotFittedError "sklearn.exceptions.NotFittedError") when a prediction method ([predict](https://scikit-learn.org/stable/glossary.html#term-predict), [transform](https://scikit-learn.org/stable/glossary.html#term-transform), etc.) is called. ([`utils.validation.check_is_fitted`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted") is used internally for this purpose.)
  * should not have any [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes) beginning with an alphabetic character and ending with an underscore. (Note that a descriptor for the attribute may still be present on the class, but hasattr should return False)



function[#](https://scikit-learn.org/stable/glossary.html#term-function "Link to this term")

We provide ad hoc function interfaces for many algorithms, while [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator) classes provide a more consistent interface.
In particular, Scikit-learn may provide a function interface that fits a model to some data and returns the learnt model parameters, as in [`linear_model.enet_path`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.enet_path.html#sklearn.linear_model.enet_path "sklearn.linear_model.enet_path"). For transductive models, this also returns the embedding or cluster labels, as in [`manifold.spectral_embedding`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding "sklearn.manifold.spectral_embedding") or [`cluster.dbscan`](https://scikit-learn.org/stable/modules/generated/dbscan-function.html#sklearn.cluster.dbscan "sklearn.cluster.dbscan"). Many preprocessing transformers also provide a function interface, akin to calling [fit_transform](https://scikit-learn.org/stable/glossary.html#term-fit_transform), as in [`preprocessing.maxabs_scale`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.maxabs_scale.html#sklearn.preprocessing.maxabs_scale "sklearn.preprocessing.maxabs_scale"). Users should be careful to avoid [data leakage](https://scikit-learn.org/stable/glossary.html#term-data-leakage) when making use of these `fit_transform`-equivalent functions.
We do not have a strict policy about when to or when not to provide function forms of estimators, but maintainers should consider consistency with existing interfaces, and whether providing a function would lead users astray from best practices (as regards data leakage, etc.)

gallery[#](https://scikit-learn.org/stable/glossary.html#term-gallery "Link to this term")

See [examples](https://scikit-learn.org/stable/glossary.html#term-examples).

hyperparameter[#](https://scikit-learn.org/stable/glossary.html#term-hyperparameter "Link to this term")


hyper-parameter[#](https://scikit-learn.org/stable/glossary.html#term-hyper-parameter "Link to this term")

See [parameter](https://scikit-learn.org/stable/glossary.html#term-parameter).

impute[#](https://scikit-learn.org/stable/glossary.html#term-impute "Link to this term")


imputation[#](https://scikit-learn.org/stable/glossary.html#term-imputation "Link to this term")

Most machine learning algorithms require that their inputs have no [missing values](https://scikit-learn.org/stable/glossary.html#term-missing-values), and will not work if this requirement is violated. Algorithms that attempt to fill in (or impute) missing values are referred to as imputation algorithms.

indexable[#](https://scikit-learn.org/stable/glossary.html#term-indexable "Link to this term")

An [array-like](https://scikit-learn.org/stable/glossary.html#term-array-like), [sparse matrix](https://scikit-learn.org/stable/glossary.html#term-sparse-matrix), pandas DataFrame or sequence (usually a list).

induction[#](https://scikit-learn.org/stable/glossary.html#term-induction "Link to this term")


inductive[#](https://scikit-learn.org/stable/glossary.html#term-inductive "Link to this term")

Inductive (contrasted with [transductive](https://scikit-learn.org/stable/glossary.html#term-transductive)) machine learning builds a model of some data that can then be applied to new instances. Most estimators in Scikit-learn are inductive, having [predict](https://scikit-learn.org/stable/glossary.html#term-predict) and/or [transform](https://scikit-learn.org/stable/glossary.html#term-transform) methods.

joblib[#](https://scikit-learn.org/stable/glossary.html#term-joblib "Link to this term")

A Python library ([memory mapping](https://scikit-learn.org/stable/glossary.html#term-memory-mapping). See [Parallelism](https://scikit-learn.org/stable/computing/parallelism.html#parallelism) for more information.

label indicator matrix[#](https://scikit-learn.org/stable/glossary.html#term-label-indicator-matrix "Link to this term")


multilabel indicator matrix[#](https://scikit-learn.org/stable/glossary.html#term-multilabel-indicator-matrix "Link to this term")


multilabel indicator matrices[#](https://scikit-learn.org/stable/glossary.html#term-multilabel-indicator-matrices "Link to this term")

The format used to represent multilabel data, where each row of a 2d array or sparse matrix corresponds to a sample, each column corresponds to a class, and each element is 1 if the sample is labeled with the class and 0 if not.

leakage[#](https://scikit-learn.org/stable/glossary.html#term-leakage "Link to this term")


data leakage[#](https://scikit-learn.org/stable/glossary.html#term-data-leakage "Link to this term")

A problem in cross validation where generalization performance can be over-estimated since knowledge of the test data was inadvertently included in training a model. This is a risk, for instance, when applying a [transformer](https://scikit-learn.org/stable/glossary.html#term-transformer) to the entirety of a dataset rather than each training portion in a cross validation split.
We aim to provide interfaces (such as [`pipeline`](https://scikit-learn.org/stable/api/sklearn.pipeline.html#module-sklearn.pipeline "sklearn.pipeline") and [`model_selection`](https://scikit-learn.org/stable/api/sklearn.model_selection.html#module-sklearn.model_selection "sklearn.model_selection")) that shield the user from data leakage.

memmapping[#](https://scikit-learn.org/stable/glossary.html#term-memmapping "Link to this term")


memory map[#](https://scikit-learn.org/stable/glossary.html#term-memory-map "Link to this term")


memory mapping[#](https://scikit-learn.org/stable/glossary.html#term-memory-mapping "Link to this term")

A memory efficiency strategy that keeps data on disk rather than copying it into main memory. Memory maps can be created for arrays that can be read, written, or both, using [joblib](https://scikit-learn.org/stable/glossary.html#term-joblib) to parallelize operations in Scikit-learn, it may automatically memmap large arrays to reduce memory duplication overhead in multiprocessing.

missing values[#](https://scikit-learn.org/stable/glossary.html#term-missing-values "Link to this term")

Most Scikit-learn estimators do not work with missing values. When they do (e.g. in [`impute.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer "sklearn.impute.SimpleImputer")), NaN is the preferred representation of missing values in float arrays. If the array has integer dtype, NaN cannot be represented. For this reason, we support specifying another `missing_values` value when [imputation](https://scikit-learn.org/stable/glossary.html#term-imputation) or learning can be performed in integer space. [Unlabeled data](https://scikit-learn.org/stable/glossary.html#term-unlabeled-data) is a special case of missing values in the [target](https://scikit-learn.org/stable/glossary.html#term-target).

`n_features`[#](https://scikit-learn.org/stable/glossary.html#term-n_features "Link to this term")

The number of [features](https://scikit-learn.org/stable/glossary.html#term-features).

`n_outputs`[#](https://scikit-learn.org/stable/glossary.html#term-n_outputs "Link to this term")

The number of [outputs](https://scikit-learn.org/stable/glossary.html#term-outputs) in the [target](https://scikit-learn.org/stable/glossary.html#term-target).

`n_samples`[#](https://scikit-learn.org/stable/glossary.html#term-n_samples "Link to this term")

The number of [samples](https://scikit-learn.org/stable/glossary.html#term-samples).

`n_targets`[#](https://scikit-learn.org/stable/glossary.html#term-n_targets "Link to this term")

Synonym for [n_outputs](https://scikit-learn.org/stable/glossary.html#term-n_outputs).

narrative docs[#](https://scikit-learn.org/stable/glossary.html#term-narrative-docs "Link to this term")


narrative documentation[#](https://scikit-learn.org/stable/glossary.html#term-narrative-documentation "Link to this term")

An alias for [User Guide](https://scikit-learn.org/stable/user_guide.html#user-guide), i.e. documentation written in `doc/modules/`. Unlike the [API reference](https://scikit-learn.org/stable/api/index.html#api-ref) provided through docstrings, the User Guide aims to:
  * group tools provided by Scikit-learn together thematically or in terms of usage;
  * motivate why someone would use each particular tool, often through comparison;
  * provide both intuitive and technical descriptions of tools;
  * provide or link to [examples](https://scikit-learn.org/stable/glossary.html#term-examples) of using key features of a tool.



np[#](https://scikit-learn.org/stable/glossary.html#term-np "Link to this term")

A shorthand for Numpy due to the conventional import statement:
```
import numpy as np

```
Copy to clipboard

online learning[#](https://scikit-learn.org/stable/glossary.html#term-online-learning "Link to this term")

Where a model is iteratively updated by receiving each batch of ground truth [targets](https://scikit-learn.org/stable/glossary.html#term-targets) soon after making predictions on corresponding batch of data. Intrinsically, the model must be usable for prediction after each batch. See [partial_fit](https://scikit-learn.org/stable/glossary.html#term-partial_fit).

out-of-core[#](https://scikit-learn.org/stable/glossary.html#term-out-of-core "Link to this term")

An efficiency strategy where not all the data is stored in main memory at once, usually by performing learning on batches of data. See [partial_fit](https://scikit-learn.org/stable/glossary.html#term-partial_fit).

outputs[#](https://scikit-learn.org/stable/glossary.html#term-outputs "Link to this term")

Individual scalar/categorical variables per sample in the [target](https://scikit-learn.org/stable/glossary.html#term-target). For example, in multilabel classification each possible label corresponds to a binary output. Also called _responses_ , _tasks_ or _targets_. See [multiclass multioutput](https://scikit-learn.org/stable/glossary.html#term-multiclass-multioutput) and [continuous multioutput](https://scikit-learn.org/stable/glossary.html#term-continuous-multioutput).

pair[#](https://scikit-learn.org/stable/glossary.html#term-pair "Link to this term")

A tuple of length two.

parameter[#](https://scikit-learn.org/stable/glossary.html#term-parameter "Link to this term")


parameters[#](https://scikit-learn.org/stable/glossary.html#term-parameters "Link to this term")


param[#](https://scikit-learn.org/stable/glossary.html#term-param "Link to this term")


params[#](https://scikit-learn.org/stable/glossary.html#term-params "Link to this term")

We mostly use _parameter_ to refer to the aspects of an estimator that can be specified in its construction. For example, `max_depth` and `random_state` are parameters of [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier"). Parameters to an estimator’s constructor are stored unmodified as attributes on the estimator instance, and conventionally start with an alphabetic character and end with an alphanumeric character. Each estimator’s constructor parameters are described in the estimator’s docstring.
We do not use parameters in the statistical sense, where parameters are values that specify a model and can be estimated from data. What we call parameters might be what statisticians call hyperparameters to the model: aspects for configuring model structure that are often not directly learnt from data. However, our parameters are also used to prescribe modeling operations that do not affect the learnt model, such as [n_jobs](https://scikit-learn.org/stable/glossary.html#term-n_jobs) for controlling parallelism.
When talking about the parameters of a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator), we may also be including the parameters of the estimators wrapped by the meta-estimator. Ordinarily, these nested parameters are denoted by using a [double underscore](https://scikit-learn.org/stable/glossary.html#term-double-underscore) (`__`) to separate between the estimator-as-parameter and its parameter. Thus `clf = BaggingClassifier(estimator=DecisionTreeClassifier(max_depth=3))` has a deep parameter `estimator__max_depth` with value `3`, which is accessible with `clf.estimator.max_depth` or `clf.get_params()['estimator__max_depth']`.
The list of parameters and their current values can be retrieved from an [estimator instance](https://scikit-learn.org/stable/glossary.html#term-estimator-instance) using its [get_params](https://scikit-learn.org/stable/glossary.html#term-get_params) method.
Between construction and fitting, parameters may be modified using [set_params](https://scikit-learn.org/stable/glossary.html#term-set_params). To enable this, parameters are not ordinarily validated or altered when the estimator is constructed, or when each parameter is set. Parameter validation is performed when [fit](https://scikit-learn.org/stable/glossary.html#term-fit) is called.
Common parameters are listed [below](https://scikit-learn.org/stable/glossary.html#glossary-parameters).

pairwise metric[#](https://scikit-learn.org/stable/glossary.html#term-pairwise-metric "Link to this term")


pairwise metrics[#](https://scikit-learn.org/stable/glossary.html#term-pairwise-metrics "Link to this term")

In its broad sense, a pairwise metric defines a function for measuring similarity or dissimilarity between two samples (with each ordinarily represented as a [feature vector](https://scikit-learn.org/stable/glossary.html#term-feature-vector)). We particularly provide implementations of distance metrics (as well as improper metrics like Cosine Distance) through [`metrics.pairwise_distances`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances.html#sklearn.metrics.pairwise_distances "sklearn.metrics.pairwise_distances"), and of kernel functions (a constrained class of similarity functions) in [`metrics.pairwise.pairwise_kernels`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_kernels.html#sklearn.metrics.pairwise.pairwise_kernels "sklearn.metrics.pairwise.pairwise_kernels"). These can compute pairwise distance matrices that are symmetric and hence store data redundantly.
See also [precomputed](https://scikit-learn.org/stable/glossary.html#term-precomputed) and [metric](https://scikit-learn.org/stable/glossary.html#term-metric).
Note that for most distance metrics, we rely on implementations from [`metrics.DistanceMetric`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.DistanceMetric.html#sklearn.metrics.DistanceMetric "sklearn.metrics.DistanceMetric") interface is used to implement distance metrics for integration with efficient neighbors search.

pd[#](https://scikit-learn.org/stable/glossary.html#term-pd "Link to this term")

A shorthand for
```
import pandas as pd

```
Copy to clipboard

precomputed[#](https://scikit-learn.org/stable/glossary.html#term-precomputed "Link to this term")

Where algorithms rely on [pairwise metrics](https://scikit-learn.org/stable/glossary.html#term-pairwise-metrics), and can be computed from pairwise metrics alone, we often allow the user to specify that the [X](https://scikit-learn.org/stable/glossary.html#term-X) provided is already in the pairwise (dis)similarity space, rather than in a feature space. That is, when passed to [fit](https://scikit-learn.org/stable/glossary.html#term-fit), it is a square, symmetric matrix, with each vector indicating (dis)similarity to every sample, and when passed to prediction/transformation methods, each row corresponds to a testing sample and each column to a training sample.
Use of precomputed X is usually indicated by setting a `metric`, `affinity` or `kernel` parameter to the string ‘precomputed’. If this is the case, then the estimator should set the `pairwise` estimator tag as True.

rectangular[#](https://scikit-learn.org/stable/glossary.html#term-rectangular "Link to this term")

Data that can be represented as a matrix with [samples](https://scikit-learn.org/stable/glossary.html#term-samples) on the first axis and a fixed, finite set of [features](https://scikit-learn.org/stable/glossary.html#term-features) on the second is called rectangular.
This term excludes samples with non-vectorial structures, such as text, an image of arbitrary size, a time series of arbitrary length, a set of vectors, etc. The purpose of a [vectorizer](https://scikit-learn.org/stable/glossary.html#term-vectorizer) is to produce rectangular forms of such data.

sample[#](https://scikit-learn.org/stable/glossary.html#term-sample "Link to this term")


samples[#](https://scikit-learn.org/stable/glossary.html#term-samples "Link to this term")

We usually use this term as a noun to indicate a single feature vector. Elsewhere a sample is called an instance, data point, or observation. `n_samples` indicates the number of samples in a dataset, being the number of rows in a data array [X](https://scikit-learn.org/stable/glossary.html#term-X). Note that this definition is standard in machine learning and deviates from statistics where it means _a set of individuals or objects collected or selected_.

sample property[#](https://scikit-learn.org/stable/glossary.html#term-sample-property "Link to this term")


sample properties[#](https://scikit-learn.org/stable/glossary.html#term-sample-properties "Link to this term")

A sample property is data for each sample (e.g. an array of length n_samples) passed to an estimator method or a similar function, alongside but distinct from the [features](https://scikit-learn.org/stable/glossary.html#term-features) (`X`) and [target](https://scikit-learn.org/stable/glossary.html#term-target) (`y`). The most prominent example is [sample_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight); see others at [Data and sample properties](https://scikit-learn.org/stable/glossary.html#glossary-sample-props).
As of version 0.19 we do not have a consistent approach to handling sample properties and their routing in [meta-estimators](https://scikit-learn.org/stable/glossary.html#term-meta-estimators), though a `fit_params` parameter is often used.

scikit-learn-contrib[#](https://scikit-learn.org/stable/glossary.html#term-scikit-learn-contrib "Link to this term")

A venue for publishing Scikit-learn-compatible libraries that are broadly authorized by the core developers and the contrib community, but not maintained by the core developer team. See

scikit-learn enhancement proposals[#](https://scikit-learn.org/stable/glossary.html#term-scikit-learn-enhancement-proposals "Link to this term")


SLEP[#](https://scikit-learn.org/stable/glossary.html#term-SLEP "Link to this term")


SLEPs[#](https://scikit-learn.org/stable/glossary.html#term-SLEPs "Link to this term")

Changes to the API principles and changes to dependencies or supported versions happen via a [SLEP](https://scikit-learn.org/stable/governance.html#slep) and follows the decision-making process outlined in [Scikit-learn governance and decision-making](https://scikit-learn.org/stable/governance.html#governance). For all votes, a proposal must have been made public and discussed before the vote. Such a proposal must be a consolidated document, in the form of a “Scikit-Learn Enhancement Proposal” (SLEP), rather than a long discussion on an issue. A SLEP must be submitted as a pull-request to

semi-supervised[#](https://scikit-learn.org/stable/glossary.html#term-semi-supervised "Link to this term")


semi-supervised learning[#](https://scikit-learn.org/stable/glossary.html#term-semi-supervised-learning "Link to this term")


semisupervised[#](https://scikit-learn.org/stable/glossary.html#term-semisupervised "Link to this term")

Learning where the expected prediction (label or ground truth) is only available for some samples provided as training data when [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting) the model. We conventionally apply the label `-1` to [unlabeled](https://scikit-learn.org/stable/glossary.html#term-unlabeled) samples in semi-supervised classification.

sparse matrix[#](https://scikit-learn.org/stable/glossary.html#term-sparse-matrix "Link to this term")


sparse graph[#](https://scikit-learn.org/stable/glossary.html#term-sparse-graph "Link to this term")

A representation of two-dimensional numeric data that is more memory efficient than the corresponding dense numpy array where almost all elements are zero. We use the _formats_. Some formats are more efficient than others for particular tasks, and when a particular format provides especial benefit, we try to document this fact in Scikit-learn parameter descriptions.
Some sparse matrix formats (notably CSR, CSC, COUP and LIL) distinguish between _implicit_ and _explicit_ zeros. Explicit zeros are stored (i.e. they consume memory in a `data` array) in the data structure, while implicit zeros correspond to every element not otherwise defined in explicit storage.
Two semantics for sparse matrices are used in Scikit-learn:

matrix semantics

The sparse matrix is interpreted as an array with implicit and explicit zeros being interpreted as the number 0. This is the interpretation most often adopted, e.g. when sparse matrices are used for feature matrices or [multilabel indicator matrices](https://scikit-learn.org/stable/glossary.html#term-multilabel-indicator-matrices).

graph semantics

As with [`neighbors.kneighbors_graph`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.kneighbors_graph.html#sklearn.neighbors.kneighbors_graph "sklearn.neighbors.kneighbors_graph")), and for precomputed distance representation where only distances in the neighborhood of each point are required.
