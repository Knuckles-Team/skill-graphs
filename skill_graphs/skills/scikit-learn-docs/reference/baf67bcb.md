##  1.1.2. Ridge regression and classification[#](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification "Link to this heading")
###  1.1.2.1. Regression[#](https://scikit-learn.org/stable/modules/linear_model.html#regression "Link to this heading")
[`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge") regression addresses some of the problems of [Ordinary Least Squares](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares) by imposing a penalty on the size of the coefficients. The ridge coefficients minimize a penalized residual sum of squares:
minw||Xw−y||22+α||w||22
The complexity parameter α≥0 controls the amount of shrinkage: the larger the value of α, the greater the amount of shrinkage and thus the coefficients become more robust to collinearity.
[![../_images/sphx_glr_plot_ridge_path_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_ridge_path_001.png) ](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html)
As with other linear models, [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge") will take in its `fit` method arrays `X`, `y` and will store the coefficients w of the linear model in its `coef_` member:
```
>>> from sklearn import linear_model
>>> reg = linear_model.Ridge(alpha=.5)
>>> reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
Ridge(alpha=0.5)
>>> reg.coef_
array([0.34545455, 0.34545455])
>>> reg.intercept_
np.float64(0.13636)

```
Copy to clipboard
Note that the class [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge") allows for the user to specify that the solver be automatically chosen by setting `solver="auto"`. When this option is specified, [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge") will choose between the `"lbfgs"`, `"cholesky"`, and `"sparse_cg"` solvers. [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge") will begin checking the conditions shown in the following table from top to bottom. If the condition is true, the corresponding solver is chosen.
**Solver** | **Condition**
---|---
‘lbfgs’ | The `positive=True` option is specified.
‘cholesky’ | The input array X is not sparse.
‘sparse_cg’ | None of the above conditions are fulfilled.
Examples
  * [Ordinary Least Squares and Ridge Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge.html#sphx-glr-auto-examples-linear-model-plot-ols-ridge-py)
  * [Plot Ridge coefficients as a function of the regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_path.html#sphx-glr-auto-examples-linear-model-plot-ridge-path-py)
  * [Common pitfalls in the interpretation of coefficients of linear models](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#sphx-glr-auto-examples-inspection-plot-linear-model-coefficient-interpretation-py)
  * [Ridge coefficients as a function of the L2 Regularization](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ridge_coeffs.html#sphx-glr-auto-examples-linear-model-plot-ridge-coeffs-py)


###  1.1.2.2. Classification[#](https://scikit-learn.org/stable/modules/linear_model.html#classification "Link to this heading")
The [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge") regressor has a classifier variant: [`RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier"). This classifier first converts binary targets to `{-1, 1}` and then treats the problem as a regression task, optimizing the same objective as above. The predicted class corresponds to the sign of the regressor’s prediction. For multiclass classification, the problem is treated as multi-output regression, and the predicted class corresponds to the output with the highest value.
It might seem questionable to use a (penalized) Least Squares loss to fit a classification model instead of the more traditional logistic or hinge losses. However, in practice, all those models can lead to similar cross-validation scores in terms of accuracy or precision/recall, while the penalized least squares loss used by the [`RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier") allows for a very different choice of the numerical solvers with distinct computational performance profiles.
The [`RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier") can be significantly faster than e.g. [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression") with a high number of classes because it can compute the projection matrix (XTX)−1XT only once.
This classifier is sometimes referred to as a
Examples
  * [Classification of text documents using sparse features](https://scikit-learn.org/stable/auto_examples/text/plot_document_classification_20newsgroups.html#sphx-glr-auto-examples-text-plot-document-classification-20newsgroups-py)


###  1.1.2.3. Ridge Complexity[#](https://scikit-learn.org/stable/modules/linear_model.html#ridge-complexity "Link to this heading")
This method has the same order of complexity as [Ordinary Least Squares](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares).
###  1.1.2.4. Setting the regularization parameter: leave-one-out Cross-Validation[#](https://scikit-learn.org/stable/modules/linear_model.html#setting-the-regularization-parameter-leave-one-out-cross-validation "Link to this heading")
[`RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV") and [`RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV") implement ridge regression/classification with built-in cross-validation of the alpha parameter. They work in the same way as [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV") except that it defaults to efficient Leave-One-Out [cross-validation](https://scikit-learn.org/stable/glossary.html#term-cross-validation). When using the default [cross-validation](https://scikit-learn.org/stable/glossary.html#term-cross-validation), alpha cannot be 0 due to the formulation used to calculate Leave-One-Out error. See [[RL2007]](https://scikit-learn.org/stable/modules/linear_model.html#rl2007) for details.
Usage example:
```
>>> import numpy as np
>>> from sklearn import linear_model
>>> reg = linear_model.RidgeCV(alphas=np.logspace(-6, 6, 13))
>>> reg.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
RidgeCV(alphas=array([1.e-06, 1.e-05, 1.e-04, 1.e-03, 1.e-02, 1.e-01, 1.e+00, 1.e+01,
      1.e+02, 1.e+03, 1.e+04, 1.e+05, 1.e+06]))
>>> reg.alpha_
np.float64(0.01)

```
Copy to clipboard
Specifying the value of the [cv](https://scikit-learn.org/stable/glossary.html#term-cv) attribute will trigger the use of cross-validation with [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV"), for example `cv=10` for 10-fold cross-validation, rather than Leave-One-Out Cross-Validation.
References[#](https://scikit-learn.org/stable/modules/linear_model.html#references "Link to this dropdown")
[[RL2007](https://scikit-learn.org/stable/modules/linear_model.html#id3)]
“Notes on Regularized Least Squares”, Rifkin & Lippert (
