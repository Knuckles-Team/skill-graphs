##  [](https://qdrant.tech/documentation/guides/quantization/#binary-quantization)Binary Quantization
_Available as of v1.5.0_
Binary quantization is an extreme case of scalar quantization. This feature lets you represent each vector component as a single bit, effectively reducing the memory footprint by a **factor of 32**.
This is the fastest quantization method, since it lets you perform a vector comparison with a few CPU instructions.
Binary quantization can achieve up to a **40x** speedup compared to the original vectors.
However, binary quantization is only efficient for high-dimensional vectors and require a centered distribution of vector components.
At the moment, binary quantization shows good accuracy results with the following models:
  * OpenAI `text-embedding-ada-002` - 1536d tested with
  * Cohere AI `embed-english-v2.0` - 4096d tested on Wikipedia embeddings - 0.98 recall@50 with 2x oversampling


Models with a lower dimensionality or a different distribution of vector components may require additional experiments to find the optimal quantization parameters.
We recommend using binary quantization only with rescoring enabled, as it can significantly improve the search quality with just a minor performance impact. Additionally, oversampling can be used to tune the tradeoff between search speed and search quality in the query time.
###  [](https://qdrant.tech/documentation/guides/quantization/#binary-quantization-as-hamming-distance)Binary Quantization as Hamming Distance
The additional benefit of this method is that you can efficiently emulate Hamming distance with dot product.
Specifically, if original vectors contain `{-1, 1}` as possible values, then the dot product of two vectors is equal to the Hamming distance by simply replacing `-1` with `0` and `1` with `1`.
**Sample truth table**
Vector 1 | Vector 2 | Dot product
---|---|---
1 | 1 | 1
1 | -1 | -1
-1 | 1 | -1
-1 | -1 | 1
Vector 1 | Vector 2 | Hamming distance
---|---|---
1 | 1 | 0
1 | 0 | 1
0 | 1 | 1
0 | 0 | 0
As you can see, both functions are equal up to a constant factor, which makes similarity search equivalent. Binary quantization makes it efficient to compare vectors using this representation.
###  [](https://qdrant.tech/documentation/guides/quantization/#15-bit-and-2-bit-quantization)1.5-Bit and 2-Bit Quantization
_Available as of v1.15.0_
**Binary quantization** storage can use **2 and 1.5 bits** per dimension, improving precision for smaller vectors. One-bit compression resulted in significant data loss and precision drops for vectors smaller than a thousand dimensions, often requiring expensive rescoring. 2-bit quantization offers 16X compression compared to 32X with one bit, improving performance for smaller vector dimensions. The 1.5-bit quantization compression offers 24X compression and intermediate accuracy.
A major limitation of binary quantization is poor handling of values close to zero. 2-bit quantization addresses this by explicitly representing zeros using an efficient scoring mechanism. In the case of 1.5-bit quantization, the zero-bit is shared between two values, balancing the efficiency of binary quantization with the accuracy improvements of 2-bit quantization, especially when 2-bit BQ requires too much memory.
In order to build 2-bit representation, Qdrant computes values distribution and then assigns bit values to 3 possible buckets:
  * `-1` - 00
  * `0` - 01
  * `1` - 11


1.5-bit quantization is similar, but merges buckets of pairs of elements into a binary triptets
![2-bit quantization](https://qdrant.tech/docs/2-bit-quantization.png)
2-bit quantization
See how to set up 1.5-bit and 2-bit quantization in the [following section](https://qdrant.tech/documentation/guides/quantization/#set-up-bit-depth).
###  [](https://qdrant.tech/documentation/guides/quantization/#asymmetric-quantization)Asymmetric Quantization
_Available as of v1.15.0_
The **Asymmetric Quantization** technique allows qdrant to use different vector encoding algorithm for stored vectors and for queries. Particularly interesting combination is a Binary stored vectors and Scalar quantized queries.
![Asymmetric quantization](https://qdrant.tech/docs/asymmetric-quantization.png)
Asymmetric quantization
This approach maintains storage size and RAM usage similar to binary quantization while offering improved precision. It is beneficial for memory-constrained deployments, or where the bottleneck is disk I/O rather than CPU. This is particularly useful for indexing millions of vectors as it improves precision without sacrificing much because the limitation in such scenarios is disk speed, not CPU. This approach requires less rescoring for the same quality output.
See how to set up Asymmetric Quantization quantization in the [following section](https://qdrant.tech/documentation/guides/quantization/#set-up-asymmetric-quantization)
