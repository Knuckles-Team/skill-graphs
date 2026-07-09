# use cache: remote
Last updated February 27, 2026
While the `use cache` directive is sufficient for most application needs, you might notice that cached operations are re-running more often than expected, or that your upstream services (CMS, databases, external APIs) are getting more hits than you'd expect. This can happen because `use cache` stores entries in-memory, which has inherent limitations:
  * Cache entries being evicted to make room for new ones
  * Memory constraints in your deployment environment
  * Cache not persisting across requests or server restarts


Note that `use cache` still provides value beyond server-side caching: it informs Next.js what can be prefetched and defines stale times for client-side navigation.
The `'use cache: remote'` directive lets you declaratively specify that a cached output should be stored in a remote cache instead of in-memory, providing durable caching shared across all server instances. This comes with tradeoffs: infrastructure cost and network latency during cache lookups.
