# NO_MIXED_ASYNC_MODULES
Last updated July 18, 2025
Conformance is available on [Enterprise plans](https://vercel.com/docs/plans/enterprise)
Top-level await expressions in modules that are imported by other modules in sync prevent possible lazy module optimizations from being deployed on the module containing the top-level await.
One such optimization this prevents is inline lazy imports. Inline lazy imports allow for modules to be lazily evaluated and executed when they're used, rather than at initialization time of the module that uses them, improving initialization performance.
This is particularly impactful for modules that might only be used conditionally or given a user's interaction which might happen much latter in an application. Without this optimization, the module initialization times, such as for cold boots on Vercel Functions, could be slowed down for every request.
