  * Efficiency [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor") with `criterion="absolute_error"` now runs much faster: O(n log n) complexity against previous O(n^2) allowing to scale to millions of data points, even hundred of millions. By
  * Fix Make [`tree.export_text`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_text.html#sklearn.tree.export_text "sklearn.tree.export_text") thread-safe. By
  * Fix [`export_graphviz`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html#sklearn.tree.export_graphviz "sklearn.tree.export_graphviz") now raises a `ValueError` if given feature names are not all strings. By
  * Fix [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor") with `criterion="absolute_error"` would sometimes make sub-optimal splits (i.e. splits that don’t minimize the absolute error). Now it’s fixed. Hence retraining trees might gives slightly different results. By
  * Fix Fixed a regression in [decision trees](https://scikit-learn.org/stable/modules/tree.html#tree) where almost constant features were not handled properly. By
  * Fix Fixed splitting logic during training in `tree.DecisionTree*` (and consequently in `ensemble.RandomForest*`) for nodes containing near-constant feature values and missing values. Beforehand, trees were cut short if a constant feature was found, even if there was more splitting that could be done on the basis of missing values. By
  * Fix Fix handling of missing values in method `decision_path` of trees ([`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier"), [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor"), [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier") and [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")) By
  * Fix Fix decision tree splitting with missing values present in some features. In some cases the last non-missing sample would not be partitioned correctly. By


###  [`sklearn.utils`](https://scikit-learn.org/stable/api/sklearn.utils.html#module-sklearn.utils "sklearn.utils")[#](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-utils "Link to this heading")
  * Efficiency The function [`sklearn.utils.extmath.safe_sparse_dot`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.extmath.safe_sparse_dot.html#sklearn.utils.extmath.safe_sparse_dot "sklearn.utils.extmath.safe_sparse_dot") was improved by a dedicated Cython routine for the case of `a @ b` with sparse 2-dimensional `a` and `b` and when a dense output is required, i.e., `dense_output=True`. This improves several algorithms in scikit-learn when dealing with sparse arrays (or matrices). By
  * Enhancement The parameter table in the HTML representation of all scikit-learn estimators and more generally of estimators inheriting from [`base.BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator "sklearn.base.BaseEstimator") now displays the parameter description as a tooltip and has a link to the online documentation for each parameter. By
  * Enhancement `sklearn.utils._check_sample_weight` now raises a clearer error message when the provided weights are neither a scalar nor a 1-D array-like of the same size as the input data. By
  * Enhancement [`sklearn.utils.estimator_checks.parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks") now lets you configure strict mode for xfailing checks. Tests that unexpectedly pass will lead to a test failure. The default behaviour is unchanged. By
  * Enhancement Fixed the alignment of the “?” and “i” symbols and improved the color style of the HTML representation of estimators. By
  * Fix Changes the way color are chosen when displaying an estimator as an HTML representation. Colors are not adapted anymore to the user’s theme, but chosen based on theme declared color scheme (light or dark) for VSCode and JupyterLab. If theme does not declare a color scheme, scheme is chosen according to default text color of the page, if it fails fallbacks to a media query. By
  * API Change `utils.extmath.stable_cumsum` is deprecated and will be removed in v1.10. Use `np.cumulative_sum` with the desired dtype directly instead. By


Code and documentation contributors
Thanks to everyone who has contributed to the maintenance and improvement of the project since version 1.7, including:
$id, 4hm3d, Acciaro Gennaro Daniele, achyuthan.s, Adam J. Stewart, Adriano Leão, Adrien Linares, Adrin Jalali, Aitsaid Azzedine Idir, Alexander Fabisch, Alexandre Abraham, Andrés H. Zapke, Anne Beyer, Anthony Gitter, AnthonyPrudent, antoinebaker, Arpan Mukherjee, Arthur, Arthur Lacote, Arturo Amor, ayoub.agouzoul, Ayrat, Ayush, Ayush Tanwar, Basile Jezequel, Bhavya Patwa, BRYANT MUSI BABILA, Casey Heath, Chems Ben, Christian Lorentzen, Christian Veenhuis, Christine P. Chai, cstec, C. Titus Brown, Daniel Herrera-Esposito, Dan Schult, dbXD320, Dea María Léon, Deepyaman Datta, dependabot[bot], Dhyey Findoriya, Dimitri Papadopoulos Orfanos, Dipak Dhangar, Dmitry Kobak, elenafillo, Elham Babaei, EmilyXinyi, Emily (Xinyi) Chen, Eugen-Bleck, Evgeni Burovski, fabarca, Fabrizio Damicelli, Faizan-Ul Huda, François Goupil, François Paugam, Gaetan, GaetandeCast, Gesa Loof, Gonçalo Guiomar, Gordon Grey, Gowtham Kumar K., Guilherme Peixoto, Guillaume Lemaitre, hakan çanakçı, Harshil Sanghvi, Henri Bonamy, Hleb Levitski, HulusiOzy, hvtruong, Ian Faust, Imad Saddik, Jérémie du Boisberranger, Jérôme Dockès, John Hendricks, Joris Van den Bossche, Josef Affourtit, Josh, jshn9515, Junaid, KALLA GANASEKHAR, Kapil Parekh, Kenneth Enevoldsen, Kian Eliasi, kostayScr, Krishnan Vignesh, kryggird, Kyle S, Lakshmi Krishnan, Leomax, Loic Esteve, Luca Bittarello, Lucas Colley, Lucy Liu, Luigi Giugliano, Luis, Mahdi Abid, Mahi Dhiman, Maitrey Talware, Mamduh Zabidi, Manikandan Gobalakrishnan, Marc Bresson, Marco Edward Gorelli, Marek Pokropiński, Maren Westermann, Marie Sacksick, Marija Vlajic, Matt J., Mayank Raj, Michael Burkhart, Michael Šimáček, Miguel Fernandes, Miro Hrončok, Mohamed DHIFALLAH, Muhammad Waseem, MUHAMMED SINAN D, Natalia Mokeeva, Nicholas Farr, Nicolas Bolle, Nicolas Hug, nithish-74, Nithurshen, Nitin Pratap Singh, NotAceNinja, Olivier Grisel, omahs, Omar Salman, Patrick Walsh, Peter Holzer, pfolch, ph-ll-pp, Prashant Bansal, Quan H. Nguyen, Radovenchyk, Rafael Ayllón Gavilán, Raghvender, Ranjodh Singh, Ravichandranayakar, Remi Gau, Reshama Shaikh, Richard Harris, RishiP2006, Ritvi Alagusankar, Roberto Mourao, Robert Pollak, Roshangoli, roychan, R Sagar Shresti, Sarthak Puri, saskra, scikit-learn-bot, Scott Huberty, Sercan Turkmen, Sergio P, Shashank S, Shaurya Bisht, Shivam, Shruti Nath, SIKAI ZHANG, sisird864, SiyuJin-1, S. M. Mohiuddin Khan Shiam, Somdutta Banerjee, sotagg, Sota Goto, Spencer Bradkin, Stefan, Stefanie Senger, Steffen Rehberg, Steven Hur, Success Moses, Sylvain Combettes, ThibaultDECO, Thomas J. Fan, Thomas Li, Thomas S., Tim Head, Tingwei Zhu, Tiziano Zito, TJ Norred, Username46786, Utsab Dahal, Vasanth K, Veghit, VirenPassi, Virgil Chan, Vivaan Nanavati, Xiao Yuan, xuzhang0327, Yaroslav Halchenko, Yaswanth Kumar, Zijun yi, zodchi94, Zubair Shakoor
[ previous Release History ](https://scikit-learn.org/stable/whats_new.html "previous page") [ next Version 1.7 ](https://scikit-learn.org/stable/whats_new/v1.7.html "next page")
On this page
  * [Version 1.8.0](https://scikit-learn.org/stable/whats_new/v1.8.html#version-1-8-0)
    * [Changes impacting many modules](https://scikit-learn.org/stable/whats_new/v1.8.html#changes-impacting-many-modules)
    * [Support for Array API](https://scikit-learn.org/stable/whats_new/v1.8.html#support-for-array-api)
    * [Metadata routing](https://scikit-learn.org/stable/whats_new/v1.8.html#metadata-routing)
    * [Free-threaded CPython 3.14 support](https://scikit-learn.org/stable/whats_new/v1.8.html#free-threaded-cpython-3-14-support)
    * [`sklearn.base`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-base)
    * [`sklearn.calibration`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-calibration)
    * [`sklearn.cluster`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-cluster)
    * [`sklearn.compose`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-compose)
    * [`sklearn.covariance`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-covariance)
    * [`sklearn.decomposition`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-decomposition)
    * [`sklearn.discriminant_analysis`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-discriminant-analysis)
    * [`sklearn.ensemble`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-ensemble)
    * [`sklearn.feature_selection`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-feature-selection)
    * [`sklearn.gaussian_process`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-gaussian-process)
    * [`sklearn.linear_model`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-linear-model)
    * [`sklearn.manifold`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-manifold)
    * [`sklearn.metrics`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-metrics)
    * [`sklearn.model_selection`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-model-selection)
    * [`sklearn.multiclass`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-multiclass)
    * [`sklearn.naive_bayes`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-naive-bayes)
    * [`sklearn.preprocessing`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-preprocessing)
    * [`sklearn.semi_supervised`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-semi-supervised)
    * [`sklearn.tree`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-tree)
    * [`sklearn.utils`](https://scikit-learn.org/stable/whats_new/v1.8.html#sklearn-utils)


### This Page
  * [Show Source](https://scikit-learn.org/stable/_sources/whats_new/v1.8.rst.txt)


© Copyright 2007 - 2025, scikit-learn developers (BSD License).
