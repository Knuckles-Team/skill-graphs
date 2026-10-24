##  [Built-in resilience](https://vercel.com/docs/flags/vercel-flags/quickstart#built-in-resilience)[](https://vercel.com/docs/flags/vercel-flags/quickstart#built-in-resilience)
The SDK can fetch your flag definitions once at build time and bundle them into the deployment. This guarantees every function uses the same snapshot during the build, and provides a runtime fallback if the Vercel Flags service is temporarily unreachable.
Embedding is experimental. Enable it by adding a `VERCEL_EXPERIMENTAL_EMBED_FLAG_DEFINITIONS=1` environment variable to your project. This is recommended to avoid downtime during service outages, and will become the default in a future release.
Learn more about [embedded definitions](https://vercel.com/docs/flags/vercel-flags/sdks/core#embedded-definitions).
