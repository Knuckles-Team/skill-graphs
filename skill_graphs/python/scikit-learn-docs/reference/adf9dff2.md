##  1.1.4. Multi-task Lasso[#](https://scikit-learn.org/stable/modules/linear_model.html#multi-task-lasso "Link to this heading")
The [`MultiTaskLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso") is a linear model that estimates sparse coefficients for multiple regression problems jointly: `y` is a 2D array, of shape `(n_samples, n_tasks)`. The constraint is that the selected features are the same for all the regression problems, also called tasks.
The following figure compares the location of the non-zero entries in the coefficient matrix W obtained with a simple Lasso or a MultiTaskLasso. The Lasso estimates yield scattered non-zeros while the non-zeros of the MultiTaskLasso are full columns.
**[![multi_task_lasso_1](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_task_lasso_support_001.png)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html)[![multi_task_lasso_2](https://scikit-learn.org/stable/_images/sphx_glr_plot_multi_task_lasso_support_002.png)](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html)**
**Fitting a time-series model, imposing that any active feature be active at all times.**
Examples
  * [Joint feature selection with multi-task Lasso](https://scikit-learn.org/stable/auto_examples/linear_model/plot_multi_task_lasso_support.html#sphx-glr-auto-examples-linear-model-plot-multi-task-lasso-support-py)

Mathematical details[#](https://scikit-learn.org/stable/modules/linear_model.html#mathematical-details-3 "Link to this dropdown")
Mathematically, it consists of a linear model trained with a mixed ℓ1 ℓ2-norm for regularization. The objective function to minimize is:
minW12nsamples||XW−Y||Fro2+α||W||21
where Fro indicates the Frobenius norm
||A||Fro=∑ijaij2
and ℓ1 ℓ2 reads
||A||21=∑i∑jaij2.
The implementation in the class [`MultiTaskLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso") uses coordinate descent as the algorithm to fit the coefficients.
