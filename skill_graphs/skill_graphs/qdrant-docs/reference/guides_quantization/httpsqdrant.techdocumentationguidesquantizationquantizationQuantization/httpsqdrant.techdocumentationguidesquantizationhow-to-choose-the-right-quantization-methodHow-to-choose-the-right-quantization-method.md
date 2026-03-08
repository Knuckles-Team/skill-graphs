##  [](https://qdrant.tech/documentation/guides/quantization/#how-to-choose-the-right-quantization-method)How to choose the right quantization method
Here is a brief table of the pros and cons of each quantization method:
Quantization method | Accuracy | Speed | Compression
---|---|---|---
Scalar | 0.99 | up to x2 | 4
Product | 0.7 | 0.5 | up to 64
Binary (1 bit) | 0.95* | up to x40 | 32
Binary (1.5 bit) | 0.95** | up to x30 | 24
Binary (2 bit) | 0.95*** | up to x20 | 16
  * `*` - for compatible models with high-dimensional vectors (approx. 1536+ dimensions)
  * `**` - for compatible models with medium-dimensional vectors (approx. 1024-1536 dimensions)
  * `***` - for compatible models with low-dimensional vectors (approx. 768-1024 dimensions)
  * **Binary Quantization** is the fastest method and the most memory-efficient, but it requires a centered distribution of vector components. It is recommended to use with tested models only.
    * If you are planning to use binary quantization with low or medium-dimensional vectors (approx. 512-1024 dimensions), it is recommended to use 1.5-bit or 2-bit quantization as well as asymmetric quantization feature.
  * **Scalar Quantization** is the most universal method, as it provides a good balance between accuracy, speed, and compression. It is recommended as default quantization if binary quantization is not applicable.
  * **Product Quantization** may provide a better compression ratio, but it has a significant loss of accuracy and is slower than scalar quantization. It is recommended if the memory footprint is the top priority and the search speed is not critical.
