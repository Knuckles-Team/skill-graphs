  * Enhancement [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array") now accepts `ensure_non_negative` to check for negative values in the passed array, until now only available through calling `utils.check_non_negative`. By
  * Enhancement [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator") and [`parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks") now check and fail if the classifier has the `tags.classifier_tags.multi_class = False` tag but does not fail on multi-class data. By
  * Enhancement [`utils.validation.check_is_fitted`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.validation.check_is_fitted.html#sklearn.utils.validation.check_is_fitted "sklearn.utils.validation.check_is_fitted") now passes on stateless estimators. An estimator can indicate it’s stateless by setting the `requires_fit` tag. See [Estimator Tags](https://scikit-learn.org/stable/developers/develop.html#estimator-tags) for more information. By
  * Enhancement Changes to [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator") and [`parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks").
    * [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator") introduces new arguments: `on_skip`, `on_fail`, and `callback` to control the behavior of the check runner. Refer to the API documentation for more details.
    * `generate_only=True` is deprecated in [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator"). Use [`estimator_checks_generator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.estimator_checks_generator.html#sklearn.utils.estimator_checks.estimator_checks_generator "sklearn.utils.estimator_checks.estimator_checks_generator") instead.
    * The `_xfail_checks` estimator tag is now removed, and now in order to indicate which tests are expected to fail, you can pass a dictionary to the [`check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator") as the `expected_failed_checks` parameter. Similarly, the `expected_failed_checks` parameter in [`parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks") can be used, which is a callable returning a dictionary of the form:
```
{
    "check_name": "reason to mark this check as xfail",
}

```
Copy to clipboard
By
  * Fix [`utils.estimator_checks.parametrize_with_checks`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.parametrize_with_checks.html#sklearn.utils.estimator_checks.parametrize_with_checks "sklearn.utils.estimator_checks.parametrize_with_checks") and [`utils.estimator_checks.check_estimator`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.estimator_checks.check_estimator.html#sklearn.utils.estimator_checks.check_estimator "sklearn.utils.estimator_checks.check_estimator") now support estimators that have `set_output` called on them. By
  * API Change The `assert_all_finite` parameter of functions [`utils.check_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_array.html#sklearn.utils.check_array "sklearn.utils.check_array"), [`utils.check_X_y`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.check_X_y.html#sklearn.utils.check_X_y "sklearn.utils.check_X_y"), [`utils.as_float_array`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.as_float_array.html#sklearn.utils.as_float_array "sklearn.utils.as_float_array") is renamed into `ensure_all_finite`. `force_all_finite` will be removed in 1.8. By
  * API Change `utils.estimator_checks.check_sample_weights_invariance` replaced by `utils.estimator_checks.check_sample_weight_equivalence_on_dense_data` which uses integer (including zero) weights and `utils.estimator_checks.check_sample_weight_equivalence_on_sparse_data` which does the same on sparse data. By
  * API Change Using `_estimator_type` to set the estimator type is deprecated. Inherit from [`ClassifierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.ClassifierMixin.html#sklearn.base.ClassifierMixin "sklearn.base.ClassifierMixin"), [`RegressorMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.RegressorMixin.html#sklearn.base.RegressorMixin "sklearn.base.RegressorMixin"), [`TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html#sklearn.base.TransformerMixin "sklearn.base.TransformerMixin"), or [`OutlierMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.OutlierMixin.html#sklearn.base.OutlierMixin "sklearn.base.OutlierMixin") instead. Alternatively, you can set `estimator_type` in [`Tags`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.Tags.html#sklearn.utils.Tags "sklearn.utils.Tags") in the `__sklearn_tags__` method. By


Code and documentation contributors
Thanks to everyone who has contributed to the maintenance and improvement of the project since version 1.5, including:
Aaron Schumacher, Abdulaziz Aloqeely, abhi-jha, Acciaro Gennaro Daniele, Adam J. Stewart, Adam Li, Adeel Hassan, Adeyemi Biola, Aditi Juneja, Adrin Jalali, Aisha, Akanksha Mhadolkar, Akihiro Kuno, Alberto Torres, alexqiao, Alihan Zihna, Aniruddha Saha, antoinebaker, Antony Lee, Anurag Varma, Arif Qodari, Arthur Courselle, ArthurDbrn, Arturo Amor, Aswathavicky, Audrey Flanders, aurelienmorgan, Austin, awwwyan, AyGeeEm, a.zy.lee, baggiponte, BlazeStorm001, bme-git, Boney Patel, brdav, Brigitta Sipőcz, Cailean Carter, Camille Troillard, Carlo Lemos, Christian Lorentzen, Christian Veenhuis, Christine P. Chai, claudio, Conrad Stevens, datarollhexasphericon, Davide Chicco, David Matthew Cherney, Dea María Léon, Deepak Saldanha, Deepyaman Datta, dependabot[bot], dinga92, Dmitry Kobak, Domenico, Drew Craeton, dymil, Edoardo Abati, EmilyXinyi, Eric Larson, Evelyn, fabianhenning, Farid “Freddie” Taba, Gael Varoquaux, Giorgio Angelotti, Hleb Levitski, Guillaume Lemaitre, Guntitat Sawadwuthikul, Haesun Park, Hanjun Kim, Henrique Caroço, hhchen1105, Hugo Boulenger, Ilya Komarov, Inessa Pawson, Ivan Pan, Ivan Wiryadi, Jaimin Chauhan, Jakob Bull, James Lamb, Janez Demšar, Jérémie du Boisberranger, Jérôme Dockès, Jirair Aroyan, João Morais, Joe Cainey, Joel Nothman, John Enblom, JorgeCardenas, Joseph Barbier, jpienaar-tuks, Julian Chan, K.Bharat Reddy, Kevin Doshi, Lars, Loic Esteve, Lucas Colley, Lucy Liu, lunovian, Marc Bresson, Marco Edward Gorelli, Marco Maggi, Marco Wolsza, Maren Westermann, MarieS-WiMLDS, Martin Helm, Mathew Shen, mathurinm, Matthew Feickert, Maxwell Liu, Meekail Zain, Michael Dawson, Miguel Cárdenas, m-maggi, mrastgoo, Natalia Mokeeva, Nathan Goldbaum, Nathan Orgera, nbrown-ScottLogic, Nikita Chistyakov, Nithish Bolleddula, Noam Keidar, NoPenguinsLand, Norbert Preining, notPlancha, Olivier Grisel, Omar Salman, ParsifalXu, Piotr, Priyank Shroff, Priyansh Gupta, Quentin Barthélemy, Rachit23110261, Rahil Parikh, raisadz, Rajath, renaissance0ne, Reshama Shaikh, Roberto Rosati, Robert Pollak, rwelsch427, Santiago Castro, Santiago M. Mola, scikit-learn-bot, sean moiselle, SHREEKANT VITTHAL NANDIYAWAR, Shruti Nath, Søren Bredlund Caspersen, Stefanie Senger, Stefano Gaspari, Steffen Schneider, Štěpán Sršeň, Sylvain Combettes, Tamara, Thomas, Thomas Gessey-Jones, Thomas J. Fan, Thomas Li, ThorbenMaa, Tialo, Tim Head, Tuhin Sharma, Tushar Parimi, Umberto Fasci, UV, vedpawar2254, Velislav Babatchev, Victoria Shevchenko, viktor765, Vince Carey, Virgil Chan, Wang Jiayi, Xiao Yuan, Xuefeng Xu, Yao Xiao, yareyaredesuyo, Zachary Vealey, Ziad Amerr
[ previous Version 1.7 ](https://scikit-learn.org/stable/whats_new/v1.7.html "previous page") [ next Version 1.5 ](https://scikit-learn.org/stable/whats_new/v1.5.html "next page")
On this page
  * [Version 1.6.1](https://scikit-learn.org/stable/whats_new/v1.6.html#version-1-6-1)
    * [Changed models](https://scikit-learn.org/stable/whats_new/v1.6.html#changed-models)
    * [Changes impacting many modules](https://scikit-learn.org/stable/whats_new/v1.6.html#changes-impacting-many-modules)
    * [`sklearn.metrics`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-metrics)
    * [`sklearn.model_selection`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-model-selection)
    * [`sklearn.tree`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-tree)
    * [`sklearn.utils`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-utils)
  * [Version 1.6.0](https://scikit-learn.org/stable/whats_new/v1.6.html#version-1-6-0)
    * [Changes impacting many modules](https://scikit-learn.org/stable/whats_new/v1.6.html#id1)
    * [Support for Array API](https://scikit-learn.org/stable/whats_new/v1.6.html#support-for-array-api)
    * [Metadata routing](https://scikit-learn.org/stable/whats_new/v1.6.html#metadata-routing)
    * [Dropping official support for PyPy](https://scikit-learn.org/stable/whats_new/v1.6.html#dropping-official-support-for-pypy)
    * [Dropping support for building with setuptools](https://scikit-learn.org/stable/whats_new/v1.6.html#dropping-support-for-building-with-setuptools)
    * [Free-threaded CPython 3.13 support](https://scikit-learn.org/stable/whats_new/v1.6.html#free-threaded-cpython-3-13-support)
    * [`sklearn.base`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-base)
    * [`sklearn.calibration`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-calibration)
    * [`sklearn.cluster`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-cluster)
    * [`sklearn.compose`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-compose)
    * [`sklearn.covariance`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-covariance)
    * [`sklearn.cross_decomposition`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-cross-decomposition)
    * [`sklearn.datasets`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-datasets)
    * [`sklearn.decomposition`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-decomposition)
    * [`sklearn.discriminant_analysis`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-discriminant-analysis)
    * [`sklearn.ensemble`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-ensemble)
    * [`sklearn.feature_extraction`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-feature-extraction)
    * [`sklearn.frozen`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-frozen)
    * [`sklearn.impute`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-impute)
    * [`sklearn.linear_model`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-linear-model)
    * [`sklearn.manifold`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-manifold)
    * [`sklearn.metrics`](https://scikit-learn.org/stable/whats_new/v1.6.html#id2)
    * [`sklearn.model_selection`](https://scikit-learn.org/stable/whats_new/v1.6.html#id3)
    * [`sklearn.neighbors`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-neighbors)
    * [`sklearn.neural_network`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-neural-network)
    * [`sklearn.pipeline`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-pipeline)
    * [`sklearn.preprocessing`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-preprocessing)
    * [`sklearn.semi_supervised`](https://scikit-learn.org/stable/whats_new/v1.6.html#sklearn-semi-supervised)
    * [`sklearn.tree`](https://scikit-learn.org/stable/whats_new/v1.6.html#id4)
    * [`sklearn.utils`](https://scikit-learn.org/stable/whats_new/v1.6.html#id5)


### This Page
  * [Show Source](https://scikit-learn.org/stable/_sources/whats_new/v1.6.rst.txt)


© Copyright 2007 - 2025, scikit-learn developers (BSD License).
