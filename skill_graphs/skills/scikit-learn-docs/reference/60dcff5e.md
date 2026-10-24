##  1.1.16. Polynomial regression: extending linear models with basis functions[#](https://scikit-learn.org/stable/modules/linear_model.html#polynomial-regression-extending-linear-models-with-basis-functions "Link to this heading")
One common pattern within machine learning is to use linear models trained on nonlinear functions of the data. This approach maintains the generally fast performance of linear methods, while allowing them to fit a much wider range of data.
Mathematical details[#](https://scikit-learn.org/stable/modules/linear_model.html#mathematical-details-7 "Link to this dropdown")
For example, a simple linear regression can be extended by constructing **polynomial features** from the coefficients. In the standard linear regression case, you might have a model that looks like this for two-dimensional data:
y^(w,x)=w0+w1x1+w2x2
If we want to fit a paraboloid to the data instead of a plane, we can combine the features in second-order polynomials, so that the model looks like this:
y^(w,x)=w0+w1x1+w2x2+w3x1x2+w4x12+w5x22
The (sometimes surprising) observation is that this is _still a linear model_ : to see this, imagine creating a new set of features
z=[x1,x2,x1x2,x12,x22]
With this re-labeling of the data, our problem can be written
y^(w,z)=w0+w1z1+w2z2+w3z3+w4z4+w5z5
We see that the resulting _polynomial regression_ is in the same class of linear models we considered above (i.e. the model is linear in w) and can be solved by the same techniques. By considering linear fits within a higher-dimensional space built with these basis functions, the model has the flexibility to fit a much broader range of data.
Here is an example of applying this idea to one-dimensional data, using polynomial features of varying degrees:
[![../_images/sphx_glr_plot_polynomial_interpolation_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_polynomial_interpolation_001.png) ](https://scikit-learn.org/stable/auto_examples/linear_model/plot_polynomial_interpolation.html)
This figure is created using the [`PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures") transformer, which transforms an input data matrix into a new data matrix of a given degree. It can be used as follows:
```
>>> from sklearn.preprocessing import PolynomialFeatures
>>> import numpy as np
>>> X = np.arange(6).reshape(3, 2)
>>> X
array([[0, 1],
       [2, 3],
       [4, 5]])
>>> poly = PolynomialFeatures(degree=2)
>>> poly.fit_transform(X)
array([[ 1.,  0.,  1.,  0.,  0.,  1.],
       [ 1.,  2.,  3.,  4.,  6.,  9.],
       [ 1.,  4.,  5., 16., 20., 25.]])

```
Copy to clipboard
The features of `X` have been transformed from [x1,x2] to [1,x1,x2,x12,x1x2,x22], and can now be used within any linear model.
This sort of preprocessing can be streamlined with the [Pipeline](https://scikit-learn.org/stable/modules/compose.html#pipeline) tools. A single object representing a simple polynomial regression can be created and used as follows:
```
>>> from sklearn.preprocessing import PolynomialFeatures
>>> from sklearn.linear_model import LinearRegression
>>> from sklearn.pipeline import Pipeline
>>> import numpy as np
>>> model = Pipeline([('poly', PolynomialFeatures(degree=3)),
...                   ('linear', LinearRegression(fit_intercept=False))])
>>> # fit to an order-3 polynomial data
>>> x = np.arange(5)
>>> y = 3 - 2 * x + x ** 2 - x ** 3
>>> model = model.fit(x[:, np.newaxis], y)
>>> model.named_steps['linear'].coef_
array([ 3., -2.,  1., -1.])

```
Copy to clipboard
The linear model trained on polynomial features is able to exactly recover the input polynomial coefficients.
In some cases it’s not necessary to include higher powers of any single feature, but only the so-called _interaction features_ that multiply together at most d distinct features. These can be gotten from [`PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html#sklearn.preprocessing.PolynomialFeatures "sklearn.preprocessing.PolynomialFeatures") with the setting `interaction_only=True`.
For example, when dealing with boolean features, xin=xi for all n and is therefore useless; but xixj represents the conjunction of two booleans. This way, we can solve the XOR problem with a linear classifier:
```
>>> from sklearn.linear_model import Perceptron
>>> from sklearn.preprocessing import PolynomialFeatures
>>> import numpy as np
>>> X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
>>> y = X[:, 0] ^ X[:, 1]
>>> y
array([0, 1, 1, 0])
>>> X = PolynomialFeatures(interaction_only=True).fit_transform(X).astype(int)
>>> X
array([[1, 0, 0, 0],
       [1, 0, 1, 0],
       [1, 1, 0, 0],
       [1, 1, 1, 1]])
>>> clf = Perceptron(fit_intercept=False, max_iter=10, tol=None,
...                  shuffle=False).fit(X, y)

```
Copy to clipboard
And the classifier “predictions” are perfect:
```
>>> clf.predict(X)
array([0, 1, 1, 0])
>>> clf.score(X, y)
1.0

```
Copy to clipboard
[ previous 1. Supervised learning ](https://scikit-learn.org/stable/supervised_learning.html "previous page") [ next 1.2. Linear and Quadratic Discriminant Analysis ](https://scikit-learn.org/stable/modules/lda_qda.html "next page")
On this page
  * [1.1.1. Ordinary Least Squares](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares)
    * [1.1.1.1. Non-Negative Least Squares](https://scikit-learn.org/stable/modules/linear_model.html#non-negative-least-squares)
    * [1.1.1.2. Ordinary Least Squares Complexity](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares-complexity)
  * [1.1.2. Ridge regression and classification](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification)
    * [1.1.2.1. Regression](https://scikit-learn.org/stable/modules/linear_model.html#regression)
    * [1.1.2.2. Classification](https://scikit-learn.org/stable/modules/linear_model.html#classification)
    * [1.1.2.3. Ridge Complexity](https://scikit-learn.org/stable/modules/linear_model.html#ridge-complexity)
    * [1.1.2.4. Setting the regularization parameter: leave-one-out Cross-Validation](https://scikit-learn.org/stable/modules/linear_model.html#setting-the-regularization-parameter-leave-one-out-cross-validation)
  * [1.1.3. Lasso](https://scikit-learn.org/stable/modules/linear_model.html#lasso)
    * [1.1.3.1. Coordinate Descent with Gap Safe Screening Rules](https://scikit-learn.org/stable/modules/linear_model.html#coordinate-descent-with-gap-safe-screening-rules)
    * [1.1.3.2. Setting regularization parameter](https://scikit-learn.org/stable/modules/linear_model.html#setting-regularization-parameter)
      * [1.1.3.2.1. Using cross-validation](https://scikit-learn.org/stable/modules/linear_model.html#using-cross-validation)
      * [1.1.3.2.2. Information-criteria based model selection](https://scikit-learn.org/stable/modules/linear_model.html#information-criteria-based-model-selection)
      * [1.1.3.2.3. AIC and BIC criteria](https://scikit-learn.org/stable/modules/linear_model.html#aic-and-bic-criteria)
      * [1.1.3.2.4. Comparison with the regularization parameter of SVM](https://scikit-learn.org/stable/modules/linear_model.html#comparison-with-the-regularization-parameter-of-svm)
  * [1.1.4. Multi-task Lasso](https://scikit-learn.org/stable/modules/linear_model.html#multi-task-lasso)
  * [1.1.5. Elastic-Net](https://scikit-learn.org/stable/modules/linear_model.html#elastic-net)
  * [1.1.6. Multi-task Elastic-Net](https://scikit-learn.org/stable/modules/linear_model.html#multi-task-elastic-net)
  * [1.1.7. Least Angle Regression](https://scikit-learn.org/stable/modules/linear_model.html#least-angle-regression)
  * [1.1.8. LARS Lasso](https://scikit-learn.org/stable/modules/linear_model.html#lars-lasso)
  * [1.1.9. Orthogonal Matching Pursuit (OMP)](https://scikit-learn.org/stable/modules/linear_model.html#orthogonal-matching-pursuit-omp)
  * [1.1.10. Bayesian Regression](https://scikit-learn.org/stable/modules/linear_model.html#bayesian-regression)
    * [1.1.10.1. Bayesian Ridge Regression](https://scikit-learn.org/stable/modules/linear_model.html#bayesian-ridge-regression)
    * [1.1.10.2. Automatic Relevance Determination - ARD](https://scikit-learn.org/stable/modules/linear_model.html#automatic-relevance-determination-ard)
  * [1.1.11. Logistic regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
    * [1.1.11.1. Binary Case](https://scikit-learn.org/stable/modules/linear_model.html#binary-case)
    * [1.1.11.2. Multinomial Case](https://scikit-learn.org/stable/modules/linear_model.html#multinomial-case)
    * [1.1.11.3. Solvers](https://scikit-learn.org/stable/modules/linear_model.html#solvers)
      * [1.1.11.3.1. Differences between solvers](https://scikit-learn.org/stable/modules/linear_model.html#differences-between-solvers)
  * [1.1.12. Generalized Linear Models](https://scikit-learn.org/stable/modules/linear_model.html#generalized-linear-models)
    * [1.1.12.1. Usage](https://scikit-learn.org/stable/modules/linear_model.html#usage)
  * [1.1.13. Stochastic Gradient Descent - SGD](https://scikit-learn.org/stable/modules/linear_model.html#stochastic-gradient-descent-sgd)
    * [1.1.13.1. Perceptron](https://scikit-learn.org/stable/modules/linear_model.html#perceptron)
    * [1.1.13.2. Passive Aggressive Algorithms](https://scikit-learn.org/stable/modules/linear_model.html#passive-aggressive-algorithms)
  * [1.1.14. Robustness regression: outliers and modeling errors](https://scikit-learn.org/stable/modules/linear_model.html#robustness-regression-outliers-and-modeling-errors)
    * [1.1.14.1. Different scenario and useful concepts](https://scikit-learn.org/stable/modules/linear_model.html#different-scenario-and-useful-concepts)
    * [1.1.14.2. RANSAC: RANdom SAmple Consensus](https://scikit-learn.org/stable/modules/linear_model.html#ransac-random-sample-consensus)
    * [1.1.14.3. Theil-Sen estimator: generalized-median-based estimator](https://scikit-learn.org/stable/modules/linear_model.html#theil-sen-estimator-generalized-median-based-estimator)
    * [1.1.14.4. Huber Regression](https://scikit-learn.org/stable/modules/linear_model.html#huber-regression)
  * [1.1.15. Quantile Regression](https://scikit-learn.org/stable/modules/linear_model.html#quantile-regression)
  * [1.1.16. Polynomial regression: extending linear models with basis functions](https://scikit-learn.org/stable/modules/linear_model.html#polynomial-regression-extending-linear-models-with-basis-functions)


### This Page
  * [Show Source](https://scikit-learn.org/stable/_sources/modules/linear_model.rst.txt)


© Copyright 2007 - 2025, scikit-learn developers (BSD License).
