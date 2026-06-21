#  [](https://qdrant.tech/documentation/concepts/collections/#collections)Collections
A collection is a named set of points (vectors with a payload) among which you can search. The vector of each point within the same collection must have the same dimensionality and be compared by a single metric. [Named vectors](https://qdrant.tech/documentation/concepts/collections/#collection-with-multiple-vectors) can be used to have multiple vectors in a single point, each of which can have their own dimensionality and metric requirements.
Distance metrics are used to measure similarities among vectors. The choice of metric depends on the way vectors obtaining and, in particular, on the method of neural network encoder training.
Qdrant supports these most popular types of metrics:
  * Dot product: `Dot` -
  * Cosine similarity: `Cosine` -
  * Euclidean distance: `Euclid` -
  * Manhattan distance: `Manhattan` -

For search efficiency, Cosine similarity is implemented as dot-product over normalized vectors. Vectors are automatically normalized during upload
In addition to metrics and vector size, each collection uses its own set of parameters that controls collection optimization, index construction, and vacuum. These settings can be changed at any time by a corresponding request.
