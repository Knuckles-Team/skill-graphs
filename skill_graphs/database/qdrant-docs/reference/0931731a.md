#  [](https://qdrant.tech/documentation/concepts/indexing/#indexing)Indexing
A key feature of Qdrant is the effective combination of vector and traditional indexes. It is essential to have this because for vector search to work effectively with filters, having a vector index only is not enough. In simpler terms, a vector index speeds up vector search, and payload indexes speed up filtering.
The indexes in the segments exist independently, but the parameters of the indexes themselves are configured for the whole collection.
Not all segments automatically have indexes. Their necessity is determined by the [optimizer](https://qdrant.tech/documentation/concepts/optimizer/) settings and depends, as a rule, on the number of stored points.
