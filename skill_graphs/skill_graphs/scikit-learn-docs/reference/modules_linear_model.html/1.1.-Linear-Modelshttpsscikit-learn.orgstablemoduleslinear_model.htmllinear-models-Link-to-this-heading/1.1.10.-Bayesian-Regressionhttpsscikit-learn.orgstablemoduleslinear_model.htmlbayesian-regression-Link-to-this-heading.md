##  1.1.10. Bayesian Regression[#](https://scikit-learn.org/stable/modules/linear_model.html#bayesian-regression "Link to this heading")
Bayesian regression techniques can be used to include regularization parameters in the estimation procedure: the regularization parameter is not set in a hard sense but tuned to the data at hand.
This can be done by introducing ℓ2 regularization used in [Ridge regression and classification](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression) is equivalent to finding a maximum a posteriori estimation under a Gaussian prior over the coefficients w with precision λ−1. Instead of setting `lambda` manually, it is possible to treat it as a random variable to be estimated from the data.
To obtain a fully probabilistic model, the output y is assumed to be Gaussian distributed around Xw:
p(y|X,w,α)=N(y|Xw,α−1)
where α is again treated as a random variable that is to be estimated from the data.
The advantages of Bayesian Regression are:
  * It adapts to the data at hand.
  * It can be used to include regularization parameters in the estimation procedure.


The disadvantages of Bayesian regression include:
  * Inference of the model can be time consuming.

References[#](https://scikit-learn.org/stable/modules/linear_model.html#references-6 "Link to this dropdown")
  * A good introduction to Bayesian methods is given in
  * Original Algorithm is detailed in the book


###  1.1.10.1. Bayesian Ridge Regression[#](https://scikit-learn.org/stable/modules/linear_model.html#bayesian-ridge-regression "Link to this heading")
[`BayesianRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html#sklearn.linear_model.BayesianRidge "sklearn.linear_model.BayesianRidge") estimates a probabilistic model of the regression problem as described above. The prior for the coefficient w is given by a spherical Gaussian:
p(w|λ)=N(w|0,λ−1Ip)
The priors over α and λ are chosen to be _Bayesian Ridge Regression_ , and is similar to the classical [`Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge").
The parameters w, α and λ are estimated jointly during the fit of the model, the regularization parameters α and λ being estimated by maximizing the _log marginal likelihood_. The scikit-learn implementation is based on the algorithm described in Appendix A of (Tipping, 2001) where the update of the parameters α and λ is done as suggested in (MacKay, 1992). The initial value of the maximization procedure can be set with the hyperparameters `alpha_init` and `lambda_init`.
There are four more hyperparameters, α1, α2, λ1 and λ2 of the gamma prior distributions over α and λ. These are usually chosen to be _non-informative_. By default α1=α2=λ1=λ2=10−6.
Bayesian Ridge Regression is used for regression:
```
>>> from sklearn import linear_model
>>> X = [[0., 0.], [1., 1.], [2., 2.], [3., 3.]]
>>> Y = [0., 1., 2., 3.]
>>> reg = linear_model.BayesianRidge()
>>> reg.fit(X, Y)
BayesianRidge()

```
Copy to clipboard
After being fitted, the model can then be used to predict new values:
```
>>> reg.predict([[1, 0.]])
array([0.50000013])

```
Copy to clipboard
The coefficients w of the model can be accessed:
```
>>> reg.coef_
array([0.49999993, 0.49999993])

```
Copy to clipboard
Due to the Bayesian framework, the weights found are slightly different from the ones found by [Ordinary Least Squares](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares). However, Bayesian Ridge Regression is more robust to ill-posed problems.
Examples
  * [Curve Fitting with Bayesian Ridge Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_bayesian_ridge_curvefit.html#sphx-glr-auto-examples-linear-model-plot-bayesian-ridge-curvefit-py)

References[#](https://scikit-learn.org/stable/modules/linear_model.html#references-7 "Link to this dropdown")
  * Section 3.3 in Christopher M. Bishop: Pattern Recognition and Machine Learning, 2006
  * David J. C. MacKay,
  * Michael E. Tipping,


###  1.1.10.2. Automatic Relevance Determination - ARD[#](https://scikit-learn.org/stable/modules/linear_model.html#automatic-relevance-determination-ard "Link to this heading")
The Automatic Relevance Determination (as being implemented in [`ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression")) is a kind of linear model which is very similar to the [Bayesian Ridge Regression](https://scikit-learn.org/stable/modules/linear_model.html#id15), but that leads to sparser coefficients w [[1]](https://scikit-learn.org/stable/modules/linear_model.html#id20) [[2]](https://scikit-learn.org/stable/modules/linear_model.html#id21).
[`ARDRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ARDRegression.html#sklearn.linear_model.ARDRegression "sklearn.linear_model.ARDRegression") poses a different prior over w: it drops the spherical Gaussian distribution for a centered elliptic Gaussian distribution. This means each coefficient wi can itself be drawn from a Gaussian distribution, centered on zero and with a precision λi:
p(w|λ)=N(w|0,A−1)
with A being a positive definite diagonal matrix and diag(A)=λ={λ1,...,λp}.
In contrast to the [Bayesian Ridge Regression](https://scikit-learn.org/stable/modules/linear_model.html#id15), each coordinate of wi has its own standard deviation 1λi. The prior over all λi is chosen to be the same gamma distribution given by the hyperparameters λ1 and λ2.
ARD is also known in the literature as _Sparse Bayesian Learning_ and _Relevance Vector Machine_ [[3]](https://scikit-learn.org/stable/modules/linear_model.html#id22) [[4]](https://scikit-learn.org/stable/modules/linear_model.html#id24).
See [Comparing Linear Bayesian Regressors](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ard.html#sphx-glr-auto-examples-linear-model-plot-ard-py) for a worked-out comparison between ARD and [Bayesian Ridge Regression](https://scikit-learn.org/stable/modules/linear_model.html#id15).
See [L1-based models for Sparse Signals](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_and_elasticnet.html#sphx-glr-auto-examples-linear-model-plot-lasso-and-elasticnet-py) for a comparison between various methods - Lasso, ARD and ElasticNet - on correlated data.
References
[[1](https://scikit-learn.org/stable/modules/linear_model.html#id16)]
Christopher M. Bishop: Pattern Recognition and Machine Learning, Chapter 7.2.1
[[2](https://scikit-learn.org/stable/modules/linear_model.html#id17)]
David Wipf and Srikantan Nagarajan:
[[3](https://scikit-learn.org/stable/modules/linear_model.html#id18)]
Michael E. Tipping:
[[4](https://scikit-learn.org/stable/modules/linear_model.html#id19)]
Tristan Fletcher:
