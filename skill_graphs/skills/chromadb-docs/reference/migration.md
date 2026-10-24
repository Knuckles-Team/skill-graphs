# Migration
Source: https://docs.trychroma.com/docs/overview/migration

Migration guides for Chroma version upgrades and schema changes.

Schema and data format changes are a necessary evil of evolving software. We take changes seriously and make them infrequently and only when necessary.

Chroma's commitment is whenever schema or data format change, we will provide a seamless and easy-to-use migration tool to move to the new schema/format.

Specifically we will announce schema changes on:

* Discord ([#migrations channel](https://discord.com/channels/1073293645303795742/1129286514845691975))
* Github ([here](https://github.com/chroma-core/chroma/issues))
* Email listserv [Sign up](https://airtable.com/shrHaErIs1j9F97BE)

We will aim to provide:

* a description of the change and the rationale for the change.
* a CLI migration tool you can run
* a video walkthrough of using the tool

## Migration Log

### v1.0.0 - March 1, 2025

In this release, we've rewritten much of Chroma in Rust. Performance has significantly improved across the board.

**Breaking changes**

Chroma no longer provides built-in authentication implementations.

`list_collections` now reverts back to returning `Collection` objects.

**Chroma in-process changes**

This section is applicable to you if you use Chroma via

```python theme={null}
import chromadb

client = chromadb.Client()
