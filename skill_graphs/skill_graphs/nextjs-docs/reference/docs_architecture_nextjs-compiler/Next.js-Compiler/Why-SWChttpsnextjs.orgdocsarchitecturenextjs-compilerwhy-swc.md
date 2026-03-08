## Why SWC?[](https://nextjs.org/docs/architecture/nextjs-compiler#why-swc)
SWC can be used for compilation, minification, bundling, and more – and is designed to be extended. It's something you can call to perform code transformations (either built-in or custom). Running those transformations happens through higher-level tools like Next.js.
We chose to build on SWC for a few reasons:
  * **Extensibility:** SWC can be used as a Crate inside Next.js, without having to fork the library or workaround design constraints.
  * **Performance:** We were able to achieve ~3x faster Fast Refresh and ~5x faster builds in Next.js by switching to SWC, with more room for optimization still in progress.
  * **WebAssembly:** Rust's support for WASM is essential for supporting all possible platforms and taking Next.js development everywhere.
  * **Community:** The Rust community and ecosystem are amazing and still growing.
