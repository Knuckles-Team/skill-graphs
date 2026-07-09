## Target Types[#](https://scikit-learn.org/stable/glossary.html#target-types "Link to this heading")

binary[#](https://scikit-learn.org/stable/glossary.html#term-binary "Link to this term")

A classification problem consisting of two classes. A binary target may be represented as for a [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass) problem but with only two labels. A binary decision function is represented as a 1d array.
Semantically, one class is often considered the “positive” class. Unless otherwise specified (e.g. using [pos_label](https://scikit-learn.org/stable/glossary.html#term-pos_label) in [evaluation metrics](https://scikit-learn.org/stable/glossary.html#term-evaluation-metrics)), we consider the class label with the greater value (numerically or lexicographically) as the positive class: of labels [0, 1], 1 is the positive class; of [1, 2], 2 is the positive class; of [‘no’, ‘yes’], ‘yes’ is the positive class; of [‘no’, ‘YES’], ‘no’ is the positive class. This affects the output of [decision_function](https://scikit-learn.org/stable/glossary.html#term-decision_function), for instance.
Note that a dataset sampled from a multiclass `y` or a continuous `y` may appear to be binary.
[`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target") will return ‘binary’ for binary input, or a similar array with only a single class present.

continuous[#](https://scikit-learn.org/stable/glossary.html#term-continuous "Link to this term")

A regression problem where each sample’s target is a finite floating point number represented as a 1-dimensional array of floats (or sometimes ints).
[`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target") will return ‘continuous’ for continuous input, but if the data is all integers, it will be identified as ‘multiclass’.

continuous multioutput[#](https://scikit-learn.org/stable/glossary.html#term-continuous-multioutput "Link to this term")


continuous multi-output[#](https://scikit-learn.org/stable/glossary.html#term-continuous-multi-output "Link to this term")


multioutput continuous[#](https://scikit-learn.org/stable/glossary.html#term-multioutput-continuous "Link to this term")


multi-output continuous[#](https://scikit-learn.org/stable/glossary.html#term-multi-output-continuous "Link to this term")

A regression problem where each sample’s target consists of `n_outputs` [outputs](https://scikit-learn.org/stable/glossary.html#term-outputs), each one a finite floating point number, for a fixed int `n_outputs > 1` in a particular dataset.
Continuous multioutput targets are represented as multiple [continuous](https://scikit-learn.org/stable/glossary.html#term-continuous) targets, horizontally stacked into an array of shape `(n_samples, n_outputs)`.
[`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target") will return ‘continuous-multioutput’ for continuous multioutput input, but if the data is all integers, it will be identified as ‘multiclass-multioutput’.

multiclass[#](https://scikit-learn.org/stable/glossary.html#term-multiclass "Link to this term")


multi-class[#](https://scikit-learn.org/stable/glossary.html#term-multi-class "Link to this term")

A classification problem consisting of more than two classes. A multiclass target may be represented as a 1-dimensional array of strings or integers. A 2d column vector of integers (i.e. a single output in [multioutput](https://scikit-learn.org/stable/glossary.html#term-multioutput) terms) is also accepted.
We do not officially support other orderable, hashable objects as class labels, even if estimators may happen to work when given classification targets of such type.
For semi-supervised classification, [unlabeled](https://scikit-learn.org/stable/glossary.html#term-unlabeled) samples should have the special label -1 in `y`.
Within scikit-learn, all estimators supporting binary classification also support multiclass classification, using One-vs-Rest by default.
A [`preprocessing.LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder") helps to canonicalize multiclass targets as integers.
[`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target") will return ‘multiclass’ for multiclass input. The user may also want to handle ‘binary’ input identically to ‘multiclass’.

multiclass multioutput[#](https://scikit-learn.org/stable/glossary.html#term-multiclass-multioutput "Link to this term")


multi-class multi-output[#](https://scikit-learn.org/stable/glossary.html#term-multi-class-multi-output "Link to this term")


multioutput multiclass[#](https://scikit-learn.org/stable/glossary.html#term-multioutput-multiclass "Link to this term")


multi-output multi-class[#](https://scikit-learn.org/stable/glossary.html#term-multi-output-multi-class "Link to this term")

A classification problem where each sample’s target consists of `n_outputs` [outputs](https://scikit-learn.org/stable/glossary.html#term-outputs), each a class label, for a fixed int `n_outputs > 1` in a particular dataset. Each output has a fixed set of available classes, and each sample is labeled with a class for each output. An output may be binary or multiclass, and in the case where all outputs are binary, the target is [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel).
Multiclass multioutput targets are represented as multiple [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass) targets, horizontally stacked into an array of shape `(n_samples, n_outputs)`.
Note: For simplicity, we may not always support string class labels for multiclass multioutput, and integer class labels should be used.
[`multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput") provides estimators which estimate multi-output problems using multiple single-output estimators. This may not fully account for dependencies among the different outputs, which methods natively handling the multioutput case (e.g. decision trees, nearest neighbors, neural networks) may do better.
[`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target") will return ‘multiclass-multioutput’ for multiclass multioutput input.

multilabel[#](https://scikit-learn.org/stable/glossary.html#term-multilabel "Link to this term")


multi-label[#](https://scikit-learn.org/stable/glossary.html#term-multi-label "Link to this term")

A [multiclass multioutput](https://scikit-learn.org/stable/glossary.html#term-multiclass-multioutput) target where each output is [binary](https://scikit-learn.org/stable/glossary.html#term-binary). This may be represented as a 2d (dense) array or sparse matrix of integers, such that each column is a separate binary target, where positive labels are indicated with 1 and negative labels are usually -1 or 0. Sparse multilabel targets are not supported everywhere that dense multilabel targets are supported.
Semantically, a multilabel target can be thought of as a set of labels for each sample. While not used internally, [`preprocessing.MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer") is provided as a utility to convert from a list of sets representation to a 2d array or sparse matrix. One-hot encoding a multiclass target with [`preprocessing.LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer") turns it into a multilabel problem.
[`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target") will return ‘multilabel-indicator’ for multilabel input, whether sparse or dense.

multioutput[#](https://scikit-learn.org/stable/glossary.html#term-multioutput "Link to this term")


multi-output[#](https://scikit-learn.org/stable/glossary.html#term-multi-output "Link to this term")

A target where each sample has multiple classification/regression labels. See [multiclass multioutput](https://scikit-learn.org/stable/glossary.html#term-multiclass-multioutput) and [continuous multioutput](https://scikit-learn.org/stable/glossary.html#term-continuous-multioutput). We do not currently support modelling mixed classification and regression targets.
