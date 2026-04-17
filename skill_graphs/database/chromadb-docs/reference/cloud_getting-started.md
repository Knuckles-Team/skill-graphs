[Skip to main content](https://docs.trychroma.com/cloud/getting-started#content-area)
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
Search...
Ctrl KAsk AI
  * [Dashboard](https://trychroma.com/login)
  * [Dashboard](https://trychroma.com/login)


Search...
Navigation
Chroma Cloud
[](https://docs.trychroma.com/docs/overview/introduction)[](https://docs.trychroma.com/cloud/getting-started)[](https://docs.trychroma.com/guides/build/building-with-ai)[](https://docs.trychroma.com/integrations/chroma-integrations)[](https://docs.trychroma.com/reference/overview)
  * [Getting Started](https://docs.trychroma.com/cloud/getting-started)


  * [Pricing](https://docs.trychroma.com/cloud/pricing)


  * [Quotas & Limits](https://docs.trychroma.com/cloud/quotas-limits)


##### Features
  * [Collection Forking](https://docs.trychroma.com/cloud/features/collection-forking)


##### Schema
  * [Schema Overview](https://docs.trychroma.com/cloud/schema/overview)
  * [Schema Basics](https://docs.trychroma.com/cloud/schema/schema-basics)
  * [Sparse Vector Search Setup](https://docs.trychroma.com/cloud/schema/sparse-vector-search)
  * [Index Configuration Reference](https://docs.trychroma.com/cloud/schema/index-reference)


##### Search API
  * [Overview](https://docs.trychroma.com/cloud/search-api/overview)
  * [Search Basics](https://docs.trychroma.com/cloud/search-api/search-basics)
  * [Filtering with Where](https://docs.trychroma.com/cloud/search-api/filtering)
  * [Ranking and Scoring](https://docs.trychroma.com/cloud/search-api/ranking)
  * [Group By & Aggregation](https://docs.trychroma.com/cloud/search-api/group-by)
  * [Hybrid Search with RRF](https://docs.trychroma.com/cloud/search-api/hybrid-search)
  * [Pagination & Selection](https://docs.trychroma.com/cloud/search-api/pagination-selection)
  * [Batch Operations](https://docs.trychroma.com/cloud/search-api/batch-operations)
  * [Examples & Patterns](https://docs.trychroma.com/cloud/search-api/examples)
  * [Migration Guide](https://docs.trychroma.com/cloud/search-api/migration)


##### Sync
  * [Overview](https://docs.trychroma.com/cloud/sync/overview)
  * [S3 Sync](https://docs.trychroma.com/cloud/sync/s3)
  * [GitHub](https://docs.trychroma.com/cloud/sync/github)
  * [Web Sync](https://docs.trychroma.com/cloud/sync/web)


##### Package Search
  * [MCP](https://docs.trychroma.com/cloud/package-search/mcp)
  * [Registry](https://docs.trychroma.com/cloud/package-search/registry)


On this page
  * [Easy to use and operate](https://docs.trychroma.com/cloud/getting-started#easy-to-use-and-operate)
  * [Reliability](https://docs.trychroma.com/cloud/getting-started#reliability)
  * [Security and Deployment](https://docs.trychroma.com/cloud/getting-started#security-and-deployment)
  * [Dashboard](https://docs.trychroma.com/cloud/getting-started#dashboard)
  * [Advanced Search API](https://docs.trychroma.com/cloud/getting-started#advanced-search-api)


# Chroma Cloud
Copy page
Copy page
Our fully managed hosted service, **Chroma Cloud** is here. [Sign up for free](https://trychroma.com/signup?utm_source=docs-getting-started). **Chroma Cloud** is a managed offering of [Distributed Chroma](https://docs.trychroma.com/docs/overview/architecture), operated by the same database and search engineers who designed the system. Under the hood, it’s the exact same Apache 2.0-licensed Chroma-no forks, no divergence, just the open-source engine running at scale. Chroma Cloud is serverless - you don’t have to provision servers or think about operations, and is billed [based on usage](https://docs.trychroma.com/cloud/pricing)
###
[​](https://docs.trychroma.com/cloud/getting-started#easy-to-use-and-operate)
Easy to use and operate
Chroma Cloud is designed to require minimal configuration while still delivering top-tier performance, scale, and reliability. You can get started in under 30 seconds, and as your workload grows, Chroma Cloud handles scaling automatically-no tuning, provisioning, or operations required. Its architecture is built around a custom Rust-based execution engine and high-performance vector and full-text indexes, enabling fast query performance even under heavy loads.
###
[​](https://docs.trychroma.com/cloud/getting-started#reliability)
Reliability
Reliability and accuracy are core to the design. Chroma Cloud is thoroughly tested, with production systems achieving over 90% recall and being continuously monitored for correctness. Thanks to its object storage-based persistence layer, Chroma Cloud is often an order of magnitude more cost-effective than alternatives, without compromising on performance or durability.
###
[​](https://docs.trychroma.com/cloud/getting-started#security-and-deployment)
Security and Deployment
Chroma Cloud is SOC 2 Type II certified, and offers deployment flexibility to match your needs. You can sign up for our fully-managed multi-tenant cluster currently running in AWS us-east-1 or contact us for single-tenant deployment managed by Chroma or hosted in your own VPC (BYOC). If you ever want to self-host open source Chroma, we will help you transition your data from Cloud to your self-managed deployment.
###
[​](https://docs.trychroma.com/cloud/getting-started#dashboard)
Dashboard
Our web dashboard lets your team work together to view your data, and ensure data quality in your collections with ease. It also serves as a touchpoint for you to view billing data and usage telemetry.
###
[​](https://docs.trychroma.com/cloud/getting-started#advanced-search-api)
Advanced Search API
Chroma Cloud introduces a powerful [Search API](https://docs.trychroma.com/cloud/search-api/overview) that enables hybrid search with advanced filtering, custom ranking expressions, and batch operations. Combine vector similarity with metadata filtering using an intuitive builder pattern or flexible dictionary syntax. Chroma Cloud is open-source at its core, built on the exact same Apache 2.0 codebase available to everyone. Whether you’re building a prototype or running a mission-critical production workload, Chroma Cloud is the fastest path to reliable, scalable, and accurate retrieval.
Was this page helpful?
YesNo
[ Pricing Next ](https://docs.trychroma.com/cloud/pricing)
Ctrl+I
[Chroma Docs home page![light logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/light-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=4d021170bd60f2e52fcb7bc0d3eb0552)![dark logo](https://mintcdn.com/chroma-8943dec5/wr97NKZIObCJm0cR/images/dark-logo.svg?fit=max&auto=format&n=wr97NKZIObCJm0cR&q=85&s=a6f162fa88876846a979771be29f2a13)](https://docs.trychroma.com/)
[Enterprise](https://trychroma.com/enterprise)[Pricing](https://trychroma.com/pricing)[Changelog](https://trychroma.com/changelog)
Assistant
Responses are generated using AI and may contain mistakes.
