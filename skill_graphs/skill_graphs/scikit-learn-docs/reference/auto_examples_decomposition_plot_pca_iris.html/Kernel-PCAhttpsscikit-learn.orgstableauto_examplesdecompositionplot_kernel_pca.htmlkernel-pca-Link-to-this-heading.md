# Kernel PCA[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html#kernel-pca "Link to this heading")
This example shows the difference between the Principal Components Analysis ([`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")) and its kernelized version ([`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")).
On the one hand, we show that [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA") is able to find a projection of the data which linearly separates them while it is not the case with [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA").
Finally, we show that inverting this projection is an approximation with [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA"), while it is exact with [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA").
```
# Authors: The scikit-learn developers
# SPDX-License-Identifier: BSD-3-Clause

```
Copy to clipboard
## Projecting data: `PCA` vs. `KernelPCA`[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html#projecting-data-pca-vs-kernelpca "Link to this heading")
In this section, we show the advantages of using a kernel when projecting data using a Principal Component Analysis (PCA). We create a dataset made of two nested circles.
```
from sklearn.datasets import [make_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")
from sklearn.model_selection import [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")

X, y = [make_circles](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_circles.html#sklearn.datasets.make_circles "sklearn.datasets.make_circles")(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)
X_train, X_test, y_train, y_test = [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split "sklearn.model_selection.train_test_split")(X, y, stratify=y, random_state=0)

```
Copy to clipboard
Let’s have a quick first look at the generated dataset.
```
import matplotlib.pyplot as plt

_, (train_ax, test_ax) = (ncols=2, sharex=True, sharey=True, figsize=(8, 4))

train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
train_ax.set_ylabel("Feature #1")
train_ax.set_xlabel("Feature #0")
train_ax.set_title("Training data")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
test_ax.set_xlabel("Feature #0")
_ = test_ax.set_title("Testing data")

```
Copy to clipboard
![Training data, Testing data](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_pca_001.png)
The samples from each class cannot be linearly separated: there is no straight line that can split the samples of the inner set from the outer set.
Now, we will use PCA with and without a kernel to see what is the effect of using such a kernel. The kernel used here is a radial basis function (RBF) kernel.
```
from sklearn.decomposition import [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA"), [KernelPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")

pca = [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA")(n_components=2)
kernel_pca = [KernelPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA")(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_pca = pca.fit(X_train).transform(X_test)
X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)

```
Copy to clipboard
```
fig, (orig_data_ax, pca_proj_ax, kernel_pca_proj_ax) = (
    ncols=3, figsize=(14, 4)
)

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Testing data")

pca_proj_ax.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test)
pca_proj_ax.set_ylabel("Principal component #1")
pca_proj_ax.set_xlabel("Principal component #0")
pca_proj_ax.set_title("Projection of testing data\n using PCA")

kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("Principal component #1")
kernel_pca_proj_ax.set_xlabel("Principal component #0")
_ = kernel_pca_proj_ax.set_title("Projection of testing data\n using KernelPCA")

```
Copy to clipboard
![Testing data, Projection of testing data  using PCA, Projection of testing data  using KernelPCA](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_pca_002.png)
We recall that PCA transforms the data linearly. Intuitively, it means that the coordinate system will be centered, rescaled on each component with respected to its variance and finally be rotated. The obtained data from this transformation is isotropic and can now be projected on its _principal components_.
Thus, looking at the projection made using PCA (i.e. the middle figure), we see that there is no change regarding the scaling; indeed the data being two concentric circles centered in zero, the original data is already isotropic. However, we can see that the data have been rotated. As a conclusion, we see that such a projection would not help if define a linear classifier to distinguish samples from both classes.
Using a kernel allows to make a non-linear projection. Here, by using an RBF kernel, we expect that the projection will unfold the dataset while keeping approximately preserving the relative distances of pairs of data points that are close to one another in the original space.
We observe such behaviour in the figure on the right: the samples of a given class are closer to each other than the samples from the opposite class, untangling both sample sets. Now, we can use a linear classifier to separate the samples from the two classes.
## Projecting into the original feature space[#](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html#projecting-into-the-original-feature-space "Link to this heading")
One particularity to have in mind when using [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA") is related to the reconstruction (i.e. the back projection in the original feature space). With [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA"), the reconstruction will be exact if `n_components` is the same than the number of original features. This is the case in this example.
We can investigate if we get the original dataset when back projecting with [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA").
```
X_reconstructed_pca = pca.inverse_transform(pca.transform(X_test))
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(kernel_pca.transform(X_test))

```
Copy to clipboard
```
fig, (orig_data_ax, pca_back_proj_ax, kernel_pca_back_proj_ax) = (
    ncols=3, sharex=True, sharey=True, figsize=(13, 4)
)

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Original test data")

pca_back_proj_ax.scatter(X_reconstructed_pca[:, 0], X_reconstructed_pca[:, 1], c=y_test)
pca_back_proj_ax.set_xlabel("Feature #0")
pca_back_proj_ax.set_title("Reconstruction via PCA")

kernel_pca_back_proj_ax.scatter(
    X_reconstructed_kernel_pca[:, 0], X_reconstructed_kernel_pca[:, 1], c=y_test
)
kernel_pca_back_proj_ax.set_xlabel("Feature #0")
_ = kernel_pca_back_proj_ax.set_title("Reconstruction via KernelPCA")

```
Copy to clipboard
![Original test data, Reconstruction via PCA, Reconstruction via KernelPCA](https://scikit-learn.org/stable/_images/sphx_glr_plot_kernel_pca_003.png)
While we see a perfect reconstruction with [`PCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA "sklearn.decomposition.PCA") we observe a different result for [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA").
Indeed, [`inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA.inverse_transform "sklearn.decomposition.KernelPCA.inverse_transform") cannot rely on an analytical back-projection and thus an exact reconstruction. Instead, a [`KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge") is internally trained to learn a mapping from the kernalized PCA basis to the original feature space. This method therefore comes with an approximation introducing small differences when back projecting in the original feature space.
To improve the reconstruction using [`inverse_transform`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA.inverse_transform "sklearn.decomposition.KernelPCA.inverse_transform"), one can tune `alpha` in [`KernelPCA`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA "sklearn.decomposition.KernelPCA"), the regularization term which controls the reliance on the training data during the training of the mapping.
**Total running time of the script:** (0 minutes 0.539 seconds)
[![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo9.svg) ](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_kernel_pca.ipynb)
[`Download Jupyter notebook: plot_kernel_pca.ipynb`](https://scikit-learn.org/stable/_downloads/c0a901203201090b01ac6d929a31ce08/plot_kernel_pca.ipynb)
[`Download Python source code: plot_kernel_pca.py`](https://scikit-learn.org/stable/_downloads/023324c27491610e7c0ccff87c59abf9/plot_kernel_pca.py)
[`Download zipped: plot_kernel_pca.zip`](https://scikit-learn.org/stable/_downloads/cc6cb3aee22cfec68cced9928e78b9af/plot_kernel_pca.zip)
Related examples
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_digits_denoising_thumb.png)
[Image denoising using kernel PCA](https://scikit-learn.org/stable/auto_examples/applications/plot_digits_denoising.html)
Image denoising using kernel PCA
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_scaling_importance_thumb.png)
[Importance of Feature Scaling](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html)
Importance of Feature Scaling
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_pca_iris_thumb.png)
[Principal Component Analysis (PCA) on Iris Dataset](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html)
Principal Component Analysis (PCA) on Iris Dataset
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_incremental_pca_thumb.png)
[Incremental PCA](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html)
Incremental PCA
[ previous Incremental PCA ](https://scikit-learn.org/stable/auto_examples/decomposition/plot_incremental_pca.html "previous page") [ next Model selection with Probabilistic PCA and Factor Analysis (FA) ](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_fa_model_selection.html "next page")
On this page
  * [Projecting data: `PCA` vs. `KernelPCA`](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html#projecting-data-pca-vs-kernelpca)
  * [Projecting into the original feature space](https://scikit-learn.org/stable/auto_examples/decomposition/plot_kernel_pca.html#projecting-into-the-original-feature-space)


### This Page
  * [Show Source](https://scikit-learn.org/stable/_sources/auto_examples/decomposition/plot_kernel_pca.rst.txt)


[ Download source code ](https://scikit-learn.org/stable/_downloads/023324c27491610e7c0ccff87c59abf9/plot_kernel_pca.py)
[ Download Jupyter notebook ](https://scikit-learn.org/stable/_downloads/c0a901203201090b01ac6d929a31ce08/plot_kernel_pca.ipynb)
[ Download zipped ](https://scikit-learn.org/stable/_downloads/cc6cb3aee22cfec68cced9928e78b9af/plot_kernel_pca.zip)
[ ![Launch JupyterLite](https://scikit-learn.org/stable/_images/jupyterlite_badge_logo9.svg) ](https://scikit-learn.org/stable/lite/lab/index.html?path=auto_examples/decomposition/plot_kernel_pca.ipynb)
© Copyright 2007 - 2025, scikit-learn developers (BSD License).
