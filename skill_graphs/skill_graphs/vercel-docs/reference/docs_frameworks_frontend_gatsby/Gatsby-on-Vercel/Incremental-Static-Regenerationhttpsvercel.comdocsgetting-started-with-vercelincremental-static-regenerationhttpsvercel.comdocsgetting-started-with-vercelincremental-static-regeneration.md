##  [Incremental Static Regeneration](https://vercel.com/docs/getting-started-with-vercel#incremental-static-regeneration)[](https://vercel.com/docs/getting-started-with-vercel#incremental-static-regeneration)
Gatsby supports [Deferred Static Generation](https://vercel.com/docs/getting-started-with-vercel#deferred-static-generation).
The static rendered fallback pages are not generated at build time. This differentiates it from incremental static regeneration (ISR). Instead, a Vercel Function gets invoked upon page request. And the resulting response gets cached for 10 minutes. This is hard-coded and currently not configurable.
See the documentation for [Deferred Static Generation](https://vercel.com/docs/getting-started-with-vercel#deferred-static-generation).
