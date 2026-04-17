# Release Highlights for scikit-learn 1.8[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#release-highlights-for-scikit-learn-1-8 "Link to this heading")
We are pleased to announce the release of scikit-learn 1.8! Many bug fixes and improvements were added, as well as some key new features. Below we detail the highlights of this release. **For an exhaustive list of all the changes** , please refer to the [release notes](https://scikit-learn.org/stable/whats_new/v1.8.html#release-notes-1-8).
To install the latest version (with pip):
```
pip install --upgrade scikit-learn

```
Copy to clipboard
or with conda:
```
conda install -c conda-forge scikit-learn

```
Copy to clipboard
## Array API support (enables GPU computations)[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#array-api-support-enables-gpu-computations "Link to this heading")
The progressive adoption of the Python array API standard in scikit-learn means that PyTorch and CuPy input arrays are used directly. This means that in scikit-learn estimators and functions non-CPU devices, such as GPUs, can be used to perform the computation. As a result performance is improved and integration with these libraries is easier.
In scikit-learn 1.8, several estimators and functions have been updated to support array API compatible inputs, for example PyTorch tensors and CuPy arrays.
Array API support was added to the following estimators: [`preprocessing.StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler"), [`preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures"), [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV"), [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV"), [`mixture.GaussianMixture`](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture "sklearn.mixture.GaussianMixture") and [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV").
Array API support was also added to several metrics in [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics") module, see [Support for Array API-compatible inputs](https://scikit-learn.org/stable/modules/array_api.html#array-api-supported) for more details.
Please refer to the [array API support](https://scikit-learn.org/stable/modules/array_api.html#array-api) page for instructions to use scikit-learn with array API compatible libraries such as PyTorch or CuPy. Note: Array API support is experimental and must be explicitly enabled both in SciPy and scikit-learn.
Here is an excerpt of using a feature engineering preprocessor on the CPU, followed by [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV") and [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV") together on a GPU with the help of PyTorch:
```
ridge_pipeline_gpu = [make_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")(
    # Ensure that all features (including categorical features) are preprocessed
    # on the CPU and mapped to a numerical representation.
    feature_preprocessor,
    # Move the results to the GPU and perform computations there
    FunctionTransformer(
        lambda x: torch.tensor(x.to_numpy().astype(np.float32), device="cuda"))
    ,
    [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")(
        RidgeClassifierCV(alphas=alphas), method="temperature"
    ),
)
with sklearn.config_context(array_api_dispatch=True):
    cv_results = cross_validate(ridge_pipeline_gpu, features, target)

```
Copy to clipboard
See the
## Free-threaded CPython 3.14 support[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#free-threaded-cpython-3-14-support "Link to this heading")
scikit-learn has support for free-threaded CPython, in particular free-threaded wheels are available for all of our supported platforms on Python 3.14.
We would be very interested by user feedback. Here are a few things you can try:
  * install free-threaded CPython 3.14, run your favourite scikit-learn script and check that nothing breaks unexpectedly. Note that CPython 3.14 (rather than 3.13) is strongly advised because a number of free-threaded bugs have been fixed since CPython 3.13.
  * if you use some estimators with a `n_jobs` parameter, try changing the default backend to threading with `joblib.parallel_config` as in the snippet below. This could potentially speed-up your code because the default joblib backend is process-based and incurs more overhead than threads.
```
grid_search = GridSearchCV(clf, param_grid=param_grid, n_jobs=4)
with joblib.parallel_config(backend="threading"):
    grid_search.fit(X, y)

```
Copy to clipboard
  * don’t hesitate to report any issue or unexpected performance behaviour by opening a


Free-threaded (also known as nogil) CPython is a version of CPython that aims to enable efficient multi-threaded use cases by removing the Global Interpreter Lock (GIL).
For more details about free-threaded CPython see
In scikit-learn, one hope with free-threaded Python is to more efficiently leverage multi-core CPUs by using thread workers instead of subprocess workers for parallel computation when passing `n_jobs>1` in functions or estimators. Efficiency gains are expected by removing the need for inter-process communication. Be aware that switching the default joblib backend and testing that everything works well with free-threaded Python is an ongoing long-term effort.
## Temperature scaling in `CalibratedClassifierCV`[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#temperature-scaling-in-calibratedclassifiercv "Link to this heading")
Probability calibration of classifiers with temperature scaling is available in [`calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV") by setting `method="temperature"`. This method is particularly well suited for multiclass problems because it provides (better) calibrated probabilities with a single free parameter. This is in contrast to all the other available calibrations methods which use a “One-vs-Rest” scheme that adds more parameters for each class.
```
from sklearn.calibration import [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")
from sklearn.datasets import [make_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")
from sklearn.naive_bayes import [GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")

X, y = [make_classification](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html#sklearn.datasets.make_classification "sklearn.datasets.make_classification")(n_classes=3, n_informative=8, random_state=42)
clf = [GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")().fit(X, y)
sig = [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")(clf, method="sigmoid", ensemble=False).fit(X, y)
ts = [CalibratedClassifierCV](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html#sklearn.calibration.CalibratedClassifierCV "sklearn.calibration.CalibratedClassifierCV")(clf, method="temperature", ensemble=False).fit(X, y)

```
Copy to clipboard
The following example shows that temperature scaling can produce better calibrated probabilities than sigmoid calibration in multi-class classification problem with 3 classes.
```
import matplotlib.pyplot as plt

from sklearn.calibration import CalibrationDisplay

fig, axes = (
    figsize=(8, 4.5),
    ncols=3,
    sharey=True,
)
for i, c in enumerate(ts.classes_):
    [CalibrationDisplay.from_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_predictions "sklearn.calibration.CalibrationDisplay.from_predictions")(
        y == c, clf.predict_proba(X)[:, i], name="Uncalibrated", ax=axes[i], marker="s"
    )
    [CalibrationDisplay.from_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_predictions "sklearn.calibration.CalibrationDisplay.from_predictions")(
        y == c,
        ts.predict_proba(X)[:, i],
        name="Temperature scaling",
        ax=axes[i],
        marker="o",
    )
    [CalibrationDisplay.from_predictions](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibrationDisplay.html#sklearn.calibration.CalibrationDisplay.from_predictions "sklearn.calibration.CalibrationDisplay.from_predictions")(
        y == c, sig.predict_proba(X)[:, i], name="Sigmoid", ax=axes[i], marker="v"
    )
    axes[i].set_title(f"Class {c}")
    axes[i].set_xlabel(None)
    axes[i].set_ylabel(None)
    axes[i].get_legend().remove()
fig.suptitle("Reliability Diagrams per Class")
fig.supxlabel("Mean Predicted Probability")
fig.supylabel("Fraction of Class")
fig.legend(*axes[0].get_legend_handles_labels(), loc=(0.72, 0.5))
(right=0.7)
_ = fig.show()

```
Copy to clipboard
![Reliability Diagrams per Class, Class 0, Class 1, Class 2](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_8_0_001.png)
## Efficiency improvements in linear models[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#efficiency-improvements-in-linear-models "Link to this heading")
The fit time has been massively reduced for squared error based estimators with L1 penalty: `ElasticNet`, `Lasso`, `MultiTaskElasticNet`, `MultiTaskLasso` and their CV variants. The fit time improvement is mainly achieved by **gap safe screening rules**. They enable the coordinate descent solver to set feature coefficients to zero early on and not look at them again. The stronger the L1 penalty the earlier features can be excluded from further updates.
```
from time import from sklearn.datasets import [make_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
from sklearn.linear_model import [ElasticNetCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")

X, y = [make_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")(n_features=10_000, random_state=0)
model = [ElasticNetCV](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNetCV.html#sklearn.linear_model.ElasticNetCV "sklearn.linear_model.ElasticNetCV")()
tic = ()
model.fit(X, y)
toc = ()
print(f"Fitting ElasticNetCV took {toc - tic:.3} seconds.")

```
Copy to clipboard
```
Fitting ElasticNetCV took 16.8 seconds.

```
Copy to clipboard
## HTML representation of estimators[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#html-representation-of-estimators "Link to this heading")
Hyperparameters in the dropdown table of the HTML representation now include links to the online documentation. Docstring descriptions are also shown as tooltips on hover.
```
from sklearn.linear_model import [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
from sklearn.pipeline import [make_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")
from sklearn.preprocessing import [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")

clf = [make_pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html#sklearn.pipeline.make_pipeline "sklearn.pipeline.make_pipeline")([StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler "sklearn.preprocessing.StandardScaler")(), [LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")(random_state=0, C=10))

```
Copy to clipboard
Expand the estimator diagram below by clicking on “LogisticRegression” and then on “Parameters”.
```
clf

```
Copy to clipboard
```
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('logisticregression',
                 LogisticRegression(C=10, random_state=0))])
```
**In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.**
Pipeline
[?Documentation for Pipeline](https://scikit-learn.org/1.8/modules/generated/sklearn.pipeline.Pipeline.html)into fitted
Parameters |  [ steps steps: list of tuples

List of (name of step, estimator) tuples that are to be chained in
sequential order. To be compatible with the scikit-learn API, all steps
must define `fit`. All non-last steps must also define `transform`. See
:ref:`Combining Estimators ` for more details. ](https://scikit-learn.org/1.8/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=steps,-list%20of%20tuples) | [('standardscaler', ...), ('logisticregression', ...)]
---|---|---
|  [ transform_input transform_input: list of str, default=None

The names of the :term:`metadata` parameters that should be transformed by the
pipeline before passing it to the step consuming it.

This enables transforming some input arguments to ``fit`` (other than ``X``)
to be transformed by the steps of the pipeline up to the step which requires
them. Requirement is defined via :ref:`metadata routing `.
For instance, this can be used to pass a validation set through the pipeline.

You can only set this if metadata routing is enabled, which you
can enable using ``sklearn.set_config(enable_metadata_routing=True)``.

.. versionadded:: 1.6 ](https://scikit-learn.org/1.8/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=transform_input,-list%20of%20str%2C%20default%3DNone) | None
|  [ memory memory: str or object with the joblib.Memory interface, default=None

Used to cache the fitted transformers of the pipeline. The last step
will never be cached, even if it is a transformer. By default, no
caching is performed. If a string is given, it is the path to the
caching directory. Enabling caching triggers a clone of the transformers
before fitting. Therefore, the transformer instance given to the
pipeline cannot be inspected directly. Use the attribute ``named_steps``
or ``steps`` to inspect estimators within the pipeline. Caching the
transformers is advantageous when fitting is time consuming. See
:ref:`sphx_glr_auto_examples_neighbors_plot_caching_nearest_neighbors.py`
for an example on how to enable caching. ](https://scikit-learn.org/1.8/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=memory,-str%20or%20object%20with%20the%20joblib.Memory%20interface%2C%20default%3DNone) | None
|  [ verbose verbose: bool, default=False

If True, the time elapsed while fitting each step will be printed as it
is completed. ](https://scikit-learn.org/1.8/modules/generated/sklearn.pipeline.Pipeline.html#:~:text=verbose,-bool%2C%20default%3DFalse) | False
StandardScaler
[?Documentation for StandardScaler](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.StandardScaler.html)
Parameters |  [ copy copy: bool, default=True

If False, try to avoid a copy and do inplace scaling instead.
This is not guaranteed to always work inplace; e.g. if the data is
not a NumPy array or scipy.sparse CSR matrix, a copy may still be
returned. ](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=copy,-bool%2C%20default%3DTrue) | True
---|---|---
|  [ with_mean with_mean: bool, default=True

If True, center the data before scaling.
This does not work (and will raise an exception) when attempted on
sparse matrices, because centering them entails building a dense
matrix which in common use cases is likely to be too large to fit in
memory. ](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_mean,-bool%2C%20default%3DTrue) | True
|  [ with_std with_std: bool, default=True

If True, scale the data to unit variance (or equivalently,
unit standard deviation). ](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.StandardScaler.html#:~:text=with_std,-bool%2C%20default%3DTrue) | True
LogisticRegression
[?Documentation for LogisticRegression](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html)
Parameters |  [ penalty penalty: {'l1', 'l2', 'elasticnet', None}, default='l2'

Specify the norm of the penalty:

- `None`: no penalty is added;
- `'l2'`: add a L2 penalty term and it is the default choice;
- `'l1'`: add a L1 penalty term;
- `'elasticnet'`: both L1 and L2 penalty terms are added.

.. warning::
Some penalties may not work with some solvers. See the parameter
`solver` below, to know the compatibility between the penalty and
solver.

.. versionadded:: 0.19
l1 penalty with SAGA solver (allowing 'multinomial' + L1)

.. deprecated:: 1.8
`penalty` was deprecated in version 1.8 and will be removed in 1.10.
Use `l1_ratio` instead. `l1_ratio=0` for `penalty='l2'`, `l1_ratio=1` for
`penalty='l1'` and `l1_ratio` set to any float between 0 and 1 for
`'penalty='elasticnet'`. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=penalty,-%7B%27l1%27%2C%20%27l2%27%2C%20%27elasticnet%27%2C%20None%7D%2C%20default%3D%27l2%27) | 'deprecated'
---|---|---
|  [ C C: float, default=1.0

Inverse of regularization strength; must be a positive float.
Like in support vector machines, smaller values specify stronger
regularization. `C=np.inf` results in unpenalized logistic regression.
For a visual example on the effect of tuning the `C` parameter
with an L1 penalty, see:
:ref:`sphx_glr_auto_examples_linear_model_plot_logistic_path.py`. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=C,-float%2C%20default%3D1.0) | 10
|  [ l1_ratio l1_ratio: float, default=0.0

The Elastic-Net mixing parameter, with `0 <= l1_ratio <= 1`. Setting
`l1_ratio=1` gives a pure L1-penalty, setting `l1_ratio=0` a pure L2-penalty.
Any value between 0 and 1 gives an Elastic-Net penalty of the form
`l1_ratio * L1 + (1 - l1_ratio) * L2`.

.. warning::
Certain values of `l1_ratio`, i.e. some penalties, may not work with some
solvers. See the parameter `solver` below, to know the compatibility between
the penalty and solver.

.. versionchanged:: 1.8
Default value changed from None to 0.0.

.. deprecated:: 1.8
`None` is deprecated and will be removed in version 1.10. Always use
`l1_ratio` to specify the penalty type. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=l1_ratio,-float%2C%20default%3D0.0) | 0.0
|  [ dual dual: bool, default=False

Dual (constrained) or primal (regularized, see also
:ref:`this equation `) formulation. Dual formulation
is only implemented for l2 penalty with liblinear solver. Prefer `dual=False`
when n_samples > n_features. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=dual,-bool%2C%20default%3DFalse) | False
|  [ tol tol: float, default=1e-4

Tolerance for stopping criteria. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=tol,-float%2C%20default%3D1e-4) | 0.0001
|  [ fit_intercept fit_intercept: bool, default=True

Specifies if a constant (a.k.a. bias or intercept) should be
added to the decision function. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=fit_intercept,-bool%2C%20default%3DTrue) | True
|  [ intercept_scaling intercept_scaling: float, default=1

Useful only when the solver `liblinear` is used
and `self.fit_intercept` is set to `True`. In this case, `x` becomes
`[x, self.intercept_scaling]`,
i.e. a "synthetic" feature with constant value equal to
`intercept_scaling` is appended to the instance vector.
The intercept becomes
``intercept_scaling * synthetic_feature_weight``.

.. note::
The synthetic feature weight is subject to L1 or L2
regularization as all other features.
To lessen the effect of regularization on synthetic feature weight
(and therefore on the intercept) `intercept_scaling` has to be increased. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=intercept_scaling,-float%2C%20default%3D1) | 1
|  [ class_weight class_weight: dict or 'balanced', default=None

Weights associated with classes in the form ``{class_label: weight}``.
If not given, all classes are supposed to have weight one.

The "balanced" mode uses the values of y to automatically adjust
weights inversely proportional to class frequencies in the input data
as ``n_samples / (n_classes * np.bincount(y))``.

Note that these weights will be multiplied with sample_weight (passed
through the fit method) if sample_weight is specified.

.. versionadded:: 0.17
*class_weight='balanced'* ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=class_weight,-dict%20or%20%27balanced%27%2C%20default%3DNone) | None
|  [ random_state random_state: int, RandomState instance, default=None

Used when ``solver`` == 'sag', 'saga' or 'liblinear' to shuffle the
data. See :term:`Glossary ` for details. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=random_state,-int%2C%20RandomState%20instance%2C%20default%3DNone) | 0
|  [ solver solver: {'lbfgs', 'liblinear', 'newton-cg', 'newton-cholesky', 'sag', 'saga'}, default='lbfgs'

Algorithm to use in the optimization problem. Default is 'lbfgs'.
To choose a solver, you might want to consider the following aspects:

- 'lbfgs' is a good default solver because it works reasonably well for a wide
class of problems.
- For :term:`multiclass` problems (`n_classes >= 3`), all solvers except
'liblinear' minimize the full multinomial loss, 'liblinear' will raise an
error.
- 'newton-cholesky' is a good choice for
`n_samples` >> `n_features * n_classes`, especially with one-hot encoded
categorical features with rare categories. Be aware that the memory usage
of this solver has a quadratic dependency on `n_features * n_classes`
because it explicitly computes the full Hessian matrix.
- For small datasets, 'liblinear' is a good choice, whereas 'sag'
and 'saga' are faster for large ones;
- 'liblinear' can only handle binary classification by default. To apply a
one-versus-rest scheme for the multiclass setting one can wrap it with the
:class:`~sklearn.multiclass.OneVsRestClassifier`.

.. warning::
The choice of the algorithm depends on the penalty chosen (`l1_ratio=0`
for L2-penalty, `l1_ratio=1` for L1-penalty and `0 < l1_ratio < 1` for
Elastic-Net) and on (multinomial) multiclass support:

================= ======================== ======================
solver l1_ratio multinomial multiclass
================= ======================== ======================
'lbfgs' l1_ratio=0 yes
'liblinear' l1_ratio=1 or l1_ratio=0 no
'newton-cg' l1_ratio=0 yes
'newton-cholesky' l1_ratio=0 yes
'sag' l1_ratio=0 yes
'saga' 0<=l1_ratio<=1 yes
================= ======================== ======================

.. note::
'sag' and 'saga' fast convergence is only guaranteed on features
with approximately the same scale. You can preprocess the data with
a scaler from :mod:`sklearn.preprocessing`.

.. seealso::
Refer to the :ref:`User Guide ` for more
information regarding :class:`LogisticRegression` and more specifically the
:ref:`Table `
summarizing solver/penalty supports.

.. versionadded:: 0.17
Stochastic Average Gradient (SAG) descent solver. Multinomial support in
version 0.18.
.. versionadded:: 0.19
SAGA solver.
.. versionchanged:: 0.22
The default solver changed from 'liblinear' to 'lbfgs' in 0.22.
.. versionadded:: 1.2
newton-cholesky solver. Multinomial support in version 1.6. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=solver,-%7B%27lbfgs%27%2C%20%27liblinear%27%2C%20%27newton-cg%27%2C%20%27newton-cholesky%27%2C%20%27sag%27%2C%20%27saga%27%7D%2C%20%20%20%20%20%20%20%20%20%20%20%20%20default%3D%27lbfgs%27) | 'lbfgs'
|  [ max_iter max_iter: int, default=100

Maximum number of iterations taken for the solvers to converge. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=max_iter,-int%2C%20default%3D100) | 100
|  [ verbose verbose: int, default=0

For the liblinear and lbfgs solvers set verbose to any positive
number for verbosity. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=verbose,-int%2C%20default%3D0) | 0
|  [ warm_start warm_start: bool, default=False

When set to True, reuse the solution of the previous call to fit as
initialization, otherwise, just erase the previous solution.
Useless for liblinear solver. See :term:`the Glossary `.

.. versionadded:: 0.17
*warm_start* to support *lbfgs*, *newton-cg*, *sag*, *saga* solvers. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=warm_start,-bool%2C%20default%3DFalse) | False
|  [ n_jobs n_jobs: int, default=None

Does not have any effect.

.. deprecated:: 1.8
`n_jobs` is deprecated in version 1.8 and will be removed in 1.10. ](https://scikit-learn.org/1.8/modules/generated/sklearn.linear_model.LogisticRegression.html#:~:text=n_jobs,-int%2C%20default%3DNone) | None



## DecisionTreeRegressor with `criterion="absolute_error"`[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#decisiontreeregressor-with-criterion-absolute-error "Link to this heading")
[`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor") with `criterion="absolute_error"` now runs much faster. It has now `O(n * log(n))` complexity compared to `O(n**2)` previously, which allows to scale to millions of data points.
As an illustration, on a dataset with 100_000 samples and 1 feature, doing a single split takes of the order of 100 ms, compared to ~20 seconds before.
```
import time

from sklearn.datasets import [make_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")
from sklearn.tree import [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")

X, y = [make_regression](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_regression.html#sklearn.datasets.make_regression "sklearn.datasets.make_regression")(n_samples=100_000, n_features=1)
tree = [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")(criterion="absolute_error", max_depth=1)

tic = ()
tree.fit(X, y)
elapsed = () - tic
print(f"Fit took {elapsed:.2f} seconds")

```
Copy to clipboard
```
Fit took 0.17 seconds

```
Copy to clipboard
## ClassicalMDS[#](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#classicalmds "Link to this heading")
Classical MDS, also known as “Principal Coordinates Analysis” (PCoA) or “Torgerson’s scaling” is now available within the `sklearn.manifold` module. Classical MDS is close to PCA and instead of approximating distances, it approximates pairwise scalar products, which has an exact analytic solution in terms of eigendecomposition.
Let’s illustrate this new addition by using it on an S-curve dataset to get a low-dimensional representation of the data.
```
import matplotlib.pyplot as plt
from matplotlib import ticker

from sklearn import datasets, manifold

n_samples = 1500
S_points, S_color = [datasets.make_s_curve](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_s_curve.html#sklearn.datasets.make_s_curve "sklearn.datasets.make_s_curve")(n_samples, random_state=0)
md_classical = [manifold.ClassicalMDS](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.ClassicalMDS.html#sklearn.manifold.ClassicalMDS "sklearn.manifold.ClassicalMDS")(n_components=2)
S_scaling = md_classical.fit_transform(S_points)

fig = (figsize=(8, 4))
ax1 = fig.add_subplot(1, 2, 1, projection="3d")
x, y, z = S_points.T
ax1.scatter(x, y, z, c=S_color, s=50, alpha=0.8)
ax1.set_title("Original S-curve samples", size=16)
ax1.view_init(azim=-60, elev=9)
for axis in (ax1.xaxis, ax1.yaxis, ax1.zaxis):
    axis.set_major_locator((1))

ax2 = fig.add_subplot(1, 2, 2)
x2, y2 = S_scaling.T
ax2.scatter(x2, y2, c=S_color, s=50, alpha=0.8)
ax2.set_title("Classical MDS", size=16)
for axis in (ax2.xaxis, ax2.yaxis):
    axis.set_major_formatter(())

()

```
Copy to clipboard
![Original S-curve samples, Classical MDS](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_8_0_002.png)
**Total running time of the script:** (0 minutes 18.545 seconds)
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg) ](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_8_0.ipynb)
[`Download Jupyter notebook: plot_release_highlights_1_8_0.ipynb`](https://scikit-learn.org/stable/_downloads/826f1a05a1b6ad38fb98368f39e30aa6/plot_release_highlights_1_8_0.ipynb)
[`Download Python source code: plot_release_highlights_1_8_0.py`](https://scikit-learn.org/stable/_downloads/2f7d0c4f8bbd7c7e4062e34c1bffe66a/plot_release_highlights_1_8_0.py)
[`Download zipped: plot_release_highlights_1_8_0.zip`](https://scikit-learn.org/stable/_downloads/195570df7730e31327589be9e4984333/plot_release_highlights_1_8_0.zip)
Related examples
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_6_0_thumb.png)
[Release Highlights for scikit-learn 1.6](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_6_0.html)
Release Highlights for scikit-learn 1.6
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_7_0_thumb.png)
[Release Highlights for scikit-learn 1.7](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html)
Release Highlights for scikit-learn 1.7
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_0_0_thumb.png)
[Release Highlights for scikit-learn 1.0](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_0_0.html)
Release Highlights for scikit-learn 1.0
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_release_highlights_1_2_0_thumb.png)
[Release Highlights for scikit-learn 1.2](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_2_0.html)
Release Highlights for scikit-learn 1.2
[ previous Release Highlights ](https://scikit-learn.org/stable/auto_examples/release_highlights/index.html "previous page") [ next Release Highlights for scikit-learn 1.7 ](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_7_0.html "next page")
On this page
  * [Array API support (enables GPU computations)](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#array-api-support-enables-gpu-computations)
  * [Free-threaded CPython 3.14 support](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#free-threaded-cpython-3-14-support)
  * [Temperature scaling in `CalibratedClassifierCV`](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#temperature-scaling-in-calibratedclassifiercv)
  * [Efficiency improvements in linear models](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#efficiency-improvements-in-linear-models)
  * [HTML representation of estimators](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#html-representation-of-estimators)
  * [DecisionTreeRegressor with `criterion="absolute_error"`](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#decisiontreeregressor-with-criterion-absolute-error)
  * [ClassicalMDS](https://scikit-learn.org/stable/auto_examples/release_highlights/plot_release_highlights_1_8_0.html#classicalmds)


### This Page
  * [Show Source](https://scikit-learn.org/stable/_sources/auto_examples/release_highlights/plot_release_highlights_1_8_0.rst.txt)


[ Download source code ](https://scikit-learn.org/stable/_downloads/2f7d0c4f8bbd7c7e4062e34c1bffe66a/plot_release_highlights_1_8_0.py)
[ Download Jupyter notebook ](https://scikit-learn.org/stable/_downloads/826f1a05a1b6ad38fb98368f39e30aa6/plot_release_highlights_1_8_0.ipynb)
[ Download zipped ](https://scikit-learn.org/stable/_downloads/195570df7730e31327589be9e4984333/plot_release_highlights_1_8_0.zip)
[ ![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo28.svg) ](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/release_highlights/plot_release_highlights_1_8_0.ipynb)
© Copyright 2007 - 2025, scikit-learn developers (BSD License).
