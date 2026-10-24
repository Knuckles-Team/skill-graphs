When working with sparse matrices, we assume that it is sparse for a good reason, and avoid writing code that densifies a user-provided sparse matrix, instead maintaining sparsity or raising an error if not possible (i.e. if an estimator does not / cannot support sparse matrices).

stateless[#](https://scikit-learn.org/stable/glossary.html#term-stateless "Link to this term")

An estimator is stateless if it does not store any information that is obtained during [fit](https://scikit-learn.org/stable/glossary.html#term-fit). This information can be either parameters learned during [fit](https://scikit-learn.org/stable/glossary.html#term-fit) or statistics computed from the training data. An estimator is stateless if it has no [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes) apart from ones set in `__init__`. Calling [fit](https://scikit-learn.org/stable/glossary.html#term-fit) for these estimators will only validate the public [attributes](https://scikit-learn.org/stable/glossary.html#term-attributes) passed in `__init__`.

supervised[#](https://scikit-learn.org/stable/glossary.html#term-supervised "Link to this term")


supervised learning[#](https://scikit-learn.org/stable/glossary.html#term-supervised-learning "Link to this term")

Learning where the expected prediction (label or ground truth) is available for each sample when [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting) the model, provided as [y](https://scikit-learn.org/stable/glossary.html#term-y). This is the approach taken in a [classifier](https://scikit-learn.org/stable/glossary.html#term-classifier) or [regressor](https://scikit-learn.org/stable/glossary.html#term-regressor) among other estimators.

target[#](https://scikit-learn.org/stable/glossary.html#term-target "Link to this term")


targets[#](https://scikit-learn.org/stable/glossary.html#term-targets "Link to this term")

The _dependent variable_ in [supervised](https://scikit-learn.org/stable/glossary.html#term-supervised) (and [semisupervised](https://scikit-learn.org/stable/glossary.html#term-semisupervised)) learning, passed as [y](https://scikit-learn.org/stable/glossary.html#term-y) to an estimator’s [fit](https://scikit-learn.org/stable/glossary.html#term-fit) method. Also known as _dependent variable_ , _outcome variable_ , _response variable_ , _ground truth_ or _label_. Scikit-learn works with targets that have minimal structure: a class from a finite set, a finite real-valued number, multiple classes, or multiple numbers. See [Target Types](https://scikit-learn.org/stable/glossary.html#glossary-target-types).

transduction[#](https://scikit-learn.org/stable/glossary.html#term-transduction "Link to this term")


transductive[#](https://scikit-learn.org/stable/glossary.html#term-transductive "Link to this term")

A transductive (contrasted with [inductive](https://scikit-learn.org/stable/glossary.html#term-inductive)) machine learning method is designed to model a specific dataset, but not to apply that model to unseen data. Examples include [`manifold.TSNE`](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE "sklearn.manifold.TSNE"), [`cluster.AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering "sklearn.cluster.AgglomerativeClustering") and [`neighbors.LocalOutlierFactor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html#sklearn.neighbors.LocalOutlierFactor "sklearn.neighbors.LocalOutlierFactor").

unlabeled[#](https://scikit-learn.org/stable/glossary.html#term-unlabeled "Link to this term")


unlabeled data[#](https://scikit-learn.org/stable/glossary.html#term-unlabeled-data "Link to this term")

Samples with an unknown ground truth when fitting; equivalently, [missing values](https://scikit-learn.org/stable/glossary.html#term-missing-values) in the [target](https://scikit-learn.org/stable/glossary.html#term-target). See also [semisupervised](https://scikit-learn.org/stable/glossary.html#term-semisupervised) and [unsupervised](https://scikit-learn.org/stable/glossary.html#term-unsupervised) learning.

unsupervised[#](https://scikit-learn.org/stable/glossary.html#term-unsupervised "Link to this term")


unsupervised learning[#](https://scikit-learn.org/stable/glossary.html#term-unsupervised-learning "Link to this term")

Learning where the expected prediction (label or ground truth) is not available for each sample when [fitting](https://scikit-learn.org/stable/glossary.html#term-fitting) the model, as in [clusterers](https://scikit-learn.org/stable/glossary.html#term-clusterers) and [outlier detectors](https://scikit-learn.org/stable/glossary.html#term-outlier-detectors). Unsupervised estimators ignore any [y](https://scikit-learn.org/stable/glossary.html#term-y) passed to [fit](https://scikit-learn.org/stable/glossary.html#term-fit).
