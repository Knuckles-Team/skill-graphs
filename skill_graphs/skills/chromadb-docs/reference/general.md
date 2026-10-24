# General
Source: https://docs.trychroma.com/guides/performance/general

How to improve Chroma performance across single-node and distributed deployments.

## Python Thin Client

If you are running Chroma in client-server mode in a Python application, you may not need the full Chroma library. Instead, you can use the lightweight client-only library.

In this case, you can install the `chromadb-client` package **instead** of our `chromadb` package.

The `chromadb-client` package is a lightweight HTTP client for the server with a minimal dependency footprint.

<CodeGroup>
  ```terminal pip theme={null}
  pip install chromadb-client
  ```

  ```terminal poetry theme={null}
  poetry add chromadb-client
  ```

  ```terminal uv theme={null}
  uv pip install chromadb-client
  ```
</CodeGroup>

```python theme={null}
