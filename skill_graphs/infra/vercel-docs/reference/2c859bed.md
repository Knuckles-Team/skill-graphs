##  [Unsupported APIs](https://vercel.com/docs/functions/runtimes/node-js#unsupported-apis)[](https://vercel.com/docs/functions/runtimes/node-js#unsupported-apis)
The Edge runtime has some restrictions including:
  * Some Node.js APIs other than the ones listed above are not supported. For example, you can't read or write to the filesystem
  * `node_modules` _can_ be used, as long as they implement ES Modules and do not use native Node.js APIs
  * Calling `require` directly is not allowed. Use `import` instead


The following JavaScript language features are disabled, and will not work:
API | Description
---|---
| Evaluates JavaScript code represented as a string
| Creates a new function with the code provided as an argument
| Compiles a WebAssembly module from a buffer source
| Compiles and instantiates a WebAssembly module from a buffer source
While `WebAssembly.instantiate` is supported in Edge Runtime, it requires the Wasm source code to be provided using the import statement. This means you cannot use a buffer or byte array to dynamically compile the module at runtime.
