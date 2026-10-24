# Or for async usage:
async def main():
    client = await chromadb.AsyncHttpClient(host='localhost', port=8000)
```

Note that the `chromadb-client` package is a subset of the full Chroma library and does not include all the dependencies. If you want to use the full Chroma library, you can install the `chromadb` package instead.

Most importantly, the thin-client package has no default embedding functions. If you `add()` documents without embeddings, you must have manually specified an embedding function and install the dependencies for it.
