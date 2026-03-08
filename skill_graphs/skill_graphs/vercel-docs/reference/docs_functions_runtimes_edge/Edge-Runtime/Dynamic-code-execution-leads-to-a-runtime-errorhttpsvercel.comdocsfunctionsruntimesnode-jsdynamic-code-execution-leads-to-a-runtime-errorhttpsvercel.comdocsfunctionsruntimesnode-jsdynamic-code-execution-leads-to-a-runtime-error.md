##  [Dynamic code execution leads to a runtime error](https://vercel.com/docs/functions/runtimes/node-js#dynamic-code-execution-leads-to-a-runtime-error)[](https://vercel.com/docs/functions/runtimes/node-js#dynamic-code-execution-leads-to-a-runtime-error)
Dynamic code execution is not available in Middleware with the `edge` runtime configured for security reasons. For example, the following APIs cannot be used:
API | Description
---|---
| Evaluates JavaScript code represented as a string
| Creates a new function with the code provided as an argument
| Compiles and instantiates a WebAssembly module from a buffer source
You need to make sure libraries used in your Middleware with the `edge` runtime configured don't rely on dynamic code execution because it leads to a runtime error.
