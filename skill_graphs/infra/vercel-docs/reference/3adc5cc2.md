##  [Choosing a storage solution](https://vercel.com/docs/marketplace-storage#choosing-a-storage-solution)[](https://vercel.com/docs/marketplace-storage#choosing-a-storage-solution)
Consider these factors when selecting a storage provider:
Factor | Considerations
---|---
Data model | Relational (Postgres) for structured data, key-value (Redis) for caching, NoSQL for flexible schemas, vector for AI embeddings
Common use cases | Postgres for ACID transactions, complex queries, and foreign keys. Redis for session storage, rate limiting, and leaderboards. Vector for semantic search and recommendations. NoSQL for document storage, high write throughput, and horizontal scaling
Latency requirements | Choose providers with regions close to your [Functions](https://vercel.com/docs/functions/configuring-functions/region)
Scale | Evaluate pricing tiers and scaling capabilities for your expected workload
Features | Compare provider-specific features like branching, point-in-time recovery, or real-time subscriptions
