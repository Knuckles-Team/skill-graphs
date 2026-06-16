# Concepts

Chroma Sync has three primary concepts: **source types**, **sources**, and **invocations**.

A **source type** defines a kind of entity that can be chunked, embedded, and indexed (e.g. S3, GitHub, Web, File Upload). A **source** is a configured instance of a source type — for example, a specific S3 bucket with credentials and a path prefix. An **invocation** is one sync run over a source's data; each invocation produces or appends to one Chroma collection.
