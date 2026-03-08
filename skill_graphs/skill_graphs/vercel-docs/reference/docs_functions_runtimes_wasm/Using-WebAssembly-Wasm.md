# Using WebAssembly (Wasm)
Last updated December 8, 2025
_alongside_ JavaScript, so that it runs in most JavaScript virtual machines.
With Vercel, you can use Wasm in [Vercel Functions](https://vercel.com/docs/functions) or [Routing Middleware](https://vercel.com/docs/routing-middleware) when the runtime is set to [`edge`](https://vercel.com/docs/functions/runtimes/edge), [`nodejs`](https://vercel.com/docs/functions/runtimes/node-js), or [`bun`](https://vercel.com/docs/functions/runtimes/bun#configuring-the-runtime).
Pre-compiled WebAssembly can be imported with the `?module` suffix. This will provide an array of the Wasm data that can be instantiated using `WebAssembly.instantiate()`.
While `WebAssembly.instantiate` is supported in Edge Runtime, it requires the Wasm source code to be provided using the import statement. This means you cannot use a buffer or byte array to dynamically compile the module at runtime.
