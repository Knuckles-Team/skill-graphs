##  [Compatible Node.js modules](https://vercel.com/docs/functions/runtimes/node-js#compatible-node.js-modules)[](https://vercel.com/docs/functions/runtimes/node-js#compatible-node.js-modules)
The following modules can be imported with and without the `node:` prefix when using the `import` statement:
Module | Description
---|---
| Manage asynchronous resources lifecycles with `AsyncLocalStorage`. Supports the
| Facilitate event-driven programming with custom event emitters and listeners. This API is fully supported
| Efficiently manipulate binary data using fixed-size, raw memory allocations with `Buffer`. Every primitive compatible with `Uint8Array` accepts `Buffer` too
| Provide a set of assertion functions for verifying invariants in your code
| Offer various utility functions where we include `promisify`/`callbackify` and `types`
Also, `Buffer` is globally exposed to maximize compatibility with existing Node.js modules.
