#  Vercel Pinecone Integration
Connectable Account
Last updated November 25, 2025
is a [vector database](https://vercel.com/kb/guide/vector-databases) service that handles the storage and search of complex data. With Pinecone, you can use machine-learning models for content recommendation systems, personalized search, image recognition, and more. The Vercel Pinecone integration allows you to deploy your models to Vercel and use them in your applications.
### What is a vector database?
A vector database is a database that stores and searches for vectors. In this context, a vector represents a data point mathematically, often termed as an embedding.
An embedding is data that's converted to an array of numbers (a vector). The combination of the numbers that make up the vector form a multi-dimensional map used in comparison to other vectors to determine similarity.
Take the below example of two vectors, one for an image of a cat and one for an image of a dog. In the cat's vector, the first element is `0.1`, and in the dog's vector `0.2`. This similarity and difference in values illustrate how vector comparison works. The closer the values are to each other, the more similar the vectors are.
vectors
```
// Example of a vector for an image of a cat
[0.1, 0.2, 0.3, 0.4, 0.5];
// Example of a vector for an image of a dog
[(0.2, 0.3, 0.4, 0.5, 0.6)];
```
