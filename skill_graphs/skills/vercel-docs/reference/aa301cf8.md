##  [Which should you use?](https://vercel.com/docs/flags/vercel-flags/sdks#which-should-you-use)[](https://vercel.com/docs/flags/vercel-flags/sdks#which-should-you-use)
Use the Flags SDK if you're building with Next.js or SvelteKit. It provides the best developer experience with automatic integration for Flags Explorer, precompute for static pages, and framework-specific optimizations.
Use OpenFeature if you need a vendor-neutral API that allows switching between flag providers without code changes, or if you're already using OpenFeature in your stack.
Use the Core Library if you're working outside of supported frameworks, building custom tooling, or need direct access to the evaluation engine.
