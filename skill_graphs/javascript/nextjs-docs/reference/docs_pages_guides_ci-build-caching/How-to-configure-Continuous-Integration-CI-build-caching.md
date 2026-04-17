# How to configure Continuous Integration (CI) build caching
Last updated February 27, 2026
To improve build performance, Next.js saves a cache to `.next/cache` that is shared between builds.
To take advantage of this cache in Continuous Integration (CI) environments, your CI workflow will need to be configured to correctly persist the cache between builds.
> If your CI is not configured to persist `.next/cache` between builds, you may see a [No Cache Detected](https://nextjs.org/docs/messages/no-cache) error.
Here are some example cache configurations for common CI providers:
