[Skip to main content](https://docs.trychroma.com/docs/overview/architecture#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
Overview
Architecture
[](https://docs.trychroma.com/docs/overview/introduction)[](https://docs.trychroma.com/cloud/getting-started)[](https://docs.trychroma.com/guides/build/building-with-ai)[](https://docs.trychroma.com/integrations/chroma-integrations)[](https://docs.trychroma.com/reference/overview)
##### Overview
  * [Introduction](https://docs.trychroma.com/docs/overview/introduction)
  * [Getting Started](https://docs.trychroma.com/docs/overview/getting-started)
  * [Architecture](https://docs.trychroma.com/docs/overview/architecture)
  * [Open Source](https://docs.trychroma.com/docs/overview/oss)
  * [Migration](https://docs.trychroma.com/docs/overview/migration)
  * [Troubleshooting](https://docs.trychroma.com/docs/overview/troubleshooting)


##### Run Chroma
  * [Chroma Clients](https://docs.trychroma.com/docs/run-chroma/clients)
  * [Client-Server Mode](https://docs.trychroma.com/docs/run-chroma/client-server)


##### Collections
  * [Manage Collections](https://docs.trychroma.com/docs/collections/manage-collections)
  * [Add Data](https://docs.trychroma.com/docs/collections/add-data)
  * [Update Data](https://docs.trychroma.com/docs/collections/update-data)
  * [Delete Data](https://docs.trychroma.com/docs/collections/delete-data)
  * [Configure Collections](https://docs.trychroma.com/docs/collections/configure)


##### Querying Collections
  * [Query and Get](https://docs.trychroma.com/docs/querying-collections/query-and-get)
  * [Metadata Filtering](https://docs.trychroma.com/docs/querying-collections/metadata-filtering)
  * [Full Text Search](https://docs.trychroma.com/docs/querying-collections/full-text-search)


##### Embeddings
  * [Embedding Functions](https://docs.trychroma.com/docs/embeddings/embedding-functions)
  * [Multimodal Embeddings](https://docs.trychroma.com/docs/embeddings/multimodal)


##### CLI
  * [Installing the CLI](https://docs.trychroma.com/docs/cli/install)
  * [Browse Collections](https://docs.trychroma.com/docs/cli/browse)
  * [Copy Collections](https://docs.trychroma.com/docs/cli/copy)
  * [DB Management](https://docs.trychroma.com/docs/cli/db)
  * [Sample Apps](https://docs.trychroma.com/docs/cli/sample-apps)
  * [Login](https://docs.trychroma.com/docs/cli/login)
  * [Profile Management](https://docs.trychroma.com/docs/cli/profile)
  * [Run a Chroma Server](https://docs.trychroma.com/docs/cli/run)
  * [Update](https://docs.trychroma.com/docs/cli/update)
  * [Vacuum](https://docs.trychroma.com/docs/cli/vacuum)


On this page
  * [Deployment Modes](https://docs.trychroma.com/docs/overview/architecture#deployment-modes)
  * [Core Components](https://docs.trychroma.com/docs/overview/architecture#core-components)
  * [The Gateway](https://docs.trychroma.com/docs/overview/architecture#the-gateway)
  * [The Log](https://docs.trychroma.com/docs/overview/architecture#the-log)
  * [The Query Executor](https://docs.trychroma.com/docs/overview/architecture#the-query-executor)
  * [The Compactor](https://docs.trychroma.com/docs/overview/architecture#the-compactor)
  * [The System Database](https://docs.trychroma.com/docs/overview/architecture#the-system-database)
  * [Storage & Runtime](https://docs.trychroma.com/docs/overview/architecture#storage-%26-runtime)
  * [Request Sequences](https://docs.trychroma.com/docs/overview/architecture#request-sequences)
  * [Read Path](https://docs.trychroma.com/docs/overview/architecture#read-path)
  * [Write Path](https://docs.trychroma.com/docs/overview/architecture#write-path)
  * [Tradeoffs](https://docs.trychroma.com/docs/overview/architecture#tradeoffs)
  * [Chroma Data Model](https://docs.trychroma.com/docs/overview/architecture#chroma-data-model)
  * [Collections](https://docs.trychroma.com/docs/overview/architecture#collections)
  * [Databases](https://docs.trychroma.com/docs/overview/architecture#databases)
  * [Tenants](https://docs.trychroma.com/docs/overview/architecture#tenants)


Overview
# Architecture
Copy page
Chroma is designed with a modular architecture that prioritizes performance and ease of use. It scales seamlessly from local development to large-scale production, while exposing a consistent API across all deployment modes.
Copy page
Chroma is designed with a modular architecture that prioritizes performance and ease of use. It scales seamlessly from local development to large-scale production, while exposing a consistent API across all deployment modes. Chroma delegates, as much as possible, problems of data durability to trusted sub-systems such as SQLite and Cloud Object Storage, focusing the system design on core problems of data management and information retrieval.
##
[​](https://docs.trychroma.com/docs/overview/architecture#deployment-modes)
Deployment Modes
Chroma runs wherever you need it to, supporting you in everything from local experimentation, to large scale production workloads.
  * **Local** : as an embedded library - great for prototyping and experimentation.
  * **Single Node** : as a single-node server - great for small to medium scale workloads of < 10M records in a handful of collections.
  * **Distributed** : as a scalable distributed system - great for large scale production workloads, supporting millions of collections.

You can use [Chroma Cloud](https://www.trychroma.com/signup?utm_source=docs-architecture), which is a managed offering of distributed Chroma.
##
[​](https://docs.trychroma.com/docs/overview/architecture#core-components)
Core Components
Regardless of deployment mode, Chroma is composed of five core components. Each plays a distinct role in the system and operates over the shared [Chroma data model](https://docs.trychroma.com/docs/overview/architecture#chroma-data-model). ![Chroma System architecture](https://mintcdn.com/chroma-8943dec5/2QFLJScSYa9JT1WU/images/system-diagram-light.png?fit=max&auto=format&n=2QFLJScSYa9JT1WU&q=85&s=8230cb5c91cdfb4f17336accd059d2e7) ![Chroma System architecture](https://mintcdn.com/chroma-8943dec5/2QFLJScSYa9JT1WU/images/system-diagram-dark.png?fit=max&auto=format&n=2QFLJScSYa9JT1WU&q=85&s=3b27d74ee4a3f1c58a6d0c38e41ab40b)
###
[​](https://docs.trychroma.com/docs/overview/architecture#the-gateway)
The Gateway
The entrypoint for all client traffic.
  * Exposes a consistent API across all modes.
  * Handles authentication, rate-limiting, quota management, and request validation.
  * Routes requests to downstream services.


###
[​](https://docs.trychroma.com/docs/overview/architecture#the-log)
The Log
Chroma’s write-ahead log.
  * All writes are recorded here before acknowledgment to clients.
  * Ensures atomicity across multi-record writes.
  * Provides durability and replay in distributed deployments.


###
[​](https://docs.trychroma.com/docs/overview/architecture#the-query-executor)
The Query Executor
Responsible for **all read operations.**
  * Vector similarity, full-text and metadata search.
  * Maintains a combination of in-memory and on-disk indexes, and coordinates with the Log to serve consistent results.


###
[​](https://docs.trychroma.com/docs/overview/architecture#the-compactor)
The Compactor
A service that periodically builds and maintains indexes.
  * Reads from the Log and builds updated vector / full-text / metadata indexes.
  * Writes materialized index data to shared storage.
  * Updates the System Database with metadata about new index versions.


###
[​](https://docs.trychroma.com/docs/overview/architecture#the-system-database)
The System Database
Chroma’s internal catalog.
  * Tracks tenants, collections, and their metadata.
  * In distributed mode, also manages cluster state (e.g., query/compactor node membership).
  * Backed by a SQL database.


##
[​](https://docs.trychroma.com/docs/overview/architecture#storage-&-runtime)
Storage & Runtime
These components operate differently depending on the deployment mode, particularly in how they use storage and the runtime they operate in.
  * In Local and Single Node mode, all components share a process and use the local filesystem for durability.
  * In **Distributed** mode, components are deployed as independent services.
    * The log and built indexes are stored in cloud object storage.
    * The system catalog is backed by a SQL database.
    * All services use local SSDs as caches to reduce object storage latency and cost.


##
[​](https://docs.trychroma.com/docs/overview/architecture#request-sequences)
Request Sequences
###
[​](https://docs.trychroma.com/docs/overview/architecture#read-path)
Read Path
![Chroma System Read Path](https://mintcdn.com/chroma-8943dec5/OHTRZei6ss2glLVb/images/read-path-light.png?fit=max&auto=format&n=OHTRZei6ss2glLVb&q=85&s=cac0a618b57dc23bc15ec2387d4bcac2) ![Chroma System Read Path](https://mintcdn.com/chroma-8943dec5/OHTRZei6ss2glLVb/images/read-path-dark.png?fit=max&auto=format&n=OHTRZei6ss2glLVb&q=85&s=99899a7f7817339bd4e7a1e410b845cf)
1
[](https://docs.trychroma.com/docs/overview/architecture)
Request arrives at the gateway, where it is authenticated, checked against quota limits, rate limited and transformed into a logical plan.
2
[](https://docs.trychroma.com/docs/overview/architecture)
This logical plan is routed to the relevant query executor. In distributed Chroma, a rendezvous hash on the collection id is used to route the query to the correct nodes and provide cache coherence.
3
[](https://docs.trychroma.com/docs/overview/architecture)
The query executor transforms the logical plan into a physical plan for execution, reads from its storage layer, and performs the query. The query executor pulls data from the log to ensure a consistent read.
4
[](https://docs.trychroma.com/docs/overview/architecture)
The request is returned to the gateway and subsequently to the client.
###
[​](https://docs.trychroma.com/docs/overview/architecture#write-path)
Write Path
![Chroma System Write Path](https://mintcdn.com/chroma-8943dec5/2QFLJScSYa9JT1WU/images/write-path-light.png?fit=max&auto=format&n=2QFLJScSYa9JT1WU&q=85&s=a791ab900059c0d1592050a45ea98578) ![Chroma System Write Path](https://mintcdn.com/chroma-8943dec5/2QFLJScSYa9JT1WU/images/write-path-dark.png?fit=max&auto=format&n=2QFLJScSYa9JT1WU&q=85&s=f9dc0b3dd158e83e9f7d6d2f1cbc2e18)
1
[](https://docs.trychroma.com/docs/overview/architecture)
Request arrives at the gateway, where it is authenticated, checked against quota limits, rate limited and then transformed into a log of operations.
2
[](https://docs.trychroma.com/docs/overview/architecture)
The log of operations is forwarded to the write-ahead-log for persistence.
3
[](https://docs.trychroma.com/docs/overview/architecture)
After being persisted by the write-ahead-log, the gateway acknowledges the write.
4
[](https://docs.trychroma.com/docs/overview/architecture)
The compactor periodically pulls from the write-ahead-log and builds new index versions from the accumulated writes. These indexes are optimized for read performance and include vector, full-text, and metadata indexes.
5
[](https://docs.trychroma.com/docs/overview/architecture)
Once new index versions are built, they are written to storage and registered in the system database.
##
[​](https://docs.trychroma.com/docs/overview/architecture#tradeoffs)
Tradeoffs
Distributed Chroma is built on object storage in order to ensure the durability of your data and to deliver low costs. Object storage has extremely high throughput, easily capable of saturating a single nodes network bandwidth, but this comes at the cost of a relatively high latency floor of ~10-20ms. In order to reduce the overhead of this latency floor, Distributed Chroma aggressively leverage SSD caching. When you first query a collection, a subset of the data needed to answer the query will be read selectively from object storage, incurring a cold-start latency penalty. In the background, the SSD cache will be loaded with the data for the collection. After the collection is fully warm, queries will be served entirely from SSD.
##
[​](https://docs.trychroma.com/docs/overview/architecture#chroma-data-model)
Chroma Data Model
Chroma’s data model is designed to balance simplicity, flexibility, and scalability. It introduces a few core abstractions - **Tenants** , **Databases** , and **Collections** - that allow you to organize, retrieve, and manage data efficiently across environments and use cases.
###
[​](https://docs.trychroma.com/docs/overview/architecture#collections)
Collections
A **collection** is the fundamental unit of storage and querying in Chroma. Each collection contains a set of items, where each item consists of:
  * An ID uniquely identifying the item
  * An **embedding vector**
  * Optional **metadata** (key-value pairs)
  * A document that belongs to the provided embedding

Collections are independently indexed and are optimized for fast retrieval using **vector similarity** , **full-text search** , and **metadata filtering**. In distributed deployments, collections can be sharded or migrated across nodes as needed; the system transparently manages paging them in and out of memory based on access patterns.
###
[​](https://docs.trychroma.com/docs/overview/architecture#databases)
Databases
Collections are grouped into **databases** , which serve as a logical namespace. This is useful for organizing collections by purpose - for example, separating environments like “staging” and “production”, or grouping applications under a common schema. Each database contains multiple collections, and each collection name must be unique within a database.
###
[​](https://docs.trychroma.com/docs/overview/architecture#tenants)
Tenants
At the top level of the model is the **tenant** , which represents a single user, team, or account. Tenants provide complete isolation. No data or metadata, is shared across tenants. All access control, quota enforcement, and billing are scoped to the tenant level.
Was this page helpful?
YesNo
[ Getting Started Previous ](https://docs.trychroma.com/docs/overview/getting-started)[ Open Source Next ](https://docs.trychroma.com/docs/overview/oss)
Ctrl+I
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
[Enterprise](https://trychroma.com/enterprise)[Pricing](https://trychroma.com/pricing)[Changelog](https://trychroma.com/changelog)
Assistant
Responses are generated using AI and may contain mistakes.
![Chroma System architecture](https://mintcdn.com/chroma-8943dec5/2QFLJScSYa9JT1WU/images/system-diagram-light.png?w=840&fit=max&auto=format&n=2QFLJScSYa9JT1WU&q=85&s=bfd8f1cfa19aeaf6ff48ebbe3482e76f)
![Chroma System Read Path](https://mintcdn.com/chroma-8943dec5/OHTRZei6ss2glLVb/images/read-path-light.png?w=840&fit=max&auto=format&n=OHTRZei6ss2glLVb&q=85&s=024cfd507c3a1b6a685de71120a47cc2)
![Chroma System Write Path](https://mintcdn.com/chroma-8943dec5/2QFLJScSYa9JT1WU/images/write-path-light.png?w=840&fit=max&auto=format&n=2QFLJScSYa9JT1WU&q=85&s=f0d5c3755e2f196aa4f377775a61c33a)
