## Metadata Routing[#](https://scikit-learn.org/stable/glossary.html#metadata-routing "Link to this heading")

consumer[#](https://scikit-learn.org/stable/glossary.html#term-consumer "Link to this term")

An object which consumes [metadata](https://scikit-learn.org/stable/glossary.html#term-metadata). This object is usually an [estimator](https://scikit-learn.org/stable/glossary.html#term-estimator), a [scorer](https://scikit-learn.org/stable/glossary.html#term-scorer), or a [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter). Consuming metadata means using it in calculations, e.g. using [sample_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight) to calculate a certain type of score. Being a consumer doesn’t mean that the object always receives a certain metadata, rather it means it can use it if it is provided.

metadata[#](https://scikit-learn.org/stable/glossary.html#term-metadata "Link to this term")

Data which is related to the given [X](https://scikit-learn.org/stable/glossary.html#term-X) and [y](https://scikit-learn.org/stable/glossary.html#term-y) data, but is not directly a part of the data, e.g. [sample_weight](https://scikit-learn.org/stable/glossary.html#term-sample_weight) or [groups](https://scikit-learn.org/stable/glossary.html#term-groups), and is passed along to different objects and methods, e.g. to a [scorer](https://scikit-learn.org/stable/glossary.html#term-scorer) or a [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter).

router[#](https://scikit-learn.org/stable/glossary.html#term-router "Link to this term")

An object which routes metadata to [consumers](https://scikit-learn.org/stable/glossary.html#term-consumer). This object is usually a [meta-estimator](https://scikit-learn.org/stable/glossary.html#term-meta-estimator), e.g. [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline "sklearn.pipeline.Pipeline") or [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV "sklearn.model_selection.GridSearchCV"). Some routers can also be a consumer. This happens for example when a meta-estimator uses the given [groups](https://scikit-learn.org/stable/glossary.html#term-groups), and it also passes it along to some of its sub-objects, such as a [CV splitter](https://scikit-learn.org/stable/glossary.html#term-CV-splitter).
Please refer to [Metadata Routing User Guide](https://scikit-learn.org/stable/metadata_routing.html#metadata-routing) for more information.
